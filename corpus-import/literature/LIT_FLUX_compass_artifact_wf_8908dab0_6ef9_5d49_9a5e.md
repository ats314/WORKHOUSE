# Novelty-and-Priors Literature Check: C-odd SU(N) Plaquette Observables, Trigonometric Factorizations, and One-Plaquette Gap Asymptotics

## TL;DR
- The **underlying trigonometry** (I) and the **Lie-algebra skeleton** (II) are strictly classical; but their specific *packaging* — the sinc-product form of Im Tr U, and the N≥5 threshold for an independent quintic C-odd direction *in glueball/plaquette operator content* — are not found in the retrievable literature and appear novel.
- The **new lattice operators** (III) — an Im Tr of the doubly-wound plaquette used as a separate C-odd variational operator, a weak-field-*content*-improved cubic source cancelling the quintic P₅ term, and an e₅/det-X SU(5)-specific source — have **no located prior**; multiply-wound traces exist elsewhere (N=4 SYM, ABJM, double-winding confinement studies) but never as C-odd glueball operators.
- The **3/2 C-odd/C-even one-plaquette gap ratio and 1/√β corrections** (IV) are **not stated in any retrievable source**; the Gross-Witten-Wadia large-N free-energy scaling you contrast against is classical and correctly distinguished, but a joint β=N³τ *spectral* scaling has no located precedent.

---

## (I) TRIGONOMETRIC FACTORIZATION IDENTITIES

**VERDICT: CLASSICAL (the identities themselves) / APPARENTLY NOVEL (the sinc-product packaging of Im Tr U in lattice/RMT).**

The SU(3) identity sin a + sin b − sin(a+b) = 4 sin(a/2) sin(b/2) sin((a+b)/2) is a textbook triangle identity. It is the standard form of "sin A + sin B + sin C = 4 cos(A/2)cos(B/2)cos(C/2) for A+B+C=π" applied to three angles summing to zero (setting c = −(a+b), so sin c = −sin(a+b)). This identity is documented across standard trigonometry references and is a staple of the "conditional identities for angles of a triangle" literature (the widely reproduced proof of sin A + sin B + sin C = 4 cos(A/2)cos(B/2)cos(C/2) under A+B+C=π). It is elementary and provable in three lines by sum-to-product.

The SU(4) four-angle version, Σⱼ sin θⱼ = 4 sin((θ₁+θ₂)/2) sin((θ₁+θ₃)/2) sin((θ₂+θ₃)/2) under Σθⱼ = 0, is likewise an elementary consequence of iterated sum-to-product; it belongs to the same classical family of "sum of sines of angles summing to zero" factorizations. I did not locate this exact four-angle form as a single named entry in Gradshteyn-Ryzhik or Hobson from retrievable sources (I did not have full-text access to those two references), but it is not a new mathematical fact — it is a routine corollary of the sum-to-product apparatus.

What I could **not** find in any retrievable lattice-gauge, random-matrix, one-plaquette-model, or character-expansion source is the *specific statement* that Im Tr U = −(P₃/6)·∏ⱼ sinc(θⱼ/2) for SU(3) (or the SU(4) pair-product analogue). The closest structural precedent is the standard Weyl character formula / Vandermonde-denominator machinery, in which characters of SU(N) are ratios of determinants over the eigenphases (Schur-polynomial form χ_R = det(εᵢ^{ℓⱼ})/∏_{i<j}(εᵢ−εⱼ)), and the eigenvalue-density character expansions of traced Wilson loops (e.g., the SU(N) 2D Yang-Mills eigenvalue-density work expanding Tr W^k in characters, arXiv:0904.4116). These use the same Vandermonde/Weyl-denominator structure but do **not** present Im Tr U as a manifestly-positive sinc-product form factor times −P₃/6. The packaging is apparently novel.

**Searches performed that returned nothing relevant to the sinc-product packaging:**
- "sin a + sin b − sin(a+b) = 4 sin(a/2)sin(b/2)sin((a+b)/2) identity" → returned only generic sum/product formula pages.
- "sum of sines four angles summing to zero product identity" → generic sum-to-product only.
- "sin A + sin B + sin C = 4 cos(A/2)cos(B/2)cos(C/2) triangle identity" → confirmed the classical triangle identity; no SU(N)/plaquette connection.
- "imaginary part of trace of SU(3) plaquette written as product of sinc functions of eigenphases" → no matching result; only general plaquette-action / eigenvalue-density material.
- "imaginary part trace SU(N) unitary matrix product sines eigenvalue Weyl denominator character expansion" → returned Weyl-character/Vandermonde and eigenvalue-density papers, none with the sinc-product Im Tr U form.

