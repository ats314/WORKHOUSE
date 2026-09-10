# SC17 consequence: actual infinite-volume physical Euclidean-time semigroup

Mathematical continuation, 2026-09-09, independently reviewed. This is an analytic derivation from the proved
SC17 Hessian rows and the actual thermodynamic score limit; it is not a
new Lean certification. All kinetic metrics below are the unit-S3
metrics, with fixed epsilon>0 and fixed lattice spacing.

## P1. Inputs and result

Use the actual finite-volume Hamiltonians

    H_Lambda=-epsilon sum_e Delta_e+sum_p J_p s_p,
    0<=J_p<=epsilon lambda,
    F_(e,Lambda)=grad_e log Omega_Lambda,
    mu_Lambda=Omega_Lambda^2 dU.

The established SC17 and thermodynamic continuation supply:

1. Uniform raw derivative matrix bounds

       h_(ei,Lambda)=sup_U ||X_i X_e log Omega_Lambda||op,
       h_(ee,Lambda)<=b,
       sup_e sum_(i!=e) q^d(e,i) h_(ei,Lambda)<=S,
       B=b+S<=1/3,
       sup_U |F_(e,Lambda)|<=3lambda.                    (P1)

   For e!=i, h_(ei,Lambda)=h_(ie,Lambda), since derivatives on different
   links commute and the two matrices are transposes. The diagonal
   bound concerns the raw derivative of the coefficient vector F_e.

2. The finite free-box laws, extended by Haar measure on the exterior,
   converge to the actual probability mu on M=product_e SU(2). The
   periodic finite-box laws have the same limit.

