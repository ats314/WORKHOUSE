import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-! # Exact localization-plateau minimization and a positive slow-mode witness

Source: docs/derivations/yangmills-reconstruction.md, R4--R5.
The scalar minimization is proved over actual real exponentials. The finite
two-mode correlation has positive spectral weights and energies; no conclusion
about an actual Wilson spectral measure is postulated.
-/

namespace Workhouse.PlateauObstruction

/-- The R4 objective in physical time, with `a = eta - E` and `b = E`. -/
noncomputable def bound (A plateau a b t : ℝ) : ℝ :=
  A * Real.exp (-a * t) + plateau * Real.exp (b * t)

/-- The derivative-balance equation is sufficient for a global minimum.
The proof uses the exponential tangent inequality, not a minimizer premise. -/
theorem stationary_global_minimum (A plateau a b t0 t : ℝ)
    (hA : 0 < A) (hp : 0 < plateau)
    (hbalance : a * (A * Real.exp (-a * t0)) =
      b * (plateau * Real.exp (b * t0))) :
    bound A plateau a b t0 ≤ bound A plateau a b t := by
  have hleft := mul_le_mul_of_nonneg_left
    (Real.add_one_le_exp (-a * (t - t0)))
    (le_of_lt (mul_pos hA (Real.exp_pos (-a * t0))))
  have hright := mul_le_mul_of_nonneg_left
    (Real.add_one_le_exp (b * (t - t0)))
    (le_of_lt (mul_pos hp (Real.exp_pos (b * t0))))
  have hcancel := congrArg (fun x : ℝ => x * (t - t0)) hbalance
  have hexpA : Real.exp (-a * t0) * Real.exp (-a * (t - t0)) =
      Real.exp (-a * t) := by
    rw [← Real.exp_add]
    congr 1
    ring
  have hexpP : Real.exp (b * t0) * Real.exp (b * (t - t0)) =
      Real.exp (b * t) := by
    rw [← Real.exp_add]
    congr 1
    ring
  unfold bound
  nlinarith [congrArg (fun x : ℝ => A * x) hexpA,
    congrArg (fun x : ℝ => plateau * x) hexpP]

/-- The logarithmic critical point satisfies the exact derivative balance. -/
theorem logarithmic_time_is_stationary (A plateau a b : ℝ)
    (hA : 0 < A) (hp : 0 < plateau) (ha : 0 < a) (hb : 0 < b) :
    let t0 := Real.log (A * a / (plateau * b)) / (a + b)
    a * (A * Real.exp (-a * t0)) = b * (plateau * Real.exp (b * t0)) := by
  dsimp
  have hsum : a + b ≠ 0 := ne_of_gt (add_pos ha hb)
  have hden : plateau * b ≠ 0 := ne_of_gt (mul_pos hp hb)
  have hratio : 0 < A * a / (plateau * b) := div_pos (mul_pos hA ha) (mul_pos hp hb)
  have htime : (a + b) * (Real.log (A * a / (plateau * b)) / (a + b)) =
      Real.log (A * a / (plateau * b)) := by field_simp
  have hexp : Real.exp ((a + b) *
      (Real.log (A * a / (plateau * b)) / (a + b))) = A * a / (plateau * b) := by
    rw [htime, Real.exp_log hratio]
  have hsplit : Real.exp (b * (Real.log (A * a / (plateau * b)) / (a + b))) =
      Real.exp ((a + b) * (Real.log (A * a / (plateau * b)) / (a + b))) *
      Real.exp (-a * (Real.log (A * a / (plateau * b)) / (a + b))) := by
    rw [← Real.exp_add]
    congr 1
    ring
  rw [hsplit, hexp]
  field_simp

/-- Above the threshold, the critical time is admissible and minimizes every
nonnegative physical time (in fact the stationary inequality holds on all R). -/
theorem admissible_logarithmic_minimum (A plateau a b : ℝ)
    (hA : 0 < A) (hp : 0 < plateau) (ha : 0 < a) (hb : 0 < b)
    (hthreshold : plateau * b ≤ A * a) :
    let t0 := Real.log (A * a / (plateau * b)) / (a + b)
    0 ≤ t0 ∧ ∀ t : ℝ, 0 ≤ t → bound A plateau a b t0 ≤ bound A plateau a b t := by
  dsimp
  have hratio : 1 ≤ A * a / (plateau * b) :=
    (le_div_iff₀ (mul_pos hp hb)).mpr (by simpa using hthreshold)
  constructor
  · exact div_nonneg (Real.log_nonneg hratio) (le_of_lt (add_pos ha hb))
  · intro t _
    exact stationary_global_minimum A plateau a b _ t hA hp
      (logarithmic_time_is_stationary A plateau a b hA hp ha hb)

