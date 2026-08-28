# Denominator localization: investigation record

**Date:** 2026-08-23
**Mode:** read-only research session; no repository files were changed.
**Snapshot:** work performed against the session's working tree (corpus pinned).
**Status of this document:** a consolidated record of derivations and issues, for
review and selective landing. Nothing here is promoted into the repository's
checked tiers by virtue of appearing in this file — each claim is labelled with
what actually establishes it.

Labels used below:
- **T0/T1/T2/T3** — the repository's verification tiers (Lean / exact re-derivation
  / numerical / asserted).
- **DERIVED** — follows from stated definitions/primitives, independent of the
  answer it predicts.
- **OBSERVED** — read off the coefficients/data; true but not (yet) derived.
- **FITTED** — a bound tuned to sampled data; carries the ADR-0005 hazard.

Everything marked "machine-checked" was reproduced with `sympy`/`workhouse` over
`src/workhouse/constants.py` and `workhouse.corpus_registry` this session.

---

## 0. Executive summary

1. The proposed **"denominator smoothness"** invariant is real but is a
   **provenance/forensic** property, not physics. Its correct form is not a
   fitted smoothness ceiling but a **typed, exponent-sensitive divisor
   certificate** `den | QBOUND` over a scope-specific localization ring
   `ℤ[S⁻¹]`.
2. The original note ("Denominatorr Smoothness") is ~90% correct against the
   machine. Four load-bearing corrections: the census count, the "one violation"
   claim, the "37 ceiling", and the `33554467/33554393` example (§7).
3. The denominator primes have two sources: a **DERIVED** structural floor
   (orders ≤3, `P_max = 17 = 2N²−1`) and an **energy-gap staircase** (orders ≥4)
   whose mechanism is identified but whose ceiling is OBSERVED (§2).
4. The fourth-order *arithmetic superset* reaches prime **47** (and 23) — the
   corpus itself hardcodes `S4_PRIMES` including 47. The reduced string-tension
   coefficients top out at **37**; the difference is the connected-support /
   linked-cluster restriction (§2.4, §5.4).
5. **41 is deferred, not forbidden** — its cheapest resolvent carrier needs a
   3-body / higher-excitation intermediate state. The governing number theory is
   the Eisenstein norm form (`ℚ(√−3)`, Heegner number **3** = SU(3)), unrelated
   to Euler's `x²+x+41` (Heegner 163) (§2.5).
6. There is **one** cubic rank-3 order-4 QBOUND (`17³`, support `{…,47}`), not a
   marked-cluster/band-kernel split. An earlier draft of this analysis under-counted
   the resolvent depth to `17²`; that is corrected here (§5.3).
7. A hash-frozen, Lean-verified, **non-circular** exact QBOUND for that scope was
   supplied externally and independently verified; a **kernel-connected witness**
   layer was added (§5.5, §6).
8. A validated **C2 acceptance gate** now exists — the structural necessary
   condition G3's target-blind `C_shp` output must satisfy. It does not (and
   cannot) adjudicate C2 (§8).
