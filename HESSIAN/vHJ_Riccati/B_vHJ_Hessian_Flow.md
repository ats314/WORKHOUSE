# B. vHJ and Hessian Evolution: Exact PDE + What It Really Implies

This note collects a useful analytic fragment: the **viscous Hamilton–Jacobi (vHJ)** PDE
and the corresponding **Hessian evolution equation**.

It is valuable because it links:
- smoothing / coarse-graining (heat flow),
- convexity / curvature (Hessian),
- and ultimately Bakry–Émery curvature heuristics.

But: it is easy to over-interpret.  
So this write-up is explicit about **what follows rigorously** and what does **not**.

---

## B1. Cole–Hopf → vHJ

Let \(u(t,x)>0\) solve the heat equation on \(\mathbb{R}^n\):
\[
\partial_t u = \Delta u.
\]

Define the “effective action” (log-density)
\[
S(t,x) := -\log u(t,x).
\]

Then, by direct computation using \(\Delta e^{-S}=e^{-S}(|\nabla S|^2-\Delta S)\),
\[
\partial_t S \;=\; \Delta S \;-\; |\nabla S|^2.
\]
This is the **viscous Hamilton–Jacobi equation** with viscosity 1.

Interpretation:
- \(u\) is a density being smoothed by heat flow;
- \(S=-\log u\) evolves by a nonlinear PDE that mixes diffusion (\(\Delta S\)) and “Burgers drift” (\(-|\nabla S|^2\)).

---

## B2. Gradient evolution

Let
\[
b(t,x) := \nabla S(t,x),\qquad H(t,x) := \nabla^2 S(t,x).
\]

Differentiate the vHJ equation:

1) Since \(\nabla\Delta=\Delta\nabla\) in Euclidean space,
\[
\partial_t b
= \nabla\Delta S - \nabla(|b|^2)
= \Delta b - 2\,H b.
\]

So the gradient is diffused by \(\Delta b\) and damped by a matrix term \(2Hb\).

---

## B3. Hessian evolution (exact PDE)

Differentiate again:
\[
\partial_t H
= \nabla(\partial_t b)
= \Delta H - 2\,\nabla(Hb).
\]

Expand \(\nabla(Hb)\) using the product rule:
\[
\nabla(Hb) = (\nabla H)\,b + H(\nabla b) = (\nabla H)\,b + H^2.
\]

Therefore the exact Hessian PDE is
\[
\boxed{
\partial_t H
= \Delta H \;-\; 2\,(\nabla H)\,b \;-\; 2\,H^2.
}
\]

Equivalently, introducing the “convective derivative”
\[
D_t := \partial_t + 2\,b\cdot\nabla,
\]
one can write
\[
\boxed{
D_t H = \Delta H - 2\,H^2.
}
\]

---

## B4. Important sign consequence (this is where people hallucinate)

The nonlinear term is \(-2H^2\).

- If \(H\) is **positive** (locally convex potential), then \(-2H^2\) is **negative** and tends to *decrease* curvature: convexity is “flattened”.
- If \(H\) has **negative** directions, then \(H^2\) is still positive semidefinite, so \(-2H^2\) tends to drive those negative eigenvalues **more negative** along characteristics.

So **there is no automatic theorem** of the form “negative curvature must flip to positive” coming purely from the Riccati term.

Any “curvature restoration” from vHJ must come from the **diffusion term** \(\Delta H\), and from how the convective term moves regions of high curvature around.

This is consistent with classic results about log-concavity preservation:
- If \(u_0\) is log-concave, heat flow preserves log-concavity.
- If \(u_0\) is not log-concave, heat flow does not give a general monotone convexification guarantee.

---

## B5. Why this is still useful for the YM program

Even without a magical sign flip theorem, the vHJ/Hessian PDE provides:

1. A **precise analytic object** for “RG-like smoothing” (heat flow is a canonical coarse-graining).

2. A quantitative target:
   if one can prove that on the relevant ensemble / along the relevant flow,
   the diffusion term dominates concave growth quickly enough, then curvature can be improved.

3. A bridge to numerics:
   in the project’s SU(3) tests, **gradient flow** on the lattice action empirically increased
   \(\lambda_{\min}\) (the smallest Hessian eigenvalue) substantially, though not always across zero within the tested time window.

(That gradient flow is **not** the same as vHJ, but it is another smoothing dynamic worth analyzing.)

---

## B6. A clean “safe claim” you *can* make

If \(S(t,\cdot)\) remains uniformly convex with \(H\succeq \rho I\) on some region,
then Bakry–Émery gives local functional inequalities on that region.

So the honest program is:

- Use dynamics (vHJ-like or gradient flow) to drive typical configurations into a convex core,
- Use static BE curvature on that core,
- Patch via tails/Lyapunov.

That chain is conditional, but each subpiece is mathematically meaningful.

---
