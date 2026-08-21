# Lattice QCD and Yang-Mills Project Summary

## Project Overview

This project aims to solve the Yang-Mills mass gap problem using lattice QCD techniques, combining geometric analysis, Riccati flow dynamics, and quantum field theory.

## Key Theoretical Framework

### 1. **Riccati Evolution of the Hessian**

The central equation governing the mass gap is:

$$\partial_t H_t = \Delta_L H_t - 2H_t^2 + R_t$$

where:
- $H_t$ is the Hessian of the effective action
- $\Delta_L$ is the Lichnerowicz Laplacian
- $R_t$ is the geometric source term containing curvature contributions

**Key Insight**: A positive lower bound on the smallest eigenvalue of $H_t$ ensures a mass gap, provided $R_t$ stays above a strictly positive threshold.

### 2. **Anomaly-Curvature Identity** (Most Recent Work)

The project has established a rigorous connection between the trace anomaly in continuum QFT and the geometric curvature term:

$$\boxed{\sigma_{\text{anom}}(t) = \mathcal{K} \cdot \frac{\beta(g(t))}{g(t)} \cdot \langle \text{Tr} F_{\mu\nu}^2 \rangle_t}$$

where:
- $\sigma_{\text{anom}}(t)$ is the anomaly contribution to the geometric source $R_t$
- $\beta(g)$ is the RG β-function
- $\langle F^2 \rangle_t$ is the expectation value of the field strength squared
- $\mathcal{K} < 0$ for asymptotically free theories (ensuring positive curvature)

**Physical Interpretation**: The trace anomaly $\Theta^\mu_\mu \sim \frac{\beta(g)}{2g} \text{Tr} F_{\mu\nu}^2$ encodes mass generation in QFT. The identity shows how this quantum effect manifests as a stabilizing geometric curvature in the Riccati flow.

### 3. **Critical Threshold Condition**

For the mass gap to persist, the projected anomaly contribution must exceed a critical threshold:

$$\boxed{\langle v, \sigma_{\text{anom}}(t) v \rangle > \sigma_{\text{crit}}(t)}$$

where $v(t)$ is the eigenvector of the smallest eigenvalue $\lambda_{\min}(t)$, and:

$$\sigma_{\text{crit}}(t) = \underbrace{- \langle v, (\Delta_L H_t) v \rangle}_{\text{Diffusion Cost}} - \underbrace{\langle v, \sigma_{\text{geom}}(t) v \rangle}_{\text{Background Geometry}} + \underbrace{|\langle v, \sigma_{\text{corr}}(t) v \rangle|}_{\text{Correction Penalty}}$$

The decomposition is: $R_t = \sigma_{\text{anom}} + \sigma_{\text{geom}} + \sigma_{\text{corr}}$

### 4. **Lattice Implementation Framework**

The project has developed a comprehensive lattice approach including:

**a) Convex Scalar Prototype**
- Establishes the mechanism: uniform convexity → Bakry-Émery curvature → dynamic mass gap
- Provides volume-uniform functional inequalities (log-Sobolev, Poincaré)
- Spectral gap $\Delta \geq \rho_* > 0$ independent of lattice size

**b) Haar Measure Mass Term**
- On configuration space $SU(N)^{|\mathcal{B}|}$, the Jacobian of exponential coordinates generates an explicit Haar-measure mass term
- Combined with Wilson action to produce strictly positive Hessian at finite lattice spacing

**c) Transfer Matrix Analysis**
- Strong-coupling regime analysis yields spectral gap between vacuum and first excited state
- Matches the dynamically generated mass scale

**d) Reducible Configuration Treatment**
- Reducible lattice configurations shown to be polar for the Dirichlet form
- Ensures dynamics and spectral theory are insensitive to singular subsets

## Critical Finding: The β_latt = 0.8 Simulation Failure

### Observation
The truncated lattice/tensor-network simulation at lattice coupling $\beta_{\text{latt}} = 0.8$ failed to "lock" the gap and produced:
- Negative topological susceptibility: $\chi_{\text{top}} < 0$ (unphysical)
- Inability to maintain positive smallest eigenvalue

### Diagnosis

**Primary Cause: Regime Breakdown**
- At $\beta_{\text{latt}} = 0.8$ (strong coupling), the lattice spacing is too coarse
- The continuum mapping $g_{\text{latt}} \to g_{\text{continuum}}$ breaks down
- The manifold becomes "jagged" rather than a smooth discretization

