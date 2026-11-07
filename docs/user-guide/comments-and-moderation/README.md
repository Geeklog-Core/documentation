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

## Moderation acceptance tests

- [ ] Article and comment queues follow their separate rights and configuration switches.
- [ ] Direct form submissions without a valid CSRF token do not perform a moderation action.
- [ ] A nonmoderator cannot approve or delete a submission.
- [ ] Approved material is visible only to its intended audience.
- [ ] Plugin-specific queues follow their plugin's permissions and callbacks.

These outcomes must be recorded from a disposable installation; reading the handler is not equivalent to a live permission test.

## Developer integration

Plugins may integrate moderation and comments through Core dispatchers, but old callback names and signatures are not a safe implementation template. Begin with the tagged [Plugin API](../../development/plugin-api/index.html) and verify dispatch behavior in Geeklog 2.2.2 before coding.

**Historical Wiki sources to evaluate:** `Adding_Moderation_Capability` and `Integrating_the_Comment_Engine`. These pages describe old version bands; their code samples and wording have not been republished. Complete UI testing and policy examples remain outstanding.
