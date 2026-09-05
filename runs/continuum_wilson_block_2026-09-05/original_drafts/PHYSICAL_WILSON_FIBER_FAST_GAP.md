# Physical Wilson fiber fast energy

Date: 2026-09-05. Status: analytic proof for the specified finite constrained
rotors. This advances the fast-mode obligation in
[REVERSE_MASS_MATCHING.md](REVERSE_MASS_MATCHING.md). It replaces the false
raw-diffusion premise by a physical-electric calculation on an actual Wilson
block. Identification with the reducing complement of an OS-history block
isometry is a separate, still required step.

The geometric input is derived below and independently in
[WILSON_BLOCK_CONDITIONAL_SCORE.md](WILSON_BLOCK_CONDITIONAL_SCORE.md), Sections
1 and 6.1. No product kinetic metric is inferred from product Haar measure.

## 1. The compact-rotor theorem

Let G=SU(N), N>=2 fixed, d=N^2-1. Use the bi-invariant metric

```text
<A,B> = -2 ReTr(AB),   A,B in su(N),
-Delta chi_R = C_R chi_R.
```

Write v(K)=N-ReTr K and, for kappa,lambda>0, define the self-adjoint
Schrodinger operator through its closed quadratic form on H^1(G):

```text
H_(kappa,lambda) = -kappa Delta + lambda v.
```

Its resolvent is compact. Let E0,E1 be its first two eigenvalues, counting
multiplicity, and E0^cl,E1^cl the corresponding eigenvalues on the closed
subspace of conjugation-invariant functions. Then, as lambda/kappa tends
to infinity,

```text
E0 = (d/2) sqrt(kappa lambda)
       + O_N(kappa^(3/4) lambda^(1/4)),
E1 = (d/2+1) sqrt(kappa lambda)
       + O_N(kappa^(3/4) lambda^(1/4)),

E0^cl = (d/2) sqrt(kappa lambda)
          + O_N(kappa^(3/4) lambda^(1/4)),
E1^cl = (d/2+2) sqrt(kappa lambda)
          + O_N(kappa^(3/4) lambda^(1/4)).                 (1)
```

Consequently, for some finite threshold L_N and lambda/kappa>=L_N,

```text
gap(H_(kappa,lambda)) >= (1/2) sqrt(kappa lambda),
gap(H_(kappa,lambda) on class functions) >= sqrt(kappa lambda). (2)
```

The thresholds and constants depend on fixed N, not on an ambient lattice
volume or on a time discretization. No uniformity as N tends to infinity is
claimed. The factor two in the leading physical class-function gap is a
selection rule, not a change in the kinetic normalization.

The same theorem holds for any compact connected group G with simple Lie
algebra and a faithful finite-dimensional unitary representation rho. Choose
a bi-invariant metric and define the positive constant b_rho by

```text
-ReTr[d rho(X) d rho(Y)] = b_rho <X,Y>.
```

Ad invariance and simplicity make this form a scalar multiple of the metric;
faithfulness makes the scalar positive. For
v_rho=dim(rho)-Re chi_rho, the unique zero is I and the local potential is
(b_rho/2)|x|^2+O(|x|^4). Replace sqrt(kappa lambda) everywhere in the leading
eigenvalues (1) by

```text
omega_rho = sqrt(2 b_rho kappa lambda).
```

The full gap is omega_rho+o(omega_rho), and the class-function gap is
2omega_rho+o(omega_rho). Constants depend on G, rho and the fixed metric.
The proof below applies without any other change: the adjoint has no
invariant linear vector and has the invariant quadratic norm. For the SU(N)
fundamental representation and the metric used here, b_rho=1/2.
Faithfulness is essential to this unique-well conclusion: a nontrivial
representation kernel gives several zero-potential minima, and the first
gap can then be controlled by tunneling rather than the local oscillator.
This generalizes the constrained-rotor theorem; it makes no extension claim
for the separate SU(N) charge-odd plaquette-band construction.

