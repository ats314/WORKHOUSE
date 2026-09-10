/-
# Vacuum-aligned projection assembly and weighted Poincare comparison

Sources: wilson-vacuum-aligned-assembly.md VA10--VA14;
wilson-true-vacuum-block-estimates.md BA2 and BA8;
yangmills-weighted-curvature.md GST-3a--GST-4.

The projection algebra is valid on an arbitrary real inner product space.
The spectral bridges prove, rather than assume, the gap implication from
T^2 >= delta T: one uses finite-dimensional diagonalization and another uses
the continuous functional calculus on arbitrary complex Hilbert spaces.
The latter yields an arbitrary-dimensional bounded projection assembly theorem.
Density comparison and covariance minorization are proved both for finite
probability spaces and genuine probability measures on arbitrary measurable
spaces, including Radon--Nikodym bounds, actual marginals and L2 transport.

These theorems do not construct the Wilson ground measure, conditional
expectations, SU(2) heat kernel, or infinite-dimensional operator domains.
-/
import Mathlib.Analysis.InnerProductSpace.Spectrum
import Mathlib.Analysis.InnerProductSpace.StarOrder
import Mathlib.Analysis.SpecialFunctions.ContinuousFunctionalCalculus.Rpow.Basic
import Mathlib.MeasureTheory.Measure.Sub
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.Probability.Moments.Variance
import Mathlib.Tactic

namespace Workhouse.GroundStateAssembly

open scoped BigOperators ENNReal
open Finset

section Probability

variable {ι : Type*} [Fintype ι]

/-- Mean with respect to a finite weight. -/
noncomputable def mean (w f : ι → ℝ) : ℝ := ∑ i, w i * f i

/-- Variance about the weighted mean; probability normalization is a theorem premise. -/
noncomputable def variance (w f : ι → ℝ) : ℝ :=
  ∑ i, w i * (f i - mean w f) ^ 2

/-- The second-moment identity includes the normalization hypothesis explicitly. -/
theorem variance_eq_second_moment (w f : ι → ℝ) (hw : ∑ i, w i = 1) :
    variance w f = (∑ i, w i * f i ^ 2) - mean w f ^ 2 := by
  unfold variance
  calc
    (∑ i, w i * (f i - mean w f) ^ 2) =
        (∑ i, w i * f i ^ 2) - 2 * mean w f * (∑ i, w i * f i) +
          mean w f ^ 2 * ∑ i, w i := by
      simp only [mul_sum, ← sum_sub_distrib, ← sum_add_distrib]
      apply sum_congr rfl
      intro i _
      ring
    _ = _ := by rw [hw]; change _ - 2 * mean w f * mean w f + _ = _; ring

/-- The mean minimizes the squared deviation; this is the variance-infimum step. -/
theorem variance_le_deviation (w f : ι → ℝ) (hw : ∑ i, w i = 1) (a : ℝ) :
    variance w f ≤ ∑ i, w i * (f i - a) ^ 2 := by
  have hid : (∑ i, w i * (f i - a) ^ 2) =
      variance w f + (a - mean w f) ^ 2 := by
    rw [variance_eq_second_moment w f hw]
    calc
      (∑ i, w i * (f i - a) ^ 2) =
          (∑ i, w i * f i ^ 2) - 2 * a * mean w f + a ^ 2 * (∑ i, w i) := by
        unfold mean
        simp only [mul_sum, ← sum_sub_distrib, ← sum_add_distrib]
        apply sum_congr rfl
        intro i _
        ring
      _ = _ := by rw [hw]; ring
  rw [hid]
  exact le_add_of_nonneg_right (sq_nonneg _)

/-- Density domination compares variance after optimizing its center. -/
theorem variance_density_upper (w v f : ι → ℝ) (hw : ∑ i, w i = 1)
    (M : ℝ) (hdom : ∀ i, w i ≤ M * v i) :
    variance w f ≤ M * variance v f := by
  calc
    variance w f ≤ ∑ i, w i * (f i - mean v f) ^ 2 :=
      variance_le_deviation w f hw (mean v f)
    _ ≤ ∑ i, (M * v i) * (f i - mean v f) ^ 2 :=
      sum_le_sum fun i _ => mul_le_mul_of_nonneg_right (hdom i) (sq_nonneg _)
    _ = M * variance v f := by unfold variance; rw [mul_sum]; congr 1; ext i; ring

/-- Full finite density-comparison theorem, the variational step in VA10/BA2.
`energy f i` is the local nonnegative squared gradient (or another energy density).
The reference Poincare inequality is an explicit input; the perturbed one is proved.
The division-free form has constant M C / m when m is positive. -/
theorem poincare_density_comparison (w v : ι → ℝ) (energy : (ι → ℝ) → ι → ℝ)
    (m M C : ℝ) (hw : ∑ i, w i = 1) (hm : 0 ≤ m) (hM : 0 ≤ M) (hC : 0 ≤ C)
    (hlower : ∀ i, m * v i ≤ w i) (hupper : ∀ i, w i ≤ M * v i)
    (henergy : ∀ f i, 0 ≤ energy f i)
    (hreference : ∀ f, variance v f ≤ C * ∑ i, v i * energy f i)
    (f : ι → ℝ) :
    m * variance w f ≤ M * C * ∑ i, w i * energy f i := by
  have hvar := variance_density_upper w v f hw M hupper
  have hen : m * (∑ i, v i * energy f i) ≤ ∑ i, w i * energy f i := by
    rw [mul_sum]
    apply sum_le_sum
    intro i _
    simpa [mul_assoc] using mul_le_mul_of_nonneg_right (hlower i) (henergy f i)
  calc
    m * variance w f ≤ m * (M * variance v f) := mul_le_mul_of_nonneg_left hvar hm
    _ ≤ m * (M * (C * ∑ i, v i * energy f i)) :=
      mul_le_mul_of_nonneg_left
        (mul_le_mul_of_nonneg_left (hreference f) hM) hm
    _ = M * C * (m * ∑ i, v i * energy f i) := by ring
    _ ≤ M * C * ∑ i, w i * energy f i :=
      mul_le_mul_of_nonneg_left hen (mul_nonneg hM hC)

/-- Cauchy--Schwarz for an arbitrary nonnegative finite weight, without normalization. -/
theorem weighted_cauchy_schwarz_sq (w a b : ι → ℝ) (hw : ∀ i, 0 ≤ w i) :
    (∑ i, w i * a i * b i) ^ 2 ≤
      (∑ i, w i * a i ^ 2) * ∑ i, w i * b i ^ 2 := by
  simpa using Finset.sum_sq_le_sum_mul_sum_of_sq_le_mul (R := ℝ)
    (s := Finset.univ) (r := fun i => w i * a i * b i)
    (f := fun i => w i * a i ^ 2) (g := fun i => w i * b i ^ 2)
    (fun i _ => mul_nonneg (hw i) (sq_nonneg _))
    (fun i _ => mul_nonneg (hw i) (sq_nonneg _))
    (fun i _ => by nlinarith [sq_nonneg (w i * a i * b i)])

