# The actual Wilson ground score on a complete localized source chart

5 September 2026. Analytic research continuation. The result is an
O(u^(-1)) relative Schur-loss estimate for physical class sources of the
actual two-adjacent-square Wilson block whose gradients lie in a fixed
rescaled neighborhood of the identity. For additive strips with a common
Gauss constraint the complete radial/pair source chart has an O(u^(-1/2))
relative estimate. Bounded radial and adjoint cutoff sources in
this class give an onto frame for the complete first physical fine-energy
window, including additive copies with one common Gauss constraint. The
constant does not grow with the number of those additive copies. The
theorem holds for every fixed SU(N), N>=2, with constants depending on N.

The measure is the exact joint quantum ground measure. The proof uses a
derivative-controlled expansion of that ground, not a classical conditional
measure or the ground of the constrained fiber. It neither restores the
refuted global Fisher bound nor identifies the selected source space with
an entire spectral window of the marginal operator. It does not by itself
exclude low Schur states descending from high retained energies.

## 1. Actual operator, coordinates and statement

Fix SU(N), N>=2, with <X,Y>=-2 ReTr(XY), d=N^2-1 and an orthonormal
Lie basis T_a. Set g=u^(-1/4). Constants and thresholds may depend on N;
no uniformity as N tends to infinity is claimed. For the explicit SU(2)
control use T_a=i sigma_a/2. The actual seven-edge two-square Hamiltonian is

```text
H(u)=-2(Delta_1+Delta_2)+sum_a L_1,a R_2,a
       +2u[v(U1)+v(U2)],       v(U)=N-ReTr U.             (1)
```

It is a uniformly elliptic operator on the smooth compact manifold G^2.
Its physical subspace consists of functions invariant under simultaneous
conjugation. Let Omega_g>0 be the normalized true ground, E_g its energy,
and h_g=H(u)-E_g. Positivity and uniqueness make Omega_g physical.

Use U=U1 U2, K0=U1. For U in the identity logarithm chart put

```text
X=log U=sqrt(2)g Q,       H=exp(X/2),
K0=H F,                  F=exp(g Z/sqrt(2)).              (2)
```

H in (2) denotes the group square root; H(u) in (1) is the operator. Define
the exact marginal and normalized conditional amplitude in the balanced
fiber coordinate F by

```text
mu_g(U)=integral |Omega_g(U,H F)|^2 dF,
phi_g(U,F)=Omega_g(U,H F)/sqrt(mu_g(U)),
rho_g(U,F)=phi_g(U,F)^2.                                 (3)
```

All measures dU,dF are Haar. The literal source map is J_g f=f(U)Omega_g,
with P_g=J_g J_g^* and Q_g=1-P_g. Thus P_g Omega_g=Omega_g exactly.
The exact marginal form is

```text
a_g[f]=(1/2) integral (grad f)^* C_uu(U) grad f dmu_g,
C_uu(U)=8I-Ad(U)-Ad(U)^*.                                (4)
```

Let I_g(U) be the intrinsic conditional Fisher matrix, including the actual
metric horizontal connection, as defined in Section 4. For each fixed R<infinity
there are constants C_(N,R),g_(N,R)>0 such that

```text
C_uu(U)^(1/2) I_g(U) C_uu(U)^(1/2) <= C_(N,R) I
whenever U=exp(sqrt(2)g Q), |Q|<=R, 0<g<g_(N,R).             (5)
```

The sharper local leading matrix in an orthonormal left coarse frame is

```text
I_g(exp(sqrt(2)g Q))
 =49/(72 sqrt(5)) ad_Q^* ad_Q+O_(N,R)(g).                (6)
```

The error is uniform on the fixed Q ball. Its leading radial null direction
is an actual cancellation. In that direction the exact matrix is O_(N,R)(g^2),
which improves the class-source estimate. It need not vanish identically
at nonzero g.

Let F_g be the operator of h_g restricted to the physical Q_g form domain.
For sources whose gradients vanish outside the ball in (5), the actual
Schur loss satisfies

```text
Sigma_g[f]=||F_g^(-1/2) Q_g h_g J_g f||^2
          <= C'_(N,R) g^4 a_g[f] for physical class sources. (7)
```

