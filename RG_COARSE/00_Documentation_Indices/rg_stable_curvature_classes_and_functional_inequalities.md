# RG-Stable Curvature Classes and Functional Inequalities

## Abstract
We define curvature-controlled potential classes stable under renormalization-group transformations and show that membership in such a class implies uniform log-Sobolev inequalities and spectral gaps across all RG scales.

## Curvature Class
Define
\[
\mathcal{C}(\kappa):=\{(g,V):\mathrm{Ric}_g+\nabla^2V\ge \kappa g\}.
\]

## Stability Properties
- Perturbations: $V\to V+W$ with $\|\nabla^2W\|\le\varepsilon$ gives $\kappa\to\kappa-\varepsilon$.
- Products: curvature tensorizes via $\min$.
- Marginalization: Schur-complement bounds give $\kappa'\ge\alpha\kappa$.

## RG Admissibility
An RG trajectory $(g_n,V_n)$ is $(\kappa_*,\alpha)$-admissible if
\[
\mathrm{Ric}_{V_n}\ge \alpha^n \kappa_* g_n.
\]

## Main Result
If $\inf_n \alpha^n\kappa_*>0$, then all RG iterates satisfy
\[
C_{\mathrm{LSI}}\le\frac{2}{\inf_n \alpha^n\kappa_*},\qquad \lambda_1\ge\inf_n \alpha^n\kappa_*.
\]

## Interpretation
This reframes RG stability as stability in curvature space, providing a geometric criterion for mass-gap preservation.

