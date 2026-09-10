# SC17: connected spatial closure and the signed background continuation

9 September 2026. This continues SC17 in
[the background covariance derivation](wilson-background-covariance-continuation.md).
The actual finite periodic cubic SU(2) Hamiltonian is
\(H=-\epsilon\Delta+k\sum_p(1-\operatorname{Tr}U_p/2)\), with the product
unit-S3 metric, side length L >= 3, epsilon > 0 and lambda=k/epsilon.
Let Omega be its positive normalized ground state, with energy E0; set
Z_T=exp(-T H)1, v_T=log Z_T, u=log Omega and
K_T=-epsilon(Delta+2 grad v_T.grad). Compact ellipticity gives these smooth
objects at every fixed finite volume. T is physical imaginary time.

For every \(0\le\lambda\le1/73\), the derivation below proves

\[
\sup_e\sum_{f\ne e}(1025/1024)^{d(e,f)}
 \|\nabla_f\nabla_e\log\Omega\|_{\infty,\mathrm{op}}\le2/7.
\]

The distance is in the link graph joining links which share a plaquette.
The norm is the 3 by 3 matrix operator norm. All constants are uniform in
finite lattice volume, configurations and preceding physical projection time.
For the true vacuum law \(\mu=\Omega^2dU\), this gives

\[
\kappa\le10658/24923,\qquad C_{\rm AT}\le24923/14265<7/4,\qquad
\operatorname{gap}_{\rm phys}H\ge(49846/37303)\epsilon>4\epsilon/3.
\]

The exact maximal open exponential interval of this bootstrap is
\(0\le\lambda<\lambda_c\), where \(1/73<\lambda_c<1/72\) is the root of
\(6561\lambda^4+1458\lambda^3-81\lambda^2-72\lambda+1=0\) in that interval.
The explicit rational corollary enlarges the earlier proved coupling interval
by more than a factor of 3506. On the narrower lambda<=1/640 interval, the
stronger weight 17/16, row 1/64, C_AT<=1567/1542 and gap>57epsilon/20 hold.
The [thermodynamic continuation](wilson-sc17-thermodynamic-limit.md) then
constructs the canonical local vacuum law, the closed infinite-volume
ground-law generator with gap at least 4epsilon/3, and an explicit positive
plaquette spectral weight in a bounded energy interval. Its fixed-coupling
limit extends to lambda_c by continuity. Exponential spatial rates are
asserted only below lambda_c.
These are analytic proofs with an independent review. Eight registered exact
controls check the algebra and constants stated in their individual names;
six supplied Lean lemmas also certify their stated rational/polynomial
budgets. The eight new parallel-work lemmas, including two earlier slab
budgets, were compiled with `lake build --wfail` and mapped in the theorem
ledger. They do not constitute a Lean formalization of the analytic proofs.
The continuum trajectory lambda tending to infinity remains outside this
interval. Parts II and III derive the actual Gaussian obstruction and a
signed remainder criterion, including its still unproved quantum inputs.

## Part I. Actual SC17 closure

## Endpoint reanchoring removes the neutral obstruction for norm bounds

Let X_e be left-multiplication Killing derivatives and Y_e right-multiplication derivatives. X_e and Y_e commute even on the same link. They carry adjoint charges at the tail and head, respectively. If e != f, replacing X_e by Y_e rotates H_ef=X_f X_e v_T by Ad(U_e), so its matrix operator norm is unchanged. Any two distinct links have a choice of endpoints which are distinct (L >= 3); thus choose derivative anchors with distinct gauge charges.

For the same link, Y_e^b X_e^a v_T=sum_c O_e(cb) X_e^c X_e^a v_T for a pointwise orthogonal matrix O_e. This is equality of differential operators applied in the indicated order: the coefficients of Y are not differentiated. Hence the entire raw diagonal derivative matrix has the same operator norm as the commuting LR mixed matrix. Its two charges lie at distinct endpoints. No assertion that the original same-tail representation lacks a singlet is needed.

SC4 applies to every chosen pair of commuting Killing derivatives, including same-link LR. The single-star charged damping is m=4 epsilon/3. Every first derivative, under either anchoring, has norm at most 3 lambda. A single plaquette's mixed matrix has operator norm at most k: for unit Lie vectors, the second derivative is a normalized trace of a product with two unit operator-norm Lie vectors and otherwise unitary factors. Every link meets four plaquettes. Consequently

    b := sup_e,T,U ||X_e X_e v_T||op <= 3 lambda+27 lambda^2.

The LR proof gives (3/(4 epsilon))*4k+18 lambda^2 for the Omega-normalized second derivative Q, followed by at most 9 lambda^2 for subtraction of the first-derivative product.

## Why the charged contraction survives the time-dependent drift

At one selected endpoint x let G_x=sum_i Z_i be its six signed incident
link generators and C_x=-sum_a(G_x^a)^2. Gauge invariance of v_T and the
product metric makes K_T commute with the gauge action. The residual
generator -K_res,T=-K_T+(epsilon/6)C_x has principal part

    epsilon Delta_outside
      +(epsilon/6)sum_a sum_(i<j)(Z_i^a-Z_j^a)^2

and smooth drift 2epsilon grad v_T.grad. It has no killing term. At every
fixed finite volume and on every compact time interval this is a genuine
smooth diffusion generator, even if its principal part is degenerate.
Its time-inhomogeneous propagator is positive and preserves constants.
Instantaneous symmetry with respect to a changing density is unnecessary
for this probability-kernel statement.

