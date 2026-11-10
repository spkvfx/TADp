# Superseded native-runtime deployment baseline

**Revision ID:** `ARC-REV-001`  
**Status:** Superseded  
**Predecessor:** `ARC-SUITE-001@1.0.0`  
**Successor:** [`ARC-SUITE-001@2.0.0`](../../00-architecture-suite-index.md)  
**Original effective date:** 2026-11-10  
**Superseded date:** 2026-11-10  
**Original authority:** User instruction to create authoritative invariant architecture using Codex best judgment  
**Supersession authority:** User, project authority, through the exact instructions preserved below  

## Purpose

This record preserves the deployment and packaging meaning of architecture
revision `1.0.0` that was accepted earlier in the same architecture-creation
session. The successor changes those claims to a container-only deployment.
All unaffected domain, API, data, search, navigation, concurrency, and
evidence-governance claims carry forward into `2.0.0` unless the successor
explicitly says otherwise.

The active files remain numbered `00` through `24`. This historical record is
kept under `revisions/1.0.0` so directory reading order and predecessor identity
are both preserved.

## Exact supersession instructions

> make this fully dockerized.

> I don;t want to install all the services on teh host. make taht decision now
> and add to the architecturer invaraint

These instructions explicitly authorize the deployment-invariant change. They
do not authorize implementation or a product-completion claim.

## Preserved revision 1.0.0 claims

The following accepted claims are superseded, not erased:

| Prior record/subject | Exact prior meaning preserved here | Successor disposition |
|---|---|---|
| `ARC-SUITE-001@1.0.0` architecture shape | Browser and a natively run API used host loopback; a natively installed CLI used a natively installed Python SDK; the API opened a host-configured SQLite file. | All application execution moves into Compose-managed containers; only the browser and Docker runtime remain on the host. |
| `ADR-004@1.0.0` trust boundary | The API process itself was required to bind an IP loopback address and reject wildcard/non-loopback binds. | The API binds `0.0.0.0:8000` inside an isolated Compose network; Docker alone publishes it to host `127.0.0.1`. Host publication remains loopback-only. |
| `ADR-005@1.0.0` runtime stack | Host-supported CPython, Uvicorn, FastAPI, Pydantic, SQLite, RE2, HTTPX, SDK wheel, CLI wheel, and web build tools formed the runtime/build compatibility target. | Those technologies remain inside pinned Linux OCI images and build stages; none is installed as a host runtime prerequisite. |
| `ARC-BND-003` / `ARC-CTR-004` placement | `EXAMPLE_RECORDS_DB_PATH` selected an absolute host-local database path; the API held an adjacent host lock. | The live database path is fixed inside the API/maintenance images and stored in a Compose named volume; host bind mounts are prohibited for live SQLite. |
| `ARC-BND-004` / `ARC-CTR-005` SDK distribution | The SDK wheel could be installed directly into a supported host CPython. | The wheel remains a versioned build artifact and is installed into CLI/test/developer images; running the example never requires a host SDK/Python install. |
| `ARC-BND-005` / `ARC-CTR-006` standalone CLI | "Standalone" meant a wheel installed with `pipx` or equivalent and invoked as host `recordctl`. | "Standalone" means an independently versioned CLI OCI image invoked through `docker compose run --rm record-cli`; no host Python/pipx/SDK install. |
| `ARC-CTR-008` supported deployment | Native Windows 11 and Ubuntu host processes were required; containers were development-only unless separately evidenced. | Docker Engine/Desktop with Compose is the runtime boundary; released Linux OCI images run consistently across accepted Docker hosts. |
| Backup/restore | The host service used API/maintenance procedures against host-local database and backup paths. | A networkless one-shot maintenance container exclusively mounts the data and backup named volumes while API is stopped. |

## Reason and scope

The User does not want application services or their language/database
toolchains installed on the host. Revision `2.0.0` therefore changes:

- deployment topology and trust enforcement;
- runtime/build/test prerequisites;
- database and backup placement;
- SDK/CLI packaging and invocation;
- configuration, health, maintenance, and recovery procedures;
- supported-platform claims; and
- conformance vectors and delivery evidence.

It does not change record fields, normalization, UUID identity, ordinal order,
ETag concurrency, HTTP resource semantics, search membership, regex dialect,
navigation, excluded domain capabilities, or evidence authority.

## Compatibility and migration effect

No API, SDK, CLI, web, database, release, or initiative implementation evidence
existed when the change was instructed. There is therefore no delivered user
state or accepted product requiring an in-place migration. All future delivery
must target `ARC-SUITE-001@2.0.0`; a native-host implementation of `1.0.0`
would be historical/nonconforming and may not be reported as current.

If an unrecorded local prototype exists, preserve it as observed evidence,
export its database only through a separately accepted migration procedure,
and do not mount its host file directly into the v2 runtime without integrity,
schema, ownership, backup, and rollback verification.

## Affected active records

Revision `2.0.0` reconciles at least:

- `00`, `01`, `02`, and `03` for suite authority, source decisions, and system
  boundary;
- `04`, `07`, `08`, `09`, and `10` for persistence topology, trust, stack,
  versioning, and delivery decomposition;
- `12`, `13`, `15`, and `16` for API/network/database/maintenance behavior;
- `17` through `23` for SDK, CLI, web packaging, interaction, and operations;
  and
- `24` for Docker-specific conformance and evidence gates.

## Verification obligation

The successor must prove that:

- active root records remain continuously numbered `00` through `24`;
- every active deployment claim is container-only and links this predecessor;
- host prerequisites exclude Python, SDK, CLI, Node, SQLite, RE2, FastAPI,
  Uvicorn, and application service installation;
- Compose publishes only loopback, the CLI uses only the private network, and
  only API/maintenance containers can mount the live data volume under mutually
  exclusive operation; and
- no native-runtime instruction remains as an active conformance path.

