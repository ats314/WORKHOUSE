/-
# Machine-checked core of the SU(N) cubic flux-band spectral program

Nothing in this file is taken on the authority of a document. Every statement
below is either proved from the definitions given here, or it is not present.
Prose in the corpus is a *pointer* to a claim, never evidence for it.

Scope: this file formalises the **exact-rational and polynomial-identity
layer**. Derivations that need operator theory or Haar integration are T1
checks in `src/workhouse/invariants/`; what they reduce to rational or
polynomial identities is proved here.

Provenance for each statement is a section reference, recorded so a reader can
find what the corpus *claims*; the Lean proof is what makes it true here.
-/
import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Exp

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

/-! ## The per-channel resolvent equation: the projector-to-hopping step

A channel's squared projector norm `d_ρ/N²` and its signed contribution to the
cross matrix element are related but not identical statements. The publication
edition (eqs. 11–12) displays the step between them: the per-channel resolvent
element is `−η_ρ s(p',e) s(p,e) (d_ρ/N²)/(C_F + C_ρ/2)` with `η = −1` on the
mixed family `{1, Adj}` and `+1` on the like family `{Λ², Sym²}`, and the
incidence-stripped four-channel sum IS the all-rank hopping. Formalised here so
the assembly is a proof-checked identity from the dimension/Casimir table, not
a jump between two displayed formulas. -/

/-- The fundamental quadratic Casimir `C_F = (n² − 1)/(2n)`. -/
noncomputable def casimirF (n : ℚ) : ℚ := (n ^ 2 - 1) / (2 * n)

/-- The per-channel resolvent weight `w = −(d/n²)/(C_F + c/2)` for an
intermediate channel of dimension `d` and Casimir `c`. -/
noncomputable def resolventWeight (d c n : ℚ) : ℚ :=
    -(d / n ^ 2) / (casimirF n + c / 2)

/-- The singlet channel `(d, c) = (1, 0)` in closed form: `w₁ = −2/(n(n²−1))`. -/
theorem resolventWeight_singlet (n : ℚ) (h0 : n ≠ 0) (h1 : n ^ 2 - 1 ≠ 0) :
    resolventWeight 1 0 n = -2 / (n * (n ^ 2 - 1)) := by
  unfold resolventWeight casimirF
  rw [show (n ^ 2 - 1) / (2 * n) + (0 : ℚ) / 2 = (n ^ 2 - 1) / (2 * n) by ring,
    div_div_eq_mul_div, div_eq_div_iff h1 (mul_ne_zero h0 h1)]
  field_simp

/-- The adjoint channel `(d, c) = (n²−1, n)`: `w_Adj = −2(n²−1)/(n(2n²−1))`. -/
theorem resolventWeight_adjoint (n : ℚ) (h0 : n ≠ 0) (h3 : 2 * n ^ 2 - 1 ≠ 0) :
    resolventWeight (n ^ 2 - 1) n n = -(2 * (n ^ 2 - 1)) / (n * (2 * n ^ 2 - 1)) := by
  unfold resolventWeight casimirF
  rw [show (n ^ 2 - 1) / (2 * n) + n / 2 = (2 * n ^ 2 - 1) / (2 * n) by field_simp; ring,
    div_div_eq_mul_div, div_eq_div_iff h3 (mul_ne_zero h0 h3)]
  field_simp

/-- The antisymmetric channel `(d, c) = (n(n−1)/2, (n+1)(n−2)/n)`:
`w_Λ = −(n−1)/((n+1)(2n−3))`. -/
theorem resolventWeight_antisym (n : ℚ) (h0 : n ≠ 0) (h1p : n + 1 ≠ 0)
    (h4 : 2 * n - 3 ≠ 0) :
    resolventWeight (n * (n - 1) / 2) ((n + 1) * (n - 2) / n) n
      = -(n - 1) / ((n + 1) * (2 * n - 3)) := by
  unfold resolventWeight casimirF
  have hD : 2 * n ^ 2 - n - 3 ≠ 0 := fun h =>
    mul_ne_zero h4 h1p (by linear_combination h)
  rw [show (n ^ 2 - 1) / (2 * n) + (n + 1) * (n - 2) / n / 2
        = (2 * n ^ 2 - n - 3) / (2 * n) by field_simp; ring,
    div_div_eq_mul_div, div_eq_div_iff hD (mul_ne_zero h1p h4)]
  field_simp
  ring

/-- The symmetric channel `(d, c) = (n(n+1)/2, (n−1)(n+2)/n)`:
`w_Sym = −(n+1)/((n−1)(2n+3))`. -/
theorem resolventWeight_sym (n : ℚ) (h0 : n ≠ 0) (h1m : n - 1 ≠ 0)
    (h5 : 2 * n + 3 ≠ 0) :
    resolventWeight (n * (n + 1) / 2) ((n - 1) * (n + 2) / n) n
      = -(n + 1) / ((n - 1) * (2 * n + 3)) := by
  unfold resolventWeight casimirF
  have hD : 2 * n ^ 2 + n - 3 ≠ 0 := fun h =>
    mul_ne_zero h5 h1m (by linear_combination h)
  rw [show (n ^ 2 - 1) / (2 * n) + (n - 1) * (n + 2) / n / 2
        = (2 * n ^ 2 + n - 3) / (2 * n) by field_simp; ring,
    div_div_eq_mul_div, div_eq_div_iff hD (mul_ne_zero h1m h5)]
  field_simp
  ring

/-- The mixed family `{1, Adj}` sums to the antiparallel channel sum `A_N`. -/
theorem mixed_family_sum (n : ℚ) (h0 : n ≠ 0) (h1 : n ^ 2 - 1 ≠ 0)
    (h3 : 2 * n ^ 2 - 1 ≠ 0) :
    resolventWeight 1 0 n + resolventWeight (n ^ 2 - 1) n n = antiparallelSum n := by
  rw [resolventWeight_singlet n h0 h1, resolventWeight_adjoint n h0 h3]
  unfold antiparallelSum
  rw [div_add_div _ _ (mul_ne_zero h0 h1) (mul_ne_zero h0 h3),
    div_eq_div_iff (mul_ne_zero (mul_ne_zero h0 h1) (mul_ne_zero h0 h3))
      (mul_ne_zero h1 h3)]
  ring

/-- The like family `{Λ²F, Sym²F}` sums to the parallel channel sum `B_N`. -/
theorem like_family_sum (n : ℚ) (h0 : n ≠ 0) (h1 : n ^ 2 - 1 ≠ 0)
    (h4 : 2 * n - 3 ≠ 0) (h5 : 2 * n + 3 ≠ 0) :
    resolventWeight (n * (n - 1) / 2) ((n + 1) * (n - 2) / n) n
        + resolventWeight (n * (n + 1) / 2) ((n - 1) * (n + 2) / n) n
      = parallelSum n := by
  have h1p : n + 1 ≠ 0 := fun h => h1 (by linear_combination (n - 1) * h)
  have h1m : n - 1 ≠ 0 := fun h => h1 (by linear_combination (n + 1) * h)
  have h45 : 4 * n ^ 2 - 9 ≠ 0 := fun h =>
    mul_ne_zero h4 h5 (by linear_combination h)
  rw [resolventWeight_antisym n h0 h1p h4, resolventWeight_sym n h0 h1m h5]
  unfold parallelSum
  rw [div_add_div _ _ (mul_ne_zero h1p h4) (mul_ne_zero h1m h5),
    div_eq_div_iff (mul_ne_zero (mul_ne_zero h1p h4) (mul_ne_zero h1m h5))
      (mul_ne_zero h1 h45)]
  ring

/-- The projector-to-cross-matrix-element assembly: the like-family sum minus
the mixed-family sum — the four per-channel resolvent elements with their
charge-odd family signs `η_ρ` — is the all-rank hopping `t_N` exactly. -/
theorem channel_resolvent_assembly (n : ℚ) (h0 : n ≠ 0) (h1 : n ^ 2 - 1 ≠ 0)
    (h3 : 2 * n ^ 2 - 1 ≠ 0) (h4 : 2 * n - 3 ≠ 0) (h5 : 2 * n + 3 ≠ 0) :
    (resolventWeight (n * (n - 1) / 2) ((n + 1) * (n - 2) / n) n
        + resolventWeight (n * (n + 1) / 2) ((n - 1) * (n + 2) / n) n)
      - (resolventWeight 1 0 n + resolventWeight (n ^ 2 - 1) n n)
      = hopping n := by
  have h45 : 4 * n ^ 2 - 9 ≠ 0 := fun h =>
    mul_ne_zero h4 h5 (by linear_combination h)
  rw [mixed_family_sum n h0 h1 h3, like_family_sum n h0 h1 h4 h5]
  unfold antiparallelSum parallelSum hopping
  rw [div_sub_div _ _ (mul_ne_zero h1 h45) (mul_ne_zero h1 h3),
    div_eq_div_iff (mul_ne_zero (mul_ne_zero h1 h45) (mul_ne_zero h1 h3))
      (mul_ne_zero (mul_ne_zero h1 h3) h45)]
  ring

