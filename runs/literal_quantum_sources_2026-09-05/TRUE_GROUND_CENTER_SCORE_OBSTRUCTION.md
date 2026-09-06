# Exact true-ground score at the central SU(2) coarse holonomy

5 September 2026. Outputs-only analytic successor. This note disproves the
specific global true-ground Fisher growth candidate proposed in Section 5
of `next_literal/GROUND_MARGINAL_SCHUR_SCORE.md`. Its generic intrinsic-score
and Schur comparison theorem remains valid under its explicit hypotheses.
The obstruction below is an exact ODE and Haar integration identity. It
does not assume a forbidden-region WKB approximation.

## 1. Actual bouquet and electric normalization

Use SU(2) with Lie metric <X,Y>=-2ReTr(XY) and orthonormal generators
T_a=i sigma_a/2. Write

```text
K=cos(theta)I+2sin(theta) n.T,   0<=theta<=pi, n in S^2,
v(K)=2-ReTr(K)=2-2cos(theta),
Delta_class=(1/4)(partial_theta^2+2cot(theta)partial_theta).
```

For a fixed a>0 define the one-loop operator

```text
h_1=-(a/2)Delta+2u v,       u>0,                           (1)
```

and the two-loop additive operator H=h_1,1+h_1,2. The parameter a=1
is the unit-rotor normalization. For the actual two square loops sharing
only their base vertex, every loop has four distinct electric edges, so
the actual electric form is four times
the product unit-rotor form and a=4. More directly each of the four edges
of each square contributes the same face gradient square, giving
H_E=-2(Delta_1+Delta_2). The loops have eight distinct edges, not the
seven-edge adjacent-square strip. There is no interloop plaquette term.

The ground omega_u of (1) is real, strictly positive, smooth and normalized
in Haar L2. Positivity improvement gives uniqueness; conjugation invariance
then makes it a class function. Write e_u for its energy. The exact ground
of H is Omega_u(U1,U2)=omega_u(U1)omega_u(U2), of energy 2e_u. It is
invariant under the one common diagonal Gauss action.

In global coordinates U=U1 U2 and K=U1, the actual product metric has

```text
C_uu=2a I,   C_uK=C_Ku=a I,   C_KK=a I,
b=C_Ku C_uu^-1=(1/2)I,   S=(a/2)I.                       (2)
```

For example a left variation of U1 gives tangent pair (E,E) in (U,K),
while a left variation of U2 gives (Ad(K)E,0). Summing the two quadratic
contributions proves (2) at every U,K. All reference measures are Haar.

## 2. The exact horizontal score at U=-I

Let Y=K^-1 U. The true normalized conditional ground density is

```text
rho_U(K)=omega_u(K)^2 omega_u(K^-1 U)^2 / mu_u(U),
mu_u(U)=integral omega_u(K)^2 omega_u(K^-1 U)^2 dK.         (3)
```

At U=-I, Y=-K^-1 has angle pi-theta and the same axis n under the
convention above. Put ell(theta)=log omega_u(theta),

```text
A(theta)=ell'(theta),    B(theta)=ell'(pi-theta),
d(theta)=A(theta)-B(theta),   s(theta)=A(theta)+B(theta).   (4)
```

The letter A in (4) is a scalar logarithmic derivative, not the coarse
cometric C_uu. The center marginal is invariant under all conjugations,
so its derivative at -I vanishes exactly: no nonzero adjoint-invariant
linear functional exists on su(2).

For a left coarse velocity E=e_a T_a at fixed K, the angle of Y has
derivative n_a/2. For the left fiber velocity T_a at fixed U, the angles
of K and Y have derivatives n_a/2 and -n_a/2. The horizontal lift in (2)
is the sum of the coarse velocity and half this fiber velocity. Thus
both loop angles change by n_a/4 along a horizontal lift at the center.
The fiber Haar divergence of this constant left vector field is zero.
The exact centered intrinsic score is consequently

```text
score_a(-I,K)
 = partial_(U,a) log rho_U
   + div_K(rho_U b_a)/rho_U
 = (1/2)[A(theta)+B(theta)]n_a.                           (5)
```

Changing the common generator orientation changes the displayed vector
sign, not its Fisher matrix. The conditional axis is uniform on S^2 and
independent of theta, so E(n_a n_b)=delta_ab/3 and the score mean is zero.
The radial conditional law is

