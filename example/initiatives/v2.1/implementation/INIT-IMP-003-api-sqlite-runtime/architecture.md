# API and SQLite runtime image architecture and specification

**Initiative:** `INIT-IMP-003`
**Status:** Proposed
**Last updated:** 2026-11-11

## Proposal standing

This record elaborates the frozen proposal without changing its source identity
or resolving any open choice.

## Specification boundary

Specify one D3 image and its source, database, maintenance, operational, and
verification behavior. Do not specify the D2 platform or D4-D6 products.

## Current repository baseline

No D3 implementation or qualified artifact exists at the captured base.

## Goals and non-goals

### Goals

- Preserve authoritative domain, HTTP, query, navigation, and SQLite semantics.
- Make initialization, migration, backup, restore, and failure deterministic.
- Produce traceable evidence for the exact D3 claim.
- Expose stable compatible interfaces to separately governed consumers.

### Non-goals

- Choose open paths, patch versions, tools, seams, owners, or split outcomes.
- Claim production, multi-user, remote, regulated, or downstream readiness.
- Treat realization notes, generated OpenAPI, or tests as requirement authority.

## Terms and identity

Record IDs, timestamps, revisions, hierarchy, query tokens, problem envelopes,
schema versions, image digests, and evidence identities must follow their
authoritative definitions and remain traceable across build and runtime.

## Architectural decisions

No initiative-local decision is final. Binding behavior comes from cited
authority; `API-01` through `API-06` own the remaining implementation choices.

## Boundaries and ownership

D3 owns the API process, SQLite database boundary, migrations, maintenance,
health/readiness behavior, and same-origin static-serving slot. D2 owns the
platform; D4-D6 own their clients and user experiences.

## Domain model and evidence/authoritative

### Model

Implement records, content, metadata, hierarchy, revisions, query results,
navigation, errors, and persistence state as specified by ARC contracts.

### Binding requirements

Validation, timestamp/UUID rules, concurrency, pagination, search semantics,
problem shapes, SQLite constraints, transactions, and recovery cannot be
weakened by implementation convenience.

## State and persistence

Durable state is SQLite data in its declared volume. Schema migrations are
ordered, transactional where required, restart-safe, and covered by verified
backup/restore. Static assets are immutable inputs, not database authority.

## Primary workflows

### Build and qualify

Resolve locked inputs; build immutably; scan and attest; initialize a clean
database; execute contract and fault vectors; retain evidence by artifact
identity.

### Operate and upgrade

Start through D2; check readiness; serve API and eligible static content;
perform explicit maintenance; migrate with backup and rollback controls; prove
recovery before compatibility claims.

## Interfaces and integration

Expose only declared `/api/v1`, health/readiness, static-hosting, maintenance,
volume, and build interfaces. Fixed internal topology and compatible matrices
must be explicit. No direct client access to SQLite is permitted.

## Failure and recovery

Invalid input, conflict, missing resources, deadlines, cancellation, database
lock/corruption, disk pressure, interrupted migration, failed health, and
restore failure produce bounded observable outcomes. Success may never mask
partial or indeterminate state.

## Security and authorization

Remain local, single-user, private/loopback, and non-production. Validate input,
queries, paths, and output; use least privilege and immutable dependencies;
exclude secrets and record payloads from logs/evidence; block actual or possible
ePHI.

## Observability and operations

Provide bounded structured operational signals for health, requests,
maintenance, migration, backup, restore, and faults. Signals must support
diagnosis without sensitive content or unbounded cardinality.

## Compatibility migration and rollout

Publish the exact D2/D3 matrix and D3 consumer contract. Use clean-install,
upgrade, backup/restore, and rollback gates. Compatibility is artifact-specific
and does not imply lifecycle state for D2 or D4-D6.

## Testing strategy

Cover applicable DOM, HTTP, SRCH, NAV, DB, CNT, OPS, and E2E vectors; contract
fixtures; OpenAPI drift checks; clean database and migration paths; concurrency,
fault, deadline, restart, corruption, and recovery cases. Test seams remain open
under `API-03`.

## Risks and edge cases

Semantic drift, unsafe query assembly, stale pagination, hierarchy cycles,
SQLite locking, interrupted migrations, corrupt backup, mutable dependencies,
leaky telemetry, and false compatibility claims block affected gates.

## Deferred work

All exact destinations, locks, injection seams, fixture/drift handling, review
owner, and possible split are deferred to `API-01` through `API-06`. Deferred
here means open work, not a lifecycle disposition.

## Architecture and specification acceptance

Not sought. A later workflow may review completeness and advance only with
explicit human authority; product acceptance and conformance remain separate.
