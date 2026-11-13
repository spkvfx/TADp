# Python SDK artifact scope assessment

**Initiative:** `INIT-IMP-004`
**Status:** Proposed
**Last updated:** 2026-11-11

## Bounded outcome

One immutable Python wheel implements the D4 public client contract with
artifact-specific compatibility and verification.

## Cohesion assessment

Models, methods, exceptions, transport policy, typing, packaging, and docs
share one public surface, release identity, compatibility policy, and D4 gate.

## Split-trigger review

| Trigger | Current finding | Follow-up |
|---|---|---|
| Independent user outcome | Not established | Keep `SDK-06` open |
| Independent lifecycle or owner | Not established | Review at Stage 5/6 |
| Independent artifact/release | Not established | Preserve one wheel |
| Mandatory safety separation | Not established | Block and reassess if evidence changes |

## Placement

`implementation` is correct because later work creates source, a wheel, docs,
metadata, and verification. `SDK-01` keeps destinations open.

## Explicit exclusions

D2/D3 delivery, D5 CLI, D6 web, direct SQLite, server behavior, host runtime,
production/regulated use, ePHI, and downstream completion.

## Assessment result

Keep one narrow D4 initiative. No umbrella or subinitiative is created.
