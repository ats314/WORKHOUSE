# Fourth-order corner operator — build status

Session of 2026-08-08. All gates re-runnable from the accompanying scripts.

## Stage 1 — geometric substrate (`substrate.py`) — COMPLETE, 8/8 gates

Cellular complex rebuilt from the definitions in the flatband paper (rev.
2026-07-25), with the paper's quoted results used only as gates.

| gate | statement | result |
|---|---|---|
| G1 | ∂₂∂₃ = 0 | exact, 0.00e+00 |
| G2 | cellular Bloch ∂₂ = Eq. (4) entrywise | exact |
| G3 | S(k) + 4I = Ñ Ñ† (Lemma 3.1) | 2e−16 |
| G4 | Ñ†Ñ = qI − uu† (Eq. 8) | 3e−15 |
| G5 | spec S(k) = {−4, −4+q, −4+q} (Thm 4.1) | 5e−15 |
| G6 | flat vector = (ū₃, −ū₂, ū₁) ∈ ker Ñ† | 3e−16 |
| G7 | flat eigenspace = L³+2 at L = 3,4,5 | 29, 66, 127 |
| G8 | first level above = 4sin²(π/L) | exact |

**Convention hazard.** Eq. (4) is the e^{+ik·x} convention; e^{−ik·x} returns
the complex conjugate matrix. Same spectrum, so no second-order check catches
it, but it flips signs at fourth order. MASTER_THEORY's ψ(k) is written in the
*opposite* convention and sits in ker Ñᵀ (verified, 3e−16). Hop operators must
carry e^{−ik·x} to be consistent with Eq. (4) for Ñ. This bit three times
during the build.

## Stage 2 — four-point extraction (`extraction.py`) — COMPLETE

Re-derived from scratch (basis table recomputed, 4×4 system solved). Gated by
reproducing the exact SU(3) and SU(4) shape vectors from α and β alone.

    A = ΔX/4
    B = (ΔX + 4ΔM − 6ΔP)/16
    C = 3(2ΔP − ΔM − ΔX)/8
    D = 3(ΔR − 6ΔM + 6ΔP)/16

**Two of these are wrong in the canonical source.** That file is a .docx whose
formatting is lost as plain text; a leading coefficient outside a parenthesis
fuses with the first term inside. It reads C = (32ΔP − ΔM − ΔX)/8 and
D = (3ΔR − 6ΔM + 6ΔP)/16. Taken literally: 32ΔP where it should be 6ΔP, and
−6ΔM where it should be −18ΔM.

**The "independent all-zone checkpoint" is not independent.** 6ΔP − 4ΔM − ΔX = 0
is precisely the statement B = 0, and ΔR − 2ΔM + ΔX = 0 follows too. Both hold
identically under the pencil form, so neither can validate a computation. The
four checkpoints *determine* (A,B,C,D) but cannot *check* them — a fifth
momentum is needed for any genuine test at SU(5)/SU(6).

## Stage 2b — two-hop orbits (`orbits.py`, `project_orbits.py`) — COMPLETE

144 ordered two-hop sequences per base plaquette → **12 orbits**, matching the
canonical count, but only after quotienting by **time reversal** (15 without —
the source does not state this). Breakdown 2 backtrack / 2 same-link /
3 corner / 5 open-path vs the source's 2/2/1/7; backtrack and same-link match
exactly, the remaining 8 orbits are the same 8 under a different label split.

All twelve project into span{q, q², qe₂, e₂, e₃} with **rank exactly 5**,
independently reproducing the certified claim. Integer vectors in
`orbit_vectors.json`.

Derived: with X = Σ w_o(N)·X_o,

    A = 4(w₇ − w₈)
    B = w₈ + w₉ − 2w₅
    D = −12w₂ + 6w₃ + 6w₄ + 6w₅ − 3w₈ − 3w₉

so the tier collapse B = D = 0 reduces to two linear conditions on the weights:

    w₈ + w₉ = 2w₅        (open-path)
    w₃ + w₄ = 2w₂        (corner, given the first)

and A = 4(w₇ − w₈) forces w₇ − w₈ = 5/192 at SU(3), 2/675 at SU(4).

## Stage 3 — complete basis (`extended_basis.py`) — ENUMERATED

The two-hop set is **not** the complete fourth order. Four insertions of V
admit two cluster-size paths:

    1→2→1→2→1   sequential two-hop     144 per base →  12 orbits
    1→2→3→2→1   three-plaquette        976 per base →  67 orbits

**Complete fourth-order basis: 79 orbits.** The two-hop set is ~13% of it.

Three-plaquette intermediates by link-multiplicity profile:

| profile | shape | orbits |
|---|---|---|
| ((1,6),(2,3)) | triangle, three pairwise shared links | 5 |
| ((1,8),(2,2)) | chain, two shared links | 50 |
| ((1,9),(3,1)) | three plaquettes on one common link | **12** |

### Consequences

1. **Max link pile-up over all of fourth order is 3, never 4.** Returning to a
   one-plaquette state in four steps caps the intermediate at three plaquettes.
   So ε-channels open only via fund^⊗3 → singlet, i.e. **only at N = 3**.
   Every N ≥ 4 is generic at fourth order in 3D. This holds for the complete
   basis, not merely the two-hop sector.

