# za_cap_geometry — Z.A LCI cap-geometry (F037, June 12, 2026)

Analytic + certified work on the finite-dimensional spherical cap-geometry that
§§8–9 of `programs/pmbsf/NOTE_PMBSF_lci_tosj_reduction_lemmaq_2026_05_26.md` reduce LCI to
(the agent-tractable deterministic core of Theorem Z.A in the OP-1 M3a split).

**Proof note:** `NOTE_OP1_za_cap_geometry_2026-06-12.md` (a57e2ba9).
**Finding:** `records/review/findings/F037_za_cap_geometry.md`.

## Results

1. **Bare-cap curvature lemma PROVED** (§1 of the note): for the target cap alone
   (A=∅), `Δ_p = 1 − ac₀ − √((1−a²)(1−c₀²)) = 2sin²δ ≥ χ₀²/2`, sharp constant
   `χ₀²/(2(1−c₀²))`. Supplies the explicit `c_curv = 1/2` the reduction's (9.5)
   left unspecified. Machine-verified to 1.3e-15 (G-ZA1/G-ZA2).
2. **(9.5) is FALSE for incident subsets** (§2): a sampling-verified counterexample
   (k=3 caps, χ₀=0.19 but Δ_p=0.002, ratio 0.007 ≪ 1/2; valid-config violation
   rate 12%). The §9 good event must be parametrized by the true height-drop
   `Δ_p(A)`, not by `χ₀` at u_A. **Actionable:** re-point `ENGINE_FLUX_lci_typicality_diagnostic.py`
   to report `min_A Δ_p(A)` (= h(A) − h(A∪p)) instead of `min_A χ₀(A)`.
3. **Cap-ratio law (8.4) rate certified** (§3): `ν(C_p) ∼ C_geom κ^{−M} e^{−κΔ_p}`,
   rate = the proved Δ_p (G-ZA3), prefactor M ≈ −1/2 (corner-Laplace, density
   vanishes at the dominant point). Law fit residual 0.005.
4. **Multi-cap rate (A≠∅) PROVED + certified** (F038, note §5-bis): the conditional
   rate is the true height-drop `lim −(1/κ)log ν(C_p|C_A) = Δ_p(A)` (Varadhan/Laplace)
   for every incident A, certified by exact 3-D quadrature (`ENGINE_OP1_za_multicap_v2.py`,
   G-ZB1/G-ZB2; worst rate err 0.006; prefactor M∈[−½,0]). **⟹ the deterministic LCI
   core is COMPLETE; Z.A reduces to the single typicality statement
   `G_LCI' = {min_A Δ_p(A) ≥ Δ_q + O(logκ/κ)}`** (stochastic core, coupled to Z.B).
   Findings F037 + F038.
5. **Corrected observable MEASURED on the heat-bath ensemble** (F039, note §6):
   `min_A Δ_p` measured on a real SU(2) exact-heat-bath config (β=3.5, L=4) via
   `ENGINE_OP1_za_dp_v3.py` (gates G-DT1 no-impossible-drops + G-DT2 bare-cap-lemma-on-data).
   Both observables agree on *whether* the good event holds (12.5%; exact, since
   Δ_p(A)>0 ⟺ χ₀(A)>0) but Δ_p shows the *margin* is much smaller (half of
   χ₀-good cases are Δ_p-marginal). At L=4/κ≈18 the strict G_LCI' is essentially
   empty ⟹ everything rooted ⟹ Z.A typicality is a **larger-L + rooted (Z.B)**
   phenomenon. **Next: same measurement at L=16.** Engines `ENGINE_OP1_za_dp_v3.py`
   (canonical) + `ENGINE_OP1_za_dp_v2.py` (iteration: dropped a wrong pointwise-ordering gate).
6. **L-scan L=4/8/16** (F040, note §7): built a **validated vectorized SU(2) heat-bath**
   `ENGINE_PMBSF_su2_hb_v3.py` (28× faster; G-HB1 staple==diagnostic 6.7e-16, G-HB2 plaquette
   matches) to reach Stage-B sizes; `ENGINE_OP1_za_dp_vsl.py` (resumable, G-DT1/G-DT2).
   **frac(min_Δp>0) = 0.125/0.175/0.121 — flat in L** (L=8 = noise), margins small
   (median 0, L=16 max 0.07). The deterministic good event does NOT open up by L=16;
   bad set ~85% ⟹ **the LCI bound rests on the rooted complement + Z.B (load-bearing).**
   OP-1's (S) weight relocated to Z.B; the LCI cap geometry (Z.A core) is settled.
   `ENGINE_PMBSF_su2_hb_v3.py` (heat-bath tool, reusable) + iterations `su2_hb_vec/v2.py`.

## Files

| File | md5 | Role |
|---|---|---|
| `ENGINE_OP1_za_cert_v5.py` | 8bc3d7e1 | **canonical** engine (hardened solver + independent sampling re-verify). Gates G-ZA1..G-ZA5 PASS. |
| `CERT_OP1_za_cap.json` | 2c296c1e | results (curvature, incident counterexample, cap-ratio law) |
| `NOTE_OP1_za_cap_geometry_2026-06-12.md` | a57e2ba9 | proof note |
| `ENGINE_OP1_za_cap_cert.py`, `RUN_OP1_za_cert.py`, `za_cert_v2/v3/v4.py` | — | gated iteration history (superseded by v5): v1 conflated "no active cap" with A=∅; v2/v3 caught the leading-const vs closed-form distinction and the wrong prefactor-power prediction; v5 added the hardened solver + sampling re-verification. Kept as the audit trail (the gates did their job each time). |

Reproduce: `python3 ENGINE_OP1_za_cert_v5.py` (≈40 s; numpy only). The 4×10⁶-point sampling
re-verification of the incident counterexample runs at the end.

**Note (infra):** the VM mount served stale/truncated views of edited files
repeatedly this pass; each engine version was therefore written one-shot to a
fresh path and run without subsequent edits (host-side Read is ground truth).
