# Static Pages plugin — creating standalone content

> **Geeklog 2.2.2 — Static Pages plugin 1.7.3.** The version and permission features below are verified against the tagged `plugins/staticpages/autoinstall.php`. Other interface details may vary with installed version and configuration.

## Purpose

The Static Pages plugin lets an authorized editor create pages outside the normal story/article publishing flow. Common uses include information pages, contact instructions and other relatively stable content.

The Wiki describes page IDs, placement in topic or index views, page cloning, access permissions, URLs and autotags. These capabilities may vary by plugin version, so consult the installed version's administration screen and bundled documentation.

## Permissions in the bundled 2.2.2 plugin

The [Static Pages 1.7.3 auto-installer](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/plugins/staticpages/autoinstall.php) defines these feature rights:

| Feature | Intended capability in the plugin |
| --- | --- |
| `staticpages.edit` | Access to the Static Pages editor |
| `staticpages.delete` | Delete Static Pages content |
| `staticpages.PHP` | Use PHP in Static Pages, a particularly sensitive capability |

The bundled installer assigns `staticpages.edit` and `staticpages.delete` to its default **Static Page Admin** group. **It does not assign `staticpages.PHP` to any group by default.** Do not infer that a user allowed to edit pages may also execute PHP.

The same installer defines configuration-tab rights, such as `config.staticpages.tab_main` and `config.staticpages.tab_permissions`. Check effective group memberships before allowing a user to change plugin configuration.

### Safe permission review

1. Sign in to a **disposable staging** installation with an account authorized for the plugin.
2. Review membership of the Static Page Admin group before assigning a new editor.
3. Confirm the chosen editor can create or update appropriate ordinary content and that a test account without `staticpages.edit` cannot access the editor.
4. Confirm delete permissions independently and keep `staticpages.PHP` unassigned unless a separately reviewed application requirement justifies it.
5. Check the final page anonymously or through the intended reader role to confirm content visibility.

This is a source-backed testing procedure; it does **not** claim that every permission scenario has been exercised in the current staging installation.

## Create and maintain a page

1. Sign in with an account authorized to administer Static Pages.
2. Open the installed plugin's administration screen.
3. Set a descriptive page title and an appropriate page ID, if editable.
4. Add the content, review its access permissions, and save.
5. Check the page with a public account or logged out to verify expected visibility.
6. Confirm links, navigation and appearance on mobile devices.

Do not give authors broader plugin or PHP-execution permissions than their tasks require.

## PHP execution is a security-sensitive historical feature

In the bundled Geeklog 2.2.2 plugin, PHP execution has a separate `staticpages.PHP` feature right that is not assigned to a group by default. **Do not enable execution of arbitrary PHP merely to reproduce a historic tutorial.** Prefer plain content, approved plugins and safe template features. If a current deployment supports PHP in page content, restrict its use to trusted administrators and verify the exact security model with the target plugin release.

## Choosing a Static Page or an article

| Requirement | Usually the better starting point |
| --- | --- |
| A stable information page such as contact details, policies or a custom landing page | Static Page |
| Dated editorial content that participates in article publishing and topic/news workflows | Article |
| Custom application behavior, data processing or access-controlled actions | A reviewed plugin or Core-supported extension, not arbitrary PHP inside a page |

This is an editorial decision guide, not a claim that each content type has identical permissions, URLs or rendering behavior. Test the actual presentation and configured plugin version.

## Publishing checklist for editors

Before saving, record the page's intended audience and navigation entry point. A page that looks correct while signed in as an administrator may be invisible to anonymous visitors.

1. Choose a short, stable page identifier where the installed editor allows it; avoid changing an existing public identifier without planning link updates.
2. Add a meaningful title, readable headings, descriptive link text and alternative text for informative images.
3. Confirm owner, group and reader permissions separately from editing rights.
4. Preview with representative content. Check long headings, links, images and narrow-screen rendering in the active theme.
5. Save and follow the actual public URL in a **logged-out** browser session; also test any account roles that should have restricted access.
6. Check inbound navigation or autotags that refer to the page, then record the change in your site maintenance notes.

