# Rank-3 / order-4 Γ-scalar: master record

**Date.** 2026-08-23. **Status of this document:** T3 (asserted) — a front-door
index and synthesis over the session's records and checks. Every *check* it
points to is machine-verified; every *inference* is labelled. No repository file
was edited; the session was read-only and everything below lives in scratchpad
until a maintainer decides what lands.

**One sentence.** The fourth-order axial Γ-scalar has two exact/measured branch
values that disagree by 10.293; this session localized the entire disagreement to
the multi-face (size ≥ 2) sector, named a single testable mechanism for it, and
built the runnable screens — without promoting either side of the open
contradiction.

---

## 0. The document set (what to read, in order)

| # | document | what it establishes |
|---|---|---|
| A | `DENOMINATOR_LOCALIZATION_INVESTIGATION` | the QBOUND/`ℤ[S⁻¹]` provenance layer; capstone that the certificate stack is *necessary, not sufficient* |
| B | `W2_R2_ORACLE_LINEAGE_TRACE` | dataflow forensics: the exact-Haar package is oracle-free but a *target-known* replay |
| C | `ORACLE_COUNTERFACTUAL_AUDIT` | the anchoring counterfactual; F07 value is invariant under the late diagonal shift |
| D | `F07_VS_BLIND_ORACLE_STRUCTURAL_TRACE` | the structural fork (W22, inventories, one-face agreement, the §9 next step) |
| E | `F07_VS_BLIND_TWOFACE_ADJUDICATION` | two-face localization, the circular v10a.21r trap, the provenance guard |
| F | `F07_VS_BLIND_COORDINATION_NOTE` | the six cross-document connections (C1–C6), incl. the W22 axis |
| — | `f07_twoface_adjudication_check.py` | runnable 8-check screen; exit 0; drop-in `invariants.py` suite |

**If you read one thing:** F (the coordination note) for the argument; the check
for the machine-verified spine.

---

## 1. The three scalars (never conflate)

| scalar | value | identity |
|---|---:|---|
| `ax_rest` (raw folded rest) | −11.9486 | `D_EXACT + FOLD` |
| **`M4_SHORTCUT`** = **F07 branch** | **−11.0685** | `ax_rest − V_link` = QUARANTINED_SCALAR |
| `M4_ORACLE` = blind linked-cluster | −0.7751 | Hamer-validated; complete construction |

- `|M4_ORACLE − M4_SHORTCUT| = 10.293333600759848` — the real, open branch conflict.
- The v10a.24c anchoring uses `local_shift = M4_ORACLE − ax_rest = +11.1734`,
  forcing the anchored answer to the **oracle**. So `M4_SHORTCUT` and `M4_ORACLE`
  are **rivals**, not input/output.
- `−11.0685` is the **complete F07-branch answer**, not a raw intermediate
  (correction to document A §11.3, resolved in E/F; see §5 below).

---

## 2. The certified spine (what is machine-verified)

Every row is T1 (exact) or T2 (numerical), reproducible via the check.

