import Workhouse.Flatness

/-!
# Signed incidence factorization `S(k) + 4I = B(k)B(k)†` (WORKHOUSE U1)

The exact Bloch incidence data of the corpus (MASTER_THEORY_UNIFIED v4.3 §3.2), in the
plaquette-orbital basis `(12),(13),(23)`, with `dᵢ = e^{ikᵢ} − 1`:

  `B(k) = !![d₂,-d₁,0; d₃,0,-d₁; 0,d₃,-d₂]`,   `ψ(k) = (d̄₃, -d̄₂, d̄₁)`,   `q_a = Σ|dᵢ|²`.

The results below are all machine-checked identities (cross-verified in `sympy` first):

* `incidence_gram`      — `B(k)B(k)† = q_a·I − ψψ†`  (Lemma 3.1, the direct computation).
* `carrier_in_kernel`   — `B(k)†·ψ(k) = 0`  (this is `∂₂∂₃ = 0` in Bloch form).
* `carrier_normSq`      — `‖ψ(k)‖² = q_a(k)`.
* `carrier_BBdagger_zero` — `B(k)B(k)†·ψ = 0`  (carrier is the `0`-eigenvector of `BB†`).
* `incidence_factorization` — `S(k) + 4I = B(k)B(k)†`, with `S := BB† − 4I`.
* `Smat_carrier_eigen`  — `S(k)·ψ = −4·ψ`  (the `−4` bottom of `spec S = {−4,−4+q_a,−4+q_a}`).
* `flat_from_incidence` — **closes the Flatness gap**: the effective Hamiltonian
  `E·I + t·(B(k)B(k)†)` has `ψ(k)` as an eigenvector with `k`-independent eigenvalue `E`.
  The `BB†` form that `Flatness.carrier_eigenvector` *assumed* is here *produced* by the
  concrete incidence operator, with `B†ψ = 0` proven rather than hypothesised.

Status: builds against `leanprover/lean4:v4.34.0-rc1` + Mathlib (repo-pinned), no `sorry`;
depends only on `[propext, Classical.choice, Quot.sound]`.  External to the WORKHOUSE clone.
-/

open Matrix

namespace Workhouse

/-- The signed face-to-link Bloch incidence matrix `B(k)` (basis `(12),(13),(23)`). -/
def Bmat (d1 d2 d3 : ℂ) : Matrix (Fin 3) (Fin 3) ℂ :=
  !![d2, -d1, 0; d3, 0, -d1; 0, d3, -d2]

/-- The charge-odd homological carrier `ψ(k) = (d̄₃, -d̄₂, d̄₁)`. -/
def psi (d1 d2 d3 : ℂ) : Fin 3 → ℂ := ![star d3, -star d2, star d1]

/-- The Bloch scalar `q_a = Σ |dᵢ|²`. -/
def qa (d1 d2 d3 : ℂ) : ℂ := star d1 * d1 + star d2 * d2 + star d3 * d3

/-- **Incidence Gram (Lemma 3.1).** `B(k)B(k)† = q_a·I − ψψ†`. -/
theorem incidence_gram (d1 d2 d3 : ℂ) :
    Bmat d1 d2 d3 * (Bmat d1 d2 d3)ᴴ
      = qa d1 d2 d3 • (1 : Matrix (Fin 3) (Fin 3) ℂ)
        - Matrix.of (fun i j => psi d1 d2 d3 i * star (psi d1 d2 d3 j)) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Bmat, psi, qa, Matrix.mul_apply, Matrix.conjTranspose_apply,
      Fin.sum_univ_three, Matrix.sub_apply, Matrix.smul_apply,
      Matrix.of_apply, smul_eq_mul] <;>
    ring

/-- **Carrier in the kernel.** `B(k)†·ψ(k) = 0` — this is `∂₂∂₃ = 0` in Bloch form. -/
theorem carrier_in_kernel (d1 d2 d3 : ℂ) :
    (Bmat d1 d2 d3)ᴴ *ᵥ (psi d1 d2 d3) = 0 := by
  funext i
  fin_cases i <;>
    simp [Bmat, psi, Matrix.mulVec, Matrix.conjTranspose_apply, dotProduct,
      Fin.sum_univ_three] <;>
    ring

/-- `‖ψ(k)‖² = q_a(k)`. -/
theorem carrier_normSq (d1 d2 d3 : ℂ) :
    star (psi d1 d2 d3) ⬝ᵥ (psi d1 d2 d3) = qa d1 d2 d3 := by
  simp [psi, qa, dotProduct, Fin.sum_univ_three]
  ring

/-- The carrier is the `0`-eigenvector of `B(k)B(k)†`. -/
theorem carrier_BBdagger_zero (d1 d2 d3 : ℂ) :
    (Bmat d1 d2 d3 * (Bmat d1 d2 d3)ᴴ) *ᵥ (psi d1 d2 d3) = 0 := by
  rw [← Matrix.mulVec_mulVec, carrier_in_kernel, Matrix.mulVec_zero]

/-- The signed shared-link adjacency `S(k) := B(k)B(k)† − 4I`. -/
noncomputable def Smat (d1 d2 d3 : ℂ) : Matrix (Fin 3) (Fin 3) ℂ :=
  Bmat d1 d2 d3 * (Bmat d1 d2 d3)ᴴ - (4 : ℂ) • (1 : Matrix (Fin 3) (Fin 3) ℂ)

/-- **The factorization.** `S(k) + 4I = B(k)B(k)†`. -/
theorem incidence_factorization (d1 d2 d3 : ℂ) :
    Smat d1 d2 d3 + (4 : ℂ) • (1 : Matrix (Fin 3) (Fin 3) ℂ)
      = Bmat d1 d2 d3 * (Bmat d1 d2 d3)ᴴ := by
  simp [Smat]

/-- `S(k)·ψ = −4·ψ` — the `−4` bottom of `spec S(k) = {−4, −4+q_a, −4+q_a}`. -/
theorem Smat_carrier_eigen (d1 d2 d3 : ℂ) :
    Smat d1 d2 d3 *ᵥ (psi d1 d2 d3) = (-4 : ℂ) • (psi d1 d2 d3) := by
  rw [Smat, Matrix.sub_mulVec, carrier_BBdagger_zero, Matrix.smul_mulVec, Matrix.one_mulVec]
  simp

/-- **Closes the Flatness gap.**  The effective Hamiltonian `E·I + t·(B(k)B(k)†)` — with the
`BB†` form now *produced* by the concrete incidence operator rather than assumed — has the
carrier `ψ(k)` as an eigenvector with `k`-independent eigenvalue `E`.  The hypothesis
`B(k)†ψ(k) = 0` of `Flatness.carrier_eigenvector` is discharged by `carrier_in_kernel`. -/
theorem flat_from_incidence (E t : ℝ) (d1 d2 d3 : ℂ) :
    ((E : ℂ) • (1 : Matrix (Fin 3) (Fin 3) ℂ) + (t : ℂ) • (Bmat d1 d2 d3 * (Bmat d1 d2 d3)ᴴ))
        *ᵥ (psi d1 d2 d3)
      = (E : ℂ) • (psi d1 d2 d3) :=
  carrier_eigenvector E t (Bmat d1 d2 d3) (psi d1 d2 d3) (carrier_in_kernel d1 d2 d3)

end Workhouse
