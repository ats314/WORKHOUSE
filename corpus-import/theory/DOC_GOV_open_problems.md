<!-- LIVE WORKING COPY as of June 12, 2026. Canonical history: E:\YANG\ORGANIZED\CLAUDE_REVIEW\10_DOC_GOV_open_problems.md (frozen same date, points here). Update THIS file going forward. -->

# Open Problems — live research targets

**Date:** April 3, 2026 (Pass 3); **reframed June 13, 2026 per `CHARTER.md` + DECISIONS #010** — these are open mathematical targets, NOT steps in a Millennium-prize attempt. Read any "closes the mass gap / continuum" tier framing below as legacy provenance ("what this target would feed"), not as an active goal. The live bottleneck is OP-1's stochastic sparsity lemma (S).
**Purpose:** the project's open questions as precise statements that can be (a) attacked analytically, (b) verified numerically, or (c) formalized in Lean. Each is self-contained with exact hypotheses and conclusion.

---

## Tier 1: Core targets (highest-leverage open problems)

### OP-1: Birman-Schwinger Closure Along the Asymptotic Freedom Trajectory

**Status:** The single most important open problem in the project.

**Setup.** Let Λ_L = (Z/LZ)⁴ with Wilson action at coupling β. Define the massive Maxwell comparator

$$M_a = m_0^2(a) I + \alpha_W(a) d_1^* d_1$$

on 1-cochains (oriented links), and the Birman-Schwinger operator

$$K_a(U) = M_a^{-1/2} V_a(U) M_a^{-1/2}$$

where V_a(U) = v₀ Π_{D(U)} projects onto defect links (those with dist(U_b, 1) > r₀).

**Problem.** Under the asymptotic freedom scaling β(a) = (11N)/(48π²) · log(1/(aΛ)²) + ..., prove:

$$\sup_{U \in \text{Typ}(\mu_a)} \|K_a(U)\|_{op} < 1 - \delta$$

for some δ > 0 independent of a, where Typ(μ_a) is the typical set of the Wilson measure (measure ≥ 1 − e^{-cL^4}).

**What's known:**
- The BS framework is complete: if ‖K‖ < 1 then γ_a(U) ≥ (1−‖K‖)m₀²(a)
- Under physical scaling, ‖K‖ = O(a²) → 0 IF defect density |D|/|E| stays bounded
- The d=4 resolvent mass has explicit closed form
- Defect density is controlled by Peierls-type estimates at large β

**What's open:** Proving defect sparsity uniformly along the AF trajectory, not just at β = ∞.

**Attack vectors:**
- (Numerical) Compute θ(a,U) for L ∈ {4, 6, 8, 12} at β values along the AF trajectory
- (Analytic) Peierls estimate for |D(U)| using the Wilson action's large-deviation rate function
- (Lean 4) Formalize the deterministic part: "given |D| ≤ D_max and v₀ ≤ v_max, then θ < 1"

**VERIDEX target:** The deterministic half (BS factorization + Combes-Thomas + HS norm bound → θ formula) is fully formalizable. The stochastic half (defect sparsity) requires measure theory.

**Addendum (June 11, 2026 — one-plaquette program cross-link).** The Wilson-defect program (Program B / PMBSF) recorded in `ORGANIZED/12_ONE_PLAQUETTE/master_docs/NOTE_FLUX_master_one_plaquette_program_v2_7.md` (§5) contains executed attacks on exactly this problem, as that program's documents report:

