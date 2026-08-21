# Project Highlight C: Haar geometry, Ricci curvature, and the “Haar mass” convexity constant

This document isolates the piece of geometry that supplies a **volume-uniform on-site convexity floor**: the contribution of the product Haar measure when viewed in exponential coordinates.

The two key takeaways are:

1. For a compact semisimple Lie group \(G\) with bi-invariant metric,
   \[
   \mathrm{Ric}_G = \kappa_G\,g_G,\qquad \kappa_G>0,
   \]
   and the same \(\kappa_G\) holds on the product manifold \(M_\Lambda=G^{E(\Lambda)}\) uniformly in \(|\Lambda|\).

2. In exponential coordinates \(U=\exp X\) near the identity,
   the Haar volume density has expansion
   \[
   J(X)=1-\frac16\mathrm{Ric}_G(X,X)+O(|X|^3),
   \]
   so the “Haar potential”
   \[
   S_H(X):=-\log J(X)
   \]
   satisfies
   \[
   \nabla^2 S_H(0)=\frac13\,\mathrm{Ric}_G.
   \]
   This gives a **uniform positive Hessian contribution** per link.

For \(G=\mathrm{SU}(3)\) in the normalization \(\langle X,Y\rangle=-\mathrm{Tr}(XY)\), one gets
\[
\kappa_G=\frac32,\qquad c_H:=\frac{\kappa_G}{3}=\frac12,\qquad \frac{c_H}{2}=\frac14.
\]

---

## C.1. Bi-invariant metric on a compact semisimple Lie group

Let \(G\) be compact and semisimple, with Lie algebra \(\mathfrak g\).  
Fix an \(\mathrm{Ad}\)-invariant inner product \(\langle\cdot,\cdot\rangle\) on \(\mathfrak g\), and let \(g_G\) be the corresponding bi-invariant Riemannian metric on \(G\).

---

## C.2. Curvature and Ricci in Lie algebra terms

For a bi-invariant metric, the Levi–Civita connection on left-invariant vector fields is
\[
\nabla_X Y = \frac12[X,Y],
\]
and the curvature operator is
\[
R(X,Y)Z = -\frac14[[X,Y],Z].
\]

Let \(\{E_i\}_{i=1}^m\) be an orthonormal basis of \((\mathfrak g,\langle\cdot,\cdot\rangle)\), \(m=\dim\mathfrak g\).  
The Ricci tensor is the trace of curvature:
\[
\mathrm{Ric}(X,Y)=\sum_{i=1}^m \langle R(E_i,X)Y,\ E_i\rangle.
\]

A standard computation using \(\mathrm{Ad}\)-invariance gives
\[
\mathrm{Ric}(X,Y)=\frac14\sum_{i=1}^m \langle [E_i,X],[E_i,Y]\rangle.
\]

Introduce the Killing form \(B(X,Y)=\mathrm{tr}(\mathrm{ad}_X\mathrm{ad}_Y)\).  
Since \(\mathrm{ad}_X\) is skew-adjoint under an \(\mathrm{Ad}\)-invariant inner product, one has
\[
B(X,Y)=-\sum_{i=1}^m \langle [X,E_i],[Y,E_i]\rangle.
\]
Comparing yields the clean identity:
\[
\boxed{\mathrm{Ric}(X,Y)=-\frac14\,B(X,Y).}
\]

---

## C.3. Einstein constant and normalization map

If \(\langle\cdot,\cdot\rangle\) is proportional to \(-B\), say
\[
\langle X,Y\rangle = -c\,B(X,Y),\qquad c>0,
\]
then
\[
\mathrm{Ric}(X,Y)=\frac{1}{4c}\,\langle X,Y\rangle.
\]
Thus \((G,g_G)\) is Einstein:
\[
\boxed{\mathrm{Ric}_G=\kappa_G\,g_G,\qquad \kappa_G=\frac{1}{4c}.}
\]

### Scaling rule
If the inner product is rescaled by a factor \(\lambda>0\),
\[
\langle\cdot,\cdot\rangle'=\lambda\langle\cdot,\cdot\rangle,
\]
then the Ricci constant rescales as
\[
\kappa_G'=\frac{\kappa_G}{\lambda}.
\]
(Geometrically: scaling the metric by \(\lambda\) scales curvature by \(1/\lambda\).)

---

## C.4. Product geometry on \(M_\Lambda=G^{E(\Lambda)}\)

Let \(n:=|E(\Lambda)|\) and form the product manifold
\[
M_\Lambda = \underbrace{G\times\cdots\times G}_{n\ \text{times}}
\]
with product metric \(g_\Lambda=\bigoplus_{e\in E(\Lambda)}g_G\).

