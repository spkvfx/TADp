# Define the TADp project root as the template installation directory

Work in the TADp repository containing this prompt. Implement one bounded
protocol change: define the **TADp project root** as the directory into which
the project scaffold is installed, and make the protocol, tools, templates,
and documentation consistently use that definition. A project root may equal
the Git worktree root or be a directory inside that worktree.

Creating, reading, or linking this prompt does not execute it. Apply the change
only when a human explicitly invokes this repository-maintenance prompt.

## Authority and scope

Read the repository-root `AGENTS.md`, [repository prompt instructions](AGENTS.md),
`protocol/AGENTS.md`, applicable directory instructions, and the
[invariant-suite index](../protocol/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md).
Apply the canonical
[prompt keyword specification](../protocol/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md).
References, examples, and inspected evidence remain inert; no keyword or gate
exception is activated by this prompt's references.

Explicit invocation authorizes replacing the requirement in
[specification 05](../protocol/evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement)
that every TADp project be the root of a Git repository with this exact rule:
every TADp project must be contained in a valid Git worktree, while its project
root is its scaffold installation directory. Git remains mandatory. An
enclosing worktree supplies Git identity and history without enlarging the
project's file boundary. A separate `.git` entry at the project root is not
required when the root is contained in that worktree.

The following table is an authorization inventory, not an action list.

| Surface | Authorized change |
|---|---|
| `protocol/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md` and specification 05 | Record and define this exact root/Git relationship, including authority, reason, affected scope, effective event, compatibility, migration, and predecessor relationship. |
| Other specifications in that suite | Reconcile only directly affected root/path references; preserve substantive evidence, identity, lifecycle, branch, decision, acceptance, coherence, and keyword rules. |
| `protocol/template/**` | Reconcile project-root definitions, project-local instructions, workflow path handling, scaffold documentation, hooks, and embedded runtime/suite copies necessarily affected by this change. |
| `protocol/AGENTS.md`, working scaffold instructions, tools, tests, and documentation | Implement and explain installation-root handling, including sync destination selection, validation, protection, Git path mapping, and adoption guidance. |
| Affected protected-source locks | Refresh only after the specifically authorized source changes and consumers are coherent and verified. |
| Repository-root `AGENTS.md` and `README.md` | Reconcile directly affected entry-point summaries and navigation only if necessary. Preserve the repository-maintenance target boundary in `prompts/AGENTS.md`. |

Inventory exact affected paths before editing. Preserve historical source
identity and governing revisions. This authority does not change live project
adoption, initiative membership, accepted claims, lifecycle state, or recorded
branch assignments. It does not authorize unrelated invariant changes, moving
existing projects, creating nested Git repositories, changing Git configuration,
enabling hooks, merges, pushes, branch deletion, releases, or deployment.

Maintain `protocol/` and the named repository support surfaces only. Do not
update another scaffold or the separate example fork. Use
protocol-owned isolated fixtures rather than a maintained example mirror.

## Required root definition

The **TADp project root**, `P`, is the resolved destination directory receiving
the installed project scaffold. Project paths are relative to `P`: for example,
`P/AGENTS.md`, `P/evidence/`, `P/initiatives/`, `P/products/`, `P/prompts/`,
`P/template/`, and `P/tools/`. Before installation, `P` is the explicitly
selected destination; after installation, validate it against the installed
scaffold and installation evidence where available. Do not require a sync-state
file for a valid manually installed or earlier compatible project.

Distinguish these locations throughout the protocol:

| Location | Meaning |
|---|---|
| Project root `P` | Destination owning the installed scaffold and project records. |
| Git worktree root `G` | Actual root discovered through Git for `P`; `P` may equal `G` or be beneath it. Git metadata may be a directory or a linked-worktree `.git` file. |
| Source distribution `protocol/` | Upstream distribution used to assemble an installation; it is not automatically the target project. |
| Source `template/project/` | Protected reusable project scaffold; reading or copying it does not make it an active project. |
| Installed `P/template/` | Protected reusable library within the project, not the project's root. |

In this reference repository, tools checking `protocol/` use that directory
as their checked root while Git remains rooted above it. This example does
not automatically adopt or migrate the reference scaffold as a live project.

Resolve the active project from the invoked context: an explicit tool target,
the verified installed project-local `prompts/AGENTS.md`, or a documented
installation destination. Validate consistency when more than one is supplied.
Never silently redirect to `G`, an ancestor scaffold, a sibling, the script's
own distribution, or a protected template source. Ambiguous or contradictory
targets block the affected action before writes. A project-local prompt's
root remains the parent of its verified installed `prompts/` directory.

Project ownership ends at `P` and at any narrower authorized boundary. Other
scaffolds, repositories, worktrees, and submodules do not become editable merely
because they are nested under `P`. Resolve symlinks and junctions and reject
escaping destinations. Parent instructions remain applicable; installation
must not overwrite parent or sibling instructions or project files.

