# Davies-type exponential decay for the massive Maxwell Green kernel

> **Goal.** Package the Part-9 “Davies method” decay mechanism into a self-contained statement and proof,
> and record two refinements that look *actually useful* downstream:
> (i) replacing the crude degree constant by a **row-sum constant** \(C_0\), and
> (ii) a **boundary refinement** \(C_\partial\) for level-set truncations.

---

## 1. Setup

Let \(\mathcal G=(\mathcal V,\mathcal E)\) be a finite undirected graph with graph distance \(\mathrm{dist}_{\mathcal E}(\cdot,\cdot)\).
Let \(\ell^2(\mathcal E^+)\) denote oriented-edge functions, with the convention that we work on a fixed choice of one
orientation per unoriented edge.

Let \(\Delta_1=d_1^\* d_1\) be the (combinatorial) **\(1\)-form Laplacian** (the “curl--curl” operator on edges).
Fix parameters \(\alpha>0\) and \(m>0\), and define the massive Maxwell operator
\[
M \;=\; m^2 I + \alpha\,\Delta_1.
\]
Let
\[
G \;=\; M^{-1}
\]
denote its Green kernel on \(\ell^2(\mathcal E^+)\), i.e. \(G(b,b')=\langle \delta_b, M^{-1}\delta_{b'}\rangle\).

We write \(D_{\mathcal E}\) for the maximal degree of the **edge graph** (links are vertices; two links adjacent
if they share an endpoint in \(\mathcal G\)).

---

## 2. Davies-type decay (degree version)

### Proposition 2.1 (Davies-type decay with \(D_{\mathcal E}\))

Assume \(M=m^2 I+\alpha \Delta_1\) with \(m>0\), \(\alpha>0\). Then for all oriented edges \(b,b'\in\mathcal E^+\),
\[
|G(b,b')| \;\le\; \frac{2}{m^2}\exp\!\Big(-\eta_M\,\mathrm{dist}_{\mathcal E}(b,b')\Big),
\]
where
\[
\eta_M \;=\; \cosh^{-1}\!\Big(1+\frac{m^2}{2\alpha D_{\mathcal E}}\Big)
\;=\;2\sinh^{-1}\!\Big(\frac{m}{2\sqrt{\alpha D_{\mathcal E}}}\Big).
\]

### Proof (Davies twist + quadratic-form control)

Pick a reference edge \(b_0\) and define a 1-Lipschitz “height function”
\[
h(b) \;=\; \mathrm{dist}_{\mathcal E}(b,b_0).
\]
For \(\theta\in\mathbb R\), define a multiplication operator
\[
(T_\theta f)(b) = e^{\theta h(b)} f(b),\qquad f\in \ell^2(\mathcal E^+).
\]
Conjugate \(M\) by \(T_\theta\):
\[
M_\theta := T_\theta M T_{-\theta} = m^2 I + \alpha\,T_\theta \Delta_1 T_{-\theta}.
\]
The key point is that \(M_\theta\) is no longer self-adjoint, but its **numerical range** can still be controlled
through the quadratic form of \(\Delta_1\).

