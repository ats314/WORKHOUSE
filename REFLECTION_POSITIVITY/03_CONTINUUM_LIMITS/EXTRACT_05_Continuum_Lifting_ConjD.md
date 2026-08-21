---
title: "EXTRACT 05 — Continuum Lifting and Conjecture D: From Lattice LSI to a Continuum Mass Gap"
date: "2025-12-31"
---

# Executive summary

Even if one proves strong functional inequalities (Poincaré / LSI) on every finite lattice,
the Millennium problem demands a **continuum** quantum field theory with a **mass gap**.

The archive’s closing mechanism is a *lifting step*:

> uniform lattice functional inequalities + convergence of measures/Dirichlet forms  
> $\Longrightarrow$ continuum functional inequality  
> $\Longrightarrow$ spectral gap for a continuum generator  
> $\Longrightarrow$ mass gap in the reconstructed QFT.

In the project’s language, the hard part is “Conjecture D”.

This extract is based on:

- `PROOF_05_Lifting_Lemma.md`
- `SYNTH_CONJ_D_spectral_to_mass.md`
- `SYNTH_P11_continuum_limit.md`
- (supporting ideas) tightness and reconstruction notes in the synthesis layer

# 1. What must survive the continuum limit?

The lattice objects depend on lattice spacing $a$ (and volume).
One typically considers a family of measures $\mu_{a}$ (or $\mu_{\beta,a}$) on lattice configuration spaces,
and asks for a limit as $a\to 0$ after appropriate renormalization / tuning.

A uniform Poincaré or LSI constant is a *quantitative* statement that must remain stable as $a\to 0$.

# 2. The lifting lemma idea (Dirichlet forms / Mosco convergence)

A standard modern approach:

1. Encode the Markov generator and its spectral gap via a Dirichlet form $(\mathcal E_a,\mathcal D_a)$ on $L^2(\mu_a)$.
2. Show the family $(\mathcal E_a)$ converges (Mosco convergence / $\Gamma$‑convergence) to a limit form $(\mathcal E,\mathcal D)$ on $L^2(\mu)$.
3. Prove that functional inequalities are stable under this convergence when constants are uniform.

The archive’s “lifting lemma” formalizes this plan:
it reduces “lattice LSI $\Rightarrow$ continuum LSI” to proving the right form of convergence and tightness.

# 3. Where metric measure geometry enters (RCD stability heuristic)

Another route emphasized in the project is to work in the synthetic curvature framework:

- If $(X_a,d_a,\mu_a)$ satisfy a curvature-dimension condition (e.g. $\mathrm{RCD}(K,\infty)$),
  and converge in measured Gromov–Hausdorff sense, then the limit inherits $\mathrm{RCD}(K,\infty)$.

Since $\mathrm{RCD}(K,\infty)$ implies LSI and Poincaré inequalities with constants depending on $K$,
this gives a geometric stability route.

The project aims to connect the lattice Bakry–Émery bound (Extract 01) to such a stability theorem.

# 4. From continuum spectral gap to mass gap

A continuum spectral gap for a suitable generator is not automatically the QFT mass gap,
but the archive’s narrative is:

- control Euclidean correlations via LSI/spectral gap,
- reconstruct the Hamiltonian (transfer matrix / Osterwalder–Schrader),
- deduce a **positive mass** (spectral gap above the vacuum) in Minkowski signature.

This is the step explicitly labeled “Conjecture D” in the SWIM2 chain documents.

# 5. Why this extract is included (despite being partly conjectural)

The lifting step is not a “detail”; it is the place where many mass gap attempts die.
What is novel here is that the archive does not treat it as magic:
it isolates it into a precise analytic package (Dirichlet form convergence + inequality stability)
and then connects it to metric-measure geometry (RCD stability).

That is a workable research program even if the final QFT reconstruction is technically heavy.

# 6. Next steps that would genuinely move the needle

1. **Tightness and identification of the limit**  
   Show the lattice measures (after gauge fixing / renormalization) are tight and have subsequential limits.
   Then characterize the limit as a Yang–Mills measure.

2. **Uniform LSI constants across scales**  
   This is the quantitative core. It may require:
   - uniform control on Bakry–Émery curvature on relevant regions,
   - or a Lyapunov + local Poincaré strategy to globalize gaps.

3. **Dirichlet form convergence**  
   Establish Mosco convergence of the lattice Dirichlet forms to a continuum form,
   compatible with the chosen topology on the configuration space.

4. **OS / transfer-matrix bridge**  
   Prove that the continuum spectral gap implied by LSI corresponds to a mass gap
   in the reconstructed QFT Hamiltonian, with the correct scaling.

