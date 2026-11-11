# Standalone CLI image assumption

**Initiative:** Standalone CLI image
**Status:** Proposed
**Last updated:** 2026-11-11
**Assumption review:** Assumed aligned; awaiting validation

Every row remains unconfirmed until explicit human review.

## Review method

Only explicit human instruction changes `Assumed aligned`. Questions are
tracked in [open-questions.md](open-questions.md).

## Boundary between assumption and open questions

| Assumption | Implementation question that may remain open |
|---|---|
| One D5 image owns the CLI outcome | Paths, libraries, version policy, seams, owner, split |
| Required process/output safeguards bind | Evidence and compatible artifact matrix |

## Product and scope

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `CLI-A01` | One one-shot CLI image has one D5 owner, lifecycle, and completion claim. | Scope, product, roadmap | Assumed aligned | Awaiting human validation |

## Domain and authority

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `CLI-A02` | CLI contracts own interaction semantics; only the public D4 wheel supplies domain/API behavior. | Architecture, mapping, tests | Assumed aligned | Awaiting human validation |

## System boundaries and dependencies

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `CLI-A03` | D5 runs one-shot in D2, targets fixed private D3, uses exact D4, and exposes no mounts/ports/socket. | Interfaces, compatibility, security | Assumed aligned | Awaiting human validation |

## Data and lifecycle

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `CLI-A04` | Record content appears only as explicit success output for synthetic/de-identified data; diagnostics stay redacted. | Output, fixtures, logging | Assumed aligned | Awaiting human validation |

## Operations security and failure behavior

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `CLI-A05` | Unsafe terminal output, ambiguous exits, leaked data, or missing process-fault evidence blocks the claim. | Failure, security, release | Assumed aligned | Awaiting human validation |

## Cross-initiative compatibility

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `CLI-A06` | D5 may declare an exact D2-D4 matrix but cannot prove those initiatives or D6 complete. | Handoffs, gates | Assumed aligned | Awaiting human validation |

## Validation record

| Review cycle | Reviewer | Date | Outcome | Notes |
|---|---|---|---|---|
| Initial assumption review | User | - | Assumed aligned; awaiting validation | All rows remain in initial review |

## Change discipline

Reconcile future dispositions across the full suite and tracking records.
