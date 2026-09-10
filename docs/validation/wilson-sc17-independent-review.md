# Independent review of SC17 Hessian closure

Reviewer: sc17_cut_locality subagent, 2026-09-09.
Read `sc17-hessian-agent.md` in full and checked against the exact SC1-SC17
equations. No shared repository file edited. Verdict: the stated analytic
closure for lambda<=1/640 passes this independent review. This is not a
claim of a Lean formalization.

1. **Endpoint charges and raw frame.** X is left multiplication, Y is
right multiplication; [X_a,Y_b]=0. The equality
Y_b(X_a v)=sum_c O_cb(U) X_c(X_a v) differentiates no O coefficient.
It therefore gives equality of operator norms between the raw same-link
XX derivative matrix and its commuting LR matrix. The latter transforms
under independent adjoint representations at the distinct link endpoints.
The single-star Casimir shift 4epsilon/3 is applicable even for adjacent
endpoints. This does not incorrectly identify the same-tail neutral
representation with a charged one: the pointwise rotation itself changes
the covariance law while preserving the norm.

2. **Diagonal bound.** The potential LR second derivative has operator
norm<=4k; each first derivative has norm<=3lambda. Charged contraction
gives Q<=3lambda+18lambda^2 and subtracting the first-gradient tensor
product gives b<=3lambda+27lambda^2. The time-dependent proof uses the
same componentwise Markov evolution and the operator norm's convexity.

3. **Off-diagonal exact equation.** Anchors can be chosen distinct for
every distinct link pair. The two Killing fields commute, so SC2 has
exactly -V_ef+2epsilon<grad F_e,grad F_f>, with no curvature remainder.
For a sum index g at a reanchored link, its derivative matrix is the LR
matrix just bounded; elsewhere the reanchoring matrix is constant under
that g derivative. Thus no derivative-of-Ad term was dropped. The Gamma
contraction is a matrix product, and operator-norm submultiplicativity
gives sum_g h_eg h_fg with no factor of three.

4. **Weighted row.** h_ef=h_fe by commuting cross-link derivatives and
transpose-invariance of operator norm. The g=e and g=f terms total 2bS.
For all remaining g, q^d(e,f)<=q^d(e,g)q^d(g,f) bounds the convolution
by S^2. A link has 12 distinct plaquette-sharing neighbors for L>=3;
there is one plaquette for each such pair. The source row is 12kq.
The resulting Volterra inequality is precisely H1.

5. **Suprema and limit.** At fixed finite lattice, smoothness and compactness
make each supremum h_ef(T) and the finite row maximum S(T) continuous.
A first crossing of S=1/64 contradicts H1 because its right side is
strictly less than that barrier. No derivative of a maximizing point is
needed. Fixed-volume C2 ground convergence then passes the constant to
u; the constant is independent of volume before that passage.

6. **Exact arithmetic.** At lambda=1/640,
b=1947/409600<1/200. At q=17/16, the source is 51/2560. The barrier
slack is

    (4/3-4/200)/64 -2/64^2 -51/2560 =17/153600>0.

The auxiliary discriminant obstruction at lambda=1/64 is also exact:
mu=3439/3072 and mu^2-96lambda=-2329055/9437184.

7. **Block integration and assembly.** Parametrize each link's shortest
geodesic by a constant Killing generator of norm<=pi. A mixed rectangle
between disjoint B,C gives D_BC<=2pi^2 sum_(e in B,f in C)h_ef. Three
links per tail block therefore give kappa<=6pi^2 S, hence
kappa<=3pi^2/32<15/16 using pi^2<10. SC15's true conditional floor
3epsilon exp(-18pi lambda) and BA6/assembly then give exactly the gap
and approximate-tensorization bounds printed in the note.

8. **Norm convention to state explicitly.** The new connected SC17
pointwise bound is in 3x3 matrix operator norm. If it is translated into
the old Euclidean tensor/Frobenius norm, multiply the displayed entry
envelope by at most three. The block-geodesic argument correctly uses
operator norm directly, so its constants remain unchanged.

