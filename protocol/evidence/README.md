# Evidence

This directory is the project's source library. It preserves material that
justifies, constrains, or explains decisions, and it records how much authority
each source has. Evidence is not a scratchpad: preserve the original artifact,
its source, date or revision, and the context needed to interpret it later.

## Choose the correct evidence class

Classify a source before an initiative or product relies on it. The label tells
reviewers whether the source is binding or merely informative.

| If the source... | Store it in | Label it | Consequence |
|---|---|---|---|
| Is accepted by a named authority and defines a condition work must meet | [authoritative/](authoritative/README.md) | `../../../evidence/authoritative` | Initiatives and products must align or record an approved exception/conflict. |
| Is an observation, example, research result, proposal input, recommendation, or unresolved interpretation | [non-authoritative/](non-authoritative/README.md) | `../../../evidence/non-authoritative` | It may inform a choice but cannot override binding evidence. |
| Is both useful context and a new rule | Store the observation as contextual evidence, then create a separately accepted authoritative record | Both, with linked IDs | The acceptance action—not the observation—creates the binding rule. |

Do not classify a source by its file extension or author alone. Classify the
specific claim and the authority that accepts it. A document may contain both a
quoted binding source and an author's non-binding interpretation; record the
distinction clearly.

## Set up the evidence library

1. Select the [evidence register source](../template/project/evidence/evidence-register.template.md)
   from the protected library and copy it to `evidence/evidence-register.md`
   when evidence needs a shared index. Edit only that destination. A small project
   may start with individual records, but create the register before sources
   become hard to discover.
2. Assign a stable ID such as `EVD-001` to every material source. Keep the ID
   when a source is revised; record the revision relationship rather than
   assigning a new identity to an unchanged concept.
3. Place the artifact or a durable record of its source in the appropriate
   class directory. Avoid placing credentials, personal data, huge generated
   exports, or unrelated working files here; link to an approved secure
   location if necessary.
4. Complete the record's owner, source, date, status, precise locator,
   classification, and limits. `A link to the evidence directory` is not a
   precise locator.
5. Add the row to the register and link every initiative or product that
   materially depends on the source.

## How to use the register template

The register is an inventory, not a replacement for the evidence itself.
Replace the leading placeholder rows with a row for each active source:

- **Evidence ID** is permanent and appears in initiatives, decisions, and
  product records.
- **Classification** is exactly `../../../evidence/authoritative` or
  `../../../evidence/non-authoritative`.
- **Artifact and precise locator** names a file, revision, heading, page,
  claim, or stable external reference.
- **Governs or informs** states the subject, not a vague label such as
  `architecture`.
- **Owner** is the source steward or accepting authority; use `Unknown` only
  with a follow-up owner and date.
- **Status** indicates whether the source is active, superseded, retired, or
  still under review.

Use the classification and conflict log for a material change in authority, a
contradiction, an expired source, or an explicit promotion from context to a
binding record. Do not log routine formatting edits that do not alter meaning.

## Cite evidence correctly

A useful citation lets another person find exactly the claim that matters.
Use a form such as `EVD-004, §2.3 “Retention”, revision 2026-10-30`, followed
by a path or link. In an initiative, state how the claim affects the scope,
specification, decision, or verification. In a product record, state which
behavior or release gate proves compliance.

When a source supports only a hypothesis, say so. For example: `OBS-003
suggests the retry limit may be too low; it is contextual evidence and does not
authorize a production change.` This prevents an exploratory study from being
mistaken for a mandate.

## Revision, preservation, and conflict workflow

1. Keep the original artifact unchanged whenever possible.
2. Add a new record or revision with its date, source, reason, and relationship
   to the earlier record.
3. Update the register and every active initiative or product that relies on a
   changed binding claim.
4. If two sources conflict, preserve both. Record the exact incompatible
   claims, their classifications, affected work, decision owner, and required
   resolution.
5. Block a product decision that conflicts with authoritative evidence until a
   named authority accepts a revision or exception.

## Review checklist

- [ ] Every active source has an ID, class, owner, date/revision, and locator.
- [ ] Each authoritative claim identifies what it governs and how it is
      verified.
- [ ] Contextual evidence states its limits and is not phrased as a mandate.
- [ ] Superseded sources remain discoverable with a successor link.
- [ ] Conflicts and unknown ownership have a named resolver and due date.
- [ ] Initiative and product citations point to a precise claim, not just this
      directory.
