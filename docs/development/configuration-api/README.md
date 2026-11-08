# Configuration API for Geeklog developers

## Configuration storage and installation

Geeklog provides a `Configuration` class in [`system/classes/config.class.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/classes/config.class.php). The installer contains configuration definitions in [`public_html/admin/install/config-install.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/install/config-install.php).

In Geeklog 2.2.2, the configuration class exposes:

```php
public function add(
    $param_name,
    $default_value,
    $type,
    $subgroup,
    $fieldset = null,
    $selection_array = null,
    $sort = 0,
    $set = true,
    $group = 'Core',
    $tab = null
);
```

This is the observed **2.2.2 method signature**, not a recommendation to call it indiscriminately. The method interacts with persistent configuration state.

## Core configuration definitions

The 2.2.2 installer defines configuration groups and input elements through `$c->add(...)`. For example, the source creates site-related subgroup, tab and fieldset entries before site settings. These are framework metadata, not ordinary content records.

When changing Core configuration, verify where each setting is defined for both a **fresh installation** and an **upgrade path**. A setting that appears only on fresh installs can be missing on upgraded sites.

## Plugin-specific settings

The historic Wiki distinguishes Core configuration from plugin configuration. A plugin should not register all of its settings as Core values by default. Inspect the configuration conventions of a bundled plugin shipped with the **same target release**, and preserve its separate namespace or group.

## Safe development and migration process

1. Identify the configuration parameter, group, default, type and display placement.
2. Inspect the current 2.2.2 installer definition and relevant upgrade code.
3. Check value serialization and validation against the configuration class.
4. Make changes in a versioned plugin or Core migration, not through ad hoc production database updates.
5. Test clean install, upgrade, save and rollback paths separately.
6. Protect configuration forms with the project's access and CSRF controls.
7. Never commit live site secrets or database credentials to documentation examples.

## Configuration lifecycle: questions every plugin should answer

Adding a configuration option involves more than defining a default. Before modifying the `Configuration` class or a plugin's setup code, record the following contract:

| Concern | Question to validate |
| --- | --- |
| Identity | Is the option registered under the intended Core or plugin group? Is its name stable across upgrades? |
| Installation | Is the option present on a clean install, with the intended type and default? |
| Upgrade | How is the option introduced for existing installations, and what happens to previously customized values? |
| Administration | Which authorized users may view and modify the option, and which input types are accepted? |
| Validation | How are invalid values rejected, normalized or reported? |
| Removal | If the plugin is uninstalled or the option is retired, which settings and data should be retained? |
| Documentation | Is the setting described in the relevant release's online guide and context-sensitive help? |

A useful review sequence is: inspect the tagged `config.class.php` method, find the corresponding installer registration, trace any upgrade-specific path, then inspect the administrator form and its server-side authorization checks. The public method signature alone does **not** prove that a value is safe, properly validated or available to unauthorized users.

## Staging regression scenario for a changed option

1. Install the plugin or Core feature from scratch with the proposed default.
2. Change the value through the authorized configuration interface and verify persistence after reloading.
3. Start with a separate fixture representing the previous supported version, run the approved upgrade procedure and verify customized values are not silently reset.
4. Submit an invalid value and confirm the handler refuses or normalizes it as intended.
5. Verify denied configuration actions with a nonadministrator test account, including a direct URL or request when safe in staging.
6. Check the corresponding online documentation and any embedded help fragment for correct default, type and release scope.
7. Restore the staging state after the test. Record failures and any migration/rollback limits.

**Example scope note:** a `$c->add(...)` registration may describe a setting, but it does not guarantee that an upgrade script automatically introduces it on all existing sites. Treat clean-install behavior and upgrade behavior as independent acceptance tests.