/-- BA7/VA16's product-minorization argument, including construction of the
nonnegative remainder and its two marginals. The squared formulation avoids
square-root side conditions. It bounds all centered observables, not a sample
of selected correlations. This version is on arbitrary finite probability spaces. -/
theorem product_minorization_covariance
    {J : Type*} [Fintype J] (p : ι → J → ℝ) (u : ι → ℝ) (v : J → ℝ)
    (α : ℝ) (hu : ∑ i, u i = 1) (hv : ∑ j, v j = 1)
    (hrow : ∀ i, ∑ j, p i j = u i) (hcol : ∀ j, ∑ i, p i j = v j)
    (hminor : ∀ i j, α * u i * v j ≤ p i j)
    (f : ι → ℝ) (g : J → ℝ)
    (hf : ∑ i, u i * f i = 0) :
    (∑ i, ∑ j, p i j * f i * g j) ^ 2 ≤
      (1 - α) ^ 2 * (∑ i, u i * f i ^ 2) * ∑ j, v j * g j ^ 2 := by
  let r : ι → J → ℝ := fun i j => p i j - α * u i * v j
  have hr : ∀ i j, 0 ≤ r i j := fun i j => sub_nonneg.mpr (hminor i j)
  have hrrow : ∀ i, ∑ j, r i j = (1 - α) * u i := by
    intro i
    simp only [r, sum_sub_distrib, ← mul_sum, hrow, hv, mul_one]
    ring
  have hrcol : ∀ j, ∑ i, r i j = (1 - α) * v j := by
    intro j
    simp only [r, sum_sub_distrib, ← sum_mul, ← mul_sum, hcol, hu, mul_one]
    ring
  have hcov : (∑ i, ∑ j, r i j * f i * g j) = ∑ i, ∑ j, p i j * f i * g j := by
    have hz : (∑ i, ∑ j, (α * u i * v j) * f i * g j) = 0 := by
      calc
        (∑ i, ∑ j, (α * u i * v j) * f i * g j) =
            α * (∑ i, u i * f i) * ∑ j, v j * g j := by
          simp only [mul_sum, sum_mul]
          rw [sum_comm]
          apply sum_congr rfl
          intro i _
          apply sum_congr rfl
          intro j _
          ring
        _ = 0 := by rw [hf]; ring
    simp only [r, sub_mul, sum_sub_distrib, hz, sub_zero]
  have hleft : (∑ i, ∑ j, r i j * f i ^ 2) =
      (1 - α) * ∑ i, u i * f i ^ 2 := by
    simp only [← sum_mul, hrrow, mul_sum, mul_assoc]
  have hright : (∑ i, ∑ j, r i j * g j ^ 2) =
      (1 - α) * ∑ j, v j * g j ^ 2 := by
    rw [sum_comm]
    simp only [← sum_mul, hrcol, mul_sum, mul_assoc]
  have hcs := weighted_cauchy_schwarz_sq (ι := ι × J)
    (fun z => r z.1 z.2) (fun z => f z.1) (fun z => g z.2)
    (fun z => hr z.1 z.2)
  simp only [Fintype.sum_prod_type] at hcs
  rw [hcov, hleft, hright] at hcs
  nlinarith [hcs]

end Probability

section MeasureComparison

open MeasureTheory

variable {Ω : Type*} [MeasurableSpace Ω]

/-- The variance-infimum step for genuine probability measures and L2 observables. -/
theorem measure_variance_le_deviation (μ : Measure Ω) [IsProbabilityMeasure μ]
    (f : Ω → ℝ) (hf : MemLp f 2 μ) (a : ℝ) :
    ProbabilityTheory.variance f μ ≤ ∫ x, (f x - a) ^ 2 ∂μ := by
  rw [← ProbabilityTheory.variance_sub_const hf.aestronglyMeasurable a]
  exact ProbabilityTheory.variance_le_expectation_sq
    (hf.sub (memLp_const a)).aestronglyMeasurable

/-- A measure domination bounds variance after optimizing its center. This is
valid on an arbitrary measurable space and includes continuous group measures. -/
theorem measure_variance_density_upper (μ ν : Measure Ω)
    [IsProbabilityMeasure μ] [IsProbabilityMeasure ν]
    (f : Ω → ℝ) (hfμ : MemLp f 2 μ) (hfν : MemLp f 2 ν)
    (M : ℝ) (hM : 0 ≤ M) (hdom : μ ≤ ENNReal.ofReal M • ν) :
    ProbabilityTheory.variance f μ ≤ M * ProbabilityTheory.variance f ν := by
  have hi : Integrable (fun x => (f x - ∫ y, f y ∂ν) ^ 2)
      (ENNReal.ofReal M • ν) :=
    (hfν.sub (memLp_const _)).integrable_sq.smul_measure ENNReal.ofReal_ne_top
  calc
    ProbabilityTheory.variance f μ ≤ ∫ x, (f x - ∫ y, f y ∂ν) ^ 2 ∂μ :=
      measure_variance_le_deviation μ f hfμ _
    _ ≤ ∫ x, (f x - ∫ y, f y ∂ν) ^ 2 ∂(ENNReal.ofReal M • ν) :=
      integral_mono_measure hdom (Filter.Eventually.of_forall fun x => sq_nonneg _) hi
    _ = M * ProbabilityTheory.variance f ν := by
      rw [integral_smul_measure, ENNReal.toReal_ofReal hM,
        ProbabilityTheory.variance_eq_integral hfν.aemeasurable]
      rfl

/-- IF11: a lower density floor preserves a definite amount of variance.
The target mean is allowed to differ from the reference mean; variance
minimization handles that difference exactly. -/
theorem measure_variance_density_lower (μ ν : Measure Ω)
    [IsProbabilityMeasure μ] [IsProbabilityMeasure ν]
    (f : Ω → ℝ) (hfμ : MemLp f 2 μ) (hfν : MemLp f 2 ν)
    (m : ℝ) (hm : 0 ≤ m) (hdom : ENNReal.ofReal m • ν ≤ μ) :
    m * ProbabilityTheory.variance f ν ≤ ProbabilityTheory.variance f μ := by
  have hi := (hfμ.sub (memLp_const (∫ y, f y ∂μ))).integrable_sq
  calc
    m * ProbabilityTheory.variance f ν ≤ m * ∫ x, (f x - ∫ y, f y ∂μ) ^ 2 ∂ν :=
      mul_le_mul_of_nonneg_left (measure_variance_le_deviation ν f hfν _) hm
    _ = ∫ x, (f x - ∫ y, f y ∂μ) ^ 2 ∂(ENNReal.ofReal m • ν) := by
      rw [integral_smul_measure, ENNReal.toReal_ofReal hm, smul_eq_mul]
    _ ≤ ∫ x, (f x - ∫ y, f y ∂μ) ^ 2 ∂μ :=
      integral_mono_measure hdom (Filter.Eventually.of_forall fun x => sq_nonneg _) hi
    _ = ProbabilityTheory.variance f μ :=
      (ProbabilityTheory.variance_eq_integral hfμ.aemeasurable).symm

