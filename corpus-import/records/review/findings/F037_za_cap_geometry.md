# F037 — Z.A cap-geometry: bare-cap curvature lemma proved; a real gap in the §9 incident reduction (June 12, 2026)

**Unit:** #58 (own-initiative analytic attack, Alex-directed "proceed" → Z.A, the agent-tractable half of M3a). **Verdict: genuine progress on Z.A's deterministic core — one lemma proved, one published reduction step refuted-and-fixed, one Laplace law certified.** Attacking the finite-dimensional spherical cap-geometry that §§8–9 of the SU(2) Lemma Q reduction (`programs/pmbsf/NOTE_PMBSF_lci_tosj_reduction_lemmaq_2026_05_26.md`) leave as *"a Laplace ratio estimate gives … under nondegenerate hypotheses"*, this pass: (1) **proves the bare-cap curvature lemma** `Δ_p = 2sin²δ ≥ χ₀²/2` with sharp constant `1/(2(1−c₀²))` (the explicit `c_curv` the reduction omits); (2) **exhibits a sampling-verified counterexample showing the reduction's incident-subset step (9.5) is FALSE** — the §9 good event, parametrized by `χ₀ = u_A·n_p − a`, does not control the cap ratio for `|A|≥1`; (3) **certifies the cap-ratio law's exponential rate** (8.4) `= Δ_p`. Constructive fix: parametrize the good event by the true height-drop `Δ_p(A)`, and re-point the existing diagnostic to measure it. Engine `programs/op1_defect_sparsity/za_cap_geometry/ENGINE_OP1_za_cert_v5.py`, gates **G-ZA1..G-ZA5 PASS**; note `NOTE_OP1_za_cap_geometry_2026-06-12.md`.

## 1. Context — where this sits in M3a

OP-1's stochastic half (S) = M3a = Theorems **Z.A** (LCI typicality) + **Z.B** (Bałaban far-source). The SU(2) reduction note proves LCI + far-source ⟹ TOS+J ⟹ Lemma Q (its §§2,3,7,11 are sound algebra/positivity) and reduces LCI itself to a finite-dimensional cap-geometry condition on vMF measures on S³ (§§8–9). That condition — the cap curvature bound (9.5) and the Laplace cap-ratio (8.4) — is stated without proof or constants. It is the agent-tractable deterministic core of Z.A; the residual stochastic typicality is the genuinely hard remainder. This finding closes the bare case, certifies the rate, and finds (and fixes) a gap in the incident case.

## 2. The bare-cap curvature lemma (PROVED)

For the target cap alone (A = ∅), vMF mean `m`, `c₀ = m·n_p`, gap `χ₀ = c₀ − a > 0`: `u_∅ = m`, `h(∅)=1`, `h({p}) = ac₀ + √((1−a²)(1−c₀²))`. Writing `a=cosα, c₀=cosβ` (`α>β`), `δ=(α−β)/2`, `σ=(α+β)/2`:

  **Δ_p = 1 − cos(α−β) = 2sin²δ,  χ₀ = 2 sinσ sinδ,  so χ₀²/2 = 2sin²σ sin²δ ≤ 2sin²δ = Δ_p**

(since `sin²σ ≤ 1`), with equality iff `α+β=π`. Leading order: `Δ_p → χ₀²/(2sin²σ) → χ₀²/(2(1−c₀²))`. This gives the explicit curvature constant **c_curv = 1/2** (universal) / **1/(2(1−c₀²))** (sharp) that (9.5) left as an unspecified symbol. **G-ZA1/G-ZA2:** closed form vs active-set solver **1.3e-15**; lower bound tight at **min ratio 0.50000**; leading constant reproduced to 1.6% in the asymptotic regime.

## 3. The incident step (9.5) is FALSE — counterexample

