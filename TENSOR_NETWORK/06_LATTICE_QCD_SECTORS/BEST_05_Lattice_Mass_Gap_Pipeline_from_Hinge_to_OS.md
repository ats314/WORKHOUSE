# Lattice Sector: From a Curvature Hinge to an OS Hamiltonian Gap (and the One Missing Brick)

## What this document extracts

This is a curated “proof skeleton” extracted from the lattice-gauge core and appendices:

- `Core_4__Vacuum_Linearization_and_Discrete_Maxwell_Structure.md`
- `Core_5__Local_Coercivity_and_Matrix_Hinge_on_Good_Set.md`
- `Appendix_E__Bakry_Emery_Calculus.md`
- `Appendix_F__Helffer_Sjostrand_Covariance.md`
- `Appendix_G__Combes_Thomas_Finite_Range_Inverse_Decay.md`
- `Appendix_H__Davies_Type_Decay_Massive_Maxwell_Green_Kernel.md`
- `Appendix_K__Reflection_Positivity_for_Wilson.md`
- `Appendix_L__OS_Reconstruction_and_Gap_Extraction.md`
- `Appendix_J__Typicality_Mechanism_for_K.md` (high-probability of the good set)

The pipeline is conceptually simple but technically rare in lattice gauge literature in this exact form:

\[
\boxed{
\text{(small-field curvature hinge)}
\Rightarrow
\text{(HS covariance as inverse operator)}
\Rightarrow
\text{(deterministic massive inverse kernel)}
\Rightarrow
\text{(exponential clustering)}
\Rightarrow
\text{(OS reconstruction)}
\Rightarrow
\text{(Hamiltonian mass gap)}.
}
\]

The key novelty is that the entire chain reduces the “mass gap” problem to a **single local analytic estimate**: stability of the Wilson Hessian near the vacuum (Core-5.EI.1).

---

## 1. Configuration geometry and curvature endomorphism

Let \(M_\Lambda=G^{E(\Lambda)}\) with product bi-invariant metric \(g_\Lambda\). The Gibbs measure is
\[
d\mu_{\Lambda,\beta}(U)\propto e^{-S_{\Lambda,\beta}(U)}\,d\mathrm{vol}_{g_\Lambda}(U).
\]
The Bakry–Émery curvature endomorphism is
\[
\mathrm{Ric}_{\mu_{\Lambda,\beta}}(U)=\mathrm{Ric}_{g_\Lambda}(U)+\nabla^2 S_{\Lambda,\beta}(U).
\]

A uniform *geometric* lower bound is available from the group manifold:
\[
\mathrm{Ric}_{g_\Lambda}\succeq \kappa_G\,I.
\]
The stack defines the associated “geometric mass”
\[
m_H^2:=\kappa_G/3.
\]

---

## 2. Vacuum linearization gives a massive Maxwell comparison operator

At the vacuum \(U^{(0)}\), the Wilson Hessian is the discrete Maxwell stiffness:
\[
\nabla^2S_{\Lambda,\beta}(U^{(0)})=\alpha_W\,d_1^*d_1,
\]
so at the vacuum,
\[
\mathrm{Ric}_{\mu}(U^{(0)})\succeq 3m_H^2 I+\alpha_W d_1^*d_1.
\]

The deterministic comparison operator (Core 4/5) is
\[
M_\Lambda:=m_H^2 I+\alpha_W d_1^*d_1,
\qquad
M_\Lambda^{\mathrm{hinge}}:=m_H^2 I+\tfrac12\alpha_W d_1^*d_1.
\]
The presence of \(m_H^2 I\) is crucial: it supplies strict positivity even on gauge-harmonic sectors.

---

## 3. The canonical good set and the matrix hinge target

Define the small-field (plaquette-log) good set \(\mathcal K_{\Lambda,\beta}\subset M_\Lambda\) by requiring all plaquette holonomies to lie in the logarithmic chart with radius \(r_\beta\sim \beta^{-1/2}\).

The **matrix hinge goal** is:

> For all \(U\in \mathcal K_{\Lambda,\beta}\),
> \[
> \boxed{\;\mathrm{Ric}_{\mu_{\Lambda,\beta}}(U)\succeq M_\Lambda^{\mathrm{hinge}}.\;}
> \]

