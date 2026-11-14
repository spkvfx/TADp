# Codex prompt keyword specification

## Purpose, authority, and adoption

This document is the canonical directive contract and extensible keyword
registry for every task in governed TADp scope. Read and apply it to ordinary
requests, analysis, project-local prompts, numbered workflow prompts, and
repository-maintenance prompts. Reading this document does not activate its
examples, the registry, or any switch. These rules govern interpretation;
they do not expand a task's target, edit boundary, or authority.

### Revision record

- **Authority:** The User's 2026-11-12 instruction to execute
  `prompts/positional-gate-switches-protocol-change.md`, preserved in
  [KWD-DR-001](../../../decisions/KWD-DR-001-positional-keywords.md), authorizes
  this exact addition and its necessarily affected protected-source consumers.
- **Reason:** Make positional prompt settings, declared list scheduling, and
  specifically authorized exceptions explicit without losing lock protection
  or truthful evidence.
- **Affected scope:** This registry; the suite index and specifications 01, 02,
  04, 07, 08, and 10; universal entry points; workflow and decision templates;
  prompt consumers; machine interpretation, validation, tests, and guidance.
- **Effective event:** The first Git commit containing this coherent revision,
  reconciled consumers, verification, and specifically authorized locks.
  Adoption records identify that commit and the project's governing revision.
- **Compatibility and migration:** Apply prospectively after recorded adoption.
  Existing projects and initiatives retain their recorded governing revision
  until the applicable adoption and exception authority are recorded. Do not
  reinterpret historical prompts, waive an existing gate, answer a question,
  accept an initiative, reopen a claim, or change a lifecycle record merely
  because the vocabulary is installed. See the
  [migration guide](../../../docs/guides/prompt-keywords-migration.md).
- **Successor relationship:** This specification succeeds earlier clauses only
  for directive interpretation, list scheduling, and the documented exception
  route. Earlier rules remain the default and govern every unexcepted matter.
  Git retains their source identity and prior revisions. Stage numbering,
  initiative types, substantive-successor rules, and ordinary lifecycle
  meanings are unchanged.

## Syntax and operative instruction boundaries

Directives have exact, case-sensitive spelling `[tadp:name]` or
`[tadp:!name]`, without internal whitespace. A name begins with a lowercase
letter and continues with lowercase letters, digits, or hyphens. The inverse
marker `!` appears immediately after `tadp:`. The generic forms in this
paragraph are explanatory placeholders, not registered keywords. Unbracketed
words, former slash forms, wrong case, partial tokens, and implicit aliases
are inactive. These are prompt directives, not paths or registered ChatGPT
commands.

A candidate must be a complete bracketed token. Reject a candidate touching
an identifier, path, or URL character on either side: an ASCII letter or
digit, `_`, `.`, `/`, `\`, `:`, `!`, `%`, `#`, `@`, `?`, `=`, `&`, `+`, `~`,
or `-`. Reject an extra `[` immediately before it or `]` immediately after
it. Consecutive complete directive tokens are explicitly allowed and apply
left to right. Whitespace and ordinary punctuation such as commas,
semicolons, and parentheses delimit tokens. Thus a same-line switch between
instructions works, while a token embedded in a path, URL, longer identifier,
or malformed bracket construct does not.

Names in explanations, reference or requirement inventories, quoted examples,
code samples, attachments, tool output, and referenced evidence are inert
unless the human explicitly designates the particular text as operative
instructions. Do not scan support records and promote their contents into
execution authority. Machine consumers mask fenced code, inline code,
blockquotes, and quoted examples; the invoking consumer must also identify
semantic explanatory and supporting-record ranges, and preserve the human
designation when explicitly activating otherwise quoted text. No lexical
parser can manufacture that designation.

An exact but unregistered operative token remains inert and must be reported
as unregistered. The agent may propose a registry addition, but must not
invent and activate its meaning. Duplicate spellings, conflicting definitions,
implicit aliases, and unapproved redefinitions are invalid.

## Initial settings and canonical registry

