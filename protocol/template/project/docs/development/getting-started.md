# Getting started with the project baseline

Use the [project README](../../README.md) to install this baseline into its own
Git root. Use Git, Codex and the project's configured Python interpreter.
Select an immutable distribution revision; copying files does not adopt it.

## Install the baseline

Copy template/project/ directly, retaining .template.md sources. Install the
complete outer template/ library once at the target template/ path, replacing
the source placeholder conceptually rather than nesting the library inside
itself. Keep the suite, tools and library at the same reviewed revision.
Preserve existing instructions, files, hooks and user work.

## Establish project records

Create project-profile.md from its source only with actual ownership and
authority. Establish required evidence and coordination records through the
[canonical coverage map](../../template/TEMPLATE-COVERAGE.md).
Do not copy another project's decisions, conflicts, initiatives, products or
verification into the new project. Templates contain shapes, not events.

## First verification

From the target Git root, use the configured interpreter to run the inert
example commands below:

~~~text
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
~~~

Review findings before explicitly enabling .githooks. Passing structural checks
does not establish adoption, acceptance or product correctness. Existing work
uses its recorded revision until authorized migration; consult the applicable
[operation and migration guides](../guides/README.md).
