# Finite-Cutoff Mass Gap Window for \(SU(N)\) Lattice Yang–Mills (Convexity Route)

This note distills the strongest **rigorous core** present in the project:  
at **fixed lattice spacing** \(a>0\), sufficiently strong bare coupling forces the effective action to be uniformly convex (on horizontal directions), which implies a **spectral gap** for the Langevin generator via Bakry–Émery.

The mechanism is geometric: the **Haar Jacobian** in exponential coordinates contributes a strictly positive quadratic term.

---

## 1. Setup and conventions

Let \(\Lambda\subset\mathbb{Z}^4\) be a finite periodic hypercubic lattice with spacing \(a>0\).  
Let \(B\) be the set of oriented links (bonds). The configuration manifold is
\[
\mathcal{C}=SU(N)^{|B|}.
\]

### Inner product

Identify \(T_{U_b}SU(N)\simeq \mathfrak{su}(N)\) by left translation and use
\[
\langle X,Y\rangle=-\mathrm{Tr}(XY),
\qquad
\|X\|^2=-\mathrm{Tr}(X^2),
\quad X,Y\in\mathfrak{su}(N).
\]

### Action

Write the effective action as
\[
S_{\mathrm{eff}}(U)=\beta S_W(U)+S_{\mathrm{Haar}}(U),
\qquad
\beta=\frac{2N}{g^2}.
\]

We will only track constants conservatively; the main point is positivity.

---

## 2. Haar Jacobian produces a positive quadratic term (“Haar mass”)

Parametrize a link near the identity by
\[
U=\exp(X),\qquad X=agA\in\mathfrak{su}(N).
\]

The pullback of Haar measure under \(\exp\) has Jacobian
\[
J(X)=\det_{\mathfrak{g}}\!\left(\frac{\sinh(\mathrm{ad}_X/2)}{\mathrm{ad}_X/2}\right),
\]
and define
\[
S_{\mathrm{Haar}}(X)=-\log J(X).
\]

Using
\[
\log\Big(\frac{\sinh z}{z}\Big)=\frac{z^2}{6}+O(z^4),
\]
we obtain
\[
\log J(X)=\frac{1}{24}\mathrm{Tr}_{\mathfrak{g}}(\mathrm{ad}_X^2)+O(\|X\|^4),
\]
hence
\[
S_{\mathrm{Haar}}(X)= -\frac{1}{24}\mathrm{Tr}_{\mathfrak{g}}(\mathrm{ad}_X^2)+O(\|X\|^4).
\]

For the compact real form, \(\mathrm{ad}_X\) is skew-adjoint, so \(\mathrm{Tr}(\mathrm{ad}_X^2)\le 0\).
With the chosen normalization one has
\[
\mathrm{Tr}_{\mathfrak{g}}(\mathrm{ad}_X^2)= -2N\,\|X\|^2,
\]
so
\[
S_{\mathrm{Haar}}(X)=\frac{N}{12}\|X\|^2+O(\|X\|^4).
\]

Summing over links,
\[
S_{\mathrm{Haar}}(A)=\frac{N}{12}a^2g^2\sum_{b\in B}\|A_b\|^2 + O(a^4g^4\|A\|^4).
\]

If we package the quadratic term as
\[
S_{\mathrm{Haar}}^{(2)}(A)=\frac{c_0}{2}a^2g^2\sum_{b}\|A_b\|^2,
\]
then **with these conventions**
\[
c_0=\frac{N}{6},
\qquad
\mathrm{Hess}\,S_{\mathrm{Haar}}^{(2)}\succeq c_0 a^2 g^2\,I.
\]

---

## 3. Conservative Wilson Hessian bound

The Wilson plaquette term is
\[
S_W(U)=\sum_{p}\left(1-\frac{1}{N}\mathrm{Re}\,\mathrm{Tr}(U_p)\right),
\]
where \(U_p\) is the ordered product of the four links around plaquette \(p\).

For a single plaquette, consider a one-parameter variation on the four links
\[
V_i(\varepsilon)=\exp(\varepsilon X_i)V_i,\qquad X_i\in\mathfrak{su}(N),
\]
and write \(S_p(\varepsilon)=1-\frac{1}{N}\mathrm{Re\,Tr}(V_1(\varepsilon)\cdots V_4(\varepsilon))\).

A direct Taylor expansion of the product shows \(S_p''(0)\) contains:
- four “diagonal” terms involving \(X_i^2\),
- six “mixed” terms involving \(X_iX_j\), each with a factor \(2\).

Using von Neumann and Frobenius/trace Cauchy–Schwarz inequalities, one obtains the safe bound
\[
|S_p''(0)|
\;\le\;
\frac{1}{N}\left(\sum_{i=1}^4\|X_i\|\right)^2
\;\le\;
\frac{4}{N}\sum_{i=1}^4\|X_i\|^2.
\]

