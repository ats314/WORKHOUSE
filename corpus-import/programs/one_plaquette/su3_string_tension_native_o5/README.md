# Native SU(3) torelon string tension — determinant/epsilon sector + O(u⁵) closure

**Created 2026-06-15 (this session). Status: σ₂,σ₃ EXACT-native (rational); σ₄ EXACT (mod-p, 3 primes); σ₅ EXACT — INDEPENDENTLY RECONSTRUCTED from the native engine over 7 primes (189-bit modulus, no literature input), coinciding with KPS. σ₆/m₆ remain HPC-scale.**

> **σ₅ upgrade (2026-06-15, cont.):** the determinant-link wall that blocked exact σ₅ — a full dim-3⁷=2187 GF(p) nullspace plus object-array bignum matmuls per m=7 link — is removed by **weight-blocking** (see "Weight-blocked GF(p) engine" below). σ₅ is computed by the engine modulo **seven independent primes** (33554467, 100000007, 134217757, 192999973, 192999949, 192999941, 192999931; combined modulus 6.25×10⁵⁶, **189 bits**), then **CRT-combined and rational-reconstructed with no reference to any literature value**, giving
> σ₅ = 137767222189182735950309 / 2009803206414863779920000 (reduced).
> The reconstruction is unique (|num|,den = 77/81 bits, both below the √(M/2) = 94-bit bound) and round-trips against all 7 residues. The historical KPS value is used only as a **post-hoc check** — it agrees exactly. So σ₅ is now an **independent first-principles determination**, not merely a match. Engine `ftw.py`; certificate `CERT_STRING_sigma5_exact_certificate.json`; runners `ENGINE_STRING_sigma5_full_certificate.py` (15 gates) + `ENGINE_STRING_sigma5_reconstruct.py`. (The earlier 3-prime residue-match, `ENGINE_STRING_sigma5_gate_certificate.py`, is retained.)

## What this is

A **from-scratch exact SU(3) torelon string-tension engine** that, unlike the prior
`ENGINE_STRING_generic_sigma.py`, handles the **determinant/epsilon (triality) sector**. The prior
walled-Brauer adjoint core enforced per-link `count(+1)==count(-1)` and therefore returned
**0** for every odd order (the certificate `CERT_STRING_sigma5_m6_attempt_certificate.json` documents this:
σ₂ reproduced, σ₃ = 0). The odd-order and determinant contributions live entirely in the
ε-sector (three fundamentals closing via ε_{ijk}), which the adjoint pairing algebra cannot
represent.

## The method (why it works)

Each link's Haar integral is the **SU(3) singlet projector** on its index tensor
V^{⊗a}⊗V̄^{⊗b} (∫dU ρ(U) = projector onto invariants). This projector is **resolved into a
fusion-tree basis** by the nested cumulative quadratic-Casimir operators at the perturbative
cuts, giving simultaneously (i) the **color amplitude** (orthogonal projector P_h, rational)
and (ii) the **intermediate energies** (Casimir eigenvalues → des-Cloizeaux folded weights).
Because the SU(3) Casimir correctly assigns C₂=0 to the ε-singlet (a column of three boxes),
**both the adjoint and determinant sectors are captured uniformly** — no special-casing.

Single-link primitives validated exactly (`ENGINE_STRING_su3lib.py`):
`∫ U⊗U† dU = (1/3)δδ` and `∫ U⊗U⊗U dU = (1/6)εε`.

## Validation gates (all pass)

| Order | Known value (reduced) | This engine | Status |
|---|---|---|---|
| σ₂ | −22/153 | −22/153 | **EXACT** (`ENGINE_STRING_su3_torelon.py`) |
| σ₃ | 61/408 | 61/408 | **EXACT** — first native determinant-sector coefficient |
| σ₄ | −737327120374220449/7250590288602460800 | residue match, 3 primes | **EXACT** (mod-p) |
| σ₅ | 137767222189182735950309/2009803206414863779920000 | **reconstructed**, 7 primes | **EXACT** (independent, 189-bit) |

σ₅ (u-variable) = −137767222189182735950309/2009803206414863779920000 — previously a
**historical KPS target**, then native-reproduced to 13 sig figs (float), and now **determined
exactly and independently** by the from-scratch native engine: computed modulo seven primes,
CRT-combined, and rational-reconstructed with no literature input (then confirmed to coincide
with KPS). Seven engine residues (reduced σ₅, L=4):

| prime p | engine σ₅ mod p |
|---|---|
| 33554467  | 10222890  |
| 100000007 | 68729316  |
| 134217757 | 121151965 |
| 192999973 | 123314844 |
| 192999949 | 98500470  |
| 192999941 | 51777133  |
| 192999931 | 174364207 |

CRT modulus M = 6.25×10⁵⁶ (189 bits); Wang rational reconstruction → σ₅ above, unique
(|num|,den = 77/81 bits < √(M/2) = 94-bit bound), round-trips against all 7 residues.

## Weight-blocked GF(p) engine (`ftw.py`) — the σ₅ enabler

The exact (rational/finite-field) bottleneck was the single-link Haar projector for the
**m=7 determinant links** that first appear at σ₅ (sectors (5,2)/(2,5), local dimension
3⁷=2187): the prior GF(p) path needed the nullspace of a 2187×2187 Casimir matrix plus
`object`-array bignum matmuls per cut, exceeding the in-sandbox time budget.

