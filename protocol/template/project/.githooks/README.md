# Project Git hooks

Copy this folder directly. `pre-commit` runs the installed validator and
protected-source guard from the project root. Inspect existing hooks before
reconciling or enabling it with `git config core.hooksPath .githooks`.
Use the project's configured interpreter through `TADP_PYTHON` when needed.
Copying files does not change Git configuration or authorize protected edits.
No record template is needed in this executable-support folder.
