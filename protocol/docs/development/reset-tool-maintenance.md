# Local project reset tool maintenance

## Authority and boundary

Captured by Codex on 2026-11-13 from the User's request:

> create a script that resets the project to the protocol template state, removing all user work.

The User then clarified the target:

> no - use the relative position from the tools directory.

> right - that's the TADp project directory. A project might have multiple TADp projects, or might be the repository root.

The implementation targets only the parent of the script's own `tools/`
directory, independently of the current directory or the enclosing Git root.
It adds [the command](../../tools/tadp_reset.py),
[isolated regression tests](../../tests/test_tadp_reset.py) and
[usage documentation](../../tools/README.md#reset-a-tadp-project-to-its-installed-template).
This instruction authorizes creation of the tool, not running a destructive
reset on the live repository. Only previews were run against the live project;
destructive operations were tested in temporary fixture repositories.

No protected-source revision, lock refresh, lifecycle event, adoption, merge,
push or release is performed. The local locked `template/project/` is the
scaffold authority. Installed protected sources remain unchanged, including
the current invariant revision; embedded sources do not replace them. The
reset command itself is retained as an explicit addition to the scaffold.
Existing synchronization behavior and its deployment payload are unchanged;
this standalone tool can be copied beside an installed `tadp_sync.py`.

## Effective settings and Git evidence

The operative request and target clarifications contain no keyword directive.
For the single implementation block the initial settings apply:
`human_gates=true`, `other_gates=true`, `preview=false`, `local=false`,
`review=false`. The target set is the command, its documentation, regression
tests and this maintenance record. No exception is requested or adopted.
Read-only safety review and independent test authoring ran concurrently;
implementation writes were serialized. Retry/resume identity is this request
and its target clarifications. The read-only reviewer identified preserved-path
collisions, relocated Git metadata and directory drift; these were reconciled
in preflight and verification checks before final testing.

The captured Git baseline is `54743ec47a3668088b00d5e290d8fbad5d3b57b7` on
branch `v1`. Existing unstaged deletions under `_old/example/` were present
before work began and were preserved. They prevent a clean-worktree branch
creation; no switch, stash or absorption of those deletions is performed.
Only this bounded maintenance's files are eligible for its commit. Git history
of this record identifies the actual maintenance commit; no future hash is
asserted here.

## Safety and evidence limits

Apply requires explicit matching project-path confirmation and a new external
backup outside the entire enclosing Git worktree and its metadata. Before any
deletion the backup records non-retained file bytes and an inventory with
hashes, modes and empty directories. Git metadata and locked sources remain
at their original paths. Links, junctions, hardlinks, nested repositories,
unsafe/colliding names, protected drift, a running interpreter in the target,
and unsuitable backup locations block apply. Concurrent changes are checked
before and after backup and at removal; unexpected paths fail verification.
The command uses individual file removal and empty-directory removal, never
recursive deletion. I/O failure can leave partial changes; verified backups
are retained and no automatic rollback overwrites later edits.

Git history, refs, index and configuration are preserved, including when
multiple TADp projects share the enclosing repository. Working-tree reset is
not a lifecycle transition and makes no acceptance, completion or adoption
claim. A post-reset scaffold still requires actual project records through
their owning workflows.

## Verification

- Live preview selected `protocol/` from the script location without applying
  its removal plan.
- Protection check: both source locks match, zero errors.
- Reset regression tests exercise actual temporary Git repositories, backups,
  ignored/untracked work, preserved staged index/refs, nested-project isolation,
  protected drift, file/directory collisions, real Windows junctions and I/O
  failures. A symlink case requires Windows privileges unavailable here and
  is explicitly skipped.
  Final run: 27 tests, 26 passed and one skipped; this includes restoration from
  the complete actual locked scaffold and refusal to remove the running local
  interpreter. The real Windows junction case passed.
- Repository validation reports two existing `TADP002` links from the unchanged
  correlation initiative to the absent old `example/` tree, plus the existing
  deferred legacy-adoption warning `TADP033`. This maintenance does not change
  those claims or restore the removed example. Validation is not claimed to
  pass.

Checks can be reproduced with the commands in the tools README and `unittest`
discovery for `test_tadp_reset.py` under `protocol/tests/`.
