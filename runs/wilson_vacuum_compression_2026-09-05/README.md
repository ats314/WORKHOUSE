# Exact vacuum compression and sharper coefficient bounds

The additive proof is `paper/research_notes/G18_VACUUM_COMPRESSION_BOUND_20260905.md`.
For the actual local vacuum correction, it proves `F=A+[D,S]=QAQ`.
Compression alone gives `6032 f_star^2/5`; retaining the actual Perron
subtraction and free kinetic damping sharpens this to
`(3096/5) f_star^2 + (41472/125)(J s1)^2 <= (118872/125) f_star^2`.
These are bounds on `[u^2]`, half the second derivative.

Four added Lean theorems certify the generic finite-matrix algebra. The
operator norm inequality and infinite-dimensional application are analytic
consequences under the stated Hilbert-space hypotheses. The full strict Lean
build now has 96 source theorems and zero `sorry`; exact axiom guards pass.
The symbolic complex-block and finite-transfer controls verify the scalar
normalization requirement and the exact bound arithmetic.

This run extends `wilson_vacuum_chart_2026-09-05`, whose source and numerical
replay evidence remain unchanged. At arbitrary fixed order the improved
activity bound is `l_n=k_n`; the generator bound and the unproved nonlinear
convergence step remain unchanged. No thermodynamic actual-Wilson band is
claimed from these finite checks.

Reproduce the exact checks with the ordinary project installation:

```text
python scripts/verify_wilson_vacuum_compression.py --output outputs/compression-replay.json
python -m pytest tests/test_wilson_vacuum_compression.py
make lean
```

Choose a fresh output path. `certificate.json` records source hashes and
runtime; `source/` preserves those source files verbatim. `lean/` preserves
the strict four-module compiler transcript and the local read-only-cache
driver as executed from `outputs/lean_compression_20260905`. Its recorded
absolute cache path is specific to the research machine; `make lean` is the
portable build entry point. `SHA256SUMS` pins every file in this run.
