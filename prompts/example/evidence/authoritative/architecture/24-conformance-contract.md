# Architecture to product conformance contract

**Architecture ID:** `ARC-CTR-009`  
**Status:** Accepted  
**Architecture revision:** `2.0.1`  
**Contract owner:** Project architecture authority  
**Producer:** This accepted architecture suite  
**Consumers:** Future documentation, API, persistence, SDK, CLI, web, operations, and release initiatives  
**Last reviewed:** 2026-11-10  

## Purpose and scope

This contract defines the minimum evidence required to claim that a product
conforms to architecture revision `2.0.1`. It supplies stable vector IDs,
verification layers, fixture rules, delivery gates, and traceability
expectations. It does not claim that any vector currently passes. Detailed
architecture is a test oracle, not execution evidence.

## Current evidence status

| Delivery unit | Implementation exists? | Conformance evidence exists? | Permitted claim now |
|---|---:|---:|---|
| `D1` architecture/contracts | This accepted suite exists | Structural verification must be recorded with this change | Architecture baseline created; no initiative completion implied |
| `D2` container platform/runtime packaging | No evidence supplied | No | Required behavior only |
| `D3` API/SQLite runtime image | No evidence supplied | No | Required behavior only |
| `D4` Python SDK artifact | No evidence supplied | No | Required behavior only |
| `D5` CLI image | No evidence supplied | No | Required behavior only |
| `D6` web bundle | No evidence supplied | No | Required behavior only |

Absence of a failure, detail in this suite, generated code/schema, or a future
unit test alone cannot be reported as product conformance or completion.

## Architecture-suite structural verification

On 2026-11-10, a repository-local read-only verification checked the delivered
architecture directory and observed:

| Check | Observed result |
|---|---|
| File sequence | 25 active root Markdown records, exactly one filename for every prefix `00` through `24`; one nested immutable predecessor record under `revisions/1.0.0` |
| Primary identities | 26 primary IDs across active plus archived records, all unique |
| Source decisions | 17 disposition rows covering `RZN-001-Q01` through `RZN-001-Q17` |
| Local links | All 202 Markdown relative-link references resolve to existing targets |
| Template residue | No unexpanded template variable or planning residue |
| Numbering-link integrity | No doubled numeric filename prefix |
| Record integrity | Each record has one H1, balanced code fences, and a final newline; every active header identifies revision `2.0.1` |
| Cross-suite reconciliation | Architecture `2.0.1`, NIST `1.0.1`, and HIPAA `1.0.1` identify one another, preserve their separate ownership, and require additive evidence for applicable future claims |

The check returned zero structural errors. It verifies suite assembly only; it
does not prove semantic correctness, human review beyond the recorded
instructions, initiative completion, or any D2-D6 product behavior.

## Conformance method

Every product claim must:

1. name architecture suite/revision, applicable NIST and HIPAA suite revisions,
   and product version/commit/artifact hash;
2. list the applicable stable vectors below and any additional contract tests;
3. record Docker Engine/Desktop/Compose/BuildKit versions, rendered Compose
   hash, OCI platform/image/manifest digests, wheel/bundle hashes, dependency/
   engine/database schema versions, browser/Python/host matrix, named-volume
   identities, and exact containerized test command/tool version;
4. preserve machine-readable test output plus a human-readable summary;
5. map each failure/skip/xfail to an owner and disposition rather than exclude
   it silently;
6. distinguish isolated mocks from live-component and end-to-end evidence;
7. prove negative boundaries through inventory/static/security tests as well as
   positive behavior; and
8. link the evidence from the governing initiative's completion record and
   product record; and
9. show that the exact same artifact and claim satisfy every applicable
   architecture vector, `SEC-POL-*` requirement, and `HSP-*` requirement.

Host-native project commands are not conformance evidence for v2. Every
automated project check must run through a declared BuildKit target or Compose
service/profile; a host browser remains valid for manual user-agent testing.

A vector may be automated at more than one layer. The highest layer does not
replace lower-layer fault/edge evidence, and a mock cannot prove live
interoperability.

## Test fixture and isolation rules

- Each test run uses a unique test Compose project, private network, and new
  disposable named data/backup volumes. It must not resolve, mount, copy, or
  inspect release/user volumes.
- Tests initialize schema v1 only through the maintenance entrypoint, then
  start one API container/worker. Browser tests publish an OS-assigned IPv4
  loopback port unless a vector specifically verifies the fixed release port;
  container clients use `record-api:8000`. Both use `/api/v1`.
- Fixtures create records only through the API except persistence-layer tests
  that explicitly own direct schema/adapter setup. Direct fixture SQL may not
  be used to make an end-to-end behavior pass.
- Time, UUID generation, retry delay, and fault injection may be controlled
  through explicit test seams. Production defaults remain OS CSPRNG/UTC clock.
- Test assertions compare canonical Unicode scalar content and ordered IDs,
  not terminal rendering alone.
