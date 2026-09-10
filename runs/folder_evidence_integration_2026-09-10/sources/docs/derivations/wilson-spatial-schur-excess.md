# Spatial passage: the complete Schur excess and its scale budget

8 September 2026. Analytic continuation of G19. This note proves an exact
reduction and a quantitative remainder theorem, supplies the full second-order
Wilson and chosen-source coefficient formulas, and derives the error budget
for spatial iteration. It does **not** assert that the required uniform
interacting Wilson bounds or a continuum correlation limit have been proved.
The finite exact controls have a narrower verification scope than these
analytic statements.

## 1. Established starting point and the question advanced

The [temporal bridge](wilson-marked-shell-transport.md) constructs and matches
the actual vacuum, complete odd shell and literal sources at fixed spatial
spacing on a common small-u interval. Spatial removal requires a controlled
trajectory; it cannot extend that interval by substituting u=g_H^-4 -> infinity.

The unchanged, hash-pinned [spatial inputs](wilson-spatial-inputs/README.md)
already establish:

* full quadratic Schur memory, its induced norm, and an inverse-fast-energy
  gap comparison;
* the exact nonreducing Gaussian fast inverse on every chaos, and a uniform
  localized cubic synthesis estimate dominated by that inverse;
* the first Wilson ground Lie cubic and first chosen-chart source correction;
* uniform actual path-source coercivity over all flat holonomies, with a smooth
  redundant source repair for the changing physical Coulomb rank.

The target here is the **complete nonlinear excess relative to the quadratic
memory**. A cubic variance divided by a fast gap is insufficient: direct
quartic energy, original electric metric, Haar density, vacuum subtraction,
moving sources, baseline cross terms and fast-form variation must enter the
same expression. Sections 2-4 assemble them without assuming that the source
space reduces the Gaussian Hamiltonian. Sections 5-7 distinguish the estimates
now proved from the uniform Wilson hypotheses still needed.

The September 6 and 7 live research maps and the G19 proof graph were consulted
before this continuation. Targeted searches found the preceding components,
but no complete excess identity with the remainder and iteration bounds below.
This records the search scope, not a claim of uniqueness in all mathematics.

## 2. Exact excess about the full reference graph

Use a fixed physical Hilbert decomposition P direct_sum Q. Let h_0 and h_g be
closed self-adjoint forms on a common domain, with d_g=h_g-h_0. Both projections
preserve this domain. The following hypotheses specify all products of forms;
no boundedness of the full Hamiltonian is assumed.

Fix a real energy z. The reference restriction F_z=Q(H_0-z)Q, understood as a
form operator, satisfies F_z>=f_z>0. On a dense retained form domain X, let
J_z p=(p,-U_z p) be the reference graph lift characterized by

    (h_0-z)[J_z p,q]=0                    for every q in D(F_z^(1/2)).   (SP1)

Require J_z p to belong to the common form domain. Define S_0(z)[p] by
(h_0-z)[J_z p]. Thus, exactly,

    (h_0-z)[J_z p+q] = S_0(z)[p]+||F_z^(1/2)q||^2.

Let B>0 be a reference retained weight, X=D(B^(1/2)); a bounded inverse is
convenient and will be assumed. Suppose the following forms extend to the
indicated bounded operators:

    A_g = J_z* d_g J_z,
    V_g = F_z^(-1/2) Q d_g J_z,
    C_g = F_z^(-1/2) Q d_g Q F_z^(-1/2),

    B^(-1/2) A_g B^(-1/2) bounded,
    V_g B^(-1/2) bounded,            ||C_g|| <= theta < 1.               (SP2)

For example, V_g is defined by
d_g[q,J_z p]=<F_z^(1/2)q,V_g p>, consistently with polarization. It does not
require Q H_g J_z to be an ordinary Hilbert-space vector. The assumptions on
domains and closedness are substantive when P is infinite dimensional.

