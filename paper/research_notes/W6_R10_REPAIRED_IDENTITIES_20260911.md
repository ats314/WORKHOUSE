# W6 R10 repaired identities and conditional H4 reduction

11 September 2026. Pinned analytic result source, extracted from the reviewed
[derivation](../../docs/derivations/w6-source-energy-jets-r10.md).
Source SHA-256: 7cb2ad710a35e1ddf049b814ebd7e2ad9a3b7717d6cb8893b136149d1617ecf5.

The arguments below establish positive-g identities and stated conditional
implications. They do not establish H0-H3 or complete R10. The submitted
closure and its defects are preserved in the [repair run](../../runs/r10_proof_repair_2026-09-11/README.md).

## 1. Setup and scope

Use the fixed twelve-edge compact square, M = SU(2)^4, at positive coupling g.
Let H_g=(g^2/2)T+g^-2 V, L_g=H_g-e_g, q_g=H_g+gamma I, with the
normalized positive ground Omega_g, 0 <= e_g <= E and physical gap gamma > 0
as in R8a. Write chi_g=partial_g Omega_g and sigma_g=chi_g/Omega_g.
The source coordinate is w=tr(U_2 U_3)/2, a(w)=1-w^2,
Gamma(w,w)=2a, dmu_g=Omega_g^2 dU, and dnu_g=rho_g(w)dw.
The conditional projection Pi_g Phi=E_mu_g[Phi|w] is defined on the
fixed space of measurable functions when differentiating in g. Set
U_g psi=psi/Omega_g and P_g=U_g^-1 Pi_g U_g.
Parameter derivatives below mean partial_g; derivatives in w are written d/dw.

