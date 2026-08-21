# F023 — New store survey: C:\SIMULATIONS (Colab authoring store); lost-engine hunt negative; real CW extractor recovered

**Date:** 2026-06-12 · **Trigger:** Alex mounted C:\SIMULATIONS this session. Rule-11 sweep (name-pattern + content fingerprints + date clusters + size/MD5 cross-check). Store treated read-only.

## 1. What the store is

Flat directory, **271 Jupyter notebooks, 47 MB**, no subdirs, mtimes 2026-03-07 → 2026-06-11 in three clusters: a June-7 00:18 bulk stamp (mass download), May-22 (GOODRESULTS1–5), June-11 18:28/18:46 (the SU3 d₃ pair). Content profile (Untitled### series, Theorem_B_v4–v12 series, SU2_4D_Phase2 variants, A100 runs, GOODRESULTS, domino/d₃) identifies it as **the Colab authoring store** — the notebook-side sources of the corpus's simulation layers.

## 2. Cross-check vs archive (rule 11)

Against all 239 `.ipynb` in `E:\YANG\ORGANIZED`: **34 match by name+size** — GOODRESULTS1–5, the wilson_su3 Peierls probes, rooted_capacity_peierls_path, Untitled222 pair, GALAXY RUNS, the SU3 d₃ pair (d₃ pair additionally **MD5-confirmed byte-identical** to `13_PMBSF/notebooks_runs/`) — i.e. the June-11/12 intakes' sources, confirmed. **237 have no name+size match** = new-to-archive candidates (rename-hidden duplicates possible — that's the known weakness of this filter; full MD5-level identification queued as **#45b**). Full-store manifest deposited: `records/review/manifests/SIMULATIONS_MD5_2026-06-12.txt` (271 MD5s).

## 3. The F015 lost-engine hunt — NEGATIVE (status reinforced)

All probes for the 7 documented-but-not-reproducible items came back empty: filename probes (c2_certificate, su3_exact_c2, su3_odd_gap, n7_c1, c2_residual_ranks, CLS-v1.1 variants) and content fingerprints (exact rationals 11/306 + 109151/249696 hit only the d₃/Untitled222 quartet; "discrimin" hits are Weyl-discriminant code; precise CLS/odd-gap/rank-cap strings: zero). **The lost certificates are absent from the authoring store too.** Consequence: F015 §2's recovery options narrow — chat re-export or approved reconstruction remain; "the authoring notebooks may hold them" is now ruled out for this store. (F011 n/a here — store is notebooks-only.)

## 4. Recovered: the real CW extractor (stub-in-archive pattern — new trap)

`NB_SU3_15_cw_extractor_alt.ipynb` (12,987 B, self-described "Self-contained Heavy-Mode Wilson Hessian Constant Extractor", SU(3) generators, JAX/Lanczos, θ-scan + lattice sizes) is **a computation of c_W — exactly the constant PROOF_04 leaves existence-only** (F022 §1.4, CONVENTIONS κ/c_W row). The archive holds only a **199-byte stub under the same base name** (`04_SIMULATIONS/colab_notebooks/15_CW_extractor.ipynb`); the real file existed nowhere in any store until now. → Recovered MD5-verified to `numerics/cw_extractor/` (status: **unrun, unverified, candidate engine** — gate-wrap before any use; README there).

**New trap recorded:** name-level dedup would have called this "already archived" — the stub matches by name, only size/MD5 expose it. Sweep rule: name+size minimum, MD5 on matches.

## 5. Other notable unarchived items (for #45b prioritization)

`Step2 SigmaGeom A100.ipynb` (σ_geom — the Mode-B constant thread, F016/F022); `Omega_Area_Law_A100.ipynb`; the Theorem_B_v12 series (~26 notebooks carrying charge-odd content incl. GALAXY RUNS — Theorem-B lineage continuation beyond the archived v4–v7); ~150 Untitled### authoring notebooks — **probable sources of 13_PMBSF's 181/185 image-PDF "Untitled-audit exports" (F012 hypothesis, now testable)**.

## 6. Deposits

`numerics/cw_extractor/` (recovery + README); `records/review/manifests/` (271-MD5 manifest + README); SOURCES.md new store section; ledger rows #45 (this survey, DONE) + #45b (deep identification, PENDING — campaign totals now n/46); STATE (header, item 3, item 3a(i) note); SESSION_LOG.
