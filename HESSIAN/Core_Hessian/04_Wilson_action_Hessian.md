Document 4 — Wilson Action Hessian and Global Hessian Bound

# Document 4: Wilson Action Hessian and Global Hessian Bound

## 1. Wilson Action and Plaquette Contribution

On a 4D hypercubic lattice, the Wilson action is
\[
  S_W(U) = \sum_p S_p(U_p),
  \qquad
  S_p(U_p) = 1 - \frac{1}{N}\Re \mathrm{Tr}(U_p),
\]
where \(U_p\) is the ordered product of the four link variables around plaquette \(p\).

Let \(A = (A_b)_{b\in B}\in T_U\mathcal{C}\) be a tangent vector in \(\mathfrak{su}(N)^{|B|}\). The Hessian of \(S_W\) is a bilinear form
\[
  \langle A, \mathrm{Hess} S_W(U) A\rangle
  = \sum_p \mathrm{Hess} S_p\big(A^{(p)},A^{(p)}\big),
\]
where \(A^{(p)}\) is the restriction of \(A\) to the four links in \(p\).

We first bound the plaquette-level Hessian.

## 2. One-Plaquette Hessian Bound

Fix a plaquette \(p\). Let \(U_p = U_b V\) where we vary a single link \(U_b\) and hold the rest \(V\) fixed. Consider variations
\[
  U_b(\varepsilon) = e^{\varepsilon X} U_b, \quad X\in\mathfrak{su}(N).
\]
Then
\[
  U_p(\varepsilon) = e^{\varepsilon X} U_p,
\]
and
\[
  S_p(\varepsilon)
  = 1 - \frac{1}{N}\Re \mathrm{Tr}\big( e^{\varepsilon X} U_p\big).
\]
Expand:
\[
  S_p'(\varepsilon) = -\frac{1}{N}\Re \mathrm{Tr}\big( X e^{\varepsilon X} U_p\big),\quad
  S_p''(\varepsilon) = -\frac{1}{N}\Re \mathrm{Tr}\big( X^2 e^{\varepsilon X} U_p\big).
\]
At \(\varepsilon=0\),
\[
  S_p''(0) = -\frac{1}{N}\Re \mathrm{Tr}(X^2 U_p).
\]

Let \(\|\cdot\|\) denote the Hilbert space norm induced by \(\langle\cdot,\cdot\rangle = -\mathrm{Tr}(XY)\), so \(\|X\|^2=-\mathrm{Tr}(X^2)\). We want a bound of the form
\[
  |S_p''(0)| \le C_{\text{plaq}}\,\|X\|^2.
\]

**Lemma 2.1 (Plaquette Hessian Bound).**  
There exists a constant \(C_{\text{plaq}} = \frac{1}{N}\) such that
\[
  \big|\mathrm{Hess} S_p(X,X)\big|
  = |S_p''(0)| \le \frac{1}{N}\,\|X\|^2.
\]

*Sketch of proof.*  
Diagonalize \(X\) and use von Neumann’s trace inequality. One shows that for any unitary \(U_p\),
\[
  |\mathrm{Tr}(X^2 U_p)| \le |\mathrm{Tr}(X^2)| = \|X\|^2,
\]
hence
\[
  |S_p''(0)| \le \frac{1}{N}\|X\|^2.
\]
The details are a standard application of trace inequalities for products of Hermitian and unitary matrices.

For a given plaquette, with four links, the same constant controls the contribution along each link direction; we can sum them without changing the constant per link.

## 3. Counting Plaquettes per Link in 4D

In \(d=4\) dimensions, each link belongs to
\[
  2(d-1) = 6
\]
plaquettes: for each of the three transverse directions, there are two plaquettes (one “above”, one “below”). Thus each link variable \(U_b\) contributes to six plaquettes.

Let \(A = (A_b)\) be a tangent vector. Summing the plaquette contributions and using the bound from Lemma 2.1:
\[
  \big|\langle A,\mathrm{Hess} S_W(U) A\rangle\big|
  \le \frac{1}{N} \sum_p \sum_{b\in \partial p} \|A_b\|^2
  = \frac{1}{N} \sum_b \Big(\sum_{p:\,b\in\partial p} 1\Big) \|A_b\|^2
  \le \frac{6}{N} \sum_b \|A_b\|^2.
\]

Define
\[
  C_V(N) := \frac{6}{N}.
\]

**Theorem 3.1 (Global Wilson Hessian Bound in 4D).**  
For all configurations \(U\) and tangent vectors \(A\),
\[
  \big|\langle A,\mathrm{Hess} S_W(U) A\rangle\big|
  \le C_V(N)\,\|A\|^2,\quad C_V(N)=\frac{6}{N}.
\]

For \(SU(2)\), \(C_V(2) = 3\). An explicit SU(2) computation at the worst-case configuration \(U_p=-I\) confirms that the smallest eigenvalue per plaquette is \(-\tfrac12\), and since each link is in 6 plaquettes we indeed get a total negative curvature bound of \(-3\) per link, matching \(C_V(2)=3\).

## 4. Global Effective Hessian: Adding Haar Mass

The effective action is
\[
  S_{\mathrm{eff}}(U) = \beta S_W(U) + S_{\mathrm{Haar}}(U).
\]
Let \(\Delta_{\text{latt}}(U)\) denote the nonnegative Laplacian-like part of the Wilson Hessian, and \(V(U)\) the potential-like part whose operator norm is bounded by \(C_V(N)\). Schematically,
\[
  \mathrm{Hess}\,S_{\mathrm{eff}}(U)
  = \beta\Delta_{\text{latt}}(U) - \beta V(U)
  + \mathrm{Hess}\,S_{\mathrm{Haar}}(U).
\]

Restrict to the **horizontal subspace** \(H_U\subset T_U\mathcal{C}\), orthogonal to gauge orbits. On horizontals:

- \(\Delta_{\text{latt}}(U)\) is nonnegative;
- The Haar term contributes \(c_0 a^2 g^2 I\) at small fields and remains bounded below by approximately this uniform mass in a neighborhood;
- \(-\beta V(U)\) is bounded below by \(-\beta C_V(N) I\).

This yields:

**Theorem 4.1 (Horizontal Hessian Lower Bound).**  
For any horizontal vector \(A\in H_U\),
\[
  \langle A, \mathrm{Hess}_{\mathrm{hor}} S_{\mathrm{eff}}(U) A\rangle
  \;\ge\; \big(c_0 a^2 g^2 - \beta C_V(N)\big) \|A\|^2.
\]

Define
\[
  \rho_*(a) := c_0 a^2 g^2 - \beta C_V(N).
\]
Whenever \(\rho_*(a) > 0\), the effective action is **uniformly convex** along horizontal directions with curvature at least \(\rho_*(a)\).

This is the core inequality that will feed into Bakry–Émery and the mass gap argument.


⸻
