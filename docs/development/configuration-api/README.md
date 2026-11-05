# Configuration API for Geeklog developers

> **Geeklog 2.2.2 source-checked overview.** The recovered Wiki article `AddToConfiguration` was written for Geeklog 1.7.x. This guide identifies APIs present in 2.2.2 and deliberately avoids copying the old database-upgrade instructions as current practice.

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

## What remains to verify

- [x] `Configuration::add()` method signature in the Geeklog 2.2.2 distribution.
- [x] Installer uses `$c->add()` for configuration metadata.
- [ ] Whether specific plugin helper methods are supported and how they should be invoked.
- [ ] Detailed upgrade workflow and backward-compatibility requirements.
- [ ] Technical review of an end-to-end code example against a disposable 2.2.2 install.
- [ ] Licensing and Wiki contributor attribution.

**Provenance:** recovered Wiki `AddToConfiguration` (2024 backup), with 1.7.x-era instructions replaced by a version-scoped development overview.
