# Quantum $6j$ symbols at $q=e^{i\theta}$: definitions and a log-space $q$-Racah algorithm

**Source notebooks:** `Phase2_Integration.ipynb`, `SU2_4D_Rank8_FINAL.ipynb`, `SU2_4D_PHASE2_FIXED.ipynb`

## 1. Background: why $q$-deformed recoupling enters

The project’s tensor construction uses $U_q(\mathfrak{su}(2))$ recoupling data to supply local amplitudes that depend on a deformation parameter
\[
q = e^{i\theta}.
\]

At $q\to 1$ (i.e. $\theta\to 0$), one recovers classical $SU(2)$ representation theory and classical Wigner $6j$ symbols. For generic $q$ on the unit circle, the relevant quantities remain well-defined but become numerically delicate because $q$-factorials can span huge dynamic ranges and acquire phases.

This note records the specific formulas and a numerically stable strategy for computing $q$-deformed $6j$ symbols for half-integer spins.

---

## 2. $q$-numbers and quantum dimensions

Define the $q$-number
\[
[n]_q = \frac{q^n - q^{-n}}{q-q^{-1}}.
\]

For $q=e^{i\theta}$ this simplifies to
\[
[n]_q = \frac{\sin(n\theta)}{\sin\theta},
\]
which is real for real $\theta$ (away from $\theta\in \pi\mathbb{Z}$, where limits are taken).

For spin-$j$ representations of $SU(2)$, the quantum dimension is
\[
d_j^{(q)} = [2j+1]_q.
\]

---

## 3. $q$-factorials in log space (including half-integers)

Formally,
\[
[n]_q! = \prod_{m=1}^{n} [m]_q,\qquad n\in\mathbb{Z}_{\ge 0}.
\]

In $SU(2)$ recoupling problems, one frequently encounters half-integers. The implementation in the project treats $n$ as a half-integer and performs the product in increments of $\tfrac12$:

- represent $n$ as $n=\tfrac{k}{2}$ for integer $k\ge 0$,
- multiply $[m]_q$ over $m=\tfrac12,\ 1,\ \tfrac32,\dots,\tfrac{k}{2}$.

To avoid overflow/underflow and preserve phase information, compute
\[
\log([n]_q!) = \sum_{m} \log|[m]_q| + i \sum_m \arg([m]_q).
\]

### Classical limit handling

As $\theta\to 0$, $[m]_q \to m$, and one should switch to
\[
\log(n!)=\log\Gamma(n+1)
\]
(using e.g. `lgamma`), which is stable and fast.

---

## 4. The $q$-triangle coefficient $\Delta_q$

The (quantum) triangle coefficient is
\[
\Delta_q(a,b,c)
=
\sqrt{
\frac{
[a+b-c]_q!\,[a-b+c]_q!\,[-a+b+c]_q!
}{
[a+b+c+1]_q!
}
}.
\]

In log space,
\[
\log \Delta_q(a,b,c)
= \tfrac12\Bigl(
\log([a+b-c]_q!)
+\log([a-b+c]_q!)
+\log([-a+b+c]_q!)
-\log([a+b+c+1]_q!)
\Bigr).
\]

If any factorial has a negative argument (interpreted as invalid), $\Delta_q=0$.

---

## 5. $q$-Racah formula for the $q$-deformed $6j$ symbol

The $q$-deformed $6j$ symbol is written as
\[
\begin{Bmatrix}
j_1 & j_2 & j_3\\
j_4 & j_5 & j_6
\end{Bmatrix}_q
=
\Delta_q(j_1,j_2,j_3)\Delta_q(j_1,j_5,j_6)\Delta_q(j_4,j_2,j_6)\Delta_q(j_4,j_5,j_3)
\sum_{t=t_{\min}}^{t_{\max}} (-1)^t\, \mathcal{R}_q(t),
\]
where the Racah summand is
\[
\mathcal{R}_q(t)
=
\frac{[t+1]_q!}{
[t-j_1-j_2-j_3]_q!\,
[t-j_1-j_5-j_6]_q!\,
[t-j_4-j_2-j_6]_q!\,
[t-j_4-j_5-j_3]_q!\,
[j_1+j_2+j_4+j_5-t]_q!\,
[j_1+j_3+j_4+j_6-t]_q!\,
[j_2+j_3+j_5+j_6-t]_q!
}.
\]

The summation limits are
\[
t_{\min}=\max(
j_1+j_2+j_3,\ j_1+j_5+j_6,\ j_4+j_2+j_6,\ j_4+j_5+j_3),
\]
\[
t_{\max}=\min(
j_1+j_2+j_4+j_5,\ j_1+j_3+j_4+j_6,\ j_2+j_3+j_5+j_6).
\]

### Selection rules

The implementation enforces:

1. Triangle inequalities for the four triples $(j_1,j_2,j_3)$, $(j_1,j_5,j_6)$, $(j_4,j_2,j_6)$, $(j_4,j_5,j_3)$.

2. “Parity” constraint: each triangle sum $a+b+c$ must be integer (so that coupling is allowed).

If violated, the $6j$ is zero.

---

## 6. Numerically stable evaluation strategy

A direct evaluation of factorial products is unstable; the notebooks use:

1. **Log-factorials** to compute $\log\Delta_q$ and the Racah summand magnitude/phase.

2. **Explicit complex summation** in linear space:
   \[
   \sum_t (-1)^t \exp\bigl(\log |\mathcal{R}_q(t)| + i\,\arg(\mathcal{R}_q(t))\bigr),
   \]
   rather than a “log-sum-exp” (which is tricky for oscillatory sums).

3. **Caching** (`lru_cache`) for repeated calls, which is essential because tensor construction calls $6j$ many times with repeated spin tuples.

---

## 7. Edge cases: $q=\pm 1$ and roots of unity

- **$\theta=0$:** $q=1$, use classical formulas (or Wigner $6j$ from a trusted library) and avoid divisions by $q-q^{-1}$.

- **$\theta=\pi$:** $q=-1$, $q-q^{-1}=0$ and $[n]_q$ can vanish for even/odd patterns. One must define the limit carefully; numerically, special handling is required to avoid spurious blow-ups.

These special points are not just numerical quirks: in quantum-group theory they are often physically/mathematically distinguished.

---

## 8. What to do next

- Add automated tests for $6j$ symmetry identities (tetrahedral symmetries).
- Validate against known tabulated values at a few $q$ (including roots of unity).
- Investigate whether the chosen half-integer product convention matches the intended $U_q(\mathfrak{su}(2))$ normalization (there are multiple conventions in the literature).

