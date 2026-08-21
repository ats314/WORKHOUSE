# programs/hodge_o4_adjudication/ — THE LIVE FRONT

This campaign exists to settle **one number**: the fourth-order planar mixed-gradient coefficient `C⁽⁴⁾`.

## The problem

Two independent computations of the SU(3) fourth-order kernel agree on the axial coefficient and disagree off-axis:

| | historical 189-record kernel | August linked marked-cluster run |
|---|---|---|
| `A` (axial) | `5/48` exactly | `0.104166666666728` (numerical) |
| `C` (planar) | `−211835444920651/4405310420659200 = −0.04808638318135875…` exactly | `−0.020213328886166577` (numerical) |
| `Γ` anchor | `q_old⁽⁴⁾ = −2.857915988114558978…` | `m_Γ⁽⁴⁾ = −0.7751458630189173` |

`ΔC = 0.027873054295192174…`, giving `Δλ_X = 0`, `Δλ_M = 8ΔC ≈ 0.22298`, `Δλ_R = 16ΔC ≈ 0.44597`.

**A scalar re-anchoring cannot fix this.** Scalar-gauge freedom `(Q₄, G) ~ (Q₄ + δG, G)` changes the quoted rest coordinate within one kernel; it cannot change a centered planar coefficient, a bandwidth, an off-axis dispersion, or a radial curvature. The `+11.17343231638178` diagonal shift used in the 15-hour run was *target-derived*; equality after it is by construction, not by derivation. See corpus §7, §9, §10 and Appendix B.

## What is here

- `notebooks/` — the `Hodge_v10a2` → `v10a32` run series (30 notebooks), plus the `O4` occurrence preflights, the `SU3_Exact_MarkedCluster_m4` engine, and `Y4_Canonical_O4_Production`.
- `src/` — the `.py` exports of the same, the `RootOnly_Firewall`, `OrderAware_Gram_Firewall`, and the `test_*` companions.
- `data/` — `CERT_O4_next14.json`, the stored Monte Carlo record.

The `v10a*` series is a record of **distinct experiments**, not drafts of one document — it was deliberately kept whole rather than version-pruned.

## What the next run must do (corpus §15.1 — all eleven, or it does not count)

1. Freeze the all-rank insertion coordinate and the `Y`-erratum.
2. Freeze the exact order-four occurrence schedule.
3. All `203 × 3 = 609` exact marked-cluster evaluations.
4. A rooted Möbius ledger **on the vacuum-subtracted object** (`H_eff` is not cluster-additive; `H_eff − eI` is).
5. Source, input, checkpoint, and output hashes.
6. **No historical scalar or shape target anywhere in the data flow.**
7. A cold 3,895-topology Stage-3H generation of an *unshifted* 189-record kernel.
8. `X`/`M` extraction with `λ_R = 2λ_M − λ_X` reserved as a **blind holdout**, then full Laurent-symbol equality.
9. An independent scalar ledger testing `q_band⁽⁴⁾ − E₀⁽⁴⁾ =? m_Γ⁽⁴⁾`.
10. The `W₂₂` order toggle across all 33 rooted classes.
11. **`m_Γ⁽⁴⁾` and `C⁽⁴⁾` from the same sealed run.**

⚠ The **3,895 Stage-3H topologies** and the **3,850 stable-rank trace topologies** are different inventories and must never be interchanged.

## Status

The marked-cluster engine passes its algebra and geometry preflights (self-test 47/47, geometry 609/609) but has produced **zero physics contractions**. It is the designated decider; it has not yet decided.

Related: `records/transcripts/15 hour RUN.txt` and `15 hour RUN. results.txt` control the August numerical adjudication.
