# Wilson strip reduction and the first two-strip physical splitting

5 September 2026. Outputs-only derivation for the finite two-square
strip with its actual shared-link electric form. The result identifies
the normalized vertical ground derivative, projected coarse energy,
and the first off-diagonal term. It is not an RG iteration or an
identification with the reducing complement of an OS-history map.

The metric and conventions are those in
[WILSON_BLOCK_CONDITIONAL_SCORE.md](WILSON_BLOCK_CONDITIONAL_SCORE.md),
Section 6.1. The required uniform vertical oscillator isolation is
proved in [PHYSICAL_WILSON_FIBER_FAST_GAP.md](PHYSICAL_WILSON_FIBER_FAST_GAP.md).

## 1. Exact horizontal and vertical decomposition

The electric operator is H_E=(1/2)sum_edges C2. For U=U1U2 and K0=U1,
write A=Ad(U). In right-trivialized tangent coordinates its link
co-metric is

```text
C = [[C_uu,C_uk],[C_ku,4I]],
C_uu=8I-A-A*,  C_uk=4I-A,  C_ku=4I-A*,
S=4I-C_ku C_uu^-1 C_uk=15 C_uu^-1.
```

The fine measure after tree gauge is exactly dU dK0. Completing the
quadratic form gives, with the factor 1/2 retained,

```text
E_E(f)= (1/2) integral [
 <grad_U f+C_uu^-1 C_uk grad_K0 f,
  C_uu(grad_U f+C_uu^-1 C_uk grad_K0 f)>
 +<grad_K0 f,S grad_K0 f>] dU dK0.
```

Thus a coarse tangent b lifts to the fine tangent
(b,C_ku C_uu^-1 b). These fiber translations are Haar-divergence-free.
This is an exact form identity; no mixed term has been bounded or
discarded, and no arbitrary coarse metric rescaling is being used.

Set u=g^-4 with g>0, alpha=sqrt(2)g, and use the balanced coordinates

```text
U=exp(alpha Q)=H^2,  H=exp(alpha Q/2),
K0=H F,  F=exp(g Z/sqrt(2)).
```

The magnetic term, after adding 4uN, splits exactly into

```text
V_coarse(U)=4u[N-Tr(Re H)],
V_vertical(U,F)=4u Tr[(Re H)(I-Re F)].
```

For fixed U let e0(U) and phi_U(F)>0 be the lowest eigenvalue and
normalized real ground function of the intrinsic vertical operator

```text
H_vertical(U)=-(1/2) sum_ab S(U)^ab L_a L_b
              +4u Tr[(Re H)(I-Re F)]
```

on L2(dF). The translation by H is unitary; Ad(H) commutes with S(U),
so the displayed kinetic coefficient is unchanged. The positive
ground is simple. Throughout, q ranges over a fixed compact subset
of the Lie algebra and g tends to zero.

## 2. The balanced-coordinate ground derivative starts at g squared

Use <X,Y>=-2 ReTr(XY), d=N^2-1, C_F=(N^2-1)/(2N). Transform the
fiber to the rescaled Z coordinate and multiply by the square root
of its full Haar density rho_g(Z)=dF/dZ, including the coordinate
scale and normalized-Haar constant. Thus locally
W_g phi(Z)=rho_g(Z)^(1/2)phi(exp(gZ/sqrt(2))) is an isometry into
Lebesgue L2. The map W_g has no Q dependence. This is the ground
normalized in conditional Haar measure, not a square root of the
classical Wilson conditional probability density.
The exponentially localized ground is then compared with

```text
h0=-(5/2)Delta_Z+|Z|^2/2,
e00=d sqrt(5)/2,
a=1/sqrt(5),
phi0(Z)=(a/pi)^(d/4) exp(-a|Z|^2/2).
```

The rescaled vertical operator has the expansion

```text
g^2 H_vertical(Q)=h0+g^2[h2(0)+h2,Q]+O(g^3),
h2,Q=-(5/6)sum_ab(ad Q)^2_ab partial_a partial_b
      -(1/4)Tr(Q^2 Z^2).
```

