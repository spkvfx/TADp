# Codex initiative governance specification

## Scope

This specification governs how Codex interprets realization notes and creates,
reviews, changes, executes, and reports initiatives.

## Realization notes

A realization note is a broad description of an opportunity, concern, desired
outcome, or possible initiative. It is proposal input, not an accepted
specification.

Codex may use a realization to identify intended outcomes, candidate scope,
dependencies, risks, and questions. It must preserve the realization's source
identity and must not treat its wording as an invariant, accepted decision,
confirmed assumption, authorized implementation, or completion evidence.

If a realization conflicts with an invariant, the invariant governs. Codex
must record the contradiction and must not carry the conflicting realization
claim into an initiative as a requirement.

## Initiatives as specifications

An initiative is the canonical structured specification for bounded work. It
defines what may be changed, why the work is authorized, which evidence and
decisions govern it, what outcome is required, and how completion will be
verified.

Codex must create and maintain initiatives using the repository's complete
initiative template. A valid initiative must be:

- internally coherent across its proposal, assumptions, architecture, source
  mapping, decisions, roadmap, steps, verification, and status;
- mutually coherent with every active or accepted initiative that shares a
  contract, product, dependency, or authority boundary;
- fully compatible with every applicable invariant;
- explicit about included scope, exclusions, ownership, interfaces, failure,
  security, compatibility, migration, recovery, and verification where they
  apply;
- traceable from source authority to each normative claim and planned output;
  and
- truthful about lifecycle standing, incomplete work, blockers, and deferred
  scope.

A proposed initiative may describe intended work but does not authorize
execution. An accepted initiative authorizes only its declared type, scope,
products or evidence, and accepted gates.

The authoritative workflow specification defines the stages that create,
align, accept, deliver, complete, and finalize an initiative. A workflow stage
does not create a lifecycle state merely by finishing.

## Narrow scope and subinitiatives

Every initiative must own one narrowly bounded outcome, one coherent authority
boundary, and one independently reviewable acceptance claim. Codex must not
create umbrella or multi-purpose initiative containers that combine independent
outcomes merely because they share a release, product area, team, dependency,
or schedule.

When proposed work contains independently acceptable outcomes, distinct
owners, materially different authority boundaries, or separable completion
gates, Codex must create separately scoped initiatives. Sibling initiatives
are preferred when no genuine parent specification exists.

Subinitiatives remain permitted when a parent initiative has a real bounded
specification and a dependent portion of that specification needs its own
narrow scope, decisions, execution, or verification. A subinitiative must:

- own one smaller outcome within the parent's accepted boundary;
- cite the exact parent requirement and applicable invariants;
- state what remains owned by the parent and by sibling work;
- have its own coherent records, decisions, gates, and verification; and
- never expand the parent, absorb unrelated work, or serve as a substitute for
  an independently scoped initiative.

A parent may coordinate dependencies and aggregate verified status, but it
must not use child records to conceal incompatible authority, ambiguous
ownership, partial completion, or unrelated acceptance claims.

## Assumptions and questions

Assumptions and open questions are human decision gates by default.

Codex may gather evidence, test consistency, identify implications, compare
invariant-compatible options, and make a clearly labelled recommendation. It
must not confirm, correct, reject, accept, defer, close, or otherwise resolve an
assumption or question without an explicit human response.

An explicit human instruction may authorize a different decision method for a
clearly bounded task. That authorization must be recorded with the resulting
disposition and rationale. It does not authorize an invariant conflict or
apply automatically to other initiatives, assumptions, or questions.

Every assumption or question must be handled individually. A blanket approval
is valid only when the human instruction clearly identifies the complete set
being approved and the evidence shows that the set is coherent.

## Initiative creation and alignment

When creating or aligning an initiative, Codex must:

1. Preserve the realization and proposal as source material.
2. Inventory applicable invariants, accepted decisions, released contracts,
   verified implementation, and dependent initiatives.
3. Classify each source by standing and preserve its limits.
4. Create one canonical owner for each requirement or contract.
5. Record unresolved assumptions, questions, conflicts, and missing evidence
   without deciding them autonomously.
6. Reconcile terminology, scope, IDs, ownership, dependencies, phases, and
   verification across the complete initiative suite.
7. Reject or route any requested outcome that cannot be made
   invariant-compatible.

Codex must not make documents appear coherent by silently narrowing claims,
rewriting history, changing another initiative, or treating proposed work as
implemented.

## Reopening and revising initiatives

An initiative may be reopened or revised, including after acceptance or
completion, but the change must be explicit and fully documented.

Before changing substantive initiative meaning, Codex must record:

- the human authority and instruction that reopened or revised the initiative;
- the prior lifecycle state and exact accepted or completed claim;
- the reason for change and the newly affected scope;
- every changed assumption, decision, invariant mapping, specification,
  dependency, product, test, migration, release, or operational claim;
- compatibility and recovery effects for previously delivered products;
- the verification required for the revised claim; and
- the effective date or event and the records that must be reconciled.

Codex must preserve the earlier state through history, an explicit supersession
relationship, or a durable change record. It must update every affected
initiative document and tracking record in the same coherent change. Reopening
does not erase prior evidence, retroactively falsify an earlier truthful claim,
or authorize unrelated scope.

If the requested revision conflicts with an invariant, Codex must use the
invariant-conflict procedure instead of revising the initiative into a
contradictory state.

## Execution and completion

Codex may execute work only when the initiative type permits that output and
all required human decisions and entry gates are satisfied. It must implement
the accepted specification rather than a convenient approximation.

Acceptance is a distinct human-authority stage. Assumption confirmation,
open-question resolution, alignment, or a general instruction to continue does
not by itself accept an initiative. Delivery follows exactly one type-specific
path: implementation creates or changes products, design creates or changes
initiative specifications, and planning creates initiative-local evidence.

Codex must not claim completion until:

- every in-scope requirement maps to a delivered product or evidence output;
- applicable invariant and acceptance gates pass;
- verification exists for the exact bounded claim;
- initiative, product, source mapping, and status records agree; and
- remaining work is explicitly deferred, blocked, transferred, cancelled, or
  otherwise given a truthful owner and disposition.

An unfinished requirement must not disappear because a version, branch,
initiative, or program is closing.

## Initiative review checklist

- [ ] The realization is treated as input rather than specification authority.
- [ ] The initiative uses the complete current template.
- [ ] The initiative owns one narrow outcome and is not an umbrella container.
- [ ] Every normative claim is invariant-compatible and traceable.
- [ ] Cross-initiative ownership and dependencies are coherent.
- [ ] Assumptions and questions retain their required human gates.
- [ ] Revisions preserve prior state and explain every affected claim.
- [ ] Lifecycle and completion statements match verified evidence.

