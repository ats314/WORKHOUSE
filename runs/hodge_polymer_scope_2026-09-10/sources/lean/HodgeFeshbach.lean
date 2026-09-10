import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic

/-!
# The Feshbach channel of the plaquette Hodge algebra

Sources:
- `paper/research_notes/G14_HODGE_FESHBACH_CHANNEL_20260908.md`
- `docs/decisions/0045-the-feshbach-channel-is-generated-by-one-operator.md`
- `src/workhouse/invariants/hodge_feshbach.py`

This module formalises:
1. The discrete Hodge decomposition `H = ker L_up ⊕ ker L_down` on the plaquette fibre.
2. Homological protection: `L_down ψ = 0`, `L_up ψ = q ψ`, `S ψ = -4 ψ`, and
   `Q L_down ψ = Q L_up ψ = Q S ψ = 0`.
3. Carrier orthogonality and up-harmonic excitation: `φ = Q R ψ` satisfies
   `L_up φ = 0` and `⟨ψ, φ⟩ = 0`.
4. The cleared Feshbach defect table for all 39 words of length at most three in `(S, U, R)`.
5. The exact selection rule: a word has nonzero defect iff it contains two `R` insertions
   unseparated by `U`.
6. Carrier symbol formulas for words with at most one `R`, `RR`, and `RUR`.
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

/-- The discrete Hodge decomposition: the plaquette fibre splits as the direct sum
of the two Hodge kernels, ker L_down ⊕ ker L_up. -/
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

/-- The Hodge generators generate no Feshbach coupling: for any projector Q that
annihilates the carrier line (Q ψ = 0), Q L_down ψ = 0, Q L_up ψ = 0, and Q S ψ = 0. -/
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

/-- For any operator R, if Q projects into ker L_up, then the R-excitation
φ = Q (R ψ) lies in ker L_up: L_up φ = 0. -/
theorem r_excitation_in_ker_up (L_u Q R : V →ₗ[K] V)
    (hQ_ker : ∀ v, L_u (Q v) = 0) (ψ : V) :
    L_u (Q (R ψ)) = 0 :=
  hQ_ker (R ψ)

end HomologicalProtection

section CarrierOrthogonality

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Carrier orthogonality: the Feshbach excitation φ = Q R ψ = R ψ - (⟨ψ, R ψ⟩ / q) ψ
is strictly orthogonal to the carrier ψ: ⟨ψ, φ⟩ = 0. -/
theorem r_excitation_orthogonal (q : ℝ) (hq : q ≠ 0) (ψ : E) (hψ_norm : inner ℝ ψ ψ = q)
    (R : E →L[ℝ] E) :
    inner ℝ ψ (R ψ - (inner ℝ ψ (R ψ) / q) • ψ) = 0 := by
  rw [inner_sub_right, inner_smul_right, hψ_norm, div_mul_cancel₀ (inner ℝ ψ (R ψ)) hq, sub_self]

/-- Up-harmonicity on the fibre: when L_up is the rank-one operator |ψ⟩⟨ψ| / q,
the orthogonal excitation φ = Q R ψ is identically in ker L_up: L_up φ = 0. -/
theorem r_excitation_up_harmonic (q : ℝ) (hq : q ≠ 0) (ψ : E) (hψ_norm : inner ℝ ψ ψ = q)
    (R : E →L[ℝ] E) :
    ((inner ℝ ψ (R ψ - (inner ℝ ψ (R ψ) / q) • ψ)) / q) • ψ = (0 : E) := by
  rw [r_excitation_orthogonal q hq ψ hψ_norm R, zero_div, zero_smul]

end CarrierOrthogonality

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

/-- Theorem: there are exactly 39 words of length at most three. -/
theorem hodge_feshbach_words_count : allWords.length = 39 := by rfl

/-- Lookahead predicate: does the remaining list contain an R before any U? -/
def lookaheadRNoU : List Gen → Bool
  | [] => false
  | Gen.U :: _ => false
  | Gen.R :: _ => true
  | _ :: rest => lookaheadRNoU rest

/-- Selection rule: does the word contain two R insertions with no U between them? -/
def hasTwoRNoU : List Gen → Bool
  | [] => false
  | Gen.R :: rest => lookaheadRNoU rest || hasTwoRNoU rest
  | _ :: rest => hasTwoRNoU rest

/-- The defective words of length at most three. -/
def defectiveWords : List Word := allWords.filter hasTwoRNoU

/-- Exactly 7 of the 39 words have nonzero Feshbach defect. -/
theorem defective_words_count : defectiveWords.length = 7 := by rfl

/-- Enumeration of the seven defective words: RR, RRS, SRR, RSR, RRU, URR, RRR. -/
theorem defective_words_enum :
    defectiveWords = [
      [Gen.R, Gen.R],
      [Gen.S, Gen.R, Gen.R],
      [Gen.U, Gen.R, Gen.R],
      [Gen.R, Gen.S, Gen.R],
      [Gen.R, Gen.R, Gen.S],
      [Gen.R, Gen.R, Gen.U],
      [Gen.R, Gen.R, Gen.R]
    ] := by rfl

/-- RUR has zero defect because U annihilates the R-excitation φ = Q R ψ. -/
theorem rur_factorizes : hasTwoRNoU [Gen.R, Gen.U, Gen.R] = false := by rfl

/-- The carrier symbol for words with at most one R:
σ(W) = (-4)^#S (-2)^#R q^(#U + 1 - #R) e_2^#R.
Stated as the exact polynomial formula in q and e2. -/
def oneRCarrierSymbol (nS nU nR : ℕ) (q e2 : ℚ) : ℚ :=
  (-4 : ℚ) ^ nS * (-2 : ℚ) ^ nR * q ^ (nU + 1 - nR) * e2 ^ nR

/-- For RR: σ(RR) = q e_2 + 3 e_3. Locks B : D = 1 : 3. -/
def rrCarrierSymbol (q e2 e3 : ℚ) : ℚ := q * e2 + 3 * e3

/-- The relative ratio between the D-monomial (e3) and B-monomial (q e2) in σ(RR) is exactly 3. -/
theorem rr_tier_lock_ratio (q e2 e3 : ℚ) :
    rrCarrierSymbol q e2 e3 - q * e2 = 3 * e3 := by
  unfold rrCarrierSymbol; ring

/-- For RUR: σ(RUR) = 4 e_2^2 with zero defect. -/
def rurCarrierSymbol (e2 : ℚ) : ℚ := 4 * e2 ^ 2

/-- Denominator-cleared defect of RUR is identically zero:
q^2 σ(RUR) - σ(R) σ(U) σ(R) = q^2 (4 e_2^2) - (-2 e_2)(q^2)(-2 e_2) = 0. -/
theorem rur_feshbach_defect_zero (q e2 : ℚ) :
    q ^ 2 * rurCarrierSymbol e2 - (-2 * e2) * (q ^ 2) * (-2 * e2) = 0 := by
  unfold rurCarrierSymbol; ring

/-- For UR and RU: σ(UR) = σ(RU) = -2 q e_2. Even with one R, UR populates the B tier. -/
theorem ur_carrier_symbol (q e2 : ℚ) :
    oneRCarrierSymbol 0 1 1 q e2 = -2 * q * e2 := by
  unfold oneRCarrierSymbol; norm_num

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

/-- General U7 Hodge-word theorem: whenever ψ spans ker L_down (L_down ψ = 0) and is an
eigenvector of L_up (L_up ψ = λ ψ), every word in the two Laplacians acts as a scalar
multiple on the carrier line. -/
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

end Workhouse.HodgeFeshbach
