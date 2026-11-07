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

## Still to verify

Create source-checked examples for supported block types and exact administration screens in the target release. The historical Wiki may supply topic names, but its older template/CSS instructions must not be copied without verification.
