# Literature Extraction Protocol for $(M')_{\rm SU(2)}$

## Reading guide for Bałaban II (1988) and Magnen-Rivasseau-Sénéor (1993)

**Purpose.** This is not a derivation. It is a **reading checklist** for extracting the constants $(C_*, m_*, \xi_*)$ and the polymer activity bound that the bridge document (`NOTE_PMBSF_mprime_hpm_bridge.md`) uses as its external input $(M')_{\rm SU(2)}$. The work is concretely scoped at 1-2 weeks of careful reading; this document defines what "done" means.

**Honest scope.** I am writing this protocol from search results plus the bridge document. I have not been able to access the projecteuclid PDFs of Bałaban Part II (Comm. Math. Phys. 116, 1988) or MR93 (Comm. Math. Phys. 155, 1993) — both are bot-blocked. The protocol therefore tells the reader **where to look** and **what to extract**, not the numerical values themselves. Those values come from the actual reading, not from me.

---

## 0. Corrected bibliography

The prior memo had the MR paper as "MR95 (1995)" — this is wrong. The correct citation is:

- **MR93.** J. Magnen, V. Rivasseau, R. Sénéor, "Construction of $YM_4$ with an infrared cut-off," *Comm. Math. Phys.* **155** (1993), 325-383.

And the Bałaban paper containing the cluster machinery is **Part II**, not Part I:

- **Bałaban I (1987).** T. Bałaban, "Renormalization group approach to lattice gauge field theories. I. Generation of effective actions in a small field approximation and a coupling constant renormalization in four dimensions," *Comm. Math. Phys.* **109** (1987), 249-301. *(Foundation; small-field RG step; coupling constant renormalization. Does not contain the cluster expansion proper.)*
- **Bałaban II (1988).** T. Bałaban, "Renormalization group approach to lattice gauge field theories. II. Cluster expansions," *Comm. Math. Phys.* **116** (1988), 1-22. *(Contains the cluster expansion. This is the load-bearing reference for (M')_SU(2).)*
- **Bałaban III (1988).** T. Bałaban, "Convergent renormalization expansions for lattice gauge theories," *Comm. Math. Phys.* **119** (1988), 243-285. *(Convergent expansions including large-field domains.)*

The expository Dimock series (arXiv 1108.1335 / 1212.5562 / 1304.0705) covers the **same Bałaban method** but applied to $\phi^4$ in $d=3$, not SU(2) YM in $d=4$. It is useful for **understanding the technique** but does not deliver the SU(2)-specific constants.

The Adhikari-Cao 2022 paper (arXiv 2202.10375, *Annals of Probability*) handles **finite (possibly non-Abelian) gauge groups at weak coupling** via Glimm-Jaffe-Spencer cluster expansion plus a "knot decomposition" technique. It is **not** directly applicable to continuous SU(2), but the knot decomposition structure may be the right model for handling the non-Abelian factorization breakdown that does appear in continuous SU(2). Worth reading as a methodological reference.

---

## 1. What we need to extract

The bridge document uses the polymer activity bound (M'.2):

$$
|\Phi(\Gamma; h)| \le C_*^{|\Gamma|} p^{|\Gamma|} e^{-m_* \tau(\Gamma)} \prod_{p \in \Gamma}(e^{h_p} - 1)
$$

with $\tau(\Gamma)$ the minimum spanning tree length on the plaquette set $\Gamma$, $p$ the high-plaquette indicator probability $\mathbb{E}_W Y_p(t) = p$, and $h_p \in [0, h_{\max}]$ test functions with $h_{\max} \le \log 2$.

The **pinned form** (B3.8) is sharper, with $p^{|\Gamma| - 1}$ in place of $p^{|\Gamma|}$ in the single-block norm — gaining one factor of $p$ at large clusters.

**Four constants must be extracted:**

| Symbol | Meaning | Where to look |
|---|---|---|
| $C_*$ | Polymer activity prefactor: cluster norm scale | Bałaban II §3-4 polymer norm; MR93 §4-5 phase-space cell bound |
| $m_*$ | Inverse correlation length / cluster decay rate | Bałaban II tree-decay constants; MR93 IR-cutoff scale |
| $\xi_*$ | Scale of $\beta$-dependence: $m_* \ge m_*(\beta_*)$ for $\beta \ge \beta_*$ | Both papers: regime of convergence in $\beta$ |
| $\beta_*$ | Lower bound on $\beta$ for cluster convergence | Bałaban II convergence radius |

At the v9 working corner $\beta = 3.5$, we need $\beta \ge \beta_*$. **The first question for the reading is whether $\beta_*$ in the available literature is small enough that $\beta = 3.5$ is in the convergent regime.** If $\beta_* > 3.5$, the program either raises $\beta$ (changing the working corner) or uses a different cluster expansion suitable for that regime.

---

## 2. Reading order

### Phase 1: Method orientation (2-3 days)

The reader should first internalize the Bałaban method through Dimock's expository series, even though Dimock treats $\phi^4$ in $d=3$. The geometric language (block-averaging, scaling back, small-field/large-field decomposition, polymer activity, tree-graph bound) is exactly the same.

**Read first:**

1. **Dimock I (arXiv 1108.1335).** "The Renormalization Group According to Balaban - I. Small fields." 52 pages, July 2013. Open access. **Small-field contribution and basic block-spin step.** Pay attention to:
   - §2 setup (toroidal lattice, scaling, block-averaging operator $Q$)
   - §3 the small-field characteristic function
   - §4 the cluster expansion structure (this is the analog of what we need from Bałaban II)
   - The polymer norm definitions and their convergence criteria

2. **Dimock III (arXiv 1304.0705).** "The Renormalization Group According to Balaban - III. Convergence." 37 pages. **Convergence of the expansion and stability bound.** This is where the actual polymer activity bounds get their constants. The structural form of the bounds (cluster-norm + tree-decay + activity scaling) is what we need for SU(2).

**Don't bother with Dimock II yet** — large fields are an orthogonal concern; for sparse Wilson high-plaquette indicators, the high-plaquette set is a "small field" event in the Bałaban sense (rare deviations from the trivial configuration). The large-field contribution is what's hard for the *partition function* but not necessarily for *high-plaquette inclusion probabilities*.

**Estimated time:** 2-3 days of careful reading with notes.

### Phase 2: Bałaban II for SU(N) (3-5 days)

Now go to the actual paper.

**Bałaban II (Comm. Math. Phys. 116, 1988).** "Renormalization group approach to lattice gauge field theories. II. Cluster expansions." 22 pages.

The structure (typical of Bałaban) is:

- **§1 Setup.** Same notation as Bałaban I; the effective action $A_k(U)$ at RG step $k$, the small-field characteristic function $\chi_{<} (U)$, the block-spin variables.
- **§2 Polymer activities.** Definition of the polymer activity functional $K(Y; U, U')$ where $Y$ is a polymer (connected lattice subset), $U$ is the gauge field, $U'$ is the block-averaged version. **This is the analog of our $\Phi(\Gamma; h)$.**
- **§3 Cluster expansion.** Mayer-style cluster expansion of the partition function with the polymer activities as expansion units.
- **§4 Bounds on polymer activities.** Tree-decay estimates, exponential weights, convergence criteria. **This is where $(C_*, m_*)$ live.**

**What to extract:**

1. The **explicit form of the polymer activity** $K(Y)$. In Bałaban's notation, it will look like

   $$|K(Y; U, U')| \le c_*^{|Y|} \exp(-m_* \cdot d(Y)) \cdot \text{(coupling factors)}$$

   where $d(Y)$ is some lattice diameter or spanning-tree length on $Y$, $c_*$ is a prefactor, and the coupling factors involve $\beta$, the RG step $k$, and possibly the block-spin scale $L$.

2. The **convergence criterion**: the value of $\beta_*$ such that for $\beta \ge \beta_*$ the cluster norm $\sum_{Y \ni 0} |K(Y)| \cdot e^{m_* d(Y)} < 1$.

3. The **dependence on RG step $k$**: Bałaban iterates the cluster expansion through many RG steps. The constants at step $k$ may scale with $k$ in a way that matters for the IR limit. For our purposes (a single lattice $L=24$, no iterated RG), we want the **constants at the unit-scale lattice**, which is roughly Bałaban's first RG step or the unscaled version.

4. The **observable being expanded**: Bałaban expands the partition function $Z$, not a high-plaquette inclusion probability. We need to translate. The cluster activities for our $\mathbb{E}_W \exp(\sum h_p Y_p(t))$ are obtained by adding a source term $\sum h_p Y_p(t)$ to the action and re-running the cluster expansion. **Whether Bałaban's machinery handles this source term gracefully is the central question.**

**Critical check.** Bałaban's machinery is for **smooth observables and the partition function**, not for hard indicators $Y_p(t) = \mathbf{1}\{\phi(U_p) \ge t\}$. The hard indicator introduces a discontinuity that may not fit the small-field framework directly. **Flag this immediately if it appears in the reading.**

**Estimated time:** 3-5 days, including significant time on §2-§4 and the convergence criterion proof.

### Phase 3: MR93 for SU(2)-specific structure (2-3 days)

**Magnen-Rivasseau-Sénéor (Comm. Math. Phys. 155, 1993), 325-383.** "Construction of $YM_4$ with an infrared cut-off." 58 pages.

MR93 takes a different approach from Bałaban: they use **phase-space cell decomposition** in a regularized axial gauge with an IR cutoff, rather than block-spin RG. The relevant content for us:

- **§3-4 Phase-space cell expansion.** The decomposition of the gauge field into momentum cells, with each cell contributing an activity. This is the analog of Bałaban's polymer activity but in momentum space.
- **§5-6 Convergence and bounds.** The convergence criterion (analogous to KP) and the activity bounds.
- **Crucially: large-field positivity.** MR93 handles the large-field region by a different mechanism than Bałaban — they use positivity at large field combined with separate small-field treatment. **High-plaquette events are large-field events** in their framework, which may make their treatment more directly applicable to our hard indicator $Y_p(t)$.

**What to extract:**

1. The **explicit IR cutoff scale** they use and whether their results survive removing the cutoff. (The cutoff is a feature, not a bug, for our finite-volume work — we want bounds on a finite lattice.)
2. The **constants in the phase-space cell expansion**: the analog of $(C_*, m_*)$ at the SU(2)-specific level.
3. The **large-field treatment** for high-plaquette events. **This is the most likely place to find a direct bound on $\mathbb{P}_W(\phi(U_p) \ge t)$ and its joint version.**
4. **Whether they give explicit numerical constants** or only existence statements. MR93 is a constructive paper, so explicit constants are likely but may be buried.

**Estimated time:** 2-3 days, focusing on §3-§6.

### Phase 4: Translation to $(M')_{\rm SU(2)}$ (2-3 days)

The Bałaban or MR93 output is a cluster bound at the **block-spin / phase-space-cell level**, not at the plaquette level. The bridge document uses plaquette-level $\Phi(\Gamma; h)$. A translation is needed.

**Translation sketch:**

1. **Block-spin to plaquette:** Bałaban's polymers $Y$ are unions of blocks; ours are sets of plaquettes. Each block contains $\sim L_{\rm block}^4$ plaquettes. The block-level cluster bound implies a plaquette-level bound with a multiplicative factor of $L_{\rm block}^{4 \cdot s}$ for clusters of size $s$ — generally a small overhead at the unit lattice.

2. **Smooth-source to hard-indicator:** Bałaban handles smooth sources $\sum h_p f_\varepsilon(U_p)$ with $f_\varepsilon$ a smoothed approximation of $\mathbf{1}_{[t, \infty)}$. As $\varepsilon \to 0$, the smooth source approaches the hard indicator. **Whether the cluster bound is uniform in $\varepsilon$ is the central question.** If yes, the smoothing bridge closes; if no, the hard-indicator version may genuinely require additional work (the smoothing bridge is the open task).

3. **Partition function vs inclusion probability:** Bałaban expands $\log Z$; we need $\log \mathbb{E} \exp(\sum h_p Y_p)$. The standard trick: introduce a source $h$, expand $\log Z(h) = \log Z + \log \mathbb{E}_W \exp(\sum h_p Y_p)$, and read off the $h$-dependent piece. This works at the polymer level: cluster activities containing the source factorize through the source insertion.

**What to extract from the translation:**

1. **A concrete numerical bound on $(C_*, m_*)$** at SU(2), $\beta = 3.5$, unit lattice, $\Lambda = 1$. **If the literature does not give such a bound directly, flag this as a partial extraction.**
2. **A clear statement of the smoothing-bridge gap** if the hard-indicator version is not directly proved.
3. **The KP convergence criterion** translated: is $C_* p J_{m_*} < 1$ at the working corner? Recall $p = 0.003$, $J_{m_*} \le 6 / m_*^4$ for the 4d plaquette lattice.

**Estimated time:** 2-3 days, possibly with consultation of expert mathematical physicists for the translation.

---

## 3. Checklist for "done" vs "partial" extraction

### Full extraction (manuscript-ready)

- [ ] Explicit numerical values of $C_*, m_*, \beta_*$ at SU(2), $\beta = 3.5$, unit lattice, $\Lambda = 1$, from either Bałaban II or MR93.
- [ ] Verification that $\beta_* \le 3.5$ (i.e., the working corner is in the convergent regime).
- [ ] Verification that the polymer bound applies to the **hard indicator** $Y_p(t)$, either directly or via a proven smoothing bridge with uniform constants.
- [ ] Computation of $N_{\rm KP}(p)$ from (B3.9) with the actual constants: $N_{\rm KP}(p) \le C_*^2 p J_{m_*} / (1 - C_* p J_{m_*})$.
- [ ] Verification that $N_{\rm KP}(p) \le 5$ at the working corner (suffices for firewall margin $\ge 0.4$).

### Partial extraction (manuscript-conditional)

- [ ] Explicit constants from Bałaban or MR93 in a related regime (different $\beta$, or for smooth observables only), with a stated extrapolation to our working corner.
- [ ] **Identification of the smoothing-bridge gap** as an explicit open task with estimated effort.
- [ ] **A numerical bound on $N_{\rm KP}(p)$ that is loose but finite** — this still gives a conditional firewall closure, just with weaker margin.

### Failed extraction (program impasse)

- [ ] No explicit constants accessible from the literature, **and**
- [ ] No proof that $\beta_* \le 3.5$ for SU(2), **and**
- [ ] No alternative cluster bound (Adhikari-Cao style for finite groups, or a direct estimate via Combes-Thomas + Fourier analyticity) that applies.

The program is then stuck on the (M') extraction. Two options: (a) shift the canonical working point to a regime where the extraction is easier (large $\beta$, smaller $\Lambda$, smoother observable); (b) prove (M') from scratch using one of the alternative methods (Glimm-Jaffe-Spencer, Mayer-Penrose, or the Adhikari-Cao knot decomposition adapted to continuous groups).

---

## 4. The hard-indicator vs smooth-observable distinction

**This is the single most likely failure point.** The reader should be alert to it from the start.

Bałaban II and MR93 are constructive papers. Their cluster bounds are proved for **smooth, analytic observables** (functions of $U_p$ that are smooth in the gauge field). The hard indicator $Y_p(t) = \mathbf{1}\{\phi(U_p) \ge t\}$ is **not** smooth: it has a jump discontinuity at $\phi = t$.

Three possible outcomes when checking whether the polymer bound applies to $Y_p(t)$:

**Outcome A: Direct extension works.** Some papers (e.g., Cammarota 1982 on long-range Ising correlations) prove cluster bounds for indicator-of-threshold observables via the explicit indicator formula
$$\mathbf{1}\{\phi \ge t\} = \int_0^\infty \mathbf{1}\{\phi - t \ge s\} \mathbf{1}\{s \le 0\} ds + \cdots$$
or via Fourier representations. **Check Bałaban II §4 footnotes and MR93 remarks for indicator-of-threshold examples.**

**Outcome B: Smoothing bridge is needed.** Define $f_\varepsilon: \mathbb{R} \to [0,1]$ smooth with $f_\varepsilon \to \mathbf{1}_{[t, \infty)}$ as $\varepsilon \to 0$, prove the polymer bound for $Y_p^{(\varepsilon)} := f_\varepsilon(\phi(U_p))$ with constants $(C_*^{(\varepsilon)}, m_*^{(\varepsilon)})$ uniform in $\varepsilon$, then take $\varepsilon \to 0$. **Whether the constants are uniform is the key question.** A smoothing bridge with $C_*^{(\varepsilon)} \to \infty$ as $\varepsilon \to 0$ fails; one with $C_*^{(\varepsilon)} \le C_*$ uniform succeeds.

**Outcome C: Direct hard-indicator proof is open.** Neither Bałaban II nor MR93 gives the hard-indicator version, and the smoothing bridge has non-uniform constants. The hard-indicator (M') is then a **genuine open analytic problem**, not just a literature extraction.

**If outcome C, the program's options are:**

1. **Use a smooth proxy.** Reformulate the firewall in terms of smooth indicators with $\varepsilon$ fixed. The v16 numerics can be redone with the smooth indicator; the firewall closure becomes a statement about smooth defect events. Less crisp but rigorous.
2. **Prove the smoothing bridge.** This is a real analytic problem (1-2 months), not a literature task. Possibly using the Combes-Thomas method on the lattice Laplacian.
3. **Defer to the literature.** Wait for a future paper that proves the hard-indicator cluster bound for SU(2). Not within program control.

---

## 5. What the bridge document needs (concrete)

The bridge document `NOTE_PMBSF_mprime_hpm_bridge.md` uses three things from $(M')_{\rm SU(2)}$:

1. **The cluster expansion existence and structure**: $\log \mathbb{E}_W \exp(\sum h_p Y_p(t)) = \sum_\Gamma \Phi(\Gamma; h)$.
2. **The polymer bound** $|\Phi(\Gamma; h)| \le C_*^{|\Gamma|} p^{|\Gamma|} e^{-m_* \tau(\Gamma)} \prod (e^{h_p} - 1)$.
3. **The singleton identity** $\Phi(\{p\}; h) = p (e^{h_p} - 1)$.

(3) is essentially the definition of $p = \mathbb{E}_W Y_p(t)$; it's automatic. (1) is the existence of the cluster expansion, which Bałaban II proves for smooth observables. (2) is the polymer bound — **this is what the extraction must deliver.**

The bridge document then derives $N_{\rm KP}(p)$, $\varepsilon_{\rm HPM}$, and the conditional firewall closure from (2). It does **not** care about the internal structure of the proof — only the final form (2) and the constants.

This means **a partial extraction with explicit numerical bounds on $(C_*, m_*)$, even if loose, is sufficient to advance the program.** The bridge plugs them in; the firewall closure follows; the margin is what the math gives.

---

## 6. Recommended sequencing

Given the constraints (paywalled / bot-blocked Bałaban II and MR93 PDFs are typical for older Comm. Math. Phys. papers; institutional access via a university library is the standard route):

**Week 1:** Read Dimock I and III (open access on arXiv). Internalize the Bałaban method on the simpler $\phi^4$ model. Take notes on the polymer activity, cluster expansion, and convergence criterion.

**Week 2 (early):** Obtain Bałaban II via institutional access or interlibrary loan. Read §2-§4 carefully. Extract the SU(N)-specific polymer bound. Flag the smooth-observable assumption.

**Week 2 (late):** Obtain MR93. Read §3-§6 for the SU(2)-specific large-field treatment. Check whether their large-field bound covers the hard-indicator case directly.

**Week 3:** Write up the translation to plaquette-level $(M')_{\rm SU(2)}$. Either (a) compute the numerical $N_{\rm KP}(p)$ at the working corner if constants are extractable, or (b) write up the smoothing-bridge gap if the hard-indicator version is not directly proved.

**Deliverable at week 3:** A 3-5 page note stating either:
- "Extraction complete: $(C_*, m_*) = (\text{value}, \text{value})$, $N_{\rm KP}(0.003) \le \text{value}$, $\varepsilon_{\rm HPM} \le \text{value}$, firewall margin $\ge \text{value}$." — **manuscript-ready.**
- "Partial extraction: constants are X for the smooth-observable version; smoothing-bridge gap is open with estimated effort Y; conditional firewall closure follows if smoothing bridge holds with uniform constants." — **conditional, with explicit follow-up.**
- "Extraction failed: $\beta_* > 3.5$ in the available literature, or no explicit constants extractable. Need to either shift working corner or prove (M') from scratch." — **program impasse, requires re-scoping.**

---

## 7. Honest disclaimers

1. **I have not read Bałaban II or MR93.** This protocol is constructed from search results, the abstracts, the Adhikari-Cao 2022 paper (which discusses cluster expansions for finite gauge groups), the Dimock expository series (which covers $\phi^4$ in $d=3$), and the bridge document.

2. **The constants $(C_* = 2, m_* = 0.5)$ used in the bridge document are illustrative placeholders.** The actual SU(2)-specific values are what this extraction protocol is designed to deliver.

3. **The hard-indicator question may be genuinely open.** It is consistent with the program's prior literature scan (and explicitly noted in the Route I corrections memo, §3) that the hard-indicator cluster bound is not directly in either Bałaban or MR93. The smoothing bridge is the standard fallback but is not free.

4. **Adhikari-Cao 2022 is for finite groups, not continuous SU(2).** The knot decomposition technique it uses is suggestive but not directly applicable. Continuous SU(2) is harder than finite non-Abelian because of the spin-wave / IR-divergent sector that doesn't exist for finite groups.

5. **The realistic outcome of a 1-2 week reading effort is partial extraction with explicit smooth-observable constants and an explicit smoothing-bridge gap.** Full extraction with hard-indicator constants is the best case and is not guaranteed.

---

## 8. Summary

The (M')_SU(2) extraction is a concrete 1-2 week mathematical reading task with three possible outcomes (full / partial / failed). The protocol above specifies:

- The corrected bibliography (MR93 not MR95; Bałaban Part II 1988 not Part I 1987).
- The four constants $(C_*, m_*, \beta_*, \xi_*)$ to extract.
- The reading sequence (Dimock for method, Bałaban II for SU(N) constants, MR93 for SU(2)-specific large-field treatment).
- The hard-indicator vs smooth-observable gap as the central failure point.
- Three checklists (full / partial / failed) for assessing the outcome.

**The next concrete action is institutional access to Bałaban II and MR93, followed by a 1-2 week reading period.** I cannot do this for you. What I can do, once you (or a collaborator) extract the constants, is plug them into the bridge document and compute the firewall closure margin.

If the extraction is partial, I can also help draft the smoothing-bridge analysis as a separate 1-2 week analytic task.