- Logs, stdout/stderr, browser storage/network, database files, and response
  bodies are inspected for prohibited leakage/bypass where applicable.
- Parallel tests use separate Compose project, network, named volumes, lock,
  loopback port, and container identities.
- A test must fail closed when a required dependency/browser/platform is
  unavailable. Release evidence cannot mark a required matrix entry skipped.
- Golden/snapshot updates require review showing why accepted meaning did not
  change; regenerating snapshots is not itself acceptance.
- Test containers never mount the Docker socket or live volumes. Fault
  injection uses declared seams/volumes or host-side Docker orchestration, not
  privileged application containers.

## Verification layers

| Layer | Minimum subject | Must prove | Cannot prove alone |
|---|---|---|---|
| Architecture/static | Imports, dependencies, routes, public symbols, commands, schemas, links | Boundary/negative inventory and traceability | Runtime correctness |
| Container/build | Dockerfile stages, image contents, Compose render, networks, mounts, user/capabilities/limits, digests/SBOM/provenance | Reproducible topology, isolation, clean-host path, artifact identity | Domain/API correctness |
| Domain/unit | Normalization, validation, matching helpers, state reducers | Pure accepted transformations and edge behavior | HTTP/database/client integration |
| Persistence integration | Real SQLite engine, migrations, transactions, backup | Schema, atomicity, concurrency, recovery | Public API/client behavior |
| API contract | Live API over real store | HTTP, models, errors, search/navigation | SDK/CLI/web packaging and UX |
| SDK contract | Mock transport plus live API | Public Python API, retries/errors, wire conformance | CLI process or browser behavior |
| CLI process | One-shot CLI image plus live API container | Grammar, streams, exit codes, live behavior, no-mount isolation | Browser accessibility |
| Web component/browser | Container-built embedded assets plus live API image | State, accessible interaction, security/storage, browser matrix | CLI/SDK packaging |
| End-to-end/recovery | Released digest-pinned Compose artifacts together | Cross-surface equality, shared `/api/v1`, clean-host operation, and recovery | Unsupported remote/multi-user claims |

## Required domain vectors

| ID | Scenario/input | Required result |
|---|---|---|
| `DOM-001` | Create with `name="  Alpha  "`, `value=" x "` | Stored/returned name `Alpha`; value preserves both spaces; canonical UUIDv4 |
| `DOM-002` | Name/value contain decomposed `Cafe\u0301` | Both normalize to NFC `Café`; later exact search with either form matches |
| `DOM-003` | Name contains CR/LF, TAB, NUL, C0/C1, `U+2028`, or `U+2029` (one case each) | Entire request rejected; no row/ordinal/revision committed |
| `DOM-004` | Value contains CRLF and lone CR | Returned/stored value uses LF at both positions |
| `DOM-005` | Empty value with valid name | Accepted; exact empty Value search can find it |
| `DOM-006` | Empty/whitespace-only normalized name | Rejected; whitespace-only value remains accepted if bounded |
| `DOM-007` | Boundary lengths 120/121 code points and 480/481 bytes for name | Exact accepted/rejected boundary under both limits |
| `DOM-008` | Boundary lengths 4,096/4,097 code points and 16,384/16,385 bytes for value | Exact accepted/rejected boundary under both limits |
| `DOM-009` | Create/patch includes `id`, unknown field, null, wrong scalar type, or empty patch | Strict validation rejection; no state change |
| `DOM-010` | Create two identical name/value pairs | Two records with different UUIDs/ordinals; both retained |
| `DOM-011` | Patch normalizes to stored values | `200`, same record/ETag/revision/updated time |
| `DOM-012` | Attempt ID change through API and direct adapter/schema update | API rejects; schema trigger rejects; original record remains |

## Required HTTP vectors

| ID | Scenario | Required result |
|---|---|---|
| `HTTP-001` | Valid create | `201`, `Location`, `ETag "rev-1"`, no-store, request ID, exact closed record |
| `HTTP-002` | Valid get/absent/invalid ID | `200`+ETag / `404 record_not_found` / `400 invalid_id` distinctly |
| `HTTP-003` | Valid material patch with current ETag | `200`, selected fields changed, ID same, ETag increments exactly once |
| `HTTP-004` | Patch lacks/malforms/stales ETag | `428` / `400` / `412` distinctly; record unchanged |
| `HTTP-005` | POST/PATCH invalid JSON, duplicate keys, non-object, wrong media, oversized body | Correct `400/415/413` problem before mutation |
| `HTTP-006` | `Idempotency-Key` on POST | `400 idempotency_not_supported`; no row |
| `HTTP-007` | Unsupported methods on record resources | `405`, accurate `Allow`, problem body; no route side effect |
| `HTTP-008` | Explicit incompatible Accept header | `406 not_acceptable`; no command execution |
| `HTTP-009` | Every stable problem | RFC-style required fields/header request ID, safe detail, deterministic issue order |
| `HTTP-010` | Internal/SQLite fault contains SQL/path/value/stack | Generic client problem; prohibited details absent from response/routine log |
| `HTTP-011` | Client-supplied valid/invalid request ID | Valid retained; invalid replaced; response/log correlation consistent |
| `HTTP-012` | Connection dropped around POST/PATCH commit | Store has either atomic old/new outcome; client layer reports indeterminate when unprovable, never false success/rollback |