/-! ## The shell isolation constant (G17)

The retained shell's volume-uniform electric isolation reduces to rational
arithmetic once the census and Casimir minimality are in hand; the arithmetic
layer is proved here. `shell_margin_five` is the counting bound's margin, and
the three shelf numerators are the family inequalities behind
`C(rho) >= 5 C_F / 4` for every nontrivial irrep other than `F`, `F-bar`:
each is `8N(C - 5C_F/4)` with denominators cleared, and each factors with the
sign visible. -/

/-- Five charged links clear the plaquette shell by exactly `C_F/2`. -/
theorem shell_margin_five (n : ℚ) :
    5 * casimirF n / 2 - 2 * casimirF n = casimirF n / 2 := by
  unfold casimirF; ring

/-- The `Λ²F` shelf numerator: `8N(C - 5C_F/4)` clears to `(3N-11)(N+1)`,
nonnegative from `N = 4`; at `N = 3` the antisymmetric square IS `F-bar`. -/
theorem lambda2_shelf_numerator (n : ℚ) :
    8 * ((n + 1) * (n - 2)) - 5 * (n ^ 2 - 1) = (3 * n - 11) * (n + 1) := by ring

/-- The `Sym²F` shelf numerator: `(3N+11)(N-1)`, nonnegative for `N ≥ 1`. -/
theorem sym2_shelf_numerator (n : ℚ) :
    8 * ((n - 1) * (n + 2)) - 5 * (n ^ 2 - 1) = (3 * n + 11) * (n - 1) := by ring

/-- The adjoint shelf numerator: `3N² + 5`, positive at every rank. -/
theorem adjoint_shelf_numerator (n : ℚ) :
    8 * (n * n) - 5 * (n ^ 2 - 1) = 3 * n ^ 2 + 5 := by ring

/-- The isolation switch point: `4N(2(C_{Λ²} − C_F) − C_F)` clears to
`2(N−5)(N+1)`, so the heavier-irrep margin undercuts the domino margin `C_F`
exactly below `N = 5` -- which, with `Λ²F = F-bar` at `N = 3`, leaves `SU(4)`
as the single rank where the isolation constant is `2(C_{Λ²} − C_F) = 5/4`
rather than `C_F`. -/
theorem isolation_switch_numerator (n : ℚ) :
    4 * ((n - 3) * (n + 1)) - 2 * (n ^ 2 - 1) = 2 * ((n - 5) * (n + 1)) := by ring

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

/-! ## The adjacent-face cube completion (G3, C2, G14 — ADR 0024)

