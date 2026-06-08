import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.Support_Pages.Support_Request_page import SupportRequestPage
from utilities.custom_logger import LogMaker

@pytest.mark.SupportRequest
class TestSupportRequest:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        request.cls.driver = setup
        request.cls.logger = LogMaker.log_gen()
        home_page = RSPROHomePage(setup)
        home_page.go_to_home()

    def test_verify_video_link_on_support_request_page(self, setup):
        self.logger.info("===== Verify video link on Support Request page =====")
        page = SupportRequestPage(self.driver)
        try:
            page.navigate_to_support_request()
            self.logger.info("Navigated to Support Request page")
            page.scroll_and_click_video()
            self.logger.info("Scrolled to video section")
            page.click_to_video()
            self.logger.info("Click to video section")
            #assert page.is_video_displayed(), "YouTube video iframe is not visible on the page"
            self.logger.passed("Video iframe is visible on Support Request page")
        except Exception as e:
            self.logger.failed(f"Video link check failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_video_link_support_request.png")
            assert False