/-- IF11 in actual Radon--Nikodym form. A normalized density bounded below by m
gives Var_(w nu) f >= m Var_nu f on every square-integrable real observable. -/
theorem withDensity_variance_floor (ν : Measure Ω) [IsProbabilityMeasure ν]
    (w : Ω → ℝ≥0∞) [IsProbabilityMeasure (ν.withDensity w)]
    (f : Ω → ℝ) (hfμ : MemLp f 2 (ν.withDensity w)) (hfν : MemLp f 2 ν)
    (m : ℝ) (hm : 0 ≤ m) (hminor : ∀ᵐ x ∂ν, ENNReal.ofReal m ≤ w x) :
    m * ProbabilityTheory.variance f ν ≤ ProbabilityTheory.variance f (ν.withDensity w) := by
  apply measure_variance_density_lower (ν.withDensity w) ν f hfμ hfν m hm
  simpa only [withDensity_const] using withDensity_mono hminor

/-- Poincare transfer between probability measures with a two-sided density
bound, for arbitrary square-integrable observables. Integrability of the energy
and the reference inequality are explicit. No finite state-space assumption is used. -/
theorem measure_poincare_comparison (μ ν : Measure Ω)
    [IsProbabilityMeasure μ] [IsProbabilityMeasure ν]
    (f energy : Ω → ℝ) (hfμ : MemLp f 2 μ) (hfν : MemLp f 2 ν)
    (m M C : ℝ) (hm : 0 ≤ m) (hM : 0 ≤ M) (hC : 0 ≤ C)
    (hlower : ENNReal.ofReal m • ν ≤ μ) (hupper : μ ≤ ENNReal.ofReal M • ν)
    (henergy : 0 ≤ᵐ[μ] energy) (henergy_int : Integrable energy μ)
    (hreference : ProbabilityTheory.variance f ν ≤ C * ∫ x, energy x ∂ν) :
    m * ProbabilityTheory.variance f μ ≤ M * C * ∫ x, energy x ∂μ := by
  have hvar := measure_variance_density_upper μ ν f hfμ hfν M hM hupper
  have hen : m * (∫ x, energy x ∂ν) ≤ ∫ x, energy x ∂μ := by
    have h := integral_mono_measure hlower henergy henergy_int
    simpa only [integral_smul_measure, ENNReal.toReal_ofReal hm, smul_eq_mul] using h
  calc
    m * ProbabilityTheory.variance f μ ≤ m * (M * ProbabilityTheory.variance f ν) :=
      mul_le_mul_of_nonneg_left hvar hm
    _ ≤ m * (M * (C * ∫ x, energy x ∂ν)) :=
      mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left hreference hM) hm
    _ = M * C * (m * ∫ x, energy x ∂ν) := by ring
    _ ≤ M * C * ∫ x, energy x ∂μ := mul_le_mul_of_nonneg_left hen (mul_nonneg hM hC)

/-- VA10/BA2 with the density represented by `withDensity`: pointwise a.e.
Radon--Nikodym bounds are converted to the measure-order hypotheses, then the
Poincare inequality is transferred. Probability normalization of the true
density is explicit. The theorem is not limited to discrete approximations. -/
theorem withDensity_poincare_comparison (ν : Measure Ω) [IsProbabilityMeasure ν]
    (w : Ω → ℝ≥0∞) [IsProbabilityMeasure (ν.withDensity w)]
    (f energy : Ω → ℝ) (hfν : MemLp f 2 ν)
    (m M C : ℝ) (hm : 0 ≤ m) (hM : 0 ≤ M) (hC : 0 ≤ C)
    (hlower : ∀ᵐ x ∂ν, ENNReal.ofReal m ≤ w x)
    (hupper : ∀ᵐ x ∂ν, w x ≤ ENNReal.ofReal M)
    (henergy : 0 ≤ᵐ[ν.withDensity w] energy)
    (henergy_int : Integrable energy (ν.withDensity w))
    (hreference : ProbabilityTheory.variance f ν ≤ C * ∫ x, energy x ∂ν) :
    m * ProbabilityTheory.variance f (ν.withDensity w) ≤
      M * C * ∫ x, energy x ∂(ν.withDensity w) := by
  have hupper_measure : ν.withDensity w ≤ ENNReal.ofReal M • ν := by
    simpa only [withDensity_const] using withDensity_mono hupper
  have hfμ : MemLp f 2 (ν.withDensity w) :=
    MemLp.mono_measure hupper_measure (hfν.smul_measure ENNReal.ofReal_ne_top)
  apply measure_poincare_comparison (ν.withDensity w) ν f energy hfμ hfν m M C
    hm hM hC ?_ hupper_measure henergy henergy_int hreference
  · simpa only [withDensity_const] using withDensity_mono hlower

/-- The usual M C / m Poincare constant, with strict positivity of the lower
density floor exposed rather than silently dividing by a potentially zero number. -/
theorem withDensity_poincare_constant (ν : Measure Ω) [IsProbabilityMeasure ν]
    (w : Ω → ℝ≥0∞) [IsProbabilityMeasure (ν.withDensity w)]
    (f energy : Ω → ℝ) (hfν : MemLp f 2 ν)
    (m M C : ℝ) (hm : 0 < m) (hM : 0 ≤ M) (hC : 0 ≤ C)
    (hlower : ∀ᵐ x ∂ν, ENNReal.ofReal m ≤ w x)
    (hupper : ∀ᵐ x ∂ν, w x ≤ ENNReal.ofReal M)
    (henergy : 0 ≤ᵐ[ν.withDensity w] energy)
    (henergy_int : Integrable energy (ν.withDensity w))
    (hreference : ProbabilityTheory.variance f ν ≤ C * ∫ x, energy x ∂ν) :
    ProbabilityTheory.variance f (ν.withDensity w) ≤
      (M * C / m) * ∫ x, energy x ∂(ν.withDensity w) := by
  have h := withDensity_poincare_comparison ν w f energy hfν m M C
    hm.le hM hC hlower hupper henergy henergy_int hreference
  calc
    ProbabilityTheory.variance f (ν.withDensity w) ≤
        (M * C * ∫ x, energy x ∂(ν.withDensity w)) / m :=
      (le_div_iff₀ hm).mpr (by simpa [mul_comm] using h)
    _ = _ := by ring

/-- The inner product of actual L2 classes equals the integral of representatives. -/
theorem integral_mul_eq_L2_inner (μ : Measure Ω) (f g : Ω → ℝ)
    (hf : MemLp f 2 μ) (hg : MemLp g 2 μ) :
    (∫ x, f x * g x ∂μ) = inner ℝ (hf.toLp f) (hg.toLp g) := by
  rw [MeasureTheory.L2.inner_def]
  apply integral_congr_ae
  filter_upwards [hf.coeFn_toLp, hg.coeFn_toLp] with x hfx hgx
  simp only [hfx, hgx, RCLike.inner_apply, conj_trivial]
  ring

/-- Cauchy--Schwarz for real square-integrable observables on an arbitrary measure. -/
theorem integral_cauchy_schwarz_sq (μ : Measure Ω) (f g : Ω → ℝ)
    (hf : MemLp f 2 μ) (hg : MemLp g 2 μ) :
    (∫ x, f x * g x ∂μ) ^ 2 ≤
      (∫ x, f x ^ 2 ∂μ) * ∫ x, g x ^ 2 ∂μ := by
  simpa only [pow_two, integral_mul_eq_L2_inner μ f g hf hg,
    integral_mul_eq_L2_inner μ f f hf hf, integral_mul_eq_L2_inner μ g g hg hg] using
    real_inner_mul_inner_self_le (hf.toLp f) (hg.toLp g)