2. **A (4,0) terminal family is unreachable at fourth order in 3D.** The
   documents' certified SU(4) exceptional sector, Δq₄ = −304746539168/160249753125,
   therefore cannot originate where they place it ("determinant singlet channels
   enter only at the third resolvent cut"). This is an open inconsistency, not
   something the genericity argument dissolves.

3. **ΔE is uniform only for the two-hop chain.** Every two-hop intermediate has
   exactly 4+4−2 = 6 excited links, so denominators are common there and the
   weights differ only through Haar overlaps. The three-plaquette intermediates
   have three distinct multiplicity profiles, so that simplification does not
   extend.

4. **The completeness diagnostic must wait.** Because the twelve two-hop vectors
   already span rank 5 — the full shape space — the missing 67 orbits cannot
   open new shapes, only shift coefficients. Running generic weights on twelve
   orbits would fail to reproduce α_N = 640/[N(N²−1)³] for reasons that localize
   nothing. The test only becomes informative on the full 79.

## Open

- Amplitudes for the 67 new orbits do **not** factorize into products of
  second-order hop signs, unlike the two-hop case. They require the actual
  strong-coupling matrix elements — i.e. the same group integrals as the
  weights. Geometry alone cannot fix them.
- The SU(4) inconsistency in (2) above.
- Generic Haar weights w_o(N) across all 79 orbits.

## Stage 4 — the odd Gram staircase (2026-08-08) — VERIFIED

Prediction: if the Gram determinant is *counting* the primitive-invariant
staircase, then extending the odd word basis from degree ≤5 to degree ≤7
(where e_7 switches on) must produce new factors vanishing at N = 5 and N = 6.

Computed exactly, by elimination over rational functions in N:

    deg<=5 basis {p3, p5, p2p3}                        (size 3)
    det = (45/2^12)  (N^2-1)^3 (N^2-4)^3 (N^2-9)   (N^2-16)                      / N^3

    deg<=7 basis {p3, p5, p2p3, p7, p2p5, p3p4, p2p2p3}  (size 7)
    det = (14175/2^34)(N^2-1)^8 (N^2-4)^7 (N^2-9)^4 (N^2-16)^3 (N^2-25)(N^2-36)  / N^7

(N^2-25)(N^2-36) appear, each to the first power — exactly as (N^2-9)(N^2-16)
did at degree 5. Confirmed independently: the degree-7 determinant vanishes at
N = 3, 4, 5, 6 and is nonzero for N = 7..12.

Structure: at each degree level the two newest factors enter linearly and the
older ones are promoted; the denominator exponent equals the basis size.

Consequence: the generic odd basis at degree <=7 is valid exactly for N >= 7.
The spatial registry's "stable rank N >= 7" is therefore not a convergence
threshold or an artifact of where the corpus stopped — it is the degree-7 Gram
threshold, i.e. the e_7 step of the classical staircase. Three things that
looked independent are one fact:

    classical Lie staircage (e3; e5 at N>=5; e7 at N>=7)
      = internal odd Gram thresholds (deg<=5 valid N>=5; deg<=7 valid N>=7)
      = spatial registry stable rank N>=7

## Stage 5 — THE REGISTRY IS COMPLETE (2026-08-08)

SU(5) and SU(6) certificates recovered. Both open ranks are closed.

| N | A_N (certified) | 640/[N(N^2-1)^3] | Delta q_N (exceptional) |
|---|---|---|---|
| 3 | 5/12 | 5/12 | e_3 sector |
| 4 | 32/675 | 32/675 | -304746539168/160249753125 |
| 5 | 1/108 | 1/108 | **0** (no mod-5 sector exists) |
| 6 | 64/25725 | 64/25725 | 6/343 |
| >=7 | 640/[N(N^2-1)^3] | — | (stable-rank theorem) |

**The stable-rank mobility formula holds exactly at every rank N >= 3.** It was
derived for N >= 7 and never had an exception. The "open ranks" were open only
in the sense that their certificates were missing from the bundle.

Delta A_N = Delta B_N = 0 at every exceptional rank: determinant channels move
the rest offset q_N and never the mobility. The internal (staircase-sensitive)
and homological (staircase-blind) halves of the theory separate cleanly.

### Independently verified here
- alpha_5 = 1/108 and alpha_6 = 64/25725, predicted at the start of the session
  from the retrodiction at N=3,4, both confirmed by certificate.
- The four-point extraction module reproduces the certified shape vector at
  **four independent ranks** (3,4,5,6): dX=A, dM=A+B/2, dR=A+B, B=D=0, parity
  identity c_R-2c_M+c_X=0, and the bandwidth, all exact.
- The whole SU(6) determinant resolvent, from first principles:
  C_2(Lambda^k V)=k(N-k)(N+1)/2N -> (14/3,21/4,14/3); x4 links -> (56/3,21,56/3);
  E_0-E_int with h=(1/2)sum C_2 -> (-7/2,-14/3,-7/2); F_det=-6/343 (343=7^3);
  C-odd phase -1 -> Delta q_6 = 6/343. Every number reproduced.
- The N-ality family rule p+q <= 6, p-q = +-N, matching parity, reproduces
  SU(4)'s (4,0),(0,4),(5,1),(1,5) and SU(6)'s (6,0),(0,6); at N=5 it admits
  nothing, matching the certified empty mod-5 scan (0 of 895,524 pairs).

### Retracted from earlier in this session
- The claim that epsilon channels cannot activate for N >= 4 at fourth order.
  WRONG. It capped fundamentals-per-link by capping cluster size, conflating
  distinct plaquettes with character insertions. The SU(6) exceptional word has
  root + four insertions + output all on the SAME plaquette, giving (6,0) on
  every boundary link with a cluster of size one.
- The factorization alpha_N = [1/C_2(f)^3][80/N^4] as a *mechanism*. Three cuts
  is right; the denominators are antisymmetric-power Casimirs, not C_2(fund)^3.
  Correct arithmetic, wrong explanation.
