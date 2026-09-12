# Analytic proof of the “affine Laplacian law” for 4D SU(2) plaquette defect

This note proves (under the same normalization used in the simulation code) an *exact* identity for the configuration-space Laplace--Beltrami operator acting on the mean plaquette defect.

---

## 1. Definitions (matching the code)

- Gauge group: \(G=\mathrm{SU}(2)\), represented as unit quaternions \(q=(w,x,y,z)\in S^3\subset\mathbb R^4\).
- Link variables: \(U_{x,\mu}\in \mathrm{SU}(2)\).
- Oriented plaquette:
\[
U_{x,\mu\nu}
:= U_{x,\mu}\,U_{x+\hat\mu,\nu}\,U_{x+\hat\nu,\mu}^{-1}\,U_{x,\nu}^{-1}.
\]
- Fundamental “trace component” (the code uses the quaternion scalar part):
\[
w(g)=\tfrac12\operatorname{Re}\operatorname{Tr}(g)\in[-1,1].
\]
- Plaquette defect:
\[
B_{x,\mu\nu}:=1-w\!\left(U_{x,\mu\nu}\right).
\]
- Mean plaquette defect:
\[
B_{\mathrm{avg}}
:=\frac{1}{N_p}\sum_{x}\sum_{\mu<\nu} B_{x,\mu\nu}.
\]
- The tracked observable in the project:
\[
\bar V := 1 + B_{\mathrm{avg}}.
\]

---

## 2. The Laplacian normalization induced by the code

The simulation perturbs each link by left-multiplication using the group exponential in axis-angle coordinates
\[
\exp(v)=\big(\cos\|v\|,\; \tfrac{\sin\|v\|}{\|v\|}\,v\big), \qquad v\in\mathbb R^3,
\]
and uses *Gaussian* tangent directions \(v=\varepsilon\,\Xi\) with \(\Xi\sim \mathcal N(0,I_3)\) (per link).

In the small-\(\varepsilon\) limit, the Monte Carlo estimator
\[
\mathbb E_\Xi\frac{f\!\left(U\exp(\varepsilon\Xi)\right)+f\!\left(U\exp(-\varepsilon\Xi)\right)-2f(U)}{\varepsilon^2}
\]
converges to the Laplace--Beltrami operator \(\Delta_G f(U)\) for the bi-invariant metric in which the coordinates \(v\in\mathbb R^3\) at the identity are orthonormal.

We will work with **this** \(\Delta_G\). (Changing the distribution of \(\Xi\) rescales the operator.)

---

## 3. SU(2) class functions and eigenvalues

Every conjugacy class in SU(2) can be parametrized by an angle \(\theta\in[0,\pi]\) via
\[
g \sim \begin{pmatrix}e^{i\theta} & 0\\ 0 & e^{-i\theta}\end{pmatrix},
\qquad\text{so}\qquad
w(g)=\cos\theta.
\]

For a class function \(f(\theta)\), the SU(2) Laplace--Beltrami operator for the round \(S^3\) metric takes the radial form
\[
(\Delta_G f)(\theta)=f''(\theta)+2\cot\theta\,f'(\theta).
\]

The irreducible characters \(\chi_j(\theta)\) (spin \(j\in\{0,\tfrac12,1,\dots\}\)) are
\[
\chi_j(\theta)=\frac{\sin((2j+1)\theta)}{\sin\theta},
\]
and satisfy the eigenvalue equation
\[
\Delta_G\chi_j = -4\,j(j+1)\,\chi_j.
\]

In particular, for the fundamental representation \(j=\tfrac12\),
\[
\chi_{1/2}(\theta)=2\cos\theta,
\qquad
\Delta_G\chi_{1/2}=-3\,\chi_{1/2}.
\]
Therefore
\[
\boxed{\Delta_G w = -3\,w.}
\]

Equivalently, for the one-link defect \(B(g):=1-w(g)\),
\[
\boxed{\Delta_G B = 3 - 3B.}
\]

