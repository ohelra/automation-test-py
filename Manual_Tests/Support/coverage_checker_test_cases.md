# Manual Test Cases — Support: Coverage Checker

**Module:** Support
**Feature:** Coverage Checker
**Ticket:** RWR-589
**Epic:** EPIC 4 — Support (extended: Coverage Checker)
**Priority:** P1 — High
**Environment:** https://pro.repairsolutions.com/Support/CoverageChecker
**Precondition:** User is on any page of the RepairSolutionsPRO website. No login required.

---

## TC_001: Navigate to Coverage Checker via Support menu

**Description:** Verify that Coverage Checker is accessible from the Support dropdown menu.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Hover over "Support" in the top navigation bar | Support dropdown menu expands |
| 2 | Click "Coverage Checker" from the dropdown | Page navigates to /Support/CoverageChecker |
| 3 | Observe the page heading | Heading "Coverage Checker" is displayed |

**Priority:** P1
**Type:** Navigation

---

## TC_002: Verify page title and description text

**Description:** Verify that the Coverage Checker page displays the correct heading and descriptive subtitle.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to /Support/CoverageChecker | Page loads |
| 2 | Observe the main page heading | "Coverage Checker" is displayed |
| 3 | Observe the subtitle/description | Text reads "Identify which SDS tool functions will work on your vehicle." |

**Priority:** P1
**Type:** UI

---

## TC_003: Verify Tool Information dropdown contains all expected options

**Description:** Verify the Tool dropdown lists all three available diagnostic tools.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Click the "Tool Information" dropdown | Dropdown opens |
| 3 | Observe all options in the list | Options include: SDS43, SDS50, 7111 |

**Priority:** P1
**Type:** Functional

---

## TC_005: Verify Year dropdown range

**Description:** Verify the Year dropdown includes years from 1982 to the current year (2024+).

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Click the "Year" dropdown under Vehicle Information | Dropdown opens |
| 3 | Scroll to the top of the list | First option is 1982 (or older) |
| 4 | Scroll to the bottom of the list | Last option is 2024 or current year |

**Priority:** P2
**Type:** Functional

---

## TC_006: Submit form with valid data — 7111, 2024 BMW 8 Series

**Description:** Verify that submitting the form with valid complete data returns a coverage results section.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Select "7111" from the Tool Information dropdown | "7111" is displayed in the field |
| 3 | Select "2024" from the Year dropdown | "2024" is displayed in the field |
| 4 | Select "BMW" from the Make dropdown | "BMW" is displayed in the field |
| 5 | Select "8 Series" from the Model dropdown | "8 Series" is displayed in the field |
| 6 | Select "L6, 3.0L (B58C)" from the Engine dropdown | Engine is displayed in the field |
| 7 | Click "SUBMIT" | Results section appears on the page |
| 8 | Observe the results heading | "Availability & Special Functions Coverage" is displayed |

**Priority:** P1
**Type:** Functional

---

## TC_007: Verify results contain OBD II Diagnostics coverage section

**Description:** Verify that after a valid submission the OBD II Diagnostics section is visible in results.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Fill all fields: Tool=7111, Language=English, Year=2024, Make=BMW, Model=8 Series, Engine=L6, 3.0L (B58C) | All dropdowns filled |
| 3 | Click "SUBMIT" | Results appear |
| 4 | Observe the coverage sections | "OBD II Diagnostics" section is visible with coverage indicators |

**Priority:** P1
**Type:** Functional

---

## TC_008: Verify results contain OEM Diagnostics coverage section

**Description:** Verify that after a valid submission the OEM Diagnostics section is visible in results.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Fill all fields: Tool=7111, Language=English, Year=2024, Make=BMW, Model=8 Series, Engine=L6, 3.0L (B58C) | All dropdowns filled |
| 3 | Click "SUBMIT" | Results appear |
| 4 | Observe the coverage sections | "OEM Diagnostics" section is visible with coverage indicators |

**Priority:** P1
**Type:** Functional

---

## TC_009: Verify results contain Workshop Tools coverage section

