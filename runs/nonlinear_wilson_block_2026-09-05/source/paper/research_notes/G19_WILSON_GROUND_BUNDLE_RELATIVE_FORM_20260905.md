# Actual Wilson ground-bundle derivative and projected coarse form

5 September 2026. Analytic derivation for the two-square bouquet
and the adjacent two-square strip, with their actual original-link kinetic
forms. All constants below may depend on fixed N>=2 and the chosen coarse
neighborhood, but not on u above a fixed threshold. No uniformity as N grows is
asserted. The earlier sealed proof and run sources remain unchanged.

Established inputs are the exact metric and compact-neighborhood full fiber gap
in [physical fiber proof](G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md), sections
3–4, and the exact horizontal decomposition in
[strip decomposition](G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md), sections 1, 3–4.
The new global complement/barrier theorem is a complementary input in
[the global vertical barrier](G19_WILSON_GLOBAL_VERTICAL_BARRIER_20260905.md); the
local derivative proof does not assume or reprove its global min-max comparison.

## 1. Statement and normalization

Use the fixed bi-invariant metric `<X,Y>=-2 ReTr(XY)` on su(N). Choose a small
closed exponential ball `U=exp X`, `|X|<=epsilon`, on which the principal root
`H=exp(X/2)` belongs to SU(N), and

```text
B(U)=Re H >= a0 I,  a0>0.
```

Such a fixed ball exists in the trace-zero Lie algebra. No square-root choice is
made across a cut locus. Set `K0=H F`; the exact product Haar measure becomes
`dU dF`, with normalized fiber Haar independent of U. Write

```text
T_U=-(1/2) sum_ab S(U)_ab D_a D_b,
V_U(F)=4u Tr[B(U)(I-Re F)],
H_U=T_U+V_U,
V_c(U)=4u[N-Tr B(U)].                                  (1)
```

Here `D_a f(F)=d/dt f(exp(t T_a)F)|_(t=0)` are fixed Haar-skew Lie derivatives.
For the bouquet `S=2I`; for the strip,

```text
R=Ad(U),  C(U)=8I-R-R*,  S(U)=15 C(U)^(-1).
```

Thus `H_U` is the **shifted balanced** vertical operator. The full constrained
fiber operator has the additional scalar `V_c(U)`. Its uncentered derivative can
be order `u |X|`; no `sqrt(u)|X|` bound for that unshifted derivative is claimed.
Subtracting this scalar changes neither the fiber eigenvector nor its gap.

Let `e(U)` be the ground energy of `H_U` and `Omega_U>0` its real normalized
ground in `L2(dF)`. There exist `u0,C,c>0` such that for `u>=u0`, uniformly in
the chosen neighborhood,

```text
e(U)<=C sqrt(u),          gap(H_U)>=c sqrt(u),
||partial_(x_i) Omega_U|| <= C |X|,
||partial_(x_i)partial_(x_j) Omega_U|| <= C,
|e(U)-e(I)| <= C sqrt(u) |X|^2.                         (2)
```

The first line is established in the uniform compact-neighborhood rotor proof;
the remaining assertions are proved below. These are derivatives of the true
quantum ground normalized in conditional Haar measure, not derivatives of the
square root of a classical conditional Wilson density.

Let `D^hor_E` be the exact metric horizontal derivative for a unit coarse
right-trivialized tangent E. Then

```text
||D^hor_E Omega_U|| <= C u^(1/4) |X|,
Phi_BH(U)=(1/2) sum_ab C_uu(U)_ab
                 <D^hor_a Omega_U,D^hor_b Omega_U>
         <= C sqrt(u) v(U),        v(U)=N-ReTr U.       (3)
```

For the bouquet `C_uu=8I`, and for the strip `C_uu=C(U)`. In particular
`Phi_BH<=C u^(-1/2) V_c` on this neighborhood. The exact compression to the
fiber-ground bundle consequently satisfies the relative quadratic-form bound

```text
q_c[psi]+(1-C/sqrt(u)) int V_c |psi|^2 dU
 <= q_full[psi Omega]-e(I)||psi||^2
 <= q_c[psi]+(1+C/sqrt(u)) int V_c |psi|^2 dU,           (4)

q_c[psi]=(1/2) int <grad_U psi,C_uu(U)grad_U psi> dU.
```

