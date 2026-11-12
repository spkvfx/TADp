# Web application bundle delivery roadmap

**Initiative:** `INIT-IMP-006`
**Status:** Proposed planning only
**Last updated:** 2026-11-11

## Objective

Sequence a future D6 delivery without implying accessibility, security, release,
or completion.

## Delivery scope

### Included

One web source/state surface, immutable same-origin bundle, help,
browser/accessibility/API compatibility, and D6 evidence.

### Excluded from this roadmap

D2/D3/D5 delivery, separate server, host Node, durable record storage, remote
assets, cross-origin API, production/regulated use, ePHI, unresolved choices.

## Type-specific delivery boundary

Delivery begins only after lifecycle authority, decisions, and product mapping.

## Prerequisites

Assumptions reviewed; `WEB-01`-`WEB-07` addressed; exact D2/D3 artifacts and
security/data/accessibility gates reviewed.

## Phase summary

| Phase | Outcome | Entry gate | Exit evidence |
|---|---|---|---|
| 0 | Specification/placement authorized | Human review | Decisions/product map |
| 1 | Accessible workflow/state core | Phase 0 | Component/state evidence |
| 2 | Bundle/integration qualification | Phase 1 | Browser/AT/security/API matrix |
| 3 | D6 qualification | Phase 2 | Artifact-bound D6 record |

## Phase 0 - Authorize specification and output boundary

### Objective

Resolve scope, paths, framework, policy, matrix, maps, owner, evidence plan.

### Work

Review web/API/security/data/accessibility contracts and create product/decision
records with exact D2/D3 inputs.

### Exit gate

Explicit authority exists and required D6 choices are addressed.

## Phase 1 - Implement accessible workflows and state

### Objective

Build record/search/navigation/edit/delete/help with complete accessible states.

### Work

Implement validation, pending/race/cancel/retry/stale/conflict/indeterminate
models plus keyboard/focus/semantic/status/contrast behavior.

### Exit gate

Component/state/accessibility contract evidence passes.

## Phase 2 - Build and prove integration

### Objective

Build immutable embedded assets and verify same-origin/browser/security matrix.

### Work

Lock/build/inspect/scan; embed in D3; test CSP, storage, maps, network faults,
browser/OS/AT/high-contrast/zoom/Safari, and API compatibility.

### Exit gate

Artifact, accessibility, security, and integration evidence passes.

## Phase 3 - Qualify D6 outcome

### Objective

Assemble a D6-only review packet.

### Work

Complete source, risk, vulnerability/license, accessibility, compatibility,
evidence, and clean-install reviews.

### Exit gate

A human can evaluate D6 without inferring D2/D3/D5 completion.

## Rollout controls

Immutable manifest/assets, narrow matrices, accessible surface diff, cache-safe
fallback, indeterminate-write controls, and accessibility/security stop gates.

## Release definition

One immutable bundle plus manifest, locked inputs, compatibility, accessibility
and security records, source-map disposition, and D6 evidence. No release here.
