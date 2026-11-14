# Planning initiatives

Use this directory for an initiative whose primary output is **planning
evidence** for another initiative or authority. Typical outputs include a
feasibility assessment, dependency analysis, sequence plan, risk analysis,
option comparison, repository audit, or scoped recommendation. A planning
initiative can make uncertainty visible and improve a later decision; it does
not create products or change specifications itself.

## Start a planning initiative

1. Use Stage 0 to select or allocate the exact
   initiatives/<scope>/<type>/<id-and-slug>/ destination under the adopted
   workflow. This baseline type folder explains the output boundary; it does
   not own unscoped live initiatives or allocate identity.
2. Use the [coverage map](../../template/TEMPLATE-COVERAGE.md) and
   [common initiative sources](../initiative-README.template.md) to instantiate
   only the records owned by the current activity. Remove .template from
   instance names and recalculate links. Do not copy conditional late-stage
   records during initial creation.
3. Write one answerable planning question and name the initiative(s), decision
   owner(s), or governance body that will consume the result.
4. Define the evidence boundary: sources to examine, methods allowed, limits,
   and what the initiative will not decide or implement.
5. Record findings with evidence locators and distinguish binding sources from
   contextual input. Recommendations must name their consumer and next action.
6. Register the initiative in the parent index and arrange the review or
   handoff gate before beginning substantial analysis.

## Complete the planning template

| Template section | Expected content |
|---|---|
| Planning question and intended evidence | The decision or initiative the work will inform, without claiming it already decides the outcome. |
| Included/excluded boundary | Specific research, analysis, or report work; explicit exclusion of products and specification changes. |
| Method and inputs | Sources, methods, environments, assumptions, and limitations sufficient for another reviewer to reproduce the reasoning. |
| Findings and recommendations | A separated finding, its evidence, a proposed action, and the receiving initiative/owner. |
| Completion and handoff | Proof that sources are classified, the report stays local, consumers are named, and no prohibited output was created. |

Use language that distinguishes evidence from recommendation. `The audit found
that module X owns the only migration routine` is a finding with a locator.
`A design initiative should decide whether to centralize the routine` is a
recommendation. `Centralize the routine now` would be an unaccepted design or
implementation directive and belongs elsewhere.

## Output boundary and handoff

Planning work may create and revise only its own initiative record and
initiative-local reports. Keep reports in the initiative directory, give them a
clear title and source inventory, and link them from the initiative README. Do
not update another initiative's specification, edit authoritative evidence, or
change a product as part of this work.

When the planning output is ready, the receiving initiative or authority
chooses whether to accept, reject, or further investigate the recommendation.
That decision belongs in the receiving record. The planning report remains
evidence with its own limits; it does not become a specification merely because
another initiative cites it.

## Evidence and confidence

For every finding, identify the source, date/revision, exact locator, evidence
classification, and limitation. If analysis draws an inference, label it as an
inference and explain the reasoning. If sources conflict, preserve the conflict
and route it to the relevant authoritative owner rather than resolving it by
assertion. A planning report normally remains non-authoritative until an
explicit owning authority accepts a distinct binding record.

## Completion checklist

- [ ] The planning question, consumer, and intended decision are explicit.
- [ ] Methods, sources, confidence, and limitations are recorded.
- [ ] Findings, interpretations, and recommendations are distinguishable.
- [ ] Reports remain in this initiative and cite precise evidence.
- [ ] No product, specification, or authoritative record changed as a result.
- [ ] The handoff, receiver, and next decision gate are linked in the record.
- [ ] The parent initiative index reflects status and next milestone.
