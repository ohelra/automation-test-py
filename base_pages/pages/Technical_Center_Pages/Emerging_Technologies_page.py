from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage

class EmergingTechnologiesPage(RSPROHomePage):

    paragraphs =                    (By.CSS_SELECTOR, "#article-content p")
    list_items =                    (By.XPATH,        "//div[@id='article-content']//li[normalize-space()]")
    main_title =                    (By.XPATH,        "//span[contains(text(),'How Advanced Safety Features Are Changing Consumer')]")
    main_title_alternative =        (By.XPATH,        "//span[contains(text(),'The Impact of Alternative Fuel Technologies on Fut')]")
    main_title_sophistication =     (By.XPATH,        "//span[contains(text(),'The Impact of Sophistication and Emissions Regulations on Vehicle Reliability')]")
    main_title_rising =             (By.XPATH,        "//span[contains(text(),'The Rising Cost of New Vehicles: From $30K to $50K in Just 12 Years')]")
    technical_center =              (By.XPATH,        "//*[@id='navbarDropdown' and contains(text(),'Technical Center')]")
    emerging_technologies =         (By.XPATH,        "//a[normalize-space()='Emerging Technologies']")
    alternative =                   (By.XPATH,        "//a[@id='item-alternative-fuel-technologies']")
    sophistication =                (By.XPATH,        "(//a[normalize-space()='Sophistication and Emissions Regulations'])[1]")
    rapid =                         (By.XPATH,        "//a[@id='item-rapid-global-adoption-of-electric-vehicles-']")
    rising =                        (By.XPATH,        "//a[@id='item-rising-cost-of-new-vehicles']")

    def navigate_to_technical_center(self):
        self.hover(self.technical_center)
        self.wait.wait_for_element_visible(*self.emerging_technologies).click()

    def get_main_title(self):
        return self.wait.wait_for_element_visible(*self.main_title).text

    def get_main_title_alternative(self):
        return self.wait.wait_for_element_visible(*self.main_title_alternative).text

    def get_main_title_sophistication(self):
        return self.wait.wait_for_element_visible(*self.main_title_sophistication).text

    def get_main_tile_rising(self):
        return self.wait.wait_for_element_visible(*self.main_title_rising).text

    def navigate_to_alternative_fuel_technologies(self):
        self.wait.wait_for_element_visible(*self.alternative).click()

    def navigate_to_sophistication_emission_regulations(self):
        self.wait.wait_for_element_visible(*self.sophistication).click()

    def navigate_to_rapid_global_adoption_electric_vehicles(self):
        self.wait.wait_for_element_visible(*self.rapid).click()

    def navigate_to_rising_cost_new_vehicle(self):
        self.wait.wait_for_element_visible(*self.rising).click()

    def get_clean_text_list(self,locator):
        element = self.wait.wait_for_element_visible(*locator)
        texts = []
        for e in element:
            text = e.text.strip()
            if text:
                texts.append(" ".join(text.split()))
        return texts

    def get_all_paragraph(self):
        elements = self.driver.find_elements(*self.paragraphs)
        texts = []
        for elem in elements:
            text = elem.text.strip()
            if text:
                texts.append(" ".join(text.split()))
        return texts

    def get_all_list_items(self):
        elements = self.driver.find_elements(*self.list_items)
        texts = []

        for elem in elements:
            try:
                text = elem.text.strip()
                if text != "":
                    texts.append(" ".join(text.split()))
            except:
                continue
        return texts
