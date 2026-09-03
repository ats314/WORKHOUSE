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

/-! ## The charge-even band -/

/-- The charge-even characteristic polynomial, in the Gram variable `μ = λ + 4`,
with `aᵢ = 2 + 2 cos kᵢ` and `p = a + b + c`. The corpus records this sector's
range and its Γ expansion but no closed form; this one is derived in
`src/workhouse/even_sector.py` and checked there against the integer
characteristic polynomial of the finite `L = 3` and `L = 4` plaquette
adjacencies. -/
def evenCubic (m a b c : ℚ) : ℚ :=
  m ^ 3 - 2 * (a + b + c) * m ^ 2 + (a + b + c) ^ 2 * m - 4 * a * b * c

/-- Why the linear coefficient is `p²`. The three principal 2×2 minors of the
unsigned Gram matrix are `a·p`, `b·p` and `c·p`: each off-diagonal
modulus-squared (`bc`, `ac`, `ab`) cancels the cross term of its minor exactly,
and the three then sum to `p²`. This is the step that makes the cubic depend on
`a, b, c` only through `p` and `abc`. -/
theorem even_gram_minors (a b c : ℚ) :
    ((b + a) * (c + a) - b * c) + ((b + a) * (c + b) - a * c)
        + ((c + a) * (c + b) - a * b)
      = (a + b + c) ^ 2 := by ring

/-- The band floor. `μ = 0`, that is `λ = -4`, is a root exactly when `abc = 0`,
which is exactly the union of the three zone-boundary planes `kⱼ = π`. -/
theorem even_cubic_at_zero (a b c : ℚ) : evenCubic 0 a b c = -(4 * (a * b * c)) := by
  unfold evenCubic; ring

/-- The band ceiling, in the form that carries the bound: at `μ = 16` the cubic
is `16(16-p)² - 4abc`. Each `aᵢ ∈ [0,4]`, so `p ≤ 12` and `abc ≤ 64`, hence
`16(16-p)² ≥ 256 ≥ 4abc` and the value is nonnegative. -/
theorem even_cubic_at_sixteen (a b c : ℚ) :
    evenCubic 16 a b c = 16 * (16 - (a + b + c)) ^ 2 - 4 * (a * b * c) := by
  unfold evenCubic; ring

/-- Above `p` the cubic is strictly increasing, because its derivative factors
as `(3μ - p)(μ - p)`. With the previous lemma this is the upper-edge argument:
no root exceeds `16`, so `λ ≤ 12`. -/
theorem even_cubic_derivative_factors (m a b c : ℚ) :
    3 * m ^ 2 - 4 * (a + b + c) * m + (a + b + c) ^ 2
      = (3 * m - (a + b + c)) * (m - (a + b + c)) := by ring

/-! ## Symmetric-function identities used by the fourth-order shape analysis -/

/-- Newton's identity in three variables. This is what lets a degree-3 numerator
carry an `e₃` component, which is the step that refuted the degree-bound
mechanism proposed for the tier collapse. -/
theorem newton_three (a b c : ℚ) :
    a ^ 3 + b ^ 3 + c ^ 3
      = (a + b + c) ^ 3 - 3 * (a + b + c) * (a * b + a * c + b * c) + 3 * (a * b * c) := by
  ring

/-- The four checkpoint-extraction formulas invert the cubic-invariant ansatz.
Stated on the checkpoint deltas `dX, dM, dP, dR`, whose forms are proved from
the ansatz by `delta_X`, `delta_M`, `delta_P` and `delta_R` below. Together the
eight cover the T1 extraction check whole: these four the inversion, those four
the derivation of the deltas including the trigonometric step. -/
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

/-! ## The primitive cell-completion family (G5)

The enumeration that produces each signed count `S_r` — temporal orderings,
merge hypotheses, resolvent denominators — lives in `workhouse.cellular` at
T1. What is provable here is the rational-algebra layer: the law's two printed
forms agree, the counts produce the printed rows, and the rows take their
recorded SU(3) values. -/

/-- The primitive completion law in its Casimir form, at the target order
r = 2: one resolvent, so a single factor of `C_F = (n² − 1)/(2n)`. -/
noncomputable def cPrimTwo (S n : ℚ) : ℚ := S / (n ^ 2 * ((n ^ 2 - 1) / (2 * n)))

/-- The four printed rows of the family. -/
noncomputable def tetraCompletion (n : ℚ) : ℚ := -8 / (n * (n ^ 2 - 1))

noncomputable def prismCompletion (n : ℚ) : ℚ := 64 / (n * (n ^ 2 - 1) ^ 2)

noncomputable def cubeCompletion (n : ℚ) : ℚ := -160 / (n * (n ^ 2 - 1) ^ 3)

noncomputable def pentCompletion (n : ℚ) : ℚ := 1120 / (n * (n ^ 2 - 1) ^ 4)

/-- The law's two printed forms are one identity at the target order: the
Casimir form with count `S` is the `2^(r−1) S / (N(N²−1)^(r−1))` form. -/
theorem cPrimTwo_forms (S n : ℚ) (h0 : n ≠ 0) (h1 : n ^ 2 - 1 ≠ 0) :
    cPrimTwo S n = 2 * S / (n * (n ^ 2 - 1)) := by
  unfold cPrimTwo; field_simp

/-- The tetrahedral count `S₂ = −4` produces the asserted row `−8/(N(N²−1))`. -/
theorem tetra_from_count (n : ℚ) (h0 : n ≠ 0) (h1 : n ^ 2 - 1 ≠ 0) :
    cPrimTwo (-4) n = tetraCompletion n := by
  unfold tetraCompletion
  rw [cPrimTwo_forms (-4) n h0 h1]; ring

/-- The SU(3) tetrahedral value. -/
theorem tetraCompletion_three : tetraCompletion 3 = -1 / 3 := by
  unfold tetraCompletion; norm_num

/-- The SU(3) prism (square-sector) value. -/
theorem prismCompletion_three : prismCompletion 3 = 1 / 3 := by
  unfold prismCompletion; norm_num

