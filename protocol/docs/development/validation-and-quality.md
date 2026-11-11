# Validation and quality

## Purpose

`../../tools/tadp_validate.py` turns machine-checkable parts of the protocol into a
repeatable repository check. It is deliberately narrower than architectural
review: it can verify structure and traceability signals, but it cannot decide
whether an architecture is good, a human response is wise, or a product is
ready for production.

## Running validation

From the protocol root (`protocol/` in the reference repository and normally
the project root in an adopted repository):

```powershell
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
```

For structured output:

```powershell
python tools/tadp_validate.py . --json
```

Exit status meanings:

| Status | Meaning |
|---|---|
| `0` | No validator errors were found. |
| `1` | One or more protocol findings were reported. |
| `2` | The requested repository root is invalid. |

Run regression tests with:

```powershell
python -m unittest discover -s tests -v
```

## What the validator checks

The current validator checks:

- SHA-256 integrity locks for every file under `template/` and
  `evidence/authoritative/LLM/`, including detection of missing locks,
  unexpected files, removed files, content drift, and symbolic links;
- containment in a valid TADp Git repository and a repository-root
  `AGENTS.md` entry point;
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
- canonical `v<major>.<minor>` work-version syntax and numeric ordering;
- one-to-one version, realization-suite, initiative, and dedicated-branch
  mappings in the canonical initiative index;
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
staged changes to either protected root. Enable it once in every clone or
worktree:

```powershell
git config core.hooksPath .githooks
```

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
pipeline should run both the validator and regression tests from the repository
root using an explicitly supported Python version.

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

