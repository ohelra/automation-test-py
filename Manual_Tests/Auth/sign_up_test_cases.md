# Manual Test Cases — Sign Up

**Module:** Authentication  
**Feature:** Sign Up (Registration)  
**Priority:** P2 — High  
**Environment:** https://staging-app-pro.repairsolutions.innovavietnam.com  
**Precondition:** Navigate to login page → click "Create One." link

---

## STEP 1: Email & Password

## TC-SIGNUP-001: Sign up with already registered email

**Description:** Verify error when user enters an email that already exists.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click "Create One." on login page | Sign Up form displayed |
| 2 | Enter existing email: `sangqa@yopmail.com` | Email field populated |
| 3 | Enter valid password: `12345678` | Password field populated |
| 4 | Click Continue | Error message "Email has been used" is displayed |

**Priority:** P2  
**Type:** Negative

---

## TC-SIGNUP-002: Sign up with invalid email format

**Description:** Verify error when email format is invalid.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter invalid email: `invalidemail` | Field populated |
| 2 | Enter valid password: `12345678` | Field populated |
| 3 | Click Continue | Error message "Email invalid" is displayed |

**Priority:** P2  
**Type:** Negative

---

## TC-SIGNUP-003: Sign up with empty email

**Description:** Verify error when email field is empty.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Leave email field empty | — |
| 2 | Enter valid password | — |
| 3 | Click Continue | Inline error shown on Email field; Continue button is disabled or blocked |

**Priority:** P2  
**Type:** Negative

---

## TC-SIGNUP-004: Sign up with empty password

**Description:** Verify error when password field is empty.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter valid email | — |
| 2 | Leave password field empty | — |
| 3 | Click Continue | Inline error shown on Password field |

**Priority:** P2  
**Type:** Negative

---

## TC-SIGNUP-005: Sign up with invalid/weak password

**Description:** Verify error when password does not meet requirements.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter valid email | — |
| 2 | Enter weak password: `123` | — |
| 3 | Click Continue | Password error message shown (e.g., "Password must be at least X characters") |

**Priority:** P2  
**Type:** Negative

---

## TC-SIGNUP-006: EULA/Terms link navigation

**Description:** Verify "EULA/Terms" link navigates to Terms of Use page.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Reach personal info step of sign up | Checkbox with EULA/Terms and Privacy Policy links visible |
| 2 | Click "EULA/Terms" link | Navigates to Terms of Use & End User License Agreement page |
| 3 | Verify page heading | "Terms of Use & End User License Agreement" heading visible |

**Priority:** P3  
**Type:** Navigation

---

## TC-SIGNUP-007: Privacy Policy link navigation

**Description:** Verify "Privacy Policy" link navigates to Privacy Policy page.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Reach personal info step of sign up | Links visible |
| 2 | Click "Privacy Policy" link | Navigates to Privacy Policy page |
| 3 | Verify page heading | "Privacy Policy" heading visible |

**Priority:** P3  
**Type:** Navigation

---

## STEP 2: Personal Information

## TC-SIGNUP-008: Empty First Name shows error

**Description:** Verify required field error when First Name is empty.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Reach personal info step | Form visible |
| 2 | Leave First Name empty | — |
| 3 | Fill all other required fields | — |
| 4 | Click Continue | First Name field shows error message |

**Priority:** P2  
**Type:** Negative

---

## TC-SIGNUP-009: Empty Last Name shows error

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Reach personal info step | — |
| 2 | Leave Last Name empty | — |
| 3 | Fill other required fields | — |
| 4 | Click Continue | Last Name field shows error message |

**Priority:** P2  
**Type:** Negative

---

## TC-SIGNUP-010: Empty Address Line 1 shows error

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Reach personal info step | — |
| 2 | Leave Address Line 1 empty | — |
| 3 | Fill other required fields | — |
| 4 | Click Continue | Address 1 error message shown |

**Priority:** P2  
**Type:** Negative

---

## TC-SIGNUP-011: Valid ZipCode auto-fills City and State

**Description:** Verify that entering a valid US ZIP code triggers auto-fill for City and State.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Reach personal info step | ZipCode, City, State fields visible |
| 2 | Enter valid ZIP: `90210` | — |
| 3 | Press Tab or click outside | City field auto-filled (e.g., "Beverly Hills"), State auto-filled (e.g., "CA") |

**Priority:** P2  
**Type:** Positive / Integration

---

## TC-SIGNUP-012: Invalid ZipCode shows error

**Description:** Verify error message for invalid ZIP code.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter invalid ZIP: `00000` or `ABCDE` | — |
| 2 | Press Tab | Error message shown on ZipCode field |
| 3 | City and State remain empty | No auto-fill occurs |

**Priority:** P2  
**Type:** Negative

---

## TC-SIGNUP-013: Empty ZipCode shows error

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Leave ZipCode empty | — |
| 2 | Click Continue | ZipCode error message displayed |

**Priority:** P2  
**Type:** Negative

---

## TC-SIGNUP-014: All required fields empty shows multiple errors

**Description:** Verify that submitting personal info step with all required fields empty shows all relevant errors.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Reach personal info step | — |
| 2 | Leave First Name, Last Name, Address1, ZipCode empty | — |
| 3 | Click Continue | All four fields show individual error messages |

**Priority:** P2  
**Type:** Negative
