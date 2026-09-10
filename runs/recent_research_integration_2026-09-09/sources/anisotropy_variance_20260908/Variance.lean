import Mathlib.Tactic

namespace AnisotropyVariance

def pairVariance (x y z : ℝ) : ℝ :=
  x*y*(x-y)^2 + x*z*(x-z)^2 + y*z*(y-z)^2

theorem variance_identity (x y z : ℝ) (h : x+y+z=1) :
    x^3+y^3+z^3-(x^2+y^2+z^2)^2 = pairVariance x y z := by
  have hz : z = 1-x-y := by linarith
  rw [hz]
  unfold pairVariance
  ring

theorem variance_nonnegative (x y z : ℝ)
    (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : 0 ≤ z) :
    0 ≤ pairVariance x y z := by
  unfold pairVariance
  positivity

theorem shape_identity (x y z : ℝ) (h : x+y+z=1) :
    pairVariance x y z =
      (x*y+x*z+y*z) + 3*x*y*z - 4*(x*y+x*z+y*z)^2 := by
  have hz : z = 1-x-y := by linarith
  rw [hz]
  unfold pairVariance
  ring

theorem axis_node (x : ℝ) : pairVariance x 0 0 = 0 := by
  unfold pairVariance
  ring

theorem face_node (x : ℝ) : pairVariance x x 0 = 0 := by
  unfold pairVariance
  ring

theorem body_node (x : ℝ) : pairVariance x x x = 0 := by
  unfold pairVariance
  ring

theorem generic_holdout : pairVariance (1/6) (1/3) (1/2) = 5/324 := by
  unfold pairVariance
  norm_num

theorem induced_coefficient :
    -4 * (-13035490122347 / 550663802582400 : ℚ)^2 / (5/612) =
    -169924002729806205028788409 / 619343593697933825385600000 := by
  norm_num

#print axioms variance_identity
#print axioms variance_nonnegative
#print axioms shape_identity
#print axioms induced_coefficient
end AnisotropyVariance
