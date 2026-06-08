from selenium.webdriver.common.by import By
from base_pages.pages.base_page import BasePage

class UpdateManualPage(BasePage):

    download_en =           (By.ID,    "download-btn")
    download_es =           (By.ID,    "download-btn-es")
    support =               (By.XPATH, "//*[@id='navbarDropdown' and contains(text(),'Support')]")
    update_manual =         (By.XPATH,  "//a[normalize-space()='Updates/Manuals']")
    select_tools =          (By.XPATH, "(//select[@id='selectedToolName'])[1]")
    select_tool_2d1 =       (By.XPATH, "//*[contains(text(),'7111 (0x02D1) - SDS Pro')]")
    select_tool_2d5 =       (By.XPATH, "//*[contains(text(),'7111 (0x02D5) - SDS Pro')]")
    select_tool_2e2 =       (By.XPATH, "//*[contains(text(),'7111 (0x02E2) - SDS Pro')]")
    select_tool_668 =       (By.XPATH, "//*[contains(text(),'7111 (0x0668) - SDS Pro')]")
    select_tool_2d6 =       (By.XPATH, "//*[contains(text(),'SDS43 (0x02D6) - SDS Inspector')]")
    select_tool_698 =       (By.XPATH, "//*[contains(text(),'SDS43 (0x0698) - SDS Inspector')]")
    select_tool_480 =       (By.XPATH, "//*[contains(text(),'SDS43a (0x0480) - SDS Inspector')]")
    select_tool_2d7 =       (By.XPATH, "//*[contains(text(),'SDS50 (0x02D7) - SDS Tech')]")
    submit =                (By.XPATH, "(//a[normalize-space()='SUBMIT'])[1]")
    title_request_help =    (By.XPATH, "(//span[normalize-space()='Request Help'])[1]")
    download_obd_updater =  (By.XPATH, "(//a[normalize-space()='Download OBD Tool Updater'])[1]")
    title_obd_updater =     (By.XPATH, "(//strong[normalize-space()='Updating the SDS Tool'])[1]")
    link_pdf_2d7 =          (By.XPATH, "(//a[contains(text(),'(0x02D7) SDS50_Release Note_V24.02.14_Jan262026.pd')])[1]")
    link_pdf_240415 =       (By.XPATH, "(//a[contains(text(),'(0x02D6) SDS43_Release Notes_V24.04.15_Jan232026.p')])[1]")
    link_pdf_698 =          (By.XPATH, "(//a[contains(text(),'(0x0698) SDS43_Release Notes_V24.04.15_Jan232026.p')])[1]")
    link_pdf_480 =          (By.XPATH, "(//a[contains(text(),'(0x0480) SDS43a_Release Notes_V24.04.18_Feb032026.')])[1]")
    link_pdf_7111_2812 =    (By.XPATH, "(//a[normalize-space()='INNOVA_7111_RN_v2.8.12.pdf'])[1]")


    def click_update_manuals(self):
        self.hover(self.support)
        self.wait.wait_for_element_visible(*self.update_manual).click()

    def select_tools_id(self):
        self.wait.wait_for_element_visible(*self.select_tools).click()

    def click_download_en(self):
        self.wait.wait_for_element_visible(*self.download_en).click()

    def click_download_es(self):
        self.wait.wait_for_element_visible(*self.download_es).click()

    def scroll_to_download_manual(self):
        self.scroll_to(self.download_es)

    def scroll_to_download_obd_updater(self):
        self.scroll_to(self.download_obd_updater)

    def select_tool_7111_2d1(self):
        self.wait.wait_for_element_visible(*self.select_tool_2d1).click()

    def select_tool_7111_2d5(self):
        self.wait.wait_for_element_visible(*self.select_tool_2d5).click()

    def select_tool_7111_2e2(self):
        self.wait.wait_for_element_visible(*self.select_tool_2e2).click()

    def select_tool_7111_668(self):
        self.wait.wait_for_element_visible(*self.select_tool_668).click()

    def select_tool_sds43_2d6(self):
        self.wait.wait_for_element_visible(*self.select_tool_2d6).click()

    def select_tool_sds43_698(self):
        self.wait.wait_for_element_visible(*self.select_tool_698).click()

    def select_tool_sds43_480(self):
        self.wait.wait_for_element_visible(*self.select_tool_480).click()

    def select_tool_sds50_2d7(self):
        self.wait.wait_for_element_visible(*self.select_tool_2d7).click()

    def click_submit_button(self):
        self.wait.wait_for_element_visible(*self.submit).click()

    def get_title(self):
        return self.wait.wait_for_element_visible(*self.title_request_help).text

    def click_download_obd_updater(self):
        self.wait.wait_for_element_visible(*self.download_obd_updater).click()

    def get_title_obd_updater(self):
        return self.wait.wait_for_element_visible(*self.title_obd_updater).text

    def click_link_pdf_2d7(self):
        self.wait.wait_for_element_visible(*self.link_pdf_2d7).click()

    def click_link_pdf_7111_2812(self):
        self.wait.wait_for_element_visible(*self.link_pdf_7111_2812).click()

    def click_link_pdf_sds43(self):
        self.wait.wait_for_element_visible(*self.link_pdf_240415).click()

    def click_link_pdf_698(self):
        self.wait.wait_for_element_visible(*self.link_pdf_698).click()

    def click_link_pdf_480(self):
        self.wait.wait_for_element_visible(*self.link_pdf_480).click()