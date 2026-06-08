# Manual Test Cases — Give/Get Fix

**Module:** Give/Get Fix
**Feature:** Give Fix & Get Fix
**Ticket:** RWR-557 — Give Fix - Update the Give Fix at Get Fix function (Pending Issues)
**Epic:** EPIC 9 — Give/Get Fix (added Apr 2026)
**Priority:** P2 — High
**Environment:** https://staging-app-pro.repairsolutions.innovavietnam.com → Give/Get Fix (sidebar)
**Admin:** http://staging-admin-pro.repairsolutions.innovavietnam.com → User Fix Submissions tab
**Precondition:** User is logged in. Navigate to Give/Get Fix via the left sidebar.

---

## TC_001: Navigate to Give/Get Fix page via sidebar

**Description:** Verify the Give/Get Fix page loads correctly from the sidebar navigation.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Log in with valid credentials | My Reports dashboard loads |
| 2 | Click "Give/Get Fix" in the left sidebar | Page navigates to `/GiveFix` |
| 3 | Verify page heading | "Give/Get Fix" heading is visible |
| 4 | Verify two tabs present | "Give Fix" tab and "Get Fix" tab are displayed |
| 5 | Verify default active tab | "Give Fix" tab is active by default |

**Priority:** P1
**Type:** Navigation

---

## TC_002: Switch between Give Fix and Get Fix tabs

**Description:** Verify both tabs are clickable and load their respective content.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Give/Get Fix page | Give Fix tab active |
| 2 | Click "Get Fix" tab | Get Fix content loads (open reports table + form) |
| 3 | Click "Give Fix" tab | Give Fix content loads (search form) |
| 4 | Verify no page reload occurs | Tab switches without full page refresh |

**Priority:** P1
**Type:** Navigation / UI

---

## TC_003: Get Fix — open reports table displays correct columns

**Description:** Verify the open reports table has all required columns.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Get Fix tab | Open reports table visible |
| 2 | Verify table columns | Vehicle, Engine, Confirmed/MIL DTC, DTC Definition, Date Requested, Close button all present |
| 3 | Verify row data | Each row shows actual vehicle and DTC data |
| 4 | Verify "Showing X Open Reports" count | Count matches number of rows displayed |

**Priority:** P2
**Type:** UI

---

## TC_004: Get Fix — pagination options change rows displayed

**Description:** Verify pagination options (10/20/50/100) control how many rows are shown.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Get Fix tab | Open reports table visible |
| 2 | Select "10" from pagination dropdown | Table shows maximum 10 rows |
| 3 | Select "50" | Table shows up to 50 rows |
| 4 | Select "100" | Table shows up to 100 rows |

**Priority:** P3
**Type:** Functional

---

## TC_005: Get Fix — view closed reports

**Description:** Verify "View my closed reports" link loads the closed report history.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Get Fix tab | "View my closed reports" link visible |
| 2 | Click "View my closed reports" | Closed reports list or page loads |
| 3 | Verify content | Previously closed reports are listed |

**Priority:** P3
**Type:** Functional

---

## TC_006: Get Fix — close a report from the open table

**Description:** Verify clicking CLOSE on a report removes it from the open list.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Get Fix tab | Open reports table shows reports |
| 2 | Click "CLOSE" on any report row | Confirmation or immediate removal |
| 3 | Verify the report is no longer in the open table | Report count decreases by 1 |
| 4 | Verify the report appears in closed reports | Report moved to closed history |

**Priority:** P2
**Type:** Functional

---

## TC_007: Get Fix — submit form with VIN → results display top 3 fixes

**Description:** Verify entering a VIN and DTC code returns the top 3 verified fixes.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Get Fix tab | Form visible below open reports table |
| 2 | Enter a valid Confirmed/MIL DTC code (e.g., `P0302`) | DTC field populated |
| 3 | Enter a valid 17-character VIN in the VIN input | VIN field populated |
| 4 | Enter Odometer value (e.g., `85000`) | Odometer field populated |
| 5 | Select Transmission (e.g., `Automatic`) | Transmission selected |
| 6 | Click "SUBMIT" | Results load showing top 3 most likely fixes |
| 7 | Verify fix results | Up to 3 verified fixes are displayed |

