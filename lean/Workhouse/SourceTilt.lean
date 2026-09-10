/-
# Corrected probability-measure source tilt estimates

Source: G17_HAMILTONIAN_OSTERWALDER_SEILER_TRANSCRIPTION_20260910.md,
equations (9)--(17), (21)--(23). The raw source in that note is bounded by
one half per plaquette. These results prove the corrected partition bound and
the bounded-footprint variance bound for actual probability measures, together
with the strict obstruction to a beta-only constant equal to one at beta zero.

The source's Haar identification is not assumed to have been constructed here:
the strict theorem exposes centeredness and a positive second moment explicitly.
No Osterwalder--Seiler expansion, uniform spectral gap, or unrestricted source
radius is asserted by this module.
-/
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.MeasureTheory.Function.L2Space
import Mathlib.Probability.Moments.Variance
import Mathlib.Tactic

namespace Workhouse.SourceTilt

open MeasureTheory ProbabilityTheory Filter
open scoped ENNReal BigOperators

variable {Ω : Type*} [MeasurableSpace Ω]

/-- The two-sided almost-everywhere exponential bound retains the source radius. -/
theorem exp_source_bounds (μ : Measure Ω) (f : Ω → ℝ) (α b : ℝ)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ b) :
    ∀ᵐ x ∂μ, Real.exp (α * f x) ∈
      Set.Icc (Real.exp (- (|α| * b))) (Real.exp (|α| * b)) := by
  filter_upwards [hb] with x hx
  have h : |α * f x| ≤ |α| * b := by
    rw [abs_mul]
    exact mul_le_mul_of_nonneg_left hx (abs_nonneg α)
  exact ⟨Real.exp_le_exp.mpr (abs_le.mp h).1,
    Real.exp_le_exp.mpr (abs_le.mp h).2⟩

/-- A bounded measurable source has an exponential in every finite-measure Lp. -/
theorem exp_source_memLp (μ : Measure Ω) [IsFiniteMeasure μ] (f : Ω → ℝ)
    (hf : AEMeasurable f μ) (α b : ℝ) (hb : ∀ᵐ x ∂μ, |f x| ≤ b)
    (p : ℝ≥0∞) : MemLp (fun x => Real.exp (α * f x)) p μ := by
  exact memLp_of_bounded (exp_source_bounds μ f α b hb)
    (hf.const_mul α).exp.aestronglyMeasurable p

/-- Correct raw partition bound: the constant depends on the source tilt. -/
theorem exp_source_integral_le (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : AEMeasurable f μ) (α b : ℝ)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ b) :
    (∫ x, Real.exp (α * f x) ∂μ) ≤ Real.exp (|α| * b) := by
  have hi := (exp_source_memLp μ f hf α b hb 1).integrable le_rfl
  simpa using integral_mono_ae hi (integrable_const (Real.exp (|α| * b)))
    ((exp_source_bounds μ f α b hb).mono fun _ hx => hx.2)

/-- Summing actual bounded plaquette observables gives the cardinality bound. -/
theorem finite_source_abs_le {ι : Type*} (μ : Measure Ω) (s : Finset ι)
    (V : ι → Ω → ℝ)
    (hV : ∀ᵐ x ∂μ, ∀ i ∈ s, |V i x| ≤ (1 : ℝ) / 2) :
    ∀ᵐ x ∂μ, |∑ i ∈ s, V i x| ≤ (s.card : ℝ) / 2 := by
  filter_upwards [hV] with x hx
  calc
    |∑ i ∈ s, V i x| ≤ ∑ i ∈ s, |V i x| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ _i ∈ s, (1 : ℝ) / 2 := Finset.sum_le_sum hx
    _ = (s.card : ℝ) / 2 := by simp [div_eq_mul_inv]

