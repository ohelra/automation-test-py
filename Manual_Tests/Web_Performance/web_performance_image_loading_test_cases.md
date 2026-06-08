# Manual Test Cases — Web Performance: Image Upload Pipeline & Loading Speed

**Module:** Web_Performance
**Feature:** Image Upload Pipeline & Legacy Image Migration
**Ticket:** RWR-588 — Web Performance (Image and Loading Speed)
**Epic:** Enhancement — Image Pipeline Optimization (AWS Lambda + S3)
**Priority:** P1 — High (infrastructure change with direct user-facing impact)
**Environment:**
- Consumer Web: https://staging-app-pro.repairsolutions.innovavietnam.com
- Admin Portal: (Admin staging URL — confirm with Dev team)
**Precondition:** Staging environment has been deployed with the new image pipeline. Test accounts available for Consumer Web and Admin.

---

## TASK 1 — Image Upload Pipeline (Consumer Web)

---

## TC-WP-001: Upload JPG image → verify converted to WebP

**Description:** Verify that uploading a `.jpg` image on Consumer Web automatically converts it to `.webp` format.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Log in to Consumer Web with valid credentials | Dashboard loads |
| 2 | Navigate to a page that supports image upload (confirm location with Dev team) | Upload area is visible |
| 3 | Click the upload button | File picker dialog opens |
| 4 | Select a valid `.jpg` image file (< max size limit) | File selected |
| 5 | Submit / confirm upload | Upload completes without error |
| 6 | Inspect the uploaded image URL (right-click → Copy Image Address) | URL ends with `.webp` extension |
| 7 | Verify image displays correctly in the UI | Image renders without distortion or broken icon |

**Priority:** P1
**Type:** Functional — Positive

---

## TC-WP-002: Upload PNG image → verify converted to WebP

**Description:** Verify that uploading a `.png` image automatically converts it to `.webp`.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Log in to Consumer Web | Dashboard loads |
| 2 | Navigate to an image upload area | Upload control visible |
| 3 | Select a valid `.png` file | File selected |
| 4 | Confirm upload | Upload completes without error |
| 5 | Inspect the resulting image URL | URL ends with `.webp` |
| 6 | Verify image displays correctly | Image renders properly |

**Priority:** P1
**Type:** Functional — Positive

---

## TC-WP-003: Upload image already in WebP format → no double-conversion, no error

**Description:** Verify that uploading a `.webp` image does not cause errors or re-conversion issues.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Log in to Consumer Web | Dashboard loads |
| 2 | Navigate to image upload area | Upload control visible |
| 3 | Select a valid `.webp` file | File selected |
| 4 | Confirm upload | Upload completes without error |
| 5 | Inspect the resulting image URL | URL ends with `.webp` (unchanged format) |
| 6 | Verify image displays correctly | Image renders properly, no corruption |

**Priority:** P2
**Type:** Functional — Boundary

---

## TC-WP-004: Upload oversized image → validation error shown

**Description:** Verify that uploading an image exceeding the maximum allowed file size is blocked with a clear error message.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Log in to Consumer Web | Dashboard loads |
| 2 | Navigate to image upload area | Upload control visible |
| 3 | Attempt to upload an image file exceeding max size limit (e.g., > 10MB — confirm limit with Dev) | Upload is rejected |
| 4 | Observe error feedback | Error message is shown explaining the file size limit |
| 5 | Verify no broken or partial image is stored | No image uploaded; UI returns to upload-ready state |

**Priority:** P1
**Type:** Negative — Validation

---

## TC-WP-005: Upload unsupported file format → validation error shown

**Description:** Verify that uploading a non-image file (PDF, TXT, SVG, etc.) is rejected with a clear error.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Log in to Consumer Web | Dashboard loads |
| 2 | Navigate to image upload area | Upload control visible |
| 3 | Attempt to upload a `.pdf` file | Upload is rejected |
| 4 | Observe error feedback | Error message indicates unsupported file type |
| 5 | Repeat with `.txt` file | Same validation error appears |
| 6 | Verify no file is stored | UI returns to clean upload state |

**Priority:** P1
**Type:** Negative — Validation

---

## TC-WP-006: Uploaded image is auto-resized within expected dimensions

