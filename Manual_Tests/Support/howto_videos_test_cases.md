# Manual Test Cases — Support: How-to Videos

**Module:** Support
**Feature:** How-to Videos
**Environment:** https://pro.repairsolutions.com/Support/HowtoVideos
**Precondition:** User is on any page of the RepairSolutionsPRO website. No login required.

---

## TC_001: Navigate to How-to Videos via Support menu

**Description:** Verify the How-to Videos page is accessible from the Support dropdown menu.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Hover over "Support" in the top navigation bar | Support dropdown menu expands |
| 2 | Click "How-to Videos" from the dropdown | Page navigates to /Support/HowtoVideos |
| 3 | Observe the page heading | "How-to Videos" heading is displayed |

**Priority:** P1
**Type:** Navigation

---

## TC_002: Verify video cards are present on the page

**Description:** Verify that the How-to Videos page displays at least one video card.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to /Support/HowtoVideos | Page loads |
| 2 | Observe the video grid | At least 1 video card is visible |
| 3 | Verify each card has a thumbnail, play button, and title | All elements are visible per card |

**Priority:** P1
**Type:** UI

---

## TC_003: Play each video for 3 seconds then pause

**Description:** Verify that clicking each video thumbnail plays the video and it can be paused after 3 seconds.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to /Support/HowtoVideos | Page loads with video grid |
| 2 | For each video card, click the play button/thumbnail | YouTube player activates and video begins playing |
| 3 | Wait 3 seconds | Video plays for 3 seconds (currentTime > 0) |
| 4 | Click pause or use keyboard shortcut | Video pauses |
| 5 | Verify video state | Video is paused (paused = true) |

**Priority:** P1
**Type:** Functional

---

## TC_004: Verify video titles are descriptive and non-empty

**Description:** Verify that each video card displays a non-empty title.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to /Support/HowtoVideos | Page loads |
| 2 | Observe each video card | Each card displays a visible title text |
| 3 | Verify no title is empty or shows placeholder text | All titles are meaningful and non-empty |

**Priority:** P2
**Type:** UI

---

## TC_005: Verify "Watch on YouTube" link opens YouTube in a new tab

**Description:** Verify that the "View on YouTube" / "Xem tren YouTube" link on each card opens YouTube in a new tab.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to /Support/HowtoVideos | Page loads |
| 2 | Click the "Watch on YouTube" link on any video card | A new browser tab opens |
| 3 | Observe the new tab URL | URL contains youtube.com or youtu.be |
| 4 | Close the new tab | Returns to How-to Videos page |

**Priority:** P2
**Type:** Functional
