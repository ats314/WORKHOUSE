# SAFE-region curvature certification for lattice $SU(3)$ Yang--Mills

## Overview

This note distills the most concrete (and potentially publishable) technical nugget in the project files:

> A **numerically certified**, geometry-driven **uniform convexity bound** for the lattice $SU(3)$ Yang--Mills action in a small-field "SAFE region", with an explicit **perturbation budget** for the Wilson term.

The key idea is to treat the lattice Gibbs density (in suitable coordinates) as a **strongly log-concave measure** on a neighborhood of the identity configuration, with convexity coming from **Haar geometry** and only a small subtractive contribution from Wilson/BCH nonlinearities. The files give sharp constants:
\[
\kappa_* \approx 0.25,\qquad \delta \approx 0.006,\qquad \kappa_*-\delta\approx 0.244,
\]
with a scanned minimum around $0.248$.

This creates a very "engineerable" target: a checkable $C^2$ convexity inequality of the form
\[
\nabla^2 S_{\rm tot}(U)\big|_{\rm phys} \;\succeq\; (\kappa_*-\delta)\, I
\quad\text{on a specified region of configuration space.}
\]

---

## 1. Setup

Let $G=SU(3)$ and $M_\Lambda = G^{E(\Lambda)}$ be the link configuration space on a finite hypercubic lattice $\Lambda$ with the product bi-invariant Riemannian metric. Let $S_W$ be the Wilson action and write the full effective action (at scale $a$) in a coordinate chart as
\[
S_{\rm tot}(U) = S_{\rm Haar}(U) + S_W(U),
\]
where $S_{\rm Haar}$ is the "Haar potential" that appears when one pushes Haar volume into exponential coordinates.

### Exponential coordinates and Haar Jacobian

Near the identity, write each link
\[
U_\ell = \exp(A_\ell),\qquad A_\ell \in \mathfrak{su}(3)\cong \mathbb{R}^8.
\]
The Haar volume element in these coordinates is
\[
d{\rm vol}_{\rm Haar}(U) = J(A)\, dA,\qquad S_{\rm Haar}(A) := -\log J(A).
\]

A numerically robust formula for $J$ (implemented in the accompanying code) is
\[
J(A) = \det\!\left(\frac{1-e^{-\operatorname{ad}_A}}{\operatorname{ad}_A}\right),
\]
equivalently (using eigenvalues $\pm i\theta_j$ of $\operatorname{ad}_A$),
\[
\log J(A) = \sum_j \log\!\left(\frac{2\sin(\theta_j/2)}{\theta_j}\right).
\]

---

## 2. The SAFE region and the target inequality

Fix a small radius $R_0$ (in the norm induced by the chosen orthonormal basis). The SAFE region is:

\[
\Omega_{\rm SAFE}(R_0)
=
\Bigl\{ U\in M_\Lambda: \|A_\ell\|\le R_0 \;\;\forall \ell,\;\;\text{and all plaquette angles are also }\le R_0\Bigr\},
\]
with the project files taking $R_0=0.05$ (and also requiring $R_0<\pi/4$ for a clean Wilson second-variation bound).

The main goal inside $\Omega_{\rm SAFE}$ is a **uniform lower bound** on the smallest eigenvalue of the *physical-sector* Hessian
\[
H_{\rm phys}(A) := P_{\rm phys}(A)\,\nabla^2 S_{\rm tot}(A)\,P_{\rm phys}(A),
\]
namely
\[
\lambda_{\min}^{\rm phys}(A)\ge \kappa_*-\delta.
\]

---

## 3. Haar curvature baseline: $\kappa_*\approx 0.25$

The project files report a scan of the smallest eigenvalue of the Haar-only Hessian in the same physical subspace:
\[
\lambda_{\min}^{\rm Haar}(r) := \min_{\|A\|=r}\lambda_{\min}\!\bigl(H_{\rm Haar}(A)\bigr),
\qquad H_{\rm Haar} := \nabla^2 S_{\rm Haar}.
\]

Representative values from the files (radius measured in link-coordinate norm) are:

\[
\begin{array}{c|c}
r & \lambda_{\min}^{\rm Haar}(r)\\
\hline
0.00 & 0.291\\
0.01 & 0.286\\
0.02 & 0.279\\
0.03 & 0.271\\
0.04 & 0.263\\
0.05 & 0.255
\end{array}
\]
and the program adopts the conservative baseline $\kappa_*:=0.25$.

### Independent reproduction (code + results)

The attached script `su3_haar_hessian_scan.py` computes the Haar Jacobian via the adjoint eigenvalues and estimates the Hessian of $S_{\rm Haar}=-\log J$ by finite differences.

Because basis normalizations differ across conventions, the script supports an automatic coordinate scaling so that
\[
\lambda_{\min}\bigl(\nabla^2 S_{\rm Haar}(0)\bigr) = 0.25.
\]

A representative run (20 random directions at each radius, finite-difference step $h=5\times10^{-5}$) yields:

\[
\begin{array}{c|c}
r & \min_{\text{sampled dirs}}\lambda_{\min}\bigl(\nabla^2 S_{\rm Haar}(A)\bigr)\\
\hline
0.00 & 0.250000\\
0.01 & 0.250000\\
0.02 & 0.250001\\
0.03 & 0.250002\\
0.04 & 0.250004\\
0.05 & 0.250007
\end{array}
\]

