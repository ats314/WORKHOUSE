# vHJ Curvature Flow: Riccati Decay, α-Extraction, and the Haar α-Band

This document extracts the **most concrete** PDE-side result in the project:
a measured Riccati law for curvature decay in a viscous Hamilton–Jacobi (vHJ) flow,
and a striking clustering of decay coefficients \(\alpha\) once Haar-like “mass curvature” is included.

## 1. Model

A vHJ-type update used in the simulations (discrete time) was summarized as
\[
S^{n+1} \;=\; S^n + \Delta t\big(\Delta S^n - \|\nabla S^n\|^2\big),
\]
on a grid (2D and 4D runs were mentioned across logs), with curvature diagnostics taken from the Hessian of \(S\)
(at a point, often the center/origin).

Define \(\lambda(t)\) as a tracked curvature scalar (e.g. smallest Hessian eigenvalue, or a curvature trace proxy).

## 2. Riccati hypothesis and α extraction

### Hypothesis
The minimal curvature follows approximately
\[
\frac{d\lambda}{dt} \;\approx\; -\alpha\,\lambda^2.
\]
This implies the explicit decay law
\[
\frac{1}{\lambda(t)} \;\approx\; \frac{1}{\lambda(0)} + \alpha t,
\qquad
\lambda(t)\approx\frac{1}{b+\alpha t}.
\]

### Extraction method
Given sampled times \(t_i\) and measured \(\lambda(t_i)\), regress
\[
y_i := \frac{1}{\lambda(t_i)} \approx \alpha t_i + b.
\]

## 3. A concrete run (quadratic-only phase)

From a logged run (PDF export), the regression produced:

- Estimated Riccati coefficient
  \[
  \alpha \approx 0.0010214540,
  \]
- Intercept
  \[
  b = \frac{1}{\lambda(0)} \approx 0.2387851562,
  \]
- Prediction
  \[
  \lambda(t) \approx \frac{1}{b+\alpha t}.
  \]

The match between \(\lambda_{\rm true}\) and \(\lambda_{\rm pred}\) was extremely close (sample table):

\[
\begin{array}{c|cc}
t & \lambda_{\rm true} & \lambda_{\rm pred}\\\hline
0 & 4.2007 & 4.1879\\
30 & 3.7135 & 3.7116\\
60 & 3.3303 & 3.3325\\
90 & 3.0203 & 3.0237\\
120 & 2.7641 & 2.7673\\
150 & 2.5486 & 2.5510\\
180 & 2.3648 & 2.3660\\
210 & 2.2060 & 2.2061\\
240 & 2.0673 & 2.0664\\
270 & 1.9453 & 1.9433\\
\end{array}
\]

## 4. The Haar α-band phenomenon

Across multiple “phases” (quadratic + Haar + YM-like perturbations), the project summary reports:

- Quadratic-only phase: “fast decay convex phase”
  \[
  \alpha \sim 0.0010.
  \]
- Haar-stabilized phases: “slow decay stable phase”
  \[
  \alpha \approx 0.00079,
  \qquad\text{with clustering in }\alpha\in(7.8,8.0)\times 10^{-4}.
  \]

Representative extracted values (from project summary):

- \(\alpha \approx 0.001002\) (quadratic, all modes)
- \(\alpha \approx 0.000788\) (Haar-stabilized, all modes)
- \(\alpha \approx 0.000781\) (slightly deformed)
- SU(2)-adjoint anisotropic example:
  \[
  \alpha_1 \approx 0.0007875,\quad
  \alpha_2 \approx 0.0007933,\quad
  \alpha_3 \approx 0.0007628,\quad
  \alpha_4 \approx 0.0007981.
  \]
- SU(3)-type nearly isotropic examples cluster similarly.

### Interpretation (working theory, not yet a theorem)
The Haar measure introduces an *effective isotropic curvature floor* that controls the long-time decay rate of curvature under vHJ smoothing.
YM-like perturbations change anisotropy but do not move the system far from the Haar-controlled \(\alpha\)-band.

This is reminiscent of a “universality class” in which the **measure curvature** dominates the effective Riccati coefficient.

## 5. What would upgrade this from an observation to a proof-like statement?

1. **Clarify which curvature is tracked** (min eigenvalue vs trace vs selected mode).
2. **Derive a Riccati inequality** for the tracked curvature from the PDE:
   establish a bound of the form \(d\lambda/dt \le -c\,\lambda^2\) with explicit \(c\).
3. **Explain the Haar band analytically** by showing \(c\) is pinned by a measure-curvature term (or an effective mass).
4. **Connect to lattice gauge dynamics** by mapping the PDE phase diagram to observed SU(3)/SU(2) convex cores and drift certificates.

Even in its current form, the α-band is a high-value “phenomenological law” that constrains viable analytic models.
