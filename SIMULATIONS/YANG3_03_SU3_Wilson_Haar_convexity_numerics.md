# SU(3) Wilson+Haar Convexity Windows: Derivations and Numerical Evidence

## Abstract

In exponential link coordinates \(U_\ell=\exp(iA_\ell)\), the lattice SU(3) path integral measure contains a **Haar Jacobian** \(J(A_\ell)\) whose logarithm contributes a **quadratic “geometric mass”** near the identity. The Wilson plaquette action introduces curvature that grows with \(\beta\) and becomes negative away from the origin in field space. The YANG 3 project implements:

- automatic differentiation Hessians (small lattices),
- Hessian–vector products + Lanczos (larger lattices),
- random small-field sampling and convexity scans,

to estimate the **minimal Hessian eigenvalue**
\(\lambda_{\min}(\nabla^2 S_{\beta}(A))\) and an empirical **static convexity radius** \(R(\beta)\).

This document compiles the key derivations, code patterns, and results.

---

## 1. Haar Jacobian \(\Rightarrow\) quadratic curvature at the vacuum

For a compact Lie group \(G\) with exponential coordinates \(U=\exp(iA)\), Haar measure can be written as
\[
dU = J(A)\, dA.
\]

Near the identity,
\[
-\log J(A) = c_0\,\mathrm{Tr}(A^2) + O(\|A\|^4),
\qquad c_0>0.
\]

Interpretation:

- In the effective action \(S_{\mathrm{eff}}(A)=S_W(A)-\sum_\ell\log J(A_\ell)\), the Haar term contributes a genuine positive quadratic form.
- In the project’s lattice units, this appears as a per-link quadratic coefficient often denoted \(c_0\) (e.g. values like \(0.125\) or \(0.25\) depending on normalization).

---

## 2. Wilson action: curvature erosion away from the origin

The Wilson plaquette action is
\[
S_W(U)=\beta\sum_{p}\left(1-\frac{1}{N}\mathrm{Re\,Tr}(U_p)\right).
\]

In the numerics, the **Hessian at the exact vacuum** (all links \(A=0\)) is dominated by the Haar quadratic term, suggesting that in these coordinates the Wilson contribution is extremely small (or cancels at leading order) at the origin, but becomes nontrivial for finite-amplitude link fields.

A useful empirical ansatz extracted from scans is:
\[
\lambda_{\min}(A)
\approx c_0 - C\,\beta\, r^2,
\qquad r\sim \|A\|_\infty,
\]
which implies a static convexity radius
\[
\boxed{
R(\beta)\approx \sqrt{\frac{c_0}{C\beta}}.
}
\]

---

## 3. Key numerical results (from project logs)

The strongest convexity evidence in the SU(3) lattice experiments comes in three layers:

1. **Vacuum Hessian**: exact \(A=0\) Hessians are positive with eigenvalues essentially equal to the Haar quadratic coefficient.
2. **Small-field random sampling**: drawing \(A\) from a Gaussian cloud \(N(0,\sigma^2)\) reveals a sharp amplitude threshold where \(\lambda_{\min}\) crosses zero.
3. **Lanczos convexity scans** at fixed sampling amplitude scale show convexity shrinking with \(\beta\).

### 3.1 Full Hessian at the vacuum (L=2 \(\Rightarrow\) 2\(^4\) lattice)

A direct JAX Hessian computation on the \(2^4\) lattice reports:

- \(n_{\mathrm{params}} = L^4 \cdot 4 \cdot (N^2-1) = 512\) (for SU(3)),
- the smallest Hessian eigenvalues at \(A=0\) cluster extremely tightly at the Haar value (e.g. \(\approx 0.25\) when \(c_0=0.25\)).

This is consistent with the statement that Haar provides a clean curvature “seed” at the vacuum.

### 3.2 β-scan on random configs: Wilson alone vs Wilson+Haar

A scan at fixed amplitude `scale = 0.1` draws random configurations and compares:

