# WORKHOUSE denominator-localization theory audit

**Date:** 2026-08-23  
**Repository snapshot:** `4f5f02c6ddba06c4ab84f393e0c3548591865d65`  
**Mode:** read-only repository audit; no repository files changed

## Executive verdict

The note has found a real and valuable organizing principle, but it states it too broadly.

The sound statement is **sector-, rank-, normalization-, and order-specific denominator localization**:

> Once every denominator-producing primitive in a fixed perturbative construction has been enumerated—including Haar/projector factors, all rational energy gaps that are inverted, fold/linked normalizations, and rational basis changes—every exactly assembled coefficient belongs to a computable localization `Z[S⁻¹]`. With exponent information, its reduced denominator divides a computable integer `Q`.

That is a genuine conservation law. The stronger proposed statement—“the SU(3) construction is 37-smooth, and a rough denominator is nearly proof of a disguised float”—is false.

The two most decisive findings are:

1. The repository's own fourth-order gap census permits primes **23 and 47**. Exact examples are
   `8/3 - 13/2 = -23/6`, giving resolvent `-6/23`, and
   `8/3 - 21/2 = -47/6`, giving resolvent `-6/47`.
   The actual fourth-order arithmetic superset in the denominator-lift notebook is
   `{2,3,5,7,11,13,17,19,23,29,31,37,47}`, not a ceiling of 37.

2. The apparent `55/56` result comes from a line-oriented extraction error. `constants.py` contains 57 direct uppercase `Rational(...)` assignments; the sole multiline call is `KPS_T6`, and it is the second non-37-smooth value. Runtime evaluation finds 60 uppercase rational scalars: 58 smooth and 2 rough.

The right next step is therefore not to discard denominator smoothness. It is to promote it from a fitted global heuristic into a **typed, derivation-scoped denominator-divisibility certificate**.

## What survives and what does not

| Claim | Verdict | Exact qualification |
|---|---|---|
| Denominators encode derivational structure | **Yes** | Only after the model, rank, sector, perturbative order, basis, and normalization are fixed. |
| Denominator support survives addition and subtraction | **Yes** | If inputs lie in `Z[S⁻¹]`, sums and differences do too. Multiplication is also closed. |
| The same support tracks arbitrary “field arithmetic” | **No** | Arbitrary inversion destroys the restriction; the fraction field of `Z[S⁻¹]` is all of `Q`. |
| Numerator primes specifically detect multiplication | **No** | Addition already creates new numerator primes: `1/2 + 1/3 = 5/6`. |
| SU(3) fourth order has a proven maximum prime 37 | **No** | The exact gap census permits 47. The selected final coefficient happens not to retain it. |
| The observed tier supports form a theorem-level monotone ladder | **No** | Reduced supports can shrink by cancellation. Only a cumulatively defined allowed envelope can be monotone by construction. |
| The linked-vacuum artifact is a strong smoothness violation | **Yes** | Its denominator is the prime `593076541`, outside every relevant declared localization. |
| A rough denominator is nearly proof of a float | **No** | `KPS_T6`, SU(4)/SU(5) coefficients, and legitimate ratios are counterexamples. |
| The current float-type test misses a `Rational` reconstructed from a float | **Yes** | `tests/test_constants.py:59-87` checks Python `float` objects, not the provenance of a `Rational`. |
| Corpus-wide roughness gives a useful triage list | **Only after semantic filtering** | The raw regex also reads slash-separated primes and generated/truncated index text as fractions. |

## The exact mathematical core

For a finite set of primes `S`, define

`R_S = Z[S⁻¹] = {a/b in Q in lowest terms : every prime dividing b lies in S}`.

Then:

- `R_S` is closed under addition, subtraction, and multiplication;
- cancellation can only remove denominator primes;
- `R_S` is not closed under inversion of an arbitrary nonzero element.

The last point is load-bearing. If `x = a/b`, then `x⁻¹ = b/a`, so primes from the **numerator** of a rational gap become denominator primes in a resolvent. A small example is

`x = 1/2 - 1/37 = 35/74`, while `x⁻¹ = 74/35`, which introduces denominator primes 5 and 7.

This is exactly what happens in the WORKHOUSE fourth-order census. `hopping(3)=5/612` has denominator support `{2,3,17}`; the 5 is initially a numerator prime. Separate energy gaps later have numerators 23 and 47, and their inverses introduce those primes into the allowed denominator palette.

The clean perturbative form is

```text
H_eff^(r)[a,b]
  = sum over legal ordered histories h:a→b
      multiplicity(h)
    × Haar/projector weight(h)
    × product over cuts j of (-1 / gap(h,j))
    × fold/linked normalization(h).
```

