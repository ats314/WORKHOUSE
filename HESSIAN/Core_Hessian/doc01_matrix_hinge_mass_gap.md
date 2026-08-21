# Matrix-Hinge \(\Rightarrow\) Fixed-Cutoff Mass Gap (Analytic Spine)

*This note extracts the core “curvature \(\Rightarrow\) gap” mechanism as a standalone analytic module, in a form that is portable across compact semisimple gauge groups (in particular \(G=\mathrm{SU}(3)\)) and across lattice volumes.*

---

## 1. Configuration geometry and generator

Let \(\Lambda\) be a finite \(4\)-dimensional torus or box, with oriented edge set \(E(\Lambda)\) and plaquette set \(P(\Lambda)\).  
Let \(G=\mathrm{SU}(N)\) with Lie algebra \(\mathfrak g\) and a fixed bi-invariant Riemannian metric.

The configuration manifold is the product Lie group
\[
M_\Lambda := G^{E(\Lambda)}.
\]
The Wilson action is
\[
S_\Lambda(U)=\sum_{p\in P(\Lambda)}\Phi_\beta(U_p),\qquad 
\Phi_\beta(g)=\beta\Bigl(1-\tfrac1N\Re\operatorname{Tr}g\Bigr).
\]

Let \(\mu_\Lambda\propto e^{-S_\Lambda}\,d\mathrm{vol}_{g_\Lambda}\) be the Gibbs measure.

The associated Langevin generator on \(M_\Lambda\) is
\[
L_\Lambda=\Delta_\Lambda-\langle \nabla S_\Lambda,\nabla(\cdot)\rangle.
\]

---

## 2. Bochner–\(\Gamma_2\) identity and the Bakry–Émery curvature matrix

Define carré-du-champ
\[
\Gamma(f)=|\nabla f|^2,\qquad 
\Gamma_2(f)=\tfrac12L\Gamma(f)-\Gamma(f,Lf).
\]

The Bochner identity with drift yields the matrix object
\[
\mathrm{Ric}_{\mu_\Lambda}(U):=\mathrm{Ric}_{g_\Lambda}(U)+\nabla^2 S_\Lambda(U),
\]
and the standard implication:
\[
\mathrm{Ric}_{\mu_\Lambda}\succeq \rho\,\mathrm{Id}
\quad\Longrightarrow\quad
\Gamma_2(f)\ge \rho\,\Gamma(f)
\quad(\text{CD}(\rho,\infty)).
\]

---

## 3. The matrix-hinge inequality on the small-field region \(K_\Lambda(r)\)

Define a linkwise small-field set \(K_\Lambda(r)\subset M_\Lambda\) by the condition that each link \(U_b\) lies in a fixed metric ball \(B^G_r(\mathbf 1)\subset G\). (Any equivalent “good set” definition that forces every plaquette holonomy into a small neighborhood of \(\mathbf 1\) works.)

The key technical feature in this project is that the curvature lower bound is kept **matrix-valued**, retaining the positive semidefinite cochain operator \(d_1^*d_1\) instead of collapsing it to scalar bounds.

Schematic matrix-hinge form:
\[
\mathrm{Ric}_{\mu_\Lambda}(U)\ \succeq\ \bigl(c_H-R_W(r)\bigr)\,\mathrm{Id}
\;+\;\alpha\, d_1^*d_1
\qquad\text{for all }U\in K_\Lambda(r),
\]
where:
- \(c_H\) is the (strictly positive) “Haar mass” contribution coming from \(\mathrm{Ric}_{g_\Lambda}\) / Jacobian convexity near the identity,
- \(R_W(r)\) is the Wilson remainder (small if \(r\) is small),
- \(\alpha\asymp \beta/\lambda_\rho\) is the vacuum stiffness scale.

**Why this is powerful:** the \(\alpha d_1^*d_1\) term is *exactly* the lattice Maxwell stiffness operator on \(1\)-cochains. Once it appears in the curvature matrix, it will reappear as a resolvent kernel in covariance bounds.

---

## 4. From local curvature to local Poincaré / LSI on \(K_\Lambda(r)\)

By CD\((\rho,\infty)\) on \(K_\Lambda(r)\), one obtains local functional inequalities on the good set:
\[
\operatorname{Var}_{\mu(\cdot\mid K)}(f)\ \le\ C_K\int_{K}|\nabla f|^2\,d\mu,
\]
and (optionally) a local log-Sobolev inequality, with constants depending on \((\beta,r,G)\) but **independent of** \(|\Lambda|\).

This is the analytic “hinge module.”

---

## 5. Global Poincaré via drift domination on \(K^c\) (conditional input)

