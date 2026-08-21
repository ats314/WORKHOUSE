# Quantum \(6j\) symbol via the \(q\)-Racah formula (and how to compute it stably)

This document extracts and organizes the *most reusable mathematical core* of the project: the \(U_q(\mathfrak{su}(2))\) building blocks and a log-space implementation strategy for the \(q\)-deformed Wigner \(6j\) symbol.

**Source files:** `CLEANRUN.pdf` (explicit \(q\)-number / \(q\)-factorial / \(\Delta_q\) / \(6j_q\) implementation), `PHASE 2 IM LOST.pdf`, `GETINNGO GOOD STUFF HERE.pdf`, `LOW SPIN CHECK.pdf` (symmetry/unit-test failures).

---

## 1. Definitions

### 1.1 \(q\)-number

\[
[n]_q=\frac{q^n-q^{-n}}{q-q^{-1}}.
\]
For \(q=e^{i\theta}\),
\[
[n]_q=\frac{\sin(n\theta)}{\sin\theta}.
\]

### 1.2 \(q\)-factorial

For integer \(n\ge 0\),
\[
[n]_q! = \prod_{k=1}^{n} [k]_q,\qquad [0]_q!=1.
\]

**Practical note:** the project treats many intermediate expressions as *integers* even though spins are half-integers; factorial arguments in the Racah formula are designed to land on integers whenever fusion/triangle constraints are satisfied.

### 1.3 Quantum triangle coefficient \(\Delta_q\)

For a triple \((a,b,c)\) satisfying the triangle inequalities and integrality condition \((a+b+c)\in\mathbb{Z}\), define
\[
\Delta_q(a,b,c)=
\sqrt{
\frac{[a+b-c]_q!\,[a-b+c]_q!\,[-a+b+c]_q!}{[a+b+c+1]_q!}
}.
\]

In log-space:
\[
\log \Delta_q(a,b,c)=\frac12\left(
\log[a+b-c]_q!+\log[a-b+c]_q!+\log[-a+b+c]_q!-\log[a+b+c+1]_q!
\right).
\]

---

## 2. The \(q\)-Racah formula for \(\{6j\}_q\)

For spins \(j_1,\dots,j_6\) (half-integers), define the prefactor
\[
\mathcal{P}_q = \Delta_q(j_1,j_2,j_3)\,\Delta_q(j_1,j_5,j_6)\,\Delta_q(j_4,j_2,j_6)\,\Delta_q(j_4,j_5,j_3).
\]

Then the \(q\)-deformed \(6j\) symbol is (one standard convention):
\[
\begin{aligned}
\left\{\begin{matrix}
j_1 & j_2 & j_3\\
j_4 & j_5 & j_6
\end{matrix}\right\}_q
&=
\mathcal{P}_q
\sum_{z=z_{\min}}^{z_{\max}}
(-1)^z\;
\frac{[z+1]_q!}{
[z-j_1-j_2-j_3]_q!\,
[z-j_1-j_5-j_6]_q!\,
[z-j_4-j_2-j_6]_q!\,
[z-j_4-j_5-j_3]_q!
}\\
&\qquad\qquad\times
\frac{1}{
[j_1+j_2+j_4+j_5-z]_q!\,
[j_2+j_3+j_5+j_6-z]_q!\,
[j_1+j_3+j_4+j_6-z]_q!
}.
\end{aligned}
\]

The allowed range is chosen so that all factorial arguments are nonnegative:
\[
\begin{aligned}
z_{\min}&=\max(j_1+j_2+j_3,\; j_1+j_5+j_6,\; j_4+j_2+j_6,\; j_4+j_5+j_3),\\
z_{\max}&=\min(j_1+j_2+j_4+j_5,\; j_2+j_3+j_5+j_6,\; j_1+j_3+j_4+j_6).
\end{aligned}
\]
In practice, \(z\) runs over integers in \([z_{\min},z_{\max}]\).

---

## 3. Log-space evaluation strategy

Direct factorial products overflow instantly. The project’s most important numerical trick is:

- compute \(\log([n]_q!)\) by summing \(\log([k]_q)\),
- compute each Racah term as \(\exp(\log|\text{term}|)\times \text{phase/sign}\),
- sum terms in complex arithmetic (or split magnitude/phase).

### 3.1 Pseudocode outline

1. Precompute/cache \(\log([n]_q!)\) for all needed \(n\) (integers up to some cutoff).
2. For given \((j_1,\dots,j_6)\), compute \(\log \mathcal{P}_q\).
3. For each \(z\in[z_{\min},z_{\max}]\):
   - compute \(\log\) numerator \(\log([z+1]_q!)\),
   - subtract \(\log\) denominators,
   - multiply by \((-1)^z\),
   - accumulate.
4. Multiply by \(\mathcal{P}_q\).

### 3.2 A compact Python reference implementation (extracted & cleaned)

