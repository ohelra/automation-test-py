# Manual Test Cases — Login

**Module:** Authentication  
**Feature:** Login  
**Priority:** P1 — Critical  
**Environment:** https://staging-app-pro.repairsolutions.innovavietnam.com  
**Precondition:** Navigate to the staging URL; login modal is visible

---

## TC-LOGIN-001: Login with valid credentials

**Description:** Verify user can successfully log in with a valid email and password.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to login page | Login form is displayed with Email, Password fields and Sign In button |
| 2 | Enter valid email: `sangqa@yopmail.com` | Email field is populated |
| 3 | Enter valid password: `12345678` | Password field is masked |
| 4 | Click "Sign In" button | User is redirected to My Reports dashboard |
| 5 | Verify dashboard loaded | "My Reports" heading and report table are visible |

**Priority:** P1  
**Type:** Positive

---

## TC-LOGIN-002: Login with invalid email

**Description:** Verify error message appears when an unregistered email is used.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter unregistered email: `invalid@test.com` | Email field populated |
| 2 | Enter any password: `12345678` | Password field masked |
| 3 | Click "Sign In" | Error message "Username or password is incorrect" is displayed |
| 4 | User remains on login page | User is NOT redirected |

**Priority:** P1  
**Type:** Negative

---

## TC-LOGIN-003: Login with wrong password

**Description:** Verify error message appears when the password is incorrect.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter valid email: `sangqa@yopmail.com` | Email field populated |
| 2 | Enter wrong password: `wrongpass` | Password field masked |
| 3 | Click "Sign In" | Error message "Username or password is incorrect" is displayed |
| 4 | User remains on login page | NOT redirected |

**Priority:** P1  
**Type:** Negative

---

## TC-LOGIN-004: Login with empty email field

**Description:** Verify the form prevents submission when email is empty.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Leave Email field empty | — |
| 2 | Enter valid password: `12345678` | Password field populated |
| 3 | Click "Sign In" | Sign In button is disabled OR inline error shown on email field |
| 4 | User remains on login page | NOT redirected |

**Priority:** P1  
**Type:** Negative

---

## TC-LOGIN-005: Login with empty password field

**Description:** Verify the form prevents submission when password is empty.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter valid email: `sangqa@yopmail.com` | Email field populated |
| 2 | Leave Password field empty | — |
| 3 | Click "Sign In" | Sign In button disabled OR inline error on password field |
| 4 | User remains on login page | NOT redirected |

**Priority:** P1  
**Type:** Negative

---

## TC-LOGIN-006: Password masking — default state

**Description:** Verify the password field is masked (type=password) by default.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to login page | Login form visible |
| 2 | Enter any text in Password field | Text is shown as dots/asterisks |
| 3 | Inspect field attribute | `type="password"` |

**Priority:** P2  
**Type:** UI / Security

---

## TC-LOGIN-007: Toggle password visibility

**Description:** Verify clicking the eye icon reveals and hides the password.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter password: `12345678` | Text masked |
| 2 | Click eye icon (toggle) | Password becomes visible as plain text |
| 3 | Field attribute changes | `type="text"` |
| 4 | Click eye icon again | Password is masked again |
| 5 | Field attribute | `type="password"` |

**Priority:** P2  
**Type:** UI

---

## TC-LOGIN-008: Remember Me checkbox

**Description:** Verify the "Remember Me" checkbox can be checked and unchecked.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to login page | Checkbox unchecked by default |
| 2 | Click "Remember Me" checkbox | Checkbox is checked |
| 3 | Click again | Checkbox is unchecked |

**Priority:** P3  
**Type:** UI

---

## TC-LOGIN-009: Forgot Password link is visible and clickable

**Description:** Verify the "Forgot Password?" link exists and navigates to the recovery page.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to login page | "Forgot Password?" link visible |
| 2 | Click "Forgot Password?" | Navigates to password recovery page or shows recovery form |

**Priority:** P2  
**Type:** Navigation

---

## TC-LOGIN-010: "Create One" link navigates to Sign Up

**Description:** Verify "Don't have an account? Create One." link navigates to sign up.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to login page | "Create One." link visible below the title |
| 2 | Click "Create One." | Sign Up form / registration flow is displayed |

**Priority:** P2  
**Type:** Navigation
