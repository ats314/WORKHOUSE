import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic

/-!
# The Feshbach channel of the plaquette Hodge algebra

Sources:
- `paper/research_notes/G14_HODGE_FESHBACH_CHANNEL_20260908.md`
- `docs/decisions/0045-the-feshbach-channel-is-generated-by-one-operator.md`
- `src/workhouse/invariants/hodge_feshbach.py`

This module proves abstract Hodge decomposition and carrier-line identities under
the displayed linear-map hypotheses. For `⟨ψ, ψ⟩ = q ≠ 0`, it distinguishes the
unnormalized rank-one Laplacian `L_up v = ⟨ψ, v⟩ ψ` from the normalized carrier
projection `P v = (⟨ψ, v⟩ / q) ψ`. It also proves the operator carrier factorization
for `R U R` when `U v = ell(v) ψ`.

The finite-word section only enumerates a syntactic filter and checks
identities between explicitly defined scalar polynomials. It does not evaluate
the Laurent-operator word table, prove that its seven filtered words have nonzero
defect, or identify those polynomials with the source's carrier symbols. Those
realization and operator-evaluation steps remain separate source obligations.
-/

namespace Workhouse.HodgeFeshbach

section HodgeAlgebra

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- The ring/algebraic relation: L_down + L_up = q • id and L_down ∘ L_up = 0
force L_down^2 = q • L_down, L_up ∘ L_down = 0, and L_up^2 = q • L_up. -/
theorem hodge_algebra_relations (q : K) (L_d L_u : V →ₗ[K] V)
    (hsum : L_d + L_u = q • LinearMap.id)
    (hcomp : L_d.comp L_u = 0) :
    L_d.comp L_d = q • L_d ∧
    L_u.comp L_d = 0 ∧
    L_u.comp L_u = q • L_u := by
  have h1 : (L_d.comp (L_d + L_u)) = L_d.comp (q • LinearMap.id) := by rw [hsum]
  have hd2 : L_d.comp L_d = q • L_d := by
    rw [LinearMap.comp_add, hcomp, add_zero, LinearMap.comp_smul, LinearMap.comp_id] at h1
    exact h1
  have h2 : (L_d + L_u).comp L_d = (q • LinearMap.id).comp L_d := by rw [hsum]
  have hud : L_u.comp L_d = 0 := by
    rw [LinearMap.add_comp, hd2, LinearMap.smul_comp, LinearMap.id_comp] at h2
    have : q • L_d + L_u.comp L_d = q • L_d + 0 := by rw [add_zero, h2]
    exact add_left_cancel this
  have h3 : (L_d + L_u).comp L_u = (q • LinearMap.id).comp L_u := by rw [hsum]
  have hu2 : L_u.comp L_u = q • L_u := by
    rw [LinearMap.add_comp, hcomp, zero_add, LinearMap.smul_comp, LinearMap.id_comp] at h3
    exact h3
  exact ⟨hd2, hud, hu2⟩

/-- The two kernels are disjoint when q ≠ 0: ker L_down ⊓ ker L_up = ⊥. -/
theorem hodge_ker_disjoint (q : K) (hq : q ≠ 0) (L_d L_u : V →ₗ[K] V)
    (hsum : L_d + L_u = q • LinearMap.id) :
    Disjoint (LinearMap.ker L_d) (LinearMap.ker L_u) := by
  rw [Submodule.disjoint_def]
  intro x hxd hxu
  rw [LinearMap.mem_ker] at hxd hxu
  have hsum_x : (L_d + L_u) x = (q • (LinearMap.id : V →ₗ[K] V)) x := by rw [hsum]
  have hzero_x : (L_d + L_u) x = 0 := by
    simp only [LinearMap.add_apply, hxd, hxu, add_zero]
  have hq_x : q • x = 0 := by
    simpa only [LinearMap.smul_apply, LinearMap.id_apply, hzero_x] using hsum_x.symm
  calc
    x = q⁻¹ • (q • x) := by rw [inv_smul_smul₀ hq]
    _ = q⁻¹ • (0 : V) := by rw [hq_x]
    _ = 0 := smul_zero (q⁻¹ : K)

