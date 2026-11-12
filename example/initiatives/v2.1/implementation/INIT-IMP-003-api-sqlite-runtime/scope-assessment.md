# API and SQLite runtime image scope assessment

**Initiative:** `INIT-IMP-003`
**Status:** Proposed
**Last updated:** 2026-11-11

## Bounded outcome

One immutable D3 image implements the authoritative record-domain, API,
search/navigation, SQLite, health, maintenance, recovery, and static-hosting
boundary.

## Cohesion assessment

These concerns share one runtime artifact, persistence boundary, compatibility
surface, failure envelope, and D3 conformance gate. Splitting them now would
fragment one observable product outcome.

## Split-trigger review

| Trigger | Current finding | Follow-up |
|---|---|---|
| Independent user outcome | Not established | Keep `API-06` open |
| Independent lifecycle or owner | Not established | Review at Stage 5/6 |
| Independent artifact or release | Not established | Preserve one D3 family |
| Mandatory safety separation | Not established | Block and reassess if evidence changes |

## Placement

Type `implementation` is appropriate because eventual work creates product
source, an image, migrations, tooling, and verification. Exact destinations
remain open under `API-01`.

## Explicit exclusions

D2 platform qualification, D4 SDK, D5 CLI, D6 web bundle, remote production
operation, regulated use, real/possible ePHI, and downstream completion claims.

## Assessment result

Keep one narrow initiative. No parent, subinitiative, sibling, or umbrella is
created; `API-06` owns any later evidence-based split decision.