For fixed rank `N`, order `r`, retained sector, basis, and SW/BCH convention, enumerate every rational factor on the right. Let `S_r` be the union of their denominator-prime supports after every required inverse has been taken. Then every entry lies in `Z[S_r⁻¹]`.

The stronger form records prime exponents. If `Q_r` is a common multiple of every legal term denominator, then

`denominator(H_eff^(r)[a,b]) | Q_r`.

This divisor statement is materially stronger than prime support: it also detects an impossible exponent such as an unexpected `2^100` while using no fitted maximum-prime threshold.

## The repository already contains the stronger mechanism

### 1. Lean proves only the rational identity layer

`lean/Workhouse/Basic.lean:1-15` explicitly limits its scope to rational and polynomial identities, not perturbative derivations or operator theory. It defines the hopping function and proves `hopping 3 = 5/612` at lines 29-41. It does **not** prove an exhaustive denominator-prime palette.

### 2. The arithmetic-provenance notebook enumerates inverse sources

`corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a18_arithmetic_geometry_prime_provenance.ipynb`, cell 2:

- lines 269-275 define exact SU(3) link energies;
- lines 293-363 enumerate projector splittings and first-/second-step reduced-resolvent gaps;
- lines 372-376 form an arithmetic-prime **superset** before physical cancellations.

A clean read-only reproduction produces the exact gap witnesses `-23/6` and `-47/6` above. The downstream notebook
`NB_O4_hodge_v10a20b_denominatorlift_exact_da_m4_a100.ipynb`, cell 2 line 6195, hardcodes

`S4_PRIMES={2,3,5,7,11,13,17,19,23,29,31,37,47}`.

Lines 6208-6218 then require inferred rational coefficients to remain inside that set. Consequently, a correct intermediate `1/47` is allowed. Its absence from the displayed final fourth-order coefficient is a cancellation or target-selection fact, not a universal ceiling.

### 3. The denominator-lift path builds `QBOUND`

`corpus-import/records/audits/07-denominator-lift.md:31-38` describes the intended chain:

- construct exact support-resolved histories;
- regenerate exact reduced resolvents;
- collapse exact state-pair orbits;
- form the prime-exponent LCM `QBOUND` from all term denominators and Haar/projector bounds;
- lift each Haar topology to an integer numerator;
- assemble the final exact coefficient.

That is the natural home of the denominator theorem. However, the same audit records that the notebooks are unexecuted in the repository, no immutable completed ledger is stored, some history coefficients originate as floats and are recovered with `limit_denominator`, and the recovery notebook depends on live kernel state (`07-denominator-lift.md:51-78`). This is a promising executable candidate, not yet a sealed certificate.

### 4. CRT is the natural independent backend

Once `Q_r` is known, compute the integer `Q_r H_eff^(r)` modulo primes not dividing `Q_r`. If the combined modulus exceeds twice a proven numerator-height bound, CRT/rational reconstruction is unique. WORKHOUSE already uses this pattern for a seven-prime string-tension reconstruction (`src/workhouse/invariants.py:1032-1045`).

This suggests a clean separation:

```text
exact model manifest
    → exactly-once history ledger
    → exact primitive-factor witnesses
    → S_r and Q_r certificate
    → integer/modular accumulation
    → reconstructed coefficient + independent checker
```

Prime support is the cheap early alarm. `denominator | Q_r` is the real arithmetic certificate. Exact/modular recomputation and coverage are what certify the coefficient.

## Reproduced census on the current snapshot

### `constants.py`

| Census | Total | 37-smooth | Not 37-smooth |
|---|---:|---:|---:|
| Direct uppercase `Rational(...)` assignments found structurally | 57 | 55 | 2 |
| Runtime uppercase scalar rational values | 60 | 58 | 2 |

The two non-37-smooth values are:

- `LINKED_VACUUM_4_ARTIFACT = -521965902/593076541` (`constants.py:429-432`);
- multiline `KPS_T6` (`constants.py:288-291`), whose denominator contains 43, 47, 53, 59, and 61 in addition to smaller primes.

`KPS_T6` is described as an exact rational printed in the historical source, although its transcription still awaits native verification (`constants.py:266-282`). It is therefore a direct counterexample to “rough means float,” not proof that the KPS transcription is correct.

Why the note found 56 is unusually clear: `KPS_T6` is the **only multiline** direct uppercase `Rational` call. A line-based count sees 56 and silently drops precisely the second rough value.

Also, the actual curated `REGISTRY` at `constants.py:576-666` is a separate 11-entry typed registry. “The curated table of 56” does not name a reproducible repository object; a frozen manifest is required.

