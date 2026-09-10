# Exact finite-g source transport and its domain boundary

9 September 2026. This audits the actual twelve-edge 2x2 block against
the source-domain requirement in `wilson-selected-inverse-wall.md`,
lines 110-125: the displayed graph vector must belong to the interacting
form domain before its residual is formed.

## 1. A globally defined exact source isometry

Let Psi_g be the normalized positive ground in the original compact
physical Hilbert space. Put

    w=Tr(U2 U3)/2, r=4(1-w)/g^2, L=8/g^2,
    nu_g=d(r)_*(Psi_g^2 dHaar), 0<r<L.

The product-to-U2U3 map preserves product Haar after the change of
variables (U2,U3) -> (U2,U2U3). Integrating the smooth strictly positive
ground density over the other three group variables gives a smooth,
strictly positive class density h_g(w). Consequently

    dnu_g(r)=g^4/(8pi) h_g(1-g^2 r/4) sqrt(r(L-r)) dr.        (D1)

Every statement here is for fixed g>0; no uniform lower bound on h_g is
being inserted. Strict positivity and smoothness follow from the actual
elliptic compact Hamiltonian: its four direct horizontal edge derivatives
alone span the four group factors.

Let mu0 be the actual retained Gaussian law, Gamma(shape 3/2, scale
theta=2sqrt(2)), with cumulative distribution F0. Let Fg be the cumulative
distribution of nu_g. The exact monotone map

    tau_g(r)=F0^(-1)(Fg(r))                                  (D2)

maps (0,L) bijectively to (0,infinity). Define

    Jg phi(U)=Psi_g(U) phi(tau_g(r(U))).                       (D3)

Then ||Jg phi||^2=||phi||^2_L2(mu0), its range is exactly the literal
retained source algebra times the true ground, and Jg 1=Psi_g. This is
a genuine global source isometry; the bounded compact observation has
not silently been identified with an unbounded Gaussian variable.

On the previously established coefficient core a1=m1=0. Differentiating
the cumulative transport gives tau1(r)=-integral_0^r nu1(s)ds/mu0(r)=0.
Thus (D3) has the same complete first source jet as the calculated K:
J1 phi=Omega0 p1 phi. This assertion uses the fixed-cell coefficient
expansion, not a global remainder estimate over all source energies.

## 2. Exact failure of the Gaussian form-domain extension

The original eight boundary edges give Gamma(w,w)=2(1-w^2). Therefore
the exact vacuum-subtracted scaled form on the source is

    h_g[Jg phi]
      = integral_0^L r(8-g^2r) |tau_g'(r)|^2
                         |phi'(tau_g(r))|^2 dnu_g(r).        (D4)

After pushforward to mu0 this is a closed weighted radial form with
weight w_g(tau)=r(8-g^2r)tau_g'(r)^2. Its domain need not contain the
Gaussian source form domain

    b[phi]=8 integral_0^infinity a |phi'(a)|^2 dmu0(a).       (D5)

In fact it does not, for every fixed g>0. Write epsilon=L-r. Equation
(D1) and positivity at w=-1 give

    dnu_g/dr ~ c_g epsilon^(1/2),
    1-Fg(r) ~ (2c_g/3) epsilon^(3/2),  c_g>0.

The Gamma tail is proportional to a^(1/2) exp(-a/theta). Equating tails
in (D2) gives the exact endpoint asymptotics

    epsilon ~ C_g a^(1/3) exp[-a/(3sqrt(2))],
    tau_g'(r) ~ 3sqrt(2)/epsilon,
    w_g(a) ~ C'_g a^(-1/3) exp[a/(3sqrt(2))].                (D6)

All constants here are finite and strictly positive at the fixed g.

An explicit vacuum-orthogonal Gaussian source with b[p]=1 is

    p(a)=sqrt(2/3) [exp(a/(8sqrt(2)))-(4/3)^(3/2)].          (D7)

Indeed the Gamma moment generating function gives
E[exp(a/(8sqrt(2)))]=(4/3)^(3/2) and the unnormalized exponential has
Gaussian source energy 3/2. Its Gaussian L2 norm and Gaussian energy
are finite. But its compact energy integrand in (D4), expressed in a,
has asymptotic exponential factor

    exp[(1/(4sqrt(2))+1/(3sqrt(2))-1/(2sqrt(2)))a]
       =exp[a/(12sqrt(2))].                                 (D8)

Therefore h_g[Jg p]=infinity for every fixed g>0.