| fact | tier | statement |
|---|---|---|
| one-face gap | T1 | `−13/896 + 39/1280 = 143/8960` (11·13 / 2⁸·5·7) |
| one-face agreement | T2 | `143/8960` = blind `size 1 c4` (`15 hour RUN.txt:10620`) |
| **one-face agreement is explained** | T1 | W22 (the branches' only structural difference) is exactly O4-null at one face; first bite O5 = `−5/7168` (`DATA_O4_OrderSchedule…:614,616`) |
| two-face vacuum | T1 | `e4(C) = −54321/837760`, `ω4 = −327/83776` (coplanar==perp) |
| linked-vacuum decomposition | T1 | `V_link = −1474623/1675520`, `1675520 = 1280·1309 = 83776·20` |
| blind table closes | T2 | Σ per-size `c4` = oracle `−0.7751458630189` (`:10626`) |
| F07 anchoring-invariant | T1 | derivative of every upstream quantity w.r.t. the anchor scalar is 0 (audit C §4) |
| F07 oracle-free | — | two independent scanners, zero leakage (B §2, C §3) |

**Capstone (A §11.2).** `M4_SHORTCUT` passes *every* arithmetic gate —
`den | QBOUND`, the C2 localization gate, a hash-frozen Lean-adjacent derivation —
and is still physics-open. The certificate stack is **necessary, not sufficient**:
exactness certifies arithmetic, never the physical identification of what is
computed.

---

## 3. The open question, fully localized

**Open:** does the F07 branch (−11.0685) or the blind linked-cluster branch
(−0.775) correspond to the canonical physical fourth-order coefficient? This is a
sub-entry of C2 / G3. **Neither side is promoted.**

**Localization (this session's contribution):** the entire 10.293 gap lives in the
**multi-face (size ≥ 2)** sector, because
1. the branches agree exactly at one face (§2), and
2. that agreement is *explained* — W22 is exactly O4-null at one face (§2), and
3. F07 is invariant under the late anchoring (§2),

so the gap is neither anchoring nor one-face; it is purely multi-face accounting.

**The named suspect:** the branches differ structurally only in the Q2↔Q2 (W22)
block. F07 and the *canonical prescription* are W22-free by construction; the blind
branch admits W22 and extracts O4 by a finite-`u` degree-6 fit. The corpus proves
W22 is O4-null **only at one face**; multi-face W22-O4-safety is fit-argued, not
exactly gated — and F07 does not depend on it.

---

## 4. The decisive test (two knobs)

Extend the **existing exact one-face** machinery (`o4_equal`, `o5_difference =
−5/7168`) to **two faces**:

- **Knob A** — exact rooted two-face F07 weight (D §9: typed physical P/Q blocks or
  a proven isometry; W22 unschedulable; vacuum before Möbius; all 3 polarizations;
  map to Stage-3H). Compare to blind `size 2 c4 = −0.403971702978` (`:10621`).
- **Knob B** — blind two-face O4 recomputed **W22-off** (order-truncated).

| outcome | meaning |
|---|---|
| W22-off blind(2) ≈ F07(2) | divergence is **W22 fit contamination** — F07 & canonical vindicated on this axis |
| W22-off blind(2) ≠ F07(2) | divergence is **genuine multi-face physics** — rooted Möbius / polarization / Stage-3H crosswalk |

Both outcomes are decisive, finite, and far cheaper than the 609-cluster full-T1
run. The W22-mask knob is the discriminator between *fit artifact* and *real
physics* — a distinction none of the five documents could draw alone.

**The trap to avoid (E §4).** Do **not** read the F07 two-face weight off
`v10a.21r`'s incidence transform: it is algebraically wired to reproduce the F07
total and was retired by the maintainer as unable to adjudicate
(`Monday 531 PM.txt:1978/2287/3702`). The check enforces this with a provenance
guard.

---

## 5. Discipline notes (corrections and boundaries kept in the record)

- **Correction, document A §11.3/§12.** The framing "the package computes the raw
  un-anchored axial rest, nobody's physical answer" is imprecise: `−11.0685` is the
  complete F07-branch scalar, a genuine rival to blind. Documents E/F carry the
  fix. Land the corrected A, not the uploaded one. (Kept, not silently overwritten,
  per the "retract in the repository" rule.)
- **Correction, my own W22 framing.** "W22 flips the suspect" was too strong. The
  corpus *proves* one-face W22-safety exactly and has a multi-face fit-stability
  guard. Honest statement: multi-face W22-O4-safety is the one load-bearing claim
  that is fit-argued rather than exactly proven, and F07 does not rest on it.
- **Meta-pattern (F C3).** The capstone (a value passing all gates yet physics-open)
  and the v10a.21r trap (a decomposition passing all gates yet non-adjudicating) are
  one lesson at two scales — a concrete sharpening of non-negotiable #5.
- **Ledger.** The `M4_SHORTCUT` relabel (`rejected-by-both` → "exact F07-branch;
  physical audit-pending") is a **maintainer call** (non-negotiable #2; the
  counterfactual audit counsels against reopening C1/C22 on arithmetic alone).
  C22 (Gate-85) unchanged; C1's `q_band` vs `m_Γ` resolution stands (ADR 0002).

---

## 6. What to land (all writes; session was read-only)

1. **Corrected document A** — resolve the −11.0685 identity across the set (F C1).
2. **`f07_twoface_adjudication_check.py`** as an `invariants.py` suite — the 8
   machine-verified checks + the two OPEN discriminators (with the v10a.21r guard).
3. **`ledger/gaps.yaml`** one-liner on G3: "the F07-vs-blind split is localized to
   size ≥ 2; the decisive test is the exact W22-off two-face recomputation."
4. **ADR** — the meta-pattern (§5): exactness certifies arithmetic, never physical
   identification. (Renumber to the next free ADR id.)
5. **Optional Lean** — the frozen QBOUND cert + witness layer (A §5.5, §6), once
   `lake build` is run externally.

Nothing in 1–5 promotes either side of C2.

---

## Appendix — reproduction one-liners

```
python3 f07_twoface_adjudication_check.py         # 8 checks, exit 0
```
- one-face vectors: `ENGINE_O4_hodge_rootonly_firewall_v1.py:41-42`
- W22 one-face exact facts: `DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:610,614,616`
- two-face vacuum: `Monday 531 PM.txt:5193-5202`
- blind per-size table: `corpus-import/records/transcripts/15 hour RUN.txt:10620-10626`
- circular route (do not use): `…v10a21r…py:42-43,300-470`; retraction `Monday 531 PM.txt:1978,2287,3702`

*End of master record.*
