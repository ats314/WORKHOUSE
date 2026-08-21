# Upgrading the q-transfer operator scaffold: replacing placeholders with true q-Racah / \\({}_4\\phi_3\\)

This note replaces the placeholder overlap kernel
\[
R_{ij}\approx e^{-|x_i-x_j|(1-q)}
\]
with an **honest q-Racah object** built from terminating \\({}_4\\phi_3\\) data, and replaces the numerical Gram–Schmidt “weight”
with the exact analytic orthogonality weight.

---

## q-Racah polynomials as a terminating \\({}_4\\phi_3\\)

Fix \\(q\\) and parameters \\(\alpha,\beta,\gamma,\delta\\) satisfying a finiteness condition so the orthogonality grid is
\(x\in\{0,1,\dots,N\}\).
(One standard choice is \\(\alpha q=q^{-N}\\), i.e. \\(\alpha=q^{-N-1}\\).)

Define the q-Racah polynomials by
\[
R_n\!\left(\mu(x);\alpha,\beta,\gamma,\delta\mid q\right)
:=
{}_4\phi_3\!\left(
\begin{matrix}
q^{-n},\;\alpha\beta q^{n+1},\;q^{-x},\;\gamma\delta q^{x+1}\\
\alpha q,\;\beta\delta q,\;\gamma q
\end{matrix}
;\;q,\;q
\right),
\qquad n=0,\dots,N,
\]
with \\(\mu(x)=q^{-x}+\gamma\delta q^{x+1}\\).

Because \\(q^{-n}\\) is an upper parameter, the \\({}_4\\phi_3\\) sum is **terminating** and has exactly \\(n+1\\) nonzero terms.

---

## Exact orthogonality weight \\(w(x)\\) and norms \\(h_n\\)

The family satisfies a closed orthogonality relation of the form
\[
\sum_{x=0}^N w(x)\,R_n(x)\,R_m(x)=h_n\,\delta_{nm}.
\]

A standard explicit weight is:
\[
w(x)
=
\frac{(\alpha q,\beta\delta q,\gamma q,\gamma\delta q;q)_x}{(q,\alpha^{-1}\gamma\delta q,\beta^{-1}\gamma q,\delta q;q)_x}
\cdot
\frac{1-\gamma\delta q^{2x+1}}{(\alpha\beta q)^x(1-\gamma\delta q)}.
\]

The norm \\(h_n\\) has a closed form, with a simplified expression depending on which finiteness condition is imposed.
For example, when \\(\alpha q=q^{-N}\\), one convenient expression is
\[
h_n =
\frac{(\beta^{-1},\gamma\delta q^2;q)_N}{(\beta^{-1}\gamma q,\delta q;q)_N}
\cdot
\frac{(1-\beta q^{-N})(\gamma\delta q)^n}{1-\beta q^{2n-N}}
\cdot
\frac{(q,\beta q,\beta\gamma^{-1}q^{-N},\delta^{-1}q^{-N};q)_n}{(\beta q^{-N},\beta\delta q,\gamma q,q^{-N};q)_n}.
\]

(Here \\((a;q)_x\\) is the q-Pochhammer symbol.)

---

## What you actually need computationally (a robust “kernel”)

Let
\[
P_{x n}:=R_n(x),\qquad W:=\mathrm{diag}(w(x)),\qquad H:=\mathrm{diag}(h_n).
\]

Then the orthogonality relation is exactly the finite-dimensional matrix identity
\[
P^\top W P = H.
\]

This identity is *numerically stable to test* and is the clean rep-theory replacement for the previous heuristic kernel.

If you want a normalized change-of-basis matrix, define
\[
U := W^{1/2} P H^{-1/2}.
\]
If the weight is positive (so a real square root exists), then \\(U\\) is orthogonal/unitary; if the weight has signs, \\(U\\) is a pseudo-unitary transform.
Either way, the identity \\(P^\top W P = H\\) is the invariant thing.

---

## Drop-in Python implementation (terminating \\({}_4\\phi_3\\) safe)

