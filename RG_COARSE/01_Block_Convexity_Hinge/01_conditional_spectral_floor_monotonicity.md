# Conditional spectral floor monotonicity under coarse information
*(Project extraction: “Conditional Spectral Floor Monotonicity for Self-Adjoint Operators” + its use in coarse-graining arguments)*

## Why this is interesting
A recurring move in the project is to argue that **coarse-graining (conditioning, block maps, RG projections)** should *not decrease* a suitable notion of “stiffness” (lowest eigenvalue) in the physical directions. The core technical fact is a very clean inequality:

> **The minimum eigenvalue is concave.**  
> Equivalently: averaging a self-adjoint operator cannot push its spectral floor downward.

Framed correctly, this is a small lemma with oversized consequences: it becomes a plug‑in module for any argument that tries to make **“defects” monotone across scales**.

---

## 1. Finite-dimensional lemma (matrix version)

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space, and let $H(\omega)\in\mathbb R^{n\times n}$ be symmetric for each $\omega$.
Let $\mathcal G\subset\mathcal F$ be a sub-$\sigma$-algebra, and assume $H$ is integrable so that the conditional expectation
\[
\mathbb E[H\mid \mathcal G]
\]
is well-defined as an $\mathcal G$‑measurable symmetric matrix.

### Theorem 1.1 (Conditional spectral floor monotonicity)
For $\mathbb P$-a.e. $\omega$,
\[
\lambda_{\min}\!\big(\mathbb E[H\mid\mathcal G](\omega)\big)
\ \ge\
\mathbb E\!\big[\lambda_{\min}(H)\mid\mathcal G\big](\omega).
\]

#### Proof
Use the Rayleigh–Ritz variational characterization:
\[
\lambda_{\min}(A)=\min_{\|v\|=1}\langle v,Av\rangle.
\]
Fix a unit vector $v$. Then
\[
\langle v,\mathbb E[H\mid\mathcal G]v\rangle
=
\mathbb E[\langle v,Hv\rangle\mid\mathcal G]
\ge
\mathbb E[\lambda_{\min}(H)\mid\mathcal G].
\]
Now minimize over $v$ on the left-hand side. ∎

---

## 2. Quadratic form version (self-adjoint operators)

A version used implicitly in infinite-dimensional settings:

Let $H(\omega)$ be a random self-adjoint operator on a Hilbert space $\mathcal H$, uniformly bounded below, with a common dense quadratic form domain $\mathcal D$ and such that $\omega\mapsto \langle \psi, H(\omega)\psi\rangle$ is integrable for each $\psi\in\mathcal D$.

Define the form-averaged operator (or averaged form)
\[
\langle \psi, \bar H \psi\rangle := \mathbb E[\langle \psi, H(\omega)\psi\rangle \mid \mathcal G].
\]

Then the same Rayleigh–Ritz argument gives, heuristically and often rigorously under standard measurability/closability hypotheses,
\[
\inf_{\|\psi\|=1}\langle \psi, \bar H \psi\rangle
\ \ge\
\mathbb E\!\Big[\inf_{\|\psi\|=1}\langle \psi, H(\omega)\psi\rangle \,\Big|\,\mathcal G\Big].
\]

---

## 3. Defect monotonicity as a corollary

Fix a target stiffness $\kappa_*>0$ and define the **defect** of a matrix $A$ by
\[
\delta(A):=\max\{0,\ \kappa_*-\lambda_{\min}(A)\}.
\]
Because $x\mapsto \max\{0,\kappa_*-x\}$ is convex and $\lambda_{\min}$ is concave, Jensen gives
\[
\delta\!\big(\mathbb E[H\mid \mathcal G]\big)
\ \le\
\mathbb E[\delta(H)\mid \mathcal G].
\]
So *defect cannot increase under conditioning*.

This is exactly the monotonicity shape needed by any “obstruction principle”: if a defect goes to $0$ at small scales, it must already have been $0$ at all coarser scales.

