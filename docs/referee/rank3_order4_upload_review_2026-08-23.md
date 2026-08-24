# Referee report: the rank-3 / order-4 F07-vs-blind upload

**Date:** 2026-08-24. **Scope:** five artifacts delivered 2026-08-23 —
four prose records (master record `A`, two-face adjudication `B`, W2/R2 lineage
trace `C`, F07-vs-blind structural trace `D`) and one certificate zip
(`E`, `WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_CERTIFICATE_20260823.zip`).
**Mode:** read-only audit against this repository. Nothing was promoted, no
tolerance widened, no `theory/` file touched. The upload itself is not checked
in; this document is the record of what it says and what survives checking.

Every number below was recomputed here in `fractions.Fraction`/`sympy`, and
every corpus citation was opened at the line cited.

---

## 0. Verdict

The upload's **arithmetic spine is sound** and several of its citations are
better than the repository's own constants. Its **central mechanism is
refuted**: the named suspect for the F07-vs-blind split — `W22` contamination
of a finite-`u` degree-6 fit — is not a property of the numbers the documents
target, and the experiment they propose to test it is provably null at order
four. Its **localization** (the whole gap lives at size ≥ 2) is arithmetically
right but rests on an exact cancellation no document states, and its
**one-face agreement is not new** — it is a presently-executable corpus
certificate the documents do not cite.

Three things the upload found that the repository should keep:

| | |
|---|---|
| `RAW_FOLDED_AXIAL_GAMMA_NUM` is 381 ulps stale | the upload's `B:36` is right and `constants.py:428` is wrong |
| the F07 branch value is exactly reproducible from a target-free route | `E` verifies it end to end; the register's `record-backed` is stale |
| the certificate cannot be replayed from what was shipped | `ledger_generator.py` is absent; 5 of 7 modules fail to import |

And one thing the upload should not do: file the dispute under **C2**.

---

## 1. What checks out

Re-derived exactly here, all confirming the documents:

```
-13/896 + 39/1280            = 143/8960          143 = 11·13, 8960 = 2⁸·5·7
e4(C) − 2·V1                 = -327/83776        e4(C) = -54321/837760, V1 = -39/1280
1675520 = 1280·1309 = 83776·20                   1309 = 7·11·17
D_EXACT + FOLD − V_link      = -160506019419340168451/14501180577204921600
                             = QUARANTINED_SCALAR  (constants.py:427), bit-identical
|M4_ORACLE − M4_SHORTCUT|    = 10.293333600759848  (0 ulps; printed at 15 hour RUN.txt:10633)
14501180577204921600         = 2 · 7250590288602460800
```

`C §6`'s SHA-256 for `ENGINE_O4_hodge_v10a7_marked_linked_scalar.py`
(`dc9ddfaa…`) reproduces byte-for-byte here, as do all three provenance
digests `C §3` pins (`68782826…`, `47c6ccc1…`, `7332bf83…`) against
`DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py`, the v10a.20b notebook and
`records/audits/07-denominator-lift.md`.

`C §7`'s dataflow claim is the strongest verified point in the set and it holds
in this repository's own copy of the notebook: `D_EXACT` is constructed at
cell-1 line 6668 and gated at 6669–6672, and the prior float target
`D_PREV = -49.7901704444838` appears only afterwards at 6674. The exact
accumulation precedes the comparison.

`B §3`'s face decomposition of the linked vacuum is not only true but uniquely
determined, which `B` does not say: `13·(-39/1280) + 124·(-327/83776) =
-1474623/1675520` exactly, and `(13, 124)` is the **only** non-negative integer
solution (the solution lattice steps by `(+2180, −17017)`).

The v10a.21r circularity trap is real and correctly quoted. Four of the five
retraction lines are verbatim at `Monday 531 PM.txt:1978, 2287, 2548, 3702`.
No execution of v10a.21 or v10a.21r exists anywhere in this repository — both
notebooks have `execution_count: null` and zero outputs — so the guard is
sound and, additionally, `B §4`'s claim that v10a.21r "**does** yield" a
size-1 weight of `143/8960` is itself a T3 statement about unrun code.

