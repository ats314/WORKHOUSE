# E. SU(3) Convexity Scanner: Code, Results, and an Empirical Wilson Constant

This document collects the most *actionable* numerical work in the project:

- A GPU-friendly **SU(3) convexity scanner**: estimate \(\lambda_{\min}\bigl(\nabla^2 S_{\rm eff}\bigr)\) using HVP + Lanczos.
- The full scan results on \(L=4,6,8\).
- A derived “effective constant” \(C_{\rm eff}(\beta)\) from the convexity boundary.
- A corrected plan for numerically estimating the **local Wilson Hessian constant** \(C_W\).

---

## E1. What is being measured?

In algebra coordinates (exponential chart) \(U_\ell=\exp(A_\ell)\), define the effective action
\[
S_{\rm eff}(A) = \sum_{\ell} S_{\rm Haar}(A_\ell) + \beta \sum_p S_W(U_p(A)).
\]

For a sampled configuration \(A\), measure the smallest eigenvalue
\[
\lambda_{\min}(A) := \lambda_{\min}\bigl(\nabla^2 S_{\rm eff}(A)\bigr).
\]

**Interpretation.**
- If \(\lambda_{\min}(A)>0\) throughout a domain \(\mathcal{C}\), then \(S_{\rm eff}\) is strongly convex on \(\mathcal{C}\), hence Bakry–Émery curvature \(\rho>0\) on \(\mathcal{C}\).
- The scan probes a *controlled-amplitude family* by sampling \(A_\ell\sim \mathcal{N}(0,\sigma^2 I)\) (with \(\sigma=\) `scale`) and taking the empirical minimum over samples.

This is **not** sampling the true YM measure; it is mapping the *geometry of the action*.

---

## E2. The core numerical method (HVP + Lanczos)

To avoid forming the full Hessian, estimate \(\lambda_{\min}\) via a Lanczos iteration using Hessian-vector products:
\[
Hv = \nabla^2 S_{\rm eff}(A)\,v.
\]

In JAX, an HVP can be computed efficiently as:
- `grad_S = jax.grad(S)`
- `hvp(v) = jax.jvp(grad_S, (theta,), (v,))[1]`

Then Lanczos uses only repeated `hvp(v)` calls.

---

## E3. The scan results (full tables)

All runs below used:
- SU(3) Padé(2,2) approximation for \(\exp(A)\),
- Haar quadratic coefficient set to `c0 = 0.125` in the code’s normalization,
- 8 β values: `linspace(0.4, 3.0, 8)`,
- 3 amplitude scales: \(0.05, 0.10, 0.15\),
- small sample counts per grid point (as logged).

The tables record the reported **minimum Hessian eigenvalue**.



### L=4 full scan (Padé22 exp, Haar coefficient c0=0.125)

| β | scale | λ_min |
|---:|---:|---:|
| 0.40 | 0.050 | +0.107639 |
| 0.40 | 0.100 | +0.084942 |
| 0.40 | 0.150 | +0.060163 |
| 0.77 | 0.050 | +0.090999 |
| 0.77 | 0.100 | +0.049703 |
| 0.77 | 0.150 | +0.000575 |
| 1.14 | 0.050 | +0.074027 |
| 1.14 | 0.100 | +0.011488 |
| 1.14 | 0.150 | -0.063704 |
| 1.51 | 0.050 | +0.058620 |
| 1.51 | 0.100 | -0.028256 |
| 1.51 | 0.150 | -0.121915 |
| 1.89 | 0.050 | +0.042761 |
| 1.89 | 0.100 | -0.061317 |
| 1.89 | 0.150 | -0.172886 |
| 2.26 | 0.050 | +0.024951 |
| 2.26 | 0.100 | -0.097842 |
| 2.26 | 0.150 | -0.229981 |
| 2.63 | 0.050 | +0.006105 |
| 2.63 | 0.100 | -0.131974 |
| 2.63 | 0.150 | -0.287083 |
| 3.00 | 0.050 | -0.008208 |
| 3.00 | 0.100 | -0.172180 |
| 3.00 | 0.150 | -0.376565 |

