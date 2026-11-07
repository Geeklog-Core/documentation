# Using Geeklog — user guide

> **Geeklog 2.2.2 orientation.** The general workflows below introduce the main concepts. Interface labels, available actions and editor options depend on your account rights, installed theme and enabled plugins. Detailed UI walkthroughs still require staging verification.

## Find your way around the site

Geeklog is a content management system: visitors read published content, while authorized users can submit or manage material depending on permissions. Start by identifying whether you are browsing as a visitor, registered user, content editor or administrator. The visible menu is not a complete description of your permissions.

1. Open the homepage and browse its topics and published articles.
2. Follow an article title to read the full content and any available comments.
3. Sign in only when you need member-specific actions. A public page may be visible without an account.
4. If an expected action is missing, ask an administrator to review your **effective permissions** rather than borrowing another account.
5. If a content link returns an error, record the page URL without sharing private tokens and consult the [troubleshooting guide](../../administration/troubleshooting/index.html).

## Common tasks

| I want to… | Start here |
| --- | --- |
| Write or edit an article | [Articles, Topics and Publishing](../articles-and-topics/index.html) |
| Find or discuss a story | [Comments and Moderation](../comments-and-moderation/index.html) |
| Understand page blocks or menu links | [Blocks, Menus and Navigation](../blocks-and-navigation/index.html) |
| Follow feeds and use autotags | [Syndication, RSS and Autotags](../syndication-rss-autotags/index.html) |
| Create a stand-alone information page | [Static Pages](../../plugins/static-pages/index.html) |
| Manage user and group rights | [Users and groups](../../administration/users-and-groups/index.html) |

## Everyday tasks and source-backed administration paths

The same action may appear through different themes or navigation menus. For Geeklog 2.2.2, these are the relevant Core entry points; the links below point to **tagged source code**, not to live URLs on your installation.

| I need to… | Geeklog component | Guide |
| --- | --- | --- |
| Submit an article as a contributor | `submit.php` | [Articles and topics](../articles-and-topics/index.html) |
| Edit or publish an article as an editor | `admin/article.php` (`story.edit`) | [Articles and topics](../articles-and-topics/index.html) |
| Manage topics | `admin/topic.php` (`topic.edit`) | [Articles and topics](../articles-and-topics/index.html) |
| Manage blocks | `admin/block.php` (`block.edit`) | [Blocks and navigation](../blocks-and-navigation/index.html) |
| Moderate submissions | `admin/moderation.php` with queue-specific rights | [Comments and moderation](../comments-and-moderation/index.html) |
| Manage installed plugins | `admin/plugins.php` (`plugin.edit`) | [Plugin installation and management](../../plugins/plugin-installation-management/index.html) |

**Important:** `admin/` paths refer to the Geeklog Core administration directory, which may be installed at a customized URL. The visible link labels and permissions depend on configuration; never assume that being logged in means being authorized for an action.

## Practical learning path

Start with one small, reversible exercise on a staging site: publish a harmless article, assign an existing topic, view the public result, and then edit the article with an appropriate administrative role. For a second exercise, add a disposable block and test its appearance on a narrow screen. Finish by checking moderation and plugin screens as separate roles without making any production changes.

The detailed guides describe the **expected actions and source-confirmed permission gates**. Their acceptance checklists remain unchecked until someone exercises them on a real Geeklog installation.

**Tagged Core references:** [submission](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/submit.php), [articles](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/article.php), [topics](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/topic.php), [blocks](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/block.php), [moderation](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/moderation.php), [plugins](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/plugins.php).

## Why two users may see different publishing screens

The public submission handler has separate behavior for users with `story.edit` and ordinary contributors: a Story Admin may be redirected into the privileged editor. Site settings can also require login before a visitor may submit (including the `submitloginrequired` configuration option). Spam filtering, topic checks and a submission speed limit can prevent a story from being accepted.

For a missing article, check the contributor's result message, the publication status and the moderation queue before concluding that the article was lost. See [Articles, Topics and Publishing](../articles-and-topics/index.html) for the two workflows.

The moderation dashboard likewise shows only queues justified by the user's configured rights. A missing moderation queue is not necessarily a software error; check [Comments and Moderation](../comments-and-moderation/index.html).

**Source:** [submission handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/submit.php) and [moderation handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/moderation.php).

## Publishing safely

Before submitting text, check its title, headings, links, image rights and intended audience. Preview the result in the installed theme when available. Some contributions require moderation or review before appearing publicly; pressing Submit does not always mean immediate publication.

Do not include passwords, private account information or another person's unpublished material in an article or support request. Ask the site administrator about the applicable publishing rules.

## What this guide still needs

A version-specific screenshot walkthrough of the login/profile forms, submission screens and editorial menus; tested accessibility and mobile paths; and the exact distinction between rights for site visitors, story contributors and approved editors. These items must be checked against a running Geeklog release before removing the scope notice.

**Source basis:** Geeklog 2.2.2 release and the maintained administration, article and plugin documentation. This is new prose, not a verbatim import from the historic Wiki.
