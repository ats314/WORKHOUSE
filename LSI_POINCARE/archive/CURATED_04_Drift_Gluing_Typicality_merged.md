# Lyapunov drift + gluing: a route to volume-uniform functional inequalities and “typicality”

## Overview

A recurring obstruction in lattice gauge theory is that “good” small-field regions \(K\) are analytically controlled (positive curvature, convexity-like behavior), but **may not be typical** under the Gibbs measure.

This note extracts a strategy from the project that can potentially close this loop:

1. Prove a **restricted** Poincaré/log-Sobolev inequality on the core set \(K\).
2. Prove a **Foster–Lyapunov drift inequality** that forces the dynamics to return to \(K\) and yields exponential tails for a coercive observable.
3. Use a **gluing argument** (partition of unity / local–global) to upgrade restricted functional inequalities to **global**, with constants uniform in volume.

The genuinely hard input is a non-cancellation lower bound on the Wilson force on the rough region, tracked as GAP-FC-02 in the project.

---

## 1. Abstract setting

Let \((M,g)\) be a compact Riemannian manifold (for the project: \(M=G^{E(\Lambda)}\)).
Let \(\mu(dU)\propto e^{-S(U)}\,dU\) be a smooth Gibbs measure.

Let \(K\subset M\) be a measurable “core” set (small-field region), and write \(\mu^K\) for \(\mu\) conditioned on \(K\).

Let \(\mathcal E(f,f)=\int \|\nabla f\|^2\,d\mu\) be the Dirichlet form.

---

## 2. Restricted functional inequalities on \(K\)

Assume a restricted Poincaré inequality:
\[
\operatorname{Var}_{\mu^K}(f)
\le
C_{\mathrm P}(K)\ \int_K \|\nabla f\|^2\,d\mu^K,
\tag{2.1}
\]
for all smooth \(f\) on \(K\) (Neumann boundary).

Similarly, one can assume a restricted log-Sobolev inequality (LSI):
\[
\operatorname{Ent}_{\mu^K}(f^2)
\le
2 C_{\mathrm{LSI}}(K)\ \int_K \|\nabla f\|^2\,d\mu^K.
\tag{2.2}
\]

**Why this is plausible on small-field regions.**  
On \(K_\Lambda(r)\), the matrix hinge inequality gives a uniform lower bound on Bakry–Émery curvature, which is a standard sufficient condition for (2.1)–(2.2) (with Neumann reflection).

---

## 3. Foster–Lyapunov drift and exponential tails

Let \(L\) be the (reversible) Langevin generator
\[
L f = \Delta f - \langle\nabla S, \nabla f\rangle.
\]

### Assumption (drift to the core)

There exist constants \(\lambda>0\), \(b<\infty\), a coercive function \(V\ge 1\), and a measurable “core” set \(K\) such that
\[
LV\ \le\ -\lambda V\ +\ b\,\mathbf 1_K
\qquad\text{(pointwise on }M\text{)}.
\tag{3.1}
\]

This is a standard Foster–Lyapunov condition: outside \(K\), the generator decreases \(V\) at rate \(\lambda\).

### Consequence 1: tail bound

Integrating (3.1) against \(\mu\) (using reversibility \(\int LV\,d\mu=0\)) gives
\[
\lambda\int V\,d\mu \ \le\ b\,\mu(K),
\quad\text{hence}\quad
\int V\,d\mu < \infty
\ \text{ with uniform control.}
\tag{3.2}
\]

With suitable choices of \(V\) (typically \(V=e^{\eta D}\) for a disorder observable \(D\)), one can bootstrap (3.2) into exponential tails:
\[
\mu(D\ge t)\ \lesssim\ e^{-c t},
\tag{3.3}
\]
with constants independent of \(|\Lambda|\), provided the drift inequality is uniform.

---

## 4. Gluing: restricted \(\Rightarrow\) global Poincaré/LSI

A typical gluing lemma (in the spirit of Cattiaux–Guillin–Wu type results) reads:

### Proposition (Poincaré gluing via drift)

Assume:

1. restricted Poincaré on \(K\), (2.1), with constant \(C_{\mathrm P}(K)\),
2. drift condition (3.1) for a Lyapunov function \(V\),
3. a mild regularity condition controlling \(\|\nabla V\|^2/V\) (or an equivalent “coercive pairing” estimate).

