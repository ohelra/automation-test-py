# Test Case Design - Web Performance: Clean Article URLs and SEO Routing

**Module:** Web_Performance
**Feature:** Article Slug Routing, Legacy Redirects, Sitemap, Robots, and Metadata
**Ticket:** RWR-589 - Upgrade website architecture and URL structure for clean URLs and SEO optimization
**Epic:** Web Performance / SEO Infrastructure
**Priority:** P1 - Critical
**Environment:**
- Consumer Production: `https://pro.repairsolutions.com`
- Consumer Staging: `https://staging-pro.repairsolutions.innovavietnam.com` or current QA target
- Admin: confirm target Admin URL and credentials with Dev/QA before execution
**Precondition:**
- `RWR-589` deployment is available in the target environment.
- QA has access to Admin article management for create/edit/preview validation.
- At least 3 existing articles are available for migration and redirect testing.
- Browser DevTools is available for Network, response-code, and page-source checks.

---

## Requirement Summary

The ticket introduces cleaner, readable article URLs and related SEO improvements:

- replace legacy article URLs such as `/article/{uuid}?p={legacy-slug}`
- use clean consumer URLs such as `/article/{slug}`
- add and validate article slug management in Admin
- backfill slugs for existing articles
- add 301 redirects from legacy article URLs
- update hardcoded article links in Navbar/Footer and other rendering points
- generate `sitemap.xml`
- configure `robots.txt`
- support Meta Title and Meta Description input/output

---

## Current Baseline Observed On Production

The following current-state behaviors were confirmed from the public site and should be used as regression baselines:

- Article pages currently use legacy URLs such as:
  - `https://pro.repairsolutions.com/article/962cbfaf-bd3e-45d9-8e9c-1007990b490e?p=innova-sds50---how-to-unlock-the-secure-gateway-sgw`
  - `https://pro.repairsolutions.com/article/6833acd0-e388-4c5f-9326-0d4690d7973d?p=innova-7111-how-to-turn-off-the-oil-warning-light`
- Production article pages currently load successfully with those legacy URLs.
- The public Support > SGW AutoAuth menu currently contains hardcoded legacy article URLs.
- `https://pro.repairsolutions.com/robots.txt` currently returns the website Error page instead of a plain text robots file.
- `https://pro.repairsolutions.com/sitemap.xml` currently returns the website Error page instead of an XML sitemap.

---

## Scope

### In Scope

- Admin article slug field behavior
- Slug auto-generation and uniqueness validation
- Existing article slug backfill/migration
- Consumer routing with `/article/{slug}`
- Legacy URL redirect behavior
- Navbar/Footer/article-link updates
- `sitemap.xml`
- `robots.txt`
- Meta Title and Meta Description rendering

### Out of Scope

- Cross-browser certification
- Non-article content routing unless directly impacted by article link generation
- Search ranking verification in external search engines
- Rich-result/schema validation unless separately requested

---

## Test Case Design

## TC_001: Admin article form shows Slug field for create and edit flows

**Description:** Verify the Admin article form includes a Slug field for both new and existing articles.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Log in to Admin and open the Article create form | Article create form loads |
| 2 | Inspect the form fields | A `Slug` field is visible |
| 3 | Open an existing article in edit mode | Article edit form loads |
| 4 | Inspect the form fields again | The same `Slug` field is visible on edit |

**Priority:** P1
**Type:** UI / Functional

---

## TC_002: Admin auto-generates slug from Title for a new article

**Description:** Verify a clean slug is auto-generated when the user enters an article title.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open the new article form in Admin | Form loads |
| 2 | Enter a title such as `Innova SDS50 - How to Unlock the Secure Gateway (SGW)` | Title field accepts the value |
| 3 | Move focus away from the Title field or trigger save-ready state | Slug value is generated automatically |
| 4 | Inspect the generated slug | Slug is lowercase, hyphenated, readable, and based on the title |

**Priority:** P1
**Type:** Functional

---

## TC_003: Slug generation removes unsafe characters and normalizes formatting

**Description:** Verify the generated slug strips unsupported characters and produces a standardized format.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter a title containing uppercase letters, extra spaces, punctuation, and symbols | Title is accepted |
| 2 | Trigger slug generation | Slug is generated |
| 3 | Review the slug format | Slug uses lowercase letters and hyphens only |
| 4 | Verify formatting cleanup | No spaces, repeated hyphens, UUID fragments, or unsafe characters remain |

**Priority:** P1
**Type:** Functional / Validation

---

## TC_004: Admin prevents duplicate slug usage

