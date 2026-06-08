import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage


class CoverageCheckerPage(RSPROHomePage):

    # ── Navigation ────────────────────────────────────────────────────────────
    support_menu =          (By.XPATH,  "//*[@id='navbarDropdown' and contains(text(),'Support')]")
    coverage_checker_link = (By.XPATH,  "//a[normalize-space()='Coverage Checker']")

    # ── Page Header ───────────────────────────────────────────────────────────
    # Title is rendered uppercase via CSS; DOM text may be mixed or upper case
    page_title =            (By.XPATH,  "//*[contains(translate(normalize-space(),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'COVERAGE CHECKER')]")
    page_subtitle =         (By.XPATH,  "//*[contains(text(),'Identify which SDS tool functions will work on your vehicle')]")

    tool_info =             (By.XPATH,  "(//span[@role='combobox'])[1]")
    search_tool =           (By.XPATH,  "(//input[@aria-label='Search'])[1]")
    year_info =             (By.XPATH,  "(//span[@role='combobox'])[3]")
    car_make =              (By.XPATH,  "(//span[@role='combobox'])[4]")
    model =                 (By.XPATH,  "(//span[@role='combobox'])[5]")
    engine =                (By.XPATH,  "(//span[@role='combobox'])[6]")

    # Select2 helpers
    select2_search =        (By.CSS_SELECTOR, ".select2-search__field")
    select2_option =        (By.CSS_SELECTOR, ".select2-results__option")

    # ── Submit Button ─────────────────────────────────────────────────────────
    submit_button =         (By.ID,     "submit-coverage-check")

    # ── Results Section ───────────────────────────────────────────────────────
    results_heading =       (By.XPATH,  "//*[contains(text(),'Availability & Special Functions Coverage')]")
    obd_diagnostic =        (By.XPATH,  "(//a[normalize-space()='OBD II Diagnostics'])[1]")
    oem_diagnostic =        (By.XPATH,  "(//a[normalize-space()='OEM Diagnostics'])[1]")
    workshop_tool =         (By.XPATH,  "(//a[normalize-space()='Workshop Tools'])[1]")


    def click_coverage_checker(self):
        self.hover(self.support_menu)
        self.wait.wait_for_element_visible(*self.coverage_checker_link).click()

    def get_page_title(self):
        return self.wait.wait_for_element_visible(*self.page_title).text

    def get_page_subtitle(self):
        return self.wait.wait_for_element_visible(*self.page_subtitle).text

    # ─────────────────────────────────────────────────────────────────────────
    # Select2 Dropdown Helper
    # ─────────────────────────────────────────────────────────────────────────

    def _get_select2_options(self, combobox_locator):
        """Open a Select2 dropdown and return all visible option texts."""
        self.wait.wait_for_element_visible(*combobox_locator).click()
        time.sleep(0.5)
        options = self.driver.find_elements(*self.select2_option)
        texts = [o.text.strip() for o in options if o.text.strip()]
        self.driver.find_element(By.TAG_NAME, "body").click()
        time.sleep(0.2)
        return texts

    # ─────────────────────────────────────────────────────────────────────────
    # Form Interaction Methods
    # ─────────────────────────────────────────────────────────────────────────

    def select_tool_info(self, tool_name):
        tool = self.wait.wait_for_element_visible(*self.tool_info)
        tool.click()
        element = self.wait.wait_for_element_visible(*self.search_tool)
        element.send_keys(tool_name)
        element.send_keys(Keys.ENTER)

    def select_year(self, year):
        years = self.wait.wait_for_element_visible(*self.year_info)
        years.click()
        element = self.wait.wait_for_element_visible(*self.search_tool)
        element.send_keys(year)
        element.send_keys(Keys.ENTER)

    def select_make(self, make):
        makes = self.wait.wait_for_element_visible(*self.car_make)
        makes.click()
        element = self.wait.wait_for_element_visible(*self.search_tool)
        element.send_keys(make)
        element.send_keys(Keys.ENTER)

    def select_model(self, model_name):
        models = self.wait.wait_for_element_visible(*self.model)
        models.click()
        element = self.wait.wait_for_element_visible(*self.search_tool)
        element.send_keys(model_name)
        element.send_keys(Keys.ENTER)

    def select_engine(self, engine_name):
        engines = self.wait.wait_for_element_visible(*self.engine)
        engines.click()
        element = self.wait.wait_for_element_visible(*self.search_tool)
        element.send_keys(engine_name)
        element.send_keys(Keys.ENTER)

    def click_submit(self):
        self.wait.wait_for_element_visible(*self.submit_button).click()
        time.sleep(1.5)

    def get_tool_options(self):
        return self._get_select2_options(self.tool_info)

    # ─────────────────────────────────────────────────────────────────────────
    # Results Methods
    # ─────────────────────────────────────────────────────────────────────────

    def scroll_to_results(self):
        self.scroll_to(self.obd_diagnostic)

    def is_results_section_visible(self):
        try:
            self.scroll_to_results()
            el = self.wait.wait_for_element_visible(*self.results_heading)
            return el.is_displayed()
        except Exception:
            return False

    def get_results_heading_text(self):
        self.scroll_to_results()
        return self.wait.wait_for_element_visible(*self.results_heading).text

    def scroll_to_obd_diagnostic(self):
        self.scroll_to(self.obd_diagnostic)

    def is_obd_diagnostic_visible(self):
        self.scroll_to(self.obd_diagnostic)
        return self.wait.wait_for_element_visible(*self.obd_diagnostic).is_displayed()

    def is_oem_diagnostic_visible(self):
        self.wait.wait_for_element_visible(*self.oem_diagnostic).click()

    def oem_display(self):
        return self.wait.wait_for_element_visible(*self.oem_diagnostic).is_displayed()

    def click_workshop_tool(self):
        self.wait.wait_for_element_visible(*self.workshop_tool).click()

    def is_workshop_tool_visible(self):
        return self.wait.wait_for_element_visible(*self.workshop_tool).is_displayed()
