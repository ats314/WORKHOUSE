# Finite-Order Nested-Quotient Spectral Reduction Theorem

## Evidence-calibrated two-cube SU(3) adjacent-hopping closure through \(O(u^2)\)

*A derivation-first supplement for the charge-odd adjacent-hopping result on the open face-sharing two-cube prism*

- Derivation and release date: 29 August 2026
- Geometry: finite open \((3,2,2)\) face-sharing two-cube prism
- Sector: complete charge-odd one-plaquette shell at \(E_*=8/3\)
- Perturbative order: Bloch/Feshbach through \(O(u^2)\)
- Hamiltonian convention: \(H(u)=E-uM\)
- Claim status: established under, and conditional on, the pinned numerical-to-rational protocol
- Final B4 manifest root: `bcdef84df480ecf7effb17b64ebdb90cc3283674f9f74a03acca27c0ed3ee750`
- Final B6 manifest root: `021558ce5bea60e43f757d76c1b8122f15f355c1e5174304f440cce5d98d422b`

---

## Abstract: the result first

Within this corpus, the following outcome is established under, and conditional on, the pinned numerical-to-rational protocol: the one-cube limitation is resolved for one precise claim, the local adjacent-face hopping term in the finite open two-cube SU(3) prism through second order. The result is no longer inferred from an isolated cube or a graph ansatz. It is obtained on an actual face-sharing two-cube gauge-invariant Hilbert space, with the complete degenerate shell removed from the resolvent and with left-cube, right-cube, and shared-face contributions subtracted at the operator level.

For the B4 truncation,

\[
K^{(2),B4}_{\mathrm{conn}}
=-\frac1{12}G_{\mathrm{conn}}+D_{B4}.
\]

For the exact-Casimir B6 truncation, all six one-action shared-link representation channels are reached and retained, and

\[
\boxed{
K^{(2),B6}_{\mathrm{conn}}
=\frac5{612}G_{\mathrm{conn}}+D_{B6}.
}
\]

The coefficient is reconstructed channel by channel:

\[
\frac1{12}-\frac1{12}-\frac1{12}
-\frac1{9}-\frac1{9}+\frac{16}{51}
=\frac5{612}.
\]

The three channels already visible at B4 sum to \(-51/612\); the restored \(\mathbf6\), \(\bar{\mathbf6}\), and \(\mathbf8\) channels contribute \(+56/612\). Their net effect reverses the sign of the B4 hopping coefficient. This is the operator-level mechanism exposed here.

The closure is deliberately narrow. The adjacent hopping coefficient is channel-complete at \(O(u^2)\). The diagonal remainder \(D_{B6}\) is B6-truncated and has not been proved stable under larger cutoffs. Neither the complete two-cube Hamiltonian at finite coupling nor any larger-volume, continuum, infinite-volume, or mass-gap statement follows.

---

## 1. Authority and relation to the existing masters

This is a synthesis supplement. The detached B4 and B6 manifests and their listed artifacts remain the canonical scientific authorities. This text becomes master authority only if explicitly promoted. Until then, it supplements, rather than silently overwrites, the current general masters:

| Existing document | Relation of this document |
| --- | --- |
| [Nested-Quotient Gauge Spectral Theory: Proven Derivations](./Nested_Quotient_Gauge_Spectral_Theory_Proven_Derivations.md) | Supplements the evidence-calibrated master and replaces its earlier one-cube-only scope sentence for adjacent hopping through \(O(u^2)\). |
| [Finite-Order Nested-Quotient Spectral Reduction Theorem](./FINITE_ORDER_NESTED_QUOTIENT_SPECTRAL_REDUCTION_THEOREM_FULL_DERIVATION_2026-08-28.md) | Adds the two-cube \(r=2\) specialization and its B6 adjacent-coefficient channel-closure corollary. |
| [Canonical Folded Theory](./CANONICAL_FOLDED_THEORY_2026-08-20.md) | Preserves its temporal-history, quotient, Feshbach, Möbius, and scalar/shape hierarchy; no unrelated cubic or pentagonal claim is changed. |
| [B4 two-cube derivation note](./TWO_CUBE_B4_CODD_O2_CONNECTED_KERNEL_2026-08-29.md) | Remains the detailed B4 implementation and certificate guide. It is not superseded. |
| [B6 two-cube derivation note](./TWO_CUBE_B6_CODD_O2_CONNECTED_KERNEL_2026-08-29.md) | Remains the detailed B6 implementation and certificate guide. It is not superseded. |

The project keeps three axes separate:

| Axis | Values used here | Meaning |
| --- | --- | --- |
| Claim status | proven, conditional, open, superseded | What is asserted within the stated regulator and protocol |
| Verification tier | T1, T2, T3 | Exact/rational reconstruction, numerical validation, or documentary chronology |
| Evidence kind | analytic, cold-reproduced, output-certified, numerical, record-backed | How the assertion was established |

The rational matrices and channel identities are T1 relative to pinned finite-precision inputs. The finite-\(u\) convergence checks are T2. The ordering of blind construction and later comparison is record-backed; it is not a cryptographic preregistration. These statuses describe evidence within this corpus and do not establish a universal priority claim.

---

## 2. Specialization of the umbrella theorem

The general finite-order nested-quotient theorem writes a physical effective operator as

\[
H_{\mathrm{eff}}^{(r)}
=
\sum_{[h]\in\mathscr H_r^{\mathrm{phys}}}
\mathcal A_N[h]T_h+F_r,
\]

where \([h]\) is an energy-decorated ordered temporal history after the physical Haar/Gram quotient, \(T_h\) is its retained-space action, and \(F_r\) contains the proper Feshbach folds. Connected cluster data are obtained only after support-resolved Möbius subtraction.

The present result is the \(r=2\), finite-open-cluster specialization. Its retained space is the full charge-odd one-plaquette eigenshell, its history graph contains every retained numerically nonzero two-action path under the sealed threshold protocol through the reduced resolvent, and its support poset is

