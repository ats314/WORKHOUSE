# M4 — Exact closed forms for the comparator kernel constants, with a uniform ceiling along the AF diagonal

**Date:** June 12, 2026
**Author:** session agent (lead math agent per DECISIONS #009), for Alex
**Engine:** `ENGINE_OP1_m4_tc_closed_form.py` → `CERT_OP1_m4_tc_closed_form.json` (all gates hard asserts)

**Status labels (per CLAUDE.md rules 4/6/10 and DECISIONS #009):**
- §1 Theorem 1 + Corollary: **PROVED here** (complete proof below), **verified at machine precision** three independent ways (G-CF1–G-CF5).
- §2 gate results and §3 tables: **EXACT / GATE-BACKED**.
- §4.1 Tier-1 ceiling: **PROVED here** (fully elementary, explicit constants).
- §3 law + §4.2 Tier-2 ceiling: analytic slope **derived**; constant term **numerically anchored** — status *rigorous-modulo two pins*, stated precisely in §4.2.
- §5 consequences: each item individually labeled GATE-BACKED / CONDITIONAL DERIVATION / OPINION.
- Scope: the OP-12 deterministic comparator on the 4-torus (m₀² > 0, v₀ = 1). **Nothing here touches CONJ_B, the stochastic lemma (S), or any continuum claim.**

---

## 0. Conventions and scope

Lattice Λ = (ℤ/Lℤ)⁴; cochain spaces C⁰, C¹, C² with counting-measure inner products; d₀: C⁰→C¹, (d₀φ)(x,μ) = φ(x+e_μ) − φ(x); d₁: C¹→C², (d₁A)(x,μν) = A(x,μ) + A(x+e_μ,ν) − A(x+e_ν,μ) − A(x,ν); d₁d₀ = 0. Comparator M = m₀²·I + α_W·d₁ᵀd₁ on C¹; P = orthogonal projector onto ker d₀ᵀ; G_P = P M⁻¹ P. Kernel constants per the M1/M2/M4 deposits (v₀ = 1): g_diag = G_P(b,b), T(b) = Σ_{b′} G_P(b,b′)².

The derivation is **convention-agnostic given (m₀², α_W)** — the factor-2 metric trap of DOC_GOV_conventions.md cannot enter, because the formula consumes (m₀², α_W) directly. All numerical rows use the Casimir row α_W = β/6 (N = 3), anchor (β₀, m₀², L₀) = (5.6, 0.5, 4), AF diagonal L = L₀s, m₀²(s) = 0.5/s², β(s) = β₀ + γ·ln s with γ = 2·33/(48π²) = 0.1393166.

---

## 1. Theorem 1 (closed forms) and proof

**Theorem 1.** Let ŵ(n) = Σ_μ 4 sin²(πn_μ/L) for n ∈ {0,…,L−1}⁴. Then for every L ≥ 2, m₀² > 0, α_W > 0:

| constant | exact value |
|---|---|
| g_H | 1/(m₀² L⁴) |
| T_H | 1/(m₀⁴ L⁴) |
| g_C | (3/(4L⁴)) Σ_{n≠0} (m₀² + α_W ŵ(n))⁻¹ |
| T_C | (3/(4L⁴)) Σ_{n≠0} (m₀² + α_W ŵ(n))⁻² |
| g_diag | g_H + g_C |
| T_full | T_H + T_C |

Moreover G_P(b,b) and Σ_{b′}G_P(b,b′)² are **constant over links** (previously a measured gate; now a theorem), and the harmonic/coexact cross term in T vanishes **identically** (deposit gate: cross_max ≤ 4·10⁻¹⁷).

**Proof.**

*(i) M commutes with P.* C¹ = im d₀ ⊕ ker d₀ᵀ. M preserves im d₀: M d₀φ = m₀² d₀φ since d₁d₀ = 0. M preserves ker d₀ᵀ: if d₀ᵀA = 0 then d₀ᵀ(d₁ᵀd₁ A) = (d₁d₀)ᵀ d₁A = 0. Both summands invariant ⇒ [M,P] = 0, and since M ⪰ m₀²I is invertible, G_P = M⁻¹P.

*(ii) Δ₁ is componentwise the scalar Laplacian.* With (d₀ᵀA)(x) = Σ_ν [A(x−e_ν,ν) − A(x,ν)] and (d₁ᵀF)(x,μ) = Σ_{ν≠μ}[F(x,μν) − F(x−e_ν,μν)] (convention F(x,νμ) = −F(x,μν)), expand both terms of Δ₁ = d₀d₀ᵀ + d₁ᵀd₁ at (x,μ). The ν = μ part of d₀d₀ᵀ gives 2A(x,μ) − A(x+e_μ,μ) − A(x−e_μ,μ). For each ν ≠ μ, d₁ᵀd₁ contributes 2A(x,μ) − A(x+e_ν,μ) − A(x−e_ν,μ) plus the cross block A(x+e_μ,ν) − A(x,ν) − A(x+e_μ−e_ν,ν) + A(x−e_ν,ν), while d₀d₀ᵀ contributes exactly the negative of that cross block, A(x+e_μ−e_ν,ν) − A(x+e_μ,ν) − A(x−e_ν,ν) + A(x,ν). The cross blocks cancel, leaving (Δ₁A)(x,μ) = Σ_ν [2A(x,μ) − A(x+e_ν,μ) − A(x−e_ν,μ)]. Hence on each Fourier fiber V_k = span{e_k ⊗ ε_μ} (k ∈ (2π/L){0,…,L−1}⁴), Δ₁|V_k = ŵ(k)·I₄.

*(iii) Fiber decomposition.* d₀ maps span{e_k} into V_k with image spanned by v(k) = (e^{ik_μ}−1)_μ, and |v(k)|² = ŵ(k). For k ≠ 0: the gauge line ℂ·v(k) carries d₁ᵀd₁ = 0 (by d₁d₀ = 0) hence d₀d₀ᵀ = ŵ(k); the transverse subspace W_k = V_k ∩ ker d₀ᵀ = v(k)^⊥ is 3-dimensional and carries d₀d₀ᵀ = 0, hence d₁ᵀd₁|W_k = Δ₁|W_k = ŵ(k)·I₃. For k = 0: v(0) = 0 and V₀ ⊂ ker d₀ᵀ ∩ ker d₁ — the 4 harmonic constant 1-forms h_μ, on which M = m₀². Dimension audit: (L⁴−1) gauge + 3(L⁴−1) coexact + 4 harmonic = 4L⁴. ✓

*(iv) Constants.* G_P therefore acts as 0 on the gauge band, 1/m₀² on V₀, and (m₀² + α_W ŵ(k))⁻¹ on each W_k. Site translations and the hypercubic point group act transitively on links and commute with G_P, so b ↦ G_P(b,b) and b ↦ (G_P²)(b,b) are constant, each equal to its normalized trace over the 4L⁴ links. Since G_P is symmetric, Σ_{b′}G_P(b,b′)² = (G_P²)(b,b). Reading the traces off the spectrum gives the table (the factor 3 is the transverse multiplicity; harmonic gives the 4/(m₀²·4L⁴) = g_H and 4/(m₀⁴·4L⁴) = T_H terms). With G_H = (1/m₀²)Π_{V₀} and G_C = G_P − G_H, G_H G_C = 0 as orthogonal spectral pieces, so the cross term in T vanishes identically. ∎

**Corollary (certificate radii, closed form).** With the deposit definitions (v₀ = 1):
N\* = ⌊1/T_full⌋,  N\*_C = ⌊1/T_C⌋,  N\*_split = max{ n ∈ ℕ : n·g_H + √(n·T_C) < 1 } — all elementary functions of (L, m₀², α_W). No linear solves are needed for any kernel-constant table in M1/M2/M4.

**Remark (off-diagonal).** The full kernel is also closed-form, G_P(b,b′) = harmonic piece + (1/L⁴) Σ_{k≠0} e^{ik·(x−x′)} [I − v̂(k)v̂(k)\*]_{μμ′} (m₀²+α_Wŵ(k))⁻¹; the W(r) shell tables are therefore in principle exact too (directional transverse projector). Not needed for this note.

---

## 2. Verification gates (all hard asserts; engine stage `gates`)

| gate | against | rows | worst rel. dev. | result |
|---|---|---|---|---|
| G-CF1 | `CERT_OP1_m4_harmonic_decomposition.json` — T_C, T_H, T_full, g_H + integer N\*, N\*_C, N\*_split | 17 | 9.7·10⁻¹⁵ | PASS (13 rounded-β rows, 4 exact-β rows) |
| G-CF2 | `CERT_OP1_kernel_consts.json` — T_full_max, g_diag, N\* | 10 | 2.3·10⁻¹⁵ | PASS |
| G-CF3 | `CERT_OP1_m4_scaling_tables.json` — T_full, g_diag, N\* | 9 | 1.5·10⁻¹⁴ | PASS (9/9 exact-β) |
| G-CF4 | **independent dense computation**, L = 4: explicit d₀, d₁ matrices, SVD gauge projector, direct solve; uses no deposited data | 1 | per-link std 1.9·10⁻¹⁶; values agree to 6·10⁻¹⁶ | PASS |
| G-CF5 | **second exact method**: heat-kernel/Bessel representation (§4.2) vs direct lattice sum | 6 rows L ≤ 64, + L = 256 | 9.2·10⁻¹⁶ (1.3·10⁻¹⁶ at L = 256) | PASS |
| G-CF6 | Tier-1 analytic bound dominates every computed T_C | all | — | PASS |

**Micro-finding (transcription precision; species of CONVENTIONS §4 item 4 / b7–b10 protocol).** The deposits store β rounded to 4 decimals while parts of the stored constants correspond to the *unrounded* β(s). Specifically, at machine precision: every `CERT_OP1_m4_scaling_tables.json` row was computed at the exact β(s) (closed form matches the exact-β reading to ≤ 9·10⁻¹⁵, the stored-rounded reading deviates by up to 6.9·10⁻⁶); in `CERT_OP1_m4_harmonic_decomposition.json`, the rows resumed from the scaling state (s ∈ {1, 1.5, 2, 3} at L ∈ {4,6,8}, plus (12, 1.0)) were computed **at the rounded β**, while the fresh rows (s = 1.25 ×3 and (12, 3.0)) used exact β. Maximum cross-reading discrepancy: 1.5·10⁻⁵ relative (T_C at L = 12, s = 3). **No integer radius is affected under either reading** (gate-checked). Recommendation: future deposits store β at full precision or record the generation rule; the affected tables are now trivially regenerable from Theorem 1 if uniformity is wanted. No deposit was modified (read-only mirror; owner's call). The two-reading structure is itself a small validation of the hard-gate culture: a 10⁻⁵-level inconsistency between two same-day engines was caught by the first independent recomputation.

---

## 3. Extended physical diagonal and the asymptotic law

Diagonal: (L, m₀², β) = (4s, 0.5/s², 5.6 + γ ln s). Engine stage `diagonal`; every row costs microseconds via Theorem 1. T_H = 1/(m₀⁴L⁴) = 1/64 exactly, for every s (m₀⁴L⁴ = 64 on this diagonal), and g_H = 1/(128 s²).

| L | s | β | T_C | T_full | N\* | N\*_C | N\*_split | Tier-1 bound |
|---|---|---|---|---|---|---|---|---|
| 4 | 1 | 5.6000 | 0.018838 | 0.034463 | 29 | 53 | 30 | 0.277 |
| 5 | 1.25 | 5.6311 | 0.021491 | 0.037116 | 26 | 46 | 32 | 0.312 |
| 6 | 1.5 | 5.6565 | 0.023583 | 0.039208 | 25 | 42 | 33 | 0.341 |
| 8 | 2 | 5.6966 | 0.026706 | 0.042331 | 23 | 37 | 32 | 0.387 |
| 12 | 3 | 5.7531 | 0.030757 | 0.046382 | 21 | 32 | 30 | 0.453 |
| 16 | 4 | 5.7931 | 0.033430 | 0.049055 | 20 | 29 | 29 | 0.499 |
| 20 | 5 | 5.8242 | 0.035412 | 0.051037 | 19 | 28 | 27 | 0.535 |
| 24 | 6 | 5.8496 | 0.036982 | 0.052607 | 19 | 27 | 26 | 0.564 |
| 32 | 8 | 5.8897 | 0.039378 | 0.055003 | 18 | 25 | 25 | 0.609 |
| 40 | 10 | 5.9208 | 0.041176 | 0.056801 | 17 | 24 | 24 | 0.643 |
| 48 | 12 | 5.9462 | 0.042611 | 0.058236 | 17 | 23 | 23 | 0.671 |
| 64 | 16 | 5.9863 | 0.044815 | 0.060440 | 16 | 22 | 22 | 0.714 |
| 80 | 20 | 6.0174 | 0.046477 | 0.062102 | 16 | 21 | 21 | 0.746 |
| 96 | 24 | 6.0428 | 0.047807 | 0.063432 | 15 | 20 | 20 | 0.773 |
| 128 | 32 | 6.0828 | 0.049854 | 0.065479 | 15 | 20 | 20 | 0.813 |
| 192 | 48 | 6.1393 | 0.052640 | 0.068265 | 14 | 18 | 18 | 0.869 |
| 256 | 64 | 6.1794 | 0.054549 | 0.070174 | 14 | 18 | 18 | 0.907 |

**The law.** Write y(s) := T_C(s)·α_W(s)². Heat-kernel (Bessel) representation — exact for every finite L, and the basis of gate G-CF5:

  T_C = (3/(4α_W²)) ∫₀^∞ t e^{−tμ²} ( Φ_L(t)⁴ − L⁻⁴ ) dt,  μ² = m₀²/α_W,  Φ_L(t) = Σ_{j∈ℤ} I_{jL}(2t) e^{−2t}.

For 1 ≪ t ≪ (L/π)², Φ_L(t) ≈ Φ_∞(t) = I₀(2t)e^{−2t} = (4πt)^{−1/2}(1 + O(1/t)), so the integrand ≈ t·(4πt)⁻² = 1/(16π² t) over the window t ∈ [O(1), O(min(μ⁻², (L/π)²))]. On the diagonal both IR scales co-scale ∝ s² (m_eff·L = 4√(3/β) drifts only 2.93 → 2.79 across the table), so the window contributes (1/(16π²))·ln(c·s²) = (1/(8π²))·ln s + const. Hence

  **y(s) = A·ln s + B + ε(s), A = 3/(32π²) = 0.00949886.**

Verification: global fit over ln s ∈ [1.10, 4.16] gives A_fit = 0.0096426 (ratio 1.0151 to the analytic value), B_fit = 0.017833; the **local slopes decrease monotonically** 0.011292 → 0.0095473 across the table, i.e. to within 0.51% of A at the last interval, with the residual visibly O(1/ln s) plus the slow m_eff·L drift. The slope of T_C itself at the anchor, A/α_W² ≈ 0.0109, reproduces the deposit's measured per-step growth (+25%, +13%, +15% per ln-step in the 17-row table).

---

## 4. Uniform ceiling along the AF diagonal

### 4.1 Tier-1: fully elementary rigorous bound (PROVED)

*Lemma.* sin(πj/L) ≥ 2j/L for 0 ≤ j ≤ L/2 (concavity of sin on [0, π]). Hence with the minimal image m(n) (m_μ = min(n_μ, L−n_μ) ∈ [0, L/2]): ŵ(n) ≥ (16/L²)|m|².

Dropping m₀² ≥ 0 and substituting into Theorem 1:

  T_C ≤ (3/(4L⁴)) Σ_{n≠0} (α_W·16|m|²/L²)⁻² = (3/(1024 α_W²)) Σ_{0<|m|∞≤L/2} |m|⁻⁴.

Small shells exactly: c₀ := Σ_{0<|m|²≤8} |m|⁻⁴ = 25.323345 (shell counts 8, 24, 32, 24, 48, 96, 64, 24 for |m|² = 1…8). Far shells by cube comparison: for |m| ≥ 3, on the unit cube C_m = m + [−½,½]⁴ one has |x| ≤ |m| + 1 ≤ (4/3)|m|, so |m|⁻⁴ ≤ (4/3)⁴ |x|⁻⁴ there; the C_m are disjoint and ∪C_m ⊂ {2 ≤ |x| ≤ L+1}; hence Σ_{|m|≥3} |m|⁻⁴ ≤ (4/3)⁴ ∫_{2≤|x|≤L+1} |x|⁻⁴ d⁴x = (4/3)⁴·2π²·ln((L+1)/2). Therefore

  **Tier-1: T_C ≤ (3/(1024 α_W²)) [ c₀ + (4/3)⁴·2π²·ln((L+1)/2) ]** for every (L, m₀², α_W).

Gate G-CF6 confirms domination on every computed row (it is ≈ 15–19× loose; e.g. 0.907 vs 0.0545 at L = 256). Along the diagonal the bound's supremum is **T̄₁ = 2.168**, attained near ln s = 38. Consequence, with no unproved input of any kind: **the coexact kernel constant is uniformly bounded along the entire AF trajectory.** Tier-1's constant is however too weak for a nontrivial uniform radius (1/T̄₁ < 1).

### 4.2 Tier-2: sharp ceiling (analytic slope; constant numerically anchored)

Maximizing the law (A x + B)(6/β(x))² with β(x) = β₀ + γx gives x\* = β₀/γ − 2B/A. Numbers:

- with (A_fit, B_fit): **x\* = 36.50, s\* = 7.1·10¹⁵, β\* = 10.685, T̄_C = 0.11660 ⇒ uniform N\*_C ≥ 8**;
- robustness — pinning A = 3/(32π²) exactly and anchoring B′ = y(64) − A·ln 64 = 0.018355 through the largest computed point: x\* = 36.33, T̄_C = 0.11511, **same integer floor N\*_C ≥ 8** (ceiling sensitivity 1.3%).

Since T_H = 1/64 exactly, this also gives a uniform full-HS radius **N\* ≥ ⌊1/(1/64 + 0.1166)⌋ = 7** along the whole diagonal, and N\*_split → N\*_C from below as g_H = 1/(128s²) → 0.

**Status, stated precisely.** The slope A is analytic; the Bessel representation it comes from is exact at every finite L with quadrature/truncation tails explicitly bounded in-engine (≤ 2.7·10⁻¹¹ at the heaviest row). The two pins that keep Tier-2 short of "fully proved" are: (i) the constant B is anchored numerically (the window-endpoint contributions to ε(s) are not yet two-sidedly bounded), and (ii) the ceiling extrapolates the law from ln s ≤ 4.16 to x\* ≈ 36.5. The upgrade path is mechanical — Euler–Maclaurin/theta-tail bounds on Φ_L giving a rigorous two-sided B-window — a bounded-effort follow-up, **flagged, not claimed**. Tier-1 already guarantees the qualitative statement unconditionally.

### 4.3 Past the turnover

For s > s\*, asymptotic freedom wins: T_C(s) ≈ (36A/γ²)/ln s ≈ 17.6/ln s → 0 — the instrument *recovers*. s\* ~ 10¹⁶ is structural information only; every reachable computation lives on the rising log branch, which is exactly what the deposits saw.

---

## 5. Consequences for the campaign (each item labeled)

**[GATE-BACKED / THEOREM]**
1. Every kernel-constant table in M1/M2/M4 is now generated by an elementary formula — CG solves are obsolete for these constants; 36 deposited rows reproduce at machine precision; any future (L, β, m₀²) row costs microseconds.
2. Per-link constancy of g_diag and T, and the exact vanishing of the harmonic/coexact cross term, are theorems (previously measured gates).
3. The deposit's empirical "T_C scaling-stable, ×1.63 over 17 rows, no limit claim" upgrades to: exact law with analytic slope 3/(32π²), **unconditional uniform finiteness** (Tier-1), and a sharp uniform ceiling **N\*_C ≥ 8, N\* ≥ 7 for all s ≥ 1** (Tier-2, modulo the two pins of §4.2).
4. The harmonic sector's weight on the diagonal is exactly g_H = 1/(128s²) and T_H = 1/64: rank-4, explicitly handled, and the split certificate's harmonic half *improves* with s. The entire scaling burden of the deterministic side is the coexact logarithm — now controlled.

**[DERIVATION, CONDITIONAL on the Peierls-form ansatz ρ(β) ≤ C e^{−cδβ}]**
5. A *global* HS count certificate along the diagonal needs |D| ≈ 4ρL⁴ = 4ρL₀⁴s⁴ ≲ N\*_C(s). With β(s) = β₀ + γ ln s, letting s → ∞ forces **c·δ ≥ 4/γ = 28.71**. This is a quantified target/obstruction for the global-HS instrument under the stated ansatz — it is *not* a claim that (S) is false, and it is not gate-backed (no ensemble input was used).

**[OPINION, given per DECISIONS #009]**
6. I read item 5 as a sharp reason the global trace/HS route cannot close OP-1 at L → ∞ by itself: cδ ≥ 28.7 is far above what first-moment Peierls arguments deliver. This is precisely why M3's windowed + Combes–Thomas-glued architecture is the right shape — there is now a number behind "why windows are forced."
7. With the deterministic comparator side reduced to a theorem with explicit constants, essentially all remaining OP-1 risk concentrates in the stochastic counting lemma (Z.A/Z.B). No deterministic surprise can appear at any scale on this side: the kernel cannot silently degrade.

**Scope honesty:** all of the above concerns the OP-12 deterministic comparator on T⁴ (m₀² > 0, v₀ = 1). CONJ_B, the (S) lemma, and the continuum are untouched.

---

## 6. Files, reproduction, suggested STATE line

Files (this pass): `ENGINE_OP1_m4_tc_closed_form.py` (engine; stages `gates` | `diagonal` | `all`), `CERT_OP1_m4_tc_closed_form.json` (gates + extended table + law + ceiling), this note. Dependencies: numpy, scipy. Reproduce: `python3 ENGINE_OP1_m4_tc_closed_form.py all`. MD5s are listed in the session message and should be recorded in the ledger on deposit.

Suggested STATE.md M4 row (owner to paste):
> M4 (comparator scaling): kernel constants now EXACT closed forms (Theorem 1, NOTE_OP1_m4_tc_closed_form_2026-06-12.md), gated at machine precision against all deposits (36 rows + anchors) plus independent dense and Bessel methods; diagonal extended to s = 64 (L = 256); law T_C·α_W² = (3/32π²)·ln s + B verified (slope to 0.5%); uniform ceiling: Tier-1 finiteness PROVED, Tier-2 sharp T̄_C ≈ 0.117 ⇒ N\*_C ≥ 8 / N\* ≥ 7 for all s (two pins flagged in note §4.2). β-rounding transcription inconsistency found in deposits (≤1.5e−5, no radius affected) — note §2.
