# TADp demonstrator security policy

**Policy ID:** `SEC-NIST-POL-001`  
**Revision:** `1.0.1`  
**Status:** Accepted future-development policy  
**Owner and accepting authority:** User, project authority  
**Effective date:** 2026-11-10  
**Governing suite:** [`SEC-NIST-SUITE-001`](00-nist-security-policy-suite-index.md)  
**Architecture input:** [`ARC-SUITE-001@2.0.1`](../../architecture/00-architecture-suite-index.md)  
**Applicable peer policy:** [`SEC-HIPAA-SUITE-001@1.0.1`](../HIPPA/00-hipaa-security-policy-suite-index.md)  

## Reconciliation standing

This revision applies together with architecture `2.0.1` and HIPAA policy
`1.0.1`. This policy remains the primary invariant for its NIST-aligned
security outcomes and guides the architecture; the HIPAA suite independently
owns its additional data-use, safeguard, and successor gates.
[`RZN-001`](../../../non-authoritative/realizations/v0.0/RZN-001-example-record-application.md)
is intent history only and cannot relax any requirement. When HIPAA policy is
applicable, only purpose-created synthetic data or externally documented
de-identified data is permitted, and the independent NIST prohibitions on
credentials, confidential business data, production records, regulated data,
and data requiring omitted controls still apply.

## Purpose

This policy establishes the minimum security behavior for design, build,
release, local operation, maintenance, and recovery of the TADp demonstrator's
example record application. Each policy below identifies the accepted
architecture evidence and the documented NIST guidance that justifies the
requirement. Detailed source identities are maintained in
[`SEC-NIST-SRC-001`](04-nist-source-register.md).

The policy governs future design and delivery. It neither validates nor records
the state of the existing demonstrator. It does not claim that a conforming
implementation, image, scan, test, backup, or release currently exists.

## Roles

| Role | Security responsibility |
|---|---|
| Project architecture authority | Accepts architecture or policy changes and any bounded risk disposition that the governing evidence permits |
| Product or release owner | Implements this policy, maintains traceability, supplies verification, and blocks unsupported release claims |
| Component owner | Implements and tests the requirements owned by the API, persistence, SDK, CLI, web, or platform boundary |
| Local operator | Protects host and Docker access, uses only accepted lifecycle commands, safeguards exported backups, and performs local response/recovery |
| Reviewer | Examines the exact release evidence and reports nonconformance without converting missing evidence into a pass |

No role may approve a result that contradicts the architecture. A risk
disposition can address a finding only when the current invariant permits the
selected outcome; it cannot waive an invariant.

## `SEC-POL-01` - Authorized use and information boundary

### Policy

- The application may be used only as a local, single-user demonstrator with
  non-production demonstration or test records.
- Operators must not intentionally store credentials, authentication tokens,
  secrets, regulated personal data, confidential business data, production
  records, or other information requiring access, encryption, retention,
  deletion, audit, or reporting controls absent from this profile.
- The release documentation must state these limitations and must not present
  the application as suitable for production, regulated, remote, or multi-user
  use.
- A proposed expansion of purpose, actors, data sensitivity, or deployment
  boundary requires a successor architecture, risk review, and policy revision
  before implementation or use.

**Architecture basis.** `AUTH-EX-001`, Applicability and claims
`AUTH-EX-001.6/.9`, limit the system to a local, single-user, unauthenticated
Compose deployment and exclude remote/multi-user and history capabilities.
`ADR-004`, Application identity boundary, places the OS account and Docker
access inside the trust boundary.

**NIST justification.** NIST CSF 2.0 `GOVERN` and `IDENTIFY` require risk
decisions to reflect organizational context and understood assets/risks. NIST
SP 800-53 Rev. 5 `PL-2` and `RA-3` support documenting the system boundary,
operational context, assumptions, and risk assessment. NIST SP 800-218 SSDF
`PW.1.1` recommends risk modeling and data classification during design. The
data restriction keeps actual use within the protections the demonstrator has
and makes the omitted identity, encryption, privacy, and audit controls
visible rather than implied.

