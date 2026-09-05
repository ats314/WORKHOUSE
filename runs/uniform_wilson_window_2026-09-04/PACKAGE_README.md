# WORKHOUSE: uniform Wilson kinetic window and finite-order shell matching

Research continuation, 4 September 2026. Read-only upstream reference:
`ats314/WORKHOUSE@31255abac3829cb0cc1ce7c36c1852db8cdafbea`.

## What this package establishes

`UNIFORM_WILSON_WINDOW.md` contains the derivations and their scope:

1. All-irrep no-pollution estimate for the calibrated Wilson kinetic energy,
   and the exact physical trivial-flux window `[0, 5 C_F/2)` containing only
   the vacuum and the fundamental plaquette shell, uniformly in spatial volume.
2. A common SU(3) kinematic contour and volume-uniform **free** norm-resolvent
   convergence. The temporal-step threshold is existential, not numerically certified.
3. The actual symmetric Wilson transfer generator's reduced second-order weight
   `d_tau(Delta) = (tau/2) coth(tau Delta/2)`, its complete charge-odd shell
   coefficient, and the first literal-Wilson source Gram correction.
4. Spatially weighted `O(epsilon^2)` matching at **each fixed magnetic Taylor
   order**. This is not a bound on the summed series.

For SU(3), the auxiliary Hamiltonians `K_epsilon - u V` admit a stronger continuation
conditional on the existing G18 construction. They are distinguished explicitly
from the actual symmetric transfer logarithm. The remaining actual-Wilson
nonperturbative task is the uniform marked-cluster majorant and spectral/source
identification in Section 10. No gap or claim in the remote repository was changed.

## Read and reproduce

- `UNIFORM_WILSON_WINDOW.md`: full proof note.
- `WILSON_KINETIC_WINDOW_INSERT.tex`: a standalone manuscript insert, with proof
  of the kinetic window and exact finite-step second-order formulas.
- `exact_su3_laplace.py`: exact rational SU(3) Cartan/Weyl Gaussian-moment calculation.
- `verify_kinetic_window_and_shell.py`: 23 exact and numerical checks, including
  the two negative controls.
- `wilson_clock.py`: copied **unchanged** from the preceding temporal-matching
  bundle; implements the numerical Weyl quadrature and character-space model.
- `window_shell_certificate.json`, `exact_laplace_certificate.json`, `checks.log`:
  recorded results of this execution, not an all-representation numerical proof.
- `graph_integration_proposal.json`: proposed claim/premise connections, not a
  native graph mutation or an instruction to close G18/G19.

Use Python 3.11 or later and install the four dependencies in `requirements.txt`.
Then run from this directory:

```bash
python exact_su3_laplace.py
OPENBLAS_NUM_THREADS=1 python verify_kinetic_window_and_shell.py \
  --grid 384 --refined-grid 768 --cutoff 20 \
  --output replay_window_shell_certificate.json
```

The verification command passed 23 checks in this session. It scans the 231 SU(3)
irreps with `p+q <= 20` at five temporal steps, on two quadrature grids. Finite
scans do not prove the high-irrep bound: its proof is the density/Dirichlet-form
argument. The numerical grid comparison is not an interval enclosure, and no
numerical value of the all-irrep temporal threshold is certified.

No full WORKHOUSE test suite, CI workflow, or Lean build was executed for these
additions. Pure symbolic arithmetic checks do not formalize the operator proofs.
The source references and byte hashes are in `source_manifest.json`; package
files are pinned by `SHA256SUMS`.