Write \(\Delta_1\) as a finite-range operator with coefficients \(K_{\Delta_1}(b,b')\) supported on
\(\mathrm{dist}_{\mathcal E}(b,b')\le 1\).
Then
\[
(T_\theta \Delta_1 T_{-\theta} f)(b)
=\sum_{b'} K_{\Delta_1}(b,b')\,e^{\theta(h(b)-h(b'))} f(b').
\]
Since \(h\) is 1-Lipschitz on the edge graph, \(|h(b)-h(b')|\le 1\) whenever \(K_{\Delta_1}(b,b')\neq 0\), hence
\(|e^{\theta(h(b)-h(b'))}|\le e^{|\theta|}\).

A standard Davies estimate (equivalently: bounding the antisymmetric part of the conjugated operator in the
form sense) gives, for any \(f\),
\[
\Re\langle f, M_\theta f\rangle
\;\ge\; m^2\|f\|^2 + \alpha\,\langle f,\Delta_1 f\rangle - \alpha\,D_{\mathcal E}\,\big(\cosh\theta-1\big)\,\|f\|^2.
\]
The constant \(D_{\mathcal E}\) enters via the worst-case count of neighbors in the edge graph.

Therefore,
\[
\Re\langle f, M_\theta f\rangle \;\ge\;
\Big(m^2 - \alpha D_{\mathcal E}(\cosh\theta-1)\Big)\|f\|^2.
\]
Choose \(\theta\ge 0\) so that
\[
\alpha D_{\mathcal E}(\cosh\theta-1)=\frac{m^2}{2},
\]
i.e.
\[
\cosh\theta = 1+\frac{m^2}{2\alpha D_{\mathcal E}},
\qquad \theta=\eta_M.
\]
Then \(\Re\langle f, M_{\eta_M} f\rangle \ge \frac{m^2}{2}\|f\|^2\), which implies the resolvent bound
\[
\|M_{\eta_M}^{-1}\|\;\le\;\frac{2}{m^2}.
\]

Now use
\[
G(b,b')=\langle \delta_b, M^{-1}\delta_{b'}\rangle
=\langle T_{\eta_M}\delta_b,\, M_{\eta_M}^{-1}\,T_{\eta_M}\delta_{b'}\rangle.
\]
But \(T_{\eta_M}\delta_b = e^{\eta_M h(b)}\delta_b\), so
\[
|G(b,b')|
\le \|M_{\eta_M}^{-1}\|\,e^{\eta_M(h(b)-h(b'))}
\le \frac{2}{m^2}\,e^{-\eta_M\mathrm{dist}_{\mathcal E}(b,b')},
\]
since \(h(b)-h(b')\ge -\mathrm{dist}_{\mathcal E}(b,b')\).
\(\square\)

---

## 3. Why Davies beats Combes--Thomas here

A Combes--Thomas (CT) resolvent bound typically gives an exponent of the form
\[
\eta_{\mathrm{CT}} \sim \log\!\Big(1+\frac{m^2}{\alpha\,\text{(connectivity)}}\Big),
\]
which is \(\sim m^2\) for small \(m\).
Davies’ method is **semigroup-informed** and produces an exponent scaling like \(\sim m\) for small \(m\),
matching the physically expected massive decay rate (up to lattice geometry factors).

This distinction matters: it is exactly the difference between “a mass gap exists” and “the bound actually
tracks the mass parameter.”

---

## 4. Refinement: replace \(D_{\mathcal E}\) by a row-sum constant \(C_0\)

The degree \(D_{\mathcal E}\) only knows adjacency, not coefficient sizes.
For finite-range operators with anisotropic stencils, a better constant is:

### Definition 4.1 (row-sum constant)
For \(\Delta_1\) with kernel \(K_{\Delta_1}(b,b')\), define
\[
C_0(\Delta_1)
:=\sup_{b}\sum_{b'\neq b} |K_{\Delta_1}(b,b')|.
\]

### Proposition 4.2 (Davies decay with \(C_0\))
Under the same assumptions,
\[
|G(b,b')|\le \frac{2}{m^2}\exp\!\Big(-\eta_{C_0}\,\mathrm{dist}_{\mathcal E}(b,b')\Big),
\qquad
\eta_{C_0}= \cosh^{-1}\!\Big(1+\frac{m^2}{2\alpha C_0(\Delta_1)}\Big).
\]

*Proof sketch.* Repeat Proposition 2.1 but bound the conjugation error by the **sum of absolute off-diagonal
coefficients** rather than “count of neighbors.” \(\square\)

---

## 5. Boundary refinement: \(C_\partial\) for level-set restrictions

If one localizes to a region \(\mathcal S\subset\mathcal E^+\) (e.g. a level-set of \(h\)), then only neighbors that
cross the boundary matter.

### Definition 5.1 (boundary row-sum constant)
For a subset \(\mathcal S\subset\mathcal E^+\), define
\[
C_\partial(\mathcal S)
:=\sup_{b\in\mathcal S} \sum_{b'\notin\mathcal S} |K_{\Delta_1}(b,b')|.
\]

### Corollary 5.2 (boundary version)
In the Davies argument with a cutoff \(h\le R\), the constant \(C_0(\Delta_1)\) can be replaced by
\(C_\partial(\{h\le R\})\) in the off-diagonal error term.

*Interpretation.* If the stencil is highly anisotropic, the *outward* couplings at the boundary can be
substantially smaller than the full row-sum. That can sharpen localized resolvent bounds used in
covariance decompositions.

---

## 6. Immediate “research handles”

1. **Gauge-fixing and cancellations.** For Maxwell-type operators, taking absolute values destroys
   cancellations. That suggests: prove decay for a *gauge-fixed* operator where the stencil collapses,
   then lift to gauge-invariant observables (see the companion note on the Hodge Laplacian).

2. **Continuum limit narrative.** The \(m\)-scaling in \(\eta_M\) is the right “mass-gap heuristic” for
   passing to a continuum statement: the discrete kernel already has the physically correct exponent.

3. **Boundary constants in multiscale expansions.** \(C_\partial\) is the natural constant in block-spin
   decompositions where you only pay for boundary-crossing interactions.

---