### L=6 full scan (Padé22 exp, Haar coefficient c0=0.125)

| β | scale | λ_min |
|---:|---:|---:|
| 0.40 | 0.050 | +0.108966 |
| 0.40 | 0.100 | +0.087381 |
| 0.40 | 0.150 | +0.063117 |
| 0.77 | 0.050 | +0.093839 |
| 0.77 | 0.100 | +0.052703 |
| 0.77 | 0.150 | +0.006658 |
| 1.14 | 0.050 | +0.079105 |
| 1.14 | 0.100 | +0.016544 |
| 1.14 | 0.150 | -0.052778 |
| 1.51 | 0.050 | +0.063542 |
| 1.51 | 0.100 | -0.017121 |
| 1.51 | 0.150 | -0.111918 |
| 1.89 | 0.050 | +0.048837 |
| 1.89 | 0.100 | -0.056489 |
| 1.89 | 0.150 | -0.173765 |
| 2.26 | 0.050 | +0.033850 |
| 2.26 | 0.100 | -0.085747 |
| 2.26 | 0.150 | -0.232562 |
| 2.63 | 0.050 | +0.018730 |
| 2.63 | 0.100 | -0.120620 |
| 2.63 | 0.150 | -0.278895 |
| 3.00 | 0.050 | +0.003391 |
| 3.00 | 0.100 | -0.154899 |
| 3.00 | 0.150 | -0.348172 |

### L=8 full scan (Padé22 exp, Haar coefficient c0=0.125)

| β | scale | λ_min |
|---:|---:|---:|
| 0.40 | 0.050 | +0.109207 |
| 0.40 | 0.100 | +0.087311 |
| 0.40 | 0.150 | +0.062942 |
| 0.77 | 0.050 | +0.094372 |
| 0.77 | 0.100 | +0.053147 |
| 0.77 | 0.150 | +0.004519 |
| 1.14 | 0.050 | +0.078979 |
| 1.14 | 0.100 | +0.015042 |
| 1.14 | 0.150 | -0.051065 |
| 1.51 | 0.050 | +0.065228 |
| 1.51 | 0.100 | -0.016862 |
| 1.51 | 0.150 | -0.107826 |
| 1.89 | 0.050 | +0.049413 |
| 1.89 | 0.100 | -0.051518 |
| 1.89 | 0.150 | -0.165610 |
| 2.26 | 0.050 | +0.036033 |
| 2.26 | 0.100 | -0.089054 |
| 2.26 | 0.150 | -0.225723 |
| 2.63 | 0.050 | +0.020245 |
| 2.63 | 0.100 | -0.119307 |
| 2.63 | 0.150 | -0.277276 |
| 3.00 | 0.050 | +0.005785 |
| 3.00 | 0.100 | -0.158744 |
| 3.00 | 0.150 | -0.336072 |


---

## E4. Extracting the convexity boundary and an “effective constant”

A standard local convexity heuristic is:
\[
\nabla^2 S_{\rm Haar}(0)\ \approx\ c_0 I,
\qquad
\|\nabla^2 S_W(A)-\nabla^2 S_W(0)\|\ \lesssim\ C_W\,\|A\|^2,
\]
so that
\[
\nabla^2 S_{\rm eff}(A)\ \succeq\ \bigl(c_0 - \beta C_W \|A\|^2\bigr)I
\]
on a core ball.

This predicts a convexity radius scaling:
\[
R_{\rm conv}(\beta) \sim \sqrt{\frac{c_0}{\beta C_W}}.
\]

We can invert this empirically:
- interpolate in **scale** between 0.05 and 0.10 (or 0.10 and 0.15) where \(\lambda_{\min}\) crosses 0,
- treat that interpolated scale as \(r^*(\beta)\),
- estimate
\[
C_{\rm eff}(\beta) := \frac{c_0}{\beta (r^*(\beta))^2}.
\]

