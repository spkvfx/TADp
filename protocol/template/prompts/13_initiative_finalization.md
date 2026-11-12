<!--
Replace every braced placeholder before using this prompt.
-->

# 13. Finalize initiative

## Use after an initiative completes its permitted work

Use this prompt after the initiative has completed its accepted type-specific
work and recorded the required verification evidence. For an
`implementation` initiative, that follows the
[implementation-execution prompt](10_initiative_execution.md). A `design`
initiative follows the [design delivery prompt](11_design_delivery.md), and a
`planning` initiative follows the
[planning delivery prompt](12_planning_delivery.md). The prompt verifies the
completion state, commits any remaining accepted work, pushes the initiative
branch, and opens its pull request. It does not declare incomplete work
complete, merge the pull request, delete the branch, deploy a product, or waive
an unresolved gate.

The initiative branch and its base branch come from the
[prepare-initiative prompt](00_initiative_preparation.md). The completion state
recorded by the initiative's type-specific work becomes part of the base branch only when the pull
request merges.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [finalize initiative prompt](13_initiative_finalization.md), finalize
> the attached initiative after its accepted work is complete. Verify its
> aligned completion records, commit any remaining accepted initiative work,
> push the prepared branch, and create the pull request.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Finalize initiative prompt** block below. Do not
execute, recurse into, or derive additional work from the example.

## Finalize initiative prompt

```text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Finalize {initiative} at {initiative_path} from {initiative_branch} into
{base_branch}.

This prompt may run only after the initiative has completed its accepted
type-specific work and all in-scope acceptance, qualification, and release
gates have recorded passing evidence. It must not turn partial, blocked, or
failed work into a completed initiative or a pull request. A separately owned
future production, deployment, or release scope may remain explicitly deferred
when it is outside the completed initiative's accepted claim.

Verify the target's declared type. An `implementation` initiative must have
completed only accepted product work; a `design` initiative must have completed
accepted specification or supporting-evidence work without creating a new
product; and a `planning` initiative must have completed evidence work only.
Do not finalize an initiative whose diff crosses its type boundary.

Apply the ownership and approval convention at {project_profile_path}. Human
owner, reviewer, and approver roles resolve as recorded for the target project.
No technical, evidence, acceptance, or release gate within the accepted
completion claim is waived.

Before changing tracking or Git state, verify that:
- the current branch is exactly {initiative_branch}, it is the branch prepared
  for this initiative, and {base_branch} is the captured branch from which it
  was created;
- the canonical work version, realization suite, initiative ID and path,
  version-bearing branch, captured base branch and commit, and reciprocal links
  match one unique project correlation row;
- {base_branch} exists locally and on the configured pull-request remote, and
  its intended target is unambiguous;
- {initiative_path} has a complete initiative record, completed permitted
  output, and supporting evidence, with no remaining required in-scope delivery
  step, acceptance
  gate, qualification gate, release gate, failed verification, unresolvable
  conflict, deferred item, or blocker; separately deferred follow-up scope is
  explicit and does not contradict the completed claim;
- `{initiative_path}/completion-evidence.md` states the exact completed claim
  and provides evidence for every applicable acceptance and verification gate;
- the completion evidence's cross-initiative coherence review records its
  inventory baseline, every other current open initiative (including Proposed
  and partial effort), affected closed claims, findings, compatible
  dispositions, and links to the project work-conflict register;
- no unresolved work conflict contradicts the completed claim, and the branch
  diff does not refine a closed initiative without a new explicit human
  reopening receipt and legal transition; substantive changes use successors;
- the linked acceptance receipt names the same accepted baseline and exact
  bounded claim, and no later delivery record silently revises that baseline;
- an `implementation` initiative also has an
  `{initiative_path}/execution-record.md` whose ledger, changed paths,
  commands, and results agree with the complete branch diff;
- a `design` or `planning` initiative also has an
  `{initiative_path}/delivery-record.md` whose ledger, outputs, methods,
  verification, and results agree with the complete branch diff;
- every uncommitted or untracked artifact traces to this initiative's permitted
  output or an already-aligned completion record. Identify the exact paths
  and do not stage unrelated work;
- {initiative_status_path} and any applicable parent initiative index are
  available, identify the intended initiative entry, and already reflect the
  verified completed result;
- the configured remote accepts pushes for {initiative_branch}, the pull
  request service is authenticated, and a pull request does not already exist
  from {initiative_branch} into {base_branch}; and
- the pull-request title, summary, delivery-step list, verification
  results, compatibility or migration effects, and recorded completion status
  can be stated from evidence.

If any precondition fails, stop and report the blocker. Do not change a status,
commit, push, create a duplicate pull request, merge, delete a branch, or use a
different target branch.

Verify, but do not re-declare, the completed result recorded before
finalization:
1. Confirm that {initiative_path}/README.md is `Completed`, has the correct
   `Last updated` value, and links the completed scope and verification
   evidence.
2. Confirm that `{initiative_path}/completion-evidence.md` states the same
   completed claim and supplies evidence for every applicable gate. For an
   `implementation` initiative, confirm that `execution-record.md` agrees with
   the complete branch diff and verification results. For a `design` or
   `planning` initiative, confirm that `delivery-record.md` agrees with the
   complete branch diff and verification results.
3. Confirm that the matching {initiative_status_path} row and any applicable
   parent or dependent record state the same verified result, next
   responsibility, and intentionally deferred or unavailable follow-up scope.
4. Confirm that the proposal, accepted specifications, decisions, evidence map,
   roadmap, and delivery steps remain aligned with the completed output and
   were not weakened merely to make the status appear complete.
5. Confirm that the canonical row retains the allocated branch and captured
   base identity, and that any absent historical ref has separately authorized
   removal evidence. Do not delete or free the branch identity in this stage.
6. Confirm the coherence review remains current against open work and affected
   closed claims at finalization. Preserve documented effort and conflict
   history. Return stale or incompatible findings to the owning workflow;
   finalization must not refine another initiative or manufacture reopening.

If a completion or tracking record is missing, stale, inconsistent, or not
supported by completion evidence, stop and return it to the appropriate
type-specific workflow
for reconciliation. Do not repair or manufacture completion state during
finalization, and do not change unrelated status rows or parent scope.

Review the complete branch diff and working tree. Stage only remaining accepted
initiative permitted output, required verification evidence, and already-aligned
tracking records. When staged changes remain, commit them with a clear
initiative-specific message; otherwise use the existing initiative commits and
do not create an empty commit. Do not add credentials, local settings,
generated caches, unrelated user work, or any path not traced to the
initiative.

Push {initiative_branch} to the configured remote and create one non-draft
pull request from {initiative_branch} into {base_branch}. Its title must name
the initiative and completed outcome. Its body must identify:
1. the initiative and accepted scope delivered;
2. delivery steps completed;
3. verification commands and results;
4. compatibility, migration, operational, or rollout effects;
5. the initiative-status records verified and any remaining accepted records
   committed; and
6. remaining in-scope blockers or deferred work, which must be `None`, plus any
   separately owned follow-up scope that remains explicitly unavailable or
   deferred outside the completed initiative claim.

Do not merge the pull request, enable auto-merge, delete {initiative_branch},
or make a deployment.

Report the tracking files verified and any that were committed during
finalization, the commit identifiers, the pushed branch and base branch, the
pull-request URL, the verification evidence summarized in the pull request,
the final correlation verification, and any follow-up that remains after
merge.
```

