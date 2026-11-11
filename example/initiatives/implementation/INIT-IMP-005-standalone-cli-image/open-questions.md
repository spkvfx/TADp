# Standalone CLI image open questions and decisions

**Initiative:** `INIT-IMP-005`
**Status:** Proposed
**Last updated:** 2026-11-11

## Status vocabulary

`Open` means no human choice exists. Only explicit authority and required
receipts may change state.

## Decision register

| ID | Decision | State | Earliest blocker | Owner |
|---|---|---|---|---|
| `CLI-01` | Exact CLI/image/evidence paths | Open | Product placement | User |
| `CLI-02` | Parser/formatter and patch locks | Open | Reproducible build | User |
| `CLI-03` | CLI semantic/compatibility policy | Open | Public surface | User |
| `CLI-04` | Process fault-injection design | Open | Negative-path evidence | User |
| `CLI-05` | Risk/security/release/evidence owner | Open | Readiness/release | User |
| `CLI-06` | Completion/automation split trigger | Open | Scope confirmation | User |

## Earliest blocking decisions

`CLI-06` blocks scope; `CLI-01` placement; `CLI-02`-`CLI-05` readiness.

## CLI-01 - Artifact placement

### Question

Which exact paths hold source, help/completion, image definition, release
metadata, and evidence?

### Why it matters

Artifact identity, ownership, and traceability require an explicit map.

### Options and tradeoffs

A consolidated CLI subtree aids cohesion; separated generated assets require
stronger lineage.

### Default if unanswered

No destination is inferred.

### Decision needed from

User.

## CLI-02 - Parser and formatting stack

### Question

Which parser/formatting libraries and patch locks are used?

### Why it matters

Interaction, output safety, licensing, and reproducibility depend on them.

### Options and tradeoffs

Standard-library choices reduce dependencies; libraries may improve UX but
expand supply-chain/evidence scope.

### Default if unanswered

No build begins.

### Decision needed from

User.

## CLI-03 - Semantic compatibility

### Question

What CLI semantic version and compatibility policy applies apart from v3.0?

### Why it matters

Commands, help, JSON, output, and exits are public automation surfaces.

### Options and tradeoffs

Strict compatibility protects automation; faster breaking evolution requires
explicit major-version and migration handling.

### Default if unanswered

No compatibility or release claim.

### Decision needed from

User.

## CLI-04 - Process fault injection

### Question

How are pre/post-dispatch, interrupt, broken-pipe, and Compose pre-entrypoint
faults injected deterministically?

### Why it matters

Ambiguous write and process outcomes need executable evidence.

### Options and tradeoffs

Subprocess harnesses are realistic; private hooks are precise but can couple
tests to implementation.

### Default if unanswered

Affected process gates remain blocked.

### Decision needed from

User.

## CLI-05 - Review ownership

### Question

Who owns risk, vulnerability, license, safe-output, incident, and evidence
retention review?

### Why it matters

Continuing safety/release duties need human accountability.

### Options and tradeoffs

One owner simplifies disposition; specialists add depth with handoffs.

### Default if unanswered

Readiness and release remain blocked.

### Decision needed from

User.

## CLI-06 - Split boundary

### Question

Does generated completion or automation integration require an independent
initiative?

### Why it matters

Independent lifecycle/artifact evidence requires a split; convenience does not.

### Options and tradeoffs

Keep one image-centered D5 initiative unless an independent owner, artifact,
lifecycle, or safety boundary is proven.

### Default if unanswered

Retain one Proposed D5 initiative and do not deliver.

### Decision needed from

User.

## Decision dependencies

Scope precedes placement; placement/stack/policy precede build; fault design
and ownership precede qualification.

## Decision process

Record explicit choices, rationale, alternatives, affected records, and
receipts; reconcile all coupled files together.