Here O(g^3) means the local differential-coefficient expansion on
Gaussian polynomial vectors; the resulting ground and derivative
statements below are norm statements after localization. The
Q-independent operator h2(0) includes the Haar, group metric and
pure-fiber quartic corrections. It cancels from the Q-dependent
energy difference and derivative. There is no order-g term.

Indeed,

```text
S(U)=(5/2)I+(5g^2/6)(ad Q)^2+O(g^4),
Re H=I+g^2 Q^2/4+O(g^4),
Re F=I+g^2 Z^2/4+O(g^4).
```

The exponential-coordinate Haar factor has no Q dependence. The
leading isotropic Laplacian has no odd first-coordinate correction;
its order-g terms cancel by skew-adjointness of the Lie brackets.

Gaussian averaging gives

```text
<phi0,partial_a partial_b phi0>=-a delta_ab/2,
Tr_ad((ad Q)^2)=-N|Q|^2,
E_(phi0^2)[Z^2]=-C_F I/(2a).
```

Consequently the actual vertical zero-point energy shift is

```text
e0(Q)-e0(0)
 =-sqrt(5)[N/12+C_F/16]|Q|^2+o(1).                 (1)
```

This is an electric-coordinate energy, of order one. Relative to
the leading energy scale g^-2 it is an order-g^2 correction.

The Q-dependent wavefunction coefficient is also explicit. Define
the quadratic polynomial

```text
B_Q(Z)=-(1/6)<Z,(ad Q)^2 Z>-(1/4)Tr(Q^2 Z^2).
```

The centered polynomial B_Q-E_(phi0^2)B_Q belongs to oscillator level
two, whose gap is 2sqrt(5). With positive real normalization,

```text
phi_Q-phi_(Q=0)
 =-(g^2/(2sqrt(5)))[B_Q-E_(phi0^2)B_Q] phi0+o(g^2),
partial_E phi_Q=O(g^2).                              (2)
```

Both statements hold uniformly on the chosen compact Q set, including
the indicated first derivative. The derivative in (2) is in the
balanced trivialization F=H^-1K0. It is not yet the intrinsic
horizontal derivative.

To justify these coefficients as asymptotics, multiply the oscillator
ground and polynomial correctors by an exponential-coordinate cutoff
whose unscaled radius tends to zero more slowly than g. The cutoff
tails and their differentiated terms are exponentially small.
Taylor expansion on their support gives an L2 residual of the next
power of g. The Q-independent second corrector is obtained by the
same inversion on finitely many Hermite levels. Higher correctors can
be constructed before taking a fixed number of Q derivatives. The
uniform isolated vertical ground and its order-g^-2 gap, proved in
the fast-rotor note, turn these residuals into norm estimates by the
ground Riesz projection. Differentiating that projection, with the
higher residual order, proves the uniform parameter derivative in
(2). This argument uses the unique global minimum and excludes the
rare higher wells; it does not perturb a quartic Taylor polynomial
as a globally bounded-below Hamiltonian.

## 3. The intrinsic derivative remains first order

The exact horizontal lift in the balanced chart has leading fiber
velocity

```text
D_E=partial_E+v_E.grad_Z,
v_E=(7g/(6sqrt(2)))[Q,E]+O(g^2).
```

In Haar fiber space the vertical part is skew-adjoint. In coordinates
div_(rho_g dZ)(v_E)=0. Therefore the exact transformed connection is

```text
W_g D_E W_g^-1
 =partial_E+v_E.grad_Z+(1/2)div_Z(v_E).
```

The leading constant-Z translation has zero divergence; its half
divergence does not contribute to the first coefficient below.
Using (2),

```text
D_E phi_Q
 =-(7g/(6sqrt(10)))<[Q,E],Z> phi0+O(g^2),
||D_E phi_Q||^2
 =(49g^2/(144sqrt(5)))||[Q,E]||^2+o(g^2).             (3)
```

The ground derivative therefore has exactly the same order-g
geometric obstruction as the conditional score. Changing from a
classical conditional density to the true quantum ground does not
alone remove it. Its leading Gaussian width and coefficient are
different, and have been computed from the actual vertical kinetic
factor 5/4.