---

## (II) CUBIC LOCK / RANK-FIVE (N≥5) TRANSITION

**VERDICT: PARTIALLY KNOWN — the Lie-algebra skeleton is classical; its manifestation as an N≥5 quintic C-odd threshold in Im Tr U / C-odd glueball operator content appears novel.**

**Classical part.** That su(N) = A_{N−1} has exactly N−1 primitive symmetric invariant tensors / Casimirs, at orders 2, 3, …, N, and that the odd-order primitive invariants (d_{abc} at order 3, the order-5 invariant, order-7, …) turn on progressively with N, is fully classical:
- de Azcárraga, Macfarlane, Mountain, Pérez Bueno, "Invariant tensors for simple groups," Nucl. Phys. B510 (1998) 657 [physics/9706006]. Verbatim from the abstract: *"For the A_l algebra it is explicitly shown that the generic forms of these tensors become zero except for the l primitive ones and that they give rise to the l primitive Casimir operators. Tables for the 3- and 5-cocycles for su(3) and su(4) are also provided."* This is the canonical reference the requester already cites.
- de Azcárraga & Macfarlane, "Fermionic realisations of Lie algebras," Nucl. Phys. B581 (2000) 743 [hep-th/0003111], Sec. 4.3, gives the explicit su(5) fifth-order operator K₅ built from the su(5) 5-cocycle Ω_{sabcd} — direct confirmation that an independent quintic primitive invariant first appears at su(5).
- Mountain, "Invariant tensors and Casimir operators for simple compact Lie groups," J. Math. Phys. 39 (1998) 5601, and Macfarlane-Pfeiffer [math-ph/9907024] give the systematic reduction of non-primitive to primitive tensors. That d_{abc} vanishes for SU(2) and the C-odd threshold is N≥3 is textbook.

So the "odd-Casimir staircase" (order-3 for SU(3),SU(4); order-3,5 for SU(5),SU(6); order-3,5,7 for SU(7),SU(8); …) is a restatement of the classical primitive-invariant content of A_{N−1}.

**Novel part.** What I could **not** find in any retrievable source is a prior statement that:
(a) the weak-field expansion of Im Tr e^{iX} = −(P₃/6)(1 − P₂/24) + e₅/24 + O(|X|⁷) contains an *independent quintic C-odd invariant* (e₅ = det X for SU(5)) precisely at N≥5, or
(b) that this constitutes a threshold ("cubic lock" failing first at N=5) in glueball / C-odd operator construction.

Searches for "d^{abcde} gluonic operator," "quintic Casimir glueball," "fifth-order invariant SU(5) gauge," "det X / det F glueball source," and "C-odd operator basis SU(N)" returned only: (i) the pure Lie-algebra tensor literature above; (ii) unrelated appearances of rank-5 SU(N) tensors in causal-perturbation-theory anomaly bases (Scharf school, hep-th/9411080) and in composite-Higgs SU(5)/SO(5) operator bases [1808.10175], neither of which concerns C-odd gluonic glueball operators or the weak-field content of Im Tr U. No one-plaquette / single-link model paper I retrieved notes that Im Tr U ceases to be proportional to a single odd invariant beyond N=4.

*Coincidental-N=5 caution.* There is an unrelated, well-known "N≥5" threshold in this field that a careless reader might conflate with yours: the bulk strong-to-weak transition. Per Bursa & Teper and related work (hep-th/0610030), *"In D = 3 + 1 it is known that for N ≥ 5 there is a strong first order transition as β is varied from strong to weak coupling."* This is a dynamical bulk-transition statement, entirely distinct from your algebraic quintic-invariant threshold; you should pre-empt the confusion explicitly.

**Searches performed that returned nothing relevant:**
- "quintic Casimir d abcde gluonic operator gauge invariant SU(5) fifth order invariant" → tensor-algebra and composite-Higgs hits only.
- "C-odd glueball operator imaginary part Wilson loop construction SU(3)" → standard shape-based constructions only (see III).
- "oddball C-odd glueball SU(N) N dependence baryonic operator det plaquette large N" → large-N glueball reviews; no quintic-threshold statement.

