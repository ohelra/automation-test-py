import pytest
from webdriver_manager.core import driver
from utilities.custom_logger import LogMaker
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.Support_Pages.Support_Request_page import SupportRequestPage
from base_pages.pages.Support_Pages.Update_Manual_page import UpdateManualPage

@pytest.mark.SupportRequest
class TestUpdateManual:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        home_page = RSPROHomePage(setup)
        home_page.go_to_home()
        request.cls.page = UpdateManualPage(driver)

    def test_verify_download_manual_7111_2d1(self):
        """
        Step by step:
            1. Navigate to Coverage Checker
            2. Select 7111 (0x02D1) - SDS Pro
            3. Click download Manual (English)
            4. Click download Manual (Spanish)
            5. Click pdf to download manual file
        """
        self.logger.info("===== Verify that download manual 7111 0x02D1 =====")
        try:
            self.page.click_update_manuals()
            self.logger.info("Click Updates/Manuals")
            self.page.select_tools_id()
            self.logger.info("Click tool id")
            self.page.select_tool_7111_2d1()
            self.logger.info("Select 7111 0x02D1")
            self.page.click_submit_button()
            self.logger.info("Click submit button")
            self.page.scroll_to_download_manual()
            self.logger.info("Scroll to download manual")
            self.page.navigate_new_tab_with_url(self.page.click_download_en,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_download_es,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_link_pdf_7111_2812, "rs-pro.s3.amazonaws")
        except Exception as e:
            self.logger.failed(f"Cannot open new tab download both En and Es : {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_download_manual_7111_2d1.png")
            assert False


    def test_verify_download_manual_7111_2d5(self):
        """
        Step by step:
            1. Navigate to Coverage Checker
            2. Select 7111 (0x02D5) - SDS Pro
            3. Click download Manual (English)
            4. Click download Manual (Spanish)
            5. Click pdf to download manual file
        """
        self.logger.info("===== Verify that download manual 7111 0x02D5 =====")
        try:
            self.page.click_update_manuals()
            self.logger.info("Click Updates/Manuals")
            self.page.select_tools_id()
            self.logger.info("Click tool id")
            self.page.select_tool_7111_2d5()
            self.logger.info("Select 7111 0x02D5")
            self.page.click_submit_button()
            self.logger.info("Click submit button")
            self.page.scroll_to_download_manual()
            self.logger.info("Scroll to download manual")
            self.page.navigate_new_tab_with_url(self.page.click_download_en,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_download_es,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_link_pdf_7111_2812, "rs-pro.s3.amazonaws")
        except Exception as e:
            self.logger.failed(f"Cannot open new tab download both En and Es : {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_download_manual_7111_2d5.png")
            assert False


    def test_verify_download_manual_7111_2e2(self):
        """
        Step by step:
            1. Navigate to Coverage Checker
            2. Select 7111 (0x02E2) - SDS Pro
            3. Click download Manual (English)
            4. Click download Manual (Spanish)
            5. Click pdf to download manual file
        """
        self.logger.info("===== Verify that download manual 7111 0x02E2 =====")
        try:
            self.page.click_update_manuals()
            self.logger.info("Click Updates/Manuals")
            self.page.select_tools_id()
            self.logger.info("Click tool id")
            self.page.select_tool_7111_2e2()
            self.logger.info("Select 7111 0x02E2")
            self.page.click_submit_button()
            self.logger.info("Click submit button")
            self.page.scroll_to_download_manual()
            self.logger.info("Scroll to download manual")
            self.page.navigate_new_tab_with_url(self.page.click_download_en,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_download_es,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_link_pdf_7111_2812, "rs-pro.s3.amazonaws")
        except Exception as e:
            self.logger.failed(f"Cannot open new tab download both En and Es : {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_download_manual_7111_2e2.png")
            assert False


    def test_verify_download_manual_7111_668(self):
        """
        Step by step:
            1. Navigate to Coverage Checker
            2. Select 7111 (0x0668) - SDS Pro
            3. Click download Manual (English)
            4. Click download Manual (Spanish)
            5. Click pdf to download manual file
        """
        self.logger.info("===== Verify that download manual 7111 0x668 =====")
        try:
            self.page.click_update_manuals()
            self.logger.info("Click Updates/Manuals")
            self.page.select_tools_id()
            self.logger.info("Click tool id")
            self.page.select_tool_7111_668()
            self.logger.info("Select 7111 0x0668")
            self.page.click_submit_button()
            self.logger.info("Click submit button")
            self.page.scroll_to_download_manual()
            self.logger.info("Scroll to download manual")
            self.page.navigate_new_tab_with_url(self.page.click_download_en,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_download_es,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_link_pdf_7111_2812, "rs-pro.s3.amazonaws")
        except Exception as e:
            self.logger.failed(f"Cannot open new tab download both En and Es : {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_download_manual_7111_668.png")
            assert False


    def test_verify_download_manual_sds43_2d6(self):
        """
        Step by step:
            1. Navigate to Coverage Checker
            2. Select SDS43 (0x02D6) - SDS Inspector
            3. Click download Manual (English)
            4. Click download Manual (Spanish)
            5. Click pdf to download manual file
        """
        self.logger.info("===== Verify that download manual 7111 0x668 =====")
        try:
            self.page.click_update_manuals()
            self.logger.info("Click Updates/Manuals")
            self.page.select_tools_id()
            self.logger.info("Click tool id")
            self.page.select_tool_sds43_2d6()
            self.logger.info("Select SDS43 0x02D6")
            self.page.click_submit_button()
            self.logger.info("Click submit button")
            self.page.scroll_to_download_obd_updater()
            self.logger.info("Scroll to download manual")
            self.page.navigate_new_tab_with_url(self.page.click_download_en,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_download_es,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_link_pdf_sds43, "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab(self.page.click_download_obd_updater, "innova-tool-firmware-update-instructions",
                                       self.page.get_title_obd_updater, "Updating the SDS Tool")
        except Exception as e:
            self.logger.failed(f"Cannot open new tab download both En and Es : {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_download_manual_sds43_2d6.png")
            assert False


    def test_verify_download_manual_sds43_698(self):
        """
        Step by step:
            1. Navigate to Coverage Checker
            2. Select SDS43 (0x0698) - SDS Inspector
            3. Click download Manual (English)
            4. Click download Manual (Spanish)
            5. Click pdf to download manual file
        """
        self.logger.info("===== Verify that download manual 7111 0x668 =====")
        try:
            self.page.click_update_manuals()
            self.logger.info("Click Updates/Manuals")
            self.page.select_tools_id()
            self.logger.info("Click tool id")
            self.page.select_tool_sds43_698()
            self.logger.info("Select SDS43 0x0698")
            self.page.click_submit_button()
            self.logger.info("Click submit button")
            self.page.scroll_to_download_obd_updater()
            self.logger.info("Scroll to download manual")
            self.page.navigate_new_tab_with_url(self.page.click_download_en,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_download_es,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_link_pdf_698, "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab(self.page.click_download_obd_updater, "innova-tool-firmware-update-instructions",
                                       self.page.get_title_obd_updater, "Updating the SDS Tool")
        except Exception as e:
            self.logger.failed(f"Cannot open new tab download both En and Es : {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_download_manual_sds43_698.png")
            assert False


    def test_verify_download_manual_sds43_480(self):
        """
        Step by step:
            1. Navigate to Coverage Checker
            2. Select SDS43 (0x0480) - SDS Inspector
            3. Click download Manual (English)
            4. Click download Manual (Spanish)
            5. Click pdf to download manual file
        """
        self.logger.info("===== Verify that download manual 7111 0x668 =====")
        try:
            self.page.click_update_manuals()
            self.logger.info("Click Updates/Manuals")
            self.page.select_tools_id()
            self.logger.info("Click tool id")
            self.page.select_tool_sds43_480()
            self.logger.info("Select SDS43 0x0480")
            self.page.click_submit_button()
            self.logger.info("Click submit button")
            self.page.scroll_to_download_obd_updater()
            self.logger.info("Scroll to download manual")
            self.page.navigate_new_tab_with_url(self.page.click_download_en,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_download_es,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_link_pdf_480, "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab(self.page.click_download_obd_updater, "innova-tool-firmware-update-instructions",
                                       self.page.get_title_obd_updater, "Updating the SDS Tool")
        except Exception as e:
            self.logger.failed(f"Cannot open new tab download both En and Es : {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_download_manual_sds43_698.png")
            assert False


    def test_verify_download_manual_sds50_2d7(self):
        """
        Step by step:
            1. Navigate to Coverage Checker
            2. Select SDS50 (0x02D7) - SDS Tech
            3. Click download Manual (English)
            4. Click download Manual (Spanish)
            5. Click pdf to download manual file
        """
        self.logger.info("===== Verify that download manual 7111 0x668 =====")
        try:
            self.page.click_update_manuals()
            self.logger.info("Click Updates/Manuals")
            self.page.select_tools_id()
            self.logger.info("Click tool id")
            self.page.select_tool_sds50_2d7()
            self.logger.info("Select SDS50 0x02D7")
            self.page.click_submit_button()
            self.logger.info("Click submit button")
            self.page.scroll_to_download_obd_updater()
            self.logger.info("Scroll to download manual")
            self.page.navigate_new_tab_with_url(self.page.click_download_en,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_download_es,  "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab_with_url(self.page.click_link_pdf_2d7, "rs-pro.s3.amazonaws")
            self.page.navigate_new_tab(self.page.click_download_obd_updater, "innova-tool-firmware-update-instructions",
                                       self.page.get_title_obd_updater, "Updating the SDS Tool")
        except Exception as e:
            self.logger.failed(f"Cannot open new tab download both En and Es : {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_download_manual_sds43_698.png")
            assert False

