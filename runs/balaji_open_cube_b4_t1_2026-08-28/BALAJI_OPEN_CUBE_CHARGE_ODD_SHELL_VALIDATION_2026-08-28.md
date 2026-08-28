# Balaji Open-Cube Charge-Odd Shell Validation

**Date:** 2026-08-28  
**Status:** **PASS for the published \(B=4=T_1\) open cube**  
**Scope:** exact gauge-invariant block of the finite \(T_1=\{\mathbf1,\mathbf3,\bar{\mathbf3}\}\) Hamiltonian; no claim here for the channel-complete \(B=6\) cube or the continuum theory

## Result

The six charge-odd one-face states of the Balaji et al. open-cube Hamiltonian form the predicted (1+3+2) strong-coupling shell.

With

\[
K(u):=\frac{H}{g^2}
=\frac12\sum_{\ell}C_2(R_\ell)
-u\sum_p(\Box_p+\Box_p^\dagger),
\qquad u=g^{-4},
\]

and with the extensive magnetic constant omitted as in the paper's perturbative discussion, the vacuum-subtracted charge-odd gaps are

\[
\boxed{
\Delta K_{C=-}
=\frac83+u+
u^2\left\{
\left(\frac{31}{12}\right)^{(2)},
\left(\frac{11}{4}\right)^{(3)},
\left(\frac{37}{12}\right)^{(1)}
\right\}
+O(u^3).}
\]

Relative to the one-dimensional signed-boundary mode, this is

\[
\boxed{
u^2\left\{
\left(-\frac12\right)^{(2)},
\left(-\frac13\right)^{(3)},
0^{(1)}
\right\}+O(u^3).}
\]

Thus the \(B=4=T_1\) cube has the predicted doublet-triplet-singlet ordering. This is the reversed kinetic ordering predicted for the truncated theory, not the channel-complete ordering obtained after the missing \(\mathbf6\) and \(\mathbf8\) routes are restored.

## What was obtained

The authors' unpublished global ED matrix was not found. What was obtained is enough to reconstruct and identify its exact physical block:

1. Balaji et al. state that their three-dimensional test is one cube with open boundary conditions in \(T_1=B=4\), and that its reference state is obtained by exact diagonalization.
2. Their public `ymcirc` development history contains the precomputed \(d=3,B=4\) oriented plaquette matrix-element table. GitHub PR #76 describes this file as data supporting \(d=3,B=4\) circuit construction.
3. The six open-cube face operators were assembled from that table. At each boundary vertex, the one physical control-link irrep was retained and the three absent periodic control directions were tensor-padded by the trivial irrep \(\mathbf1\). This is the identity-object restriction of the same local singlet contraction.
4. Only assignments satisfying Gauss' law at every trivalent cube vertex were retained. This gives the exact 243-dimensional physical block of the authors' much larger tensor-product encoding.

The result is therefore an **author-data-derived, independently assembled physical cube matrix**, not a relabeling of a WORKHOUSE effective matrix and not a claim that the authors supplied their private sparse ED artifact. Because the local table and the cube paper share the same author/code lineage, this is an independent reconstruction from upstream master coefficients, not an independent-group replication.

### Source pin

- Repository: <https://github.com/hepqis-uiuc/ymcirc>
- Data-introduction PR: <https://github.com/hepqis-uiuc/ymcirc/pull/76>
- Observed development commit: `e9e190bfda405608de9cab71c0df0161cfcb1a10`
- Git blob: `1808849c74b36f8082e7030d074681be4bb8c0fd`
- File: `B4_dim(3)_PBC_magnetic_hamiltonian.json.gz`
- File SHA-256: `4cad9538681c10e88270ef60045fb91b7f2de22b42f97621812667b492ba9a1a`
- Raw oriented local entries: 40,275

The source filename says `PBC`; the boundary restriction is independently checked below and is not assumed merely from the filename.

## Matrix reconstruction checks

