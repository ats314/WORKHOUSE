# WORKHOUSE Route A / Route B final hostile adjudication

**Date:** 2026-08-23  
**Verdict:** **PASS, strictly for the axial support-size-two direct-\(D\) claim.**  
**Full physical \(T_1\) bridge:** **INCOMPLETE by construction and correctly reported as such.**  
**Repository/implementation edits made by this review:** none.

## Bottom line

I found no blocking defect in the sealed claim that the canonical `xy` root,
input-polarization-2 direct contribution through support size two has an exact,
target-independent native calculation and an exact trace-to-native axial bridge.
Both routes give

\[
D^{(2)}_{\mathrm{direct,axial}}
=4\left(-\frac{44119723}{138858720}\right)
+8\left(-\frac{291514199}{964076256}\right)
=-\frac{31127086619}{8435667240}.
\]

That conclusion is deliberately narrow:

| claim | adjudication |
|---|---|
| Native physical-P/Q singleton direct \(D=-13/896\) | **PASS** |
| Native canonical input-polarization-2 row, all three output channels | **PASS** |
| Signed transport over all 12 nearest rooted placements | **PASS** |
| Trace-history to native physical-Haar quotient for the frozen axial component | **PASS** |
| Other two input-polarization rows / full \(3\times3\) \(T_1\) map | **NOT PROVED** |
| Fold and linked-vacuum terms | **NOT PART OF THIS SEAL** |
| Support size three or larger | **NOT PART OF THIS SEAL** |
| Total \(m_\Gamma\), C1, or C22 | **NOT PROVED OR PROMOTED** |

Route A's `2 x 2` matrices are endpoint-space matrices, not polarization-space
matrices. “All \(T_1\) channels retained” means all three **output** channels for
the one certified input row; it must not be read as a full \(3\times3\) result.

## 1. Route A: native physical-P/Q certificate

### Exact arithmetic and reconstruction

The calculator's executable input allowlist contains only the native engine,
the order-schedule guard, and the exact Haar tensor backend
(`work/native_pq_size2/native_pq_size2_exact.py:30-40,61-80`). It reconstructs
the singleton from the native character \(W_2/R_2\) construction
(`:199-227`), forms the complete native/tensor local maps and the pure-six
`729 x 729` integer tensors (`:361-436`), and fails closed unless the CRT
modulus product proves a unique lift beyond twice the numerator bound
(`work/native_pq_size2/exact_haar_tensor.py:437-480`). Binary floats are
rejected before output (`native_pq_size2_exact.py:1775-1790`).

The exact representative endpoint matrices are

\[
D_{\rm cop}=
\begin{pmatrix}
-\frac{8554053551}{26994135168} & -\frac{129523931}{8435667240}\\
-\frac{129523931}{8435667240} & -\frac{8554053551}{26994135168}
\end{pmatrix},
\]

\[
D_{\rm orth}=
\begin{pmatrix}
-\frac{8554053551}{26994135168} & \frac{129523931}{8435667240}\\
\frac{129523931}{8435667240} & -\frac{8554053551}{26994135168}
\end{pmatrix}.
\]

The canonical input-polarization-2 output rows and singleton-subtracted
increments are:

| geometry | output row `(0,1,2)` | support-size-two increment `(0,1,2)` |
|---|---|---|
| coplanar | `(0, 0, -184537657/555434880)` | `(0, 0, -44119723/138858720)` |
| orthogonal representative | `(0, 129523931/8435667240, -8554053551/26994135168)` | `(0, 129523931/8435667240, -291514199/964076256)` |

The independent verifier did not trust those stored matrices: it regrouped the
28 nonzero action-ledger records by endpoint, rebuilt the exact matrices, and
then independently regenerated all 12 affine cubic witnesses. The sign census
is four coplanar `+`, four orthogonal `+`, and four orthogonal `-`; the
off-polarization component flips with the orientation sign. The implementation
that emits these witnesses is at `native_pq_size2_exact.py:1537-1744`; the
independent result and its scope correction are documented at
`outputs/WORKHOUSE_NATIVE_PQ_SIZE2_INDEPENDENT_VERIFICATION_20260823.md:20-34,142-187`.

### Closure, rank, family, and poison gates

