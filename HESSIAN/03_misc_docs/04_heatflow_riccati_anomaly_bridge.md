# Heat-flow effective actions, viscous Hamilton–Jacobi, and a trace-anomaly curvature source

> **Status note.** This is the project’s most “mathematical physics bridge” fragment: it attempts to connect (i) RG/heat-flow type evolution of effective actions, (ii) Riccati-type stabilization of Hessian eigenvalues, and (iii) a hypothesized curvature source coming from the trace anomaly.

## 1. A clean derivation: heat flow for \(\rho_t\) implies viscous Hamilton–Jacobi for \(S_t\)

Assume a family of densities can be written as
\[
\rho_t(x)=Z_t^{-1}e^{-S_t(x)},
\]
and suppose \(\rho_t\) satisfies the heat equation
\[
\partial_t \rho_t = \Delta \rho_t.
\]

Differentiate \(\rho_t\) in time:
\[
\partial_t \rho_t = -(\partial_t S_t + \partial_t\log Z_t)\,\rho_t.
\]

Compute the Laplacian:
\[
\Delta \rho_t = \rho_t\big(-\Delta S_t + \|\nabla S_t\|^2\big).
\]

Equating \(\partial_t\rho_t\) and \(\Delta\rho_t\), and absorbing the purely time-dependent scalar \(\partial_t\log Z_t\) into \(S_t\), yields the **viscous Hamilton–Jacobi** type PDE
\[
\partial_t S_t
=
\Delta S_t - \|\nabla S_t\|^2
\qquad\text{(up to addition of a function of \(t\) only).}
\]

This calculation is elementary but valuable: it gives an explicit PDE model for how effective actions might evolve under a smoothing/heat-flow RG.

---

## 2. Hessian evolution and the Riccati “reaction” term

Formally differentiating again (schematically) leads to a Hessian evolution with a quadratic “reaction” term of the form
\[
\partial_t H_t \;\approx\; (\text{diffusion/transport}) \;-\;2H_t^2 \;+\;(\text{geometry/source terms}),
\qquad H_t=\nabla^2 S_t.
\]

The project records this as a named “Riccati evolution of the Hessian”:
\[
\partial_t H_t = \Delta_L H_t - 2H_t^2 + R_t,
\]
where \(\Delta_L\) is a Lichnerowicz-type Laplacian on symmetric tensors and \(R_t\) is a curvature/source contribution.

---

## 3. From matrix evolution to a scalar inequality for \(\lambda_{\min}\)

If \(\lambda(t,x)\) denotes the smallest eigenvalue of \(H_t(x)\), the project expects a comparison inequality of the schematic form
\[
\dot\lambda(t) \;\gtrsim\; -2\lambda(t)^2 + \sigma_{\mathrm{geom}}(t),
\]
where \(\sigma_{\mathrm{geom}}(t)\) is a positive “source term” (coming from geometry and/or QFT effects).

A standard comparison ODE for
\[
\dot\ell = -2\ell^2 + \sigma_{\mathrm{geom}},
\qquad \ell(0)=0,
\]
has explicit solution
\[
\ell(t)
=
\sqrt{\frac{\sigma_{\mathrm{geom}}}{2}}
\;
\tanh\!\big(\sqrt{2\sigma_{\mathrm{geom}}}\,t\big),
\]
which rises to a positive limit \(\sqrt{\sigma_{\mathrm{geom}}/2}\).
So: **a positive source term stabilizes the curvature** against the \(-2\lambda^2\) decay.

This is the core geometric intuition: “entropy/geometry/anomaly pumps curvature back in.”

---

## 4. The conjectural physics ingredient: trace anomaly as a curvature source

The project proposes an “Anomaly–Curvature Identity” program: relate the trace anomaly
\[
\Theta^\mu_{\ \mu}
\;\sim\;
\frac{\beta(g)}{2g}\,\mathrm{Tr}\,F_{\mu\nu}^2
\]
to a positive Bakry–Émery curvature source term \(\sigma_\*\) (or \(\sigma_{\mathrm{anom}}(t)\)) in the Hessian evolution.

One explicit project formulation introduces a curvature source at a renormalized coupling \(g_\*\):
\[
\sigma_\*
=
\frac{|\beta(g_\*)|}{2g_\*}\,\langle F^2\rangle.
\]

The goal is then to prove an implication of the style
\[
\beta(g)\neq 0
\quad\Longrightarrow\quad
\operatorname{Hess}\big(\Gamma[A]\big)\;\ge\;\sigma_{\mathrm{geom}}>0,
\]
for a properly defined renormalized effective action \(\Gamma[A]\).

The project also frames an associated threshold question:

> Is there a critical inequality \(\sigma_{\mathrm{anom}}(t)>\sigma_{\mathrm{crit}}\) required for the Riccati mechanism to keep \(\lambda_{\min}\) positive?

---

## 5. Why this is exciting (and dangerous)

Exciting:
- It offers a mechanism for maintaining positive curvature *after* the Haar mass dies in the continuum limit.

Dangerous:
- Every step here hides serious functional-analytic and QFT-definition difficulties:
  defining \(\Gamma[A]\) rigorously, controlling infinite-dimensional Hessians, and connecting a local anomaly density to global convexity.

But as a *research program*, it has a crisp shape: it reduces “mass gap” to “find a positive curvature source term that beats the Riccati decay”.

---

## Provenance pointers (project internal)
This note extracts:
- the derivation of viscous Hamilton–Jacobi from heat flow of a Gibbs density,
- the named Riccati Hessian evolution equation,
- the scalar comparison inequality and its explicit \(\tanh\) solution,
- the anomaly–curvature identity conjecture and the \(\sigma_{\mathrm{anom}}\) threshold question.

