/-
W6_PATH_FORWARD.md, R1--R6: the variational residual identity and a sufficient
residual certificate on arbitrary real Hilbert spaces, using actual bounded
operators and continuous linear functionals. The lower energy is represented
by a continuous linear equivalence, so its dual norm is an actual operator
norm after changing energy coordinates.

The interacting Wilson realization, its possibly unbounded form domains, the
construction of the local factorization, and uniform kernel/coercivity
estimates are separate obligations. In particular, no Gaussian cubic estimate
is silently identified with the complete interacting residual.
-/
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace Workhouse.W6Residual

section Hilbert

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The bounded realization of the interacting form residual at `R0 t`. -/
def residual (Ag R0 : E →L[ℝ] E) (t : E) : E := Ag (R0 t) - t

/-- The actual continuous residual functional. For real inner products its
value is both `inner r v` and `inner v r`. -/
noncomputable def residualFunctional (Ag R0 : E →L[ℝ] E) (t : E) : E →L[ℝ] ℝ :=
  innerSL ℝ (residual Ag R0 t)

/-- The dual norm for the lower quadratic energy `ell(v) = norm (U v)^2`.
This is a norm of a continuous functional, rather than a postulated budget. -/
noncomputable def energyDualNorm (U : E ≃L[ℝ] E) (f : E →L[ℝ] ℝ) : ℝ :=
  ‖f.comp U.symm.toContinuousLinearMap‖

/-- A residual functional is bounded by its actual lower-energy dual norm. -/
theorem functional_le_energyDualNorm (U : E ≃L[ℝ] E) (f : E →L[ℝ] ℝ) (v : E) :
    |f v| ≤ energyDualNorm U f * ‖U v‖ := by
  simpa [energyDualNorm, Real.norm_eq_abs] using
    (f.comp U.symm.toContinuousLinearMap).le_opNorm (U v)

/-- R1: completing the interacting quadratic form at two actual solution
vectors. The operators need not commute. -/
theorem residual_square_completion (Ag : E →L[ℝ] E) (t u w : E)
    (hsym : ∀ x y, inner ℝ x (Ag y) = inner ℝ (Ag x) y)
    (hw : Ag w = t) :
    inner ℝ t (w - u) = -inner ℝ u (Ag u - t) +
      inner ℝ (u - w) (Ag (u - w)) := by
  have hcross : inner ℝ w (Ag u) = inner ℝ t u := by rw [hsym, hw]
  simp only [map_sub, inner_sub_left, inner_sub_right, hw, hcross]
  rw [real_inner_comm w t]
  ring

/-- R1: the exact selected inverse difference is the negative Gaussian
diagonal form difference plus the interacting inverse residual energy. -/
theorem variational_residual_identity (A0 Ag R0 Rg : E →L[ℝ] E)
    (h0 : A0 * R0 = 1) (hg : Ag * Rg = 1) (hginv : Rg * Ag = 1)
    (hsym : ∀ x y, inner ℝ x (Ag y) = inner ℝ (Ag x) y) (t : E) :
    inner ℝ t ((Rg - R0) t) =
      -inner ℝ (R0 t) ((Ag - A0) (R0 t)) +
        inner ℝ (residual Ag R0 t) (Rg (residual Ag R0 t)) := by
  have h0t : A0 (R0 t) = t := congrArg (fun T : E →L[ℝ] E => T t) h0
  have hgt : Ag (Rg t) = t := congrArg (fun T : E →L[ℝ] E => T t) hg
  have hinv : Rg (Ag (R0 t)) = R0 t :=
    congrArg (fun T : E →L[ℝ] E => T (R0 t)) hginv
  have hr : Rg (residual Ag R0 t) = R0 t - Rg t := by
    simp only [residual, map_sub, hinv]
  have he : Ag (R0 t - Rg t) = residual Ag R0 t := by
    simp only [residual, map_sub, hgt]
  simpa only [sub_apply, h0t, he, hr,
    real_inner_comm (R0 t - Rg t) (residual Ag R0 t)] using
    residual_square_completion Ag t (R0 t) (Rg t) hsym hgt

