# SU(N) band-shape — completion layer (2026-06-14)

Three Alex-uploaded documents that **complete and consolidate** the fourth-order band-shape theorem
(`../README.md` is the core campaign). Intaken with the machine-checks I could run.

## 1. `THM_SU2_codd_sector_exclusion_theorem_2026-06-14.md` — closes the "SU(2) separate" gap
**The N≥3 domain is MAXIMAL, not a gap.** In pure SU(2), charge conjugation **is a gauge transformation**:
U\* = εUε⁻¹ with ε=iσ₂ (constant gauge g_x=ε ⟹ U_{xy}↦U_{xy}\*). So **C=I** on the physical Hilbert space,
P_{C=−}=(I−C)/2=**0** — there is **no SU(2) T₁⁺⁻ one-flux branch**. A₂,B₂,q₂ are not missing; they are
*undefined* (the C=− sector is empty). Equivalently χ_{1/2}(U)=2a₀ is real; TrX³=0 for traceless Hermitian 2×2.
**Verified this session:** U\*=εUε⁻¹ exactly (max err 0.0e+00 over 2000 random SU(2)); TrX³=0 (≤7e-15). Cert SHA-256 in the doc.

## 2. `THM_SUN_unified_nality_theorem_audited_v2.md` — the consolidated all-N≥3 statement
Unifies balanced + exceptional-rank corrections into one structural theorem:
A_N=A_N^bal (N≥3), B_N=B_N^bal (N≥4), **B₃=B₃^bal − 25/64**, q_N=q_N^bal+Δq_N^exc. Exact exceptional offsets:
Δq₄ = −304746539168/160249753125 (SU4; ΔA₄=ΔB₄=0), Δq₆=6/343 (SU6), SU5 has no determinant sector. Exact
q₃,q₄,q₅,q₆ tabulated; for N≥7 q_N=−(2/3N)Q₃₂(N²)/D₃₄(N²). Global theorem unchanged: A_N>0, B_N>0 ⟹ Γ unique
min, R unique max, Δc₄=A_N+B_N>0 for every N≥3.
**Verified this session:** B₃^bal − B₃^full = **25/64 exactly**; A₃=5/12; positivity (N=7..18 cross-check in `../`).
Subtlety the doc flags: at exceptional ranks q_N^bal means the *direct fixed-rank* balanced contraction, not analytic
continuation of the stable formula (the stable rational rep is singular at N=4 though the finite-rank contraction is finite).

## 3. `NOTE_SUN_su_n_closed_surface_stage1.md` — cleaner structural derivation (2nd order, all N≥3)
Exact shared-link weights give the signed C-odd hopping t_N = 2N(N−2)(N+2)/[(N−1)(N+1)(2N−3)(2N+3)(2N²−1)] > 0
for N≥3 (t₃=5/612, Σ₃=−481/612 recover the certified SU(3) domino constants; t_N~1/(4N³)). The oriented
plaquette-boundary symbol B(k) satisfies BᵀΨ=0, det B=0, N_e Ψ=−4Ψ ⟹ **H₂,N has the momentum-independent
eigenvalue d_N−4t_N: the C-odd closed-surface branch is universally FLAT at 2nd order for every SU(N), N≥3.**
A *conditional* 4th-order reduction recovers D_N=A_N ΣX_i²+B_N Σ_{i<j}X_iX_j given a three-orbit support lemma.
**Verified this session:** t₃=5/612 (sympy). **Stage-2 obligations remain open** (the doc lists 4: generic-N
three-orbit support lemma; exact q_N,c_X,c_M,c_R for enough N; closed forms; all-N positivity).

## Supporting exceptional-rank theorem extracts (provenance)
`THM_SU4_determinant_theorem.md`, `THM_SU4_hybrid_theorem_v2.md`, `THM_SU6_determinant_theorem.md`
— the per-rank determinant-sector results the unified theorem consolidates (their offsets appear above). The SU(4)
ΔA₄=ΔB₄=0 was cold-verified inside the headline band-shape verifier (see `../README.md`).

## Status / grounds
SU(2) exclusion: **T1 + elementary identity machine-checked** (solid). Unified N-ality: T1 (key rationals checked;
positivity cross-checked to N=18). Closed-surface Stage-1: 2nd-order part checked (t₃); **4th-order reduction is
conditional and Stage-2 is open**. None promoted to "established" (T2/T3 pending). Provenance + MD5 in `MAN_SUN_md5sums.txt`.
