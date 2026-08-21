# Global smooth plaquette Lyapunov drift from a fundamental-character proxy

## Scope

This note isolates a single move that (i) removes the cut-locus/nonsmoothness obstruction of plaquette distance-squared, and (ii) produces an *explicit*, volume-uniform drift identity for the pure Laplacian part of the configuration diffusion generator.

It is a clean, re-usable analytic lemma: it is not a full Yang–Mills proof by itself.

---

## 1. Replace the nonsmooth plaquette distance by a smooth conjugation-invariant proxy

Let \(G=\mathrm{SU}(N)\) with a fixed bi-invariant Riemannian metric, and let \(\Delta_G\) denote the associated Laplace–Beltrami operator on \(G\). (All constants below depend on the metric normalization, but the *structure* does not.)

For any \(U\in G\), define the smooth class function
\[
\widetilde z(U)\;:=\;1-\frac{1}{N}\,\Re\operatorname{Tr}(U)\in[0,2].
\]
This is globally \(C^\infty\), conjugation-invariant, vanishes only at the identity, and has quadratic growth near the identity:
\[
\widetilde z(\exp X)=c\,|X|^2+O(|X|^3).
\]

On a finite lattice region \(\Lambda\), with configuration manifold \(M_\Lambda=G^{E(\Lambda)}\) and product Laplacian \(\Delta_\Lambda=\sum_{\ell\in E(\Lambda)}\Delta_\ell\), define for each plaquette \(p\) the holonomy \(U_p(U)\in G\), and set
\[
\widetilde z_p(U)\;:=\;\widetilde z\!\big(U_p(U)\big).
\]
Define the averaged plaquette proxy and its affine shift:
\[
\overline z_\Lambda(U)\;:=\;\frac{1}{|P(\Lambda)|}\sum_{p\in P(\Lambda)}\widetilde z_p(U), 
\qquad
\overline V_\Lambda(U)\;:=\;1+\overline z_\Lambda(U).
\]
This is exactly the “globally smooth proxy” suggested in the analytic-engine bottleneck diagnosis (distance-square cut-locus issue).

---

## 2. The key Laplacian eigenfunction input

Assume (by definition of \(\lambda_{\mathrm{fund}}\) under your chosen metric normalization) that the *fundamental character* obeys
\[
\Delta_G\big(\Re\operatorname{Tr}(U)\big)\;=\;-\lambda_{\mathrm{fund}}\;\Re\operatorname{Tr}(U).
\tag{2.1}
\]
This is a representation-theoretic eigenfunction statement: \(\lambda_{\mathrm{fund}}>0\) is the quadratic-Casimir eigenvalue in the fundamental representation for the Laplacian convention you are using.

By linearity and \(\widetilde z(U)=1-\frac{1}{N}\Re\operatorname{Tr}(U)\),
\[
\Delta_G \widetilde z(U)= -\lambda_{\mathrm{fund}}\widetilde z(U)+\lambda_{\mathrm{fund}}.
\tag{2.2}
\]

---

## 3. Drift identity for the lattice product Laplacian

### Lemma 3.1 (Exact Laplacian drift for the smooth plaquette proxy)

Let \(U\mapsto \overline V_\Lambda(U)\) be defined as above. Under (2.1),
\[
\Delta_\Lambda \overline V_\Lambda
\;=\;
-\lambda\,\overline V_\Lambda\;+\;b,
\qquad
\lambda:=4\lambda_{\mathrm{fund}},
\qquad
b:=2\lambda=8\lambda_{\mathrm{fund}}.
\tag{3.1}
\]

#### Proof (structural; depends only on bi-invariance)

Fix a plaquette \(p\) with boundary links \(\ell_1,\ell_2,\ell_3,\ell_4\) (two of which appear inversely). For a given boundary link \(\ell\in\partial p\), freeze all other links and view \(U_p\) as a function of \(U_\ell\) alone:
\[
U_p(U)=A\,U_\ell\,B \quad\text{or}\quad U_p(U)=A\,U_\ell^{-1}\,B,
\]
for some fixed \(A,B\in G\) depending on the frozen links.

