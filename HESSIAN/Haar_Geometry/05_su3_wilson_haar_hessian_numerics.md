# SU(3) Wilson+Haar convexity maps (JAX): code + results + what they do (and do not) prove

## 0. What this file is

This is the “computational confirmation” layer: a GPU-friendly JAX engine that estimates
\(
\lambda_{\min}(\nabla^2 S_{\beta,c_0}(\theta))
\)
for the SU(3) lattice action
\[
S_{\beta,c_0}(\theta)=S_{\mathrm{Wilson}}(\exp(A(\theta))) + S_{\mathrm{Haar,quad}}(A(\theta)),
\]
where \(A(\theta)\in\mathfrak{su}(3)\) lives on each link and is parameterized by 8 real coefficients.

The engine uses:

- A fast SU(3) exponential via Padé[2/2].
- Hessian–vector products (HVP) via JAX automatic differentiation.
- Lanczos tridiagonalization to approximate the smallest Hessian eigenvalue without materializing the full Hessian.

**What you get:** a multi-volume map of a “convex core” in field space as a function of \(\beta\) and a small-field scale.

**What you do *not* get automatically:** measure concentration of true lattice YM, or a proof that typical configurations lie inside the convex core.

---

## 1. The code cell (copy/paste)

> Paste this into Colab **after** installing JAX and selecting a GPU.

```python
# ========================================================================
# TURBO SU(3) CONVEXITY ENGINE (A100-optimized, Padé[2/2], Haar-quadratic)
# ========================================================================

import jax
import jax.numpy as jnp
import numpy as np
import jax.lax as lax

jax.config.update("jax_enable_x64", False)

# -------------------------- SU(3) GENERATORS ----------------------------

def su3_generators():
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

def su3_alg_from_vec(a):
    return jnp.einsum("...a,aij->...ij", a, T_SU3)

# ---------------------- SU(3) EXP VIA PADÉ 2/2 --------------------------

@jax.checkpoint
def su3_exp_pade22(A):
    I = jnp.eye(3, dtype=jnp.complex64)
    A2 = A @ A
    c1, c2 = 0.5, 1/12.0
    Num = I + c1*A + c2*A2
    Den = I - c1*A + c2*A2
    return jnp.linalg.solve(Den, Num)

# -------------------------- BUILD LINKS ----------------------------------

def build_links_factory(L):
    @jax.checkpoint
    def build_links(params):
        flat = params.reshape(-1,8)
        A = jax.vmap(su3_alg_from_vec)(flat)
        U = jax.vmap(su3_exp_pade22)(A)
        return U.reshape(L,L,L,L,4,3,3)
    return build_links

# ---------------------- PLAQUETTE SUM (FAST) -----------------------------

def compute_plaquette_sum(U, beta):
    S = 0.0
    for mu in range(4):
        for nu in range(mu+1,4):
            U_mu = U[..., mu, :, :]
            U_nu_shift = jnp.roll(U[..., nu, :, :], -1, axis=mu)
            U_mu_dag_shift = jnp.swapaxes(
                jnp.conjugate(jnp.roll(U[..., mu, :, :], -1, axis=nu)),
                -1, -2
            )
            U_nu_dag = jnp.swapaxes(jnp.conjugate(U[..., nu, :, :]), -1, -2)
            P = U_mu @ U_nu_shift @ U_mu_dag_shift @ U_nu_dag
            trP = jnp.real(jnp.einsum("...ii->...", P))
            S += jnp.sum(1.0 - trP/3.0)
    return beta * S

def vectorized_wilson_action(params, L, beta, build_links_L):
    U = build_links_L(params)
    return compute_plaquette_sum(U, beta)

# --------------------------- HAAR MASS -----------------------------------

@jax.jit
def haar_mass(params, c0):
    flat = params.reshape(-1,8)
    def per(a):
        A = su3_alg_from_vec(a)
        return jnp.real(jnp.trace(A.conj().T @ A))
    return c0 * jax.vmap(per)(flat).sum()

# -------------------------- TOTAL ACTION ---------------------------------

def make_flat_funcs(L, beta, c0):
    build_links_L = build_links_factory(L)
    def unflatten(theta):
        return theta.reshape((L,L,L,L,4,8))
    @jax.jit
    def flat_action(theta):
        params = unflatten(theta)
        return vectorized_wilson_action(params, L, beta, build_links_L) + haar_mass(params, c0)
    n_params = L**4 * 4 * 8
    return flat_action, n_params

# --------------------------- HVP & LANCZOS -------------------------------

def hvp(flat_action, theta, v):
    g = jax.grad(flat_action)
    _, hv = jax.jvp(g, (theta,), (v,))
    return hv

def lanczos_min(flat_action, theta, k=20, seed=0):
    key = jax.random.PRNGKey(seed)
    n = theta.shape[0]
    v0 = jax.random.normal(key, (n,))
    v0 = v0 / jnp.linalg.norm(v0)

    def step(carry, _):
        v_prev, v, beta_prev = carry
        w = hvp(flat_action, theta, v)
        w = w - beta_prev * v_prev
        alpha = jnp.dot(w, v)
        w = w - alpha * v
        beta = jnp.linalg.norm(w)
        return (v, w / (beta + 1e-8), beta), (alpha, beta)

    (_, _, _), (a, b) = lax.scan(step, (jnp.zeros_like(v0), v0, 0.0), None, length=k)
    a = jnp.array(a)
    b = jnp.array(b[:-1])
    T = jnp.diag(a) + jnp.diag(b, 1) + jnp.diag(b, -1)
    return float(jnp.linalg.eigvalsh(T)[0])

# ---------------------------- GRID SCAN ----------------------------------

def convexity_grid(L, betas, scales, c0=0.125, n_samples=3, seed=1):
    key = jax.random.PRNGKey(seed)
    results = []
    for beta in betas:
        flat_action, n_params = make_flat_funcs(L, float(beta), c0)
        for scale in scales:
            vals = []
            for _ in range(n_samples):
                key, sub = jax.random.split(key)
                key, sub2 = jax.random.split(key)
                theta = (scale * jax.random.normal(sub, (n_params,), dtype=jnp.float32))
                vals.append(lanczos_min(flat_action, theta, k=20, seed=int(sub2[0])))
            results.append((float(beta), float(scale), float(np.min(vals))))
    return results
```