/-- Below the threshold, the constrained minimizer is time zero and the exact
minimum is `A + plateau`. -/
theorem endpoint_minimum (A plateau a b t : ℝ)
    (hA : 0 < A) (hp : 0 < plateau) (ht : 0 ≤ t)
    (hthreshold : A * a ≤ plateau * b) :
    A + plateau ≤ bound A plateau a b t := by
  have hleft := mul_le_mul_of_nonneg_left (Real.add_one_le_exp (-a * t)) (le_of_lt hA)
  have hright := mul_le_mul_of_nonneg_left (Real.add_one_le_exp (b * t)) (le_of_lt hp)
  have hbudget := mul_le_mul_of_nonneg_right hthreshold ht
  unfold bound
  nlinarith

/-- The attained interior value in an exact real-power coordinate. This is
the R5 expression before rewriting its positive factors into theta form. -/
theorem interior_minimum_value (A plateau a b : ℝ)
    (hA : 0 < A) (hp : 0 < plateau) (ha : 0 < a) (hb : 0 < b) :
    bound A plateau a b (Real.log (A * a / (plateau * b)) / (a + b)) =
      ((a + b) / a) * plateau * (A * a / (plateau * b)) ^ (b / (a + b)) := by
  have hratio : 0 < A * a / (plateau * b) := div_pos (mul_pos hA ha) (mul_pos hp hb)
  have hbalance := logarithmic_time_is_stationary A plateau a b hA hp ha hb
  dsimp at hbalance
  rw [Real.rpow_def_of_pos hratio]
  have he : Real.log (A * a / (plateau * b)) * (b / (a + b)) =
      b * (Real.log (A * a / (plateau * b)) / (a + b)) := by ring
  rw [he]
  unfold bound
  have hvalue (X Y : ℝ) (hXY : a * X = b * Y) :
      X + Y = (a + b) / a * Y := by
    field_simp
    nlinarith
  calc
    _ = (a + b) / a * (plateau *
      Real.exp (b * (Real.log (A * a / (plateau * b)) / (a + b)))) :=
      hvalue _ _ hbalance
    _ = _ := by ring

/-- R5 in the source's dimensionless energy fraction `theta`. -/
theorem theta_minimum_value (A plateau theta : ℝ)
    (hA : 0 < A) (hp : 0 < plateau) (ht : 0 < theta) (ht1 : theta < 1) :
    bound A plateau (1 - theta) theta
      (Real.log (A * (1 - theta) / (plateau * theta))) =
      A ^ theta * plateau ^ (1 - theta) /
        (theta ^ theta * (1 - theta) ^ (1 - theta)) := by
  have ha : 0 < 1 - theta := sub_pos.mpr ht1
  have hsum : 1 - theta + theta = 1 := by ring
  have hv := interior_minimum_value A plateau (1 - theta) theta hA hp ha ht
  rw [hsum, div_one, div_one] at hv
  rw [hv, Real.div_rpow (le_of_lt (mul_pos hA ha))
    (le_of_lt (mul_pos hp ht)) theta,
    Real.mul_rpow (le_of_lt hA) (le_of_lt ha),
    Real.mul_rpow (le_of_lt hp) (le_of_lt ht),
    Real.rpow_sub hp 1 theta, Real.rpow_sub ha 1 theta,
    Real.rpow_one, Real.rpow_one]
  field_simp

/-- Physical time and dimensionless time are related by the positive energy
scale. This makes the R5 proof apply to `E = eta * theta`. -/
theorem bound_time_rescaling (A plateau eta theta time : ℝ) (he : eta ≠ 0) :
    bound A plateau (eta * (1 - theta)) (eta * theta) (time / eta) =
      bound A plateau (1 - theta) theta time := by
  unfold bound
  congr 2 <;> field_simp

