# F07 vs blind linked-cluster: the two-face adjudication

**Scope.** Rank-3 / order-4, Γ-point axial rest coefficient (`m₄`).
**Date.** 2026-08-23. **Status of this document:** T3 (asserted) — every *check*
it cites is machine-verified against the corpus; the physical adjudication it
localizes is **open**. No repository file was edited to produce it.

Companion runnable check: `f07_twoface_adjudication_check.py` (exit 0; writes
nothing; drop-in as an `invariants.py` suite).

---

## 0. One-paragraph statement

There are two competing exact/measured values for the fourth-order axial rest,
and they are branches of the *same* physical quantity, not rival estimates of
different coordinates. The **F07 branch** (direct W2/R2 trace-history + Q1 fold −
linked vacuum) is now known **exactly**: `m₄,F07 = −11.068479463778765`. The
**blind linked-cluster oracle** (v10a.23/24c rooted incidence transform) measures
`m₄,blind = −0.7751458630189173` (Hamer-validated). They disagree by
**10.293333600759848**. The decisive new fact is that the two branches **agree
exactly at one face** (`143/8960`), so the entire gap lives in the multi-face
(size ≥ 2) sector. The natural next test — compute the F07 two-face weight and
compare it to the blind `size 2 c4 = −0.403971702978` — has a **trap**: the one
engine that yields an exact F07 per-size decomposition (`v10a.21r`) is
algebraically wired to reproduce the F07 total and was retired by the maintainer
as unable to adjudicate. The two-face question therefore remains open and
requires a genuinely independent computation.

---

## 1. The three scalars (do not conflate)

| scalar | value | identity |
|---|---:|---|
| `ax_rest` (raw folded rest) | `−11.9485781794014` | `D_EXACT + FOLD`, pre-linked-vacuum |
| `M4_SHORTCUT` = **F07 branch** | `−11.0684794637788` | `ax_rest − V_link` **= QUARANTINED_SCALAR** |
| `M4_ORACLE` = **blind linked-cluster** | `−0.7751458630189` | Hamer-validated; complete construction |

- `M4_SHORTCUT − ax_rest = +0.880098715622613 = −V_link` (a genuine linked term).
- `|M4_ORACLE − M4_SHORTCUT| = 10.293333600759848` — **the real branch conflict**.
- The v10a.24c anchoring uses `local_shift = M4_ORACLE − ax_rest = +11.1734`
  (`= RUN15_APPLIED_SHIFT`), forcing the anchored answer to the **oracle**, not
  the shortcut. So the shortcut and the oracle are **rivals**, not input/output.

All values re-verified this session against
`corpus-import/records/transcripts/15 hour RUN.txt` and `src/workhouse/constants.py`.

---

## 2. Exact one-face agreement (the load-bearing localization)

The blind oracle is the **sum of its rooted per-size contributions**
(`15 hour RUN.txt:10620-10626`, §[16] ROOTED INCIDENCE TRANSFORM):

```
size 1: c4 = +0.0159598214286
size 2: c4 = -0.403971702978
size 3: c4 = -0.178800648136
size 4: c4 ~ 0            (numerical zero)
size 5: c4 ~ 0            (numerical zero)
size 6: c4 = -0.208333333333
TOTAL m4  = -0.7751458630189173     (= M4_ORACLE)
```

The F07 branch's one-face contribution is exactly

```
D11 − e4_vac(1) = −13/896 − (−39/1280) = −13/896 + 39/1280 = 143/8960
               = 0.0159598214286…      (143 = 11·13,  8960 = 2⁸·5·7)
```

and this **equals the blind `size 1 c4` to full printed precision**. Both
one-face inputs are corpus-exact:

- `EXPECTED_AXIAL = (8/3, 1, −1/4, −1/16, −13/896)` and
  `EXPECTED_VACUUM = (0, 0, −3/4, −9/32, −39/1280)`
  — `ENGINE_O4_hodge_rootonly_firewall_v1.py:41-42`
