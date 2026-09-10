# SC17: thermodynamic vacuum, closed ground-law form and plaquette overlap

9 September 2026. Analytic continuation of
[the SC17 spatial proof](wilson-sc17-spatial-closure.md), with the same
actual SU(2) Hamiltonian, unit-S3 link metric and physical coefficient epsilon.
The fixed-coupling regime is 0<=lambda<=lambda_c. Exponential spatial and
boundary rates hold for lambda<lambda_c; the endpoint follows by uniform
coupling continuity. Here lambda_c is the root in (1/73,1/72) of
6561lambda^4+1458lambda^3-81lambda^2-72lambda+1=0.

This derivation constructs the canonical equal-time vacuum law from free
and periodic finite boxes, proves closability of its actual cylinder-gradient
form, and obtains a conservative self-adjoint generator with a simple vacuum
and full/physical gap at least 4epsilon/3. For the elementary plaquette
O=Tr(U_p)/2, D=24pi lambda and f=O-mu(O), it also proves

\[
\left\|\mathbf1_{[4\epsilon/3,\,32\epsilon e^D]}
(K_{\mu,\mathrm{phys}})f\right\|^2\ge e^{-D}/8>0.
\]

These analytic results have a narrower scope than complete isolated-shell
identification or physical-time continuum reconstruction. The exact next
large-coupling defect and source-matching obligations remain in the linked
SC17 proof. No new Lean formalization is claimed.

## Part I. Actual cut response and the thermodynamic limit
## T1. Uniform setting including an actual cut interpolation

Work first on one finite periodic cubic ambient lattice, side L>=3, with
the full product SU(2) link space, unit-S3 metric, epsilon>0. Permit
inhomogeneous plaquette coefficients J_p in [0,k], and set

    H_J=-epsilon sum_e Delta_e+sum_p J_p s_p,
    lambda=k/epsilon<lambda_c,

where lambda_c is the first positive root of
6561lambda^4+1458lambda^3-81lambda^2-72lambda+1, with
1/73<lambda_c<1/72.

Every term is gauge invariant. All electric links of the ambient torus
are retained, including links outside a selected finite subsystem.
The SC17 proof is uniform over these coefficient arrays: its inputs
are only ||grad_e V||<=4k, ||V_ef||<=k n_ef, the four-plaquette link
incidence, and the twelve-neighbor source row. Reducing or varying
plaquette coefficients within [0,k] cannot increase those bounds.

Let Omega_J be the positive L2-normalized ground, u_J=log Omega_J,
mu_J=Omega_J^2dU, and K_J=Omega_J^{-1}(H_J-E_J)Omega_J. Freeze the
optimized SC17 constants at any fixed positive upper endpoint
lambda_bar in [lambda,lambda_c). With

    b=3lambda_bar+27lambda_bar^2,
    mu_bar=4/3-4b,
    q=(1+mu_bar^2/(96lambda_bar))/2>1,
    S=mu_bar/4=1/3-b,

the proved weighted estimate gives

    h_ei=sup_U ||(X_i X_e u_J)(U)||op,
    h_ee<=b,
    sup_e sum_(i!=e) q^d(e,i) h_ei<=S,
    B=b+S<=1/3,
    m0=4/3-2B>=2/3>0.                                   (T1)

The raw diagonal derivative matrix is allowed here: the exact Killing
commutator equation uses that matrix, and the reanchoring argument
already bounds its operator norm. No covariant-to-raw replacement is
needed. Keeping these constants fixed throughout the coupling
interpolation is essential: the spatial weight does not vary with theta.
At lambda=0 choose any fixed positive lambda_bar<lambda_c; the exact
Haar conclusions also hold directly.

For a convenient uniform rational regime, lambda<=1/73, one can instead
freeze

    b=246/5329, S=2/7, q=1025/1024,
    B=12380/37303<1/3.

The stronger small-window choice lambda<=1/640 is retained as a
subsidiary corollary: b<=1/200, S=1/64, q=17/16 gives
B<=33/1600 and m0>=3101/2400.

Take two arrays J^0,J^1 in [0,k] and interpolate J^theta=(1-theta)J^0+
theta J^1. Let

    W=sum_p (J_p^1-J_p^0)s_p,
    S_W=union of the links of plaquettes with J_p^1!=J_p^0.

