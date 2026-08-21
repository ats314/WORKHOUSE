# Lyapunov drift for $W=\exp\big(\eta\sum_{p\in P(\Lambda)}\Phi(\widetilde z_p)\big)$ on $G^{E(\Lambda)}$

This note carries out the drift computation for
\[
W(U)=e^{\eta V(U)},\qquad V(U)=\sum_{p\in P(\Lambda)}\Phi\big(\widetilde z_p(U)\big),\qquad \widetilde z_p(U)=\widetilde z\big(U_p(U)\big),
\]
with the globally smooth, conjugation-invariant plaquette proxy
\[
\widetilde z(g)=1-\frac1N\Re\operatorname{Tr}(g),\qquad g\in \mathrm{SU}(N).
\]
All constants are uniform in the lattice volume.

The drift identity reduces to a **single missing coercivity inequality**:
\[
\langle \nabla S_\Lambda,\nabla V\rangle\ \gtrsim\ \sum_{p}\widetilde z_p \ \text{outside a small set.}
\]

---

## 1. Configuration manifold, vector fields, generator

Let $\Lambda\subset \mathbb Z^4$ be finite. Let $G=\mathrm{SU}(N)$ with a fixed bi-invariant Riemannian metric induced by an $\mathrm{Ad}$-invariant inner product $\langle\cdot,\cdot\rangle_{\mathfrak g}$ on $\mathfrak g=\mathfrak{su}(N)$. The configuration manifold is
\[
M_\Lambda:=G^{E(\Lambda)}
\]
with product metric.

Fix an orthonormal basis $(T^a)_{a=1}^{\dim\mathfrak g}$ of $\mathfrak g$.
For each link $\ell\in E(\Lambda)$, define the right-invariant vector fields on the $\ell$-factor
\[
(X_\ell^a f)(U):=\left.\frac{d}{dt}\right|_{t=0} f(\dots, U_\ell e^{tT^a},\dots).
\]
The product Laplacian is
\[
\Delta_\Lambda f := \sum_{\ell\in E(\Lambda)}\sum_a (X_\ell^a)^2 f.
\]
Let the Gibbs measure be
\[
\mu_\Lambda(dU)=Z_\Lambda^{-1} e^{-S_\Lambda(U)}\,\mathrm{vol}(dU),
\]
with $S_\Lambda\in C^2(M_\Lambda)$.
The symmetric generator is
\[
L_\Lambda f := \Delta_\Lambda f-\langle \nabla S_\Lambda,\nabla f\rangle
=\sum_{\ell,a}\Big((X_\ell^a)^2 f-(X_\ell^a S_\Lambda)(X_\ell^a f)\Big).
\]
The carré du champ is
\[
\Gamma_\Lambda(f,g):=\sum_{\ell,a}(X_\ell^a f)(X_\ell^a g),\qquad \Gamma_\Lambda(f):=\Gamma_\Lambda(f,f)=|\nabla f|^2.
\]

---

## 2. Two chain rules

### Lemma 2.1 (composition)
For $\Psi\in C^2(\mathbb R)$ and $f\in C^2(M_\Lambda)$,
\[
L_\Lambda(\Psi(f))=\Psi'(f)\,L_\Lambda f+\Psi''(f)\,\Gamma_\Lambda(f).
\]

### Lemma 2.2 (exponential)
For $W=e^{\eta V}$,
\[
\boxed{\ \frac{L_\Lambda W}{W}=\eta\,L_\Lambda V+\eta^2\,\Gamma_\Lambda(V).\ }
\]

Both identities follow from direct differentiation using the explicit $X_\ell^a$ representation.

---

## 3. Global derivative bounds for the smooth proxy $\widetilde z$

Define
\[
\widetilde z(g)=1-\frac1N\Re\operatorname{Tr}(g),\qquad g\in G.
\]
Then $\widetilde z\in C^\infty(G)$, $0\le \widetilde z\le 2$, and $\widetilde z(e)=0$.

Because $G$ is compact and $\widetilde z$ has a nondegenerate minimum at $e$, the following constants are finite:
\[
C_{\nabla}:=\sup_{g\ne e}\frac{|\nabla \widetilde z(g)|^2}{\widetilde z(g)}<\infty,
\qquad
C_{\Delta}:=\sup_{g\in G}|\Delta_G\widetilde z(g)|<\infty.
\]

For each plaquette $p$, define the plaquette holonomy $U_p(U)$ and set $\widetilde z_p(U)=\widetilde z(U_p(U))$.

