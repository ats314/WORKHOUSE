# SU(3) Wilson+Haar Hessian scans: convexity window and stabilization evidence

This note summarizes and preserves the **high-value simulation outputs** from your SU(3) lattice Hessian code runs.

The key quantity is the smallest Hessian eigenvalue
\[
\lambda_{\min}(A)=\lambda_{\min}\bigl(\nabla^2(S_W+S_{\mathrm{Haar}})(A)\bigr)
\]
computed in exponential coordinates \(U_\ell=e^{A_\ell}\) using JAX automatic differentiation.

Positive \(\lambda_{\min}\) means local uniform convexity at that sampled configuration.

---

## 1. Core code structure (from the project)

The SU(3) simulation code includes:

- explicit \( \mathfrak{su}(3) \) generators and a differentiable exponential approximation,
- Wilson action evaluation from plaquettes,
- Haar “mass” term approximation \(c_0\sum_\ell \|A_\ell\|^2\),
- full Hessian by JAX `hessian(...)`,
- smallest eigenvalue by dense `eigvalsh`.

Representative snippet (abridged, preserved for reproducibility):

```python
# basis, exp approximation, Wilson action, Haar term, and Hessian eigenvalues
gens = su3_generators()
U = su3_exp_differentiable(A)   # Padé [1/1] unitary surrogate
Sw = wilson_action(U, beta=beta, L=L)
Sh = haar_mass(A, c0=c0)
S  = Sw + Sh

H = jax.hessian(lambda theta: total_action(theta, beta, L, c0))(theta0)
lam_min = jnp.linalg.eigvalsh(H).min()
```

---

## 2. Direct evidence: Haar term stabilizes negative Wilson curvature

A very clean diagnostic from your logs compares Hessians:

- Wilson-only Hessian \(\lambda_{\min}(S_W)\)
- Wilson+Haar Hessian \(\lambda_{\min}(S_W+S_{\mathrm{Haar}})\)

For random small-field configs on \(L=2\), scale \(=0.1\), \(c_0=0.25\), you recorded:

| \(\beta\) | \(\lambda_{\min}(S_W)\) | \(\lambda_{\min}(S_W+S_{\mathrm{Haar}})\) |
|---:|---:|---:|
| 0.5 | \(-0.0406\) | \(+0.2094\) |
| 1.0 | \(-0.0812\) | \(+0.1688\) |
| 2.0 | \(-0.1623\) | \(+0.0877\) |

In another random sample at \(\beta=2.0\), Wilson+Haar dipped slightly negative:
\(-0.0340\), indicating proximity to the convexity boundary.

**Interpretation:** Haar provides a robust positive shift, but does not guarantee convexity for all configs at higher \(\beta\) and larger amplitude.

---

## 3. Sigma sweep: convexity boundary in a random ensemble

For \(L=2\), \(\beta=2.0\), \(c_0=0.25\), you ran a sigma sweep where link coefficients were sampled with std \(\sigma\):

| \(\sigma\) | min \(\lambda_{\min}\) (across seeds) |
|---:|---:|
| 0.02 | \(+0.1953\) |
| 0.05 | \(+0.1205\) |
| 0.10 | \(-0.0266\) |
| 0.20 | \(-0.3834\) |

This is strong evidence for an ensemble-level convexity threshold near \(\sigma\sim 0.1\) at \(\beta=2\) in this small volume.

---

## 4. “Convexity grid” style scans (selected outputs)

### 4.1 L=3 scan (mean over 2 seeds)

You recorded (selected):

- scale \(0.05\): convex up to \(\beta=2.0\) with \(\lambda_{\min}\approx 0.20\to 0.13\),
- scale \(0.10\): convexity weakens and becomes negative around \(\beta\sim 1.6\),
- scale \(0.15\): convexity becomes negative earlier (around \(\beta\sim 1.6\)).

A subset of the log:

| \(\beta\) | scale 0.05 | scale 0.10 | scale 0.15 |
|---:|---:|---:|---:|
| 0.4 | 0.2065 | 0.1832 | 0.1482 |
| 1.0 | 0.1904 | 0.1421 | 0.0691 |
| 1.4 | 0.1748 | 0.0961 | 0.0140 |
| 1.6 | 0.1688 | 0.0808 | \(-0.0041\) |
| 2.0 | 0.1546 | 0.0517 | \(-0.0341\) |

---

### 4.2 L=8 “minimal slice” scan (1 seed)

This was particularly striking: for scale \(0.05\), you recorded positive \(\lambda_{\min}\) out to \(\beta=3.0\):

| \(\beta\) | \(\lambda_{\min}\) |
|---:|---:|
| 0.40 | 0.206243 |
| 1.20 | 0.182728 |
| 2.00 | 0.159029 |
| 3.00 | 0.006509 |

The \(\beta=3.0\) point is extremely close to zero but still positive in this run.

---

## 5. What these simulations *actually* did

### What they establish (as evidence)
1. In the tested random ensembles, the Haar term pushes the Hessian spectrum upward significantly.
2. There exists a nontrivial “convex basin” at small amplitude where \(\lambda_{\min}>0\) for Wilson+Haar, even at moderate \(\beta\).
3. The boundary is sensitive to both \(\beta\) and amplitude; the transition is sharp in \(\sigma\)-style ensembles.

### What they do *not* establish (yet)
1. A theorem-level lower bound \( \lambda_{\min}\ge \rho(\beta)>0\) holding for **all** configurations in a ball.
2. Volume-uniform convexity at fixed amplitude without additional analytic control.
3. A proof that a YM-relevant RG step will land inside the convex basin.

---

## 6. Immediate next steps (high leverage)

1. **Freeze a reproducible “benchmark suite”**:
   - fixed seeds,
   - fixed lattice sizes \(L=2,3,4,6,8\),
   - fixed scales and betas,
   - export \(\lambda_{\min}\) distributions, not only means.

2. **Turn scans into provable inequalities**:
   Use the clean \(C_W\) bound (`05_Wilson_Global_Hessian_Bound_CW.md`) to obtain a *guaranteed* (small) convexity region, then try to enlarge it by improving only the few pessimistic inequalities.

3. **Dynamic restoration tests**:
   Run gradient flow from explicitly nonconvex samples and log \(\lambda_{\min}(t)\) crossing time, to build a precise conjecture of the form
   \[
   \lambda'(t)\gtrsim 2\lambda(t)^2 \quad \text{in a controlled domain}.
   \]