Interpret the cross vector first for smooth sources and then by form closure.
Equation (7) applies to every physical class source with such gradient
support, not just a single trial expectation. Without the local class
constraint, the same argument gives a relative O(g^2) estimate when the
applicable full complementary form has a floor of order g^(-2). Section 5
makes its complete-window frame scope precise.

## 2. Why the order-g operator term kills the true leading vacuum

Write j for the Haar density in exponential coordinates. The local map to
flat Lebesgue measure is

```text
Psi_g(Q,Z)=g^d sqrt(j(sqrt(2)g Q)j(g Z/sqrt(2)))
                  Omega_g(U,H F),       d=N^2-1.             (8)
```

The constants in (8) follow from the Jacobian factors (sqrt(2)g)^d and
(g/sqrt(2))^d. In these coordinates the scaled operator g^2 H(u) has a
Taylor expansion on smooth local functions,

```text
A_g=A_0+g A_1+g^2 A_2+...,
A_0=-(3/2)Delta_Q-(5/2)Delta_Z+(|Q|^2+|Z|^2)/2,
A_1=-7/(2 sqrt(2)) sum_a <[Q,T_a],grad_Z> partial_Qa.   (9)
```

Here is a direct normalization check of the first term. The exact global
based-coordinate metric has

```text
C_uu=8I-Ad U-Ad U^*,
C_Ku=4I-Ad U^*,             C_KK=4I,
b=C_Ku C_uu^(-1),          S=15 C_uu^(-1).              (10)
```

At the identity C_uu=6I and S=5I/2. The coarse square-root derivative has
right-trivialized velocity (I+Ad H)^(-1)E. In the balanced fiber frame the
exact residual horizontal velocity is

```text
r_U(E)=Ad(H)^(-1)[b(U)-(I+Ad H)^(-1)]E
      =(7/24)[X,E]+O(|X|^2)|E|.                         (11)
```

Indeed b=I/2+(ad X)/6+O(X^2), while (I+Ad H)^(-1)=I/2-(ad X)/8+O(X^2).
For unit Q-coordinate velocity the resulting Z velocity is
7g[Q,E]/(6 sqrt(2))+O(g^2). The leading coarse kinetic coefficient is 3/2,
so its cross term is exactly A_1 in (9). Its divergence vanishes at this
order: the coefficient is Z-independent and sum_a partial_Qa[Q,T_a]=0.
The vertical metric, magnetic potential and Haar density have no linear
term in this chart. For the potential this follows either by expanding
v(exp(gQ/sqrt(2))exp(+-gZ/sqrt(2))) or by the vanishing trace pairing of a
Lie bracket with its inputs. This checks (9) without assuming evenness of
every higher operator coefficient.

The normalized oscillator ground is

```text
Phi_0(Q,Z)=Phi_Q(Q)Phi_Z(Z),
Phi_Q proportional to exp(-|Q|^2/(2 sqrt(3))),
Phi_Z proportional to exp(-|Z|^2/(2 sqrt(5))).            (12)
```

It obeys A_1 Phi_0=0 exactly: contraction with partial_Q Phi_Q replaces
T_a by Q and gives [Q,Q]=0. Consequently both the order-g eigenvalue
coefficient and the order-g eigenvector correction vanish. This is the
specific cancellation required here. It concerns the actual joint ground;
no identification with the conditional fiber ground has been made.

## 3. A derivative-controlled conditional expansion

The following argument supplies the needed uniform derivatives and fiber
tails. Mere L2 convergence would not supply them.

For each fixed integers k,m, one can choose a local approximate ground to
arbitrarily high order,

```text
Phi_app,M=chi(gQ,gZ) sum_(j=0)^M g^j Phi_j(Q,Z),
Phi_1=0,       Phi_j=polynomial(Q,Z) Phi_0.              (13)
```

Use an invariant smooth cutoff supported in a fixed small original chart
and equal to one on a smaller chart. Solve each coefficient equation on
Phi_0-perp using A_0-e_0, after choosing the eigenvalue coefficient to remove
its Phi_0 component. The oscillator has a positive ground gap. Each forcing
is a polynomial times Phi_0, and inversion of the oscillator on its finitely
many Hermite components again gives a polynomial times Phi_0. Equivariance
preserves the physical constraint at every order. Equation (9) gives
Phi_1=0. This construction does not require all odd later terms to vanish.

