# Manual Test Cases — Home Page: Introduction Features

**Module:** Home Page  
**Feature:** Introduction Features — Interactive Animations  
**Priority:** P3 — Medium  
**Environment:** https://pro.repairsolutions.com  
**Precondition:** Navigate to the home page (no login required).

---

## Hover Modal Tests

## TC-HOME-001: Fix For DTC — Hover shows modal

**Description:** Verify that hovering over the "Fix For DTC" section reveals the modal with zoom animation.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to home page | Home page loads |
| 2 | Scroll down to "Fix For DTC" section | Section visible in viewport |
| 3 | Hover mouse over the Fix For DTC element | Modal/iPad overlay appears |
| 4 | Verify modal displayed | Modal is visible with zoom-out animation; `show` class present |

**Priority:** P3  
**Type:** UI / Animation  
**Note:** Flaky — re-test up to 2 times if hover doesn't trigger.

---

## TC-HOME-002: Repair Tips — Hover shows modal

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh home page | — |
| 2 | Scroll to "Repair Tips" section | Visible |
| 3 | Hover over Repair Tips element | Modal appears |
| 4 | Wait ~3 seconds | Modal fully visible with animation |

**Priority:** P3  
**Type:** UI / Animation

---

## TC-HOME-003: Vehicle Inspection Report — Hover shows modal

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh home page | — |
| 2 | Scroll to "Vehicle Inspection Report" section | Visible |
| 3 | Hover over element | Modal appears |
| 4 | Verify modal displayed | Zoom animation completes |

**Priority:** P3  
**Type:** UI / Animation

---

## Step Indicators Color Change

## TC-HOME-004: Step Indicator 1 — color changes on hover

**Description:** Verify step indicator 1 changes background color on hover.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Scroll to step indicators section | Indicators 1, 2, 3, 4 visible |
| 3 | Verify default background of indicator 1 | Color is `#d6e3f1` or `rgb(214, 227, 241)` |
| 4 | Hover over indicator 1 | Background changes |
| 5 | Verify new background | Contains `linear-gradient` with `rgb(106, 153, 204)` |

**Priority:** P3  
**Type:** UI / CSS

---

## TC-HOME-005: Step Indicator 2 — color changes on hover

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Verify default color of indicator 2 | `#d6e3f1` |
| 2 | Hover indicator 2 | Background changes to linear-gradient with `rgb(106, 153, 204)` |

**Priority:** P3 | **Type:** UI / CSS

---

## TC-HOME-006: Step Indicator 3 — color changes on hover

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Verify default color of indicator 3 | `#d6e3f1` |
| 2 | Hover indicator 3 | Background changes to linear-gradient with `rgb(106, 153, 204)` |

**Priority:** P3 | **Type:** UI / CSS

---

## TC-HOME-007: Step Indicator 4 — color changes on hover

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Verify default color of indicator 4 | `#d6e3f1` |
| 2 | Hover indicator 4 | Background changes to linear-gradient with `rgb(106, 153, 204)` |

**Priority:** P3 | **Type:** UI / CSS

---

## Device Animations

## TC-HOME-008: Three Device animation — tablet moves on hover

**Description:** Verify the three-device section animates on hover (tablet position changes).

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Scroll to three-device section | Three devices visible |
| 3 | Note tablet's `left` CSS position (default) | Position recorded |
| 4 | Hover over the device group | Animation triggers |
| 5 | Check tablet's `left` CSS position after hover | Value is different from default |

**Priority:** P3  
**Type:** UI / Animation

---

## TC-HOME-009: Mobile Device — zoom on hover

**Description:** Verify the mobile phone zooms in when hovered.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Refresh page | — |
| 2 | Scroll to mobile phone section | Mobile visible |
| 3 | Verify default transform | `matrix(1, 0, 0, 1, 0, 0)` or `none` |
| 4 | Hover over mobile device section | Zoom animation triggers |
| 5 | Verify new transform | `matrix(1.135, 0, 0, 1.135, 0, 0)` |

**Priority:** P3  
**Type:** UI / Animation

---

## General Navigation

## TC-HOME-010: "View All Products" button navigates to Products page

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Scroll to "Explore Our Award-Winning Products" section | Section visible |
| 2 | Click "View All Products" button | Navigates to Products page |

**Priority:** P3  
**Type:** Navigation

---

## TC-HOME-011: Hero "Learn More" CTA navigates correctly

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Locate "Learn More" link on hero banner | Link visible |
| 2 | Click "Learn More" | Navigates to relevant section or page |

**Priority:** P4  
**Type:** Navigation / Smoke