## Required search vectors

Seed records in ordinal order unless a vector states otherwise:

```text
1: name="Alpha" value="red apple"
2: name="alphabet" value="green apple"
3: name="beta" value=""
4: name="Café" value="line one\nline two"
5: name="ALPHA" value="a.b"
```

| ID | Scenario | Required ordered membership/result |
|---|---|---|
| `SRCH-001` | Name exact `Alpha` | Ordinal 1 only; ordinal 5 excluded (case-sensitive) |
| `SRCH-002` | Name starts_with `Al` / ends_with `bet` / contains `pha` | `[1]` / `[2]` / `[1,2]` respectively |
| `SRCH-003` | Value exact empty | Ordinal 3; empty starts/ends/contains are invalid |
| `SRCH-004` | Name exact decomposed `Cafe\u0301` | Ordinal 4 after NFC query normalization |
| `SRCH-005` | Query has leading/trailing spaces | Spaces remain meaningful; no implicit trim |
| `SRCH-006` | ID exact canonical existing/noncanonical uppercase | Existing exact match / `400 invalid_search` |
| `SRCH-007` | Regex `alpha` | Ordinal 2 only under case-sensitive unanchored search |
| `SRCH-008` | Regex `(?i)^alpha` | Ordinals `[1,2,5]` in ordinal order |
| `SRCH-009` | Regex `apple$` on Value | Ordinals `[1,2]` |
| `SRCH-010` | Regex `line.one` without/with `(?s)` on multiline Value | No ordinal 4 / ordinal 4 respectively |
| `SRCH-011` | Backreference, lookaround, malformed class, empty, or >256-byte regex | `400 invalid_regex`; no partial results/logged raw pattern |
| `SRCH-012` | Missing/partial/repeated/unknown predicate or malformed limit | `400 invalid_search` |
| `SRCH-013` | Browse/search page sizes 1 and 100; requested 0/101 | Correct page/cursor order / invalid limit |
| `SRCH-014` | Cursor round trip, changed predicate, tampered JSON/hash/range/version | Round trip continues exact order; all mismatches are `cursor_invalid` |
| `SRCH-015` | New record committed after initial page ceiling | Excluded from that cursor/context; appears in a new search |
| `SRCH-016` | Matching record updated into/out of context between pages | Current read-committed membership applies without duplication/order violation; behavior matches documented weak snapshot |
| `SRCH-017` | Evaluation exceeds 2 s injected budget | `503 search_budget_exceeded`, no items/cursor partial response |
| `SRCH-018` | API, SDK, CLI JSON, and web run same accepted predicate | Identical ordered public IDs and values |

## Required navigation vectors

| ID | Scenario | Required result |
|---|---|---|
| `NAV-001` | Browse next from ordinal 2 / previous from ordinal 2 | Ordinal 3 / ordinal 1 |
| `NAV-002` | Previous from first / next from last | `start` / `end` boundary, `200`, null record, no wrap/ETag |
| `NAV-003` | Search context `[1,2,5]`: next 1, next 2, previous 5 | 2, 5, 2 with returned record ETags |
| `NAV-004` | Current ID valid but not a member of supplied context | `409 context_mismatch`, not boundary/not-found |
| `NAV-005` | Valid ID absent / malformed | `404 record_not_found` / `400 invalid_id` |
| `NAV-006` | New record after retained ceiling | Excluded until new context |
| `NAV-007` | Current record updated out of search context | Next/previous returns context mismatch; client restarts, does not guess |
| `NAV-008` | Unchanged data repeated through every surface | Same neighbor/boundary and order every time |

## Required persistence vectors

