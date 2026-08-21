# F015 — Unit #40: one-plaquette certificate-corpus reconciliation

**Date:** 2026-06-12 · **Scope:** hunt F014 §3b's absent certificates across Downloads, 13_PMBSF run-zips, june11_misc zips, F:\STORAGE, F:\E, E:\YANG DELETE; identify the 14 non-canonical notebooks; repair the deposit record.

## 1. Recovered (15 files, MD5-verified deposits; provenance READMEs in each receiving dir)

- **`12_ONE_PLAQUETTE/weak_coupling_certificates/` (NEW, 10 files):** the charge-odd store set — ENGINE_SUN_codd_local_gap_exact.py (**re-run cold from deposit: formula check PASS at every N=3–12**), SU_N_C_odd_appendix.tex, the C-odd Finite-Wick docx, **plus 4 write-ups in no v2.7 inventory** (Finite-Wick H₁-resolvent even+odd docx; two differing editions of "Fixed-Rank SU(N) Local Class Gaps.docx"), suN_c2_even_rank_ledger.csv, su3_v9_1/v9_3 codd scripts. **mtimes May 30 / June 6 — they predate F011's June-11 date window; that is the full explanation of the miss** (pattern intake missed them earlier for name reasons; date intake for date reasons).
- **`band_certificates/`:** ENGINE_FLUX_glueball_band_certificate_v2.py (**re-run: ALL 35 GATES PASSED**; v2.7 says 36 gates — count discrepancy recorded, unadjudicated) + glueball_band_results.md (v1 as-written edition).
- **`notebooks/`:** rooted_capacity_peierls_path.ipynb (June 11) — *"crosses off the deterministic top-norm capacity envelope; isolates the Wilson Peierls/free-energy theorem as the remaining hard target"* — a direct OP-1/(S) feeder, sibling of the ROOTED probe.
- **`support_scripts/`:** su3_0pp_gevp_v4_rankcap_pca_colab.py (June 5; glueball-v4 GEVP lineage — plausibly related to the absent glueball_v4_* App-A scripts, unconfirmed).
- **`13_PMBSF/misc_research_pdfs/`:** rank_two_weyl_projected_capacity_final.tex (May 30, projected-capacity paper line; original PMBSF intake missed it).

## 2. Definitively missing (no copy on Downloads, E:\YANG incl. DELETE, F:\STORAGE, F:\E, YANG_ANTI-by-prior-hash-sweep)

**7 files:** c2_certificate.py, su3_exact_c2.py, su3_odd_gap.py, n7_c1_discrimination_certificate.py, c2_residual_ranks_certificate.py, c2_residual_ranks_routeC_storefix.py, ENGINE_FLUX_cls_flat_band_certificate_v1_1.py (+results v1.1). The Downloads cls pair is byte-identical to the deposited v1.0 (d5396786…/f299b968…) — v1.1 never left the session. These existed only in the authoring environment (`/home/claude/review/`).

**Consequence ledger (no status changes made):**
- v2.7 §2's EXACT(store) rows for **c2±(N)** (even 3–12, odd 3–13) and the **§6.2 N=7 discrimination** + **§6.14 residual-rank decisions** are *documented-but-not-reproducible*: exact decided values are recorded in the master doc (incl. instrumented printouts q1(6,7,8)), but no engine that produced them is on disk.
- The **c-odd sector** row is now partially re-backed: the recovered ENGINE_SUN_codd_local_gap_exact.py re-verifies c0−/c1− closed forms (run log June 12); su3_odd_gap.py and su3_exact_c2.py remain absent.
- **CLS robustness/completeness** (§8.6) rests on the v1.0 engine (13/13, has the G10 precedence slip + k=0 span overclaim that v1.1 fixed) — the *corrected* certificate is the missing one. The v1.1 fixes are precisely described in v2.6's changelog, so reconstruction is mechanical.
- **Options for Alex:** (a) re-export the authoring chat session(s) if they survive (the ChatGPT export ends 2026-02; these were later sessions — different export needed); (b) agent-reconstruct the missing engines as new certificates against the recorded values (cheapest: cls v1.1 — apply the two documented fixes + G09b gate; heaviest: c2_certificate.py's third-order RS engine). Reconstructions would be NEW artifacts, labeled as such, never claimed as the originals.

## 3. Notebook identification (14 files; README written into notebooks/)

Program material: Untitled221(+copy) = SU(3) 0⁺⁺ glueball MC H100 v2 (§8 MC lineage); Untitled222(+_fixed) = **authoring notebooks of ENGINE_FLUX_su3_moments_ext.py** (provenance for the §8.4 engine); rooted_capacity_peierls_path + rooted Peierls probe (OP-1 feeders). Date-window strays (re-home candidates, Alex to direct): Untitled108 (scalar propagator m_eff(L), core numerics), 111 (SU(N) drift diagnostics), 113 (**non-project** sensor toy), 117 (slab Hessian λ_min — OP-3 lineage), 119 (expm/logm scratch), 121 (plaquette-bit toy driver), 122 (3D-torus cochain complex — Hodge lineage), **124 (phi_obstruction_su2_4d_a100 — an OP-11 Φ_proxy diagnostic)**, su2_4d_complete_FOURIER (θ-term q-6j HOTRG — TENSOR_NETWORK/SixJSymmetry lineage; June 6).

## 4. Record repairs

12_ONE_PLAQUETTE/README.md gained a dated reconciliation block correcting the F011 intake paragraph (no tromino_certificates/ dir; band certs were never in band_certificates/ pre-today; §6.1 not closed; §8 corpus lives in 13_PMBSF/notebooks_runs). band_certificates/ and weak_coupling_certificates/ got provenance READMEs with run logs. 13_PMBSF/README.md gained the rank_two_weyl deposit line + cross-link note. Old text preserved; corrections appended, audit-trail style.

## 5. Verdict (one line)

8 of the 11 missing items recovered or re-backed (15 deposits, 2 cold re-runs passing); 7 files confirmed to exist nowhere — the c2/N=7/residual-rank engines and CLS v1.1 are documented-but-not-reproducible, with reconstruction options recorded for Alex; notebooks/ fully identified (2 OP-1 feeders found; 1 OP-11 diagnostic mis-filed; 1 junk).
