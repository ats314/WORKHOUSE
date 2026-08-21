# q-Racah Doob Transform Gap Lab (Toy “Mass-Gap Machine”)

This document is based on:
- `01_q_racah_doob_massgap.txt`
- `02_q_flow_and_safe_region.txt`

This is not Yang–Mills. It is a deliberately controlled *finite-dimensional laboratory* where:
- a structured Hamiltonian $H$ is built from $q$-Racah-type coefficients,
- a ground-state Doob transform produces a Markov generator $Q$,
- and the spectral gap of $Q$ is tracked under deformations (especially $q\to 1$).

---

## 1. The Jacobi matrix Hamiltonian

Fix an integer $N\ge 1$. Define an $(N+1)\times(N+1)$ tridiagonal symmetric matrix
\[
H = H(N,q;\alpha,\beta,\gamma,\delta)
\]
via coefficients $A_n,B_n,C_n$ ($n=0,\dots,N$), with $A_n$ on the superdiagonal,
$C_n$ on the subdiagonal, and $H_{nn}=A_n^2+C_n^2$.

A standard $q$-Racah-type parameterization (as used in the code) is:
\[
A_n^2 = \frac{(1 - \alpha q^{n+1})(1 - \beta\delta q^{n+1})(1 - \gamma q^{n+1})(1 - \delta q^{n+1})}
{(1 - \delta q^{2n+1})(1 - \delta q^{2n+2})},
\]
\[
C_n^2 = \frac{(1 - q^n)(1 - \beta q^n)(1 - \gamma q^n)(1 - \alpha\delta q^n)}
{(1 - \delta q^{2n})(1 - \delta q^{2n+1})},
\qquad
B_n = -(A_n^2 + C_n^2).
\]
In the “stable regime” explored most:
\[
\alpha=\beta=\gamma=\delta=1,\qquad q\in(0,1).
\]

---

## 2. Doob transform to a Markov generator

Diagonalize $H$:
\[
H\psi_k = E_k \psi_k,\qquad E_0\le E_1\le \cdots \le E_N.
\]
Let $\psi_0$ be the ground state, forced positive componentwise in code by $|\cdot|$ and checked for strict positivity.

Define the continuous-time Markov generator $Q$ by:
\[
Q_{ij} = -H_{ij}\,\frac{\psi_0(j)}{\psi_0(i)}\quad (i\neq j),
\qquad
Q_{ii} = -\sum_{j\neq i} Q_{ij}.
\]
Then:
- off-diagonal rates $Q_{ij}\ge 0$ (in the regime where $-H_{ij}\ge 0$ and $\psi_0>0$),
- row sums vanish: $\sum_j Q_{ij}=0$.

---

## 3. The “mass gap”: spectral gap of Q

Let eigenvalues of $Q$ be
\[
0=\lambda_0 > \lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_N.
\]
Define the spectral gap:
\[
m_q(N) := -\lambda_1.
\]

### Example (reported in project notes)
For $N=4$, $q\approx 0.95$ and $\alpha=\beta=\gamma=\delta=1$, one recorded:
- a strictly positive and non-uniform ground state $\psi_0$,
- eigenvalues of $Q$ roughly:
\[
\lambda_1\approx -0.0851,\ \lambda_2\approx -0.1476,\ \ldots
\]
hence
\[
m_q\approx 0.0851.
\]

---

## 4. Safe region scans (empirical)

With $\alpha=\beta=\gamma=\delta=1$ and $N$ modest, scanning $q$ gives a smooth, strictly positive gap for $q<1$ and decay toward $0$ as $q\to 1$.

A typical table (from the project notes, $N=5$) is:

| q | m_q(N=5) |
|---|----------|
| 0.85 | 0.1991 |
| 0.87 | 0.1801 |
| 0.89 | 0.1590 |
| 0.91 | 0.1361 |
| 0.93 | 0.1114 |
| 0.95 | 0.0851 |
| 0.97 | 0.0575 |
| 0.99 | 0.0295 |

An important empirical finding: **“q-flows” are stable**, while some parameter flows (like $\alpha$-flows at fixed $q$) can break positivity of $\psi_0$ and invalidate the Doob transform.

---

## 5. Why this is exciting

This is a crisp testbed for the slogan:

> *“Ground-state transforms turn Hamiltonians into Markov dynamics, and gaps become dynamically trackable.”*

As a research tool it’s great because:
- everything is finite-dimensional,
- spectral gaps are computable exactly to machine precision,
- one can explore deformations and scaling systematically.

---

## 6. Next upgrades

To turn this into a real theorem (not just numerics), you’d aim for:
1. analytic bounds ensuring $\psi_0>0$ and uniform positivity away from 0 on a parameter region,
2. explicit lower bounds on $m_q(N)$ for finite $N$ and/or scaling limits,
3. a proven monotonicity or continuity statement in $q$.

Because the object is a Jacobi matrix, there’s a lot of classical machinery available (orthogonal polynomial theory, Sturm oscillation, etc.) that can be pulled in.