Because \(\Delta_G\) is bi-invariant, left and right translations are isometries and preserve the Laplacian. Also inversion is an isometry for a bi-invariant metric. Therefore the function
\[
U_\ell\longmapsto \Re\operatorname{Tr}(U_p(U))
\]
has the *same* Laplacian eigenvalue \(\lambda_{\mathrm{fund}}\) as \(U\mapsto \Re\operatorname{Tr}(U)\). Hence, for each \(\ell\in\partial p\),
\[
\Delta_\ell \widetilde z_p(U) = -\lambda_{\mathrm{fund}}\,\widetilde z_p(U)+\lambda_{\mathrm{fund}}.
\]
Summing over the four boundary links of \(p\),
\[
\sum_{\ell\in\partial p}\Delta_\ell \widetilde z_p
=
-4\lambda_{\mathrm{fund}}\widetilde z_p+4\lambda_{\mathrm{fund}}.
\]
Since \(\widetilde z_p\) depends only on \(\partial p\), all other \(\Delta_{\ell'}\) with \(\ell'\not\in\partial p\) annihilate it. Therefore
\[
\Delta_\Lambda \widetilde z_p
=
-4\lambda_{\mathrm{fund}}\widetilde z_p+4\lambda_{\mathrm{fund}}.
\]
Average over plaquettes and add the constant \(1\) (killed by \(\Delta_\Lambda\)):
\[
\Delta_\Lambda \overline V_\Lambda
=
\Delta_\Lambda\!\left(1+\frac{1}{|P|}\sum_p \widetilde z_p\right)
=
-\underbrace{4\lambda_{\mathrm{fund}}}_{\lambda}\cdot\frac{1}{|P|}\sum_p \widetilde z_p
+
4\lambda_{\mathrm{fund}}.
\]
Since \(\frac{1}{|P|}\sum_p \widetilde z_p=\overline V_\Lambda-1\), we get
\[
\Delta_\Lambda \overline V_\Lambda
=
-\lambda(\overline V_\Lambda-1)+\lambda
=
-\lambda\overline V_\Lambda+2\lambda.
\]
Thus \(b=2\lambda\), proving (3.1). \(\square\)

---

## 4. Why this is a useful “Lyapunov atom”

The analytic-engine bottleneck identified in the project is the uncontrolled term \(X_\ell^a X_\ell^a z_p\) when \(z_p=d_G(U_p,\mathbf 1)^2\), due to global nonsmoothness/cut-locus phenomena.

With \(\widetilde z_p(U)=1-\frac{1}{N}\Re\operatorname{Tr}(U_p)\):

* \(\widetilde z_p\) is \(C^\infty\) globally on compact \(G\), so all second derivatives along link vector fields are bounded uniformly.
* The Laplacian drift (3.1) is **exact**, not “up to remainder”, and its constants are **volume-uniform**.

This gives a canonical candidate for the “linear Lyapunov” hypothesis in the local-to-global Poincaré module when the generator’s Laplacian part is the dominant second-order contribution.

---

## 5. Empirical sanity check (JAX / GPU): fitting \(\lambda,b\) and testing drift sign

The following simulation was used to sanity-check the identity (3.1) *under the exact generator convention implemented in the simulator*, and then to test that the full Langevin generator drift \(L\overline V_\Lambda\) is strongly negative at large \(\beta\).

**Important:** this is not a proof. It is a debugging tool to lock the normalization and sign conventions.

### 5.1 Code (as used in the project chat)

```python
# drift_batch_check_fit.py
import jax
import jax.numpy as jnp
import jax.scipy.linalg as jsp
from functools import partial

def haar_suN(key, shape, N):
    k1, k2 = jax.random.split(key)
    z = (jax.random.normal(k1, shape + (N, N)) +
         1j * jax.random.normal(k2, shape + (N, N))) / jnp.sqrt(2.0)
    q, r = jnp.linalg.qr(z)
    phase = jnp.exp(-1j * jnp.angle(jnp.diagonal(r, axis1=-2, axis2=-1)))
    q = q * phase[..., None, :]
    detq = jnp.linalg.det(q)
    q = q / detq[..., None, None] ** (1.0 / N)
    return q

def suN_tangent_gaussian(key, shape, N):
    k1, k2 = jax.random.split(key)
    a = (jax.random.normal(k1, shape + (N, N)) +
         1j * jax.random.normal(k2, shape + (N, N))) / jnp.sqrt(2.0)
    x = a - jnp.conjugate(jnp.swapaxes(a, -1, -2))  # anti-Hermitian
    tr = jnp.trace(x, axis1=-2, axis2=-1) / N
    x = x - tr[..., None, None] * jnp.eye(N, dtype=x.dtype)  # traceless
    return x

def shift4(arr, axis, s):
    return jnp.roll(arr, shift=s, axis=axis)

def plaquette(U, mu, nu):
    U_mu = U[..., mu, :, :]
    U_nu = U[..., nu, :, :]
    U_mu_x_nu = shift4(U_mu, axis=nu, s=1)
    U_nu_x_mu = shift4(U_nu, axis=mu, s=1)
    U_mu_dag_x_nu = jnp.conjugate(jnp.swapaxes(U_mu_x_nu, -1, -2))
    U_nu_dag = jnp.conjugate(jnp.swapaxes(U_nu, -1, -2))
    return U_mu @ U_nu_x_mu @ U_mu_dag_x_nu @ U_nu_dag

def z_stack(U):
    N = U.shape[-1]
    z_list = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            Up = plaquette(U, mu, nu)
            tr = jnp.real(jnp.trace(Up, axis1=-2, axis2=-1))
            z_list.append(1.0 - (1.0 / N) * tr)
    return jnp.stack(z_list, axis=0)   # [6,L,L,L,L]

def zsum_and_Vbar(U):
    z_all = z_stack(U)
    z_sum = jnp.sum(z_all)       # sum over plaquettes and sites
    V = 1.0 + jnp.mean(z_all)    # 1 + average z
    return z_sum, V

@partial(jax.jit, static_argnums=(4,5,6))
def estimate_LV_one(U, beta, eps, key, mc_samples: int, N: int, L: int):
    def one_dir(k):
        Xi = suN_tangent_gaussian(k, (L, L, L, L, 4), N)
        exp_p = jsp.expm(eps * Xi)
        exp_m = jsp.expm(-eps * Xi)

        U_p = U @ exp_p
        U_m = U @ exp_m

        zsum_p, V_p = zsum_and_Vbar(U_p)
        zsum_0, V_0 = zsum_and_Vbar(U)
        zsum_m, V_m = zsum_and_Vbar(U_m)

        lap = (V_p + V_m - 2.0 * V_0) / (eps ** 2)

        if beta == 0.0:
            return lap

        S_p = beta * zsum_p
        S_m = beta * zsum_m

        dS = (S_p - S_m) / (2.0 * eps)
        dV = (V_p - V_m) / (2.0 * eps)
        return lap - dS * dV   # L V = ΔV - <∇S,∇V> in this estimator

    keys = jax.random.split(key, mc_samples)
    vals = jax.vmap(one_dir)(keys)
    return jnp.mean(vals), jnp.std(vals) / jnp.sqrt(mc_samples)

@partial(jax.jit, static_argnums=(4,5,6))
def run_batch(keysU, keysL, beta, eps, mc_samples: int, N: int, L: int):
    def one(kU, kL):
        U = haar_suN(kU, (L, L, L, L, 4), N)
        _, v = zsum_and_Vbar(U)
        lv, se = estimate_LV_one(U, beta=beta, eps=eps, key=kL,
                                 mc_samples=mc_samples, N=N, L=L)
        return v, lv, se
    return jax.vmap(one)(keysU, keysL)

def fit_lambda_b(v, delta_v):
    # least-squares fit of delta_v ≈ -lambda v + b
    A = jnp.stack([-v, jnp.ones_like(v)], axis=1)
    x, _, _, _ = jnp.linalg.lstsq(A, delta_v, rcond=None)
    lam, b = x[0], x[1]
    return lam, b

if __name__ == "__main__":
    N = 3
    L = 2
    eps = 5e-3
    mc = 256
    K = 64

    key = jax.random.PRNGKey(0)
    key, kU, kL = jax.random.split(key, 3)
    keysU = jax.random.split(kU, K)
    keysL = jax.random.split(kL, K)

    # beta=0: estimate Δ V and fit (λ,b)
    beta0 = 0.0
    v0, dv0, se0 = run_batch(keysU, keysL, beta0, eps, mc, N, L)
    lam_hat, b_hat = fit_lambda_b(v0, dv0)
    err = dv0 - (-lam_hat * v0 + b_hat)

    print("=== beta=0 fit (Delta V ≈ -lambda V + b) ===")
    print("lambda_hat =", float(lam_hat))
    print("b_hat      =", float(b_hat))
    print("mean(V)    =", float(jnp.mean(v0)))
    print("mean(err)  =", float(jnp.mean(err)))
    print("max|err|   =", float(jnp.max(jnp.abs(err))))
    print("mean SE    =", float(jnp.mean(se0)))

    # beta>0: test drift inequality L V ≤ -λ V + b with fitted λ,b
    beta = 6.0
    v, lv, se = run_batch(keysU, keysL, beta, eps, mc, N, L)
    rhs = -lam_hat * v + b_hat
    slack = rhs - lv

    print("\n=== beta>0 drift inequality check (using fitted lambda,b) ===")
    print("mean(V)            =", float(jnp.mean(v)))
    print("mean(L V)          =", float(jnp.mean(lv)))
    print("mean(RHS)          =", float(jnp.mean(rhs)))
    print("min slack (rhs-lv) =", float(jnp.min(slack)))
    print("mean slack         =", float(jnp.mean(slack)))
    print("mean SE(L V)       =", float(jnp.mean(se)))
```

### 5.2 Reported outputs (as observed)

```
=== beta=0 fit (Delta V ≈ -lambda V + b) ===
lambda_hat = 21.561948776245117
b_hat      = 43.12388229370117
mean(V)    = 2.0005226135253906
mean(err)  = -1.2785429134964943e-05
max|err|   = 0.0901908278465271
mean SE    = 0.02969277650117874

=== beta>0 drift inequality check (using fitted lambda,b) ===
mean(V)            = 2.0005226135253906
mean(L V)          = -7.094058036804199
mean(RHS)          = -0.011284738779067993
min slack (rhs-lv) = 5.618908405303955
mean slack         = 7.082773208618164
mean SE(L V)       = 0.44095945358276367
```

### 5.3 Interpretation (strictly limited)

* The \(\beta=0\) fit supports the *exact affine* structure \(\Delta \overline V_\Lambda = -\lambda \overline V_\Lambda + b\) under the simulator’s Laplacian normalization, with small residuals at the chosen finite-difference and Monte-Carlo resolution.
* The \(\beta>0\) outputs are consistent with the heuristic inequality
  \[
  L\overline V_\Lambda\;\le\;\Delta \overline V_\Lambda,
  \]
  i.e. the drift term \(-\langle \nabla S,\nabla \overline V_\Lambda\rangle\) being nonpositive on average for the Wilson action direction.

This supports using \(\overline V_\Lambda\) as a plausible Lyapunov seed function for the global drift module, with constants \((\lambda,b)\) pinned to the metric convention.

---

## 6. Immediate mathematical corollary direction (where this plugs in)

The local-to-global Poincaré module in the project has the following generic shape:

* local Poincaré/LSI on a “core” set \(K\),
* plus a global Lyapunov drift inequality of the form
  \[
  L W \le -\alpha W + \beta\,\mathbf 1_K,
  \]
  with \(\alpha,\beta\) uniform in volume,

\(\Rightarrow\) global Poincaré (and under stronger hypotheses, global LSI).

The lemma above gives an explicit and volume-uniform drift identity for the Laplacian part of \(L\), and makes the smooth-proxy choice \(\widetilde z\) technically natural.

