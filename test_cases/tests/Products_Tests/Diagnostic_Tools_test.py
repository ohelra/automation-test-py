import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.Products_Pages.Diagnostic_Tools_Pages import DiagnosticToolsPage
from utilities.custom_logger import LogMaker

@pytest.mark.Diagnostic
class TestDiagnosticTools:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request,setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()

    # 7111 tool
    def test_verify_navigate_to_candian_shop(self):
        """
        Step by Step:
                1. Click Diagnostic Tools
                2. Scroll to 7111 tool
                3. Click Find a store
                4. Click Canadian store
                5. Verify that navigate to Canadian store URL
        """
        self.logger.info("===== Verify Navigate to Canadian Shop link of 7111 Tool =====")
        canadian_shop = DiagnosticToolsPage(self.driver)
        canadian_shop.click_diagnostic_tools()
        self.logger.info("Click Diagnostic Tools")
        canadian_shop.scroll_to_shop()
        self.logger.info("Scroll to 7111 Tool to find Canadian store")
        canadian_shop.click_find_a_store()
        self.logger.info("Click find a store button")
        canadian_shop.navigate_new_tab_with_url(canadian_shop.click_canadian_store, "canadiantire.ca")


    def test_verify_navigate_to_canadian_shop_by_list_view(self):
        """
        Step by Step:
                1. Click Diagnostic Tools
                2. Click List View icon
                3. Scroll to 7111 tool
                4. Click Find a store
                5. Click Canadian store
                6. Verify that navigate to Candian store URL
        """
        self.logger.info("===== Verify Navigate to Canadian Shop link by List View of 7111 Tool =====")
        canadian_shop = DiagnosticToolsPage(self.driver)
        self.driver.refresh()
        canadian_shop.click_diagnostic_tools()
        self.logger.info("Click Diagnostic Tools")
        canadian_shop.click_list_view()
        self.logger.info("Click List View icon")
        canadian_shop.scroll_to_shop_list_view()
        self.logger.info("Scroll to 7111 Tool to find Canadian store")
        canadian_shop.click_find_a_store_list_view()
        self.logger.info("Click find a store button by List View")
        canadian_shop.navigate_new_tab_with_url(canadian_shop.click_canadian_store, "canadiantire.ca")


    def test_verify_navigate_to_auto_parts_shop(self):
        """
        Step by Step:
                1. Click Diagnostic Tools
                2. Scroll to 7111 tool
                3. Click Find a store
                4. Click Auto Parts store
                5. Verify that navigate to Auto Parts store URL
        """
        self.logger.info("===== Verify Navigate to Auto Parts Shop link of 7111 Tool =====")
        auto_parts = DiagnosticToolsPage(self.driver)
        self.driver.refresh()
        auto_parts.click_diagnostic_tools()
        self.logger.info("Click Diagnostic Tools")
        auto_parts.scroll_to_shop()
        self.logger.info("Scroll to 7111 Tool to find Auto Parts store")
        auto_parts.click_find_a_store()
        self.logger.info("Click Find a Store button")
        auto_parts.navigate_new_tab_with_url(auto_parts.click_auto_parts_store, "napa")


    def test_verify_navigate_to_shop_by_list_view(self):
        """
        Step by Step:
                1. Click Diagnostic Tools
                2. Click List View icon
                3. Scroll to 7111 tool
                4. Click Find a store
                5. Click Auto Parts store
                6. Verify that navigate to Auto Parts store URL
        """
        self.logger.info("===== Verify Navigate to Auto Parts Shop link by List View of 7111 Tool =====")
        auto_parts = DiagnosticToolsPage(self.driver)
        self.driver.refresh()
        auto_parts.click_diagnostic_tools()
        self.logger.info("Click Diagnostic Tools")
        auto_parts.click_list_view()
        self.logger.info("Click List View icon")
        auto_parts.scroll_to_shop_list_view()
        self.logger.info("Scroll to 7111 Tool to find Auto Parts store")
        auto_parts.click_find_a_store_list_view()
        self.logger.info("Click Find a Store button")
        auto_parts.navigate_new_tab_with_url(auto_parts.click_auto_parts_store, "napa")


    def test_verify_navigate_to_7111_page_by_click_view(self):
        """
        Step by Step:
                1. Click Diagnostic Tools
                2. Click List View icon
                3. Click Product Detail button
                4. Verify that navigate to 7111 page by click view
        """
        self.logger.info("===== Verify Navigate to 7111 page by List View =====")
        page_7111 = DiagnosticToolsPage(self.driver)
        try:
            self.driver.refresh()
            page_7111.click_diagnostic_tools()
            self.logger.info("Click Diagnostic Tools")
            page_7111.click_list_view()
            self.logger.info("Click List View icon")
            page_7111.click_product_detail_7111_page()
            self.logger.info("Click Product Detail button")
            assert page_7111.navigate_to_7111_page() == "7111: Smart Diagnostic System Tablet", "Does matching"
        except Exception as e:
            self.logger.failed("Can't navigate to 7111 page by List View", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_7111_page_by_click_view.png")
            assert False

    # SDS50 tool
    def test_verify_navigate_to_auto_parts_of_sds50(self):
        """
        Step by Step:
                1. Click Diagnostic Tools
                2. Scroll to SDS50 tool
                3. Click Find a store
                4. Click Auto Parts store
                5. Verify that navigate to Auto Parts store URL
        """
        self.logger.info("===== Verify Navigate to Auto Parts Shop link of SDS50 Tool =====")
        sds50_tool = DiagnosticToolsPage(self.driver)
        self.driver.refresh()
        sds50_tool.click_diagnostic_tools()
        self.logger.info("Click Diagnostic Tools")
        sds50_tool.scroll_to_shop_sds50()
        self.logger.info("Scroll to SDS50 Tool to find Auto Parts store")
        sds50_tool.click_find_a_store_sds50()
        self.logger.info("Click Find a store")
        sds50_tool.navigate_new_tab_with_url(sds50_tool.click_auto_parts_sds50, "napa")


    def test_verify_navigate_to_auto_parts_of_sds50_by_list_view(self):
        """
        Step by Step:
                1. Click Diagnostic Tools
                2. Click List View icon
                3. Scroll to SDS50 tool
                4. Click Find a store
                5. Click Auto Parts store
                6. Verify that navigate to Auto Parts store URL
        """
        self.logger.info("===== Verify Navigate to Auto Parts Shop link by List View of SDS50 Tool =====")
        sds50_tool = DiagnosticToolsPage(self.driver)
        self.driver.refresh()
        sds50_tool.click_diagnostic_tools()
        self.logger.info("Click Diagnostic Tools")
        sds50_tool.click_list_view()
        self.logger.info("Click List View icon")
        sds50_tool.scroll_to_shop_sds50_list_view()
        self.logger.info("Scroll to SDS50 Tool to find Auto Parts store")
        sds50_tool.click_find_a_store_sds50_list_view()
        self.logger.info("Click Find a store by List View")
        sds50_tool.navigate_new_tab_with_url(sds50_tool.click_auto_parts_sds50, "napa")


    def test_verify_navigate_to_sds50_page_by_click_view(self):
        """
        Step by Step:
                1. Click Diagnostic Tools
                2. Click List View icon
                3. Scroll to SDS50
                4. Click Product Detail button
                5. Verify that navigate to SDS50 page
        """
        self.logger.info("===== Verify Navigate to SDS50 page by List View =====")
        page_sds50 = DiagnosticToolsPage(self.driver)
        try:
            self.driver.refresh()
            page_sds50.click_diagnostic_tools()
            self.logger.info("Click Diagnostic Tools")
            page_sds50.click_list_view()
            self.logger.info("Click List View icon")
            page_sds50.scroll_to_shop_sds50_list_view()
            self.logger.info("Scroll to SDS50 product detail")
            page_sds50.click_product_detail_sds50()
            self.logger.info("Click Product Detail button")
            assert page_sds50.navigate_to_sds50_page() == "SDS50: Smart Diagnostic System Tech"
        except Exception as e:
            self.logger.failed("Can't navigate to SDS50 page by List View", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_sds43_page_by_click_view.png")

    # SDS43 tool
    def test_verify_navigate_to_auto_parts_of_sds43(self):
        """
        Step by Step:
                1. Click Diagnostic Tools
                2. Scroll to SDS43 tool
                3. Click Find a store
                4. Click Auto Parts store
                5. Verify that navigate to Auto Parts store URL
        """
        self.logger.info("===== Verify Navigate to Auto Parts Shop link of SDS43 Tool ====")
        sds43_tool = DiagnosticToolsPage(self.driver)
        self.driver.refresh()
        sds43_tool.click_diagnostic_tools()
        self.logger.info("Click Diagnostic Tools")
        sds43_tool.scroll_to_shop_sds43()
        self.logger.info("Scroll to SDS43 Tool to find Auto Parts store")
        sds43_tool.click_find_a_store_sds43()
        self.logger.info("Click find a store")
        sds43_tool.navigate_new_tab_with_url(sds43_tool.click_auto_parts_sds43, "napa")


    def test_verify_navigate_to_auto_parts_of_sds43_page_by_click_view(self):
        """
         Step by Step:
                1. Click Diagnostic Tools
                2. Click List View icon
                3. Scroll to SDS43 tool
                4. Click Find a store
                5. Click Auto Parts store
                6. Verify that navigate to Auto Parts store URL
        """
        self.logger.info("===== Verify Navigate to Auto Parts Shop link by List View of SDS43 Tool ====")
        sds43_tool = DiagnosticToolsPage(self.driver)
        self.driver.refresh()
        sds43_tool.click_diagnostic_tools()
        self.logger.info("Click Diagnostic Tools")
        sds43_tool.click_list_view()
        self.logger.info("Click List View icon")
        sds43_tool.scroll_to_shop_sds43_list_view()
        self.logger.info("Scroll to SDS43 Tool to find Auto Parts store")
        sds43_tool.click_find_a_store_sds43_list_view()
        self.logger.info("Click find a store by List View")
        sds43_tool.navigate_new_tab_with_url(sds43_tool.click_auto_parts_sds43, "napa")


    def test_verify_grid_list_view_toggle(self):
        """
        Step by step:
            1. Click Diagnostic Tools
            2. Verify Grid View is active by default
            3. Click List View icon
            4. Verify List View becomes active
            5. Click Grid View icon
            6. Verify Grid View is active again
        """
        self.logger.info("===== Verify Grid and List View Toggle =====")
        view_toggle = DiagnosticToolsPage(self.driver)
        try:
            self.driver.refresh()
            view_toggle.click_diagnostic_tools()
            self.logger.info("Click Diagnostic Tools")
            assert view_toggle.is_grid_view_active(), "Grid View should be active by default"
            self.logger.info("Grid View is active by default")
            view_toggle.click_list_view()
            self.logger.info("Click List View icon")
            assert view_toggle.is_list_view_active(), "List View should be active after click"
            self.logger.info("List View is now active")
            view_toggle.click_grid_view()
            self.logger.info("Click Grid View icon")
            assert view_toggle.is_grid_view_active(), "Grid View should be active after clicking back"
            self.logger.passed("Grid and List view toggle works correctly")
        except Exception as e:
            self.logger.failed(f"View toggle verification failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_grid_list_view_toggle.png")
            assert False


    def test_verify_navigate_to_sds43_page_by_click_view(self):
        """
        Step by Step:
                1. Click Diagnostic Tools
                2. Click List View icon
                3. Scroll to SDS43
                4. Click Product Detail button
                5. Verify that navigate to SDS43 page
        """
        self.logger.info("===== Verify Navigate to SDS43 page by List View =====")
        page_sds43 = DiagnosticToolsPage(self.driver)
        try:
            self.driver.refresh()
            page_sds43.click_diagnostic_tools()
            self.logger.info("Click Diagnostic Tools")
            page_sds43.click_list_view()
            self.logger.info("Click List View icon")
            page_sds43.scroll_to_shop_sds43_list_view()
            self.logger.info("Scroll to SDS43 page")
            page_sds43.click_product_detail_sds43()
            self.logger.info("Click Product Detail button")
            assert page_sds43.navigate_to_sds43_page() == "SDS43: Smart Diagnostic System Inspector"
        except Exception as e:
            self.logger.failed("Can't navigate to SDS50 page by List View", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_sds43_page_by_click_view.png")