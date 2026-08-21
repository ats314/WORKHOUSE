---
title: "Extract 06 — Numerical Sanity-Check: Green-Kernel Decay for a Discrete Massive Maxwell Operator"
project: "APPENDIX PROOF OUTLINE"
---

## What this is (and what it is not)

- **Not** a proof and **not** part of the manuscript’s logical chain.
- A small numerical illustration of the deterministic claim used in the proofs:
  operators of the form
  \[
  M = m^2\,\mathrm{Id} + \alpha\,d_1^*d_1
  \]
  have inverse kernels that decay rapidly with link-graph distance.

The manuscript’s rigorous route is Combes–Thomas / Davies (Appendix G / H).  
This file just checks the “shape” on a toy lattice.

---

## Experiment setup

- Dimension: 2D periodic lattice \(\mathbb Z_L^2\) with \(L=12\).
- Space: scalar 1-cochains on oriented edges (so each link variable is a scalar).
- Operator:
  \[
  M = m^2 I + \alpha d_1^*d_1
  \]
  with \(m^2=1\), \(\alpha=1\).
- Distance \(\mathrm{dist}_\mathcal E\): graph distance on edges induced by nonzero couplings of \(d_1^*d_1\).

For each graph distance \(r\), we compute:
- \(\max\limits_{\mathrm{dist}(e_0,e)=r} |(M^-1)_{e_0,e}|\),
- \(\mathrm{mean}\limits_{\mathrm{dist}(e_0,e)=r} |(M^-1)_{e_0,e}|\).

---

## Results

Crude Combes–Thomas-style exponent lower bound (using \(\nu=\max_i \sum_{j\neq i} |(\alpha d_1^*d_1)_{ij}|\)):

- \(\nu = 6.0\)
- \(\eta_{\mathrm{bound}} = \log(1+m/\nu) = 0.154151\)

Empirical fit for the maximum-entry decay (linear regression of \(\log(\max|G|)\) versus distance on distances 1..10):

- fitted slope \(b \approx -0.832613\)  
  (so \(\max|G|\approx e^{a + b r}\) with \(b<0\), consistent with exponential decay)

### Distance profile table

|   dist |   max_abs |   mean_abs |   count |
|-------:|----------:|-----------:|--------:|
|      0 | 0.627     |  0.627     |       1 |
|      1 | 0.1509    |  0.1468    |       6 |
|      2 | 0.0711    |  0.03131   |      16 |
|      3 | 0.01454   |  0.008143  |      24 |
|      4 | 0.004976  |  0.002844  |      32 |
|      5 | 0.002116  |  0.001105  |      40 |
|      6 | 0.0009285 |  0.0004611 |      47 |
|      7 | 0.0004859 |  0.0002456 |      41 |
|      8 | 0.0003078 |  0.0001313 |      32 |
|      9 | 0.0001651 |  6.879e-05 |      24 |
|     10 | 8.035e-05 |  3.599e-05 |      16 |
|     11 | 3.992e-05 |  2.062e-05 |       8 |
|     12 | 2.838e-05 |  2.838e-05 |       1 |

A plot (log max entry vs distance) is saved here:

- `maxwell_inverse_decay_L12_d2.png`

---

## Reproducible code

A standalone script is included in the project outputs:

- `sanity_check_maxwell_decay.py`

It builds \(d_1\), forms \(d_1^*d_1\), inverts \(M\), computes distances, prints the table, and writes the plot.