`cubeCompletion` is the opposite-face row, 24 single-loop orderings. Between two
ADJACENT faces of the cube 14 orderings are single-loop (`S₄ = −11`, the
off-axis run's second primitive channel) and 10 pass through a product of two
disjoint loops; in the units of the law the latter add `−18`. The enumeration
is `workhouse.cellular.c_full` at T1; the algebra is here. -/

/-- `−106/(N(N²−1)³)`: the adjacent-face completion at every rank. -/
noncomputable def cubeCompletionAdjacent (n : ℚ) : ℚ := -106 / (n * (n ^ 2 - 1) ^ 3)

/-- Primitive plus multi-loop, at every rank. -/
theorem cubeCompletionAdjacent_split (n : ℚ) :
    cubeCompletionAdjacent n = -88 / (n * (n ^ 2 - 1) ^ 3) + -18 / (n * (n ^ 2 - 1) ^ 3) := by
  unfold cubeCompletionAdjacent; ring

/-- The SU(3) value, the rotation record's cube term in the kernel's basis. -/
theorem cubeCompletionAdjacent_three : cubeCompletionAdjacent 3 = -53 / 768 := by
  unfold cubeCompletionAdjacent; norm_num

/-- Adjacent over opposite is `53/80` at every rank. -/
theorem cubeCompletionAdjacent_ratio (n : ℚ) (h0 : n ≠ 0) (h1 : n ^ 2 - 1 ≠ 0) :
    cubeCompletionAdjacent n = 53 / 80 * cubeCompletion n := by
  unfold cubeCompletionAdjacent cubeCompletion
  have h3 : (n ^ 2 - 1) ^ 3 ≠ 0 := pow_ne_zero 3 h1
  field_simp
  ring

/-- The historical pipeline's eight orderings sum to `31/1536` in magnitude; the
sixteen it lacks are exactly `25/512`. -/
theorem cube_shortfall : (53 : ℚ) / 768 - 31 / 1536 = 25 / 512 := by norm_num

/-- `C_shp = −5/96 − u − (ρ + π)/2`, so lowering `ρ` by `25/512` raises `C_shp` by
`25/1024`. -/
theorem cShp_from_rho_shift (u rho pi : ℚ) :
    -5 / 96 - u - ((rho - 25 / 512) + pi) / 2 = (-5 / 96 - u - (rho + pi) / 2) + 25 / 1024 := by
  ring

/-- The assembled coefficient in the kernel's basis: the historical value plus `25/1024`
is the continuation-shifted rational. -/
theorem cShp_assembled_value : C_shp_old + 25 / 1024 = -13035490122347 / 550663802582400 := by
  unfold C_shp_old; norm_num

/-- Through `β = 8A + 16C`, the same shift is `+25/64` on `β₃`. -/
theorem beta_shift_from_cShp : 8 * A_shp + 16 * (C_shp_old + 25 / 1024) = βPenOld + 25 / 64 := by
  unfold A_shp C_shp_old βPenOld; norm_num

/-- The bandwidth `W₄ = α + β` moves with `β`: the assembled row is the historical
`W₄` plus `25/64`, with `α = 5/12` untouched. -/
theorem w4_shift_from_beta : W₄_old + 25 / 64 = 29985119454403 / 34416487661400 := by
  unfold W₄_old; norm_num

theorem w4_old_is_alpha_plus_beta : W₄_old = alphaPen 3 + βPenOld := by
  unfold W₄_old alphaPen βPenOld; norm_num

/-! ## The single-contact dressing at every rank (ADR 0025)

The fourth-order dressing of a shared-link pair by a plaquette touching one
face, in the C-even sector, reconstructed from the third engine at N = 3..70
and verified on the held-out ranks. Here the identity it satisfies is proved:
it is minus the C-even hopping squared over the plaquette rest energy 2 C_F. -/

/-- The all-rank C-even second-order hopping `ℓ_N = −2N(3N²−5)/((N²−1)(4N²−9)(2N²−1))`. -/
noncomputable def evenHopping (n : ℚ) : ℚ :=
  -2 * n * (3 * n ^ 2 - 5) / ((n ^ 2 - 1) * (4 * n ^ 2 - 9) * (2 * n ^ 2 - 1))

/-- The C-even single-contact dressing, as reconstructed. -/
noncomputable def singleContactEven (n : ℚ) : ℚ :=
  -4 * n ^ 3 * (3 * n ^ 2 - 5) ^ 2 / ((n ^ 2 - 1) ^ 3 * (4 * n ^ 2 - 9) ^ 2 * (2 * n ^ 2 - 1) ^ 2)

/-- `singleContactEven = −ℓ_N² / (2 C_F)` with `2 C_F = (N² − 1)/N`. -/
theorem singleContactEven_eq (n : ℚ) (h0 : n ≠ 0) (h1 : n ^ 2 - 1 ≠ 0)
    (h9 : 4 * n ^ 2 - 9 ≠ 0) :
    singleContactEven n = -(evenHopping n) ^ 2 / ((n ^ 2 - 1) / n) := by
  unfold singleContactEven evenHopping
  field_simp
  ring

/-- Its SU(3) value is the run's `−121/249696`. -/
theorem singleContactEven_three : singleContactEven 3 = -121 / 249696 := by
  unfold singleContactEven; norm_num

/-- The C-even hopping at SU(3) is `−11/306`, the registered `ell_3`. -/
theorem evenHopping_three : evenHopping 3 = -11 / 306 := by
  unfold evenHopping; norm_num

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

/-! ### The T1 triplet at Gamma and the isolation constant (ADR 0028)

At `k = 0` the orientation triplet is one irreducible `T_1`, so the effective
Hamiltonian is a scalar there at every order; on the Hodge form the deviation
from that scalar is bounded by `C_iso q_a(k)`, and the arithmetic below is the
rational part of that bound: the condition making `C_iso = -nu~ = 5/48` for the
assembled `C_shp`, and the resulting isolation threshold `u*^2 = 2/51`. -/

/-- The assembled off-axis coefficient in the kernel's basis (ADR 0024). -/
noncomputable def cShpAssembled : ℚ := -13035490122347 / 550663802582400

/-- The two-hop weight `u = X_QUANTUM`. -/
noncomputable def xQuantum : ℚ := 360421351 / 40327601932800

/-- The in-plane orbit amplitude `pi`. -/
noncomputable def piOrbit : ℚ := -20535103905179 / 1264270320593280

/-- `nu~ = -5/48`, the opposite-face cube completion. -/
noncomputable def nuTilde : ℚ := -5 / 48

/-- `pi~ = pi + 2u` is negative, so `sup |eps| = 4u - pi~` over `q_a ∈ [0, 12]`. -/
theorem piTilde_neg : piOrbit + 2 * xQuantum < 0 := by
  unfold piOrbit xQuantum; norm_num

/-- The condition under which the carrier coefficient dominates the transverse one,
`-nu~ + 2C ≥ sup |eps| = 4u - pi~`, for the assembled `C_shp`. -/
theorem isolation_condition_assembled :
    4 * xQuantum - (piOrbit + 2 * xQuantum) ≤ -nuTilde + 2 * cShpAssembled := by
  unfold xQuantum piOrbit nuTilde cShpAssembled; norm_num

/-- The assembled `C_shp` is negative, so `2C + 2|C| = 0` and `C_iso = -nu~`. -/
theorem cShpAssembled_neg : cShpAssembled < 0 := by
  unfold cShpAssembled; norm_num

/-- `C_iso = max(-nu~ + 2C, sup|eps|) + 2|C| = (-nu~ + 2C) - 2C = -nu~ = 5/48`. -/
theorem cIso_assembled : (-nuTilde + 2 * cShpAssembled) + 2 * (-cShpAssembled) = 5 / 48 := by
  unfold nuTilde cShpAssembled; norm_num

/-- The isolation threshold: `u*^2 = t_3 / (2 C_iso) = (5/612) / (5/24) = 2/51`. -/
theorem uStarSq_isolation : (5 / 612 : ℚ) / (2 * (5 / 48)) = 2 / 51 := by
  norm_num

/-- Below the threshold the relative gap `t_3 u^2 - 2 C_iso u^4` is positive. -/
theorem relative_gap_pos (u : ℚ) (hu : 0 < u) (h : u ^ 2 < 2 / 51) :
    0 < 5 / 612 * u ^ 2 - 2 * (5 / 48) * u ^ 4 := by
  have hu2 : 0 < u ^ 2 := by positivity
  have : u ^ 4 = u ^ 2 * u ^ 2 := by ring
  rw [this]
  nlinarith [mul_lt_mul_of_pos_left h hu2]

/-! ## The all-rank shape coefficient, assembled from three cumulants (ADR 0029)

The corpus states `β_N = P17(N²)/(N R20(N²))` and never derives it. ADR 0027
assembled it from cluster cumulants at N = 4..70; ADR 0029 computes every
cumulant over the field ℚ(N) with the third engine, so each is one rational
function of N. With the pair cluster cancelling and the coplanar dressings the
exact negatives of the perpendicular ones, the assembly is three cumulants and
the adjacent-face cube completion, and the identity with the corpus's formula
is the polynomial identity `betaN_assembled_numerator` below. The definitions
carry the closed forms the engine returns; what Lean checks is that they sum
to the corpus's coefficient. -/

/-- The corpus's numerator `P17(z)`, `z = N²` (GLUEBALL v3.1, Appendix A). -/
def P17 (z : ℚ) : ℚ :=
  2096187310080 * z ^ 17 - 45206560309248 * z ^ 16 + 448972002607104 * z ^ 15 - 2723575470882816 * z ^ 14 + 11288692151812096 * z ^ 13 - 33888218411529728 * z ^ 12 + 76218901019673664 * z ^ 11 - 131068691814847264 * z ^ 10 + 174326341061538992 * z ^ 9 - 180230597250871976 * z ^ 8 + 144751635142984472 * z ^ 7 - 89742150515602808 * z ^ 6 + 42388925672412712 * z ^ 5 - 14916377727371552 * z ^ 4 + 3768794520714128 * z ^ 3 - 641987460459360 * z ^ 2 + 65414604672000 * z - 2967321600000

/-- The corpus's denominator `R20(z)` in its factored form. -/
def R20 (z : ℚ) : ℚ :=
  (z - 1) ^ 3 * (2 * z - 3) * (2 * z - 1) ^ 3 * (3 * z - 2) * (3 * z - 1) * (4 * z - 9) ^ 3
    * (4 * z - 5) * (4 * z - 1) * (9 * z - 25) * (9 * z - 16) * (16 * z ^ 2 - 44 * z + 25)
    * (16 * z ^ 2 - 33 * z + 16)

/-- `β_N = P17(N²)/(N R20(N²))`, the corpus's all-rank fourth-order shape coefficient. -/
noncomputable def betaN (n : ℚ) : ℚ := P17 (n ^ 2) / (n * R20 (n ^ 2))

/-- The two-hop weight `u(N)`, C-odd: numerator. -/
def twoHopNum (n : ℚ) : ℚ :=
  n ^ 3 * (n ^ 2 - 4) ^ 2 * (16896 * n ^ 14 - 131616 * n ^ 12 + 451352 * n ^ 10 - 882908 * n ^ 8 + 1058410 * n ^ 6 - 771029 * n ^ 4 + 313093 * n ^ 2 - 54216)

/-- The two-hop weight: denominator. -/
def twoHopDen (n : ℚ) : ℚ :=
  2 * (n ^ 2 - 1) ^ 3 * (4 * n ^ 2 - 9) ^ 3 * (9 * n ^ 2 - 16) * (2 * n ^ 2 - 3) * (2 * n ^ 2 - 1) ^ 3
    * (3 * n ^ 2 - 2) * (4 * n ^ 2 - n - 4) * (4 * n ^ 2 + n - 4)

noncomputable def twoHopWeight (n : ℚ) : ℚ := twoHopNum n / twoHopDen n

/-- The C-odd single-contact dressing of the perpendicular pair: numerator and denominator. -/
def singleContactNum (n : ℚ) : ℚ := 2 * n ^ 3 * (n ^ 2 - 4) * (10 * n ^ 2 - 13)

def singleContactDen (n : ℚ) : ℚ := (n ^ 2 - 1) ^ 3 * (4 * n ^ 2 - 9) ^ 2 * (2 * n ^ 2 - 1) ^ 2

noncomputable def singleContactOdd (n : ℚ) : ℚ := singleContactNum n / singleContactDen n

/-- The C-odd corner dressing: numerator and denominator. -/
def cornerNum (n : ℚ) : ℚ :=
  16 * n ^ 3 * (n ^ 2 - 4) * (2379648 * n ^ 18 - 28088736 * n ^ 16 + 143075272 * n ^ 14 - 411323454 * n ^ 12 + 732994774 * n ^ 10 - 837251963 * n ^ 8 + 611821212 * n ^ 6 - 275614672 * n ^ 4 + 69464470 * n ^ 2 - 7465875)

def cornerDen (n : ℚ) : ℚ :=
  (n ^ 2 - 1) ^ 3 * (4 * n ^ 2 - 9) ^ 3 * (4 * n ^ 2 - 1) * (9 * n ^ 2 - 25) * (2 * n ^ 2 - 1) ^ 3
    * (3 * n ^ 2 - 1) * (4 * n ^ 2 - 5) * (4 * n ^ 2 - 2 * n - 5) * (4 * n ^ 2 + 2 * n - 5)

noncomputable def cornerDressing (n : ℚ) : ℚ := cornerNum n / cornerDen n

/-- The cofactors: `N R20(N²)` over each cumulant's denominator, polynomials because
every denominator factor is a factor of `R20`. -/
def twoHopCof (n : ℚ) : ℚ :=
  n * (4 * n ^ 2 - 1) * (9 * n ^ 2 - 25) * (3 * n ^ 2 - 1) * (4 * n ^ 2 - 5)
    * (16 * n ^ 4 - 44 * n ^ 2 + 25) / 2

def singleContactCof (n : ℚ) : ℚ :=
  n * (2 * n ^ 2 - 3) * (2 * n ^ 2 - 1) * (3 * n ^ 2 - 2) * (3 * n ^ 2 - 1) * (4 * n ^ 2 - 9)
    * (4 * n ^ 2 - 5) * (4 * n ^ 2 - 1) * (9 * n ^ 2 - 25) * (9 * n ^ 2 - 16)
    * (16 * n ^ 4 - 44 * n ^ 2 + 25) * (16 * n ^ 4 - 33 * n ^ 2 + 16)

def cornerCof (n : ℚ) : ℚ :=
  n * (2 * n ^ 2 - 3) * (3 * n ^ 2 - 2) * (9 * n ^ 2 - 16) * (16 * n ^ 4 - 33 * n ^ 2 + 16)

def cubeCof (n : ℚ) : ℚ :=
  (2 * n ^ 2 - 3) * (2 * n ^ 2 - 1) ^ 3 * (3 * n ^ 2 - 2) * (3 * n ^ 2 - 1) * (4 * n ^ 2 - 9) ^ 3
    * (4 * n ^ 2 - 5) * (4 * n ^ 2 - 1) * (9 * n ^ 2 - 25) * (9 * n ^ 2 - 16)
    * (16 * n ^ 4 - 44 * n ^ 2 + 25) * (16 * n ^ 4 - 33 * n ^ 2 + 16)

theorem twoHopDen_cof (n : ℚ) : n * R20 (n ^ 2) = twoHopDen n * twoHopCof n := by
  unfold R20 twoHopDen twoHopCof; ring

theorem singleContactDen_cof (n : ℚ) :
    n * R20 (n ^ 2) = singleContactDen n * singleContactCof n := by
  unfold R20 singleContactDen singleContactCof; ring

theorem cornerDen_cof (n : ℚ) : n * R20 (n ^ 2) = cornerDen n * cornerCof n := by
  unfold R20 cornerDen cornerCof; ring

theorem cubeDen_cof (n : ℚ) : n * R20 (n ^ 2) = (n * (n ^ 2 - 1) ^ 3) * cubeCof n := by
  unfold R20 cubeCof; ring

/-- The final polynomial identity: over the common denominator `N R20(N²)`, the three
cumulants and the cube completion, with the assembly weights `−16, 32, −16, −8`, have
numerator `P17(N²)` exactly. -/
theorem betaN_assembled_numerator (n : ℚ) :
    -16 * (twoHopNum n * twoHopCof n) + 32 * (singleContactNum n * singleContactCof n)
        - 16 * (cornerNum n * cornerCof n) - 8 * (-106 * cubeCof n)
      = P17 (n ^ 2) := by
  unfold twoHopNum twoHopCof singleContactNum singleContactCof cornerNum cornerCof cubeCof P17
  ring

theorem twoHopWeight_over_R20 (n : ℚ) (h : n * R20 (n ^ 2) ≠ 0) :
    twoHopWeight n = twoHopNum n * twoHopCof n / (n * R20 (n ^ 2)) := by
  rw [twoHopDen_cof] at h ⊢
  unfold twoHopWeight
  exact (mul_div_mul_right _ _ (right_ne_zero_of_mul h)).symm

theorem singleContactOdd_over_R20 (n : ℚ) (h : n * R20 (n ^ 2) ≠ 0) :
    singleContactOdd n = singleContactNum n * singleContactCof n / (n * R20 (n ^ 2)) := by
  rw [singleContactDen_cof] at h ⊢
  unfold singleContactOdd
  exact (mul_div_mul_right _ _ (right_ne_zero_of_mul h)).symm

theorem cornerDressing_over_R20 (n : ℚ) (h : n * R20 (n ^ 2) ≠ 0) :
    cornerDressing n = cornerNum n * cornerCof n / (n * R20 (n ^ 2)) := by
  rw [cornerDen_cof] at h ⊢
  unfold cornerDressing
  exact (mul_div_mul_right _ _ (right_ne_zero_of_mul h)).symm

theorem cubeCompletionAdjacent_over_R20 (n : ℚ) (h : n * R20 (n ^ 2) ≠ 0) :
    cubeCompletionAdjacent n = -106 * cubeCof n / (n * R20 (n ^ 2)) := by
  rw [cubeDen_cof] at h ⊢
  unfold cubeCompletionAdjacent
  exact (mul_div_mul_right _ _ (right_ne_zero_of_mul h)).symm

/-- The eleven-cumulant assembly of ADR 0027 collapses to three cumulants and the cube:
with the pair cancelling and each coplanar dressing the negative of its perpendicular
counterpart, `8A + 16C` with `A = α/4`, `C = −α/8 − u − (ρ + π)/2` is
`−16u + 32d − 16 corner − 8 K`, and `α` drops out. -/
theorem assembly_three_cumulants (alpha u pair d s corner k : ℚ) :
    8 * (alpha / 4)
        + 16 * (-alpha / 8 - u
          - ((pair + 14 * d + 2 * s + 2 * corner + k) + (-pair + 18 * (-d) + 2 * (-s))) / 2)
      = -16 * u + 32 * d - 16 * corner - 8 * k := by
  ring

/-- `β_N` from three cumulants and the cube completion, at every rank where the corpus's
denominator is nonzero. -/
theorem betaN_from_three_cumulants (n : ℚ) (h : n * R20 (n ^ 2) ≠ 0) :
    -16 * twoHopWeight n + 32 * singleContactOdd n - 16 * cornerDressing n
        - 8 * cubeCompletionAdjacent n
      = betaN n := by
  rw [twoHopWeight_over_R20 n h, singleContactOdd_over_R20 n h, cornerDressing_over_R20 n h,
    cubeCompletionAdjacent_over_R20 n h]
  unfold betaN
  rw [← betaN_assembled_numerator n]
  ring

/-- SU(3): the continuation value of the corpus's formula, which ADR 0024 showed is the
assembled `β₃ = β_historical + 25/64`. -/
theorem betaN_three : betaN 3 = 15644916262153 / 34416487661400 := by
  unfold betaN P17 R20; norm_num

/-- SU(4): the corpus's low-rank table value. -/
theorem betaN_four : betaN 4 = 3601925923737103752887 / 70481696720359496343750 := by
  unfold betaN P17 R20; norm_num

/-! ## Finite ground-state forms and the residual budget

MMM 2019, equations II.2, II.9 and II.16, and Mondal 2023, equations 4.1 and
4.9, motivate an operator-identification question: the weighted Dirichlet form
must belong to the physical Hamiltonian. The finite identities below prove
that identification for a real symmetric matrix, including a nonconstant trial
state residual. No infinite-dimensional domain, curvature, continuum limit or
Yang-Mills existence hypothesis is asserted here.
-/

open scoped BigOperators

/-- The real quadratic form of a finite matrix. -/
noncomputable def finiteMatrixForm {ι : Type*} [Fintype ι]
    (H : ι → ι → ℝ) (x : ι → ℝ) : ℝ :=
  ∑ i, ∑ j, H i j * x i * x j

/-- Multiplication by `ψ` identifies this weighted norm with the ordinary norm. -/
noncomputable def groundStateNormSq {ι : Type*} [Fintype ι]
    (ψ f : ι → ℝ) : ℝ := ∑ i, (ψ i * f i) ^ 2

/-- The finite Dirichlet form, with the factor `1/2` compensating double edge counting. -/
noncomputable def groundStateDirichlet {ι : Type*} [Fintype ι]
    (H : ι → ι → ℝ) (ψ f : ι → ℝ) : ℝ :=
  (1 / 2) * ∑ i, ∑ j, (-H i j) * ψ i * ψ j * (f i - f j) ^ 2

/-- Exact trial-ground-state transform. The residual `R` may vary with the vertex;
its row equation is a concrete matrix hypothesis, not a spectral-gap assumption. -/
theorem finite_ground_state_residual_identity {ι : Type*} [Fintype ι]
    (H : ι → ι → ℝ) (ψ f R : ι → ℝ)
    (hsymm : ∀ i j, H i j = H j i)
    (hrow : ∀ i, ∑ j, H i j * ψ j = R i * ψ i) :
    finiteMatrixForm H (fun i => ψ i * f i) =
      groundStateDirichlet H ψ f + ∑ i, R i * (ψ i * f i) ^ 2 := by
  have hleft : (∑ i, ∑ j, H i j * ψ i * ψ j * f i ^ 2) =
      ∑ i, R i * (ψ i * f i) ^ 2 := by
    apply Finset.sum_congr rfl
    intro i _
    calc
      (∑ j, H i j * ψ i * ψ j * f i ^ 2) =
          (ψ i * f i ^ 2) * ∑ j, H i j * ψ j := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro j _
        ring
      _ = R i * (ψ i * f i) ^ 2 := by rw [hrow i]; ring
  have hright : (∑ i, ∑ j, H i j * ψ i * ψ j * f j ^ 2) =
      ∑ i, R i * (ψ i * f i) ^ 2 := by
    rw [Finset.sum_comm]
    calc
      (∑ j, ∑ i, H i j * ψ i * ψ j * f j ^ 2) =
          ∑ j, ∑ i, H j i * ψ j * ψ i * f j ^ 2 := by
        apply Finset.sum_congr rfl
        intro j _
        apply Finset.sum_congr rfl
        intro i _
        rw [hsymm i j]
        ring
      _ = _ := hleft
  have hexpand : (∑ i, ∑ j, (-H i j) * ψ i * ψ j * (f i - f j) ^ 2) =
      2 * finiteMatrixForm H (fun i => ψ i * f i) -
        (∑ i, ∑ j, H i j * ψ i * ψ j * f i ^ 2) -
        (∑ i, ∑ j, H i j * ψ i * ψ j * f j ^ 2) := by
    unfold finiteMatrixForm
    simp only [Finset.mul_sum, ← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl
    intro i _
    apply Finset.sum_congr rfl
    intro j _
    ring
  unfold groundStateDirichlet
  rw [hexpand, hleft, hright]
  ring

/-- For a nonvanishing trial vector the residual is defined by the matrix itself;
the row hypothesis of the general identity is discharged by division. -/
theorem finite_ground_state_ratio_identity {ι : Type*} [Fintype ι]
    (H : ι → ι → ℝ) (ψ f : ι → ℝ)
    (hsymm : ∀ i j, H i j = H j i) (hψ : ∀ i, ψ i ≠ 0) :
    finiteMatrixForm H (fun i => ψ i * f i) = groundStateDirichlet H ψ f +
      ∑ i, ((∑ j, H i j * ψ j) / ψ i) * (ψ i * f i) ^ 2 := by
  apply finite_ground_state_residual_identity H ψ f _ hsymm
  intro i
  field_simp [hψ i]

/-- An exact eigenvector makes the residual constant, leaving precisely a Dirichlet form. -/
theorem finite_ground_state_eigenform_identity {ι : Type*} [Fintype ι]
    (H : ι → ι → ℝ) (ψ f : ι → ℝ) (E : ℝ)
    (hsymm : ∀ i j, H i j = H j i)
    (heigen : ∀ i, ∑ j, H i j * ψ j = E * ψ i) :
    finiteMatrixForm H (fun i => ψ i * f i) - E * groundStateNormSq ψ f =
      groundStateDirichlet H ψ f := by
  have h := finite_ground_state_residual_identity H ψ f (fun _ => E) hsymm heigen
  unfold groundStateNormSq
  rw [Finset.mul_sum]
  linarith

/-- Nonpositive off-diagonal matrix entries and nonnegative `ψ` give a nonnegative
Dirichlet form. Diagonal entries need no sign hypothesis, since their differences vanish. -/
theorem finite_ground_state_dirichlet_nonneg {ι : Type*} [Fintype ι]
    (H : ι → ι → ℝ) (ψ f : ι → ℝ)
    (hoff : ∀ i j, i ≠ j → H i j ≤ 0) (hψ : ∀ i, 0 ≤ ψ i) :
    0 ≤ groundStateDirichlet H ψ f := by
  classical
  unfold groundStateDirichlet
  apply mul_nonneg (by norm_num)
  apply Finset.sum_nonneg
  intro i _
  apply Finset.sum_nonneg
  intro j _
  by_cases hij : i = j
  · subst j
    simp
  · exact mul_nonneg (mul_nonneg (mul_nonneg (neg_nonneg.mpr (hoff i j hij))
      (hψ i)) (hψ j)) (sq_nonneg _)

/-- A weighted Poincare inequality transfers to the centered physical matrix form.
The inverse map `f_i = x_i / ψ_i` is constructed, so no completeness of the
weighted test vectors is hidden in an assumption. -/
theorem finite_ground_state_gap_transfer {ι : Type*} [Fintype ι]
    (H : ι → ι → ℝ) (ψ : ι → ℝ) (E γ : ℝ)
    (hsymm : ∀ i j, H i j = H j i) (hψ : ∀ i, ψ i ≠ 0)
    (heigen : ∀ i, ∑ j, H i j * ψ j = E * ψ i)
    (hpoincare : ∀ f : ι → ℝ, (∑ i, ψ i ^ 2 * f i) = 0 →
      γ * groundStateNormSq ψ f ≤ groundStateDirichlet H ψ f)
    (x : ι → ℝ) (horth : (∑ i, ψ i * x i) = 0) :
    γ * (∑ i, x i ^ 2) ≤ finiteMatrixForm H x - E * (∑ i, x i ^ 2) := by
  let f : ι → ℝ := fun i => x i / ψ i
  have htransport : ∀ i, ψ i * f i = x i := by
    intro i
    dsimp [f]
    field_simp [hψ i]
  have hzero : (∑ i, ψ i ^ 2 * f i) = 0 := by
    calc
      (∑ i, ψ i ^ 2 * f i) = ∑ i, ψ i * x i := by
        apply Finset.sum_congr rfl
        intro i _
        rw [← htransport i]
        ring
      _ = 0 := horth
  have hnorm : groundStateNormSq ψ f = ∑ i, x i ^ 2 := by
    unfold groundStateNormSq
    simp_rw [htransport]
  have hid := finite_ground_state_eigenform_identity H ψ f E hsymm heigen
  have hvec : (fun i => ψ i * f i) = x := funext htransport
  rw [hvec, hnorm] at hid
  have hbound := hpoincare f hzero
  rw [hnorm, ← hid] at hbound
  exact hbound

/-- The ground-state Dirichlet form vanishes identically on constant test functions. -/
theorem groundStateDirichlet_const {ι : Type*} [Fintype ι]
    (H : ι → ι → ℝ) (ψ : ι → ℝ) (c : ℝ) :
    groundStateDirichlet H ψ (fun _ => c) = 0 := by
  unfold groundStateDirichlet
  simp

/-- Any finite symmetric-matrix eigenvector has zero energy relative to its own eigenvalue.
This theorem contains no local baselines e_* and does not assert E - sum e_* = 0,
a positive spectral gap, or the WR26 connected assembly estimate. -/
theorem ground_state_frustration_elimination {ι : Type*} [Fintype ι]
    (H : ι → ι → ℝ) (ψ : ι → ℝ) (E : ℝ)
    (hsymm : ∀ i j, H i j = H j i)
    (heigen : ∀ i, ∑ j, H i j * ψ j = E * ψ i) :
    finiteMatrixForm H ψ - E * (∑ i, ψ i ^ 2) = 0 := by
  have hid := finite_ground_state_eigenform_identity H ψ (fun _ => 1) E hsymm heigen
  have hD : groundStateDirichlet H ψ (fun _ => 1) = 0 := groundStateDirichlet_const H ψ 1
  have hnorm : groundStateNormSq ψ (fun _ => 1) = ∑ i, ψ i ^ 2 := by
    unfold groundStateNormSq
    simp
  have hvec : (fun i => ψ i * (1 : ℝ)) = ψ := by ext i; ring
  rw [hvec, hnorm, hD] at hid
  exact hid

/-- Residual oscillation, rather than the absolute trial energy, spends the gap budget.
The eigenvalue comparison hypotheses are explicit; this does not axiomatize min-max. -/
theorem residual_oscillation_gap_budget (e0 e1 γ rlo rhi : ℝ)
    (hlower : γ + rlo ≤ e1) (hupper : e0 ≤ rhi) :
    γ - (rhi - rlo) ≤ e1 - e0 := by
  linarith

/-- A residual whose oscillation is strictly below the comparison gap leaves a positive gap. -/
theorem residual_oscillation_positive_gap (e0 e1 γ rlo rhi : ℝ)
    (hlower : γ + rlo ≤ e1) (hupper : e0 ≤ rhi) (hbudget : rhi - rlo < γ) :
    0 < e1 - e0 := by
  linarith [residual_oscillation_gap_budget e0 e1 γ rlo rhi hlower hupper]

/-! ## Algebra behind transverse confinement

Simon 1983 motivates retaining transverse zero-point energy along flat valleys.
The first identity below applies to each transverse coordinate of an SU(2)
commuting-valley expansion. The next statements are the finite aggregation and
one-variable optimization needed after analytic slice and Hardy estimates have
been established. They are lower-energy estimates, not a vacuum mass gap.
-/

/-- Lagrange's identity for any finite real family, in double-sum normalization.
It isolates the transverse quadratic potential from the common longitudinal direction. -/
theorem finite_transverse_valley_identity {ι : Type*} [Fintype ι]
    (a u : ι → ℝ) :
    (∑ i, a i ^ 2) * (∑ i, u i ^ 2) - (∑ i, a i * u i) ^ 2 =
      (1 / 2) * ∑ i, ∑ j, (a i * u j - a j * u i) ^ 2 := by
  have hswap : (∑ i, ∑ j, a j ^ 2 * u i ^ 2) = ∑ i, ∑ j, a i ^ 2 * u j ^ 2 := by
    rw [Finset.sum_comm]
  have hexpand : (∑ i, ∑ j, (a i * u j - a j * u i) ^ 2) =
      (∑ i, ∑ j, a i ^ 2 * u j ^ 2) + (∑ i, ∑ j, a j ^ 2 * u i ^ 2) -
        2 * (∑ i, ∑ j, (a i * u i) * (a j * u j)) := by
    simp only [Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl
    intro i _
    apply Finset.sum_congr rfl
    intro j _
    ring
  have hprod : (∑ i, a i ^ 2) * (∑ i, u i ^ 2) = ∑ i, ∑ j, a i ^ 2 * u j ^ 2 := by
    rw [Finset.sum_mul]
    simp only [Finset.mul_sum]
  have hcross : (∑ i, a i * u i) ^ 2 = ∑ i, ∑ j, (a i * u i) * (a j * u j) := by
    rw [pow_two, Finset.sum_mul]
    simp only [Finset.mul_sum]
  rw [hexpand, hswap, ← hprod, ← hcross]
  ring

/-- Summing slice bounds gives `T/2 + cR` from `sumK = n(T+2V)`.
The slice estimate is an explicit hypothesis; the conclusion does not assume a gap. -/
theorem transverse_slice_form_aggregation (T V c R n sumK : ℝ) (hn : 0 < n)
    (hsum : sumK = n * (T + 2 * V)) (hslice : 2 * n * c * R ≤ sumK) :
    T / 2 + c * R ≤ T + V := by
  have h : n * (2 * c * R) ≤ n * (T + 2 * V) := by nlinarith [hslice]
  have hcancel := le_of_mul_le_mul_left h hn
  linarith

/-- Exact slice remainder, so every positive slice margin survives with factor `1/(2n)`. -/
theorem transverse_slice_form_identity (T V c R n : ℝ) (hn : 0 < n) :
    T + V - (T / 2 + c * R) = (n * (T + 2 * V) - 2 * n * c * R) / (2 * n) := by
  field_simp
  ring

/-- Exact remainder at the positive radial optimizer. -/
theorem hardy_linear_remainder (z : ℝ) (hz : 0 < z) :
    1 / (2 * z ^ 2) + z - 3 / 2 = (z - 1) ^ 2 * (2 * z + 1) / (2 * z ^ 2) := by
  field_simp
  ring

/-- The radial `r^-2 + r` balance is globally minimized at the stated scale. -/
theorem hardy_linear_lower_bound (z : ℝ) (hz : 0 < z) :
    3 / 2 ≤ 1 / (2 * z ^ 2) + z := by
  have hrem := hardy_linear_remainder z hz
  have hpos : 0 ≤ (z - 1) ^ 2 * (2 * z + 1) / (2 * z ^ 2) := by positivity
  linarith

/-! ## Mean-residual quartic certificate

For a positive trial state the upper comparison for the ground energy can be
the mean residual, even if its supremum is infinite. The matrix transform above
and the following arithmetic keep this distinction explicit. The Gaussian
moments and min-max comparison are analytic inputs, not postulated axioms.
-/

/-- The gap-budget defect is exactly the sum of the two comparison slacks.
Here `meanR` may be a trial-state expectation, with no bounded-above residual required. -/
theorem residual_mean_slack_identity (e0 e1 γ rmin meanR : ℝ) :
    (e1 - e0) - (γ - (meanR - rmin)) =
      (e1 - (γ + rmin)) + (meanR - e0) := by
  ring

/-- A lower residual bound and a variational upper ground-energy bound suffice. -/
theorem residual_mean_gap_budget (e0 e1 γ rmin meanR : ℝ)
    (hlower : γ + rmin ≤ e1) (htrial : e0 ≤ meanR) :
    γ - (meanR - rmin) ≤ e1 - e0 := by
  linarith [residual_mean_slack_identity e0 e1 γ rmin meanR]

/-- At `m² Ω³ = 6 λ hbar`, the quartic Gaussian trial residual is its floor
`hbar Ω/8` plus an explicit nonnegative square when `λ > 0`. -/
theorem quartic_trial_residual_completion (hbar m omega coupling x : ℝ)
    (hcoupling : coupling ≠ 0) (hscale : m ^ 2 * omega ^ 3 = 6 * coupling * hbar) :
    hbar * omega / 2 - m * omega ^ 2 * x ^ 2 / 2 + coupling * x ^ 4 =
      hbar * omega / 8 + coupling * (x ^ 2 - m * omega ^ 2 / (4 * coupling)) ^ 2 := by
  have hs : m ^ 2 * omega ^ 4 = 6 * coupling * hbar * omega := by
    calc
      m ^ 2 * omega ^ 4 = (m ^ 2 * omega ^ 3) * omega := by ring
      _ = 6 * coupling * hbar * omega := by rw [hscale]
  field_simp
  nlinarith [hs]

/-- The optimized Gaussian trial residual has a global lower bound despite growing
without bound above. This is a polynomial statement for all real `x`. -/
theorem quartic_trial_residual_floor (hbar m omega coupling x : ℝ)
    (hcoupling : 0 < coupling) (hscale : m ^ 2 * omega ^ 3 = 6 * coupling * hbar) :
    hbar * omega / 8 ≤
      hbar * omega / 2 - m * omega ^ 2 * x ^ 2 / 2 + coupling * x ^ 4 := by
  rw [quartic_trial_residual_completion hbar m omega coupling x (ne_of_gt hcoupling) hscale]
  have hsq := mul_nonneg (le_of_lt hcoupling)
    (sq_nonneg (x ^ 2 - m * omega ^ 2 / (4 * coupling)))
  linarith

/-- The exact `3/4` budget from comparison gap `hbar Ω`, mean residual `3hbar Ω/8`,
and residual floor `hbar Ω/8`. Expectations must be established separately. -/
theorem quartic_gaussian_gap_budget (hbar omega : ℝ) :
    hbar * omega - (3 * hbar * omega / 8 - hbar * omega / 8) =
      3 * hbar * omega / 4 := by
  ring

/-- Exact defect of the normalized trial bound away from `q = Ω/Ω* = 1`. -/
theorem quartic_gaussian_frequency_remainder (q : ℝ) (hq : 0 < q) :
    3 / 4 - (5 * q / 4 - 1 / (8 * q ^ 2) - 3 * q ^ 4 / 8) =
      (q - 1) ^ 2 * (3 * q ^ 4 + 6 * q ^ 3 + 9 * q ^ 2 + 2 * q + 1) / (8 * q ^ 2) := by
  field_simp
  ring

/-- Global optimization over every positive normalized Gaussian frequency. -/
theorem quartic_gaussian_frequency_optimal (q : ℝ) (hq : 0 < q) :
    5 * q / 4 - 1 / (8 * q ^ 2) - 3 * q ^ 4 / 8 ≤ 3 / 4 := by
  have hrem := quartic_gaussian_frequency_remainder q hq
  have hnonneg : 0 ≤
      (q - 1) ^ 2 * (3 * q ^ 4 + 6 * q ^ 3 + 9 * q ^ 2 + 2 * q + 1) / (8 * q ^ 2) := by
    positivity
  linarith

/-- The Gaussian residual certificate's global maximum is attained only at `Ω = Ω*`. -/
theorem quartic_gaussian_frequency_optimal_iff (q : ℝ) (hq : 0 < q) :
    (5 * q / 4 - 1 / (8 * q ^ 2) - 3 * q ^ 4 / 8 = 3 / 4) ↔ q = 1 := by
  constructor
  · intro heq
    have hrem := quartic_gaussian_frequency_remainder q hq
    have hpoly : 0 < 3 * q ^ 4 + 6 * q ^ 3 + 9 * q ^ 2 + 2 * q + 1 := by positivity
    have hden : 0 < 8 * q ^ 2 := by positivity
    have hzero :
        (q - 1) ^ 2 * (3 * q ^ 4 + 6 * q ^ 3 + 9 * q ^ 2 + 2 * q + 1) / (8 * q ^ 2) = 0 := by
      linarith
    have hnum := (div_eq_iff (ne_of_gt hden)).mp hzero
    simp only [zero_mul] at hnum
    have hsq : (q - 1) ^ 2 = 0 := (mul_eq_zero.mp hnum).resolve_right (ne_of_gt hpoly)
    have hdiff := sq_eq_zero_iff.mp hsq
    linarith
  · intro heq
    subst q
    norm_num

/-! ## Actual Wilson transfer blocks and uniform estimate interfaces

These statements prove the displayed algebra and scalar inequalities. They do
not assume an unproved Wilson shell or turn the polymer argument into an axiom.
Provenance: docs/derivations/wilson-marked-transfer.md, WT-1 through WT-6.
-/

/-- The symmetric transfer's two endpoint half factors survive exact blocking. -/
theorem wilson_symmetric_block_identity {M : Type*} [Monoid M] (A K : M) (n : ℕ) :
    (A * K * A) ^ (n + 1) = A * (K * A * A) ^ n * K * A := by
  induction n with
  | zero => simp
  | succ n ih =>
    calc
      (A * K * A) ^ (n + 1 + 1) = (A * K * A) ^ (n + 1) * (A * K * A) :=
        pow_succ _ _
      _ = (A * (K * A * A) ^ n * K * A) * (A * K * A) := by rw [ih]
      _ = A * (K * A * A) ^ (n + 1) * K * A := by
        rw [pow_succ]
        simp only [mul_assoc]

/-- A disconnected scalar vacuum amplitude cancels if it is nonzero. -/
theorem wilson_disconnected_vacuum_cancel (marked vacuum spectator : ℝ)
    (hspectator : spectator ≠ 0) :
    (marked * spectator) / (vacuum * spectator) = marked / vacuum := by
  exact mul_div_mul_right marked vacuum hspectator

/-- Finite time sums telescope at every natural block count. -/
theorem wilson_geometric_telescope (q : ℝ) (n : ℕ) :
    (1 - q) * (∑ j ∈ Finset.range n, q ^ j) = 1 - q ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, pow_succ]
    nlinarith

/-- A microscopic time factor controls the entire positive-energy denominator. -/
theorem wilson_damped_time_denominator (tau energy : ℝ)
    (htau : 0 < tau) (henergy : 0 < energy) :
    tau / (Real.exp (tau * energy) - 1) ≤ 1 / energy := by
  have hden : 0 < Real.exp (tau * energy) - 1 := by
    have := Real.one_lt_exp_iff.mpr (mul_pos htau henergy)
    linarith
  apply (div_le_div_iff₀ hden henergy).mpr
  have hexp := Real.add_one_le_exp (tau * energy)
  nlinarith

/-- The positive geometric kernel is its damped version plus one time step. -/
theorem wilson_time_kernel_split (tau x : ℝ) (hx : x ≠ 1) :
    tau * x / (x - 1) = tau + tau / (x - 1) := by
  have hden : x - 1 ≠ 0 := sub_ne_zero.mpr hx
  field_simp
  ring

/-- The geometric counting majorant meets the abstract incompatibility budget. -/
theorem wilson_polymer_kp_budget (d r : ℝ)
    (hd : 2 ≤ d) (hhalf : r ≤ 1 / 2) :
    (d + 1) * r / (d ^ 2 * (1 - r)) ≤ 1 := by
  have hdpos : 0 < d := by linarith
  have hrpos : 0 < 1 - r := by linarith
  have hden : 0 < d ^ 2 * (1 - r) := mul_pos (sq_pos_of_pos hdpos) hrpos
  apply (div_le_iff₀ hden).mpr
  have hpoly : d + 1 ≤ d ^ 2 := by nlinarith [sq_nonneg (d - 2)]
  have hleft : (d + 1) * r ≤ (d + 1) / 2 := by nlinarith
  have hright : d ^ 2 / 2 ≤ d ^ 2 * (1 - r) := by
    nlinarith [sq_nonneg d]
  nlinarith

/-- Two worst-case eigenvalue shifts spend twice the centered error. -/
theorem wilson_relative_gap_budget (c gamma eta q : ℝ) :
    c * q - 2 * gamma * eta * q = (c - 2 * gamma * eta) * q := by
  ring

/-- Once the analytic matching bound is supplied, the remaining relative gap is positive. -/
theorem wilson_relative_gap_positive (c gamma eta q : ℝ)
    (hq : 0 < q) (herror : 2 * gamma * eta < c) :
    0 < c * q - 2 * gamma * eta * q := by
  rw [wilson_relative_gap_budget]
  exact mul_pos (sub_pos.mpr herror) hq

/-- Source-amplitude loss is quadratic only after subtracting the amplitude error. -/
theorem wilson_source_weight_defect (amplitude error : ℝ) :
    amplitude ^ 2 - (amplitude - error) ^ 2 = error * (2 * amplitude - error) := by
  ring

/-- A positive remaining frame amplitude gives a strictly positive weight. -/
theorem wilson_source_weight_positive (amplitude error : ℝ) (herror : error < amplitude) :
    0 < (amplitude - error) ^ 2 := by
  exact sq_pos_of_pos (sub_pos.mpr herror)

/-! ## Complex Wilson shell continuation: scalar interfaces only

The anchored operator, holomorphic kernel and support arguments are analytic
proofs in docs/derivations/wilson-marked-shell-transport.md, not assumptions
axiomatized here.
-/

/-- Polynomial row growth is absorbed into an exponential at every order. -/
theorem wilson_taylor_polynomial_envelope (n : ℕ) : n ^ 3 ≤ 4 * 2 ^ n := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hn : n ≤ 4
    · interval_cases n <;> norm_num
    · obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : n ≠ 0)
      have hk : 4 ≤ k := by omega
      have hprev := ih k (Nat.lt_succ_self k)
      have hstep : (k + 1) ^ 3 ≤ 2 * k ^ 3 := by
        obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le hk
        nlinarith [Nat.zero_le (j ^ 3), Nat.zero_le (j ^ 2)]
      calc
        (k + 1) ^ 3 ≤ 2 * k ^ 3 := hstep
        _ ≤ 2 * (4 * 2 ^ k) := Nat.mul_le_mul_left 2 hprev
        _ = 4 * 2 ^ (k + 1) := by rw [pow_succ]; ring

/-- Exact complex Gram budget, conditional on its operator norm estimates. -/
theorem wilson_complex_gram_budget :
    (1 / 9 : ℚ) * (9 / 8) ^ 2 + 2 / 8 + (1 / 8) ^ 2 = 13 / 32 := by
  norm_num

/-- Removing two equal Taylor terms allows a coupling-independent error budget. -/
theorem wilson_uniform_carrier_coefficient (t gamma xi : ℝ)
    (herror : 8 * gamma * xi ≤ t) :
    t / 4 ≤ t / 2 - 2 * gamma * xi := by
  nlinarith

/-! ## Spatial Schur comparison: finite-scale budget, not Wilson hypotheses -/

/-- A positive accumulated weight transports the reciprocal-gap inequality. -/
theorem wilson_spatial_weighted_step (a alpha rnext r f : ℝ)
    (ha : 0 ≤ a) (halpha : 0 < alpha) (hf : 0 < f)
    (hstep : rnext ≤ r / alpha + 1 / f) :
    a * alpha * rnext ≤ a * r + a * alpha / f := by
  have h := mul_le_mul_of_nonneg_left hstep (mul_nonneg ha (le_of_lt halpha))
  have heq : a * alpha * (r / alpha + 1 / f) = a * r + a * alpha / f := by
    field_simp [ne_of_gt halpha, ne_of_gt hf]
  exact heq ▸ h

/-- Every finite sequence of weighted one-step losses telescopes without omission. -/
theorem wilson_spatial_budget_telescope (a r b : ℕ → ℝ)
    (hstep : ∀ j, a (j + 1) * r (j + 1) ≤ a j * r j + b j) (n : ℕ) :
    a n * r n ≤ a 0 * r 0 + ∑ j ∈ Finset.range n, b j := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ]
    have hs := hstep n
    linarith

