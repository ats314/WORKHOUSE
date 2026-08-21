# Projection vs inversion: when “scalarization” is legitimate (operator lemma)

This note is extracted from the chat theorem idea, but recast in a way that matches the project’s actual needs:
**when can you project a covariance operator and then invert, without changing the result?**

This matters because your entire chain relies on restricting to *horizontal* directions.

---

## 1. Abstract operator fact (Schur complement obstruction)

Let \(\mathcal H = \mathcal H_\parallel \oplus \mathcal H_\perp\) and \(P\) be the orthogonal projection onto \(\mathcal H_\parallel\).
Let \(M:\mathcal H\to\mathcal H\) be strictly positive self-adjoint with block form
\[
M=
\begin{pmatrix}
A & B\\
B^\* & C
\end{pmatrix},
\qquad A>0,\ C>0.
\]

Define two operators on \(\mathcal H_\parallel\):
\[
M^{-1}_{\mathrm{proj}} := P M^{-1} P,
\qquad
M^{-1}_{\mathrm{scal}} := (PMP)^{-1}=A^{-1}.
\]

Then
\[
\boxed{
P M^{-1} P
=
A^{-1}
+
A^{-1} B\,(C - B^\* A^{-1} B)^{-1} B^\* A^{-1}.
}
\]
In particular,
\[
P M^{-1} P - (PMP)^{-1}\succeq 0,
\]
with equality iff \(B=0\).

So: **projection and inversion commute iff there is no mixing block.**

---

## 2. Why your project is (mostly) safe from this obstruction

Your setup contains a crucial structural lemma: at the vacuum, the relevant Maxwell/Hodge operators preserve the Hodge splitting
\[
\mathcal C^1 = \mathrm{im}(d_0)\ \oplus\ \ker(d_0^\*).
\]

Equivalently, the mixed block \(B\) vanishes between vertical (exact) and horizontal (divergence-free) subspaces.

In that case,
\[
P M^{-1} P = (PMP)^{-1},
\]
so restricting to horizontals and inverting is legitimate.

---

## 3. The bigger meta-lesson

This lemma is a **great referee shield**:

- It tells you exactly where a projected inverse is safe,
- It tells you what you must check if you change gauge fixing, discretization, or observable class.

If you ever see a numerical mismatch between two “ways of computing the same covariance,” this Schur-complement identity tells you the first thing to check:
**did you accidentally introduce a nonzero mixing block \(B\)?**
