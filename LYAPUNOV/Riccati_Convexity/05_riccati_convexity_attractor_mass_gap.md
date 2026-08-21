---
title: "Riccati Stabilisation of Convexity Eigenvalues: A Self-Sustaining Gap Mechanism (Working Note)"
date: "2025-12-28"
project: "SIMULATIONS"
---

## 1. The core slogan, made precise

> If a *convexity eigenvalue* (e.g. the smallest eigenvalue of a Hessian) obeys a **Riccati-type lower bound**
> \[
> \dot\lambda(t)\;\ge\;-\alpha\,\lambda(t)^2 + \sigma(t),\qquad \alpha>0,\quad \sigma(t)\ge \sigma_*>0,
> \]
> then it has a **positive attractor**:
> \[
> \lambda(t)\ \gtrsim\ \lambda_*:=\sqrt{\sigma_*/\alpha}\quad\text{for large }t,
> \]
> and the lower bound is **robust**: small perturbations in parameters deform \(\lambda_*\) smoothly.

This is the nonlinear “physics keeps itself gapped” mechanism: once a *positive source* survives at large scales, convexity becomes an **attractor** rather than a fine-tuned UV feature.

---

## 2. Riccati ODE: attractor and robustness

Consider the comparison ODE
\[
\dot\ell(t)=-\alpha\,\ell(t)^2+\sigma_*,\qquad \ell(0)=\ell_0\ge 0.
\]
Fixed points satisfy \(-\alpha \ell^2 + \sigma_*=0\), i.e.
\[
\ell=\pm\sqrt{\sigma_*/\alpha}.
\]
The positive fixed point \(\ell_*=\sqrt{\sigma_*/\alpha}\) is **stable** because
\[
\left.\frac{d}{d\ell}(-\alpha\ell^2+\sigma_*)\right|_{\ell=\ell_*}=-2\alpha\ell_*<0.
\]

### Explicit solution (hyperbolic tangent form)
Separating variables gives, for \(\ell_0\in[0,\ell_*)\),
\[
\ell(t)=\ell_*\,\tanh\!\Big(\alpha \ell_*\,t+\operatorname{arctanh}(\ell_0/\ell_*)\Big).
\]
In particular, if \(\ell_0=0\),
\[
\ell(t)=\ell_*\,\tanh(\alpha\ell_* t),
\]
so \(\ell(t)>0\) for all \(t>0\) and \(\ell(t)\uparrow \ell_*\) monotonically.

### Robustness to parameter drift
Let \(\lambda_*=\sqrt{\sigma_*/\alpha}\). A first-order variation yields
\[
\frac{\delta \lambda_*}{\lambda_*}=\frac12\left(\frac{\delta\sigma_*}{\sigma_*}-\frac{\delta\alpha}{\alpha}\right).
\]
So if \(\sigma_*\) stays bounded away from \(0\), the attractor does not disappear under small perturbations.

---

## 3. From PDE to ODE: how minima inherit a Riccati inequality

A typical situation is a scalar inequality on a manifold:
\[
\partial_t \lambda \;\ge\; \Delta \lambda - b\cdot \nabla\lambda -\alpha\,\lambda^2 + \sigma(t),
\]
where \(b\) is some drift field. Let
\[
m(t):=\inf_{x\in M}\lambda(t,x).
\]
At a smooth point \(x_t\) where \(\lambda(t,\cdot)\) attains its minimum (or via viscosity/approximation arguments),
\[
\nabla\lambda(t,x_t)=0,\qquad \Delta\lambda(t,x_t)\ge 0.
\]
Hence
\[
\dot m(t)\;\ge\;-\alpha\,m(t)^2+\sigma(t),
\]
so the *spatial infimum* obeys the Riccati lower bound and inherits the positive attractor.

This is the mathematical lever that turns a **local** convexity evolution equation into a **global** lower bound.

---

## 4. Where such inequalities come from: vHJ flow and Hessian reaction–diffusion

A clean “model RG/smoothing flow” is the heat equation on densities \(\rho_t\) written in Gibbs form:
\[
\rho_t(x)=Z_t^{-1}e^{-S_t(x)},\qquad \partial_t\rho_t=\Delta\rho_t.
\]
Then \(S_t\) satisfies a viscous Hamilton–Jacobi equation:
\[
\partial_t S_t=\Delta S_t-\|\nabla S_t\|^2
\]
(up to an additive time-only constant absorbed into \(S_t\)).

