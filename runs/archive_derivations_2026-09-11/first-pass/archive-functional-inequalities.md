# Smooth defects, Lyapunov patching and concentration from the historical archive

11 September 2026. Reconstructed analytic arguments, with explicit hypotheses.
The original arguments are the author's archived Appendix E and Parts 7–8;
verbatim copies and hashes are retained in
[the source package](../../runs/archive_derivations_2026-09-11/README.md).
F2 gives a shorter proof of the archived gradient bound; F6 extends its profile
calculus; F7 makes the uniform small-set constant explicit. F14–F15 are exact
controls of the later synthesis, not claims made by the original appendices.
These are implications under stated assumptions, not a continuum construction.

## F1. Trace defect, faithfulness and the vacuum set

Let rho:G->U(n) be a smooth unitary representation of a compact Lie group.
Set z(g)=1-Re Tr rho(g)/n. Then z is smooth and conjugation invariant,
0<=z<=2, and z(g)=0 iff rho(g)=I. Indeed its eigenvalues are exp(i theta_j),
and equality in sum cos(theta_j)<=n forces each eigenvalue to be 1.
Thus the zero set is ker rho; it is {1} when rho is faithful. This supplies
the exact missing hypothesis for interpreting the defect as distance from a
unique group identity. Source: Appendix E, Lemma E.1.

## F2. Global gradient domination without a quotient singularity

On a complete Riemannian manifold, let z>=0 be C² with Hess z<=H g for H>0.
At x with grad z nonzero, follow the unit geodesic opposite grad z for
t=|grad z(x)|/H. Taylor's integral remainder gives

    0 <= z(gamma(t)) <= z(x)-t|grad z(x)|+H t²/2,
    |grad z(x)|² <= 2H z(x).                         (F2)

The zero-gradient case is immediate. A smooth nonnegative function on a
compact manifold meets this hypothesis by choosing a positive H above its
Hessian norm. No smooth extension of |grad z|²/z at its zeros is required,
and faithfulness is unnecessary for this inequality. This reproves the
gradient-domination conclusion of Appendix E.3 under weaker zero-set assumptions.

## F3. Plaquette lifts preserve link derivatives

Give G a bi-invariant metric and G^E its product metric. A plaquette word
has r distinct links, each appearing once with exponent +1 or -1. Holding
the other links fixed, its map in any one link is g->a g^(+/-1) b, an
isometry. Therefore for z_p=z(U_p),

    |grad z_p|² = r |grad_G z(U_p)|² <= r Cg z_p,
    Delta z_p = r (Delta_G z)(U_p),
    |Delta z_p| <= r Cd.                              (F3)

Here |grad_G z|²<=Cg z and |Delta_G z|<=Cd. The distinct-link assumption
excludes degenerate tiny periodic cells with repeated link variables.
For ordinary square plaquettes r=4. This is the exact locality calculation
behind Appendix E.5–E.6 and Part 7.2.

## F4. Aggregate defect comparisons

For P>0 defects 0<=z_p<=B, D=sum z_p and V=sum z_p² satisfy

    D²/P <= V <= B D <= B² P.                         (F4)

The first inequality is Cauchy–Schwarz, the second follows term by term
from z_p²<=B z_p. For trace defects B=2. In particular D<=D0 bounds the
exponential weight exp(k V) by exp(k B D0), independently of P.
Source: Appendix E.2.

## F5. Exact drift identity and the squared-profile budget

Let L=Delta-grad S.grad be the symmetric diffusion for exp(-S) times
Riemannian volume, Gamma(f,g)=<grad f,grad g>, V=sum z_p² and W=exp(k V).
Assume each link belongs to at most nu plaquettes and F3 holds. Set
P_S=sum_p z_p Gamma(S,z_p). The chain rule gives exactly

    LW/W = k[2 sum z_p Delta z_p + 2 sum Gamma(z_p)-2 P_S]
           + k² Gamma(V).
    |Delta V| <= 2r(Cd+Cg) D = Cv D,
    Gamma(V) <= 4 nu r Cg B² D = Cgamma D.            (F5)