/-- PC-2 for a finite family of bounded measurable sources, for every probability measure. -/
theorem finite_source_partition_bound {ι : Type*} (μ : Measure Ω)
    [IsProbabilityMeasure μ] (s : Finset ι) (V : ι → Ω → ℝ)
    (hVm : ∀ i, AEMeasurable (V i) μ)
    (hV : ∀ᵐ x ∂μ, ∀ i ∈ s, |V i x| ≤ (1 : ℝ) / 2) (α : ℝ) :
    (∫ x, Real.exp (α * ∑ i ∈ s, V i x) ∂μ) ≤
      Real.exp (|α| * (s.card : ℝ) / 2) := by
  have hm : AEMeasurable (fun x => ∑ i ∈ s, V i x) μ := by fun_prop
  simpa [mul_div_assoc] using exp_source_integral_le μ _ hm α _
    (finite_source_abs_le μ s V hV)

/-- Eq. (16): centering the actual exponential gives its variance exactly. -/
theorem centered_exp_integral_sq (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : AEMeasurable f μ) (α b : ℝ)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ b) :
    (∫ x, (Real.exp (α * f x) - ∫ y, Real.exp (α * f y) ∂μ) ^ 2 ∂μ) =
      (∫ x, Real.exp ((2 * α) * f x) ∂μ) -
        (∫ x, Real.exp (α * f x) ∂μ) ^ 2 := by
  have hLp := exp_source_memLp μ f hf α b hb 2
  rw [← variance_eq_integral hLp.aemeasurable, variance_eq_sub hLp]
  congr 1
  apply integral_congr_ae
  filter_upwards with x
  rw [show (2 * α) * f x = α * f x + α * f x by ring, Real.exp_add]
  simp [pow_two]

/-- Popoviciu gives a volume-independent bound only after the footprint is bounded. -/
theorem exp_source_variance_le (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : AEMeasurable f μ) (α b : ℝ)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ b) :
    variance (fun x => Real.exp (α * f x)) μ ≤
      ((Real.exp (|α| * b) - Real.exp (-(|α| * b))) / 2) ^ 2 := by
  exact variance_le_sq_of_bounded (exp_source_bounds μ f α b hb)
    (exp_source_memLp μ f hf α b hb 2).aemeasurable

/-- The centered exponential is an actual real L2 vector. -/
noncomputable def centeredExpL2 (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : AEMeasurable f μ) (α b : ℝ)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ b) : Lp ℝ 2 μ :=
  ((exp_source_memLp μ f hf α b hb 2).sub
    (memLp_const (∫ y, Real.exp (α * f y) ∂μ))).toLp _

/-- The squared Hilbert norm is the true measure variance, not a scalar model. -/
theorem centeredExpL2_norm_sq (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : AEMeasurable f μ) (α b : ℝ)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ b) :
    ‖centeredExpL2 μ f hf α b hb‖ ^ 2 =
      variance (fun x => Real.exp (α * f x)) μ := by
  rw [← real_inner_self_eq_norm_sq, L2.inner_def,
    variance_eq_integral (exp_source_memLp μ f hf α b hb 2).aemeasurable]
  apply integral_congr_ae
  have h := ((exp_source_memLp μ f hf α b hb 2).sub
    (memLp_const (∫ y, Real.exp (α * f y) ∂μ))).coeFn_toLp
  filter_upwards [h] with x hx
  change (centeredExpL2 μ f hf α b hb x) * (centeredExpL2 μ f hf α b hb x) = _
  change centeredExpL2 μ f hf α b hb x = _ at hx
  rw [hx]
  simp only [Pi.sub_apply]
  ring