Taylor's theorem and Gaussian decay show that the residual, in scaled L2,
is O(g^(M+1)); applying any fixed number of ordinary derivatives only costs
a fixed power of g. Derivatives of the cutoff act at fixed original distance
from the minimum, hence on a Gaussian tail which is smaller than every power
of g. The actual physical ground is simple and its scaled spectral distance
from the next physical level is bounded below, by the established compact
two-square oscillator localization. Thus the spectral theorem turns the
normalized residual into O(g^(M+1)) L2 error after choosing the positive
ground sign, and the approximate eigenvalue differs by the same order.

Here is why one may strengthen this to the particular derivative and tail
norms below. On the original fixed compact G^2, use ellipticity of the fixed
operator H_E. If e is the exact-minus-approximate ground error, its equation
has the form

```text
g^2 H_E e+(g^(-2)V_0-lambda_g)e=r_g,
V_0=2[v(U1)+v(U2)],       lambda_g=O(1).                 (14)
```

The usual local elliptic estimate follows by freezing the positive principal
matrix on finitely many coordinate balls, applying the Fourier estimate for
a constant positive quadratic symbol, and absorbing coefficient variation;
commuting derivatives and a partition of unity gives the global estimate

```text
||e||_(H^(s+2)) <= C_s (||H_E e||_(H^s)+||e||_L2).
```

Equation (14) then loses at most a fixed power of g at each two-derivative
step (the potential coefficient costs g^(-4)). Derivatives of V_0 are
bounded on the original compact manifold. Hence an arbitrarily high choice
of M in (13) makes the error O(g^L) in any prescribed finite original Sobolev
norm, for any prescribed L. No uniform-in-M estimate is asserted or needed.

Pullback to the scaled chart and multiplication by its smooth Haar factors
again lose only finitely many powers of g. Fiber weights |Z|^m cost at most
C g^(-m) on that chart. Sobolev embedding in the d coarse coordinates, at a finite order greater
than d/2 plus the required derivative order,
with values in fiber L2, now makes the error uniform for |Q|<=R. Outside the
fixed original fiber chart the approximate ground is zero; applying the
same argument before scaling bounds the exact ground and its required
derivatives there by any chosen power of g. This controls the omitted fiber
tail as well as the derivatives inside the chart. We need only finitely
many such norms, so one sufficiently large finite M proves all of them.

In particular, let phi_(0,g) be the normalized inverse-Haar-transform of
Phi_Z with the above fiber cutoff. It is independent of Q. Define the
coarse-rescaled, fiber-Haar-valued joint vector

```text
Xi_g(Q,F)=(sqrt(2)g)^(d/2) sqrt(j(sqrt(2)g Q))
                         Omega_g(U,H F).
```

The preceding construction, including the explicitly bounded polynomial
coefficients j>=2 in (13), yields

```text
Xi_g(Q,.)=Phi_Q(Q) phi_(0,g)+O_(N,R)(g^2),
partial_Q Xi_g=(partial_Q Phi_Q) phi_(0,g)+O_(N,R)(g^2).     (15)
```

These errors hold in fiber L2 and after one scaled fiber derivative g L_F,
with any fixed polynomial Z weight in the local chart and negligible
outside-fiber tails. The same statements hold for more coarse derivatives
when needed. Normalizing the cutoff phi_(0,g) changes it only by a quantity
smaller than every power of g.

For fixed R, min_(|Q|<=R) Phi_Q(Q)>0. Hence ||Xi_g(Q,.)|| is uniformly
bounded below there. The exact normalized fiber vector in (3) equals

```text
phi_g(Q,.)=Xi_g(Q,.)/||Xi_g(Q,.)||.
```

The derivative of this Hilbert-space normalization is the orthogonal
projection of partial_Q Xi_g onto phi_g-perp divided by ||Xi_g||. It cancels
the scalar derivative partial_Q Phi_Q in (15). Therefore

```text
||phi_g-phi_(0,g)||_L2F <= C_(N,R) g^2,
||partial_Q phi_g||_L2F <= C_(N,R) g^2,
||g L_F(phi_g-phi_(0,g))||_L2F <= C_(N,R) g^2.               (16)
```

