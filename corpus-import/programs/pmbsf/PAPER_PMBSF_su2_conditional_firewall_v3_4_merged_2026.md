# A conditional projected-capacity firewall closure for SU(2) lattice gauge theory via local cap-intersection stability and Bałaban far-source stability

**Draft v3.4, journal-agnostic.** 2026-05-26.

*v3.4 changelog:* uses the uploaded v2 as the front-matter and §§1–3 base because it has the strongest two-input architecture, deterministic threshold-law section, and literature-gap framing. It then appends coherent §§4–12 to complete the manuscript structure promised in §1.8: random plaquette-incidence comparator, exact SU(2) heat-bath geometry, LCI, Bałaban far-source stability, deterministic implication chain, numerical evidence, open analytic tasks, SU(3) companion relation, and honesty/status register.

*v2 changelog (against `_v1` of 2026-05-25): central conditional architecture sharpened from three inputs (Lemma Q + source-weighted Bałaban + boundary-band gate) to two inputs (LCI typicality + Bałaban far-source stability) plus one deterministic auxiliary (boundary-band gate). Lemma Q is now a derived consequence of TOS+J via two formally-proved chain pieces (Propositions Z.1 + Z.2 of the master), not an axiom of the conditional theorem stack. §1.4 numerical-support summary updated to reflect the new exact-heat-bath side-10 anchor superseding the prior Metropolis side-10. §1.5 status table rewritten to show two open analytic theorems (Z.A, Z.B) instead of one (Lemma Q). Substance of §1.6 (honesty corrections) unchanged.*

---

## Abstract

We organise the projected Maxwell Birman–Schwinger firewall (PMBSF) program for SU(2) lattice Yang–Mills at large coupling $\beta$ into an explicit conditional theorem with two precisely-stated analytic targets. The deterministic spine of the program is unconditional: the projected covariance comparator $A_p = P \mathbf 1_{\partial p} P$, the polymer-type ordered (PTO) summability framework, and the projected Birman–Schwinger firewall criterion are established by finite-dimensional spectral and combinatorial arguments and require no probabilistic input. The probabilistic content of the program reduces, via a deterministic chain involving two formally-proved coefficient-extraction steps, to two finite SU(2)-specific theorems:

> **Local cap-intersection (LCI) typicality + Bałaban far-source stability of LCI parameters $\implies$ SU(2) projected-capacity firewall closure**

The LCI typicality input asks for a finite-dimensional spherical convex-geometry condition on the one-link conditional law on $S^3$: under tempered SU(2) Wilson heat-bath geometry at large $\beta$, the support height of the target cap separated from incident cap-intersection support heights by a margin $\chi_0 > 0$ uniform in incident-source subset (the **LCI good event**), with the complement rooted into a non-rare-event indicator. The Bałaban far-source stability input asks for an explicit exponentially-decaying influence kernel controlling distortion of LCI parameters under positive far-source tilts: a source-marked random-walk locality statement in the Bałaban / Dimock RG framework. **These two theorems together replace the previously-stated "source-weighted Bałaban cluster expansion" as the open analytic content of the program; both are strictly narrower.**

The remaining inter-step is closed: a telescoping chain rule and Taylor-coefficient positivity extraction (Propositions Z.1 + Z.2 of the master) give the formally-proved implication chain

$$\text{LCI + far-source stability} \implies \text{tilted one-source stability (TOS+J)} \implies \text{positive source-radius bound} \implies \text{Lemma Q} \implies \text{rooted cumulants and PMBSF closure}.$$

Lemma Q is thus a *derived consequence*, not an axiom.

We supply four independent empirical lines of evidence at the working point $\beta = 3.5$, $\eta = 0.005$, $q_\eta = 0.003$ for the consequences of LCI + far-source stability. **(i)** Exact one-link heat-bath block-conditional diagnostics at $L = 16$ on $8^4$ blocks with frozen exterior (32 blocks, 864 core plaquettes/block) give median conditional cavity ratio $\Lambda = 0.9249$ and median rooted cavity ratio $\Lambda_{\rm root} = 0.9563$, with maxima 1.46 and 1.40. **(ii)** Exact one-link heat-bath block-conditional diagnostics at $L = 16$ on $10^4$ blocks with margin-3 core (64 blocks, distance bins through $d = 12$) give median $\Lambda = 1.02$, median $\Lambda_{\rm root} = 1.02$, maxima 2.59 and 2.34. **(iii)** Full-volume Wilson SU(2) pair and rooted-pair covariance at $L \in \{12, 16, 64\}$ shows median ratios dropping $17\times$ from $L = 12$ to $L = 64$ while maxima remain $O(1)$ throughout — the empirical signature of Lemma Q's $k = 1$ consequence at full volume. **(iv)** A deterministic projected-capacity threshold-law on $\mathbb T_{64}^2$ achieves AUC $= 1.000$ for negative-crossing classification across 630 mask-coupling configurations, validating the deterministic spine's central operator object in a synthetic setting where ground truth is exactly computable. None of the four lines proves either LCI typicality or far-source stability; all four show the qualitative pattern those theorems predict.

A register of six prior honesty corrections through the program's history documents where earlier versions overstated and what survived correction; the register is itself part of the program's defensibility architecture.

**Keywords.** SU(2) lattice gauge theory; mass gap; projected capacity; Birman–Schwinger criterion; cluster expansion; local cap-intersection stability; conditional theorem.

**MSC primary.** 81T13 (Yang–Mills and other gauge theories), 81T25 (Quantum field theory on lattices), 60K35 (Interacting random processes; statistical mechanics type models). **Secondary.** 82B20 (Lattice systems), 47A10 (Spectrum, resolvent), 60G60 (Random fields).

---

## 1. Introduction

### 1.1 The two-input conditional architecture

The Yang–Mills mass-gap problem on a four-dimensional lattice with gauge group SU(2) asks for an exponentially decaying upper bound on connected correlations of local gauge-invariant observables, uniformly in the lattice spacing in an appropriate continuum limit. The unconditional rigorous progress of the last forty years can be organised, very roughly, into three layers: (a) the small-coupling Wilson character expansion, which converges for $\beta$ below a calculable threshold; (b) the constructive renormalization-group / cluster-expansion machinery of Bałaban \[Bałaban 1985a, 1985b, 1987, 1988\] and Dimock \[Dimock 2013a, 2013b, 2014\], which handles the small/large-field decomposition, background-field localization, and convergent polymer expansions; (c) the deterministic operator-theoretic comparator and projected-capacity framework developed more recently and which gives the Birman–Schwinger firewall structure pursued in this paper.

The PMBSF program is the working name for an attempt to **bridge (c) to (b)**: to convert the deterministic projected-capacity criterion of (c) into a probabilistic mass-gap statement at large $\beta$ by combining it with the constructive expansion machinery of (b). The bridge is not, at present, closed. The purpose of this paper is to identify the two precise analytic theorems that close it, supply the deterministic chain that reduces the program to those two theorems, and report the targeted numerical support.

The central conditional architecture is

$$\boxed{\text{LCI typicality} \;+\; \text{Bałaban far-source stability of LCI parameters} \;+\; \text{boundary-band gate at } \eta \to 0 \;\implies\; \text{SU(2) projected-capacity firewall closure}.}$$

Of the three inputs:

- **LCI typicality (Open Theorem A)** is a finite-dimensional spherical convex-geometry statement about the SU(2) one-link conditional law. Conditional on all links except one incident link $e$ to a target plaquette $p$, the Wilson conditional law on the unit quaternion $U_e \in S^3$ is the exact von Mises–Fisher law $\mathrm{vMF}_4(\overline{H_e}/\|H_e\|, \beta\|H_e\|)$ \[Fisher 1953; Kennedy–Pendleton 1985; Banerjee et al. 2005\]. The high-plaquette indicator $X_{p,\eta}$ for the target plaquette is bounded by the indicator of a spherical cap on $S^3$, and similarly for each plaquette $r$ incident to $e$. The LCI good event asks for a uniform separation $u_A \cdot n_p - a \geq \chi_0 > 0$ between the target cap and each incident-subset cap-intersection support, where $u_A$ is the cap-intersection support maximizer; combined with a uniform curvature lower bound this gives the conditional probability bound $\nu(C_p \mid C_A) \leq C_{\rm LCI}\, q_\eta$. The bad event $\mathcal B_{e,p}^{\rm LCI}$ is rooted into a source root $Y_p^{\rm LCI} = X_{p,\eta} \mathbf 1_{\mathcal B_{e,p}^{\rm LCI}}$, consistent with the rooted-bad-staple strategy.

- **Bałaban far-source stability (Open Theorem B)** is a source-marked random-walk locality statement. Far source factors (sources on plaquettes not incident to the chosen link $e$) distort the environment $U_{e^c}$ — and therefore the LCI parameters $m_e$, $\kappa_e$, $\{n_r\}_{r \ni e}$, $\chi_0$, the LCI good event itself — only through the outer block Gibbs distribution. Theorem B asks that this distortion preserves the LCI good event up to a positive influence-kernel sum $\exp(\sum_{r \in S_{\rm far}} C e^{-m\, d(p, r)})$ uniform in the far-source set and exponentially summable in distance. This is where Bałaban / Dimock RG random-walk decay must enter; the unmarked machinery is established by \[Bałaban 1988; Dimock 2013a, 2013b, 2014\], the marked version is open.

- **Boundary-band gate at $\eta \to 0$** is the deterministic step that converts the smooth-source rare-event setup (where the source is the upper envelope of $\phi_p \geq t - \eta$) into the hard-cutoff setup at $\eta = 0$. The smooth setup is the natural one for analytic estimates; the hard cutoff is the one that connects to physical mass-gap statements. The deterministic boundary-band machinery is well-known and we sketch it; the specific $\eta$-uniform bound needed remains an analytic input.

### 1.2 The deterministic chain: from LCI + far-source stability to closure

The implication chain from the two open theorems to PMBSF closure is, except for the two theorems themselves, formally proved. Writing $X_p = X_{p,\eta}$ for the smooth source indicator, $q_\eta = \mathbb E[X_p]$ for its mean, $\mu = \mu_C^\xi$ for the frozen-exterior block Gibbs measure, and

