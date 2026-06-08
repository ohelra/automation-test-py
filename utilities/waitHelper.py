from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitHelper:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element_visible(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def wait_for_element_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def wait_for_element_present(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def is_text_present(self, by, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element((by, locator), text))

    def wait_for_element_invisible(self, by, locator, timeout=15):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.invisibility_of_element_located((by, locator)))
        except TimeoutException:
            pass

    def wait_for_element_present_speed(self, by, locator, timeout=1):
        try:
            wait_short = WebDriverWait(self.driver, timeout)
            wait_short.until(EC.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False