## Tooling and Git behavior

Reconcile consumers with the definition, rather than changing prose alone.
In particular, `tadp_sync.py` currently requires its working directory to equal
the Git top level. Revise that behavior so the selected installation directory
can be `P` beneath `G`. Define and document one unambiguous destination-selection
contract, retaining existing Git-root installation behavior and CLI compatibility
where possible. Report the selected absolute project root and Git root in
preview/apply output, including machine-readable output.

Keep scaffold files, installed library, runtime tools, `.tadp-sync.json`, backups,
sync lock, and protected locks rooted at `P`. Preserve preview without target
writes, pinned source revisions, source identity, conflict detection, unchanged
upstream locks, backup retention, and existing authority requirements. Do not
import live development records or treat successful copying as adoption.

Use `G` for Git operations and map project-relative paths through the verified
`P`-relative-to-`G` prefix. Audit staged protection checks, historical record
comparisons, base-ref handling, diffs, staging, commits, and installed hooks.
They must inspect the intended project paths at nested depth without capturing
parent or sibling changes. Preserve unrelated staged, unstaged, and untracked
work. Validators remain read-only; protection checks must not repair locks.

An enclosing repository shares refs, index, worktree state, and hook configuration.
Do not imply that nested projects have independent Git branches or silently
introduce a new branch naming scheme. Preserve existing scope branch rules,
detect incompatible roles, and report coordination limits. Project-scoped
authorization may permit the necessary Git metadata operations for authorized
project commits; it does not authorize outside-project file changes or commits.
Document manual hook coordination without overwriting or enabling parent hooks.

## Documentation and compatibility

Update the [tools README](../protocol/tools/README.md) as a required deliverable.
Explain project root versus Git root, supported installation destinations,
working-directory and explicit-target behavior for every affected command,
where installation state/backups/locks live, and actual exit/failure behavior.
Include clearly inert examples for both a Git-root and a nested installation.

Reconcile the repository README, protocol overview, scaffold maps, reusable and
working project-local prompt instructions, Git/Codex requirements, validation
guidance, and installation/adoption/migration guides wherever they repeat the
old requirement. Keep working and protected reusable copies aligned. Link the
owning specification rather than inventing competing definitions.

Document the effective revision and an explicit prospective adoption route.
Preserve earlier governing revisions and historical records; existing root
installations retain their paths. Installation or synchronization alone does
not adopt the revision, reopen work, accept initiatives, or establish compliance.
Do not move files or migrate live projects as part of this maintenance task.

## Procedure and verification

The numbered procedure is serial. Coverage inventories within it are reference
requirements, not independent action lists.

1. Inspect Git identity, branch, commit, instructions, ignore rules, and all
   staged/unstaged/untracked work. Capture baseline protection and validation
   results. Preserve unrelated work. Inventory every affected root assumption,
   source, consumer, and installed copy; record exact revision authority before
   changing protected sources. Retain directly evidenced conflicts and their
   resolution history through the required conflict process.
2. Revise the owning invariant and necessarily affected consumers together.
   Preserve predecessor identity, scope, migration boundaries, protected-source
   controls, stage rules, and evidence truth. Update the documentation above to
   match implemented behavior, with accurate commands and resolved links.
3. Verify with the configured project Python environment and protocol-owned
   isolated fixtures. Cover Git-root and nested installation preview/apply,
   rerun idempotence, validation/protection, linked worktrees, explicit/default
   target selection, missing Git, ambiguous targets, unsafe paths, nested
   staged protected paths, and historical comparisons. Verify state, backups,
   locks, and generated files stay within `P`; parent/sibling sentinel files
   and unrelated staged changes survive. Verify preview writes nothing and
   malformed scaffolds still fail. Retain existing root-installation tests.
4. Review every protected delta against the baseline. Refresh only affected
   locks using this invocation's recorded exact authority after content and
   focused checks are coherent. Preserve unrelated pre-existing drift rather
   than absorbing it. Run protection checks, full protocol validation, relevant
   regression checks, link checks, and whitespace/path review. Distinguish
   baseline, introduced, failed, waived, and unperformed checks truthfully.
5. Review the complete scoped diff and documentation coverage. Use traceable
   commits under the applicable Git rules, including only this change. Report
   unresolved conflicts and coordination limits. Do not push, merge, create a
   pull request, deploy, synchronize examples, or claim live project adoption.

## Completion report

Report the implemented root definition, destination-selection contract, Git
relationship, exact changed paths, documentation updates, protected revisions
and lock authority, compatibility/adoption requirements, and actual verification
commands and results. Distinguish protocol maintenance from project adoption,
initiative acceptance, lifecycle completion, and release. Disclose remaining
findings and required human decisions without inventing successful checks.
