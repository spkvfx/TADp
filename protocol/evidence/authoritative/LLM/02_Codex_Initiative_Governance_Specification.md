# Codex initiative governance specification

## Scope

This specification governs how Codex interprets realization notes and creates,
reviews, changes, executes, and reports initiatives.

Apply the canonical
[prompt keyword specification](11_Codex_Prompt_Keyword_Specification.md)
to every governed task. The human decision, acceptance, execution, completion,
and reopening requirements below are the ordinary contract. Only exact
requirements named by specific human exception authority and recorded before
reliance may receive the stated replacement; every other obligation remains.
Mode requests alone are insufficient, inferred exceptions require confirmation,
and locks, truthful evidence, and ordinary lifecycle meanings remain enforced.

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

## Canonical template selection and use

Select the canonical reusable source for the record's role, declared initiative
type, recorded governing revision, and owning stage. The
[coverage and use map](../../../template/TEMPLATE-COVERAGE.md) identifies file,
embedded-section, conditional, and response-shape sources; it is navigation,
not a competing authority or a new document obligation. Reuse an existing
suitable source instead of creating a duplicate record. A required section
remains part of its canonical owning record.

Copy a durable source to its declared destination outside protected `template/`
before populating it. Preserve existing customization, stable IDs, immutable
identity, exact human text, accepted baselines, and history. Replace placeholders,
retain required sections, and cite a governing reason for conditional
non-applicability; empty or unresolved fields must be explicit. Recalculate
relative links from the instance's actual directory, including scope/type depth.
Response-shape templates define an answer only and create no durable-file
requirement; Stage 9 readiness is such a response unless a governing rule
explicitly requires a durable record.

For each material populated claim retain the source path or stable ID, precise
locator, evidence standing, revision or event/date when available, and limits.
Inspect underlying material references within the named project and work
boundary: applicable invariants and accepted decisions first, then source
inventories/mappings, realization inputs, actual human instructions/receipts,
initiative and dependency records, affected products, implementation,
configuration, tests, verification, and Git history. Include relevant proposed
and partial effort and affected closed claims without promoting their standing.
Record unavailable, unreadable, stale, conflicting, and out-of-scope evidence
and its effect. External access requires otherwise sufficient permission.
Neither an enclosing repository nor a linked prompt expands the scope.

Validate identity, required fields, provenance, authority, links, lifecycle,
and current applicability before using the instance. A plausible field value
does not satisfy a gate. Apply specification 08's bounded preparation procedure
for missing or stale documentary prerequisites, reusing valid records and
receipts idempotently. If a required canonical source is genuinely missing,
report its governing requirement and route it to separately authorized protocol
maintenance; ordinary workflow execution cannot invent or edit reusable sources.

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
clearly bounded task. Before relying on it, record the actual instruction and
authority in the required receipt and specification 11 exception record,
identifying every covered source ID and exact human-input rule. Preserve the
actual agent author, method, result, rationale, affected IDs, limitations, and
consumer reconciliation for each autonomous disposition. Do not fabricate a
human answer or ask repeatedly within the same sufficient approved scope.
It does not authorize an invariant conflict or apply automatically to other
initiatives, assumptions, or questions. Preview dispositions remain drafts.

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

## Correlated allocation and successor work

For work governed by the
[version-realization-initiative correlation specification](09_Codex_Version_Realization_Initiative_Correlation_Specification.md),
Codex must assess realization fit before allocation. Each initiative has one
immutable scope membership, independent ID and complete type-specific records,
precise originating and later contributing note provenance, and one recorded
active dedicated/shared execution assignment per revision cycle. The scope
registry and initiative index own their respective canonical records; copies
link there without acquiring lifecycle authority. Several narrow initiatives
may share a scope, realization sources or a declared scope branch.

A human instruction to process an identified realization under this adopted
workflow delegates the specification 09 placement, append/revision choice and
necessary reopening method for that intake. Inventory candidates and record
actual source authority, fit, alternatives and consequences before acting.
A coherent narrow outcome may retain its identity through revision. Independent
outcomes and incompatible type/owner/authority boundaries still require a
separate initiative or successor with complete records. Never infer migration,
merge identities or fabricate acceptance to avoid these boundaries.

## Reopening and revising initiatives

An open initiative may be revised through its applicable workflow, but the
change must be explicit and fully documented. A closed initiative must be
explicitly reopened before its claim is refined. Only append-only factual
historical corrections and administrative or successor references that retain
the prior claim are exempt, as defined by the
[coherence specification](10_Codex_Initiative_Coherence_Specification.md).

Before changing substantive initiative meaning, Codex must record:

- the actual human instruction, governing delegation or specific revision authority, and LLM decision author;
- the prior lifecycle state and exact accepted or completed claim;
- the reason for change and the newly affected scope;
- every changed assumption, decision, invariant mapping, specification,
  dependency, product, test, migration, release, or operational claim;
- compatibility and recovery effects for previously delivered products;
- the verification required for the revised claim; and
- the effective date or event and the records that must be reconciled.

Apply specification 09's recorded fit method rather than forcing a successor
for every substantive change. Before changing an accepted or in-progress
normative claim, pause affected delivery, preserve partial-work evidence and
return to `Proposed`. Alignment and renewed explicit human acceptance precede
resumed delivery. Closed targets first require a recorded reopening to
`Proposed`, including each affected closed scope or ancestor, under bounded
intake delegation or separate human authority. Direct return to `Accepted`
requires a separate human unchanged-claim decision. Reconcile a superseded
target with its replacement and preserve continuing ownership. Intake routing
does not decide unrelated questions, accept claims or pass completion gates.

Codex must preserve the earlier state through history, an explicit supersession
relationship, or a durable change record. It must update every affected
initiative document and tracking record in the same coherent change. Reopening
does not erase prior evidence, retroactively falsify an earlier truthful claim,
or authorize unrelated scope.

If the requested revision conflicts with an invariant, Codex must use the
invariant-conflict procedure instead of revising the initiative into a
contradictory state.

## Execution and completion

Open initiative effort, including proposed and partially performed work, must
be included in coherence and impact reviews without gaining accepted authority.
Record incompatible work in `initiatives/work-conflicts.md` and affected
initiative records; invariant contradictions also enter the invariant conflict
register. Completion must review every other open initiative and affected
closed claims, then reconcile blockers or route compatible refinements under
specification 10. Completion never authorizes silent cross-initiative edits.

Under the ordinary workflow, Codex may execute work only when the initiative
type permits that output and all required human decisions and entry gates are
satisfied. A specific documented exception may permit named bounded prompt
work under specification 11; it does not manufacture initiative acceptance,
readiness, or completion. Retain the last truthful lifecycle state where those
ordinary prerequisites remain unmet. Codex must implement
the accepted specification rather than a convenient approximation.

Acceptance is a distinct human-authority stage. Assumption confirmation,
open-question resolution, alignment, or a general instruction to continue does
not by itself accept an initiative. Delivery follows exactly one type-specific
path: implementation creates or changes products, design creates or changes
initiative specifications, and planning creates initiative-local evidence.

Codex must not claim ordinary initiative completion until:

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

