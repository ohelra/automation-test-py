# Test Planning — RepairSolutionsPRO Website

**Project:** RepairSolutionsPRO (RSPRO) Website  
**Version:** Staging  
**Environment:** https://staging-app-pro.repairsolutions.innovavietnam.com 
**Prepared by:** QA Team  
**Date:** 2026-04-02  
**STLC Phase:** Test Planning

---

## 1. STLC Overview

| Phase | Status | Owner |
|-------|--------|-------|
| 1. Requirement Analysis | Done | QA Team |
| 2. Test Planning | In Progress | QA Team |
| 3. Test Case Development | In Progress | QA Team |
| 4. Environment Setup | Done (Staging) | DevOps / QA |
| 5. Test Execution | Pending | QA Team |
| 6. Test Cycle Closure | Pending | QA Team |

---

## 2. Scope

### In Scope
| Module | Features |
|--------|---------|
| Authentication | Login, Sign Up (multi-step), ZipCode validation |
| Home Page | Introduction Features animations |
| Products | Diagnostic Tools — 7111, SDS50, SDS43 (Grid/List view, Store links, Product Detail) |
| Support | DTC Library search, SGW AutoAuth navigation, Coverage Checker form & results (added: RWR-589, May 2026) |
| Technical Center | Emerging Technologies articles content |
| My Reports | Search, Filter, Edit, Share, Delete report actions |
| Give/Get Fix | Get Fix form submission, Submit New Fix button, Give Fix search & dropdown, Admin verification (added: RWR-557, Apr 2026) |
| Web Performance | Image upload pipeline (WebP conversion, validation, resize) — Consumer Web + Admin; Legacy image migration verification; CloudFront CDN delivery; Lighthouse performance score (target > 27) (added: RWR-588, Apr 2026) |

### Out of Scope (current cycle)
- How-to Videos
- Updates / Manuals
- DLC Locator
- Support Request form
- ~~Coverage Checker~~ (moved In Scope — RWR-589, May 2026)
- Forgot Password flow
- Account Settings / Profile
- Notification system
- Mobile / Responsive layout
- Cross-browser (Firefox, Safari, Edge)

---

## 3. Test Strategy

### 3.1 Testing Types

| Type | Purpose | Tools |
|------|---------|-------|
| Functional Testing | Verify features work per requirements | Selenium + pytest |
| UI / Smoke Testing | Verify page loads, navigation, key elements visible | Manual + Selenium |
| Regression Testing | Confirm existing features work after changes | Selenium + pytest |
| Boundary Testing | Edge values for inputs (email, zipcode, date, search) | Manual + Data-driven |
| Negative Testing | Invalid inputs, error messages, access control | Manual + Selenium |
| Exploratory Testing | Discover unscripted defects | Manual |

### 3.2 Test Levels

```
Unit Tests          → Not in QA scope (Dev responsibility)
Integration Tests   → API-level (login, report CRUD) — future scope
System Tests        → End-to-end UI flows — PRIMARY FOCUS
Acceptance Tests    → Business scenario validation
```

### 3.3 Entry & Exit Criteria

**Entry Criteria:**
- Staging build is deployed and accessible
- Test data is available (accounts, reports, vehicles)
- Test environment configuration is verified

**Exit Criteria:**
- All planned test cases executed
- Critical/High priority defects resolved
- Test pass rate >= 90%
- Test summary report issued

---

## 4. Epics & Test Scenarios

### EPIC 1: Authentication

**Epic Goal:** Users can register, log in, and access the platform securely.

