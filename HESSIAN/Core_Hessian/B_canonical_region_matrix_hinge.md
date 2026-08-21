# Canonical region \(K_\Lambda(r)\) and a localized *matrix hinge* inequality

This note packages two objects that are unusually useful for gauge theory functional inequalities:

1. a **canonical small-field region** \(K_\Lambda(r)\) defined by linkwise control (no gauge fixing), and  
2. a **localized hinge inequality** that keeps the Wilson contribution as the structured PSD operator \(d_1^*d_1\), instead of collapsing it to a scalar off-diagonal bound.

The output is a pointwise operator inequality on tangent vectors:
\[
\mathrm{Ric}_{\mu_\Lambda}(U)\ \succeq\ \frac{c_H}{2}I + \frac{\beta}{3}d_1^*d_1,
\qquad U\in K_\Lambda(r),
\]
with explicit \(r\sim 1/\beta\) and constants independent of \(|\Lambda|\).

---

## 1. Setup

Let \(G=\mathrm{SU}(3)\) (the formulas below extend to \(\mathrm{SU}(N)\) with minor changes). Let \(\Lambda\subset\mathbb Z^d\) be finite. The configuration manifold is
\[
M_\Lambda := G^{E(\Lambda)}
\]
with product bi-invariant metric \(g_\Lambda\) and volume \( \mathrm{vol}_{g_\Lambda} = \bigotimes_{\ell\in E(\Lambda)}\mathrm{Haar}(dU_\ell)\).

Let the Wilson action be
\[
S_W(U)=\sum_{p\in P(\Lambda)} \Phi(U_p),
\qquad
\Phi(U)=\frac{\beta}{3}\,\mathrm{ReTr}(I-U).
\]
Define the Gibbs measure \(\mu_\Lambda\propto e^{-S_W}\mathrm{vol}_{g_\Lambda}\).

In the Bochner–Bakry–Émery identity for the diffusion generator with invariant measure \(\mu_\Lambda\),
the curvature matrix is
\[
\mathrm{Ric}_{\mu_\Lambda}(U)=\mathrm{Ric}_{g_\Lambda}(U)+\nabla^2S_W(U).
\tag{1.1}
\]

Assume a uniform “Haar mass” lower bound:
\[
\mathrm{Ric}_{g_\Lambda}\ \succeq\ c_H I
\qquad\text{(block-diagonal across links, uniform in \(\Lambda\)).}
\tag{1.2}
\]

Let \(\nu\) denote the maximum number of plaquettes incident to any edge (a local combinatorial constant; in \(d=4\), \(\nu=6\)).

---

## 2. Canonical region \(K_\Lambda(r)\)

For \(r>0\), let \(B_r(e)\subset G\) denote the metric ball of radius \(r\) around the identity element \(e\in G\).

### Definition 2.1 (Linkwise small-field region)

Define
\[
K_\Lambda(r) := \big\{U\in M_\Lambda:\ U_\ell\in B_r(e)\ \text{for every }\ell\in E(\Lambda)\big\}.
\tag{2.1}
\]
This is gauge-invariant (since \(B_r(e)\) is conjugation invariant under the bi-invariant metric) and depends only on local link variables.

---

## 3. Wilson Hessian at vacuum and its small-field stability

At the vacuum \(U^{(0)}\) one has (cf. the full derivation in the “Wilson Hessian = Maxwell operator” note)
\[
\nabla^2 S_W(U^{(0)})=\frac{\beta}{3}d_1^*d_1,
\tag{3.1}
\]
as an operator on \(\mathcal C^1(\Lambda;\mathfrak{su}(3))\).

The point of the hinge inequality is to show that for \(U\in K_\Lambda(r)\) the Hessian stays close to \(\nabla^2S_W(U^{(0)})\), with an error bounded by a *scalar* multiple of the identity that is linear in \(r\).

### Lemma 3.1 (Uniform Lipschitz bound on the plaquette Hessian)

Fix \(r_\star>0\). Let \(F:G^4\to\mathbb R\) denote the single-plaquette Wilson potential written as a function of the four boundary links:
\[
F(g_1,g_2,g_3,g_4):=\Phi(g_1g_2g_3^{-1}g_4^{-1}).
\]
Let \(M_3(r_\star)\) be a Lipschitz constant for \(D^2F\) on \((B_{r_\star}(e))^4\), i.e.
\[
\big|D^2F(g)(\xi,\xi)-D^2F(h)(\xi,\xi)\big|
\le M_3(r_\star)\,\mathrm{dist}_{G^4}(g,h)\,|\xi|^2,
\qquad g,h\in (B_{r_\star}(e))^4.
\tag{3.2}
\]
Then for \(0<r\le r_\star\) and any \(U\in K_\Lambda(r)\),
\[
\nabla^2 S_W(U)(X,X)
\ge
\nabla^2 S_W(U^{(0)})(X,X)
-
\frac{\beta}{3}\,2M_3(r_\star)\,r\sum_{p\in P(\Lambda)} |X_{\partial p}|^2,
\tag{3.3}
\]
for all \(X\in \mathcal C^1(\Lambda;\mathfrak{su}(3))\), where \(X_{\partial p}\in\mathfrak{su}(3)^4\) is the 4-tuple of link components along \(\partial p\).

