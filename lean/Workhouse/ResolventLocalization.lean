/-
Actual bounded-operator and Hilbert-space formalization of the resolvent and
Schur mechanisms in the September derivations. No Wilson domain identification,
Combes--Thomas estimate, or uniform physical Poincare constant is assumed to
follow from these abstract statements. The source hypotheses for those
applications remain distinct obligations.
-/
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Analysis.Normed.Ring.InfiniteSum
import Mathlib.Topology.Algebra.InfiniteSum.NatInt
import Mathlib.Tactic

namespace Workhouse.ResolventLocalization

section Neumann

variable {A : Type*} [NormedRing A]

/-- The inverse of `1 + C` is constructed as a convergent operator series. -/
noncomputable def neumann (C : A) : A := ∑' n : ℕ, (-C) ^ n

/-- BF1: convergence of the full infinite Neumann series. -/
theorem neumann_summable [CompleteSpace A] (C : A) (hC : ‖C‖ < 1) :
    Summable (fun n : ℕ => (-C) ^ n) :=
  summable_geometric_of_norm_lt_one (by simpa using hC)

/-- BF1: the constructed inverse is a right inverse. -/
theorem mul_neumann [CompleteSpace A] (C : A) (hC : ‖C‖ < 1) :
    (1 + C) * neumann C = 1 := by
  simpa [neumann] using mul_neg_geom_series (-C) (by simpa using hC)

/-- BF1: the constructed inverse is a left inverse. -/
theorem neumann_mul [CompleteSpace A] (C : A) (hC : ‖C‖ < 1) :
    neumann C * (1 + C) = 1 := by
  simpa [neumann] using geom_series_mul_neg (-C) (by simpa using hC)

/-- BF1: an operator norm bound, valid in any unital Banach algebra. -/
theorem norm_neumann_le [NormOneClass A] (C : A) (hC : ‖C‖ < 1) :
    ‖neumann C‖ ≤ (1 - ‖C‖)⁻¹ := by
  simpa [neumann] using tsum_geometric_le_of_norm_lt_one (-C) (by simpa using hC)

/-- BF1: the normalized inverse differs from the identity by a controlled amount. -/
theorem norm_neumann_sub_one_le [NormOneClass A] [CompleteSpace A]
    (C : A) (hC : ‖C‖ < 1) :
    ‖neumann C - 1‖ ≤ ‖C‖ / (1 - ‖C‖) := by
  have hid : neumann C - 1 = -(C * neumann C) := by
    have h := mul_neumann C hC
    rw [add_mul, one_mul] at h
    exact eq_neg_of_add_eq_zero_left (by rw [sub_add_eq_add_sub, h, sub_self])
  rw [hid, norm_neg]
  calc
    ‖C * neumann C‖ ≤ ‖C‖ * ‖neumann C‖ := norm_mul_le _ _
    _ ≤ ‖C‖ * (1 - ‖C‖)⁻¹ :=
      mul_le_mul_of_nonneg_left (norm_neumann_le C hC) (norm_nonneg C)
    _ = ‖C‖ / (1 - ‖C‖) := (div_eq_mul_inv _ _).symm

/-- BF1 with the external relative-form budget `theta`. -/
theorem norm_neumann_sub_one_le_budget [NormOneClass A] [CompleteSpace A]
    (C : A) (theta : ℝ)
    (hC : ‖C‖ ≤ theta) (htheta : theta < 1) :
    ‖neumann C - 1‖ ≤ theta / (1 - theta) := by
  have hc : ‖C‖ < 1 := hC.trans_lt htheta
  calc
    ‖neumann C - 1‖ ≤ ‖C‖ / (1 - ‖C‖) := norm_neumann_sub_one_le C hc
    _ ≤ theta / (1 - theta) := by
      apply (div_le_div_iff₀ (by linarith : 0 < 1 - ‖C‖)
        (by linarith : 0 < 1 - theta)).2
      nlinarith

end Neumann

section Algebra

variable {A : Type*} [Ring A]

/-- W6 / localization section 2.1: the signed second resolvent identity.
Only the stated left and right inverse laws are needed. -/
theorem signed_resolvent_identity (F0 Fg R0 Rg : A)
    (h0 : R0 * F0 = 1) (hg : Fg * Rg = 1) :
    R0 - Rg = R0 * (Fg - F0) * Rg := by
  rw [mul_sub, sub_mul, mul_assoc R0 Fg Rg, hg, mul_one, h0, one_mul]

end Algebra

