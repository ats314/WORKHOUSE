# Maxwell / C₀ / DG Decay Bounds + κ Plateau Extraction

This document bundles three threads that repeatedly cohere:

1. a **Maxwell Green’s function** computation,
2. extraction of a graph/operator constant \(C_0\),
3. converting a provable decay bound into a **measured mass/decay rate** \(\kappa\) using a prefactor-corrected plateau estimator.

---

## 1. The constants \(D_E\) and \(C_0\)

A standard form of Combes–Thomas / Dobrushin–Gronwall / DG-type decay bound produces an exponential rate \(\eta\) that depends on:

- a graph-degree constant \(D_E\) (for the lattice adjacency),
- an operator/kernel constant \(C_0\) (a row-sum / connectivity-weighted bound).

The Maxwell runs explicitly compute these constants on \(d=4\) tori:

- \(D_E = 18\),
- \(C_0(\Delta_1) \approx 43.9077\) (anchored at \(L=16\) in the logs).

From these:

- \(\eta_{\mathrm{DG}}(D_E)\approx 0.129010\),
- \(\eta_{\mathrm{DG}}(C_0)\approx 0.082635\),
- \(\eta_{\mathrm{CT}}(C_0)\approx 0.003410\).

---

## 2. Numerical verification: the decay inequality holds with slack

A representative “bound check” reports:

- computed max ratio \(\approx 0.1412\) at distance \(0\),
- and the condition “max ratio < 1” passes comfortably.

A separate “shell ratio” check reports:

- median shell ratio \(\approx 0.3418\),
- compared against a conservative exponential factor \(\exp(-0.2777)\approx 0.7575\),
- again a PASS with slack.

Interpretation: the analytic bound is not tight, but it is numerically respected; the bound is “alive” rather than vacuous.

---

## 3. κ extraction: why prefactor correction matters

For a scalar kernel on the lattice (or a component extracted from a tensor kernel), the asymptotic is:
\[
G(r)\;\approx\;A\,r^{-(d-1)/2}e^{-\kappa r},
\]
so the log-slope must correct the prefactor:
\[
\log|G(r)| + \tfrac{d-1}{2}\log r \;\sim\; -\kappa r + \text{const}.
\]

The “corrected slope plateau” method computes local slopes of this corrected quantity and then looks for a stable plateau region away from:

- the origin (discretization),
- torus wrap-around (finite-size contamination),
- and the floor/noise regime.

A run reports:

- expected axis \(\kappa_{\text{axis}} = 0.541097\),
- measured plateau \(\kappa_{\text{plateau}}(\text{axis}) = 0.537792\),
- difference \(-0.003305\) (PASS at the stated tolerance).

---

## 4. The failure mode: tail-envelope / wrong windowing

A different estimator (“directional tail-envelope slopes”) yields significantly larger values, e.g.:

- median slope \(\sim 0.64957\),

and an \(L^1\)-direction fit that drifts toward \(0\) as the fitting window is pushed outward — classic torus wrap-around / preprocessing artifact behavior.

Takeaway:

> κ is reproducible when you measure it the right way; it is not robust to naive tail fitting on a finite torus.

---

## 5. A bridge to “constant unification”

The same constant \(C_0\) appears in:

- the decay bound exponent \(\eta(C_0)\),
- and (numerically) in drift fits elsewhere in the project.

A drift fit reports \(b_{\hat{}} \approx 43.1239\), intriguingly close to \(C_0\approx 43.9077\).

This is not yet an identity, but it is the kind of “numerical rhyme” that often points at a shared operator norm controlling two different theorems.

**Conjecture (testable):** the drift constant \(b\) and the decay constant \(C_0\) are both controlled by the same underlying row-sum / degree bound for the relevant generator.

---

## 6. Minimal reference code (conceptual)

The full project code computes a tensor Maxwell Green’s function with a longitudinal/transverse decomposition, plus \(C_0\) from a kernel row-sum. Conceptually:

```python
# 1) Build lattice momenta p and p^2
# 2) Build inv_long = 1/m^2 and inv_trans = 1/(m^2 + α p^2)
# 3) Assemble M^{-1}(p) = inv_trans * I + (inv_long - inv_trans) * P_L(p)
# 4) iFFT to get G_{μν}(x)
# 5) Build Q(p) = p^2 δ_{μν} - \hat p_μ \hat p_ν and iFFT to kernel K(x)
# 6) Define C0 = max_μ (sum_{ν,x} |K_{μν}(x)| - |K_{μμ}(0)|)
# 7) Check DG/CT inequalities and κ plateau
```

---

## 7. What to do next (high leverage)

1. Freeze the “prefactor-correct plateau” estimator as the *only* κ oracle.
2. For each \((L,m^2)\), report the automatically detected plateau window and a “wrap-around veto.”
3. Run the constant-link test: regress \(b\) against \(C_0\) and degree constants as \(L\) varies.

