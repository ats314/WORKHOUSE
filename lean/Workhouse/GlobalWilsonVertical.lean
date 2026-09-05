/-
Scalar kernel of the global Wilson fiber comparison.
The hypotheses below represent previously proved form/min-max comparisons.
This file does not formalize SU(N), elliptic operators, ground projections,
the spectral theorem, a full-block vacuum subtraction, or a volume limit.
-/
import Mathlib.Tactic

namespace Workhouse.GlobalWilsonVertical

/-- The actual strip metric scalar is positive; its kinetic loss is controlled
on the complete principal-root neighborhood eta in [0,1/2]. -/
theorem strip_factor (eta : ℝ) (h0 : 0 ≤ eta) (hhalf : eta ≤ 1 / 2) :
    let t := 1 / (1 + (8 / 3 : ℝ) * eta)
    0 < t ∧ t ≤ 1 ∧ t ≤ 1 - eta ∧
      1 - t ≤ (8 / 3 : ℝ) * eta ∧ 1 - t ≤ 3 * eta ∧ 3 / 7 ≤ t := by
  dsimp only
  have hd : 0 < 1 + (8 / 3 : ℝ) * eta := by positivity
  have ht0 : 0 < 1 / (1 + (8 / 3 : ℝ) * eta) := by positivity
  have ht1 : 1 / (1 + (8 / 3 : ℝ) * eta) ≤ 1 := by
    apply (div_le_iff₀ hd).2
    linarith
  have hteta : 1 / (1 + (8 / 3 : ℝ) * eta) ≤ 1 - eta := by
    apply (div_le_iff₀ hd).2
    nlinarith [mul_nonneg h0 (sub_nonneg.mpr hhalf)]
  have hid : 1 - 1 / (1 + (8 / 3 : ℝ) * eta) =
      (8 / 3 : ℝ) * eta * (1 / (1 + (8 / 3 : ℝ) * eta)) := by
    field_simp
    ring
  have hloss : 1 - 1 / (1 + (8 / 3 : ℝ) * eta) ≤ (8 / 3 : ℝ) * eta := by
    nlinarith [mul_nonneg h0 (sub_nonneg.mpr ht1)]
  have hthree : 1 - 1 / (1 + (8 / 3 : ℝ) * eta) ≤ 3 * eta := by linarith
  have hlow : (3 / 7 : ℝ) ≤ 1 / (1 + (8 / 3 : ℝ) * eta) := by
    apply (le_div_iff₀ hd).2
    linarith
  exact ⟨ht0, ht1, hteta, hloss, hthree, hlow⟩

/-- A scalar min-max lower input dominates the convex spectral cap. -/
theorem near_cap (a e u epsilon t eta : ℝ)
    (hu : 0 ≤ u) (hepsilon : epsilon ≤ 3 / 2)
    (ht0 : 0 ≤ t) (ht1 : t ≤ 1)
    (hloss : 1 - t ≤ (8 / 3 : ℝ) * eta)
    (hinput : t * e + 4 * u * eta ≤ a) :
    min e (epsilon * u) ≤ a := by
  have hw : 0 ≤ 1 - t := sub_nonneg.mpr ht1
  have hleft := mul_le_mul_of_nonneg_left (min_le_left e (epsilon * u)) ht0
  have hright := mul_le_mul_of_nonneg_left (min_le_right e (epsilon * u)) hw
  have hcap := mul_le_mul_of_nonneg_left hepsilon (mul_nonneg hw hu)
  have hbudget := mul_le_mul_of_nonneg_left hloss hu
  nlinarith

/-- Near-region affine comparison. The coefficient may be negative; no
large-coupling hypothesis is needed for this conclusion. -/
theorem near_affine (a e u epsilon v t eta : ℝ)
    (he : 0 ≤ e) (hu : 0 ≤ u) (hepsilon0 : 0 < epsilon)
    (hepsilon1 : epsilon ≤ 1) (heta : 0 ≤ eta)
    (hvlow : 3 * eta ≤ v) (hvhigh : v ≤ 4 * eta)
    (hloss : 1 - t ≤ 3 * eta)
    (hinput : t * e + 4 * u * eta ≤ a) :
    e + (u - e / epsilon) * v ≤ a := by
  have hv0 : 0 ≤ v := by linarith
  have hvdiv : v ≤ v / epsilon := by
    apply (le_div_iff₀ hepsilon0).2
    nlinarith [mul_nonneg hv0 (sub_nonneg.mpr hepsilon1)]
  have hlossdiv : 1 - t ≤ v / epsilon := by linarith
  have heprod := mul_le_mul_of_nonneg_left hlossdiv he
  have huprod := mul_le_mul_of_nonneg_left hvhigh hu
  have hdiv : (e / epsilon) * v = e * (v / epsilon) := by ring
  nlinarith

