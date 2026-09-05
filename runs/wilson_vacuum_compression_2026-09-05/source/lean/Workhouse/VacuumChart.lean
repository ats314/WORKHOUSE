/-
# Algebraic kernel of the second-order Wilson vacuum chart

Source: paper/research_notes/G18_SECOND_ORDER_WILSON_VACUUM_CHART_20260905.md,
Lemmas 3.1 and 4.1. These finite-matrix theorems expose all hypotheses:
Hermitian D and A, a normalized fixed vacuum, an orthogonal vector chi, and
the equation chi - D chi = A Omega. They construct the anti-Hermitian
rank-two generator and prove that the corrected coefficient kills both
vacuum legs. No inverse existence, norm estimate, Taylor expansion,
locality, thermodynamic limit, or SU(N) input is asserted here.

The endpoint-disjoint identity below is a separate field identity for the
discrete-time resolvent weights, including the mixed magnetic kick.
-/
import Mathlib.LinearAlgebra.Matrix.ConjTranspose
import Mathlib.Tactic

namespace Workhouse.VacuumChart

open Matrix

variable {n R : Type*} [Fintype n] [CommRing R] [StarRing R]

/-- The rank-one matrix |u><v|, over a commutative star ring. -/
def rankOne (u v : n → R) : Matrix n n R := vecMulVec u (star v)

/-- The vacuum rotation generator |chi><Omega| - |Omega><chi|. -/
def generator (Ω χ : n → R) : Matrix n n R := rankOne χ Ω - rankOne Ω χ

/-- The second-order coefficient after the commutator correction. -/
def corrected (D A : Matrix n n R) (Ω χ : n → R) : Matrix n n R :=
  A + (D * generator Ω χ - generator Ω χ * D)

omit [Fintype n] in
theorem rankOne_adjoint (u v : n → R) : (rankOne u v)ᴴ = rankOne v u := by
  simp [rankOne]

omit [Fintype n] in
theorem generator_antihermitian (Ω χ : n → R) :
    (generator Ω χ)ᴴ = -generator Ω χ := by
  simp [generator, rankOne_adjoint, neg_sub]

/-- Normalization and orthogonality make the generator's vacuum column chi. -/
theorem generator_vacuum (Ω χ : n → R)
    (hnorm : star Ω ⬝ᵥ Ω = 1) (horth : star χ ⬝ᵥ Ω = 0) :
    generator Ω χ *ᵥ Ω = χ := by
  simp [generator, rankOne, sub_mulVec, vecMulVec_mulVec, hnorm, horth]

/-- A Hermitian fixed-vacuum matrix also fixes the adjoint vacuum row. -/
theorem fixed_vacuum_row (D : Matrix n n R) (Ω : n → R)
    (hD : Dᴴ = D) (hfixed : D *ᵥ Ω = Ω) : star Ω ᵥ* D = star Ω := by
  rw [← hD, ← star_mulVec, hfixed]

/-- The resolvent equation forces scalar vacuum cancellation; no
orthogonality of chi is needed for this consequence. -/
theorem scalar_vacuum_cancellation (D A : Matrix n n R) (Ω χ : n → R)
    (hD : Dᴴ = D) (hfixed : D *ᵥ Ω = Ω)
    (hsolve : χ - D *ᵥ χ = A *ᵥ Ω) : star Ω ⬝ᵥ (A *ᵥ Ω) = 0 := by
  rw [← hsolve, dotProduct_sub, dotProduct_mulVec, fixed_vacuum_row D Ω hD hfixed,
    sub_self]

/-- The commutator cancels the entire vacuum column, beyond its scalar part. -/
theorem corrected_vacuum_column (D A : Matrix n n R) (Ω χ : n → R)
    (hnorm : star Ω ⬝ᵥ Ω = 1) (horth : star χ ⬝ᵥ Ω = 0)
    (hfixed : D *ᵥ Ω = Ω) (hsolve : χ - D *ᵥ χ = A *ᵥ Ω) :
    corrected D A Ω χ *ᵥ Ω = 0 := by
  rw [corrected, add_mulVec, sub_mulVec, ← mulVec_mulVec, ← mulVec_mulVec,
    generator_vacuum Ω χ hnorm horth, hfixed, generator_vacuum Ω χ hnorm horth,
    ← hsolve]
  abel

theorem corrected_hermitian (D A : Matrix n n R) (Ω χ : n → R)
    (hD : Dᴴ = D) (hA : Aᴴ = A) : (corrected D A Ω χ)ᴴ = corrected D A Ω χ := by
  simp only [corrected, conjTranspose_add, conjTranspose_sub, conjTranspose_mul,
    hD, hA, generator_antihermitian, neg_mul, mul_neg]
  abel

/-- Both vacuum projector legs vanish for the explicitly constructed
correction. The equation for chi is an explicit premise, not a new axiom. -/
theorem corrected_vacuum_legs (D A : Matrix n n R) (Ω χ : n → R)
    (hD : Dᴴ = D) (hA : Aᴴ = A)
    (hnorm : star Ω ⬝ᵥ Ω = 1) (horth : star χ ⬝ᵥ Ω = 0)
    (hfixed : D *ᵥ Ω = Ω) (hsolve : χ - D *ᵥ χ = A *ᵥ Ω) :
    corrected D A Ω χ * rankOne Ω Ω = 0 ∧
      rankOne Ω Ω * corrected D A Ω χ = 0 := by
  have hcol := corrected_vacuum_column D A Ω χ hnorm horth hfixed hsolve
  have hrow : star Ω ᵥ* corrected D A Ω χ = 0 := by
    rw [← corrected_hermitian D A Ω χ hD hA, ← star_mulVec, hcol, star_zero]
  constructor
  · simp [rankOne, mul_vecMulVec, hcol]
  · simp [rankOne, vecMulVec_mul, hrow]

/-- Exact disjoint-support cancellation for endpoint transfer weights.
Source: G18_WILSON_ENDPOINT_GAUGE_AND_MAJORANT_20260905.md, equation (11).
With x = exp(tau E1), y = exp(tau E2), the three denominators correspond
to E1, E2, and E1 + E2. This theorem is only the rational identity;
it makes no claim about exponential representations or energy spectra.
The additional tau term is the mixed magnetic kick. -/
theorem endpoint_disjoint_cancellation {K : Type*} [Field K] (τ x y : K)
    (hx : x ≠ 1) (hy : y ≠ 1) (hxy : x * y ≠ 1) :
    (τ / (x * y - 1)) * (τ / (x - 1) + τ / (y - 1) + τ) =
      (τ / (x - 1)) * (τ / (y - 1)) := by
  field_simp [sub_ne_zero.mpr hx, sub_ne_zero.mpr hy, sub_ne_zero.mpr hxy]
  ring

/-- info: 'Workhouse.VacuumChart.corrected_vacuum_legs' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms corrected_vacuum_legs

/-- info: 'Workhouse.VacuumChart.scalar_vacuum_cancellation' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms scalar_vacuum_cancellation

/-- info: 'Workhouse.VacuumChart.endpoint_disjoint_cancellation' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms endpoint_disjoint_cancellation

end Workhouse.VacuumChart
