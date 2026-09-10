# September 1-9 theory graph and Lean integration

This run integrates source work from September 1 through September 9, 2026.
It prioritizes `docs/derivations`, `docs/research`, and `docs/validation`, then
connects the standalone campaigns and missing worktree packages to the main
verifier. Scientific dates come from documents, dated packages and Git history;
filesystem creation times alone are not used as authorship or proof dates.

Validated outcome: 4,402 catalogue records, 8,890 graph relationships, 180
registered Lean declarations, and 496/496 passing native checks. All 167
targeted regression tests passed across the main run and the focused rerun.
The strict Lean build passed; the 46 integrated declarations use standard
axioms only. See `validation.json` and the retained test reports for details.

## Delivered integration

- `docs_coverage.json` records 77 priority source files and their native citation
  IDs; 53 lacked a direct document node before this pass.
- `branch_run_imports.json` records 18 September run packages copied unchanged
  from parallel worktrees, with 686 per-file SHA-256 comparisons and original
  run registrations. These are preserved past runs, not newly replayed runs.
- `ledger/recent_research.yaml` holds named results and open routes from all
  nine standalone campaigns: 26 results and four routes, linked to 67 source
  artifacts. Sources in `sources/` retain their original bytes,
  absolute provenance paths and exact proof locators. The loader uses portable
  checkout-local paths and checks hashes before producing graph records.
- Eight modules join the active Lean build: 24 existing branch declarations
  plus 22 campaign declarations. `lean_integration_report.json` records the
  successful `lake build --wfail` and standard-axiom audit of all 46 additions.
- Native checks rederive the complete anisotropy Laurent identity, its induced
  sixth-order coefficient, and finite-order spectral controls. Two Feshbach
  suites integrate the September 8-9 word and resolvent calculations.

## What the new checks establish

The anisotropy residual identity agrees in all 85 nonzero Laurent coefficients
with the assembled fourth-order record kernel. Its virtual-mixing coefficient
is exactly `-169924002729806205028788409/619343593697933825385600000`.
The direct sixth-order operator contribution remains separately identified.

The Hodge-channel integration retains `B=D=0` for the actual fourth-order
support `{I,U,S,S^2,R}`. It also records the exact counterexample
`sigma(UR)=-2 q e_2` to the stronger R-degree-only selection rule. Normalized
projector claims require `q>0`. The resolvent suite retains two exact controls
and labels all three floating spectral controls T2. Details and unchanged
originals are linked from `docs/research/september_feshbach_integration.md`.

Lean proves the square-force coefficient bound for every real radial index
`n>=1` and finite nonnegative spectral synthesis. It proves the local four-edge
quadratic decomposition and bounds, not an unassumed identification with the
complete interacting Wilson lattice. The graph records the exact downstream
hypotheses alongside these established inputs.

## Reproduction

From a configured repository environment:

```powershell
uv run --no-sync workhouse verify --only anisotropy
uv run --no-sync python -B runs/recent_research_integration_2026-09-09/verify_new_checks.py
uv run --no-sync workhouse why RESULT:RECENT_ANISOTROPY_VARIANCE_CORE
uv run --no-sync workhouse why RESULT:W6_SQUARE_SHARP_INVERSE_ENERGY
uv run --no-sync workhouse index -w
uv run --no-sync workhouse frontier --write
uv run --no-sync workhouse certified --write
```

From `lean/`, run `lake build --wfail`. `LeanAxiomAudit.lean` and
`lean_axiom_audit.log` preserve the focused axiom audit. On this Windows host,
the existing environment required `PYTHONPATH=src` when invoked directly and
permission to load its installed mathematical DLLs. Dependency versions were
not changed for this integration.

The Windows regression environment additionally used `PYTHONUTF8=1` and put
the installed Git Bash directory before the Windows Apps Bash launcher in
`PATH`. Two initial failures were resolved by those settings. One document
inventory assertion was extended to require the exact union of the provenance
and recent-research registers, including a check that their IDs do not overlap.
The original failed report and the successful focused rerun are both retained.

## Preservation and evidence

Original research folders and parallel worktrees are untouched. Existing main
checkout work was preserved before edits under
`C:/WORKHOUSE/navigation/preserved/2026-09-09-theory-lean-integration/`.
`Basic.lean` is unchanged by this task. Generated scientific views are rebuilt
from curated source rather than hand-edited.

The live Balaban derivation changed outside this task during the integration.
Its coverage record retains the initial digest, the observed revision and a
preserved copy; the existing submitted-claim and repair metadata remain intact.
`verify_preservation.py` checks the copied branch packages, campaign sources,
priority documents and ported Lean modules against their recorded hashes.

`validation.json` records final checks and counts. `SHA256SUMS` pins this run's
stable files; transient process state is not part of the scientific claim.
