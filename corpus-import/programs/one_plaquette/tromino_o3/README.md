# tromino_o3 — the O(y³) tromino suite (intake June 12, 2026, F024; source: C:\SIMULATIONS, June-11 mtimes)

The next-order flat-band program layer: does the C-odd O(y²) flat band survive the two-hop (tromino) geometries at O(y³)? Eight engines, MD5-verified copies (manifest: this table + `records/review/manifests/SIMULATIONS_MD5_2026-06-12b.txt`). Scope discipline throughout ("NOT the full third-order effective Hamiltonian" — each file states what it does and doesn't claim).

| File (MD5 prefix) | Role | Cold run June 12 |
|---|---|---|
| ENGINE_TROM_tromino_o3_su3_weight_cards.py (81b3dc5f) | geometry contract: the 3 lifter classes + flat-band preservation test | **ALL 17 GATES PASSED** |
| ENGINE_TROM_tromino_weight_constraint_certificate.py (b402bfba) | nullspace certificate: equal-lifter weights ⇒ S(k)² protection | **ALL 15 GATES PASSED** |
| ENGINE_TROM_tromino_candidate_closed_form_check.py (4009fac7) | exact closed form α(k); extrema 8/3 (axes) vs 8/27 (R), width 64/27 | **GATE PASS + 40/40 numeric** |
| ENGINE_FLUX_su3_haar_tromino_primitives.py (e55ede27) | exact U(3) Weingarten p=q≤3 + SU(3) ε-moments + Fierz gates | **ALL 25 GATES PASSED** (needs `--cards <json>`; default path is a Colab relic `/mnt/data/…`) |
| ENGINE_TROM_tromino_o3_candidate_lift_diagnostic.py (57abf787) | candidate-weight perturbation of the flat branch | ran; see conclusion note below |
| ENGINE_TROM_su3_o3_tromino_weight_extractor_v1.py / v1_1_colab_fixed (808d79f8/69b20d8d) | extraction/validation harness (4 weight modes) | v1_1: **12/12 GATES PASSED** ("validates plumbing… not a final physical certificate") |
| ENGINE_TROM_tromino_contract_independent_check.py (dc0994fb) | independent symbolic review of the 3 contract files | **ALL 16 GATES PASSED** (run via path-redirected working copy — hardcodes `/home/claude/review/…`, an agent-session relic; verbatim copy here untouched) |

**Conclusion structure (record both levels, no adjudication):** (i) the *candidate* diagnostics (lift_diagnostic, extractor) print: under the Untitled221 primitive-weight hypothesis (W_path± = 2/9, W_corner = 2/27) equal-lifter protection **fails** ⇒ that kernel would lift the band — explicitly conditional on those weights being physical, which both scripts disclaim. (ii) the *independent symbolic check* prints the structural claim: the O(y³) NN content is purely ε-mediated and σ-covariance forces H_eff = αI + bS ⇒ **"the flat band stays EXACTLY FLAT at O(y³), rigidly shifted"** — consistent with the June-11 d₃ certificate (251/251) and implying the primitive candidate is not the physical weight set. The full SU(3) resolvent/channel computation of the physical weights remains the stated open step (their words). Status adjudication: Alex.

Also intaken beside this dir: `../ENGINE_FLUX_glueball_band_certificate.py` (v1 predecessor of the archived v2; cold run: 29 GATE PASS lines, 0 FAIL — prints the O(y²) band structure + "LOWEST BRANCH EXACTLY FLAT"). Note: the store's `ENGINE_FLUX_cls_flat_band_certificate.py` is byte-identical to the archived v1.0-era file — **CLS v1.1 remains lost** (F015 list unchanged).

Path caveats for rerunning: generate the cards JSON locally (`--emit-json ./CERT_TROM_tromino_o3_su3_weight_cards.json`), pass it to primitives via `--cards`; run the independent check from a working copy with its `/home/claude/review/` path redirected (one-line sed, documented here).
