/-
Positive spectral-measure decay and the localization interface, reconstructed
from docs/derivations/yangmills-reconstruction.md, R1 and R6--R7. The energy
space is NNReal, so nonnegative spectral support is represented in the type.
No reconstruction or Wilson correlation estimate is postulated as a theorem.
-/
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.Normed.Operator.Basic
import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.ConjTranspose
import Mathlib.Tactic

open MeasureTheory Filter
open scoped Topology NNReal

namespace Workhouse.SpectralReconstruction

/-- The physical Laplace correlation of a finite positive energy measure. -/
noncomputable def laplaceCorrelation (sigma : Measure ℝ≥0) (t : ℝ) : ℝ :=
  ∫ energy, Real.exp (-t * (energy : ℝ)) ∂sigma

/-- Positivity of energy makes the Laplace integrand bounded and integrable
for every nonnegative physical time. Integrability is derived, not assumed. -/
theorem laplace_integrable (sigma : Measure ℝ≥0) [IsFiniteMeasure sigma]
    (t : ℝ) (ht : 0 ≤ t) :
    Integrable (fun energy : ℝ≥0 => Real.exp (-t * (energy : ℝ))) sigma := by
  have hc : Continuous (fun energy : ℝ≥0 => Real.exp (-t * (energy : ℝ))) := by
    fun_prop
  apply (integrable_const (1 : ℝ)).mono' hc.aestronglyMeasurable
  filter_upwards with energy
  rw [Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
  exact Real.exp_le_one_iff.mpr
    (mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.mpr ht) energy.coe_nonneg)

/-- R1, before division by the positive exponential: the mass below energy
`a` is bounded by the actual positive Laplace integral. -/
theorem low_energy_laplace_lower_bound (sigma : Measure ℝ≥0) [IsFiniteMeasure sigma]
    (a : ℝ≥0) (t : ℝ) (ht : 0 ≤ t) :
    Real.exp (-t * (a : ℝ)) * sigma.real (Set.Iic a) ≤ laplaceCorrelation sigma t := by
  have hint := laplace_integrable sigma t ht
  have hlocal : Real.exp (-t * (a : ℝ)) * sigma.real (Set.Iic a) ≤
      ∫ energy in Set.Iic a, Real.exp (-t * (energy : ℝ)) ∂sigma := by
    apply setIntegral_ge_of_const_le_real measurableSet_Iic (measure_ne_top _ _)
      (fun energy henergy => ?_) hint.integrableOn
    apply Real.exp_le_exp.mpr
    exact mul_le_mul_of_nonpos_left (by exact_mod_cast henergy) (neg_nonpos.mpr ht)
  exact hlocal.trans (setIntegral_le_integral hint
    (Filter.Eventually.of_forall fun _ => (Real.exp_pos _).le))

/-- R1: spectral mass below `a` is at most exp(a*t) times the correlation. -/
theorem low_energy_mass_bound (sigma : Measure ℝ≥0) [IsFiniteMeasure sigma]
    (a : ℝ≥0) (t : ℝ) (ht : 0 ≤ t) :
    sigma.real (Set.Iic a) ≤ Real.exp ((a : ℝ) * t) * laplaceCorrelation sigma t := by
  have hcancel : Real.exp ((a : ℝ) * t) * Real.exp (-t * (a : ℝ)) = 1 := by
    rw [← Real.exp_add]
    rw [show (a : ℝ) * t + -t * (a : ℝ) = 0 by ring, Real.exp_zero]
  calc
    sigma.real (Set.Iic a) = Real.exp ((a : ℝ) * t) *
        (Real.exp (-t * (a : ℝ)) * sigma.real (Set.Iic a)) := by
      rw [← mul_assoc, hcancel, one_mul]
    _ ≤ _ := mul_le_mul_of_nonneg_left (low_energy_laplace_lower_bound sigma a t ht)
      (Real.exp_pos _).le

