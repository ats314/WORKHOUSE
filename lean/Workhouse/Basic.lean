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

end Workhouse