## `SEC-POL-02` - Network boundary and access enforcement

### Policy

- Docker Compose must publish exactly one application port to IPv4 loopback as
  `127.0.0.1:${RECORDS_HOST_PORT}:8000`; wildcard, IPv6, hostname, LAN,
  public, tunneled, proxied, host-network, or arbitrary-interface publication
  is prohibited.
- Only declared project services may attach to the private `record-net`
  network. The CLI and approved test consumers may reach `record-api:8000` on
  that network; the maintenance role must have no network.
- Public browser requests must enforce the exact configured Host and Origin.
  Internal clients must enforce the exact private service Host. CORS and proxy-
  derived identity must remain disabled.
- Browser and CLI/SDK traffic must terminate on the same `/api/v1` router and
  contract. No alternate administrative, consumer-specific, or direct-state
  path is allowed.
- Application accounts and authentication must not be added as a partial
  substitute for this boundary. Remote or multi-user access requires the
  complete successor architecture named in `SEC-POL-14`.

**Architecture basis.** `AUTH-EX-001.3/.6`, `ADR-004` Compose trust topology,
and `ARC-CTR-008`, Supported deployment profile and Network/Host/Origin rules,
define the exact ingress, internal network, and shared API path.

**NIST justification.** NIST SP 800-53 `AC-3` calls for enforcement of approved
logical access and `SC-7` calls for controlled communications at external and
key internal interfaces. `CM-7` supports limiting ports, protocols, software,
and capabilities to those required. NIST SP 800-190 sections `4.3.3` and
`4.4.2` recommend separated container networks, well-defined interfaces, and
controlled container network traffic. Loopback publication, a private bridge,
and role-specific connectivity are the demonstrator's tailored enforcement
mechanisms.

## `SEC-POL-03` - Least privilege and container runtime hardening

### Policy

- Runtime and maintenance containers must run as numeric UID/GID
  `10001:10001`, with a read-only root filesystem, bounded `tmpfs`, all Linux
  capabilities dropped, and `no-new-privileges:true`.
- Containers must not be privileged and must not receive the Docker socket,
  host PID/IPC/network namespaces, host devices, arbitrary host filesystems,
  or undeclared networks or mounts.
- CPU, memory, PID, temporary-storage, shutdown, request, and log limits from
  `ARC-CTR-008` must be present and effective on each supported host.
- Each service may receive only its declared artifact, network, and volume
  access. CLI, web, build, and test roles must never mount live data; the API
  must never mount backups; maintenance access is limited to an allowlisted
  stopped-API command.
- Images and runtime configuration must contain no credential, token, key, or
  secret. V2 has no application secret requirement.

**Architecture basis.** `AUTH-EX-001.12/.13`, `ADR-004`, Container controls,
and `ARC-CTR-008`, Mandatory service hardening and volume rules, define the
required identity, filesystems, privileges, resources, and mounts.

**NIST justification.** NIST SP 800-53 `AC-6` applies least privilege to users
and system processes; `CM-6` requires restrictive configuration settings;
`CM-7` requires least functionality; and `SC-6` supports resource allocation
to preserve availability. NIST SP 800-190 sections `4.1.2`, `4.4.3`, and
`4.5.5` recommend non-privileged image configuration, enforced secure runtime
configuration, minimal filesystem permissions, and avoiding sensitive host
mounts. These outcomes support the architecture's more specific read-only
filesystem and capability restrictions, reducing the effect of a compromised
demonstrator container on the Docker host boundary.

## `SEC-POL-04` - Approved configuration and controlled change

### Policy

- The reviewed source Compose model plus immutable release image references is
  the configuration baseline. Release verification must inspect the fully
  rendered `docker compose config`, not infer settings from fragments or
  examples.
- Release images must be digest-qualified. Service roles, API base path,
  internal names/ports, public bind, container user, volume paths, security
  controls, and image identities must not be ordinary operator overrides.
- The four declared `RECORDS_*` inputs must be type/range validated. Unknown
  `RECORDS_*` or `EXAMPLE_RECORDS_*` inputs must fail before readiness.
