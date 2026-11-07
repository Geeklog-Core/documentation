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

## Further verification

The full set of Geeklog 2.2.2 article administration form fields, scheduling behavior and revision options must be checked in a running installation and against the tagged handlers. Older Wiki examples may use *story* where modern editorial language uses *article*; retain the historical term when it is a code symbol or source setting.
