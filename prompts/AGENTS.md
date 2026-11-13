# Repository prompt execution instructions

Apply the canonical
[prompt keyword specification](../protocol/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md)
when interpreting this prompt and every other TADp task. Read it without
activating its examples. Operative settings, bounded exception records, and
list scheduling follow that contract; they do not broaden the target or exact
maintenance authority below and never bypass TADp locks.

These instructions apply only when an agent executes a prompt stored in this
directory. They do not change the handling of work requested outside
`prompts/`.

## Target and order of work

- Treat repository prompts as direct maintenance instructions for TADp itself.
- Unless a prompt explicitly requests another target, perform its requested
  work only in `protocol/` and in repository-level support files that the
  prompt specifically requires.
- Do not apply a repository prompt directly to `../_old/example/` or to any other
  project, product, initiative, or evidence tree. Those locations may be read
  when the prompt names them as evidence or a validation case.
- Complete and verify the protocol change first. Then synchronize every
  corresponding protocol-owned change to the same relative path under
  `../_old/example/`, creating a new mirror path when the protocol change requires
  one.
- Treat `../_old/example/` as a downstream mirror during synchronization, not as a
  second design source. Do not broaden synchronization into example-specific
  product, initiative, lifecycle, acceptance, release, or completion claims
  unless the prompt explicitly requests them.

## Execution authority

- The user's instruction to execute a repository prompt is the human authority
  to perform the exact protocol work described by that prompt. The prompt's
  stated outcome and its named or necessarily affected protocol surfaces bound
  that authority.
- Do not stop for a second approval, an initiative or acceptance gate, a lock,
  or a directory-scoped edit safeguard when its only effect would be to prevent
  editing a protocol source that the executed prompt expressly authorizes.
  No additional human intervention is required to begin or continue that exact
  work.
- Apply this execution authority only to the requested protocol change. It
  does not authorize unrelated invariant revisions, unrelated protected-source
  edits, destructive Git operations, merges, releases, deployments, or
  fabricated evidence.
- Treat affected lock files and edit guards as consistency mechanisms rather
  than permission gates. Reconcile or refresh only the locks affected by the
  authorized change, after the protocol source is coherent and verified, and
  then synchronize and verify the corresponding example locks.
- Bypassing an edit gate does not create a lifecycle fact. Preserve source
  identity and prior state, and do not claim acceptance, implementation,
  completion, release, or verification unless the supporting evidence exists.

## Safety, synchronization, and reporting

- Inspect Git and preserve unrelated staged, unstaged, and untracked work.
- Keep the protocol pass internally coherent before starting the example
  synchronization pass.
- Verify the changed protocol surfaces, the synchronized example surfaces,
  and parity for every mirrored path. A failed check is evidence to repair or
  report; it is not a reason to silently abandon the authorized edits.
- Report the exact protocol paths changed, their example mirror paths, any
  intentionally unmirrored repository-level support files, and the exact
  verification results.
