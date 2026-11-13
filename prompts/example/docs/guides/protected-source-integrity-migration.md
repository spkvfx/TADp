# Protected-source integrity migration

## Purpose and standing

This guide migrates an existing TADp adoption to the protected-source controls
for reusable templates and the Codex invariant suite. It is procedural
guidance. The authoritative evidence rules continue to determine whether a
source may change, and this guide does not accept an existing local difference
as authoritative.

The protected roots are:

- `template/`, which remains reusable source and must be copied before
  specialization; and
- `evidence/authoritative/LLM/`, which is the binding Codex invariant suite.

## Preconditions

Before changing the adoption:

1. Use a dedicated branch and inspect staged, unstaged, and untracked work.
2. Record the TADp distribution revision from which the repository was adopted,
   when it is known.
3. Compare both protected roots with that distribution and classify every
   difference as an intentional authorized revision, an instantiated record
   stored in the wrong place, or unexplained drift.
4. Obtain an explicit human decision identifying the exact baseline that may be
   locked. Do not infer acceptance from the fact that files already exist.
5. Preserve any prior invariant revision evidence and migration consequences.

If a local invariant conflicts with the governing suite, use the invariant
conflict procedure. If a file under `template/` is actually an instantiated
record, move or recreate it at the proper non-template destination through an
authorized change; do not legitimize the placement by locking it.

## Migration

1. Copy the current root and directory-scoped `../../../../AGENTS.md` instructions,
   `tools/tadp_protect.py`, the updated validator and tests, and
   `../../../../.githooks/pre-commit` from one pinned TADp revision.
2. Ensure the complete reusable template tree is present at `template/` and
   the complete invariant suite is present at
   `evidence/authoritative/LLM/`.
3. Run the ordinary validator. Expected missing-lock findings may remain, but
   resolve every unrelated error before establishing the baseline.
4. Initialize both locks with a durable reference to the human decision:

   ```powershell
   python tools/tadp_protect.py initialize . --authority "<decision record or explicit adoption authority>"
   ```

5. Review both generated `.tadp-lock.json` files. They must identify the
   correct protected root, authority reference, and every source file except
   the lock itself.
6. Activate the tracked hook in the current clone or worktree:

   ```powershell
   git config core.hooksPath .githooks
   ```

7. Configure the same hook setup for future clones and require hosting-side
   owner review for both protected roots and their lock files.
8. Commit the migration as one reviewable baseline change. Because the initial
   commit touches protected paths, use the documented one-commit environment
   gate with the exact authority string stored in the locks.

## Verification

Run all three checks from the adopted TADp root:

```powershell
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
python -m unittest discover -s tests -v
```

Then verify that an ordinary staged edit under either protected root is rejected
without the explicit protected-update gate. Do not leave the gate environment
variables configured after the authorized commit.

A successful migration proves canonical-content agreement with the recorded
locks. UTF-8 line endings are normalized before hashing; binary files are
hashed as stored. The result does not prove that an unidentified local
difference was authorized, that the named human had decision authority, or
that project-specific evidence is correct.
