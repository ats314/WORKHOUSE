import Workhouse.Incidence

/-!
# Spectrum of `S(k)` and grounding of `q_a` (WORKHOUSE U1, from `incidence_gram`)

Two results completing the incidence picture:

* **Full spectrum** (`Smat_carrier_eigen` in `Incidence` + `Smat_perp_eigen` here):
  from `incidence_gram` (`BB† = q_a·I − ψψ†`), the carrier line is the `−4`-eigenspace and
  its entire orthogonal complement (2-dimensional in `ℂ³`) is the `(−4+q_a)`-eigenspace.
  Together this is `spec S(k) = {−4, −4+q_a, −4+q_a}` — eigenvalue `−4` simple on `ψ`,
  eigenvalue `−4+q_a` with multiplicity `2` on `ψ^⟂`.

* **Grounding `q_a`** (`qa_dispersion`, `qa_dispersion_sum`): with `dᵢ = e^{ikᵢ}−1`,
  `|dᵢ|² = 4 sin²(kᵢ/2)`, hence `q_a = Σ 4 sin²(kᵢ/2)` — the physical Bloch scalar, the same
  `sin²(·/2)` dispersion form used in `FiberGap`.

Status: builds against `leanprover/lean4:v4.34.0-rc1` + Mathlib (repo-pinned), no `sorry`;
depends only on `[propext, Classical.choice, Quot.sound]`.  External to the WORKHOUSE clone.
-/

open Matrix

namespace Workhouse

/-- **Orthogonal eigenspace.**  Every `v` orthogonal to the carrier (`ψ†v = 0`) is an
eigenvector of `S(k)` with eigenvalue `−4 + q_a`.  With `Smat_carrier_eigen` (`Sψ = −4ψ`)
this gives the full spectrum `{−4, −4+q_a, −4+q_a}`: `−4` on the carrier line, `−4+q_a` on
the 2-dimensional complement. -/
theorem Smat_perp_eigen (d1 d2 d3 : ℂ) (v : Fin 3 → ℂ)
    (hv : star (psi d1 d2 d3) ⬝ᵥ v = 0) :
    Smat d1 d2 d3 *ᵥ v = (-4 + qa d1 d2 d3) • v := by
  have hOuter : (Matrix.of (fun i j => psi d1 d2 d3 i * star (psi d1 d2 d3 j))) *ᵥ v = 0 := by
    funext i
    have hentry : ((Matrix.of (fun i j => psi d1 d2 d3 i * star (psi d1 d2 d3 j))) *ᵥ v) i
        = psi d1 d2 d3 i * (star (psi d1 d2 d3) ⬝ᵥ v) := by
      simp only [Matrix.mulVec, dotProduct, Matrix.of_apply, Pi.star_apply]
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j _; ring
    rw [hentry, hv, mul_zero, Pi.zero_apply]
  rw [Smat, incidence_gram, Matrix.sub_mulVec, Matrix.sub_mulVec, hOuter]
  simp only [Matrix.smul_mulVec, Matrix.one_mulVec, sub_zero]
  module

/-- `|e^{ik} − 1|² = 4 sin²(k/2)` (as the complex scalar `star dᵢ · dᵢ`). -/
theorem qa_dispersion (k : ℝ) :
    star (Complex.exp ((k : ℂ) * Complex.I) - 1) * (Complex.exp ((k : ℂ) * Complex.I) - 1)
      = ((4 * Real.sin (k / 2) ^ 2 : ℝ) : ℂ) := by
  have hd : Complex.exp ((k : ℂ) * Complex.I) - 1
      = ((Real.cos k - 1 : ℝ) : ℂ) + ((Real.sin k : ℝ) : ℂ) * Complex.I := by
    rw [Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin]; push_cast; ring
  rw [show star (Complex.exp ((k : ℂ) * Complex.I) - 1) * (Complex.exp ((k : ℂ) * Complex.I) - 1)
        = ((Complex.normSq (Complex.exp ((k : ℂ) * Complex.I) - 1) : ℝ) : ℂ)
      from (Complex.normSq_eq_conj_mul_self).symm]
  rw [hd, Complex.normSq_add_mul_I]
  have hcos : Real.cos k = 1 - 2 * Real.sin (k / 2) ^ 2 := by
    have h2 : Real.cos k = 2 * Real.cos (k / 2) ^ 2 - 1 := by
      conv_lhs => rw [show k = 2 * (k / 2) by ring]
      exact Real.cos_two_mul (k / 2)
    nlinarith [Real.sin_sq_add_cos_sq (k / 2)]
  norm_cast
  nlinarith [Real.sin_sq_add_cos_sq k, hcos]

/-- **`q_a` grounded.**  With `dᵢ = e^{ikᵢ} − 1`, `q_a = Σ 4 sin²(kᵢ/2)` — the physical
Bloch dispersion scalar. -/
theorem qa_dispersion_sum (k1 k2 k3 : ℝ) :
    qa (Complex.exp ((k1 : ℂ) * Complex.I) - 1) (Complex.exp ((k2 : ℂ) * Complex.I) - 1)
        (Complex.exp ((k3 : ℂ) * Complex.I) - 1)
      = ((4 * Real.sin (k1 / 2) ^ 2 + 4 * Real.sin (k2 / 2) ^ 2 + 4 * Real.sin (k3 / 2) ^ 2 : ℝ) : ℂ) := by
  rw [qa, qa_dispersion k1, qa_dispersion k2, qa_dispersion k3]
  push_cast; ring

end Workhouse