### Bulk corpus index

| Population | Current reproduction | Pasted note |
|---|---:|---:|
| Distinct mechanically extracted rationals | 1,443 | 1,438 |
| Rough denominators (`prime > 37`) | 246 | 247 |
| `q > 10^6`: rough / smooth | 31 / 125 | 31 / 126 |
| `q > 10^9`: rough / smooth | 23 / 90 | 23 / 90 |

The exact `23/90` headline reproduces, but its proposed interpretation does not:

- 17 of the 23 rough values occur only in the generated `DOC_FLUX_constants_index.md`; they are self-indexed/truncated pseudo-rationals;
- four are genuine exact SU(4)/SU(5) coefficients;
- two are explicitly `radius_squared` ratios, which can legitimately inherit coefficient numerator primes in their denominators.

Excluding values found only in the generated prose index gives 1,421 total / 229 rough. Above `10^9`, only 6 rough / 88 smooth remain.

The repeated rough parts also have structural explanations. For example,

- `185791 = 47·59·67` occurs in SU(4) band/determinant material;
- `346531 = 47·73·101` occurs in the same all-rank/SU(4) family, with one additional generated-index echo;
- the repeated denominator `8815920161561` belongs to SU(6) band coefficients.

Repetition can indicate shared derivational lineage just as readily as shared corruption.

## The slash-list false positive

`33554467/33554393` is not a rational coefficient and not a float artifact.

Its source is `corpus-import/records/SESSION_LOG.md:103`, which lists three independent finite-field moduli:

`33554467 / 33554393 / 33554383`.

They were deliberately chosen near `2^25` for a modular sigma-4 check. The generic slash regex at `src/workhouse/corpus_index.py:49-53` reads the first adjacent pair as a fraction; the generated constants index repeats that false interpretation at `DOC_FLUX_constants_index.md:184`.

This example is especially instructive: denominator arithmetic cannot repair a semantic extraction error. The scanner itself declares its output T3, mechanically extracted, and untrusted (`src/workhouse/corpus_registry.py:1-12`). A smoothness triage must not promote regex matches into coefficients before classifying their role.

## The observed support ladder

The three selected unions do factor as stated:

- selected second/third-order values: `{2,3,5,17}`;
- selected pentagonal values: `{2,3,5,7,11,13,17,19,29}`;
- selected displayed cubic-fourth values: `{2,3,5,7,11,13,17,19,29,31,37}`.

This is useful provenance information, but not a theorem of monotone depth.

- The pentagonal calculation is a separate geometry from the cubic kernel; the repository explicitly firewalls them (`src/workhouse/constants.py:441-442`, and the invariant at `src/workhouse/invariants.py:974-982`).
- Cancellation can make the reduced support at a later order smaller.
- “31 and 37 occur only at fourth order” is literally false: both occur in fifth-order `SIGMA_5` and `KPS_T5`, and remain in `KPS_T6`.
- A defensible statement is: “31 and 37 first appear in this explicitly listed coefficient sequence.”
- A genuinely monotone object is the cumulative **allowed-source envelope** `S_≤r = union_{j≤r} S_j`, not the support of each final reduced coefficient.

## Dickman smoothness: useful intuition, not a calibrated probability

The quoted scale is broadly reasonable, but the statistical conclusion is too strong.

Independent Dickman-function values are approximately:

| `u = log(q)/log(37)` | `rho(u)` |
|---:|---:|
| 3.4418 | `1.8535e-2` |
| 5.5944 | `6.5379e-5` |
| 6.9674 | `9.7096e-7` |
| 12.0268 | `1.2550e-14` |

But Dickman asymptotics model uniformly sampled integers in an asymptotic regime. Continued-fraction outputs from `limit_denominator`, published exact coefficients, ratios, and representation-theoretic denominators are highly nonuniform. The cutoff 37 was also selected after inspecting this corpus. These numbers are therefore prioritization heuristics, not false-positive probabilities and certainly not proofs.

For comparison, exact finite smooth-number enumeration gives a density near `5.04e-4` at `q=593076541`, almost an order of magnitude above the Dickman approximation. The artifact remains highly conspicuous; the probability rhetoric is simply not calibrated to this data-generating process.

## A reliable implementation architecture

### A. Define a typed coefficient manifest

Every audited rational should carry:

- symbolic name;
- value;
- rank and lattice volume;
- perturbative order;
- sector/parity/geometry;
- basis and normalization;
- role: `primitive`, `derived-linear`, `ratio`, `published-target`, `modulus`, `quarantined`, or `artifact`;
- derivation/certificate hash;
- allowed prime set `S` and preferably denominator bound `Q`;
- provenance tier.

