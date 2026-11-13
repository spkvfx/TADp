# Codex initiative scope specification

## Purpose

This specification prevents umbrella initiatives and defines when proposed or
legacy work must be decomposed. Every initiative owns one independently
reviewable outcome and one acceptance claim.

## Documentary sources

Use specification 02's
[canonical template rules](02_Codex_Initiative_Governance_Specification.md#canonical-template-selection-and-use)
and specification 08's
[preceding preparation procedure](08_Codex_Initiative_Workflow_Specification.md#documentary-prerequisite-preparation)
for records required by this specification. The
[coverage map](../../../template/TEMPLATE-COVERAGE.md) identifies reusable file
and embedded-section sources, their destinations, owners, and conditional
triggers. Documentary recovery does not supply missing authority, identity,
decisions, work, verification, or legal lifecycle events; this specification's
substantive requirements remain binding.

## Cohesion test

An initiative is narrow only when all of the following describe one coherent
unit:

- outcome and beneficiary;
- specification and authority boundary;
- accountable owner;
- permitted initiative type and output class;
- acceptance and verification claim;
- lifecycle and release disposition; and
- compatibility, migration, and recovery boundary.

Shared timing, product area, team, dependency, release, or theme does not by
itself make multiple outcomes one initiative.

## Mandatory split triggers

Create separately scoped initiatives when any proposed portion has:

- an independently acceptable outcome;
- a different accountable owner;
- a materially different authority or specification boundary;
- a different initiative type;
- separable verification, release, cancellation, or completion;
- an unrelated product destination or compatibility obligation; or
- a lifecycle that could truthfully advance or stop without the rest.

A proposal that meets a split trigger must not be accepted until the work is
decomposed or a human authority records an invariant-compatible reason that
the trigger does not apply.

For work governed by the
[version-realization-initiative correlation specification](09_Codex_Version_Realization_Initiative_Correlation_Specification.md),
every mandatory split allocates a separate self-contained initiative with an
independent ID, acceptance claim and recorded execution assignment. Split
initiatives may share an exact version scope, originating realization notes,
and a declared scope branch. A scope, parent, sibling, subinitiative or release
must not act as an umbrella acceptance claim for independent outcomes.

## Siblings and subinitiatives

Use sibling initiatives when their outcomes stand independently. Use a
subinitiative only when a real parent specification owns one bounded claim and
a dependent portion needs its own decisions, execution, or verification.

A parent may coordinate shared gates and aggregate verified status. It must not
absorb separate outcomes, hide incompatible authority, or claim completion from
partial child results. Every subinitiative must cite the exact parent
requirement, state the boundary retained by the parent, and keep its own
coherent lifecycle and completion evidence.

## Scope assessment

Every initial initiative suite must contain `scope-assessment.md`. It records
the cohesion test, each split trigger, parent or sibling rationale, exclusions,
and the exact bounded acceptance claim. A scope assessment is evidence about
the proposed boundary; it does not waive a human decision or authorize work.

## Legacy decomposition

When an existing broad initiative must be split, preserve its identity and
historical claims. Record the decomposition event, map every requirement,
decision, source, dependency, product, and verification claim to a continuing
owner, and create narrow successor or subinitiative records through the normal
workflow. Never rewrite history to imply that the old initiative was always
narrow.

Under the adopted version-scope revision, each narrow successor or subinitiative
receives its own identity and complete records; source and scope reuse is valid.
Coherent same-outcome revision need not create a successor. A pre-effective
broad initiative retains its complete compatible migration-ledger disposition
until separately governed adoption, migration or successor allocation.


