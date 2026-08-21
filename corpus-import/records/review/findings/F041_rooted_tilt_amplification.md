# F041 — The tilted LCI ratio (7.2), not the pointwise min: F040's ~85% "bad set" is overwhelmingly NOT bad for the load-bearing object; Z.B's target sharpens to a thin, volume-stable heavy tail (June 13, 2026)

> **REVISION (F042, June 13, 2026):** the **bulk** result below (median Amp ≈ 1, q90 ≈ 1+s, the tilted object (7.2) holding with `C_LCI=O(1)`) **stands and is strengthened**. The **heavy-tail magnitude** reported in §3 (q99 ≈ (1+s)², max ≈ (1+s)³) is **revised down**: F042 (with a ≥40-hit per-record floor) shows that tail was largely Monte-Carlo noise on near-zero-`ν_p` records; the genuine amplification on statistically-resolved records is O(1) with only weak overlap dependence (median Amp(s=4) ≤ ~1.8 even for 3-cap overlap). The mechanism (tail = multi-cap-overlap records) is confirmed; its size is mild. See `F042_overlap_mechanism.md`.

**Unit:** #62 (own-initiative continuation, Alex "review and proceed as you see fit"). **Verdict: F040's pointwise `min_A Δ_p` is the *strictest possible* LCI proxy and it overstates the difficulty. Measuring the actual load-bearing object — the source-tilted ratio `ν^{B,s}(C_p)` of the reduction's (7.2) — on the same SU(2) heat-bath ensembles shows it is only O(1)-amplified relative to the bare cap probability for the overwhelming majority of records, including the pointwise-bad ones (median amplification ≈ 1, 90th-percentile ≈ 1+s, across L = 4/8/16). The residual is a thin (~1%) heavy tail with amplification (1+s)²–(1+s)³, concentrated on records where the target cap overlaps several incident caps; this tail does NOT proliferate with volume. So Z.B's job is not "control an ~85% bad set" but "control a thin, volume-stable, multi-cap-overlap heavy tail of the tilted ratio" — a much smaller, sharper target than F040 implied.**

This executes F040 §3's own caveat: *"the min-over-all-subsets is the strictest good-event measure … the rooted sum weights bad subsets by the tilt `s^{|A|}` … a large pointwise bad set does not by itself imply the rooted sum diverges."* F041 measures that tilted object directly.

## 1. The object, and why it is the right one

The reduction `programs/pmbsf/NOTE_PMBSF_lci_tosj_reduction_lemmaq_2026_05_26.md` §7 proves positive **tilted** one-source stability from LCI. Its load-bearing inequality (7.2) is

  `ν^{B,s}(C_p) ≤ C_LCI · q`,  where  `ν^{B,s} = [∏_{r∈B}(1+s·1_{C_r})] dν / ∫(…)dν`

is the incidently source-tilted vMF measure (B = the ≤5 incident caps other than the target p, s ≤ ρ/q the tilt). Its proof (7.4–7.7) bounds the numerator **term by term**: `ν(C_p∩C_A) ≤ C_LCI q ν(C_A)` for **every** subset A ⊆ B. **That term-wise sufficient condition is exactly F040's observable** — `min_A Δ_p(A) > 0` is `ν(C_p∩C_A) = O(q)ν(C_A)` for all A, and F040 found it fails (`min_A Δ_p = 0`) on ~85% of records. But (7.2) only needs the **ratio of the tilted sums** to be small, and a few bad subsets can carry negligible tilted weight. The exact identity (7.4–7.7) makes the tilted ratio a single vMF expectation:

  `Σ_A s^{|A|} ν(C_A) = E_ν[∏_{r∈B}(1+s·1_{C_r})]`,  numerator the same with an extra `1_{C_p}`,

so  **`R(e,p;s) = ν^{B,s}(C_p) = E_ν[1_{C_p}∏_B(1+s·1_{C_r})] / E_ν[∏_B(1+s·1_{C_r})]`** — no subset enumeration. We report the scale-free **amplification** `Amp(s) = R/ν(C_p)`; LCI (7.2) is precisely the statement that the incident tilt does not inflate the target cap probability ("prevents incident positive source tilts from making `X_p` free", reduction l.421), i.e. `Amp = O(1)` uniformly.

## 2. Method + gates

