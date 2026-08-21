---
id: CONJ_B
title: Conjecture B - Anomaly Source Positivity
status: OPEN
scope: horizontal_RG
dependencies: [P04_haar_mass]
required_for: RG Hessian positivity
tags: [conjecture, anomaly, rg-flow, positivity]
---

# Conjecture B: Anomaly Source Positivity

## Statement

**Conjecture B (Horizontal Anomaly Source Positivity)**

In the RG-Hessian flow, the anomaly contribution S_anom restricted to the horizontal, gauge-invariant subspace is local and provides a **positive** curvature source:
$$S_{anom}|_{\text{horizontal}} \geq 0$$

---

## Mathematical Formulation

Let H_phys(t) be the Hessian of effective action on physical (gauge-fixed) degrees of freedom. The RG flow:
$$\frac{dH_{phys}}{dt} = -H_{phys}^2 + S_{Haar} + S_{anom} + O(g^4)$$

**Conjecture B**: S_anom ≥ 0 on the physical subspace.

---

## Why It Matters

Combined with Haar term (P04):
$$S_{eff} = S_{Haar} + S_{anom} \geq c_0 + 0 = c_0 > 0$$

This ensures Riccati positivity (P06) implies mass gap.

---

## Evidence

1. **Perturbative**: 1-loop β-function gives positive contribution
2. **Trace anomaly**: Physical trace anomaly has definite sign
3. **Numerical**: Hessian remains positive in lattice simulations

---

## Approach to Proof

1. Compute gauge-projected anomaly explicitly
2. Use representation theory of SU(N)
3. Connect to β-function sign (asymptotic freedom)

---

## Status

| Aspect | Status |
|--------|--------|
| Statement | FORMULATED |
| Perturbative support | STRONG |
| Rigorous proof | OPEN |
