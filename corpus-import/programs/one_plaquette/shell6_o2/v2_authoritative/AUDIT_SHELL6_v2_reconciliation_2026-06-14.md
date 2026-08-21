# Shell-6 C-odd O(y²) — V2 reconciliation & adjudication (2026-06-14)

**Verdict: the V2 symmetry-reduced full-intermediate computation is AUTHORITATIVE.**
THEORY's prior orbit-0 exact coefficients (from `../NOTE_SHELL6_o2_result_2026-06-13.md`, already
self-downgraded to "strongly evidenced") are **superseded** by V2. The qualitative ordering is
unchanged. Grounds: T1 machine-gated (cold-reproduced) **plus an independent exact diagonalization
I performed**, against THEORY's un-converged single-layer (only 3 entries ever hand-checked).

## What was in conflict

THEORY's June-13 note computed the orbit-0 sector from a **single-layer** effective Hamiltonian whose
off-diagonal outer-W-independence was never fully verified (3 entries spot-checked → over-labelled
"certified", then downgraded to "strongly evidenced" in its UPDATE 4). V2 is the **full-intermediate**
computation (retains octet/sextet/ε intermediates), reduces the 44 states to O_h orbits 12+24+8,
computes 3 exact columns and symmetry-reconstructs the rest under stabilizer/Hermiticity/O_h/C gates.

The two disagree by a clean **±1/6** in the orbit-0 sector only.

| channel (×1/959310) | THEORY note (superseded) | **V2 (authoritative)** |
|---|---|---|
| 0⁻⁻ (A₁⁻⁻) | −12075379 | **−12235264** |
| 2⁻⁻ (E⁻⁻) | −13034689 | **−13194574** |
| 2⁻⁻ (T₂⁻⁻) | −12714919 | **−12555034** |
| 3⁺⁻ (A₂⁺⁻) | −21281/1530 | −21281/1530 (agree) |
| E − 0⁻⁻ | −1 | **−1** (agree) |
| T₂ − 0⁻⁻ | **−2/3** | **−1/3** |
| E − T₂ split | **1/3** | **2/3** |
| E(3⁺⁻) − E(0⁻⁻) | −1267808/959310 ≈ −1.322 | **−1107923/959310 ≈ −1.155** |

## How it was adjudicated this session

1. **V2 cold-reproduced** (`bash ENGINE_STRING_reproduce.sh`, clean sandbox, no cache): every substantive gate passes —
   word-closure, shell-4/shell-6 Hermitian cross-check, cross-entries ∈ {−1/3,−2/3}, coupling strengths
   g²₋=4/9, g²₀=8/9, g²₊=4/9 (total 16/9), unfolded m₂=419/306; and the exact-rational `CERT_SHELL6_o2_matrix_v2.json`
   + `CERT_SHELL6_o2_representatives_v2.json` reproduce **byte-identical**. The only FAIL is the `analysis` JSON's
   byte-hash, which is float-format-fragile across environments (the exact outputs are byte-identical) — a
   known nit, not a math discrepancy.
2. **Independent exact diagonalization (mine, not V2's analysis script).** I loaded the byte-identical
   44×44 rational `H2_connected` matrix and computed its exact eigenvalues with multiplicity in sympy.
   The spectrum reproduces V2's channel certificate exactly:
   0⁻⁻ = −6117632/479655 = **−12235264/959310** (mult 1);
   2⁻⁻(E) = −6597287/479655 = **−13194574/959310** (mult 2);
   2⁻⁻(T₂) = −6277517/479655 = **−12555034/959310** (mult 3);
   3⁺⁻ = −21281/1530 (mult 1). And the differences: **E−0⁻⁻ = −1, T₂−0⁻⁻ = −1/3, E−T₂ = −2/3**,
   **E(3⁺⁻)−E(0⁻⁻) = −1107923/959310**. This is independent of both V2's own scripts and THEORY's note.
3. **THEORY's own `ENGINE_SHELL6_certify.py` corroborates by construction.** It computes the converged full-row
   energies and gates them against its `PUBLISHED` dict (THEORY's now-superseded values). Run to completion
   it would therefore **fail** its final `== published` gate (the converged row yields V2's −12235264, not
   −12075379) — i.e. it refutes the values it was written to certify. (Partial cold run here: the orbit-0
   resolvent gate passes; |Winner|=36 ≪ |Wouter|=156, confirming outer-W matters — the exact mechanism by
   which the single layer under-counts. The full row is the documented ~179K-integral slow path; resumable
   but not needed given the independent diagonalization above.)

## What stands vs. what changed

- **Stands (both agree):** qualitative ordering **3⁺⁻ < 2⁻⁻(E) < 2⁻⁻(T₂) < 0⁻⁻** (lightest→heaviest;
  0⁻⁻ heaviest, answers GPT's question); the structurally-exact 3⁺⁻ orbit-1 diagonal −21281/1530; E−0⁻⁻ = −1.
- **Changed (V2 supersedes THEORY):** every orbit-0 absolute coefficient (by ±1/6); T₂−0⁻⁻ is **−1/3** not −2/3;
  the E–T₂ split is **2/3** not 1/3; E(3⁺⁻)−E(0⁻⁻) = **−1107923/959310** not −1267808/959310.

## Consequences / action
- `../NOTE_SHELL6_o2_result_2026-06-13.md` carries a correction header pointing here; its orbit-0 exact rationals
  and "1/3 split" are superseded (qualitative ordering retained).
- `../ENGINE_SHELL6_certify.py` `PUBLISHED` dict holds the superseded values — left as-is with this note recording
  that it now functions as a *refuter* of those values; updating it to V2's numbers (forward-certifier) is a
  one-line change flagged for Alex.
- STATE.md updated. **Flagged for Alex:** this is a status-bearing numeric correction (Alex owns status).

Source: `C:\ALL THEORY\ZIP ARCHIVES\SHELL6_O2_SYMMETRY_REDUCED_V2_COMPLETE_RELEASE.zip`, md5
`382788034bca6c54322bf451322cf546`. Files distilled into this directory; per-file MD5 in `MAN_SUN_md5sums.txt`.
