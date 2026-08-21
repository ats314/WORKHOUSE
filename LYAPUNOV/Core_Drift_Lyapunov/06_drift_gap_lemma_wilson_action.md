# Drift Gap Lemma for the Wilson Plaquette Badness Functional
*(explicit computation of \(L\mathcal B_\Lambda\) and a volume-uniform inward drift strip)*

## 1. Context

A standard local-to-global strategy for Poincaré/LSI on a high-dimensional configuration manifold uses:

1. a local Poincaré inequality on a “good” region,
2. a Foster–Lyapunov drift inequality outside,
3. a gluing theorem.

This note isolates the key local geometric input for step (2): an explicit negative drift for an averaged plaquette defect functional \(\mathcal B_\Lambda\).

---

## 2. Definitions

Let \(\Lambda\) be a finite lattice box and let \(P(\Lambda)\) be its set of plaquettes.

Define the plaquette defect (for \(G=\mathrm{SU}(2)\), but only the smoothness and boundedness matter here):
\[
b(g):=1-\frac12\Re\operatorname{Tr}(g),
\qquad g\in G.
\]
Define the averaged badness functional
\[
\mathcal B_\Lambda(U)
:=\frac{1}{|P(\Lambda)|}\sum_{p\in P(\Lambda)} b(U_p),
\]
where \(U_p\) is the plaquette holonomy.

The Wilson action is
\[
S_W(U)=\beta\sum_{p\in P(\Lambda)} b(U_p)
=\beta\,|P(\Lambda)|\,\mathcal B_\Lambda(U).
\tag{2.1}
\]

Let the reversible diffusion generator be
\[
L := \Delta - \langle \nabla S_W,\nabla\cdot\rangle
\]
with respect to the product metric on \(G^{E(\Lambda)}\).

---

## 3. Exact identity for the drift term

Differentiate (2.1):
\[
\nabla S_W
= \beta\,|P(\Lambda)|\,\nabla \mathcal B_\Lambda.
\tag{3.1}
\]
This is an exact identity, not an approximation.

Therefore the drift contribution satisfies
\[
\boxed{
\langle \nabla S_W,\nabla \mathcal B_\Lambda\rangle
=
\beta\,|P(\Lambda)|\,|\nabla \mathcal B_\Lambda|^2.
}
\tag{3.2}
\]

---

## 4. Bounded geometry bound on \(\Delta\mathcal B_\Lambda\)

Because:

- each plaquette depends on finitely many link variables,
- \(b(\cdot)\) is smooth on compact \(G\),
- overlaps of plaquettes are uniformly bounded by lattice degree,

there exists a constant \(C_\Delta<\infty\), independent of \(|\Lambda|\), such that
\[
\boxed{
|\Delta\mathcal B_\Lambda(U)| \le C_\Delta
\qquad \forall U.
}
\tag{4.1}
\]

This is the “nothing blows up just because volume grows” bound.

---

## 5. Assemble \(L\mathcal B_\Lambda\)

By definition,
\[
L\mathcal B_\Lambda
=
\Delta\mathcal B_\Lambda
-
\langle \nabla S_W,\nabla\mathcal B_\Lambda\rangle.
\]
Using (3.2) and (4.1),
\[
\boxed{
L\mathcal B_\Lambda
\le
C_\Delta
-
\beta\,|P(\Lambda)|\,|\nabla \mathcal B_\Lambda|^2.
}
\tag{5.1}
\]

---

## 6. Boundary strip gradient lower bound (the only geometric seam)

Fix \(\varepsilon>0\) and \(\delta>0\). Consider the boundary strip
\[
\Sigma:=\{U:\ \varepsilon<\mathcal B_\Lambda(U)<\varepsilon+\delta\}.
\]

On \(\Sigma\), a positive density of plaquettes must satisfy \(b(U_p)\ge \varepsilon/2\). For \(G=\mathrm{SU}(2)\), writing \(g=\exp(i\theta\,\hat n\cdot\sigma)\) gives \(b(g)=1-\cos\theta\), hence \(|\nabla b(g)|\asymp|\sin\theta|\). In particular, there exists \(c_\varepsilon>0\) such that
\[
b(g)\ge \varepsilon/2\quad\Longrightarrow\quad |\nabla b(g)|\ge c_\varepsilon.
\tag{6.1}
\]

To avoid cancellations between contributions from different plaquettes sharing links, assume a **local transversality / noncancellation hypothesis**:

### Assumption (A′) (local noncancellation)
On the strip \(\Sigma\), the gradients of the contributing plaquette defects cannot cancel more than a fixed fraction, yielding
\[
\boxed{
|\nabla\mathcal B_\Lambda(U)|^2 \ge \frac{c_\varepsilon^2}{|P(\Lambda)|}
\qquad \forall U\in\Sigma.
}
\tag{6.2}
\]

This assumption is the precise place where lattice geometry + group algebra enter.

---

## 7. Drift gap lemma

### Lemma 7.1 (Uniform negative drift on the boundary strip)
Assume (A′). Then on \(\Sigma\),
\[
\boxed{
L\mathcal B_\Lambda(U)\le C_\Delta - \beta c_\varepsilon^2.
}
\tag{7.1}
\]
In particular, if
\[
\boxed{
\beta > \beta_* := \frac{C_\Delta}{c_\varepsilon^2},
}
\tag{7.2}
\]
then there exists \(\rho>0\), independent of \(\Lambda\), such that
\[
\boxed{
L\mathcal B_\Lambda(U)\le -\rho
\qquad\forall U\in\Sigma,
\quad
\rho:=\beta c_\varepsilon^2 - C_\Delta.
}
\tag{7.3}
\]

**Proof.**
Insert (6.2) into (5.1):
\[
L\mathcal B_\Lambda
\le
C_\Delta - \beta|P|\cdot \frac{c_\varepsilon^2}{|P|}
=
C_\Delta - \beta c_\varepsilon^2.
\]
If \(\beta>\beta_*\), the right-hand side is \(-\rho<0\). \(\square\)

---

## 8. Why this matters

Lemma 7.1 is exactly the “inward drift on a boundary strip” hypothesis used by smooth gluing lemmas:

- it produces a Lyapunov drift inequality without illegal indicator gradients,
- constants are volume-independent,
- the only genuinely nontrivial seam is the local noncancellation hypothesis (A′).

Once (A′) is proven (or replaced by a verified algebraic lemma), the drift leg of the Poincaré/LSI proof is closed.