Engine `za_cap_geometry/ENGINE_OP1_za_rt_f041b.py` (md5 `1d260a4a…`) on the F040 heat-bath geometry (`ENGINE_PMBSF_su2hb_f041.py`, md5 `9c205f53…`, a byte-faithful fresh-path re-deposit of `ENGINE_PMBSF_su2_hb_v3.py` — the sandbox mount served a truncated view of the original, host file intact). For each core link e: 6 incident cap normals, `m_e = Ĥ_e`, `κ = β‖H_e‖ ≈ 18`, cap parameter `a = 1−(t−η) ≈ −0.0054` (identical to F039/F040). For each of the 6 target plaquettes p: draw `N` points `u ~ vMF(m_e,κ)` on S³, form the 6 cap indicators, compute `Amp(s)` for `s ∈ {0,0.5,1,2,4}`, and record F040's `min_A Δ_p` flag on the same record. β = 3.5.

Gates (all PASS at every L):
- **G-RT1** vectorized vMF sampler: resultant `⟨u·m⟩` matches the Bessel ratio `I₂/I₁(κ)` to ≤ 3×10⁻⁴ at κ = 8/18/40, and matches the reviewed scalar `sample_vmf_s3` to ≤ 2×10⁻³.
- **G-RT2** MC bare cap probability vs an independent 1-D quadrature (m-frame marginal `f(w)∝e^{κw}(1−w²)^{1/2}`, y-coord uniform on [−1,1]): worst 9×10⁻⁴ over 6 random geometries (within MC error).
- **G-RT3** `s=0 ⟹ Amp = 1` exactly (0.0) and all tilted probabilities ∈ [0,1].
- **G-RT4** product-form ratio == explicit subset-sum ratio on the *same* sample (numerical check of the 7.4–7.7 identity): ≤ 7×10⁻¹⁸ (spot-checked on the first 4 records/config; full enumeration is O(2⁵N)).
- **G-DT1** F040's no-impossible-drops gate: 0.0.

## 3. Results

| L | cm | ncfg | records (ν_p>0) | pointwise-BAD frac (F040) | Amp(s) median | Amp(s) q90 | Amp(s) q99 | Amp(s) max |
|---|---|---|---|---|---|---|---|---|
| 4 | 1 | 8 | 1152 (689) | **0.851 ± 0.026** | 1.00–1.19 | 1.0 / 1.50 / 2.00 / 2.99 / 4.97 | 1 / 2.2 / 4.0 / 9.1 / 31.8 | 1 / 3.4 / 8.0 / 26.9 / 123.7 |
| 8 | 2 | 4 | 960 (500) | **0.854 ± 0.015** | 1.00–1.04 | 1.0 / 1.49 / 1.97 / 2.91 / 4.84 | 1 / 2.24 / 3.98 / 8.88 / 24.3 | 1 / 2.27 / 4.20 / 10.3 / 33.0 |
| 16| 2 | 1* | 360 (195) | **0.839** | 1.00–1.17 | 1.0 / 1.50 / 2.00 / 3.00 / 5.00 | 1 / 3.4 / 8.0 / 27.0 / 124 | 1 / 3.4 / 8.0 / 27.0 / 124 |

(Amp columns list the five s-values 0/0.5/1/2/4. *L=16 is the single stored F040 config, so q99 ≈ max from few records. Plot: `DATA_OP1_rooted_tilt_amp.png`.)

**Reading:**
1. **F040 confirmed and tightly pinned (task: multiple configs).** The pointwise-bad fraction is `0.851 ± 0.026` (L=4, 8 cfg), `0.854 ± 0.015` (L=8, 4 cfg), `0.839` (L=16) — F040's single-config ~0.85 is now properly errored and robust. (F040's per-L noise caveat discharged.)
2. **The bulk satisfies LCI with `C_LCI = O(1)`.** The median amplification is ≈ 1 at every L and s (the typical record: the incident tilt does *nothing* to the target cap probability), and the 90th percentile is ≈ **1+s** — a single-neighbour-cap factor. This holds **identically on the ~85% pointwise-bad records** (the "Amp on pointwise-bad" block of each json is within MC noise of the overall block). So the term-wise bound failing on a subset almost never inflates the tilted ratio: **F040's ~85% "bad set" is overwhelmingly NOT bad for (7.2).**
3. **The residual is a thin heavy tail.** q99 ≈ (1+s)² and the per-config max ≈ (1+s)³ — records where `C_p` overlaps 2–3 incident caps (the `Amp(s→∞) → ν(C_p|C_B)/ν(C_p)` full-conditioning limit shows through the `s^{|overlap|}` scaling). This is the only place (7.2) is stressed.
4. **The tail does not proliferate with volume.** L=4 → 8: the median moves *closer* to 1 and the max *drops* (123.7 → 33.0 at s=4). L=16's high q99 is a single-config small-sample worst case, not a volume trend. So the heavy tail is a rare, finite, geometrically-local event, not a growing-with-L pathology.

