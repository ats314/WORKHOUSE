---
id: CONJ_D
title: Conjecture D - Spectral Gap Implies Mass Gap
status: OPEN
scope: OS_reconstruction
dependencies: [P03_transfer_matrix, P05_poincare]
required_for: Physical mass gap from functional inequality
tags: [conjecture, spectral-gap, mass-gap, os-reconstruction]
---

# Conjecture D: Spectral Gap ⟹ Physical Mass Gap

## Statement

**Conjecture D (Local-Sector Spectral Gap ⟹ Physical Mass Gap)**

Under Osterwalder-Schrader positivity and cluster decomposition hypotheses, a Poincaré/LSI inequality with constant λ_loc > 0 on the local-observable sector implies a positive mass gap Δ > 0 for the reconstructed Wightman theory.

---

## Mathematical Formulation

**Given**: Spectral gap for Langevin generator
$$\text{Var}_\mu(f) \leq \frac{1}{\lambda} \mathcal{E}(f, f)$$

**Claim**: The 2-point function decays exponentially
$$\langle O(x) O(0) \rangle \leq C e^{-m|x|}$$

with m ≥ c·√λ, implying mass gap Δ = m > 0.

---

## The Gap Between Spectral Gap and Mass Gap

| Spectral Gap | Mass Gap |
|--------------|----------|
| Property of generator -L | Property of Hamiltonian H |
| Euclidean (imaginary time) | Minkowski (real time) |
| Langevin dynamics | Quantum field theory |

**Bridge**: Osterwalder-Schrader reconstruction

---

## OS Reconstruction

1. **Reflection positivity** → Hilbert space
2. **Euclidean correlations** → Wightman functions
3. **Spectral gap** → exponential decay → mass gap

---

## What's Needed

1. Verify OS axioms for lattice/continuum YM
2. Control local vs global topological modes
3. Handle gauge fixing carefully

---

## Status

| Aspect | Status |
|--------|--------|
| OS axioms for lattice YM | ✓ KNOWN |
| Spectral gap → correlator decay | ✓ STANDARD |
| Local sector isolation | REQUIRES Conj IR-1/2 |
