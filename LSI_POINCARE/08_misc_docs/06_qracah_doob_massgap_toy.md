# \(q\)-Racah Jacobi Hamiltonian → Doob Transform → “Mass Gap” Toy Model

## What this is

This document extracts a **fully explicit toy pillar**:

1. Build a symmetric tridiagonal \(q\)-Racah-type Hamiltonian \(H\) (finite-dimensional).
2. Compute its ground state \(\psi_0\).
3. Perform the **Doob transform** to obtain a Markov generator \(Q\).
4. Define the **mass gap** as the spectral gap of \(Q\).

This is attractive because it makes “gap survives deformation” questions computationally sharp — and it is small enough to be a sandbox for proof attempts.

---

## 1. Doob transform in this setting

Given a symmetric matrix \(H\) with ground state \(\psi_0>0\) (componentwise) and ground eigenvalue \(E_0\), define
\[
\widetilde H = H - E_0 I,
\]
so that \(\widetilde H \psi_0 = 0\).

The Doob-transformed generator \(Q\) is defined for \(i\neq j\) by
\[
Q_{ij} = -\widetilde H_{ij}\,\frac{\psi_0(j)}{\psi_0(i)},
\]
and \(Q_{ii} = -\sum_{j\neq i} Q_{ij}\), ensuring row sums are zero.

Then \(Q\) is a valid continuous-time Markov generator (off-diagonal rates \(\ge 0\) if \(\widetilde H\) has the right sign pattern) with stationary distribution \(\pi(i)\propto \psi_0(i)^2\).

The “mass gap” is taken as
\[
m_q := \text{gap}(Q) = -\lambda_1(Q),
\]
where \(\lambda_1(Q)\) is the largest nonzero eigenvalue (closest to 0; negative).

---

## 2. Reference implementation excerpt (NumPy)

```python
def doob_transform(H, tol=1e-12):
    evals, evecs = np.linalg.eigh(H)
    idx0 = np.argmin(evals)
    E0 = evals[idx0]
    psi0 = evecs[:, idx0]
    # enforce positivity convention
    if psi0[psi0!=0].mean() < 0:
        psi0 = -psi0
    if np.min(psi0) <= tol:
        return None, evals, psi0, False

    Ht = H - E0*np.eye(H.shape[0])
    Q = np.zeros_like(H)
    for i in range(H.shape[0]):
        for j in range(H.shape[0]):
            if i!=j:
                Q[i,j] = -Ht[i,j]*psi0[j]/psi0[i]
        Q[i,i] = -Q[i,:].sum()
    return Q, evals, psi0, True

def spectral_gap(Q):
    evals = np.linalg.eigvals(Q).real
    evals.sort()
    # evals includes 0 at the end
    gap = -evals[-2]
    return gap, evals
```

---

## 3. Concrete numerical example (reported)

Parameters:

- \(N=4\) (matrix size \(N+1=5\))
- \(q=0.95\)
- \(\alpha=q,\;\beta=1,\;\gamma=q,\;\delta=1\)

The Hamiltonian \(H\) printed as:

\[
H=\begin{pmatrix}
0.004875 & -0.04134038 & 0 & 0 & 0\\
-0.04134038 & 0.00901832 & -0.06788456 & 0 & 0\\
0 & -0.06788456 & 0.01628785 & -0.09358721 & 0\\
0 & 0 & -0.09358721 & 0.0261009 & -0.11894883\\
0 & 0 & 0 & -0.11894883 & 0.01414882
\end{pmatrix}.
\]

Eigenvalues of \(H\):
\[
[-0.13874961,\,-0.05363197,\,0.00885577,\,0.07575322,\,0.17820348].
\]

Ground state (Doob weight):
\[
\psi_0 \approx [0.03645931,\;0.12666682,\;0.25351936,\;0.32810332,\;0.25525110].
\]

Doob generator \(Q\) (rows sum to ~0):
\[
Q=
\begin{pmatrix}
-0.14362461 & 0.14362461 & 0 & 0 & 0\\
0.01189926 & -0.14776793 & 0.13586867 & 0 & 0\\
0 & 0.03391742 & -0.15503745 & 0.12112004 & 0\\
0 & 0 & 0.07231311 & -0.16485051 & 0.09253740\\
0 & 0 & 0 & 0.15289843 & -0.15289843
\end{pmatrix}.
\]

Eigenvalues of \(Q\) (last is ~0):
\[
[-0.316953086,\,-0.214502830,\,-0.147605380,\,-0.085117632,\;0].
\]

So the extracted “mass gap” is
\[
m_q = 0.085117632\ldots
\]

---

## 4. Flow scans: which deformations preserve the gap?

A scan classified deformation “flows” as either:

- **good_monotone**: gap \(>0\) throughout and monotone in the flow parameter,
- **collapse**: gap becomes invalid or collapses.

Reported summary examples:

- \(q\)-flow: \(q_0=0.7\to q_1=0.95\) (holding other parameters fixed):  
  status = good_monotone, \(\min\) gap \(\approx 0.07627\), \(\max\) gap \(\approx 0.28359\), monotone decreasing.

- \(q\)-flow: \(q_0=0.8\to q_1=0.99\):  
  status = good_monotone, \(\min\) gap \(\approx 0.01590\), \(\max\) gap \(\approx 0.23721\).

- \(\alpha\)-flow at fixed \(q=0.95\):  
  status = collapse (gap no longer behaves well).

So the deformation space has “stable directions” (varying \(q\)) and “unstable directions” (varying \(\alpha\) here), which is exactly the kind of structure one wants in a controlled toy renormalization story.

---

## 5. Finite-size scaling near \(q\to 1\)

A scan over sizes \(N\in\{4,6,8,10,12\}\) and \(q\) values near 1 extracted
\[
m(q) = \min_N m_q(N),
\]
and fit
\[
m(q)\;\sim\;(1-q)^\nu
\quad\text{for}\quad q\approx 1.
\]

Reported fit:
\[
\nu \approx 0.9668203676,
\]
i.e. extremely close to \(1\), suggesting a roughly linear closing of the gap as \(q\to 1\) in that regime.

---

## 6. Why this toy model is worth keeping

Even if it is not physically identical to 4D YM, it has three valuable features:

1. It is **exactly computable**: no path integrals needed.
2. It packages “mass gap” into a clear spectral quantity.
3. It has a tunable deformation parameter \(q\) and exhibits stable/unstable deformation directions.

This makes it an ideal sandbox for building and testing *general* inequalities of the form:

- gap lower bounds under perturbations,
- monotonicity along certain flows,
- comparison theorems between \(H\) and \(Q\).

---

## Sources used

- `12-2-25 code runs 3.pdf` (q-Racah matrix construction; Doob transform; eigenvalue outputs; flow summary; scaling exponent \(\nu\)).
- `CHAT YANG SIMULATION 4x4.txt` (framing: Doob transform as a “mass-gap toy pillar”).
