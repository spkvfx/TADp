# Python SDK artifact delivery roadmap

**Initiative:** `INIT-IMP-004`
**Status:** Proposed planning only
**Last updated:** 2026-11-11

## Objective

Sequence a future D4 wheel delivery without implying authorization or release.

## Delivery scope

### Included

One public SDK contract, private transport, immutable wheel, docs/examples,
compatibility declarations, and D4 evidence.

### Excluded from this roadmap

D2/D3 delivery, D5 CLI, D6 web, direct SQLite, production/regulated operation,
ePHI, and unresolved destinations/tools.

## Type-specific delivery boundary

Delivery starts only after lifecycle authority, blocking decisions, and a
product record identify the output boundary.

## Prerequisites

Assumptions reviewed; `SDK-01`-`SDK-06` addressed; D2 target and compatible D3
identified; source currency/security/data-use gates reviewed.

## Phase summary

| Phase | Outcome | Entry gate | Exit evidence |
|---|---|---|---|
| 0 | Specification and placement authorized | Human review | Decisions and product map |
| 1 | Public SDK core | Phase 0 | Model/method/exception evidence |
| 2 | Package and compatibility | Phase 1 | Reproducible wheel and mock/live matrix |
| 3 | D4 qualification | Phase 2 | Complete artifact-bound evidence |

## Phase 0 - Authorize specification and output boundary

### Objective

Resolve scope, destinations, matrix, tools, seams, ownership, and evidence plan.

### Work

Review contracts, security/data use, D2/D3 interfaces, public compatibility,
and retention; create required decisions/products.

### Exit gate

Explicit authority exists and no required D4 choice is silently open.

## Phase 1 - Implement public SDK core

### Objective

Build strict models, methods, exceptions, validation, and private transport.

### Work

Implement read/write surfaces, query/navigation, URL policy, timeouts,
cancellation, cleanup, problem mapping, and read-only retry.

### Exit gate

SDK behavior and applicable contract vectors pass against mock fixtures.

## Phase 2 - Package and prove compatibility

### Objective

Produce reproducible wheel/docs/typing and verify a compatible live D3.

### Work

Lock/build/inspect/scan the wheel, run public diffs, docs checks, mock/live
matrices, and safe fault tests.

### Exit gate

Artifact identity, public surface, security, and compatibility evidence pass.

## Phase 3 - Qualify D4 outcome

### Objective

Assemble a D4-only conformance and review packet.

### Work

Complete matrix, source-currency, risk, vulnerability, retirement, and evidence
reviews without depending on D5 completion.

### Exit gate

A human can evaluate D4 alone from artifact-specific evidence.

## Rollout controls

Immutable wheel identity, narrow matrices, public-surface diff, safe fallback,
compatibility retirement, and explicit security/evidence stop conditions.

## Release definition

One immutable wheel plus locked inputs, metadata, docs, compatibility
declaration, security records, and complete D4 evidence. This roadmap creates
no release claim.
