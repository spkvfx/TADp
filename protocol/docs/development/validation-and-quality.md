# Validation and quality

## Purpose

`../../tools/tadp_validate.py` turns machine-checkable parts of the protocol into a
repeatable repository check. It is deliberately narrower than architectural
review: it can verify structure and traceability signals, but it cannot decide
whether an architecture is good, a human response is wise, or a product is
ready for production.

## Running validation

From the protocol root (`protocol/` in the reference repository and normally
the project root in an adopted repository), use the project's configured
Python interpreter. `python` below stands for that interpreter, not an
assumed system installation. These are reference commands; reading this guide
performs no checks or maintenance.

```powershell
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
```

For structured output:

```powershell
python tools/tadp_validate.py . --json
```

After adopting the coherence revision, a branch review should select the
captured integration or merge base explicitly:

```powershell
python tools/tadp_validate.py . --base-ref <captured-base-commit>
```

The explicit/default checked root is the scaffold installation directory, not
an inferred Git top level. Git operations discover `G` and map project paths
through the verified prefix; nested historical comparisons and staged guards
exclude parent and sibling paths. Shared worktree state and hooks still require
coordination. See [root adoption](../guides/project-root-installation-migration.md).

The default comparison is `HEAD`, which checks local changes against the latest
commit. An explicit comparison base covers terminal-record edits across a
branch, including changes already committed on that branch.
The history check also covers an initiative completed and then changed in a
later commit within that range. A later reopening cannot legitimize an earlier
unrecorded refinement.

Exit status meanings:

| Status | Meaning |
|---|---|
| `0` | No validator errors were found. |
| `1` | One or more validator errors were reported. Warnings alone retain exit `0`. |
| `2` | The requested root does not exist, or CLI arguments are invalid. |

An existing directory with missing Git metadata or scaffold files reports
errors with exit `1`. JSON mode reports the same findings and exit status as
text mode. The protection tool has separate text output and exit meanings;
see the [tool entry points](../../tools/README.md).

Run regression tests with:

```powershell
python -m unittest discover -s tests -v
```

## What the validator checks

The shared `../../tools/tadp_keywords.py` reads the canonical registry from
[specification 11](../../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md).
Keyword regression cases exercise positional state, exact boundaries, inert
source regions, exception prerequisites, preview/local/review composition,
and serial/parallel scheduling. The validator checks the registry and its
universal entry-point references without relaxing ordinary lifecycle checks.
These checks cannot authenticate a human instruction, infer semantic authority
from prose, intercept tools, or prove that a real review or concurrent tool
activity occurred. Consumers retain those obligations and must preserve
skipped, failed, and unavailable evidence. See the
[adoption guide](../guides/prompt-keywords-migration.md).

`TADP046` reports a malformed adopted canonical registry; `TADP047` reports
a missing direct specification reference in the suite index or universal
entry points. Reusable project instructions deliberately use the installed
project's direct relative link. Link validation resolves that exact canonical
destination against the adopting root without creating a duplicate authority
tree under `template/project/`. A missing canonical target still fails.

The current validator checks:

- SHA-256 integrity locks for every file under `template/` and
  `evidence/authoritative/LLM/`, including detection of missing locks,
  unexpected files, removed files, content drift, and symbolic links;
- containment of the project installation directory in a valid Git worktree
  and a project-root `AGENTS.md` entry point;
- required repository, authoritative-suite, template, prompt, and developer
  documentation paths;
- a direct project-local `prompts/` directory with `AGENTS.md` and
  `README.md`, resolved inside the checked scaffold and preserving the
  canonical reusable content from `template/project/prompts/`;
- separation of additional project-local prompt files from authoritative
  evidence and the protected numbered workflow, without treating an enclosing
  Git root as a wider scaffold boundary;
- local Markdown links;
- unresolved braced tokens in prose outside reusable templates (literal fenced
  and inline code is excluded);
- complete initial initiative suites;
- supported lifecycle status values;
- lifecycle history presence, legal transitions, continuity, and agreement
  with declared status;
- completion evidence for `Completed` initiatives;
- execution records for in-progress implementation initiatives;
- delivery records for in-progress or completed design and planning initiatives;
- explicit acceptance receipts for accepted, in-progress, and completed
  initiatives;
- authoritative and verification evidence fields in source mappings;
- canonical scope syntax and numeric component ordering after scope adoption;
- scope registry topology, unique initiative membership and exact source routing,
  dedicated/shared execution assignments, captured bases and integration evidence;
