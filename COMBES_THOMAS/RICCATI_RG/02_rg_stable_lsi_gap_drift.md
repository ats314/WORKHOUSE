# RG-Stable Curvature, Local-to-Global LSI with Drift, and the Spectral-Gap Chain

*Project extraction (generated 2025-12-29).*

## 0. Why this document exists

The project’s core “mass-gap engine” is the chain

\[
\text{(curvature floor)}\;\Longrightarrow\;\text{LSI}\;\Longrightarrow\;\text{spectral gap}\;\Longrightarrow\;\text{exponential decay}.
\]

Two things threaten the chain in a lattice gauge setting:

1. **RG steps:** integrating out fast modes can degrade convexity.
2. **Leaving the SAFE region:** the potential is not globally uniformly convex.

This note extracts the parts of the repository that address those two threats.

---

## 1. Curvature-controlled class

On a complete Riemannian manifold $(M,g)$ with
\[
d\mu = Z^{-1}e^{-V}\,d\mathrm{vol}_g,\qquad L = \Delta_g-\langle \nabla V,\nabla\cdot\rangle,
\]
define
\[
\mathrm{Ric}_V := \mathrm{Ric}_g+\nabla^2V.
\]

Define the curvature class
\[
\mathcal{C}(\kappa) := \{(g,V)\;:\;\mathrm{Ric}_V\ge \kappa g\}.
\]

### 1.1 Two stability facts

- **Small Hessian perturbations:** if $\|\nabla^2W\|_{op}\le \varepsilon$ then
  \[
  (g,V)\in\mathcal{C}(\kappa)\;\Rightarrow\;(g,V+W)\in\mathcal{C}(\kappa-\varepsilon).
  \]

- **Tensorization:** product measures preserve the minimum curvature floor:
  \[
  (g_i,V_i)\in\mathcal{C}(\kappa_i)\;\Rightarrow\;(g_1\oplus g_2,V_1\oplus V_2)\in\mathcal{C}(\min\{\kappa_1,\kappa_2\}).
  \]

Both are “bookkeeping lemmas” that become powerful when paired with explicit constants.

---

## 2. Curvature ⇒ LSI ⇒ spectral gap (tight version)

Assume $\mathrm{Ric}_V\ge \kappa g$ for some $\kappa>0$.

Then the Bakry–Émery calculus gives a log–Sobolev inequality
\[
\mathrm{Ent}_\mu(f^2)\le \frac{2}{\kappa}\int |\nabla f|^2\,d\mu.
\]

The LSI implies the Poincaré inequality
\[
\mathrm{Var}_\mu(f)\le \frac{1}{\kappa}\int |\nabla f|^2\,d\mu,
\]
so the generator $L$ has spectral gap $\lambda_1\ge \kappa$.

> The important feature is **constant transport**: the same $\kappa$ appears all the way down the chain.

---

## 3. RG curvature degradation factor

Let one RG step be: integrate fast variables, then reparametrize onto a coarse lattice.

Inside the SAFE region, the project uses the perturbation estimate
\[
\mathrm{Ric}_{V'} \ge (\kappa_*-\delta)\,g,
\]
where $\kappa_*$ is the Haar curvature floor and $\delta$ is the Wilson-Hessian variation budget.

It then defines an explicit “degradation factor”
\[
\alpha := \frac{\kappa_*-\delta}{\kappa_*}=1-\frac{\delta}{\kappa_*}.
\]

With the SAFE constants $(\kappa_*,\delta)=(0.25,0.006)$:
\[
\boxed{\alpha=0.976.}
\]

Iterating yields
\[
\mathrm{Ric}_{V_n}\ge \alpha^n\kappa_*\,g_n.
\]

**Interpretation:** if the RG flow reaches a convex fixed point in $O(10^2)$ steps, then $\alpha^{100}\kappa_*\approx 0.088\cdot 0.25\approx 0.022$ remains positive, so the chain “curvature ⇒ LSI ⇒ gap” stays alive across scales.

---

## 4. Escaping the SAFE region: drift-based local-to-global LSI

The repository also uses a standard “two-zone” architecture:

- **Zone A:** a compact SAFE core where curvature is explicit and positive.
- **Zone B:** the complement, controlled by a Lyapunov drift condition that prevents runaway.

A typical drift hypothesis is: there exists $W\ge 1$ and constants $a,b>0$ and a compact $K$ such that
\[
LW \le -aW + b\,\mathbf{1}_K.
\]

Together with a local LSI (or local Poincaré) on $K$ and mild regularity on $V$, this can be upgraded to a **global** LSI.

### 4.1 A subtle gap: regularity of geodesically convex potentials

Many drift constructions assume you can treat $V$ as continuous / locally Lipschitz on the relevant region.

If $V$ is only known to be geodesically convex (for example after projection / coarse graining), one needs a statement of the form:

> geodesic convexity ⇒ interior continuity (and often local Lipschitz) under mild metric hypotheses.

The project includes a supporting reference note on continuity of geodesically convex functions on Riemannian manifolds; this is the sort of lemma that plugs into drift-based patching without adding new physics.

---

## 5. What’s potentially novel here

The ingredients are standard, but the *specific* package is interesting:

1. An explicit SAFE-region constants ledger $(\kappa_*,\delta,\alpha)$.
2. A quantified “curvature survives RG” statement in the same constants.
3. A drift-based patch to turn a local uniform convexity statement into a global LSI (if one proves the return-to-SAFE estimates).

This looks like a blueprint for turning “local curvature from Haar geometry” into a genuinely volume-uniform functional inequality for a gauge theory.

---

## 6. Next steps that would strengthen this module

1. Replace the informal RG step bound by a fully explicit **Schur complement** inequality for marginalization (fast-mode integration).
2. Prove an explicit return-to-SAFE drift inequality with a computable Lyapunov function (not just a plausible one).
3. Clarify the role of gauge fixing: show the horizontal projection and Faddeev–Popov term do not destroy the curvature floor on the local core.

