# Geometry, source transport, and residual certificates in the theory graph

10 September 2026. These derivations connect the recorded Hodge kernel,
anisotropy variance, full-reference Schur forms, scalar square source, and
abstract SC17 Riccati equation. They state their finite-order and physical
identification hypotheses separately. No claim of worldwide priority is made.

The companion `scripts/verify_theory_geometry_bridges.py` checks the exact
polynomial and rational matrix identities described below. Its finite matrix
controls do not certify an infinite-volume Wilson estimate. The named analytic
arguments remain distinct from the available Lean ingredients and any new
compiled declarations registered in the statement ledger.

## TG1: The sharp three-coordinate anisotropy constant

For exactly three nonnegative coordinates with x+y+z=1, put

    V(x,y,z)=xy(x-y)^2+xz(x-z)^2+yz(y-z)^2.

The established identity is V=sum x_i^3-(sum x_i^2)^2. The complete maximum is

    K3=(827+73 sqrt(73))/18432 < 2/25,
    V <= K3.                                                     (TG1)

Equality occurs at permutations of (a,a,1-2a), where

    a=(13-sqrt(73))/48.

Proof. A maximum exists on the compact simplex. On a boundary face, put s=xy.
Then V=s(1-4s), 0<=s<=1/4, whose maximum is 1/16. At an interior stationary
point, with S=sum x_i^2, Lagrange multipliers give

    3 x_i^2-4 S x_i=lambda.

This quadratic has at most two real roots, so two of the three coordinates
are equal. Setting x=y=a and z=1-2a gives

    f(a)=2a(1-2a)(3a-1)^2,
    f'(a)=-2(3a-1)(24a^2-13a+1),       0<=a<=1/2.

The endpoint values vanish. The critical points are 1/3 and
(13+/-sqrt(73))/48. Their values are 0 and
(827-/+73 sqrt(73))/18432. The larger exceeds 1/16, and the smaller does
not. This proves the maximum and its equality cases. At either quadratic
root, f(a)=(37-73a)/384, an exact polynomial-remainder check. Squaring the
positive sides of 73 sqrt(73)<18432(2/25)-827 proves K3<2/25.

This is dimension-specific. For FOUR coordinates, using the same pair sum,

    V(4/5,1/15,1/15,1/15)=484/5625 > 2/25 > K3.             (TG1a)

Thus neither the sharp constant nor its proof may be reused for a general
number of coordinates. The older universal probability-variance bound 1/4
has a different scope. The existing three-coordinate Lean algebra is in
[`AnisotropyVariance.lean`](../../lean/Workhouse/AnisotropyVariance.lean):
`anisotropy_variance_identity`, `anisotropy_variance_nonnegative`,
`anisotropy_variance_upper_bound`, and `anisotropy_variance_zero_iff`.
The sharp stationary-point argument is stronger than that file's 1/4 bound;
formal coverage must refer to the actual compiled statement, not its title.

## TG2: Zero extension and integrated energy bounds

Let a_i>=0, q=sum a_i, and x_i=a_i/q when q>0. Define

    E(a)=q V(a/q) if q>0, and E(0)=0,
    R(a)=q^2 V(a/q) if q>0, and R(0)=0.

Then 0<=E<=K3 q and 0<=R<=K3 q^2. Both functions extend continuously to
a=0 by these bounds. The normalized carrier p=psi/sqrt(q) and its projector
are still undefined at q=0; their direction-dependent limits are not repaired
by extending these scalar energy quantities.

For any positive measure and measurable f for which the right sides are
finite, the pointwise bounds give

    integral E |f|^2 <= K3 integral q |f|^2
                     <= (2/25) integral q |f|^2.                   (TG2)

The integrated inequalities are non-strict. They include f=0, measures
supported at q=0, and nodal supports. A strict comparison using K3<2/25
requires a strictly positive right-hand integral.

The recorded full fourth-order kernel satisfies

    ||Q H4 p||^2=4 C^2 q^2 V(a/q).

Consequently TG1 improves every bound obtained by inserting V<=1/4 into
this identity by a factor 1/(4K3), approximately 3.17637. Its exact kernel
identification remains the separate Laurent calculation in
[`anisotropy_variance.py`](../../src/workhouse/invariants/anisotropy_variance.py).
This concerns the in-sector fourth-order kernel and does not identify a
continuum physical source or the complete sixth-order Hamiltonian.

