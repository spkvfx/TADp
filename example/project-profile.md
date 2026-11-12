# Example Record Application project profile

**Project:** Example Record Application

**Status:** Active; correlation adoption records and the project-wide embedded-example-root exception are established

**Project owner:** User

**Technical owner:** User

**Human authority model:** Sole project authority; the User supplies every required human disposition

**TADp project root:** This installed `example/` directory

**Git repository root:** Project-specific exception `INV-CONFLICT-001` / `EX-GIT-DR-001` — treat `example/` as the project root while the directly enclosing repository or worktree at `..` supplies Git mechanics only

**Default integration branch:** `main`


**Correlation revision effective point:** `007e791750a7dd5bca1befabd88cf83defde14b4`, the coherent distribution commit containing specification 09, affected consumers, validator behavior, tests, and synchronized protected-source locks

**Correlation migration ledger:** [Version-correlation migration ledger](initiatives/version-correlation-migration-ledger.md)

**Coherence revision baseline:** `7b9d302b3dc7a94627518e42819a3130b5ba17d3`

**Work-conflict register:** [Work conflicts](initiatives/work-conflicts.md)

**Coherence adoption authority:** [COH-DR-001](decisions/COH-DR-001-initiative-coherence.md)

**Last reviewed:** 2026-11-12

## Purpose

The Example Record Application is a protocol demonstration for a local,
single-user record system. It preserves authoritative architecture and security
constraints, non-authoritative realization inputs, future initiative records,
and eventual product evidence without treating one record class as proof of
another.

## Scope boundary

### Included

- The example application's accepted architecture, security policy, contextual
  evidence, narrowly governed initiatives, and product records.
- The local Docker Compose, API, SQLite, Python SDK, CLI, and browser boundaries
  described by the accepted architecture, subject to separate initiative and
  delivery gates.

### Excluded

- Maintenance of the generic TADp protocol, reusable templates, protected
  invariant sources, validator semantics, or generic migration guidance.
- Production or regulated use, actual or possible ePHI, remote multi-user use,
  release, deployment, or product-completion claims unsupported by their own
  governing records and verification.

## Directory map

| Logical record | Location | What belongs there | Owner |
|---|---|---|---|
| Binding evidence | [evidence/authoritative](evidence/authoritative/README.md) | Accepted architecture, security policy, and the protected Codex invariant suite | User |
| Contextual evidence | [evidence/non-authoritative](evidence/non-authoritative/README.md) | Realizations and other non-binding proposal inputs | User |
| Initiative records | [initiatives](initiatives/README.md) | Self-contained proposed, accepted, active, and terminal initiative suites | User |
| Delivered products | [products](products/README.md) | Product destinations and evidence-backed delivery records | User |

## Human ownership and approval

The User is the sole project owner, human reviewer, and human approver. Codex
may prepare, align, implement, and verify work only within the applicable
workflow stage and recorded authority. The User's explicit response is required
to accept an initiative, resolve an assumption or open question, authorize an
exception or substantive revision, authorize product execution where required,
and authorize publication, merge, release, or deployment.

This convention applies only to human roles. Every technical component owner,
source authority, external dependency, placement, contract, security,
environment, verification, and release gate remains distinct and must be
preserved in the record that owns it.

## Authority and traceability

1. The [Codex invariant suite](evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md)
   governs evidence standing, initiative scope, lifecycle, Git, human decisions,
   workflow, and correlation identity.
2. [`ARC-SUITE-001@2.0.1`](evidence/authoritative/architecture/00-architecture-suite-index.md)
   governs the accepted technical shape and product boundaries.
3. [`SEC-NIST-SUITE-001@1.0.1`](evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md)
   and [`SEC-HIPAA-SUITE-001@1.0.1`](evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md)
   govern security, permitted data and use, safeguards, assurance, and successor
   gates.
4. The [initiative index](initiatives/initiative-index.md) owns current
   membership for the six Proposed initiatives. The
   [scope registry](initiatives/version-scopes.md) owns scope topology and
   integration state; each initiative README owns its lifecycle.

Record a conflict instead of changing an earlier source to make a later record
appear aligned. Link the conflict to its owner, required decision, resolution,
and effective date.

## Work identity and correlation

Each initiative belongs to one exact version scope and has its own ID,
source-note provenance and dedicated/shared execution assignment per revision
cycle. Scopes and notes may serve several independently acceptable initiatives.
Copies link to the canonical membership and scope records without gaining
authority or lifecycle standing.

The correlation revision is adopted from distribution commit
`007e791750a7dd5bca1befabd88cf83defde14b4`. The linked ledger preserves every
pre-effective version-like realization identity without inferring a partial new
tuple. The original `v0.0` realization remains `Unmigrated`. The six existing
initiatives now have explicit `Migrate` dispositions under the adopted scope
revision. Their cycle 1 allocations, dedicated branches and bases remain in
the [historical index](initiatives/legacy-correlation-index.md). Continuation
checkout preparation remains a separate recorded recovery gate.