---

## (III) NEW LATTICE OPERATORS

**VERDICT: (a) PARTIALLY KNOWN (multiply-wound traces exist elsewhere, never as C-odd glueball operators); (b) APPARENTLY NOVEL; (c) APPARENTLY NOVEL.**

**(a) C-odd operator conventions in glueball spectroscopy.** Every lattice C-odd glueball construction I retrieved builds operators from the **imaginary part of traced Wilson loops of different SHAPES** (and smearing levels), never from Im Tr of a *multiply-wound / squared* plaquette as a separate variational channel:
- Teper, "SU(N) gauge theories in 2+1 dimensions" [hep-lat/9804008], Sec. 3.2.1: *"under charge conjugation the trace will go to its complex conjugate: so the real part is C=+ and the imaginary part is C=−"*; operators are built from loops of various shapes.
- Morningstar & Peardon [hep-lat/9901004]: many loop *shapes*, real/imag parts for C.
- Chen et al. [hep-lat/0510074]: two types of improved local gluonic operators for O(a²) improvement — a different target (discretization artifacts), consistent with the requester's preliminary note.
- Athenodorou & Teper [2007.06422, 2106.00364]: all cubic-group irreps, both C, from spatial Wilson loops of many shapes.
- Sakai & Sasaki [2211.15176]; B-field / gradient-flow constructions [2603.20178] — real part → C=+, imaginary part → C=−, shape-based.

Multiply-wound / doubly-wound traces do appear in the literature, but in unrelated contexts, and never as C-odd glueball variational operators:
- N=4 SYM / string theory: W₂ = (1/N)⟨Tr W²⟩ vs W_{1,1} = (1/N²)⟨(Tr W)²⟩ [hep-th/0010274, Drukker-Fiol lineage].
- ABJM: multiply-wound BPS Wilson loops [1605.01025].
- Higher-representation / k-wound loops via Frobenius inversion Tr_F U^k = Σ c_i^k Tr_{R_i} U [2202.00028].
- Double-winding Wilson loops in confinement studies (Kondo, Shibata, Matsudo, Kato) [2111.03998, 1910.08894] — coplanar/shifted double loops, area-law tests, not C-odd spectroscopy.
- Closest lattice-Hamiltonian remark: Carlsson, McIntosh, McKellar, Hollenberg [hep-lat/0207019] note that *"a more complicated basis (including, for example, loops covered more than once) is required to simulate SU(3) excited states"* — i.e., multiply-covered loops as basis enrichment, but not as a C-odd, weak-field-engineered operator.

So (a) is best labelled PARTIALLY KNOWN: multiply-wound traces are a known object, but their use as *distinct C-odd glueball variational operators* is not found.

**(b) Weak-field-content improvement** (cancelling the quintic P₅ contamination of Im Tr U by combining the fundamental and doubly-wound traces): no prior located. All "improved operator" work I retrieved (Chen et al. [hep-lat/0510074]; Lucini-Teper-Wenger [hep-lat/0404008]; tree-level Symanzik improvement) targets **discretization (O(a²)) artifacts**, not the weak-field operator content / higher-power-sum contamination. Improving the *operator's continuum weak-field expansion* rather than its lattice-spacing artifacts appears to be a new notion in this context.

**(c) An operator explicitly targeting det X / e₅ as an SU(5)-specific glueball source:** no prior located.

**Searches performed that returned nothing relevant:**
- "doubly wound Wilson loop multiply wound trace glueball operator higher winding lattice" → N=4 SYM / ABJM / confinement double-winding only.
- "Morningstar Peardon efficient glueball operators"; "Chen glueball spectrum matrix elements C=-1 operators" → shape-based, O(a²)-improvement only.
- "improved lattice operator cancel higher dimension weak field expansion glueball tree level Symanzik trace power" → corroborated via the improvement-context papers already retrieved.

---

## (IV) ONE-PLAQUETTE GAP ASYMPTOTICS AND N³ SCALING

**VERDICT: APPARENTLY NOVEL (the 3/2 C-odd/C-even one-plaquette gap ratio as stated, and the β=N³τ spectral scaling) / CLASSICAL and correctly distinguished (the GWW large-N free-energy scaling).**

