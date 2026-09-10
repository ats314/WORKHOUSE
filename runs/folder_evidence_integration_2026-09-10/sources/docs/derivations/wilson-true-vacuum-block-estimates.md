# Actual vacuum block estimates: optimized gap and connected angle reduction

9 September 2026. Continuation of VA19 in
`wilson-vacuum-aligned-assembly.md`. All blocks below use the actual finite
Wilson ground Omega and mu=Omega^2 dU. No isolated-cube eigenvalue or assigned
exponential correlation is substituted for a conditional operator.
The analytic arguments are not Lean formalizations. The registered exact
controls check the stated finite algebra and geometric counts.

## BA1. A specified block partition

Use the same unit-S3 link metric and H=-epsilon sum_e Delta_e+k sum_p s_p,
0<=s_p<=2, as VA1. On a periodic cubic lattice with side L divisible by ell,
L>=max(3,2ell), partition vertices into ell-cubes. Assign each positive
oriented link to the cube containing its tail. The resulting link blocks
are disjoint, cover every link, and have

    r=3 ell^3, p_B=3 ell^3+6 ell^2, m_*=1.          (BA1)

For each plaquette orientation (i,j), its three distinct link tails are
v,v+e_i,v+e_j. A plaquette touches a given vertex cube S exactly when its
base belongs to S union (S-e_i) union (S-e_j). This union has ell^3+2ell^2
vertices: S and two disjoint added faces. Sum the three orientations.
In particular ell=2 gives 24 links and 48 touching plaquettes per block.
This is a partition of the actual links; twelve edges of a geometric cube
do not supply this partition. Neighboring blocks have neighboring link
supports even though their centers are ell units apart.

## BA2. Optimizing the true conditional gap

Let p_tau be the single-link heat kernel with generator Delta and normalized
Haar measure; M_tau=max p_tau and m_tau=min p_tau. Keeping the comparison
time free in the proved positive-kernel argument VA1-VA2 gives

    max Omega(. ,b)/min Omega(. ,b)
       <= exp(2k p_B tau/epsilon)(M_tau/m_tau)^r.

The product Haar Poincare gap is 3. Variance/energy density comparison
therefore proves the actual conditional gap bound

    gamma_B >= 3 epsilon sup_(tau>0)
      exp(-4k p_B tau/epsilon)(m_tau/M_tau)^(2r).     (BA2)

Every bound is uniform in the full outside configuration b and total volume.

Here is an explicit useful estimate at short times. On unit S3 the heat
kernel satisfies

    M_tau/m_tau <= 2^(3/2) exp(pi^2/(2tau)).          (BA3)

For completeness, the heat-equation Harnack inequality used here follows
from Bochner on a compact manifold with Ric>=0. If f=log h and
w=|grad f|^2-f_t=-Delta f, then
(partial_t-Delta-2 grad f.grad)w<=-2w^2/n. The maximum principle applied
to t w gives w<=n/(2t). Integrating f_t>=|grad f|^2-n/(2t) along a minimizing
space-time geodesic yields

    h(s,x) <= h(t,y)(t/s)^(n/2) exp[d(x,y)^2/(4(t-s))].

Time-shift a heat kernel by a positive amount and pass to zero to justify
its singular initial data. For S3 take s=tau/2, t=tau, x=identity and use
diameter pi. The character expansion gives p_tau(g)<=p_tau(identity),
and p_(tau/2)(identity)>=p_tau(identity). This proves BA3. This is the
compact free-heat case of Li--Yau, *On the parabolic kernel of the
Schrodinger operator*, Acta Math. 156 (1986), sections 1-2:
https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6384-11511_2006_Article_BF02399203.pdf
No curvature condition is imposed on the interacting vacuum.

Substitute BA3 in BA2 and minimize
4k p_B tau/epsilon+r pi^2/tau at
tau=(pi/2)sqrt(r epsilon/(k p_B)). For k>0 this proves

    gamma_B >= 3 epsilon 8^(-r)
                   exp[-4pi sqrt(r p_B k/epsilon)]. (BA4)

