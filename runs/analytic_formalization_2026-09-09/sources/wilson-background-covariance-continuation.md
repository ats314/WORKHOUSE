# Wilson background reference and charged signed covariance

Continuation: [SC17 spatial closure](wilson-sc17-spatial-closure.md) now proves
the actual connected weighted row bound and conditional assembly for
0<=k/epsilon<lambda_c, with explicit corollary k/epsilon<=1/73. The historical all-coupling pointwise estimates below
remain valid; their large-coupling spatial extension is still open.

9 September 2026. Continuation of BA26 in
[the actual block estimate](wilson-true-vacuum-block-estimates.md).
This note implements the proposed change of reference and the direct BA11
route. BF4-BF6 prove an actual magnetic small-field comparison at arbitrary
k/epsilon. SC10-SC16 prove pointwise derivative and signed-covariance bounds
for the actual physical semigroup, at every coupling, uniformly in volume
and physical time. The remaining connected spatial estimate is SC17.
These are analytic arguments; the seven registered exact controls verify
finite algebra, geometry, and counterexamples, not the full operator proofs.
No continuum completion is asserted.

Use SU(2), the product unit-S3 metric and H=-epsilon Delta+k S. The natural
background fluctuation scale is g_*=(epsilon/k)^(1/4), X=g_*Y. Exactly,
H/sqrt(epsilon k)=-g_*^2 Delta+g_*^(-2)S; its local quadratic limit is
-Delta_Y+K[Y]/2. The physical time variable is sigma=t sqrt(epsilon k).
For epsilon=c_E g_phys^2/a and k=c_B/(a g_phys^2), sqrt(epsilon k) is
sqrt(c_E c_B)/a. Keep the RG blocking ratio ell fixed in BF5; a block with
fixed physical size and ell proportional to 1/a has a different radius budget.

The graph was queried for G17, G19, G22 and G23. Existing complete Schur
memory and source-rank repairs are retained below. G22 names Cartan-alignment
coercivity in this graph; the relevant Feshbach derivations are SP1-SP10 and
W4-W6, not a previously closed G22 theorem.
## Part I. Background-fast comparison

Analytic background derivation, independently reconstructed in this continuation.

## Graph and prior theorem boundary

`workhouse why G17`, `why G22`, and `why G19` were run against the current catalogue.
G17 is free-energy/source-radius stability. G22 is Cartan-alignment coercivity,
not the name of a Feshbach identity. The existing Feshbach statements are SP1-SP10
in `docs/derivations/wilson-spatial-schur-excess.md` and W4-W6 in
`docs/derivations/wilson-selected-inverse-wall.md`.

The graph already rejects an all-fast-space compact-to-Gaussian upper form
comparison after finite-rank retention. Changing the background does not undo
the high-representation asymptotics in W2-W3. A compact reference, a common
small-field domain, or selected inverses avoids that particular contradiction.

## BF1. The energy-dependent relative-form statement

Let the scale and coarse background be fixed. On a specified common fast form
domain let

    A0(z) = F0-z >= f_z I > 0,
    Ag(z) = Fg-z = A0(z)+V,
    C(z) = A0(z)^(-1/2) V A0(z)^(-1/2).

Suppose C is a bounded self-adjoint form representative, ||C(z)||<=theta_z<1.
Then Ag(z)>=(1-theta_z)A0(z), and its form inverse is

    Rg = A0^(-1/2)(I+C)^(-1)A0^(-1/2),
    ||A0^(1/2)(Rg-R0)A0^(1/2)|| <= theta_z/(1-theta_z).

In particular, for every admissible source w,

    |V[R0 w,Rg w]| = |<w,(R0-Rg)w>|
        <= theta_z/(1-theta_z) <w,R0 w>.                 (BF1)

This follows by the spectral calculus of I+C, not a perturbative series in
lambda=k/epsilon. It allows a signed V. Positivity is only imposed on the fast
restrictions at the chosen z, not on the entire unshifted interacting form.
It does not derive theta_z or the fast floor from the algebraic identity.