/-- R1: an actual exponential correlation bound excludes every closed
low-energy interval strictly below the common rate. -/
theorem laplace_decay_excludes_low_energy (sigma : Measure ℝ≥0) [IsFiniteMeasure sigma]
    (A eta : ℝ) (hdecay : ∀ t : ℝ, 0 ≤ t →
      laplaceCorrelation sigma t ≤ A * Real.exp (-eta * t))
    (a : ℝ≥0) (ha : (a : ℝ) < eta) : sigma (Set.Iic a) = 0 := by
  have hbound : ∀ t : ℝ, 0 ≤ t → sigma.real (Set.Iic a) ≤
      A * Real.exp (-((eta - (a : ℝ)) * t)) := by
    intro t ht
    calc
      sigma.real (Set.Iic a) ≤ Real.exp ((a : ℝ) * t) * laplaceCorrelation sigma t :=
        low_energy_mass_bound sigma a t ht
      _ ≤ Real.exp ((a : ℝ) * t) * (A * Real.exp (-eta * t)) :=
        mul_le_mul_of_nonneg_left (hdecay t ht) (Real.exp_pos _).le
      _ = A * Real.exp (-((eta - (a : ℝ)) * t)) := by
        rw [← mul_assoc, mul_comm (Real.exp _) A, mul_assoc, ← Real.exp_add]
        congr 2
        ring
  have hlim : Tendsto (fun t : ℝ => A * Real.exp (-((eta - (a : ℝ)) * t)))
      atTop (𝓝 0) := by
    have he := Real.tendsto_exp_neg_atTop_nhds_zero.comp
      (tendsto_id.const_mul_atTop (sub_pos.mpr ha))
    simpa using he.const_mul A
  have hzero : sigma.real (Set.Iic a) = 0 := by
    apply le_antisymm
    · exact ge_of_tendsto hlim (eventually_atTop.2 ⟨0, fun t ht => hbound t ht⟩)
    · exact measureReal_nonneg
  exact (measureReal_eq_zero_iff (measure_ne_top _ _)).mp hzero

/-- R1: countable exhaustion upgrades the closed-interval conclusion to
zero measure of the entire open energy interval below the positive rate. -/
theorem laplace_decay_support_gap (sigma : Measure ℝ≥0) [IsFiniteMeasure sigma]
    (A : ℝ) (eta : ℝ≥0) (heta : 0 < eta)
    (hdecay : ∀ t : ℝ, 0 ≤ t → laplaceCorrelation sigma t ≤
      A * Real.exp (-(eta : ℝ) * t)) : sigma (Set.Iio eta) = 0 := by
  let cutoff : ℕ → ℝ≥0 := fun n => eta * ((n : ℝ≥0) / ((n : ℝ≥0) + 1))
  have hcut : ∀ n, cutoff n < eta := by
    intro n
    dsimp [cutoff]
    calc
      eta * ((n : ℝ≥0) / ((n : ℝ≥0) + 1)) < eta * 1 := by
        apply mul_lt_mul_of_pos_left _ heta
        exact (div_lt_one (by positivity)).2 (by simp)
      _ = eta := mul_one _
  have hlim : Tendsto cutoff atTop (𝓝 eta) := by
    simpa [cutoff] using
      (tendsto_natCast_div_add_atTop (1 : ℝ≥0)).const_mul eta
  rw [← iUnion_Iic_eq_Iio_of_lt_of_tendsto hcut hlim]
  apply measure_iUnion_null
  intro n
  exact laplace_decay_excludes_low_energy sigma A (eta : ℝ) hdecay (cutoff n)
    (by exact_mod_cast hcut n)

/-- R6--R7: the balancing radius is admissible at every physical time. -/
theorem balancing_radius_nonneg (eta alpha beta t : ℝ)
    (heta : 0 < eta) (halpha : 0 ≤ alpha) (hbeta : 0 < beta) (ht : 0 ≤ t) :
    0 ≤ eta * t / (alpha + beta) := by positivity

/-- R7: the balanced decay rate is strictly positive under its actual hypotheses. -/
theorem balanced_rate_pos (eta alpha beta : ℝ)
    (heta : 0 < eta) (halpha : 0 ≤ alpha) (hbeta : 0 < beta) :
    0 < eta * beta / (alpha + beta) := by positivity