| Story | Scenario |
|-------|---------|
| E1-S1 | User logs in with valid credentials → lands on My Reports dashboard |
| E1-S2 | User logs in with invalid credentials → sees error message |
| E1-S3 | User logs in with empty fields → button disabled or inline errors |
| E1-S4 | Password field is masked by default; toggle reveals/hides password |
| E1-S5 | New user registers with valid email + strong password |
| E1-S6 | Sign up blocked for already-registered email |
| E1-S7 | Sign up blocked for invalid email format |
| E1-S8 | Sign up blocked for weak/empty password |
| E1-S9 | Valid ZipCode auto-fills City and State |
| E1-S10 | Invalid ZipCode shows error message |
| E1-S11 | Empty required fields (First Name, Last Name, Address1) show errors |
| E1-S12 | EULA/Terms link navigates to Terms of Use page |
| E1-S13 | Privacy Policy link navigates to Privacy Policy page |

---

### EPIC 2: Home Page — Introduction Features

**Epic Goal:** Interactive animations and hover effects work correctly on the home page.

| Story | Scenario |
|-------|---------|
| E2-S1 | Hover over "Fix For DTC" section shows modal with zoom animation |
| E2-S2 | Hover over "Repair Tips" section shows modal |
| E2-S3 | Hover over "Vehicle Inspection Report" section shows modal |
| E2-S4 | Hover step 1 indicator → color changes from `#d6e3f1` to gradient |
| E2-S5 | Hover step 2 indicator → color changes |
| E2-S6 | Hover step 3 indicator → color changes |
| E2-S7 | Hover step 4 indicator → color changes |
| E2-S8 | Hover over three-device section → tablet position changes |
| E2-S9 | Hover over mobile device → scale changes to 1.135 |

---

### EPIC 3: Products — Diagnostic Tools

**Epic Goal:** Users can view product details and find retail stores for each tool.

| Story | Scenario |
|-------|---------|
| E3-S1 | 7111 Grid View → Find a Store → Canadian store URL correct |
| E3-S2 | 7111 List View → Find a Store → Canadian store URL correct |
| E3-S3 | 7111 Grid View → Find a Store → Auto Parts store URL correct |
| E3-S4 | 7111 List View → Find a Store → Auto Parts store URL correct |
| E3-S5 | 7111 List View → Product Detail → correct product page title |
| E3-S6 | SDS50 Grid View → Find a Store → Auto Parts store URL correct |
| E3-S7 | SDS50 List View → Find a Store → Auto Parts store URL correct |
| E3-S8 | SDS50 List View → Product Detail → correct product page title |
| E3-S9 | SDS43 Grid View → Find a Store → Auto Parts store URL correct |
| E3-S10 | SDS43 List View → Find a Store → Auto Parts store URL correct |
| E3-S11 | SDS43 List View → Product Detail → correct product page title |

---

### EPIC 4: Support

**Epic Goal:** Technicians can search DTC codes and access SGW AutoAuth documentation.

#### DTC Library
| Story | Scenario |
|-------|---------|
| E4-S1 | Search by Make + DTC Code → results appear in table |
| E4-S2 | Results table shows Make, Code, Description columns |
| E4-S3 | Clear All resets Make and Code inputs |
| E4-S4 | Search with invalid/empty code → no results or appropriate message |

#### SGW AutoAuth
| Story | Scenario |
|-------|---------|
| E4-S5 | Support > SGW AutoAuth > 7111 → correct article page loads |
| E4-S6 | Support > SGW AutoAuth > SDS50 → correct article page loads |
| E4-S7 | Support > SGW AutoAuth > SDS43 → correct article page loads |

---

### EPIC 5: Technical Center — Emerging Technologies

**Epic Goal:** Technicians can read curated articles about emerging automotive technologies.

| Story | Scenario |
|-------|---------|
| E5-S1 | Article: "How Advanced Safety Features Are Changing Consumer Expectations" loads with correct content |
| E5-S2 | Article: "The Impact of Alternative Fuel Technologies" loads with correct content |
| E5-S3 | Article: "Sophistication and Emissions Regulations" loads with correct content |
| E5-S4 | Article: "Rapid Global Adoption of Electric Vehicles" loads with correct content |
| E5-S5 | Article: "The Rising Cost of New Vehicles" loads with correct content |

