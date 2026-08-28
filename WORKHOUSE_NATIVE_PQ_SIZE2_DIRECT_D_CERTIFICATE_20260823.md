# WORKHOUSE native physical P/Q size-two direct-D certificate

**Date:** 2026-08-23  
**Status:** **PASS**  
**Certificate schema:** `workhouse-native-physical-pq-size2-direct-D/v1`

## Result

The target-free native calculation closes the support-size-one and rooted support-size-two physical P/Q direct-D problem at order four. It uses the native trace-state generator and exact local SU(3) Haar contraction; it does not load the F07 D ledger, an oracle value, a fitted target, a transcript coefficient, or any JSON input.

The singleton result is

\[
D_{\{0\}}=\frac12\langle W_2,R_2\rangle=-\frac{13}{896}.
\]

For a coplanar pair, the exact endpoint matrix is

\[
D_{\mathrm{cop}}=
\begin{pmatrix}
-\frac{8554053551}{26994135168} & -\frac{129523931}{8435667240}\\
-\frac{129523931}{8435667240} & -\frac{8554053551}{26994135168}
\end{pmatrix}.
\]

For an orthogonal pair in the representative orientation, it is

\[
D_{\mathrm{orth}}=
\begin{pmatrix}
-\frac{8554053551}{26994135168} & \frac{129523931}{8435667240}\\
\frac{129523931}{8435667240} & -\frac{8554053551}{26994135168}
\end{pmatrix}.
\]

The canonical root source is the `xy` face, input polarization 2. Its full output-resolved row and its size-two increment after subtracting the singleton are:

| geometry | root row by output polarization `(0,1,2)` | rooted size-two increment `(0,1,2)` |
|---|---|---|
| coplanar | `(0, 0, -184537657/555434880)` | `(0, 0, -44119723/138858720)` |
| orthogonal representative | `(0, 129523931/8435667240, -8554053551/26994135168)` | `(0, 129523931/8435667240, -291514199/964076256)` |

The certificate explicitly transports that canonical input-polarization row to all 12 rooted neighboring placements. The four coplanar placements have relative C-odd orientation sign `+1`. The eight orthogonal placements split into four with sign `+1` and four with sign `-1`; the off-polarization component changes sign accordingly.

The diagonal/root-polarization axial combination is therefore

\[
4\left(-\frac{44119723}{138858720}\right)
+8\left(-\frac{291514199}{964076256}\right)
=-\frac{31127086619}{8435667240}.
\]

This last `4+8` number is a derived axial root-polarization projection. It is not a general scalarization of the output-resolved T1 row. In particular, orthogonal off-polarization terms remain channel-resolved until the full embedding/Möbius bookkeeping is applied.

## Exact closure gates

The following gates passed without binary floating-point arithmetic:

- The native one-face trace-state source maps isometrically to the exact character quotient. Native `W2` and the polynomial-H0 native `R2` give `-13/896`; the E0 component and resolvent residual have exact Haar norm zero.
- Pair and singleton histories are solved in one joint physical quotient. The Krylov rank sequence is `8, 16, 24, 24`, so closure occurs at depth 3 with physical rank 24, E0 nullity 2, and bordered-system dimension 26.
- All eight bordered equations per representative have exact zero equation residual and exact zero Q-constraint residual.
- Different-face singleton moments are zero by an executable maximal-tree/product-Haar certificate: each two-face graph is connected with cycle rank 2, each face has one distinct chord, every nonconstant character has zero Haar mean, and degrees 0 through 6 are covered.
- The exact Haar backend uses integer tensor contraction with bounded CRT. Every triality-compatible family actually encountered lies in the audited set `(0,3)`, `(0,6)`, `(1,1)`, `(2,2)`, `(3,0)`, `(3,3)`, `(6,0)`. No `(5,2)` or `(2,5)` family occurs; the maximum combined local occurrence count is 6.
- The tensor backend is exactly equivalent to the native local Haar projector. The pure-six gate compares the complete `729 x 729` integer color tensors, with rank and trace both 5 and exact identity `native_numerator = 72 * tensor_numerator`.
- The rejected first-membership cache optimization is retained as an explicit counterexample for each geometry. The production calculation uses the joint quotient instead.
- W22 is structurally excluded through order 4. The first closed order at which it enters is 5, where full-minus-pruned is `-5/7168`.

## Reproducibility and independence

The sealed script was run normally and with Python optimization enabled. The two JSON result files are byte-for-byte identical:

- byte length: `99,137`
- SHA-256 of each result: `fac8cb8b957f967409243a28aac6c2f0712f096639dc4dfc1843230a50a1881b`

The separate post-hoc validator was also run normally and with optimization enabled. It rejects floats, changed inputs, changed runtime files, false residual/rank gates, incomplete family coverage, invalid orientation witnesses, incorrect channel transport, and incorrect singleton subtraction.

Pinned sources:

| file | SHA-256 |
|---|---|
| `native_pq_size2_exact.py` | `bc203ad16a7825f24dcff69fb69f8adf094a7d003639b6c2adce022ea1749014` |
| `exact_haar_tensor.py` | `dc275cf8076fbc56102f1d3d7c21e10d88fcc18d3b78b7ed0d79ab0f9e53b3f4` |
| native marked-cluster engine | `be9d77f5b245715ed6e4fe6dc9178a56ddfa5c68efe697eaa7cf4bb6adae27ad` |
| order-schedule guard | `68782826d50ad6bcbb3a20d83649bfa7f66e42c5706d131361b7d189b1f99a8f` |
| `validate_native_pq_size2.py` | `4b054011fe12239cd52715086b5f432e0c15e9d6afcc9a0feec76274120f6d33` |
| validation JSON | `334bf6a5b0a936e994246f6490859de10c67bcfcd7a15ffc1b37ac2a3dd2027c` |

Runtime: Python 3.12.13, SymPy 1.14.0, NumPy 2.3.5. Their concrete paths and hashes are embedded in both the result and validation JSON.

Reproduction from the workspace root:

```powershell
& 'work/uv-cache/archive-v0/p5HMSCWIhZMzPNsKrqXNK/Scripts/python.exe' -B work/native_pq_size2/native_pq_size2_exact.py
& 'work/uv-cache/archive-v0/p5HMSCWIhZMzPNsKrqXNK/Scripts/python.exe' -O -B work/native_pq_size2/native_pq_size2_exact.py --output work/native_pq_size2/native_pq_size2_exact_result_optimized.json
& 'work/uv-cache/archive-v0/p5HMSCWIhZMzPNsKrqXNK/Scripts/python.exe' -B work/native_pq_size2/validate_native_pq_size2.py
```

## Interpretation boundary

This is an exact native certificate for direct D at support size one and rooted support size two, including one canonical input-polarization row resolved over all three output polarizations and its signed transport to all 12 placements. The other input-source rows follow by cubic covariance but were not separately enumerated by a root-plane rotation census.

It is not, by itself, a certificate for the complete embedded/Möbius `Gamma`, the fold and linked-vacuum terms, or the final total `m4`. The exact post-freeze agreement with the frozen F07 direct-D values is nevertheless substantive: those values are reproduced from the native P/Q and Haar construction without being supplied as inputs.