## 2. Proof by localization and min-max

Put h=sqrt(kappa/lambda); then H=lambda P_h, where P_h=-h^2 Delta+v.
In exponential normal coordinates K=exp X, X=sum_a x_a T_a in an orthonormal
Lie basis,

```text
v(exp X) = |x|^2/4 + O_N(|x|^4),
g^ab(x) = delta_ab + O_N(|x|^2),
J(x) = 1 + O_N(|x|^2).                                  (3)
```

The first equality follows directly by expanding ReTr exp X: odd powers have
pure imaginary trace and Tr X^2=-|x|^2/2. The other two are the normal-coordinate
metric and volume estimates. All estimates are uniform on a sufficiently
small fixed ball. Thus local Dirichlet Rayleigh quotients on a radius-2r ball
are bounded below and above by (1+O_N(r^2)) times the Euclidean oscillator
quotient, with its measure and norm compared by the same bounds.

The unique zero of v is I: for unitary K, ReTr K<=N, with equality only when
all eigenvalues are one. Compactness and the positive Hessian at I give

```text
v(K) >= c_N dist(K,I)^2                                  (4)
```

on the whole compact group, after lowering c_N if necessary.

Choose r=h^(1/4), for h small, and conjugation-invariant smooth functions
chi_0,chi_1 with chi_0^2+chi_1^2=1, chi_0 supported inside radius 2r,
chi_1 vanishing inside radius r, and sum |grad chi_i|^2<=C_N/r^2. The IMS
identity gives

```text
q_h(psi) = q_h(chi_0 psi)+q_h(chi_1 psi)
             - h^2 integral sum_i |grad chi_i|^2 |psi|^2,
IMS error <= C_N h^2/r^2 = C_N h^(3/2).                  (5)
```

The outside form is at least c_N r^2=c_N h^(1/2) times the outside norm.
That scale is larger than the O(h) low eigenvalues.

For completeness, the lower eigenvalue comparison does not assume that a
global eigenfunction is already localized. Let lambda_j^loc be the j-th
Dirichlet eigenvalue in the radius-2r ball. Impose the j linear conditions
that chi_0 psi be orthogonal to its first j Dirichlet eigenfunctions. This
defines a subspace of codimension at most j. On it, (5) gives

```text
q_h(psi) >= [min(lambda_j^loc,c_N r^2)-C_N h^2/r^2] ||psi||^2.
```

Zero extension from the coordinate ball to R^d and (3) imply
lambda_j^loc >= (1-C_N r^2) h e_j, where e_j is the corresponding full-space
oscillator eigenvalue. The min-max principle therefore yields

```text
E_j(P_h) >= h e_j - C_(N,j) h^(3/2).                    (6)
```

For the upper bound, take the first finitely many oscillator eigenfunctions,
rescale x=sqrt(h)y, and multiply by a radial cutoff supported in radius r.
Their Gaussian tails beyond that radius are exponentially small in
r^2/h=h^(-1/2), including the differentiated cutoff terms. The norm and form
comparisons in (3) give, on this finite-dimensional trial space,

```text
E_j(P_h) <= h e_j + C_(N,j) h^(3/2).                    (7)
```

The oscillator is -Delta_y+|y|^2/4. Its levels are d/2+n, n=0,1,... .
Its ground function exp(-|y|^2/4) is invariant. The degree-one eigenspace is
the complexified adjoint representation. It has no invariant vector because
su(N) is simple. The degree-two function

```text
(|y|^2-d) exp(-|y|^2/4)
```

is a nonzero invariant eigenfunction at level d/2+2. These are consequently
the first two invariant levels. The entire localization argument preserves
invariance: normal coordinates intertwine conjugation with Ad, and every
cutoff is radial. Apply the same min-max argument inside the invariant
subspace. This proves (1) after multiplying (6)-(7) by lambda, then (2).

