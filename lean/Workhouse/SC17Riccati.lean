import Mathlib.Analysis.Normed.Operator.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.MetricSpace.Contracting
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic

/-!
# Conditional SC17 Riccati comparison

Source: `docs/derivations/wilson-sc17-spatial-closure.md`, Part III, R4--R9.
The small-root comparison is an actual continuity argument. The Banach-algebra
result constructs a quadratic fixed point for a bounded linear inverse; its
norm budget is an explicit input. Neither theorem constructs the Wilson
weighted-Schur algebra, actual Markov evolution, quantum-pressure defect or
physical ground-state identification. The final parameter lemmas certify the
entire interval for the explicitly proposed numerical defaults, conditionally
on those defaults bounding the actual objects.
-/

namespace Workhouse.SC17Riccati

open scoped NNReal

/-- The source uses `c = delta / (2 * epsilon)`. -/
noncomputable def smallRoot (beta c : ℝ) : ℝ :=
  (1 - Real.sqrt (1 - 4 * beta ^ 2 * c)) / (2 * beta)

theorem smallRoot_nonneg (beta c : ℝ) (hb : 0 < beta) (hc : 0 ≤ c)
    (hp : 4 * beta ^ 2 * c < 1) : 0 ≤ smallRoot beta c := by
  have hs := Real.sq_sqrt (by linarith : 0 ≤ 1 - 4 * beta ^ 2 * c)
  have hn := Real.sqrt_nonneg (1 - 4 * beta ^ 2 * c)
  have hu : Real.sqrt (1 - 4 * beta ^ 2 * c) ≤ 1 := by
    nlinarith [sq_nonneg beta, mul_nonneg (sq_nonneg beta) hc]
  exact div_nonneg (by linarith) (by positivity)

theorem smallRoot_equation (beta c : ℝ) (hb : 0 < beta)
    (hp : 4 * beta ^ 2 * c < 1) :
    beta * smallRoot beta c ^ 2 + beta * c = smallRoot beta c := by
  have hs := Real.sq_sqrt (by linarith : 0 ≤ 1 - 4 * beta ^ 2 * c)
  unfold smallRoot
  generalize Real.sqrt (1 - 4 * beta ^ 2 * c) = s at *
  field_simp
  nlinarith

theorem smallRoot_lt_half_inverse (beta c : ℝ) (hb : 0 < beta)
    (hp : 4 * beta ^ 2 * c < 1) : smallRoot beta c < 1 / (2 * beta) := by
  have hs : 0 < Real.sqrt (1 - 4 * beta ^ 2 * c) := Real.sqrt_pos.2 (by linarith)
  unfold smallRoot
  exact (div_lt_div_iff_of_pos_right (by positivity : 0 < 2 * beta)).2 (by linarith)

theorem smallRoot_contraction_margin (beta c : ℝ) (hb : 0 < beta)
    (hp : 4 * beta ^ 2 * c < 1) : 2 * beta * smallRoot beta c < 1 := by
  have h := smallRoot_lt_half_inverse beta c hb hp
  have h' := (lt_div_iff₀ (by positivity : 0 < 2 * beta)).1 h
  nlinarith

/-- R9's reference floor follows from the actual budget inequality, not a
postulated positivity of the final curvature. -/
theorem smallRoot_lt_reference_floor (beta c a : ℝ) (hb : 0 < beta)
    (hp : 4 * beta ^ 2 * c < 1) (ha : 1 / (2 * beta) ≤ a) :
    smallRoot beta c < a :=
  (smallRoot_lt_half_inverse beta c hb hp).trans_le ha

theorem quadratic_forbidden_interval (beta c y : ℝ) (hb : 0 < beta)
    (hp : 4 * beta ^ 2 * c < 1)
    (hlo : smallRoot beta c < y) (hhi : y < 1 / (2 * beta)) :
    beta * y ^ 2 + beta * c < y := by
  have hr := smallRoot_equation beta c hb hp
  have hm := smallRoot_contraction_margin beta c hb hp
  have hy := (lt_div_iff₀ (by positivity : 0 < 2 * beta)).1 hhi
  have hprod : (y - smallRoot beta c) *
      (beta * (y + smallRoot beta c) - 1) < 0 := by
    apply mul_neg_of_pos_of_neg (by linarith)
    nlinarith
  nlinarith

