# API to SQLite persistence contract

**Architecture ID:** `ARC-CTR-004`  
**Status:** Accepted  
**Architecture revision:** `2.0.1`  
**Contract owner:** API persistence component owner and project architecture authority  
**Producer:** API repository/application layer  
**Consumer:** SQLite adapter and database  
**Last reviewed:** 2026-11-10  
**Supersedes:** Native-placement portions of `ARC-CTR-004@1.0.0`, preserved in [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md)  

## Purpose and scope

This contract defines the physical v1 schema, database identity, connection
configuration, transaction algorithms, capacity, migration, backup, integrity,
and restore behavior inside the mandatory Compose topology. The schema is an
internal persistence contract: only the API adapter during normal service and
the compatible, networkless maintenance command while the API is stopped may
consume it. Public clients depend on domain/HTTP contracts, not table or column
layout. No supported host process opens, copies, migrates, or inspects the live
SQLite files.

## Database identity and placement

| Property | Binding value |
|---|---|
| SQLite application ID | Decimal `1163416113` (`0x45585231`, ASCII-derived `EXR1`) |
| Initial schema/user version | `1` |
| Live files | `/var/lib/example-records/records.sqlite3` plus SQLite `-wal`/`-shm` and adjacent instance-lock file while open |
| Live storage | Compose named volume `record-data` mounted at `/var/lib/example-records`; bind mounts, anonymous volumes, container writable layers, and network/cloud-sync/removable paths are prohibited |
| Backup storage | Separate Compose named volume `record-backups`, mounted only by stopped-API maintenance operations; never mounted by `record-api` |
| Process ownership | Exactly one process/worker in the one `record-api` replica normally holds the instance lock; `record-maintenance` may open it only after proving the API is stopped and the lock is free |
| Filesystem identity | Numeric ownership `10001:10001`; runtime path and filename are fixed rather than host-configurable |
| Record capacity | 10,000 committed rows maximum |
| Text encoding | SQLite UTF-8 database; application values are canonical Unicode strings from `ARC-CTR-001` |

The serving API never creates or migrates a database. It verifies that the
fixed path, application ID, schema, migration hashes, permissions, and
integrity are compatible, and otherwise remains unready. Only the explicit
`record-maintenance initialize` command may create the initial database and it
must fail if live state already exists. Compose creates the named volume, not
the schema.

## Canonical schema v1

The initial migration creates semantically equivalent SQLite objects to the
following reviewed DDL. The delivered migration's normalized bytes and SHA-256
are recorded in `schema_migrations`; implementation-only naming changes require
contract review because tests/operations consume this schema.

```sql
PRAGMA application_id = 1163416113;

CREATE TABLE schema_migrations (
    version     INTEGER PRIMARY KEY CHECK (version > 0),
    name        TEXT NOT NULL UNIQUE,
    sha256      TEXT NOT NULL CHECK (
        length(sha256) = 64 AND sha256 = lower(sha256)
    ),
    applied_at  TEXT NOT NULL
) STRICT;

CREATE TABLE records (
    ordinal     INTEGER PRIMARY KEY AUTOINCREMENT,
    id          TEXT NOT NULL UNIQUE CHECK (
        length(id) = 36 AND id = lower(id)
    ),
    name        TEXT NOT NULL CHECK (
        length(name) BETWEEN 1 AND 120
        AND length(CAST(name AS BLOB)) <= 480
    ),
    value       TEXT NOT NULL CHECK (
        length(value) <= 4096
        AND length(CAST(value AS BLOB)) <= 16384
    ),
    revision    INTEGER NOT NULL DEFAULT 1 CHECK (revision >= 1),
    created_at  TEXT NOT NULL,
    updated_at  TEXT NOT NULL
) STRICT;

CREATE UNIQUE INDEX records_id_uq ON records(id);

CREATE TRIGGER records_id_immutable
BEFORE UPDATE OF id ON records
WHEN NEW.id IS NOT OLD.id
BEGIN
    SELECT RAISE(ABORT, 'record_id_immutable');
END;

CREATE TRIGGER records_ordinal_immutable
BEFORE UPDATE OF ordinal ON records
WHEN NEW.ordinal IS NOT OLD.ordinal
BEGIN
    SELECT RAISE(ABORT, 'record_ordinal_immutable');
END;

CREATE TRIGGER records_created_at_immutable
BEFORE UPDATE OF created_at ON records
WHEN NEW.created_at IS NOT OLD.created_at
BEGIN
    SELECT RAISE(ABORT, 'record_created_at_immutable');
END;

CREATE TRIGGER records_no_delete
BEFORE DELETE ON records
BEGIN
    SELECT RAISE(ABORT, 'record_delete_unsupported');
END;

PRAGMA user_version = 1;
```