/-- R6--R7: simultaneous localization and time estimates imply an actual
single-rate correlation estimate, with no fixed error plateau. -/
theorem localization_balanced_decay (correlation : ℝ → ℝ) (A B eta alpha beta : ℝ)
    (heta : 0 < eta) (halpha : 0 ≤ alpha) (hbeta : 0 < beta)
    (hlocal : ∀ R t : ℝ, 0 ≤ R → 0 ≤ t →
      correlation t ≤ A * Real.exp (-eta * t + alpha * R) + B * Real.exp (-beta * R))
    (t : ℝ) (ht : 0 ≤ t) :
    correlation t ≤ (A + B) * Real.exp (-(eta * beta / (alpha + beta)) * t) := by
  have hden : alpha + beta ≠ 0 := ne_of_gt (by linarith)
  have h1 : -eta * t + alpha * (eta * t / (alpha + beta)) =
      -(eta * beta / (alpha + beta)) * t := by field_simp; ring
  have h2 : -beta * (eta * t / (alpha + beta)) =
      -(eta * beta / (alpha + beta)) * t := by ring
  have h := hlocal (eta * t / (alpha + beta)) t
    (balancing_radius_nonneg eta alpha beta t heta halpha hbeta ht) ht
  rw [h1, h2, ← add_mul] at h
  exact h

/-- R1 plus R6--R7: the actual finite positive spectral measure has no mass
below the balanced rate. This composes the analytic integral argument with
the localization estimate instead of assuming the support conclusion. -/
theorem localization_excludes_low_energy (sigma : Measure ℝ≥0) [IsFiniteMeasure sigma]
    (A B eta alpha beta : ℝ)
    (heta : 0 < eta) (halpha : 0 ≤ alpha) (hbeta : 0 < beta)
    (hlocal : ∀ R t : ℝ, 0 ≤ R → 0 ≤ t → laplaceCorrelation sigma t ≤
      A * Real.exp (-eta * t + alpha * R) + B * Real.exp (-beta * R))
    (a : ℝ≥0) (ha : (a : ℝ) < eta * beta / (alpha + beta)) :
    sigma (Set.Iic a) = 0 := by
  apply laplace_decay_excludes_low_energy sigma (A + B) (eta * beta / (alpha + beta))
    (fun t ht => localization_balanced_decay (laplaceCorrelation sigma)
      A B eta alpha beta heta halpha hbeta hlocal t ht) a ha

section Density

variable {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup F] [NormedSpace ℝ F]

/-- R1 observable completeness: a bounded operator vanishing on a family
with dense linear span vanishes on the entire Hilbert/normed space. The
spectral projection is an application; its boundedness is represented by P. -/
theorem projection_zero_from_total_family (P : E →L[ℝ] F) (family : Set E)
    (htotal : Dense (Submodule.span ℝ family : Set E))
    (hzero : ∀ x ∈ family, P x = 0) : P = 0 := by
  apply ContinuousLinearMap.ext_on htotal
  intro x hx
  simpa using hzero x hx

/-- R1 with observable completeness assembled: actual positive spectral
measures for a total family, their projection-norm identities, and a common
decay rate imply that the bounded low-energy projection vanishes globally.
The prefactor is permitted to depend on the individual observable. -/
theorem total_family_spectral_projection_gap (P : E →L[ℝ] F)
    (family : Set E) (htotal : Dense (Submodule.span ℝ family : Set E))
    (sigma : E → Measure ℝ≥0)
    (hfinite : ∀ x ∈ family, IsFiniteMeasure (sigma x))
    (eta : ℝ) (a : ℝ≥0) (ha : (a : ℝ) < eta)
    (hspectral : ∀ x ∈ family, (sigma x).real (Set.Iic a) = ‖P x‖ ^ 2)
    (hdecay : ∀ x ∈ family, ∃ A : ℝ, ∀ t : ℝ, 0 ≤ t →
      laplaceCorrelation (sigma x) t ≤ A * Real.exp (-eta * t)) : P = 0 := by
  apply projection_zero_from_total_family P family htotal
  intro x hx
  let _ : IsFiniteMeasure (sigma x) := hfinite x hx
  obtain ⟨A, hA⟩ := hdecay x hx
  have hm := laplace_decay_excludes_low_energy (sigma x) A eta hA a ha
  have hr : (sigma x).real (Set.Iic a) = 0 :=
    (measureReal_eq_zero_iff (measure_ne_top _ _)).mpr hm
  rw [hspectral x hx] at hr
  exact norm_eq_zero.mp (sq_eq_zero_iff.mp hr)

