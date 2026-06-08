# Ticket Workflow Skill — From Jira Ticket to Automation

## When to Activate

Activate this workflow whenever the user brings a **new Jira ticket** (Bug, Document, Task, Story, Enhancement)
and asks to create test cases, write automation, or analyze what to test.

---

## Mandatory 4-Phase Workflow

```
Phase 1: READ PLAN  →  Phase 2: UNDERSTAND TICKET  →  Phase 3: MANUAL TEST  →  Phase 4: AUTOMATION
```

**Never skip Phase 1 or Phase 2. Never write automation before Phase 3.**

---

## Phase 1 — Read the Test Plan First

**Always read `Planning/test_planning.md` before doing anything else.**

From the plan, extract:

### 1.1 — Check Scope

| Check | Action |
|---|---|
| Is the feature in **In Scope**? | Proceed with full workflow |
| Is the feature in **Out of Scope**? | Flag it to the user before proceeding — confirm whether scope should be updated |

Current **In Scope** modules (from test_planning.md):

| Module | Features Covered |
|---|---|
| Authentication | Login, Sign Up (multi-step), ZipCode validation |
| Home Page | Introduction Features animations |
| Products | Diagnostic Tools — 7111, SDS50, SDS43 |
| Support | DTC Library search, SGW AutoAuth navigation |
| Technical Center | Emerging Technologies articles |
| My Reports | Search, Filter, Edit, Share, Delete |

Current **Out of Scope** (flag before working on these):
- How-to Videos, Support Request, Coverage Checker, Forgot Password
- Account Settings / Profile, Notifications, Mobile layout, Cross-browser

### 1.2 — Identify the Epic

Map the ticket to the closest Epic in the plan:

| Epic | Module | Covers |
|---|---|---|
| EPIC 1 | Authentication | Login, Sign Up, ZipCode |
| EPIC 2 | Home Page | Hover animations, Introduction Features |
| EPIC 3 | Products | Diagnostic Tools store links, product detail |
| EPIC 4 | Support | DTC Library, SGW AutoAuth |
| EPIC 5 | Technical Center | Emerging Technologies articles |
| EPIC 6 | My Reports | Search |
| EPIC 7 | My Reports | Filter |
| EPIC 8 | My Reports | Edit, Share, Delete |

### 1.3 — Check Existing Scenarios

Scan the relevant Epic's story table in the plan:
- Are there existing scenarios that cover this ticket?
- Does the ticket add new stories not yet in the plan?
- Does it fix a bug in an existing story?

**Decision:**
- **New feature / new stories** → add to the plan's Epic, create new manual TCs, then automate
- **Bug fix** → identify which existing story/scenario is broken, fix the automation, update plan if needed
- **Scope expansion** → update `Planning/test_planning.md` In Scope section and the relevant Epic

---

## Phase 2 — Understand the Ticket + Inspect the Live Page

### Step 2.1 — Read the Jira ticket

Fetch the ticket using the Jira MCP tool. Extract:
- Summary and description
- Acceptance criteria / UI behavior specifications
- Attachments (design mockups, screenshots)
- Comments (may contain decisions or changes to scope)
- Ticket type: Bug / Task / Story / Improvement

### Step 2.2 — Inspect the live website

**Always visit the live page before writing a single test case.**

Go to `https://pro.repairsolutions.com` and navigate to the relevant page.

During inspection, identify and record:
- Exact page heading and subheading text (use this for feature name)
- Navigation path: which menu → which submenu item
- All visible sections on the page
- Form elements: inputs, dropdowns, checkboxes, buttons — with exact label text
- Filter/sidebar options — exact names and counts
- Sort, search controls
- Table/card layout — columns and displayed fields
- Pagination controls
- Empty state messages — exact text
- Error/validation messages — exact text

### Step 2.3 — Determine module, section, and feature name

Map the page to the correct module:

| Website Section | Module folder name | Example feature name |
|---|---|---|
| Support | `Support` | `how_to_videos`, `dtc_library`, `support_request` |
| Products | `Products` | `diagnostic_tools` |
| My Account | `My_Reports` | `my_report` |
| Technical Center | `Technical_Center` | `emerging_technologies` |
| Home Page | `HomePage` | `introduction_features` |
| Auth (Login / Sign Up) | `Auth` | `login`, `sign_up` |

**Feature name rule**: `snake_case` derived from the actual page heading on the live site.
- "How-to Videos" → `how_to_videos`
- "DTC Library" → `dtc_library`
- "Coverage Checker" → `coverage_checker`

### Step 2.4 — Classify the ticket

| Ticket Type | What to do |
|---|---|
| **New Feature / Story** | Create manual TCs → automate → update test_planning.md |
| **Bug** | Identify which existing test covers it → fix automation → add missing TC if gap found |
| **UI / Design update** | Check if existing locators are still valid → update page object → update manual TC steps |
| **Content update** | Update test data in `test_data/` and expected values in test scripts |

---

## Phase 3 — Create or Update Manual Test Cases

### File location

```
Manual_Tests/<Module>/<feature_name>_test_cases.md
```

