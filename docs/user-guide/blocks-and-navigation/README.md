# Blocks, menus and site navigation

> **Geeklog 2.2.2 orientation.** Specific block types, placement choices and menu entries depend on the active theme, configured features and plugins. Test changes in staging before modifying production navigation.

## Understand the components

A **block** presents a reusable piece of content or a feature in part of the site layout. Menus offer navigation to stories, topics, administration features or other pages. A theme decides where blocks and other layout areas appear; permission checks still belong to the server.

Do not assume that adding a two-column layout inside an article is the same as configuring the theme's side blocks.

## Review a navigation change

1. Make a list of the pages readers need to find: home, current topics, important Static Pages, contact or account functions.
2. Check the current theme and enabled plugins to locate the menu/block interface actually in use.
3. On a staging copy, adjust a single entry or block at a time. Use clear link text that describes the destination.
4. Check placement on narrow and wide screens and ensure keyboard users can reach the link.
5. Verify the result as a logged-out visitor and with representative registered users.
6. Keep a record of the original layout and configuration for rollback.

## Troubleshooting

| Symptom | First check |
| --- | --- |
| Block missing | Site configuration, effective permissions and theme support |
| Menu link opens the wrong page | Exact URL, topic or page identifier and rewrite settings |
| Content overlaps another column | Responsive CSS, minimum widths and theme markup |
| Administrative link shows but is denied | Server-side feature rights; hiding/showing a link is not authorization |
| Layout differs on plugin pages | Plugin templates and the active theme's specific rendering paths |

See [Theme Development](../../development/theme-development/index.html) for a controlled layout customization and [Static Pages](../../plugins/static-pages/index.html) for stable landing content.

## Configure a block using the Core administrator

Geeklog 2.2.2 includes a [block administration handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/block.php) at `public_html/admin/block.php`. Its entry check requires `block.edit`; the handler exposes editing, saving, ordering, moving and enable/visibility changes. Deletion is separately associated with `block.delete`, and changes to saved state use CSRF checks.

**Example: publish a small information block**

1. Open the Blocks administration entry on an isolated site using an account granted `block.edit`.
2. Record the current block list, theme and the part of the page where the test block should appear.
3. Create a test block with a short title and harmless static text. Use the fields and placement choices actually shown by the installed theme and plugins; not every theme exposes the same positions.
4. Save the block, check whether it is enabled and visible, and view the homepage both signed in and signed out.
5. Test narrow screens and keyboard navigation. If a block contains a link, make its destination and label understandable without surrounding visual context.
6. Change one property (for example, order or visibility) and verify the result. Restore the original position or remove the test block using an authorized administrator.

### Distinguish common operations

| Action | What to verify |
| --- | --- |
| Edit a block | The account has `block.edit` and is permitted to change the target block |
| Delete a block | The account has the necessary delete right; do not equate edit with delete |
| Reorder or move | The target position is supported by the active theme/plugin and the change persists |
| Enable or disable | The state reported by the administration list agrees with what anonymous visitors see |
| Customize a menu | The menu is configured in the supported site/theme/plugin layer rather than by patching Core PHP |

A menu entry and a side block are different features. Menu behavior can be supplied by a theme or plugin, so this guide does not claim that every menu is editable from `admin/block.php`.

### Permission acceptance

- [ ] The authorized block editor can create and update a disposable block.
- [ ] An account without `block.edit` cannot directly load the block administration page.
- [ ] An account without deletion rights cannot delete an existing block.
- [ ] Visitors see only the expected enabled/visible content.
- [ ] Layout and links work on desktop and mobile and with keyboard navigation.

**Status:** Core handler paths/rights are checked against tag v2.2.2; the above UI sequence remains a proposed staging exercise.

## Still to verify

Create source-checked examples for supported block types and exact administration screens in the target release. The historical Wiki may supply topic names, but its older template/CSS instructions must not be copied without verification.
