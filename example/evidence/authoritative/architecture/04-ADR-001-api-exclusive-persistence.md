# API-exclusive live persistence

**Decision ID:** `ADR-001`  
**Status:** Accepted  
**Architecture revision:** `2.0.1`  
**Decision owner:** User, project authority  
**Decision date:** 2026-11-10  
**Supersedes / superseded by:** Not applicable  
**Related initiative:** Not applicable - direct project-architecture instruction  

## Decision question

Which component may access the live SQLite database, and through what paths do
the SDK, CLI, and browser obtain record capabilities?

## Context and binding evidence

| Source | Precise claim or constraint | Effect on this decision |
|---|---|---|
| [`AUTH-EX-001.1`](01-accepted-architecture-baseline.md) | The API container is the normal live-store owner; offline maintenance is mutually exclusive | Requires one mediated runtime authority plus a bounded recovery exception |
| [`RZN-001`](../../non-authoritative/realizations/v0.0/RZN-001-example-record-application.md), system boundary and Q10-Q11 | Direct versus API access was unresolved; all surfaces should share capabilities | Context only; requires an accepted path |
| [`ARC-AUT-001`](02-authority-and-source-disposition.md) | Best judgment and the later Docker-only revision are explicitly authorized | Authorizes the selected v2 topology |

## Decision

The `record-api` container is the only component permitted to open the live
SQLite database during normal operation or execute user-facing repository
operations. The API exposes the complete record contract under `/api/v1`.

The only exception is the `record-maintenance` one-shot container. It may mount
and open `record-data` solely while `record-api` is stopped, its instance lock
is absent, and the selected initialize/check/migrate/backup/restore command
requires access. It has no network and is not a second serving authority.

- The Python SDK communicates only through `/api/v1` from a declared container.
- The CLI container communicates only through its installed public SDK and the
  private Compose DNS name `record-api:8000`; it mounts no state.
- The browser adapter communicates directly with the host-loopback same-origin
  `/api/v1` published by Docker.
- The browser does not use the Python SDK; both are independent clients of the
  same HTTP contract.
- CLI/SDK and browser requests terminate on the identical `/api/v1` router and
  route set. The internal/private and public/loopback origins do not authorize
  consumer-specific paths, representations, or behavior.
- Operators may initialize/check/migrate/backup/restore only through the
  networkless stopped-API maintenance container. Host SQLite/ad hoc SQL and
  direct Docker-volume editing are not product interfaces.
- A shared domain or contract source may be used at build time, but no client
  may import the API repository adapter or share a live database connection.

No native-host, degraded, offline, embedded, sidecar, or direct-SQL fallback is
permitted when the API is unavailable. The API remains the consistency,
validation, search, navigation, concurrency, and error-semantics boundary.

## Consequences

### Benefits

- All surfaces observe one validation and mutation policy.
- Search/regex and navigation cannot drift across SQLite, CLI, and browser.
- ID immutability and conditional updates have one enforcement point plus
  database defense in depth.
- SQLite locking and normal transactions remain API-internal; migration and
  recovery use the explicitly bounded maintenance container.
- SDK, CLI, and web can be verified against one versioned API contract.

### Costs, risks, and required follow-up

- CLI and web data operations require the API process to be running.
- CLI "standalone" means an independently versioned/runnable OCI image, not
  offline, embedded, or host-installed.
- API availability becomes a user-visible dependency; clients need explicit
  unavailable and indeterminate-write behavior.
- The browser needs its own thin typed HTTP adapter because a Python SDK cannot
  run natively in the selected browser boundary.
- Future offline, embedded, or multi-process use requires a successor decision
  rather than a convenience bypass.
- Dependency scans and architecture tests must prove that non-API products do
  not import/use SQLite or repository modules.

## Alternatives considered

| Alternative | Why it was not selected | Reconsideration trigger |
|---|---|---|
| CLI and web open SQLite directly | Duplicates validation/search/concurrency and exposes schema/locking as a public contract | An explicitly accepted offline-first product with its own synchronization architecture |
| Shared in-process data library used directly by all clients/containers | Browser cannot consume Python implementation; still creates multiple database owners/processes | A replacement single-process desktop architecture |
| CLI embeds/starts the API automatically | Conflates products and lifecycle/operations; hides failure ownership | A separately accepted desktop/launcher product |
| SDK talks to SQLite while web uses API | Gives SDK/CLI different semantics and compatibility obligations | Requires another explicit major architecture revision |
| Host or generic utility container opens the volume | Bypasses compatibility, lock, image, and recovery controls | Never without an accepted maintenance successor |

## Acceptance and verification

| Required result | How it is verified | Evidence location |
|---|---|---|
| Only API/maintenance image code contains the SQLite adapter, with mutually exclusive mounts | Image dependency graph, rendered Compose mounts, and competing-container tests | Future API/operations completion evidence |
| Equivalent CLI and web operations use one `/api/v1` route/behavior | Route inventory plus cross-origin cross-surface conformance vectors | [`ARC-CTR-009`](24-conformance-contract.md) |
| API outage causes explicit unavailability, never fallback | Fault-injected SDK/CLI/web tests | Future product evidence |
| Maintenance paths never mutate a running store ad hoc | Backup/restore and instance-lock tests | Future operations evidence |

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Accepted API-exclusive persistence and client integration paths | User-authorized best-judgment architecture method recorded in `ARC-AUT-001` |
| 2026-11-10 | Reconciled API exclusivity with Docker-only runtime and a networkless stopped-API maintenance exception | User's Dockerization/no-host-services revision; predecessor recorded in `ARC-REV-001` |
| 2026-11-10 | Fixed CLI/SDK and web to one identical `/api/v1` router and route contract | User's explicit shared-API-path instruction recorded in `ARC-AUT-001` |