An anchored tensor with adjoint charge at x satisfies C_x F=8F componentwise
in the fixed Lie-algebra basis. Its representation is preserved by every
instantaneous generator. On that sector K_T=K_res,T+(4epsilon/3)I for all T,
so the scalar damping factors out of the propagator exactly. This requires
no commutation between generators at different times. Jensen for the residual
probability kernel contracts the matrix operator norm and gives

    ||P_(T,s) F||infty,op <=exp[-4epsilon(T-s)/3]||F||infty,op.

Only ONE star is subtracted. The selected endpoint and the tensor's other
endpoint may therefore be adjacent, including the same-link LR case.
Apply the evolution estimate to the actual anchored tensor before using
the pointwise frame rotation; no variable rotation is commuted through K_T.
With F_X=Xv_T, commuting Killing fields X,Y give exactly

    (partial_T+K_T)(XYv_T)=-XYV+2epsilon Gamma(F_X,F_Y),
    (partial_T+K_T)Q=-XYV-F_X tensor YV-XV tensor F_Y.

The second equality follows by adding F_X tensor F_Y and the diffusion
product rule. Both forcing tensors retain the chosen endpoint charge.
This proves the charged Duhamel step used below without a physical-gap
assumption or an assumption that the unknown drift is spatially local.

## Actual weighted Volterra inequality

For distinct e,f set h_ef(T)=sup_U ||X_f X_e v_T||op and use h_ee(T)<=b. Select the endpoint anchors above for the given pair. The exact SC2 parabolic equation and charged Duhamel contraction give

    h_ef(T) <= int_0^T exp[-m(T-s)]
       [ k n_ef + 2 epsilon sum_g h_eg(s)h_fg(s) ] ds,

where n_ef is the number of plaquettes containing both links. This is the actual signed Hessian equation; there is no inserted mass or reference covariance.

To verify the nonlinear norm estimate, at each g the Gamma contraction is a product of two 3 by 3 derivative matrices. Operator norms are submultiplicative. If a first derivative was reanchored, for g different from its own link this just rotates the original mixed matrix; for its own link the derivative is precisely the commuting LR matrix already bounded by b. Thus no omitted derivative-of-Ad term occurs, and no extra dimension factor is needed.

Use the link graph with adjacency when two different links share a plaquette, and distance d. Every cubic link has exactly 12 distinct neighbors, also for L=3. Let q>1 and

    S(T)=max_e sum_(f != e) q^d(e,f) h_ef(T).

Triangle inequality for graph distance, and separating g=e,f, give

    S(T) <= int_0^T exp[-4 epsilon(T-s)/3]
        epsilon [12 lambda q +4 b S(s)+2 S(s)^2] ds.       (H1)

At fixed finite volume S is continuous and S(0)=0. Therefore every s>0 satisfying

    12 lambda q +4 b s+2s^2 < (4/3)s                     (H2)

is an invariant barrier: at a first crossing S(T)=s the right side of H1 is at most s(1-exp[-4 epsilon T/3]), a contradiction. This proof avoids a differentiability assumption on the maximizing configuration or row.

## Explicit new regime

Take lambda<=1/640, q=17/16 and s=1/64. Then

    b <= 1947/409600 < 1/200,
    12 lambda q <= 51/2560,
    (4/3-4/200)/64 - 2/64^2 - 51/2560 = 17/153600 > 0.

It follows, uniformly in volume, physical time and configurations, that

    max_e sum_(f != e) (17/16)^d(e,f) ||X_f X_e v_T||op <=1/64,
    ||X_f X_e v_T||op <= (1/64)(16/17)^d(e,f).

Fixed-volume smooth ground convergence passes the same estimates to u=log Omega. Therefore the actual SC17 connected charged-resolvent combination has this distance envelope (the negative of H_ef for non-neighbor pairs).

For the exact disjoint three-link tail blocks, finite geodesic rectangle integration of 2u gives

    D_BC <= 2 pi^2 sum_(e in B,f in C) h_ef.

Thus the physical block-angle row obeys

    kappa <= 6 pi^2/64 =3 pi^2/32 <15/16.

The true conditional floor SC15 is gamma_B>=3 epsilon exp[-18 pi lambda], and the established block assembly gives

    gap_phys(H) >=3 epsilon exp[-18 pi lambda]*(1-3 pi^2/32)
                > (3 epsilon/16) exp[-18 pi/640].

The same local log-oscillation bounds each block conditional density ratio by exp[18 pi lambda]. Product-Haar tensorization inside each three-link block then gives the original single-link approximate tensorization constant

    C_AT <= exp[18 pi lambda]/(1-3 pi^2/32)
          <16 exp[18 pi/640].

This is an explicit 400-fold enlargement of the previous lambda<=1/256000 window. It is a true vacuum-law estimate, not just a conditional reformulation of the desired conclusion.

## Exact wall for this majorant

At the identity configuration, each off-diagonal mixed potential matrix for a plaquette-sharing pair equals plus or minus k I, and every row has 12 distinct such pairs. Thus 12 lambda q is the exact weighted source row, not merely a loose volume estimate. Even granting b=0, the maximum of (4/3)s-2s^2 over s>=0 is 2/9. The scalar barrier H2 therefore requires

    lambda <1/(54 q).

