# An actual Wilson block: action cancellation, geometric score, and rare fibers

5 September 2026. Analytic mathematical derivation. This computes a
specified Wilson gauge block, including its conditional measure, Haar
density and product/quotient metrics. It also audits the conditional
gradient and reverse-mass notes. It does not assert a four-dimensional
all-scale block estimate or identify configuration diffusion with OS
transfer energy.

## 1. A minimal actual gauge block

Take two oriented square plaquettes sharing only a base vertex, with
their eight links and no other plaquette interactions. This is a
finite cubic-lattice subcomplex: the squares can lie in two disjoint
quadrants of a coordinate plane. Maximal-tree gauge fixing identifies
its measure with two independent based plaquette holonomies U1,U2 in
SU(N), with density

```text
exp[-(2/g^2)(2N-ReTr U1-ReTr U2)] dU1 dU2.
```

These are actual Wilson plaquette weights with standard beta=2N/g^2.
Tree gauge is exact: successively integrate/tree-fix boundary links,
and Haar invariance leaves independent normalized Haar plaquette
variables. Based gauge fixing leaves simultaneous conjugation as the
residual gauge action; physical observables are invariant under it.
The deterministic coarse holonomy is U=U1 U2. It is the holonomy of the
concatenated based loops; this chosen block is not asserted to be an
elementary coarse rectangle or a reflection-adapted four-dimensional
RG map.

This is a faithful finite Wilson subcomplex. It is not the conditional
measure of an arbitrary block inside the full four-dimensional theory:
plaquettes coupling such a block to its surroundings are absent here.
It nevertheless tests purported universal gauge-block cancellations
using the actual Wilson action, rather than a polynomial surrogate.

The kinetic form is also explicit. For a gauge-invariant function
f=F(U1,U2), differentiation in each edge of square j gives a left or
right Lie derivative in Uj, conjugated by an orthogonal adjoint matrix.
Consequently

```text
sum_edges ||grad_edge f||^2
 =4(||grad_U1 F||^2+||grad_U2 F||^2).
```

Thus H_E=(1/2)sum_edges C2 has Dirichlet form
2 sum_j integral ||grad_Uj F||^2. The normalized weak-field form used
below is E_norm=(g^2/2)E_E. Its inverse metric is exactly the scaled
product metric in Section 3. All normalizations are therefore fixed
by the link form. The original electric form is recovered by the
explicit common multiplier 2/g^2.

This choice matters: for two adjacent squares sharing an edge, Haar
factorization alone does NOT imply this product face metric. The
shared-link kinetic form has additional coupling. The example here
uses the vertex-sharing bouquet precisely so the link-to-face kinetic
identity is exact; it makes no product-metric claim for an adjacent
strip.

Use anti-Hermitian traceless matrices Q,Z with Lie-algebra norm
<A,B>=-2 ReTr(AB). Let t=g/sqrt(2), and set

```text
H=exp(t Q),  K=exp(t Z),
U1=H K,  U2=K^-1 H,  U=H^2=exp(sqrt(2)g Q).
```

Lower-case q,z denote the corresponding orthonormal real coordinates.
For bounded q and small g, the square root H of the coarse U is unique
in a fixed exponential neighborhood. K is a full compact-group fiber,
not a new action approximation.

The change (U1,U2) -> (U,U1), followed by U1=H(U)K, gives exactly
dU1 dU2=dU dK. Thus the conditional fiber reference measure is Haar dK,
independent of U. In exponential coordinates its density is j(tZ) dz
up to a constant. The coarse factor j(2tQ) belongs to the marginal and
cancels from the conditional density. Exponential cut loci have Haar
measure zero; compact-fiber differentiation can be performed before
using these local coordinates, avoiding a spurious moving-domain term.

## 2. The action and Haar score start at order g squared

For anti-Hermitian Q,Z, trace cyclicity and conjugation give the exact
identity

```text
ReTr(HK+K^-1H)=2 Tr(cosh(tQ) cosh(tZ)).
```

Both cosh matrices are Hermitian, so the trace of their product is real.
The negative log conditional density, with its normalizer omitted, is

```text
V_g(q,z)=(4/g^2)[N-Tr(cosh(tQ)cosh(tZ))]-log j(tZ).
```

The first term may include a q-only summand, which has no centered
conditional score. Every displayed factor is even in g. Expanding on
fixed bounded sets of q,z, with uniform bounds also on any fixed number
of derivatives, gives

