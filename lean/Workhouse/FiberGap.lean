import Mathlib

/-!
# Fiber isolation gap of the folded carrier band (WORKHOUSE H0 audit, §4)

The carrier band is flat through `O(u³)` (homological: `B(k)†ψ(k) = 0`), so its first
dispersion is `O(u⁴)`, an ordinary `cos`-hopping cap band
`ΔE(k) = -(2861009/8438730300)·u⁴·cos k`
(Consolidation Guide §; the `u⁴` **power** is proven, the coefficient is the historical
`O(u⁴)` branch and is C2-disputed).

The `p = 0`-fiber isolation gap is the carrier's self-dispersion between `k = 0` (Γ) and
the nearest alias at `k = 2π/b`:

  `g(b) = ΔE(2π/b) - ΔE(0) = (2861009/4219365150)·u⁴·sin²(π/b)`.

Since `sin²(π/b) ~ π²/b²`, this gives `g(b) ~ 6.69×10⁻³·u⁴/b² → 0`: the isolation
collapses under blocking (the `L⁻²`/G11 phenomenon), forcing the shrinking-island route.

Results
* `cos_gap`   — general identity: `-c·cos(2π/b) - (-c·cos 0) = 2c·sin²(π/b)`.
* `fiber_gap` — the exact §4 gap with the historical `O(u⁴)` coefficient.

Status: builds against `leanprover/lean4:v4.34.0-rc1` + Mathlib (repo-pinned), no `sorry`;
depends only on `[propext, Classical.choice, Quot.sound]`.  External to the WORKHOUSE clone.
-/

namespace Workhouse

/-- Half-angle gap identity for a `cos`-hopping band `k ↦ -c·cos k`:
the gap between `k = 2π/b` and `k = 0` is `2c·sin²(π/b)`. -/
theorem cos_gap (c b : ℝ) :
    (-c * Real.cos (2 * Real.pi / b)) - (-c * Real.cos 0)
      = 2 * c * Real.sin (Real.pi / b) ^ 2 := by
  have hcos2 : Real.cos (2 * Real.pi / b) = 2 * Real.cos (Real.pi / b) ^ 2 - 1 := by
    rw [show (2 * Real.pi / b) = 2 * (Real.pi / b) by ring, Real.cos_two_mul]
  have hsin : Real.sin (Real.pi / b) ^ 2 = 1 - Real.cos (Real.pi / b) ^ 2 := Real.sin_sq _
  rw [Real.cos_zero, hcos2, hsin]; ring

/-- **Fiber isolation gap (§4).**  For the historical `O(u⁴)` cap-band dispersion
`ΔE(k) = -(2861009/8438730300)·u⁴·cos k`, the Γ-to-nearest-alias gap is exactly
`(2861009/4219365150)·u⁴·sin²(π/b)`. -/
theorem fiber_gap (u b : ℝ) :
    (-(2861009 / 8438730300 : ℝ) * u ^ 4 * Real.cos (2 * Real.pi / b))
      - (-(2861009 / 8438730300 : ℝ) * u ^ 4 * Real.cos 0)
      = (2861009 / 4219365150 : ℝ) * u ^ 4 * Real.sin (Real.pi / b) ^ 2 := by
  have hcos2 : Real.cos (2 * Real.pi / b) = 2 * Real.cos (Real.pi / b) ^ 2 - 1 := by
    rw [show (2 * Real.pi / b) = 2 * (Real.pi / b) by ring, Real.cos_two_mul]
  have hsin : Real.sin (Real.pi / b) ^ 2 = 1 - Real.cos (Real.pi / b) ^ 2 := Real.sin_sq _
  have hc : (2861009 / 4219365150 : ℝ) = 2 * (2861009 / 8438730300 : ℝ) := by norm_num
  rw [Real.cos_zero, hcos2, hsin, hc]; ring

end Workhouse