**(a) The 3/2 gap ratio and 1/√β corrections.** My dedicated deep search (including the most directly relevant body of work, the Carlsson-McKellar one-plaquette variational program) found **no source stating** that the C-odd/C-even one-plaquette gap ratio → 3/2 as β→∞, nor any 1/√β correction to single-plaquette SU(N) Hamiltonian spectra. Specifics:
- Carlsson, McIntosh, McKellar, Hollenberg [hep-lat/0207019, PRD 67 114509 (2003)] compute the symmetric (C=+) and antisymmetric (C=−) one-plaquette mass gaps for SU(2), SU(3) but do not report a 3/2 ratio.
- Carlsson & McKellar, "SU(N) glueball masses in 2+1 dimensions" [hep-lat/0303016, INSPIRE 615639] extend to SU(2)–SU(5), computing both sectors; no 3/2 ratio or 1/N correction to a ratio is stated.
- Carlsson & McKellar, "The large N glueball mass spectrum in 2+1 dimensions" [hep-lat/0303018] give an *empirical* two-dimensional harmonic-oscillator labelling m_n(J^PC) = γ₁(2n+γ₂) with integer intercepts γ₂ = 1 for 0++ and γ₂ = 5, 7 for the C-odd 0−−, 2−− — which does **not** reduce to a clean 3/2 C-odd/C-even ratio, and which the authors themselves flag as tentative. They also report an anomalous **1/√N** (not 1/√β) correction to the small-β 0−− gap minimum, ν₁(N) = 0.41390 + 1.255/√N.
- The U(1)/compact-QED analogue (Hamer group [hep-lat/0307029]) explicitly expects the symmetric/antisymmetric ratio to lie between 1 and 2, hitting **2** (not 3/2) in the free-field two-quantum limit — a relevant contrast.
- The only clean "3/2" located anywhere in the strong-coupling literature is the leading-log strong-coupling relation m(excited) ∼ −6 log β vs m(lowest) ∼ −4 log β (ratio 3/2), stated by R. S. Schor, "Glueball spectroscopy in strongly coupled lattice gauge theories," Commun. Math. Phys. 92 (1984) 369–395, verbatim: *"Besides the lowest excitation m₀ ∼ −4 log β, we find two nearly degenerate excited states m₁, m₂ with mᵢ ∼ −6 log β (i=1,2)."* This is a small-β Euclidean statement whose C-parity / one-plaquette-Hamiltonian correspondence is not established in the retrieved text.

Thus the specific "Δ₋/Δ₊ → 3/2 as β→∞, with Δ₋ − (3/2)Δ₊ = 9/(32N) + O(β^{−1/2})" claim is not a quotable prior result; it is apparently novel — with the caveat that a 3/2 appears in unrelated strong-coupling (Schor) and oscillator-labelling (Carlsson-McKellar) contexts, and that the U(1) free-field analogue gives 2, not 3/2.

**(b) GWW scaling conventions (for context).** The Gross-Witten-Wadia one-plaquette unitary matrix model is classical and precisely documented. Gross & Witten, "Possible Third Order Phase Transition in the Large-N Lattice Gauge Theory," Phys. Rev. D 21 (1980) 446, state verbatim: *"The large-N limit of the two-dimensional U(N) (Wilson) lattice gauge theory is explicitly evaluated for all fixed λ = g²N … a third-order phase transition, at λ = 2, is discovered"* (with plaquette expectation ⟨u_p⟩ = 1 − λ/4 for λ ≤ 2 and = 1/λ for λ ≥ 2). The companion analysis is S. R. Wadia, "N = ∞ Phase Transition in a Class of Exactly Soluble Model Lattice Gauge Theories," Phys. Lett. B 93 (1980) 403, and "A Study of U(N) Lattice Gauge Theory in 2-dimensions," EFI-79/44 (1979) [arXiv:1212.2906]. Note the convention dependence: the critical point is λ_c = 2 in the Gross-Witten normalization (λ = g²N), equivalently t_c = 1 in the frequently-used normalization t = Ng²/2 — the same transition, different bookkeeping. Either way this is the standard large-N *free-energy* scaling (coupling held at fixed λ = g²N, i.e. β ∼ N²). Your N²-vs-N³ distinction is therefore correctly drawn: the standard scaling balances the *free energy*, whereas your β = N³τ is proposed to balance the *gap expansions* — a different object.

