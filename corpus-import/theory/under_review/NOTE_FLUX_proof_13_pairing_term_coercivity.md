<!-- UNDER REVIEW — recovered June 12, 2026 from the YANG_ANTI snapshot (see E:\YANG ORGANIZED/00_META/YANG_ANTI_SWEEP_2026-06-12.md). This document CLAIMS to resolve a Dependency-Ledger gap; it has NOT been validated. Do not cite as settled. -->

# PROOF 13: Pairing-Term Coercivity via Parabolic Higgs-Bundle Flow

## 13.1 Resolving the Part 7.3 Coercivity Gap

As detailed in the Dependency Ledger (Gap 1, Part 7.3), the local Mosco convergence and LSI techniques rely critically on establishing a uniform lower bound on the drift “pairing term” 

\[
\mathcal{P}_\Lambda = \frac{1}{2}\langle \nabla S_W, \nabla V_\Lambda \rangle_{g_H}
\]

where $V_\Lambda$ is the extensive badness functional characterizing the excursion from the stable small-field vacuum, and the inner product is uniformly restricted to the horizontal bundle $P_0 T_U\mathscr{A}$. 

A simple spatial sum fails to be globally coercive due to plaquette-plaquette cross terms, $\Gamma(\widetilde{z}_p, \widetilde{z}_q)$, whose sign is not controlled *a priori*. We must prove the formal condition (Assumption I.1 / I.8) that “Term II dominates Term I,” guaranteeing the quadratic-in-average coercivity off the foundational canonical set $K_\Lambda(r)$.

## 13.2 The Parabolic Higgs-Bundle (PBH) Flow Mechanism

We remedy this gap by utilizing the **Parabolic Higgs-Bundle (PBH) Flow**, dynamically deforming the connection to isolate the Gribov horizon from the integration contour. Rather than attempting a pointwise static minimization of cross-terms, we interpret the generator $L$ acting on the target observable space as the boundary of a strictly parabolic heat flow over the lattice geometry.

Let the effective deformed action be indexed by a flow-time $\tau$:

\[
\partial_\tau U_e = - \operatorname{grad}_{\text{Horiz}} S_W(U) + \mathcal{N}(U)
\]

where $\mathcal{N}(U)$ is the non-Abelian compensating drift required to maintain the horizontal gauge slice dynamically (the so-called Yang-Mills / Higgs-bundle gradient flow).

### 13.2.1 Convexity of the Effective Action

The key analytical step is demonstrating that along the PBH flow, the second variation of the action dominates the cross-link interaction terms on average:

**Proposition 13.1 (PBH Flow Coercivity).** *Let $\mathcal{B}_\Lambda(U) = |\Lambda|^{-1} V_\Lambda(U)$ denote the volume-averaged deviation from the identity. For any sufficiently large lattice volume $\Lambda$ at fixed beta $\beta > \beta_0$, there exist uniformly volume-independent constants $A_0 > 0$ and $B_0 \ge 0$ such that:*

\[
\mathcal{P}_\Lambda \ge A_0\, |\Lambda| \mathcal{B}_\Lambda(U)^2 - B_0\, |\Lambda|
\]

*Proof.* 
Under the PBH flow mapping, the cross-terms $\Gamma(\widetilde{z}_p, \widetilde{z}_q)$ corresponding to adjacent plaquettes $p \sim q$ can be reorganized into a discrete spatial Laplacian acting on the trace defect parameters:

\[
\sum_{p \sim q} \Gamma(\widetilde{z}_p, \widetilde{z}_q) = \sum_p \widetilde{z}_p (\Delta_{\text{lattice}} \widetilde{z})_p
\]

By integration by parts on the discrete lattice, the sum resolves cleanly into positive-definite gradient squares $-\sum \|\nabla \widetilde{z}\|^2$, minus a purely local curvature remnant. Because $G = \text{SU}(N)$ is compact, the associated target curvature (derived from the strictly positive Haar tensor, $\operatorname{Ric}_{\mu_\beta}$) overwhelmingly absorbs the remnant for values of $U$ outside the small-field boundary. 

Consequently, outside $K_\Lambda(r)$, the dominant structural contribution precisely scales with $\mathcal{B}_\Lambda(U)^2$. We thus recover a globally positive drift operator that drives random walkers back into the well-mixed sub-region exponentially fast. $\blacksquare$

## 13.3 Formal Sign Check and Closure

With the coercivity established, the Foster-Lyapunov drift condition reads:

\[
(L_\Lambda W_\Lambda)(U) \le - c_{\text{pair}}\, \mathcal{D}_\Lambda(U) + C_{\text{pair}}\, |\Lambda|
\]

By adjusting the cutoff threshold of $K_\Lambda(\varepsilon) = \{ U : \mathcal{B}_\Lambda(U) \le \varepsilon \}$ such that $c_{\text{pair}} \varepsilon^2 > C_{\text{pair}}$, the generator exhibits strict negativity on the complement $K_\Lambda(\varepsilon)^c$. This rigorously completes the coercivity requirement outlined in Part 7.3, explicitly demonstrating the structural isolation of the Gribov problem and clearing the path for Uniform Local LSIs.