If this same one-link weighted row is also used to force the physical block-angle criterion, it needs s<1/(6 pi^2). Even granting b=0, its source budget requires

    lambda < q^(-1)[1/(54 pi^2)-1/(216 pi^4)].

Hence this bare, absolute matrix majorant cannot remain valid along lambda=(c_B/c_E)g^(-4)->infinity. A background subtraction must change the actual signed equation/source and control the resulting quantum remainder; changing q or the slab length does not address that obstruction. The construction has nevertheless discharged the missing distance decay for a strictly larger, explicit interval.

With the particular proved diagonal bound b=3 lambda+27 lambda^2, the exact scalar discriminant condition is stronger:

    mu=4/3-4b >0,
    mu^2-96 lambda q >0.

At lambda=1/64, mu=3439/3072 and, even at q=1,

    mu^2-96 lambda = -2329055/9437184 <0.

Thus this specific bootstrap cannot pass lambda=1/64. This is failure of the proposed absolute norm comparison, not failure of the actual Hessian estimate or of Yang-Mills theory. Retaining a signed negative Gaussian Hessian on a genuine background domain could increase its linear damping. Such a modified argument must retain the actual reference's complete low-frequency sector and control the true ground-state remainder; replacing the bare diagonal by a postulated negative matrix would not be a proof.

## Actual-vacuum curvature corollary

For a bi-invariant S3 link metric, the Riemannian Hessian on a single link is the symmetric part of its raw Killing derivative matrix:

    Hess_e u(a,b)= (X_a X_b u+X_b X_a u)/2.

Indeed the Levi-Civita derivative of invariant fields is half their bracket. Cross-link connection terms vanish. Thus the diagonal block norm is at most b, while the off-diagonal block norms are h_ef=h_fe. The block Schur test and the established row estimate give

    ||Hess u||op <= b+S <=1/200+1/64=33/1600.

Product unit-S3 Ricci curvature equals 2I, so the actual vacuum density exp(2u) has

    Ric-2 Hess u >= rho I,  rho=1567/800.

This holds on the full product and on every frozen conditional subset, with the same rho. It uses the actual derived ground-state Hessian, not curvature positivity of a quotient or a postulated background law.

For the dimensionless weighted Laplacian L=Delta+2 grad u.grad, integrated Bochner gives

    int (Lf)^2 dmu =int [||Hess f||HS^2+(Ric-2Hess u)(grad f,grad f)]dmu
                   >=rho int |grad f|^2dmu.

Apply this to any nonconstant eigenfunction of -L on the compact connected product (positive smooth density) to obtain gap(-L)>=rho. Consequently both the full and physical Hamiltonian gaps are at least rho epsilon. The same proof gives every true conditional block gap at least rho epsilon.

## Sharper projection angles via covariance and the derived conditional gaps

This strengthens the geodesic mixed-density-ratio estimate. Fix any outside configuration and two distinct links e,f. Let nu be their actual conditional joint law and h=h_ef. The joint law and every one-link conditional law have dimensionless Poincare constant at most 1/rho by the previous paragraph. Its f-marginal also has constant at most 1/rho: apply the joint Poincare inequality to functions depending on f alone.

For a smooth scalar a=a(U_e), set Ta(U_f)=E_nu[a|U_f], W=Var_nu(a), and A=Var_nu(Ta). Differentiating the normalized conditional density gives exactly

    grad_f Ta=2 Cov_(e|f)(a,grad_f u).

For each fixed unit tangent v at U_f, conditional Poincare applied to v.grad_f u gives

    Var_(e|f)(v.grad_f u) <= h^2/rho.

The bound is uniform in v, so covariance Cauchy-Schwarz and duality of the Euclidean gradient norm yield

    |grad_f Ta|^2 <= (4h^2/rho) Var_(e|f)(a).

Applying the f-marginal Poincare inequality and the law of total variance gives

    A <= (4h^2/rho^2) E Var_(e|f)(a)
      = (4h^2/rho^2)(W-A).

Thus the maximal correlation, which is exactly the norm of E_e E_f-E_{ef} on that conditional fiber, satisfies

    c_ef <= 2h/sqrt(rho^2+4h^2) <=2h/rho.

Smooth functions are dense, so the inequality extends to the full L2 projection norm. Taking the essential supremum over outside values yields the unrestricted angle bound; restricting to physical functions cannot increase it. Therefore

    kappa_links <=2 S/rho =25/1567,
    C_AT <=1/(1-kappa_links)=1567/1542 <51/50.

This is the original single-link approximate tensorization inequality, without a block-density comparison factor. Combining it with the stronger available single-link SC15 floor gives

    gap_phys(H) >=3 epsilon exp[-6 pi lambda]*(1542/1567)
                 >=3 epsilon exp[-3 pi/320]*(1542/1567)
                 > (57/20)epsilon.

The final rational simplification follows from pi<22/7 and exp(-x)>1-x. The nonsimplified expression is the stronger statement. The earlier direct Bochner gap and three-link angle estimate remain valid consequences but are weaker than this assembled bound in the displayed regime.

For the requested sharper simple lower floor, the exact rational check is

    3*(1542/1567)*(1-33/1120)-57/20 =13299/877520 >0.

Therefore the same proof gives gap_phys(H)>(57/20)epsilon, still uniformly throughout lambda<=1/640.

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

## Part II. The complete Gaussian endpoint reference

## 1. The actual flat quadratic ground precision