For an energy interval, an unshifted estimate

    F0>=f0 I, |V[u]|<=a F0[u]+b||u||^2, b>=0,

implies, for 0<=z<f0,

    theta_z <= (a+b/f0)/(1-z/f0).                        (BF2)

The vacuum subtraction belongs to V: a scalar change delta_e contributes to b
by |delta_e|. A bound for a bare positive magnetic action cannot discard this
term. Uniformity up to z_* requires a+b/f0 < 1-z_*/f0, with constants uniform
in scale, background, volume, and the complete retained window being matched.

If the full-graph force is r_g=Q(Hg-H0)J0,z, not merely QVP, square completion
gives exactly

    Sg(z)-S0(z) = J0,z* V J0,z - r_g* Rg(z) r_g,
    Jg,z = J0,z - i_Q Rg(z) r_g.                        (BF3)

Every product here needs the form-dual/domain hypotheses in W4. Combining BF1
with a uniform selected synthesis bound

    sup_(b[p]=1) <t1 p,R0 t1 p> <= C_force

would give the selected W6 bound with constant
theta_z C_force/(1-theta_z). For theta_z=O(g), this is the requisite O(g).
No condition on small lambda is needed in this implication. The resulting
Schur comparison retains -partial_z Sg=Jg,z*Jg,z; static energy comparison
alone does not supply the source norm/physical clock.

## BF4. An actual Wilson small-field estimate, uniform in volume

Use SU(2), unit S^3 link metric, a periodic three-dimensional cubic lattice
with side at least three, and ANY flat background Ubar. The two orientations
of a link are not independent. Put

    U_e(X)=exp(X_e) Ubar_e,
    S(X)=sum_p [1-(1/2)Re Tr U_p(X)],
    |X_e|=||X_e||_op,   max_e |X_e|<=delta.

Let v be a real original-link tangent variation, using the same coordinates.
Then

    |D^2 S(X)[v,v]-D^2 S(0)[v,v]| <= 64 delta sum_e |v_e|^2. (BF4)

Proof with the constant. Flatness writes every plaquette word as four factors
exp(Y_i), where each Y_i is a fixed adjoint transform of plus or minus one X_e.
Those transforms preserve operator norm. For skew-adjoint Y, the ordered
simplex formula for D^m exp(Y), including its m! orderings, gives
||D^m exp(Y)[a1,...,am]|| <= product_j ||aj||: the intervening exponentials
are unitary and the total simplex weight is one. Leibniz therefore gives

    |D^3 s_p(X)[a,v,v]| <= (sum_(e in p)|a_e|)
                                      (sum_(e in p)|v_e|)^2.

Integrate along tX from zero to X and use sum_(e in p)|X_e|<=4delta and
(sum_(e in p)|v_e|)^2<=4 sum_(e in p)|v_e|^2. Each link is in four plaquettes,
so 4*4*4=64. This controls the actual trace-exponential Wilson action and all
orders of its remainder. It is not a formal cubic truncation.

At X=0, D^2S(0)[v,v]=||c_Ubar v||^2. On the fixed physical transverse tangent
space C_Ubar=ker d_Ubar*, let P_Ubar be the pinned length-ell path-source
projection and Q_tan=I-P_Ubar. The existing flat-background theorem gives

    K_Ubar=c_Ubar* c_Ubar >= c_ell Q_tan,
    c_ell=3072/(pi^10 ell^2) >= 1/(33 ell^2).

For v in ran Q_tan, BF4 consequently yields

    (1-theta) K_Ubar[v] <= D^2S(X)[v,v]
                         <= (1+theta) K_Ubar[v],
    theta=64delta/c_ell <= 2112 ell^2 delta.              (BF5)

