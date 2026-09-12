# Earlier-proof integration verification receipts

The final source base includes main through PR #158 plus the recovered proofs.
`validation-final.json` records completed checks and their actual scope.
`end-v2.json` is the saved graph snapshot with matched generation provenance;
it executes no checks. `verify-final.json` is the uncached 663/663 check run.
The original full regression passed 2,043 tests before the final main integration;
final focused graph and view tests cover the combined source/registry changes.

`end-v1.json` and `base103838-*` retain the earlier verified integration state.
Initial failed fixtures and interrupted generation receipts are retained as
history, not reported as passing executions. The B6 numerical campaign remains
historical; no new whole-statement Lean formalization is claimed.

`incoming-main-preservation.json` and the merge receipts record preserved inputs.
`current-source-coverage.json` distinguishes the complete 6,882-source mapping
from substantive review (233 reviewed, 6,649 pending). Three non-semantic YAML
separator findings from the optional whitespace scan remain visible in its log.
Every file in this directory is hashed below in `SHA256SUMS`.
