import Workhouse.W6Residual
import Workhouse.SC17Riccati
import Mathlib.Tactic

/-!
# Theory-current bridges from the 10 September 2026 exploration

These proofs connect the existing W6 residual, Riccati, Schur-graph and current
budget statements. They were originally checked through standard input during
a read-only exploration and are now preserved as an ordinary source module.

There are ten mathematical lemmas and one algebraic rearrangement helper.
The W6 inverse-pairing and composed error bounds concern bounded operators with
the displayed inverse hypotheses. Only
`factored_variational_energy_without_inverse` is inverse-free. Neither the
model-specific current factorization nor the unbounded Wilson form/domain
realization is constructed by these abstract statements.

Source derivations and exact symbolic current calculations are recorded in the
accompanying theory-current bridge evidence. The pre-existing modules retain
their original statements and source boundaries.
-/

namespace Workhouse.TheoryCurrentBridges

section Riccati

open Workhouse.SC17Riccati
variable {A : Type*} [NormedRing A] [NormedAlgebra ℝ A]
/-- An approximate solution in the contraction ball is controlled by its residual.
The fixed point and ball hypotheses are explicit; this does not identify a
physical Hessian with that fixed point. -/
theorem riccati_residual_certificate (S : A →L[ℝ] A) (D X Y : A)
    (beta r : ℝ) (hb : 0 ≤ beta) (hS : ‖S‖ ≤ beta)
    (hX : ‖X‖ ≤ r) (hY : ‖Y‖ ≤ r) (hq : 2 * beta * r < 1)
    (hfix : riccatiMap S D X = X) :
    ‖Y-X‖ ≤ ‖Y-riccatiMap S D Y‖ / (1-2*beta*r) := by
  have hl := riccatiMap_lipschitz_on_ball S D Y X beta r hb hS hY hX
  rw [hfix] at hl
  have ht := dist_triangle Y (riccatiMap S D Y) X
  simp only [dist_eq_norm] at ht
  apply (le_div_iff₀ (by linarith : 0 < 1-2*beta*r)).2
  nlinarith

/-- The existing default-parameter hypotheses imply a contraction factor below
3/20 on the whole interval. These remain conditional model inputs. -/
theorem riccati_default_contraction_bound (lambda : ℝ)
    (hzero : 0 ≤ lambda) (hupper : lambda ≤ 3/100) :
    2 * defaultBeta * smallRoot defaultBeta (defaultDefect lambda) < 3/20 := by
  have hp := default_parameter_interval lambda hzero hupper
  have hparam := default_parameter_identity lambda
  have hb := defaultBeta_pos
  have hr : 0 ≤ 1 - 4 * defaultBeta ^ 2 * defaultDefect lambda := by linarith
  have hs := Real.sq_sqrt hr
  have hn := Real.sqrt_nonneg (1 - 4 * defaultBeta ^ 2 * defaultDefect lambda)
  have hslo : (17/20 : ℝ) < Real.sqrt (1 - 4 * defaultBeta ^ 2 * defaultDefect lambda) := by
    nlinarith [hp.2.1, hp.2.2]
  have heq : 2 * defaultBeta * smallRoot defaultBeta (defaultDefect lambda) =
      1 - Real.sqrt (1 - 4 * defaultBeta ^ 2 * defaultDefect lambda) := by
    unfold smallRoot
    field_simp
  rw [heq]
  linarith

end Riccati

section W6Current

open Workhouse.W6Residual
variable {E F : Type*}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [NormedAddCommGroup F] [InnerProductSpace ℝ F]
/-- A possibly degenerate lower energy controls this selected inverse pairing.
The map Y need not be injective or invertible. Ag and Rg are still bounded
operators, and the displayed right-inverse identity is an explicit hypothesis. -/
theorem factored_inverse_energy_without_uniform_gap
    (Ag Rg : E →L[ℝ] E) (Y : E →L[ℝ] F) (r : E) (j : F)
    (g κ : ℝ) (hκ : 0 < κ) (hg : Ag * Rg = 1)
    (hcoerc : ∀ v, κ * ‖Y v‖ ^ 2 ≤ inner ℝ v (Ag v))
    (hfactor : ∀ v, inner ℝ r v = g * inner ℝ j (Y v)) :
    0 ≤ inner ℝ r (Rg r) ∧
      inner ℝ r (Rg r) ≤ g ^ 2 * ‖j‖ ^ 2 / κ := by
  let q := inner ℝ r (Rg r)
  let x := ‖Y (Rg r)‖
  let n := |g| * ‖j‖
  have hgr : Ag (Rg r) = r := congrArg (fun T : E →L[ℝ] E => T r) hg
  have hx : 0 ≤ x := norm_nonneg _
  have hn : 0 ≤ n := mul_nonneg (abs_nonneg g) (norm_nonneg j)
  have hc : κ * x ^ 2 ≤ q := by
    simpa only [x, q, hgr, real_inner_comm (Rg r) r] using hcoerc (Rg r)
  have hq : 0 ≤ q := (mul_nonneg hκ.le (sq_nonneg x)).trans hc
  have hb : q ≤ n * x := by
    calc
      q ≤ |q| := le_abs_self q
      _ = |g| * |inner ℝ j (Y (Rg r))| := by dsimp only [q]; rw [hfactor, abs_mul]
      _ ≤ |g| * (‖j‖ * ‖Y (Rg r)‖) :=
        mul_le_mul_of_nonneg_left (abs_real_inner_le_norm _ _) (abs_nonneg g)
      _ = n * x := by dsimp [n, x]; ring
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
    _ = g ^ 2 * ‖j‖ ^ 2 := by dsimp [n]; nlinarith [sq_abs g]