## TG3: One secular cubic for the recorded Hodge support

Match each plane component to its missing coordinate. Write

    U=psi psi*,  D=diag(a_1,a_2,a_3),  R=D-U,
    q=sum a_i,  e2=sum_(i<j) a_i a_j,  e3=a_1 a_2 a_3.

The identity R=D-U follows from the opposite cross-plane parts of the up
and down Laplacians. In this normalization ||psi||^2=q and U psi=q psi;
U is NOT psi psi*/q. The latter is the normalized projector when q>0.
These identifications are checked in
[`hodge_feshbach.py`](../../src/workhouse/invariants/hodge_feshbach.py).

For real alpha,b,c and H=alpha I+bU+cR, setting xi=lambda-alpha gives

    det(lambda I-H)=xi^3-bq xi^2+c(2b-c)e2 xi
                             -c^2(3b-2c)e3.                       (TG3)

Proof. Since H=alpha I+cD+(b-c)psi psi*, the determinant is

    product_i(xi-c a_i)
      -(b-c) sum_i a_i product_(j!=i)(xi-c a_j).

Collecting coefficients gives TG3. This polynomial identity also holds
when coordinates vanish and at q=0. The actual recorded support
{I,U,S,S^2,R} reduces to this form because
S=L_down-4I and S^2=(q-8)L_down+16I. See the exact decomposition in
[`gamma_isolation.py`](../../src/workhouse/invariants/gamma_isolation.py).

The rank-one multiplication also proves the renewal identity

    sigma(A U B)=sigma(A)sigma(B),  sigma(A)=psi* A psi.     (TG3a)

Thus sigma(RUR)=4 e2^2 is a factorized carrier return. It does not compute
the coefficient of RUR in a physical sixth-order expansion. In particular,
a census of ordinary lattice walks is not a substitute for the weighted
plaquette/representation histories and resolvents of that expansion.

Useful actual Lean objects are `VacuumChart.rankOne`,
`VacuumCompression.vacuum_projection`, and
`HodgeFeshbach.hodge_algebra_relations`. A proof about a polynomial defined
to equal the right side of TG3 would not establish the determinant theorem.

## TG4: The induced eighth-order moment in the same truncation

For q>0 use angular variables x_i=a_i/q and X=diag(x_i). Let

    M=q u^2[tQ+u^2 h],   h=eta I+beta P+cX,
    P=pp*, Q=I-P, |p_i|^2=x_i, t>0.

The assembled fourth-order specialization is c=-2C and
beta=A+2C-eta, with t=5/612 and A=5/48. Put

    m1=sum x_i^2, m2=sum x_i^3, m3=sum x_i^4,
    V=m2-m1^2, kappa3=m3-3m1 m2+2m1^3, mu=<p,hp>.

For the simple eigenbranch emerging from the retained line,

    E0=q[u^4 mu-u^6 c^2 V/t
          +u^8(c^3 kappa3-beta c^2 V)/t^2+O(u^10)].          (TG4)

This is a fixed-momentum small-coupling expansion of the displayed matrix.
Proof: its reduced unperturbed inverse is Q/t. With w=Qhp=cQXp, the second
coefficient is -||w||^2/t and the third is
<w,(h-mu)w>/t^2. Centering the weighted X moments gives the formula.
The sixth-order term is established input; TG4 continues that calculation
by one order. It does not include independent higher-order physical kernels.

At V=0 every positive x_i is equal, so Xp is proportional to p. Therefore
p is a simultaneous eigenvector of S,U,R and every word in these operators
preserves the carrier. Application to actual higher physical kernels needs
their identification with this generated algebra.

## TG5: Complete source motion is a Schur congruence

Use the full reference graph of
[`wilson-spatial-schur-excess.md`](wilson-spatial-schur-excess.md), SP1-SP7:

    A_z=H-z, F=Q A_z Q, J=(I,-U_z)^T, A_z J=i_P S(z).

All products below require the common invariant operator/form core and
bounded extensions appropriate to SP1-SP2. For an actual skew-adjoint
source connection K, define

    L=PKJ, C=QKi_P, Gamma=QKJ+U_z PKJ.

Then

    Q[H,K]J=F Gamma-C S,
    J*[H,K]J=S L+L* S.                                    (TG5)