There is no singular-Weyl-chamber assumption in this proof. It works on the
smooth compact group, followed by restriction to an invariant closed
subspace. In particular no boundary condition is guessed at a singular
conjugacy class.

## 3. Exact physical electric factors for two Wilson blocks

The electric convention is H_E=(1/2) sum_edges C2. The magnetic convention is
-u sum_p (chi_p+conjugate chi_p). Adding a scalar to the magnetic operator
will not change its excitation gap.

### 3.1. A bouquet of two squares

Take two square loops sharing only their base vertex. Their edge sets are
disjoint. On functions of their based holonomies U1,U2, differentiation in
any of the four edges of a loop gives a left or right Lie derivative,
orthogonally rotated by an adjoint matrix. Hence the exact link form is

```text
sum_edges |grad_edge F|^2 = 4(|grad_U1 F|^2+|grad_U2 F|^2),
H_E = -2(Delta_1+Delta_2).                               (8)
```

Residual gauge transformations act by simultaneous conjugation. Define
coarse U=U1 U2 and fiber K=U1. In right-trivialized velocities the link
cometric has blocks C_uu=8I, C_uk=4I, C_kk=4I. The metric induced on a
fixed-U fiber has inverse, the Schur complement,

```text
S_fib = C_kk-C_ku C_uu^(-1) C_uk = 2I.
```

Equivalently, the fine metric is one quarter the product group metric;
on the fiber U=I, (U1,U2)=(K,K^(-1)), its pullback is one half the group
metric. The fiber measure is Haar: dU1 dU2=dU dK, and its induced metric
volume differs from Haar only by a constant. Thus the intrinsic vertical
electric form, including the factor 1/2 in H_E, is exactly that of -Delta_K.

At U=I the magnetic term is -4u ReTr K. The constrained fiber Hamiltonian,
after adding 4uN, is therefore

```text
H_fib^bouquet = -Delta_K + 4u(N-ReTr K).                 (9)
```

The theorem gives

```text
gap_full = 2 sqrt(u)+O_N(u^(1/4)),
gap_physical_class = 4 sqrt(u)+O_N(u^(1/4)).             (10)
```

For all sufficiently large u these are at least sqrt(u) and 2sqrt(u),
respectively. The physical sector at the constrained value U=I is precisely
the class-function subspace under the residual gauge action.

### 3.2. Two adjacent squares, with their shared edge retained

Write the based loops as U1=s b1 and U2=b2 s^(-1), where each b_j is a
three-edge outer path and s is their common edge. The exact link form on
based holonomies is

```text
3 sum_j |grad_Uj F|^2 + sum_a |(L1_a-R2_a)F|^2.          (11)
```

For U=U1U2,K=U1, the outer edges give tangent pairs (E,E) and (Ad(K)E,0),
each with multiplicity three. The shared edge gives ((I-Ad(U))E,E).
Writing A=Ad(U), an orthogonal operator on the real Lie algebra, gives

```text
C_uu=8I-A-A*,   C_uk=4I-A,   C_ku=4I-A*,   C_kk=4I,
S_fib(U)=4I-(4I-A*)(8I-A-A*)^(-1)(4I-A)
        =15(8I-A-A*)^(-1),
(3/2)I <= S_fib(U) <= (5/2)I.                          (12)
```

The simplification uses AA*=I and commuting polynomials in A,A*. Every
fiber coefficient is independent of K. Its divergence-free Lie derivatives
therefore give the Haar-symmetric intrinsic operator
-(1/2) sum_ab S_fib(U)^ab L_a L_b. At U=I, S_fib=(5/2)I exactly, for every K.
This derives the full fiber coefficient, not just its value near K=I.

The same magnetic restriction now gives

```text
H_fib^strip = -(5/4) Delta_K + 4u(N-ReTr K),
gap_full = sqrt(5) sqrt(u)+O_N(u^(1/4)),
gap_physical_class = 2sqrt(5) sqrt(u)+O_N(u^(1/4)).       (13)
```

