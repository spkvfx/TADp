# Protected TADp reusable sources

This entire `template/` tree is reusable source material and is read-only
during ordinary project and initiative work.

- Do not edit, fill, rename, move, or delete a file in this tree, including
  this instruction file and `.tadp-lock.json`.
- To instantiate a template, copy it to the destination declared by the
  workflow outside `template/`, then edit only that copy.
- A request to use a template, create an initiative, implement a product,
  repair validation, or complete a workflow does not authorize a reusable
  template change.
- Change this tree only when a human explicitly requests the exact reusable
  source change. Apply the TADp reusable-workflow compatibility review, update
  every affected consumer, and refresh the lock only after the change is
  complete and reviewed.
- Never run the lock refresh command or protected-update commit override merely
  to silence an integrity finding.

If ordinary work appears to require a change here, stop that affected work and
ask whether the human intends to revise the reusable TADp source or instead
wants an instantiated copy changed.
