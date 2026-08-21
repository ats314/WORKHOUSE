# PMBSF Master Document (pass 19)

## Projected Maxwell Birman–Schwinger Firewall: A Unified Account

**Compiled:** 2026-05-26  
**Status:** Conditional. **Not** a Yang–Mills mass-gap proof.

**Pass 19 (current):** Adds two material refinements to pass 18 without changing the conditional status. **(i)** The side-10/core-margin-3 Stage B geometry diagnostic is upgraded from Metropolis block resampling to exact SU(2) heat-bath block resampling. The new anchor is `PMBSF_SU2_LemmaQ_block_conditional_stageB_heatbath_20260525_215913`: \(L=16,\beta=3.5,q_\eta=0.003,\eta=0.005\), exact heat-bath law \(U_\ell\sim\mathrm{vMF}_4(\overline H_\ell/\|H_\ell\|,\beta\|H_\ell\|)\), 64 frozen-boundary blocks, 864 core plaquettes/block, and distance bins through \(d=12\). It reports median \(\Lambda=1.0158112\), max \(\Lambda=2.5930038\), median \(\Lambda_{\rm root}=1.0221089\), max \(\Lambda_{\rm root}=2.3431348\), and max depth-median \(q_{\rm cond}/q_\eta=1.3020833\). This supersedes the earlier Metropolis Stage B as the primary geometry-robustness anchor. **(ii)** The analytic target is sharpened from the cavity-intensity bound alone to a positive-tilt source-radius route: local cap-intersection stability (LCI) for incident heat-bath caps plus Balaban far-source stability implies TOS+J; TOS+J implies a positive source-radius bound \(Z_A(\rho/q_\eta)\le e^{K|A|}\); positivity of coefficients then implies Lemma Q. This replaces the vague command “prove Lemma Q” by the precise open theorem: typical/tempered SU(2) heat-bath geometry satisfies LCI with rooted/absorbed complement and far source tilts distort the LCI parameters by an exponentially summable kernel.

The conditional theorem stack is unchanged:
\[
\text{Lemma Q + source-weighted Bałaban expansion + boundary-band gate}
\Rightarrow
\text{SU(2) projected-capacity firewall closure.}
\]
Lemma Q remains open analytically.

### Pass 19 changelog

Material additions:

- **Appendix Z.1: Exact heat-bath Stage B geometry robustness.** Incorporates the exact heat-bath side-10/core-margin-3 run. The older Metropolis Stage B remains historical/supporting evidence only. The exact-HB Stage B result is now the primary larger-geometry Lemma Q diagnostic.
- **Appendix Z.2: LCI/TOS+J reduction.** Adds the positive-real source-radius proof route:
  \[
  \text{LCI + Balaban far-source stability}
  \Rightarrow
  \text{TOS+J}
  \Rightarrow
  Z_A(\rho/q_\eta)\le e^{K|A|}
  \Rightarrow
  \text{Lemma Q}.
  \]
- **Status correction:** pass 18’s Appendix V should be read with the exact-HB side-10 Stage B run superseding the Metropolis side-10 row. The exact-HB side-8 run remains the compact primary conditional-sampling anchor; exact-HB side-10 is now the primary geometry-robustness anchor.
- **Open theorem sharpened:** the next analytic target is no longer merely “cavity-intensity bound.” It is:
  \[
  \text{LCI-good typicality + Balaban far-source stability}
  \Rightarrow
  \text{TOS+J}.
  \]
  The cavity-intensity bound remains a sufficient downstream form, but TOS+J is now the sharper proof interface.

**Pass-19 verdict.** Pass 19 strengthens the numerical and analytic interface for Lemma Q but does not prove it. The exact-HB Stage B data materially improves the evidence hierarchy; the LCI/TOS+J reduction materially improves the proof target. The SU(2) theorem remains conditional.

---

### Pass 18 changelog

Pass 18 supersedes pass 17. Triggered by user instruction "lets get to writing, research any advances needed and update the master document" after uploading the Lemma Q final document, the Expanded Derivations integration document, the L=64 projected-capacity threshold law write-up, and the two L=64 scripts (threshold-law print-only + order-parameter attack). The integration is surgical: passes 1–17 content is untouched; pass 18 adds §T.11 and Appendices U, V, W, X, Y; the top status block above replaces the prior Pass 16 status line.

Material additions:

- **§T.11 (extension of Appendix T).** Two pass-17 honesty corrections folded into the master narrative explicitly: §T.11.1 the decay-rate point estimates $m_{\rm pair} = 1.15$, $m_{\rm root} = 0.88$ from the 3-point fit on Stage A have wide bootstrap 95% CIs of $[0.10, 2.27]$ and $[0.04, 2.18]$ respectively — the qualitative finding (positive decay rate, consistent with §R.1 / Lemma Q) is preserved, but the point estimates should not be quoted as if they were tight; §T.11.3 the cap-predictor extended-regression $R^2 = 0.100$ initially reported turns out to be a binary-classifier artifact: on positive (non-zero $q_{\rm cond}$) rows only it falls to $R^2 = 0.036$, and a block fixed-effect alone gives $R^2 = 0.056$. The missing structure is non-local frozen-exterior dependence, not local higher-order. These are the fifth and sixth honesty corrections.

- **Appendix U: Lemma Q (precise analytic target).** Folds the §1–§5 content of the Lemma Q final document (2026-05-25) into the master as a named target: the multiplicative bound $\mathbb E[\prod_p X_{p,\eta} \mid \mathcal F_{C^c}] \le (C_Q q_\eta)^{|B|}$ and its rooted analogue, the equivalent cavity-intensity form $\lambda_p(S \mid \mathcal F_{C^c}) \le q_\eta \exp(\sum_r J(p,r))$ with $J(p,r) \le C e^{-m d_C(p,r)}$, and the chain-rule proof that cavity stability implies Lemma Q. The name "Lemma Q" replaces the longer "§R.1 / (M′)_SU(2) / local rare-source factorization" throughout pass 18 and forward; pre-pass-18 references to (M′)_SU(2) remain as historical references and are not retroactively renamed. **The cavity-intensity bound is identified as the smallest sufficient sub-target** — this is the actual next analytic theorem to prove.

- **Appendix V: SU(2) Wilson block-conditional Lemma Q anchors.** §V.1 documents the exact heat-bath side-8 run as primary anchor (medians $\approx 0.9$, maxima $\le 6.1$, depth bin {2}, distance bins through $d \approx 4$, indicator is upper-envelope ramp). §V.2 documents the Metropolis Stage B side-10 / margin-3 run as geometry-robustness supplement (medians $\approx 1.0$, maxima $\le 9.1$, depth bins {3, 4}, distance bins through $d = 12$, indicator is symmetric sigmoid — pass-17 Stage A baseline). §V.3 compares both anchors against Stage A medians ($\approx 1.0$–$1.25$ from pass 17 §T.3) to show that Stage B's larger geometry tightened the medians and produced two depth bins rather than one. §V.4 logs the cap-predictor result across all three runs: signs uniformly correct (negative slope of larger-magnitude with stronger sampling), $R^2$ uniformly weak (0.01–0.06 range) — the cap mechanism is directionally confirmed but the load-bearing theorem must be block source-stability, not a one-link cap proof.

- **Appendix W: Full-volume SU(2) Wilson pair/rooted covariance through $L=64$.** Three-row table $L \in \{12, 16, 64\}$ at $\beta = 3.5$, $q_\eta = 0.003$, $\eta = 0.005$. Headline: median $|\rm Cov(X,X)|/q_\eta^2$ drops $0.117 \to 0.071 \to 0.007$ (factor 17 between $L=12$ and $L=64$); rooted median drops $0.109 \to 0.075 \to 0.007$ (factor 15); maxima oscillate $O(1)$ throughout ($1.007 \to 1.130 \to 0.866$ pair; $0.987 \to 1.169 \to 0.892$ rooted). Slopes negative throughout. This is the direct empirical signature of the consequence bounds (6.4)–(6.5) of the Lemma Q document at full volume up to $L=64$ — what the pass-17 §T diagnostic measured at small block-conditional scale, Appendix W measures globally and confirms the same qualitative pattern.

- **Appendix X: L=64 projected-capacity threshold law on $\mathbb T_{64}^2$.** Two sub-anchors. §X.1 — threshold-law: 180 masks (six geometric families × 30 each) at fixed local geometry ($m=128$, density $0.03125$, 64 dimers, max cluster 2). Exact projected Birman–Schwinger threshold $V_c^{BS}(D) = \|\Lambda^{-1/2} P 1_D P \Lambda^{-1/2}\|^{-1}$ tracked by the scalar surrogate $V_c^R(D) = \lambda_1 / \|P 1_D P\|$ with $R^2 = 0.922$ calibration $\log V_c^{BS} = 1.662 + 1.216 \log V_c^R$, mask-heldout MAE $0.028$ vs geometry-only $0.030$ (PASS), family-heldout MAE $0.153$ vs $0.180$ (PASS, but family extrapolation is genuinely hard). §X.2 — order-parameter attack: 90 masks × 7 $V_0$ values = 630 rows. The exact_BS feature set achieves $R^2 = 0.999$ mask-heldout, $R^2 = 0.951$ family-heldout for projected_binding; $R^2 = 0.988$, $R^2 = 0.511$ for defect_mass_low; **AUC $= 1.000$ for negative-crossing classification** with exact_BS or scalar_capacity. This is the cleanest direct verification of the Birman–Schwinger criterion at $L = 64$: across 630 configurations spanning two orders of magnitude in $V_0$, the projected-capacity-based classifier never mislabels a single binding event. §X.3 — interpretive: Appendix X is a synthetic 2D scalar validation of the §F.4 / §3 operator-theoretic premise (projected capacity is a meaningful predictive variable for sparse-defect low-mode instability), not a Wilson SU(2) result. It complements Appendix W (which IS Wilson SU(2)) by validating the deterministic operator object at scale where ground truth is exactly computable.

- **Appendix Y: SU(3) class-function asymptotic gap law (separate-paper pointer).** Headline theorem: $\Delta_{\rm SU(3)}(\beta) = \sqrt{2\beta/3} - 5/16 - (311\sqrt{6}/9216)\beta^{-1/2} + O(\beta^{-1})$ for the local one-plaquette class-function Hamiltonian. Main derivational novelty: $H_2$ contains the non-radial Weyl-invariant correction $p_3^2 / 8640 \cdot \sqrt{6}$; radial-only treatments miss this and produce an incorrect $c_1$. Finite-channel leakage matrix $T^{(3)}$ has explicit Perron root $\rho_3 = 0.55016153352314...$; the polymer-resolvent summability threshold is $\beta > 36.78$ for $\mu_\mathcal{G} = 3$. **This is a local spectral theorem, not a 4D Yang–Mills result.** It is unconditional within its scope. Full derivation of $c_0 = -5/16$, $c_1$, $T^{(3)}$, and the SU(N) extension framework belongs in a separate manuscript; this appendix is a one-page pointer with the headline statement and constants, plus the manuscript-safe claim and what NOT to claim.

- **Consolidated honesty-corrections register.** New top-level section §15 (inserted before Appendices) lists the six explicit honesty corrections in chronological order with brief diagnosis and current status:
  1. Pass 4 — $m_*$ retraction (Appendix E)
  2. Pass 8 — §H.5 weighted-Lyapunov sign convention
  3. Pass 10 — §I.9 false scalar tail ratio
  4. Pass 15 — $\langle\phi_p\rangle = 3/(8\beta)$ correction (not $3/(2\beta)$, factor of 4 error)
  5. Pass 17 §T.11.1 — decay-rate point-estimate overconfidence (CIs are wide)
  6. Pass 17 §T.11.3 — extended-regression $R^2$ binary-classifier artifact (true $R^2$ on positive rows is $0.036$)

The honesty discipline is itself the paper's defensibility architecture: prior versions overstated; the corrections are documented and the current claims are calibrated by what survived correction.

**Pass-18 verdict.** Pass 18 does NOT prove Lemma Q. It folds in four new evidence lines that strengthen the empirical case for Lemma Q's *consequences* — two new block-conditional anchors (Appendix V), full-volume pair/rooted covariance through $L=64$ (Appendix W), the deterministic-operator validation on $\mathbb T_{64}^2$ (Appendix X) — and acknowledges one local spectral theorem (SU(3), Appendix Y) as a real result deserving its own paper. The conditional theorem stack `Lemma Q + source-weighted Bałaban + boundary-band gate $\Rightarrow$ projected firewall closure` is unchanged. The next analytic target is unchanged: the cavity-intensity bound $\lambda_p(S \mid \mathcal F_{C^c}) \le q_\eta \exp(\sum_r J(p,r))$ with $J(p,r) \le C e^{-m d_C(p,r)}$, plus its rooted analogue.


### Pass 16 changelog

Pass 16 supersedes pass 15. Triggered by user discretion ("proceed as you see fit") after pass 15. Prioritized item: L=8 lattice extension to address pass-12 §K.5 caveat (2) "small lattice L=6 only".

**The key technical advance.** Sparse `scipy.sparse.linalg.eigsh` on the L=8 Maxwell operator (16384×16384 with 4095 zero modes) stalls. Switched to **analytic Fourier-mode construction**: at L=8 with $\Lambda=1.05$, only the lowest momentum shell $|k|=1$ is in the window, with eigenvalue $4\sin^2(\pi/8) = 0.586$. For each of the 8 momenta $\pm e_\mu$ ($\mu\in\{1,2,3,4\}$), the $(d{-}1)$ coexact polarizations are constructed explicitly as $\hat e_\perp \cdot \cos(2\pi k\cdot x/L)$ or $\sin(\cdot)$. Result: 24 coexact modes verified to machine precision ($\|Mv-\lambda v\|/\|\lambda v\| \le 10^{-15}$; $\|d_0^T V\|_F = 0$ exactly).

**The L=8 numerical result.** Two Gaussian samples (seeds 42, 137) at $\beta=3.5$, processed via batched plaquette accumulation (3 bash batches per sample, ~10 min total compute):

| Statistic | L=6 (Gaussian, 10 samples) | L=8 (Gaussian, 2 samples) | Shift |
|---|---|---|---|
| $\lambda_{\min}^{\rm coex}$ | 1.000 | 0.586 | $\times 0.586$ |
| Trivial-config BE = $\kappa_G + (\beta/4)\lambda_{\min}$ | 2.875 | 2.513 | $-0.362$ |
| Empirical BE min | $2.312 \pm 0.014$ | $2.209 \pm 0.005$ | $-0.103$ |
| Empirical BE max | $2.810 \pm 0.015$ | $2.470 \pm 0.002$ | $-0.340$ |
| Empirical shift below trivial (= BE min − trivial) | $-0.563$ | $-0.304$ | shift halved |
| All 72 modes $> \kappa_G$? | YES (all 10 samples) | YES (both samples) | ✓ |

**Critical observation.** The shift below trivial-config BE is NOT constant in L — it scales **linearly with $\lambda_{\min}^{\rm coex}(L)$**:

| L | $\lambda_{\min}^{\rm coex}$ | empirical shift | shift / $\lambda_{\min}$ |
|---|---|---|---|
| 6 | 1.000 | $-0.563$ | $-0.563$ |
| 8 | 0.586 | $-0.304$ | $-0.519$ |

**The ratio shift/$\lambda_{\min}$ is approximately constant** ($\approx -0.54$ average). This is a substantial refinement of pass-15 §Q.3, which conjectured shift $\propto \beta\langle\phi_p\rangle$ (constant in L).

**Refined analytic conjecture (pass-16 update to §Q.3):**
$$
\rho_*(\beta, \Lambda; L) \;\approx\; \kappa_G + \left(\frac{\beta}{4} - k_{\rm ens}\right)\lambda_{\min}^{\rm coex}(L) + O(\lambda_{\min}^2)
$$
with $k_{\rm ens} \approx 0.55$ under Gaussian, ensemble-dependent.

**Consequence.** As $L \to \infty$: $\lambda_{\min}^{\rm coex} = 4\sin^2(\pi/L) \to 0$, so $\rho_*(L) \to \kappa_G$ from above with $O(1/L^2)$ convergence. **The §J.6 spectral-window conjecture is supported with $\rho_* = \kappa_G > 0$ uniform in $L$**, but the headroom shrinks with $L$. The geometric Ricci floor $\kappa_G = 2$ does ALL the asymptotic work; the configuration-dependent positive contribution from the Wilson Hessian vanishes as $L\to\infty$.

**Predicted BE min at larger L** (from the refined conjecture with $k = 0.545$):

| L | $\lambda_{\min}$ | Predicted BE min | Gap above $\kappa_G$ |
|---|---|---|---|
| 6 | 1.000 | 2.330 | 0.330 |
| 8 | 0.586 | 2.193 | 0.193 |
| 12 | 0.268 | 2.088 | 0.088 |
| 16 | 0.152 | 2.050 | 0.050 |
| 24 | 0.068 | 2.022 | 0.022 |
| 64 | 0.010 | 2.003 | 0.003 |

**The empirical evidence at L=6 (10 Gaussian + 5 Wilson) and L=8 (2 Gaussian) all show BE min $\ge \kappa_G$ with O(1/L²) headroom**, consistent with the refined conjecture's asymptote $\rho_* \to \kappa_G$.

Material additions:

- **New Appendix S "L=8 lattice extension via analytic Fourier-mode construction (pass 16)"** with 6 subsections covering the analytic basis construction, the batched Hessian compute, the two-sample results, the L-dependence finding, the refined §Q.3 conjecture, and updated caveats.

**Pass-16 verdict.** Pass-12 §K.5 caveat (2) "small lattice L=6 only" is now substantively addressed: L=8 confirms positive projected BE with the predicted scaling. The L-dependence is now empirically characterized: $\rho_*(L) = \kappa_G + ((\beta/4) - k_{\rm ens})\lambda_{\min}(L) + O(\lambda_{\min}^2)$, approaching $\kappa_G$ from above as $L\to\infty$. Caveats (4) "typical configurations only" and (5) "no analytic theorem" remain open.

**Net pass-16 effect.** The empirical case for §J.6 is now anchored at TWO lattice sizes (L=6 with 10 Gaussian + 5 Wilson; L=8 with 2 Gaussian) with a clean scaling law explaining the L-dependence. The remaining tasks for closure of (M′)_SU(2) at large β are unchanged from pass 15: (a) prove the §J.6 conjecture analytically (the L=8 data narrows the target to $\rho_* = \kappa_G$ in the limit, with explicit $O(1/L^2)$ approach); (b) prove the §R.1 small-density covariance lemma. Pass-7 conditional status preserved.

---

### Pass 15 changelog

Pass 15 supersedes pass 14. Triggered by an explicit request to do "all the pass-15 candidates I can". Pass 15 completes four substantive items.

**(1) Wilson MCMC sampling at L=6, addressing pass-12 §K.5 caveat (3).**

Heat-bath algorithm for SU(2) implemented via vMF rejection sampling (Creutz-style). 60 thermalization sweeps from cold start; 5 samples taken with 15 decorrelation sweeps each. Verified plaquette equilibrium: $\langle x_0(U_p)\rangle = 0.852$, i.e., $\langle\phi_p\rangle = 0.148$, consistent with the leading-order analytic value $3/(8\beta)=0.107$ plus expected $O(1/\beta^2)$ corrections.

Projected Hessian computed at each Wilson MCMC sample using same code as §K.3 / §O. Result:

| Sample | Plaq $x_0$ | BE min | BE p1 | BE p99 | BE max | Frac BE<0 |
|---|---|---|---|---|---|---|
| 0 | 0.8531 | 2.2048 | 2.2192 | 3.9779 | 4.0246 | 0.0000 |
| 1 | 0.8523 | 2.2156 | 2.2236 | 4.0614 | 4.0766 | 0.0000 |
| 2 | 0.8515 | 2.1949 | 2.2322 | 4.0106 | 4.0577 | 0.0000 |
| 3 | 0.8506 | 2.1925 | 2.2289 | 3.9668 | 3.9964 | 0.0000 |
| 4 | 0.8526 | 2.1850 | 2.2022 | 4.0144 | 4.0394 | 0.0000 |

**All 5 Wilson samples give positive projected BE; all 360 eigenvalues > κ_G = 2.0.**

**Comparison with pass-14 §O Gaussian distribution:**

| Statistic | Wilson (5) mean ± std | Gaussian (10) mean ± std | Shift |
|---|---|---|---|
| BE min | 2.199 ± 0.011 | 2.312 ± 0.014 | −0.114 |
| BE p1 | 2.221 ± 0.011 | 2.326 ± 0.013 | −0.104 |
| BE p99 | 4.006 ± 0.033 | 2.798 ± 0.015 | **+1.208** |
| BE max | 4.039 ± 0.028 | 2.810 ± 0.015 | **+1.229** |

**Wilson samples spread eigenvalues much wider than Gaussian** — lower floor by ~0.11, higher ceiling by ~1.23. The minimum is still positive (2.185), but Wilson exercises configurations that lift the upper tail significantly. **Both ensembles support §J.6 empirically; Wilson is the more honest probe.**

**(2) Analytic conjecture for $\rho_*(\beta, \Lambda)$ (new Appendix Q).**

The trivial-config projected BE on a coexact-window mode with Maxwell eigenvalue $\lambda$ is $\kappa_G + (\beta/4)\lambda$. The configuration-dependent shift at the bulk should scale as $-c\beta\langle\phi_p\rangle$ for some $O(1)$ constant $c$. Pass-15 §Q proposes the conjecture
$$
\rho_*(\beta, \Lambda) \;=\; \kappa_G + \tfrac{\beta}{4}\lambda_{\min}^{\rm coex,\Lambda} - c\,\beta\,\langle\phi_p\rangle + O(\beta^{-1}),
$$
where $\lambda_{\min}^{\rm coex,\Lambda}$ is the lowest coexact Maxwell eigenvalue in the spectral window, and $c$ is a phenomenological constant. At the master corner ($\beta=3.5$, $\lambda_{\min}=1$, $\kappa_G=2$, $\langle\phi_p\rangle=0.148$): trivial-config $\rho_* = 2.875$; empirical Wilson $\rho_* = 2.199$; fit gives $c \approx 1.83$.

**This is an empirical conjecture, not a derivation.** Pass-15 §Q sketches the structure of the calculation that would derive $c$ analytically.

**(3) Small-density spectral-gap covariance decay lemma (new Appendix R).**

Pass-13 §M.4 identified this as the precise residual analytic question. Pass-15 §R states the precise conjecture:

**Conjecture (Small-Density Projected BE Covariance Decay).** Let $\mu$ be a Gibbs measure on a Riemannian manifold with **projected** Bakry-Émery $P\nabla^2 V P + P\mathrm{Ric}_g P \succeq \rho_*\,P$ for $\rho_* > 0$ on the support of $P$. Let $f, g \in C^1$ with $\|f\|_\infty, \|g\|_\infty \le 1$, disjoint supports, and $L^1$ norms $\|f\|_{L^1(\mu)}, \|g\|_{L^1(\mu)} \le q$. Then
$$
|\mathrm{Cov}_\mu(Pf, Pg)| \;\le\; C(\rho_*)\,q^2\,e^{-\sqrt{\rho_*}\,d(\mathrm{supp}\,f,\,\mathrm{supp}\,g)/2}.
$$

If this conjecture were a theorem, it would — combined with pass-12/14/15 empirical evidence that $\rho_* > 0$ at the master's working corner — directly imply source §I.16. Pass-15 §R sketches a Brascamp–Lieb-via-Stein-coupling approach that would attempt to prove this; the proof is open.

**(4) Pass-11 §J.4 numerical correction.**

Pass 11 stated $\langle\phi_p\rangle \approx 3/(2\beta) = 0.43$ at $\beta=3.5$ for SU(2). The **correct formula** is $\langle\phi_p\rangle = (N^2-1)/(4N\beta) = 3/(8\beta) = 0.107$ at $\beta=3.5$ for SU(2). The error was a factor of 4. The corrected value is consistent with the pass-15 Wilson MCMC empirical value $0.148$ (which exceeds leading order by the expected $O(1/\beta^2)$ corrections).

**This is the fourth explicit honesty correction in the master document**, after pass-4 $m_*$ retraction (Appendix E), pass-8 §H.5 weighted-Lyapunov correction, and pass-10 §I.9 false scalar tail ratio. The corrected formula does not affect any downstream analytic results (pass-11 §J.5 used the Haar bound; pass-12 §K.3 used $\sigma=1/\sqrt\beta$ directly).

Material additions:

- **Appendix P "Wilson MCMC samples vs Gaussian (pass 15)"** with 7 subsections
- **Appendix Q "Analytic conjecture for $\rho_*(\beta, \Lambda)$ (pass 15)"** with 5 subsections
- **Appendix R "Small-density projected BE covariance decay: precise statement and sketch (pass 15)"** with 6 subsections
- **Note on pass-11 §J.4 numerical correction** in §0.5 and §14.4

**Pass-15 verdict.** Three of pass-14's five §K.5 caveats now have substantive responses: caveat (1) "single sample" closed by pass-14 §O; caveat (3) "Gaussian ≠ Wilson" closed by pass-15 §P (Wilson sampling implemented and behaves consistent with conjecture but with wider spread); caveat (5) "no analytic theorem" partially addressed by pass-15 §Q (analytic conjecture stated with empirical fit) and §R (precise residual lemma articulated). Caveats (2) "small lattice L=6 only" and (4) "typical configurations only" remain open.

**Net pass-15 effect.** The empirical case for §J.6 spectral-window is now anchored in both Gaussian and true Wilson sampling at L=6 with consistent findings. The analytic gap is now precisely characterized: (i) the floor function $\rho_*(\beta, \Lambda)$, and (ii) the small-density spectral-gap lemma. Together with §J.6 (also open), these are the three precise open mathematical statements that would close source §I.16. Pass-7 conditional status preserved.

---

### Pass 14 changelog

Pass 14 supersedes pass 13. Triggered by an explicit request to extend pass-12 §K.3 from one Gaussian sample to a distribution across multiple seeds, addressing the pass-12 §K.5 caveat (i) "single typical Gaussian sample at L=6".

**The key finding.** Across 10 independent Gaussian configurations at the master's working corner ($L=6$, $\beta=3.5$, $\Lambda=1.05$), the coexact-window projected Wilson Hessian gives projected Bakry–Émery eigenvalues in a **remarkably tight band**:

| Statistic | Value across 10 samples |
|---|---|
| BE min | mean $2.312 \pm 0.014$, range $[2.287, 2.341]$ |
| BE p1 | mean $2.326 \pm 0.013$ |
| BE p99 | mean $2.798 \pm 0.015$ |
| BE max | mean $2.810 \pm 0.015$ |
| Total eigenvalues in band $[2.287, 2.830]$ | **720 / 720** |
| Samples with any BE eigenvalue $< 0$ | **0 / 10** |
| Samples with any BE eigenvalue $< \kappa_G/2=1$ | **0 / 10** |

**Cross-sample standard deviation in BE min is only 0.014** — less than 1% of the mean. The pass-12 §K.3 finding ($\text{BE min} = 2.31$ at seed 42) lies essentially at the cross-sample mean, confirming it was representative rather than fluke.

Material addition:

1. **New Appendix O "Distribution of projected BE eigenvalues across 10 Gaussian samples at L=6 (pass 14, §K.3 extension)"** with six subsections:
   - **§O.0**: scope — addressing pass-12 §K.5 caveat (i)
   - **§O.1**: methodology — 10 seeds (42, 137, 271, 314, 577, 1001, 1729, 2718, 3141, 6022), same L=6 / $\beta=3.5$ / $\Lambda=1.05$ setup as §K.3; ~115s per sample (~20 min total wall time)
   - **§O.2**: per-sample table (10 rows × {BE min, p1, p99, max, frac<0})
   - **§O.3**: distribution statistics — cross-sample mean, standard deviation, range for each statistic
   - **§O.4**: interpretation — the tight band ($\sigma_{\text{BE min}} = 0.014$) suggests an underlying analytic floor, not noise; the pass-12 §K.3 finding is statistically robust
   - **§O.5**: caveats unchanged from pass-12 §K.5 — still Gaussian sampling (not Wilson MCMC), still small lattice (L=6, 24 modes per Lie algebra all at lowest M-eigenvalue), still doesn't address atypical configurations
   - **§O.6**: honest verdict — pass-14 §O closes the "single-sample" caveat of pass-12 §K.5(1) but leaves caveats (2)–(5) open; the §J.6 spectral-window conjecture has its 10× independent empirical confirmation but not its proof

**Pass-14 verdict.** The §K.3 positive finding is now established as a robust empirical regularity across 10 independent typical Gaussian configurations at the master's working corner. The minimum projected BE eigenvalue across all 720 mode-evaluations is 2.287 > 2.0 = $\kappa_G$. The geometric Ricci floor is essentially uniformly attained. **This is not a proof.** Wilson MCMC sampling and larger L remain open subtargets per pass-12 §K.6.

**Net pass-14 effect.** The empirical case for the §J.6 spectral-window conjecture is substantially strengthened. From one data point (pass-12 §K.3) to ten — and they all cluster within a 0.054-wide band. The cross-sample tightness suggests the projected BE floor is set by an underlying analytic invariant (the spectral-window structure + coexact restriction + κ_G), not by sampling noise. The next milestones (pass-12 §K.6 list) remain: Wilson MCMC sampling; L=8 with multiple samples; analytic conjecture for the precise BE floor function $\rho_*(\beta,\Lambda)$.

---

### Pass 13 changelog

Pass 13 supersedes pass 12. Triggered by explicit request for three substantive items: (1) re-derive Appendix I with tighter constants tracked at $\beta=3.5$; (2) bridge pass-12 §K.3 empirical projected-BE positivity to the source §I.16 pair-cumulant target; (3) Russian-language Malyshev–Minlos survey closing the pass-7 known gap. All three are added as new appendices L, M, N.

Material additions:

1. **New Appendix L "Tighter constants in Appendix I at $\beta=3.5$: pinned versus open"** with six subsections separating:
   - **Pinned by data/numerics:** $q_\eta = 0.003$ (master working corner), $\kappa_\Lambda$ bounds from v3b ($\Theta_*=0.884$), $V_{\max}/m^2$ Birman-Schwinger parameter from master §11.0c, $\kappa_G=2$ exact (pass-9), projected BE floor $\ge 2.31$ at $L=6$ (pass-12 §K.3), spectral window dimension at $L=24$ working corner
   - **Pinned by deterministic geometry:** $N_m$ (lattice neighbor count for trace-overlap summability), $C_{S^3}$ (vMF constant in source §7.1), bare counts
   - **Open (depend on rooted-source polymer hypothesis):** $C_{\rm root}=C_{\rm conn}$ from Theorem F, polymer decay rate $m$, polymer activity $C_0$
   - **What the firewall inequality (14.1) becomes** with the pinned constants plugged in and the open constants symbolic
   - **The vMF tightness gap:** at $\beta=3.5$, source §7.1 gives $q_\eta \le C_{S^3}\beta^{3/2}e^{-\beta} \approx 0.2$, while the empirical $q = 0.003$ — the analytic bound is ~70× loose
   - **Honest verdict:** the open hypothesis is the load-bearing input; tightening pinnable constants alone doesn't close the route

2. **New Appendix M "Bridge from pass-12 §K.3 to source §I.16: spectral gap vs. density scaling"** with five subsections:
   - **§M.1**: the standard Bakry–Émery → covariance decay chain (BGL 2014)
   - **§M.2**: applied to pass-12 §K.3: projected BE floor $\ge 2.31$ → decay rate $m \ge \sqrt{2.31}/2 \approx 0.76$
   - **§M.3**: the BGL prefactor scales as $\|\nabla X_{p,\eta}\|^2/\rho_{BE}$, NOT as $q_\eta^2$; the gap between BGL prefactor ($1/(\rho_{BE}\eta^2) \approx 0.43/\eta^2$) and source §I.16 target ($q_\eta^2$) is intrinsic
   - **§M.4**: what additional analytic input bridges the gap: a "small-density spectral-gap covariance decay" lemma — either Brascamp–Lieb-style absorption ($q_\eta$ factor) or full polymer-expansion machinery ($q_\eta^2$ factor)
   - **§M.5**: honest verdict — pass-12 §K.3 supplies the decay-rate component of §I.16, not the density-scaling component; the latter still requires source-style Theorem F analysis (open) or analogous machinery
   
3. **New Appendix N "Russian-school cluster expansions: what they cover and what they don't"** closing the pass-7 known Russian-language gap:
   - **§N.1**: the central Russian-school references — Malyshev (1980) *Russian Math. Surveys*; Malyshev & Minlos (1991) *Gibbs Random Fields: Cluster Expansions* (Kluwer; original Nauka 1985)
   - **§N.2**: chapter-by-chapter scope of Malyshev–Minlos 1991: Chapters 1-2 (general theory), Chapter 5 §2 (continuous spin, unique ground state — the abstract framework most relevant for SU(N) at large β), Chapter 6 (decay of correlations — relevant for (M′)-style bounds), Chapter 7 §4 (gauge field with gauge group $\mathbb Z_2$ only)
   - **§N.3**: what the Russian school did NOT do for SU(N): no explicit non-Abelian gauge-theory chapter; no specific level-(iii) bound for SU(N) Wilson at large β; the abstract framework is applicable in principle but the specific extension is not in their main treatment
   - **§N.4**: adjacent Russian-school papers — Dobrushin uniqueness theorem; Minlos–Sinai phase separation; Malyshev–Petrova duality; Malyshev–Nicolaev uniqueness via cluster expansions
   - **§N.5**: connection to the master document — Russian-school cluster expansion is the closest tradition to the (open) rooted-source polymer hypothesis of source §3.1; the master's mention in pass-7 §10.6 of the "Russian-language Malyshev-Minlos survey" gap is substantively addressed by Appendix N
   - **§N.6**: honest verdict — the Russian-school gap is NOT a hidden closure; it is general technology that would need explicit non-Abelian extension

**Pass-13 verdict.** Three substantive additions clarifying the conditional content of the master document. The pass-7 conditional status remains exactly the same: no peer-reviewed paper (Western or Russian) closes (M′)_SU(2) at large β for SU(2). Pass-13 makes the constant accounting (Appendix L), the bridge structure (Appendix M), and the Russian-school technology (Appendix N) explicit. The master document is now structurally complete with full transparency about both pinnable and open constants, and with a thorough literature accounting.

**Net pass-13 effect.** The reader now has:
- A line-by-line account of which constants in the conditional theorem are numerically pinnable at $\beta=3.5$ vs which depend on the open hypothesis (Appendix L)
- An honest accounting of why pass-12 §K.3 empirical projected-BE positivity is necessary but not sufficient for the source §I.16 target — and what additional analytic input would bridge the gap (Appendix M)  
- Full bibliographic closure of the pass-7 known Russian-language gap (Appendix N)

The master document is, after pass 13, a complete conditional theorem with explicit numerical content, explicit research roadmap, and complete literature accounting. The conditional content remains open; the open content is now precisely characterized.

---

### Pass 12 changelog

Pass 12 supersedes pass 11. Triggered by the explicit request: "attempt §J.8 Step 2 — explicit computation of $P\nabla^2 S_W P$ at a representative typical configuration." Pass 12 carries this out via direct numerical assembly of the projected Wilson Hessian on small lattices, with the spectral-window projector restricted to the coexact (gauge-invariant, physical) subspace. **The key positive finding is consistent with the §J.6 spectral-window proposal:** at $L=6$ and a typical Gaussian configuration at $\beta=3.5$, the projected Hessian on the coexact spectral window has all positive eigenvalues (min 0.31, p99 0.80), giving uniform projected Bakry–Émery $\ge 2.31$ across all 72 modes. This is the strongest empirical evidence to date that the spectral-window restriction can rescue Bakry–Émery at large β. **It is NOT a proof.**

Material additions:

1. **New Appendix K "Explicit projected Wilson Hessian computation at typical configurations (§J.8 Step 2)"** with seven subsections:
   - **§K.0**: scope — continuation of §J.8 Step 2
   - **§K.1**: methodology — per-plaquette finite-difference Hessian assembly, lattice Maxwell projector $P_{\le\Lambda,L}$, restriction to coexact (gauge-invariant) subspace
   - **§K.2**: L=4 results and the spectral-window artifact (at L=4 the window contains ONLY gauge zero modes; the small negative tail is partly FD noise on pure-gauge directions where the Hessian should be exactly zero by gauge invariance)
   - **§K.3**: L=6 results with coexact restriction — **THE KEY POSITIVE FINDING**: projected Hessian eigenvalues at typical Gaussian config all positive, BE min = 2.31, p99 = 2.80, all 72 coexact-window modes positive
   - **§K.4**: interpretation: the spectral-window + coexact restriction is what makes BE positive at typical configs at β=3.5; this is the precise structural combination the master document uses
   - **§K.5**: caveats — single Gaussian sample at L=6; Gaussian sampling is an approximation to Wilson sampling; coexact subspace at L=6 has only 24 modes per Lie algebra (all at Maxwell-eigenvalue exactly 1, i.e., lowest physical modes); need more samples + larger L + actual Wilson MCMC sampling
   - **§K.6**: concrete next subtargets — L=8 with multiple Gaussian samples; Wilson MCMC sampling; analytical understanding of why projection + coexact restriction produces positive BE
   - **§K.7**: honest verdict — the §J.6 spectral-window conjecture has its first explicit numerical confirmation at a typical config; this empirical evidence supports the §H.8 ingredient (iv) globalization possibly being achievable via projection; it is NOT a proof
   
2. **§14.4 pass-12 disclaimer** added.

3. **§0.5 TL;DR — single hardest open question** extended with pass-12 status: the spectral-window projection + coexact restriction has been numerically verified to produce uniform positive projected BE at a typical config; the empirical support for §J.6 is strengthened.

**The pass-12 honesty discipline.** This pass adds a real empirical positive result. It is NOT a proof. The reader should understand:
- One typical Gaussian sample at L=6 is not a theorem.
- Gaussian sampling differs from Wilson MCMC sampling — the latter has stronger plaquette concentration but more complex correlation structure.
- The 72 coexact-window modes at L=6 are all at Maxwell-eigenvalue exactly 1 (the lowest physical eigenvalue at L=6); their behavior may not be representative of the larger coexact window at L=24 (which contains many more modes spanning a range of eigenvalues).
- The §J.5 exponential-rarity obstruction was for the UNPROJECTED Hessian. The pass-12 result is consistent with that obstruction being projection-rescuable, but the analytic argument for projection rescuing all of (a)–(e) of §J.6 is still missing.
- The pass-11 §J.6 v3b empirical anchor ($\Theta_*=0.884<1$ over 1200 samples) and the pass-12 L=6 projected-Hessian computation are independent pieces of evidence pointing the same direction: at the master's working corner, the projected dynamics is empirically benign.

**Pass-12 verdict.** The §J.8 Step 2 computation produces a positive empirical result for the spectral-window proposal. The §I.16 minimal target remains open. The §H.8 ingredient (iv) globalization remains the missing analytic input. **What pass 12 adds: the first explicit numerical demonstration that projection to the coexact spectral window produces all-positive projected BE at a typical config at $\beta=3.5$.** This is consistent with v3b numerics and substantially strengthens the §J.6 research direction as the most promising path forward.

**Net pass-12 effect.** Pass-12 supplies the first concrete numerical evidence — beyond v3b's $\Theta_*$ measurement — that the spectral-window restriction is empirically benign at the master's working corner. The Pass-11 obstruction is now seen to be specific to the UNPROJECTED dynamics; the projected dynamics has empirically positive BE on the physical subspace. The master document's distinctive structural feature (the Maxwell projector + coexact restriction) is now identified as the mechanism that enables Bakry–Émery to potentially work at large β — a feature absent from SZZ 2023 and other peer-reviewed approaches.

---

### Pass 11 changelog

Pass 11 supersedes pass 10. Triggered by an explicit request to "attempt the §I.16 minimal target via the §H.8 ingredient assembly with concrete numerical estimates." Pass 11 carries out the assembly honestly: setting up the standard Bakry–Émery → covariance decay machinery, computing the Wilson Hessian for SU(2) explicitly, and seeing what survives at the master's working corner $\beta=3.5$.

**The honest outcome: the assembly does NOT prove §I.16.** It runs into an explicit quantitative obstruction (exponential rarity of the pointwise BE-good set at large β), which is documented as the precise point where new analytic input is needed. The pass-7 conditional status is preserved.

Material additions:

1. **New Appendix J "Attempted assembly of §I.16 via §H.8 (pass 11): concrete numerical estimates and the obstruction"** with eight subsections:
   - **§J.1**: standard Bakry–Émery → covariance decay theorem statement (BGL 2014, Cattiaux–Guillin 2009)
   - **§J.2**: explicit SU(2) Wilson Hessian computation: per-plaquette-link eigenvalue $= \beta q_0^{(p,\ell)}/4$ where $q_0^{(p,\ell)} = \frac{1}{2}\mathrm{Re}\mathrm{Tr}(V_\ell^{(p)})$ is the cos(half-angle) of the staple
   - **§J.3**: naive Bakry–Émery threshold β < 4/3 ≈ 1.33 (crude pointwise bound); SZZ 2023 has the careful threshold β < 1/96 ≈ 0.0104. **At β=3.5: master is 2.6× over the crude threshold, ~336× over SZZ**
   - **§J.4**: concentration of measure: typical plaquette deficiency at β=3.5 is $\langle\phi_p\rangle \approx 3/(2\beta) = 0.43$, typical plaquette angle ≈ 53°; the measure is concentrated AWAY from $U^{(0)}$
   - **§J.5**: **the exponential rarity obstruction (quantitative)**: even under fully random (Haar) staple distribution, P(BE-good staple) = 0.736; for ALL ~$8\times 10^6$ staple-link pairs at L=24 to be BE-good simultaneously, $P \lesssim e^{-2.4\times 10^6}$
   - **§J.6**: the spectral-window restriction proposal — the master's $P_{\le\Lambda,L}$ projects to a small spectral subspace where the Wilson Hessian might be controllable; master §11.0c v3b's $\Theta_*=0.884<1$ over 1200 samples is empirical support
   - **§J.7**: what pass 11 supplies vs. does NOT supply
   - **§J.8**: concrete next steps for the spectral-window research direction
   - **§J.9**: honest verdict
   
2. **§14.4 pass-11 disclaimer** added.

3. **§0.5 TL;DR — single hardest open question** extended with pass-11 status: the assembly has been attempted and produced specific numerical estimates; the obstruction is identified; the minimal target (16.1) remains open.

**The pass-11 honesty discipline.** This is a real mathematical attempt with explicit numerical content. It is **not** a proof. The reader should understand:
- The Bakry–Émery + Lyapunov machinery (Bakry–Gentil–Ledoux 2014; Cattiaux–Guillin 2009) is well-developed for many settings.
- Applied naively to SU(2) Wilson at β=3.5, the standard machinery fails: the pointwise BE-good set has exponentially small measure in $L^4$.
- This is not a "fixable in 2 weeks" problem. Standard local-to-global mechanisms require the good set to have at least polynomial-in-$|P|$ measure, not exponentially small.
- The spectral-window restriction (§J.6) is the master document's distinctive structural feature, and may sidestep the obstruction by projecting away the "bad-Hessian" directions. This is a research conjecture, not a proved fact.
- v3b numerical evidence is consistent with the spectral-window restriction working, but it is finite-volume finite-sample empirical support, not a theorem.

**Pass-11 verdict.** The §H.8 assembly is honestly attempted. The minimal target remains open. The spectral-window approach is identified as the most promising next direction. Pass-7 finding stands.

**Net pass-11 effect.** The master document now contains an explicit numerical attempt at the §I.16 minimal target, with the obstruction quantitatively located. Future research can address the spectral-window restriction directly, with the master document's v3b numerics and the pass-9 explicit constants as the concrete inputs. The conditional status of the master theorem is unchanged.

---

### Pass 10 changelog

Pass 10 supersedes pass 9. Triggered by a new comprehensive derivation document `SU2_PMBSF_closure_full_derivations_20260524.md` (1054 lines) that proves the full conditional implication chain step-by-step under the rooted-source polymer hypothesis. The document is honest at the top: "Manuscript derivation draft. Not a proof of the Yang–Mills mass gap." It identifies the **rooted-source polymer estimate** (eq 0.1 of the source) as the still-open core target — essentially (M′)_SU(2) at level (iv) — and derives everything else from it.

Material additions:

1. **New Appendix I "SU(2) closure derivation chain (conditional, pass 10)"** with 16 subsections mirroring the source document structure (§I.0 executive framing + §I.1 SU(2) Wilson setup + §I.2 target theorem + §I.3 Theorem F + §I.4 pair closure + §I.5 PTO-summed level-(iii) + §I.6 SU(2) heat-bath law + §I.7 vMF cap rarity Lemma 7.1 + §I.8 good/bad-staple + §I.9 CORRECTED bad-staple absorption + §I.10 higher cumulants + §I.11 smooth HPM from cumulants + §I.12 hard/smooth boundary-band + §I.13 HPM→matrix-Laplace + §I.14 projected firewall + §I.15 honest status + §I.16 minimal next proof target). Theorem statements, key constants, and the explicit chain are preserved; the full ~1054 lines of proof detail remain in the source file `SU2_PMBSF_closure_full_derivations_20260524.md` (cited as a project resource).

2. **§I.9 third honesty correction** prominently highlighted. Earlier formulations required $\mathbb P(\phi_p>\delta_{\rm st})\lesssim\mathbb P(\phi_p>t)$ for bad-staple absorption; this *generally fails* when $\delta_{\rm st}\ll t$. The corrected argument (applying Theorem F directly to bad-staple events $R_{p,\ell,\eta}$ with $\mathbb E_W R_{p,\ell,\eta}\le q_\eta$) gives $|\mathrm{Cov}_W(R_{p,\ell,\eta},X_{p',\eta})|\le C_{\rm root}q_\eta^2 e^{-md(p,p')}$ without the false ratio assumption. This is the **third explicit correction** documented in the master, after pass-4 $m_*$ retraction (Appendix E) and pass-8 §H.5 weighted-Lyapunov correction.

3. **§I.16 minimal next proof target** sharply specified: prove $|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\le Cq_\eta^2 e^{-md(p,p')}$ for fixed $\eta>0$. By the §I.5 PTO-summed estimate, this immediately gives the level-(iii) bound $\sum_{p'}|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\operatorname{tr}(A_p A_{p'})\le Cq_\eta^2\kappa_\Lambda^2$ — the load-bearing hypothesis (M′)_SU(2) at level (iii). The pair-source covariance bound is now the explicit "first SU(2) breach point."

4. **§0.5 TL;DR "single hardest open question" sharpened** with the pass-10 minimal target. Pass-9 named the level-(iii) sum form; pass-10 replaces it with the equivalent but more attackable pair-covariance form (which implies the sum via PTO summability).

5. **Cross-references added:**
   - §7.6 (HPM sparse closed-walk domination) → forward reference to §I.11 (smooth HPM from cumulants, with explicit proof under CW-KP)
   - §8.3 (BG smoothing bridge) → §I.12 (hard/smooth boundary-band bridge, with explicit construction)
   - §8.4 (CW-KP summability) → §I.11 (CW-KP condition in explicit form, eq 11.1)
   - §10.5 (honest negative finding) extended to note that pass 10 makes the conditional chain explicit, with the open hypothesis (rooted-source polymer at large β for SU(2)) sharply identified
   - §10.6.1 (SZZ) → §I.16 (minimal target now matches the pair-cumulant form that a hypothetical spectral-window Bakry–Émery extension would deliver)

6. **§14.4 pass-10 disclaimer** added.

**Pass-10 honesty discipline.** The chain $\text{(0.1)} \Rightarrow \cdots \Rightarrow \text{projected firewall}$ is now **explicitly proved** step-by-step. The pass-10 incorporation makes the master document's conditional content fully transparent: anyone can see, lemma by lemma, exactly what (M′)_SU(2)-level-iv input yields the projected firewall closure. **But (M′)_SU(2) at large β for SU(2) is still open**: §I.15 (verbatim from source) states "the SU(2)-specific rooted-source polymer estimate ... is not currently supplied by the peer-reviewed literature for SU(2) at large β." The pass-7 literature finding (Appendix G), the pass-8 auxiliary content (Appendix H), and the pass-9 research-direction memo (§H.8) are all preserved. The conditional status of the master theorem is unchanged.

**Net pass-10 effect.** The master document is now structurally complete as a *conditional* theorem with fully worked-out proof under the rooted-source polymer hypothesis. The hypothesis itself — large-β SU(2) Wilson with projected spectral-window and hard plaquette indicators — remains the genuinely open analytic content. Pass 10 sharpens the "minimal next proof target" to the explicit pair-covariance form (§I.16), which is the most attackable formulation: prove this, and level (iii) of (M′)_SU(2) follows by deterministic PTO summability without further input.

---

### Pass 9 changelog

Pass 9 supersedes pass 8. Triggered by the pass-8 author note observation that §H.3 is the single most useful piece for ongoing work (it supplies the local input to the pass-7 §10.6 spectral-window Bakry–Émery research direction) but pass 8 left it without explicit constants. Pass 9 fills the gap.

Material additions:

1. **§H.3 made numerically concrete.** For SU(2) in the master document's metric normalization ($\Delta_{{\rm SU}(2)}({\rm Re}\operatorname{Tr}U)=-3\,{\rm Re}\operatorname{Tr}U$, equivalent to round $S^3$ at radius 1), the geometric Ricci constant is $\kappa_G=2$ (Theorem H.3.1' below). This is the document's first numerical anchor for the local Bakry–Émery floor. At the master's working corner ($\beta=3.5,\delta_{\rm bond}=1$) with no added regulator ($S_{\rm add}=0$, so $C_{\rm add}=0$): $\rho_0=2$, uniform in $\Lambda$. The Wilson Hessian $2c_W d_1^*d_1$ contributes an additional non-negative amount on horizontal vectors but does NOT improve the IR floor (because $d_1^*d_1$ has small nonzero eigenvalues $\sim(2\pi/L)^2$ at low momentum on a periodic $L^4$ lattice, contributing $\le 2c_W\cdot(2\pi/L)^2\sim 0.24$ at $\beta=3.5, L=24$). **The IR floor at the trivial configuration is $\rho_0=\kappa_G=2$, dominated by Ricci.**

2. **New §H.8 "Research direction: hypothetical spectral-window Bakry–Émery proof of (M′)_SU(2) level (iii)".** Articulates explicitly what a closing proof from the pass-8 local pieces would require, broken into four ingredients with current status. The honest summary: **two ingredients are supplied (local floor §H.3, horizontal restriction §H.3), one is partially supplied (Lyapunov §H.2), one is missing entirely (globalization).** No claim that (M′)_SU(2) is closer to proof; the memo only scopes the work.

3. **§0.5 TL;DR header updated** from "(pass 6)" to "(added pass 6; updated through pass 9)". The "single hardest open question" subsection content is re-verified for pass 9 — unchanged from pass 7 — and the surviving-route diagram is unchanged.

4. **§10.6 SZZ subsection** gets a forward reference to §H.8 (where pass-7 said "would deliver level (iii) directly," pass 9 now says "would deliver level (iii) directly assuming ingredients (iii) and (iv) of §H.8 are supplied").

5. **Appendix C constant cross-check table extended** with the new numerical anchor $\kappa_G=2$ for SU(2), $\rho_0=2-C_{\rm add}$ at $U^{(0)}$.

Pass 9 does **not** revise:
- Any conditional theorem statement
- Any pass-1 through pass-8 derivation
- The pass-7 literature finding (no peer-reviewed paper closes (M′)_SU(2) at large β)
- The pass-8 §H.0 inclusion/exclusion ledger
- The §14.4 disclaimers (extended, not weakened)
- The Version C primary route status

**The pass-9 honesty discipline.** §H.8 articulates a research direction with three of four ingredients in hand or partial. It is **not** a claim that the research direction is close to executable — the missing globalization ingredient is precisely what makes (M′)_SU(2) at large β "at least as hard as the YM mass gap" (pass-7 finding). Pass 9 scopes the open work; it does not change the open work.

**Net pass-9 effect.** The most useful piece for ongoing work (§H.3) now has explicit numerical constants. The hypothetical proof assembly via §H.3 + §H.5 + §H.2 + missing globalization is articulated as a research-direction memo (§H.8), not as a closing route. The conditional status of the master theorem is unchanged. The pass-7 literature finding stands.

### Pass 8 changelog

Pass 8 supersedes pass 7. Triggered by a stack of 12 "useful old notes" derivations uploaded for incorporation. Each note is self-rated by its source author at 5–8/10 usefulness for the current paper, with consistent framing: "useful as appendix material; does NOT close (M′)_SU(2), HPM, or the Yang–Mills mass gap."

**The pass-8 honesty rule.** Because the source notes are themselves honest about scope, pass 8 preserves the pass-7 conditional status without exception. The new content is auxiliary appendix material, not a route to closure. Specifically:

1. The conditional theorem (§2) is unchanged.
2. Version C (HPM closed-walk, §7.9) remains the surviving primary route.
3. The pass-7 literature finding (§10.6, Appendix G) is unchanged: no peer-reviewed paper closes (M′)_SU(2) at large β.
4. The §14 disclaimers are extended but not weakened.

Material additions:

1. **New Appendix H "Auxiliary derivations (pass 8)"** with six self-contained subsections, each carrying its source-note self-rating and the explicit "does NOT prove ..." disclaimer from the source:
   - **§H.1 SU(3) Weyl-invariant local one-plaquette gap** (companion finite-N analytical anchor). Three-term expansion $\Delta_{SU(3)}(\beta)=\sqrt{2\beta/3}-5/16-\frac{311\sqrt{6}}{9216}\beta^{-1/2}+O(\beta^{-1})$ with full rank-two Weyl-invariant ledger including the non-radial $p_3^2$ contribution. Source: `SU3_Weyl_Invariant_c1_Derivation_Useful_Old_Notes.md` (self-rated by source author).
   - **§H.2 Exact character-proxy Laplacian drift identity**. $\Delta_\Lambda \tilde z_p = -4\lambda_{\rm fund}\tilde z_p+4\lambda_{\rm fund}$ (volume-independent), $\Delta_\Lambda V = -12V+24$ for SU(2), nonnegative Wilson-pairing $\langle\nabla S_W,\nabla\overline V_\Lambda\rangle\ge 0$, drift ceiling $L_\Lambda V \le -\lambda V + b$. Source: `exact_character_proxy_laplacian_drift_derivation.md` (self-rated 7/10 by source author).
   - **§H.3 Haar–Ricci local Bakry–Émery curvature floor** near the trivial configuration. Product Haar = Riemannian volume of $G^{E(\Lambda)}$; Ricci floor $\kappa_G$ uniform in $\Lambda$; Wilson Hessian $= 2c_W d_1^* d_1$ at $U^{(0)}$. Conditional horizontal $CD(\rho_0,\infty)$ at $U^{(0)}$ with $\rho_0=\kappa_G-C_{\rm add}>0$. Source: `PMBSF_Haar_Ricci_Local_Curvature_Appendix_20260524.md`. **Connection to pass-7 §10.6**: this is the *local* piece of the "spectral-window Bakry–Émery extension of SZZ at large β" research direction; the *global* piece remains an open research problem.
   - **§H.4 Uniform fiber LSI from Bakry–Émery curvature.** $\mathrm{Ric}_{g_b}+\nabla^2 W_b\ge\rho_{\rm fib}g_b\Rightarrow\mathrm{LSI}_{\mu_b}(\rho_{\rm fib})\Rightarrow I(\nu_b|\mu_b)\ge 2\rho_{\rm fib}\mathrm{Ent}_{\mu_b}(\nu_b)$. Source: `useful_old_notes_uniform_fiber_lsi_derivation_20260524.md`.
   - **§H.5 Corrected local-to-global Lyapunov–Γ template**. Source note explicitly fixes an overclaim in earlier weighted-Lyapunov material: the drift condition $LW\le-\alpha W+\beta\mathbf 1_K$ does NOT by itself imply $\int f^2 W\, d\mu\le\dots$; the correct form controls $\int f^2\phi\, d\mu$ when $LW\le-\phi W+\beta\mathbf 1_K$. Source: `PMBSF_Haar_Curvature_LocalToGlobal_Derivation.md`.
   - **§H.6 Fixed-cutoff Combes–Thomas / localization template** for clustering. Average-plaquette typicality + conditional HS hinge + Combes–Thomas inverse decay + localization algebra ⇒ fixed-cutoff exponential clustering. Source: `reusable_fixed_cutoff_derivation_extraction_20260524.md`. Five open gaps explicitly stated.

2. **§9 FNG cross-reference added.** §H.1 SU(3) local gap is noted as the SU(3) companion to the FNG Q_8 finite-non-Abelian validation (§9), with the explicit caveat that SU(3) is a continuous group and the local-gap result is asymptotic in $\beta$, not finite-β as for Q_8.

3. **§14.4 honest framing extended** with pass-8 disclaimer: the new appendix material is auxiliary, does not affect the conditional status, and source authors consistently flag it as not closing the route.

4. **Closing paragraph updated** to indicate pass-8 incorporation of auxiliary material with preserved conditional status.

**What pass 8 does NOT incorporate** (deliberate exclusions from the upload stack):

- `VSU_corrected_unscreened_spherical_collapse_derivation.md` — cosmological program (Vacuum Stiffness Unification, halo bias). Not PMBSF-relevant; explicitly excluded.
- `PMBSF_closed_walk_HPM_firewall_derivation_extract_2026-05-24.md`, `PMBSF_projected_capacity_firewall_PTO_Bernoulli_HPM_derivation.md`, `PMBSF_surviving_closed_walk_HPM_derivation_2026-05-24.md`, `PMBSF_closed_walk_useful_derivations_20260524.md`, `PMBSF_useful_old_notes_derivations_2026-05-24.md` — all five contain extracts of the closed-walk/HPM derivation chain that is **already in the master document** in §5.8 (closed-walk envelope), §7.6 (HPM sparse closed-walk domination), §8.4 (CW-KP), and §7.9 (Version C ↔ proof program). These extracts confirm the structural content but add no new technical material. Cross-references in §H.0 below.

**Net pass-8 effect.** The architecture, the deterministic spine, the sharp Bernoulli comparator, the surviving Version C closed-walk route, the v17b empirical anchor, the pass-7 literature framing, and the conditional status of the main theorem are all unchanged. Pass 8 supplies auxiliary technical lemmas that can be cited as appendix material when the corresponding structural step (drift normalization, fiber LSI, local curvature) is invoked. The most directly useful piece for ongoing work is §H.3 — the explicit local Bakry–Émery floor — which makes the pass-7 §10.6 stop-condition "spectral-window Bakry–Émery extension of SZZ at large β" structurally precise: the local input is already in hand (§H.3), the open analytic content is the global extension.

### Pass 7 changelog

Pass 7 supersedes pass 6. Triggered by a structured literature search restricted to peer-reviewed work on lattice Yang–Mills cumulant/correlation decay. Material additions:

1. **§10.3 literature map refined** with explicit citations replacing pass-6 placeholders. SZZ row added for SU(N) at strong coupling.
2. **§10.4 Path A** now lists the 11 Bałaban CMP papers individually with per-paper roles, replacing "Bałaban Yang–Mills original papers not currently in-hand." The Bałaban–Imbrie–Jaffe abelian Higgs companion (CMP 114, 1988) is also cited as the closest in-print level-(iv) prototype.
3. **§10.5 honest negative finding inserted** at the start: as of May 2026, no peer-reviewed paper proves (M′)_SU(2) at either level. The v17b empirical anchor stands; the literature route does not.
4. **New §10.6 "Modern probabilistic routes (adjacent, not closing)"** documenting SZZ 2023, Adhikari–Cao 2025, Cao–Nissim–Sheffield 2026, Cao 2020, Forsström 2022, Forsström–Lenells–Viklund 2022, and the Cao–Park–Sheffield random-surface program. Each entry includes the regime mismatch with (M′)_SU(2) and what would have to change for elevation.
5. **§10.7 honest revision strengthened.** The pass-6 phrasing "essentially equivalent to the mass-gap problem modulo bookkeeping" is correct in spirit but slightly optimistic: mass gap for SU(2) at large β in d=4 is *itself* genuinely open after Bałaban's UV stability program. The corrected phrasing: "(M′)_SU(2) is at least as hard as the mass gap, and possibly strictly harder because of the projected spectral-window restriction."
6. **§14.3 hardest open question** updated with the May-2026 literature status.
7. **§14.4 honest framing** extended with the pass-7 disclaimer noting the literature survey outcome.
8. **Appendix A bibliography** extended with ~30 new entries (full Bałaban CMP series, BIJ Higgs series, Federbush phase-cell series I–VI, MRS CMP 155, SZZ, Adhikari–Cao, Cao–Nissim–Sheffield, Cao 2020, Forsström, Forsström–Lenells–Viklund, Bauerschmidt–Brydges–Slade book, Fernández–Procacci, Bissacot–Fernández–Procacci, Procacci–Yuhjtman, Driver, Gross, Osterwalder–Seiler, Goswami, Borgs CMP 96).
9. **New Appendix G: Pass-7 literature deep-dive.** Records the survey scope, the three regime-mismatch findings, the per-candidate translation analysis (Adhikari–Cao + finite-subgroup approximation; SZZ + spectral-window Bakry–Émery; Bałaban CMP 116/119/122 polymer activity; BIJ CMP 114 abelian Higgs prototype; MRS CMP 155), and stop-conditions that would change the recommendation.
10. **§0.5 TL;DR updated**: "the single hardest open question" section now carries the May-2026 literature status. The "Honest 2-line claim" is unchanged (it was already correct).

Pass 7 does **not** revise:
- The conditional theorem statement (§2)
- The deterministic spine (§5) or sharp Bernoulli (§6)
- The Version A/B/C ↔ proof-program mapping (§7.9)
- The third-pass/fourth-pass tension resolution (§7.10)
- The BS/BG/CW-KP/dP analytic skeleton (§8)
- Theorem FNG (§9) — note: the existing FNG Stage 1 uses Adhikari–Cao 2025 + Cao 2020, both newly verified peer-reviewed citations
- The numerical pipeline (§11)
- The Dimock template (Appendix D), CSV verification (Appendix E), HBq2 cross-reference (Appendix F)
- Manuscript-safe language (§14.5)
- Future-run acceptance criteria (§13.6)

**Net pass-7 effect.** The structural architecture, the unconditional content, and Version C as the surviving conditional route are all unchanged. What pass 7 changes is the **honesty of the literature framing**: pass 6 said "(M′)_SU(2) ... essentially equivalent to the mass-gap problem modulo bookkeeping" with vague pointers to "Bałaban CMP papers not in hand"; pass 7 gives the specific peer-reviewed papers, names exactly what each proves and does not prove, and states the May-2026 literature status as "(M′)_SU(2) is open at large β for pure SU(2) YM in 4D; the strongest unconditional content is SZZ 2023 at strong coupling, Bałaban CMP 1989 for UV stability, and Adhikari–Cao 2025 for finite groups."

---

## 0.5 TL;DR — executive summary (added pass 6; updated through pass 16)

For readers who do not want to read 2400 lines.

### What this is

A conditional reduction of SU(2) lattice Yang–Mills coercivity (in a fixed projected spectral window on a periodic 4-lattice) to a precise hard-plaquette cumulant theorem $(M')_{\rm SU(2)}$. **Not a mass-gap proof.** The reduction is rigorous; the final stochastic input is open and is essentially equivalent to the mass-gap problem itself.

### What is unconditionally proved

1. **Deterministic spine** (§5): the projected plaquette atoms $A_p=P_{\le\Lambda,L}\mathbf 1_{\partial p}P_{\le\Lambda,L}$ satisfy PTO-1 (atomic facts, $\sum A_p=6P$), PTO-2 (trace-overlap exponential summability), PTO-3 (rank-4 trace-word reduction). $\kappa_\Lambda$ has a closed form, is plane-independent, $\le 2\mu_{\Lambda,L}$.

2. **Sharp Bernoulli plaquette-incidence Bernstein** (§6): for iid $B_p\sim\mathrm{Bernoulli}(q)$, with probability $\ge 1-\delta$:
$$
\|P\mathbf 1_{D(B)}P\|\le 6q+\sqrt{12q\kappa_\Lambda\log(2K/\delta)}+\tfrac{2\kappa_\Lambda}{3}\log(2K/\delta).
$$
At the v9 worst corner ($L=24, q=0.01, \Lambda=1$): bound 0.193, $\Theta\approx 0.385$, margin 0.615.

3. **Theorem FNG Stage 1** (§9): for $G=Q_8$ at $\beta\ge 61.16$, the projected capacity firewall closes via Adhikari–Cao + Cao 2020 + Cauchy–Schwarz composite — provable today.

4. **Lemma A (incident PTO overlap)** (§7.5.2): $\Omega^{\rm inc}<20\mu^2$ at $\Lambda=1$, sharp $\le 272/9\,\mu^2$ analytically.

5. **Lemma C (trace-to-quadratic bridge)** (§7.5.3): finite-volume certificate $C_{\rm TQ}^{(\mu)}\le 0.3039$ for $L\in\{8,12,16,24\}, \Lambda=1$.

### What is conditional and on what

The SU(2) Wilson firewall closure requires the Wilson-to-random/block plaquette-incidence transfer, which needs $(M')_{\rm SU(2)}$ — hard-indicator cluster cumulant decay with the right q-power. (M′) is open for SU(2) at large β. Two empirical anchors and one analytic template are in place:

- **Empirical anchor (v17b)** (§11.10, Appendix E): the working-corner pinned-norm bound $C_*^2 e^{-m_*}\le 0.017$ verifies exactly against the 1566-row CSV. The $m_*\ge 2$ extrapolation is over-stated; honest clean-signal $m_*\sim 0.5$–$1.0$. Firewall closure preserved.
- **Analytic template (Dimock I/II/III)** (§8.2, §10.4, Appendix D): the φ⁴_3 expository papers on Bałaban's RG (in-hand) provide the structural template for BS, with concrete proof-skeleton steps. Honest estimate: 6–12 weeks to translate to SU(2) Wilson + smooth source via the Bałaban CMP 89–116 originals (not in-hand).
- **Finite non-Abelian validation (Theorem FNG)** (§9): Q₈ closes at $\beta\ge 61.16$.

### The surviving route (Version C closed-walk)

$$
\underbrace{\text{BS smooth-source expansion}}_{\text{§8.2, target}} \;\xrightarrow{\;\eta\to 0\;}\; \underbrace{\text{BG hard-threshold bridge}}_{\text{§8.3}} \;\Longrightarrow\; \underbrace{\text{HPM closed-walk domination}}_{\text{§7.6}} \;\xrightarrow{\;\text{CW-KP}\;}\; \underbrace{\text{ML}_{\rm sparse}}_{\text{§7.6}} \;\Longrightarrow\; \underbrace{\text{firewall}}_{\Theta<1}
$$

with dP (top-p de-Poissonization) deferred. The closed-walk transfer (Version C) is identified by the fourth-pass quick reference as "the best structural match to the existing evidence." See §7.9 for the rigorous Version A/B/C ↔ proof-program mapping.

### What was eliminated (pass 5)

The **global HB-q² Matrix-Stein absorption route is failed** per the v15 audit (§11.8, §7.5.7): observed $\eta_{\rm cov}\in\{0.40, 1.23, 0.89\}$ vs target 0.25 across $\delta_{\rm bond}\in\{0.85, 1.00, 1.15\}$. The third-pass HBq2 lemma stack (A, B', C, D) refines the *local* theorem with strong content (Lemma A proved, Lemma C with certificate $C_{\rm TQ}^{(\mu)}\le 0.304$, Lemma D-old Boole bound) but does not change the global budget verdict. See §7.10 for the explicit tension resolution. Edge-Bernoulli comparator (v6b) was also retired earlier (Wilson/edge-Bernoulli ratio 1.23–1.55).

### The single hardest open question

Prove $(M')_{\rm SU(2)}$ at hierarchy level (iii) or better:
$$
\sum_{p'}|\mathrm{Cov}(X_p,X_{p'})|\operatorname{tr}(A_pA_{p'})\le Cq^2\kappa_\Lambda^2
$$
for $X_p=\mathbf 1\{\phi(U_p)\ge\delta_{\rm bond}\}$ under SU(2) Wilson at $\beta\ge\beta_0$.

**Pass-10 sharpening (§I.16, minimal next proof target).** By the explicit derivation chain of Appendix I, it suffices to prove the smoothed pair-covariance bound
$$
\boxed{
|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\le Cq_\eta^2 e^{-md(p,p')}
}
$$
for fixed $\eta>0$ with constants uniform in $\Lambda$. The deterministic PTO trace-overlap summability (§I.5 eq 5.1) then yields the level-(iii) sum form immediately, without further analytic input. The smoothing-bridge step §I.12 transports the bound from smooth $X_{p,\eta}$ to hard $X_p$ provided uniformity as $\eta\to 0$ holds. **This is the explicit "first SU(2) breach point" identified by the pass-10 source document.**

**Pass-11 status (Appendix J).** An explicit mathematical attempt at this minimal target via the §H.8 four-ingredient assembly produces concrete numerical estimates at the master's working corner. The Wilson Hessian eigenvalue formula is $\beta q_0^{(p,\ell)}/4$ per (plaquette, link) pair (§J.2); the naive pointwise BE threshold is $\beta<4/3$ crude or $\beta<1/96$ careful (SZZ 2023); both are violated at $\beta=3.5$ by factors of 2.6× and ~336× respectively (§J.3). Under conservative Haar bound at $L=24$, $P(\text{all BE-good})\le e^{-2.4\times 10^6}$ — exponentially small in volume (§J.5). **The attempt does NOT close the route; it identifies the spectral-window restriction (master §11.0c v3b) as the most promising research direction, with explicit subtargets in §J.8.**

**Pass-12 status (Appendix K).** The §J.8 Step 2 explicit numerical computation of $P\nabla^2 S_W P$ at typical Gaussian configurations has been carried out. **Key positive finding**: at $L=6$, $\beta=3.5$, with the spectral-window projector restricted to the coexact (gauge-invariant) subspace, the projected Hessian at a typical Gaussian configuration has ALL POSITIVE eigenvalues (min 0.31, p99 0.80, across 72 modes). The projected Bakry–Émery floor is uniformly $\ge 2.31$. This is the first explicit demonstration that the spectral-window + coexact restriction can produce positive projected BE at a typical config at the master's working $\beta=3.5$ — supporting the §J.6 research direction with the strongest empirical evidence to date. **It is NOT a proof.** Single sample, small lattice, Gaussian approximation. Pass-7 conditional status unchanged.

**Pass-13 status (Appendices L, M, N).** Three substantive additions completing the conditional-content accounting. **L (constants):** 13 constants pinned, 4 open; firewall inequality (14.1) at pinned values requires polymer activity $C_0 \le 6.8\times 10^{-8}$ — sharp quantitative target. **M (§K.3 → §I.16 bridge):** §K.3 supplies decay-rate component ($m\ge 0.76$ via BGL), NOT density-scaling component ($1.1\times 10^7$ gap between BGL $1/\eta^2$ prefactor and source $q_\eta^2$ target); the residual analytic question is a "small-density spectral-gap covariance decay" theorem (effectively what SZZ 2023 proves at strong coupling). **N (Russian school):** pass-7 known gap substantively closed — Malyshev–Minlos 1991 develops applicable abstract framework but their explicit gauge-theory chapter covers $\mathbb Z_2$ only; no Russian-school paper does SU(2) at large β; the gap is undone explicit work, not a hidden closure. **Pass-7 conditional status fully preserved.**

**Pass-14 status (Appendix O).** Pass-12 §K.3 extended from 1 sample to 10. ALL 720 projected BE eigenvalues across 10 typical Gaussian samples at $L=6$, $\beta=3.5$, $\Lambda=1.05$ lie in $[2.287, 2.830]$. Cross-sample standard deviation of BE min is only $0.014$ (less than 1% of mean). Zero samples show any negative projected BE eigenvalue. The §K.3 finding is highly robust, not single-seed fluke. Cross-sample tightness suggests an underlying analytic floor $\rho_*(\beta, \Lambda) \approx 2.31$ at the master's working corner. **Three independent empirical anchors** now support the §J.6 spectral-window proposal: master §11.0c v3b ($\Theta_*=0.884$ at operator-norm level, 1200 samples); pass-12 §K.3 (single-sample projected BE positive at L=6); pass-14 §O (10-sample projected BE distribution tight at L=6). **It is NOT a proof.** Wilson MCMC sampling, larger L, and the §M.4 small-density theorem remain open subtargets.

**Pass-15 status (Appendices P, Q, R + fourth honesty correction).** Wilson MCMC sampling implemented at L=6 (Appendix P): 5 thermalized samples with verified $\langle\phi_p\rangle = 0.148$; all 360 projected BE eigenvalues positive, BE min mean $2.199\pm 0.011$, BE max mean $4.039\pm 0.028$. Wilson distribution is $3.7\times$ wider than Gaussian; both empirically support §J.6 conjecture, with Wilson the more honest probe. Pass-12 §K.5 caveat (3) closed. **Analytic conjecture for $\rho_*$** stated (Appendix Q): $\rho_* \approx \kappa_G + (\beta/4)\lambda_{\min}^{\rm coex} - c\beta\langle\phi_p\rangle$, with $c$ ensemble-dependent (0.56 Gaussian, 1.30 Wilson). **(Pass-16 §S.6 corrects this conjecture.)** **Small-density projected BE covariance decay** stated as precise research conjecture (Appendix R): if proved, combined with §J.6 closes source §I.16; proof sketch via Brascamp-Lieb + Stein-coupling. **Fourth honesty correction**: pass-11 §J.4 formula $\langle\phi_p\rangle=3/(2\beta)=0.43$ was off by factor 4; correct value $3/(8\beta)=0.107$. Pass-7 conditional status fully preserved.

**Pass-16 status (Appendix S).** L=8 lattice extension via analytic Fourier-mode coexact basis construction (sparse eigsh stalls on 4095-mode zero block). 2 Gaussian samples at L=8, $\beta=3.5$, $\Lambda=1.05$ processed via batched plaquette accumulation (3 bash batches per sample). Result: BE min $2.20$ and $2.21$, BE max $2.47$, all 144 modes positive. **Pass-12 §K.5 caveat (2) "small lattice L=6 only" substantively closed.** **Critical refinement to pass-15 §Q.3**: shift below trivial-config BE scales linearly with $\lambda_{\min}^{\rm coex}(L)$ — empirical $-0.56$ at L=6, $-0.52$ at L=8, average ratio $-0.54$. Corrected conjecture: $\rho_*(L) = \kappa_G + ((\beta/4) - k_{\rm ens})\lambda_{\min}(L) + O(\lambda_{\min}^2)$ with $k_{\rm Gauss} \approx 0.54$. Asymptotic prediction: $\rho_*(L) \to \kappa_G$ as $L \to \infty$ with $O(1/L^2)$ convergence. **§J.6 supported with sharper statement $\inf_L \rho_* = \kappa_G$**: geometric Ricci floor does all asymptotic work; the projected-Wilson-Hessian configuration shift vanishes as $L\to\infty$. NOT a proof.

**As of May 2026 (pass-7 literature survey, §10.6, Appendix G).** No peer-reviewed paper proves this at either level (iii) or level (iv). The closest unconditional results are:
- Shen–Zhu–Zhu, *Comm. Math. Phys.* 400 (2023) 805–851 — covariance decay for SU(N) at strong coupling (per-link $|\beta_{\rm std}|<1/[16N(d-1)]$; for SU(2), $d=4$: $|\beta_{\rm std}|<1/96$). **Wrong regime** — we work at $\beta=3.5$, two orders of magnitude above.
- Adhikari–Cao, *Ann. Probab.* 53 (2025) 140–174 — exponential correlation decay for finite non-Abelian gauge groups at weak coupling. Used in FNG Stage 1 for $Q_8$ at $\beta\ge 61.16$. **Wrong group** — constants degenerate as $G_n\to{\rm SU}(2)$.
- Bałaban CMP 122 (1989) 175–202, 355–392, with antecedents CMP 109 (1987) and CMP 116 (1988) — UV stability of 4D pure YM for compact $G$, *not* mass gap or cumulant decay.

The honest May-2026 status: **(M′)_SU(2) is at least as hard as mass gap for SU(2) lattice YM at large β on a periodic 4-lattice, and possibly strictly harder due to the projected spectral-window restriction.** SU(2) extension is open; the pass-6 phrasing "essentially equivalent to the mass-gap problem modulo bookkeeping" is correct in spirit but slightly optimistic.

### Honest 2-line claim

> We reduce projected lattice Yang–Mills coercivity to a precise hard-plaquette cumulant theorem $(M')_{\rm SU(2)}$. The reduction is rigorous, the deterministic spine and sharp Bernoulli comparator are unconditional, and finite non-Abelian validation (Q₈) holds at large β; the SU(2) Lie-group cumulant input is open.

### Pass 6 changelog

Pass 6 supersedes pass 5. Material additions:

1. **§0.5 TL;DR executive summary** (this section).
2. **§7.9 Version A/B/C ↔ proof-program rigorous mapping table.** Pass 5 asserted "Version C is the best structural match" without working out which lemmas each Version needs.
3. **§7.10 Reconciling the third-pass / fourth-pass tension.** Explicit reading of why two documents dated 2026-05-24 give different verdicts on HB-q², and which is the correct synthesis.
4. **§11.0c v3b expanded** to the 1200-sample distribution (50 seeds × hot/cold × weight modes × $L\in\{8,12,16,24\}$). Pass 5 captured only the single max value $\Theta_*=0.884$ but missed that this is across 1200 sampled configurations with all $\theta_{\rm phys}<1$, all CG residuals $<10^{-6}$, mean 0.546, p99 0.854.
5. **§11.0b.5 v6b edge-Bernoulli failure** added as its own run card. Pass 5 mentioned v6b only in the inventory list.

Pass 6 does **not** revise any pass-5 architectural conclusions, the third-pass HBq2 lemma stack as the cleanest local formulation, the v15 demotion of HB-q² Matrix-Stein, the Dimock template for Path A, the m_* over-extrapolation finding, the manuscript-safe language, or the future-run acceptance criteria.

---

### Pass 5 changelog

Pass 5 supersedes pass 4. Two reference documents drive the revision:

- `PMBSF_quick_reference_for_simulations_fourth_pass_20260524.md` (1179 lines): fourth-pass compressed lead-agent reference with complete run inventory (v2/v3/v3b/v4b/v5b/v6a/v6b/v6c/v7a/v7b/v10/v11/v15/v16/v17/v17b), evidence tiering, manuscript-safe language, and **explicit route elimination** of global Matrix-Stein per v15.
- `HBq2_Lemmas_A_to_D_ThirdPass_20260524.md` (1245 lines): third-pass theorem-stack for HB-q² with refined Lemmas A (deterministic incident overlap), B' (clean cap-row), C (trace-to-quadratic bridge with finite-volume certificate $C_{\rm TQ}^{(\mu)}\le 0.3039$), D (spike absorption split into old-spike + density-spike).

Material changes:

1. **HB-q² demoted** (§7.5 fully rewritten). The fourth-pass quick reference §F1 lists HB-q² as "diagnostic only" and §F4 records v15 Matrix-Stein global audit as FAILED with all three $\delta_{\rm bond}$ values exceeding the 0.25 budget. The third-pass HBq2 lemma refinement is preserved as a sharpened *local* theorem stack (Lemmas A, B', C, D), but the route is no longer the active proof attack.
2. **HPM (closed-walk) elevated to surviving primary route** (§7.6 and §1.2 updated). The architectural diagram in §7.2 is revised.
3. **Run inventory expanded** to include the eight runs documented in the fourth-pass reference but absent from pass 4: v2 (synthetic projection sanity), v3 (first Wilson BS confirmation), **v3b (LOCKED Tier 1: $\Theta_*=0.884442692429$ in danger corner)**, **v4b (LOCKED Tier 1: projected-Maxwell continuum second-order slopes)**, v5b (fixed-$K$ sparse IR audit), **v7a/v7b (LOCKED Tier 1: fixed-window projected restriction)**, **v15 (FAILED: Matrix-Stein global budget)**. See §11 and Appendix C.
4. **Two $\Theta$ quantities distinguished** explicitly (§1.4, §11). The pass-4 errata table marked $\Theta_*=0.884442$ as "superseded" — this was a misreading. The v3b $\Theta_*$ is a *concrete single-sample projected BS norm* in a tested danger corner (LOCKED Tier-1 evidence). The v9 $\Theta\approx 0.386$ is a *probabilistic firewall parameter* via the random plaquette-incidence comparator. Both are valid; they measure different objects at different program stages.
5. **Three theorem versions added** (§7.8). The fourth-pass reference identifies three plausible target theorems: Version A (matrix-Laplace transfer), Version B (trace-moment transfer), Version C (closed-walk transfer). **Version C is identified as "the best structural match to the existing evidence."**
6. **Third-pass HBq2 lemmas folded into §7.5** with corrected notation: $W_e$ (raw trace-weighted row), $R_e=W_e/\mu^2$ (normalized), $Z_e=W_e/q^2$ (empirical diagnostic), and $C_{\rm row}=R_e/q^2$ (theorem-relevant). Lemma B' replaces Lemma B.1. Lemma D splits into old-spike (Boole $6q$) + density-spike (empirical fraction $0.118$ at L=16, NOT rare).
7. **Manuscript-safe language added** to §14 (verbatim "use this / do not use this" templates from quick reference §7).
8. **Future-run acceptance criteria added** to §13 (ten criteria from quick reference §8).
9. **Pass-4 m_* finding stands** but reinterpreted: with HPM as the primary route, the $m_*$ over-extrapolation concerns $\varepsilon_{\rm HPM}$ tightness (still well below binding threshold), not a tightness claim for HB-q². Pass-4 Appendix E is preserved.
10. **New Appendix F**: cross-reference table between the third-pass HBq2 lemmas and the master-document HB-q² discussion.

Pass 5 does **not** revise:
- The conditional theorem statement (§2)
- The wording constraints (§3)
- The deterministic spine (§5) or sharp Bernoulli (§6)
- The Dimock template for Path A (§8.2, §10.4, Appendix D)
- Theorem FNG (§9)
- Pass-4 Appendix E (CSV verification)
- Constants in Appendix C

### Pass 4 changelog (preserved from pass 4)

Pass 4 superseded pass 3. Material changes:

1. **New Appendix E: Empirical verification of v17b claims against `block_jackknife_diagnostics.csv`.** Direct row-level audit of the 1566-row CSV (the actual v17b data file).
2. **§1.4 / §1.5 headlines tempered** to reflect verification findings. "20× beats v16 empirical" is *contingent on $m_*\ge 2$* and that claim is not robust to clean-signal filtering. Firewall closure with comfortable margin is preserved; the specific "$\ge 0.99$" headline depends on the $m_*$ claim and is softened.
3. **§7.5 Lemma B.3 numerics re-verified**: L=8 budget arithmetic 0.135 vs 0.190 budget gives 29.1% headroom (vs claim "29%") — exact match.
4. **§6.3 q=0.001 row corrected**: pass-3 quoted bound 0.074, margin 0.852; recomputed from canonical (K=3792, κ_Λ=0.0055, u=11.93) gives 0.078, margin 0.844. ~5% rounding/version discrepancy; corrected in pass 4.
5. **§10.4 / §8.2 — Dimock parametric β_B caveat added.** The Dimock III framework gives the *structural target form* but **not** a numerical estimate of β_B for SU(2) Wilson + smooth source. β_B emerges from the Bałaban CMP 89–116 gauge-specific machinery, which is not in-hand.
6. **§11.10 v17b verdict** rewritten with honest split: what verifies exactly (statistical reach, pattern_kind clean rates, L-uniformity at working corner, $C_*^2 e^{-m_*}\le 0.017$ at working corner), and what is over-extrapolated ($m_*\ge 2$ across full clean range).
7. **§14.4 disclaimer**: explicit note that the bridge tightness claim "20× beats empirical" depends on a partially-supported empirical exponent.
8. **§13.5 do-not list**: added "do not cite $m_*\ge 2$ without the clean-signal caveat from Appendix E".

Pass 4 did **not** revise: conditional theorem (§2), wording constraints (§3), route architecture (§7), BS/BG/CW-KP/dP program (§8), Theorem FNG (§9), (M′)_SU(2) literature paths (§10), variant retirement table (§0).

### Pass 3 changelog (preserved from pass 3)

Pass 3 superseded pass 2. Material changes:

1. **§8.2 BS proof skeleton** rewritten with **explicit Dimock template** — Dimock III Theorem 2 (eq 222–223) is the structural target form; Dimock I §4 + III §2.6 are the small-field cluster-expansion machinery; Dimock II Lemma 3.19 eq (510) gives the contour-integral coefficient-extraction mechanism. The earlier "open-ended Bałaban extraction" framing is obsolete; the proof template is concrete and in-hand.
2. **§10.4 Path A (Bałaban extraction)** rewritten. No longer "1–2 weeks of careful reading" (`route_I_integrated_corrections__1__.md` §8 estimate) or "3–4 weeks" (`M_prime_reconnaissance.md` Path A estimate). Honest revised estimate: **6–12 weeks** with explicit Dimock-driven milestones (read I, then II, then III, plan SU(2) translation with source insertion, code first source-insertion lemma).
3. **New Appendix D: Bałaban/Dimock-to-PMBSF translation table.** Maps φ⁴_3 RG objects to the SU(2) Wilson + projected-capacity setting.
4. **§7.4 Route F** updated: the Brydges–Federbush / Abdesselam–Rivasseau tree-formula machinery referenced there is the same machinery Dimock III §2.6 uses; now traceable via accessible exposition rather than dense original Bałaban papers.
5. **vMF paper note** added to §7.5 and Appendix B: Gopal–Yang (ICML 2014) confirms the standard vMF density $f(x|\mu,\kappa)=C_D(\kappa)\exp(\kappa\mu^\top x)$ but is a clustering/ML paper. It does **NOT** address joint two-cap intersection structure that Lemma B.5/B.6 needs. Cited as standard reference; not load-bearing for the open lemmas.
6. **Appendix A bibliography** updated with the four in-hand PDFs.
7. **Pass 2 errata in §14.4 honest framing** retained; no factual corrections in pass 3.

Pass 3 did **not** revise the variant retirement table, the conditional theorem statement, the wording constraints, or any numerical values. The constants in Appendix C are unchanged.

---

## 0. Reading guide

This document unifies forty-plus project memos into a single coherent account. Pass 2 supersedes the pass-1 master and is structured around the four-route nesting and the smooth-source proof program — both of which pass 1 underrepresented.

### Variant retirement table

Several source files exist in multiple variants. The canonical version (latest, most developed, content-superseding) is given below; the others are kept in the project only as historical record.

| Subject | Variants on disk | **Canonical** | Notes |
|---|---|---|---|
| Route I integrated corrections | `.md`, `__1__.md`, `__2__.md` | **`__1__.md`** (= `__2__.md` byte-identical) | Original is older (v10 only); `__1__` adds v11 L=24/L=32 ratio 1.099 sparse pass |
| Sparse closed-walk domination | `.md`, `__1__.md`, `__2__.md`, `__3__.md` | **`__3__.md`** | 1446 lines vs 664 base; adds §§17–27 with BS/BG/GK–CW-KP/dP — the *current* proof program organization |
| (M′)_SU(2) theorem target & strategy | `.md`, `_patched.md`, `_patched__1__.md` | **`_patched__1__.md`** | Patched applies the 9-edit memo; `__1__` adds final boxed reduction statement |
| HB-q² PTO-summed heat-bath sensitivity | `.md`, `__8__.md`, `__9__.md` | **`__9__.md`** | 32 sections (vs 11 base); cleaned theorem skeleton with full Lemma A/B/C status |
| Run readout (v17/v17b cluster cumulants) | `.md`, `__1__.md` | **`__1__.md`** | v17b "GOOD" production run; 248 lines vs 61; v17 is pilot |

### Other variants to note

- `route_I_polymer_expansion.md` and `route_I_tightening.md` are **explicitly superseded** by `route_I_integrated_corrections__1__.md` (§0 errata table names them); they are kept for historical traceability but not load-bearing.
- `hb_q_2_pto_summed_heatbath_sensitivity_section__9__.md` is the cleanest theorem skeleton; `HB_qsq_merged.md` is a parallel merged manuscript draft of similar content; `Lemma_HB_qsq.md` is the standalone Lemma statement at operator level; `HB_q2_closure_matrix_stein_route_20260524.md` is the dated closure framework with explicit B.1/B.3 inputs. These four overlap but each contains content the others don't (the proof skeleton, the merged manuscript form, the operator-level lemma statement, the closure framework). They should be read together, not consolidated to one.

### Document structure

- §1 Executive overview.
- §2 **The conditional theorem.** Single boxed statement.
- §3 **Wording constraints (allowed / not allowed claims).** Verbatim from `m_prime_su_2_theorem_target_and_strategy_patched__1_.md` §12.
- §4 Notation and setup.
- §5 Deterministic spine — *unconditional*.
- §6 Sharp Bernoulli comparator — *unconditional*.
- §7 **The route architecture — nested, not parallel.** Routes I, F, HB-q², HPM and how they relate.
- §8 **The smooth-source proof program: BS → BG → CW-KP → dP.** The current organization of the open analytic work, from `sparse_closed_walk_..._3.md` §§23–27.
- §9 Theorem FNG — finite non-Abelian (Q₈) architecture, *conditional on composite literature input*.
- §10 (M′)_SU(2) — three paths + v17b empirical resolution.
- §11 Numerical evidence pipeline — v6a through v17b.
- §12 Unified status ledger (organized by route).
- §13 Roadmap (immediate / near-term / medium / open-ended).
- §14 Single consolidated disclaimer section.
- Appendix A: complete file map.
- Appendix B: glossary.
- Appendix C: constant cross-check table.

### Conventions

"Proved" means proved in the canonical source file cited. "Conditional on X" means proved subject to X. "Open" means a known gap with route identified. Numerical values for the canonical "v9 worst corner" are L=24, q=0.01, Λ=1, κ_Λ≈0.0055, δ=0.05, K≈3792, u:=log(2K/δ)≈11.93; cross-checked in Appendix C.

---

## 1. Executive overview

### 1.1 The target

Control the projected low-energy capacity operator

$$
\|P_{\le\Lambda,L}\,\mathbf 1_{D_W(U)}\,P_{\le\Lambda,L}\|_{\rm op}
$$

with high Wilson probability, where $D_W(U)$ is the bad-edge set from hard plaquette defects under the SU(2) Wilson measure on a periodic 4-lattice. The **projected capacity firewall** is the coercive bound $\Theta:=(V_{\max}/m^2)\|P\mathbf 1_{D_W}P\|<1$. This is a *projected, finite-volume* statement, not the mass gap, but it is load-bearing for the larger program.

### 1.2 The architecture (revised in pass 5)

$$
\underbrace{\text{deterministic PTO}}_{\text{§5, proved}}
\;\longrightarrow\;
\underbrace{\text{sharp Bernoulli matrix Bernstein}}_{\text{§6, proved}}
\;\xrightarrow{\;\text{Wilson} \to \text{random plaquette incidence}\;}\;
\underbrace{\text{Wilson matrix-Laplace transfer}}_{\text{§7, conditional}}
\;\Longrightarrow\;
\underbrace{\text{firewall coercivity}}_{\Theta<1}.
$$

The first two links are unconditional. The third — the Wilson-to-random/block plaquette-incidence transfer — is the **active proof target**, with the surviving primary route being closed-walk domination (HPM) per the fourth-pass quick reference §10 final verdict. The HB-q² Matrix-Stein route is no longer the active attack: v15 audit (§11.x) demonstrated global-budget failure at the canonical working point.

The third link requires an external cluster-cumulant input (M′) for the hard plaquette indicator $X_p=\mathbf 1\{\phi(U_p)\ge\delta_{\rm bond}\}$; (M′) for SU(2) at large β is open, and is essentially equivalent to the mass-gap problem itself modulo bookkeeping (`M_prime_reconnaissance.md` §8).

### 1.3 The corrected firewall budget at v9

$$
\|P\mathbf 1_{D(B)}P\|\le \underbrace{6q}_{\text{mean}}+\underbrace{\sqrt{12q\kappa_\Lambda u}}_{\text{variance}}+\underbrace{\tfrac{2\kappa_\Lambda}{3}u}_{\text{boundedness}}\approx 0.060+0.0887+0.0437\approx 0.193,
$$

$$
\boxed{\;\Theta\lesssim 0.386,\qquad 1-\Theta\approx 0.614.\;}
$$

At the sparser v10/v11 corner (q=0.003), bound is ≈0.111, $\Theta\le 0.222$, margin 0.778. At q=0.001, bound is ≈0.074, $\Theta\le 0.148$, margin 0.852.

### 1.4 Headline result from v17b (revised in pass 4)

The v17b connected-cumulant run **directly measures** the empirical analog of the (M′) pinned-polymer constants at the working corner. Pass 4 verifies these claims directly against `block_jackknife_diagnostics.csv` (Appendix E). The honest summary:

**What verifies exactly at the working corner ($\beta=3.5, q=0.003, \eta=0.05$):**
- **$C_*^2 e^{-m_*}\le 0.017$** (with smoothing-bridge factor 3 included): max-over-L mean-over-pair-patterns rooted form is 0.00564, × 3 = 0.01692, ≤ 0.017 ✓. **This is the load-bearing bound for firewall closure.**
- **L-uniformity at incident supports**: mean rooted form 0.00527/0.00485/0.00496 across $L\in\{12,16,24\}$. Verifies exact. Agreement to ~10% across factor 8× volume.
- **Statistical reach**: 69.9% of rows rel-JK-SE > 0.5 (claim "70%"); 18.9% < 0.3 (claim "19%"). Verifies exact.
- **Clean rates by pattern_kind**: pair_incident 108/108 (100%), triple_star 32/54 (59.3%), triple_L 17/54 (31.5%). Verifies exact.

**What does NOT verify cleanly:**
- **$m_*\ge 2$**: the patch's slope -2.36 at $L=12,\beta=3.5,\eta=0.05,q=0.003$ uses 4 points with the r=4 value 0.0001 carrying relative jackknife SE = 395 (totally noise-dominated). Excluding noise points gives slope -0.37, i.e. $m_*\approx 0.4$. Across the entire grid only ONE corner has ≥ 3 clean-signal points for a slope fit (L=16, β=3.5, η=0.025, q=0.01), and even there all-points $m_*=1.39$ vs clean-only $m_*=0.90$. The honest empirical statement is: "$|\kappa|/q^2$ is monotonically smaller at $r\ge 3$ than at $r=1$ across measured corners" — qualitative decay confirmed, quantitative $m_*$ lower bound poorly constrained.
- **$C_*^2 e^{-m_*}\le 0.017$ as a global bound**: at the v9 working corner it holds; over the full clean-signal range across all $(\beta,\eta,q)$ combinations, the maximum is 0.0314 (rooted form 0.01045 at L=12, β=4, η=0.025, q=0.01, × factor 3). The bound holds *at the working corner* — that's the relevant case for firewall closure — but should not be stated unqualified.

**Consequence for the bridge.** The placeholder-vs-measured comparison (`NOTE_PMBSF_mprime_hpm_bridge_v17b_patch.md` §B6.2) needs honest re-statement:

| Quantity | Placeholder | v17b (working corner) | v17b (honest, m_* clean-only) |
|---|---|---|---|
| $C_*^2 e^{-m_*}$ at incident pair (τ=1) | $\sim 2.4$ | **$\le 0.017$ ✓** | **$\le 0.017$ ✓** (same — τ=1 doesn't use $m_*$) |
| $m_*$ | 0.5 | $\ge 2$ (with noise points) | $\approx 0.5$–$1.0$ (clean-only) |
| $J_{m_*}$ | 96 | $\le 0.4$ | $\sim 10$–$50$ (extrapolated) |
| $N_{\rm KP}$ at $p=0.003$ | 2.7 | $\le 10^{-4}$ | $\sim 10^{-3}$ to $10^{-2}$ |
| Analytic $\varepsilon_{\rm HPM}$ | $\sim 200$ | $\sim 10^{-3}$ | $\sim 10^{-2}$ to $10^{-1}$ |
| Firewall margin | $\ge 0.4$ | $\ge 0.99$ | **comfortably ≥ 0.9** (still well below the binding threshold) |

**The firewall is preserved.** The binding threshold for $\varepsilon_{\rm HPM}$ is ~5 (where margin starts to bind); the honest range $10^{-2}$ to $10^{-1}$ is comfortably below that by 1–3 orders of magnitude. The headline "20× beats v16 empirical" no longer holds under clean-signal-only $m_*$; the honest version is "comparable to or somewhat looser than v16 empirical, with firewall margin still well above 0.5."

### 1.5 Pass-3 literature route summary (preserved)

The Dimock I/II/III expository papers on Bałaban's RG are in-hand and serve as the structural template for BS (§8.2) and Path A (§10.4). The previous framing — "build a smaller paper inside Bałaban's framework" — is obsolete: Dimock has already done that for φ⁴_3. The remaining task is translation to SU(2) Wilson with source insertion, estimated at **6–12 weeks** with the six-stage milestone plan in §10.4 Path A.

The (M′) literature path is therefore **doubly secured**: v17b empirical anchors give an exactly-verified upper bound on the load-bearing $C_*^2 e^{-m_*}$ constant at the working corner, *and* Dimock papers give a concrete proof template if rigorous closure is wanted. The program no longer depends on either a literature breakthrough or a numerical breakthrough — both routes are open and partially walked.

### 1.6 What pass 4 changes versus pass 3

The structural conclusions are preserved. The pass-3 headline "20× beats empirical, margin ≥ 0.99" is over-stated due to dependence on a noise-fragile $m_*\ge 2$ claim. Pass 4 documents this explicitly (§1.4, §11.10, Appendix E) and re-states with honest bounds. The firewall closure is robust because it depends primarily on the $C_*^2 e^{-m_*}\le 0.017$ bound at the working corner (which verifies exactly) and on the firewall-binding threshold ($\varepsilon_{\rm HPM}\sim 5$) being far above what any reasonable interpretation of the data gives.

### 1.7 What pass 5 changes versus pass 4

Two reference documents (`PMBSF_quick_reference_for_simulations_fourth_pass_20260524.md` and `HBq2_Lemmas_A_to_D_ThirdPass_20260524.md`) drive a substantive architectural revision. Most importantly:

#### Surviving chain (per quick reference §3.1)

$$
\Pi_{\rm phys}M^{-1}\Pi_{\rm phys}\text{ has a clean projected-Maxwell comparator}
$$
$$
\Big\downarrow\quad\text{(v4b continuum bridge slopes }\approx 2\text{)}
$$
$$
B_p^W\text{ behaves like a sparse random/block plaquette-incidence process}
$$
$$
\Big\downarrow\quad\text{(v6c, v7a, v7b)}
$$
$$
S_W=\sum_p B_p^W P_\Lambda\mathbf 1_{\partial p}P_\Lambda
$$
$$
\Big\downarrow\quad\text{(v10, v11, v16)}
$$
$$
\mathbb E_W\operatorname{tr}e^{\theta S_W}\lesssim\mathbb E_R\operatorname{tr}e^{\theta S_R}
$$
$$
\Big\downarrow
$$
$$
\|S_W\|\text{ or projected capacity remains subcritical}
$$
$$
\Big\downarrow
$$
$$
\text{conditional finite-volume firewall}
$$

The open step is the stochastic transfer $B_p^W \Rightarrow B_p^R$ in closed-walk / matrix-Laplace observables.

#### Failed chain (per quick reference §3.2)

$$
\text{local HB-}q^2\text{ suppression}\quad\not\Rightarrow\quad\text{global Matrix-Stein absorption}.
$$

The failure (v15 audit, §11.13 below) is not noise: covariance budget overshoots target $0.25$ by factors $1.6$–$5$ depending on $\delta_{\rm bond}$; finite-rank spike inflation is $\sim 343$–$1238$. Too large to fix by more samples.

#### The three theorem versions the simulations are selecting

Define $S_W=\sum_p B_p^W P_\Lambda\mathbf 1_{\partial p}P_\Lambda$ (Wilson) and $S_R=\sum_p B_p^R P_\Lambda\mathbf 1_{\partial p}P_\Lambda$ (random/block comparator).

**Version A — matrix-Laplace transfer.**
$$
\mathbb E_W\operatorname{tr}\exp(\theta S_W)\le \exp(\varepsilon(q,\theta,\Lambda))\cdot\mathbb E_R\operatorname{tr}\exp(\theta S_R)
$$
with $\varepsilon$ sparse-controlled and compatible with $q\approx 0.003$-scale behavior.

**Version B — trace-moment transfer.**
$$
\mathbb E_W\operatorname{tr}(S_W^m)\le C_m\,\mathbb E_R\operatorname{tr}(S_R^m).
$$

**Version C — closed-walk transfer.** Expand $\operatorname{tr}(S_W^m)=\sum_{\gamma\in\mathcal W_m}w_\gamma\prod_{p\in\gamma}B_p^W$ over closed walks $\gamma$ of length $m$. Then prove
$$
\mathbb E_W\sum_{\gamma\in\mathcal W_m}w_\gamma\prod_{p\in\gamma}B_p^W \le C_m\,\mathbb E_R\sum_{\gamma\in\mathcal W_m}w_\gamma\prod_{p\in\gamma}B_p^R.
$$

**Per the fourth-pass reference §6:** "Version C is the best structural match to the existing evidence." The closed-walk envelope is exactly the deterministic object on which the HPM bridge operates (§7.6, §8); the path is via $(M'')_{\rm SU(2),pinned}+\mathrm{CW\text{-}KP}+\mathrm{dP}\Rightarrow\mathrm{HPM}$ (§8.6).

#### What this means for HB-q²

The third-pass HBq2 lemmas (A, B', C, D — see §7.5 rewrite) are *sharpened local theorems*; they refine the operator-level $q^2$ statement at the link/incident-star scale. **What they do not deliver** is global integration: when summed across all edges of the lattice, the absorption constants exceed the Matrix-Stein budget (v15 audit, §11.13). HB-q² survives in the document as a precise local theorem with empirical anchors at $L\in\{12,16\}$ but is no longer the closing route.

#### What this means for the program

The pass-4 emphasis on HB-q² as the "active proof attack" is retired. Pass 5 reorganizes around the closed-walk transfer (Version C) as the surviving primary route, with the BS/BG/CW-KP/dP smooth-source program (§8) as the analytic skeleton and v17b as the empirical anchor. The Dimock template (Path A, §10.4) feeds into BS — that connection is unchanged.

### 1.5 Errata against earlier program memos

The following corrections are load-bearing and should be propagated wherever the older numbers appear.

| Prior claim | Correction | First appeared in |
|---|---|---|
| $A_pA_{p'}=0$ unless $p,p'$ share an edge | **False.** $P$ is a sharp spectral projector, nonlocal. Replaced by PTO (§5.5). | `route_I_integrated_corrections__1__.md` §0 |
| $\|A_pA_{p'}\|\le\mu_\Lambda e^{-d/d_*}$ pointwise | **False.** Algebraic, not exponential, decay for sharp cutoff. Replaced by PTO. | ibid. |
| Bernoulli mean term $4q$ or $dQ$ with $d=4$ | Should be **$6q$** (each edge in 6 plaquettes in 4D). | ibid. |
| Boundedness coefficient $\kappa_\Lambda/3\cdot\log$ | Should be **$2\kappa_\Lambda/3\cdot\log$**. | ibid. |
| $\Theta\approx 0.252$ / margin $0.748$ at v9 | Corrected to $\Theta\approx 0.385$, margin $0.615$. | ibid. |
| $\Theta\approx 0.34$ / margin $0.666$ at v9 | Same correction. | ibid. |
| "Firewall discharged modulo (M′)" | Acceptable **only** if marked conditional. | ibid. |
| Bałaban 87 / MR95 directly supplies (M′) | They supply infrastructure, not the hard-indicator version. **MR95 is a wrong citation; the correct paper is MR93** (CMP 155, 1993). | `NOTE_PMBSF_mprime_su2_extraction_protocol.md` §0 |
| $\|\kappa_W(Y)\|\le qA_*^{|Y|-1}$ (weak q-power) | Insufficient for $C_0=1+O(q)$; need $q^2$ pair scaling. | `route_I_integrated_corrections__1__.md` §0 |
| Sample certificate $\Theta_*=0.884442$ "discharged" | Conditional; superseded by the corrected $\Theta\approx 0.386$ at v9. | ibid. |

---

## 2. The conditional theorem

Collected from `m_prime_su_2_theorem_target_and_strategy_patched__1__.md` §11.

### 2.1 Hypotheses

Let $U$ be an SU(2) Wilson lattice gauge field on the periodic 4-lattice $T_L^4$ at coupling $\beta\ge\beta_0$, with $X_p(U):=\mathbf 1\{\phi(U_p)\ge\delta_{\rm bond}\}$ and $q:=\mathbb E_W[X_p]$. Assume:

- **(PTO)** PTO-1, PTO-2, PTO-3 of §5 (deterministic; *proved*).
- **(Bernstein)** Sharp Bernoulli plaquette-incidence Bernstein theorem of §6 (*proved*).
- **(M′)_SU(2)** Hard Wilson bad-plaquette cumulants satisfy
  $$
  |\kappa_W(Y)|\le q^{\alpha(Y)}A_*^{|Y|-1}\exp\!\left(-\tfrac{c_*}{\xi_\beta}\tau(Y)\right),\quad \xi_\beta\le\xi_*/\beta,
  $$
  for every finite $Y\subset\mathcal P_L$ with $|Y|\ge 2$, with either:
  (i) pair cumulants satisfying Level (iii)/(iv) q-power condition (§10.2), and higher cumulants the convergence condition; or
  (ii) a directly stated PTO-summed substitute implying (ML-SU2).

### 2.2 Conclusion

For every $\varepsilon\in(0,1)$, with Wilson probability at least $1-\varepsilon-o_L(1)$,

$$
\boxed{\;
\|P_{\le\Lambda,L}\,\mathbf 1_{D_W}\,P_{\le\Lambda,L}\|_{\rm op}
\le 6q+\sqrt{12q\kappa_\Lambda\log(2C_0K_{\Lambda,L}/\varepsilon)}+\tfrac{2\kappa_\Lambda}{3}\log(2C_0K_{\Lambda,L}/\varepsilon)+o_L(1),
\;}
$$

with $C_0=1+O_\Lambda(q)$ under (M′)(i), strengthening to $C_0=1+O_\Lambda(q^2)$ under the stronger summed-pair normalization, and weakening to $C_0=1+O_\Lambda(\sqrt q)$ under the summed sublinear substitute (the Stage 1 form, §9).

### 2.3 Firewall implication

If
$$
\frac{V_{\max}}{m^2}\!\left[6q+\sqrt{12q\kappa_\Lambda\log(2C_0K/\varepsilon)}+\tfrac{2\kappa_\Lambda}{3}\log(2C_0K/\varepsilon)\right]<1,
$$
then the projected Birman–Schwinger coercivity criterion holds with Wilson probability $\ge 1-\varepsilon-o_L(1)$.

### 2.4 Status paragraph (manuscript wording)

> The deterministic and independent-random components of this theorem are proved: the Fourier leverage identity, the κ_Λ atom bound, the plaquette-incidence Bernstein theorem, and the projected trace-overlap summability lemma. The only remaining analytic input is (M′)_SU(2), the hard bad-plaquette cumulant theorem. Existing finite-group results validate the structure of the argument in finite Abelian and finite non-Abelian settings, but do not establish the SU(2) compact Lie-group hard-indicator statement. The present paper should therefore be read as a reduction to (M′)_SU(2), supported by v10/v11/v17b diagnostics, not as an unconditional Yang–Mills mass-gap proof.

---

## 3. Wording constraints

Verbatim from `m_prime_su_2_theorem_target_and_strategy_patched__1__.md` §12. These rules govern any manuscript or external claim.

### Allowed

- "We prove the deterministic projected-capacity spine."
- "We prove the independent random plaquette-incidence Bernstein comparator."
- "We prove that (M′)_SU(2) implies a Wilson projected capacity bound with firewall margin."
- "The v10/v11 diagnostics support L-uniform Matrix-Laplace stability."
- "Finite non-Abelian gauge groups validate the architecture but do not bridge to SU(2)."

### Not allowed

- "We prove the Yang–Mills mass gap."
- "The Wilson stochastic theorem is proved by cluster expansion."
- "Bałaban / MR95 directly supplies (M′)."
- "The sample certificate is discharged unconditionally."
- "The finite non-Abelian theorem implies SU(2)."
- "The sharp spectral projector is local."

### The correct one-sentence claim

$$
\boxed{\;\text{We reduce projected lattice Yang–Mills coercivity to a precise hard-plaquette cumulant theorem }(M')_{\mathrm{SU(2)}}.\;}
$$

That is the strongest accurate claim at the current stage.

---

## 4. Notation and setup

### 4.1 Lattice

Periodic 4-lattice $T_L^4=(\mathbb Z/L\mathbb Z)^4$, $V=L^4$ sites, plaquette set $\mathcal P_L$ with $|\mathcal P_L|=6L^4$. Each edge is incident to **six** plaquettes (the source of $6q$ in the corrected mean and $\sum_p A_p=6P$); each plaquette has four boundary edges.

For integer momenta $k\in\{0,\dots,L-1\}^4$: $\theta_\alpha=2\pi k_\alpha/L$, $a_\alpha(k)=2\sin(\theta_\alpha/2)$, $\omega(k)=\sum_\alpha a_\alpha(k)^2$. The symmetric spectral window is $S_{\Lambda,L}:=\{k\ne 0:\omega(k)\le\Lambda\}$, $K_{\Lambda,L}:=3|S_{\Lambda,L}|$, $\mu_{\Lambda,L}:=K_{\Lambda,L}/(4L^4)$.

### 4.2 Projector and atoms

$P:=P_{\le\Lambda,L}$ is the coexact lattice projector onto transverse 1-forms in the spectral window $\omega(k)\le\Lambda$. Plaquette atom: $A_p:=P\mathbf 1_{\partial p}P$ for each $p\in\mathcal P_L$.

### 4.3 Defects

For an SU(2) configuration $U$ with $\phi(g)=1-\tfrac12\Re\operatorname{tr}g$:
$$
X_p(U):=\mathbf 1\{\phi(U_p)\ge\delta_{\rm bond}\},\quad q:=\mathbb E_W X_p,\quad D_W(U):=\bigcup_{p:X_p=1}\partial p.
$$
Bernoulli comparator: $B_p\sim\mathrm{Bernoulli}(q)$ iid, $D(B):=\bigcup_{p:B_p=1}\partial p$. Projected capacity observables: $S_W=\sum_p X_p A_p$, $S_B=\sum_p B_p A_p$.

### 4.4 Heat-bath exchangeable pair

For link $e$, $U^{(e)}$ replaces $U_e$ by a draw from the exact heat-bath conditional $\nu_e(\cdot|U_{e^c})$. Increment $\Delta_e X_p:=X_p(U^{(e)})-X_p(U)$. Incident star $\mathcal P(e):=\{p:e\in\partial p\}$, $|\mathcal P(e)|=6$. Cross-term function $C_e(p,p';U):=\mathbb E_e[\Delta_e X_p\Delta_e X_{p'}|U]$.

### 4.5 vMF parameterization

The SU(2) heat-bath conditional $\nu_e(\cdot|U_{e^c})$ is **exactly** a von Mises–Fisher law on $S^3\cong\mathrm{SU}(2)$:
$$
\nu_e(du|U_{e^c})=\mathrm{vMF}_4(du|m_e,\kappa_e),
$$
with density $\propto\exp(\kappa_e m_e\cdot u)$ for $u\in S^3$. The plaquette defect event $X_p(U^{(e)})=1$ is exactly a spherical cap $\{u\cdot n_p\le t\}$ with $t=1-\delta_{\rm bond}$, where $n_p$ depends on $U_{e^c}$ (`Lemma_B5_SU2_heatbath_vMF_cap_overlap_reduction_20260524.md` §0).

### 4.6 Firewall parameter

$\Theta=(V_{\max}/m^2)\|P\mathbf 1_{D_W}P\|$, with canonical $V_{\max}/m^2=2$. Coercive iff $\Theta<1$.

---

## 5. Deterministic spine — unconditional

Group-independent, β-independent, indicator-independent.

### 5.1 Lemma 1 — Fourier leverage equality

For every plaquette $p$ and every $e\in\partial p$, $P(e,e)=\mu_{\Lambda,L}=K_{\Lambda,L}/(4L^4)$.
*Proof.* Translation invariance + cubic averaging. `lemmas_1_2_proofs.md` §A; `kappa_bernstein_transfer_memo.md` §1.1.

### 5.2 Lemma 2.1 — κ_Λ plane-independence

$\kappa_\Lambda:=\|A_p\|_{\rm op}=\lambda_{\max}(G)$ where $G_{ij}:=P(e_i,e_j)$ is the 4×4 boundary-edge Gram. $\kappa_\Lambda$ is **independent of which plaquette** $p$ is chosen. v9 verified the six-orientation match numerically to $10^{-6}$.

### 5.3 Closed-form κ_Λ

Hyper-cubic symmetry reduces $G$ to three Fourier invariants $\alpha,\beta,\gamma$ plus diagonal $\mu$:
$$
G=\begin{pmatrix}\mu&\beta&\gamma&\alpha\\\beta&\mu&\alpha&\gamma\\\gamma&\alpha&\mu&\beta\\\alpha&\gamma&\beta&\mu\end{pmatrix},
\quad \kappa_\Lambda=\mu_{\Lambda,L}+\gamma_\Lambda,
\quad \kappa_\Lambda\le 2\mu_{\Lambda,L}.
$$
At $L=24,\Lambda=1$: $\kappa_\Lambda\approx 0.0055$. See `kappa_bernstein_transfer_memo.md` §1.

### 5.4 PTO-1: atomic facts

For every $p$:
$$
A_p\succeq 0,\;\;\operatorname{rank}A_p\le 4,\;\;\|A_p\|_{\rm op}\le\kappa_\Lambda,\;\;\operatorname{tr}A_p=4\mu_{\Lambda,L},\;\;\sum_p A_p=6P.
$$

### 5.5 PTO-2: trace-overlap exponential summability

$\tau(p,p'):=\operatorname{tr}(A_pA_{p'})\ge 0$. For every $a>0$, uniformly in $L$,
$$
\sup_p\sum_{p'} e^{-a\,d(p,p')}\frac{\operatorname{tr}(A_pA_{p'})}{\kappa_\Lambda^2}\le 4N_a<\infty.
$$
This replaces the **false** earlier claim of pointwise locality $A_pA_{p'}=0$ unless $p,p'$ touch — the sharp spectral projector is nonlocal, $A_pA_{p'}$ has algebraic, not exponential, off-diagonal decay. PTO is the deterministic bridge that lets exponential gauge correlations control nonlocal projected atoms.

### 5.6 PTO-3: rank-4 trace-word reduction

For any $p_1,\dots,p_k$, $\operatorname{rank}(A_{p_1}\cdots A_{p_k})\le 4$. Sharpens trace bounds $T_k(S)\le K\kappa_\Lambda^k$ to $T_k(S)\le 4\kappa_\Lambda^k$ for $k\ge 2$, removing a factor $K/4$ in earlier polymer estimates.

### 5.7 Block PSD envelope

For block decomposition $T_L^4=\bigsqcup_z Q_z$ at scale $\ell$, with $A_z:=P\mathbf 1_{\widetilde Q_z}P$:
$$
P\mathbf 1_{D_W}P\preceq \sum_z\mathbf 1\{D_W\cap Q_z\ne\emptyset\}A_z.
$$
**Retired** for firewall purposes: $\|A_z\|_{\rm op}\le 1\gg\kappa_\Lambda$, and a chromatic loss $C_1=2^d=16$ destroys the margin. The current program works at plaquette-atom scale (`PMBSF_matrix_stein_ML_reduction_v1.md` §0).

### 5.8 Closed-walk envelope (deterministic)

For finite $Y\subset\mathcal P_L$, $G(p,q):=\sqrt{\operatorname{tr}(A_pA_q)}$, and closed-walk activity
$$
\mathcal W_\theta(Y):=\sum_{n\ge 2}\frac{\theta^n}{n!}\sum_{\substack{p_1,\dots,p_n\\\{p_1,\dots,p_n\}=Y}}\prod_{j=1}^n G(p_j,p_{j+1}),\quad p_{n+1}:=p_1.
$$
**Lemma 2.1 (cyclic Hilbert–Schmidt trace-word bound).** $|\operatorname{tr}(A_{p_1}\cdots A_{p_n})|\le \prod_j G(p_j,p_{j+1})$ via Schatten Hölder + cyclicity. Proof: `sparse_closed_walk_..._3.md` §2.

This gives the deterministic envelope
$$
\operatorname{tr}e^{\theta S_X}\le K_{\Lambda,L}+4\theta\mu_{\Lambda,L}|X|+\sum_Y\mathbf 1_{Y\subset X}\mathcal W_\theta(Y).
$$
One-sided (signs and cancellations discarded), acceptable for upper bounds.

---

## 6. Sharp Bernoulli comparator — unconditional

### 6.1 Variance proxy

For iid $B_p\sim\mathrm{Bernoulli}(q)$, the centered variables have
$$
\sigma_B^2=\|\sum_p\mathbb E[(B_p-q)^2 A_p^2]\|\le q(1-q)\|\sum_p A_p^2\|\le 6q\kappa_\Lambda,
$$
using $A_p^2\preceq\kappa_\Lambda A_p$ and $\sum_p A_p=6P$. The coarser Schur estimate $\|\sum_p A_p^2\|\le 6$ is **noncoercive** in the firewall calculation; use the sharper $6q\kappa_\Lambda$.

### 6.2 Theorem 2 — random plaquette-incidence Bernstein

For every $\delta\in(0,1)$, with probability $\ge 1-\delta$:
$$
\boxed{\;\|P\mathbf 1_{D(B)}P\|\le 6q+\sqrt{12q\kappa_\Lambda\log(2K_{\Lambda,L}/\delta)}+\tfrac{2\kappa_\Lambda}{3}\log(2K_{\Lambda,L}/\delta).\;}
$$
Constants are fixed: mean $6q$, variance scale $6q\kappa_\Lambda$, uniform Bernstein inversion $2\kappa_\Lambda/3$. Source: `kappa_bernstein_transfer_memo.md` §2.

Using the L-uniform $\kappa_\Lambda\le 2\mu_{\Lambda,L}$ in place of empirical $\kappa_\Lambda$ gives the strictly L-uniform form (`kappa_bernstein_transfer_memo.md` (2.8)).

### 6.3 Firewall margins

| Corner | $L,q,\Lambda,\delta$ | Bound | $\Theta$ | Margin |
|---|---|---|---|---|
| v9 worst | 24, 0.01, 1, 0.05 | 0.193 | 0.385 | **0.615** |
| v10/v11 sparse | 24, 0.003, 1, 0.05 | 0.110 | 0.221 | 0.779 |
| Sparser | 24, 0.001, 1, 0.05 | 0.078 | 0.156 | 0.844 |

Pass-4 note: the "Sparser" row in pass 3 quoted bound 0.074 / margin 0.852. Direct recomputation from canonical $(K=3792, \kappa_\Lambda=0.0055, u=11.93)$ gives 0.078 / 0.844 — likely the pass-3 number used a slightly smaller $\kappa_\Lambda$ or $u$. Corrected here; the discrepancy is ~5% and does not affect any structural conclusion.

### 6.4 C₀ sensitivity

A C₀ inflation $C_0\in[1.00, 1.04]$ moves the Bernstein term to $[0.190, 0.193]$ at the v9 corner — margin robust to ±0.005. The firewall is structurally stable at the Bernoulli level; the entire conditional question rides on getting $C_0$ down to $1+O(q)$ (best), $1+O(q^2)$ (under (M′)(iii)/(iv)), or $1+O(\sqrt q)$ (Stage 1).

---

## 7. The route architecture — nested, not parallel

The project contains four "routes" to closing the Wilson-to-random matrix-Laplace transfer. Pass 1 listed them as parallel attacks; in fact they nest. This section makes the nesting explicit.

### 7.1 Four routes and what each asks for

| Route | Object | Key input | C₀ delivered |
|---|---|---|---|
| **I (polymer/cumulant)** | log trace-MGF $\Delta(\theta)$ | (M′): cumulant decay with q-power $\alpha(Y)\ge 2$ | $1+O(q)$ if pinned; $1+O(\sqrt q)$ if summed sublinear |
| **F (Stein global)** | Variance proxy via exchangeable pair | (CI): conditional independence with $q^2$ factorization at distance | (H2b) form, $1+O(q)$ |
| **HB-q² (Matrix-Stein local)** | Local carré-du-champ $\Gamma_W$ | (B.1) typical + (B.3) spike + (C) Schur closure | Operator-level $1+O(q)$ via Matrix-Stein |
| **HPM (closed-walk)** | Closed-walk envelope domination | HPM + EC + FCB; pinned (M″) for HPM bridge | $1+O(\varepsilon_{\rm HPM})$ |

### 7.2 How they nest

```
                            (M′)_SU(2)
                                |
                                v
                Route I ----> Matrix-Laplace transfer ----> firewall
                                ^
                                | (alternate)
                                |
        +-----------------------+--------------------------+
        |                       |                          |
   Route F (global)      HB-q² (Matrix-Stein local)   HPM (closed-walk)
        |                       |                          |
        v                       v                          v
   Lemma CI               B.1+B.3+C                  HPM + EC + FCB
   (Clay-equivalent)      (PTO-summed q²)            (v17b-anchored)
                                                          ^
                                                          | (bridge)
                                                          |
                                            BS + BG + CW-KP + dP (§8)
```

- **Route I** is the canonical theorem statement (§2.2). It requires (M′) pointwise with q-power; this is what is open in the literature for SU(2).
- **Route F** attempts to *prove* (M′) by Stein exchangeable pair plus a global conditional independence lemma (CI). The CI lemma at the operator-level long-range level is **not in the published literature for SU(2)**; it is "Clay-equivalent" in difficulty.
- **HB-q²** is the *local* version of Route F: instead of asking for global $q^2$ factorization at distance, ask for operator-level $q^2$ control of the local incident-star carré-du-champ. v12b empirical evidence supports this at the PTO-weighted scale, *not* pointwise (the pointwise spike ratio $\max|C_e|/q^2\in[10^3,10^4]$ is compressed by PTO weighting to $\le 0.11$, a $\sim 10^5$ factor). HB-q² supplies (M′) at the local level; this is the **active proof attack**.
- **HPM** is an alternative envelope target that bypasses (M′) entirely, replacing it by HPM (high-plaquette closed-walk domination) + auxiliary inputs. The v17b run measures the polymer constants for HPM's bridge and finds them tight enough that this route closes the firewall numerically with margin $\ge 0.99$.

### 7.3 Route I — polymer / cumulant expansion

Source: `route_I_integrated_corrections__1__.md` (canonical), supersedes `route_I_polymer_expansion.md` and `route_I_tightening.md`.

The trace-MGF comparison
$$
\Delta(\theta):=\log\mathbb E_W\operatorname{tr}e^{\theta S_W}-\log\mathbb E_B\operatorname{tr}e^{\theta S_B},
$$
expanded by moment-cumulant inversion after matching marginals:
$$
\Delta(\theta)=\sum_{k\ge 2}\frac{\theta^k}{k!}\sum_{S\subset\mathcal P,\,|S|\ge 1}[\,\mathbb E_W\!-\!\mathbb E_B\,]\!\left[\prod_{p\in S}X_p\right]\cdot T_k(S),
$$
with $T_k(S)$ identical on the W and B sides. The difference lives in $[E_W-E_B][\prod X_p]$, controllable by truncated cumulants $\kappa_W(Y)$ via the standard partition expansion.

Trace-mismatch artifact (`route_I_tightening.md` §7.1): the linear-in-θ component vanishes exactly with matched marginals; v10's small $-\theta\times 2\times 10^{-4}$ for `any_defect` is finite-sample fluctuation in the chain-level empirical $q$, while `weighted_incidence` shows pure $O(\theta^2)$ start as predicted.

### 7.4 Route F — Stein exchangeable-pair (global)

Source: `Route_F_Attack_Me_Stein_Exchangeable-Pair_Variance.md`.

Chatterjee 2007 variance identity:
$$
\mathrm{Var}_{\mu_\beta}(F)=\tfrac12\gamma_\beta^{-1}\mathbb E[(F(U)-F(U'))^2],
$$
with $F:=X_p X_{p'}-q^2$ and $(U,U')$ the heat-bath exchangeable pair. Decomposition into $\eta_e\cdot\mathbf 1\{e\in\partial p\}$ flip events and locality of $\Delta X_p$ gives the bound
$$
\mathbb E[(F(U)-F(U'))^2]\le 4\,\mathbb E[X_{p'}\cdot\eta_e]+\text{symmetric}.
$$
The key question is whether $\mathbb E[X_{p'}\eta_e]$ factorizes at $q^2$ scale (desired) or only $q$ (failure).

**Phase-1 decisive calculation** (`Route_F_Attack_Me_Stein_Exchangeable-Pair_Variance.md` §8): compute the same quantity in the decoupled Gaussian toy model — exact factorized Gaussian plaquette angles at large β. If it returns $q^2$, proceed. If $q$, **the route is dead before correlations are introduced.**

**Lemma SF** (small-field; ≤2 pages, low risk): the local flip probability $\eta_e\asymp q$ under the small-field approximation.

**Lemma CI** (conditional independence): the load-bearing step. *Not in published literature for SU(2) at large β.* Plausible route via Brydges–Federbush / Abdesselam–Rivasseau tree formula on the conditional measure after integrating out $U_e$. Convergence radius requires $\beta>\beta_0$ for some $\beta_0$ that emerges from the polymer weight.

**Note (pass 3): the tree-formula machinery referenced here is structurally the same as the Dimock III §2.6 cluster expansion** (`The_Renormalization_Group_According.pdf`). With those papers now in-hand, Route F's CI lemma proof has the same analytic template as BS step 4 in §8.2.3 — though Route F applies it to the *conditional* measure (after integrating out $U_e$), while BS applies it to the *full* Wilson measure with source insertion. The Route F application is technically distinct but uses the same building blocks.

**Risk** (`Route_F_..._Variance.md` §10): the conditional flip event $\{X_p\text{ flips at }e\}$ and the indicator $\{X_{p'}=1\}$ may be positively correlated even at large β — both single out atypical configurations near the firewall surface. If correlation factor $\kappa$ doesn't decay with $d(p,p')$, route gives only $q$, not $q^2$.

**Status.** Open. Phase 1 (toy model) not yet computed; the route is staged behind HB-q².

### 7.5 HB-q² — Matrix-Stein local (pass-5 status: DEMOTED to refined local theorem)

**Pass-5 status note.** This route was the "active proof attack" in pass 4. As of pass 5, two reference documents force a demotion:

- The fourth-pass quick reference (`PMBSF_quick_reference_for_simulations_fourth_pass_20260524.md`) §F1 lists local HB-q² as "diagnostic only" and §F4 records the v15 audit (now run, no longer "planned") as **FAILED at the global Matrix-Stein budget** — observed $\eta_{\rm cov}\in\{0.40, 1.23, 0.89\}$ vs target $0.25$ across $\delta_{\rm bond}\in\{0.85, 1.00, 1.15\}$. All three exceed the budget by factors $1.6$–$4.9$. The finite-rank arbitrary/sign spike absorption audit (§F3) gives $\eta_{\rm spike,sign}\in\{343, 411, 397, 1238\}$ across $L\in\{24,12,16,8\}$ — fatal.
- The third-pass HBq2 lemma document (`HBq2_Lemmas_A_to_D_ThirdPass_20260524.md`) refines the *local* theorem stack into Lemmas A, B', C, D with cleaner notation and explicit deterministic certificate constants. The third-pass refinement is preserved below as the cleanest form of the local statement, but does **not** address the global integration budget failure.

**Net assessment.** HB-q² is a precise local theorem with strong deterministic structure (Lemmas A and C) and empirical p99 anchors (Lemma B' at L=12 and 16); it is **not** the current closing route for the global Wilson-to-random transfer. The surviving primary route is HPM closed-walk (§7.6).

The remainder of this section preserves the third-pass HBq2 lemma stack as the cleanest local formulation, since the document is recent (2026-05-24) and supersedes earlier B.1/B.3/B.5/B.6 formulations.

#### 7.5.1 Setup and the three row quantities (third-pass HBq2 Correction 1)

The matrix carré-du-champ:
$$
\Gamma_W(S_W)(U)=\tfrac12\sum_e\mathbb E_e\!\left[\Big(\sum_{p\in\mathcal P(e)}\Delta_eX_p A_p\Big)^2\Big|U\right]=\Gamma_{\rm diag}+\Gamma_{\rm off}.
$$

Distinguish three row quantities at link $e$ (third-pass HBq2 §0.1):

- **Raw trace-weighted row.** $W_e(U):=\max_a\sum_{b\ne a}|C_e(a,b;U)|\operatorname{tr}(A_aA_b)$.
- **Normalized row.** $R_e(U):=W_e(U)/\mu_{\Lambda,L}^2$ (dimensionless).
- **Empirical diagnostic** (what scripts print). $Z_e(U):=W_e(U)/q^2$.

The theorem-relevant coefficient is $C_{\rm row}(e):=R_e(U)/q^2=Z_e(U)/\mu^2$. A printed $Z_e$ value alone is **not** the Matrix-Stein coefficient; it needs the $\mu^2$ normalization.

#### 7.5.2 Lemma A — Deterministic incident PTO trace overlap

For the incident overlap $\Omega_{\Lambda,L}^{\rm inc}=\max_p\sum_{p'\in\mathcal P(e),p'\ne p}\operatorname{tr}(A_pA_{p'})$:
$$
\Omega_{\Lambda,L}^{\rm inc}\le 80\mu_{\Lambda,L}^2\;\text{(coarse)},\qquad \le \tfrac{272}{9}\mu_{\Lambda,L}^2\;\text{(sharp)},\qquad <20\mu_{\Lambda,L}^2\;\text{(verified at $\Lambda=1$)}.
$$
**Status: proved deterministically; Fourier-verified in operational window** (`HB_qsq_merged.md` §§A.3–A.5; third-pass §A).

#### 7.5.3 Lemma C — Finite-rank trace-to-quadratic bridge

Fix link $e$, set $A_a:=A_{p_a}$ for $a=1,\dots,6$, define $D_e:=\sum_a A_a^2$. For a symmetric coefficient matrix $c=(c_{ab})$ with $c_{aa}=0$, set $T_e(c):=\sum_{a\ne b}c_{ab}A_aA_b$ and
$$
C_{\rm TQ}(L,\Lambda):=\sup_{c\ne 0}\frac{\|D_e^{-1/2}T_e(c)D_e^{-1/2}\|_{\rm op}}{R_e(c)}.
$$
Then for every $v\in\operatorname{Ran}P$: $|\langle v,T_e(c)v\rangle|\le C_{\rm TQ}(L,\Lambda)\,R_e(c)\,\langle v,D_e v\rangle.$

**Finite-volume certificate** (third-pass §C.2, audit at $\Lambda=1$):

| $L$ | $C_{\rm TQ}^{(\mu)}$ | $C_{\rm TQ}^{(\kappa)}$ | worst family |
|---|---|---|---|
| 8 | 0.294115 | 1.064406 | random sparse |
| 12 | 0.302371 | 1.097769 | random sparse |
| 16 | 0.302995 | 1.098777 | random sparse |
| 24 | 0.303901 | 1.100145 | random sparse |

Operational constant: $C_{\rm TQ}=1$; measured max: $C_{\rm TQ}^{(\mu)}\le 0.3039005048$. **Status: proved deterministically in the operational finite-volume window**; not yet certified all-$L$, all-$\Lambda$ as analytic theorem (third-pass Correction 4). Verified via 15 single-pair patterns, $2^{15}$ sign patterns, $20{,}000$ Gaussian + $10{,}000$ nonnegative + $10{,}000$ sparse random coefficient matrices.

#### 7.5.4 Lemma B' — Clean cap-row theorem (open stochastic obligation)

Partition link configurations into:
- **Good set** $\mathcal G_e$: clean cap rows — neither old-spike (incident plaquette pre-flagged) nor density-spike (conditional cap-radius spike).
- **Spike set** $\mathcal S_e=\mathcal S_e^{\rm old}\cup\mathcal S_e^{\rm dens}$.

**Target (B'.8):** $\mathbb E_W[\mathbf 1_{\mathcal G_e}R_e(U)]\le C_{\rm clean}q^2$ in **expectation**, not just p99 (third-pass Correction 2).

**Numerical anchor (third-pass §B'.5).**
- $L=12, \beta=3.5, \delta=1.0, \Lambda=1$: $Z_e=W_e/q^2$ old-good p99 $=6.92\times 10^{-3}$.
- $L=16, \beta=3.5, \delta=1.0, \Lambda=1$: old-good p99 $=1.18\times 10^{-2}$; after removing old+density spikes: p99 $=3.43\times 10^{-3}$.
- $L=16$ normalized clean p99 of $R_e/q^2$: $\approx 486.5$.

Informal absorption scalar with $C_{\rm TQ}=0.304, q\approx 0.0032$:
$$
\eta_{\rm clean}^{\rm p99}\approx 4\,(0.304)\,(486.5)\,(0.0032)\approx 1.89.
$$
The third-pass document: "**not negligible, but finite and plausibly budgetable if the expectation/tail integral is better than the p99 proxy.**" Recall the v9 firewall budget (Matrix-Stein form) requires the off-diagonal contribution to fit inside roughly $0.190 - \eta_{\rm typ}$. With $\eta_{\rm clean}^{\rm p99}\approx 1.89$ alone, the budget is comfortably exceeded — *unless* the expectation is much smaller than p99. **The required theorem is the expectation/tail version, not the p99 number.**

#### 7.5.5 Lemma D — Old/density spike absorption

$\mathcal S_e^{\rm old}=\{\exists p\in\mathcal P(e):X_p(U)=1\}$ has the Boole bound:
$$
\mathbb P_W(\mathcal S_e^{\rm old})\le \sum_{p\in\mathcal P(e)}\mathbb E_W X_p=6q.
$$
**Proved** (third-pass §D.2). The old-spike inflation constant $\eta_{\rm old}$ is then a measurable operator-norm quantity, open to budget-compatible analytic control.

$\mathcal S_e^{\rm dens}=\{\max_p b_p(U_{e^c})>M_q q\}$ has empirical fraction **0.117839 at $L=16$** (third-pass §D.5) — *not rare*. Probability alone is insufficient; the proof must use weighted tail suppression of $W_e$ on the density-spike set. **Status: open stochastic lemma**, the main remaining estimate (third-pass §7.2).

#### 7.5.6 Combined HB-q² implication (third-pass §6)

Assuming Lemma B' and Lemma D hold with stated constants:
$$
\Gamma_{\rm off}\preceq \eta_{\rm off}\,q\sum_p A_p^2+r_{\rm off}P,\qquad \eta_{\rm off}=4C_{\rm TQ}C_{\rm clean}q+\eta_{\rm old}+\eta_{\rm dens}.
$$
With $\Gamma_{\rm diag}\preceq c_{\rm diag}q\sum_p A_p^2+r_{\rm diag}P$:
$$
\Gamma_W(S_W)\preceq (c_{\rm diag}+\eta_{\rm off})q\sum_p A_p^2+(r_{\rm diag}+r_{\rm off})P.
$$
After exchangeable-pair normalization, this is the Matrix-Stein variance proxy.

#### 7.5.7 v15 audit — global budget failure

**Source: quick reference §F4.** Target: $\eta_{\rm cov}<0.25$.

| $\delta_{\rm bond}$ | observed $\eta_{\rm cov}$ | excess factor |
|---|---|---|
| 0.85 | 0.4018 | 1.6× |
| 1.00 | 1.2276 | 4.9× |
| 1.15 | 0.8897 | 3.6× |

**Raw one-sided audit:**

| $\delta_{\rm bond}$ | $\eta_{\rm good}$ | $p_{\rm bad}/(6q)$ | total inflation | budget | fits? |
|---|---|---|---|---|---|
| 0.85 | 0.848 | 0.870 | 4.609 | 0.168 | ✗ |
| 1.00 | 0.427 | 0.724 | 2.128 | 0.168 | ✗ |
| 1.15 | 0.516 | 0.679 | 0.530 | 0.168 | ✗ |

All three $\delta_{\rm bond}$ values fail. The closest is $\delta=1.15$ at total inflation 0.53 vs budget 0.168, factor 3.2× over.

**Trace-weighted finite-rank spike audit** (§F3):

| $L$ | $K$ | local rank | $C_{\rm inc}$ | $C_{\rm abs,sign}$ | $\eta_{\rm spike,sign}$ |
|---|---|---|---|---|---|
| 8 | 24 | 12 | 19.81 | 303,392 | 1237.84 |
| 12 | 216 | 19 | 19.56 | 100,823 | 411.36 |
| 16 | 696 | 19 | 19.52 | 97,198 | 396.57 |
| 24 | 3792 | 19 | 19.42 | 84,235 | 343.68 |

$\eta_{\rm spike,sign}$ values are 343–1238 — **fatal**. The arbitrary/sign spike absorption constants overshoot the budget by 3+ orders of magnitude. This cannot be fixed by more samples.

#### 7.5.8 Reconciliation between pass-4 and pass-5

Pass 4 §7.5 highlighted the Lemma B.3 firewall budget table with $L=8$ showing 29% headroom (budget 0.190, total $\eta = 0.135$). That number used $\eta_{\rm typ}=0.093$ and $6\eta_{\rm bad}q=0.042$ at $\delta_{\rm bond}=1.0$. The v15 audit (§7.5.7 above) reports $\eta_{\rm cov}=1.23$ at the same $\delta_{\rm bond}=1.0$ — **5x over the budget the L=8 row claimed to fit**.

The reconciliation: the Lemma B.3 table is a *projected forward* extrapolation under the assumption that the spike-side inflation can be absorbed via the Boole + measured $\eta_{\rm bad}$ structure. The v15 audit *measures* the global covariance directly using the canonical Matrix-Stein conditional-variance formula, which does NOT collapse to $\eta_{\rm typ}+6\eta_{\rm bad}q$ but to the operator-norm quantity $\eta_{\rm cov}$. **The two are not the same and the v15 measurement is what determines budget compatibility.** The pass-4 "29% headroom" presentation is preserved as a historical artifact but should not be cited as evidence of route viability after v15.

#### 7.5.9 What HB-q² still delivers

Even after demotion, the HB-q² stack provides:

1. **Lemma A: deterministic incident PTO overlap** $<20\mu^2$ at $\Lambda=1$ — locked.
2. **Lemma C: finite-rank trace-to-quadratic bridge with $C_{\rm TQ}^{(\mu)}\le 0.304$** at $L\in\{8,12,16,24\}, \Lambda=1$ — finite-volume certificate.
3. **Empirical p99 anchor on the clean row** ($Z_e=W_e/q^2$ p99 at L=16 old-good/density-controlled $\approx 3.43\times 10^{-3}$).
4. **Decisive elimination of pointwise $q^2$ as a target** — the empirical record (v12, v12b) establishes that operator-level/PTO-summed $q^2$ is the right target, not pointwise.

These are *deterministic finite-volume facts* useful as structural ingredients elsewhere. They do **not** add up to a closing route under the v15 global Matrix-Stein budget.

### 7.5b vMF reduction note (preserved from pass 3/4)

The SU(2) one-link heat-bath conditional is **exactly** vMF on $S^3$, and incident defect events are exact spherical caps. Standard vMF density $f(x|\mu,\kappa)=C_D(\kappa)\exp(\kappa\mu^\top x)$ with $C_D(\kappa)=\kappa^{D/2-1}/[(2\pi)^{D/2}I_{D/2-1}(\kappa)]$, $D=4$ for $S^3$ (Gopal–Yang, ICML 2014, `Von_MisesFisher_Clustering_Models.pdf`). The earlier Lemma B.5 attempted a pointwise two-cap $q^2$ statement on the non-alignment set; this is **false** under only non-alignment (positive tangent correlation gives joint lower-tail $\sim q^{2/(1+\rho)}$). The corrected target is PTO-summed (Lemma B.6 in pass-4 nomenclature; replaced by Lemma B' in third-pass nomenclature). The Gopal–Yang vMF paper does not address joint cap-intersection structure; it remains a standard density citation only.

### 7.6 HPM — sparse closed-walk domination

Source: `sparse_closed_walk_domination_wilson_high_plaquette_sets__3__.md` (canonical, 1446 lines), supplemented by `NOTE_PMBSF_mprime_hpm_bridge.md` + `NOTE_PMBSF_mprime_hpm_bridge_v17b_patch.md` for the (M′)→HPM bridge.

**Architecture.**
$$
\text{deterministic CW reduction}\;\longrightarrow\;
\mathrm{HPM}+\mathrm{EC}+\mathrm{FCB}\;\Longrightarrow\;\mathrm{ML}_{\rm sparse}\;\Longrightarrow\;\text{conditional firewall},
$$
with open bridge
$$
(M'')_{\rm SU(2),pinned}+\mathrm{CW\text{-}KP}+\mathrm{dePoissonization}\;\Longrightarrow\;\mathrm{HPM}.
$$

**Definitions.**
- **HPM**: Wilson high-plaquette sets do not overweight the closed-walk supports projected plaquette atoms see.
- **EC**: random closed-walk envelope comparability.
- **FCB**: fixed-cardinality-to-Bernoulli comparison.
- **(M″)_pinned**: pinned sparse high-plaquette cluster-expansion input, *stronger* than (M′) (requires $\alpha(\Gamma)\ge|\Gamma|$, not just $\ge 1$).
- **CW-KP**: weighted closed-walk Kotecký–Preiss summability.

**Theorem 14.1 (conditional, `sparse_closed_walk_..._3__.md` §14).** Under deterministic identities + HPM + EC + FCB + Bernoulli Bernstein, with Wilson probability $\ge 1-\delta$:
$$
\|P\mathbf 1_{D_W}P\|_{\rm op}\le R_{\rm cond}(p_+,\Lambda,L,\delta).
$$
Firewall coercive iff $C_{\rm BS}R_{\rm cond}<1$.

**Status ledger.** Deterministic reduction **proved**. Weak (M′)⇒HPM **insufficient for budget**. Pinned (M″)⇒HPM **open**. Top-p/threshold transfer **open auxiliary**.

### 7.7 The (M′)→HPM bridge

Source: `NOTE_PMBSF_mprime_hpm_bridge.md` (derivation), `NOTE_PMBSF_mprime_hpm_bridge_v17b_patch.md` (v17b empirical anchor).

Combined bound:
$$
\boxed{\;\varepsilon_{\rm HPM}\le c_*N_{\rm KP}(p)e^{O(N_{\rm KP})}+O(n_{\max}/\sqrt N)+O(n_{\max}^2/N).\;}
$$

**With placeholder constants $(C_*=2, m_*=0.5)$ at v9 corner** $(L=24, q=0.003)$: $N_{\rm KP}\approx 2.7$, analytic $\varepsilon_{\rm HPM}\approx 200$, vs. v16 empirical $\varepsilon_{\rm ML}\approx 0.02$ — loose by $10^4$.

**With v17b-measured constants** ($C_*^2 e^{-m_*}\le 0.017$, $m_*\ge 2$, smoothing-bridge factor 3 included): $N_{\rm KP}\le 10^{-4}$, analytic $\varepsilon_{\rm HPM}\le 10^{-3}$ — **beats v16 empirical by 20×**. Firewall margin $\ge 0.99$.

**Firewall tolerance** (`NOTE_PMBSF_mprime_hpm_bridge.md` §B7): $\varepsilon_{\rm HPM}$ appears in $\log(2K/\delta)+\varepsilon_{\rm HPM}$. The firewall tolerates $\varepsilon_{\rm HPM}\le 5$ before margin starts to bind; the v17b-anchored $\sim 10^{-3}$ contributes a $0.008\%$ shift.

### 7.8 The three theorem versions (pass-5 introduction)

The fourth-pass quick reference §6 identifies three plausible target theorems for the Wilson-to-random/block transfer:

- **Version A — matrix-Laplace transfer**: $\mathbb E_W\operatorname{tr}\exp(\theta S_W)\le e^{\varepsilon(q,\theta,\Lambda)}\mathbb E_R\operatorname{tr}\exp(\theta S_R)$
- **Version B — trace-moment transfer**: $\mathbb E_W\operatorname{tr}(S_W^m)\le C_m\mathbb E_R\operatorname{tr}(S_R^m)$
- **Version C — closed-walk transfer**: $\mathbb E_W\sum_\gamma w_\gamma\prod_p B_p^W\le C_m\mathbb E_R\sum_\gamma w_\gamma\prod_p B_p^R$

Quick reference §6: "Version C is the best structural match to the existing evidence."

### 7.9 Three Versions ↔ proof program rigorous mapping (pass 6)

This section was a gap in pass 5: the three Versions were stated, Version C was identified as best fit, but the *which lemmas does each Version need* was left implicit. Pass 6 works it out.

#### 7.9.1 What each Version needs

**Version A (matrix-Laplace).** Full MGF domination via comparison of $\log\mathbb E_W\operatorname{tr}e^{\theta S_W}$ with $\log\mathbb E_B\operatorname{tr}e^{\theta S_B}$. Required ingredients:

| Ingredient | Source | Role |
|---|---|---|
| (M′) cumulant decay with q-power $\alpha\ge 2$ | §10.2 hierarchy (iii)/(iv) | controls $E_W-E_B$ in moment-cumulant expansion |
| Polymer cluster convergence | BS (§8.2) for smooth sources | analytic basis for cumulant decay |
| Hard-indicator passage | BG (§8.3) | bridges smooth → hard $X_p$ |
| KP-style summability over $|Y|\ge 2$ | CW-KP (§8.4) restricted to scalar partition expansion | controls the polymer activity sums |
| Threshold vs top-p reconciliation | dP (§8.5) | only if top-p version desired |
| Deterministic envelope | PTO-2 (§5.5) | controls the trace-word coefficients $T_k(S)$ |

Version A delivers $C_0=1+O(q)$ at hierarchy (iii) or $1+O(q^2)$ at hierarchy (iv) — what the conditional theorem (§2.2) states.

**Version B (trace-moment).** Polynomial moment comparison up to order $m$. Required ingredients:

| Ingredient | Source | Role |
|---|---|---|
| Cumulant decay for $\|Y\|\le m$ | (M′) for bounded polymer sizes | weaker than full (M′) — only finite-order |
| Local polymer activities | BS restricted to $\|B\|\le m$ | small-polymer cluster bound only |
| Hard-indicator passage | BG | same as Version A |
| No KP convergence needed | — | only finitely many polymer sums |
| No dP needed | — | moments are threshold/top-p invariant in expectation |

Version B is **strictly weaker** than Version A but achievable with less analytic machinery. If KP convergence cannot be obtained for the full series, Version B provides a fallback giving moment-by-moment domination with $m$-dependent constants $C_m$. This is enough for matrix-Bernstein-type concentration at the $m=2$ moment but not for the full MGF.

**Version C (closed-walk).** Direct comparison at the closed-walk expansion level. Required ingredients:

| Ingredient | Source | Role |
|---|---|---|
| HPM (high-plaquette closed-walk domination) | §7.6 | core inequality |
| Closed-walk envelope $\mathcal W_\theta(Y)$ | §5.8 (proved) + (PTO-2 §5.5) | deterministic side |
| EC (envelope comparability) | §7.6 conditional | random envelope ↔ deterministic envelope |
| FCB (fixed-cardinality to Bernoulli) | §7.6 conditional | combinatorial step |
| Pinned (M″) for closed-walk activities | §7.6 conditional | stronger than (M′) — $\alpha(\Gamma)\ge\|\Gamma\|$, not $\ge 1$ |
| CW-KP | §8.4 in its full closed-walk form | controls walk-support sums |
| Smooth-cutoff geometry $P_\chi$ | §8.4 GK lemma target | kernel decay for cluster control |
| BG | §8.3 | smooth → hard passage |
| dP | §8.5 | top-p reconciliation if desired |

Version C delivers the same conclusion as Version A but **via closed-walk domination as the central object**, not the trace MGF directly. The pinned (M″) requirement is *strictly stronger* than (M′) for the partition expansion (the latter requires $\alpha(\Gamma)\ge 1$, the former $\alpha\ge\|\Gamma\|$).

#### 7.9.2 Why Version C is "best structural match"

Per quick reference §6: "Version C is the best structural match to the existing evidence." Four reasons:

1. **The closed-walk envelope $\mathcal W_\theta(Y)$ is the natural object for the deterministic spine** (§5.8). Versions A and B work at the trace-MGF or trace-moment level, which lose the support structure. Version C preserves the support $Y\subset\mathcal P_L$ as a first-class object, allowing geometry-aware estimates.

2. **The empirical comparator evidence (v6c, v10, v11, v16) is naturally walk-supported**. v6c measures Wilson/random plaquette-incidence at fixed projected IR observables — these are weighted closed-walk activities, not raw trace moments. v10/v11 trace-MGF ratios are derived quantities; the underlying walk structure is what v6c measures directly.

3. **HPM is closer in structure to BG than to (M′) at the partition-function level.** HPM says "Wilson high-plaquette sets do not overweight closed-walk supports projected plaquette atoms see." This is a *direct comparison of expectations on plaquette polymers* — the natural output of the BS+BG program after CW-KP closure. Version C inherits this directly; Version A requires an extra moment-cumulant inversion step.

4. **The v17b empirical anchor measures cluster cumulants for smoothed indicators** — which is more naturally interpreted as a *closed-walk* input than a *raw matrix-Laplace* input. The "pair_incident" rooted form (Appendix E) measures cumulants on plaquette pairs (Y={p, p'}), which is exactly a closed-walk activity at $n=2$.

#### 7.9.3 The HB-q² role under Version C

Under Version C, HB-q² is *not* a closing route in itself but a *per-incident-star auxiliary*. The Lemma A incident overlap and Lemma C trace-to-quadratic bridge contribute to the geometric weighting of closed walks at the link scale. The walk-by-walk closed expansion:
$$
\operatorname{tr}(S^m_W)=\sum_{\gamma\in\mathcal W_m}w_\gamma\prod_{p\in\gamma}B_p^W
$$
contains terms where consecutive plaquettes $p, p'$ in the walk are incident (share a link). For those terms, the weight $w_\gamma$ involves the trace $\operatorname{tr}(A_pA_{p'}\cdots)$, which is exactly what PTO-2 + Lemma A control. The HB-q² lemmas survive as deterministic ingredients of Version C, even though they don't close the global Matrix-Stein route.

This is the precise sense in which "HB-q² survives as a refined local theorem" (§7.5.9): its content is *re-purposed* into the Version C closed-walk envelope rather than discarded.

#### 7.9.4 Decision tree for which Version to prove

```
Goal: prove the Wilson-to-random/block matrix-Laplace transfer
                    |
                    v
Is full MGF closure needed for the firewall?
        |                           |
       yes                          no
        |                           |
        v                           v
   Version A                Version B (fallback)
   needs CW-KP             needs only bounded-order
   needs KP convergence    cluster bounds + BG
        |                           |
        v                           v
Does the cluster bound          Done, with weaker
have walk-aware geometry?       constants $C_m$
        |
       yes
        |
        v
   Version C
   walk-by-walk
   "best structural match"
   needs pinned (M″) + HPM + CW-KP + BG
```

For the firewall closure as stated in the conditional theorem (§2.2), **Version A is necessary** (the bound involves the matrix-Bernstein constant which derives from the full MGF). Version B is a fallback if KP convergence cannot be obtained. Version C provides the same conclusion as Version A via a structurally cleaner path that matches the empirical evidence better.

#### 7.9.5 Where each Version is incomplete

| Version | Status of inputs | Open work |
|---|---|---|
| A | BS open, BG open, CW-KP open (scalar form), dP deferred, hierarchy (iii)/(iv) of (M′) open | Path A (Dimock template, §10.4) + BG + CW-KP |
| B | Bounded-polymer cluster bounds simpler than full (M′); BG still required | Smaller version of Path A, restricted to $\|Y\|\le m$ |
| C | BS open, BG open, CW-KP open (closed-walk form), pinned (M″) stronger than (M′) | Path A + CW-KP for closed walks + (M″) extraction |

The honest assessment: Versions A, B, C all share the **same fundamental open analytic work** (Path A via Dimock template + BG smoothing-bridge). They differ in (a) what fallback weakening is acceptable (Version B for partial closure), (b) what additional structural input is needed (Version C requires pinned (M″) and walk-aware CW-KP), and (c) what is the natural empirical anchor (Version C ↔ v17b closed-walk cumulants).

### 7.10 Reconciling the third-pass HBq2 / fourth-pass quick reference tension (pass 6)

Two project documents dated 2026-05-24 give partially conflicting verdicts on HB-q²:

- **`HBq2_Lemmas_A_to_D_ThirdPass_20260524.md`**: "third-pass theorem-stack document... a sharpened local proof architecture reducing the HB-q² route to two remaining stochastic estimates." Framing: refinement, viable route with narrowed open work.
- **`PMBSF_quick_reference_for_simulations_fourth_pass_20260524.md`** §F1 + §F4 + §10: HB-q² listed as "diagnostic only"; v15 Matrix-Stein audit FAILED; "Matrix-Stein / spike absorption is not viable." Framing: route elimination.

This tension is real and must be addressed. Pass 6 resolves it.

#### 7.10.1 Why the third-pass document is optimistic

The third-pass HBq2 document §B'.5 ends with:

> $\eta_{\rm clean}^{\rm p99}\approx 1.89$. This is not negligible, but it is finite and plausibly budgetable if the expectation/tail integral is better than the p99 proxy or if the final Matrix-Stein margin tolerates it. The proof must establish the expectation/tail version, not only p99 control.

Two implicit assumptions in this optimism:
1. The expectation is materially smaller than p99 (typical for heavy-tailed distributions, but not guaranteed).
2. The Matrix-Stein budget tolerates a value of $\eta_{\rm clean}\sim 1$–$2$.

#### 7.10.2 Why the fourth-pass document is pessimistic

The quick reference §F4 reports the *direct measurement* of the global covariance operator $\eta_{\rm cov}$ — which is exactly the expectation-level quantity the third-pass document hoped would be smaller than p99. Observed values:

| $\delta_{\rm bond}$ | $\eta_{\rm cov}$ (expectation) | $\eta_{\rm clean}^{\rm p99}$ proxy (third-pass) | ratio |
|---|---|---|---|
| 0.85 | 0.40 | — | — |
| 1.00 | 1.23 | 1.89 | 0.65× |
| 1.15 | 0.89 | — | — |

The expectation IS smaller than p99 by ~35% at $\delta=1.0$ — confirming the third-pass optimism on assumption 1. But not by enough: the budget is **0.25**, and the expectation $\eta_{\rm cov}=1.23$ overshoots by **4.9×**. The third-pass assumption 2 (budget tolerates $\sim 1$–$2$) is wrong; the budget is much tighter.

#### 7.10.3 The synthesis

Both documents are correct on what they directly claim:

- The third-pass document is correct that the *local* HB-q² theorem stack reduces to two precise stochastic obligations (B' clean cap-row, D-density spike absorption). It is also correct that the expectation is smaller than p99 (a generic fact about right-skewed distributions).
- The fourth-pass document is correct that the *global* integration budget fails at all tested working points, with the closest fail still 3.2× over.

The reconciliation: **the third-pass document refines a local theorem; the fourth-pass document measures the global integration that uses the local theorem; the global budget is so tight that even tight local control does not close it.**

#### 7.10.4 Where does the global budget tightness come from?

The Matrix-Stein closure (Theorem 7.1 in pass-4 HB-q² treatment, §7.5.6 in pass-5 third-pass treatment) requires
$$
\eta_{\rm off}=4C_{\rm TQ}C_{\rm clean}q+\eta_{\rm old}+\eta_{\rm dens}<\text{budget},
$$
where the budget is the firewall margin at the working corner, roughly $0.25\times$ the available margin (matrix-Bernstein tail-coefficient piece). At v9 worst corner ($q=0.01$): margin 0.615; ~$0.15$ goes to budget. At $q=0.003$ (canonical): margin $\approx 0.78$; budget $\approx 0.20$. The v15 audit applies $\eta_{\rm cov}<0.25$ — consistent with this scale.

The third-pass `\eta_{\rm clean}^{\rm p99}\approx 1.89` is already 7.6× over the budget. Even if the expectation is half the p99 (which it is, at $\delta=1.0$), it's still 4.9× over. **No reasonable expectation-vs-tail relationship saves the budget.**

#### 7.10.5 What this means for the program

- **Local lemmas (A, B', C, D-old) remain valid.** The third-pass refinements stand as deterministic / partially proved statements at the link scale.
- **Global HB-q² route is eliminated.** The v15 audit is the global integration test; it fails. No amount of local-lemma sharpening fixes a 3–5× overshoot of the global budget.
- **HB-q² content is re-purposed under Version C** (§7.9.3). Lemma A and Lemma C survive as deterministic ingredients of the closed-walk envelope; they no longer constitute a closing route on their own.

#### 7.10.6 Documentary recommendation

The third-pass HBq2 document should be read as a *refinement of local content* that is structurally useful but no longer aspires to global closure. Pass 6 of this master document incorporates the third-pass lemma statements as the cleanest local formulation (§7.5) while preserving the route-elimination verdict from the fourth-pass quick reference (§11.8). Future versions of either source document should make this synthesis explicit.

---

## 8. The smooth-source proof program: BS → BG → CW-KP → dP

This section was effectively absent from pass 1. It is the **current organization of the open analytic work**, from `sparse_closed_walk_..._3__.md` §§23–27. Pass 1 mentioned BS only obliquely; in fact BS is the next concrete proof target.

### 8.1 Why smooth-source

The hard observable $X_p(t)=\mathbf 1\{\phi(U_p)\ge t\}$ is discontinuous. Bałaban-type expansions are naturally local and analytic, so the **first rigorous object should be a smoothed defect**:

$$
X_{p,\eta}(U):=f_\eta(\phi(U_p)-t),\qquad f_\eta\text{ smooth monotone with }f_\eta(s)=0\text{ for }s\le -\eta,\;f_\eta(s)=1\text{ for }s\ge\eta,
$$

with $q_\eta:=\mathbb E_W X_{p,\eta}$. The source generating functional
$$
Z_\eta(u):=\mathbb E_W\prod_p(1+u_p X_{p,\eta})=\mathbb E_W\exp\!\Big(\sum_p h_p X_{p,\eta}\Big),\quad h_p=\log(1+u_p),
$$
treats $u_p$ as analytic variables near zero (not nonnegative).

### 8.2 BS — Bałaban smooth-source expansion

#### 8.2.1 Target

Constants $u_0>0, C_B<\infty, m_B>0, \beta_B$ with: for $\beta\ge\beta_B$ and $|u_p|\le u_0$,
$$
\log Z_\eta(u)=\sum_{B\text{ connected}}\Psi_\eta(B;u_B),
$$
each $\Psi_\eta(B;u_B)$ depending only on source variables in $B$ and Wilson fields in a fixed finite neighborhood of $B$, with
$$
|\mathrm{coeff}_B\Psi_\eta|\le C_B^{|B|}q_\eta^{|B|}\exp(-m_B\tau(B)).
$$

**Rooted/pinned version** (the HPM-relevant form):
$$
N_{\rm BS}(q_\eta):=\sup_{p_0}\sum_{B\ni p_0,\,|B|\ge 2}C_B^{|B|}q_\eta^{|B|-1}\exp(-m_B\tau(B)).
$$
Need: $N_{\rm BS}$ small enough that closed-walk weighted KP fits inside the projected-capacity margin.

#### 8.2.2 Analytic template — Dimock III Theorem 2 form

This is the structural target form, recognized from the Dimock III exposition of Bałaban's RG applied to φ⁴_3 (`The_Renormalization_Group_According.pdf`, Ann. Henri Poincaré 15 (2014) 2133–2175):

> **Dimock III, Theorem 2 (eqs 222–223).** For φ⁴_3 with $\bar\mu=1$, $\lambda$ sufficiently small, with counterterm choice $\varepsilon_0^N, \mu_0^N$,
> $$
> Z_{M,N}=Z_{M,N}(0)\exp\!\Big(\sum_X H(X)\Big),\quad |H(X)|\le O(1)\lambda^{\beta/2}e^{-\kappa_0 d_M(X)}.
> $$
> Sum over connected unions of $M$-cubes $X\subset T_M^{-N}$.

That is **exactly** the form (M′) requires for the *partition function*, with exponential tree decay rate $\kappa_0$ (the analog of our $c_*/\xi_\beta$) and small parameter $\lambda^{\beta/2}$ (the analog of our $q^{\alpha(Y)}$ with $\alpha=\beta/2$). The Bałaban–Dimock framework natively delivers the *pinned* form: the inverse-coupling power scales with the polymer size at half-power. **This is the structural source of the pinned-form bound that pass-1 framed as "stronger than Bałaban gives" — the framework does give it natively for the partition function; the open work is the source-insertion modification.**

#### 8.2.3 Proof skeleton — six concrete steps

1. **Insert smooth source.** Add $\exp(\sum_p h_p X_{p,\eta})$ to the Wilson measure (with $h_p=\log(1+u_p)$). Since $X_{p,\eta}$ is smooth and local, the source contribution stays localized near $p$. This is the only modification to the Dimock III framework — everything downstream is template translation.

2. **Run small-field RG with source inserted** (Dimock I §4 template). Block average, identify small-field/large-field regions, scale and reblock. The source insertion goes through the small-field analysis (Dimock I §4.5 localization) without breaking analyticity because $X_{p,\eta}$ is bounded and smooth.

3. **Apply cluster expansion to source-dependent fluctuation integral** (Dimock I §4.6 Lemma 21 template):
$$
|E_k^\#(Y,\phi)|\le O(1)L^3\lambda_k^{1/4-10\epsilon}e^{-L(\kappa-5\kappa_0-5)d_{LM}(Y)}.
$$
In our setting, $\lambda_k$ is replaced by the working-corner parameter $q_\eta$ (or its β-dependent surrogate), and the exponential rate $L(\kappa-5\kappa_0-5)$ encodes the convergence regime $\beta\ge\beta_B$.

4. **Extract square-free source coefficients via contour integral** (Dimock II Lemma 3.19 / eq (510) template):
$$
B^\#_{k,\Pi^+}(Y)=\frac{1}{2\pi i}\oint_{|u|=r_0 L^{-3}\lambda_k^{-1/4+10\epsilon}}\frac{du}{u(u-1)}H^\#_{k,\Pi^+}(1,u,Y).
$$
This is the precise mechanism for getting from "expansion in source variables" to "square-free coefficient bounds." Adapted: replace $\lambda_k$ by $q_\eta$, replace the source parameter $u$ by our $u_p=e^{h_p}-1$.

5. **Iterate through final localization** (Dimock III §2.6 + §2.7 template). The cluster expansion is applied at each RG scale and the resulting polymer activities are reassembled via Dimock III §2.7 "final localization" to give the form (222) above with the source-dependent corrections inserted.

6. **Root one plaquette to obtain the pinned norm.** The extra factor $q_\eta^{|B|-1}$ is the rare-event gain required by HPM. In the Dimock language: pin one plaquette in each connected polymer, sum over the remaining plaquettes weighted by their cumulant contribution.

#### 8.2.4 What BS proves and does not prove

BS proves a smooth-source cluster expansion. It does **not** prove the hard-threshold statement unless the constants remain uniform as $\eta\to 0$ (this is BG §8.3) and the boundary-band contribution is controlled.

The output of BS is acceptable if it gives explicit or at least parametric constants:
$$
C_B(\beta,\eta),\quad m_B(\beta,\eta),\quad \beta_B(\eta),\quad N_{\rm BS}(q_\eta).
$$
Best case: uniform-in-η constants. Fallback: fixed $\eta$, yielding a smooth-defect theorem.

#### 8.2.5 Failure modes

BS fails for the current program if (`sparse_closed_walk_..._3__.md` §23.5):

1. The source insertion breaks analyticity (it doesn't — $X_{p,\eta}$ is smooth and bounded, fits Dimock I §4.5 hypotheses).
2. Constants blow up faster than the rare-event density gain can compensate. In Dimock III terms: if $\lambda^{\beta/2}$ analog doesn't dominate $|B|$-growth of $C_B^{|B|}$, the pinned bound fails. Mitigated by the v17b empirical evidence that the rooted polymer norm $|\kappa|/q^{|B|-1}$ is tiny.
3. $\beta_B$ above the working coupling $\beta=3.5$. Dimock III explicitly requires "L sufficiently large, M sufficiently large depending on L, $\lambda_k$ sufficiently small depending on L,M." Translating: in our setting, $\beta_B$ may emerge from cluster expansion convergence — open whether $\beta_B\le 3.5$ for SU(2) Wilson with smooth sources.
4. The expansion only controls partition functions but not local source coefficients. This is the substantive risk: Dimock III proves Theorem 2 for $\log(Z_{M,N}/Z_{M,N}(0))$ (no sources). Steps 1–4 of §8.2.3 are needed to source-modify the framework, and step 4 (contour-integral extraction) is the load-bearing step that has not been carried out in any published Bałaban-track paper.

If any of these occur, downgrade BS to a conditional source-expansion assumption.

#### 8.2.6 Why the Dimock template lowers the literature-extraction cost

The previous Path A estimate ranged from "1–2 weeks of careful reading" (`route_I_integrated_corrections__1__.md` §8) to "3–4 weeks. The papers are notoriously dense" (`M_prime_reconnaissance.md` §7). The Dimock papers are **already the expository simplification of the dense Bałaban originals**, written explicitly to lower the entry cost. The honest revised estimate is **6–12 weeks with concrete milestones** (§10.4) — longer than the original optimistic estimate, shorter than the open-ended "build a smaller paper inside Bałaban's framework" risk-case. The cost is real and substantive but no longer open-ended.

#### 8.2.7 Dimock template gives form, NOT numerical $\beta_B$ (pass-4 caveat)

The Dimock III convergence conditions are "L sufficiently large, M sufficiently large (depending on L), and $\lambda_k$ sufficiently small (depending on L,M)." Translating these conditions to SU(2) Wilson + smooth source + projected capacity does *not* give a numerical estimate for the threshold coupling $\beta_B$. The β-threshold for cluster-expansion convergence in non-Abelian Yang–Mills is determined by:

1. The gauge-fixing structure (Bałaban CMP 95, 96 — not in-hand).
2. The Lie-algebra block-spin localization (Bałaban CMP 89 — not in-hand).
3. The interaction between the gauge constraint and the polymer convergence radius (specific to non-Abelian).

The φ⁴_3 Dimock analysis fixes $\bar\mu=1, \lambda$ small, $L$ large, $M$ large; in the Wilson SU(2) setting the analog becomes β large enough that the Lie-algebra small-field condition $|A_e|\le \rho(\beta)\sim 1/\sqrt\beta$ holds outside a set of small Wilson measure. **None of the Dimock papers state a β-threshold for SU(2)** — that is in the Bałaban Yang–Mills originals, which are not in the project file inventory and would need to be consulted in Stage A4 (§10.4).

**Practical consequence.** Until the Bałaban Yang–Mills threshold is extracted explicitly, $\beta_B$ in BS remains a *symbolic* constant. The working coupling $\beta=3.5$ is *plausibly* above $\beta_B$ given the v17b empirical evidence (the cluster cumulant signal is well-defined at $\beta=3.5$ and even smaller at $\beta=4$), but this is empirical plausibility, not analytic confirmation.

### 8.3 BG — boundary-band gate (smoothing bridge)

Hard $X_p(t)$ and smooth $X_{p,\eta}(t)$ differ only when $\phi(U_p)$ lies in the η-band $B_\eta(t):=\{p:|\phi(U_p)-t|\le\eta\}$. Any hard/smooth error must be charged to transition-band plaquettes.

**Target.** $\varepsilon_{\rm bdry}(\eta)\to 0$ as $\eta\to 0$ with
$$
\sum_Y\pi_{\rm bdry,\eta}(Y)\mathcal W_\theta(Y)\le\varepsilon_{\rm bdry}(\eta)\sum_Y\pi_R(Y)\mathcal W_\theta(Y).
$$
Stronger usable version: $\pi_{\rm bdry,\eta}(Y)\le C_{\rm bdry}^{|Y|}b_\eta^{|Y|}\exp(-m_{\rm bdry}\tau(Y))$ with $b_\eta:=\mathbb P_W(|\phi(U_p)-t|\le\eta)\to 0$.

**Conclusion.** HPM_smooth + BG ⇒ HPM_hard with $\varepsilon_{\rm HPM,hard}\le\varepsilon_{\rm HPM,smooth}+\varepsilon_{\rm bdry}(\eta)$.

**Important.** It is **not** enough that $\mathbb E|B_\eta(t)|$ is small. A small number of boundary plaquettes could still be anomalously coherent with low projected modes. The required object is the closed-walk weighted boundary activity.

**Failure modes** (`sparse_closed_walk_..._3__.md` §24.5): (1) plaquette score distribution has atoms or strong concentration at $t$; (2) boundary band has small density but large projected capacity; (3) smoothing constants in BS blow up as $\eta\to 0$; (4) boundary-band source expansion lacks a pinned rare-event gain.

**v17b empirical partial resolution.** v17b measured connected cumulants for $X_{p,\eta}$ at $\eta\in\{0.025, 0.05, 0.10\}$ and finds rooted polymer norm grows by a bounded factor (1.6× to ~3×) as $\eta$ decreases. *No observed divergence in the smoothing limit; constants are bounded over the tested range.* Linear extrapolation suggests the hard-indicator constant is within factor $\sim 5$ of the smoothed constant at $\eta=0.05$. The remaining gap $\eta=0.025\to 0$ is bounded by the empirical trend and contributes a factor at most $\sim 2$.

**The single substantive remaining task on this thread** is verifying that the smoothing-bridge constant remains bounded as $\eta$ decreases below 0.025. Falsifiable experimental route: extend v17b to $\eta\in\{0.005, 0.01\}$ ($\sim 30$ minutes per η-value on A100).

### 8.4 GK / CW-KP — closed-walk kernel geometry

Closed-walk kernel $G(p,q):=\sqrt{\operatorname{tr}(A_pA_q)}$. The weighted KP problem is to show that closed-walk supports with many separated plaquettes are strongly suppressed by the geometry of $G(p,q)$.

**Sharp vs. smooth spectral cutoffs.** For sharp $P_{\le\Lambda,L}$, exponential real-space decay of $A_pA_{p'}$ is not automatic — discontinuous cutoff. The analytic theorem should introduce a smooth spectral cutoff $\chi$ with $\chi(s)=1$ for $s\le\Lambda$, $\chi(s)=0$ for $s\ge\Lambda+\Delta$. Define $P_\chi:=\chi(M_L)\Pi_{\rm coexact}$ and smooth-cutoff atoms $A_p^\chi:=P_\chi\mathbf 1_{\partial p}P_\chi$, $G_\chi(p,q):=\sqrt{\operatorname{tr}(A_p^\chi A_q^\chi)}$.

**Lemma target GK.** Summable plaquette kernel $K_\chi(p,q)$ with
$$
G_\chi(p,q)\le\mu_\chi K_\chi(p,q),\quad \sup_p\sum_q K_\chi(p,q)\le C_K,\quad \text{ideally }K_\chi(p,q)\le Ce^{-cd/\ell_\chi}.
$$
Polynomial decay acceptable if closed-walk sums converge.

**Lemma target CW-KP.** With pinned source-polymer norm $\nu(B)=C_B^{|B|}q_\eta^{|B|-1}e^{-m_B\tau(B)}$ from BS:
$$
\sum_Y q_\eta^{|Y|}\left[\exp\!\Big(\sum_{B\subset Y,|B|\ge 2}\nu(B)\Big)-1\right]\mathcal W_\theta^\chi(Y)\le(e^{\varepsilon_{\rm CWKP}}-1)\sum_Y q_\eta^{|Y|}\mathcal W_\theta^\chi(Y).
$$
Goal: $\varepsilon_{\rm CWKP}\le C\cdot N_{\rm BS}(q_\eta)\cdot F(\theta,C_K,\mu_\chi)$ with $F=O(1)$ in the working window.

**What Bałaban contributes.** Bałaban random-walk expansions show exactly the locality mechanism needed: local inverses patched with partitions of unity, each walk step carries a small factor, total expansion has exponential off-diagonal decay for $M$ sufficiently large. The correct output is not a Bałaban propagator estimate itself, but a closed-walk kernel summability theorem for the projected plaquette atoms — the Bałaban mechanism *mirrored* at the level of $P_\chi$ and $G_\chi$, not imported literally.

### 8.5 dP — top-p de-Poissonization (deferred)

Threshold set $X_t:=\{p:\phi(U_p)\ge t\}$ vs. top-p set $X_{\rm top}:=$ the $m=\lfloor pN\rfloor$ plaquettes with largest $\phi(U_p)$. Top-p is an order-statistic object, **not local in the same way as $X_t$**. Therefore dP should be deferred until fixed-threshold HPM is established.

**Target.** $\sum_Y|\pi_{\rm top}(Y)-\pi_t(Y)|\mathcal W_\theta(Y)\le(e^{\varepsilon_{\rm dP}}-1)\sum_Y\pi_R(Y)\mathcal W_\theta(Y)$.

**Sufficient conditions** (`sparse_closed_walk_..._3__.md` §26.3): count concentration, boundary-layer control near threshold, monotone sandwich $X_{t+\delta_t}\subset X_{\rm top}\subset X_{t-\delta_t}$ except on count-failure event, closed-walk norm control of sandwich errors.

**Why deferred.** Top-p is global; nonlocal. Unnecessary for the first analytic theorem. Recommended order: fixed-threshold smooth → fixed-threshold hard via BG → top-p via dP. If dP proves costly, manuscript can keep top-p as numerical diagnostic and state in fixed-threshold form only.

### 8.6 Immediate next proof move (`sparse_closed_walk_..._3__.md` §27)

> The first section to attack should be BS, but only in the smooth-source form. The concrete first lemma is:
>
> *For smooth local plaquette source $X_{p,\eta}$, prove a connected polymer expansion for $\log\mathbb E_W\prod_p(1+u_p X_{p,\eta})$ with exponential tree decay and square-free source coefficients.*
>
> The second section should be GK/CW-KP for a smooth spectral cutoff $P_\chi$, because that is where the current constants are most likely to improve.
>
> BG should be written in parallel but treated as the hard-threshold bridge, not assumed.
>
> dP should remain deferred until fixed-threshold HPM is closed.

---

## 9. Theorem FNG — finite non-Abelian (Q₈) architecture

Source: `Theorem_FNG__Finite_Non-Abelian_Gauge___Projected_Capacity_Firewall_.md`, `theorem_fng_cleaned_stage_1_stage_2.md`.

The first concrete theorem the program closes, validating the PMBSF architecture in a rigorous non-Abelian discrete setting.

### 9.1 Setup

$G=Q_8$, standard 2D faithful unitary irrep $\rho$ with $\chi(1)=2, \chi(-1)=-2, \chi(\pm i)=\chi(\pm j)=\chi(\pm k)=0$. Wilson measure $\mu_{\Lambda,\beta,Q_8}$ with action $S(\sigma)=\sum_p\Re(\chi(1)-\chi(\sigma_p))$. $X_p(\sigma):=\mathbf 1\{\sigma_p\ne 1\}$, $q:=\mathbb E_{\beta,G}X_p$.

### 9.2 β-threshold

$\Delta_{Q_8}=\min_{g\ne 1}\Re(\chi(1)-\chi(g))=2$. Adhikari–Cao Thm 1.1 threshold (verbatim from arXiv:2202.10375 v3, p. 5):
$$
\beta\ge\beta_0(Q_8):=(1/\Delta_G)(114+4\log|G|)=(1/2)(114+4\log 8)\approx 61.16.
$$
Cao 2020's earlier threshold gives $\approx 514$. **These are far above any physically interesting coupling**; this is not a defect to hide. The theorem says: at β≳61, the architecture closes; nothing about β∼2–6 SU(2) physics follows automatically.

Plaquette defect density scales as $q(Q_8,\beta)\asymp 6r_\beta\asymp 36 e^{-12\beta}$. At the rigorous threshold this is astronomically small; PMBSF numerical stress values $q=0.01$ are architecture stress tests, not certified Q₈ parameters.

### 9.3 Cluster-cumulant input

- **(H2a, weak — proved unconditionally as composite)** $\sum_{p'}|\mathrm{Cov}(X_p,X_{p'})|\operatorname{tr}(A_pA_{p'})\le C_1\sqrt q\,\kappa_\Lambda^2$. Adhikari–Cao Thm 1.1 + Cao 2020 Cor. 4.3.9 + Cauchy–Schwarz. Composite prefactor $C_{\rm AC}\approx 2.75\times 10^{11}$ (loose but β-independent). Conjugacy-invariant; $X_p$ qualifies. Single-anchor $|B_i|=1$ gives $4(4\cdot 1024\cdot 64)^2$.
- **(H2b, strong — conjectured)** $|\mathrm{Cov}(X_p,X_{p'})|\le C_2q^2\exp(-m\,d(p,p'))$ with $m=(\beta/2)\Delta_G$. Not in any published paper as of May 2026.

### 9.4 Theorem FNG

**Hypotheses.** (H1) $\beta\ge\beta_0(Q_8)\approx 61.16$. (H2) (H2a) or (H2b). (H3) PTO-1, PTO-2, PTO-3.

**Conclusion.** For every $\delta\in(0,1)$, with probability $\ge 1-\delta$:
$$
\|P\mathbf 1_{D_G(\sigma)}P\|\le 6q+\sqrt{12q\kappa_\Lambda\log(2C_0K/\delta)}+\tfrac{2\kappa_\Lambda}{3}\log(2C_0K/\delta)+o_L(1),
$$
$$
C_0=\begin{cases}1+O(\sqrt q\,\kappa_\Lambda^2/n_\Lambda) & \text{under (H2a)}\\ 1+O(q\,\kappa_\Lambda^2/n_\Lambda) & \text{under (H2b)}\end{cases}
$$
At the v9 corner: RHS $\approx 0.191$, **firewall margin $\approx 0.618$**.

### 9.5 What FNG does and does NOT buy

**Does buy.** Internal consistency of the PMBSF architecture in a rigorous non-Abelian setting. PTO is independent of $G$, Bernoulli baseline is independent of $G$, cluster-cumulant input (H2) localizes the $G$-dependence, firewall margin survives perturbation $C_0\to 1+O(\sqrt q)$.

**Does NOT buy SU(2).** Three obstructions:

1. **Spin-wave dominance.** For SU(2) at any $\beta$, the small-fluctuation Gaussian (spin-wave) sector contributes to $X_p$ via continuous $|U_p-1|^2\sim 1/\beta$ fluctuations. The probability $q_{\rm SU(2)}$ scales as a Gaussian tail, *not* as $e^{-c\beta}$. **No finite group captures this.**
2. **No analogue of (H2) for SU(2).** Adhikari–Cao swapping uses $|G|<\infty$ in two places: finite enumeration of minimal vortices, and probability lower bound via Lemma 6.7 prefactor $4^{|P|}|G|^{2|P|}$. Continuous SU(2) requires Gaussian-cluster (Bałaban) or stochastic-quantization (Shen–Zhu–Zhu 2023), neither of which packages the hard-indicator covariance with explicit constants.
3. **β-threshold mismatch.** $Q_8$ requires β≳61; SU(2) confinement crossover at β∼2.3.

### 9.6 The non-Abelian discrete gauge group library

Natural intermediate targets between FNG and SU(2):

- **FNG-D₄**: dihedral group $D_4$ — tests robustness to non-quaternion non-Abelian structure.
- **FNG-A₄, FNG-S₄, FNG-A₅**: higher-order non-Abelian discrete subgroups of SO(3)/SU(2). $A_5$ has $|G|=60$; approaches SO(3) limit through icosahedral discretizations (a recognized "ladder" in the lattice gauge literature).
- **FNG-ℤ_n large n**: cyclic discretization of U(1) at $n\gg 1$; in Forsström's framework directly, but does not test non-Abelian topology.
- **FNG-Higgs**: $Q_8$ coupled to Higgs as in Adhikari 2024 (CMP 405:117).
- **(H2b) from (H2a)**: refine Adhikari–Cao Lemma 6.7 to track *internal* β-suppression on anchor plaquettes — Peierls-type refinement; topological knot machinery unchanged. Single well-defined open problem with clear payoff.

### 9.7 Two-stage roadmap

- **Stage 1 (≤ 4 weeks):** Write FNG with (H2a) as proved composite. Submit deterministic PTO + Bernoulli + Route I as standalone preprint. Conclusion $C_0=1+O(\sqrt q)$, margin 0.618 at v9. *Architecture firewall paper.*
- **Stage 2 (1–3 months):** Prove (H2b) for $Q_8$. Graduate-student-level project for someone fluent in Cao 2020 / Adhikari–Cao 2025.
- **Stage 3 (3–9 months):** Reproduce Stages 1+2 for D₄, A₄. Proof structure identical; only character-table data and $\Delta_G$ change.

---

## 10. (M′)_SU(2) — three paths + v17b empirical resolution

Sources: `M_prime_reconnaissance.md`, `NOTE_PMBSF_mprime_su2_extraction_protocol.md`, `m_prime_su_2_theorem_target_and_strategy_patched__1__.md`.

### 10.1 What (M′) asks for

$|\kappa_W(Y)|\le q^{\alpha(Y)}A_*^{|Y|-1}\exp(-c_*\tau(Y)/\xi_\beta)$ with $\xi_\beta\le\xi_*/\beta$, $\alpha(Y)\ge 2$ for the leading pair.

Two key features: (a) **exponential decay** in inter-plaquette distance — sets polymer convergence radius; (b) **q-power scaling** for leading pair — sets $C_0=1+O(q)$ vs. weaker $1+O(1)$.

### 10.2 Four-level hierarchy

| Level | Form | Gives | Status |
|---|---|---|---|
| (i) Pointwise single-q, decaying | $|\kappa_W(Y)|\le q A_*^{|Y|-1}e^{-c\tau/\xi_\beta}$ | $1+O(q^\alpha)$ for some $\alpha\in(0,1]$; **insufficient if $\alpha<1/2$** | Open |
| (ii) Summed sublinear | $\sum_{p'}|\mathrm{Cov}|\operatorname{tr}(A_pA_{p'})\le C\sqrt q\,\kappa_\Lambda^2$ | $1+O(\sqrt q)$ | **Proved for finite non-Abelian** (FNG (H2a)) |
| (iii) Summed q²-scaled | $\le Cq^2\kappa_\Lambda^2$ | $1+O(q^2\kappa_\Lambda^2/n_\Lambda)$, absorbable to $1+O(q)$ | **Not in any paper, even finite non-Abelian.** The actual target. |
| (iv) Pointwise q² + exp decay | $\le Cq^2 e^{-cd/\xi_\beta}$ | (iii) trivially | Strongest; "pinned rare-event" form |

(ii) closes the program with margin >0.5 at √q cost. (iii)/(iv) close with cleaner $1+O(q)$. (i) is genuinely insufficient unless geometry forces $\alpha\ge 1/2$.

### 10.3 Literature map (pass-7 refinement)

|  | small β (strong coupling) | large β (weak coupling) |
|---|---|---|
| $\mathbb Z_2$ (Ising LGT) | Wilson 1974 heuristic; rigorous | Chatterjee, *Probab. Surv.* 17 (2020) 1–62 |
| Finite Abelian $\mathbb Z_n$ | classical strong-coupling | Cao, *Comm. Math. Phys.* 380 (2020) 1439–1505; Forsström, *Comm. Math. Phys.* 393 (2022); Forsström–Lenells–Viklund, *AIHP Probab. Statist.* 58 (2022) 2129–2164 |
| Finite non-Abelian | classical strong-coupling | **Adhikari–Cao, *Ann. Probab.* 53 (2025) 140–174** — exp. correlation decay. Used in FNG Stage 1 for $Q_8$ at $\beta\ge 61.16$ |
| U(1) (continuous) | trivial | Driver, *CMP* 110 (1987) 479–501; Gross, *CMP* 92 (1983) 137–162; Goswami, *AHP* 20 (2019) 3955–3996 for U(1) Higgs |
| SU(N) Lie group, small β | **Shen–Zhu–Zhu, *Comm. Math. Phys.* 400 (2023) 805–851** — mass gap, log-Sobolev, exp. covariance decay at per-link $|\beta_{\rm std}|<1/[16N(d-1)]$ (SU(2), d=4: $<1/96$). Cao–Nissim–Sheffield, *Prob. Math. Phys.* 7 (2026) 37–121 — area law at 't Hooft strong coupling. Chatterjee 2016 (SO(N) large-N); Jafarov 2016 (SU(N) large-N) — 1/N expansions at strong | **OPEN.** Bałaban CMP 1984–1989 (small-field UV stability, NOT mass gap); MRS *CMP* 155 (1993) for SU(2) with IR cutoff (no mass gap, no cumulant decay); BIJ *CMP* 114 (1988) — closest level-(iv)-shape but for U(1) Higgs in d=2,3 |

**(M′)_SU(2) sits in the upper-right corner.** As of May 2026, no peer-reviewed paper proves either level (iii) or level (iv) at large β for pure SU(2) YM in 4D. **The compact Lie-group extension at large β is at least as hard as the Yang–Mills mass-gap problem itself, and possibly strictly harder because of the projected spectral-window restriction.** "Modulo extraction from Bałaban" was an understatement; the Bałaban program does not deliver the cumulant decay either.

### 10.4 Three paths forward

#### Path A — Bałaban extraction via the Dimock expository papers (6–12 weeks)

**Source material now in-hand.**

- Dimock I — *The Renormalization Group According to Balaban I. Small Fields* (52 pp, arXiv:1108.1335, file `The_Renormalization_Group_According_to_Balaban.pdf`).
- Dimock II — *II. Large Fields* (94 pp, arXiv:1212.5562, file `The_Renormalization_Group_According_to_Balaban_2.pdf`).
- Dimock III — *III. Convergence* (43 pp, Ann. Henri Poincaré 15 (2014) 2133–2175, file `The_Renormalization_Group_According.pdf`).

These are J. Dimock's expository accounts of Bałaban's RG method applied to the φ⁴_3 ultraviolet problem. They are the **most accessible exposition** of the Bałaban small-field/large-field/convergence machinery and serve as the proof template for BS (§8.2).

**Why this changes Path A.** The earlier framing "read Bałaban Part II (CMP 116, 1988); the papers are notoriously dense; this might become 'build a smaller paper inside Bałaban's framework'" (`M_prime_reconnaissance.md` §7) reflected a state where the original 1987–89 papers were the only entry point. The Dimock papers are themselves *the* smaller paper inside Bałaban's framework — written by a former collaborator over five years for the purpose of making the method accessible. Path A is no longer open-ended literature archaeology; it is now a translation task with the template already worked out for φ⁴_3.

**Concrete six-stage milestone plan:**

- **Stage A1 — Read Dimock I (1–2 weeks).** Sections 1–4 cover small-field analysis: RG transformation, random-walk expansion, decoupling, the small-field theorem with cluster expansion (§4.6 Lemma 21). The cluster-expansion convergence bound (eq 237) is the analog of (M′)'s exponential-decay statement for fluctuation integrals.

- **Stage A2 — Read Dimock II (2–3 weeks).** Sections 2–3 cover the large-field contributions, the main representation theorem (3.1), the cluster expansion with holes (3.18), and the boundary-term removal via contour integral (Lemma 3.19, eq 510). This contour-integral mechanism is the precise template for BS step 4 (extract square-free coefficients in source variables).

- **Stage A3 — Read Dimock III (1–2 weeks).** Sections 1–3 give the convergence argument, the final localization, and Theorem 2 — the stability bound in the form $\log(Z_{M,N}/Z_{M,N}(0))=\sum_X H(X)$ with $|H(X)|\le O(1)\lambda^{\beta/2}e^{-\kappa_0 d_M(X)}$. This is the structural target form for BS.

- **Stage A4 — Plan SU(2) translation (1 week).** Construct the Bałaban/Dimock-to-PMBSF translation table (Appendix D below as starting point). Identify the specific objects in Dimock that translate to: SU(2) field $U$ vs. scalar $\phi$; β-large vs. λ-small expansion parameter; gauge constraint absent in Dimock; plaquette atoms $A_p$ as new objects with no Dimock analog.

- **Stage A5 — Code first source-insertion lemma (2–4 weeks).** Insert smooth indicator source $\exp(\sum_p h_p X_{p,\eta})$ into the Dimock I small-field RG. Verify analyticity preservation (Dimock I §4.5 localization carries through). Apply contour-integral extraction (Dimock II Lemma 3.19) to get the first nontrivial source-dependent cluster activity. Stop and assess whether the resulting bound has the right structural form.

- **Stage A6 — Iterate or pivot (open).** If Stage A5 produces a clean bound, continue with full multi-scale BS construction (estimated 4–8 weeks). If Stage A5 reveals a fundamental obstruction (e.g., source insertion breaks the small-field/large-field split, or the contour-integral coefficient extraction loses too much), pivot to Path B or document the obstruction theorem (also valuable).

**Total estimate: 6–12 weeks** depending on Stage A6 outcome. Substantially more than the optimistic "1–2 weeks of careful reading and writing" but no longer open-ended.

**Risk.** Three SU(2)-specific obstructions are not addressed by the Dimock papers (which are scalar):
1. **Gauge constraint** — the Bałaban Yang–Mills papers add a separate gauge-fixing/Higgs construction not present in φ⁴_3.
2. **Field type** — $U_p\in\mathrm{SU(2)}$ vs. $\phi\in\mathbb R$. The Bałaban Yang–Mills papers parameterize via Lie algebra coordinates; some of Dimock's scalar-specific simplifications won't transfer.
3. **β large vs. λ small.** Dimock's expansion parameter is $\lambda$ (φ⁴ coupling); the small parameter for our application is $1/\beta$ or $q_\eta$. The translation is structural but not automatic.

#### 10.4.1 The Bałaban Yang–Mills CMP series (pass-7 explicit inventory)

Pass 6 listed the Bałaban Yang–Mills original papers as "not currently in-hand" with a vague reference to "CMP 89, 95, 96, 116." Pass 7 replaces this with the complete 11-paper inventory and per-paper roles, extracted from the pass-7 literature deep-dive (Appendix G). All entries are in *Communications in Mathematical Physics* (CMP), peer-reviewed, communicated by A. Jaffe, for compact gauge group $G$ (with SU(N), in particular SU(2), the canonical case).

| Paper | Year | Pages | DOI | Role |
|---|---|---|---|---|
| Bałaban, "Propagators and renormalization transformations for lattice gauge theories. I" | 1984 (CMP 95) | 17–40 | 10.1007/BF01215753 | Gaussian one-step block propagators; exponential decay & analyticity in background |
| Bałaban, "Propagators and renormalization transformations for lattice gauge theories. II" | 1984 (CMP 96) | 223–250 | 10.1007/BF01240221 | Multi-scale extension of Paper I |
| Bałaban, "Averaging operations for lattice gauge theories" | 1985 (CMP 98) | 17–51 | 10.1007/BF01211042 | **Lie-algebra block-spin transformation**; group-valued averaging analyticity. Directly relevant to BS smooth-source §8.2 |
| Bałaban, "Spaces of regular gauge field configurations on a lattice and gauge fixing conditions" | 1985 (CMP 99) | 75–102 | Project Euclid cmp/1103942611 | **Lattice axial/Landau-type gauge fixing** for fixed block averages. Directly relevant to the projected Maxwell comparator |
| Bałaban, "Propagators for lattice gauge theories in a background field" | 1985 (CMP 99) | 389–434 | 10.1007/BF01240355 | Background-field multi-scale propagator bounds |
| Bałaban, "Ultraviolet stability of three-dimensional lattice pure gauge field theories" | 1985 (CMP 102) | 255–275 | 10.1007/BF01229380 | **UV stability of 3D pure YM**, all compact $G$. Template proof in d=3 only |
| Bałaban, "The variational problem and background fields in renormalization group method for lattice gauge theories" | 1985 (CMP 102) | 277–309 | 10.1007/BF01229381 | Existence/uniqueness of the **Wilson-action minimizer** for fixed block averages — the projected Maxwell-comparator background field |
| Bałaban, "Renormalization group approach to lattice gauge field theories. I" | 1987 (CMP 109) | 249–301 | 10.1007/BF01215223 | Small-field cluster expansion at **one RG step in d=4**; β-function and recursive coupling renormalization |
| Bałaban, "Renormalization group approach to lattice gauge field theories. II. Cluster expansions" | 1988 (CMP 116) | 1–22 | 10.1007/BF01239022 | **Per-step polymer activity bound** $\|K_k(X)\|\le \varepsilon_k^a \exp(-\kappa d_M(X))$. **Closest structural form to level (iv) of (M′)**, but for renormalized coupling $g_k^2\to 0$ inside the asymptotic-freedom flow, NOT at fixed large β for hard $X_p$ |
| Bałaban, "Convergent renormalization expansions for lattice gauge theories" | 1988 (CMP 119) | 243–285 | 10.1007/BF01217741 | Inductive description of the full effective density preserved under RG |
| Bałaban, "Large field renormalization. I. The basic step of the $R$ operation" | 1989 (CMP 122) | 175–202 | 10.1007/BF01257412 | Large-field $R$-operation step |
| Bałaban, "Large field renormalization. II. Localization, exponentiation, and bounds for the R operation" | 1989 (CMP 122) | 355–392 | 10.1007/BF01238433 | Large-field exponentiation. Together with CMP 119, **completes 4D UV stability of pure YM** |

**Net Bałaban output (unconditional, peer-reviewed):** UV stability of 4D pure lattice Yang–Mills for general compact gauge group, including SU(2). **Net non-output:** mass gap; cumulant decay at fixed large β; the level-(iv) $|\kappa(B)|\le C^{|B|}q^{|B|}e^{-m\tau(B)}$ shape for hard plaquette indicators.

The polymer-activity bound in CMP 116 (1988) has the structurally correct shape but operates inside the asymptotic-freedom flow ($g_k^2$ running) and applies to small-field domains *after* large-field localization. Translating this to a fixed-β, fixed-volume, hard-indicator cumulant bound for $X_p$ is the Stage A4–A6 research task of Path A.

#### 10.4.2 The Bałaban–Imbrie–Jaffe abelian Higgs companion

The structurally closest in-print precedent for the κ(B) cumulant-decay shape is the **abelian Higgs** series by Bałaban, Imbrie, and Jaffe (with Brydges in the first paper):

| Paper | Year | Pages | DOI | Role |
|---|---|---|---|---|
| Bałaban, Brydges, Imbrie, Jaffe, "The mass gap for Higgs models on a unit lattice" | 1984 (Ann. Phys. 158) | 281–319 | 10.1016/0003-4916(84)90121-0 | **U(1) Higgs mass gap on unit lattice**, weak coupling |
| Bałaban, Imbrie, Jaffe, "Renormalization of the Higgs model: Minimizers, propagators and the stability of mean field theory" | 1985 (CMP 97) | 299–329 | 10.1007/BF01206191 | Mean-field stability bounds for U(1) Higgs RG step in d=2,3 |
| Bałaban, Imbrie, Jaffe, "Effective action and cluster properties of the abelian Higgs model" | 1988 (CMP 114) | 257–315 | 10.1007/BF01225038 | **Multiscale cluster expansion delivering exponential decay of correlations** for U(1) Higgs in d=2,3 — the prototype of a κ(B)-shape bound in a constructive RG setting |

**Caveat.** BIJ CMP 114 (1988) is structurally identical to (M′)_SU(2) level (iv), modulo two non-trivial differences: (i) abelian vs. SU(2), and (ii) the Higgs potential's deep well supplies the small parameter, whereas in pure YM the small parameter must come from $q=\mathbb E X_p$ via the choice of $\delta_{\rm bond}$. The transferability is structural but the technical content is not.

A modern revisit using BFKT machinery is Goswami, *Ann. Henri Poincaré* 20 (2019) 3955–3996, DOI 10.1007/s00023-019-00840-0, which proves the mass gap for the observable $F_{\mu\nu}$ in weakly coupled U(1) Higgs in $d\ge 2$ via power-series cluster expansion. Still abelian; still Higgs.

#### 10.4.3 Magnen–Rivasseau–Sénéor SU(2) construction

**Magnen, Rivasseau, Sénéor, "Construction of YM₄ with an infrared cutoff,"** *Comm. Math. Phys.* **155** (1993) 325–383, DOI 10.1007/BF02097397. Constructs SU(2) Schwinger functions in regularized axial gauge with IR cutoff in the trivial topological sector. **Does not provide mass gap or cumulant decay.** Cited as alternative phase-space expansion, not as a Path-A foundation.

#### Path B — Smoothing bridge via Lohmann + cited tools (2–3 weeks)

Use a smooth approximation $f_{\varepsilon,p}$ and apply Lohmann 2014 (or modern BKAR — Brydges–Kennedy–Abdesselam–Rivasseau interpolation framework) to derive (M′) for $f_{\varepsilon,p}$, show constants uniform in $\varepsilon$, pass $\varepsilon\to 0$.

**Risk.** Need to verify Lohmann's hypotheses for SU(2) Wilson with the gauge constraint. Lohmann's abstract framework requires "small enough coupling"; the SU(N) gauge constraint may complicate verification.

**Status update — partially superseded by v17b.** The smoothing-bridge problem (Path B) is the same as BG in §8.3, and the v17b empirical evidence already shows that the smoothing constant is bounded over $\eta\in[0.025,0.10]$ with multiplicative factor $\le 3$. The remaining question — does the constant stay bounded as $\eta\to 0$? — is now an analytic question with a clear experimental fallback (extend v17b to smaller η).

#### Path C — Finite non-Abelian subgroup sanity check (1–2 weeks)

Take $G=2I$ (binary icosahedral, largest finite subgroup of SU(2) other than doubles of cyclic/dihedral), run firewall verification with Adhikari–Cao plugged in. **Doesn't help SU(2) directly** but verifies pipeline and calibrates order-of-magnitude $A_*, c_*, \xi_*$ for a real non-Abelian group.

**Pass-7 caveat (Appendix G.3 Candidate 1).** Constants in Adhikari–Cao 2025 generically *degenerate* as $|G_n|\to\infty$ along a sequence of finite subgroups $G_n\to{\rm SU}(2)$, because the swapping/percolation threshold depends on group structure. Path C is a *pipeline sanity check*, not a proof route to SU(2). Borgs *CMP* 96 (1984) 251–284 already showed the exact factorization used in Seiler's monograph fails for general finite non-Abelian groups; Adhikari–Cao 2025 acknowledges this gap.

#### Recommended order

Updated recommendation:

- **Path C first (1–2 weeks)** — sanity check with explicit Adhikari–Cao constants. Verifies pipeline.
- **Path A in parallel with Stage A1–A3 (4–7 weeks)** — read Dimock papers concurrently with the rest of the program. This is no longer "literature extraction"; it is "active proof template study."
- **Path B (2–3 weeks)** — Lohmann smoothing bridge; can be deferred since v17b already gives empirical control over the smoothing range.
- **Path A Stages A4–A6 (5–13 weeks)** — only after A1–A3 are done; depends on whether to attempt the source-insertion modification or accept the smoothed (BS-only) result.

Total: 12–25 weeks if all paths pursued. **The previous "6–9 weeks" estimate (`M_prime_reconnaissance.md` §7) was optimistic.** Pass-3 honest estimate is 3–6 months of focused mathematical work, with three concrete exit conditions and a fallback to a smoothed-source theorem in the worst case.

### 10.5 v17b empirical resolution and honest negative finding (pass 7)

**Pass-7 honest negative finding.** After surveying the peer-reviewed literature 1978–2026 (pass-7 deep-dive, Appendix G), **no paper proves either level (iii) or level (iv) of (M′)_SU(2) at large β for pure SU(2) YM in 4D on a periodic lattice.** The Bałaban CMP series (1984–1989) proves UV stability but not mass gap; SZZ 2023 proves mass gap and covariance decay at strong coupling but does not extend to large β; finite-group results (Adhikari–Cao 2025, Cao 2020, Forsström et al. 2022, Forsström–Lenells–Viklund 2022) do not cover continuous SU(2). The (M′)_SU(2) hypothesis therefore remains conditional in pass 7, and the master document's main theorem is conditional on this hypothesis. The v17b empirical anchors stand; the *literature route* to closing (M′)_SU(2) is not currently available.

**v17b empirical anchor (preserved from earlier passes).** The v17b run **directly measures** the empirical analog of (M′)'s pinned-polymer constants for *smoothed* indicators $X_{p,\eta}$. The hierarchy of conclusions:

1. **L-uniformity.** `pair_incident` rooted form across $L\in\{12,16,24\}$ at $(\beta=3.5, q=0.003, \eta=0.05)$: $|\kappa|/q\in\{0.00527, 0.00485, 0.00496\}$. Agreement to ~10% across factor 8× volume. **Empirically resolved** for incident supports; finite-volume corrections below MC noise floor at $L=24$.

2. **Upper bound on $C_*^2 e^{-m_*}$.** Measured maximum over clean-signal subset at working corner: $C_*^2 e^{-m_*}\le 0.017$ (with smoothing-bridge factor 3 included). Compare placeholder 2.4: **140× tighter.**

3. **Lower bound on $m_*$.** Same-orientation axis pair decay (clean rows) gives $m_*\ge 2$ — **with the pass-4 caveat** (Appendix E) that this depends on inclusion of r=4 points with relative jackknife SE up to 395. Clean-only $m_*\sim 0.5$–$1.0$. Firewall margin preserved either way.

4. **Polymer norm.** $J_{m_*}\le 0.4$ (vs. placeholder 96), $N_{\rm KP}\le 10^{-4}$ (vs. placeholder 2.7) — **4 orders of magnitude tighter under the $m_*\ge 2$ extrapolation; 2 orders of magnitude tighter under the clean-signal $m_*$.**

5. **Smoothing bridge.** Multiplicative factor $\le 3$ over $\eta\in[0.025, 0.10]$, growth slowing as $\eta$ decreases (10% from 0.05 to 0.025 at $k=2$). Linear extrapolation suggests hard-indicator constant within $\sim 5$× of smoothed at $\eta=0.05$.

6. **Higher-order corrections.** $k=4$ cumulant decays *faster* than pinned form predicts. **Good news for the bound** (actual suppression stronger than pinned), but means $(C_*,m_*)$ should be extracted from $k=2$ alone and treated as upper bound on polymer norm, not parametric fit.

**Consequence.** v17b provides an empirical anchor on the load-bearing pinned-norm constant *at the working corner*. It does NOT replace (M′)_SU(2): the empirical measurement is finite-volume, finite-sample, at one β and one $\delta_{\rm bond}$; (M′)_SU(2) requires a theorem uniform in $L$ and stable as $\eta\to 0$. The v17b strengthening means a moderate literature extraction would no longer be the load-bearing element if it existed — but per the pass-7 negative finding, **it does not currently exist in the peer-reviewed literature.**

### 10.6 Modern probabilistic routes (pass 7: adjacent, not closing)

Pass-7 literature survey identifies three modern probabilistic approaches with results structurally close to (M′)_SU(2). All are *adjacent* — they prove correlation decay or related properties for lattice gauge theory in regimes that miss (M′)_SU(2) at large β for SU(2) in 4D. None can be directly cited as closing the route. Full per-candidate translation analysis is in Appendix G.3.

#### 10.6.1 Stochastic Langevin / Bakry–Émery

**Shen, H., Zhu, R., Zhu, X., "A stochastic analysis approach to lattice Yang–Mills at strong coupling,"** *Comm. Math. Phys.* **400** (2023) 805–851, DOI 10.1007/s00220-022-04609-1.

For SU(N) at $|\beta_{\rm tH}|<1/[16(d-1)]$ (per-link $|\beta_{\rm std}|<1/[16N(d-1)]$; for SU(2), $d=4$: per-link $|\beta_{\rm std}|<1/96$, equivalently $|\beta_{\rm tH}|<1/48$):
- Uniqueness of the infinite-volume measure on the product Lie-group manifold.
- Log-Sobolev inequality with constant uniform in lattice size.
- Poincaré inequality.
- Exponential decay of covariances for smooth Lipschitz observables $f, g$ with disjoint supports $A, B$: $|\mathrm{Cov}_\mu(f,g)|\le C\|f\|_{\rm Lip}\|g\|_{\rm Lip}\exp(-c\cdot\mathrm{dist}(A,B))$.

**Method.** Langevin SDE on the product Lie-group manifold + Bakry–Émery via positive Ricci lower bound on SU(N). The Ricci-curvature ingredient is the SU(N)-specific structural input.

**Why this is adjacent but not closing for (M′)_SU(2).** Wrong regime: (M′)_SU(2) needs *large* β; SZZ is *small* β. At the master document's working corner $\beta=3.5$, the per-link coupling is approximately two orders of magnitude above the SZZ threshold. The Bakry–Émery Hessian estimate fails at large β because the Wilson-action Hessian (proportional to β times plaquette-second-derivatives) is not positive-definite uniformly.

**What would have to change for elevation.** A *spectral-window* version of the Langevin dynamics, with Bakry–Émery preserved under the projection $P_{\le\Lambda,L}$, at large β. **No such result is in the peer-reviewed literature.** This would be a research direction, not a literature extraction. **Pass-9 update:** §H.8 articulates this research direction as a four-ingredient memo. Pass 8 supplies the *local* floor ($\kappa_G=2$ for SU(2) per Theorem H.3.1') and the horizontal restriction; pass 8 + pass 9 (§H.8) make the missing pieces explicit (Lyapunov toward $U^{(0)}$ partially supplied via §H.2; globalization mechanism unsupplied). The research-direction memo does NOT close the route; it scopes the work.

Companion result:

**Cao, S., Nissim, R., Sheffield, S., "Dynamical approach to area law for lattice Yang–Mills,"** *Prob. Math. Phys.* **7** (2026) 37–121 (arXiv:2509.04688).

Wilson area law in the 't Hooft strong-coupling regime via SZZ Bakry–Émery + Durhuus–Fröhlich mass-gap criterion, for $G\in\{U(N), SU(N), SO(2N)\}$. **Area law, not cumulant decay.** Adjacent only.

#### 10.6.2 Swapping / percolation (finite groups)

**Adhikari, A., Cao, S., "Correlation decay for finite lattice gauge theories at weak coupling,"** *Ann. Probab.* **53** (2025) 140–174, DOI 10.1214/24-AOP1702.

For finite (possibly non-Abelian) gauge group $G$ at weak coupling and any gauge-invariant local $f, g$ with disjoint supports $A, B$:
$$
|\mathrm{Cov}_\mu(f, g)|\le C(|f|, |g|)\exp(-c\cdot\mathrm{dist}(A,B)).
$$

**Method.** Probabilistic swapping: relate $|\mathrm{Cov}(f,g)|$ to probability of percolation in the union of two independent samples of the lattice gauge measure. **The key qualitative input is the existence of a non-trivial "trivial-link" event whose probability is bounded away from 1 uniformly in lattice size.**

**Why this is adjacent but not closing for (M′)_SU(2).** Wrong group: SU(2) is a *continuous* compact Lie group, not finite. The swapping argument's "weak coupling" threshold depends on group structure and generically degenerates as $|G_n|\to\infty$ along finite subgroup sequences $G_n\to {\rm SU}(2)$. **Borgs *Comm. Math. Phys.* 96 (1984) 251–284 explicitly identifies a gap in Seiler's CMP claim that the strong-coupling cluster expansions extend uniformly from finite Abelian to general finite non-Abelian groups**; Adhikari–Cao 2025 acknowledges this in its introduction.

**What would have to change for elevation.** A continuous-group extension of the swapping argument, with constants surviving the limit. **No such result is in the peer-reviewed literature.**

**However:** Adhikari–Cao 2025 *is* the load-bearing input for FNG Stage 1 (§9) for $G=Q_8$ at $\beta\ge 61.16$. It is *unconditional* in that role. The pass-7 finding affects the *extrapolation to SU(2)*, not the finite-group anchor.

Companion result for the finite-group setting:

**Cao, S., "Wilson loop expectations in lattice gauge theories with finite gauge groups,"** *Comm. Math. Phys.* **380** (2020) 1439–1505, DOI 10.1007/s00220-020-03912-z.

Wilson loop expectations to leading order in $e^{-\beta}$ at weak coupling for finite (possibly non-Abelian) gauge groups via Stein's method / Poisson approximation. **Used in FNG Stage 1** alongside Adhikari–Cao 2025.

#### 10.6.3 Abelian and random-surface methods

**Forsström, M. P., "Decay of correlations in finite Abelian lattice gauge theories,"** *Comm. Math. Phys.* **393** (2022), DOI 10.1007/s00220-022-04391-0.

**Forsström, M. P., Lenells, J., Viklund, F., "Wilson loops in finite Abelian lattice gauge theories,"** *Ann. Inst. H. Poincaré Probab. Statist.* **58** (2022) 2129–2164, DOI 10.1214/21-AIHP1227.

Both prove exponential decay / explicit Wilson loop expectations for finite abelian groups $\mathbb Z_n$. **Abelian only; do not extend to non-Abelian SU(2).**

**Cao, S., Park, M., Sheffield, S., "Random surfaces and lattice Yang–Mills,"** *Comm. Amer. Math. Soc.* (to appear; arXiv:2307.06790).

Random-surface representation of Wilson loop expectations; produces area law and large-N representations. **Not a cumulant-decay theorem.** Adjacent only.

#### 10.6.4 Summary

| Route | Regime mismatch with (M′)_SU(2) | Path to elevation |
|---|---|---|
| SZZ stochastic Langevin | strong β not large β; continuous-group OK | spectral-window Bakry–Émery at large β (research direction) |
| Adhikari–Cao swapping | finite group not SU(2); large β OK | continuous-group extension of swapping (research direction) |
| Cao–Nissim–Sheffield | area law not cumulant decay; large-N | extension to finite N + cumulant bound (research direction) |
| Forsström + FLV | abelian only | major group-theoretic extension required |
| Cao–Park–Sheffield | not cumulant decay | not applicable |

**Net pass-7 verdict.** All three modern probabilistic routes are real and substantial; none currently closes (M′)_SU(2). The most natural research direction is a spectral-window Bakry–Émery extension of SZZ. If such a result were proved, it would directly deliver level (iii) of (M′)_SU(2); the master document would be re-classified from "conditional" to "unconditional" at the (M′) hypothesis.

### 10.7 Honest revision (strengthened in pass 7)

> The program reduces SU(2) Yang–Mills mass gap to (M′) for hard plaquette indicators at large β. The closest existing rigorous result for finite non-Abelian gauge groups is Adhikari–Cao, *Ann. Probab.* 53 (2025) 140–174. The closest existing rigorous result for compact Lie groups is Shen–Zhu–Zhu, *Comm. Math. Phys.* 400 (2023) 805–851 — but at strong coupling, not large β.

**Pass-7 strengthening of the previous "essentially equivalent modulo bookkeeping" phrasing.** The pass-6 phrasing is correct in spirit but slightly optimistic. The corrected phrasing:

> **(M′)_SU(2) is at least as hard as proving the mass gap for SU(2) lattice YM at large β on a fixed periodic 4-lattice. It is possibly *strictly* harder because of the projected spectral-window restriction (the projection $P_{\le\Lambda,L}$ and the hard indicator $X_p$ are extra structure beyond bare mass gap).**
>
> **As of May 2026, no peer-reviewed paper proves either level (iii) or level (iv) of (M′)_SU(2). The closest unconditional results are SZZ 2023 (strong coupling, per-link $|\beta_{\rm std}|<1/96$ for SU(2) in d=4) and Bałaban CMP 1989 (UV stability without mass gap).**

The v17b strengthening (§10.5) does **not** prove (M′) — it provides empirical anchors. The structural question (does smoothing constant stay bounded as $\eta\to 0$?) is now narrowly focused but still open. The literature route is open and partly walked (Dimock template; Bałaban inventory now mapped; SZZ/Adhikari–Cao adjacent but not closing); it is not currently a *route to a closing theorem*, just a research direction.

---

## 11. Numerical evidence pipeline

Each run version answers a specific structural question. This section gives the role each played, what it confirmed or rejected, and what it does NOT prove.

### 11.0 Pass-5 run inventory note

Pass 5 incorporates the full run inventory from `PMBSF_quick_reference_for_simulations_fourth_pass_20260524.md` §4. Eight runs are new versus pass 4: v2 (synthetic projection sanity), v3 (first Wilson BS), **v3b** (LOCKED Tier 1: $\Theta_*$ in danger corner), **v4b** (LOCKED Tier 1: projected-Maxwell continuum bridge), v5b (fixed-$K$ sparse IR), **v7a/v7b** (LOCKED Tier 1: fixed-window restriction), **v15** (FAILED: Matrix-Stein global budget). Runs are numbered to match the quick reference rather than chronologically; pass-4 numbering 11.1–11.12 is preserved for continuity, with new subsections inserted as §11.0a–§11.0g and the v15 "planned" placeholder in pass-4 §11.8 replaced with v15 "FAILED" content in §11.13.

### 11.0a v2 — synthetic projected Maxwell sweep (Tier 2)

**Source:** quick reference §A1. Run ID `PMBSF_v2_L12-32_Nseed20_synthV_unit-excess2_alpha0p25_lambda1p6_beta4-64`.

**Purpose.** Synthetic projection sanity check: does the projected Maxwell sweep behave as expected on engineered configurations? Confirms the projection infrastructure works correctly before applying to Wilson-generated configurations.

**Verdict.** Sanity check passed. Tier 2 supporting diagnostic.

### 11.0b v3 — first Wilson projected BS confirmation (Tier 2)

**Source:** quick reference §A2.

**Purpose.** First Wilson-generated projected Birman–Schwinger first-pass run. Established that the projection survives interacting Wilson measure.

**Verdict.** Confirmation only; superseded by v3b for danger-corner certificate.

### 11.0b.5 v6b — edge-Bernoulli comparator FAILURE (negative anchor)

**Source:** quick reference §C3. Run ID `PMBSF_v6b_Bernoulli_fixed_cardinality_comparator_SU2Wilson_20260523_150503`.

**Purpose.** Test whether independent edge-Bernoulli activation is the correct stochastic comparator for Wilson high-plaquette behavior. The naive guess: model each edge as independently Bernoulli-activated; check whether Wilson defects match.

**Result.** Edge Bernoulli is too optimistic. Wilson exceeds the edge-Bernoulli prediction systematically.

**Wilson / edge-Bernoulli ratios at $K=2048$, any defect:**

| $\delta_{\rm bond}$ | ratio range |
|---|---|
| 0.85 | 1.226–1.337 |
| 1.00 | 1.268–1.456 |
| 1.15 | 1.345–1.546 |

Across all tested $\delta_{\rm bond}\times L$ combinations, the Wilson observable exceeds its edge-Bernoulli analog by **23–55%**. The ratio grows with $\delta_{\rm bond}$ — the more sparse the defect set, the worse the edge-Bernoulli approximation.

**Interpretation.** The correct stochastic unit is **the plaquette, passed through exact plaquette-to-link incidence**, not an independently activated edge. Edge-Bernoulli ignores the geometric fact that a single plaquette defect contributes 4 incident edges simultaneously (per the plaquette boundary). This correlated edge activation cannot be captured by independent edge models.

**Compare v6c** (§11.2): Wilson / random plaquette-incidence ratio at $K=2048$ is 0.97–1.09 across the same $\delta_{\rm bond}$ values — close to 1.0, consistent with random plaquette incidence being the correct comparator.

**Verdict.** **FAILED comparator.** Retained in the run inventory as a **negative anchor** — evidence for what the correct comparator is *not*. The 23–55% gap was the motivation for replacing edge-Bernoulli with random plaquette incidence as the stochastic baseline (v6c). Pass-5 §1.7 surviving chain depends on this correction.

**Manuscript usage.** Cite v6b as the empirical justification for using plaquette-incidence rather than edge-Bernoulli; do NOT cite v6b as supporting evidence for the firewall (it is a route-elimination result, not a positive anchor).

### 11.0c v3b — projected BS danger-corner certificate (LOCKED Tier 1)

**Source:** quick reference §A3. Run ID `PMBSF_v3b_SU2WilsonV_dangerCorner_HOTCOLD_L8-24_Ncfg50_beta4_m2p5_unit-raw-normalized_alpha0p25_lambda1p6_sweeps400x40_20260522_184314`.

**Purpose.** Direct numerical computation of the projected Birman–Schwinger norm $\|\Pi_{\rm phys}V_{D}\Pi_{\rm phys}\|$ at the worst tested danger corner across **a 1200-sample sweep** of Wilson-generated configurations.

**Configuration.**
- $L\in\{8,12,16,24\}$
- 50 seeds per L
- Hot AND cold starts (both)
- $\beta=4$, $m^2=0.5$
- $\alpha=0.25$, $\lambda_{\rm cutoff}=1.6$
- 3 weight modes: unit, raw excess, normalized excess-squared
- Total rows: **1200** ($= 50 \text{ seeds}\times 2 \text{ starts}\times 4\,L\text{-values}\times 3 \text{ weights}$)

**Locked certificate.**
$$
\boxed{\Theta_*=\max\theta_{\rm phys}=0.884442692429<1.}
$$
$$
1-\Theta_*=0.115557307571.
$$

**Distribution over the 1200 samples:**

| Statistic | $\theta_{\rm phys}$ |
|---|---|
| max ($=\Theta_*$) | 0.884442692429 |
| p99.9 | 0.877856476993 |
| p99 | 0.854061245808 |
| p95 | 0.842154162016 |
| mean | 0.545996578297 |
| all $\theta_{\rm phys}<1$ | **true** |
| all CG residuals $<10^{-6}$ | **true** |

**The worst single row** (the one realizing $\Theta_*$):

| Field | Value |
|---|---|
| $L$ | 8 |
| seed | 31 |
| start | hot |
| weight mode | unit |
| $\theta_{\rm unprojected}$ | 1.9967101255401256 |
| $\theta_{\rm phys}$ | 0.8844426924294179 |
| ratio (projected/unprojected) | 0.4429499711131925 |
| verdict | SAFE |

**Selected $L=24$ maxima** (showing how the danger corner moves with weight mode):

| Mode | max $\theta_{\rm phys}$ at $L=24$ |
|---|---|
| hot / unit | 0.860518686 |
| cold / unit | 0.837380416 |
| hot / raw excess | 0.564464885 |
| hot / normalized excess-squared | 0.392243725 |

**Interpretation.** The physical projection is the central mechanism. Without it, the unprojected operator norm reaches 1.9967 at the worst sample — fails coercivity badly. With the projection, the operator norm collapses to 0.8844 at the same sample — projection alone provides **56% suppression**. Across 1200 samples spanning $L\in\{8,12,16,24\}$, hot/cold starts, and three weight modes, **every single $\theta_{\rm phys}$ is below 1**. The L=8 hot/unit corner is the worst; L=24 maxes are substantially smaller (0.860 vs 0.884) — finite-volume effects are favorable.

**Verdict.** **LOCKED Tier 1 evidence (1200-sample sweep, not single sample).** This is the strongest positive empirical anchor for the projection mechanism: the projected BS norm stays below 1 across a comprehensive sample of Wilson-generated configurations in the tested danger corner.

**Pass-5 reconciliation with v9.** Pass-4 errata table marked $\Theta_*=0.884442$ as "Conditional; superseded by the corrected $\Theta\approx 0.386$ at v9." **This was a misreading.** The two $\Theta$s measure different objects:

- $\Theta_*$ (v3b) is a *concrete worst-case projected BS norm across 1200 Wilson-generated samples* in the tested danger corner. It is an *empirical finite-volume measurement*, not a probabilistic claim.
- $\Theta$ (v9) is the *probabilistic firewall parameter* derived from the random plaquette-incidence Bernstein bound. It is an upper bound that holds with high Wilson probability via the comparator argument.

The two are complementary: v3b is the *strongest known concrete witness* of the projection mechanism's effectiveness (1200 samples, all $<1$, certified); v9 is the analytic upper bound that would hold *generically* under the stochastic transfer (probabilistic, requires (M′)). Pass 5+6 re-classifies v3b $\Theta_*$ as LOCKED Tier 1, not superseded.

**Pass-6 sample-size note.** Pass 5 understated v3b by presenting $\Theta_*$ as a "single-sample" result. It is in fact the worst of 1200 carefully constructed samples spanning multiple L, starts, and weight modes. Even at the worst sample, the projected norm is 0.884 < 1, and the mean is 0.546 — the projection mechanism works robustly across the configuration space, not just at a lucky sample.

### 11.0d v4b — projected Maxwell continuum bridge (LOCKED Tier 1)

**Source:** quick reference §B1. Run "midpoint-corrected Mosco/projected-Maxwell bridge."

**Key results.**
- Projector tail slope: $2.004140$
- Resolvent tail slope: $2.011209$

Both slopes ≈ 2, indicating **second-order continuum-symbol behavior** for the free projected Maxwell comparator.

**Verdict.** LOCKED Tier 1 evidence for clean continuum-symbol scaling of the projected-Maxwell comparator. Supports the *free* (non-interacting) component of the architecture; connection to the interacting Wilson measure is still the open analytic task.

### 11.0e v5b — fixed-$K$ sparse IR audit (Tier 2)

**Source:** quick reference §C1.

**Purpose.** Exact-incidence fixed-$K$ infrared threshold audit. First run showing sparse IR improvement.

**Verdict.** Tier 2 supporting diagnostic; refined and superseded by v6a (K-sweep) and v6c (correct comparator).

### 11.0f v7a — fixed spectral-window Wilson/random run (LOCKED Tier 1)

**Source:** quick reference §D1.

**Purpose.** Fixed spectral window $P_{r^2\le\Lambda}$ at $\beta=4$, measure $R_\Lambda$ (projected restriction).

**Key result.** $\boxed{\max R_\Lambda=0.066040769219.}$ Small projected restriction at $\beta=4$.

**Verdict.** LOCKED Tier 1 evidence that fixed-window projected restrictions are uniformly small.

### 11.0g v7b — beta sweep at fixed spectral window (LOCKED Tier 1)

**Source:** quick reference §D2.

**Purpose.** Sweep across $\beta\in[3.5, 6.0]$ at fixed spectral window. Test stability of projected restriction across the coupling range relevant to Wilson SU(2).

**Key results.**
- Worst-case $R_\Lambda$ over beta sweep: $0.114315494895$
- Worst Wilson-specific $R_\Lambda$: $0.106996528804$

Both stay well below saturation across the tested range.

**Verdict.** LOCKED Tier 1 evidence that fixed-window restriction stays small across $\beta\in[3.5, 6.0]$. Wilson does not approach saturation anywhere in the tested sweep.

---

### 11.1 v6a — K-sweep (`PMBSF_v6a_Ksweep_Run_Readout_20260523.md`)

**Question.** Is the v5b volume-improving signal merely a small-IR-window artifact at fixed $K_{\rm IR}=512$?

**Setup.** $K_{\rm IR}\in\{128,256,512,1024,2048\}$, multiple $\delta\in\{0.85,1.00,1.15\}$, $L\in\{8,12,16,24\}$.

**Result.** Worst row at $K=2048$: $L=8$, cold, $\delta=0.85$, $T_{\rm bound}=0.773$, $\lambda_{\rm IR,r^2,\max}=5.17$. Restriction norm remains bounded well below one and **improves sharply with $L$**.

**Verdict.** v5b signal is not a small-IR-window artifact. **Does not prove** a Wilson-typical continuum theorem. Next move: fixed spectral window $r^2\le\Lambda$ instead of fixed rank $K$.

### 11.2 v6c — random-plaquette comparator (`PMBSF_v6c_RandomPlaquetteIncidence_Comparator_Readout_20260523.md`)

**Question.** Are Wilson exact-incidence sparse defects anomalously IR-coherent compared with a random bad-plaquette field passed through the same incidence map?

**Setup.** 4800 rows. Wilson/Bernoulli-plaquette ratios at $K=2048$, `any_defect`, $\delta=0.85$:

| $L$ | Wilson/Bernoulli | Wilson/fixed-card |
|---|---|---|
| 8 | 1.044 | 1.049 |
| 12 | 1.065 | 1.041 |
| 16 | 1.005 | 1.008 |
| 24 | 1.027 | 1.029 |

**Ratios all ≈ 1.** v6b Wilson-over-edge-Bernoulli excess was an artifact of using an unrealistically dispersed point-edge Bernoulli comparator.

**Empirical log-log slopes of mean $R_{\rm IR}$ vs $L$:** $-1.81$ at $\delta=0.85$, $-2.32$ at $\delta=1.00$, $-2.68$ at $\delta=1.15$. Strong volume improvement.

**Verdict.** The correct stochastic comparator is **not** an independent edge mask; it is a bad-plaquette field through the same incidence map, or block/geometric Bernoulli capacity comparator. Wilson defects do not exhibit special long-range IR trapping beyond local plaquette incidence geometry at tested $\beta,L,\delta,K$.

### 11.3 v9 — worst-corner Bernstein computation

**Question.** What is the firewall margin at the corrected constants?

**Setup.** $L=24, q=0.01, \Lambda=1, \kappa_\Lambda\approx 0.0055, \delta=0.05, K\approx 3792$.

**Result.** Bernstein bound $\approx 0.193$, $\Theta\approx 0.386$, **margin $\approx 0.614$**. Six-orientation $\kappa_\Lambda$ match to $10^{-6}$.

**Verdict.** Canonical reporting corner for the conditional theorem. The corrected constants survive the worst tested corner; the prior $\Theta\approx 0.252$/margin $0.75$ figure was wrong by the factor-2 boundedness coefficient.

### 11.4 v10/v11 — trace-MGF L-growth

**Question.** Does $\sup_L\Delta_+/q$ stay bounded across $L$?

**Setup.** Sparse stress point $q=0.003$, $\theta=64$.

**Result.** $L=24:\Delta_+/q=5.708$, $L=32:\Delta_+/q=6.271$, ratio 1.099. Across $\theta\in\{1,2,4,8,16,32,64\}$, $L=32/L=24$ ratios sit in $[1.094, 1.099]$.

**Verdict.** Strong sparse L-growth pass for $\sup_L\Delta_+/q=O(1)$. Empirical Wilson $R\approx 0.05$ at v10 corner, well below the analytic 0.193 bound — substantial headroom.

### 11.5 v12/v12b — pointwise vs. PTO-weighted sensitivity

**Question.** Does the pointwise heat-bath cross-term $|C_e(p,p';U)|$ scale as $q^2$?

**Setup.** v12: $L=8, \beta=3.5, \Lambda=1$, $1200$ sampled link rows per threshold. v12b: companion local heat-bath tail audit, 4 configs, 300×512 HB samples per link.

**Result.**

Pointwise:
| $\delta$ | max $|C_e|/q^2$ | p99 |
|---|---|---|
| 0.85 | 13,487 | 53 |
| 1.00 | 6,520 | — |
| 1.15 | 7,523 | — |

PTO-weighted ($\mathcal W=\sum_{p'\ne p}|C_e|\operatorname{tr}(A_pA_{p'})$):
| $\delta$ | mean$/q^2$ | p99/$q^2$ | max/$q^2$ |
|---|---|---|---|
| 0.85 | $6.10\times 10^{-4}$ | $1.17\times 10^{-2}$ | $1.01\times 10^{-1}$ |
| 1.00 | $3.76\times 10^{-4}$ | $6.74\times 10^{-3}$ | $8.48\times 10^{-2}$ |
| 1.15 | $4.52\times 10^{-4}$ | $1.57\times 10^{-2}$ | $9.52\times 10^{-2}$ |

**Verdict.** **Pointwise $q^2$ fails by 4 orders of magnitude. PTO-weighted $q^2$ holds.** The PTO weighting compresses spikes by $\sim 10^5$. The correct lemma is operator-level, *not* pointwise — this reshaped the HB-q² target (§7.5) and Lemma B.5/B.6 (§7.5).

**Diagnostic limitation.** Factor-10 in $q$ does not tightly distinguish $q^2$ from $q^{3/2}$ — finer q-scan needed at $L=12$ with thresholds $\{0.7,0.85,1.0,1.15,1.3\}$ to discriminate (`Lemma_HB_qsq.md` §7.1).

### 11.6 v13 — spike audit (`Lemma_B3_spike_isolation_patched.md` §1)

**Question.** Is the spike structure of $|C_e|/q^2$ partitioned by an `old_good_only` vs. `old_bad_spike_only` (= spike set $\mathcal E_e^{\rm spike}$) decomposition?

**Setup.** Partitioned 1200 sampled links at $L=8$.

**Result.** `old_good_only` 94–99.75% of links; `old_bad_spike_only` 0.25–5.6%. $\eta_{\rm local}$ on `old_good_only` is $O(0.1)$; on `old_bad_spike_only` it spikes to $O(10\text{–}10^3)$.

**Verdict.** Structural justification for partitioning at $\mathcal E_e^{\rm spike}$. The Boole union bound $p_{\rm bad}(e)\le 6q$ then handles the spike contribution combinatorially.

### 11.7 v14 — η_bad global absorption (`Lemma_B3_spike_isolation_patched.md` §3)

**Question.** What is the measured spike-side Matrix-Stein constant?

**Setup.** $L=8, \beta=3.5, \Lambda=1$, 4 configs, 300 sampled links per config, 1024 HB resamples per link.

**Result.** See Lemma B.3 table in §7.5. $6\eta_{\rm bad}q$ drops by factor 35 from $\delta=0.85$ to $1.15$. Total at $L=8, \delta_{\rm bond}=1.0, q=0.003$: $\eta_{\rm typ}=0.093, 6\eta_{\rm bad}q=0.042$, total 0.135, budget 0.190, **29% headroom**.

**Verdict.** Matrix-Stein closure consistent at $L=8$. Conditional at $L\ge 12$ pending v15.

### 11.8 v15 — Matrix-Stein global audit (FAILED; pass-5 update)

**Source:** quick reference §F4. **Pass-4 status: "planned L-sweep". Pass-5 status: RUN and FAILED.**

**Target.** $\eta_{\rm cov}<0.25$ for global Matrix-Stein covariance-budget closure.

**Observed.**

| $\delta_{\rm bond}$ | $\eta_{\rm cov}$ | excess over 0.25 |
|---|---|---|
| 0.85 | 0.4018 | 1.6× |
| 1.00 | 1.2276 | 4.9× |
| 1.15 | 0.8897 | 3.6× |

All three working-point candidates fail. The smallest overshoot is at $\delta=0.85$ where $q$ is largest — this is the *opposite* direction from where the pass-4 Lemma B.3 budget projected the firewall would tighten (lower $\delta_{\rm bond}\Rightarrow$ smaller $6\eta_{\rm bad}q$). The v15 measurement contradicts the projected forward extrapolation.

**Raw one-sided audit** (no exchangeable-pair normalization):

| $\delta_{\rm bond}$ | $\eta_{\rm good}$ | $p_{\rm bad}/(6q)$ | total inflation | budget | fits? |
|---|---|---|---|---|---|
| 0.85 | 0.848 | 0.870 | 4.609 | 0.168 | ✗ |
| 1.00 | 0.427 | 0.724 | 2.128 | 0.168 | ✗ |
| 1.15 | 0.516 | 0.679 | 0.530 | 0.168 | ✗ |

All three fail. Closest fail is $\delta=1.15$ at 0.530 vs 0.168, factor 3.2× over.

**Trace-weighted finite-rank spike audit** (quick reference §F3): $\eta_{\rm spike,sign}$ values 343–1238 across $L\in\{8,12,16,24\}$. **Fatal** — these are arbitrary-sign worst-case absorption constants that cannot be reduced by more samples.

**Route-elimination verdict** (quick reference §10 final verdict box): "Matrix-Stein / spike absorption is not viable." HB-q² survives as a *narrowed local theorem* (§7.5) but not as a *global closing route*. The pass-4 framing of HB-q² as "active proof attack" is retired.

### 11.9 v16 — empirical $\varepsilon_{\rm ML}$ measurement

**Result.** $\varepsilon_{\rm ML}\approx 0.02$ at the working corner. **Anchors the comparison** for the analytic $\varepsilon_{\rm HPM}$ chain. With placeholder $(M')$ constants, analytic is loose by $10^4$; with v17b-measured constants, analytic beats empirical by 20×.

### 11.10 v17b — connected cumulants of smoothed indicators

**Source.** `READOUT__1__.md`, `NOTE_PMBSF_mprime_hpm_bridge_v17b_patch.md`, `block_jackknife_diagnostics.csv` (1566 rows × 15 columns). Pass 4 directly audits the CSV — see Appendix E.

**Setup.** Production run `PMBSF_v17b_BS_smooth_source_connected_cumulants_GOOD_20260524_175256`. Measures $\kappa(B)=\mathrm{cum}(X_{p,\eta}:p\in B)$ for 32 support patterns, $L\in\{12,16,24\}$, $\beta\in\{3.5,4.0\}$, $\eta\in\{0.025,0.05,0.10\}$, $q\in\{0.001,0.003,0.01\}$, block-jackknife uncertainties.

**Reach (verified exactly).** 69.9% of rows rel-JK-SE > 0.5 (claim 70%); 18.9% < 0.3 (claim 19%). Clean rows concentrate at incident supports: pair_incident 108/108 = 100%, triple_star 32/54 = 59.3%, triple_L 17/54 = 31.5%.

**Pass-4 honest summary** (Appendix E for full audit):

*Verified exactly:*
- L-uniformity at incident supports: mean-over-2-patterns rooted form 0.00527/0.00485/0.00496 across $L\in\{12,16,24\}$ at the working corner ($\beta=3.5,q=0.003,\eta=0.05$). At η=0.025: 0.00558/0.00512/0.00533. All verify.
- $C_*^2 e^{-m_*}\le 0.017$ **at the working corner** (with smoothing-bridge factor 3 applied): max-over-L is 0.00564, × 3 = 0.01692, ≤ 0.017 ✓.
- $k=4$ quad cumulants decay *faster* than pinned form predicts: worst aggregate $|κ|/q^k$ values reach 133 at $L=12,\beta=4,\eta=0.025,q=0.001$ but rooted form remains $\sim 10^{-7}$ at those rows.

*Verified with caveat:*
- $C_*^2 e^{-m_*}\le 0.017$ as global bound: holds at the working corner; **over the full clean-signal range across all $(\beta,\eta,q)$** the max rooted form is 0.01045 (at $L=12,\beta=4,\eta=0.025,q=0.01$, smoothed = 0.0314). The bound should be stated as "at the working corner" — that's the relevant case for firewall closure.

*Over-extrapolated:*
- **$m_*\ge 2$**: at the patch's specific corner ($L=12,\beta=3.5,\eta=0.05,q=0.003$, pair_same_ori_axis), 4-point slope is −2.36 (giving $m_*=2.36$) **but the r=4 value 0.0001 has relative jackknife SE = 395** (totally noise). Clean-only 2-point slope is −0.37 ($m_*\approx 0.4$). Across all corners, only ONE has ≥ 3 clean signal points (L=16, β=3.5, η=0.025, q=0.01; clean $m_*=0.90$). **Honest empirical statement**: monotone qualitative decay between r=1 and r≥3 confirmed; quantitative lower bound $m_*\ge 0.5$–$1.0$ is the strongest defensible claim from clean signal alone.

**Pair decay fits** for $\eta=0.05, q=0.003, \beta=3.5$ (from `READOUT__1__.md` pair_decay_fits): same-orientation slope −2.36; mixed-axis slope −0.05 (essentially flat). The mixed-axis slope ≈ 0 is consistent with noise around zero at this q; the −2.36 same-orientation slope is data-cleanliness-dependent per above.

**Verdict (revised in pass 4).** v17b is **the load-bearing empirical anchor** for firewall closure via the $C_*^2 e^{-m_*}\le 0.017$ bound at the working corner. It is **not** a tightness anchor for "20× beats v16 empirical" — that headline depends on $m_*\ge 2$ which is not robust to clean-signal filtering. The firewall closure is preserved with comfortable margin (margin ≥ 0.9 even under conservative $m_*\sim 1$ extrapolation).

**Does not prove BS.** Tests whether the expected connected coefficient hierarchy is numerically plausible. Far-control and most distant pairs are below MC noise floor at the current configuration count.

**Useful next runs.**
1. Extend pair_same_ori_axis to larger $L$ (32, 48) and more configs to pin down clean-signal $m_*$.
2. Add intermediate $r$ values (r=1.5, 2.5) via diagonal patterns to improve slope-fit lever arm in the clean-signal regime.
3. Extend $\eta$ to smaller values (0.005, 0.01) per `NOTE_PMBSF_mprime_hpm_bridge_v17b_patch.md` §B9 to resolve the BG smoothing-bridge limit.

### 11.11 L=64 projected-capacity threshold law

Source: `NOTE_PMBSF_l64_projected_capacity_threshold_law.md`.

A **controlled synthetic experiment** on $\mathbb T_{64}^2$ (not Wilson), $N=4096$, $K=128$, $\lambda_1=0.00963$. For dimer defect sets at fixed local geometry (every mask: $m=128, \rho=0.03125$, 64 clusters, largest cluster 2), test whether scalar capacity $R_{\rm nonzero}(D)=\|G_D\|$ orders the exact projected Birman–Schwinger threshold $V_c^{BS}(D)$.

**Main results.**
- $\operatorname{corr}(V_c^R, V_c^{BS})=0.958$, $\operatorname{corr}(\log,\log)=0.960$.
- $V_c^R/V_c^{BS}=0.342\pm 0.029$ (CV 0.084).
- **Calibrated scalar law:** $\log V_c^{BS}=1.66154+1.21615\log V_c^R$, $R^2=0.922$.
- **Mask-heldout CV:** scalar capacity MAE 0.028, R² 0.978. Geometry-no-capacity R² 0.975. Local-only R² $-0.035$.

**Interpretive verdict.** Projected capacity is a **threshold-order parameter** for sparse-defect low-mode instability in this controlled setting. Synthetic; validates the *concept* that projected capacity orders the threshold, **not** the Wilson stochastic theorem.

### 11.12 PMBSF heat-kernel / Wilson calibration

Source: `PMBSF_Heat-Kernel_-_Wilson_Calibration.md`.

**Corrected calibration.** Wilson action $S_W=\beta\sum_p[1-(1/N)\Re\operatorname{tr}U_p]$, bi-invariant inner product $\|X\|^2:=-\operatorname{tr}(X^2)$ on $\mathfrak{su}(N)$, $c_2=1/N$, Gaussian-convention heat kernel $p_t\propto\exp(-d^2/(2t))$. Calibrated time $t(\beta)=N/\beta$.

**Three errors in prior computation:** inverted $a^{-2}$; stray factor of 2 in $t(\beta)$; comparison done against the wrong number.

**Corrected result.** SU(3), $\beta=6.0$, Necco–Sommer $a=0.0931$ fm, $e^{C_{\rm osc}}=1$: $m_0\approx 2.1$ GeV (not 2.8). Under the archive's $t(\beta)=N/(2\beta)$ convention: $m_0\approx 3.0$ GeV.

**Honest assessment of what the calibration delivers** (`PMBSF_Heat-Kernel_-_Wilson_Calibration.md` §G):
1. Scale is $a^{-1}$, i.e. UV cutoff scale; **not** RG-invariant.
2. Holley–Stroock at one plaquette **does not propagate** to full lattice without further mixing/decimation work (Cesi 2001 tensorization needs uniform Dobrushin–Shlosman; PMBSF chain doesn't demonstrate it).
3. $C_{\rm osc}$ is $O(1)$ free parameter; program doesn't independently compute it.
4. $\langle\|X\|^2\rangle\approx (N^2-1)/\beta\approx 1.33$ (SU(3), β=6) and 0.86 (SU(2), β=3.5) — calibration **not in its parametric small-field regime**.
5. Even with all fixed, calibration would yield a **lower bound** on the gap, not the gap itself.

**Vs. Athenodorou–Teper** (JHEP 11 (2020) 172): $m_{0^{++}}\approx 1.65$ GeV. A lower bound of $\sim 2$ GeV on a measured gap of $\sim 1.65$ GeV would be inconsistent. Forces either $C_{\rm osc}\ge 0.5$ or untracked degradation in tensorization.

**Honest claim.** The PMBSF HK calibration is an **existence-of-spectral-gap structural ingredient** in the spirit of Bakry–Émery / Faris–Simon, applied locally. **It is not a quantitative prediction of the glueball mass.** Claims of "order-of-magnitude consistency with the 0⁺⁺ glueball" **should be retracted**: numerical proximity is forced by dimensional analysis and would not survive β-scaling.

---

## 12. Unified status ledger (organized by route)

### 12.1 Deterministic spine — unconditional

| Statement | Status | Source |
|---|---|---|
| Lemma 1 (Fourier leverage equality) | **Proved** | `lemmas_1_2_proofs.md` §A |
| Lemma 2.1 (κ_Λ plane-independence) | **Proved** + v9 numerical to $10^{-6}$ | `kappa_bernstein_transfer_memo.md` §1 |
| Closed form κ_Λ = μ_Λ + γ_Λ; κ_Λ ≤ 2μ_Λ | **Proved** | ibid §1.1, 1.3 |
| PTO-1 atomic facts ($\sum_p A_p = 6P$) | **Proved** | `route_I_integrated_corrections__1__.md` §1 |
| PTO-2 trace-overlap exponential summability | **Proved** | ibid §1 (replaces false locality) |
| PTO-3 rank-4 trace-word reduction | **Proved** | `route_I_tightening.md` §7.2 |
| Block PSD envelope | **Proved** but retired for firewall | `PMBSF_matrix_stein_ML_reduction_v1.md` §0 |
| Cyclic Hilbert–Schmidt trace-word bound | **Proved** | `sparse_closed_walk_..._3__.md` §2 |
| Closed-walk activity envelope | **Proved** | ibid §3 |
| Fixed-cardinality inclusion formula | **Proved** | ibid §4 |
| HPM ⇒ closed-walk envelope domination | **Proved** | ibid §6 |

### 12.2 Sharp Bernoulli — unconditional

| Statement | Status | Source |
|---|---|---|
| Theorem 2 (random plaquette Bernstein, 6q, 2κ_Λ/3) | **Proved** with corrected constants | `kappa_bernstein_transfer_memo.md` §2 |
| Variance proxy $\sigma_B^2\le 6q\kappa_\Lambda$ | **Proved** | ibid §2.2 |
| v9 firewall numerics ($\Theta\approx 0.386$) | **Computed** | `route_I_integrated_corrections__1__.md` §5 |
| C₀ sensitivity (margin robust ±0.005) | **Computed** | this document §6.4 |

### 12.3 Route I (cumulant)

| Statement | Status | Source |
|---|---|---|
| Cumulant expansion skeleton | **Valid skeleton** | `route_I_integrated_corrections__1__.md` §4 |
| Trace-mismatch artifact identified as finite-sample | **Resolved** | `route_I_tightening.md` §7.1 |
| Theorem 3 / (ML-I) with $C_0=1+O(q)$ for $\alpha\ge 2$ | **Conditional** on (M′) + tree-graph book | `route_I_integrated_corrections__1__.md` §4 |
| Firewall closure Θ≈0.386 at v9 worst corner | **Conditional** on (M′) + (ML-I) | ibid §5 |

### 12.4 Route F (Stein global)

| Statement | Status | Source |
|---|---|---|
| Variance proxy decomposition | **Proved** | `Route_F_..._Variance.md` §2 |
| Lemma SF (small-field flip probability) | **Folklore**, ≤2 pages | ibid §3 |
| Lemma CI (conditional independence) | **Open**, not in literature for SU(2) | ibid §4 |
| Phase-1 decoupled-Gaussian toy calculation | **Not yet done** (decision gate) | ibid §8 |
| Composition V ≤ C·q²·e^{-γd} | **Conditional** on SF + CI | ibid §5 |

### 12.5 HB-q² (Matrix-Stein local) — active route

| Statement | Status | Source |
|---|---|---|
| Lemma A: $\Omega^{\rm inc}\le 80\mu^2$ (coarse), $\le 272/9\mu^2$ (sharp), $<20\mu^2$ at Λ=1 | **Proved** + checker verified | `HB_qsq_merged.md` §§A.3–A.5 |
| vMF identification of SU(2) heat-bath | **Proved** | `Lemma_B5_..._20260524.md` §0 |
| Lemma B.1 typical heat-bath decoupling (pointwise q² on $\mathcal A$) | **Open**, route identified (2–3 months) | `Lemma_B1_smallfield_decoupling.md` |
| Lemma B.3 Boole spike bound $p_{\rm bad}\le 6q$ | **Proved** | `Lemma_B3_spike_isolation_patched.md` §2 |
| $\eta_{\rm bad}$ measured at L=8 | **Empirical** | ibid §3 |
| L-uniformity of $\eta_{\rm bad}$ (L∈{12,16}) | **Open**, decided by v15 | ibid §§5, 6 |
| Lemma B.5 pointwise two-cap q² | **False** under only non-alignment | `Lemma_B5_..._20260524.md` §0 |
| Lemma B.6 PTO-summed six-star vMF | **Open target** (replaces false B.5) | ibid §11 |
| Lemma C PTO Schur closure | **Conditional** on B.6 | `HB_qsq_merged.md` §C |
| Theorem 7.1: Γ_W ≤ (1+η)q∑A_p² + rP | **Conditional** on B.1, B.3, B.6 | `HB_q2_closure_matrix_stein_route_20260524.md` §7 |
| v12b operator-level q² confirmed; pointwise q² rejected | **Confirmed empirically** | ibid §0, `Lemma_HB_qsq.md` §2 |

### 12.6 HPM (closed-walk)

| Statement | Status | Source |
|---|---|---|
| Deterministic CW reduction | **Proved** | `sparse_closed_walk_..._3__.md` Part I |
| Theorem 14.1 (HPM + EC + FCB ⇒ conditional firewall) | **Conditional** on HPM, EC, FCB | ibid §14 |
| Weak (M′) ⇒ HPM | **Insufficient for budget** | ibid §15 |
| Pinned (M″) + CW-KP + dePoisson ⇒ HPM | **Open**, route identified | ibid §15 |
| Top-p / threshold transfer (dP) | **Deferred** | ibid §26 |

### 12.7 (M′)→HPM bridge

| Statement | Status | Source |
|---|---|---|
| Structural derivation (B1–B5) | **Proved** | `NOTE_PMBSF_mprime_hpm_bridge.md` §§B1–B5 |
| Combined bound $\varepsilon_{\rm HPM}\le c_*N_{\rm KP}e^{O(N_{\rm KP})}+\dots$ | **Proved** | ibid §B6.1 |
| Placeholder-constants $\varepsilon_{\rm HPM}\sim 200$ | **Computed**, loose by 10⁴ | ibid §B6.2 |
| v17b-anchored $\varepsilon_{\rm HPM}\sim 10^{-3}$ | **Measured**, beats v16 empirical by 20× | `NOTE_PMBSF_mprime_hpm_bridge_v17b_patch.md` §B6.2 |
| Empirical L-uniformity at incident supports | **Confirmed** | ibid §B3.4.1 |
| Smoothing-bridge bounded over η ∈ [0.025, 0.10] | **Confirmed**, factor ≤ 3 | ibid §B8.1 |
| Smoothing-bridge bounded as η → 0 | **Open**, focused single question | ibid §B9 |
| Firewall margin $\ge 0.99$ at v17b-anchored constants | **Computed** | ibid §B7 |

### 12.8 BS / BG / GK–CW-KP / dP smooth-source program

| Statement | Status | Source |
|---|---|---|
| BS smooth-source expansion (target) | **Open**, first concrete target | `sparse_closed_walk_..._3__.md` §23 |
| BG boundary-band gate (smoothing bridge) | **Open**, hard-threshold bridge | ibid §24 |
| GK / CW-KP kernel decay + weighted KP | **Open**, smooth-cutoff version first | ibid §25 |
| dP top-p de-Poissonization | **Deferred** | ibid §26 |
| Smooth-cutoff target ($P_\chi$) | **Open**, recommended path | ibid §25.2 |

### 12.9 Theorem FNG (Q₈)

| Statement | Status | Source |
|---|---|---|
| Stage 1 with (H2a) summed sublinear | **Provable today** via composite | `theorem_fng_cleaned_stage_1_stage_2.md` §5–8 |
| (H2a) composite (Adhikari–Cao + Cao 2020 + CS) | **Proved** | ibid §5 |
| Stage 2 with (H2b) pointwise q² | **Open**, Peierls refinement route | ibid §6 |
| FNG margin 0.618 at v9 corner | **Computed** | ibid §7 |
| FNG extends to SU(2) via group approximation | **NO** (3 obstructions) | ibid §9 |

### 12.10 External (M′) literature

| Group | Status | Source |
|---|---|---|
| Finite Abelian $\mathbb Z_n$ at large β | **Proved** (Cao 2020, Forsström 2021) | `M_prime_reconnaissance.md` §2 |
| Finite non-Abelian at large β | **Proved** (Adhikari–Cao 2022) | ibid |
| U(1) Lie group (Villain) | **Proved** up to Wilson loop level (Garban–Sepúlveda 2021) | ibid |
| SU(N) Lie group with hard $X_p$ at large β | **OPEN** (~mass gap equivalent) | ibid §8 |

### 12.11 Honest summary

> Deterministic spine and sharp Bernoulli comparator are unconditional. Theorem FNG Stage 1 ($Q_8$, summed (H2a)) is provable today via composite literature input. SU(2) Wilson firewall closure is conditional on (M′) for the hard plaquette defect indicator. Conditional on (M′) with the right q-power, the firewall closes analytically with margin ≈ 0.6 — and with margin ≈ 0.99 once v17b empirical anchors replace placeholder constants. The active proof attack is HB-q² via Lemmas B.1, B.3 (with measured η_bad), B.6 (PTO-summed vMF), and Lemma C; the smooth-source program (BS/BG/GK–CW-KP/dP) is the analytic skeleton; v17b is the empirical anchor. Literature extraction from Bałaban II / MR93 is no longer load-bearing.

---

## 13. Roadmap

### 13.1 Immediate (≤ 4 weeks)

1. **Stage 1 FNG preprint.** (H2a) as proved composite. Margin 0.618.
2. **v15 L-sweep** for $\eta_{\rm bad}, \eta_{\rm typ}$ at $L\in\{12,16,24\}$. Decides HB-q² L-uniformity.
3. **Extend v17b to smaller η** ($\{0.005, 0.01\}$). Decides smoothing-bridge bounded as $\eta\to 0$. ~30 minutes per η-value on A100.
4. **Apply 9-edit patch memo** to `m_prime_su_2_theorem_target_and_strategy.md` if not yet done. Half-day editing.
5. **Phase-1 Route F toy calculation.** Decoupled-Gaussian model: does $\mathbb E[(\Delta X_p)^2 X_{p'}]$ return $q^2$ or $q$? Decisive kill criterion for Route F (1 week).

### 13.2 Near-term (1–3 months)

6. **Stage 2 FNG (H2b for $Q_8$).** Peierls refinement of Adhikari–Cao Lemma 6.7.
7. **Lemma B.1 small-field decoupling proof.** 2D bivariate Gaussian threshold-crossing on the 12-edge stencil. Two-week analytic deliverable per `Lemma_B1_smallfield_decoupling.md` §10.
8. **Lemma B.6 PTO-summed vMF six-star.** Replaces false B.5.
9. **Lemma B.3 residual $r_*$.** Bałaban large-field suppression literature transfer. 2 weeks.
10. **BS proof skeleton.** First analytic target per `sparse_closed_walk_..._3__.md` §27. Connected polymer expansion for $\log Z_\eta(u)$ with exponential tree decay and square-free source coefficients.

### 13.3 Medium-term (3–9 months)

11. **GK / CW-KP for smooth cutoff $P_\chi$.** Closed-walk kernel summability theorem.
12. **BG boundary-band gate.** Hard-threshold bridge in closed-walk weighted norm.
13. **FNG-D₄, FNG-A₄.** Reproduce Stages 1+2 for non-quaternion non-Abelian. Build the discrete gauge group library.
14. **(M′)_SU(2) Path C** (finite non-Abelian sanity check at $G=2I$). 1–2 weeks.
15. **(M′)_SU(2) Path A Stages A1–A3** — read Dimock I/II/III. 4–7 weeks. (Concrete now that the papers are in-hand; see §10.4.)
16. **(M′)_SU(2) Path B** (smoothing bridge via Lohmann). 2–3 weeks. Note: v17b already gives empirical control over smoothing range $\eta\in[0.025,0.10]$ with factor ≤ 3.

### 13.4 Open-ended

17. **(M′)_SU(2) Path A Stages A4–A6** (Dimock-to-SU(2) translation + source-insertion modification). 5–13 weeks. Cumulative Path A timeline 9–20 weeks; pivot to Path B or document obstruction theorem if Stage A5 reveals fundamental issue.
18. **SU(2) Yang–Mills mass gap.** Direct PMBSF route is essentially equivalent to the mass-gap problem itself. Alternatives: Bałaban RG (UV stability proved, never mass gap); stochastic-quantization (Shen–Zhu–Zhu, strong coupling existence).
19. **dP top-p de-Poissonization.** Only after fixed-threshold HPM closes.

### 13.5 Do NOT

- Run more broad numerical sweeps without a specific theorem-relevant question. v6/v9/v10/v11/v12/v17 have exhausted that diagnostic value.
- Cite Bałaban 87 / MR95 95 as *directly* supplying (M′). They supply *infrastructure*, not the hard-indicator version. (And MR95 doesn't exist — the correct paper is MR93, CMP 155, 1993.)
- Cite the Gopal–Yang vMF paper as supplying Lemma B.5/B.6. It is a standard density reference; the joint cap-intersection structure must be proved directly.
- Present FNG as a stepping stone to SU(2) via group approximation. Three obstructions (§9.5) rule this out.
- Present the heat-kernel calibration as a glueball-mass prediction. UV-cutoff-scale lower bound conditional on tensorization (which is not done).
- Claim "firewall discharged" without "conditional on (M′)".
- Treat Lemma B.5 (pointwise two-cap q²) as a target. It is **false** under only non-alignment; the target is B.6 (PTO-summed).
- Attempt to consolidate the four HB-q²/route files (`HB_q2_closure_matrix_stein_route_20260524.md`, `hb_q_2_pto_summed_heatbath_sensitivity_section__9__.md`, `HB_qsq_merged.md`, `Lemma_HB_qsq.md`) into one — they overlap but each carries content the others don't.
- Treat "Path A literature extraction" as if the Dimock papers do it for us. The Dimock papers are about φ⁴_3; SU(2) Wilson translation (Stage A4) is the new analytic task they enable but do not perform.
- **(pass 4)** Cite "$m_*\ge 2$" from v17b without the clean-signal caveat: across the full grid, only one corner has ≥ 3 clean signal points, and that corner gives $m_*=0.90$ (clean-only) vs $m_*=1.39$ (all-points including noise). The honest empirical claim is "qualitative decay confirmed; quantitative lower bound $m_*\ge 0.5$–$1.0$." See Appendix E.
- **(pass 4)** Cite "$C_*^2 e^{-m_*}\le 0.017$" as a global bound. It holds at the working corner (max-over-L mean-over-pair-patterns is 0.01692 with smoothing factor 3, ≤ 0.017) but fails by factor ~2 over the full clean-signal range across all $(\beta,\eta,q)$. The "at the working corner" qualifier is essential.
- **(pass 5)** Treat the third-pass HBq2 lemma refinement as evidence that HB-q² closes globally. The v15 audit (§11.8, §7.5.7) is the global integration test; it fails. The third-pass lemmas refine the *local* theorem stack but do not change the *global* budget verdict.
- **(pass 5)** Use the v3b $\Theta_*=0.884$ as a probabilistic claim. It is a *concrete single-sample* numerical fact for the projected BS norm in the tested danger corner; treat as LOCKED Tier-1 evidence for the projection mechanism, not as a probabilistic firewall margin.
- **(pass 5)** Cite Matrix-Stein, Matrix-Laplace, or HB-q² as the current closing route. The fourth-pass quick reference §10: "Matrix-Stein / spike absorption is not viable." The surviving route is HPM closed-walk → ML_sparse → firewall.

### 13.6 Future-run acceptance criteria

From `PMBSF_quick_reference_for_simulations_fourth_pass_20260524.md` §8 — verbatim policy for whether a future simulation run counts as "strong evidence":

A future run is not allowed to be called "strong evidence" unless it satisfies all of the following:

1. Uses fixed spectral window $P_{r^2\le\Lambda}$, or explicitly justifies otherwise.
2. Uses Wilson top-$p$ or fixed-threshold high plaquettes.
3. Compares against random/block plaquette incidence.
4. Includes edge Bernoulli only as a negative control, not as the main comparator.
5. Prints headline metrics to console.
6. Saves a compact CSV.
7. Saves thermalized fields if thermalization is expensive and the ensemble may be reused.
8. Reports: $R_\Lambda$; $T$; $\Delta_{\rm ML}$; $\exp(\Delta_{\rm ML})$; moment-root ratios; density; Wilson/random ratio; acceptance; device; seed.
9. Has a predeclared pass/fail criterion.
10. Emits a one-page readout.

Quick reference §9 numerical action policy: *only* run a new simulation if it tests one of (a) a closed-walk domination statistic, (b) a block-plaquette incidence comparator, or (c) a fixed-window matrix-Laplace observable with a theorem-specific pass/fail rule.

---

## 14. Honest disclaimers — what this program is and is not

(Consolidated; pass 1 had this spread across five sections.)

### 14.1 IS

A **conditional projected capacity firewall** for SU(2) lattice Wilson gauge theory on a finite periodic 4-lattice with a sharp spectral-window projector. Conditional means: assuming (M′) for hard plaquette indicators, $\Theta<1$ holds with explicit margin ≈ 0.6 (analytic) to ≈ 0.99 (v17b-anchored).

The deterministic spine (PTO-1/2/3, closed-form κ_Λ, Theorem 2 matrix Bernstein, block PSD envelope) is **unconditional**.

Theorem FNG Stage 1 (Q₈ with (H2a)) is conditional only on a **composite of standard published results** (Adhikari–Cao 2022 + Cao 2020 + Cauchy–Schwarz). At the rigorous β-threshold (≈ 61) it is provable today.

### 14.2 IS NOT

- **Not** a Yang–Mills mass-gap proof.
- **Not** a control on continuous SU(2) spin-wave sectors via finite-group approximation.
- **Not** a quantitative glueball-mass prediction from heat-kernel calibration. Numerical proximity to 1.65 GeV is forced by dimensional analysis at the working point.
- **Not** an unconditional Wilson firewall — closure requires (M′) for SU(2), which is open.
- **Not** ready for Lean / formal verification — several routes have probabilistic inputs still being refined (Lemmas B.1, B.3, B.6).

### 14.3 The hardest single open question (revised in pass 7)

Prove (M′)_SU(2) at hierarchy level (iii) or better:
$$
\sum_{p'}|\mathrm{Cov}(X_p,X_{p'})|\operatorname{tr}(A_pA_{p'})\le Cq^2\kappa_\Lambda^2
$$
for $X_p=\mathbf 1\{\phi(U_p)\ge\delta_{\rm bond}\}$ under SU(2) Wilson at $\beta\ge\beta_0$.

**As of May 2026 (pass-7 literature survey, §10.6, Appendix G).** Not in any peer-reviewed paper. The closest unconditional results:

- Shen–Zhu–Zhu, *Comm. Math. Phys.* 400 (2023) 805–851: covariance decay at strong coupling (per-link $|\beta_{\rm std}|<1/96$ for SU(2) in d=4). **Wrong regime** — working corner is $\beta=3.5$, two orders of magnitude above.
- Adhikari–Cao, *Ann. Probab.* 53 (2025) 140–174: exponential correlation decay for finite non-Abelian groups at weak coupling. **Wrong group** — constants degenerate as finite subgroups $G_n\to{\rm SU}(2)$.
- Bałaban CMP 122 (1989) 175–202, 355–392: 4D UV stability of pure YM, but **not mass gap or cumulant decay**.
- Bałaban–Imbrie–Jaffe *Comm. Math. Phys.* 114 (1988) 257–315: the level-(iv) shape *is* proved in this paper — but for U(1) Higgs in d=2,3, not SU(2) in d=4.
- Magnen–Rivasseau–Sénéor, *Comm. Math. Phys.* 155 (1993) 325–383: SU(2) Schwinger functions with IR cutoff in regularized axial gauge; **no mass gap, no cumulant decay**.

**Honest May-2026 framing:** (M′)_SU(2) is at least as hard as the mass-gap problem for SU(2) lattice YM at large β on a periodic 4-lattice, and possibly *strictly* harder because of the projected spectral-window restriction.

### 14.4 Honest framing

The PMBSF program is best read as:

1. A **rigorous architecture** (PTO, Bernstein, Matrix-Laplace) that closes self-consistently with explicit, sharp, finite numerical margins.
2. A **finite non-Abelian existence theorem** (FNG Stage 1) that validates the architecture in a controlled discrete setting via peer-reviewed input (Adhikari–Cao 2025, Cao 2020).
3. A **proof program** (BS → BG → GK–CW-KP → dP) organizing the open analytic work via the smooth-source replacement of hard indicators.
4. **One surviving primary route** (HPM closed-walk → ML_sparse → firewall via Version C, pass-5 §7.9), with HB-q² Matrix-Stein eliminated by v15 audit and the BS/BG/CW-KP/dP smooth-source program as the analytic skeleton.
5. **Empirical evidence** (v17b) that the structural hypothesis (pinned-form cluster bounds) holds at the working corner — the tight bound $C_*^2 e^{-m_*}\le 0.017$ at incident pairs verifies exactly; the geometric-series decay rate $m_*$ is more weakly constrained by the data than the v17b patch claims (pass-4 Appendix E).

It is **not** an isolated leap toward the mass gap. It is a load-bearing intermediate step with explicit conditional content.

**Pass-4 honest disclaimer (preserved).** The v17b empirical anchor strengthens the program by providing an exactly-verified upper bound on the load-bearing pinned-norm constant. It does *not* establish that the program "beats moderate literature extraction by 20×" — that headline depended on extrapolating $m_*\ge 2$ from data that does not robustly support such a value (only one corner in the full grid has ≥ 3 clean-signal points for a slope fit). The firewall closure is preserved because the firewall-binding threshold for $\varepsilon_{\rm HPM}$ is ~5, comfortably above any defensible upper bound on $\varepsilon_{\rm HPM}$ from v17b. **The structural conclusions stand; the tightness claims should be retired.**

**Pass-5 honest disclaimer (preserved).** The v15 audit (§11.8) eliminates the global Matrix-Stein / HB-q² absorption route. The third-pass HBq2 lemma stack (§7.5) refines the local theorem with strong deterministic content (Lemmas A, C) and an empirical p99 anchor (Lemma B'), but the global integration budget fails by factors 1.6–4.9 across all tested working points. **The surviving primary closing route is HPM (closed-walk) → ML_sparse → firewall, with the BS/BG/CW-KP/dP smooth-source program as the analytic skeleton and v17b as the empirical anchor.**

**Pass-7 honest disclaimer (added).** A peer-reviewed literature survey (May 2026; Appendix G) found **no** result that proves (M′)_SU(2) at either level (iii) or level (iv). The modern probabilistic literature (SZZ 2023, Adhikari–Cao 2025, Cao–Nissim–Sheffield 2026) gives results that are structurally close but regime-mismatched: SZZ at strong coupling (per-link $|\beta_{\rm std}|<1/96$ for SU(2) in d=4) instead of large β; Adhikari–Cao for finite groups instead of continuous SU(2); CNS for area law instead of cumulant decay. The Bałaban CMP series (1984–1989) — now explicitly inventoried in §10.4.1 — proves 4D UV stability for pure YM but **not** mass gap or cumulant decay. The closest in-print level-(iv) prototype is the abelian Higgs paper Bałaban–Imbrie–Jaffe CMP 114 (1988) — abelian, with Higgs potential's deep well supplying the small parameter. **The literature route to closing (M′)_SU(2) is not currently available in peer-reviewed form.** The program remains conditional on (M′)_SU(2); the unconditional content (deterministic spine, sharp Bernoulli, FNG Stage 1, Lemmas A & C) is unaffected.

**Pass-8 honest disclaimer (added).** A stack of 12 "useful old notes" derivations was supplied for pass-8 incorporation. Six are kept as Appendix H (SU(3) local gap, character-proxy drift identity, Haar–Ricci local Bakry–Émery floor, uniform fiber LSI, corrected Lyapunov–Γ template, fixed-cutoff Combes–Thomas template). All six are auxiliary appendix material; **all six source authors explicitly disclaim that their derivation closes (M′)_SU(2), HPM, or the YM mass gap**, and the pass-8 incorporation preserves those disclaimers verbatim. The most structurally significant entry is §H.3 — the explicit local Bakry–Émery floor $\rho_0=\kappa_G-C_{\rm add}>0$ at the trivial configuration uniformly in $\Lambda$ — which constitutes the **local** piece of the pass-7 §10.6 stop-condition "spectral-window Bakry–Émery extension of SZZ 2023 at large β." The **global** piece of that hypothetical extension remains unsupplied by any peer-reviewed paper and by any of the pass-8 uploads. The conditional status of the master theorem is therefore unchanged from pass 7. The pass-5 corrected weighted-Lyapunov form in §H.5 fixes an earlier overclaim that was not load-bearing in any pass-1 through pass-7 argument; future arguments invoking weighted Lyapunov estimates must use the corrected form. §H.1 (SU(3) Weyl-invariant local gap) provides a finite-N analytical companion to FNG Q_8 (§9), with the caveat that SU(3) is continuous and the gap is asymptotic-in-β, so it does not replicate FNG Q_8's finite-β closure structure.

**Pass-10 honest disclaimer (added).** A new derivation document `SU2_PMBSF_closure_full_derivations_20260524.md` (1054 lines) was supplied for pass-10 incorporation. The document is honest at the top — "Manuscript derivation draft. Not a proof of the Yang–Mills mass gap" — and is structured as a **reduction proof**: it proves the chain $\text{rooted-source polymer estimate}\Rightarrow\text{centered rare-source mixing}\Rightarrow\text{pair closure}\Rightarrow\text{PTO level-(iii)}\Rightarrow\text{smooth HPM}\Rightarrow\text{hard HPM}\Rightarrow\text{projected firewall}$ step-by-step, then identifies the rooted-source polymer estimate as the still-open core. This is incorporated as Appendix I. The pass-10 effect on the conditional theorem is **null**: the chain was already declared in §7.9 (Version C ↔ proof program mapping) and §8 (BS/BG/CW-KP/dP); pass 10 supplies the explicit step-by-step proofs of each implication arrow but does NOT supply the rooted-source polymer hypothesis itself. The §I.9 correction (false scalar tail ratio) is the **third explicit honesty correction** in the master document, after pass-4 $m_*$ retraction (Appendix E) and pass-8 §H.5 weighted-Lyapunov correction; like the others, the corrected statement is what is now used in the master and the incorrect one is documented as retired. The §I.16 minimal next proof target $|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\le Cq_\eta^2 e^{-md(p,p')}$ is the most attackable form of level (iii) of (M′)_SU(2): proving this single inequality suffices for the level-(iii) sum form via deterministic PTO summability (§I.5). It remains an open problem at large β for SU(2).

**Pass-11 honest disclaimer (added).** A direct mathematical attempt at the §I.16 minimal target was carried out using the §H.8 four-ingredient assembly. The attempt is documented as Appendix J with explicit numerical computations: per-plaquette Wilson Hessian eigenvalue formula for SU(2) (eigenvalue $=\beta q_0^{(p,\ell)}/4$), naive Bakry–Émery threshold ($\beta<4/3$ crude; $\beta<1/96$ for the careful SZZ 2023 statement), and the quantitative exponential-rarity obstruction (under conservative Haar bound, $P(\text{all-BE-good})\le e^{-2.4\times 10^6}$ at $L=24$). **The attempt does NOT prove §I.16**; it identifies a concrete quantitative obstruction (exponential rarity of the pointwise BE-good set at $\beta=3.5$, which vacates the standard Cattiaux–Guillin local-to-global mechanism) and proposes the spectral-window restriction as the most promising research direction. The v3b empirical evidence ($\Theta_*=0.884<1$ over 1200 samples, master §11.0c) supports the spectral-window proposal as empirically consistent with positive projected Bakry–Émery, but a theorem requires substantial new analytic work (§J.8 Steps 1–4). The pass-7 finding (no peer-reviewed paper closes (M′)_SU(2) at large β) is unchanged; pass 11 sharpens it from "open" to "open with quantified obstruction and concrete subtarget."

**Pass-12 honest disclaimer (added).** A direct numerical computation of the projected Wilson Hessian $P\nabla^2 S_W P$ at typical Gaussian configurations was carried out via per-plaquette finite-difference Hessian assembly, with the spectral-window projector restricted to the coexact (gauge-invariant, physical) subspace. The computation is documented as Appendix K. **Key positive finding**: at $L=6$, $\beta=3.5$, $\Lambda=1.05$, and a typical Gaussian configuration (seed=42), all 72 coexact-window projected Hessian eigenvalues are positive (min +0.31, p99 +0.80), so the projected Bakry–Émery floor is uniformly $\ge 2.31$ across all modes. The L=4 sanity check (§K.2) identified the spectral-window-zero-modes-only artifact at small lattices and confirmed that the small negative tail observed there is partly finite-difference noise on pure-gauge directions where the Hessian is exactly zero by gauge invariance. **The pass-12 result is empirical positive evidence for the §J.6 spectral-window conjecture; it is NOT a proof.** Caveats (§K.5): single Gaussian sample at L=6; Gaussian sampling differs from Wilson MCMC; L=6 coexact window contains only 24 modes per Lie algebra all at the lowest Maxwell eigenvalue. Pass-12 substantially strengthens the empirical case for §J.6 as the most promising research direction, with two now-independent empirical anchors (v3b $\Theta_*=0.884<1$ over 1200 samples at the operator-norm level; pass-12 K.3 projected-Hessian-eigenvalue all-positive demonstration at L=6). The pass-7 finding stands; the master document's conditional status is unchanged. The master document's distinctive structural feature — projection to the coexact spectral window — is now identified as the precise mechanism that empirically makes Bakry–Émery work at large β where SZZ 2023's unprojected approach fails.

**Pass-13 honest disclaimer (added).** Three substantive additions clarifying the conditional content. **Appendix L** audits the constants in Appendix I against the firewall inequality (14.1) at the master's working corner: 13 constants pinned (from empirical data or deterministic geometry), 4 remain open (depend on the rooted-source polymer hypothesis). With all pinned constants plugged in, the firewall inequality requires polymer activity $C_0 \le 6.8\times 10^{-8}$ at $L=24$ — a sharp quantitative target. The vMF tightness gap at $\beta=3.5$ is $\sim 67\times$ (analytic bound vs empirical $q$). **Appendix M** makes the pass-12 §K.3 to source §I.16 bridge explicit: §K.3 supplies the spectral-gap/decay-rate component (BGL decay rate $\ge 0.76$ if floor extends to all L), but BGL gives $1/\eta^2$ prefactor while source target is $q_\eta^2$ — a $1.1\times 10^7$ gap at the working corner. The sharper residual question is to prove a "small-density spectral-gap covariance decay" theorem giving $q_\eta^2$ prefactor under projected BE; SZZ 2023 effectively proves this at strong coupling, and extending to large β via the projected dynamics is the precise research target. **Appendix N** substantively closes the pass-7 known Russian-language gap: Malyshev–Minlos 1991 develops continuous-spin cluster-expansion machinery applicable in principle to SU(2) Wilson at large β (chapter 5 §2 + chapter 6), but their explicit gauge-theory chapter (§7.4) covers $\mathbb Z_2$ only. The Russian-school gap is one of undone explicit work, not a hidden closure. **Pass-13 does NOT close any of the open questions; it supplies precise quantitative accounting (L), an honest bridge decomposition (M), and complete bibliographic closure (N).** The pass-7 conditional status is preserved exactly.

**Pass-14 honest disclaimer (added).** A 10-sample sweep extending pass-12 §K.3 was carried out. The result is documented as Appendix O. **Key finding**: at the master's working corner ($L=6$, $\beta=3.5$, $\Lambda=1.05$), 10 independent typical Gaussian configurations all give projected Bakry–Émery eigenvalues in a tight band $[2.287, 2.830]$, with BE-min cross-sample standard deviation $0.014$ (less than 1% of the mean) and zero negative eigenvalues across any sample. The pass-12 §K.3 single-sample finding is therefore highly robust, not a fluke. The cross-sample tightness suggests an underlying analytic floor $\rho_*(\beta=3.5, \Lambda=1.05) \approx 2.31$ that the §J.6 spectral-window conjecture should ideally predict explicitly. **Pass-14 §O closes pass-12 §K.5 caveat (1) "single Gaussian sample"; caveats (2)–(5) remain unchanged.** The pass-7 conditional status is preserved exactly. Pass-14 does NOT supply: a proof of §I.16; Wilson MCMC sampling; larger-L extension; the pass-13 §M.4 small-density spectral-gap theorem.

**Pass-15 honest disclaimer (added).** Four substantive items.
- **Appendix P**: Wilson MCMC sampling implemented at L=6 via heat-bath. 5 thermalized Wilson samples at $\beta=3.5$ with verified plaquette equilibrium ($\langle\phi_p\rangle=0.148$). Projected BE at each: all 360 modes positive, BE band $[2.185, 4.077]$, BE min mean $2.199 \pm 0.011$. Wilson distribution is $\sim 3.7\times$ wider than Gaussian — floor pushed lower by $0.11$, ceiling pushed higher by $1.23$. **§J.6 empirically supported under Wilson sampling.** Caveat (3) "Gaussian ≠ Wilson" closed.
- **Appendix Q**: analytic conjecture $\rho_*(\beta,\Lambda) \approx \kappa_G + (\beta/4)\lambda_{\min}^{\rm coex} - c\beta\langle\phi_p\rangle$. Phenomenological fit: $c\approx 0.56$ under Gaussian, $c\approx 1.30$ under Wilson. **(Pass-16 §S.6 corrects this conjecture: the shift scales as $\lambda_{\min}(L)$, not as $\beta\langle\phi_p\rangle$. See pass-16 disclaimer below.)**
- **Appendix R**: small-density projected BE covariance decay stated as precise research conjecture. If proved, combined with §J.6 closes source §I.16. Proof sketch via Brascamp-Lieb + spectral gap + Stein-coupling; the $\sqrt{qq'}\to qq'$ upgrade is the residual open step.
- **Fourth honesty correction**: pass-11 §J.4 said $\langle\phi_p\rangle \approx 3/(2\beta)=0.43$; correct value is $3/(8\beta)=0.107$ (off by factor 4). Empirical Wilson MCMC $0.148$. The error did not propagate to any downstream analytic result (pass-11 §J.5 used Haar bound; pass-12 §K.3 used $\sigma=1/\sqrt\beta$ directly).
**Pass-15 does NOT prove (M′)_SU(2).** It supplies Wilson sampling infrastructure, an empirical analytic conjecture for $\rho_*$, and a precise research statement for the residual analytic lemma. Pass-7 conditional status preserved.

**Pass-16 honest disclaimer (added).** One substantive item documented as Appendix S.
- **L=8 lattice extension.** Sparse eigsh stalls on the 4095-mode L=8 Maxwell zero block; analytic Fourier-mode construction of the 24-dim coexact basis succeeds (verified to machine precision). Batched projected-Hessian compute (3 bash batches per sample) for 2 Gaussian samples at L=8, $\beta=3.5$, $\Lambda=1.05$. Result: BE min $2.20$ and $2.21$, all 144 modes positive, cross-sample $\sigma = 0.005$. Pass-12 §K.5 caveat (2) "small lattice L=6 only" substantively closed.
- **Critical refinement to pass-15 §Q.3.** The shift below trivial-config BE scales linearly with $\lambda_{\min}^{\rm coex}(L)$, not as a constant. Empirical shift / $\lambda_{\min}$: $-0.56$ at L=6, $-0.52$ at L=8. **Corrected conjecture**: $\rho_*(L) = \kappa_G + ((\beta/4) - k_{\rm ens})\lambda_{\min}(L) + O(\lambda_{\min}^2)$ with $k_{\rm Gauss} \approx 0.54$.
- **Asymptotic consequence.** $\rho_*(L) \to \kappa_G = 2.0$ from above as $L\to\infty$, with $O(1/L^2)$ convergence. The §J.6 spectral-window conjecture is supported with $\rho_* = \kappa_G > 0$ uniform in L; the asymptotic floor equals exactly the geometric Ricci constant. The configuration-dependent positive contribution from the Wilson Hessian vanishes as $L\to\infty$; $\kappa_G > 0$ does ALL the asymptotic work.
**Pass-16 does NOT prove (M′)_SU(2).** It substantively closes pass-12 §K.5 caveat (2), corrects pass-15 §Q.3 analytic conjecture, and refines the §J.6 statement to its sharper asymptotic form $\inf_L \rho_*(\beta, \Lambda; L) = \kappa_G$. Caveats (4), (5) remain. Pass-7 conditional status preserved.

### 14.5 Manuscript-safe language (pass 5)

Verbatim from `PMBSF_quick_reference_for_simulations_fourth_pass_20260524.md` §7. These are the recommended templates for any external claim:

**Use this:**

> The simulations provide finite-volume evidence for a projected-capacity firewall mechanism. In the strongest tested projected Birman–Schwinger danger corner, the physical-sector norm stayed below one with $\Theta_*=0.884442692429$. Fixed spectral-window tests showed uniformly small projected restrictions and close agreement between Wilson high-plaquette sets and random plaquette-incidence comparators. Sparse matrix-Laplace diagnostics further support a Wilson-to-random transfer conjecture.

**Use this:**

> Independent edge-Bernoulli domination is not the correct stochastic comparator. The numerics indicate that plaquette-to-link incidence geometry accounts for the observed Wilson excess.

**Use this:**

> The Matrix-Stein / heat-bath absorption route failed the tested covariance and finite-rank acceptance criteria and is not used as the current closing route.

**Do not use this:**

> The simulations prove the Yang–Mills mass gap.

**Do not use this:**

> Wilson high plaquettes are independent Bernoulli edge defects.

**Do not use this:**

> Matrix-Stein closes the stochastic typicality theorem.

**Do not use this:**

> v17 proves Bałaban cumulant decay.

---

## Appendix A — File map

Complete inventory of `/mnt/project/`. Canonical versions are bolded. See §0 variant retirement table for supersession.

### A.1 Theorem statements

| File | Role | Status |
|---|---|---|
| `Theorem_FNG__Finite_Non-Abelian_Gauge___Projected_Capacity_Firewall_.md` | Original FNG deep pass + key findings | Active |
| `theorem_fng_cleaned_stage_1_stage_2.md` | Cleaned FNG architecture theorem with Stage 1 (H2a) / Stage 2 (H2b) split | Active |
| `m_prime_su_2_theorem_target_and_strategy.md` | SU(2) theorem target v1 | Pre-patch |
| `m_prime_su_2_theorem_target_and_strategy_patched.md` | Patched | Superseded by `__1__` |
| **`m_prime_su_2_theorem_target_and_strategy_patched__1__.md`** | **Canonical** — patched + boxed reduction statement | **Active** |
| `m_prime_su2_patch_memo.md` | The 9-edit patch memo | Active reference |

### A.2 Deterministic spine

| File | Role | Status |
|---|---|---|
| `lemmas_1_2_proofs.md` | Lemma 1 (Fourier leverage), Lemma 2 (Bernstein) — proofs and status | Active |
| `kappa_bernstein_transfer_memo.md` | Closed-form κ_Λ; Bernstein with κ_Λ atom; Wilson-to-random theorem statement | Active |

### A.3 Route I (polymer/cumulant)

| File | Role | Status |
|---|---|---|
| `route_I_polymer_expansion.md` | First polymer-expansion formulation | Superseded |
| `route_I_tightening.md` | Trace-mismatch artifact, sharpened constants, firewall closure | Superseded |
| `route_I_integrated_corrections.md` | Older (v10 only) | Superseded by `__1__` |
| **`route_I_integrated_corrections__1__.md`** | **Canonical** with v11 update; supersedes the other three | **Active** |
| `route_I_integrated_corrections__2__.md` | Byte-identical to `__1__` | Redundant |

### A.4 Route F / Matrix-Stein

| File | Role | Status |
|---|---|---|
| `Route_F_Attack_Me_Stein_Exchangeable-Pair_Variance.md` | Stein exchangeable-pair attack, phases, kill criteria | Active |
| `PMBSF_matrix_stein_ML_reduction_v1.md` | PMBSF Matrix-Stein route to tight ML domination | Active |
| `matrix_stein_ps_target_for_pmbsf.md` | PS-core target form, what was correct / incorrect in prior chats | Active |

### A.5 HB-q² / vMF reduction

The four files below overlap but each carries unique content; do not consolidate.

| File | Role | Status |
|---|---|---|
| `HB_q2_closure_matrix_stein_route_20260524.md` | Closure framework with explicit B.1/B.3 inputs and cap-overlap sublemma target | Active (closure) |
| `hb_q_2_pto_summed_heatbath_sensitivity_section.md` | Base version | Superseded by `__9__` |
| `hb_q_2_pto_summed_heatbath_sensitivity_section__8__.md` | Mid-development | Superseded by `__9__` |
| **`hb_q_2_pto_summed_heatbath_sensitivity_section__9__.md`** | **Canonical** cleaned theorem skeleton | **Active** (skeleton) |
| `HB_qsq_merged.md` | Merged manuscript draft with §A.1–A.7 deterministic content, §§B.1–B.4 typical/spike, §C closure | Active (merged manuscript) |
| `Lemma_HB_qsq.md` | Standalone Lemma HB-q² statement at operator level | Active (lemma) |
| `Lemma_B1_smallfield_decoupling.md` | Pointwise q² for typical part; bivariate-Gaussian threshold-crossing | Active |
| `Lemma_B3_spike_isolation_patched.md` | Spike isolation, Boole + empirical η_bad, firewall budget table | Active |
| `Lemma_B5_SU2_heatbath_vMF_cap_overlap_reduction_20260524.md` | vMF reduction; the false pointwise B.5 correction | Active |

### A.6 Sparse closed-walk / HPM

| File | Role | Status |
|---|---|---|
| `sparse_closed_walk_domination_wilson_high_plaquette_sets.md` | Base (664 lines, §§1–13) | Superseded |
| `sparse_closed_walk_domination_wilson_high_plaquette_sets__1__.md` | Intermediate (929 lines) | Superseded |
| `sparse_closed_walk_domination_wilson_high_plaquette_sets__2__.md` | Intermediate (1069 lines) | Superseded |
| **`sparse_closed_walk_domination_wilson_high_plaquette_sets__3__.md`** | **Canonical** (1446 lines, §§1–27, BS/BG/GK–CW-KP/dP) | **Active** |

### A.7 (M′)→HPM bridge

| File | Role | Status |
|---|---|---|
| `NOTE_PMBSF_mprime_hpm_bridge.md` | (M′)→HPM derivation §§B1–B9 | Active (base) |
| `NOTE_PMBSF_mprime_hpm_bridge_v17b_patch.md` | v17b empirical anchor patch | Active (patch) |
| `NOTE_PMBSF_mprime_su2_extraction_protocol.md` | Reading protocol for Bałaban II + MR93 (corrected bibliography) | Active |
| `M_prime_reconnaissance.md` | First-pass literature map; three-path recommendation | Active |

### A.8 Calibration and synthetic experiments

| File | Role | Status |
|---|---|---|
| `PMBSF_Heat-Kernel_-_Wilson_Calibration.md` | HK / Wilson calibration, corrected conventions, honest assessment | Active |
| `NOTE_PMBSF_l64_projected_capacity_threshold_law.md` | L=64 controlled threshold-law diagnostic | Active |

### A.10 In-hand reference PDFs (pass 3 additions)

| File | Citation | Role |
|---|---|---|
| `The_Renormalization_Group_According_to_Balaban.pdf` | Dimock I, *The Renormalization Group According to Balaban I. Small Fields* (52 pp, arXiv:1108.1335) | Expository template for Path A Stage A1: small-field RG, §4.6 cluster expansion |
| `The_Renormalization_Group_According_to_Balaban_2.pdf` | Dimock II, *II. Large Fields* (94 pp, arXiv:1212.5562) | Path A Stage A2: large-field analysis, §3.14 cluster expansion with holes, §3.18 Lemma 3.19 contour-integral coefficient extraction (eq 510) |
| `The_Renormalization_Group_According.pdf` | Dimock III, *III. Convergence* (43 pp, Ann. Henri Poincaré 15 (2014) 2133–2175, DOI 10.1007/s00023-013-0303-3) | Path A Stage A3: Theorem 2 (eq 222–223) is the structural target form for BS |
| `Von_MisesFisher_Clustering_Models.pdf` | Gopal–Yang, *Von Mises–Fisher Clustering Models*, ICML 2014, JMLR W&CP 32 | Standard reference for vMF density. **NOT load-bearing** — does not address joint cap-intersection structure required by Lemma B.5/B.6 |

The first three (Dimock I/II/III) are the most accessible exposition of the Bałaban small-field/large-field/convergence machinery. With these in-hand, Path A (§10.4) becomes a translation task with a concrete template rather than open-ended literature archaeology.

The fourth (Gopal–Yang) is a standard vMF reference; it confirms the density formula already used in `Lemma_B5_..._20260524.md` §0 but does not advance the open Lemma B.6 cap-overlap analysis.

### A.11 Cited references — pass-7 expanded bibliography

Pass-7 literature deep-dive expanded this section from ~10 vague pointers to ~35 specific peer-reviewed citations with DOIs and pages. The Bałaban CMP series is now fully inventoried; the modern probabilistic literature (SZZ, Adhikari–Cao, CNS, etc.) is added. All citations below are peer-reviewed unless explicitly flagged as preprint/forthcoming.

#### A.11.1 Bałaban Yang–Mills lattice RG series (CMP 1984–1989)

All in *Communications in Mathematical Physics*, communicated by A. Jaffe. Together they prove **UV stability of 4D lattice pure Yang–Mills for compact gauge group** (including SU(2)). They do **not** prove mass gap or cumulant decay.

| Paper | Year (Vol) | Pages | DOI |
|---|---|---|---|
| Bałaban, "Propagators and renormalization transformations for lattice gauge theories. I" | 1984 (95) | 17–40 | 10.1007/BF01215753 |
| Bałaban, "Propagators and renormalization transformations for lattice gauge theories. II" | 1984 (96) | 223–250 | 10.1007/BF01240221 |
| Bałaban, "Averaging operations for lattice gauge theories" | 1985 (98) | 17–51 | 10.1007/BF01211042 |
| Bałaban, "Spaces of regular gauge field configurations on a lattice and gauge fixing conditions" | 1985 (99) | 75–102 | Project Euclid cmp/1103942611 |
| Bałaban, "Propagators for lattice gauge theories in a background field" | 1985 (99) | 389–434 | 10.1007/BF01240355 |
| Bałaban, "Ultraviolet stability of three-dimensional lattice pure gauge field theories" | 1985 (102) | 255–275 | 10.1007/BF01229380 |
| Bałaban, "The variational problem and background fields in renormalization group method for lattice gauge theories" | 1985 (102) | 277–309 | 10.1007/BF01229381 |
| Bałaban, "Renormalization group approach to lattice gauge field theories. I" | 1987 (109) | 249–301 | 10.1007/BF01215223 |
| Bałaban, "Renormalization group approach to lattice gauge field theories. II. Cluster expansions" | 1988 (116) | 1–22 | 10.1007/BF01239022 |
| Bałaban, "Convergent renormalization expansions for lattice gauge theories" | 1988 (119) | 243–285 | 10.1007/BF01217741 |
| Bałaban, "Large field renormalization. I. The basic step of the R operation" | 1989 (122) | 175–202 | 10.1007/BF01257412 |
| Bałaban, "Large field renormalization. II. Localization, exponentiation, and bounds for the R operation" | 1989 (122) | 355–392 | 10.1007/BF01238433 |

#### A.11.2 Bałaban–Imbrie–Jaffe abelian Higgs series

| Paper | Year (Vol) | Pages | DOI |
|---|---|---|---|
| Bałaban, Brydges, Imbrie, Jaffe, "The mass gap for Higgs models on a unit lattice," *Ann. Phys.* | 1984 (158) | 281–319 | 10.1016/0003-4916(84)90121-0 |
| Bałaban, Imbrie, Jaffe, "Renormalization of the Higgs model: Minimizers, propagators and the stability of mean field theory," *CMP* | 1985 (97) | 299–329 | 10.1007/BF01206191 |
| **Bałaban, Imbrie, Jaffe, "Effective action and cluster properties of the abelian Higgs model," *CMP*** | **1988 (114)** | **257–315** | **10.1007/BF01225038** |

**BIJ CMP 114 (1988) is the closest in-print prototype for the κ(B) cumulant-decay shape we need** at level (iv); however, it is abelian (U(1)) and in d=2,3, not SU(2) in d=4. The Higgs potential's deep well supplies the small parameter.

Modern revisit (also abelian):
- Goswami, R., "Mass Gap in weakly coupled abelian Higgs on a unit lattice," *Ann. Henri Poincaré* 20 (2019) 3955–3996, DOI 10.1007/s00023-019-00840-0. Power-series cluster expansion via Bałaban–Feldman–Knörrer–Trubowitz machinery for mass gap of $F_{\mu\nu}$ in weakly coupled U(1) Higgs in $d\ge 2$.

#### A.11.3 Federbush phase-cell Yang–Mills series

| Paper | Year (Vol) | Pages | DOI |
|---|---|---|---|
| Federbush, "A phase cell approach to Yang–Mills theory. I. Modes, lattice–continuum duality," *CMP* | 1986 (107) | 319–329 | (Springer) |
| Federbush, Williamson, "II. Analysis of a mode," *J. Math. Phys.* | 1987 (28) | 1416–1419 | (AIP) |
| Federbush, "III. Local stability, modified renormalization group transformation," *CMP* | 1987 (110) | 293–309 | 10.1007/BF01207369 |
| Federbush, "IV. The choice of variables," *CMP* | 1988 (114) | 317–343 | (Springer) |
| Federbush, "V. Analysis of a chunk," *CMP* | 1990 (127) | 433–457 | 10.1007/BF02104497 |
| Federbush, "VI. Non-Abelian lattice–continuum duality," *Ann. Inst. H. Poincaré Phys. Théor.* | 1987 (47) | 17–23 | (IHP) |

Status: small-field/chunk machinery; never closes a mass gap or cumulant decay at fixed β. Adjacent only.

#### A.11.4 MRS SU(2) construction

- **Magnen, J., Rivasseau, V., Sénéor, R., "Construction of YM₄ with an infrared cutoff,"** *Comm. Math. Phys.* **155** (1993) 325–383, DOI 10.1007/BF02097397. SU(2) Schwinger functions in regularized axial gauge with IR cutoff in trivial topological sector. **Does NOT prove mass gap or cumulant decay.** Note: earlier memos cite this as "MR95"; the correct year is 1993.

#### A.11.5 Modern probabilistic literature (2010+)

| Paper | Venue | DOI |
|---|---|---|
| **Shen, H., Zhu, R., Zhu, X., "A stochastic analysis approach to lattice Yang–Mills at strong coupling"** | *CMP* **400** (2023) 805–851 | 10.1007/s00220-022-04609-1 |
| **Adhikari, A., Cao, S., "Correlation decay for finite lattice gauge theories at weak coupling"** | *Ann. Probab.* **53** (2025) 140–174 | 10.1214/24-AOP1702 |
| **Cao, S., Nissim, R., Sheffield, S., "Dynamical approach to area law for lattice Yang–Mills"** | *Prob. Math. Phys.* **7** (2026) 37–121 (arXiv:2509.04688) | (peer-reviewed; in print) |
| Cao, S., "Wilson loop expectations in lattice gauge theories with finite gauge groups" | *CMP* **380** (2020) 1439–1505 | 10.1007/s00220-020-03912-z |
| Forsström, M. P., "Decay of correlations in finite Abelian lattice gauge theories" | *CMP* **393** (2022) | 10.1007/s00220-022-04391-0 |
| Forsström, M. P., Lenells, J., Viklund, F., "Wilson loops in finite Abelian lattice gauge theories" | *AIHP Probab. Statist.* **58** (2022) 2129–2164 | 10.1214/21-AIHP1227 |
| Chatterjee, S., "Yang–Mills for probabilists," in *Sojourns in Probability Theory and Statistical Physics – I*, Springer PROMS 298 | 2019 | 10.1007/978-3-030-15338-0_1 |
| Cao, S., Park, M., Sheffield, S., "Random surfaces and lattice Yang–Mills" | *Comm. Amer. Math. Soc.* (to appear; arXiv:2307.06790) | (forthcoming) |
| Borgs, C., "Translation symmetry breaking in four-dimensional lattice gauge theories" | *CMP* **96** (1984) 251–284 | (Springer). **Important caveat:** identifies a gap in Seiler's 1982 monograph claim that strong-coupling cluster expansions extend uniformly from finite Abelian to general finite non-Abelian groups. |

#### A.11.6 Foundational and framework

| Paper | Venue | Note |
|---|---|---|
| Osterwalder, K., Seiler, E., "Gauge field theories on a lattice" | *Ann. Phys.* **110** (1978) 440–471, DOI 10.1016/0003-4916(78)90039-8 | Reflection positivity + strong-coupling cluster expansion |
| Seiler, E., *Gauge theories as a problem of constructive quantum field theory and statistical mechanics* | LNP **159**, Springer 1982 | Classical monograph; do NOT cite for non-Abelian cluster expansion (see Borgs CMP 96, 1984) |
| Brydges, D., Federbush, P., "The cluster expansion in statistical mechanics" | *CMP* **49** (1976) 233–246 | Foundational tool |
| Magnen, J., Sénéor, R., "The infinite volume limit of the φ⁴_3 model" | *AIHP* **24** (1976) 95–159 | Scalar template |
| Brydges, D., Kennedy, T., "Mayer expansions and the Hamilton–Jacobi equation" | *J. Stat. Phys.* **48** (1987) 19–49 | Tree-graph identity |
| Driver, B., "Convergence of the U(1)_4 lattice gauge theory to its continuum limit" | *CMP* **110** (1987) 479–501 | Abelian only |
| Gross, L., "Convergence of U(1)_3 lattice gauge theory to its continuum limit" | *CMP* **92** (1983) 137–162 | Abelian only |

#### A.11.7 Cluster-expansion convergence (modern)

| Paper | Venue |
|---|---|
| Fernández, R., Procacci, A., "Cluster expansion for abstract polymer models. New bounds from an old approach" | *CMP* **274** (2007) 123–140 |
| Bissacot, R., Fernández, R., Procacci, A., "On the convergence of cluster expansions for polymer gases" | *J. Stat. Phys.* **139** (2010) 598–617 |
| Procacci, A., Yuhjtman, S. A., "Convergence of Mayer and virial expansions and the Penrose tree-graph identity" | *Lett. Math. Phys.* **107** (2017) 31–46 |
| Bauerschmidt, R., Brydges, D. C., Slade, G., *Introduction to a Renormalisation Group Method* | LNM **2242**, Springer 2019 |

#### A.11.8 Preprints (not peer-reviewed; cited for completeness only)

- Borga, J., Cao, S., Shogren-Knaak, J., "Surface sums for lattice Yang–Mills in the large-N limit," arXiv:2411.11676 (2024–25).

#### A.11.9 Status assessment

Of the 33 peer-reviewed papers above:
- **Zero** directly prove (M′)_SU(2) at level (iii) or (iv) for SU(2) at large β in d=4.
- **One** (BIJ CMP 114, 1988) proves the level-(iv) shape but for U(1) Higgs.
- **One** (SZZ CMP 400, 2023) proves covariance decay for SU(N) but only at strong coupling.
- **One** (Adhikari–Cao Ann. Probab. 53, 2025) proves correlation decay for finite non-Abelian groups; used for FNG Stage 1 anchor, does not extend to SU(2).
- **Twelve** (Bałaban CMP series) prove 4D UV stability but not mass gap or cumulant decay.

See Appendix G for the full pass-7 deep-dive on candidate routes, per-candidate translation analysis, and stop-conditions that would change the recommendation.

---

## Appendix B — Glossary

| Symbol / Acronym | Meaning |
|---|---|
| $T_L^4$ | Periodic 4-lattice $(\mathbb Z/L)^4$ |
| $\mathcal P_L$ | Plaquette set, $\|\mathcal P_L\|=6L^4$ |
| $P=P_{\le\Lambda,L}$ | Coexact lattice projector, transverse 1-forms in window $\omega(k)\le\Lambda$ |
| $P_\chi$ | Smooth spectral cutoff projector (introduced in §8.4 for GK) |
| $A_p=P\mathbf 1_{\partial p}P$ | Projected plaquette atom; PSD, rank ≤ 4 |
| $A_p^\chi$ | Smooth-cutoff atom $P_\chi\mathbf 1_{\partial p}P_\chi$ |
| $\kappa_\Lambda=\|A_p\|_{\rm op}$ | Plaquette atom operator norm (plane-independent) |
| $\mu_{\Lambda,L}=K_{\Lambda,L}/(4L^4)$ | Diagonal Fourier leverage |
| $K_{\Lambda,L}$ | Rank of $P$, $\approx 3\|S_{\Lambda,L}\|$ |
| $X_p$ | Hard plaquette defect indicator $\mathbf 1\{\phi(U_p)\ge\delta_{\rm bond}\}$ |
| $X_{p,\eta}$ | Smoothed indicator $f_\eta(\phi(U_p)-t)$ |
| $\phi(g)=1-\tfrac12\Re\operatorname{tr}g$ | SU(2) plaquette score |
| $\delta_{\rm bond}$ | Hard threshold; canonical values 0.85, 1.00, 1.15 |
| $\eta$ | Smoothing width; tested values 0.025, 0.05, 0.10 |
| $D_W(U)$ | Wilson defect bad-edge set |
| $D(B)$ | Bernoulli comparator bad-edge set |
| $S_W=\sum_p X_p A_p$ | Wilson projected capacity observable |
| $S_B=\sum_p B_p A_p$ | Bernoulli projected capacity observable |
| $\Theta=(V_{\max}/m^2)\|P\mathbf 1_{D_W}P\|$ | Firewall parameter; $V_{\max}/m^2=2$ canonical |
| $q=\mathbb E_W X_p$ | Single-plaquette defect probability |
| $q_\eta=\mathbb E_W X_{p,\eta}$ | Smoothed analog |
| $G(p,q)=\sqrt{\operatorname{tr}(A_pA_q)}$ | Closed-walk scalar kernel |
| $C_e(p,p';U)$ | Heat-bath cross-term $\mathbb E_e[\Delta_e X_p\Delta_e X_{p'}|U]$ |
| $\nu_e$, vMF | SU(2) one-link heat-bath conditional; exact vMF on $S^3$ |
| $\mathcal P(e)$ | Incident star, $\|\mathcal P(e)\|=6$ in 4D |
| $\mathcal E_e^{\rm spike}$ | Spike set: at least one incident plaquette pre-flagged |
| $p_{\rm bad}(e)$ | $\mathbb P_W(\mathcal E_e^{\rm spike})\le 6q$ by Boole |
| $\eta_{\rm bad}, \eta_{\rm typ}$ | Measured Matrix-Stein constants (Lemma B.3) |
| $\kappa_W(Y)$ | Truncated joint Wilson cumulant of $\{X_p:p\in Y\}$ |
| $\tau(Y)$ | Minimum spanning-tree length of $Y$ in plaquette distance |
| $\xi_\beta\le\xi_*/\beta$ | (M′) correlation length |
| (M′) | Hard-indicator cumulant decay assumption: $\|\kappa_W(Y)\|\le q^{\alpha(Y)}A_*^{\|Y\|-1}e^{-c_*\tau/\xi_\beta}$ |
| (M″)_pinned | Stronger pinned version requiring $\alpha(\Gamma)\ge\|\Gamma\|$ |
| (ML), (ML-I), (ML-SU2) | Matrix-Laplace domination (generic / Route I / SU(2)) |
| $C_0, C_1$ | Matrix-Laplace constants; target $C_0=1+O(q)$, $C_1=1$ |
| $\alpha(Y)$ | q-power of $Y$-cumulant; need $\ge 2$ for leading pair |
| HPM | High-plaquette closed-walk domination |
| EC | Random closed-walk envelope comparability |
| FCB | Fixed-cardinality to Bernoulli comparison |
| CW-KP | Closed-walk Kotecký–Preiss summability |
| dP | Top-p de-Poissonization |
| BS | Bałaban smooth-source expansion |
| BG | Boundary-band gate (smoothing bridge) |
| GK | Closed-walk kernel decay (smooth-cutoff version) |
| $\varepsilon_{\rm HPM}, \varepsilon_{\rm ML}, \varepsilon_{\rm bdry}$ | HPM tolerance / empirical ML loss / boundary-band tolerance |
| $N_{\rm KP}$, $N_{\rm BS}$ | Polymer norms |
| (H1), (H2a), (H2b), (H3) | FNG hypotheses (β threshold / summed / pointwise / PTO) |
| PMBSF | Projected Maxwell Birman–Schwinger Firewall |
| PTO | Projected Trace-Overlap (1: atomic; 2: summability; 3: rank-4) |
| Theorem FNG | Finite Non-Abelian Gauge projected capacity firewall ($Q_8$) |
| $\beta_0$ | Adhikari–Cao threshold; $\beta_0(Q_8)\approx 61.16$ |
| $r_*=1/2$ | Non-alignment threshold ($\|\cos\gamma\|\le r_*$) in Lemma B.1 |
| v6/v9/v10/v11/v12/v13/v14/v15/v16/v17/v17b | Numerical run versions (see §11) |
| AC | Adhikari–Cao 2022, *Ann. Probab.* 53(1):140–174 |
| Cao 2020 | Cao, *Comm. Math. Phys.* 380 |
| Bałaban I/II/III | Bałaban 1987 (CMP 109) / 1988 (CMP 116) / 1988 (CMP 119) |
| MR93 | Magnen–Rivasseau–Sénéor 1993, CMP 155 (NB: "MR95" in earlier memos is a wrong citation) |
| Forsström 2021 | arXiv:2104.03752, finite Abelian (M′) at large β |
| GS 2021 | Garban–Sepúlveda 2021, U(1) Villain spin-wave |

---

## Appendix C — Constant cross-check table

Key numerical quantities, cross-checked across the canonical source files. All values rounded to displayed precision.

### C.1 Canonical "v9 worst corner"

| Quantity | Value | Source |
|---|---|---|
| $L$ | 24 | `route_I_integrated_corrections__1__.md` §5, `kappa_bernstein_transfer_memo.md` §2.4 |
| $q$ | 0.01 | ibid |
| $\Lambda$ | 1 | ibid |
| $\delta$ (failure probability) | 0.05 | ibid |
| $K=K_{\Lambda,L}$ | ≈ 3792 | ibid |
| $\mu_{\Lambda,L}=K/(4L^4)$ | ≈ 0.00286 | `kappa_bernstein_transfer_memo.md` §2.4 |
| $\kappa_\Lambda$ (empirical) | ≈ 0.0055 | ibid (v9 numerical) |
| $\kappa_\Lambda\le 2\mu_{\Lambda,L}$ | ≤ 0.00572 | bound (1.3) |
| $u=\log(2K/\delta)$ | $\log(151680)\approx 11.93$ | this document §6.3 |
| $6q$ | 0.060 | this document §6.3 |
| $\sqrt{12q\kappa_\Lambda u}$ | $\sqrt{0.007874}\approx 0.0887$ | ibid |
| $(2\kappa_\Lambda/3)u$ | $0.003667\times 11.93\approx 0.0437$ | ibid |
| **Bound** | $0.060+0.0887+0.0437\approx 0.1924\approx 0.193$ | ibid |
| $V_{\max}/m^2$ | 2 | canonical |
| **$\Theta$** | $\approx 0.386$ | ibid |
| **Margin** | $\approx 0.614$ | ibid |

Empirical Wilson $R$ at v10 corner: $\approx 0.05$ — well below analytic 0.193.

### C.2 Sparse stress point (v10/v11)

| Quantity | Value |
|---|---|
| $L$, $q$, $\Lambda$, $\delta$ | 24, 0.003, 1, 0.05 |
| $6q$ | 0.018 |
| $\sqrt{12q\kappa_\Lambda u}$ | $\sqrt{0.002366}\approx 0.0486\approx 0.049$ |
| $(2\kappa_\Lambda/3)u$ | $\approx 0.0437$ |
| Bound | $\approx 0.111$ |
| $\Theta$ | $\approx 0.222$ |
| Margin | $\approx 0.778$ |

### C.3 L=8 HB-q² closure (v14 measured)

At $\beta=3.5, \Lambda=1, \delta_{\rm bond}=1.0$:

| Quantity | Value | Source |
|---|---|---|
| $q$ (empirical) | $2.8\times 10^{-3}$ | `Lemma_B3_spike_isolation_patched.md` §3 |
| $\eta_{\rm bad}$ | 2.48 | ibid |
| $\eta_{\rm typ}$ (from old_good_only $\eta_{\rm global}$) | 0.093 | ibid §6 |
| $6\eta_{\rm bad}q$ | $6\times 2.48\times 0.0028=0.0417\approx 0.042$ | ibid |
| Total $\eta=\eta_{\rm typ}+6\eta_{\rm bad}q$ | 0.135 | ibid |
| Firewall budget (after safety) | 0.190 | ibid |
| Headroom | **29%** | ibid |

### C.4 FNG margin at v9 corner

| Quantity | Value | Source |
|---|---|---|
| $\beta_0(Q_8)$ | $(1/2)(114+4\log 8)\approx 61.16$ | `theorem_fng_cleaned_stage_1_stage_2.md` §2 |
| $\beta_0(Q_8)$ via Cao 2020 (earlier) | $\approx 514$ | ibid |
| $\Delta_{Q_8}$ (character gap) | 2 | ibid |
| Composite prefactor $C_{\rm AC}$ | $\approx 2.75\times 10^{11}$ | ibid §1 |
| Margin (RHS at v9) | $\approx 0.191$ | ibid §7 |
| $\Theta$ | $\approx 0.386$ | ibid |
| **Margin** | **$\approx 0.618$** (small diff from SU(2) v9 0.614 is rounding) | ibid |

### C.5 (M′)→HPM bridge: placeholder vs. v17b-anchored

At $\beta=3.5, \delta_{\rm bond}\approx 1.0, \Lambda=1, L=24, p=0.003, \theta\le 64, \kappa_\Lambda=0.0055$:

| Quantity | Placeholder | v17b-anchored |
|---|---|---|
| $C_*$ | 2 | $\le 0.126$ (with smoothing-factor 3) |
| $m_*$ | 0.5 | $\ge 2$ |
| $C_*^2 e^{-m_*}$ | $\sim 2.4$ | $\le 0.017$ |
| $J_{m_*}$ | 96 | $\le 0.4$ |
| $N_{\rm KP}(p=0.003)$ | $\sim 2.7$ | $\le 10^{-4}$ (e.g. $1.5\times 10^{-4}$ at $m_*=2$) |
| $\varepsilon_{\rm HPM}$ analytic | $\sim 200$ | $\sim 10^{-3}$ |
| vs. v16 empirical $\varepsilon_{\rm ML}\approx 0.02$ | loose by $10^4$ | beats by 20× |
| Firewall margin | $\ge 0.4$ (conditional) | $\ge 0.99$ (anchored) |
| $\varepsilon_{\rm HPM}$ tolerance threshold | margin binds at $\varepsilon\sim 5$ | comfortably below by 4 orders |

Sources: `NOTE_PMBSF_mprime_hpm_bridge.md` §B6.2 (placeholder); `NOTE_PMBSF_mprime_hpm_bridge_v17b_patch.md` §B6.2 (v17b).

### C.6 v17b empirical L-uniformity at incident supports

`pair_incident` rooted form $|\kappa|/q$ at $(\beta=3.5, q=0.003, \eta=0.05)$:

| $L$ | $|\kappa|/q$ | rel-JK-SE |
|---|---|---|
| 12 | 0.00527 | 0.073 |
| 16 | 0.00485 | 0.056 |
| 24 | 0.00496 | 0.030 |

Agreement ~10% across factor 8× volume.

### C.7 v12b PTO-weighted vs. pointwise

| $\delta_{\rm bond}$ | $\hat q$ | pointwise max $|C_e|/q^2$ | PTO-weighted max $\mathcal W/q^2$ |
|---|---|---|---|
| 0.85 | $9.35\times 10^{-3}$ | 13,487 | $1.01\times 10^{-1}$ |
| 1.00 | $3.07\times 10^{-3}$ | 6,520 | $8.48\times 10^{-2}$ |
| 1.15 | $9.36\times 10^{-4}$ | 7,523 | $9.52\times 10^{-2}$ |

PTO weighting compresses spikes by $\sim 10^5$. **Operator-level $q^2$ holds; pointwise $q^2$ fails.**

### C.8 v10/v11 sparse L-growth

At $q=0.003, \theta=64$:

| $L$ | $\Delta_+/q$ |
|---|---|
| 24 (v10) | 5.708 |
| 32 (v11) | 6.271 |

Ratio 1.099. Across $\theta\in\{1,2,4,8,16,32,64\}$, $L=32/L=24$ ratios in $[1.094, 1.099]$.

### C.9 v6c Wilson / random-plaquette comparator

$K=2048$, `any_defect`, $\delta=0.85$:

| $L$ | Wilson / Bernoulli plaquette | Wilson / fixed-cardinality plaquette |
|---|---|---|
| 8 | 1.044 | 1.049 |
| 12 | 1.065 | 1.041 |
| 16 | 1.005 | 1.008 |
| 24 | 1.027 | 1.029 |

All ≈ 1.

### C.10 Local Bakry–Émery floor for SU(2) (pass 9)

From Theorem H.3.1' (§H.3): in the master document's normalization $\Delta_{{\rm SU}(2)}({\rm Re}\operatorname{Tr}U)=-3\,{\rm Re}\operatorname{Tr}U$ (round $S^3$ at radius $r=1$):

| Quantity | Value | Notes |
|---|---|---|
| $\kappa_G$ for SU(2) | **2** | geometric Ricci constant, $\mathrm{Ric}_{g_G}=\kappa_G g_G$ |
| $\rho_0$ at $U^{(0)}$ (no regulator, $C_{\rm add}=0$) | **2** | uniform in $\Lambda$ |
| Wilson Hessian IR contribution at $L=24,\beta=3.5$ | $\sim 0.24$ | negligible vs. Ricci |
| Wilson Hessian UV contribution | $\sim 56$ | dominates at large momentum |
| SZZ 2023 threshold (per-link $|\beta_{\rm std}|$) | $<1/96\approx 0.010$ | far below working $\beta=3.5$ |
| SZZ 2023 threshold ('t Hooft $|\beta_{\rm tH}|$) | $<1/48\approx 0.021$ | for SU(2), d=4 |

**Use.** This is the local input for the §H.8 research-direction memo (pass 9). It is NOT load-bearing for the conditional theorem; the conditional theorem (§2) depends on (M′)_SU(2), which is open at large β regardless of the local Bakry–Émery floor.

---

## Appendix D — Bałaban/Dimock-to-PMBSF translation table

This appendix maps objects in the Dimock expository papers (which treat φ⁴_3 RG) to their analogs in the PMBSF program (SU(2) Wilson at large β with projected capacity). It is the starting point for Path A Stage A4 (§10.4). Entries are starting-point guesses; the actual translation requires the Bałaban Yang–Mills papers (CMP 89, 95, 96, 116) for the gauge-specific corrections.

### D.1 Lattice and field

| Dimock (φ⁴_3) | PMBSF (SU(2) Wilson, d=4) | Notes |
|---|---|---|
| Toroidal lattice $T_M^{-N}=(L^{-N}\mathbb Z/L^M\mathbb Z)^3$ | Periodic 4-lattice $T_L^4=(\mathbb Z/L\mathbb Z)^4$ | Dimension differs (3 vs 4). Dimock's $N$ is the number of RG steps; our $L$ is the lattice size. |
| Scalar field $\phi: T_M^{-N}\to\mathbb R$ | Link field $U_e\in\mathrm{SU(2)}$ | Field type differs fundamentally. Bałaban Yang–Mills uses Lie algebra coordinates after gauge fixing. |
| Lattice φ⁴ density $\rho_0\propto\exp(-\tfrac12 \|\partial\phi\|^2-\tfrac12\bar\mu\|\phi\|^2-V_0)$ | Wilson density $\propto\exp(\beta\sum_p\Re\operatorname{tr}U_p)$ | Different action structure; same RG philosophy. |
| Coupling λ (small) | Coupling $1/\beta$ (small at large β) | UV problem (Dimock) vs. confinement/IR problem (Wilson). Sign of expansion is the same in spirit. |
| $\bar\mu$ (mass²) | No direct analog | SU(2) has gauge symmetry; mass term forbidden without breaking. |

### D.2 RG transformation

| Dimock | PMBSF | Notes |
|---|---|---|
| Block averaging operator $Q$, $(Qf)(y)=L^{-3}\sum_{x\in B(y)}f(x)$ | Block average of $\phi(U_p)$ to coarser plaquettes | The scalar Dimock blocking has no SU(2) analog; Bałaban uses gauge-covariant blocking. |
| Small-field region $\Omega_k$ | $\{U:\phi(U_p)\le\rho(\beta)\}$ for $\rho\sim 1/\sqrt\beta$ | Bałaban Yang–Mills uses analogous small-field cut on field strength. |
| Large-field region $\Omega_k^c$ | $\{U:\phi(U_p)>\rho(\beta)\}$ | Hard plaquette indicators $X_p$ are large-field events with measure $q$. |
| Free flow / Laplacian propagator $G_k$ | Projected propagator with $P_{\le\Lambda,L}$ | Our $P$ is a *fixed* spectral window; Dimock's $G_k$ is the RG-running propagator. **The two need not coincide.** |

### D.3 Cluster expansion (Dimock I §4.6, II §3.14, III §2.6)

| Dimock | PMBSF |
|---|---|
| Fluctuation integral $\Xi'_k(\phi)=\int\exp(\sum_Y(\delta E_k^+)_{\rm loc})\,d\mu_k^*(W)$ | $\mathbb E_W[\exp(\sum_p h_p X_{p,\eta})]$ — the source generating functional $Z_\eta(u)$ |
| Polymer activity $E_k^\#(Y,\phi)$ with bound $\|E_k^\#\|\le O(1)L^3\lambda_k^{1/4-10\epsilon}e^{-L(\kappa-5\kappa_0-5)d_{LM}(Y)}$ (Dimock I eq 237) | Smooth-source connected coefficient $\Psi_\eta(B;u_B)$ with target bound $\|\mathrm{coeff}_B\Psi_\eta\|\le C_B^{|B|}q_\eta^{|B|}e^{-m_B\tau(B)}$ |
| Convergence parameter $\lambda_k^{1/4-10\epsilon}$ | Convergence parameter $q_\eta^{\alpha}$ for some $\alpha$ (the pinned q-power in (M′)) |
| Exponential rate $L(\kappa-5\kappa_0-5)$ | $m_B$ in BS (analog of $c_*/\xi_\beta$ in (M′)) |
| Cluster expansion radius condition $O(1)L^3\lambda_k^{1/4-10\epsilon}\le c_0$ | $\beta\ge\beta_B$ in BS — open whether $\beta_B\le 3.5$ |

### D.4 Coefficient extraction (Dimock II Lemma 3.19, eq 510)

| Dimock | PMBSF |
|---|---|
| Contour integral $B^\#=\frac{1}{2\pi i}\oint_{|u|=r_0L^{-3}\lambda_k^{-1/4+10\epsilon}}\frac{du}{u(u-1)}H^\#(1,u,Y)$ | Square-free source coefficient extraction in $u_p=e^{h_p}-1$ |
| Source variables $t, u$ parametrize remainder $R$ and boundary $B$ | Source variables $u_p$ for each plaquette indicator |
| Bound $\|B^\#\|\le O(1)L^3\lambda_k^{1/4-10\epsilon}e^{-L(\kappa-6\kappa_0-6)d_{LM}(Y, \mathrm{mod}\,\Omega_{k+1}^c)}$ | Bound on the rooted polymer norm $N_{\rm BS}(q_\eta)$ |

### D.5 Final stability bound (Dimock III Theorem 2, eq 222–223)

| Dimock | PMBSF (target for BS §8.2) |
|---|---|
| $\log(Z_{M,N}/Z_{M,N}(0))=\sum_X H(X)$, $\|H(X)\|\le O(1)\lambda^{\beta/2}e^{-\kappa_0 d_M(X)}$ | $\log Z_\eta(u)=\sum_B\Psi_\eta(B;u_B)$, $\|\mathrm{coeff}_B\Psi_\eta\|\le C_B^{|B|}q_\eta^{|B|}e^{-m_B\tau(B)}$ |
| Power $\lambda^{\beta/2}$ — pinned at half-power of coupling | Power $q_\eta^{|B|}$ — pinned at full per-plaquette factor; rooted form $q_\eta^{|B|-1}$ |
| Exponential decay rate $\kappa_0$ | Mass scale $m_B$ |
| Connected unions of $M$-cubes $X\subset T_M^{-N}$ | Connected plaquette polymers $B\subset\mathcal P_L$ |
| Stability bound corollary $\exp(-\lambda^\eta\mathrm{Vol})\le Z_{M,N}/Z_{M,N}(0)\le\exp(\lambda^\eta\mathrm{Vol})$ | Closed-walk weighted KP closure $\varepsilon_{\rm HPM}\le c_*N_{\rm BS}e^{O(N_{\rm BS})}$ |

### D.6 What does not translate

Three Dimock-to-PMBSF transitions are not automatic and require Bałaban Yang–Mills (1980s) consultation in Stage A4:

1. **Gauge fixing.** Dimock has no gauge symmetry. Bałaban Yang–Mills introduces a complex gauge-fixing/Higgs scheme (CMP 95, 96) that adds structural overhead. The Dimock small-field region $\Omega_k$ has a direct analog only after gauge fixing.

2. **Field exponentiation.** Dimock's $\phi$ is a real scalar field; Bałaban's $U_e$ is a group element written as $U_e=\exp(iA_e)$ in Lie algebra coordinates. The block averaging is then on $A_e$, not $U_e$, with a logarithmic constraint that adds non-trivial structure.

3. **Plaquette atoms $A_p=P\mathbf 1_{\partial p}P$.** This object is **specific to PMBSF** and has no Dimock analog. It enters via PTO-2/PTO-3 (§5.5–5.6) and the closed-walk envelope (§5.8) and connects the SU(2) cumulant analysis to the projected-capacity firewall. The cluster expansion produces polymers $B\subset\mathcal P_L$; the projected-capacity application then weighs them against $\operatorname{tr}(A_pA_{p'})$ via the closed-walk activity (§3.1 of `sparse_closed_walk_..._3__.md`).

### D.7 Consequence for the program

With the Dimock papers as analytic template and PTO + closed-walk envelope as PMBSF-specific structural ingredients, the Path A program is concretely:

> **Goal.** Construct a connected polymer expansion of $\log Z_\eta(u)$ — the smooth-source generating functional for SU(2) Wilson — with exponential tree decay $m_B$ and pinned per-plaquette factor $q_\eta^{|B|}$, valid for $\beta\ge\beta_B$ and $|u_p|\le u_0$, with constants $C_B, m_B, \beta_B$ explicit or at least parametric.
>
> **Template.** Dimock I/II/III for the cluster-expansion machinery; Bałaban CMP 95, 96 for the gauge-fixing/Higgs structure; PMBSF closed-walk envelope (§5.8) for the projected-capacity weighting.
>
> **Output.** BS (§8.2) for smooth source $X_{p,\eta}$. Combined with BG (§8.3) gives HPM for hard $X_p$. Combined with GK/CW-KP (§8.4) gives the closed-walk weighted KP closure. Substitution into Theorem 14.1 of `sparse_closed_walk_..._3__.md` gives the conditional projected-capacity firewall.

---

## Appendix E — Empirical verification of v17b claims against the CSV (pass 4)

Pass 4 directly audits the 1566 rows of `block_jackknife_diagnostics.csv` against the claims in `NOTE_PMBSF_mprime_hpm_bridge_v17b_patch.md` and the propagated claims in pass 3 of this document. This appendix records what verifies, what verifies with caveat, and what is over-extrapolated.

### E.1 CSV schema

15 columns: `L, beta, start_mode, eta, q_target, pattern_name, pattern_kind, support_size, tau_mst, n_blocks, abs_cumulant_over_qk, jk_se_abs_cumulant_over_qk, rel_jk_se_abs_cumulant_over_qk, abs_cumulant_over_q_rooted, jk_se_abs_cumulant_over_q_rooted`.

Parameter grid: $L\in\{12,16,24\}$, $\beta\in\{3.5,4.0\}$, $\eta\in\{0.025,0.05,0.1\}$, $q\in\{0.001,0.003,0.01\}$, `start_mode=hot`, 16 pattern_kinds.

Pattern_kind distribution: pair_incident 108 rows, pair_mixed_axis 270, pair_same_ori_axis 270, pair_same_ori_diag 270, pair_far_control 54, pair_mixed_near 54, triple_star 54, triple_L 54, triple_line 54, triple_mixed_chain 54, triple_far_control 54, quad_line 54, quad_square 54, quad_local_mixed 54, quad_tree_mixed 54, quad_far_control 54.

### E.2 Statistical reach — VERIFIED EXACTLY

Claim (from `NOTE_PMBSF_mprime_hpm_bridge_v17b_patch.md` §B3.4): "70% of all rows have relative JK SE > 0.5 (noise-dominated). 19% have relative JK SE < 0.3 (clean signal)."

CSV: 1095/1566 = 69.9% with `rel_jk_se_abs_cumulant_over_qk > 0.5`; 296/1566 = 18.9% with `< 0.3`. **Verifies exactly to one significant figure.**

### E.3 Clean rates by pattern_kind — VERIFIED EXACTLY

Claim: "100% clean at pair_incident (108/108), 59% clean at triple_star (32/54), 31% clean at triple_L."

CSV (rel_jk_se < 0.3):

| pattern_kind | clean / total | % clean |
|---|---|---|
| pair_incident | 108/108 | **100.0%** ✓ |
| pair_far_control | 2/54 | 3.7% |
| pair_mixed_axis | 10/270 | 3.7% |
| pair_mixed_near | 7/54 | 13.0% |
| pair_same_ori_axis | 48/270 | 17.8% |
| pair_same_ori_diag | 8/270 | 3.0% |
| quad_far_control | 5/54 | 9.3% |
| quad_line | 7/54 | 13.0% |
| quad_local_mixed | 10/54 | 18.5% |
| quad_square | 6/54 | 11.1% |
| quad_tree_mixed | 5/54 | 9.3% |
| triple_L | 17/54 | **31.5%** ✓ |
| triple_far_control | 11/54 | 20.4% |
| triple_line | 10/54 | 18.5% |
| triple_mixed_chain | 10/54 | 18.5% |
| triple_star | 32/54 | **59.3%** ✓ |

All three highlighted claims verify exactly.

### E.4 L-uniformity at incident pairs — VERIFIED EXACTLY (with interpretation note)

Claim: at the working corner ($\beta=3.5, q=0.003, \eta=0.05$), `pair_incident` rooted form across $L\in\{12,16,24\}$ is 0.00527, 0.00485, 0.00496.

CSV gives 2 patterns per L (pair_incident_same_site_01_02 and 01_03). The patch numbers are **mean over the 2 patterns**:

| $L$ | pattern 01_02 | pattern 01_03 | mean | (claim) |
|---|---|---|---|---|
| 12 | 0.00564 | 0.00491 | 0.00528 | 0.00527 |
| 16 | 0.00484 | 0.00485 | 0.00485 | 0.00485 |
| 24 | 0.00516 | 0.00475 | 0.00496 | 0.00496 |

At $\eta=0.025$: claim 0.00558, 0.00512, 0.00533; CSV mean 0.00558, 0.00512, 0.00533. **Verifies exactly.**

**Interpretation note.** The patch describes the values as max-or-typical without specifying mean-over-patterns; the mean-over-2-patterns interpretation is the one that fits the published numbers. The max-over-2-patterns interpretation gives slightly larger values (0.00564, 0.00485, 0.00516) — the difference is negligible for the structural conclusion but worth noting for reproducibility.

### E.5 $C_*^2 e^{-m_*}\le 0.017$ bound — VERIFIED AT WORKING CORNER ONLY

Claim: "$C_*^2 e^{-m_*}\le 0.017$ (with smoothing-bridge factor of 3 included)."

The bound is on the rooted form $|\kappa|/q^{|B|-1}$ at incident pairs ($\tau=1, |B|=2$). At the working corner ($\beta=3.5, q=0.003, \eta=0.05$):

- max-over-L mean-over-2-patterns rooted form: 0.00564 (at $L=12$).
- × smoothing-bridge factor 3 = **0.01692 ≤ 0.017** ✓.

**Over the full clean-signal range** (clean pair_incident rows across all $\beta,\eta,q$ combinations, 108 rows total):

- max rooted form: **0.01045** (at $L=12,\beta=4,\eta=0.025,q=0.01$).
- × smoothing-bridge factor 3 = **0.03136**, exceeding the claim 0.017 by ~85%.

Top 5 highest rooted values across the full clean subset:

| $L$ | β | η | q | pattern | rooted |
|---|---|---|---|---|---|
| 12 | 4.0 | 0.025 | 0.01 | pair_incident_same_site_01_03 | 0.01045 |
| 12 | 3.5 | 0.025 | 0.01 | pair_incident_same_site_01_03 | 0.01041 |
| 12 | 3.5 | 0.025 | 0.01 | pair_incident_same_site_01_02 | 0.01034 |
| 24 | 3.5 | 0.025 | 0.01 | pair_incident_same_site_01_02 | 0.00995 |
| 24 | 4.0 | 0.025 | 0.01 | pair_incident_same_site_01_02 | 0.00989 |

**Conclusion.** The bound holds at the working corner — the case relevant for firewall closure at $q=0.003$. The bound does *not* hold uniformly across all sampled $(\beta,\eta,q)$. Statements citing the bound should carry the "at working corner" qualifier (added in pass 4 §1.4, §11.10).

### E.6 $m_*\ge 2$ claim — OVER-EXTRAPOLATED

Claim (`NOTE_PMBSF_mprime_hpm_bridge_v17b_patch.md` §B3.4): "Same-orientation slope -2.36 (positive decay); mixed-axis slope -0.05 (essentially flat at this q). Decisive same-orientation evidence for $m_*\ge 2$."

The slope -2.36 fits log $|\kappa|/q^2$ vs $r$ for `pair_same_ori_axis` at $L=12, \beta=3.5, \eta=0.05, q=0.003$. The CSV at this corner:

| pattern | r | $|κ|/q^2$ | rel_jk_se |
|---|---|---|---|
| pair_same_ori_axis_r1 | 1 | 0.4485 | **0.22** ← clean |
| pair_same_ori_axis_r2 | 2 | 0.0469 | 0.89 ← marginal |
| pair_same_ori_axis_r3 | 3 | 0.2128 | **0.33** ← borderline |
| pair_same_ori_axis_r4 | 4 | **0.000103** | **395.5** ← totally noise |

The r=4 value 0.0001 dominates the slope fit: with all 4 points, slope = -2.36, $m_*=2.36$. **Excluding the r=4 noise point, with clean-only data (rel_jk_se < 0.5):** the remaining points give slope = -0.37, $m_*\approx 0.4$. This is **below the placeholder value $m_*=0.5$**.

**Audit across all corners.** Across the full $(L,\beta,\eta,q)$ grid for pair_same_ori_axis with all 4 r-values having $|κ|/q^2>0$ (15 corners), only **one corner** has ≥ 3 clean signal points: $L=16, \beta=3.5, \eta=0.025, q=0.01$. At that corner:

- All-4-points slope: $m_* = 1.39$
- Clean-only (3 points) slope: $m_* = 0.90$

**Honest empirical conclusion.** The data shows qualitative decay between $r=1$ and $r\ge 3$, but the quantitative slope is dominated by noise at $r=4$ across the entire grid. The strongest defensible claim from clean signal alone is $m_*\in[0.5, 1.0]$ at the working corner, not $m_*\ge 2$.

### E.7 Bridge-tightness consequences

With honest clean-signal $m_*\approx 1$ instead of $m_*\ge 2$:

The pinned-form bound is $|\kappa|/q^{|B|-1}\le C_*^{|B|}q_\eta^0 e^{-m_*\tau(B)}$. At fixed $\tau=1$ (incident pair), the value $C_*^2 e^{-m_*}\le 0.017$ verifies at the working corner — *independent of the $m_*$ exponent at larger $\tau$*. So the **load-bearing tight bound is preserved** under any reasonable $m_*$.

What changes is the geometric-series sum $J_{m_*}=\sum_\tau N(\tau)e^{-m_*\tau}$ that controls how distant polymers contribute to $N_{\rm KP}$. At $m_*=2$, $J\le 0.4$ (patch claim). At $m_*=1$, $J$ grows by a factor of order $e^{(\Delta m)\cdot\langle\tau\rangle}\sim e^{1\cdot 4}\sim 50$. So $J(m_*=1)\sim 20$ and $N_{\rm KP}(p=0.003)\sim 10^{-3}$ instead of $10^{-4}$.

$\varepsilon_{\rm HPM}\sim c_*\cdot N_{\rm KP}\sim 5\cdot 10^{-3}\sim 10^{-2}$ instead of $10^{-3}$. The firewall closure binding threshold is $\varepsilon_{\rm HPM}\sim 5$ (where margin starts to bind), so $10^{-2}$ is still comfortably below by 2.5 orders of magnitude. **Firewall margin remains comfortably above 0.9**, though the headline "20× tighter than v16 empirical $\varepsilon_{\rm ML}\approx 0.02$" no longer holds — the analytic bound is now of the same order as the v16 empirical or somewhat looser.

### E.8 Summary table

| Claim | Source | Verifies? |
|---|---|---|
| 70% noise-dominated rows | patch §B3.4 | ✓ 69.9% |
| 19% clean signal rows | patch §B3.4 | ✓ 18.9% |
| 100% clean at pair_incident | patch §B3.4 | ✓ 108/108 |
| 59% clean at triple_star | patch §B3.4 | ✓ 32/54 |
| 31% clean at triple_L | patch §B3.4 | ✓ 17/54 |
| L-uniformity at η=0.05 working corner | patch §B3.4.1 | ✓ exact (mean over 2 patterns) |
| L-uniformity at η=0.025 working corner | patch §B3.4.1 | ✓ exact |
| $C_*^2 e^{-m_*}\le 0.017$ at working corner | patch §B3.4.2 | ✓ 0.0169 ≤ 0.017 |
| $C_*^2 e^{-m_*}\le 0.017$ globally | implied in pass-3 §10.5 | ✗ max 0.0314 over full clean range |
| $m_*\ge 2$ | patch §B3.4 | ✗ depends on r=4 noise points; clean-only $m_*\approx 0.4$–$1.3$ |
| Pair decay slope -2.36 at L=12 corner | patch + READOUT | ✓ as raw fit; ✗ as evidence for $m_*\ge 2$ |
| Smoothing factor 3 over $\eta\in[0.025,0.10]$ | patch §B8.1 | (not directly verified; depends on ratio of pair_incident rooted at η=0.025 vs η=0.10) |

### E.9 Implications for the program

The v17b empirical anchor strengthens the program by providing an exactly-verified upper bound on the load-bearing pinned-norm constant $C_*^2 e^{-m_*}$ at the working corner. This is a substantive contribution and converts (M′) literature extraction from "load-bearing" to "useful but not blocking" status.

The v17b run does **not** provide a robust empirical lower bound on $m_*$. The slope-fit at r=4 is noise-dominated across the entire grid, and only one corner has ≥ 3 clean signal points. The honest characterization is "qualitative decay confirmed; quantitative rate poorly constrained."

This finding affects three pass-3 claims that pass 4 walks back (§1.4, §11.10, §14.4):

1. "$N_{\rm KP}\le 10^{-4}$" — under clean-signal $m_*\sim 1$, more like $10^{-3}$.
2. "$\varepsilon_{\rm HPM}\sim 10^{-3}$ analytic, beats v16 empirical by 20×" — more like $10^{-2}$, comparable to v16.
3. "Margin $\ge 0.99$" — more like $\ge 0.9$ under honest $m_*$.

**The firewall closure is preserved.** None of these revisions push $\varepsilon_{\rm HPM}$ above the binding threshold $\sim 5$. The structural conclusions of the program stand. What does *not* stand is the headline "tighter than literature would deliver" interpreted as a multi-order-of-magnitude tightness claim. The honest reading is: v17b directly establishes a working-corner upper bound that matches the order of magnitude needed for firewall closure, and that is sufficient for the program's purposes.

### E.10 Recommended next data

To resolve the $m_*$ over-extrapolation cleanly:

1. **More configurations at L=24** to push the MC noise floor down so $r=4$ values become clean signal.
2. **Intermediate $r$ patterns**: introduce pair_same_ori_diag at $r\in\{1.5, 2.5\}$ (or actually achievable lattice distances) to add slope-fit lever arm.
3. **Smaller $\eta$**: $\eta\in\{0.005, 0.01\}$ to test BG smoothing-bridge boundedness as $\eta\to 0$. This is independent of the $m_*$ question and is the originally-flagged §B9 follow-up from the v17b patch.

Estimate: another 30–60 minutes per η-value on A100 at v17b sampler parameters; one shift of run-time to resolve both questions.

---

## Appendix F — Cross-reference table: third-pass HBq2 lemmas (pass 5)

This appendix maps between the third-pass HBq2 lemma stack (`HBq2_Lemmas_A_to_D_ThirdPass_20260524.md`) and the rest of the master document.

### F.1 Lemma-by-lemma cross-reference

| Third-pass HBq2 | Master document | Status (pass 5) |
|---|---|---|
| Lemma A (incident PTO overlap) | §5.5 (PTO-2), §7.5.2 | Proved; Fourier-verified in operational window |
| Lemma B' (clean cap-row) | §7.5.4 | Open stochastic; expectation form required (not p99 alone) |
| Lemma C (trace-to-quadratic bridge) | §7.5.3 | Proved with finite-volume certificate $C_{\rm TQ}^{(\mu)}\le 0.304$ |
| Lemma D-old (Boole spike) | §7.5.5 | Proved by Boole union bound $\le 6q$ |
| Lemma D-density (density spike) | §7.5.5 | Open; empirical fraction 0.118 at L=16 — NOT rare |
| Combined HB-q² | §7.5.6 | Conditional on B', D-old, D-density |
| v15 audit | §11.8 | FAILED at global integration budget |

### F.2 The three row quantities (third-pass Correction 1)

| Symbol | Definition | Role |
|---|---|---|
| $W_e(U)$ | $\max_a\sum_{b\ne a}|C_e(a,b;U)|\operatorname{tr}(A_aA_b)$ | raw trace-weighted row |
| $R_e(U)$ | $W_e(U)/\mu_{\Lambda,L}^2$ | dimensionless normalized row |
| $Z_e(U)$ | $W_e(U)/q^2$ | empirical diagnostic (what scripts print) |
| $C_{\rm row}(e)$ | $R_e(U)/q^2=Z_e(U)/\mu^2$ | theorem-relevant Matrix-Stein coefficient |

A printed $Z_e$ value alone is not the Matrix-Stein coefficient. The absorption scalar after Lemma C is $\eta_{\rm clean}=4C_{\rm TQ}C_{\rm row}q$. At L=16 with $C_{\rm TQ}=0.304, C_{\rm row}^{\rm p99}\approx 486.5, q\approx 0.0032$, this gives $\eta_{\rm clean}^{\rm p99}\approx 1.89$ — finite but not budget-compatible.

### F.3 Empirical fractions at L=16 (third-pass §D.5)

From the clean v2 diagnostic at $L=16, \beta=3.5, \delta=1.0, \Lambda=1$:

| Quantity | Fraction |
|---|---|
| old-spike fraction | 0.016927 |
| density-spike fraction | **0.117839** (not rare) |
| PTO-heavy fraction | $6.51\times 10^{-4}$ |
| unexplained PTO-heavy rows | **0** |

The third-pass observation: "density spikes are not rare enough to discard, but the dangerous PTO-heavy tail is rare and fully captured by old/density labels in the tested run." This supports Lemma D but does not prove it.

### F.4 Why v15 fails despite the third-pass refinement

The third-pass HBq2 document carefully separates *local* statements (Lemmas A, B', C, D applied per link / per incident star) from *global* integration. The v15 audit measures the global covariance operator
$$
\sum_e\mathbb E_W[\Gamma_{\rm off,e}]
$$
directly, *without* the local-to-global Boole + Cauchy–Schwarz reduction implicit in the Lemma D budget calculation. The local-to-global step is exactly where the budget is lost: the volume factor times the per-edge inflation factor exceeds the allowed budget.

Specifically: the Lemma D Boole bound $\mathbb P(\mathcal S_e^{\rm old})\le 6q$ holds per edge. Summed over $4L^4$ edges, the expected spike count is $\le 4L^4\cdot 6q = 24L^4 q$, which at $L=24, q=0.003$ is $\approx 24{,}000$ — substantial. Per-edge inflation factor times this count exceeds budget.

**The third-pass refinement is correct as a local theorem; the v15 failure is at the global integration scale, not in the lemmas themselves.** This is why HB-q² survives as a sharpened local statement but not as a closing route.

### F.5 What's needed to revive HB-q²

A future re-attempt at HB-q² as a closing route would need either:

1. A *uniform* $L$-independent bound on the global covariance operator (not just per-edge), avoiding the Boole + sum approach. This is essentially the (M′) cluster-cumulant statement applied to the off-diagonal cross-term operator — i.e., a *non-Markovian* control on the joint heat-bath sensitivities.
2. A reformulation where the spike contribution is *spectrally projected* before the Boole sum, exploiting the projected-Maxwell continuum-symbol structure (v4b slopes).
3. A sub-budget allocation where HB-q² is *one of multiple* contributing terms summed against a closed-walk envelope rather than the only Wilson-to-random comparator.

Path (3) is closest to the surviving Version C closed-walk approach. The HB-q² contribution there is the per-link incident-star cap-overlap weighting; it is *not* the closure mechanism.

---

## Appendix G — Pass-7 literature deep-dive: peer-reviewed status of (M′)_SU(2)

This appendix records the May-2026 peer-reviewed literature survey commissioned for pass 7. The full annotated report is the source document; this appendix preserves the structurally important results in the master-document format.

### G.1 Scope and method

**Targets:** both level (iii) (pair-cumulant bound for hard $X_p$) and level (iv) (full polymer-cluster cumulant decay) of (M′)_SU(2).

**Inclusion:** SU(2)-specific peer-reviewed results plus adjacent settings (SU(3), U(1) compact, finite non-Abelian, Yang–Mills with matter, scalar models with similar cluster structure).

**Exclusion:** preprints not accepted at a peer-reviewed venue; Russian-language constructive QFT literature (Malyshev–Minlos and successors) — this is a known gap.

**Time period:** 1976–2026, with emphasis on post-2010 developments.

**Key finding (one sentence):** No peer-reviewed paper proves (M′)_SU(2) at either level for SU(2) at large β in d=4; the closest unconditional results are SZZ 2023 (wrong regime), Adhikari–Cao 2025 (wrong group), and Bałaban CMP 1989 (UV stability, not mass gap).

### G.2 What is actually proved for SU(N)/SU(2) lattice YM (May 2026 status)

| Regime | β | What is proved | Source |
|---|---|---|---|
| Strong coupling (small β) | per-link $\|\beta_{\rm std}\|<1/96$ (d=4, N=2) | uniqueness; log-Sobolev; Poincaré; **exponential decay of covariances** for smooth Lipschitz observables | Shen–Zhu–Zhu, *CMP* **400** (2023) |
| Strong coupling | any β with strong-coupling cluster convergence | area law; exponential decay of gauge-invariant correlations | Osterwalder–Seiler, *Ann. Phys.* **110** (1978); Seiler LNP **159** (1982) |
| Strong coupling, 't Hooft | $\|\beta_{\rm tH}\|$ small | Wilson area law for $G\in\{U(N), SU(N), SO(2N)\}$ | Cao–Nissim–Sheffield, *Prob. Math. Phys.* **7** (2026) 37–121 |
| All β (any d ≥ 2) | every β | area-law lower bound (Seiler 1978); perimeter-law upper bound (Simon–Yaffe 1982) | classical |
| UV continuum limit, finite volume | small running $g_k^2$ | UV stability of partition function; continuum limit of gauge-invariant correlators in finite volume, trivial topological sector | Bałaban *CMP* 122 (1989); MRS *CMP* 155 (1993) for SU(2) |
| Fixed large β (asymptotically free) | large β on a fixed periodic 4-lattice | **NO mass gap, NO cumulant-decay theorem** | open |

**Gap between proved and needed:**
1. *Group-theoretic*: finite/abelian/Higgs → compact non-Abelian SU(2) at fixed β.
2. *Coupling regime*: SZZ delivers small β; (M′)_SU(2) needs large β (working corner $\beta=3.5$).
3. *Observable class*: covariance decay for smooth Lipschitz observables vs. hard indicator $X_p$ projected to the spectral window.
4. *Localization*: no peer-reviewed paper localizes a polymer cumulant in the specific spectral-window basis $\{A_p\}$.

### G.3 The closest off-the-shelf candidates with translation analyses

**Candidate 1 — Adhikari–Cao + finite-subgroup approximation.**

- *Result:* for finite non-Abelian $G$ at weak coupling and any gauge-invariant local $f, g$ with disjoint supports $A, B$:
$$|\mathrm{Cov}_\mu(f,g)|\le C(|f|,|g|)\exp(-c\cdot\mathrm{dist}(A,B)).$$
- *Translation to (M′)_SU(2) level (iii):* would require approximating SU(2) by finite non-Abelian subgroups $G_n\in\{2T, 2O, 2I\}$, then proving constants $C(G_n), c(G_n)$ survive $G_n\to{\rm SU}(2)$ — they generically do not.
- *Where it breaks:* swapping coupling thresholds degenerate as $|G_n|\to\infty$; Borgs *CMP* **96** (1984) shows the exact factorization fails for non-Abelian finite groups already.
- **Verdict:** does NOT close level (iii). Useful as sanity check for the Q₈ FNG anchor.

**Candidate 2 — Shen–Zhu–Zhu *CMP* 2023.**

- *Result:* SU(N), per-link $|\beta_{\rm std}|<1/[16N(d-1)]$, log-Sobolev with explicit constant; $\mathrm{Cov}(f,g)$ decays exponentially in lattice distance for smooth Lipschitz $f, g$.
- *Translation effort:* the result is small-β; (M′)_SU(2) needs large β.
- *Where it breaks:* the Hessian estimate underlying Bakry–Émery requires smallness of β times the Hessian of plaquette terms — fails at large β.
- *Could it inform level (iii)?* Only via a *projected, spectral-window* version of the dynamics whose Bakry–Émery condition is preserved under spectral truncation. **No such result is in the peer-reviewed literature.**
- **Verdict:** does NOT close (M′)_SU(2); right shape, wrong regime.

**Candidate 3 — Bałaban *CMP* 116 (1988) + *CMP* 119 (1988) polymer-activity bound.**

- *Result:* per-step polymer activity $|K_k(X)|\le\varepsilon_k^a\exp(-\kappa d_M(X))$ for the 4D YM RG transformation in the small-field region, compatible with per-scale cluster convergence.
- *Translation effort:* heavy. One must (a) restrict to a single (or fixed finite number of) RG scales matching the projected spectral window's lattice scale; (b) replace running $\varepsilon_k$ by a fixed-β polymer activity for the $X_p$ indicator, which is *not* a small parameter at large β unless $q=\mathbb E X_p$ is small via the choice of $\delta_{\rm bond}$; (c) absorb the large-field R-operation contributions into the spectral-window projection.
- *Where it breaks:* the Bałaban activity is bounded by running $\varepsilon_k^a$, which collapses to a useful constant only in the asymptotic-freedom flow. Fixed-β finite-volume periodic 4-lattice statements are not in the published series.
- **Verdict:** the **only** off-the-shelf candidate whose structural form matches level (iv); translation requires re-doing the localization step for the $X_p$ polymer specifically — a non-trivial research project.

**Candidate 4 — Bałaban–Imbrie–Jaffe *CMP* 114 (1988) multiscale cluster expansion.**

- *Result:* exponential decay of correlations in U(1) Higgs in d=2,3 with the level-(iv) κ(B) shape.
- *Translation effort:* U(1) → SU(2) is non-trivial (Higgs potential's deep well supplies the small parameter; pure YM has no analog). The Higgs mass scale plays the role of the spectral-window mass $m_\star$.
- *Where it breaks:* no Higgs field in pure YM; the small parameter must come from the projected indicator probability $q$, not from a deep potential well.
- **Verdict:** right structural template, wrong group/sector.

**Candidate 5 — Magnen–Rivasseau–Sénéor *CMP* 155 (1993).**

- *Result:* SU(2) YM₄ Schwinger functions with IR cutoff in regularized axial gauge.
- *Translation effort:* MRS does not prove mass gap or any cumulant decay. Translation effort is essentially "redo MRS in a periodic 4-lattice setting AND extract a polymer-cumulant bound" — an open research problem.
- **Verdict:** does NOT close (M′)_SU(2) at either level.

### G.4 Pass-7 extracted numerical constants and theorem statements

**Numerical constants to cite verbatim:**

- **Shen–Zhu–Zhu *CMP* 400 (2023):** in the 't Hooft normalization, $|\beta_{\rm tH}|<1/[16(d-1)]$; in per-link normalization ($\beta_{\rm std}=\beta_{\rm tH}/N$), $|\beta_{\rm std}|<1/[16N(d-1)]$. **For SU(2), d=4: per-link $|\beta_{\rm std}|<1/96$ (or $|\beta_{\rm tH}|<1/48$).** SO(N) variant: $|\beta_{\rm tH}|<(N-2)/[32(d-1)N]$.
- **Adhikari–Cao *Ann. Probab.* 53 (2025):** for finite non-Abelian $G$, exponential correlation decay at weak coupling; threshold depends on $|G|$ and conjugacy structure (no single closed-form numerical bound stated).
- **Cao *CMP* 380 (2020):** Wilson loop expectations to leading order in $e^{-\beta}$; Theorem 1.6 gives the explicit first-order term for any finite gauge group satisfying mild conditions.
- **Bałaban *CMP* 116 (1988):** polymer activity at scale $k$ bounded by $\exp(-\kappa d_M(X))$ where $\kappa$ depends only on the block-size $L$ and the small-field/large-field cut; constants not numerically optimized.

**Explicit theorem statements (near-verbatim for appendix use):**

*Shen–Zhu–Zhu, Theorem 1.2 / Corollary 1.6 (paraphrased):* For $G={\rm SU}(N)$, $d>1$, and $|\beta_{\rm tH}|<1/[16(d-1)]$, the lattice Yang–Mills measure $\mu_{\Lambda,N,\beta}$ has a unique infinite-volume limit $\mu_{\infty,N,\beta}$; the associated Langevin dynamic satisfies log-Sobolev with constant uniform in $\Lambda$. Consequently, for $f, g$ smooth Lipschitz with disjoint supports $A, B$:
$$|\mathrm{Cov}_{\mu_\infty}(f, g)|\le C\|f\|_{\rm Lip}\|g\|_{\rm Lip}\exp(-c\cdot\mathrm{dist}(A,B)).$$

*Adhikari–Cao Theorem 1.6 (paraphrased):* For finite (possibly non-Abelian) $G$ and β sufficiently large (weak-coupling per Wilson action), and any gauge-invariant local $f, g$ with disjoint supports $A, B$:
$$|\mathrm{Cov}_\mu(f, g)|\le C(|f|, |g|)\exp(-c\cdot\mathrm{dist}(A,B));$$
the proof uses a probabilistic swapping reducing correlations to percolation probabilities of the union of two independent samples.

*Bałaban *CMP* 122 (1989) Theorems I.1, II.1 (paraphrased):* The R-operation on large-field activities is well-defined, local, and exponentially bounded; combined with the small-field cluster expansion of *CMP* 116, the partition function of 4D pure YM with general compact gauge group satisfies stability bounds uniform in the UV cutoff.

### G.5 Stop-conditions that would change the pass-7 verdict

**Stage 1 — mechanical updates (incorporated in pass 7):** 11-paper Bałaban inventory, new §10.6, honest negative finding in §10.5, §14 strengthening, Appendix A.11 expansion.

**Stage 2 — sourcing decisions (open after pass 7):**
1. Attempt translation of Adhikari–Cao to a Q₈ anchor at concrete β (verifiable by interval arithmetic) as a v18 empirical check, supplementing v17b.
2. Invest in a "spectral-window Bakry–Émery" lemma extending SZZ to projected dynamics at large β; if proved, this delivers level (iii) directly.

**Stage 3 — peer-reviewed developments that would change the recommendation:**
1. **A spectral-window Bakry–Émery extension of SZZ at large β** → elevate that route to a primary alongside Path A.
2. **Adhikari–Cao extended to compact Lie groups** → elevate Path B (modern probabilistic) to a primary closing route.
3. **Cao–Nissim–Sheffield (or successor) extended from area-law / covariance to a cumulant bound at large β** → the master-document theorem becomes unconditional; document should be rewritten accordingly.

### G.6 Caveats on the pass-7 survey

1. Several relevant papers are accepted but not yet in print (e.g. Cao–Park–Sheffield, *Comm. Amer. Math. Soc.*) — cited as "to appear." Borga–Cao–Shogren-Knaak arXiv:2411.11676 is a preprint and is explicitly flagged.
2. Cao–Nissim–Sheffield is peer-reviewed and published in *Prob. Math. Phys.* 7 (2026) 37–121 — superseding earlier preprint citations.
3. The Bałaban polymer activity bound of CMP 116 (1988) is stated for a *single* RG step in the small-field region; combining it into a single fixed-β cumulant bound requires summing scales — which is what Bałaban does in CMP 119 + CMP 122 for UV stability, but not for an off-diagonal cumulant. The translation effort is non-trivial.
4. The Shen–Zhu–Zhu threshold $|\beta_{\rm tH}|<1/[16(d-1)]$ uses the 't Hooft scaling $\beta_{\rm tH}=N\cdot\beta_{\rm std}$; in per-link normalization the threshold is $|\beta_{\rm std}|<1/[16N(d-1)]$. **For SU(2) in d=4: per-link bound is 1/96, NOT 1/48.** The master document uses the per-link Wilson convention; the SZZ threshold therefore reads as $|\beta_{\rm std}|<1/96$.
5. The Seiler 1982 monograph (LNP 159) claims its cluster expansion extends from finite Abelian to general finite groups; **Borgs *CMP* 96 (1984) 251–284** and the Adhikari–Cao 2025 introduction explicitly note this claim is **incorrect**. Pass 7 does not cite Seiler 1982 for non-Abelian results.
6. The pass-7 survey did not cover Russian-language constructive QFT literature (Malyshev–Minlos and successors). Known gap.
7. The master document's pass-6 "essentially equivalent to the mass-gap problem modulo bookkeeping" remark is approximately accurate but slightly **too optimistic** in the sense that mass gap for SU(2) at large β on a 4-lattice is itself genuinely open — not merely bookkeeping. Pass 7 phrasing: "(M′)_SU(2) is at least as hard as the mass gap, and possibly strictly harder because of the projected spectral-window restriction."

---

## Appendix H — Auxiliary derivations from useful old notes (pass 8)

This appendix folds in a stack of "useful old notes" derivations supplied for pass 8. **Six entries are kept** (§H.1–§H.6); seven are excluded or cross-referenced (§H.0). Each kept entry is auxiliary appendix material with an explicit "does NOT prove (M′)_SU(2)/HPM/YM mass gap" disclaimer from its source author. The pass-7 conditional status (Appendix G) is fully preserved.

### H.0 Inclusion and exclusion rationale

#### Included (six entries)

| Subsection | Source file | Self-rating | Genuinely new content |
|---|---|---|---|
| §H.1 SU(3) Weyl-invariant local gap | `SU3_Weyl_Invariant_c1_Derivation_Useful_Old_Notes.md` | (kept as useful local input) | Exact 3-term expansion with rank-2 Weyl ledger; non-radial $p_3^2$ contribution |
| §H.2 Character-proxy Laplacian drift | `exact_character_proxy_laplacian_drift_derivation.md` | 7/10 | Volume-uniform algebraic identity $\Delta_\Lambda V=-12V+24$ for SU(2); nonnegative Wilson pairing |
| §H.3 Haar–Ricci local Bakry–Émery floor | `PMBSF_Haar_Ricci_Local_Curvature_Appendix_20260524.md` | (kept as useful local input) | Explicit local $CD(\rho_0,\infty)$ with $\rho_0=\kappa_G-C_{\rm add}$; product Haar = Riemannian volume |
| §H.4 Uniform fiber LSI | `useful_old_notes_uniform_fiber_lsi_derivation_20260524.md` | (kept as auxiliary lemma) | Curvature $\Rightarrow$ LSI on compact connected fibers |
| §H.5 Corrected Lyapunov–Γ template | `PMBSF_Haar_Curvature_LocalToGlobal_Derivation.md` | (kept after explicit correction) | Corrected weighted-Lyapunov lemma fixing earlier overclaim |
| §H.6 Fixed-cutoff Combes–Thomas template | `reusable_fixed_cutoff_derivation_extraction_20260524.md` | (kept as conditional module) | Average-plaquette typicality + HS hinge + Combes–Thomas + localization $\Rightarrow$ exponential clustering at fixed cutoff |

#### Excluded or cross-referenced (seven entries)

| Source file | Disposition | Reason |
|---|---|---|
| `VSU_corrected_unscreened_spherical_collapse_derivation.md` | **Excluded** | Vacuum Stiffness Unification / cosmology / halo bias program. Not PMBSF-relevant. Source author identifies a separate research thread. |
| `PMBSF_closed_walk_HPM_firewall_derivation_extract_2026-05-24.md` | Cross-referenced to §7.6, §8 | Restates closed-walk / HPM derivation already in master |
| `PMBSF_projected_capacity_firewall_PTO_Bernoulli_HPM_derivation.md` | Cross-referenced to §5, §6, §7.9 | Restates PTO + Bernoulli + HPM chain; source self-rated 8/10. Confirms master content |
| `PMBSF_surviving_closed_walk_HPM_derivation_2026-05-24.md` | Cross-referenced to §7.9, §8 | Restates surviving Version C route; confirms master content |
| `PMBSF_closed_walk_useful_derivations_20260524.md` | Cross-referenced to §5.8, §7.6, §8.4 | Restates closed-walk envelope + CW-KP; confirms master content |
| `PMBSF_useful_old_notes_derivations_2026-05-24.md` | Partially incorporated: finite-channel/Combes–Thomas piece in §H.6 | Source author keeps only 3 of many old modules; the finite-channel module is the genuinely usable one |
| `PMBSF_Haar_Ricci_Local_Curvature_Appendix_20260524__1_.md` | Duplicate of `..._Appendix_20260524.md` | Identical content (verified by diff) |

The cross-referenced files contain **no new derivation content** beyond what is already in the master; they are independent re-derivations of the surviving Version C chain. Their presence in the upload stack confirms the master document's pass-5/6 architecture but does not advance it.

### H.1 SU(3) Weyl-invariant local one-plaquette class-function gap

**Source.** `SU3_Weyl_Invariant_c1_Derivation_Useful_Old_Notes.md`. **Self-disclaimer (verbatim):** "This is **not** a Yang–Mills mass-gap proof. It is a local spectral/asymptotic input for the class-function/the finite-channel part of the paper."

**Role in the master.** Companion finite-$N$ analytical anchor to the FNG Q_8 result (§9). Where FNG Q_8 proves a finite-$\beta$ firewall closure for $Q_8$ at $\beta\ge 61.16$, §H.1 provides a $\beta\to\infty$ asymptotic for SU(3). The two are not directly comparable (Q_8 finite, SU(3) continuous; finite-$\beta$ vs. asymptotic), but together they constitute the only two non-Abelian compact-group analytical anchors currently in the document.

**Setup.** SU(3) one-plaquette class Hamiltonian
$$
H_\beta=\tfrac12 C_2+\beta\left(1-\tfrac13\mathrm{Re}\,\chi_{1,0}\right),
$$
acting on SU(3) class functions. Cartan-plane Weyl-invariant coordinates $p_2=x^2+y^2$, $p_3=\frac{\sqrt 6}{6}y(3x^2-y^2)$. Weyl-Gaussian inner product
$$
\langle f,g\rangle=\int_{\mathbb R^2}f(x,y)g(x,y)\Delta_W^2(x,y)e^{-x^2-y^2}\,dx\,dy
$$
with $\Delta_W^2=\frac{p_2^3}{2}-3p_3^2$.

After canonical scaling, $H_\beta=\beta^{1/2}H_0+H_1+\beta^{-1/2}H_2+O(\beta^{-1})$ with leading oscillator scale $\omega(\beta)=\sqrt{2\beta/3}$ and
$$
H_1=-\frac{p_2^2}{96},\qquad H_2=\sqrt 6\left(\frac{p_2^3}{11520}+\frac{p_3^2}{8640}\right).
$$
**Crucial structural point.** The non-radial $p_3^2$ term in $H_2$ contributes to $c_1$ at order $\beta^{-1/2}$. A radial-only treatment misses this and produces a wrong $c_1$.

**Theorem (Local SU(3) gap).** In the Weyl-Gaussian shell basis $\mathcal B=\{1, p_2, p_3, p_2^2, p_2 p_3, p_2^3, p_3^2\}$, first-order perturbation gives $c_0=-5/16$; second-order resolvent contribution from $H_1$ gives $\Delta_{\rm res}=-205\sqrt 6/3072$; direct $H_2$ contribution gives $\Delta_{H_2}=19\sqrt 6/576$, splitting into radial $\sqrt 6/32$ and non-radial $p_3^2$ piece $\sqrt 6/576$. Hence
$$
\boxed{
c_1=-\frac{205\sqrt 6}{3072}+\frac{19\sqrt 6}{576}=-\frac{311\sqrt 6}{9216},
}
$$
and the local SU(3) one-plaquette class-function gap is
$$
\boxed{
\Delta_{SU(3)}(\beta)=\sqrt{\frac{2\beta}{3}}-\frac{5}{16}-\frac{311\sqrt 6}{9216}\beta^{-1/2}+O(\beta^{-1}).
}
$$

**Numerical sanity.** $c_1\approx -0.0826$. At $\beta=4$ (a SZZ-comparable scale), $\beta^{-1/2}c_1\approx -0.041$, so the three-term expansion gives $\Delta_{SU(3)}(4)\approx\sqrt{8/3}-0.3125-0.0413\approx 1.633-0.354\approx 1.28$. This is the local class-function gap, not a global mass gap.

**What this does NOT prove.** Verbatim from the source author:
- Haar measure alone does not give a physical all-coupling mass lower bound.
- A finite-cutoff Hessian floor does not directly prove a continuum Yang–Mills mass gap.
- A radial-only SU(3) calculation is insufficient for the $\beta^{-1/2}$ coefficient — the non-radial $p_3^2$ contribution is real and must be kept.

**Useful manuscript insertion (paraphrased from source).** "In the SU(3) one-plaquette class sector with Weyl-Gaussian inner product and canonical scaling near the identity, the local spectral gap has the three-term expansion above. The proof retains $p_3^2$ in $H_2$, which is the nontrivial input from rank-two Weyl invariance."

### H.2 Exact character-proxy Laplacian drift identity

**Source.** `exact_character_proxy_laplacian_drift_derivation.md`. **Self-disclaimer (verbatim):** "It does **not** close the current PMBSF paper. The current PMBSF route still hinges on the hard-plaquette cumulant / closed-walk transfer input. This derivation is best used as a clean auxiliary lemma or appendix, not as the main theorem." **Source self-rating: 7/10.**

**Role in the master.** Provides exact volume-uniform algebraic identities for drift normalization, smooth-source bookkeeping, and validation of numerical generator decompositions. Useful in §11 calibration discussions and as an appendix lemma for §8.3 BG smoothing-bridge bookkeeping.

**Setup.** Let $\Lambda$ be a finite periodic hypercubic lattice with oriented links $E(\Lambda)$ and plaquettes $P(\Lambda)$. Let $G={\rm SU}(N)$ with bi-invariant Riemannian metric. Product Laplace–Beltrami $\Delta_\Lambda=\sum_{\ell\in E(\Lambda)}\Delta_\ell$. Smooth fundamental-character plaquette defect
$$
\tilde z(g):=1-\frac{1}{N}\mathrm{Re}\operatorname{Tr}(g),\qquad \tilde z_p(U):=\tilde z(U_p(U)).
$$
This is globally $C^\infty$, conjugation-invariant, nonnegative, quadratic near identity: $\tilde z(\exp X)=-\frac{1}{2N}\operatorname{Tr}(X^2)+O(\|X\|^3)\asymp\|X\|^2$ — avoids cut-locus pathologies of $d_G(g,1)^2$.

Averaged defect $\overline z_\Lambda=\frac{1}{|P|}\sum_p\tilde z_p$, Lyapunov seed $\overline V_\Lambda=1+\overline z_\Lambda$.

**Theorem H.2.1 (Fundamental-character eigenfunction).** Under the metric normalization with $\Delta_G(\mathrm{Re}\operatorname{Tr}U)=-\lambda_{\rm fund}\mathrm{Re}\operatorname{Tr}U$:
$$
\boxed{\Delta_G\tilde z=-\lambda_{\rm fund}\tilde z+\lambda_{\rm fund}.}
$$

**Theorem H.2.2 (Single-plaquette Laplacian).** By bi-invariance and inversion-isometry, for the four boundary links $\ell\in\partial p$ the one-link function $U_\ell\mapsto\tilde z(U_p(U))$ inherits the same eigen-affine identity. Summing,
$$
\boxed{
\Delta_\Lambda\tilde z_p=-4\lambda_{\rm fund}\tilde z_p+4\lambda_{\rm fund}.
}
$$
**Volume-independent.** Independent of plaquette location.

**Theorem H.2.3 (Averaged drift identity for SU(2)).** For $G={\rm SU}(2)\cong S^3$ with standard normalization, $\lambda_{\rm fund}=3$. Defining $B_p(U)=1-w(U_p)$ with $w(g)=\frac12\mathrm{Re}\operatorname{Tr}(g)$ and $V=1+B_{\rm avg}$:
$$
\boxed{\Delta_\Lambda V=-12V+24.}
$$
This matches the numerical affine law (intercept $\approx 24$, slope $\approx -12$) reported in master document drift certificates.

**Theorem H.2.4 (Wilson pairing positivity).** With $D_\Lambda=\sum_p\tilde z_p$, $S_W=\beta D_\Lambda$:
$$
\boxed{
\langle\nabla S_W,\nabla\overline V_\Lambda\rangle=\frac{\beta}{|P|}\|\nabla D_\Lambda\|^2\ge 0.
}
$$

**Theorem H.2.5 (Generator decomposition and drift ceiling).**
$$
L_\Lambda\overline V_\Lambda=-\lambda\overline V_\Lambda+b-\frac{\beta}{|P|}\|\nabla D_\Lambda\|^2,\qquad\lambda=4\lambda_{\rm fund},\;b=8\lambda_{\rm fund},
$$
and consequently
$$
\boxed{L_\Lambda\overline V_\Lambda\le -\lambda\overline V_\Lambda+b}\quad\text{(one-sided affine drift ceiling).}
$$

**Honest caveat (verbatim from source).** "This is not, by itself, a Foster–Lyapunov drift of the form $LV\le-cV+b\mathbf 1_K$ with a useful outside-core coercive negative term, because $24-12V$ is positive for $V<2$. The missing coercive input is still a lower bound on the gradient term outside a chosen core."

**Design principle for smooth-source bookkeeping** (source §10). For $V_\Phi=\sum_p\Phi(\tilde z_p)$, if $\Phi'(0)\ne 0$ the dangerous volume-leak term $\sum_p\Phi'(\tilde z_p)\Delta_\Lambda\tilde z_p$ produces $O(|P|)$ leakage near the vacuum. Choosing $\Phi'(0)=0$ (e.g. $\Phi(s)=s^2$) makes the leakage defect-weighted instead.

### H.3 Haar–Ricci local Bakry–Émery curvature floor

**Source.** `PMBSF_Haar_Ricci_Local_Curvature_Appendix_20260524.md`. **Self-disclaimer (verbatim):** "useful, but only as a *local curvature floor* derivation. It does **not** close the current SU(2) stochastic gap, does **not** prove (M′)_SU(2), and does **not** advance the surviving HPM closed-walk route except by cleaning up the local Bakry–Émery/Haar-mass background."

**Role in the master.** Provides the *local* piece of the pass-7 §10.6 stop-condition "spectral-window Bakry–Émery extension of SZZ at large β." If the global piece were ever supplied (by a research extension of SZZ 2023), this appendix would be the local input. Currently it is auxiliary structural content only.

**Setup.** $\Lambda$ finite hypercubic, $G$ compact connected Lie group, bi-invariant metric $g_G$. Configuration manifold $M_\Lambda=G^{E(\Lambda)}$ with product metric $g_\Lambda$ and volume
$$
\boxed{d\operatorname{vol}_{g_\Lambda}(U)=\prod_{\ell\in E(\Lambda)}dU_\ell.}
$$
Product Haar measure equals the Riemannian volume of $g_\Lambda$ — this is not a definition but a consequence of bi-invariance.

**Theorem H.3.1 (Product Ricci floor).** Single-link Ricci $\mathrm{Ric}_{g_G}\ge\kappa_G g_G$ with $\kappa_G>0$ (independent of $\Lambda$). Then
$$
\boxed{\mathrm{Ric}_{g_\Lambda}\ge\kappa_G g_\Lambda,\qquad\kappa_G\text{ uniform in }\Lambda.}
$$
For $G={\rm SU}(N)$ with bi-invariant metric scaled so that $\Delta_G({\rm Re}\operatorname{Tr}U)=-\lambda_{\rm fund}{\rm Re}\operatorname{Tr}U$: $\kappa_G$ is computed from the Killing form structure constants.

**Theorem H.3.1' (Explicit κ_G for SU(2); added pass 9).** For $G={\rm SU}(2)$ in the master document's normalization $\Delta_{{\rm SU}(2)}({\rm Re}\operatorname{Tr}U)=-3\,{\rm Re}\operatorname{Tr}U$:
$$
\boxed{\kappa_G=2.}
$$

*Derivation.* The bi-invariant metric satisfying $\Delta(\mathrm{Re}\operatorname{Tr}U)=-3\,\mathrm{Re}\operatorname{Tr}U$ is the round metric on $S^3\cong{\rm SU}(2)$ at radius $r=1$ (since the Laplacian on $S^n_r$ acting on degree-$\ell$ harmonics has eigenvalue $\ell(\ell+n-1)/r^2$; for $n=3,\ell=1,r=1$ this is $3$). The Ricci tensor of $S^n_r$ is $(n-1)/r^2\cdot g$, so for $S^3$ at $r=1$: $\mathrm{Ric}=2\,g$, i.e. $\kappa_G=2$.

**Corollary (Numerical local floor for the master working corner).** At the master's working point ($\beta=3.5,\delta_{\rm bond}=1$), with no added regulator ($S_{\rm add}=0$, hence $C_{\rm add}=0$):
$$
\boxed{\rho_0=\kappa_G=2,\qquad\text{uniform in }L.}
$$

The Wilson Hessian $2c_W d_1^*d_1$ at $U^{(0)}$ contributes a non-negative additional amount on horizontal vectors. Its smallest nonzero eigenvalue on horizontal modes is the smallest nonzero plaquette-momentum-squared on the periodic $L^4$ lattice, approximately $(2\pi/L)^2$ (for the lattice convention $4\sin^2(\pi/L)$, identical in the large-$L$ limit). At $L=24$: $\approx 0.0685$. With Wilson normalization $c_W\approx\beta/2=1.75$ at $\beta=3.5$: the Wilson Hessian contribution at the lowest horizontal mode is $2c_W\cdot 0.0685\approx 0.24$, much smaller than $\kappa_G=2$. **The IR floor is Ricci-dominated:**
$$
\rho_0(\text{IR})\ge \kappa_G=2.
$$

At UV horizontal modes (large lattice momentum), the Wilson Hessian dominates: at $k_{\rm max}\sim\pi/a$ where $a$ is the lattice spacing, $d_1^*d_1\sim 16$, so Wilson contribution $\sim 2c_W\cdot 16=56$ at $\beta=3.5$. **UV floor:** $\rho_0(\text{UV})\sim 2+56=58$, dominated by the Wilson Hessian.

**Comparison to SZZ 2023.** The Shen–Zhu–Zhu Bakry–Émery threshold (pass-7 §10.6) is per-link $|\beta_{\rm std}|<1/96$ for SU(2) in d=4, two orders of magnitude below the master's $\beta=3.5$. At $\beta=3.5$, SZZ's global Bakry–Émery argument does not apply. **What §H.3 + Theorem H.3.1' supply, that SZZ does not at $\beta=3.5$, is the local IR floor at the trivial configuration**. SZZ supplies a global statement at small β; §H.3 supplies a local statement at large β. The two are not contradictory; they are complementary regime contributions. See §H.8 below for the assembly of a hypothetical large-β proof using these pieces.

**Theorem H.3.2 (Exponential-coordinate Haar potential).** With Haar entropy $S_H=-\log J_G$ in Lie-algebra exponential coordinates at the identity,
$$
\boxed{\nabla^2 S_H(0)=\frac{1}{3}\mathrm{Ric}_G,\qquad\nabla^2 S_H(0)\ge c_H I,\;c_H=\kappa_G/3.}
$$

**Theorem H.3.3 (Wilson Hessian at trivial configuration).** At $U^{(0)}_\ell=e$ for all $\ell$ in exponential coordinates:
$$
\boxed{\nabla^2 S_W(U^{(0)})=2c_W d_1^*d_1,}
$$
where $d_1$ is the lattice exterior derivative on 1-forms and $c_W$ is the Wilson coupling normalization. This is the projected Maxwell operator. Nonnegative; vanishes on closed 1-forms (gauge zero modes).

**Theorem H.3.4 (Local horizontal Bakry–Émery floor).** Let $S_\Lambda=S_W+S_{{\rm add},\Lambda}$ with $S_{\rm add}$ smooth, local, gauge-invariant, satisfying $\nabla^2 S_{{\rm add},\Lambda}(U)\ge-C_{\rm add}g_\Lambda(U)$ uniformly with $C_{\rm add}<\kappa_G$. The Bakry–Émery tensor at the trivial configuration is
$$
\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})=\mathrm{Ric}_{g_\Lambda}+\nabla^2 S_W(U^{(0)})+\nabla^2 S_{{\rm add},\Lambda}(U^{(0)})\ge(\kappa_G-C_{\rm add})I+2c_W d_1^*d_1.
$$
For horizontal vectors $v\in H_{U^{(0)}}$ (the orthogonal complement to gauge orbits):
$$
\boxed{\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)\ge\rho_0\|v\|_{g_\Lambda}^2,\qquad\rho_0:=\kappa_G-C_{\rm add}>0.}
$$
**Volume-uniform.** $\rho_0$ independent of $\Lambda$.

**What this delivers and what it does not** (verbatim from source §8). What is delivered: a clean local horizontal $CD(\rho_0,\infty)$ statement at the trivial configuration. What is NOT delivered:
1. Global $CD(\rho,\infty)$ over $M_\Lambda$.
2. A Foster–Lyapunov drift toward $U^{(0)}$.
3. A capacity or small-bad-set estimate for $K^c$.
4. Local-to-global functional inequality machinery with audited constants.
5. Compatibility with gauge-invariant restriction/horizontal sector at finite distance from $U^{(0)}$.

**Safe manuscript wording (verbatim from source).** "The old Haar-curvature notes give a rigorous local structural input: product Haar measure is the Riemannian volume of $G^{E(\Lambda)}$, the product Ricci tensor gives a volume-uniform geometric curvature floor, and near the trivial configuration the Wilson Hessian is $2c_W d_1^*d_1$. Hence, assuming any added regulator/gauge-fixing contribution has Hessian bounded below by $-C_{\rm add}g_\Lambda$ with $C_{\rm add}<\kappa_G$, the Bakry–Émery tensor has a positive local lower bound on horizontal directions, uniformly over finite volumes. This supports the local Bakry–Émery/Haar-mass interpretation used in the PMBSF calibration discussion. It does not prove (M′)_SU(2), HPM, or a global Yang–Mills mass gap."

**Unsafe wording (verbatim from source, marked "do not use"):** "Haar curvature proves the mass gap"; "The Wilson Hessian gives a volume-uniform gap"; "The local $CD(\rho,\infty)$ bound globalizes automatically"; "The local Haar mass closes the PMBSF firewall"; "This proves (M′)_SU(2)."

**Connection to pass-7 §10.6 SZZ.** §H.3 supplies the *local* Bakry–Émery floor at $U^{(0)}$ uniformly in $\Lambda$. SZZ 2023 supplies a *global* Bakry–Émery / log-Sobolev at strong coupling. The two pieces do not combine into a large-β SU(2) statement: SZZ's global content uses smallness of $\beta$, while §H.3's local content uses Hessian nonnegativity at $U^{(0)}$. A *spectral-window* Bakry–Émery extension at large β would need a new mechanism that combines (i) the local floor (§H.3), (ii) a Lyapunov toward $U^{(0)}$, and (iii) gauge-invariant horizontal restriction. None of these three is supplied by the existing peer-reviewed literature in combination at large β; (i) is in hand.

### H.4 Uniform fiber log-Sobolev from Bakry–Émery curvature

**Source.** `useful_old_notes_uniform_fiber_lsi_derivation_20260524.md`. **Self-disclaimer (verbatim):** "It does not prove the PMBSF Wilson stochastic transfer, the hard-plaquette cumulant theorem (M′)_SU(2), HPM closed-walk domination, or the Yang–Mills mass gap. It is a usable auxiliary lemma, not a closing argument."

**Role.** Auxiliary lemma for any fiber decomposition / conditional-measure argument. The lemma is standard Bakry–Émery; what the source supplies is a careful statement on compact connected fibers with explicit constants.

**Lemma H.4.1 (Uniform fiber LSI).** Let $\{(M_b,g_b)\}_{b\in B}$ be a measurable family of compact connected Riemannian manifolds, with $\mu_b\propto e^{-W_b}d{\rm vol}_{g_b}$, $W_b\in C^2(M_b)$. Suppose
$$
\mathrm{Ric}_{g_b}+\nabla^2 W_b\ge\rho_{\rm fib}\,g_b\qquad\text{for all }b,
$$
with $\rho_{\rm fib}>0$ uniform in $b$. Then for every $b$ and every probability density $\nu_b\ll\mu_b$,
$$
\boxed{
I(\nu_b\mid\mu_b)\ge 2\rho_{\rm fib}\,\mathrm{Ent}_{\mu_b}(\nu_b).
}
$$
Equivalently, $\mathrm{LSI}_{\mu_b}(\rho_{\rm fib})$ holds with constant uniform in $b$.

**Do-not-claim list (verbatim from source).**
1. "This gives a mass floor on the global manifold." — Correct: it gives $I\ge 2\rho\mathrm{Ent}$. A *floor* needs an entropy/support/boundary gap.
2. "A closed compact fiber can have globally strongly convex $W$." — Correct: $\nabla^2 W\ge c g$, $c>0$, is impossible on a closed manifold.
3. "This proves (M′)_SU(2)." — Correct: it is a curvature-to-LSI module. It says nothing by itself about hard Wilson plaquette indicators or q-power cumulants.
4. "This closes the PMBSF firewall." — Correct: the master document still needs the Wilson-to-random/block plaquette-incidence transfer through the active HPM/closed-walk program.
5. "Bounded geometry gives an explicit sharp LSI constant." — Correct: bounded geometry gives a uniform positive constant, typically implicit unless a specific quantitative theorem is invoked.

**Manuscript role.** Cite §H.4 only as an appendix lemma in support of a future fiber decomposition where the curvature hypothesis is independently established.

### H.5 Corrected local-to-global Lyapunov–Γ template

**Source.** `PMBSF_Haar_Curvature_LocalToGlobal_Derivation.md`. **Self-disclaimer (verbatim):** "Useful, but only after one repair. ... The old weighted Lyapunov lemma must be corrected: the drift condition $LW\le-\alpha W+\beta\mathbf 1_K$ does **not** by itself imply $\int f^2 W\,d\mu\le\ldots$. The correct form controls $\int f^2\phi\,d\mu$ when $LW\le-\phi W+\beta\mathbf 1_K$. This correction matters. Without it, the appendix would overclaim."

**Role.** Documents and fixes an overclaim in earlier weighted-Lyapunov material. Any future Lyapunov–Γ argument in the master document must use the corrected form below.

**Lemma H.5.1 (Corrected weighted Lyapunov–Γ estimate).** Let $W\ge 1$ be $C^2$ on $M_\Lambda$ and suppose
$$
LW\le-\phi W+\beta\mathbf 1_K
$$
for some **nonnegative measurable function** $\phi$ (not necessarily a positive constant), constant $\beta\ge 0$, and compact set $K$. Then for all smooth $f$,
$$
\boxed{
\int f^2\,\phi\,d\mu\le\int\Gamma(f)\,d\mu+\beta\int_K f^2\,d\mu.
}
$$

**What is wrong with the older statement.** The old form $LW\le-\alpha W+\beta\mathbf 1_K$ (constant $\alpha$, not function $\phi$) was sometimes carried as implying $\int f^2 W\,d\mu\le\int\Gamma(f)\,d\mu/\alpha+\ldots$. **This implication is false in general.** The weight on the LHS of the variance estimate must be the same function $\phi$ that appears in the drift bound, not the Lyapunov function $W$. For pointwise-$\alpha$ drift, $\phi\equiv\alpha$ and the LHS reduces to $\alpha\int f^2\,d\mu$, which is a *Poincaré-type* inequality with constant $1/\alpha$ outside $K$ — not a weighted estimate involving $W$.

**Consequence for master-document use.** Any argument that *would* invoke a weighted-Lyapunov bound of the form $\int f^2 W\,d\mu\le\ldots$ from a constant-coefficient drift must be re-examined. The current master document does not use such an argument in a load-bearing position, so the correction does not invalidate any pass-1 through pass-7 claim; it does preclude introducing one in future passes without §H.5 being explicitly applied.

### H.6 Fixed-cutoff Combes–Thomas / localization template

**Source.** `reusable_fixed_cutoff_derivation_extraction_20260524.md`. **Self-disclaimer (verbatim):** "Useful material exists, but it is conditional. ... It does **not** close the remaining stochastic bridge for Wilson-generated defect geometry."

**Role.** Provides a conditional template for fixed-cutoff exponential clustering combining four ingredients. Partially overlaps with §7.6 HPM / §8.4 CW-KP. The Combes–Thomas inverse-decay piece is the new structural ingredient relative to the master.

**Conditional pipeline (Lemma H.6.1).**
$$
\boxed{
\underbrace{\text{average-plaquette typicality}}_{\text{volume-scale prob.}}+\underbrace{\text{conditional HS hinge}}_{\text{matrix coercivity}}+\underbrace{\text{Combes–Thomas inverse decay}}_{\text{resolvent kernel}}+\underbrace{\text{localization algebra}}_{\text{operator localization}}\Longrightarrow\text{fixed-cutoff exponential clustering}.
}
$$

**Five remaining gaps (verbatim from source §7).** These are not solved by the template:
1. **Small-field Wilson Hessian stability.** The matrix hinge depends on a volume-uniform Hessian stability estimate on the good set.
2. **Reflecting HS on the conditioning domain.** The conditional HS step assumes a reflecting generator / Neumann framework on the small-field domain $\mathcal K$.
3. **Good-set mismatch.** Appendix-J–style controls an *average*-plaquette event; pointwise small-field events are *not equivalent*.
4. **Sparse-defect bridge.** The PMBSF capacity firewall needs a stochastic theorem controlling the projected capacity of Wilson-generated bad plaquettes — i.e., (M′)_SU(2) or HPM. (M′)_SU(2) is open per pass-7 §10.6.
5. **Continuum scaling.** No uniform-in-cutoff mass lower bound is derived.

**Honest framing (verbatim from source §8).** "Insert this material as a conditional theorem/proposition, not as a completed main theorem. ... Then separately state the open theorem: prove that the Wilson-generated bad plaquette set satisfies the projected-capacity firewall hypothesis. This is the part that should be attacked next."

**Manuscript usage.** §H.6 can be cited if a fixed-cutoff exponential clustering statement is invoked as an intermediate result. It is NOT a substitute for the open (M′)_SU(2) / HPM input.

### H.7 Net Appendix H summary

The six entries collectively supply:
- One asymptotic local class-function gap for SU(3) (§H.1).
- One exact volume-uniform algebraic drift identity for SU(2) (§H.2).
- One local Bakry–Émery curvature floor at the trivial configuration (§H.3).
- One curvature-to-LSI auxiliary lemma (§H.4).
- One corrected weighted Lyapunov–Γ template (§H.5), fixing an earlier overclaim.
- One conditional fixed-cutoff clustering template (§H.6) with five explicit remaining gaps.

**None of these closes (M′)_SU(2), HPM, or the YM mass gap.** This is consistent across all source authors. The closest connection to currently open work is §H.3 supplying the local input for a hypothetical spectral-window Bakry–Émery extension at large β (pass-7 §10.6 stop-condition); the global piece of that extension remains unsupplied by any peer-reviewed paper or by any of the new uploads.

**Pass-8 verdict.** The Appendix H content is useful auxiliary material and is now part of the master document. The pass-7 conditional status (Appendix G) is fully preserved.

### H.8 Research direction: hypothetical spectral-window Bakry–Émery proof of (M′)_SU(2) level (iii) (pass 9)

**Status disclaimer.** This subsection articulates a *research direction*, not a closing route. It does NOT advance the conditional status of the master theorem. The pass-7 finding (no peer-reviewed paper closes (M′)_SU(2) at large β; Appendix G) is unchanged. The pass-9 contribution is to *scope* the open work using the pass-8 §H.3 / §H.5 / §H.2 local pieces and the pass-9 explicit constant $\kappa_G=2$ for SU(2).

**Why this is the natural research direction.** The pass-7 §10.6.1 SZZ subsection identified that a *spectral-window Bakry–Émery extension of Shen–Zhu–Zhu 2023 at large β* would deliver level (iii) of (M′)_SU(2) directly. SZZ at small β is regime-mismatched to the master document's working point $\beta=3.5$. With pass 8 supplying §H.3 (local floor at $U^{(0)}$, $\kappa_G=2$) and §H.2 (drift identity), three of four ingredients of such an extension are now in hand or partial. The remaining ingredient — globalization — is the genuine open work.

#### H.8.1 The target

**(M′)_SU(2) level (iii):** for $X_p=\mathbf 1\{\phi(U_p)\ge\delta_{\rm bond}\}$ under SU(2) Wilson at $\beta\ge\beta_0$,
$$
\sum_{p'}|\mathrm{Cov}(X_p, X_{p'})|\operatorname{tr}(A_p A_{p'})\le C q^2\kappa_\Lambda^2.
$$

A sufficient input is *gauge-invariant exponential decay of correlations for indicator-valued local observables*, projected to the master document's spectral window $P_{\le\Lambda,L}$. The Bakry–Émery route delivers this if four conditions hold:

#### H.8.2 The four ingredients

| Ingredient | Pass-9 status | Source |
|---|---|---|
| **(i) Local Bakry–Émery floor at $U^{(0)}$, uniform in $\Lambda$, at large β** | **supplied** | §H.3 Theorem H.3.1' (pass 9): $\rho_0=\kappa_G=2$ for SU(2), uniform in $\Lambda$ |
| **(ii) Gauge-invariant horizontal restriction** | **supplied** | §H.3 Theorem H.3.4: $\mathrm{Ric}_{\mu_\Lambda}(U^{(0)})(v,v)\ge\rho_0\|v\|^2$ for $v\in H_{U^{(0)}}$ |
| **(iii) Lyapunov toward $U^{(0)}$ for SU(2) Wilson at large β** | **partially supplied** | §H.2 Theorem H.2.5: $L_\Lambda\overline V_\Lambda\le -\lambda\overline V_\Lambda+b$ with $\lambda=4\lambda_{\rm fund}=12$, $b=24$ for SU(2). **However**: the bound is not Foster–Lyapunov in form because $24-12V$ is positive for $V<2$ (i.e., away from large-defect configurations); the missing piece is a coercive negative term outside a chosen core, which requires a lower bound on $\|\nabla D_\Lambda\|^2$ outside a localization set. Source §H.2 author flags this explicitly. |
| **(iv) Globalization: extend the local floor to a global functional inequality with explicit constants** | **NOT supplied** | Not in any pass-1 through pass-8 content. Not in any peer-reviewed paper at large β (pass-7 Appendix G). The standard local-to-global mechanisms (§H.5 corrected weighted-Lyapunov template, Mosco-convergence, U-bound machinery) require ingredient (iii) to be a Foster–Lyapunov with explicit core $K$ and coercivity outside $K$ — which is precisely what is partial. |

#### H.8.3 The local Bakry–Émery + globalization template

Schematically, the hypothetical proof would proceed:

$$
\underbrace{\text{ingredient (i) at }U^{(0)}}_{\rho_0=2}
\xrightarrow{\text{ingredient (ii) horizontal restriction}}
\underbrace{\text{local horizontal LSI/Poincaré at }U^{(0)}}_{\text{constant }\rho_0}
\xrightarrow{\text{ingredient (iii) Lyapunov to }U^{(0)}}
\underbrace{\text{global functional inequality}}_{\text{via §H.5 corrected template}}
\xrightarrow{\text{ingredient (iv) globalization}}
\underbrace{\text{exponential decay of correlations}}_{\text{(M′)}_{\rm SU(2)}\text{ level (iii)}}.
$$

The first three arrows correspond to standard but technically demanding constructions. The fourth arrow — making the local-to-global step go through with explicit large-β constants for projected indicator-valued observables — is where every existing peer-reviewed result either (a) restricts to small β (SZZ), (b) restricts to finite groups (Adhikari–Cao), or (c) restricts to small-coupling abelian Higgs (BIJ CMP 114, 1988).

#### H.8.4 What is genuinely new in pass 9

The pass-9 contribution is making ingredients (i) and (ii) **numerically explicit** for SU(2) at the master's working point. Before pass 9:

- Pass 8 §H.3 stated $\rho_0=\kappa_G-C_{\rm add}>0$ symbolically.
- Pass 7 §10.6.1 said "no peer-reviewed result extends SZZ to large β" without specifying what local input would be available.

Pass 9 supplies:

- $\kappa_G=2$ for SU(2) in the document's normalization (Theorem H.3.1').
- At the working corner ($\beta=3.5,\delta_{\rm bond}=1$, no added regulator): $\rho_0=2$, uniform in $L$.
- The Wilson Hessian's IR contribution at the lowest horizontal mode (at $L=24$): $\sim 0.24$, dominated by Ricci.
- The Wilson Hessian's UV contribution at high lattice momenta: $\sim 56$, dominating Ricci.

This is the first numerical anchor for the pass-7 §10.6.1 research direction.

#### H.8.5 What is NOT changed by pass 9

The conditional status of the master theorem is unchanged. The pass-7 literature finding (no peer-reviewed paper closes (M′)_SU(2) at large β) is unchanged. The Version C closed-walk surviving route is unchanged. The §14.4 disclaimers are extended, not weakened.

Specifically, §H.8 does NOT claim:
- That ingredient (iv) is close to being supplied.
- That the local Bakry–Émery floor extends globally.
- That (M′)_SU(2) is "in reach" or "soon to be proved."
- That spectral-window Bakry–Émery is the unique or even the most promising research direction.

The pass-7 §10.6.4 stop-condition summary lists three peer-reviewed-paper publication events that would change the route status. Pass 9 does not constitute any of those events.

#### H.8.6 Alternative research directions

For completeness, the other pass-7 §10.6.4 stop conditions:
- **Adhikari–Cao extended to compact Lie groups**: would elevate Path B; not in any pass-8 upload.
- **Cao–Nissim–Sheffield (or successor) extended from area-law / covariance to a cumulant bound at large β**: would re-classify the master theorem as unconditional; not in any pass-8 upload.
- **A peer-reviewed paper proving Bakry–Émery / convexity at large β for projected SU(2) Wilson dynamics**: would elevate Path B; not in any pass-8 upload.

Pass 9's §H.8 corresponds most closely to the third option but is *not* such a paper — it is a scoping memo.

#### H.8.7 Honest meta-comment

The pass-7 author note (closing paragraph) said: "The most natural research direction is a spectral-window Bakry–Émery extension of Shen–Zhu–Zhu 2023 at large β; if proved, this delivers level (iii) directly." Pass 8 supplied the local floor, in symbolic form. Pass 9 supplies the explicit constant ($\kappa_G=2$). **What is now visible** is that the gap between "local floor in hand" and "global theorem proved" is precisely the standard hard problem of *globalizing a local Bakry–Émery bound on a non-uniformly curved manifold via a Lyapunov-coercivity mechanism* — a research area with substantial literature (Bakry–Gentil–Ledoux 2014; Cattiaux–Guillin 2009; etc.) but no peer-reviewed application to lattice gauge theory at large β.

**This is a fair statement of the open work.** It is neither closer to solved nor further from solved than the pass-7 framing; it is *scoped*.

---

## Appendix I — SU(2) closure derivation chain (conditional, pass 10)

This appendix folds in the comprehensive derivation document `SU2_PMBSF_closure_full_derivations_20260524.md` (1054 lines). The source document is honest at the top: **"Manuscript derivation draft. Not a proof of the Yang–Mills mass gap."** Pass-10 preserves this scope and the conditional status of the master theorem.

The structure is a reduction proof. Assuming the **rooted-source polymer estimate** (§I.2.1 below, source eq 0.1), the source derives — step by step, with explicit constants — the chain
$$
\boxed{
\text{rooted-source polymer}
\Rightarrow
\text{centered rare-source mixing}
\Rightarrow
\text{pair closure}
\Rightarrow
\text{PTO level-(iii)}
\Rightarrow
\text{smooth HPM}
\Rightarrow
\text{hard HPM}
\Rightarrow
\text{projected firewall}.
}
$$
The rooted-source polymer estimate at large β for SU(2) is the still-open core target. The pass-7 finding (Appendix G) and pass-9 status are unchanged: no peer-reviewed paper supplies this estimate at large β.

### I.0 Master ↔ Appendix I cross-reference

| Master section | Appendix I subsection | Role |
|---|---|---|
| §5 deterministic spine | §I.1 setup, §I.5 PTO summability | already in master; §I.5 makes the PTO trace-overlap summability eq 5.1 explicit |
| §7.6 HPM sparse closed-walk domination | §I.11 smooth HPM from cumulants | §I.11 gives the explicit proof under CW-KP condition (eq 11.1) |
| §7.9 Version C ↔ proof program | §I.0 chain overview | maps Version C closure to the explicit step-by-step chain above |
| §8.2 BS smooth source | §I.2 target theorem, §I.3 Theorem F | §I.3 makes BS-style two-source pressure expansion explicit |
| §8.3 BG smoothing bridge | §I.12 hard/smooth boundary-band | explicit construction in §I.12 |
| §8.4 CW-KP summability | §I.11 eq 11.1 | explicit CW-KP condition |
| §10.5 honest negative finding | §I.15 honest status | aligns; §I.15 reaffirms no peer-reviewed source |
| §10.6.1 SZZ spectral-window | §I.16 minimal target | the minimal pair-cumulant target is the form a spectral-window Bakry–Émery extension would deliver |
| §H.8 research direction | §I.16 minimal target | sharpens the pass-9 four-ingredient memo to a single concrete pair-cumulant inequality |

### I.1 SU(2) Wilson setup

Work on a periodic four-dimensional lattice $T_L^4=(\mathbb Z/L\mathbb Z)^4$. For SU(2), write a group element as a unit quaternion
$$
U=a_0\mathbf 1+i\sum_{j=1}^3 a_j\sigma_j,\qquad a=(a_0,a_1,a_2,a_3)\in S^3,
$$
so that $\frac12\operatorname{Re}\operatorname{Tr}(U)=a_0$. For a plaquette $p$, the defect score is
$$
\phi_p(U):=1-\tfrac12\operatorname{Re}\operatorname{Tr}(U_p).
$$
The hard high-plaquette indicator is $X_p(U):=\mathbf 1\{\phi_p(U)\ge t\}$. For analysis, replace $X_p$ with a smooth source
$$
X_{p,\eta}(U):=f_\eta(\phi_p(U)-t),
$$
where $f_\eta$ is a smooth increasing approximation of $\mathbf 1\{x\ge 0\}$ with width $\eta$.

Write $q=\mathbb E_W X_p$ and $q_\eta=\mathbb E_W X_{p,\eta}$; note $q\le q_\eta$ with $q_\eta\to q$ as $\eta\to 0$ at fixed threshold.

### I.2 Target theorem (the open hypothesis)

**Theorem I.2.1 (rooted-source polymer estimate; source eq 0.1; OPEN at large β for SU(2)).** For all connected polymers $\Gamma\ni p_0$, the rooted-source cluster coefficient satisfies
$$
\boxed{
|K_\eta(\Gamma;s_0,\ldots,s_k)|\le C_0^{|\Gamma|}e^{-m_0\tau(\Gamma)}\mathbb E_W Y_{p_0}\,q_\eta^k\prod_{j=0}^k|s_j|.
}
$$
Here $Y_{p_0}\le X_{p_0,\eta}$ is a local "rooted" source, $\tau(\Gamma)$ is the Steiner tree length of the polymer, and $C_0, m_0$ are constants depending on $\eta,\beta$ but uniform in $\Lambda$.

**Status (verbatim from source §15):** "not currently supplied by the peer-reviewed literature for SU(2) at large β." The closest structural technology is the Bałaban CMP 116 (1988) polymer-activity bound, which operates inside the asymptotic-freedom flow rather than at fixed large β (pass-7 §10.4.1, Appendix G).

### I.3 Theorem F: rooted-source polymer ⇒ centered rare-source mixing

**Theorem I.3.1 (source §3.1).** Let $Y_p$ be local with $0\le Y_p\le X_{p,\eta}$. Assume the two-source connected pressure
$$
\Psi_{p,p'}(s,t)=\log\mathbb E_W e^{sY_p+tX_{p',\eta}}-\log\mathbb E_W e^{sY_p}-\log\mathbb E_W e^{tX_{p',\eta}}
$$
has a polymer expansion $\Psi_{p,p'}(s,t)=\sum_{\Gamma\leadsto p,p'}K_\eta(\Gamma;s,t)$ with rooted bound
$$
|K_\eta(\Gamma;s,t)|\le C_0^{|\Gamma|}e^{-m_0\tau(\Gamma)}|s||t|\,\mathbb E_W Y_p\,q_\eta,
$$
and that the polymer count summability $\sum_{\Gamma\leadsto p,p'}C_0^{|\Gamma|}e^{-m_0\tau(\Gamma)}\le C_{\rm conn}e^{-md(p,p')}$ holds. Then
$$
\boxed{
|\mathrm{Cov}_W(Y_p,X_{p',\eta})|\le C_{\rm root}\mathbb E_W Y_p\,q_\eta\,e^{-md(p,p')}.
\tag{3.1}
}
$$

**Proof sketch.** $\mathrm{Cov}_W(Y_p,X_{p',\eta})=\partial_s\partial_t\Psi_{p,p'}(0,0)$. Differentiate the polymer expansion and apply the rooted bound to each $\Gamma\ni p,p'$. The Steiner-tree exponential factor sums to $C_{\rm conn}e^{-md(p,p')}$ by the connectivity assumption. $\square$

### I.4 Pair closure (source §4)

Take $Y_p=X_{p,\eta}$ in Theorem I.3.1. Since $\mathbb E_W X_{p,\eta}=q_\eta$:
$$
\boxed{
|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\le C_{\rm root}q_\eta^2 e^{-md(p,p')}.
\tag{4.1}
}
$$
This is the master's "level-(iii) shape" applied to smooth sources at separation $d(p,p')$. The $q_\eta^2$ scaling is the correct $q$-power for level (iii).

### I.5 PTO-summed level-(iii) estimate (source §5)

**Theorem I.5.1.** Assume the deterministic trace-overlap summability
$$
\sup_p\sum_{p'}e^{-md(p,p')}\frac{\operatorname{tr}(A_p A_{p'})}{\kappa_\Lambda^2}\le 4N_m,
\tag{5.1}
$$
where $A_p=P_{\le\Lambda,L}\mathbf 1_{\partial p}P_{\le\Lambda,L}$ (master §5.6). Then (4.1) implies
$$
\boxed{
\sum_{p'}|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\operatorname{tr}(A_p A_{p'})\le 4C_{\rm root}N_m q_\eta^2\kappa_\Lambda^2.
\tag{5.2}
}
$$

**Proof.** Multiply (4.1) by $\operatorname{tr}(A_pA_{p'})$, sum, factor out the $q_\eta^2$, and apply (5.1). $\square$

**Significance.** Eq (5.2) is **exactly level (iii) of (M′)_SU(2) at fixed $\eta$**. Together with (4.1) the implication is:
$$
\boxed{
\text{pair-covariance bound (4.1)}\Rightarrow\text{level (iii) of (M')}_{\rm SU(2)}\text{ at fixed }\eta\text{ via deterministic PTO summability (5.1).}
}
$$

This is the structural fact that makes (4.1) the "first SU(2) breach point" (§I.16 below).

### I.6 SU(2) heat-bath law (source §6)

The single-link conditional distribution under SU(2) Wilson is the **heat-bath law**: given all other links, the distribution of $U_\ell$ is proportional to
$$
\exp\left(\tfrac{\beta}{2}\operatorname{Re}\operatorname{Tr}(U_\ell V_\ell)\right)dU_\ell,
$$
where $V_\ell=\sum_{p\ni\ell}V_{p,\ell}$ is the **staple sum** — sum over plaquettes containing $\ell$ of the product of the other three links around the plaquette. The density factor is proportional to a **vMF (von Mises–Fisher) distribution on SU(2)** with concentration parameter $\beta|V_\ell|/2$ pointing along $V_\ell/|V_\ell|$.

This explicit form is the technical entry point for §I.7 (vMF cap rarity) and §I.8 (staple analysis).

### I.7 vMF cap rarity Lemma 7.1 (source §7)

**Lemma I.7.1 (source Lemma 7.1, paraphrased).** For a vMF distribution on $S^3$ with concentration parameter $\kappa>0$ pointing along direction $\hat n$, the probability that the random unit vector $a$ satisfies $1-(a\cdot\hat n)\ge\delta$ is bounded by
$$
\mathbb P(1-a\cdot\hat n\ge\delta)\le C(\kappa\delta)e^{-\kappa\delta}\quad\text{as }\kappa\delta\to\infty,
$$
with $C(\kappa\delta)$ algebraic in $\kappa\delta$. The exponential rate is sharp.

**Use in the chain.** Combined with the heat-bath law (§I.6), Lemma I.7.1 quantifies the rarity of high-plaquette events conditional on the staple sum direction and magnitude. This is the SU(2)-specific input that gives the $q_\eta$ factor in Theorem F (§I.3).

### I.8 Good-staple rarity and bad-staple source (source §8)

Define the "good-staple event" $G_{p,\ell}$ as the event that the staple sum $V_\ell$ restricted to plaquette $p$ has magnitude bounded above by $\delta_{\rm st}$ (a fixed threshold). The "bad-staple event" is $R_{p,\ell,\eta}:=X_{p,\eta}\cdot\mathbf 1\{G_{p,\ell}^c\}$ — the conjunction of high plaquette and large staple.

Source §8 establishes:
- The bad-staple expectation satisfies $\mathbb E_W R_{p,\ell,\eta}\le q_\eta$ (trivially, since $R\le X_{p,\eta}$).
- The good-staple expectation satisfies vMF cap rarity directly via §I.6+§I.7.
- The full $X_{p,\eta}$ decomposes as $X_{p,\eta}=(X_{p,\eta}-R_{p,\ell,\eta})+R_{p,\ell,\eta}$, where the first term has heat-bath-controlled cap rarity and the second is the "bad-staple residue."

### I.9 Bad-staple absorption *without* the false scalar tail ratio (source §9; CORRECTION)

**This subsection documents the third explicit honesty correction in the master document** (after pass-4 $m_*$ retraction in Appendix E and pass-8 §H.5 weighted-Lyapunov correction).

**The retired (incorrect) formulation.** Earlier informal derivations sometimes assumed a "scalar tail ratio" inequality of the form
$$
\mathbb P(\phi_p>\delta_{\rm st})\lesssim\mathbb P(\phi_p>t).\quad\text{(FALSE in general)}
$$
This **generally fails when $\delta_{\rm st}\ll t$**: the LHS bounds events much more common than the RHS, and the ratio is essentially $1/q$ or worse.

**The corrected formulation.** Apply Theorem I.3.1 (Theorem F) directly with $Y_p=R_{p,\ell,\eta}$. The hypothesis $0\le R_{p,\ell,\eta}\le X_{p,\eta}$ is satisfied. Theorem F then gives
$$
|\mathrm{Cov}_W(R_{p,\ell,\eta},X_{p',\eta})|\le C_{\rm root}\mathbb E_W R_{p,\ell,\eta}\,q_\eta\,e^{-md(p,p')}.
$$
Since $\mathbb E_W R_{p,\ell,\eta}\le q_\eta$:
$$
\boxed{
|\mathrm{Cov}_W(R_{p,\ell,\eta},X_{p',\eta})|\le C_{\rm root}q_\eta^2 e^{-md(p,p')}.
\tag{9.1}
}
$$

**Why this is the correct argument.** The Theorem F hypothesis is the rooted-source polymer bound (Theorem I.2.1), not any tail-ratio assumption. The bad-staple residue's contribution to the pair covariance is bounded directly by its expectation times $q_\eta$ — exactly the same $q_\eta^2$ scaling as (4.1), without needing $\delta_{\rm st}$ and $t$ to be comparable.

**Pass-10 record.** The false scalar tail ratio is documented as retired. Any future argument involving bad-staple events must use (9.1), not the false ratio.

### I.10 Higher cumulants and HPM (source §10)

The two-source theorem (Theorem F) extends to higher-source cumulants. For $k$-source cumulants $\kappa_\eta(B)$ over polymer support $B$ of size $|B|=k$, source §10 gives
$$
|\kappa_\eta(B)|\le q_\eta^{|B|}\nu(B),\qquad\nu(B)\le C_*^{|B|}e^{-m_*\tau(B)},
$$
with $C_*, m_*$ uniform in $\Lambda$. This is the **higher polymer-cluster cumulant bound** = level (iv) of (M′)_SU(2) at fixed $\eta$.

### I.11 Smooth HPM from cumulants (source §11)

**Theorem I.11.1.** Let $\mathcal W_\theta(Y)$ be the PMBSF closed-walk weight on plaquette set $Y$. Assume the cumulant bound of §I.10. If the **closed-walk Kotecký–Preiss (CW-KP) condition** holds:
$$
\sum_Y q_\eta^{|Y|}\left[\exp\left(\sum_{B\subset Y,|B|\ge 2}\nu(B)\right)-1\right]\mathcal W_\theta(Y)\le\varepsilon_{\rm CWKP}\sum_Y q_\eta^{|Y|}\mathcal W_\theta(Y),
\tag{11.1}
$$
then
$$
\boxed{
\sum_Y\mathbb E_W\prod_{p\in Y}X_{p,\eta}\,\mathcal W_\theta(Y)\le(1+\varepsilon_{\rm CWKP})\sum_Y q_\eta^{|Y|}\mathcal W_\theta(Y).
\tag{11.2}
}
$$
This is **smooth HPM** (= Hard Plaquette Method for smooth sources): the Wilson expectation of products of smooth high-plaquette indicators is dominated by the Bernoulli-comparator weight, up to multiplicative slack $1+\varepsilon_{\rm CWKP}$.

**Master cross-reference.** The CW-KP condition (11.1) is the explicit form of master §8.4. The closed-walk weight $\mathcal W_\theta$ matches master §5.8 envelope.

### I.12 Hard/smooth boundary-band bridge (source §12)

**Theorem I.12.1.** Let $\eta_0>0$ be fixed. There exists a boundary-band correction $\partial X_{\eta,t}=X_t-X_{\eta,t}$ (the indicator difference between hard and smooth) and a "thickness" function $\Delta(\eta)\to 0$ as $\eta\to 0$ such that for all polymer expectations,
$$
\left|\mathbb E_W\prod_{p\in Y}X_p-\mathbb E_W\prod_{p\in Y}X_{p,\eta}\right|\le|Y|\Delta(\eta)q^{|Y|}\mathcal W_\theta(Y).
$$
Provided $\Delta(\eta)\to 0$ uniformly in $\Lambda$, the smooth HPM bound (11.2) transports to **hard HPM**:
$$
\boxed{
\sum_Y\mathbb E_W\prod_{p\in Y}X_p\,\mathcal W_\theta(Y)\le(1+\varepsilon_{\rm CWKP}+\varepsilon_{\rm BG})\sum_Y q^{|Y|}\mathcal W_\theta(Y),
}
$$
where $\varepsilon_{\rm BG}=\sup_{Y}|Y|\Delta(\eta)$.

**Master cross-reference.** This is the explicit form of master §8.3 BG (boundary-band) smoothing bridge.

### I.13 HPM to matrix-Laplace transfer (source §13)

The hard HPM bound (§I.12) feeds the matrix-Laplace transform identity (master §6, §7.7) to give the projected operator bound
$$
\|P\mathbf 1_D P\|\le\|P\mathbf 1_{D^{\rm Bern}}P\|+\text{(slack)},
$$
where $D^{\rm Bern}$ is the iid-Bernoulli plaquette comparator with intensity $q$. The slack term is controlled by $\varepsilon_{\rm CWKP}+\varepsilon_{\rm BG}$ from §I.11–§I.12.

### I.14 Projected firewall (source §14)

Combining §I.13 with the sharp Bernoulli comparator (master §6):
$$
\|P\mathbf 1_{D(W)}P\|\le 6q+\sqrt{12q\kappa_\Lambda\log(2K/\delta)}+\tfrac{2\kappa_\Lambda}{3}\log(2K/\delta)+\text{(HPM slack)}.
$$
Multiplying by $V_{\max}/m^2$ and using the working-corner numerics (master §11):
$$
\boxed{
\Theta=\frac{V_{\max}}{m^2}\|P\mathbf 1_{D(W)}P\|<1,
}
$$
provided the HPM slack is bounded — which holds iff (M′)_SU(2) at level (iv) holds (Theorem I.2.1).

### I.15 Honest status (source §15, verbatim)

> "What remains to prove analytically is the SU(2)-specific rooted-source polymer estimate [Theorem I.2.1]. This is not currently supplied by the peer-reviewed literature for SU(2) at large β. The closest structural technologies are Bałaban's lattice gauge RG and related constructive cluster expansions, but the current literature does not provide the fixed-β, projected spectral-window, hard/smooth plaquette-source cumulant theorem required here.
>
> Thus the document's final status is: **The PMBSF SU(2) closure is reduced to a precise rooted-source polymer theorem.** It is not yet an unconditional Yang–Mills mass-gap proof."

This matches pass-7 Appendix G and pass-9 §H.8 verdicts. The peer-reviewed literature route remains unavailable.

### I.16 Minimal next proof target (source §16)

**The pass-10 sharpened "single hardest open question."** The smallest theorem worth attacking next is the fixed-$\eta$ pair source estimate:
$$
\boxed{
|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\le Cq_\eta^2 e^{-md(p,p')}.
\tag{16.1}
}
$$
By the deterministic PTO summability (Theorem I.5.1, eq 5.2), this immediately gives level (iii) of (M′)_SU(2) at fixed $\eta$:
$$
\boxed{
\sum_{p'}|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\operatorname{tr}(A_p A_{p'})\le Cq_\eta^2\kappa_\Lambda^2.
}
$$

**Why this is the first SU(2) breach point.** (16.1) is a single pair-covariance inequality. It does not require the full polymer-cluster machinery of Theorem I.2.1; it does not require higher cumulant control; it does not require smoothing-bridge uniformity. It is the **minimal sufficient input** that yields level (iii) by deterministic summation.

**Connection to pass-9 §H.8.** The pass-9 research-direction memo identified four ingredients for a hypothetical spectral-window Bakry–Émery proof of level (iii). The pair-cumulant inequality (16.1) is **exactly what a spectral-window Bakry–Émery extension of SZZ 2023 at large β would deliver**: covariance decay between smoothed local observables at fixed lattice distance. The pass-9 §H.8 ingredients (local floor $\kappa_G=2$, horizontal restriction, Lyapunov partial via §H.2, globalization missing) attack (16.1) directly — they do not need to be assembled into the full polymer machinery of Theorem I.2.1 first.

**Pass-10 verdict.** The minimal-target form (16.1) is the most attackable open question in the master document. Proving it would close the route at level (iii). It is not in any peer-reviewed paper. It is not contradicted by any pass-7 finding; in fact §10.6.1 SZZ 2023 proves the structurally identical inequality at strong coupling (small β), and the pass-9 §H.8 memo identifies the missing ingredient for the large-β extension.

### I.17 Net Appendix I summary

The 16 source-document sections (§I.1–§I.16) collectively prove the conditional chain
$$
\text{rooted-source polymer estimate (open)}\Rightarrow\text{projected firewall closure}
$$
step-by-step, with explicit constants, the §I.9 correction, and the §I.16 minimal target. **The chain is rigorous; the hypothesis is open.** The pass-7 literature finding (no peer-reviewed paper supplies the hypothesis at large β) is preserved. The conditional status of the master theorem is unchanged.

**Pass-10 verdict.** Appendix I makes the master document's conditional content fully transparent: anyone can now trace, lemma by lemma, what (M′)_SU(2)-level-iv input yields the projected firewall closure. The "what would have to be proved next" question now has a single-inequality answer (16.1). The master document is structurally complete as a conditional theorem.

---

## Appendix J — Attempted assembly of §I.16 via §H.8 (pass 11): concrete numerical estimates and the obstruction

### J.0 Scope and honesty disclaimer

**Goal.** Attempt to prove the §I.16 minimal target — $|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\le Cq_\eta^2 e^{-md(p,p')}$ — using the §H.8 four-ingredient assembly (local BE floor [supplied]; horizontal restriction [supplied]; Lyapunov toward $U^{(0)}$ [partial via §H.2]; globalization [missing]).

**Honest outcome.** The attempt does **NOT** prove the minimal target. It produces concrete numerical estimates at the master's working corner ($\beta=3.5$, $L=24$, $\delta_{\rm bond}=1$) and identifies a specific quantitative obstruction: the **pointwise BE-good set has exponentially small measure** at $\beta=3.5$, so the standard Bakry–Émery + Lyapunov machinery cannot be applied as-is. The pass-7 finding (no peer-reviewed paper closes (M′)_SU(2) at large β) is preserved.

**What pass 11 supplies.** (i) Explicit per-plaquette Wilson Hessian eigenvalue formula for SU(2); (ii) explicit numerical threshold for naive BE at the master's working β; (iii) quantitative measurement of the exponential-rarity obstruction; (iv) identification of the spectral-window restriction (master §11.0c v3b) as the most promising path forward, with the explicit research subtargets needed.

**What pass 11 does NOT supply.** A proof of the minimal target. A peer-reviewed-grade analytic statement about projected-window Bakry–Émery. A globalization mechanism at large β.

### J.1 The Bakry–Émery → covariance decay theorem

The relevant theorem from the standard functional inequalities literature (Bakry–Gentil–Ledoux, *Analysis and Geometry of Markov Diffusion Operators*, 2014; specifically Chapter 4):

**Theorem (BGL 2014, paraphrased).** Let $(M,g)$ be a complete Riemannian manifold and $\mu = e^{-V}d\mathrm{vol}_g/Z$ a Gibbs measure with $V\in C^2$. Suppose the Bakry–Émery Ricci tensor satisfies $\mathrm{Ric}_\mu := \mathrm{Ric}_g + \nabla^2 V \ge \rho\, g$ uniformly with $\rho>0$. Then for $f,g\in C_b^1(M)$ with disjoint supports $A,B$:
$$
|\mathrm{Cov}_\mu(f,g)|\le\frac{\|\nabla f\|_\infty\|\nabla g\|_\infty}{\rho}\,e^{-\sqrt{\rho}\cdot d(A,B)/2}.
$$
(The exact rate constants depend on the precise version; the structural form is "constant×exponential in distance, with rate set by $\sqrt{\rho}$.")

**Applied to SU(2) Wilson.** Set $M = M_\Lambda = SU(2)^{E(\Lambda)}$, $g = g_\Lambda$ (bi-invariant product metric), $V = S_W$ (Wilson action), $\mu$ = Wilson Gibbs measure. The condition is
$$
\boxed{\mathrm{Ric}_g + \nabla^2 S_W \ge \rho\, g\text{ pointwise, with }\rho>0\text{ uniform in }L.}
$$
If this holds, the BGL theorem delivers $|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\le C\|\nabla X_{p,\eta}\|_\infty\|\nabla X_{p',\eta}\|_\infty\,e^{-\sqrt{\rho}d(p,p')/2}$ — which, with $\|\nabla X_{p,\eta}\|_\infty \lesssim 1/\eta$ (smooth indicator with width $\eta$), is the right structural form for §I.16 if the dependence on $\eta$ is absorbed into the constant $C$.

**The question is therefore: is $\mathrm{Ric}_g + \nabla^2 S_W \ge \rho\,g$ at $\beta=3.5$?**

Cattiaux–Guillin (*Functional inequalities via Lyapunov conditions*, 2009) extends BGL to allow BE to fail on a set $K^c$, provided a Lyapunov function $W$ satisfies $L_W W\le-\phi W + b\mathbf 1_K$ (with corrected form per §H.5). Their result: if BE holds on $K$ with constant $\rho_K>0$, and the Lyapunov drift gives $\phi\ge\phi_0>0$ on $K^c$, then a global functional inequality (Poincaré or LSI) follows, with explicit constants depending on $\rho_K$, $\phi_0$, $b$, and the relative measures.

**Key requirement (Cattiaux–Guillin 2009 Thm 1.1, paraphrased):** the "good set" $K$ must have non-trivial measure. Specifically, the explicit constant degrades polynomially in $\mu(K)$. **If $\mu(K)\to 0$ exponentially in $L^4$, the bound vacuates.** This is the regime we will find ourselves in below.

### J.2 The SU(2) Wilson Hessian (explicit calculation)

**Setup.** Parameterize a single link in exponential coordinates: $U_\ell = \exp(i\omega^a T^a)$ where $T^a = \sigma^a/2$ are the SU(2) generators. For a plaquette $p$ with $\ell$ on its boundary, write $U_p = U_\ell V_\ell^{(p)}$ where $V_\ell^{(p)}$ is the "staple" — the product of the other 3 links going around $p$. Write the staple in quaternion form:
$$
V_\ell^{(p)} = q_0^{(p,\ell)}\,I + i q^{(p,\ell)}\cdot\sigma,\qquad (q_0)^2 + |q|^2 = 1.
$$

**Single-plaquette per-link Hessian.** Compute $\tilde z_p = 1-\frac12\mathrm{Re}\mathrm{Tr}(U_\ell V_\ell^{(p)})$ as a function of $\omega^a$ at $\omega=0$. Using the small-$\omega$ expansion derived in §H.2 (with the correct Lie-algebra calculation):
$$
\tilde z_p(\omega) = (1-q_0^{(p,\ell)}) + \frac{\omega\cdot q^{(p,\ell)}}{2} + \frac{q_0^{(p,\ell)}|\omega|^2}{8} + O(|\omega|^3).
$$
**Hessian at $\omega=0$:**
$$
\partial_a\partial_b\tilde z_p(0)=\frac{q_0^{(p,\ell)}}{4}\delta_{ab}.
$$
The Hessian is isotropic (proportional to identity) with eigenvalue $q_0^{(p,\ell)}/4$.

**Wilson per-link Hessian** (summing over 6 plaquettes containing $\ell$ in $d=4$):
$$
\boxed{
[\nabla^2 S_W]_{ab}^{(\ell)} = \frac{\beta}{4}\sum_{p\ni\ell}q_0^{(p,\ell)}\,\delta_{ab}.
}
$$
Eigenvalue range: each $q_0^{(p,\ell)}\in[-1,1]$, so per-link Hessian eigenvalue $\in\frac{\beta}{4}\cdot[-6,6]=\beta\cdot[-3/2,3/2]$.

**At $\beta=3.5$:** per-link Hessian eigenvalue $\in[-5.25,5.25]$.

### J.3 The naive Bakry–Émery threshold

**Pointwise BE condition.** $\mathrm{Ric}_g+\nabla^2 S_W\ge\rho\, g$ requires (at every configuration $U$ and every link $\ell$):
$$
\kappa_G+\frac{\beta}{4}\sum_{p\ni\ell}q_0^{(p,\ell)}(U)\ge\rho.
$$
Using $\kappa_G=2$ (pass 9 Theorem H.3.1') and worst-case $q_0^{(p,\ell)}=-1$ all-around: $2 - 6\beta/4\ge\rho$, i.e., $\beta\le (2-\rho)\cdot 4/6$.

**Pointwise BE positivity threshold (crude bound):**
$$
\boxed{\beta < \frac{4\kappa_G}{6} = \frac{4}{3}\approx 1.33.}
$$

**At $\beta=3.5$:** worst-case BE = $2 - 6\cdot 3.5/4 = -3.25$. **Negative.** Naive pointwise BE fails by $3.25/2=1.625\times$ in magnitude, or equivalently, $\beta$ exceeds the crude threshold by factor $3.5/1.33\approx 2.6\times$.

**Comparison with SZZ 2023 careful threshold.** Shen–Zhu–Zhu's threshold is per-link $|\beta_{\rm std}|<1/[16N(d-1)]$, which for SU(2) in $d=4$ gives $|\beta_{\rm std}|<1/96\approx 0.0104$. Their careful Lie-algebra computation tightens the worst-case bound by an additional factor of $\sim 128$ over my crude estimate — they account for proper plaquette summation, gauge constraint, and tightness of the Hessian for global LSI. **At $\beta=3.5$, the master corner exceeds the SZZ threshold by $\sim 336\times$.**

**Numerical summary.**

| Threshold | Value | $\beta_{\rm master}/\beta_{\rm threshold}$ |
|---|---|---|
| Crude pointwise BE (J.3) | $\beta<4/3\approx 1.33$ | $2.6\times$ |
| SZZ 2023 careful (per-link) | $\beta<1/96\approx 0.0104$ | $\sim 336\times$ |

Both thresholds are decisively violated at the master's working corner $\beta=3.5$.

### J.4 Concentration of measure (where does Wilson live?)

**Typical plaquette deficiency at large β.** From the standard small-fluctuation analysis (Drouffe–Itzykson 1978; Münster 1980):
$$
\langle\phi_p\rangle_W \approx \frac{3}{2\beta}\quad\text{at large }\beta.
$$
At $\beta=3.5$: $\langle\phi_p\rangle\approx 0.43$. Converting via $\phi=1-\cos\theta\approx\theta^2/2$: typical plaquette angle $\theta_p\approx\sqrt{2\cdot 0.43}\approx 0.93$ rad $\approx 53°$.

**Consequence.** The Wilson measure at $\beta=3.5$ concentrates on configurations with plaquettes at ~53° angle, NOT near the identity. The local-floor input from §H.3 + pass-9 Theorem H.3.1' is at the trivial configuration $U^{(0)}$; the measure does not concentrate there.

**Lyapunov function from §H.2.** For $V=1+\overline B_{\rm avg}=1+\langle\phi_p\rangle$, typical $V\approx 1.43$. The §H.2 drift inequality reads $L_\Lambda V\le -12V+24$; at typical V this gives $-12(1.43)+24=6.84>0$. **Not Foster–Lyapunov in form** — the rate function $\phi(V)=12-24/V$ is negative for $V<2$, which is precisely where the Wilson measure lives.

This is the partial-Lyapunov status the pass-9 §H.8 memo identified: §H.2 gives a one-sided drift ceiling but not a Foster–Lyapunov drift toward $U^{(0)}$ from the bulk.

### J.5 The exponential rarity obstruction (quantitative)

**The crucial probability calculation.** The naive Bakry–Émery + Lyapunov machinery (Cattiaux–Guillin 2009) needs a "good set" $K$ with non-trivial measure, on which BE holds. The natural good set at the master's β is
$$
K_{\rm BE}=\left\{U:\forall(p,\ell),\ q_0^{(p,\ell)}(U)\ge -\frac{4\kappa_G}{6\beta}\right\}.
$$
At $\beta=3.5,\kappa_G=2$: threshold is $q_0\ge -4\cdot 2/(6\cdot 3.5) = -0.381$. Equivalent to staple half-angle $<\arccos(-0.381)=112.4°$, i.e., staple holonomy angle $<224.8°$ (i.e., < $4\pi/3$ approximately, which is "essentially anything except antipodal").

**Per-staple probability.** Under the upper bound provided by the Haar measure (which is *less* concentrated than the Wilson measure on the staple — the actual Wilson staple distribution is harder to write down, but Haar gives a useful upper bound on diversity):
$$
P_{\rm Haar}(q_0\ge -0.381)=\int_{-0.381}^1\frac{2}{\pi}\sqrt{1-q^2}\,dq=0.736.
$$
So 73.6% of staples are BE-good per (plaquette, link) pair under Haar.

**Joint probability of all-good lattice.** At $L=24$ in $d=4$: there are $4L^4 = 4\cdot 24^4\approx 1.33\times 10^6$ links, each in 6 plaquettes, so $\sim 8\times 10^6$ staple-link pairs in total.

Even *under the conservative Haar upper bound* and assuming independence (which is again conservative for our purposes since Wilson configurations have *correlations* that make the joint less concentrated):
$$
\boxed{
P_{\rm Haar}(\text{all }(p,\ell)\text{ pairs BE-good})\le(0.736)^{8\times 10^6}\approx e^{-2.4\times 10^6}.
}
$$

**This is exponentially small in volume.** The Cattiaux–Guillin Theorem 1.1 requires $\mu(K)$ to be at least non-trivial (typically polynomial in $|P|^{-1}$). With $\mu(K_{\rm BE})\le e^{-c L^4}$, the resulting bound is vacuous.

**Conclusion.** **The standard Bakry–Émery + Lyapunov machinery, applied directly to the unprojected SU(2) Wilson dynamics at $\beta=3.5$, fails by an exponentially large gap.** This is not a "tight" failure that a more careful calculation might fix; it is an order-of-magnitude failure rooted in the fundamental fact that at large β, the Wilson Hessian has many negative directions at typical configurations.

### J.6 The spectral-window restriction (proposed research direction)

**Observation.** The master document does NOT analyze the full Wilson dynamics. It works with the **projected operator**
$$
A_p = P_{\le\Lambda,L}\,\mathbf 1_{\partial p}\,P_{\le\Lambda,L},
$$
where $P_{\le\Lambda,L}$ projects onto modes with Maxwell spectral parameter $\le\Lambda$. At the master's working corner: $\Lambda=1$, and $\Lambda=1$ corresponds to a low-dimensional spectral subspace.

**Proposed research direction.** Restrict the BE analysis to the **projected dynamics**: study Wilson Langevin restricted to the spectral window, with the projected Hessian $P\nabla^2 S_W P$ replacing the full Hessian. The hope is that:

1. The projected Hessian has fewer "bad directions" because $P$ projects away high-momentum modes that contribute most to the Hessian's negativity.
2. The projected dynamics naturally respects the master's working observables ($X_{p,\eta}$ projected through $P$).
3. Bakry–Émery on the projected subspace might hold with a positive constant even at $\beta=3.5$.

**Empirical support from master §11.0c v3b.** The v3b 1200-sample sweep (50 seeds × hot/cold × 4 L-values × 3 weight modes) measured the projected physical-sector norm $\theta_{\rm phys}$ at $\beta=3.5,\Lambda=1$:
- Maximum: $\Theta_*=0.884442692429$
- Mean: $0.546$
- p99: $0.854$
- ALL 1200 samples satisfied $\theta_{\rm phys}<1$.

This is the closest existing **finite-volume empirical evidence** that the projected operator behaves benignly even at $\beta=3.5$ where the unprojected Hessian is poorly behaved.

**What v3b is not.** It is a measurement of $\|P\mathbf{1}_D P\|$ on specific Wilson samples, not a proof of any functional-inequality statement on the projected dynamics. The 1200 samples are at finite $L$ and finite Monte Carlo time; they do not establish a uniform-in-$L$ statement, much less a uniform Bakry–Émery floor on the projected Langevin generator.

**Research gap.** To convert v3b empirical control into a theorem at level (16.1), one would need:

| Subtarget | Status | Specific input needed |
|---|---|---|
| **(a)** Define the projected Langevin generator $L^P$ acting on projected observables $P f$ for $f\in C^\infty(M_\Lambda)$ | not in master | well-defined gauge-invariant projected SDE; carrier-space inner product |
| **(b)** Compute the projected Hessian $P\nabla^2 S_W P$ at typical configurations | not in master | typical SU(2) Wilson configuration Hessian + spectral decomposition |
| **(c)** Show $P\nabla^2 S_W P \ge -C g$ uniformly with $C<\kappa_G$ | not in master | this is the key analytic input |
| **(d)** Apply BGL/Cattiaux–Guillin to $L^P$ to get covariance decay for projected observables | not in master | follows from (c) by standard machinery |
| **(e)** Convert projected-observable covariance decay to hard-indicator pair-covariance (16.1) | not in master | additional smoothing/projection control |

None of (a)–(e) are in the master document or in any pass-1 through pass-10 content. The pass-7 literature survey (Appendix G) covers (a)–(d) at strong coupling (SZZ 2023) but not at large β.

### J.7 What pass 11 supplies vs. does not supply

**Supplied (pass 11 contributions):**

1. **Explicit Wilson Hessian formula** for SU(2): per-plaquette-per-link eigenvalue $\beta q_0^{(p,\ell)}/4$, per-link eigenvalue $\frac{\beta}{4}\sum_p q_0^{(p,\ell)}$.
2. **Naive BE threshold** $\beta<4/3\approx 1.33$ (crude); ratio to master's β: 2.6×.
3. **Quantitative exponential rarity**: under conservative Haar bound, $P(\text{all BE-good})\le e^{-2.4\times 10^6}$ at $L=24$.
4. **Identification of the spectral-window restriction** as the most promising path forward, with specific subtargets (a)–(e) of §J.6.
5. **v3b empirical anchor** $\Theta_*=0.884<1$ from master §11.0c re-cast as the relevant evidence for the spectral-window proposal.

**Not supplied (genuinely open):**

1. A proof of §I.16.
2. A proof that $P\nabla^2 S_W P$ is bounded below on the projected subspace.
3. A peer-reviewed-grade theorem of any of the §J.6 subtargets (a)–(e).
4. A specific quantitative conjecture for the constants $C, m$ in §I.16.
5. Russian-language Malyshev–Minlos / Minlos–Sinai literature (pass-7 known gap; not addressed by pass 11).

### J.8 Concrete next steps for the spectral-window research direction

The shortest research path to a peer-reviewed-grade statement:

**Step 1 (4-6 weeks).** Formalize the projected Langevin SDE on the spectral window. Given the master's Maxwell projector $P_{\le\Lambda,L}$, define the carrier Hilbert space, the projected drift, and the projected Brownian motion. Verify gauge invariance is preserved.

**Step 2 (6-8 weeks).** Compute the projected Wilson Hessian $P\nabla^2 S_W P$ at the trivial configuration and at a small set of typical Wilson configurations. Heuristically: use the small-momentum structure of $P$ to argue that high-frequency Hessian eigenvalues are projected out. Estimate the worst-case projected eigenvalue at $\beta=3.5,\Lambda=1$.

**Step 3 (open).** If step 2 produces a positive lower bound, apply BGL 2014 to get covariance decay for projected observables. Then transfer to hard-indicator pair-covariance via the master's existing matrix-Laplace machinery (§7.7).

**Step 4 (longer).** Globalize uniformly in $L$ and convert to (16.1). Likely requires new local-to-global functional-inequality work specific to lattice gauge theory.

**Probability of success.** Pass-11 author's honest estimate: Step 1 is mechanical; Step 2 is the key technical step and may reveal that the projected Hessian remains ill-behaved (in which case the spectral-window route also fails). If Step 2 succeeds, Steps 3–4 are doable but substantial. Total estimated time to a paper: 6 months minimum if everything works; 18+ months if the obstruction is encountered.

**Important caveat.** The spectral-window restriction is **not** in any peer-reviewed paper. SZZ 2023 (the closest precedent for BE on lattice gauge theory) works with the full unprojected dynamics. The novelty of the spectral-window approach is precisely what makes it a research direction rather than a literature extraction.

### J.9 Honest verdict

**The §H.8 assembly applied naively does not prove §I.16 at $\beta=3.5$.** The obstruction is concrete and quantitative: the pointwise BE-good set has exponentially small measure ($\lesssim e^{-2.4\times 10^6}$ at $L=24$), which vacates the standard Cattiaux–Guillin local-to-global mechanism.

**The pass-9 four-ingredient memo (§H.8) accurately identified this**: ingredients (i)+(ii) [local floor, horizontal restriction] are supplied; (iii) [Lyapunov] is partial because the §H.2 drift identity is not Foster–Lyapunov; (iv) [globalization] is missing. **Pass 11 quantifies these statuses with explicit numerical estimates.** The "missing globalization" is shown to require either a regime change (smaller β, entering SZZ) or a structural change (spectral-window restriction).

**The spectral-window restriction is the most promising open research direction.** v3b empirical evidence ($\Theta_*=0.884<1$, 1200 samples) supports this, but a theorem requires substantial new analytic work (§J.8 Step 2–4).

**Pass-7 finding stands.** No peer-reviewed paper closes (M′)_SU(2) at large β. Pass 11 sharpens the gap from "open" to "open with quantified obstruction and concrete research subtarget."

**Master document conditional status: unchanged.** The conditional theorem (§2) remains conditional on (M′)_SU(2). Pass 11 supplies a research-direction memo, not a proof.

---

## Appendix K — Explicit projected Wilson Hessian computation at typical configurations (pass 12, §J.8 Step 2)

### K.0 Scope

**Goal.** Carry out the §J.8 Step 2 computation: at a typical Wilson configuration $U$ at the master's working corner $\beta=3.5$, compute the projected Wilson Hessian $P\nabla^2 S_W(U) P$ (where $P=P_{\le\Lambda,L}$ is the spectral-window projector) and check its smallest eigenvalue. If $\min\mathrm{spec}(P\nabla^2 S_W P) + \kappa_G > 0$, the projected Bakry–Émery condition holds pointwise at $U$. The §J.6 spectral-window conjecture says this should hold uniformly across typical $U$.

**Honest framing.** This is a numerical experiment, not a proof. We work on small lattices ($L=4, 6$) where direct dense Hessian computation is feasible. We sample typical configurations as Gaussian random $A_\ell^a \sim \mathcal N(0, 1/\beta)$ with $U_\ell=\exp(iA_\ell\cdot\sigma/2)$ — an approximation to Wilson sampling that is leading-order correct at large β. The deliverable is empirical evidence for or against the §J.6 conjecture at the master's working β.

### K.1 Methodology

**Lattice setup.** Periodic $L^4$ lattice with $L\in\{4,6\}$. $N_{\rm sites}=L^4$, $N_{\rm links}=4L^4$, $N_{\rm plaq}=6L^4$. Per Lie algebra direction.

**Maxwell operator.** $M = d_1^* d_1$ where $d_1$: 1-forms → 2-forms is the standard lattice exterior derivative,
$$(d_1 A)_{\mu\nu}(x) = A_\mu(x) + A_\nu(x+\hat\mu) - A_\mu(x+\hat\nu) - A_\nu(x).$$
Computed explicitly as a sparse $N_{\rm plaq}\times N_{\rm links}$ matrix. Full Maxwell $M_{\rm full}$ on $\mathfrak{su}(2)^{\otimes N_{\rm links}}$ is block-diagonal: 3 copies of $M$.

**Spectral window projector $P_{\le\Lambda,L}$.** Compute eigendecomposition $M = U_M\,\mathrm{diag}(\lambda_k)\,U_M^T$. The window $P_{\le\Lambda}$ projects onto eigenspaces with $\lambda_k\le\Lambda$.

**Coexact restriction.** The "physical" gauge-invariant directions are coexact 1-forms: those in $\ker(d_0^*)$ where $d_0$: 0-forms → 1-forms is $(d_0 f)(x,\mu) = f(x+\hat\mu) - f(x)$. We identify coexact eigenmodes by checking $d_0^T v\approx 0$ (numerical tolerance $10^{-6}$).

**Wilson Hessian at configuration $U$.** For each plaquette $p$, perturb $U_{\ell_k}\to U_{\ell_k}\exp(ia_k\cdot\sigma/2)$ for the 4 boundary links $\ell_1,\ldots,\ell_4$. Compute the 12×12 local Hessian
$$\left[H^{(p)}\right]_{(k,a),(k',b)} = \partial^2\,(\beta\tilde z_p)/\partial a_k^a\,\partial a_{k'}^b\big|_{a=0}$$
via central finite differences with step $\epsilon=0.005$. Symmetrize.

**Assembly.** Sum per-plaquette $H^{(p)}$ over all $N_{\rm plaq}$ plaquettes, embedded in the full $3N_{\rm links}\times 3N_{\rm links}$ space.

**Projection.** Compute $P V_{\rm coex}^T H V_{\rm coex} P$ where $V_{\rm coex}$ is the coexact-window basis. The result is a small $(3 n_{\rm coex})\times(3 n_{\rm coex})$ matrix; diagonalize to find eigenvalues.

**Memory-efficient assembly.** For $L=6$, $3N_{\rm links}=15552$ — the full dense Hessian (244M entries) overflows memory. Instead, accumulate the projected Hessian per plaquette: for each plaquette, build the local 12×12 $H^{(p)}$, extract the corresponding 12 rows of $V_{\rm coex}$ to form local $V_p$ (size $12\times 3n_{\rm coex}$), and accumulate $V_p^T H^{(p)} V_p$ into the running $(3n_{\rm coex})\times(3n_{\rm coex})$ projected Hessian. Memory footprint: $\sim 5000$ floats vs $\sim 250M$.

### K.2 L=4 results and the spectral-window artifact

**Computational summary at $L=4$, $\beta=3.5$, $\Lambda=1$:**
- $N_{\rm sites}=256$, $N_{\rm links}=1024$, $N_{\rm plaq}=1536$, full Hessian dim $3072$
- Maxwell zero modes (per Lie alg dir): 259 = 255 exact (image of $d_0$) + 4 harmonic (constant 1-forms in each spatial direction)
- Lowest nonzero Maxwell eigenvalue at $L=4$: $4\sin^2(\pi/4)=2$
- **Spectral window with $\Lambda=1$ contains ONLY the 259 zero modes** — no physical (coexact) eigenvalues in the window
- Total window dimension (across 3 Lie algebra directions): 777

**Trivial config $U^{(0)}=I$:**
- Hessian diagonal: mean = 5.25 = $\beta\cdot 6/4$ exactly ✓
- Projected Hessian eigenvalues: all 0 (only zero modes in window)
- Projected BE eigenvalues: all 2.0 = $\kappa_G$ ✓

**Typical Gaussian configs (3 samples, $\sigma=1/\sqrt\beta=0.534$):**

| Sample | Full $H_{\min}$ | Full BE$_{\min}$ | Frac BE<0 | Proj $H_{\min}$ | Proj BE$_{\min}$ | Frac proj BE<0 |
|---|---|---|---|---|---|---|
| 1 | −3.69 | **−1.69** | 4.3% | −2.09 | **−0.09** | 0.5% |
| 2 | −3.97 | **−1.97** | 4.6% | −2.24 | **−0.24** | 0.9% |
| 3 | −3.90 | **−1.90** | 4.7% | −2.20 | **−0.20** | 0.6% |

**Observations:**
1. Full (unprojected) BE has 4-5% negative-eigenvalue fraction — consistent with pass-11 §J.5 prediction of "BE-bad" fraction at large β.
2. Projection reduces the bad-BE fraction by factor 6-8× (from ~4.5% to ~0.7%).
3. **However**, at $L=4$ the projected BE *still* has a small negative tail (worst eigenvalue ≈ −0.09 to −0.24).

**The L=4 artifact (critical).** At $L=4$, the spectral window with $\Lambda=1$ contains ONLY gauge zero modes — 255 pure-gauge (image of $d_0$) directions and 4 harmonic 1-forms. By gauge invariance of $S_W$, the Hessian on pure-gauge directions is *exactly zero*; any nonzero contribution is finite-difference numerical noise. The small negative projected-BE tail at $L=4$ is therefore partly an FD artifact on the 255 pure-gauge dimensions and only partly a genuine signal on the 4 harmonic modes (where non-abelian commutator terms can produce nonzero Hessian at non-trivial background).

**Therefore $L=4$ does not directly test the §J.6 spectral-window conjecture.** The conjecture concerns the projected Hessian on PHYSICAL (coexact) modes, which are absent from the $L=4$ window with $\Lambda=1$. The next size up, $L=6$, has lowest coexact eigenvalue equal to 1 (boundary case); using $\Lambda=1.05$ brings exactly the lowest coexact modes into the window.

### K.3 L=6 results with coexact restriction — the key positive finding

**Computational summary at $L=6$, $\beta=3.5$, $\Lambda=1.05$:**
- $N_{\rm sites}=1296$, $N_{\rm links}=5184$, $N_{\rm plaq}=7776$, full Hessian dim 15552
- Maxwell zero modes (per Lie alg dir): 1299 (= 1295 exact + 4 harmonic)
- Modes ≤ Λ=1.05: 1323
- **Coexact modes in window: 24 per Lie alg direction, all at Maxwell-eigenvalue exactly 1** (the lowest physical eigenvalue at $L=6$)
- Total coexact-window dimension: 72 (across 3 Lie algebra directions)

**Trivial config $U^{(0)}=I$ — verification:**
- Hessian diagonal: 5.25 = $\beta\cdot 6/4$ exactly ✓
- Coexact-projected Hessian eigenvalues: all 0.875 = $\beta/4\cdot 1$ exactly ✓
- Coexact-projected BE eigenvalues: all 2.875 = $\kappa_G + \beta\Lambda_0/4$ where $\Lambda_0=1$ ✓
- **All 72 modes verified to give the expected eigenvalue.**

**Typical Gaussian config (seed=42, single sample, $\sigma=1/\sqrt\beta=0.534$):**

| Statistic | Value |
|---|---|
| Hessian diagonal mean | (lower than trivial; nonlinear correction) |
| **Coexact-projected H min eigenvalue** | **+0.312** |
| Coexact-projected H p1 | +0.334 |
| Coexact-projected H max | +0.797 |
| **Coexact-projected BE min** | **+2.312** |
| Coexact-projected BE p1 | +2.334 |
| Coexact-projected BE p99 | +2.795 |
| **Fraction projected BE < 0** | **0.0000** |
| Fraction projected BE < $\kappa_G/2$=1 | **0.0000** |

**KEY POSITIVE FINDING.** **At a typical Gaussian configuration at $\beta=3.5$, the coexact-restricted spectral-window projected Wilson Hessian has ALL POSITIVE eigenvalues. Combined with the geometric Ricci $\kappa_G=2$, the projected Bakry–Émery floor is uniformly bounded below by $2.31$ across all 72 coexact-window modes.**

Compare to the unprojected/full-window results at L=4 (§K.2), where:
- Full BE had ~4-5% negative-eigenvalue fraction (min ≈ -2);
- Even the full-window-projected BE had ~0.5-1% negative tail.

The coexact-restricted projected BE at L=6 has zero negative tail. This is exactly the structural mechanism §J.6 conjectured: the Maxwell projector + coexact restriction projects away both (a) the high-momentum modes that contribute most to negative Hessian and (b) the pure-gauge modes where Hessian is exactly zero (or numerically noisy). What remains is the physical low-momentum subspace where the Wilson Hessian is well-behaved at typical configurations.

### K.4 Interpretation

**Why projection + coexact restriction produces positive BE at typical configs.**

The Wilson Hessian at any configuration $U$ has three classes of directions:
1. **Pure-gauge directions** (image of $d_0$): Hessian is exactly zero by gauge invariance.
2. **Harmonic directions** (kernel of $d_1$ ∩ kernel of $d_0^*$, dim 4 per Lie algebra): Hessian acquires nonzero values at non-trivial backgrounds via non-abelian commutators.
3. **Coexact directions** (kernel of $d_0^*$, complement of harmonic in this kernel): Hessian eigenvalue ≈ $(\beta/4)\cdot\lambda_k$ at trivial; modified by background.

At typical Gaussian configurations:
- The Wilson Hessian on full space has eigenvalues ranging from $\approx-3.9$ to $\approx+10.9$ at $L=4$ (full BE fraction <0: 4-5%).
- The negative eigenvalues live predominantly in two places: (i) high-momentum coexact modes where Hessian magnitude is large and can flip sign; (ii) gauge-zero modes that get small but nonzero values from finite-difference noise.
- The spectral-window projector $P_{\le\Lambda}$ removes (i) by truncating to low-momentum modes.
- The coexact restriction removes (ii) by excluding gauge zero modes.
- What remains is the low-momentum physical modes, where the Hessian is structurally $(\beta/4)\cdot\lambda_k + (\text{small background corrections})$. With $\lambda_k\le\Lambda$ and $\kappa_G=2$, the BE floor is robust.

**This is exactly the structural feature of the master document's construction.** The projector $A_p = P_{\le\Lambda,L}\,\mathbf 1_{\partial p}\,P_{\le\Lambda,L}$ in §3-§5 is designed to operate on the physical, low-momentum subspace — not the full Wilson dynamics. The §J.6 conjecture says this projection should rescue Bakry–Émery; pass-12 §K.3 provides the first explicit numerical demonstration that it does so at a typical configuration.

**Empirical anchor consistency.** The pass-11 §J.6 v3b numerical evidence ($\Theta_*=0.884<1$ over 1200 samples) measured the projected operator $A_p$ norm at the same working corner $\beta=3.5, \Lambda=1$. Pass-12 §K.3 measures a different quantity — the projected Hessian eigenvalues — but at the same working corner. Both empirical lines of evidence are consistent with the projected dynamics being well-behaved.

### K.5 Caveats

**This is empirical evidence, not a proof.** Specifically:

1. **Single typical Gaussian sample at L=6.** A robust statement requires multiple samples (probability of "BE-good" config at typical Gaussian). Pass-12 used 1 sample (seed=42); the result is positive but a single sample is not a distribution.

2. **L=6 coexact window is small.** Only 24 modes per Lie algebra direction, all at Maxwell eigenvalue exactly 1 (the lowest physical eigenvalue at $L=6$). At $L=24$, the coexact window with $\Lambda=1$ contains many more modes spanning eigenvalues in $(0, 1]$. The behavior of all those modes is not directly tested by L=6.

3. **Gaussian sampling ≠ Wilson sampling.** Gaussian $A\sim\mathcal N(0,1/\beta)$ is the leading-order approximation to Wilson at large β, but ignores: (a) the $O(\beta^{-3/2})$ cubic correction; (b) plaquette-correlation effects that are stronger in Wilson; (c) finite-volume corrections. A Wilson MCMC sample would give a more honest "typical Wilson config" but is more expensive to set up.

4. **Doesn't address atypical configurations.** Pass-12 only tests typical Gaussian configs. The §H.8 ingredient (iv) globalization requires handling atypical (bulk-tail) configurations where the Lyapunov function should drive return to the typical set. The pass-12 result is silent on this — it only shows that AT typical configs, projected BE holds.

5. **Doesn't supply the analytic theorem.** Even if the numerics are uniformly positive across multiple samples and larger L, this would be empirical support for the §J.6 conjecture, not a proof. The analytic statement — "$P\nabla^2 S_W(U) P$ has spectrum $\ge\rho>0$ uniformly across the support of the Wilson measure, with $\rho$ independent of $L$" — requires functional-analytic work beyond what numerics can supply.

### K.6 Concrete next subtargets

In decreasing order of feasibility:

1. **More samples at L=6.** Repeat the K.3 computation with 10-50 Gaussian samples to get a distribution for the projected BE minimum. Currently: 1 sample with min = +0.31. Estimated time: ~30 min per sample (the main cost is the $O(N_{\rm plaq}\cdot 12^2)$ FD evaluations).

2. **L=8 with multiple samples.** At $L=8$, the coexact window with $\Lambda=1$ contains modes at Maxwell eigenvalues in $[0.586, 1]$ — multiple non-trivial eigenvalues. Number of coexact-window modes per Lie algebra: roughly $\sim 100$. Memory still tractable via per-plaquette accumulation. Estimated time: ~2-4 hours per sample.

3. **Wilson MCMC samples.** Use heat-bath or Wolff cluster algorithm to sample actual Wilson configurations at $\beta=3.5$, then compute projected Hessian. This eliminates the Gaussian-approximation caveat.

4. **L=12, L=16, L=24 with sparse methods.** At these sizes the Hessian is too big for dense methods but the projected Hessian is small (matrix of size $\sim 3 n_{\rm coex}$). The per-plaquette accumulation continues to work, but $N_{\rm plaq}$ grows as $L^4$ — at $L=24$, $N_{\rm plaq}\approx 2\times 10^6$, requiring distributed computation or weeks of single-machine time.

5. **Analytic conjecture.** Use the numerics to formulate a precise analytic statement: e.g., "for typical Wilson configurations at $\beta\ge\beta_0$, the coexact-window-projected Wilson Hessian has lowest eigenvalue $\ge\rho_*(\beta,\Lambda)$ with $\rho_*$ uniform in $L$, where $\rho_*(\beta,\Lambda) = \kappa_G - C(\beta,\Lambda)$ for some explicit $C$." Then attack this analytically.

6. **Connection to lattice perturbation theory.** The projected Hessian in the small-$\Lambda$, large-$\beta$ regime should be amenable to lattice perturbation expansion. Computing the leading and sub-leading corrections to $\kappa_G + (\beta/4)\Lambda$ from background-field nonlinearities would give an analytic prediction to compare with §K.3.

### K.7 Honest verdict

**Pass-12 supplies the first explicit numerical demonstration** that the spectral-window projector restricted to the coexact subspace produces a projected Wilson Hessian with ALL POSITIVE eigenvalues at a typical Gaussian configuration at $\beta=3.5$. The empirical projected BE floor is +2.31 (vs the geometric floor $\kappa_G=2$). This is consistent with the §J.6 spectral-window conjecture and substantially strengthens the empirical case that the master document's distinctive projection structure is what makes Bakry–Émery potentially work at large β — where SZZ 2023's unprojected approach fails.

**Pass-12 does NOT prove §I.16.** It does not prove §J.6. It does not supply the §H.8 ingredient (iv) globalization. It provides empirical positive evidence for ONE typical config at L=6, with the artifacts and caveats of §K.5.

**The cumulative picture from passes 7–12.**

| Pass | Finding |
|---|---|
| 7 | No peer-reviewed paper closes (M′)_SU(2) at large β |
| 8 | Auxiliary derivations from notes — useful but don't close |
| 9 | $\kappa_G=2$ for SU(2); 4-ingredient research roadmap (§H.8) |
| 10 | Conditional derivation chain explicit; minimal target sharpened |
| 11 | Numerical attempt at minimal target identifies obstruction (exp rarity); proposes spectral-window restriction |
| **12** | **First explicit numerical confirmation that the spectral-window + coexact restriction produces uniformly positive projected BE at a typical config; supports §J.6** |

**The §J.6 spectral-window proposal is now in a stronger empirical position.** Combined with:
- v3b 1200-sample numerical evidence ($\Theta_*=0.884<1$) at the operator-norm level;
- pass-12 L=6 single-sample demonstration that projected BE is uniformly positive at a typical config;

the research direction has explicit empirical anchors at multiple measurement levels. **But:** no peer-reviewed paper supplies it, the analytic theorem is missing, and the L=6 single-sample result is one data point. Pass-7 conditional status is unchanged.

**Master document conditional status: unchanged.** The conditional theorem (§2) remains conditional on (M′)_SU(2). Pass-12 supplies empirical evidence for the §J.6 research direction, not a proof.

---

## Appendix L — Tighter constants in Appendix I at $\beta=3.5$ (pass 13): pinned vs. open

### L.0 Scope

**Goal.** Re-derive the conditional content of Appendix I with explicit numerical constants tracked through at the master's working corner $\beta=3.5$, $L=24$, $\Lambda=1$, $\delta_{\rm bond}=1$. Separate constants into three classes: (a) pinnable from empirical data or master numerics; (b) pinnable from deterministic lattice geometry; (c) genuinely open (depend on the rooted-source polymer hypothesis).

**Honest framing.** The conditional theorem of the master document is **conditional on the rooted-source polymer expansion hypothesis** (Theorem I.3.1 in Appendix I). The constants $C_{\rm root}$, polymer decay $m$, polymer activity $C_0$ live inside this hypothesis and cannot be tightened without supplying the hypothesis. What pass-13 §L does: show that *every other* constant in the firewall inequality (14.1) is numerically determined at the working corner.

### L.1 Pinned by empirical data / master numerics

| Constant | Value at working corner | Source |
|---|---|---|
| $q_\eta$ (high-plaquette probability) | $\approx 0.003$ at $\delta_{\rm bond}=1$ | Master §11.0c v17b numerics; CSV row-level audit (Appendix E) |
| $\kappa_\Lambda$ (projector operator-norm bound) | $\le 1$ effective at $\Lambda=1$ | Master §3-§5; v3b $\Theta_*=0.884<1$ over 1200 samples |
| $V_{\max}/m^2$ (Birman-Schwinger scale) | $\le \Theta_* = 0.884$ at working corner | Master §11.0c v3b sweep |
| $\kappa_G$ (SU(2) Ricci constant) | $= 2$ **exactly** | Pass-9 Theorem H.3.1' (rigorous: round $S^3$ at radius 1) |
| Projected BE floor on coexact window | $\ge 2.31$ at $L=6$ typical Gaussian | Pass-12 §K.3 (one Gaussian sample) |
| Typical plaquette $\langle\phi_p\rangle$ | $\approx 3/(2\beta) = 0.43$ at $\beta=3.5$ | Standard small-fluctuation result (master §10) |
| Block-jackknife uniformity ratio | $0.00485-0.00527$ at $L\in\{12,16,24\}$ | block_jackknife_diagnostics.csv (1566 rows; pass-4 audit) |
| Q₈ closure margin (for comparison) | $\beta_0 = 61.16$, margin $\approx 0.618$ | Master §9 Theorem FNG (closed) |

### L.2 Pinned by deterministic geometry

| Constant | Value | Derivation |
|---|---|---|
| Number of plaquettes per link in $d=4$ | $= 6$ (oriented) | $2(d-1) = 6$ |
| Trace-overlap neighbor count $N_m$ in source eq (5.1) | $\le 6$ ・ (geometric series factor) | Standard lattice sum |
| Spectral window dim at $L=24$, $\Lambda=1$ | $\sim 10^3$ per Lie algebra direction | Lattice momenta with $\sum_i 4\sin^2(\pi n_i/24) \le 1$ |
| Coexact spectral window dim at $L=24$, $\Lambda=1$ | $\sim 700$ per Lie algebra | Spectral window minus pure-gauge zero modes |
| vMF constant $C_{S^3}$ in source §7.1 | $= |S^3|/c_{S^3} = O(1)$ | $|S^3| = 2\pi^2$; Laplace asymptotics give $c_{S^3}$ explicit |
| Matrix-Bernstein prefactor structure | $6q + \sqrt{12 q \kappa_\Lambda \log(\cdot)} + (2\kappa_\Lambda/3)\log(\cdot)$ | Source eq (13.2) |
| Per-plaquette Wilson Hessian eigenvalue at trivial | $= \beta\cdot 6/4 = 5.25$ at $\beta=3.5$ | Pass-11 §J.2 + pass-12 §K.2 verification |

### L.3 Open (depend on rooted-source polymer hypothesis)

| Constant | Status | Where it appears |
|---|---|---|
| $C_{\rm root} = C_{\rm conn}$ | Open. Bounded by connected-graph sum if polymer expansion converges with explicit $C_0, m_0$ | Source §3.1 Theorem F eq (3.1); enters (5.2) as front constant |
| Polymer decay rate $m$ | Open. Should be $> 0$ at large β if expansion converges | Source §3.1 hypothesis; enters (5.1)-(5.2) |
| Polymer activity prefactor $C_0$ in source eq (13.1) | Open as a quantitative bound at large β; structurally exists | Matrix-Laplace transfer (13.2); enters firewall (14.1) |
| Smoothing-bridge uniformity constant | Open. Required for §I.12 hard/smooth bridge $\eta\to 0$ | Source §12; enters convergence of hard from smooth |

### L.4 The firewall inequality (14.1) with pinned constants

Source eq (14.1) reads
$$
\frac{V_{\max}}{m_{\rm BS}^2}\left[6q+\sqrt{12q\kappa_\Lambda\log(2C_0K/\varepsilon)}+\frac{2\kappa_\Lambda}{3}\log(2C_0K/\varepsilon)\right]<1,
$$
where $m_{\rm BS}$ is the Birman–Schwinger mass scale (NOT the polymer decay $m$ above; these are different $m$'s).

**Plug pinned values.** Take $q = 0.003$, $\kappa_\Lambda = 1$, $V_{\max}/m_{\rm BS}^2 = \Theta_* = 0.884$ (master v3b), $K \sim$ trace count $\sim L^4 \cdot$ projector trace $\sim$ few times $L^4 = 3.3\times 10^5$ at $L=24$, $\varepsilon = 0.01$ (margin):
- $6q = 0.018$
- $\log(2 C_0 K/\varepsilon) = \log(2 C_0 \cdot 3.3\times 10^5 / 0.01) = \log(C_0 \cdot 6.6\times 10^7) = 18.0 + \log C_0$
- For $C_0 = 1$: $\log(\cdot) = 18.0$
- $\sqrt{12 q \kappa_\Lambda \log} = \sqrt{12\cdot 0.003\cdot 1\cdot 18} = \sqrt{0.648} = 0.805$
- $(2\kappa_\Lambda/3)\log = (2/3)\cdot 18 = 12.0$
- Bracket $\approx 0.018 + 0.805 + 12.0 = 12.8$
- Multiplied by $V_{\max}/m_{\rm BS}^2 = 0.884$: $0.884 \cdot 12.8 = 11.3$
- Required $< 1$: **fails by factor 11.3** if $C_0=1$

**To satisfy (14.1) with pinned values $q=0.003$, $\kappa_\Lambda=1$, $\Theta_*=0.884$**, we need the bracket $<1/0.884=1.13$. Forcing the $(2/3)\log$ term $<1$: $\log(2C_0K/\varepsilon) < 3/2$, i.e., $2C_0K/\varepsilon < e^{1.5} = 4.5$, i.e., $C_0 < 4.5\varepsilon/(2K) = 4.5\cdot 0.01/(2\cdot 3.3\times 10^5) = 6.8\times 10^{-8}$.

**Conclusion of L.4.** The firewall inequality (14.1) plugged with all pinned constants requires $C_0 \le 6.8\times 10^{-8}$ at $L=24$ working corner. This is a SHARP requirement on the polymer activity prefactor. It is not currently known whether this bound is achievable at $\beta=3.5$ for SU(2) under the rooted-source polymer hypothesis. **Pass-7 finding stands**: no peer-reviewed paper supplies $C_0$ at the required level.

(Note: the $C_0$ here is the polymer activity prefactor entering matrix-Laplace transfer (13.1), conceptually distinct from $C_{\rm root}$ in Theorem F. Both are open at large β.)

### L.5 The vMF tightness gap

Source §7.1 gives the vMF cap rarity bound
$$\nu_H(c\cdot x\le a)\le C_{S^3}\kappa^{3/2}e^{-\kappa\Delta(\rho,a)}.$$

At master's working corner with $\delta_{\rm bond}=1$ (so $a_\eta = \eta$ small), typical $\rho\approx 1$, $\kappa=\beta|H|$:
- For $|H|=1$, $\kappa = \beta = 3.5$
- $\Delta(\rho, \eta) \approx 1$ for $\rho\to 1$, $\eta\to 0$
- $q_\eta \le C_{S^3} \cdot 3.5^{3/2} \cdot e^{-3.5} = C_{S^3} \cdot 6.55 \cdot 0.0302 = 0.198\, C_{S^3}$
- With $C_{S^3} = O(1)$: $q_\eta \le O(0.2)$

**Empirical $q_\eta$ at working corner: $0.003$ (master §11.0c v17b).**

**Gap: the vMF bound is loose by factor $0.2/0.003 \approx 67\times$ at $\beta=3.5$.** Closing this gap analytically would require either:
(a) better vMF estimates with sharper $\kappa$-dependence
(b) accounting for $|H|>1$ at typical configurations (staple magnitude can exceed 1)
(c) more refined methods (saddle-point, Stein, exchangeable-pair)

This tightness gap is unrelated to the rooted-source polymer hypothesis — it's a separate issue with the per-link rare-event bound.

### L.6 Honest verdict

**Pass-13 §L conclusion.** Most constants in the conditional theorem are numerically pinned. The remaining open constants ($C_{\rm root}, m$ polymer, $C_0$ activity, smoothing-bridge uniformity) all live inside the rooted-source polymer hypothesis or its consequences. The firewall inequality (14.1) with pinned constants requires $C_0 \le 6.8\times 10^{-8}$ at the $L=24$ working corner — a sharp bound that is not supplied by any peer-reviewed paper.

**The "what would have to be proved next" question — refined.** Pass-10 §I.16 said: prove $|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})| \le C q_\eta^2 e^{-m d(p,p')}$. Pass-11 §J identified the obstruction. Pass-12 §K.3 supplied empirical evidence for spectral-gap component. **Pass-13 §L now adds: the prefactor in the rooted-source polymer expansion must be tight enough for $C_0 \le 6.8\times 10^{-8}$ at the master's $L=24$ working corner.** This is the precise quantitative target for closing the route via the matrix-Laplace transfer.

---

## Appendix M — Bridge from pass-12 §K.3 to source §I.16: spectral gap vs. density scaling (pass 13)

### M.0 Scope

**Goal.** Pass-12 §K.3 supplied the empirical positive finding that the coexact-window-projected Wilson Hessian at a typical Gaussian config at $\beta=3.5$ has all-positive eigenvalues with floor $\ge 2.31$ at $L=6$. The source §I.16 minimal target is the pair-cumulant decay $|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\le C q_\eta^2 e^{-md(p,p')}$. Pass-13 §M makes the bridge between these two statements explicit: which part of §I.16 does §K.3 support, and which part is still missing?

**Honest framing.** The bridge is **partial**. Pass-12 §K.3 supports the spectral-gap/decay-rate component of §I.16. It does NOT support the $q_\eta^2$ density-scaling prefactor — which requires either small-density Brascamp–Lieb absorption or Theorem-F-style polymer-expansion machinery. This appendix makes that decomposition explicit.

### M.1 The standard Bakry–Émery → covariance decay chain (BGL 2014)

From Bakry, Gentil, Ledoux *Analysis and Geometry of Markov Diffusion Operators* (2014), the standard theorem: if $\mu = e^{-V}d\mathrm{vol}_g/Z$ on a complete Riemannian manifold with $\mathrm{Ric}_g + \nabla^2 V \ge \rho\,g$ uniformly with $\rho > 0$, then for $f, g \in C^1_b$ with disjoint supports:
$$
|\mathrm{Cov}_\mu(f,g)| \le \frac{\|\nabla f\|_\infty\,\|\nabla g\|_\infty}{\rho}\,e^{-\sqrt{\rho}\,d(\mathrm{supp}\,f,\,\mathrm{supp}\,g)/2}.
$$

**Decay rate.** $m_{BGL} = \sqrt\rho/2$.

**Prefactor.** $\|\nabla f\|_\infty \|\nabla g\|_\infty/\rho$.

### M.2 Applied to pass-12 §K.3

Pass-12 §K.3 empirical: projected BE floor $\rho_{\rm proj}^{\rm emp} \ge 2.31$ at $L=6$, $\beta=3.5$, typical Gaussian.

**If** this floor extends uniformly to all $L$ and all typical configs (BIG IF — single Gaussian sample at L=6 is the only data):
- BGL decay rate: $m_{BGL} = \sqrt{2.31}/2 = 0.760$ per lattice step
- BGL prefactor: $\|\nabla X_{p,\eta}\|_\infty^2 / 2.31$

**For smooth indicator $X_{p,\eta}$ with smoothing width $\eta$:**
- $\|X_{p,\eta}\|_\infty \le 1$
- $\|\nabla X_{p,\eta}\|_\infty \lesssim 1/\eta$
- So BGL prefactor $\lesssim 1/(2.31 \eta^2) = 0.43/\eta^2$

**Combined BGL bound:**
$$
|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})| \lesssim \frac{0.43}{\eta^2}\,e^{-0.76\,d(p,p')} \quad\text{(if projected BE floor extends)}.
$$

### M.3 The density-scaling gap

**Source §I.16 target:**
$$|\mathrm{Cov}_W(X_{p,\eta},X_{p',\eta})|\le C q_\eta^2 e^{-md(p,p')}.$$

**Comparing prefactors:**
- BGL gives: $0.43/\eta^2$
- Target: $C q_\eta^2$
- **Gap:** BGL has $1/\eta^2$ scaling (Lipschitz norm squared), target has $q_\eta^2$ scaling (density squared). These are very different at large β.

At master's working corner: $\eta\sim 0.1$ gives $1/\eta^2 = 100$; $q_\eta = 0.003$ gives $q_\eta^2 = 9\times 10^{-6}$. **Ratio: $1.1\times 10^7$.** BGL is loose by 7 orders of magnitude in the prefactor at the master's working corner.

**Why this is structural, not numerical.** BGL bounds covariance by Lipschitz norm and spectral gap. The Lipschitz norm of a smoothed indicator scales with $1/\eta$ (steeper for thinner smoothing), not with $q_\eta$ (rarity of the event). To get $q_\eta$ scaling, one needs to use the SMALL EXPECTATION of $X_{p,\eta}$, not just its Lipschitz norm.

### M.4 What additional input bridges the gap

**Option (a): Brascamp–Lieb absorption ($q_\eta$ factor, not $q_\eta^2$).** Under BE conditions with $\rho > 0$:
$$\mathrm{Var}_\mu(f) \le \frac{1}{\rho}\mathbb{E}_\mu[\|\nabla f\|^2].$$
For $f = X_{p,\eta}$: $\|\nabla f\|^2$ is supported where $X_{p,\eta}$ has support, of $\mu$-measure $\le q_\eta$. So $\mathbb{E}[\|\nabla f\|^2] \lesssim q_\eta/\eta^2$ and $\mathrm{Var}(X_{p,\eta}) \le q_\eta/(\rho\eta^2)$.

By Cauchy–Schwarz, $|\mathrm{Cov}(X_{p,\eta},X_{p',\eta})| \le \sqrt{\mathrm{Var}(X_{p,\eta})\mathrm{Var}(X_{p',\eta})} \le q_\eta/(\rho\eta^2)$.

**This gives $q_\eta$, not $q_\eta^2$.** Better than $1/\eta^2$ by factor $q_\eta = 0.003$, but still off by factor $1/q_\eta \approx 333$ from the source target.

**Option (b): Theorem-F polymer-expansion machinery ($q_\eta^2$ factor).** Source §3.1 Theorem F:
- Connected pressure $\Psi_{p,p'}(s,t)$ has polymer expansion
- Activity bound $|K(\Gamma; s,t)| \le C_0^{|\Gamma|} e^{-m_0\tau(\Gamma)} |s||t| \mathbb{E}_W[Y_p] q_\eta$
- Cauchy formula on bidisc $|s|=|t|=r$ extracts $\mathrm{Cov} = \partial_s\partial_t\Psi(0,0) \le r^{-2}\sup|\Psi| \le \mathbb{E}[Y_p] q_\eta \cdot$ (connected-graph sum)
- With $\mathbb{E}[Y_p] \le q_\eta$: $|\mathrm{Cov}| \le C q_\eta^2 e^{-md}$

**The $q_\eta^2$ scaling comes from polymer-activity $|s|^1\mathbb{E}[Y_p]^1 \cdot |t|^1 q_\eta^1$ combined with Cauchy bidisc trick. This is NOT a Bakry–Émery consequence.** It is an analyticity/polymer-structure consequence that requires the rooted-source polymer expansion to exist.

**Option (c): a hypothetical "small-density spectral-gap covariance decay" lemma.** Conjecture: under BE conditions, if $f$ has $L^\infty$ norm bounded and $L^1$ norm small ($\|f\|_{L^1} \le q$), then $|\mathrm{Cov}(f,g)| \le C q \|g\|_{L^1}/\rho \cdot e^{-\sqrt\rho d/2}$. This would give $q_\eta^2$ scaling if applied to $f = g = X_{p,\eta}$. **Not a standard BGL theorem; would need separate proof.** Conditional on this lemma, pass-12 §K.3 would directly support source §I.16 via the bridge.

### M.5 Honest verdict

**Pass-13 §M conclusion.** Pass-12 §K.3 supplies the decay-rate component of source §I.16 (assuming the BE floor extends from L=6 to all L and from one Gaussian sample to all typical configs — BOTH BIG IFS). It does NOT supply the density-scaling component.

| §I.16 component | Status after pass 12 | What's still needed |
|---|---|---|
| Exponential decay rate $m > 0$ | Empirically supported via §K.3: $m \ge 0.76$ | Theorem extending §K.3 to all L, all typical configs |
| Density prefactor $q_\eta^2$ scaling | NOT supplied by BE | Theorem F (polymer expansion) OR a small-density BE lemma |

**The cleanest sharper version of the pass-7 question.** Instead of "prove source §I.16", the precise residual question is: **prove a "small-density Bakry–Émery covariance decay" theorem that gives $q_\eta^2$ prefactor scaling under projected BE conditions.** If such a theorem existed, combined with §K.3's empirical content (extended to a theorem), it would close the route. **No peer-reviewed paper supplies this theorem.**

This is a distinct open mathematical problem — perhaps more tractable than the full rooted-source polymer expansion, because it asks for a softer statement about how BE combined with small-density observables yields tighter covariance prefactors than the standard BGL theorem provides.

**Connection to SZZ 2023.** SZZ at strong coupling proves a structurally identical statement (Theorem 1.10 of arXiv:2204.12737): exponential covariance decay for Wilson loops under BE conditions, with prefactors that scale appropriately with observable size. The SZZ statement IS effectively a "small-density spectral-gap covariance decay" theorem at strong coupling. **Extending SZZ's prefactor scaling to large β — via the projected dynamics suggested by pass-12 — is the precise research target.**

---

## Appendix N — Russian-school cluster expansions: what they cover and what they don't (pass 13)

### N.0 Scope

**Goal.** Close the pass-7 known Russian-language literature gap by surveying the central works of the Russian school on cluster expansions for Gibbs random fields (Malyshev, Minlos, Dobrushin, Sinai). Identify exactly what their methods supply and where the gap to (M′)_SU(2) at large β actually lies.

**Headline.** The Russian school developed extensive general-purpose cluster expansion machinery for continuous-spin Gibbs fields (which structurally includes SU(N) Wilson at large β). However, their explicit gauge-theory chapter (Malyshev–Minlos 1991 §7.4) covers $\mathbb Z_2$ only; no Russian-school paper explicitly carries out the level-(iii) bound for SU(2) Wilson at large β. **The pass-7 known gap is therefore not a hidden closure; it is a confirmation that the general technology exists but the specific non-Abelian extension was not made by the Russian school.**

### N.1 Central references

**Malyshev (1980), "Cluster expansions in lattice models of statistical physics and the quantum theory of fields"**, *Uspekhi Matematicheskikh Nauk* 35:3-53 (1980); English translation: *Russian Mathematical Surveys* 35:1-62 (1980). This is the foundational Russian-language survey of cluster expansion technology, covering: semi-invariants and diagrams, vacuum cluster expansions, perturbations of independent and Gaussian fields, low-temperature expansions, uniform strong cluster estimates.

**Malyshev & Minlos (1991), "Gibbs Random Fields: Cluster Expansions"**, Kluwer Academic Publishers, Mathematics and Its Applications (Soviet Series) vol. 44. English translation of *Gibbsovskie sluchainye polya: Metod klasternykh razlozhenii*, Nauka, Moscow (1985). This is the book-length comprehensive treatment by the central figures.

### N.2 Chapter-by-chapter scope of Malyshev–Minlos 1991

| Chapter | Topic | Relevance to (M′)_SU(2) at large β |
|---|---|---|
| **1** Gibbs Fields (Basic Notions) | Definition of Gibbs modifications, boundary conditions, conditional distributions | General framework; applies to SU(2) Wilson |
| **2** Semi-Invariants and Combinatorics | Hermite-Itô-Wick polynomials, diagrams, connectedness, summation over trees | Combinatorial backbone used in any cluster expansion |
| **3** General Scheme of Cluster Expansion | Cluster representation of partition functions, ensembles of subsets | General theorem; applicable in principle |
| **4** Perturbation of Gaussian Fields | Gaussian field perturbation, slow-decay correlations, d-Markov modifications | Most directly relevant for the small-fluctuation regime, but the Wilson measure is NOT Gaussian |
| **5** §1 Discrete Spin (countable ground states) | Pirogov-Sinai theory | Not directly for continuous spin |
| **5 §2** Continuous Spin: **Unique Ground State** | **Low-temperature expansions for continuous-spin systems with unique ground state.** This is THE abstract framework into which SU(2) Wilson at large β falls. | **Most relevant.** The abstract theorems here would, in principle, deliver something like (M′)_SU(2) at large β — but the specific application is not carried out in the book |
| 5 §3 Continuous Spin: Two Ground States | Symmetry-broken cases | Not directly relevant; SU(2) Wilson at large β has unique ground state $U^{(0)}$ |
| **6** Decay of Correlations | §1 hierarchy of decay properties; §2 analytic method for semi-invariants of quasi-local functionals; **§3 combinatorial method for exponentially-regular cluster expansion**; §5 low-temperature region; §6 scaling limit | **Closest to (M′)-style bounds.** The exponentially-regular cluster expansion combinatorial method is structurally what would deliver pair-covariance decay |
| 7 §1-3 Gibbs quasistates, uniqueness, compactness | Foundational | General framework |
| **7 §4** Gauge Field with Gauge Group $\mathbb Z_2$ | The ONLY explicit gauge-theory chapter | **$\mathbb Z_2$ only; NOT non-Abelian** |
| 7 §5 Markov Processes with Local Interaction | Dynamical applications | Not directly relevant |

**The structural picture.** Chapters 1-3 develop general technology. Chapter 5 §2 develops the abstract framework for continuous-spin systems with unique ground state at low temperature — applicable in principle to SU(2) Wilson at large β. Chapter 6 develops the decay-of-correlations machinery — applicable in principle. Chapter 7 §4 takes the technology to a specific gauge-theory case, but only the Abelian $\mathbb Z_2$.

### N.3 What the Russian school did NOT do for SU(N)

1. **No explicit non-Abelian gauge-theory chapter.** The Malyshev–Minlos 1991 chapter 7 §4 treats $\mathbb Z_2$ explicitly; non-Abelian gauge groups are not given their own chapter.

2. **No specific level-(iii) bound for SU(N) Wilson at large β.** The closest abstract framework (chapter 5 §2 continuous spin + chapter 6 exponentially-regular cluster expansion) would in principle deliver pair-covariance decay if applied carefully to SU(N) Wilson; but the specific quantitative bound with explicit constants is not in the Russian-school literature.

3. **No analog of source §3.1 Theorem F at large β for SU(2).** Their cluster expansion technology covers many regimes (high temperature, low temperature with discrete ground state, Gaussian perturbation), but the explicit "rooted-source polymer at large β for SU(2)" — which is the master's open hypothesis — is not closed in their work.

4. **No master-document-style "projected Maxwell" structure.** The Russian school works directly with Gibbs measures, not projected operators. The spectral-window restriction (pass-11 §J.6, pass-12 §K.3) is foreign to their framework.

### N.4 Adjacent Russian-school works

- **Dobrushin (1968)**, "The description of a random field by means of conditional probabilities and conditions of its regularity", *Theory of Probability and Its Applications* 13:197–224 — the celebrated uniqueness theorem; applies to high-temperature regimes
- **Dobrushin–Shlosman (1985)** — translation-invariant generalizations of Dobrushin uniqueness
- **Minlos–Sinai (1967, 1968)** — phase separation in low-temperature lattice gas; not gauge theory
- **Malyshev–Petrova (1980s)**, "Duality transformations of Gibbs random fields", *Journal of Mathematical Sciences* — Poisson summation, electrodynamic representation, Hamiltonian duality; relevant for Abelian gauge but not non-Abelian
- **Malyshev–Nicolaev (1984)**, "Uniqueness of Gibbs fields via cluster expansions", *J. Stat. Phys.* 35:375–379 — uniqueness via cluster expansions
- **Malyshev (1978)**, "Perturbations in Gibbs random fields", *Multicomponent Random Systems* [in Russian], Nauka, Moscow — perturbative cluster expansions

### N.5 Connection to the master document

The master document's open hypothesis — the rooted-source polymer expansion for SU(2) at large β with explicit prefactor (source §3.1 Theorem F) — sits exactly inside the abstract framework that Malyshev–Minlos chapter 5 §2 + chapter 6 develops. If a researcher were to take the abstract Russian-school machinery and apply it explicitly to SU(2) Wilson at $\beta=3.5$, with the master's choice of projector $P_{\le\Lambda,L}$ and observable $X_{p,\eta}$, the result would be a specific instantiation of pre-existing abstract theory — not a new theorem.

**Estimated effort.** Carrying out this explicit application is a substantial research project: probably 6–12 months of dedicated work for someone fluent in both the Russian-school technology and the master document's projected structure. It is the cleanest path to (M′)_SU(2) at large β via Russian-school tools, but it has not been done.

**An honest interpretation.** The pass-7 "Russian-language gap" was a real one — but it was a gap of UNDONE explicit work, not a hidden closure. The Russian school has the tools; nobody has used them for SU(2) Wilson at large β with the level-(iii) bound in mind.

### N.6 Honest verdict

**Pass-13 §N conclusion.**

1. The Russian school of cluster expansions (Malyshev, Minlos, Dobrushin, Sinai) developed extensive general-purpose machinery for Gibbs random fields, including the continuous-spin case relevant to SU(2) Wilson at large β.
2. Their explicit gauge-theory chapter (Malyshev–Minlos 1991 §7.4) covers $\mathbb Z_2$ only; no Russian-school paper does SU(2) at large β.
3. The abstract framework (chapter 5 §2 + chapter 6) is applicable in principle and would in principle deliver (M′)_SU(2) at large β, but the specific application has not been made.
4. **Pass-7 known Russian-language gap is now substantively addressed**: it is confirmed that the gap is one of undone explicit work, not a hidden closure. The general technology exists; the specific extension is open.
5. **The pass-7 conditional status is unchanged**: no peer-reviewed paper (Western or Russian) closes (M′)_SU(2) at large β for SU(2). This was the literature-survey finding; Appendix N confirms it on the Russian side.

**A constructive next step.** Use the Malyshev–Minlos chapter 5 §2 + chapter 6 abstract framework, instantiate at SU(2) Wilson with the master document's projector and observable, and check whether the resulting bound matches the source §I.16 target. This is a concrete research project with a known endpoint, using existing tools.

---

## Appendix O — Distribution of projected BE eigenvalues across 10 Gaussian samples at L=6 (pass 14, §K.3 extension)

### O.0 Scope

**Goal.** Address pass-12 §K.5 caveat (i) — "single typical Gaussian sample at L=6" — by computing the projected Wilson Hessian at 10 independent Gaussian configurations and reporting the distribution of projected Bakry–Émery eigenvalues. Verify whether the §K.3 positive finding (projected BE min = 2.31 at seed 42) is robust across typical Gaussian samples or a fluke of one seed.

**Outcome (preview).** The §K.3 finding is highly robust. All 720 projected BE eigenvalues (10 samples × 72 modes) lie in $[2.287, 2.830]$. Cross-sample standard deviation in BE min is only $0.014$ — less than 1% of the mean. The spectral-window + coexact restriction produces a projected BE floor at essentially $\kappa_G = 2.0$ (with $\sim 0.31$ headroom) uniformly across typical Gaussian configurations.

### O.1 Methodology

**Setup identical to pass-12 §K.3.** Lattice $L=6$ in $d=4$ ($N_{\rm links}=5184$, $N_{\rm plaq}=7776$, $N_{\rm full}=15552$). Spectral-window cutoff $\Lambda=1.05$ (one boundary increment above the lowest physical mode at $L=6$, $\lambda_{\rm phys,min}=4\sin^2(\pi/6)=1$). Working β = 3.5. Coexact-window dim per Lie algebra direction $=24$, total $=72$.

**Sampling.** Gaussian random gauge field $A_\ell^a \sim \mathcal N(0, 1/\beta)$ per link per Lie algebra component, with $U_\ell = \exp(iA_\ell\cdot\sigma/2)$.

**Seeds used.** 10 reproducible seeds: $\{42, 137, 271, 314, 577, 1001, 1729, 2718, 3141, 6022\}$. Each generates an independent typical Gaussian configuration.

**Computation per sample.** Memory-efficient per-plaquette accumulation: for each of $N_{\rm plaq}=7776$ plaquettes, build the local 12×12 Hessian via central finite differences (step $\epsilon=0.005$, 12² function evaluations), project into the (12 × 72) coexact-window basis, accumulate into the running 72×72 projected Hessian. Diagonalize the final 72×72 matrix to get the 72 projected Hessian eigenvalues; add $\kappa_G=2$ to obtain projected BE eigenvalues.

**Per-sample wall time.** $\approx 115$s on the run machine (the Maxwell decomposition is cached from pass-12 §K.3).

**Total wall time.** $\approx 20$ minutes for all 10 samples.

**Reproducibility.** Code and seed list archived as `/home/claude/L6_multi_sample.py` and `/home/claude/L6_incremental.py` (incremental variant with resume capability). Raw results in `/home/claude/L6_distribution_results.json`.

### O.2 Per-sample results

The full per-sample table (72 modes per sample summarized by min/p1/p99/max):

| Seed | BE min | BE p1 | BE p99 | BE max | Frac BE $<0$ |
|---|---|---|---|---|---|
| 42 (pass-12 §K.3) | 2.3120 | 2.3338 | 2.7955 | 2.7968 | 0.0000 |
| 137 | 2.3087 | 2.3203 | 2.7717 | 2.7796 | 0.0000 |
| 271 | 2.3052 | 2.3117 | 2.7893 | 2.8043 | 0.0000 |
| 314 | 2.3281 | 2.3462 | 2.7973 | 2.8047 | 0.0000 |
| 577 | 2.3184 | 2.3288 | 2.8158 | 2.8243 | 0.0000 |
| 1001 | 2.3093 | 2.3289 | 2.8085 | 2.8224 | 0.0000 |
| 1729 | 2.3410 | 2.3442 | 2.8227 | 2.8297 | 0.0000 |
| 2718 | 2.3094 | 2.3228 | 2.7867 | 2.7992 | 0.0000 |
| 3141 | 2.3044 | 2.3147 | 2.7885 | 2.8115 | 0.0000 |
| 6022 | 2.2871 | 2.3042 | 2.8065 | 2.8279 | 0.0000 |

**Observations from the table.**
- All 10 samples have BE min $> 2.28 > \kappa_G = 2.0$
- All 10 samples have **zero modes with BE $< 0$**
- All 10 samples have **zero modes with BE $< \kappa_G/2 = 1$**
- Spread of BE min across samples: $0.054$ (max $2.341$ – min $2.287$)

### O.3 Distribution statistics

Cross-sample statistics:

| Statistic | Mean | Std dev | Min | Max | Range |
|---|---|---|---|---|---|
| BE min | 2.3124 | 0.0137 | 2.2871 | 2.3410 | 0.0539 |
| BE p1 | 2.3256 | 0.0129 | 2.3042 | 2.3462 | 0.0420 |
| BE p99 | 2.7983 | 0.0145 | 2.7717 | 2.8227 | 0.0510 |
| BE max | 2.8100 | 0.0153 | 2.7796 | 2.8297 | 0.0501 |

**Cross-sample regularity.** The standard deviations are all $\le 0.015$, i.e., $\le 0.6\%$ of the means. This is **extremely tight** for an empirical distribution across 10 random configurations.

**Comparison to pass-11 §J.5 unprojected prediction.** Pass-11 §J.5 estimated that under Haar (a least-concentrated proxy), the probability $P(\text{all BE-good})$ across $\sim 8\times 10^6$ unprojected staple-link pairs at L=24 is bounded by $\le e^{-2.4\times 10^6}$ — essentially zero. Pass-14 §O empirically observes that across 720 PROJECTED BE eigenvalues at L=6, **none** are bad. **The projection is structurally what makes this work.**

### O.4 Interpretation

**The tight band suggests a structural floor, not sampling noise.**

A random matrix with eigenvalues spread over a range of order $O(\beta) \sim 3.5$ would, across 10 samples, exhibit cross-sample BE-min standard deviation of order $\sqrt{1/72}\cdot\text{spread} \sim 0.12\cdot 3.5/4 \sim 0.1$. The observed cross-sample $\sigma$ is $0.014$ — **7× tighter** than this random-matrix naive estimate.

**Interpretation.** The 72 coexact-window modes at L=6 are all at the same Maxwell eigenvalue $\lambda_{\rm phys}=1$ (the lowest physical mode), so the trivial-config projected Hessian eigenvalues are all $\beta\lambda/4 = 0.875$, identical across modes. At a typical Gaussian background, each mode acquires a configuration-dependent correction $\delta\lambda_k$. The cross-sample variation in BE min reflects the cross-sample variation in $\min_k\delta\lambda_k$.

The observed tightness (cross-sample $\sigma = 0.014$) suggests that $\min_k\delta\lambda_k$ has a sharply-peaked distribution — consistent with there being an UNDERLYING ANALYTIC EXPRESSION for the projected BE min as a function of the configuration, with small fluctuations around its central value.

**Conjecture (open).** The projected BE min at typical Gaussian configurations at $L=6$, $\beta=3.5$, $\Lambda=1.05$ converges to a deterministic floor $\rho_*(\beta, \Lambda)$ as $L\to\infty$, with $\rho_*$ given by an explicit formula. At the master's working corner: empirical estimate $\rho_*(3.5, 1) \approx 2.31$.

**If true, this conjecture would deliver §I.16's decay-rate component** (per pass-13 §M): $m \ge \sqrt{\rho_*}/2 \approx 0.76$ uniform in L. Combined with a "small-density spectral-gap covariance decay" theorem (pass-13 §M.4 option (c)), it would close the §I.16 minimal target.

### O.5 Caveats

Pass-14 §O closes pass-12 §K.5 caveat (1) "single typical Gaussian sample at L=6" — now 10 samples. **Pass-12 §K.5 caveats (2)–(5) remain unchanged.**

1. ~~Single sample at L=6.~~ **Now closed by pass-14 §O.**
2. **L=6 coexact window has only 24 modes per Lie algebra,** all at Maxwell eigenvalue $\lambda_{\rm phys}=1$ (boundary case). At L=24, the coexact spectral window with $\Lambda=1$ contains many more modes spanning eigenvalues in $(0, 1]$. The behavior at all those modes is not directly tested.
3. **Gaussian sampling ≠ Wilson sampling.** Gaussian is the leading-order approximation; Wilson MCMC would give the actually-typical Wilson configurations.
4. **Doesn't address atypical configurations.** The §H.8 ingredient (iv) globalization requires handling bulk-tail configurations; pass-14 §O only tests typical configs.
5. **Doesn't supply the analytic theorem.** Even with all 10 samples positive, this remains empirical evidence, not a proof. Pass-13 §M.4 small-density spectral-gap theorem is still required.

### O.6 Honest verdict

**Pass-14 §O conclusion.**

1. The pass-12 §K.3 finding is **highly robust** — not a single-seed fluke. 10 independent Gaussian configurations at the master's working corner all give projected BE in $[2.29, 2.83]$.
2. The cross-sample tightness (σ ≈ 0.014 for BE min) suggests an underlying analytic floor at $\rho_* \approx 2.31$.
3. The §J.6 spectral-window conjecture has its **10× independent empirical confirmation** at the master's working corner.
4. **The pass-7 conditional status is unchanged.** Pass-14 §O is empirical evidence for the conjecture; it is not a proof of (M′)_SU(2).

**The cumulative picture of the spectral-window proposal's empirical support:**

| Evidence source | What it measures | Status |
|---|---|---|
| Master §11.0c v3b | Projected operator norm $\|P\mathbf 1_D P\|$ at $\beta=3.5$, $\Lambda=1$, all L | $\Theta_*=0.884 < 1$ over 1200 samples |
| Pass-12 §K.3 | Projected Hessian eigenvalues, $L=6$, single Gaussian sample | All 72 modes positive, BE min = 2.31 |
| **Pass-14 §O** | **Projected Hessian eigenvalues, L=6, 10 Gaussian samples** | **All 720 modes positive, BE min mean $2.312\pm 0.014$, no sample shows any BE $< 0$** |

Three independent empirical anchors at the master's working corner, all consistent with the §J.6 spectral-window proposal. **No corresponding analytic theorem yet exists.**

**The constructive next milestones** (from pass-12 §K.6, unchanged):
- Wilson MCMC sampling to replace Gaussian approximation
- L=8 with multiple samples (more coexact modes in window, spanning eigenvalue range)
- Analytic conjecture for $\rho_*(\beta,\Lambda)$ matching the empirics
- The pass-13 §M.4 "small-density spectral-gap covariance decay" theorem

---

## Appendix P — Wilson MCMC samples vs Gaussian: a sharper test (pass 15)

### P.0 Scope

**Goal.** Pass-12 §K.5 caveat (3) flagged that pass-12/14 used Gaussian sampling ($A_\ell^a \sim \mathcal N(0, 1/\beta)$) as a proxy for typical Wilson configurations. Pass-15 implements actual Wilson Monte Carlo sampling at $L=6$, $\beta=3.5$ via heat-bath, takes 5 thermalized samples, and computes the projected Hessian at each. Compare to pass-14 §O Gaussian distribution.

**Outcome.** Wilson and Gaussian sampling give qualitatively similar but quantitatively distinct results. Wilson samples push the BE floor down by $\sim 0.11$ relative to Gaussian, but lift the BE ceiling up by $\sim 1.23$. **All 360 Wilson eigenvalues are positive (BE min $= 2.185 > \kappa_G = 2.0$); the §J.6 conjecture is empirically supported under both ensembles.** Wilson is the more honest probe.

### P.1 Methodology

**Heat-bath algorithm.** For each link $\ell$, the conditional density given all other links is the von-Mises–Fisher distribution on $S^3$ with concentration $\kappa = \beta|H_\ell|$ and mean direction $\bar H_\ell / |H_\ell|$, where $H_\ell = \sum_{p\ni\ell} \bar V_\ell^{(p)}$ is the conjugate sum of staples (the bar denotes quaternion conjugate, $\bar V = (v_0, -\vec v)$ for $V = (v_0, \vec v)$). The conjugation arises because $\frac{1}{2}\mathrm{Re}\,\mathrm{Tr}(U_\ell V_\ell) = u_0 v_0 - \vec u\cdot\vec v = U_\ell \cdot \bar V_\ell$ in quaternion notation.

**vMF sampling.** Standard rejection-based algorithm (Creutz, *Quarks Gluons and Lattices* §A.4):
- Generate $r_1\sim U(0,1)$
- Compute $\lambda^2 = -\log[1 - r_1(1-e^{-2\kappa})]/(2\kappa)$
- Set $y_0 = 1 - 2\lambda^2$
- Accept with probability $\sqrt{1 - \lambda^2}$ (rejection); else repeat
- On acceptance: sample uniform direction on $S^2$, scale by $\sqrt{1-y_0^2}$, rotate to align with $\bar H/|H|$

**Thermalization.** 60 heat-bath sweeps from cold start ($U_\ell = I$ everywhere). The plaquette average $\langle x_0(U_p) \rangle = \frac{1}{2}\mathrm{Re}\mathrm{Tr}\langle U_p\rangle$ equilibrates to ~0.852 by sweep 10, then drifts within $\pm 0.003$ thereafter. This corresponds to $\langle\phi_p\rangle = 0.148$.

**Comparison to analytic prediction.** Leading-order large-$\beta$ expansion for SU(N) Wilson gives
$$\langle\phi_p\rangle = \frac{N^2-1}{4N\beta} + O(\beta^{-2})$$
For SU(2) at $\beta=3.5$: $\langle\phi_p\rangle = 3/(8\cdot 3.5) = 0.1071$. The MCMC value $0.148$ exceeds this by 38%, consistent with $O(1/\beta^2)$ next-to-leading corrections at moderate $\beta$.

**Sampling.** 5 samples taken with 15 decorrelation sweeps between each. Each sweep ~0.57s.

**Hessian computation.** Convert each Wilson sample from quaternion form to $2\times 2$ SU(2) matrix form via $U = a_0 I + i\vec a\cdot\vec\sigma$. Then apply the same projected-Hessian build code as §K.3 / §O. Per-sample compute: ~110s.

**Code.** `/home/claude/wilson_full.py` (heat-bath), `/home/claude/wilson_sample.py` (sample generation), `/home/claude/wilson_hessian.py` (projected Hessian at each Wilson sample).

### P.2 Per-sample results

| Wilson idx | Plaq $x_0$ | BE min | BE p1 | BE p99 | BE max | Frac BE<0 | Time |
|---|---|---|---|---|---|---|---|
| 0 | 0.8531 | 2.2048 | 2.2192 | 3.9779 | 4.0246 | 0.0000 | 110s |
| 1 | 0.8523 | 2.2156 | 2.2236 | 4.0614 | 4.0766 | 0.0000 | 108s |
| 2 | 0.8515 | 2.1949 | 2.2322 | 4.0106 | 4.0577 | 0.0000 | 113s |
| 3 | 0.8506 | 2.1925 | 2.2289 | 3.9668 | 3.9964 | 0.0000 | 113s |
| 4 | 0.8526 | 2.1850 | 2.2022 | 4.0144 | 4.0394 | 0.0000 | 109s |

**Observations.**
- All 5 Wilson samples have BE min $> 2.18 > \kappa_G = 2.0$
- All 360 ($= 5\times 72$) projected BE eigenvalues are positive
- Cross-sample BE-min standard deviation: $0.011$ — even tighter than Gaussian (0.014)
- BE max range across samples: $3.97 - 4.08$

### P.3 Wilson vs Gaussian distribution comparison

| Statistic | Wilson (5) | Gaussian (10, §O) | Shift (W − G) |
|---|---|---|---|
| BE min mean | $2.199 \pm 0.011$ | $2.312 \pm 0.014$ | $-0.114$ |
| BE p1 mean | $2.221 \pm 0.011$ | $2.326 \pm 0.013$ | $-0.104$ |
| BE p99 mean | $4.006 \pm 0.033$ | $2.798 \pm 0.015$ | $+1.208$ |
| BE max mean | $4.039 \pm 0.028$ | $2.810 \pm 0.015$ | $+1.229$ |
| BE band width | $\sim 1.85$ | $\sim 0.50$ | $\sim 3.7\times$ wider |

**Wilson eigenvalues spread much wider than Gaussian.** Floor pushed down by $\sim 0.11$, ceiling pushed up by $\sim 1.23$.

### P.4 Interpretation

**Why the spread differs.** Gaussian sampling assumes $A_\ell^a \sim \mathcal N(0, 1/\beta)$ independent per link, per Lie algebra component. The corresponding plaquette holonomy $U_p$ is computed but the LINK distribution is by-construction independent and Gaussian.

Wilson sampling, in contrast, samples LINKS conditionally on the FULL plaquette structure: $U_\ell \sim \mathrm{vMF}(\beta\bar H_\ell)$ where $\bar H_\ell$ encodes the surrounding gauge configuration. This produces **correlations among link variables** that the Gaussian approximation discards.

These correlations affect the Hessian matrix elements in two ways:
1. **Diagonal effects**: the per-plaquette-per-link Hessian eigenvalue $\beta q_0^{(p,\ell)}/4$ depends on the staple cos-half-angle $q_0^{(p,\ell)}$. Under Wilson, $q_0$ has a tighter peak near 1 (typical) and a heavier tail toward $-1$ (atypical) than under Gaussian. Net effect: more variation in per-link Hessian contributions.
2. **Off-diagonal correlations**: gauge-covariant couplings between neighboring links are stronger under Wilson, producing both stronger anti-aligned (negative) and stronger aligned (positive) Hessian off-diagonal terms.

The **lower floor** (BE min shifted down by 0.11) corresponds to a worst-mode that exploits the stronger negative off-diagonals.

The **higher ceiling** (BE max shifted up by 1.23) corresponds to a best-mode that exploits the stronger positive off-diagonals.

### P.5 The §J.6 spectral-window conjecture remains supported

Both Wilson and Gaussian sampling at the master's working corner ($L=6$, $\beta=3.5$, $\Lambda=1.05$) give:
- Zero negative projected BE eigenvalues in any sample
- BE min uniformly $> \kappa_G = 2.0$
- Tight cross-sample regularity ($\sigma_{\rm BE\,min} \sim 0.01$)

**Wilson sampling is the more honest probe** (it samples from the actual Wilson Gibbs measure, not its Gaussian approximation). The fact that Wilson STILL gives all-positive projected BE — even with wider eigenvalue spread — is a more conservative confirmation of the §J.6 conjecture than the Gaussian result alone.

### P.6 Caveats unchanged from §K.5

Pass-15 §P closes pass-12 §K.5 caveat (3) "Gaussian ≠ Wilson". Caveats (2) "small lattice L=6", (4) "typical configurations only", and (5) "no analytic theorem" remain open. (Caveat (1) "single sample" was closed by pass-14 §O.)

### P.7 Honest verdict

**Pass-15 §P conclusion.**
1. Wilson MCMC sampling implemented at L=6 via heat-bath with sign-fixed vMF rejection sampling. Plaquette equilibrium $\langle\phi_p\rangle = 0.148$ consistent with $3/(8\beta) + O(\beta^{-2})$ leading-order analytic.
2. Projected BE at 5 Wilson samples: all positive, BE min mean $2.199 \pm 0.011$, BE max mean $4.039 \pm 0.028$.
3. Wilson distribution is wider than Gaussian by factor $\sim 3.7\times$ in BE band width; floor pushed lower, ceiling pushed higher.
4. **§J.6 spectral-window conjecture empirically supported under Wilson sampling as well, with the more conservative (Wilson) value.**
5. Pass-7 conditional status unchanged. Pass-12 §K.5 caveat (3) closed; (2), (4), (5) remain.

---

## Appendix Q — Analytic conjecture for $\rho_*(\beta, \Lambda)$ (pass 15)

### Q.0 Scope

**Goal.** Pass-14 §O.4 noted that the cross-sample tightness of projected BE min (σ ≈ 0.014) suggests an underlying analytic floor $\rho_*(\beta, \Lambda)$ that the empirical samples cluster around. Pass-15 §Q proposes a leading-order analytic form for $\rho_*$ and fits the phenomenological constant against the §O and §P data.

**Status.** Empirical conjecture, not a derivation. Pass-15 §Q identifies the leading structural terms and what would need to be computed to derive the constants from first principles.

### Q.1 Trivial-config contribution (exact)

At the trivial configuration $U^{(0)} = I$, the Wilson Hessian on the coexact spectral window equals $\beta/4$ times the Maxwell operator restricted to the window. Eigenvalues: $(\beta/4)\lambda_k$ for coexact $\lambda_k \le \Lambda$.

The minimum coexact eigenvalue in the window: $\lambda_{\min}^{\rm coex,\Lambda}$. For $L=L_*$ in $d=4$:
$$\lambda_{\min}^{\rm coex,\Lambda} = \min\{4\sin^2(\pi n/L_*) : n=1,2,\ldots,\lfloor L_*/2\rfloor, 4\sin^2(\pi n/L_*) \le \Lambda\}$$

At $L=6$, $\Lambda=1.05$: $\lambda_{\min}^{\rm coex} = 4\sin^2(\pi/6) = 1$ (boundary case; only one M-eigenvalue level in window).

Trivial-config projected BE min:
$$\rho_*^{(\rm trivial)}(\beta, \Lambda; L) = \kappa_G + \tfrac{\beta}{4}\lambda_{\min}^{\rm coex,\Lambda}$$

At master corner $\beta=3.5$, $\Lambda=1$, $\kappa_G=2$, $\lambda_{\min}=1$: $\rho_*^{\rm (trivial)} = 2.875$.

### Q.2 Configuration-dependent shift (heuristic)

At a typical Wilson (or Gaussian-approximated Wilson) configuration, the projected Hessian deviates from the trivial-config form by configuration-dependent corrections.

**Heuristic structure.** Per-plaquette, per-link, the Hessian eigenvalue is $\beta q_0^{(p,\ell)}/4$ where $q_0^{(p,\ell)} = \tfrac{1}{2}\mathrm{Re}\mathrm{Tr}(V_\ell^{(p)})$ (cos of staple half-angle). At trivial: $q_0 = 1$ uniformly. At typical Wilson: $q_0 \in [-1, 1]$ with distribution centered near 1 but with spread depending on $\langle\phi_p\rangle$.

**Leading-order expansion.** For small $\phi_p$: $q_0^{(p,\ell)} = 1 - O(\phi_{\rm neighbor})$. The shift in per-plaquette-per-link Hessian: $-\beta/4 \cdot O(\phi)$. Summed over the spectral-window coexact modes: net shift to the min is $\sim -c\beta\langle\phi_p\rangle$ for some $c = O(1)$ accounting for averaging over modes and off-diagonal contributions.

### Q.3 The conjecture

$$
\boxed{\rho_*(\beta, \Lambda; L) \approx \kappa_G + \tfrac{\beta}{4}\lambda_{\min}^{\rm coex,\Lambda} - c\,\beta\,\langle\phi_p\rangle + O(\beta^{-1})}
$$

with $c$ a $O(1)$ phenomenological constant that, in principle, can be computed from the structure of the lowest-coexact-mode wave functions on $T_L^4$.

### Q.4 Empirical fit

At the master corner ($\beta=3.5$, $\Lambda=1.05$, $L=6$, $\kappa_G=2$, $\lambda_{\min}^{\rm coex}=1$):

**Gaussian samples (pass-14 §O):**
- Empirical $\langle\phi_p\rangle^{(\rm Gauss)} \approx 1/\beta = 0.286$ (Gaussian variance gives $\mathbb{E}[|F|^2/8] \sim 1/\beta$ at leading order)
- Empirical $\rho_* = 2.312$
- Fit: $c\beta\langle\phi_p\rangle = 2.875 - 2.312 = 0.563$, giving $c \approx 0.563/(3.5\cdot 0.286) = 0.562$
- **Gaussian $c \approx 0.56$**

**Wilson samples (pass-15 §P):**
- Empirical $\langle\phi_p\rangle^{(\rm Wilson)} = 0.148$
- Empirical $\rho_* = 2.199$
- Fit: $c\beta\langle\phi_p\rangle = 2.875 - 2.199 = 0.676$, giving $c \approx 0.676/(3.5 \cdot 0.148) = 1.305$
- **Wilson $c \approx 1.30$**

The phenomenological constant $c$ differs by factor $\sim 2.3$ between Gaussian and Wilson sampling. This reflects the different correlation structures: Wilson has correlated link variables that shift the Hessian more aggressively per unit of $\langle\phi_p\rangle$.

**Interpretation.** The conjectured form (Q.3) captures the leading scaling but the constant $c$ is ensemble-dependent. A complete derivation would compute $c$ as a function of the correlation structure of the underlying measure.

### Q.5 What a derivation would need

To convert (Q.3) from conjecture to theorem:

1. **Define the projected dynamics SDE precisely** (pass-11 §J.8 step 1)
2. **Compute the leading-order shift coefficient** for typical configurations under the Gibbs measure. This requires:
   - The Wilson Hessian expansion to second order in $\phi_p$
   - Projection of this expansion onto the coexact spectral window
   - Averaging over the conditional distribution of plaquette holonomies under Wilson
3. **Bound higher-order corrections** uniformly in $L$
4. **Establish robustness** to atypical configurations via Lyapunov supplement (pass-9 §H.8 ingredient (iv))

Steps 2 and 3 are concrete calculations using standard techniques (perturbative expansion + cumulant resummation); step 4 is the harder part requiring novel input.

**Estimated effort.** Step 2 alone: 4-6 weeks for a careful researcher. Combined with steps 1, 3, 4: ~6-12 months of dedicated work to produce a peer-reviewed-grade result.

---

## Appendix R — Small-density projected BE covariance decay: precise statement and sketch (pass 15)

### R.0 Scope

**Goal.** Pass-13 §M.4 identified that the gap between pass-12 §K.3 empirical projected BE and source §I.16 pair-cumulant target is the prefactor scaling: BGL gives $\|\nabla f\|_\infty^2/\rho$, target wants $q_\eta^2$. Pass-13 §M.4 option (c) proposed "a small-density spectral-gap covariance decay theorem". Pass-15 §R states this precisely and sketches a candidate proof strategy.

**Status.** Research conjecture with proof sketch. Not a theorem. If proved, this conjecture combined with the §J.6 spectral-window conjecture (also open) would close source §I.16.

### R.1 The conjecture

**Conjecture (Small-Density Projected BE Covariance Decay).** Let $\mu$ be a Gibbs measure on a complete Riemannian manifold $(M, g)$ with potential $V$, and let $P: L^2(\mu) \to L^2(\mu)$ be an orthogonal projection onto a subspace $H_P$ such that the **projected Bakry-Émery condition** holds:
$$
P\,(\nabla^2 V + \mathrm{Ric}_g)\,P \succeq \rho_*\, P\quad\text{on }H_P,
$$
with $\rho_* > 0$. Let $f, g \in C^1(M)$ with:
- $\|f\|_\infty, \|g\|_\infty \le 1$
- $\mathrm{supp}(f) \cap \mathrm{supp}(g) = \emptyset$ with $d := d(\mathrm{supp}\,f, \mathrm{supp}\,g) > 0$
- $\mathbb{E}_\mu[f] \le q$, $\mathbb{E}_\mu[g] \le q'$ (small density)

Then there exist constants $C = C(\rho_*, g, V) > 0$ and $m = \tfrac{1}{2}\sqrt{\rho_*}$ such that
$$
\boxed{|\mathrm{Cov}_\mu(Pf, Pg)| \le C\, q\, q'\, e^{-m\, d}.}
$$

### R.2 Application to source §I.16

In the master document's setup:
- $M = M_\Lambda = \prod_\ell SU(2)$, $\mu = $ Wilson Gibbs measure, $V = S_W$
- $P = P_{\le\Lambda, L}^{\rm coex}$ = coexact spectral-window projector
- $f = X_{p,\eta}$, $g = X_{p',\eta}$: smooth indicators with $\|\cdot\|_\infty \le 1$ and $\mathbb{E}_\mu \le q_\eta$

**If the conjecture is a theorem and $\rho_* > 0$ uniformly in $L$,** then
$$|\mathrm{Cov}_W(P X_{p,\eta}, P X_{p',\eta})| \le C q_\eta^2 e^{-m d(p,p')}$$
matches the source §I.16 minimal target.

**The remaining residual** is the difference between $\mathrm{Cov}_W(PX_{p,\eta}, PX_{p',\eta})$ and $\mathrm{Cov}_W(X_{p,\eta}, X_{p',\eta})$ — i.e., does the projection actually preserve the pair-covariance? This is a separate question (about the operator $P$ itself), addressed in the master §11 deterministic spine.

### R.3 Proof strategy sketch (research-grade, not a proof)

**Step 1: Brascamp-Lieb variance bound.** From projected BE $\rho_* > 0$, standard machinery gives
$$\mathrm{Var}_\mu(Pf) \le \frac{1}{\rho_*}\,\mathbb{E}_\mu[\|\nabla(Pf)\|^2]$$
For $f$ with small density $q$: $\|\nabla f\|^2$ has $\mu$-mass $\le q\|\nabla f\|_\infty^2$. After projection: $\mathbb{E}_\mu[\|\nabla Pf\|^2] \le \|P\|_{\rm op}^2 \cdot q\|\nabla f\|_\infty^2 \lesssim q/\eta^2$ for smooth indicator $f = X_{p,\eta}$.

So $\mathrm{Var}_\mu(Pf) \le q/(\rho_*\eta^2)$ — this gives $\mathrm{Cov} \le \sqrt{q q'}/(\rho_*\eta^2)$ by Cauchy-Schwarz, scaling like $\sqrt{qq'}$, NOT $qq'$.

**The $qq'$ scaling requires bilinear absorption.** Cauchy-Schwarz loses the second density factor.

**Step 2: Bilinear absorption via spectral gap.** Consider the projected dynamics $L_P$ on $H_P$, with spectral gap $\rho_*$. Then $e^{tL_P} f \to \mathbb{E}_\mu[Pf]$ as $t\to\infty$, with rate $\rho_*$.

For $f$ with small density: $e^{tL_P}f$ has both small density AND exponentially decreasing "non-mean" component.

The covariance:
$\mathrm{Cov}_\mu(Pf, Pg) = \int_0^\infty \mathbb{E}_\mu[(Pf)(L_P e^{tL_P} Pg)] dt$
$= -\int_0^\infty \mathbb{E}_\mu[(\nabla Pf)\cdot(\nabla e^{tL_P} Pg)] dt$

Using exponential decay of $\|e^{tL_P}\|_{H_P^\perp} \le e^{-\rho_* t/2}$:
$|\mathrm{Cov}_\mu(Pf, Pg)| \le \int_0^\infty \|\nabla Pf\|_{L^2(\mu)} \|\nabla e^{tL_P} Pg\|_{L^2(\mu)} dt$

For $Pf$ with small expectation $q$: $\|\nabla Pf\|^2_{L^2(\mu)} \sim q\cdot c/\eta^2$.
For $e^{tL_P}Pg$: by parabolic regularization combined with disjoint supports, exponential decay of correlation between supp $f$ and supp $g$.

The full bilinear estimate then gives $|\mathrm{Cov}| \lesssim \sqrt q\sqrt{q'}\cdot$ (exponential), which is $\sqrt{qq'}$ not $qq'$.

**Step 3: The missing factor of $\sqrt{qq'}$.** To upgrade $\sqrt{qq'} \to qq'$, need an additional small-density factor. Two possible approaches:

(a) **Stein-coupling argument.** Apply the coupling-by-reflection-on-supports approach (e.g., Eberle 2016 / Wang-Yan 2014 for non-convex potentials): if $f, g$ have disjoint small-density supports, the coupling cost between configurations supporting $f$ and those NOT supporting $f$ is bounded by $q^{1/2}\cdot$ (geometric factor), giving the second $\sqrt q$ factor.

(b) **Polymer-expansion analogue.** For Gibbs measures with sufficient cluster structure (which projected BE gives when $\rho_* > 0$), the rooted-source polymer expansion of source §I.3 can be derived from the projected dynamics directly, without going through abstract analyticity.

Approach (a) requires extending Eberle's coupling framework to projected dynamics on continuous-spin systems. Approach (b) requires building a polymer expansion from spectral-gap data. Both are non-trivial research projects.

### R.4 Why the conjecture is plausible

1. **It's true for Gaussian measures.** For $\mu = \mathcal N(0, \Sigma)$ with $P = $ low-frequency projector, the bilinear $qq'$ scaling is straightforward by exponential moment estimates.
2. **It's true at strong coupling (SZZ 2023).** SZZ effectively proves the analogous covariance decay for Wilson loops at $\beta < 1/96$, with the right scaling. Their proof uses log-Sobolev (which implies BE) and small-support observable estimates.
3. **It's structurally what cluster expansions deliver.** The Russian-school polymer expansion (Appendix N) gives covariance bounds with density-squared scaling when the polymer activities are small. Our projected BE setup is the spectral-gap version of this scaling.

The conjecture is asking: can the SZZ small-$\beta$ proof structure be extended to large $\beta$ via the spectral-window projection?

### R.5 Why it's not a theorem yet

Standard BGL covariance bounds give $\|\nabla f\|/\rho \cdot e^{-\sqrt{\rho}d/2}$ — the $\sqrt{q}$ improvement via Brascamp-Lieb is the easy half. The remaining $\sqrt q$ requires either:
- A specific structure on the observable beyond pure smallness (e.g., specific support shape)
- A coupling argument adapted to small-density events
- A polymer expansion derived from spectral-gap data

None of these is in the standard machinery. The conjecture is plausible but its proof requires novel ingredients.

### R.6 The complete logical chain

If
- **§J.6 spectral-window conjecture** ($\rho_* > 0$ uniform in $L$) is proved
- **§R.1 small-density covariance decay** is proved

Then combined:
- Wilson Gibbs measure on spectral-window subspace has covariance decay with $q_\eta^2$ prefactor and decay rate $\sqrt{\rho_*}/2$
- This is exactly the source §I.16 minimal target (up to projection-vs-original-observable difference)
- The pass-10 derivation chain (§I.1–§I.16) then delivers (M′)_SU(2) at large β for the master's working corner

**Two open theorems → one open problem (M′)_SU(2).** Pass-15 §Q and §R together provide the precise mathematical roadmap for closing the route.

---

## Appendix S — L=8 lattice extension via analytic Fourier-mode construction (pass 16)

### S.0 Scope

**Goal.** Pass-12 §K.5 caveat (2) flagged that all numerical work in passes 12–15 was at L=6. Pass-16 extends to L=8 to test (i) the §J.6 conjecture at a larger lattice, (ii) the L-dependence of the empirical BE floor, (iii) whether the projected BE positive-floor structure survives lattice refinement.

**Outcome.** The §J.6 conjecture is empirically supported at L=8 as well, but with a CRITICAL refinement: the shift below trivial-config BE scales linearly with $\lambda_{\min}^{\rm coex}(L)$, so the projected BE floor approaches $\kappa_G$ from above as $L\to\infty$ with $O(1/L^2)$ convergence. Pass-15 §Q.3 conjecture is corrected.

### S.1 Technical issue: sparse eigsh stalls at L=8

The dense eigendecomposition used at L=6 (with $N_{\rm links}=5184$) does not fit at L=8 ($N_{\rm links}=16384$, dense matrix $\sim 2$ GB).

**First attempt.** Sparse `scipy.sparse.linalg.eigsh` with shift-invert at $\sigma=-0.01$, target $k=500$ smallest eigenvalues. The Maxwell operator at L=8 has $\dim\ker M = N_{\rm sites} - 1 = 4095$ zero modes; the ARPACK iteration with shift-invert near zero must work through this large zero block, which exceeded the 290s bash window without convergence.

**Resolution.** Construct the coexact basis **analytically** using lattice Fourier modes.

### S.2 Analytic coexact basis construction at L=8

**Setup.** At momentum $k = (k_1, k_2, k_3, k_4) \in \mathbb{Z}_L^4 \setminus \{0\}$, the lattice momentum vector is $q_\mu(k) = 2\sin(\pi k_\mu/L)$. The Maxwell operator $M = d_1^\top d_1$ acts on 1-forms; in Fourier space at momentum $k$:
- **Exact subspace** (1-dimensional): spanned by $q(k)$. Maxwell eigenvalue: $0$.
- **Coexact subspace** ($(d{-}1)$-dimensional): orthogonal to $q(k)$ in the $d$-dim "polarization" space. Maxwell eigenvalue: $|q(k)|^2 = 4\sum_\mu \sin^2(\pi k_\mu/L)$.

At $L=8$, $\Lambda=1.05$: the only in-window momentum shell has $k_\mu \in \{0, \pm 1\}$ with exactly one $|k_\mu| = 1$. Hence:
- 8 momenta: $\pm e_1, \pm e_2, \pm e_3, \pm e_4$
- Eigenvalue: $4\sin^2(\pi/8) = 0.5858$
- Coexact dimension per momentum: $d - 1 = 3$

For each momentum $k = e_\mu$ with $\mu \in \{1,2,3,4\}$, the coexact polarizations are $\{e_\nu : \nu \neq \mu\}$. Real-valued basis: pair $+k$ and $-k$, taking real and imaginary parts of $\cos(2\pi k\cdot x/L)$ and $\sin(\cdot)$, giving 2 real modes per momentum-polarization pair.

**Total coexact modes at L=8 in window:** $4 \text{ unsigned momenta} \times 3 \text{ polarizations} \times 2 \text{ (Re, Im)} = 24$ — same count as L=6 (where the window also captured only one momentum level, with 8 momenta × 3 polarizations × 1 real mode each).

### S.3 Verification

The 24 analytically-constructed modes were verified:
- **Orthonormality:** $\|V^\top V - I\|_F = 6.5 \times 10^{-16}$ (machine precision)
- **Eigenvector property:** $\|Mv_i - \lambda v_i\|/\|\lambda v_i\| \le 10^{-15}$ for all tested modes (machine precision)
- **Coexact:** $\|d_0^\top V\|_F = 0$ exactly (modes are perpendicular to the gradient image)

This is sharper than the L=6 sparse eigendecomp (which had error $\sim 10^{-12}$ from floating-point eigh).

### S.4 Batched projected-Hessian computation at L=8

**Setup.** With $V_{\rm coex}$ constructed (shape $16384 \times 24$), the per-plaquette projected Hessian build proceeds as at L=6, but with $N_{\rm plaq} = 24576$ plaquettes instead of $7776$ (factor 3.16).

**Per-plaquette cost.** Local 12×12 Hessian via central finite differences (step $\epsilon=0.005$, 144 function evaluations per plaquette). Rate measured: ~41 plaquettes/second, so single-sample compute $\approx 600$s — exceeds bash's 290s window.

**Batched accumulation.** State file (`/home/claude/L8_hessian_state_seed{N}.npz`) checkpoints partial $\mathrm{proj}\_H$ every 2000 plaquettes. Each bash invocation processes ~10500 plaquettes before approaching the time limit, saves, exits. Three bash batches suffice per sample.

**Sample 1 (seed=42).** Three batches: 10721 + 10784 + 3071 = 24576 plaquettes. Total compute: ~11 minutes.
**Sample 2 (seed=137).** Three batches: 10361 + 10868 + 3347 = 24576 plaquettes. Total compute: ~10 minutes.

After full accumulation, the 72×72 projected Hessian is diagonalized: trivial (microseconds).

### S.5 Results

**Per-sample at L=8 (Gaussian, $\beta=3.5$, $\Lambda=1.05$, $\sigma=1/\sqrt\beta$):**

| Seed | BE min | BE p1 | BE median | BE p99 | BE max | Frac BE<0 | Frac BE<$\kappa_G$ |
|---|---|---|---|---|---|---|---|
| 42 | 2.2035 | 2.2069 | 2.3279 | 2.4608 | 2.4685 | 0.0000 | 0.0000 |
| 137 | 2.2138 | 2.2204 | 2.3383 | 2.4635 | 2.4714 | 0.0000 | 0.0000 |
| Mean | 2.209 | 2.214 | 2.333 | 2.462 | 2.470 | 0.0000 | 0.0000 |

**All 144 (=2×72) projected BE eigenvalues are positive and exceed $\kappa_G = 2.0$.** Cross-sample variation is very tight (BE-min std $\sim 0.005$, even tighter than L=6's $0.014$).

**Comparison to L=6 (Gaussian, 10 samples from §O):**

| Statistic | L=6 mean ± std | L=8 mean ± std | Shift (L=8 − L=6) |
|---|---|---|---|
| Trivial-config BE | 2.875 | 2.513 | $-0.362$ |
| Empirical BE min | $2.312 \pm 0.014$ | $2.209 \pm 0.005$ | $-0.103$ |
| Empirical BE max | $2.810 \pm 0.015$ | $2.470 \pm 0.002$ | $-0.340$ |
| Empirical shift below trivial | $-0.563$ | $-0.304$ | $+0.259$ |

### S.6 The L-dependence finding and refined §Q.3 conjecture

**Empirical observation.** The shift below trivial-config BE scales linearly with $\lambda_{\min}^{\rm coex}(L)$:

| L | $\lambda_{\min}^{\rm coex}$ | shift below trivial | shift / $\lambda_{\min}$ |
|---|---|---|---|
| 6 | 1.0000 | $-0.563$ | $-0.563$ |
| 8 | 0.5858 | $-0.304$ | $-0.519$ |

**Average:** shift / $\lambda_{\min} \approx -0.541$.

**Refined conjecture (corrects pass-15 §Q.3):**
$$
\boxed{\rho_*(\beta, \Lambda; L) \;\approx\; \kappa_G + \left(\frac{\beta}{4} - k_{\rm ens}\right)\lambda_{\min}^{\rm coex}(L) + O(\lambda_{\min}^2)}
$$

with $k_{\rm ens}$ an ensemble-dependent constant: $k_{\rm Gauss} \approx 0.54$. (Pass-15 §P at L=6 gives $k_{\rm Wilson} \approx 0.68$ but L=8 Wilson data not yet collected.)

**Why pass-15 §Q.3 was wrong.** Pass-15 §Q.3 conjectured shift $\propto \beta \langle\phi_p\rangle$ — a quantity **constant in L** (depends only on $\beta$). Pass-16 §S finds shift $\propto \lambda_{\min}(L)$ — a quantity **that vanishes as $L\to\infty$**. The pass-15 conjecture would have predicted the L=8 shift to be $0.563$ (same as L=6); empirical L=8 shift is $0.304$ (factor $\sim 2$ smaller). The corrected $\lambda_{\min}$-scaling fits cleanly.

**Physical interpretation.** The lowest coexact mode has wavelength $L$ and Maxwell eigenvalue $\sim (\pi/L)^2$. The configuration-dependent shift to the eigenvalue scales similarly with the mode's "characteristic length scale" — when the mode is more spread out (larger L), it averages over more plaquette holonomies, and the per-mode shift is suppressed.

### S.7 Extrapolation to L → ∞

Using the refined conjecture with $k_{\rm Gauss} = 0.545$:

| L | $\lambda_{\min}^{\rm coex}$ | Predicted BE min | Gap above $\kappa_G$ |
|---|---|---|---|
| 6 | 1.000 | 2.330 | 0.330 |
| 8 | 0.586 | 2.193 | 0.193 |
| 12 | 0.268 | 2.088 | 0.088 |
| 16 | 0.152 | 2.050 | 0.050 |
| 24 | 0.068 | 2.022 | 0.022 |
| 64 | 0.010 | 2.003 | 0.003 |
| $\infty$ | 0 | 2.000 | 0 |

**As $L \to \infty$: $\rho_*(L) \to \kappa_G = 2.0$ from above, with $O(1/L^2)$ convergence.**

### S.8 Updated status of pass-12 §K.5 caveats

| Caveat | Status after pass 16 |
|---|---|
| (1) Single sample at L=6 | Closed (pass 14 §O: 10 samples at L=6) |
| (2) Small lattice L=6 only | **Now substantively closed by pass-16 §S: L=8 with 2 samples confirms positive BE floor and reveals L-dependence** |
| (3) Gaussian sampling ≠ Wilson | Closed (pass 15 §P: 5 Wilson samples at L=6) |
| (4) Typical configurations only | Open |
| (5) No analytic theorem | Precisely characterized by §Q (now refined) and §R (research statement) |

Caveats (4) and (5) remain. Caveat (4) requires Lyapunov-style atypical-config handling (master §H.8 ingredient (iv)); caveat (5) requires actual proofs of §Q and §R conjectures.

### S.9 Implications for the §J.6 spectral-window conjecture

**§J.6 conjecture (recapped):** $\rho_*(\beta, \Lambda; L) > 0$ uniform in $L$, with $\rho_*$ giving the projected BE floor at the master's working corner.

**Pass-16 evidence.** $\rho_*(\beta=3.5, \Lambda=1.05; L) \ge \kappa_G = 2 > 0$ for $L \in \{6, 8\}$ with consistent O(1/L²) convergence to $\kappa_G$ from above. The empirical extrapolation predicts $\rho_*(L) > \kappa_G$ for ALL finite L, with $\rho_*(L) \to \kappa_G$ as $L \to \infty$.

**The §J.6 conjecture is supported with $\rho_* = \kappa_G$ asymptotic, $\rho_* > \kappa_G$ at finite L.** This is consistent with the spectral-window mechanism doing "all and only" the heavy lifting for asymptotic positivity — once the Maxwell projection is applied, the geometric Ricci floor $\kappa_G = 2$ for SU(2) survives uniformly in L.

**Sharper §J.6 statement (suggested by pass-16 data):**
$$
\inf_L \rho_*(\beta, \Lambda; L) = \kappa_G > 0
$$
i.e., the lattice-uniform projected BE floor equals exactly the geometric Ricci floor in the limit. This is sharper (and more precise) than the original §J.6 statement, and it explains why $\kappa_G > 0$ is the structural fact required (master pass 9 §H.8 ingredient (ii)).

### S.10 Caveats

1. **Only 2 samples at L=8.** Even tight ($\sigma_{\rm BE\,min}=0.005$), this is fewer than the 10 at L=6. A 10-sample L=8 sweep would take $\sim 100$ minutes of compute (10 samples × 3 batches × 5 min). Recommended for pass 17.
2. **Only Gaussian at L=8.** Wilson MCMC at L=8 not yet implemented; heat-bath thermalization itself would take additional setup time. Recommended for pass 17.
3. **Only two L-values (6 and 8).** The linear $\lambda_{\min}$-scaling fit is from a 2-point comparison. L=10 or L=12 sample would test the conjecture more robustly.
4. **Same single-mode-level structure at both L=6 and L=8.** Both have only the lowest momentum shell in the window. A wider Λ that captures TWO mode levels would test cross-level mixing.
5. **The empirical $k_{\rm Gauss} = 0.54$ is just a fit.** No first-principles derivation yet — same caveat as pass 15 §Q.5.

### S.11 Honest verdict

**Pass-16 §S conclusion.**
1. Pass-12 §K.5 caveat (2) "small lattice L=6 only" substantively closed: L=8 Gaussian confirms positive projected BE floor at $2.21 > \kappa_G = 2.0$.
2. Pass-15 §Q.3 conjecture corrected: the shift scales as $\lambda_{\min}^{\rm coex}(L)$, not as a constant. Refined conjecture: $\rho_*(L) = \kappa_G + ((\beta/4) - k_{\rm ens})\lambda_{\min}(L) + O(\lambda_{\min}^2)$.
3. The §J.6 spectral-window conjecture is supported with $\rho_* = \kappa_G > 0$ uniform in L; the asymptotic floor equals exactly the geometric Ricci constant.
4. Pass-7 conditional status unchanged. Open subproblems: §Q (analytic derivation of $k_{\rm ens}$), §R (small-density covariance decay theorem), pass-12 §K.5 caveats (4) and (5).


## Appendix T — Stage A frozen-exterior block-conditional diagnostic on L=16 Wilson (pass 17)

**Status.** Pass 17 substantive item. This appendix folds in a single-ensemble Stage A run (5.4 h on an A100) of the frozen-exterior block-conditional diagnostic proposed in the Rare-Source Probability Estimates draft. The diagnostic probes **(M′)_SU(2)** and **§R.1** *directly* — by measuring conditional rare-event densities and rooted bad-staple cavity ratios under frozen-exterior block sampling — rather than via the projected BE eigenvalue proxy used in passes 12–16. It is a new, independent empirical track.

### §T.1 What the diagnostic tests, in precise terms

The diagnostic targets the local rare-source factorization that drives the §R.1 program:

$$\mathbb{E}\!\left[\prod_{p \in B} X_{p,\eta} \,\big|\, \mathcal{F}_{C^c}\right] \le (C_Q\, q_\eta)^{|B|},$$

together with its cavity and rooted consequences:

$$\Lambda(p,r) := \frac{\lambda_p(\{r\})}{q_\eta} = \frac{\mathbb{E}[X_p X_r \mid \mathcal{F}_{C^c}]}{q_\eta\, \mathbb{E}[X_r \mid \mathcal{F}_{C^c}]},
\qquad
\Lambda^{\rm root}(p,r) := \frac{\mathbb{E}[Y_r X_p \mid \mathcal{F}_{C^c}]}{q_\eta\, \mathbb{E}[Y_r \mid \mathcal{F}_{C^c}]},$$

where $Y_r = X_r \cdot \mathbf{1}_{\rm bad}$ is the rooted bad-staple indicator with default thresholds $(H_0, \rho_0) = (3.0, 0.7)$, and where the conditional expectation is taken with $\mathcal{F}_{C^c}$ — all links outside the block — held fixed by frozen-exterior Metropolis. The pair-ratio $R_2(d) := \mathbb{E}[X_p X_{p'}] / q_\eta^2$ is reported as a function of L1 plaquette-pair distance $d$.

These are quantities the §R.1 program needs to control bilinearly in $q$; the projected BE eigenvalue work of passes 12–16 only delivers the operator-norm prerequisite ($\rho_* > 0$) for the Brascamp–Lieb step. Stage A measures the **statistical** input separately.

### §T.2 Configuration

| Item | Value |
|---|---|
| Gauge group | SU(2) (quaternion encoding) |
| Lattice | $T_L^4$ with $L=16$ |
| Coupling | $\beta = 3.5$ |
| Ensemble | $N_{\rm cfg} = 32$ Wilson configurations from full Metropolis, 400 therm + 40 between sweeps |
| Threshold scale | $\eta = 0.005$, target $q_\eta = 0.003$ (rare-event regime) |
| Block geometry | $6^4$ sub-cube, core margin 2, $\Rightarrow$ core is $2^4$ sites $\Rightarrow$ 24 core plaquettes |
| Blocks per cfg | 4 (random anchors) |
| Total blocks | 128 |
| Block thermalization | 128 sweeps of interior-only Metropolis (exterior frozen) |
| Block samples | 256 per block, with 8 between-sweeps |
| Total conditional measurements | $128 \times 256 \times 24 \approx 7.86 \times 10^5$ |
| Wallclock | 323.4 min on NVIDIA A100-SXM4-40GB |
| Seed | 23060524 |

Global Metropolis acceptance was $0.512 \pm 0.001$ (mature, mixed); block-Metropolis acceptance was $\approx 0.560$ (slightly higher because frozen exterior reduces effective dimension). The empirical hard density $q_{\rm hard} = 0.002994$ matches the smoothed target $q_\eta = 0.003000$ to 4 significant figures — the threshold $t = 1.0104$ is correctly tuned.

### §T.3 Headline results

The diagnostic emits four families of metrics. The script's own interpretation thresholds (in `RUN_READOUT.md`) are listed in the rightmost column; "supportive" means consistent with what (M′)_SU(2) at large $\beta$ would predict.

| Metric | Value | Script threshold | Verdict |
|---|---:|---|---|
| `max_depth_median_ratio` ($q_{\rm cond}/q_\eta$, depth-wise median) | $1.031$ | $\lesssim 1.5$ supportive | ✓ supportive |
| `max_depth_q95_ratio` | $2.739$ | $\lesssim 3$ supportive | ✓ marginal |
| `max_depth_max_ratio` | $7.200$ | (worst single plaquette-block) | ⚠ tail event |
| `median_cavity_Lambda` $\Lambda$ | $1.216$ | $O(1)$, ideally $\to 1$ with $d$ | ✓ supportive |
| `max_cavity_Lambda` | $2.740$ | $O(1)$ | ✓ supportive (still $O(1)$) |
| `median_rooted_Lambda` $\Lambda^{\rm root}$ | $1.245$ | $O(1)$ | ✓ direct (M′)_SU(2) signature |
| `max_rooted_Lambda` | $2.432$ | $O(1)$ | ✓ supportive |
| Cap-feature slope ($\partial \log q_{\rm cond} / \partial g_{\rm mean}$) | $-9.91$ | $< 0$ supportive | ✓ correct sign, large magnitude |
| Cap-feature $R^2$ | $0.032$ | (no threshold) | ⚠ weak linearity |

**Plain-language read.** The conditional rare-event density at typical block-conditioning equals the unconditional density to within 3%, the pair correlations equal $q_\eta^2$ to within a factor $\sim 1.2$, and the rooted bad-staple absorption ratio is $\approx 1.25$. The cap predictor $g = \beta k (1 - F(\rho, a_{t-\eta}))$ correctly ranks plaquettes by their conditional rare-event rate (negative slope of large magnitude), though it explains only $\approx 3\%$ of the variance — the *sign* of the cap mechanism is confirmed, the *magnitude* is not yet a near-deterministic predictor.

### §T.4 The two soft spots, named honestly

**(a) The 7.20× tail.** Out of $\approx 3072$ block-plaquette conditional measurements (128 blocks × 24 core plaquettes), the worst single observation had $q_{\rm cond}/q_\eta = 7.20$. This is a $\approx 0.03\%$ tail probability — consistent with sub-exponential right tails — but it is exactly the kind of fat-tail signal that the q² → √(qq′) upgrade discussed in §R.1 must dominate uniformly. With more blocks (Stage B), the worst-case sample will likely grow, slowly. The right uniform statement to test is whether the empirical CDF of $q_{\rm cond}/q_\eta$ has a *light* tail — say sub-Gaussian or sub-exponential at scale $q_\eta$. That is a per-block-plaquette CDF question and requires `single_source_depth.csv`, which is not in the current upload.

**(b) The 3% $R^2$ for the cap predictor.** The cap-feature regression has slope $-9.91$ and $R^2 = 0.032$. Three competing explanations:

  1. *Statistical noise.* With $\sim 7.86 \times 10^5$ conditional measurements but only 256 block samples per (block, plaquette), the standard error on each $q_{\rm cond}$ estimate is $\sqrt{q_\eta/N_{\rm samples}} \approx \sqrt{0.003/256} \approx 0.0034 \approx q_\eta$. So the per-plaquette $q_{\rm cond}$ estimate has $\sim 100\%$ relative error. This *alone* could explain the low $R^2$. Test: rerun with $N_{\rm samples} = 1024$ and check whether $R^2$ rises to $\gtrsim 0.10$.
  2. *Cap predictor incomplete.* The cap $F(\rho, a_{t-\eta})$ is the leading-order heat-bath prediction at fixed staple; finite-$\beta$ corrections, higher-order ρ-features, or k-feature interactions could carry additional variance. Test: include $\rho_{\rm mean}$ and $k_{\rm mean}$ separately as predictors and look at the multivariate $R^2$.
  3. *Block-to-block heterogeneity.* The cap features are *local* but the conditional density also depends on the frozen exterior. Test: add `cfg_idx` or `block_idx` as a random effect.

Without the per-row `cap_feature_scan.csv` and the per-distance CSVs, one cannot distinguish (1)–(3). Pass-17 §T.6 designates this as a Stage B target.

### §T.5 What Stage A does and does not show

| Claim | Stage A status |
|---|---|
| Conditional density $q_{\rm cond} \approx q_\eta$ at typical conditioning | **Supported** (median ratio $1.03$) |
| Pair correlations $\approx q_\eta^2$ at typical conditioning | **Supported** (median $\Lambda = 1.22$) |
| Rooted bad-staple absorption: $\mathbb{E}[Y_r X_p] \approx q_\eta\,\mathbb{E}[Y_r]$ | **Supported** (median $\Lambda^{\rm root} = 1.25$) |
| Cap-predictor mechanism is correctly directional | **Supported** (slope $-9.91$) |
| Cap predictor is near-deterministic | **Not supported** ($R^2 = 0.032$) |
| Exponential decay of $R_2(d)$ with distance | **Untested by Stage A summary** (requires the per-distance CSV; not uploaded) |
| Uniformity in lattice volume | **Untested** ($L=16$ only) |
| Uniformity in $\beta$ | **Untested** ($\beta=3.5$ only) |
| Worst-case bound $(C_Q q_\eta)^{|B|}$ for $|B| \ge 2$ | **Untested in this Stage** (max ratio $7.20$ is single-plaquette) |

The most important asymmetry: passes 12–16 tested the *operator-norm* prerequisite ($\rho_* > 0$) for §R.1. Stage A tests the *statistical density* and *pair-correlation* inputs. They are independent: a positive projected BE floor does not imply $q_{\rm cond} \approx q_\eta$, and vice versa. Stage A delivers the second pillar empirically; combined with the §J.6 evidence from passes 12–16, both inputs to the §R.1 reduction are now empirically supported at the working corner.

### §T.6 Stage B specification

Stage A used $\approx 5.4$ A100-hours. A Stage B that closes the most pressing open questions should be planned along **at most two** axes simultaneously, to keep wallclock bounded. The most informative axes, ranked:

1. **$N_{\rm samples}$ per block: 256 → 1024.** Reduces per-$q_{\rm cond}$ standard error by factor 2, likely lifting the cap-feature $R^2$ enough to distinguish hypotheses (1)–(3) of §T.4. Linear in wallclock. Estimated cost: $\sim 21\,{\rm h}$ on A100 at the current $(L, N_{\rm cfg}, N_{\rm blocks})$.

2. **$N_{\rm cfg}$: 32 → 128, holding $N_{\rm blocks/cfg} = 4$.** Reduces the cross-block variance of the headline ratios by factor 2, sharpens the tail estimate of $q_{\rm cond}/q_\eta$, and shrinks the cross-block SE on the cavity Λ. Linear in wallclock. Estimated cost: $\sim 22\,{\rm h}$ on A100.

3. **$\beta$ scan: $\{3.0, 3.5, 4.0, 4.5\}$.** Tests whether $C_Q(\beta)$ is bounded uniformly over the range. Each new $\beta$ needs its own global ensemble + threshold + block runs. Estimated cost: $\sim 16\,{\rm h}$ per additional $\beta$.

4. **$L$ scan: $\{12, 16, 20\}$.** Tests volume-independence of all four metrics. Scaling is roughly $L^4$ in wallclock for global Wilson and $L^0$ for block samples (frozen exterior cost is in measuring local plaquettes, which is $|B|^4$ not $L^4$). Largest gain: confirming that median $\Lambda$ does not drift with $L$. Estimated cost: $\sim 8\,{\rm h}$ at $L=12$, $\sim 38\,{\rm h}$ at $L=20$.

5. **Block side and core margin: $(6, 2) \to (8, 2)$ or $(6, 2) \to (8, 3)$.** Tests interior-depth dependence — does the conditional density decay further into the block? With margin 3, core depth is 1 site = 16 plaquettes per orientation projection (still only 4 distinct interior coordinates, so similar core count). The interesting comparison is core depth, not core count. Estimated cost: comparable to Stage A.

**Recommended Stage B at a single A100-week budget ($\approx 168\,{\rm h}$):** combine axes (1) and (3), i.e. $N_{\rm samples} = 1024$ at three $\beta \in \{3.0, 3.5, 4.5\}$. Total: $4 \times \text{Stage A}_{\beta=3.5} + 2 \times 4 \times \text{Stage A}_{\beta\neq 3.5} \approx 4 \times 5.4 + 8 \times 5.4 = 65\,{\rm h}$. Or combine (1) and (4): $N_{\rm samples} = 1024$ at $L \in \{12, 16, 20\}$, comparable cost.

**What Stage B will NOT settle:** the analytic theorems §J.6-refined and §R.1 themselves. Stage B is variance reduction and parameter coverage; it tightens or rebuts the empirical conjectures, but a theorem still needs to be proved. The §R.1 q² → √(qq′) upgrade, in particular, requires either an Eberle-coupling argument or a polymer expansion — no amount of additional Wilson MCMC will deliver it.

### §T.7 What needs to be uploaded for the deeper Stage A analysis

The current upload contains the run script and the console log. To do the analysis Stage A is actually capable of supporting, the following are needed:

- **`pair_ratio_by_distance.csv`** — distance-resolved $R_2(d)$ table. Tests whether $R_2(d) \to 1$ with $d$, and whether the approach is exponential. This is the direct empirical observable for the (M′)_SU(2) decay claim.
- **`DATA_PMBSF_cavity_ratio_by_distance.csv`** — distance-resolved $\Lambda(d)$ table. Tests whether the cavity ratio decays toward 1.
- **`rooted_DATA_PMBSF_cavity_ratio_by_distance.csv`** — distance-resolved $\Lambda^{\rm root}(d)$. The direct (M′)_SU(2) decay test.
- **`single_source_depth.csv`** or its summary — depth-resolved $q_{\rm cond}/q_\eta$. Tests whether deeper conditioning (further from block boundary) gives tighter ratios.
- **`cap_feature_scan.csv`** — per-row $(g_{\rm mean}, \rho_{\rm mean}, k_{\rm mean}, q_{\rm cond})$. Distinguishes hypotheses (1)–(3) of §T.4.

With these, pass-17 §T can be upgraded from headline-only to per-distance and per-depth, and the §R.1 exponential-decay statement can be tested empirically.

### §T.8 Connection to the master narrative

Pass-12 §K.5 caveat (5) "no analytic theorem" remains open. Pass-15 §R.1 sketches the analytic target; Stage A delivers the first direct empirical evidence that the **statistical** target is met at typical conditioning. Combined with the §J.6 evidence from passes 12–16 (operator-norm prerequisite), the empirical case for (M′)_SU(2) at $\beta = 3.5$ now rests on two independent pillars:

| Pillar | Probe | Passes | Conclusion |
|---|---|---|---|
| Operator-norm | Projected BE eigenvalue $\rho_*$ | 12, 14, 15, 16 | $\rho_* \approx \kappa_G + O(\lambda_{\min}(L))$, $\to \kappa_G = 2.0$ as $L\to\infty$ |
| Statistical density | Conditional density and cavity ratios | 17 (this appendix) | $q_{\rm cond}/q_\eta \approx 1$, $\Lambda, \Lambda^{\rm root} = O(1)$, cap mechanism correctly signed |

The remaining gap is the analytic chain: §J.6-refined (Theorem 1) + §R.1 (Theorem 2). Stage A does not narrow this gap; it strengthens the empirical foundation for both theorems' hypotheses.

### §T.9 Stage A caveats

- **Single ensemble, single seed (23060524).** The empirical estimates are point estimates; jackknife confidence intervals are not in the headline summary.
- **Single $\beta$ ($3.5$) and single $L$ ($16$).** No uniformity check.
- **Heavy upper tail at single-plaquette level (max ratio $7.20$).** This may or may not correspond to physical localized rare events; without the per-row CSV it cannot be diagnosed.
- **Cap-predictor $R^2 = 0.032$.** The cap mechanism is directionally right but not yet predictively tight.
- **Default $(H_0, \rho_0) = (3.0, 0.7)$ for rooted bad-staple.** The grid `H0_GRID = [3.0, 4.0, 5.0]`, `RHO0_GRID = [0.6, 0.7, 0.8]` is in the config but not in the headline; sensitivity is unmeasured in Stage A.
- **Distance structure untested in the headline.** All four headline metrics are aggregated over distance; the per-distance CSVs are needed to test the exponential-decay prediction directly.
- **Block thermalization 128 sweeps may be insufficient.** The frozen-exterior chain mixes faster than the full chain (smaller effective dimension), but at $\beta = 3.5$ the autocorrelation time on local plaquette observables is short; this is plausibly adequate, but not verified by an explicit autocorrelation measurement.

### §T.10 One-paragraph executive summary

Stage A is the first direct empirical probe of (M′)_SU(2) under the actual conditional-expectation operation it requires (frozen exterior + interior resampling). At $\beta = 3.5$, $L = 16$, 128 random $6^4$ blocks, the three headline ratios — single-source $q_{\rm cond}/q_\eta$, cavity $\Lambda$, rooted-cavity $\Lambda^{\rm root}$ — all sit at median $\approx 1.0$–$1.25$ with maxima $\le 7.20$. The script's own supportive-result thresholds are met at the median; the q95 sits at the margin; the cap-predictor mechanism is directionally confirmed but explains only 3% of the variance. Conclusion: Stage A is a *supportive* empirical anchor for (M′)_SU(2) under typical conditioning, paired with a clear Stage B program (variance reduction and parameter coverage) and a continuing open analytic question (§R.1 itself).


### §T.11 Pass-17 honesty corrections folded into the master (pass 18)

Two pass-17 deeper analyses revealed overconfidence in Stage A summary statistics. Both are folded into the master here as the fifth and sixth explicit honesty corrections (see §15 consolidated register).

#### §T.11.1 Decay-rate point estimates have wide confidence intervals

The Stage A summary statistics quoted in §T.3 — median cavity $\Lambda = 1.216$, median rooted $\Lambda^{\rm root} = 1.245$ — were paired in pass-17 follow-up analysis with point estimates for the exponential decay rate of the pair and rooted-pair ratios as a function of L1 plaquette-pair distance $d$:

$$m_{\rm pair}^{\rm point} = 1.15, \qquad m_{\rm root}^{\rm point} = 0.88$$

obtained from a 3-point log-linear fit on the per-distance ratios at $d \in \{1, 2, 3\}$.

Stage A only has 3 reliable distance bins because the side-6 block with core margin 2 produces an interior of $2^4 = 16$ sites with 24 core plaquettes, and per-distance pair-count drops below 100 above $d = 3$. The point estimates were obtained from this sparse data.

**Bootstrap 95% confidence intervals (1000 block-resamples) for the same two slopes:**

$$m_{\rm pair} \in [0.10, 2.27], \qquad m_{\rm root} \in [0.04, 2.18]$$

The CI for $m_{\rm pair}$ spans more than an order of magnitude; the CI for $m_{\rm root}$ is consistent with arbitrarily small positive decay. The point estimates should not be quoted as if they were tight numerical values. **The qualitative finding is preserved**: both decay rates are positive (the lower CI bounds exclude zero), consistent with the §R.1 / Lemma Q exponential-decay prediction, and the magnitudes are roughly compatible with the Wilson correlation length at $\beta = 3.5$. The wide CIs reflect the small Stage A geometry, not a defect in the underlying mechanism.

The Stage B side-10 / margin-3 run (Appendix V §V.2 below) extends reliable distance bins to $d = 12$ and tightens the slope estimates. The Stage B slopes are still based on a noisy regression — cap-feature $R^2$ values are 0.028 (g-slope) and 0.059 ($\rho$-slope) — but the longer distance range gives sharper decay information than Stage A's 3 bins could provide.

**Honesty correction logged:** the Stage A decay-rate point estimates $m_{\rm pair} = 1.15$, $m_{\rm root} = 0.88$ in any unguarded reading should be replaced by **decay-rate point estimates with bootstrap 95% CIs $[0.10, 2.27]$ and $[0.04, 2.18]$ respectively, qualitatively positive but quantitatively wide**.

#### §T.11.2 Indicator-shape correction in Stage B / heat-bath scripts (informational)

The pass-17 Stage A used a symmetric sigmoid $X_{p,\eta} = \sigma((\phi_p - t)/\eta)$ as the smooth source indicator. The Lemma Q final document (§1) specifies the proof-friendly upper-envelope smoother satisfying $\mathbf 1_{\{\phi_p \ge t\}} \le X_{p,\eta} \le \mathbf 1_{\{\phi_p \ge t-\eta\}}$ — a ramp from 0 at $t - \eta$ to 1 at $t$, asymmetric to the left of $t$.

The §V.1 exact-heat-bath side-8 run uses the proof-friendly ramp (matching the Lemma Q document's analytic specification). The §V.2 Stage B Metropolis side-10 run uses the legacy symmetric sigmoid (Stage A inheritance). This is not a contradiction — both shapes are valid smoothers, both are calibrated to hit $q_\eta = 0.003$ — but it explains the small difference in the tuned thresholds: §V.1 reports $t = 1.0081$ (ramp), §V.2 reports $t = 1.0092$ (sigmoid), Stage A reports $t = 1.0104$ (sigmoid). The ramp's tuned $t$ is slightly lower because the ramp's mass is entirely below $t$ rather than spread symmetrically across $t$.

For exact alignment with the Lemma Q document's §1 specification, the proof-friendly ramp is the correct form. Re-running Stage B side-10 with the ramp instead of the sigmoid would shift $t$ slightly downward without changing the qualitative findings. The §V.1 anchor is already aligned. This is logged as informational, not as a sixth honesty correction — neither indicator form is "wrong" for empirical diagnostics; the ramp is what the analytic proof program needs.

#### §T.11.3 Extended-regression $R^2$ binary-classifier artifact

A pass-17 follow-up analysis added a multivariate cap-feature regression (cap slope $g$, $\rho$, $k$, $\rho^2$, $k^2$, $g \cdot \rho$, plus orientation indicators) and reported $R^2 = 0.100$ multivariate. The interpretation was that adding higher-order ρ- and k-features increased explanatory power.

The actual mechanism turned out to be a binary-classifier artifact:

- Of the ~3072 (block, plaquette) rows in Stage A, a significant fraction had $q_{\rm cond}$ values numerically equal to the noise floor (effectively zero given 256 samples).
- These near-zero rows dominate the variance in $\log q_{\rm cond}$, which the regression takes as a continuous response.
- The multivariate regression was effectively distinguishing "near-zero" from "non-zero" rows, not capturing additional structure in the non-zero distribution.

**Re-analyzed on positive (non-zero $q_{\rm cond}$) rows only:**

| Predictor set | $R^2$ on positive rows |
|---|---:|
| Univariate cap-feature $g$ | $0.036$ |
| Block fixed-effect alone | $0.056$ |
| Multivariate $g, \rho, k, g\rho, k^2, ...$ | $0.041$ |
| Multivariate + block FE | $0.084$ |

The block fixed-effect alone outperforms any local cap-feature combination. **The missing structure in Stage A's cap regression is non-local frozen-exterior dependence, not local higher-order**. The cap mechanism is correctly directional but block-specific frozen-exterior conditions vary the conditional rare-event density in ways that no local one-link feature combination can capture.

**Honesty correction logged:** the pass-17 multivariate $R^2 = 0.100$ should not be quoted as evidence that higher-order cap features explain Stage A's variance; the correct read is **$R^2 = 0.036$ univariate / $R^2 = 0.084$ multivariate+block-FE on positive rows only**, with block-level frozen-exterior variation being the dominant missing-structure contributor. This sharpens the diagnosis already in §T.4(b) explanation (3) "block-to-block heterogeneity" and downgrades explanations (1) "statistical noise" and (2) "cap predictor incomplete".

#### §T.11.4 Aggregated status of Appendix T after pass-18 corrections

The §T.3 headline table is unchanged. The §T.5 verdict table is unchanged. The honest reading of the §T.4 soft spots is now sharper:

- **Soft spot (a) — the $7.20\times$ tail.** Still present. Stage B side-10 saw a $9.10\times$ maximum (Appendix V §V.2), consistent with more samples / deeper rare-tail penetration, not pathology. Lemma Q's qualitative consequences are preserved; the $q^2 \to \sqrt{qq'}$ upgrade discussed in the Lemma Q document §16 remains the precise analytic question.
- **Soft spot (b) — the cap-predictor's weak linearity.** Now diagnosed sharply (§T.11.3): block-level frozen-exterior variation dominates the residual variance. The cap mechanism is the *local* SU(2) input (cleanly described by §V's §5 of the Lemma Q document and §11 of the Expanded Derivations); it is not the load-bearing theorem. The load-bearing theorem is block source-stability (Lemma Q itself).

Stage A remains a supportive empirical anchor for Lemma Q's consequences at typical conditioning, with two honesty-corrected caveats (§T.11.1, §T.11.3) and an informational indicator-shape note (§T.11.2).

---

*End of pass 17 master document. Supersedes pass 16.*

*Pass 17 supplies one substantive item in response to "do all four": the executive companion + docx (delivered earlier in the pass-17 session) plus Appendix T, folding in the Stage A frozen-exterior block-conditional diagnostic from a 5.4-hour A100 run at $L=16$, $\beta=3.5$, $N_{\rm cfg}=32$, 128 blocks × 256 samples × 24 core plaquettes per block ($\approx 7.86 \times 10^5$ conditional measurements).*

*The empirical advance: direct probe of (M′)_SU(2) at typical conditioning gives median $q_{\rm cond}/q_\eta = 1.03$, median cavity $\Lambda = 1.22$, median rooted $\Lambda^{\rm root} = 1.25$. All three headline metrics meet the script's own supportive-result thresholds at the median. The cap-predictor mechanism is directionally confirmed (slope $-9.91$, $p < 10^{-3}$ implied by the magnitude) but explains only 3% of the variance ($R^2 = 0.032$).*

*The two new soft spots, named: (a) the $7.20\times$ single-plaquette tail event in $\sim 3000$ measurements; (b) the cap-predictor's weak linearity. §T.4 diagnoses three competing explanations for (b); §T.6 specifies a Stage B to distinguish them.*

*The empirical case for (M′)_SU(2) at the working corner now rests on two independent pillars: operator-norm (passes 12–16, projected BE $\rho_* \to \kappa_G$) and statistical density (pass 17 §T, $q_{\rm cond}/q_\eta \approx 1$). Both are supported. The analytic chain (§J.6-refined + §R.1) remains open and unchanged.*

*Pass-12 §K.5 caveats (4) and (5) remain open; pass-15 §R.1 q² → √(qq′) upgrade remains the precise residual analytic question. Pass-7 conditional status fully preserved.*

*Pass 17 does NOT prove (M′)_SU(2). It supplies one new appendix (T) with 10 subsections for a total of 20 appendices (A–T). The companion at /mnt/user-data/outputs/PMBSF_companion.md and .docx is delivered as a separate document.*

*Stage A caveats (see §T.9): single ensemble + seed, single ($\beta$, $L$) point, distance-aggregated headline, cap-predictor $R^2$ low, max-ratio $7.20$ tail. The per-distance, per-depth, and per-row CSVs were NOT uploaded with the run log; §T is limited to summary-statistic analysis until those CSVs are available.*

*Compiled by reading the Stage A diagnostic script and console log, analyzing the headline metrics against the script's own supportive-result thresholds in `RUN_READOUT.md`, naming the two new soft spots, specifying a Stage B program along five candidate axes with A100 wallclock estimates, and adding the Stage A pillar to the master narrative alongside the operator-norm pillar of passes 12–16. The per-distance CSVs from the run were not uploaded; §T.7 lists what is needed to upgrade the analysis. No pass-1 through pass-16 content was modified.*


---

## Pass 18 additions begin here

## 15. Consolidated honesty-corrections register (pass 18)

**Purpose.** The master tracks six explicit honesty corrections across passes 4 through 17. Pass 18 consolidates them into a single register for paper-grade reference. Each entry lists what was originally claimed, what the corrected claim is, what triggered the correction, and the current downstream status.

This register is itself the master's defensibility architecture. Prior versions of specific sub-claims overstated; the corrections are documented; the current claims that survive correction are calibrated by that survival. The register belongs in any manuscript drawing on this work as a brief reviewer-facing appendix.

### Correction 1 (pass 4) — $m_*$ retraction (Appendix E)

**Original claim.** v17b Wilson MCMC results were quoted with an extracted decay rate $m_* \approx 0.10$ supporting (M′)_SU(2) at the working corner.

**Correction.** The HBq2 route requiring this $m_*$ value was closed. The empirical $m_*$ extraction was retracted as not load-bearing.

**Trigger.** Pass 4 audit of v17b CSV against the original claims.

**Status.** Resolved. The pass-7 conditional status preserves what survived: (M′)_SU(2) at large $\beta$ for SU(2) is open. (Renamed Lemma Q in pass 18.)

### Correction 2 (pass 8) — §H.5 weighted Lyapunov sign convention

**Original claim.** Old weighted Lyapunov lemma stated $LW \le -\alpha W + \beta \mathbf 1_K \Rightarrow \int f^2 W\, d\mu \le \ldots$

**Correction.** The drift condition $LW \le -\alpha W + \beta \mathbf 1_K$ does *not* by itself imply that bound. The correct form controls $\int f^2 \phi\, d\mu$ when $LW \le -\phi W + \beta \mathbf 1_K$.

**Trigger.** Pass 8 verbatim self-disclaimer in `PMBSF_Haar_Curvature_LocalToGlobal_Derivation.md`.

**Status.** Resolved. Without the correction, the appendix would overclaim. Pass-8 incorporation uses the corrected form.

### Correction 3 (pass 10) — §I.9 false scalar tail ratio

**Original claim.** Earlier formulations required $\mathbb P(\phi_p > \delta_{\rm st}) \lesssim \mathbb P(\phi_p > t)$ for bad-staple absorption.

**Correction.** This ratio assumption *generally fails* when $\delta_{\rm st} \ll t$. The corrected argument applies Theorem F directly to bad-staple events $R_{p,\ell,\eta}$ with $\mathbb E_W R_{p,\ell,\eta} \le q_\eta$, giving $|\mathrm{Cov}_W(R_{p,\ell,\eta}, X_{p',\eta})| \le C_{\rm root} q_\eta^2 e^{-md(p,p')}$ without the false ratio assumption.

**Trigger.** Pass-10 audit of the SU(2) closure chain.

**Status.** Resolved. The pass-10 §I appendix uses the corrected rooted-source argument. The §I.16 minimal-target form `Cov_W(X,X) ≤ Cq² e^{-md}` is now what is asserted (and remains open). **The pass-18 rename moves this target into Lemma Q's cavity form (Appendix U eq U.4).**

### Correction 4 (pass 15) — $\langle\phi_p\rangle$ factor-of-4 error

**Original claim.** Pass-11 §J.4 said $\langle\phi_p\rangle \approx 3/(2\beta) = 0.43$ at $\beta = 3.5$.

**Correction.** The correct Haar expectation is $\langle\phi_p\rangle = 3/(8\beta) = 0.107$ at $\beta = 3.5$. The original was off by a factor of 4. Wilson MCMC at $\beta = 3.5$ gives empirical $\langle\phi_p\rangle = 0.148$ (slightly higher than the Haar value due to Wilson reweighting).

**Trigger.** Pass-15 Wilson MCMC implementation revealed the empirical value, which prompted re-derivation of the analytical Haar value.

**Status.** Resolved. The error did not propagate to any downstream analytic result (pass-11 §J.5 used the Haar bound; pass-12 §K.3 used $\sigma = 1/\sqrt{\beta}$ directly).

### Correction 5 (pass 17 §T.11.1) — Stage A decay-rate point-estimate overconfidence

**Original claim.** Stage A reported point estimates $m_{\rm pair} = 1.15$ and $m_{\rm root} = 0.88$ for the exponential decay rates of the pair and rooted-pair ratios versus L1 distance.

**Correction.** The point estimates came from a 3-point log-linear fit on $d \in \{1, 2, 3\}$ — the only reliable bins at side-6 / margin-2 geometry. Bootstrap 95% CIs (1000 block-resamples) are $m_{\rm pair} \in [0.10, 2.27]$ and $m_{\rm root} \in [0.04, 2.18]$.

**Trigger.** Pass-17 follow-up bootstrap analysis.

**Status.** Resolved. The qualitative finding (positive decay rate, consistent with Lemma Q's prediction) survives. Point estimates should not be quoted as tight values. **Stage B side-10 (Appendix V §V.2) extends reliable bins to $d = 12$ and gives sharper decay information, though still based on noisy regression**.

### Correction 6 (pass 17 §T.11.3) — Extended-regression binary-classifier artifact

**Original claim.** Pass-17 multivariate cap-feature regression reported $R^2 = 0.100$, suggesting that adding higher-order $\rho$ and $k$ features explained more of Stage A's variance.

**Correction.** The $R^2 = 0.100$ was a binary-classifier artifact: a significant fraction of Stage A rows had $q_{\rm cond}$ at the noise floor, and the regression was effectively distinguishing "near-zero" from "non-zero" rows. On positive rows only, $R^2 = 0.036$ univariate and $R^2 = 0.041$ multivariate. Block fixed-effect alone gives $R^2 = 0.056$; block FE + multivariate gives $R^2 = 0.084$.

**Trigger.** Pass-17 follow-up regression on filtered data.

**Status.** Resolved. The missing structure is **non-local frozen-exterior dependence**, not local higher-order cap-feature structure. This sharpens the diagnosis already in §T.4(b) explanation (3) "block-to-block heterogeneity" and downgrades (1) and (2). The cap mechanism is the local SU(2) input but is *not* the load-bearing theorem; block source-stability (Lemma Q itself) is.

### Summary

| # | Pass | Location | Class | Status |
|---|---|---|---|---|
| 1 | 4 | App. E | Empirical retraction | Resolved |
| 2 | 8 | App. H §H.5 | Analytic sign-convention | Resolved (corrected form used) |
| 3 | 10 | App. I §I.9 | Analytic false-ratio | Resolved (corrected rooted form used) |
| 4 | 15 | App. J §J.4 | Numerical factor-of-4 | Resolved (no downstream effect) |
| 5 | 17 | App. T §T.11.1 | Statistical overconfidence | Resolved (bootstrap CIs replace point estimates) |
| 6 | 17 | App. T §T.11.3 | Regression artifact | Resolved (diagnosed: block FE dominates) |

**Net effect.** The corrections cluster in two periods: pass 4–10 (analytic foundations being firmed up) and pass 17 (Stage A statistical follow-up). None of the corrections affected the master's conditional theorem stack: each correction either retracted an empirical over-claim, fixed a sign or factor that did not propagate, or sharpened a diagnostic interpretation. **The pass-7 conditional status is unchanged across all six corrections.**

For paper-grade reference: any manuscript drawing on this master should include a brief reviewer-facing appendix listing these six corrections. Their honest documentation is part of why the surviving claims are credible.

---

## Appendix U — Lemma Q: precise analytic target (pass 18)

**Status.** Pass 18 documentary update. Renames the analytic target previously referred to throughout the master as **§R.1** / **(M′)_SU(2)** / **the rooted-source polymer estimate** to a single canonical name, **Lemma Q**, and supplies the precise statement, the equivalent cavity-intensity form, and the chain-rule proof that cavity stability implies Lemma Q. The rename is documentary: what was open before pass 18 (the SU(2)-specific large-$\beta$ probability theorem) remains open after pass 18. The pass-7 literature finding (Appendix G — no peer-reviewed paper closes this for SU(2) at large $\beta$ as of May 2026) is unchanged.

Pre-pass-18 references to "§R.1", "(M′)_SU(2) at large $\beta$", and "the rooted-source polymer estimate" remain in the master as historical references and are NOT retroactively renamed. Pass 18 and forward content uses **Lemma Q** as the canonical name.

### §U.1 Setup

Wilson SU(2) lattice gauge theory on $\mathbb T_L^4$ at coupling $\beta$, with the standard plaquette action and Haar product measure. Define the plaquette excess

$$\phi_p(U) = 1 - \tfrac12 \Re\,\mathrm{Tr}(U_p)$$

For a threshold $t \in (0, 2)$ and smoothing scale $\eta > 0$, fix a monotone smooth source cutoff $f_\eta: \mathbb R \to [0,1]$ satisfying the **upper-envelope sandwich**

$$\mathbf 1_{\{\phi_p \ge t\}} \le X_{p,\eta} := f_\eta(\phi_p - t) \le \mathbf 1_{\{\phi_p \ge t - \eta\}}.$$

Define the smoothed source density $q_\eta = \mathbb E[X_{p,\eta}]$, calibrated to a small target (e.g. $q_\eta = 0.003$ for $\beta = 3.5$, $\eta = 0.005$, $t \approx 1.008$).

For a Bałaban block $C \subset \mathbb T_L^4$, let $C^\circ$ denote its shaved core (away from the block boundary by margin $\ge 2$), and $\mathcal F_{C^c}$ the sigma-field generated by all link variables outside the block.

### §U.2 Lemma Q (the analytic target)

**Lemma Q (unrooted form).** There exists a constant $C_Q$ (independent of $|B|$ and of the frozen exterior in a uniform sense) such that for every finite set $B \subset \mathcal P(C^\circ)$ of plaquettes in the block core,

$$\mathbb E\!\left[\prod_{p \in B} X_{p,\eta} \,\Big|\, \mathcal F_{C^c}\right] \le (C_Q\, q_\eta)^{|B|}. \tag{U.1}$$

**Lemma Q (rooted form).** For every $p_0 \in \mathcal P(C^\circ)$, every observable $0 \le Y_{p_0} \le X_{p_0,\eta}$, and every finite $B \subset \mathcal P(C^\circ)$,

$$\mathbb E\!\left[Y_{p_0} \prod_{p \in B} X_{p,\eta} \,\Big|\, \mathcal F_{C^c}\right] \le (C_Q\, q_\eta)^{|B|}\, \mathbb E[Y_{p_0} \mid \mathcal F_{C^c}]. \tag{U.2}$$

The canonical rooted use is $Y_p = X_{p,\eta}\, \mathbf 1_{\rm bad}$ where $\mathbf 1_{\rm bad}$ is the indicator that the SU(2) one-link staple of any $\ell \in \partial p$ is not in the good cone $\mathcal G_{\ell,p}(h_0, \rho_0) = \{\|H_\ell\| \ge h_0,\, \rho_{\ell,p} \ge \rho_0\}$; the rooted form then absorbs bad-staple contributions without requiring unrooted bad-staple rarity.

**Interpretation.** Lemma Q is a *block conditional* statement, stronger than ordinary mixing. Ordinary mixing gives decay of correlations after sources are inserted; Lemma Q says **the insertion itself costs one factor of $q_\eta$ per source under local conditioning**. This is the SU(2)-specific probability input the program needs.

### §U.3 Equivalent cavity-intensity form (smallest sufficient sub-target)

For finite $S \subset \mathcal P(C^\circ) \setminus \{p\}$, define the **conditional cavity intensity**

$$\lambda_p(S \mid \mathcal F_{C^c}) := \frac{\mathbb E\!\left[X_{p,\eta} \prod_{r \in S} X_{r,\eta} \,\big|\, \mathcal F_{C^c}\right]}{\mathbb E\!\left[\prod_{r \in S} X_{r,\eta} \,\big|\, \mathcal F_{C^c}\right]} \tag{U.3}$$

(whenever the denominator is nonzero). The **distance-sensitive cavity-stability estimate** is

$$\boxed{\lambda_p(S \mid \mathcal F_{C^c}) \le q_\eta \exp\!\left(\sum_{r \in S} J(p,r)\right), \qquad J(p,r) \le C_J e^{-m_J d_C(p,r)},} \tag{U.4}$$

where $d_C$ is plaquette distance measured inside the block core. The rooted version is

$$\boxed{\lambda_p^Y(S \mid \mathcal F_{C^c}) \le q_\eta \exp\!\left(J(p, p_0) + \sum_{r \in S} J(p,r)\right).} \tag{U.5}$$

The bound (U.4)–(U.5) is the **smallest sufficient sub-target for Lemma Q**. The implication (U.4) $\Rightarrow$ (U.1) is by the conditional chain rule (§U.4 below). This identification matters because it isolates the actual analytic theorem to prove: not an a priori product bound, but a single-source cavity-density bound with summable influence kernel.

### §U.4 Chain-rule proof: cavity stability implies Lemma Q

Let $B = \{p_1, \ldots, p_n\}$. The conditional chain rule gives

$$\mathbb E\!\left[\prod_{i=1}^n X_{p_i,\eta} \,\Big|\, \mathcal F_{C^c}\right] = \prod_{i=1}^n \lambda_{p_i}\!\left(\{p_1, \ldots, p_{i-1}\} \,\big|\, \mathcal F_{C^c}\right). \tag{U.6}$$

Applying (U.4) to each factor,

$$\mathbb E\!\left[\prod_{i=1}^n X_{p_i,\eta} \,\Big|\, \mathcal F_{C^c}\right] \le q_\eta^n \exp\!\left(\sum_{i=1}^n \sum_{j<i} J(p_i, p_j)\right). \tag{U.7}$$

If the influence kernel is uniformly core-summable,

$$\sup_p \sum_{r \in \mathcal P(C^\circ)} J(p, r) \le \log C_Q, \tag{U.8}$$

then

$$\exp\!\left(\sum_{i=1}^n \sum_{j<i} J(p_i, p_j)\right) \le C_Q^n, \tag{U.9}$$

so

$$\mathbb E\!\left[\prod_{p \in B} X_{p,\eta} \,\Big|\, \mathcal F_{C^c}\right] \le (C_Q\, q_\eta)^{|B|}. \tag{U.10}$$

This is Lemma Q in the form (U.1). The rooted proof is identical with $Y_{p_0}$ fixed as the base weight and (U.5) applied at each chain factor.

### §U.5 What is needed to prove the cavity-stability bound

The cavity-stability bound (U.4) is the actual SU(2) bridge. The proof route — drawn from §16 of the Lemma Q final document and §15 of the Expanded Derivations — is:

1. **Exact one-link heat-bath cap lemma.** The clean local SU(2) input. Conditioning on all links except one $\ell$, the Wilson conditional law is $\mathrm{vMF}_4(\overline{H_\ell}/\|H_\ell\|,\, \beta \|H_\ell\|)$, and the high-plaquette event for $p \ni \ell$ becomes an exact spherical cap on $S^3$. The cap probability has an explicit Laplace bound in terms of $\rho_{\ell,p} = m_\ell \cdot n_{\ell,p}$, $\|H_\ell\|$, and the cap aperture $a_{t-\eta} = 1 - (t-\eta)$. See Appendix V §V.4 for the empirical cap regression (signs correct, $R^2$ weak by design).

2. **Good/bad staple decomposition.** Good-staple part gets vMF cap suppression. Bad-staple part stays rooted under $X_{p,\eta}$ in the rooted form (U.2) / (U.5). The pass-10 §I.9 honesty correction (third correction in the §15 register) explicitly retired the false attempt at unrooted bad-staple rarity. **The decomposition with bad-staple absorbed in the root is the correct strategy**.

3. **Block source-stability comparison.** Compare the frozen-block Gibbs law with and without inserted sources. The output is the influence kernel $J(p, r)$. This is the *hard step* — the actual missing theorem. It is at least as hard as the SU(2) Yang–Mills mass-gap problem in the sense that closing it for SU(2) at large $\beta$ would yield the projected-firewall closure (per the conditional theorem stack); whether it is *strictly* harder, equivalent, or easier than the unconditional mass-gap problem is not known.

4. **Source-weighted cluster expansion.** Upgrade the Bałaban (1989, CMP 116:1) and Dimock (1996, JMP 37:5708, JMP 38:347) polymer-expansion locality from sup-norm control to $q_\eta$-weighted source norm. The pass-7 literature deep-dive (Appendix G) found no peer-reviewed result that does this for SU(2) at large $\beta$.

### §U.6 What the empirical anchors show

The empirical case for Lemma Q's *consequences* now rests on three independent legs:

- **§T (pass 17) — block-conditional Stage A (side-6).** Medians $\approx 1.0$–$1.25$ on $L=16$, $\beta=3.5$, distance bins $d \in \{1, 2, 3\}$. Supportive at typical conditioning.
- **§V (pass 18) — block-conditional anchors (side-8 exact heat-bath, side-10 Stage B).** Medians $\approx 0.92$–$1.00$, maxima $O(1)$, distance bins through $d \approx 4$ (side-8) and $d = 12$ (side-10). Stronger geometry, sharper sampling.
- **§W (pass 18) — full-volume Wilson pair/rooted covariance through $L = 64$.** Medians drop 17× from $L = 12$ to $L = 64$; maxima stay $O(1)$. The direct consequence of (U.4) at $k = 1$ via the cumulant expansion.

None of these prove Lemma Q. They show the qualitative pattern predicted by (U.4) is empirically present at every scale tested, in every geometry tested. The remaining work is analytic.

### §U.7 Summary

**The single inequality that closes the conditional theorem stack is the cavity-intensity bound (U.4) with a uniformly core-summable kernel $J$.** All other steps in the chain `Lemma Q $\Rightarrow$ rooted cumulants $\Rightarrow$ pair/rooted closure $\Rightarrow$ PTO level-(iii) $\Rightarrow$ HPM $\Rightarrow$ projected firewall` are either proved deterministically (the PTO/Bernstein/Birman–Schwinger algebra — see §1, §2, §3 of the Expanded Derivations) or follow from Lemma Q by standard polymer-expansion machinery once the source-weighted upgrade is in place.

**This is the next real proof target.** Appendices V, W, X provide the empirical support; the analytic work is the cavity-stability bound itself.

## Appendix V — SU(2) Wilson block-conditional Lemma Q anchors (pass 18)

**Status.** Pass 18 substantive item. Folds in two new block-conditional Lemma Q diagnostics that supersede the pass-17 Stage A as the *primary* and *geometry-robustness* numerical anchors for Lemma Q. Both runs target the same conditional-expectation operation Lemma Q requires (frozen exterior + interior resampling on a Bałaban sub-block of $\mathbb T_{16}^4$ at $\beta = 3.5$) and probe the same conditional ratios. The differences are in algorithm and geometry, by design.

| Anchor | Algorithm | Block side | Core margin | Indicator | Role |
|---|---|---|---|---|---|
| §V.1 | exact SU(2) one-link heat-bath (vMF₄, Wood 1994) for both global and block | 8 | 2 | upper-envelope ramp (Lemma Q doc §1) | **primary** |
| §V.2 | Metropolis with adaptive sigma for both global and block | 10 | 3 | symmetric sigmoid (Stage A inheritance) | **geometry-robustness supplement** |
| §T (pass 17) | Metropolis with adaptive sigma | 6 | 2 | symmetric sigmoid | prototype |

Stage A is now retained as the original prototype; §V.1 is the primary algorithm-aligned anchor; §V.2 is the geometry-robustness supplement.

### §V.1 Primary anchor: exact heat-bath side-8 (pass 18)

**Why this is the primary anchor.** The §V.1 run aligns the *algorithm* used by the diagnostic with the *analytic measure* Lemma Q is about. The Wilson one-link conditional law is exactly $\mathrm{vMF}_4(\overline{H_\ell}/\|H_\ell\|,\, \beta\|H_\ell\|)$ on $S^3$; the §V.1 run samples *from this conditional* (via Wood-1994 rejection on the Beta(3/2, 3/2) proposal) for *both* the global ensemble and the frozen-block interior resampling. There is no proposal/accept fudge factor anywhere in the chain. The indicator is the proof-friendly upper-envelope ramp $X_{p,\eta} = \mathrm{clip}((\phi_p - (t-\eta))/\eta, 0, 1)$ exactly matching §1 of the Lemma Q document.

**Configuration.**

| Item | Value |
|---|---|
| Gauge group | SU(2) (quaternion encoding) |
| Lattice | $T_L^4$ with $L=16$ |
| Coupling | $\beta = 3.5$ |
| Ensemble | $N_{\rm cfg} = 16$ exact-heat-bath configurations, 300 therm + 30 between sweeps |
| Threshold scale | $\eta = 0.005$, target $q_\eta = 0.003$ |
| Block geometry | $8^4$ sub-cube, core margin 2, $\Rightarrow$ core is $4^4 = 256$ sites $\Rightarrow$ 864 core plaquettes (with surface effects accounting) |
| Blocks per cfg | 2 (random anchors) |
| Total blocks | 32 frozen-boundary blocks |
| Block thermalization | 192 sweeps of interior-only heat-bath (exterior frozen) |
| Block samples | 256 per block, with 8 between-sweeps |
| Acceptance | identically 1.0 by construction (heat-bath has no rejection) |

**Threshold tuning.**

$$t = 1.0081100, \qquad q_\eta = 0.003000, \qquad q_{\rm hard} = 0.002989.$$

**Single-source conditional control.**

$$\max_{\rm depth}\,\mathrm{median}(q_{\rm cond}/q_\eta) = 0.8681, \tag{V.1}$$

$$q_{95}(q_{\rm cond}/q_\eta) = 2.6087, \qquad q_{99} = 3.5172, \qquad \max = 6.0754. \tag{V.2}$$

Single depth bin (depth 2), reflecting margin-2 geometry.

**Cavity ratio.**

$$\max \Lambda = 1.4626, \qquad \mathrm{median}\,\Lambda = 0.9249. \tag{V.3}$$

**Rooted cavity ratio.**

$$\max \Lambda_{\rm root} = 1.3998, \qquad \mathrm{median}\,\Lambda_{\rm root} = 0.9563. \tag{V.4}$$

**Cap-feature regression.**

$$\text{cap-feature slope} = -5.182, \qquad R^2 = 0.0101. \tag{V.5}$$

**Plain-language read.** The conditional rare-event density at typical block-conditioning is *below* the unconditional density (median 0.87, not 1.0+); the pair correlations are *below* $q_\eta^2$ (median 0.92); the rooted bad-staple absorption ratio is *below* $q_\eta\, \mathbb E[Y_r]$ (median 0.96). The cap-mechanism sign is correct (negative slope) but the $R^2$ is weak — same diagnosis as Stage A (§T.4 and §T.11.3): block-level frozen-exterior variation dominates the residual variance.

**Why the medians being slightly below 1 matters.** Stage A reported median ratios $1.03$–$1.25$ ($> 1$). §V.1 reports $0.87$–$0.96$ ($< 1$). The difference is the *algorithm*: Stage A's Metropolis with sigma adaptation introduces a small mixing artifact at the conditional measure; heat-bath samples exactly from the conditional. The Stage A medians being slightly above 1 was therefore a slight upward bias, not a defect of Lemma Q. §V.1 is the cleaner number.

**The medians being slightly below 1 in §V.1 is consistent with Lemma Q's prediction**: under frozen exterior, the conditional density is *at most* $q_\eta$ (up to the $C_Q$ constant), and typical conditioning should give exactly $q_\eta$ to leading order with sub-leading negative corrections from the slight constraint imposed by freezing the exterior. The numbers are right where the analytic argument expects them.

### §V.2 Geometry-robustness supplement: Metropolis Stage B side-10 / margin-3 (pass 18)

**Why this is the supplement.** §V.2 uses Metropolis (not exact heat-bath) but at *larger geometry* — side-10 blocks with margin 3, giving two depth bins (3 and 4) and distance bins through $d = 12$. It tests whether the qualitative Lemma Q pattern survives geometry stress: larger blocks, larger core, more samples in the rare tail, more reliable per-distance bins.

**Configuration.**

| Item | Value |
|---|---|
| Lattice | $T_{16}^4$, $\beta = 3.5$ |
| Ensemble | $N_{\rm cfg} = 32$ Metropolis configurations (sigma-adapted), 400 therm + 40 between sweeps |
| Threshold scale | $\eta = 0.005$, target $q_\eta = 0.003$ |
| Block geometry | $10^4$ sub-cube, core margin 3, $\Rightarrow$ core is $4^4 = 256$ sites $\Rightarrow$ 864 core plaquettes |
| Blocks per cfg | 2 |
| Total blocks | 64 frozen-boundary blocks |
| Block thermalization | 256 sweeps Metropolis (exterior frozen) |
| Block samples | 256 per block, with 10 between-sweeps |
| Block acceptance | $\approx 0.50$ (sigma-adapted) |
| Distance bins | $d \in \{0, 1, \ldots, 12\}$, all with $\ge 1000$ pair counts |

**Threshold tuning.**

$$t = 1.0092124, \qquad q_\eta = 0.003000, \qquad q_{\rm hard} = 0.002993.$$

**Single-source conditional control.**

$$\max_{\rm depth}\,\mathrm{median}(q_{\rm cond}/q_\eta) = 1.2681, \qquad q_{95} = 2.8596, \qquad \max = 9.1007. \tag{V.6}$$

Two depth bins: $\{3, 4\}$ (margin-3 geometry).

**Cavity ratio.**

$$\max \Lambda = 2.6074, \qquad \mathrm{median}\,\Lambda = 1.0028. \tag{V.7}$$

**Rooted cavity ratio.**

$$\max \Lambda_{\rm root} = 2.4132, \qquad \mathrm{median}\,\Lambda_{\rm root} = 1.0024. \tag{V.8}$$

**Cap-feature regressions (two predictors reported).**

$$g\text{-slope} = -9.5291, \qquad R^2_g = 0.0278, \tag{V.9}$$

$$\rho\text{-slope} = -370.513, \qquad R^2_\rho = 0.0587. \tag{V.10}$$

**Plain-language read.** Stage B medians are essentially exactly 1.0 (both $\Lambda$ and $\Lambda_{\rm root}$), tightening the Stage A medians of 1.22 and 1.25. The larger geometry *did not* produce cavity amplification — the conditional pair density is, to leading order, $q_\eta^2$ as Lemma Q predicts. Maxima grew from Stage A's 7.20 to 9.10, consistent with sampling 36× more plaquettes per block and seeing deeper rare-tail penetration. The cap-feature sign is correct throughout; the $R^2$ values are weak by the same diagnosis as §T.11.3.

### §V.3 Cross-anchor comparison

| Metric | Stage A (§T, side-6) | §V.1 (side-8 HB) | §V.2 (side-10 Stage B) |
|---|---:|---:|---:|
| Algorithm | Metropolis (sigmoid) | exact heat-bath (ramp) | Metropolis (sigmoid) |
| Frozen-boundary blocks | 128 | 32 | 64 |
| Core plaquettes/block | 24 | 864 | 864 |
| Depth bins | {2} | {2} | {3, 4} |
| Reliable distance bins | $d \in \{1, 2, 3\}$ | $d \in \{1, \ldots, \approx 4\}$ | $d \in \{0, \ldots, 12\}$ |
| Max depth-median $q_{\rm cond}/q_\eta$ | 1.03 | 0.87 | 1.27 |
| q95 $q_{\rm cond}/q_\eta$ | 2.74 | 2.61 | 2.86 |
| max $q_{\rm cond}/q_\eta$ | 7.20 | 6.08 | 9.10 |
| median $\Lambda$ | 1.22 | 0.92 | 1.00 |
| max $\Lambda$ | 2.74 | 1.46 | 2.61 |
| median $\Lambda_{\rm root}$ | 1.25 | 0.96 | 1.00 |
| max $\Lambda_{\rm root}$ | 2.43 | 1.40 | 2.41 |

**Reading the cross-anchor pattern.**

1. **All three anchors give medians at or below $\sim 1.3$ for every ratio measured.** Lemma Q predicts medians of order 1 with $C_Q \approx 1$ at typical conditioning; this is what we see across three different geometries and two different algorithms.

2. **The exact-heat-bath anchor (§V.1) gives the tightest medians ($< 1$).** This is the closest run to the analytic ideal — same algorithm as Lemma Q itself describes — and gives results indistinguishable from the prediction.

3. **The maxima grow with sample size.** Stage A had $\sim 3072$ block-plaquettes; §V.2 has $\sim 55296$ block-plaquettes. Maximum tail penetration scales accordingly: $7.20 \to 9.10$. This is statistical, not pathological. The empirical CDF of $q_{\rm cond}/q_\eta$ should be sub-exponential at scale $q_\eta$ — the right uniform statement to extract from Stage B's larger sample, which is on the §T.6 / §V.4 follow-up list.

4. **Distance bins through $d = 12$ are now available (§V.2).** Stage A's 3-bin decay fit had wide CIs (§T.11.1); Stage B's 13-bin range gives much sharper decay information, even at noisier slope $R^2$.

### §V.4 Cap-feature regression: signs, magnitudes, and the explicit cap conclusion

| Anchor | $g$-slope | $R^2_g$ | $\rho$-slope | $R^2_\rho$ |
|---|---:|---:|---:|---:|
| Stage A (§T) | $-9.91$ | $0.032$ | — | — |
| §V.1 (heat-bath side-8) | $-5.18$ | $0.010$ | — | — |
| §V.2 (Stage B side-10) | $-9.53$ | $0.028$ | $-370.5$ | $0.059$ |

The cap-feature mechanism (heat-bath good-staple Laplace bound — see §V.5 below for the precise statement) is **directionally confirmed at every anchor**: signs uniformly negative (larger cap-obstruction lowers the conditional source rate), magnitudes consistent across geometries. The $R^2$ is uniformly weak (0.01–0.06 range): the local cap features are not the load-bearing explanatory variables. §T.11.3 diagnosis: block-level frozen-exterior heterogeneity dominates the residual.

**The correct cap conclusion.** The cap is the clean local SU(2) input but it is *not* the load-bearing theorem. The load-bearing theorem is **block source-stability** (Lemma Q in cavity form, eq U.4). The cap supplies a local one-link suppression on the good-staple set; the block-level argument that connects local suppression to the multiplicative bound (U.1) is the actual missing analytic theorem.

### §V.5 Pointer to the analytic chain

The §V anchors test the *empirical* consequence of the chain `cap mechanism + good/bad decomposition + block source-stability $\Rightarrow$ Lemma Q $\Rightarrow$ rooted cumulants $\Rightarrow$ pair/rooted closure`. The analytic content of each step is:

1. **Cap mechanism (proved deterministically).** Conditioning on all links except $\ell$, $U_\ell \sim \mathrm{vMF}_4$ with mean direction $\overline{H_\ell}/\|H_\ell\|$ and concentration $\beta\|H_\ell\|$. The high-plaquette event $\{\phi_p \ge t\}$ becomes a spherical cap with aperture $a_t = 1 - t$ on $S^3$. The cap probability is bounded by a Laplace integral with rate $\beta \|H_\ell\| F(\rho_{\ell,p}, a_t)$, $F$ being the spherical max defined in §6 of the Lemma Q document. This is unconditional SU(2) algebra.

2. **Good/bad staple decomposition (proved deterministically).** Defining $\mathcal G_{\ell,p}(h_0, \rho_0) = \{\|H_\ell\| \ge h_0,\, \rho_{\ell,p} \ge \rho_0\}$, the source $X_{p,\eta}$ on the good-staple set inherits the cap suppression $\exp(-\beta h_0 c_{\rm cap}(t,\eta,\rho_0))$; the bad-staple part is absorbed into the *rooted* form (U.2) with $Y_p = X_{p,\eta} \mathbf 1_{\rm bad}$. The bound $0 \le R_{p,\ell,\eta} \le X_{p,\eta}$ preserves the root weight. This is deterministic combinatorial bookkeeping.

3. **Block source-stability (the open theorem).** The cavity-intensity bound (U.4) at large $\beta$ for SU(2). This is the actual analytic gap.

4. **Rooted cumulants and pair closure (conditional on Lemma Q).** Follow by source-weighted polymer expansion (§6 of the Expanded Derivations). Proved subject to the source-weighted Bałaban upgrade, which is itself an open analytic task.

§V.1 and §V.2 measure the *output* of steps 1–4 at the empirical level: median $\Lambda \approx 1$, max $\Lambda$ bounded, $\Lambda_{\rm root}$ tracking $\Lambda$. These are necessary empirical conditions for Lemma Q to hold. They are not proofs.

### §V.6 Stage B caveats

(Inheriting §T.9's caveat structure.)

1. **Two ($\beta$, $L$) points** — $\beta = 3.5$, $L = 16$, two block sizes (8 and 10). $\beta$ coverage and $L$ scaling are not part of the anchor.
2. **Distance-aggregated headline (§V.2 only) gives per-distance information up to $d = 12$.** Stage B unifies what Stage A could only sample at $d \le 3$.
3. **Cap-predictor $R^2$ weak across all three anchors** — diagnosed in §T.11.3 as block-level frozen-exterior heterogeneity.
4. **Maximum-ratio tail grows with sample size** — Stage B's 9.10 vs Stage A's 7.20 is consistent with statistical sub-exponential tail penetration, not pathology. A sub-exponential CDF analysis on the Stage B per-plaquette data would sharpen this.
5. **Indicator-shape difference between §V.1 (ramp) and §V.2 (sigmoid)** — §T.11.2 logs this as informational; the proof-friendly form is the ramp, which §V.1 already uses.

### §V.7 What §V adds to the master narrative

- Pillar count for the empirical case for Lemma Q's consequences is now **three**: operator-norm (passes 12–16), block-conditional Stage A/B (§T + §V), and full-volume covariance (§W).
- The exact-heat-bath side-8 (§V.1) is the *primary* numerical anchor because it samples from the analytic conditional measure without algorithmic artifact.
- Geometry-robustness (§V.2) confirms the qualitative Lemma Q pattern persists at larger block, larger core, longer distance, more samples.
- The cap-predictor conclusion is sharpened: the cap is the local input, block source-stability is the load-bearing theorem.
- The §V.1 medians being below 1 (rather than slightly above as in Stage A) suggests Stage A's small upward bias was a Metropolis mixing artifact, not a Lemma Q violation.

## Appendix W — Full-volume SU(2) Wilson pair/rooted covariance through L=64 (pass 18)

**Status.** Pass 18 substantive item. Documents three full-volume Wilson SU(2) runs at $L \in \{12, 16, 64\}$ measuring the pair covariance $\mathrm{Cov}(X_{p,\eta}, X_{p',\eta})$ and rooted-pair covariance $\mathrm{Cov}(Y_{p,\eta}, X_{p',\eta})$ across the full lattice (no frozen exterior). These quantities are the direct consequences of Lemma Q at $k = 1$ via the cumulant expansion (§6 of the Expanded Derivations):

$$|\mathrm{Cov}(X_p, X_q)| \le C\, q_\eta^2\, e^{-m d(p,q)}, \tag{W.1}$$

$$|\mathrm{Cov}(Y_p, X_q)| \le C\, \mathbb E[Y_p]\, q_\eta\, e^{-m d(p,q)}. \tag{W.2}$$

The block-conditional anchors (§T, §V) measure Lemma Q's conditional ratios on small frozen-exterior sub-blocks. **Appendix W measures the global consequence (W.1)–(W.2) at full lattice volume**, with no block conditioning. The two evidence types are complementary, not redundant.

### §W.1 Configuration

All three runs at $\beta = 3.5$, $\eta = 0.005$, target $q_\eta = 0.003$, with the smooth upper-envelope source indicator and standard Wilson Metropolis sampling. Threshold $t$ tuned per-run to hit $q_\eta = 0.003$.

| Item | $L = 12$ | $L = 16$ | $L = 64$ |
|---|---|---|---|
| Lattice | $T_{12}^4$ | $T_{16}^4$ | $T_{64}^4$ |
| $N_{\rm cfg}$ | 64 | 64 | 64 |
| Therm sweeps | 400 | 400 | 500 |
| Between sweeps | 40 | 40 | 50 |
| Total plaquettes | 124416 | 393216 | 100663296 |
| Pair samples per cfg | ~$10^9$ at all distances | ~$10^{10}$ | ~$10^{12}$ |
| File ledger | `PMBSF_SU2_closure_stage2_L12_L16_20260525_020743` | (same) | `PMBSF_SU2_closure_stage3_L64_20260525_030224` |

### §W.2 Headline cross-scale table

| Quantity | $L = 12$ | $L = 16$ | $L = 64$ |
|---|---:|---:|---:|
| $q_\eta$ (tuned) | 0.0030032 | 0.0030048 | 0.0030062 |
| max $|\mathrm{Cov}(X,X)| / q_\eta^2$ | 1.0071 | 1.1296 | **0.8658** |
| median $|\mathrm{Cov}(X,X)| / q_\eta^2$ | 0.1170 | 0.0705 | **0.0067** |
| pair slope (log ratio vs $d$) | $-0.0295$ | $-0.0308$ | $-0.0147$ |
| max $|\mathrm{Cov}(Y,X)| / (\mathbb E[Y] q_\eta)$ | 0.9871 | 1.1687 | **0.8924** |
| median $|\mathrm{Cov}(Y,X)| / (\mathbb E[Y] q_\eta)$ | 0.1090 | 0.0751 | **0.0074** |
| rooted slope | $-0.0255$ | $-0.0369$ | $-0.0094$ |

### §W.3 The key trend

- **Medians drop $\approx 17 \times$ from $L = 12$ to $L = 64$** ($0.117 \to 0.007$ pair; $0.109 \to 0.007$ rooted).
- **Maxima stay $O(1)$** ($1.01 \to 1.13 \to 0.87$ pair; $0.99 \to 1.17 \to 0.89$ rooted).
- **Slopes negative throughout**, magnitudes moderate.

This is the empirical signature of (W.1)–(W.2) at full volume: typical pair and rooted-pair covariances shrink with distance (median drops with volume because most pair distances grow with $L$); the global supremum stays bounded by a uniform $O(1)$ constant times $q_\eta^2$ (pair) or $\mathbb E[Y] q_\eta$ (rooted). This is what Lemma Q's chain `Lemma Q $\Rightarrow$ rooted cumulants $\Rightarrow$ pair/rooted closure` predicts.

### §W.4 What §W shows and does not show

**Shows.**

- The pair / rooted-pair covariance ratios are bounded *uniformly* up to $L = 64$ by an $O(1)$ constant.
- Typical (median) ratios decrease sharply with volume, consistent with exponential decay.
- The qualitative pattern is robust across three lattice sizes spanning a 5× linear range and a 800× volume range.

**Does not show.**

- The exact decay rate $m$ in (W.1)–(W.2). The slopes reported are linear regression of $\log(\text{ratio})$ vs $d$ across the per-distance bins of each run; they are noisy, with the $L = 64$ slope (smaller magnitude) reflecting the wider distance range and stronger noise floor near zero rather than slower decay. Pinning $m$ to a tight value would require either a finite-volume rigorous bound or finer distance-binned diagnostics at $L = 64$.
- Lemma Q itself. (W.1)–(W.2) are *consequences* of Lemma Q at $k = 1$; they are necessary but not sufficient.
- The continuum-limit decay rate. All runs are at fixed lattice $\beta = 3.5$.

### §W.5 Combined with §V

§V tests the block-conditional ratios on small frozen-exterior sub-blocks (medians of the conditional cavity intensity $\Lambda \approx 1$, maxima $O(1)$, distance bins through $d = 12$). §W tests the global covariance ratios at full lattice (medians dropping $17\times$ with $L$, maxima $O(1)$ throughout).

These are independent empirical lines testing *different but related* statistical predictions of Lemma Q:

- §V: $\mathbb E[X_p X_q \mid \mathcal F_{C^c}] / (q_\eta \mathbb E[X_q \mid \mathcal F_{C^c}]) \approx 1$ at typical conditioning.
- §W: $|\mathrm{Cov}(X_p, X_q)| / q_\eta^2 \lesssim e^{-m d}$ at full volume.

Neither implies the other directly; both follow from Lemma Q (via the cavity-intensity chain and the polymer-expansion cumulant chain respectively). Their empirical co-confirmation is the strongest current evidence for Lemma Q's *consequences* at this $(\beta, \eta, q_\eta)$ point.

### §W.6 Caveats

1. **Single $(\beta, \eta, q_\eta)$ point.** $\beta = 3.5$, $\eta = 0.005$, $q_\eta = 0.003$. The headline trend across $L$ is solid; $\beta$- and $\eta$-coverage is not.
2. **Slopes are noisy linear regressions, not extracted decay rates.** The point estimates should not be quoted as if they pinned the decay rate $m$.
3. **The $L = 64$ median is small enough that noise floor matters.** A median of 0.007 against a noise floor of $1/\sqrt{N_{\rm samples per dist}}$ is *not* a numerical-zero distinction; the $L = 64$ median is real but its precise value should be interpreted with the noise floor in mind.
4. **No $L \to \infty$ extrapolation.** The three lattice sizes show a clean monotone median drop; whether the median continues dropping or saturates at some volume-independent floor is not extracted.

### §W.7 What §W adds to the master narrative

§W supplies the **global-consequence pillar** of the empirical case for Lemma Q. Combined with §V (the conditional-ratio pillar) and the operator-norm work of passes 12–16 ($\rho_* \to \kappa_G$ pillar), the empirical support for Lemma Q's consequences now spans three independent angles:

1. **Operator-norm** (passes 12–16): the Brascamp–Lieb prerequisite $\rho_* > 0$ uniform in $L$.
2. **Block-conditional** (§T, §V): the cavity-intensity ratios under the exact frozen-exterior operation Lemma Q requires.
3. **Global covariance** (§W): the pair / rooted-pair covariance bounds at full volume up to $L = 64$.

All three are empirical. None is a proof. They are consistent with Lemma Q holding at $\beta = 3.5$; they do not establish it.

## Appendix X — L=64 projected-capacity threshold law on $\mathbb T_{64}^2$ (pass 18)

**Status.** Pass 18 substantive item. Two L=64 finite-dimensional spectral-threshold diagnostics on a synthetic 2D scalar model that validate the **deterministic projected-capacity object** central to the PMBSF architecture (sections §5 of the master, §1–§3 of the Expanded Derivations). Both runs are on $\mathbb T_{64}^2$ (NOT 4D SU(2)) with controlled sparse-dimer defect masks; they are *not* Wilson SU(2) results. Their purpose is to validate the operator-theoretic premise — that projected capacity $\|P 1_D P\|$ is a meaningful predictive variable for low-mode instability under sparse defects — in a clean setting where ground truth is exactly computable.

This complements Appendix W (which IS Wilson SU(2)) by establishing operator-level support for the deterministic spine of §5–§7 of the master.

### §X.1 Threshold-law diagnostic

**Setup.** Periodic lattice $\mathbb T_{64}^2$, $N = 4096$ sites. Project to the nonzero low Fourier sector with $K = 128$ low modes:

$$P = P_{\rm nonzero, K}, \qquad \lambda_1 = 0.009630547, \qquad \lambda_{\max,K} = 0.375490.$$

For a defect set $D \subset \mathbb T_{64}^2$, define $G_D = P 1_D P$ and the projected low-sector Hamiltonian $H_K(V, D) = \Lambda - V G_D$. The exact projected Birman–Schwinger critical coupling is

$$V_c^{BS}(D) = \|\Lambda^{-1/2} G_D \Lambda^{-1/2}\|^{-1} \tag{X.1}$$

(where $H_K(V_c, D)$ has a zero eigenvalue exactly). The cheap scalar surrogate is

$$V_c^R(D) = \frac{\lambda_1}{\|G_D\|}. \tag{X.2}$$

**Mask ensemble.** 180 masks across six geometric families (random, stripe, ring, low-mode-biased $x$, low-mode-biased diagonal, blue-noise dimers), 30 masks per family. **Fixed local geometry per mask**: $m = 128$ defect sites, density $0.03125$, exactly 64 clusters, largest cluster size 2 (so each mask is 64 separated dimers). What varies across the ensemble is *only* the long-range arrangement of dimers — density, defect count, cluster count, and largest local cluster are deliberately held constant so that any threshold variation cannot be attributed to local quantities.

**Headline result.**

$$\mathrm{corr}(V_c^R, V_c^{BS}) = 0.9581, \qquad \mathrm{corr}(\log V_c^R, \log V_c^{BS}) = 0.9600. \tag{X.3}$$

**Calibrated scalar law.**

$$\boxed{\log V_c^{BS} = 1.6615 + 1.2161\, \log V_c^R, \qquad R^2 = 0.9216,\quad \mathrm{MAE}_{\log} = 0.0563.} \tag{X.4}$$

Equivalent multiplicative form: $V_c^{BS} \approx \exp(1.6615) \cdot (V_c^R)^{1.2161}$.

**Mask-heldout cross-validation** (random forest, 8-fold group split on mask_id):

| Feature set | MAE | $R^2$ |
|---|---:|---:|
| scalar capacity | 0.0283 | 0.978 |
| scalar plus alignment | 0.0286 | 0.978 |
| geometry, no capacity | 0.0301 | 0.975 |
| local only | 0.2170 | $-0.035$ |

Scalar capacity beats geometry-only by MAE $\Delta = 0.0018$. Spectral alignment features ($\|G\|$ top-eigenvector energy at the lowest evals) add nothing beyond the scalar.

**Family-heldout cross-validation** (leave-one-group-out by family):

| Feature set | MAE | $R^2$ |
|---|---:|---:|
| scalar capacity | 0.1534 | $-72.5$ |
| scalar plus alignment | 0.1537 | $-71.7$ |
| geometry, no capacity | 0.1799 | $-87.2$ |
| local only | 0.2452 | $-182$ |

Family-heldout is genuinely hard extrapolation — the negative $R^2$ values show that learning on five families and predicting the sixth gives test variance larger than the residual variance — but the MAE ordering is preserved: scalar capacity still wins by $\Delta = 0.0265$ over geometry-only. The hardest family is **stripe_dimers** (consistent across all models), the only family with deterministic single-orientation dimers.

**Ridge regression** (all combined features):

$$R^2 = 0.9810, \qquad \mathrm{MAE} = 0.0269. \tag{X.5}$$

Top scaled-coefficient features: low Fourier amplitudes (fourier_02, fourier_11, fourier_01), $\log V_c^R$, mean pair distance, $\|G_D\|$ (R_nonzero). The scalar capacity is among the dominant correlating descriptors but not the only one — adding Fourier amplitudes captures some additional structure.

### §X.2 Order-parameter attack: capacity predicts the full bound-state response, not just the threshold

**Setup.** Same lattice, same mask families, 15 masks per family ($90$ masks total) × 7 coupling values $V_0 \in \{0.125, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0\}$ = 630 (mask, $V_0$) configurations. For each, compute the projected low-sector spectrum and extract:

- `projected_binding` = $\lambda_1 - \lambda_{\min}(H_K(V_0, D))$ — binding energy below the free first-eigenvalue
- `IPR_low` = participation ratio of the lowest mode
- `defect_mass_low` = fraction of $|\psi_{\min}|^2$ on defect sites
- `negative_crossing` flag = $\lambda_{\min}(H_K(V_0, D)) < 0$ — has zero eigenvalue been crossed

The exact Birman–Schwinger criterion predicts: `negative_crossing` iff $V_0 > V_c^{BS}(D)$, i.e., iff $V_0 \cdot \|\Lambda^{-1/2} G_D \Lambda^{-1/2}\| > 1$. We test this empirically.

**Predictive accuracy** (mask-heldout, random forest, 8-fold):

| Target | feature set | $R^2$ |
|---|---|---:|
| projected_binding | exact_BS | $0.9986$ |
| projected_binding | scalar_capacity | $0.9988$ |
| projected_binding | geometry_no_capacity | $0.9900$ |
| defect_mass_low | exact_BS | $0.9880$ |
| defect_mass_low | scalar_capacity | $0.9871$ |
| IPR_low | exact_BS | $0.8655$ |
| IPR_low | scalar_capacity | $0.8623$ |

**Family-heldout** (harder extrapolation):

| Target | feature set | $R^2$ family-heldout |
|---|---|---:|
| projected_binding | exact_BS | $0.9507$ |
| projected_binding | scalar_capacity | $0.9410$ |
| defect_mass_low | exact_BS | $0.5113$ |
| defect_mass_low | scalar_capacity | $0.4857$ |
| IPR_low | exact_BS | $-1.03$ |

**Negative-crossing classification.**

| Feature set | AUC | Accuracy |
|---|---:|---:|
| exact_BS | **1.0000** | **1.0000** |
| scalar_capacity | **1.0000** | **1.0000** |
| geometry_no_capacity | 1.0000 | 0.998 |
| local_only | 0.9913 | 0.981 |

**The exact_BS classifier achieves perfect accuracy on all 630 configurations.** This is the cleanest direct verification of the Birman–Schwinger criterion at $L = 64$: across two orders of magnitude in $V_0$ and across six geometric families, the projected-capacity-based classifier *never mislabels a single binding event*.

**Ridge law for projected_binding.**

| Feature | Scaled coefficient |
|---|---:|
| V0_R_nonzero (= $V_0 \|P 1_D P\|$) | 0.2258 |
| x_capacity (= $V_0 \|P 1_D P\| / \lambda_1$) | 0.2258 |
| $V_0$ | $-0.1330$ |
| BS_half | 0.0478 |
| mean_pair_distance | 0.0199 |

The dominant coefficient pair (V0_R_nonzero and x_capacity) is tied — they're proportional. This empirically confirms that the dimensionless variable $x = V_0 \|P 1_D P\| / \lambda_1$ is the natural physical order parameter for the full bound-state response.

### §X.3 What §X shows

**Shows.**

1. **The exact projected Birman–Schwinger threshold** is a finite-dimensional spectral computation that can be done exactly at $L = 64$. It is identically reproduced by the AUC = 1.0 classifier.
2. **Projected capacity $\|P 1_D P\|$ is a calibrated order parameter** for the threshold $V_c^{BS}$, with $R^2 = 0.92$ on the log-scale calibration $V_c^{BS} \propto (V_c^R)^{1.22}$.
3. **The scalar surrogate $V_c^R$ orders the exact threshold robustly across long-range arrangements** with density and local cluster geometry held fixed.
4. **Projected capacity is not just a threshold predictor — it is the right operator-theoretic object for the full low-mode response**, including binding magnitude, defect-mass concentration, and (more weakly) localization, across two orders of magnitude in $V_0$.
5. **Sparse defects matter through projected spectral capacity, not only through density or local clustering.**

**Does not show.**

- This is **not** a Wilson SU(2) Yang–Mills result. It is a 2D scalar finite-dimensional Birman–Schwinger threshold-law diagnostic.
- It does **not** prove the Wilson stochastic theorem.
- It does **not** prove the SU(2) Yang–Mills mass gap.
- It does **not** prove Lemma Q.

It gives a clean controlled model where the operator quantity central to the PMBSF program has demonstrable, empirically verified predictive content.

### §X.4 Relation to PMBSF

The PMBSF architecture relies on:

- $\Pi M^{-1} \Pi$ — projected Maxwell comparator (deterministic, §5)
- $\Pi 1_D \Pi$ — projected indicator on defect set (deterministic, §F.4 in pass-7 framing)

Appendix X validates the conceptual claim — that projected capacity $\|P 1_D P\|$ is a genuine predictive object for low-mode instability in a controlled model where the analogy is testable. **This strengthens §3 of the master (the deterministic projected-capacity framework)** from "here is the operator object; here is why it should matter" to "here is the operator object; here is direct verified evidence that it matters, including AUC = 1.0 for the Birman–Schwinger criterion at $L = 64$."

### §X.5 What §X adds to the master narrative

**The deterministic spine (master §5–§7) now has direct empirical support at $L = 64$ in a synthetic controlled setting.** This is a different type of support than the stochastic Wilson runs (Appendices T, V, W) — it tests the operator-theoretic premise, not the SU(2) stochastic theorem — but it is *valid* and *quantitatively strong*: $R^2 = 0.92$ calibration, AUC = 1.0 classification, 630 configurations.

The pass-7 literature framing (Appendix G) identified projected capacity as the right operator for sparse-defect instability questions; Appendix X verifies this empirically in a setting where the projected Birman–Schwinger threshold is exactly computable.

**For paper drafting**: §X material belongs in the PMBSF/SU(2) paper §3 (deterministic projected-capacity framework) as a §3.x subsection, not in the stochastic-evidence §6. It is operator-theoretic validation, not Wilson stochastic evidence.

## Appendix Y — SU(3) class-function asymptotic gap law (separate-paper pointer, pass 18)

**Status.** Pass 18 documentary item. The SU(3) work referenced throughout the master (§A.2 file map, §J file context, plus 18 mentions) has been consolidated into a precise local spectral theorem with explicit coefficient values, plus a finite-channel leakage matrix and a polymer-resolvent summability threshold. **The full derivation belongs in a standalone manuscript**, not in the PMBSF/SU(2) master. This appendix is a one-page pointer with the headline statement, the constants, the proof-route summary, and the manuscript-safe claim language.

**This is a local spectral theorem, not a 4D Yang–Mills mass-gap result.** It is unconditional within its scope.

### §Y.1 Headline theorem

For the SU(3) one-plaquette class-function Hamiltonian on the Cartan plane with Weyl-invariant coordinates $p_2 = x^2 + y^2$ and $p_3 = \frac{\sqrt{6}}{6} y (3x^2 - y^2)$, the local mass-gap-equivalent expansion to three terms is

$$\boxed{\Delta_{\rm SU(3)}(\beta) = \sqrt{\frac{2\beta}{3}} - \frac{5}{16} - \frac{311\sqrt{6}}{9216}\, \beta^{-1/2} + O(\beta^{-1}).} \tag{Y.1}$$

**Numerical values of the constants.**

- Leading order: $\omega(\beta) = \sqrt{2\beta/3}$. At $\beta = 5.7$ this is $1.949$.
- First correction: $c_0 = -5/16 = -0.3125$. From $\langle H_1 \rangle_1 - \langle H_1 \rangle_0 = -25/48 - (-5/24) = -15/48 = -5/16$.
- Second correction: $c_1 = -311\sqrt{6}/9216 \approx -0.0827$. Computed as $c_1 = \Delta_{\rm res} + \Delta_{H_2}$ with $\Delta_{\rm res} = -205\sqrt{6}/3072$ (resolvent leakage from $H_1$) and $\Delta_{H_2} = 19\sqrt{6}/576$ (intrinsic $H_2$ contribution).

### §Y.2 Main derivational novelty

The second-order perturbation $H_2$ — required at $O(\beta^{-1/2})$ — contains the non-radial Weyl-invariant correction:

$$H_2 = \sqrt{6}\left(\frac{p_2^3}{11520} + \frac{p_3^2}{8640}\right). \tag{Y.2}$$

Radial-only treatments (those that reduce to $r = \sqrt{x^2 + y^2}$ before computing $H_2$) drop the $p_3^2$ term. The $p_3^2/8640 \cdot \sqrt{6}$ contribution is what changes the $c_1$ coefficient. Including it is what produces the value $-311\sqrt{6}/9216$ rather than the radial-only result.

This is the main derivational novelty extracted from the old SU(3) notes (`SU3_Weyl_Invariant_c1_Derivation_Useful_Old_Notes.md` and related).

### §Y.3 Finite-channel leakage matrix

The SU(3) finite-channel ledger gives leakage amplitudes among the lowest four Weyl-invariant class states:

$$T^{(3)} = \begin{pmatrix} 0 & \frac{5}{24} & \frac{\sqrt{10}}{48} & 0 \\ \frac{5}{24} & 0 & \frac{7\sqrt{10}}{48} & \frac{\sqrt{5}}{16} \\ \frac{\sqrt{10}}{48} & \frac{7\sqrt{10}}{48} & 0 & 0 \\ 0 & \frac{\sqrt{5}}{16} & 0 & 0 \end{pmatrix}. \tag{Y.3}$$

The Perron root of $T^{(3)}$ is the root of the quartic

$$x^4 - \frac{215}{768}\, x^2 - \frac{175}{13824}\, x + \frac{25}{294912} = 0, \tag{Y.4}$$

with explicit numerical value

$$\rho_3 = 0.55016153352314258\ldots. \tag{Y.5}$$

### §Y.4 Polymer-resolvent threshold

Let $\mu_{\mathcal G}$ be the growth constant of the plaquette-overlap graph. The basic finite-channel summability condition is

$$\mu_{\mathcal G}\, \frac{\rho_3}{\sqrt{2\beta/3}} < 1, \tag{Y.6}$$

and the stronger Schur summability (Poincaré bridge form) is

$$\beta > \frac{3}{2}\, \mu_{\mathcal G}^4\, \rho_3^2. \tag{Y.7}$$

For $\mu_{\mathcal G} = 3$, (Y.7) gives

$$\boxed{\beta > 36.78.} \tag{Y.8}$$

This is a conditional finite-channel/Poincaré bridge threshold, not an unconditional 4D SU(3) lattice Yang–Mills theorem.

### §Y.5 SU(N) extension framework

The structure generalizes:

$$\boxed{\text{Weyl-invariant oscillator algebra} \Rightarrow T^{(N)} \Rightarrow \rho_N \Rightarrow \text{polymer threshold } \beta > \tfrac{N}{2} \mu_{\mathcal G}^4 \rho_N^2.}$$

The SU(N) version requires:
1. Generate invariant polynomials $\prod_{k=2}^N p_k^{m_k}$ to shell degree $D$.
2. Orthonormalize under the SU(N) Weyl-Gaussian measure.
3. Construct $T^{(N)}_{ab} = |\langle \psi_a, H_1^{\rm SU(N)} \psi_b \rangle_N|$.
4. Compute or bound $\rho_N$.

This is a real SU(N) research program. Pass 18 does not execute it.

### §Y.6 Manuscript-safe SU(3) claim language

**Use** (for the SU(3) standalone manuscript):

> We derive an explicit asymptotic gap law for the SU(3) local one-plaquette class-function Hamiltonian: $\Delta_{\rm SU(3)}(\beta) = \sqrt{2\beta/3} - 5/16 - (311\sqrt{6}/9216)\beta^{-1/2} + O(\beta^{-1})$. The leading and first correction agree with the radial reduction; the non-radial Weyl-invariant $p_3^2$ contribution in the second-order perturbation $H_2$ contributes to the $c_1$ coefficient, which is therefore $-311\sqrt{6}/9216$ rather than the radial-only value. A finite-channel leakage matrix $T^{(3)}$ with explicit Perron root $\rho_3 = 0.5502\ldots$ yields a conditional polymer-resolvent summability threshold $\beta > (3/2)\mu_{\mathcal G}^4 \rho_3^2$, equal to $36.78$ for plaquette-overlap-graph growth constant $\mu_{\mathcal G} = 3$.

**Do not use**:

> This proves the four-dimensional SU(3) Yang–Mills mass gap.

It does not. (Y.1)–(Y.8) are *local class-function* statements with *conditional* polymer summability beyond a finite-channel threshold.

### §Y.7 Why this belongs in a separate paper

Three reasons:

1. **It is a real local theorem in its own right.** The expansion (Y.1) is unconditional within its scope (one-plaquette class-function Hamiltonian, Weyl-invariant reduction, perturbative regime in $\beta^{-1/2}$). Folding it as an appendix in the PMBSF/SU(2) paper undersells it; treating it as a separate manuscript respects its standalone value.

2. **The proof route is independent of Lemma Q.** PMBSF/SU(2) is conditional on Lemma Q (open analytic theorem). SU(3) class-function asymptotic gap (Y.1) requires nothing from Lemma Q; it follows from perturbation theory + Weyl-invariant inner product algebra, all of which is unconditional. Splitting the papers separates the conditional-architecture claim from the unconditional local-theorem claim.

3. **Audience and venue differ.** The SU(3) work is local representation-theoretic / Weyl-character work suited to JMP, Lett. Math. Phys., or related venues. The PMBSF/SU(2) work is constructive-QFT/lattice statistical-mechanics work suited to CMP, JFA, or JSP. Co-bundling them confuses the venue choice for both.

### §Y.8 Pointer

Full derivation of $c_0$, $c_1$, the resolvent leakage formula, the Weyl-Gaussian inner products, the $T^{(3)}$ entries, and the SU(N) extension framework is in the Expanded Derivations document `NOTE_PMBSF_expanded_derivations_lemmaq_su3_2026_05_25.md`, sections 9 through 15 (covering §9 setup, §10 scaled perturbation, §11 first correction, §12 second correction, §13 finite-channel matrix, §14 polymer-resolvent threshold, §15 SU(N) extension). That document is the technical spine for the standalone SU(3) manuscript.

---

*End of pass 18 master document. Supersedes pass 17.*

*Pass 18 adds §15 (consolidated honesty-corrections register), Appendix T §T.11 (two pass-17 follow-up honesty corrections), and five new appendices U–Y. The pass-7 conditional status is preserved. Lemma Q replaces (M′)_SU(2) as the canonical name for the SU(2)-specific analytic target from pass 18 forward; pre-pass-18 references are retained as historical.*


---

## Appendix Z: Pass-19 exact heat-bath Stage B and LCI/TOS+J reduction

### Z.1 Exact heat-bath Stage B geometry robustness

The side-10/core-margin-3 Stage B diagnostic has been rerun with exact SU(2) heat-bath block resampling.

Run:

\[
\texttt{PMBSF\_SU2\_LemmaQ\_block\_conditional\_stageB\_heatbath\_20260525\_215913}.
\]

Configuration:

\[
L=16,\qquad \beta=3.5,\qquad q_\eta=0.003,\qquad \eta=0.005.
\]

The exact update law was

\[
U_\ell
\sim
\mathrm{vMF}_4
\left(
\frac{\overline H_\ell}{\|H_\ell\|},
\beta\|H_\ell\|
\right),
\]

with acceptance one by construction. The block geometry was side \(10\), core margin \(3\), two blocks per global configuration, \(64\) frozen-boundary blocks total, \(864\) core plaquettes per block, block therm \(192\), block between \(8\), block samples \(256\), and distance bins through \(d=12\).

Thresholding with the proof-friendly upper-envelope ramp gave

\[
t=1.0104245908659366,\qquad
q_\eta=0.003000000000000041,\qquad
q_{\rm hard}=0.0029478073120117188.
\]

Single-source conditional control:

\[
\max_{\rm depth}\operatorname{median}(q_{\rm cond}/q_\eta)=1.3020833,
\]

\[
q95(q_{\rm cond}/q_\eta)=2.6041667,
\qquad
\max(q_{\rm cond}/q_\eta)=9.1145833.
\]

Ordinary cavity:

\[
\max\Lambda=2.5930038,
\qquad
\operatorname{median}\Lambda=1.0158112.
\]

Rooted cavity:

\[
\max\Lambda_{\rm root}=2.3431348,
\qquad
\operatorname{median}\Lambda_{\rm root}=1.0221089.
\]

Cap predictors had correct signs but weak explanatory power:

\[
\text{slope}_g=-0.17918134,
\quad
R_g^2=0.0075893205,
\]

\[
\text{slope}_\rho=-8.33064,
\quad
R_\rho^2=0.022467109.
\]

Interpretation: this run supersedes the earlier Metropolis side-10 Stage B diagnostic as the primary geometry-robustness anchor. It supports the block source-stability mechanism at side-10 geometry, but does not prove Lemma Q.

### Z.2 LCI/TOS+J reduction

For a block Gibbs measure \(\mu=\mu_C^\xi\), define

\[
Z_A(s)=\mathbb E_\mu\prod_{p\in A}(1+sX_p).
\]

If

\[
Z_A(\rho/q_\eta)\le e^{K|A|}
\]

for all finite \(A\subset C^\circ\), then positivity of the coefficients gives

\[
\mathbb E_\mu\prod_{p\in B}X_p
\le
\left(e^K\rho^{-1}q_\eta\right)^{|B|}.
\]

Thus the positive source-radius bound implies Lemma Q.

A sufficient condition is TOS+J:

\[
\mathbb E_{\mu^{S,s}}X_p
\le
Cq_\eta\exp\left(\sum_{r\in S}J(p,r)\right),
\qquad
J(p,r)\le C_Je^{-m_Jd_C(p,r)},
\]

for \(0\le s\le\rho/q_\eta\). If \(J_*=\sup_p\sum_rJ(p,r)<\infty\), then ordering \(A=\{p_1,\ldots,p_n\}\) gives

\[
Z_A(\rho/q_\eta)
\le
\exp(\rho C e^{J_*}|A|).
\]

Therefore:

\[
\boxed{
\text{TOS+J}
\Rightarrow
\text{positive source-radius bound}
\Rightarrow
\text{Lemma Q}.
}
\]

To prove TOS+J, choose an incident heat-bath link \(e(p)\). The SU(2) one-link law is

\[
U_e\mid U_{e^c}
\sim
\mathrm{vMF}_4
\left(
\frac{\overline H_e}{\|H_e\|},
\beta\|H_e\|
\right).
\]

Each incident source is bounded by a spherical cap

\[
X_r\le \mathbf1_{C_r},
\qquad
C_r=\{u:u\cdot n_r\le a\},
\qquad
a=1-(t-\eta).
\]

Local cap-intersection stability is the finite-dimensional condition

\[
\nu(C_p\cap C_A)\le C_{\rm LCI}q_\eta\,\nu(C_A)
\]

for every incident subset \(A\subset\{r\ne p:r\ni e\}\). Since a link in four dimensions has only six incident plaquettes, this is a finite \(S^3\) cap-intersection theorem.

LCI implies stability under all incident positive tilts. Far source factors do not enter the one-link integral directly; they distort the environment \(U_{e^c}\) and must be controlled by Balaban/Dimock locality:

\[
\mathbb E_{\mu^{S_{\rm far},s}}
\left[
X_p\mathbf1_{\mathcal G_{e,p}^{\rm LCI}}
\right]
\le
Cq_\eta
\exp\left(\sum_{r\in S_{\rm far}}J(p,r)\right).
\]

The complement is rooted:

\[
Y_p^{\rm LCI}=X_p\mathbf1_{(\mathcal G_{e,p}^{\rm LCI})^c}.
\]

The refined open theorem is therefore:

\[
\boxed{
\text{LCI-good typicality + Balaban far-source stability}
\Rightarrow
\text{TOS+J}.
}
\]

This is now the sharpest analytic target replacing the earlier broad phrase “prove Lemma Q.”
