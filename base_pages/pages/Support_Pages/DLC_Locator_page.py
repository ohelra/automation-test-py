from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage

class DLCLocatorPage(RSPROHomePage):

    vin =                   (By.ID, "vin")
    dlc_image =             (By.ID, "dtcImage1")
    result_message =        (By.ID, "searchResult")
    submit_vin =            (By.ID, "btnSubmitByVin")
    submit =                (By.ID, "btnSubmitByYMM")
    model =                 (By.ID, "select2-dlcModels-container")
    support =               (By.XPATH, "//*[@id='navbarDropdown' and contains(text(),'Support')]")
    dlc_locator =           (By.XPATH, "//a[contains(text(), 'DLC Locator')]")
    make =                  (By.XPATH, "(//span[@role='combobox'])[1]")
    year =                  (By.XPATH, "(//span[@role='combobox'])[2]")
    location =              (By.XPATH, "//*[@id='dlcLocatorContent']/tbody/tr/td[2]")
    select2_search =        (By.CSS_SELECTOR, "input.select2-search__field")


    def click_dlc_locator(self):
        self.hover(self.support)
        self.wait.wait_for_element_visible(*self.dlc_locator).click()

    def select_make(self, make):
        self.select_dropdown_option(self.make, make)

    def select_year(self, year):
        self.select_dropdown_option(self.year, year)

    def select_model(self, model):
        self.select_dropdown_option(self.model, model)

    def select_dropdown_option(self, locator, value):
        self.wait.wait_for_element_visible(*locator).click()
        search = self.wait.wait_for_element_visible(*self.select2_search)
        search.send_keys(str(value))
        search.send_keys(Keys.ENTER)

    def search_by_ymm(self, make, year, model):
        self.select_make(make)
        self.select_year(year)
        self.select_model(model)
        self.wait.wait_for_element_visible(*self.submit).click()

    def enter_vin(self, vin):
        element = self.wait.wait_for_element_visible(*self.vin)
        element.clear()
        element.send_keys(vin)

    def search_by_vin(self, vin):
        self.enter_vin(vin)
        self.wait.wait_for_element_visible(*self.submit_vin).click()

    def get_location_text(self):
        return self.wait.wait_for_element_visible(*self.location).text.strip()

    def get_result_message_text(self):
        return self.wait.wait_for_element_visible(*self.result_message).text.strip()

    def scroll_to_dlc_image(self):
        self.specific_scroll_to(self.dlc_image)

    def get_dlc_image_src(self):
        return self.wait.wait_for_element_visible(*self.dlc_image).get_attribute("src")

    def get_dlc_image_screenshot(self):
        return self.wait.wait_for_element_visible(*self.dlc_image).screenshot_as_png