**Proof.**
For each plaquette \(p\), the corresponding term \(S_{W,p}(U)=F(U_{\partial p})\) has second derivative \(D^2F(U_{\partial p})\). If \(U\in K_\Lambda(r)\), then each of the four boundary links of \(p\) lies in \(B_r(e)\), hence
\[
\mathrm{dist}_{G^4}(U_{\partial p},e_{\partial p})\le 2r,
\]
so by (3.2),
\[
D^2F(U_{\partial p})(X_{\partial p},X_{\partial p})
\ge
D^2F(e_{\partial p})(X_{\partial p},X_{\partial p}) - 2M_3(r_\star)r\,|X_{\partial p}|^2.
\]
Sum over plaquettes and multiply by the factor \(\beta/3\). ∎

### Lemma 3.2 (Combinatorial reduction)

For any \(X\in \mathcal C^1(\Lambda;\mathfrak{su}(3))\),
\[
\sum_{p\in P(\Lambda)} |X_{\partial p}|^2
=
\sum_{p}\sum_{\ell\in\partial p} |X_\ell|^2
=
\sum_{\ell}\#\{p:\ell\in\partial p\}\,|X_\ell|^2
\le \nu\,|X|^2.
\tag{3.4}
\]

**Proof.**
Expand and use the definition of \(\nu\). ∎

Combining (3.3)–(3.4) gives the clean bound
\[
\nabla^2S_W(U)\ \succeq\ \nabla^2S_W(U^{(0)}) - R_W(r)\,I,
\qquad U\in K_\Lambda(r),
\tag{3.5}
\]
with
\[
R_W(r):=\left(\frac{2\nu M_3(r_\star)}{3}\right)\beta r.
\tag{3.6}
\]

---

## 4. The localized hinge inequality

### Proposition 4.1 (Localized hinge inequality on \(K_\Lambda(r)\))

Fix \(r_\star>0\) and \(M_3(r_\star)\) as above. For every \(0<r\le r_\star\) and every \(U\in K_\Lambda(r)\),
\[
\mathrm{Ric}_{\mu_\Lambda}(U)
\ \succeq\
\big(c_H-R_W(r)\big)I + \frac{\beta}{3}d_1^*d_1
\qquad\text{as quadratic forms on }\mathcal C^1(\Lambda;\mathfrak{su}(3)).
\tag{4.1}
\]

In particular, if \(r\) is chosen so that
\[
R_W(r)\le \frac{c_H}{2}
\qquad\Longleftrightarrow\qquad
r \le \frac{3c_H}{4\nu M_3(r_\star)}\cdot\frac1\beta,
\tag{4.2}
\]
then
\[
\mathrm{Ric}_{\mu_\Lambda}(U)
\ \succeq\
\frac{c_H}{2}I + \frac{\beta}{3}d_1^*d_1,
\qquad U\in K_\Lambda(r).
\tag{4.3}
\]

**Proof.**
Using (1.1), (1.2), and (3.5),
\[
\mathrm{Ric}_{\mu_\Lambda}(U)
=
\mathrm{Ric}_{g_\Lambda}(U)+\nabla^2S_W(U)
\succeq
c_H I + \left(\frac{\beta}{3}d_1^*d_1 - R_W(r)I\right),
\]
giving (4.1). The choice (4.2) yields (4.3). ∎

### Specialization (hypercubic \(d=4\))

In \(d=4\), each edge belongs to \(\nu=6\) plaquettes, hence
\[
R_W(r)=4M_3(r_\star)\,\beta r.
\tag{4.4}
\]

---

## 5. Why this is structurally different from scalar diagonal-dominance bounds

The estimate (4.3) retains the Wilson contribution as the **structured PSD operator** \(d_1^*d_1\). Only the *localization remainder* is scalarized into \(R_W(r)I\).

This avoids the usual “absolute values everywhere” step that replaces a signed incidence structure by a worst-case off-diagonal constant. The downstream consequence is that covariance decay reduces to a **Green’s function estimate for**
\[
M := \frac{c_H}{2}I + \frac{\beta}{3}d_1^*d_1
\quad\text{(on the appropriate horizontal sector)}.
\]

That Green’s function estimate is the next analytic module.
