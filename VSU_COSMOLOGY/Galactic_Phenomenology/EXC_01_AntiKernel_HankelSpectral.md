# EXC_01 — Anti-kernel Hankel-Spectral Model for Galaxy Rotation Curves

## What this document contains

A concrete phenomenological mapping
\[
g_b(r)\;\mapsto\;g_\mu(r)
\]
implemented in the project as a **Hankel-domain (Bessel) multiplier** with an **infrared boost**
\[
M(k)=1+\left(\frac{\mu}{k}\right)^2,
\]
together with its relationship to the disk Hankel representation used elsewhere in the project and the fit outputs recorded in the project transcripts.

**Primary sources:** `GALAXY RUNS.pdf`, `GALAXY RUN.pdf`, `GEMINI CHAT.txt`.

---

## 1. Observables and baryonic input

Given a galaxy with observed circular speed \(V_{\rm obs}(r)\), define
\[
g_{\rm obs}(r):=\frac{V_{\rm obs}(r)^2}{r}.
\]

The project scripts define a baryonic template
\[
V_b^2(r):=V_{\rm gas}^2(r)+V_{\rm disk}^2(r)+V_{\rm bul}^2(r),
\qquad
g_b(r):=\frac{V_b^2(r)}{r}.
\]

A per-galaxy amplitude parameter \(A\) (mass-to-light proxy) enters via
\[
V_{\rm pred}^2(r)=A\;r\;g_\mu(r),
\qquad
V_{\rm pred}(r)=\sqrt{A\;r\;g_\mu(r)}.
\]

---

## 2. Hankel representation used in the project (disk sector)

The project records a standard axisymmetric Hankel representation for disk acceleration profiles:
\[
g_N(r)=2\pi G \int_0^\infty dk\; J_1(kr)\;\hat\Sigma(k),
\qquad
\hat\Sigma(k)=\frac{1}{2\pi G}\int_0^\infty dr\; r\,g_N(r)\,J_1(kr).
\]

A **screened Helmholtz/Yukawa** modification is written by inserting the filter
\[
\frac{k^2}{k^2+\mu^2}:
\qquad
g_\mu(r)
=
2\pi G\int_0^\infty dk\;\frac{k^2}{k^2+\mu^2}\;J_1(kr)\;\hat\Sigma(k).
\]

---

## 3. The **anti-kernel** mapping implemented in the project

### 3.1 Definition in \(k\)-space

The alternate kernel choice labeled `anti` is implemented as a **multiplier**
\[
M(k)=\frac{k^2+\mu^2}{k^2}=1+\left(\frac{\mu}{k}\right)^2.
\]

In the code path `KERNEL="anti"`, the transform-and-multiply structure is:

- forward Hankel transform (order-1, using \(J_1\)) of the baryonic profile,
- multiply by \(M(k)\),
- inverse Hankel transform to obtain \(g_\mu(r)\).

### 3.2 Minimal code excerpt (formatting-normalized)

```python
# Given dht.k, dht.w_k (quadrature weights), and dht.r grid:
Gb_k  = dht.forward(gbar_r)                # baryonic profile in k-space
M_k   = 1.0 + (mu / dht.k)**2              # anti kernel multiplier
gmu_k = Gb_k * M_k
gmu_r = dht.inverse(gmu_k)                 # modified profile in r-space
gmu_r = np.maximum(gmu_r, 1e-30)           # keep positive
```

---

## 4. Real-space interpretation (operator form)

The decisive feature is the \(\mu^2/k^2\) term. In any Fourier/Hankel representation where
\[
\widehat{(-\Delta)^{-1}f}(k)=\frac{1}{k^2}\hat f(k),
\]
the anti-kernel corresponds to the nonlocal operator
\[
g_\mu = g_b + \mu^2\,(-\Delta)^{-1}g_b.
\]

This is the same mathematical ingredient that produces **logarithmic Green’s functions** in codimension 2, and therefore \(1/r\) accelerations at large \(r\) (see EXC\_02).

*Note:* the project uses discrete Hankel transforms; the statement above is the continuous operator analogue.

---

## 5. Fit objective and per-galaxy amplitude handling (as encoded)

The global objective sums a weighted squared residual over galaxies and radii. A robust per-galaxy amplitude \(A\) is estimated via a median-based rule and clamped to a fixed interval to prevent extreme rescalings.

The global scale \(\mu\) is scanned on a log grid and \(\mu^\star\) is chosen by minimizing the global objective.

---

## 6. Recorded results for the anti-kernel run

The project transcript records:
\[
\mu^\star = 0.161395\ \mathrm{kpc}^{-1},
\qquad
\ell^\star=\frac{1}{\mu^\star}=6.19599\ \mathrm{kpc}.
\]

It also records median diagnostics across galaxies:
\[
\mathrm{median}\ \chi^2/\mathrm{dof}=3.056,
\qquad
\mathrm{median\ RMS}=11.8365\ \mathrm{km/s},
\qquad
\mathrm{median}\ A = 0.889698.
\]

(These values appear as literal printed output in `GEMINI CHAT.txt`.)

---

## 7. Negative controls recorded in the project runs

Two other kernel variants in the same run logs perform very poorly compared to the anti-kernel:

- `kernel avg (convex)`: \(\chi^2/\mathrm{dof}=380.288\), with strongly positive outer residual bias.
- `kernel TRANSPORT`: \(\chi^2/\mathrm{dof}=234.414\), also with strongly positive outer residual bias.

This makes the “infrared sign” of the modification a key discriminant in the project’s own pipeline.

