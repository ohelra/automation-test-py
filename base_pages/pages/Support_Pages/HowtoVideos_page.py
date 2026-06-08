import time
from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from utilities.waitHelper import WaitHelper


class HowtoVideosPage(RSPROHomePage):
    """Page Object for the Support > How-to Videos page."""

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitHelper(driver)

    # ── Navigation ────────────────────────────────────────────────────────────
    support_menu       = (By.XPATH, "//*[@id='navbarDropdown' and contains(text(),'Support')]")
    how_to_videos_link = (By.XPATH, "//a[contains(normalize-space(),'How') and contains(normalize-space(),'Video')]")

    # ── Page Header ───────────────────────────────────────────────────────────
    page_heading       = (By.XPATH, "//h1[contains(normalize-space(),'How-to Videos')] | //h2[contains(normalize-space(),'How-to Videos')]")

    # ── Category Filter Buttons ───────────────────────────────────────────────
    cat_all            = (By.XPATH, "(//a[@class='web-btn category web-btn-14 btn btn-bg-11 mb-2 mr-2'][normalize-space()='All'])[1]")
    cat_how_to_videos  = (By.XPATH, "(//a[@class='web-btn category web-btn-14 btn btn-bg-11 mb-2 mr-2'][normalize-space()='How-to Videos'])[1]")
    cat_how_to_fix     = (By.XPATH, "(//a[normalize-space()='How-to Fix'])[1]")
    cat_how_to_use     = (By.XPATH, "(//a[@class='web-btn category web-btn-14 btn btn-bg-11 mb-2 mr-2'][normalize-space()='How-to Use'])[1]")

    # ── Sort Buttons ──────────────────────────────────────────────────────────
    sort_popular       = (By.XPATH, "(//a[normalize-space()='Popular'])[1]")
    sort_latest        = (By.XPATH, "(//a[normalize-space()='Latest'])[1]")

    # ── Pagination ────────────────────────────────────────────────────────────
    pagination_bar     = (By.ID, "videoPagination")

    # ── Search ────────────────────────────────────────────────────────────────
    search_input       = (By.ID, "search-video")

    # ── Video Grid ────────────────────────────────────────────────────────────
    video_iframes      = (By.XPATH, "//iframe[contains(@src,'youtube') or contains(@src,'youtu.be')]")
    video_element      = (By.TAG_NAME, "video")

    # ── Navigation Methods ────────────────────────────────────────────────────

    def go_to_how_to_videos(self):
        self.hover(self.support_menu)
        self.wait.wait_for_element_visible(*self.how_to_videos_link).click()
        time.sleep(1.5)

    def get_page_heading(self):
        return self.wait.wait_for_element_visible(*self.page_heading).text

    # ── Filter & Sort Methods ─────────────────────────────────────────────────

    def search_video(self, keyword):
        """Type a keyword into the search bar and press Enter."""
        from selenium.webdriver.common.keys import Keys
        field = self.wait.wait_for_element_visible(*self.search_input)
        field.clear()
        field.send_keys(keyword)
        field.send_keys(Keys.ENTER)
        time.sleep(1.5)

    def click_category_how_to_videos(self):
        """Click the 'How-to Videos' category filter button."""
        btn = self.wait.wait_for_element_visible(*self.cat_how_to_videos)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        btn.click()
        time.sleep(1)

    def click_category_how_to_fix(self):
        """Click the 'How-to Fix' category filter button."""
        btn = self.wait.wait_for_element_visible(*self.cat_how_to_fix)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        btn.click()
        time.sleep(1)

    def click_sort_latest(self):
        """Click the 'Latest' sort button."""
        btn = self.wait.wait_for_element_visible(*self.sort_latest)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        btn.click()
        time.sleep(1)

    def click_sort_popular(self):
        """Click the 'Popular' sort button."""
        btn = self.wait.wait_for_element_visible(*self.sort_popular)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        btn.click()
        time.sleep(1)

    # ── Pagination Methods ────────────────────────────────────────────────────

    def get_total_pages(self):
        """Return the highest page number found inside videoPagination."""
        page_btns = self.driver.find_elements(
            By.XPATH, "//*[@id='videoPagination']//*[normalize-space() and string-length(normalize-space())<=3]"
        )
        texts = [b.text.strip() for b in page_btns if b.text.strip().isdigit()]
        return max((int(t) for t in texts), default=1)

    def scroll_to_pagination(self):
        """Scroll to the videoPagination bar."""
        try:
            bar = self.wait.wait_for_element_visible(*self.pagination_bar)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", bar)
            time.sleep(0.5)
        except Exception:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)

    def click_page_number(self, page_num):
        """Click a specific page number inside videoPagination."""
        self.scroll_to_pagination()
        locator = (
            By.XPATH,
            f"//*[@id='videoPagination']//*[normalize-space()='{page_num}']"
        )
        btn = self.wait.wait_for_element_visible(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        btn.click()
        time.sleep(1.5)

    def get_current_page_number(self):
        """Return the currently active page number from videoPagination."""
        try:
            active = self.driver.find_element(
                By.XPATH,
                "//*[@id='videoPagination']//*[contains(@class,'active') or contains(@class,'current') or @aria-current='page']"
            )
            return active.text.strip()
        except Exception:
            return "?"

    # ── Video Grid Methods ────────────────────────────────────────────────────

    def get_video_count(self):
        """Return total number of YouTube iframes (video cards) on the page."""
        return len(self.driver.find_elements(*self.video_iframes))

    def get_all_video_iframes(self):
        """Return all YouTube iframe elements on the page."""
        return self.driver.find_elements(*self.video_iframes)

    def scroll_to_video(self, iframe_element):
        """Scroll iframe element into center of viewport."""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
            iframe_element
        )
        time.sleep(0.4)

    def play_video_in_iframe(self, iframe_element):
        """Switch into a YouTube iframe and click play."""
        self.driver.switch_to.frame(iframe_element)
        try:
            play_btn = self.wait.wait_for_element_present(
                By.CSS_SELECTOR,
                "button.ytmCuedOverlayPlayButton, button.ytp-large-play-button"
            )
            self.driver.execute_script("arguments[0].click();", play_btn)
        except Exception:
            self.driver.find_element(By.TAG_NAME, "body").click()
        self.driver.switch_to.default_content()

    def pause_video_in_iframe(self, iframe_element):
        """Switch into an iframe and pause the video via JS."""
        self.driver.switch_to.frame(iframe_element)
        self.driver.execute_script("document.querySelector('video').pause();")
        self.driver.switch_to.default_content()

    def is_video_paused(self, iframe_element):
        """Return True if the video inside the iframe is paused."""
        self.driver.switch_to.frame(iframe_element)
        paused = self.driver.execute_script("return document.querySelector('video').paused;")
        self.driver.switch_to.default_content()
        return paused

    def get_video_current_time(self, iframe_element):
        """Return the currentTime (seconds) of the video inside the iframe."""
        self.driver.switch_to.frame(iframe_element)
        current_time = self.driver.execute_script(
            "return document.querySelector('video') ? document.querySelector('video').currentTime : 0;"
        )
        self.driver.switch_to.default_content()
        return current_time or 0

    def check_video_link_works(self, iframe_element, play_seconds=2):
        """
        Click play on a video, wait play_seconds, check currentTime > 0.
        Returns True if video started playing (link/embed works).
        Always pauses and returns to default content after check.
        """
        try:
            self.scroll_to_video(iframe_element)
            self.play_video_in_iframe(iframe_element)
            time.sleep(play_seconds)
            current_time = self.get_video_current_time(iframe_element)
            self.pause_video_in_iframe(iframe_element)
            return current_time > 0
        except Exception:
            try:
                self.driver.switch_to.default_content()
            except Exception:
                pass
            return False

    def play_wait_and_pause(self, iframe_element, wait_seconds=3):
        """
        Full flow: scroll → play → wait → pause.
        Returns dict: {played: bool, paused: bool, current_time: float}
        """
        self.scroll_to_video(iframe_element)
        self.play_video_in_iframe(iframe_element)
        time.sleep(wait_seconds)
        current_time = self.get_video_current_time(iframe_element)
        self.pause_video_in_iframe(iframe_element)
        paused = self.is_video_paused(iframe_element)
        return {
            "played": current_time > 0,
            "paused": paused,
            "current_time": current_time
        }
