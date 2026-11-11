# TADp protocol project profile

**Project:** Traceable Architecture Design Protocol (TADp)

**Status:** Maintained

**Project owner:** User

**Technical owner:** User

**Human authority model:** Sole project owner

**Git repository root:** Parent repository root

**Default integration branch:** Not assumed; each initiative captures its actual base

**Pull-request remote:** origin; target branch must be verified per initiative

**Correlation revision effective point:** `007e791750a7dd5bca1befabd88cf83defde14b4`,
the coherent protected-update commit containing specification 09, affected
consumers, validator behavior, tests, and refreshed protocol and example locks

**Correlation migration ledger:** [Version-correlation migration ledger](initiatives/version-correlation-migration-ledger.md)

**Last reviewed:** 2026-11-11

## Purpose

The protocol project defines and maintains TADp's authoritative Codex
invariants, reusable workflow sources, validation tools, tests, and operating
documentation for traceable initiative work.

## Scope boundary

### Included

- Authoritative protocol evidence and explicitly authorized revisions.
- Reusable templates, workflow prompts, validation tools, regression tests,
  migration guidance, and protocol development documentation.

### Excluded

- Example-application product architecture, security decisions, products, and
  lifecycle claims, which remain owned by the example project.
- Acceptance, release, merge, deployment, or legacy migration claims that lack
  their own required evidence and authority.

## Directory map

| Logical record | Location | What belongs there | Owner |
|---|---|---|---|
| Binding evidence | [evidence/authoritative](evidence/authoritative/README.md) | Authoritative Codex protocol specifications and explicitly governed revisions | User |
| Contextual evidence | [evidence/non-authoritative](evidence/non-authoritative/README.md) | Realizations, observations, migration clues, and other non-binding context | User |
| Initiative records | [initiatives](initiatives/README.md) | Self-contained design, implementation, and planning initiative suites | User |
| Delivered products | [products](products/README.md), template, tools, tests, and docs | Reusable source and implementation outputs governed by accepted initiatives | User |

## Human ownership and approval

The User is the sole project owner, reviewer, and approver for human-decision
purposes. This convention does not merge technical component ownership,
source authority, external dependencies, placement, compatibility, security,
verification, release, or lifecycle gates.

The User's explicit response is required to accept an initiative, resolve an
open decision or assumption, authorize product execution when applicable,
revise an invariant, refresh a protected lock, publish, merge, release, or
deploy when the governing workflow requires that authority.

## Authority and traceability

1. [The authoritative LLM suite](evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md)
   governs protocol evidence, initiatives, lifecycle, Git, scope, decisions,
   and workflow behavior.
2. [The project initiative index](initiatives/initiative-index.md) owns
   canonical project-level initiative discovery and identity correlation.
3. Each initiative README owns its detailed scope and lifecycle standing;
   accepted initiatives authorize only their recorded type and bounded output.
4. Products and evidence retain their own verification and lifecycle limits.

Record a conflict instead of changing an earlier source to make a later record
appear aligned.

## Work identity and correlation

The initiative index is the canonical project-level location for work-version,
realization-suite, initiative, and dedicated-branch correlation. Other records
link to the row and retain authority only for their existing subject.
Specification 09 governs allocations from the project-recorded effective
point. The v1.0 row predates that point and remains under its linked `Deferred`
migration-ledger disposition; it is not retroactively treated as governed or
migrated.

## Operating cadence

| Event | Required review | Record to update |
|---|---|---|
| New or revised authoritative evidence | Authority, compatibility, migration, and consumer review | Authoritative suite, affected initiative, and project tracking |
| Initiative receives an ID or changes status | Scope, tuple identity, dependency, and lifecycle-evidence review | Initiative index, status view, and initiative README |
| Protected source changes | Exact authority, affected consumers, verification, and lock review | Protected source, lock, delivery record, and completion evidence |
| Validator or test changes | Accepted protocol basis and positive/negative regression review | Implementation initiative, tools, tests, and documentation |

## Git workflow

This project requires Git. Every initiative uses one dedicated branch created
from a captured clean base.

- **Initiative branch convention:** initiative/v<major>.<minor>-<initiative-slug>
- **Required checks:** protected-source check, full validator, regression
  tests, local-link review, and initiative-specific verification
- **Commit requirements:** coherent initiative-traceable commits; protected
  changes require the exact recorded lock authority and one-commit guard
- **Merge authority:** User; merge method must be explicitly authorized and is
  not assumed by this profile

## Change record

| Date | Change | Reason | Owner |
|---|---|---|---|
| 2026-11-10 | Instantiated the protocol project profile and branch convention | Provide the ownership and tracking prerequisite for INIT-DSN-001 | User |
| 2026-11-11 | Adopted the version-realization-initiative correlation revision and linked the legacy ledger | Establish the effective-point and compatibility records authorized by the repository prompt | User |