This is not a proof, but it is a **data-driven calibration** of the constant in the convexity inequality.



### Convexity boundary by interpolating in scale (L=6)

| β | λ_min(scale=0.05) | λ_min(scale=0.10) | λ_min(scale=0.15) | estimated r* where λ_min≈0 | C_eff = c0/(β r*^2) |
|---:|---:|---:|---:|---:|---:|
| 0.40 | +0.108966 | +0.087381 | +0.063117 | >=0.150 (all tested scales convex) | — |
| 0.77 | +0.093839 | +0.052703 | +0.006658 | >=0.150 (all tested scales convex) | — |
| 1.14 | +0.079105 | +0.016544 | -0.052778 | 0.11193 | 8.75 |
| 1.51 | +0.063542 | -0.017121 | -0.111918 | 0.08939 | 10.36 |
| 1.89 | +0.048837 | -0.056489 | -0.173765 | 0.07318 | 12.35 |
| 2.26 | +0.033850 | -0.085747 | -0.232562 | 0.06415 | 13.44 |
| 2.63 | +0.018730 | -0.120620 | -0.278895 | 0.05672 | 14.77 |
| 3.00 | +0.003391 | -0.154899 | -0.348172 | 0.05107 | 15.97 |

### Convexity boundary by interpolating in scale (L=8)

| β | λ_min(scale=0.05) | λ_min(scale=0.10) | λ_min(scale=0.15) | estimated r* where λ_min≈0 | C_eff = c0/(β r*^2) |
|---:|---:|---:|---:|---:|---:|
| 0.40 | +0.109207 | +0.087311 | +0.062942 | >=0.150 (all tested scales convex) | — |
| 0.77 | +0.094372 | +0.053147 | +0.004519 | >=0.150 (all tested scales convex) | — |
| 1.14 | +0.078979 | +0.015042 | -0.051065 | 0.11138 | 8.84 |
| 1.51 | +0.065228 | -0.016862 | -0.107826 | 0.08973 | 10.28 |
| 1.89 | +0.049413 | -0.051518 | -0.165610 | 0.07448 | 11.92 |
| 2.26 | +0.036033 | -0.089054 | -0.225723 | 0.06440 | 13.33 |
| 2.63 | +0.020245 | -0.119307 | -0.277276 | 0.05725 | 14.50 |
| 3.00 | +0.005785 | -0.158744 | -0.336072 | 0.05176 | 15.55 |


**What jumps out:**
- For \(L=6\) and \(L=8\), at larger \(\beta\), the inferred \(C_{\rm eff}\) sits in the ballpark **\(\sim 14\)–\(17\)** (under the code’s normalization).
- The boundary is consistent across \(L=4,6,8\), suggesting it is not a tiny-volume artifact.

---

## E5. Plotting code to compare \(L\)

```python
import numpy as np
import matplotlib.pyplot as plt

betas = np.array([0.40,0.77,1.14,1.51,1.89,2.26,2.63,3.00])

L4 = np.array([0.107639,0.090999,0.074027,0.058620,0.042761,0.024951,0.006105,-0.008208])
L6 = np.array([0.108966,0.093839,0.079105,0.063542,0.048837,0.033850,0.018730,0.003391])
L8 = np.array([0.109207,0.094372,0.078979,0.065228,0.049413,0.036033,0.020245,0.005785])

plt.figure()
plt.plot(betas, L4, marker='o', label='L=4')
plt.plot(betas, L6, marker='o', label='L=6')
plt.plot(betas, L8, marker='o', label='L=8')
plt.axhline(0.0)
plt.xlabel('β')
plt.ylabel('min Hessian eigenvalue λ_min')
plt.title('Convexity scan at scale=0.05 (SU(3), Padé22)')
plt.legend()
plt.show()
```

---

## E6. The “RG/flow curvature repair” test (what the logs actually show)

A simple diagnostic is to run a short gradient flow on the (chart) action and track \(\lambda_{\min}\).

