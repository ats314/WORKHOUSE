# Curvature-Flow Mass Gap Engine (PBH/Riccati with Anomaly Source)

## Abstract

This document isolates a nonperturbative **mechanism** for generating a positive infrared scale from a curvature-flow inequality on an effective action.
The core is a Riccati-type inequality for the **minimal horizontal Hessian eigenvalue**
\[
\lambda_{\min}(t)\ :=\ \min \sigma\bigl(h_t\bigr),\qquad h_t := \mathrm{Hess}_H\, S_t,
\]
whose source term is identified with an **anomaly / gauge-fixing curvature source**.

The mechanism is modular:

1. a tensor parabolic inequality for \(h_t\) on the regular gauge orbit space,
2. a reduction to a scalar differential inequality for \(\lambda_{\min}(t)\),
3. a comparison with an autonomous Riccati ODE,
4. an explicit positive fixed point \(\sqrt{\sigma/2}\) giving a persistent scale.

The project corpus provides: (i) a complete Riccati ODE analysis; (ii) an explicit lattice gauge-fixing source term \(\sigma_A \ge N g_0^2 a^2/6\); (iii) a conditional RG/pBH stability theorem under explicit geometric hypotheses.

---

## 1. Objects

### 1.1 Effective action and horizontal Hessian

Let \(S_t\) denote a scale-dependent effective action defined on the **regular stratum** of the gauge orbit space
\[
\mathcal{M}_{\mathrm{reg}} = \mathcal{A}_{\mathrm{reg}}/\mathcal{G}.
\]
Let \(H_A \subset T_A\mathcal{A}\) be the horizontal subspace defined by a gauge condition (e.g. background gauge).
Define the **horizontal Hessian**
\[
h_t := \mathrm{Hess}_H\, S_t,
\]
a symmetric bilinear form on \(H\).

Define the **minimal eigenvalue** function
\[
\lambda_{\min}(t,x) := \min_{v\in H_x,\ \|v\|=1}\langle v,\ h_t(x)\, v\rangle,
\qquad
\lambda_{\min}(t):=\inf_{x\in\mathcal{M}_{\mathrm{reg}}}\lambda_{\min}(t,x).
\]

---

## 2. PBH / viscous-HJ-type flow and the Riccati sink

The corpus models the scale-flow of \(S_t\) using a viscous Hamilton–Jacobi structure (a “geometric RG analogue”):
\[
\partial_t S = \Delta S - |\nabla S|^2,
\]
together with gauge-projected corrections in the orbit space setting.

At the level of Hessians, the project formulates an evolution of the schematic form
\[
\partial_t h_t \;\gtrsim\; \Delta_H h_t \;-\; 2 h_t^2 \;+\; S_{\mathrm{anom}}(t)\;+\;\mathfrak{G}(t),
\]
where:

- \(\Delta_H\) is a horizontal Laplacian,
- \(-2h_t^2\) is a **Riccati sink** term (drives convexity loss),
- \(S_{\mathrm{anom}}\) is an **anomaly source** term (drives convexity creation),
- \(\mathfrak{G}\) is a geometric correction term (orbit-space curvature and trace effects).

This decomposition is the central organizing idea: **convexity is stabilized when the source dominates the Riccati sink and corrections.**

---

## 3. Scalar inequality for the minimal eigenvalue (interface)

The corpus provides the following reduction, under explicit hypotheses (curvature bound and trace bound).

### Proposition (Riccati-type inequality for \(\lambda_{\min}\))

Assuming the PBH/tensor flow structure and a tensor maximum principle on \(\mathcal{M}_{\mathrm{reg}}\), the minimal eigenvalue satisfies
\[
\partial_t \lambda_{\min}(t) \;\ge\; -2\lambda_{\min}(t)^2 \;+\; \sigma_A \;-\; C_1 g(t)^2 H_{\mathrm{Tr}}.
\tag{3.1}
\]
Here:

- \(\sigma_A\) is a lower bound for the anomaly source on horizontals,
- \(g(t)\) is the running coupling (asymptotically free in the intended regime),
- \(H_{\mathrm{Tr}}\) bounds the trace of the positive part of \(h_t\),
- \(C_1\) is a geometric constant arising from the curvature correction estimate.

In the asymptotically free regime, the correction term is dominated and one obtains a **clean Riccati inequality**
\[
\partial_t \lambda_{\min}(t) \;\ge\; -2\lambda_{\min}(t)^2 + \frac{\sigma_A}{2}.
\tag{3.2}
\]

