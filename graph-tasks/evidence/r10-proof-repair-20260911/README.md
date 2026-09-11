# R10 repair verification receipts

These receipts distinguish successive integration states. The mathematical source
was reviewed and repaired; finite checks do not certify the unresolved uniform
source-energy bounds.

- `verify.log`: uncached invariant verification on the integration with main
  60728319516c6af49c700b7791f52ecf772f4bc3, 624/624 passed.
- `pytest.log`: full suite on that integration, 1987 passed, 4 skipped,
  11 subtests passed, and one failure because the new preservation directory
  lacked a `runs/index.yaml` entry. That entry was added and its test passed.
- `end.json`: saved snapshot before the run-registration correction; retain
  its original fingerprint. It is historical, not the final integrated state.
- `lint.log` and `docs.log`: original integrated lint and documentation checks.
- Files ending `-final.log` and `pytest-integration.log`: validation after
  integrating PR 149 at ffff7bb2e67b976ba50fe5cf7184966dd581535f.

The task record identifies the final saved snapshot and later regression results.
No Lean source was changed. No fresh local Lean compilation is claimed.
