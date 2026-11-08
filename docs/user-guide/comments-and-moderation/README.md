# Comments and moderation

> **Geeklog 2.2.2 workflow overview.** Comment and submission behavior is influenced by configuration, permissions, content type and enabled plugins. The release's actual UI and policy must be checked before treating example actions as universal.

## For readers

When comments are enabled on content you can access, use the available reply or submission form responsibly. Preview your text where provided, respect the site's rules and never include private credentials or personal data. A comment that does not appear immediately may require approval or may have been rejected by moderation controls.

## For moderators

1. Determine the site's documented moderation policy and the rights required to review contributions.
2. Use a dedicated authorized account on a staging system to learn the review interface.
3. Inspect the submitted content and its context without following untrusted links or running pasted code.
4. Apply the permitted action: approve, reject, edit or request changes only where the installed interface supports it.
5. Confirm the content's final public visibility as a separate user.
6. Document an escalation route for abusive content and possible false positives without publishing private account data.

## Moderation decisions

| Situation | Review focus |
| --- | --- |
| Comment does not appear | Approval queue, publishing restrictions, spam filtering and permission checks |
| Reply action unavailable | Article/comment settings and the reader's effective rights |
| Submission appears only to moderator | Publication status and content-level visibility |
| Plugin moderation differs from Core | Plugin's own workflow, callback and permission model |

## Understand the moderation queues in Geeklog 2.2.2

The [tagged moderation handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/moderation.php) makes an important distinction between article submissions, drafts, comment submissions and plugin-supplied moderation lists:

| Queue or operation | Confirmed source condition |
| --- | --- |
| Article submissions | `story.moderate` |
| Draft article list | `listdraftstories = 1` and `story.edit` |
| Submitted comments | `commentsubmission = 1` and `comment.moderate` |
| Plugin submissions | Delegated to plugin moderation callbacks such as `PLG_showModerationList()` |
| Moderation form processing | Checks `SEC_checkToken()` before invoking moderation actions |

The moderation handler has distinct `approve` and `delete` action branches. This does not imply every displayed item supports editing or every logged-in user can approve it. Article approvals additionally check access to the topic.

### Example: approve a comment submission

1. In staging, configure a site with comment submission moderation enabled and create a test comment in an article that accepts comments.
2. Use an account with the relevant moderation right to open the moderation administration page.
3. Locate the submitted comment and inspect its text before choosing the available approval or deletion action.
4. Submit the action through the normal protected form. Verify the queue changes.
5. Reopen the relevant article as an anonymous user to check whether the comment is actually public.
6. Repeat the attempt using a user **without** `comment.moderate` and confirm direct administrative requests are rejected.

### Example: a draft does not show in the queue

Check the `listdraftstories` setting and the editor's `story.edit` right **before** assuming the draft has been deleted. The draft list is conditional and is different from the regular article-submission list. See [Articles and topics](../articles-and-topics/index.html).

**Source references:** [moderation handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/moderation.php), [security library](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/lib-security.php), [comment entry point](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/comment.php).

## When the moderation dashboard shows nothing

Geeklog 2.2.2 checks `SEC_hasModerationAccess()` before showing the dashboard. The source's separate lists matter: a user can be entitled to **one queue** without having permission to manage every other submission type.

Use these checks:

1. **No article submissions:** verify `story.moderate`, and whether a contributor's article actually entered the submission queue rather than being saved as an article.
2. **No drafts:** check both `listdraftstories` and `story.edit`; drafts are not the same as ordinary submitted stories.
3. **No comments:** check both `commentsubmission` and `comment.moderate`, and confirm the comment was actually submitted.
4. **No plugin items:** review whether that particular plugin registers a moderation list; the Core uses `PLG_showModerationList()`.
5. **Actions appear to do nothing:** confirm the form's valid CSRF token and rights before retrying; never bypass checks by constructing manual URLs.

## Moderation acceptance tests

- [ ] Article and comment queues follow their separate rights and configuration switches.
- [ ] Direct form submissions without a valid CSRF token do not perform a moderation action.
- [ ] A nonmoderator cannot approve or delete a submission.
- [ ] Approved material is visible only to its intended audience.
- [ ] Plugin-specific queues follow their plugin's permissions and callbacks.

These outcomes must be recorded from a disposable installation; reading the handler is not equivalent to a live permission test.

## Developer integration

Plugins may integrate moderation and comments through Core dispatchers, but old callback names and signatures are not a safe implementation template. Begin with the tagged [Plugin API](../../development/plugin-api/index.html) and verify dispatch behavior in Geeklog 2.2.2 before coding.

## Detailed tutorial: comment on an article

**Goal:** make a constructive comment and understand why it may not appear immediately.

1. Sign in as a reader if the site requires an account for comments.
2. Open an article where comments are enabled and follow the available comment or reply action.
3. Write a short example comment such as **Thanks for sharing these resources.** Avoid sharing contact details or confidential information.
4. Preview if the installed interface supports it, then submit once.
5. Return to the article and inspect the result. If the comment is absent, do not post repeated copies; check whether the site moderates submissions.
6. Where moderation is active, ask an authorized moderator to inspect the queue. Recheck the article anonymously after approval.

## Detailed tutorial: moderate a submitted comment

**Prerequisites:** `commentsubmission = 1`, an account with `comment.moderate`, and a disposable test comment pending review.

1. Open the administrative moderation screen (`admin/moderation.php`) using the authorized moderator account.
2. Find the **comment** submission list. A missing list may mean moderation is disabled or the user lacks the corresponding right.
3. Read the comment and the article context. Do not open suspicious links or copy untrusted code.
4. Select an available approval or deletion action. Use the built-in protected form; do not construct manual mutation URLs.
5. After processing, verify the queue changed as expected and check the article while logged out.
6. If the expected result is missing, note the article ID, moderation mode and resulting status without recording a session token.

**Expected output:** the test comment appears only after the site's configured approval workflow permits it.

## Detailed tutorial: process a contributed story

1. Use a contributor account to create a new article submission in an accessible topic.
2. As a separate account with `story.moderate`, open the story queue in `admin/moderation.php`.
3. Confirm the intended topic and the text. Check topic-level access before approving.
4. Approve or reject through the available form and record the resulting notification or redirect.
5. Check the public article as a visitor. If the article remains invisible, review its publication date and permissions rather than approving it again.
6. Finally, inspect the draft queue only if `listdraftstories` is enabled and you have `story.edit`.
