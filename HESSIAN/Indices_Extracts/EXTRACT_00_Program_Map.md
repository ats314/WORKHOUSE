---
title: "SWIM2 Selected Extracts: Geometric–Analytic Mechanisms for a Yang–Mills Mass Gap"
author: "Curated by ChatGPT (GPT‑5.2 Pro)"
date: "2025-12-31"
---

# Scope and intent

This document is **not** a full reproduction of the project archive.  
It is a curated, self‑contained set of the *most structurally novel* mechanisms in the SWIM2 proof program, as extracted from:

- `PROOF_04_Geometric_Mass_Derivation.md`
- `SYNTH_P04_haar_geometry_supplement.md`
- `UNIF_CONJB_STRATEGY.md`
- `SYNTH_P06_riccati_hessian_flow.md`
- `SYNTH_P17_trace_bound.md`
- `PROOF_02_Gradient_Flow_Stability.md`
- `SYNTH_P20_stratified_parabolic_principle.md`
- `SYNTH_P01_lattice_polarity.md`, `SYNTH_P18_gaussian_polarity.md`
- `PROOF_05_Lifting_Lemma.md`, `SYNTH_P11_continuum_limit.md`, `SYNTH_CONJ_D_spectral_to_mass.md`

The emphasis is on **derivations and proof mechanisms** that look reusable beyond this specific problem.

# The “proof chain” in one page

Let $\mathcal A_\Lambda = G^{E(\Lambda)}$ be the lattice gauge configuration manifold
for a finite lattice $\Lambda$, with compact structure group $G=\mathrm{SU}(N)$.
Equip $\mathcal A_\Lambda$ with the **product bi‑invariant metric** (the “Haar metric”),
and define the Gibbs measure
\[
  d\mu_\beta(U) \propto e^{-\beta S_W(U)}\,d\mu_{\mathrm{Haar}}(U),
\]
where $S_W$ is the Wilson plaquette action.

The project’s central strategy is to make a mass gap emerge from **convexity + curvature**:

1. **(Geometric mass / Bakry–Émery spark)**  
   Prove a lower bound on the **Bakry–Émery tensor**
   \[
     \mathrm{Ric}_{\mu_\beta} := \mathrm{Ric}_g + \beta \nabla^2 S_W,
   \]
   at least on the **horizontal** directions after gauge reduction.
   This acts like a *geometric mass term*.

2. **(Functional inequalities)**  
   A Bakry–Émery lower bound gives Poincaré and log‑Sobolev inequalities (LSI).
   These provide **spectral gaps** for the associated Markov generator.

3. **(Flow stability / PBH Riccati mechanism)**  
   Track how the **Hessian** of an effective action evolves under a flow
   (Wilson flow / generalized gradient flow).  
   The key structure is a **Riccati‑type inequality**
   \[
     \dot H \sim -H^2 + (\text{curvature / anomaly source}),
   \]
   which turns positivity of the source into **uniform lower bounds** on $H$.

4. **(Singular set bypass: polarity + maximum principle)**  
   Gauge reduction produces a singular subset (reducibles).  
   If that set is **polar** (capacity zero), a stratified parabolic maximum principle
   propagates positivity *through* the singularities.

5. **(Continuum limit)**  
   A “lifting lemma” (Mosco / $\Gamma$‑convergence of Dirichlet forms, or RCD‑stability)
   transfers uniform LSI/spectral gaps from lattice measures $\mu_{\beta,a}$ to a continuum limit measure,
   which is then related to a **mass gap** via reconstruction (transfer matrix / OS).

# What is actually “new” here?

The individual tools are classical; the novelty is the **coupling**:

- **Geometric mass from Haar + Wilson Hessian**: a concrete lower bound
  on $\mathrm{Ric}_{\mu_\beta}$ on the horizontal bundle suggests “mass from geometry”.
- **PBH (Projected Bochner–Hessian) flow**: exporting PDE maximum principles
  into operator/Hessian evolution in gauge configuration spaces.
- **Polarity as a technical solvent**: using capacity zero to avoid boundary conditions
  at the reducible locus, so that analytic inequalities remain global.

Each of the next documents isolates one of these mechanisms and pushes it into a clean lemma/theorem format.

# Documents in this extract set

- `EXTRACT_01_Haar_Geometric_Mass.md` — Bakry–Émery lower bound on horizontals (“geometric mass”)
- `EXTRACT_02_PBH_Riccati_Flow.md` — Riccati comparison principle for Hessian eigenvalues (+ toy numerics)
- `EXTRACT_03_GradientFlow_as_RG.md` — exact action‑space flow equation (Yamamura) and truncation numerics
- `EXTRACT_04_Polarity_and_MaxPrinciple.md` — polar singular sets and stratified parabolic principle
- `EXTRACT_05_Continuum_Lifting_ConjD.md` — lifting log‑Sobolev / spectral gaps to the continuum (Conj. D)

