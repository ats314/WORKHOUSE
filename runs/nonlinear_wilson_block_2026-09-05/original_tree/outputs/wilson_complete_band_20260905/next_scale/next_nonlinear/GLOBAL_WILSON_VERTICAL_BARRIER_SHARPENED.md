# A global Wilson fiber spectral cap and coarse-potential comparison

5 September 2026. Outputs-only successor research. This companion sharpens
`GLOBAL_WILSON_VERTICAL_BARRIER.md` without changing its bytes or the sealed
scale-comparison package. The statements below concern the actual intrinsic
vertical operators of one two-face block, at every fixed rank. Their proof is
an operator-form argument; the companion Python file checks exact algebra and
finite group examples, not the infinite-dimensional spectral theorem.

## 1. Operators, domains and conclusions

Use SU(N), N >= 2, the Lie metric -2 ReTr(XY), normalized Haar measure, and
v(U) = N - ReTr U. For a coarse product U = U1 U2, use fiber K = U1. The
original-link calculation in
`paper/research_notes/G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md`, Sections
3--4, gives the two exact operators

```
A_U = T_U + 2u[v(K) + v(K^-1 U)],              u > 0,
T_U^bouquet = -Delta,
T_U^strip = -(1/2) sum_ab S(U)^ab L_a L_b,
S(U) = 15[8I - Ad(U) - Ad(U)*]^-1.                    (1)
```

All inequalities are closed quadratic-form inequalities on H^1(SU(N)).
The strip metric satisfies (3/2)I <= S(U) <= (5/2)I, so the form domains
are independent of U. On the compact connected group each operator has
compact resolvent and a unique normalized strictly positive ground state.
Let E_j(U), j = 0,1,..., be the full fiber eigenvalues, with multiplicity;
P_U is the ground projection. In particular these are not eigenvalues
restricted to class functions or to the stabilizer of a generic U.

Write e_j = E_j(I), delta = e_1 - e_0, and

```
epsilon_N = min(1, 4/N),       alpha = 8/3.             (2)
```

For both actual blocks, every u > 0, U in SU(N), and every j satisfy

```
E_j(U) >= min(e_j, epsilon_N u),                       (3)
E_j(U) >= e_j + (u - e_j/epsilon_N) v(U).              (4)
```

Thus the spectral counting function below epsilon_N u is dominated by
that of the central rotor. There is no large-u hypothesis in (3) or (4).
The coefficient in (4) may be negative. The resulting joint form bound is

```
A_U - e_0 >= delta (I-P_U)
              + (u - e_1/epsilon_N) v(U) I.           (5)
```

It holds for every u; its two right-hand terms are nonnegative when
e_1 <= epsilon_N u. In particular, if e_1 <= epsilon_N u/2, the second
term can be replaced by (u/2)v(U). The sufficient threshold is
u >= max(1,N/4)e_1(u), not u >= N^2 e_1(u).

The ground scalar also has a global upper bound. There is a number
m(u,N) in [0,1], depending on the chosen block, such that

```
(u - e_0/epsilon_N)v(U) <= E_0(U)-e_0
                       <= 2u m(u,N) v(U) <= 2u v(U).  (6)
```

The lower coefficient is nonnegative once e_0 <= epsilon_N u. This is
the ground energy of the full conditional potential in (1), including
its coarse-dependent classical minimum. It is not the minimum-subtracted
vertical zero-point scalar used in the local Born--Oppenheimer expansion.

The established central compact-rotor theorem gives, for fixed N,

```
delta_bouquet = 2 sqrt(u) + O_N(u^(1/4)),
delta_strip  = sqrt(5) sqrt(u) + O_N(u^(1/4)),
e_1 = O_N(sqrt(u)).                                    (7)
```

Hence the nonnegative thresholds above hold for all sufficiently large u
at each fixed N. Neither (7) nor the present result asserts uniformity as
N grows. The class-function factor two at the central rotor is not used.

## 2. Global barrier without a square root

For arbitrary unitary K,Y, the Frobenius parallelogram identity gives

```
2[v(K)+v(Y)] - v(KY) = (1/2)||I-2K+KY||_F^2 >= 0.     (8)
```

Taking Y = K^-1 U and using T_U >= 0 yields

```
A_U >= u v(U) I.                                      (9)
```

This controls the entire region v(U) > epsilon_N. No global choice of
square root, stabilizer chart or conditional excited gap is required there.

## 3. A genuine SU(N) square root on the remaining region

Suppose v(U) <= epsilon_N. Its principal eigenangles theta_i satisfy
|theta_i| <= (pi/2)|1-exp(i theta_i)|, so Cauchy--Schwarz gives

```
|sum theta_i| <= sum |theta_i|
 <= (pi/2) sqrt(2 N v(U)) <= pi sqrt(2) < 2 pi.        (10)
```