**On terminology, the upload is clear.** The `m_4` rule is pair-scoped —
`contradictions.yaml:22` forbids *"two `m_4` values"* for `q_band^(4)` +
`m_Γ^(4)` specifically — and `D:27` explicitly disclaims that pairing. Writing
`m_{4,F07}` / `m_{4,blind}` is not the forbidden collision.

---

## 2. The refuted mechanism

`A §3` names the suspect: "the blind branch admits W22 and extracts O4 by a
finite-`u` degree-6 fit"; `A §4` makes "Knob B — blind two-face O4 recomputed
**W22-off**" the discriminator "between *fit artifact* and *real physics*".
`B §5(2)` and `D:91` carry the same requirement.

**The degree-6 fit did not produce the numbers they target.** Every blind value
in the upload is cited to `corpus-import/records/transcripts/15 hour RUN.txt`
around `:10620-10626`. That file is the **v10a.26** run
(banner at `:3`), not v10a.24c. In it, `_v23c_fit_cluster` is redefined at
`:7230` and takes its production coefficients from `_v26_sw_blocks(one,4)` at
`:7232` — an order-truncated Hermitian SW/BCH recursion returning
`'method':'canonical Hermitian SW/BCH through O(u^4)'` at `:7246`. The 13-point
degree-6 fit survives only as `_v26_legacy_fit_models`, docstring
*"Audit only: reproduce the retired 13-point fit"* (`:7220`). The run prints
this three times, including on the line immediately above the table the
documents quote:

```
:10614  [PASS] v10a.26 exact SW block diagonalization closes through O(u^4) :: max P-Q residual=5.551e-16
:10617  production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window
:10619  [16] ROOTED INCIDENCE TRANSFORM — INDEPENDENT RAW CLUSTERS
```

`-0.403971702978` occurs in exactly two places in the corpus, both v10a.26
(`15 hour RUN.txt:10621` and its results twin). The v10a.24c production run
died on `KeyboardInterrupt` and emitted no `[16]` block at all. The documents'
description of the *v10a.24c source file* is accurate (`DEG='6'` at `:6793`,
`N='13'` at `:6794`, dense `W` with no layer mask at `:6894-6899`); the error
is the "therefore".

**Knob B is a null experiment.** Two independent checks:

- *Walk count.* There are exactly 9 closed four-step Motzkin walks
  `P → P` on the Krylov layer index; none contains a `(Q2,Q2)` step, and the
  unique five-step one that does is `(P,Q1,Q2,Q2,Q1,P)`. Re-enumerated here.
- *The recursion itself.* Transcribing `_v26_poly_mul`/`_v26_poly_comm`/
  `_v26_bch`/`_v26_sw_blocks` into exact rationals and running random layered
  Hermitian models with `W[P,Q2]=0`, the effective `P`-block at orders
  0–4 is **exactly equal** with `W22` present and with `W22` zeroed, and first
  differs at order 5.

So a W22-off recomputation returns the same number, identically. Even
counterfactually the fit could not carry the gap: the run's own preflight
measures exact-SW against the retired fit at `max coefficient difference =
2.267e-07` (`:9190`), against a branch gap of `10.293…` — a factor of 4.5·10⁷.

**Correction to `A:88-92`.** "The corpus proves W22 is O4-null **only at one
face**" inverts the evidence. The gate at
`DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:609-610`
("W22 first enters a closed walk at order five") is a statement about the layer
graph and carries **no face count**; the file's own docstring line 13 states it
unqualified. What *is* one-face-only is the exact-Fraction regression at
`:317-338`, gated at `:614/:615/:616` (`o4_equal`, `-13/896`,
`o5_difference = -5/7168`) — reproduced here. The real asymmetry is
premise-freeness, not face count: the walk gate assumes `W` is layer-tridiagonal
in the Krylov index and that the `O(u⁴)` coefficient is the sum over 4-step
closed walks, and neither premise is machine-checked in this repository at any
face count.

**Also refuted:** `A:59` and `A:88-89` call W22 "the branches' only structural
difference". `A`'s own cited source says "earliest", not only (`D:83`), and
`B:157-175` lists W22 as item 2 of 5 independent requirements.