/-- R2: coercivity against an independently supplied lower energy controls
the actual interacting inverse quadratic form by the lower-energy dual norm.
Only a right inverse and the displayed coercivity estimate are needed. -/
theorem inverse_energy_le_dual (Ag Rg : E →L[ℝ] E) (U : E ≃L[ℝ] E)
    (κ : ℝ) (hκ : 0 < κ) (hg : Ag * Rg = 1)
    (hcoerc : ∀ v, κ * ‖U v‖ ^ 2 ≤ inner ℝ v (Ag v)) (r : E) :
    0 ≤ inner ℝ r (Rg r) ∧
      inner ℝ r (Rg r) ≤ energyDualNorm U (innerSL ℝ r) ^ 2 / κ := by
  let q := inner ℝ r (Rg r)
  let x := ‖U (Rg r)‖
  let n := energyDualNorm U (innerSL ℝ r)
  have hgr : Ag (Rg r) = r := congrArg (fun T : E →L[ℝ] E => T r) hg
  have hx : 0 ≤ x := norm_nonneg _
  have hn : 0 ≤ n := norm_nonneg _
  have hc : κ * x ^ 2 ≤ q := by
    simpa only [x, q, hgr, real_inner_comm (Rg r) r] using hcoerc (Rg r)
  have hq : 0 ≤ q := (mul_nonneg hκ.le (sq_nonneg x)).trans hc
  have hb : q ≤ n * x := by
    calc
      q ≤ |q| := le_abs_self q
      _ ≤ n * x := functional_le_energyDualNorm U (innerSL ℝ r) (Rg r)
  have hxbound : κ * x ≤ n := by
    by_cases hx0 : x = 0
    · simpa [hx0] using hn
    · have hxpos : 0 < x := lt_of_le_of_ne hx (Ne.symm hx0)
      nlinarith
  refine ⟨hq, (le_div_iff₀ hκ).2 ?_⟩
  calc
    q * κ ≤ (n * x) * κ := mul_le_mul_of_nonneg_right hb hκ.le
    _ = n * (κ * x) := by ring
    _ ≤ n * n := mul_le_mul_of_nonneg_left hxbound hn
    _ = _ := by ring

/-- When `U` represents the interacting energy itself, the inverse quadratic
form is exactly the squared continuous-functional dual norm. -/
theorem inverse_energy_eq_dual_norm_sq (Ag Rg : E →L[ℝ] E)
    (U : E ≃L[ℝ] E) (hg : Ag * Rg = 1)
    (hform : ∀ x y, inner ℝ x (Ag y) = inner ℝ (U x) (U y)) (r : E) :
    inner ℝ r (Rg r) = energyDualNorm U (innerSL ℝ r) ^ 2 := by
  have hgr : Ag (Rg r) = r := congrArg (fun T : E →L[ℝ] E => T r) hg
  have hf : (innerSL ℝ r).comp U.symm.toContinuousLinearMap =
      innerSL ℝ (U (Rg r)) := by
    ext v
    change inner ℝ r (U.symm v) = inner ℝ (U (Rg r)) v
    calc
      _ = inner ℝ (U.symm v) r := real_inner_comm _ _
      _ = inner ℝ v (U (Rg r)) := by
        simpa only [hgr, U.apply_symm_apply] using hform (U.symm v) (Rg r)
      _ = _ := real_inner_comm _ _
  rw [energyDualNorm, hf, innerSL_apply_norm]
  rw [← real_inner_self_eq_norm_sq, ← hform, hgr, real_inner_comm]

/-- R1 in the source's dual-energy notation, with the interacting energy
realized by the actual coordinate equivalence `Ug`. -/
theorem variational_residual_dual_identity (A0 Ag R0 Rg : E →L[ℝ] E)
    (Ug : E ≃L[ℝ] E)
    (h0 : A0 * R0 = 1) (hg : Ag * Rg = 1) (hginv : Rg * Ag = 1)
    (hsym : ∀ x y, inner ℝ x (Ag y) = inner ℝ (Ag x) y)
    (hform : ∀ x y, inner ℝ x (Ag y) = inner ℝ (Ug x) (Ug y)) (t : E) :
    inner ℝ t ((Rg - R0) t) =
      -inner ℝ (R0 t) ((Ag - A0) (R0 t)) +
        energyDualNorm Ug (residualFunctional Ag R0 t) ^ 2 := by
  rw [variational_residual_identity A0 Ag R0 Rg h0 hg hginv hsym t,
    inverse_energy_eq_dual_norm_sq Ag Rg Ug hg hform]
  rfl

