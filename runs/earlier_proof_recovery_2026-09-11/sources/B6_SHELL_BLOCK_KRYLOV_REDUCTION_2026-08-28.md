# Residual-certified B6 shell quotient

**Date:** 2026-08-28  
**Status:** **PASS** for the tracked one-cube \(A_1^{--}\oplus T_1^{+-}\oplus E^{--}\) shell on \(1\le g\le2\)  
**Scope:** finite open SU(3) cube at the saved \(B=6\) cutoff; no continuum, infinite-volume, or independent-group claim

## 1. Result

A 121-state higher-order corrected \(B=4\) shell EFT does not remain
quantitative through \(u=g^{-4}=1\). The successful training-free upgrade is
instead a symmetry-adapted, energy-decorated block-Krylov quotient of the
already assembled affine operator

\[
K_6(u)=E-uM.
\]

Its three representative radial dimensions are

\[
\dim K_8(A_1)=67,\qquad
\dim K_8(T_1)=155,\qquad
\dim K_8(E)=133,
\]

or **355 representative radial solve coordinates**. This number is the sum of
three one-carrier blocks, not the dimension of a symmetry-complete 355-state
subspace. Restoring all \(1+3+2\) carrier components gives a 798-dimensional
equivariant word span, versus 1,916 charge-odd and 3,864 full physical states.
The representative blocks reproduce the tracked shell at all eleven original
grid points with maximum absolute splitting error \(2.09\times10^{-14}\), and
pass nine nondegenerate fresh full solves with maximum absolute error
\(3.06\times10^{-14}\).

This is a genuine reduced-solution capability. It is not a gauge-local
corrected \(B=4\) Hamiltonian and does not eliminate construction of the
\(B=6\) local actions.

## 2. Construction theorem

Let \(F:\mathbb R^6\to\mathcal H_{B=6}^{C=-}\) embed the charge-odd one-face
shell, and let \(P_{A_1},P_{T_1},P_E\) be the spectral projectors of the cubical
face Gram matrix. For each irrep \(r\), choose a deterministic carrier
\(v_r\in\operatorname{ran}P_r\) by projecting the standard face vectors,
taking the largest projected norm with a lowest-index tie break, normalizing,
and fixing the sign by the first nonzero entry. Define

\[
\mathcal K_L(r)=
\operatorname{span}\{w(\widetilde E,\widetilde M)Fv_r:|w|\le L\},
\]

where \(w\) ranges over all noncommutative words in the centered/scaled
electric and scaled magnetic generators.

At \(L=8\), all

\[
1+2+4+\cdots+2^8=511
\]

word columns are generated explicitly. Normalizing each nonzero column changes
only a scalar, hence not the span. A single global SVD of the stacked word
matrix, with declared relative cutoff \(10^{-10}\), defines \(Q_{8,r}\). The
online quotient is

\[
K_{8,r}(u)=Q_{8,r}^{\mathsf T}(E-uM)Q_{8,r}.
\]

**Proof of multiplet reduction.** Both \(E\) and \(M\) commute with the cubic
action. Every word in them also commutes with it. Schur's lemma therefore makes
the radial operator identical on every carrier component of a fixed irrep.
One representative block supplies the energy of the full \(1+3+2\) shell.

**Proof of the numerical eigenvalue certificate.** For a normalized Ritz pair
\((\theta,y)\), with \(\psi=Qy\), define

\[
r=(E-uM)\psi-\theta\psi.
\]

Because \(E-uM\) is Hermitian,

\[
\operatorname{dist}(\theta,\sigma(E-uM))\le\lVert r\rVert_2.
\]

Thus the full-space Ritz residual is a target-value-free error certificate. It
does not require the reference eigenvalue. Shell overlap and cubic label select
which spectral branch is being certified.

## 3. Rank, Schur, and conditioning gates

| Irrep | rank | smallest retained \(\sigma\) | largest discarded \(\sigma\) | gap ratio |
|---|---:|---:|---:|---:|
| \(A_1\) | 67 | \(1.30735\times10^{-4}\) | \(3.81968\times10^{-15}\) | \(3.42\times10^{10}\) |
| \(T_1\) | 155 | \(3.59089\times10^{-6}\) | \(4.15988\times10^{-15}\) | \(8.63\times10^8\) |
| \(E\) | 133 | \(8.43373\times10^{-6}\) | \(4.41328\times10^{-15}\) | \(1.91\times10^9\) |

All ranks remain \((67,155,133)\) for relative SVD cutoffs from \(10^{-8}\)
through \(10^{-14}\). A six-carrier Schur check applies the same 511-word SVD
to a canonical orthonormal basis of all components and obtains

\[
67+3(155)+2(133)=798,
\]

with combined numerical rank 798. Its Gram matrix differs from the identity by
at most \(6.34\times10^{-11}\).