---

## 3. The localization: right conclusion, unstated premise

`A §3` and `B §0` conclude that the whole `10.293…` gap lives at size ≥ 2,
from the one-face agreement. Two problems, neither fatal.

**The fold is never decomposed.** The F07 total is `D_EXACT + FOLD − V_link`.
`A`, `B` and `D` decompose `D` and `V_link` by face count and never give `FOLD`
a value or a face profile — only `C:224` prints it. It is
`5315003/140454 = +37.8415922650832`, i.e. **3.68× the entire branch gap**
being localized. Under the corpus's only face convention for it (the set-union
convolution at `v10a21r:122-127`, applied at `:331-333`) it assigns weight to
the singleton support, so "F07's one-face contribution = `143/8960`" is not
self-evidently the F07 branch's one-face contribution.

It is nevertheless **exactly zero at one face**, and that is why the
localization survives. From the corpus's own gated isolated one-face model
(`DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:317-338`, `h0 = (8/3, 20/3,
12, 32/3)`), the reduced-resolvent moments are `e2 = -1/4`, `N = 1/16`,
`J = -1/64`, `C = 0`, so

```
FOLD(1 face) = -2C - e2·N + J = 1/64 - 1/64 = 0   exactly.
```

That identity is what lets `-13/896` serve simultaneously as the full one-face
`e4` (`EXPECTED_AXIAL[4]`) and as v10a21r's direct `D[{ROOT}]` (`:313`). No
document in the set states it, cites it, or checks it, and `J = -1/64` occurs
nowhere in this repository. The operational consequence is forward-looking:
the five-point specification for a valid two-face F07 weight
(`A:98-104`, `B:159-176`, `D:213-227`) fixes a **vacuum** convention and no
**fold** convention, so any comparison of an F07 size-2 weight against blind
`size 2 c4` is undefined until the `+37.84` of size ≥ 2 fold weight is assigned.

**The one-face agreement is not new.** `B §0:21`, `D:29` and `A §3`'s premise 1
present it as this session's finding. It is already a corpus certificate, one
line below the two lines they do cite:

```
ENGINE_O4_hodge_rootonly_firewall_v1.py:41  EXPECTED_VACUUM = (0, 0, -3/4, -9/32, -39/1280)
                                        :42  EXPECTED_AXIAL  = (8/3, 1, -1/4, -1/16, -13/896)
                                        :43  EXPECTED_GAP    = (8/3, 1, 1/2, 7/32, 143/8960)   ← never cited
```

`one_face_certificate()` at `:218-230` recomputes all three series in exact
`Fraction` from SU(3) characters and raises on mismatch; executed here, it
passes. Two further sites carry the same 5-vector as a frozen comparator
(`NB_O4_hodge_v10a29b_m5_first_no_m4_rerun.ipynb:20,66`, cell 7 lines 119-129;
`NB_O4_hodge_v10a24c_section15_reduced_gpu_benchmark_fresh.ipynb` `[15A]`),
both unexecuted. The *localization step* — that the gap is therefore at
size ≥ 2 — I could not find in the corpus, so that inference does belong to the
session; the premise does not.

**Why the search missed it.** `workhouse.corpus_index.PATTERNS` matches
`a/b`, `Fraction(a, b)` and `\frac{}{}`, but this engine writes `Q(143, 8960)`
under the alias `Q = Fraction` at `:37`. Running `_extract` over that file
yields **zero** rationals: the whole `EXPECTED_*` block is invisible to
search-by-value. See §6.

---

## 4. Routing: C1/C22 under G3, not C2

`A:78` and `B:220` file the F07-vs-blind split as "a sub-entry of C2 / G3".
The **G3 half is right**; the **C2 half is a category error**.

C2's registered scope is the off-axis coefficient only: its two sides are
`-211835444920651/4405310420659200` and `-0.020213328886166577`,
`delta = 0.027873054295192174` (`contradictions.yaml:63-74`), and its check
(`invariants.py:361-366`) compares nothing else. The symbol register binds
`C_shp` and `Delta_C` to C2 (`symbols.yaml:72, 98`) and `Delta_Gamma` — the
family a `Γ`-point rest-scalar gap belongs to — to `[C1, R6]` (`symbols.yaml:81`).

