# TADp tools

Run the repository validator from the protocol root (`protocol/` in the
reference repository and normally the project root in an adopted repository):

```powershell
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
```

Use `--json` for continuous integration or another machine consumer. The
validator exits with status `1` when protocol errors exist and `2` when the
requested repository root is invalid.

The validator checks the Git and repository-root `AGENTS.md` requirements,
protocol structure, protected template and authoritative-LLM SHA-256 locks,
required developer documentation, local Markdown links, unresolved
tokens outside reusable templates, complete initiative suites, legal lifecycle
transitions, acceptance receipts, type-specific execution or delivery records,
completion evidence, human decision receipts, all fourteen numbered prompt
contracts, and source-mapping fields. Its checks grow with the binding TADp
specifications; passing validation never replaces human acceptance, delivery
verification, or product verification.

The path supplied to the validator must be the protocol or adopted TADp root
and must be contained in a valid Git repository. The Git metadata may be at
that path or an ancestor, as it is in this reference repository where
`protocol/` is the distributable protocol tree and the parent directory is the
Git root.

`tadp_protect.py` owns deliberate lock creation and refresh. `initialize`
refuses to replace an existing lock, `refresh` refuses to create a missing
lock, and both require a non-empty `--authority` reference. Ordinary work must
use `check` only. The `guard-staged` action is called by the tracked pre-commit
hook and blocks protected-source commits unless the explicit update variables
and refreshed lock carry the same authority reference. See
[Validation and quality](../docs/development/validation-and-quality.md) for the
governed commands and limitations.