**Description:** Verify that uploaded images are resized according to the configured dimensions spec (confirm max dimensions with Dev team before executing).

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Log in to Consumer Web | Dashboard loads |
| 2 | Navigate to image upload area | Upload control visible |
| 3 | Upload a high-resolution image (e.g., 4000x3000px) | Upload completes |
| 4 | Right-click the displayed image → Open image in new tab | Image opens directly |
| 5 | Check image dimensions (DevTools → Inspector → naturalWidth / naturalHeight) | Dimensions are within spec (confirm max dimensions with Dev) |
| 6 | Verify image quality is acceptable | No visible pixelation or distortion |

**Priority:** P2
**Type:** Functional — Boundary

---

## TC-WP-007: File size is reduced after upload (WebP compression)

**Description:** Verify that the stored image file size is smaller than the original uploaded file, confirming WebP compression is applied.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Note the original file size of the image to be uploaded (e.g., 2.5 MB JPG) | Original size recorded |
| 2 | Upload the image on Consumer Web | Upload completes |
| 3 | Open the uploaded image URL in a new tab | Image opens |
| 4 | In DevTools → Network tab → find the image request → check response size | Response size is noticeably smaller than the original |
| 5 | Compare sizes | Stored WebP size < original JPG/PNG size |

**Priority:** P2
**Type:** Functional — Performance

---

## TASK 1 — Image Upload Pipeline (Admin Platform)

---

## TC-WP-008: Admin — Upload JPG/PNG → verify converted to WebP

**Description:** Verify image upload pipeline on Admin platform applies the same WebP conversion as Consumer Web.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Log in to Admin portal with admin credentials | Admin dashboard loads |
| 2 | Navigate to any content area that supports image upload (article, product image, banner, etc.) | Upload control is available |
| 3 | Upload a `.jpg` image | Upload completes without error |
| 4 | Inspect the stored/displayed image URL | URL ends with `.webp` |
| 5 | Repeat with `.png` image | Same conversion applied |
| 6 | Verify images display correctly in Admin UI | Images render without errors |

**Priority:** P1
**Type:** Functional — Positive

---

## TC-WP-009: Admin — Upload oversized or invalid file → validation matches Consumer Web

**Description:** Verify Admin upload validation is consistent with Consumer Web (same rules, same error messages).

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Log in to Admin portal | Admin dashboard loads |
| 2 | Navigate to an image upload area | Upload control visible |
| 3 | Attempt to upload an oversized image | Error shown — matches Consumer Web validation |
| 4 | Attempt to upload unsupported format (PDF) | Error shown — matches Consumer Web validation |

**Priority:** P2
**Type:** Negative — Consistency

---

## TASK 3 — Legacy Image Migration: Consumer Web Verification

---

## TC-WP-010: Migrated images display correctly on article pages

**Description:** Verify that all images in rich-text article pages display correctly after the legacy migration (no broken images).

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Technical Center → Emerging Technologies | Article list loads |
| 2 | Open each of the 5 articles | Article pages load |
| 3 | For each article, scroll through entire page content | All inline images render correctly — no broken icons |
| 4 | Open image URL in new tab (right-click → Open image in new tab) | Image loads successfully (HTTP 200) |

**Priority:** P1
**Type:** Functional — Post-Migration Verification

---

## TC-WP-011: Migrated standalone images display correctly (avatar, thumbnail, banner)

**Description:** Verify that standalone image fields (user avatars, product thumbnails, page banners) display correctly after migration.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Log in to Consumer Web | Dashboard loads |
| 2 | Navigate to Profile / Account settings if available | Profile page loads |
| 3 | Verify profile picture / avatar loads | Image renders correctly, no broken icon |
| 4 | Navigate to Products page | Page loads |
| 5 | Verify all product thumbnail images | All product images render correctly |
| 6 | Navigate to Homepage | Page loads |
| 7 | Verify all banner / hero images | Banner images render correctly |

**Priority:** P1
**Type:** Functional — Post-Migration Verification

---

## TC-WP-013: No broken images anywhere on key pages after migration

**Description:** Full page scan of key pages to confirm zero broken image icons after migration.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Homepage | Page loads |
| 2 | Scroll through entire homepage | No broken image icons visible |
| 3 | Navigate to Products page → each product detail page (7111, SDS50, SDS43, BA200) | Each page loads |
| 4 | Scroll through all product detail sections | No broken image icons |
| 5 | Navigate to Technical Center → all 5 articles | Pages load |
| 6 | Scroll through all article content | No broken image icons |
| 7 | Navigate to Support pages | Pages load |
| 8 | Scan all pages for broken icons | Zero broken image icons across all pages |