The structural reason is machine-checked, not merely asserted:
`invariants.py:436-447` establishes that `Φ_C` vanishes at `Γ` along every
direction, so a `Γ`-point scalar constrains `Δ_Γ` and places no constraint
whatsoever on `Δ_C`. A dispute that is entirely a `k = 0` quantity cannot be a
sub-entry of C2, because adjudicating it cannot move `Δ_C` in either direction.

The repository already keeps the disputed value in the right place:
`contradictions.yaml:36-40`, inside **C1**, as the "quarantined shortcut". A
grep of the ledger finds it at exactly that one line and never under C2.

This matters beyond bookkeeping. `B:213-219` uses the C2 label while asserting
that C1/C22 are not being reopened; naming C1 would make visible that the
document *is* proposing to reopen a resolved entry. The compliant landing is to
amend `contradictions.yaml:36-40` in place, or open **C23** (`C22` at `:272` is
the current maximum), with both values side by side and neither promoted.

Routing to G3 is *not* a reversal of ADR 0002. The ADR says G3
"no longer *needs to* adjudicate a scalar" (`0002:61`) — a relief of a burden,
not a prohibition — and G3's own protocol retains two scalar items
(`gaps.yaml:68, 70`).

---

## 5. The certificate package `E`

**What it establishes.** `sha256sum -c SHA256SUMS.txt` passes 20/20 on a fresh
extract. Replaying all 69,800 ledger records in exact `Fraction` reproduces
`Σ w_T H_T = -805586892848311021/8092176661386675` and
`D_EXACT = -13/896 + Σ/2 = -361008126292641364183/7250590288602460800`. The
target-leakage scan is **clean**: no occurrence of `M4_ORACLE`, `ax_rest`,
`local_shift`, `M4_SHORTCUT`, `7751458630189173`, `160506019419340168451` or
the `Δ_Γ` digit strings in any shipped `.py`. No float or tolerance appears in
the arithmetic path. The CRT recovery is not near critical: the tightest
`|numerator|/bound` over all records is 0.0123, an 81× margin.

**What it does not establish, and the reports say otherwise.**

1. *Not replayable as shipped.* `AUDIT_REPORT.md:70` claims the ZIP contains
   "all contractor/replay sources needed to audit the route". It does not:
   `ledger_generator.py` is absent, and **5 of 7 shipped modules raise
   `ModuleNotFoundError`**. The entry-point pickle's keys are
   `ledger_generator.LXState` instances, so the package cannot unpickle itself.
   With a 3-line class stub, the two renamed modules restored, and the
   one-level path offset fixed, everything runs and reproduces:
   `validate_modular_haar_ledger.py` exit 0; `crosscheck` exit 0 (165.7 s);
   `independent_cross_check_actual_topologies` 44/44; and the full
   `independent_replay_modular_crt.py` 69,800/69,800 in 4013.7 s, reproducing
   `D_EXACT` and `-11.068479463778765` bit-identically. **This is a packaging
   defect, not a mathematical one** — but it means the frozen census
   (69,800 ← 117,161, 5,400 matched sectors, 9,814,138 raw upper bound,
   54 skipped one-face) is carried as pass-through data and recomputed nowhere
   in the bundle.

2. *No upstream binding.* The package binds its own entry point
   (`root_exact_pair_topologies.pkl.gz = 5337734a…`) and nothing above it. A
   regex over the full 12,458,390-byte decompressed pickle finds **zero**
   64-hex substrings; the key literally named `source_history_sha256` holds a
   counts dict, not a digest. None of the nine hashes in `C §3`'s chain table
   appears anywhere in `E`. `C` describes a different artifact than the one
   delivered (`C:131`'s "final exact summary" `d3d2cb89…` is not the shipped
   summary `2b845725…`), and one shared filename makes them easy to confuse.