- Architecture, policy, Compose, image, API, SDK, CLI, web, and schema changes
  must retain version identity, compatibility analysis, traceable Git history,
  and the explicit approval required by their governing records.
- A container or image must be replaced from a reviewed build; it must not be
  patched or mutated in place.

**Architecture basis.** `ADR-005`, Build and release rules; `ADR-006`, Change
classification and feedback workflow; and `ARC-CTR-008`, Configuration surface
and Image/build/release identity, establish the baseline and change process.

**NIST justification.** NIST SP 800-53 `CM-2`, `CM-3`, and `CM-6` establish,
control, and apply secure baseline configurations; `SI-7` addresses detection
of unauthorized software/information changes. NIST SSDF `PW.9.1/.2` calls for
secure defaults, documented settings, configuration-as-code, and verification.
NIST CSF 2.0 `PROTECT` category `PR.PS` addresses platform security and
configuration management. Rendering and checking one immutable Compose model
makes the accepted baseline assessable and drift visible.

## `SEC-POL-05` - State access, transaction, and integrity protection

### Policy

- `record-api` is the only normal runtime process permitted to open live
  SQLite. `record-maintenance` may do so only with the API stopped, the shared
  exclusive lock acquired, no network, and an allowlisted command.
- Live SQLite must reside in the `record-data` named volume. Host bind mounts,
  anonymous/external live volumes, host SQLite tools, direct volume editing,
  client/test/build mounts, and multiple API replicas are prohibited.
- SQL statements must be fixed and parameterized. User-controlled fields,
  modes, directions, paths, or values must never become SQL identifiers or
  executable clauses.
- Writes must be bounded atomic transactions, use the accepted write mutex and
  expected-revision predicate, and never report success before commit. Stale
  writes must fail without overwrite; indeterminate outcomes must remain
  indeterminate until reconciled.
- Startup and readiness must verify application identity, schema/migration
  hashes, lock ownership, permissions, and database integrity without
  initializing or migrating state.

**Architecture basis.** `ADR-001`, `ARC-BND-003`, and `ARC-CTR-004` define API-
exclusive access, named-volume placement, parameterized SQL, transaction,
locking, readiness, and integrity behavior. `AUTH-EX-001.1/.5/.12` fixes the
same top-level claims.

**NIST justification.** NIST SP 800-53 `AC-3` and `AC-6` support restricting
state access to the minimum authorized processes. `SI-7` supports integrity
verification and action on unauthorized change; `CP-10(2)` identifies
transaction recovery for database systems. NIST SP 800-190 sections `4.4.3`
and `4.5.5` support restricting container filesystem access and using allocated
volumes instead of sensitive host mounts. Exclusive ownership, atomic
transactions, integrity checks, and revision preconditions protect record
integrity without claiming encryption-at-rest or protection from a Docker
administrator.

## `SEC-POL-06` - Input validation, safe interpretation, and output handling

### Policy

- Every external and cross-component input must be validated at its owning
  boundary for type, syntax, semantics, canonical encoding, allowed values,
  size, multiplicity, and unknown fields before application execution.
- HTTP handling must reject oversized bodies, malformed UTF-8/JSON, duplicate
  JSON keys, non-object bodies, unsafe media types, malformed Host/Origin, and
  invalid request identifiers as specified by the architecture.
- Record and search inputs must use the accepted Unicode normalization,
  control-character, code-point, byte, field/mode, query, cursor, and regex
  limits. Regex execution must use the pinned RE2-compatible engine and the
  complete-result time budget.
- Untrusted values must remain data: SQL uses bound parameters; browser values
  and problem content render as text; dynamic code evaluation, SQLite
  extensions, unreviewed remote assets, and user-selected filesystem paths are
  disabled.
- Client errors and routine logs must not disclose stack traces, SQL,
  filesystem paths, full record data, or raw search/regex content. Invalid
  input must produce a documented, side-effect-free failure.

**Architecture basis.** `ARC-CTR-001` defines domain validation;
`ARC-BND-002` defines the request pipeline; `ARC-CTR-002/003` define HTTP,
cursor, and regex validation; `ARC-CTR-004` requires bound SQL; and
`ARC-CTR-007/008` define safe browser rendering, CSP, headers, and error
disclosure.

