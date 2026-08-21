# Sigma Positivity as a Research Program: From Trace Anomaly to a Rigorous Source Term

**Purpose.** Extract the project’s most important *bottleneck idea* (and a plausible path forward):  
identify the RG/PBH “source term”
\[
\sigma(t,x) = \lambda_{\min}\big(\nabla_H^2 J_t(x)\big)
\]
as something that should be **positive** due to the **trace anomaly / asymptotic freedom**, and then control all remaining corrections with functional inequalities / Lyapunov structure.

This note is primarily a synthesis/roadmap built from `SYNTH_P07_sigma_positivity.md`, `SYNTH_P12_anomaly_source_bound.md`, `SYNTH_P14_rg_flow_stability.md`, and the Haar mechanism notes.

---

## 1. Why \(\sigma>0\) is the “dragon guarding the treasure”

The PBH/Riccati engine (see `EXTRACT_PBH_Riccati_Mass_Gap.md`) essentially says:

> If \(\sigma(t,x)\ge\sigma_*>0\) uniformly (eventually in RG time), then the minimal Hessian eigenvalue is driven to a strictly positive fixed point \(\Rightarrow\) mass gap.

So the mass-gap problem is reduced to one hard thing:

\[
\boxed{\text{Prove a uniform positive lower bound on the anomaly Hessian in physical directions.}}
\]

That’s Conjecture-B-flavored, whether we call it a conjecture or a theorem-in-progress.

---

## 2. Decomposing the source term

A good way to avoid mystical thinking is to split the source into pieces that can be attacked separately:
\[
\sigma_{\mathrm{eff}} = \sigma_{\mathrm{Haar}} + \sigma_{\mathrm{anom}} + \sigma_{\mathrm{corr}}.
\]

### 2.1 \(\sigma_{\mathrm{Haar}}\): geometric/entropic baseline

The project’s Haar geometry notes motivate a strictly positive baseline from:
- intrinsic Ricci curvature of \(SU(N)\),
- the exponential Jacobian concentration near identity.

This is the easiest positivity you’ll ever get from a gauge theory.

### 2.2 \(\sigma_{\mathrm{anom}}\): trace anomaly sign

In continuum Euclidean YM, the trace anomaly schematically reads
\[
T^\mu_{\ \mu}
\propto \frac{\beta(g)}{2g^3}\,\mathrm{tr}(F_{\mu\nu}F^{\mu\nu}).
\]
For asymptotically free theories, \(\beta(g)<0\) at small \(g\), and \(\mathrm{tr}(F^2)\ge 0\) in Euclidean signature.

Heuristically this sign structure suggests:
- the RG forcing \(J_t\) is sign-definite,
- and its *second variation* in physical directions is nonnegative.

That’s the conceptual core behind “\(\sigma_{\mathrm{anom}}\ge 0\).”

### 2.3 \(\sigma_{\mathrm{corr}}\): the enemy you hope is small

Corrections come from:
- higher-loop terms,
- operator mixing,
- curvature/non-integrability terms from the quotient geometry,
- finite-cutoff artifacts.

The PBH stability logic wants these to be **\(O(g^4)\)** compared to the \(O(g^2)\) leading anomaly forcing, so asymptotic freedom can crush them as \(t\to\infty\).

---

## 3. The Lyapunov bridge: turning “small corrections” into a theorem

This is one of the project’s more “exportable” ideas:

> Use **functional inequalities** (Poincaré/LSI) produced by curvature/Lyapunov conditions to control fluctuation terms that would otherwise spoil positivity.

A typical pattern is:

1. Find a Lyapunov function \(W\ge 1\) such that the generator \(L\) satisfies  
   \[
   LW \le -a W + b\mathbf{1}_{K}
   \quad\text{(outside a compact set \(K\))}.
   \]
2. This implies a global Poincaré inequality (and sometimes LSI) for the invariant measure.
3. Poincaré/LSI gives concentration and bounds on nonlinear terms.
4. Use those bounds to show
   \[
   \sigma_{\mathrm{corr}}
   \ge -C g(t)^2 \cdot \text{(controlled quantity)}
   \]
   with the controlled quantity uniformly bounded.

This is the “analytic insurance policy” that could make \(\sigma_{\mathrm{eff}}>0\) stable.

---

## 4. A concrete “proof-shaped” target statement

A clean target theorem (finite cutoff) would look like:

> **Target:** There exist \(T_0\) and \(\sigma_*>0\) such that for all \(t\ge T_0\),
> \[
> \nabla_H^2 J_t \ \ge\ \sigma_*\,\mathrm{Id}
> \quad\text{on physical directions, uniformly in }x\in\mathcal{M}_{\mathrm{reg}}.
> \]

One can try to prove this by showing:

1. **Leading term positivity:** \(\nabla_H^2 \int\mathrm{tr}(F^2)\ge 0\) on physical modes (modulo gauge).
2. **Correct sign in front:** the RG coefficient is \(+\bigl(-\beta(g)/g^3\bigr)\ge 0\).
3. **Error control:** higher-order terms are dominated by the leading term in operator sense, using Poincaré/LSI + asymptotic freedom.

---

## 5. Why this might connect to broader theory

If this program works, it suggests a general philosophy:

- RG flow has a hidden parabolic structure (vHJ/PBH),
- anomalies act as **positive sources** for convexity,
- convexity of effective actions is the common currency behind:
  - mass gaps,
  - spectral gaps,
  - concentration/LSI,
  - and perhaps even monotonicity theorems.

That sounds like the start of a “geometric renormalization” toolkit, not just a YM proof attempt.

---

## 6. Practical next steps

To expand this into a publishable result, the next steps are very concrete:

1. **Pick a specific RG formalism** (FRG/Wetterich is the cleanest for differentiating w.r.t. scale).
2. **Compute \(J_t\) and its second variation** in a controlled truncation, with explicit projection to physical modes.
3. **Bound the remainder terms** using concentration (LSI) estimates that are uniform in volume/cutoff.
4. **Test numerically on small lattices**: compute the minimal eigenvalue of \(\nabla_H^2 J_t\) along an RG trajectory.

The “sigma positivity” bottleneck is tough, but it is also unusually *well-posed*: it’s a sign problem for a quadratic form, not an amorphous QFT mystery.