3. *"All 69,800 lifted numerators independently checked" is not supported by
   any shipped artifact.* `INDEPENDENT_REFEREE_REPORT.md:48` says so; the only
   all-record artifact is `validate_modular_haar_ledger.py`, which **reads**
   `scaled_haar_numerator` from the generator's own ledger (`:59-62`) and gates
   it only by `|n| ≤ bound` — an interval admitting a **minimum of 13,123**
   integers, median 3.7·10¹³. The script that does recompute them emits no
   artifact present in the zip. Shipped independent coverage is 44 + ≤40
   ≤ **84 of 69,800 = ≤ 0.120%**.

4. *Both "exactness gates" are unfailable.* `validate_modular_haar_ledger.py:74-77`
   asserts `Fraction(n·k, QBOUND) == n/d` where `k = QBOUND//d` — a tautology
   once divisibility passes. And divisibility itself cannot fail: every term is
   `w_T·(n_T/q_T)/2`, so the denominator necessarily divides
   `A = 239017618379238526616076288000`, and `QBOUND/A = 263139840000` exactly.
   `A` is a function of the frozen weights and pattern lists only; no computed
   numerator enters it.

5. *`180/180` synthetic tests are unsupported.* The string appears on exactly
   one line in the package (`INDEPENDENT_REFEREE_REPORT.md:46`); no `.py`
   contains `180`, `synthetic`, or `three-way`, and no JSON records that count.

6. **`rank3_order4_exact_haar_summary.json` was edited after generation.**
   `modular_haar_contractor.py:545` writes it with
   `json.dumps(..., sort_keys=True)`. The shipped file has CRLF line endings
   throughout **except lines 10–14**, which are LF-only — and those five lines
   are exactly the QBOUND/decimal gate block that `AUDIT_REPORT.md:41-44`
   headlines. Of 20 top-level keys, 19 are in sort order and exactly one
   adjacent pair is transposed, at indices 2/3, inside that LF island. No
   invocation of `sort_keys=True` can emit that order. Both anomalies are
   unique to this file among the package's five JSONs. Nothing here suggests
   the *values* are wrong — the D_EXACT they carry reproduces exactly — but the
   file is not the untouched output of the program that claims to have written
   it, which is the whole point of a hash-pinned certificate.

7. *Undisclosed register status.* `AUDIT_REPORT.md:28-34` and
   `INDEPENDENT_REFEREE_REPORT.md:29-35` present
   `-160506019419340168451/14501180577204921600` as "the requested final
   combination" with no qualifier. A case-insensitive grep of the whole package
   for `quarant|reject|falsif|disput|shortcut|superseded` returns **zero** hits.
   A reader of `E` alone would not learn that WORKHOUSE carries that exact
   rational as `QUARANTINED_SCALAR`.

8. *Packaging hygiene.* `AUDIT_REPORT.md` and
   `WORKHOUSE_..._INDEPENDENT_AUDIT_20260823.md` are byte-identical
   (`99f31f3b…`) and only the first is in the manifest, so a reader may count
   two independent audit documents where there is one. 1,517,049 bytes (38.4%
   of the bundle) are duplicated between the root and `modular_haar_run/`, and
   no script reads the root copies. Under ADR 0012 the package cannot land in
   `runs/` as shipped: `tests/test_runs.py:23` requires `SHA256SUMS`, not
   `SHA256SUMS.txt`.

---

## 6. What the review found in *this* repository

These are repo-side, not upload-side, and each is currently unrecorded.

**6.1 `RAW_FOLDED_AXIAL_GAMMA_NUM` is 381 ulps stale and unchecked.**
`constants.py:428` records `-11.9485781794007`. The exact value is available
from two rationals in the same file: `QUARANTINED_SCALAR + LINKED_VACUUM_4 =
-86634244910174898583/7250590288602460800 = -11.948578179401377`. The gap is
`6.774e-13` — **381 ulps** by `math.ulp`, 511 under the `2^-53` convention the
C20 check itself uses at `invariants.py:408`. The transcription is faithful;
the imprecision is upstream, and now measurable: RUN15's own float `D`
(`-49.7901704444838`) is `7.375e-13` off the exact `D_EXACT`, and that
propagates straight through `ax_rest = D + FOLD`. Nothing reads the constant —
repo-wide it appears three times, none of them a check — so no suite would
catch drift in it. The repository has the right pattern and did not apply it
here: `DELTA_GAMMA_NUM` / `DELTA_GAMMA_AS_PRINTED_NUM` (`constants.py:211-215`)
carry a **one**-ulp discrepancy and it is a registered check
(`invariants.py:327-334`).

