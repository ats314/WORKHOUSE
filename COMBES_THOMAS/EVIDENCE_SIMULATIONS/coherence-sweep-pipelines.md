# Coherence Sweep Pipelines for 4D Lattice Propagators

## Abstract

This note captures a **high-throughput, numerically stable pipeline** for diagnosing lattice propagators and extracting exponential decay rates in 4D:

- **Pipeline A:** Computes a norm-like quantity $C_0(\Delta_1)$ (a row-sum bound built from inverse FFT kernels) and a derived decay-rate lower bound $\eta_{\mathrm{DG}}$.
- **Pipeline B:** Extracts a “mass” $\kappa$ from real-space Green’s function samples along rays using a windowed slope estimator with geometric prefactor correction and finite-volume floor truncation.

Two aspects stand out as especially useful (and extendable):

1. **Streaming / no-full-copy design** (important for $L=128$ and beyond),
2. **Auto fallback**: retry on CPU when GPU OOM occurs (keeping the sweep alive rather than dying dramatically).

---

## 1. Free massive scalar kernel on a 4D torus

Let $d=4$ and lattice size $L^4$ with periodic boundary conditions.

Define the lattice momentum components using the standard “hat” convention
\[
\hat p_\mu(k)\;=\;2\sin\!\left(\frac{p_\mu}{2}\right),\qquad p_\mu=\frac{2\pi n_\mu}{L}.
\]
Then
\[
\hat p^2(k) \;=\;\sum_{\mu=1}^d \hat p_\mu(k)^2.
\]

A canonical free-field Green’s function in Fourier space is
\[
\widetilde G(k)\;=\;\frac{1}{m^2+\alpha\,\hat p^2(k)}.
\]
Real-space values are obtained by inverse FFT:
\[
G(x)\;=\;\mathcal{F}^{-1}[\widetilde G](x).
\]

---

## 2. Pipeline A: $C_0(\Delta_1)$ and a derived exponential rate

The pipeline constructs tensor-valued symbols of the form
\[
Q_{\mu\nu}(k)=\delta_{\mu\nu}\hat p^2(k)-\hat p_\mu(k)\hat p_\nu(k)
\]
and studies their inverse transforms
\[
K_{\mu\nu}(x)=\mathcal{F}^{-1}[Q_{\mu\nu}](x).
\]

A (conservative) coherence quantity is then formed from row-sums of absolute values:
\[
C_0(\Delta_1)\;\equiv\;\max_{\mu}\left(\sum_x\sum_\nu |K_{\mu\nu}(x)| \;-\; |K_{\mu\mu}(0)|\right),
\]
implemented by FFTing each $(\mu,\nu)$ symbol and summing absolute values, subtracting the “diagonal origin” term.

A derived decay-rate proxy is computed as
\[
\eta_{\mathrm{DG}}\;\equiv\;2\,\operatorname{arcsinh}\!\Bigg(\frac{\sqrt{m^2}}{2\sqrt{\alpha\,C_0(\Delta_1)}}\Bigg).
\]
In spirit, this is a **guaranteed-rate style quantity**: if you can control the operator norm (via $C_0$), you get an exponential decay parameter.

---

## 3. Pipeline B: ray-sampled $\kappa$ extraction with corrections

For a massive field in $d$ dimensions,
\[
G(r)\sim A\,r^{-\frac{d-1}{2}}e^{-\kappa r}.
\]
Thus
\[
\log|G(r)| + \frac{d-1}{2}\log r \;\approx\; \log A - \kappa r.
\]

The pipeline uses:
- ray sampling: $x=r\cdot \text{step}\pmod L$,
- windowed slope extraction: average finite differences of the corrected log,
- a **floor truncation**: stop using radii where $|G(r)|$ is near the finite-volume floor scale $\sim \frac{1}{m^2 L^d}$ (to avoid noise-dominated “fake plateaus”).

This is a pragmatic way to make $\kappa$ extraction reliable without copying the entire $L^4$ kernel back to CPU.

---

## 4. Results from a sweep (auto OOM-retry)

A sweep over $L\in\{64,96,128\}$ and $m^2\in\{0.1,0.2,0.3\}$ (with $d=4$, $\alpha=1$) produced:

| $L$ | backend | $m^2$ | $C_0(\Delta_1)$ | $\eta_{\mathrm{DG}}$ | max\_ratio\_dist0 | $\kappa_\mathrm{expected}$ |
|---:|:---:|---:|---:|---:|---:|---:|
| 64 | cuda | 0.1 | 87.298902 | 0.033843 | 0.130643 | 0.314925 |
| 64 | cuda | 0.2 | 87.298902 | 0.047860 | 0.136024 | 0.443568 |
| 64 | cuda | 0.3 | 87.298902 | 0.058613 | 0.141185 | 0.541097 |
| 96 | cuda | 0.1 | 103.673226 | 0.031056 | 0.130643 | 0.314925 |
| 96 | cuda | 0.2 | 103.673226 | 0.043918 | 0.136024 | 0.443568 |
| 96 | cuda | 0.3 | 103.673226 | 0.053787 | 0.141185 | 0.541097 |
| 128 | cpu | 0.1 | 116.282985 | 0.029324 | 0.130643 | 0.314925 |
| 128 | cpu | 0.2 | 116.282985 | 0.041469 | 0.136024 | 0.443568 |
| 128 | cpu | 0.3 | 116.282985 | 0.050787 | 0.141185 | 0.541097 |

The run also demonstrates the intended robustness behavior: **$L=128$ OOM’d on CUDA and was retried successfully on CPU**.

---

## 5. What’s potentially “new” here (as a research tool)

The pipeline is not inventing new physics, but it is a neat **numerical “instrument”**:

- It produces simultaneously:
  - a conservative bound-like number ($C_0$),
  - a derived guaranteed-rate proxy ($\eta_{\mathrm{DG}}$),
  - and an empirical $\kappa$ from real-space decay.
- It’s designed to keep working even when GPU memory becomes a hard constraint.

This makes it attractive as a **diagnostic harness** for:
- improved actions (testing rotational symmetry restoration),
- interacting theories (plug in measured propagators),
- gauge-fixed propagators (e.g., Landau gauge) where the same ray logic applies.

---

## 6. Next expansions

1. **Make the $\kappa$ outputs first-class.**  
   Ensure printed tables always include $\kappa_\text{axis}$, $\kappa_\text{diag}$ plateaus, window counts, and stop radii.

2. **Rotational symmetry “healing” scan.**  
   The project already hints at tuning a correction coefficient $c$; formalize it: optimize $c$ to minimize axis/diagonal discrepancy in the extracted $\kappa$.

3. **Bootstrap uncertainties.**  
   Wrap ray-plateau extraction in block bootstrap over ray directions to attach error bars to $\kappa$.

4. **Interacting scalar $\phi^4$ or gauge theory propagators.**  
   Replace $\widetilde G(k)$ with measured correlators and reuse the same extraction logic.
