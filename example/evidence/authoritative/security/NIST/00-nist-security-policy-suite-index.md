# TADp demonstrator NIST-aligned security policy suite

**Suite ID:** `SEC-NIST-SUITE-001`  
**Revision:** `1.0.1`  
**Status:** Accepted future-development policy  
**Owner and accepting authority:** User, project authority  
**Effective date:** 2026-11-10  
**Architecture input:** [`ARC-SUITE-001@2.0.1`](../../architecture/00-architecture-suite-index.md)  
**Applicable peer security baseline:** [`SEC-HIPAA-SUITE-001@1.0.1`](../HIPPA/00-hipaa-security-policy-suite-index.md)  
**Supersedes:** `SEC-NIST-SUITE-001@1.0.0` at Git commit `82bd147`  
**Policy profile:** Local, single-user, Docker Compose demonstrator  

## Purpose and standing

This suite is the binding, limited-scope future-development security policy for
the example record application used as the TADp demonstrator. It establishes a
focused NIST-aligned policy, control-tailoring profile, and future assurance
plan. The architecture describes the current technical design under review;
this suite remains the primary invariant for its security, permitted-use,
review, and assurance scope and guides that architecture.
The NIST publications in the [source register](04-nist-source-register.md)
justify the security outcomes selected for that architecture.

This suite is intentionally smaller than the NIST Cybersecurity Framework,
the NIST Risk Management Framework, or a NIST SP 800-53 control baseline. It
does not establish federal authorization, FISMA compliance, an authorization
to operate, NIST certification, or complete implementation of any NIST
publication. It does not assess or validate the current demonstrator
implementation. A future product may claim conformance to this suite only
after the required evidence in
[`SEC-NIST-VER-001`](03-future-development-assurance.md) exists.

## Development posture

This suite states requirements for work performed after its acceptance. The
architecture invariant supplied factual input for initial scope selection; it
is not authority to narrow the accepted policy and is not implementation
evidence. Source code, images,
configurations, tests, scans, backups, operations, and releases are **not
assessed** by this suite, and no current pass, failure, or conformance result is
recorded here.

`SEC-NIST-VER-001` is a prospective evidence specification. It tells future
developers and reviewers what evidence an implementation would have to produce
before making a narrowly scoped claim. Creating that specification does not
assert that the evidence or implementation already exists.

## Human authorization captured

The User instructed Codex on 2026-11-10:

> create a limited scope NIST aligned security policy for the TADp demonstrator
> app. use the architecture invariant as primary evidence. The policy does not
> need to include every NIST protocol, limit only to areas relevant to the
> example app. Place the policy document suite in the NIST folder. Be certain
> to justify every policy with existing, documented NIST guidelines and
> protocols.

The User clarified on 2026-11-10:

> right - these policies guide future development, not validate existing work

That instruction authorizes creation and acceptance of this project-specific
future-development suite in the repository's authoritative security hierarchy.
The clarification controls its interpretation: this is a policy baseline, not
a current-state assessment. The instructions do not authorize alteration of
the architecture suite, the Codex invariant suite, or any protected source.

The User subsequently instructed Codex on 2026-11-10 to reconcile the files
according to the recorded findings and make the changes in place. That
instruction authorizes this coordinated patch revision with architecture
`2.0.1` and HIPAA policy `1.0.1`. It does not authorize a product-behavior
change, implementation, use of prohibited data, or a compliance claim.

The User then clarified that the security policy must remain the primary
invariant guiding both the architecture and realization note, not be changed to
match them. This controls the reconciliation: revision `1.0.1` changes
cross-references and makes precedence explicit, but does not weaken, replace,
or retarget any `SEC-POL-*` requirement.

## Authority and interpretation

Apply sources in this order for this suite's scope:

1. the repository evidence protocol and any explicit accepted revision;
2. this suite and the applicable HIPAA suite, applied together as the primary
   security invariants without using either to weaken the other;
3. the active example application architecture as a constrained technical
   design record, especially
   [`AUTH-EX-001`](../../architecture/01-accepted-architecture-baseline.md),
   [`ADR-004`](../../architecture/07-ADR-004-container-only-deployment-trust-model.md),
   and
   [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md);
4. accepted, narrowly scoped initiative specifications; and
5. implementation, test, scanner, and operational evidence.

NIST publications supply documented security guidance and control outcomes;
they do not silently revise the accepted system architecture. When broad NIST
guidance presumes enterprise identity, remote networking, regulated data,
continuous monitoring, or organizational programs that the demonstrator does
not have, the disposition in
[`SEC-NIST-MAP-001`](02-nist-control-tailoring-profile.md) governs this limited
profile. Expanding the application so a tailored-out control becomes relevant
requires an accepted successor architecture and security-policy revision.

An implementation convenience, scan result, generated configuration, or NIST
crosswalk cannot weaken either the architecture or this suite. Any discovered
contradiction must follow the repository's
[invariant-conflict process](../../LLM/03_Codex_Invariant_Conflict_Register.md).