/-- The constructed centered L2 source lies in the orthogonal complement of
every constant function, in particular the normalized vacuum `1`. -/
theorem centeredExpL2_orthogonal_constants (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : AEMeasurable f μ) (α b : ℝ)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ b) (c : ℝ) :
    inner ℝ ((memLp_const c : MemLp (fun _x : Ω => c) 2 μ).toLp _)
      (centeredExpL2 μ f hf α b hb) = 0 := by
  rw [L2.inner_def]
  have he := (exp_source_memLp μ f hf α b hb 1).integrable le_rfl
  calc
    (∫ x, inner ℝ
        (((memLp_const c : MemLp (fun _x : Ω => c) 2 μ).toLp _) x)
        (centeredExpL2 μ f hf α b hb x) ∂μ) =
        ∫ x, c * (Real.exp (α * f x) - ∫ y, Real.exp (α * f y) ∂μ) ∂μ := by
      apply integral_congr_ae
      have h := ((exp_source_memLp μ f hf α b hb 2).sub
        (memLp_const (∫ y, Real.exp (α * f y) ∂μ))).coeFn_toLp
      filter_upwards [(memLp_const c : MemLp (fun _x : Ω => c) 2 μ).coeFn_toLp, h]
        with x hc hx
      change centeredExpL2 μ f hf α b hb x = _ at hx
      simp only [hc, hx, Pi.sub_apply]
      simp [mul_comm]
    _ = 0 := by
      rw [integral_const_mul, integral_sub he (integrable_const _)]
      simp

/-- Norm version of Popoviciu for the actual projected L2 source. -/
theorem centeredExpL2_norm_le (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : AEMeasurable f μ) (α b : ℝ) (hb0 : 0 ≤ b)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ b) :
    ‖centeredExpL2 μ f hf α b hb‖ ≤
      (Real.exp (|α| * b) - Real.exp (-(|α| * b))) / 2 := by
  have hsq := exp_source_variance_le μ f hf α b hb
  rw [← centeredExpL2_norm_sq μ f hf α b hb] at hsq
  have hab : 0 ≤ |α| * b := mul_nonneg (abs_nonneg _) hb0
  have hexp : Real.exp (-(|α| * b)) ≤ Real.exp (|α| * b) :=
    Real.exp_le_exp.mpr (by linarith)
  have hnonneg : 0 ≤ (Real.exp (|α| * b) - Real.exp (-(|α| * b))) / 2 := by
    positivity
  nlinarith [norm_nonneg (centeredExpL2 μ f hf α b hb)]

/-- Corrected Eq. (23): a fixed nonempty footprint cutoff gives a uniform
radius. The cutoff dependence is explicit; no unrestricted radius is claimed. -/
theorem bounded_footprint_radius (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : AEMeasurable f μ) (α : ℝ) (m m₀ : ℕ)
    (hm : 1 ≤ m) (hcut : m ≤ m₀)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ (m : ℝ) / 2) :
    ‖centeredExpL2 μ f hf α ((m : ℝ) / 2) hb‖ / Real.sqrt (m : ℝ) ≤
      (Real.exp (|α| * (m₀ : ℝ) / 2) -
        Real.exp (-(|α| * (m₀ : ℝ) / 2))) / 2 := by
  have hnorm := centeredExpL2_norm_le μ f hf α ((m : ℝ) / 2)
    (by positivity) hb
  have hsqrt : 1 ≤ Real.sqrt (m : ℝ) := by
    have hmreal : (1 : ℝ) ≤ m := by exact_mod_cast hm
    simpa using Real.sqrt_le_sqrt hmreal
  have hsize : |α| * (m : ℝ) / 2 ≤ |α| * (m₀ : ℝ) / 2 := by
    gcongr
  calc
    _ ≤ ‖centeredExpL2 μ f hf α ((m : ℝ) / 2) hb‖ :=
      div_le_self (norm_nonneg _) hsqrt
    _ ≤ (Real.exp (|α| * ((m : ℝ) / 2)) -
        Real.exp (-(|α| * ((m : ℝ) / 2)))) / 2 := hnorm
    _ ≤ _ := by
      simp only [mul_div_assoc]
      have hu := Real.exp_le_exp.mpr hsize
      have hl := Real.exp_le_exp.mpr (neg_le_neg hsize)
      simpa only [mul_div_assoc] using
        div_le_div_of_nonneg_right (sub_le_sub hu hl) (by norm_num : (0 : ℝ) ≤ 2)