This is a specific failure of extending this exact source isometry from
all finite-Gaussian-energy sources into the interacting form domain.
It does not negate the dense common core: every phi in
C_c^infinity((0,infinity)) is mapped by (D3) to a smooth compact source
supported away from both coarse endpoints, and is admissible. It does
show that a proof on that core cannot simply assert the all-b extension
without proving the required continuous residual extension separately.

An even more literal identification, phi -> Psi_g phi(r) times any
pointwise density factor on (0,L), fails already as an L2 isometry:
a nonzero phi supported in (L+1,L+2) is sent to zero. Equivalently, a
unitary cannot intertwine multiplication by the bounded r and the
unbounded Gaussian a as the same observable.

## 3. A compact reference that removes this endpoint mismatch

There is a canonical exact alternative when a compact reference is used.
Keep the fixed source interval w in (-1,1) and the Haar class law

    dmu_H(w)=(2/pi)sqrt(1-w^2)dw.

Let F_H be its cumulative distribution and F_g^w the cumulative
distribution of the true compact coarse law h_g(w)dmu_H(w). Define

    eta_g(w)=F_H^(-1)(F_g^w(w)),
    I_g f(U)=Psi_g(U) f(eta_g(w(U))).                         (D9)

This is an exact source isometry from the fixed compact reference
L2(mu_H), maps 1 to the true vacuum, and preserves the entire physical
retained algebra. Both endpoint densities have exponent 1/2, so eta_g
extends to a smooth monotone endpoint map with finite nonzero endpoint
derivatives at fixed g. Its pulled-back source energy is

    g^2 integral (1-w^2) eta_g'(w)^2
                          |f'(eta_g(w))|^2 h_g(w)dmu_H(w).

After changing variables to eta, its weight is comparable, above and
below with finite positive constants depending on g, to 1-eta^2.
Thus its source form domain is exactly

    D_H={f in L2(mu_H): integral(1-eta^2)|f'(eta)|^2dmu_H<infinity}.

The untransported full compact Hamiltonians for all positive g already
share the physical H1 form domain, because their electric part differs
only by a positive scalar and their magnetic potentials are bounded on
the fixed compact configuration space. Hence this reference supplies a
concrete common-domain formulation of finite-g source/fast forms.

The moving projections are also explicit on the fixed compact Hilbert
space:

    P_g f=Psi_g E_Haar[Psi_g f | w]/h_g(w).                  (D10)

On any closed positive-coupling interval these projections are norm
smooth: Psi_g and its derivatives are bounded and h_g has a positive
minimum. Their Kato projection transport solves

    U'_g=[P'_g,P_g]U_g.

It gives an exact full-Hilbert unitary intertwining the source ranges.
The retained unitary relating U_g I_(g*) to I_g fixes the source
parameterization in (D9); extending that retained unitary by the identity
on the reference complement specifies a full source-compatible unitary.

This transport also preserves the common FORM domain, not only L2. Here
is the finite-positive-coupling proof. Fix a closed interval
I=[g_min,g_max] with g_min>0 and use the usual physical H1 norm on the
compact product SU(2)^4.

* The change of variables (U2,U3)->(U2,U2U3) is a smooth diffeomorphism
  of a compact manifold, so it and its inverse act boundedly on H1.
  In these variables conditional expectation onto the product group
  coordinate consists of integration over three compact group factors.
  Differentiation in the remaining coordinate commutes with that
  integration, and Cauchy-Schwarz gives its H1 bound. Passing to the
  trace coordinate is conjugation averaging on SU(2), an H1 contraction
  because conjugations are isometries for its bi-invariant metric.
  Pulling the resulting class function back to the product variables
  is bounded on H1 by the same change of variables. Thus E_Haar[.|w]
  in (D10) is a bounded H1 operator.
* Psi_g and its first g derivative are smooth on the compact manifold,
  with bounded C1 norms for g in I. The same holds for the smooth
  class functions h_g and its g derivative, and inf_(g in I,w)h_g(w)>0.
  Multiplication by Psi_g, its derivative, h_g^(-1), and its derivative
  is therefore bounded on H1, uniformly on I. Formula (D10) gives
  uniformly bounded, norm-continuous H1 operators P_g and P'_g.
