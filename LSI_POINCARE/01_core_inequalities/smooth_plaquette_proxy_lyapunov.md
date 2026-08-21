# Smooth plaquette proxy and Lyapunov drift without volume leakage

> **Problem.** For uniform-in-volume functional inequalities (Poincaré / log-Sobolev),
> the standard route is a Lyapunov drift condition
> \[
> \mathcal L V \;\le\; -a V + b |\Lambda|
> \]
> for a Markov generator \(\mathcal L\).  
> On compact Lie groups with the Wilson action, the *obvious* Lyapunov choices tend to create a catastrophic
> \(|\Lambda|\)-scaled Laplacian term (“volume leakage”) unless you tune the observable very carefully.

This note extracts the project’s key technical fix: a **smooth plaquette proxy**
whose first derivative vanishes at the identity, which prevents the Laplacian part of \(\mathcal L\)
from producing a volume-sized error.

---

## 1. The underlying geometry

Configuration space at cutoff is a compact manifold
\[
\mathcal C_\Lambda \;=\; G^{\Lambda_1},
\]
one copy of a compact Lie group \(G\) per directed link \(\ell\in\Lambda_1\).
The Langevin / heat-bath generators used in the project are of the schematic form
\[
\mathcal L = \Delta_{\mathcal C_\Lambda} - \langle \nabla S_W,\nabla (\cdot)\rangle,
\]
i.e. Laplace--Beltrami plus a drift from the Wilson action \(S_W\).

Thus for any smooth \(V\),
\[
\mathcal L V = \Delta V \;-\; \underbrace{\langle \nabla S_W,\nabla V\rangle}_{\text{pairing term}}.
\]
If you can show:
- \(\Delta V\) is at most \(O(|\Lambda|)\), and
- the pairing term dominates \(V\) from below,

you get a drift inequality.

---

## 2. Why naive “distance-to-identity” Lyapunovs fail

For a single plaquette holonomy \(U_p\in G\), a natural “badness” is the trace defect
\[
\tau(U_p) := \mathrm{Tr}(I-U_p),
\]
(or its real part / normalized version).

If you take \(V\) proportional to \(\sum_p \tau(U_p)\), you quickly run into a second-derivative issue:
\(\Delta \tau(U_p)\) has a **nonzero constant term at** \(U_p=I\).
Summing over plaquettes yields an unavoidable \(c\,|\Lambda|\) term even in “perfect vacuum” configurations.
That’s the “volume leakage” obstruction.

The project’s fix is to replace \(\tau\) by a profile whose first derivative vanishes at the origin.

---

## 3. The smooth proxy \(\Phi\) and the magic condition \(\Phi'(0)=0\)

Define a smooth scalar profile \(\Phi(\kappa; t)\) for \(t\ge 0\) (think: \(t\approx \tau(U_p)\)) by
\[
\Phi(\kappa; t) := \frac{t^2}{t^2+\kappa^2},
\qquad \kappa>0.
\]
Key features:

- \(\Phi\in[0,1)\), increasing in \(t\), and saturates to \(1\) for large defect \(t\gg\kappa\).
- \(\Phi'(0)=0\). Concretely,
  \[
  \Phi'(t)=\frac{2t\kappa^2}{(t^2+\kappa^2)^2},
  \qquad \Phi'(0)=0.
  \]

Now define the Lyapunov functional on a region \(\Lambda\) (sum over plaquettes):
\[
V_\Lambda(U)
:= \sum_{p\in\Lambda_2} \Phi\!\big(\kappa;\, \tau(U_p)\big).
\]

**Why this kills volume leakage.**  
When you apply \(\Delta\) to a composition \(\Phi(\tau(U_p))\), you get terms involving \(\Phi'\) and \(\Phi''\).
The term that used to scale like \(|\Lambda|\) is precisely the one proportional to \(\Phi'(0)\).
Setting \(\Phi'(0)=0\) forces that constant term to vanish in the small-field/vacuum regime.

This is the kind of microscopic “constant hygiene” that makes the drift method viable in compact lattice gauge models.

---

## 4. Drift decomposition: what remains after the proxy trick

With this choice,
\[
\mathcal L V_\Lambda
= \underbrace{\Delta V_\Lambda}_{\text{controlled by proxy design}}
-\underbrace{\sum_{\ell\in\Lambda_1}\langle \nabla_\ell S_W,\nabla_\ell V_\Lambda\rangle}_{=:P_\Lambda(U)}.
\]

The project identifies the **remaining hard part** as the coercivity of the pairing term \(P_\Lambda(U)\):
you need a lower bound of the form
\[
P_\Lambda(U) \;\ge\; A\,V_\Lambda(U) - B|\Lambda|,
\]
at least on the “good set” where plaquette defects are not too large.

Once such a bound is proved, the drift inequality closes and gives the uniform-in-volume functional
inequalities needed downstream (mass gap / clustering machinery).

---

## 5. Why this is promising outside this project

The \(\Phi'(0)=0\) trick is not specific to Wilson action or gauge theory; it is a design principle:

> When you build Lyapunovs from local “defect variables” on a compact manifold,
> choose the profile so that the Laplacian’s vacuum contribution cancels automatically.

This can be useful in:
- compact spin systems with nonlinear constraints,
- interacting diffusions on products of manifolds,
- coarse-graining steps where you want drift constants that do **not** degrade with volume.

---