/-- The sharper cutoff radius from the corrected G17 report. This keeps the
square-root footprint factor after applying `sinh(t) ≤ t * exp(t)`. -/
theorem bounded_footprint_radius_sharp (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : AEMeasurable f μ) (α : ℝ) (m m₀ : ℕ)
    (hm : 1 ≤ m) (hcut : m ≤ m₀)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ (m : ℝ) / 2) :
    ‖centeredExpL2 μ f hf α ((m : ℝ) / 2) hb‖ / Real.sqrt (m : ℝ) ≤
      (|α| / 2) * Real.sqrt (m₀ : ℝ) * Real.exp (|α| * (m₀ : ℝ) / 2) := by
  let t := |α| * (m : ℝ) / 2
  have hsinh : (Real.exp t - Real.exp (-t)) / 2 ≤ t * Real.exp t := by
    have heq : Real.exp t * Real.exp (-2 * t) = Real.exp (-t) := by
      rw [← Real.exp_add]
      congr 1
      ring
    have h := mul_le_mul_of_nonneg_left (Real.add_one_le_exp (-2 * t))
      (Real.exp_pos t).le
    rw [heq] at h
    nlinarith
  have hnorm : ‖centeredExpL2 μ f hf α ((m : ℝ) / 2) hb‖ ≤ t * Real.exp t := by
    have h := centeredExpL2_norm_le μ f hf α ((m : ℝ) / 2) (by positivity) hb
    apply le_trans ?_ hsinh
    simpa only [t, mul_div_assoc] using h
  have hsqrt : 0 < Real.sqrt (m : ℝ) := by
    apply Real.sqrt_pos.mpr
    exact_mod_cast (lt_of_lt_of_le Nat.zero_lt_one hm)
  calc
    _ ≤ (t * Real.exp t) / Real.sqrt (m : ℝ) :=
      div_le_div_of_nonneg_right hnorm hsqrt.le
    _ = (|α| / 2) * Real.sqrt (m : ℝ) * Real.exp t := by
      calc
        _ = (|α| / 2) * ((m : ℝ) / Real.sqrt (m : ℝ)) * Real.exp t := by
          dsimp [t]
          ring
        _ = _ := by rw [Real.div_sqrt]
    _ ≤ _ := by
      dsimp [t]
      gcongr

/-- A nonzero centered source has a strictly nontrivial raw tilt. The assumptions
are ordinary first and second moments; the desired exponential inequality is proved. -/
theorem one_lt_integral_exp_of_centered_nonzero (μ : Measure Ω)
    [IsProbabilityMeasure μ] (f : Ω → ℝ) (hf : AEMeasurable f μ)
    (α b : ℝ) (hα : α ≠ 0) (hb : ∀ᵐ x ∂μ, |f x| ≤ b)
    (hmean : ∫ x, f x ∂μ = 0) (hsecond : 0 < ∫ x, f x ^ 2 ∂μ) :
    1 < ∫ x, Real.exp (α * f x) ∂μ := by
  have hfLp : MemLp f 2 μ := MemLp.of_bound hf.aestronglyMeasurable b
    (hb.mono fun x hx => by simpa [Real.norm_eq_abs] using hx)
  have hfi := hfLp.integrable (by norm_num : (1 : ℝ≥0∞) ≤ 2)
  have hlinear : Integrable (fun x => α * f x + 1) μ :=
    (hfi.const_mul α).add (integrable_const 1)
  have he := (exp_source_memLp μ f hf α b hb 1).integrable le_rfl
  have hle : (fun x => α * f x + 1) ≤ᵐ[μ] (fun x => Real.exp (α * f x)) :=
    ae_of_all μ fun x => Real.add_one_le_exp _
  have hm : (∫ x, α * f x + 1 ∂μ) = 1 := by
    rw [integral_add (hfi.const_mul α) (integrable_const 1), integral_const_mul, hmean]
    simp
  have hge : 1 ≤ ∫ x, Real.exp (α * f x) ∂μ := by
    rw [← hm]
    exact integral_mono_ae hlinear he hle
  refine lt_of_le_of_ne hge ?_
  intro heq
  have haeeq := (integral_eq_iff_of_ae_le hlinear he hle).mp (hm.trans heq)
  have hzero : f =ᵐ[μ] 0 := by
    filter_upwards [haeeq] with x hx
    change f x = 0
    by_contra hfx
    have hs := Real.add_one_lt_exp (mul_ne_zero hα hfx)
    exact (ne_of_lt hs) hx
  have hsqzero : (∫ x, f x ^ 2 ∂μ) = 0 := by
    calc
      (∫ x, f x ^ 2 ∂μ) = ∫ _x : Ω, (0 : ℝ) ∂μ := by
        apply integral_congr_ae
        filter_upwards [hzero] with x hx
        simp [hx]
      _ = 0 := by simp
  linarith