At the identity flat background, on transverse nonzero modes, use

    H_G = -epsilon Delta_A + (k/2) <A,K A>,
    K=c* c, lambda=k/epsilon, a=sqrt(lambda/2).

The Gaussian ansatz and its second derivative give exactly

    Omega_G(A)=C exp[-(a/2)<A,sqrt(K) A>],
    Hess log Omega_G = -a sqrt(K).

Indeed the quadratic coefficient of H_G Omega_G/Omega_G is
-epsilon a^2 K+kK/2=0. Harmonic modes require a regulator or a separate
compact retained treatment; this formula does not normalize an unregulated
Gaussian on those flat directions.

For d_i(p)=exp(i p_i)-1 and q(p)=sum_i |d_i(p)|^2, the ambient transverse
symbol is sqrt(q) [I-d d*/q]. It has a |p| cusp at zero. In the infinite
volume continuum quadratic reference the off-diagonal kernel is exactly

    sqrt(K)_{ij}(x) = [4 n_i n_j-2 delta_ij]/(pi^2 |x|^4), x!=0,
    n=x/|x|.

Derivation with Fourier convention integral dp/(2pi)^3:
F^{-1}(|p|)=-1/(pi^2 r^4), F^{-1}(|p|^{-1})=1/(2pi^2 r^2), and
F^{-1}(p_i p_j/|p|)=-partial_i partial_j[1/(2pi^2 r^2)]. The displayed
tensor follows by subtraction. Its divergence is zero off the origin.
The corresponding actual lattice symbol has the same leading homogeneous
singularity. Uniform exponential decay is impossible already because an
exponentially summable lattice kernel has an analytic Fourier symbol and
the actual sqrt(q) transverse symbol is not differentiable at zero.

These are charged derivative components of the quadratic background model,
not a claim that the compact nonlinear vacuum equals this Gaussian.

## 2. Exact lattice fractional kernel and a sufficient weighted norm

For the scalar spatial lattice Laplacian L=-Delta_lat on Z^3,

    (sqrt L)_{0x}=-j(x), x!=0,
    j(x)=1/(2sqrt(pi)) integral_0^infinity t^(-3/2) p_t(x) dt >0,
    p_t(x)=exp(-6t) product_i I_{|x_i|}(2t).

This follows directly from
sqrt z=(1/(2sqrt(pi))) integral_0^infinity (1-exp(-tz)) t^(-3/2)dt.
It gives sum_{x!=0}j(x)=(sqrt L)_{00}, since the Markov heat kernel has
row sum one. No large-distance asymptotic is required for this identity.

For 0<s<1, the weighted sum is finite, with the explicit coarse estimate

    sum_{x!=0}|x|^s j(x)
      <= [12+2*6^(s/2)/(1-s)]/(2sqrt(pi)).

Proof: a continuous-time simple walk X_t has E|X_t|^2=6t. For t>=1,
concavity gives E|X_t|^s <=(6t)^(s/2). For t<=1, subadditivity and its
Poisson jump count give E|X_t|^s<=6t. Insert these into subordination.
At s=0 use P(X_t!=0)<=min(6t,1). For s>=1 the weighted sum diverges:
Paley-Zygmund applied to |X_t|^2, using E|X_t|^4=60t^2+6t, gives
E|X_t|>=c sqrt(t) at t>=1, and the integral contains integral dt/t.

Thus a polynomially weighted Schur norm

    ||A||_s=max(sup_x sum_y (1+d(x,y))^s ||A_xy||,
                sup_y sum_x (1+d(x,y))^s ||A_xy||)

is a Banach algebra for s>=0 by the triangle inequality and
1+d(x,z)<=(1+d(x,y))(1+d(y,z)). Summable algebraic decay can therefore
replace exponential locality in a perturbative inverse/comparison when
the appropriate reference inverse and the relative excess belong to this
same algebra and the excess product has norm below one. Membership by
itself does not imply that smallness condition or the angle row <1.

## 3. An exact scalar Gaussian angle test

Let M_m=sqrt(L+m^2), m>0, on a periodic scalar lattice. Its off-diagonal
entries are negative by the same heat representation, and row sums equal m.
For density exp(-a <x,M_m x>), the maximal correlation of scalar sites e,f
conditionally on all other sites is exactly

    c_ef=|M_m(e,f)|/sqrt(M_m(e,e) M_m(f,f)).

The bivariate conditional precision is its two-site principal submatrix;
inverting that matrix gives the correlation coefficient, and the Hermite
decomposition gives maximal correlation equal to its absolute value.
Translation invariance now yields exactly

    kappa_m=sum_{f!=e}c_ef=1-m/M_m(e,e).

Hence the massless limit approaches one, even though each off-diagonal
kernel is summable. The scale factor a cancels. This is a scalar inference
control, not an identification of the complete physical SU(2) conditional
subspace with independent scalar sites.

Also: on an unbounded Gaussian support, any nonzero mixed precision gives
an infinite supremum of the mixed log-density rectangle. Thus the BA6
uniform cross-ratio sufficient estimate is stronger than a direct L2
Gaussian projection-angle estimate. A compact small-field chart must retain
its actual chart radius and all omitted-field terms in transferring it.

## 4. Exact actual averaged-path fast conditional precision, ell=2