The corresponding finite weighted estimates also hold. Only a lower bound
on the rescaled marginal norm on a fixed Q compactum was used. There is no
division by a pointwise lower bound for Omega_g, no global lower bound for
mu_g, and no assumption that an unbounded multiplier preserves L2 errors.

## 4. Exact score and its local leading matrix

In balanced Haar coordinates the horizontal derivative is

```text
D_E=partial_(U,E)+L_(r_U(E)),                            (17)
```

where (11) is constant in the fiber and consequently Haar-skew. The intrinsic
density score is

```text
s_E=partial_(U,E) log rho_g+
             div_F(rho_g r_U(E))/rho_g
    =2 D_E phi_g/phi_g.
```

Thus, without estimating the logarithmic derivative pointwise,

```text
(I_g)_(EF)=4 <D_E phi_g,D_F phi_g>_L2F.                 (18)
```

The equality uses positivity for its pointwise definition and integration
for its finite norm. The derivative is centered because phi_g is normalized
and L_r is Haar-skew. In flat fiber coordinates the latter becomes
v.grad_Z+(div_Z v)/2, so the half-density connection has not been omitted.

A physical unit coarse velocity has Q-coordinate size O(g^(-1)); (16)
therefore bounds its parameter derivative of phi_g by O_(N,R)(g). Formula (11)
gives fiber velocity r_U(E)=7 sqrt(2)g[Q,E]/24+O_(N,R)(g^2).
Under F=exp(g Z/sqrt(2)), its leading flat vector field is the constant
7[Q,E]/12, of zero flat divergence. Equations (12),(16) imply in fiber L2,
uniformly on the fixed Q ball,

```text
D_E phi_g
 =-7/(12 sqrt(5)) <[Q,E],Z> Phi_Z+O_(N,R)(g),               (19)
```

with the display interpreted through the fiber Haar transform and its
negligible cutoff tail. The first-order change of the fiber differential
and its half-density term contributes only O_(N,R)(g), as does the second-order
term in (11). The weighted estimate in Section 3 controls their polynomial
Z coefficients.

The probability |Phi_Z|^2 has covariance sqrt(5) I/2. Substitution into
(18) proves

```text
I_g(E,F)=49/(72 sqrt(5)) <[Q,E],[Q,F]>+O_(N,R)(g)|E||F|.
```

For SU(2), the adjoint metric bracket is the three-dimensional cross product
up to orientation, so ad_Q^* ad_Q=|Q|^2I-Q Q^*. This is the explicit
SU(2) specialization of (6). For general N the adjoint Gram is retained. Since
C_uu=6I+O_(N,R)(g^2), its weighted leading matrix is
49/(12 sqrt(5)) ad_Q^* ad_Q. Uniform boundedness proves (5).

For a direction E commuting with Q, a stronger estimate holds. The exact
operators Ad U and Ad H fix E, so (10)-(11) give

```text
r_U(E)=0,       C_uu E=6E,       when [Q,E]=0.           (19a)
```

The only conditional derivative in that direction is the parameter
derivative in (16). Passing from Q velocity to physical U velocity costs
O(g^(-1)), hence

```text
||D_E phi_g||<=C_(N,R) g |E|,       I_g(E,E)<=C_(N,R) g^2|E|^2. (19b)
```

If a coarse function is conjugation-invariant, its Haar gradient is fixed
by Ad U: differentiate f(VUV^(-1))=f(U). In the injective logarithm chart
this means [Q,grad f]=0. The same is true of C_uu grad f by (19a).
Thus the stronger directional estimate applies exactly to physical
single-block source gradients. This centralizer and class-versus-common-
Gauss distinction already occurs in the established BO commutator
calculation. The new input here is the O(g^2) derivative remainder for the
normalized conditional amplitude of the TRUE joint ground in (16).

The center obstruction lies at U=-I, which leaves every fixed rescaled Q
ball as g tends to zero. Equations (5)-(6) make no assertion there. They
prove the local score premise in the actual low-energy localization region.

## 5. Schur loss and the complete selected physical source frame

The exact ground transform and intrinsic score give the cross vector

```text
T_g f=Q_g h_g J_g f=-(1/2) Omega_g s^* C_uu grad f.
```

For a smooth source with gradient supported as in (5), conditional integration
and (5) give

```text
||T_g f||^2
 =(1/4) integral (grad f)^* C_uu I_g C_uu grad f dmu_g
 <=(C_(N,R)/2) a_g[f].                                    (20)
```