One recorded run (L=8, β=3.0, scale=0.15) showed:

- initial \(\lambda_{\min} \approx -0.350\),
- monotone improvement to \(\lambda_{\min} \approx -0.039\) by \(t=0.2\),
- **but it did not cross to positive within that window**.

So: **curvature improves**, but “guaranteed finite-time restoration” is not yet numerically established.

Example output snippet:

```
Step  0 (t=0.000): lambda_min = -0.350166 [UNSTABLE]
Step  2 (t=0.010): lambda_min = -0.323933 [UNSTABLE]
...
Step 40 (t=0.200): lambda_min = -0.039456 [UNSTABLE]
```

This is consistent with “flow helps”, but not yet a proof or universal phenomenon.

---

## E7. A corrected numerical estimator for \(C_W\)

### The key fix
A naive attempt that computes
\[
\frac{\|\nabla^2 S_W(A)\|}{\beta r^2}
\]
will blow up like \(1/r^2\) as \(r\to 0\), because \(\nabla^2 S_W(0)\neq 0\).

The correct quantity for the **increment bound** is
\[
\frac{\|\nabla^2 S_W(A) - \nabla^2 S_W(0)\|_{\rm op}}{\beta r^2}.
\]

### Practical estimator (HVP + power iteration)

Below is a **drop-in estimator pattern**:

- sample \(A\) with \(\|A\|_\infty\le r\),
- define \(M(A) := H(A)-H(0)\),
- estimate \(\|M(A)\|_{\rm op}\) via power iteration using only HVPs of \(H(A)\) and \(H(0)\).

```python
import jax
import jax.numpy as jnp

def hvp_of_action(action_fn, theta, v):
    # H(theta) v
    g = jax.grad(action_fn)
    return jax.jvp(g, (theta,), (v,))[1]

def opnorm_power_iteration(hvp_M, key, dim, n_iter=30):
    # estimate ||M||_op for symmetric M using power iteration
    v = jax.random.normal(key, (dim,))
    v = v / (jnp.linalg.norm(v) + 1e-12)
    for _ in range(n_iter):
        w = hvp_M(v)
        nw = jnp.linalg.norm(w) + 1e-12
        v = w / nw
    # Rayleigh quotient for final v
    w = hvp_M(v)
    return jnp.abs(jnp.vdot(v, w))

def estimate_CW(action_fn, theta_sampler, beta, r, key,
                n_samples=16, n_iter=30):
    # theta_sampler(key, r) returns a theta with ||A||_inf <= r
    dim = theta_sampler(key, r).shape[0]

    # reference Hessian operator at 0
    theta0 = jnp.zeros((dim,))
    def hvp0(v): return hvp_of_action(action_fn, theta0, v)

    cws = []
    k = key
    for i in range(n_samples):
        k, kA, kPI = jax.random.split(k, 3)
        theta = theta_sampler(kA, r)
        def hvpA(v): return hvp_of_action(action_fn, theta, v)
        def hvpM(v): return hvpA(v) - hvp0(v)

        opn = opnorm_power_iteration(hvpM, kPI, dim, n_iter=n_iter)
        cws.append(opn / (beta * (r**2)))
    return float(jnp.max(jnp.array(cws))), cws
```

**Notes.**
- This estimates the operator norm of the Hessian increment using only HVPs (no huge VRAM hit).
- The estimate depends on the sampling distribution (you want worst-case directions, not typical ones).
- A good diagnostic is to run the estimator at several \(r\) and check it stabilizes (does not scale like \(1/r^2\)).

---

## E8. Why this matters

The scan results already provide a data-driven constant via the convexity boundary:
\[
C_{\rm eff}(\beta)\approx 14\text{–}17 \quad (\text{in the code normalization, at large }\beta).
\]

A direct \(C_W\) estimator is valuable because it:
- turns that “boundary fit” into a genuine operator norm estimate,
- de-risks the analytic constant-chasing: you know what constant you *should* be aiming for.

---