section Hilbert

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- BF1: the scalar selected-resolvent pairing bound follows from the
constructed operator inverse, rather than being an input hypothesis. -/
theorem normalized_selected_pairing_bound [CompleteSpace E] [Nontrivial E]
    (C : E →L[ℝ] E) (theta : ℝ)
    (hC : ‖C‖ ≤ theta) (htheta : theta < 1) (w : E) :
    |inner ℝ w ((neumann C - 1) w)| ≤
      (theta / (1 - theta)) * ‖w‖ ^ 2 := by
  calc
    |inner ℝ w ((neumann C - 1) w)| ≤ ‖w‖ * ‖(neumann C - 1) w‖ :=
      abs_real_inner_le_norm _ _
    _ ≤ ‖w‖ * (‖neumann C - 1‖ * ‖w‖) :=
      mul_le_mul_of_nonneg_left ((neumann C - 1).le_opNorm w) (norm_nonneg w)
    _ ≤ ‖w‖ * ((theta / (1 - theta)) * ‖w‖) :=
      mul_le_mul_of_nonneg_left
        (mul_le_mul_of_nonneg_right
          (norm_neumann_sub_one_le_budget C theta hC htheta) (norm_nonneg w))
        (norm_nonneg w)
    _ = _ := by ring

/-- BF1: inserting the inverse-square-root map gives the source-weighted
bound. `L` is the supplied bounded realization of `A0^(-1/2)`. -/
theorem weighted_selected_pairing_bound [CompleteSpace E] [Nontrivial E]
    (C L : E →L[ℝ] E) (theta : ℝ)
    (hC : ‖C‖ ≤ theta) (htheta : theta < 1) (w : E) :
    |inner ℝ (L w) ((neumann C - 1) (L w))| ≤
      (theta / (1 - theta)) * ‖L w‖ ^ 2 :=
  normalized_selected_pairing_bound C theta hC htheta (L w)

/-- BF1 in the original source coordinate: the sandwiched inverse difference
is controlled by the reference energy `norm (L w)^2`. Symmetry of the supplied
inverse-square-root map is included as a mathematical hypothesis. -/
theorem weighted_inverse_difference_bound [CompleteSpace E] [Nontrivial E]
    (C L : E →L[ℝ] E) (theta : ℝ)
    (hC : ‖C‖ ≤ theta) (htheta : theta < 1)
    (hL : ∀ x y, inner ℝ (L x) y = inner ℝ x (L y)) (w : E) :
    |inner ℝ w ((L * neumann C * L - L * L) w)| ≤
      (theta / (1 - theta)) * ‖L w‖ ^ 2 := by
  change |inner ℝ w (L (neumann C (L w)) - L (L w))| ≤ _
  rw [← map_sub, ← hL]
  exact weighted_selected_pairing_bound C L theta hC htheta w

/-- Resolvent proposal section 2.1: equality of the actual Hilbert-space
pairings, with symmetry of the reference inverse explicitly required. -/
theorem signed_resolvent_pairing (F0 Fg R0 Rg : E →L[ℝ] E)
    (h0 : R0 * F0 = 1) (hg : Fg * Rg = 1)
    (hsym : ∀ x y, inner ℝ (R0 x) y = inner ℝ x (R0 y)) (w : E) :
    inner ℝ (R0 w) ((Fg - F0) (Rg w)) =
      inner ℝ w ((R0 - Rg) w) := by
  rw [hsym]
  congr 1
  exact (congrArg (fun T : E →L[ℝ] E => T w)
    (signed_resolvent_identity F0 Fg R0 Rg h0 hg)).symm

/-- The real quadratic fast form in SP3 / W4. -/
def schurEnergy (a : ℝ) (v : E) (A : E →L[ℝ] E) (q : E) : ℝ :=
  a + 2 * inner ℝ v q + inner ℝ q (A q)

/-- SP3 / W4 / BF3: exact completion of the interacting fast square.
The retained value `a` and graph force `v` are arbitrary; no reducing-source
assumption is imposed. -/
theorem schur_square_completion (a : ℝ) (v : E) (A R : E →L[ℝ] E)
    (hAR : A * R = 1)
    (hsym : ∀ x y, inner ℝ x (A y) = inner ℝ (A x) y) (q : E) :
    schurEnergy a v A q = a - inner ℝ v (R v) +
      inner ℝ (q + R v) (A (q + R v)) := by
  have hsolve : A (R v) = v := by
    exact congrArg (fun T : E →L[ℝ] E => T v) hAR
  have hcross : inner ℝ (R v) (A q) = inner ℝ v q := by
    rw [hsym, hsolve]
  simp only [schurEnergy, map_add, hsolve, inner_add_left, inner_add_right]
  rw [hcross, real_inner_comm q v, real_inner_comm (R v) v]
  ring

