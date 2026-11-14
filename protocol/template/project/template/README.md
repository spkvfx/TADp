# Complete reusable template library

Every installed TADp project keeps the complete distribution's `template/`
library at this path, including its protection instructions, lock, coverage
map, workflow prompts and project baseline. Install that library once from the
same pinned revision as the project's runtime suite and tools.

This source folder deliberately contains only this README. Embedding the
library here would recursively embed `project/template/project/template/`.
The installer resolves this placeholder to the complete outer library; it
preserves that library's own README rather than replacing it with this note.
Do not populate this placeholder in the distribution.

Files named `*.template.md` are record shapes: copy a selected source to its
declared destination, remove `.template` from the instance filename, and
populate it only from sufficient evidence through the owning workflow stage.
Other baseline files copy directly, including their original names. Keep
reusable sources intact and preserve existing project work during updates.

Installing the library does not adopt a protocol revision or create project
decisions, initiative acceptance, delivery or completion evidence.
