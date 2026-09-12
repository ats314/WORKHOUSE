# The M10 tube moments are not uniform in theta, with exact rates — 2026-09-12

Replay: `scripts/check_m10_antipodal_moment_scaling.py` (exit 0, all checks exact).

This note addresses the third item of the outstanding list in
`graph-tasks/2026-09-11-m10-independent-review.md`: uniform treatment of the
antipodal angular transition. It establishes a quantitative obstruction with
closed-form constants. It does not close M10, and it supplies neither of the
other two outstanding inputs.

## The spectrum

On a regular fixed-Q four-face SU(2) fiber the conditional Hessian spectrum is
the A5/A6 table of `docs/derivations/w6-antipodal-magnetic-geometry.md`, with
`C = cos(theta/4)`:

| Eigenvalue | Multiplicity |
| --- | ---: |
| `8C` | 3 |
| `(8-4sqrt2)C` | 1 |
| `(8+4sqrt2)C` | 1 |
| `8C-4sqrt2` | 2 |
| `8C+4sqrt2` | 2 |

The independent finite-difference computation in
`graph-tasks/evidence/2026-09-11-discovery-agents/cases/m10-brascamp-lieb/fiber_hessian_theta.json`
reproduces this table at every sampled theta, up to that script's overall factor
of four. The double soft branch `8C-4sqrt2` is positive for `theta < pi` and
vanishes exactly at `pi`; by (A6), with `delta = pi - theta`,

    8 cos((pi-delta)/4) - 4 sqrt2 = sqrt2 delta - (sqrt2/8) delta^2 + O(delta^3).

## Divergence of the tube moments

Under the eikonal relation `Omega_S = sqrt(Omega_V)` the Born covariance is
`Sigma_Y = (1/2) Omega_S^-1`, and the centered Gaussian norm moments are
`c2 = s1`, `c4 = s1^2 + 2 s2`, `c6 = s1^3 + 6 s1 s2 + 8 s3` for
`s_k = Tr(Sigma_Y^k)`. The soft branch enters `Sigma_Y` as `delta^(-1/2)`, so
every moment diverges at the antipodal transition. The leading constants are
exact (SymPy `limit`, verified in the replay script):

    c2 ~ 2^(-1/4)    delta^(-1/2)
    c4 ~ 2^(1/2)     delta^(-1)
    c6 ~ 6*2^(-3/4)  delta^(-3/2)

and the interior gradient prefactor of any Bernstein-type bound carries

    4 / lambda_min^S ~ 4*2^(-1/4) delta^(-1/2).

**Consequence.** No fixed-radius conditional tube admits a theta-uniform moment
bound on this family. A uniform statement must do one of: shrink the tube radius
with `delta`; split the two soft directions off and treat them by the gauge
degeneration at `Q = -I` rather than by a Hessian floor; or carry a
`delta`-dependent reference measure through the comparison. This is the
quantitative form of the obstruction that P1 #3 of the independent review
identified qualitatively, and it is consistent with P1 #2's observation that a
fixed-radius complement can approach a different point of the minimizing sphere
as `Q` approaches `-I`.

## A discrimination test for submitted moment values

The constant `4(sqrt2-1)` of (A5) is a *lower bound* on the seven non-soft
eigenvalues, not an eigenvalue of multiplicity seven. In the actual spectrum it
occurs only at `theta = pi`, as the `(8-4sqrt2)C` singlet, with multiplicity one;
it is absent from the spectrum at `theta = 0`. The replay script checks all three
statements exactly.

Because `c4/c2^2` is scale-invariant it discriminates independently of any
normalization of the chart metric. Over `theta` in `[0, pi]` its minimum is

    min c4/c2^2 = 1.2553363, attained at theta = 0.

A moment triple whose ratio falls below this value belongs to no fiber of the
family. This is a cheap guard worth applying to any future submitted tube
moments before they are propagated.

Applied to the values circulated on 2026-09-12 as "corrected physical ground
state tube moments" — `c2 = 3.372386`, `c4 = 13.912200`, `c6 = 67.883585` —
the ratio is `1.2232670`, strictly below the minimum. Those values were obtained
by assigning the (A5) bound multiplicity seven and pairing it with the soft
branch evaluated at `theta = 0`; they mix two different fibers and correspond to
none. For reference, the actual values at `theta = 0` are `c2 = 1.916149`,
`c4 = 4.609128`, `c6 = 13.452999`.

## What this does not establish

- No parameter-differentiated ground-state estimate. P1 #1 of the review stands,
  including its counterexample `A(g,eta) = 1 + eta g^4 sin(g^-6)`, whose
  corresponding gradient is `5 g^3 sin(g^-6) - 6 g^-3 cos(g^-6)` and is not
  `O(1/g)`.
- No conditionally normalized complement bound. The rare-fiber normalization
  `h_g(Q)` still requires a uniform lower bound.
- No relation between the chart-metric Hessian used here and the Agmon phase
  Hessian. A5-A7 separate these objects and this note does not join them.
- No M10 closure, and no Lean formalization of any statement above.

The generic target `DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10`
remains open.