Minimize (h_g-z)[p+q'] over q'. The **exact** Schur form is

    S_g(z)-S_0(z) = A_g - V_g* (I+C_g)^(-1) V_g.                       (SP3)

Its minimizing graph lift is

    J_g,z = J_z - i_Q F_z^(-1/2)(I+C_g)^(-1)V_g,                        (SP4)

where i_Q embeds Q into the full Hilbert space. In particular,

    A_g - V_g*V_g/(1-theta) <= S_g-S_0
        <= A_g - V_g*V_g/(1+theta).                                   (SP5)

Proof. Set q'= -U_z p+q and r=F_z^(1/2)q. The complete shifted form equals

    S_0(z)[p]+A_g[p]+2 Re<r,V_g p>+<r,(I+C_g)r>.

Completing this positive square gives r=-(I+C_g)^(-1)V_g p and (SP3)-(SP4).
F_z^(-1/2) maps Q into the fast form domain, so the minimizer is admissible.
Spectral order for I+C_g proves (SP5). This also proves the identities by
forms, without interchanging an unbounded operator and a perturbation series.

For bounded matrices, write H_0=[[A_0,B_0],[B_0*,F_0]]. Then
J_z=(I,-(F_0-z)^(-1)B_0*)^T. Expanding S_g directly gives precisely (SP3).
The identity makes **no smallness assumption on B_0**. The defect is tested
on this full graph, not on the undressed retained vector (p,0).

At z=0, the induced norm is M_g=J_g,0*J_g,0 and the normalized static form is
M_g^(-1/2)S_g(0)M_g^(-1/2). On an interval where differentiation is justified,

    -d S_g(z)/dz = J_g,z* J_g,z.                                       (SP6)

For bounded blocks this follows by differentiating the fast inverse. More
generally it follows by differentiating the minimized form: variations of
its minimizing q vanish by stationarity, leaving -||J_g,z p||^2. Require
differentiability of the graph in the common form norm for this version.
Consequently retaining S_g(z) retains the norm and the entire energy-dependent
memory. Identifying S_g(0) alone with a coarse Hamiltonian loses (SP6).

## 3. The complete second-order coefficient and a uniform remainder

Use coefficients without factorials. Suppose, in the form sense of (SP2),

    d_g = g W_1 + g^2 W_2 + remainder,
    A_i=J_z*W_i J_z,           V_1=F_z^(-1/2)Q W_1 J_z.

Then the two excess coefficients are

    K_1(z)=J_z*W_1 J_z,
    K_2(z)=J_z*W_2 J_z - V_1*V_1.                                    (SP7)

In particular, the exchange uses the **full** compressed reference inverse.
The conditional vertical inverse may provide an upper bound; replacing it
by equality is contradicted by the existing 1/18 versus 1/20 example.

Here is a quantitative theorem that states exactly what uniformity costs.
For |g|<=g_0 suppose, uniformly in all desired volumes, backgrounds, regulators
and real energies z in a specified interval,

    ||B^(-1/2)(A_g-g A_1-g^2 A_2)B^(-1/2)|| <= a_3 |g|^3,
    ||(V_g-g V_1)B^(-1/2)|| <= v_2 g^2,
    ||V_1 B^(-1/2)|| <= v_1,
    ||C_g|| <= c_1 |g| <= theta < 1.                                  (SP8)

Then

    ||B^(-1/2)[S_g-S_0-g K_1-g^2 K_2]B^(-1/2)|| <= C_3 |g|^3,

    C_3 = a_3 + [2 v_1 v_2 + g_0 v_2^2 + c_1 v_1^2]/(1-theta).        (SP9)

Proof. Put T=(I+C_g)^(-1), X=V_g B^(-1/2), Y=g V_1 B^(-1/2).
The resolvent identity gives ||T||<=1/(1-theta) and
||T-I||<=c_1|g|/(1-theta). Expand

    X*TX-Y*Y = (X-Y)*T Y + Y*T(X-Y)
               +(X-Y)*T(X-Y)+Y*(T-I)Y.

The four terms have bounds 2v_1v_2|g|^3, v_2^2g^4 and
c_1v_1^2|g|^3, divided by 1-theta. Add the first line of (SP8).
This proves (SP9), including g=0 by its removable extension.

For example a_3=v_1=v_2=c_1=1, g_0=theta=1/4 give C_3=16/3.
These are illustrative sufficient constants, not computed Wilson constants.
There is no hidden factor equal to the number of blocks. Conversely, locality
of individual vertices does not by itself establish (SP8): extensive vacuum
terms, high retained energies and slow variables are still present there.

The same hypothesis bounds the entire fast form:
Q(H_g-z)Q>=(1-theta)F_z. Equation (SP4) also gives

    ||(J_g,z-J_z)B^(-1/2)||
       <= (|g|v_1+g^2 v_2)/[sqrt(f_z)(1-theta)].

This is a weighted graph comparison, not yet a summable source error along
a logarithmic trajectory. Retained-source and metric matching through the
required orders remain necessary.

The first-order force is graph-dressed. In block notation, if
W_1=[[a_1,b_1],[b_1*,f_1]], it is

    Q W_1 J_z = b_1* - f_1(F_0-z)^(-1)B_0*.                           (SP10)

The f_1 term is already first order when B_0!=0. Squaring (SP10), together
with J_z*W_2J_z, supplies the baseline/fast-variation cross terms omitted by
the expression a_2-b_1(F_0-z)^(-1)b_1*. The exact matrix controls include
noncommuting fast blocks and a negative control for this omission.

## 4. What W_1 and W_2 mean for the actual Wilson operator

First work on the finite, unique-flat-orbit, nondegenerate complexes of the
pinned finite-cell theorem. Let g=u^(-1/4). Its normalization is

    H_K(u)=-(1/2)sum_e Delta_e + 2u sum_f w_f v_rho(U_f),
    v_rho(U)=dim(rho)-Re Tr rho(U).

After the exact tree quotient, original-link tangent whitening, rescaling
y=g x and flattening the actual Haar density, write

    g^2 H_K(g^-4)=H_0+g H_1+g^2 H_2+O(g^3)                            (SP11)

as a local differential-operator jet on smooth vectors with cutoff. A
uniform operator remainder on the entire physical space is not implied by
this jet. Positive regulators or conditional fast fibers must be specified
separately on a torus with harmonic directions.

Here is a complete constructive coefficient prescription; it needs no
choice of independent plaquettes. In each signed face word let Z_1,...,Z_l
be its linear anti-Hermitian represented coordinates, counting every
occurrence, including reverse/repeated edges. Set

    T_f,n = sum_(k_1+...+k_l=n) Z_1^k_1 ... Z_l^k_l/(k_1!...k_l!).

The magnetic contributions are exactly

    (H_0)_mag=-2 sum_f w_f Re Tr T_f,2,
    (H_1)_mag=-2 sum_f w_f Re Tr T_f,3,
    (H_2)_mag=-2 sum_f w_f Re Tr T_f,4.                                 (SP12)

These follow by multiplying the actual exponential words before taking the
trace. They include all BCH and character terms. If
log U_f=g F_1+g^2 F_2+g^3 F_3+..., the same quartic coefficient is

    (H_2)_mag,f = w_f [b_rho |F_2|^2+2 b_rho<F_1,F_3>
                            -(1/12) Re Tr(d rho(F_1)^4)].              (SP13)

Indeed odd powers of one anti-Hermitian logarithm have purely imaginary
trace, and -Re Tr(d rho(X)d rho(Y))=b_rho<X,Y>. Keeping just |F_2|^2
does not give the full quartic coefficient when F_1!=0.

Let D_e(g)=D_e,0+g D_e,1+g^2 D_e,2+... denote each rescaled original-edge
derivative after the same quotient and half-density transformation. More
precisely, for a reduced cometric represented by real vector fields X_e and
coordinate density j, set

    D_e(g)=g j^(1/2) X_e j^(-1/2)

after dilation. The exact electric form is (1/2)sum_e ||D_e(g)psi||^2.
This definition is valid even if an individual reduced X_e is not
divergence-free; formal adjoints below use the flattened Lebesgue measure.
Thus its full second jet is

    (H_0)_el=(1/2)sum D_0*D_0,
    (H_1)_el=(1/2)sum (D_0*D_1+D_1*D_0),
    (H_2)_el=(1/2)sum (D_0*D_2+D_2*D_0+D_1*D_1).                      (SP14)

In particular the D_1*D_1 term is retained. Haar flattening occurs inside
D_e; adding an independent Haar correction afterwards would double count
it. The original-edge cometric, rather than independent face Laplacians,
is essential. Equations (SP12) and (SP14) specify the complete local H_2.

As an actual Haar/metric check, SU(2) radial class functions have electric
operator -(1/2)(partial_r^2+cot(r/2)partial_r). Multiplication by
sin(r/2)/(r/2), the square root of the Haar density relative to Euclidean
radial measure, turns it into
-(1/2)(partial_r^2+2/r partial_r)-1/8. The rescaled electric second-order
scalar is therefore -g^2/8. This is a combined metric/density calculation;
it must be retained before the true vacuum energy is subtracted.

Let e(g)=e_0+g e_1+g^2 e_2+... be the normalized true ground energy on a
fixed complex admitting the existing localized ground expansion. With
Omega_0 normalized and R_0 the reduced inverse of H_0-e_0,

    e_1=<Omega_0,H_1 Omega_0>=0,
    psi_1=-R_0 H_1 Omega_0,
    e_2=<Omega_0,H_2 Omega_0>-<H_1 Omega_0,R_0 H_1 Omega_0>,
    psi_2=-R_0[(H_1-e_1)psi_1+(H_2-e_2)Omega_0]
                                      -(1/2)||psi_1||^2 Omega_0.       (SP15)

The order-g equation and normalization give psi_1; projecting the order-g^2
equation onto Omega_0 and its orthogonal complement proves the other two
formulas. The first equality e_1=0 uses the established odd Lie-cubic
ground forcing. It does not imply that K_1 vanishes on the entire retained
source space. A torus with a zero-frequency joint Gaussian does not meet
the ground hypotheses of (SP15).

On the stated fixed, nondegenerate, unique-flat-orbit complexes these are
actual second-order asymptotic coefficients. H_1 and H_2 are polynomial
differential jets, so their forcing and the two correctors lie in a finite
Hermite span; the positive oscillator frequencies make R_0 bounded there.
Multiply Omega_0+g psi_1+g^2 psi_2 by a fixed invariant cutoff in the original
coordinates. Taylor's formula in the exact scaled operator gives a residual
O(g^3) in L2: its polynomial factors have bounded Gaussian moments, and
cutoff derivatives occur at |x| of order 1/g and have exponentially small
Gaussian norm. The order-zero, one and two equations cancel by (SP15).
The existing harmonic convergence separates the unique physical ground
from the rest by a fixed positive scaled gap. Spectral projection of this
quasimode therefore gives e(g)=e_0+g^2 e_2+O(g^3) and the displayed normalized
ground expansion with O(g^3) vector error in the cutoff/rescaled
identification, after choosing its phase. Every constant here depends on
the entire fixed complex. R_0 is the full ground-orthogonal inverse, distinct
from the literal-source fast inverse in (SP7).

Finally suppose an actual source-straightening unitary is supplied, with
U(g)=exp(g K_1^src+g^2 K_2^src+O(g^3)), K_i^src skew-adjoint, mapping the
reference retained algebra to the chosen interacting one. On a common
invariant core where these jets exist, expanding
U(g)*(H(g)-e(g))U(g) gives the W_i used in (SP7):

    W_1=H_1-e_1 I+[H_0,K_1^src],
    W_2=H_2-e_2 I+[H_1,K_1^src]+[H_0,K_2^src]
                            +(1/2)[[H_0,K_1^src],K_1^src].            (SP16)

The reference form for Section 2 is H_0-e_0 I in this application; the
constant e_0 has no effect on the displayed commutators.

Consequently (SP7), with (SP12)-(SP16), assembles the **complete second-order
coefficient in any such specified chart**. It is a coefficient formula in
terms of actual jets, not an evaluation of the interacting infinite-volume
running coupling. Uniform source-straightening and (SP8) must be proved;
neither follows from the existence of the finite-cell Taylor coefficients.

## 5. Second-order literal-source normalization and harmonic control

The moving source can also be treated directly, without assuming a global
smooth physical Coulomb projection. On a fixed finite submersive chart write

    Psi_g=Psi_0(1+g p_1+g^2 p_2+...),
    r_1=2 p_1,                 r_2=2 p_2+p_1^2,
    y_g(x)=y_0(x)+g Y_1(x)+g^2 Y_2(x)+....

For the actual fundamental SU(N) path average, the chosen polar-log chart
has an explicit Y_2. At a flat reference, right-trivialize every path by
its common coarse holonomy and expand the actual weighted average as

    M_g=I+g A+g^2 B_m+g^3 C_m+O(g^4),             A*=-A.

Each coefficient is the weighted sum of the ordered-word coefficients in
(SP12); thus this is a local recipe in the original path data. Write
skew(X)=(X-X*)/2 and Pi_su(X)=X-Tr(X)I/N on anti-Hermitian matrices.
For the locally determinant-normalized unitary polar factor Q_g,

    g^(-1) log Q_g = A+g Y_1+g^2 Y_2+O(g^3),
    Y_1=Pi_su(skew(B_m)),
    Y_2=Pi_su(skew(C_m)-(1/4){A,B_m+B_m*}+(1/3)A^3).                 (SP17a)

Here {X,Y}=XY+YX. To prove the formula, expand
M_g*M_g=I+g^2 D_2+g^3 D_3+..., where
D_2=B_m+B_m*-A^2 and D_3=C_m+C_m*-A B_m+B_m*A.
Multiply M_g by I-g^2 D_2/2-g^3 D_3/2, then use
log(I+g A+g^2 Q_2+g^3 Q_3)=g A+g^2(Q_2-A^2/2)
+g^3[Q_3-(A Q_2+Q_2 A)/2+A^3/3]. The trace subtraction implements the
local SU(N) determinant correction. This proves (SP17a) with all matrix
orders retained. It is a chosen chart of the actual observation, with the
algebra-scope limitation stated below; it does not replace the raw average
by a group element in the full history measure.

Use real ground states. Let mu_0 be the true Gaussian marginal of y_0, and
E_0[.|y] its conditional expectation. Differentiation against a compactly
supported smooth test function yields the density coefficients

    mu_1 = mu_0 E_0[r_1|y] - partial_a(mu_0 E_0[Y_1^a|y]),

    mu_2 = mu_0 E_0[r_2|y]
           -partial_a(mu_0 E_0[Y_2^a+r_1 Y_1^a|y])
           +(1/2)partial_a partial_b(mu_0 E_0[Y_1^a Y_1^b|y]).           (SP17)

Proof. Expand phi(y_g) to order two, multiply by
Psi_g^2/Psi_0^2=1+g r_1+g^2 r_2, condition on y_0, and integrate each
derivative by parts. This proves the formula distributionally; a density
expansion with a uniform norm requires additional regularity. Ground
normalization gives E r_1=E r_2=0, so both corrections have zero total mass
when the boundary terms vanish. The mixed r_1 Y_1 term and the second
derivative term cannot be recovered from the tangent source alone.

For equivalent marginal densities the exact chosen-source isometry is

    J_g^lit f(x)=Psi_g(x) [mu_0/mu_g]^(1/2)(y_g(x)) f(y_g(x)).          (SP18)

Changing variables by pushforward proves ||J_g^lit f||=||f||_L2(mu_0).
It uses the quantum ground marginal, not Haar or a classical Gibbs marginal.
Equation (SP17) determines its normalization through second order. It does
not make its derivatives bounded on all L2 functions: coordinate shifts
already differentiate arbitrary f. Source comparisons therefore need
specified energy/domain norms or complete controlled windows.

The September 7 source theorem provides a smooth redundant tangent
projection and a volume-independent submersion radius. Its physical
Coulomb projection has a norm-one jump at central SU(2) holonomy, so it
cannot be differentiated to produce K_i^src there. Use the original
endpoint-covariant observation and its exact Gauss action. A chosen
submersive chart is sufficient for its stated observables; it is not
automatically the entire matrix-observation algebra, which can see extra
directions at higher order. That full algebra/source comparison remains
an explicit Wilson obligation in (SP16)-(SP18).

There is a decisive actual quartic harmonic check. For SU(2), put
T_a=-i sigma_a/2 and take the face commutator

    U_f=exp(g x T_1)exp(g y T_2)exp(-g x T_1)exp(-g y T_2).

Its linear curl F_1 is zero, yet

    v_f=4 sin^2(gx/2)sin^2(gy/2),
    2 g^(-2)v_f=(g^2/2)x^2 y^2+O(g^4).                                (SP19)

Direct 2-by-2 multiplication proves the first identity; Taylor expansion
or (SP12) proves the second. Thus the harmonic slow directions have real
interacting quartic energy. They cannot be deleted by letting a joint
Gaussian regulator vanish. This check is compatible with the uniform
flat-background fast bound; it tests the retained dynamics.

There is also a genuine uniform **local** magnetic remainder. If each
represented |Z_j|_op<=R, word length <=ell, and |g|<=g_0, the multinomial
series gives

    ||product exp(g Z_j)-sum_(n=0)^4 g^n T_f,n||
       <= exp(g_0 ell R) |g|^5 (ell R)^5/5!.

After multiplication by 2/g^2 and trace, the per-face magnetic error is at
most 2 w_f dim(rho) exp(g_0 ell R)(ell R)^5 |g|^3/5!. This constant is
independent of volume and background unitary transports. Summing over faces
gives an extensive bound. To obtain the relative **vacuum-subtracted graph**
bound in (SP8), connected cancellation and interacting localization still
have to remove that volume loss. No global quantum estimate is inferred
from this local Taylor estimate.

## 6. Iterating energies and observable amplitudes in the physical clock

At scale j assume the hypotheses of the pinned closed-form Schur theorem
hold for the actual vacuum-subtracted physical Hamiltonian, with full fast
floor f_j. Let L_j be its normalized complete Schur form, including M_j.
Suppose the actual coarse comparison, after putting both theories in the
same physical energy units, proves

    gap(L_j) >= alpha_j Delta_j,             0<alpha_j<=1.

Then the next complete fine gap satisfies

    Delta_(j+1)^(-1) <= alpha_j^(-1) Delta_j^(-1)+f_j^(-1).            (SP20)

Set A_0=1 and A_J=product_(j<J) alpha_j. Multiplying (SP20) by A_(j+1)
and telescoping proves the exact error-weighted budget

    Delta_J >= A_J/[Delta_0^(-1)+sum_(j<J) A_(j+1)/f_j].                (SP21)

If alpha_j=1-epsilon_j, 0<=epsilon_j<=epsilon_*<1 and
sum epsilon_j<infinity, then

    A_infinity >= exp[-sum epsilon_j/(1-epsilon_*)] > 0.

This follows by integrating 1/(1-x) on [0,epsilon_j]. In particular, for
f_j>=c/a_j and a_j=a_0 b^(-j), b>1,

    inf_J Delta_J >=
      exp[-sum epsilon_j/(1-epsilon_*)]
       /[Delta_0^(-1)+(a_0/c)/(1-b^(-1))] > 0.                        (SP22)

A running clock factor belongs inside alpha_j before this estimate. If
alpha_j can exceed one, (SP21) still holds for positive alpha_j, but the
last simplification needs corresponding upper and lower product bounds.

For a complete fine window [0,E_j], E_j<f_j, the established graph-source
theorem has lower frame bound 1-(E_j/f_j)^2. If its comparison with the
actual, normalized, compatible retained-source map has operator error
delta_j, the actual lower bound is

    b_j=[sqrt(1-(E_j/f_j)^2)-delta_j]^2,                               (SP23)

provided the bracket is positive. Apply the triangle inequality to the
adjoints of the two synthesis maps to prove this. Complete frame maps
compose with lower bound product b_j. With E_j/f_j bounded below one,
summability of sum (E_j/f_j)^2+sum delta_j implies a strictly positive
product, after checking the finitely many initial steps. Restrictions to
coarse energy windows must be included in the comparison error: they are
not automatically onto the fine window.

An onto frame alone does not keep the overlap of **each specified observable**.
For the chosen observable, assume the established carrier identifications
are isometries and its normalized projected vectors have successive errors
eta_j. The elementary telescoping bound is

    ||projected O_J Omega_J|| >= ||projected O_0 Omega_0||-sum_(j<J)eta_j.
                                                                         (SP24)

Thus sum eta_j below the initial amplitude gives a positive uniform spectral
weight, the square of the remaining amplitude. This requires actual source
matching, not only (SP23). If physical carrier energies additionally converge
to M in (0,infinity) and the renormalized positive spectral measures converge
vaguely, the existing atom-passage theorem preserves this nonzero weight at
M. None of these correlation or energy convergence premises is supplied by
a fast-mode floor alone.

## 7. Why the complete second-order subtraction matters

For the concrete model of logarithmic running g_j^2=kappa/(j+j_0), j_0>0,
a generic relative error of order g_j^2 has a divergent available budget.
This statement concerns what the bound guarantees, not a proof that actual
errors must have that size. It cannot establish the positive product in
(SP22). In contrast,

    sum_(j>=0) g_j^3 <= kappa^(3/2)[j_0^(-3/2)+2 j_0^(-1/2)] < infinity,
                                                                         (SP25)

by the decreasing-function integral bound. An O(g^3) relative remainder
would therefore meet the ultraviolet summability requirement; any
O(g^4) improvement would also suffice. No evenness of the full retained
operator is assumed. This illustrative running law is a hypothesis, not
a beta-function derivation.

Equations (SP7)-(SP17) say exactly what must be retained or matched through
second order before invoking (SP9) for such a trajectory. Adding arbitrary
counterterms is not a proof of identification with the actual coarse Wilson
operator. One must match the full generated form, clock, vacuum, sources and
memory, or prove that its additional operators satisfy the required errors.

There is a further norm requirement: converting (SP9) into a relative gap
loss epsilon_j requires comparison of B with the **actual normalized coarse
energy on the vacuum-orthogonal space**, and compatible vacuum matching.
Choosing B=I, or coarse energy plus I, does not give an O(g^3) relative gap
error uniformly when that gap is small. Similarly a bound on S_g over a real
z interval alone does not bound its derivative; metric matching needs the
graph formula or appropriate differentiated/holomorphic remainder control.

The present advance is the complete coefficient assembly, its exact
nonperturbative remainder reduction, the second-order source-law formula,
and the accumulated gap/source budget. The next decisive Wilson estimate is
(SP8) in the redundant compact-source formulation, with harmonic retained
dynamics and high retained energies controlled. The existing localized
cubic estimate bounds a selected part of V_1; it does not yet bound the full
graph force (SP10), A_g's connected remainder or C_g. Establishing these and
actual coarse matching would make (SP21)-(SP24) applicable. Constructing a
nontrivial continuum correlation limit with the field-theory axioms remains
necessary even after those spectral inequalities are available.

## Reproduction scope

The subsequent [selected-inverse derivation](wilson-selected-inverse-wall.md)
tests the whole-fast-space Gaussian implementation of SP8 after finite-rank
retention and refutes that implementation by the compact SU(2) spectrum.
SP8 remains a valid conditional theorem. The continuation supplies a weaker
selected-resolvent alternative W5 and identifies W6 as the exact unproved
interacting Wilson estimate. A compatible compact reference is another
possible route; the finite-rank Gaussian counterargument does not decide it.

The native `wilson_spatial` suite checks noncommuting full Schur identities,
the complete second jet, a missing-baseline negative control, induced metric,
unitary source jets, the actual SU(2) quartic harmonic word, normalized moving
source moments, and exact scale budgets. The validation record pins this
proof, the input copies and the program. Finite controls do not formalize
the closed-form domains, all-volume hypotheses or continuum existence.
