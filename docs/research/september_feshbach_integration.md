# September Feshbach source integration

Date: 2026-09-09. This note records the reviewed integration of the September
8 Hodge-channel calculation and September 9 resolvent comparison from
`WORKHOUSE-flat-holonomy-20260907`. The original authors' source and results
remain identifiable; the scope corrections below are the integration review.

The [source manifest](../../runs/recent_research_integration_2026-09-09/sources/branch-feshbach/manifest.json)
pins the original two Python modules, two derivation notes and ADR 0045 by
SHA-256, exact source path and observed Git state. These copies are unchanged.
The working modules are [hodge_feshbach.py](../../src/workhouse/invariants/hodge_feshbach.py)
and [feshbach_resolvent.py](../../src/workhouse/invariants/feshbach_resolvent.py).

## Hodge channel: preserved identities and corrected scope

Write `q = sum_j 4 sin^2(k_j/2)` and let `psi` be the cubic cube-boundary
carrier. Exact Laurent identities give

```text
L_down + L_up = q I,   L_down L_up = 0,
L_up = psi psi^dagger,   psi^dagger psi = q.
```

For `q > 0`, the carrier line and its orthogonal complement are the two
Hodge summands. Both Hodge generators act scalarly on the carrier; the
non-Hodge insertion `R` gives an up-harmonic off-carrier excitation. At Gamma,
`q = 0` and `psi = 0`. The cleared identities still hold, but no normalized
carrier projector or complementary one-dimensional carrier follows there.
The active splitting check verifies the outer product and norm identities
explicitly and states this restriction.

The source's exact word formula is retained for every word of length at most
three with at most one `R`:

```text
sigma(W) = (-4)^#S (-2)^#R q^(#U + 1 - #R) e_2^#R.
```

Its further conclusion that R-degree one alone excludes the B tier is false.
The same formula and the exact Laurent backend give

```text
sigma(UR) = sigma(RU) = -2 q e_2,
sigma(UR)/q = -2 e_2.
```

These words have one `R`, zero Feshbach defect, and a nonzero B contribution.
The original checker compared each symbol to the single polynomial `q e_2`,
which misses its nonzero scalar multiple `-2 q e_2`. The active suite preserves
this counterexample as an explicit `FINDING:` and checks the actual
fourth-order support instead:

| Supported word | Cleared carrier symbol |
|---|---|
| `I` | `q` |
| `U` | `q^2` |
| `S` | `-4q` |
| `S^2` | `16q` |
| `R` | `-2e_2` |

That support has span `{q, q^2, e_2}` and excludes `UR`. It therefore retains
`B_shp = D_shp = 0` for the recorded fourth-order kernel. Its derivation does
not require cancellation of a B or D coefficient. The broader claim about
every R-linear kernel is not used.

The identities `sigma(RR) = q e_2 + 3e_3` and `sigma(RUR) = 4e_2^2` also
survive. The first gives the ratio `D = 3B` when `R^2` alone carries that
tier. The second lies outside the five-monomial cleared ansatz. Which words
the sixth-order dynamics actually produces remains a separate question.
The seven-word defect classification is a statement about the 39 Laurent
words of lengths one through three; it is not an all-length or pointwise
nonvanishing theorem. These results bear on G14, U2, U3 and C2 without
changing any resolved coefficient.

### Hodge-word hypotheses in other cells

The preserved source calls its proposed cross-geometry extension `U7`.
The canonical checkout now also contains GitHub's registered U7 candidate.
Its corrected record preserves the scalar Hodge-word lemma and the original
proposal, while keeping the broader cross-geometry conclusion conjectured.
The active cell check cites this review through the registered
`HODGE_FESHBACH` alias, together with U3, G5 and ADR 0008.

In the tetrahedron and pentagonal prism, exact incidence matrices give a
one-dimensional `ker L_down` spanned by `psi`, `L_down L_up = 0`, and
`L_up psi = lambda psi`, with `lambda=4` and `lambda=7`, respectively.
The tetrahedral sum is `4I`, whereas the prism sum has diagonal
`(6,6,5,5,5,5,5)` and is not scalar. Thus a scalar total Laplacian is an
unnecessary restriction: the carrier eigenvector identities suffice to
make every word in the two Hodge generators scalar on that carrier line.
This check verifies those hypotheses in the two cells. It does not calculate
their proper-return histories or discharge the general U3 proposal.

## Resolvent comparison: exact identities and numerical checks

For symmetric invertible forms on a complement, the exact identity is

```text
(A_g-A_0)[R_0 w,R_g w] = <(R_0-R_g)w,w>.
```

Positive forms additionally give the oriented variational sandwich
`g V[u_g,u_g] <= <(R_0-R_g)w,w> <= g V[u_0,u_0]`, including either sign of
`g` whenever the forms stay positive. The active check keeps that orientation
explicit rather than sorting the endpoints. These two checks are T1.

The explicit-constant check computes a relative bound by floating spectral
arithmetic. Its original module header called it T2, but its decorator
defaulted to T1. The active decorator is T2, matching the two other numerical
checks. Thus the suite has exactly two T1 and three T2 checks.

With an independently established relative form bound and
`rho = |g| kappa < 1`, the stated conditional estimate is
`|<(R_0-R_g)w,w>| <= rho/(1-rho)^2 <R_0w,w>`. Failure of this sufficient
margin condition does not imply that `A_g` loses positivity: `A_0=V=I`,
`g=2` has negative margin and positive `A_g=3I`. The active witness wording
preserves this distinction. No uniform interacting Wilson value of `kappa`
is established by these examples. Connections to G17, G22, G23 and the G19
selected inverse-pairing obligation therefore preserve those hypotheses.

## Verification

[Focused regressions](../../tests/test_september_feshbach.py) check the missed
scalar-multiple counterexample, its exact rank outside the fourth-order
span, the Gamma degeneracy, the two-T1/three-T2 split, the oriented sandwich
for both coupling signs, and the distinction between a failed sufficient
margin and actual positivity. The intake source manifest remains the
reference for byte preservation. No Lean theorem is claimed by this note.

On 2026-09-09 the two active suites were replayed with the main checkout's
locked Python environment: all 10 Hodge T1 checks and all 5 resolvent checks
(2 T1, 3 T2) passed. All six focused regressions passed; Ruff lint and format
checks passed; and all five preserved source files matched their manifest
digests. These are targeted results, not a report of the whole repository's
test suite or Lean build.