For the last inequality apply |sum_(p containing e) v_p|²<=nu sum |v_p|²
to v_p=2z_p grad_e z_p, sum over e, then use z_p³<=B² z_p.
Thus LW/W <= (k Cv+k² Cgamma)D-2k P_S. With r=4,B=2 this is
Cv=8(Cd+Cg), Cgamma=64nu Cg, the archive's Part 7.35–7.36 constants.
No sign estimate on P_S follows from this identity alone.

## F6. General profiles with vanishing derivative at zero

Under F3 and the overlap bound, let Phi be C² on [0,B], Phi'(0)=0,
and sup|Phi''|<=M. Then |Phi'(z)|<=Mz. For V_Phi=sum Phi(z_p),

    |Delta V_Phi| <= r M(Cd+Cg) D,
    Gamma(V_Phi) <= nu r M² Cg B² D.                  (F6)

Apply Delta Phi(z)=Phi'(z)Delta z+Phi''(z)Gamma(z), F3, and the same
linkwise Cauchy–Schwarz argument as F5. The exponential chain rule then
leaves only sum Phi'(z_p)Gamma(S,z_p) as the action-dependent term.
This extends the archive's squared-profile mechanism without claiming its
coercivity for a new Phi or a new action.

## F7. Linear pairing implies a genuinely uniform small-set drift

Assume the exact hypotheses of F5, k>0, and a pointwise bound
P_S>=a D-b with b>=0 independent of P. Suppose
c=2a-Cv-k Cgamma>0. Choose D0>2b/c and set

    lambda=k(c D0-2b)>0,
    b_core=(lambda+2k b) exp(k B D0),
    K={D<=D0}.
    LW <= -lambda W+b_core 1_K.                      (F7)

Outside K, F5 gives LW/W<=-lambda. Inside K, LW/W<=2k b and F4 bounds
W<=exp(k B D0). This proves the displayed global inequality. Uniform
constants in the premises give uniform lambda and b_core. Replacing b by
bP or D0 by a volume-scale threshold does not preserve this conclusion
without a separate estimate. This is a conditional application interface;
the required Wilson pairing inequality is not proved here.

## F8. Lyapunov energy conversion as a completed square

Let L be the symmetric diffusion above on a compact manifold without
boundary, or on a common core with all boundary terms zero. For smooth h>0
and real f, integration by parts and the diffusion product rule give

    integral (-Lh/h) f² dmu
      = integral [2(f/h) Gamma(f,h)-(f/h)² Gamma(h)] dmu
      = integral Gamma(f) dmu
        - integral |grad f-(f/h)grad h|² dmu
      <= integral Gamma(f) dmu.                     (F8)

Extend to a form domain only when the core approximation and integrability
are supplied. Source: Part 7, Lemma 7.45.

## F9. Local-to-global Poincare patching

Assume F8, mu(K)>0, W>=1, LW<=-lambda W+b_core 1_K with lambda>0,
and the local estimate integral_K(f-mu_K f)² dmu<=kappa_K E(f,f).
Set g=f-mu_K f. From 1<=-LW/(lambda W)+(b_core/lambda)1_K,
multiply by g² and apply F8 and the local estimate. Since
Var_mu f<=integral g² dmu and E(g,g)=E(f,f),

    Var_mu f <= (1+b_core kappa_K)/lambda E(f,f).     (F9)

Uniformity follows from uniform lambda>0, b_core and kappa_K. This proves
a Poincare inequality, not a log-Sobolev inequality. The proof also works
on gauge-invariant test functions if that class has the required core
and constant-subtraction properties. Source: Part 7, Theorem 7.46.

## F10. Averaging gives a volume-scale gradient bound

Under the distinct-link geometry of F3, let |grad_G z|<=C1 and
Bbar=P^-1 sum z_p. Applying overlap Cauchy–Schwarz at each link gives

    |grad Bbar|² <= nu/P² sum_p |grad z_p|²
                  <= r nu C1²/P.                    (F10)

For r=4,nu=6 this is 24 C1²/P, the same constant as Part 8.11 on a
four-dimensional periodic lattice. This proof uses incidence counts
directly, so no separate edge-to-plaquette ratio is needed.

## F11. Herbst concentration and the mean threshold

