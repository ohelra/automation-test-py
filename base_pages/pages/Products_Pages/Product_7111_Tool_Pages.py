import random
import time
from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage

class Product7111ToolPage(RSPROHomePage):

    # ── Overview ───────────────────────────────────────────────────────────
    product =                          (By.ID, "navbarDropdown")
    feature_list_items =               (By.CSS_SELECTOR, "ul.web-inspector-list > li")
    title_7111 =                       (By.XPATH, "//span[normalize-space()='Innova 7111']")
    page_7111 =                        (By.XPATH, "(//a[contains(text(),'7111')])[1]")
    compare_diagnostic_product =       (By.XPATH, "//span[normalize-space()='COMPARE DIAGNOSTIC PRODUCTS']")
    diagnostic_tool_title =            (By.XPATH, "//span[normalize-space()='Diagnostics Tools']")
    support =                          (By.XPATH, "//a[normalize-space()='Innova 7111: Smart Diagnostics System']")
    complete_specs_feature_list =      (By.XPATH, "//a[normalize-space()='Complete Specs and Feature List']")
    find_a_store =                     (By.XPATH, "(//a[@class='web-collapse-02 cl-02'])[1]")
    close_button =                     (By.XPATH, "(//button[@aria-label='Close'])[1]")
    napa_auto_parts =                  (By.XPATH, "(//a[@id='7111FindinstoreNP'])[1]")
    o_reilly_auto_parts =              (By.XPATH, "(//a[@id='7111FindinstoreOR'])[1]")
    auto_zone =                        (By.XPATH, "(//a[@id='7111FindinstoreAZ'])[1]")
    canadian_tire =                    (By.XPATH, "(//a[@id='7111FindinstoreCT'])[1]")
    download_manual_product =          (By.XPATH, "(//a[normalize-space()='Download Product Manual'])[1]")
    title_sgw =                        (By.ID, "_articleTitle")

    # ── Tabs ─────────────────────────────────────────────────────────────────
    overview =              (By.XPATH, "//a[@class='web-product-tabs-lnk'][normalize-space()='Overview']")
    videos_tab =            (By.XPATH, "//a[normalize-space()='Videos']")
    features_spec =         (By.XPATH, "//a[normalize-space()='Features & Specifications']")
    support_tab =           (By.XPATH, "//a[@class='web-product-tabs-lnk'][normalize-space()='Support']")

    # ── Thumbnail Gallery (bar_scroll) ───────────────────────────────────────
    # Container div holding the 4 product thumbnails
    bar_scroll =            (By.XPATH, "//div[@class='col-12 col-lg-3 order-2 order-lg-1 overflow-hidden']")
    # Individual thumbnail images inside bar_scroll (4 total)
    thumbnail_images =      (By.XPATH, "//div[@class='col-12 col-lg-3 order-2 order-lg-1 overflow-hidden']//img")
    # Swiper slide wrappers inside the thumbnail bar (col-lg-3 left column)
    # After clicking thumbnail i, its parent swiper-slide gets class 'swiper-slide-thumb-active'
    thumbnail_slides =      (By.XPATH, "//div[@class='col-12 col-lg-3 order-2 order-lg-1 overflow-hidden']//div[contains(@class,'swiper-slide')]")

    # ── Carousel Controls ────────────────────────────────────────────────────
    left_button =           (By.XPATH, "//div[@aria-label='Previous slide']")
    right_button =          (By.XPATH, "//div[@aria-label='Next slide']")

    # ── Zoom Controls ────────────────────────────────────────────────────────
    # NOTE: these buttons may only appear on hover over the main image — verify on live page
    zoom_in_button =        (By.XPATH, "//button[@aria-label='button for zoom in zoomist']")
    zoom_out_button =       (By.XPATH, "//button[@aria-label='button for zoom out zoomist']")

    # ── Video Section ────────────────────────────────────────────────────────
    # Section header
    information_our_video = (By.XPATH, "(//h2[normalize-space()='Get More Information From Our Videos'])[1]")
    view_all_videos =       (By.XPATH, "//a[normalize-space()='View All Videos']")
    diagnostic_text =       (By.XPATH, "//span[normalize-space()='Innova Diagnostic Solutions']")
    # Main embedded YouTube iframe (left side — the large player)
    # NOTE: verify class name 'web-videos-l' on live page
    main_video_iframe =     (By.XPATH, "//iframe[contains(@src, 'youtube') and not(contains(@class, 'pe-none'))]")
    yt_large_play_btn =     (By.CSS_SELECTOR, "button.ytmCuedOverlayPlayButton, button.ytp-large-play-button")

    # Right scrollable bar — container
    bar_videos =            (By.XPATH, "//div[@class='overflow-hidden web-videos-r']")
    # Clicking one loads that video into the main_video_iframe player
    video_bar_items =       (By.XPATH, "//div[@class='overflow-hidden web-videos-r']//a")

    # ── Related Content ──────────────────────────────────────────────────────
    read_more =             (By.XPATH, "/html/body/main/section[1]/div/div/div/div[2]/div/div[3]/a")
    sds50_tool =            (By.XPATH, "(//a[@class='web-award-product'])[1]")
    sds43_tool =            (By.XPATH, "(//a[@class='web-award-product'])[2]")
    title_sds50 =           (By.XPATH, "//span[normalize-space()='Innova SDS50']")
    title_sds43 =           (By.XPATH, "//span[normalize-space()='Innova SDS43']")
    view_all_product =      (By.XPATH, "//a[normalize-space()='View All Products']")
    sgw =                   (By.XPATH, "//a[normalize-space()='Secure Gateway Unlock (FCA, Nissan)']")
    learn_more =            (By.XPATH, "//a[normalize-space()='Learn More']")
    apple_link =            (By.XPATH, "//img[@class='mr-3 mb-3']")
    google_play_link =      (By.XPATH, "//img[@class='mb-3']")

    # ─────────────────────────────────────────────────────────────────────────
    # Navigation Methods
    # ─────────────────────────────────────────────────────────────────────────

    def click_7111_tools(self):
        self.hover(self.product)
        self.wait.wait_for_element_visible(*self.page_7111).click()

    def get_title_7111_text(self):
        return self.wait.wait_for_element_visible(*self.title_7111).text

    def click_videos_tab(self):
        self.wait.wait_for_element_visible(*self.videos_tab).click()
        time.sleep(1)

    def click_feature_spec(self):
        self.wait.wait_for_element_visible(*self.features_spec).click()

    def scroll_to_view_all_product(self):
        self.scroll_to(self.view_all_product)

    def click_view_all_products(self):
        self.wait.wait_for_element_visible(*self.view_all_product).click()

    def get_diagnostic_tool_title(self):
        return self.wait.wait_for_element_visible(*self.diagnostic_tool_title).text

    def get_compare_diagnostic_product_title(self):
        return self.wait.wait_for_element_visible(*self.compare_diagnostic_product).text

    def scroll_to_products(self):
        self.scroll_to(self.sds50_tool)

    def click_sds50_tool(self):
        self.wait.wait_for_element_visible(*self.sds50_tool).click()

    def click_sds43_tool(self):
        self.wait.wait_for_element_visible(*self.sds43_tool).click()

    def get_sds50_title(self):
        return self.wait.wait_for_element_visible(*self.title_sds50).text

    def get_sds43_title(self):
        return self.wait.wait_for_element_visible(*self.title_sds43).text

    def click_learn_more(self):
        self.scroll_to(self.learn_more)
        self.wait.wait_for_element_visible(*self.learn_more).click()

    def get_all_features_text(self):
        self.wait.wait_for_element_visible(*self.feature_list_items)
        elements = self.driver.find_elements(*self.feature_list_items)
        actual_texts = [el.text.strip() for el in elements if el.text.strip() != ""]
        return actual_texts

    def click_complete_specs_feature_list(self):
        self.scroll_to(self.complete_specs_feature_list)
        self.wait.wait_for_element_visible(*self.complete_specs_feature_list).click()

    def click_find_a_store_7111(self):
        self.scroll_to(self.find_a_store)
        self.wait.wait_for_element_visible(*self.find_a_store).click()

    def click_close_button(self):
        self.wait.wait_for_element_visible(*self.close_button).click()

    def click_napa_auto_parts_link(self):
        self.wait.wait_for_element_visible(*self.napa_auto_parts).click()

    def click_o_reilly_auto_parts_link(self):
        self.wait.wait_for_element_visible(*self.o_reilly_auto_parts).click()

    def click_auto_zone_link(self):
        self.wait.wait_for_element_visible(*self.auto_zone).click()

    def click_canadian_tire_link(self):
        self.wait.wait_for_element_visible(*self.canadian_tire).click()

    def click_download_product_manual(self):
        self.scroll_to(self.download_manual_product)
        self.wait.wait_for_element_visible(*self.download_manual_product).click()

    def get_text_op(self):
        element = self.wait.wait_for_element_visible(*self.title_sgw)
        return element.text.strip()
    # ─────────────────────────────────────────────────────────────────────────
    # Thumbnail Gallery Methods
    # ─────────────────────────────────────────────────────────────────────────

    # Returns the number of thumbnail images inside bar_scroll
    def get_thumbnail_count(self):
        return len(self.driver.find_elements(*self.thumbnail_images))

    def get_image_src(self):
            return self.driver.execute_script("""
                var mainActiveSlide = document.querySelector('.carousel-list .swiper-slide-active');
                if (!mainActiveSlide) {
                    return "Error! not found image";
                }
                var img = mainActiveSlide.querySelector('img');
                if (img && img.src) {
                    return img.src; 
                }
                var allElems = mainActiveSlide.querySelectorAll('*');
                for (var i = 0; i < allElems.length; i++) {
                    var bg = window.getComputedStyle(allElems[i]).backgroundImage;
                    if (bg && bg !== 'none' && bg !== 'initial') {
                        return bg; // list format url ("...")
                    }
                }
                return "Error: Not found any image. HTML of slide: " + mainActiveSlide.innerHTML.substring(0, 150);
            """)

    def click_zoom_in_button(self):
        self.wait.wait_for_element_visible(*self.zoom_in_button).click()

    def click_zoom_out_button(self):
        self.wait.wait_for_element_visible(*self.zoom_out_button).click()

    def scroll_to_zoom_in_and_out(self):
        self.scroll_to(self.zoom_in_button)

    def get_zoom_out_disabled_status(self):
        element = self.wait.wait_for_element_present(*self.zoom_out_button)
        return element.get_attribute("aria-disabled")

    # Click index each image
    def click_thumbnail_by_index(self, index):
        slide_locator = (
            By.CSS_SELECTOR,
            f".col-12.col-lg-3.order-2.order-lg-1.overflow-hidden "
            f".swiper-slide[data-swiper-slide-index='{index}']:not(.swiper-slide-duplicate)")

        self.scroll_to(slide_locator)
        self.wait.wait_for_element_visible(*slide_locator).click()
        time.sleep(1)

    # Clicks the Next slide button
    def click_carousel_next(self):
        self.wait.wait_for_element_visible(*self.right_button).click()
        time.sleep(0.5)

    # Clicks the Previous slide button
    def click_carousel_prev(self):
        self.wait.wait_for_element_visible(*self.left_button).click()
        time.sleep(0.5)

    def click_read_more(self):
        self.specific_scroll_to(self.read_more)
        self.wait.wait_for_element_visible(*self.read_more).click()

    def scroll_to_store(self):
        self.specific_scroll_to(self.find_a_store)
        self.wait.wait_for_element_visible(*self.read_more).click()

    def scroll_to_sgw_fca(self):
        self.scroll_to(self.sgw)

    def click_sgw_fca_nissan(self):
        self.wait.wait_for_element_visible(*self.sgw).click()

    def get_title_sgw(self):
        return self.wait.wait_for_element_present(*self.title_sgw).text

    def click_support_tab(self):
        self.wait.wait_for_element_visible(*self.support_tab).click()

    def get_support_title(self):
        self.wait.wait_for_element_present(*self.support)

    def scroll_to_store(self):
        self.scroll_to(self.apple_link)

    def click_apple_link(self):
        self.wait.wait_for_element_visible(*self.apple_link).click()

    def click_google_link(self):
        self.wait.wait_for_element_visible(*self.google_play_link).click()

    # ─────────────────────────────────────────────────────────────────────────
    # Main Video Player Methods
    # ─────────────────────────────────────────────────────────────────────────
    def scroll_to_view_all(self):
        self.scroll_to(self.view_all_videos)

    def get_title_video(self):
        return self.wait.wait_for_element_visible(*self.information_our_video).text

    def click_view_all_videos(self):
        self.wait.wait_for_element_visible(*self.view_all_videos).click()

    def get_diagnostic_text(self):
        return self.wait.wait_for_element_present(*self.diagnostic_text).text

    def play_main_youtube_video(self):
        time.sleep(1.5)
        iframe_element = self.wait.wait_for_element_present(*self.main_video_iframe)
        self.driver.switch_to.frame(iframe_element)
        play_btn = self.wait.wait_for_element_present(*self.yt_large_play_btn)
        self.driver.execute_script("arguments[0].click();", play_btn)

    def get_video_current_time(self):
        try:
            return self.driver.execute_script("return document.querySelector('video').currentTime")
        except:
            return 0

    def pause_youtube_video_via_js(self):
        self.driver.execute_script("document.querySelector('video').pause()")

    def is_video_paused(self):
        return self.driver.execute_script("return document.querySelector('video').paused")

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    # Returns the current src of the main YouTube iframe
    # Used to verify that the iframe changed after selecting a bar video.
    def get_main_video_iframe_src(self):
        iframe = self.wait.wait_for_element_present(*self.main_video_iframe)
        return iframe.get_attribute("src") or ""

    # Clicks the main YouTube iframe to start playing
    # Switches into the iframe context, clicks the player area, then switches back.
    def play_main_video(self):
        iframe = self.wait.wait_for_element_visible(*self.main_video_iframe)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", iframe)
        self.driver.switch_to.frame(iframe)
        try:
            # Click the video player area (works for YouTube embeds)
            player = self.driver.find_element(By.CSS_SELECTOR, ".html5-video-player, video, .ytp-cued-thumbnail-overlay")
            player.click()
        except Exception:
            # Fallback: click the body of the iframe
            self.driver.find_element(By.TAG_NAME, "body").click()
        finally:
            self.driver.switch_to.default_content()
        time.sleep(1)

    # Pauses the main video via YouTube iframe postMessage API.
    # Requires the iframe src to include 'enablejsapi=1'.
    def pause_main_video(self):
        self.driver.execute_script("""
            var iframes = document.querySelectorAll('iframe[src*="youtube"]');
            iframes.forEach(function(iframe) {
                iframe.contentWindow.postMessage(JSON.stringify({event: 'command', func: 'pauseVideo', args: []}),'*'
                );});""")
        time.sleep(0.5)


    # ─────────────────────────────────────────────────────────────────────────
    # Right Video Bar Methods
    # ─────────────────────────────────────────────────────────────────────────

    # Returns the total number of videos in the right scrollable bar.
    def get_video_bar_count(self):
        self.scroll_to(self.bar_videos)
        return len(self.driver.find_elements(*self.video_bar_items))

    # Clicks a video from the right scrollable bar by 0-based index.
    # This loads the selected video into the main YouTube player on the left.
    def click_video_from_bar(self, index):
        bar_items = self.driver.find_elements(*self.video_bar_items)
        target = bar_items[index]
        self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",target)
        time.sleep(0.3)
        target.click()
        time.sleep(1)

    def verify_video_bar_interactions(self, count=3):
        """
            Test flow for each randomly selected video in the right bar:
                  1. Click video from bar  → main iframe src must change (new video loaded)
                  2. Click play            → video starts playing
                  3. Wait 3 seconds        → video plays
                  4. Pause                 → video paused
            Args:
                  count (int): number of random videos to test from the bar (default 3)
            Returns:
                  list of dicts: [{"video_index": int, "src_changed": bool, "passed": bool}]
                  Test script asserts all entries have passed=True.
        """
        total = self.get_video_bar_count()
        sample_indices = sorted(random.sample(range(total), min(count, total)))
        results = []

        for idx in sample_indices:
            before_src = self.get_main_video_iframe_src()

            self.logger.info(f"Selecting video #{idx + 1} from right bar")
            self.click_video_from_bar(idx)

            after_src = self.get_main_video_iframe_src()
            src_changed = before_src != after_src

            self.logger.info(f"Video #{idx + 1} | src changed: {src_changed} "
                f"| before: ...{before_src[-40:]} -> after: ...{after_src[-40:]}")
            self.logger.info(f"Video #{idx + 1} - clicking play")
            self.play_main_video()

            self.logger.info(f"Video #{idx + 1} — playing for 3 seconds...")
            time.sleep(3)

            self.logger.info(f"Video #{idx + 1} — pausing")
            self.pause_main_video()

            results.append({
                "video_index": idx + 1,
                "src_changed": src_changed,
                "passed": src_changed
            })

        return results