| ID | Scenario | Required result |
|---|---|---|
| `DB-001` | Fresh named volume initialized by stopped-API maintenance | Correct ownership, application/user version, migration hash row, tables/indexes/triggers/STRICT schema/pragmas; API subsequently verifies without initializing |
| `DB-002` | API starts with missing/uninitialized/wrong app ID, old/newer/mutated migration, or failed quick check | Startup/readiness blocked; no initialization, migration, downgrade, or normal ready service |
| `DB-003` | Second API or maintenance process targets the same `record-data` volume | Exactly one obtains the shared OS lock; second fails without breaking lock/state |
| `DB-004` | Concurrent creates near capacity | At most 10,000 committed unique records/ordinals; excess stable capacity errors |
| `DB-005` | Racing patches with same ETag | Exactly one material commit; other conflict; no lost update |
| `DB-006` | Busy timeout, disk-full/read-only, injected I/O failure during write | Transaction rolls back, no false success/partial row, typed failure/readiness behavior |
| `DB-007` | Direct delete/ID/ordinal/created-at update | Trigger rejects and row remains identical |
| `DB-008` | Networkless maintenance migration fixture from every supported prior schema, including injected interruption | Mandatory pre-backup; exact transformed state or intact recoverable prior state; hash/version coherent; API remained stopped |
| `DB-009` | Offline maintenance backup to `record-backups`, export/import, then stopped-API restore | Valid hashed artifact; restored domain/search/metadata equality; former live copy preserved; no live host mount/tool |
| `DB-010` | Corrupt/invalid row or database | Never returned as partial/absent; readiness unsafe and recovery procedure invoked |

## Required SDK vectors

| ID | Scenario | Required result |
|---|---|---|
| `SDK-001` | Build wheel once, then clean container install/import/client construct/close on supported pinned Linux Python matrix | Exact wheel hash reused; no server/SQLite deps or import-time I/O; public export snapshot exact; no host Python install |
| `SDK-002` | Every valid API success | Strict immutable model with canonical values/ETag/cursor/request ID |
| `SDK-003` | Every stable API problem | Correct exception subclass/attributes; no English-text branching needed |
| `SDK-004` | Malformed success/problem/media/ETag | `ProtocolError`; no partial/coerced model |
| `SDK-005` | GET connect/502/503/504 retry conditions | At most three total attempts with accepted delay/request behavior |
| `SDK-006` | POST/PATCH transport loss before/after dispatch | Never automatically retried; determinate unavailable or `IndeterminateWriteError` accurately distinguished |
| `SDK-007` | `iter_records` normal, max-pages, repeated cursor, failure | Lazy ordered output; correct stop/protocol error; no hidden full preload |
| `SDK-008` | Log/exception inspection with sensitive record/query | Prohibited content absent; safe request correlation retained |

## Required CLI vectors

| ID | Scenario | Required result |
|---|---|---|
| `CLI-001` | Pinned `docker compose run --rm record-cli --help/--version` from release material outside source checkout | Exit 0, documented output, exact SDK wheel identity, no API start/import side effect or host CLI install |
| `CLI-002` | Create/get/update success and normalized no-op | Correct human/JSON output, exit 0, one SDK write call per action |
| `CLI-003` | Value/query from option or explicitly selected stdin (including redirected host file, multiline, empty); conflicting/invalid source | Exact canonical value or stderr/2 before SDK call; no host file bind/path access |
| `CLI-004` | Search one page/all/max-pages/empty | API order, exact JSON completion metadata, empty exit 0 |
| `CLI-005` | Next/previous record and boundaries | Record exit 0; boundary object/message exit 4; no wrap |
| `CLI-006` | Invalid usage/local data, absent, conflict, unavailable, server, search, indeterminate | Exit 2/3/5/6/7/8/9 exactly with stdout empty on failure |
| `CLI-007` | `--json` for every success/error class | One JSON document on correct stream, trailing LF, no ANSI/diagnostic mixing |
| `CLI-008` | Interrupted before/after write dispatch | Exit 130; outcome guidance accurate; no automatic replay |
| `CLI-009` | Sensitive/control-like values and query | Success data only where explicitly requested; no diagnostic/log/process-title amplification |
| `CLI-010` | Dependency/source scan | Uses SDK only; no HTTPX/SQLite/API implementation import or hidden excluded command |
| `CLI-011` | Rendered/runtime container inspection | No port, mount, Docker socket, API lifecycle side effect, root/capability escape, or alternate API path; private `record-api:8000/api/v1` only |

## Required web vectors

| ID | Scenario | Required result |
|---|---|---|
| `WEB-001` | Initial/empty, create, view, edit, cancel, save states | State/focus/actions match contract; ID never editable; no autosave |
| `WEB-002` | Double activation and late/obsolete GET responses | One write per intent; stale response cannot replace current state |
| `WEB-003` | `412` conflict | Draft preserved; Reload/Copy Draft only; no force/merge/hidden retry |
| `WEB-004` | Indeterminate create/update transport failure | No success/rollback claim; draft and reconcile actions preserved |
| `WEB-005` | Search modes, empty results, paging/back, result selection | API membership/order only; context/ceiling retained in memory |
| `WEB-006` | Search navigation boundaries/context mismatch | Accessible boundary or Restart search; no wrap/guess |
| `WEB-007` | Every validation/API/transport/protocol failure | Correct error summary/focus/live region/draft treatment/request ID |
| `WEB-008` | Malicious HTML/script/style/URL text in name/value/problem | Rendered only as text; CSP holds; no execution/navigation injection |
| `WEB-009` | Browser storage/cache/network inspection | No cookies/service worker/local/session/IndexedDB/telemetry/cross-origin data; API no-store |
| `WEB-010` | Keyboard-only, focus order, 200% zoom, 320 px, contrast, reduced motion, screen reader | Applicable WCAG 2.2 A/AA plus concrete contract requirements pass |
| `WEB-011` | Supported Chrome/Edge/Firefox/Safari matrix | Same accepted flows and results; required matrix has no skips |
| `WEB-012` | Container build/bundle/header/dependency scan | Coherent content-hashed first-party assets copied into API image, exact security controls, no runtime Node/compiler/remote dependency or host web service |
| `WEB-013` | Compare browser network route inventory to CLI/SDK route inventory | Both consume the same `/api/v1` resources/methods/problems; only loopback versus private-DNS origin differs |