---

### EPIC 6: My Reports — Search

**Epic Goal:** Logged-in users can find reports using the search bar.

| Story | Scenario |
|-------|---------|
| E6-S1 | Search by vehicle make → table shows only matching vehicles |
| E6-S2 | Search by report ID → table shows only matching IDs |
| E6-S3 | Search by report type keyword → table shows only matching types |
| E6-S4 | Search by customer name → table shows only matching customers |
| E6-S5 | Search with invalid/non-existent keyword → "No reports found." displayed |
| E6-S6 | Clear search → all reports shown again |

---

### EPIC 7: My Reports — Filter

**Epic Goal:** Logged-in users can filter reports by date, type, and tool.

| Story | Scenario |
|-------|---------|
| E7-S1 | Filter by date From–To → results within date range only |
| E7-S2 | Filter by Type: OBD II → all rows show OBD II |
| E7-S3 | Filter by Type: Diagnostic → all rows show Diagnostic |
| E7-S4 | Filter by Type: Customer → all rows show Customer |
| E7-S5 | Filter by Type: Collision → all rows show Collision |
| E7-S6 | Filter by Type: Sample → all rows show Sample |
| E7-S7 | Filter by Tool: 7111 → all rows show 7111 |
| E7-S8 | Filter by Tool: SDS43 → all rows show SDS43 |
| E7-S9 | Filter by Tool: SDS50 → all rows show SDS50 |
| E7-S10 | Click Clear → all active filters reset |

---

### EPIC 8: My Reports — Report Actions

**Epic Goal:** Logged-in users can edit, share, and delete reports.

#### Edit
| Story | Scenario |
|-------|---------|
| E8-S1 | Select report → Edit → enter valid First Name, Last Name, Phone, Email → Save succeeds |
| E8-S2 | Edit with empty First Name → error message "This field is required." |
| E8-S3 | Edit with empty Last Name → error message "This field is required." |
| E8-S4 | Edit with empty Phone → error message "Please enter a valid phone number" |
| E8-S5 | Edit with empty Email → error message "Please enter a valid email" |
| E8-S6 | Edit with invalid email format → error message shown |

#### Share
| Story | Scenario |
|-------|---------|
| E8-S7 | Select report → Share → Copy Link → button changes to "Link Copied!" |
| E8-S8 | Select report → Share → enter email → Send → popup closes |
| E8-S9 | Type partial email → auto-suggest dropdown appears → select → tag added |
| E8-S10 | Enter invalid email format → error "Please enter a valid email" |

#### Delete
| Story | Scenario |
|-------|---------|
| E8-S11 | Select report → Delete → click "No, keep it!" → report remains |
| E8-S12 | Select report → Delete → click modal close (X) → report remains |
| E8-S13 | Select report → Delete → click "Yes, delete" → report removed from table |

---

### EPIC 9: Give/Get Fix

**Epic Goal:** Logged-in users can get verified repair fixes for DTCs and submit new fixes that are stored in the Admin Pending Fix Queue.
**Ticket:** RWR-557 | **URL:** `/GiveFix` (Give Fix tab) · `/GetFix` (Get Fix tab)

#### Get Fix Tab (`/GetFix`)
| Story | Scenario |
|-------|---------|
| E9-S1 | Navigate to Give/Get Fix via sidebar → page loads with Give Fix and Get Fix tabs |
| E9-S2 | Open Reports table displays: Vehicle, Engine, Confirmed/MIL DTC, DTC Definition, Date Requested, Close button |
| E9-S3 | Pagination options (10/20/50/100) change number of rows displayed |
| E9-S4 | "View my closed reports" link shows closed report history |
| E9-S5 | Close a report from the open reports table → report moves to closed |
| E9-S6 | Submit Get Fix form with VIN → results display top 3 fixes |
| E9-S7 | Submit Get Fix form with manual YMME → results display top 3 fixes |
| E9-S8 | After submitting vehicle info, "Submit New Fix" button is **enabled** (bug fix RWR-557) |
| E9-S9 | Submit New Fix (vehicle has existing fixes) → data saved in Admin under "User Fix Submissions" |
| E9-S10 | Reinforce one of the top 3 existing fixes → data saved in Admin |
| E9-S11 | Submit without DTC Code → required field validation shown |
| E9-S12 | Submit without Vehicle info → required field validation shown |
| E9-S13 | Submit without Odometer → required field validation shown |
| E9-S14 | Submit without Transmission → required field validation shown |

