# Web application bundle scope assessment

**Initiative:** `INIT-IMP-006`
**Status:** Proposed
**Last updated:** 2026-11-11

## Bounded outcome

One immutable same-origin bundle implements the D6 browser interaction,
accessibility, security, and compatibility contract.

## Cohesion assessment

Views, state, workflows, accessibility, help, asset build, security, and
browser qualification share one bundle, release identity, and D6 gate.

## Split-trigger review

| Trigger | Current finding | Follow-up |
|---|---|---|
| Independent user outcome | Not established | Keep `WEB-07` open |
| Independent lifecycle/owner | Not established | Review Stage 5/6 |
| Independent artifact/release | Not established | Preserve one bundle |
| Mandatory safety separation | Not established | Block/reassess on evidence |

## Placement

`implementation` is correct for future source, compiled assets, manifest,
reports/traces, and evidence. `WEB-01` keeps destinations open.

## Explicit exclusions

Separate web server, host Node, durable record storage, remote assets,
cross-origin API, D2/D3/D5 delivery, production/regulated use, ePHI, and
downstream claims.

## Assessment result

Keep one narrow D6 initiative; create no umbrella or child.
