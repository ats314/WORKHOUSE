# q-Racah \(\to\) Doob Generator \(\to\) Finite-State “Mass Gap” (with Transfer-Operator Wrapper)

## 0. Scope

This document isolates a **fully explicit, finite-dimensional** construction from the project:

1. Build a symmetric tridiagonal matrix \(H=H(N,q;\alpha,\beta,\gamma,\delta)\) from q-Racah Jacobi data.
2. Extract the (positive) ground state \(\psi_0\).
3. Doob-transform \(H\) into a continuous-time Markov generator \(Q\).
4. Define a “mass gap” \(m_q(N)\) as the spectral gap of \(Q\).
5. (Optional) wrap \(e^{tQ}\) into a composite boundary transfer operator \(T_q\).

Everything here is finite linear algebra + Markov chains. Any Yang–Mills interpretation is *external*.

---

## 1. q-Racah Jacobi matrix \(H\)

For \(n=0,\dots,N\), define coefficients (as in the project text):

\[
A_n^2=\frac{
(1-\alpha q^{n+1})(1-\beta\delta q^{n+1})(1-\gamma q^{n+1})(1-\delta q^{n+1})
}{
(1-\delta q^{2n+1})(1-\delta q^{2n+2})
},
\quad n=0,\dots,N-1,\quad A_N=0,
\]
\[
C_n^2=\frac{
(1-q^{n})(1-\beta q^{n})(1-\gamma q^{n})(1-\alpha\delta q^{n})
}{
(1-\delta q^{2n})(1-\delta q^{2n+1})
},
\quad n=1,\dots,N,\quad C_0=0,
\]
and
\[
B_n = -(A_n^2+C_n^2).
\]

Then \(H\) is the symmetric tridiagonal matrix
\[
H_{n,n}=-(B_n)=A_n^2+C_n^2,\qquad
H_{n,n+1}=H_{n+1,n}=-A_n,\qquad
H_{n,n-1}=H_{n-1,n}=-C_n.
\]

In practice one clamps tiny negative floating artifacts in \(A_n^2,C_n^2\) to \(0\) before taking square roots.

---

## 2. Doob transform \(\Rightarrow\) Markov generator \(Q\)

Let \((E_0,\psi_0)\) be the ground eigenpair of \(H\) with \(\psi_0>0\) componentwise.
Normalize \(\psi_0\) to a probability vector (\(\sum_i \psi_0(i)=1\)).

Define, for \(i\neq j\),
\[
Q_{ij} = -H_{ij}\frac{\psi_0(j)}{\psi_0(i)},
\]
and set diagonal entries by row-sum zero:
\[
Q_{ii} = -\sum_{j\neq i}Q_{ij}.
\]

Then \(Q\) is a continuous-time Markov generator:
- \(Q_{ij}\ge 0\) for \(i\ne j\),
- \(\sum_j Q_{ij}=0\).

---

## 3. Gap definition

Let the spectrum of \(Q\) be \(0=\lambda_0>\lambda_1\ge\lambda_2\ge\cdots\) (real part ordering; here it is real in the tested regimes).

Define
\[
m_q(N) := -\lambda_1(Q).
\]

---

## 4. Reproducible reference code (NumPy/SciPy)