**Description:** Verify that after a valid submission the Workshop Tools section is visible in results.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Fill all fields with valid data | All dropdowns filled |
| 3 | Click "SUBMIT" | Results appear |
| 4 | Observe the coverage sections | "Workshop Tools" section is visible with coverage indicators |

**Priority:** P2
**Type:** Functional

---

## TC_010: Submit with SDS43 tool — verify results appear

**Description:** Verify Coverage Checker returns results when SDS43 is selected as the tool.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Select "SDS43" from Tool Information | "SDS43" is displayed |
| 3 | Select "English", Year=2024, Make=BMW, Model=8 Series, Engine=L6, 3.0L (B58C) | All fields filled |
| 4 | Click "SUBMIT" | Results section appears |
| 5 | Verify results heading | "Availability & Special Functions Coverage" is displayed |

**Priority:** P2
**Type:** Functional

---

## TC_011: Submit with SDS50 tool — verify results appear

**Description:** Verify Coverage Checker returns results when SDS50 is selected as the tool.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Select "SDS50" from Tool Information | "SDS50" is displayed |
| 3 | Select "English", Year=2024, Make=BMW, Model=8 Series, Engine=L6, 3.0L (B58C) | All fields filled |
| 4 | Click "SUBMIT" | Results section appears |
| 5 | Verify results heading | "Availability & Special Functions Coverage" is displayed |

**Priority:** P2
**Type:** Functional

---

## TC_012: Vehicle dropdown cascade — Make populates after Year is selected

**Description:** Verify the Make dropdown becomes available (populated) only after Year is selected, confirming the cascading dropdown behavior.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Observe the Make dropdown before selecting Year | Make dropdown is empty or disabled |
| 3 | Select "2024" from the Year dropdown | Year is set |
| 4 | Click the Make dropdown | Make options are populated and selectable |

**Priority:** P2
**Type:** Functional

---

## TC_013: Vehicle dropdown cascade — Model populates after Make is selected

**Description:** Verify the Model dropdown is populated only after Make is selected.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Select Year=2024, Make=BMW | Year and Make are set |
| 3 | Click the Model dropdown | Model options specific to BMW 2024 are shown |
| 4 | Select "8 Series" | "8 Series" is displayed in the Model field |

**Priority:** P2
**Type:** Functional

---

## TC_014: Vehicle dropdown cascade — Engine populates after Model is selected

**Description:** Verify the Engine dropdown is populated only after Model is selected.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Select Year=2024, Make=BMW, Model=8 Series | All three fields set |
| 3 | Click the Engine dropdown | Engine options specific to 8 Series are shown |
| 4 | Select "L6, 3.0L (B58C)" | Engine is displayed in the field |

**Priority:** P2
**Type:** Functional

---

## TC_016: Submit without selecting Vehicle Year — form does not submit or shows empty

**Description:** Verify behavior when the SUBMIT button is clicked without selecting a Year (incomplete form).

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Select "7111" from Tool Information | Tool is set |
| 3 | Leave Vehicle Information fields empty | No year/make/model/engine selected |
| 4 | Click "SUBMIT" | Form does not submit OR results are empty / validation message shown |

**Priority:** P2
**Type:** Negative

---

## TC_017: Submit without selecting Tool — form does not submit or shows empty

**Description:** Verify behavior when SUBMIT is clicked without selecting a Tool.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Coverage Checker | Page loads |
| 2 | Leave Tool Information empty | No tool selected |
| 3 | Select Year=2024, Make=BMW, Model=8 Series, Engine=L6, 3.0L (B58C) | Vehicle data filled |
| 4 | Click "SUBMIT" | Form does not submit OR results are empty / validation message shown |

**Priority:** P2
**Type:** Negative

---

## TC_018: Direct URL navigation to Coverage Checker

**Description:** Verify that navigating directly to /Support/CoverageChecker loads the page correctly without login.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open browser and go to https://pro.repairsolutions.com/Support/CoverageChecker | Page loads |
| 2 | Observe the page | "Coverage Checker" heading is visible, form is interactive |
| 3 | Verify no login is required | User is NOT redirected to login page |

**Priority:** P1
**Type:** Navigation

---
