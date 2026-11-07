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

## Block types in Geeklog 2.2.2

The [block editor source](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/block.php) recognizes four type identifiers. They are **not** interchangeable, and the relevant input fields differ:

| Block type | Purpose / fields recognized by Core | Documentation guidance |
| --- | --- | --- |
| `normal` | Title and text content | Appropriate starting point for a simple information block |
| `portal` | Title and feed URL | Check syndication source, feed availability and output for untrusted content |
| `phpblock` | Title and PHP block function name | **Developer-only:** execution code must be reviewed and should not be supplied by ordinary editors |
| `gldefault` | Core-provided block controls | Treat as a built-in feature; its behavior can differ from a custom text block |

The same handler obtains additional supported locations through `PLG_getBlockLocations()`. Consequently, the available position list can vary with plugins. Some theme layouts may not render all configured positions.

### Example: test a normal text block safely

1. Select the `normal` block type and provide a title plus a short text paragraph.
2. Keep the content plain for the first test, with no PHP execution and no externally loaded feed.
3. Choose a location offered by the installation and save through the administrator interface.
4. Verify the block title, readable content and resulting position in the active theme.
5. Compare logged-out and authenticated views, then test disable/enable and restore the original layout.

**Source basis:** the type selection and validation logic in `admin/block.php`. This confirms that these fields are recognized, **not** that every type is safe or enabled under the site's configuration.

## Check block visibility and display options

The tagged block save handler receives separate values for **enabled state**, **permitted audience**, **device**, **location**, **sort order** and the content itself. It also supports autotag/newline settings and CSS id/classes. These inputs do not all mean the same thing.

For a block that seems to have disappeared, investigate in this order:

1. Is it enabled in the administrative list?
2. Is its selected topic or audience permission compatible with the viewer?
3. Does the active theme render its configured position?
4. Does its device setting include the device category being tested?
5. If it contains a feed or a PHP function, is the source or function available and suitable for this site?

When editing a block, Geeklog accepts `normal`, `portal`, `phpblock` and `gldefault` as type identifiers. The presence of `phpblock` in the editor does **not** authorize entering arbitrary PHP source in a block; its implementation expects a named PHP block function. Only reviewed, trusted site code should provide one.

**Source:** [block administration save handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/block.php).

### Permission acceptance

- [ ] The authorized block editor can create and update a disposable block.
- [ ] An account without `block.edit` cannot directly load the block administration page.
- [ ] An account without deletion rights cannot delete an existing block.
- [ ] Visitors see only the expected enabled/visible content.
- [ ] Layout and links work on desktop and mobile and with keyboard navigation.

**Status:** Core handler paths/rights are checked against tag v2.2.2; the above UI sequence remains a proposed staging exercise.

## Still to verify

Create source-checked examples for supported block types and exact administration screens in the target release. The historical Wiki may supply topic names, but its older template/CSS instructions must not be copied without verification.
