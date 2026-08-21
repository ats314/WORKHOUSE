---
title: "Finite-Volume SU(3) Convexity Core: λ_min(β,r,L), R_L(β), and τ_L(β,r)"
date: "2026-01-01"
---

## 1. Scope and definitions

This document records the **project’s strongest numerical artifacts**:

- **Local convexity observable** (finite-volume):
  \[
    \lambda_{\min}(\beta,r;L)
    := \lambda_{\min}\big(\nabla^2 S_\beta(A)\big)
  \]
  evaluated at random small-field configurations with typical link amplitude \(\|A_\ell\|\sim r\).

- **Convexity radius (Gribov-horizon proxy)**:
  \[
    R_L(\beta) := \sup\{\, r>0:\ \lambda_{\min}(\beta,r;L) > 0\ \text{(robustly across samples)} \,\}.
  \]

- **Dynamic restoration time** under gradient/viscous-HJ flow:
  \[
    \partial_t A_t = - \nabla S_\beta(A_t), \qquad
    \tau_L(\beta,r) := \inf\{t\ge 0: \lambda_{\min}(\nabla^2 S_\beta(A_t))>0\},
  \]
  starting from random initial data with amplitude \(\|A_0\|\sim r\).

Numerically, these are computed with:

- JAX evaluation of the action
- Hessian–vector products via JVP
- Lanczos (small Krylov dimension) to estimate \(\lambda_{\min}\)

---

## 2. Core engine (minimal, reproducible)

Below is the *minimal* skeleton of the SU(3) engine used in the project runs.  
(Full scripts exist in the project logs; this is the “portable core.”)

```python
import jax, jax.numpy as jnp, jax.lax as lax
from functools import partial

jax.config.update("jax_enable_x64", False)

def su3_generators():
    # anti-Hermitian basis i*lambda_a/2
    lam1 = jnp.array([[0,1,0],[1,0,0],[0,0,0]], jnp.complex64)
    lam2 = jnp.array([[0,-1j,0],[1j,0,0],[0,0,0]], jnp.complex64)
    lam3 = jnp.array([[1,0,0],[0,-1,0],[0,0,0]], jnp.complex64)
    lam4 = jnp.array([[0,0,1],[0,0,0],[1,0,0]], jnp.complex64)
    lam5 = jnp.array([[0,0,-1j],[0,0,0],[1j,0,0]], jnp.complex64)
    lam6 = jnp.array([[0,0,0],[0,0,1],[0,1,0]], jnp.complex64)
    lam7 = jnp.array([[0,0,0],[0,0,-1j],[0,1j,0]], jnp.complex64)
    lam8 = jnp.array([[1,0,0],[0,1,0],[0,0,-2]], jnp.complex64) / jnp.sqrt(3)
    return 1j * jnp.stack([lam1,lam2,lam3,lam4,lam5,lam6,lam7,lam8], 0) / 2.0

T_SU3 = su3_generators()

def su3_alg_from_vec(a):  # a shape (...,8)
    return jnp.einsum("...a,aij->...ij", a, T_SU3)

@jax.checkpoint
def su3_exp_pade22(A):
    I = jnp.eye(3, dtype=jnp.complex64)
    A2 = A @ A
    c1, c2 = 0.5, 0.083333336
    Num = I + c1*A + c2*A2
    Den = I - c1*A + c2*A2
    return jnp.linalg.solve(Den, Num)

def build_links_factory(L):
    @jax.checkpoint
    def build_links(params):  # params shape (L,L,L,L,4,8)
        flat = params.reshape(-1,8)
        A = jax.vmap(su3_alg_from_vec)(flat)
        U = jax.vmap(su3_exp_pade22)(A)
        return U.reshape(L,L,L,L,4,3,3)
    return build_links

@jax.jit
def compute_plaquette_sum(U, beta):
    S = 0.0
    for mu in range(4):
        for nu in range(mu+1, 4):
            U_mu = U[..., mu, :, :]
            U_nu_shift = jnp.roll(U[..., nu, :, :], -1, axis=mu)
            U_mu_dag_shift = jnp.swapaxes(jnp.conjugate(jnp.roll(U[..., mu, :, :], -1, axis=nu)), -1, -2)
            U_nu_dag = jnp.swapaxes(jnp.conjugate(U[..., nu, :, :]), -1, -2)
            P = U_mu @ U_nu_shift @ U_mu_dag_shift @ U_nu_dag
            trP = jnp.real(jnp.einsum("...ii->...", P))
            S += jnp.sum(1.0 - trP/3.0)
    return beta * S

@jax.jit
def haar_mass(params, c0):
    flat = params.reshape(-1,8)
    def per(a):
        A = su3_alg_from_vec(a)
        return jnp.real(jnp.trace(A.conj().T @ A))  # Frobenius^2
    return c0 * jax.vmap(per)(flat).sum()

def make_flat_action(L, beta, c0):
    build_links_L = build_links_factory(L)
    def unflatten(x): return x.reshape((L,L,L,L,4,8))

    @jax.jit
    def flat_action(theta):  # theta shape (L^4*4*8,)
        params = unflatten(theta)
        U = build_links_L(params)
        return compute_plaquette_sum(U, beta) + haar_mass(params, c0)
    return flat_action

def hvp(flat_action, theta, v):
    g = jax.grad(flat_action)
    _, hv = jax.jvp(g, (theta,), (v,))
    return hv

def lanczos_min(flat_action, theta, k=25, seed=0):
    key = jax.random.PRNGKey(seed)
    n = theta.shape[0]
    v0 = jax.random.normal(key, (n,))
    v0 /= jnp.linalg.norm(v0)

    def step(carry, _):
        v_prev, v, beta_prev = carry
        w = hvp(flat_action, theta, v)
        w -= beta_prev * v_prev
        alpha = jnp.dot(w, v)
        w -= alpha * v
        beta = jnp.linalg.norm(w)
        v_next = w / (beta + 1e-9)
        return (v, v_next, beta), (alpha, beta)

    (_, _, _), (alphas, betas) = lax.scan(step, init=(jnp.zeros_like(v0), v0, 0.0),
                                         xs=None, length=k)
    alphas = jnp.array(alphas)
    betas = jnp.array(betas[:-1])
    T = jnp.diag(alphas) + jnp.diag(betas, 1) + jnp.diag(betas, -1)
    return float(jnp.linalg.eigvalsh(T)[0])
```

