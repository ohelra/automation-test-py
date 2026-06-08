import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.Support_Pages.DLC_Locator_page import DLCLocatorPage
from utilities.custom_logger import LogMaker
from utilities.dlc_image_detector import detect_highlighted_dlc_location_from_url
from utilities.json_reader import JsonReader

vin_data = JsonReader("dlc_locator.json").get_data(None)[1]["vins"]

@pytest.mark.DLCLocator
class TestDLCLocator:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        request.cls.testdata = JsonReader("dlc_locator.json")
        request.cls.home_page = RSPROHomePage(driver)
        request.cls.home_page.go_to_home()

    def test_verify_location_2_matches_dlc_diagram(self):
        """
        Step by step:
            1. Open DLC Locator page
            2. Select Make, Year, and Model
            3. Submit the DLC Locator search
            4. Verify result location is 2
            5. Verify the displayed DLC diagram image is location 2
        Expected: The table location and diagram image both show DLC location 2.
        """
        self.logger.info("===== Verify DLC Locator matches diagram in the table=====")
        dlc_locator = DLCLocatorPage(self.driver)
        test_data = self.testdata.get_data(None)[0]
        make = test_data["make"]
        year = test_data["year"]
        model = test_data["model"]
        expected_location = str(test_data["expected_location"])
        try:
            dlc_locator.click_dlc_locator()
            self.logger.info("Open DLC Locator page")
            dlc_locator.search_by_ymm(make, year, model)
            self.logger.info(f"Search DLC Locator for {year} {make} {model}")
            actual_location = dlc_locator.get_location_text()
            dlc_locator.scroll_to_dlc_image()
            self.logger.info(f"Scroll to DLC diagram image for location {expected_location}")
            image_src = dlc_locator.get_dlc_image_src()
            visual_location = detect_highlighted_dlc_location_from_url(image_src)
            result_message = dlc_locator.get_result_message_text()
            self.logger.info(f"Result message: {result_message}")
            self.logger.info(f"Location: {actual_location} | Visual image location: {visual_location} | Image: {image_src}")
            assert actual_location == expected_location, f"Expected location '{expected_location}', got '{actual_location}'"
            assert visual_location == actual_location, f"Expected highlighted image location '{actual_location}', got '{visual_location}'"
            self.logger.passed("DLC Locator table location matches the highlighted number in the diagram image")
        except Exception as e:
            self.logger.failed(f"DLC Locator location 2 verification failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_dlc_locator_location_2.png")
            assert False


    @pytest.mark.parametrize("vin", vin_data)
    def test_verify_vin_search_location_matches_dlc_diagram(self, vin):
        """
        Step by step:
            1. Open DLC Locator page
            2. Enter VIN without selecting Make, Year, or Model
            3. Submit the VIN search
            4. Read the result table location
            5. Verify the displayed DLC diagram highlights the same location number
        Expected: The VIN result table location matches the highlighted number in the DLC diagram image.
        """
        self.logger.info("===== Verify DLC Locator VIN search diagram location =====")
        dlc_locator = DLCLocatorPage(self.driver)
        try:
            self.home_page.go_to_home()
            dlc_locator.click_dlc_locator()
            self.logger.info("Open DLC Locator page")
            dlc_locator.search_by_vin(vin)
            self.logger.info(f"Search DLC Locator by VIN: {vin}")
            actual_location = dlc_locator.get_location_text()
            dlc_locator.scroll_to_dlc_image()
            self.logger.info(f"Scroll to DLC diagram image for table location {actual_location}")
            image_src = dlc_locator.get_dlc_image_src()
            visual_location = detect_highlighted_dlc_location_from_url(image_src)
            result_message = dlc_locator.get_result_message_text()
            self.logger.info(f"Result message: {result_message}")
            self.logger.info(f"VIN: {vin} | Location: {actual_location} | Visual image location: {visual_location} | Image: {image_src}")
            assert visual_location == actual_location, f"Expected highlighted image location '{actual_location}', got '{visual_location}' for VIN '{vin}'"
            self.logger.passed(f"DLC Locator VIN result matches the highlighted diagram location for VIN: {vin}")
        except Exception as e:
            self.logger.failed(f"DLC Locator VIN location verification failed for '{vin}': {e}")
            self.driver.save_screenshot(f".\\screenshots\\test_verify_dlc_locator_vin_{vin}.png")
            assert False
