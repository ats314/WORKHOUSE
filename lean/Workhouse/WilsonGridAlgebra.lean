import Mathlib.Tactic

/-!
The exact block certificate used by the all-size shared-edge grid argument in
`research/w6_compact_continuation_20260909/grid_gaussian_floor.md`, equation
(G6). Its four internal edges form a cycle; no matrix eigenvalue sampling is
used here. Global edge assembly, covariance-weighted source identification
and second quantization remain separate arguments in that source.
-/

namespace Workhouse

def wilsonGridBlockEnergy (a b c d : ℝ) : ℝ :=
  (a - b) ^ 2 + (a - c) ^ 2 + (b - d) ^ 2 + (c - d) ^ 2

noncomputable def wilsonGridBlockVariance (a b c d : ℝ) : ℝ :=
  a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2 - (a + b + c + d) ^ 2 / 4

/-- Exact quadratic-form version of L_B = 2 Q_E + (1/2) v v^T. -/
theorem wilson_grid_block_energy_identity (a b c d : ℝ) :
    wilsonGridBlockEnergy a b c d =
      2 * wilsonGridBlockVariance a b c d + (a - b - c + d) ^ 2 / 2 := by
  unfold wilsonGridBlockEnergy wilsonGridBlockVariance
  ring

/-- The internal block edges control twice the energy off the constant direction. -/
theorem wilson_grid_block_energy_lower_bound (a b c d : ℝ) :
    2 * wilsonGridBlockVariance a b c d ≤ wilsonGridBlockEnergy a b c d := by
  rw [wilson_grid_block_energy_identity]
  linarith [sq_nonneg (a - b - c + d)]

/-- The internal cycle has a dimension-free four-times-Euclidean-energy upper bound. -/
theorem wilson_grid_block_energy_upper_bound (a b c d : ℝ) :
    wilsonGridBlockEnergy a b c d ≤ 4 * (a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2) := by
  unfold wilsonGridBlockEnergy
  nlinarith [sq_nonneg (a + b), sq_nonneg (a + c), sq_nonneg (b + d), sq_nonneg (c + d)]

/-- The block certificate loses energy exactly on its retained constant direction. -/
theorem wilson_grid_block_energy_zero_iff (a b c d : ℝ) :
    wilsonGridBlockEnergy a b c d = 0 ↔ a = b ∧ a = c ∧ a = d := by
  unfold wilsonGridBlockEnergy
  constructor
  · intro h
    have hab : a = b := by nlinarith [sq_nonneg (a - c), sq_nonneg (b - d), sq_nonneg (c - d)]
    have hac : a = c := by nlinarith [sq_nonneg (a - b), sq_nonneg (b - d), sq_nonneg (c - d)]
    have hbd : b = d := by nlinarith [sq_nonneg (a - b), sq_nonneg (a - c), sq_nonneg (c - d)]
    exact ⟨hab, hac, hab.trans hbd⟩
  · rintro ⟨hab, hac, had⟩
    simp [← hab, ← hac, ← had]

end Workhouse
