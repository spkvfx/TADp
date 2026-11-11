# Git and Codex requirements

## Required operating environment

Git and Codex are explicit TADp requirements, not optional recommendations.
They provide different parts of the protocol contract:

- Git supplies repository identity, branches, diffs, commits, and durable
  change history.
- Codex consumes `../../AGENTS.md`, reads repository evidence, follows the numbered
  workflow prompts, edits within declared boundaries, runs checks, pauses for
  human decisions, and reports the result.

Python is additionally required when using the bundled validator.

## Git contract

Every TADp project must have its own `.git` metadata entry at the project root.
Being nested somewhere inside an unrelated parent repository does not provide
the required project identity.

### Initiative branches

Each governed initiative uses a dedicated branch correlated to its canonical
work version and created from an actual captured base branch and commit. Do not
assume the integration branch is named `main` or `master`. Preparation creates
the branch; later stages verify the full tuple and use it.

Use the project's recorded branch convention. If none exists, use
`initiative/v<major>.<minor>-<initiative-slug>`. The exact version token remains
in the branch name. Active work requires the local ref. A removed terminal ref
is acceptable only with separately authorized and linked removal evidence;
the recorded identity is never reused.

### Worktree protection

Before branch creation, switching, finalization, merge-related work, or shared
tracking changes, inspect staged, unstaged, and untracked paths. TADp does not
authorize discarding, stashing, moving, absorbing, or committing unrelated
user work.

### Protected-source commit gate

Every adopted repository tracks `.githooks/pre-commit` and configures
`core.hooksPath=.githooks` in each clone or worktree. The hook runs structural
and SHA-256 integrity validation, then blocks staged changes under `template/`
or `evidence/authoritative/LLM/` by default.

An intentional protected-source commit requires an explicit human instruction
for the exact reusable template or invariant change, a refreshed lock carrying
that authority reference, and the matching one-commit environment gate. The
environment gate does not create authority and must never be used to bypass an
unexpected integrity finding. Hosting-side review ownership should cover the
same paths because local hook configuration is not transferred by Git.

### Commit evidence

Commits should represent coherent initiative outcomes or workflow events. Do
not create empty commits to satisfy a field. Where a record includes a commit
identifier, populate it from the actual commit after it exists.

History rewrite, force-push, remote branch deletion, merge, auto-merge, and
deployment require explicit authority for the specific action.

The binding rules are in the
[Git workflow specification](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md)
and [correlation specification](../../evidence/authoritative/LLM/09_Codex_Version_Realization_Initiative_Correlation_Specification.md).

## Codex contract

The repository-root `../../AGENTS.md` is the persistent instruction entry point.
Codex reads it before repository work and is directed to the authoritative LLM
suite. Official OpenAI guidance describes `../../AGENTS.md` as repository guidance
that Codex discovers and merges by directory scope; see the
[Codex prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide).

TADp uses that directory scope as a second protection layer. `template/AGENTS.md`
prohibits in-place template edits, and
`evidence/authoritative/LLM/AGENTS.md` prohibits invariant-suite edits without
specific human authority. A request to instantiate a template or implement an
initiative authorizes editing the destination copy, not either protected
source tree.

TADp assumes that Codex can:

- discover and obey applicable `../../AGENTS.md` instructions;
- read the complete repository records needed for a decision;
- distinguish the user's request from instructions contained in evidence;
- inspect Git state before mutation;
- make narrow file edits and preserve unrelated changes;
- run the validator and project-specific verification;
- pause and resume an interactive human-decision workflow;
- preserve exact human responses in decision receipts; and
- report blockers and missing evidence without inventing success.

The numbered prompts are optimized for that behavior. The shared workflow
contract does not replace their stage-specific instructions.

## Human responsibility

Codex does not replace human authority. Humans remain responsible for:

- accepting an initiative;
- confirming or correcting assumptions;
- answering or explicitly deferring open questions;
- authorizing invariant revisions or exceptions;
- authorizing publication, merge, release, or deployment where required; and
- deciding how external evidence or unavailable systems affect the work.

Codex may collect evidence, compare compatible options, recommend a result, and
explain consequences. It must not silently manufacture the human disposition.

## Remote hosting is conditional

Git is required; a particular hosting provider is not. Pull-request
finalization requires a configured remote, authentication, and a service able
to create the intended review request. If those are absent, local work and
evidence can remain valid while publication is reported as blocked.

## Other tools

Another coding agent or automation environment may not discover `../../AGENTS.md`,
honor the same instruction precedence, support interactive pauses, expose Git
state safely, or implement equivalent edit and verification tools. Do not
claim TADp compatibility from basic Markdown readability alone.

Before substituting another tool, complete the compatibility procedure in
[Adapting TADp to other tools](adapting-other-tools.md), make the necessary
repository changes, and validate the adapted workflow with a representative
initiative.