*Quick sanity check (direct computation).*  
Let \(w(\theta)=\cos\theta\). Then \(w'=-\sin\theta\), \(w''=-\cos\theta\), so
\[
\Delta_G w = -\cos\theta + 2\cot\theta(-\sin\theta) = -\cos\theta -2\cos\theta = -3\cos\theta.
\]

---

## 4. A key invariance lemma (what makes the lattice proof painless)

Let \(\Delta_G\) be the bi-invariant Laplacian on SU(2). Then:

1. **Left/right translations commute with \(\Delta_G\):**
   \[
   \Delta_G(f\circ L_A)= (\Delta_G f)\circ L_A,\qquad
   \Delta_G(f\circ R_B)= (\Delta_G f)\circ R_B.
   \]
2. **Inversion is an isometry, so it also commutes:**
   \[
   \Delta_G(f\circ \mathrm{inv})=(\Delta_G f)\circ \mathrm{inv}.
   \]

Hence if \(f\) is an eigenfunction, then \(U\mapsto f(AUB)\) and \(U\mapsto f(AU^{-1}B)\) are eigenfunctions with the *same* eigenvalue.

---

## 5. Lattice theorem: affine law for a single plaquette

Fix a plaquette \(p=(x,\mu\nu)\), and consider its defect
\[
B_p(U)=1-w\!\left(U_p\right),
\qquad
U_p:=U_{x,\mu}U_{x+\hat\mu,\nu}U_{x+\hat\nu,\mu}^{-1}U_{x,\nu}^{-1}.
\]

Let \(\Delta_{x,\rho}\) denote the SU(2) Laplacian acting on the *single* link variable \(U_{x,\rho}\), and define the configuration Laplacian
\[
\Delta_{\mathrm{conf}} := \sum_{x,\rho}\Delta_{x,\rho}.
\]

### Claim.
For each plaquette defect \(B_p\),
\[
\boxed{\Delta_{\mathrm{conf}}\,B_p = 12 - 12\,B_p.}
\]

### Proof.
Only the four link variables appearing in \(U_p\) matter; for all other links, \(\Delta_{x,\rho}B_p=0\).

Now take one of the four links, call it \(U_\ell\). Holding the other three links fixed, the plaquette holonomy is either of the form
\[
U_p = A\,U_\ell\,B \quad\text{or}\quad U_p=A\,U_\ell^{-1}\,B
\]
for fixed \(A,B\in\mathrm{SU}(2)\).

Define \(f(g)=w(g)\). Section 3 showed \(\Delta_G f = -3f\). By the invariance lemma, \(U_\ell\mapsto f(AU_\ell B)\) and \(U_\ell\mapsto f(AU_\ell^{-1}B)\) are also eigenfunctions with eigenvalue \(-3\). Therefore
\[
\Delta_\ell\,w(U_p) = -3\,w(U_p).
\]
Since \(B_p=1-w(U_p)\), the constant drops out and
\[
\Delta_\ell B_p = -\Delta_\ell w(U_p) = 3\,w(U_p)=3(1-B_p)=3-3B_p.
\]

Summing over the **four** links in the plaquette boundary gives
\[
\Delta_{\mathrm{conf}}B_p = 4\,(3-3B_p)=12-12B_p,
\]
as claimed. \(\square\)

---

## 6. Corollary: affine law for the mean plaquette defect and for \(\bar V\)

By linearity,
\[
\Delta_{\mathrm{conf}}B_{\mathrm{avg}}
=\frac{1}{N_p}\sum_p\Delta_{\mathrm{conf}}B_p
=\frac{1}{N_p}\sum_p\left(12-12B_p\right)
=12-12B_{\mathrm{avg}}.
\]

Since \(\bar V=1+B_{\mathrm{avg}}\) and constants have zero Laplacian,
\[
\boxed{\Delta_{\mathrm{conf}}\bar V = 12 - 12 B_{\mathrm{avg}}.}
\]

This is exactly the empirical “affine Laplacian law” reported in the project.

---

## 7. Does the constant become \(D(D-1)\) in other lattice dimensions?

Not with these definitions.

The coefficient \(12\) comes from:
- \(3\): the SU(2) fundamental trace component \(w\) is a degree-1 spherical harmonic on \(S^3\), hence eigenvalue \(-3\) under the round Laplacian;
- \(4\): each plaquette has 4 boundary links.

So the constant is
\[
12 = 4\times 3,
\]
which does **not** depend on the lattice dimension \(D\) (spacetime dimension), provided “plaquette” still means a 4-link square and \(B_{\mathrm{avg}}\) is the average over plaquettes.

The appearance \(12=D(D-1)\) at \(D=4\) is therefore a numerical coincidence.

---

## 8. What *does* change the coefficient?

1. **Change the tangent-direction distribution.**  
   If you normalized each \(\Xi\) to unit length (uniform direction on \(S^2\)) then \(\mathbb E[\Xi_i^2]=1/3\) and the MC estimator rescales \(\Delta_G\) by \(1/3\), changing the “3” to “1”.

2. **Change the gauge group / representation.**  
   More generally, for a compact group \(G\), the bi-invariant Laplacian is (minus) the quadratic Casimir. Replacing the fundamental SU(2) character with another representation replaces the eigenvalue \(3\) accordingly.

---

## 9. Research-useful interpretation

The observable \(B_{\mathrm{avg}}\) is (up to a constant shift) an eigenfunction of the configuration Laplacian. That gives you a rare analytic handle on \(\Delta_{\mathrm{conf}}\bar V\) and turns the remaining difficulty for Lyapunov drift proofs into bounding the gradient pairing term \(\langle\nabla S,\nabla\bar V\rangle\).
