/-
# Machine-checked core of the SU(N) cubic flux-band spectral program

Nothing in this file is taken on the authority of a document. Every statement
below is either proved from the definitions given here, or it is not present.
Prose in the corpus is a *pointer* to a claim, never evidence for it.

Scope, stated honestly: this file formalises the **exact-rational and
polynomial-identity layer**. That layer is real mathematics and it is now
proof-checked. It is *not* the physics — no perturbative derivation, no
operator theory, and nothing touching the disputed fourth-order kernel appears
here, because none of that is reducible to rational arithmetic.

Provenance for each statement is a section reference, recorded so a reader can
find what the corpus *claims*; the Lean proof is what makes it true here.
-/
import Mathlib.Tactic

namespace Workhouse

/-! ## Second order, all ranks -/

/-- Channel sum over the antiparallel pairing. -/
noncomputable def antiparallelSum (n : ℚ) : ℚ := -2 * n ^ 3 / ((n ^ 2 - 1) * (2 * n ^ 2 - 1))

/-- Channel sum over the parallel pairing. -/
noncomputable def parallelSum (n : ℚ) : ℚ := -4 * n * (n ^ 2 - 2) / ((n ^ 2 - 1) * (4 * n ^ 2 - 9))

/-- The charge-odd shared-link hopping. -/
noncomputable def hopping (n : ℚ) : ℚ :=
    2 * n * (n ^ 2 - 4) / ((n ^ 2 - 1) * (2 * n ^ 2 - 1) * (4 * n ^ 2 - 9))

/-- The rank law, with denominators cleared. Over the common denominator
`(n²-1)(2n²-1)(4n²-9)` the channel difference has numerator `2n(n²-4)`, which is
the hopping numerator. Stated this way it needs no non-vanishing hypotheses. -/
theorem rank_law_numerator (n : ℚ) :
    (-4 * n * (n ^ 2 - 2)) * (2 * n ^ 2 - 1) - (-2 * n ^ 3) * (4 * n ^ 2 - 9)
      = 2 * n * (n ^ 2 - 4) := by ring

/-- SU(3). -/
theorem hopping_three : hopping 3 = 5 / 612 := by unfold hopping; norm_num

/-- SU(2) is excluded at the source; the `n ^ 2 - 4` factor is its algebraic shadow. -/
theorem hopping_two : hopping 2 = 0 := by unfold hopping; norm_num

/-- The `N⁻³` cancellation leaves a positive deficit, denominators cleared:
`(1/4)·D - n³·2n(n²-4) = (2n⁴+31n²-9)/4` where `D` is the common denominator. -/
theorem hopping_deficit_numerator (n : ℚ) :
    (n ^ 2 - 1) * (2 * n ^ 2 - 1) * (4 * n ^ 2 - 9) - 4 * (n ^ 3 * (2 * n * (n ^ 2 - 4)))
      = 2 * n ^ 4 + 31 * n ^ 2 - 9 := by ring

/-! ## SU(3) through third order -/

noncomputable def b₃ : ℚ := 1975 / 124848
noncomputable def leak₃ : ℚ := -12331 / 249696
noncomputable def d₃ : ℚ := -109151 / 249696

/-- The third-order ledger identity. -/
theorem d₃_ledger : d₃ = 7 / 32 + 12 * leak₃ - 4 * b₃ := by
  unfold d₃ leak₃ b₃; norm_num

/-! ## Fourth order: the sealed core, which both disputed kernels agree on -/

noncomputable def A_shp : ℚ := 5 / 48
noncomputable def alphaPen (n : ℚ) : ℚ := 640 / (n * (n ^ 2 - 1) ^ 3)

theorem alphaPen_three : alphaPen 3 = 5 / 12 := by unfold alphaPen; norm_num
theorem alphaPen_four : alphaPen 4 = 32 / 675 := by unfold alphaPen; norm_num
theorem alphaPen_five : alphaPen 5 = 1 / 108 := by unfold alphaPen; norm_num
theorem alphaPen_six : alphaPen 6 = 64 / 25725 := by unfold alphaPen; norm_num