- **θ_phys audits (= OP-12):** Untitled185 v3b/v4 — θ_phys = sup⟨f,V(U)f⟩/⟨f,Mf⟩ with M = m²I + α d₁*d₁, Hodge-projected; L = 8–24, 50 cfgs, hot/cold starts, 3 weightings (β = 4, m² = 0.5): all SAFE, θ_phys p99 = 0.8541, p999 = 0.8779 < 1.
- **Peierls-regime reconnaissance (the analytic attack vector, probed numerically):** `ORGANIZED/12_ONE_PLAQUETTE/program_b_defect_probes/NB_RCAP_wilson_su3_rare_defect_peierls_probe_v2.ipynb` tests P(Γ ⊂ D_δ) ≤ K^|Γ| exp(−αβδ|Γ|), sweeping δ = 0.35–1.30 at β = 5.6–6.8, after a first run at δ = 0.35 marked 55–80% of plaquettes as defects at β = 4.8–6.0 (defect set percolated — not the Peierls regime).
- **Typical-set behavior:** v16_MATRIX_PASS — Wilson top-p plaquette masks vs uniform random masks of equal count (matrix-Laplace transfer): PASS at p ≤ 0.003 through L = 24 (max Δ_ML = 0.0180), FAIL at p = 0.01.
- **Recorded negative results (reusable failure modes):** Untitled193 — the A′ spike-residual route does not close (the Bernoulli edge-mask comparator consumes the budget; allowed M̄_max ≈ 2.4–3.3×10⁻⁴ at L = 24), and the trace-weighted finite-rank route is WEAK across δ.

Only the Peierls probe notebook is deposited in this repository; the remaining notebooks are inventoried in the master document. Full connection map: `ORGANIZED/00_META/ONE_PLAQUETTE_PROGRAM_CONNECTIONS.md`.

**Addendum 3 (June 11, 2026 — slack ledger, exact kernel constants, campaign plan).** The deterministic half of this problem has been re-based from estimate to exact computation: since M and the Hodge projector are configuration-independent, tr K² = v₀²Σ_{b,b'∈D}G_P(b,b')² has a fixed kernel, computed exactly in `ORGANIZED/04_SIMULATIONS/op12_theta_scan/NOTE_OP1_kchain_ledger_2026-06-11.md`. Results: (i) the OP-7 CT chain's ~10⁶ slack against measured θ decomposes as ~3×10⁵ in the kernel estimate and only 1.8–3.5× in the HS→op step; (ii) exact constants give a probability-free certificate **θ < 1 whenever |D| ≤ N\*** (N\* = 29–61 at L = 4–6, β = 5.6–7.2, m₀² = 0.5, v₀ = 1), validated against the scan; (iii) T_full decreases with both β and L — the favorable direction. Consequence for this problem: **OP-1 reduces cleanly to its stochastic half** — the defect-sparsity/Peierls inclusion bound (ρ-weighted kernel sums < 1), which remains OPEN and is the analytic target. Campaign structure, quantified targets for that lemma, and milestone ladder: `ORGANIZED/01_PROOFS/synthesis/PLAN_OP1_unif_closure.md`. The Lean target OP-7 should be re-pointed at the exact-kernel certificate (finite rational linear algebra) rather than the CT chain.

**Addendum 5 (June 12, 2026, late — deterministic side now fully analytic; the trajectory condition).** T_C (coexact HS budget) has an exact momentum-space closed form — (3/4)(1/Ns)Σ_{k≠0}(m₀²+α_Wλ(k))⁻² — verified against all prior kernel computations (2e-15) and by independent real-space CG at L=16/24 (7e-15). On the physical diagonal it grows logarithmically forever (α²T_C = (3/64π²)(2 ln s + ln α + C), confirmed to 0.5% out to L=512); the split-certificate budget N\*_split erodes like 1/ln(1/a) — but never to zero: a **uniform deterministic floor N\*_C ≥ 8, N\* ≥ 7 holds for ALL s** (Tier-1 finiteness PROVED, Tier-2 ceiling computed directly at the s≈3×10¹⁵ ridge; F027). Combined with measured Peierls exponents from the stored ensembles, the **diagonal closure condition is q + c_af·κ(δ) > 2** (v₀ ~ a^q): q=0 is structurally closed (needs κ > 32π²/11 ≈ 28.7; fixed-δ defects cap at O(2–4)); q=2 closes for any exponential sparsity. **The open analytic content of OP-1 is therefore (S)'s concentration/tail layer plus the v₀-scaling decision (Alex)** — see `programs/op1_defect_sparsity/PLAN_OP1_unif_closure.md` M4 Addendum 3 and `numerics/op12_theta/m4_scaling/NOTE_OP1_m4_tc_asymptotics_2026-06-12.md`.