For positive real normalized phi_Q, the Berry connection is zero:
<phi_Q,D_E phi_Q>=0. The normalization derivative vanishes and the
vertical Haar-divergence-free part is skew-adjoint on real functions.

## 4. The actual projected coarse form and Born-Huang energy

Project onto the fiber ground by f(U,F)=psi(U)phi_U(F). Completing
the exact form in Section 1 then gives

```text
E_projected(psi)
 =E_coarse(psi)
   +integral [V_coarse(U)+e0(U)+Phi_BH(U)] |psi(U)|^2 dU,
Phi_BH=(1/2) sum_ab C_uu^ab <D_a phi_U,D_b phi_U>.
```

There is no Berry term for this positive ground. This is the exact
compression to the direct-integral fiber-ground space; it is not
claimed that this space reduces the full Hamiltonian.

In q coordinates the electric coarse co-metric, including H_E's
factor 1/2, expands as

```text
A_q=(3/(2g^2))I-(3/4)(ad Q)^2+O(g^2).                (4)
```

For example, this follows by writing the right-trivialized derivative
of exp(alpha Q) as alpha dexp_(alpha Q) and using
dexp^-1=I-(alpha/2)ad Q+(alpha^2/12)(ad Q)^2+... .
The leading coefficient in (4), together with (3) and
sum_a||[Q,T_a]||^2=N|Q|^2, yields

```text
Phi_BH(Q)=(49N/(96sqrt(5)))|Q|^2+o(1).               (5)
```

Combining the actual vertical zero-point shift (1) with (5) gives

```text
e0(Q)-e0(0)+Phi_BH(Q)
 =sqrt(5)(5-2N^2)/(160N) |Q|^2+o(1).                (6)
```

The near cancellation in (6) uses both the vertical metric correction
and the geometric ground derivative; neither may be dropped. This
coefficient is not a mass-gap claim by itself. The coarse magnetic
scalar also has its actual expansion

```text
V_coarse(Q)=|Q|^2/(2g^2)-Tr Q^4/24+O(g^2).
```

The measure in the projected coarse form is the Haar pullback,
j(alpha Q)dq, up to a constant. Its logarithm is
-N g^2|Q|^2/12+O(g^4). Flattening that measure adds a Q-independent
order-one scalar -Nd/8 to the leading kinetic operator; it does not
alter the quadratic coefficient in (6). The metric correction (4)
is separate. For a class function psi(Q), [Q,grad psi]=0, so its
displayed ad(Q)^2 correction annihilates the gradient. Retaining the
actual form and Haar measure makes all these normalizations explicit.

## 5. The first off-diagonal term and the full physical cancellation

Let P0 be projection onto the fixed leading fiber Gaussian phi0.
Write the complete locally rescaled operator, after subtracting an
irrelevant constant, as

```text
g^2 H=h_coarse,0+h0+g h1+O(g^2),
h_coarse,0=-(3/2)Delta_Q+|Q|^2/2,
h1=-(7/(2sqrt(2))) sum_a
          <[Q,T_a],grad_Z> partial_(q_a).             (7)
```

The only first-order term comes from the horizontal/vertical
connection. The coordinate divergence sum is zero because
sum_a partial_(q_a)[Q,T_a]=sum_a[T_a,T_a]=0. The Wilson potential,
isotropic leading fiber Laplacian and Haar factors contribute no
other order-g term.

On a fiber-ground vector, (7) gives

```text
h1[psi(Q)phi0(Z)]
 =(7/(2sqrt(10)))<[Q,grad_Q psi],Z> phi0.              (8)
```

For the actual single coarse holonomy, physical slow functions are
class functions; their gradients commute with Q. Thus

```text
h1 P0=0 on physical single-coarse slow functions.     (9)
```

This is stronger than a norm bound. The leading positive Born-Huang
scalar (5) survives, but the first off-diagonal coupling vanishes on
this physical slow space.

