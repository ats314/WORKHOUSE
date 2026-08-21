# q-Racah Doob Markov Chains as a Tunable Mass-Gap Toy Model

## Abstract

The corpus introduces a discrete toy model that mimics “mass gap vs criticality” in a controlled setting:

1. start with a symmetric tridiagonal (Jacobi) Hamiltonian \(H\) of q-Racah type,
2. apply a **Doob ground-state transform** using its positive ground state \(\psi_0\),
3. obtain a continuous-time Markov generator \(Q\),
4. define the toy “mass gap” as the spectral gap \(m = -\lambda_1(Q)\).

Simulations reported in the corpus suggest:
\[
m(q)\approx C(1-q)^\nu,\qquad \nu\approx 0.967\ (\text{consistent with }\nu=1),
\]
so that the model is gapped for \(q<1\) and becomes critical at \(q=1\).

---

## 1. Doob transform (general construction)

Let \(H\in\mathbb{R}^{n\times n}\) be a symmetric matrix with off-diagonal entries \(H_{ij}\le 0\) for \(i\ne j\) (stoquastic form).
Let \(\psi_0>0\) be the Perron–Frobenius ground state, \(H\psi_0=E_0\psi_0\).

Define a Markov generator \(Q\) by
\[
Q_{ij} := -H_{ij}\frac{\psi_0(j)}{\psi_0(i)},\quad i\ne j,
\qquad
Q_{ii} := -\sum_{j\ne i}Q_{ij}.
\tag{1.1}
\]
Then:

- \(Q_{ij}\ge 0\) for \(i\ne j\),
- \(\sum_j Q_{ij}=0\) (conservative generator),
- \(Q\) is reversible with stationary distribution \(\pi(i)\propto \psi_0(i)^2\).

Define the gap:
\[
m := -\lambda_1(Q),
\]
where \(0=\lambda_0(Q)>\lambda_1(Q)\ge\cdots\).

---

## 2. q-Racah input (as recorded in the corpus)

The corpus specifies \(H\) as a q-Racah Jacobi operator \(H(N,q;\alpha,\beta,\gamma,\delta)\) (tridiagonal).
The exact coefficient formulas are not reproduced in the available code fragments; the conceptual point is that q-Racah provides an analytically structured family with a parameter \(q\in(0,1]\) controlling criticality.

---

## 3. Reported critical scaling

Near \(q\to 1\), the corpus reports a fitted scaling law
\[
m(q)\approx C(1-q)^\nu,\qquad \nu\approx 0.967.
\]
Interpreting \(\nu=1\) suggests a linearly closing gap at a critical boundary.

---

## 4. Why this is potentially useful (as a theory-development tool)

This toy model is useful because:

- it creates a **tunable gapped-to-critical family** with a known Markov interpretation,
- it is compatible with **transfer-operator / tensor-network** language (the corpus mentions a “boundary transfer operator” built from q-data),
- it offers a clean environment where “gap persistence under coarse-graining” can be tested and proven.

Within the larger program, it is a sandbox for refining the logical interface:
\[
\text{functional inequalities}\ \Rightarrow\ \text{spectral gap}\ \Rightarrow\ \text{mass scale}.
\]

---

## 5. Minimal reproducible code: Doob transform + gap extraction

The following code implements the Doob transform and computes the gap for a supplied symmetric tridiagonal \(H\).

```python
import numpy as np

def doob_generator_from_H(H, psi0, tol=1e-14):
    H = np.asarray(H, dtype=float)
    psi0 = np.asarray(psi0, dtype=float)
    n = H.shape[0]
    assert H.shape == (n,n)
    assert psi0.shape == (n,)
    assert np.all(psi0 > 0)

    Q = np.zeros_like(H)
    for i in range(n):
        for j in range(n):
            if i == j: 
                continue
            if abs(H[i,j]) > tol:
                Q[i,j] = -H[i,j] * (psi0[j] / psi0[i])
    Q[np.diag_indices(n)] = -np.sum(Q, axis=1)
    return Q

def spectral_gap(Q):
    # eigenvalues of Q (real); largest is 0
    w = np.linalg.eigvals(Q)
    w = np.real_if_close(w, tol=1e-8)
    w = np.sort(np.real(w))[::-1]  # descending
    # w[0] should be 0
    return -(w[1])  # gap

def ground_state_pf(H):
    # For symmetric stoquastic H: smallest eigenvector can be chosen positive.
    w, v = np.linalg.eigh(H)
    idx = np.argmin(w)
    psi = v[:, idx]
    psi = np.abs(psi)
    psi = psi / np.linalg.norm(psi)
    return w[idx], psi

# Example: build a simple tridiagonal H with tunable parameter q (placeholder)
def example_tridiagonal(n=50, q=0.9):
    # NOT q-Racah; placeholder to test the pipeline
    # off-diagonal scale shrinks as q->1 to mimic closing gap
    a = (1.0-q)
    diag = np.zeros(n)
    off  = -a*np.ones(n-1)
    H = np.diag(diag) + np.diag(off,1) + np.diag(off,-1)
    return H

for q in [0.5, 0.7, 0.9, 0.95]:
    H = example_tridiagonal(n=80, q=q)
    E0, psi0 = ground_state_pf(H)
    Q = doob_generator_from_H(H - E0*np.eye(H.shape[0]), psi0)  # shift so ground energy 0
    gap = spectral_gap(Q)
    print(q, gap)
```

To reproduce the corpus q-Racah claims, replace `example_tridiagonal` by the q-Racah Jacobi coefficients and reuse the same pipeline.

---

## 6. What appears new (within the corpus)

### Pipeline Architecture
q-Racah \(\Rightarrow\) Doob transform \(\Rightarrow\) reversible Markov generator \(\Rightarrow\) tunable spectral gap \(\Rightarrow\) critical exponent.

No clear prior equivalent is identified within the corpus; the construction is plausibly novel as a “mass-gap toy model” tailored to the larger program.