> The upload's `B:36` prints `-11.9485781794014` — the correctly rounded
> 15-significant-figure decimal of the exact value, ~30× closer than the repo
> constant. `B` is right here and the repository is wrong. `A:38`'s `-11.9486`
> hides the question.

**6.2 `workhouse search --corpus` silently discards its own results.**
`search.py:219-225` returns early when there are no claim or symbol hits,
before the corpus-occurrences renderer at `:246-259`. Reproduced live:

```
$ workhouse search --corpus -- "-327/83776"
no claim matches '-327/83776'.
...
For the corpus itself, add --corpus, or grep it directly.     ← --corpus was passed
```

The value has 61 occurrences across 25 files. Same for `-13/896` (79/26),
`-54321/837760` (63/23), `-39/1280` (43/26), `143/8960` (6/3), `-5/7168` (2/2)
— every rational in this dispute. `cli.py:160-163` sets `found_in_corpus` from
the same scan and exits 0, so the output and the exit code disagree. This
directly undercuts the front-door role asserted at `CLAUDE.md:108-112` and the
stated intent in the `corpus_occurrences` docstring (`search.py:163-166`). It
went undetected because the documented example (`README.md:87`,
`workhouse search 5/48 --corpus`) has 18 claim hits and never reaches the
branch. One-line fix.

**6.3 `corpus_index` cannot see aliased `Fraction` constructors.** `PATTERNS`
misses `Q(143, 8960)` where `Q = Fraction`, which is why the one-face
certificate in `ENGINE_O4_hodge_rootonly_firewall_v1.py:41-43` is invisible to
search-by-value. Combined with 6.2, both indexes were blind to the material the
upload re-derived — which is the measured failure mode AGENTS.md names.

**6.4 Two live checks contradict each other on Hamer provenance.**
`make verify` prints both:

- `invariants.py:392-393` — "a_4 is an unverified notebook transcription, so
  this is a normalization cross-check, not primary-source proof"
- `invariants.py:1285-1292` — "The caveat is retired, not forgotten", with the
  pin `sha256 96b3ec0f…`

`literature/index.yaml:454-497` sides with the second (`status: verified`,
"verified digit for digit against Table 1"). `constants.py:229-238` and
`constants.py:647` contradict each other the same way, 400 lines apart, and
`index/claims.jsonl:29,149` regenerate the stale side faithfully — so
`make catalogue` will not fix it; `constants.py:647` must change first. The
honest replacement is neither the old caveat nor silence: the primary was read
and digest-pinned on 2026-08-21, but `fulltext: null` means the copy is not
stored here, so the digit-for-digit reading is not re-checkable in-repo.

**6.5 `HAMER_TOLERANCE = 5.3e-13` has no recorded derivation** and sits
2.46% above the observed gap (`5.1725e-13`, 4659 ulps), so the check flips to
FAIL on any drift of `M_GAMMA_4_NUM` past 114 ulps. Across the five Hamer
bridge comparisons, `gap/print-budget` is 0.994, 0.557, 0.784, 0.681 — and
**1.293 for `a_4` alone**. The structural reason is unstated: the other four
target exact corpus rationals, so paper rounding is their only error source,
whereas `a_4`'s target is a float from the blind run carrying a second error
term — measurable in the same run block (`15 hour RUN.txt:10641-10648`:
`A` vs `5/48` at rel `5.887e-13`, `alpha` vs `5/12` at rel `5.839e-13`), which
covers the overshoot. **Do not widen the tolerance**; record the reason.

*(A circularity hypothesis — that `HAMER_A4_NUM` was back-computed from the
blind per-size table — was tested and refuted. It arose from the upload's own
rendering: `B:60-61` prints sizes 4 and 5 as "`~ 0 (numerical zero)`" where the
transcript prints `-1.3933298959e-14` and `-2.85049761573e-14`. The four-row
subset does land bit-exactly on `8·a_4`; the six actual rows do not, and no
permutation of them does. The coincidence is an artifact of the substitution.)*