**NIST justification.** NIST SP 800-53 `SI-10` requires validity checks for
system inputs and discusses syntax, semantics, length, ranges, and preventing
data from becoming control information. `SI-11` addresses safe error handling,
and `SC-18` addresses controlled mobile-code use. NIST SSDF `PW.5.1` expressly
includes input validation, output encoding, graceful error handling, and safe
logging among secure coding practices. The architecture's strict parsers,
bound SQL, text-only DOM insertion, CSP, and safe problems are the specified
future implementation mechanisms for those outcomes.

## `SEC-POL-07` - Resource bounds and safe failure

### Policy

- The application must enforce the architecture's limits for HTTP bodies and
  headers, admitted requests, worker threads, SQLite busy time, record count,
  page size, regex size, search duration, request deadline, CPU, memory, PIDs,
  temporary storage, and log rotation.
- Work exceeding a limit must fail with the defined safe outcome. It must not
  return a partial result as complete, execute a rejected command, silently
  widen a limit, or fabricate success/rollback.
- Startup after OOM, forced kill, daemon restart, or lost response must verify
  lock, store, schema, and readiness before accepting traffic.
- Client write operations must never be automatically replayed. Read retries
  are limited to the exact SDK policy and must remain inside the caller's
  timeout budget.

**Architecture basis.** `ARC-CTR-003` fixes search limits and complete-result
behavior; `ARC-CTR-005/006/007` fix retry and indeterminate-write handling;
and `ARC-CTR-008`, Mandatory service hardening and Application resource and
overload behavior, fixes system and container ceilings.

**NIST justification.** NIST SP 800-53 `SC-5` addresses denial-of-service
protection and `SC-6` protects availability through resource allocation and
quotas. `SI-10` supports rejecting invalid or out-of-range inputs predictably.
NIST SP 800-190 sections `4.4.2` and `4.4.3` recommend controlled container
network surfaces and enforced runtime configuration. Explicit ceilings and
fail-closed outcomes keep a compact unauthenticated local service from turning
unbounded input into uncontrolled host resource use.

## `SEC-POL-08` - Security-relevant logging and data minimization

### Policy

- Containers must emit bounded structured UTF-8 JSON events to stdout/stderr
  with UTC time, level, stable event name, request ID, method, route template,
  status, duration, build identity, and safe error code where applicable.
- Logs must exclude record `value`, full `name`, raw bodies, queries, regexes,
  ETags, cursors, SQL bound values, environment contents, backup bytes,
  secrets, and full host/volume/database paths. Redaction applies at every log
  level.
- Docker log rotation must be bounded. Application containers must not create
  an in-container log file or send remote telemetry by default.
- Logs are diagnostic correlation evidence, not a per-user audit trail,
  authoritative record store, or recovery mechanism. The release must not
  claim user attribution or non-repudiation.
- On a suspected incident, the operator must preserve relevant logs with the
  associated Compose configuration, image digests, volume identity, and time
  range before ordinary cleanup removes them.

**Architecture basis.** `ARC-BND-001`, State and authority, classifies logs as
diagnostic only. `ARC-CTR-008`, Logging and diagnostics, defines exact fields,
prohibited content, rotation, and limitations. SDK, CLI, and web contracts add
surface-specific redaction rules.

**NIST justification.** NIST SP 800-53 `AU-2` requires selection and rationale
for security-relevant event types; `AU-3` addresses useful event content and
privacy risk; `AU-4` addresses bounded log storage; and `SI-4` supports system
monitoring. NIST SSDF `PW.5.1` includes logging and tracing while handling data
safely. The selected fields support fault and incident reconstruction, while
explicit content minimization addresses NIST's warning that audit records can
create privacy risk. Full `AU`-family audit/accountability is intentionally not
claimed for this no-identity demonstrator.

## `SEC-POL-09` - Backup, restoration, and recoverability

### Policy

