# Managing users and groups

> **Geeklog 2.2.2 administration reference.** Permission checks below are verified in the tagged source. Use a disposable test account to confirm the behavior of your particular installation and enabled plugins.

## Permissions and administrator access

Geeklog uses groups and feature rights to control administrative actions. In the 2.2.2 distribution:

- [`public_html/admin/user.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/user.php) checks `SEC_hasRights('user.edit')` before allowing user administration.
- [`public_html/admin/group.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/group.php) checks `SEC_hasRights('group.edit')` for group administration.
- [`system/lib-security.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/lib-security.php) defines `SEC_hasRights()` and `SEC_inGroup()`, and the administration handlers use these functions to check authorizations.

Do not grant the `Root` role to ordinary contributors. Avoid modifying or deleting the last account that can administer your site.

## Reviewing a user account

1. Sign in with an account that has the appropriate rights.
2. Open the site's user administration interface.
3. Verify the account's status, contact information and group memberships.
4. Change only what is necessary, then save.
5. Confirm the result from a separate, less-privileged test account.

The exact form fields depend on the installed version and enabled authentication integrations.

## Managing groups

1. Review the features and rights associated with a group before assigning users.
2. Use groups for roles rather than assigning broad rights to each user individually.
3. Verify that administrators cannot accidentally elevate a nonadministrator to `Root`.
4. Test both allowed and denied actions after changing group assignments.

A user with `user.edit` does not automatically have every group-administration right. The 2.2.2 user handler checks `group.assign` in addition to user-edit rights for group assignment operations.

## Least-privilege acceptance test

When reviewing a new administrative role, verify both **permitted** and **denied** actions on an isolated staging site. Do not conduct these tests using real users or production personal data.

| Test account | Expected access | What to confirm |
| --- | --- | --- |
| Ordinary account without `user.edit` | Cannot use user administration | Denial is enforced by the server, not just hidden navigation |
| Account with `user.edit` but not `group.assign` | User editing subject to other checks; group assignment not authorized | Editing does not silently escalate access |
| Account without `group.edit` | Cannot use group administration | Requests are rejected even if the admin URL is entered directly |
| Appropriately authorized administrator | Only explicitly granted operations | Each form action requires the normal token and rights checks |

The [2.2.2 user administration handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/user.php) checks `user.edit` at entry and checks `group.assign` for membership-changing paths. The [group administration handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/group.php) checks `group.edit`. These checks do **not** imply that the roles above have no other rights; check each test account's effective memberships.

### After adjusting group membership

1. Save the change through the normal administrator interface, never by manually manipulating group tables on a live site.
2. Sign out, then verify access in a separate test session with the affected account.
3. Check a permitted action and a prohibited action. Record the operation and outcome, without copying user records.
4. Confirm the intended administrators retain access and that `Root` membership has not expanded.
5. If the change breaks access, use a documented recovery procedure based on a tested backup rather than bypassing authorization checks.

## Account-access review after an administrator change

Treat user administration, group membership and access to individual content as **separate questions**. An administrator account used to save a configuration change is not a reliable test of what a normal visitor can do.

1. Record the intended role and the exact action it must perform, such as editing users, managing groups or publishing a page.
2. Review the effective group memberships and feature rights of a disposable staging account, not just its displayed role name.
3. Test the allowed action using the normal application form. Verify that the action really persisted and did not merely render the form.
4. In a separate session, test an action outside that role. Directly visiting an administration URL must not bypass its server-side check.
5. Verify the content's **read permissions** separately by opening its public URL anonymously and with the relevant registered role.
6. Review whether granting membership introduces additional inherited privileges; confirm that the intended `Root` accounts still retain access.

| Administrative task | Representative feature right or condition | Separate check |
| --- | --- | --- |
| Edit user records | `user.edit` | Group assignment may also require `group.assign` |
| Change group settings | `group.edit` | Do not treat an edit form as proof that assigning membership is allowed |
| Edit Static Pages | `staticpages.edit` in the bundled plugin | Check per-page visibility and independent `staticpages.PHP` restriction |
| Export through the built-in database page | `Root` group for Geeklog 2.2.2 | Check the database engine and backup path; this is not a general user-management permission |

These are **representative checks**, not a complete authorization matrix for every installed plugin. Inspect the tagged handlers and active deployment before making security claims.

## Recovery planning for accidental lockout

Before modifying administrator memberships, ensure an independently tested recovery plan exists. Keep an authorized administrator account available for verification. If the intended account loses access, do not modify SQL tables blindly or bypass token checks; follow the [backup and recovery guide](https://geeklog-core.github.io/documentation/modern/administration/backup-and-recovery/index.html) and use the supported procedure for the installed release.

For a failed login or a 403 response, collect a sanitized timestamp and error message and follow the [troubleshooting guide](https://geeklog-core.github.io/documentation/modern/administration/troubleshooting/index.html). Avoid disclosing usernames, password hashes, sessions or account records in public issues.

## Protecting changes

The tagged 2.2.2 user and group administration handlers use `SEC_createToken()` and `SEC_checkToken()` to protect sensitive form actions. Keep these checks when extending the interface.

Never expose user passwords, password-reset tokens, two-factor authentication secrets or personal details in support requests.

## Verification checklist

- [x] Rights checks verified against `user.php` and `group.php` from Geeklog 2.2.2.
- [x] Group membership, token and feature-check functions verified in `lib-security.php`.
- [ ] Screens and interface labels confirmed on a running Geeklog 2.2.2 installation.
- [ ] Every management scenario tested with least-privileged accounts.
- [ ] Existing Wiki links and reuse attribution reviewed.

**Sources:** Geeklog 2.2.2 source files linked above; recovered Wiki titles in the 2024 inventory remain candidates for further merging.