Here N epsilon_N <= 4. Since det U = 1, sum theta_i is an integer
multiple of 2 pi and is therefore zero. The principal H = U^(1/2)
belongs to SU(N). In fact v(U) <= 1 excludes an eigenangle pi, so
there is no cut-locus ambiguity on this neighborhood.

Set A = Re H, eta = Tr(I-A), and translate K = H F. If c_i are the
eigenvalues of A, then 0 <= c_i <= 1, and

```
v(U) = 2 sum_i(1-c_i^2),
2 eta <= v(U) <= 4 eta,        0 <= eta <= 1/2,
A >= (1-eta)I.                                        (11)
```

The exact balanced potential is

```
2u[v(HF)+v(F^-1 H)]
 = 4u eta + 4u Tr[A(I-Re F)]
 >= 4u eta + (1-eta) 4u v(F).                         (12)
```

The trace inequality is valid for noncommuting matrices. Specifically,
B = I-A >= 0, eta = Tr B, and Q = I-Re F >= 0 imply

```
Tr(AQ) - (1-eta)Tr Q = eta Tr Q - Tr(BQ) >= 0.         (13)
```

If B and Q are written as sums of rank-one positive matrices, the
right-hand side is the sum of the complex Lagrange squares
|v_i w_j - v_j w_i|^2. Thus no simultaneous diagonalization of B,Q is
assumed. Positivity of Q is essential to this argument.

## 4. Sharpened adjoint estimate and exact metric comparison

Let R = Ad(U), and D = (I-R)(I-R*) >= 0. Diagonalize U, with eigenvalues
z_i. The complex root spaces have eigenvalues z_i/z_j under R, and its
Cartan subspace has eigenvalue one. Since the real adjoint norm agrees
with the complexified norm,

```
||D|| = max_(i != j) |z_i-z_j|^2
 <= 2 sum_k |z_k-1|^2 = 4 v(U) <= 16 eta.             (14)
```

This uses |a-b|^2 <= 2(|a|^2+|b|^2), not an estimate growing with
the dimension of the Lie algebra. The exact strip metric ratio is

```
S(U)/(5/2) = 6(6I+D)^-1 >= t(eta) I,
t(eta) = 1/(1+(8/3)eta).                              (15)
```

On 0 <= eta <= 1/2 one has

```
3/7 <= t <= 1,
(1-eta)-t = eta(5-8eta)/(3+8eta) >= 0,
1-t <= alpha eta.                                    (16)
```

Translation by H preserves Haar measure. Its rotation of the invariant
derivatives is Ad(H), which commutes with S(U), so (15) remains an
inequality of the actual translated strip forms. For the bouquet,
T_U = T_I >= t T_I directly. Combining (12), (15), (16) gives the same
form inequality for both blocks, after this unitary translation:

```
A_U >= t A_I + 4u eta I.                              (17)
```

No truncation of the rotor space appears in (17).

## 5. Min-max, all counted levels, and the joint bound

The min-max principle applied to (17) gives E_j(U) >= t e_j+4u eta.
Since 1-t <= alpha eta,

```
t e_j + 4u eta >= t e_j + (1-t)(4u/alpha)
                >= min(e_j, epsilon_N u),             (18)
```

because 4/alpha = 3/2 >= epsilon_N. Outside the neighborhood, (9)
gives every eigenvalue at least epsilon_N u. This proves (3), including
all multiplicities, for every u and j.

For a direct proof of (4), put b_i = 1-c_i >= 0. From (11),

```
v(U) = 4eta - 2 sum b_i^2 >= 4eta - 2eta^2 >= 3eta.
1-t <= (8/3)eta <= v(U) <= v(U)/epsilon_N.             (19)
```

Also 4eta >= v(U). The central e_j are nonnegative, so (17) implies
E_j(U)-e_j >= (u-e_j/epsilon_N)v(U), without requiring this coefficient
to be positive. Outside, (9) and v(U) >= epsilon_N give the same bound.
This proves (4).

For the ground, (4) is at least
e_0+(u-e_1/epsilon_N)v(U). On its orthogonal complement the spectral
theorem gives A_U >= E_1(U), and (4) at j=1 supplies
e_1+(u-e_1/epsilon_N)v(U). This proves (5). Higher-index affine lower
bounds need not be ordered in j and are not used in this last step.

A more precise piecewise barrier, useful when e_1 <= epsilon_N u, is

```
b(U) = 4u eta - (1-t)e_1,       v(U) <= epsilon_N,
       u v(U) - e_1,           v(U) > epsilon_N.
A_U-e_0 >= delta(I-P_U) + b(U)I.                       (20)
```

Its ground bound follows because e_0 <= e_1. Both pieces are nonnegative
under the stated threshold, and dominate the scalar term in (5).

