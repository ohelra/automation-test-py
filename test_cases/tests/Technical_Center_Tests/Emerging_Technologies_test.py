import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.Technical_Center_Pages.Emerging_Technologies_page import EmergingTechnologiesPage
from utilities.custom_logger import LogMaker
from utilities.json_reader import JsonReader

@pytest.mark.SignUp
class TestEmergingTechnologies:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()


    @pytest.mark.parametrize("test_data",[JsonReader("emerging_technologies_data/advanced_safety_features.json").get_data("advanced")])
    def test_verify_article_content_advanced_safety_features_display(self,test_data):
        self.logger.info("===== Verify that user navigate to Advanced Safety Features Page =====")
        emerging = EmergingTechnologiesPage(self.driver)
        emerging.navigate_to_technical_center()
        self.logger.info("Navigate to Technical Center")
        try:
            assert emerging.get_main_title() == test_data["main_title"]
            self.logger.info("Main Title was found")
            actual_paragraph = emerging.get_all_paragraph()
            actual_items = emerging.get_all_list_items()

            for expect_p in test_data["expected_paragraphs"]:
                clear_paragraph = " ".join(expect_p.split())
                assert any(clear_paragraph in actual_p for actual_p in actual_paragraph)

            for expect_i in test_data["expected_list_items"]:
                clear_item = " ".join(expect_i.split())
                assert any(clear_item in actual_i for actual_i in actual_items)

        except Exception as e:
            self.logger.failed("The article is incorrect contents", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_article_content_advanced_safety_features_display.png")
            assert False


    @pytest.mark.parametrize("test_data", [JsonReader("emerging_technologies_data/alternative_fuel_technologies.json").get_data("alternative")])
    def test_verify_article_content_alternative_fuel_technologies_page(self, test_data):
        self.logger.info("===== Verify that user navigate to Alternative Fuel Technologies Page =====")
        emerging = EmergingTechnologiesPage(self.driver)
        emerging.navigate_to_technical_center()
        self.logger.info("Navigate to Technical Center")
        emerging.navigate_to_alternative_fuel_technologies()
        self.logger.info("Navigate to Alternative Fuel Technologies")
        try:
            assert emerging.get_main_title_alternative() == test_data["main_title"]
            self.logger.info("Main Title was found")
            actual_paragraph = emerging.get_all_paragraph()
            actual_items = emerging.get_all_list_items()

            for expect_p in test_data["expected_paragraphs"]:
                clear_paragraph = " ".join(expect_p.split())
                assert any(clear_paragraph in actual_p for actual_p in actual_paragraph)

            for expect_i in test_data["expected_list_items"]:
                clear_item = " ".join(expect_i.split())
                assert any(clear_item in actual_i for actual_i in actual_items)

        except Exception as e:
            self.logger.failed("The article is incorrect contents", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_article_content_alternative_fuel_technologies.png")
            assert False


    @pytest.mark.parametrize("test_data", [JsonReader("emerging_technologies_data/sophistication_emissions_regulations.json").get_data("sophistication")])
    def test_verify_article_content_sophistication_emissions_regulations_page(self, test_data):
        self.logger.info("===== Verify that user navigate to Sophistication Emissions Regulations Page =====")
        emerging = EmergingTechnologiesPage(self.driver)
        emerging.navigate_to_technical_center()
        self.logger.info("Navigate to Technical Center")
        emerging.navigate_to_sophistication_emission_regulations()
        self.logger.info("Navigate to Sophistication Emissions Regulations")
        try:
            assert emerging.get_main_title_sophistication() == test_data["main_title"]
            self.logger.info("Main Title was found")
            actual_paragraph = emerging.get_all_paragraph()
            actual_items = emerging.get_all_list_items()

            for expect_p in test_data["expected_paragraphs"]:
                clear_paragraph = " ".join(expect_p.split())
                assert any(clear_paragraph in actual_p for actual_p in actual_paragraph)

            for expect_i in test_data["expected_list_items"]:
                clear_item = " ".join(expect_i.split())
                assert any(clear_item in actual_i for actual_i in actual_items)

        except Exception as e:
            self.logger.failed("The article is incorrect contents", e)
            self.driver.save_screenshot(
                ".\\screenshots\\test_verify_article_content_sophistication_emissions_regulations_page.png")
            assert False


    @pytest.mark.parametrize("test_data",[JsonReader("emerging_technologies_data/rising_cost_new_vehicles.json").get_data("rising_cost")])
    def test_verify_article_content_rising_cost_new_vehicles_page(self, test_data):
        self.logger.info("===== Verify that user navigate to Rising Cost of New Vehicles Page=====")
        emerging = EmergingTechnologiesPage(self.driver)
        emerging.navigate_to_technical_center()
        self.logger.info("Navigate to Technical Center")
        emerging.navigate_to_rising_cost_new_vehicle()
        self.logger.info("Navigate to Rising Cost of New Vehicles Page")
        try:
            assert emerging.get_main_tile_rising() == test_data["main_title"]
            self.logger.info("Main Title was found")
            actual_paragraph = emerging.get_all_paragraph()
            actual_items = emerging.get_all_list_items()

            for expect_p in test_data["expected_paragraphs"]:
                clear_paragraph = " ".join(expect_p.split())
                assert any(clear_paragraph in actual_p for actual_p in actual_paragraph)

            for expect_i in test_data["expected_list_items"]:
                clear_item = " ".join(expect_i.split())
                assert any(clear_item in actual_i for actual_i in actual_items)

        except Exception as e:
            self.logger.failed("The article is incorrect contents", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_article_content_sophistication_emissions_regulations_page.png")
            assert False


    @pytest.mark.parametrize("test_data", [JsonReader("emerging_technologies_data/rapid_global_adoption.json").get_data("ev_adoption")])
    def test_verify_article_content_rapid_global_adoption(self, test_data):
        self.logger.info("===== Verify that user navigate to Rapid Global Adoption of Electric Vehicles Page =====")
        emerging = EmergingTechnologiesPage(self.driver)
        emerging.navigate_to_technical_center()
        self.logger.info("Navigate to Technical Center")
        emerging.navigate_to_rapid_global_adoption_electric_vehicles()
        self.logger.info("Navigate to Rapid Global Adoption of Electric Vehicles")
        try:
            actual_paragraph = emerging.get_all_paragraph()
            actual_items = emerging.get_all_list_items()

            for expect_p in test_data["expected_paragraphs"]:
                clear_paragraph = " ".join(expect_p.split()).lower()

                is_found = any(clear_paragraph in " ".join(actual_p.split()).lower()for actual_p in actual_paragraph)
                assert is_found, f"Paragraph not found: {expect_p}"

            for expect_i in test_data["expected_list_items"]:
                clear_item = " ".join(expect_i.split())
                is_found = any(clear_item in actual_i for actual_i in actual_items)
                assert is_found

        except Exception as e:
            self.logger.error(f"The article has incorrect contents",e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_article_content_rapid_global_adoption.png")
            raise e






