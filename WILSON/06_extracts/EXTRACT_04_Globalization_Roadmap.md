---
title: "From Local Horizontal Curvature to a Uniform Mass Gap: A Roadmap"
date: "2025-12-29"
---

# From local horizontal curvature to a uniform mass gap: a roadmap

## Abstract

The project establishes a **local** horizontal Bakry–Émery curvature bound near the trivial configuration
for lattice Yang–Mills. By itself, this yields local Poincaré/LSI control and a local spectral gap for the
Langevin diffusion restricted to a small-field region. The hard physics is global: the mass gap should
persist for the full theory, uniformly in volume, and in a suitable continuum limit.

This note outlines several mathematically plausible “globalization” routes—each with a concrete target lemma—
and suggests how they might plug into RG and/or quantum-group ideas to reach a genuine Yang–Mills mass-gap theorem.

The tone here is deliberately pragmatic: each route is a checklist of missing estimates.

---

## 1. What is already in hand (local engine)

Assume:

1. A finite-volume configuration manifold $M_\Lambda = G^{E(\Lambda)}$ with product Haar geometry.
2. A Gibbs measure $d\mu_\Lambda = Z_\Lambda^{-1} e^{-S_\Lambda} d\mathrm{vol}$.
3. A local, volume-independent, **horizontal** curvature bound:
\[
\mathrm{Ric}_{\mu_\Lambda}(U)\big|_{H_U} \ge \rho_{\mathrm{loc}}\,g_\Lambda
\quad\text{for }U\in B_r(U^{(0)}).
\tag{1.1}
\]
4. Gauge-invariant observables have horizontal gradients.

Then for gauge-invariant $f$ supported in $B_r(U^{(0)})$, one has local Poincaré and local LSI
with constants $O(1/\rho_{\mathrm{loc}})$.

The missing step is to control contributions from $M_\Lambda\setminus B_r$ in a way that does not degrade
with the number of edges.

---

## 2. Route A: Local $CD$ + Lyapunov drift $\Rightarrow$ global Poincaré/LSI (dimension-free)

### 2.1. The template theorem (Cattiaux--Guillin style)

A standard strategy for non-uniformly convex measures is:

- Prove a **local** functional inequality on a “good set” $A$ (here, $A=B_r(U^{(0)})$).
- Construct a Lyapunov function $W\ge 1$ such that
\[
L_\Lambda W \le -\lambda W + b\,\mathbf 1_A
\tag{2.1}
\]
for constants $\lambda,b$ independent of $\Lambda$.
- Conclude a **global** Poincaré inequality (and often an LSI) with constants depending only on
$\rho_{\mathrm{loc}},\lambda,b$ and the local constants.

### 2.2. What Lyapunov function might work for lattice Yang–Mills?

The natural candidate is an exponential in the action:
\[
W(U) = \exp(\alpha\,S_\Lambda(U))
\quad\text{or}\quad
W(U)=\exp(\alpha\,\mathrm{dist}(U,U^{(0)})^2).
\tag{2.2}
\]

**Key sub-problem:** compute $L_\Lambda W$ and bound it uniformly in volume.

Because $M_\Lambda$ is compact, one always has some Lyapunov function,
but uniformity in $\Lambda$ is the crux. The challenge is that $S_\Lambda$ is extensive:
$S_\Lambda$ scales like $|P(\Lambda)|$.

A possible fix is to use a *normalized* action density, e.g.
\[
\bar S_\Lambda = \frac{1}{|P(\Lambda)|} S_\Lambda,
\tag{2.3}
\]
and attempt a drift estimate for $W=\exp(\alpha |P|\,\bar S)$ that keeps $\lambda$ volume-free.

### 2.3. What would success look like?

A successful proof here would yield:

- A global Poincaré inequality for gauge-invariant observables with a constant independent of $\Lambda$.
- Hence a uniform spectral gap for the Langevin generator in $L^2(\mu_\Lambda)$.
- A quantitative mixing time bound that is volume-free in the “small-field phase”.

