\
---
title: "Dichotomy reduction and OS reconstruction: from lattice spectral data to continuum mass"
date: 2025-12-29
format: markdown+latex
---

## Abstract

Two conceptual “bridges” organize the project:

1. a **dichotomy reduction**: the 4D Yang–Mills mass gap is logically equivalent (under standard constructive hypotheses) to a **uniform lattice spectral-gap** statement;
2. the **Osterwalder–Schrader (OS) reconstruction**: reflection positivity + Euclidean decay yields a physical Hilbert space and Hamiltonian with a mass gap.

This note states these ideas cleanly and flags what is standard vs what is program-specific.

---

## 1. Dichotomy theorem (conceptual reduction)

Let $\{\mu_a\}$ be a family of lattice Yang–Mills measures with spacing $a\to 0$, and suppose:

- the continuum limit measure $\mu$ exists (tightness + uniqueness),
- reflection positivity survives the limit,
- local observables are well-defined in the limit.

Let $\lambda_{\mathrm{lat}}(a)$ be the spectral gap of the lattice Markov generator (or transfer matrix) in lattice units.

### Theorem 1.1 (Yang–Mills dichotomy template)

Exactly one of the following holds:

1. (**Mass gap**) There exists $c>0$ such that
   \[
   \liminf_{a\to 0} \frac{\lambda_{\mathrm{lat}}(a)}{a} \ge c >0,
   \]
   and the reconstructed continuum Hamiltonian has a strictly positive mass gap $\Delta\ge c$.

2. (**Gapless**) The above limit inferior is zero, and the continuum theory is gapless (e.g. conformal or otherwise massless).

*Discussion.* The point is not that the lattice gap is easy — it isn’t. The point is that, once all other failure modes are eliminated (existence, RP, locality, etc.), the Millennium problem reduces to **uniformity** of a single spectral quantity.

---

## 2. OS reconstruction (standard bridge)

Assume the limiting Euclidean measure $\mu$ satisfies the OS axioms (in particular reflection positivity). Then there exists:

- a Hilbert space $\mathcal{H}$,
- a cyclic vacuum vector $\Omega$,
- a self-adjoint Hamiltonian $H\ge 0$,
- and a representation of the time-translation semigroup.

### Lemma 2.1 (Reflection positivity passes to the limit)

If each $\mu_a$ is reflection positive and $\mu_a\Rightarrow\mu$ weakly, then $\mu$ is reflection positive (for the limiting cylinder algebra).

*Proof sketch.* The RP form is a nonnegative integral for each $a$, and weak convergence passes it to the limit.

---

### Lemma 2.2 (Spectral gap ⇒ Euclidean exponential decay)

If the Markov generator $L$ associated to the continuum Dirichlet form has spectral gap $\rho_0>0$, then for mean-zero local observable $O$,
\[
\langle O, e^{tL} O\rangle_{L^2(\mu)} \le e^{-\rho_0 t}\,\|O\|^2_{L^2(\mu)}.
\]

---

### Lemma 2.3 (Euclidean exponential decay ⇒ Hamiltonian mass gap)

Under OS reconstruction, Euclidean exponential decay at rate $\rho_0$ implies
\[
\inf(\sigma(H)\setminus\{0\})\ge \rho_0.
\]

*Proof sketch.* OS identifies Euclidean correlators with vacuum matrix elements of $e^{-tH}$. Exponential decay forces a spectral gap.

---

## 3. What’s standard, what’s not

**Standard / classical:**
- OS reconstruction itself.
- Reflection positivity of the Wilson lattice action.
- “Spectral gap implies exponential decay” in semigroup/Dirichlet-form language.

**Program-specific / hard:**
- proving a **uniform** gap in the physically normalized units as $a\to 0$;
- ensuring the curvature/spectral-gap bounds are not only local small-field statements, but control the full measure;
- rigorously constructing the continuum limit measure with the needed regularity and locality.

---

## 4. Why this belongs in the “selected” set

Even though OS reconstruction is not new, the **dichotomy reduction** is a powerful organizational tool: it says the “mystery” of the Millennium problem is concentrated in a single uniformity statement. That clarity is rare and useful.

