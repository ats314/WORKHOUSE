# Corpus Map and Clean Document Set

This document is a cleaned, unified extraction of the technically usable material captured in the chat-derived corpus. It includes:

- A corpus map and dependency graph
- Canonical definitions and objects
- Core pipeline and interfaces
- Proved results
- Conditional results and external assumptions

The content below is preserved as originally extracted, with stable IDs and sources.

---

# Corpus Map and Dependency Graph

## Accepted item index

### Canonical definitions
- `definition-lattice-geometry`
- `definition-lattice-configuration-space`
- `definition-lattice-gauge-group`
- `definition-lattice-gauge-action`
- `definition-plaquette-holonomy`
- `definition-wilson-action`
- `definition-lattice-yang-mills-measure`
- `definition-dirichlet-form`
- `definition-capacity-dirichlet-form`
- `definition-carre-du-champ`
- `definition-iterated-carre-du-champ`
- `definition-curvature-dimension-condition`
- `definition-poincare-inequality`
- `definition-log-sobolev-inequality`
- `definition-spectral-gap`
- `definition-discrete-cochains`
- `definition-discrete-coboundary-operators`
- `definition-discrete-hodge-decomposition`
- `definition-charge-conjugation-involution`
- `definition-continuum-reducible-connection`

### Core interfaces
- `interface-effective-action-flow-equation`
- `interface-pbh-hessian-flow-equation`
- `interface-os-reconstruction-bridge`

### Proved results retained from corpus
- `theorem-poincare-from-curvature-dimension`
- `theorem-variance-decay-from-curvature-dimension`
- `theorem-spectral-gap-equivalent-poincare`
- `theorem-correlation-decay-from-spectral-gap`
- `lemma-wilson-quadratic-expansion`
- `lemma-wilson-hessian-sum-of-squares`
- `lemma-gauge-directions-kernel-wilson-hessian`
- `lemma-ricci-positive-compact-product-group`
- `theorem-riccati-lower-bound-from-positive-source`
- `lemma-riccati-constant-source-fixed-points`
- `theorem-charge-conjugation-sector-decomposition`
- `lemma-charge-conjugation-trivial-on-su-two-gauge-invariants`
- `lemma-commutator-map-infinite-rank`
- `theorem-scalar-uniform-convexity-implies-spectral-gap`
- `theorem-prokhorov`
- `proposition-tails-imply-exponential-square-moment`
- `lemma-closed-balls-not-compact-in-infinite-dimensional-hilbert`
- `lemma-uniform-norm-exponential-moment-not-imply-tightness`

### Conditional results and explicit hypotheses
- `hypothesis-log-forest-uv-control`
- `hypothesis-anomaly-source-positivity`
- `hypothesis-continuum-polarity-of-reducibles`
- `hypothesis-lsi-lifting-stability`
- `hypothesis-spectral-gap-to-mass-gap`
- `hypothesis-local-gap-dominates-topology`
- `hypothesis-transfer-matrix-gap-strong-coupling`
- `hypothesis-rg-flow-stability-package`
- `conditional-theorem-gap-persistence-under-rg-flow`
- `conditional-theorem-trace-monotone-under-pbh`

## Dependency graph (acyclic layering)

### Functional-inequality layer
- `theorem-poincare-from-curvature-dimension`  
  depends on `definition-carre-du-champ`, `definition-iterated-carre-du-champ`, `definition-curvature-dimension-condition`, `definition-dirichlet-form`.
- `theorem-variance-decay-from-curvature-dimension`  
  depends on `definition-curvature-dimension-condition`, `definition-carre-du-champ`.
- `theorem-spectral-gap-equivalent-poincare`  
  depends on `definition-poincare-inequality`, `definition-spectral-gap`, `definition-dirichlet-form`.
- `theorem-correlation-decay-from-spectral-gap`  
  depends on `definition-spectral-gap`, `definition-dirichlet-form`.

### Lattice small-field geometry layer
- `lemma-wilson-quadratic-expansion`  
  depends on `definition-wilson-action`, `definition-discrete-coboundary-operators`.
- `lemma-wilson-hessian-sum-of-squares`  
  depends on `lemma-wilson-quadratic-expansion`.
- `lemma-gauge-directions-kernel-wilson-hessian`  
  depends on `definition-lattice-gauge-action`, `definition-discrete-coboundary-operators`, `lemma-wilson-hessian-sum-of-squares`.
- `lemma-ricci-positive-compact-product-group`  
  depends on `definition-lattice-configuration-space`.

### ODE comparison layer
- `theorem-riccati-lower-bound-from-positive-source`  
  depends on `definition-spectral-gap` (only as interpretation; the ODE statement is standalone).
- `conditional-theorem-gap-persistence-under-rg-flow`  
  depends on `hypothesis-rg-flow-stability-package`, `interface-pbh-hessian-flow-equation`, `theorem-riccati-lower-bound-from-positive-source`.

### Continuum bridge layer
- `hypothesis-lsi-lifting-stability`  
  depends on `definition-log-sobolev-inequality`, plus an (implicit) convergence interface for measures/forms.
- `hypothesis-spectral-gap-to-mass-gap`  
  depends on `interface-os-reconstruction-bridge` and a (local) spectral gap premise.

