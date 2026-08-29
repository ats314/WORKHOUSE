# Channel-complete two-cube SU(3) charge-odd kernel at \(B=6\) through \(O(u^2)\)

## Result and exact scope

For the open face-sharing \((3,2,2)\) prism, in the exact-Casimir \(B=6\)
Hamiltonian truncation, the complete \(C\)-odd one-plaquette shell at
\(E_*=8/3\) has dimension eleven. With

\[
H(u)=E-uM=H_0+uV,\qquad V=-M,
\]

and with the full \(E_*\) eigenspace removed from the pseudoinverse, the
operator-level left/right/shared-face Mobius fold gives

\[
K^{(2)}_{\mathrm{conn}}
=\frac{5}{612}\,G_{\mathrm{conn}}+D.
\]

Here \(G_{\mathrm{conn}}\) is the geometry-derived connected incidence Gram
matrix fixed before the contraction, and

\[
D=\frac1{612}\operatorname{diag}
(-2317,-2317,-2295,-2317,-2317,-2317,-2317,0,-2317,-2317,-2295).
\]

The coefficient \(5/612\) was recovered from the target-blind contraction.
It was not supplied to the builder, graph fit, branching logic, held-out
validator, or scientific tests.

This is a finite-volume, strong-coupling, two-cube result through \(O(u^2)\).
It is not a continuum, infinite-volume, mass-gap, or full finite-coupling
claim. A full radius-three word-space calculation was preflighted but not
executed; the bounded held-out result below is a complete two-action
Feshbach check, not a radius-three stability result.

## 1. Frozen geometry and coordinate order

The eleven oriented plaquettes are indexed as follows:

| index | plaquette address |
|---:|---|
| 0 | `((0,0,0),(1,2))` |
| 1 | `((0,0,0),(1,3))` |
| 2 | `((0,0,0),(2,3))` |
| 3 | `((0,0,1),(1,2))` |
| 4 | `((0,1,0),(1,3))` |
| 5 | `((1,0,0),(1,2))` |
| 6 | `((1,0,0),(1,3))` |
| 7 | `((1,0,0),(2,3))` |
| 8 | `((1,0,1),(1,2))` |
| 9 | `((1,1,0),(1,3))` |
| 10 | `((2,0,0),(2,3))` |

The left and right source cubes embed into target coordinates

\[
I_L=(0,1,2,3,4,7),\qquad
I_R=(5,6,7,8,9,10),\qquad I_F=(7).
\]

The signed plaquette-link boundary matrix \(B\) is constructed from these
oriented faces. No spectral output is consulted in defining

\[
G=BB^\mathsf T,
\]

or its source-folded form

\[
G_{\mathrm{conn}}
=G-J_LG_LJ_L^\mathsf T-J_RG_RJ_R^\mathsf T+J_FG_FJ_F^\mathsf T.
\]

Its only nonzero off-diagonal connected pairs are
\((0,5),(1,6),(3,8),(4,9)\) and their transposes, with signed entry \(-1\).

## 2. The \(B=6\) Hilbert space and complete shell census

The truncation retains precisely the SU(3) irreps whose exact quadratic
Casimir does not exceed six:

\[
\mathbf1,\quad \mathbf3,\quad \bar{\mathbf3},\quad
\mathbf6,\quad \mathbf8,\quad \bar{\mathbf6}.
\]

After imposing every local singlet constraint and resolving every local
intertwiner multiplicity, the two-cube basis dimension is

\[
\dim\mathcal H_{B=6}=1{,}590{,}462.
\]

There are 24 trivalent local singlets. At a four-valent vertex there are 81
irrep tuples and 87 multiplicity-resolved singlets, including six genuine
two-dimensional intertwiner blocks.

Exhaustive enumeration of every nonnegative B6 irrep-energy partition that
sums to \(E_*=8/3\) leaves only four \(2/3\) links, each carried by
\(\mathbf3\) or \(\bar{\mathbf3}\); no partition containing a sextet or
adjoint link sums to \(8/3\). Exhausting every four-link subset, all \(2^4\)
conjugacy assignments, and every compatible local multiplicity gives exactly
22 states. Their canonical ranks are

```text
1, 2, 4, 10, 20, 50, 100, 300, 680, 1172, 1876,
2053, 3864, 8324, 13680, 31165, 54070, 159944,
360788, 565943, 870269, 944105
```

Tensor-derived charge conjugation splits this entire eigenspace as

\[
22=11_{C=+1}\oplus11_{C=-1}.
\]

For each plaquette \(p\), define

\[
|q_p\rangle=\frac{i}{\sqrt2}(W_p-W_p^\dagger)|0\rangle.
\]

The eleven columns contain exactly the 22 oriented shell ranks, satisfy