/-- The SU(3) cube value is minus the sealed shape coefficient. -/
theorem cubeCompletion_three : cubeCompletion 3 = -A_shp := by
  unfold cubeCompletion A_shp; norm_num

/-- The SU(3) pentagonal (cap-sector) value. -/
theorem pentCompletion_three : pentCompletion 3 = 35 / 384 := by
  unfold pentCompletion; norm_num

/-- The axial law is −4 times the cube row, at every rank — the bridge between
the completion family and the sealed core's `alphaPen`. -/
theorem alphaPen_eq_neg_four_cube (n : ℚ) : alphaPen n = -4 * cubeCompletion n := by
  unfold alphaPen cubeCompletion; ring

/-! ## The checkpoint deltas, from the ansatz

The four `extraction_*` theorems above invert the cubic-invariant ansatz on the
deltas `dX, dM, dP, dR`, but they *assume* those deltas already have the forms
`4A`, `8A+16B+8C`, `6A+8B+16C/3`, `12A+48B+16C+16D/3`. Their doc comment says
so, and the gap was real: nothing machine-checked showed those forms follow
from the ansatz, so the T1 check `checkpoint values at X, M, P, R` had no T0
counterpart and the extraction theorems formalized only half a statement.

This section closes it, over `ℝ` rather than `ℚ` because the step is
trigonometric: the band variable is `a(k) = 4 sin²(k/2)`, and the checkpoints
are the momenta where it takes rational values.
-/

/-- The band variable. `a(k) = 4 sin²(k/2)`, the standard lattice dispersion. -/
noncomputable def bandVar (k : ℝ) : ℝ := 4 * Real.sin (k / 2) ^ 2

@[simp] theorem bandVar_zero : bandVar 0 = 0 := by
  unfold bandVar; simp

@[simp] theorem bandVar_pi : bandVar Real.pi = 4 := by
  unfold bandVar; rw [show Real.pi / 2 = Real.pi / 2 from rfl, Real.sin_pi_div_two]; norm_num

@[simp] theorem bandVar_pi_div_two : bandVar (Real.pi / 2) = 2 := by
  unfold bandVar
  rw [show Real.pi / 2 / 2 = Real.pi / 4 by ring, Real.sin_pi_div_four]
  rw [div_pow, Real.sq_sqrt (by norm_num : (2:ℝ) ≥ 0)]
  norm_num

/-- The cubic invariants of the three band variables. -/
noncomputable def qInv (a b c : ℝ) : ℝ := a + b + c
noncomputable def e2Inv (a b c : ℝ) : ℝ := a * b + a * c + b * c
noncomputable def e3Inv (a b c : ℝ) : ℝ := a * b * c

/-- The fourth-order cubic-invariant ansatz on the flat fiber:
`eps4 = c0 + A q + B e2 + C (4 e2 / q) + D (e3 / q)`. -/
noncomputable def eps4 (c0 A B C D a b c : ℝ) : ℝ :=
  c0 + A * qInv a b c + B * e2Inv a b c
    + C * (4 * e2Inv a b c / qInv a b c) + D * (e3Inv a b c / qInv a b c)

/-- `q` at the four high-symmetry points: `0, 4, 8, 12` at `Γ, X, M, R`. The
corpus figure plots this spectrum and asserts it; here it is derived. -/
theorem q_at_checkpoints :
    qInv (bandVar 0) (bandVar 0) (bandVar 0) = 0 ∧
    qInv (bandVar Real.pi) (bandVar 0) (bandVar 0) = 4 ∧
    qInv (bandVar Real.pi) (bandVar Real.pi) (bandVar 0) = 8 ∧
    qInv (bandVar Real.pi) (bandVar Real.pi) (bandVar Real.pi) = 12 := by
  unfold qInv; norm_num

/-- The checkpoint delta at `X = (π, 0, 0)`: `dX = 4A`. `X` is blind to `B`, `C`
and `D`, which is what makes it fix `A` alone. -/
theorem delta_X (c0 A B C D : ℝ) :
    eps4 c0 A B C D (bandVar Real.pi) (bandVar 0) (bandVar 0) - c0 = 4 * A := by
  unfold eps4 qInv e2Inv e3Inv; simp; ring

/-- The checkpoint delta at `M = (π, π, 0)`: `dM = 8A + 16B + 8C`. -/
theorem delta_M (c0 A B C D : ℝ) :
    eps4 c0 A B C D (bandVar Real.pi) (bandVar Real.pi) (bandVar 0) - c0
      = 8 * A + 16 * B + 8 * C := by
  unfold eps4 qInv e2Inv e3Inv; simp; ring

/-- The checkpoint delta at `P = (π, π/2, 0)`: `dP = 6A + 8B + 16C/3`. -/
theorem delta_P (c0 A B C D : ℝ) :
    eps4 c0 A B C D (bandVar Real.pi) (bandVar (Real.pi / 2)) (bandVar 0) - c0
      = 6 * A + 8 * B + 16 / 3 * C := by
  unfold eps4 qInv e2Inv e3Inv; simp; ring

/-- The checkpoint delta at `R = (π, π, π)`: `dR = 12A + 48B + 16C + 16D/3`.
`R` is the only checkpoint that sees `D`, because it is the only one where all
three band variables are nonzero and so `e3` does not vanish. -/
theorem delta_R (c0 A B C D : ℝ) :
    eps4 c0 A B C D (bandVar Real.pi) (bandVar Real.pi) (bandVar Real.pi) - c0
      = 12 * A + 48 * B + 16 * C + 16 / 3 * D := by
  unfold eps4 qInv e2Inv e3Inv; simp; ring

/-! ## Second order at every rank: the channel weights, the family sums, the charge-even hop