**Description:** Verify the system validates slug uniqueness and blocks collisions.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open an existing article and note its slug | Existing slug is captured |
| 2 | Create or edit another article | Form loads |
| 3 | Enter the same slug value as the existing article | Duplicate slug is entered |
| 4 | Attempt to save | Save is blocked and a clear uniqueness validation message is shown |

**Priority:** P1
**Type:** Negative / Validation

---

## TC_005: Existing articles receive backfilled slugs after migration

**Description:** Verify the migration/backfill process populates slug values for legacy articles that did not previously have one.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Identify 3 existing legacy articles created before `RWR-589` | Sample articles selected |
| 2 | Open each article in Admin after deployment/migration | Edit page loads |
| 3 | Inspect the Slug field on each article | Slug is populated for each existing article |
| 4 | Compare the slug to the article title | Slug is readable and derived from the title |

**Priority:** P1
**Type:** Migration / Data Integrity

---

## TC_006: Consumer article page loads by new clean slug route

**Description:** Verify consumers can access an article through the new `/article/{slug}` route.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Take the slug from a known article in Admin | Slug value is available |
| 2 | Open `https://<consumer-domain>/article/{slug}` | Article page loads successfully |
| 3 | Verify page content | The correct article title and content are displayed |
| 4 | Verify browser URL | URL remains in clean slug format with no UUID or `?p=` parameter |

**Priority:** P1
**Type:** Functional

---

## TC_007: Legacy article URL with UUID and querystring redirects to new slug URL

**Description:** Verify old article URLs remain functional through a permanent redirect to the clean slug route.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open a known legacy article URL such as `/article/{uuid}?p={legacy-slug}` | Request is sent |
| 2 | Observe the navigation in DevTools Network or browser location bar | Redirect occurs |
| 3 | Verify final URL | Final URL is `/article/{slug}` |
| 4 | Verify redirect type | Response is `301` permanent redirect |
| 5 | Verify article content after redirect | Correct article content is displayed |

**Priority:** P1
**Type:** Functional / SEO Redirect

---

## TC_008: Legacy article URL with UUID only redirects to new slug URL

**Description:** Verify old article URLs still redirect correctly even when the `p` query parameter is missing.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open a legacy URL in the format `/article/{uuid}` | Request is sent |
| 2 | Observe redirect behavior | Redirect occurs |
| 3 | Verify final destination | Final URL is the clean `/article/{slug}` route for the same article |
| 4 | Verify response type | Redirect is permanent and not a temporary redirect |

**Priority:** P1
**Type:** Functional / SEO Redirect

---

## TC_009: Unknown or invalid slug returns 404 page without redirect loop

**Description:** Verify invalid clean URLs fail safely and do not create loops or misleading redirects.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open a non-existent URL such as `/article/not-a-real-article-slug` | Request is sent |
| 2 | Observe the page result | A 404 or equivalent not-found page is shown |
| 3 | Check browser behavior | No redirect loop occurs |
| 4 | Verify the user is not shown the wrong article | No unrelated article content is displayed |

**Priority:** P1
**Type:** Negative / Routing

---

## TC_010: Navbar article links use clean slug URLs instead of legacy UUID links

**Description:** Verify consumer navigation items that point to articles are updated to the new slug format.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open the consumer site homepage | Homepage loads |
| 2 | Navigate to menu areas containing article links, such as `Support` > `SGW AutoAuth` | Article links are visible |
| 3 | Open or inspect each article link | Link target is visible |
| 4 | Verify URL format | Link uses `/article/{slug}` and does not use `/article/{uuid}?p=` |

**Priority:** P1
**Type:** Regression / Navigation

---

## TC_011: Footer and other hardcoded article entry points use clean slug URLs

**Description:** Verify Footer and other static rendering points no longer contain hardcoded legacy article URLs.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open pages that contain Footer or static article entry points | Page loads |
| 2 | Inspect article-related links in Footer or static sections | Links are visible |
| 3 | Open the links or inspect their href values | Link target is visible |
| 4 | Verify URL format | Links use clean slug paths only |

**Priority:** P1
**Type:** Regression / Navigation

---

## TC_012: Admin Preview link opens the new clean article URL

**Description:** Verify the Preview action in Admin uses the updated consumer route.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open an article in Admin edit mode | Edit form loads |
| 2 | Click the `Preview` action | Preview page opens |
| 3 | Observe the preview URL | URL uses `/article/{slug}` |
| 4 | Verify the preview content | Correct article content is shown |

**Priority:** P1
**Type:** Functional / Regression

---

## TC_013: Article cards, listings, and search results open clean slug URLs

**Description:** Verify all user-facing article entry points resolve to the new route, not just Navbar/Footer.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open an article listing page such as `Emerging Technologies` or another article collection | Listing page loads |
| 2 | Click an article card or article title | Article opens |
| 3 | Observe the destination URL | URL uses `/article/{slug}` |
| 4 | Repeat from search results if article search is available | Same clean slug behavior occurs |