Thus the actual shared-link electric form strengthens the oscillator
coefficient relative to the bouquet, while leaving the mechanism unchanged.

These fiber operators are defined by the induced vertical metric and the
actual Wilson potential. Fixing a coarse coordinate is not restriction to
a reducing subspace of the full two-face Hamiltonian. In particular (9) or
(13) must not be inserted as the OS-history complement Hamiltonian without
a separate comparison or intertwining proof.

## 4. A uniform coarse-neighborhood consequence

The exact calculation is stable on a fixed weak-field coarse neighborhood.
Choose a compact neighborhood of I with principal H=U^(1/2) and

```text
A_U=Re H >= a0 I,   a0>0.
```

Set K=H F, so U1=H F and U2=F^(-1)H. The trace identity is exact, and after
subtracting the coarse-dependent scalar minimum the potential is

```text
4u Tr[A_U(I-Re F)].                                    (14)
```

It is nonnegative with its unique zero at F=I. Indeed
I-Re F is positive semidefinite, and A_U>=a0I. In local coordinates,

```text
4 Tr[A_U(I-Re exp X)] = -2 Tr(A_U X^2)+O_N(|X|^4),
-2 Tr(A_U X^2) >= a0 |x|^2.                            (15)
```

For the bouquet the kinetic matrix is I. For the strip it is S_fib(U)/2,
whose eigenvalues lie in [3/4,5/4]. The shift by H does not change that
matrix: Ad(H) commutes with S_fib(U), a function of Ad(U). These are a compact
smooth family of uniformly elliptic Haar-symmetric operators with a uniformly
isolated nondegenerate potential minimum. Repeating the localization proof
uniformly in U gives convergence of each fixed low eigenvalue divided by
sqrt(u) to the corresponding anisotropic oscillator eigenvalue. Only an
o(sqrt(u)) remainder is needed here; no isotropic error coefficient is
asserted for this general metric.

The first full oscillator gap is at least 2sqrt(a0) for the bouquet and
sqrt(3a0) for the strip. This follows by diagonalizing the positive matrix
K_kin^(1/2) Q_U K_kin^(1/2), where x^T Q_U x=-2Tr(A_U X^2).
Consequently, for u above a threshold uniform on this chosen neighborhood,

```text
gap_fib^bouquet(U) >= sqrt(a0) sqrt(u),
gap_fib^strip(U) >= (sqrt(3a0)/2) sqrt(u).               (16)
```

The positive ground state is invariant under the residual stabilizer of U.
Restricting to its invariant subspace cannot lower the first excitation gap,
so the same lower bounds hold physically. The precise factor-two singlet
improvement (10),(13) was asserted only at U=I, where the residual group is
all of SU(N). This corollary concerns one finite constrained fiber uniformly
on a specified coarse neighborhood; it is not an estimate for unbounded
coarse fields or for interacting collections of blocks.

There is a direct form statement useful for the next comparison. Let e0(U)
and P_fib(U) be the unique ground energy and rank-one ground projection of
the fiber operator. For any finite positive coarse measure nu supported in
the chosen neighborhood and any field psi(U) in the direct-integral form
domain, the uniform spectral theorem gives

```text
integral <psi(U),(H_fib(U)-e0(U)) psi(U)> dnu(U)
 >= c sqrt(u) integral ||(I-P_fib(U)) psi(U)||^2 dnu(U).  (16a)
```

Here c is the appropriate constant in (16). The ground projections are
measurable (indeed smooth locally as a gapped elliptic family). Thus (16a)
is an exact vertical fast-energy inequality after subtracting the
coarse-dependent fiber ground energy. It identifies the useful projection
and form for a subsequent block comparison. It does not identify this
direct-integral projection with the OS-history projection or account for
the horizontal terms in the full Hamiltonian.

## 5. Why the rare diffusion well is not a low rotor mode

