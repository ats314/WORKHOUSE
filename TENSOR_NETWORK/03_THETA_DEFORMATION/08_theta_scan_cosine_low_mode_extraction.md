# Full \(\theta\)-Scan + Cosine-Only Low-Mode Extraction of \(F''(0)\) (After 6j Tests Pass)

This note documents a “unit-test-first” \(\theta\)-scan workflow:

1. certify the \(6j\) kernel (24 symmetries + orthogonality),
2. run a full \(\theta\) scan,
3. extract \(F''(0)\) using cosine-only low modes,
4. cross-check with a local finite-difference curvature near \(\theta=0\).

The point is not to win a beauty contest with a fit — it’s to separate:
- **topology talking** (stable, symmetry-respecting curvature),
- from **numerics screaming** (grid-pathologies, root-of-unity singularities, nonanalytic kinks).

---

## 1. Preconditions: the \(6j\) kernel is certified

Before scanning \(\theta\), the following tests were required:

- invariance under the full 24-element tetrahedral orbit,
- canonicalization (if used) via orbit enumeration only,
- orthogonality sum rule at \(\theta=0\).

See `06_6j_correctness_and_symmetry_tests_v2.md` for the exact test code.

---

## 2. Scan setup

**Model:** q-deformed \(6j_q\) from a \(q\)-Racah formula with \([n]_q=\sin(n\theta)/\sin\theta\).  
**Vertex contraction:** simplified diagonal-style HOTRG-like contraction (project baseline).  
**Free energy:** \(F(\theta)=-\log|Z(\theta)|\) (magnitude log to keep \(F\) real).

### 2.1 Important numerical detail: half-step shifted grid

To avoid landing exactly on “roots of unity” where \(\sin(n\theta)=0\) for small \(n\),
the scan used:
\[
\theta_k = \frac{2\pi}{N_\theta}\left(k+\tfrac12\right),\quad k=0,\dots,N_\theta-1.
\]

On an unshifted grid, the same model shows catastrophic spikes near
\(\theta=\pi/2,\;2\pi/3,\;\pi\) because small \([n]_q\) enters \(q\)-factorials.

---

## 3. Extraction recipes

### 3.1 Cosine-only low-mode fit

Fit
\[
F(\theta)\approx a_0+\sum_{n=1}^N a_n\cos(n\theta),
\qquad
\widehat{F''(0)}=-\sum_{n=1}^N a_n n^2.
\]

### 3.2 Local finite-difference check

\[
F''(0)\approx \frac{F(h)-2F(0)+F(-h)}{h^2}.
\]

---

## 4. Results: a small smoke test (fast)

Parameters:

- \(j_\max = 1.0\) (spins \(j\in\{0,\tfrac12,1\}\))
- HOTRG steps: 4
- \(N_\theta=48\)
- runtime for full scan: 0.16 s
- \(F\) range over scan: \([-1.788188,\;2.281800]\)

Evenness diagnostic:
- max \(|F(\theta)-F(2\pi-\theta)|\) = \(1.577e-14\)
- mean evenness violation = \(2.229e-15\)

### 4.1 Global low-mode fit (full \([0,2\pi)\) data)

| truncation \(N\) | \(\widehat{F''(0)}\) |
|---:|---:|
| 1 | 0.971103 |
| 2 | 6.623745 |
| 3 | 1.146258 |

### 4.2 Local-window low-mode fit (\(\theta\in[0,0.5]\))

| truncation \(N\) | \(\widehat{F''(0)}\) |
|---:|---:|
| 1 | 1.748998 |
| 2 | 1.663202 |
| 3 | 1.666804 |

### 4.3 Finite difference

| \(h\) | finite-diff \(F''(0)\) |
|---:|---:|
| 0.02 | 1.666756 |
| 0.05 | 1.667223 |
| 0.10 | 1.668894 |

**Takeaway:** local-window cosine fits agree with finite differences; global low-mode fits can be unstable.

---

## 5. Results: a more realistic run (matches the project’s typical \(j_\max\))

Parameters:

- \(j_\max = 3.0\) (spins \(j\in\{0,\tfrac12,\dots,3.0\}\))
- HOTRG steps: 4
- \(N_\theta=48\)
- runtime for full scan: 17.46 s
- \(F\) range over scan: \([-3.312886,\;2.612202]\)

Evenness diagnostic:
- max \(|F(\theta)-F(2\pi-\theta)|\) = \(6.839e-14\)
- mean evenness violation = \(7.704e-15\)

### 5.1 Global low-mode fit (full \([0,2\pi)\) data)

| truncation \(N\) | \(\widehat{F''(0)}\) |
|---:|---:|
| 1 | 1.084261 |
| 2 | 6.580780 |
| 3 | 9.406867 |

### 5.2 Local-window low-mode fit (\(\theta\in[0,0.5]\))

| truncation \(N\) | \(\widehat{F''(0)}\) |
|---:|---:|
| 1 | 10.422245 |
| 2 | 8.766632 |
| 3 | 9.037555 |

### 5.3 Finite difference

| \(h\) | finite-diff \(F''(0)\) |
|---:|---:|
| 0.02 | 9.001801 |
| 0.05 | 9.011276 |
| 0.10 | 9.045423 |

**Takeaway:** again, the local-window cosine fit tracks the finite-difference curvature, while the global low-mode fit is not reliably stable in \(N\).

---

## 6. Interpretation: where “topology” might start, and where “numerics” definitely are

At this point you can say something narrow but solid:

- The \(6j\) kernel is symmetry-certified.
- A stable **local** estimate of \(F''(0)\) exists (windowed cosine fit \(≈\) finite difference).

You cannot yet say something big without more work:

- the **global** \(F(\theta)\) shape contains high-harmonic / nonanalytic structure that contaminates global low-mode fits,
- this may come from root-of-unity proximity, naive spin truncation, or taking \(|Z|\) (kinks at zeros).

The universe loves a clever hypothesis — but it loves a unit test suite even more.

---

## 7. Next hardening steps

1. **Root-of-unity hygiene:** track when \([n]_q\) gets tiny for the factorial range implied by your \(j_\max\).
2. **Regulator idea:** consider \(q=\exp(i\theta-\varepsilon)\) with small \(\varepsilon>0\) to avoid exact zeros.
3. **Physics-consistent truncation:** at roots of unity, enforce the finite-level representation cutoff (Turaev–Viro style) instead of a naive \(j_\max\).
4. **Upgrade contraction:** replace the simplified contraction with a proper HOTRG/SVD truncation that handles complex phases consistently.

That’s the road from “numerics screaming” to “topology talking.”
