# Log-Space Evaluation of the \(q\)-Racah Formula for \(U_q(\mathfrak{su}(2))\) 6j-Symbols

This document extracts the most concrete “derivation-like” content implemented in the notebooks:
a numerically stable evaluation of the **\(q\)-deformed 6j-symbol** (quantum 6j) using:

- explicit \(q\)-Racah summation,
- **log-magnitude + phase** bookkeeping to avoid overflow/underflow,
- support for half-integer spins,
- careful handling of classical limits and root-of-unity pathologies.

---

## 1. Conventions

We parameterize the deformation by
\[
q = e^{i\theta}.
\]

### \(q\)-numbers

For real \(\theta\),
\[
[x]_q
\equiv \frac{q^x-q^{-x}}{q-q^{-1}}
= \frac{\sin(x\theta)}{\sin(\theta)}.
\]
Classical limit:
\[
\lim_{\theta\to 0} [x]_q = x.
\]

---

## 2. \(q\)-factorials and their log-space representation

### \(q\)-factorial (formal)
For nonnegative integer \(n\),
\[
[n]_q! \equiv \prod_{k=1}^{n} [k]_q,\qquad [0]_q! \equiv 1.
\]

In SU(2) recoupling, factorial arguments are usually integers due to selection rules, but the project’s implementation **accepts half-integers** as well and defines a consistent product:
\[
[n]_q! \equiv \prod_{k\in\mathcal{K}(n)} [k]_q,
\]
where \(\mathcal{K}(n)\) steps by \(1\) if \(n\in\mathbb{Z}\) and steps by \(1/2\) if \(n\in\mathbb{Z}+\tfrac12\), starting from \(1\) or \(1/2\) respectively, up to \(n\).

### Log-space representation

Define
\[
\log([n]_q!) \equiv \sum_{k\in\mathcal{K}(n)} \log([k]_q).
\]

Because \([k]_q\) can be negative (or even complex under extensions), we keep:
- **log magnitude:** \(\log|[k]_q|\),
- **phase:** \(\arg([k]_q)\).

Hence store
\[
\log([n]_q!) = \underbrace{\sum \log |[k]_q|}_{\text{log-mag}}
\;+\; i\underbrace{\sum \arg([k]_q)}_{\text{phase}}.
\]

### Special handling: classical limit

When \(\theta\) is numerically tiny, the code switches to
\[
\log([n]_q!) \approx \log(n!) = \log\Gamma(n+1),
\]
to avoid catastrophic cancellation in \(\sin(\theta)\).

### Special handling: zeros (roots of unity)

If any \([k]_q \approx 0\), the factorial is treated as vanishing:
\[
[n]_q! \to 0
\quad\Rightarrow\quad
\log([n]_q!) \to -\infty.
\]
This is essential near \(\theta=\pi\) (or other root-of-unity points), where \(\sin(k\theta)\) can vanish.

---

## 3. The \(q\)-triangle coefficient \(\Delta_q\)

Define the \(q\)-deformed triangle coefficient
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

Selection rules implemented:

- triangle inequalities: \(a+b\ge c\), \(a+c\ge b\), \(b+c\ge a\),
- SU(2) integrality: \(a+b+c\in\mathbb{Z}\).

In log-space:
\[
\log \Delta_q(a,b,c)
=
\frac12\Big(
\log([a+b-c]_q!)
+
\log([a-b+c]_q!)
+
\log([-a+b+c]_q!)
-
\log([a+b+c+1]_q!)
\Big).
\]

---

## 4. The \(q\)-Racah formula for the quantum 6j-symbol

The quantum 6j-symbol is

\[
\left\{\begin{matrix}
j_1 & j_2 & j_3\\
j_4 & j_5 & j_6
\end{matrix}\right\}_q
=
\Delta_q(j_1,j_2,j_3)\,
\Delta_q(j_1,j_5,j_6)\,
\Delta_q(j_4,j_2,j_6)\,
\Delta_q(j_4,j_5,j_3)
\;\sum_{t=t_{\min}}^{t_{\max}} (-1)^t \; \mathcal{R}(t),
\]
where
\[
\mathcal{R}(t)
=
\frac{[t+1]_q!}{
[t-(j_1+j_2+j_3)]_q!\,
[t-(j_1+j_5+j_6)]_q!\,
[t-(j_4+j_2+j_6)]_q!\,
[t-(j_4+j_5+j_3)]_q!\,
[(j_1+j_2+j_4+j_5)-t]_q!\,
[(j_2+j_3+j_5+j_6)-t]_q!\,
[(j_3+j_1+j_6+j_4)-t]_q!
}.
\]

Summation limits:
\[
t_{\min}=\max\big(
j_1+j_2+j_3,\;
j_1+j_5+j_6,\;
j_4+j_2+j_6,\;
j_4+j_5+j_3
\big),
\]
\[
t_{\max}=\min\big(
j_1+j_2+j_4+j_5,\;
j_2+j_3+j_5+j_6,\;
j_3+j_1+j_6+j_4
\big).
\]

### Half-integers and the \((-1)^t\) factor

When \(t\) is half-integer, the sign alternation is implemented as a phase:
\[
(-1)^t = e^{i\pi t}.
\]
This makes sense because the rest of the term may already carry complex phases from \(\log([n]_q!)\).

---

## 5. Numerically stable assembly

### Delta prefactor

Compute
\[
\log \Delta_{\text{pref}} =
\sum_{m=1}^{4} \log \Delta_q(\cdot)_m
=
(\text{log-mag}) + i(\text{phase}).
\]
Then convert once:
\[
\Delta_{\text{pref}}=\exp(\log \Delta_{\text{pref}}).
\]

### Summation terms

Each summand is formed as:

1. compute numerator log:
   \(\log([t+1]_q!)\),
2. compute denominator log as the sum of 7 factorial logs,
3. take the difference to get term log,
4. add the \((-1)^t\) phase \(i\pi t\),
5. exponentiate to get the complex amplitude,
6. sum amplitudes in linear space:
   \[
   S=\sum_t \exp\big(\log \mathcal{R}(t) + i\pi t\big).
   \]

Finally:
\[
\{6j\}_q = \Delta_{\text{pref}} \, S.
\]

This “log for products, linear for sums” split is the key to stability.

---

## 6. Minimal verification suite captured in the project

The integration notebook includes sanity checks:

1. **Classical limit** \(\theta=0\):  
   \(\{6j\}_q \to \{6j\}\) (Wigner 6j).
2. **Selected nontrivial \(\theta\) points**:  
   numerical consistency checks for representative spins.
3. **Root-of-unity warning:**  
   \(\theta=\pi\) is explicitly flagged as potentially singular due to vanishing \(q\)-numbers.

---

## 7. Why this matters for the rest of the project

Every higher-level construction (vertex tensors, HOTRG contraction, \(\theta\)-scan) inherits its correctness from this kernel. If you want the “theory” to mean anything, this is the algebraic engine that makes it compute.