## Required container-platform vectors

| ID | Scenario | Required result |
|---|---|---|
| `CNT-001` | Clean host inventory followed by build, static/unit/contract tests, initialize, start, web/CLI use, backup/restore, and stop | Docker/Compose and browser (plus Git for source build) are the only host prerequisites; no project Python/Node/SQLite/SDK/CLI/test tool executes on host |
| `CNT-002` | Render release Compose with every default/allowed setting | Exactly API/CLI/maintenance/test roles, one private network, separate named data/backup volumes, one IPv4-loopback port, fixed paths/DNS, one API replica/worker, and declared profiles |
| `CNT-003` | Attempt wildcard, IPv6, hostname, LAN, random alternate port, proxy/tunnel, host network, extra network, or arbitrary container attachment | Release/effective-config review or reachability test fails; only `127.0.0.1:${RECORDS_HOST_PORT}` and declared private service traffic work |
| `CNT-004` | Inspect mounts across all services and run forbidden access attempts | API mounts data only; maintenance mounts data/backups only under stopped-API guard; CLI/web/build/test cannot access live volumes; no live bind/anonymous/external volume |
| `CNT-005` | Inspect/run runtime containers as UID/GID 10001 with writes, privilege, namespace, socket, device, and capability probes | Read-only root, bounded tmpfs, all caps dropped, no-new-privileges, no Docker socket/host namespaces/devices; only declared writable storage succeeds |
| `CNT-006` | Exceed CPU/memory/PID/tmpfs/log/application admission limits and force OOM/kill | Declared bounds are effective; no host compromise/unbounded growth/false success; subsequent startup verifies lock/store before readiness |
| `CNT-007` | Scan API/CLI images and BuildKit stages/layers | Runtime targets contain only owned runtime artifacts; no compiler, Node/npm, test suite, source checkout, package cache, secret, or mutable install; CLI lacks API/SQLite |
| `CNT-008` | Trace SDK wheel and web bundle through build/test/runtime images | Tested/published/copied bytes and hashes are identical and tied to source/image provenance; rebuild/substitution mismatch blocks release |
| `CNT-009` | Inspect digest-qualified amd64/arm64 manifests and run applicable native/qualified matrix | Each claimed platform has exact image/manifest digest and passing vectors; mutable tag or skipped platform cannot support a release claim |
| `CNT-010` | Recreate API container/network with ordinary `down`/up while preserving volumes | Live records persist exactly; volume identity/ownership remains valid; API verifies rather than initializes |
| `CNT-011` | Attempt API/maintenance overlap and API scale above one | Shared lock and topology guards allow one owner only; second/scale attempt fails before database mutation |
| `CNT-012` | Review and execute safe lifecycle commands, then inspect destructive-command inventory | Safe stop/update/repair preserves volumes; `down -v`, volume removal/prune, and Desktop-data deletion are absent and explicitly destructive |
| `CNT-013` | Run test profile/projects in parallel and attempt live-volume/network resolution | Each uses disposable isolated identities and cannot access release state; teardown does not alter release volumes |
| `CNT-014` | Run CLI and web create/get/update/search/navigation while capturing method/path/representation/problem | Both traverse one API router and identical `/api/v1` paths/semantics; only internal versus public origin/Host differs |
| `CNT-015` | Run every maintenance command with network/socket/host-path/arbitrary-command probes | Network remains absent, Docker daemon/host paths inaccessible, command allowlist enforced, and invalid operation makes no state claim |

## Required operations/security vectors