At k=0 the true ground is constant and the exact conditional gap is
3epsilon. Take the maximum of BA4 and the preceding VA19 bound when k>0.
For one link p_B=4, the new bound is
(3epsilon/8)exp[-8pi sqrt(k/epsilon)], replacing the old exponent
-16k/epsilon by -8pi sqrt(k/epsilon). This is a bound for the true
conditional measure, not a frozen-link ground measure.

Along the conditional logarithmic trajectory in VA17, for a fixed block
geometry put nu_B=4pi b sqrt(r p_B c_B/c_E). Then the logarithm of the
BA4 lower bound is

    (1-nu_B)log(1/a)+o(log(1/a))-log log(1/a)+O(1). (BA5)

Thus the bound diverges if nu_B<1 and vanishes if nu_B>1; at nu_B=1 the
stated leading asymptotic of g alone does not decide the outcome. This
improves the earlier exp[-const log(1/a)^2] loss. It supplies no angle
estimate and makes no assertion that the physical coefficient nu_B<1.
Blocks growing in lattice units require re-evaluating r and p_B as well.

## BA3. Reduce the actual projection angle to a mixed ground-amplitude ratio

For two disjoint blocks B,C and fixed outside b, let p_b(x,y) be their true
joint conditional density. Write p_B,p_C for its marginals in this section.
Define the mixed oscillation

    D_BC = sup_(b,x,x',y,y') |
      log[p_b(x,y)p_b(x',y')/(p_b(x,y')p_b(x',y))]|
           = 2 sup |u(x,y,b)+u(x',y',b)
                         -u(x,y',b)-u(x',y,b)|,
    u=log Omega.                                    (BA6)

All densities are positive and smooth at fixed finite volume. Directly,

    p_b(x,y)/(p_B(x)p_C(y))
       = integral [p_b(x,y)p_b(x',y')/(p_b(x,y')p_b(x',y))]
                  [p_b(x,y')p_b(x',y)/(p_B(x)p_C(y))] dx'dy'.

The second bracket is a probability density in (x',y'). Hence
p_b>=exp(-D_BC)p_B p_C. Subtract this product part. The remainder,
divided by 1-exp(-D_BC), is a probability measure with exactly the same
marginals. Cauchy--Schwarz in that remainder bounds the covariance of any
two centered block functions by (1-exp(-D_BC)) times their L2 norms.
For D_BC=0 the density factorizes exactly.

Disintegrating the two conditional projections over the outside shows
that their nontrivial angle is the maximal correlation of these two
conditional variables. Restriction to gauge-invariant functions cannot
increase this norm. Consequently the actual physical operators satisfy

    c_BC^phys=||(E_B E_C-E_(B union C))|phys||
                   <= 1-exp(-D_BC) <= D_BC.         (BA7)

This gives a proved sufficient hypothesis expressed solely in Omega:

    sup_B sum_(C!=B) D_BC <= kappa<1
       => gap_phys H >= gamma_min(1-kappa)           (BA8)

for the disjoint covering BA1, using BA4 or any stronger true conditional
floor. The mixed ratio cancels every factor depending only on B, only on
C, or only on their outside. It is exactly the connected quantity needed;
ordinary two-point decay of a few selected observables is not BA6.

BA2 bounds D_BC by four times the smaller block amplitude oscillation,
but gives no distance dependence. This bound still fails the volume sum.
No exponential estimate for D_BC has been inserted in BA8.

## BA4. What a frozen-block spectral computation would additionally require

Split H=h_B(b)+H_out, where h_B=-epsilon Delta_B+V_B contains every
plaquette touching B. Define the real, smooth conditional pressure

    W_B(x;b)=(H_out Omega)(x,b)/Omega(x,b).

The ground equation says (h_B+W_B)Omega(. ,b)=E0 Omega(. ,b).
Positivity identifies it as the lowest eigenfunction of this compact
elliptic block operator. Multiplication by its normalized amplitude
identifies the true conditional Dirichlet generator with h_B+W_B-E0.
The min-max principle gives the useful alternative

    gap_conditional(B,b) >= gap(h_B(b))-osc_x W_B(x;b). (BA9)

