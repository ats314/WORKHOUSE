# Lattice Yang–Mills: Haar Mass Term, Hessian Structure, and Transfer-Matrix Gap

> **Purpose.** Extract the lattice-level derivations that the project treats as the “rigorous core”:  
> (i) a Haar-measure–induced quadratic term, (ii) a Hessian decomposition with a uniform positive shift, and (iii) a transfer-matrix spectral-gap consequence at fixed lattice spacing \(a\).

---

## 1. Setup

Let \(G=\mathrm{SU}(N)\) and consider a finite hypercubic lattice with link set \(B\) and plaquette set \(P\).

A configuration is \(U=(U_\ell)_{\ell\in B}\in \mathcal{C}=G^{|B|}\), with product Haar measure
\[
d\mu_{\mathrm{Haar}}(U) = \prod_{\ell\in B} d\mu_H(U_\ell).
\]

The Wilson action is
\[
S_W(U) = \beta \sum_{p\in P}\left(1-\frac{1}{N}\mathrm{Re}\,\mathrm{Tr}\,U_p\right),
\]
where \(U_p\) is the ordered product around plaquette \(p\).

The lattice Yang–Mills measure is
\[
d\mu_{\mathrm{YM}}(U) = Z^{-1}e^{-S_W(U)}\, d\mu_{\mathrm{Haar}}(U).
\]

---

## 2. Haar measure in exponential coordinates

### 2.1 Exponential chart on a single link
Near the identity, write
\[
U_\ell = \exp(iA_\ell),\qquad A_\ell\in\mathfrak{su}(N).
\]
The Haar measure on \(G\) in exponential coordinates takes the form
\[
d\mu_H(U) = J(A)\, dA,
\]
where \(dA\) is Lebesgue measure on \(\mathfrak{su}(N)\) in some fixed identification \(\mathfrak{su}(N)\cong\mathbb{R}^{N^2-1}\), and \(J(A)\) is the Jacobian determinant.

Define the “measure action”
\[
S_{\mathrm{Haar}}(A):= -\log J(A).
\]

### 2.2 Root-product formula and small-field expansion
A standard Lie-theoretic expression is
\[
J(A) = \prod_{\alpha>0}\left(\frac{\sin(\alpha(A)/2)}{\alpha(A)/2}\right)^{2},
\]
for a choice of invariant inner product where long roots have length squared \(2\).

Taylor expand for small \(x\):
\[
\log\left(\frac{\sin(x/2)}{x/2}\right) = -\frac{x^2}{24} + O(x^4).
\]
Therefore,
\[
\log J(A)
= 2\sum_{\alpha>0}\left(-\frac{\alpha(A)^2}{24} + O(\alpha(A)^4)\right)
= -\frac{1}{12}\sum_{\alpha>0}\alpha(A)^2 + O(\|A\|^4).
\]
Thus,
\[
S_{\mathrm{Haar}}(A)= -\log J(A)= \frac{1}{12}\sum_{\alpha>0}\alpha(A)^2 + O(\|A\|^4).
\]

Using the identity (for a simple Lie algebra)
\[
\sum_{\alpha>0}\alpha\otimes \alpha = h^\vee \, \mathrm{Id},
\]
we obtain
\[
\sum_{\alpha>0}\alpha(A)^2 = h^\vee\,\langle A,A\rangle,
\]
hence
\[
S_{\mathrm{Haar}}(A)=\frac{h^\vee}{12}\,\langle A,A\rangle + O(\|A\|^4).
\]
For \(G=\mathrm{SU}(N)\), the dual Coxeter number is \(h^\vee=N\). So the local quadratic coefficient is \(N/12\) with respect to the chosen invariant form \(\langle\cdot,\cdot\rangle\).

> **Normalization note.** The project uses a coefficient written as
> \[
> S_{\mathrm{Haar}}(A)=\frac{c_0}{2}\mathrm{Tr}(A^2)+O(A^4),
> \qquad c_0=\frac{N^2-1}{2N}.
> \]
> This can be reconciled with the root-form expansion by tracking the specific trace/inner-product convention used for \(\mathrm{Tr}(A^2)\).

### 2.3 The “Haar mass coefficient” as used in the project
We record the project’s preferred coefficient as a definition:

**Definition (Haar mass coefficient).**
\[
c_0 := \frac{N^2-1}{2N}.
\]
Then the Haar contribution on a link is written
\[
S_{\mathrm{Haar}}(A_\ell) = \frac{c_0}{2}\mathrm{Tr}(A_\ell^2)+O(A_\ell^4).
\]

On the full lattice,
\[
S_{\mathrm{Haar}}(A)=\sum_{\ell\in B} S_{\mathrm{Haar}}(A_\ell)
= \frac{c_0}{2}\sum_{\ell\in B}\mathrm{Tr}(A_\ell^2)+O(\|A\|^4).
\]

---

## 3. Hessian structure for the effective action

Define
\[
S_{\mathrm{eff}}(U) := S_W(U) + S_{\mathrm{Haar}}(U),
\]
where \(S_{\mathrm{Haar}}(U)\) means \(-\sum_\ell\log J(A_\ell)\) in local coordinates.

The project asserts the following decomposition for the Hessian on the **horizontal** tangent bundle (mod gauge directions):

**Theorem (Lattice Hessian structure, project form).**
\[
H(U):=\nabla^2 S_{\mathrm{eff}}(U)
= \beta \Delta_{\mathrm{lattice}} - \beta V(U) + c_0 I,
\]
where:
- \(\Delta_{\mathrm{lattice}}\) is a positive semi-definite “kinetic” Laplacian coming from the quadratic part of the plaquette coupling,
- \(V(U)\) is a bounded “potential” term depending on plaquette variables,
- \(c_0 I\) is the Haar-induced shift.

### 3.1 Why this decomposition is powerful
Even if the plaquette contribution contains indefinite pieces, the Haar term gives a **uniform positive shift** (a curvature floor). In the optimistic version:

**Claim (uniform floor).**
\[
\lambda_{\min}(U)\ge c_0 \quad \text{for all }U \text{ in the regular stratum.}
\]

A weaker but more conservative bound is:
\[
\lambda_{\min}(U)\ge c_0 - \beta\|V\|_{\mathrm{op}},
\]
which is still useful in regimes where \(\beta\|V\|_{\mathrm{op}}<c_0\).

---

## 4. Transfer matrix and spectral gap

On a reflection-positive lattice theory, Osterwalder–Schrader reconstruction yields a transfer matrix \(T\) acting on a Hilbert space \(\mathcal{H}\) of half-space functionals:
\[
T = e^{-aH_T},\qquad H_T\ge 0.
\]

The spectral gap is
\[
\Delta := E_1 - E_0.
\]

### 4.1 Curvature-to-gap intuition
If the measure is uniformly log-concave in the relevant coordinates—heuristically \(\nabla^2 S_{\mathrm{eff}}\ge \rho I\)—then a Poincaré inequality holds with constant \(\rho\), and the associated Markov generator has spectral gap \(\ge \rho\). The project’s transfer-matrix bound can be read as a discrete-time analogue of this:

**Project corollary (lattice gap lower bound).**
\[
\Delta \;\ge\; \frac{\sqrt{c_0/2}}{a}.
\]

This is explicitly evaluated as:
\[
\Delta \gtrsim 
\begin{cases}
0.61/a, & \mathrm{SU}(2),\\
0.82/a, & \mathrm{SU}(3),
\end{cases}
\]
using \(c_0=3/4\) and \(c_0=4/3\) respectively.

---

## 5. How to harden this for a paper

To turn the above into a fully audit-able proof, the “to verify” list is short but sharp:

1. **Coordinate conventions:** track \(\langle A,A\rangle\) vs \(\mathrm{Tr}(A^2)\) so that \(c_0\) is computed unambiguously.
2. **Horizontal Hessian:** show the gauge (vertical) directions do not spoil convexity, i.e. the bound holds after projection to the orbit space.
3. **Plaquette Hessian control:** either prove \(-\beta V(U)\) is nonnegative in the relevant sense, or bound its operator norm.
4. **Transfer-matrix bridge:** state precisely how a curvature/Poincaré constant lower bound translates into the transfer-matrix spectral gap.

If these four items are pinned down cleanly, the lattice piece becomes the canonical “finite-dimensional skeleton” for the continuum strategy.