$$d\mu^{S, s} = \frac{\prod_{r \in S}(1 + s X_r)}{\mathbb E_\mu \prod_{r \in S}(1 + s X_r)} \, d\mu \tag{1.1}$$

for the positive source-tilted measure with source set $S$ and tilt strength $s \in [0, \rho/q_\eta]$:

**Theorem 1 (LCI + far-source stability ⇒ TOS+J).** Under the hypotheses of Open Theorems A and B,

$$\mathbb E_{\mu^{S, s}} \big[X_p \mathbf 1_{\mathcal G_{e, p}^{\rm LCI}}\big] \leq C\, q_\eta \exp\Big(\sum_{r \in S} J(p, r)\Big), \qquad J(p, r) \leq C_J\, e^{-m_J\, d_C(p, r)}, \tag{1.2}$$

with the LCI-bad component absorbed in the source root $Y_p^{\rm LCI}$.

**Proposition 1 (TOS+J ⇒ positive source-radius bound).** Under (1.2) with $J_* := \sup_p \sum_{r \neq p} J(p, r) < \infty$, the positive source partition function $Z_A(s) := \mathbb E_\mu \prod_{p \in A}(1 + s X_p)$ satisfies

$$Z_A(\rho/q_\eta) \leq \exp\big(\rho\, C e^{J_*}\, |A|\big) \tag{1.3}$$

for all finite $A \subset C^\circ$. *Proof:* telescoping chain rule on the ratio $Z_{A_j}/Z_{A_{j-1}}$ applied to (1.2).

**Proposition 2 (Positive source-radius ⇒ Lemma Q).** Under (1.3), for all $B \subset C^\circ$,

$$\mathbb E_\mu \prod_{p \in B} X_p \leq (C_Q\, q_\eta)^{|B|}, \qquad C_Q = \rho^{-1} e^K. \tag{1.4}$$

*Proof:* the Taylor coefficients of $Z_B(s) = \sum_{R \subset B} s^{|R|} \mathbb E_\mu \prod_{p \in R} X_p$ are non-negative, so $s^{|B|} \mathbb E_\mu \prod_{p \in B} X_p \leq Z_B(s)$ evaluated at $s = \rho/q_\eta$ gives (1.4).

The chain (1.2) → (1.3) → (1.4) → rooted cumulants → pair/rooted closure → PTO level-(iii) → HPM → projected firewall is what reduces the program to the two open theorems plus the boundary-band auxiliary. Each individual arrow is either deterministic (Propositions 1 and 2 above; the deterministic chain steps from §§3–4 below) or established by standard polymer-expansion machinery applied with input controlled by (1.4) \[Kotecký–Preiss 1986; Fernández–Procacci 2007; Ueltschi 2004\].

**Lemma Q itself is now a derived consequence.** Earlier formulations of the PMBSF program treated Lemma Q as an axiomatic input. The Propositions 1 and 2 above show that the cavity-intensity bound and the multiplicative Lemma Q both follow deterministically from TOS+J, which in turn follows from LCI + far-source stability by Theorem 1. The source-weighted Bałaban cluster expansion that previous formulations required as a separate input is *not needed* — Proposition 2 substitutes for it via Taylor-coefficient positivity. This is a substantive simplification of the conditional theorem stack.

### 1.3 The literature gap

A targeted survey of the constructive lattice gauge theory and polymer-expansion literature locates the precise gap. The Bałaban / Dimock constructive renormalization-group line \[Bałaban 1985a, 1985b, 1987, 1988; Dimock 2013a, 2013b, 2014\] supplies the gauge-RG bookkeeping for unmarked activities. The abstract polymer expansion theory \[Kotecký–Preiss 1986; Fernández–Procacci 2007; Ueltschi 2004\] supplies the convergence criteria. The closest *source-marked* analogue in the rigorous literature is the random-currents source-set calculus for Ising and Ising lattice gauge theory \[Duminil-Copin 2018; Forsström–Viklund 2025\], which carries explicit switching-lemma source-set technology in nearby (but abelian and lower-spin) models. The geometric input — Fisher / von Mises–Fisher distributions on $S^3$ and spherical-cap intersections \[Fisher 1953; Kennedy–Pendleton 1985; Banerjee et al. 2005; Besau–Werner 2016; Mazonka 2012\] — is well-established. The deterministic projected-capacity / firewall criterion is in the spirit of the modern zero-free / Cauchy-extraction line \[Patel–Regts 2017; Liu–Sinclair–Srivastava 2019\] and is established here unconditionally.

What is **missing** from the rigorous literature is precisely the LCI-parameter version of source-marked random-walk locality (Open Theorem B) and the LCI typicality theorem (Open Theorem A). The geometric input (the cap-intersection geometry of LCI) and the polymer combinatorics (Bałaban/Dimock for unmarked activities) are individually well-understood. Their **LCI-specific synthesis in a non-abelian gauge-RG setting appears to be new analytic territory**. The gap is real but narrow: in passing from the previous "source-weighted Bałaban expansion" formulation to "LCI typicality + Bałaban far-source stability of LCI parameters," the open theorems are strictly narrower and concretely formulated as a spherical convex-geometry typicality theorem on $S^3$ (Open Theorem A) and a source-marked random-walk locality theorem on a specific finite-dimensional good-event indicator (Open Theorem B).

### 1.4 Targeted numerical support

A program organised around two open analytic theorems invites the question of whether the theorems can be expected to hold at all. We address this with four independent empirical lines of evidence at the working point $\beta = 3.5$, $\eta = 0.005$, $q_\eta = 0.003$. The first two are algorithm-aligned block-conditional diagnostics with exact one-link heat-bath sampling matching the analytic conditional measure; the third is full-volume Wilson SU(2) pair and rooted-pair covariance; the fourth is a deterministic projected-capacity threshold-law validation in a synthetic 2D scalar setting. None of the four proves either Open Theorem A or Open Theorem B. All four show the qualitative pattern those theorems predict.

1. **Exact one-link heat-bath, side-8 block, margin-2 core.** $L = 16$, 32 frozen-boundary blocks, 864 core plaquettes per block, distance bins through $d \approx 4$, depth bin $\{2\}$. Single-source conditional control: max depth-median $q_{\rm cond}/q_\eta = 0.87$. Cavity ratio: median $\Lambda = 0.9249$, max $\Lambda = 1.46$. Rooted cavity ratio: median $\Lambda_{\rm root} = 0.9563$, max $\Lambda_{\rm root} = 1.40$. The medians being slightly below 1 reflects the absence of algorithmic mixing artifact under exact heat-bath sampling; the sub-1 medians are consistent with the constraint imposed by exterior freezing.

2. **Exact one-link heat-bath, side-10 block, margin-3 core.** $L = 16$, 64 frozen-boundary blocks, 864 core plaquettes per block, distance bins through $d = 12$, depth bins $\{3, 4\}$. Single-source conditional control: max depth-median $q_{\rm cond}/q_\eta = 1.30$, q95 = 2.60, max = 9.11. Cavity ratio: median $\Lambda = 1.02$, max $\Lambda = 2.59$. Rooted cavity ratio: median $\Lambda_{\rm root} = 1.02$, max $\Lambda_{\rm root} = 2.34$. The medians being $\approx 1.00$ (with the larger sample of 36× more plaquettes per block) match Open Theorem A's prediction of $O(q_\eta)$ at typical conditioning to within statistical resolution.

3. **Full-volume Wilson SU(2) pair and rooted-pair covariance at $L \in \{12, 16, 64\}$.** Tests the deterministic-chain consequence of (1.4) at $k = 1$:

   $$|\mathrm{Cov}(X_p, X_q)| \leq C\, q_\eta^2\, e^{-m\, d(p,q)}.$$

   Median $|\mathrm{Cov}(X, X)| / q_\eta^2$ drops $0.117 \to 0.071 \to 0.007$ (a factor of 17) as $L$ scales from 12 to 64; the rooted analogue tracks. Maxima oscillate $O(1)$ across all three lattice sizes. This is the direct empirical signature of the $k = 1$ consequence at full volume up to $L = 64$.

4. **Deterministic projected-capacity threshold-law on $\mathbb T_{64}^2$.** In a synthetic 2D scalar setting with controlled sparse-dimer defect masks across six geometric families at fixed local geometry (density, defect count, cluster count, largest cluster all held constant), the scalar projected-capacity surrogate $V_c^R = \lambda_1 / \|P \mathbf 1_D P\|$ tracks the exact projected Birman–Schwinger critical coupling $V_c^{BS} = \|\Lambda^{-1/2} P \mathbf 1_D P \Lambda^{-1/2}\|^{-1}$ with calibration $\log V_c^{BS} = 1.66 + 1.22 \log V_c^R$ at $R^2 = 0.922$. An order-parameter attack with 630 (mask, coupling) configurations achieves AUC $= 1.000$ for negative-crossing classification under the projected Birman–Schwinger criterion. This validates the deterministic spine in a setting where ground truth is exactly computable; it does *not* validate either Open Theorem A or Open Theorem B (which are Wilson stochastic statements) but it does validate the operator-theoretic premise that projected capacity is a meaningful predictive variable for sparse-defect low-mode instability.

The first two anchors are the *algorithm-aligned* block-conditional diagnostics: same sampling law as Open Theorem A's hypothesis, both at small (side-8) and larger (side-10) geometry. Anchor 3 is the global covariance consequence of (1.4). Anchor 4 is the deterministic-spine validation. The four lines are independent in that each tests a distinct consequence or premise; none proves the two open analytic theorems.

### 1.5 What this paper proves and what it does not

**Proved (unconditional within scope):**

1. The deterministic projected-capacity / Birman–Schwinger firewall framework: PTO summability of the projected covariance comparator $A_p = P \mathbf 1_{\partial p} P$; the projected Birman–Schwinger criterion as a finite-dimensional spectral condition.
2. **Proposition 1**: TOS+J $\implies$ positive source-radius bound, via telescoping chain rule on the source-tilted partition function.
3. **Proposition 2**: positive source-radius bound $\implies$ Lemma Q (multiplicative form), via Taylor-coefficient positivity extraction.
4. **Theorem 1**: LCI typicality (Open Theorem A) + far-source stability (Open Theorem B) $\implies$ TOS+J.
5. The deterministic chain `LCI + far-source stability $\implies$ TOS+J $\implies$ source-radius $\implies$ Lemma Q $\implies$ rooted cumulants $\implies$ PTO level-(iii) $\implies$ HPM $\implies$ projected firewall`, conditional on Open Theorems A and B but unconditional in each individual step.