The flat physical source is exactly W=R* on coarse transverse covectors.
Take blocking ell=2, coarse K=(K,0,0), and transverse polarization i=2 or3.
All nonzero source aliases except p=(K/2,0,0) and p+(pi,0,0) vanish because
the y,z box averages vanish on their high aliases. With q_i=4sin^2(p_i/2),
normalize frequencies by v=1 and put

    s0=sin(K/4), c=cos(K/4)>0, s=|s0|.

The source vector in these two aliases, up to its common phase and factor
1/sqrt(2), is w=(c,i s0). Its norm is one and an analytic unit vector in
the actual fiber ker w* is v_f=(i s0,c). Fine frequencies are diag(2s,2c).
Therefore the TRUE Gaussian conditional precision along this fast fiber is

    a_f(K)=v_f* Omega v_f=2[s^3+c^3].

It is uniformly positive: sqrt(2)<=a_f(K)<=2 on |K|<=pi. Nevertheless

    a_f(K)=2-3K^2/16+|K|^3/32+7K^4/1024+O(|K|^5),
    a_f(K)^(-1)=1/2+3K^2/64-|K|^3/128+11K^4/4096+O(|K|^5).

Their third-derivative jumps at zero are 3/8 and -3/32 respectively.
Thus neither has an exponentially decaying kernel uniformly in volume.
This witness is for the repo's ACTUAL averaged-path source, not an arbitrary
high-pass cutoff. Restricting an exponentially local full block kernel to
the momentum line (K,0,0) would still give an analytic function, contradicting
this computed cusp in the analytic fast vector.

Exact SymPy verification was executed for K>0, series through order 5:

    a_f=2-3K^2/16+K^3/32+7K^4/1024-K^5/1024+O(K^6),
    1/a_f=1/2+3K^2/64-K^3/128+11K^4/4096-5K^5/4096+O(K^6).

Do not confuse this Q sqrt(K) Q precision of the coordinate conditional law
with sqrt(Q K Q), a local/gapped constrained quadratic ACTION, the literal
Fock fast restriction, or a conditioned Laplacian Green function.
The existing flat-source coercivity controls K on a specified tangent
complement; it does not establish exponential locality of Q sqrt(K) Q.
A sharp spectral cutoff also cannot supply exponential locality, since its
symbol has discontinuities. A local gapped space-time/background reference
can have exponential decay before its endpoint Schur reduction; the endpoint
kernel must retain the memory/baseline generated by that reduction.

## 5. Consequence for SC17

The exact Gaussian SC17 combination must reproduce -a sqrt(K), including
its nonzero long-range part. One may seek a bound on the nonlinear excess
after subtracting this full reference, in a polynomially weighted algebra,
or keep local space-time fields until the matched endpoint/source stage.
Neither a local classical Hessian comparison nor charged inverse existence
provides the missing all-configuration compact-vacuum bound.

At nominal fluctuation scale A=lambda^(-1/4)Y, the sqrt(lambda) Hessian
coefficient cancels the two field radii in a mixed log ratio. Consequently
its Gaussian normalized block-angle size is order one, not small in lambda
or g_* merely because the raw chart shrinks. The strictly subunit actual
angle budget and omitted-field coupling remain quantitative obligations.

