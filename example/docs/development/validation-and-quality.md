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

- containment in a valid TADp Git repository and a repository-root
  `AGENTS.md` entry point;
- required repository, authoritative-suite, template, prompt, and developer
  documentation paths;
- local Markdown links;
- unresolved braced tokens outside reusable templates;
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
- decision receipts and source links for recorded human dispositions; and
- fourteen complete numbered prompts for stages 0 through 13, each with example
  language, a shared-contract reference, and executable
  `&#123;initiative&#125;` placeholder.

The validator ignores `.git` contents when walking Markdown and treats files
under template paths as reusable, so their placeholders are permitted.

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

