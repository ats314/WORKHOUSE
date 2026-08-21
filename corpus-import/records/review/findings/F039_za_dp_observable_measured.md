# F039 — The corrected Z.A observable min_A Δ_p measured on the heat-bath ensemble: χ₀ overstates the margin; typicality must come from larger L (June 12, 2026)

**Unit:** #60 (own-initiative continuation of F037/F038, Alex "proceed as you see fit"). **Verdict: first measurement of the corrected Z.A good-event observable on a real SU(2) Wilson exact-heat-bath ensemble — evidence-grade, two hard gates pass.** F038 reduced Z.A to the single typicality statement `G_LCI' = {min_A Δ_p(A) ≥ Δ_q + O(logκ/κ)}` P-typically. The deposited diagnostic `ENGINE_FLUX_lci_typicality_diagnostic.py` measures the *old* observable `min_A χ₀(A) = min_A (u_A·n_p − a)`, which F037 showed overstates the good event. This pass measures the *correct* observable `min_A Δ_p(A) = min_A [h(A) − h(A∪{p})]` on the same heat-bath geometry (β = 3.5, the Stage-B value), with the hardened cap solver. Result: the two observables **agree on whether the good event holds** (12.5% of (e,p) at L=4) but the corrected Δ_p shows the **margin is much smaller** — among (e,p) "comfortably good" under χ₀ (>0.05), **half are Δ_p-marginal (<0.01)** — so at L=4/κ≈18 the strict G_LCI' good event is essentially empty, and Z.A's typicality (if true) must live at larger L plus the rooted/Z.B machinery, not in pointwise L=4 goodness. Engine `programs/op1_defect_sparsity/za_cap_geometry/ENGINE_OP1_za_dp_v3.py`, gates **G-DT1, G-DT2 PASS**.

## 1. What was measured

For an SU(2) Wilson config thermalized by exact heat-bath (β = 3.5, L = 4, ⟨½ Re tr U_p⟩ = 0.775 after 50 sweeps), and each (core link e, target plaquette p), the one-link conditional law is vMF(m_e, κ_e) with κ_e = β‖H_e‖; the 6 plaquettes through e give caps `C_r = {u·n_r ≤ a}`, a = 1−(t−η) = −0.0054 (the diagnostic's defaults). For each (e, p) we compute over all subsets A of the 5 neighbor caps:
- **old:** `min_A χ₀(A)`, χ₀(A) = u_A·n_p − a (the diagnostic's observable);
- **new:** `min_A Δ_p(A)`, Δ_p(A) = h(A) − h(A∪{p}) (the observable F038 proved governs the cap ratio).

144 (e,p) records (24 core links × 6 targets, one config). **Gates:** G-DT1 — the hardened cap solver produces **no geometrically-impossible negative drops** on real data (the conditioning filter works on the heat-bath geometry); G-DT2 — F037's **bare-cap lemma Δ_p(∅) ≥ χ₀(∅)²/2 holds on every record** (the proved inequality survives on the actual ensemble).

## 2. Results

| quantity | value (L=4, β=3.5) |
|---|---|
| κ_e (heat-bath concentration) | median 17.9, [q05 15.5, q95 19.4] |
| `min_A χ₀` | median −0.216; frac > 0 = **0.125**; > 0.05 = 0.069; > 0.10 = 0.062 |
| `min_A Δ_p` | median 0.000; frac > 0 = **0.125**; > 0.05 = **0.000**; > 0.10 = 0.000 |
| overstatement | **P(min_Δp < 0.01 | min_χ₀ > 0.05) = 0.50** |

**Two readings:**

1. **The good-event *fraction* is identical (0.125) under both observables** — and this is exact, not coincidence: `min_A Δ_p > 0 ⟺ all χ₀(A) > 0 ⟺ min_A χ₀ > 0` (Δ_p(A) > 0 ⟺ u_A ∉ C_p ⟺ χ₀(A) > 0). So χ₀ is a valid **yes/no** indicator of the good event. F037's correction is **not** that χ₀ gets the sign wrong; it is that χ₀ gets the **margin** wrong.

2. **The margin is much smaller under the correct observable.** `min_A χ₀` reaches > 0.10 (6.2% of records), but `min_A Δ_p` never exceeds 0.05 — and among the χ₀-comfortably-good records (min_χ₀ > 0.05), **half have min_Δp < 0.01**. The χ₀ criterion systematically overstates how far the good event clears, exactly as F037 predicted and now quantified on real data.

## 3. Consequence for Z.A typicality

G_LCI' requires `min_A Δ_p(A) ≥ Δ_q + O(logκ/κ)`. At these parameters κ ≈ 18 so `O(logκ/κ) ≈ 2.9/18 ≈ 0.16`, and Δ_q > 0 (the rare-source scale). But `min_A Δ_p ≤ 0.05` for **every** record and = 0 for 87.5% of them. So with any realistic threshold the strict good event is **essentially empty at L = 4** — almost everything falls to the **rooted/absorbed complement** (Y_p^LCI = X_p·1_bad), which is precisely the part of the reduction (§9.10, §11) designed to carry the bad event via Bałaban far-source stability (Z.B). **This does not refute Z.A:** at L = 4 the cap geometry is maximally constrained (every plaquette through a link shares links with the others), so small Δ_p margins are expected; the program's own Stage-B plausibility (median Λ ≈ 1.016) was at **L = 16**. The finding is a *steer*: the corrected observable shows Z.A's typicality, if it holds, is a **larger-L / rooted** phenomenon, and the small-margin structure at L=4 means the deterministic good event alone cannot carry it — Z.B (far-source) is load-bearing, not optional.

**Actionable:** run this Δ_p measurement at L = 16 (the Stage-B size; the geometry decorrelates and margins should open). The engine here is L-agnostic — only the thermalization cost scales — so an L=16 run (chunked heat-bath) is the direct next experiment, and it would give the first real evidence on whether `min_A Δ_p` clears a Δ_q-scale threshold typically.

## 4. Status / scope

Evidence-grade (MC on one thermalized L=4 config); the two gates (solver validity, bare-cap lemma) are hard and pass. No proved status changes; (D) closed (F033); the F037/F038 analytic results stand. The new content: (i) the corrected observable is now measurable and measured; (ii) χ₀'s margin-overstatement is quantified on real data (50% of χ₀-good cases are Δ_p-marginal); (iii) the L=4 picture localizes Z.A's typicality to larger L + the rooted/Z.B layer. Caveat: L=4 is small and the local cap geometry, while a per-link object, is most constrained there — the L=16 run is needed before any typicality verdict. Grounds: gated MC (evidence); the fraction-equivalence min_Δp>0 ⟺ min_χ₀>0 is exact (proof in §2); the typicality reading is interpretation, labeled.

## 5. Deposits

`za_cap_geometry/`: `ENGINE_OP1_za_dp_v3.py` (canonical, md5 ff1df2cc) + `CERT_OP1_za_dp_typicality.json` (fc62f3b3) + `ENGINE_OP1_za_dp_v2.py` (iteration: dropped the wrong G-DT3 pointwise-ordering gate). Note `NOTE_OP1_za_cap_geometry_2026-06-12.md` §6 (observable measured); closure-plan Z.A ADDENDUM 3; pmbsf README (diagnostic re-point now executed + the L=16 next-run). STATE + SESSION_LOG + ledger #60. Ledger count → 41/57 closed (38 DONE + 3 SKIP), F001–F039.