Then ||grad_e W||<=4k for every e, and grad_e W=0 off S_W. W may
contain an extensive number of plaquettes and either sign. These facts
are sufficient; no bound on its extensive operator norm is used. If
S_W is empty the two Hamiltonians coincide and all response bounds
below are trivial.

## T2. Weighted gradient contraction from the actual charged equations

Fix theta. For any smooth gauge-invariant scalar f, let P_t f=e^{-tK}f
and g_e(t)=grad_e P_t f, represented by the three left Killing fields.
The exact differentiated equation is

    partial_t g_e=-K g_e+2epsilon sum_i H_ei g_i,
    H_ei=(X_i X_e u).                                     (T2)

The sign of the coupling term is plus. It follows by differentiating
K=-epsilon(Delta+2grad u.grad), using the Killing identity and the
commutation of each Killing field with Delta. Matrix multiplication
in the last term orders the e component first.

Gauge invariance of P_t f makes g_e adjoint-covariant at the tail of e.
The already proved charged semigroup estimate is therefore available:
its L-infinity contraction has damping exp(-4epsilon t/3). For any
nonempty source set Y, define the fixed spatial weights

    w_e=q^dist(e,Y),
    M_f(t)=max_e w_e ||grad_e P_t f||infinity.

The distance inequality w_e/w_i<=q^d(e,i) and T1 give, exactly,

    M_f(t)<=e^(-4epsilon t/3) M_f(0)
       +2epsilon B int_0^t e^[-4epsilon(t-s)/3] M_f(s)ds.

Gronwall after multiplication by exp(4epsilon t/3) proves

    M_f(t)<=exp(-epsilon m0 t) M_f(0).                    (T3)

This is a spatially weighted estimate for the actual ground-transformed
diffusion, not a locality assumption about its drift. At fixed finite
volume all weights and derivatives are finite; the displayed constants
are independent of volume and of the size of Y.

## T3. The normalized actual vacuum response has no boundary-area loss

At fixed finite volume, bounded smooth W and the simple isolated ground
permit differentiating in theta. Set v=partial_theta log Omega_theta.
The L2 normalization and the differentiated ground equation give

    mu_theta(v)=0,
    K_theta v=-(W-mu_theta(W)).                           (T4)

Thus, for h_e=grad_e v, the exact charged response is

    h_e=-R_x grad_e W+2epsilon R_x sum_i H_ei h_i.          (T5)

Here x is the tail of e and ||R_x||infinity<=3/(4epsilon).
Using the weights w_e=q^dist(e,S_W), with weight one on the force
support, gives for M_v=max_e w_e||grad_e v||infinity

    M_v<=3lambda+(3/2)B M_v,
    M_v<=4lambda/m0.                                     (T6)

The unknown neutral inverse in T4 was not assigned a gap: its
differentiated feedback term is retained and absorbed using the
proved Hessian row. The source is bounded per link, so the number of
changed plaquettes does not enter T6.

For a smooth local gauge-invariant multiplication observable O, exact
differentiation of the normalized ground square-density gives

    partial_theta mu_theta(O)=2Cov_mu(O,v).                (T7)

The factor two is essential. At fixed finite volume the positive smooth
ground law on a compact product has only constants in ker K; hence
P_t v tends to mu(v)=0. Integration by parts gives the exact covariance
formula

    Cov_mu(O,v)
      =epsilon int_0^infinity sum_e
          mu(<grad_e O,grad_e P_t v>) dt.                 (T8)

No factor 1/2 is hidden in T8: its integrand is the ordinary Riemannian
gradient inner product for K=-epsilon(Delta+2grad u.grad).
Apply T3 to v with Y=S_W, then T6. Absolute convergence of T8 follows
from the resulting exponential time bound. Since O has finite support X,

    |partial_theta mu_theta(O)|
      <=(8lambda/m0^2) sum_(e in X)
           ||grad_e O||infinity q^[-dist(e,S_W)].         (T9)

For the optimized interval B<=1/3, one has 8/m0^2<=18. Therefore

    |mu_(J^1)(O)-mu_(J^0)(O)|
      <=18lambda sum_(e in X)||grad_e O||infinity
                                q^[-dist(e,S_W)].        (T10)

In particular, T10 holds throughout lambda<=1/73 with q=1025/1024.
For lambda<=1/640 the stronger constants give

    8/m0^2<=46080000/9616201<5,

