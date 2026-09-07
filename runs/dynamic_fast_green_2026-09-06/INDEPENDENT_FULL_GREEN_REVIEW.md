# Independent review of the full Gaussian fast Green calculation

6 September 2026. Review scope: the sibling `FULL_GAUSSIAN_FAST_GREEN.md`,
its `check_full_fast_green.py`, and the saved `FULL_FAST_GREEN_CONTROLS.json`.
The review does not edit those files. It does not adjudicate the separate
actual-plaquette harmonic witness or assert any interacting remainder bound.

## Verdict

No substantive mathematical defect was found in the reviewed inverse
identity, Fock source normalization, Lie-cubic prefactor, exterior-sector
restriction, or distinction from the fiber inverse. The statements hold
under their explicit finite-dimensional assumptions: Omega > 0, injective
W, color-diagonal covariance, and the stated common compact-group
equivariance. The actual path application retains rho > 0 for its joint
Gaussian. The uniform full-Fock lower floor is an established analytic
input, not a conclusion of the finite exterior examples.

The root controls replayed successfully with `--verify` in ordinary Python
and under `-O`. Their explicit `require` checks remain active under
optimization. A new independent exact calculation, in the larger physical
colored-polynomial sector rather than only exterior coordinates, also
passed and replayed under `-O`.

## 1. The nonreducing-Q inverse is the stated shorting

For S of full column rank and Q projecting onto ker S*, the constrained
Euler-Lagrange equations are D x + S lambda = b and S*x = 0. They uniquely
give

```
R = D^-1 - D^-1 S(S*D^-1 S)^-1 S*D^-1.
```

This R is self-adjoint, kills S, and obeys Q D R = Q. It is exactly the
extended inverse of Q D Q on Q. No commutation of Q with D is required.
It is generally different from Q D^-1 Q.

With S = L_n U_n, multiplication by L_n on both sides yields

```
L_n R L_n
 = A_n - A_n U_n(U_n* A_n U_n)^-1 U_n* A_n,
A_n = L_n D_n^-1 L_n.
```

The commuting tensor functions of Omega justify the displayed diagonal
prior 1/[product omega_i times sum omega_i]. The source Gram is strictly
positive on its stated domain. Upon a symmetry restriction, source
coordinates must be restricted to their actual supported range, with the
zero-source subtraction interpreted as zero as the note already states.

## 2. Source weighting and probability normalization

The Gaussian covariance is (1/2) Omega^-1. A coordinate linear form with
cotangent w maps into first Fock chaos with the spatial factor
Omega^(-1/2)w and the probability normalization 1/sqrt(2). Thus the
literal source range is ran(Omega^(-1/2)W). Its orthonormal isometry is

```
j = Omega^(-1/2) W (W*Omega^-1 W)^(-1/2).
```

The probability factor cancels from that range and its projection, but
does not cancel from cubic energy. This agrees with the established
endpoint note read during the review.

The independent control explicitly checks the coordinate-to-Fock
projection conjugacy. For covariance G_c = (1/2) Omega^-1, the orthogonal
projection on coordinate coefficients with their Gaussian norm is

```
P_coord = W(W*G_c W)^-1 W*G_c.
```

Conjugation by Omega^(-1/2) gives j j*. The control also rejects the
Euclidean source projection onto ran W as a substitute for j j*.

## 3. Ordered spatial tensors, color, and the bosonic sector

Let I_f embed an alternating spatial tensor D into the combined tensor
with entries D_ijk f_abc. Simultaneously permuting its three spatial/color
legs gives two alternating signs, so I_f D is a symmetric bosonic tensor.
Its squared tensor norm is

```
||I_f D||^2 = (sum_abc f_abc^2) ||D||^2
            = C_A d_G ||D||^2.
```

The third Gaussian chaos inner product supplies 3!, while three coordinate
probability-covariance factors supply 1/2^3. All spatial frequency and
source maps act as color identity and commute with this embedding. Its
Lie-color image is a reducing subspace for both D_3 and P_3, and hence for
the compressed inverse. Therefore the exact coefficient is

```
3! C_A d_G / 2^3
```

when the spatial inner product sums over all ordered triples, as in the
note. For an alternating tensor whose six entries over a fixed unordered
triple have magnitude d_alpha, its orthonormal wedge coordinate has
magnitude sqrt(6) d_alpha. Forgetting this conversion would lose another
factor of six.

The reviewed exterior controls are valid controls of this physical
Lie-cubic symmetry type. They are not controls of every bosonic symmetry
type or every invariant tensor; the note's general constrained-inverse
proof supplies the broader algebraic statement. No claim that an
antisymmetric spatial tensor alone is a physical bosonic state is needed.