/-- The global product-potential barrier gives the same affine comparison
outside the principal-root neighborhood. -/
theorem far_affine (a e u epsilon v : ℝ)
    (he : 0 ≤ e) (hepsilon : 0 < epsilon) (hfar : epsilon ≤ v)
    (hinput : u * v ≤ a) :
    e + (u - e / epsilon) * v ≤ a := by
  have hvdiv : 1 ≤ v / epsilon := by
    apply (le_div_iff₀ hepsilon).2
    simpa using hfar
  have heprod := mul_le_mul_of_nonneg_left hvdiv he
  have hdiv : (e / epsilon) * v = e * (v / epsilon) := by ring
  nlinarith

/-- Assembly of the near and far inputs, applicable at each counted
eigenvalue index independently. No spectral argument is hidden here. -/
theorem spectral_from_split (a e u epsilon v : ℝ)
    (he : 0 ≤ e) (hu : 0 ≤ u)
    (hepsilon0 : 0 < epsilon) (hepsilon1 : epsilon ≤ 1)
    (hnear : v ≤ epsilon → ∃ eta : ℝ,
      0 ≤ eta ∧ eta ≤ 1 / 2 ∧ 3 * eta ≤ v ∧ v ≤ 4 * eta ∧
        (1 / (1 + (8 / 3 : ℝ) * eta)) * e + 4 * u * eta ≤ a)
    (hfar : epsilon ≤ v → u * v ≤ a) :
    min e (epsilon * u) ≤ a ∧ e + (u - e / epsilon) * v ≤ a := by
  by_cases hv : v ≤ epsilon
  · obtain ⟨eta, heta, hhalf, hvlow, hvhigh, hinput⟩ := hnear hv
    obtain ⟨ht0, ht1, _, hloss, hthree, _⟩ := strip_factor eta heta hhalf
    constructor
    · exact near_cap a e u epsilon _ eta hu (by linarith) (le_of_lt ht0)
        ht1 hloss hinput
    · exact near_affine a e u epsilon v _ eta he hu hepsilon0 hepsilon1
        heta hvlow hvhigh hthree hinput
  · have hregion : epsilon ≤ v := le_of_lt (lt_of_not_ge hv)
    constructor
    · calc
        min e (epsilon * u) ≤ epsilon * u := min_le_right _ _
        _ ≤ u * v := by nlinarith [mul_nonneg hu (sub_nonneg.mpr hregion)]
        _ ≤ a := hfar hregion
    · exact far_affine a e u epsilon v he hepsilon0 hregion (hfar hregion)

/-- Algebra after decomposing a vector into ground and orthogonal pieces.
The variables g and q stand for their nonnegative squared norms. -/
theorem two_sector_form (a0 a1 e0 e1 u epsilon v g q : ℝ)
    (he : e0 ≤ e1) (hepsilon : 0 < epsilon) (hv : 0 ≤ v)
    (hg : 0 ≤ g) (hq : 0 ≤ q)
    (hground : e0 + (u - e0 / epsilon) * v ≤ a0)
    (hexcited : e1 + (u - e1 / epsilon) * v ≤ a1) :
    e0 * (g + q) + (e1 - e0) * q +
      (u - e1 / epsilon) * v * (g + q) ≤ a0 * g + a1 * q := by
  have hdiv : e0 / epsilon ≤ e1 / epsilon :=
    div_le_div_of_nonneg_right he (le_of_lt hepsilon)
  have hscalar := mul_le_mul_of_nonneg_right hdiv hv
  have hground' : e0 + (u - e1 / epsilon) * v ≤ a0 := by nlinarith
  have hgp := mul_le_mul_of_nonneg_right hground' hg
  have hqp := mul_le_mul_of_nonneg_right hexcited hq
  nlinarith

/-- The twice-threshold condition leaves half the Wilson potential in the
same lower bound as the fast penalty. -/
theorem half_potential_threshold (u e epsilon : ℝ) (hepsilon : 0 < epsilon)
    (hthreshold : 2 * e ≤ epsilon * u) :
    u / 2 ≤ u - e / epsilon := by
  have hdiv : e / epsilon ≤ u / 2 := by
    apply (div_le_iff₀ hepsilon).2
    nlinarith
  linarith

/-- info: 'Workhouse.GlobalWilsonVertical.strip_factor' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms strip_factor
/-- info: 'Workhouse.GlobalWilsonVertical.near_cap' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms near_cap
/-- info: 'Workhouse.GlobalWilsonVertical.near_affine' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms near_affine
/-- info: 'Workhouse.GlobalWilsonVertical.far_affine' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms far_affine
/-- info: 'Workhouse.GlobalWilsonVertical.spectral_from_split' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms spectral_from_split
/-- info: 'Workhouse.GlobalWilsonVertical.two_sector_form' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms two_sector_form
/-- info: 'Workhouse.GlobalWilsonVertical.half_potential_threshold' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms half_potential_threshold

end Workhouse.GlobalWilsonVertical
