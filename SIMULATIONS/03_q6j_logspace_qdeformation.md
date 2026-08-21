---
title: "Stable evaluation of (q-deformed) Wigner 6j symbols via log-factorials and phase tracking"
date: "2025-12-28"
source_files:
  - "2025-11-25_LogFactorialRacahSymbols_JAX-RacahSymbols-LogFactorial.pdf"
  - "2025-11-25_LogSpace6jSymbolComputation_Physics-ComputationalPhysics-JAX.pdf"
  - "2025-11-25_BatchJ4Working_JAX-Physics-ComputationalPhysics.pdf"
  - "2025-11-25_Phase2IntegrationQuantumVertex_quantum-jax-physics.pdf"
  - "2025-11-26_Quantum6jSymbolCalculation_QuantumPhysics-6j-symbol-SU2.pdf"
  - "2025-11-26_FourierAnalysisSU2GaugeTheory_GaugeTheory-JAX-QuantumPhysics.pdf"
---

# 1. Why this note exists

Tensor-network constructions for gauge theories (and quantum-group/spin-foam style models) quickly turn into a festival of $6j$ symbols.
The Racah formula is exact but numerically fragile: factorials explode, alternating sums cancel, and half-integer spins require care.

The project develops a practical trick with real theoretical content:

- Compute **factorials in log-space** via $\log\Gamma(x+1)$.
- For $q$-deformation with $q=e^{i\theta}$, compute **log-magnitudes and phases separately** for $q$-factorials.

This note extracts the underlying mathematics and shows how the numerical stability aligns with representation theory.

# 2. Classical SU(2) 6j symbol: Racah formula

Let $j_1,\dots,j_6\in \frac12\mathbb Z_{\ge0}$ satisfy the triangle constraints on each of the four triples
$(j_1,j_2,j_3)$, $(j_1,j_5,j_6)$, $(j_4,j_2,j_6)$, $(j_4,j_5,j_3)$ and the usual parity conditions.

Define the triangle coefficient

$$
\Delta(a,b,c)
=
\sqrt{
\frac{(a+b-c)!\,(a-b+c)!\,(-a+b+c)!}{(a+b+c+1)!}
}.
$$

Then Racah's formula is

$$
\begin{Bmatrix}
j_1 & j_2 & j_3\\
j_4 & j_5 & j_6
\end{Bmatrix}
=
\Delta(j_1,j_2,j_3)\Delta(j_1,j_5,j_6)\Delta(j_4,j_2,j_6)\Delta(j_4,j_5,j_3)
\sum_{z=z_{\min}}^{z_{\max}}
(-1)^z\,
\frac{(z+1)!}{\prod_{i=1}^4 (z-\alpha_i)!\;\prod_{k=1}^3(\beta_k-z)!},
$$

where

$$
\alpha_1=j_1+j_2+j_3,\;
\alpha_2=j_1+j_5+j_6,\;
\alpha_3=j_4+j_2+j_6,\;
\alpha_4=j_4+j_5+j_3,
$$

and

$$
\beta_1=j_1+j_2+j_4+j_5,\;
\beta_2=j_2+j_3+j_5+j_6,\;
\beta_3=j_3+j_1+j_6+j_4,
$$

with $z_{\min}=\max_i\alpha_i$, $z_{\max}=\min_k\beta_k$.
All factorial arguments are nonnegative integers in the valid range.

# 3. Log-factorial stabilization (half-integers included)

Instead of factorials, use

$$
\log(n!) = \log\Gamma(n+1),
$$

which naturally handles half-integers.

For spins in $\{0,\tfrac12,1,\tfrac32,\dots,J_{\max}\}$, all factorial arguments in Racah's formula lie in a bounded range.
So we precompute a cache on the grid $x\in\{0,\tfrac12,1,\tfrac32,\dots,X_{\max}\}$:

$$
\mathrm{LOG\_FACT}[x] := \log\Gamma(x+1).
$$

Then

$$
\log\Delta(a,b,c)
=
\frac12\Bigl[
\log(a+b-c)!+\log(a-b+c)!+\log(-a+b+c)!-\log(a+b+c+1)!
\Bigr],
$$

and each summand magnitude is computed as

$$
\log|\mathrm{term}(z)|
=
\log(z+1)! - \sum_{i=1}^4\log(z-\alpha_i)! - \sum_{k=1}^3\log(\beta_k-z)!.
$$

You still need the alternating sign $(-1)^z$, so the sum is performed in **linear space** after exponentiating the log-magnitudes,
with masking of invalid $z$ outside $[z_{\min},z_{\max}]$.

This reduces overflow/underflow and makes vectorization/JIT compilation practical.

# 4. q-deformation with q = exp(iθ): magnitudes + phases

For unitary $q=e^{i\theta}$, define the $q$-number

$$
[n]_q := \frac{q^n-q^{-n}}{q-q^{-1}}
= \frac{\sin(n\theta)}{\sin\theta}.
$$

Limits and singular points matter:

- As $\theta\to 0$, $[n]_q\to n$ (recover classical SU(2)).
- At $\theta\approx k\pi$, denominators can vanish; implementations must special-case $\theta\approx 0$ and avoid catastrophic cancellation near roots of unity.

Define $q$-factorial

$$
[n]_q! := \prod_{k=1}^n [k]_q,
$$

and $q$-triangle coefficient

$$
\Delta_q(a,b,c)
=
\sqrt{
\frac{[a+b-c]_q!\,[a-b+c]_q!\,[-a+b+c]_q!}{[a+b+c+1]_q!}
}.
$$

The $q$-deformed Racah formula mirrors the classical one with every factorial replaced by a $q$-factorial:

$$
\begin{Bmatrix}
j_1 & j_2 & j_3\\
j_4 & j_5 & j_6
\end{Bmatrix}_q
=
\prod_{\text{4 triangles}}\Delta_q(\cdot)
\sum_{z}
(-1)^z
\frac{[z+1]_q!}{\prod_{i=1}^4 [z-\alpha_i]_q!\;\prod_{k=1}^3[\beta_k-z]_q!}.
$$

Because $[n]_q$ can be negative or complex (depending on conventions), the project computes

$$
\log([n]_q!) = \log|[n]_q!| + i\,\arg([n]_q!),
$$

i.e. separately tracks:

- total log-magnitude: $\sum_k \log|[k]_q|$,
- total phase: $\sum_k \arg([k]_q)$.

This is the natural complex generalization of log-space stabilization.

# 5. Implementation-level observations that matter mathematically

1. **Masking encodes selection rules.** Triangle inequalities and parity conditions are handled as boolean masks; invalid configurations return $0$.
   This matches the exact representation-theory selection rules.

2. **Cancellation is physical, not numerical noise.** Alternating sums encode interference between recoupling channels; doing the sum in linear space
   preserves that.

3. **Roots of unity are special regimes.** When $q$ is a root of unity, representation categories truncate; numerically, $\sin\theta$ small makes $[n]_q$
   large and ill-conditioned unless treated carefully. The code's special-casing is the numerical shadow of that categorical transition.

# 6. Next steps

- Replace small-$\theta$ hacks with full $q$-Racah evaluation in complex log-space (including robust handling at/near roots of unity).
- Validate symmetry identities of $6j$ and $q$-$6j$ symbols numerically (tetrahedral symmetries, orthogonality relations) as regression tests.
- Build automatic differentiation-friendly versions (JAX) to allow gradient-based fitting/learning of effective tensor-network parameters.

