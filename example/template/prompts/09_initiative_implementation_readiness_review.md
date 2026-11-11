<!--
Replace every braced placeholder before using this prompt.
-->

# 9. Initiative implementation-readiness review

## Use when reviewing an existing initiative immediately before execution

Use this prompt immediately before an existing `implementation` initiative
begins the reviewed product-execution phase or work set. It gathers and reports
current evidence; it
does not create or update the initiative, an implementation-readiness document,
or any product artifact. The review compares all material existing evidence
against the initiative's current claims without implementing work, realigning
the initiative, or expanding its scope.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [initiative implementation-readiness review prompt](09_initiative_implementation_readiness_review.md),
> perform the pre-execution review for the attached initiative's requested
> phase or execution scope.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Initiative implementation-readiness review
prompt** block below. Do not execute, recurse into, or derive additional work
from the example.

## Initiative implementation-readiness review prompt

~~~text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Perform an implementation-readiness review for the existing {initiative} at
{initiative_path}, immediately before execution of
{phase_or_execution_scope}.

This is an evidence-based implementation-entry review, not implementation,
initiative alignment, or a new design exercise. Treat the existing initiative
as the subject of the comparison. Do not invent a different outcome, boundary,
architecture, owner, contract, phase, or acceptance condition to make the
evidence fit.

Verify that the target's declared type is `implementation`. A `design`
initiative changes specifications and a `planning` initiative creates evidence;
neither is eligible for this product-execution readiness review.

Verify that the initiative is `Accepted` or `In progress`, links an explicit
acceptance receipt, and identifies the accepted baseline revision. A coherent
proposal or completed human reviews do not substitute for acceptance.

Verify that the canonical work version, realization suite, initiative,
dedicated branch, captured base branch and commit, reciprocal links, and live
active branch agree. Treat any missing, duplicate, partial, or inconsistent
correlation as a no-go blocker; this read-only review must not repair it.

Apply the ownership and approval convention at {project_profile_path}. Human
owner, reviewer, and approver roles resolve as recorded for the target project.
Continue to treat a missing technical component, selected profile or placement,
external party, contract, artifact, or verification evidence as a readiness
gap.

The shared initiative template defines the standard record roles. An existing
initiative can also contain historical or initiative-specific readiness reviews,
implementation reports, consistency reviews, audits, or differently named
source maps. Read a linked record as evidence only; its title does not make it a
substitute for a missing standard record or prove the current phase is ready.
Record a template deviation or a stale, differently scoped review as a gap.

Before writing, verify that:

- {initiative_path} exists and has a readable initiative index;
- the initiative index, proposal source inventory and proposal, assumption,
  architecture, source mapping, open-question register, delivery roadmap,
  implementation steps, and every supporting record linked by the index are
  readable, or their absence is explicitly documented as an existing
  initiative condition;
- {initiative_template_root}/initiatives/implementation-readiness.md is readable;
- the reviewed phase or work set is unambiguous in the existing roadmap and
  implementation steps;
- the initiative's evidence labels, precedence rules, dependencies, and
  affected product boundaries can be identified from its existing records; and
- every SDK/API surface required by the reviewed phase has a recorded result
  from the initiative SDK/API alignment prompt; treat a blocked or conflicting
  surface as a readiness blocker for the affected work.

If the initiative itself is missing, ambiguous, or lacks enough initiative
records to identify the intended work, stop and report the exact blocker. Do
not create a partial readiness review, scaffold missing initiative material, or
substitute a newly inferred initiative.

Build a complete evidence-coverage inventory before reaching a readiness
conclusion. Treat "all existing evidence" as every material source that the
initiative's source inventory, source mapping, proposal, assumption,
architecture, decision register, roadmap, implementation steps, linked
supporting records, dependencies, and affected product boundaries identify,
plus current repository artifacts and verification evidence in those
boundaries. At minimum, cover:

1. `evidence/authoritative`, accepted repository decisions and specifications,
   released contracts, completed initiatives, and any precedence or
   cross-initiative review that the initiative identifies.
2. Every current initiative record, including its intended outcome, included
   and excluded scope, assumptions, accepted and unresolved decisions,
   ownership boundaries, source mappings, dependencies, phases, delivery
   steps, acceptance gates, and verification requirements.
3. Current repository evidence in the affected boundaries: source,
   configuration, schemas, migrations, packages, tests, fixtures, operational
   material, generated artifacts, release records, and recorded command or
   environment results. Read beyond summary tables and path inventories when
   needed to compare the actual behavior or artifact with the initiative.