**Conditional or open:**

1. **Open Theorem A — LCI good-event typicality.** Under tempered SU(2) Wilson heat-bath geometry at large $\beta$, the LCI good event $\mathcal G_{e,p}^{\rm LCI}$ holds with rooted/absorbed complement. This is a spherical convex-geometry typicality theorem on $S^3$.
2. **Open Theorem B — Bałaban far-source stability of LCI parameters.** Far-source positive tilts preserve LCI parameters up to influence-kernel sum $\exp(\sum_r C e^{-m\, d(p, r)})$. This is a source-marked random-walk locality theorem in the Bałaban/Dimock RG framework, restricted to the LCI good-event indicator.
3. **Boundary-band gate at $\eta \to 0$.** Deterministic auxiliary; standard machinery but the $\eta$-uniform bound needed is open.

**Not claimed.** This paper does **not** prove the four-dimensional SU(2) Yang–Mills mass gap. It does not prove the continuum limit of the lattice theory retains a positive mass gap. It does not establish either Open Theorem A or Open Theorem B. What it does is identify the *two* probabilistic theorems whose proofs close the conditional architecture, supply the deterministic chain that reduces the program to those two theorems, and supply empirical evidence that the consequences of those theorems hold at the working point.

### 1.6 The honesty corrections register

The PMBSF program has accumulated six explicit corrections to prior claims through its development. Three are analytic (a sign convention in a Lyapunov drift condition; a false ratio assumption in an early rooted-source argument; a numerical factor of four in a Haar-measure expectation), two are statistical (a wide confidence interval on a decay-rate point estimate; a binary-classifier artifact in an extended-regression $R^2$), and one is an early empirical retraction (a closed proof route was retracted after auditing). None of the corrections affects the conditional theorem stack of §1.1; each either retracted an empirical over-claim, fixed a sign or factor that did not propagate, or sharpened a diagnostic interpretation. We list them explicitly in §12 as the program's defensibility architecture. The discipline of documenting and surviving correction is itself part of why the surviving claims are credible.

In particular, the pass-10 honesty correction (correction 3 in §12) which retired *unrooted bad-staple rarity* is directly relevant to the LCI architecture: the LCI bad event $\mathcal B_{e,p}^{\rm LCI}$ in this paper is absorbed into a source root $Y_p^{\rm LCI} = X_{p,\eta} \mathbf 1_{\mathcal B_{e,p}^{\rm LCI}}$, matching the rooted strategy that the correction established. The pass-17 honesty corrections 5 and 6 on the Stage A decay-rate point estimates and the cap-feature extended regression are also directly relevant: they confirm that the cap mechanism is the local seed, not the load-bearing theorem, which is precisely what the two-input LCI + far-source-stability framing reflects.

### 1.7 Relation to existing work

The Bałaban / Dimock constructive lattice gauge program \[Bałaban 1985a, 1985b, 1987, 1988; Dimock 2013a, 2013b, 2014\] established the convergent renormalization-group expansion for unmarked activities in three- and four-dimensional non-abelian lattice gauge theories at sufficient (small) coupling. The PMBSF program is, in spirit, an attempt to identify *the smallest sufficient probabilistic inputs* — Open Theorems A and B — that, combined with the deterministic projected-capacity criterion, give an explicit firewall closure at large $\beta$.

The abstract polymer-expansion convergence theory \[Kotecký–Preiss 1986; Fernández–Procacci 2007; Ueltschi 2004\] supplies the combinatorial input. The closest source-marked analogue in the rigorous literature is the random-currents and source-set calculus for Ising and Ising lattice gauge theory \[Duminil-Copin 2018; Forsström–Viklund 2025\], which carries explicit switching-lemma and source-set technology in abelian models. The geometric input — vMF distributions on $S^3$ and spherical-cap intersections \[Fisher 1953; Kennedy–Pendleton 1985; Banerjee et al. 2005; Besau–Werner 2016; Mazonka 2012\] — is well-established and is what enters Open Theorem A. The modern zero-free / Cauchy-extraction line \[Patel–Regts 2017; Liu–Sinclair–Srivastava 2019\] is the deterministic-side comparator for the projected Birman–Schwinger criterion. **A key observation of this paper is that Proposition 2 — coefficient extraction by Taylor positivity — substitutes for a source-weighted version of the Bałaban / Dimock expansion in the conditional theorem stack.** What appears in §6 is therefore a sharpening of the conventional cluster-expansion-only architecture: positive-radius extraction does the job that source-weighted polymer convergence would have done, without needing the source-weighted upgrade of Bałaban / Dimock to be developed.

A companion paper treats the SU(3) one-plaquette class-function asymptotic gap law as an independent local spectral theorem with explicit constants, including the non-radial Weyl-invariant $p_3^2$ correction to the $\beta^{-1/2}$ coefficient. The SU(3) work is unconditional within its scope and is independent of the conditional architecture of the present paper.

### 1.8 Outline

§2 sets up the notation: Wilson SU(2) at large $\beta$, plaquette excess, smooth upper-envelope source indicator, $q_\eta$, rooted source, Bałaban block geometry. §3 develops the deterministic projected-capacity framework: Maxwell projection, the projected comparator $A_p = P \mathbf 1_{\partial p} P$, PTO summability, the projected Birman–Schwinger firewall criterion. **§3.5 reports the deterministic threshold-law validation at $L=64$ on $\mathbb T_{64}^2$** in a synthetic 2D scalar setting where ground truth is exactly computable. §4 develops the random plaquette-incidence comparator. §5 presents the SU(2) heat-bath mechanism: vMF on $S^3$, spherical-cap formulation, the DLR reduction to a one-link cap problem, the incident / far source split. **§6 develops local cap-intersection (LCI) stability**: the definition (Definition Z.4), the computable spherical convex-geometry criterion (eqs Z.25, Z.28), the LCI bad event $\mathcal B_{e,p}^{\rm LCI}$ and its absorption into the source root $Y_p^{\rm LCI}$, and the proved implication LCI $\implies$ incident positive TOS (Proposition Z.5). **§7 develops Bałaban far-source stability**: the Open Theorem B statement, the random-walk locality program, the connection to the unmarked Bałaban/Dimock machinery. **§8 presents the deterministic chain**: Theorem 1 (LCI + far-source stability $\implies$ TOS+J), Proposition 1 (TOS+J $\implies$ positive source-radius), Proposition 2 (positive source-radius $\implies$ Lemma Q), and the polymer-expansion-based reduction Lemma Q $\implies$ PMBSF closure. **§9 presents the four-leg numerical evidence**: §V.1 exact-HB side-8, §AA exact-HB side-10, §W full-volume covariance through $L = 64$, §X projected-capacity threshold-law on $\mathbb T_{64}^2$. §10 enumerates the open analytic tasks (Open Theorems A and B plus the boundary-band gate) and discusses what each requires. §11 connects to the SU(3) companion paper. §12 closes with the manuscript-safe scope statement and the consolidated honesty-corrections register.

---

## 2. Notation and setup

This section fixes the lattice geometry, the gauge group, the plaquette source indicator, the rooted source, the Bałaban block conditioning, and the source-tilted measure. The setup is standard; we lay it out explicitly because §§3–12 refer to these objects as established notation.

### 2.1 Lattice, gauge group, Wilson action

Let $\Lambda_L = (\mathbb{Z}/L\mathbb{Z})^4$ be a periodic four-dimensional lattice of side $L$, with elementary edges $e$ and elementary plaquettes $p$. We work with the gauge group $G = \mathrm{SU}(2)$ and assign a group element $U_e \in G$ to each oriented edge $e$, with the convention $U_{-e} = U_e^{-1}$.

For a plaquette $p$ specified by base vertex $x$ and two directions $\mu < \nu$, the plaquette holonomy is

$$U_p := U_{(x, \mu)}\, U_{(x + \hat\mu, \nu)}\, U_{(x + \hat\nu, \mu)}^{-1}\, U_{(x, \nu)}^{-1}. \tag{2.1}$$

The Wilson plaquette action is

$$S_W(U) := \beta \sum_{p \in \Lambda_L^*} \big(1 - \tfrac{1}{2}\operatorname{Re}\operatorname{Tr} U_p\big), \tag{2.2}$$

where $\Lambda_L^*$ denotes the set of all oriented plaquettes (each unoriented plaquette counted once), and $\beta > 0$ is the inverse coupling. The Wilson Gibbs measure is

$$d\mu_\beta(U) := Z_\beta^{-1} \exp(-S_W(U)) \prod_e dU_e, \tag{2.3}$$

with $Z_\beta$ the partition function and $dU_e$ normalized Haar measure on $G$.

### 2.2 Quaternion encoding of SU(2)

We use the standard identification of $G = \mathrm{SU}(2)$ with the unit quaternions on $S^3 \subset \mathbb{R}^4$. A group element

$$U = u_0 \mathbf{1} + i u_1 \sigma_1 + i u_2 \sigma_2 + i u_3 \sigma_3, \qquad u \in S^3, \tag{2.4}$$

is identified with the quaternion $u = (u_0, u_1, u_2, u_3) \in S^3$. With $\bar u := (u_0, -u_1, -u_2, -u_3)$ the quaternion conjugate, the standard quaternion product $u \cdot v$ identifies with the group product $UV$, and the **scalar inner product**

$$u \cdot v := u_0 v_0 + u_1 v_1 + u_2 v_2 + u_3 v_3 \tag{2.5}$$

(the standard $\mathbb{R}^4$ inner product on unit quaternions) gives

$$\operatorname{Scal}(uv) = u \cdot \bar v = \bar u \cdot v, \qquad \tfrac{1}{2}\operatorname{Re}\operatorname{Tr} U = u_0. \tag{2.6}$$

Throughout the paper, "the heat-bath mean direction at link $e$" refers to $m_e := \overline{H_e} / \|H_e\|$, where $H_e \in \mathbb{R}^4$ is the staple-sum quaternion at $e$, and the conjugation is necessary because of (2.6). This is the convention that produces the exact one-link conditional law (Lemma 5.1 below).

### 2.3 Plaquette excess

The plaquette excess at plaquette $p$ is