In fact the cancellation holds on the entire jointly invariant
two-variable domain, without factorization. Write
G_Q=[Q,grad_Q], G_Z=[Z,grad_Z]. The physical Gauss identity is
(G_Q+G_Z)F=0, while h1 is proportional to div_Z G_Q. In an
orthonormal compact-Lie basis the structure constants f_bcd are
totally antisymmetric. Therefore

```text
div_Z G_Z F
 =sum_bcd f_bcd [delta_bc partial_d F
                  +Z_c partial_b partial_d F]=0.
```

The first term repeats antisymmetric indices; the second contracts
antisymmetric b,d with commuting derivatives. Hence h1F=0 for every
smooth jointly Ad-invariant F(Q,Z).

### 5.1. An exact symmetry removes all odd physical Taylor coefficients

This first-order identity has a group-level explanation. On physical
functions the total Gauss generator is
G_a=L1_a+L2_a-R1_a-R2_a=0. Thus the two shared-edge derivatives
D_a=L1_a-R2_a and D'_a=R1_a-L2_a agree when applied to such a
function. Simultaneous face inversion I:(U1,U2)->(U1^-1,U2^-1)
exchanges D_a with -D'_a and preserves the individual Casimirs,
Haar measure and ReTr potential. It therefore preserves the physical
closed quadratic form and commutes with its self-adjoint operator.
This argument uses equality of form norms and needs no unproved
commutation of an individual derivative with the physical projection.

Let Phi_g(Q,Z)=(H F,F^-1 H) be the balanced chart. Direct multiplication
gives

```text
Phi_-g(Q,Z)=(H^-1 F^-1,F H^-1)
           =Conj_F[I Phi_g(Q,Z)].
```

For physical functions the final simultaneous conjugation has no
effect, even though F depends on the point. The Haar pullback density
j(alpha Q)j(gZ/sqrt(2)), including its absolute scale factor, is even
in g. Consequently the coordinate half-density pullbacks obey
W_-g=W_g I^* on the physical domain. With u=g^-4 fixed under sign
change, this proves

```text
H_pulled(-g)=W_g I^* H I^* W_g^-1=H_pulled(g)
```

on the physical local coordinate domain. This is equality of the
pulled-back physical family, not merely a parity unitary equivalence
of two unrelated operators. Every odd local Taylor coefficient of
the complete physical operator therefore vanishes. Separate
coordinate-dependent vertical and horizontal pieces need not share
that property individually.

### 5.2. What this does and does not give for elimination

For comparison, whenever the excited-complement resolvent exists at
an energy parameter E, the leading Feshbach correction would be

```text
-g^2 P0 h1 Q0 [Q0(h_coarse,0+h0-E)Q0]^-1 Q0 h1 P0,
Q0=I-P0.                                             (10)
```

It is zero on the space in (9). No adiabatic replacement of that
resolvent by just a fiber gap is used. The coarse and fiber oscillator
frequencies are both of order one in the rescaled operator, so such
a replacement would require another approximation theorem. The
resolvent is asserted only in an admitted spectral region, not on
the entire unbounded coarse spectrum.

The remaining physical two-face off-diagonal terms start at
order g^2 in g^2H. After retaining the actual projected metric,
zero-point energy and Born-Huang scalar, a higher comparison can
therefore begin with a squared order-g^2 coupling in a spectrally
separated low-energy region. This is a local mechanism for an order-g^4
error budget; it is not yet a uniform multi-block theorem.

In particular, for several coarse holonomies the Gauss identity is
only sum_j[Q_j,grad_j psi]=0. The first coupling instead contains
sum_j<[Q_j,grad_j psi],Z_j>, which need not vanish. The explicit
two-coarse example in the score note survives here as well. A genuine
RG construction must either preserve a stronger cancellation or
control and renormalize these inter-block terms.

## 6. Two actual strips: an exact on-shell angular correction

Take two edge-disjoint copies of the actual bent strip, sharing only
their base vertex. A concrete spatial cubic embedding uses the two
positive-octant squares with direction pairs (e3,e1), (e2,e3), and
their two negative-octant copies. Each pair shares its e3 or -e3
edge. Within the positive strip the six vertices are
0,e3,e1,e1+e3,e2,e2+e3; the negative strip has their negatives.
The two strips share no other vertex and no edge. The graph has
14 edges, 11 vertices and four independent face holonomies.