**Priority:** P1
**Type:** Functional

---

## TC_008: Get Fix — submit form with manual YMME → results display top 3 fixes

**Description:** Verify selecting Year/Make/Model/Engine manually and submitting returns fixes.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Get Fix tab | Form visible |
| 2 | Enter a valid Confirmed/MIL DTC code (e.g., `P0302`) | DTC field populated |
| 3 | Select Year: `2018`, Make: `Ford`, Model: `Explorer`, Engine: `V6, 3.5L; Dohc` | All dropdowns selected |
| 4 | Enter Odometer (e.g., `90000`) and select Transmission: `Automatic` | Fields populated |
| 5 | Click "SUBMIT" | Results load showing top 3 most likely fixes |

**Priority:** P1
**Type:** Functional

---

## TC_009: Get Fix — Submit New Fix button is ENABLED after submitting (RWR-557 bug fix)

**Description:** Verify the "Submit New Fix" button is enabled after the user submits vehicle info — this was the core bug in RWR-557.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Get Fix tab | Form visible |
| 2 | Enter DTC: `P0302`, Vehicle: 2018 Ford Explorer V6 3.5L, Odometer: `90000`, Transmission: `Automatic` | All required fields filled |
| 3 | Click "SUBMIT" | Fix results are displayed |
| 4 | Verify "Submit New Fix" button state | **Button is ENABLED** (not disabled/greyed out) |

**Priority:** P1
**Type:** Functional — Bug Verification

---

## TC_010: Get Fix — Submit New Fix for vehicle with existing fix → data saved in Admin

**Description:** Verify submitting a new fix for a vehicle that already has existing fixes saves correctly to Admin.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Submit Get Fix form for a known vehicle with existing fixes | Top 3 fixes displayed, Submit New Fix button enabled |
| 2 | Click "Submit New Fix" | New fix submission form or confirmation appears |
| 3 | Fill in fix details and confirm | Submission succeeds |
| 4 | Log in to Admin: `http://staging-admin-pro.repairsolutions.innovavietnam.com` | Admin loads |
| 5 | Navigate to "User Fix Submissions" tab in the left sidebar | Submissions list opens |
| 6 | Verify the submitted fix appears in the list | Fix entry visible with correct vehicle and DTC data |

**Priority:** P1
**Type:** Functional — End to End

---

## TC_011: Get Fix — reinforce one of the top 3 existing fixes → data saved in Admin

**Description:** Verify that a user can reinforce an existing fix from the top 3 results and it is recorded in Admin.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Submit Get Fix form → top 3 fixes displayed | Fixes visible |
| 2 | Click reinforce/vote on one of the top 3 fixes | Action is confirmed |
| 3 | Check Admin "User Fix Submissions" | Reinforced fix appears in the submissions list |

**Priority:** P2
**Type:** Functional

---

## TC_012: Get Fix — required field validation: missing DTC

**Description:** Verify the form cannot be submitted without a DTC code.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Get Fix tab | Form visible |
| 2 | Leave DTC Code field empty | Field is blank |
| 3 | Fill all other fields (VIN or YMME, Odometer, Transmission) | Other fields populated |
| 4 | Click "SUBMIT" | Form does not submit — DTC field shows required validation error |

**Priority:** P2
**Type:** Negative

---

## TC_013: Get Fix — required field validation: missing vehicle info

**Description:** Verify the form cannot be submitted without vehicle info (VIN or YMME).

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter only DTC and Odometer, leave Year/Make/Model/Engine and VIN blank | Vehicle info missing |
| 2 | Click "SUBMIT" | Validation error shown for vehicle info field |

**Priority:** P2
**Type:** Negative

---

## TC_014: Get Fix — required field validation: missing Odometer

**Description:** Verify the form cannot be submitted without an Odometer value.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Fill all fields except Odometer | Odometer blank |
| 2 | Click "SUBMIT" | Validation error shown on Odometer field |

**Priority:** P2
**Type:** Negative

---

## TC_015: Get Fix — required field validation: missing Transmission

**Description:** Verify the form cannot be submitted without selecting a Transmission type.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Fill all fields except Transmission | Transmission = "Select Transmission" |
| 2 | Click "SUBMIT" | Validation error shown on Transmission field |

