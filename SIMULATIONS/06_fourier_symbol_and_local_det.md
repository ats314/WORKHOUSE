# Appendix: Exact Fourier Symbol \(\mathsf D_1(k)\), Eigenvalues, and a Local \(\det M>0\) Gram Check

## 0. Why this appendix exists

Two separate “finite-dimensional” computations appear throughout the project:

1. The **global Fourier symbol** of the discrete curl \(d_1\) and of \(d_1^\ast d_1\), which makes the *horizontal-sector spectral gap* explicit.

2. A **local Gram matrix** \(M_{pq}=\langle d_1^\ast\delta_p, d_1^\ast\delta_q\rangle\) for the plaquettes incident to a fixed link, whose determinant can be computed in closed form, giving an “exact positivity certificate” at the purely local combinatorial level.

This file writes both in one place, cleanly.

---

## 1. Discrete operators on \(\mathbb Z^d\)

Let \(X=(X_\mu)_{\mu=1}^d\) be a \(\mathfrak g\)-valued 1-cochain (link field). Define the forward difference symbol
\[
q_\mu(k):=e^{ik_\mu}-1,\qquad k\in\mathbb T^d=[-\pi,\pi]^d.
\]
Also define
\[
\lambda(k):=\sum_{\mu=1}^d |q_\mu(k)|^2
=4\sum_{\mu=1}^d \sin^2\!\Big(\frac{k_\mu}{2}\Big).
\]

### 1.1 Fourier symbol of \(d_0\) and \(d_0^\ast\)

The discrete gradient \(d_0:\mathcal C^0\to\mathcal C^1\) has symbol \(\mathsf D_0(k)=q(k)\) (a \(d\times 1\) column).
Its adjoint \(d_0^\ast\) has symbol \(\mathsf D_0(k)^\ast=\overline{q(k)}^\top\).

So the horizontal constraint \(d_0^\ast X=0\) becomes
\[
\overline{q(k)}\cdot \widehat X(k)=0.
\]

---

## 2. Fourier symbol \(\mathsf D_1(k)\) of the discrete curl \(d_1\)

The discrete curl \(d_1:\mathcal C^1\to\mathcal C^2\) maps a 1-cochain to a 2-cochain indexed by oriented plaquette directions \((\mu,\nu)\), \(\mu<\nu\). Its symbol is the \(\binom{d}{2}\times d\) matrix \(\mathsf D_1(k)\) defined by
\[
\boxed{
(\mathsf D_1(k)\,\widehat X(k))_{\mu\nu}
=
q_\nu(k)\,\widehat X_\mu(k)\;-\;q_\mu(k)\,\widehat X_\nu(k),
\qquad \mu<\nu.
}
\]

Equivalently: each row corresponding to \((\mu,\nu)\) has two nonzero entries,
\[
(\mathsf D_1(k))_{(\mu,\nu),\mu}=q_\nu(k),\qquad
(\mathsf D_1(k))_{(\mu,\nu),\nu}=-q_\mu(k).
\]

---

## 3. The Maxwell symbol and eigenvalues

Compute
\[
\mathsf D_1(k)^\ast\mathsf D_1(k)
=
\lambda(k)\,I_d - q(k)\otimes \overline{q(k)}.
\]

So:

- \(q(k)\) is an eigenvector with eigenvalue \(0\).
- any vector \(\eta\in\mathbb C^d\) with \(\overline{q(k)}\cdot \eta=0\) is an eigenvector with eigenvalue \(\lambda(k)\).

Thus the eigenvalues of \(\mathsf D_1^\ast\mathsf D_1\) are
\[
\boxed{
0 \text{ (mult. 1)},\qquad
\lambda(k) \text{ (mult. }d-1\text{)}.
}
\]

In particular, **on the horizontal sector** (\(\overline{q}\cdot \widehat X=0\)), the Maxwell operator is scalar:
\[
(d_1^\ast d_1)\widehat X(k)=\lambda(k)\widehat X(k).
\]

This is the exact statement exploited in the Green’s function decay hinge.

---

## 4. A purely local Gram matrix and its determinant

Now switch from Fourier space to a *local* real-space computation on a fixed link \(\ell\).

Let \(\delta_p\) denote the plaquette basis vector in \(\mathcal C^2\). Define the 1-cochain
\[
w_p := d_1^\ast \delta_p\in\mathcal C^1.
\]

Fix a link \(\ell=(x,\mu)\) in \(d=4\). There are \(m=6\) plaquettes incident to \(\ell\):
for each \(\nu\neq \mu\) (three choices), there are two:
\[
p_{\nu,+}:=(x;\mu,\nu),
\qquad
p_{\nu,-}:=(x-\hat\nu;\mu,\nu).
\]

### 4.1 Explicit coefficients

For \(p=(x;\mu,\nu)\) with \(\mu<\nu\),
\[
w_p = e_{x,\mu} + e_{x+\hat\mu,\nu} - e_{x+\hat\nu,\mu} - e_{x,\nu}.
\]

For \(p_{\nu,-}=(x-\hat\nu;\mu,\nu)\),
the same formula gives the coefficient of the fixed edge \(e_{x,\mu}\) as \(-1\).

Define \(s_p\in\{\pm1\}\) as the coefficient of \(e_{x,\mu}\) inside \(w_p\):
\[
s_{\nu,+}=+1,\qquad s_{\nu,-}=-1.
\]

### 4.2 The local Gram matrix

Define
\[
M_{pq}:=\langle w_p,w_q\rangle_{\mathcal C^1}.
\]

- \(M_{pp}=4\) because \(w_p\) has 4 unit coefficients.
- for \(p\neq q\), the only shared edge is the fixed link edge \(e_{x,\mu}\), so \(M_{pq}=s_ps_q\).

Therefore
\[
\boxed{
M = 3I_6 + s s^\top,
}
\]
where \(s\in\{\pm1\}^6\) is the sign vector.

### 4.3 Eigenvalues and determinant

Since \(ss^\top\) has rank 1 and \(s^\top s=6\), the eigenvalues of \(M\) are:
\[
\lambda=3 \text{ (mult. 5)},\qquad \lambda=3+6=9 \text{ (mult. 1)}.
\]

Hence
\[
\boxed{
\det M = 3^5\cdot 9 = 2187>0.
}
\]

So the local Gram matrix is strictly positive definite, with an explicit uniform lower bound:
\[
M\succeq 3I_6.
\]

---

## 5. Tiny numerical sanity check (optional)

A minimal Python check:

```python
import numpy as np
s=np.array([1,-1,1,-1,1,-1],dtype=float)
M=3*np.eye(6)+np.outer(s,s)
print(np.linalg.eigvals(M))
print(np.linalg.det(M))
```

Expected output:

- eigenvalues: \(9,3,3,3,3,3\)
- determinant: \(2187\).

This is not a proof (the algebra already is), but it is a good sign/orientation bug-catcher.