Here `q_full` uses the original-link electric form and nonnegative shifted
Wilson potential `2u[v(U1)+v(U2)]`, so its energy zero is fixed throughout.
Initially `psi` is smooth with compact support inside the chart; the estimate
extends by closure to its Dirichlet coarse form domain. The exact nonlinear
coarse metric and Haar measure are retained. With `u=g^-4`, this is a relative
`O(g^2)` correction to the actual coarse magnetic form. It is an exact compression
estimate for this finite block and neighborhood, not an approximation to a
full-block vacuum-subtracted reducing Hamiltonian.

## 2. Common operator domains and an exact graph-norm estimate

For each fixed u, `V_U` is a smooth bounded function on the compact group and
`S(U)` is uniformly positive, smooth in U and independent of F. The closed
forms have common domain `H1(G)`, and the self-adjoint operators have common
domain `H2(G)`. The latter fact can be seen directly using the positive
bi-invariant Casimir

```text
L=-Delta=-sum_a D_a^2.
```

Every `D_a` commutes with L. Consequently `T_U` commutes strongly with L on
Peter–Weyl blocks, and its quadratic form obeys `T_U>=k L` with a fixed k>0.
On each finite-dimensional Casimir block this implies `T_U^2>=k^2 L^2`, hence

```text
||L psi||<=k^(-1)||T_U psi||,
sum_ab ||D_a D_b psi||^2=||L psi||^2.                  (5)
```

The second equality follows by summing
`<D_b psi,L D_b psi>` over b and commuting L with `D_b`. Density extends the
relations from smooth functions to `H2`. In the other direction the bounded
coefficient matrix gives `||T_U psi||<=C||L psi||`. This proves the common
operator domain and gives uniform control of every second fiber derivative.
It avoids introducing an uncontrolled u-dependent elliptic constant.

For complex smooth psi, integration by parts on Haar gives the exact identity

```text
2 Re<T_U psi,V_U psi>
 =int V_U <grad psi,S(U)grad psi> dF
    +int (T_U V_U)|psi|^2 dF.                          (6)
```

`V_U>=0`. Its two Lie derivatives are bounded by `C u` uniformly on the compact
coarse set and the whole fiber, so `||T_U V_U||_infinity<=C u`. Therefore

```text
||T_U psi||^2+||V_U psi||^2
 <=||H_U psi||^2+C u||psi||^2,
||T_U psi||+||V_U psi||
 <=C[||H_U psi||+sqrt(u)||psi||].                       (7)
```

Both statements extend to `H2` by density. In particular, `H_U Omega_U=e(U)
Omega_U` and the uniform energy upper bound give

```text
||T_U Omega_U||+||V_U Omega_U||+||L Omega_U||<=C sqrt(u),
sum_a ||D_a Omega_U||^2<=C sqrt(u).                    (8)
```

The last estimate also follows directly from positivity of both terms of H.
Thus the first fiber derivative is order `u^(1/4)`, whereas the full second
fiber derivative is order `sqrt(u)`. No unproved localization moment is used
in these graph-norm bounds.

## 3. Parameter derivatives of the positive normalized ground

In the exponential coordinate x of X,

```text
B(x)=Re exp(X/2),
S_strip(x)=15[8I-exp(ad X)-exp(-ad X)]^(-1).
```

Both functions are even in x. Their first coordinate derivatives are `O(|X|)`;
their second derivatives are uniformly bounded. The bouquet S is constant.
Since `I-Re F>=0` and `B>=a0I`, for each coordinate direction,

```text
|partial_i V_U(F)|<=C |X| V_U(F),
|partial_i partial_j V_U(F)|<=C V_U(F).                 (9)
```

These pointwise inequalities use
`|Tr(DB)(I-Re F)|<=||DB|| Tr(I-Re F)`; no commutativity of the two Hermitian
matrices is assumed. The same bounds for the kinetic derivatives, in operator
norm on a vector, follow from (5). Together with (7),

```text
||H_i psi|| <= C |X|[||H_U psi||+sqrt(u)||psi||],
||H_ij psi|| <= C[||H_U psi||+sqrt(u)||psi||].            (10)
```

For each finite u, this smooth common-domain elliptic family has a simple
positive ground. The eigen-equation and normalization, or its isolated Riesz
projection, give a smooth real choice `Omega_U>0`. Put
`P=|Omega><Omega|`, `Q=I-P`, and `R_U=Q(H_U-e(U))^(-1)Q`. The full fiber gap
gives `||R_U||<=C/sqrt(u)`. With positive real normalization,

```text
<Omega,Omega_i>=0,
e_i=<Omega,H_i Omega>,
Omega_i=-R_U Q H_i Omega.                              (11)
```

Equations (8),(10),(11) imply

```text
|e_i|<=C sqrt(u)|X|,       ||Omega_i||<=C|X|.
```