- `gate("exact one-face O4 coefficient is −13/896", … == Fraction(−13,896))`
  — `DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:615`
- `V1 = −39/1280`, `analytic_11 = −13/896`
  — `ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:313,358`

**Consequence.** The one-face sector cannot be the source of the split. Ruled out
at the local-root level: magnetic-interaction sign, local source normalization,
the analytic one-face direct term, the one-face vacuum subtraction. The first
disagreement must occur among connected clusters of size ≥ 2.

---

## 3. Exact two-face vacuum (a clean input that *is* available)

The two-face attached-vacuum weight is exact and independent of the disputed
axial construction:

```
e4(C)  = −54321/837760          (two-face vacuum pair energy)
ω4     = e4(C) − 2·V1 = −327/83776     (irreducible pair weight; VPAIR)
         83776 = 2⁷·7·11·17²    (in-scope, | QBOUND)
```

Verified two ways in the corpus:
- coplanar and perpendicular pairs **agree**: both `ω4 = −327/83776`
  (`Monday 531 PM.txt:5193-5202`, v10a.7 gates).
- disconnected two-face vacuum spectator has **zero** linked O(u⁴)
  (`ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5438-5444`) — so the two-face
  contribution comes only from *connected* pairs.

The linked vacuum total decomposes by face count:

```
V_link = −1474623/1675520 ;  1675520 = 1280·1309 = 83776·20
       = V1 · (single embeddings) + VPAIR · (pairs)
       (exact sum gated: v10a.21r  V_MIN == −1474623/1675520)
```

So the vacuum side of any two-face F07 computation is already exact. What is
missing is the two-face **axial-history** side under an independent construction.

---

## 4. The trap: why the exact F07 size-2 is not simply extractable

`v10a.21r` (`ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py`) builds an
exact support-resolved ledger and a recursive incidence (rooted Möbius) transform
that **does** yield an exact F07 per-size decomposition. Its size-1 weight is
`143/8960` — matching. It is tempting to read off its size-2 weight and compare
to the blind `−0.403971702978`.

**Do not.** The engine's own gates show the incidence transform is constructed to
sum back to the F07 total:

```
M4_EXACT = −160506019419340168451 / 14501180577204921600   (= M4_SHORTCUT, F07)
gate("v10a.21 minimal marked-history ledger sums to exact v10a.20 m4", … == M4_EXACT)
gate("v10a.21 full rooted recursive linked sum equals exact v10a.20 m4", … == M4_EXACT)
gate("v10a.21 recursive incidence transform exactly recovers minimal-support weights")
```

The maintainer already identified and **retracted** this route:

> "Stop. Do not run v10a.21r." — `Monday 531 PM.txt:1978`
> "its incidence test was algebraically wired to reproduce v10a.20" — `:2925, :3897`
> "v10a.21 is structurally incapable of adjudicating this" — `:3702`
> "Retire v10a.21/v10a.21r as adjudicators. They are still useful as internal
> consistency checks of support bookkeeping, but they cannot distinguish m…" — `:2287`
> "v10a.21 DELTA_MIN / RAW : NOT USED — the circular construction … is gone." — `:2548`