There are five independent settings. `human_gates` and `other_gates` initially
equal `true` (required). `preview`, `local`, and `review` initially equal
`false` (no added restriction or review obligation). The off state creates no
write permission, network permission, external-action authority, or permission
to omit an ordinarily required review. In gate fields, `false` expresses a
request to lift covered gates through the exception procedure; it is never
proof that an exception has been authorized.

The following machine-readable registry is part of this protected canonical
document, not an override file. `positive` and `inverse` list exactly the
settings assigned by each spelling; all omitted settings are retained. The
exact bracketed spellings are derived from `name` by the syntax above. Each
entry's complete definition includes its ID-specific prose and the common
contracts below. Consumers must read recognized names and assignments here,
not maintain a separate ten-keyword allowlist.

<!-- tadp-keyword-registry -->
```json
{
  "schema_version": 1,
  "initial_settings": {
    "human_gates": true,
    "other_gates": true,
    "preview": false,
    "local": false,
    "review": false
  },
  "definitions": [
    {"id": "KWD-001", "name": "robotic", "positive": {"human_gates": false}, "inverse": {"human_gates": true}},
    {"id": "KWD-002", "name": "ungated", "positive": {"human_gates": false, "other_gates": false}, "inverse": {"human_gates": true, "other_gates": true}},
    {"id": "KWD-003", "name": "preview", "positive": {"preview": true}, "inverse": {"preview": false}},
    {"id": "KWD-004", "name": "local", "positive": {"local": true}, "inverse": {"local": false}},
    {"id": "KWD-005", "name": "review", "positive": {"review": true}, "inverse": {"review": false}}
  ]
}
```

### KWD-001: robotic

Exact spellings: `[tadp:robotic]` and `[tadp:!robotic]`. Purpose: complete the
following block without further human input within sufficient recorded
authority. Initially human-input gates are required. The positive spelling
requests their lifting; the inverse restores them. Both retain other-gate,
preview, local, and review settings. A human-input gate is a requirement for
a human answer, confirmation, disposition, acceptance, or reopening. An
automated failure still blocks unless its distinct gate is also specifically
excepted. The switch alone cannot approve its own inferred use or grant
unbounded authority. Acceptance case: after an ungated block, the inverse
restores human-input gates while other gates stay lifted.

### KWD-002: ungated

Exact spellings: `[tadp:ungated]` and `[tadp:!ungated]`. Purpose: request
completion of the following block without gate stops within specific exception
authority. Initially both gate classes are required. The positive spelling
requests lifting both; the inverse restores both. Preview, local, and review
are retained. Other gates include automated checks and workflow prerequisites;
each still needs its own applicable waiver. Locks, authority, actual capability,
and truthful evidence are never lifted. Acceptance cases: robotic following
ungated leaves other gates lifted; inverse ungated restores both gate classes
without turning earlier skipped or failed checks into passes.

### KWD-003: preview

Exact spellings: `[tadp:preview]` and `[tadp:!preview]`. Purpose: produce
proposed changes or diffs without applying them. Initially preview is off.
The positive form permits analysis, read-only inspection and checks, and
response-only proposals. It forbids file creation or modification, commits,
persisted exception records, state-changing checks, and external side effects
for the previewed work. Proposed exception records remain response-only drafts,
never adopted receipts. Read-only external lookup is possible only if local
is off and access is otherwise permitted. The inverse ends preview for
following instructions; it does not apply earlier drafts retroactively.
Both forms retain every other setting. Acceptance case: preview plus robotic
plus review still produces only a proposal and obtains independent review of
that proposal, using only specifically authorized human-gate exceptions.

### KWD-004: local

Exact spellings: `[tadp:local]` and `[tadp:!local]`. Purpose: constrain
resource access to local tools, local files, and supplied context. Initially
the added local restriction is off. The positive form prohibits browsing,
fetching, pushing, publishing, or calling external services. Independent
agents may inspect supplied or local material under the same restriction;
ordinary model inference is not external resource access for this setting.
Report unavailable remote evidence instead of claiming it was checked. The
inverse removes only this added restriction and grants no authority for an
external action. Both forms retain every other setting. Acceptance case:
local plus ungated still prohibits network access.

