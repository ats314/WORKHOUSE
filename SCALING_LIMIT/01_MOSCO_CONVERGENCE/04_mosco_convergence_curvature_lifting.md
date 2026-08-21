# Mosco Convergence, Curvature Stability, and Continuum Lifting

*Project extraction (generated 2025-12-29).*

## 0. Purpose

This document distills the “analysis backbone” of the project:

- define lattice Dirichlet forms $\mathcal{E}_a$ for gauge theory,
- take $a\to 0$ via **Mosco convergence**,
- show that a uniform Bakry–Émery curvature bound survives the limit,
- conclude that continuum functional inequalities (LSI / Poincaré) survive too.

The novelty is not in Mosco convergence itself, but in welding it to the curvature-based mass mechanism.

---

## 1. Setup: Dirichlet forms

For each lattice spacing $a$:

- configuration space $\mathcal{X}_a = G^{E(\Lambda_a)}$ (after gauge fixing if desired),
- measure $\mu_a$,
- Dirichlet form
  \[
  \mathcal{E}_a(F) := \int_{\mathcal{X}_a} |\nabla_a F|^2\,d\mu_a.
  \]

In the limit:

- a measure $\mu$ on an infinite-dimensional distribution space (e.g. $H^{-s}$),
- a Dirichlet form
  \[
  \mathcal{E}(F) := \int |\nabla F|^2\,d\mu.
  \]

---

## 2. Mosco convergence (the two inequalities)

We say $\mathcal{E}_a\to\mathcal{E}$ in the Mosco sense if:

1. **Liminf inequality (lower semicontinuity):** if $F_a\to F$ strongly in $L^2(\mu)$,
   \[
   \mathcal{E}(F)\le \liminf_{a\to 0}\mathcal{E}_a(F_a).
   \]

2. **Recovery sequence:** for every $F$ there exists $F_a\to F$ strongly with
   \[
   \mathcal{E}(F)=\lim_{a\to 0}\mathcal{E}_a(F_a).
   \]

In practice, recovery sequences are built from **cylindrical functions** (finite sets of holonomies / loops).

---

## 3. Stability of Bakry–Émery curvature under Mosco limits

Assume a uniform lattice curvature condition of the form
\[
\Gamma_{2,a}(F)\ge \rho_0\,\Gamma_a(F),
\]
equivalently (for diffusion semigroups) the gradient contraction
\[
|\nabla_a P_t^a F|^2 \le e^{-2\rho_0 t} P_t^a(|\nabla_a F|^2).
\]

Mosco convergence implies strong semigroup convergence $P_t^a\to P_t$ (Trotter–Kato for forms).

With (i) liminf control of gradients and (ii) recovery sequences, the contraction passes to the limit:
\[
|\nabla P_t F|^2 \le e^{-2\rho_0 t} P_t(|\nabla F|^2).
\]

Differentiating at $t=0$ yields the continuum curvature inequality
\[
\Gamma_2(F)\ge \rho_0\,\Gamma(F).
\]

---

## 4. Two essential “measure-theory” supports

### 4.1 Tightness (existence of subsequential limits)

Uniform LSI implies Gaussian concentration via Herbst, which can be converted into tightness in $H^{-s}$ using compact Sobolev embeddings.

This gives subsequential weak convergence $\mu_{a_k}\Rightarrow \mu$.

### 4.2 Polarity of singular sets (domain stability)

Gauge theory configuration spaces have singular strata (reducible connections / non-free gauge orbits).  

The repository uses a capacity argument:

- the singular set has zero capacity under a Gaussian reference,
- the Yang–Mills measure is a bounded density perturbation of that reference (in the relevant local sense),
- hence the singular set remains polar (capacity $0$).

This protects the Dirichlet-form domain and prevents “hidden boundary terms” in integration by parts.

---

## 5. Infrared decoupling by locality (why topology doesn’t kill the gap)

A separate but important analytic point:

- the Hessian / second variation of a local lattice action is exactly finite range,
- so variations supported in a ball and variations far away have **zero** cross-term for small enough $a$.

Thus global topology (instanton sectors, winding modes, etc.) cannot destroy the **local** spectral gap for local observables once you take the continuum limit through local balls.

---

## 6. What’s “exciting” here

If the SAFE-region curvature constant $\rho_0$ can be made uniform in $a$ (and volume) on local observables, Mosco stability gives a clean, modular way to export that constant to the continuum — without re-proving PDE estimates in infinite dimensions from scratch.

That’s a rare kind of leverage in QFT: do the hard thing once (lattice curvature), then let functional analysis carry it home.