In particular delta<=1/(4224 ell^2) gives theta<=1/2. These constants do not
depend on total volume or flat winding holonomies. The kernel of K_Ubar is
retained by P_Ubar; no flat/harmonic coordinates are deleted. For smooth
background differentiation, use the pinned fixed-rank redundant source
construction rather than differentiating P_Ubar through its SU(2) rank jump.

## BF6. Centering at an actual constrained minimizer

Fix the coarse tangent data and the fixed fast affine slice. Suppose Xbar is
an interior stationary point on this slice, and the segment Xbar+t xi lies
in the above small-field region for 0<=t<=1, with xi in ran Q_tan. (Xbar=0
and zero coarse tangent data is the directly constructed flat example.) Then
Taylor's integral formula and BF5 give the exact, all-coupling estimate

    (1-theta)/2 K_Ubar[xi] <= S(Xbar+xi)-S(Xbar)
                            <= (1+theta)/2 K_Ubar[xi].   (BF6)

It applies after multiplication by any k>0. If a common positive fast kinetic
form t_D is specified on a small-field Dirichlet domain, including its actual
metric and density, then with

    h_ref=t_D+(k/2)K_Ubar[xi],
    h_sf=t_D+k[S(Xbar+xi)-S(Xbar)],

we have |(h_sf-h_ref)[psi]|<=theta h_ref[psi] for every vector of that common
domain. Retaining the same kinetic form makes this implication independent
of an electric-metric/Haar Taylor expansion. This is a precise admissible
background reference on that specified domain. It is not automatically a
Gaussian: making the kinetic form flat is an additional comparison.

This derivation applies at arbitrarily large lambda. Its small parameter is
the actual link-coordinate radius delta times ell^2. The nominal oscillator
fluctuation scale lambda^(-1/4) decreases in the weak-coupling direction; this
observation alone does not establish the actual small-field probability,
conditional ground density, or cutoff errors.

BF6 does not prove that every admissible nonlinear coarse background has such
a minimizer in this chart. Nor does the fixed tangent affine fiber equal the
actual nonlinear observation fiber. Those must be constructed if this local
bound is to serve the literal physical source algebra. The pinned submersion
theorem is an available geometric input, with volume-independent radius
1/[2sqrt(6)ell(7ell-6)^2], but does not identify the quantum source projection.

## Exact remaining implication

The completed step is an actual all-orders local magnetic comparison in a
background reference, plus the exact quantitative resolvent implication BF1.
What is not proved is its extension to the ACTUAL vacuum-subtracted quantum
fast restrictions on the whole source complement, with the localized bad-field
sector included. Specifically, one still needs either

    sup_(scale,background,Lambda,z) ||(F0-z)^(-1/2)
        (Factual-F0)(F0-z)^(-1/2)|| < 1,

in a compatible compact/localized reference, or the strictly weaker selected
version

    sup_(b[p]=1) |(Factual-F0)[R0 t1p,Ractual t1p]| <= C g,

and a uniform actual fast floor on the relevant z interval. A scalar
probability for the excluded set does not establish the form coupling or its
Schur self-energy. The fixed-tangent BF5 also is not an estimate for the
conditional law Omega^2 or its logarithmic mixed difference BA6/BA11.

Only after these steps, connected direct/force remainders and second-order
coarse/source matching give the summable O(g^3) errors of SP8-SP25. No source
overlap or physical continuum expectation limit follows from BF4 alone.

## Sources read and exact locations

* `docs/derivations/wilson-spatial-schur-excess.md`: SP1-SP6, lines 41-119;
  SP8-SP10, lines 135-185; actual Wilson jets SP11-SP16, lines 189-307;
  source SP18 and rank warning, lines 360-379; scale/overlap SP21-SP25,
  lines 429-518.
* `docs/derivations/wilson-selected-inverse-wall.md`: full-space spectral
  obstruction W2-W3; admissible selected Schur W4, lines 106 onward;
  W5 selected estimate, signed identity, and W6 (use equation labels where
  a later edit changes line numbers).
