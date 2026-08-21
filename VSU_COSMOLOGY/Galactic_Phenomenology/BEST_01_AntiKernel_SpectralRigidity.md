# BEST_01 — Anti-kernel Hankel-Spectral “Spectral Rigidity” Mapping (Galaxy Rotation Curves)

## 1. Input and observables

For each galaxy, the project uses the observed circular speed profile \(V_{\rm obs}(r)\) to define
\[
g_{\rm obs}(r) := \frac{V_{\rm obs}(r)^2}{r}.
\]

From the SPARC rotmod decomposition, the baryonic template is taken as
\[
V_b^2(r) := V_{\rm gas}^2(r) + V_{\rm disk}^2(r) + V_{\rm bul}^2(r),
\qquad
g_b(r) := \frac{V_b^2(r)}{r}.
\]

A per-galaxy amplitude \(A\) (mass-to-light proxy in the project pipeline) enters via
\[
V_{\rm pred}^2(r) = A\,r\,g_\mu(r),
\qquad
V_{\rm pred}(r) = \sqrt{A\,r\,g_\mu(r)}.
\]

---

## 2. Hankel-domain representation (axisymmetric disk sector)

The project expresses disk-sector accelerations using order-1 Hankel/Bessel transforms (kernel \(J_1\)):

- Forward:
\[
\widehat g(k) := \int_0^\infty dr\; r\,g(r)\,J_1(kr),
\]
- Inverse:
\[
g(r) := \int_0^\infty dk\; k\,\widehat g(k)\,J_1(kr),
\]
modulo numerical quadrature/finite-window choices (the code uses a discrete Hankel transform).

This is the stage on which the kernel modifications act.

---

## 3. Kernel switch: **screen** vs **anti**

The global-fit script introduces a one-parameter spectral multiplier \(M_\mu(k)\) and defines
\[
\widehat g_\mu(k) := M_\mu(k)\,\widehat g_b(k),
\qquad
g_\mu := \mathcal{H}_1^{-1}[\widehat g_\mu].
\]

### 3.1 Screened “Helmholtz/Yukawa” choice

The “screen” branch is
\[
M_{\rm screen}(k)=\frac{k^2}{k^2+\mu^2}.
\]

### 3.2 **Anti-kernel** (infrared-enhanced) choice

The “anti” branch is
\[
M_{\rm anti}(k)=\frac{k^2+\mu^2}{k^2}
=1+\left(\frac{\mu}{k}\right)^2.
\]

This is the central non-standard move: a **low-\(k\)** boost rather than suppression.

---

## 4. Continuous-operator analogue

Formally, in a setting where \((-\Delta)^{-1}\) corresponds to multiplication by \(1/k^2\) in the relevant spectral representation,
\[
M_{\rm anti}(k) = 1+\frac{\mu^2}{k^2}
\quad\Longrightarrow\quad
g_\mu = g_b + \mu^2(-\Delta)^{-1}g_b.
\]

This makes the “anti” mapping nonlocal in real space, with the nonlocality concentrated in an inverse-Laplacian piece.

(Where the project uses a discrete Hankel transform, this is the continuous analogue of the implemented multiplier.)

---

## 5. Code (minimal excerpt of the global-fit switch)

The project implements the kernel switch in the global-fit script by:

1. forward Hankel transform,
2. multiply by \(M_\mu(k)\),
3. inverse Hankel transform.

The kernel definition is the decisive line:
```python
def kernel_M(k, mu):
    if KERNEL == "screen":
        return (k*k) / (k*k + mu*mu)
    elif KERNEL == "anti":
        return (k*k + mu*mu) / (k*k)
```

---

## 6. Empirical record in the project: global-fit anti-kernel run

A global scan over \(\mu\) is performed and a best-fit \(\mu^\star\) is recorded alongside per-galaxy diagnostics.

### 6.1 Recorded best-fit scale (one-parameter global fit)

The anti-kernel run records:
\[
\mu^\star = 0.103646~{\rm kpc}^{-1},
\qquad
\ell^\star:=\frac{1}{\mu^\star}=9.6482~{\rm kpc}.
\]

The same run header records sample sizes:
\[
N_{\rm gal}=143,\qquad N_{\rm pts}=3646.
\]

### 6.2 Recorded median diagnostics across galaxies

The run records (over the galaxy sample used in the run):
\[
{\rm median}\left(\chi^2/{\rm dof}\right)=3.056,
\qquad
{\rm median}(A)=0.889698,
\qquad
{\rm median}({\rm RMS})=11.762~{\rm km/s}.
\]

---

## 7. Internal negative controls in the same simulation bundle

The run logs also record alternative kernel choices with very poor performance compared to anti-kernel:

- `kernel avg (convex)`:
  \[
  \chi^2/{\rm dof}=380.288,
  \quad
  {\rm outer\ residual\ sign:\ fraction\ positive}=0.909.
  \]
- `kernel TRANSPORT`:
  \[
  \chi^2/{\rm dof}=234.414,
  \quad
  {\rm outer\ residual\ sign:\ fraction\ positive}=0.916.
  \]

This isolates the **infrared sign** of the spectral modification as a strong internal discriminator.

---

## 8. Baselines recorded in the same simulation bundle

In the same simulation bundle (same style of aggregated diagnostics), the logs record:

- Baryons only:
  \(\chi^2/{\rm dof}=620.69\).
- MOND “Simple”:
  \(\chi^2/{\rm dof}=57.0970\).
- MOND “Exponential / RAR”:
  \(\chi^2/{\rm dof}=58.1651\).

(These are recorded as separate model blocks from the anti-kernel run logs; the project contains multiple run blocks with different selections and diagnostics.)

---

## 9. Why this is a novelty candidate inside the project

The novelty is not in standard MOND-like algebra; it is in:

1. A **single global** spectral scale \(\mu\) combined with an **IR-enhanced** multiplier \(1+\mu^2/k^2\),
2. A strong internal contrast: the sign-flipped kernel families (`screen`, `avg`, `transport`) fail badly in the same pipeline,
3. A plausible mathematical bridge to codimension-2 log Green functions via inverse-Laplacian structure (expanded in **BEST_02**).

---

## Source pointers (project-local)

- `GEMINI CHAT.txt` (anti-kernel run summary outputs; median diagnostics).
- `GALAXY RUN.pdf` (anti-kernel run header reporting \(\mu^\star\), \(\ell^\star\), and sample size).
- `GALAXYRUN.ipynb` cell containing `sparc_rigidity_HANKEL_KERNEL_SWITCH.py` (kernel definitions and global fit setup).
- `GALAXY RUNS.pdf` (baseline and negative-control model summary blocks).
