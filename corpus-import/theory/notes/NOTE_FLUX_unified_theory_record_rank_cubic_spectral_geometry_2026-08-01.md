# Unified Theory Record: Rank-Cubic Gauge-Constrained Spectral Geometry

**Canonical date:** 2026-08-01
**Role:** top-level synthesis of the entire project corpus. Supersedes `GAUGE_CONSTRAINED_SPECTRAL_GEOMETRY_STRENGTHENED_THEORY_2026-07-13.md` as the unifying record. It does **not** supersede the seven scope-specific 2026-07-13 canonical ledgers, the 2026-07-14 updated flat-band record, or the dedicated certificate files, which remain controlling for their declared domains and exact constants.
**Newly integrated sources (post-2026-07-13):** `NOTE_O4_fourth_order_hodge_shape_space_foliated_mobility.md` (07-23); `FLATBAND_PAPER_EXPANSION_AUDIT_2026-07-25.md`; `SU4_HYBRID_COMPLETE_THEOREM_V2` and certificates; `wilson_bergman_weight_theorem.md/.py/log`; `cdg_transplant_results.md`; `su2_bergman_toy_results.md`; `su3_bergman_rank2_results.md`; `seam_branch_point_results.md` + locator; `gap_singularity_atlas.md` + `singularity_atlas.py`/`atlas2.py`; `seam_crossover_v1_results.md` + `crossover_nk.py`; `recommended_tests_audit.md`; `ten_proofs_x_one_plaquette_synthesis.md`; `tight_connections_review.md`; the hardened SU(3) T₁⁺⁻ Monte Carlo pipeline, its A100 pilot JSONs, the Athenodorou–Teper replay-gate verification, and the validated 14³×16 run recorded in `SOURCEOFGOD.txt`.

---

## 0. Status vocabulary

The four-grade protocol of the canonical ledgers is retained unchanged: **Proven** (analytic or exact-arithmetic derivation, within its stated scope), **Computationally verified (CV)** (exact or converged finite computation; corroboration, not theorem), **Conjectural** (positive mechanism with finite evidence, no all-parameter proof), **Open** (not established). Dispositions **superseded / rejected / withdrawn** appear only in the conflict register (§8). Precedence rules are those of the 07-13 ledgers: later explicit corrections override earlier statements, executed certificates override prose, exact arithmetic overrides decimals, and local results are never promoted to global field-theoretic claims without separate proof.

## 1. The theory in one paragraph

The corpus now supports a single structural theory with six pillars and three cross-cutting theses. Internally, compact Lie geometry fixes local spectral stiffness (the large-β one-plaquette class theory, Pillar I). Spatially, cubical chain-complex geometry fixes mobility (the strong-coupling homological flat-band theory, Pillar II). Globally, projected-capacity geometry constrains what survives coupling to the Wilson measure (the conditional Peierls program, Pillar III). Two new analytic layers now connect these: a **seam theory** of the gap functions' complex singularities, in which every observed obstruction to crossover is an identified exceptional-point level collision whose symmetric functions are analytic (Pillar IV), and a **weight-and-transfer theory** built on the exact Bessel–Toeplitz form of the Wilson–Bergman weight, which converts the program's N-uniformity question into two exact growth rates (Pillar V). A hardened Euclidean Monte Carlo layer (Pillar VI) has now produced the program's first like-for-like agreement with published physics and, more importantly, converted the long-standing local-to-physical scope firewall from a precaution into a measured number. The unifying quantitative discovery is a **rank-cubic law**: the scale N³ appears independently as the fusion coefficient decay t_N ∼ 1/(4N³), as the ordering threshold β ≫ N³ of the fixed-rank local expansion (equivalently the matched-scaling variable τ = β/N³), and as the exact growth Θ(N³) of the Schur transfer constant. Fixed-rank theorems exist; N-uniform ones provably fail along every route so far attempted, now with exact rates attached.

## 2. Pillar I — Compact one-plaquette local spectral theory (large β, fixed N)

Unchanged in substance from the combined 07-13 ledger; restated for closure of this record.

The SU(3) C-even class gap obeys the three-term compact theorem

Δ⁺_{SU(3)}(β) ∼ √(2β/3) − 5/16 − (311√6/9216) β^{−1/2} + O(β^{−1}),

