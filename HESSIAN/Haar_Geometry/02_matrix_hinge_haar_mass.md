# Localized matrix hinge inequality: Haar “mass” + Wilson Maxwell term (on a canonical \(K_\Lambda\))

This note extracts the key geometric inequality that makes the “curvature → covariance → decay” pipeline run:

> On a **canonical small-field region** \(K_\Lambda\), the Bakry–Émery curvature matrix of the lattice Gibbs measure has a **volume-uniform, matrix lower bound**
> \[
> \mathrm{Ric}_{g_\Lambda}(U) + \nabla^2 S_\Lambda(U)\ \succeq\ m^2 I + t\, d_1^\ast d_1,
> \]
> at least on **horizontal** directions (physical, gauge-invariant gradients).

The point is not that \(m^2I\) or \(t d_1^\ast d_1\) are exotic; the point is that you preserve the *signed, sparse incidence structure* of \(d_1^\ast d_1\) instead of throwing it away via scalar diagonal-dominance bounds.

---

## 1. Configuration geometry and the Bakry–Émery matrix

Let \(\Lambda\) be finite. Let \(G\) be compact with a bi-invariant metric \(g_G\). Define
\[
M_\Lambda := G^{E(\Lambda)},\qquad g_\Lambda := \bigoplus_{e\in E(\Lambda)} g_G.
\]

Let \(S_\Lambda\) be the (possibly augmented) action; for concreteness
\[
S_\Lambda = S_W + S_{\mathrm{add},\Lambda},
\]
where \(S_W\) is Wilson and \(S_{\mathrm{add},\Lambda}\) is any additional gauge-invariant local term.

Define the Gibbs measure
\[
d\mu_\Lambda(U) = Z_\Lambda^{-1}\,e^{-S_\Lambda(U)}\,d\mathrm{vol}_{g_\Lambda}(U).
\]

### Definition 1.1 (Bakry–Émery curvature matrix)
At \(U\in M_\Lambda\), define the Bakry–Émery tensor
\[
\mathrm{Ric}_{\mu_\Lambda}(U) := \mathrm{Ric}_{g_\Lambda}(U) + \nabla^2 S_\Lambda(U),
\]
viewed as a self-adjoint endomorphism of \(T_U M_\Lambda\).

This is the matrix that appears in the Bochner identity for the reversible diffusion
\[
L_\Lambda f = \Delta_{g_\Lambda} f - \langle \nabla S_\Lambda,\nabla f\rangle_{g_\Lambda}.
\]

---

## 2. Haar “mass”: product Ricci is a uniform on-site positive term

Assume \(G\) is compact semisimple with the chosen bi-invariant metric. Then there exists \(\kappa_G>0\) such that
\[
\mathrm{Ric}_G \ \ge\ \kappa_G\, g_G.
\]

### Lemma 2.1 (Product Ricci lower bound is volume-independent)
On \(M_\Lambda\) with the product metric \(g_\Lambda\),
\[
\mathrm{Ric}_{g_\Lambda} \ \ge\ \kappa_G\, g_\Lambda,
\]
with the **same** \(\kappa_G\), independent of \(|E(\Lambda)|\).

**Proof.**
For a Riemannian product, the Ricci tensor is the direct sum of the factor Ricci tensors. If \(v=(v_e)_{e\in E}\in T_U M_\Lambda\),
\[
\mathrm{Ric}_{g_\Lambda}(v,v)=\sum_{e\in E}\mathrm{Ric}_G(v_e,v_e)\ \ge\ \sum_e \kappa_G |v_e|^2
=\kappa_G |v|^2_{g_\Lambda}.
\]
\(\square\)

This uniform \(\kappa_G\) is what the project calls “Haar mass”.

---

## 3. Canonical small-field region \(K_\Lambda\)

Fix \(r>0\) smaller than the injectivity radius of \(G\). Let \(B_r(e)\subset G\) denote the geodesic ball around the identity.

### Definition 3.1 (Linkwise small-field set)
\[
K_\Lambda(r) := \{U\in M_\Lambda:\ U_e\in B_r(e)\text{ for every }e\in E(\Lambda)\}.
\]

This definition is not gauge-invariant, but it is the simplest set on which one can make **uniform Taylor bounds** on all plaquette factors.

(You can also define averaged-plaquette “badness” sets; those are more natural probabilistically, but for a *pointwise operator bound* you typically want a uniform local neighborhood where third derivatives are controlled.)

---

## 4. Stability of the Wilson Hessian on \(K_\Lambda(r)\)

Assume \(G=\mathrm{SU}(N)\) with the conventions of `01_wilson_hessian_hodge.md`. Let
\[
S_W(U)=\sum_{p\in P(\Lambda)}\Phi(U_p),\qquad \Phi(U)=\frac{\beta}{N}\,\mathrm{ReTr}(I-U).
\]

We will need one uniform combinatorial constant:
\[
\nu := \sup_{e\in E(\Lambda)} \#\{p\in P(\Lambda): e\in\partial p\},
\]
the maximal number of plaquettes containing a given oriented edge; on the hypercubic lattice \(\nu=2(d-1)\).

