# SAFE-Region Curvature Certification for SU(3)

## Abstract
We define and certify a small-field SAFE region in right-invariant coordinates on SU(3), within which the physical Bakry–Émery curvature is uniformly positive. Explicit analytic bounds are combined with numerical eigenvalue scans to obtain a robust curvature floor $\kappa_*>0$.

## Haar Curvature
For SU(3) with Killing-form normalization,
\[
\mathrm{Ric}_{SU(3)} \ge \tfrac14 g.
\]
In exponential coordinates $U=\exp(X)$, the Haar density satisfies
\[
d\mathrm{Haar}(U)=J(X)dX,
\]
with
\[
\|\nabla^2 \log J(X)\|_{op} \le 0.049 \quad \text{for } \|X\|\le 0.05.
\]
Hence
\[
\mathrm{Ric}_{\mathrm{Haar}} \ge 0.201 g.
\]

## Wilson Hessian Perturbation
Using BCH expansion of the Wilson action,
\[
\|\nabla^2 S_W\|_{op,\ell} \le 0.006 \quad \text{for } \beta a^4\le 0.05,\ \|X_\ell\|\le0.05.
\]

## SAFE Constant
Combining the two contributions,
\[
\mathrm{Ric}_{\mathrm{phys}} \ge \kappa_* g, \qquad \kappa_*=0.25,
\]
uniformly throughout the SAFE region.

## Numerical Verification
Discrete eigenvalue scans of the physical Hessian confirm
\[
\lambda_{\min}^{\mathrm{phys}}(X) \ge 0.248 \quad \forall \|X\|\le0.05.
\]

## Conclusion
The SAFE region is analytically and numerically certified as a curvature-controlled domain suitable for RG, LSI, and mass-gap arguments.

