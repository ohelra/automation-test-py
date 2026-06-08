# Project: qa-automation-test-rspro-website
### Description: 
##### Master skill for the RSPRO website QA Automation Test project. Activate whenever the user wants to: create a new Page Object, write a new test script, read/analyze logs or test results, maintain the CI/CD pipeline, add test data, or perform any task related to the Selenium + Pytest + Allure framework in this project.
##### Always use this skill when base_pages, test_cases, conftest, Page Object Model, POM, Allure Report, waitHelper, JsonReader, LogMaker, or any folder/file from the qa-automation-test-rspro-website project structure is mentioned.

---

# QA Automation RSPRO — Master Skill

## Project Stack

| Component | Technology | Notes |
|---|---|---|
| Language | Python 3.11 | |
| Browser Driver | Selenium WebDriver + `undetected_chromedriver` | Headless Chrome by default |
| Test Runner | Pytest | Fixtures via `conftest.py` |
| Design Pattern | Page Object Model (POM) | Layered inheritance (see below) |
| Reporting | Allure Report + pytest-html | Trend data pulled from server |
| Config | `configurations/config.ini` | Read via `read_properties.py` |
| Logging | `custom_logger.py` → `LogMaker` | Output → `logs/RSPROwebsite.log` |
| Wait Strategy | `utilities/waitHelper.py` → `WaitHelper` | Explicit Wait via `wait_for_element_visible` / `wait_for_element_present` |
| JSON Reader | `utilities/json_reader.py` → `JsonReader` | All JSON test data access |

---

## Inheritance Chain (CRITICAL)

```
BasePage                          ← base_pages/pages/base_page.py
    └── RSPROHomePage             ← base_pages/pages/HomePage_Pages/RSPRO_Homepage.py
            └── <FeaturePage>    ← base_pages/pages/<Section>_Pages/<Feature>_page.py
```

**Rule**: Feature Page Objects inherit from `RSPROHomePage` (which itself inherits `BasePage`),
**not** directly from `BasePage`. This gives every page access to login, navigation, and home page methods.

```python
# CORRECT
class MyReportPage(RSPROHomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitHelper(driver)

# WRONG — do not do this
class MyReportPage(BasePage): ...
```

---

## Directory Structure

```
qa-automation-test-rspro-website/
├── base_pages/pages/
│   ├── HomePage_Pages/
│   │   └── RSPRO_Homepage.py      ← Login, navigation — parent of all feature pages
│   ├── My_Report_Pages/
│   │   └── My_Report_page.py      ← Inherits RSPROHomePage
│   ├── Auth_Pages/
│   ├── Products_Pages/
│   ├── Support_Pages/
│   ├── Technical_Center_Pages/
│   └── base_page.py               ← Root base class
│
├── test_cases/tests/              ← Mirrors base_pages structure
│   ├── My_Report_Tests/
│   │   └── My_Report_test.py
│   ├── conftest.py                ← `setup` fixture (scope="class")
│   └── ...
│
├── test_data/                     ← JSON + Excel only, no hardcoded data
├── utilities/
│   ├── custom_logger.py           ← LogMaker
│   ├── json_reader.py             ← JsonReader
│   ├── waitHelper.py              ← WaitHelper
│   └── read_properties.py         ← ReadConfig
└── configurations/config.ini
```

---

## Core Conventions (ALWAYS FOLLOW)

### 1. Naming Convention

| Artifact | Pattern | Example |
|---|---|---|
| Page Object file | `{FeatureName}_page.py` | `My_Report_page.py` |
| Test file | `{FeatureName}_test.py` | `My_Report_test.py` |
| Test function | `test_<what_is_being_tested>` | `test_verify_search_report_by_vehicle` |
| Locator variables | `snake_case` at class level | `search_box = (By.ID, "new-report-search-input")` |
| Page Object class | `{FeatureName}Page` | `MyReportPage` |
| Test class | `Test{FeatureName}` | `TestMyReport` |

> **Note on locator style**: The real codebase uses `snake_case` for locator constants
> (e.g., `search_box`, `filter`, `date_from`), not `UPPER_SNAKE_CASE`. Follow the existing style.

### 2. Directory Symmetry Rule

```
base_pages/pages/My_Report_Pages/   ↔   test_cases/tests/My_Report_Tests/
```

### 3. Inheritance Rule

- Feature Page Objects inherit from **`RSPROHomePage`**, not `BasePage` directly
- Never call `driver.find_element()` in test files — go through Page Object methods

### 4. Data Separation Rule

- No hardcoded test data in test files or page objects
- All data in `test_data/` as `.json` or `.xlsx`
- Access via `JsonReader("filename.json")`