The permissions table above identifies **plugin-level feature rights**, not every per-page owner/group/read flag. Never infer that possession of `staticpages.edit` means the user is authorized to publish any page to any audience.

## Problems after publishing

| Observation | What to verify |
| --- | --- |
| Page not visible to anonymous visitors | Effective page visibility, ownership/group permissions and navigation placement |
| Existing links return 404 | Stable page ID, actual URL and routing configuration; avoid blindly changing rewrite rules |
| Page formatting differs from articles | Active theme and Static Pages template rendering, not only the editor preview |
| Embedded features or PHP do not execute | Plugin feature rights and selected rendering mode; never enable `staticpages.PHP` as a generic workaround |
| A cloned page behaves differently | Unique identifier, inherited settings, permissions and links before publication |

When troubleshooting a site failure, follow the [administration troubleshooting guide](../../administration/troubleshooting/index.html). Where behavior depends on the original plugin implementation, compare with the tagged 2.2.2 plugin files linked below.

## Before publishing or upgrading

- Verify visibility and ownership permissions.
- Review any embedded scripts and external resources.
- Test URL/autotag behavior and navigation.
- Check whether content depends on a legacy plugin configuration key.
- Back up the site before changing plugin versions.

**Sources and provenance:** [tagged Static Pages auto-installer](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/plugins/staticpages/autoinstall.php) and [plugin functions](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/plugins/staticpages/functions.inc). The archived Wiki topic `Static_Pages_Plugin` was used as a topic locator, not copied. Verify interface details on the deployed release.

## Detailed tutorial: create an About page with Static Pages

**Scenario:** publish a standalone **About our community** page, distinct from news articles. **Prerequisites:** the bundled Static Pages plugin is installed, a disposable site, and an account with `staticpages.edit`.

1. Open the Static Pages administration interface. In the tagged 2.2.2 plugin it is handled by `admin/plugins/staticpages/index.php`.
2. Choose the new-page action and enter **About our community** as the title. Use a unique page ID such as `training_about_us` if the installed editor exposes an editable identifier.
3. Add simple content: **Our community shares news, tutorials and useful links.** Include a heading and a descriptive link to an existing public article where appropriate.
4. Check owner/group and anonymous/member permissions carefully. Do not set the page to private if the intention is a public About page.
5. Leave any PHP execution controls disabled. The `staticpages.PHP` right is distinct from `staticpages.edit` and should not be required for ordinary HTML content.
6. Preview the page if the editor offers it. Inspect headings, link destinations and layout.
7. Save through the normal editor. The tagged handler checks a CSRF token for the save operation.
8. Open the resulting public URL while logged out and on a narrow-screen browser. Confirm its content and access permissions.
9. If you want this page in a menu, add its **public URL** using a supported theme/menu feature or a normal text block; saving a page does not guarantee it appears in every theme menu.
10. Edit a sentence and save again to confirm the maintenance workflow. Remove the disposable page later only with appropriate delete rights.

**Expected output:** a stable About page with the intended public visibility. If it is absent, inspect its permission settings, page ID and navigation placement before modifying server rewrite rules.

### Safe clone exercise

1. In staging, create and save the test About page above.
2. If the editor exposes **Clone**, select it and inspect the copied title, ID, permissions and placement.
3. Give the copy a new unique ID before saving. Do not allow two pages to share a public identifier.
4. Review permissions and links; inherited defaults may not match the new page's intended audience.
5. Inspect the cloned page anonymously, then remove the disposable copy.

**Tagged source:** [Static Pages administrator](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/plugins/staticpages/index.php) checks `staticpages.edit` to enter, `staticpages.delete` for deletion controls, and `staticpages.PHP` plus the plugin setting before offering PHP-related options. It supports preview, edit and clone branches. Exact UI labels and template presentation require staging verification.
