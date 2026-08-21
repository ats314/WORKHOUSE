# Quantum-group deformation as a spectral-gap machine: q-Racah → Doob generator → scaling → transfer operator

This note collects the finite-dimensional construction that turns a symmetric tridiagonal “Hamiltonian” \(H\) into a continuous-time Markov generator \(Q\) by a Doob (ground-state) transform, plus empirical scaling of the gap as \(q\to 1\), and a scaffold for a boundary transfer operator \(T_q\).

---

## Core primitive: a symmetric q-Racah Jacobi matrix

A concrete (project) implementation of a symmetric tridiagonal q-Racah-type matrix \(H\in\mathbb{R}^{(N+1)\times (N+1)}\) is:

```python
import numpy as np

def q_racah_jacobi_matrix(N, q, alpha, beta, gamma, delta):
    """
    Build a (N+1)x(N+1) symmetric tridiagonal 'Hamiltonian' H
    of q-Racah type for given parameters.
    """
    A = np.zeros(N+1)
    B = np.zeros(N+1)
    C = np.zeros(N+1)

    for n in range(0, N+1):
        if n < N:
            numA = ((1 - alpha*q**(n+1)) *
                    (1 - beta*delta*q**(n+1)) *
                    (1 - gamma*q**(n+1)) *
                    (1 - delta*q**(n+1)))
            denA = ((1 - delta*q**(2*n+1)) *
                    (1 - delta*q**(2*n+2)))
            valA = numA/denA
            A[n] = np.sqrt(max(valA, 0.0))

        if n > 0:
            numC = ((1 - q**n) *
                    (1 - beta*q**n) *
                    (1 - gamma*q**n) *
                    (1 - alpha*delta*q**n))
            denC = ((1 - delta*q**(2*n)) *
                    (1 - delta*q**(2*n+1)))
            valC = numC/denC
            C[n] = np.sqrt(max(valC, 0.0))

        B[n] = -(A[n]**2 + C[n]**2)

    H = np.zeros((N+1, N+1))
    for n in range(N+1):
        H[n, n] = -B[n]
        if n < N:
            H[n, n+1] = -A[n]
            H[n+1, n] = -A[n]
        if n > 0:
            H[n, n-1] = -C[n]
            H[n-1, n] = -C[n]

    return H
```

---

## Doob transform (finite-dimensional, exact)

Let \(H\) be symmetric with ground state eigenpair \(H\psi_0=E_0\psi_0\), where \(\psi_0>0\) componentwise. Define the off-diagonal entries of \(Q\) for \(i\ne j\) by
\begin{equation}
Q_{ij} \;:=\; -H_{ij}\,\frac{\psi_0(j)}{\psi_0(i)},
\qquad i\neq j,
\end{equation}
and the diagonal by row-sum normalization \(Q_{ii}=-\sum_{j\neq i}Q_{ij}\). Then \(Q\mathbf{1}=0\).

A reference implementation used in the project is:

---

## Correct continuous-time gap extraction

For a continuous-time generator \(Q\), eigenvalues satisfy \(0=\lambda_0>\lambda_1>\lambda_2>\cdots\). The “mass gap” is \(m_q=-\lambda_1\). The project code explicitly implements this sign convention:

```python
def spectral_gap(Q, tol=1e-12):
    eig = np.linalg.eigvals(Q)
    eig = np.real_if_close(eig, tol=1e-9)
    eig_sorted = np.sort(eig)          # ascending: most negative ... ~0
    neg = eig_sorted[eig_sorted < -tol]
    if neg.size == 0:
        return 0.0, eig_sorted
    lambda1 = neg[-1]                  # closest to 0
    return float(-lambda1), eig_sorted
```

---

## Fully explicit example (matrix, spectrum, gap)

For \(N=4\), \(q=0.95\), and a non-symmetric parameter choice \(\alpha=q,\beta=1,\gamma=q,\delta=1\), the printed Doob generator \(Q\) and its spectrum included:

\begin{align}
\operatorname{spec}(Q) &\approx (-0.316953,\,-0.214503,\,-0.147605,\,-0.085118,\;0),\\
m_q &= 0.0851176323.
\end{align}

---

## Simple 1D scan: \(m_q\) vs \(q\) at fixed \(N\)

A direct scan (with \(N=4\) and parameter pattern \(\alpha=\gamma=0.95,\beta=\delta=1\)) printed:

\begin{align}
q &\quad m_q\\
0.8500 &\quad 0.199122\\
0.8700 &\quad 0.180060\\
0.8900 &\quad 0.159033\\
0.9100 &\quad 0.136111\\
0.9300 &\quad 0.111415\\
0.9500 &\quad 0.085118\\
0.9700 &\quad 0.057508\\
0.9900 &\quad 0.029483.
\end{align}

---

## Finite-size scaling: gap(N,q) over \(N\in\{4,6,8,10,12\}\)

A larger scan varied \(N\) and \(q\) and printed per-\(q\) summaries, including monotonicity flags.

Selected output slices:

---

## Near-critical fit: \(m(q)\sim (1-q)^\nu\)

Defining \(m(q)=\min_N m(q,N)\) and fitting \(\log m = \nu\log(1-q)+c\) for \(q>0.92\) produced:
\begin{equation}
\nu \approx 0.9668203676.
\end{equation}

---

## Flow classification scan: “q-flow” vs “alpha-flow”

A “next steps” routine classified trajectories as “good_monotone” or “collapse”, with a printed summary that included three monotone q-flows and two collapsing alpha-flows.

---

## q-6j numerical error scaling and safe region (data-driven)

A test on symmetric \(6j\) families reported the deviation scaling ratio
\(\max|\delta|/(\theta^2 J_{\max}^{5/2})\) as approximately constant \(\approx 4.7\times 10^{-2}\)–\(5.2\times10^{-2}\) for \(J_{\max}=4\) and \(\theta\in\{0.01,0.02,0.05\}\).

A “safe clamp” example maps \((J_{\max},\theta)=(6.0,0.05)\mapsto(4.0,0.02)\) before downstream tensor steps.

---

## Prototype boundary transfer operator \(T_q\) (scaffold)

A composite operator was assembled in the schematic form
\begin{equation}
T_q \;=\; \Lambda^\top\,T_{\mathrm{bulk}}\,\Lambda\,R\,W,
\qquad
T_{\mathrm{bulk}}=\exp(Q),
\end{equation}
using placeholder constructions for \(R\), \(W\), and \(\Lambda\).

---

## Why this is exciting (math-wise)

- The Doob transform supplies a **systematic route from Jacobi/recoupling data to a gapped Markov semigroup** \(e^{tQ}\), with an observed near-linear critical exponent \(\nu\approx 1\) as \(q\to 1\).
- The \(q\)-\(6j\) error scaling gives a **numerically calibrated UV-safe window** for using \(q\)-deformed amplitudes at small \(\theta\) and moderate spin cutoff.

Concrete upgrade path: replace the placeholder kernels in \(T_q\) by exact representation-theoretic ones, then re-measure the gap scaling and test stability under increasing truncation \(N\) and spin cutoff.
