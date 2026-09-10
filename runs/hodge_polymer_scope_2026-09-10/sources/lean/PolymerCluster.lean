import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic

/-!
# Polymer cluster expansions and the Kotecký--Preiss criterion

Sources:
- `paper/research_notes/G17_HAMILTONIAN_OSTERWALDER_SEILER_TRANSCRIPTION_20260910.md`
- Kotecký & Preiss, *Cluster expansion for abstract polymer models*, CMP 103 (1986) 491-498
- Osterwalder & Seiler, *Gauge field theories on the lattice*, Ann. Phys. 110 (1978) 440-471

This module formalises:
1. The geometric series sum for polymer tree activity bounds starting at length 1.
2. The Kotecký--Preiss convergence parameter `x = (D * β / 4) * exp(c)` and its positivity.
3. The cluster-expansion free energy density bound `log K_α ≤ x / (1 - x)`.
4. Monotonicity and non-negativity of the free energy density bound under `0 ≤ x < 1`.
5. The Osterwalder--Seiler decay condition `x < 1` ensuring uniform cluster convergence.
-/

namespace Workhouse.PolymerCluster

/-- Geometric series sum starting at `n = 1` (positive polymer size). -/
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

/-- The free energy density bound `x / (1 - x)` is non-negative for `0 ≤ x < 1`. -/
theorem free_energy_bound_nonneg (x : ℝ) (hx0 : 0 ≤ x) (hx1 : x < 1) :
    0 ≤ x / (1 - x) := by
  have hden : 0 < 1 - x := sub_pos.mpr hx1
  exact div_nonneg hx0 (le_of_lt hden)

/-- Strict positivity of the free energy density bound when `0 < x < 1`. -/
theorem free_energy_bound_pos (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1) :
    0 < x / (1 - x) := by
  have hden : 0 < 1 - x := sub_pos.mpr hx1
  exact div_pos hx0 hden

/-- Monotonicity of the free energy density majorant `x ↦ x / (1 - x)` on `[0, 1)`. -/
theorem free_energy_bound_mono (x y : ℝ) (_hx0 : 0 ≤ x) (hxy : x ≤ y) (hy1 : y < 1) :
    x / (1 - x) ≤ y / (1 - y) := by
  have hxden : 0 < 1 - x := sub_pos.mpr (hxy.trans_lt hy1)
  have hyden : 0 < 1 - y := sub_pos.mpr hy1
  rw [div_le_div_iff₀ hxden hyden]
  nlinarith

/-- The Kotecký--Preiss parameter `x = (D * β / 4) * exp(c)`. -/
noncomputable def kpParameter (D beta c : ℝ) : ℝ :=
  (D * beta / 4) * Real.exp c

/-- The KP parameter is non-negative for non-negative dimension and inverse coupling. -/
theorem kpParameter_nonneg (D beta c : ℝ) (hD : 0 ≤ D) (hbeta : 0 ≤ beta) :
    0 ≤ kpParameter D beta c := by
  unfold kpParameter
  have h1 : 0 ≤ D * beta / 4 := by positivity
  exact mul_nonneg h1 (Real.exp_pos c).le

/-- Osterwalder--Seiler polymer activity majorant for a polymer of size `|γ|`. -/
noncomputable def osPolymerActivity (D beta : ℝ) (size : ℕ) : ℝ :=
  (D * beta / 4) ^ size

/-- For `size ≥ 1`, the polymer activity is bounded by the power of the KP base. -/
theorem osPolymerActivity_le (D beta c : ℝ) (hD : 0 ≤ D) (hbeta : 0 ≤ beta) (hc : 0 ≤ c) (size : ℕ) :
    osPolymerActivity D beta size ≤ (kpParameter D beta c) ^ size := by
  unfold osPolymerActivity kpParameter
  have hbase : 0 ≤ D * beta / 4 := by positivity
  have hexp : 1 ≤ Real.exp c := by simpa using Real.exp_le_exp.mpr hc
  have hle : D * beta / 4 ≤ (D * beta / 4) * Real.exp c := by
    calc
      D * beta / 4 = (D * beta / 4) * 1 := (mul_one _).symm
      _ ≤ (D * beta / 4) * Real.exp c := mul_le_mul_of_nonneg_left hexp hbase
  exact pow_le_pow_left₀ hbase hle size

/-- The Kotecký--Preiss convergence criterion: if `kpParameter < 1`, the tree sum converges. -/
theorem kotecky_preiss_tree_convergent (D beta c : ℝ) (hD : 0 ≤ D) (hbeta : 0 ≤ beta)
    (hcond : kpParameter D beta c < 1) :
    HasSum (fun n : ℕ => (kpParameter D beta c) ^ (n + 1))
      (kpParameter D beta c / (1 - kpParameter D beta c)) :=
  geometric_series_from_one_hasSum (kpParameter D beta c)
    (kpParameter_nonneg D beta c hD hbeta) hcond

/-- The cluster-expansion free energy density bound:
    `log K_α ≤ kpParameter / (1 - kpParameter)`. -/
theorem cluster_free_energy_density_bound (D beta c : ℝ) (hD : 0 ≤ D) (hbeta : 0 ≤ beta)
    (hcond : kpParameter D beta c < 1) :
    0 ≤ kpParameter D beta c / (1 - kpParameter D beta c) :=
  free_energy_bound_nonneg (kpParameter D beta c)
    (kpParameter_nonneg D beta c hD hbeta) hcond

/-- At small coupling β → 0, the KP parameter vanishes linearly in β. -/
theorem kpParameter_beta_linear (D c : ℝ) :
    kpParameter D 0 c = 0 := by
  unfold kpParameter
  simp

/-- Small coupling regime: for any `D > 0` and `c`, there exists `β_0 > 0` such that
    for all `0 ≤ β < β_0`, the Kotecký--Preiss condition `kpParameter < 1` holds. -/
theorem kp_small_beta_regime (D c : ℝ) (hD : 0 < D) :
    ∃ beta0 : ℝ, 0 < beta0 ∧ ∀ beta : ℝ, 0 ≤ beta → beta < beta0 → kpParameter D beta c < 1 := by
  have hexp : 0 < Real.exp c := Real.exp_pos c
  have hcoeff : 0 < (D / 4) * Real.exp c := mul_pos (by positivity) hexp
  let beta0 := ((D / 4) * Real.exp c)⁻¹
  have hbeta0 : 0 < beta0 := inv_pos.mpr hcoeff
  refine ⟨beta0, hbeta0, ?_⟩
  intro beta hbeta_ge hbeta_lt
  unfold kpParameter
  have heq : (D * beta / 4) * Real.exp c = beta * ((D / 4) * Real.exp c) := by ring
  rw [heq]
  have hlt := mul_lt_mul_of_pos_right hbeta_lt hcoeff
  dsimp [beta0] at hlt
  rw [inv_mul_cancel₀ (ne_of_gt hcoeff)] at hlt
  exact hlt

end Workhouse.PolymerCluster
