from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage

class DTCLibraryPage(RSPROHomePage):

    search_dtc =            (By.ID,           "dtcCode")
    clear_all_button =      (By.ID,           "btnClear")
    submit_button =         (By.ID,           "btnSearchDtcLibrary")
    car_make_container =    (By.ID,           "select2-dtcMakes-container")
    delete_button =         (By.XPATH,        "//*[@id='dtcLibraryContent']/tbody/tr/td[4]/a/img")
    logo_RSPRO =            (By.XPATH,        "//*[@id='sidebar-v2-wrapper']/div/a")
    support =               (By.XPATH,        "//*[@id='navbarDropdown' and contains(text(),'Support')]")
    dtc_library =           (By.XPATH,        "//a[contains(text(), 'DTC Library')]")
    make_table =            (By.XPATH,        "//*[@id='dtcLibraryContent']/tbody/tr/td[1]")
    code_table =            (By.XPATH,        "//*[@id='dtcLibraryContent']/tbody/tr/td[2]")
    desc_table =            (By.XPATH,        "//*[@id='dtcLibraryContent']/tbody/tr/td[3]")
    delete_dtc =            (By.XPATH,        "//*[@id='dtcLibraryContent']/tbody/tr/td[4]/a/img")
    table_rows =            (By.XPATH,        "//*[@id='dtcLibraryContent']/tbody/tr")
    enter_make =            (By.CSS_SELECTOR, "input.select2-search__field")

    def click_logo_website(self):
        self.wait.wait_for_element_visible(*self.logo_RSPRO).click()

    def click_dtc_library(self):
        self.hover(self.support)
        self.wait.wait_for_element_visible(*self.dtc_library).click()

    def click_car_make(self):
        self.wait.wait_for_element_visible(*self.car_make_container).click()

    def enter_make_textbox(self,car):
        element = self.wait.wait_for_element_visible(*self.enter_make)
        element.send_keys(car)
        element.send_keys(Keys.ENTER)

    def search_dtc_library(self,code):
        element = self.wait.wait_for_element_visible(*self.search_dtc)
        element.clear()
        element.send_keys(code)

    def click_submit_button(self):
        self.wait.wait_for_element_visible(*self.submit_button).click()

    def click_clear_all_button(self):
        self.wait.wait_for_element_visible(*self.clear_all_button).click()

    def get_make_table_text(self):
        return self.wait.wait_for_element_visible(*self.make_table).text

    def get_code_table_text(self):
        return self.wait.wait_for_element_visible(*self.code_table).text

    def get_desc_table_text(self):
        return self.wait.wait_for_element_visible(*self.desc_table).text

    def get_desc_table(self):
        return self.wait.wait_for_element_visible(*self.desc_table)

    def get_table_row_count(self):
        rows = self.driver.find_elements(*self.table_rows)
        return len(rows)

    def get_dtc_code_value(self):
        return self.wait.wait_for_element_visible(*self.search_dtc).get_attribute("value")

    def get_car_make_container_text(self):
        return self.wait.wait_for_element_visible(*self.car_make_container).text

    def click_delete_icon(self):
        self.wait.wait_for_element_visible(*self.delete_button).click()

