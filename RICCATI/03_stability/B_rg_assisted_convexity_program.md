---
title: "RG-Assisted Convexity → Functional Inequalities → Gap (Speculative Program)"
format: "markdown+latex"
status: "Research sketch: standard finite-dimensional theorem + speculative YM lift"
---

## 0. Scope and epistemic status

This document extracts another potentially “exciting” direction from the chat:

> Use renormalization (coarse-graining) to reach a scale where an **effective action** becomes sufficiently “convex” (in a suitable sense), then invoke **Bakry–Émery / Poincaré / log-Sobolev** technology to obtain a spectral gap for an associated generator, and finally connect that gap to the physical mass gap.

The finite-dimensional Bakry–Émery implications are standard. The novelty (if any) is the proposed *order of operations* for Yang–Mills: **RG first, convexity second**.

---

## 1. The standard finite-dimensional theorem (anchor point)

Let \(\mu\) be a probability measure on \(\mathbb R^n\):
\[
\mu(dx)=Z^{-1}e^{-S(x)}\,dx,
\]
with \(S\in C^2\).

Define the Langevin generator:
\[
L f = \Delta f - \nabla S\cdot \nabla f.
\]

Assume the Bakry–Émery curvature condition:
\[
\nabla^2 S(x)\succeq \rho I_n\quad\text{for all }x,
\qquad \rho>0.
\]

Then one has a Poincaré inequality:
\[
\mathrm{Var}_\mu(f)\le \frac{1}{\rho}\int \|\nabla f\|^2\,d\mu,
\]
equivalently a spectral gap:
\[
\lambda_1(-L)\ge \rho.
\]

This is rigorous, textbook material in finite dimensions.

---

## 2. The naïve lift to YM fails (and why)

For lattice YM, one has a Gibbs measure on a compact product space:
\[
\mu(dU)\propto e^{-S_E(U)}\prod_{\text{links}} dU_{\text{Haar}}.
\]

Two immediate obstacles block a direct Bakry–Émery lift:

1. The configuration space is not \(\mathbb R^n\) but a product of compact groups with gauge redundancy.
2. The action \(S_E\) is not globally convex; gauge invariance creates flat directions.

So a “global Hessian \(\ge \rho I\)” statement is generally false.

---

## 3. The RG-assisted idea (the potentially new move)

Introduce a coarse-graining map (blocking factor \(b\)):
\[
\mathcal R_b:\ (S,a)\mapsto (S_{\mathrm{eff}}, a' = ba),
\]
where \(S_{\mathrm{eff}}\) is the effective action after integrating out UV degrees of freedom.

**Key heuristic:** integrating out UV modes may generate an effective action that is
*more coercive* in the remaining IR degrees of freedom, even if the bare action is not.

So the speculative plan is:

1. Perform several RG steps to reach a scale where the remaining theory is “massive-like”.
2. Prove a *scale-dependent* functional inequality (Poincaré/log-Sobolev) for \(\mu_{\mathrm{eff}}\propto e^{-S_{\mathrm{eff}}}\).
3. Translate that inequality into a **uniform** spectral gap statement for an associated generator at that scale.
4. Transfer the implication back to the original lattice model (using stability under RG steps).
5. Take \(a\to 0\) while preserving a nontrivial lower bound.

Symbolically:
\[
\mu \xrightarrow{\mathrm{RG}} \mu_{\mathrm{eff}}
\;\Rightarrow\;
\text{(Poincaré/LSI for }\mu_{\mathrm{eff}}\text{)}
\;\Rightarrow\;
\text{gap for generator}
\;\Rightarrow\;
\text{mass gap}.
\]

---

## 4. A concrete intermediate object: stochastic quantization

Stochastic quantization (Langevin evolution on configuration space) provides a canonical generator \(L_{\mathrm{YM}}\) whose invariant measure is \(\mu\).

If one could prove a Poincaré inequality (or log-Sobolev inequality) for \(\mu\) with constant uniform in volume and lattice spacing (after appropriate scaling), one would obtain a uniform spectral gap for \(-L_{\mathrm{YM}}\).

The speculative bridge is then:

- uniform gap for a physically natural generator \(L_{\mathrm{YM}}\),
- plus reflection positivity / reconstruction input,
- implies exponential clustering for Euclidean correlators,
- hence a physical mass gap.

This bridge is not automatic; it is a programmatic direction.

---

## 5. Testable subproblems

### 5.1 Numerical RG + convexity diagnostics

On small SU(2) lattices:

1. Run a blocking procedure producing \(S_{\mathrm{eff}}\) in a parameterized ansatz family.
2. Estimate local convexity proxies (e.g., Hessian spectrum of an effective potential in a chosen coordinate chart).
3. Estimate Poincaré/LSI constants numerically for \(\mu_{\mathrm{eff}}\) via Markov chain mixing diagnostics.

Look for “convexification after RG” as a reproducible phenomenon.

### 5.2 Prove something in a controlled cousin model

Look at a model where cluster expansions or strong-coupling methods *do* give exponential decay (hence a gap-like behavior), and re-derive that exponential decay using an LSI/Poincaré inequality post-RG.

Even if this works only in a regime (strong coupling), it could provide a blueprint for “functional inequality proofs of clustering” that might be extensible.

---

## 6. Connection to larger theory

This direction ties together:

- **Renormalization** (coarse-graining/flow),
- **functional inequalities** (Poincaré/log-Sobolev),
- **Markov semigroups** (stochastic quantization),
- **constructive QFT** (OS reconstruction / reflection positivity).

If successful, it reframes the mass gap as an inequality about the geometry of the renormalized measure, rather than a direct spectral estimate on the microscopic Hamiltonian.

---

## 7. What would count as genuine progress

Not “the action seems stiff”.

Progress would be:

1. A statement of the form:
\[
\mathrm{Var}_{\mu_{\mathrm{eff}}}(f)\le C \,\mathcal E_{\mathrm{eff}}(f,f),
\]
with \(C\) uniform in volume for a nontrivial effective measure \(\mu_{\mathrm{eff}}\).

2. A proof that this inequality is stable under one inverse-RG step (lifting back to the fine lattice).

3. A path to controlling the \(a\to 0\) limit while retaining \(C<\infty\).

Even partial theorems of this type in a simplified gauge model would be credible steps toward a new approach.
