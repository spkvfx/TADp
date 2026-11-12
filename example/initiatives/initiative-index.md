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
| `v1.0` | [`RZN-001-P1-DOCS-SUITE`](../evidence/non-authoritative/realizations/v1.0/00-RZN-001-P1-DOCS-suite-index.md) | [`INIT-IMP-001`](implementation/INIT-IMP-001-contract-documentation/README.md) | Contract documentation | `implementation` | Proposed | `initiative/v1.0-contract-documentation` | `v1` | `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b` | None | [`implementation/INIT-IMP-001-contract-documentation`](implementation/INIT-IMP-001-contract-documentation/README.md) | [Lifecycle history](implementation/INIT-IMP-001-contract-documentation/README.md#initiative-lifecycle), [Migrate disposition](version-correlation-migration-ledger.md#migration-ledger), preparation commit `f27b09bf8580668073dbf2265466ae5f4d14a737` | Not removed | User | Stage 5 assumption confirmation review |
| `v2.0` | [`RZN-001-P2-PLATFORM-SUITE`](../evidence/non-authoritative/realizations/v2.0/00-RZN-001-P2-PLATFORM-suite-index.md) | [`INIT-IMP-002`](implementation/INIT-IMP-002-container-platform/README.md) | Container platform and runtime packaging | `implementation` | Proposed | `initiative/v2.0-container-platform` | `v1` | `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b` | None | [`implementation/INIT-IMP-002-container-platform`](implementation/INIT-IMP-002-container-platform/README.md) | [Lifecycle history](implementation/INIT-IMP-002-container-platform/README.md#initiative-lifecycle), [Migrate disposition](version-correlation-migration-ledger.md#migration-ledger), preparation commit `d888ea74d36477ba2a192c1eb5531aca6003fe25` | Not removed | User | Stage 5 assumption-confirmation review |
| `v2.1` | [`RZN-001-P2-API-SQLITE-SUITE`](../evidence/non-authoritative/realizations/v2.1/00-RZN-001-P2-API-SQLITE-suite-index.md) | [`INIT-IMP-003`](implementation/INIT-IMP-003-api-sqlite-runtime/README.md) | API and SQLite runtime image | `implementation` | Proposed | `initiative/v2.1-api-sqlite-runtime` | `v1` | `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b` | None | [`implementation/INIT-IMP-003-api-sqlite-runtime`](implementation/INIT-IMP-003-api-sqlite-runtime/README.md) | [Lifecycle history](implementation/INIT-IMP-003-api-sqlite-runtime/README.md#initiative-lifecycle), [Migrate disposition](version-correlation-migration-ledger.md#migration-ledger), preparation commit `eaebb511c49c4f451af8516504763d9529b00967` | Not removed | User | Stage 5 assumption-confirmation review |
| `v2.2` | [`RZN-001-P2-SDK-SUITE`](../evidence/non-authoritative/realizations/v2.2/00-RZN-001-P2-SDK-suite-index.md) | [`INIT-IMP-004`](implementation/INIT-IMP-004-python-sdk/README.md) | Python SDK artifact | `implementation` | Proposed | `initiative/v2.2-python-sdk` | `v1` | `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b` | None | [`implementation/INIT-IMP-004-python-sdk`](implementation/INIT-IMP-004-python-sdk/README.md) | [Lifecycle history](implementation/INIT-IMP-004-python-sdk/README.md#initiative-lifecycle), [Migrate disposition](version-correlation-migration-ledger.md#migration-ledger), preparation commit `9ea472f8287a38f324edce41662a07058e1bd5e1` | Not removed | User | Stage 5 assumption-confirmation review |
| `v3.0` | [`RZN-001-P3-CLI-SUITE`](../evidence/non-authoritative/realizations/v3.0/00-RZN-001-P3-CLI-suite-index.md) | [`INIT-IMP-005`](implementation/INIT-IMP-005-standalone-cli-image/README.md) | Standalone CLI image | `implementation` | Proposed | `initiative/v3.0-standalone-cli-image` | `v1` | `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b` | None | [`implementation/INIT-IMP-005-standalone-cli-image`](implementation/INIT-IMP-005-standalone-cli-image/README.md) | [Lifecycle history](implementation/INIT-IMP-005-standalone-cli-image/README.md#initiative-lifecycle), [Migrate disposition](version-correlation-migration-ledger.md#migration-ledger), preparation commit `af45ea7b2d98decd875eb793fadc16558ffae764` | Not removed | User | Stage 5 assumption-confirmation review |
| `v4.0` | [`RZN-001-P4-WEB-SUITE`](../evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md) | [`INIT-IMP-006`](implementation/INIT-IMP-006-web-application-bundle/README.md) | Web application bundle | `implementation` | Proposed | `initiative/v4.0-web-application-bundle` | `v1` | `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b` | None | [`implementation/INIT-IMP-006-web-application-bundle`](implementation/INIT-IMP-006-web-application-bundle/README.md) | [Lifecycle history](implementation/INIT-IMP-006-web-application-bundle/README.md#initiative-lifecycle), [Migrate disposition](version-correlation-migration-ledger.md#migration-ledger), preparation commit `370ffcfa1bee8763a23ef5481716e6b093a11e42` | Not removed | User | Stage 5 assumption-confirmation review |

All six named tuples were allocated through the pre-effective-suite migration
path. The original broad `v0.0` realization remains preserved under its
`Unmigrated` disposition in the
[version-correlation migration ledger](version-correlation-migration-ledger.md)
and is not inferred into any of these tuples.

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

## Prospective scope membership

The preceding register retains historical correlation and lifecycle evidence.
No initiative has been migrated into the new model. New membership after
adoption is owned here, with scopes registered in [version-scopes.md](version-scopes.md).
See the [scope migration ledger](version-scope-migration-ledger.md).

| Scope | Initiative ID | Type | Record location | Source notes | Execution branch | Execution mode | Captured base ref | Captured base commit | Integration target | Revision cycle | Lifecycle evidence | Integration evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