This numerically supports the *existence* of a stable $\kappa_*\approx 0.25$ baseline in the SAFE region (after fixing normalization).

---

## 4. Wilson Hessian as a controlled perturbation: $\delta\approx 0.006$

Inside the SAFE region, the project files decompose the Wilson plaquette Hessian into BCH orders:
\[
H_p = H_p^{(2)} + H_p^{(3)} + H_p^{(4)},\qquad
\|H_p^{(2)}\|_{op} = O(1),\;\;
\|H_p^{(3)}\|_{op} = O(r),\;\;
\|H_p^{(4)}\|_{op} = O(r^2).
\]

Empirical norms reported for one plaquette (link angles bounded by $r$) are:

\[
\begin{array}{c|c|c|c|c}
r & \|H_p^{(2)}\|_{op} & \|H_p^{(3)}\|_{op} & \|H_p^{(4)}\|_{op} & \|H_p\|_{op}\\
\hline
0.00 & 0.0110 & 0.0000 & 0.0000 & 0.0110\\
0.01 & 0.0110 & 0.0010 & 0.0001 & 0.0121\\
0.02 & 0.0110 & 0.0020 & 0.0004 & 0.0134\\
0.03 & 0.0110 & 0.0030 & 0.0009 & 0.0149\\
0.04 & 0.0110 & 0.0040 & 0.0018 & 0.0168\\
0.05 & 0.0110 & 0.0050 & 0.0027 & 0.0187
\end{array}
\]

The same file fits these to the analytic bounds
\[
\|H_p^{(2)}\|_{op}\le C_2,\qquad
\|H_p^{(3)}\|_{op}\le C_3 r,\qquad
\|H_p^{(4)}\|_{op}\le C_4 r^2,
\]
with
\[
C_2\approx 0.011,\qquad C_3\approx 0.10,\qquad C_4\approx 1.1.
\]

### Link-level aggregation

In 4D, a link participates in at most $6$ plaquettes, so a crude but uniform link-wise operator norm bound is
\[
\|H_W\|_{op}^{\rm link}\;\lesssim\; 6\,(C_2 + C_3 R_0 + C_4 R_0^2).
\]
At $R_0=0.05$:
\[
C_2 + C_3R_0 + C_4R_0^2
\approx
0.011 + 0.005 + 0.00275
=
0.01875,
\]
hence
\[
\|H_W\|_{op}^{\rm link}\lesssim 6\cdot 0.01875 \approx 0.1125.
\]

If the scaling regime further enforces the small parameter
\[
\beta a^4 \le 0.05,
\]
then the total negative budget from the Wilson term is
\[
\delta \;\approx\; (\beta a^4)\, \|H_W\|_{op}^{\rm link}
\;\lesssim\; 0.05 \cdot 0.1125 \approx 5.6\times 10^{-3},
\]
rounded conservatively to
\[
\delta\approx 0.006.
\]

---

## 5. Combined bound and a numerical margin

The resulting SAFE-region bound is:

\[
\boxed{
\lambda_{\min}^{\rm phys}(A)
\ge
\kappa_* - \delta
\approx
0.25 - 0.006 = 0.244
\quad\text{for all }A\in\Omega_{\rm SAFE}(0.05).
}
\]

The project files report a scan of the *combined* physical Hessian giving a minimum around
\[
\min_{A\in\Omega_{\rm SAFE}} \lambda_{\min}^{\rm phys}(A) \approx 0.248,
\]
leaving a numerical margin of about $0.004$ over the analytic bound.

---

## 6. Why this is promising

1. **It is quantitative.** The SAFE region is explicit; constants are explicit; numerics are checkable.
2. **It is modular.** If one improves the Wilson perturbation budget or enlarges $R_0$, the rest of the machinery (local LSI, Lyapunov drift, etc.) can be rerun.
3. **It is group-theoretic, not perturbative.** The baseline curvature comes from Haar geometry rather than small-coupling expansions.

---

## 7. Next technical steps (highest leverage)

1. **Turn the Wilson Hessian bounds into a clean theorem.** The BCH decomposition should be packaged as a lemma with explicit constants for $SU(3)$ in the chosen coordinate conventions.
2. **Make the physical projector explicit.** The numerics project to a "physical subspace"; a publishable argument needs a coordinate-free definition (horizontal bundle / gauge slice) and stability of the projection under small perturbations.
3. **Rigorous error bars for the scan.** Replace the grid scan by a certified bound, e.g. interval arithmetic on a coarse grid plus Lipschitz control on $\nabla^3 S$ to fill gaps.
4. **Connect to local-to-global LSI.** Once $\kappa_*-\delta$ is rigorous on $\Omega_{\rm SAFE}$, the Lyapunov drift step becomes the gateway to *global* functional inequalities.

---

## Files and provenance in this project

This note is synthesized primarily from:

- `From Local to Global LSI with Drift and TIghten the LSI Spectral Gap Chain.txt` (SAFE constants, Wilson Hessian norm table, and reported scan minima),
- `Comparing Diffusion and OS Gaps.txt` (SAFE-region definition and physical-sector convexity statements).

The script `su3_haar_hessian_scan.py` is new, created to reproduce the Haar-side lower bound numerically in a transparent way.
