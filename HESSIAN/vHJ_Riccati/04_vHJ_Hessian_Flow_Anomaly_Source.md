# Viscous Hamilton–Jacobi \(\&\) Hessian Riccati Flow: How Convexity Can Die (and How an “Anomaly Source” Could Save It)

## 0. Context

If you encode a probability density as \(\rho_t\propto e^{-S_t}\), then many smoothing flows become nonlinear PDEs for the effective action \(S_t\). The Hessian \(H_t=\nabla^2 S_t\) typically satisfies a **reaction–diffusion–Riccati** equation with a destabilizing \(-2H_t^2\) term.

This is a natural way convexity can *shrink* as you coarse‑grain.

The exciting speculative move in this project is:

> identify a **positive source term** (geometric + measure + anomaly) that counteracts the Riccati decay and stabilizes \(H_t\succeq \rho I\).

---

## 1. From heat/Fokker–Planck to viscous Hamilton–Jacobi (vHJ)

### 1.1 Pure heat equation on \(\mathbb{R}^n\)

Let \(\rho_t\) solve
\[
  \partial_t\rho_t=\Delta \rho_t.
\]
Write \(\rho_t = Z_t^{-1}e^{-S_t}\). Then
\[
  \partial_t \rho_t
  =-(\partial_t S_t + \partial_t\log Z_t)\rho_t,
\]
and
\[
  \Delta \rho_t
  = \rho_t\big(-\Delta S_t+\|\nabla S_t\|^2\big).
\]
Equating and absorbing \(\partial_t\log Z_t\) into an additive constant in \(S_t\) gives the vHJ equation:
\[
  \boxed{\ \partial_t S_t = \Delta S_t - \|\nabla S_t\|^2\ }.
\]

### 1.2 With a drift (general Fokker–Planck form)

If instead
\[
  \partial_t \rho = \Delta \rho + \nabla\cdot(b\,\rho),
\]
then the same calculation yields
\[
  \partial_t S = \Delta S - \|\nabla S\|^2\ -\ b\cdot\nabla S\ +\ \nabla\cdot b
\]
(up to an additive time function).

---

## 2. Hessian evolution: matrix reaction–diffusion–Riccati

Let \(H_t=\nabla^2 S_t\) with components \(H_{ij}=\partial_i\partial_j S_t\).  
Differentiate vHJ twice. In Euclidean space one obtains schematically:
\[
  \boxed{\ \partial_t H
  = \Delta H\ -\ 2(\nabla S\cdot\nabla)H\ -\ 2H^2\ +\ \text{(drift/geometry terms)}\ }.
\]

- \(\Delta H\) diffuses curvature.
- the transport term \(-2(\nabla S\cdot\nabla)H\) is advection along characteristics.
- the Riccati term \(-2H^2\) is *curvature‑destroying*: even if \(H\succeq 0\) initially, this term tends to push eigenvalues downward.

On a manifold (or a gauge quotient) additional terms appear from curvature (Ricci), from the Levi‑Civita connection, and from projecting onto horizontal directions.

---

## 3. The smallest eigenvalue inequality

Let \(\lambda(t,x)\) denote the smallest eigenvalue of \(H(t,x)\) (on the regular stratum). Under suitable smoothness, one can derive a scalar inequality of the form
\[
  \partial_t \lambda
  \;\ge\;
  \Delta \lambda\ -\ 2\nabla S\cdot\nabla \lambda\ -\ 2\lambda^2\ +\ \sigma_{\mathrm{eff}}(t,x),
\]
where \(\sigma_{\mathrm{eff}}\) collects the “good” source contributions (geometry, measure terms, anomalies, etc.).

Even in a toy ODE model (ignore diffusion/transport), the inequality becomes
\[
  \lambda'(t)\ \gtrsim\ -2\lambda(t)^2 + \sigma_{\mathrm{eff}}(t).
\]

---

## 4. Why convexity can die without a source

If \(\sigma_{\mathrm{eff}}\equiv 0\), the ODE
\[
  \lambda'=-2\lambda^2
\]
has solutions \(\lambda(t)=\frac{1}{2t+C}\), so curvature decays like \(1/t\).

This is the “RG flattening” intuition: as you smooth / integrate out degrees of freedom, convexity weakens unless something constantly injects curvature.

---

## 5. How a positive source stabilizes curvature

Assume \(\sigma_{\mathrm{eff}}(t,x)\ge \sigma_0>0\) uniformly for \(t\ge t_0\). Then the ODE comparison
\[
  \lambda' \ge -2\lambda^2 + \sigma_0
\]
has a positive equilibrium \(\lambda_*=\sqrt{\sigma_0/2}\).  
Solutions are driven toward \(\lambda_*\) from below, yielding a uniform lower bound after some time.

This is the conceptual payload:

> **If you can show \(\sigma_{\mathrm{eff}}>0\) beyond some UV scale, you can trap the Hessian eigenvalues away from zero.**

---

## 6. Where could \(\sigma_{\mathrm{eff}}\) come from in Yang–Mills?

This project isolates several candidate contributions:

1. **Measure geometry (finite cutoff):** the Haar Jacobian produces a local quadratic term, a direct curvature source at the lattice scale.
2. **Manifold / orbit‑space geometry:** Ricci curvature terms can contribute positively (at least on compact group manifolds / nice quotients).
3. **Quantum trace anomaly (continuum):** the program proposes a link between an “anomaly source”
   \(\sigma_{\mathrm{anomaly}}\) and the Yang–Mills \(\beta\)-function, with the heuristic sign
   \[
     \sigma_{\mathrm{anomaly}}(t)\ \propto\ \frac{\beta(g(t))^2}{g(t)^2}\ \ge\ 0,
   \]
   and strictly \(>0\) if \(\beta(g)\neq 0\).

The third point is ambitious; it is framed as a “high‑risk / high‑reward” prong.

---

## 7. Stratified maximum principle: why polarity is needed

On the gauge quotient, the PDE for \(\lambda(t,x)\) lives on the **regular stratum** \(\mathcal{M}_{\mathrm{reg}}\) and the singular set \(\Sigma\) is not a smooth boundary.

If \(\Sigma\) is **polar** for the diffusion driving \(L\), then \(\Sigma\) is too thin to break positivity. One expects:

> If \(\lambda(0,\cdot)\ge 0\) almost everywhere and \(\sigma_{\mathrm{eff}}\ge 0\), then \(\lambda(t,\cdot)\ge 0\) for \(t>0\).

This is the analytic bridge between:
- polarity / capacity (potential theory),
- and the curvature‑flow / Hessian‑Riccati layer.

---

## 8. Concrete next steps

1. Derive the exact matrix PDE for \(H_t\) on the **horizontal distribution** of \(\mathcal{A}/\mathcal{G}\).
2. Prove a **weak maximum principle** for \(\lambda_{\min}(H_t)\) under polarity hypotheses.
3. Identify and rigorously bound the candidate \(\sigma_{\mathrm{eff}}\) contributions:
   - measure (Haar / Jacobian),
   - geometry (Ricci),
   - anomaly (requires nonperturbative control of \(\beta\)).

