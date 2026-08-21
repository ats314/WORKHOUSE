# SIMULATION REVIEW (Dec 2025): Selected Derivations & Simulation Results

This bundle extracts the most *theory-relevant* derivations, proof-skeletons, and simulation results found in the project files (Dec 2025 runs).  
The selections are biased toward work that looks like it could “scale up” into a genuine research program: **curvature/convexity control**, **RG stability**, **spectral gap & decay**, and **computational identities** that materially simplify analysis.

## What’s in here

1. **Curvature → RG → Gap program sketch (with evidence)**  
   *Haar curvature seed, Riccati curvature decay, and HOTRG curvature explosion + Riccati “restoration” experiments.*  
   → `01_curvature_rg_riccati_hotrg.md`

2. **Lyapunov drift diagnostic for lattice gauge Langevin**  
   *Stochastic-generator check of a drift inequality for a plaquette-defect Lyapunov function on a periodic \(L^4\) lattice.*  
   → `02_lyapunov_drift_langevin_suN.md`

3. **Exponential decay bounds for lattice Green’s functions**  
   *Combes–Thomas–type bounds and envelope-slope measurements (FFT-based propagators).*  
   → `03_greens_decay_combes_thomas.md`

4. **Hodge projection & “phi obstruction” diagnostic for \(SU(2)\) Wilson action**  
   *Riemannian Hessian-vector products, Lanczos for \(\lambda_{\min}\), and a “defect” statistic signaling near-zero curvature events.*  
   → `04_phi_obstruction_hodge_hessian_su2.md`

5. **\(q\)-\(6j\) classical-limit error budget**  
   *A practical, quantitative “safe region” for \((\theta, J_{\max})\) where \(6j_q \approx 6j\) with explicit scaling \(O(\theta^2 J_{\max}^{5/2})\).*  
   → `05_q6j_error_budget_safe_region.md`

6. **\(q\)-Racah → Doob transform toy “mass gap machine”**  
   *A fully explicit finite-state Markov generator built from a \(q\)-Racah Jacobi Hamiltonian; gap extraction; flow classification; finite-size scaling exponent near \(q\to 1\).*  
   → `06_qracah_doob_massgap_toy.md`

7. **Determinant sparsity identity for lag-permuted observables**  
   *A clean algebraic reduction: identity case forces determinant \(0\); transposition case reduces to a 2-row bilinear; 3-cycles are the only fully dense case. Includes large randomized verification.*  
   → `07_determinant_sparsity_lag_permutations.md`

---

## A unifying theme (why these pieces hang together)

A recurring “big picture” across the files is a possible chain:

\[
\text{(Uniform convexity / curvature floor)} \quad\Longrightarrow\quad
\text{(functional inequalities: Poincaré / LSI)} \quad\Longrightarrow\quad
\text{(spectral gap / mixing)} \quad\Longrightarrow\quad
\text{(exponential decay / mass scale)}.
\]

The project’s most *distinctive* angle is that it tries to keep **convexity/curvature from collapsing under coarse-graining**, by pairing:

- a **coarse-graining step that can explode curvature anisotropy** (HOTRG-style pushforward), with  
- an explicit **Riccati-like spectral map** that damps large eigenvalues while (ideally) protecting the low end.

Whether that can ever be made mathematically clean in real 4D lattice YM is an open question — but the files contain nontrivial evidence, diagnostics, and a toy pillar (the \(q\)-Racah Doob chain) that can be used as a sandbox for “gap survives deformation” arguments.

---

## Provenance

This bundle was built from (at minimum) the following project artifacts:

- `CHAT YANG SIMULATION 4x4.txt`  
- `Simulations_and_Results_Summary.txt`  
- `GPT CODE PRODCUTIOPN TEST.txt`  
- `RUN 110.pdf`, `RUN 122.pdf`, `RUN 124.pdf`, `RUN 113.pdf`  
- `12-2-25 code runs 3.pdf`  

(Each individual document ends with a “Sources used” section listing the precise files it was distilled from.)
