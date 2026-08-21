# Contracting the 4D tensor network and extracting $\chi_{\rm top}$ from $F(\theta)$

**Source notebooks:** `SU2_4D_PHASE2_FIXED.ipynb`, `SU2_4D_Rank8_FINAL.ipynb`, `gauge_theory_theta_scan.ipynb`

## 1. From a local tensor to a partition function

Given a local tensor $T$ on each vertex (or building block) of a regular lattice, the partition function is a full contraction of copies of $T$:

\[
Z(\theta) = \mathrm{tTr}\,\bigotimes_{\text{sites}} T(\theta),
\]
where $\mathrm{tTr}$ denotes contraction over all shared indices.

In practice, exact contraction in 4D is impossible for any nontrivial bond dimension, so the project uses a coarse-graining strategy in the spirit of HOTRG.

---

## 2. A simplified HOTRG step

For a rank-8 tensor with each index of dimension $D$, one convenient contraction step reshapes $T$ into a matrix by grouping 4 indices into “left” and 4 into “right”:

\[
T_{i_1 i_2 i_3 i_4 i_5 i_6 i_7 i_8}
\ \longrightarrow\
M_{(i_1 i_2 i_3 i_4),(i_5 i_6 i_7 i_8)}.
\]

Then perform an SVD:
\[
M = U\,\Sigma\,V^\dagger,
\]
truncate to a bond dimension $\chi$ by keeping only the largest $\chi$ singular values, and reshape back to rank 8.

This is not a full HOTRG implementation (which chooses optimized isometries along each direction), but it captures the key idea: iteratively compress degrees of freedom while controlling error via $\chi$.

---

## 3. Log-normalization and “free energy” extraction

Tensor contractions often overflow/underflow. The notebooks normalize at each step:

- compute $n = \max |T|$,
- replace $T \leftarrow T/n$,
- accumulate $\log n$ in a running “budget.”

After $N$ steps, this yields an estimate of $\log Z$ as the sum of the accumulated logs plus the final contraction value.

The free energy used in the notebooks is essentially:
\[
F(\theta) = -\Re\bigl(\log Z(\theta)\bigr),
\]
up to volume normalization (which depends on the exact coarse-graining scheme).

---

## 4. Why Fourier fitting is the right bias for $\chi_{\rm top}$

If CP symmetry holds, then $Z(\theta)=Z(-\theta)$ and $F(\theta)$ is an even function. Additionally, $\theta$ is an angle: physics is $2\pi$-periodic.

So a Fourier cosine series is the natural model class:
\[
F(\theta) \approx a_0 + \sum_{n=1}^{N} a_n \cos(n\theta).
\]

Then the second derivative at zero is
\[
F''(0) = -\sum_{n=1}^{N} n^2 a_n,
\]
so, up to the convention-dependent volume factor,
\[
\chi_{\rm top} \propto F''(0).
\]

### Polynomial fit vs Fourier fit

A quadratic fit near $\theta=0$,
\[
F(\theta)\approx c_0 + c_2 \theta^2,
\]
gives $F''(0)\approx 2c_2$.

This can work if sampling is dense near $0$ and higher-order terms are negligible. But it ignores periodicity and is sensitive to the chosen window.

A Fourier fit uses *all* $\theta$ values and enforces periodic structure, making it a better-conditioned estimator for $F''(0)$.

---

## 5. Diagnostics that matter

1. **Fit quality:** compare $R^2$ (or residuals) between polynomial and Fourier models.
2. **Evenness:** check $F(\theta)-F(-\theta)$ numerically.
3. **Stability in $\chi_{\max}$:** increase bond dimension $\chi_{\max}$; a physical result should stabilize.
4. **Stability in $j_{\max}$:** for spin truncation models, increase $j_{\max}$ and check convergence trend.
5. **Special angles:** inspect $\theta=\pi$ behavior separately; many models have non-analyticities or special structure there.

---

## 6. A sanity-check baseline: 2D $U(1)$ models

The project also contains a 2D $U(1)$ $\theta$-term implementation (both TRG-style and Monte Carlo). This is useful because:

- topological sectors are cleanly integer-valued in 2D $U(1)$,
- $Z(\theta)$ is explicitly a cosine series in the sector weights,
- $\chi_{\rm top}$ can also be computed directly as $\langle Q^2\rangle/V$.

Using the same Fourier extraction pipeline on this “known case” is a strong validation step for the analysis machinery.

---

## 7. Next steps

- Implement a direction-by-direction HOTRG (or an established library) to reduce artifacts from the simplified reshape-SVD-reshape scheme.
- Propagate truncation errors to uncertainties in $\chi_{\rm top}$.
- Validate $F(\theta)$ periodicity and evenness to high precision as a basic correctness test.