The differentiated eigen-equation further gives
`||H_U Omega_i||<=C sqrt(u)|X|`. Applying (7),(5) to this vector yields

```text
||T_U Omega_i||+||V_U Omega_i||+||L Omega_i||
 <=C sqrt(u)|X|,
sum_a ||D_a Omega_i||^2<=C sqrt(u)|X|^2.                (12)
```

For second derivatives, differentiation of the first line of (11) gives
`<Omega,Omega_ij>=-<Omega_i,Omega_j>`. Differentiating the eigen-equation twice
and projecting off Omega gives

```text
Q Omega_ij = -R_U Q[H_ij Omega
              +(H_i-e_i)Omega_j+(H_j-e_j)Omega_i].      (13)
```

The first term in brackets has norm `C sqrt(u)` by (10). The others are at most
`C sqrt(u)|X|^2` by (10),(12). Division by the gap, followed by the normalization
component, proves `||Omega_ij||<=C`. This supplies the requested second
parameter derivative control without assuming that H_i is bounded on bare L2.
All products in (13) are defined on the common operator domain. The same
calculation gives `|e_ij|<=C sqrt(u)`.

Integrating `|de(sx)[x]|<=C sqrt(u)s|x|^2` over `0<=s<=1` proves the energy
difference in (2). In fact the exact coefficient evenness implies
`Omega_(exp X)=Omega_(exp(-X))` in this balanced trivialization; the derivative
vanishes exactly at I. This does not say that the intrinsic horizontal
connection vanishes to second order.

## 4. Exact horizontal connection, metric covariance and Haar normalization

In coordinates `(U,K0)`, let `b(U)=C_ku C_uu^(-1)`. For the bouquet `b=I/2`;
for the strip

```text
b(U)=(4I-R*)[8I-R-R*]^(-1).
```

A coarse right-trivialized velocity E has horizontal K0 velocity `b(U)E`.
Differentiating `U=H^2` exactly gives

```text
dH H^(-1)=(I+Ad H)^(-1)E.
```

Differentiating `K0=H F` then gives the balanced fiber velocity

```text
r_U(E)=Ad(H)^(-1)[b(U)-(I+Ad H)^(-1)]E,
D^hor_E=d_E+D_(r_U(E)).                                (14)
```

This formula uses the actual coarse metric horizontal lift; it is not an
independent rescaling of the source or conditional norm. Its fiber coefficient
is independent of F. Thus the fiber Lie derivative is Haar-skew with zero
fiber divergence. The coefficient in brackets vanishes at I and is smooth;
uniformly, `||r_U||<=C|X|` and `||dr_U||<=C`.

An exact factorization verifies the vanishing. Put `Q_h=Ad H`, so `R=Q_h^2`.
All displayed functions of this orthogonal operator commute. With
`C=8I-Q_h^2-Q_h^(-2)`,

```text
r_bouquet = (Q_h-I)[2 Q_h(I+Q_h)]^(-1),
r_strip = (Q_h-I)(Q_h^2+5Q_h+I)
                    [Q_h^2 C(I+Q_h)]^(-1).            (15)
```

These inverses are bounded on the chosen neighborhood. For `B_ad=ad X`,
their first terms are respectively `B_ad/8` and `7 B_ad/24`. The latter
recovers the earlier `7alpha/12` balanced Z-lift when
`X=alpha Q`, `F=exp(alpha Z/2)`; it is a normalization check of the exact
same link metric, not a replacement gauge.

The first bound in (3) follows by combining (2), the bounded conversion
between exponential coordinates and right-trivialized coarse tangent frames,
`||r_U||<=C|X|`, and the first-fiber derivative estimate (8). The positive real
normalization implies

```text
<Omega_U,D^hor_E Omega_U>=0.                            (16)
```

The parameter term vanishes by differentiating unit norm, while the fiber term
vanishes by Haar skew-adjointness and reality. Thus this chart has zero Berry
connection. Haar measure is fixed before any fiber coordinate expansion.
If one flattens a local fiber density rho into Lebesgue measure, the skew
generator becomes `r.grad+(1/2)div(r)` in that flat representation, because
`div_(rho)(r)=0`. Its half-density term is thereby included rather than dropped.

Gauge conjugation carries B, S and r covariantly and acts unitarily on Haar
fiber space. Uniqueness and positivity therefore give
`Omega_(gUg^-1)(gFg^-1)=Omega_U(F)`. The ground-bundle map preserves the
residual physical invariant subspace. No claim of a generic class-function
factor-two gap is used; the uniform gap input is the full fiber gap.

