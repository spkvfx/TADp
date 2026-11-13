# RZN-001 architecture and security reconciliation record

- **Assessment ID:** `REC-RZN-001-001`
- **Status:** Applied
- **Recorded date:** 2026-11-10
- **Classification:** Non-authoritative reconciliation evidence
- **Input baseline:** `ARC-SUITE-001@2.0.0`, `SEC-NIST-SUITE-001@1.0.0`, `SEC-HIPAA-SUITE-001@1.0.0`, and `RZN-001`
- **Applied baseline:** `ARC-SUITE-001@2.0.1`, `SEC-NIST-SUITE-001@1.0.1`, `SEC-HIPAA-SUITE-001@1.0.1`, and annotated `RZN-001`
- **Input repository snapshot:** Git commit `95f2b01`
- **Initial assessment commit:** Git commit `5f0c325`

> **Standing:** This non-authoritative record preserves the comparison and
> identifies where its findings were applied. The User's explicit in-place
> reconciliation instruction—not this record—authorized the coordinated patch
> revisions. The authoritative records retain ownership of every binding claim;
> this record does not authorize implementation or establish conformance.

## Requested reconciliation

This assessment addresses three comparisons:

1. the accepted architecture invariant against the NIST- and HIPAA-aligned
   security policy invariants;
2. the v0 realization note against the accepted architecture invariant; and
3. the v0 realization note against both security policy invariants.

The original request and historical candidate wording in
[`RZN-001`](../realizations/v0.0/RZN-001-example-record-application.md) remain
preserved. The User later explicitly authorized source-preserving in-place
annotations, so that note now points readers to the authoritative dispositions
without becoming an accepted specification.

## Source standing and precedence

