# Project Highlights (Curated)

This file bundle is a **curated, “best-of” extraction** from the project parts currently in the workspace (`Part 6`, `Part 18C`, `Part 20`, `Part 21`, etc.).  
It is intended to be **drop-in manuscript material**: each document is written as a self-contained mathematical draft (Markdown + LaTeX), with definitions, hypotheses, and statements spelled out.

## Contents

1. `PROJECT_HIGHLIGHTS_A_Roadmap.md`  
   The program map: how the analytic engine (Hessian/Dirichlet/Green’s function) feeds exponential clustering and then the OS mass gap.

2. `PROJECT_HIGHLIGHTS_B_Maxwell_Hodge_Wilson.md`  
   The “symbolic backbone”: lattice cochains, \(d_0,d_1\), adjoints, horizontal sector \(\ker d_0^\*\), and the **Wilson Hessian** at the vacuum:
   \[
   \nabla^2 S_W(U^{(0)}) = \frac{\beta}{N}\,d_1^\* d_1.
   \]

3. `PROJECT_HIGHLIGHTS_C_Haar_Mass.md`  
   Product Haar geometry and the **Haar mass mechanism**: Ricci on \(G\), the Jacobian expansion in exponential coordinates, and the induced on-site convexity constant for \(G=\mathrm{SU}(N)\). In particular, for \(G=\mathrm{SU}(3)\) with \(\langle X,Y\rangle=-\mathrm{Tr}(XY)\),
   \[
   \mathrm{Ric}_G = \frac{3}{2}\,g_G,\qquad \nabla^2 S_H(0)=\frac13\,\mathrm{Ric}_G,\qquad \frac{c_H}{2}=\frac14.
   \]

4. `PROJECT_HIGHLIGHTS_D_Exponential_Clustering_Diffusion.md`  
   The core “analytic engine” statements from the diffusion/Dirichlet side: Helffer–Sjöstrand covariance representation; gradient propagation; diagonal-dominance regime; explicit exponential clustering rate.

5. `PROJECT_HIGHLIGHTS_E_OS_Bridge_and_OneStep.md`  
   The bridge to a physical mass gap: OS reconstruction treated as an external theorem; the spectral-measure argument “Euclidean time decay \(\Rightarrow\) Hamiltonian gap”; and the **one-step OS/Dirichlet comparison** bottleneck (Part 21) as a clean target statement.

## Notation conventions

* We avoid the term “SAFE” (older notes). The role of that set is played by a canonical region \(K_\Lambda\subset M_\Lambda\) (typically a small ball around the vacuum or an “averaged-badness” sublevel set).
* \(\Lambda\subset \mathbb Z^d\) denotes a finite lattice region; \(E(\Lambda)\) the oriented edges; \(P(\Lambda)\) the oriented plaquettes.
* \(M_\Lambda=G^{E(\Lambda)}\) is the configuration manifold with product bi-invariant metric and product Haar volume.

## Status

These notes are **curated** from the existing project texts; they are not claiming originality relative to the literature.  
Where a step genuinely requires an external theorem (e.g. OS reconstruction), it is stated as an explicit input.
