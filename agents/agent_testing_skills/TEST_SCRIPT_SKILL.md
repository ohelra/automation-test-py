# Test Script Skill — RSPRO QA Automation Test Infrastructure

## Structure of a Test Script

Each test in `test_cases/tests/<Section>_Tests/<FeatureName>_test.py` follows this structure:

1. **`class_setup` fixture** — runs once per class, handles login + navigation
2. **`test_` methods** — one per scenario, wrapped in `try/except`
3. **Logging** — `logger.info()` for steps, `logger.passed()` on success, `logger.failed()` on failure
4. **Screenshot** — saved to `screenshots/` on failure
5. **`assert False`** — at end of `except` block to mark test as FAILED in Pytest

---

## Full Template

```python
# test_cases/tests/<Section>_Tests/<FeatureName>_test.py

import pytest
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from base_pages.pages.<Section>_Pages.<FeatureName>_page import <FeatureName>Page
from utilities.custom_logger import LogMaker
from utilities.json_reader import JsonReader


@pytest.mark.<FeatureName>
class Test<FeatureName>:

    # ── Class-level Setup ─────────────────────────────────────────────────────
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self, request, setup):
        driver = setup
        request.cls.logger = LogMaker.log_gen()
        request.testdata = JsonReader("<feature>.json")
        self.home_page = RSPROHomePage(driver)
        self.home_page.go_to_home()
        self.home_page.click_my_account()
        self.home_page.perform_login()

    # ── Simple Test ───────────────────────────────────────────────────────────
    def test_verify_<scenario>(self):
        """
        Step by step:
            1. <Step 1>
            2. <Step 2>
        Expected: <Expected outcome>
        """
        self.logger.info("===== <Test description> =====")
        page = <FeatureName>Page(self.driver)
        try:
            page.<action_method>()
            page.<verify_method>()
            self.logger.passed("<Description of what passed>")
        except Exception as e:
            self.logger.failed(f"<Description of what failed>: {e}")
            self.driver.save_screenshot(f".\\screenshots\\test_<name>.png")
            assert False

    # ── Data-Driven Test (parametrize) ────────────────────────────────────────
    @pytest.mark.parametrize("item", item_data := JsonReader("<feature>.json").get_data("<key>")["<field>"])
    def test_verify_<scenario>_by_<dimension>(self, item):
        """
        Step by step:
            1. <Step 1 with item>
            2. <Step 2>
        Expected: <column> matches keyword for all rows
        """
        self.logger.info("===== <Test description> =====")
        <Feature_name>_page = <FeatureName>Page(self.driver)
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

## The `setup` Fixture (conftest.py)

Defined in `conftest.py` with `scope="class"` — shared WebDriver for all tests in a class.

```python
@pytest.fixture(scope="class", autouse=True)
def class_setup(self, request, setup):    # 'setup' is injected from conftest.py
    driver = setup                        # This IS the WebDriver instance
    request.cls.logger = LogMaker.log_gen()
    # After this fixture: self.driver is available (set by conftest via request.cls.driver)
```

**What conftest.py does automatically:**
- Launches Chrome headless (`--headless=new`, 1920×1080)
- Sets `request.cls.driver = driver` → makes `self.driver` available in all test methods
- Captures screenshot and attaches to pytest-html report on failure
- Calls `driver.quit()` after all tests in the class finish

---

## LogMaker — Correct Usage

```python
# Initialize once in class_setup
request.cls.logger = LogMaker.log_gen()

# In test methods:
self.logger.info("Step description or context")
self.logger.passed("Description of what passed")   # Logs as INFO with PASS: prefix
self.logger.failed(f"Failure description: {e}")    # Logs as ERROR with FAIL: prefix

# CRITICAL: logger.failed() accepts ONE string only
self.logger.failed(f"Failed for '{item}': {e}")    # CORRECT — embed exception in f-string
self.logger.failed("message", e)                   # WRONG — TypeError, second arg not supported
```

---

## JsonReader — Correct Usage

```python
from utilities.json_reader import JsonReader

# Load at module level for @pytest.mark.parametrize (outside class)
vehicles_data = JsonReader("my_reports.json").get_data("search_vehicle")["vehicles"]

# Load inside fixture for general data access
request.testdata = JsonReader("my_reports.json")

# Parametrize with walrus operator (project style)
@pytest.mark.parametrize("vehicle", vehicles_data := JsonReader("my_reports.json").get_data("search_vehicle")["vehicles"])
def test_verify_search_report_by_vehicle(self, vehicle):
    ...
```

---

## Screenshot Convention

```python
# Pattern: descriptive name with the variable that caused failure
self.driver.save_screenshot(f".\\screenshots\\test_verify_search_type_{vehicle}.png")
self.driver.save_screenshot(f".\\screenshots\\test_verify_search_report_by_id.png")

# conftest.py also auto-saves a screenshot named after the test function
# So manual screenshots in try/except are supplemental/more specific
```

---

## Refresh Strategy

Some tests need `self.driver.refresh()` between parametrize iterations to reset UI state:

```python
# Add refresh when previous search/filter state bleeds into next iteration
self.driver.refresh()
self.logger.info(f"Testing keyword: {report_type}")
page.enter_search(report_type)
```

Use judgment — not every parametrized test needs it. Check if state from previous iteration affects the current one.

---

## Checklist — Creating a New Test Script

- [ ] File in correct folder: `test_cases/tests/<Section>_Tests/<FeatureName>_test.py`
- [ ] File named: `<FeatureName>_test.py`
- [ ] Class named: `Test<FeatureName>` with `@pytest.mark.<FeatureName>`
- [ ] `class_setup` has `scope="class"` and `autouse=True`
- [ ] `request.cls.logger = LogMaker.log_gen()` assigned in `class_setup`
- [ ] Login flow in `class_setup`: `go_to_home()` → `click_my_account()` → `perform_login()`
- [ ] All test data loaded via `JsonReader(...)`, no hardcoded values
- [ ] Parametrize data loaded at module level (outside class) using walrus `:=` operator
- [ ] Every `test_` function has a docstring with steps and expected result
- [ ] All test logic inside `try/except Exception as e`
- [ ] `self.logger.failed(f"... {e}")` — exception embedded in f-string (NOT second arg)
- [ ] `assert False` at end of `except` block
- [ ] Screenshot filename is descriptive and includes the variable/scenario
- [ ] `self.driver.refresh()` added where UI state could persist between parametrize iterations
- [ ] `__init__.py` updated in the folder if needed

---

## Real Example Reference

```
test_cases/tests/My_Report_Tests/My_Report_test.py
```

Three canonical patterns from this file:
1. `test_verify_search_report_by_vehicle` — parametrize + action + collection verify
2. `test_verify_search_report_by_id` — same pattern, no refresh needed
3. `test_verify_search_report_by_types` — same pattern, **with** `self.driver.refresh()` before each iteration