9. **Boundary of the result.** The all-time bootstrap is restricted to
the stated coupling window. The bare positive source term 12lambda q
and the scalar barrier discriminant really do prevent this particular
absolute-norm comparison from extending to lambda tending to infinity.
The review does not turn that failure of a majorant into failure of the
actual signed Hessian equation or the continuum program.

## Additional corollaries independently checked

10. **Actual weighted curvature.** For the bi-invariant link metric,
the Levi-Civita term is one half of the Killing-field bracket, so the
covariant same-link Hessian is exactly the symmetric part of the raw
XX matrix. Its operator norm is at most b. Product mixed-link connection
terms vanish. Symmetry of the off-diagonal matrix blocks and
2|v_e||v_f|<=|v_e|^2+|v_f|^2 then give

    ||Hess u||op <= b+S <=1/200+1/64=33/1600.

Each unit S3 factor has Ricci tensor 2I; the weighted Ricci tensor of
mu=exp(2u)dU is therefore

    Ric-2Hess u >=2(1-b-S)I >=(1567/800)I.

Fixing any outside links leaves a full compact product of SU2 groups,
not a chart with a boundary. Its conditional log density has the
corresponding principal Hessian restriction and the same lower curvature
bound rho=1567/800. Integrated Bochner thus proves the joint, marginal
(by restriction to marginal functions), and all conditional Poincare
inequalities in unscaled gradient units. Multiplication by epsilon gives
the corresponding H-E0 gap floor rho epsilon. Full-space positivity
restricts to the gauge-invariant subspace.

11. **Sharper true single-link angle.** Fix the outside of e,f. Let p(x,y)
be their actual smooth positive conditional density, F=F(x), and
TF(y)=E[F|y]. Differentiate the normalized conditional integral; precisely

    grad_y TF=2Cov_(x|y)(F,grad_y u).

For a unit tangent v at the fixed y, the scalar score v.grad_y u has
x-gradient bounded by h_ef in norm, because this is a mixed product
Hessian and the v direction is fixed with respect to x. Conditional
Poincare gives Var_(x|y)(v.grad_y u)<=h_ef^2/rho. Cauchy-Schwarz then
gives |grad_y TF|^2<=4h_ef^2 Var_(x|y)(F)/rho. There is no factor of three:
the vector norm is the supremum over unit v of the same directional
bound. The normalizing derivative was retained as the covariance.

The marginal y law inherits Poincare constant rho from the true joint
law by applying the joint inequality to functions depending only on y.
For A=Var(TF), W=Var(F), total variance therefore gives

    A <=(4h_ef^2/rho^2)(W-A),
    c_ef <=2h_ef/sqrt(rho^2+4h_ef^2)<=2h_ef/rho.

The argument begins with smooth F, for which differentiation under the
integral is justified on the compact group. Smooth functions are dense
in the positive smooth marginal L2 space and conditional expectation is
an L2 contraction, so the bound extends to the full operator norm. Its
centered operator norm is exactly the pair's maximal correlation, hence
the two-conditional-projection angle. Disintegration over outside values
preserves the uniform bound; physical restriction cannot increase it.

Consequently

    kappa_links <=2S/rho=25/1567,
    C_AT <=1567/1542,
    gap_phys H >=3epsilon exp(-6pi/640)*(1542/1567)
                 >(57/20)epsilon.

For the last fully rational floor, pi<22/7 and exp(-x)>=1-x give the
lower ratio 3*(1087/1120)*(1542/1567)=5028462/1755040. Its difference
above 57/20 has positive cross-multiplied numerator 531960. The inputs
are the actual vacuum Hessian bounds and actual conditional laws; no
frozen-boundary Hamiltonian gap or assigned covariance is substituted.
## Adversarial review of the time-dependent charged contraction

The decisive estimate survives the nonlinear drift and endpoint changes. Fix any finite physical-time interval. The positive heat solution makes v_T smooth, and gauge invariance follows from gauge invariance of H and the initial constant. No uniform derivative estimate for v_T is used to establish existence on this finite interval.

At a selected vertex x,

    -K_res,T = epsilon[Delta-(1/6)sum_a(G_x^a)^2]
               +2epsilon grad v_T.grad.

