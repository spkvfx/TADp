# TADp protocol initiative index

**Index owner:** User

**Last reviewed:** 2026-11-10

**Review cadence:** At initiative preparation and every lifecycle transition

## Authority boundary

This index owns the canonical project-level correlation row and initiative
discovery. It does not accept an initiative, resolve a decision, prove
delivery, or replace the initiative README's lifecycle authority.

## Initiative and correlation register

| Work version | Realization suite | Initiative ID | Name | Type | Status | Dedicated branch | Captured base | Predecessor or successor | Record location | Lifecycle evidence | Owner | Next gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v1.0 | [RZN-TADP-001-VERSION-CORRELATION-SUITE](../evidence/non-authoritative/realizations/v1.0/00-RZN-TADP-001-VERSION-CORRELATION-suite-index.md) | INIT-DSN-001 | Version-realization-suite-initiative correlation | design | Proposed | initiative/v1.0-version-realization-correlation | v1 at d05f334e854431716275a59c980f0c909d88d002 | None; first protocol work-version allocation | [Initiative README](design/INIT-DSN-001-version-realization-correlation/README.md) | [Draft proposal](design/INIT-DSN-001-version-realization-correlation/proposal/proposal.md); Stage 0 commit e2677f2 | User | Complete aligned baseline, resolve human gates, and request Stage 7 acceptance |

## Cross-initiative dependencies

| Dependent initiative | Depends on | Required state | Owner | Blocking? |
|---|---|---|---|---|
| Planned validator implementation consumer, identity not yet allocated | INIT-DSN-001 | Accepted correlation design and exact validator contract | User | Yes for executable enforcement; no for design acceptance |

## Correlation rules

- Each row is project-local and retains its immutable identities and captured
  Git base even if later status or branch availability changes.
- The realization-suite index and initiative README link back to this row.
- Lifecycle status is copied from the initiative README and must cite its
  supporting receipt or verification; this index cannot create the state.
- A missing or proposed consumer is not assigned a work version, suite,
  initiative ID, or branch until its own Stage 0 preparation.

## Status update rules

- Add a row when an initiative receives an ID and record location.
- Reconcile the row when tuple identity, lifecycle evidence, owner,
  dependency, or next gate changes; never silently renumber or reuse identity.
- Keep completed, cancelled, and superseded rows as traceable history.
- Link conflicts and decisions to their initiative-local records.
- Keep this register coherent with [status.md](status.md) and each initiative
  README. A row establishes identity and discoverability, not acceptance,
  implementation authority, qualification, completion, or release readiness.
