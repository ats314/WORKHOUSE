import Mathlib

/-!
# Folded-fiber carrier-atom lemma (WORKHOUSE H0 free-carrier audit, §5)

The finite-dimensional core behind the carrier atom on the alias-folded `p = 0`
fiber.  A unit source supported on the carrier eigenspace of `H₀`, perturbed to
`H = H₀ + V` with `‖V‖ ≤ ε`, keeps at least `1 - (2ε/g)²` of its spectral mass
inside the window `[m₀ - g/2, m₀ + g/2]`, where `g` is the fiber isolation gap.

The proof is a spectral Chebyshev inequality — no Davis–Kahan / sin-θ machinery,
hence no operator-valued contour integrals.  For a source `ψ` on the carrier
eigenspace, `(H - m₀)ψ = Vψ`, so the spectral second moment `∑ (λᵢ - m₀)² |cᵢ|²`
equals `‖(H - m₀)ψ‖² = ‖Vψ‖² ≤ ε²`; a Chebyshev/Markov bound then confines the
mass to the window.  Combined with `g(b) ~ u⁴/b²` (audit §4), the uniform-atom
condition is `ε_mix(b) = o(u⁴/b²)`.

Results
* `window_weight_ge`            — spectral Chebyshev core (real weights).
* `norm_sq_eq_sum_repr`         — Parseval for an orthonormal basis.
* `spectral_second_moment`      — `∑ (λᵢ-m₀)²|cᵢ|² = ‖(H-m₀)ψ‖²`.
* `carrier_atom_weight`         — spectral form (unit source, second-moment bound).
* `carrier_atom_of_perturbation`— operator form (source on carrier, `‖(H-H₀)ψ‖ ≤ ε`).

Status: builds against `leanprover/lean4:v4.34.0-rc1` + Mathlib (repo-pinned rev),
no `sorry`; every result depends only on `[propext, Classical.choice, Quot.sound]`
(checked via `#print axioms`).  Provenance and the informal statement:
`WORKHOUSE_H0_FREE_CARRIER_ALIAS_COMPLETION_AUDIT_20260822.md`, §5 and §9.

Author: Alex (ats314).  Read-only session: external to the WORKHOUSE clone.
-/

open Finset
open scoped InnerProductSpace

namespace Workhouse

/-- **Spectral Chebyshev core.**  If nonnegative spectral weights `w` with total
mass `1` obey the second-moment bound `∑ (λᵢ - m₀)² wᵢ ≤ ε²`, then the mass inside
the window `W = {i : |λᵢ - m₀| ≤ g/2}` is at least `1 - (2ε/g)²`. -/
theorem window_weight_ge
    {n : ℕ} (lam w : Fin n → ℝ) (m0 g eps : ℝ)
    (hg : 0 < g) (hw : ∀ i, 0 ≤ w i)
    (hsum : ∑ i, w i = 1)
    (hcheb : ∑ i, (lam i - m0) ^ 2 * w i ≤ eps ^ 2)
    (W : Finset (Fin n)) (hW : ∀ i, i ∈ W ↔ |lam i - m0| ≤ g / 2) :
    1 - (2 * eps / g) ^ 2 ≤ ∑ i ∈ W, w i := by
  -- total mass splits over `W` and its complement
  have hsplit : (∑ i ∈ W, w i) + ∑ i ∈ Wᶜ, w i = 1 := by
    rw [Finset.sum_add_sum_compl W w]; exact hsum
  -- each complement term is dominated by its second moment
  have hterm : ∀ i ∈ Wᶜ, (g / 2) ^ 2 * w i ≤ (lam i - m0) ^ 2 * w i := by
    intro i hi
    have hnotin : i ∉ W := Finset.mem_compl.mp hi
    have hgt : g / 2 < |lam i - m0| := not_le.mp (fun h => hnotin ((hW i).mpr h))
    have hsq : (g / 2) ^ 2 ≤ (lam i - m0) ^ 2 := by
      calc (g / 2) ^ 2 ≤ |lam i - m0| ^ 2 := by gcongr
        _ = (lam i - m0) ^ 2 := sq_abs _
    exact mul_le_mul_of_nonneg_right hsq (hw i)
  -- sum the pointwise bound over the complement
  have hcsum : (g / 2) ^ 2 * ∑ i ∈ Wᶜ, w i ≤ ∑ i ∈ Wᶜ, (lam i - m0) ^ 2 * w i := by
    rw [Finset.mul_sum]; exact Finset.sum_le_sum hterm
  -- complement second moment ≤ full second moment ≤ ε²
  have hfull : ∑ i ∈ Wᶜ, (lam i - m0) ^ 2 * w i ≤ ∑ i, (lam i - m0) ^ 2 * w i :=
    Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ _)
      (fun i _ _ => mul_nonneg (sq_nonneg _) (hw i))
  have hcmass : (g / 2) ^ 2 * ∑ i ∈ Wᶜ, w i ≤ eps ^ 2 :=
    le_trans hcsum (le_trans hfull hcheb)
  -- solve for the complement mass
  have hbound : ∑ i ∈ Wᶜ, w i ≤ (2 * eps / g) ^ 2 := by
    rw [div_pow, le_div_iff₀ (by positivity : (0 : ℝ) < g ^ 2)]
    nlinarith [hcmass]
  linarith [hsplit, hbound]

