# Riccati Flow, Convexity Decay, and What Could Sustain a Mass Scale

This note is half “solid derivation” and half “working theory”.

- The **solid** part: under heat-flow coarse-graining, the effective action \(S_t\) satisfies a viscous Hamilton–Jacobi equation, and its Hessian obeys a **matrix Riccati-type evolution**. In the Gaussian case, convexity decays like \(1/t\).
- The **working theory** part: any continuum mass gap mechanism in this framework must introduce a **positive source term** (geometric, entropic, or anomalous) that stabilizes the Riccati flow at a nonzero curvature floor.

---

## 1. Heat-flow coarse-graining \(\Rightarrow\) viscous Hamilton–Jacobi

Let \(\rho_t(x)\) solve the heat equation on \(\mathbb R^d\):
\[
\partial_t \rho_t = \Delta \rho_t,
\qquad 
\rho_t = e^{-S_t}.
\]
(Any time-dependent normalization can be absorbed into \(S_t\) as an additive constant.)

Then a direct substitution gives the **viscous Hamilton–Jacobi** equation:
\[
\partial_t S_t = \Delta S_t - \|\nabla S_t\|^2.
\]

This equation is the clean analytic avatar of “smoothing by convolution with a Gaussian kernel”.

---

## 2. Hessian evolution: a matrix Riccati structure

Let \(H_t(x):=\nabla^2 S_t(x)\).
Differentiate the vHJ equation twice. One convenient form is:
\[
\partial_t H_t
=
\Delta H_t
-2(\nabla S_t\cdot\nabla)H_t
-2H_t^2
\;+\; \mathcal R_t,
\]
where \(\mathcal R_t\) is a remainder built from third derivatives (it vanishes identically in the purely quadratic/Gaussian case).

The important structural term is the reaction term \(-2H_t^2\): it is exactly the matrix Riccati nonlinearity.

---

## 3. The Gaussian calibration: convexity decays like \(1/t\)

Take an initial quadratic action
\[
S_0(x)=\frac12 x^\top A_0 x,\qquad A_0\succ 0.
\]
Heat-flow convolution keeps Gaussians Gaussian, and the Hessian evolves exactly by
\[
\frac{d}{dt}H_t = -2H_t^2,
\]
so eigenvalues satisfy the scalar ODE
\[
\dot\lambda = -2\lambda^2,\qquad \lambda(t)=\frac{\lambda(0)}{1+2t\lambda(0)}.
\]

In particular,
\[
\lambda_{\min}(t)\sim \frac{1}{2t}\quad (t\to\infty).
\]

**Conclusion:** under pure heat-flow coarse-graining on flat space, convexity **always decays**.
So if you want a nonzero mass scale in the IR, something must counteract that decay.

---

## 4. The “sustainer” requirement: you need a positive source term

A caricature of what you want is an inequality for the minimum eigenvalue \(\lambda(t)\):
\[
\dot\lambda \;\gtrsim\; -2\lambda^2 + \sigma_*,
\qquad \sigma_*>0.
\]
The ODE \(\dot\ell=-2\ell^2+\sigma_*\) has a stable fixed point
\[
\ell_*=\sqrt{\sigma_*/2},
\]
which is exactly a “mass-gap-from-stable-curvature-floor” mechanism.

So the continuum program becomes very crisp:

> Find a mechanism producing a \(\sigma_*>0\) term that does not vanish as \(a\to 0\).

---

## 5. Plausible sources of \(\sigma_*\) working hypotheses

### 5.1. Geometric source manifold curvature
On a curved configuration manifold, Bochner-type formulas introduce Ricci curvature terms into the \(\Gamma_2\) calculus.
In a Hessian-evolution picture, this can look like an additive positive contribution to the lower curvature bound.

This is the cleanest mathematical source, but it has a known problem:
the *global* curvature infimum still gets killed by the Wilson negative directions (RECOMMENDED_02).
So geometry alone is unlikely to be sufficient without localization.

### 5.2. Entropic source boundary / domain restriction
If the effective measure is supported in a convex (or effectively convex) domain \(\mathcal F\) (e.g., a gauge-fixed fundamental region), then the marginalization can pick up an entropic quadratic term:
\[
V_{\mathrm{eff}}(y)=-\log\mathrm{Vol}(\mathcal F\cap P^{-1}(y))+\cdots
\]
A robust quadratic lower bound on this entropic term is *exactly* Conjecture 3.1 in **RECOMMENDED_04**.

In Riccati-flow language: the domain constraint acts like a reflecting/entropic forcing that can supply \(\sigma_*\).

### 5.3. Anomaly source trace anomaly as curvature injection
This is the boldest hypothesis: in Yang–Mills, the trace anomaly produces a physical scale \(\Lambda_{\mathrm{QCD}}\).
One can speculate that, in a coarse-graining PDE, that scale appears as an effective positive source term in curvature evolution.

To be clear: this is not a theorem; it’s a programmatic translation:

- “Anomaly generates a scale”  
  \(\leadsto\)  
  “Hessian lower bound stabilizes at a nonzero fixed point”.

The missing step is to turn the anomaly into an inequality of the form \(\sigma_*>0\).

---

## 6. Discrete cousin: why the block RG inequality matters here

The continuous Riccati story is slippery in a true interacting field theory.

The block convexity inequality (RECOMMENDED_03) is the discrete, rigorous cousin: it shows that *if* you have a spark \(\rho_k>0\) and cross-couplings \(M_k\) are controlled, then
\[
\rho_{k+1}\ge \rho_k-\frac{M_k^2}{\rho_k}.
\]

In other words: the block inequality gives a concrete path to a sustained curvature floor *without* fully solving the Riccati PDE.

So one practical strategy is:

1. Prove/observe a spark \(m_*^2\) in a gauge-fixed IR effective potential.
2. Use the block inequality iteratively to propagate a positive lower bound through successive RG steps.
3. Combine with localization to handle the “bad set” where the inequalities fail.

---

## 7. Why this is recommended despite the speculative part

Because it cleanly separates:

- what the **flow** does to convexity (it decays it), from
- what a **mass gap mechanism** must add (a source), from
- how to approximate the story rigorously (block RG inequalities).

It turns “RG stability” from a vibe into a concrete inequality problem.
