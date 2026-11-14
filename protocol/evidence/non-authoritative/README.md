# Non-authoritative evidence

This directory holds contextual evidence: observations, studies, examples,
recommendations, exploratory analysis, proposals, and other material that can
inform a decision without becoming a binding requirement. It protects useful
discovery work from being lost while protecting the project from treating every
note as a mandate.

## What belongs here

| Material | Where to start | What it may do | What it may not do |
|---|---|---|---|
| A bounded observation, research summary, benchmark, or recommendation | [Contextual evidence source](../../template/project/evidence/non-authoritative/contextual-evidence.template.md) | Provide context, reveal uncertainty, or support a proposal | Override a binding source or authorize implementation alone |
| An opportunity, concern, insight, or requested outcome | [realizations/README.md](realizations/README.md) | Seed a proposal or triage conversation | Become an accepted initiative requirement merely by being cited |
| A source accepted as binding | Move or recreate it in [authoritative evidence](../authoritative/README.md) with acceptance metadata | Govern work after explicit acceptance | Gain authority from a filename or directory move alone |

## Capture contextual evidence

1. When the governing workflow calls for contextual evidence, select the
   [contextual evidence source](../../template/project/evidence/non-authoritative/contextual-evidence.template.md)
   from the protected library and copy it into this directory with a descriptive
   filename such as `OBS-014-latency-study.md`. Edit only that copy.
2. Preserve the original source, author or origin, date, method, sample or
   environment, and any conditions that affect interpretation.
3. Give the observation an ID and label it exactly
   `../../../../evidence/non-authoritative`.
4. Write the finding as an observation, not an instruction. For example,
   `The benchmark observed a 95th-percentile latency increase under load`, not
   `The service must adopt approach X`.
5. State limitations: incomplete samples, assumptions, potential bias, stale
   data, unverified claims, or missing authoritative sources.
6. Say which initiative, proposal, product assessment, or question the record
   may inform and what follow-up is needed.

## Use contextual evidence safely

An initiative may cite contextual evidence to explain why a question is being
asked, compare options, or prioritize investigation. It must still identify
binding evidence separately and make an explicit decision before work is
accepted. A product record may cite an observation as verification context, but
the observation is not acceptance evidence unless the governing specification
or rule says so.

If contextual and authoritative evidence appear to conflict, preserve both and
record the contradiction in the initiative or evidence register. Do not
silently select the observation because it is newer, more convenient, or closer
to an implementation. Ask the authoritative record's owner to clarify, revise,
or explicitly accept an exception.

## Promote evidence deliberately

Context can become a candidate input to a binding record, but it cannot promote
itself. To promote a finding:

1. Keep the original contextual record unchanged and cite its ID.
2. Have the responsible authority review the method, limitations, and proposed
   normative claim.
3. Create an authoritative evidence, architecture, or rule record that names
   the accepting authority, scope, effective date, verification, and source.
4. Update the evidence register and affected initiatives to cite the new binding
   record for requirements, while retaining the contextual record as support.

## Revision and archival practice

Add a linked revision when facts, measurements, or interpretation change. State
what changed and why; do not overwrite an earlier observation or erase its
limitations. Mark a record superseded or closed when appropriate, but keep it
discoverable. This lets later work explain why an earlier proposal or decision
was reasonable at the time.

## Review checklist

- [ ] The source, date, method, conditions, and limits are recorded.
- [ ] The record is labelled non-authoritative and does not use normative
      wording unless it quotes a separately cited binding source.
- [ ] Its potential consumer or follow-up owner is explicit.
- [ ] Any authoritative conflict is visible and routed to the correct owner.
- [ ] Revisions preserve the original observation and link the change.
