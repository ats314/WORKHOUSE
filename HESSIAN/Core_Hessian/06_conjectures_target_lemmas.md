# Conjectures & Target Lemmas (Every overclaim rewritten honestly)

This file is meant to be brutally clean: it rewrites the parts of the “mass gap proof narrative”
that were overstated into precise conjectures/hypotheses.

It also identifies **what exact lemmas** would upgrade the chain from conditional to actual.

---

## C0. Scope disclaimer

Everything here is formulated so that it can be:
- *true or false*,
- attacked directly,
- and cited safely in a paper as “Hypothesis / Conjecture.”

---

## C1. Target Lemma: Uniform Wilson Hessian bound in exponential coordinates

Let $S_W(A)$ be the Wilson action written in exponential coordinates $U_\ell=\exp(A_\ell)$.

**Target lemma (uniform block bound).**  
There exists a constant $C_W<\infty$ depending only on the group and local lattice geometry such that on any finite lattice,
\[
\|\nabla^2 S_W(A)\|_{\mathrm{op}} \le C_W\,\beta
\quad\text{for all } A.
\]
A candidate explicit $C_W$ is developed in `07_uniform_wilson_hessian_bound_candidate.md`.

**Why it matters:** it makes all “convexity in a ball” arguments local and volume-stable, and allows Lipschitz bounds for validated numerics.

---

## C2. Hypothesis DR: Dynamic restoration of convexity (YM version)

Let $\Phi_t$ be the chosen “RG-like” smoothing map on gauge fields (gradient flow, diffusion RG, etc.), and define a curvature functional such as
\[
\lambda(t) := \lambda_{\min}\big(\nabla^2 S_{\mathrm{eff},t}(A)\big).
\]

**Hypothesis DR (comparison inequality).**  
Along the flow, $\lambda(t)$ satisfies a Riccati-type inequality
\[
\lambda'(t) \ge -\alpha\,\lambda(t)^2 + \beta_0 - \varepsilon(t),
\]
with $\alpha>0$, $\beta_0>0$ and $\varepsilon$ controlled so that for relevant initial data, $\lambda(t)\ge \rho_0>0$ for all $t\ge t_*$.

**Status:** rigorous for finite-dimensional vHJ models (`01_vhj_hessian_flow_riccati.md`), not proved for SU(3) lattice YM.

---

## C3. Hypothesis MC: Measure concentration into a convex basin (large β)

Let $\mu_\beta$ be the lattice YM measure at inverse coupling $\beta$ and let $\mathcal{D}_\beta$ be a “dynamic basin” (e.g. fields that restore convexity by time $t_*$).

**Hypothesis MC (tail bound).**  
There exist $c,C>0$ (ideally volume-uniform) such that
\[
\mu_\beta(\mathcal{D}_\beta^c) \le C\,e^{-c\,\beta}.
\]
**Status:** plausible but not proven in these files. Numerical attempts exist (sampling $\lambda_{\min}$ under Gaussian-ish draws).

---

## C4. Hypothesis OS-RG: Reflection positivity preserved by the RG step

**Hypothesis OS-RG.**  
The RG map $\mathcal{R}_t$ can be realized as an **OS-positive kernel**:
- reflection-invariant,
- supported on the correct half-space structure,
- and acting by a Markov operator that preserves the OS cone.

Then $\nu_t := (\mathcal{R}_t)_*\mu$ is reflection positive if $\mu$ is.

**Status:** not proven in the current stack. Equivariance of an ODE map is not enough; one needs kernel-level positivity.

---

## C5. Conditional mass-gap theorem (honest version)

If (C1) + (C2) + (C3) + (C4) hold with constants uniform along the asymptotically free scaling trajectory, then:

1. you obtain a uniform Bakry–Émery curvature lower bound in the relevant regime,
2. hence LSI and Poincaré (spectral gap) for the associated diffusion generator,
3. hence exponential clustering of Euclidean correlations,
4. and, by OS reconstruction, a positive Hamiltonian mass gap.

This is the logical chain the manuscript narrative was aiming for — but it is conditional on these explicit hypotheses.

---

## C6. “Action items” (what to prove next)

If you want one lemma that unlocks many downstream upgrades, it is **C1**:
a truly clean, uniform Wilson Hessian bound in the right coordinates/norm.

If you want one numerics upgrade that could become a theorem via validated computation, it is:
- a certified $\lambda_{\min}\ge\rho_0$ on a region, using grid+Lipschitz.

Everything else becomes clearer once those two exist.

