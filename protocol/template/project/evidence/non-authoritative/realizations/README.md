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

1. During Stage 0, preflight one unused canonical work version, suite ID and
   path, initiative ID and path, version-bearing branch, base branch, and base
   commit. Create them only after the full tuple is unambiguous and unique.
2. Copy [realization-suite-index.template.md](realization-suite-index.template.md)
   to the work-version directory as its `00-...-suite-index.md`. Record the
   suite boundary, reciprocal initiative and branch identity, and link to the
   canonical project correlation row.
3. Copy [realization.template.md](realization.template.md) to a descriptive,
   stable filename such as `RZN-001-checkout-friction.md` within that suite.
4. Assign a realization ID and record the original source, observer or reporter,
   date, context, and any related artifact. If the source is a conversation,
   identify the participant or channel only to the degree appropriate for the
   project's privacy and retention rules.
5. Write the **Realization** in one concise statement. It should describe what
   was observed or requested, not prescribe a solution.
6. Complete the context table. Explain who or what is affected, when and where
   the observation applies, evidence locators, assumptions, and uncertainty.
7. Describe a **candidate outcome** in user- or operator-visible terms. Avoid
   design or product language until a proposal and initiative have accepted it.
8. Name a suggested next step and owner: create a proposal, perform research,
   triage, link to an existing initiative, or deliberately take no action.
9. Remove the HTML instruction comment only after every token is replaced.

All notes in one suite must share one narrowly bounded outcome, owner,
authority boundary, output family, verification claim, and lifecycle. A
mandatory split receives a new work version, suite, initiative, and branch.
The suite and its version remain identity records, not accepted authority.

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

1. The suite index preserves the work-version and reciprocal tuple identity.
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
- [ ] The suite index records one canonical work version and reciprocal
      initiative, branch, base, and canonical-row links.
- [ ] Observation, desired outcome, and uncertainty are distinct.
- [ ] The note does not prescribe unaccepted architecture or product work.
- [ ] The next step or deliberate closure has an owner.
- [ ] Later proposals and initiatives cite the realization rather than rewriting it.