Its tree-gauge Haar space is L2(G^4), and the physical constraint is
simultaneous conjugation of all four based holonomies. The actual
Hamiltonian is the sum of the two strip Hamiltonians, with no added
interaction or kinetic approximation. Write Q_i,Z_i, i=1,2 for their
balanced coarse and fiber variables. On slow functions psi(Q1,Q2),
only the total condition L1 psi+L2 psi=0 is imposed, where
L_i=[Q_i,grad_Qi]. It does not force either term to vanish.

The leading slow oscillator is

```text
H_c,0=sum_i[-(3/2)Delta_Qi+|Q_i|^2/2].
```

Each component of L_i commutes with H_c,0, because it is an
infinitesimal orthogonal rotation of that isotropic oscillator.
Let psi belong to one fixed coarse-energy eigenspace. Acting on
the two fiber ground functions, the first coupling is exactly

```text
h1[psi phi0(Z1)phi0(Z2)]
 =(7/(2sqrt(10))) sum_i <Z_i,L_i psi> phi0(Z1)phi0(Z2).
```

It preserves the coarse energy and raises the total fiber energy
by precisely one quantum sqrt(5). Hence the on-shell complementary
resolvent is exactly multiplication by 1/sqrt(5) on this image.
This is not replacement of an arbitrary resolvent by a fiber-gap
bound. On a fixed finite coarse-energy range the oscillator inverse
is well-defined away from the chosen eigenspace: an equality
m sqrt(3)+k sqrt(5)=n sqrt(3) with k>0 would contradict the
irrationality of sqrt(5/3). No uniform inverse bound over the entire
unbounded coarse spectrum is claimed.

Gaussian orthogonality between fiber coordinates and between the
two fibers gives the exact second-order self-energy form

```text
-g^2 <h1 psi phi0, R h1 psi phi0>
 =-(49g^2/80) sum_i ||L_i psi||^2.                    (11)
```

The actual direct coarse metric correction in (4) contributes
+(3g^2/4) sum_i||L_i psi||^2 to g^2H. Therefore their sum is

```text
+(11g^2/80) sum_i ||L_i psi||^2.                      (12)
```

This is a nonzero, positive angular contribution to the effective
coarse kinetic form. It coexists with the scalar (6), magnetic
quartics and Haar corrections; it is not the entire second-order
effective Hamiltonian. Its derivation applies to the on-shell
finite-energy matrices, with no uncontrolled time-scale separation.

The physical witness psi proportional to
(Q1.Q2) exp[-(|Q1|^2+|Q2|^2)/(2sqrt(3))] lies at coarse Hermite
degree two and obeys only the total Gauss condition. For its unit
normalization,

```text
sum_i||L_i psi||^2=2N,
angular correction = (11N/40)g^2.
```

Indeed the two independent coarse Gaussian variances are sqrt(3)/2.
The squared norm of Q1.Q2 is 3d/4, whereas
E||[Q1,Q2]||^2=(3/4)Nd; the two angular derivatives have opposite
sign and equal squared norms. This explicitly exhibits a surviving
physical multi-holonomy correction after the geometric cancellation.

## 7. An actual first-shell splitting on this finite graph

The first physical harmonic excitation cluster for the two-strip
graph has rank three. Its leading eigenvectors are the radial
excitation R1 in Q1, the radial excitation R2 in Q2, and the
bilinear excitation M=Q1.Q2, all multiplied by the four ground
Gaussians. All have excitation energy 2sqrt(3) in g^2H. There is
no degree-one diagonal-adjoint singlet. The next possible physical
cluster has energy sqrt(3)+sqrt(5), so its fixed harmonic separation
is sqrt(5)-sqrt(3)>0.

Put

```text
c_N=sqrt(5)(5-2N^2)/(160N),
A_common=2sqrt(3)c_N=sqrt(15)(5-2N^2)/(80N),
k_N=(2N^2-3)/[4N(N^2+1)].
```

