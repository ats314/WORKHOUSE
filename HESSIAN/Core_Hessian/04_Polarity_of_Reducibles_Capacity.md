# Polarity of Reducible Configurations: Capacity as a “Singularity Firewall”  
*Corrected potential-theory note for lattice gauge configuration spaces*

Reducible configurations (those with stabilizer larger than the center) form singular strata in gauge orbit spaces. The project uses a key idea:

> **If the reducible locus is polar (capacity zero), it is invisible to the Dirichlet form and to spectral-gap statements.**

This note states the relevant capacity fact **carefully** (codimension matters!) and explains how it applies on a finite lattice.

---

## 1. Configuration space and reducibility

Let
\[
\mathcal{C}_\Lambda = SU(N)^{|\mathcal{B}|}
\]
with the product bi-invariant metric. Its dimension is
\[
m = (N^2-1)|\mathcal{B}|.
\]

A configuration is **reducible** if its holonomy is contained (up to conjugation) in a proper closed subgroup \(H\subsetneq SU(N)\), equivalently if its stabilizer in the gauge group is larger than the center.

Let \(\Sigma_\Lambda\subset\mathcal{C}_\Lambda\) be the reducible locus.

---

## 2. Capacity and polarity

Let \((M,g)\) be a compact Riemannian manifold and \(\mu\) a smooth probability measure with density bounded above/below relative to volume. Consider the Dirichlet form
\[
\mathcal{E}(f,f)=\int_M \|\nabla f\|^2\,d\mu.
\]

Define the \((1,2)\)-capacity of a Borel set \(E\subset M\) by
\[
\mathrm{Cap}(E)
=
\inf\left\{
\mathcal{E}(u,u)+\int u^2\,d\mu:\;
u\in C^\infty(M),\;
u\ge 1 \text{ near }E
\right\}.
\]

A set is **polar** if \(\mathrm{Cap}(E)=0\). Polar sets are hit with probability \(0\) by the diffusion associated to \(\mathcal{E}\) (for quasi-every starting point).

---

## 3. The codimension threshold (important correction)

A common pitfall: **codimension 1 sets are generally not polar** for Brownian motion / elliptic diffusions. In Euclidean potential theory, the \((1,2)\)-capacity threshold corresponds to Hausdorff dimension \(m-2\).

### Theorem (thin sets are polar)

Let \(M\) have dimension \(m\ge 3\). If \(E\subset M\) has Hausdorff dimension \(\le m-2\) (in particular if \(E\) is contained in a finite union of smooth embedded submanifolds of codimension \(\ge 2\)), then
\[
\mathrm{Cap}(E)=0.
\]

**Proof idea (standard).** Use local charts and Sobolev embedding \(H^1\hookrightarrow L^{2m/(m-2)}\) to build cutoff functions supported in tubular neighborhoods whose Dirichlet energy tends to \(0\) as the tube radius shrinks. \(\square\)

Because \(\mu\) is a smooth bounded density times volume, polarity is unchanged by replacing volume with \(\mu\).

---

## 4. Why reducibles should have codimension \(\ge 2\) on the lattice

The reducible locus is (at worst) a finite union over proper subgroups \(H\subsetneq SU(N)\) of “\(H\)-valued” strata (up to gauge). A crude but useful dimension heuristic is:

- \(\dim SU(N)=N^2-1\).
- Any proper connected closed subgroup \(H\subsetneq SU(N)\) has \(\dim H \le N^2-2\), and in many cases \(\dim H \le N^2-3\).  
- For \(SU(2)\), the largest proper connected subgroup is \(U(1)\) of dimension 1, giving codimension \(2\) already at the single-link level.

On the product space \(SU(N)^{|\mathcal{B}|}\), constraints “link variables lie in \(H\)” typically produce codimension at least \((\dim SU(N)-\dim H)\,|\mathcal{B}|\), and gauge constraints do not restore that lost dimension.

So it is very plausible (and in many finite-dimensional models provable by stratification theory) that each reducible stratum has codimension \(\ge 2\), hence is polar.

---

## 5. Application: reducibles are a “singularity firewall” for spectral analysis

Assume \(\Sigma_\Lambda\) is contained in a finite union of codimension \(\ge 2\) submanifolds (or semialgebraic sets of dimension \(\le m-2\)). Then:

1. \(\mathrm{Cap}(\Sigma_\Lambda)=0\); hence \(\Sigma_\Lambda\) is polar.  
2. Any Dirichlet-form/spectral-gap statement (Poincaré, log-Sobolev, etc.) is controlled by the **irreducible sector** \(M\setminus \Sigma_\Lambda\).  
3. In particular, a horizontal Hessian lower bound that fails only on \(\Sigma_\Lambda\) can still yield a global spectral gap.

This is an elegant way to neutralize orbit-space singularities without having to “resolve” them geometrically.

---

## 6. What further work would strengthen this

A rigorous project milestone would be:

- produce a **stratification theorem** for \(\Sigma_\Lambda\) on a finite lattice,  
- compute explicit codimension bounds for each stabilizer type, and  
- verify the \((m-2)\)-dimensional Hausdorff bound needed for capacity zero.

This would convert “plausible and standard” into a clean lemma usable inside a full proof.

