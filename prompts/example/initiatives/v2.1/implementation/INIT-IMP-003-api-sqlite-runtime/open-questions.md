# API and SQLite runtime image open questions and decisions

**Initiative:** `INIT-IMP-003`
**Status:** Proposed
**Last updated:** 2026-11-11

## Status vocabulary

`Open` means no human decision exists. A decision may change state only through
explicit human authority and a receipt when protocol rules require one.

## Decision register

| ID | Decision | State | Earliest blocker | Owner |
|---|---|---|---|---|
| `API-01` | Exact artifact and evidence destinations | Open | Product placement and delivery planning | User |
| `API-02` | Dependency, base-image, SQLite, and RE2 identities | Open | Reproducible build and matrix | User |
| `API-03` | Test and fault-injection seams | Open | Verification design | User |
| `API-04` | Contract fixtures and OpenAPI drift evidence | Open | Contract-evidence design | User |
| `API-05` | D3 security and operational review owner | Open | Readiness and release gates | User |
| `API-06` | Mandatory D3 split trigger | Open | Final scope confirmation | User |

## Earliest blocking decisions

`API-06` blocks final scope confirmation. `API-01` blocks product placement.
`API-02` through `API-05` block implementation-readiness and evidence planning.

## API-01 - Artifact placement

### Question

Which exact repository and product paths hold API/domain/query/persistence
source, migrations, maintenance commands, static-hosting code, image metadata,
and evidence?

### Why it matters

Traceability and ownership require one non-overlapping destination map.

### Options and tradeoffs

A consolidated D3 subtree improves cohesion; separated technical subtrees may
match build tooling but increase mapping and ownership complexity.

### Default if unanswered

No destination is inferred and delivery remains blocked.

### Decision needed from

User.

## API-02 - Supported dependency matrix

### Question

Which dependency patches, base digest, SQLite build, RE2 wheel, and Python image
identities form the first compatible D2/D3 matrix?

### Why it matters

Unpinned or incompatible inputs invalidate reproducibility and qualification.

### Options and tradeoffs

A narrow matrix reduces evidence cost; a broader matrix expands support and
testing obligations.

### Default if unanswered

No build or compatibility claim.

### Decision needed from

User.

## API-03 - Test seams

### Question

How are clocks, UUIDs, faults, deadlines, cancellation, and network loss
injected without weakening production defaults?

### Why it matters

Deterministic negative-path evidence requires controlled seams.

### Options and tradeoffs

Private dependency injection is precise; process-level fault harnesses preserve
encapsulation but can be slower and less granular.

### Default if unanswered

No readiness claim for affected vectors.

### Decision needed from

User.

## API-04 - Contract and drift evidence

### Question

Where and how are contract fixtures and OpenAPI drift evidence generated,
stored, and reviewed without making generated output authoritative?

### Why it matters

Consumers need stable evidence while source authority remains clear.

### Options and tradeoffs

Committed fixtures aid review; generated CI artifacts reduce repository churn
but require durable retention and identity.

### Default if unanswered

No contract-drift gate is claimed.

### Decision needed from

User.

## API-05 - Review ownership

### Question

Who owns D3 risk analysis, security evidence, activity review,
incident/recovery drills, and source-currency checks?

### Why it matters

Required review work needs accountable human authority.

### Options and tradeoffs

One owner simplifies accountability; named specialist reviewers improve depth
but require explicit handoffs.

### Default if unanswered

Readiness, release, and completion remain blocked.

### Decision needed from

User.

## API-06 - D3 split boundary

### Question

Does any sub-scope require an independently governed initiative while
preserving one D3 artifact and completion boundary?

### Why it matters

Mandatory split triggers override convenience, but arbitrary splitting would
fragment one outcome.

### Options and tradeoffs

Keep one initiative unless evidence establishes an independent lifecycle,
owner, artifact, or safety boundary; split only the proven independent scope.

### Default if unanswered

Retain one Proposed D3 initiative and do not begin delivery.

### Decision needed from

User.

## Decision dependencies

Scope confirmation precedes placement; placement and matrix precede build
planning; seams, drift evidence, and ownership precede qualification planning.

## Decision process

Record explicit human choices, rationale, alternatives, affected records, and
receipts where required. Reconcile README, assumptions, architecture, mapping,
roadmap, steps, index, and status together.