\[
C|q_p\rangle=-|q_p\rangle,
\qquad
Q_-^\dagger Q_-=I_{11},
\]

and span the full \(C\)-odd \(E_*\) sector. The measured Gram residual is
\(2.22\times10^{-16}\).

## 3. Complete on-demand magnetic action

The calculation never assembles the \(1{,}590{,}462\)-dimensional magnetic
matrix. For each queried initial plaquette key, it instead:

1. enumerates every compatible local singlet and every allowed local
   multiplicity row;
2. evaluates the pinned finite-precision SU(3) CGC factors for both \(W\) and
   \(W^\dagger\);
3. forms the full Cartesian product of the local factors;
4. glues only physical global states and ranks them with the sealed backend;
5. retains the plaquette address, branch, local transition ordinal, local
   \(G_i,G_f\) labels, and global multiplicity indices for every path.

The filtered construction was compared with complete upstream plaquette
tables on both a mixed-valence face and an all-trivalent face. Across every
queried initial key, the key sets and amplitudes agree exactly at stored
precision.

Acting on all eleven shell columns produces 794 unaccumulated one-step paths
and 398 distinct reachable ranks. Every retained irrep is reached. Both rows
of the multiplicity-two blocks occur; 32 reachable vertex labels use the
second row, so the calculation cannot be reduced to scalar local channels.

## 4. Degenerate perturbation theory and the resolvent sign

Let \(P=Q_-Q_-^\dagger\) and let

\[
\bar P_*=I-P_{E_*}
\]

remove the complete 22-dimensional \(E_*\) eigenspace, not merely the eleven
displayed shell columns. The frozen pseudoinverse is

\[
R_*=(E_*-H_0)^+
=\bar P_*\frac1{E_*-H_0}\bar P_*.
\]

Thus

\[
H_{\mathrm{eff}}(u)
=E_*P+uK_1+u^2K_2+O(u^3),
\]

with

\[
K_1=PVP=I_{11},\qquad
K_2=(VQ_-)^\dagger R_*(VQ_-).
\]

For an intermediate state \(m\), the history contribution is therefore

\[
\frac{\langle q_f|V|m\rangle
      \langle m|V|q_i\rangle}
     {E_*-E_m}.
\]

Exactly 22 one-step paths land in the excluded zero-denominator eigenspace.
After their removal, 364 accumulated intermediate ranks contribute. A
separate diagonal-resolvent contraction agrees with the ordered-history fold
to machine zero. The deliberately incorrect replacement
\((E_*-E_m)^{-1}\mapsto(E_*-E_m)\) differs by \(45.6895424836602\), fixing the
reciprocal and its sign independently.

## 5. Raw second-order matrix

In the face order of Section 1, rational recovery gives

\[
K_2^{\mathrm{raw}}=\frac1{612}
\begin{pmatrix}
-4700&5&-5&0&-5&-5&0&5&0&0&0\\
5&-4700&5&-5&0&0&-5&-5&0&0&0\\
-5&5&-4678&5&-5&0&0&0&0&0&0\\
0&-5&5&-4700&5&0&0&-5&-5&0&0\\
-5&0&-5&5&-4700&0&0&5&0&-5&0\\
-5&0&0&0&0&-4700&5&-5&0&-5&5\\
0&-5&0&0&0&5&-4700&5&-5&0&-5\\
5&-5&0&-5&5&-5&5&-4766&5&-5&0\\
0&0&0&-5&0&0&-5&5&-4700&5&-5\\
0&0&0&0&-5&-5&0&-5&5&-4700&5\\
0&0&0&0&0&5&-5&0&-5&5&-4678
\end{pmatrix}.
\]

The maximum residual of the rational reconstruction is below
\(1.8\times10^{-14}\). This is robust numerical rational recovery from pinned
finite-precision CGCs; it is not presented as a formal symbolic-CGC identity.

## 6. Literal operator-level Mobius subtraction

Let \(K_{LR}\) be the target raw operator and let \(K_L,K_R,K_F\) be the
left-cube, right-cube, and shared-face source operators computed in their own
source coordinates. The connected operator is defined literally by

\[
K_{\mathrm{conn}}
=K_{LR}-J_LK_LJ_L^\dagger-J_RK_RJ_R^\dagger+J_FK_FJ_F^\dagger.
\]

The same operation was applied history by history. There are 1,984 ordered
nonzero two-step histories: 1,192 cancel with Mobius weight zero and 792
survive with weight one. The literal ledger sum and the matrix-level source
subtraction agree within \(4.88\times10^{-15}\). At first order the identical
fold cancels \(PVP=I_{11}\) to zero.

The resulting matrix is