This does **not** yet equal the physical mass gap, but it supplies a rigorous, robust analytic handle.

---

## 3. Route B: Uniform gap from product Haar + local interaction perturbations (Zegarlinski / Dobrushin)

The lattice Yang–Mills Gibbs measure is a finite-range (nearest-neighbor in plaquettes) perturbation
of product Haar. Product Haar has a dimension-free spectral gap.

A well-known high-dimensional strategy is:

1. Start from a reference measure $\mu_0$ with known uniform spectral gap (here, product Haar).
2. Treat $e^{-S_W}$ as an interaction.
3. Use a **block dynamics / martingale decomposition** to show the interacting measure has a uniform gap
whenever an appropriate influence matrix is contractive (a Dobrushin-type condition).

**Key sub-problem:** produce an explicit, volume-independent bound on the influence of changing one edge/link
on the conditional measure of a nearby block.

This is plausible at strong coupling (small $\beta$), but hard at weak coupling.

---

## 4. Route C: Two-phase interpolation (strong $\beta\to 0$ to weak $\beta\to\infty$)

Because:

- at strong coupling $\beta\approx 0$, $\mu_\Lambda$ is close to Haar (uniform gap),
- at weak coupling $\beta\gg 1$, the measure concentrates near the identity (local curvature engine),

one can dream of proving that the spectral gap stays bounded away from $0$ along $\beta\in[0,\infty)$.

A practical version:

- Prove uniform gap for $\beta\le \beta_0$ by perturbation from Haar.
- Prove uniform gap for $\beta\ge \beta_1$ by localization in $B_r(U^{(0)})$ plus a concentration estimate
showing $\mu_\Lambda(B_r)$ is bounded below uniformly in volume.
- Bridge the compact interval $[\beta_0,\beta_1]$ by continuity / compactness arguments (hard part: show the
gap cannot collapse with volume inside the bridge interval).

---

## 5. Route D: RG + emergent quantum-group/TQFT structure (speculative but tempting)

This is where the curated quantum-group and TQFT material becomes conceptually relevant.

Working hypothesis (a *theory*, not a theorem):

- Under RG, the effective IR description of confining $4$d Yang–Mills becomes a gapped topological phase,
often modeled by a quantum group at a root of unity or by a modular tensor category.

If true, then:

- the IR transfer matrix would have a gap protected by topological data,
- the deformation parameter $q$ (or truncation level $k$) would encode an emergent mass scale.

**Concrete task:** connect the curvature–dimension gap for the Langevin generator to a gap for the transfer matrix
at a coarse RG scale, then use an RG monotonicity statement to push it to the continuum.

This is ambitious, but it suggests a bridge:

> Bakry–Émery curvature controls **stochastic quantization**.  
> Quantum-group/TQFT data controls **topological stability of IR spectra**.  
> RG is the missing translator.

---

## 6. A sanity check: why “horizontal” is not just a technicality

Gauge symmetry creates flat directions (pure gauge). If one demands global convexity in all directions,
one is fighting gauge redundancy rather than physics.

The horizontal approach is the clean fix:

- gauge-invariant observables only “see” horizontal directions,
- curvature bounds only need to hold horizontally,
- the resulting inequalities are physically meaningful (they control gauge-invariant correlations).

This turns a would-be obstruction into a feature.

---

## 7. Minimal next lemmas to shoot for

1. **Uniform concentration**: show $\inf_\Lambda \mu_\Lambda(B_r(U^{(0)}))>0$ in a suitable regime (e.g. large $\beta$).
2. **Volume-free drift**: build a Lyapunov function satisfying (2.1) with constants independent of $\Lambda$.
3. **Uniform block Poincaré**: prove a block inequality stable under local interactions.
4. **Transfer-matrix bridge**: relate the Langevin (stochastic) gap to a Hamiltonian/transfer gap.

Any one of these would materially move the program from “local engine” to “global theorem”.