- The API must be stopped and the shared exclusive lock acquired for backup,
  migration, restore, or integrity recovery. These operations must use the
  networkless maintenance role and generated, allowlisted artifact identities.
- A validated backup is mandatory before every existing-database migration,
  upgrade that changes schema, restore attempt, or explicitly authorized
  destructive data operation. Existing backup destinations must not be
  overwritten.
- Each accepted backup must carry source/build/schema/architecture metadata
  and a SHA-256 value, and pass identity, schema, migration, capacity, row, and
  SQLite integrity checks before atomic finalization.
- Restore must validate before and after copying, preserve the prior live set,
  switch atomically where supported, run readiness and smoke verification, and
  roll back or leave recoverable state on failure.
- A same-host backup volume protects against logical failure only. If records
  are expected to survive host loss, the operator must choose and record a
  backup cadence and must export a validated bundle off-volume. The exported
  file must be protected according to its record content. Without that record
  and export, no host-loss recovery objective is claimed.
- Recovery must be exercised with the exact release artifacts before a release
  may claim the corresponding recovery behavior.

**Architecture basis.** `ARC-CTR-004`, Backup and restore contract, defines the
artifact, validation, preservation, and switch behavior. `ARC-CTR-008`, Backup,
recovery, and incident handling, defines operational use and the host-loss
limitation. `ARC-CTR-009` requires backup/restore and recovery vectors.

**NIST justification.** NIST SP 800-53 `CP-9` calls for user/system information
backups at a risk-appropriate frequency and protection of backup
confidentiality, integrity, and availability. `CP-10` calls for recovery to a
known state and identifies transaction recovery; `SI-7` supports integrity
verification. NIST CSF 2.0 `RECOVER` calls for executed and verified recovery
activities. Offline, hashed, validated, non-overwriting backups and exercised
restore would provide proportionate local protection while explicitly leaving
RTO, RPO, and high availability outside scope.

## `SEC-POL-10` - Software supply chain and release integrity

### Policy

- Base images, packages, wheels, and build tools must come from reviewed
  trusted sources and be fixed by immutable digest, hash-locked dependency, or
  an equivalently reproducible identity. Mutable tags and local caches are not
  release identity.
- BuildKit stages must separate build/test tooling from minimal runtime images.
  Runtime images must contain only the owned runtime artifacts and libraries;
  source checkout, compilers, package caches, test fixtures, build secrets,
  and unrelated tools are prohibited.
- Each release must record source commit, architecture/API/schema versions,
  image and manifest digests, supported platforms, exact SDK wheel and web
  bundle hashes, licenses, an SBOM, provenance, and the applicable signature
  or authenticated-provenance verification policy.
- The exact tested wheel and bundle bytes must be the bytes copied into release
  images. A provenance, digest, or artifact-substitution mismatch blocks the
  release.
- Image, dependency, license, secret, and configuration scanning must cover
  every released image and claimed platform. A material finding must be fixed
  or receive an explicit, architecture-compatible human disposition before
  release.
- Registry/package retrieval used for release must use authenticated trusted
  sources over protected transport supported by the selected tooling.

**Architecture basis.** `AUTH-EX-001.13`, `ADR-005`, and `ARC-CTR-008`, Image,
build, and release identity, require pinned inputs, minimal images, immutable
digests, SBOM/provenance, vulnerability/license review, and artifact hash
continuity.

**NIST justification.** NIST SP 800-53 `SR-3` addresses documented supply-chain
controls, `SR-4` addresses component provenance, `SR-11` addresses component
authenticity, and `SI-7` addresses integrity. NIST SP 800-190 sections
`4.1.1`-`4.1.5` and `4.2.1`-`4.2.2` recommend image vulnerability/configuration
gates, non-privileged minimal images, exclusion of embedded secrets, trusted
images, protected registry connections, and immutable version identities.
NIST SSDF `PS.2.1`, `PS.3.1/.2`, and `PW.4` call for release-integrity
verification, protected release/provenance records including SBOMs, and
reviewed third-party components. The policy turns those recommendations into
traceable release gates without claiming that a signature alone proves trust.

## `SEC-POL-11` - Secure development and security verification

