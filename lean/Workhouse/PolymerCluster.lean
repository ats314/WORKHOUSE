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

end Workhouse.PolymerCluster