/-- Every vector decomposes into a down-harmonic and an up-harmonic component:
v = q⁻¹ • L_up v + q⁻¹ • L_down v. -/
theorem hodge_vector_decomposition (q : K) (hq : q ≠ 0) (L_d L_u : V →ₗ[K] V)
    (hsum : L_d + L_u = q • LinearMap.id)
    (hcomp : L_d.comp L_u = 0) (v : V) :
    v = q⁻¹ • (L_u v) + q⁻¹ • (L_d v) ∧
    q⁻¹ • (L_u v) ∈ LinearMap.ker L_d ∧
    q⁻¹ • (L_d v) ∈ LinearMap.ker L_u := by
  have rel := hodge_algebra_relations q L_d L_u hsum hcomp
  have hsum_v : (L_d + L_u) v = q • v := by
    have : (L_d + L_u) v = (q • (LinearMap.id : V →ₗ[K] V)) v := by rw [hsum]
    simpa using this
  have hsplit : v = q⁻¹ • (L_u v) + q⁻¹ • (L_d v) := by
    calc
      v = q⁻¹ • (q • v) := by rw [inv_smul_smul₀ hq]
      _ = q⁻¹ • ((L_d + L_u) v) := by rw [hsum_v]
      _ = q⁻¹ • (L_d v + L_u v) := by rw [LinearMap.add_apply]
      _ = q⁻¹ • (L_u v) + q⁻¹ • (L_d v) := by rw [smul_add, add_comm]
  have hker_d : q⁻¹ • (L_u v) ∈ LinearMap.ker L_d := by
    rw [LinearMap.mem_ker, LinearMap.map_smul]
    have : L_d (L_u v) = (L_d.comp L_u) v := rfl
    rw [this, hcomp, LinearMap.zero_apply, smul_zero (q⁻¹ : K)]
  have hker_u : q⁻¹ • (L_d v) ∈ LinearMap.ker L_u := by
    rw [LinearMap.mem_ker, LinearMap.map_smul]
    have : L_u (L_d v) = (L_u.comp L_d) v := rfl
    rw [this, rel.2.1, LinearMap.zero_apply, smul_zero (q⁻¹ : K)]
  exact ⟨hsplit, hker_d, hker_u⟩

