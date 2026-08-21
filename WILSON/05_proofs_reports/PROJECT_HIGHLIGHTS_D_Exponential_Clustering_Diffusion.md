# Project Highlight D: Diffusion covariance representation and exponential clustering (finite volume)

This document extracts the key analytic mechanism from `Part 18C`:

1. A **Helffer–Sjöstrand-type covariance representation** for the reversible diffusion (Langevin) semigroup.
2. A **gradient propagation inequality** driven by (i) on-site convexity and (ii) bounded cross-link interactions.
3. A **finite-volume exponential clustering bound** with an explicit rate
   \[
   \mu = \log\!\Big(\frac{\kappa}{JD}\Big),
   \]
   in the diagonal-dominance regime \(JD<\kappa\).

Throughout, \(G\) is compact and \(\Omega_\Lambda=G^{E(\Lambda)}\) carries the product Haar measure.

---

## D.1. Configuration diffusion generator and Dirichlet form

Let \(\Lambda\subset\mathbb Z^d\) be a finite periodic box and set
\[
\Omega_\Lambda := G^{E(\Lambda)}.
\]

Let \(S_\Lambda:\Omega_\Lambda\to\mathbb R\) be \(C^2\) and define the Gibbs measure
\[
d\mu_\Lambda(U) := Z_\Lambda^{-1}e^{-S_\Lambda(U)}\prod_{\ell\in E(\Lambda)} d\mathrm{Haar}(U_\ell).
\]

Fix an orthonormal basis \(\{X^a\}_{a=1}^{\dim G}\) of \(\mathfrak g\), and let \(X_\ell^a\) denote the corresponding right-invariant vector field acting on link \(\ell\) (trivial on other links).  
Define the link gradient and global gradient:
\[
\nabla_\ell f := (X_\ell^a f)_{a=1}^{\dim G},\qquad
|\nabla_\ell f|^2 := \sum_a (X_\ell^a f)^2,\qquad
|\nabla f|^2 := \sum_{\ell} |\nabla_\ell f|^2.
\]

Define the (overdamped Langevin) generator
\[
L := \sum_{\ell\in E(\Lambda)} \Big(\Delta_\ell - \langle \nabla_\ell S_\Lambda,\ \nabla_\ell(\cdot)\rangle\Big),
\qquad
\Delta_\ell := \sum_a (X_\ell^a)^2.
\]
Then \(L\) is symmetric in \(L^2(\mu_\Lambda)\) and generates a self-adjoint Markov semigroup \(P_t:=e^{tL}\).

The carré du champ is
\[
\Gamma(f,g):=\frac12(L(fg)-fLg-gLf)=\sum_{\ell}\langle\nabla_\ell f,\nabla_\ell g\rangle,
\qquad \Gamma(f):=\Gamma(f,f)=|\nabla f|^2.
\]

**Lemma D.1 (Integration by parts).** For smooth \(f,g\),
\[
\int f\,Lg\,d\mu_\Lambda = -\int \Gamma(f,g)\,d\mu_\Lambda.
\]

---

## D.2. Covariance as an integral of Dirichlet pairings

For \(F,G\in L^2(\mu_\Lambda)\), define
\[
\mathrm{Cov}_{\mu_\Lambda}(F,G)
:=\int (F-\mu_\Lambda F)(G-\mu_\Lambda G)\,d\mu_\Lambda.
\]

Assume \(F,G\) are mean-zero. Define \(h(t):=\langle P_tF, G\rangle_{L^2(\mu_\Lambda)}\).  
Then \(h'(t)=\langle LP_tF,G\rangle\) and Lemma D.1 gives \(h'(t)=-\int\Gamma(P_tF,G)\,d\mu_\Lambda\).

If \(P_tF\to 0\) in \(L^2\) as \(t\to\infty\) (e.g. by a spectral gap), then \(h(t)\to 0\) and we obtain:

**Proposition D.2 (Covariance–Dirichlet representation).**
For mean-zero \(F,G\) in the form domain,
\[
\mathrm{Cov}_{\mu_\Lambda}(F,G)
=
\int_0^\infty \int \Gamma(P_tF,G)\,d\mu_\Lambda\,dt
=
\int_0^\infty \int \langle\nabla P_tF,\nabla G\rangle\,d\mu_\Lambda\,dt.
\]

This identity is the analytic “wire” connecting locality of the dynamics to decay of correlations.

---

## D.3. Locality graph and distance

