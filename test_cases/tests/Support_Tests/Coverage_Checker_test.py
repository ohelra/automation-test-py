import json
import os
import time

import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.Support_Pages.Coverage_Checker_page import CoverageCheckerPage
from utilities.custom_logger import LogMaker
from utilities.json_reader import JsonReader


@pytest.mark.CoverageChecker
class TestCoverageChecker:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        request.cls.testdata = JsonReader("coverage_checker.json")
        request.cls.home_page = RSPROHomePage(driver)
        request.cls.home_page.go_to_home()

    # ─────────────────────────────────────────────────────────────────────────
    # Navigation — TC_001
    # ─────────────────────────────────────────────────────────────────────────

    def test_navigate_to_coverage_checker(self):
        """
        TC_001 - P1 Navigation
        Steps:
            1. Hover Support menu -> click Coverage Checker
            2. Verify page title is 'Coverage Checker'
        """
        self.logger.info("===== TC_001: Navigate to Coverage Checker via Support menu =====")
        page = CoverageCheckerPage(self.driver)
        try:
            page.click_coverage_checker()
            self.logger.info("Clicked Coverage Checker from Support menu")
            title = page.get_page_title()
            assert "COVERAGE CHECKER" in title.upper(), f"Expected 'Coverage Checker', got '{title}'"
            self.logger.passed("TC_001 PASS - Page title matches 'Coverage Checker'")
        except Exception as e:
            self.logger.failed(f"TC_001 FAIL: {e}")
            self.driver.save_screenshot(".\\screenshots\\tc001_navigate_coverage_checker.png")
            assert False

    # ─────────────────────────────────────────────────────────────────────────
    # Form — TC_003: Tool dropdown options
    # ─────────────────────────────────────────────────────────────────────────

    def test_submit_valid_data_results_appear(self):
        """
        Steps:
            1. Navigate to Coverage Checker
            2. Select Tool, Year, Make, Model, Engine from JSON
            3. Click SUBMIT
        """
        self.logger.info("===== Verify that submit valid data result appear =====")
        page = CoverageCheckerPage(self.driver)
        test_data = self.testdata.get_data(None)

        for i, data in enumerate(test_data):
            tool = data["tool"]
            year = data["year"]
            make = data["make"]
            model = data["model"]
            engine = data["engine"]
            self.logger.info(f"Coverage Lookup {i + 1}: Tool: {tool} | Car: {year} {make} {model}")
            try:
                self.driver.refresh()
                page.click_coverage_checker()
                self.logger.info("Click Coverage Checker")
                page.select_tool_info(tool)
                self.logger.info(f"Click and enter select tool info : {tool}")
                page.select_year(year)
                self.logger.info(f"Click and enter select year : {year}")
                page.select_make(make)
                self.logger.info(f"Click and enter select make : {make}")
                page.select_model(model)
                self.logger.info(f"Click and enter select model : {model}")
                page.select_engine(engine)
                self.logger.info(f"Click and enter select engine : {engine}")
                page.click_submit()
                self.logger.info("Click submit")
                time.sleep(3)
                assert page.is_obd_diagnostic_visible()
                page.is_oem_diagnostic_visible()
                self.logger.info("Click OEM Diagnostic")
                assert page.oem_display()
                page.click_workshop_tool()
                self.logger.info("Click Workshop Tool")
                assert page.is_workshop_tool_visible()
                self.logger.passed(f"Coverage Lookup {i + 1}: OK")
            except Exception as e:
                self.logger.failed(f"Not navigate tab: {e}")
                self.driver.save_screenshot(f".\\screenshots\\exception_coverage_{tool}_{make}.png")
                assert False

    # ─────────────────────────────────────────────────────────────────────────
    # Results sections — TC_007 / TC_008
    # ─────────────────────────────────────────────────────────────────────────

    def test_results_contain_obd_diagnostic_section(self):
        """
        TC_007 - P1 Functional
        Data: coverage_checker.json -> valid_vehicles[0]
        Steps:
            1. Submit form using JSON test data
            2. Verify OBD II Diagnostics section is visible in results
        """
        self.logger.info("===== TC_007: Verify OBD II Diagnostics in results =====")
        self.logger.info(f"[DATA] Tool={TOOL} | Year={YEAR} | Make={MAKE} | Model={MODEL} | Engine={ENGINE}")
        page = CoverageCheckerPage(self.driver)
        try:
            page.go_to_coverage_checker()
            page.fill_and_submit(TOOL, YEAR, MAKE, MODEL, ENGINE)
            self.logger.info(f"Form submitted - checking OBD II Diagnostics section")
            assert page.is_obd_diagnostic_visible(), \
                "OBD II Diagnostics section not visible in results"
            self.logger.passed("TC_007 PASS - OBD II Diagnostics section is visible")
        except Exception as e:
            self.logger.failed(f"TC_007 FAIL: {e}")
            self.driver.save_screenshot(".\\screenshots\\tc007_obd_diagnostic.png")
            assert False


    def test_results_contain_oem_diagnostic_section(self):
        """
        TC_008 - P1 Functional
        Data: coverage_checker.json -> valid_vehicles[0]
        Steps:
            1. Submit form using JSON test data
            2. Verify OEM Diagnostics section is visible in results
        """
        self.logger.info("===== TC_008: Verify OEM Diagnostics in results =====")
        self.logger.info(f"[DATA] Tool={TOOL} | Year={YEAR} | Make={MAKE} | Model={MODEL} | Engine={ENGINE}")
        page = CoverageCheckerPage(self.driver)
        try:
            page.go_to_coverage_checker()
            page.fill_and_submit(TOOL, YEAR, MAKE, MODEL, ENGINE)
            self.logger.info(f"Form submitted - checking OEM Diagnostics section")
            assert page.is_oem_diagnostic_visible(), \
                "OEM Diagnostics section not visible in results"
            self.logger.passed("TC_008 PASS - OEM Diagnostics section is visible")
        except Exception as e:
            self.logger.failed(f"TC_008 FAIL: {e}")
            self.driver.save_screenshot(".\\screenshots\\tc008_oem_diagnostic.png")
            assert False