/-- R1/R6/R7 composed with totality: vector-dependent localization
prefactors and common rates force the whole low-energy projection to vanish. -/
theorem total_family_localization_projection_gap (P : E →L[ℝ] F)
    (family : Set E) (htotal : Dense (Submodule.span ℝ family : Set E))
    (sigma : E → Measure ℝ≥0)
    (hfinite : ∀ x ∈ family, IsFiniteMeasure (sigma x))
    (eta alpha beta : ℝ) (heta : 0 < eta) (halpha : 0 ≤ alpha) (hbeta : 0 < beta)
    (a : ℝ≥0) (ha : (a : ℝ) < eta * beta / (alpha + beta))
    (hspectral : ∀ x ∈ family, (sigma x).real (Set.Iic a) = ‖P x‖ ^ 2)
    (hlocal : ∀ x ∈ family, ∃ A B : ℝ, ∀ R t : ℝ, 0 ≤ R → 0 ≤ t →
      laplaceCorrelation (sigma x) t ≤
        A * Real.exp (-eta * t + alpha * R) + B * Real.exp (-beta * R)) : P = 0 := by
  apply total_family_spectral_projection_gap P family htotal sigma hfinite
    (eta * beta / (alpha + beta)) a ha hspectral
  intro x hx
  obtain ⟨A, B, hAB⟩ := hlocal x hx
  exact ⟨A + B, fun t ht => localization_balanced_decay (laplaceCorrelation (sigma x))
    A B eta alpha beta heta halpha hbeta hAB t ht⟩

end Density

section FiniteReflection

open scoped ComplexConjugate

variable {J : Type*}

/-- The actual finite-mode correlation sequence in R2. -/
def finiteCorrelation (modes : Finset J) (weight ratio : J → ℝ) (n : ℕ) : ℝ :=
  ∑ j ∈ modes, weight j * ratio j ^ n

/-- The finite-time mode amplitude, including the actual complex coefficients. -/
def modeAmplitude (times : Finset ℕ) (coeff : ℕ → ℂ) (ratio : ℝ) : ℂ :=
  ∑ k ∈ times, coeff k * (ratio : ℂ) ^ k

/-- R2: the exact complex reflection-kernel Gram factorization for arbitrary
finite sets of modes and times, not merely a fixed small matrix. -/
theorem reflection_kernel_gram (modes : Finset J) (times : Finset ℕ)
    (weight ratio : J → ℝ) (coeff : ℕ → ℂ) :
    (∑ k ∈ times, ∑ l ∈ times,
      conj (coeff k) * coeff l * (finiteCorrelation modes weight ratio (k + l) : ℂ)) =
    ∑ j ∈ modes, (weight j : ℂ) * (Complex.normSq (modeAmplitude times coeff (ratio j)) : ℂ) := by
  simp only [finiteCorrelation, Complex.ofReal_sum, Complex.ofReal_mul, Complex.ofReal_pow,
    Finset.mul_sum]
  simp_rw [Finset.sum_comm (s := times) (t := modes)]
  apply Finset.sum_congr rfl
  intro j hj
  rw [Complex.normSq_eq_conj_mul_self]
  simp only [modeAmplitude, map_sum, map_mul, map_pow, Complex.conj_ofReal,
    Finset.mul_sum, Finset.sum_mul, pow_add]
  rw [Finset.sum_comm (s := times) (t := times)]
  apply Finset.sum_congr rfl
  intro k hk
  apply Finset.sum_congr rfl
  intro l hl
  ring

/-- R2: nonnegative mode weights make the complex reflection quadratic
form nonnegative for every finite complex time-coefficient vector. -/
theorem reflection_kernel_nonnegative (modes : Finset J) (times : Finset ℕ)
    (weight ratio : J → ℝ) (coeff : ℕ → ℂ)
    (hweight : ∀ j ∈ modes, 0 ≤ weight j) :
    0 ≤ (∑ k ∈ times, ∑ l ∈ times,
      conj (coeff k) * coeff l * (finiteCorrelation modes weight ratio (k + l) : ℂ)).re := by
  rw [reflection_kernel_gram]
  simp only [Complex.re_sum, Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im,
    mul_zero, sub_zero]
  exact Finset.sum_nonneg fun j hj => mul_nonneg (hweight j hj) (Complex.normSq_nonneg _)

/-- The physical energy belonging to one positive transfer eigenvalue. -/
noncomputable def transferEnergy (ratio step : ℝ) : ℝ := -Real.log ratio / step