The \(L=8\) word space is **not globally invariant** under \(E\) and \(M\):
generator-defect directions remain in the \(T_1\) and \(E\) blocks. The claim
is residual-certified reproduction of the tracked branches, not closure of the
entire \(B=6\) spectrum.

## 4. Complete eleven-point comparison

Predictions equal the full values to all digits shown. Error columns retain the
actual double-precision differences.

| \(g\) | full \(s_T\) | full \(s_E\) | \(|\delta s_T|\) | \(|\delta s_E|\) | rel. \(s_T\) | rel. \(s_E\) |
|---:|---:|---:|---:|---:|---:|---:|
| 2.0 | 0.000140757076 | 0.000216887643 | \(4.44\times10^{-16}\) | \(7.55\times10^{-15}\) | \(3.16\times10^{-12}\) | \(3.48\times10^{-11}\) |
| 1.9 | 0.000215130334 | 0.000336296005 | \(4.00\times10^{-15}\) | \(1.60\times10^{-14}\) | \(1.86\times10^{-11}\) | \(4.75\times10^{-11}\) |
| 1.8 | 0.000335538258 | 0.000537270118 | \(1.02\times10^{-14}\) | \(1.20\times10^{-14}\) | \(3.04\times10^{-11}\) | \(2.23\times10^{-11}\) |
| 1.7 | 0.000531917761 | 0.000888124272 | \(4.44\times10^{-15}\) | \(3.55\times10^{-15}\) | \(8.35\times10^{-12}\) | \(4.00\times10^{-12}\) |
| 1.6 | 0.000844878802 | 0.00152459080 | \(1.42\times10^{-14}\) | \(3.11\times10^{-15}\) | \(1.68\times10^{-11}\) | \(2.04\times10^{-12}\) |
| 1.5 | 0.00128416064 | 0.00271861951 | \(2.22\times10^{-15}\) | \(4.88\times10^{-15}\) | \(1.73\times10^{-12}\) | \(1.80\times10^{-12}\) |
| 1.4 | 0.00156327112 | 0.00498298877 | \(8.88\times10^{-15}\) | \(1.15\times10^{-14}\) | \(5.68\times10^{-12}\) | \(2.32\times10^{-12}\) |
| 1.3 | -0.000169525054 | 0.00904343369 | \(1.20\times10^{-14}\) | \(1.07\times10^{-14}\) | \(7.07\times10^{-11}\) | \(1.18\times10^{-12}\) |
| 1.2 | -0.0114981736 | 0.0148604370 | \(1.29\times10^{-14}\) | \(2.09\times10^{-14}\) | \(1.12\times10^{-12}\) | \(1.40\times10^{-12}\) |
| 1.1 | -0.0484098395 | 0.0188899566 | \(1.09\times10^{-14}\) | \(9.10\times10^{-15}\) | \(2.25\times10^{-13}\) | \(4.82\times10^{-13}\) |
| 1.0 | -0.111201338 | 0.0150652472 | \(5.76\times10^{-15}\) | \(6.94\times10^{-16}\) | \(5.18\times10^{-14}\) | \(4.61\times10^{-14}\) |

Ordering is correct at **11/11** points. The maximum pointwise error normalized
by the larger target splitting is \(4.75\times10^{-11}\).

## 5. Interval and fresh-validation gates

A target-value-free sweep at 201 equally spaced points on \(1\le g\le2\)
gives

\[
\max_{g,r}\lVert(E-uM)\psi_{8,r}-\lambda_{8,r}\psi_{8,r}\rVert_2
=8.78\times10^{-14}.
\]

The smallest representative shell weight is 0.267697 at \(g=1\).
A separate hostile 1,001-point reduced-space sweep found no selected-index
change; the selected shell-weight margin over the runner-up stayed above
0.1815, 0.1525, and 0.2242 in the \(A_1,T_1,E\) blocks, respectively. Fresh
full-B6 checks at \(g=1,1.30397,2\) place the tracked \(1+3+2\) multiplets at
eigenvalue indices 0 through 5.

The original eleven points are **not** out-of-sample evidence: \(L=8\) was
historically identified after their convergence was inspected. The fresh test
sealed seven off-grid values and two root-bracketing values before their full
1,916-state solves. On the nine nondegenerate points, ordering is **9/9**,
maximum absolute error is \(3.06\times10^{-14}\), and maximum pointwise
normalized error is \(6.81\times10^{-11}\). The maximum absolute-relative
error, \(4.42\times10^{-6}\), occurs next to the crossing where
\(|s_T|\approx4.12\times10^{-9}\).

## 6. Sharpened crossing

The quotient has one sign change and gives

\[
g_\times^{\rm red}=1.303954664171324.
\]

This differs by \(1.49\times10^{-5}\) from the earlier full-B6 linear estimate
inside its width-0.0025 bracket. Fresh full solves give

\[
s_T(g_\times-10^{-7})=-4.12399\times10^{-9},\qquad
s_T(g_\times+10^{-7})=+4.12399\times10^{-9}.
\]

