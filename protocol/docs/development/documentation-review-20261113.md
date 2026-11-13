# Documentation review, 2026-11-13

## Scope and evidence

The User's item 3 invokes `prompts/update-documentation.md` after item 2.
Item 1 supplied both example URLs and was committed as `7cc3ddf`; item 2's
template/prerequisite revision was committed as
`f1f7df6710d247a4f0c4e4fd154981c31595ea8f` before this review began.
The branch remains `maintenance/template-prerequisites-docs-20261113`.
The scoped documentation baseline was clean. Unrelated `_old/example/`
deletions were preserved outside the staged work; `.gitignore` was unchanged.

No operative keyword or exception is used. The item-3 settings remain
human/other gates required, preview/local/review off. The numbered prompt
procedure is serial; independent audits and disjoint documentation edits
within an activity were delegated concurrently. References and examples are
inert. This review changes explanations only; it does not adopt a protocol
revision for live work or establish acceptance, lifecycle completion or release.

## Coverage and dispositions

| Topic | Inspected owning evidence and consumers | Documentation disposition |
|---|---|---|
| Purpose/prerequisites | Specification 05; project scaffold README; existing Git/Codex instructions | Root/protocol overview and getting started clarified; compatibility guide updated. |
| Setup/adoption | Suite revision records; template/project README; profile Change record and existing ledgers; lock tool/tests | Reference/adopted roots, source receipts, hooks and configured interpreter explained; no migration inferred. |
| Evidence/authority | Specifications 01/07; source-mapping and receipt sources; validator decision tests | Evidence orientation and architecture guide distinguish invariants, observations, work conflicts and human decisions. |
| Initiative workflow | Specifications 02/04/08; all 14 prompts/shared contract; validator/template tests | Separate acceptance, three delivery paths, canonical use and preceding owning-stage recovery reconciled. |
| Scopes/provenance | Specifications 06/09; tadp_scopes; scopes/topology tests and canonical registries | Grouped paths, exact scope/note identities and legacy compatibility reconciled in layout/scope guides. |
| Intake/revision | Specifications 02/07/09/10; intake prompts and reopening tests | Bounded delegation explained without inferring acceptance; changed claims require renewed acceptance. |
| Git/closure | Specifications 05/09; integration helper and isolated Git tests | Shared/dedicated roles, captured bases and immediate-parent closure authority clarified; remote actions remain separate. |
| Coherence/feedback | Specification 10; work-conflict/completion sources and coherence tests | Current open effort and affected closed claims retained; invariant and work-conflict routes distinguished. |
| Prompt locations | Repository prompts/AGENTS; project-local prompts/AGENTS; protected numbered library | Navigation distinguishes the three boundaries; local README gets compatible appended guidance only. |
| Prompt keywords | Specification 11; tadp_keywords and keyword/scheduling tests | Defaults, positional/inverse behavior, list scheduling and exact authority linked; examples remain reference-only. |
| Protected sources | Suite index and scoped instructions; tadp_protect/tests; protected locks | Sources versus copies and specifically authorized refresh retained; no protected change in this documentation execution. |
| Tools/verification | CLI parser implementations, observed help output, existing tests and final validator output | Entry points, roots, args, exit behavior, JSON support and library limits documented. |

The added prerequisite capability is installed at the item-2 commit. Existing
project adoption records and proposed/partial initiative effort retain their
recorded standing. File presence, source labels, branches and passing structural
tests do not establish adoption, accepted scope or verified application behavior.

## Document inventory

The reviewed editable set comprises root `README.md`; `protocol/README.md`;
`protocol/docs/README.md`; every guide under `protocol/docs/development/` and
`protocol/docs/guides/`; `protocol/tools/README.md`; and the explanatory
initiative, product, evidence and project-local prompt READMEs named below.
Changed paths are listed in the final section. Unchanged reviewed documents
are retained where current or deliberately describing a predecessor revision:

- `protocol/docs/guides/initiative-coherence-migration.md`
- `protocol/docs/guides/legacy-initiative-decomposition.md`
- `protocol/docs/guides/project-local-prompts-migration.md`
- `protocol/docs/guides/protected-source-integrity-migration.md`
- `protocol/docs/guides/template-prerequisites-migration.md`
- `protocol/docs/guides/version-realization-correlation-migration.md`
- `protocol/docs/guides/workflow-stage-0-13-migration.md`
- `protocol/evidence/non-authoritative/README.md`
- `protocol/evidence/non-authoritative/realizations/README.md`

