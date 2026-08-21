# Finite-Dimensional vHJ Hessian Flow and Riccati Structure (Rigorous)

This document extracts and consolidates the rigorous pieces from:

- `doc2_vHJ_Hessian_Flow.txt`
- `YM_Salvage_Stack_Appendix_D_Hessian_Flow_and_Riccati.txt`
- simulation notes in `YM_PDE_vHJ_Sims.txt` and `12-2-25 code runs.pdf`

The key point: **the Hessian evolution equation and the Riccati-type structure are fully rigorous in $\mathbb{R}^n$**. Any attempt to use the same mechanism for lattice Yang–Mills must be stated as an additional hypothesis (see `06_conjectures_target_lemmas.md`).

---

## 1. From heat flow to viscous Hamilton–Jacobi (vHJ)

Let $\rho_t(x)>0$ solve the heat equation on $\mathbb{R}^n$:
\[
\partial_t \rho_t = \Delta \rho_t.
\]
Write $\rho_t = Z_t^{-1} e^{-S_t}$. A direct computation yields
\[
\partial_t S_t = \Delta S_t - \lvert \nabla S_t\rvert^2 \quad\text{(up to an additive function of $t$)}.
\]
This is the **viscous Hamilton–Jacobi equation**.

---

## 2. Gradient evolution

Let $b = \nabla S_t$. Differentiate the vHJ equation:
\[
\partial_t b
= \Delta b - 2\,(\nabla^2 S_t)\, b.
\]
In indices:
\[
\partial_t (\partial_j S) = \Delta(\partial_j S) - 2\,(\partial_k S)(\partial_{jk}S).
\]

---

## 3. Hessian flow equation (reaction–diffusion + transport + Riccati)

Let $H = \nabla^2 S_t$ (symmetric). Differentiating once more yields
\[
\boxed{
\partial_t H
= \Delta H - 2\,(\nabla S\cdot \nabla)H - 2 H^2.
}
\]
More generally, if the density has a source term and $S_t$ satisfies
\[
\partial_t S_t = \Delta S_t - |\nabla S_t|^2 + J_t(x),
\]
then
\[
\boxed{
\partial_t H
= \Delta H - 2(\nabla S\cdot \nabla)H - 2 H^2 + \nabla^2 J_t(x).
}
\]
This is the “Hessian flow” backbone used in the project’s curvature-stability architecture.

---

## 4. Minimal eigenvalue: what you can *actually* conclude

Let $\lambda_{\min}(t,x)$ be the smallest eigenvalue of $H(t,x)$. Evaluating the PDE along a unit eigenvector $v_{\min}$ gives the exact identity (pointwise):
\[
\langle v_{\min},\, (\partial_t H)\, v_{\min}\rangle
=
\langle v_{\min},\, (\Delta H)\, v_{\min}\rangle
-2\langle v_{\min},\, (\nabla S\cdot\nabla H)\, v_{\min}\rangle
-2\lambda_{\min}^2
+ \langle v_{\min}, (\nabla^2 J_t)v_{\min}\rangle.
\]
The nonlinear part is **always**:
\[
-2\lambda_{\min}^2.
\]

### 4.1 A clean comparison ODE (conditional)

If, along some chosen path/characteristic, you can bound the “other terms” by constants:
\[
\langle v_{\min},\, (\Delta H)\, v_{\min}\rangle
-2\langle v_{\min},\, (\nabla S\cdot\nabla H)\, v_{\min}\rangle
+ \langle v_{\min}, (\nabla^2 J_t)v_{\min}\rangle
\;\ge\; \beta,
\]
then you get a Riccati inequality of the form
\[
\boxed{
\frac{d}{dt}\lambda(t) \ge -2\lambda(t)^2 + \beta.
}
\]
- If $\beta>0$, the equality ODE has a stable fixed point $\lambda_*=\sqrt{\beta/2}$.
- This is the mathematically correct “curvature floor” story: **a positive source can balance the Riccati drain**.

Importantly: this is *not* the inequality $\lambda'(t)\ge +2\lambda(t)^2$. The sign matters.

---

## 5. Simulation evidence (what it suggests, without claiming proof)

### 5.1 4D vHJ curvature flow (finite-difference)
A representative run recorded in `YM_PDE_vHJ_Sims.txt` reports:
- $\lambda_{\min}$ decreases smoothly from $\approx 1.8468$ to $\approx 1.0080$ over the sampled times,
- a Riccati fit of the form $d\lambda/dt\approx -\alpha\lambda^2$ gives
\[
1/\lambda(t)\approx 1/\lambda(0) + \alpha t,
\]
with $\alpha \approx 1.021\times 10^{-3}$ (excellent fit).

### 5.2 “Universal $\alpha$” across multiple eigenvalues (toy YM-like PDE)
In `12-2-25 code runs.pdf` a least-squares fit of $1/\lambda_i(t)$ vs $t$ for several eigenmodes in an SU(2)+Haar+YM-like PDE reports:
\[
\alpha_i \approx 7.9\times 10^{-4}\ \ \text{with small spread across } i.
\]
This “near-universality” is the interesting empirical phenomenon: it suggests that in the tested regime, eigenmodes share a common effective Riccati rate.

---

## 6. Why this is exciting

Because it’s one of the few places where the project has:
- **exact derivations** (not just narrative),
- a clear **mechanism** (Riccati drain vs curvature source),
- and direct **numerical signatures**.

If you want to push this into publishable math, the next step is to prove a theorem of the form:

> Under hypotheses (H1–H3) on $J_t$ and on bounds for the transport/diffusion terms, $\lambda_{\min}$ stays $\ge \rho_0>0$ for all $t\ge t_*$.

That theorem is purely PDE/ODE analysis on $\mathbb{R}^n$ and is an achievable “first hard result.”