The Levi–Civita connection splits by factors, and so do curvature and Ricci. In particular,
\[
\boxed{\mathrm{Ric}_{g_\Lambda}=\kappa_G\,g_\Lambda,}
\]
with the same \(\kappa_G\) as on \(G\).  
This is the first “volume-uniformity miracle”: \(\kappa_G\) depends only on \(G\) and metric normalization, not on \(\Lambda\).

---

## C.5. Haar (Riemannian) volume and the Haar potential in exponential coordinates

For a bi-invariant metric, the Riemannian volume measure on \(G\) is Haar (unique up to normalization).  
Fix the normalized Haar probability on \(G\). Then the Riemannian volume on the product manifold is the product Haar measure:
\[
d\mathrm{vol}_{g_\Lambda}(U)=\prod_{e\in E(\Lambda)} d\mathrm{Haar}_G(U_e).
\]

### Exponential coordinates and Jacobian
Fix normal coordinates at the identity: \(U=\exp X\), \(X\in\mathfrak g\).  
Let \(J(X)\) denote the Jacobian density of Haar volume in these coordinates:
\[
d\mathrm{Haar}_G(\exp X)=J(X)\,dX.
\]

A standard normal-coordinate expansion gives
\[
J(X)=1-\frac16\,\mathrm{Ric}_G(X,X)+O(|X|^3)\qquad (|X|\to 0).
\]
Define the Haar potential
\[
S_H(X):=-\log J(X).
\]
Then
\[
S_H(X)=\frac16\,\mathrm{Ric}_G(X,X)+O(|X|^3),
\]
and differentiating twice at \(0\) yields the key identity
\[
\boxed{\nabla^2 S_H(0)=\frac13\,\mathrm{Ric}_G.}
\]

If \(\mathrm{Ric}_G\ge \kappa_G g_G\), then
\[
\nabla^2 S_H(0)\ge \frac{\kappa_G}{3}\,I.
\]
It is convenient to set
\[
c_H:=\frac{\kappa_G}{3},
\]
so that \(\nabla^2 S_H(0)\ge c_H\,I\).

### Local uniformity on a small ball
By continuity of \(\nabla^2 S_H\), there exists \(r_0>0\) (depending only on \(G\) and the chosen metric) such that
\[
\|X\|\le r_0\quad\Longrightarrow\quad \nabla^2 S_H(X)\succeq \frac{c_H}{2}\,I.
\]
This is the form used downstream: the Haar contribution is uniformly coercive on a canonical region \(K_\Lambda\) defined as a small ball.

---

## C.6. Specialization to \(G=\mathrm{SU}(N)\) and explicit constants

Take \(G=\mathrm{SU}(N)\).  
Let \(\langle\cdot,\cdot\rangle_\lambda\) be the standard lattice normalization used in the project:
\[
\langle X,Y\rangle_\lambda := \lambda\,\bigl(-\mathrm{Tr}(XY)\bigr),
\qquad X,Y\in\mathfrak{su}(N)\ \text{(anti-Hermitian)}.
\]
The Killing form on \(\mathfrak{su}(N)\) is
\[
B(X,Y)=2N\,\mathrm{Tr}(XY),
\]
so \(-\mathrm{Tr}(XY)=\frac{1}{2N}(-B(X,Y))\). Hence
\[
\langle X,Y\rangle_\lambda = \frac{\lambda}{2N}(-B(X,Y)),
\]
so \(c=\lambda/(2N)\) in the Einstein formula, and therefore
\[
\boxed{\kappa_G=\frac{1}{4c}=\frac{N}{2\lambda}.}
\]

Consequently,
\[
c_H=\frac{\kappa_G}{3}=\frac{N}{6\lambda},
\qquad
\frac{c_H}{2}=\frac{N}{12\lambda}.
\]

### SU(3) in the \(\lambda=1\) normalization
For \(N=3\), \(\lambda=1\):
\[
\kappa_G=\frac32,\qquad c_H=\frac12,\qquad \frac{c_H}{2}=\frac14.
\]

This is exactly the numerical Haar add-on used in the project’s SU(3) ledger.

---

## C.7. Why this matters (one sentence)

The Wilson part contributes \(\frac{\beta}{N}d_1^\*d_1\), whose smallest nonzero eigenvalue collapses with volume on large tori; the Haar mass term contributes a **uniform diagonal floor** \(\frac{c_H}{2}I\), preventing that collapse on the horizontal sector and enabling uniform exponential clustering.

