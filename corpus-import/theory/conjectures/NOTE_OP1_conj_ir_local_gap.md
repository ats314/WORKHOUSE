---
id: CONJ_IR
title: Conjecture IR - Local Gap and Topology
status: OPEN
scope: infrared
dependencies: [P07_sigma, CONJ_B]
required_for: Local sector mass gap
tags: [conjecture, infrared, topology, local-sector]
---

# Conjecture IR: Local Gap and Topological Modes

## Statement

**Conjecture IR-1 (Curvature-Driven Local Gap)**

Within each topological sector, curvature controls a local-observable spectral gap λ_loc > 0.

**Conjecture IR-2 (Topology Non-Dominant)**

Global topological modes do not dominate the decay rate of local Schwinger functions in the infinite-volume limit.

---

## Mathematical Formulation

### IR-1

For local observables O supported in region Λ_0 ⊂ Λ:
$$\text{Var}_{\mu|_{\text{sector}}}(O) \leq \frac{1}{\lambda_{\text{loc}}} \mathcal{E}(O, O)$$

with λ_loc independent of total volume.

### IR-2

$$\lim_{|\Lambda| \to \infty} \frac{\lambda_{\text{topo}}}{\lambda_{\text{loc}}} = 0$$

Topological gaps are slower than local gaps.

---

## Why They Matter

The physical mass gap involves local operators. If topology dominates:
- Exponential decay could fail
- Cluster decomposition violated

IR-1/2 ensure physical observables see the spectral gap.

---

## Evidence

1. **Strong coupling**: Topological fluctuations suppressed
2. **Large N**: Topological sectors decouple
3. **Numerics**: Local correlators decay faster than global

---

## Status

| Aspect | Status |
|--------|--------|
| Formulation | CLEAR |
| Strong coupling | SUPPORTED |
| General proof | OPEN |
