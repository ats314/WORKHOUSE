---
title: "Rulebook Entry 02 — Reflection Positivity Preserved Under Coarse-Graining Pushforward"
author: ""
date: "2025-12-31"
---

# Rulebook Entry 02 — Reflection Positivity Preserved Under Coarse-Graining Pushforward

This note is **stand‑alone**. It defines reflection positivity in the Osterwalder–Schrader (OS) sense,
defines a broad class of deterministic coarse‑graining maps, and proves that **reflection positivity
is preserved** under pushforward by any coarse‑graining map that is compatible with the reflection and with
“positive time”.

The result is a canonical example of *admissibility as a structural inequality calculus*:
a positivity inequality survives a model transformation.

---

## 1. OS reflection setup

Let \((\Omega,\mathcal F,\mu)\) be a probability space.

### 1.1 Reflection on configurations

A **reflection** is a measurable involution
\[
\Theta:\Omega\to\Omega,\qquad \Theta^2=\mathrm{id}.
\]

### 1.2 Reflected observables

Let \(\mathcal B(\Omega)\) denote the bounded complex measurable functions on \(\Omega\).
Define the induced **antilinear** involution \(\theta:\mathcal B(\Omega)\to\mathcal B(\Omega)\) by
\[
(\theta F)(\omega) := \overline{F(\Theta\omega)}.
\]
Then \(\theta(\lambda F + G)=\overline{\lambda}\,\theta F + \theta G\) and \(\theta(\theta F)=F\).

### 1.3 Positive‑time algebra

Fix a linear subspace (typically an algebra) \(\mathcal A_+\subseteq \mathcal B(\Omega)\)
intended to represent observables supported in “nonnegative time”.

We do **not** need to model time translations here; the argument below uses only \((\Theta,\theta,\mathcal A_+)\).

---

## 2. Reflection positivity

### 2.1 OS bilinear form

Define the OS sesquilinear form on \(\mathcal A_+\) by
\[
\langle F,G\rangle_{\mathrm{OS}} := \int_\Omega (\theta F)(\omega)\,G(\omega)\,d\mu(\omega)
= \mu\big((\theta F)G\big).
\]

### 2.2 Reflection positivity condition

The measure \(\mu\) is **reflection positive on \(\mathcal A_+\)** if
\[
\mu\big((\theta F)F\big)\ \ge\ 0
\qquad \forall\,F\in\mathcal A_+.
\]
Equivalently, \(\langle F,F\rangle_{\mathrm{OS}}\ge 0\) for all \(F\in\mathcal A_+\).

---

## 3. Deterministic coarse‑graining and pushforward

### 3.1 Coarse‑graining map

Let \((\Omega',\mathcal F')\) be another measurable space. A **deterministic coarse‑graining map**
is a measurable function
\[
P:\Omega\to\Omega'.
\]

Define the **pushforward** measure \(\mu'\) on \((\Omega',\mathcal F')\) by
\[
\mu' := P_{\#}\mu,
\qquad
\mu'(B) := \mu(P^{-1}(B))\ \ (B\in\mathcal F').
\]
Equivalently, for bounded measurable \(G:\Omega'\to\mathbb C\),
\[
\int_{\Omega'} G\,d\mu' = \int_\Omega (G\circ P)\,d\mu.
\]

### 3.2 Reflection equivariance

Assume \(\Omega'\) is also equipped with a reflection \(\Theta':\Omega'\to\Omega'\).
We say \(P\) is **reflection equivariant** if
\[
P\circ\Theta = \Theta'\circ P.
\]
This is the exact compatibility needed for reflection positivity to transport.

### 3.3 Positive‑time compatibility

Let \(\mathcal A_+'\subseteq\mathcal B(\Omega')\) be a chosen positive‑time algebra on \(\Omega'\).

We say \(P\) is **positive‑time compatible** if for every \(G\in\mathcal A_+'\),
the pullback \(G\circ P\) lies in \(\mathcal A_+\):
\[
G\in\mathcal A_+' \quad\Longrightarrow\quad G\circ P\in\mathcal A_+.
\]

Intuition: coarse‑graining must not turn a positive‑time observable into one that depends on negative‑time degrees of freedom.

---

## 4. The pushforward permanence theorem

### Theorem 4.1 (Reflection positivity preserved by reflection‑equivariant pushforward)

Assume:
1. \(\mu\) is reflection positive on \(\mathcal A_+\).
2. \(P:\Omega\to\Omega'\) is reflection equivariant: \(P\circ\Theta=\Theta'\circ P\).
3. \(P\) is positive‑time compatible: \(G\in\mathcal A_+'\Rightarrow G\circ P\in\mathcal A_+\).
4. \(\mu' = P_{\#}\mu\).

Then \(\mu'\) is reflection positive on \(\mathcal A_+'\), i.e.
\[
\mu'\big((\theta' G)G\big)\ \ge\ 0\qquad \forall\,G\in\mathcal A_+',
\]
where \(\theta'\) is induced by \(\Theta'\) via \((\theta'G)(\omega')=\overline{G(\Theta'\omega')}\).

#### Proof

Fix any \(G\in\mathcal A_+'\) and define its pullback \(F:=G\circ P\).
By positive‑time compatibility, \(F\in\mathcal A_+\).

Compute the reflected pullback:
for \(\omega\in\Omega\),
\[
(\theta F)(\omega)
= \overline{F(\Theta\omega)}
= \overline{G(P(\Theta\omega))}
\overset{P\circ\Theta=\Theta'\circ P}{=}
\overline{G(\Theta'(P\omega))}
= (\theta'G)(P\omega).
\]
Hence
\[
(\theta F)= (\theta'G)\circ P.
\]

Now use the pushforward identity:
\[
\mu'\big((\theta'G)G\big)
= \int_{\Omega'} (\theta'G)(\omega')\,G(\omega')\,d\mu'(\omega')
= \int_{\Omega} (\theta'G)(P\omega)\,G(P\omega)\,d\mu(\omega).
\]
Substitute \((\theta'G)\circ P = \theta F\) and \(G\circ P=F\):
\[
\mu'\big((\theta'G)G\big)=\int_{\Omega} (\theta F)(\omega)\,F(\omega)\,d\mu(\omega)
= \mu\big((\theta F)F\big)\ \ge\ 0,
\]
where the last inequality is reflection positivity of \(\mu\) on \(\mathcal A_+\).
\(\square\)

---

## 5. What this buys you (firewall interpretation)

- Reflection positivity is an inequality statement: \(\mu((\theta F)F)\ge 0\).
- Coarse‑graining is a model morphism: \(P\).
- The theorem proves **certificate transport**: reflection positivity at fine scale implies reflection positivity at coarse scale.

This is the prototypical “physics firewall” behavior: you can transform the model
without losing a structural admissibility guarantee, provided the morphism respects the
minimal symmetries that the guarantee depends on.

---

## 6. Typical coarse‑grainings that fit the hypotheses

- **Block maps** on lattice configurations that average or project blocks entirely within the positive‑time half.
- **Decimation** (subsampling) that commutes with reflection.
- **Local feature extraction** maps that ignore negative‑time degrees of freedom when computing positive‑time observables.

The theorem is deterministic; stochastic coarse‑grainings require a Markov‑kernel variant,
but the essential algebra is the same: equivariance + positivity‑time compatibility.
