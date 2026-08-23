# WORKHOUSE T0 / T3 boundary — the carrier-atom chain

Date: 2026-08-23
Purpose: record exactly what the Lean layer now certifies (T0) and the two physics inputs
that remain asserted (T3), for the ledger.
Repository status: read-only; external to the clone. Lean sources staged (uncommitted) under
`lean/Workhouse/`. No document is authority — every T0 row below is `#print axioms`-clean
(`[propext, Classical.choice, Quot.sound]`, no `sorry`), built against
`leanprover/lean4:v4.34.0-rc1` + repo-pinned Mathlib.

---

## The chain, one line

incidence factorization → carrier kernel → full spectrum (with multiplicities) →
`q_a = Σ 4sin²(kᵢ/2)` → `BB†` eigenvector form → flat `k`-independent eigenvalue →
exact fiber gap `g(b)` → `g(b) ∼ c·u⁴/b²` → carrier-atom window bound `≥ 1−(2ε/g)²` →
the `o(u⁴/b²)` clean-atom rule.

Everything on that line except the two inputs in §T3 is now **T0**.

---

## T0 — machine-checked (Lean, no `sorry`)

| Fact | Theorem(s) | File |
|---|---|---|
| `B(k)B(k)† = q_a·I − ψψ†` (Lemma 3.1) | `incidence_gram` | `Incidence` |
| `B(k)†ψ(k) = 0` (`∂₂∂₃=0`) | `carrier_in_kernel` | `Incidence` |
| `‖ψ(k)‖² = q_a` | `carrier_normSq` | `Incidence` |
| `S(k)+4I = B(k)B(k)†` | `incidence_factorization` | `Incidence` |
| `spec S(k) = {−4, −4+q_a, −4+q_a}` with multiplicities (−4 simple, −4+q_a mult 2, for `k≠Γ`) | `Smat_carrier_eigen`, `Smat_perp_eigen`, `carrier_perp_finrank`, `carrier_ne_zero` | `Incidence`, `Spectrum` |
| `q_a = Σ 4sin²(kᵢ/2)` (grounds the Bloch scalar) | `qa_dispersion`, `qa_dispersion_sum` | `Spectrum` |
| `E·I + t·BB†` fixes carrier as eigenvector, eigenvalue `E` **independent of k** | `carrier_eigenvector`, `carrier_flat`, `flat_from_incidence` | `Flatness`, `Incidence` |
| exact fiber gap `g(b) = (2861009/4219365150)·u⁴·sin²(π/b)` | `fiber_gap`, `cos_gap` | `FiberGap` |
| `b²·g(b) → (2861009/4219365150)·u⁴·π²`, i.e. `g(b) ∼ c·u⁴/b²` | `gap_asymptotic` | `CarrierAtomGap` |
| carrier-atom weight `≥ 1−(2ε/g)²` (spectral Chebyshev / operator form) | `window_weight_ge`, `carrier_atom_weight`, `carrier_atom_of_perturbation` | `AtomLemma` |
| atom at the physical gap; `ε_mix/g→0 ⟹` weight `→1` (the `o(u⁴/b²)` rule) | `carrier_atom_fiber_gap`, `carrier_atom_clean_limit` | `CarrierAtomGap` |

Files: `lean/Workhouse/{Incidence, Spectrum, Flatness, FiberGap, AtomLemma, CarrierAtomGap}.lean`
(plus pre-existing `Basic.lean`).

**Power caveat inside T0.** The `u⁴` *power* of the leading dispersion is T0 (it follows from
`B†ψ=0` ⇒ exact `O(u³)` flatness). The exact `O(u⁴)` *coefficient* `2861009/8438730300` is the
**historical branch and inherits the C2 dispute** — the algebra is certified, the disputed
input is not.

---

## T3 — still asserted (the two genuine physics inputs)

1. **The `O(u³)` factorized form of the effective Hamiltonian**
   `H_eff⁻(k,u) = E_flat(u)·I + t(u)·B(k)B(k)† + O(u⁴)`.
   The Lean layer takes the operator `E·I + t·BB†` as given and proves everything downstream;
   the *derivation* of this form (degenerate perturbation theory / projection to the
   one-plaquette sector) is the corpus's cold-certified computation, not formalized.
   Evidence level: `cold-reproduced` (corpus), `record-backed` for the Lean interface.

2. **The interacting alias-mixing bound `ε_mix(b) = o(u⁴/b²)`** — i.e. **G17** (RG /
   Wilson free-energy / source-radius stability at scale `A`). This is the one quantitative
   input the clean-atom rule needs and the sole remaining hard step of the spectral bridge.
   Nothing in the corpus proves it; the fixed-spacing package and the abstract transport are
   proved, the uniform bound is not.

Both are **load-bearing** and unchanged by the Lean work. Everything else on the chain is now
T0, so the continuum carrier-atom existence has been reduced, rigorously, to exactly these two.

---

## Reading

- The Lean layer certifies the **algebraic / homological / spectral spine** and the
  **abstract atom machinery**. It does **not** certify any physics regime crossing
  (finite `k` fiber → interacting → infinite volume → continuum); those crossings are the T3
  inputs above and the standing G17/G18/G19 debts.
- Net: `spec S`, the flat band, the `u⁴` power, the gap scaling, and the atom bound are no
  longer assertions. "The protected object is the glueball" is still not proved — it now rests
  on precisely inputs (1) and (2), not on the algebra.