### Lemma 3.1 (linkwise bounds for $\widetilde z_p$)
If $\ell\notin\partial p$ then $X_\ell^a\widetilde z_p\equiv 0$ and $(X_\ell^a)^2\widetilde z_p\equiv 0$.
If $\ell\in\partial p$ then
\[
\sum_a (X_\ell^a \widetilde z_p)^2\le C_{\nabla}\,\widetilde z_p,
\qquad
\left|\sum_a (X_\ell^a)^2\widetilde z_p\right|\le C_{\Delta}.
\]
Consequently,
\[
\Gamma_\Lambda(\widetilde z_p)\le 4C_{\nabla}\,\widetilde z_p,
\qquad
|\Delta_\Lambda\widetilde z_p|\le 4C_{\Delta}.
\]

**Proof sketch.** The map $U\mapsto U_p(U)$ depends on $U_\ell$ by left/right multiplication and inversion, which are isometries for a bi-invariant metric. Thus derivative norms of $\widetilde z\circ U_p$ w.r.t. a link coordinate are bounded by the corresponding derivative norms of $\widetilde z$ on $G$. The factor $4$ comes from four boundary links. ∎

---

## 4. Expanding $\Gamma_\Lambda(V)$ and the overlap combinatorics

Write
\[
V(U)=\sum_{p}\Phi(\widetilde z_p(U)),\qquad \Phi\in C^2([0,2]),\ \Phi\ge 0,\ \Phi(0)=0.
\]
Let
\[
P(\ell):=\{p\in P(\Lambda):\ell\subset\partial p\},\qquad \nu:=\max_{\ell}|P(\ell)|.
\]
(In $4$D cubic, $\nu=6$.)

### Lemma 4.1 (first derivatives of $V$)
For each link $\ell$ and index $a$,
\[
X_\ell^a V
=\sum_{p\in P(\ell)} \Phi'(\widetilde z_p)\,X_\ell^a\widetilde z_p.
\]

