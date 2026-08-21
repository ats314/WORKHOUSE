# CLS / Gauss-law flat-band results note — v1.1

**Companion to:** `ENGINE_FLUX_cls_flat_band_certificate_v1_1.py` (14 gates, all passing; cold run June 13, 2026, ~4 s).
**Status tier:** T1 (machine-gated). Candidate §8.6 / §6.15 material for the master document; backs the standalone paper's Gauss-law / flat-band / CLS / robustness theorems.
**Independence:** built from first principles (oriented plaquette boundaries only); takes no input from `ENGINE_FLUX_glueball_band_certificate.py`, `ENGINE_FLUX_su3_domino_d3.py`, or `RUN_TROM_d3_results.json`. Anchored against the document via §3.15's S(k) and the band edges of §8.1.

**Provenance (honest).** The original v1.1 was authored in a session whose artifacts were not saved and survives in **no store** (THEORY finding F015; re-upload June 13 returned only v1.0, md5 `d5396786…`). This edition is an **agent reconstruction** (THEORY, June 13, 2026) built from the surviving v1.0 (13/13) plus the master-document v2.6 changelog specification of the two audit fixes. The mathematics is v1.0's except for the two fixes and one added completeness gate; it is not claimed byte-identical to the lost original.

## What changed from v1.0 (13 gates) to v1.1 (14 gates)

1. **G10 — edge count now gated.** v1.0 wrote `len(edge_sum)==12 and all(...) or all(...)`, which Python parses as `(A and B) or C`; the "exactly 12 edges" clause was bypassed. v1.1 gates the count properly: there are exactly 12 cube edges **and** the signed face amplitudes cancel on each.
2. **G09 — k=0 span overclaim removed; new G09b.** v1.0's phrase "cube states span the flat band" is false at k=0 (there u(0)=0; the flat subspace is the three rest states, Ñ(0)=−4I). v1.1's G09 claims only the generic-k statement it proves (the cube symbol spans the 1-dim kernel for k≠0, rank 2), and a new **G09b** certifies exact completeness on the torus.
3. **G11 — wording sharpened** (all-orders / link-mediated scope made explicit). Gate logic unchanged.

## Theorem (Gauss-law structure of the C-odd flat band)

Let H_σ be the signed shared-link adjacency on plaquettes of the cubic lattice (signs s(p,p′) = σ_p(b)σ_{p′}(b), the incidence product on the shared link b). Then:

**(i) Exact factorization.** In the plaquette-center Bloch gauge, Ñ(k) + 4I = B(k)B(k)† identically in k, where B(k) is the plaquette→link boundary symbol. Hence Ñ ⪰ −4 and the flat band at μ ≡ −4 is exactly ker B† — states carrying **zero net signed amplitude into every link**. The O(y²) flatness (det(Ñ+4I) ≡ 0) is the determinant shadow of this factorization. (Gates G04–G05.)

**(ii) Compact localized state.** The consistently oriented (Levi-Civita) boundary of one elementary cube — six faces, amplitudes ε·(±1) — is an exact real-space eigenvector: H_σ ψ_cube = −4 ψ_cube with **zero leakage** off the cube. Its Bloch symbol u(k) = (−sin k₂/2, −sin k₀/2, +sin k₁/2) is nonvanishing for k ≠ 0; translates of ψ_cube span the flat band away from k=0. (Gates G06–G09.)

**(iii) Exact completeness on the torus (v1.1, gate G09b).** The torus Hamiltonian block-diagonalizes (discrete Bloch transform) into its L³ momentum blocks Ñ(k)+4I, so the flat-band dimension is Σ_k nullity(Ñ(k)+4I). At **L=3** this is computed exactly:

    dim ker(Ñ + 4I) = L³ + 2 = 29  =  26  ⊕  3,

with **26** from the 26 nonzero Bloch momenta (one cube state each; equivalently the L³ = 27 real-space cube states modulo the single global relation Σ_cubes ψ = 0, i.e. rank L³−1 = 26) and **3** rest states at k=0, where Ñ(0) = −4I. This corrects the v1.0 k=0 overclaim and supplies exactly the L³+2 decomposition cited by the standalone paper's CLS theorem.