/-- The precise SU(2) one-plaquette moment inputs suffice to refute K(0)=1.
The Haar group construction and the two moment evaluations remain separate inputs. -/
theorem raw_tilt_gt_one_of_su2_moments (μ : Measure Ω) [IsProbabilityMeasure μ]
    (V : Ω → ℝ) (hV : AEMeasurable V μ) (α : ℝ) (hα : α ≠ 0)
    (hbound : ∀ᵐ x ∂μ, |V x| ≤ (1 : ℝ) / 2)
    (hmean : ∫ x, V x ∂μ = 0) (hsecond : ∫ x, V x ^ 2 ∂μ = (1 : ℝ) / 16) :
    ¬ (∫ x, Real.exp (α * V x) ∂μ) ≤ 1 := by
  exact not_le.mpr (one_lt_integral_exp_of_centered_nonzero μ V hV α (1 / 2)
    hα hbound hmean (by rw [hsecond]; norm_num))

/-- Exponentiation of a nonzero centered bounded source has strictly positive
variance. This proves the strict second-versus-first moment gap needed for
independent product sources, without assuming that moment gap itself. -/
theorem exp_source_variance_pos (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : AEMeasurable f μ) (α b : ℝ) (hα : α ≠ 0)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ b) (hmean : ∫ x, f x ∂μ = 0)
    (hsecond : 0 < ∫ x, f x ^ 2 ∂μ) :
    0 < variance (fun x => Real.exp (α * f x)) μ := by
  refine lt_of_le_of_ne (variance_nonneg _ _) ?_
  intro hz
  have hconstExp := ae_eq_integral_of_variance_eq_zero
    (exp_source_memLp μ f hf α b hb 2) hz.symm
  obtain ⟨x, hx⟩ := hconstExp.exists
  have hconst : f =ᵐ[μ] fun _ => f x := by
    filter_upwards [hconstExp] with y hy
    exact mul_left_cancel₀ hα (Real.exp_injective (hy.trans hx.symm))
  have hxzero : f x = 0 := by
    calc
      f x = ∫ _y : Ω, f x ∂μ := by simp
      _ = ∫ y, f y ∂μ := integral_congr_ae hconst.symm
      _ = 0 := hmean
  have hsqzero : (∫ y, f y ^ 2 ∂μ) = 0 := by
    calc
      (∫ y, f y ^ 2 ∂μ) = ∫ _y : Ω, (0 : ℝ) ∂μ := by
        apply integral_congr_ae
        filter_upwards [hconst] with y hy
        simp [hy, hxzero]
      _ = 0 := by simp
  linarith

