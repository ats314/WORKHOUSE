# WORKHOUSE: blocked Wilson vacuum and source-window continuation

Research date: 4 September 2026. Read repository snapshot:
`8e44da1fbd4b8643a12d514a1fb83ac636edf094`.

## Main result

Blocking a fixed physical duration, rather than a fixed count of fine time
steps, gives a scalar polymer construction for the **actual** retuned Wilson
transfer. Under the preceding uniform kinetic estimates, the new note proves a
common small magnetic-coupling domain for its vacuum and full local
multiplication-source correlations, their weighted continuous-time matching,
and a positive three-orientation source Gram in a fixed Borel plaquette-energy
window. The abstract scalar cluster theorem is an explicit external input.

This is not a claim that the Wilson excited window is already a complete
isolated three-component band. Riesz isolation, totality, and exponentially
weighted matching of the band-projected h, G, S kernels remain separate.

## Contents

- `DISCRETE_TIME_VACUUM_AND_WINDOW.md`: complete derivation, assumptions,
  constants, spectral-measure consequences, and remaining question.
- `WILSON_BLOCKED_VACUUM_INSERT.tex`: manuscript insert; not automatically
  included in any existing paper and not compiled into a paper here.
- `verify_discrete_time_bridge.py`: 26 finite diagnostics, including exact
  combinatorics, a finite-state bridge construction, and negative controls.
- `wilson_clock.py`: unchanged numerical primitive from the earlier temporal
  matching delivery. Its shared origin is recorded in `source_manifest.json`.
- `discrete_time_certificate.json` and `checks.log`: executed results.
- `graph_proposal.json`: staged dependency nodes; not a native-ledger update.
- `source_manifest.json`, `environment.json`, `SHA256SUMS`: provenance.
- `requirements.txt`: numerical dependencies.
- `prior/UNIFORM_WILSON_WINDOW.md`: immutable copy of the preceding input note,
  not silently revised or promoted by this continuation.

## Reproduce

Python 3.11 or later is sufficient for the script. In an environment with the
listed dependencies installed:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python verify_discrete_time_bridge.py \
  --grid 192 --refined-grid 384 \
  --output rerun_certificate.json
```

The script raises an exception at the first failed diagnostic. The default
Weyl grids and all finite test spaces are declared in its output. The original
certificate is not overwritten by the command above.

## Interpretation of the tests

All 26 checks passed in this session. They do not constitute a formal proof of
the infinite-volume cluster expansion. The SU(3) test uses **one closed
plaquette in the 21-character space p+q <= 5**, not the infinite cubic lattice.
The finite clock models are explicitly not SU(3). Temporal refinement is tested
against the Hamiltonian on the same finite retained space. Grid refinement is
not rigorous interval quadrature.

The empirical block duration near one and magnetic couplings in the numerical
tests do not evaluate the very conservative infinite-lattice convergence
threshold. That threshold depends on heat/mixing constants not evaluated here.
No summed O(epsilon^2) rate, spatial continuum limit, full WORKHOUSE CI, or Lean
formalization is reported.

## Repository handling

No remote files, native ledger statuses, immutable corpus files, or generated
views were changed. Integration should retain the proof dependencies and the
unresolved excited-band node in `graph_proposal.json`; the finite checks must
not automatically promote the operator theorems to proof-checked status.
