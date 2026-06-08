import pytest
from webdriver_manager.core import driver
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.Support_Pages.SGW_AutoAuth_page import SGWAutoAuthPage
from utilities.custom_logger import LogMaker

@pytest.mark.SGW
class TestSGWAutoAuth:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()

    def test_verify_navigate_to_7111_page(self):
        self.logger.info("===== Verify that navigate to 7111 pages =====")
        sgw_auto_auth = SGWAutoAuthPage(self.driver)
        try:
            sgw_auto_auth.click_sgw_auto_auth()
            sgw_auto_auth.click_7111_page()
            self.logger.info("Click 7111")
            assert "7111" in sgw_auto_auth.get_text()
        except Exception as e:
            self.logger.failed("Can't navigate to 7111  page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_7111_page.png")
            assert False

    def test_verify_navigate_to_sds50_page(self):
        self.logger.info("===== Verify that navigate to SDS50 pages =====")
        sgw_auto_auth_sds50 = SGWAutoAuthPage(self.driver)
        try:
            sgw_auto_auth_sds50.click_sgw_auto_auth()
            sgw_auto_auth_sds50.click_sds50_page()
            self.logger.info("Click SDS50")
            assert "SDS50" in sgw_auto_auth_sds50.get_text()
        except Exception as e:
            self.logger.failed("Can't navigate to 7111 SDS50 SDS43 page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_sds50_page.png")
            assert False

    def test_verify_navigate_to_sds43_page(self):
        self.logger.info("===== Verify that navigate to SDS43 pages =====")
        sgw_auto_auth_sds43 = SGWAutoAuthPage(self.driver)
        try:
            sgw_auto_auth_sds43.click_sgw_auto_auth()
            sgw_auto_auth_sds43.click_sds43_page()
            self.logger.info("Click SD43")
            assert "SDS43" in sgw_auto_auth_sds43.get_text()
        except Exception as e:
            self.logger.failed("Can't navigate to 7111 SDS50 SDS43 page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_sds43_page.png")
            assert False