---

# Canonical Definitions and Objects

Definition: Lattice geometry for gauge theory  
ID: definition-lattice-geometry  
Statement: A lattice region consists of a finite vertex set \(\Lambda\), an oriented bond (edge) set \(B(\Lambda)\), and a plaquette set \(P(\Lambda)\) of oriented elementary faces.  
Sources: SYNTH_P01_lattice_polarity.md [lattice-setup], SYNTH_CONJ_IR_local_gap.md [setup]

---

Definition: Lattice configuration space  
ID: definition-lattice-configuration-space  
Statement: For gauge group \(G=SU(N)\), the lattice configuration space is  
\[
\mathcal C_\Lambda := G^{B(\Lambda)}=\{U=(U_b)_{b\in B(\Lambda)}: U_b\in G\}.
\]  
Sources: SYNTH_P01_lattice_polarity.md [definition-configuration-space], SYNTH_CONJ_IR_local_gap.md [setup]

---

Definition: Lattice gauge group  
ID: definition-lattice-gauge-group  
Statement: The lattice gauge group is  
\[
\mathcal G_\Lambda := G^\Lambda=\{g=(g_x)_{x\in\Lambda}: g_x\in G\}.
\]  
Sources: SYNTH_P01_lattice_polarity.md [definition-gauge-group], SYNTH_CONJ_IR_local_gap.md [setup]

---

Definition: Lattice gauge action on configurations  
ID: definition-lattice-gauge-action  
Statement: The gauge action of \(g\in\mathcal G_\Lambda\) on \(U\in\mathcal C_\Lambda\) is, for an oriented bond \(b=(x,y)\),  
\[
(g\cdot U)_{(x,y)} := g_x^{-1}\,U_{(x,y)}\,g_y .
\]  
Sources: SYNTH_P01_lattice_polarity.md [definition-gauge-action], SYNTH_CONJ_IR_local_gap.md [setup]

---

Definition: Plaquette holonomy  
ID: definition-plaquette-holonomy  
Statement: For \(p\in P(\Lambda)\) with oriented boundary \(b_1 b_2 b_3 b_4\), the plaquette holonomy is  
\[
U_p := U_{b_1}U_{b_2}U_{b_3}U_{b_4}.
\]  
Sources: SYNTH_P01_lattice_polarity.md [definition-plaquette], PROOF_04_Geometric_Mass_Derivation.md [wilson-setup]

---

Definition: Wilson action  
ID: definition-wilson-action  
Statement: The Wilson action is  
\[
S_W(U) := \frac{\beta}{N}\sum_{p\in P(\Lambda)} \mathrm{Re}\,\mathrm{Tr}(I-U_p).
\]  
Sources: SYNTH_P01_lattice_polarity.md [definition-wilson-action], PROOF_04_Geometric_Mass_Derivation.md [wilson-setup], SYNTH_P09_wilson_hessian.md [wilson-hessian-setup]

---

Definition: Lattice Yang–Mills measure  
ID: definition-lattice-yang-mills-measure  
Statement: The lattice Yang–Mills measure is the probability measure on \(\mathcal C_\Lambda\) given by  
\[
d\mu_{\beta,\Lambda}(U)=\frac{1}{Z_{\beta,\Lambda}}\,e^{-S_W(U)}\prod_{b\in B(\Lambda)} d\mathrm{Haar}(U_b).
\]  
Sources: SYNTH_P01_lattice_polarity.md [definition-lattice-measure], SYNTH_CONJ_IR_local_gap.md [setup]

---

Definition: Dirichlet form and carré du champ for a symmetric Markov generator  
ID: definition-dirichlet-form  
Statement: For a symmetric Markov generator \(L\) on \(L^2(\mu)\), the Dirichlet form is \(\mathcal E(f,f):=-\langle f,Lf\rangle_{L^2(\mu)}\) on its form domain. For diffusion-type generators, \(\mathcal E(f,f)=\int \Gamma(f)\,d\mu\), where \(\Gamma\) is the carré du champ.  
Sources: SYNTH_P05_poincare_from_curvature.md [gamma-calculus-setup], SYNTH_CONJ_D_spectral_to_mass.md [spectral-gap-poincare], SYNTH_CONJ_IR_local_gap.md [setup-dirichlet]

---

Definition: Capacity associated with a Dirichlet form  
ID: definition-capacity-dirichlet-form  
Statement: For a Dirichlet form \(\mathcal E\) on \(L^2(\mu)\), the (one-)capacity of a measurable set \(A\) is  
\[
\mathrm{Cap}(A):=\inf\Big\{\mathcal E(u,u)+\int u^2\,d\mu:\ u\in\mathcal D(\mathcal E),\ u\ge 1\ \mu\text{-a.e. on a neighborhood of }A\Big\}.
\]  
Sources: SYNTH_P01_lattice_polarity.md [capacity-definitions], SYNTH_CONJ_C_continuum_polarity.md [capacity-language]

---

