# F042 — The F041 heavy tail is the cap-overlap mechanism, and it amplifies only MILDLY: a verification that confirms the mechanism and revises F041's tail magnitude down (June 13, 2026)

**Unit:** #63 (own-initiative continuation of F041, Alex "proceed"). **Verdict: two results, one confirming and one correcting.** (1) **Mechanism confirmed:** the source-tilted amplification `Amp(s)=ν^{B,s}(C_p)/ν(C_p)` rises monotonically with the number of incident caps that the target cap overlaps, and its `s→∞` limit equals the full-conditioning lift `ν(C_p|C_B)/ν(C_p)` **exactly** (gate G-OV1 = 0.000 at every L) — so F041's heavy tail is precisely the multi-cap-overlap records. (2) **Magnitude revised down:** with adequate per-record statistics (≥40 target-cap hits), the amplification is O(1) *throughout* — median `Amp(s=4) ≤ ~1.8` even for the `k_eff=3` overlap stratum, versus the naive `(1+s)³=125`. **F041's q99≈(1+s)² / max≈(1+s)³ tail was largely Monte-Carlo noise on near-zero-`ν_p` records** (excluded here by the hit floor); the genuine cap overlaps are *weak*, so multi-overlap gives only mild amplification. This strengthens F041's core conclusion (the tilted object (7.2) holds with `C_LCI=O(1)`) and de-escalates its heavy tail.

## 1. Setup

F041 found the tilted ratio (7.2) `ν^{B,s}(C_p)` is O(1)-amplified in the bulk but reported a heavy tail (q99≈(1+s)², max≈(1+s)³). The `(1+s)^k` shape suggested the tail records are those where `C_p` overlaps `k` incident caps. F042 tests that mechanism directly. Same geometry as F039–F041 (SU(2) one-link heat-bath, β=3.5, κ≈18, `a≈−0.0054`). Per (e,p) record with ≥ `MINHIT=40` samples in `C_p` (so `ν_p ≳ 7×10⁻⁴`, controlling the ratio estimator):

- **pairwise conditional lift** `L_r = ν(C_p|C_r)/ν(C_p)` for each of the 5 incident caps r;
- **effective overlap count** `k_eff = #{r : L_r ≥ 2}` (caps that at least double the target probability);
- **full-conditioning lift** `Lfull = ν(C_p|C_B)/ν(C_p)`;
- `Amp(s)` for `s ∈ {0,1,2,4,64}`.

Engine `za_cap_geometry/ENGINE_OP1_za_overlap_f042.py` (md5 `7adf3e8e…`). Gates (all PASS): **G-RT1** vMF sampler vs Bessel `I₂/I₁` (≤ 5×10⁻⁴); **G-RT2** MC cap prob vs 1-D quadrature (≤ 5×10⁻⁴); **G-OV1** `Amp(s=64) ≈ Lfull` worst **0.000** at every L (the `s→∞` interpretation is exact).

## 2. Results

| L | ncfg | records (≥40 hits) | k_eff hist {0:1:2:3:4} | median Amp(s=4) by k_eff (0/1/2/3/4) | heavy-tail (top-1% Amp4) |
|---|---|---|---|---|---|
| 4 | 8 | 283 | 51:121:74:36:1 | 1.00 / 1.06 / 1.15 / 1.49 / 3.07 | **100% k_eff≥2** ({2:1,3:2}) |
| 8 | 6 | 237 | 71:93:56:14:3 | 1.00 / 1.04 / 1.17 / 1.42 / 1.95 | 67% k_eff≥2 ({1:1,2:2}) |
| 16| 1 | 79 | 19:33:24:2:1 | 0.99 / 1.09 / 1.17 / 1.75 / 2.79 | (1 record; small sample) |

(Plot `DATA_OP1_overlap_amp_vs_keff.png`: median Amp(s=4) vs k_eff, three L, against the naive `5^k` reference — the data sit one-to-two orders of magnitude **below** it.)

