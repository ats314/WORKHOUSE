# Convergent rooted coordinates for the actual Wilson vacuum

This run supports the analytic theorem in
`paper/research_notes/G18_ROOTED_WILSON_CONTRACTION_20260905.md` and its
infinite-lattice coefficient consequence in
`G18_WILSON_CREATOR_THERMODYNAMIC_LIMIT_20260905.md`.

The magnetic creator flow loses support weight at rate `gamma/2`; the
full reduced resolvent restores that weight. With the stated local gap,
incidence and bounded-potential hypotheses, and `mu >= gamma*tau0/2`, the
composed map contracts the ball of radius `1/16` with constant at most
`1/2` for

```text
|u| <= min(9*gamma/(309680*J_star*exp(4*mu)),
           9/(8450*tau0*J_star*exp(4*mu))).
```

This gives a common complex coupling disk for the exact finite-volume
nonunitary vacuum coordinates. Stabilized connected Taylor coefficients
give a canonical analytic infinite-lattice creator family on the same disk,
with a quantitative local rooted error bound. Physical state/GNS realization,
a controlled unitary chart or physical metric, and the complete excited
Riesz/source projection remain separate tasks.

## Evidence and scope

- `certificate.json` recomputes the explicit scalar constants and finite
  binary-support controls. It checks three overlapping four-link Pauli
  interactions, three specified trial families, exact normalization,
  exp/log inversion, creator-flow differentiation, and sampled composed-map
  contraction. It does not prove a bound on the complete ball by sampling.
- `obstruction/` contains independent two- and three-level creation-log
  controls, exact SU(3) Haar moments, and separate numerical matrix
  exponentials. The actual SU(3) counterexample concerns independently active
  disjoint plaquettes and arbitrary trial families; its scope is stated in
  `G18_SAME_WEIGHT_CREATOR_OBSTRUCTION_20260905.md`.
- `lean/` records strict compilation of all five modules, 97 theorems,
  zero `sorry`, and exact standard-axiom guards. The new theorem certifies
  the real rational Taylor inequality used in the obstruction. The
  Hilbert-space contraction proof is analytic, not formalized in Lean.
- `source/` preserves the executed sources and proof notes. `SHA256SUMS`
  pins every run file. The preceding sealed September 5 runs are unchanged.

## Reproduce

Use the ordinary project environment and fresh output paths:

```text
python -m pip install -e ".[dev]"
python scripts/verify_rooted_wilson_contraction.py --output outputs/rooted-replay.json
python scripts/verify_rooted_creator_obstruction.py --output outputs/obstruction-exact.json --skip-numerics
python -m pytest tests/test_rooted_creator.py
make lean
```

The independent numerical diagnostics additionally used NumPy 2.5.2 and
SciPy 1.18.1 with Python 3.12.14 and SymPy 1.14.0. To run them, install those
optional dependencies and replace `--skip-numerics` by `--require-numerics`.
Both verifiers refuse to overwrite an existing result. The preserved local
Lean driver uses this machine's read-only mathlib cache; `make lean` is the
portable build entry point.

The continuation started at `e6380a25a88ea4764deeb32358967ee44e3ecfe4`.
GitHub main was compared live at `f36db9e1a447ff23ed72faf43783f886958a43ef`.
The calibrated Wilson kinetic input and the original endpoint equation are
the established September 4/5 inputs; this run advances their nonlinear
creator estimate.
