import Workhouse.AtomLemma
import Workhouse.FiberGap

/-!
# Carrier atom at the physical fiber gap (WORKHOUSE H0 audit, §5 ∘ §4)

Combines the folded-fiber atom lemma (`carrier_atom_of_perturbation`, §5) with the exact
`O(u⁴)` fiber gap (`fiber_gap`, §4): the carrier's spectral mass in the window is at least
`1 - (2ε/g(b))²` with `g(b) = (2861009/4219365150)·u⁴·sin²(π/b)` written out.

Since `g(b) ~ u⁴/b² → 0`, a uniform (clean) atom requires the block-induced mixing to
shrink faster than the gap, `ε_mix(b) = o(g(b)) = o(u⁴/b²)`.  `carrier_atom_clean_limit`
is the formal statement: `ε_mix(b)/g(b) → 0 ⟹` the atom lower bound `→ 1`.

Results
* `gapfun`                 — the §4 gap `g(b)` as a function.
* `gapfun_eq_dispersion`   — `g(b)` equals the physical `cos`-band dispersion gap (via §4).
* `carrier_atom_fiber_gap` — atom weight `≥ 1 - (2ε/g(b))²` with `g(b)` substituted.
* `carrier_atom_clean_limit` — `ε_mix(b)/g(b) → 0 ⟹` lower bound `→ 1` (the `o(u⁴/b²)` rule).

Status: builds against `leanprover/lean4:v4.34.0-rc1` + Mathlib (repo-pinned), no `sorry`;
depends only on `[propext, Classical.choice, Quot.sound]`.  External to the WORKHOUSE clone.
-/

open Finset Filter Topology

namespace Workhouse

/-- The §4 fiber isolation gap `g(b) = (2861009/4219365150)·u⁴·sin²(π/b)`. -/
noncomputable def gapfun (u b : ℝ) : ℝ :=
  (2861009 / 4219365150 : ℝ) * u ^ 4 * Real.sin (Real.pi / b) ^ 2

/-- `g(b)` is exactly the Γ-to-nearest-alias gap of the historical `O(u⁴)` `cos`-band
dispersion (this is `fiber_gap`, §4). -/
theorem gapfun_eq_dispersion (u b : ℝ) :
    gapfun u b
      = (-(2861009 / 8438730300 : ℝ) * u ^ 4 * Real.cos (2 * Real.pi / b))
        - (-(2861009 / 8438730300 : ℝ) * u ^ 4 * Real.cos 0) :=
  (fiber_gap u b).symm

/-- **Carrier atom at the physical gap.**  With the fiber gap fixed to its §4 value
`g(b) = gapfun u b`, a unit source on the `m₀`-eigenspace of `H₀`, `H = H₀ + V` with
`‖(H-H₀)ψ‖ ≤ ε`, has window mass at least `1 - (2ε/g(b))²`. -/
theorem carrier_atom_fiber_gap
    {n : ℕ} {F : Type*} [NormedAddCommGroup F] [InnerProductSpace ℂ F]
    (b : OrthonormalBasis (Fin n) ℂ F) (lam : Fin n → ℝ)
    (H H0 : F →ₗ[ℂ] F) (ψ : F) (m0 u blk eps : ℝ)
    (hgap : 0 < gapfun u blk) (hψ : ‖ψ‖ = 1)
    (hEig : ∀ i, H (b i) = (lam i : ℂ) • b i)
    (hCarrier : H0 ψ = (m0 : ℂ) • ψ)
    (hPert : ‖H ψ - H0 ψ‖ ≤ eps)
    (W : Finset (Fin n)) (hW : ∀ i, i ∈ W ↔ |lam i - m0| ≤ gapfun u blk / 2) :
    1 - (2 * eps / gapfun u blk) ^ 2 ≤ ∑ i ∈ W, ‖b.repr ψ i‖ ^ 2 :=
  carrier_atom_of_perturbation b lam H H0 ψ m0 (gapfun u blk) eps hgap hψ hEig hCarrier hPert W hW

/-- **The `o(u⁴/b²)` rule, formalized.**  If the block-induced mixing shrinks faster than
the gap (`ε_mix(k)/g(k) → 0`), the carrier-atom lower bound `1 - (2 ε_mix/g)²` tends to `1`
— a clean atom in the limit.  (With `g(k) ~ u⁴/k²` from §4, `ε_mix/g → 0` is exactly
`ε_mix = o(u⁴/k²)`.) -/
theorem carrier_atom_clean_limit (gseq epsseq : ℕ → ℝ)
    (h : Tendsto (fun k => epsseq k / gseq k) atTop (𝓝 0)) :
    Tendsto (fun k => 1 - (2 * epsseq k / gseq k) ^ 2) atTop (𝓝 1) := by
  have h2 : Tendsto (fun k => 2 * epsseq k / gseq k) atTop (𝓝 0) := by
    have := h.const_mul (2 : ℝ)
    simpa [mul_div_assoc] using this
  have h3 : Tendsto (fun k => (2 * epsseq k / gseq k) ^ 2) atTop (𝓝 0) := by
    have := h2.pow 2
    simpa using this
  have := h3.const_sub (1 : ℝ)
  simpa using this

end Workhouse