The coefficient is one oscillation, not twice its absolute supremum:
lambda_1 shifts by at least inf W_B and lambda_0 by at most sup W_B.
An outside-dependent constant cancels. Explicitly its remaining variation
is the B-variation of

    -epsilon sum_(e outside B)[Delta_e u+|grad_e u|^2]. (BA10)

The outside potential cancels from this oscillation. A numerical gap of
an isolated block does not bound BA9 without its boundary-uniform frozen
gap and this pressure-oscillation estimate. BA4 already gives a weaker
unconditional positive result without needing BA10.

## BA5. Exact finite-time derivation of the connected quantity

There is a direct way to expose the source of BA6. Let
Z_T(U)=(exp(-T H)1)(U)=E_U exp[-integral_0^T V(U_t)dt], where the links
follow independent Brownian motion with generator epsilon Delta.
For fixed finite lattice, the strictly positive ground and discrete
spectrum imply log Z_T+T E0 -> u+constant in C2. No uniform convergence
rate in volume is asserted.

Choose infinitesimal left translations X and Y on disjoint blocks. Write
J_X=integral_0^T (XV)(U_t)dt and J_XY similarly for XYV. Starting a path at
exp(sX)U amounts to the same left translation of the entire Brownian path.
Differentiate the finite-time expectation; compactness justifies this.
With expectation tilted by exp[-integral V]/Z_T, exactly

    XY log Z_T = Cov_T,U(J_X,J_Y)-E_T,U J_XY,
    XY u = lim_(T->infinity)
                 [Cov_T,U(J_X,J_Y)-E_T,U J_XY].     (BA11)

When no plaquette meets both blocks, XYV=0, so the direct term vanishes.
The covariance is still taken in the interacting tilted path measure.
For unit product-metric vectors on B,C, integration over two product
geodesics, of lengths at most pi sqrt(r_B), pi sqrt(r_C), gives

    D_BC <= 2pi^2 sqrt(r_B r_C)
                       sup_(U,|X|=|Y|=1) |XYu(U)|. (BA12)

This exposes a concrete route to BA8 through connected force covariances.
Bounding J_X and J_Y separately by their suprema gives only O(T^2), not
BA12 uniformly in T. Even a bound on the absolute time-covariance integral
that grows like T would lose the vacuum cancellation in BA11. The
finite-volume limit alone does not control its spatial dependence.

## BA6. The first connected coefficients for the actual coupled lattice

The covariance formula can be pushed further at the decoupled endpoint.
Put lambda=k/epsilon, w_p=Tr(U_p)/2, and fix the additive constant of
u=log Omega by Haar mean zero. At each fixed finite lattice analytic
perturbation of the simple ground at lambda=0 gives
u=sum_(n>=1)lambda^n u_n in a neighborhood of zero. No volume-uniform
radius is asserted. Substituting in the ground equation gives exactly

    u_1=(1/12)sum_p w_p,
    (-Delta)u_n = Q_Haar sum_(i+j=n) grad u_i.grad u_j,
                              n>=2.                (BA13)

Here -Delta=sum_e(-Delta_e), and Q_Haar removes constants. Each fundamental
plaquette has -Delta w_p=12w_p and Haar norm squared 1/4.
The inverse on centered functions supported on a set of links retains
that support: the product heat semigroup acts as identity outside it.
The gradient product is zero for disjoint link supports. Induction thus
proves that every contribution to u_n is supported on a connected union
of at most n plaquettes, joined through shared links. Disconnected vacuum
products cancel at every formal order in the logarithm.

The first nontrivial connected pair is explicitly calculable. A single
plaquette contributes

    u_(2,self,p)=-chi_2(U_p)/4608,
    chi_2(U_p)=4w_p^2-1.                            (BA14)

