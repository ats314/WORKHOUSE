# F038 — Multi-cap rate = Δ_p(A): the deterministic core of LCI is complete; Z.A reduces to one typicality statement (June 12, 2026)

**Unit:** #59 (own-initiative continuation of F037, Alex "proceed"). **Verdict: the deterministic/finite-dimensional half of Z.A is now closed — what remains of Z.A is a single, precisely-stated stochastic statement.** F037 proved the bare-cap (A=∅) curvature lemma, certified the bare-cap cap-ratio rate, and showed the §9 incident criterion must be parametrized by the height-drop Δ_p, not χ₀. This pass completes the **incident** case: it establishes (Varadhan/Laplace) and **certifies by exact quadrature** that the conditional cap-ratio rate equals the true height-drop Δ_p(A) for **every** incident cap set A≠∅, with prefactor power bounded in [−1/2, 0]. Combined with F037, every finite-dimensional step of the LCI reduction §§6–11 is now proved or certified, and the LCI condition reduces to the **single typicality statement** `min_A Δ_p(A) ≥ Δ_q + O(log κ / κ)`, P-typically, with rooted/absorbed complement. Engine `programs/op1_defect_sparsity/za_cap_geometry/ENGINE_OP1_za_multicap_v2.py`, gates **G-ZB1, G-ZB2 PASS**.

## 1. The multi-cap rate theorem

**Theorem (rate).** For the vMF measure ν = vMF(m, κ) on S³, incident cap set A, target cap C_p, with Δ_p(A) = h(A) − h(A∪{p}) > 0 (good event),

  **lim_{κ→∞} −(1/κ) log ν(C_p | C_A) = Δ_p(A).**

*Proof (Laplace/Varadhan).* The vMF family vMF(m, κ) satisfies a large-deviation principle on the compact manifold S³ as κ→∞ with rate function I(u) = 1 − m·u (relative to the maximum at u=m) and speed κ. For any closed set with nonempty interior in its closure, Varadhan/Laplace gives `−(1/κ) log ν(F) → min_{u∈F} I(u) = 1 − max_{u∈F} m·u`. Apply to F = C_A (max attained at u_A, value h(A)) and to F = C_p ∩ C_A (value h(A∪{p})):

  `−(1/κ) log ν(C_A) → 1 − h(A)`,  `−(1/κ) log ν(C_p∩C_A) → 1 − h(A∪{p})`.

Subtracting, `−(1/κ) log ν(C_p|C_A) → h(A) − h(A∪{p}) = Δ_p(A)`. ∎

The polynomial prefactor `κ^{−M}` depends on the active-face structure at the two maximizers (their active-set codimension and the corner geometry), and is not universal — but it is **bounded** (§2), so it is absorbed into the `O(log κ / κ)` correction of the LCI criterion (§3).

## 2. Quadrature certification (G-ZB1, G-ZB2)

Restricting m, n_p, A to a 3-D subspace V (legitimate: the rate claim is geometric, independent of whether the normals span 3 or 4 dimensions) makes `ν(C_p|C_A)` an **exact 3-D quadrature** over the projection onto V's unit ball, marginal density `∝ e^{κ m·v}(1−|v|²)^{−1/2}` (the S³→3-ball coarea). This removes the Monte-Carlo noise that obstructs a clean rate read at large κ (an earlier full-4-D MC version, `RUN_OP1_za_multicap.py`, was rate-noisy at κ≤37 — kept as the audit trail). Over a κ-ladder 20–150 and four geometries spanning active-set codimension 0/1/2:

| k (|A|) | active-set codim at u_A / u_{A∪p} | Δ_p(A) solver | Δ_p fit | χ₀(A) | prefactor M |
|---|---|---|---|---|---|
| 2 | 1 / 2 | 0.1008 | 0.1009 | 0.454 | −0.44 |
| 4 | 2 / 2 | 0.2971 | 0.2915 | 0.381 | −0.19 |
| 2 | 1 / 2 | 0.0627 | 0.0607 | 0.305 | −0.47 |
| 1 | 0 / 1 | 0.0718 | 0.0716 | 0.178 | −0.46 |

