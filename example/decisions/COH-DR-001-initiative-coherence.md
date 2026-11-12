# Initiative coherence and completion feedback decision

**Receipt ID:** COH-DR-001

**Source decision ID:** COH-001

**Affected initiative:** Not applicable; direct protocol maintenance and example adoption

**Responder:** User

**Human authority:** Sole project owner; explicit authority for this protocol rule and its protocol, example, and reusable-template consumers

**Response date:** 2026-11-12

**Disposition:** Authorized specific invariant addition and necessary consumer changes

## Exact initiating question

> as initiatives complete they must be able to further refine open initiatives, but must not refine closed initiatives without reopening them. Does the protocol support this behavior?

## Evidence presented

The review identified existing alignment, acceptance, reopening, and successor
mechanisms, but no explicit completion feedback review, no blanket closed-claim
edit restriction, and no Git comparison enforcing that restriction. It also
identified the existing human decision gates and specification 09 requirement
for a new tuple when substantive meaning changes.

## Exact human response

> I think I want this rule in place. Open initiative effort should be considered work. If efforts conflicts with work that needs to be documented. Coherancy is teh entire point of TADp

## Exact scope follow-up

> will this applied to both the protocol, the example and each template suite?

## Resulting disposition and boundary

Authorize the specific coherence rule: open initiative effort is work that
must be considered alongside planned, partial, and delivered work; conflicting
effort must be documented; completion findings can refine open initiatives
through their governed workflows; closed claims require explicit human
reopening before refinement. Apply the rule to the protocol, the installed
example, and every reusable initiative type through common templates and
type-specific prompts.

This authorizes the necessary invariant, reusable-template, prompt, validator,
regression-test, documentation, adoption, and protected-lock changes for this
rule. It does not resolve any example open question, accept an initiative,
authorize unrelated product work, weaken the successor requirement, or reopen
an existing terminal initiative.

## Identity, preservation, and compatibility

- **Maintenance branch:** `protocol/initiative-coherence-feedback`
- **Captured base branch:** `v1`
- **Captured pre-revision Git baseline:** `7b9d302b3dc7a94627518e42819a3130b5ba17d3`
- **New governed tuple:** None; this is a direct, specifically authorized
  protocol-maintenance operation, not a fabricated initiative acceptance.
- **Preserved predecessor:** The captured baseline and its Git history retain
  the earlier invariants, templates, tools, and historical claims.
- **Effective event:** Adoption of the coherent specification 10 change and
  its reconciled consumers. The profile's coherence baseline names the
  pre-adoption snapshot; it is not represented as the future delivery commit.
- **Migration:** Existing closed claims need no invented retrospective
  completion reviews. New work and later refinements are governed. Existing
  open initiatives retain their identity, unresolved decisions, and recorded
  compatibility; substantive successors still follow specification 09.

## Reconciled records

- [Specification 10](../evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md),
  suite index, governance, lifecycle, decision-receipt and workflow consumers.
- Project profiles, work-conflict registers, reusable initiative and project
  sources, numbered workflow consumers, validator and regression tests.
- Developer guidance and the [migration guide](../docs/guides/initiative-coherence-migration.md).
- Corresponding protocol sources installed in `example/`, preserving its
  project-specific authoritative conflict history and Git-root exception.
- Protected locks refreshed only for these authorized changes after review.

This receipt is mirrored into the installed example for local traceability of
the same decision, not as a second human decision or independent acceptance.
The canonical maintenance receipt is `protocol/decisions/COH-DR-001-initiative-coherence.md`.

## Verification and remaining limits

Verification is recorded in the linked maintenance verification record after
the checks run. Structural validation cannot decide whether every semantic
conflict was found or whether claimed human authority is authentic.

**Verification record:** [Maintenance verification](COH-VER-001-initiative-coherence.md)

**Recording commit:** Pending; recorded in Git when the coherent change is committed
