# September 10 upstream scalar proof inventory

Integration repair against main cf84a46564ec8ed44d30490c6173d23883bde6e4.
The preceding main merges added the declarations below without registering them or
refreshing the kernel export. This note preserves the exact encoded hypotheses and
conclusions for that repair. It adds no physical theorem and is separate from the
[antipodal magnetic review](w6-antipodal-magnetic-geometry.md).

The Lean proofs remain unchanged. Each displayed signature is transcribed from its
existing declaration. The associated whole source arguments retain their own
analytic status; these links describe only the compiled ingredients.

## U1 Tilted KP scalar ingredients

Scalar tilted-activity, geometric-series, coupling-window, logarithm and source-radius inequalities under their displayed real-number hypotheses. The source-parameter formulas are definitions; their Wilson activity, Hamiltonian or spectral identifications are separate.

Source: [the unchanged module](../../lean/Workhouse/PolymerCluster.lean).

### tiltedKpParameter_nonneg

~~~lean
theorem tiltedKpParameter_nonneg (D beta c alpha : ℝ) (hD : 0 ≤ D) (hbeta : 0 ≤ beta) :
    0 ≤ tiltedKpParameter D beta c alpha
~~~

### tiltedKpParameter_at_alpha_zero

~~~lean
theorem tiltedKpParameter_at_alpha_zero (D beta c : ℝ) :
    tiltedKpParameter D beta c 0 = weightedActivityBase D beta c
~~~

### strict_kp_criterion_lt_one

~~~lean
theorem strict_kp_criterion_lt_one (x c : ℝ) (hc : 0 ≤ c) (hxc : x ≤ c / (1 + c)) :
    x < 1
~~~

### strict_kotecky_preiss_criterion

~~~lean
theorem strict_kotecky_preiss_criterion (x c : ℝ) (hc : 0 ≤ c) (_hx0 : 0 ≤ x)
    (hxc : x ≤ c / (1 + c)) :
    x / (1 - x) ≤ c
~~~

### strict_kotecky_preiss_iff

~~~lean
theorem strict_kotecky_preiss_iff (x c : ℝ) (hc : 0 ≤ c) (hx0 : 0 ≤ x) (hx1 : x < 1) :
    x / (1 - x) ≤ c ↔ x ≤ c / (1 + c)
~~~

### tilted_kotecky_preiss_tree_bound

~~~lean
theorem tilted_kotecky_preiss_tree_bound (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 ≤ D)
    (hbeta : 0 ≤ beta) (hcond : tiltedKpParameter D beta c alpha ≤ c / (1 + c)) :
    tiltedKpParameter D beta c alpha / (1 - tiltedKpParameter D beta c alpha) ≤ c
~~~

### tilted_kotecky_preiss_convergent

~~~lean
theorem tilted_kotecky_preiss_convergent (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 ≤ D)
    (hbeta : 0 ≤ beta) (hcond : tiltedKpParameter D beta c alpha ≤ c / (1 + c)) :
    HasSum (fun n : ℕ => (tiltedKpParameter D beta c alpha) ^ (n + 1))
      (tiltedKpParameter D beta c alpha / (1 - tiltedKpParameter D beta c alpha))
~~~

### betaStabilityWindow_pos

~~~lean
theorem betaStabilityWindow_pos (D c alpha : ℝ) (hD : 0 < D) (hc : 0 < c) :
    0 < betaStabilityWindow D c alpha
~~~

### beta_le_window_implies_tiltedKp_le

~~~lean
theorem beta_le_window_implies_tiltedKp_le (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 < D)
    (_hbeta : 0 ≤ beta) (hwin : beta ≤ betaStabilityWindow D c alpha) :
    tiltedKpParameter D beta c alpha ≤ c / (1 + c)
~~~

### beta_le_window_implies_tree_bound

~~~lean
theorem beta_le_window_implies_tree_bound (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 < D)
    (hbeta : 0 ≤ beta) (hwin : beta ≤ betaStabilityWindow D c alpha) :
    tiltedKpParameter D beta c alpha / (1 - tiltedKpParameter D beta c alpha) ≤ c
~~~

### cluster_free_energy_density_bound_le

~~~lean
theorem cluster_free_energy_density_bound_le (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 ≤ D)
    (hbeta : 0 ≤ beta) (hcond : tiltedKpParameter D beta c alpha ≤ c / (1 + c)) :
    clusterFreeEnergyDensityBound D beta c alpha ≤ |alpha| / 2 + c
~~~

### cluster_free_energy_density_bound_le_window

~~~lean
theorem cluster_free_energy_density_bound_le_window (D beta c alpha : ℝ) (hc : 0 ≤ c) (hD : 0 < D)
    (hbeta : 0 ≤ beta) (hwin : beta ≤ betaStabilityWindow D c alpha) :
    clusterFreeEnergyDensityBound D beta c alpha ≤ |alpha| / 2 + c
~~~

### cluster_free_energy_density_bound_nonneg

~~~lean
theorem cluster_free_energy_density_bound_nonneg (D beta c alpha : ℝ) (hD : 0 ≤ D)
    (hbeta : 0 ≤ beta) (hc : 0 ≤ c) (hcond : tiltedKpParameter D beta c alpha ≤ c / (1 + c)) :
    0 ≤ clusterFreeEnergyDensityBound D beta c alpha
~~~

### clusterMassGap_pos

~~~lean
theorem clusterMassGap_pos (x : ℝ) (hx0 : 0 < x) (hx1 : x < 1) :
    0 < clusterMassGap x
~~~

### clusterMassGap_ge_log_kp

