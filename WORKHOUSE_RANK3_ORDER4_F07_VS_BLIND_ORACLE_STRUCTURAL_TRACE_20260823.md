# WORKHOUSE rank-3/order-4: exact F07 versus blind linked-cluster oracle

Date: 2026-08-23  
Scope: read-only provenance and structural audit; no repository file was changed

## Executive verdict

The new exact-Haar package establishes a real and important fact:

\[
m_{4,\mathrm{F07}}
=D_{\mathrm{EXACT}}+F-V_{\mathrm{link}}
=-\frac{160506019419340168451}{14501180577204921600}
\approx -11.068479463778765
\]

is produced by a target-independent exact evaluation of the frozen F07 formula. It is not created by `local_shift`, and it is no longer defensible to describe it as merely a float-reconstruction artifact or as “rejected by both sides.” The exact result and its components are recorded in `work/rank3_order4_exact_haar_package_verify/WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md:9-40`; the exact 69,800-class ledger and CRT uniqueness proof are at `:42-55,57-91,93-126`.

That does **not** yet identify this number with the canonical physical fourth-order gap. The exact package closes the arithmetic of one historical F07 branch. It does not prove that the frozen global trace-history formula is equivalent to the prescribed physical-P/Q, rooted linked-cluster, full-T1 calculation.

The blind linked-cluster result remains

\[
m_{4,\mathrm{blind}}=-0.7751458630189173,
\]

as recorded at `work/WORKHOUSE-readonly/corpus-import/records/transcripts/15 hour RUN.txt:10619-10640`. The genuine unresolved conflict is therefore **exact F07 branch versus blind linked-cluster branch**, not the old `q_band` versus `m_Gamma` naming issue.

The most useful new localization is exact: the one-face contribution agrees between the branches. Consequently, the discrepancy begins in the multi-face sector.

## 1. The one-face sector agrees exactly

The exact F07 replay starts its direct sum with

\[
D_{11}=-\frac{13}{896},
\]

confirmed by the independent verifier at `work/rank3_order4_exact_haar_package_verify/WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md:124-126`. The exact marked-vacuum replay gives the one-face vacuum coefficient

\[
e_{4,\mathrm{vac}}^{(1)}=-\frac{39}{1280},
\]

at `work/fold_linked_exact/README.md:21-27`. Therefore the one-face gap coefficient is

\[
D_{11}-e_{4,\mathrm{vac}}^{(1)}
=-\frac{13}{896}+\frac{39}{1280}
=\frac{143}{8960}
=0.015959821428571\ldots .
\]

The blind rooted oracle prints exactly that value for its size-one contribution: `size 1 ... c4=+0.0159598214286` at `work/WORKHOUSE-readonly/corpus-import/records/transcripts/15 hour RUN.txt:10619-10626`.

This rules out the following as explanations of the split at the local root level:

- the sign of the magnetic interaction;
- the local source normalization used internally by the two branches;
- the analytic one-face direct term;
- the one-face vacuum subtraction.

The first numerical disagreement must occur among connected clusters of size at least two, or in their P-return/fold/incidence accounting.

## 2. Earliest implementation fork: state space and order schedule

### Exact F07 branch

The new package fixes one axial polarization (`polarization_index = 2`) and two magnetic steps per half-history in `work/rank3_order4_cubic_ledger/primitive_rank3_order4_cubic.json:3-14`. It then constructs

```text
source -> W1 -> R1 -> W2 -> R2
```

with exact rational trace states and exact supportwise removal of the resonant plaquette band; see `work/rank3_order4_cubic_ledger/ledger_generator.py:1199-1215` and the exact P0 certificate at `:910-963,1250-1261`. The fourth-order direct scalar is the exact bilinear of the two-step histories; no `Q2 -> Q2` matrix block is constructed.

### Blind finite-cluster branch

The blind branch explicitly stops using the F07 W/R coefficients for the scalar. It retains them only as a support census, then recomputes each raw cluster coefficient from a restricted Hamiltonian, a des-Cloizeaux one-particle block, and a separately diagonalized vacuum; see `work/WORKHOUSE-readonly/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6767-6777`.

Its cluster-local basis is built as P, `W(P)=Q1`, and `W(Q1)=Q2` at `:6848-6889`. It then applies `W` to **every** retained basis vector and projects onto every compatible retained row at `:6894-6899`. Because no layer mask is applied, that dense matrix contains `Q2 <-> Q2`, i.e. `W22`.

This is the earliest definite structural mismatch. The selected fourth-order route is

```text
P -> Q1 -> Q2 -> Q1 -> P,
```

while `W22` adds a fifth magnetic step. The order trace and the later `(2,5)` failure are documented at `work/WORKHOUSE-readonly/corpus-import/records/audits/06-pattern-2-5-runtime-forensics.md:50-76`.

This fact must be interpreted carefully: exact perturbative power counting places the first `W22` contribution at fifth order, so the mere presence of the block does **not** prove that it changed the true fourth-order Taylor coefficient. The v10a24c implementation, however, diagonalizes at finite `u` and extracts coefficients using a degree-six fit on 13 points (`ENGINE...v10a24c...py:6928-6946`). An exact order-truncated `W22`-off comparison is therefore required before the blind fourth-order scalar can be promoted. The current canonical architecture avoids the ambiguity by making `W22` impossible at order four.

