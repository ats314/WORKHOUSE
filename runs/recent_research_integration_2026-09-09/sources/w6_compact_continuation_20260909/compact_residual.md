# Complete compact-source residual and selected inverse comparison

9 September 2026. This is an actual finite-coupling, all-source theorem for
the twelve-edge, four-face square. The reference coupling is a positive
number s. Both the reference and compared operators are the compact Wilson
operators. The source is the complete algebra of the literal outer trace.
The comparison below retains the actual vacuum, actual source projection,
nonreducing reference graph, and interacting fast inverse.

## 1. The family and the precise choice of source transport

Let M=SU(2)^4, restricted to simultaneous-conjugation-invariant states, and
write

    H_t = (t^2/2) T_op + t^(-2) V,
    T[u,v] = sum_(e,c) <E_(e,c)u,E_(e,c)v>,
    0 <= V <= 32,
    L_t = H_t-e_t,       Omega_t = the normalized positive ground.

The edge fields and potential are exactly those in
`../w6_square_block_20260909/finite_g_quantum_floor.md`. In particular,
T is uniformly elliptic on the fixed compact manifold. Set

    Vform = H^1(M)_phys,       ||u||_1^2 = ||u||^2+T[u].

Fix a closed interval I=[a,b] of positive couplings within the interval
where the proved physical quantum gap is at least gamma=2. More generally
the same proof works with the positive minimum physical gap gamma_I on
any compact positive interval. All untransported forms have domain Vform.

Let w=Tr(U2 U3)/2. Haar conditional expectation in w is denoted E_w, and

    h_t(w)=E_w[Omega_t^2],
    P_t f = Omega_t h_t^(-1) E_w[Omega_t f].                (C1)

Thus ran(P_t) is the complete actual source space Omega_t f(w), and
P_t Omega_t=Omega_t. The direct-product holonomy change of variables and
conjugation averaging prove that E_w is bounded on Vform. The positive
ground, its parameter derivatives, and h_t are smooth. On I they have
bounded smooth norms, and h_t has a positive minimum. Formula (C1)
therefore proves that t -> P_t is norm C-infinity on both L2 and Vform.

Here is a full source-compatible transport with the same norm regularity.
Fix s in I, and solve

    U'_t=[P'_t,P_t] U_t,                 U_s=1.

This is the usual projection transport, but its Vform properties follow
directly from its bounded-operator ODE: U_t and U_t^(-1) preserve Vform,
are norm C-infinity there, and U_t P_s U_t^*=P_t. Define

    chi_t=U_t^* Omega_t,
    D_t=|chi'_t><chi_t|-|chi_t><chi'_t|,
    S'_t=D_t S_t,                        S_s=1,
    R_t=U_t S_t.                                               (C2)

The ground and these operators can all be chosen real. Hence
<chi_t,chi'_t>=0. Both chi_t and chi'_t lie in ran(P_s), so D_t is a
bounded skew-adjoint finite-rank operator supported on P_s. Its ODE gives
S_t chi_s=chi_t and S_t=1 on Q_s. Consequently

    R_s=1,   R_t P_s R_t^*=P_t,   R_t Omega_s=Omega_t,
    R_t Vform=Vform,   t -> R_t is norm C-infinity on Vform. (C3)

This specifies the full Q-to-Q action as well as the source action. It is
an alternative compact source chart to the CDF-adjusted chart in
`finite_g_source_domain.md`. It transports exactly the same complete
source ranges and true vacuum. It does not assert that an individual
function of the CDF coordinate is transported identically in the two
charts, or that its first coefficient equals the earlier Gaussian K1.
That distinction is necessary: a varying diffeomorphism pullback has an
unbounded first-order generator, and mere preservation of H1 by the CDF
transport does not prove norm differentiability H1 -> H1.

If an explicit source injection at s is fixed, define its injection at t
by R_t I_s. This is an exact isometry onto Omega_t L2(nu_t), maps the
retained vacuum to Omega_t, and covers every actual retained form-energy
source. No finite-energy cutoff is imposed.

Put P=P_s, Q=1-P, Omega=Omega_s, and define the transported form

    l_t[u,v] = <R_t u,L_t R_t v>.                            (C4)

It has common domain Vform, annihilates Omega, and has gap at least gamma
on Omega-perp. Equations (C1)-(C4) establish its norm C-infinity dependence
as a form Vform -> Vform*. No residual regularity is being assumed.

## 2. Actual derivative bounds and their dependence on positive coupling