* `docs/derivations/wilson-spatial-inputs/G19_FLAT_HOLONOMY_SOURCES_AND_RANK_REPAIR_20260907.md`:
  lines 19-25 flat background scope; 27-59 definitions, coercivity, retained
  kernel; 61-82 rank issue, redundant source, submersion radius and quantum
  projection limitation.

Primary literature searched for regime verification:

* Balaban (1985), variational/background-field paper, institutional repository:
  https://deepblue.lib.umich.edu/items/e9af57c2-30bd-4dfc-85cd-3f01956f02fa .
  Its abstract proves a minimum on regular configurations with fixed averages,
  unique up to gauge. Only the institutional abstract was read here, not the
  full proof or its quantitative hypotheses.
* Balaban (1987), four-dimensional small-field effective actions:
  https://www.researchwithrutgers.org/en/publications/renormalization-group-approach-to-lattice-gauge-field-theories-i-/ .
  Its abstract explicitly uses cluster expansions in one-step transformations
  within the small-field region. Again, not treated as a discharged quantum
  ground-law hypothesis.

The analytical BF4-BF6 argument above is derived here; it has not been Lean
formalized and no finite arithmetic control has been substituted for its
operator/domain hypotheses.

## Exact finite controls and scale convention

One standalone SymPy/standard-library check was actually run successfully:
on the nondegenerate periodic side-three cubic lattice there are 81 links and
81 plaquettes; every face has four distinct links and every link belongs to
four faces. Thus the combinatorial factor in BF4 is exactly 4*4*4=64.
Independently use four anti-Hermitian Pauli vectors with twelve independent
real symbolic components. The coefficient of t^2 in
1-Tr[exp(tX1)exp(tX2)exp(-tX3)exp(-tX4)]/2 is exactly
|X1+X2-X3-X4|^2/2. SymPy simplified the difference to zero. The test checks
the actual SU(2) second jet without a commuting-matrix assumption. The
Frechet derivative/unitary-simplex estimate itself is the analytical proof
above, not a result inferred by testing these finite matrices.

The natural dimensionless background fluctuation convention is

    g_*=(epsilon/k)^(1/4), X=g_*Y,
    Hhat=H/sqrt(epsilon*k)=-g_*^2 Delta+g_*^(-2) S,
    Hhat -> -Delta_Y+(1/2)K[Y],
    sigma=t sqrt(epsilon*k).

The continuum parameter g_* is distinguished from any prior g_H convention.
For epsilon=c_E g_phys^2/a and k=c_B/(a g_phys^2),
g_*=(c_E/c_B)^(1/4)g_phys and sqrt(epsilon*k)=sqrt(c_E c_B)/a.
Use a fixed integer RG blocking ratio ell in BF5. A macroscopic block with
ell growing as 1/a has an allowable chart radius only of order a^2 under
this estimate; treating that as a fixed radius would be an invalid change
of quantifiers. With fixed ell, the allowable radius is uniform in total
volume and refinement step, and typical oscillator coordinates are of
order g_*. Controlling the actual law in those coordinates remains separate.

## Part II. Charged-sector control of exact log-vacuum derivatives

Analytic signed-covariance derivation. Its Casimir, Markov, and parabolic
arguments received an independent review recorded with the validation artifacts.

## 1. Setup and exact equations

Let M=SU(2)^E with the product unit-S3 metric, normalized product Haar
measure, and a finite periodic cubic lattice of side L>=3. Put

    H=-epsilon Delta+V,  V=k sum_p (1-Tr(U_p)/2), lambda=k/epsilon.

The positive normalized ground Omega is gauge invariant. Define
u=log Omega, mu=Omega^2 dU and

    K=Omega^{-1}(H-E0)Omega
     =-epsilon(Delta+2 grad u . grad).

K is nonnegative self-adjoint in L2(mu), with Dirichlet form
epsilon integral |grad f|^2 dmu. Its kernel consists of constants. All
arguments below are at fixed finite volume first, but their displayed
constants are independent of that volume.

