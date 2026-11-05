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

## Before publishing or upgrading

- Verify visibility and ownership permissions.
- Review any embedded scripts and external resources.
- Test URL/autotag behavior and navigation.
- Check whether content depends on a legacy plugin configuration key.
- Back up the site before changing plugin versions.

**Sources and provenance:** [tagged Static Pages auto-installer](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/plugins/staticpages/autoinstall.php) and [plugin functions](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/plugins/staticpages/functions.inc). The archived Wiki topic `Static_Pages_Plugin` was used as a topic locator, not copied. Verify interface details on the deployed release.
