# Manual Test Cases — Products: Diagnostic Tools

**Module:** Products  
**Feature:** Diagnostic Tools Page (7111, SDS50, SDS43)  
**Priority:** P2 — High  
**Environment:** https://pro.repairsolutions.com → Products → Diagnostic Tools  
**Precondition:** Navigate to home page; user does NOT need to be logged in.

---

## 7111 — Smart Diagnostic System Tablet

## TC-DIAG-001: 7111 Grid View → Find a Store → Canadian store

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click "Products" in navigation | Dropdown appears |
| 2 | Click "Diagnostic Tools" | Diagnostic Tools page loads |
| 3 | Scroll to the 7111 tool card | 7111 card visible (Grid View) |
| 4 | Click "Find a store" button | Store selection popup/section opens |
| 5 | Click "Canadian" store option | New tab opens |
| 6 | Verify URL in new tab | URL contains `canadiantire.ca` |

**Priority:** P2  
**Type:** Positive / Navigation

---

## TC-DIAG-002: 7111 List View → Find a Store → Canadian store

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Diagnostic Tools page | Default Grid View |
| 2 | Click "List View" icon | View switches to list layout |
| 3 | Scroll to 7111 in list | 7111 row visible |
| 4 | Click "Find a store" | Store options shown |
| 5 | Click "Canadian" | New tab opens |
| 6 | Verify URL | Contains `canadiantire.ca` |

**Priority:** P2  
**Type:** Positive / Navigation

---

## TC-DIAG-003: 7111 Grid View → Find a Store → Auto Parts store

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Diagnostic Tools | Grid View |
| 2 | Scroll to 7111 card | — |
| 3 | Click "Find a store" | Store selection opens |
| 4 | Click "Auto Parts" / NAPA option | New tab opens |
| 5 | Verify URL | Contains `napa` |

**Priority:** P2  
**Type:** Positive / Navigation

---

## TC-DIAG-004: 7111 List View → Find a Store → Auto Parts store

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Diagnostic Tools → click List View | List View active |
| 2 | Scroll to 7111 | — |
| 3 | Click "Find a store" | Store options shown |
| 4 | Click Auto Parts | New tab opens |
| 5 | Verify URL | Contains `napa` |

**Priority:** P2  
**Type:** Positive / Navigation

---

## TC-DIAG-005: 7111 List View → Product Detail page

**Description:** Verify clicking Product Detail in List View navigates to the 7111 product page.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Diagnostic Tools → click List View | — |
| 2 | Locate 7111 entry | — |
| 3 | Click "Product Detail" / "View" button | Page navigates to 7111 product page |
| 4 | Verify page title/heading | "7111: Smart Diagnostic System Tablet" |

**Priority:** P2  
**Type:** Positive / Navigation

---

## SDS50 — Smart Diagnostic System Tech

## TC-DIAG-006: SDS50 Grid View → Find a Store → Auto Parts store

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Diagnostic Tools | Grid View |
| 2 | Scroll to SDS50 card | — |
| 3 | Click "Find a store" | Store options shown |
| 4 | Click "Auto Parts" | New tab opens |
| 5 | Verify URL | Contains `napa` |

**Priority:** P2  
**Type:** Positive / Navigation

---

## TC-DIAG-007: SDS50 List View → Find a Store → Auto Parts store

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Diagnostic Tools → List View | — |
| 2 | Scroll to SDS50 | — |
| 3 | Click "Find a store" | — |
| 4 | Click Auto Parts | New tab opens with `napa` URL |

**Priority:** P2  
**Type:** Positive / Navigation

---

## TC-DIAG-008: SDS50 List View → Product Detail page

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Diagnostic Tools → List View | — |
| 2 | Scroll to SDS50 | — |
| 3 | Click "Product Detail" | SDS50 product page loads |
| 4 | Verify page title | "SDS50: Smart Diagnostic System Tech" |

**Priority:** P2  
**Type:** Positive / Navigation

---

## SDS43 — Smart Diagnostic System Inspector

## TC-DIAG-009: SDS43 Grid View → Find a Store → Auto Parts store

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Diagnostic Tools | Grid View |
| 2 | Scroll to SDS43 | — |
| 3 | Click "Find a store" | — |
| 4 | Click Auto Parts | New tab with `napa` URL |

**Priority:** P2  
**Type:** Positive / Navigation

---

## TC-DIAG-010: SDS43 List View → Find a Store → Auto Parts store

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Diagnostic Tools → List View | — |
| 2 | Scroll to SDS43 | — |
| 3 | Click "Find a store" | — |
| 4 | Click Auto Parts | New tab with `napa` URL |

**Priority:** P2  
**Type:** Positive / Navigation

---

## TC-DIAG-011: SDS43 List View → Product Detail page

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Diagnostic Tools → List View | — |
| 2 | Scroll to SDS43 | — |
| 3 | Click "Product Detail" | SDS43 product page loads |
| 4 | Verify page title | "SDS43: Smart Diagnostic System Inspector" |

**Priority:** P2  
**Type:** Positive / Navigation

---

## TC-DIAG-012: Grid View to List View toggle

**Description:** Verify switching between Grid and List view updates the layout correctly.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Diagnostic Tools | Grid View is default |
| 2 | Click List View icon | Layout changes to list format |
| 3 | Click Grid View icon | Layout returns to card/grid format |

**Priority:** P3  
**Type:** UI

---

## TC-DIAG-013: Store links open in new tab

**Description:** Verify all store links open in a new browser tab.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click "Find a store" for any tool | Store options shown |
| 2 | Click any store link | New tab opens |
| 3 | Original page remains open | Previous tab unchanged |

**Priority:** P2  
**Type:** Positive / UI