### Prescribed canonical branch

The prescribed computation is neither of the preceding representations. It requires explicit physical P/Q1/Q2 states, typed block identity `(canonical joint irrep, exact H0 energy, canonical center flux)`, `B B^T=K` and `B12` witnesses, an order-aware schedule with no `W22`, and canonical Hermitian SW/BCH; see `work/WORKHOUSE-readonly/corpus-import/records/audits/03-unified-proposal.md:17-27,134-143,153-161`.

The exact F07 trace-vector calculation may ultimately be equivalent to that quotient for the direct scalar, but the new package does not supply the equivalence map or the physical-Q witnesses. The blind cluster-local Gram/Krylov basis supplies a third representation. Neither equality of representations has been certified.

## 3. Rooted Möbius treatment: what is and is not wrong

The blind v10a24c source gets the formal ordering right:

1. It constructs the one-particle effective block and subtracts the independently computed vacuum energy in the raw cluster gap at `ENGINE...v10a24c...py:6928-6932`.
2. Its canonical shape key keeps the marked root as a separate field, preventing the old unrooted-cache collision, at `:7105-7128`.
3. It downward-closes the rooted connected-cluster poset at `:7223-7255`.
4. It subtracts every proper rooted connected subcluster only after the raw gap has been formed, at `:7283-7289`.

Accordingly, the discrepancy should **not** be attributed to applying Möbius inversion to raw `H_eff` before vacuum subtraction. That particular suspected error is absent in v10a24c.

The exact F07 package has the opposite limitation: it has no rooted Möbius ledger to compare with this calculation. Its exact pair-collapse routine uses the W2/R2 support labels to identify and skip the separate one-face term, but then aggregates by relabelled endpoint trace states alone; see `work/rank3_order4_cubic_ledger/exact_haar_sum.py:276-368`. The canonicalization explicitly renames physical links and forgets lattice geometry at `:81-111`. Thus the 69,800 rows preserve the total Haar scalar but do not retain the marked support/subcluster data needed to reconstruct rooted incidence weights.

The exact fold/vacuum package states this boundary directly: it closes the historical Gamma-scalar Q1 fold and local marked-vacuum subtraction, but does not replace the unrun full-T1 609-cluster adjudicator (`work/fold_linked_exact/README.md:59-64`).

## 4. The inventories are different objects

The counts must not be treated as competing enumerations of one corpus:

| Branch | Stored/computed inventory | What it represents |
|---|---:|---|
| Exact F07 | 117,161 orientation-sensitive endpoint-Haar keys, losslessly quotiented to 69,800 unordered contraction classes | A scalar contraction of the frozen global W2/R2 formula |
| Blind linked cluster | 203 concrete rooted clusters, 33 rooted shape classes, one default polarization | A numerical cluster-gap/Möbius scalar |
| Canonical marked calculation | `203 x 3 = 609` marked evaluations | All three T1 polarizations with marked support retained |
| Canonical Stage 3H | 3,895 exact topology records, including the formerly missing 2,417 folded cases | The unshifted 189-record full-T1 H4 kernel |

The F07 counts and exact result are at `work/rank3_order4_exact_haar_package_verify/WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md:42-55,65-75`. The blind 203/33 result is at `work/WORKHOUSE-readonly/corpus-import/records/transcripts/15 hour RUN.txt:10743-10750`. The 609 and 3,895 requirements, and the fact that the marked engine has produced zero physics contractions, are at `work/WORKHOUSE-readonly/corpus-import/programs/hodge_o4_adjudication/README.md:27-45`. The corpus audit explicitly warns that F07, rooted-support, rooted-cluster, and Stage-3H inventories are not interchangeable at `work/WORKHOUSE-readonly/corpus-import/records/audits/02-duplication-report.md:41-49`.

There is currently no termwise map

```text
69,800 F07 Haar classes
    <-> 203/609 rooted marked-cluster weights
    <-> 3,895 Stage-3H amplitudes
    -> unshifted 189-record kernel.
```

That missing crosswalk, not arithmetic precision, is now the decisive issue.

## 5. Normalization is not the internal source of the split

The exact direct, fold, and linked-vacuum packages all use the same declared convention `H = H0 - u M`; see `work/fold_linked_exact/README.md:8-19`. The exact one-face equality above further shows that the blind and F07 branches agree locally in their internal `u` convention.

What remains open is the **external** bridge from the source variable to canonical `u`, particularly the conversion used to compare with Hamer. The audit states that this normalization remains an assumption at `work/WORKHOUSE-readonly/corpus-import/records/audits/05-latest-run-forensics.md:60`. Therefore the blind value's Hamer agreement is conditional evidence, not a completed physical normalization certificate. This issue affects external interpretation, but it does not explain the internal F07-versus-blind difference.

## 6. What the new exact package closes