The open cube has 8 vertices, 12 edges, and 6 faces. Each edge was labeled by \(\mathbf1,\mathbf3,\bar{\mathbf3}\). At a vertex, incoming link irreps were conjugated before testing whether the three incident half-link irreps fuse to a singlet.

The resulting exact matrix census is:

| Object | Result |
|---|---:|
| gauge-invariant basis dimension | 243 |
| directed \(\sum_p\Box_p\) nonzeros | 1,458 |
| \(\sum_p(\Box_p+\Box_p^\dagger)\) nonzeros | 2,916 |
| charge-odd block dimension | 121 |
| missing author-table local states | 0 |
| transitions leaving the physical basis | 0 |
| \(\lVert[C,M]\rVert_{\max}\) | 0 |
| vacuum-to-oriented-face amplitude | 1 on all 6 faces |

Every physical basis state has exactly one nonzero oriented transition per face. Charge conjugation is the independently constructed operation \(\mathbf3\leftrightarrow\bar{\mathbf3}\); it was not inferred from the spectrum.

### Boundary-padding audit

A second implementation used the public `pyclebsch` open-boundary generator directly on a \(2\times2\times2\) lattice with fully open boundaries. It independently obtained:

- physical dimension 243;
- directed magnetic nonzeros 1,458;
- Hermitian magnetic nonzeros 2,916;
- charge-odd dimension 121;
- exact charge commutator zero.

It then compared each directly generated open-boundary local coefficient with the trivially padded entry in the \(d=3,B=4\) table. All \(6\times81=486\) directed local elements were present, no entries were missing or extra, and the maximum absolute difference was zero. A separate exhaustive convention check at \(B=3\) compared 17,367 open-boundary coefficients with their signed-direction-slot embeddings in the periodic table and likewise found 17,367 exact matches, zero missing entries, and zero mismatches. Balaji et al. also state that lower-dimensional singlets embed at the same \(B\) in higher dimensions by tensoring with copies of \(\mathbf1\). Together these close the only nontrivial embedding assumption.

## Exact Schur-complement extraction

Let \(P\) contain the six normalized one-face odd states

\[
|p,-\rangle
=\frac{|p,\circlearrowleft\rangle-|p,\circlearrowright\rangle}{\sqrt2},
\qquad p=1,\dots,6.
\]

They all have unperturbed energy (8/3). For (V=-M), direct projection of the reconstructed matrix gives

\[
P^\dagger V P=I_6,
\]

which supplies the common (+u) term. The vacuum second-order coefficient is

\[
E_{\mathrm{vac}}^{(2)}=-\frac92.
\]

The full second-order gap operator, computed from every state outside the degenerate one-face shell, is

\[
W_{\mathrm{gap}}^{(2)}
=P^\dagger VQ\frac{1}{\frac83-H_0}QVP
-E_{\mathrm{vac}}^{(2)}I_6.
\]

In the face order

\[
(xy|_{z=0},xy|_{z=1},xz|_{y=0},xz|_{y=1},yz|_{x=0},yz|_{x=1}),
\]

the independently constructed cubical face Gram matrix is

\[
G=
\begin{pmatrix}
4&0&1&-1&-1&1\\
0&4&-1&1&1&-1\\
1&-1&4&0&1&-1\\
-1&1&0&4&-1&1\\
-1&1&1&-1&4&0\\
1&-1&-1&1&0&4
\end{pmatrix},
\qquad
\operatorname{spec}G=\{0^{(1)},4^{(3)},6^{(2)}\}.
\]

The author-data Schur complement satisfies the **full matrix identity**, not only an eigenvalue fit:

\[
\boxed{
W_{\mathrm{gap}}^{(2)}
=\frac{37}{12}I_6-\frac1{12}G.}
\]

The maximum entrywise discrepancy is \(4.27\times10^{-11}\), set by the decimal precision of the public matrix-element table. Its eigenvalues differ from the predicted rationals by at most \(1.34\times10^{-10}\).

No coefficient or multiplicity was fit to obtain this identity.

### Cubic-irrep identification

