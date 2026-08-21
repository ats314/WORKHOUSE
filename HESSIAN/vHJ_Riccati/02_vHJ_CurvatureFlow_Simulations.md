# vHJ Curvature-Flow Simulations (JAX) + Riccati Law Extraction

## 0. Scope

This document records the **viscous Hamilton–Jacobi (vHJ) curvature-flow** toy simulations used throughout the project as an RG surrogate:

- evolve a scalar potential \(S_t\) by
  \[
  \partial_t S_t = \Delta S_t - \|\nabla S_t\|^2 + J_t,
  \qquad
  J_t=\|\nabla S_t\|^2
  \]
  (or a closely related nonnegative source), and track curvature:
  \(\lambda_{\min}(t)=\min_x \lambda_{\min}(\nabla^2 S_t(x))\).

Empirically, the smallest Hessian eigenvalues follow a Riccati-type decay law
\[
\lambda(t)\approx\frac{1}{\mathrm{intercept}+\alpha t},
\]
with \(\alpha\) nearly constant across eigenmodes and across several “geometry terms” added to the action.

These are numerics. They are not a proof of anything about continuum YM.

---

## 1. Core derivations used in the simulation

Let \(\rho_t = P_t \rho_0\) with \(\rho_0=e^{-S_0}\), \(S_t=-\log\rho_t\).

Then (in Euclidean space) the evolution is
\[
\partial_t S_t = \Delta S_t - \|\nabla S_t\|^2 + J_t,
\qquad
J_t=\frac{\|\nabla\rho_t\|^2}{\rho_t^2}\ge 0.
\]

Differentiating twice gives the Hessian-flow PDE
\[
\partial_t H_t
=
\Delta H_t
-2(\nabla S_t\cdot\nabla)H_t
-2H_t^2
+\nabla^2 J_t,
\qquad H_t=\nabla^2 S_t.
\]

The \(-2H_t^2\) term is what produces Riccati-like decay even when the flow remains convex.

---

## 2. Minimal 4D JAX implementation

Below is a cleaned version of the 4D finite-difference implementation used in the project notes.

> **Warning:** It is a *toy* PDE on a periodic grid; it is **not** the Yang–Mills gradient flow.

```python
import jax
import jax.numpy as jnp

# -------------------------
# Grid + finite differences
# -------------------------
def laplacian(f):
    return (
        jnp.roll(f, +1, 0) + jnp.roll(f, -1, 0) +
        jnp.roll(f, +1, 1) + jnp.roll(f, -1, 1) +
        jnp.roll(f, +1, 2) + jnp.roll(f, -1, 2) +
        jnp.roll(f, +1, 3) + jnp.roll(f, -1, 3) -
        8.0*f
    )

def grad(f):
    return jnp.stack([
        0.5*(jnp.roll(f,-1,0)-jnp.roll(f,+1,0)),
        0.5*(jnp.roll(f,-1,1)-jnp.roll(f,+1,1)),
        0.5*(jnp.roll(f,-1,2)-jnp.roll(f,+1,2)),
        0.5*(jnp.roll(f,-1,3)-jnp.roll(f,+1,3)),
    ], axis=-1)

def hessian(f):
    # 4x4 Hessian at each lattice site
    g = grad(f)  # (...,4)
    Hcols = []
    for i in range(4):
        Hcols.append(grad(g[..., i]))   # (...,4)
    # stack columns -> (...,4,4)
    return jnp.stack(Hcols, axis=-1)

# -------------------------
# vHJ update step
# -------------------------
@jax.jit
def vHJ_step(S, dt, nu=1.0):
    g = grad(S)
    J = jnp.sum(g*g, axis=-1)          # toy nonnegative source
    dS = nu*laplacian(S) - jnp.sum(g*g, axis=-1) + J
    return S + dt*dS

# -------------------------
# Diagnostics
# -------------------------
@jax.jit
def hessian_min_eigs(S):
    H = hessian(S)                         # (...,4,4)
    evals = jnp.linalg.eigvalsh(H)         # (...,4)
    # sort eigenvalues ascending at each site
    evals = jnp.sort(evals, axis=-1)
    # spatial minima of each eigenvalue branch
    return jnp.min(evals.reshape(-1,4), axis=0)

# -------------------------
# Example driver
# -------------------------
def run(L=32, steps=300, dt=0.01, seed=0):
    key = jax.random.PRNGKey(seed)
    # initialize with small random convex bump
    S = 0.05*jax.random.normal(key, (L,L,L,L))
    records = []
    for k in range(steps+1):
        if k % 30 == 0:
            lam = hessian_min_eigs(S)
            records.append((k, lam))
            print(k, lam)
        S = vHJ_step(S, dt)
    return records
```

---

## 3. Representative outputs recorded in the project

### 3.1 “Curvature trace” decay (sum of eigenvalues)

The following is a representative run summary (project log):

```
step   curvature_trace
   0   4.200736
  30   3.713531
  60   3.330270
  90   3.020311
 120   2.764121
 150   2.548645
 180   2.364778
 210   2.205960
 240   2.067349
 270   1.945289
```

A one-parameter Riccati fit of the form
\[
\lambda(t)\approx \frac{1}{\mathrm{intercept}+\alpha t}
\]
was extracted with:

```
Estimated Riccati coefficient α = 0.0010214540013711412
Intercept (1/λ0) = 0.23878515618101043
```

and the prediction was numerically accurate at the tabulated times.

### 3.2 Full 4×4 Hessian eigenvalue branches

Another run logged the four smallest spatial-minima eigenvalues:

```
step     λ1      λ2      λ3      λ4   (sorted eigenvalues)
   0   3.137619  3.801772  4.401150  5.462403
  30   2.866945  3.411298  3.885940  4.689939
  ...
 270   1.696828  1.873549  2.008032  2.202747
```

Each branch \(\lambda_i(t)\) fit well to a Riccati form with nearly identical \(\alpha_i\):

```
i=1:  α≈0.0010022789
i=2:  α≈0.0010026004
i=3:  α≈0.0010028736
i=4:  α≈0.0010033081
```

---

## 4. How the \(\alpha_i\) extraction was performed (template)

Given a time series \(\{(t_k,\lambda_i(t_k))\}\), fit
\[
\frac{1}{\lambda_i(t)} \approx \mathrm{intercept}_i + \alpha_i\, t
\]
by linear regression.

```python
import numpy as np

def fit_alpha(times, lambdas):
    # times: shape (K,)
    # lambdas: shape (K,) positive
    y = 1.0/np.array(lambdas)
    X = np.vstack([np.array(times), np.ones_like(times)]).T
    alpha, intercept = np.linalg.lstsq(X, y, rcond=None)[0]
    return alpha, intercept
```

---

## 5. Interpretation within the project

The project uses these numerics as evidence for a **robust Riccati decay law** in curvature-flow toy models, and as motivation for a curvature-propagation mechanism under coarse-graining.

What is not supplied (and is needed for any YM claim) is a derivation that the same PDE (or a controlled analog with the right source term) governs the **log density** under an actual Yang–Mills renormalization or gradient flow on the gauge configuration space.

