# W6: repaired source-energy identities and the remaining R10 estimates

11 September 2026. This is the reviewed replacement for the R10 closure claim
in PR 150. The [submitted source and checks](../../runs/r10_proof_repair_2026-09-11/README.md)
are preserved with their original hashes. The failed steps do not disprove R10.

The established inputs are the [ground jets R8a](w6-ground-jets-and-transport-budget.md),
the [score-frame identities SF1-SF8 and conditional SF9](w6-source-generator-score-frame.md),
and the [antipodal magnetic geometry](w6-antipodal-magnetic-geometry.md).
This note corrects conditional differentiation and projection jets, proves
that H0 implies H4 using R8a, and retains the unresolved actual-model estimates.

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

## 6. Scaling defects and unresolved estimates (C6)

The submitted diffusion gap c_trans gives the physical gap g^2 c_trans/2.
With forcing norm 4 g^-3(C_V g^2), its inverse estimate is

    8 C_V/(c_trans g^3), not 8 C_V/(c_trans g).                  (C6a)

A uniform physical fiber gap would repair this exponent arithmetic, but must
be proved together with the correct conditional operator equation and uniform
forcing. The full-space spectral gap and the seven local magnetic Hessian
directions alone do not prove these fiber statements.

Writing v=E[V|w], the submitted H2 inequality would require a uniform C_1
in 4 sqrt(32 kappa_0) g^-4 sqrt(v) <= C_1 g^-2(1+g^-2 v).
At v=g^2 the ratio is

    8 sqrt(2 kappa_0)/g -> infinity.                           (C6b)

Thus bounded V and the stated variance bound do not justify that scalar
step. Actual covariance cancellation, stronger conditional moments, or another
estimate of the full SF7e identity is needed, including its drift and flux.
Smoothness for each positive g alone gives no uniform small-g derivative bound.

The preserved statement IDs retain these unresolved targets:

- H0_ENERGY_CONTRACTION: uniform energy boundedness of Pi_g, including the
  original proposed kappa_P=1. C1 corrects the argument; C3 is only sufficient.
- H1_FIBERWISE_SCORE_VARIANCE: sup_w Var(sigma_g|w) <= kappa_0 g^-2.
- VACUUM_CROSS_DERIVATIVES: the energy bounds for partial_g^r A_nu, r=0,1,2.
  C4b handles r=0 only conditionally on H0; derivatives of m_g remain needed.
- KATO_DERIVATIVES: the energy bounds for partial_g^r[P_g',P_g], r=0,1,2.
  C5 fixes the identity, but supplies no uniform bounds for its terms.

Global q_g ground-jet bounds do not automatically imply essential-supremum
conditional moments of sigma_g, sigma_g^2 or their derivatives, nor the required
multiplication-operator estimates. H3 also retains the covariance in C2.
R10 and the H0-H4 package remain open. The prior conditional R10-to-R11/R12
transport budget remains valid; it has not been instantiated by this attempt.
The interacting-grid uniformity and continuum limits remain separate successors.

## 7. Verification and provenance

The repaired invariant suite checks exact finite conditional derivatives,
product-rule terms, and the two scalar scaling defects. Its outputs describe
only those computations. The analytic C1-C5 results remain T3 for complete
machine coverage; no full-model R10 or Lean proof is claimed.
The [repair run](../../runs/r10_proof_repair_2026-09-11/README.md) retains
original source bytes, the independent review, and validation provenance.