```python
import numpy as np
import math
import numpy.linalg as la
from scipy.linalg import expm

def q_racah_jacobi_matrix(N,q,alpha=1.0,beta=1.0,gamma=1.0,delta=1.0,eps=1e-15):
    A = np.zeros(N+1)
    C = np.zeros(N+1)

    # A_n, n=0..N-1
    for n in range(0,N):
        num = (1-alpha*q**(n+1))*(1-beta*delta*q**(n+1))*(1-gamma*q**(n+1))*(1-delta*q**(n+1))
        den = (1-delta*q**(2*n+1))*(1-delta*q**(2*n+2))
        if abs(den) <= eps:
            return None
        val = num/den
        if val < 0 and val > -1e-12:
            val = 0.0
        if val < 0:
            return None
        A[n] = math.sqrt(val)
    A[N] = 0.0

    # C_n, n=1..N
    C[0] = 0.0
    for n in range(1,N+1):
        num = (1-q**n)*(1-beta*q**n)*(1-gamma*q**n)*(1-alpha*delta*q**n)
        den = (1-delta*q**(2*n))*(1-delta*q**(2*n+1))
        if abs(den) <= eps:
            return None
        val = num/den
        if val < 0 and val > -1e-12:
            val = 0.0
        if val < 0:
            return None
        C[n] = math.sqrt(val)

    B = -(A**2 + C**2)

    H = np.zeros((N+1,N+1))
    for n in range(N+1):
        H[n,n] = -B[n]
        if n < N:
            H[n,n+1] = H[n+1,n] = -A[n]
        if n > 0:
            H[n,n-1] = H[n-1,n] = -C[n]
    return H

def doob_transform(H, tol=1e-12):
    evals, evecs = la.eigh(H)
    idx = np.argsort(evals)
    evals = evals[idx]
    psi0  = evecs[:, idx[0]]

    # choose a positive gauge (numerically)
    if psi0.sum() < 0:
        psi0 = -psi0
    psi0 = np.abs(psi0)

    if np.min(psi0) < tol:
        return None, evals, psi0, False

    psi0 = psi0/psi0.sum()

    n = H.shape[0]
    Q = np.zeros_like(H)
    for i in range(n):
        for j in range(n):
            if i == j: 
                continue
            if H[i,j] != 0:
                Q[i,j] = -H[i,j]*psi0[j]/psi0[i]
    Q[np.diag_indices(n)] = -np.sum(Q, axis=1)

    rowsum_ok = np.max(np.abs(np.sum(Q,axis=1))) < 1e-6
    offdiag_ok = np.min(Q - np.diag(np.diag(Q))) >= -1e-10
    ok = rowsum_ok and offdiag_ok
    return Q, evals, psi0, ok

def spectral_gap(Q, tol=1e-10):
    eig = la.eigvals(Q)
    eig = np.real_if_close(eig, tol=1000)
    eig = np.sort(np.real(eig))
    neg = eig[eig < -tol]
    return 0.0 if neg.size == 0 else -neg[-1]
```

---

## 5. Safe region and flow classification harness

The project isolates a stable regime
\[
\alpha=\beta=\gamma=\delta=1,\qquad q\in(0,1),
\]
and observes that certain \(\alpha\)-flows “collapse” (invalid Doob transform) at moderate deformation.

A minimal harness:

```python
def classify_flow(builder, ts):
    # builder(t) -> (H or None)
    gaps = []
    oks  = []
    for t in ts:
        H = builder(t)
        if H is None:
            gaps.append(np.nan); oks.append(False); continue
        Q,_,_,ok = doob_transform(H)
        oks.append(bool(ok))
        gaps.append(spectral_gap(Q) if ok else np.nan)

    gaps = np.array(gaps, dtype=float)
    oks  = np.array(oks, dtype=bool)

    if not np.all(oks):
        label = "collapse"
    else:
        dg = np.diff(gaps)
        if np.all(dg <= 1e-12) or np.all(dg >= -1e-12):
            label = "good_monotone"
        else:
            label = "good_nonmonotone"
    return {"label": label, "oks": oks, "gaps": gaps}

def q_path(N, q0, q1):
    return lambda t: q_racah_jacobi_matrix(N, q0 + t*(q1-q0), 1,1,1,1)

def alpha_path(N, q_fixed, a0, a1):
    return lambda t: q_racah_jacobi_matrix(N, q_fixed, a0 + t*(a1-a0), 1,1,1)
```

Empirically (and reproducibly with the code above):
- \(q\)-flows at \(\alpha=\beta=\gamma=\delta=1\) are valid and give strictly positive gaps.
- \(\alpha\)-flows at fixed \(q\) can fail once coefficients force negative \(A_n^2\) or \(C_n^2\).

---

## 6. Finite-size scaling and near-critical exponent \(\nu\)

Define
\[
m(q)=\min_{N\in\{4,6,8,10,12\}} m_q(N).
\]
Fit, near \(q\to 1^-\),
\[
m(q)\approx C(1-q)^\nu.
\]

