# Theme development — step by step

For CTL method signatures and the historical template syntax inventory, see the [Caching Template Library developer reference](../caching-template-library/).

## 1. Identify the rendering layer

Distinguish site-wide theme layout, a specific page template, an article body and a plugin template. Changing a theme does not automatically make a new two-column article content structure or add server-side functionality.

Review [Themes and templates](../templates/index.html) before editing; historical template names are examples to check against the installed theme, not universal paths.

## 2. Create a reversible staging change

1. Copy the target theme to an isolated site and preserve the original version.
2. Locate the template or stylesheet actually used for the affected page.
3. Make a small visual-only change; document modified files.
4. Open the homepage, an article, a plugin page and an administrative page where authorized.
5. Test long titles, narrow screens, contrast, focus and keyboard navigation.
6. Restore the original file if behavior differs; avoid modifying multiple elements simultaneously.

## 3. Design reusable components

Prefer consistent headers, navigation, readable cards, forms and block layouts instead of page-specific hacks. Optimize images and decorative backgrounds without hiding important content or introducing heavy dependencies. Serve local assets using correct relative paths, and test caching after changes.

## 4. Keep responsibilities separate

| Requirement | Appropriate area to investigate |
| --- | --- |
| Header/footer arrangement | Theme templates |
| Sidebar/block placement | Theme plus supported block configuration |
| Rich article-body layout | Authorized content markup or a reviewed extension |
| Custom business logic | Plugin/Core APIs, with permissions |
| Search or data processing | Server-verified feature, not CSS alone |

## 5. Validate before release

Test representative plugins, responsive layouts, upgrades and anonymous access; check for duplicate headers, missing assets and overlapping columns. Ensure that no template exposes private values or bypasses server authorization.

**Historic Wiki leads:** `Theme_Developers_Guide` and `Caching_Template_Library`. Do not import old compatibility scripts blindly. A tagged-theme walk-through with verified file names remains to be produced.