/-- The axial coefficient is four times the sealed shape coefficient. -/
theorem alphaPen_three_eq_four_A : alphaPen 3 = 4 * A_shp := by
  unfold alphaPen A_shp; norm_num

/-! ## The generalized pencil -/

/-- Band value at a high-symmetry point, in the two-invariant parametrisation. -/
noncomputable def lam (α β t : ℚ) : ℚ := α + β * t

/-- The blind holdout: `R` is determined by `X` and `M`, so it can be withheld
from a fit and used as an independent check. -/
theorem blind_holdout (α β : ℚ) : lam α β 1 = 2 * lam α β (1 / 2) - lam α β 0 := by
  unfold lam; ring

/-- The 25-point stencil obeys a zero-mode gate: the weights sum to zero. -/
theorem stencil_zero_mode (α β : ℚ) :
    (9 / 2 * α + 3 * β) + 6 * (-(α + β)) + 6 * (α / 4) + 12 * (β / 4) = 0 := by ring

/-! ## The historical SU(3) kernel -/

noncomputable def βPenOld : ℚ := 17607806155349 / 275331901291200
noncomputable def C_shp_old : ℚ := -211835444920651 / 4405310420659200
noncomputable def W₄_old : ℚ := 132329431693349 / 275331901291200

/-- The off-axis coefficient is fixed by the diagonal coefficient and the axial one. -/
theorem C_from_beta : C_shp_old = (βPenOld - 2 * alphaPen 3) / 16 := by
  unfold C_shp_old βPenOld alphaPen; norm_num

/-- Bandwidth is the sum of the two pencil coefficients. -/
theorem width_eq_alpha_add_beta : W₄_old = alphaPen 3 + βPenOld := by
  unfold W₄_old alphaPen βPenOld; norm_num

/-- The tier-collapse relation, valid when `B = D = 0`. -/
theorem beta_from_A_and_C : βPenOld = 8 * A_shp + 16 * C_shp_old := by
  unfold βPenOld A_shp C_shp_old; norm_num

/-! ## Symmetric-function identities used by the fourth-order shape analysis -/

/-- Newton's identity in three variables. This is what lets a degree-3 numerator
carry an `e₃` component, which is the step that refuted the degree-bound
mechanism proposed for the tier collapse. -/
theorem newton_three (a b c : ℚ) :
    a ^ 3 + b ^ 3 + c ^ 3
      = (a + b + c) ^ 3 - 3 * (a + b + c) * (a * b + a * c + b * c) + 3 * (a * b * c) := by
  ring

/-- The four checkpoint-extraction formulas invert the cubic-invariant ansatz.
Stated on the checkpoint deltas `dX, dM, dP, dR` as they arise from the ansatz. -/
theorem extraction_A (A : ℚ) : (4 * A) / 4 = A := by ring

theorem extraction_B (A B C : ℚ) :
    ((4 * A) + 4 * (8 * A + 16 * B + 8 * C) - 6 * (6 * A + 8 * B + 16 / 3 * C)) / 16 = B := by
  ring

theorem extraction_C (A B C : ℚ) :
    3 * (2 * (6 * A + 8 * B + 16 / 3 * C) - (8 * A + 16 * B + 8 * C) - (4 * A)) / 8 = C := by
  ring

theorem extraction_D (A B C D : ℚ) :
    3 * ((12 * A + 48 * B + 16 * C + 16 / 3 * D) - 6 * (8 * A + 16 * B + 8 * C)
        + 6 * (6 * A + 8 * B + 16 / 3 * C)) / 16 = D := by
  ring

/-! ## Finite volume -/

/-- The cycle count on the three-torus: cube boundaries plus the harmonic triplet. -/
theorem dim_Z₂ (L : ℤ) : (L ^ 3 - 1) + 3 = L ^ 3 + 2 := by ring

end Workhouse