Protected and unchanged in this execution: all `protocol/template/**`, the
authoritative evidence suite (including its already recorded conflicts), all
locks and all AGENTS instructions. Historical and preserved: distribution
decision receipts, the earlier template maintenance record, adoption/profile
records, migration-ledger dispositions and live initiative claims/specifications,
source realizations, status and lifecycle records. Product deliverables,
executable tools/tests/hooks/configuration, other repository prompts, historical
examples, other scaffolds and the separate fork are outside this edit target.

## Remaining findings and limits

Baseline and final validation retain two historical `TADP002` links in
`initiatives/design/INIT-DSN-001-version-realization-correlation/architecture.md:46`
and `source-mapping.md:23`, pointing to removed example material. Correcting
those excluded records requires specific authority and applicable closed-claim
handling. `TADP033` still reports the Deferred legacy mapping; this documentation
task cannot decide its migration.

The root `.githooks/pre-commit` loops over `protocol` and `example`, although
current repository maintenance excludes example synchronization. Its exact
proposed correction is to remove the example iteration for this reference
repository, retaining protocol validation and protection. Executable-hook
maintenance requires a separate explicit instruction. Documentation now
identifies the existing `protocol/.githooks/pre-commit` and correct reference
versus adopted hook paths; no configuration or hook was changed here.

The two pre-existing contradictions in the invariant register remain open:
`INV-CONFLICT-001` identifies realization standing/suite-boundary clauses in
`template/initiatives/proposal/README.md`; proposed correction is to preserve
permanent non-authoritative standing and many-outcome catalogs under
specification 09. `INV-CONFLICT-002` identifies unconditional push clauses in
Stages 5/6; proposed correction is to require separately sufficient remote
authority. Each requires exact protected-source follow-up authority, consumer
reconciliation, verification and matching locks. This review does not resolve
them or advertise those contradictory clauses as supported operation.

The human-supplied example repository and clone URL are linked without remote
inspection. Availability, rebuild completion, feature parity, application
verification and adoption are unverified. No synchronization, cloning,
separate-fork work, push, integration, PR, release or deployment was performed.

## Verification

All commands use the configured Python 3.11.1 executable at
`C:/Users/User/PycharmProjects/TADp/.venv/Scripts/python.exe`, from `protocol/`
unless explicitly identified otherwise. Baseline protection exited 0 with
zero errors; baseline validation exited 1 with the two historical errors and
one warning described above. Read-only `--help` checks for `tadp_validate.py`,
`tadp_protect.py` and `tadp_keywords.py` each exited 0. No documented mutating
setup, lock, integration or external command was executed for this refresh.

The item-2 full suite passed 163 tests and the final focused suite passed 26;
their output and limitations remain in the earlier maintenance record. The
documentation-only refresh retains that executable verification without
rerunning the multi-minute suite. Final link/anchor, protection, validator,
whitespace and boundary results are recorded below after checking.

Final changed-document link/anchor check examined 138 local references with
zero findings (exit 0), including the repository-root README, which is outside
the protocol validator's root. Scoped whitespace review passed. The added
review-index link uses the existing file and matching heading.

Concurrent external work added and staged 14 copied files under
`protocol/template/project/evidence/authoritative/LLM/` after the clean item-3
baseline. They are unrelated to this documentation refresh and remain
untouched in the index. At the final observed check, protection exited 1 with
14 `TADP025` unexpected-source errors; validation exited 1 with 41 errors and
one warning: the baseline two link errors plus 14 integrity and 25 copied-source
link errors. These additional findings arise from the concurrent copied tree,
not a documentation or lock change. No lock is refreshed to absorb them.
This differs from item 2's verified protection pass and baseline-only validator
result. The final documentation commit explicitly selects its own paths so
the externally staged additions and unrelated deletions are excluded.

The worktree diff of the existing protected suite, template sources and locks,
tools, tests, instructions and `.gitignore` against `f1f7df6` is unchanged by
this task. The concurrent additions retain their separate standing and require
their owner's decision; this review does not authorize or resolve them.

## Exact changed paths

- `README.md`
- `protocol/README.md`
- `protocol/docs/README.md`
- `protocol/docs/development/adapting-other-tools.md`
- `protocol/docs/development/architecture-and-authority.md`
- `protocol/docs/development/developing-tadp.md`
- `protocol/docs/development/getting-started.md`
- `protocol/docs/development/git-and-codex-requirements.md`
- `protocol/docs/development/initiative-workflow.md`
- `protocol/docs/development/repository-layout.md`
- `protocol/docs/development/validation-and-quality.md`
- `protocol/docs/development/documentation-review-20261113.md`
- `protocol/docs/guides/prompt-keywords-migration.md`
- `protocol/docs/guides/version-scope-migration.md`
- `protocol/evidence/README.md`
- `protocol/initiatives/README.md`
- `protocol/products/README.md`
- `protocol/prompts/README.md`
- `protocol/tools/README.md`