/-- R2: positive contraction eigenvalues correspond to nonnegative energy
in the specified positive physical time step. -/
theorem transfer_energy_nonnegative (ratio step : ℝ) (hr : 0 < ratio)
    (hr1 : ratio ≤ 1) (hstep : 0 < step) : 0 ≤ transferEnergy ratio step := by
  exact div_nonneg (neg_nonneg.mpr (Real.log_nonpos hr.le hr1)) hstep.le

/-- R2: the time-step convention is exact: exp(-a E)=r. -/
theorem transfer_energy_reconstructs_ratio (ratio step : ℝ) (hr : 0 < ratio)
    (hstep : 0 < step) : Real.exp (-step * transferEnergy ratio step) = ratio := by
  have he : -step * transferEnergy ratio step = Real.log ratio := by
    dsimp [transferEnergy]
    field_simp
  rw [he, Real.exp_log hr]

/-- R2: every discrete-time mode equals its physical-time exponential. -/
theorem transfer_power_eq_physical_decay (ratio step : ℝ) (hr : 0 < ratio)
    (hstep : 0 < step) (n : ℕ) :
    ratio ^ n = Real.exp (-(step * (n : ℝ)) * transferEnergy ratio step) := by
  calc
    ratio ^ n = (Real.exp (-step * transferEnergy ratio step)) ^ n := by
      rw [transfer_energy_reconstructs_ratio ratio step hr hstep]
    _ = Real.exp (-(step * (n : ℝ)) * transferEnergy ratio step) := by
      rw [← Real.exp_nat_mul]
      congr 1
      ring

end FiniteReflection

section FiniteFrame

/-- The exact three-observable, two-sector frame from R3. -/
def observableFrame : Matrix (Fin 3) (Fin 2) ℂ := !![1, 1; 1, -1; 0, 1]

/-- R3: the actual conjugate-transpose Gram matrix is diag(2,3). -/
theorem observable_frame_gram :
    observableFrame.conjTranspose * observableFrame = !![2, 0; 0, 3] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [observableFrame, Matrix.mul_apply, Fin.sum_univ_succ]

/-- R3: the exact Euclidean squared-norm excess of the frame is the
second coordinate's squared norm, including arbitrary complex vectors. -/
theorem observable_frame_energy (v : Fin 2 → ℂ) :
    (∑ i : Fin 3, Complex.normSq (observableFrame.mulVec v i)) -
      2 * (∑ j : Fin 2, Complex.normSq (v j)) = Complex.normSq (v 1) := by
  simp [observableFrame, Matrix.mulVec, dotProduct, Fin.sum_univ_succ,
    Complex.normSq_apply]
  ring

/-- R3: the actual full frame has lower frame bound two on both sectors. -/
theorem observable_frame_lower_bound (v : Fin 2 → ℂ) :
    2 * (∑ j : Fin 2, Complex.normSq (v j)) ≤
      ∑ i : Fin 3, Complex.normSq (observableFrame.mulVec v i) := by
  have h := observable_frame_energy v
  have hp := Complex.normSq_nonneg (v 1)
  linarith

/-- R3: summing the three actual observable correlators gives positive
weights two and three on the respective physical modes. -/
theorem observable_frame_correlation (r1 r2 : ℝ) (n : ℕ) :
    (∑ i : Fin 3, (Complex.normSq (observableFrame i 0) * r1 ^ n +
      Complex.normSq (observableFrame i 1) * r2 ^ n)) =
      2 * r1 ^ n + 3 * r2 ^ n := by
  norm_num [observableFrame, Fin.sum_univ_succ, Complex.normSq_apply]
  ring

/-- Keeping only the source's final observable row discards the first sector. -/
def deletedObservableFrame : Matrix (Fin 1) (Fin 2) ℂ := !![0, 1]

/-- R3: an explicit nonzero vector is invisible after the specified row deletion. -/
theorem deleted_frame_invisible_sector :
    (![1, 0] : Fin 2 → ℂ) ≠ 0 ∧
      deletedObservableFrame.mulVec (![1, 0] : Fin 2 → ℂ) = 0 := by
  constructor
  · intro h
    have h0 := congrFun h 0
    norm_num at h0
  · ext i
    fin_cases i
    norm_num [deletedObservableFrame, Matrix.mulVec, dotProduct, Fin.sum_univ_succ]

end FiniteFrame

end Workhouse.SpectralReconstruction
