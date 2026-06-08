import pytest
from base_pages.pages.Auth_Pages.Login import LoginPage
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from utilities.custom_logger import LogMaker
from utilities.json_reader import JsonReader

@pytest.mark.Login
class TestLogin:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        request.cls.testdata = JsonReader("login.json")
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()
        self.home_page.click_my_account()

    @pytest.mark.parametrize("data_key", ["invalid_email", "invalid_password","empty_fields","sensitivity","sql_injection"])
    def test_verify_login_invalid_account(self, setup, data_key):
        self.logger.info("===== Verify that user cannot login with invalid account =====")
        test_data = self.testdata.get_data(data_key)
        login_page = LoginPage(self.driver)
        try:
            email_enter = test_data["email"]
            password = test_data["password"]
            login_page.enter_email(email_enter)
            self.logger.info(f"Enter invalid email : {email_enter}")
            login_page.enter_password(password)
            self.logger.info("Enter password textbox")
            login_page.click_submit_button()
            self.logger.info("Click submit button")
            assert login_page.get_message() == "Username or password is incorrect"
            self.logger.passed("Display error message")
        except Exception as e:
            self.logger.failed("User can login with invalid password", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_login_invalid_password.png")
            assert False

    def test_verify_password_masking(self, setup):
        self.logger.info("===== Verify Password Masking UI Security =====")
        login_page = LoginPage(self.driver)
        test_data = self.testdata.get_data("eye_password")
        try:
            email_enter = test_data["email"]
            password = test_data["password"]
            login_page.enter_email(email_enter)
            self.logger.info(f"Enter invalid email : {email_enter}")
            login_page.enter_password(password)
            self.logger.info("Entered password into the textbox")
            assert login_page.get_input_type() == "password"
            self.logger.passed("Default eye password field is properly masked type = 'password'")
            login_page.click_toggle_password()
            self.logger.info("Clicked the eye icon to unmask password")
            assert login_page.get_input_type() == "text"
            self.logger.passed("Open eye password field is unmasked type='text'")
            login_page.click_toggle_password()
            self.logger.info("Clicked the eye icon again to hide password")
            assert login_page.get_input_type() == "password"
            self.logger.passed("Close eye password field is masked again type='password'")
        except Exception as e:
            self.logger.failed("Password masking verification failed", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_password_masking.png")
            assert False

    def test_verify_remember_me_checkbox(self):
        """
        Step by step:
            1. Navigate to login page
            2. Verify Remember Me is unchecked by default
            3. Click Remember Me checkbox
            4. Verify it becomes checked
            5. Click again and verify it unchecks
        """
        self.logger.info("===== Verify Remember Me Checkbox =====")
        login_page = LoginPage(self.driver)
        self.driver.refresh()
        try:
            assert not login_page.is_remember_me_checked(), "Remember Me should be unchecked by default"
            self.logger.info("Remember Me is unchecked by default")
            login_page.click_remember_me()
            self.logger.info("Click Remember Me checkbox")
            assert login_page.is_remember_me_checked(), "Remember Me should be checked after click"
            self.logger.info("Remember Me is checked")
            login_page.click_remember_me()
            self.logger.info("Click Remember Me checkbox again")
            assert not login_page.is_remember_me_checked(), "Remember Me should be unchecked after second click"
            self.logger.passed("Remember Me checkbox toggles correctly")
        except Exception as e:
            self.logger.failed(f"Remember Me checkbox verification failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_remember_me_checkbox.png")
            assert False

    def test_verify_forgot_password_navigates_to_reset_page(self):
        """
        Step by step:
            1. Verify 'Forgot Password?' link is visible on login page
            2. Click 'Forgot Password?' link
            3. Verify 'Reset Password' page title is displayed
            4. Click 'Back to Sign In' link on Reset Password page
            5. Verify Email field on login page is visible again
        """
        self.logger.info("===== Verify Forgot Password Navigates to Reset Password Page =====")
        login_page = LoginPage(self.driver)
        self.driver.refresh()
        try:
            assert login_page.is_forgot_password_displayed(), "Forgot Password link should be visible on login page"
            self.logger.info("Forgot Password link is visible")
            login_page.click_forgot_password()
            self.logger.info("Click Forgot Password link")
            title = login_page.get_reset_password_title()
            self.logger.info(f"Reset Password page title: {title}")
            assert title == "Reset Password", f"Expected 'Reset Password', got '{title}'"
            self.logger.info("Reset Password page loaded successfully")
            login_page.click_back_to_sign_in()
            self.logger.info("Click Back to Sign In on Reset Password page")
            assert login_page.is_email_field_displayed(), "Email field should be visible after clicking Back to Sign In"
            self.logger.passed("Forgot Password → Reset Password page → Back to Sign In → Login page restored")
        except Exception as e:
            self.logger.failed(f"Forgot Password navigation failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_forgot_password_navigates.png")
            assert False

    def test_verify_create_one_navigates_to_sign_up_page(self):
        """
        Step by step:
            1. Verify 'Create One.' link is visible on login page
            2. Click 'Create One.' link
            3. Verify 'Create your RepairSolutionsPRO® account' heading is displayed
            4. Click 'Sign in' link on the Create Account page
            5. Verify Email field on login page is visible again
        """
        self.logger.info("===== Verify Create One Navigates to Sign Up Page =====")
        login_page = LoginPage(self.driver)
        self.driver.refresh()
        try:
            assert login_page.is_create_one_displayed(), "'Create One.' link should be visible on login page"
            self.logger.info("'Create One.' link is visible")
            login_page.click_create_one()
            self.logger.info("Click Create One link")
            title = login_page.get_create_account_title()
            self.logger.info(f"Create Account page title: {title}")
            assert "Create your RepairSolutionsPRO" in title, f"Expected sign up title, got '{title}'"
            self.logger.info("Create Account page loaded successfully")
            login_page.click_sign_in_link()
            self.logger.info("Click Sign in link on Create Account page")
            assert login_page.is_email_field_displayed(), "Email field should be visible after clicking Sign in"
            self.logger.passed("Create One → Create Account page → Sign in → Login page restored")
        except Exception as e:
            self.logger.failed(f"Create One navigation failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_create_one_navigates.png")
            assert False

    def test_verify_login_valid_account(self):
        self.logger.info("===== Verify that user can login with valid email and password  =====")
        test_data = self.testdata.get_data("valid")
        login_page = LoginPage(self.driver)
        self.driver.refresh()
        try:
            email_enter = test_data["email"]
            password = test_data["password"]
            login_page.enter_email(email_enter)
            self.logger.info(f"Enter email : {email_enter}")
            login_page.enter_password(password)
            self.logger.info("Enter password textbox")
            login_page.click_submit_button()
            self.logger.info("Click submit button")
            assert login_page.title_is_displayed() == "My Reports"
            self.logger.passed("Login Successful with invalid account")
        except Exception as e:
            self.logger.failed("Email does not exist", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_login_valid_account.png")
            assert False

