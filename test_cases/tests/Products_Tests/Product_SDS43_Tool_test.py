import time
import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.Products_Pages.Product_SDS43_Tool_Pages import ProductSDS43ToolPage
from utilities.custom_logger import LogMaker
from utilities.json_reader import JsonReader

@pytest.mark.ProductSDS43
class TestProductSDS43Tool:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()
        request.cls.page = ProductSDS43ToolPage(driver)

    # Overview
    def test_verify_navigate_to_sds43_page(self):
        """
        Step by step:
            1. Hover Products menu
            2. Click SDS43 menu item
            3. Verify page title is 'INNOVA SDS43'
        Expected: Page title matches
        """
        self.logger.info("===== Verify Navigate to SDS43 Product Page =====")
        try:
            self.page.click_sds43_tool()
            title = self.page.get_title_sds43_text()
            assert title == "INNOVA SDS43", f"Expected 'INNOVA SDS43', got '{title}'"
            self.logger.passed("Navigated to SDS43 page successfully — title matches")
        except Exception as e:
            self.logger.failed(f"Failed to navigate to SDS43 page: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_sds43_page.png")
            assert False

    def test_verify_thumbnails_show_different_images(self):
        """
        Step by step:
            1. Navigate to SDS43 page
            2. Click each of the thumbnails sequentially
            3. After each click, record the actual image SRC of the active slide
            4. Verify all recorded SRCs are unique
        """
        self.logger.info("===== Verify Each Thumbnail Changes Active Image =====")
        try:
            self.page.click_sds43_tool()
            count = self.page.get_thumbnail_count_sds43()
            active_images = []
            for i in range(count):
                self.page.click_thumbnail_by_index_sds43(i)
                img_src = self.page.get_image_src_sds43()
                self.logger.info(f"Thumbnail {i + 1} clicked -> Active Image SRC: {img_src}")
                active_images.append(img_src)
            unique_images_count = len(set(active_images))
            assert count == 8 and unique_images_count == count, (
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
        try:
            self.page.click_sds43_tool()
            self.page.scroll_to_zoom_in_and_out_sds43()
            self.logger.info("Scroll to zoom in and out")
            initial_status = self.page.get_zoom_out_disabled_status_sds43()
            self.logger.info(f"Initial Zoom Out 'aria-disabled': {initial_status}")
            assert initial_status == "true"

            for i in range(3):
                self.page.click_zoom_in_sds43_button()
                status_after_zoom_in = self.page.get_zoom_out_disabled_status_sds43()
                self.logger.info(f"Zoom In click {i + 1} -> Zoom Out 'aria-disabled': {status_after_zoom_in}")
                assert status_after_zoom_in == "false"
            self.logger.passed("Successfully completed 3 consecutive Zoom In clicks.")

            for i in range(3):
                self.page.click_zoom_out_sds43_button()
                status_after_zoom_out = self.page.get_zoom_out_disabled_status_sds43()
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
            1. Navigate to SDS43 page
            2. Get the initial active image SRC
            3. Click 'Next' button and verify the image SRC changes
            4. Click 'Prev' button and verify the image SRC returns to the initial one
        """
        self.logger.info("===== Verify Carousel Next/Prev Arrows =====")
        try:
            self.page.click_sds43_tool()
            initial_img_src = self.page.get_image_src_sds43()
            self.logger.info(f"Initial Image SRC: {initial_img_src}")
            self.page.click_carousel_next_sds43()
            self.logger.info(f"Click next button")
            next_img_src = self.page.get_image_src_sds43()
            self.logger.info(f"After clicking NEXT -> Image SRC: {next_img_src}")
            assert initial_img_src != next_img_src, (
                f"Expected image to change after clicking Next. "
                f"Both SRCs are: {initial_img_src}")
            self.logger.passed("Verified Next button changes the active image.")
            self.page.click_carousel_prev_sds43()
            self.logger.info(f"Click previous button")
            prev_img_src = self.page.get_image_src_sds43()
            self.logger.info(f"After clicking PREV -> Image SRC: {prev_img_src}")
            assert next_img_src != prev_img_src, "Image did not change after clicking Prev."
            assert initial_img_src == prev_img_src, (f"Expected to return to initial image. "
                                                     f"Expected: {initial_img_src}, Got: {prev_img_src}")
            self.logger.passed("Verified Prev button returns to the previous image successfully.")

        except Exception as e:
            self.logger.failed(f"Carousel navigation verification failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_carousel_navigation_arrows.png")
            assert False

    @pytest.mark.parametrize("sds43_tool", [JsonReader("product_sds43_tool.json").get_data("product_sds43")])
    def test_verify_name_features_are_correctly(self, sds43_tool):
        """
        Step by step:
             1. Navigate to SDS43 tool page
             2. Scroll to Read more
             3. Verify that display features name
             4. Click Read less
        """
        self.logger.info("===== Verify that name features are correctly =====")
        try:
            self.page.click_sds43_tool()
            self.page.click_read_more_sds43_button()
            self.logger.info("Scrolled to Read more and clicked button")
            assert self.page.get_all_features_sds43_text() == sds43_tool["features"]
            time.sleep(1.5)
            self.page.click_read_more_sds43_button()
            self.logger.passed("Verified all feature names match the JSON data perfectly.")
        except Exception as e:
            self.logger.failed(f"Missing or incorrect feature name : {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_name_features_are_correctly.png")
            assert False

    def test_verify_click_secure_gateway_fca_navigate_to_article(self):
        """
        Step by Step:
            1. Navigate to SDS43 tool page
            2. Scroll to Read more
            3. Click Read more button
            4. Click Secure Gateway Unlock (FCA)
            5. Verify that navigate to Innova SDS43 - How to Unlock the Secure Gateway (SGW)
        """
        self.logger.info("===== Verify that Secure Gateway Unlock (FCA) to Innova SDS43 - How to Unlock the Secure Gateway (SGW) =====")
        try:
            self.page.click_sds43_tool()
            self.page.click_read_more_sds43_button()
            self.logger.info("Scrolled to Read more and clicked button")
            self.page.click_secure_gate_fca()
            self.logger.info("Click Security Gateway Un-clock (FCA)")
            assert self.page.get_title_text_secure_gateway_fca() == "Innova SDS43 - How to unlock the Secure Gateway (SGW)"
            self.logger.passed("Navigate to Innova SDS43 Unlock Secure Gateway (SGW) page")
        except Exception as e:
            self.logger.failed(f"Not navigate to the article: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_click_secure_gateway_fca_navigate_to_article.png")
            assert False

    def test_verify_complete_specs_and_feature_list_navigate_to_compare_diagnostic_product(self):
        """
        Step by Step:
            1. Navigate to SDS43 tool page
            2. Scroll to Read more
            3. Click Read more button
            4. Click Complete Specs and Feature List button
            5. Verify that navigate to COMPARE DIAGNOSTIC PRODUCTS
        """
        self.logger.info("===== Verify that Complete Specs and Feature List navigate to COMPARE DIAGNOSTIC PRODUCTS =====")
        try:
            self.page.click_sds43_tool()
            self.page.click_read_more_sds43_button()
            self.logger.info("Scrolled to Read more and clicked button")
            self.page.click_complete_specs_feature_list_sds43()
            self.logger.info("Click Complete Specs and Feature List button")
            assert self.page.get_compare_diagnostic_product_title() == "COMPARE DIAGNOSTIC PRODUCTS"
            self.logger.passed("Navigate to COMPARE DIAGNOSTIC PRODUCTS")
        except Exception as e:
            self.logger.failed(f"Not navigate to compare diagnostic products: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_complete_specs_and_feature_list_navigate_to_compare_diagnostic_product.png")
            assert False

    def test_verify_navigate_to_napa_auto_parts_retailer(self):
        """
        Step by step:
             1. Navigate to SDS43 page
             2. Click Find a Store button
             3. Click NAPA Auto Parts icon
             4. Verify that navigate to NAPA Auto Parts retailer
        """
        self.logger.info("===== Verify that Find a Store navigate to NAPA Auto Parts retailer =====")
        try:
            self.page.click_sds43_tool()
            self.page.scroll_to_and_click_find_a_store_button()
            self.logger.info("Scrolled and click Find a Store button")
            self.page.navigate_new_tab_with_url(self.page.click_napa_auto_parts, "napaonline.com")
            self.page.click_close_button()
        except Exception as e:
            self.logger.failed(f"Not navigate to new tab: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_napa_auto_parts_retailer.png")
            assert False

    def test_verify_navigate_to_o_reilly_auto_parts_retailer(self):
        """
        Step by step:
             1. Navigate to SDS43 page
             2. Click Find a Store button
             3. Click O'Reilly Auto Parts icon
             4. Verify that navigate to O'Reilly Auto Parts retailer
        """
        self.logger.info("===== Verify that Find a Store navigate to O'Reilly Auto Parts retailer =====")
        try:
            self.page.click_sds43_tool()
            self.page.scroll_to_and_click_find_a_store_button()
            self.logger.info("Scrolled and click Find a Store button")
            self.page.navigate_new_tab_with_url(self.page.click_o_reilly_auto_parts, "oreillyauto.com")
            self.page.click_close_button()
        except Exception as e:
            self.logger.failed(f"Not navigate to new tab: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_o_reilly_auto_parts_retailer.png")
            assert False

    def test_verify_navigate_to_auto_zone_retailer(self):
        """
        Step by step:
             1. Navigate to SDS43 page
             2. Click Find a Store button
             3. Click Auto Zone icon
             4. Verify that navigate to Auto Zone retailer
        """
        self.logger.info("===== Verify that Find a Store navigate to Auto Zone retailer =====")
        try:
            self.page.click_sds43_tool()
            self.page.scroll_to_and_click_find_a_store_button()
            self.logger.info("Scrolled and click Find a Store button")
            self.page.navigate_new_tab_with_url(self.page.click_auto_zone, "autozone.com")
            self.page.click_close_button()
        except Exception as e:
            self.logger.failed(f"Not navigate to new tab: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_auto_zone_retailer.png")
            assert False

    def test_verify_download_manual_product_navigate_to_new_tab(self):
        """
        Step by step:
             1. Navigate to SDS43 page
             2. Click Scroll and click Download Manual Product
             4. Verify that navigate to new tab
        """
        self.logger.info("===== Verify that Download Manual Product navigate to Download Manual Product =====")
        try:
            self.page.click_sds43_tool()
            self.logger.info("Scrolled and click Download Manual Product")
            self.page.navigate_new_tab_with_url(self.page.click_download_manual_product, "rs-pro.s3.amazonaws.com")
        except Exception as e:
            self.logger.failed(f"Not navigate to new tab: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_download_manual_product_navigate_to_new_tab.png")
            assert False

    def test_verify_learn_more_navigate_to_diagnostic_tool_page(self):
        """
        Step by step:
             1. Navigate to SDS43 page
             2. Scroll to SDS43 banner
             3. Click Learn more button
             4. Verify that navigate to Diagnostic Tool page
        """
        self.logger.info("===== Verify that learn more navigate to Diagnostic Tool page =====")
        try:
            self.page.click_sds43_tool()
            self.page.click_learn_more_button()
            self.logger.info("Scrolled and click Learn more button")
            assert self.page.get_compare_diagnostic_product_title() == "COMPARE DIAGNOSTIC PRODUCTS"
        except Exception as e:
            self.logger.failed(f"Not navigate to COMPARE DIAGNOSTIC PRODUCTS: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_learn_more_navigate_to_diagnostic_tool_page.png")
            assert False

    def test_verify_learn_more_build_for_pros_navigate_to_compare_diagnostic_products(self):
        """
        Step by step:
             1. Navigate to SDS43 page
             2. Scroll to Build for Pros
             3. Click Learn more button
             4. Verify that navigate to COMPARE DIAGNOSTIC PRODUCTS
        """
        self.logger.info("===== Verify that Build for Pros navigate to Compare Diagnostic Product =====")
        try:
            self.page.click_sds43_tool()
            self.page.click_learn_more_build_for_pros()
            self.logger.info("Scroll and click Learn more button of Build for Pros")
            assert self.page.get_compare_diagnostic_product_title() == "COMPARE DIAGNOSTIC PRODUCTS"
        except Exception as e:
            self.logger.failed(f"Not navigate to Compare Diagnostic Products: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_learn_more_build_for_pros_navigate_to_compare_diagnostic_products.png")
            assert False

    def test_verify_default_video_play_and_pause(self):
        """
        Step by step:
            1. Navigate to SDS43 page
            2. Click 'Videos' tab
            4. Switch to iframe, click play video
            5. Wait 5s, verify video is actually playing (currentTime > 3)
            6. Pause video via JS and verify it is paused
            7. Switch back to main content
        """
        self.logger.info("===== Verify Videos Tab: Play and Pause Video =====")
        try:
            self.page.click_sds43_tool()
            self.page.scroll_to_video_sds43()
            self.logger.info("Scroll to video")
            self.page.play_main_youtube_video_sds43()
            time.sleep(5)
            current_time = self.page.get_video_current_time_sds43()
            self.logger.info(f"Video current time: {current_time} seconds")
            assert current_time > 3, f"Error : Video not run, the time at the present {current_time}s"
            self.logger.passed("Verified video is playing successfully.")

            self.page.pause_youtube_video_sds43()
            self.logger.info("Pausing the video...")
            assert self.page.is_video_paused_sds43() is True

        except Exception as e:
            self.logger.failed(f"Video playback verification failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_default_video_play_and_pause.png")
            assert False
        finally:
            self.page.switch_to_default_content_sds43()

    def test_verify_navigate_to_apple_store(self):
        """
        Step by step:
             1. Navigate to SDS43 page
             2. Scroll to app download section
             3. Click Apple icon
             4. Verify that navigate to AppleStore
        """
        self.logger.info("===== Verify that navigate to Apple store =====")
        try:
            self.page.click_sds43_tool()
            self.logger.info("Navigate to SDS43 page")
            self.page.scroll_to_store_sds43()
            self.logger.info("Scroll to store download app")
            self.page.navigate_new_tab_with_url(self.page.click_apple_link_sds43, "apps.apple.com")
            self.logger.passed("Navigate to apple store")
        except Exception as e:
            self.logger.failed("Not navigate diagnostic tool page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_apple_store.png")
            assert False

    def test_verify_navigate_to_google_play_store(self):
        """
        Step by step:
             1. Navigate to SDS43 page
             2. Scroll to app download section
             3. Click Google Play icon
             4. Verify that navigate to Google play store
        """
        self.logger.info("===== Verify that navigate to Google play store =====")
        try:
            self.page.click_sds43_tool()
            self.logger.info("Navigate to SDS43 page")
            self.page.scroll_to_store_sds43()
            self.logger.info("Scroll to store download app")
            self.page.navigate_new_tab_with_url(self.page.click_google_link_sds43, "play.google.com")
            self.logger.passed("Navigate to Google play store")
        except Exception as e:
            self.logger.failed("Not navigate diagnostic tool page", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_navigate_to_google_play_store.png")
            assert False