```text
V_g(q,z)= (|q|^2+|z|^2)/2 + g^2 V2(q,z)+O(g^4),

V2= -[Tr Q^4+Tr Z^4]/24 - Tr(Q^2 Z^2)/4
     +N |z|^2/48.
```

For the Haar term, the exponential-map Jacobian is
det[(1-exp(-ad X))/(ad X)]. Expanding its logarithm and using
Tr_ad(ad X)=0 gives

```text
log j(X)=Tr_ad[(ad X)^2]/24+O(|X|^4),
Tr_ad[(ad Z)^2]=2N Tr Z^2=-N |z|^2.
```

Consequently -log j(tZ)=N g^2 |z|^2/48+O(g^4). It contributes no
mixed q,z Hessian. For unit Lie-algebra directions E,F the leading
flat-coordinate mixed Hessian is

```text
d_E d_F V_g
 =-(g^2/4) Tr[(QE+EQ)(ZF+FZ)]+O(g^4).
```

This coefficient need not vanish. On an embedded SU(2) commuting line
Q=q T3, Z=z T3, with Ta=i sigma_a/2, it equals -g^2 qz/8+O(g^4).
There is therefore a genuine O(g^2), generally nonzero, coordinate
score after the conditional normalizer is subtracted.

On a fixed bounded convex z chart with q bounded, the flat fiber Hessian
is I+O(g^2). A reflecting, truncated weak-field conditional measure then
has flat Poincare gap at least 1-C g^2 by the convex-domain Hessian
argument. This is a statement about that truncated measure. Section 6
shows why it cannot be substituted for the global compact fiber gap.

## 3. The actual product metric has an order-g cross term

Give the two fine holonomies the scaled product bi-invariant metric

```text
ds_f^2=g^-2 (||U1^-1 dU1||^2+||U2^-1 dU2||^2).
```

This normalization agrees at g=0 with |dq|^2+|dz|^2. Product
multiplication has quotient metric (2g^2)^-1 ||U^-1 dU||^2; in the
normalized q chart this is |dq|^2+O(g^2). This is the metric fixed by
the fine kinetic form, not an independently chosen flat coarse metric.

Put a=H^-1 dH and b=K^-1 dK. Exact differentiation gives

```text
U1^-1 dU1=Ad(K^-1)a+b,
U2^-1 dU2=a-Ad(H^-1)Ad(K)b,

g^2 ds_f^2
 =2||a||^2+2||b||^2
  +2<a,(I-Ad(H^-1))Ad(K)b>.
```

Using a=t dQ-t^2[Q,dQ]/2+O(t^3), and the analogous formula for b,
the diagonal order-g terms vanish by skew-adjointness of ad. The cross
term remains:

```text
ds_f^2=|dq|^2+|dz|^2
       +(g/sqrt(2))<dQ,[Q,dZ]>+O(g^2).
```

Equivalently the q,z metric block is
G_zq=-(g/(2sqrt(2))) ad(Q)+O(g^2). A horizontal lift of a normalized
coarse direction E is therefore

```text
L_E=d_E+v_E.grad_z,
v_E=(g/(2sqrt(2)))[Q,E]+O(g^2).
```

The correction is fixed by orthogonality to every vertical variation.
It is absent if one simply differentiates the flat-coordinate
conditional integral, but it is present in the actual quotient metric.

## 4. The horizontal conditional score generally starts at order g

Write P f(q)=E_q f. Compact-fiber integration by parts, including the
fiber Haar density in V_g, gives

```text
d_E P f=E_q L_E f-Cov_q(f,Sigma_E),
Sigma_E=d_E V_g+v_E.grad_z V_g-div_z v_E.
```

This formula is an identity in local coordinates for the intrinsic
horizontal differentiation; the compact integration has no boundary.
For weak-field asymptotic coefficients the terms outside a fixed
exponential neighborhood are exponentially suppressed in the actual
conditional integrals. On a truncated chart alone a non-tangent lift
would require its boundary term; it is not omitted here.

The leading v_E is constant in z and has zero z divergence. Since the
coordinate potential is Gaussian to order zero,

```text
Sigma_E-E_q Sigma_E
 =(g/(2sqrt(2)))<[Q,E],Z>+O(g^2).
```

The normalizer subtracts the conditional mean, not this linear random
variable. It already has mean zero. In particular

```text
||grad_z Sigma_E||
 =(g/(2sqrt(2)))||[Q,E]||+O(g^2),
Var_q(Sigma_E)
 =(g^2/8)||[Q,E]||^2+O(g^3).
```