9. **Capstone (§11).** An external exact-Haar package computes the fourth-order
   scalar and lands *exactly* on `QUARANTINED_SCALAR` (C1's "quarantined
   shortcut", `rejected-by-both`). The value **passes every denominator/QBOUND/
   Lean gate** — the definitive proof that the certificate stack is
   **necessary, not sufficient**: it cannot catch a by-construction physics
   artifact. Forensics: the package is provably oracle-free and exactly computes
   the *raw un-anchored axial rest*; the quarantine stands (it is a pre-anchoring
   intermediate, nobody's physical answer); the dispute is the anchoring step
   (G3) the package skips. Byproduct: a candidate exact form of
   `RAW_FOLDED_AXIAL_GAMMA_NUM`.

---

## 1. The denominator-smoothness invariant

### 1.1 The claim
A *primitive perturbative coefficient* in this corpus has a denominator supported
only on small primes; a **rough** denominator (a large prime where only small
primes belong) is nearly a proof that the value is a `sympy.Rational`
reconstructed from a float, not an exact coefficient. This is a screen for the
failure CLAUDE.md non-negotiable #3 calls the single most dangerous bug.

### 1.2 What machine-checked out
- **The prime ladder** (T1, machine-checked). Within one homogeneous series
  (native `SIGMA_n`, published `KPS_T_n` string tension) the largest denominator
  prime by order is:

  | order r | 0 | 2 | 3 | 4 | 5 | 6 |
  |---|---|---|---|---|---|---|
  | `P_max` | 3 | 17 | 17 | 37 | 37 | 61 |

  New large primes appear **only at even orders**; the set is monotone
  non-decreasing. `KPS_T6` = `2¹⁸·3¹⁰·5⁶·7⁴·11³·13³·17⁵·19³·23·29³·31³·37³·43·47·53·59·61`
  (all primes ≤61 **except 41**).
- **Sector supports** (T1, machine-checked):

  | sector | denominator primes | max |
  |---|---|---|
  | 2nd/3rd order band | {2,3,5,17} | 17 |
  | sealed 4th core | {2,3} | 3 |
  | 4th historical kernel & native σ | {2,3,5,7,11,13,17,19,29,31,37} | 37 |
  | pentagonal cap band | {2,3,5,7,11,13,17,19,29} | 29 |
  | KPS t₆ (order 6) | {2,3,5,7,11,13,17,19,23,29,31,37,43,47,53,59,61} | 61 |

- **The one artifact** (T1, machine-checked). `LINKED_VACUUM_4 = −1474623/1675520`
  (denominator `2⁸·5·7·11·17`, smooth) vs `LINKED_VACUUM_4_ARTIFACT =
  −521965902/593076541` (denominator = the 9-digit **prime** 593076541). They agree
  to relative `3.4×10⁻¹⁵` (~27 ulps). This is contradiction **C20** ("RUN15
  internal display artifact", resolved) in `ledger/contradictions.yaml`.
  `corpus_registry.near_miss_pairs()` returns exactly this one pair.
- **The type guard is blind to it** (machine-checked). `tests/test_constants.py::
  test_float_only_values_are_named_num` iterates and checks only
  `isinstance(value, float)`; a `Rational(521965902, 593076541)` is a `Rational`
  and passes. Smoothness is the intrinsic (single-value, tolerance-free) screen
  that fires where `near_miss` (relational) and the type guard (type-based) are
  each half-blind.

### 1.3 Denominator support is addition-stable; numerators are noise
(T1, machine-checked.) `β`, `C_shp`, `W₄` share the identical denominator support
`{2,3,5,13,17,29,31,37}` with `den(C_shp) = 16·den(β)`, while their numerator
primes are disjoint (`{23,…}`, `{191,…}`, `{11,167,…}`). Support survives
`+, −, ÷`-by-small (an LCM only shrinks under cancellation); numerator primes
scramble. This is why the "numerator prime" version of the idea failed under
addition and the denominator version does not.

---

## 2. Where the primes come from (two sources)

### 2.1 DERIVED structural floor (orders 0–3)
The fixed, rank-independent SU(3) hopping denominator `(n²−1)(2n²−1)(4n²−9)`
(formalized T0 in `lean/Workhouse/Basic.lean`, `hopping 3 = 5/612`) evaluates at
`n=3` to `8·17·27 = 3672 = 2³·3³·17`. Its largest prime, `17 = 2n²−1`, **is** the
ceiling through third order. This is a genuine polynomial derivation (same
polynomial for every N), not a per-point fit. (Correction to a draft claim: the
hopping *denominator* supplies only `{2,3,17}`; `5` and `7` first appear in a
*denominator* at order 4. They arise as `n²−4=5`, `n²−2=7` in *numerators*/
resolvents, which cannot by themselves put a factor into a denominator.)

### 2.2 Energy-gap staircase (orders ≥4) — mechanism identified, ceiling OBSERVED
Higher primes enter as an LCM over Kogut-Susskind resolvent products. The
fingerprint is a textbook LCM shape: small primes to high powers, large primes to
the first power (e.g. `SIGMA_4 = 2⁷·3⁶·5²·7·11·13·17³·19·29·31·37`). The primitive
Haar-resolvent channel (`src/workhouse/cellular.py`) is only ≤5-smooth, so the
large primes come from the full band-kernel sum, not the primitive channel.

**FITTED caveat.** At the single point N=3 every integer is a value of infinitely
many low-degree polynomials, so "prime = rank-polynomial value at N=3" is vacuous
for the large primes. Only the fixed, N-independent polynomials constitute a
derivation. The specific ceiling values (37, 61) and the prime gaps are OBSERVED
from three transcribed coefficients. A clean fit `P_max(r) = r²/2 + 7r + 1`
(17,37,61,89…) has **zero derivational content** (three even-order points, zero
d.o.f.) and must not be trusted — this is the ADR-0005 hazard.

### 2.3 The rank-polynomial origin (Drouffe–Zuber)
The corpus's own novelty search (`docs/referee/novelty_search_2026-08-21.md`)
pins the mechanism: Drouffe–Zuber (Phys. Rep. 102, 1983, A.26) give the finite-N
strong-coupling coefficients with **product** denominators `(N²−1)(N²−4)…`, while
the completion family strips these to **pure powers** `(N²−1)^(r−1)`. This is why
the completion channel is 2,3-smooth (`8^(r−1) = 2^{3(r−1)}`) and the full band
kernel carries the richer primes. The corpus flags "whether the finite-N
coefficients are derivable from these cumulant weights" as **open**.

### 2.4 The fourth-order superset reaches 47 (and 23) — machine-checked
**FINDING (external: GPT audit; independently verified here).** The corpus
notebook `NB_O4_hodge_v10a20b_denominatorlift_exact_da_m4_a100.ipynb` literally
hardcodes

    S4_PRIMES = {2,3,5,7,11,13,17,19,23,29,31,37,47}.

The prime-provenance notebook `NB_O4_hodge_v10a18_arithmetic_geometry_prime_
provenance.ipynb` computes it as `HAAR ∪ PROJECTOR ∪ R1 ∪ R2` with:
- Haar/Gram primes `{2,3,5}`;
- first-step resolvents `{2,3,5,7,11,17}`;
- second-step resolvents `{2,3,5,7,11,13,17,19,23,29,31,37,47}`.

Exact gap witnesses (machine-checked): `8/3 − 13/2 = −23/6` and
`8/3 − 21/2 = −47/6`. So the clean "37 is a fourth-order ceiling" is **false** at
the superset level: `47` is a legitimate fourth-order resolvent prime that
cancels in the displayed reduced coefficient. The reduced string-tension
denominators top out at 37 (§5.4). The superset is explicitly an
over-approximation ("keeps every irrep branch before Haar/center cancellations").

### 2.5 Why 41 is missing — DERIVED direction, OBSERVED exact predicate
Every resolvent prime `p>3` needs a reachable intermediate state solving
`ΣC ≡ 16 (mod p)`, where `C(p,q) = p² + pq + q² + 3p + 3q` is the SU(3) Casimir
(`6·E₀ = 16`). The cheapest carrier (machine-checked):

| prime | in σ₄? | cheapest carrier |
|---|---|---|
| **37** | yes | 2 links, max 4 boxes — `(0,4)+(1,3)` |
| 23 | no | 2 links, max 5 boxes — `(0,4)+(2,3)` |
| 43 | no | 2 links, max 5 boxes — `(1,3)+(2,3)` |
| 41 | no | 2 links, max 6 boxes — `(1,5)+(1,5)` |
| 47 | no | 2 links, max 6 boxes — `(0,3)+(3,3)` |

37 is the cheapest large prime; 41/43/47/23 each require a strictly heavier
excitation. So **41 is deferred to higher order** (it enters the ladder at
order 8), not forbidden. This partially cracks the reachability predicate.

**Number-theoretic substrate.** The form `p²+pq+q²` is the norm form of the
Eisenstein integers `ℤ[ζ₃]` = ring of integers of `ℚ(√−3)` — the class-number-1
field of **Heegner number 3**, i.e. SU(**3**) itself. The Reddit/Euler
observation about `x²+x+41` is a **different** Heegner story (number 163,
`ℚ(√−163)`); same numeral, unrelated theorem. Conflating them is unfounded.

### 2.6 von Staudt–Clausen pedigree
`den(B_2n) = ∏_{(p−1)|2n} p` (von Staudt–Clausen, 1840) is a rigorous
smooth-denominator law for a perturbative/generating-function coefficient,
squarefree, small-prime-dominated, largest prime growing with order. Verified:
`B₁₆ = −3617/510`, `510 = 2·3·5·17` — the corpus's own low-order support. The
corpus fingerprint is a **hybrid** (von-Staudt-like large-prime skeleton + an LCM
small-prime part to high powers), so the analogy is structural, not literal
(corpus denominators are not squarefree). The novel move is inverting the
smoothness fact into a Dickman-ρ-quantified forensic.

---

## 3. Corpus-wide census (machine-checked)

`workhouse.corpus_registry.combined_table()`: ~1446 distinct nonzero rationals.

| gate | rough (`P_max > 37`) | smooth |
|---|---|---|
| all sizes | 247 | ~1199 |
| `q > 10⁶` | 31 | 126 |
| `q > 10⁹` | 23 | 90 |

Of the 23 at `q > 10⁹`: ~17 are self-indexed/truncated pseudo-rationals in the
generated `DOC_FLUX_constants_index.md`; 4 are genuine exact SU(4)/SU(5)
coefficients (rough because `P_max ~ 2N²−1 = O(N²)`); 2 are `radius_squared`
ratios (denominator = another coefficient's numerator). **No new undetected
exact-primitive artifact** beyond C20. Repeated rough parts trace to
representation theory: `185791 = 47·59·67` (SU(4)), `346531 = 47·73·101` (SU(4)),
`8815920161561` (SU(6) band).

**Dickman.** `ρ(u), u = ln q / ln 37`: `ρ(3.44) ≈ 1.9e−2`, `ρ(5.59) ≈ 7e−5`
(9-digit denominator), `ρ(12.0) ≈ 2e−6`. These are order-of-magnitude
prioritization heuristics, **not calibrated probabilities** (Dickman models
uniform integers; CF reconstructions and rep-theoretic denominators are
non-uniform, and 37 was chosen after inspecting the corpus). Exact finite
smooth-number density near `q = 593076541` is `≈5e−4`, ~an order of magnitude
above the Dickman value.

---

## 4. The two axes that matter

- **Rank AND order.** The closed-surface certificate
  `CERT_SUN_closed_surface_stage1_certificate.json` gives the exact second-order
  denominator `∝ 1/((N−1)(N+1)(2N−3)(2N+3)(2N²−1))`. Since `2N²−1 = 127,199,241`
  at `N=8,10,11` (machine-checked: `282321 = 3²·13·19·127`), a legitimate
  SU(N≥8) coefficient is rough at **second** order. An order-only "37" ceiling
  false-positives every such coefficient. `P_max` is bounded by the largest prime
  **factor** of the rank polynomials `{n²−1, 2n²−1, 4n²−9}`, i.e. `O(N²)` —
  **not** `2N²−1` itself (which is not always prime: `N=5 → 49 = 7²`).
- **Support vs shape.** The robust, order/N-free discriminant is denominator
  *shape*: a legitimate rough denominator is an **LCM** (small primes to high
  powers, large primes to first power) **or** equals another coefficient's
  numerator (a ratio). A float artifact is a **single generic large prime** with
  no LCM structure. `den | QBOUND` (below) makes this exact.

---

## 5. The QBOUND / localization certificate

### 5.1 The localization ring
For a finite prime set `S`, `R_S = ℤ[S⁻¹] = {a/b ∈ ℚ (lowest terms) : every prime
of b lies in S}`. It is closed under `+, −, ×` but **not** inversion (inverting a
gap `a/b` turns numerator primes into denominator primes — this is why resolvents
enlarge `S`). The exponent-sensitive strengthening `den | QBOUND` catches an
impossible exponent (e.g. `2¹⁰⁰`) that prime-support membership misses, and uses
no fitted threshold. (Formalization credit: the `ℤ[S⁻¹]` / `den|QBOUND` framing
was sharpened by the external GPT theory audit; it is cleaner than the
max-prime "smoothness" screen it replaces.)

### 5.2 The mechanism, from the engine (DERIVED)
`corpus-import/.../ENGINE_STRING_su3_tension_sigma4.py::folded` computes each
resolvent denominator as `((L0−A)N² − B·N + C − L0)/(4N)` — a **quadratic in the
rank N**. At `N=3`, feeding `(a,b,c)=(−2,0,−1)` gives `17/12`, so the resolvent
factor `1/(E₀−E)` has denominator exactly `17 = 2N²−1`. A construction of
resolvent depth `d` therefore carries `17ᵈ`. The order-4 chain `W1→R1→W2→R2`
contributes `17¹` (W2) + `17²` (R2) = **`17³`**.

### 5.3 CORRECTION — one cubic order-4 scope, not two (17³, not 17²/17³)
An earlier draft of this analysis split the cubic order-4 sector into a
"marked-cluster" bound (`17²`, from a 2-resolvent sketch of the m₄-mass notebook)
and a "band-kernel" bound (`17³`), and claimed the second failed the first as
"scope discrimination". **That was an under-count.** The sealed shape coefficient
`A_SHP` and the off-axis `C_SHP` are siblings in one fourth-order shape kernel;
the honest `W1→R1→W2→R2` accounting gives a single `17³` bound they all divide.
The `17²` estimate would have wrongly rejected `C_SHP` (a legitimate coefficient
with `17³`). What survives is the **support** structure, not the 17-power split:
the bound's superset reaches `{…,47}` while the band/string coefficients occupy
the sub-support `{…,37}`. (This correction was forced by the external GPT exact
package, §5.5.)

### 5.4 Why the string sector stops at 37 (mechanism DERIVED, exact predicate OBSERVED)
The string tension sums only **connected (linked-cluster)** diagrams. The raw
connected denominator (`CERT_STRING_su3_tension_physical_o6_certificate.json`,
fourth order) is `2⁷·3⁶·5²·7·11·13·17³·19·29·31·37` — already **no 47, before any
subtraction**. So 47 is *never produced* by a linked diagram (not
produced-then-cancelled, as an earlier external suggestion framed it). Why it
isn't produced: 37 has a cheap 2-link/4-box carrier; 23/41/43/47 need heavier
excitation a connected four-plaquette diagram can't build. **Honest limit:** a
clean "≤2 links, ≤4 boxes" cap gives `{5,7,11,13,17,19,37}` — right ceiling but
drops `29,31` (which enter via a 6-box `(3,3)` state that IS connectedly
reachable). So the exact reachable set needs the walled-Brauer contraction module
(`y4_sun_walled_brauer_fixed_rank.py`), whose input is not in the repo.

### 5.5 The frozen exact QBOUND (external GPT package; independently verified)
The `WORKHOUSE_RANK3_ORDER4_CUBIC_EXACT_QBOUND` package supplied a hash-frozen,
Lean-verified, **non-circular** bound. Independently verified this session:

    QBOUND = 62895057857493885215590055852113920000000
           = 2³⁶·3²⁰·5⁷·7·11·13·17³·19·23·29·31·37·47
           = qW2 · qR2 · qHaar · qBilinear   (= QPAIR)
      qW2  = 881280                        = 2⁷·3⁴·5·17
      qR2  = 409824214482575692800         = 2¹⁰·3⁴·5²·7·11·13·17²·19·23·29·31·37·47
      qHaar= 87071293440000                = 2¹⁸·3¹²·5⁴
      qBilinear = 2 ;  qAnalytic = 896 = 2⁷·7
      17³  = 17^(1 W2 + 2 R2)

Machine-checked: `QPAIR = QTIGHT`; `lcm(896, QPAIR) = QTIGHT`; `896 | QTIGHT`;
`QTIGHT | QPATH` with quotient `2²⁰·3²⁵·7·11`. All **10 enforced targets divide**
QBOUND (sealed core, `Q_BAND_4`, `C_SHP_HISTORICAL`, `BETA_PEN_3`, `Q4_CROSS`,
true `LINKED_VACUUM_4`); the artifact is the **one quarantine** (support). The
generator never reads `constants.py` (non-circular); `−13/896` is derived by an
exact recurrence `[8/3, 1, −1/4, −1/16, −13/896]`, not a literal; the Lean cert is
clean (861 jobs, no `sorry`/`admit`, standard axioms `propext, Classical.choice,
Quot.sound` for the arithmetic core). History-ledger sha256
`543869b1…` verified.

**Honest trust boundary (stated by the package, agreed here):** this is an exact
*denominator* certificate, **not** the full scalar-coefficient certificate. It
does not contract the 117,161 endpoint-Haar topologies, produce `D_EXACT`, or
certify the fold/linked-vacuum numerators; the Haar divisor `2¹⁸·3¹²·5⁴` is a
conservative universal envelope; the small-prime exponents (`2³⁶·3²⁰·5⁷`) are
loose (actual coefficients reach `2¹⁰·3⁶·5²`). Identifying the frozen scope with
the physical perturbation expansion is a modeling premise outside the arithmetic.

### 5.6 The QBOUND's real teeth (calibration)
The gate rejects: (a) any prime ∉ `S₄`; (b) any of
`{7,11,13,17,19,23,29,31,37,47}` appearing to a power above its QBOUND exponent
(1, except 17 at 3); (c) `17^>3`. It does **not** constrain powers of 2, 3, 5
(exponents 36, 20, 7 are effectively unbounded). So the discriminating power is
concentrated in **support + the exponent-1 large primes + the 17³ cap** — real,
but not a tight bound.

---

## 6. Kernel-connected witness layer (added this session)

The base cert takes the stage LCMs `qW2`, `qR2` as **declared** integers. The
witness file `Rank3Order4QBoundWitnesses.lean` closes that for the denominator
layer:
- The frozen `W2_scaled` records have **58 distinct** denominators (LCM = `qW2`);
  `R2_scaled` have **181 distinct** (LCM = `qR2`); 199 in union, all `| qTight`
  (machine-checked; extracted from the hash-pinned ledger, hash re-verified).
- Lean proves (standard axioms): each frozen denominator `∣ qW2`/`qR2` (`decide`);
  `qW2, qR2 ∣ qTight` (explicit quotient witnesses); hence every frozen
  coefficient denominator `∣ qTight`; and a capstone
  `frozen_assembly_denominator_dvd_qTight` reusing the base
  `assembled_denominator_dvd_qTight`.
- Two `native_decide` theorems (adds `Lean.ofReduceBool`) prove `qW2`/`qR2` are
  the **exact** LCMs of the frozen denominators — deriving them from data.
- Delivered as a package with a reproducible extractor. **Not compiled here** (no
  Lean toolchain in-session); every `decide`/`native_decide`/`norm_num` goal was
  pre-verified in Python; needs external `lake build` (v4.34.0-rc1, Mathlib rev
  `1f29011071772620f612bf5a06433775f06067b8`).

---

## 7. Issues and errors discovered (consolidated)

### 7.1 In the original note ("Denominatorr Smoothness")
- **Census "56".** A line-based count that silently drops the sole multiline
  `Rational` call, `KPS_T6`. Correct: 60 scalar Rationals, **2** rough
  (`KPS_T6`, the artifact); among the program's own 57 internal constants the
  artifact is unique. `KPS_T6` (`P_max=61`) is an external order-6 transcription —
  the ladder continuing, not a violation.
- **"37 ceiling."** `37 = P_max(≤5)`; order 6 reaches 61; the superset reaches 47
  (§2.4); high rank reaches `O(N²)` (§4). The ceiling is rank-and-order-indexed.
- **"{31,37} occur only at fourth order."** False — both occur in `SIGMA_5`,
  `KPS_T5`, and remain in `KPS_T6`.
- **`33554467/33554393`.** Not a coefficient and not a float artifact: it is a
  slash-separated list of two CRT **moduli** near `2²⁵` (`SESSION_LOG.md`), read as
  a fraction by the generic scanner. A scanner false positive; semantic
  classification must precede arithmetic lint.

### 7.2 In the "tridecagon" message
Numerology, discarded: "13 primes = 13 vertices" is unmotivated; it silently
swaps the corpus's actual 13th prime **47 for 41** (41 is precisely the prime
*absent* at order ≤6); `ℚ(ζ₁₃)` cyclotomics are unrelated to the SU(3) band
kernel; and `2d² ≤ M` is a garbled CRT bound.

### 7.3 In the Gemini "string-tension scope" message
- "Band-kernel reaches 47" — **false**; band-kernel support is `{…,37}`, no 47/23.
- "Band-kernel 3-step vs string-tension 4-step" — **false**; `Q_BAND_4` and
  `SIGMA_4` have the identical denominator, both `17³` (same depth).
- `QBOUND_string` with `17⁴·…·23³` — over-built; the real coefficients have `17³`
  and no 23. The *observation* (string support truncates at 37) is correct; the
  depth arithmetic is not.

### 7.4 In the GPT packages (minor)
- **ADR misnumbered.** The exact-QBOUND ADR was labelled `0010`, which collides
  with the existing `docs/decisions/0010-external-tools-…`; the repo is already at
  ADR **0012**, so it should be **0013**.
- Small-prime exponents in the QBOUND are loose (conservative Haar envelope); the
  package states this.

### 7.5 In this analysis's own earlier draft
- The **17²/17³ two-scope split** (§5.3) was an under-count corrected by the GPT
  exact package. Recorded here rather than silently overwritten (per the "retract
  in the repository" discipline).

---

## 8. The C2 acceptance gate

C2 (the disputed off-axis coefficient `C_shp`; historical `−0.04808…` vs v10a.26
`−0.02021…`) is the corpus's one open contradiction. The denominator machinery's
**honest ceiling** for it is a necessary-condition acceptance gate on G3's
target-blind exact output, not a resolution.

- **Gate:** `support(den) ⊆ S₄` and `den | QBOUND`. Delivered as
  `c2_acceptance_gate.py` (returns the `(passed, detail)` shape the invariant
  suite expects) with an integration spec for
  `settlement/mce_adjudication_harness.py::stage_adjudicate` (as "item 12 —
  structural localization", complementing the current float-proximity verdict).
- **Validated:** accepts all 8 known exact cubic order-4 coefficients (incl. the
  exact historical `C_shp`); rejects the C20 artifact (alien prime 593076541), a
  float (firewalled), and hypothetical `7²`, alien `43`, `17⁴`. Independently
  reproduces C20.
- **What it adds:** catches a run that lands near an anchor yet emits an exact
  coefficient with an alien/rough denominator — float contamination or engine
  fault — which the numerical verdict is blind to.
- **What it cannot do (non-negotiable #2 respected):** it does not adjudicate C2.
  The historical value passes (exact, in-scope); the v10a.26 value is a float
  with no exact denominator to gate; `S₄`-smooth rationals are dense near any
  float (QBOUND permits `2³⁶·3²⁰·5⁷`), so the recorded numbers cannot be
  separated. Decisive use is **prospective**, on G3's exact output. It never
  prefers a side.

---

## 9. Honest limits and open problems

- The r≥4 `P_max` ceiling and the exact prime-gap/truncation predicates remain
  **OBSERVED/FITTED**, not derived. The decisive open computation: enumerate the
  order-7 Kogut-Susskind states and predict `KPS_T7`'s prime set before obtaining
  it (**no Hamiltonian `t₇` exists** — KPS 1981 published to `O(g⁻²⁴) = x⁶`; the
  order-12/14 series are *Euclidean*, a different quantity §12 forbids comparing).
  So a native order-7 σ (the corpus's own G7/G8 territory) is what would adjudicate
  "derived vs fitted".
- The exact QBOUND is a **denominator** certificate; the numerator/`D_EXACT` layer
  (117,161 endpoint-Haar topologies) is unbuilt and needs the missing
  walled-Brauer inputs.
- The scope↔physics identification is a modeling premise, not a machine result.
- The whole edifice is a **provenance** layer. It does not touch the load-bearing
  gaps (G17 free-energy stability, G18 spectral bridge, G19 continuum) or resolve
  C2. Beware accumulation over compression.

---

## 10. What to land in the repository (concrete)

Suggested, in order of value; each is a **write** (this session was read-only):

1. **FINDING checks** in `src/workhouse/invariants.py`:
   - the fourth-order arithmetic superset includes 47/23 (from the hardcoded
     `S4_PRIMES`), so 37 is not a fourth-order ceiling — assert the superset;
   - the artifact `LINKED_VACUUM_4_ARTIFACT` leaves the cubic o4 localization
     (support `{593076541}`), while its intended value stays inside — a
     denominator-localization FINDING complementing the C20 near-miss.
2. **C2 acceptance gate** as a registered check + a one-line note on the G3 gap in
   `ledger/gaps.yaml` ("G3 output must satisfy the cubic o4 localization").
3. **Ledger candidate U4** (`unifying_candidates`, with a falsifier): "a primitive
   perturbative coefficient's reduced denominator lies in the scope's
   `ℤ[S⁻¹]` localization and divides its `QBOUND`; a Rational violating it,
   absent a ratio-of-coefficients origin, is a float reconstruction." Falsifier:
   a coefficient re-derived exactly whose denominator exceeds the scope's QBOUND
   and is neither a rank-polynomial factor nor another coefficient's numerator;
   or a proven float artifact reconstructing to an in-localization denominator.
4. **ADR** recording the two-scope→one-scope correction (§5.3) and the derived
   `17 = 2N²−1` / `17^depth` mechanism — renumbered **0013** (0010–0012 are taken).
5. The **Lean** additions: the frozen QBOUND cert + the witness layer (§5.5, §6),
   as a new `lean/Workhouse/` module, once `lake build` is run externally.

---

## 11. The exact-Haar package and the necessary-not-sufficient capstone

An external package (`WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_CERTIFICATE`) built
the numerator layer that all prior packages bracketed: an exact endpoint-SU(3)
Haar contraction of the frozen 117,161-key W2/R2 history, losslessly aggregated
to 69,800 unordered classes, via integer-scaled projectors + signed CRT (no float
reconstruction). Machine-verified internal arithmetic:

    D_EXACT  = −13/896 + ½·Σ_T w_T H_T = −361008126292641364183/7250590288602460800
    m_4,rest = D_EXACT + FOLD − V_link  = −160506019419340168451/14501180577204921600
      FOLD   = 5315003/140454 (already exact in corpus; v10a18 FOLD_A)
      V_link = −1474623/1675520 (= LINKED_VACUUM_4)
    den(D_EXACT) | QBOUND ✓ ;  den(m_4,rest) | QBOUND ✓ ;  TOTAL_NUM/QBOUND = D_EXACT ✓

### 11.1 The result is the quarantined value (machine-checked)
`m_4,rest = QUARANTINED_SCALAR`, verbatim. The corpus records this exact value as
contradiction **C1**'s "**quarantined shortcut**", status `rejected-by-both`, and
`constants.py` carries the note *"Rejected by both sides; recorded so it is never
silently resurrected."* `settlement/mce_adjudication_harness.py` runs a
contamination scan to ensure engine source is **free of this exact constant**.
The package presents `m_4,rest` as "the requested final combination" and does not
flag any of this.

### 11.2 Capstone: the certificate stack is NECESSARY, not SUFFICIENT
This is the cleanest demonstration in the whole investigation. The quarantined
shortcut **passes every arithmetic gate**: `den | QBOUND` ✓, the C2 localization
gate ✓ (support `{2,3,5,7,11,13,17,19,29,31,37}`), an exact hash-frozen
independently-cross-checked Lean-adjacent derivation ✓ — **and it is a value
rejected on physics/construction grounds.** No amount of denominator/QBOUND/Lean
certification catches a by-construction physics artifact. Two independent routes
agreeing exactly does not rescue it — both reproduce the same value. **Denominator
localization is provenance, not physics.**

### 11.3 Forensic resolution — oracle-free, but the wrong quantity (machine-checked)
The sharp question was whether the package's `m_4,rest` (a) silently carries the
oracle-forcing `local_shift = M4_ORACLE − ax_rest`, or (b) is an independent
result that would rehabilitate the quarantine. Neither. The pipeline is provably
**oracle-free** (no `oracle`/`M4_ORACLE`/`ax_rest`/`local_shift`/`m_gamma` in the
contractor or generator; the only "diagonal" is tensor-index extraction, the only
"shift" is lattice geometry; assembly is `d_exact + FOLD − LINKED`). The exact
decomposition:

    ax_rest = D_EXACT + FOLD = −86634244910174898583/7250590288602460800 = −11.9485781794014
    m_4,rest = ax_rest − V_link = −11.0684794637788   (= QUARANTINED_SCALAR)

`ax_rest` is the **raw, un-anchored axial rest**. The C1 dispute is the
**anchoring step** `local_shift = M4_ORACLE − ax_rest`, which the package does
**not** perform (checked: `M4_ORACLE − ax_rest = 11.17343231638… =
RUN15_APPLIED_SHIFT`; `ax_rest + local_shift = oracle`, C22's gate-85). So:
- the package's arithmetic and non-circularity are **exonerated** — it honestly
  computes the raw rest;
- the **quarantine is upheld for the right reason** — the raw rest is *nobody's*
  physical answer (each side anchors differently); it is a pre-anchoring
  intermediate, correctly rejected as not-a-prediction;
- the package **does not bear on C1/C2** — it computed the *input* to the
  anchoring, not the anchoring (which is G3). C1 is in any case dissolved
  (ADR 0002) as an anchoring distinction; the open item remains C2.

### 11.4 Byproduct: a candidate float→exact upgrade
The package yields an **exact rational for the raw folded axial value**,
`ax_rest = −86634244910174898583/7250590288602460800`, matching the corpus float
`RAW_FOLDED_AXIAL_GAMMA_NUM = −11.9485781794007` to its printed precision. It is
CRT-derived (not float-reconstructed) and **passes the localization gate**
(denominator = `SIGMA_4`'s, in-scope). Per repo discipline a precision match is
not proof (cf. C20), but this one is an exact computation that clears the screen,
so it is a well-supported candidate exact form of a previously-float RUN15-lineage
intermediate. It is the exact form of a *disputed-lineage* quantity — record it as
such, not as a physical promotion.

---

## 12. The fourth-order axial Γ scalar: exact arithmetic + one physics input

With the package's exact `ax_rest` (§11.4), the whole arithmetic layer of the
fourth-order axial Γ-point scalar is exact and passes the cubic-o4 localization
gate. All values machine-checked this session.

| quantity | exact value | note |
|---|---|---|
| `Σ_T w_T H_T` | `−805586892848311021/8092176661386675` | Haar sum |
| `D_EXACT` | `−361008126292641364183/7250590288602460800` | direct scalar |
| `FOLD` | `5315003/140454` | already exact (v10a18 `FOLD_A`) |
| `V_link` | `−1474623/1675520` | `LINKED_VACUUM_4` |
| **`ax_rest = D_EXACT + FOLD`** | `−86634244910174898583/7250590288602460800` | **NEW exact; was float-only** |
| `q_band^(4)` | `−20721577909065127111/7250590288602460800` | band-kernel anchor (exact) |

**The single irreducible physics input** is `m_Γ^(4) = −0.7751458630189173` (the
Hamer-validated oracle) — the only float that cannot be made exact.

### 12.1 New exact fact (T1) — the anchor gap
The two *independent* fourth-order axial anchors differ by an exact, low-height,
gate-passing rational:

    ax_rest − q_band^(4) = −2179000819 / 239696600
      denominator = 2³·5²·11·13·17²·29  (max prime 29, in S₄, | QBOUND)
      numerator   = 31·53·151·8783

The shared 19-digit denominator `7250590288602460800` mostly cancels (common
factor `30249032688`), so the raw axial rest and the band anchor sit a *simple*
exact shift apart — the exact form of C1's "differently-anchored coordinates"
(ADR 0002).

### 12.2 The anchoring shortcut, written exactly
`F_anchor = oracle − ax_rest = 11.17343… = RUN15_APPLIED_SHIFT`, and
`ax_rest + F_anchor = oracle` — the by-construction equality (C22 gate-85), now
transparent because `ax_rest` is exact.

### 12.3 G3 specification (what the open computation must produce)
`m_Γ^(4) = ax_rest(EXACT) + F_anchor`. The shortcut *sets*
`F_anchor := oracle − ax_rest`, forcing the answer. G3 must derive `F_anchor`
**target-blind** (an independent vacuum-subtraction constant) and then test
whether `ax_rest + F_anchor` reproduces the oracle *without being set to it*. The
exact `ax_rest` is a clean, gate-passing input.

### 12.4 Terminus
This exhausts the arithmetic layer: every computable-by-arithmetic quantity in
the fourth-order axial scalar is now exact and gate-verified; the residue is
exactly one physics quantity (`F_anchor`, equivalently the oracle), which is
**G3** — a marked-cluster engine run, not a certificate. The apparatus of this
whole investigation (smoothness, localization, QBOUND, Lean witnesses, the exact
Haar sum) cannot supply that last input; §11.2's capstone proved it. The two
honest continuations are **land the record** (§10) or **run G3** (physics).

---

## Appendix — reproduction pointers

- Ladder / sector supports: factor `KPS_T*`, `SIGMA_*`, band constants in
  `src/workhouse/constants.py` with `sympy.factorint`.
- Corpus census: `workhouse.corpus_registry.combined_table()`, factor denominators.
- 47/23 superset: `NB_O4_hodge_v10a18_arithmetic_geometry_prime_provenance.ipynb`
  cell 1 (`ARITH_PRIMES`); `S4_PRIMES` literal in the `v10a20b` notebook.
- 41 deferral: `ΣC ≡ 16 (mod p)` reachability over `C(p,q)=p²+pq+q²+3p+3q`.
- QBOUND / mechanism: `folded` in `ENGINE_STRING_su3_tension_sigma4.py`;
  `Rank3Order4QBoundCertificate.lean` (`qTight`), history ledger sha256
  `543869b10f5137ea74fbd5f27d25027dea66f936ce9844b77a029453b8bf8c97`.
- C2 gate: `c2_acceptance_gate.py` (validated against `constants.py`).

*End of record.*
