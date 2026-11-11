# VRC-DR-001 decision receipt

**Receipt ID:** VRC-DR-001

**Initiative:** [INIT-DSN-001-version-realization-correlation](../README.md)

**Source ID or lifecycle event:** INIT-DSN-001 Proposed-to-Superseded lifecycle event

**Human authority:** User, Sole Project Owner, exercising explicit supersession authority

**Response date or event:** 2026-11-11

**Capture context:** Current Codex repository task executing the named repository prompt

**Disposition:** Superseded

**Git commit:** Pending

## Exact prompt or question

No earlier Codex question initiated this decision. The User supplied this exact
execution instruction:

```text
begin or resume work outlined by this prompt.[@version-realization-initiative-correlation-protocol-change.md](file:///C:/Users/User/PycharmProjects/TADp/prompts/version-realization-initiative-correlation-protocol-change.md)[@version-realization-initiative-correlation-protocol-change.md](file:///C:/Users/User/PycharmProjects/TADp/prompts/version-realization-initiative-correlation-protocol-change.md)
```

## Evidence and limitations presented

- **Authoritative evidence:**
  [Codex initiative lifecycle specification](../../../../evidence/authoritative/LLM/04_Codex_Initiative_Lifecycle_Specification.md)
  permits `Proposed` to `Superseded` when human supersession authority, a named
  replacement, compatibility or migration effects, and retained history are
  recorded; the
  [human decision receipt specification](../../../../evidence/authoritative/LLM/07_Codex_Human_Decision_Receipt_Specification.md)
  requires this receipt before source or lifecycle reconciliation.
- **Other evidence:** The
  [repository prompt](../../../../../prompts/version-realization-initiative-correlation-protocol-change.md)
  is the User-authored direct-maintenance instruction and named replacement.
  The prior [initiative README](../README.md),
  [proposal source inventory](../proposal/README.md),
  [canonical project index](../../../initiative-index.md), and
  [status view](../../../status.md) record the initiative's prior `Proposed`
  state. These records establish historical state but do not provide the
  supersession authority.
- **Material limitations:** VRC-01 and VRC-02 remain unresolved historical
  project-specific questions. The User expressly excluded them from governing
  this revision and excluded their project-specific evidence from protocol
  design and validation input. This decision does not establish acceptance,
  implementation, completion, release, or migration for INIT-DSN-001 or for
  the replacement protocol work.
- **Affected scope described to the human:** Supersede only
  INIT-DSN-001-version-realization-correlation and reconcile its initiative
  lifecycle, source disposition, canonical project index row, status row,
  realization-suite navigation, and decision-receipt index while preserving
  every prior record and source identity.

## Exact human response

The named repository prompt contains this exact response:

```text
I explicitly authorize this prompt to supersede the execution plan recorded in
`protocol/initiatives/design/INIT-DSN-001-version-realization-correlation/`.
This repository prompt is the named replacement that owns the exact direct
protocol-maintenance work defined here.

Before changing the initiative's source disposition or lifecycle, create a
human-decision receipt that preserves this instruction and records:

- its prior `Proposed` state;
- this prompt as the named replacement;
- the reason for supersession: the prior plan's type split and
  project-specific migration analysis no longer govern this direct
  repository-prompt execution;
- preservation of all prior records, source identity, and unresolved
  project-specific questions; and
- every initiative index, status, and lifecycle record reconciled by the
  transition.

Record the legal `Proposed` to `Superseded` transition. Do not record
acceptance, implementation, completion, release, or migration for that
initiative. Retain VRC-01 and VRC-02 as historical unresolved questions that
do not govern this revision, and do not use their project-specific evidence as
protocol design or validation input.
```

## Resulting scope and rationale

INIT-DSN-001 transitions legally from `Proposed` to `Superseded`. The named
replacement is the repository prompt, which directly owns the authorized
protocol-maintenance outcome. The prior initiative's type split and
project-specific migration analysis no longer govern that work. All prior
initiative, proposal, realization, question, and Git records remain historical
evidence under their original identities; none is reclassified as accepted,
implemented, completed, released, or migrated.

## Reconciled records

| Record | Change required by this decision | Verification |
|---|---|---|
| [Decision-receipt index](README.md) | Register VRC-DR-001 before changing the source disposition or lifecycle | Receipt-link and diff review |
| [Initiative README](../README.md) | Record the named replacement, preserve the prior claim, and append the `Proposed` to `Superseded` lifecycle transition | Lifecycle-table and link review |
| [Proposal source inventory](../proposal/README.md) | Mark the proposal as retained historical source and identify the replacement prompt without rewriting prior proposal content | Source-identity review |
| [Open questions](../open-questions.md) | Retain VRC-01 and VRC-02 as unresolved historical questions that do not govern the replacement | Stable-ID and status review |
| [Canonical project index](../../../initiative-index.md) | Reconcile the INIT-DSN-001 row to `Superseded`, link this receipt and replacement, and remove any active next gate | Row and reciprocal-link review |
| [Project status](../../../status.md) | Reconcile the copied lifecycle status and portfolio gates without creating an acceptance, delivery, or completion claim | Status-row review |
| [Realization-suite index](../../../../evidence/non-authoritative/realizations/v1.0/00-RZN-TADP-001-VERSION-CORRELATION-suite-index.md) | Preserve non-authoritative standing while updating the copied initiative lifecycle and replacement navigation | Standing and reciprocal-link review |

## Unresolved consequences and re-entry conditions

VRC-01 and VRC-02 remain unresolved historical questions and have no authority
over the replacement protocol revision. Reopening INIT-DSN-001 would require a
new explicit human reopening decision and reconciliation with this named
replacement. The replacement protocol work still requires its own coherent
authoritative specification, consumer updates, protected locks, example
synchronization, and verification before any effective-point or completion
claim can be made.