with the isolated non-radial rank-two shift c₁ − c₁^rad = √6/576 exactly. **Proven** (compact class sector, standard nondegenerate compact-well semiclassics as declared infrastructure). The fixed-rank formulas

Δ⁺_{SU(N)} = √(2β/N) − (2N²−3)/(16N) − √2(6N⁴−24N²+41)/(1024N^{3/2}) β^{−1/2} + O_N(β^{−1}),
Δ⁻_{SU(N)} = √(9β/2N) − 3(N²−3)/(16N) − √2(14N⁴−97N²+290)/(1536N^{3/2}) β^{−1/2} + O_N(β^{−1}),

are **Proven at N = 3**, **CV for N = 4,…,12**, **Conjectural** for unrestricted fixed N. They are non-uniform in N; the displayed hierarchy already requires β ≫ N³ (first appearance of the rank-cubic law). The radial-tail obstruction, the finite-channel-only status of the leakage root ρ₃, and the compressed-versus-buffered resolvent split all stand as graded in the combined ledger. The dual-basis coordinate-space Weyl-triangle solver now cross-validates the character graph in both C sectors at β = 64–256 to ≤ 2.3×10⁻⁸ (**CV**, `recommended_tests_audit.md`), retiring the early triangle-solver pathology.

## 3. Pillar II — Strong-coupling homological flat-band and mobility theory (small y, spatial KS Hamiltonian)

This pillar has advanced the most since 07-13.

**Complete C-odd Bloch spectrum (new theorem).** With u_j = 1 − e^{ik_j}, q = Σ|u_j|², the incidence identity ÑÑ† = qI − ww† gives exactly

spec S(k) = { −4, −4 + q(k), −4 + q(k) },

so the lowest branch is flat at all k with explicit projector P_flat = ww†/q, an r^{−3} real-space projector tail, and exact finite-size scales. The C-even sector has **no** flat band by the two-point spectral argument spec A(0) = {12,0,0} vs spec A(π,π,π) = {−4,−4,−4}. Both **Proven** (07-25 audit, promotable directly into the manuscript).

**Homology and Hodge content.** dim Z₂ = N₃ + b₂ − b₃; on the torus the raw degeneracy L³ + 2 equals rank ∂₃ + b₂, not a Betti number; the face/link pair is an exact one-sided cubical Hodge operator with zero Witten index. The correct headline (Proven): the C-odd Hamiltonian's kernel separates exact cube boundaries from harmonic two-cycles.

**Fourth-order shape space (07-23, exactly certified).** The tromino support decomposes into **twelve** actual space-group orbits, not two classes; the projected nonconstant obstruction space is **four-dimensional**,

ε₄(k) = c₀ + A q + B e₂ + C (4e₂/q) + D (e₃/q),

with an exactly invertible four-point extraction (Γ, X, M, P, R) and a foliated zero-set hierarchy: q vanishes only at Γ (Bloch triplet), e₂-type shapes vanish on axes (sheet states, O(L) degeneracy), e₃/q vanishes on planes (tube states, O(L²)), and full flatness gives O(L³). The earlier two-shape ansatz and the tube attribution to f_co are **rejected**; cubic covariance kills the isolated f_dif direction. The boundary ideal I_∂ = {ÑBÑ†} is the correct all-orders algebraic object; the all-orders survival question is the decisive Open computation for SU(3).

**SU(4) fourth-order exceptional completion (Proven, exact arithmetic).** The complete SU(4) fourth-order one-flux T₁⁺⁻ dispersion is closed: exceptional (N-ality) channels shift the flat branch by the exact scalar Δq₄ = −304746539168/160249753125 and contribute ΔA₄ = ΔB₄ = 0; the full coefficients are A₄ = 32/675 > 0 and B₄ > 0 (exact rationals in the certificate), with the parity identity c_R − 2c_M + c_X = 0. Because A₄, B₄ > 0, **the SU(4) fourth-order band is strictly dispersive** with unique minimum at Γ and maximum at R. This is the first complete fourth-order answer in the program and pre-answers, for rank four, the flat-band decision criterion: at fourth order, homological flatness does not survive at SU(4). The SU(3) O(y⁴) signed-corner computation (Priority 1 below) decides whether SU(3) behaves the same way or realizes one of the sheet/tube phases.