## 4. Independent calculation in the larger colored polynomial space

The new `check_full_green_review.py` imports no function or saved value
from the reviewed script. It uses

```
Omega = diag(1,4,9,16),
W = [[1,0,0], [0,1,0], [0,0,1], [1,0,0]],
f_abc = epsilon_abc   (SU(2), C_A=2, d_G=3),
D_(123), D_(124), D_(134), D_(234) = 1,-2,3,-4.
```

This W is nonreducing and differs from the reviewed script's example.
The calculation explicitly expands every ordered D_ijk epsilon_abc term
into the 64 commutative monomials x_i^1 x_j^2 x_k^3. This is already a
bosonic coordinate representation. Because the covariance is color
diagonal and each color occurs once, its Gaussian Gram is precisely the
third tensor power of (1/2) Omega^-1, with no hidden internal Wick terms.
Other third-chaos color occupations are orthogonal and are preserved by
the frequency and observation operators, so this polynomial sector is
sufficient for the stated forcing.

All 27 retained monomials are included. The code finds all 37 independent
conditionally centered directions, constructs the full Gaussian
Dirichlet form on that complement, and directly solves its variational
equation. No exterior reduction is used in this solve. The result is

```
actual full compressed polynomial energy = 128397/695968,
ordered spatial energy from proposed T_3 = 42799/1043952,
orthonormal wedge energy                 = 42799/6263712.
```

These agree exactly through

```
128397/695968
 = (9/2) (42799/1043952)
 = 27 (42799/6263712).
```

Here 9/2 = 3! C_A d_G/8. The full 64-component solution is verified to
remain in the alternating spatial Lie-color sector, independently
checking that its exterior description discards no coupled component.
Replacing the energy prior by equal-time conditioning gives the distinct
wrong value 609/136, which is explicitly rejected.

The result is saved in `FULL_GREEN_INDEPENDENT_POLYNOMIAL_CONTROLS.json`,
including its review-script SHA256. The direct derivation and optimized
payload replay both passed.

## 5. Fast-sector and fiber boundaries

The at-least-one-fast complement of a tensor source is larger than the
tensor of one-leg fast complements. The reviewed diagonal wedge example
correctly preserves three nonzero sectors after the all-fast exterior
cube has become zero. This is a structural failure of separate-leg
conditioning, not a scalar normalization ambiguity.

The conditional-fiber OU inverse and the actual full compression remain
distinct. Vertical Dirichlet-form domination gives F0^-1 <= D_vert^-1.
It transfers a bounded-mean, local-coefficient synthesis estimate as a
quadratic-form inequality. It transfers neither the exact entries nor an
absolute rooted row bound. Both notes retain this boundary correctly.

The denominator with two retained frequencies rho and a fast frequency
omega_h has the stated rho^-2 asymptotic when its coefficient is nonzero.
Establishing that coefficient for the actual local Wilson vertex belongs
to the separate witness, which this review did not recompute. The current
proof correctly does not infer a uniform nonlinear conclusion from the
finite identity or from the fast spectral floor alone.

## 6. Reviewed file pins and replay commands

SHA256 pins of the files reviewed:

```
FULL_GAUSSIAN_FAST_GREEN.md
b8691f1bc4425f0ae2281b46200c8f1dba086107de508900996b9c6ae8e63ae2
check_full_fast_green.py
ed9137a3876c31e16d64ca05e76df6e132f9881707105d169336fc61bb4ec0e8
FULL_FAST_GREEN_CONTROLS.json
522d7d9b32f386f981b5637aae659763204fe217f909a88c43bfeac5240ae25f
```

Run from the repository root. The base directory below is
`outputs/wilson_complete_band_20260905/next_scale/next_nonlinear/next_connected_cubic_fast_energy`:

```powershell
$reviewBase = 'outputs/wilson_complete_band_20260905/next_scale/next_nonlinear/next_connected_cubic_fast_energy'
.\.venv\Scripts\python.exe -B "$reviewBase/check_full_fast_green.py" --verify "$reviewBase/FULL_FAST_GREEN_CONTROLS.json"
.\.venv\Scripts\python.exe -O -B "$reviewBase/check_full_fast_green.py" --verify "$reviewBase/FULL_FAST_GREEN_CONTROLS.json"
.\.venv\Scripts\python.exe -O -B "$reviewBase/dynamic_fiber/check_full_green_review.py" --verify "$reviewBase/dynamic_fiber/FULL_GREEN_INDEPENDENT_POLYNOMIAL_CONTROLS.json"
```
