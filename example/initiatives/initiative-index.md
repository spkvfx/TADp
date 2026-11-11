# Example Record Application initiative index

**Index owner:** User

**Last reviewed:** 2026-11-11

**Review cadence:** At Stage 0 preparation and every lifecycle or correlation change

## Authority boundary

This index owns canonical project-level tuple identity and initiative discovery.
It does not accept an initiative, resolve a decision, prove delivery, or replace
an initiative README's lifecycle authority.

## Initiative and correlation register

| Work version | Realization suite | Initiative ID | Name | Type | Status | Dedicated branch | Captured base branch | Captured base commit | Predecessor or successor | Record location | Lifecycle evidence | Branch removal evidence | Owner | Next gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `v2.1` | [`RZN-001-P2-API-SQLITE-SUITE`](../evidence/non-authoritative/realizations/v2.1/00-RZN-001-P2-API-SQLITE-suite-index.md) | [`INIT-IMP-003`](implementation/INIT-IMP-003-api-sqlite-runtime/README.md) | API and SQLite runtime image | `implementation` | Proposed | `initiative/v2.1-api-sqlite-runtime` | `v1` | `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b` | None | [`implementation/INIT-IMP-003-api-sqlite-runtime`](implementation/INIT-IMP-003-api-sqlite-runtime/README.md) | [Lifecycle history](implementation/INIT-IMP-003-api-sqlite-runtime/README.md#initiative-lifecycle), [Migrate disposition](version-correlation-migration-ledger.md#migration-ledger) — preparation commit pending | Not removed | User | Stage 1 proposal creation |

The `v2.1` tuple was allocated through the pre-effective-suite migration path.
Other pre-effective realization identities remain preserved in the
[version-correlation migration ledger](version-correlation-migration-ledger.md)
until their own Stage 0 branch allocates a complete reciprocal tuple.

## Cross-initiative dependencies

| Dependent initiative | Depends on | Required state | Owner | Blocking? |
|---|---|---|---|---|

No initiative dependency has been registered. Dependency order recorded in
architecture or realization evidence does not create an initiative or prove a
predecessor complete.

## Adoption gate

The project-wide
[`EX-GIT-DR-001`](decision-receipts/EX-GIT-DR-001-enclosing-worktree-exception.md)
resolution satisfies the Git-root precondition by treating `example/` as the
TADp project root and the directly enclosing repository or worktree as Git
mechanics only. It applies to every otherwise-authorized allocation in this
installed example; it is not limited to the current
[migration prompt](../prompts/create-v1.0-through-v4.0-initiatives.md#exact-initiative-map).
The exception allocates no tuple and waives no identity, migration, or
lifecycle gate. Stage 0 must still create each complete reciprocal row on its
exact dedicated branch.

## Status update rules

- Add a row only as part of the Stage 0 preparation unit that allocates an
  unused version, suite, initiative, and branch from a captured base.
- Preserve allocated identity and base fields immutably. Update copied status,
  lifecycle evidence, branch-removal evidence, owner, dependency, or next gate
  only from their owning records.
- Keep completed, cancelled, and superseded rows as traceable history.
- Link conflicts and major decisions to the initiative's own record; do not put
  unreviewed decisions only in this index.
- Keep this registry coherent with [status.md](status.md), the realization-suite
  index, the initiative README, and any applicable parent or subinitiative
  indexes. A row establishes identity and discoverability, not evidence
  authority, acceptance, implementation, qualification, completion, or release
  readiness.
- Never reuse a version or branch. If a terminal branch ref is separately
  removed, retain the recorded name and link its removal authority.
