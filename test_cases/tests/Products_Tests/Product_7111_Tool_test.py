import time
import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.Products_Pages.Product_7111_Tool_Pages import Product7111ToolPage
from utilities.custom_logger import LogMaker
from utilities.json_reader import JsonReader

@pytest.mark.Product7111
class TestProduct7111Tool:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()
        request.cls.page = Product7111ToolPage(driver)
        request.cls.page.click_7111_tools()

    # Overview
    def test_verify_navigate_to_7111_page(self):
        """
        Step by step:
            1. Hover Products menu
            2. Click 7111 menu item
            3. Verify page title is '7111: Smart Diagnostic System Tablet'
        Expected: Page title matches
        """
        self.logger.info("===== Verify Navigate to 7111 Product Page =====")
        page = Product7111ToolPage(self.driver)
        try:
            # page.click_7111_tools()
            # self.logger.info("Clicked 7111 from Products menu")
            title = page.get_title_7111_text()
            assert title == "INNOVA 7111", f"Expected 'INNOVA 7111', got '{title}'"
            self.logger.passed("Navigated to 7111 page successfully — title matches")
        except Exception as e:
            self.logger.failed(f"Failed to navigate to 7111 page: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_7111_page.png")
            assert False


    def test_verify_thumbnails_show_different_images(self):
        """
        Step by step:
            1. Navigate to 7111 page
            2. Click each of the thumbnails sequentially
            3. After each click, record the actual image SRC of the active slide
            4. Verify all recorded SRCs are unique
        """
        self.logger.info("===== Verify Each Thumbnail Changes Active Image =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            count = page.get_thumbnail_count()
            active_images = []
            for i in range(count):
                page.click_thumbnail_by_index(i)
                img_src = page.get_image_src()
                self.logger.info(f"Thumbnail {i + 1} clicked -> Active Image SRC: {img_src}")
                active_images.append(img_src)
            unique_images_count = len(set(active_images))
            assert count == 4 and unique_images_count == count, (
                f"Expected {count} unique images, got {unique_images_count}. "
                f"Image sources recorded: {active_images}")
            self.logger.passed(f"All {count} thumbnails show different images successfully!")
        except Exception as e:
            self.logger.failed(f"Thumbnail slide change verification failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_thumbnails_show_different_images.png")
            assert False


    def test_verify_zoom_multi_clicks(self):
        """
        Step by Step:
            1. Click Zoom In (+) consecutively 3 times.
            2. After each click, verify the image width increases.
            3. Click Zoom Out (-) consecutively 3 times.
            4. After 3 Zoom Outs, verify the Zoom Out button returns to the Disabled state.
        """
        self.logger.info("===== Verify Zoom In/Out - 3 Clicks Sequence =====")
        page = Product7111ToolPage(self.driver)

        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            page.scroll_to_zoom_in_and_out()
            self.logger.info("Scroll to zoom in and out")
            initial_status = page.get_zoom_out_disabled_status()
            self.logger.info(f"Initial Zoom Out 'aria-disabled': {initial_status}")
            assert initial_status == "true"

            for i in range(3):
                page.click_zoom_in_button()
                status_after_zoom_in = page.get_zoom_out_disabled_status()
                self.logger.info(f"Zoom In click {i + 1} -> Zoom Out 'aria-disabled': {status_after_zoom_in}")
                assert status_after_zoom_in == "false"
            self.logger.passed("Successfully completed 3 consecutive Zoom In clicks.")

            for i in range(3):
                page.click_zoom_out_button()
                status_after_zoom_out = page.get_zoom_out_disabled_status()
                self.logger.info(f"Zoom Out click {i + 1} -> Zoom Out 'aria-disabled': {status_after_zoom_out}")
                if i < 2:
                    assert status_after_zoom_out == "false", f"Error Zoom Out {i + 1}"
                else:
                    assert status_after_zoom_out == "true", "Error Zoom Out 3"

            self.logger.passed("Successfully verified Zoom Out returns to origin state.")

        except Exception as e:
            self.logger.failed(f"Zoom sequence failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_zoom_multi_clicks.png")
            assert False


    def test_verify_carousel_navigation_arrows(self):
        """
        Step by step:
            1. Navigate to 7111 page
            2. Get the initial active image SRC
            3. Click 'Next' button and verify the image SRC changes
            4. Click 'Prev' button and verify the image SRC returns to the initial one
        """
        self.logger.info("===== Verify Carousel Next/Prev Arrows =====")
        page = Product7111ToolPage(self.driver)

        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            initial_img_src = page.get_image_src()
            self.logger.info(f"Initial Image SRC: {initial_img_src}")
            page.click_carousel_next()
            self.logger.info(f"Click next button")
            next_img_src = page.get_image_src()
            self.logger.info(f"After clicking NEXT -> Image SRC: {next_img_src}")
            assert initial_img_src != next_img_src, (
                f"Expected image to change after clicking Next. "
                f"Both SRCs are: {initial_img_src}")
            self.logger.passed("Verified Next button changes the active image.")
            page.click_carousel_prev()
            self.logger.info(f"Click previous button")
            prev_img_src = page.get_image_src()
            self.logger.info(f"After clicking PREV -> Image SRC: {prev_img_src}")
            assert next_img_src != prev_img_src, "Image did not change after clicking Prev."
            assert initial_img_src == prev_img_src, (f"Expected to return to initial image. "
                f"Expected: {initial_img_src}, Got: {prev_img_src}")
            self.logger.passed("Verified Prev button returns to the previous image successfully.")

        except Exception as e:
            self.logger.failed(f"Carousel navigation verification failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_carousel_navigation_arrows.png")
            assert False


    @pytest.mark.parametrize("test_data", [JsonReader("product_7111_tool.json").get_data("product_7111")])
    def test_verify_name_features_are_correctly(self,test_data):
        """
        Step by step:
             1. Navigate to 7111 tool page
             2. Scroll to Read more
             3. Verify that display features name
             4. Click Read less
        """
        self.logger.info("===== Verify that name features are correctly =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            page.click_read_more()
            self.logger.info("Scrolled to 'Read more' and clicked button")
            actual_features = page.get_all_features_text()
            expected_features = test_data["features"]
            assert actual_features == expected_features
            self.logger.passed("Verified all feature names match the JSON data perfectly.")
        except Exception as e:
            self.logger.failed(f"Carousel navigation verification failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_name_features_are_correctly.png")
            assert False


    def test_verify_click_secure_gateway_fca_navigate_to_article(self):
        """
        Step by Step:
            1. Navigate to 7111 tool page
            2. Scroll to Read more
            3. Click Read more button
            4. Click Secure Gateway Unlock (FCA, Nissan)
            5. Verify that navigate to Innova 7111 How to unlock secure gateway
        """
        self.logger.info("===== Verify that navigate to Innova 7111 How to un-clock secure gateway =====")
        page = Product7111ToolPage(self.driver)

        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            page.click_read_more()
            self.logger.info("Scroll to Read more and click button")
            page.scroll_to_sgw_fca()
            self.logger.info("Scroll to Security Gateway Un-clock (FCA, Nissan)")
            page.click_sgw_fca_nissan()
            self.logger.info("Click the link")
            assert page.get_text_op() == "Innova 7111: How to unlock Secure Gateway (SGW)"
        except Exception as e:
            self.logger.failed(f"Zoom sequence failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_click_secure_gateway_fca_navigate_to_article.png")
            assert False

    def test_verify_complete_specs_and_feature_list_navigate_to_compare_diagnostic_product(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Scroll and click Read more button
             3. Click Complete Specs and Feature List
             4. Verify that navigate to COMPARE DIAGNOSTIC PRODUCT
        """
        self.logger.info("===== Verify that navigate to COMPARE DIAGNOSTIC PRODUCT =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            page.click_read_more()
            self.logger.info("Scroll to Read more and click button")
            page.click_complete_specs_feature_list()
            self.logger.info("Click Complete Specs and Feature List")
            assert page.get_compare_diagnostic_product_title() == "COMPARE DIAGNOSTIC PRODUCTS"
        except Exception as e:
            self.logger.failed(f"Zoom sequence failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_complete_specs_and_feature_list_navigate_to_compare_diagnostic_product.png")
            assert False


    def test_verify_find_store_navigate_to_napa_auto_parts_retailer(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Click Find a Store button
             3. Click NAPA Auto Parts icon
             4. Verify that navigate to NAPA Auto Parts retailer
        """
        self.logger.info("===== Verify that clicking Find a Store for NAPA Auto Parts navigates to the correct retailer website =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            page.click_find_a_store_7111()
            self.logger.info("Scroll and click Find a Store button")
            page.navigate_new_tab_with_url(page.click_napa_auto_parts_link, "napaonline.com")
            page.click_close_button()
        except Exception as e:
            self.logger.failed(f"Zoom sequence failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_find_store_navigate_to_napa_auto_parts_retailer.png")
            assert False


    def test_verify_find_store_navigate_to_o_reilly_auto_parts_retailer(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Click Find a Store button
             3. Click O'Reilly Auto Parts icon
             4. Verify that navigate to O'Reilly Auto Parts retailer
        """
        self.logger.info("===== Verify that clicking Find a Store for O'Reilly Auto Parts navigates to the correct retailer website. =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            page.click_find_a_store_7111()
            self.logger.info("Scroll and click Find a Store button")
            page.navigate_new_tab_with_url(page.click_o_reilly_auto_parts_link, "oreillyauto.com")
            page.click_close_button()
        except Exception as e:
            self.logger.failed(f"Zoom sequence failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_find_store_navigate_to_o_reilly_auto_parts_retailer.png")
            assert False


    def test_verify_find_store_navigate_to_auto_zone_retailer(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Click Find a Store button
             3. Click Auto Zone icon
             4. Verify that navigate to Auto Zone retailer
        """
        self.logger.info("===== Verify that clicking Find a Store for Auto Zone navigates to the correct retailer website =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            page.click_find_a_store_7111()
            self.logger.info("Scroll and click Find a Store button")
            page.navigate_new_tab_with_url(page.click_auto_zone_link, "autozone.com")
            page.click_close_button()
        except Exception as e:
            self.logger.failed(f"Zoom sequence failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_find_store_navigate_to_auto_zone_retailer.png")
            assert False


    def test_verify_find_store_navigate_to_canadian_tire_retailer(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Click Find a Store button
             3. Click Canadian Tire icon
             4. Verify that navigate to Canadian Tire retailer
        """
        self.logger.info("===== Verify that clicking Find a Store for Canadian Tire navigates to the correct retailer website  =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            page.click_find_a_store_7111()
            self.logger.info("Scroll and click Find a Store button")
            page.navigate_new_tab_with_url(page.click_canadian_tire_link, "canadiantire.ca")
            page.click_close_button()
        except Exception as e:
            self.logger.failed(f"Zoom sequence failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_find_store_navigate_to_canadian_tire_retailer.png")
            assert False


    def test_verify_download_product_manual_navigate_to_pdf_tab(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Scroll to Download Product Manual
             3. Click the link
             4. Navigate to pdf tab
        """
        self.logger.info("===== Verify that download product manual navigate to pdf tab  =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            # page.click_find_a_store_7111()
            self.logger.info("Scroll and click Download Product Manual button")
            page.navigate_new_tab_with_url(page.click_download_product_manual, "rs-pro.s3.amazonaws.com")
        except Exception as e:
            self.logger.failed(f"Zoom sequence failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_download_product_manual_navigate_to_pdf_tab.png")
            assert False


    def test_verify_click_learn_more_to_navigate_diagnostic_tool_page(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Scroll to learn more and click button
             3. Verify that navigate to diagnostic tool page
        """
        self.logger.info("===== Verify Video Bar Contains Videos =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigate to 7111 page")
            page.click_learn_more()
            self.logger.info("Scroll to learn more and click the button")
            assert page.get_diagnostic_tool_title() == "DIAGNOSTICS TOOLS"
            self.logger.passed("Verify that navigate to diagnostic tool page")
        except Exception as e:
            self.logger.failed("Not navigate diagnostic tool page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_click_learn_more_to_navigate_diagnostic_tool_page.png")
            assert False

    # Videos
    def test_verify_scroll_to_get_more_information_and_view_all_videos(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Click 'Videos' tab
             3. Scroll to get more information
             4. Verify get title
             5. Click View all videos button
             6. Verify navigate to Youtube
        """
        self.logger.info("===== Verify that scroll to get more information and view all video links =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigated to 7111 page")
            page.click_videos_tab()
            self.logger.info("Click video bar")
            assert page.get_title_video() == "Get More Information From Our Videos"
            self.logger.passed("Scroll to Get more information")
            page.navigate_new_tab(page.click_view_all_videos, "innovadiagnosticsolutions",
                                  page.get_diagnostic_text, "Innova Diagnostic Solutions")
        except Exception as e:
            self.logger.failed(f"Video playback verification failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_get_more_information_and_view_all_videos.png")
            assert False


    def test_verify_default_video_play_and_pause(self):
        """
        Step by step:
            1. Navigate to 7111 page
            2. Click 'Videos' tab
            4. Switch to iframe, click play video
            5. Wait 5s, verify video is actually playing (currentTime > 3)
            6. Pause video via JS and verify it is paused
            7. Switch back to main content
        """
        self.logger.info("===== Verify Videos Tab: Play and Pause Video =====")
        page = Product7111ToolPage(self.driver)

        try:
            page.click_7111_tools()
            self.logger.info("Navigate to 7111 page")
            page.click_videos_tab()
            self.logger.info("Click video bar")
            assert page.get_title_video() == "Get More Information From Our Videos"
            page.play_main_youtube_video()
            self.logger.info("Playing the main YouTube video...")
            time.sleep(5)

            current_time = page.get_video_current_time()
            self.logger.info(f"Video current time: {current_time} seconds")
            assert current_time > 3, f"Error : Video not run, the time at the present {current_time}s"
            self.logger.passed("Verified video is playing successfully.")

            page.pause_youtube_video_via_js()
            self.logger.info("Pausing the video...")
            assert page.is_video_paused() is True
            self.logger.passed("Verified video paused successfully.")

        except Exception as e:
            self.logger.failed(f"Video playback verification failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_default_video_play_and_pause.png")
            assert False

        finally:
            page.switch_to_default_content()


    def test_verify_video_bar_count(self):
        """
        Step by step:
            1. Navigate to 7111 page
            2. Click 'Videos' tab
            3. Count video items in the right scrollable bar
            4. Verify at least 1 video is present
        Expected: Right bar contains > 0 video items
        """
        self.logger.info("===== Verify Video Bar Contains Videos =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigate to 7111 page")
            page.click_videos_tab()
            self.logger.info("Click videos tab")
            count = page.get_video_bar_count()
            self.logger.info(f"Video bar contains {count} videos")
            assert count > 0, "No videos found in the right video bar"
            self.logger.passed(f"Video bar contains {count} videos — verified")
        except Exception as e:
            self.logger.failed(f"Video bar count verification failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_video_bar_count.png")
            assert False


    def test_verify_video_bar_interactions(self):
        """
        Step by step:
            1. Navigate to 7111 page
            2. Click 'Videos' tab
            3. Randomly select 3 videos from the right scrollable bar
            4. For each selected video:
               a. Click video item from the right bar
               b. Verify the main iframe src changed (new video loaded into player)
               c. Click play on the main player
               d. Wait 3 seconds (video plays)
               e. Pause the video
        Expected:
            - After clicking each bar video, the main iframe src must change
            - Play and pause complete without errors for each video
        """
        self.logger.info("===== Verify Video Bar Interactions (3 Random Videos) =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigate to 7111 page")
            page.click_videos_tab()
            self.logger.info("Click videos tab")
            results = page.verify_video_bar_interactions(count=3)
            self.logger.info(f"Tested {len(results)} random videos from bar")

            failed = [r for r in results if not r["passed"]]
            if failed:
                for r in failed:
                    self.logger.info(f"Video #{r['video_index']} — src_changed: {r['src_changed']}")
                assert False, (f"{len(failed)} video(s) did not change the main player after clicking: "
                    f"{[r['video_index'] for r in failed]}")

            self.logger.passed(f"All {len(results)} random bar videos loaded into the main player and played correctly")
        except Exception as e:
            self.logger.failed(f"Video bar interaction test failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_video_bar_interactions.png")
            assert False


    def test_verify_navigate_to_compare_diagnostic_product_page(self):
        """
        Step by step:
            1. Navigate to 7111 page
            2. Click Feature & Specification bar
            3. Verify that navigate to compare diagnostic product page
        """
        self.logger.info("===== Verify that navigate to compare diagnostic product page =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigate to 7111 page")
            page.click_feature_spec()
            self.logger.info("Click feature and specification tab")
            assert page.get_compare_diagnostic_product_title() == "COMPARE DIAGNOSTIC PRODUCTS"
            self.logger.passed("Verify that navigate to compare diagnostic product page")
        except Exception as e:
            self.logger.failed("Not navigate to compare diagnostic product page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_compare_diagnostic_product_page.png")
            assert False


    def test_verify_navigate_to_diagnostic_tool_page(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Scroll to View Product Other
             3. Click to View All Products button
             4. Verify that navigate to diagnostic tool page
        """
        self.logger.info("===== Verify that View All Products navigate to diagnostic tool page =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigate to 7111 page")
            page.scroll_to_view_all_product()
            self.logger.info("Scroll to view all product")
            page.click_view_all_products()
            self.logger.info("Click view all products")
            assert page.get_diagnostic_tool_title() == "DIAGNOSTICS TOOLS"
            self.logger.passed("Verify that navigate to diagnostic tool page")
        except Exception as e:
            self.logger.failed("Not navigate to diagnostic tool page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_diagnostic_tool_page.png")
            assert False


    def test_verify_navigate_to_sds50_diagnostic_tool_page(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Scroll to Products
             3. Click SDS50 diagnostic tool
             4. Verify that navigate to SDS50 diagnostic tool page
        """
        self.logger.info("===== Verify that navigate to SDS50 diagnostic tool page =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigate to 7111 page")
            page.scroll_to_products()
            self.logger.info("Scroll to products")
            page.click_sds50_tool()
            self.logger.info("Click SDS50 tool")
            assert page.get_sds50_title() == "INNOVA SDS50"
            self.logger.passed("Verify that navigate to SDS50 diagnostic tool page")
        except Exception as e:
            self.logger.failed("Not navigate to SDS50 diagnostic tool page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_sds50_diagnostic_tool_page.png")
            assert False


    def test_verify_navigate_to_sds43_diagnostic_tool_page(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Scroll to Products
             3. Click SDS43 diagnostic tool
             4. Verify that navigate to SDS43 diagnostic tool page
        """
        self.logger.info("===== Verify that navigate to SDS43 diagnostic tool page =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigate to 7111 page")
            page.scroll_to_products()
            self.logger.info("Scroll to products")
            page.click_sds43_tool()
            self.logger.info("Click SDS43 tool")
            assert page.get_sds43_title() == "INNOVA SDS43"
            self.logger.passed("Verify that navigate to SDS43 diagnostic tool page")
        except Exception as e:
            self.logger.failed("Not navigate to SDS43 diagnostic tool page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_sds43_diagnostic_tool_page.png")
            assert False


    def test_verify_navigate_to_apple_store(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Scroll to app download section
             3. Click Apple icon
             4. Verify that navigate to AppleStore
        """
        self.logger.info("===== Verify that navigate to Apple store =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigate to 7111 page")
            page.scroll_to_store()
            self.logger.info("Scroll to store download app")
            page.navigate_new_tab_with_url(page.click_apple_link, "apps.apple.com")
            self.logger.passed("Verify that navigate to apple store")
        except Exception as e:
            self.logger.failed("Not navigate diagnostic tool page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_apple_store.png")
            assert False


    def test_verify_navigate_to_google_play_store(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Scroll to app download section
             3. Click Google Play icon
             4. Verify that navigate to Google play store
        """
        self.logger.info("===== Verify that navigate to Google play store =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigate to 7111 page")
            page.scroll_to_store()
            self.logger.info("Scroll to store download app")
            page.navigate_new_tab_with_url(page.click_google_link, "play.google.com")
            self.logger.passed("Verify that navigate to Google play store")
        except Exception as e:
            self.logger.failed("Not navigate diagnostic tool page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_google_play_store.png")
            assert False


    def test_verify_scroll_to_support(self):
        """
        Step by step:
             1. Navigate to 7111 page
             2. Click support tab
             4. Verify that scroll to support articles
        """
        self.logger.info("===== Verify Video Bar Contains Videos =====")
        page = Product7111ToolPage(self.driver)
        try:
            page.click_7111_tools()
            self.logger.info("Navigate to 7111 page")
            page.click_support_tab()
            self.logger.info("Click support tab")
            assert page.get_support_title().is_displayed()
            self.logger.passed("Verify that scroll to support articles")
        except Exception as e:
            self.logger.failed("Not scroll to support articles", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_scroll_to_support.png")
            assert False