**Refined decision criterion.** Per the 07-25 audit, "no exact remnant survives" is too strong; the correct four-tier outcome ladder is: link factorization (whole band flat) → harmonic annihilation (band disperses, H₂ triplet pinned) → nonzero harmonic scalar (triplet shifts rigidly) → cubic-symmetry breaking (only then can T₁ split). The SU(4) result sits in the second/third tiers: the exceptional correction acts as a scalar on the flat branch while A₄, B₄ disperse it.

**Mobility and rank-cubic scaling.** t_N ∼ 1/(4N³) (Proven), W⁻_N/E_{F,N} ∼ 3y²/N⁴, and both formal descriptions select τ = β/N³ from opposite sides. The double-scaled crossover at β = N³τ remains a **matched-scaling target, Conjectural** — there is no overlap theorem. The shell-6 first-order C-odd ordering result and the shell-structure prediction stand as gate-backed finite computations feeding this pillar.

**Layer firewall (binding editorial theorem).** The 07-25 audit's central ruling is retained as policy: none of the Pillar I large-β local documents may be merged into the flat-band manuscript. Pillar I concerns the compact one-plaquette weak-well operator at large β; Pillar II concerns the full spatial KS Hamiltonian's one-excitation sector at small y. Source 13's "C-odd local gap" and the T₁⁺⁻ band are different objects with similar names. Unification in this record is structural, never a merger of asymptotics.

## 4. Pillar III — Conditional global Wilson projected-capacity program

The Proven conditional chain stands: free-energy stability ⇒ hard-defect Peierls bound ⇒ rooted capacity summability ⇒ local source stability, with the incidence-shadow capacity 0 ≤ K ≤ 1 and single rooted mark e^{sγ} canonical. The Bernoulli fixed-density no-go is Proven; its correlated Wilson analogue remains Conjectural/Open; the global fixed-window firewall stays rejected.

**Sharpened since 07-13:** the incidence constant improves 24 → 16 = 4d, and this is now **Proven by a one-line lemma** (B_Γ B_Γ* is PSD, supported on C(Γ), norm ≤ ‖B‖² = 4d; Loewner order survives conjugation by P), verified with slack ≥ −5×10⁻¹⁶ on four geometries at L = 4. The measured capacity-ratio cushion (≤ 0.036 raw, ≤ 0.125 sharply normalized — an 8–30× margin) is the relevant budget input for the Program B arithmetic that previously failed by ∼10⁻⁴. The next result that materially advances this pillar is unchanged: a sharp proof or falsification of an (ML)-type Wilson tail bound, not another fixed-grid run.

## 5. Pillar IV — Seam and singularity theory (new pillar)

This is the corpus's principal analytic advance since 07-13 and completes the program's own stated open target ("kill the seam").

**Exceptional-point atlas (CV, branch-identified, K-stable to 14 digits).** The low-lying singularities of both exact gap towers are level-collision exceptional points. C-even: E₂↔E₃ at |β| = 0.364, E₄↔E₅ at 0.925, **E₀↔E₁ (vacuum–gap) at β_c = 0.7978428285 + 1.3893517794 i, |β_c| = 1.6021, arg 60.13°**, E₁↔E₂ at **2.4245∠159.8°**, E₃↔E₄ at 2.709. C-odd: O₂↔O₃ at 0.939, O₄↔O₅ at 1.691, O₀↔O₁ at 3.143. Three independent consistency checks pin the vacuum–gap EP: the level-repulsion minimum near β ≈ 0.8, the period-6 sign pattern of b₁…b₆ predicting a 60° conjugate pair, and the empirical seam (1.5, 2.5) bracketing |β_c| = 1.602.

**Structure theorem for the odd sector (new; machine-verified).** Because the dominant singularity is a vacuum–gap collision, Δ⁺² is a symmetric function of the colliding pair and hence analytic at β_c; and with G := O₀ − (E₀+E₁)/2,

Δ⁻(β) = G(β) + ½ Δ⁺(β), with G analytic on |β| < 2.4245.

Verified branch-cancellation ratio 2.0×10⁻⁴ at β_c; anchors G(0) = 1/3, G′(0) = 1/4. Consequence: one Theorem-4.2-style representation of (Δ⁺)² plus one ordinary representation of G gives certified two-sided control of **both** sectors across the entire seam. This retro-explains the manuscript's own empirical hierarchy — the squared-gap closure reaches 9.5×10⁻⁴ while every pole-free Padé of Δ⁺ stalls at 6.1×10⁻²; squaring removes the branch points, and 2.4245 (the E₁↔E₂ collision at negative coupling) is the hard analytic ceiling of that route.

