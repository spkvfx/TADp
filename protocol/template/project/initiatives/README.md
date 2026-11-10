# Initiatives

This directory holds authoritative records of bounded work. An initiative says
what outcome is intended, what evidence and decisions govern it, who owns it,
what it may change, and how completion will be proved. It is authoritative for
its declared scope, status, and accepted work—not for rewriting another
initiative's scope, binding evidence, or an observed product state.

## Begin and register an initiative

Use the following workflow for every new effort:

1. Determine the initiative type from the output it is permitted to create,
   not from the title or team name.
2. Create a uniquely named directory inside the correct type directory, such as
   `implementation/INIT-IMP-001-payment-retries/`. Do not place unrelated
   initiatives in one shared folder or one shared document.
3. Copy the complete
   [canonical initiative template suite](../../initiatives/README.md) into the
   new directory. It is the single source of truth for every initiative type;
   specialize its content without dropping required artifacts.
4. Replace every token, remove the instruction comment, cite applicable
   authoritative evidence precisely, and distinguish contextual input from
   binding requirements.
5. Copy [initiative-index.template.md](initiative-index.template.md) to
   `initiative-index.md` and [status.template.md](status.template.md) to
   `status.md` before registering the first initiative. Add the initiative to
   both records. Include the initiative ID,
   record path, type, status, owner, governing evidence, primary output, and
   next gate. The index is the stable registry; the status record is the
   current lifecycle and blocker view.
6. Obtain the required review before changing a status from `Proposed` to
   `Accepted` or beginning the type's permitted output.

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
locator. Binding claims come from `../../../evidence/authoritative`; research, proposal
input, and observations are `../../../evidence/non-authoritative` until accepted
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