The complete generator is the established R9 expression

    A=[P_g',P_g]+|nu_g><Omega_g|-|Omega_g><nu_g|,
    nu_g=P_g chi_g=m_g(w)Omega_g,  m_g=Pi_g sigma_g.

Here nu_g denotes the vector only in this formula; dnu_g denotes the marginal.
Finite positive-g identities below are not uniform estimates as g tends to zero.

## 2. Correct conditional differentiation (C1)

On regular fibers w in (-1,1), put X=grad(w)/Gamma(w,w), so X(w)=1,
and B_g=div_mu_g X. For smooth Phi, the exact derivative is

    d/dw E_mu_g[Phi|w] = E_mu_g[X(Phi)|w] + Cov_mu_g(Phi,B_g|w).  (C1)

Cov(Phi,B)=E[Phi B]-E[Phi]E[B]; B is real. The formula extends in the
weak sense whenever the terms are locally integrable. It makes no assertion
at the critical endpoint fibers without an additional limiting argument.

Proof. Apply SF7d to X and Phi X, whose w components are 1 and Phi:

    E[B_g|w]=rho_g'/rho_g,
    E[X(Phi)+Phi B_g|w]=rho_g^-1 (rho_g E[Phi|w])'.

Subtract E[Phi|w] times the first equation. This gives C1.
The covariance term measures the changing conditional ground measure and fiber
geometry. It was omitted in the submitted H0 and H3 arguments.
For eta=E[tilde_sigma_g Phi|w], C1 gives all three terms:

    eta'=E[X(tilde_sigma_g)Phi|w]+E[tilde_sigma_g X(Phi)|w]
          +Cov(tilde_sigma_g Phi,B_g|w).                         (C2)

A compact exact counterexample to omission uses density (1+a*w*y)/4 on
[-1,1]^2, |a|<1, X=partial_w, Phi=y. Then E[Phi|w]=a*w/3,
its derivative is a/3, and E[X(Phi)|w]=0. This refutes the general
shortcut, not H0 for the actual square.

## 3. A sufficient horizontal-score estimate for H0 (C3)

Suppose, in addition to the setup, that

    ess sup_w g^2(1-w^2) Var_mu_g(B_g|w) <= C_B                 (C3a)

uniformly in 0<g<g_*, with a common smooth form core whose conditional expectations belong to
the source form domain. The estimate below extends the projection to the full
form domain.
Then H0 holds with kappa_P=2+2 C_B/gamma:

    b_g[Pi_g Phi] <= (2+2 C_B/gamma) q_g[Omega_g Phi].           (C3)

Proof. In C1, use |x+y|^2 <= 2|x|^2+2|y|^2 and conditional
Cauchy-Schwarz. Since |X(Phi)|^2 <= Gamma(Phi,Phi)/(2a),

    b_g[Pi_g Phi] <= 2 L_g[Omega_g Phi]
                   +2 integral g^2 a Var(Phi|w) Var(B_g|w) dnu_g
                 <= 2 L_g[Omega_g Phi]+2 C_B ||Omega_g Phi||^2.

Use q_g >= gamma I and L_g <= q_g. Boundedness on the core and L2
continuity of conditional expectation yield a unique extension in the form
norm, with the same inequality. This is a sufficient condition, not a
necessity or an established estimate on B_g. Proving C3a for the actual model
would discharge H0; other proofs of H0 remain possible.

## 4. H4 follows from H0 and the established ground jet (C4)

Assume H0 with a g-independent kappa_P. The first ground jet R8a says
q_g[chi_g] <= D_1^2 g^-2. At fixed positive g, sigma_g=chi_g/Omega_g
belongs to the transformed form domain. Substitute Phi=sigma_g into H0:

    b_g[m_g] <= kappa_P q_g[chi_g] <= kappa_P D_1^2 g^-2.        (C4)

Thus H4 follows with kappa_3=kappa_P D_1^2. No semiclassical marginal-profile
ansatz or tail truncation is needed. H0 itself remains open.

Also, L_g >= 0 implies q_g >= (e_g+gamma) I. Conditional expectation is
an L2(mu_g) orthogonal projection, so

    q_g[P_g chi_g] = (e_g+gamma)||P_g chi_g||^2+b_g[m_g]
                   <= (1+kappa_P) q_g[chi_g].                  (C4a)

The rank-one energy bound therefore yields

    || |nu_g><Omega_g|-|Omega_g><nu_g| ||_(q_g->q_g)
       <= 2 sqrt(E+gamma) sqrt(1+kappa_P) D_1/(gamma g).         (C4b)

In SF9 one may now assume H0-H3 and set kappa_3=kappa_P D_1^2.
This reduces the sufficient order-zero checklist from five estimates to four.
It does not establish those four estimates or parameter orders one and two.

## 5. Complete projection-jet recurrence (C5)

On a common smooth core at fixed positive g, U_g'=-sigma_g U_g and
(U_g^-1)'=U_g^-1 sigma_g. For any differentiable operator family F_g,

    partial_g(U_g^-1 F_g U_g)=U_g^-1(F_g'+[sigma_g,F_g])U_g.

Consequently, define F_0=Pi_g and recursively

    F_(n+1)=partial_g F_n+[sigma_g,F_n],
    P_g^(n)=U_g^-1 F_n U_g.                                   (C5)

This is an exact differentiation identity, not an energy-norm bound. In particular,

    F_2 = Pi_g''+[sigma_g',Pi_g]+2[sigma_g,Pi_g']
            +[sigma_g,[sigma_g,Pi_g]].                         (C5a)

In expanded form this is

    F_2=(sigma_g^2+sigma_g')Pi_g-2 sigma_g Pi_g sigma_g
        +Pi_g(sigma_g^2-sigma_g')+Pi_g''
        +2 sigma_g Pi_g'-2 Pi_g' sigma_g.

The last two terms were missing in the submission. Pi_g varies because mu_g
varies; it cannot be differentiated as a fixed conditional measure. The
recurrence supplies the higher terms without dropping mixed derivatives.
The complete Kato derivatives retain

    A_P'=[P_g'',P_g],
    A_P''=[P_g''',P_g]+[P_g'',P_g'].                            (C5b)

These identities follow by the product rule and [P_g',P_g']=0.
Every term, including [P_g'',P_g'], needs the required energy estimate.

For a finite check take Omega=(cos t,sin t), 0<t<pi/2,
Pi=[[cos(t)^2,sin(t)^2],[cos(t)^2,sin(t)^2]], and U=diag(1/Omega).
Then P=Omega Omega^T. At t=pi/4, the true P'' minus the submitted
formula is [[0,-4],[-4,0]]. The corrected formula equals P'' exactly.
This verifies a counterexample and a finite realization, not the continuum
operator-domain assumptions; the general identity follows from the product rule.

## Verification scope

The six exact finite/scalar checks have their stated limited scope. These full
analytic statements have no whole Lean or machine certification (T3).
