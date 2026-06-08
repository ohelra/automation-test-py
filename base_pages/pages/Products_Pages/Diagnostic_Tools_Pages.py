import time
from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage

class DiagnosticToolsPage(RSPROHomePage):

    product  =                      (By.ID,    "navbarDropdown")
    list_view_icon =                (By.ID,    "pills-02c-tab")
    grid_view_icon =                (By.ID,    "pills-01c-tab")
    auto_parts =                    (By.ID,    "7111FindinstoreNP")
    auto_parts_sds50 =              (By.ID,    "SDS50FindinstoreNP")
    auto_parts_sds43 =              (By.ID,    "SDS43FindinstoreNP")
    diagnostic_tools =              (By.XPATH, "//*[@id='navbarCollapse']/ul/li[2]/div/div/div/div[1]/a")
    find_store_list_view =          (By.XPATH, "//*[@id='pills-02c']/div/div[1]/div/div[3]/div/p/a")
    canadian_store_link =           (By.XPATH, "//*[@id='7111FindinstoreCT']")
    find_a_store_7111 =             (By.XPATH, "//*[contains(@data-bs-target, '#modal-find-store-7111')]")
    product_details_7111 =          (By.XPATH, "//*[@id='pills-02c']/div/div[1]/div/div[3]/p/a")
    page_7111 =                     (By.XPATH, "//*[contains(text(),'7111: Smart Diagnostic System Tablet')]")
    product_details_sds50 =         (By.XPATH, "//*[@id='pills-02c']/div/div[2]/div/div[3]/p/a")
    find_a_store_sds50 =            (By.XPATH, "//*[contains(@data-bs-target, '#modal-find-store-SDS50')]")
    find_store_sds50_list_view =    (By.XPATH, "//*[@id='pills-02c']//a[contains(@data-bs-target, 'SDS50')]")
    page_sds50 =                    (By.XPATH, "//*[contains(text(),'SDS50: Smart Diagnostic System Tech')]")
    product_details_sds43 =         (By.XPATH, "//*[@id='pills-02c']/div/div[3]/div/div[3]/p/a")
    page_sds43 =                    (By.XPATH, "//*[contains(text(),'SDS43: Smart Diagnostic System Inspector')]")
    find_a_store_sds43  =           (By.XPATH, "//*[contains(@data-bs-target, '#modal-find-store-SDS43')]")
    find_store_sds43_list_view =    (By.XPATH, "//*[@id='pills-02c']//a[contains(@data-bs-target,'SDS43')]")

    def click_diagnostic_tools(self):
        self.hover(self.product)
        self.wait.wait_for_element_visible(*self.diagnostic_tools).click()

    def click_product(self):
        self.wait.wait_for_element_visible(*self.product).click()

    def scroll_to_shop(self):
        self.scroll_to(self.find_a_store_7111)

    # 7111 : Find a store
    def click_find_a_store(self):
        self.wait.wait_for_element_visible(*self.find_a_store_7111).click()
        time.sleep(3)

    def scroll_to_shop_list_view(self):
        self.scroll_to(self.find_store_list_view)

    def click_find_a_store_list_view(self):
        self.wait.wait_for_element_visible(*self.find_store_list_view).click()
        time.sleep(3)

    def click_list_view(self):
        self.wait.wait_for_element_visible(*self.list_view_icon).click()

    # 7111 tool for Auto Parts store
    def click_auto_parts_store(self):
        self.wait.wait_for_element_visible(*self.auto_parts).click()

    # 7111 tool for Canadian store
    def click_canadian_store(self):
        self.wait.wait_for_element_visible(*self.canadian_store_link).click()

    def click_product_detail_7111_page(self):
        self.wait.wait_for_element_visible(*self.product_details_7111).click()

    def navigate_to_7111_page(self):
        return self.wait.wait_for_element_visible(*self.page_7111).text

    # SDS50 tool
    def click_product_detail_sds50(self):
        self.wait.wait_for_element_visible(*self.product_details_sds50).click()

    def scroll_to_shop_sds50(self):
        self.scroll_to(self.find_a_store_sds50)

    def scroll_to_shop_sds50_list_view(self):
        self.scroll_to(self.find_store_sds50_list_view)

    def navigate_to_sds50_page(self):
        return self.wait.wait_for_element_visible(*self.page_sds50).text

    def click_find_a_store_sds50(self):
        self.wait.wait_for_element_visible(*self.find_a_store_sds50).click()

    def click_find_a_store_sds50_list_view(self):
        self.wait.wait_for_element_visible(*self.find_store_sds50_list_view).click()

    def click_auto_parts_sds50(self):
        self.wait.wait_for_element_visible(*self.auto_parts_sds50).click()

    # SDS43 tool
    def click_product_detail_sds43(self):
        self.wait.wait_for_element_visible(*self.product_details_sds43).click()

    def scroll_to_shop_sds43(self):
        self.scroll_to(self.find_a_store_sds43)

    def scroll_to_shop_sds43_list_view(self):
        self.scroll_to(self.find_store_sds43_list_view)

    def click_find_a_store_sds43(self):
        self.wait.wait_for_element_visible(*self.find_a_store_sds43).click()

    def click_find_a_store_sds43_list_view(self):
        self.wait.wait_for_element_visible(*self.find_store_sds43_list_view).click()

    def click_auto_parts_sds43(self):
        self.wait.wait_for_element_visible(*self.auto_parts_sds43).click()

    def navigate_to_sds43_page(self):
        return self.wait.wait_for_element_visible(*self.page_sds43).text

    def click_grid_view(self):
        self.wait.wait_for_element_visible(*self.grid_view_icon).click()

    def is_list_view_active(self):
        tab = self.wait.wait_for_element_visible(*self.list_view_icon)
        return "active" in tab.get_attribute("class")

    def is_grid_view_active(self):
        tab = self.wait.wait_for_element_visible(*self.grid_view_icon)
        return "active" in tab.get_attribute("class")

