# TADp demonstrator HIPAA-aligned security policy suite

**Suite ID:** `SEC-HIPAA-SUITE-001`  
**Revision:** `1.0.0`  
**Status:** Accepted prospective policy  
**Owner and accepting authority:** User, project authority  
**Technical author:** Codex  
**Effective date:** 2026-11-10  
**Primary evidence:** [`ARC-SUITE-001@2.0.0`](../../architecture/00-architecture-suite-index.md)  
**Authority record:** [`SEC-HIPAA-AUT-001`](01-authority-scope-and-source-basis.md)  
**Applicable peer security baseline:** [`SEC-NIST-SUITE-001@1.0.0`](../NIST/00-nist-security-policy-suite-index.md)  

## Purpose and standing

This suite is the binding, limited-scope security policy for **future
development** of the TADp example record application. It adapts selected
requirements of the currently effective HIPAA Security Rule to the accepted
local, single-user demonstrator architecture. It governs future initiative
specifications, product design, implementation, test evidence, release
instructions, and operational documentation for delivery units `D2` through
`D6`.

This suite is prospective. It does **not** inspect or validate an existing
implementation, assert that a product exists, establish that any control is
implemented, certify HIPAA compliance, or authorize use of electronic
protected health information (`ePHI`). Future work may claim conformance to a
policy only after its governing initiative produces the evidence required by
this suite and by [`ARC-CTR-009`](../../architecture/24-conformance-contract.md).

The requested directory is named `HIPPA`; the documents use the legally
correct acronym **HIPAA** (Health Insurance Portability and Accountability
Act).

## Accepted demonstrator profile

The only profile governed by this revision is:

- local, single-user operation under one authorized host operating-system
  account;
- Docker Compose as the only supported application runtime;
- exact IPv4-loopback browser ingress and a private Compose network;
- no application accounts, roles, sessions, credentials, remote access,
  proxy, tunnel, or public/LAN exposure;
- synthetic data or data whose de-identification has been documented outside
  the application under an accepted HIPAA method; and
- prospective development and verification, not a regulated production
  deployment.

Possible or actual ePHI, multiple users, remote access, shared workstations,
production clinical use, treatment or payment workflows, and public or
multi-tenant deployment are outside this suite. They are blocked by the
successor-architecture gate in `HSP-015`.

## Evidence and authority order

Apply the following order within this suite's scope:

1. the repository's [Codex invariant suite](../../LLM/00_Codex_Invariant_Suite_Index.md);
2. the accepted example-app architecture, beginning with
   [`ARC-SUITE-001`](../../architecture/00-architecture-suite-index.md) and
   [`AUTH-EX-001`](../../architecture/01-accepted-architecture-baseline.md);
3. the applicable accepted security suites—
   [`SEC-NIST-SUITE-001`](../NIST/00-nist-security-policy-suite-index.md) and
   this suite—applied together without silently ranking one peer suite over
   the other;
4. accepted, narrowly scoped future initiative specifications; and
5. product and verification evidence produced under those specifications.

The architecture is the primary evidence for system shape, trust boundaries,
data flow, exclusions, and verification ownership. The HIPAA regulation and
official HHS guidance cited in this suite justify why the selected safeguards
are included. This policy may add a stricter development or use gate, but it
does not silently revise an architecture component or authorize a product.
The NIST suite remains binding for its scope; the cross-suite mapping in
[`SEC-HIPAA-MAP-001`](03-control-rationale-and-traceability.md#cross-suite-compatibility)
shows how the requirements are intended to operate together.

## Suite catalog and reading order

| Order | ID | Record | Purpose |
|---:|---|---|---|
| `00` | `SEC-HIPAA-SUITE-001` | **This index** | Establishes standing, profile, precedence, and navigation |
| `01` | `SEC-HIPAA-AUT-001` | [Authority, scope, and source basis](01-authority-scope-and-source-basis.md) | Preserves the human instruction, source status, legal baseline, and exclusions |
| `02` | `SEC-HIPAA-POL-001` | [Prospective security policy](02-prospective-security-policy.md) | Defines the complete set of in-scope normative policies `HSP-001` through `HSP-015` |
| `03` | `SEC-HIPAA-MAP-001` | [Control rationale and traceability](03-control-rationale-and-traceability.md) | Justifies every policy with precise architecture and HIPAA sources |
| `04` | `SEC-HIPAA-DEV-001` | [Future development and evidence standard](04-future-development-and-evidence-standard.md) | Converts the policies into initiative, delivery, and verification obligations |
| `05` | `SEC-HIPAA-GATE-001` | [Regulated-use successor gate](05-regulated-use-successor-gate.md) | Records architecture-declared limits that block ePHI and the authority needed to change them |

## Normative language

`Must`, `must not`, `required`, and `may only` are binding for future work in
scope. `Should` states the expected safeguard unless a documented,
invariant-compatible risk analysis supports another measure. `May` grants
permission only within the accepted demonstrator profile.

A HIPAA implementation specification labelled **addressable** is not treated
as optional. Future work must assess it, implement it when reasonable and
appropriate, or document why it is not reasonable and appropriate and use an
equivalent alternative measure when reasonable and appropriate, as required
by [45 CFR 164.306(d)(3)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306).

## Explicit limitations

- This suite covers only safeguards with a direct relationship to the example
  application's architecture, development, local operation, data, or delivery
  evidence. It is not an organization-wide HIPAA manual.
- It does not determine whether a person or organization is a covered entity
  or business associate.
- It does not replace the HIPAA Privacy Rule, Breach Notification Rule,
  business-associate obligations, state law, contractual duties, or legal
  advice.
- It does not approve real patient data merely because a developer labels a
  fixture "de-identified." De-identification requires the external evidence
  described in `HSP-002`.
- It does not claim that the architecture alone satisfies HIPAA. Architecture
  is a design authority; product controls and organizational practices still
  require implementation and evidence.
- The January 2025 Security Rule changes remain a notice of proposed
  rulemaking in the official HHS material reviewed for this revision. This
  suite uses the Security Rule currently in effect and requires a source
  currency review before future acceptance or release.

## Policy ownership and change control

Every future initiative affecting `D2` through `D6` must cite the applicable
`HSP-*` policies and their exact rationale entries. A policy requirement may
be tightened by a future initiative but may not be weakened or treated as
implemented without evidence.

A change to this suite requires explicit project-authority instruction,
review of the current HIPAA source text, impact analysis against every linked
architecture record and active initiative, preservation of this revision,
and a successor or revision relationship. A request to implement, test,
align, or make a product pass is not authority to revise this policy.