Examples:
```
Manual_Tests/Support/how_to_videos_test_cases.md
Manual_Tests/Support/dtc_library_test_cases.md
Manual_Tests/Auth/login_test_cases.md
Manual_Tests/Technical_Center/emerging_technologies_test_cases.md
```

### Test case ID format

`TC_001`, `TC_002`, ... (sequential, zero-padded to 3 digits).
Do NOT use prefixes like `TC-HTV-001` or `TC-DTC-001`.

### File header template

```markdown
# Manual Test Cases — <Module>: <Feature Name>

**Module:** <Module>
**Feature:** <Feature Name>
**Ticket:** <TICKET-ID> — <Ticket Summary>
**Epic:** EPIC <N> — <Epic Name> (from test_planning.md)
**Priority:** P<1|2|3> — <High|Medium|Low>
**Environment:** https://pro.repairsolutions.com → <Navigation Path>
**Precondition:** <What state the user must be in before starting>

---
```

### Test case template

```markdown
## TC_001: <Short description of what is being verified>

**Description:** Verify that <expected behavior>.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | <User action> | <Expected outcome> |
| 2 | <User action> | <Expected outcome> |

**Priority:** P<1|2|3>
**Type:** <Functional | UI | Navigation | Negative | Design System>

---
```

### Coverage checklist — write TCs for every section found on the page

- [ ] Navigation to the page
- [ ] Page layout and section headings
- [ ] All filter/category options (one TC per option)
- [ ] Search (positive, partial, negative / empty result, clear)
- [ ] Sort options (one TC per option)
- [ ] Each interactive element (buttons, dropdowns, checkboxes)
- [ ] Active filter tags (appear, remove one, clear all)
- [ ] Pagination (next, previous, direct page number)
- [ ] Empty / no-results state (assert exact message text from live page)
- [ ] Combined scenarios (filter + search together)
- [ ] Design System compliance (checkbox, dropdown, button styles) — P3
- [ ] For video pages: play inline, title links to YouTube, stats display
- [ ] For form pages: valid input, invalid input, required field validation

### Priority assignment

| Priority | Use when |
|---|---|
| P1 | Core user flow — navigation, primary action, happy path, empty state |
| P2 | Secondary behavior — UI elements, count verification, combined scenarios |
| P3 | Design System compliance, edge cases, rarely-used options |

### Update test_planning.md after creating TCs

- If this is a **new feature**: add it to In Scope and create a new Epic or add stories to an existing one
- If previously **Out of Scope**: move it to In Scope, note the ticket that drove the change
- Add new stories to the relevant Epic's story table
- Update the **Test Priority Matrix** if the module changes priority

---

## Phase 4 — Automation

Only start automation **after** manual test cases are written and complete.

### Automation file locations (mirror Manual_Tests structure)

```
base_pages/pages/<Module>_Pages/<Feature>_page.py      ← Page Object
test_cases/tests/<Module>_Tests/<Feature>_test.py      ← Test Script
test_data/<feature>.json                               ← Test Data
```

### Which manual TCs to automate

| Manual TC type | Automate? |
|---|---|
| P1 Functional | Always |
| P2 Functional | Yes, if stable (no hover-only or animation-only assertions) |
| P2 UI | Yes, if element presence / text can be asserted via Selenium |
| P3 Design System | Skip — visual only, requires screenshot diff tools |
| Negative / empty state | Yes — assert exact error message text from live page |

### Automation order

1. Navigation test (verifies page loads, URL, heading)
2. Happy-path / positive functional tests
3. Negative / empty-state tests
4. Filter, search, sort tests
5. Combined scenario tests
6. Pagination tests (only if enough data exists to paginate)

### Gap analysis (after automation)

Compare automated TCs against manual TCs:
- Mark each manual TC as: `AUTOMATED` / `SKIPPED (reason)` / `PENDING`
- Reasons to skip: visual-only, animation-only, flaky by nature, Design System, destructive data

---

## Quick Reference: Full Workflow Checklist

```
[ ] 1.  Read Planning/test_planning.md
[ ] 2.  Check: is the feature In Scope or Out of Scope?
[ ] 3.  Identify the Epic in test_planning.md that this ticket belongs to
[ ] 4.  Check existing stories — is this a new story or a fix to an existing one?
[ ] 5.  Read the Jira ticket (summary, description, attachments, comments)
[ ] 6.  Visit the live page at pro.repairsolutions.com
[ ] 7.  Record: navigation path, exact page heading, all sections, exact UI text
[ ] 8.  Determine: module folder name + feature_name in snake_case
[ ] 9.  Classify: New Feature / Bug / UI update / Content update
[ ] 10. Create or update Manual_Tests/<Module>/<feature_name>_test_cases.md
[ ] 11. Write TCs using TC_001 format — cover all sections from checklist
[ ] 12. Update Planning/test_planning.md (scope, epic stories, priority matrix)
[ ] 13. Create Page Object: base_pages/pages/<Module>_Pages/<Feature>_page.py
[ ] 14. Create Test Script: test_cases/tests/<Module>_Tests/<Feature>_test.py
[ ] 15. Add test data to test_data/ if needed
[ ] 16. Run tests locally (headed mode) to verify
[ ] 17. Perform gap analysis (manual vs automated)
```
