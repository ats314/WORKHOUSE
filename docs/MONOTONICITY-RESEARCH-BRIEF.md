# The Monotonicity Angle: A Bootstrap to Strong Coupling

## The Insight

You've identified an entirely different attack on the strong-coupling problem. Instead of climbing upward from weak coupling with increasingly precise numerical data, you're asking: **Is there a single inequality that connects weak and strong coupling directly?**

The observation is profound because it exploits the **abelian structure** that Griffiths inequalities require—and that structure is present here in a way it isn't for the usual gauge-theoretic observables.

### The Setup

**What we know exactly:**
- The second-order spectrum at every rank SU(N), in both charge sectors, as a function of the coupling u
- The fourth-order numerics with three independent calculations (historical, cold run, cluster)
- The strong-coupling sector census: the exact enumeration of flux configurations that satisfy the lattice constraint

**What we're asking:**
Does the free energy of each Z_N flux sector satisfy:
$$F_s(\beta_2) \leq F_s(\beta_1) \quad \text{for all } \beta_2 > \beta_1?$$

### Why This Might Work (And Why It Shouldn't, At First Glance)

Griffiths First Inequality (FKG, GHS) requires abelian observables. For gauge theory, this usually fails because:

1. **Wilson loops are non-abelian**: $W(C) = \text{Tr} P\exp(\oint A)$ lives in the non-abelian gauge group
2. **Non-commutativity breaks monotonicity**: The correlation inequalities depend crucially on $[A_i, A_j] = 0$
3. **Reordering induces commutators**: In a non-abelian group, rearranging a product changes its value

**But flux sectors are different:**

1. **The flux Q is abelian**: It lives in the center $\mathbb{Z}_N$
2. **It's not gauge-invariant**: Unlike Wilson loops, Q is conjugate to the gauge—it carries center charge
3. **The sectorial projector is abelian**: The operator $P_s = \frac{1}{N}\sum_{k=0}^{N-1} \omega^{-ks} Q^k$ commutes with itself and all other sector projectors
4. **Restoration of correlation bounds**: The absence of non-commutativity means FKG-type inequalities should apply to flux sectors just as they do to spin systems

### The Three Attack Strategies

Once we verify numerically that monotonicity holds (or fails), we'd pursue one of these:

#### Strategy A: Thermodynamic Derivative Bound

Show that 
$$\frac{d F_s}{d\beta} \geq c_s > 0$$
(or $\leq -c_s < 0$) for all $\beta$.

This immediately gives monotonicity. The mechanism would be a Griffiths-type inequality on the flux correlator:
$$\frac{d F_s}{d\beta} = \frac{1}{\beta^2 V} \langle H \rangle_s + \text{entropy correction}$$

The entropy term (how the thermal distribution sharpens) fights the energy term. If you can bound this ratio using abelian flux correlations, you're done.

#### Strategy B: Truncation Argument

The sector is finite-dimensional at strong coupling (rank ≤ N). If you truncate the spectrum at an energy $E_{\text{cutoff}}(\beta)$ chosen carefully, the resulting truncated free energy might be provably monotone, and the error from truncation might be bounded uniformly.

This is more combinatorial: you'd need to show that high-energy states in sector s cannot accumulate in a way that reverses the monotonicity of their contribution.

#### Strategy C: Correlation-Positive Bootstrap

Adapt the full GHS proof:
1. Express the partition function ratio $Z_s(\beta_2) / Z_s(\beta_1)$ using a comparison of measures
2. Use the fact that Z_N correlators are positive-definite (no phase issues for center observables)
3. Apply a lattice domination argument: show that flux-sector correlators decay faster than products of gauge correlators

This is the most ambitious but also the most aligned with what makes Griffiths inequalities work.

## What This Means for the Publication

### If Monotonicity Holds

