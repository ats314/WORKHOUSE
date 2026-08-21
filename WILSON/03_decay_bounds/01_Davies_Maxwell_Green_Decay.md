# Davies/Combes–Thomas decay for the massive Maxwell $1$-form Green kernel

This note extracts and streamlines the **Part 9** estimate:
an explicit exponential off-diagonal bound for the inverse of a massive Maxwell operator on lattice $1$-forms,
proved via **Davies/Combes–Thomas conjugation**.
The bound is uniform in volume and sharp enough (in exponent scaling) to plug into exponential clustering arguments.

---

## 1. Setup

Let $\Lambda=(\mathbb Z/L\mathbb Z)^d$ with $d=4$ (though the argument is dimension-agnostic).
Let $C^1(\Lambda)$ denote real-valued $1$-forms on oriented links, equipped with the standard $\ell^2$ inner product.
Let $d_1:C^1\to C^2$ be the lattice exterior derivative on $1$-forms and $d_1^*$ its adjoint.

Fix $m^2>0$ and $\alpha>0$ and define the Maxwell-type operator on $1$-forms
\[
M \;=\; m^2 I \;+\; \alpha\, d_1^* d_1 .
\]
Let $G = M^{-1}$ denote the Green operator (matrix elements $G(b,b')$ in the link basis).

---

## 2. The link-graph distance and a degree constant

Define a graph on links: two links are adjacent if they co-bound a plaquette.
Let $\mathrm{dist}_E(b,b')$ be the graph distance on this link graph.
Let $D_E$ be the maximum degree of this link graph.

---

## 3. Main bound (Proposition 9.X)

**Proposition (Davies-type decay for massive Maxwell kernel).**  
For all links $b,b'$,
\[
|G(b,b')|
\;\le\;
\frac{2}{m^2}\,\exp\!\bigl(-\eta_{\mathrm{DG}}\;\mathrm{dist}_E(b,b')\bigr),
\]
where the decay exponent can be chosen explicitly as
\[
\eta_{\mathrm{DG}}
\;=\;
\operatorname{arcosh}\!\Bigl(1+\frac{m^2}{2\alpha D_E}\Bigr)
\;=\;
2\,\operatorname{arsinh}\!\Bigl(\frac{m}{2\sqrt{\alpha D_E}}\Bigr).
\]

A stronger exponent arises from the sharp Combes–Thomas condition:
\[
\eta_{\mathrm{CT}}
\;=\;
\operatorname{arcosh}\!\Bigl(1+\frac{m^2}{\alpha D_E}\Bigr)
\;\ge\;
\eta_{\mathrm{DG}}.
\]

---

## 4. Proof idea (Davies conjugation in one page)

Pick a base link $b_0$ and set $\rho(b)=\mathrm{dist}_E(b,b_0)$.
For $\eta\ge 0$ define the conjugated operator
\[
M_\eta \;:=\; e^{\eta\rho} M e^{-\eta\rho}
\;=\;
m^2 I \;+\; \alpha\, e^{\eta\rho}(d_1^*d_1)e^{-\eta\rho}.
\]

Let $\Delta_1:=d_1^*d_1$ (the $1$-form Laplacian).
One shows that conjugation perturbs $\Delta_1$ by an off-diagonal operator $Q$ whose symmetric part is bounded below:
\[
\frac{Q+Q^*}{2} \;\ge\; -2D_E(\cosh\eta -1)\,I.
\]
Equivalently,
\[
M_\eta \;\ge\; \Bigl(m^2 - 2\alpha D_E(\cosh\eta -1)\Bigr) I.
\]
Choosing $\eta$ so that
\[
m^2 > 2\alpha D_E(\cosh\eta -1)
\]
gives a uniform bound on $\|M_\eta^{-1}\|$.

Now relate $G(b,b_0)$ to $M_\eta^{-1}$:
\[
|G(b,b_0)|
=
\bigl| \langle \delta_b,\, M^{-1}\delta_{b_0}\rangle \bigr|
=
e^{-\eta\rho(b)}\bigl| \langle \delta_b,\, M_\eta^{-1}\delta_{b_0}\rangle \bigr|
\le
e^{-\eta\rho(b)} \,\|M_\eta^{-1}\|.
\]

Optimizing $\eta$ at the boundary of the positivity condition yields the closed form exponent $\eta_{\mathrm{DG}}$ above.

---

## 5. Local-constant refinements: $C_0$ and $C_{\partial}$

The degree bound $D_E$ is deliberately crude.
Two refinements replace it by operator-dependent row-sum constants of the $1$-form Laplacian $\Delta_1$:

### 5.1 Global row-sum constant
Define
\[
C_0(\Delta_1)
:= \max_{b}\sum_{b'\neq b}|\Delta_1(b,b')|.
\]
Repeating the argument with $C_0$ in place of $D_E$ improves the exponent whenever $\Delta_1$ has cancellations or sparser effective coupling than the worst-case link graph.

### 5.2 Boundary-local constant
Given a region $\Omega$ of links and its boundary $\partial\Omega$,
define
\[
C_\partial(\Delta_1;\Omega)
:= \max_{b\in\partial\Omega}\sum_{b'\notin\Omega}|\Delta_1(b,b')|.
\]
In localized bounds (e.g. when proving decay from a set to its complement),
$C_\partial$ can be much smaller than $C_0$, yielding stronger decay rates inside $\Omega$.

This is useful in “good/bad set” decompositions where $\Omega$ is the good region.

---

## 6. Why this matters (conceptual)

The exponent $\eta$ scales like $\mathcal O(m)$ for small $m$ (since $\operatorname{arsinh}(x)\sim x$),
which is the correct scaling for massive theories.
Many naive graph resolvent bounds give only $\mathcal O(m^2)$, too weak to close clustering estimates uniformly.

The $C_\partial$ refinement is a clean interface between **global spectral estimates** and **localized probabilistic decompositions**.