Definition: Carré du champ  
ID: definition-carre-du-champ  
Statement: For a Markov generator \(L\), the carré du champ bilinear form is  
\[
\Gamma(f,g):=\frac12\big(L(fg)-fLg-gLf\big),\qquad \Gamma(f):=\Gamma(f,f).
\]  
Sources: SYNTH_P05_poincare_from_curvature.md [gamma-calculus-setup], SYNTH_P02_bakry_emery_curvature.md [definitions]

---

Definition: Iterated carré du champ  
ID: definition-iterated-carre-du-champ  
Statement: The iterated carré du champ is  
\[
\Gamma_2(f):=\frac12\big(L\Gamma(f)-2\Gamma(f,Lf)\big).
\]  
Sources: SYNTH_P05_poincare_from_curvature.md [gamma-calculus-setup], SYNTH_P02_bakry_emery_curvature.md [definitions]

---

Definition: Curvature-dimension condition  
ID: definition-curvature-dimension-condition  
Statement: The curvature-dimension condition \(CD(\rho,\infty)\) holds if for all smooth (or core) \(f\),  
\[
\Gamma_2(f)\ge \rho\,\Gamma(f).
\]  
Sources: SYNTH_P05_poincare_from_curvature.md [cd-definition], SYNTH_P02_bakry_emery_curvature.md [definitions]

---

Definition: Poincaré inequality  
ID: definition-poincare-inequality  
Statement: A probability measure \(\mu\) satisfies a Poincaré inequality with constant \(\rho>0\) if, for all \(f\) with \(\int f\,d\mu=0\),  
\[
\mathrm{Var}_\mu(f)=\int f^2\,d\mu \le \frac{1}{\rho}\int \Gamma(f)\,d\mu.
\]  
Sources: SYNTH_P05_poincare_from_curvature.md [poincare-definition], SYNTH_CONJ_D_spectral_to_mass.md [spectral-gap-poincare]

---

Definition: Log-Sobolev inequality  
ID: definition-log-sobolev-inequality  
Statement: A probability measure \(\mu\) satisfies a log-Sobolev inequality with constant \(\rho>0\) if, for all smooth \(f\),  
\[
\mathrm{Ent}_\mu(f^2):=\int f^2\log\frac{f^2}{\int f^2\,d\mu}\,d\mu \le \frac{2}{\rho}\int \Gamma(f)\,d\mu.
\]  
Sources: SYNTH_P05_poincare_from_curvature.md [lsi-definition], PROOF_01_Continuum_LSI_Loop_Groups.md [theorem-log-sobolev-context]

---

Definition: Spectral gap for a symmetric generator  
ID: definition-spectral-gap  
Statement: A symmetric Markov generator \(L\) has an \(L^2(\mu)\) spectral gap \(\lambda_1>0\) if \(-L\) has bottom nonzero spectrum at \(\lambda_1\), equivalently if the Poincaré inequality holds with constant \(\lambda_1\).  
Sources: SYNTH_CONJ_D_spectral_to_mass.md [spectral-gap-poincare], SYNTH_CONJ_IR_local_gap.md [spectral-gap]

---

Definition: Discrete cochains for linearized lattice gauge fields  
ID: definition-discrete-cochains  
Statement: Let \(\mathfrak g=\mathfrak{su}(N)\). The spaces of \(\mathfrak g\)-valued \(k\)-cochains are \(C^0:=\mathfrak g^\Lambda\), \(C^1:=\mathfrak g^{B(\Lambda)}\), \(C^2:=\mathfrak g^{P(\Lambda)}\), equipped with the \(\ell^2\) inner product \(\langle X,Y\rangle=\sum \langle X_\sigma,Y_\sigma\rangle_{\mathfrak g}\).  
Sources: SYNTH_P09_wilson_hessian.md [setup-discrete-forms], SYNTH_P04_haar_geometry_supplement.md [cochain-setup]

---

Definition: Discrete coboundary operators  
ID: definition-discrete-coboundary-operators  
Statement: The discrete coboundary operators are \(d_0:C^0\to C^1\) and \(d_1:C^1\to C^2\), with \(d_1\circ d_0=0\). Their \(\ell^2\)-adjoints are denoted \(d_0^*\) and \(d_1^*\).  
Sources: SYNTH_P09_wilson_hessian.md [setup-discrete-forms], SYNTH_P04_haar_geometry_supplement.md [cochain-setup]

---

Definition: Discrete Hodge decomposition  
ID: definition-discrete-hodge-decomposition  
Statement: With the above inner products,  
\[
C^1=\mathrm{im}(d_0)\ \oplus\ \mathrm{im}(d_1^*)\ \oplus\ \mathcal H^1,
\]
where \(\mathcal H^1:=\ker(d_1)\cap\ker(d_0^*)\) is the space of discrete harmonic \(1\)-cochains.  
Sources: SYNTH_P09_wilson_hessian.md [hodge-decomposition], SYNTH_P04_haar_geometry_supplement.md [hodge]

---

Definition: Charge conjugation involution on lattice configurations  
ID: definition-charge-conjugation-involution  
Statement: The charge conjugation map \(C\) acts on configurations by entrywise complex conjugation \(U\mapsto U^*=(U_b^*)_{b\in B(\Lambda)}\). It induces a unitary involution on \(L^2(\mu)\) by \((Cf)(U):=f(U^*)\).  
Sources: SYNTH_P08_charge_conjugation.md [setup]