/-! ## Geometric summation interfaces for W6, conditional on the decay input

No Wilson resolvent or source map is defined here. The decay hypothesis needed
to apply these scalar lemmas remains an analytic operator estimate.
-/

/-- Telescoping polynomial identity for geometric sums: (1 - ρ) * ∑_{j=0}^{n-1} ρ^j = 1 - ρ^n. -/
theorem geom_sum_mul_sub (rho : ℝ) (n : ℕ) :
    (1 - rho) * (∑ j ∈ Finset.range n, rho ^ j) = 1 - rho ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, mul_add, ih]
    ring

/-- A non-negative factor rho < 1 yields a bound on every finite geometric sum. -/
theorem combes_thomas_geometric_bound (rho : ℝ) (hrho_ge : 0 ≤ rho) (hrho_lt : rho < 1) (n : ℕ) :
    (∑ j ∈ Finset.range n, rho ^ j) ≤ 1 / (1 - rho) := by
  have hpos : 0 < 1 - rho := by linarith
  have hmul := geom_sum_mul_sub rho n
  have hpow : 0 ≤ rho ^ n := by positivity
  have hle : (1 - rho) * (∑ j ∈ Finset.range n, rho ^ j) ≤ 1 := by
    linarith [hmul, hpow]
  exact (le_div_iff₀ hpos).mpr (by linarith)

