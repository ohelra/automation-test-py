# Manual Test Cases — Support: How-to Videos

**Module:** Support
**Feature:** How-to Videos
**Ticket:** RWR-266 — Update How To Videos Page
**Priority:** P2 — High
**Environment:** https://pro.repairsolutions.com → Support → How-to Videos
**Precondition:** User is on the RSPRO homepage. Login may not be required to view videos.

---

## TC_001: Navigate to How-to Videos page via Support menu

**Description:** Verify user can reach the How-to Videos page from the navigation.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Go to https://pro.repairsolutions.com | Homepage loads |
| 2 | Hover over "Support" in the top navigation | Dropdown menu appears |
| 3 | Click "How-to Videos" | How-to Videos page loads |
| 4 | Verify page URL | Contains `/Support/HowToVideos` |
| 5 | Verify page heading | "How-to Videos" heading is visible |
| 6 | Verify page description | "Watch our step-by-step videos and get the guided assistance you need." is displayed |

**Priority:** P1
**Type:** Navigation

---

## TC_002: Page layout — 2-column featured video section

**Description:** Verify the "Get More Information from Our Videos" section renders with correct 2-column layout.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Page loads |
| 2 | Scroll to the featured video section | Section is visible |
| 3 | Verify left column | A large featured video is displayed |
| 4 | Verify right column | A list of related videos appears next to the featured video |
| 5 | Verify layout proportions | Left (featured) column is larger than right (list) column |

**Priority:** P2
**Type:** UI / Layout

---

## TC_003: Featured video — click to play inline

**Description:** Verify the featured video plays inline on the page when clicked.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Page loads with featured video visible |
| 2 | Identify the featured video on the left column | Video thumbnail is displayed with play indicator |
| 3 | Click the video / play button | Video starts playing inline on the page |
| 4 | Observe playback | Video plays without redirecting to YouTube |

**Priority:** P1
**Type:** Functional

---

## TC_004: Featured video — title links to YouTube

**Description:** Verify clicking the video title opens the YouTube page in a new tab.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Featured video with title visible |
| 2 | Click the title text of the featured video | YouTube page opens in a new browser tab |
| 3 | Verify new tab URL | Contains `youtube.com` or `youtu.be` |
| 4 | Close the new tab | Return to How-to Videos page |

**Priority:** P2
**Type:** Functional

---

## TC_005: Featured video — YouTube stats displayed

**Description:** Verify likes, views, and share counts sourced from YouTube are shown.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Featured video section visible |
| 2 | Inspect the featured video area | Like count is displayed |
| 3 | Verify view count | View count is visible |
| 4 | Verify share option | Share button or count is visible |

**Priority:** P2
**Type:** UI

---

## TC_006: Video card display — thumbnail, duration, title

**Description:** Verify each video card shows a thumbnail image, duration, and title.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Video list is visible |
| 2 | Inspect any video card | Thumbnail/preview image is displayed |
| 3 | Verify duration indicator | Time (e.g., "2:34") is shown on or below the thumbnail |
| 4 | Verify title text | Video title is visible below/beside the thumbnail |

**Priority:** P2
**Type:** UI

---

## TC_007: Video in list — click to play

**Description:** Verify clicking a video in the list plays it.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Video list visible |
| 2 | Click any video card | Video plays inline or featured video updates to selected video |

**Priority:** P1
**Type:** Functional

---

## TC_008: Category filter — All shows all videos

**Description:** Verify selecting "All" category displays all available videos.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Page loads |
| 2 | Locate the Categories section in the sidebar | Categories list visible |
| 3 | Click "All" checkbox | "All" is selected |
| 4 | Verify video list | All videos across all categories are displayed |
| 5 | Verify total count | Matches total number beside "All" label |

**Priority:** P1
**Type:** Functional

---

## TC_009: Category filter — How-to Videos

**Description:** Verify selecting "How-to Videos" category filters the list correctly.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Page loads |
| 2 | Click "How-to Videos" checkbox in Categories | Checkbox is checked |
| 3 | Verify video list updates | Only "How-to Videos" category videos are shown |
| 4 | Verify count | Number of results matches count next to the category label |

**Priority:** P1
**Type:** Functional

---

## TC_010: Category filter — How-to Fix

**Description:** Verify selecting "How-to Fix" category filters the list correctly.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Page loads |
| 2 | Click "How-to Fix" checkbox in Categories | Checkbox is checked |
| 3 | Verify video list updates | Only "How-to Fix" category videos are shown |
| 4 | Verify count | Matches count next to "How-to Fix" |

**Priority:** P1
**Type:** Functional

---

## TC_011: Category filter — How-to Use

**Description:** Verify selecting "How-to Use" category filters the list correctly.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Page loads |
| 2 | Click "How-to Use" checkbox in Categories | Checkbox is checked |
| 3 | Verify video list updates | Only "How-to Use" category videos are shown |
| 4 | Verify count | Matches count next to "How-to Use" |

