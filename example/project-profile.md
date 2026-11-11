# Example Record Application project profile

**Project:** Example Record Application

**Status:** Active; correlation adoption records established, with the Git-root gate still open

**Project owner:** User

**Technical owner:** User

**Human authority model:** Sole project authority; the User supplies every required human disposition

**Git repository root:** Not satisfied — `example/` is embedded in the enclosing repository worktree at `..`; the parent repository is not a substitute for a project-local Git root

**Default integration branch:** `v1` in the enclosing repository; each initiative must capture its actual source branch and commit

**Pull-request remote:** `origin`; the target branch must be verified per initiative

**Correlation revision effective point:** `007e791750a7dd5bca1befabd88cf83defde14b4`, the coherent distribution commit containing specification 09, affected consumers, validator behavior, tests, and synchronized protected-source locks

**Correlation migration ledger:** [Version-correlation migration ledger](initiatives/version-correlation-migration-ledger.md)

**Last reviewed:** 2026-11-11

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
4. The [initiative index](initiatives/initiative-index.md) owns canonical
   project-level tuple identity after Stage 0 allocates it. No canonical tuple
   has yet been allocated.

Record a conflict instead of changing an earlier source to make a later record
appear aligned. Link the conflict to its owner, required decision, resolution,
and effective date.

## Work identity and correlation

The initiative index owns the canonical one-to-one mapping among work version,
realization suite, self-contained initiative, and dedicated Git branch. Copies
in suites, initiatives, status, delivery, completion, and Git records link to
that row and do not create authority or lifecycle standing.

The correlation revision is adopted from distribution commit
`007e791750a7dd5bca1befabd88cf83defde14b4`. The linked ledger preserves every
pre-effective version-like realization identity without inferring a partial new
tuple. The original `v0.0` realization remains `Unmigrated`; the six existing
`v1.0` through `v4.0` suites remain `Deferred` until their separately governed
migration runs on their own branches.

This record does not waive the Git-root invariant. Initiative allocation remains
blocked while `example/` is only an embedded scaffold rather than the root of
its own Git repository or Git worktree.

## Operating cadence

| Event | Required review | Record to update |
|---|---|---|
| New or revised authoritative evidence | Authority, compatibility, migration, and affected-consumer review | Evidence suite, affected initiative, profile, and tracking records |
| Initiative receives a tuple or changes lifecycle state | Scope, reciprocal identity, dependency, and lifecycle-evidence review | Initiative index, status view, suite index, and initiative README |
| Product work begins or delivery evidence changes | Accepted scope, target, security, compatibility, and verification review | Initiative execution record, product record, and completion evidence |
| Before every workflow handoff | Branch, tuple, source standing, blockers, and owned-record reconciliation | Records named by the stage exit contract |

## Git workflow

The scaffold currently fails the requirement that a TADp project be the root of
its own Git repository or Git worktree. The enclosing repository is on branch
`v1`, has remote `origin`, and currently supplies the only Git metadata. That
relationship may be used to preserve this adoption change, but it does not make
the embedded scaffold compliant or authorize initiative allocation.

- **Initiative branch convention:** `initiative/v<major>.<minor>-<initiative-slug>`
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
