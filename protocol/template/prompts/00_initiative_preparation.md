<!--
Replace every braced placeholder before using this prompt.
-->

# 0. Prepare correlated initiative

## Use before proposal creation

Use this prompt to preflight and allocate one canonical work version, one
realization suite, one self-contained initiative identity, and one dedicated
version-bearing Git branch. On that branch it creates the suite index and
initial realization note, canonical project correlation row, reciprocal
metadata, and smallest initiative README skeleton as one preparation unit.

Run it before the [proposal-creation prompt](01_proposal_creation.md). It
creates no proposal, assumption or question disposition, acceptance, delivery
output, completion claim, or product artifact. A pre-effective initiative uses
its recorded migration-ledger workflow instead of this new-allocation prompt.

If no parent initiative is supplied, the initiative belongs to `root`. Set
`{parent_initiative_or_root}` to `root` and place it at
`{initiative_registry_root}/{initiative_type}/{initiative_slug}`. Do not infer
a parent from a similar name, version, or nearby directory.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [initiative preparation prompt](00_initiative_preparation.md),
> prepare the attached initiative's correlated work version, realization
> suite, canonical row, branch, and minimum README skeleton.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Prepare initiative prompt** block below. Do not
execute, recurse into, or derive additional work from the example.

## Prepare initiative prompt

```text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Prepare canonical work version {work_version}, realization suite
{realization_suite_id} at {realization_suite_path}, and the
{initiative_type} initiative {initiative_id} named {initiative} at
{initiative_path} as a member of {parent_initiative_or_root}.
{initiative_type} must be exactly `implementation`, `design`, or `planning`.
The tuple is new and owns one narrow outcome and acceptance claim.

Use the currently checked-out branch as the source branch. Capture its exact
name as {base_branch} and its current commit as {base_commit}. Apply the branch
convention in {project_profile_path}. If none is recorded, use
initiative/{work_version}-{initiative_slug}. The exact {work_version} token
must appear in {initiative_branch}; {initiative_branch} is the new branch to
create, not an existing branch to reuse.

If no parent is provided, set {parent_initiative_or_root} to `root` and use the
project's type directory for {initiative_path}. If a parent is provided, verify
the exact parent requirement and intended member location. The parent does not
share this tuple and must not absorb this initiative's acceptance claim.

Before writing, perform one read-only preflight and verify that:
- this is a Git repository with a checked-out source branch captured exactly as
  {base_branch} at {base_commit}; do not assume a default branch;
- the worktree is clean, including untracked paths;
- {project_profile_path} records the correlation-revision effective commit,
  branch convention, and migration-ledger location;
- {work_version} has canonical `v<major>.<minor>` syntax and is unused in the
  project initiative index, realization hierarchy, initiative records, local
  branch refs, and retained historical identities;
- {realization_suite_id}, {realization_suite_path}, {initiative_id},
  {initiative_path}, and {initiative_branch} are unused and unambiguous;
- {realization_source} is readable, preserves its original identity and
  limitations, and supports only the single narrow suite boundary;
- {initiative_registry_path} exists, owns the canonical initiative and
  correlation register, and has no partial or conflicting row;
- the initiative, proposal-source, realization-note, and suite-index
  preparation templates exist at their declared locations; and
- the proposed outcome passes the narrow-scope cohesion test without a
  mandatory split.

If any precondition fails, stop and report every blocker. Do not allocate a
partial tuple; normalize or infer a legacy mapping; reuse or silently renumber
a version; reuse a suite, initiative, or branch; guess a base; create a parent;
stash or move unrelated work; or write a record merely to clear validation.

Create {initiative_branch} from {base_commit} on {base_branch} and switch to
it. Preserve the source branch and do not query, create, or change a remote
branch during preparation.

On {initiative_branch}, create only this preparation unit:
1. {realization_suite_path} and its `00-...-suite-index.md`, instantiated from
   the realization-suite-index template with the exact work version, suite,
   initiative, branch, captured base, boundary, evidence standing, catalog,
   canonical-row link, and lifecycle navigation;
2. one initial realization note at {realization_note_path}, instantiated from
   the realization-note template and faithfully preserving
   {realization_source}, uncertainty, and non-authoritative standing;
3. {initiative_path} and {initiative_path}/proposal;
4. {initiative_path}/README.md, instantiated from
   initiatives/preparation-README.template.md;
5. {initiative_path}/proposal/README.md, instantiated from
   initiatives/proposal/preparation-README.template.md; and
6. one row in {initiative_registry_path} containing the same work version,
   suite ID and path, initiative ID, type and path, branch, captured base branch
   and commit, predecessor or successor relationship, `Proposed` lifecycle
   evidence, branch-removal evidence state, owner, and next gate.

Replace every template token in the created files. Make every reciprocal link
resolve. The canonical index row owns project-level correlation; the suite and
README copies link to it and do not create status or authority.

Do not create proposal/proposal.md, assumption.md, scope-assessment.md,
architecture.md, source-mapping.md, open-questions.md,
implementation-roadmap.md, implementation-steps.md,
implementation-readiness.md, execution-record.md, delivery-record.md,
completion-evidence.md, a portfolio status entry, code, tests, configuration,
or any other artifact.

Review the diff. Stage and commit only the suite index, realization note,
canonical row, and two prepared README files with a clear preparation message.
Record the resulting preparation commit in the created lifecycle and
correlation evidence when available. Do not push or open a pull request.

Report the exact work version, suite ID and path, initiative ID and path,
branch, captured base branch and commit, parent-or-root placement, canonical
row, files created, reciprocal-link verification, and preparation commit.
State the proposal-creation prompt as the next stage on the same branch.
```