/-- **Carrier atom on the folded `p = 0` fiber (spectral form).**
`b` is an orthonormal eigenbasis with real eigenvalues `lam`; `ψ` is a unit source
with eigen-coefficients `b.repr ψ`.  If the spectral second moment about `m₀` is at
most `ε²` (this equals `‖(H - m₀)ψ‖²`; for a source on the carrier eigenspace of `H₀`
and `H = H₀ + V`, it is `‖Vψ‖² ≤ ε²`), then the spectral mass of `ψ` inside the window
`|λ - m₀| ≤ g/2` is at least `1 - (2ε/g)²`. -/
theorem carrier_atom_weight
    {n : ℕ} {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    (b : OrthonormalBasis (Fin n) ℂ E) (lam : Fin n → ℝ) (ψ : E)
    (m0 g eps : ℝ) (hg : 0 < g) (hψ : ‖ψ‖ = 1)
    (hcheb : ∑ i, (lam i - m0) ^ 2 * ‖b.repr ψ i‖ ^ 2 ≤ eps ^ 2)
    (W : Finset (Fin n)) (hW : ∀ i, i ∈ W ↔ |lam i - m0| ≤ g / 2) :
    1 - (2 * eps / g) ^ 2 ≤ ∑ i ∈ W, ‖b.repr ψ i‖ ^ 2 := by
  -- Parseval: the eigen-coefficients of a unit vector have total mass 1
  have parseval : ∑ i, ‖b.repr ψ i‖ ^ 2 = 1 := by
    have h2 : ‖b.repr ψ‖ ^ 2 = ∑ i, ‖b.repr ψ i‖ ^ 2 := by
      rw [EuclideanSpace.norm_eq,
        Real.sq_sqrt (Finset.sum_nonneg (fun i _ => by positivity))]
    rw [← h2, b.repr.norm_map ψ, hψ]; norm_num
  exact window_weight_ge lam (fun i => ‖b.repr ψ i‖ ^ 2) m0 g eps hg
    (fun i => sq_nonneg _) parseval hcheb W hW

/-- Parseval for an orthonormal basis: `‖x‖² = ∑ i, ‖(b.repr x) i‖²`. -/
theorem norm_sq_eq_sum_repr
    {n : ℕ} {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    (b : OrthonormalBasis (Fin n) ℂ E) (x : E) :
    ‖x‖ ^ 2 = ∑ i, ‖b.repr x i‖ ^ 2 := by
  have h1 : ‖x‖ = Real.sqrt (∑ i, ‖b.repr x i‖ ^ 2) := by
    rw [← b.repr.norm_map x, EuclideanSpace.norm_eq]
  rw [h1, Real.sq_sqrt (Finset.sum_nonneg (fun i _ => by positivity))]

/-- The spectral second moment about `m₀` equals `‖(H - m₀)ψ‖²`, when `b, lam` are an
eigenbasis/eigenvalues of `H`. -/
theorem spectral_second_moment
    {n : ℕ} {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    (b : OrthonormalBasis (Fin n) ℂ E) (lam : Fin n → ℝ)
    (H : E →ₗ[ℂ] E) (ψ : E) (m0 : ℝ)
    (hEig : ∀ i, H (b i) = (lam i : ℂ) • b i) :
    ∑ i, (lam i - m0) ^ 2 * ‖b.repr ψ i‖ ^ 2 = ‖H ψ - (m0 : ℂ) • ψ‖ ^ 2 := by
  -- coordinate of the residual: (repr of Hψ - m₀ψ)ᵢ = (λᵢ - m₀)·cᵢ
  have hrepr : ∀ i, b.repr (H ψ - (m0 : ℂ) • ψ) i = ((lam i : ℂ) - m0) * b.repr ψ i := by
    intro i
    have hHinner : ⟪b i, H ψ⟫_ℂ = (lam i : ℂ) * b.repr ψ i := by
      have e1 : H ψ = ∑ j, (b.repr ψ j) • ((lam j : ℂ) • b j) := by
        conv_lhs => rw [← b.sum_repr ψ]
        rw [map_sum]
        exact Finset.sum_congr rfl (fun j _ => by rw [map_smul, hEig])
      rw [e1, inner_sum, Finset.sum_eq_single i]
      · have h1 : (⟪b i, b i⟫_ℂ) = 1 := by
          rw [orthonormal_iff_ite.mp b.orthonormal i i]; simp
        rw [inner_smul_right, inner_smul_right, h1, b.repr_apply_apply]; ring
      · intro j _ hji
        have h0 : (⟪b i, b j⟫_ℂ) = 0 := by
          rw [orthonormal_iff_ite.mp b.orthonormal i j]
          exact ite_eq_right_iff.mpr (fun h => absurd h.symm hji)
        rw [inner_smul_right, inner_smul_right, h0, mul_zero, mul_zero]
      · intro h; exact absurd (Finset.mem_univ i) h
    rw [b.repr_apply_apply, inner_sub_right, inner_smul_right, hHinner, b.repr_apply_apply]
    ring
  rw [norm_sq_eq_sum_repr b (H ψ - (m0 : ℂ) • ψ)]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [hrepr i, norm_mul, mul_pow]
  congr 1
  rw [← Complex.ofReal_sub, Complex.norm_real, Real.norm_eq_abs, sq_abs]

/-- **Carrier atom on the folded `p = 0` fiber (operator form).**
`H` is self-adjoint with orthonormal eigenbasis `b` and real eigenvalues `lam`; `ψ`
is a unit source in the `m₀`-eigenspace of `H₀`, and `H = H₀ + V` with `‖(H-H₀)ψ‖ ≤ ε`
(e.g. `‖V‖ ≤ ε`).  Then the spectral mass of `ψ` for `H` inside the window
`|λ - m₀| ≤ g/2` is at least `1 - (2ε/g)²`.  This is §5 of the H0 free-carrier audit. -/
theorem carrier_atom_of_perturbation
    {n : ℕ} {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    (b : OrthonormalBasis (Fin n) ℂ E) (lam : Fin n → ℝ)
    (H H0 : E →ₗ[ℂ] E) (ψ : E) (m0 g eps : ℝ)
    (hg : 0 < g) (hψ : ‖ψ‖ = 1)
    (hEig : ∀ i, H (b i) = (lam i : ℂ) • b i)
    (hCarrier : H0 ψ = (m0 : ℂ) • ψ)
    (hPert : ‖H ψ - H0 ψ‖ ≤ eps)
    (W : Finset (Fin n)) (hW : ∀ i, i ∈ W ↔ |lam i - m0| ≤ g / 2) :
    1 - (2 * eps / g) ^ 2 ≤ ∑ i ∈ W, ‖b.repr ψ i‖ ^ 2 := by
  refine carrier_atom_weight b lam ψ m0 g eps hg hψ ?_ W hW
  rw [spectral_second_moment b lam H ψ m0 hEig, ← hCarrier]
  nlinarith [hPert, norm_nonneg (H ψ - H0 ψ)]

end Workhouse