---

Definition: Continuum reducible connection  
ID: definition-continuum-reducible-connection  
Statement: A connection \(A\) is reducible if its stabilizer in the gauge group is nontrivial, equivalently if there exists \(\xi\neq 0\) with \(D_A\xi=0\).  
Sources: SYNTH_CONJ_C_continuum_polarity.md [definitions-reducible]

---

# Core Pipeline and Interfaces

Interface: Effective action flow equation for a lattice smoothing map  
ID: interface-effective-action-flow-equation  
Statement: For the “effective action” \(S_t\) defined by a smoothing map \(V_t[U]\) (with Jacobian built into the definition), the evolution satisfies an identity of the form  
\[
\frac{dS_t}{dt}
= g_0^2 \sum_{x,\mu}\left\{\frac{\partial S_t}{\partial V_\mu(x)}\frac{\partial S_0^W}{\partial V_\mu(x)}
-\frac{\partial^2 S_0^W}{\partial V_\mu(x)^2}\right\}.
\]  
Sources: PROOF_02_Gradient_Flow_Stability.md [eq-eleven-flow]

---

Interface: Projected Hessian flow model (PBH/Riccati form)  
ID: interface-pbh-hessian-flow-equation  
Statement: A projected Hessian \(h_t\) along a flow is modeled by an evolution of the form  
\[
\partial_t h_t = -2h_t^2 + [h_t,K_t] + \Sigma_t,
\]
where \([h_t,K_t]\) is a commutator term (hence traceless) and \(\Sigma_t\) is a source term.  
Sources: SYNTH_P17_trace_bound.md [pbh-trace-setup], SYNTH_P14_rg_flow_stability.md [pbh-model]

---

Interface: OS reconstruction bridge from Euclidean data to a Minkowski mass gap  
ID: interface-os-reconstruction-bridge  
Statement: Under reflection positivity and related Euclidean axioms, a Euclidean field theory yields a Hilbert space and a self-adjoint Hamiltonian whose spectrum controls exponential decay of Euclidean two-point functions; a strictly positive spectral gap in the Hamiltonian corresponds to a mass gap.  
Sources: SYNTH_CONJ_D_spectral_to_mass.md [os-reconstruction]

---

Interface: Proof-stack pipeline skeleton (objects and handoff points)  
ID: interface-proof-stack-pipeline  
Statement: The corpus organizes a mass-gap pipeline through: (i) a local spectral gap/functional inequality input on lattice measures, (ii) stability/lifting to a continuum measure/Dirichlet form, and (iii) a reconstruction bridge turning Euclidean decay into a Minkowski spectral gap.  
Sources: SYNTH_CONJ_D_spectral_to_mass.md [bridge-overview], SYNTH_CONJ_IR_local_gap.md [conjecture-ir], PROOF_05_Lifting_Lemma.md [conjecture-d-lifting]

---

# Proved Results

Theorem: Curvature-dimension implies Poincaré inequality  
ID: theorem-poincare-from-curvature-dimension  
Statement: Assume \(CD(\rho,\infty)\) for some \(\rho>0\). Then \(\mu\) satisfies the Poincaré inequality with constant \(\rho\): for all \(f\) with \(\int f\,d\mu=0\),  
\[
\int f^2\,d\mu \le \frac{1}{\rho}\int \Gamma(f)\,d\mu.
\]  
Assumptions: \(CD(\rho,\infty)\) in the sense of `definition-curvature-dimension-condition`.  
Proof: The corpus proof proceeds by applying the semigroup \(P_t=e^{tL}\), using \(\frac{d}{dt}\mathrm{Var}_\mu(P_t f)=-2\int \Gamma(P_t f)\,d\mu\) and \(\frac{d}{dt}\int \Gamma(P_t f)\,d\mu=-2\int \Gamma_2(P_t f)\,d\mu\le -2\rho\int \Gamma(P_t f)\,d\mu\). Integrating yields \(\int \Gamma(P_t f)\,d\mu\le e^{-2\rho t}\int \Gamma(f)\,d\mu\), and then \(\mathrm{Var}_\mu(f)=2\int_0^\infty \int \Gamma(P_t f)\,d\mu\,dt\le \rho^{-1}\int \Gamma(f)\,d\mu\).  
Sources: SYNTH_P05_poincare_from_curvature.md [method-one-proof], SYNTH_P02_bakry_emery_curvature.md [poincare-from-cd]

---

Theorem: Curvature-dimension implies exponential variance decay  
ID: theorem-variance-decay-from-curvature-dimension  
Statement: Under \(CD(\rho,\infty)\) with \(\rho>0\), the variance along the semigroup decays as  
\[
\mathrm{Var}_\mu(P_t f)\le e^{-2\rho t}\,\mathrm{Var}_\mu(f).
\]  
Assumptions: \(CD(\rho,\infty)\) and \(\mu\)-symmetry of \(P_t\).  
Proof: Differentiate \(\mathrm{Var}_\mu(P_t f)\) to obtain \(\frac{d}{dt}\mathrm{Var}_\mu(P_t f)=-2\int \Gamma(P_t f)\,d\mu\). Combine with the \(\Gamma\)-decay bound derived from \(CD(\rho,\infty)\) to close the Grönwall estimate.  
Sources: SYNTH_P05_poincare_from_curvature.md [variance-decay], SYNTH_P02_bakry_emery_curvature.md [variance-decay]