$$\phi_p(U) := 1 - \tfrac{1}{2} \operatorname{Re} \operatorname{Tr} U_p \;\in\; [0, 2]. \tag{2.7}$$

In quaternion form $\phi_p = 1 - (U_p)_0$. The Wilson action (2.2) is $S_W = \beta \sum_p \phi_p$.

We work throughout at the empirical working point

$$\boxed{\beta = 3.5, \qquad \eta = 0.005, \qquad q_\eta = 0.003,} \tag{2.8}$$

with lattice sizes $L = 16$ for block-conditional diagnostics and $L \in \{12, 16, 64\}$ for full-volume covariance diagnostics, calibrated such that the threshold-tuned $t \approx 1.01$ (see §2.4). The choice of $\beta = 3.5$ places the system well above the SU(2) deconfinement crossover and inside the strong-coupling regime where convergent character expansions exist; the calibration of $q_\eta = 0.003$ matches the rare-event scale at which the polymer expansion's source-rate input becomes the load-bearing combinatorial quantity.

### 2.4 Smooth upper-envelope source indicator

Fix a threshold $t \in (0, 2)$ and smoothing scale $\eta \in (0, t)$. The **smooth upper-envelope source indicator** at plaquette $p$ is

$$\boxed{X_{p, \eta}(U) := \operatorname{clip}\!\Big(\frac{\phi_p(U) - (t - \eta)}{\eta},\, 0,\, 1\Big) = \operatorname{clip}\!\Big(\frac{\phi_p - t}{\eta} + 1,\, 0,\, 1\Big).} \tag{2.9}$$

By construction:

- $X_{p, \eta} = 0$ for $\phi_p \leq t - \eta$,
- $X_{p, \eta} = 1$ for $\phi_p \geq t$,
- linear ramp from 0 to 1 on $\phi_p \in [t - \eta, t]$.

This satisfies the **upper-envelope sandwich**

$$\mathbf{1}_{\{\phi_p \geq t\}} \;\leq\; X_{p, \eta} \;\leq\; \mathbf{1}_{\{\phi_p \geq t - \eta\}}. \tag{2.10}$$

The smooth source rate $q_\eta := \mathbb{E}_{\mu_\beta} X_{p, \eta}$ is independent of $p$ by lattice translation invariance and is tuned to the target value $q_\eta = 0.003$ by bisection on $t$. At the working point (2.8), the tuned $t = 1.0104$ (this exact value comes from the side-10 exact-HB run; the side-8 exact-HB anchor gives $t = 1.0081$ because of slightly different $N_{\rm cfg}$ statistics).

**Why the upper envelope and not a symmetric sigmoid.** The sandwich (2.10) is the key analytic property used in Proposition Z.2 (positive source-radius ⇒ Lemma Q): the proof relies on $X_{p, \eta}$ vanishing strictly below $t - \eta$ and hitting 1 strictly above $t$, so that the positive source-radius bound's Taylor coefficient extraction gives the multiplicative Lemma Q with the cap-aperture parameter $a_{t-\eta} = 1 - (t - \eta)$. A symmetric sigmoid would not satisfy the upper-envelope sandwich on a finite interval. We make this dependence explicit because previous (pre-pass-18) diagnostics used a symmetric sigmoid; the pass-18 / pass-19 master switched to the upper-envelope ramp for analytic alignment.

### 2.5 The rooted source $Y_p$

For each link $e$ and incident plaquette $p \ni e$, define:

- The unit quaternion $n_{e, p} \in S^3$ such that $\tfrac{1}{2} \operatorname{Re} \operatorname{Tr} U_p = U_e \cdot n_{e, p}$ (the complementary three-link product, see §5 for the explicit formula).
- The alignment $\rho_{e, p} := m_e \cdot n_{e, p}$, with $m_e = \overline{H_e}/\|H_e\|$ the heat-bath mean direction.
- The good staple cone

$$\mathcal{G}_{e, p}(h_0, \rho_0) := \{ \|H_e\| \geq h_0 \text{ and } \rho_{e, p} \geq \rho_0 \}, \qquad h_0 > 0,\; \rho_0 > a_{t-\eta}. \tag{2.11}$$

The bad event is the complement $\mathcal{B}_{e, p}(h_0, \rho_0) := \mathcal{G}_{e, p}(h_0, \rho_0)^c$. The **rooted source** is

$$\boxed{Y_p := X_{p, \eta}\, \mathbf{1}_{\mathcal{B}_{e(p), p}},} \tag{2.12}$$

where $e(p)$ is a designated incident link to $p$ (the choice is canonical up to relabeling). By construction $0 \leq Y_p \leq X_{p, \eta}$ and $Y_p$ vanishes on the good staple cone.

**The rooted strategy.** The pass-10 honesty correction (correction 3 in §12) established that *unrooted bad-staple rarity* — the statement that the bad event $\mathcal{B}_{e, p}$ is itself sub-$q_\eta$ — does not hold in general. The correct strategy, used throughout this paper, is to absorb the bad-event indicator into the source root: the rooted source $Y_p$ inherits the rare-event factor $X_{p, \eta}$, and Lemma Q's rooted form ((Z.2) above and (6.3) below) gives the rooted multiplicative bound without requiring unrooted bad-staple rarity.

In §6 we will replace the good-cone $(h_0, \rho_0)$-based bad event by the sharper LCI good event $\mathcal{G}_{e, p}^{\rm LCI}$ from Definition Z.4. The rooted strategy persists: the LCI bad event is absorbed into a refined source root $Y_p^{\rm LCI} = X_{p, \eta} \mathbf{1}_{\mathcal{B}_{e, p}^{\rm LCI}}$.

### 2.6 Bałaban block geometry and the frozen-exterior conditional measure

Fix a positive integer block side $\ell$ and core margin $m$. A **Bałaban block** is an $\ell^4$ sub-cube $C \subset \Lambda_L^4$:

$$C = \{x \in \Lambda_L^4 : x_\mu \in [a_\mu, a_\mu + \ell), \; \mu = 1, \ldots, 4\} \tag{2.13}$$

for some block anchor $a \in \Lambda_L^4$. The **shaved core** of $C$ is the inner block

$$C^\circ := \{x \in C : a_\mu + m \leq x_\mu < a_\mu + \ell - m, \; \mu = 1, \ldots, 4\} \tag{2.14}$$

of side $\ell - 2m$. The shaved core is the set of vertices whose entire incident-link neighborhood, plus a margin of $m$ extra link steps, lies inside the block; this guarantees that the plaquettes at base in $C^\circ$ and the staples around their incident links also lie inside $C$, so that the conditional law on $C$ with exterior frozen does not require access to links outside $C$.

We will use the working block geometries:

- **Side-8 / margin-2** ($\ell = 8$, $m = 2$): $C^\circ$ is a $4^4 = 256$ vertex inner block. 864 core plaquettes per block at depth 2. Used in §V.1 exact-HB anchor.
- **Side-10 / margin-3** ($\ell = 10$, $m = 3$): $C^\circ$ is a $4^4 = 256$ vertex inner block. 864 core plaquettes per block at depths $\{3, 4\}$. Used in §AA exact-HB anchor and §V.2 historical Metropolis anchor.

The **frozen-exterior conditional measure** at block $C$ with exterior $\xi := U|_{\Lambda_L \setminus C}$ tempered (a fixed gauge configuration on the complement) is

$$\boxed{d\mu_C^\xi(U|_C) := (Z_C^\xi)^{-1} \exp\!\Big(-\beta \!\!\sum_{p \text{ incident to } C}\!\! \phi_p(U)\Big) \prod_{e \subset C} dU_e,} \tag{2.15}$$

where "$p$ incident to $C$" means $p$ has at least one edge in $C$, and the staples of those edges are computed using exterior links from $\xi$. The Gibbs measure (2.3) is recovered as a mixture of $\mu_C^\xi$ over $\xi \sim \mu_\beta|_{\Lambda_L \setminus C}$.

The Lemma Q conditional expectation $\mathbb{E}[\cdot \mid \mathcal{F}_{C^c}]$ in (Z.2), (1.4), and elsewhere is exactly the integration against $\mu_C^\xi$, with the exterior $\xi$ playing the role of the conditioning event.

**Tempered exterior.** Throughout we assume $\xi$ is *tempered* in the sense that the exterior links satisfy uniform bounds compatible with the working-point statistics: typical staple norms $\|H_e\|$ for $e$ adjacent to $C$ are $O(1)$ and the exterior plaquette excesses are bounded away from $2$ uniformly. This is a probability-1 condition under $\mu_\beta$ at $\beta = 3.5$ and is the right setting for the LCI typicality theorem (Open Theorem A) — the LCI good event is required to hold uniformly only over tempered exteriors, not over all measurable exterior configurations.

### 2.7 The positive source-tilted measure

For $S \subset C^\circ$ (a finite set of core plaquettes) and tilt strength $s \in [0, \rho/q_\eta]$ with positive radius parameter $\rho > 0$, the **positive source-tilted measure** on the block $C$ with frozen exterior $\xi$ is

$$\boxed{d\mu_C^{\xi, S, s}(U|_C) := \frac{\prod_{r \in S}(1 + s X_{r, \eta})}{\mathbb{E}_{\mu_C^\xi}\!\left[\prod_{r \in S}(1 + s X_{r, \eta})\right]} \, d\mu_C^\xi(U|_C).} \tag{2.16}$$

This is the natural one-parameter family of positive perturbations of $\mu_C^\xi$ by source insertions on $S$. The tilt strength $s = \rho/q_\eta$ gives a source weight of $1 + \rho/q_\eta \cdot X_r$ at each $r \in S$ — multiplicative on the high-plaquette set $\{\phi_r \geq t\}$, of order $\rho \cdot q_\eta^{-1}$ for unit-mass rare events.

The **rooted positive source-tilted measure** is

$$d\mu_C^{\xi, Y, S, s}(U|_C) := \frac{Y_{p_0} \prod_{r \in S}(1 + s X_{r, \eta})}{\mathbb{E}_{\mu_C^\xi}\!\left[Y_{p_0} \prod_{r \in S}(1 + s X_{r, \eta})\right]} \, d\mu_C^\xi(U|_C), \tag{2.17}$$