## 6. A global upper bound for the induced coarse potential

Use the central normalized positive ground phi_I(K) as an unbalanced
trial function at every U; there is no square root in this trial. The
central operator is invariant under conjugation and inversion. Uniqueness
and positivity of its ground imply the same invariances of phi_I. Hence
irreducibility of the defining SU(N) representation gives

```
integral K phi_I(K)^2 dK = m I,
```

and inversion makes m real. The operator norm of an average of unitaries
is at most one, so m <= 1. The constant trial at the center has energy
4uN, because the Haar mean of the defining representation is zero. Thus

```
e_0 = <phi_I,T_I phi_I> + 4uN(1-m) <= 4uN,
```

and T_I >= 0 implies m >= 0. For the strip, S(U) <= S(I) gives
T_U <= T_I; this is equality for the bouquet. The difference of potential
expectations is exactly 2u m v(U). The variational principle therefore
gives E_0(U) <= e_0+2u m v(U). Together with (4) this proves (6).

## 7. SU(2): the exact obstruction and its repair

Write U = exp(i theta n.sigma), 0 <= theta <= pi, c = cos(theta/2),
H = U^(1/2), and F = x0 I+i x.sigma. Then the exact balanced potential is

```
V(U,F) = 8u(1-c x0).                                  (21)
```

At U = -I it is exactly the constant 8u. The bouquet kinetic is -Delta.
For the strip Ad(-I)=I, so the kinetic is exactly -(5/4)Delta. With the
metric convention of (1), the first nonzero SU(2) Casimir is 3/4.
Consequently the exact conditional gaps at this coarse value are 3/4
and 15/16, respectively, for every u. This rules out a global estimate
of the form A_U-E_0(U) >= c0 sqrt(u)(I-P_U) with c0>0 fixed.

For general SU(2) U the strip metric ratio has one longitudinal
eigenvalue one and two transverse eigenvalues

```
r(c) = 6/[6+16c^2(1-c^2)].                            (22)
```

At c=0 the metric is isotropic despite the nonunique square root. The
large absolute energy 8u, retained in (5), resolves the conditional-gap
obstruction. No extrapolation of numerically truncated eigenvalues is
involved in this conclusion.

## 8. Direct integral, full vacuum subtraction and the next obligation

The uniformly elliptic family in its original K chart is smooth in U.
Its simple ground projection is therefore measurable globally. For a
positive finite coarse measure, (5) integrates on the vertical direct-
integral form domain. With a conjugation-invariant coarse measure,
covariance and uniqueness make the direct-integral projection compatible
with the residual physical gauge action. Restriction to that subspace
preserves (5); it does not double delta.

The exact horizontal-square decomposition in
`paper/research_notes/G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md`,
Section 1, puts this vertical form inside the full original-link block
form. It is a bound before subtracting the true full-block ground energy.
In particular e_0 is a central fiber ground, not the full-block vacuum.
For the SU(2) strip the leading difference is
(3sqrt(3)/2)sqrt(u), already larger than the full vertical gap
sqrt(5)sqrt(u). Subtracting this difference and then discarding it would
invalidate a claimed positive full fast compression.

The concrete advance is an all-coarse-space spectral cap and a genuine
global Wilson-potential sandwich for the actual conditional ground,
together with its fast penalty. To use it uniformly in a lattice one
must control horizontal motion, the varying ground and Born--Huang term,
interblock couplings and the vacuum-adapted retained projection. The
closed-form Schur scale theorem then additionally needs its induced mass
and literal/OS source hypotheses. No sum of fixed per-block vacuum errors,
global OS reducing range, continuum limit, or volume-uniform nonlinear
fast-complement theorem follows from this one-block result alone.

## 9. Reproducible evidence and provenance

The argument depends on the exact original-link metric and central rotor
theorems cited above, and sharpens the separate conservative candidate
`GLOBAL_WILSON_VERTICAL_BARRIER.md`. The latter remains unchanged by this
companion. No earlier canonical proof, code or sealed run is modified.

Run the guarded, fresh-output control from the repository root:

```
.venv/Scripts/python.exe outputs/wilson_complete_band_20260905/next_scale/next_nonlinear/check_global_wilson_vertical_barrier.py --output <new.json>
```

It checks arbitrary-symbol complex Lagrange and parallelogram identities;
noncommuting rational PSD trace inequalities and a missing-positivity
counterexample; actual rational SU(2) group, adjoint, metric and Casimir
calculations; and symbolic scalar budgets for the cap, all-u affine bound,
joint gap/potential estimate and the ground trial. It records hashes of
the proof inputs and script, refuses overwrite and optimized Python, and
uses no numerical eigensolver. These are finite and algebraic controls.
The domain, compact-resolvent, ground-positivity and all-rank conclusions
are established by the analytic argument, not certified by the control.