Let \(H_t=\nabla^2 S_t\). In Euclidean space one obtains the schematic Hessian evolution
\[
\partial_t H_t=\Delta H_t - 2(\nabla S_t\cdot\nabla)H_t -2H_t^2,
\]
i.e. a diffusion + advection + **quadratic reaction** term \(-2H^2\).

Taking the smallest eigenvalue \(\lambda_{\min}(t,x)\) of \(H_t(x)\), one expects a parabolic inequality of the form
\[
\partial_t \lambda_{\min}\ \ge\ \Delta \lambda_{\min} - 2(\nabla S_t\cdot\nabla)\lambda_{\min} - 2\lambda_{\min}^2
\]
(at least where the eigenvalue is simple; otherwise in a viscosity sense).

On curved manifolds (e.g. compact Lie groups), curvature and third-derivative terms add a **source**:
\[
\partial_t \lambda_{\min}(t,x)\ \gtrsim\ -2\lambda_{\min}(t,x)^2 + \sigma(t),
\]
where \(\sigma(t)\) depends on curvature lower bounds and control of \(\nabla^3 S_t\).

The whole “Riccati stabilisation” story is: **if** \(\sigma(t)\ge \sigma_*>0\), then \(\inf_x \lambda_{\min}(t,x)\) is forced toward \(\sqrt{\sigma_*/2}\).

---

## 5. Why this helps a mass-gap program: convexity ⇒ spectral gap ⇒ mass gap

On a Riemannian manifold, the overdamped Langevin generator for a potential \(S\) is
\[
L f=\Delta f-\langle\nabla S,\nabla f\rangle.
\]
A uniform lower bound on \( \mathrm{Ric}+\nabla^2 S \) (Bakry–Émery curvature) implies a Poincaré inequality and hence a **spectral gap** for \(-L\).

In stochastic quantisation / Osterwalder–Schrader reconstruction settings, that generator gap controls exponential decay of Euclidean-time correlations and therefore a **mass gap** (up to universal constants).

So: a *uniform* positive lower bound on the relevant Hessian eigenvalues (in physical/horizontal directions) is a direct “route” to a gap.

---

## 6. The hard part: continuum scaling and the survival of the source term

At fixed lattice spacing \(a>0\), a *Haar-measure-induced mass seed* provides an explicit positive convexity contribution.  
But that seed typically scales like \(a^2\) in naive expansions, so it **vanishes** as \(a\to 0\).

The Riccati attractor only stays positive in the continuum if the source term has an \(a\)-independent component:
\[
\sigma(t,a)=\underbrace{\sigma_{\rm geom}(t)}_{\text{independent of }a}+\underbrace{\sigma_{\rm Haar}(t,a)}_{\sim a^2}.
\]
Then
\[
\lambda_*(a)\sim \sqrt{\sigma_{\rm geom}/\alpha},
\]
so it survives the continuum limit.

A plausible candidate for \(\sigma_{\rm geom}\) is intrinsic positive curvature of compact gauge group factors together with controlled third-derivative terms along the smoothing/RG flow (this is the “geometric handoff” idea).

---

## 7. What would make this *real* (checklist)

1. **Choose a flow that *is* the RG step.** Heat-kernel convolution on \(SU(N)\) links, Wilson/gradient flow with a controlled Jacobian, etc.
2. **Prove a tensor maximum principle on the (irreducible) orbit space.** Gauge directions and reducible strata need to be treated (polarity/capacity-zero arguments are one route).
3. **Extract a uniform positive source term.** This is the crucial “σ_geom stays >0 as a→0” step.
4. **Bridge to physical mass gap.** Show that the generator gap (from Bakry–Émery) controls the transfer-matrix/continuum Hamiltonian gap for gauge-invariant observables.

---

## 8. Tiny intuition nugget

The nonlinearity \(-\alpha\lambda^2\) is *exactly* what makes the mechanism self-regulating:

- if \(\lambda\) is too small, the source \(\sigma_*\) pushes it up;
- if \(\lambda\) is too large, \(-\alpha\lambda^2\) drags it down;
- the system forgets microscopic details and flows toward \(\lambda_*\).

That “forgetfulness” is what you want when your UV lattice seed (like the Haar term) fades in the continuum.