```python
import cmath, functools, numpy as np

@functools.lru_cache(None)
def q_number(n: float, q: complex) -> complex:
    # [n]_q = (q^n - q^{-n}) / (q - q^{-1})
    if np.isclose(q, 1.0):  # classical limit
        return float(n)
    denom = q - 1.0/q
    if abs(denom) < 1e-14:
        return float(n)
    return (q**n - q**(-n)) / denom

@functools.lru_cache(None)
def log_q_factorial(n: float, q: complex) -> complex:
    # log([n]_q!) for integer n>=0
    if n < 0: return -np.inf + 0j
    if n == 0: return 0.0j
    acc = 0.0j
    for k in range(1, int(round(n)) + 1):
        v = q_number(float(k), q)
        if abs(v) < 1e-14:  # hit a root -> treat as zero
            return -np.inf + 0j
        acc += cmath.log(v)
    return acc

@functools.lru_cache(None)
def log_delta_q(a: float, b: float, c: float, q: complex) -> complex:
    # log Δ_q(a,b,c)
    if not (abs(a-b) <= c <= a+b): return -np.inf + 0j
    if (a+b+c) % 1.0 != 0.0: return -np.inf + 0j
    l1 = log_q_factorial(a+b-c, q)
    l2 = log_q_factorial(a-b+c, q)
    l3 = log_q_factorial(-a+b+c, q)
    l4 = log_q_factorial(a+b+c+1, q)
    if any(np.isneginf(x.real) for x in (l1,l2,l3,l4)):
        return -np.inf + 0j
    return 0.5*(l1+l2+l3-l4)

def sixj_q(j1,j2,j3,j4,j5,j6, q: complex) -> complex:
    # prefactor
    lp = (log_delta_q(j1,j2,j3,q) + log_delta_q(j1,j5,j6,q)
        + log_delta_q(j4,j2,j6,q) + log_delta_q(j4,j5,j3,q))
    if np.isneginf(lp.real): return 0.0 + 0j

    zmin = int(np.ceil(max(j1+j2+j3, j1+j5+j6, j4+j2+j6, j4+j5+j3)))
    zmax = int(np.floor(min(j1+j2+j4+j5, j2+j3+j5+j6, j1+j3+j4+j6)))
    if zmin > zmax: return 0.0 + 0j

    s = 0.0 + 0j
    for z in range(zmin, zmax+1):
        # log of Racah summand
        ln = log_q_factorial(z+1, q)
        ld = (log_q_factorial(z-(j1+j2+j3), q) +
              log_q_factorial(z-(j1+j5+j6), q) +
              log_q_factorial(z-(j4+j2+j6), q) +
              log_q_factorial(z-(j4+j5+j3), q) +
              log_q_factorial((j1+j2+j4+j5)-z, q) +
              log_q_factorial((j2+j3+j5+j6)-z, q) +
              log_q_factorial((j1+j3+j4+j6)-z, q))
        if np.isneginf(ln.real) or np.isneginf(ld.real):
            continue
        term = ((-1)**z) * cmath.exp(ln - ld)
        s += term

    return cmath.exp(lp) * s
```

This is essentially what the project uses (with more caching and edge-case handling).

---

## 4. Validation & symmetry tests (critical!)

A Wigner \(6j\) symbol satisfies a big set of symmetries (permutations of columns, swapping top/bottom rows, etc.). In the project’s `LOW SPIN CHECK.pdf`, a symmetry test fails: the same \(6j\) value under a permutation returns a different number (even zero). That’s a neon sign saying:

> **Before trusting any \(\theta\)-physics extracted from \(q\)-\(6j\)’s, the symmetry suite must pass.**

Recommended unit tests:

- compare against `sympy.physics.wigner.wigner_6j` at \(q\to 1\),
- check invariances under the 24 symmetries,
- verify known small-spin values.

---

## 5. Numerical pitfalls for \(q=e^{i\theta}\)

- At \(\theta\approx 0\), \(\sin\theta\) in \([n]_q\) is small → avoid catastrophic cancellation by using the series expansion for \([n]_q\) when \(|\theta|<\theta_{\text{tol}}\).
- At \(\theta\) where \(\sin(k\theta)=0\) for some \(k\) in your factorial product, \([k]_q=0\) and \([n]_q!\) vanishes → the log factorial should go to \(-\infty\). That’s fine physically, but numerically you want predictable behavior.
- If you ever use complex logs, phase tracking matters; splitting magnitude/phase is safer.

---

## 6. Where this plugs into the rest of the project

Once you have a trustworthy \(6j_q\), you can build:
- 4D vertex tensors (rank-8),
- coarse-grain them via HOTRG,
- compute \(F(\theta)\),
- and then extract \(\chi_{\text{top}}\) using robust periodic fitting.

See `03_rank8_vertex_and_hotrg.md` and `04_chi_top_extraction_fourier_and_fits.md`.
