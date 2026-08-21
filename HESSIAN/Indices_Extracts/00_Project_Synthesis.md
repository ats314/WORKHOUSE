# Project Synthesis: What is Actually New Here?

This note is a curated **high-signal** extraction of the project’s most conceptually distinctive and technically reusable pieces.
It is written to be readable standalone.

The project’s overall strategy is a *fixed-cutoff* mass–gap argument on the lattice (for nonabelian $SU(2)$ in $d=4$), then a cross–scale step to the continuum.
The pieces below are the ones that (i) are already fully proved in the project files, or (ii) are clearly formulated and plausibly provable with a small number of missing ingredients,
and (iii) have potential life beyond this particular project.

---

## 1. The fixed–cutoff chain (in one page)

At a fixed lattice spacing (cutoff) $a$ and finite periodic volume $\Lambda$:

1. **Lyapunov drift + functional inequalities** on the configuration manifold (product Lie group modulo gauge) are used to obtain a uniform spectral gap for a Markov generator (Langevin / heat-bath / Gibbs sampler).  

2. **Helffer–Sj\"ostrand-type covariance representations** turn functional inequalities for the measure into exponential clustering bounds.  

3. The key analytic “kernel” estimate is an **exponential off-diagonal decay bound for the inverse of a massive Maxwell-type operator on $1$-forms**, proved by a Davies/Combes–Thomas conjugation method with explicit constants.  

4. A **localization/decomposition across a good event $K$** separates “small curvature” regions from “rough” regions and pays a localization error controlled by a typicality/tail term.

The technical novelty is concentrated in (3) and in the attempt to make (4) work in a nonabelian setting via a *quantitative coercivity-on-$K^c$* principle.

---

## 2. What seems genuinely publishable as independent pieces

### (A) A clean Davies/Combes–Thomas bound for the massive Maxwell $1$-form kernel with local constants
This is a finite-range inverse decay lemma tailored to the $1$-form Laplacian on the link graph.
It upgrades the exponent scaling from $\mathcal O(m^2)$ to $\mathcal O(m)$ and introduces a **boundary-local row-sum constant** $C_{\partial}$ that can materially sharpen decay in localized regions.

(See: `01_Davies_Maxwell_Green_Decay.md`.)

### (B) A “reflection positivity permanence” toolkit + a sharp nonabelian no-go for exact Markovian coarse graining
Two things happen here:

- A set of lemmas packages how **OS reflection positivity** survives reflection-equivariant pushforwards and **projective limits**.
- A striking **no-go theorem**: an *exact* reflection-equivariant Markov coarse-graining kernel with an exact projection property cannot exist for nontrivial nonabelian groups; it forces commutativity.

This is a structural constraint on RG architectures for gauge theories.

(See: `02_Reflection_Positivity_and_RG_NoGo.md`.)

### (C) A geometric reduction of the mass gap to bounded-geometry control in a tubular neighborhood of the flat stratum
This reframes a chunk of the “hard analysis” problem as a uniform bounded-geometry problem for the orbit-space manifold near the vacuum (flat) stratum.
That is a bridge to finite-dimensional Riemannian techniques.

(See: `03_Tubular_Neighborhood_Reduction.md`.)

### (D) A coercivity program based on “local cancellation $\Rightarrow$ Cartan alignment”
This is the most speculative but possibly the most powerful: the idea that in $SU(2)$, **rough curvature cannot have small force unless the configuration is essentially abelian (Cartan-aligned)**.
The project articulates an overdetermined-constraints heuristic (6 constraints vs 3 local DOF per link), plus numerical hunting evidence.

(See: `04_Coercivity_via_Cartan_Alignment.md`.)

### (E) Numerical counterexample hunting as a research instrument
The project includes a set of GPU-friendly “search” scripts whose job is not to fit physics data but to falsify coercivity assumptions by looking for **rough + non-Cartan + tiny force** configurations.
That is a neat methodological contribution by itself.

(See: `05_Numerical_Evidence_and_Scripts.md`.)

---

## 3. What to do next (highest leverage)

1. **Turn the Cartan-alignment heuristic into a quantitative lemma.**
   The missing move is a *uniform lower bound* on force in $K^c$ away from Cartan-aligned sets, with explicit dependence on $\beta$, $L$, and the roughness threshold.

2. **Exploit the $C_{\partial}$ refinement** in the localization argument.
   If you localize to a region $\Omega$, you should use $C_{\partial}(\Omega)$ rather than a global degree bound, improving decay constants and tail estimates.

3. **Replace the impossible exact Markov coarse graining** (no-go) with a realistic nonexact interface:
   extended state space, stochastic gauge fixing, boundary edge modes, or approximate kernels with quantified error.