- \(\lambda_{\min}(\nabla^2 S_W)\) for Wilson alone,
- \(\lambda_{\min}(\nabla^2(S_W+S_{\mathrm{Haar}}))\) for Wilson+Haar.

Representative output (L=2, \(c_0=0.25\)):

- At \(\beta=0.5\): Wilson is negative but Wilson+Haar is positive (\(\sim 0.17\)–\(0.19\)).
- At \(\beta=1.0\): Wilson is negative and Wilson+Haar is still positive (\(\sim 0.11\)).
- At \(\beta=2.0\): Wilson is negative and Wilson+Haar becomes negative for this scale (\(\sim -0.02\) to \(-0.06\)).

Interpretation: **Haar shifts the spectrum upward**, but the Wilson curvature erosion grows with \(\beta\) at fixed amplitude.

### 3.3 σ-sweep at fixed β: locating the small-field convexity window

A particularly clean diagnostic is to fix \(\beta\) and compute \(\lambda_{\min}\) for samples
\(\theta\sim N(0,\sigma^2)\) in \(\mathbb{R}^{512}\).

Example: \(L=2\), \(\beta=2.0\), \(c_0=0.25\), 3 samples per \(\sigma\):

| \(\sigma\) | min \(\lambda_{\min}\) | mean \(\lambda_{\min}\) |
|---:|---:|---:|
| 0.00 | +0.2500 | +0.2500 |
| 0.02 | +0.1952 | +0.2005 |
| 0.05 | +0.1202 | +0.1234 |
| 0.10 | −0.0262 | −0.0217 |
| 0.20 | −0.3836 | −0.3456 |

This shows a sharp crossing between \(\sigma=0.05\) and \(\sigma=0.10\) (in this normalization), giving an operational notion of a **convexity window** in the typical-amplitude sense.

### 3.4 Convexity scan vs \(\beta\) and amplitude scale (Lanczos on Hessian–vector products)

A typical scan (labeled “Turbo Scan”) estimates \(\lambda_{\min}\) for random Gaussian field samples with amplitude scale `scale`:

| \(\beta\) | scale | \(\lambda_{\min}\) |
|---:|---:|---:|
| 0.40 | 0.05 | +0.100 |
| 0.40 | 0.10 | +0.030 |
| 0.40 | 0.15 | −0.087 |
| 1.00 | 0.05 | +0.088 |
| 1.00 | 0.10 | −0.017 |
| 2.00 | 0.05 | +0.059 |
| 2.00 | 0.10 | −0.080 |
| 3.00 | 0.05 | −0.043 |

Interpretation:

- for fixed \(\beta\), there is a **small-field region** where convexity holds,
- as \(\beta\) increases, the maximal convex scale shrinks.

### 3.5 Empirical convexity radii \(R(\beta)\) (bisection + Lanczos)

The project also records a bisection-style estimate of a radius \(R(\beta)\) such that \(\lambda_{\min}\ge 0\) for amplitudes below \(R\) (under the scan’s sampling protocol). A representative table:

| \(\beta\) | \(R(\beta)\) | inferred \(C_\beta = c_0/(\beta R(\beta)^2)\) |
|---:|---:|---:|
| 0.40 | 0.2449 | 5.22 |
| 0.80 | 0.1454 | 7.35 |
| 1.60 | 0.0808 | 11.95 |
| 3.20 | 0.0460 | 17.08 |

These are broadly consistent with \(R(\beta)\propto \beta^{-1/2}\) with a slowly varying \(C_\beta\).



### 3.1 Full Hessian at the vacuum (L=2 \(\Rightarrow\) 2\(^4\) lattice)

A direct JAX Hessian computation on the \(2^4\) lattice reports:

- \(n_{\mathrm{params}} = L^4 \cdot 4 \cdot (N^2-1) = 512\) (for SU(3)),
- the smallest Hessian eigenvalues at \(A=0\) cluster extremely tightly at the Haar value (e.g. \(\approx 0.25\) when \(c_0=0.25\)).

