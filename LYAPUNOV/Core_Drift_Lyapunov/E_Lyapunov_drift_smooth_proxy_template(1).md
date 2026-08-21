# A Lyapunov drift template with a globally smooth plaquette “badness” proxy

This note isolates an analytic design pattern that appears repeatedly in the project:

* globalizing a local curvature/functional inequality requires a Lyapunov drift estimate with **volume-uniform** constants;
* distance-squared on a compact Lie group, \(d_G(g,e)^2\), is not globally smooth (cut locus), and its second derivatives are hard to control uniformly;
* a globally smooth, conjugation-invariant proxy such as
  \[
  \widetilde z(g):=1-\frac1N\mathrm{ReTr}(g)
  \quad (g\in \mathrm{SU}(N))
  \tag{1.1}
  \]
  avoids the cut-locus obstruction because it is \(C^\infty\) on the compact manifold \(G\).

This note does **not** prove a full drift inequality for lattice Yang–Mills. It records:

1. the exact drift formula for \(W=\exp(\eta V)\) under a gradient diffusion generator,  
2. the point where a naive choice produces an \(O(|P(\Lambda)|)\) leakage term, and  
3. a structural fix (already suggested in the project chat): choose \(V\) so that the Laplacian/Hessian leakage is **weighted by \(\widetilde z_p\)** rather than producing a volume-proportional constant.

---

## 1. Generator and chain rules

