# Web application bundle assumption

**Initiative:** Web application bundle
**Status:** Proposed
**Last updated:** 2026-11-11
**Assumption review:** Assumed aligned; awaiting validation

Every row remains unconfirmed until explicit human review.

## Review method

Only explicit human instruction changes `Assumed aligned`. Questions live in
[open-questions.md](open-questions.md).

## Boundary between assumption and open questions

| Assumption | Implementation question that may remain open |
|---|---|
| One embedded D6 bundle owns web outcome | Paths, framework, version, matrix, maps, owner, split |
| Required accessibility/security states bind | Exact tools and evidence mechanisms |

## Product and scope

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `WEB-A01` | One same-origin bundle has one D6 owner, lifecycle, and completion claim. | Scope, product, roadmap | Assumed aligned | Awaiting human validation |

## Domain and authority

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `WEB-A02` | Web/API contracts own interaction/state semantics; client convenience cannot invent server truth. | Architecture, mapping, tests | Assumed aligned | Awaiting human validation |

## System boundaries and dependencies

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `WEB-A03` | D6 builds through D2, is served same-origin by compatible D3, and has no separate server/cross-origin/remote assets. | Interfaces, build, security | Assumed aligned | Awaiting human validation |

## Data and lifecycle

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `WEB-A04` | Record data stays in session memory; no durable browser record store; evidence is synthetic/de-identified. | State, storage, fixtures | Assumed aligned | Awaiting human validation |

## Operations security and failure behavior

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `WEB-A05` | Accessibility, unsafe DOM/assets/maps, race, conflict, indeterminate, or leak gaps block affected claims. | Interaction, security, release | Assumed aligned | Awaiting human validation |

## Cross-initiative compatibility

| ID | Assumption currently treated as aligned | Affected records if the assumption changes | Disposition | Correction or note |
|---|---|---|---|---|
| `WEB-A06` | D6 may declare exact D2/D3 compatibility but cannot prove them or D5 complete. | Handoffs, matrices, gates | Assumed aligned | Awaiting human validation |

## Validation record

| Review cycle | Reviewer | Date | Outcome | Notes |
|---|---|---|---|---|
| Initial assumption review | User | - | Assumed aligned; awaiting validation | Every row remains in initial review |

## Change discipline

Reconcile future dispositions across the full suite and tracking records.
