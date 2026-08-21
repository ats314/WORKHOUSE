# Reflection Positivity Stress Tests (Numerical Falsification Toolkit)

This note extracts the “stress-test” mindset from the project: treat reflection positivity (RP) as something you can try to **break quickly** in code, even before full proofs.

This doesn’t replace OS reconstruction proofs — it’s a *debugger* for subtle sign/definition errors.

---

## 1. What must be nonnegative

Given a Euclidean measure \(\mu\) on lattice fields and a time reflection \(\theta\), reflection positivity says:

\[
\langle F,F\rangle_{\mathrm{OS}}
:=
\int \overline{F}\,(\theta F)\,d\mu
\ge 0
\quad\text{for all }F\in\mathcal F^+,
\]

where \(\mathcal F^+\) is the algebra of observables supported on \(t\ge 0\).

Any counterexample \(F\) kills OS reconstruction.

---

## 2. The most practical numerical test: Gram matrices

Choose a finite basis of test observables \(F_1,\dots,F_m\subset\mathcal F^+\) and form the OS Gram matrix

\[
G_{ij} := \langle F_i, F_j\rangle_{\mathrm{OS}}
= \int \overline{F_i}\,(\theta F_j)\,d\mu.
\]

RP implies \(G\succeq 0\).  
So the test is simply: **compute eigenvalues of \(G\)** and search for negatives.

---

## 3. Test-function families that are cheap but expressive

Good “RP breakers” are:

1. **Single-link characters**: \(F(U)=\chi_{\mathrm{fund}}(U)\), \(\mathrm{Re\,Tr}(U)\).
2. **Plaquette terms** supported in \(t\ge 0\).
3. **Small Wilson loops** near the reflection plane.
4. **Random linear combinations** of local gauge-invariant polynomials:
   \[
   F_\xi = \sum_{k=1}^m \xi_k\, O_k,
   \quad \xi_k\sim\mathcal N(0,1).
   \]

The random-combo trick is great because if there’s a negative direction, random sampling tends to find it.

---

## 4. Monte Carlo estimator

If you can sample \(U^{(1)},\dots,U^{(M)}\sim\mu\),

\[
G_{ij}
\approx
\frac1M \sum_{m=1}^M \overline{F_i(U^{(m)})}\,F_j(\theta U^{(m)}).
\]

Then compute \(\lambda_{\min}(G)\). If it’s significantly negative relative to Monte Carlo error, RP likely fails (or your implementation does).

---

## 5. Minimal pseudocode

```python
# Given: sampler() -> configuration U ~ mu
# Given: reflection(theta, U) -> reflected configuration
# Given: list of observables Fs: callable(U)->complex

import numpy as np

def estimate_gram(Fs, M=20000):
    m = len(Fs)
    G = np.zeros((m,m), dtype=np.complex128)
    for _ in range(M):
        U = sampler()
        Uth = reflection(theta, U)
        vals = np.array([F(U) for F in Fs], dtype=np.complex128)
        vals_th = np.array([F(Uth) for F in Fs], dtype=np.complex128)
        G += np.outer(np.conjugate(vals), vals_th)
    return G / M

G = estimate_gram(Fs)
evals = np.linalg.eigvalsh((G+G.conj().T)/2)  # symmetrize for numerical stability
print("min eigenvalue:", evals[0])
```

---

## 6. Transfer-operator sanity tests (independent of Gram matrices)

If you approximate the transfer operator \(T\) in a truncated basis, you can sanity-check:

- spectrum should lie in \([0,1]\) (since \(T=e^{-H}\) with \(H\ge 0\)),
- leading eigenvalue should be \(1\) (vacuum),
- next eigenvalues should be separated if there’s a gap.

This can catch “silent” violations of positivity.

---

## 7. Why this tool matters in your program

Your pipeline depends on RP surviving:

- SAFE-region truncations / cutoffs,
- coarse-graining steps,
- continuum limits.

A numerical “RP breaker” is a brutally effective way to avoid spending months proving a theorem about a kernel you accidentally defined with the wrong sign.

---

## 8. What would make this *really* strong

- Use **high-temperature expansions / character expansions** to compute \(G\) exactly for small lattices and compare to Monte Carlo.
- Run tests across \(\beta\) and SAFE cutoffs to map where RP is fragile.
- Include gauge-fixing or gauge-projection variants to catch hidden symmetry breakage.
