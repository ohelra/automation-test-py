# Manual Test Cases — My Reports: Search

**Module:** My Reports  
**Feature:** Search Report  
**Priority:** P1 — Critical  
**Environment:** https://staging-app-pro.repairsolutions.innovavietnam.com/Report  
**Precondition:** User is logged in with `sangqa@yopmail.com / 12345678` and is on the My Reports page.

---

## TC-SEARCH-001: Search by vehicle make — valid keyword

**Description:** Verify the report table filters correctly when searching by vehicle make.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Locate the "Search report" input bar | Search bar visible |
| 2 | Type a vehicle keyword (e.g., `TOYOTA`) | Search bar populated |
| 3 | Wait for table to refresh (debounce ~1–2s) | Table updates |
| 4 | Inspect all rows in the Vehicle column | Every row contains "TOYOTA" (case-insensitive) |

**Test data:** RAM, TOYOTA, HYUNDAI, ACURA, CHRYSLER, CHEVROLET, DODGE, GMC, BMW, AUDI, FORD, NISSAN, MITSUBISHI, SUBARU  
**Priority:** P1  
**Type:** Positive / Data-driven

---

## TC-SEARCH-002: Search by report ID — valid ID

**Description:** Verify the report table filters correctly when searching by report ID.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Clear search bar | Cleared |
| 2 | Type a valid report ID (e.g., `46`) | Search bar populated |
| 3 | Wait for table to refresh | Table updates |
| 4 | Inspect all rows in the ID column | Every displayed ID contains the entered value |

**Test data:** 1, 3, 5, 10, 15, 29, 35, 46  
**Priority:** P1  
**Type:** Positive / Data-driven

---

## TC-SEARCH-003: Search by report type — valid type keyword

**Description:** Verify the report table filters correctly when searching by report type.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | Table shows all reports |
| 2 | Type type keyword (e.g., `OBD II`) | Search bar populated |
| 3 | Wait for table to refresh | Table updates |
| 4 | Inspect all rows in Type column | Every row matches the type keyword |

**Test data:** `OBD II`, `Diagnostic`, `Customer`, `Collision`  
**Priority:** P1  
**Type:** Positive / Data-driven

---

## TC-SEARCH-004: Search by customer name — valid keyword

**Description:** Verify the report table filters correctly when searching by customer name.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | Table reset |
| 2 | Enter a customer name that exists | Search bar populated |
| 3 | Wait for results | Table filters |
| 4 | Inspect all rows in Customer column | Every row contains the customer keyword |

**Priority:** P1  
**Type:** Positive

---

## TC-SEARCH-005: Search with invalid/non-existent keyword — "No reports found."

**Description:** Verify that searching with an invalid keyword shows "No reports found." message.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | Table shows all reports |
| 2 | Enter invalid keyword (e.g., `XYZXYZXYZ999`) | Search bar populated |
| 3 | Wait for results | Table updates |
| 4 | Verify table area | "No reports found." message is displayed |
| 5 | No data rows shown | Table is empty |

**Priority:** P1  
**Type:** Negative

---

## TC-SEARCH-006: Clear search restores full report list

**Description:** Verify clearing the search box restores all reports.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Type any keyword in search | Table filtered |
| 2 | Clear the search box (delete all text) | — |
| 3 | Wait for table to refresh | Full report list restored |
| 4 | Verify multiple rows visible | More than 1 row in table |

**Priority:** P2  
**Type:** Positive

---

## TC-SEARCH-007: Search is case-insensitive

**Description:** Verify search works regardless of letter case.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Search `toyota` (lowercase) | Results show "TOYOTA" rows |
| 2 | Clear and search `TOYOTA` (uppercase) | Same results as step 1 |
| 3 | Clear and search `Toyota` (mixed) | Same results |

**Priority:** P2  
**Type:** Boundary
