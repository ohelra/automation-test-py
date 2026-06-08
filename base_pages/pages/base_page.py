from selenium.webdriver import ActionChains
from utilities.custom_logger import LogMaker
from utilities.waitHelper import WaitHelper
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)
        self.action = ActionChains(self.driver)
        self.logger = LogMaker.log_gen()

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.wait_for_element_present(*locator)

    def hover(self, locator):
        element = self.wait.wait_for_element_visible(*locator)
        self.action.move_to_element(element).perform()

    def hover_element_present(self, locator):
        element = self.wait.wait_for_element_present(*locator)
        self.action.move_to_element(element).perform()
        self.driver.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true, cancelable: true}));",element)

    def scroll_to(self, locator):
        element = self.wait.wait_for_element_visible(*locator)
        self.action.scroll_to_element(element).perform()

    def specific_scroll_to(self, locator):
        element = self.wait.wait_for_element_present(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", element)

    def get_attribute_element(self, locator, attribute: str):
        el = self.wait.wait_for_element_present(*locator)
        return el.get_attribute(attribute)

    def wait_for_class_contains(self, locator, class_substr: str, timeout: int = 15):
        def _class_contains(driver):
            el = driver.find_element(*locator)
            cl = el.get_attribute("class") or ""
            return class_substr in cl
        WebDriverWait(self.driver, timeout).until(_class_contains)
        return True

    def navigate_new_tab(self, click_action, expected_url_part, get_text_action, expected):
        original_window = self.driver.current_window_handle
        self.logger.info("Click link to open new tab")
        click_action()
        try:
            WebDriverWait(self.driver, 5).until(ec.number_of_windows_to_be(2))
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
            self.logger.info(f"Switched to new tab: {self.driver.title}")
            current_url = self.driver.current_url.lower()
            assert expected_url_part in current_url and get_text_action() == expected
        except Exception as e:
            self.logger.failed(f"Failed to verify new tab", e)
            self.driver.save_screenshot(f".\\screenshots\\fail_tab_{expected_url_part}.png")
        finally:
            if len(self.driver.window_handles) > 1:
                self.driver.close()
            self.driver.switch_to.window(original_window)
            self.logger.info("Closed tab and switched back to original window.")


    def navigate_new_tab_with_url(self, click_action, expected_url_part):
        original_window = self.driver.current_window_handle
        self.logger.info("Click link to open new tab")
        click_action()
        try:
            WebDriverWait(self.driver, 5).until(ec.number_of_windows_to_be(2))
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
            self.logger.info(f"Switched to new tab: {self.driver.title}")
            current_url = self.driver.current_url.lower()
            self.logger.info(f"Get current url: {current_url}")
            assert expected_url_part in current_url
        except Exception as e:
            self.logger.failed(f"Failed to verify new tab", e)
            self.driver.save_screenshot(f".\\screenshots\\fail_tab_{expected_url_part}.png")
        finally:
            if len(self.driver.window_handles) > 1:
                self.driver.close()
            self.driver.switch_to.window(original_window)
            self.logger.info("Closed tab and switched back to original window.")