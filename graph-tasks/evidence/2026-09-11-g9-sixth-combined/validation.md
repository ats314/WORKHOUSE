# Final local validation

Canonical source base fa1bbadddd52955cb6517a0d7af5b59c086c40df. Publication branch
codex/g9-sixth-combined-20260911. Commands ran in REPO's independent environment.

- Fresh `workhouse verify`: **585/585 passed**, exit 0. See verify.txt.
- Focused sixth-order tests: **15 passed**.
- Full native Windows pytest: **1904 passed, 4 skipped, 11 subtests passed**,
  with two run packaging failures (missing registration and manifest). The exact
  original output is retained in full-pytest-before-run-repair.txt.
- Added runs/index.yaml registration and SHA256SUMS pinning all seven run inputs.
  The nine affected run/registration tests then passed.
- After final index/frontier/certified regeneration, **30 targeted tests passed**
  in 350.34 seconds: test_frontier.py, test_certified.py,
  test_search.py::test_catalogue_files_are_current,
  test_graph.py::test_run_register_matches_runs_directory and test_runs.py.
  See final-targeted-tests.txt. This is not described as a second fresh full run.
- Ruff check and format pass for tracked publication Python files plus new code
  (292 formatted files). Separate preexisting untracked tetrahedral files fail
  ambient full-tree lint and remain untouched and excluded from publication.
- Documentation validation: 38 maintained files, 558 local links, zero errors
  and warnings. Whitespace validation passes for active implementation and metadata;
  byte-preserved reports and original sources retain their received whitespace
  and CRLF. Staged Git blobs match every run and physical-probe manifest hash.
  Result ledger validation returned [].
- Final index: 17,395 claims, 28 symbols, 29,360 graph records.

Fresh execution and cache reuse are distinct. The fresh verifier above executed
all 585 checks. Final generated views reused 1,170 check results through the
public content-manifest cache context; the observation is retained in
view-cache-observation.json. The final targeted tests retain their own cache
observation. Both contexts assert that input bytes did not change.

The authoritative final saved target snapshot is end-after-run-registration.json:
freshness matched, 585 recorded verdicts, zero checks executed by that saved read,
fingerprint e138ca6f5e4367784900d507c7eb4c8798d507ea5db4e73258b66614f9277461.
Earlier snapshots are preserved and superseded for final freshness purposes.

Four larger physical probes and their exact failure/support evidence are retained
under physical-probes/. None is a completed direct H6 calculation. Formal folds,
all H4 mixing pairs, conditional noncancellation and the one-face dynamics are
established at their documented scopes. Direct connected multi-face q e2/e3
coefficients and a direct local RUR amplitude remain open.

Remote PR/CI/merge status is pending at this local checkpoint; confirmed closeout
is recorded in C:/WORKHOUSE/navigation/tasks/2026-09-11-g9-sixth-combined.md and
reported separately. No pending run or unpublished result is claimed merged.