**Priority:** P1
**Type:** Functional — Regression

---

## TC-WP-015: Image count and content integrity — articles look identical before and after migration

**Description:** Verify that articles display the same number of images and the same visual content after migration (no missing images, no wrong images).

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Before migration: take screenshots of 3 articles and record image count per article | Baseline screenshots + image counts captured |
| 2 | After migration: navigate to the same 3 articles | Pages load |
| 3 | Compare screenshot before/after | Same number of images in same positions |
| 4 | Compare image content visually | Images appear visually identical to pre-migration baseline |
| 5 | Check no images are swapped (wrong image in wrong place) | All images match their pre-migration positions and content |

**Priority:** P1
**Type:** Functional — Data Integrity

---

## TC-WP-017: Images load via HTTPS — no mixed content warnings

**Description:** Verify that all image requests are HTTPS and do not trigger browser mixed content warnings.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Homepage on staging (HTTPS) | Page loads |
| 2 | Open DevTools → Console tab | Console visible |
| 3 | Reload the page | Page reloads |
| 4 | Check Console for mixed content warnings | Zero "Mixed Content" warnings in Console |
| 5 | Open DevTools → Network → filter Images | All image request URLs start with `https://` |
| 6 | Repeat on an article page with many images | Same result — no mixed content warnings |

**Priority:** P1
**Type:** Security / Infrastructure

---

## TASK 4 — Performance Verification (Lighthouse)

---

## TC-WP-019: Lighthouse Performance score on Homepage meets target (> 27)

**Description:** Verify that the Homepage achieves a Lighthouse Performance score above the target of 27 after the image pipeline is applied.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open Chrome in Incognito mode | Fresh session, no cache |
| 2 | Navigate to Staging Homepage | Page loads |
| 3 | Open DevTools → Lighthouse tab | Lighthouse panel visible |
| 4 | Select "Performance" category, Desktop mode | Settings configured |
| 5 | Click "Analyze page load" | Lighthouse runs |
| 6 | Record Performance score | Score > 27 (target per ticket) |
| 7 | Note "Properly size images" and "Serve images in next-gen formats" diagnostics | These diagnostics should show improvement or pass |

**Priority:** P1
**Type:** Performance

---

## TC-WP-020: Lighthouse Performance score on article-heavy page meets target (> 27)

**Description:** Verify that pages with multiple article images (Technical Center) also meet the Lighthouse performance target.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open Chrome in Incognito mode | Fresh session |
| 2 | Navigate to a Technical Center article page (one with multiple images) | Article page loads |
| 3 | Open DevTools → Lighthouse tab → Performance → Desktop | Settings configured |
| 4 | Click "Analyze page load" | Lighthouse runs |
| 5 | Record Performance score | Score > 27 |
| 6 | Note "Total Blocking Time" and "Largest Contentful Paint" values | Values should show improvement vs. pre-migration baseline |

**Priority:** P1
**Type:** Performance

---

## TC-WP-021: Lighthouse score comparison — before vs. after migration

**Description:** Verify measurable improvement in Lighthouse score from pre-migration baseline to post-migration result.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Before migration: run Lighthouse on Homepage and record score | Pre-migration baseline score captured |
| 2 | Before migration: run Lighthouse on a Technical Center article page | Baseline score captured |
| 3 | After migration: run Lighthouse on same Homepage | Post-migration score captured |
| 4 | After migration: run Lighthouse on same article page | Post-migration score captured |
| 5 | Compare scores | Post-migration score >= pre-migration score; both must exceed 27 |

**Priority:** P1
**Type:** Performance — Regression Benchmark

---

## TASK 4 — Migration Monitoring Per Environment

---

## TC-WP-022: DEV environment — no errors in browser console after migration

**Description:** Verify that the DEV environment shows no image-related errors after running the migration script.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to DEV environment URL | Page loads |
| 2 | Open DevTools → Console | Console visible |
| 3 | Navigate through: Homepage, Products, Technical Center, My Reports | Multiple pages visited |
| 4 | Observe console output on each page | Zero 404 errors for image resources |
| 5 | Open DevTools → Network → filter "Img" → check for failed requests (red) | No failed image requests |

**Priority:** P1
**Type:** Monitoring — DEV

---

## TC-WP-023: STAGING environment — full regression smoke test after migration