---

## 3. Raw convexity scan data (λ_min tables)

### 3.1 L=4 scan (β × scale ∈ {0.05,0.10,0.15})

```python
res4 = [
    (0.40, 0.050, +0.107639), (0.40, 0.100, +0.084942), (0.40, 0.150, +0.060163),
    (0.77, 0.050, +0.090999), (0.77, 0.100, +0.049703), (0.77, 0.150, +0.000575),
    (1.14, 0.050, +0.074027), (1.14, 0.100, +0.011488), (1.14, 0.150, -0.063704),
    (1.51, 0.050, +0.058620), (1.51, 0.100, -0.028256), (1.51, 0.150, -0.121915),
    (1.89, 0.050, +0.042761), (1.89, 0.100, -0.061317), (1.89, 0.150, -0.172886),
    (2.26, 0.050, +0.024951), (2.26, 0.100, -0.097842), (2.26, 0.150, -0.229981),
    (2.63, 0.050, +0.006105), (2.63, 0.100, -0.131974), (2.63, 0.150, -0.287083),
    (3.00, 0.050, -0.008208), (3.00, 0.100, -0.172180), (3.00, 0.150, -0.376565),
]
```

### 3.2 L=6 scan

```python
res6 = [
    (0.40, 0.050, +0.108966), (0.40, 0.100, +0.087381), (0.40, 0.150, +0.063117),
    (0.77, 0.050, +0.093839), (0.77, 0.100, +0.052703), (0.77, 0.150, +0.006658),
    (1.14, 0.050, +0.079105), (1.14, 0.100, +0.016544), (1.14, 0.150, -0.052778),
    (1.51, 0.050, +0.063542), (1.51, 0.100, -0.017121), (1.51, 0.150, -0.111918),
    (1.89, 0.050, +0.048837), (1.89, 0.100, -0.056489), (1.89, 0.150, -0.173765),
    (2.26, 0.050, +0.033850), (2.26, 0.100, -0.085747), (2.26, 0.150, -0.232562),
    (2.63, 0.050, +0.018730), (2.63, 0.100, -0.120620), (2.63, 0.150, -0.278895),
    (3.00, 0.050, +0.003391), (3.00, 0.100, -0.154899), (3.00, 0.150, -0.348172),
]
```

### 3.3 L=8 scan (full: scales 0.05, 0.10, 0.15 at the same β grid)

```python
res8_full = [
    (0.40, 0.050, +0.109207), (0.40, 0.100, +0.087311), (0.40, 0.150, +0.062942),
    (0.77, 0.050, +0.094372), (0.77, 0.100, +0.053147), (0.77, 0.150, +0.004519),
    (1.14, 0.050, +0.078979), (1.14, 0.100, +0.015042), (1.14, 0.150, -0.051065),
    (1.51, 0.050, +0.065228), (1.51, 0.100, -0.016862), (1.51, 0.150, -0.107826),
    (1.89, 0.050, +0.049413), (1.89, 0.100, -0.051518), (1.89, 0.150, -0.165610),
    (2.26, 0.050, +0.036033), (2.26, 0.100, -0.089054), (2.26, 0.150, -0.225723),
    (2.63, 0.050, +0.020245), (2.63, 0.100, -0.119307), (2.63, 0.150, -0.277276),
    (3.00, 0.050, +0.005785), (3.00, 0.100, -0.158744), (3.00, 0.150, -0.336072),
]
```

