from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilities.waitHelper import WaitHelper

class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    email =                   (By.ID,"Email")
    password =                (By.ID,"Password")
    title =                   (By.ID,"navbar-v2-page-title")
    submit_button =           (By.XPATH, "//*[contains(@type,'submit')]")
    message =                 (By.XPATH, "//*[contains(text(),'Username or password is incorrect')]")
    toggle_pass_icon =        (By.CSS_SELECTOR, "span.toggle-pass")
    remember_me =             (By.XPATH, "//input[@id='RememberMe']")
    forgot_password =         (By.XPATH, "//*[contains(text(),'Forgot Password?')]")
    create_one_link =         (By.XPATH, "//a[contains(text(),'Create One')]")
    create_account_button =   (By.XPATH, "//a[contains(text(),'Create an account')] | //button[contains(text(),'Create an account')]")
    reset_password_title =    (By.XPATH, "//*[normalize-space(text())='Reset Password']")
    back_to_sign_in =         (By.XPATH, "//a[normalize-space()='Back to Sign In']")
    create_account_title =    (By.XPATH, "//*[contains(text(),'Create your RepairSolutionsPRO')]")
    sign_in_link =            (By.XPATH, "//a[normalize-space()='Sign in']")

    def enter_email(self, mail):
        element = self.wait.wait_for_element_visible(*self.email)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(mail)

    def enter_password(self, pwd):
        element = self.wait.wait_for_element_visible(*self.password)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(pwd)

    def click_submit_button(self):
        element = self.wait.wait_for_element_clickable(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def get_input_type(self):
        return self.wait.wait_for_element_visible(*self.password).get_attribute("type")

    def title_is_displayed(self):
        return self.wait.wait_for_element_visible(*self.title).text

    def click_toggle_password(self):
        self.wait.wait_for_element_visible(*self.toggle_pass_icon).click()

    def get_message(self):
        return self.driver.find_element(*self.message).text

    def is_remember_me_checked(self):
        return self.wait.wait_for_element_visible(*self.remember_me).is_selected()

    def click_remember_me(self):
        self.wait.wait_for_element_visible(*self.remember_me).click()

    def click_forgot_password(self):
        self.wait.wait_for_element_visible(*self.forgot_password).click()

    def is_forgot_password_displayed(self):
        return self.wait.wait_for_element_visible(*self.forgot_password).is_displayed()

    def click_create_one(self):
        self.wait.wait_for_element_visible(*self.create_one_link).click()

    def is_create_one_displayed(self):
        return self.wait.wait_for_element_visible(*self.create_one_link).is_displayed()

    def get_reset_password_title(self):
        return self.wait.wait_for_element_visible(*self.reset_password_title).text

    def click_back_to_sign_in(self):
        self.wait.wait_for_element_visible(*self.back_to_sign_in).click()

    def get_create_account_title(self):
        return self.wait.wait_for_element_visible(*self.create_account_title).text

    def is_email_field_displayed(self):
        return self.wait.wait_for_element_visible(*self.email).is_displayed()

    def click_sign_in_link(self):
        self.wait.wait_for_element_visible(*self.sign_in_link).click()



