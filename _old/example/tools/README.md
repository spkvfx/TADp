# TADp tools

Run the repository validator from the protocol root (`../../../protocol` in the
reference repository and normally the project root in an adopted repository):

```powershell
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
```

Use `--json` for continuous integration or another machine consumer. The
validator exits with status `1` when protocol errors exist and `2` when the
requested repository root is invalid.

The validator checks the Git and repository-root `../../../AGENTS.md` requirements,
protocol structure, protected template and authoritative-LLM SHA-256 locks,
the project-local prompt boundary and its reusable-source alignment, required
developer documentation, local Markdown links, unresolved
prose tokens outside reusable templates, complete initiative suites, legal lifecycle
transitions, acceptance receipts, type-specific execution or delivery records,
completion evidence, human decision receipts, all fourteen numbered prompt
contracts, source-mapping fields, and—after a project declares the correlation
revision effective—legacy work-version syntax, reciprocal tuple metadata,
branch continuity and migration dispositions. After explicit version-scope
adoption, it also validates shared scope membership, precise source routing,
major/minor/patch topology, recorded execution placement and closure evidence.
Its checks grow with the binding TADp
specifications; passing validation never replaces human acceptance, delivery
verification, or product verification.

After the project profile records a resolved `Coherence revision baseline`,
validation also checks the work-conflict register, completion reviews of every
other open initiative, and terminal-record preservation against Git. Proposed
effort is included in the review without gaining authority. Historical closed
claims preserved at the adoption baseline do not acquire invented reviews.

The terminal comparison defaults to `HEAD`. Use a captured integration or
merge-base commit to review a whole branch:

```powershell
python tools/tadp_validate.py . --base-ref <captured-base-commit>
```

The guard detects record edits and missing reopening evidence; it cannot judge
semantic compatibility or whether the named human had authority. See the
[coherence migration guide](../docs/guides/initiative-coherence-migration.md)
for the separate adoption-baseline and comparison-base roles.

The path supplied to the validator must be the protocol or adopted TADp root
and must be contained in a valid Git repository. The Git metadata may be at
that path or an ancestor, as it is in this reference repository where
`../../../protocol` is the distributable protocol tree and the parent directory is the
Git root.

`tadp_protect.py` owns deliberate lock creation and refresh. `initialize`
refuses to replace an existing lock, `refresh` refuses to create a missing
lock, and both require a non-empty `--authority` reference. Ordinary work must
use `check` only. The `guard-staged` action is called by the tracked pre-commit
hook and blocks protected-source commits unless the explicit update variables
and refreshed lock carry the same authority reference. See
[Validation and quality](../docs/development/validation-and-quality.md) for the
governed commands and limitations.


`tadp_keywords.py` consumes the single protected registry in
[specification 11](../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md).
It exposes positional interpretation, objective exception-record checks,
preview/local action checks, independent-review checks, and an asynchronous
reference scheduler for explicitly classified action trees. The validator
checks installed registry structure and universal entry-point links when that
revision is present; earlier projects retain their recorded governing revision.
Stored prompts and evidence are never scanned to activate directives.

```powershell
python tools/tadp_keywords.py . --prompt-id request-1 --text "Inspect first [tadp:preview] propose a change"
```

The CLI reports source blocks and requested settings; it performs no work and
adopts no exception. Callers must identify semantic explanatory ranges, actual
action lists, dependencies, tool permissions, specific human authority, and
active exception duration. Source settings snapshots are immutable. The list
scheduler joins nested children, preserves serial blockers, runs bulleted
siblings concurrently, and reports capacity limits before dispatch rather
than silently serializing declared parallel work.

`ExceptionRecord` records exact authority, rule/revision, source block, targets,
settings, prior state, method, actual agent dispositions, risks, evidence
limits, reconciliation, and restoration. `evaluate_gate` fails closed without
an exact active target scope; it preserves the original observed result and
never turns an exception into passing evidence. A preview exception remains a
response-only proposal; preview analysis and proposals use read-only action
checks without persisting or adopting an exception. Separate protected-source
maintenance must actually reconcile and verify locks through `tadp_protect`.
These helpers cannot authenticate human authority, classify natural-language
intent, establish semantic review quality, or intercept arbitrary agent tools.
The governing agent remains responsible for enforcing the canonical contract.

`tadp_scopes.py` supplies the prospectively adopted version-scope model.
`parse_scope` accepts exact `vN`, `vN.M`, and `vN.M.P` identities, compares
components numerically and preserves arity. `scope_parent` derives only the
structural major/minor parent; major scopes use the project's explicitly
recorded integration branch. No helper infers migration or source authority.

An immutable `Version scope revision effective point` in `project-profile.md`
activates `initiatives/version-scopes.md`, the scope membership table in
`initiative-index.md`, and `version-scope-migration-ledger.md`. Absence,
`Not yet adopted`, and `Installed; adoption pending` retain legacy handling.
The module exports `SCOPE_HEADERS`, `MEMBER_HEADERS`, `MIGRATION_HEADERS`, and
`SOURCE_HEADERS`; templates use those table shapes. Original tuple tables and
their legacy ledger remain checked when retained alongside the new table.
Deferred records do not qualify for delegated reopening just because a
project has adopted scopes; the target needs actual new canonical membership.

Read-only checks cover explicit suite/note identities and metadata, reciprocal
links, source catalogs, grouped paths and types, branch roles and captured
ancestry, scope navigation, current cycle/claim acceptance and delivery records,
closed-member/child integration evidence, and required scope reopening.
Recorded scope creation fields and execution assignment history are compared
with `HEAD`. This scope-table comparison does not inspect every intermediate
commit in a branch range; review must inspect those transitions separately.
The existing coherence guard retains its independent `--base-ref` range checks
for closed initiative claims. Human authority authenticity, narrow semantic
fit, ownership, completeness of an inventory and verification quality still
require review; objective fields cannot establish them.

`integrate_closed_child(root, IntegrationRequest(...), verify)` is an optional
bounded local helper, not a workflow dispatcher. Callers first persist the
actual closure instruction/authority, inspect accepted source changes and the
current parent, and check ownership of every included change. The helper
requires the recorded parent already checked out, a clean worktree, matching
captured source/target tips, closed source, open parent and qualified changes.
It rechecks refs/worktree after pre-verification and records direct placement,
no-deliverable, fast-forward, merge, already-integrated, or blocked results.
Conflicts and failed post-verification retain actual Git evidence; the helper
does not revert, delete branches, push, or invoke a hosting service. Callers
persist the result and post-verification evidence; it never accepts an
initiative or closes ancestors. Shared completed members must record their
`Verified member commit` separately from the whole shared tip.

`test_tadp_scopes.py` uses isolated Git repositories for shared/dedicated
placement, cross-scope provenance and mixed types, full adopted-project
validation, delegated terminal-state reopening, current-cycle acceptance,
closure blockers, precise numeric syntax, integration reruns, drift and real
conflicts. These fixtures are protocol-owned and do not migrate live projects.