**Physical-channel continuity (CV).** The single compact operator O⁻ = Im χ₍₁,₀₎ retains ≥ 97.4% spectral weight on the lowest C-odd state over β ∈ [0, 3200]: the analytic continuation has a nearby singularity, yet the physical channel is tracked by one fixed operator straight through the seam.

**Certification status and lesson.** All of Pillar IV is currently a **locator, not a certificate** (five hard gates PASS; cutoff drift 1.7×10⁻¹⁴). Promotion requires Newton–Kantorovich or interval disks around the two governing EPs (1.6021 and 2.4245) and Kato-remainder envelopes on β ∈ [0.25, 50]. The v1 crossover build contributed a standing methodological rule: the maximal exactly-determined rational system can be formally solvable yet mutually inconsistent (84% error at [10/8]); **gate the fit residual, not just pole-freeness** (the consistent [8/6] system achieves residual 8×10⁻⁴).

**Thesis D (symmetric-function analyticity).** The general principle extracted for the theory: gap-function singularities in this program are eigenvalue collisions of a Kato-analytic family; symmetric functions of the colliding branches are analytic there; therefore certified crossovers exist for appropriately symmetrized objects, and the achievable certified accuracy is set by the *next* singularity layer, which the atlas now names.

## 6. Pillar V — Wilson–Bergman weight theory and the N-uniformity limitation (new pillar)

**Theorem F (Proven).** The Wilson–Bergman weight is an N×N Bessel–Toeplitz determinant: with ℓ = λ+ρ, κ = 2β/N,

w_λ(β) = c_N(β) Σ_{s∈ℤ} det[ I_{ℓ_a−ℓ_b+s}(κ) ],

verified to machine precision at N = 2–5 with spectral quadrature convergence. Corollary F1 gives the SU(2) closed form w_n = c[I₀(2β) − I_{2n+2}(2β)]; **Corollary F2 (Proven, sharp)** gives w_{n+k}/w_n ≤ (k+1)², so at quartic bandwidth √(w′/w) ≤ 5 — the SU(2) toy's measured "O(1) shifted-norm ratios" is now a proven bound with exact constant; Corollary F3 gives the (dim λ/dim μ)² large-β limit with a genuine O(1/β) Laplace correction.

**Theorem H (CV).** The rank-general transfer tail T_N is finite and chamber-uniform at every fixed N tested (N = 2–6), β-stable, killing obstruction (v) at each fixed rank — but its constant grows as **Θ(N³)** (fitted exponent 3.04), pinned to (1.28–1.48)·q(1)/N = (1.28–1.48)·(2N)⁴/N, i.e., explained by row sum (2N)^k × Θ(N) Casimir denominator × O(1) weight ratios rather than merely fitted. Honest scope: T is a Schur sufficient condition; Θ(N³) growth kills this route to an N-uniform constant but does not prove no N-uniform estimate exists — a true limitation theorem needs a lower bound on the actual resolvent tail.

**Two exact non-uniformity mechanisms.** The CDG transplant gives a radial mechanism (certificate degree must grow like c*N² with c* = (π−2)²/8π); Theorem H gives a transfer mechanism (Θ(N³)). They are distinct, they are both exact rates, and they jointly reinforce the ledger's standing conclusion: fixed-rank theorems exist, N-uniform ones do not — now quantitatively. The chamber-stencil note's "correct N-uniform statement ‖M_q/q(1)‖ = 1" is **withdrawn** as true-but-useless (a normalization, not a bound) and replaced by Theorem H. Practical yield: shell-K transfer estimates may legitimately use λ_max(K) (1208 at K = 24) instead of (2N)^k (1296).

## 7. Pillar VI — Euclidean Monte Carlo physical layer

The hardened SU(3) T₁⁺⁻ pipeline (checkerboard SU(2)-subgroup Metropolis + over-relaxation, APE smearing, GEVP, blocked bootstrap, torelon scale, replay gate against Athenodorou–Teper arXiv:2007.06422) carries exact topology certificates as hard gates: d₂d₃ = 0, b₂ = 3 harmonic planes, cube boundary is A₁^{−−} with no k = 0 carrier while the H₂ plane triplet is T₁⁺⁻ — the Pillar II kinematics verified inside the sampling code itself.

