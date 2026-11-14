# Getting started with the project baseline

Use the [project README](../../README.md) to install this baseline into selected
project root `P` inside a valid Git worktree. `P` may equal Git root `G`
or lie beneath it under [specification 05](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement).
Use Git, Codex and the project's configured Python interpreter.
Select an immutable distribution revision; copying files does not adopt it.

## Install the baseline

Copy template/project/ directly, retaining .template.md sources. Install the
complete outer template/ library once at the target template/ path, replacing
the source placeholder conceptually rather than nesting the library inside
itself. Keep the suite, tools and library at the same reviewed revision.
Preserve existing instructions, files, hooks and user work.

Sync selects an existing `--target DIRECTORY` or the exact current directory.
It reports absolute project and Git roots. An unidentified/uninstalled default
cwd beneath an installed project is rejected as ambiguous; explicit selection
can identify an independent installation. A verified installed nested project
remains a valid default. Files, state, backups and locks stay under `P`. See the
[root adoption guide](../guides/project-root-installation-migration.md).

## Establish project records

Create project-profile.md from its source only with actual ownership and
authority. Establish required evidence and coordination records through the
[canonical coverage map](../../template/TEMPLATE-COVERAGE.md).
Do not copy another project's decisions, conflicts, initiatives, products or
verification into the new project. Templates contain shapes, not events.

## First verification

From the project installation root, use the configured interpreter to run the inert
example commands below:

~~~text
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
~~~

Review findings before explicitly enabling .githooks. Passing structural checks
does not establish adoption, acceptance or product correctness. Existing work
uses its recorded revision until authorized migration; consult the applicable
[operation and migration guides](../guides/README.md).