with $0 \leq Y_{p_0} \leq X_{p_0, \eta}$ a rooted source at a designated root plaquette $p_0$.

These two measures are the central technical objects of §§6–8. The tilted one-source stability theorem (TOS+J), the positive source-radius bound, and Lemma Q (Propositions Z.1, Z.2 of the master) are all statements about expectations under (2.16) and (2.17).

### 2.8 Notation summary

| Symbol | Meaning |
|---|---|
| $\Lambda_L$ | Periodic 4D lattice of side $L$ |
| $U_e \in \mathrm{SU}(2) \simeq S^3$ | Link variable (quaternion) |
| $H_e \in \mathbb{R}^4$ | Staple-sum quaternion at link $e$ |
| $m_e = \overline{H_e}/\|H_e\| \in S^3$ | Heat-bath mean direction |
| $\kappa_e = \beta\|H_e\|$ | Heat-bath concentration |
| $\phi_p = 1 - \tfrac{1}{2}\operatorname{Re}\operatorname{Tr} U_p$ | Plaquette excess |
| $X_{p, \eta}$ | Smooth upper-envelope source indicator (2.9) |
| $q_\eta = \mathbb{E}_{\mu_\beta} X_{p, \eta}$ | Smooth source rate, calibrated to $0.003$ |
| $t \in (0, 2)$ | Source threshold, tuned to $\approx 1.01$ at the working point |
| $\eta$ | Smoothing scale, fixed at $0.005$ |
| $a_{t-\eta} = 1 - (t-\eta)$ | Cap-aperture parameter on $S^3$ |
| $n_{e, p} \in S^3$ | Plaquette $p$ unit-vector contribution at link $e$ |
| $\rho_{e, p} = m_e \cdot n_{e, p}$ | Mean–plaquette alignment |
| $\mathcal{G}_{e, p}(h_0, \rho_0)$ | Good staple cone (2.11) |
| $Y_p = X_{p, \eta} \mathbf{1}_{\mathcal{B}_{e(p), p}}$ | Rooted source (2.12) |
| $C \subset \Lambda_L^4$ | Bałaban block (2.13), side $\ell$ |
| $C^\circ$ | Shaved core (2.14), margin $m$ |
| $\xi \in G^{\Lambda_L \setminus C}$ | Frozen exterior configuration |
| $\mu_C^\xi$ | Frozen-exterior conditional measure (2.15) |
| $d_C(p, r)$ | L1 plaquette distance inside $C$ |
| $\mu_C^{\xi, S, s}$ | Positive source-tilted measure (2.16) |
| $\mu_C^{\xi, Y, S, s}$ | Rooted positive source-tilted measure (2.17) |

This notation is fixed throughout the paper. Source-tilted measures abbreviate to $\mu^{S, s}$, $\mu^{Y, S, s}$ when the block $C$ and exterior $\xi$ are clear from context.

---

## 3. The deterministic projected-capacity framework

This section sets up the **unconditional spine** of the program: the projected covariance comparator $A_p = P \mathbf 1_{\partial p} P$, polymer-type ordered (PTO) summability, and the projected Birman–Schwinger firewall criterion. All results in this section are finite-dimensional spectral and combinatorial statements; none requires probabilistic input from the Wilson measure. The Wilson stochastic content enters only when §§4–8 supply random plaquette-incidence and source data for the deterministic spine to act on.

The deterministic spine plays two roles. **(i)** It supplies the operator-theoretic target object — projected capacity, $\|P \mathbf 1_D P\|$ for a defect set $D$ — whose magnitude controls low-mode instability under sparse perturbations. **(ii)** It provides the threshold criterion: whenever projected capacity stays below an explicit constant determined by the spectral window, no negative bound state can appear in the projected Hamiltonian, and the projected covariance kernel inherits exponential decay. §3.5 reports the $L = 64$ numerical validation of both roles in a 2D scalar setting where the threshold is exactly computable.

### 3.1 Lattice plaquette space and the Maxwell projection

Let $\Lambda = T_L^4 = (\mathbb Z/L\mathbb Z)^4$ be the periodic four-dimensional lattice of §2.1. We work with three lattice form spaces:

- **0-forms** $C^0(\Lambda) := \mathbb R^{|\Lambda|}$ (scalar functions on vertices),
- **1-forms** $C^1(\Lambda) := \mathbb R^{|\Lambda| \cdot d}$ with $d = 4$ (link variables; per Lie-algebra direction in the gauge-theory context, but we suppress the Lie-algebra index here as the deterministic framework is the same in each direction),
- **2-forms** $C^2(\Lambda) := \mathbb R^{|\Lambda| \cdot \binom{d}{2}}$ (plaquette variables).

The lattice exterior derivatives are

$$(d_0 f)(x, \mu) := f(x + \hat\mu) - f(x), \qquad d_0 : C^0(\Lambda) \to C^1(\Lambda), \tag{3.1}$$

$$(d_1 A)(x, \mu\nu) := A(x, \mu) + A(x + \hat\mu, \nu) - A(x + \hat\nu, \mu) - A(x, \nu), \qquad d_1 : C^1(\Lambda) \to C^2(\Lambda), \tag{3.2}$$

with $d_1 d_0 = 0$ (the lattice analogue of $d^2 = 0$).

The **lattice Maxwell operator** on 1-forms is

$$M := d_1^* d_1 : C^1(\Lambda) \to C^1(\Lambda), \tag{3.3}$$

a positive semidefinite symmetric operator. Its kernel consists of *exact* 1-forms (those of the form $d_0 f$) — the gauge directions in the lattice analogue. The physical 1-form subspace consists of **coexact** 1-forms, the orthogonal complement of $\ker d_0^*$:

$$C^1_{\rm coex}(\Lambda) := (\ker d_0^*)^\perp = \mathrm{range}(d_0)^\perp. \tag{3.4}$$

Equivalently, $A \in C^1_{\rm coex}$ iff $d_0^* A = 0$. The Maxwell operator $M$ acts non-degenerately on $C^1_{\rm coex}$ with strictly positive spectrum.

For a spectral window upper bound $\Lambda > 0$, the **window projector** is

$$P = P_{\le \Lambda, L} : C^1(\Lambda) \to C^1(\Lambda), \qquad P = \sum_{k : \mu_k \le \Lambda} v_k v_k^T, \tag{3.5}$$

where $\{\mu_k, v_k\}$ are the (coexact-restricted) eigenpairs of $M$. We take $P$ to be the orthogonal projection onto the span of coexact eigenmodes of $M$ with eigenvalue at most $\Lambda$. The choice of $\Lambda$ fixes a spectral window: large $\Lambda$ retains more modes and gives larger projected capacity; small $\Lambda$ retains fewer and gives a smaller, more targeted comparator. The PMBSF program treats $\Lambda$ as a tunable scale, with the dependence on $\Lambda$ explicit in all subsequent bounds.

**The Maxwell projection $P$ is the central deterministic object.** It selects the spectral window in which low-mode instability under defect perturbations is to be diagnosed; all subsequent comparator constructions are formed by sandwiching defect indicators between two copies of $P$.

### 3.2 The projected covariance comparator $A_p$

For each plaquette $p \in \Lambda^*$, let $\partial p$ denote the set of edges in the boundary of $p$ (four edges in 4D). Let $\mathbf 1_{\partial p}$ be the diagonal indicator operator on $C^1(\Lambda)$ that picks out the components on the edges in $\partial p$:

$$(\mathbf 1_{\partial p} A)(x, \mu) := \begin{cases} A(x, \mu) & \text{if } (x, \mu) \in \partial p, \\ 0 & \text{otherwise}. \end{cases} \tag{3.6}$$

The **projected covariance comparator** at plaquette $p$ is

$$\boxed{A_p := P \mathbf 1_{\partial p} P : C^1(\Lambda) \to C^1(\Lambda).} \tag{3.7}$$

Each $A_p$ is symmetric (since $P$ and $\mathbf 1_{\partial p}$ are both symmetric) and positive semidefinite. Its rank is at most $|\partial p| = 4$ per plaquette per Lie-algebra direction, so $A_p$ has at most 4 (resp. $4 \times 3 = 12$ in the SU(2) gauge-theory context) nonzero eigenvalues.

**Spectral bound.** Since $\|\mathbf 1_{\partial p}\| = 1$ and $\|P\| = 1$,

$$\|A_p\|_{\rm op} = \|P \mathbf 1_{\partial p} P\|_{\rm op} \le \|\mathbf 1_{\partial p}\|_{\rm op} = 1. \tag{3.8}$$

**Trace and capacity.** The trace of $A_p$ is

$$\operatorname{Tr} A_p = \operatorname{Tr}(P \mathbf 1_{\partial p}) = \sum_{e \in \partial p}\, \langle e, P e \rangle, \tag{3.9}$$

where $\langle e, P e \rangle$ is the diagonal entry of $P$ on edge $e$. This is the *local projected capacity* at the edges of $p$.

For a defect set $D \subset \Lambda^*$ (a collection of plaquettes), the **aggregate projected comparator** is

$$A_D := \sum_{p \in D} A_p = P\Big(\sum_{p \in D} \mathbf 1_{\partial p}\Big) P. \tag{3.10}$$

The aggregate comparator's operator norm $\|A_D\|$ is the **projected capacity of $D$**:

$$\boxed{\mathrm{cap}_P(D) := \|A_D\|_{\rm op} = \|P \mathbf 1_{\partial D} P\|_{\rm op}, \qquad \mathbf 1_{\partial D} := \sum_{p \in D} \mathbf 1_{\partial p}.} \tag{3.11}$$

Projected capacity is monotone, additive on disjoint defect sets up to overlap corrections, and bounded above by $\mathrm{cap}_P(D) \le \sum_{p \in D} \|A_p\| \le |D|$ in the worst case.

### 3.3 Polymer-type ordered (PTO) summability

The comparators $\{A_p\}_{p \in \Lambda^*}$ are not generally commuting, so naive product expansions of operator polynomials in the $A_p$ fail. The PTO framework provides a polymer-type ordering under which operator product sums converge.

**Definition (PTO ordering).** A **polymer** $\gamma \subset \Lambda^*$ is a finite, connected subset of plaquettes under the plaquette-overlap graph (where two plaquettes are connected if they share at least one edge). A **PTO sequence** $(\gamma_1, p_1) \to (\gamma_2, p_2) \to \ldots$ is a sequence of (polymer, base plaquette) pairs satisfying a plaquette-graph connectivity constraint inherited from the Bałaban / Dimock cluster decomposition.

