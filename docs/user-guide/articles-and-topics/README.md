# Articles, topics and publishing

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

## Article scheduling and topic hierarchy: fields to verify

The tagged [article editor](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/article.php) exposes separate **publication** and **expiration** date components and loads story permission fields for owner, group, members and anonymous readers. The [topic editor](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/topic.php) includes a **parent topic**, an **inherit** setting and topic permission fields.

This means the editor's publishing checklist should cover more than title and body:

| Editorial decision | Inspect in the 2.2.2 form | Common failure to investigate |
| --- | --- | --- |
| Publication date | Date and time values, including the site's time settings | Article scheduled for a later time is not yet visible |
| Expiration | Expiration fields, when applicable | Content disappears or changes presentation after expiration |
| Topic hierarchy | Assigned topic, parent topic and inheritance | Unexpected category placement or inherited access |
| Audience | Owner/group/member/anonymous access | Article visible to an editor but not to the intended public |
| Draft versus submission | Draft state and separate moderation queues | Author expects immediate publication from a submission |

**Do not assume that changing a date alone publishes an item.** Record actual resulting visibility with anonymous and editor accounts, and check the site's configuration before drawing conclusions.

### Staging exercise: a scheduled story

1. As a permitted editor, create a harmless article in a disposable topic and record the current site time.
2. Inspect the publication and expiration controls supplied by the installed editor. Use a future publication date only in an isolated test environment.
3. Save using the editor's normal workflow and record the resulting state.
4. Check the item as an editor and as an anonymous visitor **before** the intended publication time.
5. After the test time, check again and record the exact observed behavior. Do not infer scheduling behavior from the existence of form fields.
6. Remove the test item and check its topic associations.

## Submission outcomes and role-aware navigation

The tagged `public_html/submit.php` includes two important details that are easy to miss:

- When a user already has `story.edit`, the ordinary story submission route redirects them toward the privileged article editor (`admin/article.php?mode=edit`). Therefore, do not assume the same **Submit Story** action presents an identical form to contributors and editors.
- For an ordinary story submission, the Core invokes a spam check and submission speed limit, validates required content and topic selection, then handles the result. `STORY_SAVED` redirects to the story URL; `STORY_SAVED_SUBMISSION` redirects to the homepage with a submission message. Neither response should be described as an unconditional promise of public visibility.

The `submit.php` handler also checks `loginrequired` and `submitloginrequired` before allowing anonymous submissions when those settings are enabled.

### Example: compare a contributor and an editor

1. In staging, visit the submission route with a normal contributor and record the visible form and its result after submission.
2. Repeat using a user with `story.edit`. Check whether Geeklog redirects to the administration editor instead of presenting the public submission workflow.
3. With the contributor, submit a valid test article to an allowed topic. Record whether it was saved directly or went to the moderation queue.
4. Repeat the request with a restricted topic, invalid submission data or a blocked/too-fast repeat submission; record the actual message, not just the redirected URL.
5. Check publication as an anonymous reader and inspect the moderation queue separately with an authorized account.

### Parent-topic access and topic identifiers

The tagged `admin/topic.php` checks whether a requested parent exists, whether it is a forbidden archive parent, whether a topic identifier is reserved or already used, and whether the editor has sufficient access to the target and parent topic. Its save path requires a CSRF token.

When designing the category tree, verify the parent topic and its rights **before** saving. Changing an identifier or deleting a parent can affect existing article assignments; do this first in a staging copy. The Core represents the root with `TOPIC_ROOT`, not an ordinary user-created topic identifier.

## Check publishing and permissions

- A normal contributor can submit but cannot reach the privileged article editor.
- A Story Admin can edit an allowed article, and cannot bypass an unrelated topic restriction.
- A user without `topic.edit` cannot save or delete a topic directly.
- A moderator can review submitted articles only with the corresponding rights.
- Draft visibility follows configuration and role, including the `listdraftstories` condition.
- The final article has the intended public visibility and presentation.

## Detailed tutorial: write, review and publish an article

**Scenario:** publish a short community announcement. **Prerequisites:** an existing topic, a contributor account and (if submissions are moderated) a separate user with `story.moderate`.

### Step A — Prepare the article

Use this example material (replace it with original text for your site):

- **Title:** Community meeting on Saturday
- **Topic:** News or Events, whichever exists and is accessible
- **Introduction:** We are holding a community meeting this Saturday.
- **Body:** Everyone is welcome. Check the events page for the time and location.

Before opening Geeklog, make sure the introduction makes sense on its own: themes may display only the opening text on topic listings. Use a descriptive title and ordinary formatting; do not paste executable scripts.

### Step B — Submit as a contributor

1. Sign in as a regular contributor, not a Story Admin. Open the site's **Submit Story** action if available.
2. Enter the title, introduction and the selected topic. Add the body in the field provided by the installed editor.
3. Select an allowed content format. If HTML is enabled for the account, use only supported markup; the server may filter unsupported tags.
4. Preview when offered. Inspect paragraphs, links and the difference between introduction and extended text.
5. Submit once. Record the displayed message. The source distinguishes `STORY_SAVED` from `STORY_SAVED_SUBMISSION`, so the item might publish or enter a submission queue.
6. Check the public article list. If it is absent, ask an authorized moderator to review the submission; do not repeatedly submit duplicates.

### Step C — Review as an editor or moderator

1. Open `admin/moderation.php` with a moderator authorized for article submissions (`story.moderate`).
2. Confirm the submission matches the intended topic and contains no private details.
3. Use the available approval action. The handler also checks topic access; being a moderator does not imply permission to publish into every topic.
4. Alternatively, a user with `story.edit` can open `admin/article.php` and create or edit an article through that privileged workflow.
5. Open the article in a logged-out browser to check actual public visibility and copy its stable public URL.

**Expected output:** one announcement in the correct topic with no duplicate submission and a link accessible to its intended readers.

## Detailed tutorial: create a topic and a child topic

**Scenario:** add a **Resources** category and a **Tutorials** child category. **Prerequisites:** `topic.edit`, rights to the relevant parent and a disposable site.

1. Open `admin/topic.php` as a topic editor. Record existing topic identifiers so that you do not reuse one.
2. Create the parent topic with a readable name, a unique ID such as `training_resources`, and a parent choice corresponding to the root.
3. Review its group and anonymous/member permissions. Decide whether the category is visible to the public before saving.
4. Save through the form. Confirm it appears in the topic list, then reopen it to inspect the saved values.
5. Create a second topic, for example `training_tutorials`, selecting `training_resources` as parent.
6. Inspect the **inherit** option; note its selected state rather than assuming inheritance always applies.
7. Save and assign a disposable article to the child topic. Check navigation and topic access as a member and anonymously.
8. Test a user without `topic.edit`: the administration action must be denied. Remove the disposable article before deleting the test categories.

**Common mistakes:** duplicate or reserved topic IDs, selecting an archive topic as parent, insufficient rights to a parent, and assuming topic visibility equals article visibility.

## Detailed tutorial: investigate an unpublished article

1. Note the article title, user role, topic and approximate submission time.
2. Ask whether it was sent through `submit.php` or saved in `admin/article.php`.
3. Check the submission queue (`story.moderate`) and the draft list (`listdraftstories` plus `story.edit`), which are separate.
4. Inspect publish/expire dates, topic membership and owner/group/member/anonymous permissions.
5. Review any spam or rate-limit feedback. Do not disable security checks just to make the test succeed.
6. Recheck the public site in a logged-out session after an authorized change.