Indeed sum_e|grad_e w_p|^2=4(1-w_p^2), so the centered order-two
source from this plaquette is -chi_2/144, and -Delta chi_2=32chi_2.

For an unordered pair of distinct plaquettes sharing a link, orient their
traces so that w_p=Tr(AU)/2 and w_q=Tr(U^-1 B)/2; SU2 trace reversal
does not change w_q. Let L_pq=Tr(AB)/2, the six-link boundary loop.
The unit-S3 Fierz identity gives

    grad_e w_p.grad_e w_q=L_pq-w_p w_q,
    (-Delta)L_pq=18L_pq,
    (-Delta)(w_p w_q)=26w_p w_q-2L_pq.

Both orders (p,q) and (q,p) appear in |grad u_1|^2. Their exact logarithmic
coefficient is therefore

    u_(2,pq)=L_pq/1404-w_p w_q/1872,
    (-Delta)u_(2,pq)=(L_pq-w_p w_q)/72.             (BA15)

This term retains the actual common-link coupling and boundary loop. Its
coefficients do not depend on the surrounding volume. The corresponding
energy coefficient is E0/epsilon=lambda|P|-lambda^2|P|/48+O_L(lambda^3).
Distinct plaquette characters are Haar orthogonal, so this energy identity
follows from integral |grad u_1|^2=|P|/48.

For the signed four-point mixed difference in BA6, all coefficients of
order less than d(B,C) vanish, where d(B,C) is the least number of
link-connected plaquettes whose union meets both blocks. Thus the actual
ground has connected spatial locality coefficient by coefficient. At
first order one obtains

    D_BC <= (2/3)N_BC |lambda|+O_L(lambda^2),        (BA16)

where N_BC counts plaquettes touching both blocks. The factor 2/3 is
2 (from log mu) times 4 (the oscillation bound for four values of w_p)
times 1/12. The remainder is only a finite-volume remainder. Turning
these linked coefficients into a uniform bound on D_BC requires a
summable all-order majorant for BA13, or a nonperturbative estimate of
BA11. Neither a formal support induction nor its first two coefficients
supplies that remainder, especially on the continuum large-lambda trajectory.

## BA7. Actual angle closure in an explicit strong-coupling window

There is a uniform summation using exact Brownian slabs. Set
Zhat_s=exp(-s H/epsilon)1=Z_(s/epsilon), and take dimensionless slab length
tau=4. The physical clock is restored by the factor epsilon in BA25.
This is not a Trotter approximation.
Condition each free link Brownian path on its endpoints in each slab.
Realize its bridge law by independent auxiliary uniform random variables,
measurably in the two endpoints, using the positive heat transition
densities on dyadic subdivisions. Endpoint variables at times 1,...,N
have product Haar reference measure; initial endpoints are fixed at U.
The auxiliary bridge variables have product reference measure independent
of the endpoints. Feynman--Kac now expresses Zhat_(4N)(U) exactly as the
reference integral of a product of factors

    1+a_(e,j)=p_4(U_(e,j),U_(e,j+1)),
    1+b_(p,j)=exp[-lambda integral_(4j)^(4j+4) s_p(U_t)dt]. (BA20)

The four paths in each b are their actual bridges. With lambda=k/epsilon,
the character-tail bound VA3 and 0<=s_p<=2 give

    |a_(e,j)| <= e^-9 (1541/6859) < 1/32000,
    |b_(p,j)| <= 8lambda <= 1/32000
                 if 0<=lambda<=1/256000.             (BA21)

Here e^3>20 and 1541/6859<1/4 suffice for the first inequality.
Join factors sharing an endpoint or bridge variable; including fixed
initial endpoints only enlarges this dependency graph. Each interior
endpoint belongs to two temporal and eight plaquette factors. Each bridge
variable belongs to four plaquette factors. A plaquette factor uses eight
endpoints and four bridges, so its degree is at most 8*9+4*3=84. A temporal
factor has degree at most 18. These bounds hold uniformly at all boundaries.