The redundant unique index name makes the index identity explicit even though
the table constraint already requires uniqueness; a delivered migration may
use the table-created autoindex instead only if inspection/conformance does not
depend on the name. Domain validation remains responsible for full UUID syntax,
NFC, allowed-control, and timestamp format because SQLite checks above are
defense in depth, not an alternate semantic implementation.

## Internal column contract

| Column | Meaning | Write rule |
|---|---|---|
| `ordinal` | Positive, monotonically allocated total creation order | SQLite allocates; never updated/reused/exposed |
| `id` | Canonical public UUIDv4 | API supplies on create; unique; trigger forbids update |
| `name` | Canonical domain name | API supplies on create/material update only |
| `value` | Canonical domain value | API supplies on create/material update only |
| `revision` | Positive optimistic-concurrency counter | Starts 1; increment exactly once for material update under expected revision |
| `created_at` | Creation UTC timestamp | API supplies once; trigger forbids update |
| `updated_at` | Last material-update UTC timestamp | Equals `created_at` at creation; changes with revision only |

Timestamps use exactly `YYYY-MM-DDTHH:MM:SS.sssZ`, Gregorian UTC, millisecond
precision, generated from the service clock. They are not public ordering or
concurrency sources.

## Connection contract

Every opened connection must establish and verify:

```text
PRAGMA foreign_keys = ON
PRAGMA busy_timeout = 5000
PRAGMA journal_mode = WAL
PRAGMA synchronous = FULL
PRAGMA temp_store = MEMORY
PRAGMA trusted_schema = OFF
```

- `journal_mode=WAL` is set/verified during exclusive startup rather than
  raced on every request.
- Dynamic extension loading is disabled. No user-defined SQL function,
  collation, or `REGEXP` controls domain semantics.
- Connections are short-lived or drawn from a bounded internal pool; a
  connection is never concurrently used by multiple threads/tasks.
- SQL uses fixed statements and bound values. Field/mode/direction never
  interpolate SQL identifiers or clauses from raw request values.
- Read connections use transactions when multiple statements must share one
  view. Write connections always use the write algorithm below.

## Interface surface

| Repository operation | Required input | Success result | Failure result |
|---|---|---|---|
| `create` | Canonical generated ID/name/value/time | Stored row with allocated ordinal and revision 1 | Capacity, ID collision, busy, integrity, or storage failure; no partial row |
| `get_by_id` | Canonical ID | Complete canonical row or absent | Typed storage/integrity failure, never partial row |
| `update_if_revision` | Canonical ID, expected revision, canonical patch, update time | Updated row; unchanged row for normalized no-op; absent/conflict distinguished | Busy/integrity/storage failure with rollback |
| `max_ordinal` | None | Nonnegative max or zero | Typed storage failure |
| `scan_after` | `after`, `ceiling`, bounded batch | Rows in ascending ordinal within bounds | Typed storage failure |
| `scan_before` | `before`, lower bound, bounded batch | Rows in descending ordinal within bounds | Typed storage failure |
| `integrity_status` | Startup/maintenance context | Verified application/schema IDs and `quick_check=ok` | Readiness/startup failure |
| `maintenance_backup` | Stopped-API context and new generated artifact ID | Validated complete image and metadata in `record-backups` | Candidate failure; live DB unchanged and API remains stopped |

