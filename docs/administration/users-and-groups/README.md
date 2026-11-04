# Managing users and groups

> **Geeklog 2.2.2 administration guide — draft.** This guide is grounded in the tagged 2.2.2 source and deliberately avoids assuming that historical Wiki screenshots or menus are unchanged.

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