The principal part is the sum of the outside-link Laplacians and

    (epsilon/6)sum_a sum_(i<j)(Z_i^a-Z_j^a)^2,

where Z_i are the six signed incoming/outgoing link fields. It is therefore a smooth diffusion generator with no killing; its time-inhomogeneous propagator is positive and preserves constants. The time-varying drift does not affect these Markov properties. Instantaneous self-adjointness relative to the changing density is not needed here, nor is preservation of one time-independent probability measure.

Every K_T and residual generator commutes with the gauge action, because the product metric and v_T are gauge invariant. Consequently their propagators preserve any fixed equivariant tensor sector. For a tensor with an adjoint charge at x, C_x=8 acting componentwise in the fixed Lie-algebra basis. On that sector,

    K_T=K_res,T+(4epsilon/3)I

for every T, and the scalar shift factors from the nonautonomous evolution. No commutation of the generators at different times is required. The residual propagator acts componentwise by a probability kernel, so Jensen applies to every convex norm on the finite-dimensional target, specifically the 3 by 3 matrix operator norm.

Only the Casimir at ONE endpoint is subtracted throughout this continuation. Therefore overlapping gauge stars do not require an allocation correction. This includes the adjacent endpoints of the same link. Same-link left and right multiplication fields commute, and their mixed tensor transforms in adjoint_tail tensor adjoint_head; L>=3 ensures the endpoints differ.

For the parabolic Q equation, the product-rule cross-gradient terms cancel exactly:

    partial_T Q=-K_T Q-V_XY-F_X tensor V_Y-V_X tensor F_Y.

For the H equation the retained forcing is -V_XY+2epsilon Gamma(F_X,F_Y). Both forcing tensors lie in the same chosen endpoint representation, so sector-preserving Duhamel applies. The endpoint rotations are used pointwise only after applying this estimate to the anchored tensor. Their variable coefficients are not pulled through K_T. In the Gamma norm bound their own-link derivative is the LR mixed tensor itself; different-link derivatives do not differentiate that link's rotation.

No counterexample or hidden physical-gap assumption was found in this contraction step. The finite-volume limit T to infinity is taken only after the bounds, and thus requires no uniform-in-volume ground-state convergence rate.

# Independent final review of Part III, R1-R14

Reviewer: sc17_cut_locality subagent. 2026-09-09.
Read `docs/derivations/wilson-sc17-spatial-closure.md` in full, with the
requested focus on its conditional Euclidean theorem. No core repository
files edited. Verdict: the identities, bootstrap constants, and angle
corollary pass this review under the explicitly stated regularity,
constant Euclidean kinetic metric, and actual-defect hypotheses. This
does not discharge those hypotheses for Wilson fibers.

## Algebra and signed projection

For D=partial_t-epsilon Delta-2epsilon grad u.grad, differentiating
the Euclidean logarithmic heat equation gives DJ=2epsilon J^2-V''.
Putting E=J+Omega gives exactly R1. For constant orthogonal Q,
the QQ block of Omega E+E Omega is AX+XA+BY*+YB*, and the QQ block
of E^2 is X^2+YY*. This checks every term of R2.

Applying D to QEQ gives the three cross-gradient terms in R3, each
with coefficient -2epsilon, besides (DQ)EQ and QE(DQ). A moving
reference adds D Omega. R13 and R14 have the same correct diffusion
product-rule signs. These computations use a constant Euclidean
kinetic metric; no compact-group curvature or moving-frame term is
implicitly included.

## Weighted Riccati bootstrap

The symmetric weighted Schur norm dominates operator norm and is
submultiplicative since its weight is submultiplicative. Taking the
configuration supremum separately in every entry makes it contractive
under a componentwise Markov transition. This stronger norm, rather
than the supremum of a pointwise matrix norm, is correctly used.

For A constant, left/right multiplication by exp(-2epsilon tau A)
commutes with every componentwise Markov transition, regardless of
whether A has entrywise positive exponential. Duhamel therefore gives

    M_T <= beta_s M_T^2 + beta_s delta/(2epsilon).