/-- Subtracting a dominated finite reference measure gives an actual remainder
measure. This integral identity is used to compute both its marginals/energies;
no signed-density heuristic or normalization assumption is needed. -/
theorem integral_remainder_measure (μ ν : Measure Ω) [IsFiniteMeasure ν]
    (α : ℝ) (hα : 0 ≤ α) (hdom : ENNReal.ofReal α • ν ≤ μ)
    (f : Ω → ℝ) (hfμ : Integrable f μ) (hfν : Integrable f ν) :
    (∫ x, f x ∂(μ - ENNReal.ofReal α • ν)) =
      (∫ x, f x ∂μ) - α * ∫ x, f x ∂ν := by
  have : IsFiniteMeasure (ENNReal.ofReal α • ν) :=
    ⟨by simp only [Measure.smul_apply, smul_eq_mul]; finiteness⟩
  have hsum : μ - ENNReal.ofReal α • ν + ENNReal.ofReal α • ν = μ :=
    Measure.sub_add_cancel_of_le hdom
  have hr := hfμ.mono_measure (Measure.sub_le (μ := μ) (ν := ENNReal.ofReal α • ν))
  have ha := hfν.smul_measure (c := ENNReal.ofReal α) ENNReal.ofReal_ne_top
  have hid := integral_add_measure hr ha
  rw [hsum, integral_smul_measure, ENNReal.toReal_ofReal hα, smul_eq_mul] at hid
  linarith

/-- Continuous-measure minorization covariance theorem. The base/reference
cross moment vanishes, and both second moments agree with the target measure.
The remainder μ−αν is constructed, its two energies become (1−α) times the
original energies, and L2 Cauchy--Schwarz proves the full correlation bound. -/
theorem measure_minorization_covariance (μ ν : Measure Ω) [IsFiniteMeasure ν]
    (α : ℝ) (hα : 0 ≤ α) (hdom : ENNReal.ofReal α • ν ≤ μ)
    (f g : Ω → ℝ) (hfμ : MemLp f 2 μ) (hgμ : MemLp g 2 μ)
    (hfν : MemLp f 2 ν) (hgν : MemLp g 2 ν)
    (hcross : (∫ x, f x * g x ∂ν) = 0)
    (hfsq : (∫ x, f x ^ 2 ∂μ) = ∫ x, f x ^ 2 ∂ν)
    (hgsq : (∫ x, g x ^ 2 ∂μ) = ∫ x, g x ^ 2 ∂ν) :
    (∫ x, f x * g x ∂μ) ^ 2 ≤
      (1 - α) ^ 2 * (∫ x, f x ^ 2 ∂μ) * ∫ x, g x ^ 2 ∂μ := by
  let η := μ - ENNReal.ofReal α • ν
  have hle : η ≤ μ := Measure.sub_le
  have hcov : (∫ x, f x * g x ∂η) = ∫ x, f x * g x ∂μ := by
    change (∫ x, (f * g) x ∂(μ - ENNReal.ofReal α • ν)) = _
    rw [integral_remainder_measure μ ν α hα hdom _ (hfμ.integrable_mul hgμ)
      (hfν.integrable_mul hgν)]
    change (∫ x, f x * g x ∂μ) - α * (∫ x, f x * g x ∂ν) = _
    rw [hcross]
    ring
  have hleft : (∫ x, f x ^ 2 ∂η) = (1 - α) * ∫ x, f x ^ 2 ∂μ := by
    rw [integral_remainder_measure μ ν α hα hdom _ hfμ.integrable_sq hfν.integrable_sq,
      ← hfsq]
    ring
  have hright : (∫ x, g x ^ 2 ∂η) = (1 - α) * ∫ x, g x ^ 2 ∂μ := by
    rw [integral_remainder_measure μ ν α hα hdom _ hgμ.integrable_sq hgν.integrable_sq,
      ← hgsq]
    ring
  have hcs := integral_cauchy_schwarz_sq η f g
    (MemLp.mono_measure hle hfμ) (MemLp.mono_measure hle hgμ)
  rw [hcov, hleft, hright] at hcs
  nlinarith [hcs]

/-- VA16/BA7 for genuine joint probability measures with their actual marginals.
If μ dominates α times the product of its marginals, every centered L2 block
observable has covariance at most (1−α) times the product of its L2 norms
(stated in squared form). This removes the finite-distribution restriction. -/
theorem joint_measure_minorization_covariance
    {X Y : Type*} [MeasurableSpace X] [MeasurableSpace Y]
    (μ : Measure (X × Y)) (μX : Measure X) (μY : Measure Y)
    [IsProbabilityMeasure μ] [IsProbabilityMeasure μX] [IsProbabilityMeasure μY]
    (hfst : Measure.map Prod.fst μ = μX) (hsnd : Measure.map Prod.snd μ = μY)
    (α : ℝ) (hα : 0 ≤ α) (hdom : ENNReal.ofReal α • μX.prod μY ≤ μ)
    (f : X → ℝ) (g : Y → ℝ) (hf : MemLp f 2 μX) (hg : MemLp g 2 μY)
    (hcenter : (∫ x, f x ∂μX) = 0) :
    (∫ z, f z.1 * g z.2 ∂μ) ^ 2 ≤
      (1 - α) ^ 2 * (∫ x, f x ^ 2 ∂μX) * ∫ y, g y ^ 2 ∂μY := by
  have mpfst : MeasurePreserving Prod.fst μ μX := ⟨measurable_fst, hfst⟩
  have mpsnd : MeasurePreserving Prod.snd μ μY := ⟨measurable_snd, hsnd⟩
  have hfμ : MemLp (fun z : X × Y => f z.1) 2 μ := hf.comp_measurePreserving mpfst
  have hgμ : MemLp (fun z : X × Y => g z.2) 2 μ := hg.comp_measurePreserving mpsnd
  have hfprod : MemLp (fun z : X × Y => f z.1) 2 (μX.prod μY) :=
    hf.comp_measurePreserving measurePreserving_fst
  have hgprod : MemLp (fun z : X × Y => g z.2) 2 (μX.prod μY) :=
    hg.comp_measurePreserving measurePreserving_snd
  have hfsq : (∫ z, f z.1 ^ 2 ∂μ) = ∫ x, f x ^ 2 ∂μX := by
    rw [← hfst]
    exact (integral_map measurable_fst.aemeasurable
      (hfst ▸ hf.integrable_sq.aestronglyMeasurable)).symm
  have hgsq : (∫ z, g z.2 ^ 2 ∂μ) = ∫ y, g y ^ 2 ∂μY := by
    rw [← hsnd]
    exact (integral_map measurable_snd.aemeasurable
      (hsnd ▸ hg.integrable_sq.aestronglyMeasurable)).symm
  have hb := measure_minorization_covariance μ (μX.prod μY) α hα hdom
    (fun z => f z.1) (fun z => g z.2) hfμ hgμ hfprod hgprod
    (by rw [integral_prod_mul, hcenter]; ring)
    (hfsq.trans (by simpa using
      (integral_fun_fst (μ := μX) (ν := μY) (fun x => f x ^ 2)).symm))
    (hgsq.trans (by simpa using
      (integral_fun_snd (μ := μX) (ν := μY) (fun y => g y ^ 2)).symm))
  simpa only [hfsq, hgsq] using hb

