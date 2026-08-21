# CONVENTIONS — metric normalizations and constant bookkeeping across the corpus

**Created June 12, 2026 (distilled from findings F014/F016; sources cited per row). Purpose: the master papers will quote constants from four eras of work that use TWO metric conventions and TWO Haar-bookkeeping modes. This page is the single translation table. Update it whenever a new constant enters the citable set.**

## 1. The two inner products (the factor-2 trap)

| Convention | Definition on su(N) | α_W (Wilson Hessian at 1) | ω₀ (per-quantum) | Used by |
|---|---|---|---|---|
| **Trace** | ⟨Y,Z⟩ = −Re Tr(YZ) | **β/N** | √(β/N) | P04_haar_geometry_supplement (κ, c_W); P13; parts of proof/ HESSIAN sector |
| **Casimir (physics)** | ⟨Y,Z⟩ = −2Re Tr(YZ), Tr(T_aT_b)=δ_ab/2, C₂(fund)=4/3 at N=3 | **β/2N** | √(β/2N) | One-plaquette manuscript + program (master doc C.0); flat-band paper; **OP-12 θ-runner (α_W = β/6 at N=3 ✓)**; P09/P10's c₀ |
| **λ-parametrized (brown appendices)** | ⟨X,Y⟩_λ = λ(−Tr XY), λ > 0 explicit; rep constant λ_ρ | **α := β/(nλ_ρ)** — subsumes both rows (λ_ρ=1 → trace; λ_ρ=2 → Casimir) | √(β/(2nλ_ρ))·(2-quantum) | `02_APPENDICES/brown_sections/` (§3.1; constants index = `BROWN - NOTATION_AND_CONSTANTS.md`). **Immune to the factor-2 trap by construction — prefer this formulation when drafting master-paper sections** (F019) |

**Trap (master doc C.0, verified live in F016):** pairing the trace-convention Hessian with Casimir-normalized ½C₂ inflates the leading gap by √2. Any document stating a Hessian **must pin the metric**. The external support-derivations note made exactly this error (caught in master doc §7); no document in `01_PROOFS/proven/` pins its metric. **Third normalization in the citable set (F022):** the heat-kernel paper behind `clay_submission/CODE/VERIFY_01` uses **g = −Killing = 2N(−Tr)** (script header: "their metric is scaled. We will use the PAPER'S CONSTANTS exactly" — a live exhibit of this trap); under it ρ = 1 for SU(2), numerically coinciding with PROOF_04's κ = ¼C_adj = 1 at SU(2) — coincidence vs consistency unresolved, treat the normalizations as distinct.

## 2. The two Haar-bookkeeping modes (F002's "Mode A/B", located at origin in F016)

- **Mode A (metric/measure):** work on the curved product manifold (G^E, g_Haar), reference measure dvol_g; Haar contributes through geometry: Ric_g = κ·g, κ > 0 (κ = ¼C_adj under trace normalization). Used by: P04_haar_geometry_supplement; PROOF_04 (Clay chain).
- **Mode B (flat/penalty):** work on flat ℝ^M with Lebesgue dA, Ric = 0; Haar/gauge effects enter as an action term, σ_A = Ng₀²a²/6 from the quadratic gauge-fixing penalty S_FP. Used by: P04_haar_mass_mechanism; P12.

**Rule (standing, from the January audit + F016):** never combine κ (Mode A) and σ_A (Mode B) in one estimate without an explicit reconciliation argument. **Update (F019; locality resolved F021): a Mode-A-internal reconciliation DOES exist in the brown appendices** — §3.1 Lemma 3.8 proves dvol_g = normalized Haar, and the curvature mechanism is the **localized** hinge (Prop 5.21/Cor 5.22): Ric_μ ⪰ (c_H − R_W(r))I + (β/nλ_ρ)d₁\*d₁ **for U ∈ K_Λ(r) only** (linkwise small-field region), R_W(r) = (β/n)(2νM₃)r, with the radius condition R_W(r) ≤ c_H/2 ⟺ **r ≤ c_H n/(4βνM₃) = O(1/β)** giving the c_H/2 form. **#10b locality check PASSED:** the F016 globalization pattern is absent from brown; the global side is explicitly conditional — global Poincaré on the named **Assumption 7.38** (coercive pairing; "open input"), global LSI additionally on the flagged SPI→LSI external. Brown = confirmed citation target for the *mechanism*, always with the K_Λ(r), r = O(1/β) hypotheses attached — and note brown = verbatim Comprehensive-manuscript sections (its Dependency Ledger governs). The A-vs-B (κ vs σ_A) cross-mode rule still stands. Both modes are quoted as "PROVEN" by their home documents; downstream docs (P07, P10, P20) cite them interchangeably. A master paper must pick one mode per chain of inequalities and say so.

## 3. Citable constants and where they live