Using the code above with \(q\in\{0.93,0.94,0.95,0.96,0.97,0.98,0.99\}\),
the values obtained (in this environment) are:

| \(q\) | \(m(q)\) |
|---:|---:|
| 0.93 | 0.104153 |
| 0.94 | 0.090423 |
| 0.95 | 0.076270 |
| 0.96 | 0.061716 |
| 0.97 | 0.046786 |
| 0.98 | 0.031506 |
| 0.99 | 0.015902 |

A log–log fit over this window yields:
\[
\nu \approx 0.9668,
\]
numerically consistent with \(\nu=1\) (linear gap closing).

**Window dependence:** fitting further from \(q=1\) shifts the estimated \(\nu\), as expected for a finite-size toy.

---

## 7. Composite boundary transfer operator \(T_q\)

This is a wrapper that embeds the bulk Markov evolution into a boundary-variable space \(\chi\).

Ingredients:
- bulk evolution \(T_{\mathrm{bulk}}=\exp(t_{\mathrm{bulk}}Q)\),
- boundary kernel \(R\) on a \(\chi\)-grid (e.g. Gaussian + row-normalization),
- diagonal “Wilson-like” weight \(W(\chi)=\exp(\kappa(\chi+\chi^{-1}))\),
- a projection \(\Lambda\) from \(\chi\) to bulk indices \(i\in\{0,\dots,N\}\), e.g.
  \(\Lambda_{ij}\propto \exp(-(i-c\chi_j)^2/(2\sigma_L^2))\) with column normalization.

Composite operator:
\[
T_q := \Lambda^\top\,T_{\mathrm{bulk}}\,\Lambda\,R\,W.
\]
Normalize by its leading eigenvalue magnitude so the spectral radius is 1, and define the effective gap
\[
m_{\mathrm{eff}} := -\log|\lambda_1(\widetilde T_q)|
\]
where \(\lambda_1\) is the second-largest eigenvalue (in magnitude).

Reference implementation:

```python
def gaussian_kernel(x, sigma):
    x = np.asarray(x)
    dx = x[:,None]-x[None,:]
    return np.exp(-0.5*(dx*dx)/(sigma*sigma))

def normalize_rows(M):
    s = M.sum(axis=1, keepdims=True)
    s[s==0] = 1.0
    return M/s

def normalize_cols(M):
    s = M.sum(axis=0, keepdims=True)
    s[s==0] = 1.0
    return M/s

def build_transfer_operator(Q, chi,
                            t_bulk=1.0,
                            sigma_R=0.3,
                            strength=0.0,
                            sigma_L=1.0,
                            c=1.0):
    N = Q.shape[0]-1
    T_bulk = expm(t_bulk*Q)

    R = normalize_rows(gaussian_kernel(chi, sigma_R))
    W = np.diag(np.exp(strength*(chi + 1.0/chi)))

    i = np.arange(N+1)[:,None]
    Lam = np.exp(-0.5*((i - c*chi[None,:])**2)/(sigma_L*sigma_L))
    Lam = normalize_cols(Lam)

    T = Lam.T @ T_bulk @ Lam @ R @ W

    evals = la.eigvals(T)
    lam0  = evals[np.argmax(np.abs(evals))]
    Tn    = T/lam0

    evals2 = la.eigvals(Tn)
    mags = np.sort(np.abs(evals2))[::-1]
    lam1_mag = mags[1] if len(mags) > 1 else 0.0
    m_eff = -np.log(lam1_mag) if lam1_mag > 0 else np.inf
    return m_eff, lam1_mag
```

---

## 8. What looks structurally reusable

- **Pipeline architecture:** orthogonal-polynomial data \(\to\) Markov generator \(\to\) spectral gap \(\to\) transfer-operator language.
- **Safe-region engineering:** the “flow classification” recipe is a general tool for exploring parameter families where a Doob transform stays well-conditioned.
- **Near-critical scaling:** the toy has a measurable critical line at \(q=1\) with approximately linear gap closure.

