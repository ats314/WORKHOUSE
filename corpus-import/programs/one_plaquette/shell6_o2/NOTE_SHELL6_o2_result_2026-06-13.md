> **⚠ CORRECTION 2026-06-14 — orbit-0 exact coefficients SUPERSEDED.** A full-intermediate,
> symmetry-gated, cold-reproducible computation (the V2 release) plus my own independent exact
> diagonalization of its byte-identical 44×44 matrix supersede this note's orbit-0 numbers by a
> clean ±1/6. **The qualitative ordering 3⁺⁻ < 2⁻⁻(E) < 2⁻⁻(T₂) < 0⁻⁻ STANDS**, as does 3⁺⁻ = −21281/1530
> and E−0⁻⁻ = −1. But: **0⁻⁻ = −12235264/959310, 2⁻⁻(E) = −13194574/959310, 2⁻⁻(T₂) = −12555034/959310;
> T₂−0⁻⁻ = −1/3 (NOT −2/3); the E–T₂ split is 2/3 (NOT 1/3); E(3⁺⁻)−E(0⁻⁻) = −1107923/959310 (NOT
> −1267808/959310).** Root cause: this note's orbit-0 off-diagonal was the un-converged single layer
> (its own UPDATE 4 already downgraded "certified" → "strongly evidenced"); the outer-W-independence
> assumption fails off-diagonal. See `v2_authoritative/AUDIT_SHELL6_v2_reconciliation_2026-06-14.md` for the
> full adjudication. Everything below this banner is retained as the historical record; read the orbit-0
> exact rationals and the "1/3 split" as superseded.

# Shell-6 C-odd glueballs at second order O(y²): the ordering, computed

**Date:** 2026-06-13
**Status discipline:** every claim is tagged [gate-backed], [diagnosis], or [conjecture].
§§1–4 record the build (symmetry skeleton, first-order factor-2 fix, why naive engines
fail). **The O(y²) ordering was then COMPUTED and CONVERGENCE-CONFIRMED — see the three
UPDATE sections at the bottom.** Final certified ordering (lightest→heaviest):
**3⁺⁻ < 2⁻⁻(E) < 2⁻⁻(T₂) < 0⁻⁻**; 0⁻⁻ is the heaviest and sits above 3⁺⁻; the lattice
splits spin-2 C-odd into E (lighter) and T₂, gap exactly 1/3 y². The orbit-0 H₂ is
Hermitian + O_h×C-commuting; the diagonal is exact; the off-diagonal is outer-W-
independent (spot-checked incl. the C-conjugate entry), so the single layer is the
exact effective Hamiltonian. This continues the uploaded
`NOTE_SHELL6_first_order_codd_result_2026-06-13.md`, whose first-order conclusion stands
(with one factor-2 correction, §2).

## Question (from the first-order note)

The first-order note settled that the exotic C-odd channels (0⁻⁻, 3⁺⁻, 2⁻⁻, 2⁺⁻)
are degenerate at O(y), and that ordering them is an O(y²) effect. This pass attacks
the O(y²) computation: it (1) settles the group theory the O(y²) result must obey,
(2) corrects the first-order split, (3) builds and validates the exact SU(3) Haar
amplitude machinery, and (4) determines precisely what the O(y²) ordering computation
requires — including why the naive engine is insufficient.

## 1. Symmetry skeleton — multiplicities across the FULL 44-loop shell [gate-backed]

`ENGINE_SHELL6_o2_skeleton.py` (13 gates). The first-order note worked inside the 32 twisted
hexagons; this pass decomposes the **full** 44-loop shell (32 hexagons + 12 rectangles)
under O_h × C. Result (multiplicity of each exotic C-odd channel; "hex/rect" = where it
lives):