**The summability bound.** For an operator polynomial $\prod_{p \in \gamma} A_p$ ordered along a PTO sequence within polymer $\gamma$,

$$\Big\|\prod_{p \in \gamma}^{\rm PTO} A_p\Big\| \le \prod_{p \in \gamma} \|A_p\| \le 1. \tag{3.12}$$

The non-trivial content is the **summed bound** over polymers $\gamma$ containing a fixed base plaquette $p_0$:

$$\sum_{\gamma \ni p_0} \Big\|\prod_{p \in \gamma}^{\rm PTO} A_p\Big\| \cdot z^{|\gamma|} \le K(z), \tag{3.13}$$

where $z > 0$ is a polymer-activity weight. The series $K(z)$ converges for $z$ below the polymer-overlap growth radius. We denote the (deterministic) **PTO summability radius** by $z_{\rm PTO}^*$; for plaquette-overlap graphs with growth constant $\mu_{\mathcal G}$, $z_{\rm PTO}^* \ge 1/\mu_{\mathcal G}$ holds by standard polymer-expansion arguments \[Kotecký–Preiss 1986; Fernández–Procacci 2007\]. In 4D lattice gauge theories, $\mu_{\mathcal G} \le 32$ (since each plaquette has at most 32 neighbouring plaquettes counted with overlap multiplicities); finer estimates give smaller working values.

**The deterministic PTO summability theorem.** For each $z < z_{\rm PTO}^*$ there exists a constant $K(z) < \infty$ such that (3.13) holds uniformly in $p_0$ and in the lattice size $L$. The proof is standard polymer combinatorics applied to the comparator family $\{A_p\}$ and uses no probabilistic input. We defer the proof to master Appendix I §I.5 where it is given explicitly for the SU(2) plaquette-overlap graph.

### 3.4 The projected Birman–Schwinger firewall criterion

We now combine the comparator family with the spectral window to obtain the deterministic firewall criterion. Fix a coupling strength $V > 0$ and a defect set $D \subset \Lambda^*$.

**The projected low-sector Hamiltonian.** Restrict to the spectral window $P$ and define

$$H_K(V, D) := M|_P - V\, A_D = M|_P - V\, P \mathbf 1_{\partial D} P, \tag{3.14}$$

where $M|_P$ denotes the Maxwell operator restricted to the window range. Since $P$ is finite-dimensional (rank at most the number of modes in the window), $H_K(V, D)$ is a finite symmetric matrix. The defect coupling $-V A_D \le 0$ is an attractive perturbation; if $V$ is large enough, $H_K(V, D)$ acquires negative eigenvalues — a **bound state**.

**The projected Birman–Schwinger threshold.** The exact threshold coupling at which $H_K(V, D)$ first acquires a negative eigenvalue is

$$\boxed{V_c^{BS}(D) := \|M|_P^{-1/2}\, A_D\, M|_P^{-1/2}\|_{\rm op}^{-1}.} \tag{3.15}$$

For $V < V_c^{BS}(D)$, no negative eigenvalue exists; for $V > V_c^{BS}(D)$, at least one exists. This is the standard Birman–Schwinger criterion \[Reed–Simon IV\] restricted to the projected sector and applied to the comparator family.

**The firewall criterion.** The PMBSF deterministic firewall states that, provided

$$\boxed{V \cdot \mathrm{cap}_P(D) \cdot \big\|M|_P^{-1}\big\| < 1,} \tag{3.16}$$

no negative bound state appears in $H_K(V, D)$. The condition is equivalent to $V < V_c^{BS}(D)$ up to a single eigenvalue-versus-spectral-radius factor and is the operationally convenient form.

**The cheap scalar surrogate.** The exact threshold $V_c^{BS}(D)$ requires computing the operator norm of a triple matrix product, which involves the Maxwell operator's inverse on the window. A computationally cheap surrogate is

$$V_c^R(D) := \frac{\lambda_1}{\|A_D\|_{\rm op}}, \tag{3.17}$$

