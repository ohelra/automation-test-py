import time
import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.My_Report_Pages.My_Report_page import MyReportPage
from utilities.custom_logger import LogMaker
from utilities.json_reader import JsonReader

@pytest.mark.MyReport
class TestMyReport:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self,request,setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        request.testdata = JsonReader("my_reports.json")
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()
        self.home_page.click_my_account()
        self.home_page.perform_login()


    @pytest.mark.parametrize("vehicle", vehicles_data := JsonReader("my_reports.json").get_data("search_vehicle")["vehicles"])
    def test_verify_search_report_by_vehicle(self, vehicle):
        """
        Step by step:
            1. Login account
            2. Search vehicles : RAM,TOYOTA,HYUNDAI,ACURA,CHRYSLER,CHEVROLET,DODGE,GMC,BMW,AUDI,LAND,FORD,MITSUBISHI,SUBARU
            3. Verify the Vehicle column matching each vehicle keyword
        """
        self.logger.info("===== Verify Search valid vehicle report =====")
        search_page = MyReportPage(self.driver)
        try:
            #self.driver.refresh()
            self.logger.info(f"Testing keyword : {vehicle}")
            search_page.enter_search(vehicle)
            self.logger.info("Enter vehicle keyword")
            search_page.get_contains_vehicle_values(vehicle)
            self.logger.info("Table contains vehicle keyword")
            self.logger.passed(f"The table contains vehicles {vehicle}")
        except Exception as e:
            self.logger.failed(f"Failed dont match keyword '{vehicle}'", e)
            self.driver.save_screenshot(f".\\screenshots\\test_verify_search_type_{vehicle}.png")
            assert False


    # Search report by ID
    @pytest.mark.parametrize("report_id", id_data := JsonReader("my_reports.json").get_data("search_id")["id"])
    def test_verify_search_report_by_id(self, report_id):
        """
        Step by step:
            1. Login account
            2. Search ID reports: 1,3,5,7,8,9,10,15,21,25,29,35,50,70,88,90,155,239,241,248,250,255
            3. Verify the ID column matching each ID keyword
        """
        self.logger.info("===== Verify Search valid ID report =====")
        search_page = MyReportPage(self.driver)
        try:
            # self.driver.refresh()
            search_page.enter_search(report_id)
            self.logger.info(f"Enter ID keyword : {report_id}")
            search_page.get_contains_id_values(report_id)
            self.logger.info("Table contains ID keyword")
            self.logger.passed(f"The table contains ID keyword {report_id}")
        except Exception as e:
            self.logger.failed("Failed : Not show result", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_search_report_by_id.png")
            assert False


    #Search report by types
    @pytest.mark.parametrize("report_type", type_data := JsonReader("my_reports.json").get_data("search_types")["types"])
    def test_verify_search_report_by_types(self, report_type):
        """
        Step by step:
            1. Login account
            2. Search types : OBD II, Diagnostic, Customer, Collision
            3. Verify the Type column matching each type keyword
        """
        self.logger.info("===== Verify Search valid type report =====")
        search_page = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            self.logger.info(f"Testing keyword: {report_type}")
            search_page.enter_search(report_type)
            self.logger.info("Enter type keyword")
            search_page.get_contains_type_values(report_type)
            self.logger.passed(f"The table contains type keyword: {report_type}")
        except Exception as e:
            self.logger.failed(f"Failed dont match type '{report_type}'", e)
            self.driver.save_screenshot(f".\\screenshots\\test_verify_search_type_{report_type}.png")
            assert False


    # Search report by customer
    @pytest.mark.parametrize("customers", customer_data := JsonReader("my_reports.json").get_data("search_customer")["customer"])
    def test_verify_search_report_by_customer(self, customers):
        """
        Step by Step:
            1. Login account
            2. Search customer
            3. Verify the Customer column matching each keyword
        """
        self.logger.info("===== Verify Search valid customer report =====")
        search_page = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            self.logger.info(f"Testing keyword: {customers}")
            search_page.enter_search(customers)
            self.logger.info("Enter customer keyword")
            search_page.get_contains_customer_values(customers)
            self.logger.info("Table contains customer keyword")
            self.logger.passed("The table contains customer keyword")
        except Exception as e:
            self.logger.failed("Failed : Not show result", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_search_report_by_customer.png")
            assert False


    # Display Not found report when searching invalid keyword
    data = JsonReader("my_reports.json").get_data("search_invalid")
    @pytest.mark.parametrize("input_dt, expected_dt", [(data["input"], data["expected"])])
    def test_verify_displayed_not_found_with_invalid_search(self, input_dt, expected_dt):
        """
        Step by Step:
            1. Login account
            2. Search invalid keyword
            3. Verify the report table display Not found report
        """
        self.logger.info("===== Verify search Not Found with invalid keyword =====")
        search_page = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            self.logger.info(f"Testing keyword: {input_dt}")
            search_page.enter_search(input_dt)
            self.logger.info("Enter invalid keyword")
            not_found = search_page.get_contains_not_found()
            self.logger.info("Get invalid keyword and displayed message")
            assert not_found == expected_dt
            self.logger.passed("Displayed 'No reports found.' successfully")
        except Exception as e:
            self.logger.failed("Failed : Not show result", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_displayed_not_found_invalid.png")
            assert False


    #date_data = JsonReader("my_reports.json").get_data("date_picker")
    #@pytest.mark.parametrize("from_date, to_date", [(d["from_date"], d["to_date"]) for d in date_data])
    # Filter Date picker
    @pytest.mark.parametrize("from_date, to_date", [("01 10 2026", "01 27 2026")])
    def test_verify_valid_date_picker_from_to_by_filter(self, from_date, to_date):
        """
        Step by Step:
            1. Login account
            2. Click Filter button
            3. Enter From date
            4. Enter To date
            5. Verify list dates in Date and Time column in range (From - To)
        """
        self.logger.info("===== Verify Date Picker from to valid date =====")
        date_picker = MyReportPage(self.driver)
        self.driver.refresh()
        time.sleep(3)
        date_picker.filter_click()
        self.logger.info("Click filter button")
        entered_from_date = date_picker.enter_date_from(from_date).date()
        self.logger.info("Enter date From filter keyword")
        entered_to_date = date_picker.enter_to_date(to_date).date()
        self.logger.info("Enter date To filter keyword")
        table_dates = date_picker.get_date_values()
        for d in table_dates:
            assert entered_from_date <= d <= entered_to_date, \
                f"Date {d.strftime('%m/%d/%Y')} is out of range {entered_from_date.strftime('%m/%d/%Y')} - {entered_to_date.strftime('%m/%d/%Y')}"
        self.logger.passed("The date in range From and To keyword")


    # Filter types : OBD II, Diagnostic, Customer, Collision, Sample
    # Filter with OBD-II type
    def test_verify_filter_click_obd2_type(self):
        """
        Step by Step:
            1. Login account
            2. Click Filter button
            3. Click OBD II type
            4. Verify that the report table display all OBD II in Type column
        """
        self.logger.info("===== Verify filter click OBD II type =====")
        filter_type = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            time.sleep(3)
            filter_type.filter_click()
            self.logger.info("Click filter type")
            filter_type.click_type_obd2()
            self.logger.info("Click OBD II type")
            filter_type.get_contains_type_values("OBD II")
            self.logger.info("Table contains OBD II type")
            self.logger.passed("The table contains OBD II type")
        except Exception as e:
            self.logger.failed("Failed : Not matching obd2 keyword type", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_filter_click_obd2_type.png")


    # Filter with Diagnostic type
    def test_verify_filter_click_diagnostic_type(self):
        """
        Step by Step:
            1. Login account
            2. Click Filter button
            3. Click Diagnostic type
            4. Verify that the report table display all Diagnostic in Type column
        """
        self.logger.info("===== Verify filter click diagnostic type =====")
        filter_type = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            time.sleep(3)
            filter_type.filter_click()
            self.logger.info("Click filter type")
            filter_type.click_type_diagnostic()
            self.logger.info("Click diagnostic type")
            filter_type.get_contains_type_values("Diagnostic")
            self.logger.info("Table contains diagnostic type")
            self.logger.passed("The table contains diagnostic type")
        except Exception as e:
            self.logger.failed("Failed : Not matching diagnostic keyword type", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_filter_click_diagnostic_type.png")


    # Filter with Customer type
    def test_verify_filter_click_customer_type(self):
        """
        Step by step:
            1. Login account
            2. Click Filter button
            3. Click Customer type
            4. Verify the report table display all Customer in Type column
        """
        self.logger.info("===== Verify filter click customer type =====")
        filter_type = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            time.sleep(3)
            filter_type.filter_click()
            self.logger.info("Click filter type")
            filter_type.click_type_customer()
            self.logger.info("Click customer type")
            filter_type.get_contains_type_values("Customer")
            self.logger.info("Table contains customer type")
            self.logger.passed("The table contains customer type")
        except Exception as e:
            self.logger.failed("Failed : Not matching customer keyword type", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_filter_click_customer_type.png")


    # Filter with Collision type
    def test_verify_filter_collision_type(self):
        """
        Step by Step:
            1. Login account
            2. Click Filter button
            3. Click Collision type
            4. Verify the report table display all Collision in Type column
        """
        self.logger.info("===== Verify filter collision type =====")
        filter_type = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            time.sleep(3)
            filter_type.filter_click()
            self.logger.info("Click filter type")
            filter_type.click_type_collision()
            self.logger.info("Click collision type")
            filter_type.get_contains_type_values("Collision")
            self.logger.info("Table contains collision type")
            self.logger.passed("The table contains collision type")
        except Exception as e:
            self.logger.failed("Failed : Not matching collision keyword type", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_filter_collision_type.png")


    # Filter with Sample type
    def test_verify_filter_sample_type(self):
        """
        Step by Step:
            1. Login account
            2. Click Filter button
            3. Click Collision type
            4. Verify the report table display all Sample in Type column
        """
        self.logger.info("===== Verify filter sample type =====")
        filter_type = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            time.sleep(3)
            filter_type.filter_click()
            self.logger.info("Click filter type")
            filter_type.click_type_sample()
            self.logger.info("Click sample type")
            filter_type.get_contains_type_values("Sample")
            self.logger.info("Table contains sample type")
            self.logger.passed("The table contains sample type")
        except Exception as e:
            self.logger.failed("Failed : Not matching sample keyword type", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_filter_sample_type.png")


    # Filter tools : 7111, SDS43, SDS50
    # Filter with 7111 tool
    def test_verify_filter_7111_tool(self):
        """
        Step by Step:
            1. Login account
            2.Click Filter button
            3. Click 7111 tool
            4. Verify that the report table display all 7111 in Tool column
        """
        self.logger.info("===== Verify filter 7111 tool =====")
        filter_tool = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            time.sleep(3)
            filter_tool.filter_click()
            self.logger.info("Click filter tool")
            filter_tool.click_tool_7111()
            self.logger.info("Click tool 7111")
            filter_tool.get_contains_tool_values("7111")
            self.logger.info("Table contains 7111 tool")
            self.logger.passed("The table contains 7111 tool")
        except Exception as e:
            self.logger.failed("Failed : Not matching 7111 keyword tool", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_filter_7111_tool.png")


    # Filter with SDS43 tool
    def test_verify_filter_sds43_tool(self):
        """
        Step by Step:
            1. Login account
            2. Click Filter button
            3. Click SDS43 tool
            4. Verify that the report table display all SDS43 Tool column
        """
        self.logger.info("===== Verify filter sds43 tool  =====")
        filter_tool = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            time.sleep(3)
            filter_tool.filter_click()
            self.logger.info("Click filter tool")
            filter_tool.click_tool_sds43()
            self.logger.info("Click tool SDS43")
            filter_tool.get_contains_tool_values("SDS43")
            self.logger.info("Table contains SDS43 tool")
            self.logger.passed("The table contains SDS43 tool")
        except Exception as e:
            self.logger.failed("Failed : Not matching SDS43 keyword tool", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_filter_SDS43_tool.png")


    # Filter with SDS50 tool
    def test_verify_filter_sds50_tool(self):
        """
        Step by Step:
            1. Login account
            2. Click Filter button
            3. Click SDS50 tool
            4. Verify that the report table display all SDS50 Tool column
        """
        self.logger.info("===== Verify filter SDS50 tool =====")
        filter_tool = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            time.sleep(3)
            filter_tool.filter_click()
            self.logger.info("Click filter tool")
            filter_tool.click_tool_sds50()
            self.logger.info("Click tool SDS50")
            filter_tool.get_contains_tool_values("SDS50")
            self.logger.info("Table contains SDS50 tool")
            self.logger.passed("The table contains SDS50 tool")
        except Exception as e:
            self.logger.failed("Failed : Not matching SDS50 keyword tool", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_filter_SDS50_tool.png")


    # Clear all filter
    def test_verify_clear_button_enable(self):
        """
        Step by Step:
            1. Login account
            2. Click Filter button
            3. Click any button (Type : Diagnostic)
            4. Click Clear button
            5. Verify Filter pop up return default, not display any type, tool, date
        """
        self.logger.info("===== Verify clear button enable =====")
        clear_btn = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            time.sleep(3)
            clear_btn.filter_click()
            self.logger.info("Click filter button")
            clear_btn.click_type_diagnostic()
            self.logger.info("Select Diagnostic type")
            self.logger.info("Type button selected and displayed")
            clear_btn.click_clear_button()
            self.logger.info("Click Clear button")
            assert clear_btn.is_type_cleared()
            self.logger.passed("Clear button is enable and remove Diagnostic type")
        except Exception as e:
            self.logger.failed("Failed : Not matching clear button enable", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_clear_button_enable.png")


    #Select check box
    #Edit with valid fields : FirstName, LastName, Phone, Email
    user = JsonReader("my_reports.json").get_data("edit_valid_user")
    @pytest.mark.parametrize("first_name, last_name, phone, email", [(user["first_name"], user["last_name"], user["phone"], user["email"])])
    def test_verify_can_edit_with_valid_information(self, first_name, last_name, phone, email):
        """
        Step by Step:
            1. Login account
            2. Choose select check box at first
            3. Click Edit bụtton
            4. Enter First Name in textbox
            5. Enter Last Name in textbox
            6. Enter Phone Number in textbox
            7. Enter Email in textbox
            8. Verify can click Save button
        """
        self.logger.info("===== Verify can_edit with invalid information =====")
        edit = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            edit.select_check_box()
            self.logger.info("Choose select checkbox report")
            edit.click_edit_button()
            self.logger.info("Click edit button")
            edit.enter_first_name_textbox(first_name)
            self.logger.info("Enter first name in textbox")
            edit.enter_last_name_textbox(last_name)
            self.logger.info("Enter last name in textbox")
            edit.enter_email_textbox(email)
            self.logger.info("Enter phone in textbox")
            edit.enter_phone_textbox(phone)
            self.logger.info("Enter email in textbox")
            assert edit.get_enable_save_button(), "Save button is disabled"
            edit.click_save_button()
            self.logger.passed("Edit save successfully")
        except Exception as e:
            self.logger.failed("Failed : Cannot save user information", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_cannot_edit.png")


    # # Edit with empty fields : FirstName, LastName, Phone, Email
    user = JsonReader("my_reports.json").get_data("empty_field")
    # @pytest.mark.parametrize("first_name_empty",[(user["first_name"])])
    # def test_verify_edit_cannot_save_with_empty_first_name(self, first_name_empty):
    #     """
    #     Step by Step:
    #         1. Login account
    #         2. Choose select check box at first
    #         3. Click Edit button
    #         4. Enter First Name with " "
    #         5. Verify the First Name textbox display red border color and message "This field is required."
    #     """
    #     self.logger.info("===== Verify edit can not save with empty first name =====")
    #     edit = MyReportPage(self.driver)
    #     try:
    #         self.driver.refresh()
    #         edit.select_check_box()
    #         self.logger.info("Choose select checkbox report")
    #         edit.click_edit_button()
    #         self.logger.info("Click edit button")
    #         edit.enter_first_name_textbox(first_name_empty)
    #         self.logger.info("Enter empty value in first name textbox")
    #         edit.click_save_button()
    #         self.logger.info("Click save button to display red border")
    #         assert edit.is_error_red_border(edit.first_name) and edit.is_required_firstname_error() == "This field is required."
    #         self.logger.passed("Text box display red border and message successfully")
    #     except Exception as e:
    #         self.logger.failed("Failed : Can save user information", e)
    #         self.driver.save_screenshot(".\\screenshots\\test_verify_edit_cannot_save_with_empty_first_name.png")
    #
    #
    # @pytest.mark.parametrize("last_name_empty",[(user["last_name"])])
    # def test_verify_edit_cannot_save_with_empty_last_name(self, last_name_empty):
    #     """
    #     Step by Step:
    #         1. Login account
    #         2. Choose select check box at first
    #         3. Click Edit button
    #         4. Enter Last Name with " "
    #         5. Verify the Last Name textbox display red border color and message "This field is required."
    #     """
    #     self.logger.info("===== Verify edit can not save with empty last name =====")
    #     edit = MyReportPage(self.driver)
    #     try:
    #         self.driver.refresh()
    #         edit.select_check_box()
    #         self.logger.info("Choose select checkbox report")
    #         edit.click_edit_button()
    #         self.logger.info("Click edit button")
    #         edit.enter_last_name_textbox(last_name_empty)
    #         self.logger.info("Enter empty value in last name textbox")
    #         edit.click_save_button()
    #         self.logger.info("Click save button to display red border")
    #         assert edit.is_error_red_border(edit.last_name) and edit.is_required_lastname_error() == "This field is required."
    #         self.logger.passed("Text box display red border and message successfully")
    #     except Exception as e:
    #         self.logger.failed("Failed : Can save user information", e)
    #         self.driver.save_screenshot(".\\screenshots\\test_verify_edit_cannot_save_with_empty_last_name.png")
    #
    #
    # @pytest.mark.parametrize("phone_empty",[(user["phone"])])
    # def test_verify_edit_cannot_save_with_empty_phone(self, phone_empty):
    #     """
    #     Step by Step:
    #         1. Login account
    #         2. Choose select check box at first
    #         3. Click Edit button
    #         4. Enter Phone with " "
    #         5. Verify the Phone textbox display red border color and message "Please enter a valid phone number"
    #     """
    #     self.logger.info("===== Verify edit can not save with empty phone =====")
    #     edit = MyReportPage(self.driver)
    #     try:
    #         self.driver.refresh()
    #         edit.select_check_box()
    #         self.logger.info("Choose select checkbox report")
    #         edit.click_edit_button()
    #         self.logger.info("Click edit button")
    #         edit.enter_phone_textbox(phone_empty)
    #         self.logger.info("Enter empty value in phone textbox")
    #         edit.click_save_button()
    #         self.logger.info("Click save button to display red border")
    #         assert edit.is_error_red_border(edit.phone) and edit.is_required_phone_error() == "Please enter a valid phone number"
    #         self.logger.passed("Text box display red border and message successfully")
    #     except Exception as e:
    #         self.logger.failed("Failed : Can save user information", e)
    #         self.driver.save_screenshot(".\\screenshots\\test_verify_edit_cannot_save_with_empty_phone.png")
    #
    #
    # @pytest.mark.parametrize("email_empty",[(user["email"])])
    # def test_verify_edit_cannot_save_with_empty_email(self, email_empty):
    #     """
    #     Step by Step:
    #         1. Login account
    #         2. Choose select check box at first
    #         3. Click Edit button
    #         4. Enter Email with " "
    #         5. Verify the Email textbox display red border color and message "Please enter a valid phone number"
    #     """
    #     self.logger.info("===== Verify edit can not save with empty email =====")
    #     edit = MyReportPage(self.driver)
    #     try:
    #         self.driver.refresh()
    #         edit.select_check_box()
    #         self.logger.info("Choose select checkbox report")
    #         edit.click_edit_button()
    #         self.logger.info("Click edit button")
    #         edit.enter_email_textbox(email_empty)
    #         self.logger.info("Enter empty value in email textbox")
    #         edit.click_save_button()
    #         self.logger.info("Click save button to display red border")
    #         assert edit.is_error_red_border(edit.edit_email) and edit.is_required_email_error() == "Please enter a valid email"
    #         self.logger.passed("Text box display red border and message successfully")
    #     except Exception as e:
    #         self.logger.failed("Failed : Can save user information", e)
    #         self.driver.save_screenshot(".\\screenshots\\test_verify_edit_cannot_save_with_empty_email.png")


    # Edit with invalid emails
    # @pytest.mark.parametrize("email_invalid",[(user["invalid_email"])])
    # def test_verify_edit_cannot_save_with_invalid_email(self, email_invalid):
    #     """
    #     Step by Step:
    #         1. Login account
    #         2. Choose select check box at first
    #         3. Click Edit button
    #         4. Enter invalid Email
    #         5. Verify the Email textbox display red border color and message "Please enter a valid email"
    #     """
    #     self.logger.info("===== Verify edit can not save with invalid email =====")
    #     edit = MyReportPage(self.driver)
    #     try:
    #         self.driver.refresh()
    #         edit.select_check_box()
    #         self.logger.info("Choose select checkbox report")
    #         edit.click_edit_button()
    #         self.logger.info("Click edit button")
    #         for i in email_invalid:
    #             edit.enter_email_textbox(i)
    #             #edit.click_save_button()
    #             assert edit.is_error_red_border(edit.edit_email)
    #             assert edit.is_required_email_error() == "Please enter a valid email"
    #             time.sleep(1)
    #     except Exception as e:
    #         self.logger.failed("Failed : Can save user information", e)
    #         self.driver.save_screenshot(".\\screenshots\\test_verify_edit_cannot_save_with_invalid_email.png")


    # Share feature : email, copy link
    def test_verify_can_copy_link(self):
        """
        Step by Step:
            1. Login account
            2. Choose select check box at first row
            3. Click Share button
            4. Click Copy Link
            5. Verify the button change to "Link Copied" status
        """
        self.logger.info("===== Verify can copy link =====")
        share = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            share.select_check_box()
            self.logger.info("Choose select checkbox report")
            share.click_share_button()
            self.logger.info("Click share button")
            share.click_copy_link()
            self.logger.info("Click copy link button")
            time.sleep(3)
            assert share.get_copied_link() == "Link Copied!", "Button not change to Link Copied!"
            self.logger.passed("The button changed to Link Copied!")
        except Exception as e:
            self.logger.failed("Failed : Button not change to Link Copied!", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_can_copy_link.png")

    @pytest.mark.parametrize("email", [("thang.huynh@vn.innova.com")])
    def test_verify_can_be_share_report_with_email(self, email):
        """
        Step by Step:
            1. Login account
            2. Choose select check box at first row
            3. Click Share button
            4. Enter email
            5. Click email suggested
            6. Verify the email textbox can share with auto suggest email
        """
        self.logger.info("===== Verify can be auto suggest email =====")
        share = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            share.select_check_box()
            self.logger.info("Choose select checkbox report")
            share.click_share_button()
            self.logger.info("Click share button")
            share.enter_share_email_textbox(email)
            self.logger.info("Enter email")
            share.click_send_share()
            self.logger.info("Click share button")
            assert share.is_share_popup_closed() == True
        except Exception as e:
            self.logger.failed("The email textbox does not auto-suggest email", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_can_be_share_report_with_email.png")

    @pytest.mark.parametrize("email, expected", [("thang", "thang.huynh@vn.innova.com")])
    def test_verify_can_be_auto_suggest_email(self, email, expected):
        """
        Step by Step:
            1. Login account
            2. Choose select check box at first row
            3. Click Share button
            4. Enter email
            5. Click email suggested
            6. Verify the email textbox can share with auto suggest email
        """
        self.logger.info("===== Verify can be auto suggest email =====")
        share = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            share.select_check_box()
            self.logger.info("Choose select checkbox report")
            share.click_share_button()
            self.logger.info("Click share button")
            share.enter_share_email_textbox(email)
            self.logger.info("Enter email textbox")
            share.select_suggested_email(expected)
            self.logger.info("Click email suggested")
            assert share.verify_email_select_displayed(expected)
        except Exception as e:
            self.logger.failed("The email textbox does not auto-suggest email", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_can_be_auto_suggest_email.png")


    def test_verify_invalid_email_with_error_message(self):
        """
        Step by Step:
            1. Login account
            2. Choose select check box at first row
            3. Click Share button
            4. Enter invalid email textbox
            5. Verify the email textbox display error message
        """
        self.logger.info("===== Verify invalid email error message =====")
        share = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            share.select_check_box()
            self.logger.info("Choose select checkbox report")
            share.click_share_button()
            self.logger.info("Click share button")
            share.enter_share_email_textbox("abcde")
            self.logger.info("Enter invalid email textbox")
            assert share.get_email_error_message() == "Please enter a valid email"
        except Exception as e:
            self.logger.failed("The email textbox does not display error message", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_invalid_email_with_error_message.png")


    # Delete button : click keep it, modal close, confirm
    def test_verify_can_keep_it_report(self):
        """
        Step by Step:
            1. Login account
            2. Choose select check box at first row
            3. Click Delete button
            4. Click Keep it button
            5. Verify that the report at first row still remains
        """
        self.logger.info("===== Verify can keep it report =====")
        delete = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            report_before = delete.get_report_vehicle()
            delete.select_check_box()
            self.logger.info("Choose select checkbox report")
            delete.click_delete_button()
            self.logger.info("Click delete button")
            delete.click_keep_button()
            self.logger.info("Click keep button")
            report_after = delete.get_report_vehicle()
            assert report_before == report_after, "The report was deleted after clicking keep button"
            self.logger.passed("Click keep it button and close button")
        except Exception as e:
            self.logger.failed("Failed : Click keep it button and can not close", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_can_keep_it_report.png")


    def test_verify_clear_search_restores_full_list(self):
        """
        Step by step:
            1. Login account
            2. Enter a search keyword
            3. Clear the search field
            4. Verify the full report list is restored (more than 1 row)
        """
        self.logger.info("===== Verify Clear Search Restores Full List =====")
        search_page = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            search_page.enter_search("TOYOTA")
            self.logger.info("Enter search keyword TOYOTA")
            search_page.enter_search("")
            self.logger.info("Clear the search field")
            row_count = search_page.get_report_row_count()
            self.logger.info(f"Row count after clearing: {row_count}")
            assert row_count > 1, f"Expected more than 1 row after clearing search, got {row_count}"
            self.logger.passed("Full report list restored after clearing search")
        except Exception as e:
            self.logger.failed(f"Clear search did not restore full list: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_clear_search_restores_full_list.png")
            assert False

    def test_verify_combined_type_and_tool_filter(self):
        """
        Step by step:
            1. Login account
            2. Click Filter button
            3. Click OBD II type
            4. Click 7111 tool
            5. Verify all rows show Type = OBD II and Tool = 7111
        """
        self.logger.info("===== Verify Combined Type and Tool Filter =====")
        filter_page = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            time.sleep(3)
            filter_page.filter_click()
            self.logger.info("Click filter button")
            filter_page.click_type_obd2()
            self.logger.info("Select OBD II type")
            time.sleep(3)
            filter_page.click_tool_7111()
            self.logger.info("Select 7111 tool")
            time.sleep(3)
            filter_page.get_contains_type_values("OBD II")
            self.logger.info("All rows contain OBD II type")
            filter_page.get_contains_tool_values("7111")
            self.logger.info("All rows contain 7111 tool")
            self.logger.passed("Combined OBD II + 7111 filter returns correct results")
        except Exception as e:
            self.logger.failed(f"Combined filter did not return expected results: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_combined_type_and_tool_filter.png")
            assert False

    def test_verify_delete_button_visible_only_after_checkbox_selection(self):
        """
        Step by step:
            1. Login account
            2. Verify Delete button is not visible without checkbox
            3. Select first checkbox
            4. Verify Delete button is now visible
        """
        self.logger.info("===== Verify Delete Button Visible Only After Checkbox Selection =====")
        delete = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            assert not delete.is_delete_button_displayed(), "Delete button should not be visible without selection"
            self.logger.info("Delete button is not visible without checkbox selection")
            delete.select_check_box()
            self.logger.info("Select first checkbox")
            assert delete.is_delete_button_displayed(), "Delete button should be visible after selection"
            self.logger.passed("Delete button appears only after checkbox selection")
        except Exception as e:
            self.logger.failed(f"Delete button visibility check failed: {e}")
            self.driver.save_screenshot(".\\screenshots\\test_verify_delete_button_visible_after_selection.png")
            assert False

    def test_verify_can_click_modal_close(self):
        """
        Step by Step:
            1. Login account
            2. Choose select check box at first row
            3. Click Delete button
            4. Click modal close icon button
            5. Verify that the report at first row still remains
        """
        self.logger.info("===== Verify can click modal close =====")
        delete = MyReportPage(self.driver)
        try:
            self.driver.refresh()
            report_before = delete.get_report_vehicle()
            delete.select_check_box()
            self.logger.info("Choose select checkbox report")
            delete.click_delete_button()
            self.logger.info("Click delete button")
            delete.click_modal_close()
            self.logger.info("Click modal close icon button")
            report_after = delete.get_report_vehicle()
            assert report_before == report_after, "The report was deleted after clicking modal close"
        except Exception as e:
            self.logger.failed("Failed : Click modal close button", e)
            self.driver.save_screenshot(".\\screenshots\\test_verify_can_click_modal_close.png")

    # def test_verify_can_delete_report(self):
    #     self.logger.info("===== Verify can delete report =====")
    #     delete = MyReportPage(self.driver)
    #     try:
    #         report_before = delete.get_first_report()
    #         delete.select_check_box()
    #         self.logger.info("Choose select checkbox report")
    #         delete.click_delete_button()
    #         self.logger.info("Click delete button")
    #         delete.click_confirm_yes_button()
    #         self.logger.info("Click confirm button")
    #         report_after = delete.get_rows_reports()
    #         assert report_before not in report_after, "The report was not deleted after clicking confirm button"
    #     except Exception as e:
    #         self.logger.failed("Failed : Click modal close button", e)
    #         self.driver.save_screenshot(".\\screenshots\\test_verify_can_click_modal_close.png")




