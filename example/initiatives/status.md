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
| `v2.0` | [`INIT-IMP-002`](implementation/INIT-IMP-002-container-platform/README.md) | [`RZN-001-P2-PLATFORM-SUITE`](../evidence/non-authoritative/realizations/v2.0/00-RZN-001-P2-PLATFORM-suite-index.md) | `implementation` | Proposed | Stages 0–4 complete; Proposed record aligned | Stage 5 assumption-confirmation review | [`PLT-01`–`PLT-06`](implementation/INIT-IMP-002-container-platform/open-questions.md#decision-register) remain open; assumptions await human review | [Lifecycle history](implementation/INIT-IMP-002-container-platform/README.md#initiative-lifecycle) | User | 2026-11-11 |

The `v2.0` initiative now has a canonical correlation row and remains
`Proposed`. Other pre-effective realization suites remain non-authoritative
inputs with their dispositions recorded in the
[migration ledger](version-correlation-migration-ledger.md).

## Portfolio gates

| Gate ID | Outcome required | Depends on | Evidence required | Owner | State |
|---|---|---|---|---|---|
| EX-ADOPT-GIT-01 | A valid Git traceability boundary exists before governed tuple allocation | Project adoption boundary | [Project profile Git workflow](../project-profile.md#git-workflow), [resolved `INV-CONFLICT-001`](../evidence/authoritative/LLM/03_Codex_Invariant_Conflict_Register.md#inv-conflict-001--embedded-example-project-root-and-git-root-invariant), and [EX-GIT-DR-001](decision-receipts/EX-GIT-DR-001-enclosing-worktree-exception.md) | User | Passed project-wide for this installed example — `example/` is the project root and the directly enclosing worktree supplies Git mechanics only |
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
