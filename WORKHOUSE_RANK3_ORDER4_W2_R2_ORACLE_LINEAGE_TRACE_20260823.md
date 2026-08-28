# Rank-3/order-4 W2/R2 oracle-lineage forensic trace

Date: 2026-08-23  
Scope: frozen rank-3, order-4 cubic `T1+-` W2/R2 history and the final exact-Haar package  
Mode: read-only source and artifact audit; no repository source was changed

## Bottom line

The runtime/dataflow independence claim is real:

> The frozen W2/R2 generator and exact endpoint-Haar contraction do not consume
> `M4_ORACLE`, `ax_rest`, `local_shift`, the fitted diagonal, or the
> `-11.068479...` scalar. The exact Haar route genuinely regenerates
> `-11.068479463778765...` without the later diagonal fit.

The stronger independence claim is not established:

> This is a target-known exact replay of the v10a.7/v10a.20 scalar construction,
> not a prospectively blind derivation that this construction is the canonical
> physical fourth-order coefficient. The package pins historical v10a.20 census
> values and its source hash, and it supplies separately certified fold and
> linked-vacuum constants. Those choices do not numerically encode the final
> scalar, but they do preserve design/provenance dependence on the same lineage.

The proposed two-way fork therefore resolves as follows:

1. **“The frozen W2/R2 diagonal already carries `local_shift`” — false.** There
   is no fitted diagonal in W2/R2, and the late `local_shift` is downstream.
2. **“The exact Haar route produces `-11.0685` without diagonal fitting” — true.**
   It exactly certifies the older direct-history/fold/linked-vacuum prescription.

This does **not** by itself remove the physical-identification quarantine. It
removes the numerical-rationalization objection to that prescription.

## 1. The premise requiring correction

The preserved v10a.24c source distinguishes three different quantities:

- `M4_ORACLE = float(totals[4])` at
  `work/WORKHOUSE-readonly/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:7309`;
- `M4_SHORTCUT = -160506019419340168451/14501180577204921600` at
  `...ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:7310`;
- `ax_rest = V23_AXIAL_SHAPE['rest_direct']` and
  `local_shift = M4_ORACLE - ax_rest` at
  `...ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:7322-7326`.

The source first compares the oracle to the shortcut at lines 7314-7320. It
then adds `local_shift` only to the three anchor diagonals at lines 7325-7326
and gates the resulting rest against **`M4_ORACLE`**, not against the shortcut,
at lines 7335-7336.

The repository's authority layer records the same distinction:

- `M_GAMMA_4_NUM = -0.7751458630189173` in
  `work/WORKHOUSE-readonly/src/workhouse/constants.py:203-214`;
- `QUARANTINED_SCALAR = -160506.../...`, raw folded rest
  `-11.9485781794007`, and the actual applied shift
  `11.17343231638178` in `.../constants.py:426-435`;
- the invariant explicitly says the final equality is target-derived and hence
  not an independent verification in
  `work/WORKHOUSE-readonly/src/workhouse/invariants.py:414-422`;
- ADR 0002 makes the same separation in
  `work/WORKHOUSE-readonly/docs/decisions/0002-anchoring-is-not-a-dispute.md:50-57`.

Therefore the late fit forces approximately `-0.775145863`, not
`-11.068479464`. The latter existed earlier and is merely loaded for comparison
after the oracle unblind.

## 2. Exact W2/R2 runtime dataflow

The primitive manifest fixes the physical/combinatorial scope, not a scalar
answer:

- rank 3, order 4, periodic `L=5`, sector `T1+-`, polarization index 2, and two
  magnetic steps: `work/rank3_order4_cubic_ledger/primitive_rank3_order4_cubic.json:3-14`;
- exact electric/Fierz/fusion primitives: `...primitive_rank3_order4_cubic.json:16-33`;
- local Haar denominators: `...primitive_rank3_order4_cubic.json:36-43`;
- bilinear prefactor and the exact one-face recurrence input matrices:
  `...primitive_rank3_order4_cubic.json:45-59`;
- explicit completeness claims including no float reconstruction and no target
  coefficients in generation inputs: `...primitive_rank3_order4_cubic.json:61-70`.

The generator's executable path is local exact arithmetic:

- its module contract excludes NumPy, SymPy, `limit_denominator`, tolerance
  fallbacks, and imported repository code:
  `work/rank3_order4_cubic_ledger/ledger_generator.py:1-12`;
- source documents in the primitive manifest are only existence/SHA checks;
  their code is not imported or evaluated:
  `.../ledger_generator.py:344-357`;
- the SU(3) electric action and exact spectral projector are implemented at
  `.../ledger_generator.py:516-568`;
- the projected plaquette action is implemented at
  `.../ledger_generator.py:700-751`;
- the scaled charge-odd source is literally the `+1/-1` pair at
  `.../ledger_generator.py:754-760`;
- `W=-M` and the reduced resolvent are implemented at
  `.../ledger_generator.py:763-809`;
- the complete history path is
  `source -> W1 -> R1 -> W2 -> R2` at
  `.../ledger_generator.py:1199-1213`;
- the frozen history is serialized only after that build at
  `.../ledger_generator.py:1285-1341`.

The target-audit code is a separate subcommand. `generate` calls `generate(...)`
while `audit` calls `audit_targets(...)` only after an existing freeze is
verified: `.../ledger_generator.py:1541-1608` and `:1653-1675`. No target value
can flow backward from that audit into the frozen W2/R2 history.

A scoped search across the primitive manifest, generator, contractor, package
builder, verifier, and independent-Haar sources found no occurrence of
`M4_ORACLE`, `ax_rest`, `local_shift`, `K4_mass`, or `M4_SHORTCUT`. The exact
shortcut numerator itself occurs in output/corpus records, not in the W2/R2
generator or endpoint contractor source.

## 3. Frozen hash chain

The final frozen chain is:

| stage | SHA-256 / count |
|---|---|
| raw primitive JSON file | `3685369c951036765f940612114419e76e27dd4f9efe79112053a48abd1faa33` |
| canonical parsed primitive content recorded by freeze | `2eda6c8940280d269e27983800d8f51d9cc51dc27735ef71823dfff37b1362ab` |
| final W2/R2 generator | `a72a2c412bfa3a7da3847ac4fe04c48fb5e1d1db7f95ae4e391c1ea31ca306ce` |
| final freeze file | `e68d515899f03d1a84a028645b2f42e176bb0bb54c3b21be8be030da41f1dc26` |
| W2/R2 history ledger | `543869b10f5137ea74fbd5f27d25027dea66f936ce9844b77a029453b8bf8c97` |
| history records | 164,662 = 82,384 W2 + 82,278 R2 |
| exact endpoint-Haar contractor | `f944bfef52a2176de113d0ca66dd4d1c98ada7f4224ec3cccc8d4c4ae48b7e29` |
| exact topology ledger, gzip | `48abeca47d51993b05a9b297b20656af3dfed3aaf4d857eac1f466d073c2a662` |
| exact topology ledger, canonical uncompressed | `a7f13ca19eb675ec4340f1664ec04a49979a5cb9e8e95dbb59272b69fa2bb2dd` |
| final exact summary | `d3d2cb899966eef88e87f8bdc5216772a26a9620d6d77fce0b6341b67c87d9c7` |

The final freeze records the matching primitive, generator, and history hashes
in
`work/rank3_order4_cubic_ledger/canonical_run_final_20260823/rank3_order4_cubic_freeze.json`.
The exact-Haar summary binds the same history hash and the contractor hash in
`work/rank3_order4_exact_haar_run/rank3_order4_exact_haar_summary.json:1`.

The primitive manifest also pins three provenance documents:

| provenance source | SHA-256 |
|---|---|
| exact one-face preflight | `68782826d50ad6bcbb3a20d83649bfa7f66e42c5706d131361b7d189b1f99a8f` |
| v10a.20b historical algorithm notebook | `47c6ccc18079c49416c511c2a27a9d757525d6e279992514ed63f5ba413530fd` |
| denominator-lift evidence-boundary audit | `7332bf8363a13a44f329fca3d96d75584bc41447032906d5a7ae371889f4daf5` |

These bindings are declared at
`.../primitive_rank3_order4_cubic.json:81-99` and enforced by SHA only at
`.../ledger_generator.py:344-357`.