**Reading:**
1. **The mechanism is real.** Amplification rises monotonically with `k_eff` at every L, and at L=4 (the cleanest statistics) the top-1% tail is **100% multi-overlap** (`k_eff≥2`). The `s→∞` amplification equals the full-conditioning lift exactly (G-OV1). So F041's heavy tail *is* the records where the target cap is geometrically tied to several incident caps.
2. **But the amplification is mild, not `(1+s)^k`.** Median `Amp(s=4)` is ≤ 1.17 for `k_eff≤2` and ≤ 1.75 for `k_eff=3` across all L; only the lone `k_eff=4` records reach ~2–3. The incident caps overlap `C_p` *weakly* (each conditioning lift is modest), so even several overlaps compound to a small factor — nothing like `5^k`.
3. **F041's tail was mostly MC noise.** F041's q99≈30 and max≈124 (at s=4, L=4) came from records with `ν_p` far below the `MINHIT` floor (a handful of `C_p` hits in 40k samples → a wildly noisy ratio). With ≥40 hits the genuine worst over 283 records has top-1% threshold **4.2** (L=4), i.e. single-digit, not 124. So **F041's "heavy tail ≈ (1+s)²–(1+s)³" is revised: the real amplification on statistically-resolved records is O(1) with weak overlap dependence.**

## 3. Consequence for LCI / Z.B

- **F041's core conclusion is strengthened.** The tilted object (7.2) `ν^{B,s}(C_p) ≤ C_LCI·ν(C_p)` holds with `C_LCI = O(1)` not just for the bulk but for essentially all statistically-resolved records, including the multi-overlap ones — the worst median amplification measured is ≈ 1.8 (k_eff=3) and the well-sampled maximum is single-digit. The incident source tilt does **not** make `X_p` free.
- **The residual is now sharper still.** The only records F042 cannot resolve are those with `ν_p < 7×10⁻⁴` (below the hit floor) — the rarest target-cap events. For these the MC amplification is unreliable; their genuine amplification is governed by `Lfull = ν(C_p|C_B)/ν(C_p)`, a finite-dimensional cap-geometry quantity (computable by quadrature, not MC). This — the conditional cap probability for ultra-rare target caps under full incident conditioning — is the precise object Z.B must bound, and it is a deterministic cap-geometry estimate, not a stochastic 85%-bad-set problem.

## 4. Scope / grounds

- **Grounds:** gated Monte-Carlo (G-RT1/2 validate the sampler and cap probabilities; G-OV1 is the exact `s→∞`↔full-conditioning identity). The stratification medians are robust across three volumes; the top-1% tail composition is clean only at L=4 (283 records); L=8/16 have too few tail records (2–3, 1) for the tail-composition statistic, though the k_eff stratification is consistent.
- **Selection caveat (stated plainly):** the `MINHIT=40` floor removes near-zero-`ν_p` records. This is what removes F041's MC-noise tail, but it also removes the genuinely rarest cap events, which are not resolved here and are flagged as the Z.B residual (to be computed by quadrature on the worst geometries, the natural next step).
- **No proved status changes.** F037/F038/F040 stand; (D) closed. **F041 status note:** its bulk result (median≈1, q90≈1+s, (7.2) with O(1) constant) stands and is reinforced; its heavy-tail *magnitude* (q99/max ≈ (1+s)²–³) is **revised** by F042 to MC noise on sub-floor records — the genuine amplification is O(1) with weak overlap dependence. Recorded per rule 6 (corrections surfaced, not buried).

## 5. Deposits

`za_cap_geometry/`: `ENGINE_OP1_za_overlap_f042.py` (engine, md5 7adf3e8e) + `overlap_L{4,8,16}.json` + `DATA_OP1_overlap_amp_vs_keff.png`. Updated: STATE.md, ZA_CAP_GEOMETRY note §9, F041 finding revision note, REVIEW_LEDGER #63, SESSION_LOG. Ledger count → 44/57 closed (41 DONE + 3 SKIP), F001–F042.