---

## 7. Tier discipline and citation errata

`A §2` is headed "The certified spine (what is machine-verified)" and asserts
"Every row is T1 (exact) or T2 (numerical), reproducible via the check". None
of its eight rows is a registered check in `invariants.py` — grep of the file
for `8960, 896, 1280, 83776, 837760, 1675520, 1474623, 54321, 7168, W22`
returns zero hits — and the check it names was not delivered. Row-level:

| row | claimed | actual |
|---|---|---|
| one-face gap | T1 | correct |
| one-face agreement | T2 | T2, tolerance unstated; blind side is `%+.12g`, bounds equality only to `~3e-14` |
| one-face agreement is explained | T1 | source-text gates, no recorded run; and see §2 — the face qualifier is inverted |
| two-face vacuum | T1 | **T2 at 3e-9.** `_v17_vac_cluster` is pure float; the rationals are *recognized* by `Fraction(x).limit_denominator(1e9)` (`v10a7:5265`), and all four gates are `abs(float − float(rational)) < V10A7_TOL` (`:5192, 5433, 5434, 5436`). Residuals: `e4` 4 ulps, `ω4` 67 ulps |
| linked-vacuum decomposition | T1 | the row's content is `1675520 = 1280·1309 = 83776·20`, which is just "1675520 is the lcm of the two summand denominators" — true for *every* integer pair `(a,b)`. It pins no counts. The exact identity in §1 does |
| blind table closes | T2 | the six printed rows sum to `-0.7751458630184425`, **4.748e-13 = 4277 ulps** from the oracle at `:10626`. Inside the `1.55e-12` print budget, so not a defect — but `A`'s 13th digit (`…189`) is not supported by its cited evidence |
| F07 anchoring-invariant | T1 | rests on an undelivered document |
| F07 oracle-free | **—** | no tier at all, under a "machine-verified" banner |

Errata found in the citations:

- **`B:99`** — `83776 = 2⁷·7·11·17²` is wrong; `83776 = 2⁶·7·11·17 = 64·1309`.
  The printed product is `2848384 = 34 × 83776`. The `2⁷` is carried over from
  `837760 = 2⁷·5·7·11·17` two lines above. The value and the `| QBOUND`
  divisibility both survive; only the annotation is wrong. `B:112`'s
  `1675520 = 83776·20` in fact *forces* the correct factorization.
- **`B:143`** — the quotation *"its incidence test was algebraically wired to
  reproduce v10a.20"* is cited to `:2925, :3897`. It is verbatim at `:2925`
  and `:2981` (a duplicated transcript block, one utterance) and **not** at
  `:3897`, which paraphrases it in different words.
- **`A`/`B`** attribute the v10a.21r retirement to *the maintainer*. All six
  cited lines are in the assistant's voice; `:1977` is the human turn and
  `:1978` opens the reply.
- **`C:61`** cites `invariants.py:414-422` for the target-derived statement.
  5 of those 9 lines belong to the C20 check and 2 are blank; the correct range
  is `:421-429`. This is a **stale** citation, not a wrong one — it was exact
  until commit `fb8a35c` displaced the block by +7 lines.
- **`E`** — `INDEPENDENT_REFEREE_REPORT.md:16` gives
  `D_EXACT_decimal = -49.790170444484609`; the correctly rounded value is
  `…607`. `modular_haar_contractor.py:535` emits
  `format(float(d_exact), ".17g")` — the exact rational is rounded to binary
  before being rendered, so the field is the 17-digit rendering of the nearest
  double.
- **`A §0`** advertises an "8-check screen"; `B §6` lists 6 rows.

**Four of the seven documents `A` declares are missing**, including both it
names as entry points ("If you read one thing: F … the check"):
`DENOMINATOR_LOCALIZATION_INVESTIGATION`, `ORACLE_COUNTERFACTUAL_AUDIT`,
`F07_VS_BLIND_COORDINATION_NOTE`, and `f07_twoface_adjudication_check.py`.
`A`'s declared reading order cannot be followed, and `A §2` rows 7-8 plus the
capstone cannot be audited. `D`'s five line-anchors into
`WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md` are likewise
unresolvable, though the substance behind two of them is corroborated by `E`.

