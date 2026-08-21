# Bianchi Constraints as Maxwell–Calladine Rigidity
*(a redundancy-driven spectral gap mechanism for lattice gauge Hessians)*

## 1. Executive statement

On a cubic lattice, the linearized plaquette constraints and the cube-level Bianchi identities form a **cochain complex**
\[
\mathbb R^{E d}\ \xrightarrow{\ D\ }\ \mathbb R^{F d}\ \xrightarrow{\ C\ }\ \mathbb R^{C d},
\qquad
C D = 0.
\]
If the plaquette-level Hessian is uniformly positive on **Bianchi-compatible strains** \(\ker C\), then the induced edge-level stiffness operator
\[
K := D^\top H D
\]
has a **uniform spectral gap modulo gauge**, with constants independent of volume. The mechanism is purely **constraint redundancy** (Maxwell–Calladine style), not global convexity.

This document is a clean algebraic packaging of that argument.

---

## 2. Lattice cochain operators

Let \(\Lambda\subset\mathbb Z^3\) be a finite cubic box (periodic or with boundary conditions that make the incidence operators well-defined).

- \(E(\Lambda)\): oriented edges (links),
- \(F(\Lambda)\): oriented faces (plaquettes),
- \(C(\Lambda)\): oriented cubes (3-cells).

Fix an internal dimension \(d\) (for \(G=\mathrm{SU}(2)\) one can think \(d=\dim\mathfrak{su}(2)=3\); the argument below is linear-algebraic and independent of the group).

### 2.1 Edge-to-face operator \(D\) (linearized plaquette strain)
Let \(X\in \mathbb R^{E d}\) assign to each oriented edge \(e\) a vector \(X_e\in\mathbb R^d\).

Define \(Y=DX\in\mathbb R^{F d}\) by
\[
(DX)_p := \sum_{e\in\partial p} \sigma_{p,e}\, X_e,
\]
where \(\sigma_{p,e}\in\{\pm 1\}\) is the oriented incidence sign of edge \(e\) in the oriented boundary \(\partial p\).

Interpretation: \(DX\) is the linearized plaquette holonomy / “curl of the link field.”

### 2.2 Face-to-cube operator \(C\) (linearized Bianchi closure)
Let \(Y\in\mathbb R^{F d}\) assign a vector to each oriented plaquette.

Define \(Z=CY\in\mathbb R^{C d}\) by
\[
(CY)_c := \sum_{p\in\partial c} \sigma_{c,p}\, Y_p,
\]
with \(\sigma_{c,p}\in\{\pm 1\}\) the oriented incidence sign of face \(p\) in the oriented boundary \(\partial c\).

Interpretation: \(CY\) is “curl of curl”; in a smooth limit it becomes a discrete Bianchi divergence.

### 2.3 Exactness identity \(CD=0\)
For any \(X\),
\[
C(DX)=0.
\]

**Proof.** Each edge of a cube appears exactly twice with opposite orientation in \(\partial(\partial c)\), so the signed sum cancels (boundary of a boundary is zero). \(\square\)

Thus
\[
\operatorname{Ran}(D)\subset \ker C.
\]

---

## 3. Quadratic energy and stiffness operator

Let \(H\) be a symmetric operator on \(\mathbb R^{F d}\) representing the **plaquette-level Hessian** (or a local curvature matrix) of an action in a small-field regime.

Define the quadratic energy on edge variables:
\[
\mathcal Q(X)
:=\frac12\langle DX,\,H\,DX\rangle.
\]
The induced stiffness operator is
\[
K := D^\top H D,
\qquad
\mathcal Q(X)=\frac12\langle X, K X\rangle.
\]

### Assumption (UBP): uniform Bianchi-positive curvature
There exists \(\alpha>0\) such that
\[
\boxed{
\langle Y,HY\rangle \ge \alpha\|Y\|^2
\qquad \forall Y\in\ker C.
}
\tag{UBP}
\]
Because \(\operatorname{Ran}(D)\subset \ker C\), this implies
\[
\langle DX,H DX\rangle \ge \alpha \|DX\|^2.
\]

---

## 4. Maxwell–Calladine-type rigidity lemma