The generic Git-root invariant remains unchanged outside this installed example.
The resolved
[`INV-CONFLICT-001`](evidence/authoritative/LLM/03_Codex_Invariant_Conflict_Register.md#inv-conflict-001--embedded-example-project-root-and-git-root-invariant)
and [`EX-GIT-DR-001`](initiatives/decision-receipts/EX-GIT-DR-001-enclosing-worktree-exception.md)
establish `example/` as the TADp project root for all current and future work
governed by this project. The directly enclosing repository or worktree
supplies Git mechanics only. The exception is not limited to the six mappings
in the migration prompt, but it does not expand the example project's scope
into its parent, a sibling, another scaffold, or another repository.

## Operating cadence

The [coherence revision](evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md)
applies to all six existing Proposed initiatives and subsequent work from the
recorded pre-adoption baseline. Their effort counts as work to reconcile;
their questions, assumptions, accepted authority boundaries, and lifecycle
standing do not change through adoption. At each material handoff, document
incompatible efforts and route completion feedback through the target's
governed workflow. Preserve historical closed claims until explicit reopening.

| Event | Required review | Record to update |
|---|---|---|
| New or revised authoritative evidence | Authority, compatibility, migration, and affected-consumer review | Evidence suite, affected initiative, profile, and tracking records |
| Initiative receives an execution assignment or changes lifecycle state | Scope, reciprocal identity, dependency, and lifecycle-evidence review | Initiative index, status view, suite index, and initiative README |
| Product work begins or delivery evidence changes | Accepted scope, target, security, compatibility, and verification review | Initiative execution record, product record, and completion evidence |
| Before every workflow handoff | Branch assignment, scope, provenance, source standing, blockers, and owned-record reconciliation | Records named by the stage exit contract |
| Initiative alignment, acceptance, or completion | Open effort, partial and delivered work, conflicts, and owned feedback | Work-conflict register, owning review, and completion evidence |

## Git workflow

`example/` is the project root. The directly enclosing repository or worktree
supplies the only Git metadata under the project-wide exception recorded by
[`EX-GIT-DR-001`](initiatives/decision-receipts/EX-GIT-DR-001-enclosing-worktree-exception.md).
Every initiative and other governed operation must capture the applicable
enclosing base branch and commit, use any required dedicated branch, and stage
only paths inside `example/`. Repository Git metadata is the only permitted
mutation outside the project root. The exception applies throughout this
installed example but nowhere else in the enclosing TADp repository.

- **Initiative branch convention:** `initiative/<scope>-<initiative-id-and-slug>` (dedicated); a recorded scope branch may also host shared execution
- **Required checks:** protected-source check, full validator, regression tests,
  local-link review, initiative-specific verification, and exact branch-diff
  review
- **Commit requirements:** coherent initiative-traceable commits; do not amend,
  rewrite, merge, or publish without the authority required by the applicable
  workflow stage
- **Merge authority:** User; target and merge method must be explicitly verified
  and authorized

## Change record

| Date | Change | Reason | Owner |
|---|---|---|---|
| 2026-11-11 | Instantiated the project profile, canonical initiative index, status view, and legacy correlation ledger | The correlation records were introduced after the example was first drafted; the User explicitly instructed their creation without authorizing inferred tuples | User |
| 2026-11-11 | Recorded the project-wide embedded-example-root exception | Treat `example/` as the complete example project's root while using the enclosing worktree only for Git mechanics and leaving the generic Git-root invariant unchanged elsewhere | User via [EX-GIT-DR-001](initiatives/decision-receipts/EX-GIT-DR-001-enclosing-worktree-exception.md) |
| 2026-11-12 | Adopted initiative coherence and completion-feedback controls from the captured pre-revision baseline | Apply User's COH-DR-001 rule to open effort without answering questions, accepting initiatives, or changing the Git-root exception | User |

## Version scope installation

**Version scope revision effective point:** `873021eef226576aebfc60b94f69886eb4da4a1c`

**Version scope migration ledger:** [Version scope dispositions](initiatives/version-scope-migration-ledger.md)

**Version scope registry:** [Scope registry](initiatives/version-scopes.md)

**Version scope installation authority:** [VSG-DR-001](decisions/VSG-DR-001-version-scope-grouping.md)

This project now adopts the installed revision under [EX-VSG-DR-001](initiatives/decision-receipts/EX-VSG-DR-001-initiative-migration.md), from baseline `9ab8c991222a026277a6f238bd0b64704b97f840`. The explicit migration ledger maps the six Proposed initiatives and preserves legacy claims and branch history. The previous integration default v1 is historical; main is the captured integration base for major scopes, while v1 retains its evidenced historical main creation. The enclosing-worktree exception remains in force.

Local integration is authorized only by an identified close/finalize instruction after all gates pass, into the recorded immediate parent. No such instruction is supplied by this migration. PRs remain human managed; pushes and ref removal require separate authority.

The historical tuple and dedicated-branch clauses above apply to cycle 1. Current preparation verifies scope membership, provenance, cycle and dedicated/shared assignment. Before Stage 5 on a continuation, [preparation recovery](initiatives/decision-receipts/EX-VSG-VER-001-migration-verification.md) must verify the actual checkout contains the migrated suite and adopted scaffold.