/-- The exact attained value at the source's physical-time optimum. Admissibility
requires `plateau * theta ≤ A * (1-theta)`, as proved separately. -/
theorem physical_time_minimum_value (A plateau eta theta : ℝ)
    (hA : 0 < A) (hp : 0 < plateau) (he : 0 < eta)
    (ht : 0 < theta) (ht1 : theta < 1) :
    bound A plateau (eta * (1 - theta)) (eta * theta)
      (Real.log (A * (1 - theta) / (plateau * theta)) / eta) =
      A ^ theta * plateau ^ (1 - theta) /
        (theta ^ theta * (1 - theta) ^ (1 - theta)) := by
  rw [bound_time_rescaling A plateau eta theta _ (ne_of_gt he)]
  exact theta_minimum_value A plateau theta hA hp ht ht1

/-- The R4 interior optimum is admissible, attains the R5 value, and minimizes
the objective over all nonnegative physical times. -/
theorem r4_r5_interior_optimum (A plateau eta theta : ℝ)
    (hA : 0 < A) (hp : 0 < plateau) (he : 0 < eta)
    (ht : 0 < theta) (ht1 : theta < 1)
    (hthreshold : plateau * theta ≤ A * (1 - theta)) :
    let t0 := Real.log (A * (1 - theta) / (plateau * theta)) / eta
    0 ≤ t0 ∧
      bound A plateau (eta * (1 - theta)) (eta * theta) t0 =
        A ^ theta * plateau ^ (1 - theta) /
          (theta ^ theta * (1 - theta) ^ (1 - theta)) ∧
      ∀ t : ℝ, 0 ≤ t →
        bound A plateau (eta * (1 - theta)) (eta * theta) t0 ≤
          bound A plateau (eta * (1 - theta)) (eta * theta) t := by
  dsimp
  have hmin := admissible_logarithmic_minimum A plateau (1 - theta) theta
    hA hp (sub_pos.mpr ht1) ht hthreshold
  have hsum : 1 - theta + theta = 1 := by ring
  dsimp at hmin
  rw [hsum, div_one] at hmin
  refine ⟨div_nonneg hmin.1 (le_of_lt he),
    physical_time_minimum_value A plateau eta theta hA hp he ht ht1, ?_⟩
  intro t htime
  rw [bound_time_rescaling A plateau eta theta _ (ne_of_gt he)]
  have hscale : bound A plateau (eta * (1 - theta)) (eta * theta) t =
      bound A plateau (1 - theta) theta (eta * t) := by
    have he1 : -(eta * (1 - theta)) * t = -(1 - theta) * (eta * t) := by ring
    have he2 : eta * theta * t = theta * (eta * t) := by ring
    simp only [bound, he1, he2]
  rw [hscale]
  exact hmin.2 (eta * t) (mul_nonneg (le_of_lt he) htime)

/-- Applying the actual optimized R4 bound gives R5. The spectral estimate
itself is an explicit premise; this theorem does not assert R1 for an operator. -/
theorem r4_r5_optimized_upper_bound (mass A plateau eta theta : ℝ)
    (hA : 0 < A) (hp : 0 < plateau) (he : 0 < eta)
    (ht : 0 < theta) (ht1 : theta < 1)
    (hthreshold : plateau * theta ≤ A * (1 - theta))
    (hbound : ∀ t : ℝ, 0 ≤ t → mass ≤
      bound A plateau (eta * (1 - theta)) (eta * theta) t) :
    mass ≤ A ^ theta * plateau ^ (1 - theta) /
      (theta ^ theta * (1 - theta) ^ (1 - theta)) := by
  have h := r4_r5_interior_optimum A plateau eta theta hA hp he ht ht1 hthreshold
  dsimp at h
  rw [← h.2.1]
  exact hbound _ h.1

/-- The positive two-atom centered correlation used to exhibit a slow mode. -/
noncomputable def correlation (weight slow fast t : ℝ) : ℝ :=
  weight * Real.exp (-slow * t) + Real.exp (-fast * t)