For N>=5 the secondary central point zeta I, zeta=exp(2pi i/N), is a local
minimum of v with positive value N(1-cos(2pi/N)). The cutoff in the block
score note gives an exponentially small weighted configuration-diffusion
gap. In the physical rotor its well bottom instead has potential energy

```text
4u N(1-cos(2pi/N)),                                    (17)
```

which is order u. The physical ground and first low excitations have energy
order sqrt(u). Estimate (4) and the outside term in (5) exclude every region
away from I from that low spectrum, including all secondary wells, without
having to classify each one. A state confined to a rare secondary well has
large physical excitation energy, even though the normalized equilibrium
diffusion leaves that well slowly.

The operators are explicitly different. For the weighted diffusion with
density exp(-beta v), its positive generator is

```text
L_beta = -Delta + beta grad v . grad.
```

Multiplication by exp(-beta v/2) transfers it to Haar space and gives

```text
-Delta + (beta^2/4)|grad v|^2 - (beta/2) Delta v,        (18)
```

not -kappa Delta+lambda v. The effective potential in (18) is sensitive to
all critical wells through grad v; the physical Wilson potential pays the
strict height in (17). Thus the proven diffusion obstruction and the proven
fast physical rotor gap are compatible.

## 6. Physical units and the actual next implication

The Hamiltonian-coordinate convention of the reverse-matching note is

```text
u=g_H^(-4),
H_physical = c_H(a) (g_H^2/a) H_electric-coordinate.
```

For the bouquet physical fiber, (10) gives the leading physical gap

```text
4 c_H(a)/a + O_N(c_H(a) g_H/a),                         (19)
```

and for the adjacent strip the coefficient is 2sqrt(5) in place of 4.
If c_H is bounded below and g_H is sufficiently small, both provide a
positive lower bound of order 1/a. This is a fast ultraviolet energy, not a
finite continuum glueball mass. The uniform neighborhood statement provides
the same order with a neighborhood-dependent constant.

To use this mechanism in the reverse OS blocking theorem one must still
construct the actual reflection/time-covariant block map, identify its
reducing complement, and compare that complement's vacuum-subtracted
transfer-energy form to the constrained vertical energy. In a coupled
multi-block problem this also requires control of horizontal/vertical
cross terms, the coarse-dependent ground energy, and couplings between
blocks. The present proof supplies the physical single-block energy scale
and rules out the rare-diffusion-well argument as an obstruction to that
scale. It does not assume those remaining comparisons.

## 7. Independent controls and evidence scope

The analytic proof consists of (3)-(7), the invariant oscillator selection
rule, and the exact link-form calculations (8)-(12). Its conclusion holds
for every fixed N>=2; it is not inferred from a rank sweep or a truncated
character matrix. The companion SU(2) radial identity is an independent
normalization control: with K having eigenvalues exp(+-i theta), the class
transform f(theta)->sin(theta)f(theta) gives

```text
H_fib^bouquet = -(1/4) d^2/dtheta^2 -1/4 +8u(1-cos theta)
```

on (0,pi), with Dirichlet endpoints. Its near-zero half-line oscillator has
energies (4j+3)sqrt(u), matching d=3 in (1) and the physical gap 4sqrt(u).
Certified character-Jacobi enclosures are complementary finite-u controls;
they are not the proof of the asymptotic theorem or of any OS comparison.

The exact radial/character controls are in
[check_su2_physical_rotor.py](check_su2_physical_rotor.py), with saved output
[su2_physical_rotor_control.json](su2_physical_rotor_control.json) and the
additional [u=1000000 certificate](su2_rotor_1000000_certificate.json).
[replay_su2_rotor_certificates.py](replay_su2_rotor_certificates.py) checks
four fixed-u enclosures by exact integer Sturm signs and a tail Schur
comparison, with the numerical eigensolver disabled. Independent replay
passed and rejected a corrupted interval. The enclosures concern the full
untruncated SU(2) class-space operator at those four couplings; the separate
cutoff-convergence scan in the JSON is numerical evidence only.