---

Theorem: Poincaré inequality is equivalent to an \(L^2\) spectral gap  
ID: theorem-spectral-gap-equivalent-poincare  
Statement: For a symmetric Markov generator \(L\) with invariant probability \(\mu\), the following are equivalent:
- There exists \(\lambda>0\) such that for all \(f\) with \(\int f\,d\mu=0\), \(\int f^2\,d\mu \le \lambda^{-1}\mathcal E(f,f)\).
- The spectrum of \(-L\) on the orthogonal complement of constants is bounded below by \(\lambda\).  
Assumptions: Self-adjointness of \(L\) on \(L^2(\mu)\) with constants in the kernel.  
Proof: The corpus proof uses the Rayleigh–Ritz variational characterization of the first nonzero eigenvalue of \(-L\) and identifies it with the best Poincaré constant.  
Sources: SYNTH_CONJ_D_spectral_to_mass.md [spectral-gap-poincare], SYNTH_CONJ_IR_local_gap.md [spectral-gap]

---

Theorem: Spectral gap implies exponential decay of time correlations for the reversible semigroup  
ID: theorem-correlation-decay-from-spectral-gap  
Statement: Let \(P_t\) be a \(\mu\)-reversible Markov semigroup with spectral gap \(\lambda_1>0\). For \(f,g\in L^2(\mu)\) with zero mean,  
\[
\big|\langle f,P_t g\rangle_{L^2(\mu)}\big|\le e^{-\lambda_1 t}\,\|f\|_{L^2(\mu)}\,\|g\|_{L^2(\mu)}.
\]  
Assumptions: \(\mu\)-reversibility and `definition-spectral-gap`.  
Proof: Expand \(g\) in the spectral decomposition of \(-L\) and use \(P_t=e^{tL}\) to obtain \(\|P_t g\|_2\le e^{-\lambda_1 t}\|g\|_2\), then apply Cauchy–Schwarz.  
Sources: SYNTH_CONJ_D_spectral_to_mass.md [theorem-time-correlation]

---

Lemma: Quadratic expansion of Wilson action near the identity configuration  
ID: lemma-wilson-quadratic-expansion  
Statement: In a small-angle parametrization \(U_b=\exp(X_b)\) near the identity, the Wilson action has leading quadratic term  
\[
S_W(U) = \frac{\beta}{2}\sum_{p\in P(\Lambda)} \| (d_1 X)_p\|_{\mathfrak g}^2 \ +\ O(\|X\|^3),
\]
where \(d_1\) is the linearized plaquette coboundary.  
Assumptions: Small-field regime where \(U_b=\exp(X_b)\) is valid and \(X_b\) are \(\mathfrak g\)-valued.  
Proof: The corpus derivation expands each plaquette holonomy \(U_p=\exp(\theta_p)\) with \(\theta_p=(d_1X)_p+O(\|X\|^2)\), and uses \(\mathrm{Re}\,\mathrm{Tr}(I-e^{\theta})=\frac12\|\theta\|^2+O(\|\theta\|^3)\) in \(\mathfrak{su}(N)\).  
Sources: SYNTH_P09_wilson_hessian.md [wilson-action-linearization], PROOF_04_Geometric_Mass_Derivation.md [wilson-plaquette-expansion]

---

Lemma: Wilson Hessian is a sum of plaquette-square terms at the identity  
ID: lemma-wilson-hessian-sum-of-squares  
Statement: The second variation of \(S_W\) at the identity configuration satisfies  
\[
\delta^2 S_W(I)[X,X] \;=\; \beta\sum_{p\in P(\Lambda)} \|(d_1 X)_p\|_{\mathfrak g}^2,
\]
hence is nonnegative.  
Assumptions: Linearization at the identity configuration.  
Proof: Differentiate the quadratic expansion in `lemma-wilson-quadratic-expansion` to obtain the exact second variation at \(X=0\).  
Sources: PROOF_04_Geometric_Mass_Derivation.md [wilson-hessian-formula], SYNTH_P09_wilson_hessian.md [wilson-hessian-setup]

---

Lemma: Gauge directions lie in the kernel of the Wilson Hessian at the identity  
ID: lemma-gauge-directions-kernel-wilson-hessian  
Statement: If \(X=d_0\phi\) is an infinitesimal gauge direction, then \(\delta^2 S_W(I)[X,X]=0\).  
Assumptions: Linearization at identity and \(d_1\circ d_0=0\).  
Proof: Using `definition-discrete-coboundary-operators`, \(d_1(d_0\phi)=0\), and then `lemma-wilson-hessian-sum-of-squares` gives zero.  
Sources: PROOF_04_Geometric_Mass_Derivation.md [gauge-kernel], SYNTH_P09_wilson_hessian.md [gauge-kernel]

---

