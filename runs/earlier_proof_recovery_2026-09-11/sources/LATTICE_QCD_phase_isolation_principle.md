# Phase-Isolation Principle for θ-Terms in Tensor Networks
*(A unifying “working theory” distilled from the project’s rotor + U(1) gauge constructions.)*

## Abstract

Many lattice models with a topological angle have a partition function of the form

\[
Z(\theta)=\sum_{\mathcal C} w_0(\mathcal C)\,e^{i\theta\,Q(\mathcal C)},
\qquad
w_0(\mathcal C)\ge 0,\quad Q(\mathcal C)\in\mathbb Z,
\]

where \(Q\) is an **integer-valued** topological charge (winding number, flux sum, instanton number, …).
The *Phase-Isolation Principle* is the observation that when \(Q\) is **additive** and the \(\theta=0\) weights are **locally non-negative**, one can often build a tensor network (TN) that computes the **sector weights**
\(\{Z_Q^{(0)}\}_{Q\in\mathbb Z}\) with **strictly non-negative local tensors**, and then restore the \(\theta\)-dependence only at the end via

\[
Z(\theta)=\sum_{Q\in\mathbb Z} e^{i\theta Q} Z_Q^{(0)}.
\]

This reframes the “sign problem from a \(\theta\)-term” as a **boundary evaluation problem** (or equivalently, an evaluation of a positive-coefficient generating function on the unit circle).

This document formalizes the idea at a level useful for design and error analysis.

---

## 1. Sector decomposition as a generating function

Assume:

1. **Integer charge:** \(Q(\mathcal C)\in \mathbb Z\).
2. **Additivity:** \(Q(\mathcal C)\) can be written as a sum of local increments,
   \[
   Q(\mathcal C)=\sum_{c\in\text{cells}} q_c(\mathcal C),\qquad q_c(\mathcal C)\in\mathbb Z.
   \]
3. **Positivity at \(\theta=0\):** the local Boltzmann factors at \(\theta=0\) can be chosen non-negative.

Then define the **sector weights**
\[
Z_Q^{(0)} := \sum_{\mathcal C:\,Q(\mathcal C)=Q} w_0(\mathcal C)\quad\ge 0.
\]

Equivalently, define the **charge-generating function**
\[
P(z) := \sum_{Q\in\mathbb Z} Z_Q^{(0)}\,z^{Q}.
\]
When the above assumptions hold, \(P\) has **non-negative real coefficients**, and

\[
Z(\theta) = P(e^{i\theta}).
\]

### Why this is structurally powerful

- The complex phase \(e^{i\theta Q}\) is not “spread throughout the bulk” as oscillatory local factors; it is a **final evaluation** of a real non-negative object.
- Once \(P(z)\) (or the coefficients \(Z_Q^{(0)}\)) are available, one can evaluate \(Z(\theta)\) at *many* \(\theta\) values cheaply, and one can compute moments of \(Q\) by derivatives at \(z=1\).

---

## 2. Two equivalent implementations

### 2.1 Boundary-phase form (explicit sector sum)

Design a TN that directly computes \(Z_Q^{(0)}\) (or a truncated set of them), then multiply by \(e^{i\theta Q}\) and sum.

This is exactly what the 1D rotor construction does: the bulk TN stays non-negative, while the \(\theta\)-term appears as a boundary factor \(e^{ik\theta}\) in the final winding sum.

### 2.2 Polynomial / Laurent-polynomial TN (evaluation at \(z=e^{i\theta}\))

Instead of computing every coefficient explicitly, build a TN whose contraction yields the polynomial \(P(z)\).

A very useful “engineering” form is a **polynomial transfer matrix**:

\[
W(z) = \sum_{\Delta Q\in\mathbb Z} W^{(\Delta Q)}\, z^{\Delta Q},
\qquad
W^{(\Delta Q)}\ge 0\ \text{entrywise}.
\]

Then for \(N\) time steps (or layers),
\[
Z(\theta)=\operatorname{Tr}\big(W(e^{i\theta})^N\big),
\]
and coefficient extraction of \(W(z)^N\) yields the sector weights.

