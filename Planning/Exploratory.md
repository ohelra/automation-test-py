# Exploratory Testing — RepairSolutionsPRO Website

**Tester:** QA Team  
**Date:** 2026-04-02  
**Environment:** Staging — https://staging-app-pro.repairsolutions.innovavietnam.com  
**Credentials used:** sangqa@yopmail.com / 12345678  
**Production reference:** https://pro.repairsolutions.com

---

## 1. Application Overview

RepairSolutionsPRO (RSPRO) is a web platform for automotive technicians that provides:
- Diagnostic report management
- Product information for SDS diagnostic tablets
- Technical resources and articles
- DTC (Diagnostic Trouble Code) library and support tools

The application has **two access zones**:
- **Public Zone** — accessible without login (Home, Products, Support, Technical Center)
- **Private Zone** — requires login (My Reports dashboard, Give/Get Fix, account-level features)

---

## 2. Modules & Features Discovered

### 2.1 Authentication Module (`/login`)

| Feature | Description |
|---------|-------------|
| Login | Email + Password form, Remember Me checkbox, Forgot Password link |
| Password Toggle | Show/hide password via eye icon |
| Error Message | "Username or password is incorrect" on invalid credentials |
| Sign Up | "Don't have an account? Create One." link |
| App Download | Links to Google Play & Apple App Store |
| Language Selector | English / Spanish toggle |

**Sign Up Flow (Multi-step):**
1. **Step 1** — Enter Email + Password → Continue
2. **Step 2** — Enter personal info: First Name, Last Name, Address Line 1 & 2, ZipCode (auto-fills City/State), checkbox agree to EULA/Terms + Privacy Policy → Continue
3. **Step 3** — Verify Account (email verification)

**Sign Up Validations:**
- Email: empty, invalid format, already registered
- Password: empty, invalid (too short/weak)
- ZipCode: invalid, empty (auto-fill City & State on valid zip)
- Required fields: First Name, Last Name, Address Line 1
- EULA/Terms and Privacy Policy links navigate to respective pages

---

### 2.2 Home Page Module (`/`)

| Section | Feature |
|---------|---------|
| Hero Banner | Full-width banner with headline "A Community By Tech For Techs" and "Learn More" CTA |
| Navigation | Products, Support, Technical Center dropdowns + Search + Language + Account button |
| Explore Products | "View All Products" button |
| Introduction Features | Interactive animated sections |

**Introduction Features — Interactive Animations:**

| Feature | Behavior |
|---------|---------|
| Fix For DTC | Scroll to section → Hover → Modal appears with zoom animation |
| Repair Tips | Scroll to section → Hover → Modal appears |
| Vehicle Inspection Report | Scroll to section → Hover → Modal appears |
| Step Indicators (1–4) | Default color `#d6e3f1` → Hover → changes to linear-gradient `rgb(106, 153, 204)` |
| Three Device Animation | Hover over group → tablet moves (left position changes) |
| Mobile Device Zoom | Default scale `matrix(1,0,0,1,0,0)` → Hover → `matrix(1.135, 0, 0, 1.135, 0, 0)` |

---

### 2.3 Products Module — Diagnostic Tools

**Tools Available:**
- **7111** — Smart Diagnostic System Tablet
- **SDS50** — Smart Diagnostic System Tech
- **SDS43** — Smart Diagnostic System Inspector

**View Modes:** Grid View (default) | List View

| Feature | 7111 | SDS50 | SDS43 |
|---------|------|-------|-------|
| Find a Store → Canadian (canadiantire.ca) | Yes | No | No |
| Find a Store → Auto Parts (napa) | Yes | Yes | Yes |
| Product Detail Page (List View) | Yes | Yes | Yes |
| Store opens in new tab | Yes | Yes | Yes |

---

### 2.4 Support Module

#### 2.4.1 DTC Library (`/Support/DtcLibrary`)
| Feature | Description |
|---------|-------------|
| Car Make selector | Dropdown with search input (Select2 component) |
| DTC Code input | Text field to enter code (e.g., P0300) |
| Search button | Submits search |
| Clear All button | Resets all inputs |
| Results table | Columns: Make, Code, Description, Delete icon |

#### 2.4.2 SGW AutoAuth (`/Support/SGWAutoAuth`)
| Feature | Description |
|---------|-------------|
| Sub-navigation | Tabs for 7111, SDS50, SDS43 tools |
| Article content | Per-tool SGW AutoAuth article displayed |
| Navigation via Support dropdown | Hover Support → click SGW AutoAuth |

#### 2.4.3 Other Support items (visible in nav, not yet tested)
- How-to Videos
- Updates / Manuals
- DLC Locator
- Support Request
- Coverage Checker

---