**Priority:** P1
**Type:** Functional

---

## TC_012: Category — each item shows checkbox, name, and video count

**Description:** Verify each category item renders with all three UI elements per Design System spec.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Categories sidebar visible |
| 2 | Inspect each category row | Checkbox component is present (not a plain HTML checkbox) |
| 3 | Verify category name text | Name label is visible and readable |
| 4 | Verify video count | Number shown in parentheses or beside name |

**Priority:** P2
**Type:** UI

---

## TC_013: Category — selecting one deselects others (single select behavior)

**Description:** Verify that selecting a new category updates the filter (only one active at a time unless multi-select is intended).

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click "How-to Fix" in Categories | How-to Fix is selected, videos filtered |
| 2 | Click "How-to Use" | How-to Use is selected |
| 3 | Observe "How-to Fix" state | Behavior reflects single or multi-select per spec |
| 4 | Verify video list | Updates to reflect current selection |

**Priority:** P2
**Type:** Functional

---

## TC_014: Popular Topics — selecting a topic filters videos

**Description:** Verify Popular Topics sidebar filters the video list when a topic is selected.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Popular Topics sidebar visible |
| 2 | Click any topic checkbox | Topic is selected |
| 3 | Verify video list | Filtered to show only videos matching that topic |
| 4 | Verify topic count | Matches number beside the topic label |

**Priority:** P1
**Type:** Functional

---

## TC_015: Popular Topics — checkbox, name, count UI

**Description:** Verify each Popular Topic item shows checkbox, name, and count per Design System spec.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Popular Topics sidebar visible |
| 2 | Inspect each topic row | Checkbox component visible |
| 3 | Verify name label | Readable topic name shown |
| 4 | Verify count | Number of videos in that topic shown |

**Priority:** P2
**Type:** UI

---

## TC_016: Active filters — tag appears when filter is selected

**Description:** Verify an active filter tag appears when user selects a category or topic.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | No active filters shown |
| 2 | Click any category (e.g., "How-to Fix") | Active filter tag "How-to Fix" appears in the filter bar |
| 3 | Verify tag appearance | Tag shows filter name with a close (×) icon |

**Priority:** P1
**Type:** UI / Functional

---

## TC_017: Active filters — remove single filter via × icon

**Description:** Verify clicking the × icon on a filter tag removes only that filter.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select two filters (one category + one topic) | Two active filter tags visible |
| 2 | Click × on the first filter tag | First filter removed, video list updates |
| 3 | Verify second filter tag | Still present and active |
| 4 | Verify video list | Filtered only by remaining active filter |

**Priority:** P1
**Type:** Functional

---

## TC_018: Active filters — Clear All button appears only when filter is active

**Description:** Verify "Clear All" button is hidden when no filters active, visible when filters active.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page with no filters | "Clear All" button is NOT visible |
| 2 | Select any category | Active filter tag appears |
| 3 | Verify "Clear All" button | Now visible in the filter bar |
| 4 | Observe button style | Follows Design System Action Button spec |

**Priority:** P2
**Type:** UI

---

## TC_019: Active filters — Clear All removes all filters

**Description:** Verify "Clear All" clears every active filter and restores full video list.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Select one or more categories and/or topics | Multiple active filter tags visible |
| 2 | Click "Clear All" button | All filter tags removed |
| 3 | Verify filter sidebar | All checkboxes deselected |
| 4 | Verify video list | Full unfiltered list restored |
| 5 | Verify "Clear All" button | No longer visible |

**Priority:** P1
**Type:** Functional

---

## TC_020: Search — search with matching keyword returns results

**Description:** Verify the search bar filters videos by keyword.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Search bar visible |
| 2 | Type a keyword that matches a known video title | Search results update |
| 3 | Verify video list | Shows only videos whose title contains the keyword |
| 4 | Verify search input | Typed keyword visible in search field |

**Priority:** P1
**Type:** Functional

---

## TC_021: Search — partial keyword returns relevant results

**Description:** Verify partial keyword search still returns matching videos.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Type first 3+ characters of a known video title | Results begin filtering |
| 2 | Verify list | Shows videos containing those characters in title |

**Priority:** P2
**Type:** Functional

---

## TC_022: Search — no matching keyword shows "There is no record found"

**Description:** Verify the empty state message appears when search returns no results.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Page loads |
| 2 | Type a keyword that matches no video (e.g., `ZZZZNOTEXIST`) | No results match |
| 3 | Verify empty state | "There is no record found" message is displayed |
| 4 | Verify video list area | No video cards shown |

**Priority:** P1
**Type:** Negative

---

## TC_023: Search — clear search input restores full list

**Description:** Verify clearing the search field restores all videos.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Type a keyword in search | Filtered results shown |
| 2 | Delete the text in search field (or click clear icon) | Input is empty |
| 3 | Verify video list | All videos restored |