**Priority:** P2
**Type:** Negative

---

## TC_016: Give Fix — search vehicle by Year/Make/Model/Engine

**Description:** Verify the Give Fix search form returns matching vehicle results.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Give Fix tab | Search form with Year/Make/Model/Engine dropdowns visible |
| 2 | Select Year: `2018`, Make: `Ford`, Model: `Explorer`, Engine: `V6, 3.5L` | Dropdowns populated |
| 3 | Click "SEARCH" | Matching vehicle results are displayed |

**Priority:** P1
**Type:** Functional

---

## TC_017: Give Fix — Clear button resets search form

**Description:** Verify the Clear button empties all search fields.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Give Fix tab | Search form visible |
| 2 | Select Year, Make, Model, Engine | All dropdowns have values |
| 3 | Click "Clear" | All dropdowns reset to default (empty / placeholder) |
| 4 | Verify no search results remain | Results area cleared |

**Priority:** P2
**Type:** Functional

---

## TC_018: Give Fix — Use Information From My Reports auto-fills form

**Description:** Verify selecting a report from "Use Information From My Reports" auto-fills the vehicle search form.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Give Fix tab | "Use Information From My Reports" section visible |
| 2 | Click "Select report to auto-fill" dropdown | List of user's reports appears |
| 3 | Select a report from the list | Year, Make, Model, Engine fields auto-populate |
| 4 | Click "SEARCH" | Results appear for the auto-filled vehicle |

**Priority:** P2
**Type:** Functional

---

## TC_019: Give Fix — fix dropdown shows available fix options after search

**Description:** Verify that after a search returns results, a dropdown of available fixes appears.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Search a vehicle in Give Fix tab | Results shown |
| 2 | Inspect the results area | A dropdown list of available fixes is displayed |
| 3 | Open the dropdown | Fix options are listed and selectable |

**Priority:** P1
**Type:** Functional

---

## TC_020: Give Fix — select fix from dropdown and submit → data saved in Admin

**Description:** Verify that selecting a fix from the dropdown and submitting saves it to Admin.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Search a vehicle in Give Fix tab | Results with fix dropdown shown |
| 2 | Select a fix option from the dropdown | Fix selected |
| 3 | Submit/confirm the selection | Submission confirmation shown |
| 4 | Log in to Admin: `http://staging-admin-pro.repairsolutions.innovavietnam.com` | Admin loads |
| 5 | Go to "User Fix Submissions" tab in the left sidebar | Submissions list opens |
| 6 | Verify the submitted fix appears in the list | Fix visible with correct vehicle and DTC data |

**Priority:** P1
**Type:** Functional — End to End

---

## TC_021: Admin — submitted fix uses Profile First Name + Last Name

**Description:** Verify the submitter name in Admin uses Option 2 (Profile First + Last Name), not "RSPRO".

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Submit a fix via Get Fix or Give Fix | Submission saved |
| 2 | Log in to Admin → User Fix Submissions tab | Submissions list visible |
| 3 | Locate the submitted fix row | Row is present |
| 4 | Verify the "Name" or submitter field | Shows user's Profile First Name + Last Name (e.g., "Minh Nguyen") |
| 5 | Verify it does NOT show "RSPRO" as the first name | Field does not contain "RSPRO" |

**Priority:** P1
**Type:** Functional — Data Verification

---

## TC_022: Admin — submitted fix data format matches Pending Fix Queue format

**Description:** Verify that fix submissions stored in Admin follow the same data format as the existing Pending Fix Queue.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Submit a fix via Get Fix | Fix saved in Admin |
| 2 | Log in to Admin → User Fix Submissions tab | Submissions list visible |
| 3 | Compare the submitted fix entry with an existing Pending Fix Queue entry | Fields, structure, and data format are consistent |

**Priority:** P2
**Type:** Data Verification

---

*Total: 22 test cases*
*Generated from Jira ticket RWR-557 — Give Fix: Update the Give Fix at Get Fix function (Pending Issues)*
*Tester: QA — Huynh Quoc Thang*
*Page inspected via Selenium: https://staging-app-pro.repairsolutions.innovavietnam.com/GiveFix and /GetFix*