This is consistent with the statement that Haar provides a clean curvature “seed” at the vacuum.

### 3.2 Convexity scan vs \(\beta\) and amplitude scale (Lanczos on Hessian–vector products)

A typical scan (labeled “Turbo Scan”) estimates \(\lambda_{\min}\) for random Gaussian field samples with amplitude scale `scale`:

| \(\beta\) | scale | \(\lambda_{\min}\) |
|---:|---:|---:|
| 0.40 | 0.05 | +0.100 |
| 0.40 | 0.10 | +0.030 |
| 0.40 | 0.15 | −0.087 |
| 1.00 | 0.05 | +0.088 |
| 1.00 | 0.10 | −0.017 |
| 2.00 | 0.05 | +0.059 |
| 2.00 | 0.10 | −0.080 |
| 3.00 | 0.05 | −0.043 |

Interpretation:

- for fixed \(\beta\), there is a **small-field region** where convexity holds,
- as \(\beta\) increases, the maximal convex scale shrinks.

### 3.3 Empirical convexity radii \(R(\beta)\) (bisection + Lanczos)

The project also records a bisection-style estimate of a radius \(R(\beta)\) such that \(\lambda_{\min}\ge 0\) for amplitudes below \(R\) (under the scan’s sampling protocol). A representative table:

| \(\beta\) | \(R(\beta)\) | inferred \(C_\beta = c_0/(\beta R(\beta)^2)\) |
|---:|---:|---:|
| 0.40 | 0.2449 | 5.22 |
| 0.80 | 0.1454 | 7.35 |
| 1.60 | 0.0808 | 11.95 |
| 3.20 | 0.0460 | 17.08 |

These are broadly consistent with \(R(\beta)\propto \beta^{-1/2}\) with a slowly varying \(C_\beta\).

---

## 4. Minimal code patterns used in the scans

### 4.1 Sampling random small fields

```python
def sample_theta(L, scale, key):
    # theta has shape (L,L,L,L,4,8) for SU(3) algebra coords
    return scale * jax.random.normal(key, (L,L,L,L,4,8), dtype=jnp.float32)
```

### 4.2 Hessian–vector product (HVP) via JAX

```python
def hvp(flat_action, theta_flat, v):
    g = jax.grad(flat_action)(theta_flat)
    return jax.jvp(jax.grad(flat_action), (theta_flat,), (v,))[1]
```

### 4.3 Lanczos estimate of the minimal eigenvalue

The scan uses a Lanczos routine on the implicit linear operator \(v\mapsto H v\) defined by HVP. The key point: **no explicit Hessian matrix** is formed, enabling larger lattices than full Hessian builds.

---

## 5. How to interpret these results (and what remains open)

### What is solid

- The Haar Jacobian contributes a real quadratic curvature term near the vacuum.
- Numerically, the Hessian spectrum at \(A=0\) is dominated by this term.
- The Wilson term appears to erode curvature quadratically with amplitude, producing a shrinking convexity window as \(\beta\) increases.

### What is still conjectural / needs rigorous closure

- A **provable** operator-norm bound on \(\nabla^2 S_W(A)\) in the same exponential coordinates, of the form \(\|\nabla^2 S_W(A)\|\le C\beta \|A\|^2\) (or a correct variant).
- A proof that the convexity window can be made uniform enough along \(\beta(a)\to\infty\) after appropriate coarse-graining.
- A mathematically controlled statement relating the scan’s \(R(\beta)\) to a true convexity region in the full configuration space (as opposed to a sampling protocol artifact).

---

## 6. Suggested next numerical/analytic checks

1. **Gauge-mode separation**: identify whether negative directions are gauge artifacts or physical (in the chosen coordinates).
2. **Local vs global convexity**: compare \(\lambda_{\min}\) along structured directions (single-link, plane-wave modes) rather than random Gaussian samples only.
3. **Analytic bounding experiments**: measure \(\sup_{\|A\|_\infty\le r}\|\nabla^2 S_W(A)\|\) numerically and fit scaling constants to guide proofs.