/-- The same continuous joint theorem from an actual density relative to the
product of its marginals. The a.e. floor is the sole correlation input, and
the lower measure domination is proved from it. -/
theorem joint_withDensity_minorization_covariance
    {X Y : Type*} [MeasurableSpace X] [MeasurableSpace Y]
    (μX : Measure X) (μY : Measure Y)
    [IsProbabilityMeasure μX] [IsProbabilityMeasure μY]
    (w : X × Y → ℝ≥0∞) [IsProbabilityMeasure ((μX.prod μY).withDensity w)]
    (hfst : Measure.map Prod.fst ((μX.prod μY).withDensity w) = μX)
    (hsnd : Measure.map Prod.snd ((μX.prod μY).withDensity w) = μY)
    (α : ℝ) (hα : 0 ≤ α)
    (hminor : ∀ᵐ z ∂μX.prod μY, ENNReal.ofReal α ≤ w z)
    (f : X → ℝ) (g : Y → ℝ) (hf : MemLp f 2 μX) (hg : MemLp g 2 μY)
    (hcenter : (∫ x, f x ∂μX) = 0) :
    (∫ z, f z.1 * g z.2 ∂((μX.prod μY).withDensity w)) ^ 2 ≤
      (1 - α) ^ 2 * (∫ x, f x ^ 2 ∂μX) * ∫ y, g y ^ 2 ∂μY := by
  apply joint_measure_minorization_covariance ((μX.prod μY).withDensity w)
    μX μY hfst hsnd α hα ?_ f g hf hg hcenter
  simpa only [withDensity_const] using withDensity_mono hminor

/-- Continuous covariance-to-variance bound for arbitrary L2 observables.
Centering is performed in the proof using the actual marginals. In particular,
no preselected observable family or finite approximation is involved. -/
theorem joint_withDensity_covariance_variance
    {X Y : Type*} [MeasurableSpace X] [MeasurableSpace Y]
    (μX : Measure X) (μY : Measure Y)
    [IsProbabilityMeasure μX] [IsProbabilityMeasure μY]
    (w : X × Y → ℝ≥0∞) [IsProbabilityMeasure ((μX.prod μY).withDensity w)]
    (hfst : Measure.map Prod.fst ((μX.prod μY).withDensity w) = μX)
    (hsnd : Measure.map Prod.snd ((μX.prod μY).withDensity w) = μY)
    (α : ℝ) (hα : 0 ≤ α)
    (hminor : ∀ᵐ z ∂μX.prod μY, ENNReal.ofReal α ≤ w z)
    (f : X → ℝ) (g : Y → ℝ) (hf : MemLp f 2 μX) (hg : MemLp g 2 μY) :
    ProbabilityTheory.covariance (fun z => f z.1) (fun z => g z.2)
        ((μX.prod μY).withDensity w) ^ 2 ≤
      (1 - α) ^ 2 * ProbabilityTheory.variance f μX * ProbabilityTheory.variance g μY := by
  let μ := (μX.prod μY).withDensity w
  have hmeanf : (∫ z, f z.1 ∂μ) = ∫ x, f x ∂μX := by
    rw [← hfst]
    exact (integral_map measurable_fst.aemeasurable
      (hfst ▸ hf.aestronglyMeasurable)).symm
  have hmeang : (∫ z, g z.2 ∂μ) = ∫ y, g y ∂μY := by
    rw [← hsnd]
    exact (integral_map measurable_snd.aemeasurable
      (hsnd ▸ hg.aestronglyMeasurable)).symm
  have hfcenter : (∫ x, (f x - ∫ y, f y ∂μX) ∂μX) = 0 := by
    rw [integral_sub (hf.integrable one_le_two) (integrable_const _)]
    simp
  have hb := joint_withDensity_minorization_covariance μX μY w hfst hsnd
    α hα hminor (fun x => f x - ∫ y, f y ∂μX) (fun y => g y - ∫ x, g x ∂μY)
    (hf.sub (memLp_const _)) (hg.sub (memLp_const _)) hfcenter
  change (∫ z, (f z.1 - ∫ t, f t.1 ∂μ) * (g z.2 - ∫ t, g t.2 ∂μ) ∂μ) ^ 2 ≤ _
  rw [hmeanf, hmeang, ProbabilityTheory.variance_eq_integral hf.aemeasurable,
    ProbabilityTheory.variance_eq_integral hg.aemeasurable]
  exact hb

end MeasureComparison

section Projections

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
local notation "⟪" x ", " y "⟫" => inner ℝ x y

/-- A self-adjoint idempotent, without a finite-dimensional or commutation assumption. -/
structure OrthogonalProjection where
  map : E →ₗ[ℝ] E
  symmetric : map.IsSymmetric
  idempotent : ∀ x, map (map x) = map x

/-- The energy of a projection is the squared norm of its projected vector. -/
theorem projection_energy (Q : OrthogonalProjection (E := E)) (x : E) :
    ⟪x, Q.map x⟫ = ‖Q.map x‖ ^ 2 := by
  rw [← real_inner_self_eq_norm_sq]
  simpa only [Q.idempotent] using (Q.symmetric x (Q.map x)).symm

/-- Orthogonal projection energies are nonnegative. -/
theorem projection_energy_nonneg (Q : OrthogonalProjection (E := E)) (x : E) :
    0 ≤ ⟪x, Q.map x⟫ := by rw [projection_energy]; positivity

variable {I : Type*} [Fintype I]

/-- The finite sum of true-vacuum complement projections. -/
noncomputable def assembly (Q : I → OrthogonalProjection (E := E)) : E →ₗ[ℝ] E :=
  ∑ i, (Q i).map

/-- No simultaneous diagonalization is needed for the exact assembly energy. -/
theorem assembly_energy (Q : I → OrthogonalProjection (E := E)) (x : E) :
    ⟪x, assembly Q x⟫ = ∑ i, ‖(Q i).map x‖ ^ 2 := by
  simp [assembly, LinearMap.sum_apply, inner_sum, projection_energy]

/-- Sums of orthogonal projections remain symmetric even when they do not commute. -/
theorem assembly_symmetric (Q : I → OrthogonalProjection (E := E)) :
    (assembly Q).IsSymmetric := by
  intro x y
  simp only [assembly, LinearMap.sum_apply, sum_inner, inner_sum]
  exact sum_congr rfl fun i _ => (Q i).symmetric x y

