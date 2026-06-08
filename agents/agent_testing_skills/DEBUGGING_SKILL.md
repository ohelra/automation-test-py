# Debugging Skill — RSPRO QA Automation Test Infrastructure

## Three Layers of Debug Information

| Source | Location | Use when |
|---|---|---|
| Execution log | `logs/RSPROwebsite.log` | Tracing test flow, finding exact failure point |
| Screenshots | `screenshots/` | Inspecting UI at moment of failure |
| Allure / HTML Report | `allure-report/` or `http://SERVER_IP:8000` | Trends, pass rates, flaky history |

---

## Reading the Log File

```bash
# View full log
cat logs/RSPROwebsite.log

# Watch in real time while tests run
tail -f logs/RSPROwebsite.log

# Filter errors only
grep -i "FAIL\|ERROR" logs/RSPROwebsite.log

# Filter by test class or keyword
grep "TestMyReport" logs/RSPROwebsite.log
```

**Log format (from LogMaker):**
```
15/01/2024 10:23:45: INFO: ===== Verify Search valid vehicle report =====
15/01/2024 10:23:46: INFO: Testing keyword : RAM
15/01/2024 10:23:47: INFO: PASS: The table contains vehicles RAM
15/01/2024 10:23:50: ERROR: FAIL: Failed dont match keyword 'FORD': NoSuchElementException(...)
```

**Log levels in this project:**
- `self.logger.info(msg)` → `INFO: msg`
- `self.logger.passed(msg)` → `INFO: PASS: msg`
- `self.logger.failed(f"msg: {e}")` → `ERROR: FAIL: msg: <exception>`

> **Remember**: `logger.failed()` takes ONE string. Embed the exception with f-string: `f"Failed: {e}"`

---

## Analyzing Screenshots

Screenshots are saved to `screenshots/` on test failure — both by the test's own `try/except` and automatically by `conftest.py`'s `pytest_runtest_makereport` hook.

```bash
# View most recent screenshots
ls -lt screenshots/ | head -10
```

**What to look for:**

| What you see in screenshot | What it means |
|---|---|
| Loading spinner still visible | Element not yet ready — need to increase/add wait |
| Error popup / modal | Server-side error or validation triggered unexpectedly |
| Wrong page / login page | Session expired or navigation failed |
| Empty table / no rows | Data not loaded — wait for rows before asserting |
| Partially rendered page | Timing issue — add wait after action |

---

## Common Selenium Exceptions & Fixes

### `NoSuchElementException`
```
Cause:  Locator is wrong, or element hasn't loaded yet
Fix:
  1. Inspect in DevTools (F12 → Inspector) and verify selector
  2. Switch from driver.find_element() to:
     self.wait.wait_for_element_visible(*self.locator)
  3. If element is inside iframe: driver.switch_to.frame() first
```

### `ElementNotInteractableException`
```
Cause:  Element is hidden, covered, or disabled
Fix:
  1. Use wait_for_element_visible() — ensures element is interactable
  2. Use self.scroll_to(locator) or self.specific_scroll_to(locator) first
  3. Add brief time.sleep(1) only if animation/transition is the cause
```

### `StaleElementReferenceException`
```
Cause:  DOM re-rendered after reference was captured
Fix:    Re-find element after any navigation or DOM change
        Call self.wait.wait_for_element_visible(*locator) again
```

### `TimeoutException` (from WaitHelper)
```
Cause:  Element didn't appear within wait timeout
Fix:
  1. Verify the locator is correct in DevTools
  2. Check screenshot — did the page load at all?
  3. Increase timeout constant in waitHelper.py
```

### `AssertionError` in `get_contains_*_values()`
```
Cause:  A table cell doesn't contain the expected keyword
        (the verify method asserts inside Page Object)
Fix:
  1. Check if UI is filtering correctly — maybe search didn't trigger
  2. Add self.driver.refresh() before the search in the test
  3. Check if time.sleep() after enter_search() is sufficient
```

---

## Debug Workflow

```
1. Read the FAIL log line — what exception + what keyword/value caused it?
2. Open the screenshot from that test
3. Re-run that single test with -s flag to see real-time output:
   pytest test_cases/tests/My_Report_Tests/My_Report_test.py::TestMyReport::test_verify_search_report_by_vehicle[RAM] -v -s
4. Verify the locator in DevTools — has the website changed?
5. Check JSON data file — is the test value what you expect?
6. If it fails only sometimes → likely a timing/flaky issue (see below)
```

---

## Flaky Tests — Detection and Fix

A flaky test passes and fails inconsistently without code changes.

**Common causes in this project:**

| Cause | Fix |
|---|---|
| `time.sleep(3)` not long enough after search | Increase duration or replace with explicit wait on result element |
| Previous parametrize iteration's state bleeds in | Add `self.driver.refresh()` before action |
| Race condition on table rendering | Wait for a specific row to appear before `find_elements` |
| Session expired mid-run | Check session timeout on the server |

**Upgrade from `time.sleep()` to explicit wait:**
```python
# Current pattern in project (acceptable but fragile):
search.send_keys(keyword)
time.sleep(3)
vehicles = self.driver.find_elements(*self.get_vehicle_values)

# More robust — wait for first result row to appear:
search.send_keys(keyword)
self.wait.wait_for_element_visible(*self.get_vehicle_values)
vehicles = self.driver.find_elements(*self.get_vehicle_values)
```

---

## Useful Pytest Commands

```bash
# Run a specific test method
pytest "test_cases/tests/My_Report_Tests/My_Report_test.py::TestMyReport::test_verify_search_report_by_vehicle[RAM]" -v -s

# Run a full test file
pytest test_cases/tests/My_Report_Tests/My_Report_test.py -v

# Run a full section folder
pytest test_cases/tests/My_Report_Tests/ -v

# Run by marker
pytest -m MyReport -v

# Run all tests
pytest test_cases/tests/ -v

# Stop on first failure
pytest test_cases/tests/ -x -v

# Run with specific browser
pytest test_cases/tests/ --browser=chrome -v
```