/-- Strict product-growth input on actual exponential moments of a measure. -/
theorem exp_source_second_moment_gap (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : AEMeasurable f μ) (α b : ℝ) (hα : α ≠ 0)
    (hb : ∀ᵐ x ∂μ, |f x| ≤ b) (hmean : ∫ x, f x ∂μ = 0)
    (hsecond : 0 < ∫ x, f x ^ 2 ∂μ) :
    (∫ x, Real.exp (α * f x) ∂μ) ^ 2 < ∫ x, Real.exp ((2 * α) * f x) ∂μ := by
  have hv := exp_source_variance_pos μ f hf α b hα hb hmean hsecond
  rw [variance_eq_integral (exp_source_memLp μ f hf α b hb 2).aemeasurable,
    centered_exp_integral_sq μ f hf α b hb] at hv
  linarith

/-- An explicit probability-measure witness for the generic obstruction.
This atomic measure is not identified with SU(2) Haar measure. -/
noncomputable def symmetricTwoPoint : Measure ℝ :=
  ENNReal.ofReal ((1 : ℝ) / 2) • Measure.dirac (-(1 : ℝ) / 4) +
    ENNReal.ofReal ((1 : ℝ) / 2) • Measure.dirac ((1 : ℝ) / 4)

instance symmetricTwoPoint_isProbabilityMeasure : IsProbabilityMeasure symmetricTwoPoint where
  measure_univ := by
    norm_num [symmetricTwoPoint]
    rw [← ENNReal.ofReal_add (by norm_num) (by norm_num)]
    norm_num

/-- Exact integration against the constructed atomic probability measure. -/
theorem symmetricTwoPoint_integral (g : ℝ → ℝ) :
    (∫ x, g x ∂symmetricTwoPoint) = (g (-(1 : ℝ) / 4) + g ((1 : ℝ) / 4)) / 2 := by
  have hn : Integrable g (Measure.dirac (-(1 : ℝ) / 4)) := integrable_dirac (by simp)
  have hp : Integrable g (Measure.dirac ((1 : ℝ) / 4)) := integrable_dirac (by simp)
  rw [symmetricTwoPoint, integral_add_measure
    (hn.smul_measure ENNReal.ofReal_ne_top) (hp.smul_measure ENNReal.ofReal_ne_top)]
  simp only [integral_smul_measure, integral_dirac, smul_eq_mul]
  norm_num
  ring

/-- The witness meets a genuine almost-everywhere bounded-source hypothesis. -/
theorem symmetricTwoPoint_source_bound :
    ∀ᵐ x ∂symmetricTwoPoint, |x| ≤ (1 : ℝ) / 2 := by
  change ∀ᵐ x ∂(ENNReal.ofReal ((1 : ℝ) / 2) • Measure.dirac (-(1 : ℝ) / 4) +
    ENNReal.ofReal ((1 : ℝ) / 2) • Measure.dirac ((1 : ℝ) / 4)), |x| ≤ (1 : ℝ) / 2
  rw [ae_add_measure_iff]
  constructor <;>
    rw [Measure.ae_ennreal_smul_measure_iff
      (by norm_num : ENNReal.ofReal ((1 : ℝ) / 2) ≠ 0),
      ae_dirac_eq] <;> norm_num

/-- A fully constructed bounded centered probability source refutes a universal
raw tilt bound of one at every nonzero real tilt. This is not a Haar assertion. -/
theorem symmetricTwoPoint_raw_tilt_gt_one (α : ℝ) (hα : α ≠ 0) :
    1 < ∫ x, Real.exp (α * x) ∂symmetricTwoPoint := by
  apply one_lt_integral_exp_of_centered_nonzero symmetricTwoPoint id
    measurable_id.aemeasurable α (1 / 2) hα symmetricTwoPoint_source_bound
  · norm_num [symmetricTwoPoint_integral]
  · norm_num [symmetricTwoPoint_integral]

end Workhouse.SourceTilt