```text
p_u(theta)dtheta
 = Z_u^-1 sin(theta)^2 omega_u(theta)^2
                    omega_u(pi-theta)^2 dtheta.           (6)
```

Writing expectation under (6) as E_c, the exact Fisher matrix is

```text
I_c=E_c(score score^*)=(1/12)E_c(s^2) I_3.                (7)
```

## 3. Exact radial identity and the linear-u lower bound

The class ground equation obtained directly from (1) is

```text
ell''+(ell')^2+2cot(theta)ell'
 = (32u/a)(1-cos(theta))-8e_u/a.                          (8)
```

Equivalently, f=sin(theta)omega_u is the positive Dirichlet ground on
(0,pi) of

```text
-(a/8)f''+4u(1-cos(theta))f=(e_u+a/8)f.                  (9)
```

This verifies the radial Casimir and constant-shift conventions without
invoking semiclassical log derivatives.

Adding (8) at theta and pi-theta gives, since B'(theta)=-ell''(pi-theta),

```text
d'=64u/a-16e_u/a-(A^2+B^2)-2cot(theta)d,
p_u'/p_u=2cot(theta)+2d.                                 (10)
```

Smooth positive class functions have zero radial derivative at both
central endpoints. In particular A,B=O(theta) at theta=0 and
O(pi-theta) at theta=pi for each fixed u. Hence p_u d vanishes at both
endpoints, with order at least three. All terms in the following Haar
integration by parts are integrable:

```text
E_c d' = -E_c[d(2cot(theta)+2d)].
```

Insert (10). The cotangent terms cancel exactly and give

```text
E_c(A^2+B^2)=64u/a-16e_u/a+2E_c(d^2),
E_c(s^2)=128u/a-32e_u/a+3E_c(d^2).                       (11)
```

Combining (2),(7),(11), the full weighted intrinsic Fisher matrix is

```text
C_uu^(1/2) I_c C_uu^(1/2)
 = [(64/3)u-(16/3)e_u+(a/2)E_c(d^2)] I_3
 >= [(64/3)u-(16/3)e_u] I_3.                             (12)
```

The leading lower coefficient is independent of the electric normalization
a; the raw Fisher matrix itself has the corresponding factor 1/a.
This is an exact identity for every u>0, including when the displayed
lower bound is not positive.

A localized Gaussian trial near the identity, of width u^-1/4 in the
three smooth Lie coordinates, proves e_u<=C_a sqrt(u) for u>=1. Its
kinetic expectation is O_a(sqrt(u)); the inequality
1-cos(theta)<=theta^2/2 bounds the magnetic expectation by the same order.
The normalization scales as u^-3/4, chart cutoffs have exponentially
small Gaussian tails, and the smooth positive Haar density is uniformly
comparable to Euclidean measure on that fixed chart. Also e_u>=0 by (1).
These elementary variational bounds, or the established compact-rotor
localization theorem, are sufficient to conclude

```text
liminf_(u->infinity) u^-1
  lambda_min(C_uu^(1/2)I_c C_uu^(1/2)) >= 64/3.             (13)
```

No assertion that E_c(d^2)=o(u), no exact leading asymptotic equality,
and no WKB remainder is needed or claimed.

## 4. The failed global candidate and its exact scope

At U=-I, v(U)=4. For any fixed finite C0,C1, (12)--(13) contradict

```text
C_uu^(1/2) I(U) C_uu^(1/2)
 <= [C0+C1 sqrt(u) v(U)]I                               (14)
```

for all sufficiently large u. Therefore the proposed global true-ground
Fisher estimate in Section 5 of the preceding score note is false already
on the actual a=4 two-square bouquet. It cannot serve as an all-block
Wilson hypothesis with constants independent of u.

This is not only a measure-zero exceptional point. For every fixed u the
ground, positive marginal, conditional density and Fisher matrix are
smooth in U. A strict violation at -I therefore persists on a nonempty
open neighborhood. That neighborhood has positive Haar and true-marginal
measure. Uniform almost-everywhere formulations of (14) fail as well.

The generic score theorem remains correct. This argument does not prove
that every alternative weighted criterion has eta>=1, that no physical
gradient-restricted inequality is useful, or that the full quantum gap
is small. For a smooth class function of one coarse holonomy the coarse
gradient at -I itself vanishes by symmetry. A matrix bound in all coarse
directions is stronger than the actual form estimate on a selected
physical source or energy space. The counterexample must not be promoted
to the failure of that weaker, more relevant estimate.