#### Give Fix Tab (`/GiveFix`)
| Story | Scenario |
|-------|---------|
| E9-S15 | Search vehicle by Year/Make/Model/Engine → matching results shown |
| E9-S16 | "Use Information From My Reports" → select report → form auto-fills |
| E9-S17 | Clear button resets all search fields |
| E9-S18 | After search results load, Give Fix dropdown shows available fix options |
| E9-S19 | Select a fix from dropdown → Submit → data saved in Admin "User Fix Submissions" |

#### Admin Verification
| Story | Scenario |
|-------|---------|
| E9-S20 | Admin "User Fix Submissions" tab shows submitted fix with correct data |
| E9-S21 | Submitter name in Admin = Profile First Name + Last Name (not "RSPRO") |
| E9-S22 | Submitted fix data format matches current Pending Fix Queue format |

---

## 5. Test Priority Matrix

| Priority | Module | Rationale |
|----------|--------|-----------|
| P1 — Critical | Authentication (Login) | Gate for all logged-in features |
| P1 — Critical | My Reports Search & Filter | Core user workflow |
| P1 — Critical | My Reports Edit / Share / Delete | Core CRUD operations |
| P2 — High | Sign Up | New user onboarding |
| P2 — High | Products — Diagnostic Tools | Revenue-linked store navigation |
| P2 — High | Support — DTC Library | Core technician tool |
| P3 — Medium | Home Page animations | Visual/UX, not business-critical |
| P3 — Medium | Technical Center articles | Content verification |
| P3 — Medium | SGW AutoAuth | Support documentation |
| P2 — High | Give/Get Fix — Submit New Fix, Give Fix dropdown, Admin check | Active bug fix RWR-557 — STAGING verification required |
| P1 — Critical | Web Performance — Image Migration, Broken Image scan, CloudFront delivery | Infrastructure change RWR-588 — directly impacts all pages; post-migration verification required on DEV/STAGING/PROD |
| P4 — Low | Cross-browser | Future cycle |

---

## 6. Test Data Requirements

| Module | Data Needed |
|--------|-------------|
| Login | Valid account: sangqa@yopmail.com / 12345678; Invalid credentials |
| Sign Up | New unique email; existing email; invalid emails; valid/invalid zipcodes |
| My Reports — Search | Vehicle makes, IDs, types, customer names from test account |
| My Reports — Filter | Date ranges covering existing reports |
| My Reports — Edit | Valid names, phones, emails; empty/invalid values |
| My Reports — Share | Known user emails for auto-suggest (thang.huynh@vn.innova.com) |
| DTC Library | Car makes (e.g., Toyota), DTC codes (e.g., P0300) |

---

## 7. Test Environment

| Item | Detail |
|------|--------|
| Staging URL | https://staging-app-pro.repairsolutions.innovavietnam.com |
| Browser | Chrome (primary) |
| Resolution | 1920x1080 |
| Test Account | sangqa@yopmail.com / 12345678 |
| Automation Framework | Python + Selenium + pytest |
| Report Tool | Allure Reports |
| Config | config.ini (environment URLs, credentials) |

---