/-- An assumed geometric envelope bounds a scalar absolute sum uniformly in n.
The envelope hR is a hypothesis, not a derived Combes-Thomas estimate. The
parameter g is unused, and the conclusion is not a bilinear resolvent pairing. -/
theorem combes_thomas_pairing_volume_independent
    (C rho g : ℝ) (hC : 0 ≤ C) (hrho_ge : 0 ≤ rho) (hrho_lt : rho < 1) (_hg : 0 ≤ g)
    (n : ℕ) (R : ℕ → ℝ) (hR : ∀ j ∈ Finset.range n, |R j| ≤ C * rho ^ j) :
    (∑ j ∈ Finset.range n, |R j|) ≤ C / (1 - rho) := by
  have hbound := combes_thomas_geometric_bound rho hrho_ge hrho_lt n
  calc
    (∑ j ∈ Finset.range n, |R j|)
      ≤ ∑ j ∈ Finset.range n, (C * rho ^ j) := by
        apply Finset.sum_le_sum
        intro j hj
        exact hR j hj
    _ = C * (∑ j ∈ Finset.range n, rho ^ j) := by rw [← Finset.mul_sum]
    _ ≤ C * (1 / (1 - rho)) := mul_le_mul_of_nonneg_left hbound hC
    _ = C / (1 - rho) := by ring