**(iv) The mechanism is ∂∘∂ = 0.** Every edge of the cube is shared by exactly two faces with opposite induced orientation, so the signed face amplitudes cancel on all 12 edges (gate G10). The C-odd one-flux glueball at the band minimum is a **closed-surface (Gauss-law) excitation**; its immobility is topological at the level of the hopping geometry.

**(v) Robustness and the sharp O(y⁴) criterion.** Any correction whose symbol factors through the link channel, H_corr(k) = B(k)M(k)B(k)† with M Hermitian, annihilates the flat subspace exactly: the band stays flat at μ = −4 + (diagonal constants) at **every link-mediated order** (gate G11). This subsumes O(y²) and explains why tromino-vanishing preserved flatness at O(y³). The O(y⁴) question reduces to

    flat at O(y⁴)  ⟺  u(k)† H₄(k) P_⊥(k) ≡ 0,    P_⊥ = I − uu†/|u|²,

and gate G12 certifies that the **minimal corner-sharing (site-mediated) symbol fails** it — so once trominoes activate at O(y⁴), geometry alone will not protect the band. Either the O(y⁴) weights cancel on closed surfaces (suggesting an exact lattice Gauss-law symmetry and all-orders flatness) or the C-odd glueball acquires its first nonzero bandwidth at fourth order, computable from the same scalars.

**(vi) Partner-band bookkeeping.** tr(Ñ + 4I) = 8(sin²k₀/2 + sin²k₁/2 + sin²k₂/2) = 8|u(k)|², so the two dispersive eigenvalues sum to 8|u|², reaching the documented top μ = 8 at k = (π,π,π) — re-deriving the coefficient interval [11/306, 41/306] and the flat band touching at k = 0. (Gate G13.)

## C-even factorization correction (note-level)

Both charge sectors are link-mediated and factor structurally, but they are **not symmetric**: the C-odd signed incidence B has det B ≡ 0 (a whole flat band, kernel everywhere), whereas the C-even **unsigned** incidence N has det N = −2 v₁v₂v₃ with v_j = 1+e^{ik_j}, vanishing only on the zone faces k_j = π. Hence the C-even kernel is measure-zero (it disperses) while the C-odd kernel is a full band. The earlier loose phrasing that "both sectors factorize identically" is corrected here: the *form* B M B† is shared, but only the signed (C-odd) symbol is rank-deficient at generic k. This is the structural origin of the dispersing/non-dispersing asymmetry behind the per-bond ratio 5/22.

## Novelty split (what is new vs re-derived)

- **Re-derived** (already in `glueball_band_certificate(_v2)`): the existence of the flat band itself (det(Ñ+4I) ≡ 0; band edges [11/306, 41/306]).
- **New in this certificate**: the operator factorization Ñ+4I = BB† (the "lattice Gauss law" reading), the explicit cube CLS with zero leakage, the **exact L³+2 torus completeness** (G09b), the **all-orders robustness theorem** (any B M B† leaves the band flat), and the **pre-registered, falsifiable O(y⁴) criterion** with its corner-sharing sharpness witness (G12).

## Gate ledger (14/14)

G01 geometry (12 neighbors: 4+8) · G02 S(k) anchor vs §3.15 · G03 S-spectrum anchors {12,0,0}, −4I · G04 det(Ñ+4I) ≡ 0 · G05 Ñ+4I = BB† · G06 CLS eigenvalue on support · G07 zero leakage · G08 B†u = 0 and (Ñ+4I)u = 0 · G09 generic-k span (|u|² = Σsin², rank 2 at k≠0) · **G09b exact torus completeness L³+2 = 29 = 26+3 at L=3 (NEW)** · G10 twelve-edge cancellation, count gated (∂∂=0) · G11 all-orders link-mediated robustness · G12 corner-sharing sharpness · G13 trace identity and band top μ=8. **Total: 14/14.**