---

## 8. Revised recommendation

`A §6` proposes five things to land. Revised against the above:

1. **Do not** file the split under C2 (§4). Amend the C1 quantity block at
   `contradictions.yaml:36-40` in place, or open C23, naming C1/C22 under G3.
2. **Do not** land the G3 one-liner as written. Its first clause credits the
   session with the one-face agreement, which is a pre-existing corpus
   certificate (§3); its second clause names a discriminator that is provably
   null (§2). What is genuinely new is the size ≥ 2 *inference*.
3. **The relabel is still a maintainer call, and the evidence has moved one
   axis, not two.** `E` moves the *evidence* level of `QUARANTINED_SCALAR`
   (`record-backed` is now stale — the value is reproducible from a target-free
   route, subject to §5's provenance gaps). It moves the *status* axis not at
   all: `falsified` is a claim about physical identification, and nothing in
   the upload bears on it. `A`/`B`/`D`'s proposed field names
   (`arithmetic_status`, `physical_status`, `quarantine_reason`) would
   introduce a fourth vocabulary, which AGENTS.md forbids; the existing
   status/evidence split already expresses the distinction exactly.
4. **The proposed ADR duplicates existing rules.** "Exactness certifies
   arithmetic, never physical identification" is CLAUDE.md non-negotiable #5,
   ADR 0001, and ADR 0010. A new ADR adds nothing.
5. **Cheapest genuine promotions available now**, none of which the upload
   proposes:
   - register `one_face_certificate()` (`ENGINE_O4_hodge_rootonly_firewall_v1.py:218-230`)
     as a T1 invariant. It executes and passes today, derives all five
     `EXPECTED_GAP` entries from SU(3) characters, and `143/8960` appears
     nowhere in the verification layer;
   - register the exact `ax_rest` alongside the stale float, in the
     `DELTA_GAMMA_AS_PRINTED_NUM` pattern (§6.1);
   - fix `search.py:219-225` and extend `corpus_index.PATTERNS` to aliased
     constructors (§6.2, §6.3);
   - reconcile the two Hamer provenance statements (§6.4) and record the
     derivation of `HAMER_TOLERANCE` **without** widening it (§6.5);
   - register the one-face fold cancellation `-2C - e2·N + J = 0` (§3) — it is
     the unstated premise the whole localization rests on, and it is exact.

The decisive test the upload was reaching for still exists, but it is not
Knob B. `C §9` states it correctly: prove or refute, from a target-free
canonical construction, that `D11 + ½⟨W2,R2⟩ + fold − attached_vacuum` **is**
the canonical vacuum-subtracted order-4 `Γ` coefficient. That is an operator
identity, not another numerator replay, and no amount of exact arithmetic on
the F07 side substitutes for it.

---

## 9. Reproduction

```bash
python3 - <<'PY'
from fractions import Fraction as F
D=F(-361008126292641364183,7250590288602460800); FOLD=F(5315003,140454); V=F(-1474623,1675520)
assert D+FOLD-V == F(-160506019419340168451,14501180577204921600)
assert float(D+FOLD) == -11.948578179401377          # constants.py:428 says -11.9485781794007
assert F(-13,896)+F(39,1280) == F(143,8960)
assert F(-54321,837760)-2*F(-39,1280) == F(-327,83776) and 83776 == 2**6*7*11*17
assert 13*F(-39,1280)+124*F(-327,83776) == V
PY

sed -n '3p;10614p;10617p;10619,10626p' "corpus-import/records/transcripts/15 hour RUN.txt"   # v10a.26 exact-SW
sed -n '41,43p;218,231p' corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_rootonly_firewall_v1.py
sed -n '606,616p'        corpus-import/programs/hodge_o4_adjudication/src/DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py
workhouse search --corpus -- "-327/83776"            # reproduces §6.2
```

*End of referee report.*