3. For every fixed link e, the finite free-box scores, extended as
   cylinder functions, converge uniformly on M to a continuous
   F_e. The periodic scores have the same local uniform limit. In
   particular |F_e|<=3lambda. The proof is the companion
   [thermodynamic note's uniform score limits](wilson-sc17-thermodynamic-limit.md#uniform-score-limits-discharge-the-form-constructions-local-input),
   including its endpoint coupling-continuity argument.

4. The limiting integration-by-parts identity is

       int X_e^a f dmu=-2 int f F_e^a dmu                (P2)

   for every smooth cylinder f. Its closed gradient form, initially
   on smooth cylinders, is

       E_mu(f,g)=epsilon sum_(e,a) int X_e^a f X_e^a g dmu.

   Write K_mu for its nonnegative self-adjoint generator. Cylinders
   lie in D(K_mu), with

       K_mu f=-epsilon sum_e(Delta_e f+2F_e.grad_e f).   (P3)

   This is a generator-domain assertion, not an operator-core assertion.

For each fixed 0<=lambda<lambda_c one may freeze q>1,b,S at any
positive upper endpoint below lambda_c. Thus all following assertions
hold throughout the optimized SC17 open interval, including uniformly
lambda<=1/73 using q=1025/1024. Sections P2-P8 prove:

* A unique strong infinite product SU(2) diffusion with actual score F.
* Convergence, in a weighted path metric, of stationary free and
  periodic finite-volume ground-transformed processes.
* Convergence of all bounded continuous cylinder multitime vacuum
  correlations, at fixed physical Euclidean times.
* Identification of this diffusion semigroup with exp(-t K_mu).

The last identification uses regular Dirichlet-form representation,
coordinate martingales, and SDE uniqueness. It does not assume that
smooth cylinders form an operator core. P9 gives a further endpoint
extension using a nonexponential summable weight.

## P2. A limiting influence kernel and weighted Lipschitz estimate

Fix a free-box exhaustion. For any finite box the ground score is
independent of all exterior variables, so set h_(ei,Lambda)=0 when
either coordinate does not enter that ground. Choose the auxiliary
ambient torus sufficiently large that the distances between the
finitely many nonzero coordinates equal infinite link-graph distances.
The available finite-volume SC17 estimate therefore gives P1 using
the infinite graph metric for these free-box scores.

For all e,i set

    a_ei=liminf_Lambda h_(ei,Lambda).

Then a_ei>=0, a_ei=a_ie, and Fatou's lemma gives

    sup_e sum_i q^d(e,i) a_ei<=B.                        (P4)

No convergence of the actual Hessians is assumed here. If U and V
differ only on link i, integrating the finite derivative along a
shortest geodesic on S3 and taking the uniform score limit gives

    |F_e(U)-F_e(V)|<=a_ei dist_S3(U_i,V_i).

Telescoping finitely many coordinate changes gives the corresponding
finite sum. Then use product continuity of F_e and the summable row
of a to take the limit over all coordinate changes. Consequently

    |F_e(U)-F_e(V)|
       <=sum_i a_ei dist_S3(U_i,V_i)
       <=(pi/2) sum_i a_ei |U_i-V_i|.                   (P5)

The last norm is chordal distance under the unit-quaternion embedding
SU(2)=S3 subset R4. The factor pi/2 is necessary globally, including
antipodal points.

Fix one link e0 and 0<alpha<log(q). Set

    w_e=exp[-alpha d(e,e0)],
    W=sum_e w_e<infinity,
    H_w=l2(E,w;R4), G_w=l2(E,w;R3).

Cubic link-graph balls have polynomial growth, so W is finite. The
subset M=product_e S3 of H_w is closed and compact. Its induced metric
has the product topology: finitely many coordinates control one part
of the metric, and summability of w uniformly controls the tail.

For the nonnegative matrix A=(a_ei), the unitarily transformed
matrix on unweighted l2 has entries a_ei sqrt(w_e/w_i). The weight
ratio is at most exp[alpha d(e,i)/2]<=q^d(e,i). P4 and symmetry give
both row and column sums at most B. The elementary Schur test gives

    ||A||_(l2(w)->l2(w))<=B,
    ||F(U)-F(V)||_G_w <= (pi B/2)||U-V||_H_w.           (P6)

The assumption alpha<log(q) is more restrictive than necessary;
alpha<=2log(q) also suffices for this estimate. Keeping the stated
strict choice avoids boundary bookkeeping.

## P3. A global extension with exact sphere invariance

Let T_1,T_2,T_3 be left multiplication by the imaginary unit
quaternions on R4. They are skew orthogonal matrices, T_a^2=-I,
and, for x in S3, the vectors T_a x form an orthonormal tangent
frame. For v in R3 and x in R4,

    |sum_a v_a T_a x|=|v||x|.                            (P7)

Kirszbraun's Hilbert-space extension theorem extends F from M to
H_w with Lipschitz constant at most pi B/2. Compose this extension
with the orthogonal projection of G_w onto the closed convex set

    C={v: |v_e|<=3lambda for every e}.

The projection acts coordinatewise and is 1-Lipschitz. The resulting
extension Ftilde remains globally Lipschitz with the same constant,
has |Ftilde_e|<=3lambda everywhere, and agrees with F on M. See
[Azagra--Le Gruyer--Mudarra, Theorem 1.2](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/kirszbrauns-theorem-via-an-explicit-formula/15797B44C630B0E2A4BB12547759929D)
for the Hilbert extension theorem and an explicit construction.

Define chi(x)=x/max(1,|x|), the Euclidean projection onto the closed
unit ball. It is radial, 1-Lipschitz, bounded by one, and equals x
on S3. Let the globally defined Hilbert drift be

    b_e(U)=-3epsilon U_e
           +2epsilon sum_a Ftilde_e^a(U) T_a chi(U_e).   (P8)

Using P7, split a product difference into a score difference and a
chi difference. This gives

    Lip(b)<=L_b=epsilon(3+6lambda+pi B).                 (P9)

Let the driving noise space be Q=l2(E x {1,2,3}), with independent
coordinate Brownian motions B_e^a. Define the noise map sigma(U)
on its unit vectors by

    sigma(U)_(e,a)=sqrt(2epsilon)
        [the H_w vector supported at e with value T_a U_e].

Its exact Hilbert--Schmidt bounds are

    ||sigma(U)||HS^2=6epsilon ||U||H_w^2,
    ||sigma(U)-sigma(V)||HS^2=6epsilon ||U-V||H_w^2.     (P10)

Thus the Hilbert Itô equation

    dU=b(U)dt+sigma(U)dB                                (P11)

has a unique global strong solution with continuous H_w paths for
every square-integrable initial condition. This follows directly
from the Picard iteration using the Hilbert Itô isometry, Doob's
inequality, and the global Lipschitz bounds. A primary general
existence/uniqueness theorem is
[Jentzen--Kloeden, Theorem 3.1](https://doi.org/10.1017/S0004972709000677).
Their strictly negative linear-operator convention is accommodated
by taking its A=-I and its nonlinear drift b+I; no smoothing or
unbounded linear operator is needed in this application.

It remains to prove that this extension generates a process on the
actual product of groups. For each coordinate e, Itô's formula gives

    d|U_e|^2
      =[-6epsilon|U_e|^2
        +4epsilon sum_a Ftilde_e^a U_e.T_a chi(U_e)
        +2epsilon sum_a |T_a U_e|^2]dt
        +2sqrt(2epsilon)sum_a U_e.T_a U_e dB_e^a
      =0.                                               (P12)

The score term vanishes because chi is radial and T_a is skew; the
other drift terms cancel exactly. Hence |U_e(t)|=|U_e(0)| for all t,
almost surely. Countability lets this hold simultaneously for every
e. Initial conditions in M remain in M, where P11 reduces to

    dU_e=sqrt(2epsilon)sum_a T_a U_e dB_e^a
         +[-3epsilon U_e
           +2epsilon sum_a F_e^a(U)T_a U_e]dt.           (P13)

In Stratonovich notation this is Brownian motion on each S3 with
drift 2epsilon grad log Omega, interpreted through the actual
limiting score. The Itô construction P8-P12 avoids assuming an
unproved infinite-dimensional manifold invariance theorem.

Uniqueness on M makes the restricted process independent of the
chosen extension. Lipschitz dependence on the initial condition
implies the Feller property on the compact state space M.

## P4. Uniform Hilbert convergence of the actual finite drifts

For a finite free box, extend the actual finite-volume score by
zero on exterior links and view it as a map F_Lambda on M. For
each fixed finite set D, uniform local score convergence gives

    sup_U sum_(e in D) w_e |F_(e,Lambda)(U)-F_e(U)|^2 ->0.

For the complementary links the uniform bound is

    sum_(e notin D) w_e |F_(e,Lambda)-F_e|^2
       <=36lambda^2 sum_(e notin D) w_e.

Therefore

    eta_Lambda=sup_(U in M)
          ||F_Lambda(U)-F(U)||G_w ->0.                   (P14)

Define the approximating process by the exact finite-dimensional
ground-transformed SDE on the box and independent Brownian S3
processes outside it. This is the finite process extended to M.
Its score drift is exactly P13 with F replaced by F_Lambda.
It has a unique solution on M, since the finite scores are smooth
on a compact finite product and the exterior is independent.

The same argument covers periodic finite boxes after labeling the
torus coordinates by a fundamental domain of infinite-lattice links.
For a fixed interior e, compare the periodic Hamiltonian to a large
central free box by switching its exterior plaquette coefficients
to zero. The uniform-score section of the thermodynamic note bounds their score difference
uniformly in every torus coordinate and sends it to zero as that
inner box recedes from e. Thus the periodic scores also satisfy P14.

A required distinction: periodic wrap interactions can destroy a
uniform Lipschitz constant for F_Lambda in an exponentially weighted
infinite-lattice norm. No such constant is used below. Only the
limiting drift must satisfy the uniform Lipschitz estimate.

## P5. Strong finite-time process comparison

Couple U^Lambda and U, initially in M, using the same coordinate
Brownian motions. Let

    D_t=U_t^Lambda-U_t,
    d0=E||D_0||H_w^2,
    delta_Lambda=2epsilon eta_Lambda,
    L_sigma^2=6epsilon.

On M, split the drift difference as

    b_Lambda(U^Lambda)-b(U)
       =[b_Lambda(U^Lambda)-b(U^Lambda)]
         +[b(U^Lambda)-b(U)].

The first term has norm <=delta_Lambda by P7 and P14. The second
has norm <=L_b||D||. Applying the elementary inequality for the
sum of three vectors, Cauchy--Schwarz to the time integral, and
Doob's L2 inequality to the stochastic integral gives, for t<=T,

    M(t)=E sup_(s<=t)||D_s||H_w^2
       <=3d0+6T^2 delta_Lambda^2
         +(6T L_b^2+12L_sigma^2) int_0^t M(s)ds.

Thus a completely explicit, deliberately coarse bound is

    E sup_(t<=T)||U_t^Lambda-U_t||H_w^2
       <=(3d0+24epsilon^2 T^2 eta_Lambda^2)
          exp[6T^2 L_b^2+72epsilon T].                 (P15)

The constants do not depend on the volume. No approximate-drift
Lipschitz constant occurs, so the periodic construction in P4 is
covered without a wrap-distance error.

## P6. Stationary path laws and actual multitime vacuum correlations

Extend each finite-volume law by product Haar measure on its
exterior. These laws converge weakly to mu on compact M. Compactness
implies convergence in the quadratic Wasserstein metric defined by
H_w distance. Choose initial couplings with d0->0, independently of
the common Brownian motions. P14-P15 then give convergence in
L2 of the path supremum metric on every fixed interval [0,T].

The finite extended processes are stationary and reversible.
Bounded continuous finite-coordinate multitime functions are
continuous functionals on path space, so their expectations
converge. Stationarity and time reversal therefore pass to the
limiting path law. In particular mu is invariant for P13, and its
Markov semigroup is symmetric on L2(mu).

The finite-volume generator of P13 is

    L_Lambda=epsilon sum_e(Delta_e+2F_(e,Lambda).grad_e)
            =-Omega_Lambda^{-1}(H_Lambda-E_Lambda)Omega_Lambda.

This is the exact physical-Hamiltonian ground transform. For
0=t0<=t1<=...<=tn and bounded multiplication observables O_j,

    E_(mu_Lambda) product_(j=0)^n O_j(U_(tj)^Lambda)
      =<Omega_Lambda,
          O_0 exp[-(t1-t0)(H_Lambda-E_Lambda)] O_1
             ... exp[-(tn-t(n-1))(H_Lambda-E_Lambda)] O_n
        Omega_Lambda>.                                 (P16)

This formula also covers complex observables by multilinearity;
the displayed brackets use the usual complex Hilbert inner product.
Exterior Haar factors cancel because the observables are supported
in a fixed interior set for all sufficiently large boxes.

Consequently the left side has a common free/periodic limit for
every finite collection of bounded continuous cylinder observables
and every fixed collection of physical Euclidean times.

## P7. Identification with the already closed gradient form

This step supplies the missing identification and avoids an
operator-core assumption.

First, mu has full support on M. For any finite coordinate set D,
the bound |grad_e log Omega_Lambda|<=3lambda gives, with exterior
coordinates fixed,

    osc_D log Omega_Lambda<=3pi lambda |D|.

Hence its conditional square-density relative to product Haar
is bounded below by exp[-6pi lambda |D|]. For any nonnegative
continuous cylinder f depending on D,

    int f dmu_Lambda
       >=exp[-6pi lambda |D|] int f dHaar_D.

Passing to the limit proves the same inequality for mu. Every
nonempty open cylinder therefore has positive mu measure.

The closed form E_mu is regular: smooth cylinders are a form core
by its definition, lie in C(M), and are uniformly dense in C(M)
by Stone--Weierstrass and finite-group smooth approximation.
It is strongly local. One precise way to pass locality from the
core is the Beurling--Deny decomposition of the regular closed form.
For nonnegative smooth cylinders f,g with disjoint supports the
core expression gives E_mu(f,g)=0. In that decomposition this
annihilates the integral of f(x)g(y) against the nonnegative jump
measure. Every distinct pair x,y in M admits disjoint cylinder
neighborhoods and nonnegative smooth cylinder functions supported
there; a countable collection of these neighborhoods covers the
off-diagonal of M x M. The jump measure therefore vanishes.
Also 1 lies in the core and E_mu(1,1)=0, so the killing measure
vanishes. The remaining form is strongly local. The same constant
function identity gives a conservative associated semigroup.

The regular strongly local Dirichlet-form representation theorem
now provides an associated mu-symmetric Hunt diffusion with continuous
M paths outside an exceptional starting set. It suffices to start
with law mu, which charges no such set. The standard representation
and Fukushima decomposition may be used here: the symmetric regular
case is contained in
[Ma--Ma--Sun, Section 2 and Theorem 2.4](https://arxiv.org/abs/1104.2951),
with the comparison form taken equal to E_mu.

There is no domain extrapolation in the following use of that
process. For each coordinate function f_(e,r)(U)=U_e^r, r=1,...,4,
and each product f_(e,r) f_(i,s), P3 already proves membership in
D(K_mu). Their generators are bounded continuous functions. Dynkin's
martingale formula (equivalently Fukushima's decomposition in this
generator-domain case) therefore gives

    M_e^r(t)=U_e^r(t)-U_e^r(0)-int_0^t b_e^r(U_s)ds.

The product formula gives the exact covariations

    <M_e^r,M_i^s>_t
       =2epsilon 1_(e=i) int_0^t
             [delta_(rs)-U_e^r(s)U_e^s(s)]ds.            (P17)

Indeed sum_a(T_a U)_r(T_a U)_s=delta_(rs)-U_rU_s on S3.
These are continuous martingales; bounded coefficients permit
localization removal on each finite time interval.

Set

    B_e^a(t)=(2epsilon)^(-1/2)
                int_0^t (T_a U_e(s)).dM_e(s).

P17 and tangent-frame orthonormality give

    <B_e^a,B_i^c>_t=1_(e=i)1_(a=c)t.

Every finite collection is a standard independent Brownian vector
by the continuous-martingale Levy characterization. These consistent
collections define the required cylindrical Brownian motion.
Moreover

    M_e=sqrt(2epsilon)sum_a int T_a U_e dB_e^a,

because the difference has identically zero quadratic variation:
I-U_e U_e^T is the tangent projection and P17 has no normal component.
Thus the associated Dirichlet-form diffusion solves exactly P13.

Its coordinate equations assemble into P11 in H_w: the state space
has bounded H_w norm sqrt(W), the drift is H_w bounded on M, and
the noise has finite Hilbert--Schmidt norm by P10. For example,
the sum of expected squared coordinate-martingale norms at time t
is 6epsilon Wt, which controls all finite-coordinate truncation
tails. This identifies the assembled stochastic integral; it does
not introduce an additional process assumption.

The globally Lipschitz Hilbert SDE has uniqueness in law, as follows
also directly from its Picard construction for every Brownian
driver and initial law. Therefore the associated Dirichlet-form
diffusion and the constructed process P13 have the same law when
started with mu. Their semigroups coincide as L2(mu) operators:

    P_t=exp(-t K_mu).                                    (P18)

For clarity about the logical role of uniqueness: merely exhibiting
a symmetric process with the same cylinder formula would not rule
out a different closed extension. Here the diffusion of the specified
closed form itself is proved to solve the uniquely solvable SDE.
That proves P18 without establishing or using essential
self-adjointness of the cylinder operator.

## P8. Physical restriction and the fixed-spacing time limit

Each actual finite model and its ground score are gauge covariant.
Their limiting measure, score, and gradient form retain this
covariance. Uniqueness of the Markov process, or P18 and invariance
of the form, shows that P_t preserves the closed gauge-invariant
physical subspace.

The already proved limiting Poincare estimate

    Var_mu(f)<=3 E_mu(f,f)/(4epsilon)

therefore belongs to the actual limiting physical Euclidean-time
semigroup, with

    ker K_mu=span{1},
    spec(K_mu) subset {0} union [4epsilon/3,infinity).

For a centered physical O in L2(mu),

    |<O,exp(-tK_mu)O>|<=exp(-4epsilon t/3)||O||2^2.

Together, P16 and P18 identify the limits of the finite physical
vacuum correlations with the previously constructed K_mu. This is
an actual thermodynamic physical-time identification at fixed
spacing and coupling. It does not identify any selected finite
excited shell, total source frame, continuum scaling map, or
continuum Yang--Mills Hamiltonian. No fifth stochastic-quantization
time or claimed time rescaling is involved in P16.

## P9. Endpoint extension by a summable nonexponential weight

The exponential weight construction P2 requires q>1 and therefore
does not apply with that weight at lambda=lambda_c. However, the
endpoint's proved q=1 row and its uniform score limit give enough
information for a different, explicit Hilbert weight. This is a
further valid consequence, not an exponential endpoint claim.

At lambda_c the same liminf construction gives a symmetric
nonnegative A with

    sup_e sum_i a_ei<=B=1/3.

Symmetry also bounds its l1 operator norm by B. Choose any strictly
positive summable sequence w0, for example exp[-d(e,e0)], and any
c>B, for example c=2/3. Define the l1-convergent nonnegative series

    w=sum_(n=0)^infinity (A/c)^n w0.                     (P19)

Its convergence and pointwise positivity are explicit:

    w>=w0>0,
    sum_e w_e <= (sum_e w0_e)/(1-B/c),
    Aw=c(w-w0)<=cw.

For an arbitrary real sequence x, weighted Cauchy--Schwarz followed
by Tonelli gives

    sum_e w_e (sum_i a_ei |x_i|)^2
       <= B sum_(e,i) w_e a_ei |x_i|^2
       = B sum_i (Aw)_i |x_i|^2
       <= Bc sum_i w_i |x_i|^2.                         (P20)

Thus ||A||_(l2(w)->l2(w))<=sqrt(Bc), and P5 gives

    Lip_(H_w->G_w)(F)<=pi sqrt(Bc)/2.

For c=2/3 this is at most pi sqrt(2)/6. The state space M remains
compact in this weighted Hilbert space because every w_e is positive
and sum_e w_e is finite. No comparison of w to an exponential is
asserted or needed.

Sections P3-P8 now apply with B in the Lipschitz constants replaced
by sqrt(Bc), using the already proved endpoint uniform local score
and measure convergence. In particular P14 needs only a summable
weight and the uniform per-link score bound, so it remains valid.
P15 again uses only the limiting drift Lipschitz constant.

Consequently the actual infinite-volume physical Euclidean-time
identification reaches the full closed bare-bootstrap interval
0<=lambda<=lambda_c. The exponential boundary/correlation rate
remains established only strictly below lambda_c. The endpoint
construction uses an influence-dependent auxiliary metric, not a
new spatial-decay estimate.

## P10. Exact scope and inputs still required for spatial continuum

This derivation uses actual finite-volume vacuum scores and their
proved uniform limits. It therefore removes the specific uncertainty
about whether the closed thermodynamic gradient generator governs
the limits of finite physical Euclidean-time correlations.

It supplies no new estimate for the background-reference defects
outside the bare SC17 interval. The spatial continuum trajectory
lambda proportional to g^(-4) is not contained in this interval.
Continuum matching still requires its actual interacting fast-sector
coercivity and full relative-form/pressure-Hessian estimates, plus
the relevant carrier/source maps. Those are not consequences of
changing the topology used to construct the fixed-spacing process.

No claim about arbitrary frozen gauge-breaking boundary conditions
is made; the finite-volume comparisons are the already proved free,
periodic, and gauge-invariant coefficient-cut constructions.