**Addendum 4 (June 12, 2026 — M2 executed).** Pair-level exact certificates built and run (`op12_theta_scan/m2_certificates/`): 4 solves per (L,β) determine the whole kernel by translation invariance; per-config cert = exact √(tr K²) via lookups. All hard gates pass; fresh ensembles with stored defect sets: δ=1.1 certified 62/68 (91%), L=4 100%; pair-exact certifies up to ~2.5× beyond N\*; L=8 constants extend the favorable T_full trend to three volumes. Structural point for (S): |D| ∝ L⁴ at fixed (β,δ) outruns N\* — the open lemma must deliver density *scaling* along the trajectory, not smallness at fixed parameters. M3 (the sparsity lemma) remains the bottleneck and is unchanged.

**Addendum 6 (June 12, 2026, late evening — the analytic attack vector executed to Tier-R; F029/F030).** The "(Analytic) Peierls estimate … large-deviation rate function" vector above now has a first partial execution via reflection positivity + FILS chessboard: **P(Γ ⊂ D_δ) ≤ e^{−β(δ−1)|Γ|}** for arbitrary plaquette sets, conditional on the cited OS-RP/chessboard package (flags listed in the route note), with rooted summability for β(δ−1) > log μ̄ = 3.9957 (**the animal constant is now PROVED — first pinned value**) and uniformity along the trajectory automatic (rate monotone in β). Nonvacuous for β ≥ 8.9–40 depending on δ ∈ (1, 3/2]; the anchor (5.6, 1.1) is NOT covered — the remaining gap is localized to one expectation bound Ē₁ = E_{Z′}φ_p plus a sharper animal constant, both quantified (F029 §4). Deterministic side, same day: the Tier-2 uniform-floor pin is now two referee-ready lemmas (cover domination + infinite-lattice constant, ×2.8 margin on the constant), and the law constant D∞ = 0.0213019402 is a renormalized lattice integral (F030). Route note: `programs/op1_defect_sparsity/NOTE_FLUX_s_chessboard_route_2026-06-12.md`; engines: `numerics/op12_theta/s_chessboard/` + `m4_scaling/` audits.

**Addendum 7 (June 12, 2026, late night — Lemma B PROVED; F031).** The deterministic Tier-2 thread of Addenda 5–6 advances: **Lemma B is now a theorem** — C_inf(x) ≤ G_BOUND = 0.018664535031 < 1/28 uniformly on the diagonal, proved by an exact-rational certificate over one elementary *upper* Bessel bound (no monotonicity input; `programs/op1_defect_sparsity/LEM_OP1_lemma_b_proof_2026-06-12.md` + `numerics/op12_theta/m4_scaling/ENGINE_OP1_lemma_b_cert.py`, gates LB0–LB9 ALL PASS, in-store cold run). **The uniform deterministic floors N\*_C ≥ 8 / N\* ≥ 7 for all s are now conditional on Lemma A (cover domination) alone.** The same-day session-P intake (F031) proves Region A (t ≥ 0.4L²) of Lemma A — **reviewed-proved, F032** — localizing the remaining deterministic work to the compact window τ = t/L² ∈ (0, 0.4] (uniform numeric margin 0.0396 there, independently reproduced).

**Addendum 8 (June 12, 2026, late night — LEMMA A PROVED; the Tier-2 floors are unconditional; F033).** The compact window is closed: Region-A extension to τ₀ = 0.31 (h_A2(0.31) = 0.8879 < 1) + a certified min{exact-difference, convexity} cell sweep — uniform in L ≥ 12 via the Λ\*-monotonicity 2Λ\*(v) ≥ vΛ\*′(v) (one L₀ = 12 sweep covers all larger L), per-L for 4..11, with the new **contour-shift wrap bound p_k(t) ≤ e^{−tΛ\*(k/t)}·q(√(t²+k²/4))** (prefactor-sharp, one-line Cauchy) and **r ≥ 1 for t ≥ 3** as the only Bessel inputs. Worst certified cells 0.945–0.955 (margins 4.5–5.5%, binding at the τ = 0.31 corner). **Hence Φ_L⁴ − L⁻⁴ ≤ q⁴ everywhere, and with Lemma B (Addendum 7): T_C(L) ≤ T̄(1/28) = 0.124806 < 1/8 ⟹ N\*_C ≥ 8, T_full < 9/64, N\* ≥ 7 for every integer L ≥ 4 on the diagonal — UNCONDITIONALLY.** The deterministic side of this problem is closed at every tier (Tier-1 F027; Tier-2 here; exact kernel certificates M1/M2). **OP-1's open content is now exactly its stochastic half (S) — Theorems Z.A/Z.B or the chessboard route — plus the v₀-scaling decision (STATE #0).** Proof: `programs/op1_defect_sparsity/LEM_OP1_lemma_closure_2026-06-12.md`; certificate `numerics/op12_theta/m4_scaling/ENGINE_OP1_lemma_window_cert.py` (WB0–WB5); finding F033.

