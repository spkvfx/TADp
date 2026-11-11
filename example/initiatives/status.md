# Example Record Application initiative status

**Status owner:** User

**Last reviewed:** 2026-11-11

**Review cadence:** At every initiative lifecycle, gate, or correlation change

## Authority boundary

This record summarizes current lifecycle standing and gates. Each initiative's
own record remains authoritative for its scope, decisions, assumptions, and
detailed state. A status row must cite the evidence that supports its claim.
Listing work as `Proposed`, `Accepted`, `In progress`, or `Completed` here does
not create that state without the required initiative-local authority and
verification.

## Current status

| Work version | Initiative ID | Realization suite | Type | Status | Current milestone | Next gate | Blockers or holds | Status evidence | Owner | Last updated |
|---|---|---|---|---|---|---|---|---|---|---|

No initiative has a canonical correlation row or lifecycle status. The
pre-effective realization suites remain non-authoritative inputs with the
dispositions recorded in the
[migration ledger](version-correlation-migration-ledger.md).

## Portfolio gates

| Gate ID | Outcome required | Depends on | Evidence required | Owner | State |
|---|---|---|---|---|---|
| EX-ADOPT-GIT-01 | `example/` is the root of its own Git repository or Git worktree before governed tuple allocation | Project adoption boundary | [Project profile Git workflow](../project-profile.md#git-workflow) and read-only Git-root verification | User | Blocked — the scaffold is embedded in the enclosing repository |
| EX-ADOPT-CORR-01 | Correlation profile, canonical index, status view, and complete legacy dispositions are structurally valid | Distribution commit `007e791750a7dd5bca1befabd88cf83defde14b4` | 2026-11-11 protected-source check, validator, regression tests, and adoption diff review | User | Passed — protected sources: 0 errors; validator: 0 errors and 7 actionable legacy warnings; regression tests: 51 passed |

## Maintenance rules

- Update a row only from current initiative and verification evidence.
- Record only lifecycle states and transitions permitted by the authoritative
  lifecycle specification. `Reopened` is an event recorded in the initiative
  history, not a status value.
- Link a blocker to the record that owns its resolution; do not restate an
  unresolved decision as if this status page could decide it.
- Keep completed, cancelled, and superseded rows until an authorized retention
  rule permits archival.
- Reconcile this record with [initiative-index.md](initiative-index.md),
  applicable parent and subinitiative indexes, and affected initiative READMEs
  in the same reviewed change.
- Copy work-version and suite identity from the canonical correlation row;
  never allocate, renumber, or infer identity in this status view.
- A parent, subinitiative, release, or version boundary does not rewrite the
  identity, authority, or classification of retained proposal sources.