* Consequently [P'_g,P_g] is bounded and norm-continuous on H1. Its
  ODE has an invertible bounded H1 evolution with norm and inverse norm
  at most exp(C_I |g-g*|). Uniqueness of the ODE in L2 identifies this
  evolution with the Kato unitary U_g. Hence U_g H1=H1 exactly.
* The CDF map eta_g in (D9) lifts to a smooth conjugation-equivariant
  diffeomorphism of SU(2): send cos(theta) to eta_g(cos(theta)) while
  preserving the quaternion direction. Near theta=0 its new angle is
  sqrt(eta'_g(1))theta+O(theta^3); the analogous expansion holds near
  theta=pi. The expansions have smooth even coefficients because both
  marginal densities have the same square-root endpoint factor.
  Thus no polar singularity is introduced. This diffeomorphism and
  its inverse have bounded derivatives on I. Their pullbacks preserve
  the radial H1 domain D_H. Together with the preceding averaging and
  multiplication bounds this proves I_g:D_H->H1 and
  I_g^*:H1->D_H are bounded, uniformly for g in I.

For clarity, the final full unitary can be written explicitly. Put

    I*=I_(g*), P*=I* I*^*, Q*=1-P*,
    S_g=I*^* U_g^* I_g,
    R_g=U_g [I* S_g I*^*+Q*].

S_g is unitary on the retained L2 space and maps D_H onto itself by the
displayed bounds. Hence R_g is a full physical L2 unitary,
R_g I*=I_g, and R_g H1=H1 with bounded inverse on H1. The transported
forms h_g[R_g .] therefore have the SAME compact physical H1 domain.
This supplies an actual source-compatible common-form transport on I.

All constants in this construction depend on I and the true compact
ground, including its positive minimum and derivative bounds. No
uniform extension of these constants to g_min=0 is asserted. In
particular this compact common-form construction does not remove the
Gaussian endpoint counterexample (D7).

This compact reference has a different high-energy source scale from
the Gaussian reference. Its scalar Sturm-Liouville reference has
quadratic eigenvalue growth n(n+2), whereas the radial Gaussian source
has linear eigenvalue growth 2sqrt(2)n. No uniform Gaussian comparison
is implied by changing the reference.

The concrete choices are therefore: use (D3) on its admissible common
core and establish the precise residual extension, or use (D9) with
the displayed compact source domain. Formula (D7) identifies exactly
why the first choice cannot assume preservation of the whole Gaussian
energy domain.

Every fixed polynomial phi is also admissible under (D3): its energy
integrand is a polynomial factor times exp[-a/(6sqrt(2))] at infinity.
Thus the quantile domain issue does not invalidate any individual finite
Laguerre source calculation. It appears when one attempts the full
Gaussian-energy completion without a new bound.

## 4. The retained norm to use in the next finite-g calculation

There are three distinct norms; they should not share the same symbol:

    b0[phi]=8 integral a|phi'(a)|^2 dmu0(a),
    b_g^compact[f]=integral_0^L r(8-g^2r)|f'(r)|^2dnu_g(r),
    b_g^transport[phi]=b_g^compact[phi composed with tau_g].  (D11)

The already proved all-energy Gaussian force and first-residual estimates
use b0. The actual finite-g retained electric energy is b_g^compact;
in the exact Gaussian probability coordinate it is b_g^transport.
Replacing b0 by this last form is an explicit change of target, not an
automatic consequence of the coefficient calculation. Equation (D7)
proves that their full form domains are different.

A concrete common source core is

    C=C_c^infinity((0,infinity)),
    C_g={phi composed with tau_g: phi in C}.

Every C_g source is smooth and supported away from the two coarse
endpoints. Both b0 and b_g^transport are finite on C. Centering by the
respective mean preserves admissibility and both derivative energies.
For a compact-compatible formulation the final source closure should
use the norm ||phi||_mu0^2+b_g^transport[phi], or equivalently the
compact norm ||f||_nu_g^2+b_g^compact[f]. The compact Haar version (D9)
has the fixed weighted domain D_H instead.

The companion `finite_g_quantum_floor.md` establishes a fixed-square
physical floor at least 2 for sufficiently small positive g. Consequently
the literal fast form satisfies F_g>=2, and for real z<2 its inverse
has norm at most (2-z)^(-1). In this fixed block the missing estimate is
therefore a residual comparison, not a spectral floor assertion.

To preserve the original Gaussian-normalized W6 target, one must form
the complete finite-g residual on the displayed common core using a
specified full source-compatible transport, prove its continuity as
an interacting fast-form functional, and establish

    <rho_(g,phi),(F_g-z)^(-1)rho_(g,phi)>
         <= C g^2 b0[phi]  for every phi in C,                (D12)

with the desired small-g uniform constant. A bound with
b_g^transport on the right is a different, compact-compatible target.
Neither follows merely from the first coefficient bound. In particular,
source admissibility on C has now been constructed explicitly, while
the finite-g full residual extension in (D12) remains the concrete
comparison to calculate. No finite-g error estimate is asserted here.
