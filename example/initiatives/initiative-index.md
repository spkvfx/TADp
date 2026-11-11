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

No governed tuple has been allocated. Pre-effective realization identities are
preserved in the
[version-correlation migration ledger](version-correlation-migration-ledger.md)
and must not be copied here until Stage 0 creates a complete reciprocal tuple.

## Cross-initiative dependencies

| Dependent initiative | Depends on | Required state | Owner | Blocking? |
|---|---|---|---|---|

No initiative dependency has been registered. Dependency order recorded in
architecture or realization evidence does not create an initiative or prove a
predecessor complete.

## Adoption gate

Canonical allocation is blocked while the example scaffold is not the root of
its own Git repository or Git worktree. See the
[project profile](../project-profile.md#git-workflow). This blocker does not
allocate an initiative, branch, version, or lifecycle state.

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
