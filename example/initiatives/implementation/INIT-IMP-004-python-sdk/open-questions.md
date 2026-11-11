# Python SDK artifact open questions and decisions

**Initiative:** `INIT-IMP-004`
**Status:** Proposed
**Last updated:** 2026-11-11

## Status vocabulary

`Open` means no human choice exists. Only explicit authority and required
receipts may change state.

## Decision register

| ID | Decision | State | Earliest blocker | Owner |
|---|---|---|---|---|
| `SDK-01` | Exact SDK and evidence destinations | Open | Product placement | User |
| `SDK-02` | Dependency and Python/platform matrix | Open | Reproducible build | User |
| `SDK-03` | Typing/docs/compatibility tools | Open | Verification design | User |
| `SDK-04` | Private fault and transport seams | Open | Negative-path evidence | User |
| `SDK-05` | Security, release, and compatibility owner | Open | Readiness/release | User |
| `SDK-06` | Documentation or adapter split trigger | Open | Scope confirmation | User |

## Earliest blocking decisions

`SDK-06` blocks final scope; `SDK-01` blocks placement; `SDK-02`-`SDK-05`
block implementation-readiness and qualification planning.

## SDK-01 - Artifact placement

### Question

Which exact paths hold SDK source, wheel, metadata, docs, examples, and evidence?

### Why it matters

One traceable destination map prevents overlap and unsupported artifact claims.

### Options and tradeoffs

A consolidated package subtree improves cohesion; separated docs/evidence
locations may aid publishing but require stronger identity links.

### Default if unanswered

No destination or product record is inferred.

### Decision needed from

User.

## SDK-02 - Supported matrix

### Question

Which dependency patches and Python/platform images form the first matrix?

### Why it matters

Reproducibility and compatibility depend on exact locked inputs.

### Options and tradeoffs

A narrow matrix lowers evidence cost; broader support expands test obligations.

### Default if unanswered

No wheel build or compatibility claim.

### Decision needed from

User.

## SDK-03 - Verification tools

### Question

Which typing, documentation, and public-compatibility-diff tools run inside D2?

### Why it matters

Public-surface evidence must be reproducible without host-only prerequisites.

### Options and tradeoffs

One integrated toolchain is simpler; specialized tools may find more drift but
increase lock and maintenance scope.

### Default if unanswered

No public-surface readiness claim.

### Decision needed from

User.

## SDK-04 - Private test seams

### Question

How are fault, clock, randomness, and transport injection provided without
expanding the public API or weakening URL validation?

### Why it matters

Negative-path evidence needs control while the supported surface stays narrow.

### Options and tradeoffs

Private injection is precise; process/network harnesses preserve encapsulation
but are slower.

### Default if unanswered

Affected negative-path gates remain blocked.

### Decision needed from

User.

## SDK-05 - Review ownership

### Question

Who owns security/risk review, vulnerability monitoring, release disposition,
and D3 compatibility retirement?

### Why it matters

These continuing duties need accountable human authority.

### Options and tradeoffs

One owner simplifies decisions; specialist reviewers improve depth with more
handoffs.

### Default if unanswered

Readiness and release remain blocked.

### Decision needed from

User.

## SDK-06 - Split boundary

### Question

Does independently releasable documentation or an adapter require its own
initiative?

### Why it matters

A real independent lifecycle requires a split; convenience does not.

### Options and tradeoffs

Keep one wheel-centered D4 initiative unless evidence proves an independent
owner, artifact, lifecycle, or safety boundary.

### Default if unanswered

Retain one Proposed D4 initiative and do not start delivery.

### Decision needed from

User.

## Decision dependencies

Scope precedes placement; placement/matrix precede build; tools/seams/ownership
precede qualification and release planning.

## Decision process

Record human choices, rationale, alternatives, affected records, and receipts;
reconcile the complete suite and tracking records together.