**Addendum 9 (June 12, 2026, late night — chessboard (S) single-class route is a dead-end for the sparse channel; F034).** Direct measurement of the chessboard Tier-S target Ē₁ = E_{Z′}φ_p (Z′ = one orientation class removed = the faithful chessboard product measure) gives **Ē₁ ≈ 1** (1.003 @ β=5.6, 0.961 @ 7.2; sampler G-Z1-calibrated vs deposited ⟨φ⟩), not the route note's hoped ≲ 0.49 — those plaquettes disorder to near-free-Haar. So the k_x = 1 (sparse-animal) channel gets Tier-S rate β(δ−1), no better than Tier-R, exactly where the entropy (up to log μ̄ = 3.996) is largest: **the chessboard route cannot reach the anchor.** This retires one (S) sub-route (joining the prior four) and **redirects the highest-value (S) lever to the δ-window-vs-gap-protection question** (Alex's call against `NOTE_OP1_unif_gap_protection_factorization.md`): if δ = 1.3–1.45 is tolerated, Tier-R alone covers the trajectory tail and only a bounded-β window near the anchor needs (S) by other means. Z.A/Z.B (M3a) stay the covariance-form bottleneck. Finding F034; engine `numerics/op12_theta/s_chessboard/ENGINE_OP1_z_prime_mc.py`. (S), Z.A/Z.B, and the v₀-scaling decision are untouched — the OP-1 bottleneck remains M3a.

---

### OP-2: Physical-Units Coercivity (★)

**Status:** The master inequality; everything downstream is mechanical if this holds.

**Statement.** For the lattice Yang-Mills measure μ_a on Λ_L at coupling β(a), prove:

$$a^{-2} \mathcal{E}_a(f, f) \geq \rho_{\text{phys}} \cdot \text{Var}_{\mu_a}(f)$$

for all gauge-invariant f, with ρ_phys > 0 independent of a and L.

**What's known:**
- Local (single-stencil) version follows from HK calibration + Holley-Stroock
- Global version requires defect patching (OP-1) or block-Schur dominance (OP-3)

**Relation to OP-1:** OP-2 follows from OP-1 + the HK-Wilson calibration chain.

---

### OP-3: Block-Schur Dominance at Fixed Physical Scale

**Status:** An alternative to OP-1 that packages the same content differently.

**Statement.** There exist ℓ > 0, σ_geom > 0, and ρ* > 0 such that for blocks B(a) of physical diameter ℓ:

$$\sup_{a \downarrow 0} \frac{M(B(a))^2}{\gamma(B(a))} < \sigma_{\text{geom}} - \rho_*$$

where M = ‖∇²_{x_B x_{B^c}} S_a‖_op (mixed Hessian) and γ = inf spec(∇²_{x_{B^c} x_{B^c}} S_a) (fiber coercivity).

**What's known:**
- The Schur complement identity (deterministic) is proven
- σ_geom = h∨/2 as a mathematical statement about the Jacobian Hessian
- The physical scaling predicts M² ~ a⁰ and γ ~ a⁻² so M²/γ ~ a² → 0

**Attack vector:** Direct numerical computation of M, γ, and the ratio on small lattices.

---

## Tier 2: Problems That Complete the Continuum Limit

### OP-4: Tightness of Lattice Measures in Cylinder Coordinates

**Status:** The remaining bottleneck for Mosco convergence.