/-- R8 -> R7: a continuous path starting from zero cannot jump to the large
root branch. No differentiability or monotonicity of the path is assumed. -/
theorem continuous_riccati_barrier (beta c T : ℝ) (hb : 0 < beta) (hc : 0 ≤ c)
    (hp : 4 * beta ^ 2 * c < 1) (hT : 0 ≤ T) (M : ℝ → ℝ)
    (hcont : ContinuousOn M (Set.Icc 0 T)) (hzero : M 0 = 0)
    (hineq : ∀ t ∈ Set.Icc 0 T, M t ≤ beta * M t ^ 2 + beta * c) :
    M T ≤ smallRoot beta c := by
  by_contra h
  have hMT : smallRoot beta c < M T := lt_of_not_ge h
  have hr := smallRoot_nonneg beta c hb hc hp
  have hhalf := smallRoot_lt_half_inverse beta c hb hp
  let y := (smallRoot beta c + min (M T) (1 / (2 * beta))) / 2
  have hlo : smallRoot beta c < y := by
    dsimp [y]
    have := lt_min hMT hhalf
    linarith
  have hhi : y < 1 / (2 * beta) := by
    dsimp [y]
    linarith [min_le_right (M T) (1 / (2 * beta))]
  have hy : y ∈ Set.Icc (M 0) (M T) := by
    rw [hzero]
    constructor
    · linarith
    · dsimp [y]
      linarith [min_le_left (M T) (1 / (2 * beta))]
  obtain ⟨t, ht, heq⟩ := intermediate_value_Icc hT hcont hy
  have hm := hineq t ht
  rw [heq] at hm
  exact (not_lt_of_ge hm) (quadratic_forbidden_interval beta c y hb hp hlo hhi)

section BanachAlgebra

variable {A : Type*} [NormedRing A] [NormedAlgebra ℝ A]

/-- The quadratic fixed-point map for a specified bounded linear inverse. -/
noncomputable def riccatiMap (S : A →L[ℝ] A) (D X : A) : A := S (X * X - D)

theorem riccatiMap_norm_le (S : A →L[ℝ] A) (D X : A) (beta c r : ℝ)
    (hb : 0 ≤ beta) (hr : 0 ≤ r) (hS : ‖S‖ ≤ beta)
    (hD : ‖D‖ ≤ c) (hX : ‖X‖ ≤ r) :
    ‖riccatiMap S D X‖ ≤ beta * (r ^ 2 + c) := by
  have hsquare : ‖X * X‖ ≤ r ^ 2 := by
    have := norm_mul_le X X
    nlinarith [norm_nonneg X]
  calc
    ‖riccatiMap S D X‖ ≤ ‖S‖ * ‖X * X - D‖ := S.le_opNorm _
    _ ≤ beta * ‖X * X - D‖ :=
      mul_le_mul_of_nonneg_right hS (norm_nonneg _)
    _ ≤ beta * (r ^ 2 + c) := by
      apply mul_le_mul_of_nonneg_left _ hb
      linarith [norm_sub_le (X * X) D]

