import time
import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.Support_Pages.HowtoVideos_page import HowtoVideosPage
from utilities.custom_logger import LogMaker


@pytest.mark.HowtoVideos
class TestHowtoVideos:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        home = RSPROHomePage(driver)
        home.go_to_home()

    # ─────────────────────────────────────────────────────────────────────────
    # TC_001: Navigate to How-to Videos page
    # ─────────────────────────────────────────────────────────────────────────

    def test_navigate_to_how_to_videos(self):
        """
        TC_001 - P1 Navigation
        Steps:
            1. Hover Support menu -> click How-to Videos
            2. Verify page loads (heading visible)
        """
        self.logger.info("===== TC_001: Navigate to How-to Videos via Support menu =====")
        page = HowtoVideosPage(self.driver)
        try:
            page.go_to_how_to_videos()
            self.logger.info("Navigated to How-to Videos page")
            heading = page.get_page_heading()
            self.logger.info(f"Page heading: {heading}")
            assert heading, "Page heading is empty or not found"
            self.logger.passed("TC_001 PASS - How-to Videos page loaded successfully")
        except Exception as e:
            self.logger.failed(f"TC_001 FAIL: {e}")
            self.driver.save_screenshot(".\\screenshots\\tc001_how_to_videos_nav.png")
            assert False

    # ─────────────────────────────────────────────────────────────────────────
    # TC_002: Verify video cards are present on the page
    # ─────────────────────────────────────────────────────────────────────────

    def test_videos_are_present(self):
        """
        TC_002 - P1 Functional
        Steps:
            1. Navigate to How-to Videos
            2. Verify at least 1 video card is visible
        """
        self.logger.info("===== TC_002: Verify video cards are present =====")
        page = HowtoVideosPage(self.driver)
        try:
            page.go_to_how_to_videos()
            count = page.get_video_count()
            self.logger.info(f"Total video cards found: {count}")
            assert count > 0, f"Expected at least 1 video, found {count}"
            self.logger.passed(f"TC_002 PASS - Found {count} video cards on the page")
        except Exception as e:
            self.logger.failed(f"TC_002 FAIL: {e}")
            self.driver.save_screenshot(".\\screenshots\\tc002_videos_present.png")
            assert False

    # ─────────────────────────────────────────────────────────────────────────
    # TC_003: Play each video for 3 seconds then pause
    # ─────────────────────────────────────────────────────────────────────────

    def test_play_and_pause_each_video(self):
        """
        TC_003 - P1 Functional
        Steps:
            1. Navigate to How-to Videos
            2. For each video card:
                a. Click play
                b. Wait 3 seconds
                c. Pause the video
                d. Assert video is paused and currentTime > 0
        """
        self.logger.info("===== TC_003: Play each video for 3s then pause =====")
        page = HowtoVideosPage(self.driver)
        try:
            page.go_to_how_to_videos()
            iframes = page.get_all_video_iframes()
            total = len(iframes)
            self.logger.info(f"Total videos to test: {total}")
            assert total > 0, "No video iframes found on the page"

            failed_videos = []
            for i, iframe in enumerate(iframes):
                self.logger.info(f"--- Video {i + 1}/{total} ---")
                try:
                    result = page.play_wait_and_pause(iframe, wait_seconds=3)
                    self.logger.info(
                        f"Video {i + 1}: played={result['played']} | "
                        f"paused={result['paused']} | time={result['current_time']:.1f}s")
                    if not result["paused"]:
                        failed_videos.append(i + 1)
                        self.logger.failed(f"Video {i + 1}: not paused after pause command")
                    else:
                        self.logger.passed(f"Video {i + 1}: OK - played and paused successfully")
                except Exception as e:
                    failed_videos.append(i + 1)
                    self.logger.failed(f"Video {i + 1} error: {e}")
                    self.driver.switch_to_default_content() if hasattr(self.driver, 'switch_to_default_content') else self.driver.switch_to.default_content()

            assert not failed_videos, f"Videos failed to play/pause: {failed_videos}"
            self.logger.passed(f"TC_003 PASS - All {total} videos played and paused successfully")
        except Exception as e:
            self.logger.failed(f"TC_003 FAIL: {e}")
            self.driver.save_screenshot(".\\screenshots\\tc003_play_pause_videos.png")
            assert False

    # ─────────────────────────────────────────────────────────────────────────
    # TC_004: Category "How-to Videos" + Sort "Latest" — check every video
    #         across all 10 pages
    # ─────────────────────────────────────────────────────────────────────────

    def test_how_to_videos_latest_all_pages(self):
        """
        TC_004 - P1 Functional
        Steps:
            1. Navigate to How-to Videos
            2. Click category "How-to Videos"
            3. Click sort "Latest"
            4. For pages 1-10:
                a. Click each video — verify it plays (link works)
                b. Scroll to pagination and click next page number
        """
        self.logger.info("===== TC_004: How-to Videos | Latest | Check all videos across pages =====")
        page = HowtoVideosPage(self.driver)
        max_pages = 10
        findings = {}

        try:
            page.go_to_how_to_videos()
            self.logger.info("Navigated to How-to Videos page")

            page.click_category_how_to_videos()
            self.logger.info("Clicked category: How-to Videos")

            page.click_sort_latest()
            self.logger.info("Clicked sort: Latest")

            actual_pages = min(page.get_total_pages(), max_pages)
            self.logger.info(f"Total pages to check: {actual_pages}")

            for page_num in range(1, actual_pages + 1):
                self.logger.info(f"===== Page {page_num}/{actual_pages} =====")

                iframes = page.get_all_video_iframes()
                video_count = len(iframes)
                self.logger.info(f"Page {page_num}: {video_count} videos found")
                assert video_count > 0, f"No videos found on page {page_num}"

                failed_on_page = []
                for i, iframe in enumerate(iframes):
                    result = page.play_wait_and_pause(iframe, wait_seconds=5)
                    played = result["played"]  # True only if currentTime > 0
                    status = "OK" if played else "NOT OK (unavailable/private)"
                    self.logger.info(f"  Page {page_num} | Video {i + 1}/{video_count}: {status}")
                    if not played:
                        failed_on_page.append(i + 1)

                if failed_on_page:
                    findings[page_num] = failed_on_page
                    self.logger.info(f"Page {page_num}: {len(failed_on_page)} unavailable video(s): {failed_on_page}")
                else:
                    self.logger.passed(f"Page {page_num}: all {video_count} videos OK")

                if page_num < actual_pages:
                    page.click_page_number(page_num + 1)
                    self.logger.info(f"Navigated to page {page_num + 1}")

            if findings:
                self.logger.info(f"TC_004 COMPLETE - Hidden/unavailable videos by page: {findings}")
            self.logger.passed(f"TC_004 PASS - Checked all {actual_pages} page(s) of How-to Videos / Latest")
        except Exception as e:
            self.logger.failed(f"TC_004 FAIL: {e}")
            self.driver.save_screenshot(".\\screenshots\\tc004_how_to_videos_latest.png")
            assert False

    # ─────────────────────────────────────────────────────────────────────────
    # TC_005: Category "How-to Fix" + Sort "Latest" — check every video
    #         across all 10 pages
    # ─────────────────────────────────────────────────────────────────────────

    def test_how_to_fix_latest_all_pages(self):
        """
        TC_005 - P1 Functional
        Steps:
            1. Navigate to How-to Videos
            2. Click category "How-to Fix"
            3. Click sort "Latest"
            4. For each available page (up to 10):
                a. Click each video — verify it plays (link works)
                b. Scroll to pagination and click next page number
        Hidden/unavailable videos are logged as FAIL findings but do not fail the test.
        """
        self.logger.info("===== TC_005: How-to Fix | Latest | Check all videos across pages =====")
        page = HowtoVideosPage(self.driver)
        max_pages = 10
        findings = {}

        try:
            page.go_to_how_to_videos()
            self.logger.info("Navigated to How-to Videos page")

            page.click_category_how_to_fix()
            self.logger.info("Clicked category: How-to Fix")

            page.click_sort_latest()
            self.logger.info("Clicked sort: Latest")

            actual_pages = min(page.get_total_pages(), max_pages)
            self.logger.info(f"Total pages to check: {actual_pages}")

            for page_num in range(1, actual_pages + 1):
                self.logger.info(f"===== Page {page_num}/{actual_pages} =====")

                iframes = page.get_all_video_iframes()
                video_count = len(iframes)
                self.logger.info(f"Page {page_num}: {video_count} videos found")
                assert video_count > 0, f"No videos found on page {page_num}"

                failed_on_page = []
                for i, iframe in enumerate(iframes):
                    result = page.play_wait_and_pause(iframe, wait_seconds=5)
                    played = result["played"]  # True only if currentTime > 0
                    status = "OK" if played else "NOT OK (unavailable/private)"
                    self.logger.info(f"  Page {page_num} | Video {i + 1}/{video_count}: {status}")
                    if not played:
                        failed_on_page.append(i + 1)

                if failed_on_page:
                    findings[page_num] = failed_on_page
                    self.logger.info(f"Page {page_num}: {len(failed_on_page)} unavailable video(s): {failed_on_page}")
                else:
                    self.logger.passed(f"Page {page_num}: all {video_count} videos OK")

                if page_num < actual_pages:
                    page.click_page_number(page_num + 1)
                    self.logger.info(f"Navigated to page {page_num + 1}")

            if findings:
                self.logger.info(f"TC_005 COMPLETE - Hidden/unavailable videos by page: {findings}")
            self.logger.passed(f"TC_005 PASS - Checked all {actual_pages} page(s) of How-to Fix / Latest")
        except Exception as e:
            self.logger.failed(f"TC_005 FAIL: {e}")
            self.driver.save_screenshot(".\\screenshots\\tc005_how_to_fix_latest.png")
            assert False

    # ─────────────────────────────────────────────────────────────────────────
    # TC_006: Search for a video by keyword and verify it plays
    # ─────────────────────────────────────────────────────────────────────────

    def test_search_video_and_play(self):
        """
        TC_006 - P1 Functional
        Steps:
            1. Navigate to How-to Videos
            2. Click search bar (id=search-video)
            3. Type "Innova 7111 - Setup" and press Enter
            4. Verify at least 1 result appears
            5. Click the first video and verify it plays
        """
        self.logger.info("===== TC_006: Search video 'Innova 7111 - Setup' and play =====")
        page = HowtoVideosPage(self.driver)
        keyword = "Innova 7111 - Setup"

        try:
            page.go_to_how_to_videos()
            self.logger.info("Navigated to How-to Videos page")

            page.search_video(keyword)
            self.logger.info(f"Searched for: {keyword}")

            iframes = page.get_all_video_iframes()
            count = len(iframes)
            self.logger.info(f"Search results: {count} video(s) found")
            assert count > 0, f"No videos found for search '{keyword}'"

            result = page.play_wait_and_pause(iframes[0], wait_seconds=3)
            played = result["played"]
            status = "OK" if played else "NOT OK (unavailable/private)"
            self.logger.info(f"First video: {status} | currentTime={result['current_time']:.1f}s")
            assert played, f"First search result video did not play (currentTime=0)"

            self.logger.passed(f"TC_006 PASS - Search '{keyword}' returned {count} result(s) and video plays")
        except Exception as e:
            self.logger.failed(f"TC_006 FAIL: {e}")
            self.driver.save_screenshot(".\\screenshots\\tc006_search_video.png")
            assert False