\[
\{LR,L,R,F\},
\]

where \(LR\) is the two-cube target, \(L\) and \(R\) are the source cubes, and \(F=L\cap R\) is the shared face.

### Theorem 2.1 — two-cube charge-odd adjacent-hopping closure

Let \(H(u)=E-uM\) be the open two-cube SU(3) Hamiltonian in either the B4 or exact-Casimir B6 truncation. Let \(P\) project onto the complete charge-odd one-plaquette shell at \(E_*=8/3\). Construct every source operator with the same coupling sign, normalization, electric energy, zero-denominator policy, and coordinate embeddings, and perform the literal operator-level Möbius transform

\[
\mathfrak M[K]
=K_{LR}-J_LK_LJ_L^\dagger-J_RK_RJ_R^\dagger+J_FK_FJ_F^\dagger.
\]

Then:

1. \(PVP=I_{11}\), while \(\mathfrak M[PVP]=0\).
2. At B4,
   \[
   \mathfrak M[K_2]
   =-\frac1{12}G_{\mathrm{conn}}+D_{B4}.
   \]
3. At B6, every shared-link irrep reachable in one magnetic action is present, and
   \[
   \mathfrak M[K_2]
   =\frac5{612}G_{\mathrm{conn}}+D_{B6}.
   \]
4. Consequently, the adjacent-face hopping coefficient changes sign between B4 and the B6 calculation that exhausts the adjacent shared-link channels at this order.

The conclusion applies to the connected off-diagonal adjacent-hopping term through \(O(u^2)\). It does not assert cutoff-completeness of \(D_{B6}\) or of the full Hamiltonian.

### Proof strategy

The proof has five finite steps.

1. Exhaust the \(E_*\) eigenspace and prove that the eleven normalized charge-odd plaquette columns span its complete odd half.
2. Enumerate every retained numerically nonzero one-action path under the sealed threshold protocol and remove the entire \(E_*\) eigenspace from the pseudoinverse.
3. Sum every ordered two-action history and independently contract the diagonal resolvent.
4. Construct the incidence Gram matrix from geometry alone and classify each adjacent history by the exact irrep on its unique common link.
5. Form source operators in source coordinates, lift them, and apply the Möbius transform before any spectral comparison.

Sections 3–7 give these steps explicitly.

---

## 3. Frozen convention, shell, and projectors

Write

\[
H(u)=H_0+uV,
\qquad
H_0=E,
\qquad
V=-M,
\]

with

\[
M=\sum_p\left(W_p+W_p^\dagger\right).
\]

For each of the eleven oriented plaquettes \(p\), define

\[
|q_p\rangle
=\frac{i}{\sqrt2}(W_p-W_p^\dagger)|0\rangle,
\qquad
Q_-=(|q_1\rangle,\ldots,|q_{11}\rangle).
\]

The phase and \(1/\sqrt2\) normalization are part of the theorem. In both truncations,

\[
Q_-^\dagger Q_-=I_{11},
\qquad
P=Q_-Q_-^\dagger.
\]

Let \(P_*\) be the projector onto the entire \(E_*\) eigenspace, including both charge sectors, and let

\[
\bar P_*=I-P_*.
\]

The reduced resolvent is the full pseudoinverse

\[
R_*=(E_*-H_0)^+
=\bar P_*\frac1{E_*-H_0}\bar P_*.
\]

Thus every zero denominator is removed, not merely the eleven displayed odd columns. If \(Q=I-P\) is used after restriction to the charge-odd sector, then \(Q\) and the full-space prescription agree because \(Q_-\) exhausts the odd \(E_*\) eigenspace. The implementation nevertheless performs the stronger full-space removal of all 22 states.

Bloch/Feshbach perturbation theory gives

\[
H_{\mathrm{eff}}(u)
=E_*P+uK_1+u^2K_2+O(u^3),
\]

with

\[
K_1=PVP,
\qquad
K_2=PVR_*VP.
\]

Because \(V=-M\), the two minus signs cancel at second order:

\[
K_2=PMR_*MP.
\]

For an intermediate physical state \(|m\rangle\), the ordered-history weight is

\[
\mathcal A[m;f,i]
=
\frac{\langle q_f|V|m\rangle
      \langle m|V|q_i\rangle}
     {E_*-E_m}.
\]

Direct contraction, expressed in the orthonormal \(Q_-\) coordinates, gives

\[
\boxed{PVP=I_{11}.}
\]

The first-order term is therefore nonzero but scalar on the retained shell. Under the connected support transform, the target identity is exactly canceled by the two lifted cube identities with the shared-face inclusion restored:

\[
\boxed{K^{(1)}_{\mathrm{conn}}=0.}
\]

This distinguishes a scalar first-order shift from connected transport.

---

## 4. Geometry and literal operator-level Möbius subtraction

Let

\[
\partial_2\in\mathbb Z^{20\times11}
\]

be the signed oriented link-by-plaquette cellular boundary operator, with links as rows and plaquettes as columns. The serialized array `incidence_boundary` uses the face-by-link row convention

\[
B_{\mathrm{row}}=\partial_2^\mathsf T
\in\mathbb Z^{11\times20}.
\]

The face Gram matrix is therefore

\[
\boxed{
G=\partial_2^\mathsf T\partial_2
=B_{\mathrm{row}}B_{\mathrm{row}}^\mathsf T.
}
\]

The source embeddings are

\[
I_L=(0,1,2,3,4,7),
\quad
I_R=(5,6,7,8,9,10),
\quad
I_F=(7).
\]

The connected geometry is

\[
G_{\mathrm{conn}}
=G-J_LG_LJ_L^\mathsf T-J_RG_RJ_R^\mathsf T+J_FG_FJ_F^\mathsf T.
\]

Its only nonzero off-diagonal pairs are

\[
(0,5),\ (1,6),\ (3,8),\ (4,9)
\]

