<!--
Create this directory only when the first explicit human decision is received.
Create one receipt per source decision unless the human explicitly identifies
a coherent complete set. Do not copy this README during initial initiative
creation.
-->

# {{initiative_name}} decision receipts

Decision receipts preserve the exact human responses that govern assumption,
question, lifecycle, and exception dispositions. Link every receipt from its
source record and commit it with the records reconciled from that decision.

For the canonical prompt-keyword contract, preserve the human authorization in
a decision receipt before relying on a bounded gate exception. Use
`gate-exception.template.md` for the separate per-rule exception and block
ledger. The LLM may author both from sufficient existing authority without
asking for the same decision again. Automatic authorship supplies no approval.
Keep the human authorization distinct from every agent-made disposition under
its recorded autonomous method. Preview receipts and exceptions are response-only
drafts and must not create this directory or persistent records.

| Receipt ID | Source ID or event | Disposition | Human authority | Date or event | Source record | Commit |
|---|---|---|---|---|---|---|
| {{receipt_id}} | {{source_id_or_event}} | {{disposition}} | {{human_authority}} | {{yyyy-mm-dd_or_event}} | {{relative_link}} | {{commit_or_pending}} |