Lemma: Positive Ricci curvature for the compact product group configuration manifold  
ID: lemma-ricci-positive-compact-product-group  
Statement: With the product bi-invariant metric on \(G^{B(\Lambda)}\) (with \(G=SU(N)\)), the Ricci tensor satisfies \(\mathrm{Ric}_g=\kappa\,g\) for a constant \(\kappa>0\) (Einstein property of compact semisimple Lie groups and stability under finite products).  
Assumptions: Bi-invariant metric on each \(SU(N)\) factor and product metric.  
Proof: The corpus proof cites the standard Lie-group computation giving \(\mathrm{Ric}=\kappa g\) for compact semisimple \(G\), and then uses additivity of Ricci under Riemannian products.  
Sources: PROOF_04_Geometric_Mass_Derivation.md [ricci-product-group], SYNTH_P04_haar_geometry_supplement.md [ricci-supplement]

---

Lemma: Fixed points and blow-up threshold for Riccati with constant source  
ID: lemma-riccati-constant-source-fixed-points  
Statement: For the scalar Riccati ODE \(\dot\lambda=-2\lambda^2+\sigma\) with constant \(\sigma>0\), the equilibria are \(\lambda_\pm=\pm\sqrt{\sigma/2}\). Initial data \(\lambda(0)>\lambda_-\) yields global solutions; \(\lambda(0)<\lambda_-\) yields finite-time blow-down to \(-\infty\).  
Assumptions: \(\sigma>0\) constant.  
Proof: Solve explicitly by separation of variables, or equivalently analyze phase portrait of \(\dot\lambda\).  
Sources: SYNTH_P06_riccati_hessian_flow.md [constant-source-analysis]

---

Theorem: Lower bound for Riccati evolution under a strictly positive source  
ID: theorem-riccati-lower-bound-from-positive-source  
Statement: Let \(\lambda(t)\) satisfy  
\[
\dot\lambda(t) = -2\lambda(t)^2 + \sigma(t),
\]
with \(\sigma(t)\ge \sigma_{\min}>0\) for all \(t\ge 0\). If \(\lambda(0)>-\sqrt{\sigma_{\min}/2}\), then \(\lambda(t)\) exists for all \(t\ge 0\) and satisfies  
\[
\liminf_{t\to\infty}\lambda(t)\ \ge\ \sqrt{\sigma_{\min}/2}.
\]  
Assumptions: \(\sigma(t)\ge\sigma_{\min}>0\) and initial condition \(\lambda(0)>-\sqrt{\sigma_{\min}/2}\).  
Proof: Compare \(\lambda\) to the solution \(\underline\lambda\) of the constant-source ODE \(\dot{\underline\lambda}=-2\underline\lambda^2+\sigma_{\min}\) with the same initial value. The comparison principle yields \(\lambda(t)\ge \underline\lambda(t)\) while both exist, and `lemma-riccati-constant-source-fixed-points` gives global existence and a lower asymptotic bound.  
Sources: SYNTH_P06_riccati_hessian_flow.md [corrected-theorem-variable-source]

---

Theorem: Charge conjugation yields an even/odd decomposition preserved by the dynamics  
ID: theorem-charge-conjugation-sector-decomposition  
Statement: If \(\mu\) is invariant under \(U\mapsto U^*\) and the generator \(L\) commutes with the induced involution \(C\), then \(L^2(\mu)\) decomposes orthogonally as  
\[
L^2(\mu)=\mathcal H^+\oplus\mathcal H^-,
\qquad
\mathcal H^\pm:=\{f: Cf=\pm f\},
\]
and both \(\mathcal H^\pm\) are invariant under \(L\) (and \(P_t\)).  
Assumptions: Invariance of \(\mu\) under complex conjugation and commutation \(LC=CL\).  
Proof: Use that \(C\) is a unitary involution, so spectral projections \((I\pm C)/2\) give the decomposition, and commutation implies invariance.  
Sources: SYNTH_P08_charge_conjugation.md [decomposition-proof]

---

Lemma: Charge conjugation is trivial on \(SU(2)\) gauge-invariant observables  
ID: lemma-charge-conjugation-trivial-on-su-two-gauge-invariants  
Statement: For \(G=SU(2)\), complex conjugation is an inner automorphism; consequently \(f(U^*)=f(U)\) for any gauge-invariant \(f\), so the odd subspace \(\mathcal H^-\) is trivial in the gauge-invariant sector.  
Assumptions: Gauge invariance and \(G=SU(2)\).  
Proof: The corpus argument identifies \(U^*=\Omega U\Omega^{-1}\) for a fixed \(\Omega\in SU(2)\) and uses gauge invariance to conclude equality.  
Sources: SYNTH_P08_charge_conjugation.md [su-two-inner-automorphism]

---

Lemma: The commutator map has infinite rank in the Gaussian tangent model  
ID: lemma-commutator-map-infinite-rank  
Statement: Let \(\xi\in\mathfrak{su}(N)\setminus\{0\}\) and define \(T_\xi: H^s\to H^s\) by \(T_\xi(a)=[a,\xi]\) (pointwise). Then \(T_\xi\) has infinite rank (hence \(\ker T_\xi\) has infinite codimension) in Sobolev-based models with infinitely many Fourier modes.  
Assumptions: Sobolev model with infinitely many modes and \(\xi\neq 0\).  
Proof: Decompose into Fourier modes \(a=\sum_{k} a_k e^{ik\cdot x}\); for each mode, \([\,\cdot\,,\xi]\) has nontrivial image whenever \(\xi\) is noncentral (and \(\mathfrak{su}(N)\) is center-free), yielding a uniformly positive rank contribution per mode and hence infinite rank overall.  
Sources: SYNTH_P18_gaussian_polarity.md [commutator-rank-lemma]

