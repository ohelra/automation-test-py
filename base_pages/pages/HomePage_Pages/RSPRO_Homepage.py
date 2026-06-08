from selenium.webdriver.common.by import By
from base_pages.pages.Auth_Pages.Login import LoginPage
from base_pages.pages.base_page import BasePage
from utilities.read_properties import ReadConfig
from utilities.waitHelper import WaitHelper

class RSPROHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitHelper(driver)

    my_account =    (By.XPATH, "//*[contains(text(),'My Account')]")

    def go_to_home(self):
        base_url = ReadConfig.get_urls()
        self.open(base_url)

    def is_logged_in(self):
        try:
            return self.wait_for_element_visible(self.my_account, 3)
        except:
            return False

    def click_my_account(self):
        self.wait.wait_for_element_visible(*self.my_account).click()

    def perform_login(self):
        email = ReadConfig.get_email()
        pwd = ReadConfig.get_password()
        login_page = LoginPage(self.driver)
        login_page.enter_email(email)
        login_page.enter_password(pwd)
        login_page.click_submit_button()