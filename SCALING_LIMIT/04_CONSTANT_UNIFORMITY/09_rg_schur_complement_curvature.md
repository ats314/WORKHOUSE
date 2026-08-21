
# RG Step Curvature Bound via Schur Complements and Brascamp–Lieb

## Problem statement

You want a theorem of the form:

> Integrating out fast modes (marginalization) cannot reduce the curvature floor below a controlled factor:
> \[
> \kappa' \ge \alpha\,\kappa_*
> \]
> with explicit \(\alpha\) and explicit hypotheses.

The cleanest version is Euclidean and already strong enough to justify most of the “placeholder” \(\alpha\)-arguments in the draft.

---

## 1. The exact Hessian formula for free energy

Let \(V:\mathbb{R}^n\times \mathbb{R}^m\to\mathbb{R}\) be \(C^2\).
Define the effective potential (free energy)
\[
V_{\rm eff}(x) := -\log\int_{\mathbb{R}^m} e^{-V(x,y)}\,dy.
\]
Let \(\nu_x\) be the conditional measure
\[
\nu_x(dy) := \frac{e^{-V(x,y)}}{\int e^{-V(x,\cdot)}}\,dy.
\]

Then:
\[
\nabla V_{\rm eff}(x) = \mathbb{E}_{\nu_x}\big[\partial_x V(x,y)\big],
\]
and
\[
\nabla^2 V_{\rm eff}(x)
=
\mathbb{E}_{\nu_x}\big[\partial_{xx}^2 V(x,y)\big]
-
\mathrm{Cov}_{\nu_x}\big(\partial_x V(x,y)\big),
\]
where the covariance is the \(n\times n\) matrix
\[
\mathrm{Cov}_{\nu_x}(g)
=
\mathbb{E}[g g^\top]-\mathbb{E}[g]\mathbb{E}[g]^\top.
\]

So marginalization *subtracts* a positive semidefinite term; curvature can decrease.

---

## 2. Brascamp–Lieb control of the covariance

If for each \((x,y)\) the block \(\partial^2_{yy}V(x,y)\) is positive definite, Brascamp–Lieb implies
\[
\mathrm{Cov}_{\nu_x}\big(\partial_x V\big)
\preceq
\mathbb{E}_{\nu_x}\Big[
\partial^2_{xy}V \,
\big(\partial^2_{yy}V\big)^{-1}
\partial^2_{yx}V
\Big].
\]

Therefore:
\[
\nabla^2 V_{\rm eff}(x)
\;\succeq\;
\mathbb{E}_{\nu_x}\Big[
\underbrace{
\partial^2_{xx}V
-
\partial^2_{xy}V \,
(\partial^2_{yy}V)^{-1}
\partial^2_{yx}V
}_{\text{Schur complement of the Hessian}}
\Big].
\]

---

## 3. Strong convexity is preserved *without loss* (α = 1)

### Theorem (marginal preserves strong convexity)

Assume the full Hessian satisfies a uniform bound
\[
\nabla^2_{(x,y)} V(x,y) \succeq \kappa I_{n+m}
\qquad \text{for all } (x,y).
\]
Then the effective potential satisfies
\[
\nabla^2 V_{\rm eff}(x)\succeq \kappa I_n
\qquad \text{for all } x.
\]

### Proof sketch

Let the block Hessian be
\[
H=\begin{pmatrix}A & B^\top\\B & C\end{pmatrix}\succeq \kappa I.
\]
Then for any \(u\in\mathbb{R}^n\), choose \(v=-C^{-1}Bu\). By positive definiteness,
\[
\begin{pmatrix}u\\v\end{pmatrix}^\top H \begin{pmatrix}u\\v\end{pmatrix}
=
u^\top(A-B^\top C^{-1}B)u
\;\ge\;
\kappa(\|u\|^2+\|v\|^2)
\;\ge\;\kappa\|u\|^2.
\]
So the Schur complement \(A-B^\top C^{-1}B\succeq \kappa I_n\).
Taking conditional expectations preserves the inequality, and the Brascamp–Lieb step shows
\(\nabla^2 V_{\rm eff}\) dominates the expected Schur complement.

Thus \(\alpha=1\): **marginalization does not reduce the convexity parameter** when the *joint* potential is uniformly strongly convex.

---

## 4. Where α<1 can enter in the project

So why is your draft carrying \(\alpha=0.976\) as a “placeholder”? Because the hypotheses of the α=1 theorem are *not* satisfied as stated in the lattice gauge setting:

- You only have a **local** convexity certificate (SAFE region), not global.
- Gauge directions / harmonic sectors can produce **zero modes** unless you quotient correctly.
- The RG map is not “just marginalization”: it typically includes a **nonlinear block map** and a Jacobian term.
- You may integrate out variables where convexity is weak, or only available after projection.

### Practical, explicit α
A pragmatic RG curvature theorem in this context should state something like:

> On the SAFE region, the joint coarse+fine potential is \(\kappa_*\)-convex on the *physical horizontal subspace*.
> The block map has distortion bounded by \(L\) and second derivative bounded by \(M\).
> Then the coarse effective potential is \(\kappa' \ge \kappa_* - \varepsilon(L,M,\mathrm{Var}_{\nu_x})\).

In many regimes \(\varepsilon\) can be made numerically tiny, giving an effective \(\alpha=1-\varepsilon/\kappa_*\).

---

## 5. What to write in the “real theorem” section

A “clean hypotheses” lemma you can paste into the main draft is:

1. State the Euclidean theorem above (α=1) for marginalization under uniform strong convexity.
2. Add a corollary that allows:
   - projecting to a subspace (physical directions),
   - restricting to a SAFE region,
   - and adding a perturbation with operator norm \(\delta\) (giving \(\kappa-\delta\)).

That gets you a sharp, honest theorem statement and separates the hard physics (return-to-SAFE + gauge quotient) from the easy convex analysis (Schur complements).

