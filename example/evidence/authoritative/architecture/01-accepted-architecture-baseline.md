# Example record application accepted architecture baseline

**Evidence ID:** `AUTH-EX-001`  
**Classification:** `evidence/authoritative/architecture`  
**Status:** Active  
**Owner and accepting authority:** User, project authority  
**Effective date:** 2026-11-10  
**Source and revision:** `RZN-001` interpreted under the User's 2026-11-10 instructions; architecture revision `2.0.1`  
**Supersedes / superseded by:** Supersedes revision `2.0.0` preserved at Git commit `5f0c325`; revision `2.0.0` superseded [`ARC-SUITE-001@1.0.0`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md); no successor  

## Binding statement

The example project must realize one coherent, locally operated record system
whose public records contain an immutable system-generated UUID, an editable
name, and an editable textual value. All executable user surfaces must use one
versioned API and one SQLite-backed authority for record behavior. The focused
records linked from this baseline define the accepted v2 interpretation of
that outcome. Application services/clients/tests/migrations/maintenance run in
Compose-managed containers and builds run through Docker BuildKit targets; the
host installs no application runtime or service.
The CLI and browser use the same `/api/v1` route set and wire behavior; their
private-network and host-loopback origins are transport boundaries, not
separate APIs.

Future work under this architecture must also satisfy the applicable
requirements of
[`SEC-NIST-SUITE-001@1.0.1`](../security/NIST/00-nist-security-policy-suite-index.md)
and
[`SEC-HIPAA-SUITE-001@1.0.1`](../security/HIPPA/00-hipaa-security-policy-suite-index.md).
The supported information profile is non-production demonstration/test data
that is purpose-created synthetic or supported by the external documented
de-identification basis accepted by the HIPAA suite, while also satisfying the
NIST suite's separate prohibition on production, confidential, regulated, or
higher-control data. Actual, possible, or insufficiently classified ePHI is
not permitted.

For security, permitted data/use, safeguards, review, and evidence, those
security suites are the primary invariants and guide this architecture. The
architecture supplies technical shape only within their limits; neither it nor
`RZN-001` can narrow, waive, or cause a policy requirement to be rewritten.

## Source standing and acceptance

[`RZN-001`](../../non-authoritative/realizations/v0/RZN-001-example-record-application.md)
is preserved as non-authoritative proposal input. It supplied the requested
outcome, candidate products, risks, and unresolved questions; it did not
accept its own proposed behavior.

The User's 2026-11-10 instruction to create a highly detailed architecture
suite and treat it as authoritative invariant evidence establishes the output
classification. The follow-up instruction, "complete the architecture suite
to your best judgement. I will read it and address any issues after it is
created", authorizes Codex's decision method for all unresolved `RZN-001`
items and directly necessary architecture choices. `ARC-AUT-001` preserves
the bounded disposition and limitations of that authority.

The User then explicitly instructed, "make this fully dockerized" and "I
don;t want to install all the services on teh host. make taht decision now and
add to the architecturer invaraint". Those instructions authorize the specific
deployment-invariant revision from `1.0.0` to `2.0.0`. The predecessor and
impact are preserved in `ARC-REV-001`.

The User further instructed, "the CLI should use the same API path as teh web
app." That instruction fixes `AUTH-EX-001.3` and is preserved verbatim in
`ARC-AUT-001`.

The User then instructed, "I need you to actually reconcile the files according
to these findings. I need you to make these changes to the files in place."
That instruction authorizes patch revision `2.0.1`: it incorporates the
already-binding NIST and HIPAA suites and their `RZN-001` dispositions into
the files that own architecture, security, and realization meaning. It does
not authorize new product behavior, implementation, ePHI, remote access, or a
completion/compliance claim.

## Applicability

| Applies to | Does not apply to | Rationale |
|---|---|---|
| Architecture and future documentation for the example record application | Unrelated TADp protocol, templates, or projects | The User named the example project and target architecture directory |
| Future record API, SQLite adapter, Python SDK, CLI, and browser application | A product implementation not governed by an accepted initiative | Architecture constrains products but does not authorize execution |
| Local single-user v2 Docker Compose deployment with the accepted non-production synthetic/documented-de-identified data profile | Native-host application runtime, actual or possible ePHI, production clinical use, public/remote/multi-tenant/regulated deployment, shared workstation identity, third-party record processing, Kubernetes, or non-Compose orchestration | The User requires no host service installs and the accepted security suites require a successor for excluded data or use; other environments require materially different deployment, identity, security, privacy, and operations decisions |
| Record create, retrieve, update, browse, search, and adjacent navigation | Delete, bulk operations, record-level import/export, audit history, and arbitrary queries | The source did not request the excluded capabilities, and best-judgment scope keeps the example bounded; opaque backup transfer remains an operations concern |

## Binding claims