Let X_e^a be left-translation Killing fields on link e, with a=1,2,3.
Precisely, X_e^a f(U)=d/ds f(...,exp(s T_a)U_e,...) at s=0.
These generate left multiplication and are right-invariant vector fields
in differential-geometric terminology. This explicit convention, also used
by the quaternion control, determines the gauge charge at the link tail.
The bi-invariant Laplacian commutes with these fields, and the Killing
identity is

    X <grad f,grad g>=<grad Xf,grad g>+<grad f,grad Xg>.

Differentiating the logarithmic ground equation gives, exactly,

    K(Xu)=-XV.                                                   (SC1)

Haar integration by parts gives mu(Xu)=0, and integrating SC1 gives
mu(XV)=0. For commuting fields X,Y on different links,

    K(XYu)=-XYV+2epsilon <grad Xu,grad Yu>,
    mu(XYu)=-2 mu((Xu)(Yu)).                                    (SC2)

Thus the unrestricted reduced-resolvent formula must retain the constant:

    XYu=-2mu((Xu)(Yu))
        +K_0^{-1}[-XYV+2epsilon <grad Xu,grad Yu>].               (SC3)

The bracket has mean zero. Taking an unrestricted norm of K_0^{-1}
would insert the unknown global gap. It is unnecessary for the charged
sectors below.

An exact product-rule rearrangement removes derivatives of Xu from the
right side. Set F_e=(X_e^a u)_a, V_e=(X_e^a V)_a, and for e!=f set

    H_ef=(X_f^b X_e^a u)_{a,b},
    Q_ef=H_ef+F_e tensor F_f
        =((X_f^b X_e^a Omega)/Omega)_{a,b}.

Then

    K Q_ef=-V_ef-F_e tensor V_f-V_e tensor F_f,
    V_ef=(X_f^b X_e^a V)_{a,b}.                                 (SC4)

This can also be obtained by differentiating H Omega=E0 Omega twice.
Tensor ordering in SC4 follows the e-index first and the f-index second.

## 2. A gauge-orbit gap that does not assume the physical gap

Orient links from x to y, with gauge action U_e -> h_x U_e h_y^{-1}.
Let G_x^a be the infinitesimal gauge generator at x and

    C_x=-sum_a (G_x^a)^2.

For every scalar f, pointwise Cauchy--Schwarz gives

    sum_a |G_x^a f|^2 <= d_x sum_(e incident x) |grad_e f|^2,
    d_x=6.                                                      (SC5)

Left and right link frames have identical metric norm. Gauge invariance
of mu implies G_x^a is skew-adjoint in L2(mu). Therefore

    K_res,x=K-(epsilon/6) C_x                                   (SC6)

has nonnegative Dirichlet form. More is true: that form has a smooth
positive semidefinite diffusion matrix and no killing term, and satisfies
the Markov contraction property. Its closed Friedrichs form generates a
positivity-preserving, mu-preserving semigroup, contractive on every Lp.
Degeneracy of the residual diffusion causes no problem for this assertion.

There is also an explicit smooth sum-of-squares realization. At x, let
Z_i^a be the six signed link generators (left for outgoing links, minus
right for incoming links), so G_x^a=sum_i Z_i^a. Different links commute,
and

    Delta_star-(1/6)sum_a (G_x^a)^2
       =(1/6)sum_a sum_(i<j)(Z_i^a-Z_j^a)^2.                   (SC6a)

Adding the outside-link Laplacians and the smooth drift 2grad u.grad
realizes -K_res,x as a smooth diffusion generator. Replacing u by v_T
below gives the same explicit realization at each finite physical time.
For two disjoint stars the two subtractions have disjoint link support.

K commutes with the gauge group, hence with C_x. The residual form also
commutes with the gauge group. Strong commutation and the spectral
decomposition of C_x give, on its Casimir-c eigenspace,

    exp(-tK)=exp[-epsilon c t/6] exp(-t K_res,x).                 (SC7)