/-- W4: the graph correction `-R v` attains the stated Schur value. -/
theorem schur_minimizer_value (a : ℝ) (v : E) (A R : E →L[ℝ] E)
    (hAR : A * R = 1)
    (hsym : ∀ x y, inner ℝ x (A y) = inner ℝ (A x) y) :
    schurEnergy a v A (-R v) = a - inner ℝ v (R v) := by
  rw [schur_square_completion a v A R hAR hsym]
  simp

/-- W4: positivity of the full fast operator proves global minimization,
not merely stationarity of the proposed graph correction. -/
theorem schur_minimizer_lower_bound (a : ℝ) (v : E) (A R : E →L[ℝ] E)
    (hAR : A * R = 1)
    (hsym : ∀ x y, inner ℝ x (A y) = inner ℝ (A x) y)
    (hpos : ∀ x, 0 ≤ inner ℝ x (A x)) (q : E) :
    a - inner ℝ v (R v) ≤ schurEnergy a v A q := by
  rw [schur_square_completion a v A R hAR hsym]
  exact le_add_of_nonneg_right (hpos (q + R v))

/-- BF1 / SP2: a small operator perturbation has an actual coercive
quadratic form. This statement does not assume the coercivity conclusion. -/
theorem normalized_fast_coercive (C : E →L[ℝ] E) (theta : ℝ)
    (hC : ‖C‖ ≤ theta) (q : E) :
    (1 - theta) * ‖q‖ ^ 2 ≤ inner ℝ q ((1 + C) q) := by
  have hbound : |inner ℝ q (C q)| ≤ theta * ‖q‖ ^ 2 := by
    calc
      |inner ℝ q (C q)| ≤ ‖q‖ * ‖C q‖ := abs_real_inner_le_norm _ _
      _ ≤ ‖q‖ * (‖C‖ * ‖q‖) :=
        mul_le_mul_of_nonneg_left (C.le_opNorm q) (norm_nonneg q)
      _ ≤ ‖q‖ * (theta * ‖q‖) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_right hC (norm_nonneg q)) (norm_nonneg q)
      _ = _ := by ring
  have hlower := (abs_le.mp hbound).1
  simp only [add_apply, one_apply_eq_self,
    inner_add_right, real_inner_self_eq_norm_sq]
  nlinarith

/-- SP3--SP4: small bounded symmetric relative perturbations have a unique
minimizing graph correction. Invertibility and coercivity are proved from
the norm budget rather than included among the inputs. -/
theorem normalized_schur_unique_minimizer [CompleteSpace E] [Nontrivial E]
    (a : ℝ) (v : E) (C : E →L[ℝ] E) (theta : ℝ)
    (hC : ‖C‖ ≤ theta) (htheta : theta < 1)
    (hsym : ∀ x y, inner ℝ x (C y) = inner ℝ (C x) y) (q : E) :
    a - inner ℝ v (neumann C v) ≤ schurEnergy a v (1 + C) q ∧
      (schurEnergy a v (1 + C) q = a - inner ℝ v (neumann C v) ↔
        q = -(neumann C v)) := by
  have hAR := mul_neumann C (hC.trans_lt htheta)
  have hsymA : ∀ x y, inner ℝ x ((1 + C) y) = inner ℝ ((1 + C) x) y := by
    intro x y
    simp only [add_apply, one_apply_eq_self, inner_add_left, inner_add_right]
    rw [hsym]
  have hpos : ∀ x, 0 ≤ inner ℝ x ((1 + C) x) := by
    intro x
    exact (mul_nonneg (by linarith : 0 ≤ 1 - theta) (sq_nonneg ‖x‖)).trans
      (normalized_fast_coercive C theta hC x)
  refine ⟨schur_minimizer_lower_bound a v (1 + C) (neumann C) hAR hsymA hpos q, ?_⟩
  constructor
  · intro heq
    have hsquare := schur_square_completion a v (1 + C) (neumann C) hAR hsymA q
    have hzero : inner ℝ (q + neumann C v) ((1 + C) (q + neumann C v)) = 0 := by
      linarith
    have hcoercive := normalized_fast_coercive C theta hC (q + neumann C v)
    have hnorm : ‖q + neumann C v‖ ^ 2 = 0 := by
      rw [hzero] at hcoercive
      have hs := sq_nonneg ‖q + neumann C v‖
      nlinarith
    exact eq_neg_of_add_eq_zero_left (norm_eq_zero.mp (sq_eq_zero_iff.mp hnorm))
  · intro heq
    rw [heq]
    exact schur_minimizer_value a v (1 + C) (neumann C) hAR hsymA