Indeed KJ=JL+i_Q Gamma. Applying Q A_z and using A_zJ=i_PS proves the
first identity; skew-adjointness gives the second. The baseline cross
block is fully retained, as required by SP10. On shell S(z)p=0, the source
force has the fast factor F. Off shell the C S term remains; it must not
be omitted from a selected-force bound.

Suppose now the pulled physical family has derivative

    Hdot_g=D_g+[H_g,K_g],

where D_g is the transported physical derivative and K_g=U_g* Udot_g is
the actual source connection. Stationarity of the minimizing graph gives

    Sdot_g=J_g*D_gJ_g+S_gL_g+L_g*S_g.

The retained evolution Tdot_g=-L_g T_g, T_0=I therefore satisfies

    d_g(T_g*S_gT_g)=T_g*J_g*D_gJ_gT_g.                      (TG5a)

For pure source motion D_g=0 this is an exact invariant through every
order. It removes the direct and exchange source terms together.

For example, for constant K, W1=[H,K], W2=[[H,K],K]/2 and t=QW1J give

    Ldot=C*F^(-1)t,  D2=(L^2+Ldot)/2,
    J*W2J-t*F^(-1)t=L*SL+S D2+D2*S.                        (TG5b)

This is the complete second coefficient of a retained congruence. Omitting
either its direct double commutator or its exchange term breaks the identity.
The companion check uses a two-dimensional retained block, a nonzero baseline
cross block, and a noncommuting rational full matrix.

If L is bounded, ||T_g|| and ||T_g^(-1)|| are at most
exp(integral_0^|g| ||L_s|| ds). In a retained energy norm the required
quantity is instead ||B^(1/2)L_s B^(-1/2)||. Merely bounded Hilbert-space
transport does not prove that estimate or identify B with the physical
normalized coarse energy.

## TG6: The metric and finite source resolvent must travel with the form

Let M=-partial_z S=J*J as in SP6. For z-dependent T,

    -partial_z(T*ST)=T*MT-(partial_z T)*ST-T*S(partial_z T).   (TG6)

The extra terms vanish as quadratic forms on a transported on-shell vector.
They do not vanish for arbitrary off-shell vectors. Thus TG5a preserves
the spectral equation but does not authorize freezing the graph metric.

The compiled helper `TheoryCurrentBridges.schur_metric_pairing_on_shell`
only rearranges the given algebraic expression as

    T*MT-Tz*ST-T*STz = T*MT-(Tz*ST+T*STz).

Despite its retained historical name, it proves neither differentiability,
M=-partial_z S, nor cancellation on an on-shell vector. Those are the
separate analytic hypotheses and argument of TG6.

For a concrete two-level rotation, c^2+s^2=1 implies

    (E c^2+F s^2-z)(E s^2+F c^2-z)-(cs(F-E))^2
        =(E-z)(F-z).                                    (TG6b)

Indeed subtracting the right side factors as
(c^2+s^2-1)[EF(c^2+s^2+1)-z(E+F)]. This is exactly the polynomial
numerator statement proved by
`TheoryCurrentBridges.rotated_two_level_schur_numerator`. Dividing by
E s^2+F c^2-z to obtain a Schur function additionally requires this fast
denominator to be nonzero. The polynomial theorem alone does not assert
that inverse, a gap, or a transformed metric.

For a finite source unitary U, define A=J*Ui_P and D=i_Q*Ui_P. Where the
inverses exist, the Schur complement after conjugating H-z by U obeys

    S_new(z)^(-1)=A*S(z)^(-1)A+D*F(z)^(-1)D.                (TG6a)

This follows from (H-z)^(-1)=J S^(-1)J*+i_QF^(-1)i_Q*. Below the fast
spectrum the second term is regular; the first transports spectral
singularities through the actual source overlap. Frame invertibility,
analytic/energy control, and physical source residues remain separate
requirements. The exact finite identity alone is not an infinite-volume
spectral-measure identification.

See [source currents and spectral totality](source-currents-and-spectral-totality.md)
for the actual-source derivative, ground/current hypotheses, and totality
conditions. Source decay must hold on an unbounded sequence of late times
(or for all sufficiently late times), with the SAME positive exponential
rate for a total family. A finite-time fit or unrelated source-dependent
rates does not establish a spectral gap. Norms must belong to the transported
physical source/metric identification used in TG6.

## TG7: Scalar square-source parity eliminates formal odd Schur jets

