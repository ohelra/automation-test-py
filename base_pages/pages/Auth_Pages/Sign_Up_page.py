import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from utilities.waitHelper import WaitHelper
from utilities.custom_logger import LogMaker

class SignUpPage(RSPROHomePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitHelper(driver)
        self.logger = LogMaker.log_gen()

    email =                     (By.ID,        "EmailPwd_Email")
    password =                  (By.ID,        "EmailPwd_Password")
    city =                      (By.ID,        "AccountInformation_City")
    state =                     (By.ID,        "AccountInformation_State")
    zipcode_button =            (By.ID,        "AccountInformation_ZipCode")
    first_name_textbox =        (By.ID,        "AccountInformation_FirstName")
    last_name_textbox =         (By.ID,        "AccountInformation_LastName")
    address1_textbox =          (By.ID,        "AccountInformation_Address1")
    address2_textbox =          (By.ID,        "AccountInformation_Address2")
    email_empty_error =         (By.ID,        "EmailPwd_Email-error")
    password_message_error =    (By.ID,        "EmailPwd_Password-error")
    first_name_message_error =  (By.ID,        "AccountInformation_FirstName-error")
    last_name_message_error =   (By.ID,        "AccountInformation_LastName-error")
    address_l1_message_error =  (By.ID,        "AccountInformation_Address1-error")
    check_box =                 (By.ID,        "checkbox-02")
    eula_terms_link =           (By.LINK_TEXT, "EULA/Terms")
    privacy_policy_link =       (By.LINK_TEXT, "Privacy Policy")
    create_account_button =     (By.XPATH,     "//*[@id='navbarCollapse']/form/a[4]")
    continue_button =           (By.XPATH,     "//*[contains(@class,'div-email-submit')]")
    zipcode_message =           (By.XPATH,     "//*[@id='step-personal-info']/form/div[5]/div[1]/span")
    email_exist_error =         (By.XPATH,     "//span[contains(text(),'Email has been used')]")
    email_invalid_error =       (By.XPATH,     "//span[contains(text(),'Email invalid')]")
    disable_continue_button =   (By.XPATH,     "//button[@class='btn web-btn-signup w-100']")
    eula_terms_text =           (By.XPATH,     "//*[contains(@class, 'fs-48') and normalize-space(text())='Terms of Use & End User License Agreement']")
    privacy_policy_text =       (By.XPATH,     "//*[contains(@class, 'fs-48') and normalize-space(text())='Privacy Policy']")
    continue_button_next =      (By.XPATH,     "//div[2]/button[contains(@class, 'web-btn-signup w-100 enabled') and normalize-space(text())='Continue'] ")
    verify_account_button =     (By.XPATH,     "//*[contains(text(),'Verify Account')]")


    def get_create_account(self):
        return self.driver.find_elements(*self.create_account_button)

    def click_create_account(self):
        self.wait.wait_for_element_visible(*self.create_account_button).click()

    def get_email(self):
        return self.driver.find_elements(*self.email)

    def enter_email(self, email):
        self.wait.wait_for_element_visible(*self.email).send_keys(email)

    def enter_password(self, password):
        element = self.wait.wait_for_element_visible(*self.password)
        element.send_keys(password)
        element.send_keys(Keys.TAB)

    def click_continue_button(self):
        self.wait.wait_for_element_visible(*self.continue_button).click()

    def enter_zipcode(self, zipcode):
        elements = self.wait.wait_for_element_visible(*self.zipcode_button)
        elements.clear()
        elements.send_keys(str(zipcode))
        elements.send_keys(Keys.TAB)
        self.wait_for_city_to_fill()

    def wait_for_city_to_fill(self):
        try:
            self.wait.until(lambda d: d.find_element(*self.city).get_attribute("value") != "")
        except:
            pass

    def get_city_value(self):
        elem = self.wait.wait_for_element_visible(*self.city)
        return elem.get_attribute("value")

    def get_state_value(self):
        elem = self.wait.wait_for_element_visible(*self.state)
        return elem.get_attribute("value")

    def enter_zipcode_invalid(self, zipcode):
        element = self.wait.wait_for_element_visible(*self.zipcode_button)
        element.send_keys(zipcode)
        element.send_keys(Keys.TAB)
        time.sleep(1)

    def enter_zipcode_empty(self, zipcode):
        element = self.wait.wait_for_element_visible(*self.zipcode_button)
        element.send_keys(zipcode)
        element.clear()
        time.sleep(3)

    def get_zipcode_message_error(self):
        return self.wait.wait_for_element_visible(*self.zipcode_message).text

    # Get attribute email existing error message
    def get_email_existing_error(self):
        element = self.wait.wait_for_element_visible(*self.email_exist_error)
        return element.text

    # Get attribute invalid email error message
    def get_email_invalid_error(self):
        element = self.wait.wait_for_element_visible(*self.email_invalid_error)
        return element.text

    # Get attribute email empty error message
    def get_email_empty_error_message(self):
        element = self.wait.wait_for_element_visible(*self.email_empty_error)
        return element.text

    # Get attribute password error message
    def get_password_message_error(self):
        element = self.wait.wait_for_element_visible(*self.password_message_error)
        return element.text

    # Get continue button disabled
    def get_continue_button_enable(self):
        self.wait.wait_for_element_visible(*self.continue_button).is_enabled()

    # Get continue button background color attribute
    def get_continue_button_background_color(self):
        return self.wait.wait_for_element_visible(*self.continue_button).value_of_css_property("background-color")

    # Get continue button border color attribute
    def get_cọntinue_button_border(self):
        return self.wait.wait_for_element_visible(*self.continue_button).value_of_css_property("border-color")

    def enter_email_txb(self, email):
        element = self.wait.wait_for_element_visible(*self.email)
        element.clear()
        element.send_keys(email)
        element.send_keys(Keys.TAB)
        #time.sleep(1)

    def enter_password_txb(self, password):
        self.wait.wait_for_element_visible(*self.password).send_keys(password)

    def clear_email_textbox(self):
        element = self.wait.wait_for_element_visible(*self.email)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)

    def clear_password_textbox(self):
        element = self.wait.wait_for_element_visible(*self.password)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)

    def is_at_email_step(self):
        return self.wait.wait_for_element_present_speed(*self.email)

    def is_at_info_step(self):
        return self.wait.wait_for_element_present_speed(*self.first_name_textbox)

    def refresh_page(self):
        self.driver.refresh()

    def click_eula_term_link(self):
        self.wait.wait_for_element_visible(*self.eula_terms_link).click()

    def click_privacy_policy_link(self):
        self.wait.wait_for_element_visible(*self.privacy_policy_link).click()

    def get_eula_term_text(self):
        element = self.wait.wait_for_element_visible(*self.eula_terms_text).text
        return element.split('\n')[0].strip()

    def get_privacy_policy_text(self):
        element = self.wait.wait_for_element_visible(*self.privacy_policy_text).text
        return element.split('\n')[0].strip()

    # Create an account
    def enter_first_name(self, first_name):
        element = self.wait.wait_for_element_visible(*self.first_name_textbox)
        element.send_keys(first_name)

    def enter_last_name(self, last_name):
        element = self.wait.wait_for_element_visible(*self.last_name_textbox)
        element.send_keys(last_name)

    def enter_address_line_1(self, address1):
        element = self.wait.wait_for_element_visible(*self.address1_textbox)
        element.send_keys(address1)

    def clear_first_name(self):
        element = self.wait.wait_for_element_visible(*self.first_name_textbox)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)

    def clear_last_name(self):
        element = self.wait.wait_for_element_visible(*self.last_name_textbox)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)

    def clear_address_line_1(self):
        element = self.wait.wait_for_element_visible(*self.address1_textbox)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)

    def clear_zipcode(self):
        element = self.wait.wait_for_element_visible(*self.zipcode_button)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)

    def get_first_name_message_error(self):
        return self.wait.wait_for_element_visible(*self.first_name_message_error).text

    def get_last_name_message_error(self):
        return self.wait.wait_for_element_visible(*self.last_name_message_error).text

    def get_address_line_1_message_error(self):
        return self.wait.wait_for_element_visible(*self.address_l1_message_error).text

    def enter_address_line_2(self, address2):
        self.wait.wait_for_element_visible(*self.address2_textbox).send_keys(address2)

    def click_check_box_agree(self):
        self.wait.wait_for_element_visible(*self.check_box).click()

    def click_continue_button_next(self):
        self.wait.wait_for_element_visible(*self.continue_button_next).click()

    def verify_account_disable(self):
        self.wait.wait_for_element_visible(*self.verify_account_button).is_enabled()

    