/-- The variational bound requires no inverse operator or nondegeneracy of Y.
The function a is arbitrary apart from the displayed lower bound; a closed-form
or physical Hamiltonian realization is a separate application. -/
theorem factored_variational_energy_without_inverse
    (Y : E →L[ℝ] F) (j : F) (a : E → ℝ) (g κ : ℝ) (hκ : 0 < κ)
    (hcoerc : ∀ v, κ * ‖Y v‖ ^ 2 ≤ a v) (v : E) :
    2 * g * inner ℝ j (Y v) - a v ≤ g ^ 2 * ‖j‖ ^ 2 / κ := by
  let x := ‖Y v‖
  let n := |g| * ‖j‖
  have hlin : g * inner ℝ j (Y v) ≤ n * x := by
    calc
      _ ≤ |g * inner ℝ j (Y v)| := le_abs_self _
      _ = |g| * |inner ℝ j (Y v)| := abs_mul _ _
      _ ≤ |g| * (‖j‖ * ‖Y v‖) :=
        mul_le_mul_of_nonneg_left (abs_real_inner_le_norm _ _) (abs_nonneg g)
      _ = _ := by dsimp [n, x]; ring
  have hc : κ * x ^ 2 ≤ a v := hcoerc v
  apply (le_div_iff₀ hκ).2
  calc
    (2 * g * inner ℝ j (Y v) - a v) * κ ≤
        (2 * n * x - κ * x ^ 2) * κ := by
      apply mul_le_mul_of_nonneg_right _ hκ.le
      nlinarith
    _ ≤ n ^ 2 := by nlinarith [sq_nonneg (n - κ * x)]
    _ = g ^ 2 * ‖j‖ ^ 2 := by dsimp [n]; rw [mul_pow, sq_abs]

/-- The bounded-operator W6 implication with lower energy represented by an
arbitrary Y. Both inverse identities remain explicit. In particular, the name
`gapless` does not assert an unbounded-operator or inverse-free W6 theorem. -/
theorem gapless_factored_w6_bound (A0 Ag R0 Rg : E →L[ℝ] E)
    (Y : E →L[ℝ] F) (t : E) (j : F) (κ a C g g0 b : ℝ)
    (hκ : 0 < κ) (hC : 0 ≤ C) (hb : 0 ≤ b) (hg0 : |g| ≤ g0)
    (h0 : A0 * R0 = 1) (hg : Ag * Rg = 1) (hginv : Rg * Ag = 1)
    (hsym : ∀ x y, inner ℝ x (Ag y) = inner ℝ (Ag x) y)
    (hcoerc : ∀ v, κ * ‖Y v‖ ^ 2 ≤ inner ℝ v (Ag v))
    (hdiag : |inner ℝ (R0 t) ((Ag - A0) (R0 t))| ≤ a * |g| * b)
    (hfactor : ∀ v, inner ℝ (residual Ag R0 t) v = g * inner ℝ j (Y v))
    (hj : ‖j‖ ^ 2 ≤ C * b) :
    |inner ℝ t ((Rg - R0) t)| ≤ (a + C * g0 / κ) * |g| * b := by
  have he := factored_inverse_energy_without_uniform_gap Ag Rg Y
    (residual Ag R0 t) j g κ hκ hg hcoerc hfactor
  have hgg : g ^ 2 ≤ g0 * |g| := by nlinarith [abs_nonneg g, sq_abs g]
  have hrem : inner ℝ (residual Ag R0 t) (Rg (residual Ag R0 t)) ≤
      (C * g0 / κ) * |g| * b := by
    calc
      _ ≤ g ^ 2 * ‖j‖ ^ 2 / κ := he.2
      _ ≤ g ^ 2 * (C * b) / κ := by gcongr
      _ ≤ (g0 * |g|) * (C * b) / κ :=
        div_le_div_of_nonneg_right
          (mul_le_mul_of_nonneg_right hgg (mul_nonneg hC hb)) hκ.le
      _ = _ := by ring
  rw [variational_residual_identity A0 Ag R0 Rg h0 hg hginv hsym t]
  calc
    _ ≤ |-(inner ℝ (R0 t) ((Ag - A0) (R0 t)))| +
        |inner ℝ (residual Ag R0 t) (Rg (residual Ag R0 t))| := abs_add_le _ _
    _ = |inner ℝ (R0 t) ((Ag - A0) (R0 t))| +
        inner ℝ (residual Ag R0 t) (Rg (residual Ag R0 t)) := by
      rw [abs_neg, abs_of_nonneg he.1]
    _ ≤ a * |g| * b + (C * g0 / κ) * |g| * b := add_le_add hdiag hrem
    _ = _ := by ring