(9.5) claims `χ₀(A) ≥ χ₀* ⟹ Δ_p(A) ≥ c χ₀*²` for every incident subset `A`. **This fails.** Verified exhibit (G-ZA5, independently checked by 4×10⁶-point dense sphere sampling): `k=3` incident caps, `χ₀(A) = 0.192` (healthy gap at `u_A`), but the true drop `Δ_p(A) = 0.0025` (solver and sampling agree) vs `χ₀²/2 = 0.0184` — a **~7× shortfall**, ratio `0.0069 ≪ 1/2`. Valid-config violation rate **12%** (hardened solver, zero geometrically-inconsistent artifacts after the conditioning filter). **Mechanism:** `χ₀` measures only how far the single maximizer `u_A` lies outside `C_p`; with neighbor caps present, `C_A ∩ C_p` can retain an alternative near-maximal point (a different cap active), so adding `C_p` barely lowers the height. The bare cap has no alternative — which is exactly why §2's lemma holds there and only there.

**Constructive fix.** The cap ratio (8.4) is governed by the *height drop* `Δ_p(A)`, not `χ₀`. Restate the good event as `G_LCI' = { min_A Δ_p(A) ≥ Δ* }`, `Δ* ≳ Δ_q + (M logκ + O(1))/κ`. **Actionable for the program:** `programs/pmbsf/ENGINE_FLUX_lci_typicality_diagnostic.py` measures `min_A χ₀(A)`; it already computes `h(A)` and `h(A∪{p})` in its cap solver, so re-pointing it to report `Δ_p(A) = h(A) − h(A∪p)` is a one-line change and gives the geometrically correct typicality observable.

## 4. The cap-ratio law (8.4) — rate certified

`ν(C_p) = P_vMF(u·n_p ≤ a)` by exact 2-D vMF quadrature over `κ ∈ [60,700]`: the form `−log ν = κΔ_p − M logκ − log C_geom` fits with **max residual 0.005**, rate matches the proved `Δ_p` (G-ZA3: slopes 0.0810/0.0802 vs `Δ_p=0.0804`). Prefactor **M ≈ −1/2** (`ν ∼ κ^{+1/2} e^{−κΔ_p}`): the dominant Laplace point is the corner where the constraint meets the sphere-disk boundary and the fiber density `√(1−w²−y²)` vanishes — so the prefactor grows, a correction to the naive `κ^{M>0}` reading; harmless since only the rate is load-bearing.

## 5. Status / what remains of Z.A

**This pass settles:** the curvature constant (bare cap, sharp), the cap-ratio rate, and a correction to the published §9 reduction (the `χ₀ → Δ_p` substitution, with a verified counterexample). **Z.A remains open**, now sharpened to: with `G_LCI'` correctly stated via `Δ_p`, prove (i) the **multi-cap Laplace estimate (8.4) for `A≠∅`** with uniform prefactor over the ≤5 incident caps (agent-tractable next: the §2 rate method extends; the corner/uniformity needs the general argument), and (ii) the **stochastic typicality** of `min_A Δ_p(A) ≥ Δ*` under the heat-bath geometry (the genuinely probabilistic core, coupled to Z.B/Bałaban locality). No proved status elsewhere changes; (D) stays closed (F033). Grounds: §2 proof derived-and-machine-verified (1.3e-15); §3 sampling-verified counterexample; §4 exact-quadrature certificate; §5 residual labeled open.

## 6. Deposits

`programs/op1_defect_sparsity/za_cap_geometry/`: `ENGINE_OP1_za_cert_v5.py` (canonical, md5 8bc3d7e1) + `CERT_OP1_za_cap.json` (2c296c1e) + `NOTE_OP1_za_cap_geometry_2026-06-12.md` (a57e2ba9) + README + v1–v4 gated-iteration audit trail. Closure-plan M3a row gets a Z.A-progress addendum; pmbsf README notes the §9 correction + diagnostic re-point; STATE + SESSION_LOG + ledger #58 updated. Ledger count → 39/57 closed (36 DONE + 3 SKIP), F001–F037.