For a vector F with values in a fixed finite-dimensional gauge
representation, the residual Markov semigroup acts componentwise.
Jensen's inequality gives |P_t F|<=P_t |F|; therefore (SC7) yields

    ||exp(-tK)F||_Lp(mu;R^n)
      <=exp[-epsilon c t/6] ||F||_Lp(mu;R^n), 1<=p<=infinity.    (SC8)

With the unit-S3 normalization, spin-j has Casimir 4j(j+1): the adjoint
representation (spin 1) has c=8. A left link derivative of any
gauge-invariant scalar is an adjoint-covariant 3-vector at its tail and
is gauge invariant at every other vertex. Thus F_e and V_e satisfy
C_x F_e=8 F_e, C_x V_e=8 V_e at x=tail(e).

Consequently the charged inverse R_x=(K restricted to adjoint at x)^-1
exists with

    ||R_x||_Lp->Lp <= 3/(4epsilon), 1<=p<=infinity.              (SC9)

This is a consequence of local gauge symmetry and electric energy. It
does not use a physical-sector Poincare inequality or an interacting
mass gap. The scale is epsilon and need not stay positive in an arbitrary
continuum rescaling.

If x and y are different nonadjacent vertices, their incident link sets
are disjoint. Then one may subtract (epsilon/6)(C_x+C_y), giving charged
mass 8epsilon/3 for a field adjoint at both x and y. For arbitrary
different x,y, the single-vertex mass 4epsilon/3 always suffices. A global
variant subtracts (epsilon/12)sum_x C_x, because every link meets two
vertices; it gives mass 4epsilon/3 for two distinct adjoint charges.

## 3. Uniform pointwise first and mixed derivatives at every coupling

Each cubic link belongs to four plaquettes. For a single occurrence of a
link in a plaquette, |grad_e Tr(U_p)/2|<=1 in the unit-S3 metric. Hence
||V_e||_infinity<=4k. Combining SC1 and SC9 proves

    F_e=-R_x V_e,
    ||F_e||_infinity <=3lambda.                                (SC10)

This is uniform in the entire configuration U, all outside values and
total lattice volume, and holds for every lambda>=0.

For x=tail(e) and y=tail(f) distinct, H_ef and Q_ef transform as
adjoint_x tensor adjoint_y. To see this even when f ends at x, note that
its left derivative commutes with the right action at its head. Thus the
charged inverse applies to SC4, with no constant part and no physical
gap assumption. In the Euclidean tensor norm,

    ||Q_ef||_infinity
       <=(3/(4epsilon))||V_ef||_infinity+18lambda^2,
    ||H_ef||_infinity
       <=(3/(4epsilon))||V_ef||_infinity+27lambda^2.              (SC11)

If x,y are nonadjacent, improve the inverse factor by two:

    ||H_ef||_infinity
       <=(3/(8epsilon))||V_ef||_infinity+18lambda^2.              (SC12)

When no plaquette contains both e and f, V_ef=0 exactly. Thus SC12 gives

    ||H_ef||_infinity <=18lambda^2                               (SC13)

for every such distant pair, independently of how large its distance is.
This supplies a true all-coupling bound on the BA11 signed covariance
limit and suppresses its spurious T or T^2 growth. It does not supply
decay with the distance.

For blocks B,C separated enough that every pair of tails is nonadjacent
and no plaquette meets both blocks, SC13 and Cauchy--Schwarz give

    sup_(|X|=|Y|=1) |XYu| <=18lambda^2 sqrt(r_B r_C),
    D_BC <=36 pi^2 lambda^2 r_B r_C.                            (SC14)

The first derivative result also gives a supplementary true conditional
gap. Sequential shortest link geodesics have lengths at most pi; hence
osc_B u<=3pi r_B lambda. Comparing mu(.|outside) to product Haar gives

    gamma_B >=3epsilon exp[-6pi r_B lambda].                    (SC15)

