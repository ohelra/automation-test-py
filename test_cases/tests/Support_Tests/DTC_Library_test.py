import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.Support_Pages.DTC_Library_page import DTCLibraryPage
from utilities.custom_logger import LogMaker
from utilities.json_reader import JsonReader

@pytest.mark.DTCLibrary
class TestDTCLibrary:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        request.cls.testdata = JsonReader("dtc_library.json")
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()


    def test_verify_search_dtc_library(self):
        """
        Step by step:
            1. Navigate to DTC Library
            2. Select make
            3. Enter DTC
            4. Click Submit
            5. Verify DTC display description
        """
        self.logger.info("===== Verify search DTC library =====")
        dtc_libraries = DTCLibraryPage(self.driver)
        test_data = self.testdata.get_data(None)
        dtc_libraries.click_dtc_library()
        errors = []
        for i, j in enumerate(test_data):
            make = j['make']
            code = j['code']
            expected = j['expected_desc']
            self.logger.info(f"DTC Lookup {i + 1}: Make: {make} | Code: {code} ")
            try:
                self.driver.refresh()
                self.logger.info("Click DTC Library Page")
                dtc_libraries.click_car_make()
                self.logger.info("Select make")
                dtc_libraries.enter_make_textbox(make)
                self.logger.info(f"Enter make {make}")
                dtc_libraries.search_dtc_library(code)
                self.logger.info(f"Enter code {code}")
                dtc_libraries.click_submit_button()
                self.logger.info("Enter submit button")
                if dtc_libraries.get_desc_table_text().strip() != expected.strip():
                    fail_msg = f"[FAIL] Make: {make}, Code: {code}. Expected: '{expected}', Got: '{dtc_libraries.get_desc_table_text()}'"
                    self.logger.error(fail_msg)
                    errors.append(fail_msg)
                    self.driver.save_screenshot(f".\\screenshots\\fail_{make}_{code}.png")
                else:
                    self.logger.info(f"[PASS] {make} - {code}")

            except Exception as e:
                crash_msg = f"[EXCEPTION] Error at {make} - {code}: {str(e)}"
                self.logger.failed(crash_msg, e)
                errors.append(crash_msg)
                self.driver.save_screenshot(f".\\screenshots\\exception_{make}_{code}.png")
        if errors:
            pytest.fail(f"Test failed with {len(errors)} issues:\n" + "\n".join(errors))


    def test_verify_clear_all_resets_inputs(self):
        """
        Step by step:
            1. Navigate to DTC Library
            2. Select a car make and enter a DTC code
            3. Click Submit to load results
            4. Click Clear All button
            5. Verify DTC code field is empty
        """
        self.logger.info("===== Verify Clear All Resets DTC Library Inputs =====")
        dtc = DTCLibraryPage(self.driver)
        try:
            self.driver.refresh()
            dtc.click_dtc_library()
            self.logger.info("Navigate to DTC Library")
            dtc.click_car_make()
            dtc.enter_make_textbox("TOYOTA")
            self.logger.info("Select make: TOYOTA")
            dtc.search_dtc_library("P0457")
            self.logger.info("Enter DTC code: P0457")
            dtc.click_submit_button()
            self.logger.info("Click Submit")
            dtc.click_clear_all_button()
            self.logger.info("Click Clear All")
            dtc_value = dtc.get_dtc_code_value()
            self.logger.info(f"DTC code field value after clear: '{dtc_value}'")
            assert dtc_value == "", f"DTC code field should be empty after Clear All, got: '{dtc_value}'"
            self.logger.passed("Clear All successfully resets the DTC code input")
        except Exception as e:
            self.logger.failed(f"Clear All did not reset inputs: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_clear_all_resets_inputs.png")
            assert False


    def test_verify_invalid_code_returns_no_results(self):
        """
        Step by step:
            1. Navigate to DTC Library
            2. Select a valid car make
            3. Enter an invalid/non-existent DTC code
            4. Click Submit
            5. Verify Invalid DTC code returns 'Definition Not Found
        """
        self.logger.info("===== Verify Invalid DTC Code Returns No Results =====")
        dtc = DTCLibraryPage(self.driver)
        try:
            self.driver.refresh()
            dtc.click_dtc_library()
            self.logger.info("Navigate to DTC Library")
            dtc.click_car_make()
            dtc.enter_make_textbox("TOYOTA")
            self.logger.info("Select make: TOYOTA")
            dtc.search_dtc_library("ZZZZZ9999")
            self.logger.info("Enter invalid DTC code: ZZZZZ9999")
            dtc.click_submit_button()
            self.logger.info("Click Submit")
            desc = dtc.get_desc_table_text().strip()
            self.logger.info(f"Description text: '{desc}'")
            assert desc == "Definition Not Found", f"Expected 'Definition Not Found', got '{desc}'"
            self.logger.passed("Invalid DTC code returns 'Definition Not Found' in the description column")
        except Exception as e:
            self.logger.failed(f"Invalid code test failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_invalid_code_returns_no_results.png")
            assert False


    def test_verify_can_click_delete_button(self):
        """
        Step by step:
            1. Navigate to DTC Library
            2. Select a valid car make
            3. Enter a DTC code
            4. Click Submit
            5. Click delete icon
            5. Verify the result will be removed from table
        """
        self.logger.info("===== Verify can click delete icon in the table =====")
        dtc = DTCLibraryPage(self.driver)
        try:
            self.driver.refresh()
            dtc.click_dtc_library()
            self.logger.info("Navigate to DTC Library")
            dtc.click_car_make()
            dtc.enter_make_textbox("NISSAN")
            self.logger.info("Select make: NISSAN")
            dtc.search_dtc_library("P0500")
            self.logger.info("Enter invalid DTC code: P0500")
            dtc.click_submit_button()
            self.logger.info("Click Submit")
            desc = dtc.get_desc_table_text().strip()
            self.logger.info(f"Description text: '{desc}'")
            dtc.click_delete_icon()
            self.logger.info("Click Delete Icon")
            row_count = dtc.get_table_row_count()
            assert row_count == 0, f"Table should be empty after delete, but still has {row_count} row(s)"
            self.logger.passed("The result will be removed from table")
        except Exception as e:
            self.logger.failed(f"Invalid code test failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_can_click_delete_button.png")
            assert False

    