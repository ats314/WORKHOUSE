# From Helffer–Sjöstrand to exponential clustering (and an OS gap) on the small-field region

## Overview

This note packages a key “engine” from the project into a single pipeline:

1. **Helffer–Sjöstrand (HS) covariance representation** reduces \(\mathrm{Cov}(F,G)\) to a quadratic form involving the inverse of a **Witten Laplacian** on 1-forms.
2. A **matrix hinge inequality** on a small-field region \(K_\Lambda(r)\) bounds that Witten Laplacian from below by a **massive discrete Maxwell operator**
   \[
   M\ :=\ m_{\mathrm H}^2 I\ +\ \alpha\, d_1^\*d_1.
   \]
3. A **Combes–Thomas estimate** for \(M^{-1}\) yields exponential decay of its kernel in the link graph distance.
4. This gives **exponential clustering** (at fixed cutoff) for the Gibbs state conditioned on \(K_\Lambda(r)\), and by standard OS/reflection-positivity arguments, a corresponding **Hamiltonian spectral gap** (at fixed lattice spacing).

The method is “geometric” in the sense that the scalar mass floor \(m_{\mathrm H}^2\) arises from the Ricci curvature of the compact gauge group (the “Haar mass”).

---

## 1. Setup

Let \(\Lambda\subset\mathbb Z^d\) be a finite periodic lattice.
Let \(E(\Lambda)\) be oriented links, \(P(\Lambda)\) plaquettes, and \(U\in G^{E(\Lambda)}\) a configuration.

Let the Wilson action be
\[
S_\Lambda(U) := \beta \sum_{p\in P(\Lambda)}\vartheta(U_p(U)),
\qquad
\vartheta(g):=1-\frac1n\Re\operatorname{Tr}(\rho(g)).
\]
Define the Gibbs measure
\[
\mu_{\Lambda,\beta}(dU)\ \propto\ e^{-S_\Lambda(U)}\,dU.
\]

Let \(M_\Lambda:=G^{E(\Lambda)}\) with its product bi-invariant metric, and write \(\nabla\) for the Riemannian gradient on \(M_\Lambda\).

---

## 2. Small-field region and the “massive Maxwell” operator

Define a small-field event \(K_\Lambda(r)\) by requiring all plaquette holonomies to stay within distance \(r\) of the identity:
\[
K_\Lambda(r):=\{U:\ z_p(U):=d_G(U_p(U),e)\le r\ \ \forall p\in P(\Lambda)\}.
\]

On \(K_\Lambda(r)\) the project establishes a **matrix hinge inequality**:
there exist constants \(m_{\mathrm H}^2>0\) and \(\alpha>0\) (depending on \(G,d,\rho,\beta\) but *not* on \(|\Lambda|\)) such that
\[
\mathrm{Ric}_{M_\Lambda} + \mathrm{Hess}\,S_\Lambda(U)
\ \succeq\
m_{\mathrm H}^2\,I + \alpha\,d_1^\*d_1,
\qquad U\in K_\Lambda(r).
\tag{2.1}
\]
Here \(d_1:\mathcal C^1(\Lambda;\mathfrak g)\to \mathcal C^2(\Lambda;\mathfrak g)\) is the coboundary operator and \(d_1^\*\) its adjoint.

The constant \(m_{\mathrm H}^2\) is sourced by the uniform Ricci lower bound on \(G\) (the “Haar mass”).

Define the operator
\[
M := m_{\mathrm H}^2\,I + \alpha\,d_1^\*d_1
\quad\text{acting on }\mathcal C^1(\Lambda;\mathfrak g)
\ \cong\ \ell^2(E(\Lambda);\mathfrak g).
\tag{2.2}
\]

---

## 3. Helffer–Sjöstrand representation and conditional covariance bound

Let \(\mu^K\) denote \(\mu_{\Lambda,\beta}\) restricted to \(K_\Lambda(r)\) and normalized.
Equip \(K_\Lambda(r)\) with a reflecting/Neumann generator \(L^K\) that is reversible w.r.t. \(\mu^K\).
Let \(\mathcal L^{(1)}_K\) be the associated Witten Laplacian acting on 1-forms.

The HS identity (for smooth \(F,G\) with \(\mu^K(G)=0\)) reads
\[
\mathrm{Cov}_{\mu^K}(F,G)
=
\int_{K_\Lambda(r)}\Big\langle \nabla F,\ (\mathcal L_K^{(1)})^{-1}\nabla G\Big\rangle\,d\mu^K.
\tag{3.1}
\]

The Bochner–Weitzenböck decomposition implies \(\mathcal L_K^{(1)}\succeq \mathrm{Ric}_{\mu}(U)\) pointwise, and (2.1) yields \(\mathcal L_K^{(1)}\succeq M\) on \(K_\Lambda(r)\).
By inverse order reversal, \((\mathcal L_K^{(1)})^{-1}\preceq M^{-1}\), so (3.1) gives the **conditional covariance bound**
\[
\boxed{
\mathrm{Cov}_{\mu^K}(F,G)
\ \le\
\int_{K_\Lambda(r)} \big\langle \nabla F,\ M^{-1}\nabla G\big\rangle\,d\mu^K.
}
\tag{3.2}
\]

If \(F,G\) are gauge-invariant, one may project gradients horizontally throughout; this does not affect the argument.

---

## 4. Turning (3.2) into an explicit distance decay

Let \(A,B\subset E(\Lambda)\) be two edge sets.
Say \(F\) is \(A\)-local if it depends only on \(\{U_\ell:\ell\in A\}\), and similarly \(G\) is \(B\)-local.

