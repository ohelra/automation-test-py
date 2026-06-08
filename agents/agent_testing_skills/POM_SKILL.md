# Page Object Model Skill — RSPRO QA Automation Test Infrastructure

## What is a Page Object?

A Page Object represents one screen / one section of the website. It contains:
- **Locators** — element selectors as class-level tuples
- **Action methods** — interact with the UI (click, type, select, ...)
- **Getter / verify methods** — read values or state for assertions in test scripts
- **NO `assert` statements** — assertions belong only in test scripts

---

## Inheritance Chain

```
BasePage  →  RSPROHomePage  →  <FeatureName>Page
```

All feature Page Objects **must inherit from `RSPROHomePage`**, not `BasePage` directly.
`RSPROHomePage` provides login, navigation, and home page methods that most pages need.

---

## Standard Template

```python
# base_pages/pages/<Section>_Pages/<FeatureName>_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from base_pages.pages.HomePage_Pages.RSPRO_Homepage import RSPROHomePage
from utilities.waitHelper import WaitHelper


class <FeatureName>Page(RSPROHomePage):
    """Page Object for the <screen/section name>."""

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitHelper(driver)      # Always re-init WaitHelper explicitly

    # ── Locators ──────────────────────────────────────────────────────────────
    # snake_case, class-level tuples — (By.STRATEGY, "selector")
    # Group by UI area: search, filter, table, form, modal, buttons, ...

    search_box        = (By.ID, "feature-search-input")
    result_rows       = (By.XPATH, "//table/tbody/tr/td[2]/span")
    submit_button     = (By.CSS_SELECTOR, "button[type='submit']")
    msg_not_found     = (By.XPATH, "//*[normalize-space(text())='No results found.']")
    modal_close       = (By.XPATH, "//div[@id='modal-x']/div/div/div[1]/button")

    # ── Action Methods ────────────────────────────────────────────────────────
    # One method = one user action
    # Use self.wait.wait_for_element_visible(*locator) before interacting

    def enter_search(self, keyword):
        """Type a keyword into the search field."""
        field = self.wait.wait_for_element_visible(*self.search_box)
        field.clear()
        field.send_keys(keyword)

    def click_submit(self):
        """Click the submit/apply button."""
        self.wait.wait_for_element_visible(*self.submit_button).click()

    def enter_field_and_tab(self, locator, value):
        """Clear a field, type a value, then press TAB (e.g. for validation triggers)."""
        field = self.wait.wait_for_element_visible(*locator)
        field.clear()
        field.send_keys(value)
        field.send_keys(Keys.TAB)

    # ── Getter / Verify Methods ───────────────────────────────────────────────
    # Return values or booleans — used for assertions in test scripts
    # Assertion logic stays in the TEST, not here

    def get_result_texts(self):
        """Return list of text values from result rows."""
        rows = self.driver.find_elements(*self.result_rows)
        return [r.text.strip() for r in rows]

    def get_not_found_text(self):
        """Return the 'no results' message text."""
        return self.driver.find_element(*self.msg_not_found).text

    def is_modal_closed(self):
        """Return True if the modal/popup is no longer visible."""
        try:
            self.wait.wait_for_element_visible(*self.modal_close)
            return True
        except:
            return False

    # ── Verify-and-assert helpers (used inside Page Object only) ─────────────
    # Only when you need to iterate/validate a collection of elements
    # These ARE allowed to contain assert — they are called from test try/except blocks

    def get_contains_<column>_values(self, keyword):
        """Assert every row in the <column> column contains the keyword."""
        rows = self.driver.find_elements(*self.result_rows)
        for row in rows:
            text = row.text.lower()
            assert keyword.lower() in text, f"Expected '{keyword}' in '{text}'"
```

---

## BasePage Methods Available

These come from `base_page.py` — use them inside Page Objects:

| Method | What it does |
|---|---|
| `self.find(locator)` | Wait for element present, return element |
| `self.hover(locator)` | Move mouse over element (visible wait) |
| `self.hover_element_present(locator)` | Move mouse over element (present wait) |
| `self.scroll_to(locator)` | Scroll until element is visible |
| `self.specific_scroll_to(locator)` | Scroll element to center of viewport (smooth) |
| `self.get_attribute_element(locator, attr)` | Get an attribute value from an element |
| `self.wait_for_class_contains(locator, substr)` | Wait until element's class contains a substring |
| `self.navigate_new_tab(click_fn, url_part, text_fn, expected)` | Open a new tab, verify URL + text, close tab |
| `self.navigate_new_tab_with_url(click_fn, url_part)` | Open a new tab, verify URL only, close tab |
| `self.open(url)` | Navigate to a URL |

## WaitHelper Methods Available

`self.wait = WaitHelper(driver)` — call these directly on `self.wait`:

| Method | What it does |
|---|---|
| `self.wait.wait_for_element_visible(*locator)` | Wait until element is **visible**, return element |
| `self.wait.wait_for_element_present(*locator)` | Wait until element is in DOM (may not be visible) |

> **Always unpack the locator tuple with `*`**: `self.wait.wait_for_element_visible(*self.search_box)`

---

## Real Example Reference

```
base_pages/pages/My_Report_Pages/My_Report_page.py
```

Key patterns from this file to replicate:
- Locators grouped by feature area (Search Box, Filter, Checkbox, Share, Edit, Delete)
- `self.wait.wait_for_element_visible(*self.locator).click()` — chain directly
- `self.driver.find_elements(*self.locator)` — for collecting multiple rows
- `field.clear(); field.send_keys(value)` — standard input clearing pattern
- `Keys.TAB` sent after email inputs to trigger validation

---

## Section → Folder → Class → Parent Map

| Section | Folder | Class | Inherits |
|---|---|---|---|
| Home Page | `HomePage_Pages/` | `RSPROHomePage` | `BasePage` |
| My Report | `My_Report_Pages/` | `MyReportPage` | `RSPROHomePage` |
| Auth | `Auth_Pages/` | `AuthPage` | `RSPROHomePage` |
| Products | `Products_Pages/` | `ProductsPage` | `RSPROHomePage` |
| Support | `Support_Pages/` | `SupportPage` | `RSPROHomePage` |
| Technical Center | `Technical_Center_Pages/` | `TechnicalCenterPage` | `RSPROHomePage` |

---

## Checklist — Creating a New Page Object

- [ ] File in correct folder: `base_pages/pages/<Section>_Pages/<FeatureName>_page.py`
- [ ] Class inherits `RSPROHomePage` (not `BasePage`)
- [ ] `__init__` calls `super().__init__(driver)` and `self.wait = WaitHelper(driver)`
- [ ] All locators are class-level `snake_case` tuples
- [ ] `self.wait.wait_for_element_visible(*self.locator)` used before interactions
- [ ] Locator tuple unpacked with `*` when passed to WaitHelper
- [ ] No `import time` unless absolutely necessary for UI delay (use sparingly)
- [ ] No `assert` in action or getter methods (only in collection-verify helpers)
- [ ] No hardcoded test data — methods accept parameters
- [ ] `__init__.py` updated in the folder if needed
- [ ] Corresponding test folder exists: `test_cases/tests/<Section>_Tests/`