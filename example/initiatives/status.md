# Example Record Application initiative status

**Status owner:** User

**Last reviewed:** 2026-11-12

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
| `v1.0` | [`INIT-IMP-001`](v1.0/implementation/INIT-IMP-001-contract-documentation/README.md) | [`RZN-001-P1-DOCS-SUITE`](../evidence/non-authoritative/realizations/v1.0/00-RZN-001-P1-DOCS-suite-index.md) | `implementation` | Proposed | Stages 0–4 complete; Proposed record aligned | Stage 5 assumption review under the authorized decision method | [`DOC-01`–`DOC-06`](v1.0/implementation/INIT-IMP-001-contract-documentation/open-questions.md#decision-register) remain open; assumptions await the authorized review | [Lifecycle history](v1.0/implementation/INIT-IMP-001-contract-documentation/README.md#initiative-lifecycle) and aligned initiative record | User | 2026-11-12 |
| `v2.0` | [`INIT-IMP-002`](v2.0/implementation/INIT-IMP-002-container-platform/README.md) | [`RZN-001-P2-PLATFORM-SUITE`](../evidence/non-authoritative/realizations/v2.0/00-RZN-001-P2-PLATFORM-suite-index.md) | `implementation` | Proposed | Stages 0–4 complete; Proposed record aligned | Stage 5 assumption review under the authorized decision method | [`PLT-01`–`PLT-06`](v2.0/implementation/INIT-IMP-002-container-platform/open-questions.md#decision-register) remain open; assumptions await the authorized review | [Lifecycle history](v2.0/implementation/INIT-IMP-002-container-platform/README.md#initiative-lifecycle) | User | 2026-11-12 |
| `v2.1` | [`INIT-IMP-003`](v2.1/implementation/INIT-IMP-003-api-sqlite-runtime/README.md) | [`RZN-001-P2-API-SQLITE-SUITE`](../evidence/non-authoritative/realizations/v2.1/00-RZN-001-P2-API-SQLITE-suite-index.md) | `implementation` | Proposed | Stages 0–4 complete; Proposed record aligned | Stage 5 assumption review under the authorized decision method | [`API-01`–`API-06`](v2.1/implementation/INIT-IMP-003-api-sqlite-runtime/open-questions.md#decision-register) remain open; assumptions await the authorized review | [Lifecycle history](v2.1/implementation/INIT-IMP-003-api-sqlite-runtime/README.md#initiative-lifecycle) | User | 2026-11-12 |
| `v2.2` | [`INIT-IMP-004`](v2.2/implementation/INIT-IMP-004-python-sdk/README.md) | [`RZN-001-P2-SDK-SUITE`](../evidence/non-authoritative/realizations/v2.2/00-RZN-001-P2-SDK-suite-index.md) | `implementation` | Proposed | Stages 0–4 complete; Proposed record aligned | Stage 5 assumption review under the authorized decision method | [`SDK-01`–`SDK-06`](v2.2/implementation/INIT-IMP-004-python-sdk/open-questions.md#decision-register) remain open; assumptions await the authorized review | [Lifecycle history](v2.2/implementation/INIT-IMP-004-python-sdk/README.md#initiative-lifecycle) | User | 2026-11-12 |
| `v3.0` | [`INIT-IMP-005`](v3.0/implementation/INIT-IMP-005-standalone-cli-image/README.md) | [`RZN-001-P3-CLI-SUITE`](../evidence/non-authoritative/realizations/v3.0/00-RZN-001-P3-CLI-suite-index.md) | `implementation` | Proposed | Stages 0–4 complete; Proposed record aligned | Stage 5 assumption review under the authorized decision method | [`CLI-01`–`CLI-06`](v3.0/implementation/INIT-IMP-005-standalone-cli-image/open-questions.md#decision-register) remain open; assumptions await the authorized review | [Lifecycle history](v3.0/implementation/INIT-IMP-005-standalone-cli-image/README.md#initiative-lifecycle) | User | 2026-11-12 |
| `v4.0` | [`INIT-IMP-006`](v4.0/implementation/INIT-IMP-006-web-application-bundle/README.md) | [`RZN-001-P4-WEB-SUITE`](../evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md) | `implementation` | Proposed | Stages 0–4 complete; Proposed record aligned | Stage 5 assumption review under the authorized decision method | [`WEB-01`–`WEB-07`](v4.0/implementation/INIT-IMP-006-web-application-bundle/open-questions.md#decision-register) remain open; assumptions await the authorized review | [Lifecycle history](v4.0/implementation/INIT-IMP-006-web-application-bundle/README.md#initiative-lifecycle) | User | 2026-11-12 |

All six named initiatives have canonical correlation rows and remain
`Proposed`. The original broad `v0.0` realization remains non-authoritative
under its `Unmigrated` disposition in the
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

## Current scope status

[Scope registry](version-scopes.md) owns scope coordination and integration;
[initiative membership](initiative-index.md#initiative-and-correlation-register)
owns the six current assignments. Ten scopes are registered by the explicit
project migration, including four major ancestors and six member scopes.
All scopes remain open and all initiatives remain Proposed. The
[scope migration dispositions](version-scope-migration-ledger.md) preserve
their prior revisions, paths and assignments.


## Version-scope migration handoff

The six current paths above are grouped by their unchanged source scopes. [Current membership](initiative-index.md) owns cycle 2 continuation assignments; [scope registry](version-scopes.md) owns topology. All six remain Proposed with their original Stage 5 human reviews pending. Administrative migration does not pass those reviews. Before invoking Stage 5, [branch preparation recovery](decision-receipts/EX-VSG-VER-001-migration-verification.md) must confirm the assigned checkout contains the adopted scaffold and migrated suite. No scope is closed or merged.

## Autonomous review preflight: 2026-11-12

Execution of the [assumption and question prompt](../prompts/answer-assumptions-and-open-questions.md)
stopped before templates 05/06 at the unexcepted preparation checks.
[EX-AQ-PREFLIGHT-001](decision-receipts/EX-VSG-VER-001-migration-verification.md#assumption-and-question-review-preflight-2026-11-12)
records the actual `v1` checkout, missing current suites on all six assigned
cycle 2 branches, and validator error `TADP048` (the recorded scope effective
point is absent from current history). Protection passed. All 36 assumptions
and 37 questions remain unresolved; all six initiatives remain `Proposed`
and none is ready for Stage 7. The prompt supplies bounded autonomous decision
authority, but no preparation or protected-baseline installation waiver.
User-authorized Stage 0/adoption recovery owns the blocker and recorded
re-entry checks; no per-item approval is requested. The preflight tracking
addenda remain uncommitted pending a valid execution/recovery checkout.

## Current preparation recovery: 2026-11-12

Under [EX-PREP-DR-001](decision-receipts/EX-PREP-DR-001-branch-recovery.md),
the original adoption history and captured main ancestry were merged into
`v1`, preserving existing file content. The ten scope branches and six
assigned initiative branches received the verified administrative baseline.
All six actual assigned checkouts passed full validation, protection and
local-link checks. [Actual results](decision-receipts/EX-VSG-VER-001-migration-verification.md#ex-prep-001-verified-recovery-results)
supersede the preceding preparation/ancestry blockers; their earlier failed
evidence is retained. The earlier uncommitted preflight notes are now preserved
in authority commit `c69fa54`.

All six initiatives remain `Proposed`. Their next gate is the assumption and
question review, starting with D1 under the separately authorized automatic
method. All 36 assumptions and 37 questions remain unresolved; Stage 7 is not
ready. No product or scope is accepted, completed or closed, and no work is
merged upward into `main`. Historical refs remain available. Final tracking
updates are committed and fast-forwarded as administrative preparation, not
initiative delivery integration.