- predecessor one-to-one correlation only for records governed by that revision;
- reciprocal identity and base metadata among the canonical index, suite index,
  initiative record, and the project status view after Stage 3 expands the
  preparation skeleton;
- live local refs for active initiative branches, and linked removal authority
  when a historical initiative branch is absent;
- orphan realization suites and initiatives after correlation adoption;
- permanently non-authoritative standing for realization suites; and
- complete legacy migration-ledger actions, including actionable warnings for
  deliberately `Unmigrated` or `Deferred` rows;
- decision receipts and source links for recorded human dispositions; and
- fourteen complete numbered prompts for stages 0 through 13, each with example
  language, a shared-contract reference, and executable
  `&#123;initiative&#125;` placeholder.

Correlation validation activates only when `project-profile.md` declares a
version-correlation effective point. Pre-effective projects therefore remain
compatible until they explicitly adopt the revision. Once active, incomplete or
mixed legacy mappings are errors; a complete `Unmigrated` or `Deferred` row is
reported as `TADP033` warning so the unresolved migration remains visible without
inventing a canonical identity. Warnings do not change the validator exit status
when no errors exist.

## Canonical template and prerequisite checks

When the canonical coverage revision is installed, `TADP050` checks its JSON
map, unique IDs, required metadata, source files/sections, governing locators,
embedded members, and instance destination boundaries. `TADP051` checks the
shared preparation procedure and the fourteen numbered prompts plus scope
closure for known prerequisite IDs and explicit executable preparation calls.
Removing a map still fails when the governing specifications reference it.
Older distributions without this revision keep their earlier contract.

`tools/tadp_templates.py` exposes a read-only assessment API for explicitly
reviewed prerequisite facts. Focused tests cover missing and embedded sources,
conditional records, grouped-depth links, recorded authority versus missing
paperwork, unavailable/conflicting evidence, owning-stage recovery, missing
identity, wrong type, closed claims, stale phase evidence, idempotence and the
Stage 9 preparation/assessment boundary. No helper writes a record or executes
a prompt. Review actual prompt behavior as well: passing synthetic cases cannot
prove semantic evidence completeness, authentic authority, lawful adoption,
or that a missing event occurred. See the
[canonical map](../../template/TEMPLATE-COVERAGE.md) and
[migration guide](../guides/template-prerequisites-migration.md).

## Initiative coherence checks

The [coherence specification](../../evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md)
adds checks when the project profile declares a resolved
`Coherence revision baseline`. This is the fixed pre-adoption Git commit,
not an authority or acceptance record. Existing terminal completions preserved
at that baseline do not need an invented historical review; new completion
claims and later changes follow the adopted rule.

| Finding | Checked condition |
|---|---|
| `TADP041` | A resolvable adoption baseline and the project work-conflict register exist. |
| `TADP042` | Governed completion evidence has a cross-initiative coherence review, baseline and register fields, and an inventory covering every other open initiative. |
| `TADP043` | A prior terminal initiative's files are preserved unless a new reopening event and linked human decision receipt support the change. |
| `TADP044` | Work-conflict rows preserve their required identity, claims, effort, impact, owner, status, and disposition fields. |

The terminal-record comparison includes removed initiative directories and
files. It permits narrow administrative additions and append-only factual
history corrections; it does not treat an old reopening receipt as authority
for a new revision. An adopted baseline cannot be silently changed, removed,
or deactivated in the project profile. See the [migration guide](../guides/initiative-coherence-migration.md)
for adoption and comparison-base handling.

The inventory check does not determine semantic compatibility, discover every
unrecorded conflict, certify that effort estimates are accurate, or accept a
proposed resolution. Those obligations remain part of human and architectural
review. Recognizing proposed effort never makes that effort authoritative.

The validator ignores `.git` contents when walking Markdown and treats files
under template paths as reusable, so their placeholders are permitted.
Additional files under root `prompts/` are validated as ordinary working
project material; they are not added to the protected template file set.

## Protected-source workflow

`template/` and `evidence/authoritative/LLM/` are read-only during ordinary
project and initiative work. Each root contains a `.tadp-lock.json` whose file
set and SHA-256 digests are checked by both `tadp_protect.py check` and the full
validator.

An exact copy of a TADp distribution already includes valid locks. A legacy
adoption with no locks may initialize them only after a human identifies the
baseline being accepted:

```powershell
python tools/tadp_protect.py initialize . --authority "initial TADp adoption from <revision or decision>"
```

For an explicitly authorized change, refresh only the affected protected root
after completing its compatibility, migration, consumer, and verification
work:

```powershell
python tools/tadp_protect.py refresh . --protected-root template --authority "<human instruction or decision record>"
python tools/tadp_protect.py refresh . --protected-root evidence/authoritative/LLM --authority "<human instruction or decision record>"
```

Never initialize or refresh a lock merely to make an unexplained difference
pass. A lock states the authorized canonical-content baseline; it does not
authorize the underlying template or invariant change. UTF-8 text is normalized
to LF line endings before hashing so a Git checkout's line-ending conversion
does not create false drift; binary content is hashed as stored.

The tracked `.githooks/pre-commit` first runs full validation and then blocks
staged changes to either protected root. This describes the hook inside the
protocol/adopted project. Inspect and coordinate existing hooks at the actual
Git root before explicitly configuring its shared hook path. This inert example
applies to a Git-root installation only:

```powershell
git config core.hooksPath .githooks
```

For a nested project at `projects/widget`, the Git-relative setting would be
`core.hooksPath=projects/widget/.githooks`. In this reference repository the
protocol hook is at `protocol/.githooks`, so the setting relative to `G` is
`core.hooksPath=protocol/.githooks`. Do not overwrite or enable parent hooks
implicitly; installation performs no configuration change.
The repository-root `.githooks/pre-commit` is an older combined hook that still
targets `protocol` and `example`; it does not reflect the current separate
example boundary. Correcting that executable requires separately authorized
support-file maintenance. Inspect an existing hook configuration before
changing it. The supported protocol hook uses `TADP_PYTHON` when set and
otherwise resolves `python`; select the configured interpreter explicitly
when the shell default differs. Hook installation changes local Git
configuration and is not performed by a validation command.

An authorized protected-source commit must set
`TADP_ALLOW_PROTECTED_UPDATE=1` and set
`TADP_PROTECTED_UPDATE_AUTHORITY` to the exact authority string stored in the
affected refreshed lock. These variables are an intentional commit gate, not a
general bypass. Directory-scoped and root `AGENTS.md` instructions prohibit
Codex from using them without the same explicit human authority.

## What validation does not prove

A zero-error result does not prove:

- that every applicable invariant was discovered;
- that a source was classified correctly;
- that a human had the claimed authority;
- that the initiative architecture is complete or internally sound;
- that a test was actually run unless independently evidenced;
- that local verification generalizes to release or production;
- that a pull request was reviewed or merged; or
- that an external system is available or correctly configured.

It also does not prove that the person named by a protected lock had authority.
Git review ownership and the recorded human decision remain responsible for
that claim.

Those claims remain owned by evidence, human review, product verification, and
the appropriate lifecycle gate.

## Adding a validator rule

Add a rule only when the protocol defines an objective condition that can be
checked without inventing semantic authority.

For every new rule:

1. Identify the authoritative or template contract it enforces.
2. Choose a stable finding code and a precise path and message.
3. Avoid false authority; warn or stop when the validator cannot know the
   semantic answer.
4. Add one passing test and at least one failing regression test.
5. Update `../../tools/README.md` and this document.
6. Run the full validator and test suite.

Do not make the validator silently repair records. Repairs can destroy evidence
or imply decisions. It should report the exact discrepancy and leave the
governed correction to the appropriate workflow.

## Continuous integration

The JSON mode is suitable for CI or a repository-specific wrapper. A minimal
pipeline should run both the validator and regression tests from `protocol/`
in this distribution, or the adopted project's root, using its configured
Python interpreter. The interpreter verified for this maintenance was Python
3.11.1; this does not certify other interpreter versions.

CI should fail on validator errors. It must not automatically accept an
initiative, resolve a question, or promote a lifecycle state merely because the
structural checks pass.

CI and host-side branch protection should also require owner review whenever a
diff touches `template/**`, `evidence/authoritative/LLM/**`, or either lock
file. This server-side review complements the local hook, which Git does not
enable automatically in a new clone.

## Documentation quality

When editing Markdown:

- prefer repository-relative links;
- link the exact authoritative source for normative statements;
- keep the root README and `../README.md` indexes synchronized;
- avoid project names and local filesystem locations in reusable prompt
  examples;
- use “attached initiative” only in example invocation text and
  `&#123;initiative&#125;` in executable prompt blocks; and
- run the validator after every rename or move.