**Validated physics run (CV; recorded in `SOURCEOFGOD.txt`).** On the published 14³×16 volume and coupling, all 23 pre-registered hard gates passed with zero warnings: aM(T₁⁺⁻) = 1.6897 ± 0.121 vs published 1.591(18) (pull +0.82), string scale agreeing at +0.71σ, error shrunk 10.8× from the pilot (whitener conditioning 7.97×10³ under its 10⁴ spec). First like-for-like attempt, first agreement; the campaign over the six continuum ensembles is green-lit at measured throughput 7.1×10⁵ site-sweeps/s.

**The scientifically loaded number.** The raw ImTr plaquette carries 0.0072 ± 0.0165 — i.e., < 4% at 2σ — of the physical T₁⁺⁻ state, versus ≥ 97% weight of O⁻ on the lowest C-odd state in the one-plaquette Hilbert space (Pillar IV continuity result). The physical state is extended (smeared-basis coupling 0.80). This converts the program's scope firewall — a local class gap is not a physical glueball mass; the operator bridge Im Tr e^{iX} = −Tr X³/6 + … is an identity whose physical completion runs through smearing — from a precaution into a **measured fact**, and it belongs in the manuscript's §8. Cheap follow-up: raw fraction vs APE level to map the overlap flow.

## 8. Conflict and supersession register (changes since 2026-07-13)

| Prior statement | Disposition | Replacement |
|---|---|---|
| 07-13 strengthened-theory record as top synthesis | Superseded | This record |
| Seam-results conjecture: second singularity layer "strictly farther out," right half-plane | Superseded | Atlas: governing E₁↔E₂ EP at 2.4245∠159.8° (negative-Re side); small-radius E₂↔E₃ (0.364) and O₂↔O₃ (0.939) collisions are irrelevant to the gap functions but fatal to effective models carrying E₂/O₂ explicitly |
| Chamber-stencil §6: N-uniform ‖M_q/q(1)‖ = 1 | Withdrawn | Theorem H: transfer constant Θ(N³) |
| SU(2) toy: measured O(1) shifted-norm ratios | Upgraded | Proven sharp bound (k+1)² (Corollary F2) |
| Two-shape fourth-order ansatz; f_dif as cubic scalar; f_co tube phase | Rejected | Four-dimensional orbit-resolved shape space; f_dif non-covariant (γ = 0 under cubic symmetry); f_co → sheets, e₃/q → tubes |
| Raw flat degeneracy L³+2 read as b₂; nonzero index protection | Rejected | L³+2 = rank ∂₃ + b₂; index is zero |
| Flat-band criterion "no exact remnant survives" | Refined | Four-tier ladder (link factorization / harmonic annihilation / harmonic scalar / symmetry breaking) |
| Incidence Loewner constant 24 (audit-only) | Sharpened | 16 = 4d, one-line Proven lemma, measured 8–30× cushion |
| SU(4) fourth-order flat-band fate unknown | Closed | Strictly dispersive; exact (q₄, A₄, B₄), exceptional scalar shift, parity identity c_R − 2c_M + c_X = 0 |
| Crossover fits gated only on pole-freeness | Corrected | Residual-and-conditioning gate mandatory (v1 failure mode: 84% error from a solvable but inconsistent [10/8] system) |
| One-plaquette operator presumed to dominate physical overlap | Measured | Raw fraction < 4% (2σ); physical state extended; bridge remains an exact operator identity |

## 9. Unifying theses (current form)

**A. Gauge-constrained spectral geometry** (retained). Internal Lie geometry sets local stiffness; spatial chain-complex geometry sets mobility; exact marginalization sets how much protection survives coupling to unresolved sectors. Kernel–resolvent duality of d₁ remains the exact structural bridge.

**B. Filtered spectral escape** (retained, extended). Identify a filtration, prove rigidity inside it, compute the first escaped coefficient exactly. Instances: radial algebra ℝ[p₂] escaped at β^{−1/2} by √6/576; incidence ideal escaped at O(u⁴); and now, for SU(4), the boundary ideal escaped at fourth order by the exact pair (A₄, B₄) with the exceptional sector remaining inside (scalar shift only).

