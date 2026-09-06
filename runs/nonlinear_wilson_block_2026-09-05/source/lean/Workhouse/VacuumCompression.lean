/-
# Exact compression of the corrected vacuum coefficient

For the rank-two generator constructed in VacuumChart, the corrected
coefficient is exactly Q A Q, where Q = 1 - |Omega><Omega|. This proves
the finite-matrix algebra behind the sharper operator-norm estimate.

The compression identity needs only Hermitian D and A, D Omega = Omega,
and chi - D chi = A Omega. Normalization and orthogonality of chi are
unnecessary for the equality itself. Normalization makes the rank-one
matrix an orthogonal projection; that property is also proved below.
This file does not formalize an operator norm or an infinite-dimensional
extension, and does not supply the resolvent equation as a new axiom.
-/
import Workhouse.VacuumChart

namespace Workhouse.VacuumCompression

open Matrix Workhouse.VacuumChart

variable {n R : Type*} [Fintype n] [CommRing R] [StarRing R]

/-- A normalized vacuum defines a Hermitian idempotent rank-one matrix. -/
theorem vacuum_projection (Ω : n → R) (hnorm : star Ω ⬝ᵥ Ω = 1) :
    (rankOne Ω Ω)ᴴ = rankOne Ω Ω ∧ rankOne Ω Ω * rankOne Ω Ω = rankOne Ω Ω := by
  constructor
  · exact rankOne_adjoint Ω Ω
  · simp [rankOne, vecMulVec_mul_vecMulVec, hnorm]

/-- The resolvent equation makes the scalar vacuum corner vanish. -/
theorem vacuum_corner_zero (D A : Matrix n n R) (Ω χ : n → R)
    (hD : Dᴴ = D) (hfixed : D *ᵥ Ω = Ω)
    (hsolve : χ - D *ᵥ χ = A *ᵥ Ω) :
    rankOne Ω Ω * A * rankOne Ω Ω = 0 := by
  rw [rankOne, vecMulVec_mul, vecMulVec_mul_vecMulVec, ← dotProduct_mulVec,
    scalar_vacuum_cancellation D A Ω χ hD hfixed hsolve]
  simp

/-- The commutator subtracts precisely the two vacuum row/column terms. -/
theorem corrected_eq_sub_vacuum_terms (D A : Matrix n n R) (Ω χ : n → R)
    (hD : Dᴴ = D) (hA : Aᴴ = A) (hfixed : D *ᵥ Ω = Ω)
    (hsolve : χ - D *ᵥ χ = A *ᵥ Ω) :
    corrected D A Ω χ = A - A * rankOne Ω Ω - rankOne Ω Ω * A := by
  have hχrow : star χ ᵥ* D = star (D *ᵥ χ) := by
    rw [← hD, ← star_mulVec, hD]
  have hArow : star Ω ᵥ* A = star (A *ᵥ Ω) := by
    rw [← hA, ← star_mulVec, hA]
  simp only [corrected, generator, rankOne, mul_sub, sub_mul, mul_vecMulVec,
    vecMulVec_mul, hfixed, fixed_vacuum_row D Ω hD hfixed, hχrow, hArow, ← hsolve,
    star_sub, sub_vecMulVec, vecMulVec_sub]
  abel

/-- The corrected coefficient is exactly the complementary compression.
All analytic work is outside this algebraic identity's explicit hypotheses. -/
theorem corrected_eq_compression [DecidableEq n] (D A : Matrix n n R) (Ω χ : n → R)
    (hD : Dᴴ = D) (hA : Aᴴ = A) (hfixed : D *ᵥ Ω = Ω)
    (hsolve : χ - D *ᵥ χ = A *ᵥ Ω) :
    corrected D A Ω χ = (1 - rankOne Ω Ω) * A * (1 - rankOne Ω Ω) := by
  rw [corrected_eq_sub_vacuum_terms D A Ω χ hD hA hfixed hsolve]
  rw [sub_mul, one_mul, mul_sub, mul_one, sub_mul,
    vacuum_corner_zero D A Ω χ hD hfixed hsolve]
  abel

/-- info: 'Workhouse.VacuumCompression.corrected_eq_compression' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms corrected_eq_compression

/-- info: 'Workhouse.VacuumCompression.vacuum_projection' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms vacuum_projection

end Workhouse.VacuumCompression