| ID | Scenario | Required result |
|---|---|---|
| `OPS-001` | Every allowed Compose input default/boundary plus invalid/unknown `RECORDS_`/`EXAMPLE_RECORDS_` variable | Accepted typed value or fail before ready service; fixed internal path/DNS/user/security/image values cannot be operator-overridden |
| `OPS-002` | Correct/incorrect/missing public/internal Host, browser Origin, cross-origin preflight, proxy headers, host gateway, and container-IP request | Exact public/internal behavior; mismatches denied before body; no permissive CORS or proxy-derived identity |
| `OPS-003` | Inventory CLI and web HTTP traffic for every capability | Same `/api/v1` routes, methods, media, errors, ETags, cursors, and outcomes; no consumer-only route |
| `OPS-004` | Fresh initialization followed by API startup, plus missing/old/new/foreign/corrupt store cases | Only stopped-API maintenance initializes/migrates; serving API verifies and fails closed without state mutation |
| `OPS-005` | Live/ready under healthy and each unsafe store/asset/lock condition | Coarse correct status via image health command, no data/path/version leakage or health-triggered mutation |
| `OPS-006` | 64/65+ concurrent admission, worker bound, body/header/request/search deadlines, and container resource ceilings | Bounded resources and safe overload; no false partial/success or unbounded queue |
| `OPS-007` | Graceful stop and forced kill/OOM/daemon restart with idle/read/write/busy requests | Bounded drain or accurate indeterminate result; atomic store outcome; lock release/recovery verification before readiness |
| `OPS-008` | Docker/application logs for success and every failure using sensitive fixtures | Required safe fields/correlation and bounded rotation; prohibited data absent at all levels; no in-container log file/telemetry |
| `OPS-009` | CSP and browser security headers on entry/assets/API/health/error routes | Exact/equivalent restrictive policy, no cross-origin/remote asset/debug disclosure |
| `OPS-010` | Locked multi-stage release build, image/wheel/bundle hashes, manifests, SBOM/provenance/signature policy, vulnerability/license review | Traceable inputs/artifacts/findings/dispositions on both OCI platforms; no debug/test default or mutable-tag claim |
| `OPS-011` | Offline backup/export/import overwrite, framing, hash, path, volume, interruption, and network hazards | Validated generated artifact only; no live host mount/network/arbitrary path; live DB untouched; incomplete candidate rejected |
| `OPS-012` | Offline restore/migration validation, atomic switch, post-start smoke failure, and rollback | API stopped; mandatory backup; previous live preserved/recoverable; false success impossible |
| `OPS-013` | Safe stop/down/update runbook and destructive volume commands | Ordinary lifecycle preserves volumes; destructive forms are excluded, conspicuously warned, and require separate human data-loss authority |

## Required end-to-end vectors

| ID | Scenario | Required result |
|---|---|---|
| `E2E-001` | Create via CLI, retrieve/edit via web, get via SDK/API | Same ID/canonical values and revision-safe behavior everywhere |
| `E2E-002` | Create via web, update via CLI with concurrent stale web draft | CLI commit succeeds; stale web save conflicts and preserves draft |
| `E2E-003` | Full literal/regex fixture searched through API/SDK/CLI/web | Identical ordered IDs and canonical values |
| `E2E-004` | Browse/search next/previous through CLI/web | Same neighbors, ceilings, context mismatches, and boundaries |
| `E2E-005` | API stopped/restarted around each client | Explicit unavailable then recovered refetch; no direct/offline fallback |
| `E2E-006` | Offline maintenance backup, additional writes, export/import of opaque backup, then stopped-API restore | Restored point-in-time data identical across all surfaces; later writes absent; former live state preserved; no host SQLite access |
| `E2E-007` | Route/command/SDK/UI/schema inventory | No delete/bulk/record-import/record-export/history/auth/offline/direct-DB capability; maintenance backup transport is not exposed as record functionality |
| `E2E-008` | Runtime artifact/dependency/mount/network graph | CLI image -> SDK -> shared `/api/v1` -> API -> named-volume SQLite and Web -> same `/api/v1` -> API -> SQLite are the only record paths |
| `E2E-009` | Complete lifecycle from a clean supported host using released Compose material | Build/pull, initialize, start, web, CLI, test, backup/restore, stop complete without host application/runtime/tool installation |
| `E2E-010` | Capture equivalent CLI and web operations through both network origins | Identical `/api/v1` path/method/representation/problem and domain result; only Host/Origin/network entrance differs |

## Claim-to-evidence traceability