Assume Ent_mu(f²)<=2/rho E(f,f), rho>0, and a bounded smooth H with
|grad H|<=L_H. For psi(t)=log E exp(tH), applying LSI to exp(tH/2)
gives t psi'(t)-psi(t)<=t² L_H²/(2rho). Integrating the derivative
of psi(t)/t from zero yields

    log E exp[t(H-EH)] <= t² L_H²/(2rho).
    mu(H>EH+d) <= exp[-rho d²/(2 L_H²)], d>0.         (F11)

The second line follows by Chernoff minimization t=rho d/L_H²; if L_H=0
the centered variable is zero on each connected component covered by the
LSI. For F10 and a uniform epsilon-E Bbar>=d>0,
mu(Bbar>epsilon)<=exp[-rho d² P/(2r nu C1²)]. Both the LSI and the
mean-below-threshold estimate are hypotheses, as Part 8.13 and 8.19 state.

## F12. Covariance localization with an explicit error budget

For bounded real F,G and 0<p=mu(K)<1, write conditional means f0,f1,g0,g1
on K,Kc. Expanding E(FG)-EF EG gives

    Cov_mu(F,G)=p Cov_K(F,G)+(1-p)Cov_Kc(F,G)
                  +p(1-p)(f0-f1)(g0-g1).            (F12)

Since |Cov_nu(F,G)|<=4||F||inf||G||inf and conditional mean differences
are at most twice the corresponding norm,

    |Cov_mu(F,G)-p Cov_K(F,G)|
       <=8||F||inf||G||inf mu(Kc).

Thus a conditional exponential covariance estimate plus F11 gives a
quantitative unconditioned bound. The conditional estimate must hold on
this same K. Source: Part 8, Lemma 8.1 and Corollary 8.2.

## F13. Absorbing a volume tail into a distance exponent

Assume |Cov_K(F,G)|<=C exp(-m R), ||F||inf<=MF, ||G||inf<=MG,
mu(Kc)<=A exp(-cP), and the compared supports obey R<=d0 P, d0>0.
Then F12 implies

    |Cov_mu(F,G)| <= (C+8A MF MG) exp[-min(m,c/d0)R]. (F13)

This is a direct inequality: exp(-cP)<=exp(-cR/d0). It records the
geometry and bounded-observable conditions needed to turn the archived
error ledger into a uniform distance estimate. It does not prove those
conditional covariance or probability inputs for Wilson fields.

## F14. Averaged smallness does not imply plaquettewise smallness

On a sufficiently large periodic four-dimensional SU(2) lattice, take one
link equal to -I and all other links I. Exactly its six incident square
plaquettes have z=2; all others have z=0. Thus D=12, max z=2 and
Bbar=12/P tends to zero with volume. The configuration is gauge-invariantly
distinguished by its plaquette traces. Consequently no fixed positive
average threshold enforces an arbitrarily small maximum defect. This
does not refute methods designed to accommodate a sparse bad set.

## F15. Center configurations refute the proposed Laplacian identity

At every all-center SU(2) link configuration, each variation of a plaquette
trace is plus or minus Tr X=0 for X in su(2). Hence grad z_p=0 for every p
and sum_(p~q) Gamma(z_p,z_q)=0. For the nonconstant defect field in F14
on a connected plaquette adjacency graph,

    sum_p z_p (Delta_graph z)_p
       =-sum_{unordered edges {p,q}}(z_p-z_q)² < 0.  (F15)

This disproves the later synthesis's equality between these expressions
under the ordinary graph Laplacian convention. A boundary edge contributes
-4. These configurations are also stationary for the Wilson gradient
flow, as the existing PBH center check proves. A new compensating flow
would require a specified equation and a new proof of the desired identity.

## Application boundary

F1–F6 and F8–F13 are analytic lemmas with explicit hypotheses; F7 is the
conditional Wilson-facing drift interface; F14–F15 are exact negative
controls. Background Ricci curvature and the Gibbs sampling generator are
not identified here with the physical transfer Hamiltonian. The existing
[PBH Wilson test](yangmills-pbh-wilson-test.md) gives the signed-curvature
and physical-ground-weight boundaries. Global LSI, uniform mean typicality,
the correct conditional covariance estimate and the physical-time bridge
remain separate inputs. No G17, G19, G20 or G23 closure is asserted.
