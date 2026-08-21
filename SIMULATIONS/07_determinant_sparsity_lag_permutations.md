# Determinant Sparsity Identity for Lag-Permuted Observables

## Problem shape

Three observables (or “sensors”) produce a vector \(x\in\mathbb R^3\) at time \(k\).  
Two perturbation columns \(u,v\in\mathbb R^3\) are constructed from lagged differences under two lag assignments (permutations) \(\sigma,\tau\in S_3\).

A quantity of interest is the oriented volume / triple product
\[
D(x,u,v) := -\det\begin{pmatrix}
x_1 & u_1 & v_1\\
x_2 & u_2 & v_2\\
x_3 & u_3 & v_3
\end{pmatrix}.
\]

Naively, computing \(D\) is a full 3×3 determinant every time.

The project discovers a **classification and sparsity reduction** based on the relative permutation
\[
\pi = \tau\circ\sigma^{-1}.
\]

---

## 1. Key observation: rewrite using \(w=v-u\)

Let
\[
w := v-u.
\]
Then
\[
\det[x,u,v] = \det[x,u,u+w] = \det[x,u,w],
\]
since determinants are multilinear and alternating.

So computing \(D\) reduces to computing a determinant with columns \((x,u,w)\).

Now, the components of \(w\) satisfy:
\[
w_i = v_i-u_i.
\]
If the lag assignment fixes a row (i.e., \(\tau(i)=\sigma(i)\)), then \(v_i=u_i\) for that row and thus \(w_i=0\).

Therefore:

- the **support** of \(w\) is exactly the set of rows where \(\sigma\) and \(\tau\) differ,
- and that support size is determined by the cycle type of \(\pi\).

---

## 2. The classification theorem (cycle type)

For \(\pi\in S_3\), exactly one of these holds:

1. **Identity:** \(\pi = e\).  
   Then \(\tau=\sigma\) and \(v=u\), so \(w=0\) and
   \[
   D(x,u,v)=0.
   \]

2. **Transposition:** \(\pi\) swaps two indices and fixes one.  
   Then exactly one row is fixed, so \(w\) has support size 2.  
   In this case, the determinant reduces to a **2-row bilinear** expression.

3. **3-cycle:** \(\pi\) is a 3-cycle.  
   Then no row is fixed, \(w\) has support size 3, and no sparsity reduction occurs: use the full determinant.

So **only the 3-cycle case is genuinely “dense.”**

---

## 3. Explicit reduction formula in the transposition case

Assume the fixed row is \(r\in\{1,2,3\}\), and the active rows are \(p,q\) (the other two indices).  
Let \(w_p, w_q\) be the nonzero entries of \(w\).

Then one derived bilinear form is:

\[
D
=
x_r\,(u_p w_q - u_q w_p) \;-\;
u_r\,(x_p w_q - x_q w_p).
\]

So you can compute \(D\) using only a handful of multiplies/subtractions, and you never need to build a 3×3 matrix.

---

## 4. Verification: side-by-side correctness

A small deterministic test compared:

- the “old” full determinant,
- the “new” reduction formula,

and found agreement to \(2\times 10^{-14}\) error.

Example printed:

- det_old = -32.01082079
- det_new = -32.01082079
- abs error ≈ 2.13e-14

---

## 5. Large randomized verification (massive check)

A large randomized test (time-series length \(T=400\)) reports:

- total checked triples: **9,070,110**
- identity-case determinant max abs: \(6.48\times 10^{-13}\) (numerical zero)
- identity-case \(w_k\) max abs: \(9.15\times 10^{-13}\)
- support mismatches (rare accidental zero in a 3-cycle): 1
- transposition reduction checks: 2,699,368
- reduction mismatches: 0
- dtype divergences: 0

So the reduction appears *structurally exact* and numerically stable.

---

## 6. Why this is actually useful in theory work

If you’re trying to bound or average \(D(x,u,v)\) over random lags/permutations:

- this classification lets you separate the measure into cases with known degeneracy,
- and it implies many terms are identically zero (identity) or have reduced algebra (transpositions).

In other words, it turns a “messy combinatorial determinant quantity” into a tractable decomposition by conjugacy class in \(S_3\).

---

## 7. Next step: GPU kernel and branchless implementation

The notebook also sketches a **branched JAX kernel**:

- compute full determinant everywhere,
- overwrite identity cases with zero,
- overwrite transposition cases with the reduced closed form (choosing the fixed row).

That enables a single-pass GPU evaluation with a large speedup when identity/transposition dominate.

---

## Sources used

- `RUN 113.pdf` (side-by-side test; stress test; JAX branched kernel sketch).
- `RUN 113.pdf` (large randomized verification log; invariants classification).
