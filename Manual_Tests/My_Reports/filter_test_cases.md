# Manual Test Cases — My Reports: Filter

**Module:** My Reports  
**Feature:** Filter Reports  
**Priority:** P1 — Critical  
**Environment:** https://staging-app-pro.repairsolutions.innovavietnam.com/Report  
**Precondition:** User is logged in and on the My Reports page.

---

## Date Picker Filter

## TC-FILTER-001: Filter by valid date range (From – To)

**Description:** Verify that filtering by a date range returns only reports within that range.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click "Filter" button | Filter panel expands |
| 2 | Enter From date: `01/10/2026` | From date field populated |
| 3 | Enter To date: `01/27/2026` | To date field populated |
| 4 | Wait for table to update | Table refreshes |
| 5 | Inspect Date and Time column for each row | Every date is between 01/10/2026 and 01/27/2026 (inclusive) |

**Priority:** P1  
**Type:** Positive

---

## TC-FILTER-002: Filter with From date only

**Description:** Verify behavior when only From date is provided.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click "Filter" button | Filter panel opens |
| 2 | Enter From date: `01/01/2026` | — |
| 3 | Leave To date empty | — |
| 4 | Wait for table update | Reports on or after 01/01/2026 are shown, OR all reports shown |

**Priority:** P3  
**Type:** Boundary

---

## TC-FILTER-003: Filter with To date only

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click "Filter" button | — |
| 2 | Leave From date empty | — |
| 3 | Enter To date: `01/31/2026` | — |
| 4 | Wait for table update | Reports on or before 01/31/2026 shown, OR all reports shown |

**Priority:** P3  
**Type:** Boundary

---

## TC-FILTER-004: Filter with From date after To date

**Description:** Verify the system handles an invalid date range gracefully.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click "Filter" | — |
| 2 | Enter From: `01/31/2026`, To: `01/01/2026` | — |
| 3 | Wait for table update | "No reports found." OR validation error shown |

**Priority:** P2  
**Type:** Negative

---

## Type Filter

## TC-FILTER-005: Filter by Type — OBD II

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | Full report list |
| 2 | Click "Filter" | Filter panel opens |
| 3 | Click "OBD II" type button | Button activates (highlighted) |
| 4 | Inspect Type column | Every row shows "OBD II" |

**Priority:** P1  
**Type:** Positive

---

## TC-FILTER-006: Filter by Type — Diagnostic

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Click "Filter" → Click "Diagnostic" | Diagnostic button active |
| 3 | Inspect Type column | Every row shows "Diagnostic" |

**Priority:** P1  
**Type:** Positive

---

## TC-FILTER-007: Filter by Type — Customer

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Click "Filter" → Click "Customer" | Customer button active |
| 3 | Inspect Type column | Every row shows "Customer" |

**Priority:** P1  
**Type:** Positive

---

## TC-FILTER-008: Filter by Type — Collision

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Click "Filter" → Click "Collision" | Collision button active |
| 3 | Inspect Type column | Every row shows "Collision" |

**Priority:** P1  
**Type:** Positive

---

## TC-FILTER-009: Filter by Type — Sample

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Click "Filter" → Click "Sample" | Sample button active |
| 3 | Inspect Type column | Every row shows "Sample" |

**Priority:** P2  
**Type:** Positive

---

## Tool Filter

## TC-FILTER-010: Filter by Tool — 7111

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | Full report list |
| 2 | Click "Filter" → Click "7111" tool | Tool button active |
| 3 | Inspect Tool column | Every row shows "7111" |

**Priority:** P1  
**Type:** Positive

---

## TC-FILTER-011: Filter by Tool — SDS43

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Click "Filter" → Click "SDS43" | — |
| 3 | Inspect Tool column | Every row shows "SDS43" |

**Priority:** P1  
**Type:** Positive

---

## TC-FILTER-012: Filter by Tool — SDS50

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Click "Filter" → Click "SDS50" | — |
| 3 | Inspect Tool column | Every row shows "SDS50" |

**Priority:** P1  
**Type:** Positive

---

## Clear Filter

## TC-FILTER-013: Clear All resets active filters

**Description:** Verify Clear button removes all active filter selections.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Click "Filter" | Panel opens |
| 3 | Click "Diagnostic" type | Diagnostic button active/highlighted |
| 4 | Verify type active indicator visible | Active button displayed |
| 5 | Click "Clear" button | All active filter buttons deactivated |
| 6 | Verify no active filter remains | No type or tool button is highlighted |

**Priority:** P1  
**Type:** Positive

---

## TC-FILTER-014: Combine Type + Tool filter

**Description:** Verify applying both a type and a tool filter returns correct combined results.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click "Filter" | — |
| 2 | Click "OBD II" type | — |
| 3 | Click "7111" tool | — |
| 4 | Inspect table | All rows show Type=OBD II AND Tool=7111 |

**Priority:** P2  
**Type:** Positive / Integration