Published comparison: [Dimock's Euclidean d=3 QED construction](https://arxiv.org/html/1712.10029v3)
uses block averaging.
Its displayed action begins with a local ||dA||^2 quadratic form. Its
conditioned Laplacian covariance is not the square-root precision of this
physical-time Yang-Mills ground law. No source theorem is treated as a
discharged quantum SC17 hypothesis here.

## 6. The existing dynamic covariance supplies the flat reference budget

The broader G19 source review supplies a positive input to R4 below. Use the
actual averaged-path fast fiber F and its Gaussian precision A=Omega_F from
[the dynamic fiber proof](wilson-spatial-inputs/G19_DYNAMIC_FIBER_COVARIANCE_AND_CUBIC_ENERGY_20260906.md),
sections 1-4. Fix L>=2, v>0 and 0<=rho/v<=epsilon_*<infinity. In the fixed
ambient block coordinates put

    c=1/(sqrt(33)L), M=sqrt(12+epsilon_*^2),
    H(K)=v Q_F A^(-1) Q_F,
    spec H(K) subset {0} union [1/M,1/c].

The fast rank is 2L^3-2, including K=0. The separate unconditioned transverse
projector's rank behavior does not change this positive spectral island.
The dynamic proof gives a contour Gamma around that island, excluding zero,
with Re(1/z)>=c/2. Replace its function z exp(-vt/z) by exp(-vt/z), setting
the function to zero on the disjoint zero island. Then exactly

    Q_F exp(-tA) Q_F
      =(1/(2pi i)) integral_Gamma exp(-vt/z)(zI-H)^(-1) dz.

Momentum derivatives act on the resolvents only. The same conormal
resolvent estimates through order five therefore have bound
C_alpha exp(-cvt/2)|K|^(1-|alpha|), with the smooth part bounded by
C_alpha exp(-cvt/2). This remains true at t=0, where the contour gives Q_F.
The dyadic Fourier argument and exact periodization in the cited proof yield

    ||[Q_F exp(-tA) Q_F](x)||op
      <=C exp(-cvt/2)(1+|x|)^(-4).

For every 0<=s<1 in three spatial dimensions, multiplying by (1+|x|)^s
and summing is finite. Self-adjointness supplies both Schur rows and columns:

    ||Q_F exp(-tA) Q_F||_s <= C_s exp(-cvt/2),
    beta_s(A) <= C_s^2/(cv) = sqrt(33)L C_s^2/v.          (R4a)

Here the semigroup on F is represented by its ambient extension, zero on
the retained complement. Products and the weighted Banach norm use those
fixed coordinates; no momentum-dependent orthonormal frame is differentiated.
Constants are uniform in volume and bounded regulator at fixed L. At rho=0
this is a normalized conditional affine-fiber result, not a normalized full
massless joint Gaussian. Thus R4 is discharged on this actual flat Gaussian
reference. Transferring it to nonlinear curved fibers with their actual
kinetic metric remains a further estimate. The same contour proof does not
establish a strict reference-angle margin by itself.

## Part III. Signed Riccati continuation with explicit quantum defects

## 1. Exact Euclidean equation and its projected cross terms

For H=-epsilon Delta+V on the complete Euclidean configuration space R^n,
let Z_t=exp(-tH)psi_ref>0, u_t=log Z_t, J_t=Hess u_t, and
K_t=-epsilon(Delta+2 grad u_t.grad). Direct differentiation gives

    (partial_t+K_t)J_t = 2epsilon J_t^2-V''.

For a constant symmetric reference precision Omega and E=J+Omega,

    (partial_t+K_t)E+2epsilon(Omega E+E Omega)
       =2epsilon E^2-[V''-2epsilon Omega^2].                  (R1)

Thus the proposed signs and constants are correct. Take constant orthogonal
Q, P=I-Q, and write A=QOmegaQ, B=QOmegaP, X=QEQ, Y=QEP. Projection is exact:

    (partial_t+K_t)X+2epsilon(AX+XA)
      =2epsilon X^2-Q[V''-2epsilon Omega^2]Q
           +2epsilon YY* -2epsilon(BY*+YB*).                 (R2)

The last two terms cannot be discarded merely because A is positive.
They are present for the actual averaged-path projection, for which
Omega and Q do not commute. A bound on the fast projected action Hessian
does not by itself bound this effective right side.

If Q=Q(t,x), D=partial_t+K_t, there are additionally the exact terms

    (DQ)EQ+QE(DQ)
      -2epsilon sum_i [(partial_i Q)(partial_i E)Q
                       +(partial_i Q)E(partial_i Q)
                       +Q(partial_i E)(partial_i Q)].        (R3)

If the reference precision also moves, (R1) acquires +D Omega on its right.
These identities are Euclidean coordinate identities; replacing the kinetic
metric by the actual compact-link chart metric introduces its actual
connection, coefficient, and commutator terms.

## 2. A rigorous conditional small-defect criterion

Let indices carry a metric and use the symmetric weighted Schur norm

    ||M||_s=max(sup_i sum_j (1+d(i,j))^s ||M_ij||,
                sup_j sum_i (1+d(i,j))^s ||M_ij||), s>=0.

For configuration-dependent matrices replace ||M_ij|| by its supremum over
configurations. This stronger entrywise-uniform norm, denoted ||.||_(s,infty),
is preserved by every componentwise Markov transition, and it is a Banach
algebra. It dominates the Hilbert-space operator norm.

Let A=A*>0 be constant on the specified Euclidean fast fiber and define the
actual reference semigroup budget

    beta_s(A)=integral_0^infinity ||exp(-tA)||_s^2 dt < infinity. (R4)

Finite dimensionality makes this finite at each fixed volume, but a uniform
bound on beta_s is an additional hypothesis. It is not an automatic consequence
of a volume-uniform spectral floor. Polynomial spatial decay is allowed.

For every outside value b suppose the actual conditional potential U_b has

    ||U_b''-2epsilon A^2||_(s,infty) <=delta,                (R5)

uniformly in b and volume. Assume the relevant Euclidean Schrödinger semigroup
and smooth ground limit exist, and the finite-time Hessians have the usual
classical boundedness and norm continuity on compact time intervals. These
regularity assumptions hold, for example, for smooth quadratically confining
potentials with bounded Hessian defect and a positive Gaussian initial state;
one may instead include them explicitly as hypotheses when using a new fiber.
Require the actual time-dependent ground-transformed Markov evolution to be
conservative. This is the complete-space theorem, not a killed chart theorem.

If

    2 beta_s(A)^2 delta/epsilon < 1,                       (R6)

then the actual conditional ground obeys

    ||Hess log Omega_b + A||_(s,infty) <= r_-,
    r_-=[1-sqrt(1-2 beta_s(A)^2 delta/epsilon)]/[2 beta_s(A)]. (R7)

Proof. Initialize psi_ref=exp(-<x,A x>/2), so E_0=0. Using a constant reference
lets its left/right matrix semigroups commute with the actual componentwise
Markov evolution P_(t,s) generated by -K_t. Duhamel in (R1) is

    E_t=integral_0^t P_(t,s)[exp(-2epsilon(t-s)A)
            (2epsilon E_s^2-D_b)
                            exp(-2epsilon(t-s)A)] ds,
    D_b=U_b''-2epsilon A^2.

For M_T=sup_(t<=T)||E_t||_(s,infty), (R4) gives

    M_T <= beta_s M_T^2+beta_s delta/(2epsilon).            (R8)

The right side minus M_T has two distinct nonnegative roots r_-<r_+.
Starting from zero and using continuity, M_T cannot cross any number strictly
between those roots, since (R8) would then imply M_T<M_T at the first crossing.
Hence M_T<=r_- for all T. Pass to the actual conditional ground at fixed finite
volume and then retain the displayed uniform constants. This uses physical
imaginary time and the actual ground transformation; there is no identification
with a separate stochastic-quantization clock.

If a=lambda_min(A), beta_s>=1/(2a), and (R6) ensures delta<2epsilon a^2 and
r_-<a. Thus the effective potential is quadratically confining and
-Hess log Omega_b >=(a-r_-)I. Bochner/Poincare for the actual ground-transformed
conditional Hamiltonian gives

    gamma_b >=2epsilon(a-r_-).                            (R9)

For A=aI, beta_s=1/(2a), and (R7) becomes
r_-=a-sqrt(a^2-delta/(2epsilon)), recovering the exact scalar oscillator
lower-curvature root. This confirms the constants in the criterion.

## 3. An explicit true-angle consequence if the full Hessian defect is known

Consider two Euclidean coordinate blocks B,C conditional on their complement,
with density exp(-Phi). If, uniformly in all fields,

    Phi_BB >=2a_B I, Phi_CC>=2a_C I, ||Phi_BC||<=2h_BC,
    h_BC^2<a_B a_C,

then their actual L2 conditional projection angle obeys

    c_BC <=h_BC/sqrt(a_B a_C).                            (R10)

Proof without Gaussian substitution: differentiate E[f(B)|C]. Conditional
Poincare in B and the mixed Hessian bound give

    |grad_C E[f|C]|^2 <=(2h_BC^2/a_B) Var(f|C).

Differentiating the marginal potential and applying the same conditional
Poincare gives marginal C curvature at least 2(a_C-h_BC^2/a_B). Its Poincare
inequality yields

    Var(E[f|C]) <=[h_BC^2/(a_B a_C-h_BC^2)] E Var(f|C).

Total variance then gives Var(E[f|C])/Var(f)<=h_BC^2/(a_B a_C), exactly the
squared conditional-expectation norm/maximal-correlation bound. Approximation
extends from smooth f to L2. Restricting to an invariant physical subspace
can only reduce this bound, once the underlying conditional operators and
fiber have actually been identified.

For Phi=-2 log Omega and Hess log Omega=-A+E, use
a_B=lambda_min(A_BB)-||E_BB|| and h_BC=||A_BC||+||E_BC||.
For a disjoint coordinate-block partition covering the fiber, in the
particularly transparent uniform-block case A_BB>=a_0 I,

    kappa_A=sup_B sum_(C!=B)||A_BC||/a_0 <1,
    ||E||_(s,infty)<=r,
    2r<a_0(1-kappa_A),

one obtains

    kappa_actual <=(a_0 kappa_A+r)/(a_0-r) <1,
    gamma_min(1-kappa_actual)
       >=2epsilon[a_0(1-kappa_A)-2r].                    (R11)

Thus (R4)-(R7), a reference angle margin, and explicit coordinate/source
compatibility supply a concrete conditional route to both requested estimates.
None of these inequalities claims that the unconditioned massless reference
has kappa_A<1. The exact scalar test in the preceding report has kappa_A->1.

## 4. The actual quantum pressure and cutoff defects are part of the input

For an actual product Euclidean block write
H=-epsilon Delta_B+V_B+H_out, assigning each multiplication term exactly
once. For its full vacuum Omega, define

    W_B=(H_out Omega)/Omega.

Then Omega(. ,b) is the conditional positive eigenfunction of
-epsilon Delta_B+V_B+W_B. Accordingly the potential in (R5) must be

    U_b=V_B+W_B,
    D_b=V_B''+(W_B)''-2epsilon A^2.                       (R12)

It is not enough to bound V_B''. This includes the complete outside quantum
pressure, rather than replacing the true conditional law by a frozen-link
Hamiltonian ground. For an oblique actual source fiber, first construct its
kinetic metric and its effective potential; those are additional inputs.

The complete coupled Gaussian baseline cancels exactly. Write its precision
in orthogonal fast/retained coordinates as Omega_0=[[A,B],[B*,C]], with
ground exp(-<z,Omega_0 z>/2), and take
H_0=-epsilon Delta+epsilon<z,Omega_0^2 z>. Assign the multiplication potential
to V_0 and the retained kinetic term to H_out,0. With fast coordinate x and
retained coordinate y,

    W_0=epsilon Tr(C)-epsilon||B* x+C y||^2,
    V_0,xx''=2epsilon(A^2+BB*),
    W_0,xx''=-2epsilon BB*.

Thus V_0,xx''+W_0,xx''=2epsilon A^2 even when B is large. This is the actual
conditional Gaussian precision; the nonproduct score is retained. After
identifying common coordinates and all kinetic terms, the nonlinear target
can equivalently be written

    D_b=(V_B-V_0)''+(W_B-W_0)'',                         (R12a)

with the additional actual metric/projector/cutoff terms still included.
The target is a small complete excess over this baseline; no smallness of
W_B'' or of B separately is assumed. The G19 endpoint/covariance proofs and
the [Gaussian-family review](../validation/wilson-g19-gaussian-review.md)
provide the source and normalization for this cancellation.

For a smooth cutoff chi, the exact localized Riccati field satisfies

    D(chi E)=chi DE+(Dchi)E-2epsilon grad chi.grad E.       (R13)

Thus localization generates shell terms including derivatives of E. Equally,

    [H,chi]Omega=-epsilon(Delta chi)Omega
                  -2epsilon grad chi.grad Omega.          (R14)

Their sign, support, norms, and any Schur self-energy must be controlled in
the same comparison. A probability assigned to the excluded region does not
bound (R13) or (R14). A Dirichlet chart ground vanishes at the boundary and
logarithmic Hessians may diverge there; the global theorem (R7) cannot be
applied across that boundary without an actual interior localization and
these explicit defect terms.

## 5. The averaged-path cusp is an analytic compression, not an eigenvalue crossing

For the actual ell=2 two-alias transverse source of the preceding report,
choose signed s_0=sin(K/4), c=cos(K/4) and

    w(K)=(c,i s_0), v_f(K)=(i s_0,c).

Both vectors are real-analytic functions of K near zero; w* v_f=0 and
||v_f||=1 exactly. The actual Euclidean fast projection in this two-alias
subspace is Q=v_f v_f*. The coefficient

    v_f(K)* Q(K) Omega(K) Q(K) v_f(K)
       =2[|sin(K/4)|^3+cos^3(K/4)]                      (R15)

is therefore a compression in a specified analytic frame, not a numerically
sorted eigenvalue. A hypothetical full matrix symbol analytic near K=0 would
make (R15) analytic, contradicting its third-derivative jump 3/8. The inverse
coefficient similarly has jump -3/32. The chosen transverse polarization is
fixed along the axis on both sides of zero, so no polarization eigenvalue
crossing explains the cusp. The harmonic fine alias is retained at K=0;
the fast coefficient is well-defined there, or can be obtained as a positive
regulator tends to zero. The contradiction concerns uniform volume/regulator
locality, not a finite Fourier polynomial on a single fixed lattice.

## Precise remaining large-lambda target

Construct the actual fast/coarse fiber and prove a uniform polynomial reference
semigroup budget (R4), a strictly subunit reference block-angle budget when
required, and a bound for the COMPLETE defect (R12), or equivalently for the
right side of (R2) including (R3), (R13), and (R14), small enough for (R6) and
(R11). This is a finite list of quantitative inequalities. A magnetic local
Hessian comparison alone supplies only one contribution to that list.

## Exact stopping point and the user's guidance document

The subsequently supplied BC2 repairs were checked against their updated
source. The cellwise adjoint law (3.4), the rescaling algebra in (5.8), and
the conditional stiffness absorption in (5.13) are accepted. They do not
bound the actual outside-pressure Hessian below. The source-version-pinned
[BC2 update audit](../validation/wilson-sc17-bc2-update-audit.md) identifies
the remaining first inverse estimate in (5.8), the omitted averaging
commutator in (5.17), and the actual nonlinear source-fiber issue.

The new actual-vacuum proof closes exponential SC17 through lambda<lambda_c,
including lambda<=1/73. Its bare norm majorant fails beyond lambda_c;
at lambda=1/72 the discriminant is exactly -47/2304, as calculated in
Part I. Part III then goes beyond that failed comparison: the signed
background Riccati equation is exact, and R4-R11 prove a sufficient
conditional theorem with stated analytic hypotheses.
The separate thermodynamic continuation discharges the fixed-spacing local
vacuum limit and constructs its closed physical ground-law form in this
regime. The [physical-time continuation](wilson-sc17-physical-time-limit.md)
then identifies actual free/periodic multitime vacuum limits with that
generator, including lambda_c. Its bounded-interval plaquette overlap does
not discharge complete isolated-shell or continuum source matching.

The next unproved derivation is the actual Wilson bound R5/R12, uniformly
on admissible scale-dependent source fibers, strong enough for R6 and R11:

\[
\|D_b\|_{s,\infty}\le\delta,\qquad
D_b=V_B''+\left((H_{\rm out}\Omega)/\Omega\right)''-2\epsilon A^2,
\qquad 2\beta_s(A)^2\delta/\epsilon<1.
\]

Here the actual coordinate metric, moving source projector and cutoff
corrections R2-R3/R13-R14 must also be included when those are present.
BF4 controls the magnetic contribution on its specified small-field slice.
The broader G19 corpus supplies the flat Gaussian reference budget R4a and
the exact coupled Gaussian pressure cancellation R12a. What remains is the
complete nonlinear excess, including the outside-pressure difference, and
its transfer to the actual curved Wilson source fibers. The needed strict
source-compatible reference angle margin is also not discharged there.
This is the precise missing estimate,
not an assertion that the estimate is false. Complete retained Schur control,
carrier rank and observable source matching remain subject to their existing
theorem hypotheses; a finite-spacing gap alone does not discharge them.

For the separately proposed Balaban continuum construction, the
[broader G19 reconciliation](../validation/wilson-g19-corpus-reconciliation.md)
locates an additional explicit wall: (7.6) supplies O(1/k) increments, while
Theorem 7.1 concludes Cauchy convergence using summability of 1/k^2.
A sufficient common-space contraction and summable scale/source drift
repair is proved there; its actual Wilson map hypotheses remain to be supplied.

Jaffe-Witten, section 6.5, page 11, states the corresponding continuum
obligation exactly:

> One must then verify the existence of limits of appropriate expectations of gauge-invariant observables as the lattice spacing tends to zero and as the volume tends to infinity.

Source: the user's `1-yangmills.pdf`, SHA256
`3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09`.
The new uniform-volume estimates apply on the explicitly displayed coupling
interval; no passage along the large-lambda spatial continuum trajectory is
claimed.

