---
title: "EXTRACT 04 — Conjecture B Reframed: Positivity of the RG-Hessian Source on Physical Directions"
project: "SWIM2"
source_files:
  - "SYNTH_CONJ_B_anomaly_source.md"
  - "UNIF_CONJB_STRATEGY.md"
  - "SYNTH_P07_sigma_positivity.md"
  - "SYNTH_P12_anomaly_source_bound.md"
status: "extracted synthesis"
---

# Conjecture B Reframed: Positivity of the RG-Hessian Source on Physical Directions

## Abstract

The project’s most leverage-heavy open hypothesis is a positivity statement:

> In the RG evolution of the *physical* (horizontal) Hessian, the “source term” that is not \(-H^2\) is **nonnegative** as a quadratic form.

In the project’s notation this is Conjecture B:
\[
S_{\mathrm{anom}}\big|_{\mathrm{hor}} \ge 0.
\]

This note extracts the conjecture in its most actionable form, clarifies what would count as a proof, and explains why several different objects (Wilson Hessian, trace anomaly, measure curvature) get conflated in the current writeup — and how to disentangle them.

---

## 1. The equation where Conjecture B lives

The PBH/RG-Hessian schematic evolution is:
\[
\frac{d}{dt} H_{\mathrm{phys}}(t)
=
- H_{\mathrm{phys}}(t)^2
+
S_{\mathrm{Haar}}
+
S_{\mathrm{anom}}
+
(\text{controlled corrections}).
\]

Conjecture B is the statement:
\[
\langle v, S_{\mathrm{anom}}(t,x) v\rangle \ge 0
\quad\text{for all unit physical }v,
\text{ uniformly in }(t,x).
\]

If true, and if \(S_{\mathrm{Haar}}\ge c_0 I\) (another project pillar), then the combined source is uniformly positive, feeding the Riccati comparison mechanism (EXTRACT 02).

---

## 2. The “three-pronged” positivity architecture

The project repeatedly organizes the positivity of the effective source \(\sigma_{\mathrm{eff}}\) as:

- **Prong A:** geometric/Haar positivity (a curvature floor),
- **Prong B:** anomaly/source positivity (this conjecture),
- **Prong C:** control of corrections (Lyapunov / functional inequalities).

A key virtue of this split is that each prong can be attacked with different tools.

---

## 3. Important clarification: what exactly is “the anomaly source”?

Right now “\(S_{\mathrm{anom}}\)” is used for multiple, not-identical things:

1. **Trace anomaly / beta function physics:**  
   \(J_t\sim\int \beta(g)\,\mathrm{tr}\,F^2\), so \(S_{\mathrm{anom}}=\nabla_H^2J_t\).

2. **Wilsonian operator mixing (FRG/Wetterich):**  
   Differentiating the Wetterich equation twice gives a flow for \(\Gamma^{(2)}\) with “source terms” coming from higher vertices and regulator kernels.

3. **Wilson-action Hessian positivity near identity:**  
   The object \(\nabla^2 S_\beta\big|_{\mathrm{hor}}\ge \beta c_W g\) is *not* an anomaly; it’s the local convexity of the bare lattice action in physical directions.

4. **Bakry–Émery curvature floor:**  
   \(\mathrm{Ric}_\mu = \mathrm{Ric}_g + \nabla^2 S\) is a *geometric* source of coercivity, not a trace anomaly.

These are related, but not interchangeable. A clean proof strategy requires committing to **one** definition of \(S_{\mathrm{anom}}\) and showing it is positive.

---

## 4. What is already “proved on the lattice” (in project terms)

The strongest lattice-level input in the project is:

> Near the identity/small-field region, the Bakry–Émery tensor on horizontals satisfies
\[
\mathrm{Ric}_{\mu_\beta}\big|_{\mathrm{hor}} \ge (\kappa + \beta c_W) g.
\]

This is a *strict positivity* statement, but it is a statement about **\(\mathrm{Ric}_{\mu_\beta}\)**, not directly about \(S_{\mathrm{anom}}\) as a time-dependent RG forcing.

So: it provides strong evidence that **a positive source exists** at least in a local region and at a fixed cutoff, but it does not automatically settle Conjecture B for the full RG-Hessian flow.

---

## 5. Three concrete routes to a proof (and what each would need)

### Route 1: Spectral/positivity representation (OS / reflection positivity)

Goal: represent \(\langle v,S_{\mathrm{anom}}v\rangle\) as an integral of a positive spectral density (Källén–Lehmann style), then invoke reflection positivity.

Hard part: build a rigorous identification between the RG forcing term in the Hessian flow and a reflection-positive quadratic form of local observables.

### Route 2: Functional RG (Wetterich/Polchinski) with a positivity-preserving regulator

Goal: show that in a gauge-fixed-but-projected scheme,
\[
\partial_t \Gamma_t^{(2)} = -\Gamma_t^{(2)}\,K_t\,\Gamma_t^{(2)} + \mathcal{S}_t
\]
has \(\mathcal{S}_t\ge 0\) on physical modes, where \(K_t\ge 0\).

Hard part: keep gauge invariance under control while maintaining positivity under projection.

### Route 3: “Bakry–Émery source” interpretation

Goal: interpret the driving term as a Bakry–Émery curvature lower bound:
\[
S_{\mathrm{source}} \equiv \mathrm{Ric}_\mu \;\text{or}\; \nabla^2 S_{\mathrm{eff}},
\]
and then prove convexity directly (e.g. via gauge-fixing quadratic terms and Wilson Hessian positivity).

Hard part: globalize beyond the local small-field region and show the right notion of “source” matches what PBH/Riccati uses along RG.

---

## 6. A clean restatement that would be publishable as a conjecture

Here is a version that avoids conflating objects:

> **Conjecture B′ (Positive physical forcing in Hessian RG flow).**  
> Fix a concrete RG scheme (e.g. gradient flow effective action, or FRG with specified regulator and gauge fixing) and define the projected physical Hessian \(H_{\mathrm{phys}}(t)\). Then there exists a local, gauge-invariant forcing tensor \(S_{\mathrm{phys}}(t)\) such that
> \[
> \frac{d}{dt}H_{\mathrm{phys}}(t) = -H_{\mathrm{phys}}(t)^2 + S_{\mathrm{phys}}(t) + \text{(terms controlled by asymptotic freedom)},
> \]
> and
> \[
> S_{\mathrm{phys}}(t)\ge 0
> \quad\text{as a quadratic form for all }t.
> \]

This is the precise positivity input needed by the PBH comparison argument.

---

## 7. What to do next (high-value steps)

1. **Choose and freeze a definition of \(S_{\mathrm{anom}}\).**  
   (Gradient flow forcing? FRG vertex source? Something else?)

2. **Prove positivity in a controlled regime** (near identity, high-\(\beta\), weak coupling) and quantify constants.

3. **Design a continuation argument** (Lyapunov barrier / tightness / concentration) to move from local-in-field-space positivity to global statements.

4. **Connect the “curvature floor” to the time-dependent source** in the PBH flow: show exactly how the same positivity appears in the Hessian evolution equation, not just in the static Gibbs measure.