so the same conclusion has coefficient 5lambda and q=17/16.
T10 uses theta
integration over [0,1] and the bounds already uniform over that interval.
There is no boundary area, volume, vacuum energy, or spectator factor.

## T4. Actual exponential covariance localization

The same proof supplies a useful direct check. For a second smooth local
gauge-invariant observable A supported in Y, let
D_A=max_(e in Y)||grad_e A||infinity. T3 starts with M_A(0)=D_A. Thus

    |Cov_mu(O,A)|
      <=(D_A/m0) sum_(e in X)||grad_e O||infinity
                                       q^[-dist(e,Y)].   (T11)

One may take the smaller of this expression and its symmetric version
interchanging O,A. This is an actual signed covariance localization
derived from the Hamiltonian equations, not a global Poincare estimate
multiplied by the size of a distant boundary.

## T5. Fixed-lambda thermodynamic Cauchy convergence

On the standard infinite cubic lattice, define a finite free-boundary
Hamiltonian H_Lambda using links in a finite box and plaquettes whose
four links lie in that box. To compare nested Lambda_1 subset Lambda_2,
embed both in a sufficiently large periodic ambient torus and retain
free electric Hamiltonians on every other ambient link. Its ground is
the desired finite-box ground times the constant exterior ground, so
local expectations are exactly the finite-box expectations, independently
of the chosen ambient size.

Set J^0_p=k on plaquettes of Lambda_1 and zero elsewhere, and J^1_p=k
on plaquettes of Lambda_2 and zero elsewhere. Their interpolation is
precisely T1. It includes both boundary-crossing and entirely exterior
new plaquettes. Their extensive count is harmless because T9 uses their
bounded local derivatives.

Let R_(Lambda_1) be the link-graph distance from X to the union of links
of plaquettes not wholly contained in Lambda_1. For any larger Lambda_2,
the changed-plaquette support has distance at least R_(Lambda_1), so

    |mu_(Lambda_2)(O)-mu_(Lambda_1)(O)|
       <=18lambda L_O q^[-R_(Lambda_1)],
    L_O=sum_(e in X)||grad_e O||infinity.                  (T12)

As the inner boxes exhaust the lattice, R_(Lambda_1) tends to infinity.
This proves uniform Cauchy convergence of every fixed smooth local
gauge-invariant observable expectation at every fixed
0<=lambda<lambda_c, with fixed epsilon>0 and a fixed upper endpoint
strictly below lambda_c used to choose q. In particular this is uniform
throughout lambda<=1/73 with the displayed rational q. Two nonnested exhaustions are
compared through a common large inner box, proving independence of the
free-box exhaustion. Periodic finite boxes have the same limit: compare
their torus Hamiltonian to a large central free box by setting all
plaquette coefficients outside that inner box to zero, and apply T10
before taking its interior radius to infinity.

Smooth cylinder functions are uniformly dense in continuous cylinder
functions on the compact link group. Expectations have norm one, so
the conclusion extends to continuous local gauge-invariant observables.
For general continuous local observables, average over the finitely many
gauge transformations at their incident vertices; this preserves their
support, and every finite-volume expectation equals that of the averaged
observable. Thus the limits define consistent positive normalized local
functionals, or equivalently a gauge-invariant equal-time probability
measure on the countable product of link groups.

The finite-volume full Poincare inequality also passes to smooth local
cylinder functions of this measure, by convergence of the finitely many
expectation terms involved. Part II constructs and closes the resulting
ground-law generator. Identification of the full operator-algebra vacuum,
physical-time correlation limits and source/carrier transport requires
additional arguments and is not asserted here.

## T6. Precise scope of the boundary independence

All comparisons above preserve the full ambient gauge symmetry and
change only gauge-invariant plaquette coefficients within [0,k]. They
include free and periodic finite-volume exhaustions via an ambient
product embedding. They do not prove independence from arbitrary
deterministically frozen, gauge-breaking boundary link values. Such
boundaries require their actual gauge/charged estimates or a separate
boundary construction.

The physical lattice spacing and lambda are fixed in T12. The bound
does not continue along lambda=(c_B/c_E)g^(-4) tending to infinity, and
the rate log(q) is in lattice link-distance units. No continuum
claim or source-frame identification is imported through this limit.

## T7. Endpoint continuity also gives a thermodynamic limit at lambda_c

