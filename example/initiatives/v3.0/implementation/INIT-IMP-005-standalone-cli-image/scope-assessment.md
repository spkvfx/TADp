# Standalone CLI image scope assessment

**Initiative:** `INIT-IMP-005`
**Status:** Proposed
**Last updated:** 2026-11-11

## Bounded outcome

One immutable one-shot CLI image provides the complete D5 interaction and
process contract through the public D4 wheel.

## Cohesion assessment

Commands, parser, rendering, exit codes, signals, help/completion, packaging,
and compatibility share one executable artifact and D5 gate.

## Split-trigger review

| Trigger | Current finding | Follow-up |
|---|---|---|
| Independent user outcome | Not established | Keep `CLI-06` open |
| Independent lifecycle/owner | Not established | Review Stage 5/6 |
| Independent artifact/release | Not established | Preserve one image |
| Mandatory safety separation | Not established | Block/reassess on evidence |

## Placement

`implementation` is correct for future source, image, metadata, assets, and
verification. `CLI-01` keeps destinations open.

## Explicit exclusions

D2-D4/D6 delivery, direct HTTP/SQLite, internal SDK imports, daemon behavior,
mounts/ports/socket, production/regulated use, ePHI, and downstream claims.

## Assessment result

Keep one narrow D5 initiative; create no umbrella or child.