---

## 4. Tiny simulation (sanity check)

This is not a proof (the proof above is the proof).  
It’s just a concrete numerical check to catch sign mistakes and build intuition.

We generate $100$ random symmetric matrices $H(\omega)\in\mathbb R^{8\times 8}$, then “condition” on a coarse observable by grouping them into $10$ bins of size $10$. In each bin we compare:

- $\lambda_{\min}\big(\mathbb E[H\mid\mathcal G]\big)$ = minimum eigenvalue of the *bin-average* matrix
- $\mathbb E[\lambda_{\min}(H)\mid\mathcal G]$ = average of the minimum eigenvalues in that bin

### Python code
```python
import numpy as np
import numpy.linalg as la
import pandas as pd

def rand_sym(n, seed=None):
    A = np.random.normal(size=(n,n))
    return (A + A.T)/2

np.random.seed(0)
n = 8
num = 100
mats = [rand_sym(n) for _ in range(num)]
groups = [list(range(i,i+10)) for i in range(0, num, 10)]

rows = []
for gi,g in enumerate(groups):
    Havg = sum(mats[i] for i in g)/len(g)
    lam_avg = la.eigvalsh(Havg)[0]
    lam_cond = sum(la.eigvalsh(mats[i])[0] for i in g)/len(g)
    rows.append((gi, lam_avg, lam_cond, lam_avg-lam_cond))

df = pd.DataFrame(rows, columns=[
    "group", "lambda_min(E[H|G])", "E[lambda_min(H)|G]", "difference"
])
print(df.round(3))
print("min difference:", df["difference"].min())
```

### Output (rounded to 3 decimals)

| group | $\lambda_{\min}(\mathbb E[H\mid\mathcal G])$ | $\mathbb E[\lambda_{\min}(H)\mid\mathcal G]$ | difference |
|---:|---:|---:|---:|
| 0 | -0.973 | -3.253 | 2.280 |
| 1 | -1.090 | -3.251 | 2.161 |
| 2 | -0.869 | -3.116 | 2.246 |
| 3 | -1.136 | -3.148 | 2.012 |
| 4 | -0.997 | -3.308 | 2.311 |
| 5 | -1.138 | -3.305 | 2.167 |
| 6 | -1.134 | -3.393 | 2.259 |
| 7 | -0.838 | -3.189 | 2.352 |
| 8 | -0.962 | -3.152 | 2.190 |
| 9 | -0.958 | -3.240 | 2.281 |

All differences are positive (here the smallest is about $2.01$), matching the theorem.

---

## 5. How this plugs into the larger program

The project’s “geometric mass gap” strategy wants to turn:

1. **Local stiffness / curvature** in physical directions  
2. into **functional inequalities** (Poincaré / log-Sobolev / spectral gap of configuration diffusion)  
3. and then into a **Hamiltonian mass gap** via OS reconstruction and a one-step comparison inequality.

This lemma is a technical hinge for step (1→2) whenever you build a **scale‑dependent stiffness functional** and want it to behave monotonically under RG blocking or conditional expectations.

---

## 6. What to do next

1. **State precisely what is being averaged.**  
   In real RG, the coarse “effective action” is a log-integral, so its Hessian is not literally a conditional expectation of fine Hessians; extra covariance terms appear. You’ll want a corrected monotonicity statement that accounts for those terms.

2. **Use this lemma as a bound, not an identity.**  
   Even when $\nabla^2 S_{\text{eff}}$ differs from $\mathbb E[\nabla^2 S\mid\text{coarse}]$, the lemma often still gives a useful *inequality* once you identify a form-dominating piece.

3. **Push into a stability theorem.**  
   Combine defect monotonicity with OS positivity to prove a rigidity statement: “if defect $\to0$, the continuum limit is Gaussian.”

(That rigidity/obstruction piece is extracted in a separate document in this set.)