All such physical cross vectors are orthogonal to the exact vacuum. The
established full physical strip gap is at least sqrt(3)/g^2 for small g.
Since Q_g Omega_g=0, restriction gives F_g>=sqrt(3)/g^2. Consequently

```text
Sigma_g[f] <= C_(N,R) g^2/(2 sqrt(3)) a_g[f]       (21)
```

on the selected source space before using the class cancellation. For
physical single-block class sources, apply (19a)-(19b) inside (20) instead.
This improves (21) to

```text
Sigma_g[f] <= C_(N,R) g^4 a_g[f],
(1-C_(N,R) g^4)a_g[f] <= k0_g[f] <= a_g[f].                 (21a)
```

Constants have been enlarged here. This is (7). The bound is for fast
energy through F_g^(-1/2) T_g; it is not inferred from an L2 projection
angle.

Here is a complete fine-window application. Choose a fixed large radius R
and an invariant smooth cutoff chi(Q) supported in |Q|<R. Use the centered
radial source chi(Q)(|Q|^2-d sqrt(3)/2), extended by zero in the original
coarse chart and then centered in the exact marginal. Its gradient is
supported inside (5). Its normalized harmonic overlap with the first radial
oscillator is nonzero for R sufficiently large. Bounded-cutoff convergence
of the true ground and the complete simple first physical eigenvector
preserves that nonzero overlap at small g. Together with the constant
vacuum source, it is therefore an onto frame for the entire physical fine
spectral window below any scaled threshold strictly between
2 sqrt(3) and sqrt(3)+sqrt(5). This follows from the established spectral
ordering, not from a lower bound alone in an unknown-dimensional space.

The source space just described is a selected two-dimensional chart. It
need not equal the first spectral window of the marginal A_g=J_g^*h_gJ_g.
The actual strip frequencies differ, so this first fine window has one
excited singlet. In the additive equal-frequency bouquet there are three
degree-two physical singlets at the same first fine energy; a single
radial product-holonomy source would not be an onto chart for that triple.

## 6. Uniform additive copies with a common Gauss constraint

Take identical additive actual strips, with the single simultaneous SU(N)
action on every strip. This includes neither interstrip plaquette terms nor
ambient boundary couplings. Use the exact product true vacuum and literal
product source projection. The established full inverse-energy literal
theorem gives, uniformly in the copy count M,

```text
h_M >= c_g (I-P_M),       c_g >= c_* g^(-2)>0            (22)
```

for small g, including the common invariant subspace. This is the full-form
bound; using only a purported tensor product of conditional fiber gaps here
would not justify the statement. The common-Gauss theorem classifies the
complete first fine window: vacuum, a single radial excitation in any one
strip, and the unique singlet made from two slow-adjoint excitations in two
different strips, below t_g=min(b_g,alpha_g+beta_g,3alpha_g).

Choose, in addition to the local radial cutoff profile, the equivariant
adjoint profiles chi(Q)Q_a, with exact marginal normalization. Form the
radial single-copy and adjoint-pair singlet source span. Each differentiated
local profile has support inside the same fixed Q ball. Exact support
orthogonality and equivariance give onto projected fine-window frame weights

```text
1, |z_r|^2, |z_A|^4,                                  (23)
```

where the nonzero local cutoff overlaps z_r,z_A have positive lower bounds
for small g. These weights have no copy-count loss, even for arbitrary
superpositions of the pair singlets. This is the bounded-cutoff frame
argument in the companion local-gradient note, Section 6.

The product conditional density has centered, independent local scores.
Consequently the squared norm of the sum of the local cross vectors is
the sum of their squared norms after conditioning on all coarse variables.
Equation (20) and (22) therefore give, on the whole selected common-Gauss
source chart,

```text
Sigma_M[f] <= (C_(N,R)/(2c_g)) a_M[f]
            <= (C_(N,R)/(2c_*)) g^2 a_M[f].                 (24)
```

The O(g^4) single-class improvement cannot be inferred for these pair
sources from the common Gauss law alone. That law says only
sum_i [Q_i,grad_i f]=0. The independent fiber vectors Z_i in the leading
scores keep the corresponding nonnegative variances separate; they do not
cancel by this sum. The O(g^2) conclusion (24) retains them. For example
the leading pair profile Q_1.Q_2 has [Q_1,grad_1 f]=[Q_1,Q_2] and the
opposite bracket in the other block, which are separately nonzero.