/-! ## Polymer cluster expansion and Kotecký–Preiss bounds for G17

Scalar tree-bound and geometric convergence lemmas for polymer cluster activity.
These lemmas bound finite geometric sums. The underlying graph coordination,
actual plaquette activities, Hamiltonian interactions and strict
Kotecky-Preiss incompatibility budget remain analytic hypotheses.
-/

/-- A contraction factor rho < 1 bounds the sum of connected polymer clusters of size 1 to n:
    ∑_{j=0}^{n-1} rho ^ (j + 1) ≤ rho / (1 - rho). -/
theorem kotecky_preiss_cluster_sum_bound (rho : ℝ) (hrho_ge : 0 ≤ rho) (hrho_lt : rho < 1) (n : ℕ) :
    (∑ j ∈ Finset.range n, rho ^ (j + 1)) ≤ rho / (1 - rho) := by
  have hgeom := combes_thomas_geometric_bound rho hrho_ge hrho_lt n
  have hshift : (∑ j ∈ Finset.range n, rho ^ (j + 1)) = rho * (∑ j ∈ Finset.range n, rho ^ j) := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j _
    rw [pow_succ]
    ring
  rw [hshift]
  have hmul : rho * (∑ j ∈ Finset.range n, rho ^ j) ≤ rho * (1 / (1 - rho)) :=
    mul_le_mul_of_nonneg_left hgeom hrho_ge
  calc
    rho * (∑ j ∈ Finset.range n, rho ^ j) ≤ rho * (1 / (1 - rho)) := hmul
    _ = rho / (1 - rho) := by ring

