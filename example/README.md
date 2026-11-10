# TADp Example Record Application

This directory presents a complete worked example of the Traceable
Architecture Design Protocol (TADp) through a small, local record-management
application. The application carries an initial request through realization,
evidence reconciliation, explicit human decisions, authoritative architecture,
security policy, delivery, and verification in narrowly scoped, traceable
initiatives.

## Application

The application manages records with three public fields:

- `id`: an immutable, service-generated UUID;
- `name`: editable text; and
- `value`: editable text.

Users can create, retrieve, and update records; move to the next or previous
record in a deterministic order; and search by an accepted field using exact,
prefix, suffix, contains, or regular-expression matching.

The application uses a local, single-user architecture in which:

- a versioned HTTP API owns record behavior and is the only normal runtime
  component that accesses the live SQLite database;
- a Python SDK, one-shot command-line client, and browser interface use the
  same `/api/v1` contract and semantics;
- Docker Compose provides the supported build and runtime path, without
  installing the application toolchain or services directly on the host; and
- operation is limited to non-production demonstration and test data that
  satisfies the applicable security-policy restrictions.

Deletion, bulk mutation, record history, application accounts, remote
multi-user access, and regulated production use are outside the accepted
example boundary.

## What the example demonstrates

The repository material demonstrates how TADp can:

- preserve an initial realization without treating it as an accepted
  specification;
- distinguish authoritative evidence from contextual or non-authoritative
  material;
- retain explicit human authority and decisions alongside the records they
  govern;
- turn a broad application idea into versioned boundaries, contracts, policy,
  and independently reviewable delivery units;
- keep architecture, security policy, future initiatives, products, tests,
  and completion claims traceable without allowing lower-authority material to
  rewrite a governing invariant; and
- use Git and Codex as part of a reviewable, evidence-backed workflow.

Useful starting points are:

- the original [application realization](evidence/non-authoritative/realizations/v0.0/RZN-001-example-record-application.md);
- the accepted [architecture suite](evidence/authoritative/architecture/00-architecture-suite-index.md);
- the example [NIST-aligned security-policy suite](evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md);
- the example [HIPAA-aligned security-policy suite](evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md); and
- the [initiative workflow guide](docs/development/initiative-workflow.md).

## Security evidence status

The NIST- and HIPAA-aligned security-policy suites are provided as example
evidence. Their relationships to the realization, architecture, future
initiatives, delivery gates, and verification requirements demonstrate the
effects that security evidence can have on a TADp workflow.

Those suites are prospective examples, not current assessment results. Their
presence does not establish that a product exists or that the proposed
product, architecture, realizations, initiatives, designs, code, tests,
configuration, documentation, or any other intermediate material conforms to
NIST or HIPAA guidelines. Nothing in this example is a NIST or HIPAA
compliance claim.

## Status and disclaimer

> **Protocol demonstration only:** The README presents the application in its
> complete end-state form so the workflow can be understood from beginning to
> end. The repository material is a protocol workflow demonstration, not proof
> that a product or intermediate artifact has actually been implemented,
> tested, released, validated, or certified. Not all evidence, realizations,
> initiatives, product records, verification records, intermediate artifacts,
> or other material in the example has been fully validated, reviewed,
> reconciled, accepted, implemented, or completed.

An accepted architecture or prospective policy describes what future work must
satisfy; it does not prove that a product or control exists. Passing the TADp
validator checks protocol structure and traceability rules only. It does not
replace architecture review, product testing, security assessment, legal
review, release approval, or evidence from a running system.

Do not use this example with actual or possible electronic protected health
information (ePHI), production data, confidential data, credentials, or other
sensitive material.

This README is explanatory. The applicable records under
[`evidence/authoritative`](evidence/authoritative/README.md) remain the binding
source for the example's accepted architecture and policy.