/-- R2--R4: the actual selected inverse difference obeys the W6 error bound
from a lower-energy coercivity estimate and the two independently stated
diagonal/residual estimates. -/
theorem variational_residual_error_bound (A0 Ag R0 Rg : E →L[ℝ] E)
    (U : E ≃L[ℝ] E) (t : E) (κ a c g g0 b : ℝ)
    (hκ : 0 < κ) (_hc : 0 ≤ c) (hb : 0 ≤ b) (hg0 : |g| ≤ g0)
    (h0 : A0 * R0 = 1) (hg : Ag * Rg = 1) (hginv : Rg * Ag = 1)
    (hsym : ∀ x y, inner ℝ x (Ag y) = inner ℝ (Ag x) y)
    (hcoerc : ∀ v, κ * ‖U v‖ ^ 2 ≤ inner ℝ v (Ag v))
    (hdiag : |inner ℝ (R0 t) ((Ag - A0) (R0 t))| ≤ a * |g| * b)
    (hres : energyDualNorm U (residualFunctional Ag R0 t) ≤
      c * |g| * Real.sqrt b) :
    |inner ℝ t ((Rg - R0) t)| ≤ (a + κ⁻¹ * c ^ 2 * g0) * |g| * b := by
  have henergy := inverse_energy_le_dual Ag Rg U κ hκ hg hcoerc
    (residual Ag R0 t)
  have hsq : energyDualNorm U (residualFunctional Ag R0 t) ^ 2 ≤
      c ^ 2 * |g| ^ 2 * b := by
    calc
      _ ≤ (c * |g| * Real.sqrt b) ^ 2 :=
        pow_le_pow_left₀ (norm_nonneg _) hres 2
      _ = _ := by rw [mul_pow, mul_pow, Real.sq_sqrt hb]
  have hgg : |g| ^ 2 ≤ g0 * |g| := by
    nlinarith [abs_nonneg g]
  have hrem : inner ℝ (residual Ag R0 t) (Rg (residual Ag R0 t)) ≤
      (κ⁻¹ * c ^ 2 * g0) * |g| * b := by
    calc
      _ ≤ energyDualNorm U (residualFunctional Ag R0 t) ^ 2 / κ := henergy.2
      _ ≤ (c ^ 2 * |g| ^ 2 * b) / κ :=
        div_le_div_of_nonneg_right hsq hκ.le
      _ = (κ⁻¹ * c ^ 2 * b) * |g| ^ 2 := by ring
      _ ≤ (κ⁻¹ * c ^ 2 * b) * (g0 * |g|) :=
        mul_le_mul_of_nonneg_left hgg (by positivity)
      _ = _ := by ring
  rw [variational_residual_identity A0 Ag R0 Rg h0 hg hginv hsym t]
  calc
    _ ≤ |-(inner ℝ (R0 t) ((Ag - A0) (R0 t)))| +
        |inner ℝ (residual Ag R0 t) (Rg (residual Ag R0 t))| := abs_add_le _ _
    _ = |inner ℝ (R0 t) ((Ag - A0) (R0 t))| +
        inner ℝ (residual Ag R0 t) (Rg (residual Ag R0 t)) := by
      rw [abs_neg, abs_of_nonneg henergy.1]
    _ ≤ a * |g| * b + (κ⁻¹ * c ^ 2 * g0) * |g| * b := add_le_add hdiag hrem
    _ = _ := by ring

end Hilbert

section Factorization

variable {E P F : Type*}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [NormedAddCommGroup P] [NormedSpace ℝ P]
  [NormedAddCommGroup F] [InnerProductSpace ℝ F]