/-- Substitute rho=D*w in the finite geometric bound. Identifying these scalar
terms with actual connected activities requires a separate construction. -/
theorem kotecky_preiss_polymer_activity_bound
    (D w : ℝ) (hD : 0 ≤ D) (hw : 0 ≤ w) (hbound : D * w < 1) (n : ℕ) :
    (∑ j ∈ Finset.range n, (D * w) ^ (j + 1)) ≤ (D * w) / (1 - (D * w)) := by
  have hrho_ge : 0 ≤ D * w := mul_nonneg hD hw
  exact kotecky_preiss_cluster_sum_bound (D * w) hrho_ge hbound n

/-- Triangle inequality for finite-volume free energy deviations across two volumes. -/
theorem polymer_free_energy_cauchy_bound
    (f1 f2 f_inf e1 e2 : ℝ)
    (h1 : |f1 - f_inf| ≤ e1)
    (h2 : |f2 - f_inf| ≤ e2) :
    |f1 - f2| ≤ e1 + e2 := by
  have heq : f1 - f2 = (f1 - f_inf) + (f_inf - f2) := by ring
  have hsymm : |f_inf - f2| = |f2 - f_inf| := abs_sub_comm f_inf f2
  calc
    |f1 - f2| = |(f1 - f_inf) + (f_inf - f2)| := by rw [heq]
    _ ≤ |f1 - f_inf| + |f_inf - f2| := abs_add_le (f1 - f_inf) (f_inf - f2)
    _ = |f1 - f_inf| + |f2 - f_inf| := by rw [hsymm]
    _ ≤ e1 + e2 := add_le_add h1 h2