## 4. Census values inherited from v10a.20

There is real target-known structural pinning, but it is census pinning, not
scalar injection.

The v10a.20b notebook's single code cell (notebook cell index 1; described as
“cell 2” in the corpus audit) computes and gates:

- 5,400 matched H0 blocks, 3,597 whole-block orbits, raw upper bound 9,814,138,
  and 54 skipped one-face matches at source lines 6315-6346;
- 1,829,147 pair occurrences and 117,161 nonzero canonical topologies at source
  lines 6348-6371.

The new exact generator copies three of those as structural regressions:

```text
matched_h0_blocks      = 5,400
raw_pair_upper_bound   = 9,814,138
skipped_one_face       = 54
```

See `work/rank3_order4_cubic_ledger/ledger_generator.py:1215-1231`.

The exact-Haar contractor additionally pins 2,468,250 compatible state pairs
and 117,161 historical orientation-sensitive topologies at
`work/rank3_order4_cubic_ledger/exact_haar_sum.py:35-41`; its older orientation-
sensitive collapse also gates 3,597, 1,829,147, and 117,161 at lines 218-272.
The final unordered contraction independently produces and gates 69,800
classes at lines 276-368. The replay verifier gates 69,800/117,161 at
`work/rank3_order4_cubic_ledger/verify_exact_haar_ledger.py:17-35`.

One nuance matters: the production `run()` calls the unordered collapse at
`.../exact_haar_sum.py:957-959`. In that route, 69,800 and 2,468,250 are
recomputed and checked; 117,161 is carried as the historical orientation-
sensitive reference rather than recomputed by the production sum. The unused
older collapse function is the code path that can recompute and gate 117,161.

None of these integers is used in the scalar sum. They appear only in equality
checks that raise on drift. The actual numerator path uses each regenerated
pair's exact `weight`, independently computed exact `haar`, and the factor
`1/2`: `.../exact_haar_sum.py:1000-1037`. The final rational is constructed
from the accumulated integer numerator at lines 1073-1080.

So the correct assessment is:

- **not numeric target leakage:** changing an expected count can only make the
  program pass or fail; it cannot steer the accumulated numerator toward
  `-11.0685`;
- **yes design/provenance coupling:** the accepted construction and its
  regression envelope were chosen with the historical v10a.20 behavior known.

## 5. Where the shortcut is actually assembled

The exact contractor first verifies and regenerates the frozen history:
`work/rank3_order4_cubic_ledger/exact_haar_sum.py:935-955`. It then collapses
the regenerated W2/R2 pairs at lines 957-971. The sum is

```text
D_EXACT = D11 + (1/2) * sum(weight_scaled * exact_endpoint_Haar)
```

as recorded at `.../exact_haar_sum.py:1135-1148`.

The exact result is

```text
D_EXACT = -361008126292641364183 / 7250590288602460800
```

Only after `D_EXACT` is accumulated does the contractor add the separately
certified constants

```text
FOLD_EXACT          =  5315003 / 140454
LINKED_VACUUM_EXACT = -1474623 / 1675520
```

declared at `.../exact_haar_sum.py:601-608`. Their integration is explicitly
downstream at lines 1073-1088:

```text
m4_rest_exact = D_EXACT + FOLD_EXACT - LINKED_VACUUM_EXACT
              = -160506019419340168451
                / 14501180577204921600
              ~= -11.068479463778765.
```

The fold and linked-vacuum values are not fitted to the final scalar in this
contractor, but neither are they derived inside the 69,800-topology Haar loop.
They are supplied as exact constants bound to separate reproducer/package
hashes at lines 606-608 and reported at lines 1145-1154. That is another
provenance boundary, not an oracle edge into W2/R2.

## 6. Earliest direct-scalar lineage predates `local_shift`

The earliest clear implementation of this scalar route in the preserved source
lineage is

`work/WORKHOUSE-readonly/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py`

with SHA-256
`dc9ddfaab437ad4478c85eb631ed0319699c3e3304bd83b22bd31fc2f1f1107d`.

Its call flow is already the same conceptual construction:

- projected plaquette `W=-M` action: lines 4548-4596;
- normalized charge-odd face source: lines 4599-4614;
- reduced resolvent: lines 4652-4679;
- support-labelled `W` and `R`: lines 5483-5508;
- `S0 -> W1L -> R1L -> W2L -> R2L`: lines 5574-5589;
- direct moment `D=<W2|R2>`: lines 5602-5624;
- exact fold `-e2*N+J`: lines 5646-5653;
- marked linked-vacuum subtraction and blind candidate:
  lines 5687-5707;
- only after all gates, optional unblinding: lines 5720-5747.

The source explicitly says no historical fourth-order mass is supplied at
lines 5181-5182 and again at line 5707. This route therefore predates the later
v10a.23/v10a.24 `local_shift` branch.

## 7. What v10a.20 adds—and the design caveat

The primitive manifest pins the v10a.20b notebook as historical algorithm
provenance. That notebook's code cell contains:

- exact SU(3) energy/fusion: source lines 4373-4391;
- projected action: 4595-4615;
- source construction: 4638-4653;
- labelled W/R history: 6041-6080;
- exactified W2 and derived R2: 6245-6310;
- the pair census: 6315-6371;
- Haar denominator/QBOUND construction: 6382-6433;
- `D_EXACT` construction: 6668-6672.

Crucially, the prior numerical target appears only **after** the exact D
accumulation: `D_PREV=-49.790...` at source lines 6674-6678. The notebook then
loads exact fold and linked terms, forms `M4_EXACT`, and only afterward defines
`M4_PREV=-11.068...` for a comparison at source lines 6680-6688.

This proves dataflow separation inside that cell. It does not make the overall
research design blind: the expected scalar and census were known when the
algorithm and regression gates were frozen. The corpus's own F07 audit states
that its exactness was conditional on the recovered history and that the old
notebook had no immutable completed artifact:
`work/WORKHOUSE-readonly/corpus-import/records/audits/07-denominator-lift.md:69-78`.
The new package materially improves that boundary by replacing float
rationalization with exact generation and by freezing the history/topology
ledgers, but it still evaluates the selected historical prescription.

## 8. Corrected scalar flow

```text
exact primitives
  -> exact source/W1/R1/W2/R2
  -> exact endpoint-Haar D
  -> add exact Q1 fold
  -> subtract exact attached linked vacuum
  -> -11.068479... shortcut

later, separate v10a.23/v10a.24 branch:
blind full construction
  -> ax_rest ~= -11.948578...
  -> independent finite-cluster M4_ORACLE ~= -0.775145863...
  -> local_shift = M4_ORACLE - ax_rest ~= +11.173432316...
  -> shifted final rest = M4_ORACLE by construction
```

There is no arrow from the second branch's `M4_ORACLE` or `local_shift` back
into the first branch's W2/R2 history or exact Haar numerator.

## 9. Forensic verdict and next discriminant

### Verdict

- **Runtime/dataflow independence:** established.
- **Independence from the late diagonal fit:** established.
- **Exactness of D relative to the frozen W2/R2 construction:** established by
  the package's exact arithmetic and immutable ledgers.
- **Exactness of final shortcut assembly:** established relative to the frozen
  D plus the separately certified fold/linked constants.
- **Prospective blindness/design independence:** not established.
- **Identification with the physical fourth-order Gamma coefficient:** not
  established; the later finite-cluster value is approximately
  `-0.775145863`, not `-11.068479464`.

### Consequence

Do not retain the claim that `local_shift` created `-11.0685`; the preserved
code disproves it. Also do not promote `-11.0685` merely because its arithmetic
is now exact. The strongest defensible statement is:

> The exact package independently verifies, at the arithmetic/dataflow level,
> the old direct-history plus fold minus attached-vacuum scalar prescription.
> Its remaining uncertainty is the physical/operator identity of that
> prescription, not its rational arithmetic.

### The next decisive question

Prove or refute, from a target-free canonical Schrieffer-Wolff/linked-cluster
construction, the operator identity

```text
D11 + (1/2)<W2,R2> + fold - attached_vacuum
    = canonical vacuum-subtracted order-4 Gamma coefficient.
```

That bridge—not another Haar numerator replay—is what decides whether the
quarantined shortcut is physically complete or an exact artifact of a selected
restricted prescription.