## 8. Risk & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Staging environment instability | High | Run smoke tests before full regression |
| Test data dependency (reports may be deleted) | High | Use dedicated test account; restore data if needed |
| Animation timing sensitivity | Medium | Use explicit waits; add flaky reruns |
| New tab handling in store tests | Medium | Implement tab-switch utility |
| Email verification in Sign Up | High | Use yopmail or skip in automation (manual only) |
| Auto-suggest email changes | Medium | Keep test email consistent |

---

## 9. Automation Recommendation (Pending Confirmation)

The following test cases are recommended for automation based on:
- Repetition frequency
- Stability (no external dependencies)
- Business criticality

> **Note:** These are recommendations pending QA lead / stakeholder review before implementation.

| Recommended for Automation | Reason |
|---------------------------|--------|
| Login — valid/invalid | Runs every regression cycle |
| My Reports — Search (all variants) | Parameterizable, stable |
| My Reports — Filter type/tool | Stable UI interactions |
| My Reports — Filter date range | Logic-heavy, error-prone manually |
| My Reports — Clear filter | Fast, deterministic |
| My Reports — Copy Link | Simple assertion |
| My Reports — Share with email | Auto-suggest logic |
| Products — Store navigation (all 11 tests) | Repetitive, already automated |
| DTC Library — Search | Stable form interaction |
| SGW AutoAuth — Page navigation | Simple navigation |
| Home Page — Hover animations | Already automated (flaky — keep reruns) |
| Technical Center — Article content | Content regression |

| Keep as Manual Only | Reason |
|--------------------|--------|
| Sign Up — email verification step | Requires real email inbox |
| Delete report (confirm yes) | Destructive, data restoration needed |
| Edit empty/invalid fields | Commented out — unstable assertions |
| Forgot Password flow | External email dependency |
| Give/Get Fix | Not yet mapped |
| Cross-browser testing | Manual exploratory per cycle |

---

## 10. Schedule (Indicative)

| Activity | Timeline |
|----------|---------|
| Test Case Development | Week 1 |
| Environment Verification | Week 1 |
| Manual Test Execution | Week 2 |
| Automation Script Review | Week 2–3 |
| Regression Execution | Week 3 |
| Defect Triage & Retest | Week 3–4 |
| Test Cycle Closure Report | End of Week 4 |

---

## 11. End-to-End Test Scenarios

End-to-end tests validate complete user journeys that span multiple modules. Each scenario starts from the entry point a real user would use and asserts the final expected outcome.

---

### E2E-1: New User Registration → First Login → View Dashboard

**Goal:** A brand-new user can create an account and reach the My Reports dashboard.

**Priority:** P1 — Critical  
**Automation:** Partial (skip email verification step; verify redirect post-login manually)

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to `/login` → click "Create One." | Sign Up page loads (Step 1) |
| 2 | Enter unique valid email + strong password → Continue | Step 2 loads (personal info form) |
| 3 | Enter First Name, Last Name, Address Line 1, valid US ZipCode | City and State auto-fill correctly |
| 4 | Check EULA + Privacy Policy checkbox → Continue | Step 3 (email verification) appears |
| 5 | (Manual) Verify email via yopmail inbox | Account activated |
| 6 | Navigate to `/login`, enter new credentials → Login | Redirected to `/Report` (My Reports dashboard) |
| 7 | Assert dashboard header, sidebar navigation, reports table are visible | Dashboard fully loaded |

---

### E2E-2: Returning User Full Login → Search → Filter → View Result

**Goal:** A logged-in user can find a specific report using combined search and filter.

**Priority:** P1 — Critical  
**Automation:** Full automation candidate

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to `/login`, enter `sangqa@yopmail.com / 12345678` → Login | My Reports dashboard loads |
| 2 | Type a known vehicle make keyword in the search bar | Table filters to matching vehicle rows only |
| 3 | Clear search | All reports restored |
| 4 | Apply Type filter: "OBD II" | Only OBD II rows visible |
| 5 | Apply Tool filter: "7111" (while Type filter still active) | Table shows only OBD II rows from tool 7111 |
| 6 | Click "Clear" filters | All reports restored to full list |

