---
title: "Constructive Mass Gap Pipeline"
subtitle: "From functional inequalities to OS reconstruction (paper-ready synthesis)"
status: "Synthesis of proved components + clearly labeled open upgrades"
---

# Constructive Mass Gap Pipeline
## From functional inequalities to Osterwalder–Schrader reconstruction

### Abstract
This document distills the most technically promising thread in the project files: a *constructive* route to a Hamiltonian mass gap for lattice gauge theory at fixed cutoff. The pipeline is:

\[
\text{Local coercivity (hinge)} \Rightarrow
\text{uniform functional inequalities (LSI)} \Rightarrow
\text{Helffer–Sjöstrand covariance} \Rightarrow
\text{resolvent off-diagonal decay (Combes–Thomas)} \Rightarrow
\text{exponential clustering} \Rightarrow
\text{OS reconstruction} \Rightarrow
\text{gap extraction}.
\]

The novelty candidate here is not any single ingredient (many are classical), but the *architecture*: the files give an explicit “no-handwaving” dependency chain, including localization/typicality to remove conditioning, and permanence results to pass to limits.

### Scope and what is *actually* claimed
- **Setting:** Euclidean lattice gauge theory with a finite ultraviolet cutoff (fixed lattice spacing).
- **Goal:** A **positive spectral gap** for the reconstructed Hamiltonian, extracted from exponential decay of Euclidean correlations.
- **Important:** This is **not** claiming a full continuum-limit Yang–Mills mass gap theorem. It is a *fixed-cutoff constructive gap program* with an explicit list of upgrades required to reach a continuum theorem.

---

# 1. OS structure at finite volume and fixed cutoff

## 1.1 Configuration space and reflections
Let \(\Lambda \subset \mathbb Z^d\) be a finite box (often \(d=4\) later). The configuration space is a product Lie group
\[
\mathcal C_\Lambda \;=\; \prod_{e\in E_\Lambda} G,
\]
with \(G\) compact (e.g. \(SU(N)\)), equipped with Haar measure and local coordinates near the identity.

Fix an OS reflection plane (a discrete hyperplane). It induces
- an involution \(\theta\) acting on edge variables, and
- a decomposition of observables into “positive time” and “negative time” algebras.

## 1.2 Reflection positivity for the Wilson measure (proved component)
For the Wilson action \(S_\Lambda(U)\), the finite-volume Gibbs measure
\[
d\mu_\Lambda(U)\;\propto\;e^{-S_\Lambda(U)}\,dU
\]
is **reflection positive** with respect to \(\theta\), i.e.
\[
\langle \theta(F)\,F\rangle_{\mu_\Lambda}\ge 0
\quad \text{for all }F\in \mathcal A_+.
\]

**Project-file provenance:** Appendix K develops this at the level of the lattice action and reflection plane; Appendix L uses it as OS input.

---

# 2. From local coercivity to uniform functional inequalities

## 2.1 The Bakry–Émery \(\Gamma_2\) identity with drift (proved component)
On \(\mathcal C_\Lambda\), introduce the diffusion generator
\[
\mathcal L = \Delta - \nabla V \cdot \nabla,
\]
associated to the Gibbs density \(e^{-V}\). The files derive a **matrix-valued** Bakry–Émery curvature structure via the \(\Gamma_2\) identity, tailored to a product Lie-group manifold with drift.

Key outputs:
- a curvature matrix \(\mathrm{Ric}_V\) controlling coercivity,
- a way to treat non-quadratic potentials via a “hinge” inequality.

## 2.2 The local matrix hinge inequality (proved component)
Near the vacuum configuration, the Hessian of the Wilson potential has a *degenerate* direction structure. The project replaces a naive uniform convexity requirement by a **local hinge inequality**:

\[
\mathrm{Hess}\,V \;\succeq\; \text{(massive Maxwell operator)} \;-\; \text{controlled error}.
\]

The “massive Maxwell operator” appears as the correct coercive object for gauge degrees of freedom after linearization.

## 2.3 Lyapunov drift \(\Rightarrow\) global LSI, uniform in volume (proved component)
A Lyapunov function \(W\) is constructed so that outside a compact set
\[
\mathcal L W \le -\lambda W + b.
\]
Combined with the local coercivity on the “good” region, this yields a **Log–Sobolev inequality**
\[
\mathrm{Ent}_{\mu_\Lambda}(f^2)\;\le\; \frac{2}{\rho}\int |\nabla f|^2\,d\mu_\Lambda,
\]
with constant \(\rho>0\) **uniform in \(|\Lambda|\)** at fixed cutoff.

This is the essential quantitative input that later implies concentration and correlation decay.

