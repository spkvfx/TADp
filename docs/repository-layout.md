# Repository layout

Resolve `R` as the actual enclosing Git worktree, using
`git rev-parse --show-toplevel`. Folder names do not identify a second Git
repository or enlarge a prompt's file authority.

```text
R/
|-- AGENTS.md                 enclosing repository instructions
|-- README.md                 adoption and contribution entry point
|-- docs/                     repository explanations (this directory)
|-- prompts/                  repository maintenance prompts and instructions
|-- TADp/                     P: installed, adopted development project
|   |-- project-profile.md    project ownership/adoption and boundaries
|   |-- decisions/            actual human decisions
|   |-- evidence/             governing baseline and contextual evidence
|   |-- initiatives/          canonical scopes, membership and lifecycle
|   |-- products/             product records
|   |-- docs/                 project guides and local development workflow
|   |-- prompts/              project-local boundary remains unchanged
|   |-- protocol/             C: candidate workspace, not another installation
|   `-- template/             D: protected installed reusable library
`-- protocol/                 U: implementation-ready distribution
    |-- README.md             portable overview
    |-- docs/                 portable adoption and operation
    |-- tools/ and tests/     runtime checks and distribution regressions
    `-- template/             S: protected upstream reusable library
```

Root `.gitignore`, `.gitattributes`, `.githooks/` and editor configuration are
repository support files. This documentation change alters none of them.
Git refs, index, worktree and hook configuration are shared. No nested `.git`
directory is needed for P. The older root hook still expects a local `example/`
tree; executable repair is outside this documentation task. Do not enable it
as a side effect of copying files or reading a guide.

Root `prompts/` is distinct from P's project-local `prompts/` and the protected
numbered workflow at `template/prompts/`. An explicit invocation of a root
maintenance prompt authorizes its exact named target only. Changing cwd or
copying a prompt does not confer that authority on a project-local prompt.

The project [profile](../TADp/project-profile.md) owns local appointments,
adoption and integration conventions. The current repository-owner role
includes the respective owner in a fork; an adopter does not inherit these
appointments. P's records, receipts, manifests, verification and completion
history remain there. Repository documentation is explanatory.

For an adopting project's record tree, see the portable
[project layout guide](../protocol/docs/development/repository-layout.md).
The supplied example lives in a [separate repository](https://github.com/spkvfx/TADp-example).
No example synchronization, parity or adoption follows from this layout.