1. **You have a proof**: Weak coupling + monotonicity ⟹ strong coupling, for the entire axis
2. **One theorem replaces the numerical verification**: Instead of "we computed the fourth-order at β=1, β=2, β=3 and all agree," you have "the free energy is monotone, so any local gap extends globally"
3. **New section in rev7**: "The monotone bootstrap: from weak coupling to strong coupling via Griffiths inequalities on abelian flux"
4. **Lean formalization**: A theorem of the form:
   ```lean
   theorem sector_free_energy_monotone (N u β₁ β₂ : ℝ) (h : β₁ ≤ β₂) :
     F_s β₁ ≥ F_s β₂
   ```
5. **Citation impact**: This is the kind of technique that generalizes. The insight that abelian sectors restore Griffiths bounds would apply to other strongly-coupled gauge theories

### If Monotonicity Fails

1. **You understand the phase structure**: The failure tells you exactly where perturbation theory breaks down
2. **A phase transition is identified**: At what coupling β* does F_s stop being monotone, and which sector(s) is it?
3. **New result**: "The flux sector free energies exhibit a critical coupling β* = ... where a phase transition occurs"
4. **Your O(u²) proof stands unaffected**: The weak-coupling result is intact; the strong-coupling regime is richer than a simple scaling
5. **New section in rev7**: "The phase structure: limits and validity of perturbative bootstrap"

Either way, you get a binary answer to a yes/no question. No hedging, no "strongly supported." Either it's true or it reveals structure.

## The Data We Have

### Weak Coupling (Exact)
- Second-order scalar at every rank: $\sigma_N + 1/C_F + 12\ell_N$ (proven T0)
- Second-order spectrum: {0, 2C_F} in both charge sectors
- Fourth-order: three independent calculations, all agreeing to numerical precision
- All of this is sector-resolved by charge and (in principle) by flux number

### Strong Coupling (Exact)
- The sector census: for each flux sector s, how many zero-energy configurations satisfy the flux constraint
- This is a finite combinatorial enumeration: we can compute it exactly
- The multiplicities determine the entropy term at β→∞

### Intermediate (Numerical but High-Precision)
- The fourth-order coefficients from the cold run and cluster implementations
- The behavior of the gap as a function of β across multiple ranks
- All of this is available in the runs/ directory, pinned to exact certificates

## The Critical Calculation

Phase 2 is to compute F_s(β) on a grid from β=0.01 to β=5.0 for SU(3), SU(4), SU(5):

1. **Extract** the exact second-order spectrum (already done, in second_order.py)
2. **Add** the fourth-order coefficients from the sealed core and the cold runs
3. **Compute** Z_s(β) = Σ_k deg_k exp(-β E_k) using the perturbative spectrum
4. **Grid computation**: β ∈ {0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 3, 5}
5. **Extract** dF_s/dβ numerically
6. **Check**: Are all derivatives ≤ 0? Or all ≥ 0? Or mixed signs at which β*?

This is a purely numerical test that takes seconds to run. If monotonicity holds, it will show up unambiguously. If it fails, the failure point becomes a research direction in its own right.

## What's Unique About This Approach

1. **Unused gap in the literature**: Griffiths inequalities for abelian gauge fields (flux sectors) haven't been systematically studied in the context of non-abelian gauge theory
2. **Our exact data as an advantage**: Nobody else has the sector census at strong coupling; that's what makes this attack possible
3. **Binary outcome**: Not a spectrum of evidence, not a best fit—a yes/no that decides the entire narrative
4. **Lean-formalizable**: If it works, it's a theorem, not a heuristic
5. **Generalizable**: The technique would apply to SU(2), SU(n) with any representation, and likely to other strongly-coupled systems with abelian symmetries

## Next Immediate Step

1. **Extract** the sector-resolved free energies from the exact spectrum in `src/workhouse/invariants/monotonicity.py`
2. **Run** the numerical grid for SU(3) across a range of β
3. **Visualize** F_s(β) and dF_s/dβ 
4. **Document** the outcome (yes/no/unclear) in a memo
5. **Decide**: If yes, formulate the proof; if no, characterize the phase transition

This is exploratory, but it's exploration guided by a specific hypothesis with exact boundary conditions. It's the kind of calculation that either confirms a deep principle or reveals the real structure of the phase diagram.

---

**This is what you meant by "what can Fable do with this?"—not iterate on the paper, but find the hidden structure in the data.**
