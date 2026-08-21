# Cube Bianchi as Maxwell–Calladine Self-Stress (Rigidity Viewpoint)

*This note is extracted from the cube-level “Bianchi = self-stress” sketch developed in this chat, rewritten as a clean finite-dimensional linear-algebra lemma. The goal is conceptual: it connects lattice gauge constraints to rigidity theory and explains, at the level of chain complexes, how redundancy generates curvature.*

---

## 1. The cube complex

Fix a single oriented 3-cube \(c\) of the cubic lattice.

Let \(E\) be its 12 oriented edges and \(F\) its 6 oriented faces.
Let \(d=\dim\mathfrak g\).

- Edge variables: \(X\in \mathbb R^{|E|d}\) (infinitesimal link motions).
- Face strains: \(A\in \mathbb R^{|F|d}\) (infinitesimal plaquette strains).

Define the linear edge-to-face operator
\[
D:\mathbb R^{|E|d}\to \mathbb R^{|F|d},\qquad A=DX,
\]
where each face component \(A_p\) is an oriented signed sum of its boundary edges.

Define the face-to-cube closure operator
\[
C:\mathbb R^{|F|d}\to \mathbb R^{d},
\qquad
C(A)=\sum_{p\subset \partial c}\sigma_{cp}\,A_p,
\]
with the standard sign pattern encoding the linearized Bianchi identity (outward normals):
\[
\sigma_{cp_x^+}=+1,\ \sigma_{cp_x^-}=-1,\quad
\sigma_{cp_y^+}=+1,\ \sigma_{cp_y^-}=-1,\quad
\sigma_{cp_z^+}=+1,\ \sigma_{cp_z^-}=-1.
\]

Then the discrete exactness identity holds:
\[
CD=0.
\]

---

## 2. Maxwell–Calladine index on the cube

Define:
- mechanisms \(m:=\dim\ker D\) (edge motions producing zero face strain),
- self-stresses \(s:=\dim\ker C^\top\) (face stress assignments doing zero work on all compatible strains).

Then the Maxwell–Calladine index reads:
\[
m-s=\dim\ker D-\dim\ker C^\top
=|E|d-\mathrm{rank}(D)-\mathrm{rank}(C).
\]

Interpretation: nontrivial \(\ker C^\top\) means the face constraints are redundant; redundancy reduces mechanisms and tends to increase rigidity.

---

## 3. Energy curvature from redundancy: a clean lemma

Let \(H:\mathbb R^{|F|d}\to\mathbb R^{|F|d}\) be symmetric positive semidefinite (block diagonal with \(d\times d\) blocks \(H_p\succeq 0\)). Define the pulled-back stiffness operator on edges
\[
K := D^\top H D \succeq 0.
\]

Assume that \(H\) is positive definite on the Bianchi-compatible strain subspace:
\[
\exists \alpha>0\quad
\langle A,HA\rangle\ \ge\ \alpha\|A\|^2
\quad\forall A\in\ker C.
\tag{H|kerC}
\]

> **Lemma (Bianchi–Calladine rigidity).**  
> Under (H|kerC),
> 1. \(\ker K=\ker D\).  
> 2. On \((\ker D)^\perp\), \(K\) has a spectral gap:
> \[
> \lambda_{\min}\!\left(K\big|_{(\ker D)^\perp}\right)
> \ \ge\
> \alpha\ \sigma_{\min}\!\left(D\big|_{(\ker D)^\perp}\right)^2\ >0.
> \]

*Proof.*  
(1) If \(X\in\ker D\), then \(KX=0\). Conversely, if \(KX=0\), then
\(\langle DX, H DX\rangle=0\). Since \(DX\in \mathrm{Ran}(D)\subseteq \ker C\) (because \(CD=0\)), (H|kerC) implies \(DX=0\), so \(X\in\ker D\).

(2) Let \(X\perp\ker D\). Then \(DX\neq 0\) and \(DX\in\ker C\). Hence
\[
\langle X,KX\rangle=\langle DX,H DX\rangle\ge \alpha\|DX\|^2
\ge \alpha\,\sigma_{\min}(D|_{(\ker D)^\perp})^2\,\|X\|^2,
\]
which gives the eigenvalue lower bound. \(\square\)

---

## 4. Why this viewpoint is useful for Yang–Mills

This lemma says: **curvature (energy Hessian) is not only local convexity of a face potential; it is also redundancy of constraints.**

In lattice gauge terms:
- The face variables \(A_p\) are not independent; they satisfy Bianchi.
- If the face energy is strictly convex on \(\ker C\), then the edge-energy Hessian is strictly coercive modulo gauge.

This is a rigidity-theoretic explanation of why “topological exactness” (\(d_2\circ d_1=0\)) can generate a uniform spectral floor for the pulled-back Hessian.

---

## 5. Assembly to the full lattice (sketch)

On a full lattice,
\[
\text{edges}\xrightarrow{d_1}\text{faces}\xrightarrow{d_2}\text{cubes}
\]
is a cochain complex with \(d_2d_1=0\). Replacing \((D,C)\) by \((d_1,d_2)\) yields a global analogue:
- self-stresses correspond to \(\ker d_2^\top\),
- mechanisms correspond to \(\ker d_1\),
- cohomology controls the index.

This is a natural bridge between:
- discrete Hodge theory (Maxwell operators),
- rigidity theory (Calladine index),
- and the project’s “Maxwell resolvent controls correlations” module.

---

## Source

This note is distilled from the cube-level Bianchi/Calladine sketch developed in this chat (not from a standalone project file).
