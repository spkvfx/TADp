# Initiative coherence maintenance verification

**Record ID:** COH-VER-001

**Authority:** [COH-DR-001](COH-DR-001-initiative-coherence.md)

**Status:** Verified 2026-11-12

**Captured Git baseline:** `7b9d302b3dc7a94627518e42819a3130b5ba17d3`

**Branch:** `protocol/initiative-coherence-feedback`

This is direct protocol-maintenance evidence, not initiative acceptance,
example-product delivery, release, or deployment evidence.

## Scope and preservation review

The change adds specification 10 and reconciles the suite index, governance,
lifecycle, receipt and workflow consumers; the common initiative suite and
type-specific prompts; the project scaffold; validator and behavioral tests;
operating documentation; and protocol/example adoption records and locks.
The enclosing repository's root pre-commit hook runs both installed project
validators and protected-source guards; standalone reusable project hooks
retain their existing project boundary.

The installed example receives the same reusable rule. Its project-specific
invariant-conflict register and Git-root exception are preserved. No existing
initiative specification, open-question answer, decision, acceptance, or
terminal lifecycle is changed by this maintenance operation.

## Work and effort inventory

**Inventory baseline:** Captured pre-change Git commit above and current
project initiative indexes; review updated before final verification.

| Project and target | State | Work and effort considered | Finding and disposition |
|---|---|---|---|
| Protocol `INIT-DSN-001` (source project historical record) | Superseded | Prior correlation proposal and supersession history | Preserve closed records. New rule does not reopen its questions or change the prior claim. |
| Example `INIT-IMP-001` contract documentation | Proposed | D1 documentation proposal, questions, and shared contract boundaries | Adopt coherence controls in the example profile; no question is answered or product delivered. |
| Example `INIT-IMP-002` container platform | Proposed | Platform proposal and dependent product boundaries | Same prospective controls; intended work remains Proposed. |
| Example `INIT-IMP-003` API/SQLite runtime | Proposed | API and persistence proposal, source and compatibility dependencies | Same prospective controls; preserve human gates and specification standing. |
| Example `INIT-IMP-004` Python SDK | Proposed | SDK proposal, API dependency and verification boundaries | Same prospective controls; no implementation authority inferred. |
| Example `INIT-IMP-005` standalone CLI image | Proposed | CLI proposal, SDK/API dependencies and release boundary | Same prospective controls; no scope or decision changes. |
| Example `INIT-IMP-006` web application bundle | Proposed | Web proposal, API dependency and independent verification gates | Same prospective controls; no scope or decision changes. |

The example targets and their governing records are inventoried by its
`initiatives/initiative-index.md` and `initiatives/status.md`. This review
checks impact of this protocol change, not the full compatibility of all
future example products. No directly evidenced work conflict was identified
between this maintenance change and the listed claims. Empty work-conflict
registers do not certify a comprehensive semantic audit of all example work.

## Verification results

All checks used the configured PyCharm virtual environment, Python 3.11.11,
on Windows. The full validators used the captured pre-revision commit as
`--base-ref`, covering the complete maintenance change.

| Check | Protocol | Installed example |
|---|---|---|
| Full regression suite, including protected-source and validator behavior | 77 tests passed | 77 tests passed |
| Protected-source integrity | 0 errors | 0 errors |
| Full validator, including local links and coherence checks | 0 errors, 1 existing legacy warning | 0 errors, 1 existing legacy warning |
| Changed invariant, validator, and regression-test mirror comparison | Matched installed copies | Matched protocol sources |
| Complete reusable template tree and lock comparison | Matched installed copy | Matched protocol source |
| Git whitespace and changed-path review | Passed | Passed |

The existing warnings are the protocol's `Deferred` pre-effective v1.0
bootstrap and the example's `Unmigrated` original v0.0 realization. They remain
actionable under their original ledger dispositions; no migration is inferred.

The protected changes were reviewed against their prior locks before refresh;
each project reported only the expected 23 changed or added protected-source
findings. Both roots were then refreshed with authority
`decisions/COH-DR-001-initiative-coherence.md` and checked again successfully.

The regression cases include open Proposed effort, incomplete inventories,
documented conflict entry links, every closed lifecycle state, fresh reopening
authority, the unchanged-claim exception, removed or renamed records,
append-only corrections, independently governed children, baseline removal
and invalid-ref bypasses, and completion followed by an unlawful later
refinement within the reviewed Git history.

Existing protocol and example initiative suites and the example's authoritative
invariant-conflict register have no changes in the final diff.

**Guarded delivery commit:** `0ac8c32a95169c902fb14b0a6549af097a24274c`

The enclosing repository hook ran both project validators and staged
protected-source guards successfully for this commit. The one-commit
protected-update authority was not persisted. The first commit attempt was
blocked before recording a commit because the combined hook inherited
relative Git paths; normalizing its Git directory, worktree, and actual index
to absolute paths corrected the nested-project check without bypassing it.

## Limits and remaining work

Machine checks cannot establish that every semantic conflict was discovered,
an authority claim is authentic, or a product is correct. Existing questions
and legacy correlation warnings keep their recorded owners and re-entry
conditions. Adoption does not erase them.