### Policy

- Security requirements must trace to this policy and the precise architecture
  claim they implement. Generated schemas, code, and tests must not replace
  that authority.
- Development must use language- and environment-appropriate secure coding,
  peer review, automated static analysis, dependency/image analysis, and the
  applicable domain, API, persistence, SDK, CLI, web, container, fault,
  recovery, and end-to-end tests in `ARC-CTR-009`.
- Tests must include negative and adversarial inputs, injection boundaries,
  unauthorized network/mount paths, unsafe Host/Origin, XSS payloads,
  concurrency races, resource limits, security headers, log redaction, image
  contents, and backup/restore failure behavior.
- The exact release configuration and artifacts must be assessed. A source
  test, successful image build, health response, scanner pass, or local smoke
  test cannot independently establish release conformance.
- Every nonpass, skip, scanner limitation, and untested platform must remain
  visible. Missing evidence keeps the affected gate open.

**Architecture basis.** `ARC-CTR-009`, Verification layers, vector catalog,
delivery gates, and evidence requirements, defines the required coverage and
claim limits. `ADR-006` prevents product behavior from rewriting contracts.

**NIST justification.** NIST SP 800-53 `SA-11` requires an ongoing developer
assessment plan, unit/integration/system/regression testing, evidence,
remediation, and correction. `CA-2` supports scoped control assessment. NIST
SP 800-53A provides customizable examination, interview, and test methods.
NIST SSDF `PO.1`, `PW.5`, `PW.7`, and `PW.8` call for known security
requirements, secure coding, human-readable code review/analysis, and
executable-code security testing. Traceable multi-layer evidence is therefore
required before the demonstrator can make a security conformance claim.

## `SEC-POL-12` - Vulnerability monitoring and remediation

### Policy

- The release owner must monitor supported base images, runtime, application
  dependencies, and owned code for credible vulnerabilities at release time
  and when a new potentially applicable vulnerability is reported.
- Findings must record affected component/digest, source and detection time,
  applicability, reachability or exposure within the accepted boundary,
  severity information, proposed response, owner, and verification status.
- A finding is material when it can violate an in-scope policy or architecture
  claim, materially change risk within the local boundary, or invalidate a
  release claim. Material findings block release until remediated or explicitly
  dispositioned by human authority in a way the architecture permits.
- Remediation must update locked inputs and rebuild immutable artifacts; no
  runtime container or released image may be patched in place. Relevant
  security and regression checks must be rerun before release.
- Confirmed vulnerabilities in owned code must be analyzed for root cause and
  similar defects; requirements, tests, or development controls must be
  updated when needed to prevent recurrence.

**Architecture basis.** `ADR-005`, Costs and follow-up, makes base/runtime CVE
response a product obligation. `ARC-CTR-008`, Image/build/release identity and
Failure/recovery, requires vulnerability review and explicit human disposition
for material findings.

**NIST justification.** NIST SP 800-53 `RA-5` requires monitoring/scanning,
analysis, risk-based remediation, and updated scanner capability; `SI-2`
requires flaw identification, tested correction, and update handling. NIST SP
800-190 sections `4.1.1` and `4.4.1` call for container-aware image/runtime
vulnerability management and quality gates. NIST SSDF `RV.1`, `RV.2`, and
`RV.3` call for ongoing vulnerability discovery, risk-based remediation, root-
cause analysis, and prevention of recurrence. Rebuild-and-reverify preserves
the immutable release model while responding proportionately to risk.

## `SEC-POL-13` - Local incident handling and evidence preservation

### Policy

- Suspected disclosure, corruption, unexpected remote exposure, malicious or
  substituted artifacts, unexplained privileged container behavior, Docker
  socket/host mount exposure, or a security-relevant integrity failure must be
  treated as a local security incident.
- The operator must stop the API when continued operation could change or
  disclose evidence, preserve the named-volume identity and SQLite companions,
  logs, rendered Compose configuration, image/manifest digests, policy and
  architecture versions, relevant backup artifacts, and cryptographic hashes,
  and avoid editing originals.