Relative to the historical F07 audit, the new package closes all of the following for the frozen branch:

- exact symbolic W2/R2 generation, replacing `limit_denominator` recovery;
- exact supportwise P0 cancellation before resonant exclusion;
- exact evaluation of every endpoint Haar class rather than a sampled alternate check;
- a rigorous CRT uniqueness interval for each modular numerator;
- the full `D_EXACT` integer sum and denominator-divisibility gates;
- target-free exact replays of the previously literal fold and linked-vacuum addends;
- immutable topology rows, hashes, and an independent full-ledger verifier;
- computational independence from `M4_ORACLE`, `M4_SHORTCUT`, `local_shift`, and the historical target rational.

The result and boundary are summarized at `work/rank3_order4_exact_haar_package_verify/WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md:9-40,42-55,57-91,93-160`; target independence of the fold and vacuum replayers is at `work/fold_linked_exact/README.md:36-48`.

The package therefore proves this narrow proposition:

> Under the frozen exact F07 trace-history formula and its declared normalization, the fourth-order scalar is exactly `-160506019419340168451/14501180577204921600`.

## 7. What it still does not close

It does not yet prove:

- that the frozen F07 trace-history formula is the canonical physical-P/Q1/Q2 Hermitian SW/BCH coefficient;
- a typed physical-Q quotient or `B B^T`/`B12` completeness witness;
- rooted linked-cluster equality in the multi-face sector;
- an exact 609-evaluation marked-cluster ledger;
- the distinct 3,895-record Stage-3H corpus;
- an unshifted exact 189-record full-T1 kernel;
- the off-axis `C` coefficient or the full Laurent symbol;
- the source-variable-to-canonical-`u` normalization bridge.

The exact package's own boundary says that it closes arithmetic assembly for the frozen scope, not the separate operator-construction and physical-interpretation obligations (`WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md:158-160`).

## 8. Required status amendments

### C1: split the resolved naming issue from the newly genuine branch conflict

Keep C1's narrow resolution that `q_band^(4)` and `m_Gamma^(4)` are differently anchored coordinates; that statement is at `work/WORKHOUSE-readonly/ledger/contradictions.yaml:8-25` and is unaffected by the exact F07 result.

Amend the third quantity at `work/WORKHOUSE-readonly/ledger/contradictions.yaml:36-40`. The value `-11.068479463778765` should no longer be labeled `rejected-by-both`. Recommended status:

```text
label: exact F07-branch fourth-order scalar
arithmetic_status: exact and independently replayed
physical_status: audit-pending / not promoted
quarantine_reason: no canonical physical-Q/rooted/Stage-3H equivalence certificate
```

Create a separate open contradiction or sub-entry:

```text
exact F07 branch:        -11.068479463778765...
blind linked-cluster:     -0.7751458630189173
status: open pending exact multi-face rooted crosswalk and canonical run
```

Likewise, retain `QUARANTINED_SCALAR` as a production quarantine but change its metadata from `falsified` / `rejected by both sides` at `work/WORKHOUSE-readonly/src/workhouse/constants.py:426-435,649-655` to `exact historical branch; physical identification audit-pending`.

The C1 statement that the blind value is substantive external validation (`contradictions.yaml:49-54`) should be qualified as conditional on the unproved normalization bridge and on rehabilitation by the canonical state/order/inventory calculation.

### C22: no change

C22 remains correctly resolved. In the blind/hybrid source, `local_shift = M4_ORACLE - ax_rest` is added to the diagonal and the shifted rest is then gated against `M4_ORACLE`; see `ENGINE...v10a24c...py:7322-7337`. That gate is bookkeeping by construction, exactly as stated at `work/WORKHOUSE-readonly/ledger/contradictions.yaml:272-278`.

The exact F07 package independently producing `-11.068479...` does not make Gate 85 independent and does not validate the shifted 189-record kernel. It rehabilitates the provenance of the F07 scalar, not the evidentiary meaning of C22's equality.

## 9. Sharpest next adjudication

The cheapest decisive next step is not another global scalar recomputation. Preserve the root, concrete support, polarization, order layer, and coefficient role **before** the F07 pair-collapse erases them, then compute an exact rooted decomposition of the same F07 formula.

Start with two-face rooted clusters because the one-face sector is already proven equal. Compare exact F07 two-face weights with the blind aggregate printed as

```text
size 2: c4 = -0.403971702978
```

at `work/WORKHOUSE-readonly/corpus-import/records/transcripts/15 hour RUN.txt:10620-10622`. If they disagree at size two, trace the difference separately through direct Q2 return, P-return/fold, and vacuum terms. If they agree, continue through sizes three to six. The calculation must:

1. consume exact typed physical P/Q1/Q2 blocks or prove an exact isometry from the trace-history representation;
2. make `W22` unschedulable at order four;
3. subtract the exact vacuum before rooted Möbius inversion;
4. retain all three T1 polarizations;
5. map the resulting marked weights to the 3,895 Stage-3H records and assemble the unshifted 189-record kernel.

That is the shortest route from “two exact/numerical branch values” to a genuine physical adjudication.
