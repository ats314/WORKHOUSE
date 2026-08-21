# Horizontal Bakry–Émery curvature for gauge-invariant observables (local CD\((\rho,\infty)\) with volume-uniform constants)

## Scope

This note extracts a single technical theorem that is unusually “physics-aligned”:

*The diffusion only needs curvature on the **physical** (horizontal) directions, because gradients of gauge-invariant observables are automatically horizontal.*

This converts a local geometric estimate into a functional-inequality statement that is compatible with gauge projection.

---

## 1. Geometry: gauge orbits and horizontality

Let \(M_\Lambda=G^{E(\Lambda)}\) with product bi-invariant metric \(g_\Lambda\). Let the lattice gauge group \(\mathcal G_\Lambda=G^{V(\Lambda)}\) act by
\[
(g\cdot U)_{(x,\mu)} := g_x\,U_{(x,\mu)}\,g_{x+\hat e_\mu}^{-1}.
\]

At any \(U\in M_\Lambda\), the tangent space splits into:

* **vertical** directions \(V_U\): tangent to the gauge orbit through \(U\),
* **horizontal** directions \(H_U:=V_U^\perp\) w.r.t. \(g_\Lambda\).

At the vacuum \(U^{(0)}\), under the right-invariant trivialization, the vertical space is \(\mathrm{im}(d_0)\subset\mathcal C^1(\Lambda;\mathfrak g)\) and a canonical horizontal choice is
\[
H_{U^{(0)}}=\ker(d_0^*).
\]

---

## 2. Lemma: gauge invariance forces horizontal gradients

### Lemma 2.1 (If \(f\) is gauge invariant then \(\nabla f(U)\in H_U\))

Let \(f\in C^\infty(M_\Lambda)\) satisfy \(f(g\cdot U)=f(U)\) for all \(g\in\mathcal G_\Lambda\). Then for every \(U\in M_\Lambda\),
\[
\langle \nabla f(U), v\rangle_{g_\Lambda}=0
\quad\forall v\in V_U.
\tag{2.1}
\]
Equivalently, \(\nabla f(U)\in H_U\).

**Proof.** Fix \(U\) and take any vertical vector \(v\in V_U\). By definition of verticality there exists a smooth curve \(g(t)\in\mathcal G_\Lambda\) with \(g(0)=e\) such that \(\frac{d}{dt}|_{t=0}(g(t)\cdot U)=v\). Gauge invariance implies \(f(g(t)\cdot U)\) is constant in \(t\), so its derivative at \(0\) is \(0\):
\[
0=\frac{d}{dt}\Big|_{t=0}f(g(t)\cdot U)=df(U)[v]=\langle\nabla f(U),v\rangle.
\]
\(\square\)

This is the precise place where gauge projection becomes analytically benign: the diffusion sees only horizontal derivatives for gauge-invariant observables.

---

## 3. Bochner–Bakry–Émery identity (Γ₂ calculus)

Let \(\mu_\Lambda\propto e^{-S_\Lambda}\mathrm{vol}_{g_\Lambda}\) and let
\[
L_\Lambda = \Delta_\Lambda - \langle \nabla S_\Lambda,\nabla\cdot\rangle
\]
be the reversible generator. Define \(\Gamma(f)=|\nabla f|^2\) and \(\Gamma_2(f)=\frac12(L\Gamma(f)-2\Gamma(f,Lf))\).

Then the project uses the standard identity
\[
\Gamma_2(f)
=
\|\nabla^2 f\|_{\mathrm{HS}}^2
+
\mathrm{Ric}_{\mu_\Lambda}(\nabla f,\nabla f),
\qquad
\mathrm{Ric}_{\mu_\Lambda}:=\mathrm{Ric}_{g_\Lambda}+\nabla^2 S_\Lambda.
\tag{3.1}
\]
This is the place where a curvature lower bound implies a CD inequality.

---

## 4. Core curvature theorem (local, horizontal, volume-uniform)

The project’s “Core curvature theorem” proves:

### Theorem 4.1 (Local horizontal curvature bound \(\Rightarrow\) local CD\((\rho,\infty)\) for gauge-invariants)

Assume:

1. \(G\) is compact semisimple with \(\mathrm{Ric}_{g_G}\ge \kappa_G g_G\) for some \(\kappa_G>0\).
2. \(S_\Lambda=S_W+S_{\mathrm{add},\Lambda}\), where \(S_W\) is Wilson and \(S_{\mathrm{add},\Lambda}\) is gauge-invariant and satisfies a global Hessian lower bound
   \[
   \nabla^2 S_{\mathrm{add},\Lambda}(U)\ge -C_{\mathrm{add}}\,g_\Lambda(U)
   \quad\forall U,
   \]
   with \(C_{\mathrm{add}}\) independent of \(\Lambda\).
3. \(C_{\mathrm{add}}<\kappa_G\).

Then there exist constants \(r>0\) and \(\rho_{\mathrm{loc}}>0\), depending only on \((\kappa_G,C_{\mathrm{add}})\) and local lattice structure, such that for every finite \(\Lambda\):

1. For all \(U\) with \(d(U,U^{(0)})\le r\) and all \(v\in H_U\),
   \[
   \mathrm{Ric}_{\mu_\Lambda}(U)(v,v)\ \ge\ \rho_{\mathrm{loc}}\,|v|^2.
   \tag{4.1}
   \]
2. For all gauge-invariant \(f\in C^\infty(M_\Lambda)^{\mathcal G_\Lambda}\) and all \(U\in B_r(U^{(0)})\),
   \[
   \Gamma_{2,\Lambda}(f)(U)\ \ge\ \rho_{\mathrm{loc}}\Gamma_\Lambda(f)(U).
   \tag{4.2}
   \]

**Proof sketch (what matters structurally).**

* Use product Ricci: \(\mathrm{Ric}_{g_\Lambda}\ge \kappa_G g_\Lambda\).
* At \(U^{(0)}\), \(\nabla^2 S_W(U^{(0)})\succeq 0\) (it equals a PSD Maxwell operator).
* By continuity and locality of the action, there exists \(r>0\) independent of \(\Lambda\) such that on \(B_r(U^{(0)})\) the negative part of \(\nabla^2 S_W\) is uniformly bounded by a small \(\varepsilon g_\Lambda\).
* Combine with \(\nabla^2 S_{\mathrm{add},\Lambda}\ge -C_{\mathrm{add}}g_\Lambda\) to get (4.1) with \(\rho_{\mathrm{loc}}=\kappa_G-C_{\mathrm{add}}-\varepsilon>0\).
* For gauge-invariant \(f\), Lemma 2.1 gives \(\nabla f\in H_U\). Plug into (3.1) to obtain (4.2) since the Hessian square term is nonnegative.

The nontrivial part is that \(r,\rho_{\mathrm{loc}}\) are made independent of \(\Lambda\), which relies on strict locality and bounded plaquette degree.

---

## 5. Why this is a “novel module” inside the project

This theorem is the bridge that makes “small-field curvature” compatible with gauge projection:

* It avoids any need to have a global curvature bound on the full manifold.
* It shows precisely which directions matter and why (horizontality).
* It packages the output as a local CD inequality in the exact form used by local Poincaré/LSI modules.

It is also the right place to swap Wilson for heat-kernel actions (the project notes an optional global-CD mechanism when Hessian bounds for \(-\log K_t\) are available).