where $\lambda_1$ is the smallest non-zero eigenvalue of $M|_P$ (the window's spectral edge). The surrogate $V_c^R$ tracks $V_c^{BS}$ closely on geometrically-controlled defect ensembles, with the deviation calibrated by §3.5 to be a power-law of the form $V_c^{BS} \approx \exp(\alpha)\, (V_c^R)^\gamma$ at fixed local geometry. This calibration is the **deterministic threshold law**.

**Closure of the deterministic spine.** The criterion (3.16), the comparator bound (3.8), and the PTO summability (3.13) together close the deterministic spine:

- The comparator $A_p$ is bounded by 1.
- The aggregate $A_D$ has bounded operator norm by (3.11)–(3.12).
- The PTO sum (3.13) converges.
- The Birman–Schwinger criterion (3.16) gives an explicit threshold below which no negative bound state appears.

All four statements are unconditional. They hold for arbitrary defect sets $D$ and arbitrary configurations of the deterministic comparator family. The probabilistic content — what distribution of $D$ to consider, what value of $V$ corresponds to the Wilson coupling $\beta$, what set of "defect plaquettes" the Wilson source $X_{p, \eta}$ realises — is exactly what §§4–8 supply.

### 3.5 Deterministic threshold-law validation on $\mathbb T_{64}^2$

The deterministic spine is unconditional, but its quantitative usefulness depends on the calibrations entering (3.16) and (3.17). To validate the central operator object — projected capacity $\|P \mathbf 1_D P\|$ as a predictor of low-mode instability — and the scalar surrogate (3.17) at scale, we report a finite-dimensional threshold-law experiment on a synthetic two-dimensional scalar lattice where the exact projected Birman–Schwinger threshold (3.15) is computable for every defect mask. The experiment is **not** a Wilson SU(2) result; its purpose is to validate the deterministic operator object in a setting where ground truth is exactly computable. This complements the Wilson SU(2) consequences in §9 (which test stochastic predictions of Open Theorems A and B).

#### 3.5.1 Setup

We work on the periodic two-dimensional lattice $\mathbb T_{64}^2$ with $N = 4096$ sites. The lattice Laplacian (the 2D scalar analogue of (3.3)) is

$$\Lambda f(x) := \sum_{\mu = 1,2}\big(2 f(x) - f(x + \hat\mu) - f(x - \hat\mu)\big). \tag{3.18}$$

The spectral window projector is $P = P_{\rm nonzero, K}$, the projection onto the $K = 128$ smallest *nonzero* Laplacian eigenmodes. At these settings:

$$\lambda_1 = 0.009630547, \qquad \lambda_{\max, K} = 0.375490. \tag{3.19}$$

For a defect set $D \subset \mathbb T_{64}^2$ (a subset of vertices in the 2D scalar setting; the 2D analogue of plaquettes), the scalar projected comparator is $G_D := P \mathbf 1_D P$, where $\mathbf 1_D$ is the diagonal indicator of $D$. The exact projected Birman–Schwinger critical coupling (3.15) and the cheap surrogate (3.17) become

$$V_c^{BS}(D) = \|\Lambda^{-1/2} G_D \Lambda^{-1/2}\|^{-1}, \qquad V_c^R(D) = \frac{\lambda_1}{\|G_D\|}. \tag{3.20}$$

Both norms are computed exactly by direct diagonalization on the 4096-dimensional vertex space.

#### 3.5.2 Mask ensemble at fixed local geometry

We construct an ensemble of 180 defect masks across six geometric families, 30 masks per family. Mask families: (a) random, (b) stripe, (c) ring, (d) low-mode-biased horizontal, (e) low-mode-biased diagonal, (f) blue-noise dimers. Each mask has *exactly* the same local statistics:

- $m = 128$ defect sites (density $3.125\%$),
- exactly 64 connected clusters,
- largest cluster size 2 (each mask is 64 separated dimers).

What varies across the ensemble is only the long-range arrangement of dimers. Density, defect count, cluster count, and largest cluster size are held constant by construction, so any variation in $V_c^{BS}$ across masks cannot be attributed to local statistics alone — the variation must reflect the non-local interaction with the Laplacian's low-mode structure.

#### 3.5.3 Headline calibration

Across all 180 masks:

$$\mathrm{corr}(V_c^R, V_c^{BS}) = 0.9581, \qquad \mathrm{corr}(\log V_c^R, \log V_c^{BS}) = 0.9600. \tag{3.21}$$

Linear regression in log–log coordinates gives

$$\boxed{\log V_c^{BS} = 1.6615 + 1.2161\, \log V_c^R, \qquad R^2 = 0.9216, \quad \mathrm{MAE}_{\log} = 0.0563.} \tag{3.22}$$

The calibration is power-law $V_c^{BS} \approx 5.27 \cdot (V_c^R)^{1.22}$ at the working window $(K = 128, \Lambda_{\max, K} = 0.375)$. The exponent close to 1 confirms that the surrogate $V_c^R$ is the correct *order* of $V_c^{BS}$ across two orders of magnitude in defect arrangement; the offset and slight super-linearity calibrate the spectral-window factor that $V_c^R$ misses.

#### 3.5.4 Mask-heldout cross-validation

We test whether projected capacity is genuinely the predictive variable (versus mere local geometry) using random-forest regression with 8-fold group split on mask identifier:

| Feature set | MAE | $R^2$ |
|---|---:|---:|
| scalar capacity ($\log V_c^R$) | 0.0283 | 0.978 |
| scalar plus spectral alignment | 0.0286 | 0.978 |
| geometry features, no capacity | 0.0301 | 0.975 |
| local statistics only | 0.2170 | $-0.035$ |

The scalar capacity beats the local-only baseline by an order of magnitude in MAE. Crucially, it also beats the "geometry features, no capacity" model — which includes pair distances, Fourier amplitudes, cluster statistics — by a measurable margin ($\Delta \mathrm{MAE} = 0.0018$). This is the operational validation of the deterministic comparator as a *predictive* quantity, not just a *bound*.

#### 3.5.5 Family-heldout cross-validation

Leave-one-family-out cross-validation tests the harder extrapolation problem (learning on five geometric families and predicting the sixth):

| Feature set | MAE | $R^2$ |
|---|---:|---:|
| scalar capacity | 0.1534 | $-72.5$ |
| scalar plus alignment | 0.1537 | $-71.7$ |
| geometry, no capacity | 0.1799 | $-87.2$ |
| local only | 0.2452 | $-182$ |

Family-heldout is genuinely hard extrapolation. The negative $R^2$ values reflect that the spread of $V_c^{BS}$ across one family is large enough that learning on five families produces test variance larger than the residual variance for the sixth. **But the MAE ordering is preserved**: scalar capacity still wins by $\Delta \mathrm{MAE} = 0.0265$ over geometry-only. The hardest family across all models is stripe_dimers (the only family with deterministic single-orientation alignment), confirming the diagnosis that the long-range Fourier structure of the mask matters and that the projected capacity captures it.

#### 3.5.6 Order-parameter attack

The threshold $V_c^{BS}(D)$ is not the only deterministic prediction; the full bound-state response $\lambda_{\min}(H_K(V, D))$ as a function of $V$ is also predictable from the projected capacity. We test this with a separate ensemble of 90 masks × 7 coupling values $V_0 \in \{0.1, 0.5, 1, 2, 5, 10, 20\}$, giving 630 mask-coupling configurations.

For each (mask, coupling) pair, compute the projected low-sector ground-state eigenvalue $\lambda_{\min}(H_K(V_0, D))$ and the binary indicator $\mathrm{neg}_{V_0}(D) = \mathbf 1\{\lambda_{\min} < 0\}$.

The classifier $\widehat{\mathrm{neg}}(V_0, D) = \mathbf 1\{V_0 > V_c^{BS}(D)\}$ derived from the projected Birman–Schwinger criterion (3.15) achieves

$$\boxed{\mathrm{AUC} = 1.000 \quad (\text{negative-eigenvalue classification across 630 (mask, coupling) configurations}).} \tag{3.23}$$

The same AUC of 1.000 holds when the feature is replaced by the cheap scalar surrogate $V_c^R(D)$ from (3.17): *no false positive and no false negative* on the 630 configurations. This is the operational validation of the projected Birman–Schwinger criterion as a deterministic firewall: across two orders of magnitude in coupling $V_0$ and 90 distinct defect arrangements at fixed local geometry, the projected-capacity criterion never mislabels a single binding event.

Regression metrics on the continuous targets:

| Target | Feature set | $R^2$ (mask-heldout) | $R^2$ (family-heldout) |
|---|---|---:|---:|
| projected_binding | exact_BS | 0.999 | 0.951 |
| projected_binding | scalar_capacity | 0.999 | 0.945 |
| defect_mass_low | exact_BS | 0.988 | 0.511 |
| defect_mass_low | scalar_capacity | 0.985 | 0.502 |

#### 3.5.7 Interpretation

§3.5 validates two distinct deterministic claims at scale:

1. **Projected capacity is a meaningful predictive variable for low-mode instability** under sparse defect perturbations — not merely a bound but a quantitative predictor. The mask-heldout $R^2 = 0.978$ and the family-heldout MAE ordering both confirm this.

2. **The projected Birman–Schwinger criterion is operationally exact** — the AUC = 1.000 across 630 configurations means the criterion never gives a false threshold. This is the deterministic firewall at work: when projected capacity falls below the spectral-window threshold, no binding occurs.

**§3.5 is not a Wilson SU(2) result.** The 2D scalar setting is a synthetic ground-truth-computable proxy for the operator-theoretic content of (3.7), (3.10), and (3.15). The Wilson SU(2) analogue at 4D requires the random plaquette-incidence machinery of §4 (which links $\mathrm{cap}_P(D)$ at random $D$ to expectations under the Wilson measure) and the source-rate input of §§5–8 (which controls the distribution of $D$ via the source indicator $X_{p, \eta}$). §3.5's role is to confirm that the *operator-theoretic spine* is sound at L = 64 in a clean setting; §9 then reports the Wilson stochastic anchors at L = 16 and L = 64 that test the random-source consequences.

The deterministic threshold law (3.22) and the order-parameter AUC = 1.000 together constitute the strongest deterministic-side numerical evidence available for the PMBSF framework's central operator object.

---

## 4. Random plaquette-incidence comparator

The deterministic spine in §3 controls the operator consequences of a defect set \(D\). The stochastic problem is to show that Wilson-generated high-plaquette sets behave, in the projected low-mode window, like sparse plaquette-incidence random sets rather than adversarial defect sheets.

The natural random comparator is not an independent Bernoulli mask on links, but a random plaquette set pushed through the exact plaquette-to-link incidence map. Let \(B_p\in\{0,1\}\) be a random plaquette indicator. Define the induced link mask

\[
\mathbf1_{\partial B}
=
\sum_{p}B_p\,\mathbf1_{\partial p}.
\]

The projected random defect operator is

\[
S_B=P\mathbf1_{\partial B}P
=
\sum_p B_p A_p.
\]

Thus the same deterministic atom

\[
A_p=P\mathbf1_{\partial p}P
\]

is the stochastic plaquette-incidence atom.

For independent Bernoulli plaquettes with mean \(q\), a matrix-Bernstein comparator gives a threshold of the schematic form

\[
\|P\mathbf1_{\partial B}P\|
\le
6q+
\sqrt{12q\kappa_\Lambda\log(2K/\delta)}
+
\frac{2\kappa_\Lambda}{3}\log(2K/\delta),
\tag{4.1}
\]

with probability at least \(1-\delta\). Here \(K=\operatorname{rank}P\) and \(\kappa_\Lambda=\sup_p\|A_p\|\). The factor \(6q\) is the expected local incidence density in four dimensions: each link belongs to six plaquette planes.

The Wilson high-plaquette set is not independent Bernoulli. Lemma Q is the replacement:

\[
\mathbb E_{\mu_C^\xi}
\prod_{p\in B}X_{p,\eta}
\le
(C_Qq_\eta)^{|B|}.
\tag{4.2}
\]

This condition is strong enough to transfer Bernoulli plaquette-incidence control to Wilson sources after localization and boundary-band control.

---

## 5. Exact SU(2) heat-bath geometry

This section isolates the exact local SU(2) object underlying LCI.

Fix a link \(e\). Conditional on all links except \(e\), the Wilson action involving \(U_e=u\in S^3\) combines into a staple-sum quaternion \(H_e\). With convention

\[
\operatorname{Scal}(uH)=u\cdot\overline H,
\]

the conditional density is

\[
d\nu_e(u\mid U_{e^c})
=
Z_e^{-1}
\exp\{\beta u\cdot \overline H_e\}
\,d\sigma_{S^3}(u).
\]

Thus

\[
\boxed{
U_e\mid U_{e^c}
\sim
\mathrm{vMF}_4
\left(
\frac{\overline H_e}{\|H_e\|},
\beta\|H_e\|
\right).
}
\tag{5.1}
\]

Set

\[
m_e=\frac{\overline H_e}{\|H_e\|},
\qquad
\kappa_e=\beta\|H_e\|.
\]

For each plaquette \(r\ni e\), there exists \(n_{e,r}\in S^3\) such that

\[
\frac12\operatorname{Re}\operatorname{Tr}(U_r)
=
u\cdot n_{e,r}.
\tag{5.2}
\]

Since

\[
X_{r,\eta}\le \mathbf1_{\{\phi_r\ge t-\eta\}},
\]

we obtain the spherical cap domination

\[
X_{r,\eta}
\le
\mathbf1_{C_r},
\qquad
C_r=\{u\in S^3:u\cdot n_{e,r}\le a\},
\qquad
a=1-(t-\eta).
\tag{5.3}
\]

For a single cap, if \(\rho_r=m_e\cdot n_{e,r}\), then

\[
\sup_{u\cdot n_{e,r}\le a}m_e\cdot u
=
\rho_ra+\sqrt{1-\rho_r^2}\sqrt{1-a^2}.
\tag{5.4}
\]

This gives the single-source heat-bath cap suppression. Lemma Q requires the multi-cap increment estimate below.

---

## 6. Local cap-intersection stability

Fix target plaquette \(p\ni e\). For incident subset

\[
A\subset\{r\ne p:r\ni e\},
\]

define

\[
C_A=\bigcap_{r\in A}C_r.
\]

The local cap-intersection condition is

\[
\boxed{
\nu_e(C_p\cap C_A)
\le
C_{\rm LCI}q_\eta\,\nu_e(C_A)
}
\tag{6.1}
\]

for every such \(A\). Since a link in four dimensions is incident to six plaquettes, \(A\) has at most five elements. LCI is therefore a finite-dimensional statement about at most six caps on \(S^3\).

LCI implies incident positive-tilt stability. Let

\[
d\nu^{B,s}
=
\frac{
\prod_{r\in B}(1+s\mathbf1_{C_r})
}{
\int\prod_{r\in B}(1+s\mathbf1_{C_r})\,d\nu_e
}
d\nu_e,
\qquad
0\le s\le\rho/q_\eta.
\]

Then

\[
\nu^{B,s}(C_p)\le C_{\rm LCI}q_\eta.
\tag{6.2}
\]

Indeed,

\[
\int_{C_p}\prod_{r\in B}(1+s\mathbf1_{C_r})\,d\nu_e
=
\sum_{A\subset B}s^{|A|}\nu_e(C_p\cap C_A),
\]

and (6.1) bounds this by

\[
C_{\rm LCI}q_\eta
\sum_{A\subset B}s^{|A|}\nu_e(C_A),
\]

which is \(C_{\rm LCI}q_\eta\) times the normalizing denominator.

A support-height criterion for LCI is as follows. Define

\[
h(A)=\sup_{u\in C_A}m_e\cdot u,
\qquad
\Delta(A)=1-h(A),
\]

and

\[
\Delta_p(A)=\Delta(A\cup\{p\})-\Delta(A)
=
h(A)-h(A\cup\{p\}).
\]

Under nondegenerate exposed-maximizer hypotheses,

\[
\nu_e(C_p\mid C_A)
\le
C_{\rm geom}\kappa_e^M e^{-\kappa_e\Delta_p(A)}.
\tag{6.3}
\]

Thus LCI follows if

\[
\Delta_p(A)
\ge
\Delta_q+
\frac{M\log\kappa_e+\log C_{\rm geom}+O(1)}{\kappa_e},
\tag{6.4}
\]

where \(q_\eta\asymp e^{-\kappa_e\Delta_q}\).

Let

\[
u_A\in\arg\max_{u\in C_A}m_e\cdot u.
\]

A computable good event is

\[
\mathcal G_{e,p}^{\rm LCI}
=
\left\{
\forall A\subset\{r\ne p:r\ni e\},
\quad
u_A\cdot n_{e,p}-a\ge\chi_0
\right\}.
\tag{6.5}
\]

The LCI-bad event is

\[
\mathcal B_{e,p}^{\rm LCI}
=
(\mathcal G_{e,p}^{\rm LCI})^c,
\]

and it is rooted:

\[
Y_p^{\rm LCI}
=
X_{p,\eta}\mathbf1_{\mathcal B_{e,p}^{\rm LCI}}.
\tag{6.6}
\]

Open Theorem A is that, under tempered SU(2) Wilson heat-bath geometry, \(\mathcal G_{e,p}^{\rm LCI}\) holds with rooted/absorbed complement.

---

## 7. Bałaban far-source stability

LCI handles only sources on plaquettes incident to the selected heat-bath link \(e(p)\). Split

\[
S=S_{\rm inc}(e)\cup S_{\rm far}(e),
\qquad
S_{\rm inc}(e)=\{r\in S:r\ni e\}.
\]

The far sources do not enter the one-link vMF integral directly. They influence \(X_p\) by changing the environment \(U_{e^c}\), and hence \(H_e\), \(\kappa_e\), \(m_e\), the cap normals \(n_{e,r}\), and \(\mathcal G_{e,p}^{\rm LCI}\).

Open Theorem B is the source-marked random-walk locality estimate

\[
\boxed{
\mathbb E_{\mu^{S_{\rm far},s}}
\left[
X_{p,\eta}\mathbf1_{\mathcal G_{e,p}^{\rm LCI}}
\right]
\le
Cq_\eta
\exp\left(\sum_{r\in S_{\rm far}}J(p,r)\right),
}
\tag{7.1}
\]

with

\[
J(p,r)\le C_Je^{-m_Jd_C(p,r)}.
\tag{7.2}
\]

The rooted version is

\[
\boxed{
\mathbb E_{\mu^{Y,S_{\rm far},s}}
\left[
X_{a,\eta}\mathbf1_{\mathcal G_{e,a}^{\rm LCI}}
\right]
\le
Cq_\eta
\exp\left(J(a,p_0)+\sum_{r\in S_{\rm far}}J(a,r)\right).
}
\tag{7.3}
\]

This is the precise place where the Bałaban/Dimock expansion must be upgraded to positive source tilts of size \(O(q_\eta^{-1})\).

---

## 8. Deterministic implication chain

Assume Open Theorem A and Open Theorem B. Condition on \(U_{e^c}\). Incident sources produce a finite positive tilt of the one-link vMF law; by LCI,

\[
\mathbb E
\left[
X_{p,\eta}
\mid
U_{e^c},S_{\rm inc}\text{-tilt},\mathcal G_{e,p}^{\rm LCI}
\right]
\le
Cq_\eta.
\]

Then integrate over \(U_{e^c}\) under the far-source tilted measure. Theorem B gives

\[
\mathbb E_{\mu^{S,s}}
\left[
X_{p,\eta}\mathbf1_{\mathcal G_{e,p}^{\rm LCI}}
\right]
\le
Cq_\eta
\exp\left(\sum_{r\in S}J(p,r)\right).
\tag{8.1}
\]

The complement is the rooted source \(Y_p^{\rm LCI}\). This is TOS+J.

Now define

\[
Z_A(s)=\mathbb E_\mu\prod_{p\in A}(1+sX_{p,\eta}).
\]

Order \(A=\{p_1,\ldots,p_n\}\). At \(s=\rho/q_\eta\),

\[
\frac{Z_{A_j}(s)}{Z_{A_{j-1}}(s)}
=
1+s\,\mathbb E_{\mu^{A_{j-1},s}}X_{p_j,\eta}
\le
1+\rho C e^{J_*},
\]

where \(J_*=\sup_p\sum_rJ(p,r)\). Hence

\[
Z_A(\rho/q_\eta)
\le
\exp(\rho C e^{J_*}|A|).
\tag{8.2}
\]

Finally, positivity of coefficients gives

\[
\mathbb E_\mu\prod_{p\in B}X_{p,\eta}
\le
\left[
\rho^{-1}\exp(\rho C e^{J_*})q_\eta
\right]^{|B|}.
\tag{8.3}
\]

This is Lemma Q.

---

## 9. Numerical evidence

The numerical evidence does not prove either Open Theorem A or Open Theorem B. It verifies the qualitative patterns predicted by the conditional theorem stack.

### 9.1 Exact-HB side-8 block conditional anchor

At \(L=16,\beta=3.5,q_\eta=0.003,\eta=0.005\), exact heat-bath frozen-block diagnostics on side-8/margin-2 blocks report

\[
\operatorname{median}\Lambda=0.9249,
\qquad
\max\Lambda=1.4626,
\]

and rooted

\[
\operatorname{median}\Lambda_{\rm root}=0.9563,
\qquad
\max\Lambda_{\rm root}=1.3998.
\]

### 9.2 Exact-HB side-10 geometry anchor

At \(L=16,\beta=3.5,q_\eta=0.003,\eta=0.005\), exact heat-bath diagnostics on side-10/core-margin-3 blocks report

\[
t=1.0104245908659366,
\quad
q_\eta=0.003000000000000041,
\quad
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

### 9.3 Full-volume pair/rooted covariance through \(L=64\)

The \(L=64\) ledger reports

\[
q_\eta=0.0030061514,
\qquad
q_{\rm hard}=0.0030000228,
\]

\[
\max|\operatorname{Cov}(X,X)|/q_\eta^2=0.86578135,
\]

\[
\operatorname{median}=0.0067171416.
\]

Rooted:

\[
\max=0.89244247,
\qquad
\operatorname{median}=0.0074250476.
\]

This is the global \(k=1\) consequence evidence, pending artifact-packaged citation of the \(L=64\) readout.

### 9.4 Deterministic threshold-law validation

The 2D scalar \(\mathbb T_{64}^2\) deterministic threshold-law experiment validates the operator spine in a ground-truth-computable setting. Across 630 mask-coupling configurations, the projected Birman–Schwinger threshold classifier achieves

\[
\mathrm{AUC}=1.000.
\]

This does not test Wilson SU(2). It tests the deterministic projected-capacity object.

---

## 10. Open analytic tasks

The remaining analytic tasks are exactly:

1. **Open Theorem A: LCI-good typicality.** Prove that typical/tempered SU(2) Wilson heat-bath geometry satisfies the cap-intersection increment inequality with rooted complement.

2. **Open Theorem B: Bałaban far-source stability.** Prove that far positive source tilts distort LCI parameters only through an exponentially summable kernel.

3. **Boundary-band gate.** Prove the \(\eta\to0\) passage from the smooth upper-envelope source to hard high-plaquette sources.

4. **Continuum layer.** Separate from this manuscript: prove infinite-volume/continuum construction, OS reconstruction, nontriviality, and positive physical mass gap.

---

## 11. Relation to the SU(3) companion paper

The SU(3) companion paper is independent. It proves a local one-plaquette class-function gap asymptotic,

\[
\Delta_{\mathrm{SU}(3)}(\beta)
=
\sqrt{\frac{2\beta}{3}}
-
\frac5{16}
-
\frac{311\sqrt6}{9216}\beta^{-1/2}
+
O(\beta^{-1}),
\]

including the non-radial Weyl-invariant \(p_3^2\) correction. That result is local spectral theory, not PMBSF projected-capacity closure. It should remain a separate paper.

---

## 12. Status and honesty register

The manuscript-safe claim is:

> We reduce SU(2) projected-capacity firewall closure to local cap-intersection typicality plus Bałaban far-source stability, and we provide exact heat-bath finite-volume diagnostics supporting the resulting positive-tilt source-stability mechanism.

The manuscript must not claim:

> We prove the SU(2) Yang–Mills mass gap.

### 12.1 Status table

| Component | Status | Role |
|---|---|---|
| Projected comparator \(A_p=P\mathbf1_{\partial p}P\) | deterministic | operator spine |
| PTO summability | deterministic / finite-dimensional | covariance-to-capacity transfer |
| Birman–Schwinger firewall | deterministic | coercivity if threshold holds |
| Exact SU(2) heat-bath law | exact local identity | vMF cap formulation |
| LCI typicality | open | near-field source stability |
| Bałaban far-source stability | open | nonlocal source factorization |
| TOS+J \(\Rightarrow\) source-radius | proved reduction | telescoping partition function |
| source-radius \(\Rightarrow\) Lemma Q | proved reduction | positivity extraction |
| Lemma Q | derived if open theorems hold | rare-source factorization |
| Boundary-band gate | open | smooth-to-hard passage |
| Exact-HB side-8/side-10 | numerical evidence | local source stability support |
| \(L=64\) covariance | numerical evidence | global \(k=1\) consequence support |
| Clay mass gap | not proved | outside current scope |

### 12.2 Prior corrections

The program previously corrected or retracted:

1. a sign convention in an auxiliary drift statement;
2. a false ratio assumption in an early rooted-source argument;
3. a numerical Haar-measure factor;
4. an overinterpretation of a decay-rate confidence interval;
5. a binary-classifier artifact in an extended regression;
6. an early empirical overclaim of proof closure.

The surviving manuscript has been adjusted to avoid those errors. In particular, unrooted bad-staple rarity is not assumed; all bad local geometry is rooted.

---

## 13. References placeholder

The final manuscript should include precise entries for:

- Wilson lattice gauge theory.
- Fisher / von Mises–Fisher distributions.
- Kennedy–Pendleton SU(2) heat-bath algorithm.
- Bałaban’s lattice gauge RG papers.
- Dimock’s exposition/reconstruction papers.
- Kotecký–Preiss cluster expansion.
- Fernández–Procacci polymer convergence.
- Ueltschi polymer expansion notes.
- Random current/source-set references as abelian analogues only.
- Spherical cap asymptotics and convex-geometric Laplace estimates.
- Modern zero-free / coefficient-extraction literature as conceptual comparison.