\[
K_{\mathrm{conn}}=\frac1{612}
\begin{pmatrix}
-2317&0&0&0&0&-5&0&0&0&0&0\\
0&-2317&0&0&0&0&-5&0&0&0&0\\
0&0&-2295&0&0&0&0&0&0&0&0\\
0&0&0&-2317&0&0&0&0&-5&0&0\\
0&0&0&0&-2317&0&0&0&0&-5&0\\
-5&0&0&0&0&-2317&0&0&0&0&0\\
0&-5&0&0&0&0&-2317&0&0&0&0\\
0&0&0&0&0&0&0&0&0&0&0\\
0&0&0&-5&0&0&0&0&-2317&0&0\\
0&0&0&0&-5&0&0&0&0&-2317&0\\
0&0&0&0&0&0&0&0&0&0&-2295
\end{pmatrix}.
\]

Its exact spectrum is

\[
0^{\times1},\qquad
\left(-\frac{15}{4}\right)^{\times2},\qquad
\left(-\frac{578}{153}\right)^{\times4},\qquad
\left(-\frac{129}{34}\right)^{\times4}.
\]

## 7. Six shared-link channels and the sign mechanism

For an adjacent ordered pair of shell faces, the unique common link defines a
representation channel: the exact irrep carried by that link in the ranked
intermediate state. The six independently reconstructed graph coefficients
are

\[
\begin{array}{c|rrrrrr}
\rho&\mathbf1&\mathbf3&\bar{\mathbf3}&\mathbf6&\bar{\mathbf6}&\mathbf8\\
\hline
c_\rho&\frac1{12}&-\frac1{12}&-\frac1{12}&-\frac1{9}&-\frac1{9}&\frac{16}{51}
\end{array}
\]

and hence

\[
\sum_\rho c_\rho
=\frac{51-51-51-68-68+192}{612}
=\frac5{612}.
\]

Each shared-link channel matrix is separately proportional to \(G\) off the
diagonal, and its connected fold is separately proportional to
\(G_{\mathrm{conn}}\). Same-face histories carry an ordered four-link irrep
signature, while disjoint histories are labeled `no_shared_link`; they are
retained in exact `other_raw` and `other_connected` matrices rather than being
assigned arbitrarily to one of the six graph channels.

## 8. Tensor-derived symmetry checks

Charge conjugation and the cube-exchange reflection \(U_x\) were constructed
from independent CGC tensor overlaps on every reachable local multiplicity
block, not fitted from \(K_2\). On the 398-state reachable subspace:

- 896 local blocks were evaluated, including 48 full \(2\times2\) blocks;
- the \(C\) and \(U_x\) unitarity/involution residuals are at most
  \(4.44\times10^{-16}\);
- \([C,U_x]=0\) exactly at stored precision;
- shell and one-step covariance residuals are at most
  \(1.11\times10^{-16}\);
- all 794 local transition ordinals transform covariantly under \(U_x\);
- both raw and connected effective matrices commute with the shell action.

## 9. Independent one-cube and finite-\(u\) checks

The left source fold was compared with the independently stored one-cube
\(B=6\), 3,864-state magnetic operator. It reproduces both \(PVP=I_6\) and the
one-cube second-order contraction within the release tolerance.

An independent energy-decorated \(P+Q_1\) word space was then built from all
eleven shell states. It has dimension

\[
11+55=66,
\]

with six exact-energy sectors of dimension eleven. Without reading any
reported coefficient, it recovers

\[
\|PVP-(PVP)_{\mathrm{Krylov}}\|_{\max}=0,
\]

and

\[
\|K_2^{\mathrm{raw}}-(K_2)_{\mathrm{Krylov}}\|_{\max}
=6.217248937900877\times10^{-15}.
\]

At the held-out points

\[
u\in\left\{\frac1{127},\frac1{97},\frac1{73},\frac1{59}\right\},
\]

the correct second-order residual has log-log slope \(2.901745\), while a
reversed second-order sign has slope \(2.002000\). The minimum wrong-sign to
correct-error ratio is \(324.86\). This validates the complete two-action
Feshbach fold and its cubic small-\(u\) remainder inside \(P+Q_1\).

The attempted next-radius preflight was stopped after 16 of 55 radius-two
frontier vectors had already produced 127 new directions and cached 196
physical ranks. No radius-three convergence or cutoff-stability claim is
made.

## 10. Post-hoc comparison, performed only after the blind freeze

The target-blind replay froze these pre-publication payload hashes:

```text
artifact     3fd15a3ab5060b7e477662d63e3fdcf65cb2b9eb52c2b1a11a0f6065249f5cb4
certificate  638b72d539e5dbff0426254145a7f1aa344174f02375cd85c2a9441a8ae32940
history      b638c2d0c5e14348c678ce20c60ba1c465b94ce0d8133c150d4b8519c17e5c02
```