Do not infer this cohort from uppercase names or source-line regexes.

### B. Separate semantic extraction from arithmetic lint

1. Use Python's AST for `Rational`, `Fraction`, and exact expressions in code.
2. Exclude generated indexes from their own input set.
3. Reject or explicitly classify slash chains such as `p1/p2/p3`.
4. Treat prose regex matches as untrusted occurrences until tied to a typed manifest entry.
5. Preserve the original source line and semantic role in every finding.

### C. Use three levels of arithmetic checking

1. **Prime-support lint:** `support(denominator) ⊆ S`.
2. **Divisor certificate:** `denominator | Q`.
3. **Exact reconstruction:** integer accumulation after multiplying by `Q`, or modular accumulation plus a uniqueness bound.

Level 1 is a cheap negative screen. It cannot prove a coefficient. Level 2 catches forbidden exponents. Level 3 proves the arithmetic result, conditional on complete history coverage and correct primitive witnesses.

### D. Replace heuristic float exactification with an interval witness

Two `limit_denominator` ceilings agreeing is strong evidence but not proof. If a divisor bound `Q` is known, enclose the numerical value in a certified interval `I` and prove that `Q·I` contains exactly one integer. Then the recovered rational is unique relative to the bound.

Alternatively generate the representation/Haar coefficients symbolically from the start.

### E. Make the history certificate checkable

The immutable artifact should contain:

1. the model and convention manifest;
2. the canonical history DAG, including every temporal prefix;
3. an exactly-once coverage certificate;
4. exact irrep, Casimir/gap, Haar/projector, center-flux, and support witnesses;
5. orbit representatives and multiplicities;
6. the constructed `S` and prime-exponent `Q`;
7. every term denominator and proof it divides `Q`;
8. the integer or modular accumulator;
9. reconstruction bounds and held-out modular checks;
10. hashes for every parent and output.

Temporal history matters: two configurations with the same final spatial support can traverse different intermediate irreps and therefore different resolvent denominators. The current history object records order and intermediate lengths (`src/workhouse/cellular.py:247-302`), which is the right direction.

## What Lean should prove

Lean is well suited to the small checker, not the giant ledger.

Useful generic theorems are:

- closure of `Z[S⁻¹]` under the permitted operations;
- the precise unit condition for safe division;
- denominator-divisibility of a finite history sum from term-wise divisor witnesses;
- correctness of prime-exponent LCM construction;
- CRT/rational-reconstruction uniqueness under a height bound;
- exact Gram/projector identities;
- soundness of the reflected history-certificate checker;
- the finite-order SW/BCH algebra used by the assembly.

The large history ledger should remain external data with hashes and compact certificates. `Basic.lean` correctly says that the current formalization proves only rational/polynomial identities, not the perturbative enumeration.

## Physics interpretation and firewall

Denominator localization can certify arithmetic lineage inside a fixed perturbative model. It cannot by itself establish:

- completeness of the history enumeration;
- correctness of multiplicities or numerator signs;
- convergence or a controlled perturbative remainder;
- a thermodynamic or continuum limit;
- reflection positivity or OS reconstruction;
- a Källén-Lehmann atom or nonzero continuum residue;
- full-sector isolation, stability, or continuum spin.

Nor is every denominator pole a physical singularity: it may mark a chosen basis becoming singular or a representation/projector degeneracy at a special rank.

Prime support is therefore a **strong negative invariant and weak positive invariant**. An alien prime relative to a proved manifest is decisive evidence that something left the declared derivation. Expected support does not prove that the derivation was complete or correct.

## Recommended decision

Keep the insight, but rename and rescope it:

> **Finite-order denominator-localization and divisor certificate.** For a fixed, explicitly manifested WORKHOUSE perturbative problem, enumerate all inverse-producing primitives, derive `S` and `Q`, and require every exact term and final coefficient to satisfy the corresponding localization/divisibility witnesses.

Immediate implementation priorities:

1. Freeze a semantic manifest for the exact cohort being audited.
2. Fix the scanner's slash-chain and self-indexing failures.
3. Add the sole multiline `KPS_T6` regression.
4. Replace global `37-smooth` with per-rank/order/sector `S` membership.
5. Prefer `denominator | QBOUND` over support-only checks.
6. Serialize one clean denominator-lift run with its complete ledger and hashes.
7. Add a compact Lean-checked certificate verifier.

This turns the original observation from an overfitted forensic rule into a rigorous and reusable part of the WORKHOUSE proof architecture.

## Read-only assurance

The repository at the stated commit remained clean. All reproduction work was performed outside the repository worktree.
