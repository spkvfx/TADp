# API and SQLite runtime image delivery steps

**Initiative:** `INIT-IMP-003`
**Status:** Proposed planning only
**Last updated:** 2026-11-11

## Current-state analysis

The repository has authoritative D3 contracts and non-authoritative realization
notes, but no governed D3 product source, image, migration set, or qualification
record.

## Delivery strategy

Deliver contract core, persistence, operations/recovery, then qualify one exact
immutable image. Every step is gated by unresolved decisions and later lifecycle
authority.

## Step 1 - Establish locked source and build graph

### Objective

Create the authorized D3 product structure and reproducible dependency graph.

### Expected output locations

Open under `API-01`; do not infer paths.

### Planned output

Domain/API/query/persistence source skeleton, locked runtime/build inputs,
image definition, artifact metadata, and evidence identity.

### Dependencies

`API-01`, `API-02`, `API-06`, compatible D2 interface.

### Evidence / authoritative

ADR-007, ARC-CTR-001 through ARC-CTR-004, ARC-CTR-008/009, security suites.

### Migration and rollback

No data migration in this step; build changes must be revertible by immutable
artifact identity.

### Verification

Reproducible build, dependency provenance, scans, and clean image startup.

### Acceptance

Later review only; no acceptance is recorded here.

## Step 2 - Implement contract and SQLite behavior

### Objective

Implement domain, HTTP, search/navigation, schema, transactions, and problems.

### Expected output locations

Authorized D3 paths from `API-01`.

### Planned output

Models, services, handlers, query/navigation logic, schema and clean-init
migration, contract fixtures, and negative-path behavior.

### Dependencies

Step 1, `API-03`, `API-04`.

### Evidence / authoritative

Domain/API/search/navigation/SQLite contracts and DOM/HTTP/SRCH/NAV/DB vectors.

### Migration and rollback

Schema changes require ordered migration, backup protection, and compatible
rollback/recovery design.

### Verification

Contract, property, concurrency, pagination, query-safety, transaction, and
database-fault tests.

### Acceptance

Exact authoritative outcomes pass for the built artifact.

## Step 3 - Implement operations and recovery

### Objective

Add health, maintenance, migration, backup/restore, static slot, and telemetry.

### Expected output locations

Authorized D3 runtime, maintenance, static, and evidence paths.

### Planned output

Health/readiness endpoints, explicit maintenance commands, recovery checks,
bounded logs/metrics, and safe static-serving boundary.

### Dependencies

Step 2 and `API-03` through `API-05`.

### Evidence / authoritative

Operations/security contract, security suites, CNT/OPS/DB/E2E vectors.

### Migration and rollback

Exercise interrupted migration, locked/corrupt database, failed restore,
restart, and previous-artifact recovery.

### Verification

Fault injection, health transitions, maintenance isolation, data-leak checks,
backup/restore drills, and static path safety.

### Acceptance

No critical finding or unsupported recovery claim remains.

## Step 4 - Qualify the D3 outcome

### Objective

Produce an artifact-bound conformance record for D3 alone.

### Expected output locations

Authorized evidence and product records.

### Planned output

Matrix results, drift report, security/risk review, compatibility declaration,
source-currency check, evidence manifest, and human review packet.

### Dependencies

Steps 1-3 and all blocking decisions.

### Evidence / authoritative

ARC-CTR-009 and the exact vector/source mappings in this initiative.

### Migration and rollback

Release disposition identifies safe fallback, database compatibility, and
evidence invalidation conditions.

### Verification

Clean install, upgrade, backup/restore, fault, security, and end-to-end matrix.

### Acceptance

Only explicit later human authority may advance lifecycle or accept the product.

## Validation matrix

| Area | Required evidence | Blocking gap |
|---|---|---|
| Domain/API | DOM and HTTP vectors | Semantic or problem-shape drift |
| Search/navigation | SRCH and NAV vectors | Unsafe or nondeterministic behavior |
| Persistence | DB vectors and recovery drills | Migration or restore uncertainty |
| Runtime/operations | CNT/OPS/E2E vectors | Health, fault, or telemetry gap |
| Security/data use | Scans and policy review | Secret, sensitive-data, or ePHI risk |
| Compatibility | Exact D2/D3 and consumer interface record | Unbounded or untested matrix |

## Final acceptance criteria

All binding requirements map to passing artifact-specific evidence; assumptions
and decisions have authority; product and lifecycle records are coherent; no
claim depends on D4-D6 completion. This file itself satisfies none of those
criteria.