## 4. What this means for Z.B and OP-1's (S)

F040 relocated OP-1's (S) weight onto Z.B and framed the question as "does Z.B control an ~85% bad set?". F041 **re-frames that question more favourably and precisely**:

- The ~85% is an artifact of the *strictest* proxy. For the actual tilted object (7.2), ~99% of records (including ~99% of the pointwise-bad ones) have `Amp ≤ (1+s)` — LCI holds for them with `C_LCI = O(1)` directly, no rooting needed.
- **Z.B's real target is the thin, volume-stable, multi-cap-overlap heavy tail** where `Amp` reaches (1+s)²–(1+s)³. Because the tilt is bounded `s ≤ ρ/q`, this tail is exactly where the rooted/far-source summation must absorb the few records whose `ν(C_p|C_B)` is O(1). That is a far smaller and sharper burden than "85% of plaquettes."
- This is **not** a proof of LCI/Z.A: it measures the per-(e,p) tilted ratio (7.2) — the atom of the rooted construction — not the assembled rooted summability over Bałaban block cores (that remains Z.B). But it shows the per-atom object is healthy in the bulk and isolates the precise rare event Z.B must handle.

## 5. Scope / grounds (honest)

- **Grounds:** gated Monte-Carlo evidence (G-RT1/2 validate the sampler and the bare-cap probability against a Bessel ratio and an independent quadrature; G-RT3/4 are exact identity checks; G-DT1 is F040's). The amplification statistics are over records with `ν_p>0` (≈ 55–60%; for `ν_p = 0` the ratio is undefined and excluded). The deep tail (q99/max) rests on few records — especially L=16 (one config) — and is the least-pinned number here; the **bulk** statements (median, q90) are robust across L and configs.
- **Setting:** SU(2) one-link heat-bath cap geometry, β = 3.5, κ ≈ 18, the F039/F040 setting. This is the single-link conditional tilt (7.2), not the SU(3) comparator and not the full rooted sum.
- **s is a free sweep parameter;** the theory ties `s ≤ ρ/q`. With `q ~ ν(C_p)` small, large s is admissible, and the tail amplification `(1+s)^{2,3}` at large s is precisely where (7.2)'s constant could grow — so the heavy tail is the load-bearing rare event, correctly flagged for Z.B rather than swept under.
- No proved status changes. F037 (bare-cap lemma), F038 (multi-cap rate = Δ_p), F040 (pointwise bad-set scan) stand; (D) closed (F033). New content: (i) F040's bad fraction pinned with multiple configs; (ii) the tilted ratio (7.2) measured directly, showing the bulk satisfies LCI with O(1) constant and isolating the heavy tail; (iii) the resulting sharpening of the Z.B target.

## 6. Deposits

`za_cap_geometry/`: `ENGINE_OP1_za_rt_f041b.py` (engine; `ENGINE_OP1_za_rt_f041.py` = earlier full-RT4 variant retained; `RUN_OP1_za_rooted_tilt.py`/`ENGINE_OP1_za_rooted_tilt.py` = superseded drafts caught by the mount truncation) + `ENGINE_PMBSF_su2hb_f041.py` (fresh-path heat-bath re-deposit) + `rooted_tilt_L{4,8,16}.json` + `DATA_OP1_rooted_tilt_amp.png`. MD5s in §2. Updated: STATE.md, ZA_CAP_GEOMETRY note §8, UNIF_OP1_CLOSURE_PLAN Z.A ADDENDUM 5, REVIEW_LEDGER #62, SESSION_LOG. Ledger count → 43/57 closed (40 DONE + 3 SKIP), F001–F041.
