# Connected local vacuum chart of the actual Wilson transfer

This run records the 5 September continuation from the supplied discrete-time
and excited-window bundles. The mathematical deliverable is the analytic
connected-monomial chart at every fixed perturbative order, together with the
explicit second-coefficient bound `40432 f_star^2/5` and block-independent
vacuum generators. The exact finite models check the construction through
fourth order; they do not replace the untruncated proof or prove convergence.

Read `paper/research_notes/G18_WILSON_CHART_RESEARCH_REPORT_20260905.md` first.
The second-order proof, recursion proof and endpoint-gauge note specify the
assumptions and remaining nonlinear estimate. `source_manifest.json` binds
the actual source and proof files used. `source/` preserves the executed code
and formal algebra as a frozen snapshot. `SHA256SUMS` pins every run file.

## Evidence

- `chart_certificate.json`: live exact second-/third-/fourth-order tensor
  calculations and a separate direct-exponential numerical diagnostic.
- `replay/`: both supplied verifiers replayed unmodified with their original
  grid sizes; all 26 and 33 diagnostics passed. The comparison records
  floating-point drift separately from exact/non-numerical fields.
- `lean/`: strict compiler transcript and reproduction command for the new
  rank-two matrix kernel and transfer denominator identity. Only these
  algebraic statements, not the analytic induction, are Lean theorems.

The certificate's `passed` field concerns its executed checks. The analytic
theorems have written proofs under the calibrated kinetic-gap hypotheses.
No common finite-coupling radius for the nonlinear chart, thermodynamic
actual-Wilson Riesz band, or sharp weighted source projection is asserted.

## Reproduce

Use a clean checkout of this run's source revision. Core exact computations
require the normal project dependencies. The standalone numerical diagnostic
additionally used NumPy 2.5.2 and SciPy 1.18.1; SymPy was 1.14.0 and Python
3.12.14. Future Python/runtime versions may change the numerical tail values.

```text
python -m pip install -e ".[dev]"
python -m pip install numpy==2.5.2 scipy==1.18.1
python scripts/verify_wilson_vacuum_chart.py --output outputs/chart-replay.json
python -m pytest tests/test_wilson_vacuum_chart.py tests/test_wilson_chart_recursion.py tests/test_wilson_chart_independent_oracle.py tests/test_wilson_bundle_provenance.py
python -m workhouse.cli verify
make lean
```

Use a new output path; the verifier refuses to overwrite an existing result.
The source imports' README files give the exact original-bundle commands.
The preserved replay comparison retains the original `outputs/` paths; the
files copied here are byte-identical to those outputs.

The research checkout began at `aea97f279e662575cada93b67547c8d01a244538`,
which already contained the uniform kinetic window. The two new user bundles
were brought in from local import commit `7411dce1139c9af39fe3348d114d0c0f1d206743`.
GitHub main was `5bdad789a796a4bc8ece58003c501be9b133716c` initially and advanced
to `f36db9e1a447ff23ed72faf43783f886958a43ef` with that uniform-window package
during the continuation. Their ZIP and every relocated member digest are in
the two imported runs' `import_manifest.json` files.