/-- This estimate uses noncommutative multiplication, so it applies to
continuous endomorphisms and weighted matrix Banach algebras. -/
theorem riccatiMap_lipschitz_on_ball (S : A →L[ℝ] A) (D X Y : A)
    (beta r : ℝ) (hb : 0 ≤ beta) (hS : ‖S‖ ≤ beta)
    (hX : ‖X‖ ≤ r) (hY : ‖Y‖ ≤ r) :
    ‖riccatiMap S D X - riccatiMap S D Y‖ ≤ (2 * beta * r) * ‖X - Y‖ := by
  have hid : X * X - Y * Y = (X - Y) * X + Y * (X - Y) := by noncomm_ring
  have hnorm : ‖X * X - Y * Y‖ ≤ (2 * r) * ‖X - Y‖ := by
    rw [hid]
    have h1 := norm_mul_le (X - Y) X
    have h2 := norm_mul_le Y (X - Y)
    have h3 := norm_add_le ((X - Y) * X) (Y * (X - Y))
    have h4 := mul_le_mul_of_nonneg_left hX (norm_nonneg (X - Y))
    have h5 := mul_le_mul_of_nonneg_right hY (norm_nonneg (X - Y))
    nlinarith
  have heq : riccatiMap S D X - riccatiMap S D Y = S (X * X - Y * Y) := by
    simp only [riccatiMap, ← map_sub]
    congr 1
    abel
  rw [heq]
  calc
    ‖S (X * X - Y * Y)‖ ≤ ‖S‖ * ‖X * X - Y * Y‖ := S.le_opNorm _
    _ ≤ beta * ‖X * X - Y * Y‖ :=
      mul_le_mul_of_nonneg_right hS (norm_nonneg _)
    _ ≤ beta * ((2 * r) * ‖X - Y‖) := mul_le_mul_of_nonneg_left hnorm hb
    _ = _ := by ring

/-- A genuine Banach fixed-point construction, including uniqueness within
the invariant small-root ball. The inverse map and its norm budget are inputs. -/
theorem exists_riccati_fixedPoint [CompleteSpace A] (S : A →L[ℝ] A) (D : A)
    (beta c : ℝ) (hb : 0 < beta) (hc : 0 ≤ c)
    (hp : 4 * beta ^ 2 * c < 1) (hS : ‖S‖ ≤ beta) (hD : ‖D‖ ≤ c) :
    ∃ X : A, ‖X‖ ≤ smallRoot beta c ∧ riccatiMap S D X = X ∧
      ∀ Y : A, ‖Y‖ ≤ smallRoot beta c → riccatiMap S D Y = Y → Y = X := by
  let r := smallRoot beta c
  have hr : 0 ≤ r := smallRoot_nonneg beta c hb hc hp
  have hmap : Set.MapsTo (riccatiMap S D) (Metric.closedBall (0 : A) r)
      (Metric.closedBall (0 : A) r) := by
    intro X hX
    have hn : ‖X‖ ≤ r := by simpa using hX
    have h := riccatiMap_norm_le S D X beta c r (le_of_lt hb) hr hS hD hn
    have heq := smallRoot_equation beta c hb hp
    have hbound : ‖riccatiMap S D X‖ ≤ r := by dsimp [r] at *; nlinarith
    simpa using hbound
  let k : ℝ≥0 := ⟨2 * beta * r, by positivity⟩
  have hcontract : ContractingWith k (hmap.restrict (riccatiMap S D) _ _) := by
    constructor
    · exact smallRoot_contraction_margin beta c hb hp
    · apply LipschitzWith.of_dist_le_mul
      intro X Y
      change dist (riccatiMap S D X) (riccatiMap S D Y) ≤ (2 * beta * r) * dist (X : A) Y
      simp only [dist_eq_norm]
      exact riccatiMap_lipschitz_on_ball S D X Y beta r (le_of_lt hb) hS
        (by simpa only [Metric.mem_closedBall, dist_zero_right] using X.property)
        (by simpa only [Metric.mem_closedBall, dist_zero_right] using Y.property)
  obtain ⟨X, hX, hfix, _, _⟩ := ContractingWith.exists_fixedPoint'
    Metric.isClosed_closedBall.isComplete hmap hcontract
    (show (0 : A) ∈ Metric.closedBall (0 : A) r by simpa using hr) (edist_ne_top _ _)
  refine ⟨X, by simpa using hX, hfix, ?_⟩
  intro Y hY hYfix
  have hdiff := riccatiMap_lipschitz_on_ball S D Y X beta r (le_of_lt hb) hS hY
    (by simpa using hX)
  rw [hYfix, hfix] at hdiff
  have hk := smallRoot_contraction_margin beta c hb hp
  have : ‖Y - X‖ = 0 := by dsimp [r] at *; nlinarith [norm_nonneg (Y - X)]
  exact sub_eq_zero.mp (norm_eq_zero.mp this)

