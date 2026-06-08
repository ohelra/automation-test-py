import time
import pytest
from base_pages.pages.HomePage_Pages.Introduction_Features_Page import IntroductionFeaturesPage
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from utilities.custom_logger import LogMaker

@pytest.mark.IntroductionFeatures
class TestIntroductionFeatures:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()

    @pytest.mark.flaky(reruns=2, reruns_delay=3)
    def test_verify_fix_for_dtc_hover_shows_modal_fix(self, setup):
        """
            Step by step:
                1. Navigate to Home Page
                2. Scroll to Fix For DTC
                3. Hover over Fix For DTC
                4. Verify 'show' in ipad-model
        """
        self.logger.info("===== Verify Fix For DTC Hover Shows Modal =====")
        fix_for_dtc = IntroductionFeaturesPage(self.driver)
        try:
            fix_for_dtc.scroll_to_fix_for_dtc()
            self.logger.info("Scroll to Fix For DTC")
            fix_for_dtc.hover_fix_for_dtc()
            self.logger.info("Hover over Fix For DTC")
            #assert "show" in fix_for_dtc.wait_for_modal_show_dtc(), f"Expected 'show' in ipad-modal class but nothing"
            assert fix_for_dtc.is_modal_displayed()
            self.logger.passed("Fix For DTC modal displayed successfully with zoom out animation")
        except Exception as e:
            self.logger.failed("Fix For DTC modal does not display", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_fix_for_dtc_hover_shows_modal_fix.png")
            assert False

    @pytest.mark.flaky(reruns=2, reruns_delay=3)
    def test_verify_repair_tips_hover_shows_modal(self, setup):
        """
            Step by step:
                 1. Navigate to Home Page
                 2. Scroll to Repair Tips
                 3. Hover over Repair Tips
                 4. Verify 'show' in ipad-model
        """
        self.logger.info("===== Verify Repair Tips Hover Shows Modal =====")
        repair_tips = IntroductionFeaturesPage(self.driver)
        try:
            self.driver.refresh()
            repair_tips.scroll_to_repair_tips()
            self.logger.info("Scroll to Repair Tips")
            repair_tips.hover_repair_tips()
            self.logger.info("Hover to Repair Tips")
            #assert "show" in repair_tips.wait_for_modal_show_repair(), f"Expected 'show' in ipad-modal class but nothing"
            time.sleep(3)
            assert repair_tips.is_modal_displayed_repair()
            self.logger.passed("Repair Tips modal displayed successfully with zoom out animation")
        except Exception as e:
            self.logger.failed(f"Repair Tips modal does not display. {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_repair_tips_hover_shows_modal.png")
            assert False

    @pytest.mark.flaky(reruns=2, reruns_delay=3)
    def test_verify_vehicle_inspection_report_hover_shows_modal(self, setup):
        """
            Step by step:
                 1. Navigate to Home Page
                 2. Scroll to Vehicle Inspection Report
                 3. Hover over Vehicle Inspection Report
                 4. Verify 'show' in ipad-model
        """
        self.logger.info("===== Verify Vehicle Inspection Report Hover Shows Modal =====")
        vehicle_ir = IntroductionFeaturesPage(self.driver)
        try:
            self.driver.refresh()
            vehicle_ir.scroll_to_vehicle_inspection_report()
            self.logger.info("Scroll to Vehicle Inspection Report")
            vehicle_ir.hover_vehicle_inspection_report()
            self.logger.info("Hover over Vehicle Inspection Report")
            #assert "show" in vehicle_ir.wait_for_modal_show_vehicle(), f"Expected 'show' in ipad-modal class but nothing"
            assert vehicle_ir.is_modal_displayed_vehicle()
            self.logger.passed("Vehicle Inspection Report modal displayed successfully with zoom out animation")
        except Exception as e:
            self.logger.failed("Vehicle Inspection Report modal does not display",e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_vehicle_inspection_report_hover_shows_modal.png")
            assert False

    def test_verify_indicators_changes_color_number_1(self,setup):
        """
         Step by step:
                 1. Navigate to Home Page
                 2. Scroll to Indicator numbers
                 3. Hover over each number in order 1, 2, 3, 4
                 4. Verify that the color of each number changes
        """
        self.logger.info("===== Verify indicators number changed color number 1,2,3,4 =====")
        get_color = IntroductionFeaturesPage(self.driver)
        expected_color_rgb = 'rgb(106, 153, 204)'
        try:
            self.driver.refresh()
            get_color.scroll_to_get_color()                                             # Scroll to numbers color
            self.logger.info("Scroll to Obtain an SDS Diagnostics Tablet")

            get_color_default_1 = get_color.get_color_1_default()                       # Get default color 1
            self.logger.info("Before color changed was D6E3F1")
            assert "#d6e3f1" in get_color_default_1.lower() or "rgb(214, 227, 241)" in get_color_default_1 or "rgba(214, 227, 241, 1)" in get_color_default_1
            self.logger.info(f"Get Color {get_color_default_1.lower()}")
            get_color.hover_1_obtain()                                                  # hover and get new color
            self.logger.info("Hover to 1 : Obtain an SDS Diagnostics Tablet")
            changed_background_color_1 = get_color.get_color_1_changed()                # Get background-image (contains linear-gradient)
            self.logger.info(f"Changed background {changed_background_color_1}")
            assert "linear-gradient" in changed_background_color_1 and expected_color_rgb in changed_background_color_1

            get_color_default_2 = get_color.get_color_2_default()
            self.logger.info("Before color changed was D6E3F1")
            assert "#d6e3f1" in get_color_default_2.lower() or "rgb(214, 227, 241)" in get_color_default_2 or "rgba(214, 227, 241, 1)" in get_color_default_2
            self.logger.info(f"Get Color {get_color_default_2.lower()}")
            get_color.hover_2_obtain()
            self.logger.info("Hover to 2 : Obtain an SDS Diagnostics Tablet")
            changed_background_color_2 = get_color.get_color_2_changed()
            self.logger.info(f"Changed background {changed_background_color_2}")
            assert "linear-gradient" in changed_background_color_2 and expected_color_rgb in changed_background_color_2

            get_color_default_3 = get_color.get_color_3_default()
            self.logger.info("Before color changed was D6E3F1")
            assert "#d6e3f1" in get_color_default_3.lower() or "rgb(214, 227, 241)" in get_color_default_3 or "rgba(214, 227, 241, 1)" in get_color_default_3
            self.logger.info(f"Get Color {get_color_default_3.lower()}")
            get_color.hover_3_obtain()
            self.logger.info("Hover to 3 : Obtain an SDS Diagnostics Tablet")
            changed_background_color_3 = get_color.get_color_3_changed()
            self.logger.info(f"Changed background {changed_background_color_3}")
            assert "linear-gradient" in changed_background_color_3 and expected_color_rgb in changed_background_color_3

            get_color_default_4 = get_color.get_color_4_default()
            self.logger.info("Before color changed was D6E3F1")
            assert "#d6e3f1" in get_color_default_4.lower() or "rgb(214, 227, 241)" in get_color_default_4 or "rgba(214, 227, 241, 1)" in get_color_default_4
            self.logger.info(f"Get Color {get_color_default_4.lower()}")
            get_color.hover_4_obtain()
            self.logger.info("Hover to 4 : Obtain an SDS Diagnostics Tablet")
            changed_background_color_4 = get_color.get_color_4_changed()
            assert "linear-gradient" in changed_background_color_4 and expected_color_rgb in changed_background_color_4

            self.logger.info(f"SUCCESS: Background changed to linear-gradient containing {expected_color_rgb}.")
        except Exception as e:
            self.logger.failed("Get color visibility Failed",e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_indicators_changes_color_numbers.png")
            assert False

    def test_verify_three_device_get_together(self, setup):
        """
            Step by step:
                 1. Navigate to Home Page
                 2. Scroll to three devices
                 3. Hover over the middle of three devices
                 4. Verify that the default location has changed
        """
        self.logger.info("===== Verify three device move together =====")
        devices_page = IntroductionFeaturesPage(self.driver)
        self.driver.refresh()
        try:
            self.driver.refresh()
            devices_page.scroll_to_grid_2_box()
            self.logger.info("Scroll to the three-device animation section.")
            default_positions = devices_page.get_device_positions()  # Get default value
            self.logger.info(f"Default positions: {default_positions}")
            devices_page.hover_grid_box()
            self.logger.info("Hover over the device box to trigger movement.")
            after_position = devices_page.get_device_positions()
            self.logger.info(f"Hover positions: {after_position}")
            time.sleep(1)
            assert default_positions['tablet_left'] != after_position['tablet_left']
        except Exception as e:
            self.logger.error("Three-device movement verification Failed", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_three_device_get_together.png")
            assert False

    def test_verify_mobile_zoom_out(self, setup):
        """
            Step by step:
                 1. Navigate to Home Page
                 2. Scroll to mobile phone
                 3. Hover over the middle of mobile phone
                 4. Verify that the default location has changed
        """
        self.logger.info("===== Verify mobile zoom in =====")
        mobile_page = IntroductionFeaturesPage(self.driver)
        self.driver.refresh()
        expected_matrix_scale = 'matrix(1.135, 0, 0, 1.135, 0, 0)'
        default_matrix_scale =  'matrix(1, 0, 0, 1, 0, 0)'
        try:
            self.driver.refresh()
            mobile_page.scroll_to_mobile_device()
            self.logger.info("Scroll to mobile device section.")
            default_scale = mobile_page.get_mobile_scale_default()                  # Get value Default
            self.logger.info(f"Default scale transform: {default_scale}")
            is_default_scale_correct = (default_scale == default_matrix_scale or default_scale == 'none')
            assert is_default_scale_correct, \
                f"FAIL: Scale default invalid. Expected: 'none' or '{default_matrix_scale}'. Actual: {default_scale}"
            mobile_page.hover_mobile_device()                                       # Hover mobile
            self.logger.info("Hover over the animation frame.")
            changed_scale = mobile_page.get_mobile_scale_after_hover()              # Get value after hovering
            self.logger.info(f"Scale transform after hover: {changed_scale}")
            assert changed_scale == expected_matrix_scale, \
                f"FAIL: Mobile device did not zoom correctly. Expected: {expected_matrix_scale}. Actual: {changed_scale}"
            self.logger.info("SUCCESS: Mobile device successfully zoomed out (scale 1.135) on hover.")
        except Exception as e:
            self.logger.error("Mobile device zoom effect verification Failed", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_mobile_device_zooms_on_hover.png")
            assert False