/-- The common kernel is exactly the kernel of the sum; positivity rules out cancellation. -/
theorem assembly_kernel_iff (Q : I → OrthogonalProjection (E := E)) (x : E) :
    assembly Q x = 0 ↔ ∀ i, (Q i).map x = 0 := by
  constructor
  · intro hx i
    have hsum : (∑ i, ‖(Q i).map x‖ ^ 2) = 0 := by rw [← assembly_energy, hx]; simp
    have hi := (Finset.sum_eq_zero_iff_of_nonneg
      (fun j (_ : j ∈ (Finset.univ : Finset I)) => sq_nonneg ‖(Q j).map x‖)).mp hsum i (mem_univ i)
    simpa using hi
  · intro hx
    simp [assembly, LinearMap.sum_apply, hx]

/-- Symmetric interaction weights collect into row sums, with both orderings retained. -/
theorem symmetric_coupling_sum (c : I → I → ℝ) (e : I → ℝ)
    (hsymm : ∀ i j, c i j = c j i) :
    (∑ i, ∑ j, c i j * (e i + e j)) =
      2 * ∑ i, (∑ j, c i j) * e i := by
  simp only [mul_add, sum_add_distrib]
  have hfirst : (∑ i, ∑ j, c i j * e i) = ∑ i, (∑ j, c i j) * e i := by
    simp only [sum_mul]
  have hsecond : (∑ i, ∑ j, c i j * e j) = ∑ i, (∑ j, c i j) * e i := by
    rw [sum_comm]
    simp_rw [hsymm, sum_mul]
  rw [hfirst, hsecond]
  ring

/-- The noncommuting projection row-budget calculation in VA12.
Only pairwise anticommutator estimates are assumed. The global square-form
estimate is derived by summing them; no common eigenbasis is assumed. -/
theorem assembly_square_lower (Q : I → OrthogonalProjection (E := E))
    (c : I → I → ℝ) (κ : ℝ)
    (hsymm : ∀ i j, c i j = c j i) (hdiag : ∀ i, c i i = 0)
    (hrow : ∀ i, (∑ j, c i j) ≤ κ)
    (hpair : ∀ i j, i ≠ j → ∀ x,
      -(c i j * (‖(Q i).map x‖ ^ 2 + ‖(Q j).map x‖ ^ 2)) ≤
        2 * ⟪(Q i).map x, (Q j).map x⟫)
    (x : E) :
    (1 - κ) * ⟪x, assembly Q x⟫ ≤ ‖assembly Q x‖ ^ 2 := by
  classical
  let e : I → ℝ := fun i => ‖(Q i).map x‖ ^ 2
  have hp : ∀ i j,
      (if i = j then 2 * e i else 0) - c i j * (e i + e j) ≤
        2 * ⟪(Q i).map x, (Q j).map x⟫ := by
    intro i j
    by_cases hij : i = j
    · subst j
      simp [e, hdiag]
    · simpa [hij, e] using hpair i j hij x
  have hpall := sum_le_sum (s := univ) fun i _ =>
    sum_le_sum (s := univ) fun j _ => hp i j
  have hexpand : (∑ i, ∑ j, 2 * ⟪(Q i).map x, (Q j).map x⟫) =
      2 * ‖assembly Q x‖ ^ 2 := by
    simp only [assembly, LinearMap.sum_apply, ← real_inner_self_eq_norm_sq,
      sum_inner, inner_sum, mul_sum]
    exact sum_comm
  have hleft : (∑ i, ∑ j, ((if i = j then 2 * e i else 0) -
      c i j * (e i + e j))) =
        2 * (∑ i, e i) - 2 * ∑ i, (∑ j, c i j) * e i := by
    simp only [sum_sub_distrib]
    rw [symmetric_coupling_sum c e hsymm]
    simp [mul_sum]
  rw [hleft, hexpand] at hpall
  have hrows : (∑ i, (∑ j, c i j) * e i) ≤ κ * ∑ i, e i := by
    rw [mul_sum]
    apply sum_le_sum
    intro i _
    exact mul_le_mul_of_nonneg_right (hrow i) (sq_nonneg _)
  rw [assembly_energy]
  change (1 - κ) * (∑ i, e i) ≤ _
  nlinarith

/-- A symmetric nonnegative operator satisfying T² ≥ delta T has a gap on its
kernel complement in every finite dimension. The eigenspace argument proves
the missing spectral implication, including exclusion of (0, delta).
No gap, inverse, or lower bound on nonzero eigenvalues is assumed. -/
theorem finite_spectral_gap_of_square [FiniteDimensional ℝ E]
    (T : E →ₗ[ℝ] E) (hT : T.IsSymmetric) (δ : ℝ)
    (hpos : ∀ x, 0 ≤ ⟪x, T x⟫)
    (hsquare : ∀ x, δ * ⟪x, T x⟫ ≤ ‖T x‖ ^ 2)
    (x : E) (horth : x ∈ (LinearMap.ker T)ᗮ) :
    δ * ‖x‖ ^ 2 ≤ ⟪x, T x⟫ := by
  let b := hT.eigenvectorBasis (n := Module.finrank ℝ E) rfl
  let ev := hT.eigenvalues (n := Module.finrank ℝ E) rfl
  have heigen : ∀ i, T (b i) = ev i • b i := hT.apply_eigenvectorBasis rfl
  have hunit : ∀ i, ‖b i‖ = 1 := b.orthonormal.norm_eq_one
  have hEigen : ∀ i, ev i = 0 ∨ δ ≤ ev i := by
    intro i
    have hp := hpos (b i)
    have hs := hsquare (b i)
    rw [heigen i] at hp hs
    simp only [real_inner_smul_right, real_inner_self_eq_norm_sq,
      hunit i, one_pow, mul_one] at hp hs
    simp only [norm_smul, Real.norm_eq_abs, hunit i, mul_one, sq_abs] at hs
    by_cases hz : ev i = 0
    · exact Or.inl hz
    · right
      have hl : 0 < ev i := lt_of_le_of_ne hp (Ne.symm hz)
      nlinarith
  have hterm : ∀ i, δ * ⟪b i, x⟫ ^ 2 ≤ ev i * ⟪b i, x⟫ ^ 2 := by
    intro i
    rcases hEigen i with hz | hδ
    · have hk : b i ∈ LinearMap.ker T := by simp [LinearMap.mem_ker, heigen, hz]
      have hc : ⟪b i, x⟫ = 0 := horth (b i) hk
      simp [hc]
    · exact mul_le_mul_of_nonneg_right hδ (sq_nonneg _)
  calc
    δ * ‖x‖ ^ 2 = ∑ i, δ * ⟪b i, x⟫ ^ 2 := by rw [← b.sum_sq_inner_right, mul_sum]
    _ ≤ ∑ i, ev i * ⟪b i, x⟫ ^ 2 := sum_le_sum fun i _ => hterm i
    _ = ⟪x, T x⟫ := by
      rw [← b.sum_inner_mul_inner x (T x)]
      apply sum_congr rfl
      intro i _
      rw [← hT (b i) x, heigen i, real_inner_smul_left, real_inner_comm x (b i)]
      ring