/-- A specified genuine linear inverse turns the constructed fixed point into
a solution of the algebraic Riccati equation. The inverse identity is separate
from the small-defect conclusion, and is not assumed for the Wilson operator. -/
theorem exists_riccati_solution [CompleteSpace A] (L S : A →L[ℝ] A) (D : A)
    (beta c : ℝ) (hb : 0 < beta) (hc : 0 ≤ c)
    (hp : 4 * beta ^ 2 * c < 1) (hS : ‖S‖ ≤ beta) (hD : ‖D‖ ≤ c)
    (hLS : Function.LeftInverse L S) :
    ∃ X : A, ‖X‖ ≤ smallRoot beta c ∧ L X = X * X - D := by
  obtain ⟨X, hX, hfix, _⟩ := exists_riccati_fixedPoint S D beta c hb hc hp hS hD
  refine ⟨X, hX, ?_⟩
  calc
    L X = L (S (X * X - D)) := congrArg L hfix.symm
    _ = X * X - D := hLS _

/-- For the source's scalar precision `a I`, the Sylvester inverse is actually
constructed as `(2a)^{-1}` times the identity continuous linear map. -/
theorem exists_scalar_reference_riccati [CompleteSpace A] (a c : ℝ) (D : A)
    (ha : 0 < a) (hc : 0 ≤ c) (hD : ‖D‖ ≤ c)
    (hp : 4 * (1 / (2 * a)) ^ 2 * c < 1) :
    ∃ X : A, ‖X‖ ≤ smallRoot (1 / (2 * a)) c ∧ (2 * a) • X = X * X - D := by
  let beta : ℝ := 1 / (2 * a)
  have hb : 0 < beta := by dsimp [beta]; positivity
  let S : A →L[ℝ] A := beta • ContinuousLinearMap.id ℝ A
  have hS : ‖S‖ ≤ beta := by
    dsimp [S]
    rw [norm_smul, Real.norm_eq_abs, abs_of_pos hb]
    nlinarith [ContinuousLinearMap.norm_id_le (𝕜 := ℝ) (E := A)]
  obtain ⟨X, hX, hfix, _⟩ := exists_riccati_fixedPoint S D beta c hb hc hp hS hD
  refine ⟨X, hX, ?_⟩
  have heq := congrArg (fun Y : A => (2 * a) • Y) hfix
  have hcancel : (2 * a) * beta = 1 := by dsimp [beta]; field_simp
  simpa only [riccatiMap, S, smul_apply,
    ContinuousLinearMap.id_apply, smul_smul, hcancel, one_smul] using heq.symm

end BanachAlgebra

/-- The full default budget from `sc17_quantum_defect_check.py`:
`L = 3`, `C_s = 6/5`, and reference velocity one. -/
noncomputable def defaultBeta : ℝ := (108 / 25) * Real.sqrt 33

noncomputable def defaultDefect (lambda : ℝ) : ℝ :=
  lambda * Real.sqrt lambda / 48

noncomputable def defaultParameter (lambda : ℝ) : ℝ :=
  (32076 / 625) * lambda * Real.sqrt lambda

noncomputable def defaultReferenceFloor : ℝ := 1 / (3 * Real.sqrt 33)

theorem defaultBeta_pos : 0 < defaultBeta := by unfold defaultBeta; positivity

theorem defaultBeta_sq : defaultBeta ^ 2 = (384912 / 625 : ℝ) := by
  have hs := Real.sq_sqrt (show (0 : ℝ) ≤ 33 by norm_num)
  unfold defaultBeta
  nlinarith

/-- Exact cancellation of epsilon in the proposed default Riccati parameter. -/
theorem default_parameter_identity (lambda : ℝ) :
    4 * defaultBeta ^ 2 * defaultDefect lambda = defaultParameter lambda := by
  rw [defaultBeta_sq]
  unfold defaultDefect defaultParameter
  ring