- The representative exact Krylov ranks are `8,16,24,24`; the joint physical
  block has rank `24`, \(E_0\)-nullity `2`, and bordered rank `26`. Exact closure,
  residual, and Hermiticity checks are implemented at
  `native_pq_size2_exact.py:1048-1192`.
- Runtime family census admits exactly the seven supported joint-moment
  families. Triality and allowlist checks are at `:531-549`.
- Poison calls reject `(2,5)` in the tensor contractor and `(7,1)` in the native
  engine; neither `(2,5)` nor `(5,2)` is contracted.
- The pure-six check compares the complete `729 x 729` tensors and establishes
  rank/trace `5` together with `native_numerator = 72 * tensor_numerator`.
- The \(W_{22}\) guard proves first appearance at order five and checks the exact
  order-five difference `-5/7168` (`:1747-1772`).

### Target/oracle/F07 leakage adjudication

There is no executable data path from F07, an oracle, a fitted target, a report,
a result JSON, or a transcript scalar into Route A's arithmetic. Four fresh
calculator executions—normal, `-O`, and both modes with an empty alternate
bytecode cache—produced byte-identical result JSON with SHA-256
`fac8cb8b957f967409243a28aac6c2f0712f096639dc4dfc1843230a50a1881b`.
F07 was opened by the **independent verifier only after** the native values and
hashes had been frozen; its later exact agreement is a cross-check, not an input.

Two source-text caveats are real but inert:

1. The loaded native engine contains a provenance filename with the word
   `DualColdOracle` at
   `DATA_SU3_Exact_MarkedCluster_m4_Colab.py:310`. Route A never accesses that
   `SOURCE_AUTHORITIES` entry, and it contains no scalar used by this path.
2. The loaded order-guard module has `-13/896` in the standalone `run()`
   regression at `DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:615`.
   Import does not execute `run()`. Route A calls
   `exact_one_face_w22_sensitivity()` but consumes only `o4_equal` and
   `o5_difference` (`native_pq_size2_exact.py:1747-1772`); its singleton is
   independently reconstructed by the character calculation.

Thus **runtime/dataflow independence is real**, while the stronger claim that
no loaded source text contains any target-adjacent word or dead diagnostic would
be false.

## 2. Route B: exact trace-to-native axial bridge

Route B independently passes the frozen axial component and deliberately fails
the full-\(T_1\) promotion. Its certificate status is
`EXACT_AXIAL_BRIDGE_PASSED_FULL_T1_INCOMPLETE`, with
`axial_component_passed=true`, `full_T1_bridge_passed=false`, and top-level
`passed=false`.

The exact gates establish:

- literal coordinate identity on 750 oriented-face constructors, both generated
  \(W\) stages, and raw \(H_0\) compatibility on 4,556 states;
- 924 physical-Haar quotient blocks, including 180 blocks whose formal residual
  dictionaries are nonempty but whose exact Haar norms vanish;
- mixed `(4,1)/(1,4)` Gram rank `3`, kernel `(-1,1,-1,1)`, and all four Penrose
  identities;
- complete pure-six `729 x 729` tensor equality, trace-basis rank `5`, native
  frame rank `5`, and native kernel dimension `5`;
- all 12 placements and exact `4+8` recombination;
- a full-unfiltered-versus-optimized support check over 74,013 residual classes
  and 16 endpoint channels at every placement; the formal maps are **not**
  literally equal, but their exact Haar-weighted residuals cancel to zero;
- 74,126 unique evaluated canonical pair payloads in the hash-chained checkpoint.

The residual calculation is therefore quotient equality, not an improper claim
that the pre-quotient formal dictionaries coincide. The relevant exact paths are
`work/trace_pq_isometry/certify_trace_pq_isometry.py:1175-1360,1690-2064`.

Route B scans the primitive input for forbidden result tokens, rejects binary
floats, and loads the generator, exact Haar contractor, and native engine as
pinned executable dependencies (`certify_trace_pq_isometry.py:1-143,2121-2159`).
No F07 class fraction, final axial scalar, oracle value, or transcript scalar
occurs in its arithmetic inputs. The phrase “only numerical input” should be
read as “only external numerical data file”: structural constants such as
\(E_0=8/3\) and the algebra live in the pinned executable sources. The primitive
also records source-document hashes for provenance; validation hashes those
documents but does not parse their numeric contents into the contraction.