/-- Finite-dimensional physical projection gap from the local angle row budget. -/
theorem finite_assembly_gap [FiniteDimensional ℝ E]
    (Q : I → OrthogonalProjection (E := E)) (c : I → I → ℝ) (κ : ℝ)
    (hsymm : ∀ i j, c i j = c j i) (hdiag : ∀ i, c i i = 0)
    (hrow : ∀ i, (∑ j, c i j) ≤ κ)
    (hpair : ∀ i j, i ≠ j → ∀ x,
      -(c i j * (‖(Q i).map x‖ ^ 2 + ‖(Q j).map x‖ ^ 2)) ≤
        2 * ⟪(Q i).map x, (Q j).map x⟫)
    (x : E) (horth : x ∈ (LinearMap.ker (assembly Q))ᗮ) :
    (1 - κ) * ‖x‖ ^ 2 ≤ ∑ i, ‖(Q i).map x‖ ^ 2 := by
  rw [← assembly_energy]
  apply finite_spectral_gap_of_square (assembly Q) (assembly_symmetric Q) (1 - κ)
    (fun y => by rw [assembly_energy]; exact sum_nonneg fun i _ => sq_nonneg _)
    (assembly_square_lower Q c κ hsymm hdiag hrow hpair) x horth

/-- Local Dirichlet floors plus approximate tensorization give a physical form floor.
The Hilbert space may already be the gauge-invariant subspace. The conclusion is
the full vector inequality, not merely arithmetic on prospective eigenvalues. -/
theorem local_floor_tensorization (Q : I → OrthogonalProjection (E := E))
    (energy : I → E → ℝ) (γ C : ℝ) (hγ : 0 ≤ γ) (hC : 0 < C)
    (hlocal : ∀ i x, γ * ‖(Q i).map x‖ ^ 2 ≤ energy i x)
    (x : E) (htensor : ‖x‖ ^ 2 ≤ C * ∑ i, ‖(Q i).map x‖ ^ 2) :
    (γ / C) * ‖x‖ ^ 2 ≤ ∑ i, energy i x := by
  have hsum : γ * (∑ i, ‖(Q i).map x‖ ^ 2) ≤ ∑ i, energy i x := by
    rw [mul_sum]
    exact sum_le_sum fun i _ => hlocal i x
  have hscaled := mul_le_mul_of_nonneg_left htensor hγ
  apply (mul_le_mul_iff_right₀ hC).mp
  calc
    C * ((γ / C) * ‖x‖ ^ 2) = γ * ‖x‖ ^ 2 := by field_simp
    _ ≤ γ * (C * ∑ i, ‖(Q i).map x‖ ^ 2) := hscaled
    _ ≤ C * (∑ i, energy i x) := by nlinarith

/-- The VA9/VA14 physical transfer on an explicit form domain.
An isometric ground-state multiplication, its exact form identity, local
conditional floors, and approximate tensorization together imply the physical
gap form inequality. No dimensional restriction is made and no excited
eigenvector is assumed to exist. Constructing these inputs for the actual
Wilson measure is separate from this implication. -/
theorem unitary_ground_state_gap
    {F : Type*} [NormedAddCommGroup F] [InnerProductSpace ℝ F]
    (U : E ≃ₗᵢ[ℝ] F) (domain : Submodule ℝ E) (vacuum : E)
    (Q : I → OrthogonalProjection (E := E)) (energy : I → E → ℝ)
    (qH : F → ℝ) (E0 γ C : ℝ) (hγ : 0 ≤ γ) (hC : 0 < C)
    (hform : ∀ f ∈ domain, qH (U f) - E0 * ‖U f‖ ^ 2 = ∑ i, energy i f)
    (hlocal : ∀ i f, f ∈ domain → γ * ‖(Q i).map f‖ ^ 2 ≤ energy i f)
    (htensor : ∀ f, f ∈ domain → ⟪vacuum, f⟫ = 0 →
      ‖f‖ ^ 2 ≤ C * ∑ i, ‖(Q i).map f‖ ^ 2)
    (ψ : F) (hψ : U.symm ψ ∈ domain) (horth : inner ℝ (U vacuum) ψ = 0) :
    (γ / C) * ‖ψ‖ ^ 2 ≤ qH ψ - E0 * ‖ψ‖ ^ 2 := by
  let f := U.symm ψ
  have horthf : ⟪vacuum, f⟫ = 0 := by
    simpa only [f, U.inner_map_eq_flip] using horth
  have hsum : γ * (∑ i, ‖(Q i).map f‖ ^ 2) ≤ ∑ i, energy i f := by
    rw [mul_sum]
    exact sum_le_sum fun i _ => hlocal i f hψ
  have hscaled := mul_le_mul_of_nonneg_left (htensor f hψ horthf) hγ
  have hbound : (γ / C) * ‖f‖ ^ 2 ≤ ∑ i, energy i f := by
    apply (mul_le_mul_iff_right₀ hC).mp
    calc
      C * ((γ / C) * ‖f‖ ^ 2) = γ * ‖f‖ ^ 2 := by field_simp
      _ ≤ γ * (C * ∑ i, ‖(Q i).map f‖ ^ 2) := hscaled
      _ ≤ C * (∑ i, energy i f) := by nlinarith
  have hid := hform f hψ
  rw [← hid] at hbound
  simpa only [f, U.apply_symm_apply, U.symm.norm_map] using hbound

end Projections

section BoundedSpectralBridge

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
local notation "⟪" x ", " y "⟫" => inner ℂ x y

/-- GST-3a to GST-3b, bounded realization; also the VA12 spectral step.
A positive bounded operator satisfying T² ≥ delta T has the corresponding
energy floor on its range. The positive square root is constructed by the
continuous functional calculus; it is not an additional hypothesis. -/
theorem bounded_gap_on_range_of_square (T : H →L[ℂ] H) (hT : T.IsPositive)
    (δ : ℝ) (hsquare : ∀ x, δ * (⟪x, T x⟫).re ≤ ‖T x‖ ^ 2)
    (x : H) : δ * ‖T x‖ ^ 2 ≤ (⟪T x, T (T x)⟫).re := by
  let B : H →L[ℂ] H := CFC.sqrt T
  have hB : B.IsPositive := ContinuousLinearMap.nonneg_iff_isPositive.mp (CFC.sqrt_nonneg T)
  have hBB : ∀ y, B (B y) = T y := by
    intro y
    have hid : B * B = T := CFC.sqrt_mul_sqrt_self T
      (ContinuousLinearMap.nonneg_iff_isPositive.mpr hT)
    exact congrArg (fun A : H →L[ℂ] H => A y) hid
  have hcomm : ∀ y, T (B y) = B (T y) := by
    intro y
    rw [← hBB (B y), hBB y]
  have hinner : (⟪B x, T (B x)⟫).re = ‖T x‖ ^ 2 := by
    have hs : ⟪B (B x), T x⟫ = ⟪B x, B (T x)⟫ := hB.isSymmetric (B x) (T x)
    rw [hcomm x, ← hs, hBB x]
    exact (norm_sq_eq_re_inner (𝕜 := ℂ) (T x)).symm
  have hnorm : ‖T (B x)‖ ^ 2 = (⟪T x, T (T x)⟫).re := by
    have hs : ⟪B (T x), B (T x)⟫ = ⟪T x, B (B (T x))⟫ :=
      hB.isSymmetric (T x) (B (T x))
    rw [hcomm x, norm_sq_eq_re_inner (𝕜 := ℂ), hs, hBB]
    rfl
  simpa only [hinner, hnorm] using hsquare (B x)