### KWD-005: review

Exact spellings: `[tadp:review]` and `[tadp:!review]`. Purpose: require a
distinct independent review before considering the block finished. Initially
this added review requirement is off. The positive form attaches a review
obligation to the actual or previewed output, normally by an independent agent
or reviewer. Review applicable requirements, identify findings, and reconcile
them or report unresolved issues. The producing agent's second pass is not
independent. This does not itself require a human reviewer, but existing
human-review requirements remain. An unavailable reviewer is an unmet request,
not a completed review. The inverse ends the added requirement for following
work, retaining earlier review obligations and every ordinarily mandatory
review. Both forms retain every other setting. Acceptance case: inverse
ungated leaves a prior preview, local, or review setting unchanged.

### Common definition metadata and examples

KWD-001 through KWD-005 are revision 1, authorized together by KWD-DR-001 and
effective at the coherent revision commit defined above. Their implementation
and consumer links are [the shared interpreter](../../../tools/tadp_keywords.py),
[workflow contract](../../../template/prompts/WORKFLOW-CONTRACT.md), and
[exception source](../../../template/project/initiatives/decision-receipts/gate-exception.template.md).
Their compatibility consequences are prospective interpretation only, with
no historical gate waiver. Each definition applies at source position to
nested lists, parallel branches, retries, and resumed work under the common
rules below. All require ordinary task authority; gate lifting additionally
requires the named governing rule's specific exception authority. No entry
permits weakening locks, inventing evidence, or activating an inferred
exception without confirmation.

These are inert examples, illustrating operative use only when a human supplies
the illustrated line as actual instructions:

```text
Inspect A; [tadp:robotic] resolve named questions by the authorized method; [tadp:!robotic] present B.
[tadp:ungated] perform A under EX-001; [tadp:!ungated] verify B under ordinary gates.
[tadp:preview] propose A; [tadp:!preview] inspect B without applying A.
[tadp:local] inspect supplied files; [tadp:!local] use otherwise permitted resources.
[tadp:review] prepare A and obtain an independent review; [tadp:!review] inspect B.
```

Mentioning any of these ten spellings in this registry, a quotation, a code
sample, or a support attachment is inert. The initial default and every
negative form retain ordinary permission and lock boundaries.

## Positional composition and execution ledger

Interpret operative directives left to right before dispatch. Each changes
only its declared settings for subsequent instructions until a later directive
changes them or that source prompt ends. Text before the first switch uses
initial settings. Repetition is idempotent. Headings, paragraphs, indentation,
and list boundaries do not reset state. A same-line switch affects only the
following text, never earlier instructions, decisions, drafts, or evidence.
There is no stack, implicit nesting, or implicit reset. New prompts and later
tasks start at the initial state; settings do not leak to another initiative.
A resumed execution retains its recorded source prompt and block identity.

Record an effective-settings ledger for every affected instruction block:
source prompt identity and revision, source offsets or precise block text,
effective settings, target records, exception/authority links, scheduling
parent and branch, execution or preview disposition, and retry/resume identity.
Compute these values from source position before concurrency; runtime
interleaving must never mutate another branch's settings. Retain earlier
review obligations and failed or skipped evidence after a setting changes.

## List structure and execution order

Apply scheduling only to operative action lists, at each nesting level.
Reference, requirement, option, and verification-case inventories are not
actions merely because they use list markers; quoted illustrations are inert.

| Structure | Sibling execution contract |
|---|---|
| Numbered action list | Serial, in written order. Complete each item and its applicable checks before starting the next. A blocked item blocks later siblings. |
| Bulleted or dashed action list (`-`, `*`, `+`) | Explicit parallel execution with equal priority. Dispatch ready siblings concurrently; textual position creates no priority or precedence. |
| Instructions outside a list | Agent discretion between serial and parallel execution, subject to actual dependencies and applicable rules. |