| Constant | Value | Convention/Mode | Source (cite this, with its review grade) |
|---|---|---|---|
| κ (Haar Ricci floor) | ¼C_adj·(metric) — "constants not needed for sign" | Trace, Mode A | P04_supplement (UNLABELED chat deliverable) — prefer PROOF_04 ed. (**F022: labeled AI reorganization w/ honest local banner; its Lemma 3.3(4) volume-blind — mechanism cites go to brown**). Cross-era: ≡ brown's c_H = κ_G at λ_ρ=1; SU(2) datum κ = 1 (= heat-kernel paper's ρ under −Killing norm) |
| σ_A (anomaly source floor) | Ng₀²a²/6 (= 0.5 at N=3, g₀=a=1) | Mode B (penalty) | P04_mass / P12; April review: positivity is *local/gauge-fixing-derived* |
| c₀ (Haar mass, phys sector) | (N²−1)/2N = 4/3 at N=3 | Casimir | P09 §4.1 / P10 |
| Weyl curvature floor | ∇²S_geom ⪰ (N/2)I on Σθᵢ=0 | Casimir | OP-9 target; P-chain Thm 2.1 |
| α_W in OP-12 runner | β/6 (N=3) | **Casimir ✓** (coherence verified F014) | numerics/op12_theta/ENGINE_OP1_op12_runner.py |
| m₀² in OP-12 runner | 0.5 | comparator parameter | **open lineage question:** numerically = σ_A at N=3,g₀=a=1 (F016 §4.4) — AND = brown's m² := c_H/2 under c_H = 1 normalization (F021 §4); two candidates, for Alex |
| One-plaquette exact set | Δ±(β) six coefficients; c-odd closed forms; t₊=−11/306; d₃=−109151/249696; bands | Casimir, y=2β/3 | master doc v2.7 §§1–2, 8 (gate-backed; see whitelist) |
| N\* (HS certificate radius) | 29–68 across L=4/6/8 | comparator (m₀²=0.5, v₀=1) | numerics/op12_theta/ M1/M2 (exact, all gates pass) |
| T_C closed form | (3/4)(1/Ns)Σ_{k≠0}(m₀²+α_Wλ(k))⁻²; diagonal law α²T_C = (3/64π²)(2 ln s + ln α + C), C ≈ 3.890 | **Casimir** (α_W = β/6; convention-pinned — the 3/64π² coefficient changes under trace norm) | m4_scaling/NOTE_OP1_m4_tc_asymptotics_2026-06-12.md (gates F1–F5 + real-space cross-check) |
| Diagonal closure exponent | q + c_af·κ(δ) > 2; q=0 threshold κ_req = 2/c_af = 32π²/11 ≈ 28.712 (N=3); measured κ̂(δ=0.7/0.9/1.1) = 1.24/1.85/2.57 | Casimir; AF diagonal L=4s, anchor β₀=5.6; v₀ = c_v·a^q | same note §3 + CERT_OP1_m4_sparsity_interface.json (gates D1–D4; κ̂ caveats apply) |
| Ceiling-law constants (M4 Tier-2) | α-form: D∞ = 0.0213019402 (renormalized integral, F030), D_crit = 0.0447517251; β-form: C_sat = 0.0127921031, C_crit = 0.0362418881; **exact offset (A/2)ln 6 = 0.0085098369** | Casimir; AF diagonal; A = 3/32π², law Y = A ln s + (A/2)ln(α or β) + const | F028 `AUDIT_OP1_m4_ceiling_pin.json` + F030 audits. **Live trap (factor-2 species): a D-constant quoted without its ln-argument normalization (α vs β) is ambiguous by 0.0085 — state the form** |
| log μ̄ (plaquette-animal growth) | log μ̄ = 1 + log 20 = 3.9957 (PROVED; rooted, link-sharing adjacency, Δ = 20); true connective constant ≈ 25–35 (exact a₂..a₄ = 20, 458, 11132) | combinatorial (convention-free) | NOTE_FLUX_s_chessboard_route_2026-06-12.md Lemma A, verified F029; gate G-S4 |
| Lemma-B certified bound (M4 Tier-2) | **G_BOUND = 0.018664535031** (exact rational, < 1/28; margin 0.0170498, ×1.91) | β-form (C-constants); T0 = 2 split; μ² ∈ (0, 15/28] exact | F031: proof `LEM_OP1_lemma_b_proof_2026-06-12.md`, certificate `LEM_OP1_lemma_b_cert.json` LB6 (rational-exact). **Quoting rule: G_BOUND is the *proved* envelope of C_inf (theorem-grade); C_sat = 0.0127921031 is the *measured/derived* sup (audit-grade) — cite the one matching the claim's grade** |
| Lemma-A theorem constants (M4 Tier-2) | τ₀ = 0.31 (Region-A ext, h_A2 = 0.8879); L₀ = 12 (uniform sweep); R̄ = 1.19 (certified cap); **sup_t r(t) = 1.17511 at t ≈ 0.40** (true; the "r(0.5) = 1.16748 peak" in June-12 session messages was WRONG — that is a sample, not the sup) | Casimir; τ = t/L²; r = √(4πt)q | F033: `LEM_OP1_lemma_closure_2026-06-12.md` + `LEM_OP1_lemma_window_cert.json` WB0–WB5. Floors N\*_C ≥ 8 / N\* ≥ 7 now UNCONDITIONAL (cite F033 + F031 + F032 chain, not any single note) |

## 4. Operational checklist for any new derivation or paper section

1. State the inner product (trace vs Casimir) in the first display where a Hessian or Casimir appears.
2. State the reference measure (dvol_g vs Lebesgue) before writing Ric_μ = Ric + ∇²S.
3. When importing a constant from another era, run it through §1/§3 of this page and cite the row.
4. If a constant's convention cannot be determined from its source — stop and flag (records/review ledger), don't guess. Precedent: the b7–b10 transcription protocol (master doc §6.4).
