# Matrix hinge to massive Maxwell covariance control

## 1. Setup

Let $G$ be a compact Lie group with Lie algebra $\mathfrak g$ and bi-invariant metric $g_G$.  Let $\Lambda$ be a finite $d$-dimensional lattice box (periodic or with suitable boundary), with oriented link set $E(\Lambda)$ and plaquette set $P(\Lambda)$.  The configuration manifold is
\[
M_\Lambda := G^{E(\Lambda)}
\]
with product Riemannian metric $g_\Lambda$ (right-trivialized linkwise).  The Wilson action at inverse coupling $\beta$ is
\[
S_{\Lambda,\beta}(U)
:= \beta\sum_{p\in P(\Lambda)} \Phi\big(U_p(U)\big),
\qquad
\Phi(g):=1-\frac{1}{n}\Re\,\mathrm{Tr}(\rho(g)),
\]
where $\rho$ is a fixed faithful unitary representation of dimension $n$.

The Wilson Gibbs measure is
\[
d\mu_{\Lambda,\beta}(U)
:= Z_{\Lambda,\beta}^{-1} e^{-S_{\Lambda,\beta}(U)}\,d\mathrm{vol}_{g_\Lambda}(U).
\]
Let
\[
L_\Lambda := \Delta_{g_\Lambda}-\langle\nabla S_{\Lambda,\beta},\nabla(\cdot)\rangle_{g_\Lambda}
\]
be the reversible Langevin generator on $L^2(\mu_{\Lambda,\beta})$.

The Bakry–Émery curvature endomorphism (right-trivialized to a bundle of $\mathfrak g$-valued $1$-cochains) is
\[
\mathrm{Ric}_{\mu}(U)
:= \mathrm{Ric}_{g_\Lambda}(U) + \nabla^2 S_{\Lambda,\beta}(U).
\]

## 2. Vacuum linearization and the Maxwell stiffness operator

Let $U^{(0)}$ denote the vacuum configuration ($U^{(0)}\equiv \mathbf 1$ linkwise).  Linearizing the plaquette map in exponential coordinates $U=\exp(A)$ with $A\in\mathcal C^1(\Lambda;\mathfrak g)$ small gives
\[
U_p(U)=\exp\big((d_1 A)_p + O(|A|^2)\big).
\]
For the Wilson action, the Hessian at vacuum is the discrete Maxwell stiffness:
\[
\nabla^2 S_{\Lambda,\beta}(U^{(0)})
= \frac{\beta}{n\lambda_\rho}\, d_1^* d_1,
\]
where $d_1$ is the cochain coboundary $\mathcal C^1\to\mathcal C^2$ and $\lambda_\rho>0$ is the representation constant appearing in the quadratic expansion of $\Phi$ at $\mathbf 1$.

Define the Maxwell parameter
\[
\alpha := \frac{\beta}{n\lambda_\rho}.
\]

## 3. A localized hinge inequality for $\mathrm{Ric}_{\mu}$

Fix $r>0$ and define the linkwise small-field set $K_\Lambda(r)\subset M_\Lambda$ by the condition that all plaquette holonomies lie in a fixed geodesic ball of radius $r$ around $\mathbf 1$.

Let $c_H>0$ be a uniform lower bound for the Ricci curvature of the product Haar metric $g_\Lambda$ (depending only on $(G,g_G)$).  Let $R_W(r)$ denote the Wilson-Hessian remainder term controlling how far $\nabla^2 S$ can drift from its vacuum value on $K_\Lambda(r)$; in the Wilson case one obtains $R_W(r)=O(\beta r)$ as $r\downarrow 0$.

### Proposition 3.1 (localized matrix hinge)
On $K_\Lambda(r)$ one has the pointwise operator inequality
\[
\mathrm{Ric}_{\mu}(U)
\ \succeq\ 
\big(c_H - R_W(r)\big)\,I\ +\ \alpha\, d_1^* d_1,
\qquad U\in K_\Lambda(r),
\]
as quadratic forms on the horizontal sector (gauge-invariant gradients).