This is exact at lambda=0 and holds for all lambda, but the previous BA4
floor is better at sufficiently large lambda. One may take the maximum
of the two proved floors.

## 4. Direct finite-time form, without an implicit long-time interchange

Let Z_T=exp(-TH)1, v_T=log Z_T and
K_T=-epsilon(Delta+2grad v_T.grad). Gauge invariance holds for each T.
Differentiating the parabolic equation gives

    partial_T F_e,T=-K_T F_e,T-V_e,  F_e,0=0,
    partial_T Q_ef,T=-K_T Q_ef,T
                     -V_ef-F_e,T tensor V_f-V_e tensor F_f,T,
    Q_ef,0=0.                                                   (SC16)

The residual Markov argument works for the time-dependent diffusion:
its principal matrix is unchanged, its drift is gauge invariant, and
each instantaneous operator has the same charged Casimir shift. Maximum
principle/Markov evolution contraction gives damping exp[-m(T-s)] in
L-infinity, where m=4epsilon/3 (or 8epsilon/3 for two nonadjacent tails).
Thus

    ||F_e,T||_infinity <=3lambda(1-exp[-4epsilon T/3]),

and SC11-SC13 hold uniformly for every T as upper bounds. At fixed finite
volume, smooth ground-state convergence then passes them to u. Therefore
the BA11 signed-covariance bound is obtained before taking the ground
limit, with no volume-uniform ground convergence assumption.

## 5. The neutral channel and the exact remaining spatial bound

When e and f have the same tail, their second derivative transforms as
adjoint tensor adjoint at one vertex. That representation contains a
singlet. The scalar contraction sum_a X_f^a X_e^a u can be physical, and
the Casimir shift is zero on it. The unrestricted SC3 must retain its
mean and its reduced physical resolvent. This is a precise representation
boundary, not a claim that every Hessian component is protected.

Even at distinct distant tails, SC13 has no distance factor. Summing its
right side over blocks still grows with volume. Writing V_ef=0, the
remaining connected quantity is exactly

    H_ef = -R_xy(F_e tensor V_f+V_e tensor F_f)
           -F_e tensor F_f.                                    (SC17)

Here R_xy is the actual charged inverse under the true vacuum. Separate
norm bounds on the two terms give SC13/SC11 and discard their spatial
connected cancellation. The next needed estimate is a bound on SC17,
uniform over configurations and outside values, of the form

    || R_xy(F_e tensor V_f+V_e tensor F_f)
          +F_e tensor F_f ||_infinity <=C(lambda) exp[-m(lambda)d(e,f)],

with a block row sum strictly below one after the stated physical
rescaling. The gauge Casimir argument supplies resolvent invertibility,
but does not supply quasi-locality of the ground-state drift or the
connected cancellation in SC17. Those require the proposed background
reference/Feshbach construction, or another new spatial estimate.

The new result is therefore stronger than merely rewriting BA11: it
proves all-coupling, volume-uniform pointwise first derivatives and distant
mixed derivatives, without a presumed physical gap. The exact missing
step for the actual BA1 ell=1 covering is spatial decay of the connected
charged-resolvent combination SC17. Every cross-block derivative for
those disjoint three-link tail blocks has distinct tails, so the same-tail
neutral channel is not an extra prerequisite for that particular block
angle. It is a limitation only of extending the inversion to arbitrary
second derivatives. Charged inverse existence, finite-time boundedness,
and a true conditional gap are supplied by the present argument.

## BC1. Why a fast inverse alone cannot finish the transport

A minimal exact control is H_eta=0 direct_sum [[1+eta,1],[1,1]], eta>0.
Its fast inverse is identically one, its retained Schur form is eta, and
the excited vector (1,-1) has Rayleigh quotient eta/2. Thus fast resolvent
invertibility and a zero fast perturbation can coexist with a vanishing
physical gap. The remaining retained Schur form and its induced source
metric must be controlled. This example is an inference test, not a model
of Wilson gauge theory.

