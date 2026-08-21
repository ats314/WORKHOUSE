---
title: "q-Racah Doob–Transform Toy Model: Spectral Gap, Scaling, and Reproducible Numerics"
author: "Project extraction (compiled)"
date: "2025-12-29"
---

## 0. Why this toy is in the project

The model is a controlled sandbox where you can:

1. build a structured, \(q\)-deformed tridiagonal Hamiltonian \(H\),
2. Doob-transform it into a Markov generator \(Q\) using the positive ground state,
3. measure a **spectral gap** \(m_q(N)\),
4. and study finite-size scaling as \(q\to 1\).

This is not claimed to be literal YM — it’s a testbed for “gap survives until a deformation limit.”

---

## 1. Definition: q-Racah Jacobi matrix Hamiltonian

Fix \(N\in\mathbb{N}\) and parameters \(\alpha,\beta,\gamma,\delta\). Define sequences \(A_n,B_n,C_n\) for \(n=0,\dots,N\) by:

\[
A_n^2
= \frac{(1-\alpha q^{n+1})(1-\beta\delta q^{n+1})(1-\gamma q^{n+1})(1-\delta q^{n+1})}
{(1-\delta q^{2n+1})(1-\delta q^{2n+2})},
\quad n=0,\dots,N-1,
\]

\[
C_n^2
= \frac{(1-q^n)(1-\beta q^n)(1-\gamma q^n)(1-\alpha\delta q^n)}
{(1-\delta q^{2n})(1-\delta q^{2n+1})},
\quad n=1,\dots,N,
\]

\[
B_n = -(A_n^2 + C_n^2).
\]

The symmetric tridiagonal Hamiltonian is:
\[
H_{n,n} = -B_n = A_n^2 + C_n^2,\qquad
H_{n,n+1}=H_{n+1,n}=-A_n,\qquad
H_{n,n-1}=H_{n-1,n}=-C_n,
\]
with boundary \(A_N=C_0=0\).

In the project’s “stable regime,” \(\alpha=\beta=\gamma=\delta=1\) and \(q\in(0,1)\).

---

## 2. Doob transform: from \(H\) to a Markov generator \(Q\)

Diagonalize \(H\) and take the ground state eigenvector \(\psi_0>0\).
Define, for \(i\ne j\),
\[
Q_{ij} = -H_{ij}\,\frac{\psi_0(j)}{\psi_0(i)},
\qquad
Q_{ii} = -\sum_{j\ne i} Q_{ij}.
\]

Then \(Q\) has nonnegative off-diagonals and row sums zero, i.e. it is a valid continuous-time Markov generator.

Define the spectral gap (“mass gap”) as
\[
m_q(N) = -\lambda_1,
\]
where \(0=\lambda_0>\lambda_1\ge\lambda_2\ge\cdots\) are eigenvalues of \(Q\).

---

## 3. Reproducible Python implementation

```python
import numpy as np, math

def q_racah_jacobi_matrix(N, q, alpha=1.0, beta=1.0, gamma=1.0, delta=1.0, clip_tol=1e-14):
    q=float(q); alpha=float(alpha); beta=float(beta); gamma=float(gamma); delta=float(delta)
    A = np.zeros(N+1); C = np.zeros(N+1)

    for n in range(0, N):
        num = (1 - alpha*q**(n+1))*(1 - beta*delta*q**(n+1))*(1 - gamma*q**(n+1))*(1 - delta*q**(n+1))
        den = (1 - delta*q**(2*n+1))*(1 - delta*q**(2*n+2))
        val = num/den
        if val < 0 and val > -clip_tol: val = 0.0
        A[n] = math.sqrt(val) if val>0 else 0.0
    A[N]=0.0

    for n in range(1, N+1):
        num = (1 - q**n)*(1 - beta*q**n)*(1 - gamma*q**n)*(1 - alpha*delta*q**n)
        den = (1 - delta*q**(2*n))*(1 - delta*q**(2*n+1))
        val = num/den
        if val < 0 and val > -clip_tol: val = 0.0
        C[n] = math.sqrt(val) if val>0 else 0.0
    C[0]=0.0

    H = np.zeros((N+1,N+1))
    diag = A**2 + C**2
    np.fill_diagonal(H, diag)
    for n in range(0, N):
        H[n,n+1] = H[n+1,n] = -A[n]
    for n in range(1, N+1):
        H[n,n-1] = H[n-1,n] = -C[n]
    return H

def doob_transform(H, tol=1e-12):
    evals, evecs = np.linalg.eigh(H)
    idx = np.argsort(evals)
    psi0 = np.abs(evecs[:,idx[0]])
    if psi0.min() < tol:
        return None, psi0, False
    psi0 = psi0/psi0.sum()

    n = H.shape[0]
    Q = np.zeros_like(H)
    for i in range(n):
        for j in range(n):
            if i==j: continue
            Q[i,j] = -H[i,j] * psi0[j]/psi0[i]
    Q[np.diag_indices(n)] = -Q.sum(axis=1)

    ok = np.max(np.abs(Q.sum(axis=1))) < 1e-8 and np.all(Q - np.diag(np.diag(Q)) >= -1e-10)
    return Q, psi0, ok

def spectral_gap(Q, tol=1e-10):
    eig = np.linalg.eigvals(Q)
    eig = np.real_if_close(eig)
    eig = np.sort(np.real(eig))
    neg = eig[eig < -tol]
    return (-neg[-1] if neg.size else 0.0), eig
```

---

## 4. Numerical results (this run)

### 4.1 Gap vs \(q\) at fixed \(N=5\)

|q|m_q|
|---|---|
|0.85|0.197572|
|0.87|0.181144|
|0.89|0.161565|
|0.91|0.13878|
|0.93|0.112838|
|0.95|0.0838852|
|0.97|0.0521502|
|0.99|0.0179322|

The gap is strictly positive for \(q<1\) and decreases toward \(0\) as \(q\to 1\).

### 4.2 Finite-size snapshot at \(q=0.99\)

|N|m_q(N,q=0.99)|
|---|---|
|4|0.0159021|
|6|0.0195953|
|8|0.0222467|
|10|0.0243139|
|12|0.0259884|

This matches the project’s logged finite-size table for \(q=0.99\) and \(N\in\{4,6,8,10,12\}\).

### 4.3 Extracting a near-critical exponent

Define
\[
m(q) := \min_{N\in\{4,6,8,10,12\}} m_q(N).
\]

Sampled values:

|q|m(q)|
|---|---|
|0.800000|0.136564|
|0.821111|0.123140|
|0.842222|0.112322|
|0.863333|0.106851|
|0.884444|0.107553|
|0.905556|0.110700|
|0.926667|0.108632|
|0.947778|0.079450|
|0.968889|0.048463|
|0.990000|0.015902|

Fit \(m(q)\approx C(1-q)^\nu\) using only \(q\ge 0.93\) gives
\[
\nu \approx 0.974637,\qquad C\approx 1.417663.
\]

This is numerically consistent with \(\nu=1\) (linear vanishing of the gap at the “critical” boundary \(q=1\)).

---

## 5. How this connects back to the larger program

The structural pattern here is:

\[
H \ \longrightarrow\ \text{(ground state)}\ \psi_0\ \longrightarrow\ \text{Doob}(H,\psi_0)=Q\ \longrightarrow\ \text{gap}(Q).
\]

This is a miniature version of the “Euclidean measure → generator → spectral gap” chain used in the analytic YM program.
In that sense, this toy is a *numerical rehearsal* of the same proof architecture.
