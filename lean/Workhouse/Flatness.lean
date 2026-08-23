import Mathlib

/-!
# Homological flatness of the carrier band (WORKHOUSE, earns the O(u⁴) power)

Through third order, the corpus effective Hamiltonian on the one-plaquette degenerate
sector factors as
  `H_eff⁻(k,u) = E_flat(u)·I + t(u)·B(k)·B(k)† + O(u⁴)`,
where `B(k)` is the coboundary (signed-incidence) operator and the charge-odd carrier
`ψ(k)` lies in its kernel: `B(k)†·ψ(k) = 0` (MASTER_THEORY §4.4; the flat value is
`k`-independent *because* `B†ψ = 0`).

The homological fact below is exactly what makes the carrier energy flat through `O(u³)`,
so the first `k`-dependence — hence the leading dispersion — is pushed to `O(u⁴)`
(audit §4).  It is the load-bearing half of the "`u⁴` power is proven" claim.

Results
* `carrier_eigenvector` — `B†ψ = 0 ⟹ (E•I + t•B·B†) ψ = E•ψ` (eigenvalue `E`, no `k`).
* `carrier_energy`      — Rayleigh value `⟨ψ, H_eff ψ⟩ = E·⟨ψ,ψ⟩`.
* `carrier_flat`        — carrier energies at two momenta (any `B(k)`, `B(k')`) are equal:
                          the band is flat, to this order, for a homological reason.

Status: builds against `leanprover/lean4:v4.34.0-rc1` + Mathlib (repo-pinned), no `sorry`;
depends only on `[propext, Classical.choice, Quot.sound]`.  External to the WORKHOUSE clone.
-/

open Matrix

namespace Workhouse

variable {n m : ℕ}

/-- **Homological flatness core.**  If the carrier `ψ` is annihilated by the coboundary
`B(k)†` (`B(k)†·ψ = 0`), then it is an eigenvector of the third-order effective
Hamiltonian `E•I + t•(B·B†)` with eigenvalue `E`.  The eigenvalue does not mention `B(k)`,
so it is independent of `k`. -/
theorem carrier_eigenvector (E t : ℝ) (Bk : Matrix (Fin n) (Fin m) ℂ) (ψ : Fin n → ℂ)
    (hker : Bkᴴ *ᵥ ψ = 0) :
    ((E : ℂ) • (1 : Matrix (Fin n) (Fin n) ℂ) + (t : ℂ) • (Bk * Bkᴴ)) *ᵥ ψ = (E : ℂ) • ψ := by
  rw [Matrix.add_mulVec, Matrix.smul_mulVec, Matrix.smul_mulVec,
    Matrix.one_mulVec, ← Matrix.mulVec_mulVec, hker, Matrix.mulVec_zero, smul_zero, add_zero]

/-- The carrier's Rayleigh value is `E·‖ψ‖²`, with `E` independent of `k`. -/
theorem carrier_energy (E t : ℝ) (Bk : Matrix (Fin n) (Fin m) ℂ) (ψ : Fin n → ℂ)
    (hker : Bkᴴ *ᵥ ψ = 0) :
    star ψ ⬝ᵥ (((E : ℂ) • (1 : Matrix (Fin n) (Fin n) ℂ) + (t : ℂ) • (Bk * Bkᴴ)) *ᵥ ψ)
      = (E : ℂ) * (star ψ ⬝ᵥ ψ) := by
  rw [carrier_eigenvector E t Bk ψ hker, dotProduct_smul, smul_eq_mul]

/-- **Flatness.**  For any two momenta — encoded by coboundaries `B(k)`, `B(k')` with
kernel carriers `ψ`, `ψ'` of equal norm — the carrier energies coincide (both equal `E`).
The band is flat through `O(u³)` for the homological reason `B†ψ = 0`. -/
theorem carrier_flat (E t : ℝ) (Bk Bk' : Matrix (Fin n) (Fin m) ℂ) (ψ ψ' : Fin n → ℂ)
    (hker : Bkᴴ *ᵥ ψ = 0) (hker' : Bk'ᴴ *ᵥ ψ' = 0)
    (hψ : star ψ ⬝ᵥ ψ = 1) (hψ' : star ψ' ⬝ᵥ ψ' = 1) :
    star ψ ⬝ᵥ (((E : ℂ) • (1 : Matrix (Fin n) (Fin n) ℂ) + (t : ℂ) • (Bk * Bkᴴ)) *ᵥ ψ)
      = star ψ' ⬝ᵥ (((E : ℂ) • (1 : Matrix (Fin n) (Fin n) ℂ) + (t : ℂ) • (Bk' * Bk'ᴴ)) *ᵥ ψ') := by
  rw [carrier_energy E t Bk ψ hker, carrier_energy E t Bk' ψ' hker', hψ, hψ', mul_one]

end Workhouse
