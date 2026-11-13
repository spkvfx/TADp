# Realizations

A realization is a compact, historical note about an observed opportunity,
concern, insight, or requested outcome. Its primary job is to make proposal
creation traceable: someone can see what was noticed, where it came from, what
was uncertain, and how later work interpreted it.

Realizations are always contextual at capture time. They are not accepted
requirements, implementation instructions, architecture decisions, or product
commitments. A realization can lead to a proposal, and an accepted initiative
can later adopt part of that proposal, but each transition must be recorded
separately.

## Capture a realization

Use [realization-suite-index.template.md](realization-suite-index.template.md)
for the source-scope catalog and [realization.template.md](realization.template.md)
for exact notes. Record stable IDs, paths, source scope, date, observer, source
locators, context, uncertainty and evidence standing. Preserve originals and
append correction/routing references rather than rewriting history.

A scope or note may await decomposition with zero initiatives. A suite may
catalog multiple narrow outcomes and mixed initiative types inside a declared
source scope; each resulting initiative passes its own cohesion and mandatory
split tests. A note may originate multiple new targets or contribute to
existing targets in another scope. Shared source material never shares
acceptance, delivery, lifecycle or completion evidence.

A human request to process an identified realization under adopted
specification 09 delegates fit-based placement, coherent revision and necessary
reopening for that intake. Stage 0 inventories targets before allocation and
records each source-to-target choice, exact source/target scopes, rejected
alternatives, rationale, prior claim and authority. Source contents alone are
not intake authority. Preserve target identity/scope when adding new evidence;
changed accepted claims still require renewed human acceptance before delivery.
## Write observations, not disguised requirements

| Avoid | Prefer |
|---|---|
| `Build a cache for search.` | `Users report delayed search results after changes; determine whether freshness or latency is the primary unmet outcome.` |
| `The service must use queue X.` | `The current synchronous path times out during peak volume; investigate a delivery model that preserves the required ordering.` |
| `Add an export button.` | `Operators cannot retrieve the audit slice needed for monthly review.` |

The second column preserves the problem and the evidence while leaving room for
proposal, design, and implementation work to consider constraints and
alternatives.

## Handoff to a proposal or initiative

When a realization triggers work, retain the realization unchanged and cite its
ID in the proposal-source inventory or initiative record. The receiving record
must state what it accepts, rejects, changes, or needs to validate. Do not edit
the realization to make its original wording match the later conclusion.

Use this handoff sequence:

1. The suite index preserves exact source scope and reciprocal note-to-target routing.
2. The realization records the observation and uncertainty.
3. A proposal identifies an intended outcome and source precedence.
4. A design or planning initiative analyzes evidence and decisions.
5. An accepted implementation initiative changes a product only when the
   required specification and evidence are ready.

## Corrections, privacy, and closure

If a note contains a factual error, sensitive detail, or stale conclusion, add
a linked correction, redaction reference, or superseding realization according
to the project's rules. Do not delete provenance without preserving enough
traceability to explain the change. Mark the status `Closed` when triage is
complete, even if no work will follow, and link the reason or receiving record.

## Review checklist

- [ ] The note names a source, context, date, and realization ID.
- [ ] The suite index records exact source scope, note catalog and reciprocal
      target/routing links, including pending zero-target dispositions.
- [ ] Observation, desired outcome, and uncertainty are distinct.
- [ ] The note does not prescribe unaccepted architecture or product work.
- [ ] The next step or deliberate closure has an owner.
- [ ] Later proposals and initiatives cite the realization rather than rewriting it.