and their transposes, each with \((G_{\mathrm{conn}})_{ab}=-1\).

The physical connected operator is not obtained by subtracting eigenvalues or fitted coefficients. Each source Hamiltonian is folded in its own physical coordinates, lifted with its certified embedding, and subtracted as an operator:

\[
\boxed{
K_{\mathrm{conn}}
=K_{LR}-J_LK_LJ_L^\dagger-J_RK_RJ_R^\dagger+J_FK_FJ_F^\dagger.
}
\]

The identical inclusion–exclusion weights are also attached to individual temporal histories. Agreement between the history sum and the matrix-level transform is a required gate.

---

## 5. B4 derivation

### 5.1 Complete shell census

The B4 two-cube gauge-invariant basis has dimension 8,361. The entire \(E_*=8/3\) eigenspace has dimension 22. Tensor-derived charge conjugation has trace zero there and splits it as

\[
22=11_{C=+1}\oplus11_{C=-1}.
\]

The eleven columns of \(Q_-\) have rank eleven and Gram residual \(2.22\times10^{-16}\); hence they exhaust the complete odd zero-denominator sector. The full implementation removes all 22 zero-denominator states.

### 5.2 Raw and connected histories

The sealed ledger contains 1,236 ordered, retained numerically nonzero two-action histories under the sealed threshold protocol. Under the support Möbius weights,

\[
764\ \text{histories cancel},
\qquad
472\ \text{histories survive}.
\]

The raw history sum agrees with direct contraction to \(3.56\times10^{-15}\), and the connected history sum agrees with the operator-level transform to \(2.66\times10^{-15}\).

### 5.3 Connected coefficient, diagonal remainder, and spectrum

For every nonzero off-diagonal geometry entry,

\[
(K_2^{B4})_{ab}=-\frac1{12}G_{ab}.
\]

After literal subcluster subtraction,

\[
\boxed{
K^{(2),B4}_{\mathrm{conn}}
=-\frac1{12}G_{\mathrm{conn}}+D_{B4},
}
\]

where

\[
D_{B4}=\operatorname{diag}
\left(
-\frac74,-\frac74,-\frac{15}{4},-\frac74,-\frac74,
-\frac74,-\frac74,0,-\frac74,-\frac74,-\frac{15}{4}
\right).
\]

The cross-cell off-diagonal entries are therefore \(+1/12\). The spectrum of the serialized rational \(11\times11\) connected kernel is

\[
\boxed{
0^{\times1},
\quad
\left(-\frac{15}{4}\right)^{\times2},
\quad
\left(-\frac{11}{6}\right)^{\times4},
\quad
\left(-\frac53\right)^{\times4}.
}
\]

This matrix is not globally proportional to \(G_{\mathrm{conn}}\); the nonuniform diagonal remainder is retained rather than hidden in a graph fit. It is not the rooted scalar of the general master theorem.

### 5.4 B4 held-out validation

Direct diagonalization of the complete 4,180-dimensional charge-odd block of \(H_0-uM\) was performed at training points \(u=0.004,0.008\) and held-out points \(u=0.002,0.006\). Across all four points, the error after subtracting

\[
E_*+u+u^2\operatorname{eig}(K_2)
\]

is consistent with an \(O(u^3)\) remainder: the maximum error divided by \(u^3\) remains between approximately 2.22 and 2.26, and the held-out scaled-error ratio is 0.98817. A deterministic 8,361-state fourth-root rephasing leaves both \(PVP\) and \(K_2\) invariant after transport.

These checks validate the B4 finite Hamiltonian and phase convention. They do not make the B4 adjacent coefficient channel-complete, because the sextet and adjoint routes are absent.

---

## 6. B6 basis and reachable-space completeness

### 6.1 Gauge-invariant basis

The exact-Casimir B6 truncation retains

\[
\mathbf1,\ \mathbf3,\ \bar{\mathbf3},\ \mathbf6,\ \mathbf8,\ \bar{\mathbf6}.
\]

After every local singlet constraint and every intertwiner multiplicity is resolved,

\[
\boxed{\dim\mathcal H_{B6}=1{,}590{,}462.}
\]

There are 24 trivalent local singlets. At a four-valent vertex, 81 irrep tuples produce 87 multiplicity-resolved singlets, including six genuine two-dimensional intertwiner blocks.

### 6.2 Exhaustive \(E_*\) census

Exact enumeration of all nonnegative B6 irrep-energy partitions at \(8/3\) shows that the shell can contain only four links of energy \(2/3\), carried by \(\mathbf3\) or \(\bar{\mathbf3}\). Exhausting the four-link supports, all conjugacy assignments, and all compatible local multiplicities produces exactly 22 states. Tensor-derived charge conjugation gives

\[
\boxed{22=11_{C=+1}\oplus11_{C=-1}.}
\]

Again, \(Q_-^\dagger Q_-=I_{11}\), its columns contain all 22 oriented ranks, and the full 22-dimensional eigenspace is removed from \(R_*\).

### 6.3 Complete one-action image

The B6 magnetic matrix is never assembled at dimension 1,590,462. Instead, every retained numerically nonzero local path under the sealed threshold protocol is generated, glued into a physical global state, and ranked. Acting on all eleven shell columns yields

\[
\boxed{794\ \text{unaccumulated paths},\qquad398\ \text{distinct reachable states}.}
\]

Every retained irrep is reached. Both rows of the multiplicity-two intertwiners occur; 32 reachable local labels use the second row. Tensor-derived charge conjugation \(C\) and cube exchange \(U_x\) were evaluated on 896 local blocks, including 48 full \(2\times2\) blocks. Their involution, unitarity, commutation, shell covariance, and all 794 transition-ordinal covariance gates pass at residuals no larger than \(4.44\times10^{-16}\).

This is why a scalar-channel approximation is insufficient: the calculation actually visits non-scalar multiplicity blocks.

