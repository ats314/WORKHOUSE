---
id: CONJ_C
title: Conjecture C - Continuum Polarity
status: OPEN
scope: continuum
dependencies: [P01_lattice_polarity]
required_for: Continuum functional inequalities
tags: [conjecture, polarity, continuum, capacity]
---

# Conjecture C: Continuum Polarity of Reducibles

## Statement

**Conjecture C (Polarity of Reducible Strata)**

The singular set of reducible connections Σ ⊂ 𝒜 is of **capacity zero** for the YM Dirichlet form. The Langevin dynamics and all relevant functional inequalities can be formulated on 𝓜_reg without boundary conditions at Σ.

---

## Comparison to Lattice

| Aspect | Lattice (P01) | Continuum (Conj C) |
|--------|---------------|-------------------|
| Configuration space | Finite-dim compact | Infinite-dim affine |
| Codimension | Finite | Infinite |
| Measure | Well-defined | Formal/limit |
| Status | ✓ PROVEN | OPEN |

---

## Why Infinite Codimension Helps

In infinite dimensions, the "effective codimension" of Σ is infinite because:
- Reducibility requires ξ ∈ Γ(ad P) with D_A ξ = 0
- This is an infinite-dimensional constraint
- By Gaussian polarity theory, infinite codim ⟹ zero capacity

---

## What's Proven

1. **Gaussian polarity**: For Gaussian measure on Hilbert space, sets of infinite codimension are polar
2. **Lattice polarity**: ✓ (See P01)

## What Remains

Transfer polarity from Gaussian/lattice to continuum YM measure via:
- Measure equivalence arguments
- Capacity estimates under measure change
- Continuum limit of lattice bounds

---

## Status

| Aspect | Status |
|--------|--------|
| Lattice version | ✓ PROVEN (P01) |
| Gaussian version | ✓ PROVEN |
| Continuum YM | OPEN |