```python
import numpy as np

def q_poch(a, q, n):
    out = 1.0 + 0j
    for k in range(n):
        out *= (1.0 - a * (q ** k))
    return out

def q_poch_list(params, q, n):
    out = 1.0 + 0j
    for a in params:
        out *= q_poch(a, q, n)
    return out

def phi_4_3_terminating(a_params, b_params, q, z, n_terms):
    # Exact terminating sum: k = 0..n_terms
    s = 0.0 + 0j
    for k in range(n_terms + 1):
        num = q_poch_list(a_params, q, k)
        den = q_poch_list(b_params, q, k) * q_poch(q, q, k)  # (q;q)_k
        s += (num / den) * (z ** k)
    return s

def q_racah_R(n, x, alpha, beta, gamma, delta, q):
    a_params = [q**(-n), alpha*beta*q**(n+1), q**(-x), gamma*delta*q**(x+1)]
    b_params = [alpha*q, beta*delta*q, gamma*q]
    return phi_4_3_terminating(a_params, b_params, q, z=q, n_terms=n)

def q_racah_weight(x, alpha, beta, gamma, delta, q):
    num = q_poch_list([alpha*q, beta*delta*q, gamma*q, gamma*delta*q], q, x)
    den = q_poch_list([q, (gamma*delta*q)/alpha, (gamma*q)/beta, delta*q], q, x)
    return (num/den) * (1.0 - gamma*delta*q**(2*x+1)) / ((alpha*beta*q)**x * (1.0 - gamma*delta*q))

def q_racah_norm_alphaq(n, N, alpha, beta, gamma, delta, q):
    # simplified h_n for the finiteness condition alpha*q = q^{-N}
    pref = q_poch_list([beta**(-1), gamma*delta*q**2], q, N) / q_poch_list([beta**(-1)*gamma*q, delta*q], q, N)
    pref *= (1.0 - beta*q**(-N)) * (gamma*delta*q)**n / (1.0 - beta*q**(2*n - N))
    num = q_poch_list([q, beta*q, beta*(gamma**(-1))*q**(-N), (delta**(-1))*q**(-N)], q, n)
    den = q_poch_list([beta*q**(-N), beta*delta*q, gamma*q, q**(-N)], q, n)
    return pref * (num/den)

def q_racah_P_W_H(N, q, alpha, beta, gamma, delta):
    xs = np.arange(N+1)
    w = np.array([q_racah_weight(int(x), alpha, beta, gamma, delta, q) for x in xs], dtype=complex)
    h = np.array([q_racah_norm_alphaq(int(n), N, alpha, beta, gamma, delta, q) for n in xs], dtype=complex)
    P = np.zeros((N+1, N+1), dtype=complex)
    for x in xs:
        for n in xs:
            P[int(x), int(n)] = q_racah_R(int(n), int(x), alpha, beta, gamma, delta, q)
    return P, w, h

def check_orthogonality_identity(P, w, h):
    W = np.diag(w)
    M = P.conj().T @ W @ P
    return np.linalg.norm(M - np.diag(h))
```

---

## Where this plugs into the existing \\(T_q\\) assembly

The current scaffold constructs something like
\[
T_q \approx \Lambda^\top\,e^{Q}\,\Lambda\,R\,W
\]
and explicitly flags that \\(R\\) is still a placeholder.

Upgrade path:

- Replace the heuristic \\(R\\) with \\(P\\) and the weight matrix \\(W\\), or with the normalized transform \\(U=W^{1/2}PH^{-1/2}\\).
- Remove Gram–Schmidt and use the analytic \\(w(x),h_n\\) identity \\(P^\top W P = H\\).
- Keep \\(\Lambda\\) and the Wilson operator part \\(W\\) as placeholders only until the rep-theory objects are inserted.

---

## What remains “rep-theory”, not special functions

1. **Boundary basis**: decide whether boundary states are discrete representation labels (natural for q-Racah),
   or discretized holonomies \\(\chi\\).  
2. **\(\Lambda\) (RPP projection)**: should be built from intertwiners / branching coefficients.
3. **Wilson operator factor**: replace polynomial placeholders with q-characters / traces.

Once these are in place, the gap-scaling test becomes decisive: if the exponent near \\(\nu\approx1\\) survives,
the “deformation → gap” story is no longer a kernel artifact.

