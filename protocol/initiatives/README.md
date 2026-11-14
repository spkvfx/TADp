# Initiatives

This directory holds authoritative records of bounded work. An initiative says
what outcome is intended, what evidence and decisions govern it, who owns it,
what it may change, and how completion will be proved. It is authoritative for
its declared scope, status, and accepted work—not for rewriting another
initiative's scope, binding evidence, or an observed product state.

## Begin and register an initiative

Process identified realizations through Stage 0 fit assessment before allocation.
Inventory existing targets and scopes; record append, coherent revision,
reopening or new-initiative dispositions under the adopted bounded intake
method. Existing complete records are reused. Acceptance remains human.

For new work use initiatives/<scope>/<type>/<initiative-id-and-slug>/, retaining
implementation/design/planning output boundaries. Each initiative owns complete
independent records; it may share scope, notes and a declared scope branch.

Instantiate the [scope registry source](../template/project/initiatives/version-scopes.template.md)
as `version-scopes.md`; use the [scope navigation source](../template/project/initiatives/scope-README.template.md)
for scope READMEs. Instantiate the [membership index source](../template/project/initiatives/initiative-index.template.md)
as `initiative-index.md`, owning one membership/provenance row per initiative;
the [status source](../template/project/initiatives/status.template.md) supplies
the `status.md` view. Record adoption and legacy dispositions using the
[scope migration ledger source](../template/project/initiatives/version-scope-migration-ledger.template.md). Preserve
earlier correlation migration history without retroactively relabeling it.

Stage 0 prepares scope/ancestor records when needed and chooses dedicated child
or existing shared scope execution. Create only the new initiative's minimal
README skeletons there. Stage 1 creates its proposal and Stage 3 completes the
[canonical initiative source](../template/project/initiatives/initiative-README.template.md). Later delivery records
are created only when their respective stages begin. Use
[work-conflict register source](../template/project/initiatives/work-conflicts.template.md) for all relevant open
and partial effort; preserve their original authority standing.
Reusable record sources remain in the protected
[template library](../template/project/initiatives/README.md). This directory
contains navigation and actual work records when their workflow triggers occur;
it does not keep duplicate `.template.md` files. Select sources through the
[coverage map](../template/TEMPLATE-COVERAGE.md), copy only the required source
to its declared destination, remove `.template` from the instance filename,
and populate evidence-backed fields through the owning stage. Never fill or
modify the source in `template/`.

The type directories define output boundaries only. They do not carry separate
initiative templates. Every design, implementation, and planning initiative
uses the same canonical suite so structure and review gates cannot drift by
type.

## Narrow scope and subinitiatives

Each initiative must own one narrowly bounded outcome, authority boundary, and
acceptance claim. Do not create umbrella or multi-purpose initiatives and do
not use a shared directory as a substitute for separate initiative records.

Use separate initiatives when outcomes can be accepted independently, have
different owners, cross materially different authority boundaries, or need
different completion evidence. A subinitiative is allowed when it owns one
smaller dependent outcome inside a genuine parent specification. It must cite
the parent requirement, preserve its own decisions and verification, and leave
unrelated work with the parent or another initiative.

## Choose the type by output boundary

| Type | Primary alignment direction | It may create or modify | It must not do |
|---|---|---|---|
| [design](design/README.md) | Specifications to observed product state | Specifications and supporting initiative evidence | Create a new product to make its specification appear aligned |
| [implementation](implementation/README.md) | Products to accepted specifications | Products and product documentation | Silently modify an existing specification |
| [planning](planning/README.md) | Evidence for another initiative's decision | Its own record and initiative-local evidence/reports | Create products, specifications, or edits outside declared scope |

If an implementation effort discovers a specification problem, stop the
affected product work and create or route a design initiative. If a design
initiative needs evidence before it can specify behavior, create or cite a
planning initiative. Type boundaries are a safety mechanism: they prevent a
single effort from creating the evidence, deciding what it means, and
implementing it without an independent review point.

## Required contents of an initiative record

Every reviewable canonical record includes:

| Subject | What to record | Why it matters |
|---|---|---|
| Identity and stewardship | Initiative ID, title, type, status, owner, last updated | Lets reviewers find the accountable record and know whether it is current. |
| Correlation identity | Exact scope, originating/contributing notes, initiative path, revision/assignment history, captured base, integration evidence and canonical row | Prevents identity reuse, drift, partial mappings, and umbrella versions. |
| Intended outcome | Observable result rather than only a task list | Defines what completion means. |
| Scope boundary | Included work, exclusions, products/specifications/evidence it may touch | Prevents accidental expansion or cross-initiative edits. |
| Evidence basis | Precise IDs, links, sections, classifications, and known gaps | Distinguishes mandates from context. |
| Decisions and risks | Open question, decision owner, resolution gate, dependency, conflict | Makes uncertainty visible before irreversible work. |
| Output and verification | Product destination, specification, report, tests, review, release or recovery evidence | Provides a traceable completion gate. |

Use `Not applicable — {{reason}}` for a required field that truly does not
apply. Do not remove a section simply because the answer is not ready; a blank
section hides a decision gap that a reviewer needs to see.

## Status and review gates

Use these statuses consistently:

- **Proposed:** source material, scope, assumptions, or decisions are still
  under review. No type-prohibited output may be created.
- **Accepted:** a named authority has approved the scope, type, and required
  evidence/decision gates. The initiative may begin its permitted work.
- **In progress:** permitted work is underway and evidence of completed gates
  is being recorded.
- **Completed:** type-specific acceptance conditions pass, output is linked,
  and remaining deferred work has a home.
- **Cancelled:** work stops without a replacement; retain the reason and
  reusable evidence.
- **Superseded:** another initiative replaces this one; link the replacement
  and keep the original as historical context.

Update the index whenever status, next milestone, owner, governing evidence,
or dependency changes. Keep the initiative's own record as the source for
detailed decisions; the index is a discovery and coordination tool, not a
second decision log.

Update `status.md` whenever an initiative's lifecycle standing, next gate,
blocker, or status evidence changes. Keep applicable parent and subinitiative
tracking coherent. A tracking entry does not accept a proposal, confirm an
assumption, resolve a decision, authorize implementation, or establish release
readiness.

## Evidence, conflicts, and cross-initiative work

Every material requirement must cite evidence with a stable ID and precise
locator. Binding claims come from `../evidence/authoritative`; research, proposal
input, and observations are `../evidence/non-authoritative` until accepted
elsewhere. Link an initiative to the product it governs, but do not describe an
existing product as if the initiative already changed it.

When two initiatives, an initiative and a product, or an initiative and
authoritative evidence disagree, preserve all records and write down the
conflict. Name the incompatible claims, affected scope, owner, decision needed,
and stop condition. Never edit another initiative's record merely to make this
one look coherent.

## Completion checklist

- [ ] The initiative is in the correct type directory and has a stable ID.
- [ ] Its record names outcome, scope, owner, evidence, dependencies, and
      permitted output.
- [ ] Binding and contextual evidence are classified and cited precisely.
- [ ] Open decisions, conflicts, and risks have owners and gates.
- [ ] The type-specific completion conditions are verified.
- [ ] Product, specification, or planning evidence is linked at its durable
      destination.
- [ ] The initiative index and any dependent records reflect the final status.
- [ ] The portfolio status record identifies the current gate and links the
      evidence supporting the status claim.