/-- A positive slow spectral weight lies beneath an arbitrarily small plateau
for every nonnegative time. -/
theorem slow_mode_fits_positive_plateau (weight slow fast t : ℝ)
    (hw : 0 ≤ weight) (hs : 0 ≤ slow) (ht : 0 ≤ t) :
    0 < correlation weight slow fast t ∧
      correlation weight slow fast t ≤ Real.exp (-fast * t) + weight := by
  have he : Real.exp (-slow * t) ≤ 1 := by
    apply Real.exp_le_one_iff.mpr
    nlinarith
  have hupper := mul_le_mul_of_nonneg_left he hw
  unfold correlation
  constructor
  · positivity
  · nlinarith

/-- Multiplication by the proposed faster decay exposes the slow spectral
component exactly, without estimating it away. -/
theorem rescaled_correlation_identity (weight slow fast t : ℝ) :
    correlation weight slow fast t * Real.exp (fast * t) =
      weight * Real.exp ((fast - slow) * t) + 1 := by
  unfold correlation
  rw [add_mul, mul_assoc, ← Real.exp_add, ← Real.exp_add]
  have hfirst : -slow * t + fast * t = (fast - slow) * t := by ring
  have hsecond : -fast * t + fast * t = 0 := by ring
  rw [hfirst, hsecond, Real.exp_zero]

/-- No finite nonnegative prefactor gives the faster exponential rate when
the positive spectral measure has a nonzero atom at the lower energy. -/
theorem positive_slow_mode_prevents_faster_bound (weight slow fast prefactor : ℝ)
    (hw : 0 < weight) (hgap : slow < fast) (hp : 0 ≤ prefactor) :
    ∃ t : ℝ, 0 ≤ t ∧ prefactor * Real.exp (-fast * t) <
      correlation weight slow fast t := by
  let t := (prefactor / weight + 1) / (fast - slow)
  have hd : 0 < fast - slow := sub_pos.mpr hgap
  have ht : 0 ≤ t := by dsimp [t]; positivity
  have htime : (fast - slow) * t = prefactor / weight + 1 := by
    dsimp [t]
    field_simp
  have hlinear := Real.add_one_le_exp ((fast - slow) * t)
  have hscaled := mul_le_mul_of_nonneg_left hlinear (le_of_lt hw)
  rw [htime] at hscaled
  have hcancel : weight * (prefactor / weight) = prefactor := by field_simp
  have hstrict : prefactor < weight * Real.exp ((fast - slow) * t) + 1 := by
    nlinarith
  refine ⟨t, ht, ?_⟩
  apply (mul_lt_mul_iff_left₀ (Real.exp_pos (fast * t))).mp
  have hunit : Real.exp (-fast * t) * Real.exp (fast * t) = 1 := by
    rw [← Real.exp_add]
    simp
  rw [mul_assoc, hunit, mul_one, rescaled_correlation_identity]
  exact hstrict

/-- Every positive error, however small, permits a strictly positive lower
energy with a nonzero positive spectral weight. Its correlation satisfies the
plateau estimate for every time, but defeats every proposed faster prefactor. -/
theorem arbitrarily_small_plateau_obstruction (plateau fast : ℝ)
    (hp : 0 < plateau) (hf : 0 < fast) :
    ∃ weight slow : ℝ, 0 < weight ∧ weight < plateau ∧ 0 < slow ∧ slow < fast ∧
      (∀ t : ℝ, 0 ≤ t → 0 < correlation weight slow fast t ∧
        correlation weight slow fast t ≤ Real.exp (-fast * t) + plateau) ∧
      (∀ prefactor : ℝ, 0 ≤ prefactor → ∃ t : ℝ, 0 ≤ t ∧
        prefactor * Real.exp (-fast * t) < correlation weight slow fast t) := by
  refine ⟨plateau / 2, fast / 2, by positivity, by linarith,
    by positivity, by linarith, ?_, ?_⟩
  · intro t ht
    have h := slow_mode_fits_positive_plateau (plateau / 2) (fast / 2) fast t
      (by positivity) (by positivity) ht
    exact ⟨h.1, by linarith [h.2]⟩
  · intro prefactor hpre
    exact positive_slow_mode_prevents_faster_bound (plateau / 2) (fast / 2)
      fast prefactor (by positivity) (by linarith) hpre

end Workhouse.PlateauObstruction
