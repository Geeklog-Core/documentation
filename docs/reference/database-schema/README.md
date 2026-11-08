# Database schema and data model

This reference describes the **Geeklog 2.2.2** schema declared in its tagged installation scripts. Actual table names include the configured database table prefix. Enabled plugins may create further tables.

## Core tables by purpose

| Area | Tables defined in the installer |
| --- | --- |
| Articles and content | `stories`, `storysubmission`, `article_images`, `topics`, `blocks` |
| Comments and community | `comments`, `commentedits`, `commentnotifications`, `commentsubmissions`, `likes`, `trackback` |
| Users and sessions | `users`, `user_attributes`, `userautologin`, `sessions`, `backup_codes`, `tokens` |
| Rights and groups | `groups`, `group_assignments`, `features`, `access` |
| Configuration and operations | `conf_values`, `vars`, `plugins`, `routes`, `syndication`, `pingservice`, `ip_addresses`, `speedlimit`, `language_items` |

The tagged MySQL installation script declares **30** Core tables; the PostgreSQL script declares **31**, including an additional `topic_assignments` table. These are installer definitions, not a count of every table present in an upgraded site.

Sources: [MySQL table definitions](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/sql/mysql_tableanddata.php) and [PostgreSQL table definitions](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/sql/pgsql_tableanddata.php).

## Bundled plugin tables

These plugin installation scripts also define tables, depending on which plugins are installed:

| Plugin | Tables defined by its MySQL install script |
| --- | --- |
| Calendar | `events`, `eventsubmission`, `personal_events` |
| Links | `linkcategories`, `links`, `linksubmission` |
| Polls | `pollanswers`, `pollquestions`, `polltopics`, `pollvoters` |
| Spam-X | `spamx` |

Sources: [Calendar](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/plugins/calendar/sql/mysql_install.php), [Links](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/plugins/links/sql/mysql_install.php), [Polls](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/plugins/polls/sql/mysql_install.php), and [Spam-X](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/plugins/spamx/sql/mysql_install.php). Other bundled and third-party extensions may have different data requirements.

## Inspect your own installation safely

1. Identify your exact Geeklog version, database engine, configured table prefix and installed plugin versions.
2. Consult the schema scripts for the matching release. Use the [MySQL updates](https://github.com/Geeklog-Core/geeklog/tree/v2.2.2/sql/updates) and the appropriate plugin's `sql/*_updates.php` when examining an upgraded installation.
3. Use your database administrator's **read-only schema inspection** to list tables, columns and indexes. For example, on MySQL or MariaDB, `SHOW TABLES;` lists tables in the selected database; `SHOW CREATE TABLE gl_stories;` displays a table definition if the actual configured prefix is `gl_`.
4. Compare schema metadata against a separate, clean installation of the same Geeklog and plugin versions before diagnosing a mismatch.
5. Keep credentials and user records out of exported documentation. Use supported backup and restore procedures rather than directly changing live tables.

A shared column name does not establish an enforced foreign-key relationship. Use the actual engine-specific definitions when checking indexes, primary keys and constraints.

## Upgrades and compatibility

A fresh-install schema and the schema of an upgraded site can differ. The database engine, plugin versions and migration path determine which updates must be applied. Never replace a live database schema with installer SQL or use an older Wiki schema as a migration script. See [Maintenance and upgrades](../../administration/maintenance/index.html) and [Backup and recovery](../../administration/backup-and-recovery/index.html) before making changes.
