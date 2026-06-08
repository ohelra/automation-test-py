import time
from datetime import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from utilities.waitHelper import WaitHelper

class MyReportPage(RSPROHomePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitHelper(driver)

    # Loading overlay
    loading_spinner =        (By.XPATH, "//*[contains(text(),'Loading...')]")

    # Search Box
    search_box =            (By.ID,"new-report-search-input")
    get_id_values =         (By.XPATH, "//*[@id='all-report']/div/table/tbody/tr/td[2]/span")
    get_vehicle_values =    (By.XPATH, "//*[@id='all-report']/div/table/tbody/tr/td[3]/span")
    get_type_values =       (By.XPATH, "//*[@id='all-report']/div/table/tbody/tr/td[5]/span")
    get_tool_values =       (By.XPATH, "//*[@id='all-report']/div/table/tbody/tr/td[6]/span")
    get_customer_values  =  (By.XPATH, "//*[@id='all-report']/div/table/tbody/tr/td[7]/span")
    get_not_found =         (By.XPATH, "//*[normalize-space(text())='No reports found.']")

    # Filter
    # Date Picker
    filter =                (By.ID, "new-filter-dropdown")
    date_from =             (By.ID, "filter-date-from")
    date_to =               (By.ID, "filter-date-to")
    date_and_time_values =  (By.XPATH, "//*[@id='all-report']/div/table/tbody/tr/td[8]/span")
    # Type
    type_OBD_II =           (By.XPATH, "//button[normalize-space()='OBD II']")
    type_diagnostic =       (By.XPATH, "//*[contains(@data-report-type, '1')]")
    type_customer =         (By.XPATH, "//*[contains(@data-report-type, '2')]")
    type_collision =        (By.XPATH, "//*[contains(@data-report-type, '3')]")
    type_sample =           (By.XPATH, "//*[contains(@data-report-type, 'sample')]")
    # Tool
    tool_7111 =             (By.XPATH, "//*[contains(@data-tool-name, '7111')]")
    tool_SDS43 =            (By.XPATH, "//*[contains(@data-tool-name, 'SDS43')]")
    tool_SDS50 =            (By.XPATH, "//*[contains(@data-tool-name, 'SDS50')]")
    # Clear
    clear_button =          (By.ID, "clear-all-filters")
    selected_type_tag =     (By.XPATH, "//button[contains(@class,'type-filter-btn') and contains(@class,'active')]")

    # Checkbox
    checkbox_button =       (By.XPATH, "//*[contains(@class,'form-check-input checkbox-input rounded-1 mt-0')][1]")
    report =                (By.XPATH, "//*[@id='all-report']/div[1]/table/tbody/tr[1]/td[3]/span")

    # Share
    share_button =          (By.ID, "selection-share-btn")
    email_textbox =         (By.ID, "share-email-input")
    send_button =           (By.ID, "share-send-btn")
    copy_link_button =      (By.ID, "share-copy-link-btn")
    invalid_email_error =   (By.ID, "share-email-error")
    auto_suggest_item =     (By.CSS_SELECTOR, "#share-email-suggestions .suggestion-item")
    tags_container =        (By.ID, "share-email-tags-container")

    # Edit
    edit_button =           (By.ID, "selection-edit-btn")
    first_name =            (By.ID, "firstName")
    last_name =             (By.ID, "lastName")
    phone =                 (By.ID, "phone")
    edit_email =            (By.ID, "email")
    save_button =           (By.ID, "assignReportBtn")

    # Delete
    delete_button =         (By.ID, "selection-delete-btn")
    confirm_delete_button = (By.ID, "confirm-delete-btn")
    keep_button =           (By.XPATH, "//*[normalize-space(text())='No, keep it!']")
    modal_close =           (By.XPATH, "//*[@id='modal-delete-report']/div/div/div[1]/button")
    get_table_report =      (By.XPATH, "//*[@id='all-report']/div[1]/table/tbody/tr")


    # Search logic action
    def enter_search(self, keyword):
        search = self.wait.wait_for_element_visible(*self.search_box)
        search.clear()
        search.send_keys(keyword)
        time.sleep(3)

    def get_contains_vehicle_values(self, keyword):
        time.sleep(3)
        vehicles = self.driver.find_elements(*self.get_vehicle_values)
        for v in vehicles:
            text = v.text.lower()
            assert keyword.lower() in text, f"Expected '{keyword}' in '{text}'"

    def get_contains_id_values(self, keyword):
        time.sleep(3)
        get_id = self.driver.find_elements(*self.get_id_values)
        for i in get_id:
            text = i.text.lower()
            assert keyword.lower() in text, f"Expected '{keyword}' in '{text}'"

    def get_contains_type_values(self, keyword):
        time.sleep(3)
        get_type = self.driver.find_elements(*self.get_type_values)
        for i in get_type:
            text = i.text.strip().lower()
            assert keyword.lower() in text, f"Expected '{keyword}' in '{text}'"

    def get_contains_customer_values(self, keyword):
        time.sleep(3)
        get_custom = self.driver.find_elements(*self.get_customer_values)
        for i in get_custom:
            text = i.text.lower()
            assert keyword.lower() in text, f"Expected '{keyword}' in '{text}'"

    def get_contains_tool_values(self, keyword):
        time.sleep(3)
        get_tool = self.driver.find_elements(*self.get_tool_values)
        for i in get_tool:
            text = i.text.lower()
            assert keyword.lower() in text, f"Expected '{keyword}' in '{text}'"

    def get_contains_not_found(self):
        return self.driver.find_element(*self.get_not_found).text

    # Filter logic action
    # Date Picker
    def filter_click(self):
        self.wait.wait_for_element_visible(*self.filter).click()

    def enter_date_from(self, keyword):
        date_str = keyword.replace(" ", "/")
        field = self.wait.wait_for_element_visible(*self.date_from)
        field.clear()
        field.send_keys(date_str)
        return datetime.strptime(date_str, "%m/%d/%Y")

    def enter_to_date(self, keyword):
        date_str = keyword.replace(" ", "/")
        field = self.wait.wait_for_element_visible(*self.date_to)
        field.clear()
        field.send_keys(date_str)
        return datetime.strptime(date_str, "%m/%d/%Y")

    def get_date_values(self):
        time.sleep(3)
        self.wait.wait_for_element_visible(*self.date_and_time_values)
        elements = self.driver.find_elements(*self.date_and_time_values)
        result = []
        for e in elements:
            text = e.text.strip()
            if text:
                date_part = text.split(" ")[0]
                date_object = datetime.strptime(date_part, "%m/%d/%Y").date()
                result.append(date_object)
        return result

    # Type
    def click_type_obd2(self):
        self.wait.wait_for_element_visible(*self.type_OBD_II).click()

    def click_type_diagnostic(self):
        self.wait.wait_for_element_visible(*self.type_diagnostic).click()

    def click_type_customer(self):
        self.wait.wait_for_element_visible(*self.type_customer).click()

    def click_type_collision(self):
        self.wait.wait_for_element_visible(*self.type_collision).click()

    def click_type_sample(self):
        self.wait.wait_for_element_visible(*self.type_sample).click()


    # Tool
    def click_tool_7111(self):
        self.wait.wait_for_element_visible(*self.tool_7111).click()

    def click_tool_sds43(self):
        self.wait.wait_for_element_visible(*self.tool_SDS43).click()

    def click_tool_sds50(self):
        self.wait.wait_for_element_visible(*self.tool_SDS50).click()


    # Clear
    def click_clear_button(self):
        time.sleep(1)
        self.wait.wait_for_element_visible(*self.clear_button).click()

    def get_type_button_display(self):
        return self.wait.wait_for_element_visible(*self.selected_type_tag).is_displayed()

    def is_type_cleared(self):
        clear_elements = self.driver.find_elements(*self.selected_type_tag)
        return len(clear_elements) == 0

    # Select check box
    def select_check_box(self):
        self.driver.find_element(*self.checkbox_button).click()

    def get_report_vehicle(self):
        return self.driver.find_element(*self.report).text.strip()

    # Edit
    def click_edit_button(self):
        self.wait.wait_for_element_visible(*self.edit_button).click()

    def enter_first_name_textbox(self, keyword):
        firstname = self.driver.find_element(*self.first_name)
        firstname.clear()
        firstname.send_keys(keyword)

    def enter_last_name_textbox(self, keyword):
        lastname = self.driver.find_element(*self.last_name)
        lastname.clear()
        lastname.send_keys(keyword)

    def enter_phone_textbox(self, keyword):
        phone = self.driver.find_element(*self.phone)
        phone.clear()
        phone.send_keys(keyword)

    def enter_email_textbox(self, keyword):
        email = self.driver.find_element(*self.edit_email)
        email.clear()
        email.send_keys(keyword)
        email.send_keys(Keys.TAB)

    def click_save_button(self):
        self.driver.find_element(*self.save_button).click()

    def get_enable_save_button(self):
        return self.driver.find_element(*self.save_button).is_enabled()

    def wait_for_loading(self):
        """Wait until the Loading... overlay disappears before next interaction."""
        self.wait.wait_for_element_invisible(*self.loading_spinner)
        
    # Get message required
    def is_required_firstname_error(self) -> WebElement:
        return self.wait.wait_for_element_visible(By.ID, "firstName-error").text.strip()

    def is_required_lastname_error(self) -> WebElement:
        return self.wait.wait_for_element_visible(By.ID, "lastName-error").text.strip()

    def is_required_phone_error(self) -> WebElement:
        return self.wait.wait_for_element_visible(By.ID, "phone-error").text.strip()

    def is_required_email_error(self) -> WebElement:
        return self.wait.wait_for_element_visible(By.ID, "email-error").text.strip()

    def clear_first_name(self):
        self.wait.wait_for_element_visible(By.ID, "firstName-error").clear()

    # "rgb(220, 38, 38)",  -> #dc2626
    # "rgb(225, 32, 24)"]  -> #e12018
    def is_error_red_border(self, locator):
        red_border = self.driver.find_element(*locator)
        border_color = red_border.value_of_css_property("border-color")
        return "rgb(220, 38,38)" or "rgb(225,32,24)" in border_color

    # Share feature
    def click_share_button(self):
        self.driver.find_element(*self.share_button).click()

    def click_copy_link(self):
        self.driver.find_element(*self.copy_link_button).click()

    def get_copied_link(self):
        return self.wait.wait_for_element_visible(*self.copy_link_button).text

    def enter_share_email_textbox(self, email):
        element = self.wait.wait_for_element_visible(*self.email_textbox)
        element.send_keys(email)
        element.send_keys(Keys.TAB)

    # def select_suggestion_email(self):
    #     auto_suggest = self.wait.wait_for_element_visible(*self.auto_suggest_item)
    #     time.sleep(1)
    #     auto_suggest.get_attribute("data-email").strip()
    #     auto_suggest.click()

    def select_suggested_email(self, exact_email):
        item_locator = (By.XPATH, f"//*[contains(@class, 'suggestion-item') and @data-email='{exact_email}']")
        self.wait.wait_for_element_visible(*item_locator).click()

    def verify_email_select_displayed(self, expected_value):
        element = self.wait.wait_for_element_visible(*self.tags_container)
        return expected_value in element.text

    def get_email_error_message(self):
        return self.wait.wait_for_element_visible(*self.invalid_email_error).text

    def click_send_share(self):
        self.wait.wait_for_element_visible(*self.send_button).click()

    def is_share_popup_closed(self):
        try:
            self.wait.wait_for_element_visible(*self.send_button)
            return True
        except:
            return False

    # Delete report
    def click_delete_button(self):
        self.driver.find_element(*self.delete_button).click()

    def click_keep_button(self):
        self.driver.find_element(*self.keep_button).click()

    def click_modal_close(self):
        self.driver.find_element(*self.modal_close).click()

    def click_confirm_yes_button(self):
        self.driver.find_element(*self.confirm_delete_button).click()

    def get_first_report(self):
        return self.driver.find_element(*self.report).text.strip()

    def get_rows_reports(self):
        rows = self.driver.find_elements(*self.get_table_report)
        return [r.text.strip() for r in rows]

    def get_report_row_count(self):
        rows = self.driver.find_elements(*self.get_table_report)
        return len(rows)

    def is_delete_button_displayed(self):
        try:
            return self.wait.wait_for_element_visible(*self.delete_button).is_displayed()
        except Exception:
            return False

    def is_send_button_enabled(self):
        return self.wait.wait_for_element_visible(*self.send_button).is_enabled()