**(c) N³ coupling scaling for spectral quantities in reduced/matrix models.** No precedent located. Eguchi-Kawai and twisted-EK reduction use an *effective volume* scale l_eff = a√N (a √N, not N³, rescaling), with the coupling held at the fixed 't Hooft value; I found no N³ coupling scaling for spectral quantities in EK/TEK (González-Arroyo & Okawa), induced QCD, or matrix quantum mechanics.

**Searches performed that returned nothing relevant:**
- "one plaquette model excited state gap ratio parity even odd 3/2 harmonic oscillator strong coupling SU(N)" → covered via Exa and the dedicated subagent; no 3/2 one-plaquette ratio located.
- "one-plaquette SU(N) Hamiltonian ratio of C-odd to C-even mass gap 3/2 weak coupling expansion" → Carlsson-McKellar program and Hamer U(1) results, none stating 3/2.
- "Eguchi-Kawai reduced model coupling scaling spectrum N^3 twisted large N" → √N effective-volume scaling only; no N³ spectral scaling.
- "Robson Webber one plaquette Hamiltonian gauge theory eigenvalues" → general Hamiltonian-LGT gauge-covariance work; no gap ratio.

---

## SUMMARY TABLE

| Claim | Verdict | Closest prior |
|---|---|---|
| (I) SU(3) sin identity | CLASSICAL | Standard triangle identity sin A+sin B+sin C=4∏cos(·/2) (A+B+C=π) |
| (I) SU(4) four-angle sine factorization | CLASSICAL (elementary corollary) | Sum-to-product family; no single named GR/Hobson entry located |
| (I) sinc-product form of Im Tr U in lattice/RMT | APPARENTLY NOVEL | Weyl/Vandermonde character formula; 2D-YM eigenvalue-density expansions [0904.4116] |
| (II) N−1 primitive Casimirs; odd-tensor staircase | CLASSICAL | de Azcárraga et al. B510 (1998) 657 [physics/9706006]; su(5) 5-cocycle [hep-th/0003111] |
| (II) N≥5 quintic C-odd threshold in Im Tr U / operator content | APPARENTLY NOVEL | No prior; only pure-tensor and composite-Higgs SU(5) bases (distinct N≥5 bulk transition in hep-th/0610030 is unrelated) |
| (III a) Im Tr of doubly-wound plaquette as C-odd operator | PARTIALLY KNOWN | Multiply-wound traces in N=4 SYM [hep-th/0010274], ABJM [1605.01025], double-winding confinement [2111.03998]; Carlsson "loops covered more than once" [hep-lat/0207019] |
| (III b) Weak-field-content improvement (cancel P₅) | APPARENTLY NOVEL | Chen et al. [hep-lat/0510074] & Symanzik improvement target O(a²), not weak-field content |
| (III c) e₅/det-X SU(5)-specific glueball source | APPARENTLY NOVEL | None located |
| (IV a) 3/2 C-odd/C-even one-plaquette gap ratio; 1/√β corrections | APPARENTLY NOVEL | Carlsson-McKellar [hep-lat/0207019, 0303016, 0303018] compute both gaps, no 3/2; U(1) free-field ratio =2 [hep-lat/0307029]; strong-coupling −6logβ/−4logβ=3/2 (Schor, CMP 92 (1984) 369) |
| (IV b) GWW large-N free-energy scaling | CLASSICAL | Gross-Witten PRD 21 (1980) 446 (transition at λ=2); Wadia PLB 93 (1980) 403 |
| (IV c) β=N³τ spectral scaling in reduced/matrix models | APPARENTLY NOVEL | EK/TEK use l_eff=a√N effective volume, not N³ coupling |

---

## RECOMMENDATIONS (what to cite, and how to frame the novelty claims)

**Stage 1 — Frame (I) and the classical part of (II) as "known, and we use it," not as results.** Cite a standard trigonometry reference for the triangle identity and present the SU(4) four-angle form as an elementary corollary; do not claim these as new. For the invariant-tensor skeleton cite de Azcárraga, Macfarlane, Mountain, Pérez Bueno, Nucl. Phys. B510 (1998) 657 [physics/9706006]; de Azcárraga & Macfarlane [hep-th/0003111] (su(5) 5-cocycle, Sec. 4.3); Mountain, J. Math. Phys. 39 (1998) 5601; Macfarlane-Pfeiffer [math-ph/9907024]; Sudbery (1990). This inoculates the paper against "you rediscovered classical trig / classical Casimir counting."

