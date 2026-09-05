/-
Exact scalar estimate used in the explicit SU(3) disjoint-plaquette
linearization obstruction. This is a rational inequality on a real
interval. It does not assume or formalize an operator-norm bound,
the Haar moments, or an infinite-volume conclusion.
-/
import Mathlib.Tactic

namespace Workhouse.RootedScalarBounds

/-- Taylor remainder bounds with ||V|| <= 6 give this explicit rational
lower bound, uniformly for 0 <= t <= 1/200. -/
theorem normalized_taylor_growth (t : ℝ) (h0 : 0 ≤ t) (ht : t ≤ 1 / 200) :
    1 + t / 2 ≤ (1 + t - 36 * t ^ 2) / (1 + 36 * t ^ 2) - 9 * t ^ 2 := by
  have ht2 : t ^ 2 ≤ t / 200 := by
    nlinarith [mul_nonneg h0 (sub_nonneg.mpr ht)]
  have ht3 : t ^ 3 ≤ t / 40000 := by
    nlinarith [mul_le_mul_of_nonneg_left ht2 h0]
  have ht4 : t ^ 4 ≤ t / 8000000 := by
    nlinarith [mul_le_mul_of_nonneg_left ht3 h0]
  have hden : 0 < 1 + 36 * t ^ 2 := by positivity
  apply (le_sub_iff_add_le).2
  apply (le_div_iff₀ hden).2
  nlinarith

/-- info: 'Workhouse.RootedScalarBounds.normalized_taylor_growth' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms normalized_taylor_growth

end Workhouse.RootedScalarBounds