/-- GST-3a to GST-3b, bounded realization, and the VA12 spectral bridge.
For a positive bounded operator T, T² ≥ delta T implies the gap form inequality
on the complete kernel complement. The proof extends the range estimate by
continuity using closure(range T) = (ker T)^perp. No discreteness, compactness,
inverse, pre-existing gap, or spectral measure representation is assumed. -/
theorem bounded_spectral_gap_of_square (T : H →L[ℂ] H) (hT : T.IsPositive)
    (δ : ℝ) (hsquare : ∀ x, δ * (⟪x, T x⟫).re ≤ ‖T x‖ ^ 2)
    (x : H) (horth : x ∈ T.kerᗮ) :
    δ * ‖x‖ ^ 2 ≤ (⟪x, T x⟫).re := by
  have hstar : T.adjoint = T := hT.isSelfAdjoint
  have hclosure : T.kerᗮ = T.range.topologicalClosure := by
    rw [T.orthogonal_ker, hstar]
  have hclosed : IsClosed {y : H | δ * ‖y‖ ^ 2 ≤ (⟪y, T y⟫).re} :=
    isClosed_le (by fun_prop) (by fun_prop)
  have hrange : (T.range : Set H) ⊆ {y : H | δ * ‖y‖ ^ 2 ≤ (⟪y, T y⟫).re} := by
    rintro y ⟨z, rfl⟩
    exact bounded_gap_on_range_of_square T hT δ hsquare z
  have hmem : x ∈ closure (T.range : Set H) := by
    rw [hclosure] at horth
    exact horth
  exact closure_minimal hrange hclosed hmem

noncomputable local instance : InnerProductSpace ℝ H := InnerProductSpace.rclikeToReal ℂ H

/-- A complex orthogonal projection is also an orthogonal projection on the
underlying real Hilbert space, with exactly the same norm and action. -/
noncomputable def complexProjectionAsReal (Q : H →L[ℂ] H)
    (hsymm : Q.IsSymmetric) (hidem : ∀ x, Q (Q x) = Q x) :
    OrthogonalProjection (E := H) where
  map := Q.toLinearMap.restrictScalars ℝ
  symmetric := by
    intro x y
    change inner ℝ (Q x) y = inner ℝ x (Q y)
    simp only [real_inner_eq_re_inner (𝕜 := ℂ)]
    exact congrArg Complex.re (hsymm x y)
  idempotent := hidem

/-- VA12 on an arbitrary complex Hilbert space: the finite family of actual
bounded projections is assembled without any dimension restriction. Its local
anticommutator estimates and strict row budget yield the full kernel-complement
gap, through the proved continuous-functional-calculus spectral bridge. -/
theorem bounded_projection_assembly_gap {I : Type*} [Fintype I]
    (Q : I → H →L[ℂ] H) (hsymmQ : ∀ i, (Q i).IsSymmetric)
    (hidem : ∀ i x, Q i (Q i x) = Q i x)
    (c : I → I → ℝ) (κ : ℝ)
    (hsymm : ∀ i j, c i j = c j i) (hdiag : ∀ i, c i i = 0)
    (hrow : ∀ i, (∑ j, c i j) ≤ κ)
    (hpair : ∀ i j, i ≠ j → ∀ x,
      -(c i j * (‖Q i x‖ ^ 2 + ‖Q j x‖ ^ 2)) ≤ 2 * (⟪Q i x, Q j x⟫).re)
    (x : H) (horth : x ∈ (∑ i, Q i).kerᗮ) :
    (1 - κ) * ‖x‖ ^ 2 ≤ ∑ i, ‖Q i x‖ ^ 2 := by
  let QR : I → OrthogonalProjection (E := H) :=
    fun i => complexProjectionAsReal (Q i) (hsymmQ i) (hidem i)
  let G : H →L[ℂ] H := ∑ i, Q i
  have hG : ∀ y, assembly QR y = G y := by
    intro y
    simp [assembly, QR, complexProjectionAsReal, G, LinearMap.sum_apply]
  have hQpos : ∀ i, (Q i).IsPositive := by
    intro i
    refine ⟨hsymmQ i, ?_⟩
    intro y
    change 0 ≤ (⟪Q i y, y⟫).re
    have h := projection_energy_nonneg (QR i) y
    change 0 ≤ inner ℝ y (Q i y) at h
    rw [real_inner_comm] at h
    simpa only [real_inner_eq_re_inner (𝕜 := ℂ), RCLike.re_to_complex] using h
  have hGpos : G.IsPositive := by
    exact ContinuousLinearMap.isPositive_sum univ (fun i _ => hQpos i)
  have hsquare : ∀ y, (1 - κ) * (⟪y, G y⟫).re ≤ ‖G y‖ ^ 2 := by
    intro y
    have h := assembly_square_lower QR c κ hsymm hdiag hrow
      (fun i j hij z => by simpa only [QR, complexProjectionAsReal,
        LinearMap.restrictScalars_apply, ContinuousLinearMap.coe_coe,
        real_inner_eq_re_inner (𝕜 := ℂ), RCLike.re_to_complex] using hpair i j hij z) y
    rw [hG y] at h
    simpa only [real_inner_eq_re_inner (𝕜 := ℂ), RCLike.re_to_complex] using h
  have hbound := bounded_spectral_gap_of_square G hGpos (1 - κ) hsquare x horth
  have henergy := assembly_energy QR x
  rw [hG x] at henergy
  change inner ℝ x (G x) = ∑ i, ‖Q i x‖ ^ 2 at henergy
  simp only [real_inner_eq_re_inner (𝕜 := ℂ), RCLike.re_to_complex] at henergy
  rw [henergy] at hbound
  exact hbound

end BoundedSpectralBridge

section Gram

variable {I J : Type*} [Fintype I] [Fintype J]

/-- GA20: every finite Gram form is exactly a sum of squares, regardless of
the origin of its typed amplitudes. This theorem does not identify the amplitudes
as correlation functions of a field theory. -/
theorem gram_quadratic_eq_squares (V : I → J → ℝ) (a : I → ℝ) :
    (∑ i, ∑ j, (∑ k, V i k * V j k) * a i * a j) =
      ∑ k, (∑ i, a i * V i k) ^ 2 := by
  simp only [sum_mul, pow_two, mul_sum]
  rw [sum_comm]
  conv_lhs => arg 2; ext j; rw [sum_comm]
  rw [sum_comm]
  apply sum_congr rfl
  intro k _
  apply sum_congr rfl
  intro i _
  apply sum_congr rfl
  intro j _
  ring

/-- GA20 positivity is a structural Gram identity, not an OS construction. -/
theorem gram_form_nonnegative (V : I → J → ℝ) (a : I → ℝ) :
    0 ≤ ∑ i, ∑ j, (∑ k, V i k * V j k) * a i * a j := by
  rw [gram_quadratic_eq_squares]
  exact sum_nonneg fun k _ => sq_nonneg _

end Gram

end Workhouse.GroundStateAssembly