### 6.4 Why the six channels exhaust adjacent hopping at B6

Before evaluating their amplitudes, the possible adjacent shared-link channels can be exhausted representation-theoretically. A one-plaquette shell state carries \(\mathbf3\) or \(\bar{\mathbf3}\) on the link shared by an adjacent face. One Wilson action tensors that link by \(\mathbf3\) or \(\bar{\mathbf3}\). Hence

\[
\mathbf3\otimes\mathbf3=\mathbf6\oplus\bar{\mathbf3},
\qquad
\mathbf3\otimes\bar{\mathbf3}=\mathbf1\oplus\mathbf8,
\]

together with the conjugate products

\[
\bar{\mathbf3}\otimes\bar{\mathbf3}=\bar{\mathbf6}\oplus\mathbf3,
\qquad
\bar{\mathbf3}\otimes\mathbf3=\mathbf1\oplus\mathbf8.
\]

Their union is exactly

\[
\{\mathbf1,\mathbf3,\bar{\mathbf3},\mathbf6,\bar{\mathbf6},\mathbf8\}.
\]

The largest endpoint exact-Casimir budget is

\[
C_2(\mathbf6)+2C_2(\mathbf3)
=\frac{10}{3}+2\frac43=6,
\]

while the adjoint endpoint budget is

\[
C_2(\mathbf8)+2C_2(\mathbf3)
=3+2\frac43=\frac{17}{3}.
\]

Both lie within B6. Thus B6 retains every representation channel available to adjacent one-action intermediates and therefore every adjacent off-diagonal route contributing through \(O(u^2)\). This argument does not exhaust same-face diagonal, onsite/rest, higher-action, or untruncated-Hilbert-space contributions.

---

## 7. B6 folded operator and channel mechanism

### 7.1 Resolvent census and reciprocal guard

Exactly 22 one-step paths land in the excluded \(E_*\) eigenspace. After their removal and path accumulation, 364 distinct intermediate ranks contribute. This contributing-rank count and the earlier 398-state reachability census measure different stages of the construction. The ordered-history contraction uses

\[
\frac1{E_*-E_m},
\]

not \(E_*-E_m\). An independent diagonal-resolvent contraction agrees with the history fold exactly at stored precision. The deliberately wrong multiplication-by-energy-gap control differs by

\[
45.6895424836602,
\]

fixing both the reciprocal and its sign.

### 7.2 History census and Möbius fold

The B6 ledger contains 1,984 ordered, retained numerically nonzero two-step histories under the sealed threshold protocol:

\[
1{,}192\ \text{have Möbius weight }0,
\qquad
792\ \text{survive with weight }1.
\]

The literal history sum and operator-level source subtraction agree within \(4.88\times10^{-15}\). The first-order identity cancels exactly.

### 7.3 Six exact shared-link channels

For an adjacent ordered face pair, the channel label is the exact irrep on the unique common link of the intermediate ranked state. The six coefficients are

