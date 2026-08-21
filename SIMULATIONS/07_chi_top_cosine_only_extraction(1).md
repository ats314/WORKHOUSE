# $\chi_{\text{top}}$ from Cosine-Only Fourier Extraction (and Why High Harmonics Can Lie)

This note is about extracting topological susceptibility from discrete free-energy data
\[
F(\theta) \equiv -\log Z(\theta)
\]
in a way that respects periodicity and $CP$ evenness *by construction*.

---

## 1. Evenness + $2\pi$ periodicity ⇒ cosine-only Fourier series

For an ordinary $\theta$ term with integer topological charge $Q\in\mathbb{Z}$,
\[
Z(\theta)=\sum_{Q\in\mathbb{Z}} Z_Q\,e^{i\theta Q},
\]
and $CP$ invariance at $\theta=0$ implies $Z_Q=Z_{-Q}$, hence $Z(\theta)=Z(-\theta)$ is even.

Therefore, the free energy is even:
\[
F(\theta)=F(-\theta),
\]
and (assuming smoothness) admits a cosine-only Fourier series:
\[
F(\theta)=a_0+\sum_{n=1}^{\infty} a_n \cos(n\theta).
\]

No sine terms. If your fit produces sizable sine coefficients, it’s a diagnostic: either noise, broken symmetry, or a bug.

---

## 2. The key identity: curvature at the origin is a weighted sum of cosine modes

Differentiate twice:
\[
F''(\theta)= -\sum_{n=1}^{\infty} n^2 a_n \cos(n\theta),
\]
so at $\theta=0$,
\[
\boxed{\;\chi_{\text{top}} \equiv F''(0)= -\sum_{n=1}^{\infty} n^2 a_n.\;}
\]

That minus sign is not optional.

### Special case: dilute-instanton / single-mode ansatz
If you approximate
\[
F(\theta)\approx \text{const} - \chi \cos\theta,
\]
then \(a_1=-\chi\) and \(F''(0)=\chi\).

If instead your model is $\pi$-periodic and you fit
\[
F(\theta)\approx \text{const} + a_1\cos(2\theta),
\]
then
\[
\chi_{\text{top}} = -4a_1.
\]

---

## 3. Practical fitting from discrete samples

Suppose you have samples \(\{(\theta_i,F_i)\}_{i=1}^M\).

Pick a truncation order \(N\) and solve the least-squares problem
\[
F_i \approx a_0+\sum_{n=1}^{N} a_n\cos(n\theta_i).
\]

Then estimate
\[
\chi_{\text{top}}^{(N)} = -\sum_{n=1}^{N} n^2 a_n.
\]

### Important warning: $n^2$ makes high modes dangerous
Because of the \(n^2\) weight, even a modest overfit in \(a_N\) can dominate \(\chi_{\text{top}}\).
So, unlike “fit the curve everywhere,” extracting curvature at 0 wants you to:

- keep \(N\) **small**, or
- **regularize** high modes (ridge/Tikhonov), or
- fit only **small** \(|\theta|\) data (and then you’re basically doing a polynomial fit).

---

## 4. Robust cosine-only extraction code (NumPy)

```python
import numpy as np

def fit_cosine_series(theta, F, N, ridge=0.0):
    '''
    Fit F(theta) = a0 + sum_{n=1..N} a_n cos(n theta)
    using (optionally) ridge regularization on a_n (not on a0).
    '''
    theta = np.asarray(theta)
    F = np.asarray(F)

    X = np.column_stack([np.ones_like(theta)] +
                        [np.cos(n*theta) for n in range(1, N+1)])

    if ridge == 0.0:
        a = np.linalg.lstsq(X, F, rcond=None)[0]
    else:
        # Ridge: minimize ||Xa - F||^2 + ridge * ||a_{1:}||^2
        # (do not penalize the constant term)
        P = np.diag([0.0] + [1.0]*N)
        a = np.linalg.solve(X.T@X + ridge*P, X.T@F)

    # chi_top = F''(0) = -sum_{n>=1} n^2 a_n
    chi = -sum((n**2)*a[n] for n in range(1, N+1))
    return a, chi
```

---

## 5. A diagnostic workflow that avoids “false negative $\chi_{\text{top}}$”

If you see an unphysical negative curvature at \(\theta=0\):

1. **Check the $6j$ engine** first (symmetry + parity tests).
2. Then check that your **$F(\theta)$** is even within tolerance.
3. Fit with **small** \(N\) (e.g. \(N=1,2,3\)) and see if \(\chi_{\text{top}}\) stabilizes.
4. If \(\chi_{\text{top}}\) flips sign when increasing \(N\), you’re seeing high-harmonic pollution.
   Add ridge regularization or restrict the fit window to small \(|\theta|\).

---

## 6. Optional but conceptually clean: Fourier-transform $Z(\theta)$, not $F(\theta)$

Because \(F=-\log Z\) is nonlinear, Fourier coefficients of \(F\) do *not* directly correspond to the topological charge distribution.

If you can compute \(Z(\theta)\) (not just \(F(\theta)\)), then a discrete Fourier transform gives estimates of \(Z_Q\), and
\[
\chi_{\text{top}} = \frac{1}{V}\frac{\sum_Q Q^2 Z_Q}{\sum_Q Z_Q}
\]
at \(\theta=0\).

This is closer to the underlying physics and typically more stable numerically.

---

## 7. What to do next

- Use cosine-only fits as a *symmetry-enforcing* estimator.
- Keep \(N\) low, or regularize high modes.
- Treat any weird global $\theta$ features as “suspicious until the $6j$ and cache are certified.”