4. Existing dependency and integration evidence: owner assignments, public
   interfaces, compatibility commitments, migrations, security controls,
   recovery and rollback limits, external environment constraints, and
   verification prerequisites.
5. Canonical correlation and Git evidence: project index row, suite index,
   initiative metadata, branch ref, captured base, and any authorized branch
   removal evidence relevant to historical dependencies.

Follow every material local reference and every explicitly identified external
source that is available in the current environment. If a source is missing,
unreadable, stale, only proposed, or lacks the required verification, record
that fact as a gap with its readiness effect. Do not silently omit it or treat
   an initiative assertion, recommendation, unconfirmed assumption, or inaccessible
source as implementation evidence.

For each inventory item, record its precise location, evidence label or
authority, version/date when available, the initiative claim or requirement it
was compared against, the comparison result, and the readiness effect. A source
may support several initiative claims, but do not collapse distinct conflicts
or gates into an untraceable summary. Use source mapping as a starting point;
verify it against the current repository and all initiative records instead of
assuming it is complete or current.

For every implementation step in {phase_or_execution_scope}, distinguish the
accepted specification direction, current product evidence, entry prerequisites, and
release or later-phase evidence. Evidence that justified an earlier limited
phase or a completed artifact does not establish readiness for a different
phase, a broader integration, deployment, or release claim.

Compare the complete inventory against the existing initiative in these areas:

1. Intended outcome, included and excluded scope, product boundaries, and
   ownership.
2. Governing-source precedence, accepted directions, assumption dispositions,
   unresolved questions, and source conflicts.
3. Architecture, interfaces, data ownership, security, compatibility,
   migrations, operations, recovery, rollback, and environmental constraints.
4. Roadmap and implementation-step order, dependencies, owners, phase entry
   criteria, release gates, and acceptance conditions.
5. Current product behavior and artifacts, including whether existing code,
   configuration, tests, and verification results implement, contradict, or
   leave unproven the planned work.

For every mismatch, missing input, unverified claim, stale evidence, or
cross-initiative dependency, state the exact initiative record and evidence
source, their evidence label, why they do not reconcile, the affected phase or step,
whether the gap is blocking, and the owner, decision, artifact, or verification
needed to resolve it. Actual repository evidence can expose an initiative drift;
it does not silently override `evidence/authoritative` or authorize a change to the
initiative.

Use {initiative_template_root}/initiatives/implementation-readiness.md only as the
shape of the review response. Do not copy, create, populate, or update that
document. Under the response's `## Evidence reviewed` section, add a
`### Evidence coverage` table with these columns:

| Evidence source | Standing or state | Initiative record or claim compared | Result | Readiness effect |

Use concise rows with exact links, paths, stable IDs, or precise sections. The
summary table may group related evidence only when the coverage table still
identifies every material source and comparison.

Record a precise, phase-specific disposition:

- **Go** only for work whose required decisions, inputs, owners, boundaries,
  environment, and verification prerequisites are all reconciled and supported
  by current evidence.
- **Conditional or limited go** only when the exact authorized scope and every
  remaining gate are explicit, and no listed condition is required before that
  limited scope can safely begin.
- **No-go, blocked, or deferred** when a required decision, source,
  specification, owner, dependency, environment, or verification gate is
  unresolved, conflicting, or unsupported.

Do not generalize a phase-specific result into a release, deployment,
operational-readiness, or broader implementation claim. Do not mark a phase
implemented merely because its accepted direction is documented.

Do not create, copy, update, move, rename, stage, commit, or delete any file
or directory. In particular, do not create or update
implementation-readiness.md; add a README link; change the proposal,
assumption, architecture, source map, open-question register, roadmap,
implementation steps, status records, other initiative records, product
artifacts, tests, or templates; or begin implementation. When evidence shows
that one of those records needs correction, preserve the evidence in the review
response and report the required follow-up, owner, and blocking effect for a
later, separately scoped action.

Before finishing, verify that every material evidence source in the inventory
was compared, every conclusion cites its evidence, and no initiative or product
file changed during the review.

Report the reviewed scope and disposition; the evidence-coverage count and any
unavailable sources; every ready, conditional, blocked, or deferred phase; all
mismatches and unresolved gates; the exact initiative records that would need
follow-up; and every required owner, decision, artifact, or verification. State
the correlation-verification result and that the review changed no files. Do
not create a separate report file, stage a file, create a commit, or begin
implementation.
~~~

