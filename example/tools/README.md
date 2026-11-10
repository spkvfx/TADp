# TADp tools

Run the repository validator from the protocol root (`protocol/` in the
reference repository and normally the project root in an adopted repository):

```powershell
python tools/tadp_validate.py .
```

Use `--json` for continuous integration or another machine consumer. The
validator exits with status `1` when protocol errors exist and `2` when the
requested repository root is invalid.

The validator checks the Git and repository-root `AGENTS.md` requirements,
protocol structure, authoritative LLM suite, required developer documentation,
local Markdown links, unresolved
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

