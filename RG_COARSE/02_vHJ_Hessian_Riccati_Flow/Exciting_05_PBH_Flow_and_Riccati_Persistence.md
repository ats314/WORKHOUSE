# Exciting Extract 05 — PBH Flow + Riccati Persistence of a Gap (A Curvature-RG Mechanism)

## 1. Why this is exciting

This extract is a “mechanism blueprint”:

- start with a (projected) parabolic evolution equation for a symmetric tensor \(h_t\) (a horizontal Hessian / curvature object),
- extract a scalar parabolic inequality for its **minimal eigenvalue** \(\lambda_{\min}\),
- combine it with a maximum principle (possibly on a stratified space via polarity),
- reduce the lower bound problem to a **Riccati-type ODE**.

It’s Hamilton’s tensor maximum principle energy, repurposed for a mass-gap pipeline.

Even if the physics inputs (anomaly positivity, asymptotic freedom bounds) remain conditional, the analytic architecture is crisp and highly general.

---

## 2. PBH flow: a representative model equation

Work on a finite-dimensional “regular” configuration manifold \(\mathcal M_{\mathrm{reg}}\) with a horizontal distribution \(H\) (e.g., gauge orbit space regular stratum). Let \(S_t:\mathcal M_{\mathrm{reg}}\to\mathbb R\) solve a viscous Hamilton–Jacobi type equation
\[
\partial_t S_t = \Delta_H S_t - |\nabla_H S_t|^2 + J_t,
\tag{2.1}
\]
where \(J_t\) encodes forcing/anomaly.

Define:

- horizontal drift \(V_t:=\nabla_H S_t\),
- horizontal Hessian tensor \(h_t := \nabla_H^2 S_t\) (symmetric bilinear form on \(H\)).

A standard Bochner/Hamilton calculation (projected to horizontals) yields a tensor evolution inequality of the form
\[
\partial_t h_t
\ \ge\
\Delta_H h_t - 2\nabla_{V_t}h_t \ -\ 2 h_t^2 \ +\ S_{\mathrm{anom}}(t)\ +\ \mathfrak G(t),
\tag{2.2}
\]
where:

- \(S_{\mathrm{anom}}(t)=\nabla_H^2 J_t\) is the “anomaly source tensor”,
- \(\mathfrak G(t)\) collects geometric correction terms (curvature of \(\mathcal M_{\mathrm{reg}}\), non-integrability of \(H\), etc),
- \(h_t^2\) is the quadratic tensor product \(h_t\circ h_t\), giving the Riccati nonlinearity.

The specific form of \(\mathfrak G\) can be complicated; what matters is bounding it.

---

## 3. Extracting a scalar inequality for the minimal eigenvalue

Let \(\lambda_{\min}(t,x)\) be the smallest eigenvalue of \(h_t(x)\) (restricted to the horizontal space \(H_x\)). Under mild regularity, Hamilton’s tensor maximum principle yields:

### Proposition 3.1 (Eigenvalue inequality)

Assume:

1. \(S_{\mathrm{anom}}(t,x)\ge \sigma\,\mathrm{Id}\) on horizontals for some \(\sigma>0\),
2. \(\mathfrak G(t,x)\ge -\varepsilon(t)\,\mathrm{Id}\) on horizontals for some \(\varepsilon(t)\ge 0\).

Then (in a viscosity/weak sense if necessary),
\[
\partial_t \lambda_{\min}
\ \ge\
L\lambda_{\min} \ -\ 2\lambda_{\min}^2 \ +\ \sigma - \varepsilon(t),
\tag{3.1}
\]
where \(L:=\Delta_H-2\nabla_{V_t}\) is the second-order operator appearing in (2.2).

**Interpretation.**
The diffusion/transport parts become \(L\lambda_{\min}\) (good for minima), the quadratic term becomes \(-2\lambda_{\min}^2\), and the forcing becomes \(+\sigma\) minus a controllable error \(\varepsilon(t)\).

---

## 4. Parabolic comparison \(\Rightarrow\) Riccati reduction

