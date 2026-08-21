# F027 — Review of the uploaded closed-form trio (m4_tc_closed_form.{py,json} + NOTE_OP1_m4_tc_closed_form_2026-06-12.md)

**Unit:** #48 (Alex upload, June 12 late). **Verdict: CONCORDANT + ADDITIVE — adopt; one corrective finding against the same-day THEORY deposits (β-rounding), verified and applied.**
**Secured verbatim** (uploads are temporary) → `numerics/op12_theta/m4_scaling/`: engine md5 `5245f316…`, json `d63fcd2a…`, note `223fd85b…`.

## 1. Identification and provenance

A **parallel-session** derivation (env paths `/mnt/project`, `/home/claude` — the agent-authoring environment of the F024 path-relic precedent), self-attributed "session agent (lead math agent per DECISIONS #009)", authored from the **morning deposit state**: it gates against `CERT_OP1_m4_harmonic_decomposition.json`, `CERT_OP1_kernel_consts.json`, `CERT_OP1_m4_scaling_tables.json` and nowhere references the late-pass artifacts (`m4_tc_fourier.*`, the real-space check, the sparsity interface). It therefore constitutes an **independent re-derivation of the same closed form**, same day, different code, different verification routes — the strongest cross-validation the kernel constants have received.

## 2. Concordance (all verified here, not assumed)

| Their claim | Check performed | Result |
|---|---|---|
| Theorem 1 closed forms (g_H, T_H, g_C, T_C, multiplicity 3, gauge band 0) | identical to the late-pass `ENGINE_OP1_m4_tc_fourier.py` formula; proof text read line-by-line (Δ₁ componentwise cancellation, fiber decomposition, dimension audit 1+3+… = 4L⁴, transitivity ⇒ per-link constancy) | **sound**; their proof text is the more complete citable derivation (per-link constancy and exact cross-term vanishing upgraded from measured gates to theorems) |
| Gates G-CF1–6 | their engine re-run on OUR stores (adapted copy, paths only) | **ALL PASS, bit-identical gate stats** to their json (e.g. G-CF1 worst 9.66e-15, 13/4 β-partition) |
| 17-row diagonal incl. their unique s = 1.25 (L=5), 10, 20 | recomputed with MY engine at exact β | worst rel **3.05e-15**; vs my deposited 16-row json (14 overlaps) **2.42e-15** |
| Law A_fit/A_theory = 1.0151 on ln s ∈ [1.10, 4.16] | consistent with my window fits (1.0069 on s≥8, 1.0052 on s≥24) given the monotone local slopes; their last local slope 0.0095473 = mine at s=48→64 to all digits | **consistent** (window effect, not disagreement) |
| Tier-1 bound: lemma sin πx ≥ 2x on [0,½]; c₀ = 25.323345; cube comparison (4/3)⁴·2π²·ln((L+1)/2) | lemma + algebra checked by hand; shell counts r₄(1..8) = 8,24,32,24,48,96,64,24 verified; c₀ recomputed independently = 25.323345; dominance tested on MY far rows they never computed | **proof sound**; dominates at s=96/128 ×16.8–16.9 — **unconditional uniform finiteness of T_C along the diagonal is now a theorem** |
| Tier-2 ceiling T̄_C ≈ 0.1166 ⇒ N\*_C ≥ 8, N\* ≥ 7 (two pins flagged) | recomputed under my law form *including the ln α term* (their fit omits it): T̄ = 0.11550, x\* = 36.23 — same floors. **Plus a new direct check (below)** | **floors robust across three law variants + direct evaluation** |
| Their §5 item 5: cδ ≥ 4/γ = 28.71 under the Peierls ansatz | 4/γ = 2/c_af = 32π²/11 = 28.712 ≡ the late-pass requirement; theirs is data-free/conditional, the late-pass version measured κ̂ | **same inequality, two scopes** — see §5 synthesis |

## 3. Their corrective finding against the THEORY deposits — CONFIRMED, applied