| Claim ID | Requirement or constraint | Verification or observation method |
|---|---|---|
| `AUTH-EX-001.1` | The API container is the sole normal runtime writer/reader of live SQLite. The networkless maintenance container may mount the data volume only under proved mutual exclusion while API is stopped. | Rendered Compose mount graph, competing-container tests, and dependency checks proving CLI/web/SDK have no SQLite path |
| `AUTH-EX-001.2` | The public record contract contains exactly `id`, `name`, and `value`; `id` is generated by the service and cannot change after creation. | Schema review, API contract tests, update rejection tests, and database trigger test |
| `AUTH-EX-001.3` | Every executable surface uses the same API-owned create, retrieve, update, search, and next/previous semantics. CLI and web consume the identical `/api/v1` paths, methods, representations, errors, and version lifecycle; no consumer-specific record API exists. Their transport origins differ only at the Docker network boundary. | Route inventory plus cross-surface conformance vectors in `ARC-CTR-009` |
| `AUTH-EX-001.4` | Searches target zero or one accepted predicate and use the field, mode, normalization, regex, ordering, and paging rules in `ARC-CTR-003`; clients must not reimplement membership. | API search tests and cross-client result comparison |
| `AUTH-EX-001.5` | Concurrency is explicit: updates require the current strong revision ETag and never silently overwrite a newer revision. | Competing-update API, SDK, CLI, and web tests |
| `AUTH-EX-001.6` | V2 is local, single-user, and unauthenticated at the application layer. The API may bind all interfaces only inside its private Compose network; Docker must publish it exclusively to host `127.0.0.1`. | Rendered Compose, host/peer reachability, Origin/Host, and publication-negative tests |
| `AUTH-EX-001.7` | Documentation/architecture, Compose/runtime packaging, API, SDK, CLI image, and web assets are distinct, independently verifiable delivery units with the dependencies in `ADR-007`. | Future scope assessments, image/build records, initiative records, and completion evidence |
| `AUTH-EX-001.8` | Released contract meaning is versioned and never rewritten in place to match implementation drift. | Revision history and compatibility review under `ADR-006` |
| `AUTH-EX-001.9` | Deletion, bulk mutation, record-level import/export, history, accounts, remote multi-user access, and offline writes are not v2 capabilities. Opaque validated backup-bundle transfer under the maintenance contract is operational recovery, not a record feature. | Route/command/UI inventory, maintenance-command boundary, and negative contract tests |
| `AUTH-EX-001.10` | No implementation or completion claim exists until a governing initiative delivers the product and supplies the evidence required by `ARC-CTR-009`. | Initiative status and completion-evidence audit |
| `AUTH-EX-001.11` | Docker Compose is the only supported runtime/orchestration path. Running the example must require no host installation of Python, SDK, CLI, SQLite, RE2, FastAPI, Uvicorn, Node/TypeScript, migration, maintenance, or test tooling. | Clean-host prerequisite inventory and end-to-end Compose-only run/build/test/maintenance audit |
| `AUTH-EX-001.12` | Live SQLite and backups use distinct Docker named volumes. Host bind mounts are forbidden for the live database; only API and mutually exclusive maintenance containers may mount data. | Compose config/mount inspection, permission/locking tests, backup export/restore drill |
| `AUTH-EX-001.13` | Released images run non-root with read-only root filesystems, dropped capabilities, no Docker socket, bounded resources, pinned/traceable inputs, and declared multi-platform targets. | Image metadata/SBOM/signature or provenance, rendered config, and runtime negative tests |
| `AUTH-EX-001.14` | Every future D2-D6 specification, delivery, release, and conformance claim must apply `SEC-NIST-SUITE-001@1.0.1` and `SEC-HIPAA-SUITE-001@1.0.1` together for their applicable scopes. Architecture evidence cannot substitute for policy evidence, and passing one security suite cannot substitute for the other. | Initiative source mapping, policy applicability matrices, exact architecture/security evidence, and release-claim review |
| `AUTH-EX-001.15` | The supported data/use profile permits only non-production demonstration/test records that are purpose-created synthetic or have the accepted externally documented de-identification basis and that do not violate the NIST suite's independent data restrictions. Actual, possible, or insufficiently classified ePHI and every successor-gate trigger are prohibited in v2. | Fixture/data manifest, provenance or de-identification record review, repository/image/artifact scans, operator documentation, and successor-gate review |

## Interpretation and conflicts

The focused accepted records in this directory are the precise interpretation
of these claims. A product convenience, implementation limitation, generated
OpenAPI document, test fixture, or client expectation cannot weaken them.

Revision `1.0.0` was the first project architecture; its native-host deployment
claims are now superseded by explicit User authority and preserved in
`ARC-REV-001`. No unresolved invariant conflict remains from that change. The
governing Codex protocol remains higher authority for evidence handling, human
decisions, initiative lifecycle, and Git traceability.

Revision `2.0.1` makes the primary NIST and HIPAA security requirements explicit.
Those suites already bound future work before this patch, so the reconciliation
changes no accepted product behavior. It establishes one visible data/use and
evidence boundary across architecture, security, and `RZN-001`. The policies
guide both documents for their scope; neither architecture implementation
convenience nor realization-note candidate text may be used to waive or revise
a policy gate.

If a later record or product contradicts this baseline, preserve both sources,
stop only the affected work, and use the protocol invariant-conflict process.

## Revision record

| Date | Change | Reason | Authority |
|---|---|---|---|
| 2026-11-10 | Accepted revision `1.0.0` and its focused architecture suite | User requested an authoritative architecture derived from `RZN-001` and authorized best-judgment completion | User, project authority |
| 2026-11-10 | Accepted revision `2.0.0`; superseded native-host deployment with mandatory Docker Compose, containerized runtime/build/test/maintenance, named-volume state, and no host application-service installs | User explicitly required full Dockerization and stated that services must not be installed on the host | User, project authority; exact instructions in `ARC-REV-001` |
| 2026-11-10 | Fixed CLI and web to one identical `/api/v1` route/semantic surface while preserving distinct Docker origins | User explicitly required the CLI to use the same API path as the web app | User, project authority; exact instruction in `ARC-AUT-001` |
| 2026-11-10 | Accepted patch revision `2.0.1`; reconciled architecture with NIST/HIPAA policy revisions `1.0.1` and annotated `RZN-001` with its current authoritative dispositions | The three baselines were already simultaneously binding, but their ownership, data profile, successor triggers, and consumer rules needed to be explicit in the source files | User, project authority; exact in-place reconciliation instruction in `ARC-AUT-001` |

