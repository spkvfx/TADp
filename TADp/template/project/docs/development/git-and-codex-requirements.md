# Git and Codex requirements

TADp requires Git and Codex. Project root `P` is the scaffold installation
directory, contained in a valid Git worktree rooted at `G`. `P` may equal
`G` or lie beneath it; no separate `.git` entry is required at nested `P`.
Linked-worktree `.git` files are supported. Read project AGENTS.md, parent
instructions and the applicable governing suite before work. Discover actual
branches and integration configuration; assume no default branch or remote.
See [root adoption](../guides/project-root-installation-migration.md).

Git paths use the verified `P`-relative-to-`G` prefix. Refs, index, worktree
state and hook configuration are shared. Detect incompatible branch roles
without inventing independent project namespaces. Necessary metadata operations
for an authorized commit do not permit outside-project file changes or commits.

Inspect staged, unstaged and untracked work before Git mutation. Preserve
unrelated work and record actual bases, scope membership and execution
assignment when the adopted workflow requires them. Use traceable commits.
A branch, merge or filename proves no acceptance or completion.

The installed .githooks files copy directly but are not enabled by copying.
Inspect existing configuration at `G` and coordinate a shared dispatcher
before explicit activation. Hook paths are relative to `G`; a nested project
includes its prefix. Never overwrite or enable parent hooks implicitly.
Set TADP_PYTHON to the configured interpreter where needed.

Local integration, branch deletion, pushes, releases and deployment retain
their distinct authority. The [Git workflow specification](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md)
governs exact placement and closure; project documentation supplies no waiver.

Other tools require the compatibility assessment described in
[Adapting other tools](adapting-other-tools.md).