end Hilbert

section Localization

variable {I J : Type*}

/-- Propagation of a finitely supported source retains its full l1 mass.
In particular a bound using only its supremum norm needs a support-cardinality
factor, absent from the submitted localization proposal for nonsingleton S0. -/
theorem finite_source_propagation (support : Finset I) (kernel source : I → ℝ)
    (envelope : ℝ)
    (hkernel : ∀ i ∈ support, |kernel i| ≤ envelope) :
    |∑ i ∈ support, kernel i * source i| ≤
      envelope * ∑ i ∈ support, |source i| := by
  calc
    |∑ i ∈ support, kernel i * source i| ≤
        ∑ i ∈ support, |kernel i * source i| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ i ∈ support, envelope * |source i| := by
      apply Finset.sum_le_sum
      intro i hi
      rw [abs_mul]
      exact mul_le_mul_of_nonneg_right (hkernel i hi) (abs_nonneg _)
    _ = _ := (Finset.mul_sum _ _ _).symm

/-- Localization section 2.3, with actual infinite sums: independent summable
left/right majorants and a bounded kernel imply absolute convergence and a
volume-independent bound. No Wilson kernel identification is inferred. -/
theorem localized_kernel_pairing (left : I → ℝ) (right : J → ℝ)
    (kernel : I → J → ℝ) (u : I → ℝ) (v : J → ℝ) (delta : ℝ)
    (hu : Summable u) (hv : Summable v) (hu0 : ∀ i, 0 ≤ u i)
    (hv0 : ∀ j, 0 ≤ v j) (hdelta : 0 ≤ delta)
    (hleft : ∀ i, |left i| ≤ u i) (hright : ∀ j, |right j| ≤ v j)
    (hkernel : ∀ i j, |kernel i j| ≤ delta) :
    Summable (fun p : I × J => left p.1 * kernel p.1 p.2 * right p.2) ∧
      |∑' p : I × J, left p.1 * kernel p.1 p.2 * right p.2| ≤
        delta * ((∑' i, u i) * (∑' j, v j)) := by
  have huv := hu.mul_of_nonneg hv hu0 hv0
  have hsum := (hu.hasSum.mul hv.hasSum huv).mul_left delta
  have hbound : ∀ p : I × J,
      ‖left p.1 * kernel p.1 p.2 * right p.2‖ ≤ delta * (u p.1 * v p.2) := by
    intro p
    simp only [Real.norm_eq_abs, abs_mul]
    calc
      |left p.1| * |kernel p.1 p.2| * |right p.2| ≤
          u p.1 * delta * v p.2 := by
        exact mul_le_mul
          (mul_le_mul (hleft p.1) (hkernel p.1 p.2) (abs_nonneg _) (hu0 _))
          (hright p.2) (abs_nonneg _) (mul_nonneg (hu0 _) hdelta)
      _ = _ := by ring
  exact ⟨hsum.summable.of_norm_bounded hbound,
    by simpa only [Real.norm_eq_abs] using tsum_of_norm_bounded hsum hbound⟩

/-- The same majorant controls every finite subvolume, without taking a
finite-volume observation as proof of the infinite-volume bound. -/
theorem localized_finite_volume_bound (term : I → ℝ) (majorant : I → ℝ)
    (hm : Summable majorant) (hm0 : ∀ i, 0 ≤ majorant i)
    (hterm : ∀ i, |term i| ≤ majorant i) (volume : Finset I) :
    |∑ i ∈ volume, term i| ≤ ∑' i, majorant i := by
  calc
    |∑ i ∈ volume, term i| ≤ ∑ i ∈ volume, |term i| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ i ∈ volume, majorant i := Finset.sum_le_sum fun i _ => hterm i
    _ ≤ ∑' i, majorant i := hm.sum_le_tsum volume (fun i _ => hm0 i)