end W6Current

section SourceCongruence

variable {A : Type*} [Ring A] [StarRing A]
/-- Transporting the retained coordinates cancels the two connection terms in
the displayed noncommutative congruence derivative. -/
theorem schur_connection_cancellation (S D L T : A) :
    star (-L*T)*S*T + star T*(D+S*L+star L*S)*T + star T*S*(-L*T)
      = star T*D*T := by
  simp only [star_mul, star_neg]
  noncomm_ring

/-- Algebraic rearrangement helper retained under its original exploration name.
No on-shell condition or metric-transport theorem is asserted by this identity. -/
theorem schur_metric_pairing_on_shell
    (S M T Tz : A) :
    star T*M*T - star Tz*S*T - star T*S*Tz
      = star T*M*T - (star Tz*S*T + star T*S*Tz) := by
  noncomm_ring

/-- The determinant numerator of a rotated real two-level matrix is independent
of the rotation when c squared plus s squared is one. -/
theorem rotated_two_level_schur_numerator (E F z c s : ℝ)
    (h : c^2+s^2=1) :
    (E*c^2+F*s^2-z)*(E*s^2+F*c^2-z)-(c*s*(F-E))^2
      = (E-z)*(F-z) := by
  have haux : (E*c^2+F*s^2-z)*(E*s^2+F*c^2-z)-(c*s*(F-E))^2
      - (E-z)*(F-z) =
      (c^2+s^2-1)*(E*F*(c^2+s^2+1)-z*(E+F)) := by ring
  rw [h] at haux
  nlinarith

end SourceCongruence

section RectangularGraph

open Matrix
variable {n m : Type*} [Fintype n] [Fintype m]
/-- A full rectangular graph relation gives the source-connection congruence
identity. The reference graph equation is an explicit matrix hypothesis. -/
theorem full_graph_source_ward
    (A K : Matrix n n ℝ) (J I : Matrix n m ℝ) (S : Matrix m m ℝ)
    (hA : A.transpose = A) (hK : K.transpose = -K)
    (hS : S.transpose = S) (hgraph : A * J = I * S) :
    J.transpose * (A*K-K*A) * J =
      S * (I.transpose*K*J) + (I.transpose*K*J).transpose * S := by
  have hl : J.transpose * A = S * I.transpose := by
    have ht := congrArg Matrix.transpose hgraph
    simpa only [Matrix.transpose_mul, hA, hS] using ht
  have hr : (I.transpose*K*J).transpose = -(J.transpose*K*I) := by
    simp only [Matrix.transpose_mul, Matrix.transpose_transpose, hK,
      Matrix.mul_neg, Matrix.neg_mul, Matrix.mul_assoc]
  rw [hr]
  calc
    J.transpose * (A*K-K*A) * J =
        (J.transpose*A)*K*J - (J.transpose*K)*(A*J) := by
      simp only [Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_assoc]
    _ = (S*I.transpose)*K*J - (J.transpose*K)*(I*S) := by rw [hl, hgraph]
    _ = S * (I.transpose*K*J) + -(J.transpose*K*I) * S := by
      simp only [Matrix.mul_assoc, Matrix.neg_mul, sub_eq_add_neg]

end RectangularGraph

section CurrentBudget

/-- A single scalar resolvent bound controls the combined zeroth- and first-energy
terms without taking separate spectral suprema. -/
theorem joint_resolvent_budget (A d m x : ℝ)
    (hA : 0 ≤ A) (hm : 0 < m) (hx : 0 ≤ x) (hmargin : d*m ≤ 2*A) :
    (A+d*x)/(x+m)^2 ≤ A/m^2 := by
  apply (div_le_div_iff₀ (sq_pos_of_pos (by linarith)) (sq_pos_of_pos hm)).2
  have hp : 0 ≤ x*(A*x+m*(2*A-d*m)) := by positivity
  nlinarith

/-- Scalar consequence of a selected residual bound, with no independent diagonal
budget. Applying it to operator inverse energies needs the signed residual
identity and nonnegative reference-energy data. -/
theorem residual_controls_inverse_without_diagonal
    (x y e : ℝ) (hy : 0 ≤ y) (he : 0 ≤ e)
    (hres : |x ^ 2 - y ^ 2| ≤ e * x) :
    |x ^ 2 - y ^ 2| ≤ e * y + e ^ 2 := by
  have hup := (abs_le.mp hres).2
  have hxy : x ≤ y + e := by
    by_contra h
    have hgap : 0 < x - y - e := by linarith
    have hsum : 0 < x + y := by linarith
    have hp := mul_pos hgap hsum
    have hey := mul_nonneg he hy
    nlinarith
  have hm := mul_le_mul_of_nonneg_left hxy he
  nlinarith

end CurrentBudget

end Workhouse.TheoryCurrentBridges