The common scalar correction (6) changes each of the three gap
coefficients by A_common. To compute the magnetic quartic, isotropic
angular averaging gives

```text
average_angle Tr Q^4=k_N |Q|^4.
```

For completeness, the Gaussian Wick contraction is
sum_ab Tr(Ta^2 Tb^2+Ta Tb Ta Tb+Ta Tb^2 Ta)
=d(2N^2-3)/(4N). Division by d(d+2), with d+2=N^2+1,
gives k_N. The same angular average applies to a radial state.
For the bilinear state each reduced one-strip density is the
uniform adjoint degree-one density, so its scalar expectation has
that angular average as well.

The exact Gaussian moment changes from the ground are

```text
Delta_R sum_i E|Q_i|^2 = Delta_M sum_i E|Q_i|^2=2sqrt(3),
Delta_R sum_i E|Q_i|^4 =9(d+2),
Delta_M sum_i E|Q_i|^4 =6(d+2).
```

The angular form in (12) vanishes on R1,R2 and equals 2N on M.
Consequently the second-order gap matrix, after subtracting the
ground correction, is diagonal in {R1,R2,M}, with entries

```text
delta_R=A_common-3(2N^2-3)/(32N),
delta_M=A_common-(2N^2-3)/(16N)+11N/40,

delta_M-delta_R=(54N^2-15)/(160N)>0.                   (13)
```

No scalar has been inferred from the angular term alone. The
Q-independent fiber and Haar scalars cancel in the gap difference;
the Q-dependent scalar, actual quartic and angular term are all
included above. Radial-to-radial cross entries vanish because the
strip operators are additive and the other factor has zero ground
overlap. Radial-to-bilinear entries vanish by the independent strip
color representations (equivalently the relevant odd Gaussian
factor). The first-order self-energy vanishes on each radial state.

### 7.1. From coefficients to actual finite-graph eigenvalues

The complete four-holonomy operator has a unique global potential
minimum at (I,I,I,I) and a uniformly elliptic link form. Global
compact localization and min-max, on the physical subspace, give
the harmonic limit and the rank-three first cluster. Only an
o(sqrt(u)) leading error is needed for this count; the single-strip
inversion cancellation is not assumed for this globally invariant
two-strip space.

Here is the higher-order step needed to turn (13) into an actual
order-one splitting. Work with the Haar half-density pullback of
g^2H in a small balanced coordinate chart:

```text
g^2H=h_0+g h1+g^2 h2+O(g^3).
```

All coefficients through this order are polynomial differential
operators on oscillator Gaussian vectors. Choose one normalized
leading vector w in the first rank-three physical eigenspace P_E.
The first corrector is

```text
w1=-Q_E(h_0-E)^-1 Q_E h1 w,
Q_E=I-P_E.
```

On its nonzero image the inverse is the exact 1/sqrt(5) already
computed. The solvability condition for a second corrector is

```text
P_E[h2-h1 Q_E(h_0-E)^-1 Q_E h1]P_E w=kappa w.
```

Its matrix is the common ground correction plus (13). After
choosing R1,R2,M as the corresponding eigenvectors, solve for w2
on the orthogonal complement. This requires only finitely many
Hermite levels, since polynomial differential operators preserve
finite Hermite expansions. Every nonzero denominator is separated
from zero on this finite set; no infinite-energy inverse estimate
is used. The corrections remain physical because the actual
Taylor operators and oscillator inverse commute with simultaneous
Ad. The ground is treated similarly, with h1 annihilating its
leading Gaussian.

Multiply w+g w1+g^2 w2 by a smooth physical cutoff in a fixed small
unscaled coordinate chart and pull it back to the group. The cutoff
lies at rescaled distance of order 1/g, so differentiated Gaussian
tails are exponentially small. Taylor remainder estimates on
Gaussian polynomial vectors give an L2 residual O_N(g^3) for
g^2H at the approximate eigenvalue E+g^2 kappa. The same estimate
holds for the corrected ground. The leading harmonic spectral
count prevents additional eigenvalues from entering this cluster.
The quasimode spectral theorem, followed by orthonormalization of
the finite trial family, therefore gives the actual eigenvalue
errors O_N(g^3) in g^2H, hence O_N(g)=O_N(u^-1/4) in H.

