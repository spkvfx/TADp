# TADp initiative index

**Index owner:** Current repository owner (respective owner in a fork); see OWNERSHIP-001

**Last reviewed:** 2026-11-14

**Review cadence:** At intake, alignment, acceptance, completion, or material drift

## Authority boundary

This is the canonical membership/provenance index with exactly one row per
initiative. [Version scopes](version-scopes.md) owns scopes;
each initiative README owns lifecycle. Source catalogs remain permanently
non-authoritative. Correlation creates no acceptance, delivery or release.

## Initiative and correlation register

| Scope | Initiative ID | Type | Record location | Source notes | Execution branch | Execution mode | Captured base ref | Captured base commit | Integration target | Revision cycle | Lifecycle evidence | Integration evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v2 | TADP-001 | implementation | [Owned assumption and question review decisions](v2/implementation/tadp-001-owned-review-decisions/README.md) | [RZN-001](../evidence/non-authoritative/realizations/v2/RZN-001-owned-review-decisions.md) | initiative/v2-tadp-001-owned-review-decisions | Dedicated | v2 | 9c9fd1daad655fd58349c005f8d31a4f52790cc9 | v2 | 1 | [Proposed history](v2/implementation/tadp-001-owned-review-decisions/README.md#lifecycle-history) | Not integrated; no closure authority |

Each initiative has one immutable scope, one narrow claim and one active
execution assignment per revision cycle. Multiple initiatives may share scope,
notes/suites and a declared scope branch. IDs remain independent of scope
numbers. Preserve exact source and selected target scopes, fit/routing rationale,
predecessor/successor links and branch-removal authority in reciprocal records.
No row or historical branch identity may be reassigned to unrelated work.

## Source and execution history

| Initiative | Cycle | Source suite ID/path | Source note ID/path | Source scope | Target scope | Routing disposition and rationale | Branch/mode | Captured base ref/commit | Integration target | Prior/replacement relationship | Authority and evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TADP-001 | 1 | [RZN-SUITE-001](../evidence/non-authoritative/realizations/v2/00-review-decisions-suite-index.md) | [RZN-001](../evidence/non-authoritative/realizations/v2/RZN-001-owned-review-decisions.md) | v2 | v2 | New narrow candidate outcome; no existing initiative fits | initiative/v2-tadp-001-owned-review-decisions / Dedicated | v2 / 9c9fd1daad655fd58349c005f8d31a4f52790cc9 | v2; not integrated | Initial; no predecessor | [Codex placement under exact intake](../evidence/non-authoritative/assumption-question-review/intake.md) |

Append contributing sources and new-cycle/continuation assignments; do not
overwrite earlier allocation/base/integration history. The current row points
to that history and current lifecycle evidence. Serialize shared writes and
preserve concurrent additions instead of restoring an older index snapshot.

## Cross-initiative dependencies

| Dependent initiative | Depends on | Required state | Owner | Blocking? |
|---|---|---|---|---|

Review proposed and partial effort without promoting authority. Record
incompatible work in [work-conflicts.md](work-conflicts.md).
Routing authority and necessary reopening follow the exact adopted intake
method; changed claims still require renewed human acceptance before delivery.

## Status update rules

Preserve closed rows and prior claims. Update copied current fields from their
owners, not inference. A closed scope needs recorded reopening before new
membership. Legacy records stay under their complete non-inferred ledger and
governing revision until explicit migration; historical paths are retained.

## Installation inventory

The setup event below remains historical. TADP-001 is the first subsequent
allocation, under the exact intake recorded above; no upstream work is imported.

No scopes, realization notes, initiatives, prior decisions, products, or lifecycle
claims were imported or allocated. The setup authority and verification records
are linked from [SETUP-001](../decisions/SETUP-001.md). Existing upstream work and
Git branch names do not become this project's membership. Ownership follows the current repository owner under OWNERSHIP-001; prospective adoption is recorded in [the profile](../project-profile.md) under ADOPTION-001.
