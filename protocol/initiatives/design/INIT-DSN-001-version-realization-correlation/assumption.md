# Version-realization-suite-initiative correlation assumption

**Initiative:** INIT-DSN-001-version-realization-correlation

**Status:** Proposed

**Last updated:** 2026-11-10

**Assumption review:** Assumed aligned; awaiting validation

This document records high-confidence intended boundaries. Each row remains
Assumed aligned until an explicit human response is captured in a decision
receipt and reconciled.

The User's 2026-11-10 clarification that realization artifacts are always
non-authoritative and belong only under
`evidence/non-authoritative/realizations/**` is a source-directed boundary, not
an assumption awaiting Codex disposition. Its initiative acceptance and
delivery effects remain gated separately.

## Review method

The permitted dispositions are Confirmed, Corrected, or Not applicable. A
receipt must preserve the exact prompt and response before a disposition
changes. Genuine uncertainty belongs in [open-questions.md](open-questions.md).

## Boundary between assumption and open questions

| Assumption | Decision that may remain open |
|---|---|
| The protocol project may allocate unused work version v1.0 to this design | Exact meaning of requested but unobserved legacy v3.1 and v4.1 identities |
| Protocol and example protected sources must carry identical normative semantics | Project-specific migration rows may differ because their observed records differ |
| Validator work is a different initiative type | Its future version, suite, initiative ID, branch, acceptance, and execution evidence are not yet allocated |

## Product and scope

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| VRC-A01 | INIT-DSN-001 owns only the authoritative correlation design, synchronized reusable specification sources, and initiative-local migration/handoff evidence; executable validation is excluded | Proposal, scope, acceptance claim, roadmap, and implementation handoff | Assumed aligned | Current type boundary requires a separate implementation consumer |

## Domain and authority

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| VRC-A02 | The project initiative index owns the canonical tuple row while the initiative README remains lifecycle authority and each evidence source retains its classification; realization artifacts remain permanently non-authoritative at the canonical evidence path | Correlation model, templates, status rules, realization consumers, and validator contract | Assumed aligned | Copies link to the canonical row and do not become competing authority; accepted derivative claims are recorded separately |

## System boundaries and dependencies

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| VRC-A03 | The protected protocol and example LLM/template counterparts must express identical normative correlation semantics | Protected path matrix, parity verification, locks, and migration guidance | Assumed aligned | Project-relative paths may differ only where actual placement requires it |

## Data and lifecycle

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| VRC-A04 | Protocol work version v1.0 is unused, immutable after allocation, and correctly correlated to this suite, initiative, and branch | Suite index, project row, README, branch, lineage, and successor rules | Assumed aligned | No competing protocol work-version registry or allocation was found |

## Operations security and failure behavior

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| VRC-A05 | Protected locks are refreshed only after authorized source review and verification, using the exact user instruction as lock authority | Delivery order, verification, lock metadata, and commit gate | Assumed aligned | A stale lock is expected during review and is never suppressed early |

## Cross-initiative compatibility

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| VRC-A06 | Existing legacy evidence remains immutable in meaning; bare vN becomes vN.0 only for a proven notation-only mapping, while broad or dot-scoped ambiguity stays unresolved until explicitly decided | Migration ledger, compatibility guidance, and future migration initiatives | Assumed aligned | No legacy lifecycle or completion state may be invented |

## Validation record

| Review cycle | Reviewer | Date | Outcome | Notes |
|---|---|---|---|---|
| Initial assumption review | User | 2026-11-10 | Assumed aligned; awaiting validation | Stage 5 must present each stable row and create receipts before changing dispositions |

## Change discipline

Keep proposal and realization sources traceable. Reconcile every receipt with
architecture, source mapping, roadmap, steps, suite index, project row, status,
and this record in the same change.