**Stage 2 — Stake the genuinely novel claims sharply.** The defensible novelty is: (i) the sinc-product *form factor* representation of Im Tr U and its positivity on the alcove; (ii) the N≥5 quintic C-odd threshold *in the weak-field content of glueball/plaquette operators* (explicitly distinguished from the pure-Lie-algebra counting and from the unrelated N≥5 bulk transition); (iii) the three new operators; (iv) the 3/2 gap ratio and β=N³τ spectral scaling. State each as "we are not aware of a prior statement," not "there is none."

**Stage 3 — Cite the near-misses to show you did the diligence.** For C-odd operator conventions: Teper [hep-lat/9804008] §3.2.1; Morningstar & Peardon [hep-lat/9901004]; Chen et al. [hep-lat/0510074]; Lucini-Teper-Wenger [hep-lat/0404008]; Athenodorou & Teper [2007.06422, 2106.00364]; Sakai & Sasaki [2211.15176]. For multiply-wound context to distinguish from: Drukker-Fiol lineage [hep-th/0010274]; ABJM [1605.01025]; double-winding confinement [2111.03998, 1910.08894]. For one-plaquette Hamiltonian spectroscopy and GWW: Carlsson-McIntosh-McKellar-Hollenberg, PRD 67 (2003) 114509 [hep-lat/0207019]; Carlsson-McKellar [hep-lat/0303016, hep-lat/0303018]; Kogut-Sinclair-Susskind, Nucl. Phys. B114 (1976) 199; Banks-Susskind-Kogut, PRD 13 (1976) 1043; Schor, CMP 92 (1984) 369; Gross-Witten, PRD 21 (1980) 446; Wadia, PLB 93 (1980) 403; González-Arroyo & Okawa (twisted EK).

**Stage 4 — Pre-empt the two most likely referee objections.** (a) On (III a): explicitly acknowledge that multiply-wound traces are known objects (N=4 SYM, ABJM, double-winding) and that Carlsson-McKellar mention "loops covered more than once," then argue your novelty is their use as a *weak-field-engineered C-odd variational operator*. (b) On (IV a): acknowledge the recurring 3/2 in Schor's strong-coupling logs and the Carlsson-McKellar oscillator labelling, and the U(1) free-field ratio of 2, then argue your 3/2 is a *different, β→∞ Hamiltonian one-plaquette* statement.

**Benchmarks that would change these verdicts:** any of the following, if found, downgrades the corresponding "APPARENTLY NOVEL" to "PARTIALLY KNOWN": (1) a one-plaquette-model or character-expansion paper writing Im Tr U as a sinc/half-angle product; (2) any glueball/oddball paper invoking det X, e₅, or d^{abcde} as a gluonic source; (3) any lattice study using Im Tr U^k (k≥2) as a *separate* C-odd operator; (4) any Hamiltonian-LGT paper stating a C-odd/C-even one-plaquette gap ratio of exactly 3/2 at weak coupling, or a 1/√β spectral correction; (5) any reduced/matrix-model paper with an N³ coupling scaling for spectral (not free-energy) quantities.

## CAVEATS
- "Apparently novel" here means *not found in retrievable sources after the searches listed*; absence of a located prior is not proof of absence. The claims most exposed to a hidden prior are (III a) — because multiply-wound traces are a known object that someone may have used as a C-odd probe in an obscure proceedings — and (IV a), where the number 3/2 recurs in adjacent (but distinct) strong-coupling and oscillator-labelling settings.
- I did not have full-text access to Gradshteyn-Ryzhik, Hobson, or several 1976–1989 Hamiltonian strong-coupling papers; verdicts on those rest on secondary confirmations and on the dedicated subagent's targeted retrieval.
- The GWW critical-point value is convention-dependent (λ_c = 2 with λ = g²N in Gross-Witten; t_c = 1 with t = Ng²/2 elsewhere); ensure your manuscript fixes one convention explicitly when drawing the N²-vs-N³ contrast.
- All mathematics in the claims was taken as given per the requester's instruction; this report evaluates only priors, not correctness.