There is no indicator that every coarse coordinate is good and no union
bound over vacuum coordinates. Only the support of the gradient in its own
coordinate matters. For countably many copies, finite-support source
coefficient truncations converge in the marginal form norm. The centered
local cross vectors converge in L2 by (20); (22) bounds the inverse fast
form uniformly. These observations extend (23)-(24) to the closed selected
source chart in the vacuum incomplete tensor product. They do not assume
that a global infinite product dressing is a unitary on an unrelated Hilbert
representation.

## 7. Exact scope and next actual obligation

Equations (5),(21a),(24) prove an actual Wilson local score premise and its
relative O(u^(-1)) single-strip class-source and O(u^(-1/2)) common-Gauss
Schur consequences on complete selected source charts.
They replace the false global Fisher-growth proposal by a controlled local
statement, with the true joint vacuum, correct horizontal metric and actual
full-vacuum fast form in the same argument. Arbitrary source superpositions
in that chart are included, and the additive common-Gauss statement is
uniform in volume.

The statement does not control the full Schur gap merely because the chart
is onto a fine window. The infinite retained complement can contain high
marginal-energy sources whose mixing must still be controlled, or a complete
endpoint spectral comparison must incorporate them. Interacting interfaces
also destroy the exact product conditional covariance used in (24). The
next scale obligation is to retain an energy-localized score or memory
estimate when actual neighboring blocks are coupled, with a complete
spectral comparison and the physical clock accounted for. No continuum
mass gap, all-scale trajectory, or OS reconstruction follows from this
single finite-geometry/additive theorem alone.

## Provenance and finite control boundary

The actual link metric and its first balanced expansion are established in
[G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md](G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md),
Sections 1 and 3-4. The complete physical oscillator ordering and compact
localization are in [G19_WILSON_TWO_SQUARE_PHYSICAL_SHELLS_20260905.md](G19_WILSON_TWO_SQUARE_PHYSICAL_SHELLS_20260905.md),
Sections 2-4. The exact score identity is in
[G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md](G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md), Sections 1-3. The literal/common
fast bounds are in the current literal notes, including the separately
provenanced inverse-energy addendum. The companion selected-profile and
countable-support argument is
[local gradient source theorem](G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md).

The new analytic work here is the high-derivative true-ground construction,
its normalized conditional consequence, the resulting actual local Fisher
matrix and the application to the complete selected source chart. The
companion exact SU(2) algebra checker verifies the 7/24 residual coefficient,
the vanishing order-g Gaussian forcing, the leading Fisher normalization
and its radial cancellation. Those finite identities do not replace the
compact elliptic, quasimode, domain or countable arguments in the proof.

## Canonical source provenance and reproduction

This is the canonical copy of the independently reviewed 5 September
derivation [TRUE_GROUND_LOCALIZED_WILSON_SCORE.md](../../runs/wilson_endpoint_local_score_2026-09-05/TRUE_GROUND_LOCALIZED_WILSON_SCORE.md),
whose original SHA256 is `92c90d38b44975a75fe5f69f483ef1fea2190385e345dc33d575d6ac05848f55`. The original proof bytes are
preserved; this copy adjusts only stage metadata and relative links,
then appends this explicitly separate provenance and follow-up record.

The [reproduction run](../../runs/wilson_endpoint_local_score_2026-09-05/README.md) preserves the analytic
sources and the precisely scoped finite controls:

- [check_localized_true_ground_score.py](../../runs/wilson_endpoint_local_score_2026-09-05/check_localized_true_ground_score.py)
- [localized_true_ground_score_controls.json](../../runs/wilson_endpoint_local_score_2026-09-05/localized_true_ground_score_controls.json)
- [INDEPENDENT_LOCAL_SCORE_AUDIT.md](../../runs/wilson_endpoint_local_score_2026-09-05/INDEPENDENT_LOCAL_SCORE_AUDIT.md)

The [complete endpoint theorem](G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md)
provides a separate complete additive spectral comparison including
all high retained directions. It does not promote the selected
static Schur estimate here to a bound on every retained source.
