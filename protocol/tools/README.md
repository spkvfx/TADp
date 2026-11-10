# TADp tools

Run the repository validator from the project root:

```powershell
python tools/tadp_validate.py .
```

Use `--json` for continuous integration or another machine consumer. The
validator exits with status `1` when protocol errors exist and `2` when the
requested repository root is invalid.

The validator checks the Git requirement, protocol structure, authoritative
LLM suite, required developer documentation, local Markdown links, unresolved
tokens outside reusable templates, complete initiative suites, legal lifecycle
transitions, execution and completion records, human decision receipts, prompt
contracts, and source-mapping fields. Its checks grow with the binding TADp
specifications; passing validation never replaces human acceptance or product
verification.