Suppose \(\mathcal M\) is stratified with singular set \(\Sigma\) (reducibles) and regular stratum \(\mathcal M_{\mathrm{reg}}\). If \(\Sigma\) is polar for the diffusion associated to \(L\), then comparison principles can be run on \(\mathcal M_{\mathrm{reg}}\) without boundary conditions on \(\Sigma\) (see Exciting Extract 04).

In the smooth case (or stratified-polar case), apply the parabolic maximum principle to (3.1) to deduce that the global infimum
\[
m(t):=\inf_{x\in\mathcal M_{\mathrm{reg}}}\lambda_{\min}(t,x)
\tag{4.1}
\]
satisfies the scalar differential inequality
\[
\dot m(t)\ \ge\ -2m(t)^2 + \sigma - \varepsilon(t).
\tag{4.2}
\]

Now compare \(m(t)\) to the solution of the ODE
\[
\dot y(t) = -2y(t)^2 + \sigma - \varepsilon(t),
\qquad y(0)=m(0).
\tag{4.3}
\]
Standard comparison gives \(m(t)\ge y(t)\).

---

## 5. A clean persistence corollary (eventual dominance)

### Corollary 5.1 (Eventual positive lower bound)

Assume there exists \(T_1\) such that for all \(t\ge T_1\),
\[
\varepsilon(t)\le \frac{\sigma}{2}.
\tag{5.1}
\]
Then for \(t\ge T_1\), \(m(t)\) is bounded below by the solution to
\[
\dot y = -2y^2 + \frac{\sigma}{2},
\tag{5.2}
\]
so in particular
\[
\liminf_{t\to\infty} m(t)\ \ge\ \sqrt{\frac{\sigma}{4}}.
\tag{5.3}
\]

**Proof.**
For \(t\ge T_1\), (4.2) implies
\[
\dot m \ge -2m^2 + \frac{\sigma}{2}.
\]
Compare to the autonomous Riccati ODE (5.2), whose stable fixed point is \(+\sqrt{\sigma/4}\). ∎

This is the core “source dominates geometry” principle: once the negative geometric corrections are small enough, positivity becomes self-sustaining.

---

## 6. Where the physics enters (and what to prove)

To use this as a genuine mass-gap pipeline, one must justify the two inputs:

1. **Anomaly source positivity:** \(S_{\mathrm{anom}}(t,x)\ge \sigma\,\mathrm{Id}\).  
2. **Control of geometric correction:** \(\mathfrak G(t,x)\ge -\varepsilon(t)\mathrm{Id}\) with \(\varepsilon(t)\to 0\) (often expected \(\varepsilon(t)\sim g(t)^2\) in an asymptotically free regime).

A recurring structural claim in the project is:

- sectional curvature of gauge orbit space is \(O(g(t)^2)\),
- trace/size of \(h_t\) is uniformly bounded,
- therefore \(\mathfrak G\) is \(O(g(t)^2)\).

This is exactly the kind of estimate where a careful geometric-analysis paper could live.

---

## 7. What theory this points toward

This is a general theory direction:

> **Tensor parabolic maximum principles for projected (horizontal) Hessian flows on quotient/stratified spaces, with explicit Riccati-type lower bounds for minimal eigenvalues.**

It would have applications to:

- RG-style parabolic flows for effective actions,
- stochastic quantization and convexity propagation,
- stability of functional inequality constants under scale flows.

The novelty is not the Riccati ODE (which is classical), but the *identification* of the mass-gap problem with a curvature-eigenvalue parabolic comparison problem that can be run despite singular strata.

---

## 8. Next work needed (to make this rigorous and useful)

1. **Derive (2.2) cleanly** in your chosen finite-dimensional approximation (lattice or Galerkin truncation) and identify \(\mathfrak G\) explicitly.  
2. **Prove tensor maximum principle hypotheses** (regularity, domain, boundary behavior).  
3. **Establish polarity of singular strata** for the relevant diffusion (or avoid singularities by working in a slice).  
4. **Prove the anomaly lower bound** in a way compatible with OS/reflection positivity constraints.

If steps (1)–(4) land, (5.3) becomes a concrete, mechanism-level explanation for why a positive “source” forces a persistent gap.