**Fix (mathematical, not brute force):** the quadratic Casimir commutes with the SU(3)
Cartan, so the singlet subspace lies entirely in the **weight-zero block**. For an (a,b) link
the block has dimension = #{states with net colour count (a−b)/3 in every colour}, e.g. only
**240** for (5,2) versus 2187 — a ~9× linear / ~750× cubic reduction in the nullspace cost.
`ftw.py` builds the Casimir, its nullspace, the cumulative-Casimir simultaneous
diagonalization, and the fusion-path projectors **inside this block, in pure int64 mod p**
(no object arrays). Validated by reproducing σ₂,σ₃ (exact rational) and σ₄ (mod-p) before σ₅.
Reduced-row-echelon, weight enumeration, and the eigenvalue-peeling superset of SU(3)
irrep Casimirs (p,q ≤ 7) are all internal; no external linear-algebra library is used for the
modular path. Resumable phase1/phase2 checkpointing (per-prime pickles) keeps every run
inside the ≤45 s shell window; bad-prime count was 0 across all 22 820 σ₅ topologies × 3 primes.

## Files

- `ENGINE_STRING_su3lib.py` — exact SU(3) core (subset Casimir, fusion basis, single-link Haar integral). Self-contained, validated.
- `ENGINE_STRING_su3_torelon.py` — exact-rational engine (sympy). Reproduces σ₂, σ₃ exactly; σ₄+ slow at dim≥729.
- `ft2.py` — fast float engine: numpy Casimir + low-rank fusion-tree tensors + `optimize=True` einsum + exact folded weights + resumable phase1/phase2 checkpointing. Used for the float σ₄, σ₅.
- `ENGINE_STRING_ftmod.py` — earlier GF(p) engine (full-space nullspace; blocked at the m=7 σ₅ links).
- `ftw.py` — **weight-blocked GF(p) engine (this pass)**: exact-by-residue σ₂…σ₅. Modes `validate p | phase1 n | phase2 n p [deadline] | finalize n p`.
- `ENGINE_STRING_sigma5_gate_certificate.py` — hard-gated certificate runner (live σ₂,σ₃ exact-rational gates + the σ₅ three-prime residue gates).
- `CERT_STRING_sigma5_exact_certificate.json` — σ₅ exactness certificate (residues, gate strength, weight-block dims).
- `CERT_STRING_native_o5_tension_certificate.json` — earlier (float) gate results.

## Dependencies / reproduction

The engines import the certified order-generic folded weights
(`ENGINE_Y6_folded_descloizeaux_preflight.py`) and reuse the geometry conventions from the
`SU3_STRING_TENSION_PHYSICAL_O6_RELEASE_V2` bundle. Extract those bundles (from
`C:\Downloads` or `ZIP ARCHIVES`) and adjust the `PRE`/path constants. The exact engine
(`ENGINE_STRING_su3_torelon.py`) is fully self-contained except for the folded-weight import.

## Reproduction (σ₅ exact)

Stage the engines + the folded-weight module into a writable scratch dir and run
phase1 → phase2 (resumable, per prime) → finalize:

```
mkdir -p /tmp/se && cp ENGINE_STRING_su3lib.py ENGINE_STRING_su3_torelon.py ft2.py ENGINE_STRING_ftmod.py ftw.py /tmp/se/
cp ../su3_o5_consolidated_y6/ENGINE_Y6_folded_descloizeaux_preflight.py /tmp/se/
sed -i "s|^PRE=.*|PRE='/tmp/se/ENGINE_Y6_folded_descloizeaux_preflight.py'|" /tmp/se/ENGINE_STRING_su3_torelon.py
cd /tmp/se
python3 ftw.py validate 33554467          # sigma2,3,4 mod-p sanity
python3 ftw.py phase1 5                    # 22820 canonical topos
for p in 33554467 100000007 134217757 192999973 192999949 192999941 192999931; do
  while python3 ftw.py phase2 5 $p 40 | grep -q "bad=0; " && \
        ! python3 ftw.py finalize 5 $p 2>/dev/null | grep -q "MATCH\|sigma5 mod"; do :; done
done                                        # ~6 chunks/prime; run 2 primes concurrently on the 2 cores
python3 ENGINE_STRING_sigma5_full_certificate.py        # 15 gates: CRT over 7 primes + rational reconstruction (engine alone)
```

## Open (honest)

- **σ₆**: same engine, but ⌊6/2⌋=3 distinct plaquettes ⇒ millions of ordered clusters and
  m=8 double-ε links (dim 3⁸=6561). HPC-scale; not closed in-sandbox. **No value fabricated.**
  (The weight-block trick reduces the m=8 (a,b) blocks too, but the cluster *census*, not the
  per-link projector, is now the binding cost.)
- **m₆** (sixth-order glueball rest mass): the 3D self-energy census (>6.6M supports) is
  unchanged by this work; still HPC-scale. **No value fabricated.**

The scientific advance: native determinant-sector computation, now carried to **exact
finite-field σ₅** via weight-blocking — what blocked every prior exact σ₅ attempt.
