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
- The example application will be rebuilt in a separate fork. It is not a
  maintained mirror or a required synchronization or validation target for
  protocol maintenance in this repository.
- Do not apply repository prompts to `_old/example/`, another scaffold, or the
  separate example fork without a new explicit human instruction naming that
  target. Historical examples may be read when named as contextual evidence;
  they do not become the protocol's design source or adoption evidence.
- Earlier stored prompts may still request example synchronization or mirror
  parity. Those clauses are superseded by this target boundary; perform and
  verify their authorized protocol work without example synchronization.

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
  authorized change, after the protocol source is coherent and verified.
- Bypassing an edit gate does not create a lifecycle fact. Preserve source
  identity and prior state, and do not claim acceptance, implementation,
  completion, release, or verification unless the supporting evidence exists.

## Safety, verification, and reporting

- Inspect Git and preserve unrelated staged, unstaged, and untracked work.
- Keep protocol sources and their consumers internally coherent. Use
  protocol-owned isolated fixtures for regression coverage rather than
  requiring the example application.
- Verify the changed protocol surfaces and scoped repository support files.
  A failed check is evidence to repair or report; it is not a reason to
  silently abandon the authorized edits.
- Report the exact protocol and repository support paths changed and the
  exact verification results. Preserve `.gitignore`; do not force-add ignored
  historical examples or create a replacement mirror.