### Lemma 4.1 (Wilson Hessian is a controlled perturbation of its vacuum matrix)
There exists a constant \(C_3<\infty\) (depending on \(G\) and the chosen \(r_\star\) but not on \(\Lambda\)) such that for all \(0<r\le r_\star\), all \(U\in K_\Lambda(r)\), and all \(X\in \mathcal C^1(\Lambda;\mathfrak{su}(N))\),
\[
\nabla^2 S_W(U)(X,X)
\ \ge\
\nabla^2 S_W(U^{(0)})(X,X) \;-\; \underbrace{(C_3\,\nu\,\beta\, r)}_{=:R_W(r)}\,\|X\|^2.
\]

Equivalently, as quadratic forms on \(\mathcal C^1\),
\[
\nabla^2 S_W(U)\ \succeq\ \frac{\beta}{N} d_1^\ast d_1 \;-\; R_W(r)\,I.
\]

**Proof.**
Write the Wilson action as a sum of local plaquette functions \(F(U_{\partial p})\), \(S_W=\frac{\beta}{N}\sum_p F\).  
On \((B_{r_\star}(e))^4\subset G^4\), \(D^2F\) is Lipschitz with constant \(\sup|D^3F|=:C_3\). For \(U\in K_\Lambda(r)\), each plaquette boundary lies within distance \(\mathcal O(r)\) of \((e,e,e,e)\), hence
\[
D^2F(U_{\partial p}) \ge D^2F(e_{\partial p}) - C_3\,r\cdot I
\]
as quadratic forms on the 4-edge boundary tangent space. Summing over plaquettes and using that each edge appears in at most \(\nu\) plaquettes yields the stated global bound with \(R_W(r)\propto \nu\beta r\). \(\square\)

---

## 5. Additive terms and the final hinge inequality

Assume the additional action satisfies a uniform Hessian lower bound
\[
\nabla^2 S_{\mathrm{add},\Lambda}(U)\ \ge\ -C_{\mathrm{add}}\, I
\qquad \forall U\in M_\Lambda,
\]
with \(C_{\mathrm{add}}\ge 0\) independent of \(\Lambda\).

Then for \(U\in K_\Lambda(r)\),
\[
\nabla^2 S_\Lambda(U)
\ge
\frac{\beta}{N}d_1^\ast d_1\ -\ (R_W(r)+C_{\mathrm{add}})I.
\]

Combine with Lemma 2.1:

### Proposition 5.1 (Localized matrix hinge inequality)
For all \(U\in K_\Lambda(r)\),
\[
\mathrm{Ric}_{\mu_\Lambda}(U)
=
\mathrm{Ric}_{g_\Lambda}(U)+\nabla^2S_\Lambda(U)
\ \succeq\
\underbrace{\big(\kappa_G-(R_W(r)+C_{\mathrm{add}})\big)}_{=:m^2(r)}\, I
\ +\
\underbrace{\frac{\beta}{N}}_{=:t}\, d_1^\ast d_1.
\]

In particular, if \(r\) is chosen such that \(R_W(r)+C_{\mathrm{add}}\le \kappa_G/2\), then on \(K_\Lambda(r)\),
\[
\mathrm{Ric}_{\mu_\Lambda}(U)\ \succeq\ \frac{\kappa_G}{2} I + \frac{\beta}{N} d_1^\ast d_1.
\]

**Proof.**
Immediate from the previous inequalities and the definition of \(\mathrm{Ric}_{\mu_\Lambda}\). \(\square\)

---

## 6. Horizontal directions and gauge-invariant gradients

Let the lattice gauge group \(\mathcal G_\Lambda=G^{V(\Lambda)}\) act on \(M_\Lambda\) by \((g\cdot U)_e=g_{s(e)}U_e g_{t(e)}^{-1}\).

At \(U^{(0)}\), the infinitesimal gauge directions are exactly \(\mathrm{Im}(d_0)\subset\mathcal C^1\). The orthogonal complement is the horizontal subspace \(H_{U^{(0)}}=\ker(d_0^\ast)\).

### Lemma 6.1 (Gradients of gauge-invariant observables are horizontal)
If \(F:M_\Lambda\to\mathbb R\) is gauge invariant, then for every \(U\in M_\Lambda\), its Riemannian gradient satisfies
\[
\nabla F(U)\ \perp\ T_U(\mathcal G_\Lambda\cdot U).
\]
In particular, at \(U^{(0)}\) one has \(\nabla F(U^{(0)})\in\ker(d_0^\ast)\).

**Proof.**
Let \(V\) be any tangent vector generated by the gauge action (a vertical vector). Gauge invariance means \(F(\exp(tV)\cdot U)=F(U)\) for all \(t\), hence \(dF_U(V)=0\). But \(dF_U(V)=\langle \nabla F(U),V\rangle\). Thus \(\nabla F(U)\) is orthogonal to all vertical directions. \(\square\)

So, for gauge-invariant observables, the hinge inequality can be restricted to the horizontal sector without loss.

---

## 7. Why this hinge is “the” nontrivial structural asset

Scalar diagonal-dominance approaches replace the Wilson Hessian by inequalities of the form
\[
\mathrm{Hess}(S_W)\ \ge\ (\kappa - JD)\,I,
\]
where \(J\) bounds cross-terms and \(D\) is the interaction degree. This discards the signed Maxwell structure.

The hinge inequality above keeps the full PSD matrix \(d_1^\ast d_1\).  
Everything downstream (matrix covariance bounds + Green's function decay) exploits that structure rather than fighting it.

---