In particular the actual first physical gap and next singlet obey

```text
gap_radial(u)=2sqrt(3)sqrt(u)+delta_R+O_N(u^-1/4),
gap_mixed(u)=2sqrt(3)sqrt(u)+delta_M+O_N(u^-1/4),
gap_mixed-gap_radial
 =(54N^2-15)/(160N)+O_N(u^-1/4).                       (14)
```

For sufficiently large u the first excitation is the radial
doublet, and the mixed singlet lies strictly above it. The doublet
is exactly degenerate for the two identical strips: the true
single-strip physical radial excitation can be placed in either
factor, with the true ground in the other. Both product vectors
are physical eigenvectors with exactly the same energy. The
rank-three count and (13) identify them as the lowest pair and
exclude additional low states. No hopping is created between
disjoint strip Hamiltonians by imposing the common Gauss condition.

This is a genuine finite-graph spectral selection result beyond a
formal score estimate. Its order-one electric-coordinate splitting
is relative order g^2 compared with the leading g^-2 excitation
energy. The graph has four faces and no boundary-crossing
interactions. The theorem does not provide volume-independent
multi-block errors, an RG trajectory, an OS complement
identification, or a continuum mass.

## 8. Independent audit and scope

The fast-rotor proof's IMS error is h^2/r^2=h^(3/2) at r=h^(1/4).
Its codimension lower-bound argument and finite Gaussian trial upper
bound give the stated O(h^(3/2)) first eigenvalue errors. There is no
adjoint singlet at oscillator degree one for a simple Lie algebra,
and the radial degree-two polynomial supplies the first invariant
excitation. The global potential minimum at I excludes every rare
secondary center well from this low physical energy scale. The
coarse-neighborhood result correctly uses the full anisotropic gap
and only an o(sqrt(u)) error; it does not incorrectly double that
gap at every noncentral coarse background. These arguments audit
correctly under the stated fixed-group hypotheses.

The direct-integral ground projection used here is a configuration
fiber projection. It is not identified with the OS-history blocking
isometry. An exact OS map can retain more histories than a time-zero
coarse coordinate, and its reducing range may even be the full fine
space. A comparison to its actual reducing complement, the generated
history interaction, and a multi-scale energy estimate remains
necessary. No continuum Yang-Mills conclusion is inferred from this
finite-block first term.

## 9. Independent verification and evidence scope

The derivation and its actual finite-graph spectral completion were
independently reviewed in
`STRIP_BORN_OPPENHEIMER_INDEPENDENT_AUDIT.md`. Reproducible controls
in this output directory are:

* `check_strip_born_oppenheimer_audit.py` and
  `strip_born_oppenheimer_audit_controls.json`: exact coordinate
  jets, finite-rank Lie/Gaussian contractions, invariant mixed
  polynomials and noninvariant negative controls.
* `check_multistrip_selfenergy.py` and
  `multistrip_selfenergy_controls.json`: the exact on-shell image
  energy, Gaussian angular form and a negative control for using
  one denominator on different coarse shells.
* `check_multistrip_first_shell.py` and
  `multistrip_first_shell_controls.json`: symbolic-rank moments,
  direct Wick contractions and the full SU(2) first-shell matrix.
* `check_original_strip_su2.py` and its JSON record: a separate
  calculation from the original seven-link electric form in product
  logarithm coordinates, without the Schur coefficient, balanced
  horizontal lift or Born-Huang intermediate formulas.

The last calculation independently gives

```text
delta_R(2)=-15/64-3sqrt(15)/160,
delta_M(2)=63/160-3sqrt(15)/160,
delta_M(2)-delta_R(2)=201/320,
```

matching (13). Individual geometric coefficients differ between
coordinate charts; these final spectral coefficients agree after
all metric, Haar, potential and off-diagonal terms are retained.
The finite calculations verify identities and finite examples.
The all-fixed-rank spectral asymptotics and remainder follow from
the analytic localization and quasimode argument above, not from
a numerical rank sweep or extrapolation in u.