Each item includes all descendants. A numbered parent waits for every parallel
child before its next numbered sibling starts. Parallel parent branches may
each execute numbered children serially; completion of the containing item or
list joins all children. A blocked parallel sibling does not stop independent
siblings, but the list remains incomplete until every sibling has its required
disposition. Preserve actual dependencies, shared-write constraints, capacity,
gates, and locks. Report conflicts or capability limits that prevent declared
parallelism; do not silently serialize, invent priority, or claim concurrency
that did not occur. Gate switches alone do not change scheduling. A scheduling
exception needs its own exact authority and record.

Inert mixed-nesting illustration:

```markdown
1. Prepare shared inputs.
2. Run both branches:
   - Review contracts:
     1. Read contracts.
     2. Compare changes.
   - Review checks:
     1. Read checks.
     2. Identify gaps.
3. Reconcile both results after both finish.
```

## Explicit exceptions and confirmation

Requested settings and authority to except a rule are distinct. Inventory all
applicable rules and gates for each block. Identify human-input and other gates
separately and apply a waiver only when its exact scope and actual authority
cover that rule. Unexcepted rules remain binding. A supplied keyword plus
bounded instructions expresses the requested behavior; determine whether that
instruction actually supplies the governing rule's required specific authority.
The keyword alone never authorizes invariant contradictions, protected edits,
scope expansion, unavailable tools, or claims that a gate passed.

The agent may automatically author documentation from sufficient human
authority. Create the required receipt and exception record before relying on
the exception; do not require the human to write paperwork or repeat sufficient
authority solely because a record is missing. Preview permits response-only
drafts instead. If authority is absent or ambiguous, retain the rule and obtain
the exact missing confirmation before affected work.

Each exception record must preserve:

- Stable ID, actual authoring agent, capture date or event, and disposition.
- Exact original rule, source path or stable ID, governing revision, affected
  gate and class, original requirement, and precise replacement or waiver.
- Source prompt, operative spelling, exact instruction block, effective
  settings, target initiative or records, duration, and end condition.
- Exact human instruction or confirmation, actual authority, and decision
  receipt link where required; never an invented human response.
- Reason, rationale, consequences, risks, and evidence limitations.
- Any autonomous decision method, actual agent-made dispositions and author,
  affected source IDs, and reconciled consumers.
- Remaining obligations, especially locks, and reconciliation of decisions,
  lifecycle, status, verification, dependent records, and failed evidence.
- Restoration and re-entry conditions, prior state, and actual Git evidence
  when available.

Use specification 07 decision receipts and the conflict register where they
apply. Multiple gates may share a record only when each is named and human
authority clearly covers the whole bounded set. Merely recording a mode name
is insufficient. Once sufficient authority and records exist, do not introduce
repeated human stops within the same approved robotic scope. Apply the recorded
method and label results as agent-made under that authority, not human answers.

An agent-inferred switch, inferred placement, inferred meaning, or other
agent-proposed invariant exception remains inactive until explicit human
confirmation. First present proposed spellings, placement, blocks, assignments,
and exceptions. Drafting a proposal creates no approval. Capture the exact
confirmation and reconcile only its scope before use. A general request to
continue, finish, act autonomously, or avoid questions is not an inferred
invariant waiver. No switch waives confirmation for its own inferred use or
another unapproved exception. Previously sufficient authority remains usable
within its recorded boundary.

## Locks, lifecycle, and evidence reconciliation

TADp locks and protected-source rules stay enforced in every setting. No
keyword authorizes a protected edit, lock refresh or deletion, guard disable,
protected-update override, or concealment of pre-existing drift. Separately
authorized maintenance follows specific authority, preservation, coherent
consumer reconciliation, verification, and only then the affected lock update.
That maintenance authority is distinct from a mode switch.

Waived, excepted, skipped, not performed, failed, and passed are distinct
evidence dispositions. Preserve actual failures and missing evidence. Never
fabricate approval, review, tests, ownership, readiness, acceptance, release,
or completion. Restoring gates does not validate prior skipped checks or
erase agent decisions; recheck current prerequisites when later gated work
depends on earlier excepted work.

