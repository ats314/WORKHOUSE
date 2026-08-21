# Localized curvature, capacity, and RG-friendly convexity bookkeeping

> **Status note.** This document extracts a cluster of “repair ideas” that show up repeatedly in the project: when global convexity fails, try to prove **localized** convexity where the measure actually lives, and neutralize the rest via **capacity** or perturbation arguments.

## 1. The main obstruction diagnosed in the project

At finite lattice spacing \(a>0\), one can sometimes get a coercive lower bound on the Hessian of an effective action on the horizontal (gauge-fixed) subspace:
\[
\langle A, H_H(U) A\rangle \;\ge\; m(a,\beta)\,\|A\|^2,
\qquad
m(a,\beta)=c_0 a^2 g^2 - \beta C_V.
\]

The project explicitly notes the fatal scaling issue along the asymptotically free trajectory:
- the Haar/entropic convexity contribution behaves like \(a^2 g^2\to 0\) as \(a\to 0\),
- while the Wilson part scales with \(\beta\to\infty\),
so the strong-coupling window \(0<\beta<\beta_c(a)\) cannot contain the continuum \(\beta(a)\), forcing a sign change in \(m(a,\beta(a))\) before the continuum is reached.

So: **global uniform convexity dies before the continuum limit**.

---

## 2. The “measure-weighted curvature” idea (a genuinely nonstandard move)

Instead of defining curvature by a global infimum over configuration space, the project proposes an RG-adapted notion:

\[
\sigma_{\mathrm{eff}}(t)
:= \sigma_{\mathrm{geom}}(t)+\sigma_{\mathrm{anom}}(t)+\sigma_{\mathrm{Haar}}(t)+\sigma_{\mathrm{corr}}(t),
\]
and the core question is whether one can prove a positive lower bound
\[
\mathrm{Ric}+\nabla^2 S_t \;\ge\; \sigma_{\mathrm{eff}}^\* > 0
\]
**on the region where the RG-evolved measure \(\mu_t\) is concentrated**, while the complement is controlled by:
- exponentially small \(\mu_t\)-mass, *or*
- small Dirichlet capacity.

This is precisely the sort of condition that could make Bakry–Émery / log-Sobolev arguments viable even when the global curvature bound \(\rho_\*(a)\) runs to \(-\infty\).

---

## 3. Capacity as a “proof lubricant”: polar sets don’t matter to Dirichlet forms

The project contains a particularly clean idea:

> The set of *reducible* gauge-field configurations (where the stabilizer is larger than the center) is **polar** for the relevant Dirichlet form, hence negligible for Poincaré/log-Sobolev inequalities and spectral gaps.

Interpretation:
- Some “bad” subsets are so thin (in the capacity sense) that diffusion/Dirichlet-form arguments literally do not see them.
- This suggests a strategy: identify other curvature-bad regions whose capacity is small enough to be negligible.

That’s more subtle than “small probability”: a set can have small measure but still large capacity, and vice versa. Capacity is the right tool if the goal is to control functional inequalities.

---

## 4. Coarse-graining and Schur complements: convexity under marginalization

A recurring technical need is to understand what happens to convexity when integrating out UV variables.

If a block-decomposed Hessian has the form
\[
\nabla^2 S(x,y)
=
\begin{pmatrix}
A & B\\
B^\top & C
\end{pmatrix},
\]
then for the marginal (effective) action
\[
\bar S(x) := -\log\int e^{-S(x,y)}\,dy,
\]
one expects a Schur-complement style lower bound
\[
\nabla_x^2 \bar S(x)
\;\succeq\;
A - B\,C^{-1}B^\top,
\]
so convexity degrades by an amount controlled by the coupling block \(B\) and the UV convexity \(C\).

The project records a scale-propagation inequality of the same flavor:
\[
\kappa(2L)\;\ge\;c_{\mathrm{geom}}\big(\kappa_0-\varepsilon_L\big),
\]
with an explicit (toy) estimate
\[
\varepsilon_L \;\le\; \frac{M^2}{\gamma}
\]
under bounds \(A\succeq \alpha\), \(C\succeq \gamma\), \(\|B\|\le M\), and \(\kappa_0\equiv\alpha\).

This is *exactly* the sort of lemma you want if you’re trying to track curvature/LSI constants through a multiscale RG scheme.

---

## 5. How this ties back to the “defect gas” picture

Combine the ideas:

- **Good region:** where the local curvature bound is positive; use Bakry–Émery to get local Poincaré/LSI.
- **Bad region:** where curvature becomes negative, but (hope) it has either
  - exponentially small measure, or
  - small capacity, or
  - polymer/defect structure with controllable interactions.

Then attempt to “upgrade” the good-region inequalities to global ones via:
- perturbative stability (Holley–Stroock), and/or
- localization + capacity estimates.

This is the project’s most coherent *bridge* from the finite-cutoff convexity mechanism to a plausible continuum strategy.

---

## Provenance pointers (project internal)
This note distills:
- the scaling argument that \(m(a,\beta(a))\) must cross zero before \(a\to 0\),
- the proposal to define \(\sigma_{\mathrm{eff}}(t)\) on the support of \(\mu_t\),
- the polarity/capacity claim for reducible configurations,
- Schur-complement style convexity-under-marginalization bookkeeping,
- the scale-propagation inequality for \(\kappa(L)\mapsto \kappa(2L)\).