| Source | Standing in this comparison | Permitted use |
|---|---|---|
| [Codex invariant suite](../../authoritative/LLM/00_Codex_Invariant_Suite_Index.md) | Governing evidence protocol | Controls precedence, contradiction handling, source preservation, and future initiative use |
| [`ARC-SUITE-001@2.0.1`](../../authoritative/architecture/00-architecture-suite-index.md) | Accepted project architecture invariant constrained by the security policies | Owns technical system shape, contracts, exclusions, delivery units, and conformance vectors inside the policy boundary |
| [`SEC-NIST-SUITE-001@1.0.1`](../../authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Primary future-development security invariant for its scope | Governs the limited NIST-aligned security requirements and evidence gates applicable to the architecture and realization |
| [`SEC-HIPAA-SUITE-001@1.0.1`](../../authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Primary prospective security invariant for its scope | Governs the limited HIPAA-aligned data-use, safeguard, documentation, and successor-architecture gates applicable to the architecture and realization |
| [`RZN-001`](../realizations/v0.0/RZN-001-example-record-application.md) | Non-authoritative realization input, now annotated with current owners | Preserves requested outcomes, candidate sequencing, risks, assumptions, and questions; cannot override any invariant |

The two security suites together are the primary security invariants within
their stated scopes and guide both the architecture and realization. They are
not changed to fit either document. When both apply, future work must satisfy
both; the stricter compatible gate controls the bounded claim. An incompatible
technical design requires an authorized architecture successor, not a weaker
policy.

## 1. Architecture invariant to security policy invariants

### Reconciliation matrix

| Concern | Architecture invariant | Security policy invariants | Reconciled interpretation |
|---|---|---|---|
| Standing and current-state claims | [`ARC-SUITE-001`, Purpose](../../authoritative/architecture/00-architecture-suite-index.md#purpose-and-standing) and [`ARC-CTR-009`, Current evidence status](../../authoritative/architecture/24-conformance-contract.md#current-evidence-status) specify future behavior and record no D2-D6 implementation claim | NIST suite **Development posture**, `SEC-NIST-VER-001`, `HSP-001`, and `SEC-HIPAA-DEV-001` are prospective and record no present control result | Architecture and policy are requirements, not implementation, release, compliance, or certification evidence |
| Supported use and data | [`AUTH-EX-001.6/.9`](../../authoritative/architecture/01-accepted-architecture-baseline.md#binding-claims) define local, single-user, unauthenticated operation and exclude remote, accounts, and audit history; `ARC-CTR-001` treats full names and values as sensitive by default | `SEC-POL-01` permits only non-production demonstration/test records; `HSP-002` permits only purpose-created synthetic data or externally documented de-identified data and preserves the NIST prohibitions | The security suites narrow permitted use without changing the three-field record schema. Actual, possible, or insufficiently classified ePHI and any data requiring omitted controls are outside the accepted profile |
| Human identity and access | [`ADR-004`, Application identity boundary](../../authoritative/architecture/07-ADR-004-container-only-deployment-trust-model.md#application-identity-boundary) uses the authorized host OS account and Docker access; the app has no accounts, roles, login, or sessions | `SEC-POL-01` through `03` preserve that trust boundary; `HSP-004` requires one named authorized person, a unique OS account, restricted Docker authority, and truthful documentation of the missing app identity layer | Host/OS/Docker controls are inherited dependencies for this non-ePHI profile, not application authentication. Multi-user, shared-account, or regulated use requires a successor architecture |
| Network and transmission | [`AUTH-EX-001.6`](../../authoritative/architecture/01-accepted-architecture-baseline.md#binding-claims), `ADR-004`, `ARC-CTR-002`, and `ARC-CTR-008` require IPv4 loopback publication, private Compose networking, exact Host/Origin checks, shared `/api/v1`, HTTP, and no proxy/CORS/remote path | `SEC-POL-02` and `HSP-005` require the same topology and negative reachability evidence; both route remote or regulated transmission to a TLS/identity/proxy successor design | HTTP is accepted only inside the local non-ePHI profile. The security policies do not retrofit TLS into v2 or authorize remote exposure |
| State ownership and integrity | [`AUTH-EX-001.1/.5/.12`](../../authoritative/architecture/01-accepted-architecture-baseline.md#binding-claims), `ADR-001`, and `ARC-CTR-004` require API-exclusive live SQLite, conditional updates, named volumes, and stopped-API networkless maintenance | `SEC-POL-05` and `HSP-007` adopt the same ownership, transaction, lock, integrity, migration, and restore rules | There is one normal live-state authority. Security requirements add evidence and release gates, not an alternate database path |
| Client and browser data handling | `ARC-CTR-005` through `ARC-CTR-007` prohibit direct state access, unsafe retry, durable browser record storage, third-party content, cross-origin traffic, and client-owned search meaning | `SEC-POL-06/08` and `HSP-006/008` add minimum-data, safe presentation, diagnostic, and collaboration-artifact restrictions | Explicit success output may contain the requested in-profile record, but logs, diagnostics, URLs, process metadata, browser storage, telemetry, and evidence artifacts must not amplify record content |
| Logging and audit | [`ARC-CTR-008`, Logging and diagnostics](../../authoritative/architecture/23-operations-security-contract.md#logging-and-diagnostics) defines bounded redacted diagnostics and expressly rejects an audit/recovery claim | `SEC-POL-08` and `HSP-008` preserve that limitation and require review procedures without claiming per-user attribution | Diagnostic correlation is required; a HIPAA audit-control, non-repudiation, or per-user activity claim is prohibited in this profile |
| Containers, configuration, and supply chain | `AUTH-EX-001.13`, `ADR-005`, and `ARC-CTR-008` require non-root/read-only containers, least privilege, immutable identities, locked inputs, SBOM/provenance, bounded resources, and finding disposition | `SEC-POL-03/04/10/12` and `HSP-009` make those architecture controls future security and release gates | One set of artifacts and effective Compose settings can support both security suites only when exact evidence satisfies each mapped claim |
| Backup, recovery, and emergency handling | `ARC-CTR-004` and `ARC-CTR-008` require offline validated backup/restore, separate volumes, preserved prior state, and explicit host-loss limitations | `SEC-POL-09` and `HSP-010/011` preserve that mechanism and add criticality, custody, media, encryption-decision, and drill records | The opaque backup path remains recovery, not record import/export. Same-host backup does not prove host-loss recovery, and any off-volume copy inherits the source data restrictions |
| Incident response | `ARC-CTR-008` defines stop, preserve, hash, recover, and reverify behavior while disclaiming remote response and per-user attribution | `SEC-POL-13` and `HSP-012` add owners, incident records, exercises, possible-PHI escalation, and organization responsibilities | The architecture owns technical containment/recovery; the security suites add governance and escalation without claiming the app decides legal notification |
| Verification and claims | `ARC-CTR-009` owns product vectors, D1-D6 gates, exact artifact/environment identity, and truthful limitations | `SEC-NIST-VER-001`, `SEC-HIPAA-DEV-001`, `SEC-POL-11`, and `HSP-014` add policy mappings, risk/source reviews, records, and narrow claim language | A future claim must pass the architecture gate and every applicable NIST/HIPAA gate. Passing one evidence set cannot substitute for another or establish general compliance |
| Exceptions and boundary expansion | `ADR-006`, `ADR-004`, and `ARC-CTR-008` require explicit authority and a successor for remote, multi-user, identity, TLS/proxy, audit, privacy, or materially different deployment | `SEC-POL-14` allows only invariant-compatible bounded risk dispositions; `HSP-015` provides no exception that permits actual or possible ePHI in the current profile | No exception can waive policy or architecture. Policy controls its security/use scope; an incompatible design requires a separately accepted architecture successor. The no-ePHI gate remains binding for ePHI, production clinical use, remote access, shared workstations, or third-party record processing |

### Architecture-security result

No direct contradiction was found between `ARC-SUITE-001@2.0.1`,
`SEC-NIST-SUITE-001@1.0.1`, and `SEC-HIPAA-SUITE-001@1.0.1` for the accepted
local demonstrator profile. The security suites explicitly use the architecture
as technical input, but remain the primary invariants for their security and
permitted-use scopes. They guide the architecture and `RZN-001`, preserve the
compatible component and trust boundaries, and impose the controlling
future-development, allowed-use, review, and evidence gates.

The accepted architecture is **not** suitable for actual or possible ePHI,
regulated production, multiple users, shared identities, or remote access.
That statement is a preserved limitation, not an architecture defect silently
repaired by policy text.

## 2. V0 realization note to architecture invariant

[`ARC-AUT-001`](../../authoritative/architecture/02-authority-and-source-disposition.md)
already owns the authoritative disposition of every `RZN-001-Q01` through
`RZN-001-Q17`. The summary below records how future consumers must interpret
the remaining apparent differences.

| `RZN-001` subject | Accepted architecture disposition | Reconciliation result |
|---|---|---|
| Three-field record and create/edit behavior | `ARC-CTR-001`, `ADR-002`, and `ARC-CTR-002` fix canonical UUIDv4, name/value normalization, immutability, ETags, and conditional update | The requested outcome is retained; unresolved field and update details are no longer decision authority |
| Next/previous and search (`Q05`-`Q08`) | `ADR-002`, `ADR-003`, and `ARC-CTR-003` fix ordinal order, boundaries, context ceilings, one predicate, NFC/case rules, and bounded RE2 semantics | The realization's broad capabilities are preserved under one accepted deterministic API contract |
| Direct SQLite versus API access (`Q10`-`Q11`) | `ADR-001` requires API-exclusive live persistence; CLI uses the SDK and browser uses a thin adapter against the identical `/api/v1` route set | The realization's possible direct-SQL and shared-lower-layer options are rejected alternatives, not continuing options |
| SDK and technology (`Q09`, `Q12`) | `ADR-005`, `ARC-BND-004`, and `ARC-CTR-005` select the container-built synchronous Python/Pydantic/HTTPX SDK and accepted application stack | The realization's unspecified packaging/framework choices are superseded for architecture v2 by accepted decisions |
| Standalone CLI | `ARC-BND-005` and `ARC-CTR-006` define a one-shot independently versioned Compose image that uses the SDK and mounts no state | "Standalone" means independently runnable container artifact, not host binary, offline service, or embedded SQLite |
| Deployment, security, privacy, logging, accessibility, backup (`Q13`) | `ADR-004`, `ARC-CTR-007`, `ARC-CTR-008`, and the security suites own these concerns | The realization remains the source of the question; accepted invariant records own the answer |
| Excluded capabilities (`Q14`) | `AUTH-EX-001.9` excludes delete, bulk mutation, record import/export, history, accounts, remote multi-user use, and offline writes | Opaque maintenance backup transport remains recovery and does not reintroduce an excluded record feature |
| Evidence and feedback (`Q15`-`Q16`) | `ARC-CTR-009` defines conformance; `ADR-006` defines preserved revisions and implementation-feedback governance | Implementation cannot rewrite the contract, and no product claim exists without exact initiative evidence |
| SDK/API cohesion and product sequence (`Q17`) | `ADR-007` splits the candidate four-product sequence into D1-D6, separates API from SDK, adds the Docker platform unit, and preserves CLI-before-web delivery sequencing | The later explicit Docker instruction and narrow-scope invariant refine the candidate sequence without changing the realization's historical wording |

### Realization-architecture result

The v0 realization is compatible as historical proposal input. Its open
questions and candidate alternatives must not be presented as still governing
architecture v2. `ARC-AUT-001` is the complete accepted disposition register,
and `ADR-007` is the accepted delivery decomposition. The realization now
contains source-preserving reconciliation annotations while its original
request and historical uncertainty remain recoverable.

## 3. V0 realization note to security policy invariants

| `RZN-001` subject | Security-policy disposition | Future consumer rule |
|---|---|---|
| Generic `name` and free-text `value` | `SEC-POL-01`, `HSP-002`, and `HSP-006` restrict permitted content and secondary copies | Capability to store text is not authority to store secrets, production data, confidential business data, regulated personal data, or possible ePHI |
| Candidate create/edit/search/navigation flows | NIST and HIPAA policies retain the flows but require safe validation, bounded resources, integrity, minimum data, and redacted diagnostics | Tests, examples, screenshots, demonstrations, backup drills, and evidence use purpose-created synthetic data or the exact documented de-identification path allowed by `HSP-002` |
| Authentication, authorization, privacy, logging, and deployment question `Q13` | The accepted profile has no app identity, roles, sessions, TLS, audit ledger, remote access, or regulated-use approval; OS/Docker and loopback/private confinement are the limited trust boundary | Future documentation must state these absences. Adding one partial control does not authorize an excluded deployment |
| Product 1 documentation intent | Architecture and both security suites now own the accepted contracts and security requirements | Derivative documentation must cite exact invariant IDs and must not restate a realization candidate as authority |
| Candidate executable products | NIST policy applies to future design and delivery; HIPAA policy and `SEC-HIPAA-DEV-001` apply to D2-D6 | Each narrow initiative must map its owned delivery unit to applicable `SEC-POL-*`, `HSP-*`, architecture vectors, data/fixture plan, risk owner, and exact evidence |
| CLI/web feature parity | `SEC-POL-02/06/08` and `HSP-004/005/006/008` preserve the shared API while constraining network, output, storage, and diagnostics | Parity covers accepted record behavior, not an alternate state path or a right to expose sensitive data through every surface |
| Security, resource, observability, recovery candidate documentation | `SEC-NIST-POL-001`, `SEC-HIPAA-POL-001`, and their evidence standards now supply binding requirements | The realization's general recommendation is consumed; it cannot narrow or replace the accepted policy detail |
| Candidate outcome and suggested next steps | Security conformance remains prospective and current product status is not assessed | Product-specific realizations and proposals must carry the security limitations forward and must not claim implementation, release readiness, NIST certification, HIPAA compliance, or ePHI authorization |
| Expanded or regulated use | `SEC-POL-14`, `HSP-015`, and `SEC-HIPAA-GATE-001` stop affected work before implementation | Actual/possible ePHI, production clinical use, remote or multi-user access, shared workstations, third-party record processing, or formal compliance claims require successor authority and design |

### Realization-security result

`RZN-001` does not contradict either security invariant because it records a
requested capability set, labels security and deployment as unresolved, and
expressly disclaims specification authority. Its generic data model and
candidate flows are now usable only inside the narrower, authoritative
non-production, local, single-user, synthetic/documented-de-identified profile.

## Application record

The User instructed Codex on 2026-11-10 to reconcile the files according to
these findings and make the changes in place. The findings were applied as
follows:

The User then clarified that the security policy must remain the primary
invariant guiding both the architecture and realization note, not be changed to
match them. That clarification controls the applied precedence below.

| Applied source | Result |
|---|---|
| Architecture suite | Patch revision `2.0.1`; makes the primary security-policy boundary controlling for allowed data/use, safeguards, review, and evidence; adds additive D1-D6 gates and successor triggers without changing product behavior |
| NIST suite | Patch revision `1.0.1`; records policy primacy, architecture `2.0.1` as constrained technical input, HIPAA `1.0.1`, and RZN-001's non-authoritative role; no `SEC-POL-*` outcome changed |
| HIPAA suite | Patch revision `1.0.1`; records policy primacy, architecture `2.0.1` as constrained technical input, NIST `1.0.1`, and RZN-001's non-authoritative role; no `HSP-*` outcome changed |
| `RZN-001` | Historical request text retained and annotated with current authoritative owners, resolved-question groups, permitted data/use profile, and D1-D6 handoff |
| This record | Retained at the User's request and updated from assessment status to an applied-change record |

No protected template or Codex-invariant source was changed, no product
implementation was assessed, and no policy conformance result was created.

## Conflict-register disposition

No entry is added to the
[Codex invariant conflict register](../../authoritative/LLM/03_Codex_Invariant_Conflict_Register.md)
by this assessment. No pair of applicable binding claims was found to require
incompatible behavior. Differences involving `RZN-001` are dispositions of a
lower-standing unresolved source, not invariant conflicts.

If later evidence identifies an exact incompatible binding claim, the affected
work must stop and the conflict must be recorded with precise source locators;
this assessment must not be used to suppress that future record.

## Reconciled consumption rules

Future proposals and initiatives consuming `RZN-001` must:

1. cite `RZN-001` only for requested intent and historical context;
2. use `ARC-SUITE-001@2.0.1` and `ARC-AUT-001` for accepted system and source
   dispositions;
3. apply `SEC-NIST-SUITE-001@1.0.1` and
   `SEC-HIPAA-SUITE-001@1.0.1` together for every applicable future claim;
4. retain the local, single-user, non-production, non-ePHI boundary and the
   exact successor triggers;
5. follow the D1-D6 decomposition and create separately governed narrow
   initiatives rather than revive the four candidate products as one umbrella
   scope;
6. map each requirement to exact architecture vectors and security evidence,
   with synthetic/de-identification, risk, inherited-control, and source-
   currency records where applicable; and
7. preserve the distinction among policy, implementation, verified
   conformance, release approval, and organization-level compliance.

## Assessment limitations

- No implementation, image, Compose configuration, source tree, test, scan,
  backup, host, or release was assessed.
- No NIST, HIPAA, product-conformance, regulated-use, or compliance result is
  created by this record.
- External security and legal sources remain subject to the review rules in
  their authoritative suites.
- This record does not independently authorize further edits, initiative
  acceptance, implementation, release, deployment, or merge. The applied
  source revisions rely on the separately recorded explicit User instruction.
