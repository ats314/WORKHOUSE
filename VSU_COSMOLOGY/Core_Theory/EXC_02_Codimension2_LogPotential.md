# EXC_02 — Codimension-2 Log Potentials and the \(1/k^2\) Signature

## What this document contains

A geometric asymptotic statement about potentials sourced on submanifolds: the far-field behavior is controlled by the **codimension** \(k\).

In particular, codimension \(k=2\) produces a **logarithmic potential** and therefore
\[
g(r)\propto \frac{1}{r},
\]
the scaling behind asymptotically flat rotation curves.

**Primary source:** `WIZ UPDATE.txt`. A short connection is made to the anti-kernel spectral multiplier used in EXC\_01.

---

## 1. Setup: potential sourced on a submanifold

The project considers a source supported on a \(d\)-dimensional submanifold \(\Sigma\subset\mathbb{R}^n\) and writes a smeared potential of the form
\[
\Phi(y)=\int_\Sigma \rho(y')\,G_n\!\left(|y-y'|^2+R^2\right)\,d\mathrm{vol}_\Sigma(y').
\]

---

## 2. Far-field expansion and “mass times Green’s function” factorization

For large transverse distance \(R\), the project expands the kernel and obtains the leading behavior
\[
\Phi(y)\approx G_n(R)\int_\Sigma \rho(y')\,d\mathrm{vol}_\Sigma(y')
=
M_\Sigma\,G_n(R),
\]
i.e. “total mass on \(\Sigma\)” times a radial Green factor.

---

## 3. Codimension controls the potential law

The project identifies the relevant “transverse” dimension as the codimension
\[
k := n-d,
\]
and records the corresponding Green-function asymptotics:

- If \(k\neq 2\), then
  \[
  \Phi(r)\sim \frac{1}{r^{k-2}}.
  \]
- If \(k=2\), then
  \[
  \Phi(r)\sim \log r,
  \qquad
  g(r)=|\nabla\Phi(r)|\sim \frac{1}{r}.
  \]

---

## 4. Connection to the anti-kernel multiplier \(M(k)=1+\mu^2/k^2\)

The Fourier signature of a log Green’s function is a \(1/k^2\) factor, because
\[
\widehat{(-\Delta)^{-1}f}(k)=\frac{1}{k^2}\,\hat f(k).
\]

The project’s anti-kernel used in the galaxy fitting pipeline is
\[
M(k)=1+\left(\frac{\mu}{k}\right)^2,
\]
so (in the continuous-operator idealization) the mapping corresponds to
\[
g_\mu = g_b + \mu^2\,(-\Delta)^{-1}g_b.
\]

This is a clean mathematical bridge inside the project between:
- codimension-2 log-potential reasoning, and
- the empirically tuned infrared-boost operator that fits the SPARC sample better than suppression-type kernels in the recorded runs (EXC\_01).

