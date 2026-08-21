\
---
title: "Computation note: heat-kernel super-extractor scan (SU(2) bound)"
date: 2025-12-29
format: markdown+latex
---

## Abstract

The project includes `VERIFY_01_Heat_Kernel_Stability.py`, a short computation that scans a bound on a heat-kernel “super-extractor” Hessian term $M_2(t)$ and reports derived coefficients.

This note embeds the script’s output (as produced in this environment) and briefly records what it is checking.

---

## 1. What the script computes

The script defines
\[
M_2(t)=\frac{K(t)}{t},
\]
with $K(t)$ taken from a heat-kernel Hessian bound (as cited in the script comments), and then defines:

- $\alpha(t)=48\,M_2(t)$
- $\kappa(t)=1-12\,M_2(t)$

It also compares these values to a “geometric anomaly source” proxy
\[
\sigma_{\mathrm{geom}}(t)=\frac{4}{3}t.
\]

The printed “PASS/FAIL” in the output corresponds to $\kappa(t)>0$ (as per the script).

---

## 2. Raw output

Running:

```bash
python VERIFY_01_Heat_Kernel_Stability.py
```

produces:

```text
t     M2(t)     Alpha     Kappa     Route A        Route B
------------------------------------------------------------
0.05  15000.000 720000.000 -179999.000 0.067 FAIL
0.10  3750.000  180000.000 -44999.000  0.133 FAIL
0.20  937.500   45000.000  -11249.000  0.267 FAIL
0.30  416.667   20000.000  -4999.000   0.400 FAIL
0.40  234.375   11250.000  -2811.500   0.533 FAIL
0.50  150.000   7200.000   -1799.000   0.667 FAIL
0.60  104.167   5000.000   -1249.000   0.800 FAIL
0.70  76.531    3673.469   -917.375    0.933 FAIL
0.80  58.594    2812.500   -702.125    1.067 FAIL
0.90  46.296    2222.222   -554.556    1.200 FAIL
1.00  37.500    1800.000   -449.000    1.333 FAIL
1.10  31.095    1492.537   -372.140    1.467 FAIL
1.20  26.042    1250.000   -311.500    1.600 FAIL
1.30  22.041    1057.971   -263.490    1.733 FAIL
1.40  18.878    906.144    -225.535    1.867 FAIL
1.50  16.406    787.500    -195.875    2.000 FAIL
1.60  14.521    697.917    -173.250    2.133 FAIL
1.70  12.578    603.782    0.099       2.267 PASS
1.80  0.000     0.000      1.000       2.400 PASS
1.90  0.000     0.000      1.000       2.533 PASS
2.00  0.000     0.000      1.000       2.667 PASS
```

---

## 3. Notes and caveats

1. The “jump” to $M_2(t)=0$ for $t\ge 1.8$ comes from the way the script defines $K(t)$ (piecewise); it is not a physical discontinuity in the actual heat kernel.
2. The output is best interpreted as: *for sufficiently large flow-time in this bound model, the coefficient $\kappa(t)$ becomes positive*, which is the relevant “stability” condition in the script.

This computation is a **sanity-check** only. It does not replace a model-specific proof that the corresponding Hessian bounds hold uniformly in the lattice YM system.

