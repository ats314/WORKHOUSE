# Continuum-facing mechanism attempt: Riccati spine + scale-free geometric source terms (\(\sigma_*\))

## What this document establishes

It reconstructs the project’s proposed *continuum-relevant* mechanism:

- The effective action under a smoothing / RG-like semigroup has a Hessian evolving by a **matrix Riccati-type inequality**.
- The smallest horizontal Hessian eigenvalue can (in principle) be stabilized by an **\(a\)-independent positive source term** \(\sigma_*\).
- Two concrete candidates for \(\sigma_*\) are identified:
  1. Weyl-denominator (eigenvalue-repulsion) convexity on conjugacy-class variables.
  2. Orbit-volume / Faddeev–Popov determinant convexity near reducible strata.

This is a mechanism proposal with partial rigor: individual geometric lemmas are rigorous, but the connection to the full interacting Yang–Mills RG is not.

---

## 0. The problem the fixed-cutoff convexity window does not solve

The fixed-cutoff convexity parameter
\[
\rho_*(a,g)=c_0 a^2 g^2 - \frac{12}{g^2}
\]
cannot stay positive if \(g(a)\to 0\) as \(a\to 0\) (asymptotic freedom). Any continuum program needs an additional *scale-free* positivity input not of order \(a^2\).

The project’s answer: a nonlinear Hessian evolution with a positive “geometric/anomaly” source term.

---

## 1. Riccati spine: abstract discrete multiscale inequality (MFIP template)

Let \(\alpha_j\) denote the minimal horizontal convexity (smallest eigenvalue of the horizontal Hessian) at RG scale \(j\).

The project posits/derives a recurrence of the form
\[
\alpha_{j+1}\ \ge\ K\,\alpha_j \ -\ \varepsilon_j\ +\ \sigma_*,
\qquad 0<K<1,
\tag{MFIP}
\]
where:
- \(K\) is a “mixing/averaging” factor from blocking,
- \(\varepsilon_j\) is an erosion/error term (e.g. from bounded negative Hessian components),
- \(\sigma_*\) is a positive source term.

If \(\varepsilon_j\) is summable or uniformly small and \(\sigma_*>0\) is uniform in \(j\), then the recursion has a positive fixed point:
\[
\alpha_\infty \ \gtrsim\ \frac{\sigma_*}{1-K} - \text{(error)}.
\]

**Status.** (MFIP) is a *template*. The block-Hessian inequality provides the correct algebraic shape for one-step decimation, but a genuine RG for interacting YM is not constructed in the project.

---

## 2. Continuous surrogate: viscous Hamilton–Jacobi and Hessian Riccati inequality

A standard log-transform of heat flow yields viscous Hamilton–Jacobi (vHJ) for an effective potential \(S_t\):
\[
\partial_t S_t = \frac12 \Delta S_t - \frac12 \|\nabla S_t\|^2 + \text{(drift/source)}.
\]

Formally differentiating twice gives a matrix PDE/inequality for \(H_t:=\nabla^2 S_t\) of schematic form
\[
\partial_t H_t \approx \frac12 \Delta_L H_t \ -\ H_t^2\ +\ \mathcal R_t,
\]
where \(\Delta_L\) is a Lichnerowicz Laplacian on symmetric 2-tensors and \(\mathcal R_t\) collects curvature commutators and measure/quotient effects.

If one can prove a *tensor lower bound*
\[
\mathcal R_t\ \succeq\ \sigma_* I - \varepsilon(t) I,
\]
then the minimum eigenvalue \(\lambda_{\min}(H_t)\) satisfies a scalar Riccati inequality at the level of maxima/minima (via a tensor maximum principle),
\[
\dot \lambda \ \gtrsim\ -\lambda^2 + \sigma_* - \varepsilon(t).
\]

A positive \(\sigma_*\) then forces a positive long-time floor for \(\lambda\).

**Status.** This is the right conceptual geometry, but the project does not supply a complete derivation for lattice Yang–Mills under an actual RG; it uses vHJ as a surrogate model.

---

## 3. Candidate \(\sigma_*\) source I: Weyl denominator convexity (rigorous lemma)

Consider the pushforward of any **class function** density \(\rho(g)\,dg\) on \(SU(N)\) to conjugacy classes \(T/W\), in eigenangle coordinates \(\theta\).

