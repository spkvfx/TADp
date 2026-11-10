# Codex initiative scope specification

## Purpose

This specification prevents umbrella initiatives and defines when proposed or
legacy work must be decomposed. Every initiative owns one independently
reviewable outcome and one acceptance claim.

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


