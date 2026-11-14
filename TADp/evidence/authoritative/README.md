# Authoritative evidence

This directory is the home for binding evidence: records accepted by a named
authority that establish conditions initiatives and products must meet. It is
not a place to elevate a preference, a proposal, or a convenient product
implementation into a rule without review.

## What belongs here

| Record type | Use it for | Start with |
|---|---|---|
| General authoritative evidence | A bounded binding source that is neither an architecture record nor a rule | [authoritative-evidence.template.md](authoritative-evidence.template.md) |
| Architecture | Durable ownership boundaries, interfaces, and accepted technical decisions | [architecture/README.md](architecture/README.md) |
| Rules | Independently enforceable policies, standards, constraints, and acceptance conditions | [rules/README.md](rules/README.md) |

Choose the narrowest record type that fits. A broad policy should be split into
individual rules when different owners, scopes, exceptions, or verification
methods apply. An architectural record should be split when a component
boundary, interface contract, or decision can be reviewed and changed without
changing the other subjects.

## Admit a source as authoritative

Before using the generic template, confirm all of the following:

1. A named authority has accepted the source or is empowered to do so.
2. The record makes a clear normative claim: what must, must not, or is
   required to be true.
3. Its applicable scope and exclusions are known.
4. An initiative or product can verify compliance, or the record states why
   verification is not possible and how review will occur instead.
5. The original source, revision, effective date, and owner are preserved.

If any answer is unknown, store the material as
[non-authoritative evidence](../non-authoritative/README.md) until it is
accepted. `Potentially important` does not mean `binding`.

## Use the general evidence template

Copy [authoritative-evidence.template.md](authoritative-evidence.template.md)
to a stable filename such as `AUTH-001-identity.md`. Fill it in this order:

1. Assign the **Evidence ID** and name the accepting authority. IDs must remain
   stable across small clarifications and revisions.
2. Write a one-paragraph **binding statement** in plain language. It should say
   what the evidence requires, not merely where it came from.
3. Define **applicability** so a reviewer can tell which products, components,
   initiatives, or environments must comply and which are deliberately outside
   the record.
4. Break the statement into individually citable **claim IDs**. Each claim must
   have a verification or observation method.
5. State known ambiguities and conflicts rather than hiding them in a later
   implementation document.
6. Record source, revision, effective date, status, and any predecessor or
   successor. Remove the HTML instruction comment only after every placeholder
   has been resolved.

## How initiatives and products use these records

An initiative cites an evidence ID and claim ID, explains how the claim affects
its scope or specification, and records a conflict when it cannot comply. A
product record links the same claim to a behavior, test, audit, or operational
check. Do not copy a claim into an initiative and then let the copied text drift
from its authoritative source.

An initiative can interpret evidence for its stated work, but it cannot revise
the evidence. A product can reveal a conflict, but it cannot resolve the
conflict by itself. Route a needed change to the record's accepting authority.

## Revision and exception control

Preserve every active and superseded artifact. An authorized revision must:

- name the predecessor, reason, authority, and effective date;
- identify every active initiative or product affected by the change;
- update the evidence register and affected citations;
- state whether the revision applies immediately, has a migration period, or
  leaves historical products under an earlier rule; and
- retain the old record for audit and explanation.

An exception is not an undocumented mismatch. It needs its own owner, scope,
expiration or review date, compensating controls, and explicit approval.

## Review checklist

- [ ] The record has a named accepting authority and source/revision.
- [ ] Its binding claims, scope, exclusions, and verification are explicit.
- [ ] It lives in the correct specialization: general, architecture, or rules.
- [ ] Active initiatives and products cite precise claim IDs.
- [ ] Changes, conflicts, and exceptions preserve prior evidence and name an
      owner.
