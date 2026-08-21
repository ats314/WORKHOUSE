# Viscous Hamilton–Jacobi coarse-graining and Riccati curvature dynamics

## 0. Why this document exists

If you want a curvature-based mass-gap method, you need a story for **how curvature behaves under coarse-graining**.

This project uses a specific, mathematically crisp model: start from a density \(\rho_t\) evolving under heat flow, write \(\rho_t=e^{-S_t}\), and analyze the resulting PDE for \(S_t\). This yields an explicit PDE for the Hessian \(H_t=\nabla^2 S_t\) with a **Riccati term** \(-2H_t^2\) that tries to kill curvature.

The key strategic point is simple:

- Without a positive source, curvature tends to decay (often like \(1/t\)).
- With a persistent positive source (a “mass-like” \(\nabla^2 J_t\ge c_0 I\)), curvature can stabilize.

This is the correct mathematical shape of the problem even if Yang–Mills ultimately needs a more sophisticated RG.

---

## 1. vHJ equation from heat flow (exact finite-dimensional derivation)

Let \(\rho_t(x)>0\) solve the heat equation on \(\mathbb{R}^n\):
\[
\partial_t \rho_t = \Delta \rho_t.
\]
Write \(\rho_t = Z_t^{-1}e^{-S_t}\). A direct computation gives
\[
\partial_t S_t = \Delta S_t - |\nabla S_t|^2 - \partial_t(\log Z_t).
\]
Dropping the purely time-dependent constant \(-\partial_t\log Z_t\) (it does not affect gradients/Hessians), we obtain the **viscous Hamilton–Jacobi equation**
\[
\boxed{\;\partial_t S_t = \Delta S_t - |\nabla S_t|^2.\;}
\]

---

## 2. Gradient and Hessian flow (exact identities)

Let \(b=\nabla S_t\) and \(H=\nabla^2 S_t\). Differentiating the vHJ equation yields:

- **Gradient flow**
\[
\partial_t b = \Delta b - 2 H b.
\]

- **Hessian flow** (componentwise Laplacian and transport)
\[
\boxed{\;\partial_t H = \Delta H - 2(b\cdot\nabla)H - 2H^2.\;}
\]

This is a reaction–diffusion–transport equation with a matrix Riccati reaction term.

### Adding a source
If instead
\[
\partial_t S_t = \Delta S_t - |\nabla S_t|^2 + J_t(x),
\]
then
\[
\boxed{\;\partial_t H = \Delta H - 2(b\cdot\nabla)H - 2H^2 + \nabla^2 J_t.\;}
\]

Interpretation: \(\nabla^2J_t\) is the only place a *persistent* curvature source can live.

---

## 3. Riccati control for the smallest Hessian eigenvalue

Let \(\lambda_{\min}(t,x)\) be the smallest eigenvalue of \(H(t,x)\). If \(H\) were an ODE
\(
\dot H = -2H^2 + K,
\)
then along the eigenvector of \(\lambda_{\min}\) we’d get
\[
\dot\lambda_{\min} \ge -2\lambda_{\min}^2 + \lambda_{\min}(K).
\]

For the PDE, one needs a maximum-principle argument. The standard tool is a **matrix maximum principle** (Hamilton-type) applied to symmetric-matrix-valued parabolic equations. In this project’s “salvage stack,” we use the following controlled template.

**Proposition 3.1 (template Riccati lower bound).**
Assume

1. \(H(t,\cdot)\) is smooth and symmetric for each \(t\),
2. \(\nabla^2J_t(x)\succeq c_0 I\) for all \(t,x\),
3. the diffusion/transport terms admit a matrix maximum principle for \(\lambda_{\min}\) (this is true in many smooth finite-dimensional settings).

Then the spatial infimum
\(
\underline\lambda(t):=\inf_x \lambda_{\min}(t,x)
\)
obeys the viscosity inequality
\[
\boxed{\;\underline\lambda'(t) \ge -2\underline\lambda(t)^2 + c_0.\;}
\]

### Solving the comparison ODE
Consider the equality ODE
\(
\dot\lambda = -2\lambda^2 + c_0\).
Two regimes:

- If \(c_0=0\), then \(\lambda(t)\sim 1/(2t)\) for large \(t\) (curvature decays).
- If \(c_0>0\), then \(\lambda(t)\) is driven toward the fixed point
\[
\lambda_* = \sqrt{c_0/2}.
\]

So a true positive source arrests Riccati decay.

**Takeaway:** “curvature-stable RG” is precisely the claim that the effective \(\nabla^2 J_t\) term stays positive enough to prevent \(\underline\lambda(t)\to 0\).

---

## 4. Computational confirmation: vHJ curvature follows Riccati laws

The project includes 4D grid simulations of the PDE
\(
\partial_t S = \Delta S - |\nabla S|^2
\)
starting from a strictly convex quadratic \(S_0(x)=\tfrac12 x^T H x\). The smallest Hessian eigenvalue at the grid center decays smoothly and is well-fit by
\[
\frac{1}{\lambda(t)} \approx \frac{1}{\lambda(0)} + \alpha t,
\]
consistent with \(\dot\lambda\approx -\alpha\lambda^2\).

A YM-inspired variant (quadratic + Haar mass + quartic terms) tracks the full 4×4 Hessian spectrum over time, producing sequences \(\lambda_i(t)\) and fitted Riccati slopes \(\alpha_i\) that are tightly clustered (mode-universal decay).

This is **not** a proof of YM curvature stability; it is evidence that the Riccati mechanism is the correct effective dynamical law in the convex regime.

---

## 5. What must be true for Yang–Mills

To turn this into a Yang–Mills theorem, you need a genuine RG/coarse-graining map for lattice YM such that, in appropriate local coordinates:

1. It induces an effective potential \(S_t\) satisfying a Hessian flow comparable to the PDE above.
2. The analogue of \(\nabla^2J_t\) has a **uniform positive lower bound** (or dominates Riccati decay) across scales.

The Haar-induced curvature in exponential coordinates is the natural candidate “seed” source; the next hard question is whether it persists under coarse-graining in the *presence* of the plaquette coupling.
