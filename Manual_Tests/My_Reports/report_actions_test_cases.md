# Manual Test Cases — My Reports: Report Actions (Edit / Share / Delete)

**Module:** My Reports  
**Feature:** Edit, Share, Delete Report  
**Priority:** P1 — Critical  
**Environment:** https://staging-app-pro.repairsolutions.innovavietnam.com/Report  
**Precondition:** User is logged in and on the My Reports page.

---

## EDIT REPORT

## TC-EDIT-001: Edit report with valid information

**Description:** Verify a report can be updated with valid customer information.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Check the checkbox of the first report | Checkbox selected; Edit, Share, Delete buttons become active |
| 2 | Click "Edit" button | Edit form/modal opens |
| 3 | Clear and enter First Name: `John` | First Name populated |
| 4 | Clear and enter Last Name: `Doe` | Last Name populated |
| 5 | Clear and enter Phone: `5551234567` | Phone populated |
| 6 | Clear and enter Email: `john.doe@test.com` | Email populated |
| 7 | Verify Save button is enabled | Save/Assign button is clickable |
| 8 | Click Save | Form submits; modal closes or success message shown |

**Priority:** P1  
**Type:** Positive

---

## TC-EDIT-002: Edit with empty First Name — error validation

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select a report checkbox | Edit button active |
| 2 | Click "Edit" | Edit form opens |
| 3 | Clear First Name field (enter spaces or blank) | Empty |
| 4 | Click Save | Error: "This field is required." on First Name; red border shown |
| 5 | Form does not submit | Modal stays open |

**Priority:** P2  
**Type:** Negative

---

## TC-EDIT-003: Edit with empty Last Name — error validation

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select a report checkbox | Edit button active |
| 2 | Click "Edit" | Edit form opens |
| 3 | Clear Last Name field | Empty |
| 4 | Click Save | Error: "This field is required." on Last Name; red border shown |

**Priority:** P2  
**Type:** Negative

---

## TC-EDIT-004: Edit with empty Phone — error validation

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select a report checkbox | — |
| 2 | Click "Edit" | Edit form opens |
| 3 | Clear Phone field | Empty |
| 4 | Click Save | Error: "Please enter a valid phone number"; red border |

**Priority:** P2  
**Type:** Negative

---

## TC-EDIT-005: Edit with empty Email — error validation

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select a report checkbox | — |
| 2 | Click "Edit" | Edit form opens |
| 3 | Clear Email field | Empty |
| 4 | Click Save | Error: "Please enter a valid email"; red border |

**Priority:** P2  
**Type:** Negative

---

## TC-EDIT-006: Edit with invalid email format

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select checkbox → Click "Edit" | Edit form opens |
| 2 | Enter invalid email: `notanemail` | Field populated |
| 3 | Click Save or Tab out | Error: "Please enter a valid email"; red border |

**Test data:** `notanemail`, `user@`, `@domain.com`, `user@.com`  
**Priority:** P2  
**Type:** Negative

---

## SHARE REPORT

## TC-SHARE-001: Copy Link changes button text

**Description:** Verify clicking "Copy Link" changes the button text to "Link Copied!".

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Check the first report checkbox | Action buttons appear |
| 3 | Click "Share" button | Share modal/panel opens |
| 4 | Click "Copy Link" button | Button text changes to "Link Copied!" |
| 5 | Verify button state | "Link Copied!" is displayed |

**Priority:** P1  
**Type:** Positive

---

## TC-SHARE-002: Share report via email (direct send)

**Description:** Verify a report can be shared by entering a valid email address.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select first report checkbox | — |
| 2 | Click "Share" | Share panel opens |
| 3 | Enter email: `thang.huynh@vn.innova.com` | Email entered |
| 4 | Press Tab or confirm email entry | Email tag/chip added |
| 5 | Click "Send" button | Share popup closes |
| 6 | No error shown | Share completed successfully |

**Priority:** P1  
**Type:** Positive

---

## TC-SHARE-003: Auto-suggest email on partial input

**Description:** Verify that typing a partial email triggers auto-suggest dropdown.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select first report checkbox | — |
| 2 | Click "Share" | Share panel opens |
| 3 | Type partial keyword: `thang` | Auto-suggest dropdown appears below input |
| 4 | Verify suggestion: `thang.huynh@vn.innova.com` | Suggestion item visible |
| 5 | Click on the suggestion | Email added as tag/chip |
| 6 | Verify tag visible | `thang.huynh@vn.innova.com` shown in tag container |

**Priority:** P1  
**Type:** Positive

---

## TC-SHARE-004: Share with invalid email — error message

**Description:** Verify error message shown when an invalid email is entered in Share.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select first report checkbox | — |
| 2 | Click "Share" | Share panel opens |
| 3 | Enter invalid email: `abcde` | Field populated |
| 4 | Press Tab or click elsewhere | Error: "Please enter a valid email" |

**Priority:** P1  
**Type:** Negative

---

## TC-SHARE-005: Share with empty email — Send button behavior

**Description:** Verify Send button is disabled or shows error when no email is entered.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select checkbox → Click "Share" | Share panel opens |
| 2 | Leave email input empty | — |
| 3 | Click "Send" | Send button is disabled OR error shown |

**Priority:** P2  
**Type:** Negative

---

## DELETE REPORT

## TC-DELETE-001: Delete → "No, keep it!" — report is not deleted

**Description:** Verify that clicking "No, keep it!" in the delete confirmation cancels the deletion.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Note the first report in the list (vehicle name) | Vehicle name recorded |
| 3 | Check the first report checkbox | Action buttons appear |
| 4 | Click "Delete" button | Delete confirmation modal appears |
| 5 | Click "No, keep it!" | Modal closes |
| 6 | Inspect first row in table | Same report still visible; NOT deleted |

**Priority:** P1  
**Type:** Negative / Cancellation flow

---

## TC-DELETE-002: Delete → close modal (X) — report is not deleted

**Description:** Verify that clicking the modal close (X) button cancels the deletion.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Note the first report | Vehicle name recorded |
| 3 | Select first checkbox → Click "Delete" | Delete confirmation modal appears |
| 4 | Click X (close icon) on modal | Modal closes |
| 5 | Inspect first row | Report still present |

**Priority:** P1  
**Type:** Negative / Cancellation flow

---

## TC-DELETE-003: Delete → "Yes, delete" — report is removed

**Description:** Verify that confirming deletion removes the report from the table.

> **Warning:** This is a destructive test. Run only when test data can be restored.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Note vehicle name of first report | Name recorded |
| 3 | Select first checkbox → Click "Delete" | Confirmation modal appears |
| 4 | Click "Yes, delete" (confirm button) | Modal closes |
| 5 | Inspect report table | The deleted report no longer appears in the list |

**Priority:** P1  
**Type:** Positive / Destructive

---

## TC-DELETE-004: Delete button appears only after checkbox selection

**Description:** Verify that the Delete button is only visible/active after at least one checkbox is selected.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | No action buttons visible |
| 2 | Do NOT check any checkbox | — |
| 3 | Verify Delete button state | Delete button absent or disabled |
| 4 | Check one checkbox | Delete button appears/becomes active |

**Priority:** P2  
**Type:** UI / Access control