| Shared-link irrep \(\rho\) | \(\mathbf1\) | \(\mathbf3\) | \(\bar{\mathbf3}\) | \(\mathbf6\) | \(\bar{\mathbf6}\) | \(\mathbf8\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| \(c_\rho\) | \(1/12\) | \(-1/12\) | \(-1/12\) | \(-1/9\) | \(-1/9\) | \(16/51\) |
| Ordered shared-link histories | 336 | 56 | 56 | 56 | 56 | 112 |

Every channel matrix is separately proportional to \(G\) off diagonal, and every connected channel matrix is separately proportional to \(G_{\mathrm{conn}}\). Same-face histories retain their ordered four-link signature, while disjoint histories are labeled `no_shared_link`; neither class is forced into a graph channel.

Summing the six contributions gives

\[
\begin{aligned}
c_{B6}
&=\frac1{12}-\frac1{12}-\frac1{12}
-\frac1{9}-\frac1{9}+\frac{16}{51}\\
&=\frac{51-51-51-68-68+192}{612}\\
&=\boxed{\frac5{612}}.
\end{aligned}
\]

The sign reversal is exposed by grouping old and restored channels:

\[
\underbrace{
\frac1{12}-\frac1{12}-\frac1{12}
}_{\text{legacy channels}}
=-\frac{51}{612},
\]

\[
\underbrace{
-\frac19-\frac19+\frac{16}{51}
}_{\mathbf6+\bar{\mathbf6}+\mathbf8}
=\frac{56}{612},
\]

and therefore

\[
-\frac{51}{612}+\frac{56}{612}=\frac5{612}.
\]

The adjoint contribution is large enough to overcome both negative sextet contributions and the negative legacy sum.

### 7.4 Connected matrix decomposition and reduced spectrum

The full \(11\times11\) connected B6 second-order shell matrix is

\[
\boxed{
K^{(2),B6}_{\mathrm{conn}}
=\frac5{612}G_{\mathrm{conn}}+D_{B6},
}
\]

with

\[
D_{B6}
=\frac1{612}\operatorname{diag}
(-2317,-2317,-2295,-2317,-2317,
-2317,-2317,0,-2317,-2317,-2295).
\]

The four connected cross-cell pairs have matrix element \(-5/612\). In the geometry-adapted block decomposition, four identical \(2\times2\) pair blocks produce the two fourfold eigenvalues; two isolated directions produce \(-15/4\), and the shared-face shell direction produces zero. Thus

\[
\boxed{
\operatorname{spec}K^{(2),B6}_{\mathrm{conn}}
=
0^{\times1}
\oplus
\left(-\frac{15}{4}\right)^{\times2}
\oplus
\left(-\frac{34}{9}\right)^{\times4}
\oplus
\left(-\frac{129}{34}\right)^{\times4}.
}
\]

The nonuniform diagonal \(D_{B6}\) includes B6-truncated same-face and other-sector information. It is retained explicitly, but it is **not** the rooted scalar of the general master theorem and is **not** claimed to be complete in untruncated SU(3).

---

## 8. Independent reconstruction and validation evidence

Validation uses distinct internal cross-checks that attack different failure modes; they are not unaffiliated reproductions.

### 8.1 Independent constructions

- The link-by-plaquette boundary \(\partial_2\), its serialized transpose \(B_{\mathrm{row}}\), and \(G_{\mathrm{conn}}\) are derived from oriented geometry before the contraction.
- Filtered on-demand transitions agree with complete upstream plaquette tables on one mixed-valence and one all-trivalent face, with identical key sets and zero amplitude error at stored precision.
- The ordered-history sum and an independent diagonal-resolvent contraction agree exactly at stored precision.
- The left source fold agrees with the independently stored 3,864-state one-cube B6 operator: \(PVP\) differs by at most \(2.22\times10^{-16}\), and \(K_2\) by at most \(8.88\times10^{-16}\).
- Tensor-derived \(C\) and \(U_x\), rather than symmetries fitted from \(K_2\), commute with the raw and connected operators.

The 3,864-state comparison is only a source-fold normalization and convention check. No one-cube spectrum, word-space dimension, or finite-coupling conclusion is transferred to the 1,590,462-state two-cube calculation.

### 8.2 The 66-dimensional held-out star

An energy-decorated word space containing the eleven shell vectors and all exact-energy projected one-action images has dimension

\[
11+55=66.
\]

It recovers \(PVP\) exactly and the raw second-order operator within

\[
6.22\times10^{-15}.
\]

At

\[
u\in\left\{\frac1{127},\frac1{97},\frac1{73},\frac1{59}\right\},
\]

the correct second-order residual has log-log slope

\[
2.901745,
\]

while reversing the sign of \(K_2\) gives slope

\[
2.002000.
\]

The minimum wrong-sign to correct-error ratio is

\[
324.86.
\]

This strongly separates the correct Feshbach sign from the wrong-sign control. The calculation is nevertheless only the 66-dimensional \(P+Q_1\) star with the \(Q_1\)-to-\(Q_1\) magnetic block set to zero. It is not a full finite-\(u\) diagonalization of the 1,590,462-dimensional two-cube Hamiltonian.

### 8.3 Radius-three boundary

The next-radius preflight processed 16 of 55 radius-two frontier vectors, already generated 127 new directions, and cached 196 physical ranks before it was stopped. Therefore no radius-three convergence, larger-word-space stability, or cutoff stability is claimed.

---

## 9. Target blindness, chronology, and exactness firewalls

### 9.1 What target-blind means here

The target \(5/612\) also occurs in sealed nested-B4 post-hoc metadata and source paths, and the comparator source existed before the B6 execution. The B6 scientific builder, graph construction, branching logic, held-out validator, scientific tests, and scientific replay dependency path never parse that target and never invoke the comparator. The final release manifest classifies the comparator as `posthoc_only`, and the scientific replay role set excludes it.

The record shows that the B6 artifact and history-ledger hashes were first produced before the recorded comparator execution. The final regenerative package was resealed afterward without changing either the artifact bytes or the ledger bytes. This establishes record-backed runtime data-flow target blindness. It does **not** establish a cryptographic preregistration or a publicly timestamped prediction; the chronology remains only partially independently auditable.

The stronger statement “\(5/612\) occurs nowhere in the corpus” would be false. The B6 executable construction and replay path hash the nested package as an authority object but do not parse or use its target-bearing post-hoc fields or source paths. The defensible claim is therefore dependency-path nonuse, not corpus-wide byte absence or cryptographic chronology.

### 9.2 Numerical-to-rational boundary

Electric energies, incidence matrices, energy denominators, Möbius weights, integer numerators, and final rational serialization are exact after reconstruction. The local Wilson amplitudes originate from hash-pinned, approximately 14-digit finite-precision CGCs. Continued-fraction reconstruction uses a maximum denominator of 1,000,000 and is accepted only after small residuals and independent contraction checks. The largest B6 reported reconstruction residual is below \(2.14\times10^{-14}\).

Accordingly,

> “Exact” in the matrix and coefficient statements means exact rational serialization under the pinned numerical-to-rational protocol. It is not a formal symbolic-CGC or exact-arithmetic Haar proof.

### 9.3 Same-builder replay boundary

Both releases provide deterministic byte-for-byte replay. This proves reproducibility of the sealed construction but is not an independent scientific implementation. Independence comes only from the separately constructed geometry, diagonal-resolvent contraction, full-table transition comparisons, tensor symmetries, one-cube source check, and finite-\(u\) control calculations. External-group replication remains open.

---

## 10. What “the one-cube scope is resolved” now means

The phrase has a precise, limited meaning.

| Question | Before this closure | After this closure |
| --- | --- | --- |
| Is the hopping coefficient inferred only from one cube? | Yes; the decisive validation chain stopped at isolated-cube data. | No. It is derived on a genuine face-sharing two-cube Hilbert space. |
| Is connectedness imposed by a fitted scalar subtraction? | Not decisively excluded. | No. Left, right, and shared-face operators are lifted and Möbius-subtracted literally. |
| Is the B6 sign reversal only a proposed channel story? | Yes. | No. All six channels are reached, separately contracted, and sum to \(5/612\). |
| Is adjacent hopping closed through \(O(u^2)\)? | Not with all B6 adjacent shared-link channels retained. | Yes, for the adjacent off-diagonal coefficient in this finite open two-cube sector and convention. |
| Is the complete diagonal or finite-coupling Hamiltonian closed? | No. | Still no. |
| Are larger volumes, radius three, cutoff stability, or continuum limits closed? | No. | Still no. |

Thus the one-cube-only objection is resolved for the first such multi-cube instance in this corpus: the local connected two-cube adjacent-hopping coefficient at second order. It is not a statement that one cube suffices for all observables, nor that the two-cube cluster settles thermodynamic propagation.

---

## 11. Novelty and impact assessment

Within this program, the result is a stronger specialist theorem, a distinctive contribution, and a demonstrated computational capability.

Its strongest novelty candidate within this corpus is not merely the fraction \(5/612\). It is the end-to-end demonstration that a finite temporal-history graph, full zero-denominator removal, multiplicity-resolved SU(3) transitions, literal subcluster Möbius subtraction, and a clean regenerative release can recover the complete B6 adjacent off-diagonal coefficient at this order without assembling the 1.59-million-dimensional magnetic matrix. This is a program-scoped assessment, not a universal priority claim.

The sign reversal matters because it is a qualitative regulator effect with an explicit representation-theoretic cause. B4 gives the opposite sign when the \(\mathbf6\), \(\bar{\mathbf6}\), and especially \(\mathbf8\) paths are omitted. The calculation therefore identifies exactly which restored channels change the low-energy transfer operator and by how much.

It should not yet be presented as field-changing on current evidence. The theorem remains finite-volume, second-order, strong-coupling, and sector-specific; the diagonal lacks an untruncated completeness proof; the finite-\(u\) two-cube test is a 66-dimensional star rather than the full Hamiltonian; radius three and larger clusters are unexecuted; and no independent external group has reproduced the release. A larger-volume or higher-order calculation that changes what can be computed in practice, followed by external reproduction, would materially raise the impact.

---

## 12. Changes to the master claims

| Earlier master claim or limitation | New statement | Status after this supplement |
| --- | --- | --- |
| The decisive capability evidence is one-cube only. | A literal face-sharing two-cube connected calculation now exists at B4 and with exact-Casimir-B6 channel closure for the adjacent off-diagonal coefficient through \(O(u^2)\). | Superseded within this corpus for adjacent hopping at second order. |
| The B6 two-cube value \(5/612\) is prospective. | The target-blind B6 contraction recovers \(5/612\) and exposes its six-channel sum. | Proven within the B6 numerical-to-rational protocol. |
| The B4 coefficient \(-1/12\) has no actual two-cube operator realization. | The 8,361-state B4 construction gives \(-\frac1{12}G_{\mathrm{conn}}+D_{B4}\) with 1,236 histories and literal source subtraction. | Proven within B4. |
| The sign reversal is a qualitative prediction. | Legacy channels contribute \(-51/612\); restored channels contribute \(+56/612\); total \(+5/612\). | Closed at B6 through \(O(u^2)\). |
| “Full SU(3)” can be attached to the entire B6 operator. | Channel completeness applies only to the adjacent off-diagonal coefficient at this order; \(D_{B6}\) and the whole Hamiltonian remain B6-truncated. | Scope narrowed and clarified. |
| Two-cube finite-coupling validation is complete. | Only the 66-dimensional \(P+Q_1\) star is validated at held-out \(u\); the full finite-\(u\) two-cube problem is open. | Open. |
| Chronology can be described as preregistered. | Runtime target blindness is established; chronology is record-backed, not cryptographically preregistered. | Claim corrected. |

No cubic off-axis, rooted fourth-order scalar, pentagonal, continuum, or infinite-volume claim is changed by this supplement.

---

## 13. Theorem/corollary insertion text for the existing master

The following block can be inserted after the all-rank shared-link discussion in the focused umbrella theorem, or as a new post-snapshot appendix in the evidence-calibrated master.

> ### Corollary — exact-Casimir-B6 channel closure for SU(3) adjacent hopping through \(O(u^2)\)
>
> On the finite open face-sharing \((3,2,2)\) prism, let \(P\) be the complete eleven-dimensional charge-odd one-plaquette shell at \(E_*=8/3\), let \(H=E-uM\), and remove the full 22-dimensional \(E_*\) eigenspace from \((E_*-H_0)^+\). Let \(\partial_2\in\mathbb Z^{20\times11}\) be link-by-plaquette incidence, let the serialized row convention be \(B_{\mathrm{row}}=\partial_2^\mathsf T\), and set \(G=\partial_2^\mathsf T\partial_2=B_{\mathrm{row}}B_{\mathrm{row}}^\mathsf T\). With literal left/right/shared-face operator Möbius subtraction,
> \[
> PVP=I_{11},
> \qquad
> K^{(1)}_{\mathrm{conn}}=0.
> \]
> At B4,
> \[
> K^{(2),B4}_{\mathrm{conn}}
> =-\frac1{12}G_{\mathrm{conn}}+D_{B4}.
> \]
> The shared link initially carries \(\mathbf3\) or \(\bar{\mathbf3}\), and one Wilson action tensors it by \(\mathbf3\) or \(\bar{\mathbf3}\). The decompositions \(\mathbf3\otimes\mathbf3=\mathbf6\oplus\bar{\mathbf3}\), \(\mathbf3\otimes\bar{\mathbf3}=\mathbf1\oplus\mathbf8\), and their conjugates exhaust \(\mathbf1,\mathbf3,\bar{\mathbf3},\mathbf6,\bar{\mathbf6},\mathbf8\). The maximal endpoint budget is \(C_2(\mathbf6)+2C_2(\mathbf3)=6\), while the adjoint budget is \(17/3\); both lie within B6. Thus exact-Casimir B6 retains every adjacent shared-link route contributing through \(O(u^2)\), and
> \[
> K^{(2),B6}_{\mathrm{conn}}
> =\left(
> \frac1{12}-\frac1{12}-\frac1{12}
> -\frac19-\frac19+\frac{16}{51}
> \right)G_{\mathrm{conn}}+D_{B6}
> =\frac5{612}G_{\mathrm{conn}}+D_{B6}.
> \]
> Hence the adjacent-hopping coefficient reverses sign when the sextet and adjoint routes are restored. Here “channel-complete” means only the adjacent off-diagonal coefficient at this order. \(D_{B6}\) is a B6-truncated diagonal remainder, not a rooted scalar and not an onsite/rest closure. No untruncated diagonal, full finite-\(u\), cutoff-stability, transport, infinite-volume, or continuum claim is made. The fractions are rational reconstructions from pinned finite-precision CGCs, not formal symbolic-CGC identities.

---

## 14. Evidence ledger

The manifests, not filenames containing “master” or “final,” define the release roots. The table links the principal evidence; each manifest seals the remaining implementation closure in exact order.

| Release role | Authoritative file | SHA-256 | Claim supported |
| --- | --- | --- | --- |
| B4 detached root | [B4 manifest](./two_cube_b4_codd_o2_connected_kernel_manifest.json) | `bcdef84df480ecf7effb17b64ebdb90cc3283674f9f74a03acca27c0ed3ee750` | Exact ordered ten-role B4 release and detached-manifest convention |
| B4 operator | [B4 NPZ](./two_cube_b4_codd_o2_connected_kernel.npz) | `259174b82e8007432d38a98f338bf09b5326d1f0c7a7f8577c9ac63e01ba1b88` | Serialized shell, raw/connected matrices, graph decomposition, and spectrum of the serialized rational \(11\times11\) kernel |
| B4 certificate | [B4 certificate](./two_cube_b4_codd_o2_connected_kernel_certificate.json) | `7f65a8efb1e7cbf0128371afeeb6e89fae70c319c3052c08ce252a1fbe74d566` | Census, 1,236/472 histories, source folds, phase and finite-\(u\) gates |
| B4 history ledger | [B4 JSONL ledger](./two_cube_b4_codd_o2_history_ledger.jsonl) | `5073b97376875ad7d595e79e059d33a1ec709283e4ca77b57ced04dc2e805a37` | Ordered path-level provenance and Möbius weights |
| B4 strict loader | [B4 loader](./two_cube_b4_codd_o2_kernel_loader.py) | `255a1a609cb35d97352aed5481aaecd754f7c962d1f1cd1de82fdf8f08788dfc` | Fail-closed schema, hash, NPZ, rational, CSR, and release validation |
| B4 quick verifier | [B4 verifier](./verify_two_cube_b4_codd_o2_connected_kernel.py) | `a21dc41217a5cfaac8942deb159ec66c90833a7e62e9921255d79945bbaf07be` | Artifact-only scientific gates |
| B4 replay | [B4 replay verifier](./rebuild_verify_two_cube_b4_codd_o2_connected_kernel.py) | `df50354e8ef28b9443a5a2a5f5ac71185319460cc82c45d6b512adf54314bd23` | Same-builder deterministic array and ledger reproduction |
| B4 tests | [Focused](./test_two_cube_b4_codd_o2_connected_kernel.py), [hostile release](./test_two_cube_b4_codd_o2_release_safety.py) | `6c1128e8e77fd9201d924a3ea79cbbbd840d0f3b90d2e1f5eedbaf5eee3aac84`, `f4c1326543aeb9225202c3a44406a93c40957eec373977a1e7b27464bb7d267d` | Scientific identities, corruption rejection, aliases, rollback, ACL portability; 47/47 current acceptance |
| B4 detailed derivation | [B4 note](./TWO_CUBE_B4_CODD_O2_CONNECTED_KERNEL_2026-08-29.md) | `dff8fb5db1d6cd46d65dbcd8e90cfe2406abe8f5b8bb7bff4dbee84ad5368646` | Full implementation details and B4 claim boundary |
| B6 detached root | [B6 manifest](./two_cube_b6_codd_o2_connected_kernel_manifest.json) | `021558ce5bea60e43f757d76c1b8122f15f355c1e5174304f440cce5d98d422b` | Exact ordered 43-role regenerative release, authority classes, replay/post-hoc separation |
| B6 operator | [B6 NPZ](./two_cube_b6_codd_o2_connected_kernel.npz) | `3fd15a3ab5060b7e477662d63e3fdcf65cb2b9eb52c2b1a11a0f6065249f5cb4` | Raw/connected operators, six channels, \(5/612\), and spectrum of the serialized rational \(11\times11\) connected kernel |
| B6 certificate | [B6 certificate](./two_cube_b6_codd_o2_connected_kernel_certificate.json) | `bb6a51ef64de61f91ff7c7f023a4ab04149308bbef69dc7b0b295d0805c31440` | 1,590,462-state census, completeness, folds, controls, symmetries, held-out validation |
| B6 history ledger | [B6 JSONL ledger](./two_cube_b6_codd_o2_history_ledger.jsonl) | `b638c2d0c5e14348c678ce20c60ba1c465b94ce0d8133c150d4b8519c17e5c02` | 1,984 ordered histories and 792 surviving connected paths |
| B6 strict loader | [B6 loader](./two_cube_b6_codd_o2_kernel_loader.py) | `e3ba7d9d656ba527ff58df57f0dde50b2fa1f301d9b6197a0de4dd34f13ea16d` | Exact role order, import/data closure, nested B4 seal, strict artifact validation |
| B6 quick verifier | [B6 verifier](./verify_two_cube_b6_codd_o2_connected_kernel.py) | `6a557c6716c05bbf3d5ee3c7ac162363da7176dfd99701d04f1ee4f58370c12a` | Artifact-only gates without builder, adapter, or expected coefficient |
| B6 replay | [B6 replay verifier](./rebuild_verify_two_cube_b6_codd_o2_connected_kernel.py) | `25a9be4f062e01e8c58ed7fb248f67c81ef7b5b23cef8f9913b63699f90c907f` | Same-builder byte replay; final acceptance reports no byte mismatches |
| B6 tests | [Focused](./test_two_cube_b6_codd_o2_connected_kernel.py), [hostile release](./test_two_cube_b6_codd_o2_release_safety.py), [isolated extraction](./test_two_cube_b6_codd_o2_isolated_extraction.py) | `db70318025a5dc5d49972861fbc04cf875cfbaa4837b30f359949f861c8c5021`, `a4dafa7d307a7befebf0e98dd3cf31d96b18b62d9809bbdb3c1e518615b036f9`, `4a4885f4b001a63efb5b20e8c4cefa9934c17cab91245e8bce46cddf219989aa` | 29/29 focused/hostile acceptance plus 2/2 full isolated extraction, replay, and dependency mutation sweep |
| Portable CGC bootstrap | [Bootstrap](./two_cube_b6_pyclebsch_adapter.py), [pinned archive](./pyclebsch-feature-obc.zip) | `1a6ee7d48ec99a82696d373ec08880f678a0772b17ad94e0ca6627ce5f6083ed`, `6d16ee0fa055b143d8373efa8d57e4f5a745b362bcab6eb12318a9c09922111b` | Eleven-member hash-pinned CGC source materialization without private paths |
| B6 post-hoc comparator | [Comparator](./two_cube_b6_codd_o2_posthoc_comparison.py) | `e7c50f9b2bc94517bef1b50de197ee60cd5a31bf5e19ba7268a4d5d22cd59027` | Comparator source existed earlier; recorded comparison ran only after initial artifact and ledger hash production |
| B6 detailed derivation | [B6 note](./TWO_CUBE_B6_CODD_O2_CONNECTED_KERNEL_2026-08-29.md) | `0a523c1dc57323e3ac348b1a9264f56a0594680ae5b4ba561ac51086518c5367` | Full B6 derivation, validation details, and claim firewall |

The B6 manifest includes the B4 manifest with the exact nested hash shown above. The final B6 artifact and ledger hashes are unchanged from the blind scientific freeze. The final certificate hash differs from the earlier pre-publication certificate hash because release-closure metadata was resealed; no scientific array or history byte changed.

---

## 15. Reproducibility from the 43-role B6 authority root

The B6 release is designed to be copied into a flat clean directory containing exactly the 43 manifest-listed roles plus the detached manifest.

From the release directory:

```powershell
python -c "import json,pathlib,shutil; s=pathlib.Path('.'); m=json.loads((s/'two_cube_b6_codd_o2_connected_kernel_manifest.json').read_text('ascii')); d=pathlib.Path('b6_release_extract'); d.mkdir(exist_ok=False); [shutil.copyfile(s/r['name'],d/r['name']) for r in m['files']]; shutil.copyfile(s/'two_cube_b6_codd_o2_connected_kernel_manifest.json',d/'two_cube_b6_codd_o2_connected_kernel_manifest.json')"
Set-Location b6_release_extract
```

Run strict loading and the target-blind scientific checks first:

```powershell
python -I -c "import sys; sys.path.insert(0,'.'); import two_cube_b6_codd_o2_kernel_loader as L; R=L.load_release(); print(R.kernel.sha256)"
python -I -c "import runpy,sys; sys.path.insert(0,'.'); runpy.run_path('verify_two_cube_b6_codd_o2_connected_kernel.py',run_name='__main__')"
python -I -c "import runpy,sys; sys.path.insert(0,'.'); runpy.run_path('rebuild_verify_two_cube_b6_codd_o2_connected_kernel.py',run_name='__main__')"
```

Only after those checks succeed should the separate post-hoc comparator be run:

```powershell
python -I -c "import runpy,sys; sys.path.insert(0,'.'); runpy.run_path('two_cube_b6_codd_o2_posthoc_comparison.py',run_name='__main__')"
```

The full isolated dependency and corruption sweep is:

```powershell
python test_two_cube_b6_codd_o2_isolated_extraction.py --full
```

Tested runtime: CPython 3.12, NumPy 2.3.5, and SciPy 1.17.1. `PYTHONPATH`, an installed local `pyclebsch`, and a private `.scratch` tree are not required. The manifest-bound bootstrap checks the sealed adapter, the archive, and all eleven required Python members before materializing them in an operating-system temporary directory.

The reproducibility sequence preserves the evidentiary firewall:

\[
\text{strict manifest load}
\rightarrow
\text{artifact-only verification}
\rightarrow
\text{target-blind byte replay}
\rightarrow
\text{post-hoc comparison}.
\]

Reversing this order does not change the sealed bytes, but it weakens the human chronology argument and should be avoided.

---

## 16. Open problems and final claim boundary

The following are closed:

- the complete charge-odd \(E_*=8/3\) shell in B4 and B6;
- full zero-denominator removal for the stated truncations;
- \(PVP=I_{11}\) and connected first-order cancellation;
- literal two-cube operator-level Möbius subtraction through \(O(u^2)\);
- B4 adjacent hopping \(-1/12\);
- the B6 adjacent off-diagonal coefficient \(+5/612\), with all six shared-link channels exhausted at this order;
- the six-channel mechanism and the B4-to-B6 sign reversal;
- deterministic regenerative release from the 43-role B6 manifest.

The following remain open:

- radius-three and larger temporal word spaces;
- larger connected volumes and finite-volume scaling;
- cutoff stability beyond B6, especially the diagonal remainder;
- a full finite-coupling two-cube spectrum;
- higher perturbative orders on the two-cube cluster;
- a global rooted scalar, momentum-space dispersion, or transport law from this open two-cube operator;
- independent reproduction by an external group or a genuinely separate implementation;
- infinite-volume and continuum limits;
- any implication for the Yang–Mills mass gap.

The final defensible statement is therefore:

> On the finite open face-sharing two-cube SU(3) prism, the complete charge-odd one-plaquette shell and its connected adjacent-hopping Bloch/Feshbach coefficient are closed through \(O(u^2)\) under the pinned numerical-to-rational protocol. Literal operator-level Möbius subtraction gives \(-1/12\) at B4 and the exact-Casimir-B6 channel-closed value \(+5/612\); the restored sextet and adjoint channels cause the sign reversal. This is a strong finite-regulator result and a demonstrated computational capability within this program, not an untruncated, finite-coupling, thermodynamic, transport, continuum, or mass-gap result, and not a universal novelty or priority claim.