**Setup.** Let μ_a be the Wilson lattice gauge measure, and let Φ_a: configurations → cylinder coordinates (via holonomies along a fixed set of paths).

**Problem.** Prove that the family {(Φ_a)_*μ_a}_{a>0} is tight in the topology of Mosco convergence.

**What's known:**
- If (★) holds uniformly, tightness follows from Herbst concentration + Prokhorov's theorem
- The Carré du champ matrices Q_a converge: ‖Q_a − Q‖ ≤ C_I · a with Q_a ≼ 24I (4D)
- The recovery sequence construction (via Yang-Mills heat flow) is identified

**Relation to OP-2:** Downstream. If OP-2 is solved, OP-4 follows.

---

### OP-5: Reflection Positivity Preservation Under Mosco Limit

**Status:** The hardest step in the OS reconstruction.

**Problem.** Show that if μ_a satisfies reflection positivity (known for Wilson action) and E_a → E_∞ in the Mosco sense, then E_∞ also satisfies reflection positivity.

**What's known:**
- For Φ⁴₃: Gubinelli-Hofmanová (2021) proved this using stochastic quantization
- For Yang-Mills: the gauge structure introduces complications (gauge orbits are not reflected simply)
- The cut-torus gauge slice map (OP-8) is needed to handle boundary conditions

**Template:** Adapt the Gubinelli-Hofmanová argument, replacing the scalar field structure with gauge-covariant heat flow.

---

### OP-6: Osterwalder-Schrader Reconstruction with Spectral Gap

**Status:** Standard once RP + spectral gap are established; the hard part is RP.

**Problem.** Given reflection positivity + spectral gap ρ_phys of the continuum Dirichlet form E_∞, construct the physical Hilbert space H and Hamiltonian H with spec(H) ⊂ {0} ∪ [Δ, ∞) where Δ ≥ ρ_phys.

**What's known:** This is textbook OS reconstruction (Glimm-Jaffe, Chapter 6). The only content is verifying hypotheses.

---

## Tier 3: Formalizable Building Blocks (VERIDEX Priority)

### OP-7: Lean 4 Formalization of the BS Closure Chain

**Status:** The highest-priority VERIDEX target.

**Scope:** Formalize the following deterministic chain in Lean 4:

1. **Combes-Thomas decay:** For M = m²I + α d*d on a finite graph, prove |(M⁻¹)(b,b')| ≤ (2/m²) q^{d(b,b')} with q = (1 + m²/(2αD_E))⁻¹.

2. **HS norm bound:** For K = M⁻¹/² V M⁻¹/², prove ‖K‖_HS² ≤ (2v₀/m²)² |D| · Ξ₂,tot(q).

3. **d=4 resolvent mass:** Prove Ξ₂,tot(q) ≤ c_E ((1+q²)/(1−q²))⁴ with c_E = 4 or 8.

4. **Closure:** Chain 1-3 to get the explicit θ formula.

**Mathlib status:**
- Matrix inverses, norms, operator theory: partially available
- Graph theory basics: available in Mathlib
- Shell counting on Z⁴: needs custom development
- Combes-Thomas: not in Mathlib (but the proof is elementary)

**Estimated effort:** Medium-high. The mathematics is linear algebra on finite-dimensional spaces — no measure theory, no topology, no infinite-dimensional analysis. Every object is bounded and every sum is finite.

**Addendum (June 12, 2026 — F019):** `02_APPENDICES/red_propositions/` holds an unused sharper-decay toolkit aimed at exactly this chain: Davies-type decay for (m²I + αd₁\*d₁)⁻¹ with **row-sum constants C₀/C_∂ in place of the global degree D_E** (Props 9.X/9.X′/9.X″ + row-sum definitions). Since the CT chain's known slack is ~10⁵–10⁶ in the q → 1 regime (Addendum 2 above), cross-reading these against the exact-kernel ledger (`04_SIMULATIONS/op12_theta_scan/KCHAIN_LEDGER`) is review unit **#10d** — it may re-point this problem's formalization target a second time.