**Priority:** P2
**Type:** Regression / Navigation

---

## TC_014: sitemap.xml is accessible and returns valid XML content

**Description:** Verify the site exposes a proper XML sitemap instead of an error page.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open `https://<consumer-domain>/sitemap.xml` | Request is sent |
| 2 | Observe the response content | Response is XML, not an HTML error page |
| 3 | Verify sitemap structure | XML contains valid sitemap elements such as `<urlset>` and `<url>` |
| 4 | Verify response status | Page returns HTTP 200 |

**Priority:** P1
**Type:** SEO / Infrastructure

---

## TC_015: sitemap.xml contains clean article URLs and excludes legacy UUID article URLs

**Description:** Verify the sitemap indexes the new article routes only.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open `sitemap.xml` | Sitemap loads |
| 2 | Search for known article entries | Article URLs are present |
| 3 | Verify sitemap URL format | Indexed article URLs use `/article/{slug}` |
| 4 | Verify legacy exclusion | No sitemap entry uses `/article/{uuid}` or `?p=` legacy format |

**Priority:** P1
**Type:** SEO / Content Validation

---

## TC_016: robots.txt is accessible and contains crawler instructions

**Description:** Verify the site exposes a valid robots file instead of an application error page.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open `https://<consumer-domain>/robots.txt` | Request is sent |
| 2 | Observe the response content | Plain text robots content is shown |
| 3 | Verify response type | Response is not the site Error page |
| 4 | Verify response status | Page returns HTTP 200 |

**Priority:** P1
**Type:** SEO / Infrastructure

---

## TC_017: robots.txt references sitemap location

**Description:** Verify the robots file points crawlers to the sitemap.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open `robots.txt` | Robots file loads |
| 2 | Inspect file content | Standard crawler rules are present |
| 3 | Verify sitemap directive | File contains a valid `Sitemap:` entry pointing to `sitemap.xml` |

**Priority:** P1
**Type:** SEO / Content Validation

---

## TC_018: Meta Title from Admin is rendered on the consumer article page

**Description:** Verify article-specific Meta Title values appear in the page title and source.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | In Admin, set a unique Meta Title for an article | Meta Title is saved |
| 2 | Open the article on the consumer site | Article page loads |
| 3 | Verify browser tab title | Browser title matches the configured Meta Title or expected title pattern |
| 4 | Inspect page source or DOM head | `<title>` reflects the configured Meta Title |

**Priority:** P1
**Type:** SEO / Metadata

---

## TC_019: Meta Description from Admin is rendered on the consumer article page

**Description:** Verify article-specific Meta Description values appear in the page metadata.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | In Admin, set a unique Meta Description for an article | Meta Description is saved |
| 2 | Open the article on the consumer site | Article page loads |
| 3 | Inspect page source or DOM head | `<meta name="description">` is present |
| 4 | Verify content value | Meta description matches the configured Admin value |

**Priority:** P1
**Type:** SEO / Metadata

---

## TC_020: Updating slug or metadata does not break article accessibility

**Description:** Verify post-publish edits to slug-related SEO data do not leave the article inaccessible.

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open an existing article in Admin | Edit form loads |
| 2 | Update slug-related SEO values within allowed rules and save | Save succeeds |
| 3 | Open the current clean article URL | Article remains accessible |
| 4 | Verify the article content and metadata | Updated values are reflected without broken routing |

**Priority:** P2
**Type:** Regression / Metadata

---

## Exit Criteria

- New article URLs use `/article/{slug}` consistently
- Legacy article URLs redirect with `301` to the correct clean URL
- No known hardcoded legacy article URLs remain in public navigation points
- `robots.txt` and `sitemap.xml` are accessible and valid for SEO use
- Meta Title and Meta Description render correctly for article pages
- No broken routing, redirect loops, or duplicate-slug data issues remain

---

## Open Questions

- Confirm the exact Admin URL/environment for execution
- Confirm whether slug can be manually edited after auto-generation or should remain system-managed
- Confirm uniqueness strategy for collisions, for example suffixing vs blocking save
- Confirm whether sitemap should include only article pages or all public pages
- Confirm whether canonical tags are part of this ticket or a follow-up

---

## Notes

- This design file intentionally stays under `Web_Performance` because the ticket was requested there, even though the implementation spans Admin, consumer routing, and SEO infrastructure.
- The current production baseline shows legacy article URLs and missing `robots.txt` / `sitemap.xml` behavior, so these areas should be considered mandatory verification points for `RWR-589`.