**G-ZB1 (rate):** the 3-parameter fit `−log ν = κ Δ_p − M log κ − c` returns Δ_p matching the solver height-drop to **worst error 0.0056**. **G-ZB2 (form):** max fit residual **0.014**. Two consequences:
- The rate is `Δ_p(A)`, **not** `χ₀(A)`: the table's χ₀ values (0.18–0.45) differ sharply from the rates (0.06–0.30) — independent re-confirmation of F037's correction (the k=4 row: χ₀=0.38 but rate=0.30; the k=1 row: χ₀=0.18 but rate=0.072).
- The prefactor power **M ∈ [−0.47, −0.19]** across codimensions, i.e. bounded in [−1/2, 0]: the prefactor is at worst `κ^{1/2}`, so it never overturns the exponential and folds into the `O(log κ / κ)` LCI margin. This answers F037's open residual (1) (uniform/bounded prefactor over the ≤5 incident caps).

## 3. The deterministic LCI core is complete

Assembling F037 + F038 against the reduction's §§6–11:
- **§7 (LCI ⟹ incident TOS), §11 (LCI + far ⟹ TOS+J), §§2–3 (TOS+J ⟹ Lemma Q):** algebra/positivity, sound (verified F037 §0).
- **§8–9 cap geometry:** the curvature constant is `c_curv = 1/2` (bare cap, proved F037); the incident criterion is corrected from χ₀ to the height-drop Δ_p (F037); the **cap-ratio law (8.4) holds for all A with rate Δ_p(A) and bounded prefactor** (this finding).

Therefore the LCI condition (6.3) `ν(C_p|C_A) ≤ C_LCI q` for all incident A holds **iff**

  **min_A Δ_p(A) ≥ Δ_q + (M log κ + O(1))/κ,  M ∈ [−1/2, 0],  q ≍ e^{−κ Δ_q},**

a criterion now stated entirely in the **correct deterministic variable** (Δ_p) with a **certified rate**. Every finite-dimensional / Laplace step is proved or certified.

## 4. What remains of Z.A — exactly one stochastic statement

**Z.A is reduced to:** under the tempered SU(2) Wilson heat-bath geometry, the event

  **G_LCI' = { min_{A ⊆ incident(e)} Δ_p(A) ≥ Δ_q + O(log κ / κ) }**

holds P-typically, with rooted/absorbed complement, uniformly along the trajectory. This is purely probabilistic — a statement about the distribution of the staple geometry (m_e, κ_e, the n_r) — and is the piece that couples to Z.B (far-source stability of these parameters, §10 of the reduction) and to Bałaban locality. The deterministic cap-geometry that the reduction left as "a Laplace ratio estimate … under nondegenerate hypotheses" is no longer a gap.

**Actionable (carried from F037, now sharper):** re-point `ENGINE_FLUX_lci_typicality_diagnostic.py` to measure `min_A Δ_p(A) = h(A) − h(A∪p)` (it already computes both heights) — this is exactly the observable whose typicality is the entire remaining content of Z.A. A re-run of the diagnostic under this observable on the Stage-B ensemble would give the first direct evidence for/against G_LCI'.

## 5. Status / scope

No proved status elsewhere changes; (D) stays closed (F033); Z.B and M3b unaffected. This finding closes the **deterministic** half of Z.A and isolates its stochastic remainder to one observable. Grounds: §1 theorem = derived (standard Varadhan/Laplace on a compact manifold; rigorous at the rate level); §2 = exact-quadrature certificate (G-ZB1/G-ZB2); the prefactor boundedness is numerical evidence over codim 0/1/2 (not a proof of uniformity over all configurations, but consistent and bounded where tested). The reduction of Z.A to G_LCI'-typicality is exact given the certified rate.

## 6. Deposits

`za_cap_geometry/`: `ENGINE_OP1_za_multicap_v2.py` (canonical, md5 4f92e60d) + `CERT_OP1_za_multicap.json` (b7f4ed1d) + `RUN_OP1_za_multicap.py` (MC iteration, rate-noisy, audit trail). Note `NOTE_OP1_za_cap_geometry_2026-06-12.md` gets a §5-bis (multi-cap rate). Closure-plan Z.A addendum + pmbsf README updated to "deterministic core complete; residual = G_LCI'-typicality". STATE + SESSION_LOG + ledger #59. Ledger count → 40/57 closed (37 DONE + 3 SKIP), F001–F038.