---

## 4. Quick scaling check across lattice sizes (coarse R-estimates)

A fast estimate of the convexity radius at a given \(\beta\) can be extracted from the 3-scale data by linear interpolation in \(r\) between the nearest positive and negative \(\lambda_{\min}\).

Let \(R_{\mathrm{est}}(\beta;L)\) be the linear root estimate between \((r_i,\lambda_i)\) and \((r_{i+1},\lambda_{i+1})\).

Computed from the above \(\{0.05,0.10,0.15\}\) grids:

| β | R_est(L=4) | R_est(L=6) | R_est(L=8) |
|---:|---:|---:|---:|
| 1.14 | 0.1076 | 0.1119 | 0.1114 |
| 1.51 | 0.0837 | 0.0894 | 0.0897 |
| 1.89 | 0.0705 | 0.0732 | 0.0745 |
| 2.26 | 0.0602 | 0.0642 | 0.0644 |
| 2.63 | 0.0522 | 0.0567 | 0.0573 |
| 3.00 | <0.05 | 0.0511 | 0.0518 |

Interpretation (purely finite-volume, empirical):

- For \(\beta \in [1.14, 2.63]\), the inferred \(R_{\mathrm{est}}\) is *very* close for \(L=6\) and \(L=8\), and not far for \(L=4\).
- The outlier at \((L=4,\beta=3)\) is consistent with a **small finite-volume drift** rather than a collapse of the convexity core.

---

## 5. Numerically detected convexity radius curve R(β) at L=8

The project also ran a more robust radius finder using:

- multiple random samples per radius
- conservative stability test: **min**\(\lambda_{\min}\) across samples must be \(>0\)
- bisection on \(r\)

Output:

```python
R_curve_L8 = [
    (0.4, 0.2448828125),
    (0.8, 0.1454296875),
    (1.2, 0.1038671875),
    (1.6, 0.0816015625),
    (2.0, 0.0682421875),
    (2.4, 0.0578515625),
    (2.8, 0.051171875),
    (3.2, 0.0459765625),
]
```

This extends beyond \(r=0.15\) at small \(\beta\), which is why the coarse 3-scale scan cannot see it.

---

## 6. τ(β,r) dynamic restoration map (fast version)

The project also computed a coarse “restoration time” map under gradient flow:
\[
  \tau(\beta,r) \in \{0, 0.08, 0.16, 0.24, \dots\}
\]
with coarse measurement intervals and early stopping once \(\lambda_{\min}>0\).

A recorded partial table (L=8) includes:

- \(\beta=0.40\): \(\tau\approx 0\) for \(r \le 0.24\)
- \(\beta\ge 0.96\): \(\tau\) increases with \(r\) beyond the convex core (values \(0.16\)–\(0.48\) in the coarse grid)

(See the project log text for the exact printed triples.)

---

## 7. Multi-L scaling experiment: “candidate continuum structure” test

The key next numerical test is:

1. Compute \(R_L(\beta)\) for multiple \(L\in\{4,6,8,10,\dots\}\).
2. Compute \(\tau_L(\beta,r)\) on an \(r\)-grid expressed as multiples of \(R_L(\beta)\), e.g.
   \[
     r = s\,R_L(\beta), \qquad s \in [0.5, 2.0].
   \]
3. Attempt collapse:
   - plot \(R_L(\beta)\) vs \(\beta\) for each \(L\)
   - plot \(\tau_L(\beta,sR_L(\beta))\) vs \(s\) at fixed \(\beta\)
   - check whether \(\tau_L\) approaches an \(L\)-independent function \(\tau_\infty\)

### Suggested wrapper code

```python
import numpy as np

def compute_R_curve_multi(Ls, betas, c0=0.125, **R_kwargs):
    out = {}
    for L in Ls:
        out[L] = compute_R_curve(L=L, c0=c0, betas=np.array(betas), **R_kwargs)
    return out

def compute_tau_map_multi(Ls, betas, r_grid, c0=0.125, **tau_kwargs):
    out = {}
    for L in Ls:
        out[L] = compute_tau_map_fast(L=L, betas=np.array(betas), r_grid=np.array(r_grid),
                                      c0=c0, **tau_kwargs)
    return out

Ls = [4,6,8]
betas = [0.8, 1.2, 1.6, 2.0, 2.4, 2.8]
# r-grid expressed later as multiples of measured R_L(beta)
```

---

## 8. What this numerical package *does* and *does not* claim

- **Does**: document a nontrivial, volume-stable convexity core in the *small-field* region under a specific coordinate choice and a specific regularized Haar term.
- **Does**: provide candidate observables \((R_L,\tau_L)\) that can be stress-tested for scaling/collapse.

- **Does not**: by itself establish a continuum mass gap, OS reconstruction, or any infinite-volume/continuum uniformity theorems.
