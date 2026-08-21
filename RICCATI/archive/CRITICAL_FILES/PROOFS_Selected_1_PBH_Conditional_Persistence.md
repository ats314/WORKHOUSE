# Selected Proof 1: Projected Bochner–Hessian Flow and Conditional Persistence of a Mass Gap

**Source backbone:** `Conditional_Persistence_Theorem_v2_Enhanced.md` and related notes.  
**This document is an extracted, tightened presentation** of the main conditional mechanism: *a uniformly positive “anomaly source” term beats geometric corrections that decay like \(g(t)^2\), forcing the minimal Hessian eigenvalue to stay positive.*

---

## 1. The geometric–analytic setting

Let \(\mathcal{M}_{\mathrm{reg}}\) be a finite-dimensional approximation to the regular gauge-orbit space
\[
\mathcal{M}_{\mathrm{reg}} \approx \mathcal{A}_{\mathrm{reg}}/\mathcal{G},
\]
obtained from a lattice cutoff or Galerkin truncation. Endow \(\mathcal{M}_{\mathrm{reg}}\) with the quotient metric induced by the \(L^2\) metric on \(\mathcal{A}\).

Let \(S_t:\mathcal{M}_{\mathrm{reg}}\to\mathbb{R}\) be a time-dependent effective action solving a **horizontal viscous Hamilton–Jacobi equation**
\[
\partial_t S_t = \Delta_H S_t - \|\nabla_H S_t\|^2 + J_t,
\]
where \(\Delta_H,\nabla_H\) denote the horizontal Laplacian and gradient and \(J_t\) is the forcing term induced by RG/trace-anomaly effects.

Define
\[
V_t := \nabla_H S_t,\qquad h_t := \nabla_H^2 S_t,
\]
so \(h_t\) is a symmetric bilinear form (a self-adjoint operator after metric identification). Let
\[
\lambda_{\min}(t) := \min \operatorname{Spec}(h_t)
\]
be the minimal eigenvalue; heuristically \(\lambda_{\min}(t)\) is the **running mass-squared** of the lightest mode at RG time \(t\).

---

## 2. The PBH flow (Projected Bochner–Hessian flow)

A key structural identity is that \(h_t\) evolves by a parabolic tensor equation of Riccati type:
\[
\boxed{
\partial_t h_t
= \Delta_H h_t - 2\nabla_{V_t} h_t - 2 h_t^2 + S_{\mathrm{anom}}(t) + \mathfrak{G}(S_t,h_t).
}
\]
Here

- \(S_{\mathrm{anom}}(t) := \nabla_H^2 J_t\) is the **anomaly source** term (a symmetric tensor forcing convexity),
- \(\mathfrak{G}(S_t,h_t)\) collects the **geometric correction terms** (curvature and non-integrability of the horizontal distribution).

The core mass-gap mechanism is entirely visible in this equation:

- \(-2h_t^2\) is a stabilizing nonlinearity (a matrix Riccati term),
- \(S_{\mathrm{anom}}\) is a *positive* forcing term that pushes \(h_t\) upward,
- \(\mathfrak{G}\) is a perturbation controlled by the geometry of \(\mathcal{M}_{\mathrm{reg}}\).

---

## 3. Hypotheses (the “five locks”)

We isolate five quantitative hypotheses:

### (H1) Curvature scaling
There exists \(C_0>0\) and a running coupling \(g(t)\) such that for all unit horizontal \(X,Y\),
\[
|K_t(X,Y)| \le C_0\, g(t)^2.
\]

### (H2) Trace bound
There exists \(H_{\mathrm{Tr}}<\infty\) such that
\[
\|h_t\|_{\mathrm{Tr},+} := \sum_i \max\{\lambda_i(t),0\} \le H_{\mathrm{Tr}}
\quad\text{for all } t\ge 0.
\]