### Lemma 4.1 (Kernel identification)
Assume **(UBP)**. Then
\[
\boxed{
\ker K = \ker D.
}
\]

**Proof.**
If \(X\in\ker D\), then \(DX=0\) so \(KX=D^\top H D X=0\).

Conversely, if \(KX=0\) then
\[
0 = \langle X,KX\rangle = \langle DX,H DX\rangle.
\]
But \(DX\in\ker C\), and by (UBP),
\[
\langle DX,H DX\rangle \ge \alpha \|DX\|^2,
\]
so \(\|DX\|=0\), i.e. \(DX=0\). \(\square\)

Interpretation: the only zero-energy modes are **mechanisms** (exact edge fields with zero plaquette strain), matching the Maxwell–Calladine “mechanism vs self-stress” dichotomy.

---

## 5. Uniform spectral gap modulo gauge

The spectral gap statement needs one more ingredient: a uniform lower bound on the smallest singular value of \(D\) away from \(\ker D\). This is where gauge fixing or boundary conditions enter.

### 5.1 Gauge subspace
In gauge theory, \(\ker D\) contains gauge directions (exact 0-cochains), i.e. the infinitesimal gauge orbit. Let
\[
\mathcal G := \ker D
\]
and define the physical subspace \(\mathcal G^\perp\) by any fixed orthogonal choice (e.g. via gauge fixing).

### Proposition 5.1 (Coercivity on \(\mathcal G^\perp\))
Assume:

1. (UBP) holds with constant \(\alpha>0\),
2. there exists \(\sigma_*>0\), independent of volume, such that
\[
\|DX\| \ge \sigma_* \|X\|
\qquad\forall X\in \mathcal G^\perp.
\tag{SV}
\]

Then
\[
\boxed{
\langle X, K X\rangle \ge \alpha\,\sigma_*^2\,\|X\|^2
\qquad\forall X\in \mathcal G^\perp,
}
\]
and hence the nonzero spectrum of \(K\) has a uniform lower bound \(\ge \alpha\sigma_*^2\).

**Proof.**
For \(X\in\mathcal G^\perp\),
\[
\langle X,KX\rangle = \langle DX,H DX\rangle \ge \alpha \|DX\|^2 \ge \alpha\sigma_*^2\|X\|^2.
\quad\square
\]

### 5.2 Tree gauge gives (SV) with volume-independent constants (template)
Let \(T\subset E(\Lambda)\) be a spanning tree and impose the **tree gauge**
\[
X_e=0 \qquad \forall e\in T.
\]
Denote by \(\mathcal H_T\) the resulting linear subspace. Then \(\ker(D|_{\mathcal H_T})=\{0\}\) and (SV) holds on \(\mathcal H_T\) with a smallest singular value depending only on lattice coordination, not on \(|\Lambda|\).

*(This is a standard discrete Hodge/gauge-fixing fact: the tree removes all exact 0-cochains and kills global mechanisms.)*

---

## 6. From stiffness to functional inequalities (where this plugs in)

Once the reduced stiffness operator is uniformly coercive, one can feed it into the analytic pipeline:

1. **Local Poincaré/LSI on a compact set**: coercive Hessian bounds control the measure locally.
2. **Lyapunov drift outside**: a Foster–Lyapunov function \(W(X)=\|X\|^2\) yields negative drift for large \(\|X\|\) because the action is (quadratically) stiff at infinity.
3. **Gluing**: local + drift gives a **global** Poincaré inequality with constants independent of \(|\Lambda|\).

In other words, the Bianchi–rigidity mechanism supplies the *geometric coercivity* input that replaces any need for global Bakry–Émery curvature.

---

## 7. Why this is potentially new (as a structural idea)

The novelty is not “there is a cochain complex” (that’s topology 101). The novelty is:

- using **cube-level Bianchi redundancy** as an explicit **Maxwell–Calladine self-stress** mechanism,
- to produce a **volume-uniform** stiffness gap *modulo gauge*,
- with no appeal to global convexity of the full action.

That creates a bridge between:
- rigidity theory of mechanical networks,
- discrete Hodge theory (gauge fixing),
- and mass-gap / Poincaré constants in lattice gauge measures.

It is a nice example of a general principle: *redundant constraints can act like curvature.*