This statement concerns the actual four-face SU(2) square and its complete
scalar outer-trace source; it does not concern arbitrary coarse matrix or
mixed-parity observable spaces. Sources are the preserved
[`square source`](../../runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/source.md)
and
[`finite-g source domain`](../../runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/finite_g_source_domain.md).

In the chord chart U_i=sqrt(1-g^2|X_i|^2/4)I+ig X_i.sigma/2,

    a_g=4/g^2[1-sqrt(1-g^2|X2|^2/4)sqrt(1-g^2|X3|^2/4)]
          +X2.X3.                                          (TG7)

Thus a_g is separately even in signed g and in Pi:X->-X. The actual
chart reflection gives H_-g=Pi H_g Pi and Omega_-g=Pi Omega_g.
Consequently the true source marginal and its monotone CDF transport are
even in g, and the actual scalar-source isometry obeys J_-g=Pi J_g.
The reference source Omega0 phi(|qt|^2) is pointwise Pi-even.

When the requisite projector derivatives exist on the common core,
P_-g=Pi P_g Pi implies [P'_-g,P_-g]=-Pi[P'_g,P_g]Pi. Kato transport with
initial value I therefore obeys U_-g=Pi U_g Pi; the same argument applies
to formal jets. Q7 has this parity already: its coefficients are quadratic
and its single derivative is odd, so Pi K Pi=-K.

After source straightening, Schur inversion respects this covariance. Since
Pi acts as I on the retained space,

    S_-g(z)=S_g(z).                                         (TG7a)

Every existing two-sided Taylor coefficient of odd order vanishes, including
the first and third. The full W1 and its odd fast force need not vanish.
Evenness by itself does NOT improve an O(g^3) estimate to O(g^4): |g|^3 is
an even counterexample. A controlled fourth-order remainder and the actual
source/common-domain jets at g=0 must still be established. The compact
finite-positive-coupling source transport does not supply uniform constants
as its lower coupling endpoint tends to zero.

## TG8: A residual certificate for the abstract Riccati fixed point

In a real normed Banach algebra let S be bounded and real-linear and put
T(X)=S(X^2-D), with ||S||<=beta,
beta>=0. Suppose X*=T(X*), ||X*||<=r, ||Y||<=r, and q_c=2 beta r<1.
The established multiplication estimate gives
||T(Y)-T(X*)||<=q_c||Y-X*||. Therefore

    ||Y-X*|| <= ||Y-T(Y)||/(1-q_c).                         (TG8)

Proof: insert T(Y) in the difference Y-X*, use the triangle inequality,
and move q_c||Y-X*|| to the left. This certifies proximity to the fixed
point from a residual without requiring the approximate Y to be a
commuting or scalar element. The ball-membership and fixed-point
hypotheses are essential.

For the existing abstract defaults in
[`SC17Riccati.lean`](../../lean/Workhouse/SC17Riccati.lean),

    beta=(108/25)sqrt(33), c(lambda)=lambda sqrt(lambda)/48,
    r=(1-sqrt(1-4 beta^2 c))/(2 beta), 0<=lambda<=3/100,

the established interval estimate is 4 beta^2 c<27/100. It follows that

    q_c=1-sqrt(1-4 beta^2 c)<3/20,
    (1-q_c)^(-1)<20/17,
    ||Y-X*|| <= (20/17)||Y-T(Y)||.                          (TG8a)

The last inequality is non-strict, including zero residual. The endpoint
parameter equals 96228 sqrt(3)/625000 and is checked exactly by squaring
positive quantities. `riccatiMap_lipschitz_on_ball` supplies the Lean
dependency for the residual proof; `default_parameter_interval` supplies
the default contraction estimate. These are abstract defect/solution
certificates. They do not prove the actual Wilson conditional-pressure
defect, its source identification, or continuation outside the stated
interval.

## Verification scope and open application

The companion script independently expands the generic six-variable
determinant polynomial, checks the extremum algebra and dimension
counterexamples, verifies the complete source-congruence identities on
rational matrices, and checks the endpoint inequalities. Tests include
negative controls for a wrong secular coefficient and an omitted exchange
term. Such controls establish neither smooth unbounded source transport nor
a uniform interacting remainder. Those remain model/domain obligations;
finite coefficient and scalar certificate results must not be promoted into
G19 continuum closure.
