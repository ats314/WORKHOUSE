# Extracting \(\chi_{\text{top}}\) from \(F(\theta)\): Finite Differences, Fourier Fits, and Consistency Checks

The project computes a \(\theta\)-dependent partition function \(Z(\theta)\) (via tensor contraction) and defines
\[
F(\theta) \equiv -\mathrm{Re}\,\log Z(\theta).
\]

The topological susceptibility is then targeted as
\[
\chi_{\text{top}}
=
\left.\frac{\partial^2 F(\theta)}{\partial \theta^2}\right|_{\theta=0}.
\]

This document collects the extraction strategies used in the notebooks, and highlights a key sign-convention pitfall that should be checked carefully.

---

## 1. Quadratic fit near \(\theta=0\)

If the sampling includes small \(|\theta|\), fit
\[
F(\theta)\approx c_0 + c_1 \theta + c_2 \theta^2.
\]
Then
\[
\chi_{\text{top}} = 2c_2.
\]

Physics expectation in CP-symmetric setups:
- \(F(\theta)\) should be even in \(\theta\),
- hence \(c_1\approx 0\).

---

## 2. Finite-difference estimate using \(F(\pi)-F(0)\)

If you only have coarse samples, a rough estimate used in the project is:

Assume \(F(\theta)\approx F(0)+\tfrac12\chi_{\text{top}}\theta^2\) over a wide range (crude!).
Then
\[
F(\pi)-F(0)\approx \tfrac12\chi_{\text{top}}\pi^2
\quad\Rightarrow\quad
\chi_{\text{top}}\approx \frac{2(F(\pi)-F(0))}{\pi^2}.
\]

Pros:
- requires only \(\theta=0\) and \(\theta=\pi\).

Cons:
- uncontrolled if higher harmonics in \(\theta\) are significant (very likely).

---

## 3. Fourier-series fit for periodic \(F(\theta)\)

Because \(\theta\) is an angle, \(F(\theta)\) should be \(2\pi\)-periodic (up to truncation effects).
A natural model is a Fourier series. One truncated fit used in the project is:

\[
F(\theta)\approx a_0 + a_1\cos(2\theta)+b_1\sin(2\theta)+a_2\cos(4\theta)+b_2\sin(4\theta).
\]

### Computing \(\chi_{\text{top}}\) from Fourier coefficients

Differentiate twice:
\[
\frac{d^2}{d\theta^2}\cos(2n\theta)=-(2n)^2\cos(2n\theta),
\qquad
\frac{d^2}{d\theta^2}\sin(2n\theta)=-(2n)^2\sin(2n\theta).
\]

Hence at \(\theta=0\),
\[
\chi_{\text{top}} = F''(0) = -4a_1 - 16 a_2 - 36 a_3 - \cdots
\]
(assuming a series in \(\cos(2n\theta)\) as written).

### Important sign convention check

One notebook sets
\[
\chi_{\text{top}} \stackrel{?}{=} 4a_1.
\]
That is only correct under a *different* parameterization, e.g. if one fits
\[
F(\theta)\approx \tilde a_0 + \frac{\chi_{\text{top}}}{4}(1-\cos(2\theta)) + \cdots,
\]
for which the coefficient of \(\cos(2\theta)\) is \(-\chi_{\text{top}}/4\), and therefore
\[
\chi_{\text{top}} = -4 a_1.
\]

So: **derive the mapping from your chosen Fourier basis** before trusting the sign.

---

## 4. A “genuine” cross-check: sector decomposition \(Z(\theta)=\sum_Q Z_Q e^{i\theta Q}\)

Independently of tensor methods, if topological charge sectors \(Q\in\mathbb{Z}\) are well-defined, then
\[
Z(\theta)=\sum_Q Z_Q\,e^{i\theta Q}.
\]
Then
\[
\left.\frac{\partial^2}{\partial\theta^2}\log Z(\theta)\right|_{\theta=0}
=
-\langle Q^2\rangle_{\theta=0},
\]
so
\[
\chi_{\text{top}}
=
\left.\frac{\partial^2 F}{\partial\theta^2}\right|_{\theta=0}
=
\mathrm{Re}\,\langle Q^2\rangle_{\theta=0}
\quad(\text{up to volume normalization conventions}).
\]

One project notebook implements this logic explicitly for 2D U(1) by sampling \(P(Q)\) and constructing \(Z(\theta)\) from the Fourier series in \(Q\).
That provides a baseline check on any tensor-network \(\chi_{\text{top}}\) extraction.

---

## 5. Practical best practices suggested by the project

1. Fit only even terms (cosines) if CP symmetry is expected. Check that fitted sine coefficients are near zero.

2. Use enough \(\theta\) points near 0 to resolve curvature reliably; a few points on \([0,2\pi)\) can easily “fit” periodicity while getting curvature wrong.

3. Propagate errors: \(\chi_{\text{top}}\) is a second derivative; it amplifies noise.

4. Always do at least two independent extraction methods (poly-fit near 0 and Fourier fit), and check they agree in sign and magnitude.
