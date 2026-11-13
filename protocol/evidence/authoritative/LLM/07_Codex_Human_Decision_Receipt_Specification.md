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
migration-ledger rows. It does not retroactively make incomplete identity valid.

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

## Documentary sources

Use specification 02's
[canonical template rules](02_Codex_Initiative_Governance_Specification.md#canonical-template-selection-and-use)
and specification 08's
[preceding preparation procedure](08_Codex_Initiative_Workflow_Specification.md#documentary-prerequisite-preparation)
for records required by this specification. The
[coverage map](../../../template/TEMPLATE-COVERAGE.md) identifies reusable file
and embedded-section sources, their destinations, owners, and conditional
triggers. Documentary recovery does not supply missing authority, identity,
decisions, work, verification, or legal lifecycle events; this specification's
substantive requirements remain binding.

## One decision per receipt

Each receipt records one human decision for one stable source ID or one clearly
bounded event. Under specification 09, capture the actual human realization
intake instruction as delegation, then record each LLM routing/reopening event
and its actual author, target and fit separately before applying it. Do not
fabricate a per-target human answer or require repeated confirmation solely
because the target is closed, existing or cross-scope. A blanket human response
may cover a set only when it identifies that complete set without ambiguity.

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
- every affected scope, suite/note, initiative/revision cycle, branch, canonical-row, and
  migration-ledger identity when the decision changes correlation handling;
- unresolved consequences or re-entry conditions; and
- the Git commit that records the receipt and reconciliation, when available.

## Recording order

A reopening receipt declares `**Disposition:** Reopened` and
`**Human authority:**`, cites the exact prior claim, and identifies the newly
authorized scope and verification boundary. A direct closed-to-`Accepted`
transition also declares `**Unchanged accepted claim:** Yes` and preserves the
human decision supporting that exception. Each new reopening needs its own
receipt; an earlier acceptance or reopening event cannot be reused. A bounded
intake may support several necessary target events, each independently recorded.
A delegated event also records `**Decision method:** Delegated realization intake`,
`**Decision author:**`, source realization ID/path, exact human intake words,
governing revision and delegation, candidate targets, chosen scope/branch,
rejected alternatives, fit rationale, prior state/claim revision, risks,
compatibility, affected records and necessary scope/ancestor reopening events.
Its human-authority field links the delegation, not an invented target answer.
Direct return to `Accepted` still requires a separate explicit human
unchanged-claim decision. Delegation never implies acceptance, product
execution, unrelated answers or passing verification. These objective fields support the
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

A receipt preserves what the named human instructed and what the recorded
LLM author decided under an applicable delegation. It does not prove
implementation, verification, release or broader acceptance, waive an
unexcepted invariant, or silently transfer ownership. Outside specification
09's bounded intake method, ordinary per-event human authority remains required.