## System and data scope

This suite applies prospectively to:

- the local example record application at architecture revision `2.0.1`;
- the `record-api`, `record-cli`, `record-maintenance`, and isolated
  `record-test` container roles;
- the embedded same-origin browser application, Python SDK artifact, private
  Compose network, and Docker named volumes;
- the source, BuildKit graph, OCI images, release Compose material, SBOM,
  provenance, dependencies, configuration, logs, backups, and recovery
  procedures that deliver those roles; and
- future product initiatives that claim conformance to the demonstrator
  architecture or this policy.

The approved information scope is non-production demonstration and test data.
Operators must not intentionally place credentials, authentication material,
regulated data, confidential business data, production records, or data whose
loss or disclosure would require controls outside this profile into the
application. Record content is nevertheless treated as sensitive-by-default
for logging, diagnostics, backups, and incident preservation.

## Explicit exclusions

The suite does not approve or govern:

- LAN, Internet, public, tunneled, proxied, or other remote access;
- multiple users, application accounts, roles, sessions, or per-user audit;
- TLS termination, an identity provider, secrets management, or a reverse
  proxy for application traffic;
- production, regulated, safety-critical, high-impact, or multi-tenant use;
- a fixed availability objective, disaster-recovery objective, failover, or
  high availability;
- enterprise SIEM, endpoint detection, network intrusion detection, or a
  security operations center;
- organizational personnel, physical, procurement, legal, training, or
  privacy-program controls outside the demonstrator product boundary; or
- a complete NIST SP 800-53B baseline, full RMF package, penetration-test
  program, cryptographic-module validation, or federal authorization package.

These are deliberate tailoring decisions, not evidence that the associated
risks do not exist. The triggers that invalidate each exclusion are recorded
in `SEC-NIST-MAP-001`.

## Relationship to RZN-001 and the HIPAA suite

[`RZN-001`](../../../non-authoritative/realizations/v0/RZN-001-example-record-application.md)
is historical, non-authoritative intent evidence. Its generic record model and
previously open security/deployment question do not authorize credentials,
confidential or production data, regulated data, actual or possible ePHI, or a
boundary excluded here. Architecture `2.0.1` owns the system decisions; this
suite and `SEC-HIPAA-SUITE-001@1.0.1` own their respective security, data-use,
and evidence gates. Future work must satisfy all applicable gates for the same
artifact and claim.

## Document catalog

| Order | ID | Document | Purpose |
|---:|---|---|---|
| `00` | `SEC-NIST-SUITE-001` | **This index** | Establishes authority, scope, precedence, limitations, and navigation |
| `01` | `SEC-NIST-POL-001` | [Demonstrator security policy](01-demonstrator-security-policy.md) | States the binding security requirements that architecture and product work must satisfy and gives a NIST justification for every policy |
| `02` | `SEC-NIST-MAP-001` | [NIST control tailoring profile](02-nist-control-tailoring-profile.md) | Maps selected NIST outcomes to the policy and records why other control areas are outside this profile |
| `03` | `SEC-NIST-VER-001` | [Future development assurance and evidence standard](03-future-development-assurance.md) | Defines the evidence and assessment methods future work must satisfy; records no current results |
| `04` | `SEC-NIST-SRC-001` | [NIST source register](04-nist-source-register.md) | Preserves official source identities, versions, locators, and maintenance rules |

## Normative language

`Must`, `must not`, `required`, and `may only` are binding. `Should` expresses
the expected practice unless an explicit, evidence-backed, policy-compatible
disposition records why it is inapplicable. `May` grants permission
only inside the stated boundary.

NIST control identifiers in this suite are alignment references. A mapping
means that a policy was selected because it supports the cited NIST outcome;
it is not, by itself, evidence that the full control or every control
enhancement is implemented.

## Review and change control

The project architecture authority must review this suite at least for each
demonstrator architecture major revision, any change to the trust or data
boundary, and any relevant final NIST publication update. Review does not
silently incorporate new external text. A semantic policy change requires an
explicit User or later named-authority instruction, impact analysis, a new
suite revision or successor, updated control and verification mappings, and
preservation of the earlier accepted meaning.

Remote exposure, application identity, sensitive-data approval, encryption
requirements, multi-user operation, production use, or a formal compliance
claim always requires a successor security architecture; it cannot be approved
as an informal exception to this limited profile.

## Revision record

| Date | Revision | Change | Authority |
|---|---|---|---|
| 2026-11-10 | `1.0.0` | Established the limited NIST-aligned future-development policy | User's NIST policy instruction and clarification |
| 2026-11-10 | `1.0.1` | Made policy primacy explicit and reconciled cross-references to architecture 2.0.1, HIPAA 1.0.1, and RZN-001; no policy outcome changed | User's explicit reconciliation instruction and policy-primacy clarification |