These are weak-field coefficient statements for the actual conditional
measure; the latter follows from its Gaussian Laplace limit. Thus, even
with a hypothetical uniform order-one global fiber gap, a generic
horizontal score ratio is O(g), not O(g^2). The action and Haar
cancellation in Section 2 does not establish the desired intrinsic
score bound.

For bounded q, the conditional potential has its unique global minimum
at K=I when cosh(tQ)>0: its K-dependent part is
(4/g^2)Tr[cosh(tQ)(I-Re K)]. Away from any fixed neighborhood of I
it has a uniform positive excess of order 1/g^2. This justifies the
Gaussian coefficient calculation and suppression of far contributions
to these moments. It does not imply a global Poincare bound, which
tests rare localized functions as well as typical moments.

## 5. What gauge invariance cancels, and what it does not

For one coarse holonomy, every residual-gauge-invariant coarse function
is a class function. Its gradient E commutes with Q. The order-g
horizontal score then vanishes. This is a real quotient cancellation,
and it explains why a single coarse plaquette calculation can suggest
the stronger O(g^2) result.

It does not extend merely by imposing the total Gauss constraint.
Take four square plaquettes sharing only their common base vertex,
with four independent Wilson weights, and group them into two pairs.
This can be realized in a four-dimensional cubic subcomplex by the
direction pairs (e1,e2), (-e1,e3), (-e2,e4), (-e3,-e4); their links and
non-base vertices are disjoint. Use the same based gauge. The two
coarse Q1,Q2 and fiber Z1,Z2 all transform by the same
conjugation. Near identity the coarse physical function

```text
F(q1,q2)=<Q1,Q2>
```

has gradients E1=Q2,E2=Q1 and satisfies exactly
[Q1,E1]+[Q2,E2]=0. Nevertheless its horizontal centered score has
leading term

```text
(g/(2sqrt(2)))<[Q1,Q2],Z1-Z2>.
```

Choose noncommuting Q1,Q2 in an embedded SU(2) subalgebra. This is a
nonzero gauge-invariant random variable. Its conditional mean is zero
and its leading Gaussian variance is
(g^2/4)||[Q1,Q2]||^2. Normalizing the coarse direction only changes the
nonzero constant.

For an explicit physical conditional test, put
f=<[Q1,Q2],Z1-Z2>. The conditional densities are even in each fiber
coordinate. Extending it with an inversion-symmetric gauge-invariant
cutoff in a fixed group exponential neighborhood gives P f=0 exactly;
the cutoff changes its weak-field coefficients only by exponentially
small tails. At leading order both
E L_E f and Cov(f,Sigma_E) equal
(g/sqrt(2))||[Q1,Q2]||^2 and cancel in d_E P f. This also identifies
the useful surviving structure: the geometric derivative and score
are correlated. Bounding them separately by a uniform mixed-Hessian
norm discards that cancellation. Connected subtraction alone does not
remove the score term.

A change of fiber coordinates cannot remove this leading intrinsic
score for the same quotient horizontal lift and conditional measure.
A successful improvement would have to change the block/form,
restrict to directions with an additional cancellation, or use the
correlated geometric derivative more sharply than the generic score
Poincare estimate. A calculation of only the action or only the
block-map Jacobian would miss this distinction.

## 6. A global compact-fiber obstruction for SU(N), N at least five

There is a separate exact obstruction to a uniform raw conditional
Poincare premise. At coarse U=I, hence H=I, the full conditional fiber is

```text
mu_g(dK)=Z_g^-1 exp[-W(K)/g^2] dK,
W(K)=4(N-ReTr K).
```

For N>=5, let zeta=exp(2pi i/N), theta=2pi/N. The central point
K_star=zeta I lies in SU(N), differs from I, and has cos(theta)>0.
For X small in su(N),

```text
W(K_star exp X)
 =4N(1-cos(theta))+cos(theta)||X||^2+O(||X||^3).
```

The linear term is zero because Tr X=0. Thus K_star is a strict local
minimum of W with positive excess above the unique global minimum I.
Choose a small radius r so its ball of radius 2r excludes I and

```text
W(K_star exp X)>=W(K_star)+c||X||^2  (||X||<=2r),
c>0.
```