To upgrade local control on \(K\) to global control on all of \(M_\Lambda\), the manuscript uses a K/\(K^c\) variance decomposition plus a “drift domination” inequality on the bad set.

The single missing geometric input that closes this route cleanly is:

**Coercivity / no-flat-rough-plateaus (Assumption A′):**  
there exist \(\varepsilon_0,c_0>0\) (independent of \(|\Lambda|\)) such that
\[
U\in K^c(\varepsilon_0)\quad\Longrightarrow\quad |\nabla S_\Lambda(U)|\ge c_0.
\]

Given A′, integration-by-parts and a standard “Foster–Lyapunov + gluing” pattern yields a volume-uniform global Poincaré inequality
\[
\operatorname{Var}_{\mu_\Lambda}(f)\ \le\ C_P\int_{M_\Lambda}|\nabla f|^2\,d\mu_\Lambda,
\qquad C_P\text{ independent of }|\Lambda|.
\]

---

## 6. Covariance as a resolvent of a massive Maxwell operator

A Helffer–Sjöstrand-type covariance representation converts Poincaré + curvature control into an estimate involving the inverse of a **massive Maxwell operator**
\[
M := m^2\,\mathrm{Id}+\alpha\,d_1^*d_1
\quad\text{acting on }\ell^2(E(\Lambda);\mathfrak g).
\]

The project then proves off-diagonal decay for \(M^{-1}\) **uniformly in volume** via a Combes–Thomas / Davies conjugation argument for finite-range operators on the link graph.

This is the second major conceptual hinge: the nonabelian gauge problem is reduced to a *robust* linear-algebraic Green-kernel decay lemma for a finite-range positive operator.

---

## 7. Exponential clustering \(\Rightarrow\) OS Hamiltonian gap (fixed cutoff)

Once (i) covariance is controlled by a decaying kernel and (ii) typicality bounds keep the measure from spending too much time in \(K^c\), the fixed-cutoff Euclidean measure exhibits exponential clustering of local observables:
\[
|\operatorname{Cov}_{\mu_{\Lambda,\beta}}(F,G)|
\ \le\ C(F,G)\,e^{-\eta\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)}.
\]

OS reconstruction (reflection positivity + time-translation invariance) then upgrades Euclidean time decay to a spectral gap of the reconstructed Hamiltonian \(H_a\) at lattice spacing \(a\):
\[
\mathrm{gap}(H_a)\ \ge\ \frac{\eta(a)}{a}.
\]

---

## 8. What is potentially new here

The “exciting” technical synthesis is:

1. **Matrix (not scalar) Bakry–Émery curvature** that preserves the Maxwell stiffness operator \(d_1^*d_1\) at the level of \(\mathrm{Ric}_\mu\).
2. A **fully explicit linear-algebraic Combes–Thomas module** giving exponential decay for \((m^2I+\alpha d_1^*d_1)^{-1}\) with constants uniform in volume and boundary conditions.
3. A modular pipeline where the **only** nontrivial geometric unknown is A′ (“rough \(\Rightarrow\) force bounded below”), which is isolated and attacked separately.

This gives a clean “audit trail” for a fixed-cutoff mass gap proof where every dependency is visible and either proved or explicitly flagged.

---

## 9. Next steps that would strengthen / generalize the theory

1. **Prove A′ (or a sufficient surrogate) for \(\mathrm{SU}(3)\).**  
   The SU(2) local cancellation geometry suggests a general “Cartan-alignment exceptional set” mechanism. For SU(3), one expects the exceptional set to be configurations where all incident plaquette forces lie in a common Cartan subalgebra and the transports preserve it.

2. **Make “typicality” quantitative without LSI.**  
   The project already leans toward a Poincaré-only route; the remaining bookkeeping is concentration at a separation scale suitable for patching.

3. **Continuum conditionality:**  
   formulate the minimal additional input (scaling-limit existence + physical scaling of \(\eta(a)\)) needed to upgrade fixed-cutoff gap to a continuum gap.

---

## Sources inside this project

- Bochner/\(\Gamma_2\) module: `## 6.1 Bochner Γ_2 identity with drift and the Bakry–Émery curvature matrix.txt`  
- Matrix-hinge module and Wilson vacuum stiffness: `## 5.1 Vacuum configuration and linearization.txt`, `SECTION_1.md`  
- Covariance decomposition: `## 8.1 Covariance decomposition across an event (K).txt`  
- Combes–Thomas/Davies decay: `### 9.1 Abstract finite-range inverse decay lemma...`, `003_Proposition_9_X_...`, `006_Proposition_9_X_...`, `008_Corollary_9_X_...`  
- Exponential clustering statement: `### 10.1 Exponential clustering at fixed cutoff statement.txt`  
- OS extraction interface: `1 Introduction.md`