~~~lean
theorem clusterMassGap_ge_log_kp (x c : ℝ) (hx0 : 0 < x) (hc : 0 < c)
    (hxc : x ≤ c / (1 + c)) :
    Real.log ((1 + c) / c) ≤ clusterMassGap x
~~~

### log_one_add_div_pos

~~~lean
theorem log_one_add_div_pos (c : ℝ) (hc : 0 < c) :
    0 < Real.log ((1 + c) / c)
~~~

### clusterMassGap_pos_of_strict_kp

~~~lean
theorem clusterMassGap_pos_of_strict_kp (x c : ℝ) (hx0 : 0 < x) (hc : 0 < c)
    (hxc : x ≤ c / (1 + c)) :
    0 < clusterMassGap x
~~~

### cluster_correlation_exponential_decay

~~~lean
theorem cluster_correlation_exponential_decay (x : ℝ) (hx0 : 0 < x) (d : ℕ) :
    x ^ d = Real.exp (- ((d : ℝ) * clusterMassGap x))
~~~

### uniform_source_radius_bound_le

~~~lean
theorem uniform_source_radius_bound_le (C0 x c : ℝ) (hC0 : 0 ≤ C0) (hc : 0 ≤ c)
    (_hx0 : 0 ≤ x) (hxc : x ≤ c / (1 + c)) :
    uniformSourceRadiusBound C0 x ≤ Real.sqrt (C0 * (1 + c))
~~~

### uniform_source_radius_bound_nonneg

~~~lean
theorem uniform_source_radius_bound_nonneg (C0 x : ℝ) :
    0 ≤ uniformSourceRadiusBound C0 x
~~~

### uniform_source_radius_bound_le_window

~~~lean
theorem uniform_source_radius_bound_le_window (D beta c alpha C0 : ℝ) (hC0 : 0 ≤ C0) (hc : 0 ≤ c)
    (hD : 0 < D) (hbeta : 0 ≤ beta) (hwin : beta ≤ betaStabilityWindow D c alpha) :
    uniformSourceRadiusBound C0 (tiltedKpParameter D beta c alpha) ≤ Real.sqrt (C0 * (1 + c))
~~~

## U2 Coercivity scalar ingredients

Real-number curvature/coercivity arithmetic under the stated inequalities. The Bochner-named lemma adds a nonnegative square to real numbers. The scale hierarchy is bounded by L_max; no positive floor over unbounded L is encoded.

Source: [the unchanged module](../../lean/Workhouse/BakryEmeryCoercivity.lean).

### quantum_curvature_restoration

~~~lean
theorem quantum_curvature_restoration (ric hess_u rho : ℝ)
    (hdom : -ric + rho ≤ 2 * hess_u) :
    rho ≤ ricInftyLowerBound ric hess_u
~~~

### ricInfty_pos_of_quantum_restoration

~~~lean
theorem ricInfty_pos_of_quantum_restoration (ric hess_u rho : ℝ)
    (hrho : 0 < rho) (hdom : -ric + rho ≤ 2 * hess_u) :
    0 < ricInftyLowerBound ric hess_u
~~~

### bochner_gamma2_lower_bound

~~~lean
theorem bochner_gamma2_lower_bound (eps rho hess_sq grad_sq : ℝ)
    (_heps : 0 ≤ eps) (_hrho : 0 ≤ rho) (hhess : 0 ≤ hess_sq) (_hgrad : 0 ≤ grad_sq) :
    eps ^ 2 * rho * grad_sq ≤ eps ^ 2 * hess_sq + eps ^ 2 * rho * grad_sq
~~~

### coercivityConstant_pos

~~~lean
theorem coercivityConstant_pos (rho : ℝ) (hrho : 0 < rho) :
    0 < coercivityConstant rho
~~~

### coercivityConstant_lt_one

~~~lean
theorem coercivityConstant_lt_one (rho : ℝ) (hrho : 0 < rho) :
    coercivityConstant rho < 1
~~~

### coercivityConstant_mono

~~~lean
theorem coercivityConstant_mono (rho1 rho2 : ℝ) (h1 : 0 ≤ rho1) (hle : rho1 ≤ rho2) :
    coercivityConstant rho1 ≤ coercivityConstant rho2
~~~

### form_coercivity_bound

~~~lean
theorem form_coercivity_bound (T V H rho : ℝ)
    (hT : 0 ≤ T) (hV : 0 ≤ V) (hrho : 0 < rho) (hgap : rho * V ≤ H) :
    coercivityConstant rho * (T + V) ≤ T + H
~~~

### quantum_restoration_ratio_gt_one

~~~lean
theorem quantum_restoration_ratio_gt_one (cA sqrt33 L_sqrt : ℝ)
    (hcA : 2 ≤ cA) (h33 : 5 ≤ sqrt33) (hL : 1 ≤ L_sqrt) :
    1 < quantumRestorationRatio cA sqrt33 L_sqrt
~~~

### volume_uniform_rho_pos

~~~lean
theorem volume_uniform_rho_pos (rho0 L : ℝ) (hrho0 : 0 < rho0) (hL : 0 < L) :
    0 < rho0 / L ^ 2
~~~

### volume_uniform_coercivity_hierarchy

~~~lean
theorem volume_uniform_coercivity_hierarchy (rho0 L L_max : ℝ)
    (hrho0 : 0 < rho0) (hLpos : 0 < L) (hLle : L ≤ L_max) :
    coercivityConstant (rho0 / L_max ^ 2) ≤ coercivityConstant (rho0 / L ^ 2)
~~~