**Priority:** P2
**Type:** Functional

---

## TC_024: Sort by — Popular

**Description:** Verify selecting "Popular" sort orders videos by popularity.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Video list visible |
| 2 | Open the "Sort by" dropdown | Options shown: Popular, Latest (and Oldest if available) |
| 3 | Select "Popular" | Dropdown closes, selection shows "Popular" |
| 4 | Verify video list order | Videos sorted by highest view/engagement count first |

**Priority:** P2
**Type:** Functional

---

## TC_025: Sort by — Latest

**Description:** Verify selecting "Latest" sort orders videos by most recently uploaded.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Sort by dropdown visible |
| 2 | Select "Latest" | Dropdown shows "Latest" selected |
| 3 | Verify video list | Most recently uploaded video appears first |

**Priority:** P2
**Type:** Functional

---

## TC_026: Sort by — Oldest

**Description:** Verify selecting "Oldest" sort orders videos by oldest upload date.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Sort by dropdown visible |
| 2 | Open dropdown | "Oldest" option present |
| 3 | Select "Oldest" | Dropdown shows "Oldest" selected |
| 4 | Verify video list | Oldest uploaded video appears first |

**Priority:** P3
**Type:** Functional

---

## TC_027: Pagination — navigate to next page

**Description:** Verify pagination allows user to go to the next page of results.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page with enough videos to paginate | Pagination controls visible |
| 2 | Click the "Next" (>) button | Next page of videos loads |
| 3 | Verify URL or page indicator | Page 2 is indicated |
| 4 | Verify video list | Different set of videos shown |

**Priority:** P2
**Type:** Functional

---

## TC_028: Pagination — navigate to previous page

**Description:** Verify pagination allows user to go back to the previous page.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to page 2 via pagination | Page 2 loaded |
| 2 | Click "Previous" (<) button | Page 1 loads |
| 3 | Verify page indicator | Shows page 1 active |

**Priority:** P2
**Type:** Functional

---

## TC_029: Pagination — click page number directly

**Description:** Verify user can jump to a specific page by clicking its page number.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Ensure multiple pages of videos exist | Pagination shows page numbers |
| 2 | Click page number "3" (or any available) | Page 3 loads |
| 3 | Verify active page indicator | Page 3 is highlighted/active |
| 4 | Verify video list | Page 3 video set is displayed |

**Priority:** P2
**Type:** Functional

---

## TC_030: No results state — message and empty layout

**Description:** Verify the "no results" state is handled gracefully.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Apply a filter or search with no matching results | Video list area is empty |
| 2 | Verify empty state message | "There is no record found" message displayed |
| 3 | Verify layout | No broken layout or JS errors |
| 4 | Verify pagination | Pagination hidden or shows 0 results |

**Priority:** P1
**Type:** Negative / UI

---

## TC_031: Combined filter + search — results reflect both conditions

**Description:** Verify applying a category filter AND a search keyword together narrows results correctly.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to How-to Videos page | Page loads |
| 2 | Select category "How-to Fix" | Videos filtered by category |
| 3 | Type a keyword in the search bar | Results filtered further |
| 4 | Verify video list | Only videos matching BOTH the category and keyword are shown |
| 5 | Verify active filter tag | Category tag still visible in filter bar |

**Priority:** P1
**Type:** Functional

---

## TC_032: Sort by dropdown — follows Design System Dropdown component

**Description:** Verify Sort By dropdown is styled and behaves per Design System Dropdown spec.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click Sort by dropdown | Dropdown opens with option list |
| 2 | Verify dropdown appearance | Matches Design System Dropdown / Dropdown-option list style |
| 3 | Select an option | Dropdown closes, selected value shown |
| 4 | Click dropdown again without selecting | Closes without changing selection |

**Priority:** P3
**Type:** UI / Design System

---

## TC_033: Search bar — follows Design System Search Bar component

**Description:** Verify the search bar component matches Design System Search Bar spec.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Inspect the search bar | Search icon visible within the input |
| 2 | Click the search bar | Focused state shown (outline/highlight) |
| 3 | Verify placeholder text | Appropriate placeholder (e.g., "Search...") displayed |
| 4 | Verify overall styling | Matches Design System Search Bar component |

**Priority:** P3
**Type:** UI / Design System

---

## TC_034: Category checkboxes — follow Design System Checkbox component

**Description:** Verify category and topic checkboxes match Design System Checkbox spec.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Inspect unchecked category checkbox | Renders per Design System (border, size, color) |
| 2 | Click checkbox | Checked state shows correct checkmark and style |
| 3 | Click again | Unchecked state restores correctly |
| 4 | Hover over checkbox | Hover state matches Design System spec |

**Priority:** P3
**Type:** UI / Design System
   
---

*Total: 34 test cases*
*Generated from Jira ticket RWR-266 — Update How To Videos Page*
*Tester: QA — Huynh Quoc Thang*

