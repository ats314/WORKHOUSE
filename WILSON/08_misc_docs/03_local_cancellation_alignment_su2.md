# Local Cancellation Rigidity in SU(2): Toward “Rough ⇒ Force Bounded Below”

This note extracts the **single geometric input** that would make the bad-set coercivity step volume-uniform:

> If the averaged plaquette disorder is bounded below, then the Wilson force cannot be arbitrarily small.

This is GAP-FC-02 in the project gap map.

---

## 1. What is being targeted (Assumption A′)

Let $U$ be a lattice gauge field on a finite lattice $\Lambda$ (fixed cutoff).

Define the gauge-invariant disorder functional
\[
\mathcal B_\Lambda(U)
=
\frac{1}{|P(\Lambda)|}\sum_{p\in P(\Lambda)}
\Bigl(1-\frac12\mathrm{Re\,Tr}(U_p)\Bigr).
\]
Let $K^c:=\{\mathcal B_\Lambda\ge \varepsilon_0\}$ for some fixed $\varepsilon_0>0$.

Let $S_\Lambda(U)$ be the Wilson action at inverse coupling $\beta$.

### Assumption (A′) — “no fake vacua”
There exist constants $\varepsilon_0>0$ and $c_0=c_0(\varepsilon_0,\beta)>0$ such that
\[
\mathcal B_\Lambda(U)\ge \varepsilon_0
\quad\Longrightarrow\quad
\|\nabla S_\Lambda(U)\|\ge c_0,
\]
with $c_0$ independent of the volume $|\Lambda|$.

**Why it matters.**
A′ is exactly the kind of statement that lets you prove *coercivity on the bad set* $K^c$ without fighting entropy/volume blowup.

---

## 2. Reduction to a single link (the local cancellation problem)

Fix a link $\ell$.

In $d=4$, $\ell$ is incident to $m=6$ plaquettes, naturally grouped into three transverse planes.
The linkwise force has schematic form
\[
\nabla_\ell S(U)
=
\sum_{p\ni\ell}\sigma_{p,\ell}\,\mathrm{Ad}_{g_{p,\ell}(U)}(X_p),
\qquad
X_p := \nabla\Phi_\beta(U_p)\in \mathfrak{su}(2),
\]
where:
- $\sigma_{p,\ell}\in\{\pm 1\}$ is an orientation sign,
- $g_{p,\ell}(U)\in \mathrm{SU}(2)$ is a transport determined by neighboring links,
- $\Phi_\beta$ is the single-plaquette potential.

### Single-plaquette coercivity
If a plaquette has defect
\[
e_p:=1-\tfrac12\mathrm{Re\,Tr}(U_p)\ge \varepsilon,
\]
then by compactness there is a deterministic lower bound
\[
\|X_p\|\ge c_1(\varepsilon,\beta)>0.
\]

So the only remaining obstruction to A′ is **cancellation**:

> Can the sum of several rotated vectors in $\mathfrak{su}(2)\cong\mathbb R^3$ cancel even if one of them has size $\ge c_1$?

---

## 3. The key lemma you actually need

### Lemma (Local cancellation ⇒ alignment, informal “drop-in” version)

Fix $\varepsilon>0$.
Assume at least one incident plaquette has defect $\ge \varepsilon$, hence at least one $X_p$ has $\|X_p\|\ge c_1(\varepsilon,\beta)$.

If
\[
\Big\|\sum_{p\ni\ell}\sigma_{p,\ell}\,\mathrm{Ad}_{g_{p,\ell}(U)}(X_p)\Big\|
\ \ \text{is very small},
\]
then the incident data must lie in an **aligned Cartan exceptional set**:

- all $X_p$ point along a common axis in $\mathfrak{su}(2)$ (a single maximal torus direction), and
- the transports $\mathrm{Ad}_{g_{p,\ell}(U)}$ preserve that axis.

This exceptional set is lower-dimensional (closed, “thin”) inside the local configuration space.

**How it would close A′.**
If the exceptional set lies inside the small-disorder region $K$ (or cannot occur while $\mathcal B_\Lambda\ge \varepsilon_0$), then any $U\in K^c$ forces at least one link to have $|\nabla_\ell S|\ge c(\varepsilon_0,\beta)$.
Summing over links yields $\|\nabla S\|\ge c_0$.

---

## 4. What still has to be made rigorous

The lemma above is “morally obvious” in $\mathbb R^3$ if the rotations were arbitrary,
but the lattice imposes strong constraints.

A rigorous proof needs:

1. **Compatibility of transports.**  
   The $g_{p,\ell}(U)$ are not independent $\mathrm{SU}(2)$ elements; they come from adjacent link variables and share edges/vertices.

2. **Exceptional set control.**  
   Show the set of cancellation configurations has empty interior (semi-algebraic / real-analytic geometry), and in fact lies in the *small-disorder* region.

3. **Quantitative bound by compactness.**  
   On the compact set “incident roughness $\ge\varepsilon$” minus the exceptional set, the continuous map
   \[
   U\mapsto \|\nabla_\ell S(U)\|
   \]
   has a positive minimum.

4. **Uniformity in volume.**  
   Since the statement is local, constants should depend only on $\varepsilon$ and $\beta$, not on $|\Lambda|$.

---

## 5. Numerical evidence (supporting, not a proof)

A 2D exact-force toy model (SU(2) on a small $L\times L$ torus) was used to search for “flat rough directions”:

- from random rough initial data, the disorder stayed $O(1)$ while the gradient norm stayed macroscopically positive,
- a structured “checkerboard Cartan” initial condition rapidly flowed toward the vacuum (both disorder and gradient collapsed).

Interpretation: these runs **rule out obvious low-complexity counterexamples** in a fast testbed, and support A′ as a plausible geometric fact, but they do not prove it.

(Concrete code + example output are in `05_simulation_appendix_maxwell_and_a100_su2.md`.)

---

## 6. Why this is “new theory potential”

This is a rigidity statement in disguise.

A cartoon version is:

> **Non-abelian vector-sum rigidity:**  
> In $\mathrm{SU}(2)$, if several adjoint-rotated plaquette forces cancel exactly while at least one plaquette is “rough,” then the configuration must lie near a maximal torus alignment set.

That resembles phenomena in:
- **almost-commuting matrices** (alignment into a Cartan),
- **frustration-free vs frustrated** spin systems,
- and even **rigidity theory** (constraints kill mechanisms).

If you can formalize the exceptional set and prove it is confined to the low-disorder region, you get a genuinely powerful geometric lemma: it turns a global coercivity problem into a local classification of cancellation patterns.

---

## 7. A100-scale simulation that directly tests A′ (design)

The most informative GPU experiment is not a single long Markov chain.
It is a **batched adversarial search**:

- maintain $B\sim 10^3$–$10^4$ independent configurations on GPU,
- optimize (or sample) with a penalty to enforce $\mathcal B_\Lambda\ge \varepsilon_0$,
- try to minimize $\|\nabla S\|$.

If the optimizer never finds $\|\nabla S\|\ll 1$ at fixed roughness across a wide range of seeds and lattice sizes, that becomes strong evidence for A′; if it *does* find such points, you’ve discovered a counterexample family.

A ready-to-run skeleton for this appears in `05_simulation_appendix_maxwell_and_a100_su2.md`.