---

# 3. Covariance representation and resolvent decay

## 3.1 Helffer–Sjöstrand covariance representation (proved component)
For centered observables \(F,G\), the covariance admits a resolvent formula
\[
\mathrm{Cov}_{\mu_\Lambda}(F,G)
=
\left\langle \nabla F,\; \mathcal H^{-1}\nabla G\right\rangle_{L^2(\mu_\Lambda)},
\]
where \(\mathcal H\) is a (Witten-type) second-order operator derived from \(\mathcal L\).

This rephrases correlation decay as a **Green’s function decay** problem for \(\mathcal H^{-1}\).

## 3.2 Combes–Thomas / conjugation method for finite-range inverse decay (proved component)
A Combes–Thomas conjugation argument establishes exponential off-diagonal decay for \(\mathcal H^{-1}\), schematically:
\[
|\langle \nabla F,\,\mathcal H^{-1}\nabla G\rangle|
\;\lesssim\;
e^{-\gamma\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)}\,\|\nabla F\|\,\|\nabla G\|.
\]

The project states this as an abstract finite-range inverse decay lemma, designed to plug directly into the HS formula.

---

# 4. From conditional clustering to unconditional clustering

## 4.1 Localization event \(K_\Lambda(r)\) (proved component)
To keep the analysis in the “elliptic, vacuum-like” region where the hinge inequality is effective, the project defines a localization event \(K_\Lambda(r)\) (a cylinder event on plaquettes / local coordinates) encoding:
- smallness of local curvature variables,
- control of Jacobians and coordinate charts,
- stability of the coercivity bounds.

## 4.2 Typicality (proved component)
A concentration argument yields an explicit typicality bound:
\[
\mu_\Lambda(K_\Lambda(r)^c) \;\le\; C\,e^{-c\,r^2\,|\Lambda|}.
\]
This is what turns the analysis into something “thermodynamic”: bad sets are exponentially rare in volume.

## 4.3 Covariance decomposition across \(K_\Lambda(r)\) (proved component)
Decompose:
\[
\mathrm{Cov}(F,G)
=
\mu(K)\,\mathrm{Cov}(F,G\mid K)
+\text{error terms controlled by }\mu(K^c).
\]
Choosing \(r\) as a suitable function of \(|\Lambda|\) yields unconditional exponential clustering at fixed cutoff.

---

# 5. OS reconstruction and gap extraction

## 5.1 OS Hilbert space and transfer matrix (proved component)
Given reflection positivity, translation invariance, and clustering, OS reconstruction builds:
- a Hilbert space \(\mathcal H\),
- a transfer matrix \(T\) acting as Euclidean time translation,
- a self-adjoint Hamiltonian \(H\ge 0\) with \(T=e^{-aH}\).

## 5.2 From exponential clustering to a mass gap (proved component)
If Euclidean correlations decay exponentially in time separation, then the spectral theorem implies the Hamiltonian has a **gap above the vacuum**:
\[
\exists\,m>0:\quad \sigma(H)\cap(0,m)=\varnothing.
\]

The project isolates this implication as a standalone lemma and packages it as the final “extraction” step.

---

# 6. What looks publishable vs. what remains to upgrade

## 6.1 Likely publishable now (in principle)
1. **Uniform-in-volume LSI for the fixed-cutoff Wilson measure on the good set**, obtained via matrix \(\Gamma_2\) + hinge + drift.
2. **The HS + Combes–Thomas chain** specialized to the lattice gauge setting, with explicit distance metrics and finite-range structure.
3. **Localization + typicality** as a clean mechanism to uncondition correlation decay.

## 6.2 Upgrades required to reach a full “Yang–Mills gap” theorem (open work)
- **Thermodynamic limit:** show existence of limit points of \(\mu_\Lambda\) as \(|\Lambda|\to\infty\), and permanence of OS structure in the limit.
- **Coarse graining / RG permanence:** show reflection positivity and OS axioms are stable under reflection-equivariant block-spin / projective limits of cylinder observables.
- **Continuum limit:** control the cutoff removal \(a\to 0\) with uniform estimates that survive renormalization.

These are explicitly named and structurally separated in the project files; they are the correct remaining “holes” to close.

---

# Dependencies in the project
This synthesis is extracted primarily from:
- Appendix D (local matrix hinge inequality),
- Appendix E (Lyapunov drift and uniform functional inequalities),
- Appendix F (Helffer–Sjöstrand covariance representation),
- Appendix G (Combes–Thomas / inverse decay lemma),
- Appendix I–J (localization and typicality),
- Appendix K (reflection positivity),
- Appendix L (OS reconstruction and gap extraction).
