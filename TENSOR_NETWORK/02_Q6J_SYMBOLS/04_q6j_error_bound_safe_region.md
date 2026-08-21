# q–6j Classical Limit Error: \(O(\theta^2)\) Bounds and a Path to a Computer-Assisted Theorem

## 1. Setup

Write \(q=e^{i\theta}\) with \(|\theta|\ll 1\). Define the q-integer (SU(2)-type)
\[
[n]_q=\frac{q^{n/2}-q^{-n/2}}{q^{1/2}-q^{-1/2}}=\frac{\sin(n\theta/2)}{\sin(\theta/2)}.
\]
The q-factorial and q-triangle coefficient are
\[
[n]_q! = \prod_{k=1}^n [k]_q,\qquad
\Delta_q(a,b,c)=\sqrt{\frac{[-a+b+c]_q!\,[a-b+c]_q!\,[a+b-c]_q!}{[a+b+c+1]_q!}}.
\]

The q–6j symbol is computed via the standard q-Racah/Racah sum:
\[
\begin{Bmatrix} a & b & e \\ c & d & f \end{Bmatrix}_q
= \Delta_q(a,b,e)\Delta_q(c,d,e)\Delta_q(a,c,f)\Delta_q(b,d,f)\;
\sum_z (-1)^z \frac{[z+1]_q!}{\prod_{i=1}^7 [\;\cdot\;]_q! }.
\]

The project focuses on a **compact safe region**
\[
J_{\max}\le 4,\qquad |\theta|\le 0.02,
\]
and seeks a bound of the form
\[
\left|\{6j\}_q - \{6j\}\right|
\;\le\;
C_{\mathrm{rig}}\;\theta^2\;J_{\max}^{5/2},
\quad
C_{\mathrm{rig}}\lesssim 0.3,
\]
with an explicit constant.

## 2. Formal \(O(\theta^2)\) expansion mechanism

Taylor expand:
\[
[n]_q = n\Big(1-\frac{n^2-1}{24}\theta^2+O(\theta^4 n^4)\Big).
\]
Summing logs gives, for \(N\theta\ll 1\),
\[
\log\frac{[N]_q!}{N!}
= \sum_{k=1}^N \log\left(1-\frac{k^2-1}{24}\theta^2+O(\theta^4k^4)\right)
= -\frac{\theta^2}{24}\sum_{k=1}^N(k^2-1)\;+\;O(\theta^4 N^5).
\]
Since \(\sum_{k=1}^N(k^2-1)=O(N^3)\), we get a relative error \(O(\theta^2N^3)\) at the factorial level.  

The nontrivial part is the **Racah sum**: cancellations and the intrinsic scaling of the classical 6j with spin (asymptotically \(\sim J^{-3/2}\) in generic semiclassical regimes) motivates a net scaling closer to \(\theta^2 J^{5/2}\) rather than \(\theta^2 J^3\) in the worst case.

This is why the project aims for \(J_{\max}^{5/2}\): it is consistent with semiclassical scaling and looks numerically correct in the tested window.

## 3. Numerical evidence: empirical constants in the safe region

A global scan over a \((J_{\max},\theta)\) grid reported an empirical constant around
\[
C_{\text{emp}}\approx 0.183,
\]
and explicitly flags \((J_{\max}\le 4,\;|\theta|\le 0.02)\) as belonging to the “safe region” under a tolerance \(\varepsilon=10^{-3}\) (coarse scan).

A separate check in the symmetric family \(j_1=\cdots=j_6=j\) at \(\theta=0.02\) gives
\[
\frac{| \{6j\}_q - \{6j\}|}{\theta^2 j^{5/2}}
\approx 4.8\times 10^{-2}\quad (j=4),
\]
suggesting the true constant for that family is closer to \(0.05\) than \(0.3\).

## 4. JAX reference implementation (used in the scans)

Below is a minimal (non-plotting) JAX-style implementation skeleton.

```python
import jax.numpy as jnp
from jax import jit

def q_int(n, theta):
    return jnp.sin(n*theta/2.0)/jnp.sin(theta/2.0)

def q_fact(N, theta):
    ks = jnp.arange(1, N+1)
    return jnp.prod(q_int(ks, theta))

def delta_q(a,b,c, theta):
    num = q_fact(-a+b+c,theta)*q_fact(a-b+c,theta)*q_fact(a+b-c,theta)
    den = q_fact(a+b+c+1,theta)
    return jnp.sqrt(num/den)

def q6j(a,b,c,d,e,f, theta):
    pref = delta_q(a,b,e,theta)*delta_q(c,d,e,theta)*delta_q(a,c,f,theta)*delta_q(b,d,f,theta)
    # compute z-range and Racah sum with q-factorials
    ...
    return pref*sum_val
```

## 5. How to make it *rigorous*: interval arithmetic plan

The safe region is tiny. For \(J_{\max}\le 4\), there are finitely many admissible spin 6-tuples. This makes a brute-force, computer-assisted theorem feasible:

1. Enumerate all admissible \((a,b,c,d,e,f)\) with \(0\le j\le 4\) and triangle constraints.
2. For each tuple, evaluate both \(\{6j\}_q\) and \(\{6j\}\) **using ball/interval arithmetic**:
   - mpmath interval types (`mpmath.iv`) or
   - Arb via python bindings.
3. For \(\theta\in[-0.02,0.02]\), compute an interval enclosure for
   \[
   R(\theta) = \frac{| \{6j\}_q - \{6j\}|}{\theta^2 J_{\max}^{5/2}}
   \]
   and take the supremum over \(\theta\) and spin tuples.

### Practical trick
Because the dependence on \(\theta\) is smooth and the region is small, you can:
- partition \(\theta\in[-0.02,0.02]\) into subintervals,
- use interval arithmetic on each subinterval, and
- take the max of interval upper bounds.

### Skeleton interval code (mpmath)

```python
import mpmath as mp
iv = mp.iv

def q_int_iv(n, th):
    return iv.sin(n*th/2)/iv.sin(th/2)

def q_fact_iv(N, th):
    out = iv.mpf(1)
    for k in range(1, N+1):
        out *= q_int_iv(k, th)
    return out

# then implement Δ_q and the Racah sum similarly with iv types
# and compute an enclosure for |q6j - sixj| / (th^2 * J**(5/2)).
```

## 6. Why this module is exciting

Most of the YM-side program leans on *functional inequalities* (hard analysis).  
This q–6j module is different: it is tailor-made for a **finite, exhaustive, computer-assisted theorem**. Once done, it upgrades a “formal + numerical” appendix into a genuinely rigorous statement, with a fully explicit constant \(C_{\mathrm{rig}}\).

That’s low-hanging rigor fruit. The universe rarely hands those out.