Take a smooth cutoff phi equal to one on the radius-r ball and zero
outside radius 2r. It can depend only on distance from the central
point, so it is gauge invariant. Its gradient is supported where
W>=W(K_star)+b, with b=c r^2>0. On the radius-g ball about K_star,
W<=W(K_star)+C g^2 and Haar volume is at least c0 g^d,
d=N^2-1. The probability of supp(phi) tends to zero because the
entire support stays a fixed positive energy above I. Cauchy-Schwarz
gives (E_mu phi)^2<=mu(supp(phi)) E_mu(phi^2), so for small g its
variance is at least half its second moment.

The actual scaled vertical metric at fixed U is
2g^-2 ||K^-1dK||^2. Its Dirichlet form is therefore
(g^2/2) integral ||grad_K f||^2 dmu_g. The cutoff Rayleigh quotient
gives the explicit form of an upper bound on its Poincare gap:

```text
kappa_g <= C g^(2-d) exp(-b/g^2) ->0.
```

The common normalizer Z_g and the well's Boltzmann weight cancel from
the quotient. An unscaled group Dirichlet form has the same exponential
obstruction with prefactor g^-d. The secondary well is suppressed in
ordinary weak-field moments but remains visible to the spectral-gap
variational problem.

This is not removed by gauge invariance or coarse center neutrality:
U1=K_star,U2=K_star^-1 has coarse product I, and the cutoff is already
a physical class function. The argument as stated uses N>=5; it makes
no secondary-center-well claim for N=2,3,4.

Thus even an improved small-field O(g^2) score cannot justify a
uniform global raw-fiber Poincare constant for this block at N>=5.
One must explicitly handle these modes, change the conditional
Dirichlet mechanism, or use a different physical complement estimate.

### 6.1. The adjacent-square link metric can also be computed exactly

The same rare-well obstruction holds for a genuine adjacent two-square
strip, with its shared-edge kinetic coupling retained. It is useful to
record this independently of the simpler bouquet metric calculation.

Choose based loops U1=s b1 and U2=b2 s^-1, where s is the common edge
and b1,b2 are the three-edge outer paths. In right-trivialized face
velocities each outer edge gives an orthogonally rotated derivative
in its own face. The shared edge gives (E,-Ad(U2)E). Thus the exact
unscaled link co-metric is represented by

```text
3 sum_j ||grad_Uj F||^2 + sum_a |(L1_a-R2_a)F|^2.
```

In coordinates U=U1U2 and K0=U1 its tangent vectors are (E,E),
(Ad(K0)E,0), each with multiplicity three, and ((I-Ad(U))E,E).
Consequently its exact matrix blocks are

```text
C_uu=8I-Ad(U)-Ad(U)^*,
C_uk=4I-Ad(U),  C_ku=C_uk^*,  C_kk=4I,
S(U)=C_kk-C_ku C_uu^-1 C_uk=15 C_uu^-1,
(3/2)I<=S(U)<=(5/2)I.
```

The exact simplification follows because all factors are commuting
polynomials in Ad(U) and its inverse. Its bounds use the spectrum of
Ad(U)+Ad(U)^* in [-2,2]. Thus the vertical metric has no degeneracy
that could account for the rare-well diffusion obstruction.

At U=I this becomes [[6I,3I],[3I,4I]]. Its induced fiber co-metric is
the Schur complement 4I-(3I)(6I)^-1(3I)=(5/2)I, for every K0.
Including H_E's factor 1/2, the intrinsic fixed-U=I electric fiber
operator is exactly -5 Delta_K0/4, restricted to class functions in
the physical sector. The conditional Haar density is the same Wilson
density as above. Therefore the cutoff proof still gives an
exponentially small diffusion gap; only a fixed metric prefactor changes.

The geometric score also remains first order. Put alpha=sqrt(2)g,
U=exp(alpha Q), K0=H K with H=exp(alpha Q/2), K=exp(alpha Z/2).
The horizontal K0 velocity is C_ku C_uu^-1 times the coarse U velocity.
Expanding gives

```text
C_ku C_uu^-1 = I/2+(alpha/6)ad(Q)+O(alpha^2),
dU U^-1=alpha E+(alpha^2/2)[Q,E]+O(alpha^3),
dH H^-1=alpha E/2+(alpha^2/8)[Q,E]+O(alpha^3),
v_Z=(7alpha/12)[Q,E]+O(alpha^2)
    =(7g/(6sqrt(2)))[Q,E]+O(g^2).
```

Thus the actual shared-link metric changes the coefficient, not the
order. For E_norm=(g^2/2)E_E its leading coordinate metric is
(4/3)|dq|^2+(4/5)|dz|^2. Setting qhat=2q/sqrt(3),
zhat=2z/sqrt(5) makes it Euclidean to leading order and gives
V0=3|qhat|^2/8+5|zhat|^2/8. In those matched variables the leading
horizontal lift and centered score are respectively

