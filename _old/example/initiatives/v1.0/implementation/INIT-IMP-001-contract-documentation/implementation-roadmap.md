# Contract documentation delivery roadmap

**Initiative:** Contract documentation  
**Status:** Proposed  
**Last updated:** 2026-11-11  
**Initiative type:** `implementation`

Related documents: [initiative](README.md), [assumptions](assumption.md),
[architecture](architecture.md), [mapping](source-mapping.md), [decisions](open-questions.md),
and [steps](implementation-steps.md).

## Objective

Deliver one accepted, versioned derivative documentation product whose exact
source identity, scope, limitations, safe examples, and review evidence make
the example-record contracts usable without claiming any executable outcome.

## Delivery scope

### Included

- Destination-selected derivative guides, navigation, source mapping,
  examples, version metadata, and limitations.
- Documentation-specific structural, semantic, data/claim, and selected
  accessibility/usability qualification.

### Excluded from this roadmap

- Authoritative specification changes and every D2–D6 product.
- Acceptance, implementation, completion, release, or regulated-use claims
  without their separately required authority and evidence.

## Type-specific delivery boundary

This `implementation` initiative may change only its accepted documentation
product and product documentation. A required source/specification change
stops the affected work and routes to an owning design/authority workflow.

## Prerequisites

| Prerequisite | Required state | Evidence |
|---|---|---|
| Initiative lifecycle | Explicitly Accepted after assumption/decision review | Future lifecycle receipt and README history |
| Product placement and scope | `DOC-01`–`DOC-03` accepted; no mandatory split | Decision receipts and scope assessment |
| Source baseline | Exact architecture/security revisions captured and current | Source map and currency review |
| Data/use plan | Synthetic provenance and prohibited-claim handling approved | Fixture/data manifest and policy mapping |

## Phase summary

| Phase | Outcome | Depends on | Parallel work allowed |
|---|---|---|---|
| 0 | Accepted specifications and documentation output boundary | None | No product work |
| 1 | Exact destination, source manifest, information architecture, and review design | Phase 0 | Source inventory may proceed in parallel with tooling evaluation |
| 2 | Authored/generated derivative content and safe examples | Phase 1 | Independent pages only within the accepted one-product claim |
| 3 | Outcome qualification and publication evidence | Phase 2 | Checks may run in parallel against the same immutable revision |

## Phase 0 - Accept the specifications and output boundary

### Objective

Reconcile assumptions, evidence, split triggers, and blocking decisions before
creating the product.

### Work

- Resolve every `Open, blocking` decision and review every assumption.
- Confirm source ownership, product destination, audience cohesion, versioning,
  data/use, compatibility, and rollback boundaries.
- Map each authoritative requirement to a product destination and check.
- Verify the canonical tuple and pre-effective migration remain reciprocal.

### Exit gate

- [ ] Assumption review is explicitly complete.
- [ ] Every blocking decision has a receipt and coupled reconciliation.
- [ ] No split trigger is present or each split has its own Stage 0 tuple.
- [ ] The initiative is explicitly Accepted; no specification change is hidden.

## Phase 1 - Establish the documentation product frame

### Objective

Create the accepted destination, source manifest, navigation model, content
classes, version identity, fixture rules, and verification configuration.

### Work

- Create only the paths selected by `DOC-01` and enumerate audience entry points.
- Record exact authoritative revisions and claim/source mappings.
- Define authored/generated boundaries, synthetic fixture provenance, link
  roots, accessibility/usability method, and review ownership.

### Exit gate

- [ ] Product structure and source manifest match accepted decisions.
- [ ] Every planned claim has an authority and every example has safe provenance.
- [ ] Drift, overclaim, missing-source, and rollback behavior are testable.

## Phase 2 - Author derivative content

### Objective

Produce the accepted guides, source links, examples, limitations, and optional
generated appendices without changing source meaning.

### Work

- Author orientation and accepted audience guides in dependency order.
- Generate only accepted, hash-bound observed derivatives.
- Apply consistent profile limitations and prospective/result vocabulary.

### Exit gate

- [ ] Accepted content coverage and navigation are complete.
- [ ] Generated content matches exact input and remains visibly derivative.
- [ ] No unsafe data, broken source, unsupported claim, or D2–D6 completion claim remains.

## Phase 3 - Outcome qualification

### Objective

Qualify the exact documentation revision and capture evidence for the bounded
D1 completion claim.

### Work

- Run structure/link, coverage, semantic drift, example, security/claim, and
  selected accessibility/usability checks.
- Exercise missing source, generated mismatch, unsafe fixture, interrupted
  publication, and rollback behavior.
- Record exact revision, environment, method, results, limitations, and reviewer.

### Exit gate

- [ ] Every accepted documentation outcome passes in the supported destination.
- [ ] No unresolved blocking decision, split, source conflict, or unowned risk remains.
- [ ] Rollback and revision traceability have evidence.
- [ ] Completion evidence and lifecycle/status records truthfully match the result.

## Rollout controls

| Control | Initial state | Enablement condition | Rollback or disable behavior |
|---|---|---|---|
| Public/product entry point | Disabled/not created | Exact revision passes the complete D1 product gate | Restore last reviewed revision or withdraw candidate links |
| Generated appendices | Disabled | `DOC-03` accepted and exact artifact/drift evidence exists | Remove invalid derivative; never change authority |
| Observed product statements | Prohibited | Exact later product evidence and compatible source identity exist | Revert to prospective wording and preserve invalid finding |

## Release definition

The initiative can complete only after every phase gate passes, every
authoritative requirement has exact documentation evidence, open choices are
resolved, deferred work is explicit, and completion/status records point to
the durable reviewed product. This definition authorizes no current release.
