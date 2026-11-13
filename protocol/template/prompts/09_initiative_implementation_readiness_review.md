<!--
Replace every braced placeholder before using this prompt.
-->

# 9. Initiative implementation-readiness review

## Use when reviewing an existing initiative immediately before execution

Use this prompt immediately before an existing `implementation` initiative
begins the reviewed product-execution phase or work set. First prepare any
constructible documentary prerequisites through their owning activities.
Then the readiness assessment gathers and reports current evidence without
creating or updating the initiative, a readiness file or any product artifact.
The assessment compares all material existing evidence
against the initiative's current claims without implementing work, realigning
the initiative, or expanding its scope.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Documentary prerequisites

Use the [canonical coverage and use map](../TEMPLATE-COVERAGE.md) and the
[shared preparation procedure](WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation).
The following metadata is a reference inventory of applicable canonical
record roles, not an action list or authority to create every listed record.
<!-- tadp-prerequisites: {"stage":9,"records":["profile","initial-suite","membership","decision-receipt","acceptance","readiness-response"],"procedure":"WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation"} -->

The executable block below applies these prerequisites to this stage before
its substantive entry check. Existing records and actual events retain their
owners and authority; conditional roles require a cited applicability result.

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
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md and the canonical
prompt keyword specification at evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md.
The following human-response and gate-stop instructions state the ordinary
required path. Apply only specifically authorized, recorded exceptions under
that specification; a mode request alone supplies no waiver. Record effective
settings for each source-position block before dispatch or retry, preserve
locks and truthful evidence, and retain ordinary lifecycle meanings. Preview
work remains response-only; local resource restrictions and independent review
obligations compose with gates. The shared contract and this prompt retain
all unexcepted preconditions, edit boundaries, verification, and reporting.

Before the substantive step, apply documentary prerequisite preparation in
{initiative_template_root}/prompts/WORKFLOW-CONTRACT.md using
{initiative_template_root}/TEMPLATE-COVERAGE.md and this stage's inventory.
Classify and prepare only necessary constructible inputs from sufficient
scoped evidence through their owning stages; then validate and recheck this
step's real entry gates. Disclose preparation changes separately. The edit
limits below govern the substantive activity after this preparation.
Reusable source paths below are relative to {initiative_template_root};
instantiate only at the map's declared project-relative destination.
Required inputs: accepted implementation suite/baseline/receipt, exact phase
plan, current SDK/API results, product/dependency/verification evidence and
initiatives/implementation-readiness.md as response shape only. Use the mapped
initial-suite and decision sources for preceding owning-stage documentary
recovery from actual sufficient evidence. Do not reconstruct passing tests or
human acceptance. Missing identity, wrong type, stale phase evidence, required
verification or authority remains a blocker. Disclose all preparation changes,
then capture a file-state baseline including staged, unstaged and untracked
content before the read-only assessment; verify it is unchanged afterwards.

For a project with the version-scope revision adopted, verify exact scope
membership, originating and contributing suite/note IDs and paths, per-source
routing, current numeric revision cycle, recorded dedicated/shared execution
mode and branch, immutable captured base ref/commit and immediate integration
target. Shared source/scopes and declared shared scope branches are valid;
initiative identities and active per-cycle assignments remain unique. Preserve
historical allocation, closure and branch history. No later-stage repair by
inference is allowed; route inconsistencies to the owning preparation/intake.
After preceding preparation, the readiness assessment remains read-only. It may inspect recorded authority and
exceptions or show proposed records in its response, but it cannot persist
them. Preserve the observed readiness result independently of any separately
authorized permission to perform bounded work under an exception. Waived,
failed, and unperformed checks are not Go evidence.

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

Verify that the exact version scope, realization suite, initiative,
execution branch, captured base branch and commit, reciprocal links, and live
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

Before assessing readiness, verify that:

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

After owning-stage preparation, if the initiative identity remains missing or
ambiguous, or evidence is insufficient to identify the intended work, stop and
report the exact blocker. Do not substitute an inferred initiative or treat
reconstructed documentary inputs as proof that a readiness gate passed.

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

During the readiness assessment, do not create, copy, update, move, rename,
stage, commit or delete any file or directory. In particular, do not create or update
implementation-readiness.md; add a README link; change the proposal,
assumption, architecture, source map, open-question register, roadmap,
implementation steps, status records, other initiative records, product
artifacts, tests, or templates; or begin implementation. When evidence shows
that one of those records needs correction, preserve the evidence in the review
response and report the required follow-up, owner, and blocking effect for a
later, separately scoped action. This assessment boundary begins only after
the preceding preparation changes have been disclosed and its file-state
baseline captured; preparation remains an owning-stage activity.

Before finishing, verify that every material evidence source in the inventory
was compared, every conclusion cites its evidence, and no file changed during
the assessment compared with its post-preparation baseline.

Report the reviewed scope and disposition; the evidence-coverage count and any
unavailable sources; every ready, conditional, blocked, or deferred phase; all
mismatches and unresolved gates; the exact initiative records that would need
follow-up; and every required owner, decision, artifact, or verification. State
the correlation-verification result, every preceding preparation path/change,
and whether the assessment itself changed no files. Never claim the whole
invocation changed no files when preparation did. Do not create a readiness
report file or begin implementation; stage or commit no files during assessment.
~~~