### Proposition 4.2 (uniform bound $\Gamma(V)\lesssim V$)
Define the one-variable constant
\[
K_\Phi:=\sup_{s\in(0,2]} \frac{s\,(\Phi'(s))^2}{\Phi(s)}\in[0,\infty].
\]
Then
\[
\boxed{\ \Gamma_\Lambda(V)\le 4\nu C_{\nabla}K_\Phi\,V.\ }
\]

**Proof.** By Lemma 4.1,
\[
\Gamma(V)=\sum_{\ell,a}\Big(\sum_{p\in P(\ell)}\Phi'(\widetilde z_p)X_\ell^a\widetilde z_p\Big)^2.
\]
Use $(\sum_{i=1}^m u_i)^2\le m\sum_{i=1}^m u_i^2$ with $m\le\nu$:
\[
(X_\ell^a V)^2\le \nu\sum_{p\in P(\ell)} (\Phi'(\widetilde z_p))^2 (X_\ell^a\widetilde z_p)^2.
\]
Sum over $a$ and apply Lemma 3.1:
\[
\sum_a (X_\ell^a V)^2\le \nu\sum_{p\in P(\ell)} (\Phi'(\widetilde z_p))^2\,C_{\nabla}\widetilde z_p.
\]
Sum over $\ell$ and note each plaquette has $4$ boundary links:
\[
\Gamma(V)\le 4\nu C_{\nabla}\sum_p (\Phi'(\widetilde z_p))^2\widetilde z_p.
\]
Finally, $(\Phi'(s))^2 s\le K_\Phi\Phi(s)$ gives the claim. ∎

### Useful specialization: $\Phi(s)=s^2$
If $\Phi(s)=s^2$, then $K_\Phi\le 8$ (since $s(2s)^2/s^2=4s\le 8$) and
\[
V=\sum_p \widetilde z_p^2\le 2\sum_p \widetilde z_p=:2D
\]
because $s^2\le 2s$ on $[0,2]$. Hence
\[
\Gamma(V)\le 4\nu C_{\nabla}K_\Phi V\le 64\nu C_{\nabla}D.
\]

---

## 5. Expanding $L_\Lambda V$

By Lemma 2.1 applied termwise,
\[
L_\Lambda V=\sum_{p}\Big(\Phi'(\widetilde z_p)L_\Lambda\widetilde z_p+\Phi''(\widetilde z_p)\Gamma_\Lambda(\widetilde z_p)\Big).
\]
Write $L\widetilde z_p=\Delta\widetilde z_p-\langle \nabla S_\Lambda,\nabla \widetilde z_p\rangle$. Using $\nabla V=\sum_p \Phi'(\widetilde z_p)\nabla\widetilde z_p$ yields
\[
\boxed{\ L_\Lambda V
=\sum_p \Phi'(\widetilde z_p)\,\Delta_\Lambda\widetilde z_p
+\sum_p \Phi''(\widetilde z_p)\,\Gamma_\Lambda(\widetilde z_p)
-\langle \nabla S_\Lambda,\nabla V\rangle.\ }
\]

---

## 6. Bounding the non-coercive terms using $\Phi'(0)=0$

Assume
\[
\Phi'(0)=0.
\]
Then by the mean value theorem, $|\Phi'(s)|\le \|\Phi''\|_\infty\,s$ for $s\in[0,2]$. Define
\[
A_\Phi:=\|\Phi''\|_\infty,
\qquad
B_\Phi:=\sup_{s\in(0,2]}\frac{|\Phi'(s)|}{s}\le A_\Phi.
\]
Define the extensive functional
\[
D(U):=\sum_{p\in P(\Lambda)}\widetilde z_p(U).
\]

### Lemma 6.1 (Laplacian term)
\[
\left|\sum_p \Phi'(\widetilde z_p)\,\Delta_\Lambda \widetilde z_p\right|
\le 4B_\Phi C_{\Delta}\,D.
\]

**Proof.** Use $|\Delta \widetilde z_p|\le 4C_{\Delta}$ and $|\Phi'(\widetilde z_p)|\le B_\Phi\widetilde z_p$, then sum over $p$. ∎

### Lemma 6.2 (chain-rule term)
\[
\sum_p \Phi''(\widetilde z_p)\,\Gamma(\widetilde z_p)
\le 4A_\Phi C_{\nabla}\,D.
\]

**Proof.** Use $\Gamma(\widetilde z_p)\le 4C_{\nabla}\widetilde z_p$ and $\Phi''\le A_\Phi$. ∎

---

## 7. Drift inequality reduced to a coercivity estimate

Combine Lemma 2.2, the $LV$ expansion, and the bounds above:
\[
\frac{LW}{W}
=\eta LV+\eta^2\Gamma(V)
\le
-\eta\langle \nabla S_\Lambda,\nabla V\rangle
+\eta C_1 D +\eta^2 C_2 D,
\]
with
\[
C_1:=4(B_\Phi C_{\Delta}+A_\Phi C_{\nabla}),
\qquad
C_2:=\begin{cases}
4\nu C_{\nabla}K_\Phi\,\sup_{s\in(0,2]}\frac{\Phi(s)}{s}, &\text{if }V\le cD\text{ is available},\\
64\nu C_{\nabla}, &\text{for }\Phi(s)=s^2.
\end{cases}
\]

Thus the **only possible source of negativity** is the term
\[
\mathcal J(U):=\langle \nabla S_\Lambda(U),\nabla V(U)\rangle.
\]

### Missing coercivity input
A sufficient condition to turn the above into a Lyapunov drift is:

> **(Coercivity outside a small set)** There exist constants $c_0>0$, $b_0<\infty$, and a measurable set $K\subset M_\Lambda$ such that
> \[
> \boxed{\ \langle \nabla S_\Lambda,\nabla V\rangle\ \ge\ c_0 D - b_0\,\mathbf 1_K,\ }
> \]
> with $c_0,b_0$ independent of $\Lambda$.

If this holds, then
\[
\frac{LW}{W}\le -\eta(c_0-C_1-\eta C_2)D+\eta b_0\mathbf 1_K.
\]
Choose $\eta>0$ so that $c_0-C_1-\eta C_2\ge c_0/2$. Then
\[
\frac{LW}{W}\le -\frac{\eta c_0}{2}D+\eta b_0\mathbf 1_K.
\]
If $K$ is taken as a sublevel set $K=\{D\le D_*\}$, then on $K^c$ we have $D\ge D_*$ and hence
\[
LW\le -\lambda W\quad\text{on }K^c,\qquad \lambda:=\frac{\eta c_0}{2}D_*.
\]
On $K$, $LW\le \eta b_0 W$ gives the standard Lyapunov form $LW\le -\lambda W + b\mathbf 1_K$ by taking $b:=\eta b_0\sup_K W$.

**Conclusion.** All volume-sensitive parts of the drift are controlled once $\widetilde z$ is used and $\Phi'(0)=0$. The remaining obstruction is the coercivity bound on $\langle \nabla S_\Lambda,\nabla V\rangle$. The next reduction (to a link-local Gram-matrix row-sum condition) is carried out in the companion note `H_link_local_Gram_rowwise_coercivity.md`.
