# WORKHOUSE rank-3, order-4 exact Haar and final scalar audit

Date: 2026-08-23  
Scope: Hamiltonian SU(3), periodic cubic `L=5`, `T1+-`, polarization index 2, two magnetic insertions per half-history  
Repository status: read-only; no repository file was changed

## Result

The frozen exact `W2/R2` history has now been contracted through the endpoint SU(3) Haar integral without floating-point reconstruction. The direct scalar is

\[
D_{\mathrm{EXACT}}
=-\frac{361008126292641364183}{7250590288602460800}
\approx -49.79017044448461.
\]

The independently replayed fold and linked-vacuum terms are

\[
F=\frac{5315003}{140454},\qquad
V_{\mathrm{link}}=-\frac{1474623}{1675520},
\]

so

\[
F-V_{\mathrm{link}}
=\frac{268015015453}{6921573120}
\]

and

\[
m_{4,\mathrm{rest}}
=D_{\mathrm{EXACT}}+F-V_{\mathrm{link}}
=-\frac{160506019419340168451}{14501180577204921600}
\approx -11.068479463778765.
\]

No historical decimal or target rational was used to construct `D_EXACT`.

## Exact topology ledger

The historical collapse has 117,161 nonzero orientation-sensitive keys. Joint physical-link relabelling and the exact symmetry of the Haar inner product under exchanging its two arguments reduce these losslessly to 69,800 fully unordered contraction classes. The exact weights are aggregated before Haar evaluation, so this quotient changes neither the sum nor any coefficient.

The final compressed ledger contains all 69,800 classes. Every row embeds:

- the canonical left and right occurrence/partition tensors;
- a SHA-256 digest of that canonical topology encoding;
- its exact collapsed weight;
- its exact Haar numerator and denominator;
- the endpoint pattern list and declared local denominator product;
- its integer contribution over the global `QBOUND`.

Of the 69,800 classes, 60,616 have nonzero Haar value. The corpus contains 10,368 pure-six classes and 21,128 balanced-`k=3` classes. The largest reduced Haar denominator actually encountered is 9.

## Exact contractor

The contractor regenerates `W2` and `R2` from the pinned primitives and requires the regenerated canonical history SHA-256 to equal

```text
543869b10f5137ea74fbd5f27d25027dea66f936ce9844b77a029453b8bf8c97
```

It then performs the complete H0/translation/center-flux collapse. The reproduced census is:

| Gate | Exact result |
|---|---:|
| left physical blocks | 3,439 |
| H0-matched blocks | 5,400 |
| raw pair upper bound | 9,814,138 |
| skipped analytic one-face matches | 54 |
| compatible exact state pairs | 2,468,250 |
| historical orientation-sensitive keys | 117,161 |
| fully unordered contraction classes | 69,800 |

The local Haar factors are exact integer/rational projectors:

- balanced `k=1,2,3` Weingarten projectors;
- SU(3) determinant projectors for `(3,0)` and `(0,3)`;
- the rank-five pure-six projector derived from the ten epsilon-pair invariants.

The pure-six Gram calculation selects five independent invariants, inverts their exact integer Gram matrix, expands the projector into 488 nonzero permutation terms, obtains common denominator 72, and verifies projector trace 5.

Each topology is compiled to a low-rank integer tensor network. It is evaluated modulo enough pairwise-coprime primes that their product exceeds twice the rigorous numerator bound

\[
q_H\,3^{n_{\mathrm{trace\ labels}}}.
\]

Signed CRT therefore determines the unique integer numerator. This is exact modular arithmetic with a proved uniqueness interval, not float fitting or heuristic rational reconstruction.

## Denominator and integer-accumulator gates

The previously frozen bound is

```text
QBOUND = 62895057857493885215590055852113920000000.
```

All 69,800 exact terms pass `term.denominator | QBOUND`. The final checks are

```text
QBOUND % denominator(D_EXACT) = 0
QBOUND / denominator(D_EXACT) = 8674474126108262400000
```

and the single integer accumulator is

```text
TOTAL_NUM = -3131555650840341423974721085483725619200000
TOTAL_NUM / QBOUND
  = -361008126292641364183 / 7250590288602460800
  = D_EXACT.
```

The incorporated final denominator also divides the same bound:

```text
QBOUND % denominator(m4_rest) = 0
QBOUND / denominator(m4_rest) = 4337237063054131200000.
```

## Independent replay

The included verifier decompresses and hashes the canonical ledger, recomputes every topology SHA from its embedded occurrence/partition encoding, verifies stable ordering and all 69,800 divisibility/scaled-numerator rows, repeats the rational sum from `D11 = -13/896`, and then repeats the fold/linked assembly. Its result is `passed: true`.

Canonical uncompressed topology-ledger SHA-256:

```text
a7f13ca19eb675ec4340f1664ec04a49979a5cb9e8e95dbb59272b69fa2bb2dd
```

Compressed topology-ledger SHA-256:

```text
48abeca47d51993b05a9b297b20656af3dfed3aaf4d857eac1f466d073c2a662
```

Contractor source SHA-256:

```text
f944bfef52a2176de113d0ca66dd4d1c98ada7f4224ec3cccc8d4c4ae48b7e29
```

Fold reproducer SHA-256:

```text
063979837850c1c8ae3bacb4317a75020c7b92db89681b5785c2c22807a9ef3c
```

Linked-vacuum final certificate SHA-256:

```text
ac7a0feb4581d64315cbea1e16fd81632f79754d4a30fc276d1e0411c54f25e8
```

## Boundary

This closes the exact endpoint-Haar numerator contraction and arithmetic assembly for the frozen rank-3/order-4 cubic scope. It does not, by itself, widen that scope, establish a continuum limit, or replace the separate proof obligations governing the operator construction and physical interpretation.