Thus, for the plaquette Hessian quadratic form,
\[
\big|\mathrm{Hess}\,S_p(X^{(p)},X^{(p)})\big|
\le \frac{4}{N}\|X^{(p)}\|^2.
\]

Now sum over plaquettes. In \(d=4\), each link belongs to \(2(d-1)=6\) plaquettes, hence
\[
\sum_{p}\|A^{(p)}\|^2
=\sum_{p}\sum_{b\in\partial p}\|A_b\|^2
\le 6\sum_{b}\|A_b\|^2
=6\|A\|^2.
\]

Therefore
\[
\big|\langle A,\mathrm{Hess}\,S_W(U)A\rangle\big|
\le C_V(N)\,\|A\|^2,
\qquad
C_V(N)=\frac{24}{N}.
\]

*(This constant is conservative; sharpening it is an obvious “technical improvement” task.)*

---

## 4. Finite-cutoff convexity window

Combine the positive Haar Hessian and the bounded Wilson Hessian:
\[
\langle A,\mathrm{Hess}_{\mathrm{hor}}\,S_{\mathrm{eff}}(U)\,A\rangle
\ge \left(c_0 a^2 g^2 - \beta C_V(N)\right)\|A\|^2.
\]

Insert \(\beta=2N/g^2\), \(c_0=N/6\), \(C_V(N)=24/N\):
\[
\rho_*(a)
:=c_0 a^2 g^2-\beta C_V(N)
=\frac{N}{6}a^2 g^2-\frac{48}{g^2}.
\]

A sufficient condition for strict convexity is \(\rho_*(a)>0\), i.e.
\[
\boxed{
g^4>\frac{288}{Na^2}.
}
\]

This provides a **finite-cutoff convexity window** (very strong coupling) in which the horizontal Hessian is uniformly bounded below.

---

## 5. Bakry–Émery \(\Rightarrow\) Poincaré \(\Rightarrow\) spectral gap

On a compact manifold, uniform convexity (on the relevant tangent subspace) yields a Bakry–Émery lower bound and hence a Poincaré inequality. In this window one obtains a **volume-uniform spectral gap** for the Langevin generator \(L\):
\[
\lambda_1(-L)\ge \rho_*(a).
\]

This is the cleanest “convexity \(\Rightarrow\) gap” pipeline in the notes.

---

## 6. One-step RG-stable subwindow (block convexity bound)

Apply the block convexity inequality from `01_block_convexity_engine.md`.

Let the horizontal degrees of freedom be split into coarse \((x)\) and fine \((y)\) variables.  
Assume the full Hessian satisfies \(H_{\mathrm{hor}}\succeq \rho_*(a)I\), so \(\alpha=\gamma=\rho_*(a)\).

Take the mixed block size as
\[
M\lesssim \|\mathrm{Hess}(\beta S_W)\|_{\mathrm{op}} \le \beta C_V(N)=\frac{48}{g^2}.
\]

Then the coarse action after integrating out \(y\) satisfies
\[
\nabla_x^2 S_{\mathrm{coarse}} \succeq \left(\rho_*(a)-\frac{M^2}{\rho_*(a)}\right)I.
\]

A sufficient condition for the RHS to be positive is \(\rho_*(a)>M\), i.e.
\[
c_0 a^2 g^2-\beta C_V(N)>\beta C_V(N)
\quad\Longleftrightarrow\quad
c_0 a^2 g^2>2\beta C_V(N).
\]

With the constants above this becomes
\[
\boxed{
g^4>\frac{576}{Na^2}.
}
\]

So there is a stricter **RG-stable strong-coupling subwindow** where at least one nontrivial blocking step preserves strict convexity.

---

## 7. Independent strong-coupling gap: transfer matrix route

Separately, in Hamiltonian/transfer-matrix language with anisotropic couplings and sufficiently small temporal coupling \(\beta_t\), strong-coupling character expansions yield exponential decay of Wilson-loop correlators and hence a transfer matrix gap:
\[
\frac{\lambda_1}{\lambda_0}\le (c\beta_t)^L<1
\quad\Rightarrow\quad
\Delta=E_1-E_0\ge \frac{L}{a_t}|\log(c\beta_t)|>0.
\]

This is conceptually independent from the convexity/Bakry–Émery route and can serve as a cross-check in overlapping regions.

---

## 8. What this does **not** prove

All statements above are **finite-cutoff**: they hold at fixed \(a>0\) under strong-coupling inequalities.

They do **not** establish the 4D continuum Yang–Mills mass gap, because:
- along an asymptotically free continuum trajectory \(g(a)\to 0\) as \(a\to 0\),
- the Haar quadratic term scales like \(a^2 g(a)^2\to 0\),
- while the Wilson term carries \(\beta\sim 1/g^2\to\infty\).

So a different “spark” is needed in the continuum.