The exact product ground in (3) is the true quantum ground. Thus this
obstruction differs from both the earlier raw Wilson Gibbs conditional
score and the intrinsic conditional rotor-ground derivative bound.

## 5. A surviving energy-localized Schur criterion

Use the generic score setting of the preceding note. Write C(U) for the
coarse cometric, nu=Omega^2 dU dK, mu for its marginal, and I(U) for the
actual intrinsic conditional Fisher matrix. Let Q be conditional mean-zero
and F its actual full vacuum-subtracted restricted form. Assume

```text
F >= multiplication by w(U) on Q,       w>=f0>0.           (15)
```

Multiplication by a coarse function preserves Q. For a smooth coarse f,
define the centered cross vector

```text
(T f)(U,K)=-(1/2) score(U,K)^* C(U) grad f(U).
```

Its conditional mean is zero, and the exact cross form is <T f,g>.
The actual static Schur loss is therefore

```text
Sigma[f]=||F^-1/2 T f||^2
 <= (1/4) integral w(U)^-1
           grad(f)^* C(U) I(U) C(U) grad(f) dmu(U).        (16)
```

The inverse inequality follows from (15), or directly by the variational
formula for F^-1. Equation (16) extends by the stated form approximation
whenever its right side is finite. It retains the actual energy weight;
it does not require a pointwise small Fisher ratio.

Let a[f]=(1/2)integral grad(f)^* C grad(f) dmu, and choose a closed
coarse low-energy source subspace L in the marginal form domain, for
example a specified finite spectral window of its true marginal operator.
Partition the coarse space into G and B. Suppose

```text
C^(1/2) I C^(1/2) <= 2 eta_G w I on G,
C^(1/2) I C^(1/2) <= 2 C_B w I on B,
a_B[f]:=(1/2)integral_B grad(f)^* C grad(f) dmu
       <= epsilon_L a[f],       f in L.                 (17)
```

Then (16) proves the useful operator-form estimate

```text
Sigma[f] <= (eta_G+C_B epsilon_L) a[f],   f in L.          (18)
```

If C_B>=eta_G, the sharper coefficient is
eta_G+(C_B-eta_G)epsilon_L. These statements control arbitrary
superpositions in L. In particular eta_G=O(g^2), bounded C_B, and a
coarse-gradient energy leakage epsilon_L=O(g^2) would give the desired
relative loss O(g^2) on that whole source window, even though the
pointwise global candidate (14) is false.

All three estimates in (17), the actual full-Q bound (15), and the
appropriate coarse source window must still be verified for the intended
interacting Wilson family. Small marginal probability of B alone is not
the third estimate: arbitrary gradients can concentrate in a rare region.
The needed object is the restricted gradient-energy operator, or the
still sharper resolvent-weighted norm ||F^-1/2 T f||. The source window,
true marginal metric and physical clock must remain the same throughout
the scale comparison.

A bound only on this selected low marginal window does not prove a full
Schur gap or exclude low states descending from high retained energies
through strong mixing. That application additionally needs control of
the remaining retained space and its coupling, or a proved complete fine
low-window comparison. The global gap formula of the preceding score
theorem cannot be applied merely by substituting (18) on L.

Thus the next central task is energy-localized actual score/form control,
not the disproved global sublinear Fisher candidate. The proven additive
literal projection and regulated Gaussian full-quantum bounds remain
reference inputs. Interacting interfaces, nonlinear coarse matching,
generated temporal memory and the continuum limit remain separate.

## 6. Provenance and finite evidence

The exact center identity (11)--(12) was first isolated by the root
collaborator, then independently checked here and by the geometry audit.
The metric normalization follows directly from the actual two-square
bouquet discussed in the canonical block-score source; the true-vacuum
projection and generic Schur score theorem are the immediate preceding
outputs. The canonical adjacent-strip and conditional fiber theorems are
not premises identifying this bouquet's conditional density.

The companion `check_central_score_identity_independent.py` tests the
Riccati algebra, Haar integration identity on an exact reconstructed
smooth-potential example, SU(2) horizontal derivatives, Casimir factors
and axis moments. Its positive trial function is explicitly not asserted
to be the Wilson ground. The actual Wilson conclusion uses the analytic
ground equation (8), exact integration by parts and the variational
O(sqrt(u)) energy upper bound. No fitted numerical asymptotic or unproved
forbidden-region log-derivative approximation enters the result.