### 2.5 Technical Center Module

#### 2.5.1 Emerging Technologies (`/TechnicalCenter/EmergingTechnologies`)
| Article | Title |
|---------|-------|
| 1 | How Advanced Safety Features Are Changing Consumer Expectations |
| 2 | The Impact of Alternative Fuel Technologies on Future Vehicle Repair |
| 3 | The Impact of Sophistication and Emissions Regulations on Vehicle Reliability |
| 4 | Rapid Global Adoption of Electric Vehicles |
| 5 | The Rising Cost of New Vehicles: From $30K to $50K in Just 12 Years |

**Navigation pattern:** Technical Center dropdown → Emerging Technologies → left sidebar article links

---

### 2.6 My Reports Dashboard (Logged-in, `/Report`)

**Layout:**
- Left sidebar: My Reports | Give/Get Fix | Technical Center (expandable) | Support
- Top bar: Global search (SearchRepairSolutionsPRO), Notification bell, User profile
- Main area: Reports management table

#### 2.6.1 Report Table Columns
| Column | Description |
|--------|-------------|
| Checkbox | Select for bulk/single action |
| ID | Report ID number |
| Vehicle | Year Make Model Engine info |
| (MOTOR badge) | Appears on some vehicles |
| Type | OBD II / Diagnostic / Customer / Collision / Sample |
| Tool | 7111 / SDS43 / SDS50 |
| Customer | Assigned customer name |
| Date and Time | Format MM/DD/YYYY HH:MM AM/PM |

#### 2.6.2 Search Feature
| Search by | Behavior |
|-----------|---------|
| Vehicle | Keyword match in Vehicle column |
| ID | Keyword match in ID column |
| Type | Keyword match in Type column (OBD II, Diagnostic, Customer, Collision) |
| Customer | Keyword match in Customer column |
| Invalid keyword | Displays "No reports found." message |

#### 2.6.3 Filter Feature
**Date Picker:**
- From date / To date inputs
- Results filtered within date range

**Type Filters:** OBD II | Diagnostic | Customer | Collision | Sample

**Tool Filters:** 7111 | SDS43 | SDS50

**Clear All:** Resets all active filter selections

#### 2.6.4 Report Actions (requires checkbox selection)

**Edit:**
- Fields: First Name, Last Name, Phone, Email
- Validations: Required fields (red border + error message), Invalid email format
- Save button enabled only when valid

**Share:**
- Copy Link → button text changes to "Link Copied!"
- Share by Email → email input with auto-suggest from known users, tag display
- Invalid email → error message "Please enter a valid email"
- Send button closes popup on success

**Delete:**
- Confirm modal with "Yes, delete" and "No, keep it!" buttons
- Modal close (X) icon
- On "Keep it" or modal close → report remains unchanged

---

### 2.7 Give/Get Fix (Sidebar, logged-in)

Visible in sidebar navigation. Dedicated feature for community fix sharing — **not yet covered by automated tests**.

---

## 3. Observations & Risk Areas

| Area | Observation |
|------|-------------|
| Authentication | Multi-step sign-up with external email verification — risk of flaky tests |
| Sign Up ZipCode | Auto-fill City/State on zip lookup — depends on external API |
| Modal Animations | Hover-based CSS animations — timing-sensitive in automation |
| New Tab Navigation | Store links open new tabs — requires tab switching logic |
| Share Email Auto-suggest | Depends on backend user data — brittle if test data changes |
| Delete Report | Destructive action — test data dependency, commented out in automation |
| Filter Date Range | Date format `MM/DD/YYYY` — locale-sensitive |
| MOTOR badge | Some reports carry MOTOR badge — unclear business logic |
| Give/Get Fix | No test coverage observed |
| How-to Videos / Manuals / DLC Locator / Support Request / Coverage Checker | No test coverage observed |
| Pagination / Infinite scroll | Report count shows 50 — unknown if pagination exists |
| Responsiveness | Mobile/tablet breakpoints not explored |
| Cross-browser | Only Chrome confirmed, Firefox/Safari/Edge not tested |

---

## 4. Untested Areas (Gaps)

- [ ] Give/Get Fix feature
- [ ] How-to Videos
- [ ] Updates / Manuals
- [ ] DLC Locator
- [ ] Support Request (form submission)
- [ ] Coverage Checker
- [ ] Forgot Password flow
- [ ] Account settings / Profile management
- [ ] Notification bell
- [ ] Global top search bar (in dashboard)
- [ ] Language switcher (English/Spanish)
- [ ] Pagination of reports
- [ ] Multiple checkbox selection (bulk actions)
- [ ] Report detail view (clicking a report row)
- [ ] Mobile / responsive layout
- [ ] Cross-browser compatibility
