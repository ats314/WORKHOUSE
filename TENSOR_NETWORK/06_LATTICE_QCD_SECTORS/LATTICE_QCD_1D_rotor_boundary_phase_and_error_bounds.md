# 1D Quantum Rotor with a θ-Term: Boundary-Phase Tensor Network and a Gaussian Truncation Bound
*(A cleaned-up derivation/proof package extracted from the rotor archive.)*

## 0. Why this is in the “novel” pile

The mathematically interesting part is not “the rotor spectrum” (that’s standard), but the **structural proof** that:

1. a TN can be built where **every bulk tensor element is real and non-negative**, and
2. the only \(\theta\)-dependence is a **boundary factor** \(e^{ik\theta}\) in a final winding sum, and
3. truncating the winding index admits an explicit **Gaussian tail bound** with the correct scaling \(K_{\max}\sim \sqrt{\beta\ln(1/\varepsilon)}\), independent of the Trotter slice count \(N\).

This is the core “sign-problem deferral” move the project keeps reusing.

---

## 1. Model and topological charge

Consider a particle on a circle (quantum rotor) with angle \(\phi\in[0,2\pi)\) and Euclidean time extent \(\beta\).  
The \(\theta\)-term couples to the winding number \(k\in\mathbb Z\) of the Euclidean path:

\[
Q[\phi] \equiv k
= \frac{1}{2\pi}\int_0^\beta d\tau\, \dot\phi(\tau)\in\mathbb Z
\quad\text{(with periodic boundary conditions).}
\]

So the partition function can be written as

\[
Z(\beta,\theta)=\sum_{k\in\mathbb Z} e^{i k\theta}\, Z_k^{(0)}(\beta),
\qquad
Z_k^{(0)}(\beta)\ge 0.
\]

The entire strategy is to compute \(Z_k^{(0)}\) using only non-negative weights, then apply the phase \(e^{ik\theta}\) at the end.

---

## 2. A strictly non-negative bulk kernel (Villain / covering-space form)

Discretize Euclidean time into \(N\) slices with \(\Delta\tau=\beta/N\).  
The standard “unwrapped” (covering-space) Gaussian step kernel is

\[
K(\phi',\phi)
= \sum_{n\in\mathbb Z}\exp\!\left[-\frac{I}{2\Delta\tau}\,(\phi'-\phi+2\pi n)^2\right],
\]

which is manifestly real and strictly positive.

### Extended configuration space

Introduce an integer label \(k_j\in\mathbb Z\) at each time slice recording which lift of the angle we are on:
\[
\tilde\phi_j = \phi_j + 2\pi k_j\in\mathbb R.
\]

Then one time step connects \((\phi_j,k_j)\) to \((\phi_{j+1},k_{j+1})\) via

\[
T\big((\phi_{j+1},k_{j+1}),(\phi_j,k_j)\big)
=
\exp\!\left[-\frac{I}{2\Delta\tau}\,(\phi_{j+1}-\phi_j+2\pi(k_{j+1}-k_j))^2\right].
\]

Every entry is \(\ge 0\).

---

## 3. Boundary-only θ dependence

Define the total winding over the loop as
\[
k \equiv k_N-k_0.
\]

Then a natural “boundary tensor” inserts the \(\theta\)-term as
\[
B_\theta(k)=e^{ik\theta}.
\]

The resulting TN contraction is:

1. contract the **bulk** network with all local weights non-negative to compute sector weights \(Z_k^{(0)}\),
2. form \(Z(\beta,\theta)=\sum_k B_\theta(k) Z_k^{(0)}\).

### Proposition (strict sign-problem-free bulk)

> **Proposition.**  
> In this representation, all bulk tensor elements are real and non-negative, and the only complex factors are the boundary phases \(e^{ik\theta}\).

**Reason.** The kernel above is a product of Gaussians; the \(\theta\)-term depends only on the integer \(k\), which is global for a closed loop and can be applied as a final sum. ∎

This is precisely why early attempts that encoded \(\theta\) locally in the kernel were abandoned: they reintroduce complex phases inside the network and destroy local positivity.

---

## 4. A Gaussian truncation error bound for the winding cutoff

The rotor archive derives a clean and very useful fact: the winding index behaves like a diffusion variable with variance proportional to \(\beta\) and **independent of \(N\)**.

Let \(k_j\) be the integer lift index after \(j\) steps. Under the Gaussian kernel, \(k_j\) behaves like a random walk whose final variance is

\[
\mathrm{Var}(k_N)=\frac{\beta}{(2\pi)^2}.
\]

Suppose we impose a hard cutoff at all slices:
\[
|k_j|\le K_{\max}\quad\text{for all }j=0,\dots,N.
\]

Then the difference between the truncated TN partition function \(Z_{\mathrm{TN}}\) and the exact \(Z\) is bounded by the probability that the walk exits the band:

\[
|Z_{\mathrm{TN}}-Z(\beta)|
\le Z(\beta)\,\mathbb P\!\left(\max_{0\le j\le N}|k_j|>K_{\max}\right).
\]

Using the reflection principle,

\[
\mathbb P\!\left(\max_{0\le j\le N}|k_j|>K_{\max}\right)
\le 2\,\mathbb P(|k_N|>K_{\max}).
\]

Finally, for a Gaussian \(X\sim\mathcal N(0,\sigma^2)\),

\[
\mathbb P(|X|>a)\le 2\exp\!\left(-\frac{a^2}{2\sigma^2}\right),
\]

so with \(\sigma^2=\beta/(2\pi)^2\),

\[
\mathbb P(|k_N|>K_{\max})
\le 2\exp\!\left(-\frac{2\pi^2 K_{\max}^2}{\beta}\right).
\]

Putting it together gives the explicit bound:

\[
|Z_{\mathrm{TN}}-Z(\beta)|
\le
4 Z(\beta)\exp\!\left(-\frac{2\pi^2 K_{\max}^2}{\beta}\right).
\]

### Corollary (required cutoff for tolerance \(\varepsilon\))

Requiring the RHS \(\le \varepsilon\) yields

\[
K_{\max}(\beta,\varepsilon)\ \sim\ \sqrt{\beta\ln\!\left(\frac{1}{\varepsilon}\right)}.
\]

This is the scaling that makes the whole framework practical: **the cutoff grows only like \(\sqrt{\beta}\)** up to a log.

---

## 5. Why this matters beyond the rotor

This derivation is the prototype for a more general pattern:

- When a \(\theta\)-term couples to an **integer additive charge**, compute the \(\theta=0\) sector weights with a positive TN, then reintroduce phases at the boundary.
- The computational “pain” becomes a question of how fast the tails of the charge distribution decay; for Gaussian tails you get \(K_{\max}\sim\sqrt{\ln(1/\varepsilon)}\) behavior.

This is the conceptual bridge to the proposed 2D U(1) \(Q\)-sector TN and to the attempt (likely obstructed in the same way) to do something similar for SU(2).

---

## Source in the project

This document is primarily a cleaned-up presentation of the truncation-bound derivation and the “boundary-only θ” design recorded in `TN_1D_Rotor_Detail_v2.md`.

