import Workhouse.Basic

/-!
Exact anisotropy-variance algebra from the standalone 2026-09-08 campaign:
`research/anisotropy_variance_20260908/Variance.lean` and `THEORY.md` in the
outer workspace. The original eight proofs are retained under explicit names;
the centered moment, universal bound and complete zero criterion make the
algebra usable without an unformalized simplex argument.

The kernel/carrier identification and spectral estimates are separate source
arguments. The induced coefficient concerns the mixing contribution of the
displayed fourth-order matrix, not the complete sixth-order Hamiltonian.
-/

namespace Workhouse

noncomputable def anisotropyVariance (x y z : ℝ) : ℝ :=
  x * y * (x - y) ^ 2 + x * z * (x - z) ^ 2 + y * z * (y - z) ^ 2

/-- Source `variance_identity`: the simplex variance is an explicit sum of squares. -/
theorem anisotropy_variance_identity (x y z : ℝ) (h : x + y + z = 1) :
    x ^ 3 + y ^ 3 + z ^ 3 - (x ^ 2 + y ^ 2 + z ^ 2) ^ 2 =
      anisotropyVariance x y z := by
  have hz : z = 1 - x - y := by linarith
  rw [hz]
  unfold anisotropyVariance
  ring

/-- Source `variance_nonnegative`; normalization is unnecessary for positivity. -/
theorem anisotropy_variance_nonnegative (x y z : ℝ)
    (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : 0 ≤ z) :
    0 ≤ anisotropyVariance x y z := by
  unfold anisotropyVariance
  positivity

/-- Source `shape_identity`: the induced angular combination has ratio 1:3:-4. -/
theorem anisotropy_shape_identity (x y z : ℝ) (h : x + y + z = 1) :
    anisotropyVariance x y z =
      (x * y + x * z + y * z) + 3 * x * y * z - 4 * (x * y + x * z + y * z) ^ 2 := by
  have hz : z = 1 - x - y := by linarith
  rw [hz]
  unfold anisotropyVariance
  ring

/-- The weighted centered moment used by the carrier residual calculation. -/
theorem anisotropy_centered_moment_identity (x y z : ℝ) (h : x + y + z = 1) :
    let mean := x ^ 2 + y ^ 2 + z ^ 2
    x * (x - mean) ^ 2 + y * (y - mean) ^ 2 + z * (z - mean) ^ 2 =
      anisotropyVariance x y z := by
  dsimp
  have hz : z = 1 - x - y := by linarith
  rw [hz]
  unfold anisotropyVariance
  ring

/-- The variance is at most 1/4 throughout the closed probability simplex. -/
theorem anisotropy_variance_upper_bound (x y z : ℝ)
    (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : 0 ≤ z) (h : x + y + z = 1) :
    anisotropyVariance x y z ≤ 1 / 4 := by
  have hx1 : 0 ≤ 1 - x := by linarith
  have hy1 : 0 ≤ 1 - y := by linarith
  have hz1 : 0 ≤ 1 - z := by linarith
  have hc : 1 / 4 - anisotropyVariance x y z =
      (x ^ 2 + y ^ 2 + z ^ 2 - 1 / 2) ^ 2 +
        x ^ 2 * (1 - x) + y ^ 2 * (1 - y) + z ^ 2 * (1 - z) := by
    rw [← anisotropy_variance_identity x y z h]
    ring
  have hp : 0 ≤ (x ^ 2 + y ^ 2 + z ^ 2 - 1 / 2) ^ 2 +
      x ^ 2 * (1 - x) + y ^ 2 * (1 - y) + z ^ 2 * (1 - z) := by positivity
  linarith

/-- The complete nodal criterion: every pair of positive coordinates is equal. -/
theorem anisotropy_variance_zero_iff (x y z : ℝ)
    (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : 0 ≤ z) :
    anisotropyVariance x y z = 0 ↔
      (x = 0 ∨ y = 0 ∨ x = y) ∧ (x = 0 ∨ z = 0 ∨ x = z) ∧
        (y = 0 ∨ z = 0 ∨ y = z) := by
  have hxy : 0 ≤ x * y * (x - y) ^ 2 := by positivity
  have hxz : 0 ≤ x * z * (x - z) ^ 2 := by positivity
  have hyz : 0 ≤ y * z * (y - z) ^ 2 := by positivity
  have pair_zero (a b : ℝ) (hzero : a * b * (a - b) ^ 2 = 0) :
      a = 0 ∨ b = 0 ∨ a = b := by
    rcases mul_eq_zero.mp hzero with hab | hab
    · rcases mul_eq_zero.mp hab with ha | hb
      · exact Or.inl ha
      · exact Or.inr (Or.inl hb)
    · exact Or.inr (Or.inr (sub_eq_zero.mp (sq_eq_zero_iff.mp hab)))
  constructor
  · intro hv
    unfold anisotropyVariance at hv
    exact ⟨pair_zero x y (by linarith), pair_zero x z (by linarith),
      pair_zero y z (by linarith)⟩
  · rintro ⟨hxy0, hxz0, hyz0⟩
    have hzxy : x * y * (x - y) ^ 2 = 0 := by
      rcases hxy0 with h | h | h <;> simp [h]
    have hzxz : x * z * (x - z) ^ 2 = 0 := by
      rcases hxz0 with h | h | h <;> simp [h]
    have hzyz : y * z * (y - z) ^ 2 = 0 := by
      rcases hyz0 with h | h | h <;> simp [h]
    unfold anisotropyVariance
    rw [hzxy, hzxz, hzyz]
    ring

/-- Source `axis_node`. -/
theorem anisotropy_axis_node (x : ℝ) : anisotropyVariance x 0 0 = 0 := by
  unfold anisotropyVariance
  ring

/-- Source `face_node`. -/
theorem anisotropy_face_node (x : ℝ) : anisotropyVariance x x 0 = 0 := by
  unfold anisotropyVariance
  ring

/-- Source `body_node`. -/
theorem anisotropy_body_node (x : ℝ) : anisotropyVariance x x x = 0 := by
  unfold anisotropyVariance
  ring

/-- Source `generic_holdout`, a strictly positive off-node rational value. -/
theorem anisotropy_generic_holdout :
    anisotropyVariance (1 / 6) (1 / 3) (1 / 2) = 5 / 324 := by
  unfold anisotropyVariance
  norm_num

/-- Source `induced_coefficient`, now using the registered kernel and hopping definitions. -/
theorem anisotropy_induced_coefficient :
    -4 * cShpAssembled ^ 2 / hopping 3 =
      -169924002729806205028788409 / 619343593697933825385600000 := by
  rw [hopping_three]
  unfold cShpAssembled
  norm_num

end Workhouse
