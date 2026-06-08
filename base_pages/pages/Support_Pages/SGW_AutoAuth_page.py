from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage

class SGWAutoAuthPage(RSPROHomePage):

    article_title =     (By.ID,     "_articleTitle")
    sgw_auto_auth =     (By.XPATH,  "//span[contains(text(), 'SGW AutoAuth')]")
    support =           (By.XPATH,  "//*[@id='navbarDropdown' and contains(text(),'Support')]")
    sgw_7111 =          (By.XPATH,  "//*[@id='dropdown-sgw-autoauth']//a[contains(text(), '7111')]")
    sgw_sds50 =         (By.XPATH,  "//*[@id='dropdown-sgw-autoauth']//a[contains(text(), 'SDS50')]")
    sgw_sds43 =         (By.XPATH,   "//*[@id='dropdown-sgw-autoauth']//a[contains(text(), 'SDS43')]")

    def click_sgw_auto_auth(self):
        self.hover(self.support)
        self.wait.wait_for_element_visible(*self.sgw_auto_auth).click()

    def click_7111_page(self):
        self.wait.wait_for_element_visible(*self.sgw_7111).click()

    def click_sds50_page(self):
        self.wait.wait_for_element_visible(*self.sgw_sds50).click()

    def click_sds43_page(self):
        self.wait.wait_for_element_visible(*self.sgw_sds43).click()

    def get_text(self):
        element = self.wait.wait_for_element_visible(*self.article_title).text
        return element.split('\n')[0].strip()