The multiplicities were not identified from numerical degeneracy alone. Let \(b_{\pm i}\) denote the outward-oriented charge-odd states on the two faces normal to axis \(i\). Spatial inversion acts as

\[
P b_{+i}=-b_{-i}.
\]

Consequently the three sums \(s_i=b_{+i}+b_{-i}\) are parity odd and decompose as \(A_1\oplus E\), while the three differences \(d_i=b_{+i}-b_{-i}\) are parity even and transform as \(T_1\). Including charge conjugation, the shell is

\[
\boxed{A_1^{--}\oplus T_1^{+-}\oplus E^{--},}
\]

with the explicit spectral assignment

| cubic irrep | dimension | \(G\) eigenvalue | gap coefficient | relative coefficient |
|---|---:|---:|---:|---:|
| \(A_1^{--}\) | 1 | 0 | \(37/12\) | 0 |
| \(T_1^{+-}\) | 3 | 4 | \(11/4\) | \(-1/3\) |
| \(E^{--}\) | 2 | 6 | \(31/12\) | \(-1/2\) |

This is the representation-theoretic \(1+3+2\) statement tested by the reconstructed Hamiltonian.

### Independent literature cross-check—and its limit

Kimura's 1984 Hamiltonian strong-coupling calculation contains a translation-projected four-link \(T_1^{+-}\) branch. In Kimura's convention,

\[
W=\frac{2aH}{g^2}=D-yM,
\qquad y=2g^{-4}=2u,
\]

whereas the present dimensionless cube convention has \(W=2K\) after removal of the additive magnetic constant. Kimura reports

\[
T_1^{+-}:\qquad
w=\frac{16}{3}+y+0.0180y^2+\cdots.
\]

This independently checks the zeroth-order energy, first-order sign, normalization dictionary, and existence of the \(T_1^{+-}\) channel. It does **not** test the open-cube second-order coefficient: Kimura's state is translation projected in a different geometry, and his listed \(A_1/E\) four-link states are charge even rather than the open-cube \(A_1^{--}/E^{--}\) partners. It is therefore corroboration, not a substitute for the coefficient-level cube reconstruction above.

## Full finite-\(u\) diagonalization

The 121-dimensional charge-odd block was diagonalized directly. At each \(u\), the six states were selected only by overlap with the independently defined one-face odd subspace. The displayed coefficient is

\[
c_j(u)=
\frac{\Delta K_j(u)-\frac83-u}{u^2}.
\]

| \(u\) | minimum one-face-shell overlap | doublet \(c_2(u)\) | triplet \(c_3(u)\) | singlet \(c_1(u)\) |
|---:|---:|---:|---:|---:|
| 0.0200 | 0.999630 | 2.59740465 | 2.76480313 | 3.09983166 |
| 0.0100 | 0.999908 | 2.59076148 | 2.75782004 | 3.09199311 |
| 0.0050 | 0.999977 | 2.58714402 | 2.75401290 | 3.08776441 |
| 0.0025 | 0.999994 | 2.58526263 | 2.75203195 | 3.08557398 |
| \(u\to0\) | 1 | \(31/12=2.583333\ldots\) | \(11/4=2.75\) | \(37/12=3.083333\ldots\) |

The degeneracies are exact at every sampled \(u\); the shell overlap tends to one and the coefficients converge to the independently calculated Schur-complement values.

## Reproduction of the paper's published ED curve

The paper does not publish its charge-odd excited spectrum, but Figure 8 publishes the exact cube ground-state curve. The source PDF retains that black curve as a 61-point vector path.

The reconstruction script extracted the path and vector tick locations directly, then diagonalized the reconstructed cube matrix at the same 61 values from \(g=0.8\) through \(g=2.0\). With the paper normalization \(H=g^2K\) and the same omitted additive constant:

| Check | Result |
|---|---:|
| points compared | 61 |
| maximum absolute energy discrepancy | \(5.59\times10^{-8}\) |
| RMS energy discrepancy | \(1.88\times10^{-8}\) |

