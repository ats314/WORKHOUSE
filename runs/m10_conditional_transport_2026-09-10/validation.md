# Scoped validation checkpoint

10 September 2026, isolated branch `codex/m10-conditional-transport-20260910`.

- `python scripts/check_m10_transport.py --output runs/m10_conditional_transport_2026-09-10/exact_checks.json`: 20/20 exact controls passed.
- `python -m pytest -q tests/test_recent_research.py`: 25 cases passed, including every allowed source bundle, hash drift, traversal rejection and prefix-lookalike rejection.
- `python -m ruff check .`: passed.
- `python -m ruff format --check .`: 471 files already formatted at this checkpoint.
- `python scripts/check_docs.py`: 27 maintained files, 459 local links, zero errors or warnings at this checkpoint.
- Independent analytic review: no remaining actionable issue in the reviewed source; exact reviewed hash and theorem dependency are in `independent_review.md`.

The proof map and native graph are regenerated using the repository entry
points. Required full regressions, uncached mathematical verification and CI
are separate landing gates; their final results are recorded in the pull
request and task completion record after reconciliation with concurrent main.
The counts above are this checkpoint's observed results, not a claim about
later merged files. No local Lean source was changed or rebuilt by this task.

The analytic theorem is not promoted to T0/T1 by these finite checks. Full
uniform M10 for the synchronized transport remains open.