The full-\(T_1\) refusal is explicit and correct. The frozen known-entry mask is
rank one, `diag(0,0,1)`; rank three is required and no cubic rotation
intertwiner is certified (`certify_trace_pq_isometry.py:2186-2225`). The script's
claim boundary expressly excludes the missing polarization rows, fold,
linked-vacuum, rooted full-\(T_1\), support size three and above, and total
\(m_\Gamma\) (`:2309-2321`).

The lightweight Route B verifier passed normally and under `-O` with
byte-identical `VERIFIED` output. It is a fail-closed **seal and consistency
verifier**, not an independent rerun of the expensive 74,126-pair contraction.
This review additionally streamed the checkpoint: all 74,126 rows and serialized
pair payloads were unique, its SHA-256 and chain tip matched the certificate, and
all ten entries in the outer manifest re-hashed against the live files.

## 3. Canonical-row and cubic-transport adjudication

Route A directly proves one input row—polarization 2—resolved across all three
output channels and all 12 rooted placements. That is sufficient for the
certified **axial diagonal support-size-two direct-\(D\)** scalar because the
exact aggregation selects the root-polarization increment and performs the
signed cubic `4+8` sum.

It is not sufficient for a full \(3\times3\) \(T_1\) operator. “The other rows
follow by cubic covariance” is a valid proposed route, not a completed
certificate, until an executable root-plane rotation/polarization intertwiner
is supplied. Route B independently reaches exactly this boundary and marks it
false rather than silently promoting it. Within this chain, that rotation
intertwiner is the earliest missing full-\(T_1\) gate; size-three support is the
next untested support only **after** keeping the claim axial/frozen-pol.

## 4. Three forensic corrections

These corrections concern historical display/provenance. None enters the sealed
Route A or Route B direct-\(D\) arithmetic.

### 4.1 Denominator factorization

The correct factorizations are

\[
83776=2^6\cdot7\cdot11\cdot17,
\qquad
837760=2^7\cdot5\cdot7\cdot11\cdot17.
\]

`C:\Users\Alex\Downloads\F07_VS_BLIND_TWOFACE_ADJUDICATION.md:97-100`
prints `83776 = 2^7*7*11*17^2`; that right-hand side is 34 times too large.
The rational linked-vacuum value `-327/83776` itself is unaffected, as is its
prime support; only the printed factorization was wrong.

### 4.2 Stale \(D+F\) float

The exact value is

\[
D_{\rm EXACT}+F
=-\frac{86634244910174898583}{7250590288602460800},
\]

whose correctly rounded binary64 value is `-11.948578179401377`. The historical
literal `-11.9485781794007` at
`work/WORKHOUSE-readonly/src/workhouse/constants.py:428` and
`15 hour RUN.txt:9112` is stale. Comparing the two rounded binary64 numbers gives
an absolute difference `6.767919558114954e-13`, exactly **381 representable
binary64 steps** at this magnitude. Therefore the statement at
`outputs/WORKHOUSE_RANK3_ORDER4_ORACLE_COUNTERFACTUAL_AUDIT_20260823.md:81-82`
that the exact value agrees with that stale literal “to its floating-point
precision” must not be retained.

### 4.3 Hamer comparison

The Hamer printout is a terminal, post-hoc comparison at reported decimal
precision—not an exact equality and not a computational input. The notebook
first obtains an authenticated exact fraction, then sets the external decimal
reference `Fraction('-0.0968932328773')`, constructs a half-width of
\(5\times10^{-14}\), and prints `HAMER_TERMINAL_MATCH_AT_REPORTED_PRECISION`
(`NB_O4_hodge_su3_exact_markedcluster_m4_colab.ipynb:1268-1292`). The engine's
corresponding diagnostic requires an already sealed candidate plus a
caller-supplied reference and is disabled by default
(`DATA_SU3_Exact_MarkedCluster_m4_Colab.py:6282-6299`).

The displayed coincidence must also not be overstated: four material printed
rows sum to the rounded Hamer display, while literally including all six printed
rows does not; the internal total is different again beyond the reported
rounding. No Hamer value feeds, shifts, fits, or selects the Route A/B result,
and no exact external normalization equality is established here.