## BC2. The additional multiscale document is evidence, not a completed input

During the search, `yangmills-continuum-balaban-multiscale-proof.md` was
located and read in full by the independent audit. Its earliest substantive
failed equality is Lemma 3.2, the second equality after (3.5): the transported
average of g^-1 partial g is replaced by the derivative of an interpolation
of barycenter values. For A=0 and g=exp(h T) in a Cartan subgroup, take h a
smooth bump crossing a block face and vanishing near every barycenter.
The coarse gauge samples are all I, whereas the normal component is
Q(A^g)=-T/|Delta| integral_face h !=0. Interpolating the identical coarse
samples gives the identity coarse gauge and cannot reproduce this term.
A finite polynomial control on two cells gives the same mismatch 1/16.

A valid replacement is averaging an adjoint fluctuation z relative to a
transforming background B. This transforms homogeneously. The repo's
actual endpoint-covariant matrix path observations supply another available
repair. Neither replacement permits treating the nonlinear observation as
a fixed linear map when differentiating its constrained action.

Two later inequalities in that document independently miss the desired
small parameter: (5.8) declares C_0 g^(-kappa') small for kappa'>0; and
(5.12)-(5.13) drop the adverse factor g^(-kappa). BF4-BF6 above instead
specify the coordinate radius and retain every factor in the magnetic bound.
The submitted source is preserved unchanged.

## BC3. Exact current stopping point

The small-field reference no longer requires k/epsilon to be small.
The physical-time signed covariance is now uniformly bounded before the
long-time limit. What remains is a spatially summable bound for SC17, or a
complete quantum fast/retained comparison that implies it. Explicitly,
for distinct distant tails and V_ef=0, it is necessary for the proposed
angle route to bound

    R_xy(F_e tensor V_f+V_e tensor F_f)+F_e tensor F_f

with enough decay that the actual mixed-ratio block row is strictly below
one, uniformly through the prescribed scale trajectory. SC13 bounds its
norm by 18lambda^2 but supplies no distance factor. BF6 controls the actual
magnetic form on a specified small-field affine slice; it does not bound
the coupling to the omitted field sector, actual vacuum subtraction,
nonlinear observation fibers, or the complete retained Schur energy.
Those are the precise inputs still needed to apply BF1 to the physical
source family and then the existing matching/relative-gap theorems.
The two resolvents also have distinct roles: R_xy acts in a sector with
two adjoint gauge charges, whereas the G19 physical source complement is
gauge invariant. BF1 is available in either specified sector, but their
projections, norms, and source vectors cannot be identified. A background
application to SC17 must construct the charged comparison; physical carrier
transport must separately satisfy the physical source theorem's hypotheses.

No probability assigned to an omitted sector bounds its Schur self-energy.
No constant bound on SC17 is summable over infinitely many separated blocks.
The quantitative physical-scale target should retain the available local
floor: if kappa(a) is the angle row and m_*(a) the covering multiplicity,
the sufficient assembly budget is kappa(a)<1 together with

    inf_a gamma_min(a) [1-kappa(a)] / m_*(a) > 0.

A scale-independent margin below one is stronger than this requirement.
All gamma values here already contain the physical epsilon(a). Changing to
blocks of fixed physical diameter also changes their lattice link count;
the fixed-ell ultraviolet comparison and that physical block construction
must not be identified without the actual coarse/source maps.
The present derivation stops at this connected spatial estimate, after
proving the all-coupling bounds above; it does not stop at BA26's small
Haar-activity obstruction or at the existence of a charged inverse.

The user's Jaffe-Witten guidance states the remaining target in section
6.5, page 11: "One must then verify the existence of limits of appropriate
expectations of gauge-invariant observables as the lattice spacing tends
to zero and as the volume tends to infinity."