This is exactly the interacting rotor’s “polynomial matrix representation” idea (a pragmatic way to keep the bulk real/non-negative while deferring the phase).  

---

## 3. A minimal “Phase-Isolation Lemma”

> **Lemma (Phase isolation via positive coefficients).**  
> Suppose a model admits a representation \(P(z)=\sum_Q Z_Q^{(0)} z^Q\) such that all \(Z_Q^{(0)}\ge 0\).  
> Then \(Z(\theta)=P(e^{i\theta})\) can be evaluated without any internal sign cancellations in the computation of the coefficients \(Z_Q^{(0)}\).

**Proof sketch.** The coefficients are sums of non-negative local contributions, so their computation (by TN contraction, transfer matrix multiplication, dynamic programming, etc.) never subtracts nearly equal numbers with opposite signs. Any oscillation comes only from the *final* linear combination \(\sum_Q e^{i\theta Q}Z_Q^{(0)}\), not from the internal aggregation. ∎

This is not just “numerical niceness”: it is the structural reason the rotor / U(1) Villain TNs avoid Monte Carlo’s exponential “average-sign collapse.”

---

## 4. Error control lives in the tails of \(Q\)

Phase isolation makes the *source* of complexity explicit: you pay for the width of the distribution of \(Q\).

For many Gaussian-type models (Villain kernels, diffusion on a circle, etc.), tail probabilities are Gaussian:

\[
\mathbb P(|Q|>Q_{\max}) \lesssim \exp\big(-c\,Q_{\max}^2\big).
\]

So truncating to \(|Q|\le Q_{\max}\) often has a **super-polynomial** (Gaussian) suppression.  
In the rotor archive, the winding cutoff \(K_{\max}\) scales like \(\sqrt{\beta\ln(1/\varepsilon)}\).

---

## 5. Connecting the project’s constructions into a “bigger theory”

The project’s most “theory-shaped” idea is:

> **Working hypothesis (general sign-problem deferral).**  
> Whenever a topological term couples to an **additive integer charge** \(Q\), one should try to represent the partition function as a **positive-coefficient generating function** in \(z=e^{i\theta}\), pushing all complex structure into a final evaluation step.

This is a unifying lens across:
- 1D rotor winding sectors,
- 2D U(1) Villain flux sectors (where a strict \(Q\)-sector TN is proposed but not yet built),
- exploratory attempts to replicate the trick for SU(2), where the *vertex intertwiners* introduce unavoidable sign/phase structure in the standard fusion basis (suggesting an obstruction that needs a different set of variables).

---

## 6. Research directions implied by the principle

1. **2D U(1) strict sector TN (engineering):** build an explicit accumulator/charge-MPO that outputs \(Z_Q^{(0)}(\beta)\) with non-negative tensors, then evaluate \(Z(\theta)\).
2. **FFT / roots-of-unity evaluation:** compute \(P(z)\) on \(z=e^{2\pi i m/M}\) for many \(m\), invert discrete Fourier transform to recover \(\{Z_Q^{(0)}\}\). This can amortize the cost of many \(\theta\) points.
3. **Non-Abelian obstruction analysis:** determine whether the “phase-isolation lemma” can be extended to non-Abelian \(\theta\)-terms by moving to a dual formulation where the relevant topological charge becomes additive over local integers (or by identifying categorical/topological symmetry variables that play the role of \(Q\)).
4. **Complex-TN philosophy:** if strict local positivity is impossible (as in the SU(2) fusion-basis story), the principle still helps: you explicitly identify *where* phases must live (often intertwiners), and then optimize for deterministic TRG/TNR contraction instead of sampling.

---

## Sources in the project

- Proposed strict \(Q\)-sector decomposition for 2D U(1) Villain: `TN_2D_U1_Detail_v2.md`.
- Rotor winding cutoff and Gaussian truncation bound: `TN_1D_Rotor_Detail_v2.md`.
- Polynomial transfer matrix and “boundary-only θ”: interacting rotor construction notes.
- SU(2) fusion-basis obstruction discussion and roadmap.

