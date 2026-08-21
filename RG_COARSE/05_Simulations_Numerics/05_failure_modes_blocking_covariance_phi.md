# Failure Modes That Are Probably Not Physics (Blocking, Covariance, φ-Hessian)

This document isolates three “red flag” clusters that can fabricate fake obstructions if treated as physical conclusions.

---

## 1. Blocking can worsen curvature drastically

A blocking diagnostic reports:

- fine lattice: \(\lambda_{\min}\) around \(-36\) to \(-40\),
- blocked lattice: \(\lambda_{\min}\) around \(-38\) to \(-44\),
- \(\Phi_{\text{fine}}\approx 39.6\), \(\Phi_{\text{block}}\approx 68.3\), \(\Delta\Phi\approx 28.7\).

This is not a subtle effect. If a coarse-graining map increases defects and makes \(\lambda_{\min}\) more negative, then “convexity survives blocking” is not true for that map (or for that measurement pipeline).

Actionable conclusion: **blocking needs its own projection + invariant harness** (just like Maxwell).

---

## 2. “H_expect − Cov” with *uniform* covariance weights is a known-bad baseline

A coarse-graining experiment computes a “coarse Hessian” via:
\[
H_{\text{coarse}} = \mathbb{E}[H] - \mathrm{Cov}(\nabla),
\]
but the covariance term is assembled with **uniform weights** in at least one run.

The same run reports that the minimum eigenvalue plunges strongly negative, e.g.:

- \(\ell=0.333\): \(\lambda_{\min}\approx -19.48\)
- \(\ell=1.0\): \(\lambda_{\min}\approx -324\)

This behavior is exactly what you expect if the covariance term is not computed under the correct Gibbs weight: the covariance can swamp the Hessian and manufacture huge negativity.

Conclusion: treat uniform-cov coarse-graining as a **diagnostic failure mode**, unless the intended theorem genuinely uses that measure.

---

## 3. SU(2) φ-obstruction Hessian mismatch: likely a convention/factor bug

In the φ-obstruction run:

- symmetry checks are small (\(\sim 10^{-12}\)),
- but the finite-difference Hessian check is badly off:

\[
v^\top H v \approx 59.30 \quad\text{vs}\quad \text{finite-diff}\approx 29.27.
\]

A near factor-of-2 gap is a classic signature of:

- missing factor of 2 in the Hessian definition,
- Euclidean vs Riemannian Hessian mismatch,
- or projector inconsistency.

Until resolved, any downstream \(\Phi\)-proxy values are “instrument readings,” not ground truth.

---

## 4. What to do next (minimal fixes)

1. For blocking: freeze a “physical subspace” projector and compute \(\lambda_{\min}\) only on that subspace.
2. For coarse-graining: compute covariance under the actual Gibbs weight and report an ESS (effective sample size) / variance budget.
3. For φ: write a single-purpose unit test on a known analytic function where the Hessian is trivial, then re-run the φ harness.