**Addendum 2 (June 12, 2026 — F020, #10d executed):** the swap was run mechanically on the June-11 chain (`numerics/op12_theta/ENGINE_OP1_red_davies_kchain.py`, 35 hard gate checks in 7 families pass; chain structure byte-identical, only the decay constant replaced). Computed: **C₀ = C_∂ = D_E = 18 exactly** for this comparator at L = 4, 6 — the row-sum refinements (9.X′/9.X″) buy nothing here — but **Prop 9.X's Davies (arcosh) rate alone tightens the chain bound ×133–172** (S_kernel 3.2–9.0×10⁵ → 2.4–5.2×10³; per-√|D| constant 5.2–8.5×10⁴ → 389–497 vs exact √T_full = 0.127–0.186, residual ~2–4×10³). Pointwise Davies bound dominates exact M⁻¹ columns (max ratio 0.15). Chain-level certification remains vacuous at these parameters (bound < 1 needs |D| ≲ 10⁻⁵): the exact-kernel N\* certificate stays the sharp instrument; the Davies form matters for the *analytic* chain (m-vs-m² small-mass scaling). P-transfer (M⁻¹ → PM⁻¹P) caveat carried, unresolved — as in the June-11 ledger. **Whether to re-point this problem's analytic/Lean target at the Davies chain is Alex's call.** Materials: `programs/op1_defect_sparsity/red_davies_toolkit/` (MD5-verified copies + outcome README), `numerics/op12_theta/NOTE_OP1_red_davies_results_2026-06-12.md`, finding F020.

---

### OP-8: Lean 4 Formalization of the Cut-Torus Slice Map

**Status:** Second-priority VERIDEX target. Pure combinatorics.

**Scope:** Formalize:
- Given a periodic lattice Λ_L = (Z/LZ)^d and a gauge field U with all plaquettes within r of identity
- The cut-torus gauge transform g(x) = Hol_U(γ_x) satisfies:
  - For non-seam edges: dist((g·U)_b, 1) ≤ (d−1)(L−1) · r
  - For seam edges: dist((g·U)_b, T_μ) ≤ C_tor(L) · r

**Mathlib status:**
- Graph theory: available
- Metric spaces with triangle inequality: available
- Group actions: available
- Specific Lie group geometry: would need axiomatization

**Estimated effort:** Medium. The proof is a path-counting argument + iterated triangle inequality.

---

### OP-9: Lean 4 Formalization of the Weyl Curvature Floor

**Scope:** Formalize Theorem 2.1: for SU(N) with standard normalization,

$$\nabla^2 S_{\text{geom}}(\theta) \succeq \frac{N}{2} I \text{ on } \{\sum_i \theta_i = 0\}$$

**Proof structure in Lean:**
1. csc²(x) ≥ 1 for all x ∈ (0, π)
2. Hessian = Σ (1/2)csc²(⟨α,θ⟩/2) (α⊗α) ≽ (1/2) Σ (α⊗α)
3. Root-system identity: Σ_{α∈Φ⁺} (α⊗α) = h∨ · Id on the Cartan subalgebra
4. For SU(N): h∨ = N

**Estimated effort:** Medium. Steps 1-2 are real analysis. Step 3 requires formalizing the root system of SU(N). Step 4 is a fact about the dual Coxeter number.

---

### OP-10: Bakry-Émery Infrastructure

**Scope:** Build the Lean 4 library for:
- Carré du champ Γ(f,g) = (1/2)(L(fg) − fLg − gLf)
- Iterated Γ₂(f) = (1/2)LΓ(f) − Γ(f, Lf)
- CD(ρ,∞) condition: Γ₂(f) ≥ ρΓ(f)
- CD(ρ,∞) → Poincaré inequality with constant 1/ρ
- CD(ρ,∞) → Log-Sobolev inequality with constant 2/ρ

**Mathlib status:** Γ₂ calculus is NOT in Mathlib as of v4.26. This is a significant infrastructure gap.

**Estimated effort:** High. This requires building the entire diffusion semigroup + curvature-dimension framework. Worth doing because it's reusable infrastructure for many applications beyond Yang-Mills.

---

## Tier 4: Numerical Experiments (Not Formalizable, but Essential)

### OP-11: Resolve the RG Blocking Obstruction

Run the three diagnostics on the blocking proxy Φ_proxy:
1. Enforce projector consistency: pushforward the fine-scale coexact projector vs. recompute on the blocked lattice
2. Separate toron sectors before and after blocking
3. Correlate Φ_proxy with the Schur ledger term M²/γ

If naive blocking fails but heat-flow blocking preserves the gap → publishable result.
If both fail → fundamental obstruction to the RG approach.

### OP-12: Direct θ Computation

For SU(2) and SU(3) on lattices L ∈ {4, 6, 8, 12} at β along the AF trajectory:
1. Sample gauge configurations from the Wilson measure
2. Identify defect set D(U) = {b : dist(U_b, 1) > r₀}
3. Build M_a = m₀²I + α_W d₁*d₁
4. Compute θ(a, U) using the explicit formula
5. Plot θ vs. a (or β) and check whether θ < 1

This is the most direct numerical test of whether the BS framework closes.

**Addendum (June 11, 2026).** Threshold calibration data now exist: the one-plaquette program's Peierls probe (`ORGANIZED/12_ONE_PLAQUETTE/program_b_defect_probes/NB_RCAP_wilson_su3_rare_defect_peierls_probe_v2.ipynb`) reports that δ = 0.35 marks 55–80% of plaquettes as defects at β = 4.8–6.0 (the defect set percolates), and sweeps δ = 0.35–1.30 at β = 5.6–6.8 to locate the rare-defect regime. Step 2's r₀ should be checked against this sweep before interpreting any θ computation. Prior θ_phys audits at L = 8–24 (all SAFE, p99 = 0.8541 < 1) are recorded in `ORGANIZED/12_ONE_PLAQUETTE/master_docs/NOTE_FLUX_master_one_plaquette_program_v2_7.md` §5.

**Addendum 2 (June 11, 2026 — OP-12 EXECUTED along a β ladder).** Deposited at `ORGANIZED/04_SIMULATIONS/op12_theta_scan/`: SU(3) Wilson MC at L = 4 (β = 5.6–7.2, 20 cfgs) and L = 6 (3 β values, 12 cfgs), plaquette-seeded defect sets at Peierls-calibrated thresholds δ ∈ {0.7, 0.9, 1.1}, θ = v₀·λmax(Π_D P M⁻¹ P Π_D) computed exactly per configuration (hard-gated; m₀² = 0.5, α_W = β/6, v₀ = 1). Results: θ < 1 with margin at every point in the sparse regime (δ ≥ 0.9: θ_max 0.55 → 0.18 along the L = 4 ladder), monotonically decreasing in β, volume-stable L = 4 → 6; the firewall fails (θ_max ≈ 1.13–1.20) only at the near-percolating point δ = 0.7, β = 5.6 — confirming sparsity as the load-bearing hypothesis. The deterministic OP-7 HS-chain bound evaluates to 10⁵–10⁶ at these parameters (q → 1 regime), i.e. ~6 orders of magnitude looser than measured θ — the analytic route needs the physical-units scaling or a sharper-than-HS argument. Caveats (thermalization ~2–3% high on ⟨plaq⟩, fixed comparator parameters, small statistics) in `NOTE_OP1_results_2026-06-11.md`. **Status: evidence along the ladder; the uniform analytic bound remains the open content of OP-1.**

---

## Problem Dependency Graph

```
OP-1 (BS closure) ←→ OP-3 (Block-Schur)
       ↓
OP-2 (Physical coercivity ★)
       ↓
OP-4 (Tightness)
       ↓
OP-5 (RP preservation)  ←  [Gubinelli-Hofmanová template]
       ↓
OP-6 (OS reconstruction)
       ↓
   MASS GAP

VERIDEX targets (independent, can start now):
OP-7 (BS chain)     — highest priority
OP-8 (Cut-torus)    — combinatorial, clean
OP-9 (Weyl floor)   — real analysis + Lie theory
OP-10 (Bakry-Émery) — infrastructure, high effort
```

---

### OP-13: Riccati Synthesis Formalization (NEW — Pass 7)

**What:** Formalize the vHJ equation and Riccati fixed point analysis from Synthesis_03_Renormalization_Riccati.md (1100+ lines of professional-grade math physics).

**Scope:** Three formalizable components:
1. dλ/dt ≥ −2λ² + σ(t) comparison principle (finite-dimensional ODE)
2. Fixed point analysis: λ(∞) ≥ √(σ_min/2) (asymptotic stability)
<!-- OP-13 tail through OP-14 and the Recommended Attack Order section restored 2026-06-14 from E:\YANG\ORGANIZED\CLAUDE_REVIEW\10_DOC_GOV_open_problems.md (frozen June-12 sibling) after a write-truncation; all live OP-1 addenda above are preserved. -->
3. Anomaly-curvature identity: σ_anom = κ·β(g)/g·⟨F²⟩ > 0 (algebraic identity + positivity)

**Why it matters:** This is the PRECISE mathematical mechanism for why the mass gap survives RG flow. Without it, the gap vanishes as a → 0. With it, the gap stays positive at a uniform lower bound.

**Estimated effort:** Medium-high. Mathematics is self-contained. Component 1 is an ODE comparison principle (standard). Component 2 is fixed-point theory. Component 3 requires connecting to gauge theory constants.

**Priority:** ★★★★★ — Co-equal with OP-7 (BS chain). The 1100+ lines of synthesis make this the richest single Lean formalization target.

---

### OP-14: Flat-Band / Gauss-Law and Domino Constants Formalization (NEW — added June 11, 2026)

**What:** Formalize the exact strong-coupling band results of the one-plaquette program (`ORGANIZED/12_ONE_PLAQUETTE/`):

1. The incidence factorization Ñ(k) + 4I = B(k)B(k)† and det Ñ(k) ≡ 0 — the exactly flat C-odd band as ker B† (3×3 symbolic Bloch matrices)
2. The cube-boundary CLS eigenvector (∂∂ = 0 on twelve edges) and the L³+2 kernel dimension on the L³ torus
3. The link-mediated robustness theorem: any correction B M B† annihilates the flat subspace
4. The two-plaquette domino level rationals {1769/3060, 13/20}, {31/68, 17/36} and d₃ = −109151/249696

**Why it's cheap:** Finite symbolic linear algebra and exact rational arithmetic — no measure theory, no topology, no infinite-dimensional analysis (compare OP-7's profile, which it resembles but undercuts). The claims are already machine-certified in Python (400+ hard gates per the program's master document); Lean would upgrade certificate-style verification to proof.

**Connections:** P08 supplies the charge-conjugation sector decomposition these results live in; MaxwellOperator.lean already handles incidence-operator structure; the protection mechanism is discussed in `ORGANIZED/01_PROOFS/synthesis/NOTE_OP1_unif_gap_protection_factorization.md`.

**Estimated effort:** Low-medium.

**Priority:** ★★★ — not load-bearing for the mass gap, but the cheapest path to a fully formalized nontrivial spectral theorem in the workspace, and a good warm-up for OP-7's operator bookkeeping.

---

## Recommended Attack Order

**For VERIDEX (formalization):**
1. **OP-7 (BS chain) and OP-13 (Riccati synthesis)** — co-equal highest impact; finite-dimensional and ODE-based respectively
2. OP-8 (Cut-torus) — combinatorial, good warm-up for graph-theoretic Lean
3. OP-9 (Weyl floor) — involves real analysis and Lie theory
4. OP-10 (Bakry-Émery) — heavy infrastructure, do last
5. OP-14 (flat band / domino rationals) — cheapest exact-arithmetic wins, parallel warm-up to OP-8 *(added June 11, 2026)*

**For numerics:**
1. OP-12 (Direct θ computation) — most direct test of the framework
2. OP-11 (RG blocking) — potential showstopper, must be resolved
3. Extend E04 (curvature-mass proportionality) with proper statistics

**For analysis (hardest):**
1. OP-1/OP-3 (defect sparsity / Block-Schur) — THE bottleneck
2. OP-5 (RP preservation) — needs new ideas beyond the Φ⁴₃ template
3. OP-4 (tightness) — follows from OP-1 if solved

---