This is a separate consequence and does not assert exponential boundary
decay at the endpoint. The optimized SC17 proof gives at lambda_c the
unweighted q=1 row with b_c+S_c=1/3: the nonstrict scalar barrier still
cannot be crossed at any finite time, and the ground limit preserves it.
Thus the gradient contraction and normalized response proof above remain
valid with spatial weights one and m0>=2/3.

For any fixed finite-volume plaquette set, interpolate its common
coupling from lambda' to lambda_c. Now the source satisfies
||grad_e W||<=4epsilon|lambda_c-lambda'|. Repeating T6-T9 yields

    |mu_(Lambda,lambda_c)(O)-mu_(Lambda,lambda')(O)|
       <=18|lambda_c-lambda'| L_O,                       (T13)

uniformly in volume. The same bound holds between any two couplings
in [0,lambda_c], by freezing the q=1 constants at lambda_c.

Given two sufficiently large volumes and lambda'<lambda_c, their
expectation difference at lambda_c is therefore bounded by

    36(lambda_c-lambda') L_O
       +|mu_(Lambda_2,lambda')(O)-mu_(Lambda_1,lambda')(O)|.

First choose lambda' sufficiently close to lambda_c, then use T12 at
that fixed lambda'. This proves thermodynamic Cauchy convergence at
lambda_c as well. The same argument identifies the periodic and free
limits there and gives coupling-continuity of the limiting local state.
The uniform exponential spatial rate remains proved only strictly below
lambda_c; the endpoint extension is by uniform coupling continuity.

## Uniform score limits discharge the form construction's local input

In the same ambient embedding, integrate T6 for a fixed link e between
nested finite boxes. At the decoupled endpoint the smaller-box logarithmic
ground score is exactly its extension independent of exterior links. Thus

    ||F_(e,Lambda_2)-F_(e,Lambda_1)||infinity
       <=(4lambda/m0) q^[-dist(e,S_W)]
       <=6lambda q^[-dist(e,S_W)].

The right side tends to zero with the inner box. Each score is a continuous
cylinder on the infinite compact product; its uniform limit F_e is therefore
continuous and quasilocal, with ||F_e||infinity<=3lambda. Periodic and free
interior embeddings have the same limit by the same comparison.

At lambda_c, the coupling version of T6 gives exactly

    ||F_(e,Lambda,lambda_c)-F_(e,Lambda,lambda')||infinity
       <=6|lambda_c-lambda'|.

For two volumes use twice this bound and then score convergence at fixed
lambda'<lambda_c. This proves the required uniform score Cauchy property
at the endpoint. No exponential boundary rate at lambda_c is asserted.
The full-space Poincare estimate used next was proved before physical
restriction by the product weighted-curvature argument in the SC17 note.

## Part II. Infinite-volume form, physical restriction and actual observable overlap
## 1. Precisely sufficient thermodynamic inputs

Let E be the countable link set of the infinite cubic lattice and
X=SU(2)^E with its compact metrizable product topology. For finite volumes
Lambda let mu_Lambda=Omega_Lambda^2 dU be the actual normalized ground law.
Extend these measures to X by an arbitrary consistent outside product Haar
law; for periodic approximants, use their usual interior-cylinder embedding.
Only cylinders eventually lying inside the nonwrapped interior are used.

The inputs established in Part I and the SC17 proof are:

1. The actual cut-response estimates yield a unique weak limit mu on local
   continuous observables, independent of the chosen admissible exhaustion.
2. For each fixed link e, the actual logarithmic scores
   F_(e,Lambda)=(X_e^a log Omega_Lambda)_a, extended as functions on X,
   converge uniformly to a continuous quasilocal vector F_e. Their bounds
   include ||F_e||_infinity<=3lambda. Uniform Cauchy convergence follows from
   summing the score response along the finite-range cut, with the actual
   cut incidence/boundary multiplicities retained.
3. The finite-volume full-space Poincare estimate is

       Var_(mu_Lambda)(f) <= [3/(4epsilon)]
                   epsilon sum_e integral |grad_e f|^2 dmu_Lambda,   (IF1)

   for every smooth cylinder observable in the volume. The SC17
   product weighted-Ricci lower bound gives
   this full-space estimate, before physical restriction.

These are actual ground-law inputs. No globally defined Omega_infinity
relative to infinite product Haar is inferred: the limiting probability
measure can be singular to that product law.

## 2. Exact infinite-volume integration by parts

Let C be the algebra of smooth cylinder functions. Each member depends on
finitely many links. Let X_e^a be the same left-translation Killing derivative
used in SC1-SC17, skew-adjoint for finite product Haar. Put beta_e^a=2F_e^a.
For f,g in C, finite-volume Haar integration by parts is exactly

    integral (X_e^a f) g dmu_Lambda
      =-integral f [X_e^a g+2F_(e,Lambda)^a g] dmu_Lambda.   (IF2)

Uniform score convergence and weak convergence of mu_Lambda give

    integral (X_e^a f) g dmu
      =-integral f [X_e^a g+beta_e^a g] dmu,               (IF3)
    ||beta_e||_infinity<=6lambda.

All limiting integrands are bounded continuous functions on X; multiplying
the uniform score error by bounded fg justifies the only noncylinder term.
For complex functions put a conjugate on g. Equation (IF3) identifies the
actual logarithmic derivative of mu. It needs no formal infinite product
density or infinite vacuum energy subtraction.

## 3. Closability and the canonical closed form

C is uniformly dense in C(X) by Stone-Weierstrass/Peter-Weyl and hence dense
in L2(mu). Define on C

    Df=(X_e^a f)_(e,a) in ell2(E x {1,2,3}; L2(mu)),
    E_mu(f,g)=epsilon sum_(e,a) integral (X_e^a f)(X_e^a g) dmu. (IF4)

Only finitely many derivative components are nonzero on a cylinder.
Suppose f_n tends to zero in L2 and Df_n tends to v in the displayed
Hilbert direct sum. For any fixed e,a and any g in C, (IF3) gives

    <v_e^a,g> = lim <X_e^a f_n,g>
      =-lim <f_n,X_e^a g+beta_e^a g>=0.

The vector on the right is in L2 because beta_e is bounded. Density of C
shows v_e^a=0 for every component, hence v=0. This proves D is closable.
Consequently E_mu is closable; denote its closure by (E_mu,D(E_mu)).

The cylinder chain rule proves the normal-contraction inequality, first
for smooth normal contractions and then by approximation. Its closure is
therefore a symmetric Dirichlet form. It is regular on compact X: C is
both a form core by construction and uniformly dense in C(X). The closed
form defines a nonnegative self-adjoint operator K_mu through the usual
representation theorem. Since 1 is a cylinder, E_mu(1)=0 and

    exp(-tK_mu)1=1.                                       (IF5)

Thus the associated Markov semigroup is conservative and mu-preserving.

For a smooth cylinder f the finite sum

    L_mu f=epsilon sum_(e,a)[(X_e^a)^2 f+beta_e^a X_e^a f]  (IF6)

is a bounded continuous function and belongs to L2(mu). Integration by
parts gives E_mu(f,g)=<-L_mu f,g> first for cylinder g and then, by form-core
approximation, for all g in D(E_mu). Therefore f belongs to D(K_mu) and

    K_mu f=-L_mu f.                                       (IF7)

This proves an actual operator action, not only a formal generator. C is
a form core; no essential self-adjointness/operator-core claim beyond this
is needed or inferred.

## 4. Gauge invariance and the physical closed subspace

Every finite-volume vacuum law is invariant under its exact vertex gauge
action. For a fixed cylinder and a finite-support vertex gauge transform,
all links needed by that test lie in the finite-volume interior eventually.
Passing expectations to the limit proves invariance of mu under all such
transforms. Each local test depends on only finitely many gauge variables,
so the statement extends to the full compact product gauge group
G_site=SU(2)^(vertices).

The induced action U_h on L2(mu) is unitary and strongly continuous.
Gauge transformations rotate the three link derivatives orthogonally;
therefore E_mu(U_h f,U_h f)=E_mu(f,f) on cylinders and then on the closed
form domain. Its resolvent and semigroup commute with U_h.

Let H_phys be the closed fixed-vector subspace, equivalently the invariants
under all finite-support gauge transforms. Haar averaging over G_site is
the orthogonal projection P_phys. Averaging a cylinder uses only the finitely
many endpoint gauge variables of its supporting edges and produces a smooth
gauge-invariant cylinder with the same edge support. Jensen's inequality
and form invariance make P_phys a form contraction. Hence invariant smooth
cylinders are a form core for the restricted physical form. K_mu reduces
H_phys and defines its physical self-adjoint restriction K_mu,phys.

## 5. Passing the full and physical Poincare floor

For a fixed smooth cylinder f, both f, f^2 and |grad f|^2 are
continuous cylinders. Weak convergence in (IF1) yields

    Var_mu(f)<= [3/(4epsilon)] E_mu(f).                    (IF8)

Extend through the cylinder form core. The constant vector is the only
zero-energy vector. Spectral calculus and physical restriction give

    spectrum(K_mu) subset {0} union [4epsilon/3,infinity),
    ker K_mu=span{1},
    spectrum(K_mu,phys) subset {0} union [4epsilon/3,infinity),
    ker K_mu,phys=span{1}.                                (IF9)

Thus the finite-volume actual Poincare estimate survives on both the full
ground-law space and its physical gauge-invariant subspace in the
constructed fixed-spacing infinite-volume vacuum representation.

## 6. Actual nonzero local observable overlap with a bounded energy band

Take a fixed elementary plaquette and O(U)=Tr(U_p)/2, a bounded smooth
gauge-invariant cylinder. Its support has four distinct links. The proven
score bound and shortest SU(2) link geodesics of length at most pi imply

    osc_B log Omega_Lambda <=12pi lambda,
    osc_B log[mu_Lambda(.|outside)/dU_B] <=D,
    D=24pi lambda.                                        (IF10)

Every normalized conditional density relative to product Haar therefore
has pointwise lower bound exp(-D). Using the variational formula for
variance gives

    Var_(mu_Lambda)(O) >= E Var(O|outside)
      >=exp(-D) Var_(Haar)(O)=exp(-D)/4.                   (IF11)

The last equality is exact: the plaquette product is Haar-distributed and
the normalized SU(2) fundamental trace has Haar variance 1/4. Pass (IF11)
to mu by weak convergence. On each of the four links the unit-S3 gradient
has squared norm 1-O^2<=1, so

    v=||O-mu(O)||_L2(mu)^2 >=exp(-D)/4,
    E_mu(O)<=4epsilon.                                    (IF12)

Put f=O-mu(O), and let sigma_f be its spectral measure for K_mu,phys.
It is supported in [4epsilon/3,infinity), its total mass is v, and its
first moment is E_mu(f)<=4epsilon. For M=32epsilon exp(D), Markov's first-
moment bound gives

    sigma_f((M,infinity)) <=4epsilon/M=exp(-D)/8,

and hence the actual projection estimate

    ||1_[4epsilon/3,32epsilon exp(D)](K_mu,phys) f||^2
       >= exp(-D)/8 >0.                                  (IF13)

This is an actual nonzero gauge-invariant observable overlap with a bounded
physical-energy interval in the constructed infinite-volume representation.
The constants are uniform in total volume at fixed coefficients in the
proved SC17 regime. This is stronger than merely assigning a positive
spectral weight in a finite simulation.

It does not identify an isolated eigenvalue, a complete excited-shell rank,
a source frame, or the exact retained carrier of the matching theorem.
It also does not make the band endpoints or weight uniform through a
continuum trajectory on which epsilon and lambda change. The word 'band'
here denotes a spectral interval, not an assertion of particle dispersion.

## 7. Physical-time identification and remaining scope

K_mu is the canonical self-adjoint generator of the closed equal-time
ground-law cylinder-gradient form. Its coefficients are the actual local
limits of finite-volume ground scores, and it has the actual spectral floor
and plaquette interval overlap proved above. No free or phenomenological
reference measure appears in (IF3)-(IF13).

The subsequent [physical-time proof](wilson-sc17-physical-time-limit.md)
supplies the additional identification. Actual uniform score limits give
convergence of the free/periodic stationary ground-transformed processes.
The specified closed form's coordinate martingales solve the same uniquely
solvable Hilbert SDE, identifying its semigroup with exp(-t K_mu). Hence all
bounded continuous cylinder multitime vacuum correlations converge to this
physical Euclidean-time semigroup at fixed spacing, through lambda_c.
No operator-core premise is used. The endpoint uses a summable
influence-dependent weight and does not acquire an exponential spatial rate.

This does not prove spatial-continuum reconstruction, Lorentz invariance,
an isolated complete shell or matched continuum source frame. Those require
the actual cross-scale identifications and estimates in the G19 chain.