---

## 4. Riccati ODE comparison and the emergent fixed scale

Consider the autonomous Riccati ODE
\[
\dot \lambda = -2\lambda^2 + \sigma,\qquad \sigma>0.
\tag{4.1}
\]
The project corpus contains a full ODE analysis establishing:

- global existence of solutions,
- a stable positive fixed point \(\lambda_+ = \sqrt{\sigma/2}\),
- a quantitative lower bound on \(\liminf_{t\to\infty}\lambda(t)\) whenever \(\sigma(t)\ge \sigma_{\min}>0\).

### Structural Principle: Source–Sink Fixed Point

If \(\lambda_{\min}(t)\) satisfies (3.2), then comparison with (4.1) yields an eventual uniform lower bound
\[
\lambda_{\min}(t)\ \gtrsim\ \sqrt{\sigma_A/4}.
\]
The project interprets the corresponding infrared value as a **mass scale**
\[
m_{\mathrm{Riccati}} \ :=\ \sqrt{\sigma/2}.
\]

---

## 5. A concrete lattice source term (Prong C)

A key concrete input is an explicit gauge-fixing quadratic term in the lattice-algebra parametrization \(A\in\mathbb{R}^M\):
\[
S_{FP}(A) = \frac{N g_0^2 a^2}{12}\,\|A\|^2.
\tag{5.1}
\]
Its Hessian is constant:
\[
\mathrm{Hess}(S_{FP}) \;=\; \frac{N g_0^2 a^2}{6}\, I.
\tag{5.2}
\]
Thus the corpus records a uniform positive lower bound
\[
\sigma_A \;\ge\; \frac{N g_0^2 a^2}{6} \;>\;0
\tag{5.3}
\]
in the lattice gauge-fixed setting.

This is the **explicit quantitative source** needed for (3.1)–(3.2) at finite lattice spacing.

---

## 6. Conditional persistence theorem (the core nonperturbative engine)

### Conditional Theorem (Gap persistence under RG flow)

Assume:

1. **(Anom)** a uniform horizontal anomaly source floor \(\sigma_A>0\),
2. **(Curv)** an orbit-space curvature estimate of the form \(|K|\lesssim g(t)^2\) needed to control \(\mathfrak{G}\),
3. **(Trace)** a uniform bound on the trace of the positive part of \(h_t\),
4. **(AF)** asymptotic freedom: \(g(t)\to 0\),
5. **(Init)** a strictly positive \(\lambda_{\min}\) at some finite RG time.

Then there exists \(T_1\) and \(\sigma_{\min}>0\) such that for all \(t\ge T_1\),
\[
\lambda_{\min}(t)\ \ge\ \sigma_{\min}\ >\ 0.
\tag{6.1}
\]
Interpretation: the horizontal effective action becomes **uniformly convex** at sufficiently large RG times, in the relevant (local) sector.

---

## 7. Interfaces to “physics” (not closed inside this corpus)

The mechanism above produces a persistent **convexity / functional-inequality scale**. To turn this into a physical mass gap requires interfaces that are currently explicit conjectures in the corpus:

- **Conjecture D:** local-sector spectral gap (Dirichlet/Langevin) \(\Rightarrow\) physical mass gap via OS reconstruction.
- **Conjecture IR:** separation of local mixing from slow global/topological modes.

Thus the PBH/Riccati engine is best viewed as an **analytic mass-scale generator** whose output must be connected to correlation decay via OS/transfer machinery.

---

## 8. What appears new (within the corpus)

### Pipeline Architecture
A modular chain:
\[
\text{(Anomaly source)}\ +\ \text{(PBH flow)}\ \Longrightarrow\ \text{Riccati inequality for }\lambda_{\min}
\Longrightarrow\ \text{positive fixed point}.
\]

### Rigidity Mechanism
The output \(\sqrt{\sigma/2}\) is insensitive to detailed ultraviolet structure once a source floor \(\sigma>0\) is established and corrections are \(o(1)\).

---

## 9. Minimal technical upgrades that would enlarge the theorem

To move the conditional theorem closer to an unconditional statement, the sharp missing steps are:

1. a fully explicit derivation (not schematic) of the tensor flow and the correction decomposition in the orbit-space setting;
2. a quantitative, nonperturbative bound on \(\mathfrak{G}\) implying (Curv) and (Trace);
3. an explicit local-sector OS bridge (Conjecture D/IR).