**β-rounding generation mix (their note §2 micro-finding).** Verified with my own engine, independently of their code: of the 17 `CERT_OP1_m4_harmonic_decomposition.json` rows, **13 match the stored-rounded-β reading at ≤1e-12 and 4 match exact-β(s)** (the three s=1.25 rows + (12,3)); the four s=1 rows are ties (rounding is identity there). Max cross-reading deviation **1.54e-5 at (4, s=3)** (they localized it at (12,3) — same magnitude, same Δβ; mine is the sharper localization). No integer radius changes under either reading (their gate + my check).

**Consequence: the deposits' "CG path noise" attribution (morning DECOMP run record; repeated in the late-pass note §1 and MANIFEST/README) was WRONG.** CG at these tolerances is exact to ≤1e-9 (the L=16/24 real-space check sits at 1e-15). Corrected this pass in: `NOTE_OP1_m4_harmonic_decomp_2026-06-12.md` (run-record correction appended), `NOTE_OP1_m4_tc_asymptotics_2026-06-12.md` §1, `MAN_FLUX_manifest.md` row, `m4_scaling/README.md`. Their G-CF1/G-CF3 dual-reading gate is adopted as the model for transcription-precision forensics (CONVENTIONS §4 item 4 family).

Also fixed under this review (self-found, same class): the sparsity-interface header and note displayed E|D| with prefactor 1536 s⁴ (the plaquette count) where the link bound is 4× that, 6144 s⁴ — exponents and all findings unaffected; both files corrected with notes.

## 4. Reviewer addition: the ceiling computed directly (pin (ii) shrunk)

Their Tier-2 extrapolates the fitted law to x\* ≈ 36.5. But for s ≳ 100 the wrapped-Bessel images are numerically dead and the diagonal T_C is the **infinite-volume function** — directly evaluable at any s (Φ∞ = I₀e⁻², far tail = exact exponential integral, remainder bounded <1e-7 rel, panel refinement ≤1e-9). Computed here: **max T_C^∞ = 0.11692 (±4e-10 quadrature) at ln s = 35.62 (s ≈ 3.0×10¹⁵, β ≈ 10.56)**, ridge flat to 0.3% over ln s ∈ [34, 40]. The lattice diagonal sits **4.8–5.3% below** the ∞-volume curve at every computed overlap (s = 64/96/128, deficit shrinking). So the extrapolation pin is replaced by: (a) direct ridge evaluation (done), (b) the finite-vs-infinite-volume comparison on the diagonal (T_C^L ≤ T_C^∞: observed at all computed points, not yet proven — the remaining honest pin, alongside their pin (i)). **Floors N\*_C ≥ 8, N\* ≥ 7 are unanimous across: their fit, their pinned-A variant, my ln α law form, and the direct ridge.** Grounds: derived + machine-verified quadrature; the L-vs-∞ inequality is observed-unproven.

## 5. Synthesis of the two §5/§3 readings (their Opinion 6 vs the late-pass (S)-interface)

Same inequality, two exits, both now recorded in the closure plan: at **v₀ ≡ 1** (their declared scope) the global-HS instrument cannot ride the diagonal — fixed-δ κ is capped at O(2–4) vs 28.71 required — which is their "number behind why windows are forced" (M3's windowed + CT-glued architecture). The late-pass measured-κ̂ version adds the second exit: **v₀ ~ a^q with q > q\*(δ) = 2 − c_af·κ̂ ≈ 1.82–1.91** closes the global certificate for any exponential sparsity. The exits are not exclusive: q is a normalization/modeling decision (Alex, STATE #0), windows are an architectural one (M3a). One nuance their Tier-2 adds to the q=0 branch: even there the deterministic budget never vanishes (uniform N\*_C ≥ 8) — it is the defect *count*, not the certificate, that fails at q=0.

## 6. Deposit record

Trio deposited verbatim beside the late-pass suite (no name collisions; env-path relics documented per F024 precedent — runnable here via `/tmp` adapted copy, gates replicate). MANIFEST +3 rows (62 files); README cross-link; closure-plan M4 addendum amended (ceiling floors + proof-text pointer); STATE M4 row + header; ledger #48 DONE; this finding. **Open items handed to Alex:** none new — the trio's pins (i)/(ii-residual) are agent-executable follow-ups (Euler–Maclaurin two-sided B; L-vs-∞ monotonicity on the diagonal), queued as optional M4 hardening.