By the Weyl integration formula, the density always includes a universal Jacobian factor
\[
|\Delta(\theta)|^2 = \prod_{i<j} 4\sin^2\!\frac{\theta_i-\theta_j}{2}.
\]

Define the geometric potential
\[
S_{\mathrm{geom}}(\theta) := -\log|\Delta(\theta)|^2
= -\sum_{i<j}\log\Big(4\sin^2\!\frac{\theta_i-\theta_j}{2}\Big).
\]

Then, on the regular set (no eigenvalue collisions),
\[
\delta^2 S_{\mathrm{geom}}(\theta)[x,x]
=\frac12\sum_{i<j}\csc^2\!\Big(\frac{\theta_i-\theta_j}{2}\Big)\,(x_i-x_j)^2.
\]

Since \(\csc^2(\cdot)\ge 1\) wherever finite, and restricting to the \(SU(N)\) tangent constraint \(\sum_i x_i=0\),
\[
\delta^2 S_{\mathrm{geom}}(\theta)[x,x] \ \ge\ \frac{N}{2}\,\|x\|^2.
\]

Thus:
\[
\nabla^2 S_{\mathrm{geom}}\big|_{\sum x_i=0}\ \succeq\ \frac{N}{2}\,I,
\]
with a constant independent of any smoothing scale.

**Status.** This bound is rigorous and scale-independent. It is, however, a statement about *conjugacy-class variables* for class functions; mapping it into an interacting lattice YM RG is nontrivial.

---

## 4. Candidate \(\sigma_*\) source II: orbit-volume / FP determinant convexity (partial)

On the irreducible stratum, the orbit metric Gram matrix is
\[
M(U)=D_U^*D_U,
\qquad
(D_U\xi)_b := \xi_x - \mathrm{Ad}_{U_b}\xi_y,
\]
so the orbit-volume density contains \(\sqrt{\det M(U)}\). The associated geometric potential is
\[
S_{\mathrm{orb}}(U):=-\tfrac12\log\det M(U).
\]

Matrix calculus gives
\[
\delta^2 S_{\mathrm{orb}}(U)
= -\tfrac12 \mathrm{Tr}\big(M^{-1}\delta^2 M\big)
+\tfrac12 \mathrm{Tr}\big(M^{-1}\delta M\,M^{-1}\delta M\big),
\]
and the second term is manifestly nonnegative (trace of a square).

Heuristic: as one approaches reducibles, \(M^{-1}\) blows up and the positive term can dominate, yielding strong convexity (“repulsive wall”) near singular strata.

**Status.**
- The decomposition is rigorous.
- Turning it into a uniform *lower bound* on \(\mathrm{Hess}\,S_{\mathrm{orb}}\) requires control of the “bad term” \(\mathrm{Tr}(M^{-1}\delta^2 M)\) and a quantified stratified analysis near reducibles. This is not completed.

---

## 5. What is missing to make this a constructive continuum mechanism

To promote “candidate \(\sigma_*\)” into an RG-stable curvature floor, one would need:

1. A concrete coarse-graining map producing effective actions where \(\sigma_*\) is visible in the *horizontal Hessian* of the physical effective action (not only in auxiliary variables).
2. A rigorous tensor maximum principle / comparison theorem on the relevant bundle that turns the matrix PDE/recurrence into a scalar inequality for \(\lambda_{\min}\).
3. Uniform control of error/erosion terms \(\varepsilon_j\) or \(\varepsilon(t)\) (summable or strictly dominated).
4. Control of reducible strata (polarity/capacity) in a form compatible with the chosen Dirichlet form and the RG map.

At present, the Weyl denominator piece is the cleanest *mathematically explicit* scale-free convexity contribution; the orbit-volume/FP determinant is the cleanest *structurally aligned* candidate for the lattice orbit space, but its quantitative convexity remains conjectural.

---

## Internal sources in this project

Primary modules:
- `06_Riccati_Spine_Module.md`, `01_curvature_rg_riccati_hotrg.md`, `YANG3_02_vHJ_hessian_flow_riccati.md`
- `07_heat_kernel_weyl_denominator_scale_independent_sigma_geom.md`
- `06_fp_weyl_determinant_orbit_space_hessian.md`
- `RECOMMENDED_10_YM_Core_Specialization_FP_and_Dirichlet(1).md`