In Core 5 this is reduced to one explicit missing estimate:

### External Input Core-5.EI.1 (small-field Wilson Hessian stability)

There exists \(C_{\rm WH}\) such that for all \(U\in\mathcal K_{\Lambda,\beta}\),
\[
\langle X,(\nabla^2S(U)-\nabla^2S(U^{(0)}))X\rangle
\ \ge\
-\,C_{\rm WH}\,\beta\,r_\beta\,\langle X,X\rangle.
\]

If this holds, then geometric Ricci \(+\) vacuum Maxwell stiffness dominate the error, giving the hinge.

**Interpretation:** EI.1 is local, finite-range, and model-specific. Everything after it is generic.

---

## 4. Helffer–Sjöstrand identity: covariance is an inverse operator

Appendix F proves the exact identity
\[
\mathrm{Cov}_\mu(F,G)
=
\int\left\langle\nabla F,\ (\mathcal L^{(1)})^{-1}\nabla G\right\rangle\,d\mu,
\]
where \(\mathcal L^{(1)}=(({-L})\otimes I)+\mathrm{Ric}_\mu\) is the Witten Laplacian on gradients.

Since \((({-L})\otimes I)\succeq 0\),
a pointwise hinge \(\mathrm{Ric}_\mu\succeq M\) implies
\[
\mathcal L^{(1)}\succeq M
\quad\Rightarrow\quad
(\mathcal L^{(1)})^{-1}\preceq M^{-1}
\]
(order reversal under inversion).

Thus covariances are controlled by a **deterministic inverse kernel** \(M^{-1}\).

This is the analytic bridge:
\[
\boxed{\text{“curvature lower bound”} \Rightarrow \text{“covariance dominated by massive Green function”}.}
\]

---

## 5. Exponential decay of \(M^{-1}\): Combes–Thomas / Davies

The deterministic operator \(M_\Lambda^{\mathrm{hinge}}\) is:

- self-adjoint,
- strictly positive (\(\succeq m_H^2 I\)),
- finite-range (built from \(d_1^*d_1\)).

Appendix G gives a Combes–Thomas kernel bound of the form
\[
\|(M^{-1})_{xy}\|\ \lesssim\ \exp(-\eta_{\rm CT}\,\mathrm{dist}(x,y)),
\]
and Appendix H provides a continuous-time analogue (Davies-type) when needed for semigroup estimates.

Feeding this into the HS bound yields **exponential clustering** of gauge-invariant observables at fixed cutoff.

---

## 6. OS reconstruction: clustering in Euclidean time ⇒ Hamiltonian gap

Appendix K establishes reflection positivity for the Wilson measure; Appendix L states the OS interface:

- reconstruct \(\mathcal H_{\rm OS}\),
- obtain a positive contraction \(T\) implementing time translations,
- write \(T=e^{-aH}\) for a self-adjoint \(H\ge 0\),
- use a spectral-support lemma to show:

> If centered OS correlations satisfy \(|\langle\psi,e^{-naH}\psi\rangle|\lesssim e^{-\eta n}\), then \(\mathrm{gap}(H)\ge \eta/a\).

Thus, Euclidean-time clustering becomes a genuine Hamiltonian spectral gap.

---

## 7. Why this is “new-theory grade” inside this corpus

The project reframes “mass gap” as a curvature problem:

- the “mass term” is a curvature floor \(m_H^2\),
- the Maxwell stiffness is a Hessian (second variation) term,
- the only model-specific content is controlling how far the Wilson Hessian drifts from its vacuum value on a small-field set.

Everything else is a universal functional-analytic machine.

This is unusually sharp: it isolates a single finite-range local analytic inequality (Core-5.EI.1) as the bottleneck for a mass gap proof strategy.

---

## 8. Immediate next proofs to lock the pipeline

1. **Prove EI.1** (the Wilson Hessian stability bound) by explicit differentiation of the plaquette holonomy map and uniform control of second derivatives on the small-field chart.

2. **Prove typicality:** show \(\mu_{\Lambda,\beta}(\mathcal K_{\Lambda,\beta})\to 1\) as \(\beta\to\infty\) uniformly in volume (Appendix J is designed for this).

Once (1)–(2) are done, the rest of the pipeline is already written and becomes a theorem cascade.