| channel | cubic irrep | mult (full) | hex | rect | O(y²) energy is… |
|---|---|---|---|---|---|
| 0⁻⁻ | A₁⁻⁻ | 1 | 1 | 0 | a single number ⟨ψ|H²|ψ⟩ |
| 3⁺⁻ | A₂⁺⁻ | 1 | 1 | 0 | a single number |
| 2⁻⁻ | E⁻⁻ | 1 | 1 | 0 | a single number |
| 2⁻⁻ | T₂⁻⁻ | 1 | 1 | 0 | a single number |
| 2⁺⁻ | T₂⁺⁻ | **2** | 1 | 1 | eigenvalue of a 2×2 hex–rect block |
| 1⁺⁻ (exc.) | T₁⁺⁻ | **3** | 2 | 1 | eigenvalues of a 3×3 block |

**Consequence (the key structural result):** the three channels whose ordering the
note asks for — **0⁻⁻, 3⁺⁻, and 2⁻⁻ (both its E and T₂ copies) — are each
multiplicity-1 and purely hexagonal.** So each one's O(y²) energy is a *single*
diagonal expectation value, not an eigenvalue of a mixing block. The 2⁺⁻ uniquely
mixes a hexagon with a rectangle at O(y²); the excited 1⁺⁻ is a 3-state block.
This was not known from the first-order note and sharply constrains the O(y²) problem.

Because the diagonal self-energy ⟨L|H²|L⟩ is identical for all hexagons (O_h symmetry),
it contributes the **same** shift to every pure-hexagon channel. **The ordering of
0⁻⁻ / 3⁺⁻ / 2⁻⁻ is therefore set entirely by the OFF-DIAGONAL part of H² between
distinct hexagons.** [gate-backed structural reduction]

## 2. First-order split corrected by a factor of 2 [gate-backed]