---

Theorem: Uniform convexity implies a uniform lattice spectral gap in the scalar prototype  
ID: theorem-scalar-uniform-convexity-implies-spectral-gap  
Statement: For a finite lattice scalar field \(\phi\in\mathbb R^\Lambda\) with action  
\[
S(\phi)=\sum_{x}\Big(\frac{m_0^2}{2}\phi_x^2+\frac{\lambda}{4}\phi_x^4\Big)+\frac{\kappa}{2}\sum_{\langle x,y\rangle}(\phi_x-\phi_y)^2,
\]
the Hessian satisfies \(\nabla^2 S(\phi)\ge m_0^2 I\). The associated Gibbs measure satisfies \(CD(m_0^2,\infty)\) and hence has a Poincaré constant (spectral gap) at least \(m_0^2\).  
Assumptions: \(m_0^2>0\), \(\lambda\ge 0\), \(\kappa\ge 0\).  
Proof: The on-site potential contributes a diagonal Hessian with entries \(\ge m_0^2\); the nearest-neighbor Laplacian term is positive semidefinite; apply Bakry–Émery on \(\mathbb R^{|\Lambda|}\).  
Sources: SYNTH_P19_scalar_prototype_gap.md [theorem-and-proof]

---

Theorem: Prokhorov theorem  
ID: theorem-prokhorov  
Statement: In a complete separable metric space, a family of probability measures is relatively compact in the weak topology if and only if it is tight.  
Assumptions: Polish (complete separable metric) state space.  
Sources: SYNTH_P16_measure_tightness.md [prokhorov-statement]

---

Proposition: Sub-Gaussian tails imply exponential square moments  
ID: proposition-tails-imply-exponential-square-moment  
Statement: If \(X\ge 0\) satisfies \(\mathbb P(X\ge r)\le e^{-\alpha r^2}\) for all \(r\ge r_0\), then for any \(0<\theta<\alpha\), \(\mathbb E[e^{\theta X^2}]<\infty\).  
Assumptions: Tail bound of the stated form.  
Proof: Write \(\mathbb E[e^{\theta X^2}]=\int_0^\infty \mathbb P(e^{\theta X^2}\ge t)\,dt=\int_0^\infty \mathbb P(X\ge \sqrt{\frac{1}{\theta}\log t})\,dt\) and split the integral at \(t=e^{\theta r_0^2}\); bound the tail part by \(\int_{e^{\theta r_0^2}}^\infty t^{-\alpha/\theta}\,dt<\infty\).  
Sources: SYNTH_P16_measure_tightness.md [proposition-a-three-proof]

---

Lemma: Closed balls are not compact in an infinite-dimensional Hilbert space  
ID: lemma-closed-balls-not-compact-in-infinite-dimensional-hilbert  
Statement: If \(H\) is an infinite-dimensional Hilbert space, no closed ball \(B_R=\{x:\|x\|\le R\}\) is compact in the norm topology.  
Assumptions: \(H\) infinite dimensional.  
Proof: Let \(\{e_k\}\) be an orthonormal basis. Then \(e_k\in B_1\) and \(\|e_k-e_\ell\|=\sqrt2\) for \(k\neq \ell\), hence no Cauchy subsequence exists in \(B_1\), so \(B_1\) is not sequentially compact and thus not compact.  
Sources: SYNTH_P16_measure_tightness.md [ball-noncompact-proof]

---

Lemma: Uniform exponential integrability of the norm does not imply tightness in infinite dimensions  
ID: lemma-uniform-norm-exponential-moment-not-imply-tightness  
Statement: There exist probability measures \(\{\mu_n\}\) on an infinite-dimensional Hilbert space \(H\) with \(\sup_n \int e^{\theta\|x\|^2}\,d\mu_n(x)<\infty\) for all \(\theta\), yet \(\{\mu_n\}\) is not tight in \(H\).  
Assumptions: \(H\) infinite dimensional.  
Sources: SYNTH_P16_measure_tightness.md [sphere-counterexample]

---

# Conditional Results and External Assumptions

Hypothesis: UV log-forest control  
ID: hypothesis-log-forest-uv-control  
Statement: For any fixed local observable \(F\) and its lattice discretization \(F_a\), there exists \(k\ge 0\) such that  
\[
\|\nabla F_a\|_{L^2(\mu_a)} \;\le\; C(F)\,(\log(1/a))^k
\quad\text{as }a\to 0.
\]  
Assumptions: As stated.  
Sources: SYNTH_CONJ_A_log_forest_uv.md [conjecture-a-statement]

---

