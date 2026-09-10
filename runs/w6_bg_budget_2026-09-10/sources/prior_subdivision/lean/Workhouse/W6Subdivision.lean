/-
Scalar error-budget consequences of the actual compact Schur estimates.
Source: docs/research/w6-subdivided-compact-transport-2026-09-10.md, S4--S5.
Transport, source growth and the local cubic estimate are explicit inputs;
this module does not formalize the Wilson Hamiltonian or its transport ODE.
-/
import Mathlib.Analysis.PSeries
import Mathlib.Tactic

namespace Workhouse.W6Subdivision

/-- S4: summing `m` actual local errors of cubic size gains `m⁻²`. -/
theorem subdivided_cubic_error_bound (m : ℕ) (hm : 0 < m)
    (n A G : ℝ) (hn : 0 < n) (hA : 0 ≤ A) (hG : 0 ≤ G)
    (e h : Fin m → ℝ) (hh : ∀ i, 0 ≤ h i)
    (hstep : ∀ i, h i ≤ 1 / (n * m))
    (he : ∀ i, |e i| ≤ A * G * h i ^ 3) :
    |∑ i, e i| ≤ A * G / (n ^ 3 * (m : ℝ) ^ 2) := by
  have hm' : (0 : ℝ) < m := Nat.cast_pos.mpr hm
  calc
    |∑ i, e i| ≤ ∑ i, |e i| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ _i : Fin m, A * G * (1 / (n * m)) ^ 3 := by
      apply Finset.sum_le_sum
      intro i _
      apply (he i).trans
      gcongr
      exact hh i
      exact hstep i
    _ = A * G / (n ^ 3 * (m : ℝ) ^ 2) := by
      simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
      field_simp
      <;> ring

/-- S5: any subdivision whose squared count dominates source amplification
removes that amplification from the cubic budget. -/
theorem subdivision_absorbs_source_growth (m : ℕ) (hm : 0 < m)
    (n A G E : ℝ) (hn : 0 < n) (hA : 0 ≤ A)
    (hG : G ≤ (m : ℝ) ^ 2)
    (hE : |E| ≤ A * G / (n ^ 3 * (m : ℝ) ^ 2)) :
    |E| ≤ A / n ^ 3 := by
  have hm' : (0 : ℝ) < m := Nat.cast_pos.mpr hm
  calc
    |E| ≤ A * G / (n ^ 3 * (m : ℝ) ^ 2) := hE
    _ ≤ A * (m : ℝ) ^ 2 / (n ^ 3 * (m : ℝ) ^ 2) := by gcongr
    _ = A / n ^ 3 := by field_simp

/-- S5: every finite real amplification admits a finite positive subdivision.
The conclusion does not require a bounded amplification sequence. -/
theorem exists_subdivision_count (G : ℝ) :
    ∃ m : ℕ, 0 < m ∧ G ≤ (m : ℝ) ^ 2 := by
  obtain ⟨k, hk⟩ := exists_nat_gt (max G 1)
  have hk1 : (1 : ℝ) < k := lt_of_le_of_lt (le_max_right G 1) hk
  refine ⟨k, Nat.cast_pos.mp (lt_trans zero_lt_one hk1), ?_⟩
  have hGk : G < k := lt_of_le_of_lt (le_max_left G 1) hk
  nlinarith

/-- S5: the whole series of actual macro errors is absolutely summable under
the resulting cubic bound. No restriction on a source-growth exponent occurs. -/
theorem subdivided_error_absolutely_summable (A : ℝ) (e : ℕ → ℝ)
    (he : ∀ n, |e n| ≤ A / ((n : ℝ) + 1) ^ 3) :
    Summable (fun n => |e n|) := by
  have hbase : Summable (fun n : ℕ => 1 / (n : ℝ) ^ 3) :=
    Real.summable_one_div_nat_pow.mpr (by norm_num)
  have hshift : Summable (fun n : ℕ => 1 / ((n : ℝ) + 1) ^ 3) := by
    simpa only [Nat.cast_add, Nat.cast_one] using
      (summable_nat_add_iff 1).mpr hbase
  exact Summable.of_nonneg_of_le (fun n => abs_nonneg (e n))
    (by simpa only [div_eq_mul_inv, one_mul] using he) (hshift.mul_left A)

end Workhouse.W6Subdivision
