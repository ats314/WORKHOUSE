# CLS / Gauss-law flat-band results note

**Companion to:** ENGINE_FLUX_cls_flat_band_certificate.py (13 gates, all passing).
**Status tier:** delivered (June 11, 2026); candidate §8.6 / §6.15 material for master document v2.5.
**Independence:** built from first principles (oriented plaquette boundaries only); takes no input from ENGINE_FLUX_glueball_band_certificate.py, ENGINE_FLUX_su3_domino_d3.py, or RUN_TROM_d3_results.json. Anchored against the document via §3.15's S(k) and the band edges of §8.1.

## Theorem (Gauss-law structure of the C-odd flat band)

Let H_σ be the signed shared-link adjacency on plaquettes of the cubic lattice (signs s(p,p′) = σ_p(b)σ_{p′}(b), the incidence product on the shared link b), the hopping structure matrix of the C-odd sector (master §8.1; manuscript Theorem 6.3). Then:

**(i) Exact factorization.** In the plaquette-center Bloch gauge, Ñ(k) + 4I = B(k)B(k)† identically in k, where B(k) is the plaquette→link boundary symbol (each plaquette feeds its four boundary links with incidence signs; B is 3×3 over orientations × link directions). Hence Ñ ⪰ −4 as an operator and the flat band at μ ≡ −4 is exactly ker B† — the states carrying **zero net signed amplitude into every link**. The O(y²) flatness theorem (det Ñ + 4I ≡ 0, certified 29/29 in ENGINE_FLUX_glueball_band_certificate.py) is the determinant shadow of this factorization. (Gates G04–G05.)

**(ii) Compact localized state.** The consistently oriented (Levi-Civita) boundary of a single elementary cube — six faces, amplitudes ε_{μνρ}·(±1) on the near/far face pair of each orientation — is an exact real-space eigenvector: H_σ ψ_cube = −4 ψ_cube with **zero leakage** onto any plaquette off the cube. Its Bloch symbol is u(k) = (−sin(k₂/2), −sin(k₀/2), +sin(k₁/2)) (orientation order xy, yz, xz), nonvanishing for k ≠ 0; translates of ψ_cube therefore span the flat band. (Gates G06–G09.)

**(iii) The mechanism is ∂∘∂ = 0.** Every edge of the cube is shared by exactly two faces with opposite induced orientation, so the signed face amplitudes cancel on all 12 edges (gate G10). The flat band is the image of the 3-cell coboundary inside the 2-cochain space: the C-odd one-flux glueball at the band minimum is a **closed-surface (Gauss-law) excitation**, and its immobility is topologically protected at the level of the hopping geometry — a sharper statement than Remark 6.4's ratio argument, and consistent with v2.2's note that "immobility survives via the exact flat band, not the ratio."

**(iv) Robustness, and the sharp O(y⁴) criterion.** Any correction to the effective Hamiltonian whose symbol factors through the link channel, H_corr(k) = B(k)M(k)B(k)† with M(k) an arbitrary Hermitian symbol, annihilates the flat subspace exactly: the band stays flat at μ = −4 + (diagonal constants), at **every order in which the correction is link-mediated** (gate G11). This subsumes O(y²), and explains structurally why the tromino-vanishing lemma (§8.3) preserved flatness at O(y³): with trominoes absent, the third order retains the signed-adjacency (hence link-mediated) form. The flatness question at O(y⁴) (§6.12) therefore reduces to a single criterion:

    flat at O(y⁴)  ⟺  u(k)† H₄(k) P_⊥(k) ≡ 0,    P_⊥ = I − uu†/|u|²,

equivalently: H₄ commutes with the flat projector; equivalently in real space: the fourth-order effective hopping annihilates cube-boundary states up to a constant. Gate G12 certifies that the **minimal corner-sharing (site-mediated) symbol fails the criterion** — so when trominoes activate at O(y⁴), geometry alone will not protect the band. Either the O(y⁴) tromino/tetromino weights conspire to cancel on closed surfaces (which would strongly suggest an exact lattice Gauss-law symmetry of the full effective Hamiltonian and all-orders flatness), or the C-odd glueball acquires its first nonzero bandwidth at fourth order. The criterion above turns the §6.12 computation into a **predeclared, falsifiable gate**: once the O(y⁴) weight cards exist, each hopping geometry class g contributes a computable scalar w_g · [u†T_g P_⊥], and flatness is a finite system of exact rational linear conditions on the weights.

**(v) Partner-band bookkeeping.** tr(Ñ + 4I) = 8(sin²(k₀/2) + sin²(k₁/2) + sin²(k₂/2)) = 8|u(k)|², so the two dispersive eigenvalues sum to 8|u|², reaching the documented top μ = 8 at k = (π,π,π) — re-deriving §8.1's coefficient interval [11/306, 41/306] and the flat band touching at k = 0. (Gate G13.)

## Suggested master-document actions

1. Add this theorem as §8.6 (or fold (i)–(iii) into §8.1) with the certificate in Appendix B; the corrected band edition (§6.11) needs no change — this note explains its constants, it does not alter them.
2. Re-cut §6.12 around criterion (iv): the O(y⁴) frontier now has a binary, pre-registered outcome (weight cancellation ⇒ all-orders Gauss-law protection conjecture; otherwise first bandwidth at O(y⁴), with the bandwidth computable from the same scalars).
3. Optional manuscript remark: the C-even sector has no analogous factorization (S(k) is the unsigned adjacency; its k = 0 eigenvector is the uniform A₁ state, not a closed surface), which is why C-even disperses and C-odd does not — a one-sentence physical explanation of the 5/22 per-bond asymmetry's *qualitative* content.

## Gate ledger

G01 geometry (12 neighbors: 4 + 8) · G02 S(k) anchor vs §3.15 · G03 S spectrum anchors {12,0,0}, −4I · G04 det(Ñ+4I) ≡ 0 re-derived · G05 Ñ+4I = BB† · G06 CLS eigenvalue on support · G07 zero leakage · G08 B†u = 0 and (Ñ+4I)u = 0 · G09 completeness |u|² = Σsin² and rank 2 at generic k · G10 twelve-edge cancellation (∂∂ = 0) · G11 generic link-mediated robustness · G12 corner-sharing sharpness (geometry alone insufficient at O(y⁴)) · G13 trace identity and band top 8. **Total: 13/13.**
