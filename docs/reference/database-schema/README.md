# Database schema and data model

> **Historical Wiki data-model page is not a current schema.** The recovered `DatabaseSchema` article describes an older Geeklog 1.4.1 database. Do **not** use its SQL definitions to create or upgrade a Geeklog 2.2.2 or 2.2.3 database.

## Get the correct schema

For any installation, schema inspection should start with the **tagged installer and upgrade code** for that exact Geeklog release, plus the installed plugin versions. Different database engines and plugin combinations can have different structures.

1. Record Geeklog release, database engine and installed plugins.
2. Inspect the target release's schema-install and migration scripts.
3. Install a fresh copy in a disposable database; do not test schema migrations against production.
4. Export schema metadata with a database-native read-only method suited to your engine.
5. Compare a clean installation to a supported upgraded installation and record differences requiring review.
6. Never run historical SQL from the Wiki against an existing Geeklog site.

## Source-to-data reference matrix

| Data area | Questions the eventual verified reference should answer |
| --- | --- |
| Content and topics | Which entities and keys represent articles, topics and publication state? |
| Users and groups | Which relations and features affect effective rights? |
| Configuration | Where are defaults, customized values and version transitions managed? |
| Plugins | Which tables are Core-owned and which belong to optional plugins? |
| Updates | How are schema versions and migration scripts coordinated? |

This table is a **research checklist**, not a claim that the current schema was reverse-engineered.

## Safe documentation artifact

Publish a generated, version-pinned schema inventory (table name, purpose, key relations, applicable engine, source script, upgrade changes) only after verifying it against the release source and an isolated installation. Remove database credentials and all user records from examples.

## Still missing

The actual 2.2.2 table inventory and relationships, PostgreSQL-specific differences, plugin schema inventories and real upgrade comparisons. Database schema documentation for Geeklog 2.2.3 must be generated separately from its own release baseline.
