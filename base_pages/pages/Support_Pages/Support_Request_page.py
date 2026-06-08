import time
from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage


class SupportRequestPage(RSPROHomePage):

    support_nav         = (By.XPATH, "//*[@id='navbarDropdown' and contains(text(),'Support')]")
    support_request_nav = (By.XPATH, "//ul[@class='dropdown-menu-items']//a[normalize-space()='Support Request']")
    video_iframe        = (By.XPATH, "//iframe[contains(@src,'youtube')]")
    play_button         = (By.XPATH, "//*[@id='player-controls']/ytm-custom-control/ytm-watch-player-controls/cued-overlay/button/c3-icon/span/div")

    def navigate_to_support_request(self):
        self.hover(self.support_nav)
        self.wait.wait_for_element_visible(*self.support_request_nav).click()

    def scroll_and_click_video(self):
        self.scroll_to(self.video_iframe)

    def click_to_video(self):
        iframe = self.wait.wait_for_element_visible(*self.video_iframe)
        self.driver.switch_to.frame(iframe)
        self.wait.wait_for_element_visible(*self.play_button).click()
        time.sleep(4)
        self.driver.switch_to.default_content()

    def is_video_displayed(self):
        return self.wait.wait_for_element_visible(*self.video_iframe).is_displayed()
