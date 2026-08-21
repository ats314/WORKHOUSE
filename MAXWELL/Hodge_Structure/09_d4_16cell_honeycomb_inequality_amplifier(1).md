
# The D4 / 16-cell honeycomb lattice as an “inequality amplifier”
*(Why higher rotational symmetry could make your analytic constants less nasty.)*

## 1. What the Katz–Nógrádi preprint claims (in one paragraph)
A December 2025 preprint studies QCD discretized on the **4D 16-cell honeycomb** (the \(D_4\) lattice), arguing that its much larger remnant rotational symmetry produces substantially smaller cut-off effects than the standard cubic (tesseractic) lattice.

The headline points (as stated in the paper):
- symmetry group size is larger (1152 vs 384 elements for cubic),
- in free-field benchmarks and in quenched SU(3), leading scaling violations often look like \(O(a^4)\) rather than \(O(a^2)\),
- and several topological/chiral observables appear closer to continuum at fixed \(a\).

## 2. Why this might matter for *functional inequalities*
Many functional inequality constants (Poincaré/log-Sobolev, coercivity constants in discrete elliptic estimates, etc.) are sensitive to:
- anisotropy,
- the dispersion relation of low modes,
- and how “round” the discrete Laplacian/curl operators look at finite \(a\).

A discretization with more rotational symmetry can:
1. reduce direction-dependent worst cases (fewer “soft directions”),
2. make continuum approximations cleaner (smaller remainder terms),
3. potentially improve the stability of the one-step comparison you want between two different operators (diffusion vs OS transfer).

In the language of your project: if the constants in the hinge inequality or in the strip-coercivity lemma are polluted by lattice artifacts, the \(D_4\) lattice is a plausible way to turn down that pollution.

## 3. A concrete “work now” test you can do
Do the simplest analytic check first, where you can compute everything:

1. **Free Gaussian field on the \(D_4\) lattice.**  
   Compute the lowest nonzero eigenvalues of the discrete Laplacian (or the relevant curl-curl operator) and compare their rotational splitting to the cubic lattice at the same nominal spacing.

2. **Plug into your Dirichlet constants.**  
   Your Poincaré constants in finite volume often reduce to the first nonzero eigenvalue of some elliptic operator after gauge fixing. If the \(D_4\) lattice pushes the first anisotropic corrections from \(O(a^2)\) to \(O(a^4)\), that feeds directly into cleaner scaling windows.

3. **Check the strip coercivity constant.**  
   Rebuild the local “plaquette badness” functional \(\mathcal B_\Lambda\) using the \(D_4\) elementary loops (triangles) and see whether the gradient lower bound on the strip is easier to prove (because the incidence structure is richer: each site has 24 nearest neighbors).

## 4. The one caution
The \(D_4\) lattice changes the combinatorics substantially (triangular elementary loops, different coordination number), so any part of the argument that depends delicately on “plaquettes are squares” has to be retranslated.

But from a “constant chasing” perspective, that pain may pay for itself if it removes the need for delicate anisotropic estimates.
