---
title: "Encoding a θ-term via q-deformation in a 4D SU(2) tensor-network model: χ_top from free-energy curvature"
date: "2025-12-28"
source_files:
  - "2025-11-26_4DSU2GaugeTheorySimulation_4D-SU2-gaugetheory.pdf"
  - "2025-11-26_4DSU2GaugeTheorySimulation_gaugetheory-quantumgroups-tensorrenormalization.pdf"
  - "2025-11-26_HybridQDeformationSU2_SU2-4DGaugeTheory-q-Deformation.pdf"
  - "2025-11-26_Phase2QDeformation_4D-SU2-q-Deformation.pdf"
  - "2025-11-26_Hybrid6jSymbolsComputation_4D-SU2-GaugeTheory.pdf"
  - "2025-11-26_FourierAnalysisSU2GaugeTheory_GaugeTheory-JAX-QuantumPhysics.pdf"
  - "2025-11-25_4DPhaseScanSimulation_Python-Physics-TensorNetwork.pdf"
---

# 1. What is being attempted

A Euclidean Yang--Mills $\theta$-term weights topological sectors by a phase:

$$
Z(\theta) = \sum_{Q\in\mathbb Z} e^{i\theta Q}\, Z_Q
\quad\Longrightarrow\quad
F(\theta) := -\log Z(\theta),
\qquad
\chi_{\mathrm{top}} = \frac{1}{V}\left.\frac{\partial^2 F}{\partial \theta^2}\right|_{\theta=0}.
$$

On standard lattice formulations this creates a sign problem for Monte Carlo.

The project tries a different computational representation:
build a 4D SU(2) tensor-network (HOTRG) where the deformation parameter

$$
q = e^{i\theta}
$$

enters the recoupling data (quantum dimensions, $q$-deformed $6j$ symbols, or perturbative hybrids).
The hope is that the $\theta$-dependence is handled deterministically by tensor contraction rather than stochastically.

# 2. The small-θ extraction logic

The practical pipeline in the notebooks is:

1. For each $\theta$ in a small set near $0$, build a vertex tensor $T(\theta)$ whose entries include the relevant group-theoretic weights.
2. Contract it (approximately) via HOTRG or a simplified contraction to obtain $Z(\theta)$.
3. Fit $F(\theta)=-\log Z(\theta)$ to a quadratic model

$$
F(\theta) \approx a + b\theta + c\theta^2,
$$

and set

$$
\chi_{\mathrm{top}} = \left.\frac{\partial^2 F}{\partial \theta^2}\right|_{\theta=0}
= 2c.
$$

This is the *local* (near-zero) version of extracting curvature of the vacuum energy.

# 3. A perturbative hybrid q-deformation (working theory)

One notebook introduces a “hybrid” $q$-deformed $6j$ symbol:

- Use a trusted classical value at $\theta=0$ (e.g. SymPy's exact $6j$).
- Multiply by a small-$\theta$ correction intended to mimic $q$-deformation.

A representative ansatz extracted from the code is

$$
\{6j\}_q(\theta)
=
\{6j\}_0\;\Bigl[1 + i\theta\,J_{\mathrm{tot}} - \alpha\,\theta^2\Bigr],
$$

where

$$
J_{\mathrm{tot}} = j_1+j_2+j_3+j_4+j_5+j_6,
\qquad
\alpha = \frac16\sum_{r=1}^6 \bigl[(2j_r+1)^2 - 1\bigr].
$$

This is explicitly labeled as a small-angle approximation (e.g. $\theta<0.5$) in the project files.

**Important caveat.** This is not derived from first principles here; treat it as a *working theory* for prototyping
how $\theta$-dependence might propagate through the tensor network.
A full implementation would compute the true $q$-$6j$ symbols.

# 4. Fourier perspective: recovering Z_Q and consistency checks

A strength of tensor-network access to $Z(\theta)$ is that it invites a discrete Fourier transform:

$$
Z_Q = \frac{1}{2\pi}\int_0^{2\pi} d\theta\ e^{-i\theta Q}\, Z(\theta),
\qquad
P(Q)=\frac{Z_Q}{\sum_{Q'}Z_{Q'}}.
$$

Then

$$
\chi_{\mathrm{top}} = \frac{1}{V}\langle Q^2\rangle
= \frac{1}{V}\sum_Q Q^2 P(Q).
$$

This provides global diagnostics:

- $Z(\theta)$ should be $2\pi$-periodic in $\theta$.
- CP symmetry suggests $F(\theta)$ is even near $\theta=0$, so $b\approx 0$ in the quadratic fit.
- $Z_Q$ should be real and nonnegative in a consistent physical definition (for pure YM).

These are excellent regression tests for whether the chosen $q$-deformation prescription is physically faithful.

# 5. Why this is potentially new/interesting

The intellectually spicy part is the proposed **representation-theoretic encoding** of $\theta$:

- Standard lattice YM inserts $\exp(i\theta Q)$ built from gauge fields.
- Here the $\theta$-dependence is pushed into **quantum-group deformation data** used to build the tensor network.

If the mapping can be made precise (not just heuristic), it could be a new angle on the $\theta$-term that is friendlier to deterministic contraction methods.

# 6. Concrete next steps

1. **Replace the hybrid ansatz with actual q-6j.** Use the log-magnitude + phase $q$-factorial machinery to compute $q$-$6j$ symbols directly,
   and confirm smooth $\theta\to 0$ reduction to the classical values.

2. **Full $\theta\in[0,2\pi]$ scan + Fourier reconstruction.** Compute $Z(\theta)$ on a grid, recover $Z_Q$, and compute $\chi_{\mathrm{top}}$ via $\langle Q^2\rangle/V$.

3. **Volume scaling.** Check that $\chi_{\mathrm{top}}$ stabilizes (or scales correctly) with effective volume / number of RG steps.

4. **Cross-check against known limits.** In strong coupling, compare qualitative trends with known lattice results;
   in the classical ($\theta=0$) case, check confinement indicators (string tension proxies, etc.) as sanity tests.