- The owner must record detection, scope, affected assets/data, observed facts,
  containment, eradication or correction, recovery source, verification,
  limitations, and any required vulnerability or invariant-conflict record.
- Recovery must use a verified image and validated backup under `SEC-POL-09`,
  followed by readiness and canonical domain/search/client smoke vectors. A
  suspected malicious image must not be reused merely because data restoration
  succeeds.
- Lessons learned must feed vulnerability remediation, tests, configuration,
  and policy/architecture review. Organization-wide notification, legal
  reporting, and remote incident response are not supplied by this app and
  remain the operator organization's responsibility.

**Architecture basis.** `ARC-CTR-008`, Backup, recovery, and incident handling,
specifies stop/preserve/restore behavior and the absence of remote response or
per-user attribution. `ARC-CTR-004` and `ARC-CTR-009` define safe recovery and
verification.

**NIST justification.** NIST SP 800-53 `IR-4` calls for preparation, detection
and analysis, containment, eradication, recovery, coordination, and lessons
learned. `CP-10` supports restoration to a known state and `SI-7` supports
integrity verification. NIST SP 800-190 section `6.4` calls for documented,
container-specific collection of logging and forensic data. The procedure is
limited to the local product boundary but preserves the minimum evidence and
known-state recovery needed for a defensible response.

## `SEC-POL-14` - Exceptions, risk decisions, and expansion triggers

### Policy

- A policy exception must never be implicit. The request must identify the
  exact policy ID, architecture claims, reason, affected release/data/scope,
  risk, owner, start/end or review point, compensating measures, evidence, and
  explicit human authority.
- An exception may not authorize behavior the architecture prohibits. Such a
  request requires an architecture revision or successor and any required
  invariant-conflict handling.
- Remote/LAN/public exposure, multi-user use, application identity or roles,
  sensitive or regulated data, TLS/proxy trust, encryption-at-rest, formal
  audit retention, production availability objectives, telemetry/SIEM, or
  federal/compliance claims always require a successor security architecture
  and revised verification profile.
- Approved bounded exceptions must be reviewed at their recorded point and
  reconciled with release evidence. Expired, unsupported, or unverified
  exceptions do not authorize release.
- A NIST publication update, scanner result, or implementation limitation is
  evidence for review, not automatic authority to change policy.

**Architecture basis.** `ADR-006`, Feedback workflow, requires preserved
evidence, impact analysis, explicit authority, revision identity, and consumer
reconciliation. `ADR-004` states the remote/multi-user successor needs, and the
Codex evidence authority specification prohibits lower-standing overrides.

**NIST justification.** NIST CSF 2.0 `GOVERN` categories `GV.PO` and `GV.OV`
address established, reviewed policy and oversight. NIST SP 800-53 `CM-3`,
`PL-2`, and `RA-3` support controlled change, documented assumptions, and risk
assessment. NIST SSDF `PO.1.2` recommends maintained requirements and a process
for exception requests, while `PW.1` requires justification when risk analysis
relaxes a security requirement. Durable, time-bounded human decisions prevent
an exception from silently becoming a broader system design.

## Enforcement and truthful claims

A failed mandatory requirement or missing required evidence blocks only the
release or conformance claim that depends on it; independent verified work may
continue. The finding must not be hidden by weakening a test, narrowing a
claim after the fact, changing generated output, or labelling the policy
inapplicable without following `SEC-POL-14`.

Permitted wording after all required evidence passes is:

> Conforms to `SEC-NIST-SUITE-001@1.0.1` for the local single-user TADp
> demonstrator profile.

The release must not say "NIST certified," "NIST compliant," "FISMA compliant,"
or "implements NIST SP 800-53" based solely on this suite.

## Revision record

| Date | Revision | Change | Authority |
|---|---|---|---|
| 2026-11-10 | `1.0.0` | Established the demonstrator security policies | User's NIST policy instruction and clarification |
| 2026-11-10 | `1.0.1` | Made policy primacy and the architecture, HIPAA, and RZN-001 relationship explicit without changing a policy outcome | User's explicit reconciliation instruction and policy-primacy clarification |