/-- Exact one-dimensional exponential lattice sum, using `q = exp(-eta)`.
The hypotheses require an actual positive decay rate through `q < 1`. -/
theorem integer_geometric_hasSum (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q < 1) :
    HasSum (fun z : ℤ => q ^ z.natAbs) ((1 + q) / (1 - q)) := by
  have hnat := hasSum_geometric_of_lt_one hq0 hq1
  have hneg : HasSum (fun n : ℕ => q ^ (n + 1)) (q * (1 - q)⁻¹) := by
    simpa only [pow_succ', mul_comm] using hnat.mul_left q
  have hnat' : HasSum (fun n : ℕ => q ^ (n : ℤ).natAbs) ((1 - q)⁻¹) := by
    simpa only [Int.natAbs_natCast] using hnat
  have hneg' : HasSum (fun n : ℕ => q ^ (-(n + 1 : ℤ)).natAbs)
      (q * (1 - q)⁻¹) := by
    convert hneg using 1
    funext n
    congr 1
  have h := HasSum.of_nat_of_neg_add_one (f := fun z : ℤ => q ^ z.natAbs) hnat' hneg'
  convert h using 1
  simp only [div_eq_mul_inv]
  ring

/-- A concrete recursive presentation of the integer lattice of dimension d. -/
def CubicLattice : ℕ → Type
  | 0 => Unit
  | d + 1 => ℤ × CubicLattice d

/-- Product exponential weight, equivalent to `q` to the lattice l1 distance. -/
def cubicWeight (q : ℝ) : (d : ℕ) → CubicLattice d → ℝ
  | 0, _ => 1
  | d + 1, x => q ^ x.1.natAbs * cubicWeight q d x.2

/-- Positivity of the majorant in every lattice dimension. -/
theorem cubicWeight_nonneg (q : ℝ) (hq : 0 ≤ q) (d : ℕ)
    (x : CubicLattice d) : 0 ≤ cubicWeight q d x := by
  induction d with
  | zero => exact zero_le_one
  | succ d ih => exact mul_nonneg (pow_nonneg hq _) (ih x.2)

/-- Localization section 2.3: the infinite cubic-lattice sum is exactly the
displayed product constant, not merely bounded on tested lattice sizes. -/
theorem cubic_geometric_hasSum (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q < 1) (d : ℕ) :
    HasSum (cubicWeight q d) (((1 + q) / (1 - q)) ^ d) := by
  induction d with
  | zero =>
      simp [CubicLattice, cubicWeight]
  | succ d ih =>
      have hz := integer_geometric_hasSum q hq0 hq1
      have hprod := hz.mul ih (hz.summable.mul_of_nonneg ih.summable
        (fun z => pow_nonneg hq0 z.natAbs) (cubicWeight_nonneg q hq0 d))
      simpa only [CubicLattice, cubicWeight, pow_succ'] using hprod

/-- Conditional lattice localization in every dimension: given the actual
decay envelopes, the infinite pairing converges absolutely and obeys an
explicit constant independent of the choice of finite subvolume. -/
theorem cubic_localized_pairing (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q < 1) (d : ℕ)
    (left right : CubicLattice d → ℝ)
    (kernel : CubicLattice d → CubicLattice d → ℝ) (delta : ℝ)
    (hdelta : 0 ≤ delta)
    (hleft : ∀ x, |left x| ≤ cubicWeight q d x)
    (hright : ∀ x, |right x| ≤ cubicWeight q d x)
    (hkernel : ∀ x y, |kernel x y| ≤ delta) :
    Summable (fun p : CubicLattice d × CubicLattice d =>
      left p.1 * kernel p.1 p.2 * right p.2) ∧
      |∑' p : CubicLattice d × CubicLattice d,
        left p.1 * kernel p.1 p.2 * right p.2| ≤
        delta * (((1 + q) / (1 - q)) ^ d) ^ 2 := by
  have hc := cubic_geometric_hasSum q hq0 hq1 d
  have hp := localized_kernel_pairing left right kernel
    (cubicWeight q d) (cubicWeight q d) delta hc.summable hc.summable
    (cubicWeight_nonneg q hq0 d) (cubicWeight_nonneg q hq0 d)
    hdelta hleft hright hkernel
  simpa only [hc.tsum_eq, pow_two] using hp

end Localization

section CubicRemainder

variable {A : Type*} [NormedRing A] [CompleteSpace A]

/-- BF1 / SP7--SP9: exact noncommutative third-order remainder of the
constructed inverse after its quadratic Taylor polynomial. -/
theorem neumann_quadratic_remainder_identity (C : A) (hC : ‖C‖ < 1) :
    neumann C - (1 - C + C ^ 2) = -(C ^ 3 * neumann C) := by
  have hpoly : (1 - C + C ^ 2) * (1 + C) = 1 + C ^ 3 := by
    noncomm_ring
  have h := congrArg (fun T : A => (1 - C + C ^ 2) * T) (mul_neumann C hC)
  rw [← mul_assoc, hpoly, add_mul, one_mul, mul_one] at h
  apply eq_neg_of_add_eq_zero_left
  rw [sub_add_eq_add_sub, h, sub_self]

/-- The inverse expansion contains a genuine operator-valued remainder,
given explicitly rather than postulated through a norm hypothesis. -/
theorem neumann_quadratic_expansion (C : A) (hC : ‖C‖ < 1) :
    neumann C = 1 - C + C ^ 2 + -(C ^ 3 * neumann C) := by
  have h := neumann_quadratic_remainder_identity C hC
  exact (sub_eq_iff_eq_add.mp h).trans (add_comm _ _)

/-- BF1 / SP7--SP9: the quadratic inverse approximation has a cubic
operator norm error with the full geometric denominator retained. -/
theorem norm_neumann_quadratic_remainder_le [NormOneClass A]
    (C : A) (hC : ‖C‖ < 1) :
    ‖neumann C - (1 - C + C ^ 2)‖ ≤ ‖C‖ ^ 3 / (1 - ‖C‖) := by
  rw [neumann_quadratic_remainder_identity C hC, norm_neg]
  calc
    ‖C ^ 3 * neumann C‖ ≤ ‖C ^ 3‖ * ‖neumann C‖ := norm_mul_le _ _
    _ ≤ ‖C‖ ^ 3 * (1 - ‖C‖)⁻¹ :=
      mul_le_mul (norm_pow_le C 3) (norm_neumann_le C hC)
        (norm_nonneg _) (pow_nonneg (norm_nonneg _) _)
    _ = _ := (div_eq_mul_inv _ _).symm

/-- The cubic error persists under arbitrary bounded left/right source
maps; the two operator norms remain explicit in the bound. -/
theorem norm_sandwiched_neumann_quadratic_remainder_le [NormOneClass A]
    (C U V : A) (hC : ‖C‖ < 1) :
    ‖U * (neumann C - (1 - C + C ^ 2)) * V‖ ≤
      ‖U‖ * (‖C‖ ^ 3 / (1 - ‖C‖)) * ‖V‖ := by
  calc
    ‖U * (neumann C - (1 - C + C ^ 2)) * V‖ ≤
        ‖U * (neumann C - (1 - C + C ^ 2))‖ * ‖V‖ := norm_mul_le _ _
    _ ≤ (‖U‖ * ‖neumann C - (1 - C + C ^ 2)‖) * ‖V‖ :=
      mul_le_mul_of_nonneg_right (norm_mul_le _ _) (norm_nonneg _)
    _ ≤ _ := mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_left (norm_neumann_quadratic_remainder_le C hC)
        (norm_nonneg _)) (norm_nonneg _)

end CubicRemainder

section CubicPairing

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [CompleteSpace E] [Nontrivial E]

/-- The actual Hilbert-space selected pairing inherits the cubic inverse
remainder. Substituting `w = L source` gives its weighted source version. -/
theorem neumann_quadratic_remainder_pairing_bound
    (C : E →L[ℝ] E) (hC : ‖C‖ < 1) (w : E) :
    |inner ℝ w ((neumann C - (1 - C + C ^ 2) : E →L[ℝ] E) w)| ≤
      (‖C‖ ^ 3 / (1 - ‖C‖)) * ‖w‖ ^ 2 := by
  calc
    |inner ℝ w ((neumann C - (1 - C + C ^ 2) : E →L[ℝ] E) w)| ≤
        ‖w‖ * ‖(neumann C - (1 - C + C ^ 2) : E →L[ℝ] E) w‖ :=
      abs_real_inner_le_norm _ _
    _ ≤ ‖w‖ * (‖(neumann C - (1 - C + C ^ 2) : E →L[ℝ] E)‖ * ‖w‖) :=
      mul_le_mul_of_nonneg_left
        ((neumann C - (1 - C + C ^ 2)).le_opNorm w) (norm_nonneg w)
    _ ≤ ‖w‖ * ((‖C‖ ^ 3 / (1 - ‖C‖)) * ‖w‖) :=
      mul_le_mul_of_nonneg_left
        (mul_le_mul_of_nonneg_right (norm_neumann_quadratic_remainder_le C hC)
          (norm_nonneg w)) (norm_nonneg w)
    _ = _ := by ring

end CubicPairing

end Workhouse.ResolventLocalization
