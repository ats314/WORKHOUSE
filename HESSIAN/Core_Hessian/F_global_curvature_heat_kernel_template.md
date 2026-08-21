# Global Bakry–Émery curvature template for heat-kernel plaquette actions

This note records a simple but structurally important mechanism:

> If a plaquette potential has a **uniform global Hessian upper bound** on the compact group \(G\), then the induced lattice action has a **global** Bakry–Émery curvature lower bound of the form
> \[
> \kappa_{\mathrm{global}}
> \ \ge\
> \kappa_G - \nu\,M_2,
> \]
> where \(\kappa_G\) is the group Ricci constant and \(\nu\) is the local plaquette-incidence constant.

This is especially clean for **heat-kernel** (Villain) plaquette weights, where \(V_t(g):=-\log K_t(g)\) is smooth on \(G\) for each fixed \(t>0\).

The output is a global curvature-dimension condition \(CD(\kappa_{\mathrm{global}},\infty)\) whenever \(\kappa_{\mathrm{global}}>0\), with \(\kappa_{\mathrm{global}}\) independent of \(|\Lambda|\).

---

## 1. Setup

Let \(G\) be a compact, connected Lie group with bi-invariant metric \(g_G\) and Ricci lower bound
\[
\mathrm{Ric}_G\ge \kappa_G g_G,
\qquad \kappa_G>0.
\tag{1.1}
\]
Let \(\Lambda\subset\mathbb Z^d\) be finite, and \(M_\Lambda:=G^{E(\Lambda)}\) with product metric \(g_\Lambda\). Let \(\nu\) be the maximal number of plaquettes incident to a given edge.

Let \(K_t:G\to(0,\infty)\) be the heat kernel on \(G\) at time \(t>0\) (with respect to Haar volume), and define the heat-kernel potential
\[
V_t(g):=-\log K_t(g).
\tag{1.2}
\]
Since \(G\) is compact and \(K_t\) is smooth and strictly positive for \(t>0\), \(V_t\in C^\infty(G)\).

Define the global second-derivative bound
\[
M_2(t):=\sup_{g\in G}\ \|\nabla^2 V_t(g)\|_{\mathrm{op}} <\infty.
\tag{1.3}
\]

Consider the plaquette action
\[
A_t(U):=\sum_{p\in P(\Lambda)} V_t(U_p(U)).
\tag{1.4}
\]
Define the Gibbs measure
\[
\mu_{\Lambda,t}(\mathrm dU)=Z_{\Lambda,t}^{-1}e^{-A_t(U)}\,\mathrm{vol}_{g_\Lambda}(\mathrm dU).
\tag{1.5}
\]

---

## 2. A uniform lower bound for the lattice action Hessian

### Lemma 2.1 (Single plaquette Hessian lower bound)

Fix a plaquette \(p\). Let \(A_{t,p}(U):=V_t(U_p(U))\). Then for all \(U\in M_\Lambda\),
\[
\nabla^2 A_{t,p}(U)\ \succeq\ -C_p\,M_2(t)\,g_\Lambda(U),
\tag{2.1}
\]
where \(C_p\) depends only on the number of links in \(\partial p\) (hence \(C_p\) is an absolute constant, independent of \(\Lambda\)).

**Proof.**
The map \(U\mapsto U_p(U)\) depends only on the four link variables in \(\partial p\) and is smooth. Its differential and second differential are bounded in operator norm on the compact manifold \(G^4\). Composing with \(V_t\) and using \(\|\nabla^2 V_t\|_{\mathrm{op}}\le M_2(t)\) yields the bound (2.1) with a constant \(C_p\) determined by the chain rule constants for the holonomy map. ∎

For the global action \(A_t=\sum_p A_{t,p}\), the key point is that each link participates in at most \(\nu\) plaquettes.

### Lemma 2.2 (Global Hessian lower bound with incidence factor)

There exists a constant \(C_{\mathrm{hol}}<\infty\), depending only on the plaquette holonomy map for the hypercubic lattice (in particular independent of \(\Lambda\)), such that
\[
\nabla^2 A_t(U)\ \succeq\ -\nu\,C_{\mathrm{hol}}\,M_2(t)\,g_\Lambda(U)
\qquad\forall U\in M_\Lambda.
\tag{2.2}
\]

**Proof.**
Sum the single-plaquette bounds (2.1) over \(p\). In the quadratic form \(\nabla^2A_t(U)(v,v)\), each link-component \(v_\ell\) appears only in the plaquettes \(p\) incident to \(\ell\). The incidence bound \(\#\{p:\ell\in\partial p\}\le \nu\) yields an overall factor \(\nu\). Absorb all holonomy-map constants into \(C_{\mathrm{hol}}\). ∎

---

## 3. Global Bakry–Émery curvature and \(CD(\kappa,\infty)\)

The Bakry–Émery tensor of \(\mu_{\Lambda,t}\) is
\[
\mathrm{Ric}_{\mu_{\Lambda,t}}
=
\mathrm{Ric}_{g_\Lambda}+\nabla^2 A_t.
\tag{3.1}
\]
By (1.1) and the product Ricci bound,
\[
\mathrm{Ric}_{g_\Lambda}\ge \kappa_G g_\Lambda.
\tag{3.2}
\]
Combine with (2.2):
\[
\mathrm{Ric}_{\mu_{\Lambda,t}}
\ \succeq\
\Big(\kappa_G-\nu C_{\mathrm{hol}}M_2(t)\Big)\,g_\Lambda.
\tag{3.3}
\]
Define the global curvature constant
\[
\kappa_{\mathrm{global}}(t):=\kappa_G-\nu C_{\mathrm{hol}}M_2(t).
\tag{3.4}
\]

### Theorem 3.1 (Global \(CD(\kappa_{\mathrm{global}}(t),\infty)\) when \(\kappa_{\mathrm{global}}(t)>0\))

If \(\kappa_{\mathrm{global}}(t)>0\), then for all smooth \(f:M_\Lambda\to\mathbb R\),
\[
\Gamma_2(f)\ge \kappa_{\mathrm{global}}(t)\,\Gamma(f)
\qquad\text{pointwise on }M_\Lambda.
\tag{3.5}
\]
In particular, any functional inequality consequence of \(CD(\kappa,\infty)\) (Poincaré, log-Sobolev, etc.) holds with constants controlled by \(\kappa_{\mathrm{global}}(t)\), uniformly in \(|\Lambda|\).

**Proof.**
(3.5) is an immediate consequence of the Bochner–Bakry–Émery identity and the tensor bound (3.3). ∎

---

## 4. Variants: multiple heat-kernel times

If the action is a sum of plaquette potentials with two times \(t_0,t_1>0\),
\[
A(U)=\sum_{p\in P_0}V_{t_0}(U_p)+\sum_{p\in P_1}V_{t_1}(U_p),
\]
then the same argument yields
\[
\kappa_{\mathrm{global}}
\ \ge\
\kappa_G - \nu C_{\mathrm{hol}}\big(M_2(t_0)+M_2(t_1)\big).
\tag{4.1}
\]

---

## 5. What this template does and does not do

*If \(\kappa_{\mathrm{global}}(t)>0\)*, this route bypasses small-field localization and Lyapunov drift entirely: one has global \(CD(\kappa,\infty)\) on the full configuration manifold.

The unresolved quantitative issue is the behavior of \(M_2(t)\) as \(t\downarrow 0\) (the weak-coupling/continuum regime). The template isolates this as the single analytic quantity that controls whether a global curvature mechanism is available.