Expand the finite product and group connected sets gamma of factors.
Nonadjacent sets integrate independently under the reference product law,
giving an exact polymer gas with |z_gamma(U)|<=alpha^|gamma|,
alpha=1/32000, uniformly in the initial configuration. A degree-D graph
has at most (4D)^(n-1) connected n-vertex sets containing a fixed vertex:
encode a canonical spanning tree by an ordered rooted tree and neighbor
choices. Take D=84 and apply the KP criterion with a(gamma)=|gamma| to
activities tilted by exp(|gamma|). The tilt records the total factor
count N_c of a cluster, including multiplicities. Since e<87/32 and e^2<8,

    x=alpha e^2<1/4000,
    A=sum_(n>=1)(4D)^(n-1)x^n <=1/3664,
    (D+1)A<=85/3664<1.                              (BA22)

An incompatible polymer is rooted at one of at most (D+1)|gamma| factors,
so BA22 checks the KP hypothesis. The pinned cluster conclusion, summed
over polymers containing a fixed factor v, is

    sum_(clusters containing v) exp(N_c)|coefficient| <= A.

Coefficients here include activities. Use their uniform activity majorants
when taking suprema over initial data. A pinned polymer can be distinguished
in several ways, which overcounts the unmarked sum and is therefore valid.
The theorem used is Ueltschi, *Cluster expansions and correlation functions*,
Theorem 1, equations (3)-(4), PDF page 2, specialized to discrete hard-core
polymers: https://arxiv.org/pdf/math-ph/0304003 . The activities and
model-dependent constants needed to apply it have been constructed above.

Only clusters touching time-zero variables depend on U. A mixed difference
cancels every cluster not touching both B and C. Four evaluations and the
factor 2 from log mu give a bound 8 times the uniform cluster majorant.
At most 5r factors touch the initial links of B. A cluster of total size
N_c touches at most 4N_c blocks of a disjoint initial-link partition.
Sum over C before discarding support, and use N_c<=exp(N_c). This proves

    sup_B sum_(C!=B) D_BC <=8*(5r)*4*A=160r A.       (BA23)

These estimates hold for every finite N. At each fixed finite spatial
lattice, the ground limit of the mixed log Zhat_(4N) difference equals the
mixed log Omega difference. BA23 therefore passes to the actual ground
with its constant independent of spatial volume. No uniform convergence
rate or exchange with an uncontrolled infinite-volume limit is needed.

For BA1 with ell=1, r=3 and p_B=9, the actual physical projections satisfy

    kappa_blocks <=30/229<1.                         (BA24)

There is also an exponential envelope: let d(B,C) be minimum link distance
in the graph joining links that share a plaquette. A cluster touching both
blocks has N_c>=d(B,C). The same weighted pinned sum gives
D_BC<=40r A exp[-d(B,C)], hence c_BC^phys<=(15/458)exp[-d(B,C)].

In this small-lambda window, the tau=4 conditional comparison is stronger
than the simple BA4 estimate. Since 1-alpha<=p_4<=1+alpha, it gives

    gamma_B >=3epsilon exp(-144lambda)(31999/32001)^6,
    gap_phys(H_Lambda) >= (199/229)3epsilon
                          exp(-144lambda)(31999/32001)^6>0,
    0<=lambda<=1/256000, L>=3.                       (BA25)

This also closes the original single-link variance inequality VA14 in
this window. The conditional three-link density has max/min ratio at
most T_B=exp(144lambda)(32001/31999)^6. Haar tensorization and density
comparison give Var_(mu_B) f<=T_B sum_(e in B) E_(mu_B)Var_(mu_e) f:
bound the full variance by M times the Haar variance, and each integrated
conditional variance from below by m times its Haar counterpart.
Combine this with the block variance bound and the disjoint covering:

    C_AT <= (229/199)exp(144lambda)(32001/31999)^6.   (BA25a)

This bound holds on the full function space and hence also on the
gauge-invariant form-domain class required in VA14.