/-- Under the sum and composition relations with `q ≠ 0`, the two Hodge kernels
are complementary. Identifying these maps with a plaquette fibre is separate. -/
theorem hodge_decomposition (q : K) (hq : q ≠ 0) (L_d L_u : V →ₗ[K] V)
    (hsum : L_d + L_u = q • LinearMap.id)
    (hcomp : L_d.comp L_u = 0) :
    IsCompl (LinearMap.ker L_d) (LinearMap.ker L_u) := by
  refine ⟨hodge_ker_disjoint q hq L_d L_u hsum, codisjoint_iff.mpr ?_⟩
  rw [Submodule.eq_top_iff']
  intro v
  have dec := hodge_vector_decomposition q hq L_d L_u hsum hcomp v
  rw [dec.1]
  exact Submodule.add_mem_sup dec.2.1 dec.2.2

end HodgeAlgebra

section HomologicalProtection

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- The operator S = L_down - 4 I on the plaquette fibre. -/
def hodgeS (L_d : V →ₗ[K] V) : V →ₗ[K] V :=
  L_d - (4 : K) • LinearMap.id

/-- Homological protection: L_down ψ = 0 implies L_up ψ = q • ψ. -/
theorem carrier_homological_protection (q : K) (L_d L_u : V →ₗ[K] V)
    (hsum : L_d + L_u = q • LinearMap.id) (ψ : V) (hψ : L_d ψ = 0) :
    L_u ψ = q • ψ := by
  have h : (L_d + L_u) ψ = (q • (LinearMap.id : V →ₗ[K] V)) ψ := by rw [hsum]
  have hleft : (L_d + L_u) ψ = L_u ψ := by
    simp only [LinearMap.add_apply, hψ, zero_add]
  have hright : (q • (LinearMap.id : V →ₗ[K] V)) ψ = q • ψ := by
    simp only [LinearMap.smul_apply, LinearMap.id_apply]
  rw [← hleft, ← hright, h]

/-- The operator S = L_down - 4 I acts scalarly on the carrier: S ψ = -4 ψ. -/
theorem carrier_s_eigenvalue (L_d : V →ₗ[K] V) (ψ : V) (hψ : L_d ψ = 0) :
    hodgeS L_d ψ = (-4 : K) • ψ := by
  simp only [hodgeS, LinearMap.sub_apply, hψ, zero_sub, LinearMap.smul_apply,
    LinearMap.id_apply, neg_smul]

/-- Any linear map `Q` annihilating the carrier also annihilates the images of
the carrier under the two Hodge maps and `S`. No projector hypothesis is needed. -/
theorem feshbach_hodge_no_coupling (q : K) (L_d L_u Q : V →ₗ[K] V)
    (hsum : L_d + L_u = q • LinearMap.id) (ψ : V) (hψ : L_d ψ = 0) (hQ : Q ψ = 0) :
    Q (L_d ψ) = 0 ∧
    Q (L_u ψ) = 0 ∧
    Q (hodgeS L_d ψ) = 0 := by
  have hup := carrier_homological_protection q L_d L_u hsum ψ hψ
  have hs := carrier_s_eigenvalue L_d ψ hψ
  refine ⟨by rw [hψ, LinearMap.map_zero], ?_, ?_⟩
  · rw [hup, LinearMap.map_smul, hQ, smul_zero]
  · rw [hs, LinearMap.map_smul, hQ, smul_zero]

/-- For any operator R, if Q maps into ker L_up, then the R-excitation
φ = Q (R ψ) lies in ker L_up: L_up φ = 0. -/
theorem r_excitation_in_ker_up (L_u Q R : V →ₗ[K] V)
    (hQ_ker : ∀ v, L_u (Q v) = 0) (ψ : V) :
    L_u (Q (R ψ)) = 0 :=
  hQ_ker (R ψ)

end HomologicalProtection

section CarrierOrthogonality

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- With `q = ⟨ψ, ψ⟩`, the unnormalized rank-one Laplacian has carrier
eigenvalue `q`. -/
theorem rank_one_laplacian_carrier_eigenvalue (q : ℝ) (ψ : E)
    (hψ_norm : inner ℝ ψ ψ = q) :
    (inner ℝ ψ ψ) • ψ = q • ψ := by
  rw [hψ_norm]

/-- Dividing the rank-one Laplacian by nonzero `q` gives a map fixing `ψ`. -/
theorem normalized_carrier_projection_fixes_carrier (q : ℝ) (hq : q ≠ 0) (ψ : E)
    (hψ_norm : inner ℝ ψ ψ = q) :
    ((inner ℝ ψ ψ) / q) • ψ = ψ := by
  rw [hψ_norm, div_self hq, one_smul]

/-- Carrier orthogonality: the Feshbach excitation φ = Q R ψ = R ψ - (⟨ψ, R ψ⟩ / q) ψ
is strictly orthogonal to the carrier ψ: ⟨ψ, φ⟩ = 0. -/
theorem r_excitation_orthogonal (q : ℝ) (hq : q ≠ 0) (ψ : E) (hψ_norm : inner ℝ ψ ψ = q)
    (R : E →L[ℝ] E) :
    inner ℝ ψ (R ψ - (inner ℝ ψ (R ψ) / q) • ψ) = 0 := by
  rw [inner_sub_right, inner_smul_right, hψ_norm, div_mul_cancel₀ (inner ℝ ψ (R ψ)) hq, sub_self]

/-- The unnormalized rank-one Laplacian `L_up = |ψ⟩⟨ψ|` annihilates the
orthogonal excitation. The factor `1 / q` belongs to the carrier projector,
not to `L_up`; consequently this is the actual Laplacian normalization. -/
theorem r_excitation_up_harmonic (q : ℝ) (hq : q ≠ 0) (ψ : E) (hψ_norm : inner ℝ ψ ψ = q)
    (R : E →L[ℝ] E) :
    (inner ℝ ψ (R ψ - (inner ℝ ψ (R ψ) / q) • ψ)) • ψ = (0 : E) := by
  rw [r_excitation_orthogonal q hq ψ hψ_norm R, zero_smul]

/-- The normalized carrier projector `P = |ψ⟩⟨ψ| / q` also annihilates the
orthogonal excitation. This is stated separately from the Laplacian identity. -/
theorem r_excitation_carrier_projection_zero (q : ℝ) (hq : q ≠ 0) (ψ : E)
    (hψ_norm : inner ℝ ψ ψ = q) (R : E →L[ℝ] E) :
    ((inner ℝ ψ (R ψ - (inner ℝ ψ (R ψ) / q) • ψ)) / q) • ψ = (0 : E) := by
  rw [r_excitation_orthogonal q hq ψ hψ_norm R, zero_div, zero_smul]

end CarrierOrthogonality

section RankOneOperator

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- A rank-one middle map factors the actual vector-valued operator product. -/
theorem rank_one_rur_vector_factorization (ψ : V) (ell : V →ₗ[K] K)
    (R U : V →ₗ[K] V) (hU : ∀ v, U v = (ell v) • ψ) :
    R (U (R ψ)) = (ell (R ψ)) • R ψ := by
  rw [hU, LinearMap.map_smul]

/-- Actual operator factorization: when `U v = ell(v) ψ`, the carrier
functional of `R U R ψ` equals `ell(R ψ)^2`. No prescribed scalar carrier
polynomial or finite-word predicate is substituted for the operator product. -/
theorem rank_one_rur_carrier_factorization (ψ : V) (ell : V →ₗ[K] K)
    (R U : V →ₗ[K] V) (hU : ∀ v, U v = (ell v) • ψ) :
    ell (R (U (R ψ))) = (ell (R ψ)) ^ 2 := by
  rw [rank_one_rur_vector_factorization ψ ell R U hU, LinearMap.map_smul]
  simp only [smul_eq_mul, pow_two]

/-- With `ell(ψ) = q` and the unnormalized rank-one map `U v = ell(v) ψ`,
the actual `R U R` operator word has zero denominator-cleared carrier defect.
This identity does not require division and therefore also holds at `q = 0`. -/
theorem rank_one_rur_cleared_defect_zero (q : K) (ψ : V) (ell : V →ₗ[K] K)
    (hψ : ell ψ = q) (R U : V →ₗ[K] V) (hU : ∀ v, U v = (ell v) • ψ) :
    q ^ 2 * ell (R (U (R ψ))) - ell (R ψ) * ell (U ψ) * ell (R ψ) = 0 := by
  rw [rank_one_rur_carrier_factorization ψ ell R U hU, hU, LinearMap.map_smul, hψ]
  simp only [smul_eq_mul]
  ring

end RankOneOperator

section WordCalculus

/-- The three generators of the plaquette Hodge-Feshbach algebra. -/
inductive Gen | S | U | R deriving DecidableEq, Repr

abbrev Word := List Gen

/-- All words of length 1 in (S, U, R). -/
def words1 : List Word := [[Gen.S], [Gen.U], [Gen.R]]

/-- All words of length 2 in (S, U, R). -/
def words2 : List Word :=
  [[Gen.S, Gen.S], [Gen.S, Gen.U], [Gen.S, Gen.R],
   [Gen.U, Gen.S], [Gen.U, Gen.U], [Gen.U, Gen.R],
   [Gen.R, Gen.S], [Gen.R, Gen.U], [Gen.R, Gen.R]]

/-- All words of length 3 in (S, U, R). -/
def words3 : List Word :=
  [-- S **
   [Gen.S, Gen.S, Gen.S], [Gen.S, Gen.S, Gen.U], [Gen.S, Gen.S, Gen.R],
   [Gen.S, Gen.U, Gen.S], [Gen.S, Gen.U, Gen.U], [Gen.S, Gen.U, Gen.R],
   [Gen.S, Gen.R, Gen.S], [Gen.S, Gen.R, Gen.U], [Gen.S, Gen.R, Gen.R],
   -- U **
   [Gen.U, Gen.S, Gen.S], [Gen.U, Gen.S, Gen.U], [Gen.U, Gen.S, Gen.R],
   [Gen.U, Gen.U, Gen.S], [Gen.U, Gen.U, Gen.U], [Gen.U, Gen.U, Gen.R],
   [Gen.U, Gen.R, Gen.S], [Gen.U, Gen.R, Gen.U], [Gen.U, Gen.R, Gen.R],
   -- R **
   [Gen.R, Gen.S, Gen.S], [Gen.R, Gen.S, Gen.U], [Gen.R, Gen.S, Gen.R],
   [Gen.R, Gen.U, Gen.S], [Gen.R, Gen.U, Gen.U], [Gen.R, Gen.U, Gen.R],
   [Gen.R, Gen.R, Gen.S], [Gen.R, Gen.R, Gen.U], [Gen.R, Gen.R, Gen.R]]

/-- The 39 words of length at most three in (S, U, R). -/
def allWords : List Word := words1 ++ words2 ++ words3

/-- The explicitly listed nonempty words of lengths one through three number 39. -/
theorem hodge_feshbach_words_count : allWords.length = 39 := by rfl

/-- Lookahead predicate: does the remaining list contain an R before any U? -/
def lookaheadRNoU : List Gen → Bool
  | [] => false
  | Gen.U :: _ => false
  | Gen.R :: _ => true
  | _ :: rest => lookaheadRNoU rest

/-- Syntactic filter: does the word contain two R letters with no U between them?
Its correspondence with a nonzero operator defect is not proved here. -/
def hasTwoRNoU : List Gen → Bool
  | [] => false
  | Gen.R :: rest => lookaheadRNoU rest || hasTwoRNoU rest
  | _ :: rest => hasTwoRNoU rest

/-- Words in the explicit list satisfying the syntactic two-R/no-U filter. -/
def twoRNoUWords : List Word := allWords.filter hasTwoRNoU

/-- Exactly seven listed words satisfy the syntactic two-R/no-U filter. -/
theorem two_r_no_u_words_count : twoRNoUWords.length = 7 := by rfl

/-- Enumeration of the seven filtered words; no operator defect is evaluated. -/
theorem two_r_no_u_words_enum :
    twoRNoUWords = [
      [Gen.R, Gen.R],
      [Gen.S, Gen.R, Gen.R],
      [Gen.U, Gen.R, Gen.R],
      [Gen.R, Gen.S, Gen.R],
      [Gen.R, Gen.R, Gen.S],
      [Gen.R, Gen.R, Gen.U],
      [Gen.R, Gen.R, Gen.R]
    ] := by rfl

/-- RUR fails the syntactic filter. Operator factorization is proved separately
by `rank_one_rur_carrier_factorization` under its rank-one hypothesis. -/
theorem rur_two_r_no_u_false : hasTwoRNoU [Gen.R, Gen.U, Gen.R] = false := by rfl

/-- Scalar expression suggested by the source's one-R carrier formula. This
definition alone does not identify it with an evaluated word; natural subtraction
in the exponent is relevant outside the intended `nR ≤ 1` regime. -/
def oneRCarrierPolynomial (nS nU nR : ℕ) (q e2 : ℚ) : ℚ :=
  (-4 : ℚ) ^ nS * (-2 : ℚ) ^ nR * q ^ (nU + 1 - nR) * e2 ^ nR

/-- The scalar polynomial `q e2 + 3 e3`; its equality to `σ(RR)` is a
separate operator-evaluation statement. -/
def rrCarrierPolynomial (q e2 e3 : ℚ) : ℚ := q * e2 + 3 * e3

/-- Removing `q e2` from the defined RR polynomial leaves `3 e3`.
This scalar identity does not establish the carrier-symbol realization. -/
theorem rr_carrier_polynomial_remainder (q e2 e3 : ℚ) :
    rrCarrierPolynomial q e2 e3 - q * e2 = 3 * e3 := by
  unfold rrCarrierPolynomial; ring

/-- The scalar polynomial `4 e2^2`, without an operator-symbol identification. -/
def rurCarrierPolynomial (e2 : ℚ) : ℚ := 4 * e2 ^ 2

/-- The substituted polynomials satisfy a denominator-cleared identity.
Their identification with the source's actual symbols is not part of this lemma. -/
theorem rur_carrier_polynomial_cleared_identity (q e2 : ℚ) :
    q ^ 2 * rurCarrierPolynomial e2 - (-2 * e2) * (q ^ 2) * (-2 * e2) = 0 := by
  unfold rurCarrierPolynomial; ring

/-- The scalar one-R expression at counts `(0, 1, 1)` simplifies to `-2 q e2`.
This does not evaluate the `UR` or `RU` operator words. -/
theorem ur_carrier_polynomial_value (q e2 : ℚ) :
    oneRCarrierPolynomial 0 1 1 q e2 = -2 * q * e2 := by
  unfold oneRCarrierPolynomial; norm_num

end WordCalculus

section GeneralGeometry

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- Letters of the Hodge algebra. -/
inductive HodgeGen | Down | Up deriving DecidableEq, Repr

/-- Application of a Hodge word to a vector. -/
def applyHodgeWord (L_d L_u : V →ₗ[K] V) : List HodgeGen → V → V
  | [], v => v
  | HodgeGen.Down :: w, v => L_d (applyHodgeWord L_d L_u w v)
  | HodgeGen.Up :: w, v => L_u (applyHodgeWord L_d L_u w v)

/-- If `L_down ψ = 0` and `L_up ψ = eig • ψ`, every word in the two maps
acts as a scalar multiple on `ψ`. This conclusion needs neither a spanning-kernel
hypothesis nor an identification of the Feshbach complement with a Hodge summand. -/
theorem hodge_word_is_scalar (L_d L_u : V →ₗ[K] V) (eig : K) (ψ : V)
    (h_down : L_d ψ = 0) (h_up : L_u ψ = eig • ψ) :
    ∀ (w : List HodgeGen), ∃ (c : K), applyHodgeWord L_d L_u w ψ = c • ψ
  | [] => ⟨1, by simp [applyHodgeWord]⟩
  | HodgeGen.Down :: w => by
      rcases hodge_word_is_scalar L_d L_u eig ψ h_down h_up w with ⟨c, hc⟩
      use 0
      simp [applyHodgeWord, hc, h_down]
  | HodgeGen.Up :: w => by
      rcases hodge_word_is_scalar L_d L_u eig ψ h_down h_up w with ⟨c, hc⟩
      use eig * c
      simp [applyHodgeWord, hc, h_up, smul_smul, mul_comm]

end GeneralGeometry

section UniversalCellularHodge

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The Feshbach complement projector Q = id - P where P v = (⟨ψ, v⟩ / λ) • ψ
annihilates the unnormalized rank-one Laplacian L_up v = ⟨ψ, v⟩ • ψ identically:
L_up ∘ Q = 0. -/
theorem feshbach_q_annihilates_l_up (lam : ℝ) (hlam : lam ≠ 0) (ψ : E)
    (hψ_norm : inner ℝ ψ ψ = lam) (v : E) :
    (inner ℝ ψ (v - (inner ℝ ψ v / lam) • ψ)) • ψ = (0 : E) := by
  rw [inner_sub_right, inner_smul_right, hψ_norm, div_mul_cancel₀ _ hlam, sub_self, zero_smul]

/-- Universal up-harmonicity: for any bounded linear operator R on the face space,
the Feshbach excursion φ = Q (R ψ) is identically up-harmonic: L_up φ = 0. -/
theorem cellular_excursion_up_harmonic (lam : ℝ) (hlam : lam ≠ 0) (ψ : E)
    (hψ_norm : inner ℝ ψ ψ = lam) (R : E →L[ℝ] E) :
    (inner ℝ ψ (R ψ - (inner ℝ ψ (R ψ) / lam) • ψ)) • ψ = (0 : E) := by
  exact feshbach_q_annihilates_l_up lam hlam ψ hψ_norm (R ψ)

/-- In Feshbach-Schur perturbation theory, the intermediate Q projection annihilates
any state that returns to the carrier line Im(P). -/
theorem feshbach_intermediate_return_annihilation (lam : ℝ) (hlam : lam ≠ 0) (ψ : E)
    (hψ_norm : inner ℝ ψ ψ = lam) (c : ℝ) :
    (c • ψ) - (inner ℝ ψ (c • ψ) / lam) • ψ = (0 : E) := by
  rw [inner_smul_right, hψ_norm, mul_div_cancel_right₀ c hlam, sub_self]

end UniversalCellularHodge

section TetrahedralDuality

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- Tetrahedral Hodge duality: on a 4-dimensional face space, if L_down = 4 • Q
and L_up = 4 • P where P + Q = id and P ∘ Q = 0, then L_down + L_up = 4 • id
and L_down ∘ L_up = 0. -/
theorem tetrahedral_hodge_duality (P Q L_d L_u : V →ₗ[K] V)
    (hPQ : P + Q = LinearMap.id)
    (hPcompQ : P.comp Q = 0)
    (hd : L_d = (4 : K) • Q)
    (hu : L_u = (4 : K) • P) :
    L_d + L_u = (4 : K) • LinearMap.id ∧
    L_d.comp L_u = 0 := by
  constructor
  · rw [hd, hu, ← smul_add, add_comm Q P, hPQ]
  · rw [hd, hu, LinearMap.comp_smul, LinearMap.smul_comp, smul_smul]
    have hQP : Q.comp P = 0 := by
      have h1 : (P + Q).comp P = LinearMap.id.comp P := by rw [hPQ]
      have h2 : P.comp P + Q.comp P = P := by
        rw [LinearMap.add_comp, LinearMap.id_comp] at h1; exact h1
      have hP2 : P.comp P = P := by
        have h3 : P.comp (P + Q) = P.comp LinearMap.id := by rw [hPQ]
        rw [LinearMap.comp_add, hPcompQ, add_zero, LinearMap.comp_id] at h3
        exact h3
      rw [hP2] at h2
      have : P + Q.comp P = P + 0 := by rw [add_zero, h2]
      exact add_left_cancel this
    rw [hQP, smul_zero]

/-- Traceless compression theorem: if an operator M on a 3-dimensional subspace
acts as a scalar multiple c • id (as guaranteed by Schur's Lemma for the 3
irrep of S_4), its traceless part vanishes identically: c • id - (Tr(c • id)/3) • id = 0. -/
theorem traceless_compression_vanishes (c : K) (h3 : (3 : K) ≠ 0) :
    c - (3 * c) / 3 = 0 := by
  rw [mul_comm 3 c, mul_div_cancel_right₀ c h3, sub_self]

end TetrahedralDuality

section ShiftedHodgePowers

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- The geometric polynomial coefficient, defined without division at q = 0. -/
def hodgePi (q : K) : ℕ → K
  | 0 => 0
  | n + 1 => (q - 4) ^ n - 4 * hodgePi q n

/-- The cleared geometric-sum identity holds even when q = 0. -/
theorem hodge_pi_cleared (q : K) (n : ℕ) :
    q * hodgePi q n = (q - 4) ^ n - (-4 : K) ^ n := by
  induction n with
  | zero => simp [hodgePi]
  | succ n ih =>
    simp only [hodgePi, pow_succ]
    rw [mul_sub, show q * (4 * hodgePi q n) = 4 * (q * hodgePi q n) by ring, ih]
    ring

/-- All powers of S = (q - 4) I - U reduce to I and U when U² = q U.
This is an operator identity, with no invertibility or q ≠ 0 premise. -/
theorem hodge_shifted_power (q : K) (U : Module.End K V)
    (hU : U * U = q • U) (n : ℕ) :
    ((q - 4) • (1 : Module.End K V) - U) ^ n =
      (q - 4) ^ n • (1 : Module.End K V) - hodgePi q n • U := by
  induction n with
  | zero => simp [hodgePi]
  | succ n ih =>
    rw [pow_succ, ih]
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one,
      hU, smul_smul, hodgePi, pow_succ]
    module

/-- Sandwiching the exact power identity gives the all-length R S^n R
 decomposition. Identifying its carrier symbols is a separate Laurent calculation. -/
theorem hodge_sandwiched_power (q : K) (U R : Module.End K V)
    (hU : U * U = q • U) (n : ℕ) :
    R * ((q - 4) • (1 : Module.End K V) - U) ^ n * R =
      (q - 4) ^ n • (R * R) - hodgePi q n • (R * U * R) := by
  rw [hodge_shifted_power q U hU n]
  simp only [mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc, mul_one]

end ShiftedHodgePowers

end Workhouse.HodgeFeshbach