---

### E2E-3: Logged-In User → Edit Report → Share Report → Verify State

**Goal:** A user can update a report's customer info and share it via copy link in a single session.

**Priority:** P1 — Critical  
**Automation:** Full automation candidate

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Login with valid credentials → My Reports dashboard | Dashboard loads |
| 2 | Select checkbox of a report row | Row highlighted; action buttons (Edit, Share, Delete) enabled |
| 3 | Click Edit → update First Name, Last Name, valid Phone, valid Email → Save | Edit modal closes; table reflects updated customer info |
| 4 | Re-select the same report row → click Share | Share modal opens |
| 5 | Click "Copy Link" | Button label changes to "Link Copied!" |
| 6 | Enter a valid known email in Share by Email field → Send | Popup closes on success |
| 7 | Verify report is still present in the table (no accidental delete) | Report row intact |

---

### E2E-4: Logged-In User → Delete Report → Confirm Cancellation → Confirm Deletion

**Goal:** The delete flow protects against accidental deletion and allows intentional removal.

**Priority:** P1 — Critical  
**Automation:** Partial (cancel flow only; deletion is destructive — manual for "Yes, delete" step)

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Login → select a report row → click Delete | Confirm modal appears |
| 2 | Click "No, keep it!" | Modal closes; report row still in table |
| 3 | Select same report row → click Delete | Confirm modal appears again |
| 4 | Click modal close (X) | Modal closes; report row still in table |
| 5 | (Manual) Select report → Delete → "Yes, delete" | Report removed from table permanently |

---

### E2E-5: Guest User — Browse Products → Navigate to Store in New Tab

**Goal:** An unauthenticated user can discover a diagnostic tool and navigate to a retailer.

**Priority:** P2 — High  
**Automation:** Full automation candidate

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to home page `/` | Home page loads, Nav shows Products, Support, Technical Center |
| 2 | Hover "Products" in nav → click "Diagnostic Tools" | Products page loads in Grid View |
| 3 | Locate 7111 product card → click "Find a Store" → Canadian Tire | New tab opens with `canadiantire.ca` URL |
| 4 | Switch back to original tab | Products page still in Grid View |
| 5 | Switch to List View | Layout switches; product rows displayed |
| 6 | Click "Find a Store" → NAPA Auto Parts for SDS50 | New tab opens with correct NAPA URL |
| 7 | Click "Product Detail" for SDS43 | Product detail page loads with correct title |

---

### E2E-6: Guest User — DTC Library Search → Clear → Re-search

**Goal:** A technician can use the DTC Library to look up a trouble code without logging in.

**Priority:** P2 — High  
**Automation:** Full automation candidate

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to home page → hover "Support" → click "DTC Library" | DTC Library page loads (`/Support/DtcLibrary`) |
| 2 | Select a car make from the dropdown (e.g., Toyota) | Make selected in Select2 component |
| 3 | Enter DTC code `P0300` → click Search | Results table populates with Make, Code, Description |
| 4 | Click "Clear All" | Make dropdown and Code input both reset to empty |
| 5 | Search with only a DTC code and no make selected | Results shown (or appropriate empty state) |
| 6 | Search with completely invalid code (e.g., `XXXXX`) | No results row or empty message displayed |

---

### E2E-7: Guest User — Support → SGW AutoAuth → Switch Tool Tabs

**Goal:** A technician can navigate to SGW AutoAuth and read documentation for each tool.

**Priority:** P3 — Medium  
**Automation:** Full automation candidate

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to home page → hover "Support" → click "SGW AutoAuth" | SGW AutoAuth page loads |
| 2 | Click sub-navigation tab "7111" | Article for 7111 SGW AutoAuth is displayed |
| 3 | Click sub-navigation tab "SDS50" | Article for SDS50 SGW AutoAuth is displayed |
| 4 | Click sub-navigation tab "SDS43" | Article for SDS43 SGW AutoAuth is displayed |