The time change t=2epsilon tau accounts for the factor 1/(2epsilon).
The discriminant is 1-2beta_s^2 delta/epsilon, and the two roots are
the stated [1 plus/minus sqrt(discriminant)]/(2beta_s). A continuous
M_T starting at zero cannot enter their open interval, so M_T<=r_-
for all times. This argument also covers delta=0, giving r_-=0.

Since the norm dominates operator norm,
beta_s>=integral exp(-2at)dt=1/(2a), where a=lambda_min(A).
The stated strict defect condition therefore implies
delta<2epsilon a^2 and r_-<1/(2beta_s)<=a. The potential Hessian is
globally positive, and the limiting log-vacuum curvature is at least
a-r_-. The ground-transformed gap 2epsilon(a-r_-) is correct. The
scalar calibration A=aI reproduces the exact oscillator root.

The entrywise-uniform estimate passes to the ground limit at each
fixed finite dimension by pointwise C2 convergence and preservation
of the uniform bounds; uniform convergence over the entire unbounded
configuration space is not needed for that final lower-semicontinuity
step. The preceding norm continuity on finite time intervals remains
an explicit hypothesis, as the proof states.

## Score-to-angle corollary

For actual density exp(-Phi), differentiation of the normalized
conditional expectation gives grad_C E[f|C]=-Cov(f,grad_C Phi).
The conditional B Poincare constant is 1/(2a_B). Directional score
variance is therefore at most 2h_BC^2/a_B, with no dimension factor:
the gradient norm is the supremum over unit C directions.

The marginal potential Hessian is

    E(Phi_CC)-Cov(grad_C Phi,grad_C Phi)
       >=2(a_C-h_BC^2/a_B)I.

Combining its Poincare constant with the preceding gradient bound
gives the coefficient h_BC^2/(a_B a_C-h_BC^2) multiplying the average
conditional variance. Total variance then yields maximal correlation
at most h_BC/sqrt(a_B a_C), exactly R10. Smooth approximation extends
the centered conditional expectation operator bound to L2.

For R11, a_B>=a_0-r and the off-block h row is at most a_0 kappa_A+r.
The strict condition 2r<a_0(1-kappa_A) ensures both positive block
curvature and every pair's strict hypothesis. Thus

    kappa_actual <=(a_0 kappa_A+r)/(a_0-r),
    gamma_min >=2epsilon(a_0-r),
    gamma_min(1-kappa_actual)
       >=2epsilon[a_0(1-kappa_A)-2r].

The block conditional floor here comes from the diagonal conditional
curvature, which can be stronger than the full-space reference
eigenvalue floor used in R9. No incorrect identification is needed.

## Assumptions to retain when applying the theorem

The Euclidean fiber must be complete R^n (or another setting with the
same conservative componentwise Markov evolution and proved boundary
conditions), rather than an unaccounted Dirichlet chart. Bounded
finite-time Hessians give at-most-linear, globally Lipschitz drift and
justify non-explosion in the stated Euclidean setting. The manuscript
already expressly excludes direct use across a Dirichlet chart boundary.

The R11 assembly uses a disjoint coordinate-block partition; an
overlapping cover would need its covering multiplicity and the actual
conditional projection geometry retained. The source-fiber coordinate
identification cannot be omitted. The actual conditional vacuum must
also be normalizable on each admissible fiber; the stated conditional
ground/semigroup hypotheses supply this in R5-R9.

For the normalized conditional derivatives and marginal Hessian,
assume the stated smoothness and justify differentiation under the
integral, or use the usual smooth truncation/weak-convexity argument.
Uniform mixed-Hessian bounds and strong conditional convexity provide
the needed linear score growth and Gaussian moment control. This is
not a Gaussian substitution for the actual conditional density.

Finally, the quantum pressure (H_out Omega)/Omega and every moving
projector/metric/cutoff term remain part of the actual defect. The
review does not certify a magnetic Hessian estimate as a bound for
that complete defect.


Final interval optimization checked by sc17_hessian_hierarchy:

## Maximized bare-Hessian bootstrap: a larger interval