For convenient rational constants throughout this window, use
exp(-144lambda)>1-9/16000 and
(31999/32001)^6>1-12/32001. Their product exceeds
1-9/16000-12/32001. Exact rational arithmetic in BA25 and BA25a then gives
gap_phys(H_Lambda)>(13/5)epsilon and C_AT<29/25. These simpler constants
do not rely on rounding a numerical evaluation of the exponential.

Thus both requested estimates hold for the actual coupled vacuum in this
explicit finite-spacing regime, uniformly in outside configurations and
volume. A continuum state or complete source shell is not inferred from
this finite-volume family. The small parameter is k/epsilon. Under the
physical coefficients in VA17, k/epsilon=(c_B/c_E)g^-4 tends to infinity.
BA21 fails along that trajectory; it does not supply a continuum bridge.

Changing the slab length cannot fix this particular small-activity route
at arbitrarily large lambda. If both factor suprema must stay below the
same alpha in (0,1), the fundamental heat character at the identity gives
p_tau(identity)-1>=4exp(-3tau). The essential supremum of a single
plaquette-path factor is 1-exp(-2lambda tau): bridges have full support
near constant paths whose plaquette holonomy is -I. Therefore necessarily

    tau >= (1/3)log(4/alpha),
    tau <= -log(1-alpha)/(2lambda),
    lambda <= 3[-log(1-alpha)]/[2log(4/alpha)].       (BA26)

For any fixed admissible small-activity budget this excludes lambda tending
to infinity, independently of the selected tau. A different reference
measure, a cancellation retaining large plaquette factors, or a direct
nonperturbative BA11 estimate is needed to continue this route there.

## BA8. Precise remaining wall and the incoming walkthrough

The conditional block-gap obligation is now discharged at fixed positive
coefficients by BA4, uniformly in boundary and volume, with a substantially
improved coupling dependence. BA20-BA25 now prove the strict summable angle
bound when k/epsilon<=1/256000. The next unproved step is extending that
control to the large-k/epsilon continuum trajectory: BA21 fails there.
BA11 identifies a nonperturbative signed covariance target, and BA13-BA16
give the actual connected coefficients, but outside the proved window a
uniform remainder estimate is still missing. BA9-BA10 identify a separate
exact route to sharper conditional coercivity.

The supplied Downloads/walkthrough.md has SHA-256
f6452918246a2c4344de8f6f200f7562353ded05287715d584045e78818950da;
the accompanying pasted command report has SHA-256
2bd29c94c2820a8c5d50e5c0c1cb67f49632792a773e770b183613fab9442a9d.
They are evidence submissions, not instructions to execute their commands.
Their Phase 9 code constructs a Gram matrix from assigned energies and
matrix elements, and inserts Delta_phys into its two-exponential function.
Neither computation estimates BA6 or BA10. The existing GPU audit records
the separate reconstruction and fourth-moment discrepancies.

The subsequently located `phase10_balaban_small_field_block_va19.py` also
does not provide the missing large-lambda input. It assigns
gamma_small=(pi*hbar_c/L_phys)(1-.08*g^2), a large-field probability
exp(-2.4/g^.30), and then gamma_net=gamma_small*(1-p_large); it retains
the assigned Phase 8 kappa=.052853. No conditional form is computed.
The probability-to-gap inference itself needs an additional transition
estimate. For example, on three states with measure ((1-p)/2,(1-p)/2,p),
take conductances c_12=(1-p)gamma_s/4 and c_23=eta p(1-p). The conditional
gap on the first two states is exactly gamma_s. But the indicator of the
third state has variance p(1-p) and energy eta p(1-p), so the full gap
is at most eta, however small p is. Thus gamma_s(1-p) is not a valid
general lower bound. This finite counterexample tests the inference,
not the Wilson gap. The missing inter-sector control is not supplied
by calling the proposed sector split a Balaban construction.

The supplied Jaffe--Witten guidance, section 6.5, page 11, describes the
still unmet continuum passage: "One must then verify the existence of limits
of appropriate expectations of gauge-invariant observables as the lattice
spacing tends to zero and as the volume tends to infinity."