The derivatives of the untransported form are explicit:

    L^(0): (t^2/2)T+t^(-2)V-e_t,
    L^(1): t T-2t^(-3)V-e'_t,
    L^(2): T+6t^(-4)V-e''_t,
    L^(3): -24t^(-5)V-e'''_t.                              (C5)

Write E_j=sup_I |e_t^(j)| and

    alpha_0=b^2/2+32a^(-2)+E_0,
    alpha_1=b+64a^(-3)+E_1,
    alpha_2=1+192a^(-4)+E_2,
    alpha_3=768a^(-5)+E_3.

These bound the respective Vform form norms. The constant trial function
gives e_t<=16/t^2, so E_0<=16/a^2. Hellmann-Feynman and nonnegativity of
the electric and magnetic energies give |e'_t|<=2e_t/t<=32/t^3.
The remaining E_j are finite derivatives of the actual isolated simple
eigenvalue, obtained by differentiating its compact elliptic equation.
For example, with the inverse on the physical vacuum complement,

    Omega'_t = (4/t^3)(L_t|Omega_t-perp)^(-1)
                         (V-<V>_Omega_t) Omega_t.           (C6)

This formula fixes the actual quantum ground derivative; it is not a
classical Gibbs replacement. Repeated differentiation supplies E_2,E_3
and higher smooth ground norms. The fixed positive interval and elliptic
regularity make all of them finite.

For transparency, even the transport constants can be obtained directly
from (C1), rather than imposed as an extra analytic hypothesis. If m(f)
is any multiplication-operator bound on Vform, for example

    m(f)=sqrt(2)(||f||_infinity+||grad_E f||_infinity),

and C_E=||E_w||_(Vform->Vform), then

    ||P_t^(j)||_1 <= C_E sum_(r+k+v=j) j!/(r!k!v!)
                  m(Omega_t^(r)) m((h_t^(-1))^(k))
                                      m(Omega_t^(v)).        (C7)

Derivatives of [P'_t,P_t] follow by the product rule. Its bounded ODE,
followed by the explicitly finite-rank ODE in (C2), bounds every
N_j=sup_I ||R_t^(j)||_(Vform->Vform). In particular, these are constructed
finite constants for the actual operator, not an assumed residual bound.

The conditional-score expression gives a sharper interpretation in L2.
With sigma_t=partial_t log Omega_t, disintegration of Haar in w gives

    ||P'_t||_(L2->L2)=||[P'_t,P_t]||_(L2->L2)
        = ess sup_w sqrt(Var_(Omega_t^2)(sigma_t | w)).      (C8)

Indeed the normalized fiber vector v_t=Omega_t/sqrt(h_t) satisfies
v'_t=(sigma_t-E[sigma_t|w])v_t, and P_t(w)=|v_t><v_t|. The H1 estimate
still involves spatial derivatives of these fiber data, as made explicit
by (C7); the L2 identity alone is not substituted for it.

There is also a conditional-moment H1 refinement that avoids division by
a very small marginal lower bound. Use product coordinates (xi,W), where
xi consists of three independent group variables and W=U2 U3 is the
complete outer group variable. Their product Sobolev norm is equivalent
to ||.||_1, with fixed geometric constants. On physical functions,
conditional expectation in W agrees with the literal trace source
projection because the resulting coarse function is a class function.
Set v_t=Omega_t/sqrt(h_t(W)), a normalized vector in each xi fiber.
For a parameter-dependent normalized fiber vector v, define

    C_0 = sup_W ||v'||_(L2(xi)),
    X_0 = sup_W (sum_X ||Xv||_(L2(xi))^2)^(1/2),
    Y_0 = sup_W (sum_Y ||Yv||_(L2(xi))^2)^(1/2),
    X_1 = sup_W (sum_X ||Xv'||_(L2(xi))^2)^(1/2),
    Y_1 = sup_W (sum_Y ||Yv'||_(L2(xi))^2)^(1/2).            (C8a)

Here X runs through fixed fiber group derivatives and Y through coarse
group derivatives, and sup can be replaced by essential supremum.
The rank-one formulas P=|v><v| and P'=|v'><v|+|v><v'| give, in the
product Sobolev norm, the explicit nonoptimal bounds

    ||P||_(H1->H1) <= 2+X_0+2Y_0,
    ||P'||_(H1->H1)
                    <= C_0(4+X_0+2Y_0)+X_1+2Y_1.         (C8b)

To verify these, apply a fiber rank-one map K_ab u=a<b,u>.
Its L2 derivative-free bound is ||a|| ||b||; a fiber derivative
differentiates only a; a coarse derivative gives the three terms
(Ya)<b,u>+a<Yb,u>+a<b,Yu>. Integrating their pointwise Cauchy-Schwarz
bounds proves (C8b). Conversion to the electric Sobolev norm only
multiplies these estimates by the fixed equivalence constants.

All five quantities in (C8a) have exact actual-quantum conditional-moment
formulas. Write sigma=partial_t log Omega_t, eta_X=X log Omega_t,
eta_Y=Y log Omega_t, r=sigma-E[sigma|W], and c_Y=eta_Y-E[eta_Y|W]. Then

    v'=r v,                 Xv=eta_X v,             Yv=c_Y v,
    Xv'=(Xsigma+r eta_X)v,
    Yv'={Ysigma-E[Ysigma|W]-2Cov(sigma,eta_Y|W)+r c_Y}v.    (C8c)

The covariance term follows by differentiating the normalized fiber
density: Y E[sigma|W]=E[Ysigma|W]+2Cov(sigma,eta_Y|W).
Taking squared conditional expectations of the brackets in (C8c)
therefore computes (C8a), including all spatial derivatives. Higher
parameter derivatives of P have the same rank-one structure with
partial_t^j v. These identities apply unchanged after any positive,
source-algebra-preserving dilation with its unitary density factor.

Thus an averaged ground-score estimate is meaningful progress, but the
uniform H1 transport needed here asks for the displayed fiber essential
suprema and their spatial conditional moments. This is the precise
stronger uniformity that cannot be inferred from an unconditional
ground derivative norm. At every fixed positive interval the quantities
are finite by smoothness and positivity, so no additional hypothesis is
needed for (C15)-(C19).

Leibniz differentiation of (C4) gives the following definite bounds:

    B_1=alpha_1 N_0^2+2alpha_0 N_0 N_1,
    B_2=alpha_2 N_0^2+4alpha_1 N_0 N_1
                                  +2alpha_0(N_1^2+N_0 N_2),
    B_3=alpha_3 N_0^2+6alpha_2 N_0 N_1
       +6alpha_1(N_1^2+N_0 N_2)
                                  +2alpha_0(3N_1 N_2+N_0 N_3).

At the positive reference s, the actual quantum gap gives, on Omega-perp,

    ||u||_1^2 <= D_s l_s[u],
    D_s=1/gamma+(2/s^2)(1+e_s/gamma).

For gamma=2 one may use D_s<=1/2+2/s^2+16/s^4. For a fixed real spectral
interval Z=[z_-,z_+] with z_+<gamma, put

    c_Z=max(1,gamma/(gamma-z_+)),
    beta_Z=max(1,1-z_-/gamma),
    M_j=c_Z D_s B_j,          j=1,2,3.                     (C9)

On Omega-perp let k_s=l_s-z<.,.>. Then, uniformly for z in Z,

    |l_t^(j)[u,v]| <= M_j sqrt(k_s[u] k_s[v]).             (C10)

This follows from the displayed Sobolev bound and k_s>=l_s/c_Z.
The fact that every derivative annihilates Omega follows from (C3).
Thus (C10) controls all the relevant source and fast vectors.

The bounds explicitly depend on a>0, the actual conditional ground
derivatives, and the fixed square. No estimate uniform as a goes to zero
or as the spatial volume grows is contained in (C7)-(C10).

## 3. The nonreducing graph and the actual retained energy

For p in ran(P) intersect Vform with p perpendicular to Omega, set

    b_s[p]=l_s[p].

This is the actual reference retained energy. If p=Omega_s f(w), then

    b_s[p]=s^2 integral (1-w^2)|f'(w)|^2 dnu_s(w),
    dnu_s=h_s(w)(2/pi)sqrt(1-w^2)dw.                        (C11)

It is neither the earlier Gaussian radial energy nor a truncated source
norm. Its form closure covers every actual finite-energy retained source.

Let a_s=k_s restricted to Q intersect Vform, with inverse G_s in the
form-dual sense. Define the actual baseline coupling functional

    B_s^* p(q)=k_s[q,p],
    J_s(z)p=p-G_s B_s^*p.                                  (C12)

No claim that P reduces L_s is needed. Cauchy-Schwarz for k_s and the
positive fast floor prove that B_s^*p is a bounded fast-form functional.
The minimizer in (C12) belongs to Q intersect Vform, and

    k_s[q,J_s p]=0 for q in Q intersect Vform,
    k_s[J_s p]=k_s[p]-a_s[G_s B_s^*p]
                         <=k_s[p]<=beta_Z b_s[p].          (C13)

This is the required complete graph synthesis estimate on the entire
retained form domain. It retains the baseline off-diagonal coupling.

## 4. Complete residual and the interacting inverse

Put Delta=t-s, d_t=l_t-l_s, and epsilon=M_1|Delta|. Assume epsilon<1.
Integration of (C10) gives |d_t[u,v]|<=epsilon sqrt(k_s[u]k_s[v]).
Consequently the actual transported fast form

    a_t=(l_t-z)|Q

satisfies a_t>=(1-epsilon)a_s. Let G_t=a_t^(-1), including its continuous
extension from fast-form duals. The COMPLETE finite-coupling graph
residual and its leading derivative are

    r_t p(q)=d_t[q,J_s p],
    t_s p(q)=l'_s[q,J_s p].                                (C14)

These definitions include the electric form, magnetic potential, true
vacuum subtraction, and both derivatives of the complete source unitary.
They are not just a cubic coefficient or a magnetic score. Equations
(C10), (C13), and the a_t lower bound prove

    ||t_s p||_(a_s*) <= M_1 sqrt(beta_Z b_s[p]),
    <r_t p,G_t r_t p>
             <= beta_Z epsilon^2/(1-epsilon) b_s[p].       (C15)

This proves the full finite-g residual dual norm for all actual retained
form-energy sources on the fixed positive interval. It is a direct
interacting inverse estimate; no local derivative seminorm of r_t occurs.

For the selected inverse term set u_s=G_s t_s p and u_t=G_t t_s p. Then

    a_s[u_s] <= beta_Z M_1^2 b_s[p],
    a_s[u_t] <= beta_Z M_1^2/(1-epsilon)^2 b_s[p].

The form resolvent identity now gives the compact-reference W6 estimate

    <t_s p,(G_t-G_s)t_s p> = -d_t[u_s,u_t],

    |d_t[u_s,u_t]|
       <= beta_Z M_1^3 |Delta|/(1-epsilon) b_s[p].          (C16)

Both inverse images lie in the common actual form domain by construction.
In particular, the previously uncontrolled interacting inverse image has
an energy bound here; it has not been replaced by a Gaussian inverse.

One can also isolate the complete selected residual itself:

    rho_t p(q)=d_t[q,G_s t_s p],
    <rho_t p,G_t rho_t p>
       <= beta_Z M_1^2 epsilon^2/(1-epsilon) b_s[p].         (C17)

This is the dual-resolvent version of the selected signed pairing. It
uses the full finite difference d_t and its complete transported operator.

## 5. The resulting cubic Schur remainder

Let S_t(z) be the Schur form of l_t-z on P, and A_j=J_s^* l_s^(j) J_s.
The actual graph square completion is valid on the common form domain:

    S_t-S_s = J_s^* d_t J_s-r_t^*G_t r_t.                  (C18)

Taylor's integral remainder and (C10) give

    ||r_t p-Delta t_s p||_(a_s*)
                   <= (M_2 Delta^2/2) sqrt(beta_Z b_s[p]),

    |(J_s^*d_t J_s-Delta A_1-Delta^2 A_2/2)[p]|
                   <= beta_Z M_3 |Delta|^3 b_s[p]/6.

Expanding the two factors of r_t in (C18), and applying (C16), proves

    |(S_t-S_s-Delta A_1
                 -Delta^2[A_2/2-t_s^*G_s t_s])[p]|
      <= beta_Z |Delta|^3 b_s[p]
         { M_3/6 + [M_1 M_2+|Delta|M_2^2/4+M_1^3]
                                                    /(1-epsilon) }. (C19)

The estimate is uniform over b_s[p]=1, all source energies, and z in Z.
It extends from smooth source functions by the proved form-domain bounds.
Polarization gives the associated bounded retained energy-space form.
Unlike the Hilbert-norm version of W5, no unsupported assertion that a
second-order force is L2-bounded by one source derivative is needed:
the whole proof uses the appropriate fast-form duals.

At z=0 the same proof also compares the actual retained norms along this
transport. Writing b_t for the untransported actual source energy at t,

    (1-epsilon)b_s[p] <= b_t[R_t p]
                                      <=(1+epsilon)b_s[p]. (C20)

Thus a successive positive-reference step has a definite source-energy
comparison as well as a Schur remainder. On a chain of steps the factors
1+epsilon multiply. If epsilon_j is of order 1/j, these accumulated
factors can grow polynomially; that growth must be retained when summing
all errors in a single reference norm.

## 6. What is discharged, and the next quantitative dependency

For a positive compact reference on the actual fixed square, the source
and inverse-domain conditions, complete residual estimate, selected
interacting inverse comparison, and cubic Schur remainder are now proved.
The nonreducing baseline source is included explicitly in (C12).

To use a chain of positive references tending to zero, the next estimate
is quantitative control of the actual M_j(s), especially the conditional
ground score and its spatial derivatives in (C7)-(C8). Bounds of the form
M_j(s)<=C s^(-j) would make a relative step |Delta|/s the natural small
parameter in (C19); those scaling bounds are not proved by compactness.
Spatial volume, changing lattice geometry, and comparison of different
coarse energy norms require their own uniform estimates. The theorem
above makes no identification of this compact reference with the original
Gaussian-normalized W6 at zero coupling.

`check_compact_residual.py` independently checks the nonreducing graph,
full residual, signed resolvent identity, square completion, and displayed
bounds in an exact rational finite-dimensional control. The all-energy
and parameter-regularity claims are the analytic proofs above, not an
extrapolation from those finite controls.
