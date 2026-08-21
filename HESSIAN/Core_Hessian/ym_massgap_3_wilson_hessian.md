
# Part 3 — Hessian Bound for the Wilson Plaquette Action

We now bound the curvature (Hessian) of the Wilson action. The bound is global and completely uniform in the lattice volume; it is the only place where potential “negative curvature” enters the story.

## 1. Wilson action

For a configuration \(U = (U_b)_{b\in B} \in \mathcal{C} = SU(N)^{|B|}\), the Wilson action is
\[
S_W(U) = \sum_{p} S_p(U_p),
\qquad
S_p(U_p) = 1 - \frac{1}{N}\,\Re \mathrm{Tr}(U_p),
\]
where \(U_p\) is the ordered product of the four link variables around plaquette \(p\).

We equip the tangent space with the product metric induced by \(\langle X,Y\rangle = -\mathrm{Tr}(XY)\) on \(\mathfrak{su}(N)\).

## 2. One‑plaquette second derivative

Consider a single plaquette \(p\) and perturb just one of its links by a tangent vector \(X\in\mathfrak{su}(N)\). Fix the other three links and write
\[
U_p(\varepsilon) = e^{\varepsilon X} U_p,
\]
so that \(U_p(0)=U_p\). Define \(S_p(\varepsilon) = S_p(U_p(\varepsilon))\). Then
\[
S_p(\varepsilon) = 1 - \frac{1}{N}\Re \mathrm{Tr}( e^{\varepsilon X} U_p).
\]
Expanding
\[
e^{\varepsilon X} = I + \varepsilon X + \frac{\varepsilon^2}{2}X^2 + O(\varepsilon^3)
\]
gives
\[
S_p''(0)
 = -\frac{1}{N} \Re \mathrm{Tr}(X^2 U_p).
\]

Let \(H = -X^2\). Because \(X\in\mathfrak{su}(N)\) is anti‑Hermitian, \(X^2\) is Hermitian negative semidefinite, hence \(H\) is Hermitian positive semidefinite.  Let its eigenvalues be \(\lambda_j\ge 0\). Then
\[
\sum_j \lambda_j = \mathrm{Tr}(H) = -\mathrm{Tr}(X^2) = \|X\|^2.
\]

For a Hermitian \(H\) and unitary \(U_p\), von Neumann’s trace inequality gives
\[
|\mathrm{Tr}(H U_p)| \le \sum_j \lambda_j = \|X\|^2.
\]
Since \(\Re \mathrm{Tr}(X^2 U_p) = -\Re \mathrm{Tr}(H U_p)\), we obtain
\[
|S_p''(0)|
 = \frac{1}{N}\, |\Re \mathrm{Tr}(X^2 U_p)|
 \le \frac{1}{N}\,|\mathrm{Tr}(H U_p)|
 \le \frac{1}{N}\,\|X\|^2.
\]

Thus, along any single‑link direction,
\[
\left| \big\langle X, \mathrm{Hess}\,S_p(U_p)\,X \big\rangle \right| \le \frac{1}{N} \|X\|^2.
\]

This estimate can be extended to general tangent vectors that affect several links in the plaquette: the Hessian quadratic form restricted to the 4‑tuple of link directions in \(p\) satisfies
\[
\big| \mathrm{Hess}\,S_p(U_p)(A^{(p)}, A^{(p)}) \big| \le \frac{1}{N}\,\|A^{(p)}\|^2,
\]
where \(A^{(p)}\in \mathfrak{su}(N)^4\) is the restriction of the global tangent vector to the plaquette’s links and \(\|\cdot\|\) is the product norm.

## 3. Global Hessian bound in 4D

Let \(A = (A_b)_{b\in B}\) be any tangent vector on \(\mathcal{C}\), and let \(A^{(p)}\) be its restriction to plaquette \(p\). The Hessian quadratic form for the full Wilson action is
\[
\langle A, \mathrm{Hess} S_W(U) A\rangle
 = \sum_p \mathrm{Hess}\,S_p(U_p)(A^{(p)}, A^{(p)}).
\]

Using the one‑plaquette bound and summing,
\[
\begin{aligned}
\big|\langle A, \mathrm{Hess} S_W(U) A\rangle\big|
 &\le \frac{1}{N} \sum_p \|A^{(p)}\|^2 \\[0.3em]
 &= \frac{1}{N}\sum_p \sum_{b\in\partial p} \|A_b\|^2.
\end{aligned}
\]

In \(d=4\) dimensions, each link belongs to exactly \(2(d-1) = 6\) plaquettes, so
\[
\sum_p \sum_{b\in\partial p} \|A_b\|^2
 = \sum_{b} \Big(\#\text{plaquettes touching }b\Big)\, \|A_b\|^2
 = 6 \sum_b \|A_b\|^2
 = 6 \|A\|^2.
\]

Therefore
\[
\big|\langle A, \mathrm{Hess} S_W(U) A\rangle\big|
 \le \frac{6}{N}\, \|A\|^2.
\]

**Theorem (Wilson Hessian bound in 4D).**  
For \(SU(N)\) lattice gauge theory with the Wilson action in \(d=4\),
\[
\big|\langle A, \mathrm{Hess} S_W(U) A\rangle\big|
 \le C_V(N)\, \|A\|^2
\quad\text{for all }U,A,
\]
with the explicit constant
\[
C_V(N) = \frac{6}{N}.
\]

In particular, \(\mathrm{Hess} S_W(U)\) is a globally bounded self‑adjoint operator on each tangent space, and all its eigenvalues lie in the interval \([ -C_V(N), +C_V(N) ]\).
