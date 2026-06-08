# Manual Test Cases — Support: DTC Library

**Module:** Support  
**Feature:** DTC Library  
**Priority:** P2 — High  
**Environment:** https://pro.repairsolutions.com → Support → DTC Library  
**Precondition:** Navigate to DTC Library page via Support dropdown (login may not be required).

---

## TC-DTC-001: Search by Car Make and DTC Code — valid inputs

**Description:** Verify that searching with a valid Make and DTC code returns matching results.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Hover "Support" in navigation | Dropdown opens |
| 2 | Click "DTC Library" | DTC Library page loads |
| 3 | Click the Car Make selector | Dropdown/search input appears |
| 4 | Type make: `Toyota` | Filtered options appear |
| 5 | Press Enter or select "Toyota" | Make is selected |
| 6 | Enter DTC code: `P0300` in the code input | Code populated |
| 7 | Click "Search" button | Results table populates |
| 8 | Verify table columns | Make, Code, Description columns visible |
| 9 | Verify first row Make column | Contains "Toyota" or matches |

**Priority:** P2  
**Type:** Positive

---

## TC-DTC-002: Search results table displays correct columns

**Description:** Verify the results table has Make, Code, and Description columns.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Perform any valid search | Results shown |
| 2 | Inspect table headers | Make, Code, Description columns present |
| 3 | Inspect each row | Data populates all columns |
| 4 | Delete icon visible | Each row has a delete/clear icon in 4th column |

**Priority:** P2  
**Type:** UI

---

## TC-DTC-003: Clear All resets inputs

**Description:** Verify "Clear All" button resets the Make and DTC Code fields.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select a Make and enter a DTC code | Inputs populated |
| 2 | Click "Clear All" button | Make selector resets to default |
| 3 | Verify DTC Code field | Field is empty |
| 4 | Verify results table | Cleared or shows default state |

**Priority:** P2  
**Type:** Positive

---

## TC-DTC-004: Search with only Make (no DTC code)

**Description:** Verify behavior when only Make is selected without a DTC code.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select a Make: `Honda` | — |
| 2 | Leave DTC Code empty | — |
| 3 | Click "Search" | Results show all DTCs for Honda, OR search is blocked with message |

**Priority:** P3  
**Type:** Boundary

---

## TC-DTC-005: Search with only DTC Code (no Make)

**Description:** Verify behavior when only DTC code is entered without selecting a Make.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Leave Make unselected | — |
| 2 | Enter DTC code: `P0171` | — |
| 3 | Click "Search" | Results appear for all makes with that code, OR validation error shown |

**Priority:** P3  
**Type:** Boundary

---

## TC-DTC-006: Search with invalid DTC code

**Description:** Verify behavior for a non-existent DTC code.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select any Make | — |
| 2 | Enter invalid code: `ZZZZZ9999` | — |
| 3 | Click "Search" | No results shown OR "No results found" message |

**Priority:** P2  
**Type:** Negative

---

## TC-DTC-007: Delete icon removes a search result row

**Description:** Verify the delete icon on a result row removes that row.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Perform a valid search | Results shown |
| 2 | Note the first row content | — |
| 3 | Click the delete icon on the first row | Row is removed from table |
| 4 | Verify remaining rows | Other rows unaffected |

**Priority:** P3  
**Type:** Positive

---

## TC-DTC-008: Navigate to DTC Library via Support dropdown

**Description:** Verify DTC Library is accessible from the Support navigation dropdown.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Hover over "Support" in navigation | Dropdown menu appears |
| 2 | Verify "DTC Library" link visible | Visible in dropdown |
| 3 | Click "DTC Library" | DTC Library page loads correctly |

**Priority:** P2  
**Type:** Navigation
