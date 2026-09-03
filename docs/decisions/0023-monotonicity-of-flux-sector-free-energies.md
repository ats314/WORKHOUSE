# ADR 0023: Monotonicity of Electric-Flux Sector Free Energies as a Bootstrap to Strong Coupling

**Decision Date:** 2026-09-02  
**Author:** User  
**Status:** PROPOSED (Research Question)  

## Context

The current approach to the strong-coupling gap problem proceeds bottom-up:
- Weak coupling (small β): exact second-order scalar at every rank
- Fourth-order: numerical high-precision data + adversarial verification
- Strong coupling: numerical limit studies + cold runs
- The gap is proven at O(u²) and strongly supported at O(u⁴), but a single proof covering the entire coupling range has remained elusive

## Hypothesis: Griffiths-Type Monotonicity for Abelian Flux Sectors

### The Conjecture

For each Z_N-valued flux sector s, the sector free energy is monotone in bare coupling β:

$$F_s(\beta_2) \leq F_s(\beta_1) \quad \text{for all } \beta_2 > \beta_1$$

where the sector free energy is defined as:
$$F_s(\beta) = -\frac{1}{\beta V} \log \text{Tr}_s \left[ \exp(-\beta H) \right]$$

and $\text{Tr}_s$ denotes the trace over states in flux sector s.

### Why This Should Work

1. **Abelian Structure Restored**
   - Griffiths inequalities (FKG, GHS) require abelian symmetry
   - They fail for Wilson loops (non-abelian gauge algebra)
   - Flux sectors live in the center $Z_N$ → abelian commutative structure
   - The flux Q is not a gauge-invariant observable; it is conjugate to the gauge

2. **Correlation Bounds Become Applicable**
   - Griffiths First Inequality: $\langle AB \rangle \geq \langle A \rangle \langle B \rangle$ for suitable observables
   - In spin systems: derives from comparison of measures on a lattice
   - In gauge theory: the absence of non-commutativity for Z_N observables restores the mechanism
   - Crucially: the flux is abelian, so $[Q_i, Q_j] = 0$ (different sites)

3. **Data Advantage**
   - **Weak coupling**: exact perturbative spectrum at every rank, sector-resolved by charge and flux
   - **Strong coupling**: exact sector multiplicities from our census (what we enumerate in the corpus)
   - **Boundary values known exactly**: E_s^(min) at β→0 and the strong-coupling ground-state degeneracy at β→∞
   - **No approximation needed at either end of the axis**: both regimes are fully determined

### Mechanical Insight

The question is whether:

$$\frac{d F_s}{d\beta} \geq f_s(\beta, \text{correlators})$$

for some bound $f_s$ that depends on the flux-sector correlators but has a consistent sign across all β.

**Mechanism A: Thermodynamic Derivative**
$$\frac{d F_s}{d\beta} = -\frac{1}{\beta^2 V} \log Z_s(\beta) + \frac{1}{\beta V} \langle H \rangle_s$$

where the first term (entropy cost of tightening the distribution) fights against the second term (energy cost). Monotonicity would say the entropy term always wins (or vice versa).

**Mechanism B: Truncation Argument**
The sector is finite-dimensional (rank ≤ N, local) at strong coupling. The number of low-energy configurations is bounded. A truncation of the full spectrum at energy E_cutoff(β) might give a monotone bound on F_s.

**Mechanism C: Correlation Positivity**
Adapt the GHS proof: use the fact that Z_N correlators are positive-definite (or satisfy an ordering relation) to bound the partition function ratio Z_s(β₂) / Z_s(β₁).

## Falsifiability

If monotonicity holds:
- It is a single fact that replaces all numerical verification across the axis
- A proof would be a non-perturbative bootstrap: weak coupling → strong coupling in one step
- The gap at weak coupling immediately extends to all β

If monotonicity fails:
- The failure mode reveals a phase transition: at what β and in which sector(s) does the ordering reverse?
- This gives a mechanism for understanding the strong-coupling structure
- A false sign reversal would pinpoint where perturbation theory breaks down

