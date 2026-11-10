<!--
Replace every braced placeholder before using this prompt.
-->

# 0. Prepare initiative

## Use before proposal creation

Use this prompt to give either a new or an existing initiative its own Git
branch and, only when needed, the smallest standard initiative skeleton. Run it
before the [proposal-creation prompt](01_proposal_creation.md) for a new
initiative, or use it to adopt an existing initiative onto its own branch. It
creates no proposal, initiative record, status entry, or product artifact.

If no parent initiative is supplied, the initiative belongs to `root`. In that
case, set `{parent_initiative_or_root}` to `root` and place it at
`{initiative_registry_root}/{initiative_slug}`. Do not infer a parent from a
similar name or nearby directory.

The preparation skeleton consists only of the initiative root
`../../../README.md` and its proposal-source `proposal/README.md`, copied from the
shared [initiative templates](../initiatives/README.md). Later prompts fill
those files in and create the remaining initiative artifacts.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [initiative preparation prompt](00_initiative_preparation.md),
> prepare the attached initiative on its own branch. Create only the minimum
> initiative and proposal-source README skeleton.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Prepare initiative prompt** block below. Do not
execute, recurse into, or derive additional work from the example.

## Prepare initiative prompt

```text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Prepare the {initiative_type} initiative named {initiative} as a member of
{parent_initiative_or_root}, at {initiative_path}. The target may be new or an
existing initiative. {initiative_type} must be exactly `implementation`,
`design`, or `planning`; retain this prompt's stated target and edit
boundaries.

Use the currently checked-out branch as the source branch. Capture it as
{base_branch}. If {initiative_branch} is absent or blank, set it to
{initiative_slug}; otherwise use the supplied {initiative_branch}. In either
case, {initiative_branch} is the new branch to create, not a branch that must
already exist.

If no parent is provided, treat the initiative as a root initiative: set
{parent_initiative_or_root} to root and set {initiative_path} to
{initiative_registry_root}/{initiative_slug}. If a parent is provided, verify
that it is the intended existing initiative and that {initiative_path} is its
intended direct member location. Do not infer or create a parent.

Before making any change, verify that:
- this is a Git repository with a checked-out source branch captured as
  {base_branch}; do not assume `main`, `master`, or another default;
- the Git worktree is clean, including untracked files;
- the new target branch name {initiative_branch} is unused locally; its
  absence is expected and permits its creation. Do not query, create, or
  otherwise change a remote branch during preparation; a later push handles
  publication;
- {initiative_path} is either absent or identifies the intended existing
  initiative; inventory every existing target path before creating anything;
- {initiative_template_root}/initiatives/README.md and
  {initiative_template_root}/initiatives/proposal/README.md exist; and
- the initiative name, type, slug, target path, parent-or-root placement, and
  target branch name are unambiguous.

If any precondition fails, stop and report the blocker. Do not switch branches,
reuse a branch, overwrite or repair an existing target, stash or move unrelated
work, create a parent, or guess a base branch.

Create {initiative_branch} from the current HEAD on {base_branch} and switch
to it. Preserve {base_branch} and do not commit to it. Do not report the absent
target branch as a blocker: create it after the checks pass.

For a new target, create only:
1. the {initiative_path} directory;
2. the {initiative_path}/proposal directory;
3. {initiative_path}/README.md, copied from
   {initiative_template_root}/initiatives/README.md; and
4. {initiative_path}/proposal/README.md, copied from
   {initiative_template_root}/initiatives/proposal/README.md.

For an existing target, preserve every existing directory and file exactly as
it is. Do not create, copy, overwrite, rename, move, or delete an existing
document or directory. Create only a missing part of the two-directory,
two-README skeleton when doing so is unambiguous and does not change an
existing initiative record; otherwise stop and report the structural gap.

Leave template placeholders and instructional comments in newly copied README
files for the later creation prompts. Do not create proposal/proposal.md,
assumption.md, architecture.md, source-mapping.md, open-questions.md,
implementation-roadmap.md, implementation-steps.md,
implementation-readiness.md, a status entry, a parent index entry, a
supporting report, code, tests, configuration, or any other file.

If this preparation created README files, review the staged diff and commit only
those new README files with a clear preparation message. If the initiative was
already structurally complete, create no documentation commit. Do not push the
branch or open a pull request.

Report the exact branch and captured base branch, parent-or-root placement,
whether the initiative was new or existing, every directory and README created
or preserved, and any preparation commit. State the appropriate next prompt on
the same branch.
```