Only after those bytes existed was the recovered coefficient compared with
the prior proposed value. The comparison is exact:

\[
c_{B=6}^{\mathrm{recovered}}=\frac5{612}
=c_{B=6}^{\mathrm{proposed}}.
\]

The sealed \(B=4\) result is

\[
c_{B=4}=-\frac1{12}=-\frac{51}{612}.
\]

The newly restored \(\mathbf6,\bar{\mathbf6},\mathbf8\) channels contribute

\[
-\frac19-\frac19+\frac{16}{51}
=\frac{56}{612},
\]

so that

\[
-\frac{51}{612}+\frac{56}{612}=\frac5{612}.
\]

Thus the predicted sign reversal is reproduced, and its mechanism is exposed:
the positive adjoint-channel contribution exceeds the two negative sextet
contributions by \(56/612\), overturning the \(B=4\) coefficient.

## 11. Reproducibility and claim firewall

The public release contains a deterministic pickle-free NPZ, canonical JSON
certificate, canonical 1,984-record JSONL history ledger, strict artifact-only
loader, quick verifier, byte-for-byte replay verifier, focused tests, hostile
publication tests, isolated-extraction acceptance test, and a detached
exact-role manifest published last. The manifest binds the full regenerative
closure by role, authority class, basename, size, order, and SHA-256. The
closure includes the B6 construction engines, basis backend and dormant local
imports, original sealed CGC adapter, exact pinned source archive, both
one-cube B6 inputs, every B4 source used by the tensor path, and the complete
nested B4 detached release plus its three replay inputs. Publication uses
same-parent candidates, rollback, inherited directory permissions, and the
manifest is replaced last.

The sealed adapter remains byte-identical. Its historical private source-tree
assumption is replaced only for this B6 release by a manifest-bound portable
bootstrap. The bootstrap verifies adapter SHA-256
`6e6164cc04ff3321a3fc0ee7ac52863299acd2681d7aae2c135432c0312c2f32`,
archive SHA-256
`6d16ee0fa055b143d8373efa8d57e4f5a745b362bcab6eb12318a9c09922111b`,
and all eleven pinned archive members, materializes those members in an OS
temporary directory, and deletes that temporary tree at process exit. No
workspace-relative hidden directory, installed local module, or `PYTHONPATH`
is needed. The archive's embedded comment is not promoted to an upstream
commit because no such provenance is documented locally.

The tested runtime is CPython 3.12 with NumPy 2.3.5 and SciPy 1.17.1. The
portable release requires Python, NumPy, and SciPy; optional imports in the
sealed adapter retain their existing fail-closed fallbacks.

The executable scientific path contains no post-hoc target value or sign
expectation. The certificate explicitly distinguishes exact integer/rational
serialization from the finite-precision CGC amplitudes from which those
rationals were recovered.

The comparator is packaged under the explicit non-authoritative manifest
class `posthoc_only`. Its hash and presence are required for a complete release,
but neither the scientific builder nor deterministic replay imports it. It is
run only after the blind artifact is frozen.

### Exact manifest-only extraction and replay

From the release directory, create a flat extraction containing exactly the
manifest-listed files plus the detached manifest:

```powershell
python -c "import json,pathlib,shutil; s=pathlib.Path('.'); m=json.loads((s/'two_cube_b6_codd_o2_connected_kernel_manifest.json').read_text('ascii')); d=pathlib.Path('b6_release_extract'); d.mkdir(exist_ok=False); [shutil.copyfile(s/r['name'],d/r['name']) for r in m['files']]; shutil.copyfile(s/'two_cube_b6_codd_o2_connected_kernel_manifest.json',d/'two_cube_b6_codd_o2_connected_kernel_manifest.json')"
Set-Location b6_release_extract
```

Run the strict artifact verification, same-builder byte replay, and post-hoc
comparison in isolated interpreters without `PYTHONPATH`:

```powershell
python -I -c "import runpy,sys; sys.path.insert(0,'.'); runpy.run_path('verify_two_cube_b6_codd_o2_connected_kernel.py',run_name='__main__')"
python -I -c "import runpy,sys; sys.path.insert(0,'.'); runpy.run_path('rebuild_verify_two_cube_b6_codd_o2_connected_kernel.py',run_name='__main__')"
python -I -c "import runpy,sys; sys.path.insert(0,'.'); runpy.run_path('two_cube_b6_codd_o2_posthoc_comparison.py',run_name='__main__')"
```

The packaged hostile acceptance test performs the same extraction, strict
load, quick verification, full replay, 1,984-record ledger byte comparison,
post-hoc comparison, and per-critical-role deletion/corruption sweep:

```powershell
python test_two_cube_b6_codd_o2_isolated_extraction.py --full
```
