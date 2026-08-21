# SU(4) Fourth-Order Band Bundle: Independent Re-Verification (19/19) and Integration with the Staircase Theorem

2026-08-01. Inputs: `THM_SU4_hybrid_theorem_v2.md` + `CERT_SU4_hybrid_certificate_v2.json` (two copies each, byte-identical — deduped) + `CERT_SU4_exceptional_topology_word_ledger_v2.json` (96 topology records, 76 word corrections), version `2026-06-14-su4-hybrid-complete-v2`. Also `SOURCEOFGOD.txt` — identified as a **saved transcript of this conversation**, not the canonical symbolic source; its SHA-256 (bf6373…) does not match the certificate's `canonical_symbolic_source_sha256` (8feec874…). Consequence: the bundle's external provenance chain (canonical source, persistent archive zip) references files not present in the corpus and remains *asserted*; everything internally checkable was re-verified here independently.

## Independent verification: 19/19 PASS

Exact rationals (Fractions) and a 61³ Brillouin-zone scan:
1. **Correction additivity**: full = balanced + Δq for each of q, X, M, R with the single exact shift Δq = −304746539168/160249753125; ΔA = ΔB = 0 confirmed on the quoted rationals.
2. **Parity identities on the full numbers**: c_X = q₄+A₄, c_M = q₄+A₄+½B₄, c_R = q₄+A₄+B₄, and c_R − 2c_M + c_X = 0 — all exact.
3. **Bandwidth** = A₄+B₄ = 2314426811641505637629/23493898906786498781250 in both balanced and full blocks; decimals consistent to 10⁻¹²⁺; A₄ = 32/675 closed form confirmed; positivity confirmed.
4. **Dispersion theorem**: the formula c₄,₄(k) = q₄ + [A₄ΣXᵢ² + B₄ΣXᵢXⱼ]/(2ΣXᵢ) reproduces the X/M/R symmetry-point values exactly (they are consequences of the formula, and the certificate's numbers satisfy them); on the scan the global maximum equals A₄+B₄ and is attained **only** at R, and the minimum extends continuously to 0 at Γ with positivity elsewhere — the strict-dispersion claim holds as stated.
5. **Ledger cross-counts**: 96 exceptional trace topologies and 76 exceptional-bearing words in the ledger match the certificate corpus block.

The bundle's own correction note (downgrading ΔH = Δq·𝟙 to the flat-branch eigenvalue identity H^exc ψ(k) = Δq ψ(k), with ψ(k) = (e^{ik₂}−1, −(e^{ik₁}−1), e^{ik₀}−1)) is the house discipline working as intended; the eigenvalue identity itself is not re-derivable here without H^exc, but its downstream consequences (q₄ shift, A₄/B₄ invariance) are the items verified above.

## Integration: the lock and the dispersion are not in tension — they factorize the N-dependence

Today's staircase theorem says SU(3) and SU(4) are **exactly cubic-locked at the source-operator level**: ImTr U = −(P₃/6) × (strictly positive alcove form factor) for both, identical sign and nodal structure. This June bundle says the **dynamics differ**: the SU(4) fourth-order one-flux T₁⁺⁻ band is strictly dispersive (bandwidth ≈ 0.0985) while the SU(3) C-odd band is exactly flat through y³. Read together, the N-dependence at this level lives **entirely in the Hamiltonian's word algebra, not in the C-odd source**: the SU(4) exceptional sector — ε₄/determinant channels (final Haar families (4,0), (0,4), (5,1), (1,5); determinant singlets entering only at the third des-Cloizeaux cut; 76 words, 156 C-orbits) — has no SU(3) counterpart in this role, and its entire effect on the flat branch is the momentum-independent shift Δq₄, with the dispersion (A₄, B₄) coming from the balanced sector.

**The ordering caveat that creates the next target.** SU(3) flatness is certified through y³; c₄,₄ is a *fourth-order* statement. The like-for-like comparison — SU(3)'s y⁴ band coefficient c₄,₃(k) — is not in the corpus. Two scenarios: (i) SU(3) also disperses at y⁴, and flatness was a low-order accident; (ii) SU(3) stays flat at y⁴, making flatness an **N = 3-exceptional phenomenon** with a named mechanism candidate already certified in this program: the quartic Weyl barcode ‖P₄ − Π_rad P₄‖² = (N²−1)(N²−4)(N²−9)/[4(N²+1)] **vanishes identically at N = 3 and opens at N = 4** — the same (N²−9) zero that appears in the odd Gram determinant. **Barcode–flatness conjecture (open, decidable):** the SU(3) fourth-order one-flux T₁⁺⁻ band is flat iff the quartic angular channel is closed, i.e., c₄,₃(k) is k-independent. This is computable with the existing SU(3) word-calculus engine and is the single highest-value follow-up this bundle creates.

## Ledger placement

- SU(4) fourth-order band theorem: **EXACT (machine-verified rationals; +19 independent re-verification gates on top of the bundle's 12)**, with the same scope condition as the SU(3) band program (infinite-volume linked-cluster / Assumption-6.5 analog — the certificate does not state it; the manuscript should).
- `SOURCEOFGOD.txt`: archive-only (conversation log); keep out of the citable source set; the true canonical symbolic source (SHA 8feec874…) should be added to the project corpus if provenance is to be independently closable.
- Cross-links to record: staircase lock (operator level) ↔ exceptional-sector dispersion (dynamics level); barcode (N²−9) ↔ flatness conjecture; SU(4) determinant families ↔ the N-ality structures the rank-two Bergman note flagged as the C-conjugation strips' algebraic relatives.