Then \(\mu\) satisfies a global Poincaré inequality
\[
\operatorname{Var}_\mu(f)
\le
C_{\mathrm P}\ \int \|\nabla f\|^2\,d\mu,
\tag{4.1}
\]
with \(C_{\mathrm P}\) independent of \(|\Lambda|\).

A parallel statement holds for LSI under corresponding assumptions.

**What is nontrivial here.**  
For lattice Yang–Mills, the drift inequality (3.1) is not automatic; it requires a lower bound on \(\langle\nabla S,\nabla V\rangle\) outside \(K\), i.e. that the Wilson “force” cannot become small while disorder is large.

---

## 5. Specialization to Wilson disorder: where GAP-FC-02 enters

A natural disorder observable is
\[
D_\Lambda(U) := \sum_{p\in P(\Lambda)} \vartheta(U_p(U)),
\qquad
\mathcal B_\Lambda(U) := \frac{1}{|P(\Lambda)|}D_\Lambda(U).
\]
Note that \(S_\Lambda=\beta D_\Lambda\).

A common Lyapunov choice is \(V=e^{\eta D_\Lambda}\). Then
\[
LV = e^{\eta D_\Lambda}
\Bigl(
\eta\,L D_\Lambda + \eta^2 \|\nabla D_\Lambda\|^2
\Bigr),
\tag{5.1}
\]
and since \(L D_\Lambda=\Delta D_\Lambda - \langle\nabla S_\Lambda,\nabla D_\Lambda\rangle\),
one is led to control the coercive term
\[
\langle\nabla S_\Lambda,\nabla D_\Lambda\rangle
=
\beta\,\|\nabla D_\Lambda\|^2.
\tag{5.2}
\]

To obtain a genuine drift outside \(K\), one needs a **force non-cancellation** statement of the form:
\[
\mathcal B_\Lambda(U)\ge \varepsilon
\quad\Longrightarrow\quad
\|\nabla S_\Lambda(U)\|\ge c(\varepsilon),
\tag{5.3}
\]
or at least a local version sufficient to ensure \(\|\nabla D_\Lambda\|^2\) is bounded below on the rough region.
This is exactly **GAP-FC-02** (“Cartan alignment / local cancellation”).

---

## 6. Typicality and localization

Once a global LSI is available with constant \(C_{\mathrm{LSI}}\) independent of \(|\Lambda|\), concentration of Lipschitz observables implies:

- if \(f\) is \(L\)-Lipschitz, then
  \[
  \mu\bigl(f-\mathbb Ef\ge t\bigr) \le \exp\!\Bigl(-\frac{t^2}{2C_{\mathrm{LSI}}L^2}\Bigr),
  \tag{6.1}
  \]
- in particular, for \(\mathcal B_\Lambda\) one has \(L^2\asymp |P(\Lambda)|^{-1}\),
  so deviations are \(\exp(-c|P(\Lambda)|)\).

This produces the “typicality” bound needed to control localization errors in covariance decompositions:
\[
\mu\!\left(K_\Lambda(\varepsilon)^c\right)
\le
\exp\!\bigl(-c_{\mathrm{typ}}|P(\Lambda)|\bigr).
\tag{6.2}
\]

The key point is that the large-volume exponent \(|P(\Lambda)|\) can be traded for a graph-distance exponent along a corridor connecting the supports of observables.

---

## 7. What’s genuinely new / high-upside here

- The strategy replaces classical cluster expansions by a **functional inequality + resolvent decay** mechanism.
- The presence of a **geometric mass floor** (Haar mass) stabilizes the Witten Laplacian uniformly in volume.
- If GAP-FC-02 can be made quantitative, the drift+gluing route becomes a potentially robust framework for **nonabelian lattice gauge Gibbs states** beyond perturbation theory.

---

## 8. Next steps that would materially advance the project

1. Make (5.3) rigorous in the actual lattice geometry (Cartan alignment exceptional set, uniform constants).  
2. Prove a clean drift inequality (3.1) with \(V=e^{\eta D_\Lambda}\) or a variant adapted to the Wilson action.  
3. Close the loop: drift \(\Rightarrow\) global LSI \(\Rightarrow\) typicality \(\Rightarrow\) remove the \(K\)-conditioning in exponential clustering.
