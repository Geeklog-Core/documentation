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

## Developer integration

Plugins may integrate moderation and comments through Core dispatchers, but old callback names and signatures are not a safe implementation template. Begin with the tagged [Plugin API](../../development/plugin-api/index.html) and verify dispatch behavior in Geeklog 2.2.2 before coding.

**Historical Wiki sources to evaluate:** `Adding_Moderation_Capability` and `Integrating_the_Comment_Engine`. These pages describe old version bands; their code samples and wording have not been republished. Complete UI testing and policy examples remain outstanding.
