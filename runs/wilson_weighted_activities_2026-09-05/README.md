# Weighted activities for the actual Wilson transfer

This additive run records two analytic proof notes and exact finite controls.
The new creator-velocity chart has a real-linear inverse, a holomorphic
doubled extension, and connected assigned-support coefficients. An ordered
contour expansion retains the actual Perron scalar normalization and proves

```text
sup_i sum_(X contains i) 2^|X| ||F_X|| <= 1/2500,
|u| <= u_star/1252800000.
```

The full-operator perturbation is at most 1/998. Together with the calibrated
physical free window, this gives the complete finite-volume odd shell on one
common volume- and mesh-independent interval. The interval is conservative.
Weighted local-source transport is proved separately in the chart note.
The thermodynamic Riesz range and uniformly invertible/total projected
literal-source frame remain open. This uses a new unitary chart; its excited
action is not identified with the earlier common-filter chart.

## Executed controls and evidence boundary

- Six native exact checks. Independent support convolution and rank-one
  tensor matrices agree on 22 tangent columns, including entangled overlaps.
- Real-linear inverses, a four-link component-factorization control, and
  the nonzero complex vacuum phase 1/198 are exact.
- Finite rooted coefficient-l1 contraction bounds 1321/112500 and 123/5000
  bound genuinely nonzero four-term Neumann remainders.
- Noncommuting ordered-contour coefficients agree with partition extraction:
  six quadratic and 24 cubic connected words, with commutator square 3/4.
- Kirchhoff spanning-tree counts on 363 labeled graphs match 20 formal
  marked-tree coefficients at four roots through degree five. Omitting a
  root multiplicity gives 1/98 instead of the required 1/49.
- A separate implementation checks 28 root/order bounds through degree seven
  and independently recomputes the primitive constant margin exactly.
- Rational checks verify the 1/6 creator, 1/2500 activity and 1/998 operator
  constants under their stated transcendental and analytic premises.

These finite computations certify their own algebra and arithmetic. They do
not machine-certify the general Banach-space, full Hilbert-space or spectral
theorems. Those have explicit analytic proofs in the two frozen notes.
No new Lean theorem is claimed. Earlier sealed evidence remains unchanged.

## Reproduce

```text
python scripts/verify_wilson_creator_velocity.py --output outputs/fresh-velocity.json
python -m pytest tests/test_wilson_creator_velocity.py tests/test_wilson_contour_trees.py
python -B runs/wilson_weighted_activities_2026-09-05/replay_frozen.py
python -B runs/wilson_weighted_activities_2026-09-05/independent/check_contour_tree_majorant.py
```

The canonical runner refuses an existing output and disabled assertions.
`replay_frozen.py` imports the frozen modules by path, verifies all recorded
source hashes, and compares recomputed exact payloads to the certificate.
`source/` retains the executed code and proof notes. `independent/` retains
the independent derivations and full-chain audit, including audited proof
hashes. `SHA256SUMS` pins every file in this run.