The repository returns typed outcomes. It must not make a busy/corrupt/invalid
row indistinguishable from absent, empty search, or collection boundary.

## Transaction algorithms

### Create

1. Acquire the one in-process write mutex.
2. Open a write connection; `BEGIN IMMEDIATE`.
3. Count rows inside the transaction. If count is 10,000, roll back and return
   capacity exceeded without inserting.
4. Insert canonical fields, revision 1, and equal create/update timestamps.
5. Read/validate the inserted row using `RETURNING` where the supported SQLite
   version provides it, otherwise by ID inside the transaction.
6. Commit, release mutex, then return success.

An ID unique violation permits at most two additional internally generated
UUID attempts (three total) while no attempt has committed. Other constraint
failures are integrity/programming errors and are not retried.

### Conditional update

1. Validate and normalize outside the transaction; acquire write mutex.
2. `BEGIN IMMEDIATE`; select current row by ID.
3. Return absent on no row. Return conflict if current revision differs.
4. If canonical patch values equal stored values, commit/close without UPDATE
   and return unchanged row/revision/timestamp.
5. Execute one parameterized UPDATE setting selected mutable fields,
   `revision = revision + 1`, and `updated_at`, constrained by both ID and
   expected revision.
6. Require exactly one changed row, read/validate it, commit, then return.

Any unexpected row count or invariant violation rolls back and becomes an
internal/integrity failure, not a revision conflict.

### Read/search/navigation

Reads are side-effect-free. Initial search obtains `MAX(ordinal)` and rows
within one read transaction. Subsequent cursor/neighbor requests use their
accepted ceiling but read current canonical values. The adapter returns bounded
ordered batches; API application code owns literal/regex membership.

## Migration contract

- Migration files are immutable, UTF-8, numbered positive integers with a
  descriptive name and recorded SHA-256.
- API startup compares `application_id`, `user_version`, migration rows,
  expected names, and hashes but never changes them. Missing, reordered,
  changed, duplicate, unknown, older, or newer migrations block readiness.
- A new install applies from version zero only through `docker compose run
  --rm record-maintenance initialize` while `record-api` is stopped.
- Every existing-database migration runs through the networkless maintenance
  service after proving the API is stopped and the instance lock is free.
- Before any existing database migration, maintenance creates and validates a
  new backup in `record-backups`. A convenience or metadata-only classification
  does not waive this v2 requirement.
- Apply one migration at a time, in ascending order, under exclusive instance
  ownership and a transaction wherever SQLite permits. Record its row and set
  `user_version` in the same successful unit.
- The maintenance image digest must declare compatibility with both the source
  and target schema. A migration command records image digest, migration
  hashes, source/target versions, input backup ID, result, and timestamp without
  record content.
- No automatic down migration exists. Rollback uses a compatible old binary
  with an unchanged schema or restores the mandatory pre-migration backup into
  a preserved/new `record-data` volume.
- Any migration changing domain meaning, public behavior, recovery, capacity,
  or compatibility requires prior architecture revision; schema convenience
  alone cannot alter those contracts.

## Backup and restore contract

### Backup

1. Stop `record-api`; maintenance proves the Compose service is not running and
   that the instance lock cannot be acquired by any competing owner.
2. Start `record-maintenance` with `network_mode: none` and its two declared
   named-volume mounts. The backup command opens the live source read-only at
   the application/SQLite layer and writes only a new candidate under
   `record-backups`; neither volume is exposed to a host SQLite process.
3. Select a generated destination that does not exist and is outside the live
   database basename/companion paths. Operator-supplied arbitrary filesystem
   paths are rejected.
4. Open the source read-only, checkpoint only through a separately guarded
   read-write preflight when required, and use SQLite's backup API to a
   temporary destination in `record-backups`.
5. Set restrictive ownership/mode and run application ID, schema, migration,
   row-decoding, capacity, and `PRAGMA quick_check` validation.
6. Record artifact ID, UTC timestamp, source image digest, architecture/schema
   versions, byte size, and SHA-256 in a sidecar without record content; then
   atomically rename the validated candidate inside `record-backups`.
