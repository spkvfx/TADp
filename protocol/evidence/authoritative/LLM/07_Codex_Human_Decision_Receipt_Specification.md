# Codex human decision receipt specification

## Purpose

An assumption disposition, open-question answer, initiative acceptance,
reopening, cancellation, supersession, or invariant exception that requires a
human decision must have a durable decision receipt. A chat summary or changed
status alone is not sufficient evidence.

A meaning-changing legacy identity mapping, exception to a mandatory split,
or removal of a recorded initiative branch also requires a receipt. The
receipt must preserve every source identity, distinguish notation-only change
from changed meaning, and identify the affected canonical correlation and
migration-ledger rows. It does not retroactively make a partial tuple valid.

## Prompt exceptions and actual decision authorship

The canonical
[prompt keyword specification](11_Codex_Prompt_Keyword_Specification.md)
governs mode requests and exceptions, including exceptions proposed without a
keyword. The agent may automatically capture sufficient actual human authority
and prepare the receipt before using it; the human need not author paperwork
or repeat the same sufficiently bounded instruction. Automatic documentation
does not supply approval. Preserve exact human words separately from the
agent's interpretation, proposed scope, autonomous method, and resulting
agent-made dispositions. Link every covered rule, source ID, instruction
block, affected record, and reconciliation. Never label an agent's answer as
a human response. Once the authority and records cover the exact scope, no
repeated confirmation is required solely to recreate that authority.

Use the
[gate-exception source](../../../template/initiatives/decision-receipts/gate-exception.template.md)
for the additional per-rule and per-block fields. A shared receipt may cover
multiple named gates only when the actual human authority explicitly covers
the complete bounded set. Inferred use or a further inferred invariant
exception remains unapproved until its exact proposal is confirmed. Neither
gate setting can authorize its own missing confirmation. Preview receipts and
exceptions remain response-only drafts, not adopted records.

Retain waived, skipped, failed, and passed evidence distinctly in receipts,
lifecycle, delivery, and completion consumers. An exception receipt records
the specific authority and disposition; it is not evidence that an ordinary
approval, test, review, acceptance, reopening, or completion occurred. Locks
and protected-source maintenance authority remain separate and enforced.

## One decision per receipt

Each receipt records one human decision for one stable source ID or one clearly
bounded lifecycle event. A blanket response may use one receipt only when the
human explicitly identifies the complete set and the receipt lists every item
without ambiguity.

## Required content

A decision receipt must preserve:

- a stable receipt ID and affected initiative;
- the source assumption, question, or lifecycle event ID;
- the exact prompt or question presented to the human;
- the exact human response, without paraphrase;
- the responder and the authority under which the response governs;
- the response date or event and capture context;
- the evidence and material limitations presented with the question;
- the resulting disposition and its precise scope;
- every initiative or tracking record reconciled from the decision;
- every affected work-version, suite, initiative, branch, canonical-row, and
  migration-ledger identity when the decision changes correlation handling;
- unresolved consequences or re-entry conditions; and
- the Git commit that records the receipt and reconciliation, when available.

## Recording order

A reopening receipt declares `**Disposition:** Reopened` and
`**Human authority:**`, cites the exact prior claim, and identifies the newly
authorized scope and verification boundary. A direct closed-to-`Accepted`
transition also declares `**Unchanged accepted claim:** Yes` and preserves the
human decision supporting that exception. Each new reopening needs its own
receipt; an earlier acceptance or reopening receipt cannot be reused. These
objective fields support the
[closed-claim preservation check](10_Codex_Initiative_Coherence_Specification.md)
without substituting for human authority.

After receiving an explicit response, Codex must create the decision receipt
before changing the source disposition. It must link the receipt from the
assumption, question, lifecycle history, or conflict record it resolves and
commit the receipt with the resulting reconciliation.

If the response is ambiguous, incomplete, outside the initiative boundary, or
would conflict with authoritative evidence, Codex must preserve it as context
but must not record a governing disposition. Ask the human to clarify or use
the invariant-conflict procedure.

## Limits

A receipt proves what the named human decided for the recorded scope. It does
not prove implementation, verification, release, or broader acceptance; waive
an invariant; or transfer authority to another initiative.