/-- The proposed comparison parameter is monotone throughout the nonnegative
coupling half-line, independently of the selected endpoint. -/
theorem default_parameter_monotone : MonotoneOn defaultParameter (Set.Ici 0) := by
  intro x _ y hy hxy
  have hprod : x * Real.sqrt x ≤ y * Real.sqrt y :=
    mul_le_mul hxy (Real.sqrt_le_sqrt hxy) (Real.sqrt_nonneg x) hy
  unfold defaultParameter
  nlinarith

/-- The diagnostic endpoint has this exact radical value. -/
theorem default_parameter_endpoint :
    defaultParameter (3 / 100) = 96228 * Real.sqrt 3 / 625000 := by
  have hs : Real.sqrt (100 : ℝ) = 10 := by norm_num
  unfold defaultParameter
  rw [Real.sqrt_div (by norm_num : (0 : ℝ) ≤ 3) 100, hs]
  ring

/-- The reference-floor comparison has a strict, exactly evaluated margin. -/
theorem default_reference_product :
    2 * defaultBeta * defaultReferenceFloor = (72 / 25 : ℝ) := by
  have hs : Real.sqrt (33 : ℝ) ≠ 0 := ne_of_gt (Real.sqrt_pos.2 (by norm_num))
  unfold defaultBeta defaultReferenceFloor
  field_simp
  ring

/-- The comparison covers every real coupling in the full closed interval,
not just the finite diagnostic sample in the companion script. -/
theorem default_parameter_interval (lambda : ℝ) (hzero : 0 ≤ lambda)
    (hupper : lambda ≤ 3 / 100) :
    0 ≤ defaultParameter lambda ∧
      defaultParameter lambda ≤ defaultParameter (3 / 100) ∧
      defaultParameter (3 / 100) < 27 / 100 := by
  have hs := Real.sqrt_le_sqrt hupper
  have hp : lambda * Real.sqrt lambda ≤ (3 / 100) * Real.sqrt (3 / 100) :=
    mul_le_mul hupper hs (Real.sqrt_nonneg lambda) (by norm_num)
  have hsq := Real.sq_sqrt (show (0 : ℝ) ≤ 3 / 100 by norm_num)
  have hn := Real.sqrt_nonneg (3 / 100 : ℝ)
  have hsqrt : Real.sqrt (3 / 100 : ℝ) < 7 / 40 := by nlinarith
  unfold defaultParameter
  refine ⟨by positivity, ?_, ?_⟩
  · nlinarith
  · nlinarith

theorem default_small_defect_criterion (lambda : ℝ) (hzero : 0 ≤ lambda)
    (hupper : lambda ≤ 3 / 100) : 4 * defaultBeta ^ 2 * defaultDefect lambda < 1 := by
  rw [default_parameter_identity]
  have h := default_parameter_interval lambda hzero hupper
  linarith [h.2.1, h.2.2]

theorem default_reference_budget : 1 / (2 * defaultBeta) ≤ defaultReferenceFloor := by
  have hs : 0 < Real.sqrt (33 : ℝ) := by positivity
  unfold defaultBeta defaultReferenceFloor
  apply (div_le_div_iff₀ (by positivity) (by positivity)).2
  nlinarith

/-- Positivity of the proposed curvature/gap floor is certified on the full
default interval. Its Wilson interpretation still requires actual R4/R5. -/
theorem default_smallRoot_and_gap (lambda : ℝ) (hzero : 0 ≤ lambda)
    (hupper : lambda ≤ 3 / 100) :
    0 ≤ smallRoot defaultBeta (defaultDefect lambda) ∧
      smallRoot defaultBeta (defaultDefect lambda) < defaultReferenceFloor ∧
      0 < 2 * (defaultReferenceFloor - smallRoot defaultBeta (defaultDefect lambda)) := by
  have hc : 0 ≤ defaultDefect lambda := by unfold defaultDefect; positivity
  have hp := default_small_defect_criterion lambda hzero hupper
  have hr := smallRoot_nonneg defaultBeta (defaultDefect lambda) defaultBeta_pos hc hp
  have ha := smallRoot_lt_reference_floor defaultBeta (defaultDefect lambda)
    defaultReferenceFloor defaultBeta_pos hp default_reference_budget
  exact ⟨hr, ha, by linarith⟩

end Workhouse.SC17Riccati