Define a graph on links \(E(\Lambda)\) by \(\ell\sim\ell'\) if the action contains an interaction involving both \(\ell\) and \(\ell'\) (for Wilson-type actions: if \(\ell,\ell'\) lie on a common plaquette).  
Let \(D\) be a uniform bound on the degree of this graph (independent of \(\Lambda\) on periodic boxes).

For link sets \(A,B\subset E(\Lambda)\), define the graph distance
\[
\mathrm{dist}(A,B):=\min_{\ell\in A,\ell'\in B}\mathrm{dist}(\ell,\ell').
\]

An observable \(F\) is **local** if it depends only on a finite link set \(\mathrm{supp}(F)\); equivalently, \(\nabla_\ell F=0\) for \(\ell\notin\mathrm{supp}(F)\).

---

## D.4. Gradient propagation: convexity + bounded cross-interactions

Write the (linkwise) Hessian blocks of \(S_\Lambda\) in the right-invariant frame:
\[
(\mathrm{Hess}\,S_\Lambda)_{\ell a,\ell' b}(U) := X_\ell^a X_{\ell'}^b S_\Lambda(U).
\]

Assume two quantitative bounds hold **uniformly on a canonical region \(K_\Lambda\subset\Omega_\Lambda\)**:

### (A) On-site convexity
There exists \(\kappa>0\) such that for all \(U\in K_\Lambda\), all links \(\ell\), and all \(v\in\mathbb R^{\dim G}\),
\[
\sum_{a,b} v_a\,(\mathrm{Hess}\,S_\Lambda)_{\ell a,\ell b}(U)\,v_b \;\ge\; \kappa\,|v|^2.
\]

### (B) Bounded cross-link interactions
There exists \(J\ge 0\) such that for all \(U\in K_\Lambda\), for all \(\ell\neq\ell'\),
\[
\sum_{a,b} \big|(\mathrm{Hess}\,S_\Lambda)_{\ell a,\ell' b}(U)\big|\ \le\ J\,\mathbf 1_{\{\ell\sim\ell'\}}.
\]

In the project’s SU(3) Wilson bookkeeping, the cross-link constant is \(J=\beta/3\).

---

### D.4.1. Differential inequality

Under (A)–(B), one obtains a comparison inequality for
\[
u_\ell(t):=\big\|\ |\nabla_\ell P_tF|\ \big\|_{L^\infty(\mu_\Lambda)}.
\]

**Lemma D.3 (Gradient propagation inequality).**  
For \(F\) smooth and for all \(t\ge 0\),
\[
\frac{d}{dt}u_\ell(t)\ \le\ -\kappa\,u_\ell(t) + J\sum_{\ell'\sim \ell}u_{\ell'}(t).
\]

Equivalently, with \(u(t)=(u_\ell(t))_{\ell\in E(\Lambda)}\) and adjacency matrix \(A\),
\[
\dot u(t)\ \le\ -(\kappa I - J A)\,u(t).
\]

This is the analytic place where the “diagonal dominance” condition \(JD<\kappa\) enters.

---

## D.5. Exponential clustering in graph distance

Iterating the propagation inequality along paths yields decay away from \(\mathrm{supp}(F)\). The explicit bookkeeping in the project gives:

**Lemma D.4 (Off-support gradient bound).**  
If \(\ell\notin\mathrm{supp}(F)\) and \(r:=\mathrm{dist}(\ell,\mathrm{supp}(F))\ge 1\), then
\[
u_\ell(t)\ \le\ e^{-\kappa t}\,\frac{(JDt)^r}{r!}\,\|\nabla F\|_{L^\infty}.
\]
In particular,
\[
\int_0^\infty u_\ell(t)\,dt
\ \le\
\frac{1}{\kappa}\,\Big(\frac{JD}{\kappa}\Big)^r\,\|\nabla F\|_{L^\infty}.
\]

Using Proposition D.2 and a support decomposition, one obtains the main correlation decay theorem:

**Theorem D.5 (Finite-volume exponential clustering).**  
Assume:
1. a spectral gap for \(L\) (to justify \(P_tF\to 0\)),
2. the locality bounds (A)–(B) on \(K_\Lambda\),
3. a localization step ensuring the same bounds are effectively valid for \(\mu_\Lambda\).

If \(JD<\kappa\), define
\[
\mu := \log\!\Big(\frac{\kappa}{JD}\Big) >0.
\]
Then for all smooth local observables \(F,G\),
\[
\big|\mathrm{Cov}_{\mu_\Lambda}(F,G)\big|
\;\le\;
\frac{2}{\kappa}\,\|\nabla F\|_{L^\infty}\,\|\nabla G\|_{L^\infty}\,
\exp\!\big(-\mu\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)\big).
\]

---

## D.6. What this theorem is *really* buying you

* It gives exponential decay in **graph distance** with a **uniform exponent** once \(\kappa,J,D\) are uniform in volume.
* Specializing to observables in time-separated slabs gives exponential decay in Euclidean time steps.
* Part 9 (thermodynamic limit) preserves the same exponent.
* Part 10 (OS bridge) converts this to a Hamiltonian gap \(m\gtrsim \mu/a\).

So Theorem D.5 is the functional-analytic engine whose “output constant” is the mass gap after dividing by \(a\).

