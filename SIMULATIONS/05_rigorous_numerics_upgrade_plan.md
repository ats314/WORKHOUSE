# Upgrading the Simulations into Rigorous Numerics (Validated bounds, not vibes)

This file is pragmatic: how to turn the project’s strongest simulations into
**certificates** that could support real proof steps.

It pulls examples from:
- `YM_PDE_vHJ_Sims.txt` (vHJ PDE curvature),
- `COLAB PDF EXPORT 2.pdf` (the “catastrophic negative curvature” debug story),
- `12-3-25 CODE RUN.pdf` (SU(3) lattice Hessian scans for Wilson+Haar in A-coordinates),
- and the q-Racah lab.

---

## 0. The core philosophy

A numerical result is proof-grade only if you can bound:
1. **discretization error** (PDE),
2. **Monte Carlo / sampling error**,
3. **floating-point / roundoff error**,
4. and **cover the domain** you claim the bound holds on.

The fastest upgrade path here is **verified eigenvalue bounds** (not “just run more samples”).

---

## 1. Diagnose the failure mode we already saw (and how to prevent it)

In `COLAB PDF EXPORT 2.pdf`, the “coarse-grained Hessian” experiment produced absurdly negative eigenvalues:
- at $\ell=1.0$, $\lambda_{\min}(H_\ell)\approx -324$ while a naive bound predicted $+0.666$.

This is not “physics being mean.” It indicates *the estimator or hypotheses were wrong*.

Two common culprits in this project family:

### (A) Wrong measure / missing weights
For a coarse-grained potential
\[
S_\ell(x) = -\log \mathbb{E}_{\xi\sim N(0,I)}\left[e^{-S(x+\ell\xi)}\right],
\]
the correct identity is
\[
\nabla^2 S_\ell(x) = \mathbb{E}_w[\nabla^2 S] - \operatorname{Cov}_w(\nabla S),
\]
where $w \propto e^{-S(x+\ell\xi)}$ is the **importance weight**.
Using **uniform** weights will generally break the identity.

### (B) Global nonconvexity in the perturbation
The project also observed that choosing $f(x)=\sin(\sum x_i)$ causes global nonconvexity problems, while switching to a bounded bump $f(x)=\varepsilon e^{-\|x\|^2}$ controls Hessian blow-up.

**Action item:** every “curvature stability” simulation must log (i) the weighting used and (ii) a global bound on the perturbation Hessian.

---

## 2. Verified extremal eigenvalues: the cheapest proof-grade certificate

Suppose you have a symmetric matrix $H$ (exactly what the Hessian is numerically).
Let $(\hat\lambda, \hat v)$ be an approximate eigenpair with $\|\hat v\|=1$ and residual
\[
r := \|H\hat v - \hat\lambda \hat v\|_2.
\]
Then a standard result implies: there exists a true eigenvalue $\lambda$ of $H$ with
\[
|\lambda - \hat\lambda| \le r.
\]

### How to use this for a lower bound on $\lambda_{\min}(H)$
If you have an approximation $\hat\lambda_{\min}$ from Lanczos/ARPACK and you can compute a residual $r$ for the returned eigenvector, then
\[
\lambda_{\min}(H) \ge \hat\lambda_{\min} - r.
\]
That’s already a **rigorous certificate** modulo floating-point error control.

**Floating-point wrap:** compute the residual in higher precision (e.g. `mpmath.mp.dps=100`) to dominate roundoff.

---

## 3. Covering a region: grid + Lipschitz bounds for Hessians

To certify “$\lambda_{\min}(H(A))\ge \rho_0$ for all $A$ in a region $\Omega$”, you can:

1. Choose a finite grid $\{A_k\}$ covering $\Omega$ by balls of radius $\delta$.
2. Certify $\lambda_{\min}(H(A_k))\ge \rho_0 + \epsilon$ at each grid point (via residual bounds).
3. Prove a Lipschitz bound for the Hessian:
\[
\|H(A)-H(B)\|_{\mathrm{op}} \le L\,\|A-B\|.
\]
4. Then for any $A$ within $\delta$ of some $A_k$:
\[
\lambda_{\min}(H(A)) \ge \lambda_{\min}(H(A_k)) - \|H(A)-H(A_k)\|
\ge (\rho_0+\epsilon) - L\delta.
\]
Choose $\delta \le \epsilon/L$.

**Where does $L$ come from?**  
From bounding **third derivatives**. In this project, that means bounding derivatives of $\exp(A)$ and products of exponentials. This is exactly why `07_uniform_wilson_hessian_bound_candidate.md` matters: once derivative bounds are uniform, a Lipschitz constant becomes feasible.

---

## 4. Specific upgrade targets in this repo

### 4.1 SU(3) lattice Hessian scans (`12-3-25 CODE RUN.pdf`)
This run computed Hessians at $A=0$ for $L=2$:
- Wilson-only min eigenvalue $\approx 0$ (numerical),
- Haar-only min eigenvalue $\approx 0.25$,
- Wilson+Haar min eigenvalue $\approx 0.25$.

Next upgrades:
- replace “random sampling over configs” by a **grid+Lipschitz** certificate on a ball $\|A\|_\infty\le r$,
- use residual-based bounds for $\lambda_{\min}$,
- use interval arithmetic (optional) for the worst-case rounding.

### 4.2 vHJ PDE curvature (`YM_PDE_vHJ_Sims.txt`)
Validated PDE numerics is harder because of discretization error.

A feasible intermediate certificate:
- treat the PDE as a *finite-dimensional ODE* after spatial discretization,
- compute curvature evolution on that ODE system and certify its behavior (residual bounds on Jacobians/Hessians),
- state clearly: “certificate for the discretized system,” not the continuum PDE.

For full PDE validation, you’d want monotone schemes + a posteriori error bounds (serious numerical analysis).

### 4.3 q-Racah gap lab
This is already “close” to rigorous because it’s finite-dimensional linear algebra.
For certificates:
- compute eigenvalues in high precision,
- prove positivity of the Doob ground state (no near-zero entries),
- compute the gap with rigorous rounding bounds.

---

## 5. Minimal code skeleton: certified $\lambda_{\min}$ via residual

```python
import numpy as np
import mpmath as mp

def certified_min_eig(H):
    # Step 1: approximate smallest eigenpair
    w, V = np.linalg.eigh(H)
    lam_hat = float(w[0])
    v_hat = V[:, 0]
    v_hat = v_hat / np.linalg.norm(v_hat)

    # Step 2: compute residual in high precision
    mp.mp.dps = 80
    Hv = mp.matrix(H.tolist()) * mp.matrix(v_hat.tolist())
    v = mp.matrix(v_hat.tolist())
    r = mp.norm(Hv - lam_hat * v)

    # certified lower bound
    return lam_hat - float(r)
```

This is not the endgame, but it’s the fastest path from “simulation” to “certificate.”

---

## 6. Bottom line

The simulations in this project are valuable — but a subset can be **converted into rigorous numerics** with:
- residual-based eigenvalue certification,
- grid + Lipschitz covering,
- explicit derivative bounds (analytic) feeding into the Lipschitz constants.

That’s the shortest bridge from “cool plots” to “referee-checkable lemmas.”