This is at the coordinate precision of the vector figure. It is a strong end-to-end check that the independently assembled physical block is the matrix underlying the authors' published cube ED curve.

## What this establishes—and what it does not

### Established

- The public Balaji/`ymcirc` local data determine an exact 243-state physical \(B=4=T_1\) open-cube Hamiltonian.
- That matrix reproduces the authors' published 61-point exact ground-state curve.
- Its independently projected \(C=-\) one-face shell has exactly \(1+3+2\) multiplicities.
- Its complete second-order gap matrix is \(37I/12-G/12\).
- The truncated-cube relative coefficients are exactly \(0^{(1)},(-1/3)^{(3)},(-1/2)^{(2)}\), confirming the predicted negative \(T_1\) kinetic coefficient and reversed ordering.

### Not established by this run

- The channel-complete \(+(5/612)G\) coefficient has not been tested against a full \(B=6\) open-cube matrix; the public \(d=3\) table currently stops at \(B=4\).
- This does not identify the shell as a continuum glueball multiplet or prove persistence toward the continuum limit.
- The authors' original full tensor-product sparse matrix and their private ED code were not recovered.
- This is not an independent-group replication: the paper, `ymcirc`, and `pyclebsch` share an author/code lineage.
- The public `ymcirc` and `pyclebsch` repositories do not currently state an explicit software/data license; publication or redistribution of their raw table or code therefore requires separate permission or a clean-room release plan.

The honest conclusion is therefore:

> **The decisive \(B=4=T_1\) author-data reconstruction is now complete.** The one-cube Hamiltonian independently assembled from the authors' public master coefficients reproduces their published exact ground curve and exhibits the predicted \(1+3+2\) charge-odd shell with the exact truncated-theory coefficients. The remaining stronger test is the channel-complete \(B=6\) cube, which would decide the predicted sign reversal after the \(\mathbf6\) and \(\mathbf8\) channels are restored.

## Reproducibility artifacts

- `reconstruct_balaji_open_cube.py` — fail-closed reconstruction, projection, Schur complement, finite-(u) diagonalization, and published-curve comparison.
- `balaji_open_cube_B4_T1_hamiltonian.npz` — matrix family data and bases. Use
  \(K(u)=\operatorname{diag}(\texttt{electric\_diagonal})-u\,\texttt{magnetic\_box\_plus\_dagger}\).
- `balaji_open_cube_B4_T1_certificate.json` — machine-readable provenance, diagnostics, exact shell result, finite-(u) results, and curve comparison.
- `balaji_open_cube_padding_audit_certificate.json` — independent direct-open-boundary versus padded-periodic coefficient audit, with all 486 cube-face comparisons recorded.

Current hashes:

- Matrix NPZ: `b65b1e911a6bff0e669a1eeccfae908938562917993dfcdd3b4d66accc4e9378`
- Certificate JSON: `36687f407dfbb1c4b56183f21f7ed5eae22a330db07dd70fa51de379291100d8`
- Padding-audit JSON: `3a253bf551d74133e82c09a0805e36d651dbfaa68f604b2467109719cb80e1f9`

## Primary references

- P. Balaji et al., [“Perturbation theory, irrep truncations, and state preparation methods for quantum simulations of SU(3) lattice gauge theory,” arXiv:2509.25865v3](https://arxiv.org/abs/2509.25865), published as *Phys. Rev. D* **113**, 094505 (2026), DOI [10.1103/m719-7tdf](https://doi.org/10.1103/m719-7tdf).
- `ymcirc` [PR #76, “Feature/more B truncations”](https://github.com/hepqis-uiuc/ymcirc/pull/76), which added circuit-construction data for \(d=3,B=4\).
- N. Kimura, [“Glueball spectroscopy from strong coupling expansions in Hamiltonian lattice QCD,” *Nucl. Phys. B* **246** (1984) 143–156](https://www-library.desy.de/preparch/desy/postpr/1984/desy84-010.pdf), Table 2.