/-- The local residual factorization as a concrete continuous functional,
with arbitrary (possibly infinite-dimensional) source and kernel spaces. -/
noncomputable def factoredResidual (g : ℝ) (K : F →L[ℝ] F)
    (X : P →L[ℝ] F) (Y : E →L[ℝ] F) (p : P) : E →L[ℝ] ℝ :=
  g • (innerSL ℝ (X p)).comp (K.comp Y)

/-- R5--R6: square budgets for the actual maps yield the exact square-root
constant in the lower-energy dual norm. A kernel norm estimate is an explicit
input; a Gaussian Gram operator is not substituted for `K`. -/
theorem factored_residual_dual_bound (U : E ≃L[ℝ] E)
    (K : F →L[ℝ] F) (X : P →L[ℝ] F) (Y : E →L[ℝ] F)
    (g CB CL KF b : ℝ) (hCB : 0 ≤ CB) (hCL : 0 ≤ CL)
    (_hKF : 0 ≤ KF) (_hb : 0 ≤ b) (p : P)
    (hX : ‖X p‖ ^ 2 ≤ CB * b)
    (hY : ∀ v, ‖Y v‖ ^ 2 ≤ CL * ‖U v‖ ^ 2)
    (hK : ‖K‖ ^ 2 ≤ KF) :
    energyDualNorm U (factoredResidual g K X Y p) ≤
      |g| * Real.sqrt (CB * CL * KF) * Real.sqrt b := by
  have hX' : ‖X p‖ ≤ Real.sqrt CB * Real.sqrt b := by
    simpa only [Real.sqrt_mul hCB] using Real.le_sqrt_of_sq_le hX
  have hK' : ‖K‖ ≤ Real.sqrt KF := Real.le_sqrt_of_sq_le hK
  have hY' (v : E) : ‖Y v‖ ≤ Real.sqrt CL * ‖U v‖ := by
    simpa only [Real.sqrt_mul hCL, Real.sqrt_sq (norm_nonneg _)] using
      Real.le_sqrt_of_sq_le (hY v)
  unfold energyDualNorm
  apply ContinuousLinearMap.opNorm_le_bound _ (by positivity)
  intro v
  have hYv : ‖Y (U.symm v)‖ ≤ Real.sqrt CL * ‖v‖ := by
    simpa using hY' (U.symm v)
  calc
    ‖((factoredResidual g K X Y p).comp U.symm.toContinuousLinearMap) v‖ =
        |g| * |inner ℝ (X p) (K (Y (U.symm v)))| := by
      simp [factoredResidual, Real.norm_eq_abs]
    _ ≤ |g| * (‖X p‖ * ‖K (Y (U.symm v))‖) :=
      mul_le_mul_of_nonneg_left (abs_real_inner_le_norm _ _) (abs_nonneg g)
    _ ≤ |g| * (‖X p‖ * (‖K‖ * ‖Y (U.symm v)‖)) := by
      gcongr
      exact K.le_opNorm _
    _ ≤ |g| * ((Real.sqrt CB * Real.sqrt b) *
        (Real.sqrt KF * (Real.sqrt CL * ‖v‖))) := by gcongr
    _ = (|g| * Real.sqrt (CB * CL * KF) * Real.sqrt b) * ‖v‖ := by
      rw [Real.sqrt_mul (mul_nonneg hCB hCL), Real.sqrt_mul hCB]
      ring