Extracting the F07 size-2 from `v10a.21r` and comparing it to the blind size-2
would produce a green-looking comparison that means nothing — the exact failure
mode CLAUDE.md warns against ("make the failing check pass is frequently wrong
here"). The companion check encodes a **provenance guard** that refuses any F07
two-face value whose source names the retired engine.

---

## 5. What a valid two-face F07 computation must satisfy

Per `WORKHOUSE_RANK3_ORDER4_F07_VS_BLIND_..._STRUCTURAL_TRACE §9`, an independent
F07 two-face weight (comparable to blind `size 2 c4 = −0.403971702978`,
`15 hour RUN.txt:10621`) must:

1. consume **typed physical P/Q1/Q2 blocks**, or prove an exact isometry from the
   trace-history representation (the exact-Haar package aggregates by endpoint
   trace-states and *forgets lattice geometry*, so it cannot supply rooted
   two-face weights — `exact_haar_sum.py:276-368, 81-111`);
2. make **`W22` unschedulable at order four** (the blind v10a.24c basis admits
   `Q2↔Q2` and extracts coefficients by a degree-6 fit on 13 points — an
   order-truncated `W22`-off comparison is required before its size-2 is
   promotable — `ENGINE…v10a24c…py:6894-6899, 6928-6946`);
3. subtract the exact **vacuum before** rooted Möbius inversion;
4. retain **all three T1 polarizations** (the F07 package fixes
   `polarization_index = 2`);
5. map the resulting marked weights to the **3,895 Stage-3H records** and assemble
   the unshifted **189-record** full-T1 kernel.

Either outcome is decisive and finite:
- **agree at two faces** → the divergence lives at size ≥ 3; the F07 restriction
  is provably the whole story (a clean, falsifiable localization);
- **disagree at two faces** → the F07 shortcut is *wrong* at the first multi-face
  order, and the blind oracle is vindicated where it was quarantined.

---

## 6. The runnable check (summary)

`f07_twoface_adjudication_check.py` — standalone, exit 0, no repo write:

| # | check | tier | asserts |
|---|---|---|---|
| 1 | `oneface_gap_is_143/8960` | T1 | `−13/896 + 39/1280 = 143/8960` |
| 2 | `oneface_matches_blind_size1` | T2 | `143/8960` == blind size-1 (`:10620`) |
| 3 | `twoface_vacuum_is_-327/83776` | T1 | `e4(C)=−54321/837760`, `ω4=−327/83776` |
| 4 | `vlink_face_decomposable` | T1 | `1675520 = 1280·1309 = 83776·20` |
| 5 | `blind_table_sums_to_oracle` | T2 | Σ size-c4 = `−0.775145863…` (`:10626`) |
| 6 | `twoface_adjudication_OPEN` | FINDING | target `−0.403971702978` pinned; F07 size-2 **unresolved**; circular v10a.21r provenance **refused** |

Verified: the guard rejects an F07 size-2 value tagged with retired-engine
provenance, and accepts one tagged with an independent (§5-compliant) source.

---

## 7. Ledger status — flagged, not changed

The forensic traces recommend relabeling `M4_SHORTCUT` from
`rejected-by-both` / `falsified` to *"exact F07-branch scalar; physical
identification audit-pending"* (`contradictions.yaml:36-40`,
`constants.py:426-435,649-655`). **This document does not make that change.**

Rationale (non-negotiable #2 — never promote a disputed value):
- the arithmetic exoneration is real (the F07 value is exact and provably
  oracle-free), **but**
- the F07 branch is *physically incomplete* (restricted face-set; no rooted
  crosswalk; no independent two-face weight yet), and the counterfactual audit
  explicitly counsels **not** reopening C1/C22 on arithmetic grounds alone.

The relabel is a maintainer judgement for **Alex**. What *is* settled and safe to
record: C22 (Gate-85) is unchanged and correctly resolved; C1's `q_band` vs
`m_Γ` naming resolution stands (ADR 0002); the open item is the F07-vs-blind
multi-face split (a sub-entry of C2/G3), **localized to size ≥ 2 by the exact
one-face agreement above**.

---

## 8. Reproduction pointers

- one-face vectors: `ENGINE_O4_hodge_rootonly_firewall_v1.py:41-42`;
  `DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:615`
- two-face vacuum: `Monday 531 PM.txt:5193-5202`;
  `ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5438-5444`
- F07 total / support ledger: `ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:42-43,300-470`
- blind per-size table: `corpus-import/records/transcripts/15 hour RUN.txt:10620-10626`
- circularity retraction: `corpus-import/records/transcripts/Monday 531 PM.txt:1978,2287,2548,3702,3897`
- check: `f07_twoface_adjudication_check.py`

*End of record.*
