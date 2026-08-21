# SU(3) O(y⁴) C-odd flat-band — independent verification

**Date:** 2026-06-13 · **Verdict: LIFT** (the band is flat through O(y³) and acquires nonzero dispersion at O(y⁴)).

This folder records an *independent* re-derivation (no reuse of the production engine) of the
fourth-order flat-band-breaking result. Run `python3 ENGINE_Y4_independent_verification.py DATA_Y4_full_real_space_h4_kernel.json.gz`.

## What was checked, and the result

| Gate | Check (independent) | Result |
|---|---|---|
| G1 | 3G Haar contraction reproduces all **2,798** Stage-3F `bare_amplitude` values | **PASS — exact** |
| G2 | des-Cloizeaux **folded** identity `H₄=PVRVRVRVP−a(PVR²VRVP+PVRVR²VP)+a²PVR³VP−½{PVRVP,PVR²VP}` vs brute-force 4th-order PT on 5 random Hamiltonians | **PASS — exact** |
| G3 | archived 189-entry H₄ kernel is exactly Hermitian, `T(r;a→b)=T(−r;b→a)` | **PASS** |
| G4 | parity-momentum corrections match the published theorem; dispersion witness ≠ 0 | **PASS — LIFT** |
| G5 | real-space `H₄·ψ_cube` leaks: 36-plaquette image, 30-plaquette residual, max `5/48` on 6 plaquettes | **PASS — LIFT** |

Kernel SHA-256 `635d40fa…afb2900` (matches the stage-3j verdict certificate).

## Decisive numbers (exact rationals, reproduced here)

- c4(π,0,0)   = −17700498622147435111 / 7250590288602460800
- c4(π,π,0)   = −4367164159624988707 / 1812647572150615200
- c4(π,π,π)   = −3447362930970494909 / 1450118057720492160
- **Dispersion witness** c4(π,π,π) − c4(π,0,0) = **17607806155349 / 275331901291200 ≈ 0.063951 > 0**
- Real-space rigid cube eigenvalue c₄ = −4555981615057344457 / 1812647572150615200; residual max leakage = **5/48**.

Because the branch is exactly flat through O(y³), a nonzero value at two momenta proves the first nonzero bandwidth is O(y⁴). The witness is **convention-independent** (parity momenta ⇒ real phases), so the LIFT verdict does not depend on any normalization choice.

## On Wp, Wc and the proposed closed form

Defining the geometry weights from the high-symmetry momenta via `alpha = 12Wp − 4(Wp−Wc)·e₂/e₁`:

- **Wp = −17700498622147435111 / 87007083463229529600**
- **Wc = −34705471293352429373 / 174014166926459059200**
- **Wp − Wc = −17607806155349 / 4405310420659200 ≈ −0.0039970 ≠ 0  ⇒ LIFT**

**Caveat (important).** The two-parameter closed form `alpha(k)=12Wp−4(Wp−Wc)e₂/e₁` is **exact only on the
parity sublattice**, not at generic k. From the verified kernel, c4(π/2,0,0) and c4(π,0,0) both have
e₂/e₁ = 0 yet differ — the closed form misses them by exactly **5/24** at (π/2,0,0). The true O(y⁴)
correction c4(k) is a richer cubic-covariant lattice function; a numeric BZ scan gives a true bandwidth
≈ 0.48 (max at (π,π,π); minimum near Γ, where the flat eigenvector degenerates). Hence:

- the exact **bandwidth lower bound** is the parity witness `17607806155349/275331901291200 ≈ 0.0639512`;
- the careful theorem (`THEOREM_…md`) correctly claims only `W₄ ≥` this witness and explicitly does **not**
  claim a closed-form bandwidth — consistent with this finding. The `Wp/Wc` 2-parameter description is a
  high-symmetry projection, **not** a global parameterization of the band.

## The resonant-sector question (resolved)

61% of orbits (10,237 of 16,835) are model-space *resonant*; Stage-1 stores their resolvents as `null`
(`requires_folded_terms`). This is **not** missing data: those contributions are fixed by the des-Cloizeaux
folding (the `−a(E_L+E_R)+a²F−½{B,D₂}` subtraction with `a=PVP` scalar and the *non-resonant* resolvent
`R=Q(E₀−H₀)⁻¹Q`). G2 above validates that identity against brute-force perturbation theory. So all 16,835
orbits are computable — there is **no** orbit class that cannot be evaluated. (An earlier intermediate
script that declared the folded terms "absent data" was mistaken.)

## Scope / honesty boundary

Verified: engine calibration (G1), the folding identity (G2), and that the *archived* kernel is Hermitian
and reproduces the theorem's exact momentum-space and real-space certificates (G3–G5). Not done here: a
full from-primary-data regeneration of the 189-entry kernel (that requires the read-protected production
engine and possibly regenerated stage inputs). No continuum / all-orders / mass-gap claim is made or implied.

## Addendum — representation-theory foundation independently confirmed (2026-06-13)

The SU(3) fusion/singlet dictionary (the `d3` vertex generator that underlies the Haar
engine) was re-verified with a **second, independent algorithm**: exact Schur-polynomial
bialternants `s_λ = a_{λ+δ}/V` with leading-term peeling, vs the notebook's Littlewood–
Richardson skew-tableau engine. See `ENGINE_Y4_rep_check.py`.

- all **100** pairwise SU(3) tensor products agree;
- all **10** six-factor singlet anchors agree (incl. multiplicities 798, 145, 124, 12, 7).

Two distinct algorithms ⇒ the rep-theory layer beneath the Haar engine is not a single-
implementation artifact. (`endgame (1)` notebook = this verification reproduced on Colab.)
