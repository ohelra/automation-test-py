import time, os, csv, pytest
from selenium import webdriver
from base_pages.pages.Auth_Pages.Sign_Up_page import SignUpPage
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from utilities.custom_logger import LogMaker
from utilities.sign_up_excel import ExcelReader

BATCH_SIZE = 100                                            # Restart browser one times
CHECKPOINT_FILE = "checkpoint_index.txt"
RESULT_FILE = "sign_up_zipcode_result.csv"
DATA_FILE = "zipcode_usa_canada.xlsx"

@pytest.mark.SignUpZipcode
class TestSignUpZipCode:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        request.cls.testdata = ExcelReader(DATA_FILE)
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()
        self.home_page.click_my_account()

    def go_to_sign_up_step_1(self, sign_up_page):
        self.logger.info("--- Ensuring user is at Step 1 ---")

        if sign_up_page.is_at_info_step():
            self.logger.info("Refreshing to back to Step 1...")
            sign_up_page.refresh_page()
            return

        if sign_up_page.is_at_email_step():
            self.logger.info("Refreshing to clear data...")
            sign_up_page.refresh_page()
            return

        self.logger.info("Not at Sign Up page, click Create Account.")
        sign_up_page.click_create_account()

    @staticmethod
    def get_start_index():                      # checkpoint
        if os.path.exists(CHECKPOINT_FILE):
            with open(CHECKPOINT_FILE, "r") as f:
                try:
                    line = f.readline().strip()
                    if not line:
                        return 0
                    return int(line)
                except ValueError:
                    return 0
        return 0

    @staticmethod
    def save_checkpoint(index):
        with open(CHECKPOINT_FILE, "w") as f:
            f.write(str(index))

    @staticmethod
    def log_result_to_csv(row_index, zipcode, exp_city, act_city, status, error_msg=""):
        file_exists = os.path.exists(RESULT_FILE)
        with open(RESULT_FILE, mode="a", newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Row Index", "ZipCode", "Expected City", "Actual City", "Status", "Error Message"])
            writer.writerow([row_index, zipcode, exp_city, act_city, status, error_msg])

    def restart_browser_session(self):
        self.logger.info("BATCH LIMIT REACHED - RESTARTING DRIVER")
        try:
            if self.driver:
                self.driver.quit()
        except Exception:
            pass

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.home_page = RSPROHomePage(self.driver)
        new_sign_up_page = SignUpPage(self.driver)
        self.home_page.go_to_home()
        self.home_page.click_my_account()
        self.go_to_sign_up_step_1(new_sign_up_page)
        self.set_up_email_password(new_sign_up_page)
        return new_sign_up_page

    def set_up_email_password(self, sign_up_page):
        self.logger.info("Entering valid credentials to go to Step 2...")
        sign_up_page.enter_email("sakanomi123@gmail.com")
        sign_up_page.enter_password("12345678")
        sign_up_page.click_continue_button()
        time.sleep(3)

    def test_verify_valid_zipcode(self):
        self.logger.info("===== Verify Valid Zipcode =====")
        data_list = self.testdata.get_zipcode_data()
        total_rows = len(data_list)
        start_index = self.get_start_index()
        self.logger.info(f"RESUMING TEST FROM ROW: {start_index} / {total_rows}")
        sign_up_page = SignUpPage(self.driver)
        self.go_to_sign_up_step_1(sign_up_page)
        self.set_up_email_password(sign_up_page)
        for i in range(start_index, total_rows):
            row = data_list[i]
            if i > start_index and (i - start_index) % BATCH_SIZE == 0:
                sign_up_page = self.restart_browser_session()
            try:
                zip_code = str(row['PHYSICAL ZIP'])
                expected_city = str(row['PHYSICAL CITY']).strip()
                expected_state = str(row['STATE']).strip()
                sign_up_page.enter_zipcode(zip_code)
                time.sleep(0.5)
                actual_city = sign_up_page.get_city_value()
                actual_state = sign_up_page.get_state_value()
                if actual_city.lower() == expected_city.lower() and actual_state.lower() == expected_state.lower():
                    self.log_result_to_csv(row_index=i + 1, zipcode=zip_code, exp_city=expected_city, act_city=actual_city,status="PASS")
                else:
                    error_msg = f"City mismatch. Exp: {expected_city} - Act: {actual_city}"
                    self.logger.error(f"FAIL Row {i}: {error_msg}")
                    self.log_result_to_csv(row_index=i + 1, zipcode=zip_code, exp_city=expected_city,act_city=actual_city,status="FAIL",error_msg=error_msg)
                self.save_checkpoint(i + 1)
            except Exception as e:
                self.logger.error(f"CRITICAL ERROR at Row {i}: {e}")
                self.log_result_to_csv(row_index=i + 1,zipcode=zip_code if 'zip_code' in locals() else "N/A",exp_city="N/A",act_city="N/A",status="ERROR",error_msg=str(e))
                self.save_checkpoint(i)
