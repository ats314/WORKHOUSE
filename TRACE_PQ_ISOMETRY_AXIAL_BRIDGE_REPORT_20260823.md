# Route-B exact trace-to-native P/Q bridge

## Verdict

**Axial/frozen-polarization bridge: PASS.**  
**Overall/full physical \(T_1\) bridge: INCOMPLETE.**

The exact transported size-two direct contribution is

\[
D^{(2)}_{\mathrm{direct,axial}}
= -\frac{31\,127\,086\,619}{8\,435\,667\,240}.
\]

The certificate status is `EXACT_AXIAL_BRIDGE_PASSED_FULL_T1_INCOMPLETE`, with `axial_component_passed=true`, `full_T1_bridge_passed=false`, and top-level `passed=false`. The false top-level field is intentional: the frozen source covers only polarization index 2, a rank-one subspace of the required rank-three \(T_1\) space.

## Exact gates closed

- The frozen `LXState(occ, part)` and native `State(occ, part)` map by literal coordinate identity. Constructor compatibility was checked on 750 oriented faces, raw \(H_0\) compatibility on 4,556 states, and both generated \(W\) stages.
- The physical Haar quotient was checked on 924 spectral blocks. Although 180 blocks have nonempty formal \(H_0\) residual dictionaries, all have exact zero Haar norm. Reduced-resolvent residuals vanish, and all 26 resonant blocks lie in \(P\) modulo the Haar kernel.
- For the mixed \((4,1)/(1,4)\) family, the exact Gram matrix has dimension 4, rank 3, and kernel `(-1,1,-1,1)`. The independently derived rational pseudoinverse satisfies all four Penrose identities.
- For the pure-six family, the trace and native formal delta expansions contain 488 and 456 terms respectively, reflecting \(N=3\) redundancy. Their complete `729 x 729` exact color tensors are identical. The trace basis has dimension/rank 5; the native frame has dimension 10, rank 5, and kernel dimension 5.
- All 12 rooted size-two placements were contracted. Each of 4 coplanar placements gives `-44119723/138858720`; each of 8 orthogonal placements gives `-291514199/964076256`. Their exact sum is the fraction above.
- Full supportwise contraction without a signature or energy filter was compared against the optimized matched contraction. Their raw formal maps differ, but their Haar-weighted difference is exactly zero on each of 12 placements and each of 16 endpoint channels.
- That exhaustiveness gate covered 74,013 residual canonical classes: 10,044 have individually zero Haar value and 63,969 have individually nonzero Haar value whose weighted contributions cancel exactly. The exact evaluator covered 74,126 unique canonical pairs in total.
- Every skipped `1 x 1` match had translated support-union cardinality one; zero size-two histories were excluded.

## Independence boundary

No F07 \(D\) value, prior Haar-result ledger, oracle, target, or transcript scalar was loaded. The only numerical input was the frozen rank-3/order-4 primitive JSON. The exact generator, Haar contractor, and native engine were executable code dependencies and are pinned in the companion checksum manifest. The Haar module was used only as the exact local contractor; no stored result scalar was consumed.

## Scope boundary

This proves transport of the **frozen axial-diagonal size-two direct \(D\)**. It does not prove the other two polarization components, a full \(3\times3\) \(T_1\) bridge, fold or linked-vacuum terms, a rooted full-\(T_1\) kernel, supports of size three or larger, or total \(m_\Gamma\). The earliest remaining gate is an executable cubic rotation/polarization intertwiner that raises certified endpoint coverage from rank 1 to rank 3.

## Sealed central hashes

- calculation script: `f16aceb0b21b7bbf76e36cbd2bb84d770c8ccaae9af6181d7e122f137ebb67c9`
- certificate: `762e28a685da3625979138553c2e06aa270dccbd6485e91b83e15fb3eff485ba`
- exact ledger: `20de5959575ab85513c3ce3a3d9763c5d2cd1d5c0ae7560f4f611151b81ded97`
- hash-chained checkpoint: `ee294ff416ddc531ed082d8d2420179a89d243229ca366b550cf5044273586e6`

The lightweight fail-closed verifier was run in normal and optimized (`-O`) modes; both emitted byte-identical `VERIFIED` output. The expensive 74,126-pair contraction was not rerun during sealing.
