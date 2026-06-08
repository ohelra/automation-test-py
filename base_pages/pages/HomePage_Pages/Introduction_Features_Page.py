import time
from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage

class IntroductionFeaturesPage(RSPROHomePage):

    fix_for_dtc_box =               (By.ID, "fix-for-dtc-main")
    repair_tips_box =               (By.ID, "repair-tips-main")
    vehicle_inspection_report_box = (By.ID, "vehicle-inspect-main")
    to_get_started =                (By.ID, "to-get-started")
    container_box =                 (By.ID, "download-the-app")
    tablet_device =                 (By.CSS_SELECTOR, ".dta-tablet")
    phone_device =                  (By.CSS_SELECTOR, ".dta-phone")
    laptop_device =                 (By.CSS_SELECTOR, ".dta-laptop")
    mobile_device =                 (By.XPATH, "//*[contains(@class, 'ca-phone')]")
    Get_Color_1 =                   (By.XPATH, "//*[contains(@class, 's9-indicators') and text()=1]")
    Get_Color_2 =                   (By.XPATH, "//*[contains(@class, 's9-indicators') and text()=2]")
    Get_Color_3 =                   (By.XPATH, "//*[contains(@class, 's9-indicators') and text()=3]")
    Get_Color_4 =                   (By.XPATH, "//*[contains(@class, 's9-indicators') and text()=4]")
    fix_for_dtc_box_scroll =        (By.XPATH, "//div[@id='fix-for-dtc-main']//div[contains(text(),'Did this fix the car?')]")
    repair_tips_box_scroll =        (By.XPATH, "//div[@id='repair-tips-main']//div[@class='dtc-title'][normalize-space()='Repair Validation']")
    vehicle_inspection_scroll =     (By.XPATH, "//span[@class='tab-menu-item pr-6']")

    # Fix for DTC : hover over the box, dark background, zoomed out
    def scroll_to_fix_for_dtc(self):
        self.specific_scroll_to(self.fix_for_dtc_box)

    def hover_fix_for_dtc(self):
        self.hover_element_present(self.fix_for_dtc_box)  # Hover over to the Fix For DTC box
        time.sleep(5)

    # def wait_for_modal_show_dtc(self):
    #     self.wait_for_class_contains(self.fix_for_dtc_box, "show")  # Wait for <ipad-modal> class 'show'
    #     return self.get_attribute_element(self.fix_for_dtc_box, "class")  # Get class attributes to verify

    def is_modal_displayed(self):
        return self.wait.wait_for_element_visible(*self.fix_for_dtc_box_scroll).is_displayed()

    # Repair Tips : hover over the box, dark background, zoomed out
    def scroll_to_repair_tips(self):
        self.specific_scroll_to(self.repair_tips_box)

    def hover_repair_tips(self):
        self.hover_element_present(self.repair_tips_box)  # Hover over to the Fix For DTC box
        time.sleep(5)

    # def wait_for_modal_show_repair(self):
    #     self.wait_for_class_contains(self.repair_tips_box, "show")  # Wait for <ipad-modal> class 'show'
    #     return self.get_attribute_element(self.repair_tips_box, "class")  # Get class attributes to verify

    def is_modal_displayed_repair(self):
        return self.wait.wait_for_element_visible(*self.repair_tips_box_scroll).is_displayed()

    # Vehicle Inspection Reports : hover over the box, dark background, zoomed out
    def scroll_to_vehicle_inspection_report(self):
        self.specific_scroll_to(self.vehicle_inspection_report_box)

    def hover_vehicle_inspection_report(self):
        self.hover_element_present(self.vehicle_inspection_report_box)  # Hover over to the Fix For DTC box
        time.sleep(5)

    # def wait_for_modal_show_vehicle(self):
    #     self.wait_for_class_contains(self.vehicle_inspection_report_box, "show")  # Wait for <ipad-modal> class 'show'
    #     return self.get_attribute_element(self.vehicle_inspection_report_box,"class")  # Get class attributes to verify

    def is_modal_displayed_vehicle(self):
        return self.wait.wait_for_element_visible(*self.vehicle_inspection_scroll).is_displayed()

    # ==================================================================================================

    # Indicator number 1
    def scroll_to_get_color(self):
        self.scroll_to(self.to_get_started)

    def hover_1_obtain(self):
        self.hover(self.Get_Color_1)
        #time.sleep(5)

    def get_color_1_default(self):
        df = self.find(self.Get_Color_1)
        return df.value_of_css_property("background-color")

    def get_color_1_changed(self):
        changed  = self.find(self.Get_Color_1)
        return changed.value_of_css_property("background-image")

    # Indicator number 2
    def hover_2_obtain(self):
        self.hover(self.Get_Color_2)
        #time.sleep(5)

    def get_color_2_default(self):
        df = self.find(self.Get_Color_2)
        return df.value_of_css_property("background-color")

    def get_color_2_changed(self):
        changed  = self.find(self.Get_Color_2)
        return changed.value_of_css_property("background-image")

    # Indicator number 3
    def hover_3_obtain(self):
        self.hover(self.Get_Color_3)
        #time.sleep(5)

    def get_color_3_default(self):
        df = self.find(self.Get_Color_3)
        return df.value_of_css_property("background-color")

    def get_color_3_changed(self):
        changed  = self.find(self.Get_Color_3)
        return changed.value_of_css_property("background-image")

    # Indicator number 4
    def hover_4_obtain(self):
        self.hover(self.Get_Color_4)
        #time.sleep(5)

    def get_color_4_default(self):
        df = self.find(self.Get_Color_4)
        return df.value_of_css_property("background-color")

    def get_color_4_changed(self):
        changed  = self.find(self.Get_Color_4)
        return changed.value_of_css_property("background-image")


    #==================================================================================================
    def scroll_to_mobile_device(self):
        self.scroll_to(self.mobile_device)
        time.sleep(3)

    def hover_mobile_device(self):
        self.hover(self.mobile_device)
        time.sleep(2)

    def get_mobile_scale_default(self):
        mobile_element = self.find(self.mobile_device)
        return mobile_element.value_of_css_property("transform")

    def get_mobile_scale_after_hover(self):
        mobile_element = self.find(self.mobile_device)
        return mobile_element.value_of_css_property("transform")


    # ==================================================================================================
    def scroll_to_grid_2_box(self):
        self.scroll_to(self.container_box)

    def hover_grid_box(self):
        self.hover(self.container_box)
        time.sleep(2)

    def get_css_property(self, locator, property_name):
        element = self.find(locator)
        return element.value_of_css_property(property_name)

    def get_device_positions(self):
        return {
            'tablet_left':  self.get_css_property(self.tablet_device, "left"),
            'phone_bottom': self.get_css_property(self.phone_device, "left"),
            'laptop_right': self.get_css_property(self.laptop_device, "left")
        }