## 5. Frozen hashes and verification boundary

### Route A

| artifact | SHA-256 |
|---|---|
| native calculator | `bc203ad16a7825f24dcff69fb69f8adf094a7d003639b6c2adce022ea1749014` |
| exact Haar backend | `dc275cf8076fbc56102f1d3d7c21e10d88fcc18d3b78b7ed0d79ab0f9e53b3f4` |
| result JSON | `fac8cb8b957f967409243a28aac6c2f0712f096639dc4dfc1843230a50a1881b` |
| supplied validator | `4b054011fe12239cd52715086b5f432e0c15e9d6afcc9a0feec76274120f6d33` |
| certificate report | `77f8b8acec75d51e1057ec6c1aeaa30cba7988c053f66afb80180a9ca13feece` |
| certificate bundle | `a5710adfdc298e598d6c1da8803554e544b343e6b41a4cc96476a9f4c90bbd02` |
| independent-verification report | `dd12c84a4de9e3e1c574ed08daff78c7ff8e5cd5d5e7c38f2ddc14b43a9380cc` |
| independent-verification bundle | `689a698ff0bdc0ff45b801d2116a45877b5e4838b416b52635e39d7677a43444` |
| supplied validation evidence, normal/`-O` | `334bf6a5b0a936e994246f6490859de10c67bcfcd7a15ffc1b37ac2a3dd2027c` |
| independent evidence, normal/`-O` | `cd2fcc1b50917f2538102bf6ddcd0dc4c4377829ef1053fe8c04b2d15ff7debe` |

No executable Route A calculator/backend/validator/verifier uses removable
Python `assert` checks; `-O` therefore does not erase its fail-closed gates.

### Route B

| artifact | SHA-256 |
|---|---|
| calculation script | `f16aceb0b21b7bbf76e36cbd2bb84d770c8ccaae9af6181d7e122f137ebb67c9` |
| certificate | `762e28a685da3625979138553c2e06aa270dccbd6485e91b83e15fb3eff485ba` |
| exact ledger | `20de5959575ab85513c3ce3a3d9763c5d2cd1d5c0ae7560f4f611151b81ded97` |
| hash-chained checkpoint | `ee294ff416ddc531ed082d8d2420179a89d243229ca366b550cf5044273586e6` |
| fail-closed seal verifier | `c37f96551aa3416f9eaa1eeda5e0b5d88ab40497e83639270b0da507c4f10dea` |
| public report | `5c165d35f70d7f74c1ea846f75360108327dd45534157758cd12c7339bc610aa` |
| ten-entry outer manifest | `16ab1f08ea158f44aa75eb8b989c9566382384afbed6032da29479b09c9046eb` |
| primitive specification | `3685369c951036765f940612114419e76e27dd4f9efe79112053a48abd1faa33` |
| trace generator | `a72a2c412bfa3a7da3847ac4fe04c48fb5e1d1db7f95ae4e391c1ea31ca306ce` |
| exact trace Haar contractor | `f944bfef52a2176de113d0ca66dd4d1c98ada7f4224ec3cccc8d4c4ae48b7e29` |
| native engine | `be9d77f5b245715ed6e4fe6dc9178a56ddfa5c68efe697eaa7cf4bb6adae27ad` |

No executable Route B calculator/verifier/dependency examined here uses
removable Python `assert` checks in its gate path. Normal and `-O` seal checks
are byte-identical. The expensive contraction was not recomputed during this
final adjudication; its sealed checkpoint, ledger, source logic, manifests, and
independent consistency checks were reviewed instead.

## Final adjudication

**No release-blocking defect remains for the exact axial/frozen-polarization,
support-size-two direct-\(D\) result.** The computation has meaningful
runtime/dataflow independence from the oracle/F07 target path, exact arithmetic,
complete 12-placement signed bookkeeping, fail-closed family/rank/residual
gates, and mutually consistent Route A and Route B values.

The seal must remain exactly where it is: it does **not** close the full
polarization intertwiner, full \(3\times3\) \(T_1\), fold, linked vacuum,
support size three and above, total \(m_\Gamma\), C1, or C22.
