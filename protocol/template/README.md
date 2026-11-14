# Project baseline and reusable library

This directory contains the complete TADp reusable library. Its `project/`
directory is the clean project-shaped baseline; its `prompts/` directory is
the operational workflow library. Initiative record sources belong under
`project/initiatives/`, alongside that baseline's coordination sources.

## Baseline copy contract

Copy the project baseline's ordinary files directly, retaining their names.
Files ending in `.template.md` are reusable record shapes: retain them during
installation, then instantiate only the selected source at its declared
destination and owning trigger. Remove `.template` from actual record names
and populate evidence-backed fields; a source file creates no live work.

Every project also receives this entire library at `P/template/`, where
project root `P` is the scaffold installation directory defined by
[specification 05](../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement).
`P` may equal or lie beneath the Git worktree root. The source `project/`
scaffold and installed library are protected reusable material, never active
project targets merely because they contain project-shaped files.
`project/template/README.md` documents that destination without embedding the
library recursively. During installation the complete outer library supplies
that destination; do not overwrite its README with the placeholder.

The baseline contains navigation, applicable record shapes, runtime support,
governing protocol rules and project-use guides. It contains no TADp live
initiatives, development reports, decisions, delivered project products or
test results. The empty project conflict register does not inherit TADp's
active conflicts. Protocol revision history identifies upstream provenance;
it is not the adopting project's history or adoption evidence.

## Layout revision and compatibility

The user's 2026-11-13 instruction explicitly requests this consolidation,
complete folder navigation, nonrecursive library placeholder and clean
baseline. Git preserves the former sibling `initiatives/` source and original
filenames. The coverage map and necessarily affected prompts, source links,
tools and integrity locks follow the new source locations. Substantive
protocol rules, stage ownership, instance destinations and lifecycle claims
do not change. Existing projects retain their sources and work until an
authorized update; synchronization never deletes retired or user-owned files.

The [canonical coverage and use map](TEMPLATE-COVERAGE.md) identifies the
source, destination, applicability, owning activity, evidence, and checks for
each required record or embedded section. Read it before selecting a source;
embedded sections and conditional response shapes retain their owning record.

## Protected source boundary

This complete tree is protected reusable source. Read or copy it during
ordinary work; do not edit, fill, rename, move, or delete files in place.
`AGENTS.md` carries that boundary into Codex's directory-scoped instructions,
and `.tadp-lock.json` lets the validator detect content or file-set drift.

Instantiate a record outside `template/` and edit the copy. A change to this
tree requires an explicit human request for the exact reusable-source change,
compatibility and migration review, affected-consumer updates, verification,
and a governed lock refresh. A lock refresh is not a repair for an unintended
template edit.

## Protocol vocabulary

- `../evidence/authoritative` replaces the former `invariants` label. It identifies
  binding evidence that governs a specification or product decision.
- `../evidence/non-authoritative` identifies contextual, exploratory, or supporting
  evidence. It can inform a decision but cannot by itself override
  `../evidence/authoritative`.
- A **product** is output material placed in a repository, distribution channel,
  or other declared destination. Products include executable code, scripts,
  SDKs, APIs, product documentation, and similar deliverables. A document that
  defines what a product must do is a **specification**, not a product merely
  because it is a document.

- [Initiative templates](project/initiatives/initiative-README.template.md) define the standard initiative
  record: proposal sources, assumptions, scope, specifications, evidence
  mapping, decisions, delivery roadmap, delivery steps, type-specific work
  records, completion evidence, and the minimal preparation skeletons used at
  Stage 0.
- [Project templates](project/README.md) define project profile and initiative
  indexes, the canonical realization-suite index, and the pre-effective
  correlation migration ledger, plus the work-conflict register and coherence
  adoption baseline.
- [Initiative prompts](prompts/README.md) provide focused workflows for
  preparing an initiative branch, proposal creation and alignment, initiative
  creation and alignment, human-led assumption and decision reviews, explicit
  acceptance, type-specific delivery, implementation readiness, and
  finalization.

Use the initiative templates to structure a new initiative. Use a prompt only
for its named workflow; the initiative type, evidence classification, and
repository evidence continue to govern the outcome.

## Protocol directory readmes

The reusable templates operate with the protocol directories at this project
root:

- [Authoritative evidence](../evidence/authoritative/README.md) provides
  invariant conditions that initiatives and products must meet.
- [Non-authoritative evidence](../evidence/non-authoritative/README.md)
  provides clues and context only; it cannot supersede binding evidence.
- [Realizations](../evidence/non-authoritative/realizations/README.md) provide
  permanently non-authoritative notes for proposals from their sole canonical
  location.
- [Initiatives](../initiatives/README.md) hold authoritative, conflict-resolved
  initiative records.
- [Products](../products/README.md) identify authoritative output placements.

Keep the copied initiative record coherent with these directories. Do not use a
template, proposal, realization, or product convenience to silently alter
`../evidence/authoritative`.

## Scope grouping and integration sources

Newly governed initiative records belong under initiatives/<scope>/<type>/<id-and-slug>/.
The project sources include the canonical [scope registry](project/initiatives/version-scopes.template.md),
[scope navigation README](project/initiatives/scope-README.template.md),
[membership index](project/initiatives/initiative-index.template.md), and
[prospective adoption ledger](project/initiatives/version-scope-migration-ledger.template.md).
Stage 0 records fit-based routing before allocation, including coherent revision
and necessary reopening under its bounded adopted intake authority. It chooses
a dedicated child or declared shared scope assignment with per-cycle history.
[Scope closure](prompts/scope_closure.md) is separate from member finalization
and integrates only into the recorded immediate parent after its own gates.
Preserve legacy paths and claims during distribution synchronization.
When instantiating an initiative in the grouped layout, recompute all relative
links from its actual scope/type depth rather than copying navigation paths
from the reusable source location.

The [integration receipt source](project/initiatives/integration-receipt.template.md)
records exact current-cycle source/target Git evidence, closure authority,
post-integration checks and explicit exclusion/transfer/no-deliverable outcomes.
