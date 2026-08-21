---
title: "Selection G — Gradient Flow as a Geometric Renormalization Group for Lattice Yang–Mills"
date: "2025-12-28"
---

# Abstract

The Yang–Mills gradient flow (Wilson flow) is often sold as a smoothing device for defining renormalized observables.
In the project files it plays a bigger role: it can be viewed as an **exact coarse-graining map** inducing a
time-dependent effective action $S_t$ on the configuration manifold.
This note distills the definitions and the exact flow equation, and suggests how it could integrate with curvature/Lyapunov methods.

# 1. Lattice gradient flow

Let $V\in G^{E(\Lambda)}$ denote link variables. The (Wilson) gradient flow is an ODE on configurations
\[
\frac{d}{dt}V_t = -\nabla S_W(V_t),
\qquad V_0 = V,
\]
where $\nabla$ is the Riemannian gradient on the compact manifold $G^{E(\Lambda)}$ and $S_W$ is the Wilson action.

Heuristically, $t$ is a smoothing scale: $t\!\uparrow$ damps UV fluctuations.

# 2. Effective action induced by the flow

Define an effective action $S_t$ by pushforward of the Gibbs weight under the deterministic map $V\mapsto V_t(V)$:
\[
e^{-S_t(V')}
:=
\int_{G^{E(\Lambda)}} \delta\!\big(V' - V_t(V)\big)\,e^{-S_W(V)}\,dV,
\]
so that $e^{-S_t}dV$ is the law of the flowed field at time $t$ when the initial field is distributed according to $e^{-S_W}dV$.

Equivalently,
\[
\int F(V')\,e^{-S_t(V')}\,dV'
=
\int F(V_t(V))\,e^{-S_W(V)}\,dV
\]
for all observables $F$.

# 3. Exact evolution equation for $S_t$

Because the flow is a diffeomorphism for small times (on a compact manifold, globally well-defined), one can differentiate the identity above in $t$
and derive an exact PDE for $S_t$.

A schematic form is:
\[
\partial_t S_t
=
\|\nabla S_t\|^2 - \Delta S_t + \text{(curvature/Jacobian terms)}.
\]
In other words, $S_t$ evolves by a Hamilton–Jacobi–type nonlinearity plus a Laplacian correction.

This resembles the functional renormalization group (FRG) and Polchinski-type flow equations, but here it is geometrically intrinsic on $G^{E(\Lambda)}$.

# 4. Why this might matter for the curvature program

The curvature/Lyapunov route needs two hard ingredients:

1. a **local curvature bound** near the vacuum (already supplied by the core curvature theorem),
2. a **global Lyapunov drift** to prevent excursions into bad regions.

Gradient flow offers a canonical candidate for (2).

A concrete idea:

- define $W(V)$ as a functional measuring how much smoothing time is needed to bring $V$ into the SAFE region,
  e.g. $W(V)=1+t_\mathrm{hit}(V)$ where $t_\mathrm{hit}$ is the first time the gradient flow enters the small-field ball.

If one could show a uniform inequality of the form
\[
L_\Lambda W \le -\alpha W + \beta \mathbf 1_{\mathrm{SAFE}},
\]
then the Lyapunov patching machinery would deliver volume-uniform global Poincaré/LSI.

# 5. Bigger-theory connections (disciplined speculation)

- **Geometric RG**: the map $V\mapsto V_t$ is a deterministic coarse-graining. If one can prove that Bakry–Émery curvature
  is monotone (or stable) along the induced $S_t$, that would be a new RG monotonic quantity beyond free energy.
- **Holographic flavor**: the extra “flow time” $t$ behaves like an emergent dimension. In AdS/CFT language, it is tempting to read
  curvature bounds at finite $t$ as bulk energy conditions.
- **Algorithmic verification**: because the flow is explicit, one can numerically estimate curvature and drift constants
  on finite lattices as evidence for uniformity.

# 6. Next technical tasks

1. Write the exact $\partial_t S_t$ equation in the chosen metric normalization for $G^{E(\Lambda)}$.
2. Prove stability of horizontal coercivity of the Wilson Hessian under small $t$.
3. Define a flowed Lyapunov functional and estimate $L_\Lambda W$ using convexity of the Haar and Wilson potentials.

