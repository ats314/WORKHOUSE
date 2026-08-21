---
title: "Dynamic Restoration and the τ(β,r) Envelope (Riccati-Style Mechanism)"
date: "2026-01-01"
---

## 1. Status statement

This document isolates the project’s proposed **dynamic convexification** step:

> Even if \(\lambda_{\min}(\nabla^2 S_\beta(A_0))<0\), the flow  
> \(\partial_t A_t = -\nabla S_\beta(A_t)\) reaches the convexity core in finite time.

The project’s analytic template uses:

1. Haar convexity floor \(c_0>0\),
2. Wilson Hessian erosion bound with explicit constant \(C_{SU(3)}\),
3. a Riccati-type inequality for \(\lambda_{\min}(t)\) once convexity holds.

**Important:** The flow-to-amplitude differential inequalities below are the part that must be written with maximal care; numerical runs suggest the mechanism is real, but an analytic proof must carefully justify each inequality.

---

## 2. Baseline static inequality and convexity radius

Assume:

- Haar floor:
  \[
    \nabla^2 S_{\mathrm{Haar}}(A)\succeq c_0 I,\qquad c_0=0.125.
  \]
- Wilson erosion bound in a small-field region:
  \[
    \|\nabla^2 S_W(A)\|_{\mathrm{op}}
    \le
    C_{SU(3)}\,\beta\,r^2,
    \qquad r:=\|A\|_\infty.
  \]

Then the minimal Hessian eigenvalue satisfies the static bound
\[
  \lambda(t) := \lambda_{\min}(\nabla^2 S_\beta(A_t))
  \ge
  c_0 - C_{SU(3)}\,\beta\,r(t)^2.
\]
Define the (static) convexity radius
\[
  R(\beta)^2 := \frac{c_0}{C_{SU(3)}\,\beta}.
\]
Whenever \(r(t) \le R(\beta)\), one has \(\lambda(t)\ge 0\).

---

## 3. Project-form dynamic entry estimate

The project notes contain the differential inequality (in the “unstable” region \(r(t)>R(\beta)\))
\[
  \frac{d}{dt} r(t)^2 \le -2\gamma\,r(t)^2,
  \qquad
  \gamma := C_{SU(3)}\beta r(t)^2 - c_0 > 0,
\]
and after integration,
\[
  r(t)^2 \le r_0^2 e^{-2\gamma t}.
\]

### Warning (audit note)

As written, \(\gamma\) depends on \(r(t)\), hence is not constant; the integrated form requires either:

- replacing \(\gamma\) by a lower bound \(\gamma_\ast\) valid over a time interval, or
- solving a differential inequality with variable coefficient.

A rigorous manuscript version must explicitly address this.

---

## 4. Post-entry Riccati inequality for λ_min

Once \(A_t\) enters the convex region (so that \(\lambda(t)>0\) and the action is uniformly convex along the trajectory), the project asserts a Riccati-type curvature growth:
\[
  \lambda'(t) \ge 2\lambda(t)^2,
\]
which implies monotone increase of \(\lambda(t)\) and prevents later loss of convexity.

Again, the precise derivation depends on the chosen flow and regularity assumptions; it should be proven from the exact identity for \(\frac{d}{dt}\nabla^2 S(A_t)\) along the flow.

---

## 5. τ-envelope: what a proof needs

A proof-ready τ-envelope is a function \(\overline{\tau}(\beta,r)\) such that
\[
  \tau(\beta,r) \le \overline{\tau}(\beta,r)
\]
for all initial conditions with \(\|A_0\|\le r\), uniformly in lattice volume.

A minimal viable envelope structure is:

1. **Entry time to the convex ball** \(r(t)\le R(\beta)\), obtained from a rigorous contraction inequality for \(r(t)\).
2. **Instant curvature stabilization** once in the convex region, provided by the Riccati inequality or any monotone-curvature lemma.

A common target form (depending on the contraction estimate) is:
\[
  \overline{\tau}(\beta,r) \;\sim\; \frac{1}{\alpha(\beta,r)}\log\!\left(\frac{r}{R(\beta)}\right),
\]
or a rational bound derived from the Riccati ODE solution.

---

## 6. Numerical anchor: dynamic restoration observed

The project includes direct simulation evidence that, for a strongly unstable configuration (example: \(L=8\), \(\beta=3.0\), \(r=0.15\)), gradient flow increases \(\lambda_{\min}\) from negative to positive over finite flow time.

This supports (but does not prove) the existence of a finite τ-map.

---

## 7. What to formalize next

To convert this document into a proof component, the project needs:

1. A theorem bounding amplitude decay \(r(t)\) under the chosen flow, in a coordinate-invariant way.
2. A lemma deriving \(\lambda'(t)\ge 2\lambda(t)^2\) (or an alternative monotone positivity mechanism) from the exact evolution equation of the Hessian.
3. A uniformity statement: constants in the τ-envelope must not depend on lattice size \(L\).
