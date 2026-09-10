import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
Universal coefficient inequalities for the actual square-block first force.
Source: `research/w6_square_block_20260909/inverse_synthesis.md`, equations
(S5)-(S7), independently controlled by `verify_inverse_synthesis.py`.

This module proves the sharp coefficient, the bound at every radial level,
and its preservation under arbitrary finite nonnegative spectral weights.
The source's original-edge operator identification, Gaussian spectral
decomposition and infinite-energy-domain closure are separate analytic steps.
-/

namespace Workhouse

noncomputable def wilsonSquareGamma : ℝ := (4 * Real.sqrt 2 - 2) / 7

noncomputable def wilsonSquareRadialRatio (n : ℝ) : ℝ :=
  wilsonSquareGamma ^ 2 / (4 * (4 + Real.sqrt 2 * (2 * n - 1)))

noncomputable def wilsonSquareSharpConstant : ℝ := (4 - Real.sqrt 2) ^ 3 / 1372

/-- The cubic radical constant equals the full retained-plus-fast denominator ratio. -/
theorem wilson_square_sharp_constant :
    wilsonSquareSharpConstant = wilsonSquareGamma ^ 2 / (4 * (4 + Real.sqrt 2)) := by
  have hs : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hd : 4 * (4 + Real.sqrt 2) ≠ 0 := by positivity
  unfold wilsonSquareSharpConstant wilsonSquareGamma
  field_simp
  nlinarith [sq_nonneg (Real.sqrt 2 - 1)]

/-- The sharp first-force coefficient is strictly positive. -/
theorem wilson_square_sharp_constant_pos : 0 < wilsonSquareSharpConstant := by
  have hs : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hnonneg : 0 ≤ Real.sqrt 2 := Real.sqrt_nonneg 2
  have hlt : Real.sqrt 2 < 4 := by nlinarith
  unfold wilsonSquareSharpConstant
  positivity

/-- The first centered radial excitation has exactly the sharp inverse-energy ratio. -/
theorem wilson_square_first_source_saturates :
    wilsonSquareSharpConstant * (24 * Real.sqrt 2) =
      (528 * Real.sqrt 2 - 600) / 343 := by
  have hs : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  unfold wilsonSquareSharpConstant
  nlinarith [sq_nonneg (Real.sqrt 2 - 1)]

/-- Exact all-level difference, with no finite truncation parameter. -/
theorem wilson_square_radial_ratio_difference (n : ℝ) (hn : 1 ≤ n) :
    wilsonSquareSharpConstant - wilsonSquareRadialRatio n =
      wilsonSquareGamma ^ 2 * Real.sqrt 2 * (n - 1) /
        (2 * (4 + Real.sqrt 2) * (4 + Real.sqrt 2 * (2 * n - 1))) := by
  have hn' : 0 < 2 * n - 1 := by linarith
  have hden : 4 + Real.sqrt 2 * (2 * n - 1) ≠ 0 := by positivity
  have hbase : 4 + Real.sqrt 2 ≠ 0 := by positivity
  rw [wilson_square_sharp_constant]
  unfold wilsonSquareRadialRatio
  field_simp
  ring

/-- Every real radial index n>=1 has a nonnegative ratio bounded by the first level. -/
theorem wilson_square_radial_ratio_bound (n : ℝ) (hn : 1 ≤ n) :
    0 ≤ wilsonSquareRadialRatio n ∧ wilsonSquareRadialRatio n ≤ wilsonSquareSharpConstant := by
  have hn' : 0 ≤ n - 1 := by linarith
  have hn'' : 0 < 2 * n - 1 := by linarith
  have hdiff := wilson_square_radial_ratio_difference n hn
  have hnonneg : 0 ≤ wilsonSquareGamma ^ 2 * Real.sqrt 2 * (n - 1) /
      (2 * (4 + Real.sqrt 2) * (4 + Real.sqrt 2 * (2 * n - 1))) := by positivity
  constructor
  · unfold wilsonSquareRadialRatio
    positivity
  · linarith

/-- Only the first radial level can saturate the bound among real indices n>=1. -/
theorem wilson_square_radial_ratio_strict (n : ℝ) (hn : 1 < n) :
    wilsonSquareRadialRatio n < wilsonSquareSharpConstant := by
  have hs : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hspos : 0 < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  have hgamma : 0 < wilsonSquareGamma := by
    unfold wilsonSquareGamma
    nlinarith
  have hn' : 0 < n - 1 := by linarith
  have hn'' : 0 < 2 * n - 1 := by linarith
  have hdiff := wilson_square_radial_ratio_difference n (le_of_lt hn)
  have hpos : 0 < wilsonSquareGamma ^ 2 * Real.sqrt 2 * (n - 1) /
      (2 * (4 + Real.sqrt 2) * (4 + Real.sqrt 2 * (2 * n - 1))) := by positivity
  linarith

/-- Arbitrary finite radial superpositions inherit the sharp bound from their energy weights. -/
theorem wilson_square_finite_radial_synthesis_bound {ι : Type*} (s : Finset ι)
    (level weight : ι → ℝ) (hlevel : ∀ i ∈ s, 1 ≤ level i)
    (hweight : ∀ i ∈ s, 0 ≤ weight i) :
    ∑ i ∈ s, wilsonSquareRadialRatio (level i) * weight i ≤
      wilsonSquareSharpConstant * ∑ i ∈ s, weight i := by
  rw [Finset.mul_sum]
  exact Finset.sum_le_sum fun i hi =>
    mul_le_mul_of_nonneg_right (wilson_square_radial_ratio_bound (level i) (hlevel i hi)).2
      (hweight i hi)

end Workhouse