For assumptions and questions, preserve the human authorization receipt and
link the agent-made method and result to each source ID before changing its
disposition. For acceptance or reopening, name the exact governing requirement
and prior claim; general autonomous-question authority is insufficient. For
execution, record actual output, start evidence, and every bypassed prerequisite.
For completion, retain exact delivered scope and actual verification, including
failed or waived gates and dependent records. An exception permitting prompt
work is not ordinary initiative acceptance or qualification.

Ordinary `Accepted` and `Completed` retain specifications 04 and 08's meanings.
Do not assign those labels using waived approval or missing passing evidence.
Retain the last truthful lifecycle state and report bounded prompt work as
finished under the named exception with its limitations. Any proposed
replacement of a lifecycle requirement requires separately specific human
authority identifying that requirement, a documented meaning and reconciliation
for every consumer before use; a keyword or generic gate waiver alone is
insufficient. No such replacement is adopted by this vocabulary revision.
Closed claims still require recorded reopening under specification 09's bounded
realization-intake delegation or separate specific human authority. That
specification permits coherent same-outcome revision; independent outcomes and
incompatible type/owner/authority boundaries still require separate initiatives
or successors. Its delegation does not change this registry, switch semantics,
acceptance or unrelated human gates. Specifications 01 and 10 conflicts and
coherence inventories remain required unless an exact separately authorized
exception names the affected obligation, and factual conflict evidence remains
visible. Tool permissions, higher-priority instructions, factual limits, and
unavailable capabilities always bound execution. Report blockers and continue
independent authorized work.

## Adding a keyword

A user can request a precise new spelling and behavior in ordinary language.
The agent prepares the registry entry, authority receipt, impact reconciliation,
consumer changes, and verification; the human need not construct paperwork.
Registration changes this protected authority source and requires explicit
human authority naming the precise addition or revision. Automatic authorship
documents authority; it does not create it. If the agent infers the spelling,
semantics, or an invariant exception beyond that instruction, obtain explicit
confirmation before adoption or use.

Use this reusable entry format, including both JSON assignments and prose:

```text
Definition ID and revision:
Name; exact positive spelling; exact inverse spelling:
Purpose and initial state:
Positive settings assigned; inverse settings assigned; settings retained:
Positional scope; nested lists; parallel branches; retries; resumed work:
Required authority; affected rules; permitted exceptions; explicit limits:
Locks remain enforced:
Operative-use example; inert-mention example; acceptance and rejection cases:
Exact human instruction/confirmation; receipt; effective revision/event:
Compatibility/migration consequences; predecessor/history relationship:
Implementation, consumer, verification, and affected-lock links:
```

Check the name syntax, unique ID, unique positive and inverse spellings,
non-conflicting meaning, precise assignments and defaults, and all required
metadata. Reject duplicates, aliases, conflicting definitions, and revision
of an existing name without explicit revision authority. Preserve earlier
definitions and revision history; do not silently replace semantics. Update
the canonical JSON and the entry's complete prose together. New settings may
be declared with explicit defaults and assignments; unsupported behavior needs
reconciled implementation before claiming operational support. An entry does
not manufacture unavailable tool support or authorize external action.

Reconcile all affected consumers and regression cases, verify coherence, then
update only specifically authorized locks and adoption records. Never introduce
an unprotected override registry or a competing hardcoded name allowlist.

Inert worked proposal, not a registered name or adopted behavior:

```text
Proposed ID KWD-EXAMPLE; revision draft; name concise.
Spellings [tadp:concise] and [tadp:!concise].
Purpose: request brief reporting. Add initial setting concise=false.
Positive {"concise":true}; inverse {"concise":false}; all others retained.
Common positional/list/retry/resume rules apply; no rule or gate waived.
Ordinary task authority only; locks and required evidence remain enforced.
Operative example if adopted: [tadp:concise] report the local findings.
Inert example: a quotation discussing [tadp:concise].
Accept: only following report detail changes; reject: omitted required evidence.
Human authority: pending exact approval; no adoption or effective event yet.
Compatibility: prospective only, earlier definitions unchanged.
Consumers/tests/lock reconciliation: proposed, not performed.
```

Until specifically approved and registered, that proposed token is unregistered
and inert. Registration alone never activates examples or changes the default
behavior of an existing task.