Either way, the answer is binary and testable.

## Attack Strategy

### Phase 1: Formalize the Sector Free Energy (T1/T2)

Extract from the exact second-order spectrum:
1. The energy eigenvalues $E_k^{(s)}$ for each sector s
2. The partition function $Z_s(\beta) = \sum_k \exp(-\beta E_k^{(s)})$
3. The free energy $F_s(\beta) = -(1/\beta V) \log Z_s(\beta)$

This is purely combinatorial arithmetic on the known second-order (and fourth-order) spectrum.

### Phase 2: Compute Boundary Values Exactly

**Weak coupling:**
$$F_s(0^+) = \lim_{\beta \to 0^+} F_s(\beta) = E_s^{\min} \quad \text{(ground state energy of sector s)}$$

From the second-order exact ledger: we have $E_s^{\min}$ for every rank and every sector.

**Strong coupling:**
$$F_s(\infty) = E_s^{\min}(\infty) - \frac{1}{V} \log M_s$$

where $M_s$ is the sector multiplicity at strong coupling. This is a finite census: the number of Z_N-valued one-forms on the cubic lattice with prescribed total charge s.

For the trivial flux sector (the one we care about), $M_s$ is the rank of the homology $H_1^{\text{flux}}$.

### Phase 3: Interpolate Numerically

On a grid of β values:
1. Compute $F_s(\beta)$ using the spectral definition
2. Compute derivatives $dF_s/d\beta$ numerically
3. Check the sign and magnitude across all sectors and all β

Expected outcome:
- If $dF_s/d\beta$ ≤ 0 everywhere: monotonicity holds (or $\geq 0$ if decreasing from strong to weak)
- If there are sign changes: identify the critical coupling(s) and the affected sectors

### Phase 4: Prove or Refute (If Numerical Test Passes)

If Phase 3 shows monotonicity:
1. Differentiate the partition function inequality
2. Use GHS or a similar bound on abelian flux correlators
3. Track the sign carefully through the derivation

If it fails:
1. Characterize the phase transition
2. Understand which mechanism (energy vs. entropy, truncation breaking down, etc.) causes the reversal
3. Update the model of the phase diagram

## Relevance to the Publication

The publication currently:
- Proves the gap at O(u²)
- Reports strong evidence at O(u⁴) via three independent calculations
- Uses scaling and asymptotic analysis to argue for all-β consistency

**If monotonicity can be established:**
- One theorem covers the entire axis
- The paper becomes a proof, not a report of evidence
- The section on strong coupling can cite a single fact rather than averaging independent runs

**If monotonicity fails:**
- The paper's caution becomes vindication: there *is* a phase transition
- The characterization of where it occurs becomes a secondary result
- The O(u²) proof stands as the firm ground, and the O(u⁴) behavior is richer than a simple scaling

## Next Steps

1. **Write the extraction code** (`src/workhouse/invariants/monotonicity.py`)
   - Parse the second-order exact spectrum
   - Define $Z_s(\beta)$ for each sector
   - Implement the numerical grid

2. **Run the numerical grid** on SU(3), SU(4), SU(5)
   - Cover β ∈ [0.01, 5.0]
   - Plot $F_s(\beta)$ and $dF_s/d\beta$ for each sector
   - Identify any anomalies

3. **Synthesize the results** in a memo
   - If monotone: sketch a proof mechanism
   - If not: document the failure mode and its interpretation

4. **Decide the publication angle**
   - If proven: add as a Lean theorem in the "All-Coupling Bootstrap" section
   - If open: propose it as an open conjecture with the numerical evidence

---

**Related decisions:** ADR 0019 (Hodge normal form), ADR 0020 (chain-amplitude route), ADR 0021 (cold computation authority), ADR 0022 (adversarial review of revision 6)  
**Rests on:** The exact second-order spectrum; the sector census at strong coupling  
**Carries:** A binary testable hypothesis that can either unify the gap proof or reveal a phase transition

