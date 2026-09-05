# Exact creator-parent controls

The final files are `finite_certificate_final.json`,
`independent_replay_final.json`, their matching execution logs,
`verify_creator_parent.py`, and `replay_parent_certificate.py`. The reusable
implementation is `src/workhouse/wilson_creator_parent.py`; the 17 focused
tests live in `tests/test_wilson_creator_parent.py`. `canonical_replay.json`
records the canonical source hashes and checks that its certificates agree
exactly with the independently generated draft artifacts.

The six finite tensor models have dimensions 8, 16, 16, 8, 27, and 12.
They include overlapping pair and triple creators, disjoint components,
three-dimensional links with vector-valued creators, and mixed link
dimensions. One overlapping multibody model lies within the rooted
weight-2 ball of radius 1/8. Its exact rational bounds are
M1 <= 19/512 and g = 256663/262144 >= 247/256.

For P_i = q_i - A_i and H = sum_i P_i^T P_i, the controls establish:

- the P_i are commuting idempotents, with the exact finite similarity
  P_i = exp(S) q_i exp(-S);
- an independently enumerated disjoint-support creation exponential is
  the common vacuum, has vacuum coefficient one, and has the displayed
  exact positive normalization;
- H has a one-dimensional kernel;
- H^2 - gH and H - g(I - |psi><psi|/||psi||^2) are positive semidefinite,
  using g = 1 - K1 - M1^2 and declared coefficient-l1 upper bounds on
  the creator vector norms;
- the individual idempotent singular bounds and the intersecting-creator
  commutator estimates used in the sharper analytic proof hold in these
  tensor examples.

There are 81 rational PSD certificates. Each is an explicit equality
M = U^T diag(d) U, where U is unit upper triangular and every d is
nonnegative. Both generation and independent replay reconstruct the whole
matrix exactly. No floating eigenvalues or numerical tolerances occur.
The replay also rejects a deliberately altered diagonal factor.

Dropping the quadratic sum A_i^T A_i loses the vacuum and gives a strictly
negative exact expectation in every nonzero test family. A separate
factorized family with one-link amplitude 1/32 has rooted weight-2 norm
1/16 for every volume and auxiliary parent gap 1025/1024, while its global
creator similarity has condition number at least (1025/1024)^n. This bound
exceeds 1000 at n=8192, proved by an exact rational comparison. It rules out
obtaining a uniform global similarity bound from the rooted estimate alone.

These are exact finite controls plus the explicit tensor-product
counterfamily. The general parent-gap estimate is an analytic theorem
proved separately. These calculations do not identify the parent with the
physical Wilson Hamiltonian or establish physical excited-band completeness.

To reproduce with fresh output names:

```powershell
.venv\Scripts\python.exe -B outputs/creator_parent_20260905/verify_creator_parent.py --output outputs/creator_parent_20260905/new_certificate.json
.venv\Scripts\python.exe -B outputs/creator_parent_20260905/replay_parent_certificate.py --certificate outputs/creator_parent_20260905/new_certificate.json --source outputs/creator_parent_20260905/verify_creator_parent.py --output outputs/creator_parent_20260905/new_replay.json
.venv\Scripts\python.exe -m pytest -o addopts=--strict-markers -q tests/test_wilson_creator_parent.py
```

Earlier `v1` and `v4` execution logs record implementation failures that
were repaired: comparison of expanded versus factored symbolic expressions,
and JSON serialization of a SymPy Boolean. Neither was a failed matrix
inequality. Intermediate source snapshots preserve the successful earlier
certificates' byte provenance; the `final` files are the current artifacts.
