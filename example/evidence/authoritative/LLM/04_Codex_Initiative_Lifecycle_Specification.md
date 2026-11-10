# Codex initiative lifecycle specification

## Purpose

This specification defines the only lifecycle states and transitions Codex may
record for a TADp initiative. Lifecycle claims are evidence claims. Changing a
status does not create the facts required by that status.

## States

| State | Meaning | Minimum evidence |
|---|---|---|
| `Proposed` | The bounded claim is under review and does not authorize delivery. | Proposal source, declared type and scope, and an open lifecycle entry. |
| `Accepted` | A human authority accepted the coherent initiative claim and its gates. | Acceptance decision receipt, resolved blocking decisions, invariant-compatible specification, and accepted baseline revision. |
| `In progress` | Permitted work has actually begun on the accepted claim. | Accepted state, prepared Git branch, start event, and type-appropriate execution evidence. |
| `Completed` | The exact accepted claim has passed every in-scope gate. | `completion-evidence.md`, required outputs, verification, reconciled status records, and no undisposed in-scope work. |
| `Cancelled` | Work stopped without a replacement claim. | Human cancellation authority, reason, retained evidence, and disposition of partial work. |
| `Superseded` | A named replacement now owns the claim. | Human supersession authority, replacement link, compatibility or migration effect, and retained history. |

`Reopened` is an event, not a steady state. A reopened initiative returns to
`Proposed` unless an explicit human decision states that the prior accepted
claim remains unchanged and authorizes return to `Accepted`.

Workflow stages and lifecycle states are distinct. The authoritative workflow
specification defines which stages may produce transition evidence; completion
of a stage does not itself cause a transition.

## Legal transitions

| From | May transition to | Required evidence |
|---|---|---|
| `Proposed` | `Accepted`, `Cancelled`, `Superseded` | The decision, decision receipt, resulting claim, and reconciled records. |
| `Accepted` | `In progress`, `Proposed`, `Cancelled`, `Superseded` | Start evidence for `In progress`; otherwise a documented revision, cancellation, or supersession event. |
| `In progress` | `Completed`, `Accepted`, `Proposed`, `Cancelled`, `Superseded` | Completion evidence, or a documented pause/replanning/revision event with partial-work disposition. |
| `Completed` | `Proposed`, or `Accepted` only under the unchanged-claim exception | Explicit human reopening authority, prior completed claim, reason, affected evidence, compatibility effect, and new verification boundary. |
| `Cancelled` | `Proposed`, or `Accepted` only under the unchanged-claim exception | Explicit human reopening authority and a new disposition for the earlier cancellation. |
| `Superseded` | `Proposed`, or `Accepted` only under the unchanged-claim exception | Explicit human reopening authority and reconciliation with the named replacement. |

Every other direct transition is prohibited. Codex must not infer acceptance
from implementation activity, completion from a merge, cancellation from
inactivity, or supersession from the existence of newer work.

## Lifecycle history

Every initiative README must keep an append-only lifecycle history with:

- effective date or event;
- prior and resulting state;
- human authority or execution evidence;
- decision-receipt or verification link;
- accepted or completed claim revision;
- reason and affected scope; and
- Git commit when available.

A correction may add a new entry that explains an earlier mistake. It must not
silently rewrite a truthful historical transition.

## Reopening and revision

Before reopening or materially revising an initiative, preserve the earlier
accepted or completed claim and record the human instruction that authorizes
the change. Reconcile assumptions, decisions, architecture, evidence mapping,
roadmap, steps, products, verification, parent and dependent tracking, and
completion evidence affected by the revision.

Reopening authorizes only the recorded scope. It does not authorize an
invariant change, erase prior evidence, or make an earlier product claim false
retroactively.

## Status synchronization

The initiative README is the lifecycle authority for the initiative. Shared
status views, parent indexes, subinitiative records, branch descriptions, and
pull requests must reflect it without expanding the claim. When records differ,
Codex must stop the affected transition, preserve the stronger evidence, and
reconcile the records before continuing.


