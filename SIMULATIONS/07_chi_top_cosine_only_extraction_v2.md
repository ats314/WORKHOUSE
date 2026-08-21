# \(\chi_{\mathrm{top}}\) from Cosine-Only Fourier Extraction: Low Modes, Correct Signs, and Sanity Checks

This note is about extracting the curvature
\[
F''(0),\qquad F(\theta)\equiv-\log Z(\theta),
\]
from discrete \(\theta\)-scan data in a way that:

- enforces \(2\pi\)-periodicity,
- enforces \(CP\) evenness (\(F(\theta)=F(-\theta)\)),
- avoids “high-harmonic hallucinations” unless the data truly demand them.

---

## 1. Why cosine-only is the right basis (when \(CP\) is intact)

If the theory has integer topological charge \(Q\in\mathbb{Z}\),
\[
Z(\theta)=\sum_Q Z_Q\,e^{i\theta Q},
\]
then complex conjugation gives \(Z(-\theta)=Z(\theta)^*\).  
For real free energy \(F(\theta)\), this implies
\[
F(\theta)=F(-\theta),
\]
so the Fourier series contains **cosines only**:
\[
F(\theta)=a_0+\sum_{n\ge 1} a_n\cos(n\theta).
\]

If your numerics violate this symmetry, *do not* “fit sines to fix it”.  
Instead, treat it as a diagnostic: something is broken (or you are taking \(|Z|\) in a way that creates nonanalytic kinks).

---

## 2. The money formula: \(F''(0)\) in terms of cosine modes

From
\[
F(\theta)=a_0+\sum_{n\ge 1} a_n\cos(n\theta),
\]
we have
\[
F''(\theta)= -\sum_{n\ge 1} a_n\,n^2\cos(n\theta),
\]
hence
\[
\boxed{\;F''(0)= -\sum_{n\ge 1} a_n\,n^2\;}.
\]

So: **watch the sign**.
If \(a_1<0\), it contributes **positively** to \(F''(0)\).

If you define \(\chi_{\mathrm{top}}\equiv \tfrac{1}{V}F''(0)\), then
\[
\chi_{\mathrm{top}} = -\frac{1}{V}\sum_{n\ge 1} a_n\,n^2.
\]

---

## 3. Discrete extraction on an equally spaced grid

Given sampled values \(\{(\theta_k,F_k)\}\) with \(\theta_k\in[0,2\pi)\), build a cosine-only design matrix:

\[
X_{k,0}=1,\qquad X_{k,n}=\cos(n\theta_k)\quad (n=1,\dots,N).
\]

Solve least squares:
\[
\hat a = \operatorname*{argmin}_a \|Xa-F\|_2^2.
\]

Then estimate
\[
\widehat{F''(0)} = -\sum_{n=1}^N \hat a_n\,n^2.
\]

### 3.1 Code snippet (cosine-only LS)

```python
import numpy as np

def cosine_only_fit(thetas, F, N):
    X = np.column_stack([np.ones_like(thetas)] + [np.cos(n*thetas) for n in range(1, N+1)])
    a, *_ = np.linalg.lstsq(X, F, rcond=None)
    return a  # a[0]=a0, a[n]=a_n

def Fpp0_from_cos_coeffs(a):
    return -sum(a[n]*(n**2) for n in range(1, len(a)))
```

---

## 4. Two practical “symmetry enforcement” tricks

### 4.1 Evenness symmetrization (cheap and usually worth it)

If your scan includes both \(\theta\) and \(2\pi-\theta\),
replace data by
\[
F_{\mathrm{even}}(\theta)=\frac{F(\theta)+F(2\pi-\theta)}{2}.
\]

This kills odd contamination without inventing sine physics.

### 4.2 Avoid roots of unity when using \(q=e^{i\theta}\)

If you compute a quantum \(6j_q\) via \([n]_q=\sin(n\theta)/\sin\theta\), then for rational points where \(\sin(n\theta)\approx 0\) (with small \(n\) inside your factorial range), the \(q\)-factorials can blow up or underflow catastrophically.

A very effective hack for scans is to use a **half-step shifted grid**
\[
\theta_k=\frac{2\pi}{N_\theta}\left(k+\tfrac{1}{2}\right),
\]
plus a separate evaluation at \(\theta=0\) if you need it.

This avoids sampling exactly at \(\theta=\pi/2,\,2\pi/3,\,\pi,\dots\) where small \([n]_q\) can cause numerical drama.

---

## 5. “Low-mode” means you are making a physics assumption

Truncating at small \(N\) assumes that higher harmonics are either:

- physically small (e.g., nearly-Gaussian \(Q\) distribution), or
- numerical artifacts you intend to suppress.

That is not automatically true. Therefore:

- report \(\widehat{F''(0)}\) for \(N=1,2,3\) and check stability,
- cross-check against a local finite-difference estimate near \(\theta=0\),
\[
F''(0)\approx \frac{F(h)-2F(0)+F(-h)}{h^2}.
\]

If the finite-difference result and the low-mode result disagree strongly, that’s not a “fit problem”; it’s your model telling you it has significant high-harmonic structure (or nonanalytic features), i.e. *numerics may be screaming*.

---

## 6. Recommended reporting template

Given a full scan, report:

1. scan parameters (\(j_{\max}\), HOTRG steps, grid choice, normalization),
2. evenness violation \(\max_\theta |F(\theta)-F(2\pi-\theta)|\),
3. cosine-only \(N=1,2,3\) estimates of \(F''(0)\),
4. local finite-difference \(F''(0)\) near \(0\),
5. whether these are mutually consistent.

That’s the minimum needed to tell “topology talking” from “numerics screaming”.
