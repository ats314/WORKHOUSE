# SIS Project Extracts (December 2025)

This folder contains short, self-contained **Markdown + \LaTeX{}** notes extracted from the project artifacts.  
The emphasis is on **(i)** derivations/proof-adjacent structure that looks unusually clean, and **(ii)** simulations whose outputs appear to be informative and worth following up.

## Contents

1. **Affine Laplacian Law & Generator Decomposition (SU(2), 4D)**  
   A remarkably tight empirical law: the configuration-space Laplacian of the chosen observable is *affine* in the average plaquette, with coefficients pinned to \(\approx 12\) in 4D.  
   Also includes a split-half Monte Carlo (MC) test confirming the generator decomposition.

2. **Core-Set Lyapunov Certificate (Negative Drift Outside a Threshold)**  
   A data-driven certificate that, on the subset \(\{B_{\rm avg}\ge \tau_0\}\), the gradient pairing dominates enough to force uniformly negative drift.  
   This is the shape of the hypothesis used in Harris/Foster--Lyapunov approaches to geometric ergodicity.

3. **Scalar-Lattice “Coherence Sweep” & Hypercubic Artifact Tuning**  
   Results and code for extracting mass-gap proxies and tuning an anisotropy-correction parameter \(c\) to reduce hypercubic artifacts.

4. **4D \(\phi^4\) Symmetry-Breaking Quench Snapshot + Topological Audit**  
   A Fourier-accelerated relaxation/quench producing a saved 64\(^4\) state, followed by an audit that counts walls/knots and estimates a “tension ratio”.

## How to use these notes

- If you want to **turn any of this into a theorem**: start with the affine Laplacian law note; it suggests an exact identity may be provable from SU(2) representation theory + the link-wise Laplace--Beltrami operator.
- If you want to **turn this into a mixing-time / ergodicity result**: start with the core-set certificate and try to build a genuine minorization condition on the core.
- If you want to **stress-test the numerics**: rerun the sweeps at additional \(\beta\), increase MC chunks, and verify the pinned constants persist.