/-! ## Wilson True-Vacuum Block Estimates (BA20–BA25) and SC17 Spatial Closure

Exact-rational and polynomial identities underlying the true-vacuum Brownian slab
and spatial-decay derivations. Analytic operator estimates, diffusion semigroups,
and Combes-Thomas decays remain separate hypotheses.
-/

/-- Pinned activity in the Brownian slab polymer expansion at alpha = 1 / 32000 (BA21). -/
theorem wilson_slab_pinned_activity :
    let alpha : ℚ := 1 / 32000
    let degree : ℚ := 84
    let x : ℚ := 8 * alpha
    x / (1 - 4 * degree * x) = 1 / 3664 := by
  norm_num

/-- Slab angle row and approximate-tensorization constant (BA25). -/
theorem wilson_slab_block_row_and_cat :
    let pinned : ℚ := 1 / 3664
    let row : ℚ := 160 * 3 * pinned
    row = 30 / 229 ∧
    1 - row = 199 / 229 ∧
    1 / (1 - row) = 229 / 199 ∧
    1 / (1 - row) < 29 / 25 := by
  norm_num

/-- SC17 sharp invariant barrier slack at lambda = 1 / 640, q = 17 / 16, row = 1 / 64. -/
theorem wilson_sc17_sharp_barrier :
    let lam : ℚ := 1 / 640
    let q : ℚ := 17 / 16
    let row : ℚ := 1 / 64
    let diag : ℚ := 3 * lam + 27 * lam ^ 2
    let source : ℚ := 12 * lam * q
    let slack : ℚ := (4 / 3 - 4 / 200) * row - 2 * row ^ 2 - source
    diag = 1947 / 409600 ∧
    diag < 1 / 200 ∧
    source = 51 / 2560 ∧
    slack = 17 / 153600 ∧
    0 < slack := by
  norm_num

/-- SC17 sharp curvature floor, angle row, and physical gap factor at lambda <= 1 / 640. -/
theorem wilson_sc17_sharp_curvature_and_gap :
    let rho : ℚ := 2 * (1 - 1 / 200 - 1 / 64)
    let kappa : ℚ := 2 * (1 / 64) / rho
    let cat : ℚ := 1 / (1 - kappa)
    let gap_factor : ℚ := 3 * (1 - kappa) * (1 - 33 / 1120)
    rho = 1567 / 800 ∧
    kappa = 25 / 1567 ∧
    cat = 1567 / 1542 ∧
    cat < 51 / 50 ∧
    57 / 20 < gap_factor := by
  norm_num

/-- SC17 broad invariant barrier slack at lambda = 1 / 73, q = 1025 / 1024, row = 2 / 7. -/
theorem wilson_sc17_broad_barrier :
    let lam : ℚ := 1 / 73
    let q : ℚ := 1025 / 1024
    let row : ℚ := 2 / 7
    let diag : ℚ := 3 * lam + 27 * lam ^ 2
    let source : ℚ := 12 * lam * q
    let slack : ℚ := (4 / 3 - 4 * diag) * row - 2 * row ^ 2 - source
    diag = 246 / 5329 ∧
    source = 12300 / 74752 ∧
    slack = 77375 / 200540928 ∧
    0 < slack := by
  norm_num

/-- SC17 broad curvature floor, angle row, and C_AT bound at lambda <= 1 / 73. -/
theorem wilson_sc17_broad_curvature_and_cat :
    let diag : ℚ := 246 / 5329
    let row : ℚ := 2 / 7
    let rho : ℚ := 2 * (1 - diag - row)
    let kappa : ℚ := 2 * row / rho
    let cat : ℚ := 1 / (1 - kappa)
    rho = 49846 / 37303 ∧
    4 / 3 < rho ∧
    kappa = 10658 / 24923 ∧
    cat = 24923 / 14265 ∧
    cat < 7 / 4 := by
  norm_num

/-- The exact threshold polynomial identity for the SC17 Volterra discriminant. -/
theorem wilson_sc17_barrier_polynomial (lam : ℚ) :
    let mu : ℚ := 4 / 3 - 12 * lam - 108 * lam ^ 2
    9 * (mu ^ 2 - 96 * lam) = 16 * (6561 * lam ^ 4 + 1458 * lam ^ 3 - 81 * lam ^ 2 - 72 * lam + 1) := by
  intro mu; ring

/-- The Volterra discriminant is strictly negative at lambda = 1 / 72. -/
theorem wilson_sc17_discriminant_negative_at_seventy_two :
    let lam : ℚ := 1 / 72
    let mu : ℚ := 4 / 3 - 12 * lam - 108 * lam ^ 2
    mu ^ 2 - 96 * lam = -47 / 2304 ∧
    mu ^ 2 - 96 * lam < 0 := by
  norm_num

end Workhouse
