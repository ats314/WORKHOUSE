import Mathlib.MeasureTheory.Integral.Pi
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic
import Workhouse.SourceTilt

/-!
# Independent exponential sources and the source-radius obstruction

The product integrals here are actual integrals over finite product measures.
The growth conclusion concerns their centered second-moment expression, which
is the variance when the exponential lies in L2. This is the obstruction in
the corrected Track A source, not an assertion that SU(2) Haar has already been
identified with the abstract single-site probability measure.
-/

namespace Workhouse.SourceRadiusGrowth

open MeasureTheory ProbabilityTheory Filter
open scoped BigOperators Topology

variable {Ω : Type*} [MeasurableSpace Ω]

/-- The exponential moment of an independent sum is the power of its one-site moment. -/
theorem independent_exp_sum_integral (μ : Measure Ω) [SigmaFinite μ]
    (V : Ω → ℝ) (α : ℝ) (n : ℕ) :
    (∫ x : Fin n → Ω, Real.exp (α * ∑ i, V (x i))
      ∂Measure.pi (fun _ : Fin n => μ)) =
      (∫ x, Real.exp (α * V x) ∂μ) ^ n := by
  have heq (x : Fin n → Ω) :
      Real.exp (α * ∑ i, V (x i)) = ∏ i, Real.exp (α * V (x i)) := by
    rw [Finset.mul_sum, Real.exp_sum]
  simp_rw [heq]
  simpa using (integral_fintype_prod_eq_pow (ι := Fin n)
    (μ := μ) (fun x => Real.exp (α * V x)))

/-- Exact moment difference underlying the projected exponential-source norm. -/
theorem independent_exp_moment_difference (μ : Measure Ω) [SigmaFinite μ]
    (V : Ω → ℝ) (α : ℝ) (n : ℕ) :
    (∫ x : Fin n → Ω, Real.exp ((2 * α) * ∑ i, V (x i))
      ∂Measure.pi (fun _ : Fin n => μ)) -
      (∫ x : Fin n → Ω, Real.exp (α * ∑ i, V (x i))
        ∂Measure.pi (fun _ : Fin n => μ)) ^ 2 =
      (∫ x, Real.exp ((2 * α) * V x) ∂μ) ^ n -
      ((∫ x, Real.exp (α * V x) ∂μ) ^ 2) ^ n := by
  rw [independent_exp_sum_integral, independent_exp_sum_integral]
  congr 1
  rw [← pow_mul, ← pow_mul, Nat.mul_comm n 2]

