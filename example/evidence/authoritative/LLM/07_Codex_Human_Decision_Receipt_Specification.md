# Codex human decision receipt specification

## Purpose

An assumption disposition, open-question answer, initiative acceptance,
reopening, cancellation, supersession, or invariant exception that requires a
human decision must have a durable decision receipt. A chat summary or changed
status alone is not sufficient evidence.

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
- unresolved consequences or re-entry conditions; and
- the Git commit that records the receipt and reconciliation, when available.

## Recording order

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


