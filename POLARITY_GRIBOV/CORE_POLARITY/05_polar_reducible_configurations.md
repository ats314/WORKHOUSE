# Polar reducible configurations and why codimension \(\ge 2\) can save your analysis

## The problem this addresses

Gauge theories have “bad sets” in configuration space:
- reducible configurations (non-generic stabilizers),
- gauge-fixing singularities,
- Gribov horizons and related boundaries.

If the analysis of spectral gaps relied on excluding such sets, you’d worry that you just proved a theorem on the wrong space.

This note extracts an elegant escape hatch: many of these bad sets are **polar** for the Dirichlet form driving the diffusion, so they do not affect the spectral analysis.

---

## 1. Reducible configurations as algebraic subvarieties

Fix a proper block-diagonal subgroup \(H\subsetneq SU(N)\).  
Consider the set of configurations where **all holonomies lie in \(H\)**.

This imposes polynomial constraints on the matrix entries of link variables \(U_b\), so it defines an algebraic subvariety of the configuration space
\[
\mathcal C_\Lambda = SU(N)^{|\mathcal B|}.
\]

A dimension count (using decomposition of \(\mathfrak{su}(N)\) into irreducible \(H\)-modules) gives:

> Each such reducible locus has codimension \(\ge 2\).

A finite union over possible \(H\) preserves codimension \(\ge 2\).

---

## 2. Capacity and polar sets (Dirichlet form viewpoint)

Given a Dirichlet form \(\mathcal E(f,f)=\int |\nabla f|^2\,d\mu\), one defines the capacity of a Borel set \(A\) by
\[
\mathrm{Cap}(A)=\inf\left\{\mathcal E(f,f)+\|f\|_{L^2(\mu)}^2:
f\ge 1\text{ on a neighborhood of }A\right\}.
\]

A set is **polar** if \(\mathrm{Cap}(A)=0\).  
Polar sets are “invisible” to the diffusion: starting from typical initial data, the process hits a polar set with probability \(0\).

Heuristic principle (made precise in many settings):
- In sufficiently regular manifolds, sets of codimension \(\ge 2\) tend to have zero capacity for the natural Dirichlet form.

So codimension \(\ge 2\) is not just a geometric fact; it’s an *analytic firewall*.

---

## 3. Why this matters for the mass-gap program

If reducible configurations (and often other gauge-fixing singular sets) are polar:

- You can define the diffusion / Langevin generator on the full configuration space and safely ignore measure-zero, capacity-zero pathologies.
- Spectral gap statements derived from Bakry–Émery curvature bounds remain meaningful for the physically relevant dynamics.
- It reduces the danger that “the gap proof works only off a set where the physics lives.”

In other words: the theory might still be hard, but you’re not defeated by a technicality like a singular gauge slice.

---

## 4. Next steps

To make this ingredient truly “bolt-on rigorous” in 4D lattice \(SU(N)\):

1. Specify the Dirichlet form precisely on \(\mathcal C_\Lambda\) with the Gibbs weight \(e^{-S_{\mathrm{eff}}}\).
2. Prove the codimension \(\ge 2\) loci indeed have zero capacity for that weighted form (not only for the unweighted Laplacian).
3. Extend from reducible loci to any other problematic sets introduced by gauge fixing (if gauge fixing is used).

This is a tractable-looking analysis problem compared to the deep RG questions, and it shores up the foundations.