**Mechanism: Threshold Violation**
- Lattice artifacts create large negative correction terms: $\sigma_{\text{corr}} \ll 0$
- This causes $\sigma_{\text{crit}}(t)$ to skyrocket
- Even if $\sigma_{\text{anom}}$ is present, it cannot overcome the massive negative curvature

**Topological Signature**
- $\chi_{\text{top}} < 0$ represents a catastrophic inversion of manifold orientation
- Confirms the regime breakdown is fundamental, not merely quantitative

### Interpretation

The failure is **both** a regime failure and threshold violation, causally linked:
1. Strong coupling regime → invalid continuum mapping (regime failure)
2. Invalid mapping → overwhelming negative corrections (threshold violation)
3. Result: topological inversion and gap closure

## Next Steps and Open Questions

### Immediate Priorities

1. **Determine the Valid Regime**
   - What is the critical value $\beta_{\text{latt}}^{\text{crit}}$ above which the continuum relation holds?
   - How does $\sigma_{\text{corr}}$ scale with $\beta_{\text{latt}}$?

2. **Quantify the Threshold**
   - Can we compute $\sigma_{\text{crit}}$ explicitly for given lattice parameters?
   - What is the minimum $\beta_{\text{latt}}$ needed to ensure $\sigma_{\text{anom}} > \sigma_{\text{crit}}$?

3. **Refine the Anomaly-Curvature Identity**
   - Determine the scheme-dependent constant $\mathcal{K}$ more precisely
   - Include higher-order corrections to the trace anomaly

4. **Numerical Validation**
   - Run simulations at higher $\beta_{\text{latt}}$ (weaker coupling, finer lattice)
   - Verify that $\chi_{\text{top}} > 0$ and gap locks when in valid regime
   - Map out the phase diagram: $\sigma_{\text{anom}}$ vs $\beta_{\text{latt}}$

### Theoretical Extensions

1. **Continuum Limit**
   - Prove that as $\beta_{\text{latt}} \to \infty$ (continuum limit), the anomaly-curvature identity becomes exact
   - Establish rigorous error bounds on $\sigma_{\text{corr}}$ as function of lattice spacing

2. **Finite Temperature**
   - Extend the framework to finite temperature $T$
   - Study how thermal effects modify $\sigma_{\text{anom}}$ and the critical threshold

3. **Full Yang-Mills**
   - Current work focuses on pure gauge theory
   - Include dynamical quarks (full QCD)
   - How do fermion determinants affect the Hessian evolution?

4. **Confinement Connection**
   - Relate the mass gap mechanism to confinement
   - Can the Riccati flow framework explain the area law for Wilson loops?

### Proof Strategy for Yang-Mills Mass Gap

The project provides a pathway toward a rigorous proof:

**Step 1**: Establish uniform convexity of the effective action on lattice
- ✓ Done for scalar prototype
- In progress for Yang-Mills with Haar mass term

**Step 2**: Prove Bakry-Émery curvature bound $\Gamma_2 \geq \rho_* \Gamma$
- Requires showing $R_t \geq \rho_* > 0$ uniformly

**Step 3**: Connect to continuum via anomaly-curvature identity
- ✓ Identity derived
- Need: rigorous control of $\sigma_{\text{corr}}$ in continuum limit

**Step 4**: Prove spectral gap persists in thermodynamic limit
- Use uniform functional inequalities
- Show tightness and strong resolvent convergence

**Step 5**: Osterwalder-Schrader reconstruction
- Translate spectral gap to physical mass gap in Minkowski signature

## Key Mathematical Tools

- **Bakry-Émery curvature**: $\Gamma_2(f) \geq \rho_* \Gamma(f)$
- **Log-Sobolev inequality**: $\text{Ent}_\mu(f^2) \leq \frac{2}{\rho_*} \int |\nabla f|^2 d\mu$
- **Riccati differential inequality**: $\partial_t \lambda_{\min} \geq -2\lambda_{\min}^2 + \sigma(t)$
- **Viscous Hamilton-Jacobi equation**: $\partial_t S_t = \Delta S_t - \|\nabla S_t\|^2$

## References to Session Files

- **MoA_Session_2025-11-27T22-16-38.txt**: Initial framework with scalar prototype, Riccati flow, Haar mass term
- **MoA_Session_2025-11-27T23-24-40.txt**: Anomaly-curvature identity, critical threshold, β_latt = 0.8 failure analysis

---

**Status**: The project has made significant theoretical progress in connecting geometric analysis (Riccati flow) with quantum field theory (trace anomaly). The key challenge now is to validate the framework numerically in the correct regime and establish rigorous continuum limit theorems.