---

### E2E-8: Guest User — Technical Center → Read All Emerging Technologies Articles

**Goal:** A technician can navigate to and read all 5 emerging technologies articles.

**Priority:** P3 — Medium  
**Automation:** Full automation candidate

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to home page → hover "Technical Center" → click "Emerging Technologies" | Emerging Technologies landing page loads |
| 2 | Click article 1 in left sidebar: "How Advanced Safety Features…" | Article body loads with correct title |
| 3 | Click article 2: "The Impact of Alternative Fuel Technologies…" | Article loads with correct title |
| 4 | Click article 3: "Sophistication and Emissions Regulations…" | Article loads with correct title |
| 5 | Click article 4: "Rapid Global Adoption of Electric Vehicles" | Article loads with correct title |
| 6 | Click article 5: "The Rising Cost of New Vehicles…" | Article loads with correct title |

---

### E2E-9: Home Page Animations → Full Hover Journey

**Goal:** All interactive animation sections on the home page respond correctly to hover.

**Priority:** P3 — Medium  
**Automation:** Existing automation (flaky — keep `--reruns 2`)

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to home page `/` | Page loads fully |
| 2 | Scroll to "Introduction Features" section | Section is in viewport |
| 3 | Hover over "Fix For DTC" card | Modal appears with zoom animation |
| 4 | Hover over "Repair Tips" card | Modal appears |
| 5 | Hover over "Vehicle Inspection Report" card | Modal appears |
| 6 | Hover over Step Indicator 1–4 sequentially | Each indicator color changes from `#d6e3f1` to `rgb(106,153,204)` gradient |
| 7 | Hover over Three Device group | Tablet moves (left position changes) |
| 8 | Hover over mobile device image | Scale transforms from `matrix(1,0,0,1,0,0)` to `matrix(1.135,0,0,1.135,0,0)` |

---

### E2E-10: Login → Session Persistence → Navigate Across Modules → Logout (Future)

**Goal:** An authenticated session is maintained across module navigation until logout.

**Priority:** P2 — High  
**Automation:** Partial (logout not yet mapped)

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Login with valid credentials | Redirected to `/Report` dashboard |
| 2 | Click "Support" in the sidebar → DTC Library | DTC Library loads while session is active |
| 3 | Click "Technical Center" in sidebar → Emerging Technologies | Article list loads; user still logged in |
| 4 | Navigate back to `/Report` via sidebar | My Reports dashboard loads; session intact |
| 5 | (Future) Click user profile → Logout | Session ends; redirected to `/login` |
| 6 | (Future) Attempt to navigate directly to `/Report` | Redirected to `/login` (access control enforced) |

---

### E2E Summary Table

| ID | Journey | Modules Covered | Priority | Automation |
|----|---------|----------------|----------|------------|
| E2E-1 | New user registration → first login → dashboard | Auth → Dashboard | P1 | Partial |
| E2E-2 | Login → search → filter → clear | Auth → My Reports | P1 | Full |
| E2E-3 | Login → edit report → share via copy + email | Auth → My Reports | P1 | Full |
| E2E-4 | Login → delete (cancel) → delete (confirm) | Auth → My Reports | P1 | Partial |
| E2E-5 | Browse products → store link → new tab | Home → Products | P2 | Full |
| E2E-6 | DTC Library search → clear → re-search | Home → Support | P2 | Full |
| E2E-7 | SGW AutoAuth tab navigation | Home → Support | P3 | Full |
| E2E-8 | Read all Emerging Technologies articles | Home → Technical Center | P3 | Full |
| E2E-9 | Home page hover animation journey | Home | P3 | Existing |
| E2E-10 | Cross-module session persistence → logout | Auth → All modules | P2 | Partial |