*Proof.* The product metric satisfies $\mathrm{Ric}_{g_\Lambda}(U)\succeq c_H I$ uniformly.  On $K_\Lambda(r)$, the Wilson Hessian stability estimate gives
\[
\nabla^2 S_{\Lambda,\beta}(U)
\succeq \nabla^2 S_{\Lambda,\beta}(U^{(0)})-R_W(r)\,I
= \alpha\,d_1^*d_1 - R_W(r)\,I.
\]
Adding the two bounds yields the claim.
\hfill $\square$

Choosing $r$ so that $R_W(r)\le c_H/2$ yields the cleaner form
\[
\mathrm{Ric}_{\mu}(U)
\succeq m^2 I + \alpha\, d_1^* d_1,
\qquad m^2:=c_H/2,
\qquad U\in K_\Lambda(r).
\]

## 4. Helffer–Sjöstrand representation and matrix Brascamp–Lieb

Let $\mathcal L^{(1)}_\Lambda$ denote the Witten Laplacian on $1$-forms (equivalently on vector fields) associated with $L_\Lambda$.  It satisfies the commutation identity
\[
\nabla(-L_\Lambda u)=\mathcal L^{(1)}_\Lambda(\nabla u),
\]
and the Bochner–Weitzenböck decomposition
\[
\mathcal L^{(1)}_\Lambda
= (-L_\Lambda)\otimes I + \mathrm{Ric}_{\mu}.
\]
In particular,
\[
\mathcal L^{(1)}_\Lambda \succeq \mathrm{Ric}_{\mu}
\qquad\text{(quadratic-form order).}
\]

### Proposition 4.1 (Helffer–Sjöstrand covariance identity)
For $F,G\in C^\infty(M_\Lambda)$ with $\mu(G)=0$,
\[
\mathrm{Cov}_\mu(F,G)
= \int\Big\langle\nabla F,\ (\mathcal L^{(1)}_\Lambda)^{-1}\nabla G\Big\rangle\,d\mu.
\]

### Corollary 4.2 (matrix Brascamp–Lieb via a curvature lower bound)
If on a domain $\mathcal D\subseteq M_\Lambda$ one has $\mathrm{Ric}_{\mu}(U)\succeq M$ for a fixed strictly positive self-adjoint operator $M$ on the horizontal sector, then on $\mathcal D$,
\[
(\mathcal L^{(1)}_\Lambda)^{-1}\preceq M^{-1},
\]
and, after localizing gradients to $\mathcal D$,
\[
|\mathrm{Cov}_\mu(F,G)|
\le
\Big(\int\langle\nabla F,M^{-1}\nabla F\rangle\,d\mu\Big)^{1/2}
\Big(\int\langle\nabla G,M^{-1}\nabla G\rangle\,d\mu\Big)^{1/2}.
\]

## 5. The massive Maxwell operator

On the horizontal sector, define the **massive Maxwell operator**
\[
M_\Lambda := m^2 I + \alpha\, d_1^* d_1,
\qquad m^2>0,\ \alpha>0.
\]
On $K_\Lambda(r)$, Proposition 3.1 gives $\mathrm{Ric}_{\mu}(U)\succeq M_\Lambda$, hence the matrix Brascamp–Lieb bound yields, for observables whose gradients are supported in $K_\Lambda(r)$ (or after conditioning to $K_\Lambda(r)$),
\[
|\mathrm{Cov}_\mu(F,G)|
\lesssim
\Big(\int\langle\nabla F,M_\Lambda^{-1}\nabla F\rangle\,d\mu\Big)^{1/2}
\Big(\int\langle\nabla G,M_\Lambda^{-1}\nabla G\rangle\,d\mu\Big)^{1/2}.
\]

This reduces correlation decay on the small-field set to off-diagonal decay bounds for the inverse kernel $M_\Lambda^{-1}$ on the link graph.