Hypothesis: Anomaly source positivity in the effective Hessian flow  
ID: hypothesis-anomaly-source-positivity  
Statement: Along the (projected) Hessian flow, the “anomaly source term” in the minimal-eigenvalue inequality satisfies a uniform lower bound  
\[
\sigma_{\mathrm{anomaly}}(t)\ \ge\ \sigma_0\ >\ 0
\quad\text{for all sufficiently large }t.
\]  
Assumptions: As stated.  
Sources: SYNTH_CONJ_B_anomaly_source.md [conjecture-b-statement]

---

Hypothesis: Continuum polarity of reducibles  
ID: hypothesis-continuum-polarity-of-reducibles  
Statement: In the continuum Yang–Mills Dirichlet form setting, the set \(\Sigma\) of reducible connections has zero capacity: \(\mathrm{Cap}_\mu(\Sigma)=0\).  
Assumptions: Existence of the continuum Dirichlet form and capacity notion `definition-capacity-dirichlet-form`.  
Sources: SYNTH_CONJ_C_continuum_polarity.md [conjecture-c-statement]

---

Hypothesis: LSI lifting and stability under the continuum limit  
ID: hypothesis-lsi-lifting-stability  
Statement: A uniform lattice log-Sobolev inequality (or \(CD(\rho_0,\infty)\)) for the lattice measures \(\mu_a\) lifts to the continuum limit measure \(\mu\) under an appropriate convergence (e.g., Mosco-type convergence of Dirichlet forms), yielding an LSI with the same constant \(\rho_0\).  
Assumptions: Uniform lattice LSI/BE bound and a convergence framework.  
Sources: PROOF_05_Lifting_Lemma.md [conjecture-d-lifting], SYNTH_CONJ_C_continuum_polarity.md [mosco-capacity-language]

---

Hypothesis: Spectral gap implies mass gap through OS reconstruction  
ID: hypothesis-spectral-gap-to-mass-gap  
Statement: If a continuum Euclidean Yang–Mills theory satisfies reflection positivity and related OS axioms, and if its reconstructed Hamiltonian has a strictly positive spectral gap, then the theory has a mass gap (exponential decay of Euclidean two-point functions and positive Minkowski mass).  
Assumptions: OS axioms and a positive Hamiltonian spectral gap.  
Sources: SYNTH_CONJ_D_spectral_to_mass.md [conjecture-d-statement], SYNTH_CONJ_D_spectral_to_mass.md [os-reconstruction]

---

Hypothesis: Local gap dominates topology  
ID: hypothesis-local-gap-dominates-topology  
Statement: There is a local Poincaré constant \(\lambda_{\mathrm{loc}}>0\), uniform in volume, controlling the variance of local observables within any topological sector, while the global gap may be reduced by tunneling between sectors without affecting local relaxation.  
Assumptions: As stated (IR-1 and IR-2).  
Sources: SYNTH_CONJ_IR_local_gap.md [conjecture-ir]

---

Hypothesis: Strong-coupling transfer-matrix gap  
ID: hypothesis-transfer-matrix-gap-strong-coupling  
Statement: In a strong-coupling regime, the (lattice) transfer matrix has a spectral gap above the vacuum, implying exponential decay of time-separated correlations and a mass gap at fixed lattice spacing.  
Assumptions: Strong coupling and transfer-matrix formulation.  
Sources: SYNTH_P03_transfer_matrix_gap.md [statement]

---

Hypothesis: RG flow stability package  
ID: hypothesis-rg-flow-stability-package  
Statement: The RG/flow analysis assumes: a curvature commutator bound \(|K_t|\lesssim g(t)^2\), a trace bound \(\mathrm{Tr}(h_t)\lesssim g(t)^2\), an anomaly lower bound, asymptotic freedom for \(g(t)\), and an initial positivity of \(\lambda_{\min}(h_t)\) at a starting time.  
Assumptions: As stated.  
Sources: SYNTH_P14_rg_flow_stability.md [hypotheses-block]

---

Conditional theorem: Persistence of a positive minimal eigenvalue under the RG flow hypotheses  
ID: conditional-theorem-gap-persistence-under-rg-flow  
Statement: Under `hypothesis-rg-flow-stability-package`, the minimal eigenvalue \(\lambda_{\min}(h_t)\) stays uniformly bounded below by a strictly positive constant for all \(t\) beyond the initial time.  
Assumptions: `hypothesis-rg-flow-stability-package` and the Riccati-type comparison inequality for \(\lambda_{\min}\).  
Sources: SYNTH_P14_rg_flow_stability.md [conditional-persistence-theorem]

---

Conditional theorem: Trace monotonicity under the PBH model  
ID: conditional-theorem-trace-monotone-under-pbh  
Statement: If \(h_t\) evolves by `interface-pbh-hessian-flow-equation` with \(\mathrm{Tr}([h_t,K_t])=0\) and \(\mathrm{Tr}(\Sigma_t)=0\), then  
\[
\frac{d}{dt}\mathrm{Tr}(h_t) = -2\,\mathrm{Tr}(h_t^2)\le 0,
\]
so \(\mathrm{Tr}(h_t)\) is nonincreasing.  
Assumptions: `interface-pbh-hessian-flow-equation` plus trace conditions.  
Proof: Take the trace of the evolution equation and use \(\mathrm{Tr}([A,B])=0\).  
Sources: SYNTH_P17_trace_bound.md [trace-monotonicity]

---
