# Codex Git workflow specification

## Requirement

Every TADp project must be the root of a Git repository. Git history is part of
the traceability record; a copied directory, external change log, or informal
statement is not a substitute.

The repository must identify its actual current and base branches from Git.
Codex must not assume `main`, `master`, a remote, or a hosting service.

## Initiative branches

Every initiative must have one dedicated branch created from a captured base
branch. Preparation owns branch creation and records both names. Later workflow
stages must use that branch and stop if another branch is active.

A branch may contain only work traceable to its initiative, required
verification, and the tracking records that must change with it. Work for a
separately scoped initiative belongs on its own branch.

## Worktree safety

Before creating or switching an initiative branch, rebasing, finalizing,
merging, or changing shared tracking, Codex must inspect the worktree and
identify staged, unstaged, and untracked paths. It must not discard, overwrite,
stash, move, absorb, or commit unrelated user work.

Preparation requires a clean worktree. Finalization must account for every
changed path and stage only initiative-traceable work.

## Commits and history

Commits must be coherent, reviewable, and named for the initiative outcome or
workflow event. Where a protocol record has a commit field, record the actual
identifier after the commit exists. Do not create empty commits merely to
satisfy a template.

Codex must not rewrite shared history, force-push, delete a remote branch,
merge a pull request, or enable automatic merging unless an explicit human
instruction authorizes that specific action. A general request to implement or
finalize an initiative is not authorization for those actions.

## Finalization

Before finalization, the branch diff, lifecycle history, execution record when
applicable, completion evidence, and status records must describe the same
bounded claim. The configured remote and pull-request target must be verified
rather than inferred.

Finalization may commit remaining accepted work, push the initiative branch,
and open one pull request when the prompt and repository configuration authorize
those actions. It must not merge, deploy, or delete the branch.