Then \(\nabla_\ell F\equiv 0\) for \(\ell\notin A\), and \(\nabla_{\ell'}G\equiv 0\) for \(\ell'\notin B\).
Writing the quadratic form in coordinates gives
\[
\mathrm{Cov}_{\mu^K}(F,G)
\ \le\
\sum_{\ell\in A}\sum_{\ell'\in B}
\int_{K_\Lambda(r)}
\big\langle \nabla_\ell F,\ (M^{-1})_{\ell\ell'}\,\nabla_{\ell'}G\big\rangle\,d\mu^K.
\tag{4.1}
\]
Bounding \(\|\nabla_\ell F\|\le \|\nabla_\ell F\|_\infty\) and similarly for \(G\), we obtain
\[
|\mathrm{Cov}_{\mu^K}(F,G)|
\ \le\
\sum_{\ell\in A}\sum_{\ell'\in B}
\|\nabla_\ell F\|_\infty\,\|\nabla_{\ell'}G\|_\infty\,
\bigl\|(M^{-1})_{\ell\ell'}\bigr\|_{\mathrm{op}}.
\tag{4.2}
\]

### Combes–Thomas decay for \(M^{-1}\)

The operator \(M\) has **finite range** on the link graph: \((d_1^\*d_1)_{\ell\ell'}\neq 0\) only if \(\ell,\ell'\) lie in a common plaquette (or are equal), so the range \(R\) is a lattice constant.
Moreover, since \(M\succeq m_{\mathrm H}^2 I\), its diagonal positivity is \(a_0=m_{\mathrm H}^2\).
A uniform bound on the off-diagonal row sums is
\[
B \ \lesssim\ \alpha\,D,
\tag{4.3}
\]
where \(D\) is a bounded-degree constant for the link adjacency induced by plaquettes (depends only on \(d\)).

Applying the abstract Combes–Thomas theorem to \(M\) yields: there exist constants \(C_{\mathrm{CT}},m_{\mathrm{CT}}>0\) (independent of \(|\Lambda|\)) such that
\[
\bigl\|(M^{-1})_{\ell\ell'}\bigr\|_{\mathrm{op}}
\ \le\
C_{\mathrm{CT}}\ e^{-m_{\mathrm{CT}}\, d_E(\ell,\ell')}.
\tag{4.4}
\]

Combining (4.2) and (4.4), and using \(d_E(\ell,\ell')\ge \operatorname{dist}_E(A,B)\) for \(\ell\in A,\ell'\in B\), gives the **exponential clustering bound**
\[
\boxed{
|\mathrm{Cov}_{\mu^K}(F,G)|
\ \le\
C(F,G)\ e^{-m_{\mathrm{CT}}\,\operatorname{dist}_E(A,B)},
}
\tag{4.5}
\]
where \(C(F,G):=C_{\mathrm{CT}}\bigl(\sum_{\ell\in A}\|\nabla_\ell F\|_\infty\bigr)\bigl(\sum_{\ell'\in B}\|\nabla_{\ell'}G\|_\infty\bigr)\).

---

## 5. Explicit exponent (one convenient form)

With the Combes–Thomas constant from the abstract lemma, one may take
\[
m_{\mathrm{CT}}
=
\frac1R\log\!\Bigl(1+\frac{m_{\mathrm H}^2}{2B}\Bigr)
\ \gtrsim\
\frac1R\log\!\Bigl(1+\frac{m_{\mathrm H}^2}{C\,\alpha}\Bigr),
\tag{5.1}
\]
with \(C\) depending only on the bounded-degree geometry.

In the project’s normalization one often has \(\alpha \propto \beta\), so \(m_{\mathrm{CT}}\) behaves like
\[
m_{\mathrm{CT}} \asymp \log\!\Bigl(1+\frac{c_{\mathrm H}}{C\,\beta}\Bigr)
\quad(\text{up to fixed lattice constants}).
\tag{5.2}
\]

---

## 6. From Euclidean-time clustering to an OS Hamiltonian gap

Let \(\theta\) be reflection in the OS plane and \(F\) an observable supported in the positive-time half-lattice.
Under reflection positivity, one has the spectral representation
\[
\langle F,\theta F\rangle_{\mu} = \sum_{n\ge 0} |\langle n|F\rangle|^2\, e^{-E_n t},
\]
where \(t\) is the time-separation and \(E_n\) are spectrum values of the OS Hamiltonian.

A bound of the form
\[
|\mathrm{Cov}_{\mu}(F,\theta F)| \le C(F)\,e^{-m t}
\]
forces \(E_1\ge m\), i.e. a **spectral gap** of at least \(m\).
At fixed lattice spacing \(a\), this gap is typically reported as
\[
m_{\mathrm{OS}} = \frac{m}{a}.
\]

In the project, (4.5) yields such a decay on the small-field region \(K_\Lambda(r)\); the remaining step is to control the contribution of \(K_\Lambda(r)^{c}\) via a localization/typicality decomposition (handled in a separate note).

---

## 7. What remains outside the small-field region

The pipeline above proves exponential clustering for the **conditioned** measure \(\mu^K\).

To upgrade to the full Gibbs state \(\mu_{\Lambda,\beta}\) one needs:

- a decomposition of covariances across the event \(K_\Lambda(r)\),
- a bound on \(\mu_{\Lambda,\beta}(K_\Lambda(r)^c)\) strong enough not to spoil the distance exponent.

These are precisely the “typicality/localization” and “force non-cancellation” gaps tracked elsewhere in the project.