The lambda<=1/640 result is a strong-gap corollary, not the maximal interval of H1-H2. Define

    b(lambda)=3lambda+27lambda^2,
    mu(lambda)=4/3-4b(lambda),
    D(lambda)=mu(lambda)^2-96lambda.

On the interval mu>0, D is strictly decreasing since

    D'(lambda)=2mu(lambda)(-12-216lambda)-96<0.

It starts positive and becomes negative before mu vanishes. Its unique zero in that interval is lambda_c, the first positive root of

    6561lambda^4+1458lambda^3-81lambda^2-72lambda+1=0.

Exactly, 1/73<lambda_c<1/72, because D(1/73)>0 and D(1/72)=-47/2304. Its numerical location 0.0137324181787834 is only a diagnostic; the polynomial and isolating interval define it exactly.

For every 0<lambda<lambda_c, set

    q=(1+mu(lambda)^2/(96lambda))/2 >1,
    s=mu(lambda)/4=1/3-b(lambda).

Then the invariant-barrier slack is exactly

    mu s-2s^2-12lambda q =D(lambda)/16>0.

Consequently the actual exponential Hessian row estimate holds with this q and s at every volume and physical time. Furthermore b+s=1/3, so the actual conditional curvature and assembled constants satisfy

    rho>=4/3,
    kappa_links<=(3/2)s=1/2-(3/2)b,
    C_AT<=2/(1+3b)<2,
    gap_phys(H)>= (4/3)epsilon.

The displayed direct Bochner gap is stronger near lambda_c than the simple SC15-plus-angle lower bound. That separate valid assembled bound is

    gap_phys(H)>=(3epsilon/2)(1+3b)exp[-6pi lambda].

At lambda=0 the exact Haar conclusions apply separately. For every fixed upper endpoint strictly below lambda_c one can freeze b,q,s at that endpoint to obtain constants valid throughout the entire smaller interval. The exponential rate degenerates as the endpoint approaches lambda_c.

At lambda=lambda_c, the unweighted choice q=1 and the same s still satisfies the nonstrict Volterra barrier: at a first finite-time crossing the integral is strictly smaller than s owing to its initial zero value. This supplies an unweighted summable row, approximate tensorization, and gap at the endpoint, but not a positive exponential weight by this argument. Beyond lambda_c there is no s>0 satisfying H2 for any q>=1 while mu>0; once mu<=0 a positive scalar barrier is also impossible. This is the exact ceiling of this bare absolute-Hessian bootstrap, not a claimed ceiling for the actual Yang-Mills estimates.

### Explicit rational larger-window corollary

A convenient uniform choice throughout 0<=lambda<=1/73 is

    b_*=246/5329,
    q=1025/1024,
    s=2/7.

Its exact slack and resulting constants are

    (4/3-4b_*)s-2s^2-12(1/73)q =77375/200540928 >0,
    rho=2(1-b_*-s)=49846/37303 >4/3,
    kappa_links<=2s/rho=10658/24923,
    C_AT<=24923/14265 <7/4,
    gap_phys(H)>=(49846/37303)epsilon >(4/3)epsilon.

The independent direct-assembly expression is

    gap_phys(H)>=3epsilon exp[-6pi/73]*(14265/24923).

The lambda<=1/73 interval is more than 3506 times wider than the previous 1/256000 window. The exact maximal open exponential interval is lambda<lambda_c, so the rational endpoint is chosen for readability rather than claimed optimality.


## Thermodynamic and infinite-form continuation review

The root task reconstructed the cut-response and infinite-form arguments
against the independently developed sc17_cut_locality and
sc17_gaussian_baseline notes on 9 September 2026.

The differentiated normalized ground equation is Kv=-(W-mu(W)); its gradient
retains +2epsilon H grad(v). The spatially weighted charged semigroup has
rate epsilon(4/3-2B), with B=b+S<=1/3. Its score response is therefore bounded
by 6lambda q^-distance. The exact covariance integral contributes a second
inverse rate and the density derivative contributes a factor two, giving
18lambda times the local observable gradient sum, with no boundary-area
factor. All interpolations retain gauge-invariant plaquette coefficients in
[0,k]; arbitrary frozen gauge-breaking boundary values are outside the claim.