**Description:** Verify all key pages display correctly with no broken images or performance regressions after migration on STAGING.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to STAGING: `https://staging-app-pro.repairsolutions.innovavietnam.com` | Staging loads |
| 2 | Run through key pages: Homepage, Products, Technical Center (all 5 articles), My Reports, Support | All pages load without error |
| 3 | On each page: visually scan for broken image icons | Zero broken images across all pages |
| 4 | On each page: open DevTools → Network → check for 404 image errors | Zero HTTP 404 on image resources |
| 5 | Run Lighthouse on Homepage | Score > 27 |

**Priority:** P1
**Type:** Monitoring — STAGING Regression

---

## TC-WP-024: PRODUCTION environment — smoke test after go-live

**Description:** Verify PRODUCTION environment is stable with no broken images immediately after the migration deployment.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to `https://pro.repairsolutions.com` | Production loads |
| 2 | Open DevTools → Network → filter "Img" | Network ready |
| 3 | Visit: Homepage, Products page, one article page, My Reports | Key pages visited |
| 4 | Check for HTTP 404 errors on images | Zero 404 errors |
| 5 | Visually confirm images render on all visited pages | No broken icons |
| 6 | Check browser Console for errors | Zero image-related errors |
| 7 | Run Lighthouse on Homepage (quick check) | Score > 27 |

**Priority:** P1
**Type:** Monitoring — PROD Smoke Test

---

## TC-WP-025: Rollback scenario — verify data integrity if migration fails mid-run

**Description:** Verify that if the migration is interrupted mid-execution, the system does not leave the database or storage in a partially corrupted state. (Coordinate with Dev team to simulate on DEV only.)

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | (Dev to simulate) Interrupt migration script mid-execution on DEV | Migration is halted |
| 2 | Navigate to article pages in DEV | Pages load |
| 3 | Check images on articles that were processed before interruption | Images still display (not corrupted) |
| 4 | Check images on articles not yet processed | Images still display (old URLs still valid) |
| 5 | Verify no mixed state (some images broken, some fine) | Either all images intact OR rollback is clean — no partial corruption |
| 6 | Re-run migration from checkpoint or full re-run | Migration completes successfully on retry |

**Priority:** P2
**Type:** Negative — Resilience

---

## Test Coverage Summary

| Task | Test Cases | Priority |
|------|-----------|---------|
| Task 1 — Image Upload Pipeline (Consumer Web) | TC-WP-001 to TC-WP-007 | P1–P2 |
| Task 1 — Image Upload Pipeline (Admin) | TC-WP-008 to TC-WP-009 | P1–P2 |
| Task 3 — Legacy Migration: Image Display | TC-WP-010, TC-WP-011, TC-WP-013, TC-WP-015 | P1 |
| Task 3 — HTTPS Verification | TC-WP-017 | P1 |
| Task 4 — Performance (Lighthouse) | TC-WP-019 to TC-WP-021 | P1 |
| Task 4 — Migration Monitoring (DEV/STAGING/PROD) | TC-WP-022 to TC-WP-024 | P1 |
| Rollback / Resilience | TC-WP-025 | P2 |
| **Total** | **21 test cases** | |

> **Removed (out of scope):** TC-WP-012, TC-WP-014, TC-WP-016, TC-WP-018 — CloudFront CDN URL verification removed per Dev team decision (2026-04-16).

---

## Blocked / Pending Test Cases

| Test Case | Blocked By |
|-----------|-----------|
| TC-WP-001 to TC-WP-007 | Upload page location on Consumer Web — confirm with Dev team |
| TC-WP-008, TC-WP-009 | Admin platform URL and credentials — confirm with Dev team |
| TC-WP-006 | Max resize dimensions spec — confirm with Dev team |
| TC-WP-021 | Requires pre-migration Lighthouse baseline to be captured BEFORE Dev runs migration |
| TC-WP-025 | Requires Dev team coordination to simulate rollback on DEV |

---

## Pre-Migration Checklist (QA Actions Before Dev Runs Migration)

- [ ] Capture Lighthouse baseline score on Homepage (for TC-WP-021)
- [ ] Capture Lighthouse baseline score on one article page (for TC-WP-021)
- [ ] Take screenshots of 3 articles showing image layout (for TC-WP-015)
- [ ] Confirm max file size limit and max resize dimensions with Dev team
- [ ] Confirm Admin portal staging URL and credentials with Dev team
- [ ] Confirm upload page location on Consumer Web with Dev team
