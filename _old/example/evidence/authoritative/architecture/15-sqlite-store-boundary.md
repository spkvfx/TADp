# SQLite record store system boundary

**Architecture ID:** `ARC-BND-003`  
**Status:** Accepted  
**Architecture revision:** `2.0.1`  
**Owner:** API persistence component owner under a future accepted initiative  
**Last reviewed:** 2026-11-10  
**Related records:** [`ADR-001`](04-ADR-001-api-exclusive-persistence.md), [`ADR-002`](05-ADR-002-identity-order-and-concurrency.md), [`ARC-CTR-004`](16-sqlite-persistence-contract.md), [`ARC-CTR-008`](23-operations-security-contract.md)  

## Boundary statement

The SQLite store boundary comprises Compose named volume `record-data`, fixed
container path `/var/lib/example-records/records.sqlite3`, SQLite-managed
`-wal`/`-shm` companions while open, adjacent exclusive instance lock, ordered
migration resources embedded in the API/maintenance image, and the API-owned
adapter. It is authoritative for one Compose project. `record-api` is the
normal owner; networkless `record-maintenance` may open the volume only while
API is stopped. The boundary excludes host bind mounts/paths/tools,
client/test/build containers, backup volume as live state, arbitrary SQL,
network filesystems, multiple API replicas, and domain behavior above the port.

## Responsibilities

| Responsibility | Boundary owner | Explicitly outside this boundary |
|---|---|---|
| Persist records and internal metadata atomically | SQLite adapter and SQLite engine | HTTP status, SDK models, UI messages, or command parsing |
| Allocate monotonically increasing, non-reused ordinals | `records.ordinal INTEGER PRIMARY KEY AUTOINCREMENT` | UUID generation or user-visible numbering |
| Enforce ID uniqueness and defense-in-depth immutability | Schema constraints and trigger | Creation policy and HTTP validation |
| Serialize writes and apply expected revision predicates | API write mutex plus transactional SQL | Client conflict-resolution choices |
| Track/verify schema during runtime | API startup verifier | Applying schema changes while serving |
| Initialize and apply ordered migrations | Stopped-API maintenance container | Runtime auto-generation from Pydantic or host migration tools |
| Create/validate/restore backups | Networkless maintenance container using `record-backups` | Treating backup volume as live authority or mounting it in API |
| Report integrity, busy, full, I/O, permission, and schema failures | Adapter error mapping | Suppressing failures or presenting them as successful empty results |

## Inputs and outputs

| Direction | Counterparty | Interface or artifact | Validated by | Compatibility rule |
|---|---|---|---|---|
| Inbound | API application layer | Typed repository commands and queries | Repository adapter and domain types | Adapter interface changes require synchronized API and persistence revision |
| Inbound | Maintenance container | Named initialize/check/migrate/backup/restore command, ordered migration, fixed paths | API-stopped/lock guard, command allowlist, checksum/version/volume validation | Apply exactly once; no arbitrary shell/SQL/file path |
| Inbound | Local operator through Compose | Explicit maintenance command and backup artifact ID/export destination | Compose profile, guard, overwrite/path checks | Host never receives live-volume mount or runs SQLite |
| Outbound | API application layer | Domain rows or typed repository failures | Row decoder and invariant validation | Invalid/corrupt row is an integrity failure, not a partial record |
| Outbound | `record-backups`/explicit export | SQLite-consistent image plus metadata/hash | Maintenance validation | Partial candidate is not accepted; export never becomes live authority |
| Outbound | Readiness | Schema/integrity/writability status | Startup and health probes | Readiness false when safe required operations cannot complete |

## State and authority

| State or decision | System of record | Write authority | Recovery or reconciliation rule |
|---|---|---|---|
| Live records and internal metadata | Fixed DB in `record-data` named volume | API adapter normally; maintenance only with API stopped | Restore validated backup into preserved/new volume; never merge files |
| Current schema version | `PRAGMA user_version` plus migration table | Maintenance migration runner; API verifies read/write compatibility | Refuse uninitialized/unknown/newer; never guess/downgrade |
| SQLite application identity | `PRAGMA application_id` | Initial migration only | Refuse a database with a different nonzero application ID |
| Instance ownership | Lock inside `record-data` held by API; checked by maintenance | API startup/shutdown and maintenance preflight | Compose state plus OS lock state; filename alone insufficient |
| Backup image | Versioned file/metadata in `record-backups` or explicit exported artifact | Maintenance container only | Becomes live only after stopped-API validated restore |

## Invariants and failure boundaries

- The live database must use the Compose-managed `record-data` named volume.
  Bind mounts, Docker socket/host filesystem mounts, NFS/SMB/cloud-sync,
  removable media, tmpfs, anonymous volume, and container writable layer are
  prohibited live locations.
- Data files are owned by numeric `10001:10001` and accessible only to API or
  guarded maintenance containers. CLI/web/test/build images never mount them.
- Every connection enables foreign keys, a 5,000 ms busy timeout, WAL journal
  mode, and `synchronous=FULL`; configuration failure stops readiness.
- The API container uses one process/worker and one in-process write mutex. A write begins
  with `BEGIN IMMEDIATE`, either commits completely or rolls back completely,
  and is never automatically replayed.
- Reads may use separate read-only transactions/connections, but no connection
  object is shared concurrently across threads or tasks.
- Capacity is at most 10,000 records. At capacity, create fails without
  allocating a committed record; reads and updates remain available.
- No supported operation deletes a record or manually resets/reuses an
  ordinal.
- A database error cannot be translated to an empty search, missing record, or
  successful update unless that is the actual committed domain result.
- Migration is never applied by a serving API. Maintenance first creates and
  validates a backup in `record-backups`; failure leaves API stopped and prior
  volume preserved or explicitly recoverable.

## Recovery ownership

| Condition | Required store behavior | Operator action |
|---|---|---|
| Busy within timeout | Roll back current operation and return typed busy failure | Retry manually after cause clears; writes are not auto-replayed |
| Named volume full/read-only/permission/I/O failure | Roll back/readiness false | Stop API; use guarded maintenance/volume procedure; restart and integrity-check |
| Integrity check failure | Do not serve | Stop/preserve volume, create forensic export, restore verified backup to preserved/new volume |
| Uninitialized/unknown/newer schema | API does not initialize/migrate/downgrade | Run accepted maintenance init/migrate or compatible image while API stopped |
| Interrupted backup/export | Live data unchanged; candidate incomplete | Quarantine candidate and rerun maintenance command |
| Failed restore validation | Do not replace current live contents | Keep/preserve prior volume; investigate candidate in maintenance container |

## Verification and change control

| Claim | Verification | Evidence location |
|---|---|---|
| Store is inaccessible except API normal runtime and exclusive maintenance | Rendered Compose mount graph, image deps, volume permissions, competing-container tests | Future API/operations evidence |
| Atomic writes and revision predicates prevent partial/stale updates | Transaction rollback and racing-update tests | Required by `ARC-CTR-009` |
| Migrations preserve or explicitly transform all records | Migration fixtures from every supported prior schema | Future persistence completion evidence |
| Backup is restorable and semantically identical | Backup/restore drill plus record/query comparison | Future operations completion evidence |
| Capacity and corruption fail safely | Fault-injection tests | Future persistence evidence |

Changes require persistence owner review plus project architecture authority.
Schema changes must also revise `ARC-CTR-004`, migration and recovery evidence,
API/domain compatibility analysis, and every affected product contract.