**C. The rank-cubic law** (new; Conjectural as a single mechanism, exact in each instance). N³ is the recurring scale: t_N ∼ 1/(4N³) (Proven), ordering threshold β ≫ N³ and matched-scaling variable τ = β/N³ (exact on both sides, crossover Conjectural), transfer constant Θ(N³) (CV, mechanism explained). The working conjecture is that one rank-cubic mobility/transfer scale governs the reorganization between rank-suppressed homological dynamics and rank-growing local Weyl dynamics. A theorem requires a rank-uniform resolvent limit in τ — not substitution into either fixed-regime series — and Pillar V's exact rates now say any such theorem cannot be reached through the Schur-transfer or fixed-degree-certificate routes.

**D. Symmetric-function analyticity** (new). Gap singularities are exceptional-point collisions; symmetric functions of colliding pairs are analytic; certified crossovers therefore exist for symmetrized objects, with radius set by the next collision layer. The odd-sector structure theorem Δ⁻ = G + ½Δ⁺ is the first exact instance, and it reduces certified two-sided control of both sectors to two analytic representations on |β| < 2.4245.

**E. Layer separation.** The unification is structural. Pillars I, II, III, and VI concern different operators, regimes, and evidentiary layers; the theory's strength is that it names exact bridges between them (the incidence factorization, the operator-continuity result, the τ variable, the MC hard-gate embedding of the homological kinematics) without ever merging their asymptotics.

## 10. Master open-problem ranking

1. **SU(3) O(y⁴) signed-corner operator** (Pillar II, decisive). Exact fourth-order effective matrix, channel separation, action on the wrapping sheets, bandwidth, and Γ shift, with the four-number (A,B,C,D) extraction pre-registered. SU(4)'s answer (dispersive) sharpens the stakes: does SU(3) follow, or realize a sheet/tube phase?
2. **EP certification and certified crossover** (Pillar IV). Newton–Kantorovich interval disks at 1.6021 and 2.4245; `seam_crossover_certificate.py` v2 with the conformal map adapted to the certified pair and Kato remainders; target certified two-sided envelopes on β ∈ [0.25, 50] at Theorem-4.2-class accuracy.
3. **Thermodynamic-limit gap theorem** (Direction 1 of the ten-proofs synthesis). Check Yarotsky/DFPR–Lie–Schwinger hypotheses against KS line-by-line (infinite-dimensional link space is the only nonstandard feature), run one block-diagonalization step with the word-calculus engine, and extract an explicit y₀; the exact rationals (−481/612, t₊ = −11/306, tromino vanishing, d₃) are the inputs that make the constants explicit. Also check whether Osterwalder–Seiler admits a transfer-matrix KS reading off the shelf.
4. **(ML)-type Wilson projected-capacity tail bound** (Pillar III). Still the single result that unlocks the conditional chain; the sharpened 16-constant and measured cushion re-price its budget.
5. **True N-uniform limitation theorem** (Pillar V). Lower-bound the actual resolvent tail, converting the Θ(N³) Schur growth and the c*N² CDG degree into a genuine no-go.
6. **SU(N) shared-link recoupling amplitudes** for the flat-band generalization (audit Priority 3): prove αI + βS structure before promoting the topology theorem beyond SU(3)/SU(4).
7. **Hedgehog π₂ charge at Γ** (audit §8): construct Q(k), fix the symmetry class, compute the invariant on a small S²; Open until the convention is checked; do not substitute a Chern number.
8. **MC campaign execution** (Pillar VI): the six continuum ensembles at the measured throughput; raw-fraction vs APE level; window-positivity and finite-volume gates as staged.
9. **Two-particle projected interaction program** (Pillar II §12): classify overlap geometries and compute V_proj on the smallest complete clusters before any use of "glueball crystal."
10. **One non-product topology** for the Betti theorem (audit Priority 4), and the Hamer-1989 1⁺⁻ series comparison with the five-row normalization checklist before any coefficient-novelty claim.

## 11. Scope firewall

Nothing in this record establishes or claims: a four-dimensional infinite-volume or continuum Yang–Mills mass gap; Osterwalder–Schrader reconstruction; a continuum glueball mass prediction; an all-orders localized physical particle; a Wilson area law; N-uniform versions of any fixed-rank theorem; or an overlap theorem between the strong-coupling and large-β expansions. The one-plaquette operator bridge is an exact identity whose physical completion is now measured to run through smearing (raw overlap < 4% at 2σ). All Monte Carlo results are numerical evidence at stated volumes and couplings, gated but not proofs.

---

*End of record. For exact constants, certificate hashes, and full dependency graphs, the scope-specific ledgers and certificate files remain controlling.*
