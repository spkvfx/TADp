# EX-VSG-VER-001: migration verification

**Authority:** [EX-VSG-DR-001](EX-VSG-DR-001-initiative-migration.md)

**Capture date:** 2026-11-12

**Migration baseline:** `9ab8c991222a026277a6f238bd0b64704b97f840`

## Baseline

The initial worktree was clean. `example/tools/tadp_protect.py check example`
passed with zero errors. `example/tools/tadp_validate.py example --json`
passed with zero errors and one TADP033 warning for the original unmigrated
broad realization. Commands used the configured `.venv/Scripts/python.exe`
and a per-process `safe.directory` setting for the enclosing worktree.

## Migration checks

Pending implementation and actual verification; no passing result is implied.