/-- A quantitative geometric lower bound for the difference of two powers. -/
theorem power_difference_lower (A B : ℝ) (hB : 0 ≤ B) (hAB : B ≤ A) (n : ℕ) :
    ((n + 1 : ℕ) : ℝ) * (A - B) * B ^ n ≤ A ^ (n + 1) - B ^ (n + 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hA : 0 ≤ A := hB.trans hAB
    have hbase : 0 ≤ ((n + 1 : ℕ) : ℝ) * (A - B) * B ^ n := by positivity
    have h1 := mul_le_mul_of_nonneg_left ih hA
    have h2 := mul_le_mul_of_nonneg_right hAB hbase
    simp only [pow_succ, Nat.cast_add, Nat.cast_one] at ih h1 h2 ⊢
    nlinarith

/-- Dividing the independent variance by cardinality cannot stop its growth. -/
theorem power_difference_per_site_tendsto (A B : ℝ) (hB : 1 < B) (hAB : B < A) :
    Tendsto (fun n : ℕ => (A ^ (n + 1) - B ^ (n + 1)) / (n + 1 : ℝ))
      atTop atTop := by
  have hlim : Tendsto (fun n : ℕ => (A - B) * B ^ n) atTop atTop :=
    (tendsto_pow_atTop_atTop_of_one_lt hB).const_mul_atTop (sub_pos.mpr hAB)
  apply tendsto_atTop_mono (fun n => ?_) hlim
  apply (le_div_iff₀ (by positivity : (0 : ℝ) < n + 1)).mpr
  simpa [Nat.cast_add, Nat.cast_one, mul_assoc, mul_comm, mul_left_comm] using
    power_difference_lower A B (le_of_lt (lt_trans zero_lt_one hB)) hAB.le n

/-- The actual product-measure centered moment per source site is unbounded
whenever the one-site first and second exponential moments have the strict gap.
The moment hypotheses are explicit and do not assume the multi-site conclusion. -/
theorem independent_exp_radius_squared_tendsto (μ : Measure Ω) [SigmaFinite μ]
    (V : Ω → ℝ) (α : ℝ)
    (hmean : 1 < (∫ x, Real.exp (α * V x) ∂μ) ^ 2)
    (hvar : (∫ x, Real.exp (α * V x) ∂μ) ^ 2 <
      ∫ x, Real.exp ((2 * α) * V x) ∂μ) :
    Tendsto (fun n : ℕ =>
      ((∫ x : Fin (n + 1) → Ω, Real.exp ((2 * α) * ∑ i, V (x i))
          ∂Measure.pi (fun _ : Fin (n + 1) => μ)) -
        (∫ x : Fin (n + 1) → Ω, Real.exp (α * ∑ i, V (x i))
          ∂Measure.pi (fun _ : Fin (n + 1) => μ)) ^ 2) / (n + 1 : ℝ))
      atTop atTop := by
  simp_rw [independent_exp_moment_difference]
  exact power_difference_per_site_tendsto _ _ hmean hvar

omit [MeasurableSpace Ω] in
/-- A pointwise one-site bound gives a bound on every configuration of the
actual finite product space. -/
theorem independent_sum_abs_le (V : Ω → ℝ) (b : ℝ)
    (hb : ∀ x, |V x| ≤ b) (n : ℕ) (x : Fin n → Ω) :
    |∑ i, V (x i)| ≤ (n : ℝ) * b := by
  calc
    _ ≤ ∑ i, |V (x i)| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ _i : Fin n, b := Finset.sum_le_sum (fun i _ => hb (x i))
    _ = _ := by simp

/-- With bounded measurable single-site data the product moment difference
is the actual probability variance, hence an L2 norm squared. -/
theorem independent_exp_variance (μ : Measure Ω) [IsProbabilityMeasure μ]
    (V : Ω → ℝ) (hV : Measurable V) (α b : ℝ)
    (hb : ∀ x, |V x| ≤ b) (n : ℕ) :
    variance (fun x : Fin n → Ω => Real.exp (α * ∑ i, V (x i)))
      (Measure.pi (fun _ : Fin n => μ)) =
      (∫ x, Real.exp ((2 * α) * V x) ∂μ) ^ n -
      ((∫ x, Real.exp (α * V x) ∂μ) ^ 2) ^ n := by
  have hm : Measurable (fun x : Fin n → Ω => ∑ i, V (x i)) := by fun_prop
  have hbd : ∀ᵐ x ∂Measure.pi (fun _ : Fin n => μ),
      |∑ i, V (x i)| ≤ (n : ℝ) * b :=
    Filter.Eventually.of_forall (independent_sum_abs_le V b hb n)
  have hLp := SourceTilt.exp_source_memLp (Measure.pi (fun _ : Fin n => μ))
    _ hm.aemeasurable α ((n : ℝ) * b) hbd 2
  rw [variance_eq_integral hLp.aemeasurable,
    SourceTilt.centered_exp_integral_sq _ _ hm.aemeasurable α ((n : ℝ) * b) hbd]
  exact independent_exp_moment_difference μ V α n

/-- A nontrivial centered bounded source on a genuine probability space
produces an independent family whose squared projected-source radius diverges.
No independence-to-radius inference or strict moment gap is assumed. -/
theorem independent_nonzero_source_radius_unbounded (μ : Measure Ω)
    [IsProbabilityMeasure μ] (V : Ω → ℝ) (hV : Measurable V)
    (α b : ℝ) (hα : α ≠ 0) (hb : ∀ x, |V x| ≤ b)
    (hmean : (∫ x, V x ∂μ) = 0) (hsecond : 0 < ∫ x, (V x) ^ 2 ∂μ) :
    Tendsto (fun n : ℕ =>
      variance (fun x : Fin (n + 1) → Ω => Real.exp (α * ∑ i, V (x i)))
        (Measure.pi (fun _ : Fin (n + 1) => μ)) / (n + 1 : ℝ))
      atTop atTop := by
  have hbd : ∀ᵐ x ∂μ, |V x| ≤ b := Filter.Eventually.of_forall hb
  have hfirst := SourceTilt.one_lt_integral_exp_of_centered_nonzero
    μ V hV.aemeasurable α b hα hbd hmean hsecond
  have hgap := SourceTilt.exp_source_second_moment_gap
    μ V hV.aemeasurable α b hα hbd hmean hsecond
  have hsq : 1 < (∫ x, Real.exp (α * V x) ∂μ) ^ 2 := by nlinarith
  simp_rw [independent_exp_variance μ V hV α b hb]
  exact power_difference_per_site_tendsto _ _ hsq hgap

/-- A globally bounded representative of the two-point source. It agrees with
the identity on the two atoms but meets the product theorem's pointwise bound. -/
noncomputable def boundedTwoPointSource (x : ℝ) : ℝ :=
  max (-(1 : ℝ) / 4) (min ((1 : ℝ) / 4) x)

/-- The concrete source is bounded on every real input, not only almost everywhere. -/
theorem boundedTwoPointSource_abs_le (x : ℝ) :
    |boundedTwoPointSource x| ≤ (1 : ℝ) / 2 := by
  rw [abs_le]
  constructor
  · dsimp [boundedTwoPointSource]
    linarith [le_max_left (-(1 : ℝ) / 4) (min ((1 : ℝ) / 4) x)]
  · dsimp [boundedTwoPointSource]
    apply max_le
    · norm_num
    · exact (min_le_left _ _).trans (by norm_num)

/-- Fully constructed independent-source counterexample. The atomic law is
explicitly not asserted to be SU(2) Haar measure. -/
theorem independent_twoPoint_radius_unbounded (α : ℝ) (hα : α ≠ 0) :
    Tendsto (fun n : ℕ =>
      variance (fun x : Fin (n + 1) → ℝ =>
        Real.exp (α * ∑ i, boundedTwoPointSource (x i)))
        (Measure.pi (fun _ : Fin (n + 1) => SourceTilt.symmetricTwoPoint)) /
        (n + 1 : ℝ)) atTop atTop := by
  apply independent_nonzero_source_radius_unbounded
    SourceTilt.symmetricTwoPoint boundedTwoPointSource (by unfold boundedTwoPointSource; fun_prop)
    α (1 / 2) hα boundedTwoPointSource_abs_le
  · norm_num [SourceTilt.symmetricTwoPoint_integral, boundedTwoPointSource]
  · norm_num [SourceTilt.symmetricTwoPoint_integral, boundedTwoPointSource]

end Workhouse.SourceRadiusGrowth
