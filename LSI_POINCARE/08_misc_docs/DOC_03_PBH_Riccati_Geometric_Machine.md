# DOC 03 — The PBH / Riccati “Geometric Machine” for a Stable Gap

## 0. Purpose

This note extracts the project’s most “theory-generating” idea:

> Treat the renormalization of the effective action’s Hessian as an **infinite-dimensional Riccati flow** driven by a **positive curvature source**, yielding a stable, nonzero lower bound for the smallest eigenvalue — interpreted as the mass gap / LSI constant.

Primary project sources:
- `03_GEOMETRIC_FLOW.md`
- `PROOF_11_Infinite_Curvature_Flow.md`
- `PROOF_02_Gradient_Flow_Stability.md` (Yamamura gradient-flow effective action equation, as motivation)
- `PROOF_04_Geometric_Mass_Derivation.md` (local Bakry–Émery positivity near identity)

## 1. The PBH flow (formal equation)

Let \(S_t\) denote a flow-time dependent effective action (gradient-flow–induced Wilsonian effective action).
Let \(H(t)\) denote the Hessian of \(S_t\) in appropriate coordinates on configuration space:
\[
H(t) \equiv \nabla^2 S_t.
\]

The project proposes the **Perelman–Bakry–Hessian (PBH) flow**:
\[
\partial_t H = -2 H^2 + \mathcal{R}(t).
\tag{PBH}
\]

Interpretation:
- \(-2H^2\) is a nonlinear damping term (Riccati-type),
- \(\mathcal{R}(t)\) is a “curvature injection” / anomaly source, intended to be **positive** due to compact gauge-group geometry (Haar) plus locality.

This resembles matrix Riccati flows arising from Schur complements / marginalization in Gaussian integration, and from differential equations for effective actions in RG-like settings.

## 2. Well-posedness in a Banach operator setting (sketch)

Let \(H(t)\) lie in a Banach algebra of bounded symmetric operators on a scale of Sobolev spaces, e.g.
\[
H(t)\in \mathcal{B}_s(H^{-s},H^s).
\]

If \(\mathcal{R}(t)\) is bounded and locally Lipschitz as an operator-valued function, then the RHS
\[
F(H)= -2H^2 + \mathcal{R}(t)
\]
is locally Lipschitz in \(H\), and Picard–Lindelöf yields local existence and uniqueness.

The quadratic term \(-2H^2\) provides damping against blowup to \(+\infty\) for positive initial data.

## 3. Riccati lower bound for the smallest eigenvalue

Let \(\lambda(t)\) denote the smallest eigenvalue of \(H(t)\) restricted to the relevant (physical / horizontal / local) subspace.

Project (PBH) onto an instantaneous unit eigenvector \(v_t\):
\[
\dot{\lambda}(t) = \langle v_t, \partial_t H\, v_t\rangle
= -2\lambda(t)^2 + \langle v_t,\mathcal{R}(t) v_t\rangle.
\tag{eig}
\]

Assume the source has a uniform floor on the sector of interest:
\[
\langle v,\mathcal{R}(t)v\rangle \ge c_{\rm geom} >0
\qquad \forall v,\ \|v\|=1.
\tag{Rpos}
\]

Then
\[
\dot{\lambda}(t)\ \ge\ -2\lambda(t)^2 + c_{\rm geom}.
\tag{Riccati}
\]

The scalar comparison ODE \(\dot{y}=-2y^2+c_{\rm geom}\) has a stable fixed point at
\[
y_* = \sqrt{\frac{c_{\rm geom}}{2}}.
\]

Hence if \(\lambda(0)\) is sufficiently large (UV), the solution decreases toward \(y_*\) but cannot cross below it:
\[
\lambda(t) \ge y_* =: \rho_0 > 0.
\tag{Gap}
\]

**Interpretation:** \(\rho_0\) is the *stable curvature floor* and is identified with the LSI constant / mass gap.

## 4. Where does \(c_{\rm geom}>0\) come from?

The project points to two “geometric” sources:

1. **Haar (Ricci) curvature.**  
   Configuration space has a product Haar metric; the associated Ricci tensor is positive (compact Lie group geometry). This contributes a strictly positive term to Bakry–Émery curvature near identity.

2. **Wilson action Hessian near identity.**  
   For small plaquette angles, the Wilson action is convex in physical directions, producing a further positive Hessian contribution.

Together these yield a local Bakry–Émery positivity estimate of the type
\[
\mathrm{Ric} + \nabla^2 S \ \ge\ \kappa_{\rm Haar} + \beta c_W
\]
on horizontal directions, in a neighborhood of identity.

## 5. Why this is exciting (even if incomplete)

This “machine” suggests a geometric reformulation of mass generation:

- The gap is not a mysterious dynamical output; it is a **fixed point of a curvature-driven Riccati flow**.

If made rigorous, it would be a conceptual bridge between:
- **RG / coarse-graining** (effective actions),
- **geometric analysis** (curvature evolution),
- and **spectral theory** (gap).

It also hints at a more general program:

> **Mass gaps might correspond to stable curvature floors of effective potentials under renormalization.**

That could extend to other gapped QFTs, sigma models on compact targets, and perhaps to certain condensed-matter systems described by Gibbs measures on compact groups.

## 6. Concrete next steps to make PBH rigorous

1. **Derive (PBH) from an actual RG map.**  
   Show that integrating out fast modes produces a Schur complement formula leading to a matrix Riccati inequality for the coarse Hessian.

2. **Identify \(\mathcal{R}(t)\) explicitly.**  
   Right now \(\mathcal{R}(t)\) is a placeholder. One wants:
   - positivity,
   - locality (block structure),
   - scaling estimates (polylog vs power).

3. **Control off-diagonal terms.**  
   Combine with IR decoupling: the flow should preserve local/topological splitting, so the local sector sees a stable gap.

4. **Recover the beta function.**  
   A real “physics check”: can the PBH coefficients reproduce the known 1-loop (and ideally 2-loop) running of the coupling?

