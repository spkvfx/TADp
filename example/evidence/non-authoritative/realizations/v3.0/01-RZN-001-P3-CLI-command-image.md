# One-shot Compose command-line image

**Realization ID:** `RZN-001-P3-CLI-N01`  
**Suite:** [`RZN-001-P3-CLI-SUITE@v3.0`](00-RZN-001-P3-CLI-suite-index.md)  
**Suite version:** `v3.0`  
**Status:** Recorded; invariant-bounded proposal input  
**Recorded by:** Codex on behalf of the User  
**Recorded date:** 2026-11-10  
**Source:** User request in the current Codex conversation and [`RZN-001`](../v0/RZN-001-example-record-application.md)  
**Historical product lineage:** `RZN-001-P3-CLI`  
**Accepted delivery-unit alignment:** `D5 Standalone CLI image`  
**Related initiative or proposal:** None created  

> **Evidence standing:** This note records detailed realization input for one
> possible D5 outcome. It is not an initiative, accepted product
> specification, built image, command result, security assessment, release,
> conformance result, or completion claim. The cited authoritative records own
> every accepted command and runtime meaning.

## Realization

There is a bounded opportunity to deliver one independently versioned,
digest-identified `example-records-cli` OCI image whose exec-form `recordctl`
entrypoint exposes the already accepted record capabilities as one-shot Docker
Compose commands. The image would consume the exact released Python SDK wheel,
reach only the compatible API at `http://record-api:8000/api/v1` on the private
Compose network, produce stable human or machine-readable process output, and
terminate with one documented exit status.

The candidate CLI would give a local shell user a scriptable alternative to the
browser while preserving the API as the only record authority. It would not
install anything on the host, open SQLite, implement HTTP independently, start
or stop the API, persist drafts, control Docker, or introduce a second record
path.

## Narrow outcome and beneficiary

| Dimension | Candidate record |
|---|---|
| Outcome | One minimal, one-shot D5 CLI image that realizes the accepted invocation, commands, streams, failures, isolation, dependency, and evidence contracts |
| Primary beneficiaries | Local shell users, automation authors, D4 SDK consumers, operators validating the shared API path, release owners, and conformance reviewers |
| Authority boundary | CLI parsing, bounded stdin, public-SDK adaptation, human/JSON formatting, safe diagnostics, and process exit mapping only |
| Output class | CLI source/package, exec-form image entrypoint, command/help/completion material, exact SDK-wheel copy proof, minimal OCI image, and D5 evidence records |
| Independent review claim | The exact pinned CLI image behaves as one disposable process and passes the D5 CLI, applicable container/operations, security, and end-to-end gates |
| Explicit non-claim | No host binary, API implementation, HTTP shortcut, SQLite access, Docker control, server lifecycle, persistent CLI state, browser capability, remote use, regulated use, or general compliance certification |

## Version identity is not product acceptance

`v3.0` identifies this realization suite and its future-initiative boundary. It
does not silently select a CLI semantic version, replace the accepted `v1`
interaction contract, or rewrite the `v2` standalone wording in
`ARC-BND-005`. A future proposal and release record must identify the actual
CLI semantic version, image digest, compatible SDK and API versions, Compose
release identity, architecture revision, and security-suite revisions.

Any conflict among those identities must be recorded and resolved through the
governed successor process. This note cannot normalize the conflict by treating
its suite label as implementation authority.

## Context and invariant evidence

| Question | Record |
|---|---|
| What was requested historically? | Product 3 in `RZN-001` requested a CLI that mirrors the record operations exposed through the SDK and API. |
| What is now accepted? | Architecture `2.0.1` fixes a one-shot Compose service, fixed private API origin, public SDK dependency, command grammar, input limits, output schemas, diagnostics, exit codes, isolation, and D5 evidence gate. |
| What is current product status? | `ARC-CTR-009` records required vectors and no supplied D5 implementation or passing conformance evidence. |
| What remains proposal-level? | Exact repository destinations, implementation libraries within the accepted boundary, image/base/dependency patch locks, product semantic version, owners, release channel, evidence storage, and any separately acceptable sub-scope. |
| Who is affected? | Local users, automation callers, D2-D4 owners, API operators, release/security reviewers, and the later D6 parity evidence owner. |
| Which data may be used? | Only non-production purpose-created synthetic data or externally documented de-identified data that also satisfies the NIST restrictions; actual or possible ePHI and higher-control data remain prohibited. |

## Binding source inventory