/-- R1--R6 combined: the complete bounded-operator W6 certificate from an
actual residual factorization. The diagonal estimate remains an explicit,
separate hypothesis, as required by the variational source. -/
theorem factored_w6_bound (A0 Ag R0 Rg : E →L[ℝ] E)
    (U : E ≃L[ℝ] E) (K : F →L[ℝ] F) (X : P →L[ℝ] F)
    (Y : E →L[ℝ] F) (t : E) (p : P) (κ a g g0 CB CL KF b : ℝ)
    (hκ : 0 < κ) (hCB : 0 ≤ CB) (hCL : 0 ≤ CL) (hKF : 0 ≤ KF)
    (hb : 0 ≤ b) (hg0 : |g| ≤ g0)
    (h0 : A0 * R0 = 1) (hg : Ag * Rg = 1) (hginv : Rg * Ag = 1)
    (hsym : ∀ x y, inner ℝ x (Ag y) = inner ℝ (Ag x) y)
    (hcoerc : ∀ v, κ * ‖U v‖ ^ 2 ≤ inner ℝ v (Ag v))
    (hdiag : |inner ℝ (R0 t) ((Ag - A0) (R0 t))| ≤ a * |g| * b)
    (hfactor : residualFunctional Ag R0 t = factoredResidual g K X Y p)
    (hX : ‖X p‖ ^ 2 ≤ CB * b)
    (hY : ∀ v, ‖Y v‖ ^ 2 ≤ CL * ‖U v‖ ^ 2)
    (hK : ‖K‖ ^ 2 ≤ KF) :
    |inner ℝ t ((Rg - R0) t)| ≤
      (a + κ⁻¹ * (CB * CL * KF) * g0) * |g| * b := by
  have hres := factored_residual_dual_bound U K X Y g CB CL KF b
    hCB hCL hKF hb p hX hY hK
  rw [← hfactor] at hres
  rw [mul_comm |g| (Real.sqrt (CB * CL * KF))] at hres
  have h := variational_residual_error_bound A0 Ag R0 Rg U t κ a
    (Real.sqrt (CB * CL * KF)) g g0 b hκ (Real.sqrt_nonneg _) hb hg0
    h0 hg hginv hsym hcoerc hdiag hres
  simpa only [Real.sq_sqrt (mul_nonneg (mul_nonneg hCB hCL) hKF)] using h

end Factorization

section GaussianCoefficients

/-- The first coefficient in the dynamic cubic-energy bracket, with the
source spectral scale `c=1/(sqrt(33)L)` and `a=c/2`. -/
theorem gaussian_energy_coefficient_one (L : ℝ) (hL : 0 < L) :
    9 / ((1 / (Real.sqrt 33 * L)) / 2) = 18 * Real.sqrt 33 * L := by
  have hs : Real.sqrt 33 ≠ 0 := ne_of_gt (Real.sqrt_pos.2 (by norm_num))
  field_simp
  norm_num

/-- The second coefficient after the exact substitution `sigma=1/(2c)`. -/
theorem gaussian_energy_coefficient_two (L : ℝ) (hL : 0 < L) :
    18 * (1 / (2 * (1 / (Real.sqrt 33 * L)))) /
      ((1 / (Real.sqrt 33 * L)) / 2 + 1 / (Real.sqrt 33 * L)) = 198 * L ^ 2 := by
  have hs : Real.sqrt 33 ≠ 0 := ne_of_gt (Real.sqrt_pos.2 (by norm_num))
  have hs2 : (Real.sqrt 33) ^ 2 = 33 := Real.sq_sqrt (by norm_num)
  field_simp
  nlinarith [sq_nonneg L]

/-- The third coefficient, including its exact factor `1/5`. -/
theorem gaussian_energy_coefficient_three (L : ℝ) (hL : 0 < L) :
    6 * (1 / (2 * (1 / (Real.sqrt 33 * L)))) ^ 2 /
      ((1 / (Real.sqrt 33 * L)) / 2 + 2 * (1 / (Real.sqrt 33 * L))) =
        99 * Real.sqrt 33 * L ^ 3 / 5 := by
  have hs : Real.sqrt 33 ≠ 0 := ne_of_gt (Real.sqrt_pos.2 (by norm_num))
  have hs2 : (Real.sqrt 33) ^ 2 = 33 := Real.sq_sqrt (by norm_num)
  have hs3 : (Real.sqrt 33) ^ 3 = 33 * Real.sqrt 33 := by
    calc
      _ = (Real.sqrt 33) ^ 2 * Real.sqrt 33 := by ring
      _ = _ := by rw [hs2]
  field_simp
  nlinarith [sq_nonneg L]

end GaussianCoefficients

end Workhouse.W6Residual