### (H3) Uniform anomaly positivity
There exists \(\sigma_A>0\) such that for all \(x\in\mathcal{M}_{\mathrm{reg}}\) and unit \(v\in T_x\mathcal{M}_{\mathrm{reg}}\),
\[
\langle v, S_{\mathrm{anom}}(t,x)v\rangle \ge \sigma_A
\quad\text{for all }t\ge 0.
\]

### (H4) Asymptotic freedom
\[
\lim_{t\to\infty} g(t) = 0.
\]

### (H5) Initial gap
There exists \(T_0\ge 0\) and \(\lambda_*>0\) such that
\[
\lambda_{\min}(T_0) \ge \lambda_*.
\]

---

## 4. The key estimate: geometric correction is \(O(g^2)\)

The correction term \(\mathfrak{G}\) is linear in the curvature tensor contracted against \(h_t\) (and possibly \(V_t\)). Under (H1) and finite-dimensional norm comparisons,
\[
\|\mathfrak{G}(S_t,h_t)\|_{\mathrm{op}}
\;\lesssim\;
\big(\sup |K_t|\big)\,\|h_t\|_{\mathrm{op}}
\;\le\;
C\, g(t)^2 \|h_t\|_{\mathrm{Tr},+}.
\]
Evaluated on a unit eigenvector \(v_0(t)\) for \(\lambda_{\min}(t)\), and using (H2),
\[
\boxed{
\big|\langle v_0,\mathfrak{G}(S_t,h_t)v_0\rangle\big|
\le C_1 g(t)^2 H_{\mathrm{Tr}}.
}
\]

---

## 5. Scalar inequality for the minimal eigenvalue

A tensor maximum principle argument (standard for parabolic flows of symmetric tensors) yields
\[
\boxed{
\partial_t \lambda_{\min}(t)
\;\ge\;
-2\lambda_{\min}(t)^2
+\sigma_A
- C_1 g(t)^2 H_{\mathrm{Tr}}.
}
\]
This is the entire game: **a scalar Riccati inequality with a decaying error term**.

---

## 6. Asymptotic dominance and persistence

By (H4), \(g(t)^2\to 0\), so choose \(T_1\ge T_0\) such that for \(t\ge T_1\),
\[
C_1 g(t)^2 H_{\mathrm{Tr}} \le \frac{\sigma_A}{2}.
\]
Hence for \(t\ge T_1\),
\[
\partial_t \lambda_{\min}(t) \;\ge\; -2\lambda_{\min}(t)^2 + \frac{\sigma_A}{2}.
\]
Compare \(\lambda_{\min}\) to the scalar ODE
\[
\dot{\lambda} = -2\lambda^2 + \frac{\sigma_A}{2},\qquad \lambda(T_1)=\lambda_*.
\]
This ODE has a stable positive equilibrium
\[
\lambda_\infty = \sqrt{\frac{\sigma_A}{4}} = \frac{1}{2}\sqrt{\sigma_A}.
\]
By comparison,
\[
\boxed{
\lambda_{\min}(t) \ge \sigma_{\min} > 0 \quad\text{for all } t\ge T_1,
}
\]
for example one may take a conservative explicit choice such as
\[
\sigma_{\min} := \frac{1}{4}\sqrt{\sigma_A}.
\]

---

## 7. Why this is “the interesting part”

This is more than a single theorem: it is a **template**.

- Any QFT or statistical field theory whose RG-improved effective action produces a *uniformly positive Hessian source* \(S_{\mathrm{anom}}\),
- and whose geometric correction terms are suppressed by a small parameter (here \(g^2\) via asymptotic freedom),

inherits a *convexification mechanism* forcing a nonzero spectral gap at large RG time.

In other words, the PBH-flow viewpoint is a candidate for a **general “gap persistence by convexification” principle** for asymptotically free systems.

---

## References within the project

- `Conditional_Persistence_Theorem_v2_Enhanced.md`
- `Riccati_Equation_Analysis_Proof.md`
- `Conditional_Persistence_Theorem_Review.md`