At the reduced root itself, the full solve gives
\(s_T=-2.89\times10^{-14}\); reduced and full differ by
\(3.06\times10^{-14}\). Strict ordering is not scored at this degenerate point.

## 7. Why the higher-order B4 EFT was not promoted

Perturbative recursion gives the numerical series

\[
\begin{aligned}
s_T(u)&=\frac5{153}u^2+0.0632769447648u^3-0.0912558401823u^4+\cdots,\\
s_E(u)&=\frac5{102}u^2+0.0949154171472u^3+0.175723487765u^4+\cdots.
\end{aligned}
\]

The cubic terms are numerically consistent with \(1975/31212\) and
\(1975/20808\) to about \(2.4\times10^{-14}\), but are not promoted as exact
symbolic values because the saved Clebsch--Gordan operator is floating-point.

| 121-state model | ordering | median absolute-relative error | max absolute error |
|---|---:|---:|---:|
| \(O(u^2)\) | 9/11 | 0.605 | 0.172 |
| \(O(u^3)\) | 7/11 | 0.0665 | 0.365 |
| \(O(u^4)\) | 7/11 | 0.0526 | 0.571 |
| Padé \([4/4]\) | 11/11 | \(9.30\times10^{-4}\) | 0.302 |

The polynomial counterterms diverge toward \(u=1\); even the best
ordering-only Padé candidate has unacceptable strong-coupling absolute error.

## 8. Resources and chronology

- representative radial solve dimensions: \(67+155+133=355\), or 18.5% of
  the charge-odd sector and 9.19% of the physical basis; this is a 5.40-fold
  reduction relative to solving the full charge-odd sector, but it is not a
  symmetry-complete 355-state subspace;
- full six-component equivariant word span: 798 dimensions, or 41.65% of the
  charge-odd sector and 20.65% of the physical basis, a 2.40-fold reduction
  relative to the full charge-odd sector;
- serialized reduced operator: 639,587 bytes;
- online dense arrays: 742,088 bytes;
- observed eleven-point online solve time after construction: 0.080 s;
- observed root-run construction time: 0.90 s;
- complete builder with rank, Schur, sweep, crossing, and fresh-full gates:
  6.96 s in the recorded run.

These are implementation-specific warm timings. Construction consumes the
already assembled full \(B=6\) \(E,M\). The quotient accelerates repeated
finite-\(u\) solution; it does not remove local-action generation.

There are zero fitted parameters. The stable builder constructs and seals all
predictions before it opens the target certificate. The prediction seal is

`a8593544775497dbdedcaeb8fecbdabb5c23460111b0ca822c1d7b575ba2dedc`.

This is an auditable target-value firewall, not external preregistration. The
residual rule was not publicly timestamped in advance, and the original grid
participated in model development. The fresh off-grid/full-crossing solves are
the prospective evidence.

## 9. Publication-safe claim

> For the finite open SU(3) cube at cutoff \(B=6\), the tracked charge-odd
> \(A_1\oplus T_1\oplus E\) one-face shell admits a deterministic
> energy-decorated word-SVD quotient with 355 coordinates across three
> representative radial solves (798 dimensions after all carrier components
> are restored).
> On \(1\le g\le2\), its 201-point full-space Ritz residual is at most
> \(8.78\times10^{-14}\); it reproduces eleven saved and nine fresh
> nondegenerate full-B6 comparisons to double precision and locates the
> symmetry-protected \(A_1/T_1\) crossing at
> \(g=1.303954664171324\).

The narrow novelty candidate is the **theory-specific SU(3) circuit/Hodge
history quotient** and the capability it enables. Block Krylov, Ritz, SVD, and
Feshbach methods are prior art. Also unclaimed are global spectral closure,
every-\(g\) theorem, continuum physics, elimination of B6 construction, and
unaffiliated replication.

## 10. Reproduction

```powershell
& 'C:\Users\Alex\AppData\Local\Programs\Python\Python312\python.exe' `
  'build_b6_shell_block_krylov_reduction.py' `
  --output-dir '.scratch\b6_shell_replay'
```

Artifacts:

- `build_b6_shell_block_krylov_reduction.py`
- `b6_shell_block_krylov_reduction_certificate.json`
- `b6_shell_block_krylov_reduced_operator.npz`
- `b6_shell_block_krylov_replay_certificate.json`
- `B6_SHELL_BLOCK_KRYLOV_HOSTILE_AUDIT_2026-08-28.md`
- `b6_shell_block_krylov_hostile_audit_certificate.json`

Canonical reduced-operator numerical-content hash:

`1523190fe0de1bb4e2dc9ac41c6e8bd92abc985827afb83516fdf0d1e70a8964`

The fresh-process replay reproduced the same prediction seal, canonical
operator content, dimensions, and six-seed rank. It is an internal deterministic
replay, not an independent-group replication.
