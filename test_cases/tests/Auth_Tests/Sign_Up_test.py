import pytest
from base_pages.pages.Auth_Pages.Sign_Up_page import SignUpPage
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from utilities.custom_logger import LogMaker
from utilities.json_reader import JsonReader

@pytest.mark.SignUp
class TestSignUp:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        request.cls.testdata = JsonReader("sign_up_invalid_email.json")
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

    def set_up_email_password(self, sign_up_page):
        self.logger.info("Entering valid credentials to go to Step 2...")
        sign_up_page.enter_email("sakanomi123@gmail.com")
        sign_up_page.enter_password("12345678")
        sign_up_page.click_continue_button()

    def test_verify_email_exists_with_error_message(self):
        """
            Step by Step:
                 1. Go to Homepage
                 2. Click My Account
                 3. Click Create an Account
                 4. Enter exists email
                 5. Enter exists password
                 6. Verify that the textbox displayed message error
        """
        self.logger.info("===== Verify that user cannot sign up with email exists =====")
        test_data = self.testdata.get_data("exist_email")
        sign_up_page = SignUpPage(self.driver)
        self.go_to_sign_up_step_1(sign_up_page)
        for i, j in enumerate(test_data):
            email_enter = j["email"]
            expected = j["expected"]
            self.logger.info(f"Testing Case {i + 1}: Email: {email_enter}")
            try:
                sign_up_page.enter_email_txb(email_enter)
                self.logger.info(f"Enter email : {email_enter}")
                sign_up_page.enter_password_txb("12345678")
                self.logger.info("Enter password textbox")
                sign_up_page.click_continue_button()
                self.logger.info("Click continue button")
                assert sign_up_page.get_email_existing_error() == expected
                assert not sign_up_page.get_continue_button_enable()
            except Exception as e:
                self.logger.failed("Email does not exist", e)
                self.driver.save_screenshot(".\\screenshots\\test_verify_email_exists_with_error_message.png")
                assert False

    def test_verify_invalid_email_with_error_message(self):
        """
            Step by Step:
                 1. Go to Homepage
                 2. Click My Account
                 3. Click Create an Account
                 4. Enter invalid email
                 5. Enter password
                 6. Verify that the textbox displayed message error
        """
        self.logger.info("===== Verify that user cannot sign up with invalid email =====")
        test_data = self.testdata.get_data("invalid_email")
        sign_up_page = SignUpPage(self.driver)
        self.go_to_sign_up_step_1(sign_up_page)
        for i, j in enumerate(test_data):
            email_invalid = j["email"]
            expected = j["expected"]
            self.logger.info(f"Testing Case {i + 1}: Email: {email_invalid}")
            try:
                sign_up_page.enter_email_txb(email_invalid)
                self.logger.info(f"Enter email : {email_invalid}")
                sign_up_page.enter_password_txb("12345678")
                self.logger.info("Enter password textbox")
                assert sign_up_page.get_email_invalid_error() == expected
                assert not sign_up_page.get_continue_button_enable()
            except Exception as e:
                self.logger.failed("Email valid and go to next step", e)
                self.driver.save_screenshot(".\\screenshots\\test_verify_invalid_email_with_error_message.png")
                assert False

    def test_verify_empty_email_with_error_message(self):
        """
            Step by Step:
                 1. Go to Homepage
                 2. Click My Account
                 3. Click Create an Account
                 4. Enter email textbox
                 5. Enter password textbox
                 7. Clear email textbox
                 6. Verify that the textbox displayed empty message error
        """
        self.logger.info("===== Verify that user cannot sign up with empty email =====")
        sign_up_page = SignUpPage(self.driver)
        self.go_to_sign_up_step_1(sign_up_page)
        self.logger.info("Set up email password and click continue button")
        try:
            sign_up_page.enter_email_txb("shinomiya123@gmail.com")
            self.logger.info("Enter email")
            sign_up_page.enter_password_txb("12345678")
            self.logger.info("Enter password")
            sign_up_page.clear_email_textbox()
            self.logger.info("Clear email textbox")
            assert sign_up_page.get_email_empty_error_message() == "This field can't be empty"
            assert not sign_up_page.get_continue_button_enable()
        except Exception as e:
            self.logger.failed("Ignore the textbox empty and enable continue button", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_empty_email_with_error_message.png")
            assert False

    def test_verify_empty_password_with_error_message(self):
        """
             Step by Step:
                  1. Go to Homepage
                  2. Click My Account
                  3. Click Create an Account
                  4. Enter email textbox
                  5. Enter password textbox
                  7. Clear password textbox
                  6. Verify that the textbox displayed message error
        """
        self.logger.info("===== Verify that user cannot sign up with invalid password =====")
        sign_up_page = SignUpPage(self.driver)
        self.go_to_sign_up_step_1(sign_up_page)
        try:
            sign_up_page.enter_password("123")
            self.logger.info("Enter password")
            sign_up_page.clear_password_textbox()
            self.logger.info("Clear password textbox")
            assert sign_up_page.get_password_message_error() == "This field can't be empty"
            assert not sign_up_page.get_continue_button_enable()
        except Exception as e:
            self.logger.failed("Ignore the textbox empty and enable continue button", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_empty_password_with_error_message.png")
            assert False

    def test_verify_invalid_password_with_error_message(self):
        """
             Step by Step:
                  1. Go to Homepage
                  2. Click My Account
                  3. Click Create an Account
                  4. Enter email textbox
                  5. Enter 3 characters in password textbox
                  7. Clear password textbox
                  6. Verify that the textbox displayed message error
        """
        self.logger.info("===== Verify that user cannot sign up with invalid password =====")
        sign_up_page = SignUpPage(self.driver)
        self.go_to_sign_up_step_1(sign_up_page)
        try:
            sign_up_page.enter_email("yukonomi123@gmail.com")
            self.logger.info("Enter email")
            sign_up_page.enter_password("123")
            self.logger.info(f"Enter invalid password ")
            assert sign_up_page.get_password_message_error() == "At least 8 characters"
            assert not sign_up_page.get_continue_button_enable()
        except Exception as e:
            self.logger.failed("Ignore the textbox empty and enable continue button", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_invalid_password_with_error_message.png")
            assert False

    def test_verify_navigate_to_eula_term_and_privacy_policy(self):
        """
             Step by Step:
                  1. Go to Homepage
                  2. Click My Account
                  3. Click Create an Account
                  4. Enter email and password
                  5. Click EULA link
                  6. Click Privacy Policy link
                  7. Verify that navigate to new tab
        """
        self.logger.info("===== Verify that user can navigate to EULA/Term and Privacy Policy tab =====")
        sign_up_page = SignUpPage(self.driver)
        self.go_to_sign_up_step_1(sign_up_page)
        self.set_up_email_password(sign_up_page)
        self.logger.info("Click EULA/Term link")
        sign_up_page.navigate_new_tab(sign_up_page.click_eula_term_link, "eula",
                              sign_up_page.get_eula_term_text,"Terms of Use & End User License Agreement")
        self.logger.info("Click Privacy Policy")
        sign_up_page.navigate_new_tab(sign_up_page.click_privacy_policy_link,"privacy",
                              sign_up_page.get_privacy_policy_text,"Privacy Policy")


    def test_verify_invalid_zipcode_with_error_message(self):
        """
             Step by Step:
                  1. Go to Homepage
                  2. Click My Account
                  3. Click Create an Account
                  4. Enter email and password
                  5. Enter invalid zipcode
                  6. Verify that the texbox displayed message error
        """
        self.logger.info("===== Verify that user cannot enter with invalid zipcode =====")
        try:
            sign_up_page = SignUpPage(self.driver)
            self.go_to_sign_up_step_1(sign_up_page)
            self.set_up_email_password(sign_up_page)
            sign_up_page.enter_zipcode_invalid("aaaaaa")
            self.logger.info("Enter zipcode invalid")
            assert sign_up_page.get_zipcode_message_error() == "Zipcode is invalid"
        except Exception as e:
            self.logger.failed("Failed invalid zipcode", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_invalid_zipcode_with_error_message.png")
            assert False

    def test_verify_empty_zipcode_with_error_message(self):
        """
                Step by Step:
                     1. Go to Homepage
                     2. Click My Account
                     3. Click Create an Account
                     4. Enter email and password
                     5. Enter zipcode
                     7. Clear zipcode
                     8. Verify that the texbox displayed message error
        """
        self.logger.info("===== Verify that user cannot enter with empty zipcode =====")
        try:
            sign_up_page = SignUpPage(self.driver)
            self.go_to_sign_up_step_1(sign_up_page)
            self.set_up_email_password(sign_up_page)
            sign_up_page.enter_zipcode_invalid("96214")
            self.logger.info("Enter zipcode")
            sign_up_page.clear_zipcode()
            self.logger.info("Clear zipcode")
            assert sign_up_page.get_zipcode_message_error() == "This field can't be empty"
        except Exception as e:
            self.logger.failed("Zipcode textbox does not display message error", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_empty_zipcode_with_error_message.png")
            assert False

    @pytest.mark.parametrize("firstname, lastname, address1, zipcode", [("Akan", "Rotan", "123 abc","96214")])
    def test_verify_empty_fields_information(self, firstname, lastname, address1, zipcode):
        """
            Step by Step:
                  1. Go to Homepage
                  2. Click My Account
                  3. Click Create an Account
                  4. Enter email and password
                  5. Click continue button
                  6. Enter firstname, lastname, address1, zipcode
                  7. Clear all fields
                  8. Verify that the textboxes displayed message error
        """
        self.logger.info("===== Verify that textboxes displayed message error with empty fields =====")
        sign_up_page = SignUpPage(self.driver)
        self.go_to_sign_up_step_1(sign_up_page)
        self.set_up_email_password(sign_up_page)
        try:
            sign_up_page.enter_first_name(firstname)
            self.logger.info("Enter first name")
            sign_up_page.enter_last_name(lastname)
            self.logger.info("Enter last name")
            sign_up_page.enter_address_line_1(address1)
            self.logger.info("Enter address line 1")
            sign_up_page.enter_zipcode(zipcode)
            self.logger.info("Enter zipcode")
            sign_up_page.clear_first_name()
            self.logger.info("Clear first name")
            sign_up_page.clear_last_name()
            self.logger.info("Clear last name")
            sign_up_page.clear_address_line_1()
            self.logger.info("Clear address line 1")
            sign_up_page.clear_zipcode()
            self.logger.info("Clear Zip or Postal Code")
            assert sign_up_page.get_first_name_message_error() == "This field can't be empty"
            assert sign_up_page.get_last_name_message_error() == "This field can't be empty"
            assert sign_up_page.get_address_line_1_message_error() == "This field can't be empty"
            assert sign_up_page.get_zipcode_message_error() == "This field can't be empty"
        except Exception as e:
            self.logger.failed("Textbox does not display error message", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_empty_fields_information.png")