Let \(M_\Lambda=G^{E(\Lambda)}\) with product metric. Let \(\mu_\Lambda(\mathrm dU)\propto e^{-S_\Lambda(U)}\mathrm{vol}(\mathrm dU)\) and define the reversible diffusion generator
\[
L f = \Delta f - \langle \nabla S_\Lambda,\nabla f\rangle.
\tag{1.2}
\]
Let \(\Gamma(f)=|\nabla f|^2\). Then for any \(C^2\) scalar function \(\Psi:\mathbb R\to\mathbb R\),
\[
L(\Psi(f))=\Psi'(f)\,Lf+\Psi''(f)\,\Gamma(f),
\qquad
\Gamma(\Psi(f))=(\Psi'(f))^2\Gamma(f).
\tag{1.3}
\]

---

## 2. Lyapunov test function of exponential type

Let \(V:M_\Lambda\to\mathbb R\) be \(C^2\), and set
\[
W:=e^{\eta V},
\qquad \eta>0.
\tag{2.1}
\]
Apply (1.3) with \(\Psi(x)=e^{\eta x}\) to obtain the exact identity
\[
\frac{LW}{W}
=
\eta\,LV+\eta^2\,\Gamma(V).
\tag{2.2}
\]

Thus, a drift inequality of the type
\[
LW \le (-c\,\mathcal D + b)\,W
\tag{2.3}
\]
reduces to producing **upper bounds** for \(LV\) and \(\Gamma(V)\) in terms of a coercive functional \(\mathcal D\), with constants uniform in \(\Lambda\).

---

## 3. Plaquette-based choice of \(V\) and the “leakage” mechanism

Fix a nonnegative plaquette function \(z:G\to[0,\infty)\) with \(z(e)=0\), and define
\[
V(U):=\sum_{p\in P(\Lambda)} \Phi(z(U_p(U))),
\tag{3.1}
\]
where \(\Phi:[0,\infty)\to[0,\infty)\) is \(C^2\).

By linearity and (1.3),
\[
LV
=
\sum_{p}\Big(\Phi'(z_p)\,Lz_p+\Phi''(z_p)\,\Gamma(z_p)\Big),
\qquad
z_p:=z(U_p(U)).
\tag{3.2}
\]
Also,
\[
\Gamma(V)=\Big|\sum_p \Phi'(z_p)\nabla z_p\Big|^2.
\tag{3.3}
\]

### 3.1 The naive issue

If one uses \(z(g)=d_G(g,e)^2\), then \(z\) is not globally smooth and \(\sup|\nabla^2 z|\) is not controlled on all of \(G\). Even if one replaces it by a smooth proxy, a second issue appears:

*Even for smooth \(z\), \(Lz_p\) contains a Laplacian term \(\Delta z_p\), and \(\sup|\Delta z_p|\) is a constant, but summing it over all plaquettes produces an \(O(|P(\Lambda)|)\) term.*

This is the “leakage” of a volume-proportional constant into \(LW/W\).

---

## 4. Smooth proxy \(z(g)=1-\frac1N\mathrm{ReTr}(g)\) and bounded derivatives

Let \(G=\mathrm{SU}(N)\) and define
\[
\widetilde z(g):=1-\frac1N\mathrm{ReTr}(g).
\tag{4.1}
\]
Then:

* \(\widetilde z\ge 0\) and \(\widetilde z(e)=0\).
* \(\widetilde z\) is conjugation-invariant (a class function).
* \(\widetilde z\in C^\infty(G)\) since \(\mathrm{ReTr}\) is smooth.

### Lemma 4.1 (Uniform derivative bounds)

For each \(k\ge 0\) there exists \(C_k<\infty\) such that
\[
\sup_{g\in G} \|\nabla^k \widetilde z(g)\| \le C_k.
\tag{4.2}
\]

**Proof.**
\(\widetilde z\) is \(C^\infty\) on the compact manifold \(G\), hence all covariant derivatives \(\nabla^k \widetilde z\) are continuous and attain their maxima. ∎

Consequently, for each plaquette observable \(\widetilde z_p(U):=\widetilde z(U_p(U))\), all linkwise first and second derivatives are uniformly bounded (the holonomy map \(U\mapsto U_p\) is smooth and depends on finitely many links).

This removes the cut-locus obstruction and supplies uniform bounds on terms like \(X_\ell^aX_\ell^a \widetilde z_p\).

---

## 5. Weighting away the \(O(|P|)\) constant by choosing \(\Phi'(0)=0\)

A structural fix suggested in the project chat is:

*Choose \(\Phi\) so that \(\Phi'(0)=0\), e.g. \(\Phi(s)=s^2\).*

Then \(\Phi'(s)\) carries an extra factor of \(s\) near \(0\), and the potentially dangerous Laplacian term in (3.2)
\[
\sum_{p}\Phi'(z_p)\,\Delta z_p
\tag{5.1}
\]
is **weighted by \(z_p\)** near the vacuum, instead of producing a uniform constant per plaquette.

Concretely, if \(|\Delta z_p|\le C\) uniformly and \(\Phi'(s)\le C' s\) for small \(s\) (which holds for \(\Phi(s)=s^2\) globally: \(\Phi'(s)=2s\)), then
\[
\big|\Phi'(z_p)\Delta z_p\big|
\le (C C')\,z_p.
\tag{5.2}
\]
Summing yields \(\sum_p z_p\), an “energy-like” quantity, rather than \(|P(\Lambda)|\).

This does not by itself prove a global drift inequality; it changes the algebra so that the only surviving extensive quantity is an explicit energy functional that can plausibly be controlled by the Gibbs weight.

---

## 6. What a full Lyapunov inequality would still need

To turn (2.2) into a uniform drift inequality, one must still prove **for the chosen \(V\)**:

1. a coercive lower bound: \(\mathcal D(U)\gtrsim \sum_p z_p(U)\) (or \(\sum_p z_p(U)^2\)),  
2. an upper drift estimate: \(LV \le -c\,\mathcal D + b\) with \(c,b\) independent of \(\Lambda\),  
3. a control of \(\Gamma(V)\) that can be absorbed into the \(-c\mathcal D\) term by choosing \(\eta\) small enough.

The key point of this note is that choosing the smooth proxy \(\widetilde z\) and a nonlinearity with \(\Phi'(0)=0\) makes the “worst” second-derivative contributions appear multiplied by \(\widetilde z_p\), which is the correct algebraic shape to avoid automatic \(|P(\Lambda)|\) leakage in \(LW/W\).