| Binding claim | Minimum vector groups |
|---|---|
| `AUTH-EX-001.1` API-exclusive persistence | `DB-003`, `CNT-004/011/015`, `CLI-010/011`, `WEB-009`, `E2E-005/008` |
| `AUTH-EX-001.2` exact three-field immutable record | `DOM-*`, `HTTP-001`-`004`, `DB-007`, `E2E-007` |
| `AUTH-EX-001.3` shared capabilities and one API path | `HTTP-*`, `SDK-*`, `CLI-*`, `WEB-013`, `CNT-014`, `OPS-003`, `E2E-001`-`004`, `E2E-010` |
| `AUTH-EX-001.4` one search contract | `SRCH-*`, `NAV-*`, `E2E-003`-`004` |
| `AUTH-EX-001.5` explicit concurrency | `DOM-011`, `HTTP-003`-`004`, `DB-005`, `SDK-006`, `CLI-006`, `WEB-003`, `E2E-002` |
| `AUTH-EX-001.6` local trust model | `CNT-002/003/005`, `OPS-001`-`003`, `OPS-009`, `WEB-009`, `E2E-005/009` |
| `AUTH-EX-001.7` independent delivery units | Packaging/dependency evidence plus `CNT-007`-`009`, `SDK-001`, `CLI-001`, `WEB-012`, `E2E-008` |
| `AUTH-EX-001.8` versioned contracts | Release metadata, compatibility diff, migration fixtures `DB-002/008` |
| `AUTH-EX-001.9` excluded product features | `HTTP-007`, `CLI-010`, `E2E-007`; distinguish opaque maintenance backup transport |
| `AUTH-EX-001.10` evidence before completion | Governing initiative source mapping, delivery/execution record, this matrix, and completion evidence |
| `AUTH-EX-001.11` Compose-only/no host application tools | `CNT-001`, `CNT-007`, `CLI-001`, `SDK-001`, `WEB-012`, `E2E-009` |
| `AUTH-EX-001.12` separate named volumes and exclusive mounts | `DB-001/003/008/009`, `CNT-004/010/011/013/015`, `OPS-011/012` |
| `AUTH-EX-001.13` hardened traceable multi-platform images | `CNT-005`-`009`, `OPS-006/008/010`, release matrix evidence |
| `AUTH-EX-001.14` additive architecture and security conformance | Applicable architecture vectors plus exact NIST and HIPAA policy/evidence mappings for one artifact and claim |
| `AUTH-EX-001.15` permitted data/use profile and successor triggers | Synthetic/de-identification record, data-flow and copy inventory, inherited-control review, negative ePHI/remote/multi-user evidence, and successor-gate disposition |

## Delivery gates

### D1 architecture/documentation gate

- Every active root file `00` through `24` exists in numeric order, has a unique
  stable ID, accepted status/authority/date, and no unresolved template token;
  superseded revision records are preserved below `revisions` and are not
  interleaved into the active reading sequence.
- All relative links resolve and all record-catalog IDs match their targets.
- `RZN-001-Q01` through `Q17` each has exactly one disposition and owning
  record in `ARC-AUT-001`.
- The current architecture, NIST, and HIPAA suite revisions cross-reference one
  another, and `RZN-001` identifies their authoritative dispositions without
  becoming a specification.
- No statement claims an implementation/test/release that lacks evidence.
- Architecture review finds no internal contradiction or unrecorded conflict.

This gate verifies the architecture artifact only. Initiative completion for a
documentation product still requires its governing workflow records.

### D2 container platform/runtime packaging gate

- All `CNT` plus applicable `OPS` and `E2E-009` vectors pass from a clean host
  on every required Docker-host and OCI-platform matrix entry.
- The multi-stage build, `.dockerignore`, Compose services/profiles/network/
  volumes/health/security/limits, image contents, immutable digests, SBOM,
  provenance/signature policy, and safe lifecycle/recovery commands are
  evidenced.
- Automated project checks use only declared containers; native application
  installation/run/test/maintenance instructions are absent.
- D2 may prove topology/artifact behavior without claiming API/domain behavior.
- Applicable `SEC-POL-*` and `HSP-*` mappings, data/fixture classification, and
  inherited-control evidence exist for the exact D2 artifacts.

### D3 API/SQLite runtime-image gate

- All applicable `DOM`, `HTTP`, `SRCH`, `NAV`, `DB`, `OPS`, `CNT`, and API
  portions of `E2E` pass on supported image/Python/SQLite/RE2/schema matrix.
- OpenAPI/schema/route inventory is reviewed against the accepted contracts.
- Containerized initialization/migration, named-volume locking, backup/restore,
  security, load/fault, embedded-web hosting, and prohibited-route/path evidence
  exists. API startup proves it never initializes/migrates.
- Product metadata names exact architecture/API/schema/image/build revision.
- The exact D3 artifact passes every applicable NIST and HIPAA evidence gate;
  architecture-vector results alone are insufficient.

### D4 SDK artifact gate

- All `SDK` plus applicable `DOM/HTTP/SRCH/NAV/E2E` vectors pass against mock
  fixtures and the accepted live D3 baseline.
- One hashed wheel is built/tested/installed in pinned containers across the
  claimed Python matrix; public API/dependency/compatibility evidence exists.
- SDK release declares supported API major, same `/api/v1` routes, and no
  SQLite/server/host-install dependency.
- SDK fixtures, examples, diagnostics, and release evidence satisfy the
  applicable NIST and HIPAA data-minimization and disclosure gates.

### D5 CLI image gate

- All `CLI` plus applicable `CNT/DOM/HTTP/SRCH/NAV/OPS/E2E` vectors pass using
  the pinned one-shot CLI image, exact released D4 wheel, and compatible D3 API.
- Human/JSON streams, exit codes, interruption/indeterminate behavior,
  no-mount/private-network packaging, identical `/api/v1` path, dependency
  graph, and excluded commands are evidenced.
