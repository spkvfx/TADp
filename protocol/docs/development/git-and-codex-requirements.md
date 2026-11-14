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

The project root is its resolved scaffold installation directory `P`, contained
in a valid Git worktree rooted at `G`. `P` may equal `G` or be nested
beneath it. Git supplies identity and history without expanding the project
file boundary; a separate `.git` entry at `P` is unnecessary. Linked
worktrees with a `.git` file are supported. See the
[owning definition](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement)
and [prospective adoption guide](../guides/project-root-installation-migration.md).
The reference distribution at `protocol/` is checked against enclosing Git
without becoming an adopted live project by shape or installation alone.

Map project paths through the verified `P`-relative-to-`G` prefix for Git
history, staging and commits. Refs, index, worktree state and hook configuration
are shared across projects. Preserve existing branch rules and detect
incompatible roles; a nested project has no independent namespace. Necessary
metadata operations for authorized commits do not authorize outside-project
file changes or commits. Preserve parent and sibling work.

### Initiative and scope branches

Discover the actual configured integration base. Major `vN` branches come from
its captured tip, minor `vN.M` branches directly from matching majors, and patch
`vN.M.P` branches directly from matching minors. Siblings never create the next
minor. Capture immutable creation bases and retain branch-role history.

Record one active execution assignment per initiative revision: directly on its
matching scope branch or on `initiative/<scope>-<id-and-slug>` from that scope.
Preflight existing role, work, parent, clean worktree and reciprocal records.
Shared scopes retain per-member paths, commits and verification; serialize
shared writes and preserve concurrent index additions. Dedicated branches host
only their bounded initiative. Historical refs are not reassigned to unrelated
work; separately authorized removal retains identity and evidence.

Closure integrates the closed child into its immediate recorded parent after
all gates pass. A close/finalize instruction for an identified governed unit
supplies only that bounded local merge authority. Direct scope hosting records
presence without self-merge. Scope closure requires its own complete inventory,
closed descendants, child integration, aggregate checks and authority; no
premature upward merge or unaccepted shared work is permitted. Retain actual
tips, method, resulting commit, failure/pending state and post-integration checks.
Pull requests are independently human managed; pushes remain separately authorized.
See [scope migration and operation](../guides/version-scope-migration.md).

### Worktree protection

Before branch creation, switching, finalization, merge-related work, or shared
tracking changes, inspect staged, unstaged, and untracked paths. TADp does not
authorize discarding, stashing, moving, absorbing, or committing unrelated
user work.

### Protected-source commit gate

Every adopted project tracks `.githooks/pre-commit`. Inspect the enclosing
worktree's existing hooks and coordinate a dispatcher before explicitly
configuring one shared `core.hooksPath`. Paths are relative to `G`: use
`.githooks` for `P=G` or, for example, `projects/widget/.githooks` for a
nested project. Copying files never enables hooks or overwrites parent hooks.
The hook runs structural
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

History rewrite, force-push, remote branch deletion and deployment require
separate specific authority. Local child-to-recorded-parent integration uses
the captured close/finalize instruction and satisfied closure gates described
above; it does not authorize a push or further upward integration.

The binding rules are in the
[Git workflow specification](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md)
and [correlation specification](../../evidence/authoritative/LLM/09_Codex_Version_Realization_Initiative_Correlation_Specification.md).

## Codex contract

The project-root `../../AGENTS.md` is the persistent instruction entry point; parent instructions remain applicable.
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

The [keyword contract](../../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md)
also applies to ordinary requests: compute settings by source position,
preserve inert evidence and examples, and distinguish a requested gate setting
from authority to except a rule. See the
[operating summary](../guides/prompt-keywords-migration.md#operating-summary).
Every workflow prompt now prepares constructible documentary prerequisites
through their owning stages before rechecking substantive entry gates; the
[recovery guide](../guides/template-prerequisites-migration.md) explains the
boundary and Stage 9's separately read-only assessment.

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

Git is required; a particular hosting provider is not. Local finalization and
child-to-parent integration need no remote or PR service. Humans independently
manage pull requests. Pushes need separate authority; report an external remote
policy without bypassing it or creating a PR automatically.

The installed Stage 5 and 6 prompt endings still request an unconditional
push. This known consumer contradiction is recorded as `INV-CONFLICT-002` in
the [invariant conflict register](../../evidence/authoritative/LLM/03_Codex_Invariant_Conflict_Register.md).
Those clauses do not supply the required separate remote authority. Correcting
the protected sources needs specific maintenance authorization; this guide
does not certify them as reconciled.

## Other tools

Another coding agent or automation environment may not discover `../../AGENTS.md`,
honor the same instruction precedence, support interactive pauses, expose Git
state safely, or implement equivalent edit and verification tools. Do not
claim TADp compatibility from basic Markdown readability alone.

Before substituting another tool, complete the compatibility procedure in
[Adapting TADp to other tools](adapting-other-tools.md), make the necessary
repository changes, and validate the adapted workflow with a representative
initiative.