The finite-volume normalized scores differ uniformly by the integrated
score response. This proves continuous quasilocal score limits before the
integration-by-parts passage. At lambda_c, the q=1 response bounds the score
change by 6 times the coupling change and the expectation change by 18 times
the coupling change times the observable gradient sum. Approximation from
below gives both limits at the endpoint without an exponential boundary rate.

For the infinite form, each adjoint test uses a bounded limiting score and
a dense smooth cylinder function. This proves closability component by
component in the Hilbert direct sum. The finite-volume full Poincare bound
passes on cylinders by local expectation convergence, then on the form closure.
The operator action is proved on cylinders by the representation theorem;
no unjustified operator-core assertion or global density Omega_infinity is used.
Gauge averaging is a form contraction and gives the physical restriction.

For the plaquette, conditional density oscillation is at most 24pi lambda.
Haar variance 1/4 gives actual variance at least exp(-24pi lambda)/4; its four
link gradients give energy at most 4epsilon. The spectral first-moment bound
at M=32epsilon exp(24pi lambda) leaves mass at least exp(-24pi lambda)/8
in the stated interval. This is nonzero interval overlap, not an isolated
complete-shell rank or a matched source frame. The subsequent physical-time
extension below resolves its distinct multitime correlation identification.

## Physical-time extension and endpoint review

The cut-locality reviewer derived the actual limiting dynamics in
[the physical-time note](../derivations/wilson-sc17-physical-time-limit.md).
The root and an independent Hessian-hierarchy reviewer checked its proof.
The liminf Hessian influence kernel preserves each coordinate Lipschitz
inequality; Fatou preserves its symmetric row bound. For q>1 the weighted
Schur estimate yields a globally Lipschitz score in a summable Hilbert metric.
At q=1, w=sum_n(A/c)^n w0 is positive and summable, Aw<=cw, and weighted
Cauchy-Schwarz gives ||A||_(l2(w))<=sqrt(Bc). This includes lambda_c.

The quaternion SDE preserves each unit sphere by exact Ito cancellation.
P15's process comparison uses the limiting drift's Lipschitz constant and
uniform score convergence; it does not assume a volume-uniform weighted
Lipschitz constant for periodic wrap interactions. P17-P18 use coordinate
and coordinate-product functions already in the specified closed generator's
domain. Their martingales reconstruct the Brownian drivers of that unique
Hilbert SDE and identify exp(-t K_mu) without an operator-core claim.
Thus free/periodic bounded continuous cylinder multitime vacuum correlations
converge to the actual fixed-spacing physical-time semigroup. No spatial
continuum or complete-shell matching hypothesis is imported by this result.


## Supplied Lean arithmetic: compilation, axiom audit and graph registration

The user supplied eight additional lemmas during this continuation: two
Brownian-slab budgets and six SC17 rational/polynomial budgets. This task
registered each against its actual proof document with promotes=[]; it did
not attribute these supplied formalizations to its analytic derivation.

A local replay of lake build --wfail completed successfully with 3034 jobs.
#print axioms for all eight compiled lemmas returned only propext,
Classical.choice and Quot.sound. The raw build and axiom logs are retained
alongside this review. The only Basic.lean change by this task was correcting
one comment to say approximate-tensorization constant. No analytic operator,
Markov, thermodynamic, conditional-score or continuum theorem was silently
promoted through these arithmetic lemmas.

## Final active control census

The original eight controls were supplemented at 16:28 by a supplied ninth
control, `_massless_reference_row`, on a 3x3 periodic scalar lattice. The root
read and replayed it during final validation. It checks the exact square-root
row identity, off-diagonal negativity at m=1/10, and the symbolic m-to-zero
limit. The all-m negativity follows separately from the heat representation
in the analytic note; this finite check does not identify physical SU2
conditional angles. References above to eight controls describe the original
package. The final active suite has nine passing controls, and its registration
test gives ten focused invariant tests. This is distinct from the eight
supplied compiled Lean lemmas.