- CLI output, input, diagnostics, container configuration, and release evidence
  satisfy every applicable NIST and HIPAA gate.

### D6 web bundle gate

- All `WEB` plus applicable `CNT/DOM/HTTP/SRCH/NAV/OPS/E2E` vectors pass with
  container-built assets embedded in the compatible D3 API image.
- Required browser and accessibility matrix, security headers/storage/network,
  bundle hash/provenance/runtime-content, shared `/api/v1`, conflict/race/
  indeterminate behavior, and excluded UI capability evidence exists.
- Browser storage, presentation, accessibility, network, diagnostics, fixture,
  and release evidence satisfy every applicable NIST and HIPAA gate.

No later unit's passing evidence retroactively completes an earlier unit.
Cross-product end-to-end failures block only claims that require the failing
interaction, while independent verified work remains truthfully reportable.

## Evidence record requirements

For each verification run, preserve at least:

| Field | Required content |
|---|---|
| Evidence ID | Stable initiative/product-scoped identifier |
| Architecture | `ARC-SUITE-001@2.0.1` and applicable record/vector IDs |
| Security policy | `SEC-NIST-SUITE-001@1.0.1`, `SEC-HIPAA-SUITE-001@1.0.1`, and every applicable `SEC-POL-*`/`HSP-*`/evidence-gate ID |
| Product | D1-D6 unit, semantic version, OCI/wheel/bundle/Compose artifact hash, Git commit |
| Environment | Host OS/architecture, Docker/Desktop/Compose/BuildKit, OCI platform/image digests, rendered Compose hash, Python/browser/SQLite/RE2/dependency versions, named test-volume identities, schema/migrations |
| Method | Exact containerized command/target/profile/config/fixture seed and whether static/mock/live/end-to-end/native-or-qualified-platform |
| Time | Start/end UTC and duration |
| Results | Total/pass/fail/skip plus per-vector mapping and output/artifact location |
| Limitations | Missing environment, nondeterminism, untested branch, scanner limits |
| Disposition | Owner and linked defect/conflict/decision for every nonpass |
| Reviewer | Human/automation identity and review date as required by initiative |

Screenshots alone do not prove behavior/accessibility, coverage alone does not
prove requirements, and a successful local run does not prove a required
platform/release artifact. Evidence must support the exact claim made.

## Failure and change control

- A failing vector blocks the conforming claim it traces to; do not delete,
  weaken, skip, or reword the vector to make a product pass.
- If implementation behavior conflicts with this suite, record the invariant
  conflict and correct the product or obtain an explicit architecture revision.
- If architecture and an applicable security policy appear incompatible,
  preserve both exact claims and use the invariant-conflict process; do not
  waive one evidence family or reinterpret `RZN-001` as higher authority. The
  security policy remains primary for its scope; resolve the technical design
  through an explicitly accepted architecture successor rather than changing
  policy to fit the architecture.
- If a vector is ambiguous or impractical, preserve the observation and use
  the `ADR-006` feedback process. The current requirement remains in force
  until a successor is accepted.
- New regression vectors may be added compatibly when they only prove existing
  meaning. Changing expected behavior or removing a vector requires impact
  analysis and the corresponding semantic architecture revision.
- Product-specific tests may be stricter but cannot substitute different
  behavior for the accepted vectors.

## Related records

- Suite index: [`ARC-SUITE-001`](00-architecture-suite-index.md)
- Baseline: [`AUTH-EX-001`](01-accepted-architecture-baseline.md)
- Delivery decomposition: [`ADR-007`](10-ADR-007-product-and-delivery-decomposition.md)
- Version/change governance: [`ADR-006`](09-ADR-006-contract-versioning-and-feedback.md)
- Governing protocol: [Codex invariant suite](../LLM/00_Codex_Invariant_Suite_Index.md)
- Operations/security contract: [`ARC-CTR-008`](23-operations-security-contract.md)
- Governing security suites: [`SEC-NIST-SUITE-001@1.0.1`](../security/NIST/00-nist-security-policy-suite-index.md), [`SEC-HIPAA-SUITE-001@1.0.1`](../security/HIPPA/00-hipaa-security-policy-suite-index.md)
- Superseded native deployment baseline: [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md)

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Defined revision 1.0 domain/API/persistence/SDK/CLI/web/operations conformance vectors | User-authorized best-judgment architecture completion |
| 2026-11-10 | Added D2 container-platform gate, Docker-only vectors, six-unit mapping, named-volume/offline-maintenance proofs, and shared CLI/web `/api/v1` evidence for architecture 2.0 | User's explicit Dockerization, no-host-services, and shared-API-path instructions |
| 2026-11-10 | Made NIST/HIPAA evidence additive at D1-D6 and recorded the permitted data/use and successor-gate proofs for architecture 2.0.1 | User's explicit instruction to apply the reconciliation findings in place |