---

## 2. Recorded results (multi-volume convexity window)

These were reconstructed from the project run logs.

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

res8 = [
    (0.40, 0.050, +0.109223),
    (0.77, 0.050, +0.094255),
    (1.14, 0.050, +0.079963),
    (1.51, 0.050, +0.064737),
    (1.89, 0.050, +0.050365),
    (2.26, 0.050, +0.035428),
    (2.63, 0.050, +0.021559),
    (3.00, 0.050, +0.006509),
]
```

A plotting helper:

```python
import numpy as np
import matplotlib.pyplot as plt

def extract_curve(res, target_scale=0.05):
    pts = [(b,lam) for (b,sc,lam) in res if abs(sc-target_scale)<1e-12]
    pts = sorted(pts)
    b = np.array([x[0] for x in pts])
    l = np.array([x[1] for x in pts])
    return b,l

for lbl,res in [("L=4",res4),("L=6",res6),("L=8",res8)]:
    b,l = extract_curve(res, 0.05)
    plt.plot(b,l,marker='o',label=lbl)

plt.axhline(0,color='k',lw=1)
plt.xlabel(r"$\beta$")
plt.ylabel(r"$\lambda_{\min}(\nabla^2 S)$")
plt.title("Convexity window (scale=0.05)")
plt.grid(True)
plt.legend();
plt.show()
```

---

## 3. Interpretation (what the numerics are actually saying)

1. **A convex core exists** for small enough field scale (here, \(\text{scale}\approx 0.05\)) over a wide range of \(\beta\), and the smallest Hessian eigenvalue decreases smoothly with \(\beta\).

2. **Multi-volume stability:** the \(L=4,6,8\) curves are extremely close, suggesting the convex core does not immediately vanish as volume grows.

3. **What this supports in the analytic program:** any attempt to prove a BE lower bound for lattice YM has a plausible starting point: show the YM Gibbs measure concentrates inside (or mostly inside) this convex chart, then invoke the curvature-to-gap pipeline.

---

## 4. Critical caveat: pointwise convexity \(\neq\) equilibrium concentration

The convexity scan samples \(A\)-coordinates from an *ad hoc* Gaussian. That is **not** the equilibrium YM distribution.

To connect to mass-gap claims you need a second step:

- **Sample the true lattice distribution in \(U\)-space** (links distributed by Haar with Wilson weight),
- Then map \(U\mapsto A\) via a principal logarithm chart,
- Then measure \(\lambda_{\min}(\nabla^2 S)\) (or at least check how often samples lie inside the convex region).

This separation (local convexity vs measure concentration) is exactly why a naive Metropolis in \(A\)-space can give misleading “typical norms.”

---

## 5. One clean next step (computationally decisive)

Run a link-based (\(U\)-space) Markov chain at several \(\beta\), gather samples, then compute:

\[
\mathbb{P}_{\mu_{\beta}}\big( A(U) \in \mathcal{C}_{\beta} \big)
\]
where \(\mathcal{C}_{\beta}\) is the convex core defined by \(\lambda_{\min}(\nabla^2 S)\ge 0\).

If that probability stays bounded away from 0 uniformly in volume in some \(\beta\)-window, you have real evidence for a curvature-based initialization regime.