For clarity, uniform boundedness of balanced second parameter derivatives does
not imply uniform boundedness of all intrinsic horizontal second derivatives.
From (8),(12),(14), in a smooth coarse frame one obtains the sufficient estimate

```text
||D^hor_a D^hor_b Omega_U||
 <=C[u^(1/4)+sqrt(u)|X|^2].                            (17)
```

The derivative of r times the first fiber derivative supplies the first term.
The product of two r factors times a second fiber derivative supplies the
second. Mixed parameter/fiber derivatives are controlled by (12). This records
the scale of second horizontal derivatives needed for any later operator-level
coupling calculation; it does not assert the stronger false uniform estimate.

## 5. Born–Huang bound and exact projected-energy sandwich

The horizontal coefficient C_uu is bounded and positive on the chosen compact
coarse set. Thus (3) follows directly from (14),(8),(2). Since
`v(exp X)` is uniformly comparable to `|X|^2` on this chart, it has the stated
form `Phi_BH<=C sqrt(u) v(U)`.

For the principal-root eigenvalues `c_j=cos(theta_j/2)>0`, put
`eta=sum_j(1-c_j)`. The exact scalar relation is

```text
v(U)=2 sum_j(1-c_j^2),
2 eta<=v(U)<=4 eta,       V_c=4u eta>=u v(U).            (18)
```

The ground-bundle map `J psi(U,F)=psi(U)Omega_U(F)` is an isometry because
the fiber ground is normalized in fixed Haar measure. On smooth compactly
supported psi, its fine form is finite by (8),(14). Substituting in the exact
horizontal-plus-vertical completed-square form and using (16) gives

```text
q_full[J psi]
 =q_c[psi]+int [V_c(U)+e(U)+Phi_BH(U)]|psi(U)|^2 dU.    (19)
```

There are no discarded mixed terms or Berry terms in (19). Combining (2),(3),
(18) gives

```text
|e(U)-e(I)|<=C u^(-1/2) V_c(U),
0<=Phi_BH(U)<=C u^(-1/2) V_c(U),
```

which proves (4). The constants can be enlarged once to apply throughout the
fixed chart and all `u>=max(u0,1)`. The exact coarse kinetic metric/measure are
kept on both sides, so the result is not a norm-rescaling argument. It bounds
the aggregate scalar zero-point and Born–Huang correction, rather than claiming
that those scalars constitute the entire coarse effective Hamiltonian.

For any number r of **additive disjoint-edge copies** of this same block,
the tensor ground bundle gives the same relative constant after summing (4)
and subtracting `r e(I)`. General coarse wavefunctions and a common residual
Gauss constraint are allowed. This tensor observation has no dependence on
r in the error factor, but it does not add plaquettes or shared-edge kinetic
couplings between the copies. The required ambient interacting-block bound
is still a separate problem.

## 6. Exact contribution and remaining obligations

The preceding proof establishes a u-uniform derivative bound for an actual
all-SU(N) finite Wilson fiber, its intrinsic geometric correction, and an
actual local projected coarse form with relative `O(g^2)` magnetic error.
The global vertical barrier proof handles the region outside this local chart
at the level of the vacuum-referenced vertical form. Together these provide
concrete inputs for a global block comparison without a raw conditional
diffusion-gap premise.

The ground-bundle projection P here is not asserted to contain the actual
full-block vacuum, to reduce the full Hamiltonian, or to coincide with the
OS-history projection. In particular `e(I)` is a central fiber ground energy,
not the full-block vacuum energy. Off-diagonal coupling, the true vacuum shift,
global patching of the projected coarse model, and interactions between blocks
must be controlled before invoking the earlier full Schur scale theorem.
The exact operator domains and second derivative estimates above make those
next comparisons well-posed; they do not supply them by assumption.

The proof uses the established uniform fiber gap and exact metric. The companion
[symbolic control](../../runs/nonlinear_wilson_block_2026-09-05/check_ground_bundle_geometry.py), with
[saved output](../../runs/nonlinear_wilson_block_2026-09-05/check_ground_bundle_geometry.json), checks the rational metric/lift
identities, matching first coefficients, and a noncommuting spin-one Casimir
example. These finite calculations do not certify this entire uniform operator
theorem or any continuum conclusion. The independent mathematical reviewer
accepted the graph-norm, domain, normalization, horizontal and projected-form
arguments at the precise finite-block and near-identity scope stated here.

The [nonlinear block run](../../runs/nonlinear_wilson_block_2026-09-05/README.md) preserves the original derivation,
independent audit, exact control and native replay with their separate scopes.
