# Project runtime tools

These files copy directly. Use Python 3.11 or later, Git and the project's
configured interpreter. Run commands from the project Git root. The following
examples are inert until an authorized invocation executes them.

| Command | Effect |
|---|---|
| `python tools/tadp_protect.py check .` | Read-only integrity check: exit 0 passes, 1 reports drift, 2 rejects input. |
| `python tools/tadp_validate.py . --json` | Read-only structural checks: exit 0 has no errors, 1 has findings, 2 rejects input. |
| `python tools/tadp_sync.py --json` | Preview an upstream update, pinned to an actual commit, without project writes. |
| `python tools/tadp_sync.py --ref UPSTREAM_COMMIT --apply` | Apply a reviewed conflict-free update; existing protected changes also need `--authority` naming actual human authorization. |

The keyword tool reads the protected registry. Scope and template modules
supply runtime APIs and objective checks; they do not allocate work or create
decisions. Template checks include folder READMEs and the nonrecursive library
placeholder. Passing structural checks proves no adoption or product claim.

## Preserve project work

Synchronization copies `.template.md` sources unchanged, preserves existing
scaffold files and user work, refuses conflicts, and retains retired files.
It saves managed replacements under `.tadp-sync-backups/`. Keep
`.tadp-sync.json` for content hashes, source revision and authority history.
There is no delete or force option. The complete library is installed once;
its source `project/template/README.md` is only a nonrecursive placeholder.

The payload excludes TADp development reports, decisions, live initiatives,
delivered products and regression fixtures. It installs no test results or
project-specific evidence. No hooks, Git configuration, staging, commits,
merges, pushes or lifecycle events occur automatically.

Apply is not transactional. Avoid concurrent writers. Inspect retained files
and backups after an I/O failure before retrying. Inspect an interrupted run's
`.tadp-sync.lock` before manually reconciling it.

## Authority and verification

Actual project records require the owning workflow and sufficient evidence.
`initialize` and `refresh` require separately authorized source maintenance;
ordinary work uses `check`. Never refresh a lock to hide unexplained drift.
See [validation guidance](../docs/development/validation-and-quality.md) and
[the governing suite](../evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md).
[Project tests](../tests/README.md) arise from actual scoped work; the clean
baseline supplies no TADp regression suite or fictional verification.