### 5. Wait Strategy Rule

- Use `self.wait.wait_for_element_visible(*locator)` or `self.wait.wait_for_element_present(*locator)`, etc in `utilities\waitHelpper.py` methods that are appropriate for that element
- Avoid `time.sleep()` where possible — use it only as a last resort for unavoidable UI delays
- Never use `driver.implicitly_wait()` inside Page Objects (it's set once in `conftest.py`)

### 6. Assertion Rule

- No `assert` inside Page Objects (except `navigate_new_tab` in BasePage which is a special helper)
- Assertions belong in test scripts inside `try/except` blocks

### 7. Logger Rule

```python
# logger.failed() takes ONE string argument only
self.logger.failed(f"Failed: description of the error")   # CORRECT
self.logger.failed("message", e)                          # WRONG — will raise TypeError

self.logger.passed("Description of what passed")          # CORRECT
self.logger.info("Step description")                      # CORRECT
```

---

## Canonical Patterns (from real source)

### Page Object Pattern

```python
from selenium.webdriver.common.by import By
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from utilities.waitHelper import WaitHelper

class <FeatureName>Page(RSPROHomePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitHelper(driver)

    # Locators — snake_case, class-level tuples
    search_box     = (By.ID, "element-id")
    result_rows    = (By.XPATH, "//table/tbody/tr")
    submit_button  = (By.CSS_SELECTOR, "button[type='submit']")

    # Action methods — use self.wait, never driver.find_element directly in tests
    def enter_search(self, keyword):
        field = self.wait.wait_for_element_visible(*self.search_box)
        field.clear()
        field.send_keys(keyword)

    def get_result_texts(self):
        rows = self.driver.find_elements(*self.result_rows)
        return [r.text.strip() for r in rows]
```

### Test Script Pattern

```python
import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.<Section>_Pages.<Feature>_page import <Feature>Page
from utilities.custom_logger import LogMaker
from utilities.json_reader import JsonReader

@pytest.mark.<FeatureName>
class Test<FeatureName>:

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        request.testdata = JsonReader("<feature>.json")
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()
        self.home_page.click_my_account()
        self.home_page.perform_login()

    # Data-driven test
    @pytest.mark.parametrize("item", item_data := JsonReader("<feature>.json").get_data("<key>")["<field>"])
    def test_verify_<scenario>(self, item):
        """
        Step by step:
            1. <Step 1>
            2. <Step 2>
        Expected: <Expected result>
        """
        self.logger.info("===== <Test description> =====")
        page = <Feature>Page(self.driver)
        try:
            self.logger.info(f"Testing with: {item}")
            page.<action_method>(item)
            page.<verify_method>(item)
            self.logger.passed(f"<Description> passed for: {item}")
        except Exception as e:
            self.logger.failed(f"Failed for '{item}': {e}")
            self.driver.save_screenshot(f".\\screenshots\\test_<name>_{item}.png")
            assert False
```

---

## When to Read Which Reference File

| Task | Read |
|---|---|
| New Jira ticket (bug / task / story) | [→ agents/agent_testing_skills/TICKET_WORKFLOW_SKILL.md](agents/agent_testing_skills/TICKET_WORKFLOW_SKILL.md) |
| Create a new Page Object | [→ agents/agent_testing_skills/POM_SKILL.md](agents/agent_testing_skills/POM_SKILL.md) |
| Write a new Test Script | [→ agents/agent_testing_skills/TEST_SCRIPT_SKILL.md](agents/agent_testing_skills/TEST_SCRIPT_SKILL.md) |
| Add or manage test data | [→ agents/agent_testing_skills/TEST_DATA_SKILL.md](agents/agent_testing_skills/TEST_DATA_SKILL.md) |
| Analyze logs or failing tests | [→ agents/agent_testing_skills/DEBUGGING_SKILL.md](agents/agent_testing_skills/DEBUGGING_SKILL.md) |

---

## Quick Decision Tree

```
What does the user need?
│
├─ New Jira ticket (bug / task / story / improvement)
│   → Read TICKET_WORKFLOW_SKILL.md
│   → Phase 1: Read ticket + inspect live page
│   → Phase 2: Write manual TCs in Manual_Tests/<Module>/
│   → Phase 3: Write automation (Page Object + Test Script)
│
├─ "Create a page / page object for feature X"
│   → Read POM_SKILL.md
│
├─ "Write a test for feature X"
│   → Read TEST_SCRIPT_SKILL.md
│
├─ "Add / update test data"
│   → Read TEST_DATA_SKILL.md
│
└─ "Test failing" / "Debug" / "Read log"
    → Read DEBUGGING_SKILL.md
```