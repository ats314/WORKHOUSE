/- Exact star-ring algebra behind the creator parent gap.
These identities do not formalize operator norms, spectral calculus,
creator convergence, or a thermodynamic limit. -/
import Mathlib.Tactic

namespace Workhouse.CreatorParent

variable {R : Type*} [Ring R] [StarRing R]

theorem idempotent_square_defect (P : R) (hP : P * P = P) :
    (star P * P) * (star P * P) - star P * P =
      star ((star P - 1) * P) * ((star P - 1) * P) := by
  have hstar : star P * star P = star P := by
    simpa only [star_mul] using congrArg star hP
  simp only [star_mul, star_sub, star_star, star_one]
  noncomm_ring [hP, hstar]
  simp only [← mul_assoc, hstar]

theorem commuting_pair_square (P Q : R) (hPQ : P * Q = Q * P) :
    (star P * P) * (star Q * Q) =
      star (P * Q) * (P * Q) + star P * (P * star Q - star Q * P) * Q := by
  have hstar : star Q * star P = star P * star Q := by
    simpa only [star_mul] using congrArg star hPQ
  simp only [star_mul]
  noncomm_ring [hstar]

theorem wilson_gap_constant (a K M : ℝ) (ha : a ≤ 1 / 8)
    (hK : K ≤ a / 4) (hM0 : 0 ≤ M) (hM : M ≤ a / 2) :
    247 / 256 ≤ 1 - K - M^2 := by
  have hmax : M ≤ 1 / 16 := by linarith
  have hsquare : M^2 ≤ 1 / 256 := by nlinarith
  linarith

/-- info: 'Workhouse.CreatorParent.idempotent_square_defect' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms idempotent_square_defect
/-- info: 'Workhouse.CreatorParent.commuting_pair_square' depends on axioms: [propext] -/
#guard_msgs in
#print axioms commuting_pair_square
/-- info: 'Workhouse.CreatorParent.wilson_gap_constant' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms wilson_gap_constant

end Workhouse.CreatorParent
