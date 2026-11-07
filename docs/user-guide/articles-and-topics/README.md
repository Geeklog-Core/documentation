# Articles, topics and publishing

> **Geeklog 2.2.2 task guide — UI verification pending.** Exact publishing controls depend on the site's theme, configuration and your feature rights. Do not treat this page as an authorization specification.

## Concepts

An **article** (historically called a *story*) is dated editorial content. A **topic** groups related articles and can help readers navigate the site. A **draft** is not necessarily published: approval, publication time, audience permissions and moderation settings can affect visibility.

For a stand-alone page that is not part of the normal article publishing flow, see [Static Pages](../../plugins/static-pages/index.html).

## Draft, review and publish

1. Sign in with an account authorized to create or submit content.
2. Open the article submission or editorial interface available to that account.
3. Choose a useful, descriptive title and the appropriate topic.
4. Write an introduction and body using the editor provided by the installed release. Check formatting and meaningful headings.
5. Review images, embedded links, attribution and text accessibility.
6. Preview the output where the interface supports it.
7. Submit the article. Check whether it is awaiting approval, saved as a draft or actually published rather than assuming Submit means public visibility.
8. Open the public URL as a logged-out reader to check access and presentation. If a change is not visible, verify moderation and publishing state before resubmitting.

## Editor checklist

| Check | Questions |
| --- | --- |
| Topic | Is this the right category for readers? |
| Timing | Is it a draft, scheduled item or immediately visible? |
| Visibility | Can the intended audience actually read it? |
| Formatting | Are headings, paragraphs, links and images readable on narrow screens? |
| Comments | Are commenting rules appropriate for the content? |
| Recovery | Is there a record of the changed material in case the edit must be reverted? |

## Common problems

An article that is visible to its author but not anonymous visitors may be unpublished, restricted or awaiting moderation. A broken preview can arise from the theme or editor, not necessarily from the article text. Do not change database tables or permission settings to force publication; consult [Users and groups](../../administration/users-and-groups/index.html) and [Troubleshooting](../../administration/troubleshooting/index.html).

## Choose the correct workflow in Geeklog 2.2.2

Geeklog distinguishes a visitor-facing submission route from privileged administration. The tagged source contains:

| Task | Source-backed entry point | Authorization or workflow |
| --- | --- | --- |
| Submit a new article for review | `public_html/submit.php` (`submitstory()`, `savestory()`) | Uses the submission flow and its configured review/spam checks; this is not the privileged article editor |
| Edit or publish articles with editorial rights | `public_html/admin/article.php` | Requires `story.edit` before entering the administration handler |
| Create, update or organize topics | `public_html/admin/topic.php` | Requires `topic.edit`, checks a CSRF token when saving, and applies topic/group access rules |
| Approve submitted articles | `public_html/admin/moderation.php` | Shows the article submission list only when `story.moderate` is granted; approval also checks access to the assigned topic |
| Review drafts in moderation | `public_html/admin/moderation.php` | The draft list requires `listdraftstories = 1` **and** `story.edit` |

**Why this matters:** a registered user who can submit a story is not necessarily a Story Admin. A user authorized to edit a story may still lack rights to edit a particular topic. Confirm permission and publication state separately.

### Example: submit a story without publishing it accidentally

1. In a staging installation, use a regular account allowed to submit articles. Open the site-provided submission action, which is handled through `submit.php`.
2. Fill out the article's title, topic and text. If your site requires preview, use it before submitting.
3. Submit once and record the resulting message. Check the administration moderation list with a separate moderator account.
4. If the story is awaiting approval, the moderator should check topic access and content before approving it.
5. Verify visibility as an anonymous visitor. Do not assume that the author's preview is proof of publication.
6. Repeat with a Story Admin through `admin/article.php`; note how this differs from ordinary submission.

### Example: add a topic without bypassing permissions

1. With a `topic.edit` account, open the Topics administration entry (`admin/topic.php`) on a test site.
2. Create a clearly named test topic and save it using the form's built-in token.
3. Select it from a test article and check that its public navigation is sensible.
4. Test with an account **without** `topic.edit`; it must not be able to modify the topic by visiting the administrator URL directly.
5. Remove the disposable test topic only after checking whether it has associated content.

**Code references:** [article administrator](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/article.php), [topic administrator](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/topic.php), [article submission](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/submit.php), [moderation](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/moderation.php).

## Staging acceptance checklist

- [ ] A normal contributor can submit but cannot reach the privileged article editor.
- [ ] A Story Admin can edit an allowed article, and cannot bypass an unrelated topic restriction.
- [ ] A user without `topic.edit` cannot save or delete a topic directly.
- [ ] A moderator can review submitted articles only with the corresponding rights.
- [ ] Draft visibility follows configuration and role, including the `listdraftstories` condition.
- [ ] The final article has the intended public visibility and presentation.

These are **test cases to execute**, not a record of a completed staging test.

## Further verification

The full set of Geeklog 2.2.2 article administration form fields, scheduling behavior and revision options must be checked in a running installation and against the tagged handlers. Older Wiki examples may use *story* where modern editorial language uses *article*; retain the historical term when it is a code symbol or source setting.