| Source | Exact relevance |
|---|---|
| [Codex invariant suite](../../../authoritative/LLM/00_Codex_Invariant_Suite_Index.md) | Governs authority, source identity, narrow scope, explicit decisions, truthful status, and evidence claims. |
| [`ARC-SUITE-001@2.0.1`](../../../authoritative/architecture/00-architecture-suite-index.md) | Owns the active technical architecture and its complete reading order. |
| [`AUTH-EX-001`](../../../authoritative/architecture/01-accepted-architecture-baseline.md) | Owns the binding API-exclusive, shared-capability, Compose-only, security-additive, and permitted-use claims. |
| [`ADR-001`](../../../authoritative/architecture/04-ADR-001-api-exclusive-persistence.md) | Forbids direct/offline persistence and requires the CLI to traverse the shared API. |
| [`ADR-004`](../../../authoritative/architecture/07-ADR-004-container-only-deployment-trust-model.md) | Owns the local loopback/private-network trust boundary and unsupported remote paths. |
| [`ADR-005`](../../../authoritative/architecture/08-ADR-005-containerized-technology-stack.md) | Owns the container-only build/runtime stack and immutable artifact path. |
| [`ADR-006`](../../../authoritative/architecture/09-ADR-006-contract-versioning-and-feedback.md) | Governs compatibility feedback and successor revisions instead of implementation-led drift. |
| [`ADR-007`](../../../authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md) | Owns D5 dependencies, independent completion, and delivery before D6. |
| [`ARC-CTR-005`](../../../authoritative/architecture/18-python-sdk-contract.md) | Owns the only public client surface the CLI may consume. |
| [`ARC-BND-005`](../../../authoritative/architecture/19-cli-boundary.md) | Owns the image, entrypoint, parser/adapter/formatter boundary, state, isolation, and exclusions. |
| [`ARC-CTR-006`](../../../authoritative/architecture/20-cli-interaction-contract.md) | Owns invocation, options, commands, stdin, human/JSON output, diagnostics, exit codes, and failures. |
| [`ARC-CTR-008`](../../../authoritative/architecture/23-operations-security-contract.md) | Owns effective Compose hardening, network, logging, lifecycle, resource, and release behavior. |
| [`ARC-CTR-009`](../../../authoritative/architecture/24-conformance-contract.md) | Owns `CLI-001` through `CLI-011`, applicable cross-vector groups, the D5 gate, and evidence fields. |
| [`SEC-NIST-SUITE-001@1.0.1`](../../../authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Primary future-development security and assurance invariant for this candidate. |
| [`SEC-HIPAA-SUITE-001@1.0.1`](../../../authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Primary data/use, safeguard, inherited-control, evidence, and successor-gate invariant. |

The parent realization explains lineage only. It cannot reopen a decision that
the accepted architecture owns or override either primary security suite.

## Exact product boundary

The D5 candidate includes:

- the `example-records-cli` image and its own semantic version, digest, SBOM,
  provenance/signature disposition, and release metadata;
- an exec-form `recordctl` entrypoint, top-level dispatcher, parser, bounded
  stdin reader, SDK adapter, human and JSON formatters, safe error mapper, and
  stable exit-code mapping;
- command help and optional generated completion artifacts that contain no
  record or query data;
- the exact released D4 wheel copied without rebuild or substitution; and
- process, dependency, image, security, cross-surface, and clean-host evidence
  for the exact released artifact.

The D5 candidate excludes:

- API, FastAPI/Uvicorn, SQLite binaries/state/tools, migrations, browser assets,
  compilers, package-manager caches, test suites, and source checkout from the
  runtime image;
- direct HTTPX use outside the SDK, direct SQL, alternate API paths, offline
  state, record caches, configuration files, host-path options, and file mounts;
- delete, bulk, record import/export, SQL, force update, server start, login,
  Docker-control, background daemon, pager ownership, and full-screen terminal
  UI capabilities; and
- API lifecycle, Compose orchestration, operator recovery, database ownership,
  SDK behavior, or web behavior as part of the D5 completion claim.

## Candidate invocation and configuration

The supported host-facing grammar is exactly:

```text
docker compose run --rm record-cli [GLOBAL-OPTIONS] COMMAND [COMMAND-OPTIONS]
```

Redirected or noninteractive stdin adds Compose option `-T` before the service
name. The operator starts the compatible API separately with the accepted
release material; a CLI invocation never manages that lifecycle. Direct
`recordctl` execution exists only inside image/conformance tests.

| Global option | Candidate behavior inherited from `ARC-CTR-006` |
|---|---|
| `--timeout SECONDS` | Finite decimal `0.1..60.0`; image default `5.0` |
| `--json` | Stable machine-readable success/problem output on the contract-selected stream |
| `--no-color` | Disables ANSI; ANSI is also absent for non-TTY streams or `NO_COLOR` |
| `--version` | Prints CLI plus compatible SDK/API-major identity and exits `0`; no command may accompany it |
| `--help` | Prints contextual help to stdout and exits `0` |

The release service fixes `http://record-api:8000` as its base origin. There is
no public API URL option, URL environment override, implicit config file,
credential, working-directory database, host-gateway discovery, or Docker
socket discovery. Unknown, repeated single-value, missing, or conflicting
options fail as usage errors before an SDK call.

## Candidate command surface

| Command | Accepted input boundary | One intended action | Success/boundary result |
|---|---|---|---|
| `create --name TEXT (--value TEXT\|--value-stdin)` | Exactly one value source; explicitly selected stdin is strict UTF-8 and bounded to 16,384 accepted bytes plus decoder overhead | Validate and call `create_record` once | Canonical created record, exit `0` |
| `get ID` | One canonical UUID | One public SDK get | Canonical record/ETag representation, exit `0`; absent is `3` |
| `update ID [--name TEXT] [--value TEXT\|--value-stdin]` | At least one mutable field; mutually exclusive value source | Retrieve current record/ETag, send one conditional SDK update | Returned canonical record or normalized no-op, exit `0`; conflict `5`; indeterminate `9` |
| `search [predicate] [--limit N] [--all] [--max-pages N]` | Predicate is absent or complete field/mode/query source; page size `1..100`, default `25`; `--max-pages` only with `--all` | One page call or SDK iterator calls | API order; explicit empty result is success `0`; bounded-all metadata remains truthful |
| `next ID [context] [--ceiling N]` | Canonical ID plus absent or complete retained search context | One SDK neighbor call | Record `0`, end boundary `4`, mismatch/search failure `8` |
| `previous ID [context] [--ceiling N]` | Same rule as `next` | One SDK neighbor call | Record `0`, start boundary `4`, mismatch/search failure `8` |

`--value` and `--value-stdin`, and `--query` and `--query-stdin`, remain
mutually exclusive. Standard input is never read implicitly. Host files can be
redirected into stdin by the shell, but no path is passed and no host directory
or file is mounted into the CLI service.

## Output and stream contract

Human success output belongs only on stdout. A single record presents `ID`,
`Name`, then `Value`; multiline value content is emitted literally only as
explicit success data. Search retains API order, does not silently truncate,
and states `No records found.` for a successful empty result.

In JSON mode stdout contains exactly one UTF-8 document plus trailing LF and no
ANSI, progress text, or diagnostic. Candidate schemas remain those owned by
`ARC-CTR-006`:

- a single record is wrapped under `record`;
- one page contains `items`, `next_cursor`, and `snapshot_ceiling`;
- `--all` contains `items`, `complete`, `pages`, and `snapshot_ceiling`, with
  `complete=false` only for a normal user-selected `--max-pages` stop;
- a boundary contains a null record, `start` or `end`, and the ceiling; and
- JSON version output is a separately documented stable version object.

Explicit help uses stdout/`0`; parser and runtime failures use stderr with
stdout empty. JSON diagnostics contain one safe problem-like object with code,
message, optional request ID, and safe issue metadata. No traceback, transport
representation, raw regex/query, full record value, or hidden debug mode is a
normal user-facing diagnostic.

## Stable process outcomes

| Exit | Meaning preserved by the candidate |
|---:|---|
| `0` | Success, including no-op update, empty/completed search, help, and version |
| `1` | Unexpected CLI or incompatible-protocol failure |
| `2` | Usage or local validation failure before an accepted action |
| `3` | Requested canonical record is absent |
| `4` | Start/end collection boundary; not an error and never wraparound |
| `5` | Conditional revision conflict; no force or automatic merge |
| `6` | Service unavailable, including exhausted safe-read handling or pre-dispatch connection failure |
| `7` | Server/API failure not assigned another stable class |
| `8` | Search/navigation failure such as invalid cursor/context or budget exhaustion |
| `9` | Write dispatched but commit outcome cannot be proved |
| `130` | User interruption; never a success or rollback claim |

If interruption or transport loss follows write dispatch, the CLI preserves
the unknown outcome and tells the user to get or search before making an
explicit retry decision. It never replays the write, searches for a similar
record, reports rollback without proof, or converts uncertainty into ordinary
unavailability.

## Image, process, and state boundary

The candidate runtime service would have `restart: "no"`, no published port,
no data/backup/host/Docker-socket mount, only private `record-net`, a read-only
root filesystem, bounded `tmpfs`, all capabilities dropped, no new privileges,
and numeric user `10001:10001`. Container exit status is the CLI exit status;
Compose or daemon failures before entrypoint execution remain platform errors
and cannot be relabelled as a CLI domain result.

Record data, search cursors, ETags, drafts, and paging history exist only in
process memory. Redirection creates a host-owned output file outside the CLI's
authority. The image does not discover Docker, persist a cache, inspect the host
working directory, or use a background process.

## Security and permitted-use boundary

- Record content may appear only in explicit success output requested by the
  invoking user; diagnostics, logs, process titles, completions, evidence, and
  release metadata remain minimized and redacted.
- The CLI has no authentication option because the accepted product has no
  application account system; this is a limitation of the loopback/private
  Compose profile, not evidence of general access control.
- No secret, token, or credential is a supported CLI input. The image has no
  runtime outbound dependency and reaches only the compatible private API.
- Fixtures and examples must be purpose-created synthetic or supported by an
  external de-identification record and must also satisfy the NIST restrictions.
- Actual or possible ePHI, production/confidential records, remote or
  multi-user access, shared-workstation use, third-party processing, telemetry,
  or formal certification/compliance claims trigger successor review and are
  not authorized by this realization.
- Architecture vectors and a clean image scan cannot substitute for the NIST
  and HIPAA policy/evidence gates for the exact CLI artifact.

## Security-policy applicability

| D5 concern | NIST policy anchors | HIPAA policy anchors | Candidate evidence direction |
|---|---|---|---|
| Permitted use and truthful claims | `SEC-POL-01`, `SEC-POL-14` | `HSP-001`, `HSP-002`, `HSP-015` | Data/fixture manifest, limitation text, negative successor-trigger review, no broad compliance claim |
| Fixed access/network path | `SEC-POL-02`, `SEC-POL-03`, `SEC-POL-06` | `HSP-004`, `HSP-005`, `HSP-006` | Private-DNS route inventory, no credential/alternate URL, mount/network/socket negatives |
| Input, output, and failures | `SEC-POL-06`, `SEC-POL-07`, `SEC-POL-08` | `HSP-006`, `HSP-007`, `HSP-008` | Bounded stdin, strict parsing, stream/exit goldens, redaction canaries, indeterminate-write evidence |
| Ephemeral state and continuity interface | `SEC-POL-05`, `SEC-POL-09`, `SEC-POL-13` | `HSP-007`, `HSP-010`, `HSP-012` | No durable client copies, accurate unavailable/interruption behavior, incident/reconciliation exercise |
| Image and release integrity | `SEC-POL-04`, `SEC-POL-10`, `SEC-POL-12` | `HSP-009`, `HSP-013` | Exact image/wheel hashes, SBOM/provenance/signature disposition, scan/license/external-service evidence |
| Secure development and assurance | `SEC-POL-11` | `HSP-003`, `HSP-014` | Named owner, risk mapping, architecture/policy/vector traceability, exact method/results/limitations/reviewer |

Every policy requires an exact applicability decision in future governed work.
This table routes evidence; it creates no implementation result, pass, waiver,
or accepted exception.

## Required invariant verification

The minimum D5 claim would require the exact `CLI` vectors, without weakening
or replacing them:

| Vector | Candidate evidence obligation |
|---|---|
| `CLI-001` | Run pinned help/version through released Compose material outside source checkout; prove exit `0`, exact SDK wheel identity, and no host install/API side effect. |
| `CLI-002` | Prove create/get/update and normalized no-op human/JSON success, exit `0`, and one SDK write call per user action. |
| `CLI-003` | Exercise option/stdin sources including redirected, multiline, empty, invalid, and conflicting cases; prove no host path/mount access and pre-SDK exit `2`. |
| `CLI-004` | Prove one-page, all-pages, max-pages, and empty search ordering and truthful completion metadata. |
| `CLI-005` | Prove next/previous records and boundaries, exit `0`/`4`, and no wrap. |
| `CLI-006` | Prove exact `2/3/5/6/7/8/9` failure classes with stdout empty. |
| `CLI-007` | Prove exactly one JSON document on the correct stream with LF and no ANSI/diagnostic mixing for every class. |
| `CLI-008` | Interrupt before and after write dispatch; prove exit `130`, accurate outcome guidance, and no replay. |
| `CLI-009` | Use sensitive/control-like fixtures; prove requested success data is not amplified into diagnostics, logs, or process titles. |
| `CLI-010` | Prove public SDK-only dependency and absence of HTTPX/SQLite/API implementation imports and hidden commands. |
| `CLI-011` | Inspect effective container runtime; prove no ports/mounts/socket/lifecycle/root escape/alternate route and only private `record-api:8000/api/v1`. |

Applicable `DOM`, `HTTP`, `SRCH`, `NAV`, `CNT`, `OPS`, and `E2E` vectors also
remain required. In particular, cross-surface route parity, immutable wheel
copy identity, safe logs, container hardening, API unavailability/recovery,
same record/search/navigation results, and clean-host Compose lifecycle cannot
be inferred from the CLI-only goldens.

## Evidence-record boundary

Any future execution record must identify at least the evidence ID;
`ARC-SUITE-001@2.0.1` and vector IDs; NIST/HIPAA suite, policy, and gate IDs;
D5 semantic version, image digest, SDK wheel hash, Compose/render hash, source
commit; host/OCI/Python/dependency/API identities; exact containerized command,
configuration, fixture seed, and static/mock/live/end-to-end method; UTC time;
per-vector results; limitations; nonpass dispositions; and reviewer identity.

Help output, screenshots, coverage, an image scan, a Compose exit code, or one
successful local invocation alone cannot prove the D5 claim.

## Dependencies and handoffs

| Relationship | Required identity | Boundary preserved |
|---|---|---|
| `v1.0` / D1 -> D5 | Exact architecture/contract revision and derivative documentation used | Documentation guides the CLI but does not prove it. |
| `v2.0` / D2 -> D5 | Exact CLI build/runtime target, effective Compose model, network/security controls, base/image identity | D5 does not claim the platform gate. |
| `v2.1` / D3 -> D5 | Compatible API image, route/problem/search behavior, live endpoint identity | CLI cannot add routes, manage the server, or open SQLite. |
| `v2.2` / D4 -> D5 | Exact released wheel filename/version/SHA-256 and supported API major | CLI consumes the public wheel unchanged and cannot import internals. |
| D5 -> `v4.0` / D6 | Shared capability/result and route-parity evidence | CLI delivery precedes web, but D5 neither implements nor completes D6. |

## Risks to preserve for proposal analysis

| Risk | Consequence |
|---|---|
| CLI implements transport directly | SDK compatibility and one-client-path authority are bypassed. |
| CLI image rebuilds the wheel | Tested, published, and consumed bytes no longer match. |
| A URL override or Docker discovery is added | The accepted fixed private trust boundary silently expands. |
| File-path convenience requires a host mount | The no-mount and host-data boundary is violated. |
| Retry logic replays a write | Duplicate create or unintended update may occur after an unknown outcome. |
| Human and JSON streams mix | Automation can parse a diagnostic as data or miss a failure. |
| Record/query values enter errors, logs, completions, or process titles | Sensitive content is amplified beyond explicit success output. |
| Compose start failure is mapped to a CLI exit class | Platform absence is falsely reported as a domain result. |
| CLI passing tests claim D3/D4 or security completion | Independent product and additive security gates are obscured. |
| Host installation becomes documented or tested | The product conflicts with the Compose-only architecture. |

## Questions that remain for a future proposal

1. Which exact repository and product paths own CLI source, generated help or
   completion material, image definition, release metadata, and evidence?
2. Which parser/formatting libraries and dependency patch locks fit the
   accepted image and public-SDK-only boundary?
3. Which CLI semantic version and compatibility policy are proposed without
   confusing them with this `v3.0` realization-suite label?
4. How will process-level fault injection distinguish pre-dispatch,
   post-dispatch, interruption, broken-pipe, and pre-entrypoint Compose failure?
5. Which owner is accountable for release risk analysis, vulnerability and
   license review, safe-output review, incident exercise, and evidence retention?
6. Does any generated completion or automation integration have a different
   owner, destination, lifecycle, or independently acceptable claim that
   triggers a separate dot-version suite?

No answer is selected by this note.

## Candidate outcome

A local user or automation caller can invoke one exact, disposable Compose CLI
image to create, retrieve, update, search, and navigate records through the
released SDK and shared API; receive deterministic human or JSON output and an
accurate exit class; and terminate without host installation, durable client
state, direct transport/database access, hidden retry, or a claim broader than
the independently evidenced D5 artifact.

## Suggested next step

Take no initiative action now. If later explicitly directed, prepare one
D5-only proposal from this realization, cite the exact invariant sources and
policy IDs, identify the compatible D2-D4 artifact hashes, choose product
destinations and owners, perform the mandatory scope assessment, and preserve
all unresolved choices for explicit human disposition.

## Handoff notes

A receiving proposal must cite this realization and its `v3.0` suite, preserve
the historical Product 3 lineage, distinguish suite identity from product
semantic version, map every candidate output and failure to authoritative
contracts and additive security evidence, and avoid treating this detail as an
accepted specification or implementation authorization.