```text
v_zhat=(7g/(4sqrt(10)))[Qhat,Ehat],
Sigma_Ehat-centered
 =(35g/(16sqrt(10)))<[Qhat,Ehat],Zhat>.
```

The leading weak-field fiber gap is 5/4. This still gives a generally
order-g score ratio. Single-holonomy class directions cancel it as
before; no assertion about arbitrary multi-block cancellation follows.
The computations describe a pointwise constrained rotor and its
configuration form. They do not identify that rotor with the
orthogonal complement of an OS-history block isometry.

## 7. Independent audit of the two input notes

The conditional formula, sharp Gaussian two-by-two matrix, corrected
coarse metric, and separated-fiber square-budget theorem in
[G19_CONDITIONAL_GRADIENT_REPAIR_20260905.md](G19_CONDITIONAL_GRADIENT_REPAIR_20260905.md)
are correct under their stated hypotheses. In particular the matrix
majorization determinant is t(t-c^2)>=0 when t=c^2/(1-theta), and
the Gaussian example attains its constant. The needed input is the
actual score and actual fiber gap in the same metric. Sections 3-6
show why these inputs cannot be read off from a flat weak-field action.

[G19_OS_BLOCKING_AND_REVERSE_MASS_MATCHING_20260905.md](G19_OS_BLOCKING_AND_REVERSE_MASS_MATCHING_20260905.md) correctly constructs
an OS-history isometry from an exact reflection-adapted pushforward
whose map commutes with time blocking. Its identities

```text
T_f^b J=J T_c,
T_f J=J T_c^(1/b)
```

follow from time covariance and positive functional calculus. The
physical clock h_c=b h_f preserves a coarse mass bound on ran J.
The note correctly requires a separate estimate on its reducing
orthogonal complement before concluding a full fine-theory gap.
Its reverse energy scaling, normalized-source requirement and
fixed-momentum/finite-physical-volume atom scope are also consistent.

## 8. Consequence for the next physical target

The two calculations separate three issues: the Wilson/Haar
small-field action is even in g; the intrinsic multi-holonomy score
already has an order-g geometric contribution; and the global
configuration-diffusion fiber can have exponentially slow rare wells.
None contradicts the established small-magnetic-coordinate actual
Wilson transfer theorem, and none by itself implies a slow physical
OS transfer mode. Configuration diffusion and transfer energy are
different operators; their comparison is precisely the unresolved
form obligation, not a consequence of reflection positivity.

The reverse-mass bridge provides a more direct target: construct the
actual reflection/time-covariant block isometry and bound the OS
transfer on (ran J)^perp, with the fine physical clock retained.
A gauge-reduced free Maxwell high-momentum complement can serve as a
specified leading ultraviolet reference, but interacting control,
zero/constraint modes and the actual effective measure must be proved.
The rare-fiber calculation is a reason to test that physical
complement directly rather than assume a raw conditional diffusion
gap transfers to it.

No four-dimensional scale estimate is proved in this note. What is
proved is the exact cancellation and obstruction mechanism in a
faithful Wilson block, including an explicit gauge-invariant
two-holonomy counterexample and a global conditional-gap upper bound.

## 9. Reproducible controls and independent review

The [sealed run](../../runs/continuum_wilson_block_2026-09-05/README.md)
preserves [check_wilson_block_score.py](../../runs/continuum_wilson_block_2026-09-05/check_wilson_block_score.py)
and its [output](../../runs/continuum_wilson_block_2026-09-05/wilson_block_score_controls.json).
The checks use exact Lie-algebra traces for the mixed quartic
coefficient, total Gauss identity, nonzero physical commutator,
positive SU(5) center Hessian and strip Schur constant. Direct finite
matrix exponentials independently check the action identity and both
geometric metric coefficients at four decreasing g values. These are
finite algebra and floating coefficient controls; the analytic
remainder and rare-well estimates are established by the arguments
above, not by extrapolating the table.

The parallel reverse-matching collaborator independently checked the
product metric, actual adjacent-strip co-metric, 7alpha/12 lift,
rare-well mechanism and the revised kinetic/OS scope. The two input
notes were independently audited in Section 7. The current result and
route scopes are recorded in the maintained claim graph; the source
extractions and previous sealed proofs remain unchanged.