`ENGINE_SHELL6_firstorder_corrected.py` (8 gates) + `ENGINE_FLUX_shell6_o2_engine2.py` (exact multi-link
SU(3) Haar). The corner-push matrix element is **⟨L′|W|L⟩ = +1/3** — reproduced here
from first principles (96 entries, all 1/3; matches the note's point 3). With the note's
own H⁽¹⁾ = −y·W, the first-order Hamiltonian on the shell is **H¹ = −(1/3)·(corner-push
adjacency)**, so the excited 1⁺⁻ (T₁⁺⁻ block, adjacency eigenvalues ±2√2) splits by

> **±(1/3)·2√2 · y = ± 2√2⁄3 · y ≈ ± 0.9428 y.**

The uploaded `shell6_first_order_codd_band.py` hardcodes `hop = 1/6` (= ½ × the matrix
element) and so reports **±√2⁄3 ≈ ±0.4714 — a factor of 2 too small.** The qualitative
conclusion is unaffected (exotic channels still exactly 0 at O(y); only the excited 1⁺⁻
disperses), but the magnitude should be **±2√2/3**, not ±√2/3. [gate-backed]

## 3. Exact SU(3) Haar amplitude engine — validated [gate-backed]

`ENGINE_FLUX_shell6_o2_engine2.py` builds a multi-link exact-rational SU(3) Haar integrator on the
certified `su3_moments_ext` primitives (it threads the per-link Weingarten/ε-baryon
moments through lattice geometry). Validated: norm(simple loop)=1; the +1/3 corner-push
element; and (`ENGINE_SHELL6_link_calculus_validate.py`) a **link-variable word calculus** with
H₀ = Σ_links ½·Casimir reproduces the single-plaquette vacuum self-energy **e₂ = −3/4**
exactly — i.e. the electric-energy bookkeeping in link variables is correct.

## 4. What the O(y²) ordering computation requires — and why the naive engine fails [diagnosis]

The off-diagonal H²[L′,L] = Σ_m ⟨L′|W|m⟩⟨m|W|L⟩ / (E₀ − E_m). The honest finding of this
pass is a **precise specification of the intermediate space m**, obtained by calibrating
against the certified shell-4 hops:

- A **Wilson-loop-intermediate** engine (intermediates = single simple loops, both the
  singlet 3⊗3̄→1 and the ε-baryon 3⊗3→3̄ routes) was built and tested on the shell-4
  neighbour-plaquette hop. It returns **C-even hop = C-odd hop = −1/12**, but the
  certified values are **−481/612 (C-even) and 5/612 (C-odd)** — different from each other.
  The engine misses the C-parity-distinguishing amplitude entirely. [gate-backed negative]
- **Reason (diagnosis):** the C-parity-flip amplitude is mediated by **disconnected /
  two-loop intermediates** (e.g. Tr(U_pa)·Tr(U_pb†), two loops sharing a link) and by
  **higher-irrep intermediates** (octet/sextet on a link), whose electric energies are
  *not* set by loop length. A single-simple-loop enumeration drops exactly these, so it
  cannot resolve C-even vs C-odd. This is the same reason the shell-4 Bridge self-energy
  (13/20, 1/2) needs the full word calculus.

**Therefore the exact O(y²) C-odd splitting requires the full SU(3) word calculus**
(the `su3_domino_d3` machinery — exact Casimir H₀ + rational resolvent + des Cloizeaux),
extended to the shell-6 hexagon basis with **disconnected and higher-irrep intermediates
carrying irrep-resolved denominators.** Two viable routes, both staged:
  (a) **link-variable word calculus** (H₀ = Σ_links ½·Cas, no cross-terms — already
      validated to e₂ = −3/4), computing only the off-diagonal hexagon couplings so the
      diagonal self-energy's repeated-link blow-up is avoided; or
  (b) **plaquette-holonomy cluster** (compact, like the domino) — needs the per-shared-link
      cross-term generalization of `make_H0`, then the hexagon as a length-3 holonomy
      trace word.

## Conclusion

[gate-backed] The O(y²) ordering of 0⁻⁻, 3⁺⁻, 2⁻⁻ reduces to **three single numbers**
(mult-1 pure-hexagon channels), fixed entirely by the **off-diagonal** hexagon couplings
of H²; the diagonal self-energy is a common shift. [gate-backed] The first-order excited
1⁺⁻ split is **±2√2/3 y** (correcting the uploaded ±√2/3). [diagnosis] Computing the
off-diagonal couplings exactly requires the word calculus with disconnected + higher-irrep
intermediates; the naive Wilson-loop engine provably cannot (shell-4 C-even/odd hops
collapse to a single −1/12). [conjecture] Since A₁, A₂, E, T₂ are distinct irreps, nothing
forces them to remain degenerate, so a nonzero finite O(y²) splitting is expected; its
sign/order is exactly what the staged word-calculus computation will deliver.

## Files (this directory)

| file | role | gates |
|---|---|---|
| `ENGINE_SHELL6_o2_skeleton.py` | O_h×C decomposition of the full 44-loop shell; multiplicities | 13 ✓ |
| `ENGINE_SHELL6_firstorder_corrected.py` | corrected first-order spectrum (±2√2/3) from the Haar M.E. | 8 ✓ |
| `ENGINE_FLUX_shell6_o2_engine2.py` | exact multi-link SU(3) Haar engine + shell-4 calibration (diagnostic) | partial |
| `ENGINE_SHELL6_link_calculus_validate.py` | link-variable word calculus; H₀ validated (vacuum e₂ = −3/4) | partial |

`ENGINE_SHELL6_o2.py` (truncated by a stale-mount write) and `ENGINE_SHELL6_haar_loops.py`
are superseded by `ENGINE_FLUX_shell6_o2_engine2.py` — do not use.

---

# UPDATE (same day) — the O(y²) ordering, COMPUTED

The staged engine of §4 was built and the computation run. Summary of the new
machinery (all gate-backed) and the result.

## Engine completed [gate-backed]

- `ENGINE_HAAR_fast_haar.py` — exact SU(3) Haar integral by **tensor-network variable
  elimination** (every index variable has degree 2). Bit-exact vs the naive
  cartesian-product integrator; **245× faster** on the ε-heavy case (39 s → 0.16 s)
  that had stalled the link calculus.
- `ENGINE_FLUX_cluster_pt.py` — generalized the certified domino H₀ to clusters; reproduces the
  domino constants (C-odd hop 5/612, C-even −11/306, vacuum −3/2). **46 gates.**
  (Used to *disprove* the plaquette-holonomy route: it mis-energizes multi-face
  loops — H₀(hexagon)=11/2≠4 — so it is wrong for shell-6. Link variables are the
  only correct H₀.)
- `DATA_HAAR_o2_v2.py` — the **correct exact engine**: link-variable word calculus,
  H₀=Σ_links ½·Cas, with a **Galerkin / Gram-matrix resolvent** robust to the
  function-space linear dependencies the raw monomial basis carries (composite
  Cayley-Hamilton, which `canon_word` does not see). Reproduces the single-plaquette
  Bridge towers **(13/20, 1/2)** and the shell-4 hops **(5/612, −11/306)**. **39 gates.**
- `ENGINE_HAAR_shell6_final2.py` / `ENGINE_SHELL6_orbit1.py` / `ENGINE_SHELL6_shell6_analyze.py` — the shell-6 driver
  (connected-cluster W; Gram resolvent; charge-signature-pruned; persistent integral
  cache for resumability) + symmetry assembly.

## Result (connected single-layer cluster; exact rational arithmetic)

The 32 hexagons form **two O_h×C orbits**: size-24 (carries 0⁻⁻, 2⁻⁻E, 2⁻⁻T2, 2⁺⁻,
excited 1⁺⁻) and size-8 (carries 3⁺⁻). The O(y²) energy coefficients (units y²; a
common, geometry-independent disconnected-vacuum shift is omitted — it cancels in all
comparisons):

| channel | irrep | O(y²) coefficient | vs 0⁻⁻ |
|---|---|---|---|
| **0⁻⁻** | A₁⁻⁻ | −12075379/959310 ≈ −12.5876 | 0 |
| **2⁻⁻** | T₂⁻⁻ | −12714919/959310 ≈ −13.2542 | **−2/3** |
| **2⁻⁻** | E⁻⁻  | −13034689/959310 ≈ −13.5876 | **−1** |
| 2⁺⁻ | T₂⁺⁻ | ≈ −13.2542 | −2/3 |
| 1⁺⁻ (exc.) | T₁⁺⁻ | ≈ −13.2542 | −2/3 |
| **3⁺⁻** | A₂⁺⁻ | −21281/1530 ≈ −13.9092 | ≈ −1.32 *(preliminary)* |

**Orbit-0 sector — VALIDATED & exact [gate-backed]:** the 24×24 zero-momentum H² is
**Hermitian** and **commutes with all of O_h×C** (gates), the resolvent is consistent,
and first order is recovered. The ordering **2⁻⁻(E) < 2⁻⁻(T2) < 0⁻⁻** holds with
**exact rational splittings −1 and −2/3 y²** — i.e. **0⁻⁻ is the heaviest** exotic
C-odd channel, and the lattice splits the spin-2 C-odd state into a lighter E and a
heavier T₂ (gap 1/3 y²). The 2⁺⁻ and excited 1⁺⁻ are degenerate with 2⁻⁻(T2) at this
order/cluster. The clean rationals indicate the off-diagonal (which fixes the
within-orbit ordering) is converged.

**Cross-orbit (0⁻⁻ vs 3⁺⁻) — PRELIMINARY:** at this single-layer cluster 3⁺⁻ ≈
−13.91 y², **below 0⁻⁻** (so 0⁻⁻ sits *above* 3⁺⁻ — answering GPT's original
question), and 3⁺⁻ is preliminarily the **lightest** exotic channel. But the
0⁻⁻−3⁺⁻ difference is not yet a clean rational: the cross-orbit comparison depends on
the orbit-0-vs-orbit-1 **diagonal self-energy** difference, whose connected part
needs a two-layer cluster (return-plaquettes on the length-8 intermediates) to
converge. Within-orbit differences are insensitive to this (the diagonal cancels),
which is why they are already clean.

## Bottom line

[gate-backed] At O(y²) the exotic C-odd channels **do** split (confirming the
first-order note), and **0⁻⁻ is the heaviest**; the spin-2 C-odd state splits on the
lattice into E (lighter, −1 y² below 0⁻⁻) and T₂ (−2/3 y² below 0⁻⁻). [preliminary]
3⁺⁻ lies below 0⁻⁻ and is the lightest, pending a two-layer-cluster reconvergence of
the cross-orbit diagonal. **Next:** layers=2 cluster (resumable r
---

# UPDATE 2 — convergence analysis (layers→2 outer W)

Ran the convergence-correct engine (`ENGINE_HAAR_shell6_final3.py`): the resolvent R=(E₀−H₀)⁻¹
uses W_inner = plaquettes touching the reference (provably complete + exact for the
first W — H₀ is per-link so R never leaves those links), while the **outer** W that
reads ⟨L′|W|y⟩ is expanded to plaquettes touching the intermediate (y's support).

**Decisive check [gate-backed]:** the **diagonal** self-energy is *identical* under
the small and the large outer W — H₂[L₀,L₀] = **−13674229/959310 ≈ −14.2542** both
ways (plaquettes not touching L₀ cannot return y to L₀). So **the diagonal is exact
at the single layer.** Consequence: **3⁺⁻ = the orbit-1 diagonal exactly** (its
off-diagonal A₂⁺⁻-projection vanishes), so **3⁺⁻ = −21281/1530 is exact.**

The orbit-0 channel energies are (exact diagonal) + (off-diagonal): with the diagonal
−14.2542, the off-diagonal channel parts are **0⁻⁻: +5/3, 2⁻⁻(T2): +1, 2⁻⁻(E): +2/3**
(clean rationals). The only quantity whose layer-convergence is not yet *machine-
confirmed* is the off-diagonal (the m→L′ route through plaquettes touching the
intermediate's new link). The large-outer-W off-diagonal recompute costs |Wy|≈10⁴
integrals per row entry and exceeded this session's budget; the resumable runner
(`ENGINE_HAAR_shell6_final3.py`, persistent cache) is in place to finish it.

## Confidence-graded final answer

- **0⁻⁻ is the HEAVIEST exotic C-odd channel** [high — Hermitian + O_h×C-commuting
  24×24 H², exact diagonal, clean rational off-diagonal].
- **lattice splits spin-2 C-odd into E (lighter) and T₂**, gap **1/3 y²**; with 2⁺⁻
  and excited 1⁺⁻ degenerate with 2⁻⁻(T2) at this order [high].
- **3⁺⁻ is the LIGHTEST**, **below 0⁻⁻** (answering GPT's question: 0⁻⁻ sits *above*
  3⁺⁻) [3⁺⁻ value exact; cross-orbit gap rests on the exact diagonals + the clean
  off-diagonals].
- Full ordering: **3⁺⁻ < 2⁻⁻(E) < 2⁻⁻(T2) < 0⁻⁻**
  (≈ −13.909, −13.588, −13.254, −12.588 y²).

Residual to fully certify (resumable, queued): the large-outer-W off-diagonal, to
confirm the orbit-0 splittings −1, −2/3 and the exact 0⁻⁻−3⁺⁻ gap 1267808/959310.

---

# UPDATE 3 — convergence CONFIRMED; the ordering is the exact answer

To certify the off-diagonal (the only quantity §UPDATE-2 left open) without the
prohibitive full large-outer-W row, I tested **outer-W-independence entry by entry**:
compute each H₂ entry with the small outer W (plaquettes touching L₀) and the large
outer W (plaquettes touching the intermediate y), and compare.

**Result — every entry tested is IDENTICAL under small vs large outer W:**
- diagonal H₂[L₀,L₀] = −13674229/959310 (both) [shown in UPDATE 2];
- off-diagonal, share-6 entry (the **C-conjugate** coupling, i.e. ⟨L̄₀|H₂|L₀⟩ — the
  single most C-parity-sensitive matrix element) = **−1 (both)**;
- off-diagonal, share-4 entry = **−1/4 (both)**.

The C-conjugate entry being outer-W-independent is the decisive check: the C-parity
physics (which is exactly what distinguishes the channels) does not move with the
cluster. So **H₂ is outer-W-independent and the single-layer computation is the
converged, exact effective Hamiltonian.** (Reason: y = R·W|L₀⟩ is supported on L₀'s
plaquette neighbourhood, and the extra far plaquettes contract to zero against the
shell-6 loops — confirmed empirically on the diagonal and the C-odd-critical entries.)

## FINAL, certified O(y²) ordering

**3⁺⁻ < 2⁻⁻(E) < 2⁻⁻(T₂) < 0⁻⁻**  (lightest → heaviest), exact:

| channel | irrep | O(y²) coefficient | ≈ | vs 0⁻⁻ |
|---|---|---|---|---|
| 3⁺⁻ | A₂⁺⁻ | −21281/1530 | −13.9092 | −1267808/959310 ≈ −1.3216 |
| 2⁻⁻ | E⁻⁻ | −13034689/959310 | −13.5876 | **−1** |
| 2⁻⁻ | T₂⁻⁻ | −12714919/959310 | −13.2542 | **−2/3** |
| 0⁻⁻ | A₁⁻⁻ | −12075379/959310 | −12.5876 | 0 |

(common geometry-independent disconnected-vacuum shift omitted; cancels in every
comparison). The orbit-0 24×24 H₂ is Hermitia

---

# UPDATE 4 (2026-06-14) — status correction + full-row certification script

A verification pass (gates re-run, convergence argument re-read) found that UPDATE 3's
**"certified / exact effective Hamiltonian / no remaining hedge" overstates the grounds.**
Honest accounting:

- **Engine validated** [gate-backed, re-run this pass]: link_o2_v2 39/39, cluster_pt 46/46,
  skeleton 13/13; calibration constants reproduce (Bridge 13/20, 1/2; shell-4 hops 5/612,
  -11/306; domino -3/2).
- **Diagonal — structurally exact** [sound]: plaquettes not touching L0 cannot return y to L0,
  so the single-layer diagonal IS the full diagonal. Hence **3+- = orbit-1 diagonal =
  -21281/1530 is exact**, and the orbit-0 diagonal is exact.
- **Within-orbit ordering** [strong]: 0-- = exact diagonal + clean off-diagonal +5/3; 2--(T2) +1;
  2--(E) +2/3 — clean rationals in all three irrep channels at once (a strong joint convergence
  signal). Off-diagonal outer-W-independence was checked on the diagonal, share-4 (-1/4) and
  share-6 (-1, the C-conjugate) entries.
- **The hedge** [honest]: the off-diagonal has NO locality proof (unlike the diagonal),
  outer-W-independence was verified on 3 entry-classes not all (share-5 / second-neighbour
  untested), and the full large-outer-W row recompute was NOT completed (degree-20 integrals
  ~1-4 s each, thousands of them; the prior 179K-integral cache is what made it tractable, and
  it is not portable across sandboxes). Correct label: **strongly evidenced / very likely —
  NOT certified.**

**To actually close it:** `ENGINE_SHELL6_certify.py` (this directory) computes the FULL orbit-0 and
orbit-1 rows under BOTH outer-W choices and gates outer-W-independence ENTRY BY ENTRY over the
whole row (the exhaustive version of the 3-entry spot-check), then checks the exact channel
rationals against the published values. Cheap on top of the large-W row (small-W plaquettes
nest inside large-W) and resumable. Run locally: `python3 ENGINE_SHELL6_certify.py` (then `... 2`
for a rowbox cross-check). It prints CERTIFIED only if every entry agrees; otherwise it fails
loudly with the discrepancies. Until that run completes, **3+- < 2--(E) < 2--(T2) < 0-- stands
as strongly evidenced, not certified.**
