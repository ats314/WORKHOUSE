# Numerical sanity check (toy): \(U(1)\) Wilson Hessian equals \(\beta\,d_1^\top d_1\)

The project’s nonabelian derivation (SU(N)) is conceptual and uses BCH expansions.  
As a cheap “unit test” of the *discrete geometry* side (cochains \(d_0,d_1\), Maxwell matrix structure, kernel dimensions), it’s useful to check the abelian \(U(1)\) case where the Wilson action is explicit in link angles.

This is not a proof of the SU(N) result; it is just a consistency check that the discrete operator you are relying on is exactly the expected one.

---

## 1. Model

On a 2D periodic \(L\times L\) lattice:

- link variables are angles \(\theta_e\in\mathbb R\) (for \(U(1)\), \(U_e=e^{i\theta_e}\)),
- plaquette angle is the signed sum \((d_1\theta)_p\),
- Wilson action is
  \[
  S(\theta)=\beta \sum_{p}(1-\cos((d_1\theta)_p)).
  \]

At \(\theta=0\), Taylor expansion gives
\[
S(\theta)=\frac{\beta}{2}\,\|d_1\theta\|^2 + O(\|\theta\|^4)
\quad\Rightarrow\quad
\nabla^2 S(0)=\beta\,d_1^\top d_1.
\]

---

## 2. What we check numerically

1. Finite-difference Hessian at \(\theta=0\) matches \(\beta\,d_1^\top d_1\).
2. Kernel dimension of \(d_1^\top d_1\) matches “exact + harmonic” on the 2-torus:
   \[
   \dim\ker(d_1)=\mathrm{rank}(\mathrm{im}\,d_0) + \dim H^1(\mathbb T^2)
   =(|V|-1)+2
   = L^2+1.
   \]
3. Smallest positive eigenvalue matches the expected Fourier formula:
   \[
   \lambda_{\min,+}\big(\beta\,d_1^\top d_1\big)=\beta\cdot 4\sin^2\Big(\frac{\pi}{L}\Big).
   \]

---

## 3. Code

See `u1_hessian_check.py` in the same folder.

---

## 4. Output (beta = 2.7, eps = 1e-4)

Running the script prints:

```text
L=3x3: rel_err=6.077e-09, nullity=10, min_pos_eig=8.100000, nE=18, nV=9, nP=9
L=4x4: rel_err=6.077e-09, nullity=17, min_pos_eig=5.400000, nE=32, nV=16, nP=16
L=5x5: rel_err=6.077e-09, nullity=26, min_pos_eig=3.731308, nE=50, nV=25, nP=25
```

Interpretation:

- The **relative error \(\sim 10^{-8}\)** confirms the finite-difference Hessian matches the analytic matrix.
- The **nullities** are \(L^2+1\), matching \((|V|-1)+2\).
- The **smallest positive eigenvalues** match \(\beta\cdot 4\sin^2(\pi/L)\) exactly to floating error.

---

## 5. Why this matters for the nonabelian program

The hard part of the nonabelian theory is controlling remainders away from the vacuum and managing gauge invariance.

But the **operator-theoretic backbone** (the incidence structure of \(d_1^\ast d_1\), Hodge splitting, kernel geometry, and the transverse “physical” coercivity) is already present in the abelian case and survives as a linearized structure in SU(N).

This toy check is a quick way to detect if you ever accidentally changed sign conventions, orientation conventions, or adjoint definitions in later steps.

---
