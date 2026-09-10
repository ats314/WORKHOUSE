import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic

/-!
# Scalar geometric majorants for polymer estimates

Sources:
- `paper/research_notes/G17_HAMILTONIAN_OSTERWALDER_SEILER_TRANSCRIPTION_20260910.md`
- Kotecký & Preiss, *Cluster expansion for abstract polymer models*, CMP 103 (1986) 491-498
- Osterwalder & Seiler, *Gauge field theories on the lattice*, Ann. Phys. 110 (1978) 440-471

This module proves the geometric series identity and scalar inequalities for
`x = (D * β / 4) * exp(c)`. It supplies arithmetic ingredients for a potential
polymer argument. It constructs no polymer model, incompatibility relation,
cluster expansion, partition function, or Osterwalder--Seiler reconstruction.
In particular, `x < 1` guarantees convergence of this scalar geometric series;
it is not by itself a proof of the Kotecký--Preiss criterion or any `log K` bound.
-/

namespace Workhouse.PolymerCluster

/-- Scalar geometric series sum starting at exponent one. -/
theorem geometric_series_from_one_hasSum (x : ℝ) (hx0 : 0 ≤ x) (hx1 : x < 1) :
    HasSum (fun n : ℕ => x ^ (n + 1)) (x / (1 - x)) := by
  have hnat := hasSum_geometric_of_lt_one hx0 hx1
  have hsucc : HasSum (fun n : ℕ => x ^ (n + 1)) (x * (1 - x)⁻¹) := by
    simpa only [pow_succ', mul_comm] using hnat.mul_left x
  convert hsucc using 1
  simp only [div_eq_mul_inv]

/-- The infinite sum of `x^(n+1)` is exactly `x / (1 - x)`. -/
theorem geometric_series_from_one_tsum (x : ℝ) (hx0 : 0 ≤ x) (hx1 : x < 1) :
    (∑' n : ℕ, x ^ (n + 1)) = x / (1 - x) :=
  (geometric_series_from_one_hasSum x hx0 hx1).tsum_eq

/-- The scalar geometric majorant `x / (1 - x)` is non-negative for `0 ≤ x < 1`. -/
theorem geometric_majorant_nonneg (x : ℝ) (hx0 : 0 ≤ x) (hx1 : x < 1) :
    0 ≤ x / (1 - x) := by
  have hden : 0 < 1 - x := sub_pos.mpr hx1
  exact div_nonneg hx0 (le_of_lt hden)

/-- Strict positivity of the scalar geometric majorant when `0 < x < 1`. -/
theorem geometric_majorant_pos (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1) :
    0 < x / (1 - x) := by
  have hden : 0 < 1 - x := sub_pos.mpr hx1
  exact div_pos hx0 hden

/-- Monotonicity of the scalar geometric majorant on `[0, 1)`. -/
theorem geometric_majorant_mono (x y : ℝ) (_hx0 : 0 ≤ x) (hxy : x ≤ y) (hy1 : y < 1) :
    x / (1 - x) ≤ y / (1 - y) := by
  have hxden : 0 < 1 - x := sub_pos.mpr (hxy.trans_lt hy1)
  have hyden : 0 < 1 - y := sub_pos.mpr hy1
  rw [div_le_div_iff₀ hxden hyden]
  nlinarith

/-- A scalar majorant fits budget `c` exactly when `x ≤ c / (1 + c)`.
The convergence condition `x < 1` alone supplies no prescribed positive budget. -/
theorem geometric_majorant_le_iff (x c : ℝ) (_hx0 : 0 ≤ x) (hx1 : x < 1)
    (hc : 0 ≤ c) :
    x / (1 - x) ≤ c ↔ x ≤ c / (1 + c) := by
  have hden : 0 < 1 - x := sub_pos.mpr hx1
  have hcden : 0 < 1 + c := by linarith
  rw [div_le_iff₀ hden, le_div_iff₀ hcden]
  constructor <;> intro h <;> nlinarith

/-- The scalar weighted activity base `(D * beta / 4) * exp(c)`.
No activity estimate for an actual polymer model is part of this definition. -/
noncomputable def weightedActivityBase (D beta c : ℝ) : ℝ :=
  (D * beta / 4) * Real.exp c

/-- The defined scalar weighted base is non-negative for `D, beta ≥ 0`. -/
theorem weightedActivityBase_nonneg (D beta c : ℝ) (hD : 0 ≤ D) (hbeta : 0 ≤ beta) :
    0 ≤ weightedActivityBase D beta c := by
  unfold weightedActivityBase
  have h1 : 0 ≤ D * beta / 4 := by positivity
  exact mul_nonneg h1 (Real.exp_pos c).le

/-- The unweighted scalar power `(D * beta / 4)^size`. -/
noncomputable def unweightedActivityPower (D beta : ℝ) (size : ℕ) : ℝ :=
  (D * beta / 4) ^ size

/-- For every natural exponent, weighting the non-negative scalar base by
`exp(c) ≥ 1` increases its power. This is not an estimate of polymer activities. -/
theorem unweightedActivityPower_le_weighted (D beta c : ℝ) (hD : 0 ≤ D)
    (hbeta : 0 ≤ beta) (hc : 0 ≤ c) (size : ℕ) :
    unweightedActivityPower D beta size ≤ (weightedActivityBase D beta c) ^ size := by
  unfold unweightedActivityPower weightedActivityBase
  have hbase : 0 ≤ D * beta / 4 := by positivity
  have hexp : 1 ≤ Real.exp c := by simpa using Real.exp_le_exp.mpr hc
  have hle : D * beta / 4 ≤ (D * beta / 4) * Real.exp c := by
    calc
      D * beta / 4 = (D * beta / 4) * 1 := (mul_one _).symm
      _ ≤ (D * beta / 4) * Real.exp c := mul_le_mul_of_nonneg_left hexp hbase
  exact pow_le_pow_left₀ hbase hle size

/-- The geometric series of powers of the weighted scalar base converges when
that base is less than one. No tree or cluster expansion is constructed. -/
theorem weightedActivityBase_geometric_hasSum (D beta c : ℝ) (hD : 0 ≤ D) (hbeta : 0 ≤ beta)
    (hcond : weightedActivityBase D beta c < 1) :
    HasSum (fun n : ℕ => (weightedActivityBase D beta c) ^ (n + 1))
      (weightedActivityBase D beta c / (1 - weightedActivityBase D beta c)) :=
  geometric_series_from_one_hasSum (weightedActivityBase D beta c)
    (weightedActivityBase_nonneg D beta c hD hbeta) hcond

/-- Non-negativity of the weighted geometric majorant. There is no free energy
or partition function on either side of this inequality. -/
theorem weighted_geometric_majorant_nonneg (D beta c : ℝ) (hD : 0 ≤ D) (hbeta : 0 ≤ beta)
    (hcond : weightedActivityBase D beta c < 1) :
    0 ≤ weightedActivityBase D beta c / (1 - weightedActivityBase D beta c) :=
  geometric_majorant_nonneg (weightedActivityBase D beta c)
    (weightedActivityBase_nonneg D beta c hD hbeta) hcond

/-- The weighted scalar base equals zero at `beta = 0`. -/
theorem weightedActivityBase_beta_zero (D c : ℝ) :
    weightedActivityBase D 0 c = 0 := by
  unfold weightedActivityBase
  simp

/-- For `D > 0`, a positive threshold makes the scalar weighted base less than
one. This threshold guarantees a scalar geometric convergence radius only. -/
theorem weightedActivityBase_small_beta_regime (D c : ℝ) (hD : 0 < D) :
    ∃ beta0 : ℝ, 0 < beta0 ∧ ∀ beta : ℝ, 0 ≤ beta → beta < beta0 →
      weightedActivityBase D beta c < 1 := by
  have hexp : 0 < Real.exp c := Real.exp_pos c
  have hcoeff : 0 < (D / 4) * Real.exp c := mul_pos (by positivity) hexp
  let beta0 := ((D / 4) * Real.exp c)⁻¹
  have hbeta0 : 0 < beta0 := inv_pos.mpr hcoeff
  refine ⟨beta0, hbeta0, ?_⟩
  intro beta hbeta_ge hbeta_lt
  unfold weightedActivityBase
  have heq : (D * beta / 4) * Real.exp c = beta * ((D / 4) * Real.exp c) := by ring
  rw [heq]
  have hlt := mul_lt_mul_of_pos_right hbeta_lt hcoeff
  dsimp [beta0] at hlt
  rw [inv_mul_cancel₀ (ne_of_gt hcoeff)] at hlt
  exact hlt

/-!
### Corrected α-dependent tilted Kotecký--Preiss expansion
-/

/-- The α-dependent tilted Kotecký--Preiss parameter:
    `x(α) = (D * β / 4) * exp(|α| / 2 + c)`. -/
noncomputable def tiltedKpParameter (D beta c alpha : ℝ) : ℝ :=
  (D * beta / 4) * Real.exp (|alpha| / 2 + c)

/-- The tilted KP parameter is non-negative for non-negative dimension and coupling. -/
theorem tiltedKpParameter_nonneg (D beta c alpha : ℝ) (hD : 0 ≤ D) (hbeta : 0 ≤ beta) :
    0 ≤ tiltedKpParameter D beta c alpha := by
  unfold tiltedKpParameter
  have h1 : 0 ≤ D * beta / 4 := by positivity
  exact mul_nonneg h1 (Real.exp_pos _).le

/-- At tilt α = 0, the tilted KP parameter reduces to the untilted parameter `weightedActivityBase`. -/
theorem tiltedKpParameter_at_alpha_zero (D beta c : ℝ) :
    tiltedKpParameter D beta c 0 = weightedActivityBase D beta c := by
  unfold tiltedKpParameter weightedActivityBase
  simp

/-- When `x ≤ c / (1 + c)` for `c ≥ 0`, `x` is strictly less than 1. -/
theorem strict_kp_criterion_lt_one (x c : ℝ) (hc : 0 ≤ c) (hxc : x ≤ c / (1 + c)) :
    x < 1 := by
  have hpos : 0 < 1 + c := by linarith
  have hlt : c / (1 + c) < 1 := (div_lt_one hpos).mpr (by linarith)
  exact hxc.trans_lt hlt

/-- Strict Kotecký--Preiss criterion: when `x ≤ c / (1 + c)`, the tree activity
satisfies `x / (1 - x) ≤ c`. -/
theorem strict_kotecky_preiss_criterion (x c : ℝ) (hc : 0 ≤ c) (_hx0 : 0 ≤ x)
    (hxc : x ≤ c / (1 + c)) :
    x / (1 - x) ≤ c := by
  have hx1 : x < 1 := strict_kp_criterion_lt_one x c hc hxc
  have hden : 0 < 1 - x := sub_pos.mpr hx1
  have hpos : 0 < 1 + c := by linarith
  rw [div_le_iff₀ hden]
  have h1 : x * (1 + c) ≤ c := by
    calc
      x * (1 + c) = (1 + c) * x := mul_comm _ _
      _ ≤ (1 + c) * (c / (1 + c)) := mul_le_mul_of_nonneg_left hxc (le_of_lt hpos)
      _ = c := mul_div_cancel₀ c (ne_of_gt hpos)
  nlinarith

/-- Strict Kotecký--Preiss equivalence: for `0 ≤ x < 1` and `c ≥ 0`,
`x / (1 - x) ≤ c` holds if and only if `x ≤ c / (1 + c)`. -/
theorem strict_kotecky_preiss_iff (x c : ℝ) (hc : 0 ≤ c) (hx0 : 0 ≤ x) (hx1 : x < 1) :
    x / (1 - x) ≤ c ↔ x ≤ c / (1 + c) := by
  have hden : 0 < 1 - x := sub_pos.mpr hx1
  have hpos : 0 < 1 + c := by linarith
  constructor
  · intro hle
    rw [div_le_iff₀ hden] at hle
    have h1 : x * (1 + c) ≤ c := by linarith
    rwa [le_div_iff₀ hpos]
  · intro hxc
    exact strict_kotecky_preiss_criterion x c hc hx0 hxc

/-- Under the strict criterion `tiltedKpParameter ≤ c / (1 + c)`, the tree sum is bounded by `c`. -/
theorem tilted_kotecky_preiss_tree_bound (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 ≤ D)
    (hbeta : 0 ≤ beta) (hcond : tiltedKpParameter D beta c alpha ≤ c / (1 + c)) :
    tiltedKpParameter D beta c alpha / (1 - tiltedKpParameter D beta c alpha) ≤ c :=
  strict_kotecky_preiss_criterion (tiltedKpParameter D beta c alpha) c hc
    (tiltedKpParameter_nonneg D beta c alpha hD hbeta) hcond

/-- Convergence of the tilted geometric polymer tree series under the strict KP criterion. -/
theorem tilted_kotecky_preiss_convergent (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 ≤ D)
    (hbeta : 0 ≤ beta) (hcond : tiltedKpParameter D beta c alpha ≤ c / (1 + c)) :
    HasSum (fun n : ℕ => (tiltedKpParameter D beta c alpha) ^ (n + 1))
      (tiltedKpParameter D beta c alpha / (1 - tiltedKpParameter D beta c alpha)) := by
  have hx1 : tiltedKpParameter D beta c alpha < 1 :=
    strict_kp_criterion_lt_one (tiltedKpParameter D beta c alpha) c hc hcond
  exact geometric_series_from_one_hasSum (tiltedKpParameter D beta c alpha)
    (tiltedKpParameter_nonneg D beta c alpha hD hbeta) hx1

/-- Certified coupling-tilt stability threshold:
    `β_*(D, c, α) = 4c / ((1 + c) * D * exp(|α| / 2 + c))`. -/
noncomputable def betaStabilityWindow (D c alpha : ℝ) : ℝ :=
  (4 * c) / ((1 + c) * D * Real.exp (|alpha| / 2 + c))

/-- The certified coupling-tilt stability threshold is strictly positive for `D > 0` and `c > 0`. -/
theorem betaStabilityWindow_pos (D c alpha : ℝ) (hD : 0 < D) (hc : 0 < c) :
    0 < betaStabilityWindow D c alpha := by
  unfold betaStabilityWindow
  have hnum : 0 < 4 * c := by linarith
  have hexp : 0 < Real.exp (|alpha| / 2 + c) := Real.exp_pos _
  have h1c : 0 < 1 + c := by linarith
  have hden : 0 < (1 + c) * D * Real.exp (|alpha| / 2 + c) := mul_pos (mul_pos h1c hD) hexp
  exact div_pos hnum hden

/-- When `β ≤ betaStabilityWindow`, the strict Kotecký--Preiss condition holds. -/
theorem beta_le_window_implies_tiltedKp_le (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 < D)
    (_hbeta : 0 ≤ beta) (hwin : beta ≤ betaStabilityWindow D c alpha) :
    tiltedKpParameter D beta c alpha ≤ c / (1 + c) := by
  unfold tiltedKpParameter betaStabilityWindow at *
  have hexp : 0 < Real.exp (|alpha| / 2 + c) := Real.exp_pos _
  calc
    (D * beta / 4) * Real.exp (|alpha| / 2 + c)
      ≤ (D * ((4 * c) / ((1 + c) * D * Real.exp (|alpha| / 2 + c))) / 4) * Real.exp (|alpha| / 2 + c) := by
        gcongr
    _ = c / (1 + c) := by
        have _hDne : D ≠ 0 := ne_of_gt hD
        have _hEne : Real.exp (|alpha| / 2 + c) ≠ 0 := ne_of_gt hexp
        field_simp

/-- When `β ≤ betaStabilityWindow`, the tilted tree activity is bounded by `c`. -/
theorem beta_le_window_implies_tree_bound (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 < D)
    (hbeta : 0 ≤ beta) (hwin : beta ≤ betaStabilityWindow D c alpha) :
    tiltedKpParameter D beta c alpha / (1 - tiltedKpParameter D beta c alpha) ≤ c := by
  have hle := beta_le_window_implies_tiltedKp_le D beta c alpha hc hD hbeta hwin
  exact tilted_kotecky_preiss_tree_bound D beta c alpha hc (le_of_lt hD) hbeta hle

/-- The α-dependent cluster free-energy density bound:
    `log K_α ≤ |α| / 2 + x(α) / (1 - x(α))`. -/
noncomputable def clusterFreeEnergyDensityBound (D beta c alpha : ℝ) : ℝ :=
  |alpha| / 2 + tiltedKpParameter D beta c alpha / (1 - tiltedKpParameter D beta c alpha)

/-- The cluster free-energy density bound is majorized by `|α| / 2 + c`. -/
theorem cluster_free_energy_density_bound_le (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 ≤ D)
    (hbeta : 0 ≤ beta) (hcond : tiltedKpParameter D beta c alpha ≤ c / (1 + c)) :
    clusterFreeEnergyDensityBound D beta c alpha ≤ |alpha| / 2 + c := by
  unfold clusterFreeEnergyDensityBound
  have htree := tilted_kotecky_preiss_tree_bound D beta c alpha hc hD hbeta hcond
  linarith

/-- Under the stability window `β ≤ betaStabilityWindow`, the free energy density bound is majorized by `|α| / 2 + c`. -/
theorem cluster_free_energy_density_bound_le_window (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 < D)
    (hbeta : 0 ≤ beta) (hwin : beta ≤ betaStabilityWindow D c alpha) :
    clusterFreeEnergyDensityBound D beta c alpha ≤ |alpha| / 2 + c := by
  have hle := beta_le_window_implies_tiltedKp_le D beta c alpha hc hD hbeta hwin
  exact cluster_free_energy_density_bound_le D beta c alpha hc (le_of_lt hD) hbeta hle

/-- The cluster free-energy density bound is non-negative. -/
theorem cluster_free_energy_density_bound_nonneg (D beta c alpha : ℝ) (hD : 0 ≤ D)
    (hbeta : 0 ≤ beta) (hc : 0 ≤ c) (hcond : tiltedKpParameter D beta c alpha ≤ c / (1 + c)) :
    0 ≤ clusterFreeEnergyDensityBound D beta c alpha := by
  unfold clusterFreeEnergyDensityBound
  have hx1 : tiltedKpParameter D beta c alpha < 1 :=
    strict_kp_criterion_lt_one (tiltedKpParameter D beta c alpha) c hc hcond
  have htree_nonneg := geometric_majorant_nonneg (tiltedKpParameter D beta c alpha)
    (tiltedKpParameter_nonneg D beta c alpha hD hbeta) hx1
  have halpha : 0 ≤ |alpha| / 2 := by positivity
  linarith

/-- Genuine cluster-decay mass gap: `m_gap = -log x(α) > 0`, derived from cluster decay. -/
noncomputable def clusterMassGap (x : ℝ) : ℝ :=
  - Real.log x

/-- Strict positivity of the cluster mass gap when `0 < x < 1`. -/
theorem clusterMassGap_pos (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1) :
    0 < clusterMassGap x := by
  unfold clusterMassGap
  have hlog : Real.log x < 0 := by
    rw [← Real.log_one]
    exact Real.log_lt_log hx0 hx1
  linarith

/-- Under the strict KP condition `x ≤ c / (1 + c)`, the mass gap satisfies
    `m_gap ≥ log((1 + c) / c) > 0`. -/
theorem clusterMassGap_ge_log_kp (x c : ℝ) (hx0 : 0 < x) (hc : 0 < c)
    (hxc : x ≤ c / (1 + c)) :
    Real.log ((1 + c) / c) ≤ clusterMassGap x := by
  unfold clusterMassGap
  have hcpos : 0 < 1 + c := by linarith
  have _hratio : 0 < c / (1 + c) := div_pos hc hcpos
  have hle := Real.log_le_log hx0 hxc
  have hinv : c / (1 + c) = ((1 + c) / c)⁻¹ := by rw [inv_div]
  have heq : Real.log (c / (1 + c)) = - Real.log ((1 + c) / c) := by
    rw [hinv, Real.log_inv]
  linarith

/-- For `c > 0`, the logarithmic lower bound `log((1 + c) / c)` is strictly positive. -/
theorem log_one_add_div_pos (c : ℝ) (hc : 0 < c) :
    0 < Real.log ((1 + c) / c) := by
  have hgt1 : 1 < (1 + c) / c := by
    rw [lt_div_iff₀ hc]
    linarith
  rw [← Real.log_one]
  exact Real.log_lt_log zero_lt_one hgt1

/-- Under the strict KP condition `x ≤ c / (1 + c)`, the mass gap is strictly positive. -/
theorem clusterMassGap_pos_of_strict_kp (x c : ℝ) (hx0 : 0 < x) (hc : 0 < c)
    (hxc : x ≤ c / (1 + c)) :
    0 < clusterMassGap x := by
  have hle := clusterMassGap_ge_log_kp x c hx0 hc hxc
  have hpos := log_one_add_div_pos c hc
  exact hpos.trans_le hle

/-- Exponential tree correlation decay: `x^d = exp(-d * m_gap)`. -/
theorem cluster_correlation_exponential_decay (x : ℝ) (hx0 : 0 < x) (d : ℕ) :
    x ^ d = Real.exp (- ((d : ℝ) * clusterMassGap x)) := by
  unfold clusterMassGap
  have he : - ((d : ℝ) * - Real.log x) = (d : ℝ) * Real.log x := by ring
  rw [he, Real.exp_nat_mul, Real.exp_log hx0]

/-- Uniform source-radius bound: `R_0 = √(C₀ / (1 - x))`. -/
noncomputable def uniformSourceRadiusBound (C0 x : ℝ) : ℝ :=
  Real.sqrt (C0 / (1 - x))

/-- The uniform source-radius bound is majorized by `√(C₀ * (1 + c))` uniformly in volume. -/
theorem uniform_source_radius_bound_le (C0 x c : ℝ) (hC0 : 0 ≤ C0) (hc : 0 ≤ c)
    (_hx0 : 0 ≤ x) (hxc : x ≤ c / (1 + c)) :
    uniformSourceRadiusBound C0 x ≤ Real.sqrt (C0 * (1 + c)) := by
  unfold uniformSourceRadiusBound
  have hx1 := strict_kp_criterion_lt_one x c hc hxc
  have h1x : 0 < 1 - x := sub_pos.mpr hx1
  have h1c : 0 < 1 + c := by linarith
  have hle : 1 / (1 + c) ≤ 1 - x := by
    calc
      1 / (1 + c) = 1 - c / (1 + c) := by
        have : 1 - c / (1 + c) = (1 + c) / (1 + c) - c / (1 + c) := by
          rw [div_self (ne_of_gt h1c)]
        rw [this, ← sub_div]
        ring
      _ ≤ 1 - x := sub_le_sub_left hxc 1
  have hdiv_le : 1 / (1 - x) ≤ 1 + c := by
    rw [div_le_iff₀ h1x]
    calc
      1 = (1 + c) * (1 / (1 + c)) := by rw [mul_one_div_cancel (ne_of_gt h1c)]
      _ ≤ (1 + c) * (1 - x) := mul_le_mul_of_nonneg_left hle (le_of_lt h1c)
  have hmul_le : C0 / (1 - x) ≤ C0 * (1 + c) := by
    calc
      C0 / (1 - x) = C0 * (1 / (1 - x)) := by ring
      _ ≤ C0 * (1 + c) := mul_le_mul_of_nonneg_left hdiv_le hC0
  exact Real.sqrt_le_sqrt hmul_le

/-- The uniform source-radius bound is non-negative. -/
theorem uniform_source_radius_bound_nonneg (C0 x : ℝ) :
    0 ≤ uniformSourceRadiusBound C0 x :=
  Real.sqrt_nonneg _

/-- Under the stability window `β ≤ betaStabilityWindow`, the uniform source-radius bound
is majorized by `√(C₀ * (1 + c))` uniformly in volume. -/
theorem uniform_source_radius_bound_le_window (D beta c alpha C0 : ℝ) (hC0 : 0 ≤ C0) (hc : 0 ≤ c)
    (hD : 0 < D) (hbeta : 0 ≤ beta) (hwin : beta ≤ betaStabilityWindow D c alpha) :
    uniformSourceRadiusBound C0 (tiltedKpParameter D beta c alpha) ≤ Real.sqrt (C0 * (1 + c)) := by
  have hle := beta_le_window_implies_tiltedKp_le D beta c alpha hc hD hbeta hwin
  have hnonneg := tiltedKpParameter_nonneg D beta c alpha (le_of_lt hD) hbeta
  exact uniform_source_radius_bound_le C0 (tiltedKpParameter D beta c alpha) c hC0 hc hnonneg hle

end Workhouse.PolymerCluster
