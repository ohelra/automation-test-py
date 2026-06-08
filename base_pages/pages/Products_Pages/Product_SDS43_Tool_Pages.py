import time
from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage

class ProductSDS43ToolPage(RSPROHomePage):

    product =                          (By.ID, "navbarDropdown")
    title_sgw =                        (By.ID, "_articleTitle")
    napa_auto_parts =                  (By.ID, "SDS43FindinstoreNP")
    o_reilly_auto_parts =              (By.ID, "SDS43FindinstoreOR")
    auto_zone =                        (By.ID, "SDS43FindinstoreAZ")
    sds43_tool =                       (By.XPATH, "(//a[contains(text(),'SDS43')])[1]")
    title_sds43 =                      (By.XPATH, "(//span[normalize-space()='Innova SDS43'])[1]")
    overview =                         (By.XPATH, "(//a[@class='web-product-tabs-lnk'][normalize-space()='Overview'])[1]")
    left_button =                      (By.XPATH, "//div[@aria-label='Previous slide']")
    right_button =                     (By.XPATH, "//div[@aria-label='Next slide']")
    zoom_in_button =                   (By.XPATH, "//button[@aria-label='button for zoom in zoomist']")
    zoom_out_button =                  (By.XPATH, "//button[@aria-label='button for zoom out zoomist']")
    thumbnail_images =                 (By.XPATH, "//div[@class='col-12 col-lg-3 order-2 order-lg-1 overflow-hidden']//img")
    thumbnail_slides =                 (By.XPATH, "//div[@class='col-12 col-lg-3 order-2 order-lg-1 overflow-hidden']//div[contains(@class,'swiper-slide')]")
    find_a_store =                     (By.XPATH, "(//a[@class='web-collapse-02 cl-02'])[1]")
    close_button =                     (By.XPATH, "(//button[@aria-label='Close'])[1]")
    compare_diagnostic_product =       (By.XPATH, "//span[normalize-space()='COMPARE DIAGNOSTIC PRODUCTS']")
    diagnostic_tool_title =            (By.XPATH, "//span[normalize-space()='Diagnostics Tools']")
    download_manual_product =          (By.XPATH, "(//a[normalize-space()='Download Product Manual'])[1]")
    read_more =                        (By.XPATH, "/html/body/main/section[1]/div/div/div/div[2]/div/div[2]/a")
    complete_specs_feature_list =      (By.XPATH, "//a[normalize-space()='Complete Specs and Feature List']")
    secure_gate_fca =                  (By.XPATH, "(//a[normalize-space()='Secure Gateway Unlock (FCA)'])[1]")
    learn_more =                       (By.XPATH, "//a[normalize-space()='Learn More']")
    learn_more_build_pro =             (By.XPATH, "(//a[@class='fs-24 web-lnk web-lnk-08'])[1]")
    main_video_iframe =                (By.XPATH, "//iframe[contains(@src, 'youtube') and not(contains(@class, 'pe-none'))]")
    apple_link =                       (By.XPATH, "//img[@class='mr-3 mb-3']")
    google_play_link =                 (By.XPATH, "//img[@class='mb-3']")
    yt_large_play_btn =                (By.CSS_SELECTOR, "button.ytmCuedOverlayPlayButton, button.ytp-large-play-button")
    feature_list_items =               (By.CSS_SELECTOR, "ul.web-inspector-list > li")

    def click_sds43_tool(self):
        self.hover(self.product)
        self.wait.wait_for_element_visible(*self.sds43_tool).click()

    def get_title_sds43_text(self):
        return self.wait.wait_for_element_visible(*self.title_sds43).text

    def get_title_text_secure_gateway_fca(self):
        element = self.wait.wait_for_element_visible(*self.title_sgw)
        return element.text.strip()

    def get_thumbnail_count_sds43(self):
        return len(self.driver.find_elements(*self.thumbnail_images))

    def get_image_src_sds43(self):
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
                return "Error: Not found any image. HTML of slide: " + mainActiveSlide.innerHTML.substring(0, 150); """)

    def click_thumbnail_by_index_sds43(self, index):
        slide_locator = (By.CSS_SELECTOR,
            f".col-12.col-lg-3.order-2.order-lg-1.overflow-hidden "
            f".swiper-slide[data-swiper-slide-index='{index}']:not(.swiper-slide-duplicate)")
        self.scroll_to(slide_locator)
        self.wait.wait_for_element_visible(*slide_locator).click()
        time.sleep(1)

    def click_zoom_in_sds43_button(self):
        self.wait.wait_for_element_visible(*self.zoom_in_button).click()

    def click_zoom_out_sds43_button(self):
        self.wait.wait_for_element_visible(*self.zoom_out_button).click()

    def scroll_to_zoom_in_and_out_sds43(self):
        self.scroll_to(self.zoom_in_button)

    def get_zoom_out_disabled_status_sds43(self):
        element = self.wait.wait_for_element_present(*self.zoom_out_button)
        return element.get_attribute("aria-disabled")

    def click_carousel_next_sds43(self):
        self.wait.wait_for_element_visible(*self.right_button).click()
        time.sleep(0.5)

    # Clicks the Previous slide button
    def click_carousel_prev_sds43(self):
        self.wait.wait_for_element_visible(*self.left_button).click()
        time.sleep(0.5)

    def click_read_more_sds43_button(self):
        self.scroll_to(self.read_more)
        self.wait.wait_for_element_visible(*self.read_more).click()

    def get_all_features_sds43_text(self):
        self.wait.wait_for_element_visible(*self.feature_list_items)
        elements = self.driver.find_elements(*self.feature_list_items)
        actual_texts = [el.text.strip() for el in elements if el.text.strip() != ""]
        return actual_texts

    def click_read_less(self):
        self.specific_scroll_to(self.readless)
        self.wait.wait_for_element_visible(*self.readless).click()

    def click_secure_gate_fca(self):
        self.scroll_to(self.secure_gate_fca)
        self.wait.wait_for_element_visible(*self.secure_gate_fca).click()

    def click_complete_specs_feature_list_sds43(self):
        self.scroll_to(self.complete_specs_feature_list)
        self.wait.wait_for_element_visible(*self.complete_specs_feature_list).click()

    def get_compare_diagnostic_product_title(self):
        return self.wait.wait_for_element_visible(*self.compare_diagnostic_product).text

    def scroll_to_and_click_find_a_store_button(self):
        self.scroll_to(self.find_a_store)
        self.wait.wait_for_element_visible(*self.find_a_store).click()

    def click_napa_auto_parts(self):
        self.wait.wait_for_element_visible(*self.napa_auto_parts).click()

    def click_o_reilly_auto_parts(self):
        self.wait.wait_for_element_visible(*self.o_reilly_auto_parts).click()

    def click_auto_zone(self):
        self.wait.wait_for_element_visible(*self.auto_zone).click()

    def click_close_button(self):
        self.wait.wait_for_element_visible(*self.close_button).click()

    def click_download_manual_product(self):
        self.scroll_to(self.download_manual_product)
        self.wait.wait_for_element_visible(*self.download_manual_product).click()

    def click_learn_more_button(self):
        self.scroll_to(self.learn_more)
        self.wait.wait_for_element_visible(*self.learn_more).click()

    def get_diagnostic_tool_title_text(self):
        return self.wait.wait_for_element_visible(*self.diagnostic_tool_title).text

    def click_learn_more_build_for_pros(self):
        self.scroll_to(self.learn_more_build_pro)
        self.wait.wait_for_element_visible(*self.learn_more_build_pro).click()

    def scroll_to_video_sds43(self):
        self.scroll_to(self.main_video_iframe)

    def play_main_youtube_video_sds43(self):
        time.sleep(1.5)
        iframe_element = self.wait.wait_for_element_present(*self.main_video_iframe)
        self.driver.switch_to.frame(iframe_element)
        play_btn = self.wait.wait_for_element_present(*self.yt_large_play_btn)
        self.driver.execute_script("arguments[0].click();", play_btn)

    def get_video_current_time_sds43(self):
        try:
            return self.driver.execute_script("return document.querySelector('video').currentTime")
        except:
            return 0

    def switch_to_default_content_sds43(self):
        self.driver.switch_to.default_content()

    def pause_youtube_video_sds43(self):
        self.driver.execute_script("document.querySelector('video').pause()")

    def is_video_paused_sds43(self):
        return self.driver.execute_script("return document.querySelector('video').paused")

    def scroll_to_store_sds43(self):
        self.scroll_to(self.apple_link)

    def click_apple_link_sds43(self):
        self.wait.wait_for_element_visible(*self.apple_link).click()

    def click_google_link_sds43(self):
        self.wait.wait_for_element_visible(*self.google_play_link).click()