7. A host export, when explicitly requested, copies only the already validated
   backup artifact through a bounded Compose command. It never bind-mounts or
   exports the live volume.

### Restore

1. Stop `record-api`; prove no instance lock is held. Restore refuses to run if
   the API container is running or ownership cannot be proven.
2. Run networkless maintenance; the restore command opens the selected backup
   artifact read-only and the intended `record-data` volume read-write.
   Validate the source sidecar/hash,
   application ID, supported schema, migrations, capacity, and `quick_check`
   without modifying the source.
3. Copy to a new candidate directory/file inside the live named volume, set
   numeric ownership/mode, and validate again.
4. Preserve the former live database and companions under a generated rollback
   name in the same volume and ensure a separate validated backup exists; never
   overwrite the only copy.
5. Atomically switch the fixed database filename when volume filesystem
   semantics permit, removing stale WAL/SHM only after exact path and ownership
   checks. Start the pinned API image and run readiness plus domain smoke tests.
6. On failure, stop the API, retain the failed candidate for bounded forensic
   handling, and switch back to the preserved former live set.

Merging two databases, importing backup rows as a restore shortcut, restoring
while the service runs, supplying an arbitrary host path, mounting the Docker
socket, or invoking host `sqlite3` is prohibited.

## Failure and recovery

| Failure condition | Detection | Required behavior | Recovery owner |
|---|---|---|---|
| Busy timeout | SQLite busy result after 5 s | Roll back and return typed busy outcome; no automatic write replay | Caller/operator |
| Constraint/trigger breach | SQLite constraint code/message mapped internally | Roll back; expose safe internal/integrity problem except documented collision | API/persistence owner |
| Disk full/read-only/I/O | SQLite extended result | Roll back; no success; readiness false when persistent | Operator |
| Corrupt/malformed row | Row decoder/integrity check | Do not return it; mark store unsafe | Operator restores verified backup |
| Migration mismatch/failure | Startup verifier/transaction | Block startup and preserve evidence/backup | Persistence owner/operator |
| Backup validation failure | Integrity/hash checks | Delete/quarantine candidate; live DB unchanged | Operator |
| Restore smoke failure | Readiness/domain vectors | Stop and roll back to preserved live set | Operator |

## Compatibility and verification

The public does not depend on schema layout, but every delivered service must
support its declared schema versions and preserve semantic state through
migration/restore. Removing support for a prior schema requires a release and
migration policy, not an implicit startup failure.

| Verification | Scenario | Evidence location |
|---|---|---|
| Fresh schema snapshot | Containerized initialize followed by API read-only startup verification of exact objects, pragmas, IDs, constraints, triggers | Future persistence evidence |
| Transaction/fault matrix | Commit, rollback, busy, disk error, collision, conflict, no-op | [`ARC-CTR-009`](24-conformance-contract.md) |
| Migration fixtures | Every declared prior version and interrupted migration | Future migration evidence |
| Backup/restore drill | Offline networkless maintenance, separate named volumes, full data/metadata/search comparison, and rollback | Future operations evidence |
| SQL injection/identifier review | All untrusted inputs remain bound data/enum branches | Future security evidence |
| Volume/mount isolation | Rendered Compose shows only API/maintenance can mount `record-data`, API cannot mount `record-backups`, and no live bind mount exists | Future operations evidence |

## Related records

- System boundary: [`ARC-BND-003`](15-sqlite-store-boundary.md)
- Decisions: [`ADR-001`](04-ADR-001-api-exclusive-persistence.md), [`ADR-002`](05-ADR-002-identity-order-and-concurrency.md)
- Governing evidence: [`AUTH-EX-001`](01-accepted-architecture-baseline.md)
- Superseded native deployment baseline: [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md)

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Defined v1 SQLite schema and repository semantics | User-authorized best-judgment architecture completion |
| 2026-11-10 | Fixed live state to a Compose named volume and moved initialize/migrate/backup/restore into stopped-API networkless maintenance | User's explicit full-Dockerization/no-host-services instruction |

