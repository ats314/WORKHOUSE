# F040 — Z.A good-event margin vs L (vectorized heat-bath): the deterministic LCI good event stays weak through L=16; the weight is on Z.B (June 12, 2026)

**Unit:** #61 (own-initiative continuation, Alex "proceed in your best direction"). **Verdict: a sobering, honest L-scan — the corrected Z.A good event does NOT open up by L=16, so the LCI bound leans almost entirely on the rooted/Z.B machinery, not on a healthy deterministic good event.** F039 measured the corrected observable `min_A Δ_p` at L=4 and flagged "typicality may be a larger-L phenomenon." To test that, this pass builds and validates a **vectorized SU(2) exact heat-bath** (28× faster than the diagnostic's pure-Python version) and measures `min_A Δ_p` at L = 4, 8, 16 (β = 3.5, the Stage-B value). Result: the good-event fraction stays roughly **flat at ~0.12–0.18 across L** (the L=8 bump is single-config noise), with margins small at every size (median 0; the L=16 tail reaches only 0.07). So the deterministic LCI good event `G_LCI'` does not become typical by L=16 — the bad set stays ~85% — and the entire LCI bound rests on the rooted/absorbed complement carried by **Z.B (Bałaban far-source stability)**, which is load-bearing rather than complementary. Engines `ENGINE_PMBSF_su2_hb_v3.py` (vectorized heat-bath, gates G-HB1/G-HB2) + `ENGINE_OP1_za_dp_vsl.py` (gates G-DT1/G-DT2), all PASS.

## 1. The tool: a validated vectorized SU(2) heat-bath

To reach L=16 (256× the work of L=4) the diagnostic's per-link pure-Python heat-bath is too slow. I wrote a vectorized quaternion checkerboard heat-bath (`ENGINE_PMBSF_su2_hb_v3.py`): 8 sub-sweeps per sweep (direction μ × site parity), each fully vectorized via `np.roll`, with the staple **recomputed between parity updates** (the bug that an earlier version missed — reusing one staple for both parities breaks detailed balance and gave the wrong equilibrium plaquette 0.645 vs 0.778). Validation gates:
- **G-HB1:** the vectorized staple equals the diagnostic's `link_normals(...).sum()` to **6.7×10⁻¹⁶** (60 random links) — the geometry matches the reviewed code exactly.
- **G-HB2:** the L=4 equilibrium `⟨½ Re tr U_p⟩ = 0.778` reproduces the diagnostic's pure-Python heat-bath value 0.772 (|diff| 0.0065) at β=3.5.

Speed: L=4 80 sweeps in 0.53 s (vs 14.7 s); L=8 in 2.2 s; L=16 in ~39 s (chunked/resumable). Reusable for any future SU(2) Stage-B-scale work.

## 2. The L-scan (β = 3.5; 240 (e,p) records per L, one thermalized config each)

| L | ⟨½ReTr⟩ | κ_e median | frac(min_Δp > 0) | frac(min_Δp > 0.05) | max min_Δp | overstatement P(Δp<0.01 | χ₀>0.05) |
|---|---|---|---|---|---|---|
| 4 | 0.775 | 17.9 | 0.125 | 0.000 | ≤0.05 | 0.50 |
| 8 | 0.770 | 17.9 | 0.175 | 0.000 | 0.043 | 0.56 |
| 16 | 0.768 | 17.6 | 0.121 | 0.008 | 0.070 | 0.67 |

(Gates per L: G-DT1 — hardened solver, no impossible drops; G-DT2 — F037 bare-cap lemma holds on every record. Both PASS at all L.)

**Reading:**
- **The good-event fraction is roughly flat in L** at ~0.12–0.18. The L=8 value (0.175) is **not** a monotone trend — at L=16 it returns to 0.121. With ~240 correlated records from one config, the per-L sampling noise on a ~15% fraction is ≈ ±0.03–0.05, so 0.125 / 0.175 / 0.121 are mutually consistent. There is **no clear opening-up of the good event with L**.
- **Margins stay small at every L.** The median `min_Δp` is 0 at all sizes (≥83% of (e,p) have a worst-incident-subset drop of exactly zero). The only L-signal is a mild **tail extension**: max `min_Δp` grows 0.05 → 0.043 → 0.070 and the first nonzero `frac(>0.05)` appears at L=16 (0.008). The bulk is unchanged.
- κ_e ≈ 18 at all L (the one-link concentration is a local quantity, correctly L-independent).

## 3. What this means for Z.A and OP-1's (S)

`min_A Δ_p = 0` means there exists an incident subset A whose cap-maximizer already lies inside C_p, so `ν(C_p|C_A)` is O(1) and the LCI condition (6.3) `ν(C_p|C_A) ≤ C_LCI q` **fails for that A** — that (e,p) goes to the rooted/absorbed complement `Y_p^LCI = X_p·1_bad` (reduction §9.10). The scan shows this bad set is **~85% at every L ≤ 16** and does not shrink with L. Consequences, stated honestly:

1. **The deterministic LCI good event is not typical** at the tested parameters — it is a ~15% minority at all L. F039's tentative "typicality is a larger-L phenomenon" is **not borne out** by the L-scan: going to the Stage-B size L=16 does not make `G_LCI'` typical.
2. **The LCI bound therefore rests on the rooted complement + Z.B**, not on a healthy Z.A good event. Z.B (Bałaban far-source stability of the LCI parameters, reduction §10) is **load-bearing**, carrying ~85% of plaquettes, not a complement to a dominant good event. This relocates the weight of OP-1's (S) closure squarely onto Z.B.
3. **Caveat against over-pessimism.** The min-over-all-32-subsets is the *strictest* good-event measure (it asks whether *any* incident configuration frees X_p). The rooted sum (§7.4–7.6) weights bad subsets by the tilt `s^{|A|}` and the far-source structure; a large pointwise bad set does not by itself imply the rooted sum diverges. So this is **not** a disproof of Z.A — it is evidence that Z.A cannot be carried by the deterministic cap good event alone, and that the rooted/far-source layer is where the closure must come from. The reduction's architecture (rooting the bad part) is consistent with this; the scan quantifies that the bad part is the majority.

## 4. Status / scope

No proved status changes; F037 (bare-cap lemma), F038 (multi-cap rate = Δ_p, deterministic core complete) stand; (D) closed (F033). The new content: (i) a validated, fast vectorized SU(2) heat-bath (reusable tool); (ii) the corrected Z.A observable measured across L=4/8/16, showing the deterministic good event stays a ~15% minority with small margins through the Stage-B size; (iii) the resulting relocation of OP-1's (S) weight onto Z.B. **Grounds:** gated MC (evidence; single config per L ⟹ fractions carry ~±0.03–0.05 noise, but the qualitative picture — large bad set, small margins, weak L-dependence — is robust across three sizes and consistent with G-DT1/G-DT2 passing throughout). **For Alex:** the next refinement is more configs per L (to pin the fractions) and, more importantly, that the (S) closure question is now concretely **"does Z.B's far-source stability control an ~85% bad set?"** — the LCI cap geometry (Z.A's deterministic core, F037/F038) is settled and is not where the difficulty lives.

## 5. Deposits

`za_cap_geometry/`: `ENGINE_PMBSF_su2_hb_v3.py` (vectorized heat-bath, md5 bdf0e9ca; G-HB1/G-HB2) + `ENGINE_OP1_za_dp_vsl.py` (L-scan, md5 752418a8; resumable) + `vsL_result_L{8,16}.json` + state files + earlier iterations `ENGINE_OP1_su2_hb_vec.py`/`ENGINE_OP1_su2_hb_v2.py` (gated debugging: staple-convention then stale-staple bugs, both caught). Note `NOTE_OP1_za_cap_geometry_2026-06-12.md` §7; closure-plan Z.A ADDENDUM 4; pmbsf README. STATE + SESSION_LOG + ledger #61. Ledger count → 42/57 closed (39 DONE + 3 SKIP), F001–F040.

## 6. Re-verification (June 13, 2026, Alex "check this work again")

Independent re-run of every gate and the L-scan. **Headline conclusion CONFIRMED and, with better sampling, cleaner than the original table.** Specifics:

- **G-HB1 / G-HB2 reproduce exactly.** Vectorized staple = diagnostic to **6.66×10⁻¹⁶**; L=4 equilibrium plaquette 0.77839 (vec) vs 0.77187 (diag), |diff| 0.0065 < 0.015; timing 0.53 s vs 14.4 s ⇒ ~28×. The heat-bath tool is sound; the two-bug narrative (staple convention, then stale-staple-across-parities) checks out.
- **Defect 1 (FIXED): hardcoded stale session mount.** `ENGINE_PMBSF_su2_hb_v3.py` pinned `PMBSF` to a previous session's `/sessions/<id>/...` path, so the gates did not import in a fresh session. Re-pointed to a path relative to the file.
- **Defect 2 (FIXED): the per-L numbers were not reproducible.** `ENGINE_OP1_za_dp_vsl.py` reused the thermalization `rng` for the 40-link subsample (`rng.shuffle`). The stored results were produced with the rng advanced by 80 thermalization sweeps; resuming from the saved state skips those draws, so a *different* 40 links were selected and the stored fractions did not reproduce (L=8 came out 0.146, not 0.175; κ_median 17.88 vs 17.91 confirms a different link set). Fixed by using an independent seeded rng for the subsample.
- **Consequence for the table:** the §2 values are 40-link single-config subsamples and carry larger noise than even §2's own ±0.03–0.05 caveat implied — the **max-margin column in particular is an artifact** (a re-draw at L=8 gave max 0.137, exceeding every entry in the table). The "mild tail extension, max grows 0.05→0.07 with L" sub-claim is **retracted**: it is subsample noise, not an L-trend.
- **Qualitative conclusion robust under larger sampling.** Re-measured with 720 records (nlinks 120) per L on the same stored configs: **frac(min_Δp>0) = 0.156 (L=8), 0.158 (L=16)** — flat and nearly equal, median min_Δp = 0 throughout. This *strengthens* F040's core finding: the deterministic Z.A good event does not open up to typicality by L=16 (~84% bad set at all L), so the weight of OP-1's (S) closure sits on the rooted/Z.B layer. The original 0.125/0.175/0.121 should be read as ~0.15-flat; the L=8 "bump" was correctly flagged as noise in §2 and is confirmed to be so.

**Net:** the conclusion stands and is better-supported after re-sampling; it never depended on the noisy table values. Two reproducibility defects fixed; tool validated. The stored `vsL_result_L{8,16}.json` are retained as original-run artifacts but should be cited as ~0.15-flat, not at three-digit precision, and the max-margin column should not be cited.