The manuscript derives four shared-link channel weights `w_ρ = −(d_ρ/N²)/(C_F + C_ρ/2)`
from the fusion table and sums them within the two orientation families. Everything
below is the rational algebra of that step: the closed forms of the four weights, the
family sums `A_N` and `B_N` (which the registry had as inputs and the T1 suite made
outputs), the weights summing to one per family, and the charge-even shared-link hop
`ℓ_N = A_N + B_N + 1/C_F`. Nothing here is the physics; the physics is the identification
of the weights with resolvent matrix elements, which lives in the paper's Theorem
(all-rank adjacent shared-link law). -/

/-- The fundamental Casimir, `C_F = (N² − 1)/(2N)`. -/
noncomputable def casimirF (n : ℚ) : ℚ := (n ^ 2 - 1) / (2 * n)

/-- Resolvent weight of a shared-link channel of dimension `d` and Casimir `c`:
`w = −(d/N²)/(C_F + c/2)`. -/
noncomputable def channelWeight (n d c : ℚ) : ℚ := -(d / n ^ 2) / (casimirF n + c / 2)

/-- The weight in cleared form: `w = −2d / (N(N² − 1 + Nc))`. -/
theorem channelWeight_eq (n d c : ℚ) (h0 : n ≠ 0) (hden : n ^ 2 - 1 + n * c ≠ 0) :
    channelWeight n d c = -(2 * d) / (n * (n ^ 2 - 1 + n * c)) := by
  unfold channelWeight casimirF
  have hden' : (n ^ 2 - 1) / (2 * n) + c / 2 = (n ^ 2 - 1 + n * c) / (2 * n) := by
    field_simp
  rw [hden']
  field_simp

/-- The singlet channel, `d = 1`, `C = 0`. -/
noncomputable def wSinglet (n : ℚ) : ℚ := channelWeight n 1 0
/-- The adjoint channel, `d = N² − 1`, `C = N`. -/
noncomputable def wAdjoint (n : ℚ) : ℚ := channelWeight n (n ^ 2 - 1) n
/-- The antisymmetric square, `d = N(N−1)/2`, `C = (N+1)(N−2)/N`. -/
noncomputable def wAntisym (n : ℚ) : ℚ :=
  channelWeight n (n * (n - 1) / 2) ((n + 1) * (n - 2) / n)
/-- The symmetric square, `d = N(N+1)/2`, `C = (N−1)(N+2)/N`. -/
noncomputable def wSym (n : ℚ) : ℚ :=
  channelWeight n (n * (n + 1) / 2) ((n - 1) * (n + 2) / n)

theorem wSinglet_closed (n : ℚ) (h0 : n ≠ 0) (h1 : n ^ 2 - 1 ≠ 0) :
    wSinglet n = -2 / (n * (n ^ 2 - 1)) := by
  unfold wSinglet
  rw [channelWeight_eq n 1 0 h0 (by simpa using h1)]
  ring

theorem wAdjoint_closed (n : ℚ) (h0 : n ≠ 0) (h2 : 2 * n ^ 2 - 1 ≠ 0) :
    wAdjoint n = -2 * (n ^ 2 - 1) / (n * (2 * n ^ 2 - 1)) := by
  unfold wAdjoint
  rw [channelWeight_eq n (n ^ 2 - 1) n h0 (by ring_nf; ring_nf at h2; exact h2)]
  ring_nf

theorem wAntisym_closed (n : ℚ) (h0 : n ≠ 0) (hp : n + 1 ≠ 0) (hm : 2 * n - 3 ≠ 0) :
    wAntisym n = -(n - 1) / ((n + 1) * (2 * n - 3)) := by
  unfold wAntisym
  have hc : n * ((n + 1) * (n - 2) / n) = (n + 1) * (n - 2) := by field_simp
  have hden : n ^ 2 - 1 + n * ((n + 1) * (n - 2) / n) ≠ 0 := by
    rw [hc]
    have : n ^ 2 - 1 + (n + 1) * (n - 2) = (n + 1) * (2 * n - 3) := by ring
    rw [this]; exact mul_ne_zero hp hm
  rw [channelWeight_eq n _ _ h0 hden, hc]
  have : n ^ 2 - 1 + (n + 1) * (n - 2) = (n + 1) * (2 * n - 3) := by ring
  rw [this]
  field_simp

theorem wSym_closed (n : ℚ) (h0 : n ≠ 0) (hm : n - 1 ≠ 0) (hp : 2 * n + 3 ≠ 0) :
    wSym n = -(n + 1) / ((n - 1) * (2 * n + 3)) := by
  unfold wSym
  have hc : n * ((n - 1) * (n + 2) / n) = (n - 1) * (n + 2) := by field_simp
  have hden : n ^ 2 - 1 + n * ((n - 1) * (n + 2) / n) ≠ 0 := by
    rw [hc]
    have : n ^ 2 - 1 + (n - 1) * (n + 2) = (n - 1) * (2 * n + 3) := by ring
    rw [this]; exact mul_ne_zero hm hp
  rw [channelWeight_eq n _ _ h0 hden, hc]
  have : n ^ 2 - 1 + (n - 1) * (n + 2) = (n - 1) * (2 * n + 3) := by ring
  rw [this]
  field_simp

/-- The mixed family `F ⊗ F̄ = 1 ⊕ Adj` sums to `A_N`. -/
theorem mixed_family_sum (n : ℚ) (h0 : n ≠ 0) (hm : n - 1 ≠ 0) (hp : n + 1 ≠ 0)
    (h2 : 2 * n ^ 2 - 1 ≠ 0) :
    wSinglet n + wAdjoint n = antiparallelSum n := by
  have h1 : n ^ 2 - 1 ≠ 0 := by
    have : n ^ 2 - 1 = (n - 1) * (n + 1) := by ring
    rw [this]; exact mul_ne_zero hm hp
  rw [wSinglet_closed n h0 h1, wAdjoint_closed n h0 h2]
  unfold antiparallelSum
  field_simp
  ring

/-- The like family `F ⊗ F = Λ²F ⊕ Sym²F` sums to `B_N`. -/
theorem like_family_sum (n : ℚ) (h0 : n ≠ 0) (hm : n - 1 ≠ 0) (hp : n + 1 ≠ 0)
    (ha : 2 * n - 3 ≠ 0) (hb : 2 * n + 3 ≠ 0) :
    wAntisym n + wSym n = parallelSum n := by
  rw [wAntisym_closed n h0 hp ha, wSym_closed n h0 hm hb]
  unfold parallelSum
  have hA : (n + 1) * (2 * n - 3) ≠ 0 := mul_ne_zero hp ha
  have hB : (n - 1) * (2 * n + 3) ≠ 0 := mul_ne_zero hm hb
  have hT : (n ^ 2 - 1) * (4 * n ^ 2 - 9) ≠ 0 := by
    have h1 : n ^ 2 - 1 = (n - 1) * (n + 1) := by ring
    have h9 : 4 * n ^ 2 - 9 = (2 * n - 3) * (2 * n + 3) := by ring
    rw [h1, h9]; exact mul_ne_zero (mul_ne_zero hm hp) (mul_ne_zero ha hb)
  rw [div_add_div _ _ hA hB, div_eq_div_iff (mul_ne_zero hA hB) hT]
  ring

/-- The resolvent gap of a shared-link channel: six nonshared half-links at `3C_F` plus the
fused link at `C_ρ/2`, against the external `2C_F`, leave `C_F + C_ρ/2`. -/
theorem channel_gap (cf c : ℚ) : (3 * cf + c / 2) - 2 * cf = cf + c / 2 := by ring

/-- The weights of each family sum to one: `(1 + (N²−1))/N² = 1` and
`(N(N−1)/2 + N(N+1)/2)/N² = 1`. -/
theorem family_weights_sum_to_one (n : ℚ) (h0 : n ≠ 0) :
    (1 + (n ^ 2 - 1)) / n ^ 2 = 1 ∧ (n * (n - 1) / 2 + n * (n + 1) / 2) / n ^ 2 = 1 := by
  constructor <;> field_simp <;> ring

/-- The charge-even shared-link hop, `ℓ_N = A_N + B_N + 1/C_F`, in closed form. -/
noncomputable def evenHop (n : ℚ) : ℚ :=
  -2 * n * (3 * n ^ 2 - 5) / ((n ^ 2 - 1) * (2 * n ^ 2 - 1) * (4 * n ^ 2 - 9))

/-- The vacuum-mediated route adds exactly `1/C_F = 2N/(N² − 1)` to the two family sums. -/
theorem evenHop_eq (n : ℚ) (h1 : n ^ 2 - 1 ≠ 0) (h2 : 2 * n ^ 2 - 1 ≠ 0)
    (h9 : 4 * n ^ 2 - 9 ≠ 0) :
    antiparallelSum n + parallelSum n + 2 * n / (n ^ 2 - 1) = evenHop n := by
  unfold antiparallelSum parallelSum evenHop
  have hA : (n ^ 2 - 1) * (2 * n ^ 2 - 1) ≠ 0 := mul_ne_zero h1 h2
  have hB : (n ^ 2 - 1) * (4 * n ^ 2 - 9) ≠ 0 := mul_ne_zero h1 h9
  have hT : (n ^ 2 - 1) * (2 * n ^ 2 - 1) * (4 * n ^ 2 - 9) ≠ 0 := mul_ne_zero hA h9
  rw [div_add_div _ _ hA hB, div_add_div _ _ (mul_ne_zero hA hB) h1,
    div_eq_div_iff (mul_ne_zero (mul_ne_zero hA hB) h1) hT]
  ring

theorem evenHop_three : evenHop 3 = -11 / 306 := by unfold evenHop; norm_num

/-- The shared-link-only sum at `N = 3` is the superseded `−481/612` of C13; the
vacuum route `3/4` is exactly what was omitted. -/
theorem evenHop_three_from_channels :
    antiparallelSum 3 + parallelSum 3 = -481 / 612 ∧ (-481 / 612 : ℚ) + 3 / 4 = -11 / 306 := by
  unfold antiparallelSum parallelSum; norm_num

/-- The charge-even hop never vanishes where the charge-odd one does: `ℓ_2 = −4/21`. -/
theorem evenHop_two : evenHop 2 = -4 / 21 := by unfold evenHop; norm_num

/-- The bandwidth ratio `16|ℓ_N| / (12 t_N) = 4(3N²−5)/(3(N²−4))`, denominators cleared:
the charge-even band is the wider one at every rank `N ≥ 3`. -/
theorem width_ratio_numerator (n : ℚ) :
    16 * (2 * n * (3 * n ^ 2 - 5)) * 3 * (n ^ 2 - 4)
      = 12 * (2 * n * (n ^ 2 - 4)) * (4 * (3 * n ^ 2 - 5)) := by ring

/-! ## The second-order scalar ledger at every rank

New in the revised manuscript. The on-site second-order scalar of the charge-odd
shell is `σ⁻_N + 1/C_F + 12 ℓ_N`, where `σ⁻_N` is the reduced same-face route; the flat
(carrier) scalar subtracts `4 t_N`. For `N ≥ 5` the same-face route is
`−N/((N−1)(N+3)) − N/((N+1)(N−3))`, the two denominators being the electric gaps
`E_F − 2C_2(Sym²F)` and `E_F − 2C_2(Λ²F)`; `N = 3` (where `Λ²F = F̄` is retained) and
`N = 4` (where `Λ²F` is self-conjugate) are exceptional and are stated separately.
The derivation is the manuscript's; what is proved here is the arithmetic. -/

/-- The two-flux plaquette gaps: `E_F − 2C_2(Sym²F) = −(N−1)(N+3)/N` and
`E_F − 2C_2(Λ²F) = −(N+1)(N−3)/N`. -/
theorem two_flux_gaps (n : ℚ) (h0 : n ≠ 0) :
    (n ^ 2 - 1) / n - 2 * ((n - 1) * (n + 2) / n) = -((n - 1) * (n + 3)) / n ∧
    (n ^ 2 - 1) / n - 2 * ((n + 1) * (n - 2) / n) = -((n + 1) * (n - 3)) / n := by
  constructor <;> field_simp <;> ring

/-- The reduced same-face route of the charge-odd shell, generic rank `N ≥ 5`. -/
noncomputable def sameFaceOdd (n : ℚ) : ℚ :=
  -n / ((n - 1) * (n + 3)) - n / ((n + 1) * (n - 3))

/-- The same-face route of the charge-even shell, generic rank `N ≥ 5`: the vacuum
piece `1/C_F`, the adjoint at gap `E_F − 2N`, and the two like irreps. -/
noncomputable def sameFaceEven (n : ℚ) : ℚ :=
  2 * n / (n ^ 2 - 1) - 2 * n / (n ^ 2 + 1)
    - n / ((n - 1) * (n + 3)) - n / ((n + 1) * (n - 3))

/-- The adjoint gap: `E_F − 2N = −(N² + 1)/N`. -/
theorem adjoint_gap (n : ℚ) (h0 : n ≠ 0) : (n ^ 2 - 1) / n - 2 * n = -(n ^ 2 + 1) / n := by
  field_simp; ring

/-- The charge-odd tower `σ⁻_N + 1/C_F`, generic rank. -/
noncomputable def towerOdd (n : ℚ) : ℚ := sameFaceOdd n + 2 * n / (n ^ 2 - 1)
/-- The charge-even tower `σ⁺_N + 1/C_F`, generic rank. -/
noncomputable def towerEven (n : ℚ) : ℚ := sameFaceEven n + 2 * n / (n ^ 2 - 1)

/-- The same-face route and the vacuum bubble cancel at leading order: the charge-odd
tower is `−12N/((N²−1)(N²−9))`, of order `N⁻³`. -/
theorem towerOdd_closed (n : ℚ) (hm : n - 1 ≠ 0) (hp : n + 1 ≠ 0) (h3m : n - 3 ≠ 0)
    (h3p : n + 3 ≠ 0) :
    towerOdd n = -12 * n / ((n ^ 2 - 1) * (n ^ 2 - 9)) := by
  unfold towerOdd sameFaceOdd
  have h1 : n ^ 2 - 1 = (n - 1) * (n + 1) := by ring
  have h9 : n ^ 2 - 9 = (n - 3) * (n + 3) := by ring
  rw [h1, h9]
  field_simp
  ring

/-- The on-site and flat second-order scalars of the charge-odd shell, generic rank. -/
noncomputable def onsiteOdd (n : ℚ) : ℚ := towerOdd n + 12 * evenHop n
noncomputable def flatOdd (n : ℚ) : ℚ := onsiteOdd n - 4 * hopping n
/-- The on-site scalar of the charge-even shell and its `Γ`-point `A₁⁺⁺` level. -/
noncomputable def onsiteEven (n : ℚ) : ℚ := towerEven n + 12 * evenHop n
noncomputable def gammaEven (n : ℚ) : ℚ := onsiteEven n + 12 * evenHop n

theorem towerOdd_five : towerOdd 5 = -5 / 32 := by
  unfold towerOdd sameFaceOdd; norm_num
theorem onsiteOdd_five : onsiteOdd 5 = -4785 / 20384 := by
  unfold onsiteOdd towerOdd sameFaceOdd evenHop; norm_num
theorem flatOdd_five : flatOdd 5 = -4945 / 20384 := by
  unfold flatOdd onsiteOdd towerOdd sameFaceOdd evenHop hopping; norm_num
theorem towerOdd_six : towerOdd 6 = -8 / 105 := by
  unfold towerOdd sameFaceOdd; norm_num
theorem flatOdd_six : flatOdd 6 = -13976 / 111825 := by
  unfold flatOdd onsiteOdd towerOdd sameFaceOdd evenHop hopping; norm_num
theorem towerEven_five : towerEven 5 = -155 / 1248 := by
  unfold towerEven sameFaceEven; norm_num
theorem gammaEven_five : gammaEven 5 = -17195 / 61152 := by
  unfold gammaEven onsiteEven towerEven sameFaceEven evenHop; norm_num

/-- `N = 3`: the sextet route `−1/4` plus the vacuum bubble `3/4` is the tower `1/2`;
twelve leakages `ℓ_3` give the on-site `7/102`; subtracting `4t_3` gives the flat `11/306`. -/
theorem su3_odd_ledger :
    (-1 / 4 : ℚ) + 3 / 4 = 1 / 2 ∧
    (1 / 2 : ℚ) + 12 * evenHop 3 = 7 / 102 ∧
    (1 / 2 : ℚ) + 12 * evenHop 3 - 4 * hopping 3 = 11 / 306 := by
  unfold evenHop hopping; norm_num

/-- `N = 3`, charge even: vacuum `3/4`, adjoint `−3/5`, sextet `−1/4` give `σ⁺ = −1/10`;
the tower is `13/20`, the on-site `223/1020`, the `Γ`-point `A₁⁺⁺` level `−217/1020`,
and the band top (`λ = −4`) `1109/3060`. -/
theorem su3_even_ledger :
    (3 / 4 : ℚ) - 3 / 5 - 1 / 4 = -1 / 10 ∧
    (-1 / 10 : ℚ) + 3 / 4 = 13 / 20 ∧
    (13 / 20 : ℚ) + 12 * evenHop 3 = 223 / 1020 ∧
    (13 / 20 : ℚ) + 24 * evenHop 3 = -217 / 1020 ∧
    (13 / 20 : ℚ) + 8 * evenHop 3 = 1109 / 3060 := by
  unfold evenHop; norm_num

/-- `N = 4`: `Λ²F` is self-conjugate, so only `Sym²F` survives in the odd same-face route
(`−4/21`) and it is doubled in the even one (`−8/5`). -/
theorem su4_ledger :
    (-4 / 21 : ℚ) + 8 / 15 = 12 / 35 ∧
    (12 / 35 : ℚ) + 12 * evenHop 4 = 10828 / 59675 ∧
    (12 / 35 : ℚ) + 12 * evenHop 4 - 4 * hopping 4 = 9932 / 59675 ∧
    (8 / 15 : ℚ) - 8 / 17 - 4 / 21 - 8 / 5 + 8 / 15 = -2132 / 1785 := by
  unfold evenHop hopping; norm_num

/-- The charge-even vacuum route on a link-disjoint pair, `2/E_F`, is cancelled exactly by
the doubly-excited exchange route, `2/(E_F − 2E_F)`. -/
theorem disjoint_pair_cancels (e : ℚ) : 2 / e + 2 / (e - 2 * e) = 0 := by
  have : e - 2 * e = -e := by ring
  rw [this, div_neg]; ring

/-- The link-resolved census at `N = 3`: the self-conjugate mixed channels carry `−w_ρ`,
the like channels carry `w_ρ/2` each for `ρ` and `ρ̄`, and the six sum to `t_3`. -/
theorem census_three :
    -(wSinglet 3) = 1 / 12 ∧ -(wAdjoint 3) = 16 / 51 ∧
    wAntisym 3 / 2 = -1 / 12 ∧ wSym 3 / 2 = -1 / 9 ∧
    -(wSinglet 3) - wAdjoint 3 + 2 * (wAntisym 3 / 2) + 2 * (wSym 3 / 2) = hopping 3 := by
  unfold wSinglet wAdjoint wAntisym wSym channelWeight casimirF hopping; norm_num

/-! ## The electric window: the Casimir shelf -/

/-- `C_2(ω_i)` for `su(N)`, every root of squared length two. -/
noncomputable def casimirWeight (i n : ℚ) : ℚ := i * (n - i) * (n + 1) / (2 * n)

theorem casimirWeight_one (n : ℚ) (h0 : n ≠ 0) : casimirWeight 1 n = casimirF n := by
  unfold casimirWeight casimirF; field_simp; ring

/-- `C_2(ω_i) − C_F = (N+1)(i−1)(N−i−1)/(2N)`: minimal exactly at the fundamental pair. -/
theorem casimirWeight_sub_fundamental (i n : ℚ) (h0 : n ≠ 0) :
    casimirWeight i n - casimirF n = (n + 1) / (2 * n) * ((i - 1) * (n - i - 1)) := by
  unfold casimirWeight casimirF; field_simp; ring

/-- The three shelf comparisons of the window theorem, as rational functions of `N`. -/
theorem casimir_shelf (n : ℚ) (h0 : n ≠ 0) :
    casimirWeight 2 n - 5 / 4 * casimirF n = (n + 1) * (3 * n - 11) / (8 * n) ∧
    (n - 1) * (n + 2) / n - 5 / 4 * casimirF n = (n - 1) * (3 * n + 11) / (8 * n) ∧
    n - 5 / 4 * casimirF n = (3 * n ^ 2 + 5) / (8 * n) := by
  unfold casimirWeight casimirF
  refine ⟨?_, ?_, ?_⟩ <;> field_simp <;> ring

/-- The one-form flux exclusion at `L = 4`: a once-winding fundamental loop sits at `2C_F`
for every `N`, while a zero-`N`-ality loop costs `2C_2(R) ≥ 2N`, which clears the window
`5C_F/2 = 5(N² − 1)/(4N)`; denominators cleared: `2N · 4N − 5(N² − 1) = 3N² + 5 > 0`. -/
theorem zero_nality_clears_window (n : ℚ) :
    2 * n * (4 * n) - 5 * (n ^ 2 - 1) = 3 * n ^ 2 + 5 := by
  ring

/-- ... and the three-cycle at `L = 3`: `(3N/2) · 4N − 5(N² − 1) = N² + 5 > 0`. -/
theorem winding_triangle_clears_window (n : ℚ) :
    (3 * n / 2) * (4 * n) - 5 * (n ^ 2 - 1) = n ^ 2 + 5 := by ring

/-! ## The SU(3) Riesz island: the arithmetic the contour is placed by -/

/-- The SU(3) one-link electric numerator in units of `1/6`: `p² + q² + pq + 3p + 3q`. -/
def su3Numerator (p q : ℕ) : ℕ := p * p + q * q + p * q + 3 * p + 3 * q

/-- The nonzero one-link numerators below `18` are exactly `4, 9, 10, 16`
(`F`, `Adj`, `Sym²F` and its conjugate, `(2,1)`-type). -/
theorem su3_numerators_below_eighteen :
    ∀ p q : Fin 5, (p.val, q.val) ≠ (0, 0) → su3Numerator p.val q.val < 18 →
      su3Numerator p.val q.val = 4 ∨ su3Numerator p.val q.val = 9 ∨
        su3Numerator p.val q.val = 10 ∨ su3Numerator p.val q.val = 16 := by
  decide

/-- Any label above `4` already exceeds `18`: `p ≥ 5` gives `p² + 3p ≥ 40`. -/
theorem su3_numerator_large (p q : ℕ) (hp : 5 ≤ p) : 18 < su3Numerator p q := by
  unfold su3Numerator; nlinarith

/-- The generators: the empty link and the four numerators below `18`. -/
def su3Generators : Fin 5 → ℕ := ![0, 4, 9, 10, 16]

/-- The additive semigroup generated by `{4, 9, 10, 16}` does not reach `15` with at most
four links, while it reaches `14` and `17`. -/
theorem su3_semigroup_gap :
    (∀ a b c d : Fin 5,
      su3Generators a + su3Generators b + su3Generators c + su3Generators d ≠ 15) ∧
    (4 + 10 = 14) ∧ (4 + 4 + 9 = 17) := by
  refine ⟨?_, rfl, rfl⟩
  decide

/-- The two separations of the Riesz island, from the neighbours `14` and `17` of the
shell `16` in units of `1/6`, each interval dilated by `1 ± λ`. -/
theorem riesz_separations (l : ℚ) :
    (8 / 3 - 8 * l / 3) - (7 / 3 + 7 * l / 3) = (1 - 15 * l) / 3 ∧
    (17 / 6 - 17 * l / 6) - (8 / 3 + 8 * l / 3) = (1 - 33 * l) / 6 := by
  constructor <;> ring

/-- The contour `|z − 8/3| = (1 − λ)/12` clears the shell interval, the upper neighbour and
the lower neighbour by `(1 − 33λ)/12`, `(1 − 33λ)/12` and `(3 − 27λ)/12`. -/
theorem riesz_contour_clearances (l : ℚ) :
    (1 - l) / 12 - 8 * l / 3 = (1 - 33 * l) / 12 ∧
    (17 / 6 - 17 * l / 6) - 8 / 3 - (1 - l) / 12 = (1 - 33 * l) / 12 ∧
    8 / 3 - (1 - l) / 12 - (7 / 3 + 7 * l / 3) = (3 - 27 * l) / 12 := by
  refine ⟨?_, ?_, ?_⟩ <;> ring

/-- For `λ ≥ 0` the lower clearance dominates, so the minimum is `(1 − 33λ)/12` and the
resolvent bound on the contour is `12/(1 − 33λ)`. -/
theorem riesz_min_clearance (l : ℚ) (hl : 0 ≤ l) : (1 - 33 * l) / 12 ≤ (3 - 27 * l) / 12 := by
  linarith

/-- The local interaction bound `27|u|`: the `3/2` rescaling, three plaquettes per cell,
and `‖χ + χ̄‖ ≤ 6`; and the rescaled SU(3) local gap `(3/4) C_F = 1`. -/
theorem kinematic_constants : (3 / 2 : ℚ) * 3 * 6 = 27 ∧ (3 / 4 : ℚ) * (4 / 3) = 1 := by
  norm_num

/-! ## The incidence factorisation, over `ℂ` -/

open Matrix in
/-- The face-to-link Bloch incidence `B(k) = ∂₂(k)†` in the `(12, 13, 23)` face basis,
with `d_j = e^{ik_j} − 1`. -/
def blochB (d₁ d₂ d₃ : ℂ) : Matrix (Fin 3) (Fin 3) ℂ :=
  !![d₂, -d₁, 0; d₃, 0, -d₁; 0, d₃, -d₂]

/-- The carrier vector `w(k) = (d̄₃, −d̄₂, d̄₁)`. -/
def carrierW (d₁ d₂ d₃ : ℂ) : Fin 3 → ℂ := ![star d₃, -star d₂, star d₁]

/-- `q(k) = |d₁|² + |d₂|² + |d₃|²`, written with `star` so the identity is polynomial. -/
def bandQ (d₁ d₂ d₃ : ℂ) : ℂ := d₁ * star d₁ + d₂ * star d₂ + d₃ * star d₃

open Matrix in
/-- The incidence factorisation `B B† = q I − w w†`, entry by entry. -/
theorem bloch_factorisation (d₁ d₂ d₃ : ℂ) :
    blochB d₁ d₂ d₃ * (blochB d₁ d₂ d₃)ᴴ
      = bandQ d₁ d₂ d₃ • (1 : Matrix (Fin 3) (Fin 3) ℂ)
        - vecMulVec (carrierW d₁ d₂ d₃) (star (carrierW d₁ d₂ d₃)) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [blochB, carrierW, bandQ, Matrix.mul_apply, Fin.sum_univ_three, vecMulVec] <;> ring

open Matrix in
/-- The carrier is annihilated by `B†`: the Bloch form of `∂₂∂₃ = 0`. -/
theorem carrier_in_kernel (d₁ d₂ d₃ : ℂ) :
    (blochB d₁ d₂ d₃)ᴴ *ᵥ carrierW d₁ d₂ d₃ = 0 := by
  ext i
  fin_cases i <;>
    simp [blochB, carrierW, Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;> ring

open Matrix in
/-- `‖w‖² = q`. -/
theorem carrier_norm (d₁ d₂ d₃ : ℂ) :
    star (carrierW d₁ d₂ d₃) ⬝ᵥ carrierW d₁ d₂ d₃ = bandQ d₁ d₂ d₃ := by
  simp [carrierW, bandQ, dotProduct, Fin.sum_univ_three]; ring

/-! ## The unsigned comparison band: every root of the cubic lies in `[0, 16]` -/

/-- The charge-even cubic over the reals. -/
noncomputable def evenCubicR (m a b c : ℝ) : ℝ :=
  m ^ 3 - 2 * (a + b + c) * m ^ 2 + (a + b + c) ^ 2 * m - 4 * a * b * c

theorem evenCubicR_factor (m a b c : ℝ) :
    evenCubicR m a b c = m * (m - (a + b + c)) ^ 2 - 4 * (a * b * c) := by
  unfold evenCubicR; ring

/-- Below `μ = 0` the cubic is strictly negative, so `λ ≥ −4`. -/
theorem even_cubic_neg_below_zero (m a b c : ℝ) (hm : m < 0) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hc : 0 ≤ c) : evenCubicR m a b c < 0 := by
  rw [evenCubicR_factor]
  have hp : 0 ≤ a + b + c := by linarith
  have h1 : 0 < (m - (a + b + c)) ^ 2 := by
    have : m - (a + b + c) < 0 := by linarith
    nlinarith
  have h2 : m * (m - (a + b + c)) ^ 2 < 0 := mul_neg_of_neg_of_pos hm h1
  have h3 : 0 ≤ a * b * c := by positivity
  linarith

/-- Above `μ = 16` the cubic is strictly positive when each `a_i ∈ [0, 4]`, so `λ ≤ 12`:
`f(μ) − f(16) = (μ − 16)((μ − p)² + 16(μ + 16 − 2p))` and `f(16) = 16(16 − p)² − 4abc ≥ 0`. -/
theorem even_cubic_pos_above_sixteen (m a b c : ℝ) (hm : 16 < m)
    (ha : 0 ≤ a) (ha4 : a ≤ 4) (hb : 0 ≤ b) (hb4 : b ≤ 4) (hc : 0 ≤ c) (hc4 : c ≤ 4) :
    0 < evenCubicR m a b c := by
  have hp : a + b + c ≤ 12 := by linarith
  have habc : a * b * c ≤ 64 := by
    have h1 : a * b ≤ 16 := by nlinarith
    have h2 : 0 ≤ a * b := by positivity
    nlinarith
  have h16 : 0 ≤ 16 * (16 - (a + b + c)) ^ 2 - 4 * (a * b * c) := by
    have : 4 ≤ 16 - (a + b + c) := by linarith
    nlinarith
  have hdiff : evenCubicR m a b c - (16 * (16 - (a + b + c)) ^ 2 - 4 * (a * b * c))
      = (m - 16) * ((m - (a + b + c)) ^ 2 + 16 * (m + 16 - 2 * (a + b + c))) := by
    unfold evenCubicR; ring
  have hpos : 0 < (m - 16) * ((m - (a + b + c)) ^ 2 + 16 * (m + 16 - 2 * (a + b + c))) := by
    apply mul_pos
    · linarith
    · have : 0 < m + 16 - 2 * (a + b + c) := by linarith
      have hsq := sq_nonneg (m - (a + b + c))
      linarith
  linarith

/-! ## The two-cube closure and the one-cube shell: the printed spectra -/

/-- `B = 6`: the four cross-cell pairs split `D ∓ c` about `−2317/612` by `c = 5/612`, the
end caps sit at `−2295/612 = −15/4`; `B = 4`: about `−7/4` by `c = −1/12`. -/
theorem two_cube_spectra :
    (-2317 / 612 : ℚ) - 5 / 612 = -129 / 34 ∧ (-2317 / 612 : ℚ) + 5 / 612 = -34 / 9 ∧
    (-2295 / 612 : ℚ) = -15 / 4 ∧
    (-7 / 4 : ℚ) - (-1 / 12) = -5 / 3 ∧ (-7 / 4 : ℚ) + (-1 / 12) = -11 / 6 := by
  norm_num

/-- The link cutoff: `w_Λ − w_1 = −1/12`, what it drops is `w_Sym − w_Adj = 14/153`, and the
two sum to `t_3`. -/
theorem cutoff_split :
    wAntisym 3 - wSinglet 3 = -1 / 12 ∧ wSym 3 - wAdjoint 3 = 14 / 153 ∧
    (-1 / 12 : ℚ) + 14 / 153 = hopping 3 := by
  unfold wAntisym wSinglet wSym wAdjoint channelWeight casimirF hopping; norm_num

/-- The `B = 6` cube scalar misses the bridge's by exactly the same-face sextet route `1/4`,
and its shell `{α, α + 4t, α + 6t}` is `{39/68, 371/612, 127/204}`. -/
theorem one_cube_shell :
    (39 / 68 : ℚ) - 11 / 34 = 1 / 4 ∧
    (39 / 68 : ℚ) + 4 * (5 / 612) = 371 / 612 ∧ (39 / 68 : ℚ) + 6 * (5 / 612) = 127 / 204 := by
  norm_num

/-! ## The fourth-order kernel in orbit amplitudes (ADR 0019–0021)

The 189-record historical kernel carries six orbit amplitudes; the shape coefficients are
closed form in them, and both recorded values of `C_shp` and the cluster-assembled third
side are the same formula evaluated on different `ρ`. These are the exact rationals the
kernel-orbits suite establishes at T1; here they are proof-checked arithmetic. Nothing
here prefers any side of C2. -/

/-- The two-hop weight `u`, the historical kernel's `X_QUANTUM`. -/
noncomputable def xQuantum : ℚ := 360421351 / 40327601932800
/-- The historical rotation, in-plane and normal amplitudes. -/
noncomputable def rhoHist : ℚ := 238714892212171339 / 29002361154409843200
noncomputable def piHist : ℚ := -20535103905179 / 1264270320593280
noncomputable def nuHist : ℚ := -1050558388351 / 10081900483200
/-- The cluster-assembled rotation amplitude of `runs/g3_shared_link_pair_2026-09-02`. -/
noncomputable def rhoCluster : ℚ := 588708011765248393 / 14501180577204921600
/-- The cluster-assembled third side of C2. -/
noncomputable def C_shp_cluster : ℚ := -54822624038066723 / 853010622188524800

/-- The normal amplitude both kernels agree on is `−(5/48 + 4u)`: the cube-completion
channel plus the two-hop shadow of `S²`. -/
theorem nu_from_A_and_u : nuHist = -(A_shp + 4 * xQuantum) := by
  unfold nuHist A_shp xQuantum; norm_num

/-- `C_shp = −5/96 − u − (ρ + π)/2` reproduces the historical value on the historical
amplitudes ... -/
theorem C_shp_from_orbits_historical : C_shp_old = -5 / 96 - xQuantum - (rhoHist + piHist) / 2 := by
  unfold C_shp_old xQuantum rhoHist piHist; norm_num

/-- ... and the cluster-assembled third side on the cluster `ρ`. -/
theorem C_shp_from_orbits_cluster :
    C_shp_cluster = -5 / 96 - xQuantum - (rhoCluster + piHist) / 2 := by
  unfold C_shp_cluster xQuantum rhoCluster piHist; norm_num

/-- The tier collapse in orbit amplitudes: `D = −6u + 3u₂` with `u₂ = 2u`, and
`B = (+1 +1 −2)·x`, both zero identically. -/
theorem tier_collapse_orbits (u x : ℚ) : -6 * u + 3 * (2 * u) = 0 ∧ (1 + 1 - 2) * x = 0 := by
  constructor <;> ring

/-- The ε-sector of `ρ + π̃` measured by the ε-blind assembly, `2 × (−55/13872) = −55/6936`,
is not U5's `−25/512`. -/
theorem eps_sector_refutes_U5 :
    2 * (-55 / 13872 : ℚ) = -55 / 6936 ∧ (-55 / 6936 : ℚ) ≠ -25 / 512 := by
  norm_num

end Workhouse
