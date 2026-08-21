# Expansion Audit for *Topological Protection of a Dispersionless \(T_1^{+-}\) Glueball Band*

**Date:** July 25, 2026  
**Scope reviewed:** `flatband paper.pdf` plus all 16 supplied project-source documents  
**Purpose:** identify defensible ways to enlarge the paper without importing results from a different Hamiltonian, coupling limit, or evidentiary layer

## Executive verdict

The paper should be expanded, but not by merging the supplied SU(3)/SU(\(N\)) local-gap and projected-capacity documents.

The present manuscript already contains the right publishable core:

1. the signed face-to-edge incidence factorization;
2. exact flatness of the lowest \(C\)-odd branch through \(O(y^3)\);
3. identification of the flat eigenspace with \(Z_2=\ker\partial_2\);
4. the Betti-number count
   \[
   \dim Z_2=N_3+b_2-b_3;
   \]
5. incompleteness of the compact cube states;
6. the boundary-operator protection mechanism;
7. exact SU(3) strong-coupling coefficients through \(O(y^3)\); and
8. a falsifiable fourth-order decision criterion.

None of the auxiliary documents supplies another theorem that can simply be inserted into this chain. Most concern the compact one-plaquette **large-\(\beta\) weak-well problem**, whereas the flat-band paper concerns the full spatial Kogut-Susskind Hamiltonian in the **small-\(y\) strong-coupling one-excitation sector**. Combining them would blur two different operators and two opposite asymptotic regimes.

The strongest expansion is instead latent inside the paper's own incidence matrix. It yields, almost for free:

- the exact spectrum of all three \(C\)-odd Bloch branches;
- an exact flat-band projector;
- an \(r^{-3}\) real-space projector tail;
- a candidate unit \(\pi_2\) hedgehog charge at the \(\Gamma\) touching;
- a strictly stronger disorder-tolerant channel-protection theorem;
- exact spectral flow under twisted boundary conditions; and
- a sharper symmetry-resolved \(O(y^4)\) test.

With these additions, the paper becomes a 13-16 page mathematical-physics paper rather than a nine-page result note. The best headline remains the gauge-theory realization of a homological singular flat band, not a continuum glueball prediction.

## 1. Source-by-source compatibility audit

| # | Supplied source | Use in this paper | Judgment |
|---:|---|---|---|
| 1 | *Non-Uniformity in \(N\) and Formal 't Hooft Rescaling* | None in the main text | This analyzes fixed-rank large-\(\beta\) local class gaps and their non-uniformity in \(N\). It is a different asymptotic problem. |
| 2 | *SU(3) Weyl Geometry and Local Hamiltonian* | None in the main text | The Weyl-Gaussian weak-well Hamiltonian is not the strong-coupling one-flux effective Hamiltonian. |
| 3 | *Wilson Hard-Defect Peierls Bound* | Do not merge | Conditional four-dimensional Wilson-measure geometry; no logical input to the finite-order one-excitation theorem. |
| 4 | *From Local Class Gaps to Global Wilson Geometry* | Scope language only | Its warning that a local gap is not a physical glueball mass supports the paper's existing scope disclaimer, but supplies no flat-band theorem. |
| 5 | *Rooted Projected-Capacity Source Stability* | Do not merge | Conditional global source-stability program; separate paper and separate regime. |
| 6 | *Compact Character-Basis Numerical Audit* | Do not merge | Numerical audit of the compact large-\(\beta\) one-plaquette gap. |
| 7 | *Finite Leakage Matrix and Radial Tail Obstruction* | Do not merge | A useful negative result for the weak-well paper, unrelated to homological caging. |
| 8 | *Theorem Ledger and Open Analytic Targets* | Status discipline only | Its separation of theorem/certificate/audit/conditional claim is useful and is already reflected in the flat-band draft. |
| 9 | *SU(3) Three-Term Local Gap* | Separate companion paper | Strong local theorem, but for the wrong operator and limit. |
| 10 | *SU(3) Weyl Geometry and Local Hamiltonian (1)* | Delete as duplicate | Its extracted text is identical to source 2. |
| 11 | *Logical Status and Theorem Map (1)* | Status discipline only | Reinforces the need not to collapse local, finite, and global claims. |
| 12 | *Numerical Projected-Capacity Audits* | Do not merge | The word “incidence” occurs in a different probabilistic construction; it is not evidence for the flat band. |
| 13 | *Finite Wick Certificate for the SU(\(N\)) \(C\)-odd Local Gap* | Do not merge; nomenclature warning | “\(C\)-odd local gap” here is a weak-well class excitation, not the \(T_1^{+-}\) propagating one-flux band. This is the most dangerous source to merge because the labels look similar while the objects are different. |
| 14 | *SU(3) Coefficient Tables and Matrix Elements* | Separate companion appendix | Reproducibility material for source 9, not for the flat-band coefficients. |
| 15 | *Fixed-Rank SU(\(N\)) Local Class Gaps* | Separate companion paper | Does not establish an SU(\(N\)) extension of the strong-coupling incidence band. |
| 16 | *Sun report* | Reuse only selected bibliography | The quantum-simulation references are relevant to the introduction. Its Calogero-Sutherland, Weyl-gap, and projected-capacity discussion belongs to the local-gap paper. |

**Net result:** no auxiliary theorem should be copied into the flat-band manuscript. Sources 8, 11, and 16 offer framing or bibliography; the rest belong in separate papers.

## 2. Corrections required before adding new claims

### 2.1 Replace the Gauss-law statement

Section 5 currently interprets
\[
\partial_2 c=0
\]
as “the Gauss-law-satisfying subspace.” That is not correct.

Kogut-Susskind Gauss law is a vertex constraint. Every single-plaquette Wilson-loop state is already gauge invariant: its link flux forms a closed loop and satisfies the vertex constraint because
\[
\partial_1\partial_2=0.
\]
The additional condition \(\partial_2c=0\) says that the **superposed face 2-chain has no oriented edge boundary**. It is a closed-surface or higher-form closure condition, not ordinary Gauss law.

Recommended replacement:

> The flat eigenspace is the space of boundary-free 2-chains. This condition is stronger than the ordinary vertex Gauss constraint, which is already satisfied throughout the one-plaquette gauge-invariant manifold.

This correction improves the physics. It identifies the mechanism as destructive interference organized by a chain complex, without claiming that all non-flat one-plaquette states are unphysical.

### 2.2 Add the omitted remainder

The displayed mass formula must read
\[
m_-(k)=\frac83+y+\frac{11}{306}y^2
-\frac{109151}{249696}y^3+O(y^4),
\]
not as an exact polynomial. The same applies in the abstract and to all top/bandwidth formulas truncated at third order.

### 2.3 Narrow “all-orders” to the proved protection class

Theorem 6.3 is mathematically correct for the stated boundary-operator algebra. It does **not** prove that the physical SU(3) effective Hamiltonian remains inside that algebra at every order. The abstract should say:

> to all orders within the boundary-operator channel algebra

rather than implying an unconditional all-orders theorem for the complete strong-coupling expansion.

Likewise, “pinned at the unperturbed energy” should mean “pinned relative to the common scalar self-energy.” Any scalar term shifts every state, including \(H_2\).

### 2.4 Complete the proof that the \(C\)-even sector has no flat band

\(\det N(k)\not\equiv0\) proves only that there is no \(C\)-even band identically at the lower bound \(-4\). It does not by itself exclude a flat band at another eigenvalue.

A complete two-point proof is immediate:

\[
\operatorname{spec}A(0)=\{12,0,0\},\qquad
\operatorname{spec}A(\pi,\pi,\pi)=\{-4,-4,-4\}.
\]

The spectra have empty intersection, so no eigenvalue can be constant across the Brillouin zone.

### 2.5 Compare explicitly with Hamer's 1989 \(1^{+-}\) series

The bibliography cites Hamer-Irving-Preece (1986), but omits C. J. Hamer, *Hamiltonian strong coupling expansions for glueball masses in SU(3)*, Phys. Lett. B 224, 339-342 (1989), DOI [10.1016/0370-2693(89)91242-2](https://doi.org/10.1016/0370-2693(89)91242-2). The 1989 paper explicitly computes strong-coupling series for the \(0^{++}\), \(1^{+-}\), and \(2^{++}\) masses.

Before claiming novelty for the numerical mass coefficients, obtain that four-page paper and compare:

| Comparison item | Required check |
|---|---|
| Hamiltonian normalization | electric Casimir and magnetic-term conventions |
| expansion parameter | conversion between Hamer's variable and \(y\) |
| energy definition | one-particle energy versus vacuum-subtracted mass |
| \(1^{+-}\) coefficients | equality or disagreement through the shared order |
| momentum resolution | whether Hamer computed only \(k=0\) masses or a full band |

Even if every coefficient is already present in Hamer, the incidence factorization, exact flatness at all \(k\), Betti count, singular-band structure, and channel-protection theorem remain distinct. The paper should make that distinction explicit.

### 2.6 Supply the certificates, not merely their names

Appendix A names:

- `flatband_one_page_audit.py`;
- `flatband_homology_certificate.py`; and
- a companion one-plaquette exact-arithmetic program.

None is included among the supplied project files. A submission claiming certified constants needs:

1. a public repository or archival DOI;
2. immutable commit and file hashes;
3. exact commands and expected terminal summaries;
4. environment/dependency versions; and
5. machine-readable outputs for every table.

This is more important than adding another numerical figure.

## 3. Strongest new theorem: the complete \(C\)-odd spectrum

The incidence matrix already determines all three branches.

Define
\[
u_j=1-e^{ik_j},\qquad
q(k)=\sum_{j=1}^3|u_j|^2
=4\sum_{j=1}^3\sin^2\frac{k_j}{2},
\]
and write the paper's null vector as
\[
w=
\begin{pmatrix}
\overline{u_3}\\
-\overline{u_2}\\
\overline{u_1}
\end{pmatrix},
\qquad
\|w\|^2=q.
\]

A direct multiplication gives the stronger identity
\[
\widetilde N\widetilde N^\dagger
=qI-ww^\dagger.
\]
For \(q\ne0\), define
\[
P_{\mathrm{flat}}(k)=\frac{ww^\dagger}{q}.
\]
Then
\[
S(k)+4I=q(k)\bigl(I-P_{\mathrm{flat}}(k)\bigr),
\]
and therefore
\[
\boxed{
\operatorname{spec}S(k)
=\left\{-4,\,-4+q(k),\,-4+q(k)\right\}.
}
\]

This is stronger than Theorem 4.1:

- the two dispersive branches are exactly degenerate for every \(k\);
- their common dispersion is the standard cubic-lattice Laplacian symbol;
- the threefold \(\Gamma\) touching is explicit;
- the upper endpoint \(8\) follows from \(q_{\max}=12\); and
- the flat projector is available in closed form.

The characteristic polynomial is
\[
\det(\lambda I-S)
=(\lambda+4)\bigl(\lambda+4-q(k)\bigr)^2.
\]

### 3.1 Full SU(3) mass dispersion through \(O(y^3)\)

The paper states that the third-order effective Hamiltonian retains the same signed-adjacency structure. Its flat and top coefficients therefore determine the whole band:

\[
m_{\mathrm{flat}}
=\frac83+y+\frac{11}{306}y^2
-\frac{109151}{249696}y^3+O(y^4),
\]

\[
\boxed{
m_{\mathrm{disp},1}(k)
=m_{\mathrm{disp},2}(k)
=m_{\mathrm{flat}}
+q(k)\left(
\frac5{612}y^2
+\frac{1975}{124848}y^3
\right)
+O(y^4).
}
\]

At \(q=12\), this reproduces the stated band top:
\[
\frac{41}{306}y^2-\frac{61751}{249696}y^3.
\]

This should replace the present plot-only discussion. It makes the entire \(C\)-odd one-excitation spectrum an exact analytic result through the certified order.

### 3.2 Exact finite-size spectral scale

On the periodic \(L^3\) lattice,
\[
q_n=4\sum_{j=1}^3\sin^2\frac{\pi n_j}{L}.
\]
The smallest positive value is
\[
q_{\min}=4\sin^2\frac{\pi}{L}
=\frac{4\pi^2}{L^2}+O(L^{-4}).
\]

After excluding the \(\Gamma\) zero modes, the first spectral separation above the flat level is
\[
\Delta_L
=4\sin^2\frac{\pi}{L}
\left(
\frac5{612}y^2+\frac{1975}{124848}y^3
\right)
+O(y^4).
\]

This gives a second direct finite-volume benchmark in addition to the degeneracy count.

## 4. The singular projector and its real-space consequence

Near \(\Gamma\),
\[
u_j=-ik_j+O(k_j^2),
\qquad
w=iRk+O(k^2),
\]
where
\[
R(k_1,k_2,k_3)=(k_3,-k_2,k_1)
\]
is an orthogonal map. Hence
\[
P_{\mathrm{flat}}(k)
\longrightarrow
\frac{(Rk)(Rk)^{T}}{|k|^2},
\]
which depends on the direction of approach to \(\Gamma\). This proves the nonextendability of the projector, not merely of one chosen eigenvector.

Fourier transformation gives a dipolar algebraic tail:
\[
P_{\mathrm{flat},ij}(r)
\sim
\frac{
R_{ia}R_{jb}
\left(\delta_{ab}-3\widehat r_a\widehat r_b\right)
}{4\pi r^3},
\qquad r\to\infty,
\]
up to lattice-contact terms and convention-dependent overall signs.

Thus:

\[
\boxed{\text{the flat-band projector decays as }r^{-3}.}
\]

This is the real-space signature of the singular band and explains why compact cube states exist but cannot furnish a complete localized basis. It also places the result directly beside recent work showing generic \(r^{-d}\) decay for singular flat-band projectors: Y. Kim, S. Flach, and A. Andreanov, [*Real-space decay of flat-band projectors from compact localized states*](https://arxiv.org/abs/2510.17258) (2025/2026).

The corresponding finite-volume projector has the Hodge form
\[
P_{B_2}
=D_3(D_3^TD_3)^+D_3^T,
\]
with \((\cdot)^+\) the Moore-Penrose inverse. On the torus, \(D_3^TD_3\) is the scalar Laplacian on cube chains. Its Green function is the source of the algebraic nonlocality.

## 5. Stronger protection theorem: arbitrary channel weights

The polynomial formulation in Theorem 6.3 is unnecessarily restrictive.

Let
\[
A:C_1\to C_1,\qquad B:C_3\to C_3
\]
be arbitrary self-adjoint operators. They may be spatially varying, disordered, or nonlocal. Define
\[
X=D_2^TAD_2+D_3BD_3^T.
\]

Then:

1. \(D_2^TAD_2\) annihilates all of \(Z_2=\ker D_2\);
2. \(D_3BD_3^T\) annihilates \(H_2=\ker D_2\cap\ker D_3^T\); and
3. therefore \(X\) annihilates \(H_2\).

If \(B\) is positive definite on the relevant cube quotient, then \(D_3BD_3^T\) is positive definite on \(B_2=\operatorname{im}D_3\), so its kernel inside \(Z_2\) is exactly \(H_2\).

This yields:

> **Channel-ideal protection theorem.** The full flat space is immune to arbitrary link-channel corrections \(D_2^TAD_2\), while the harmonic sector \(H_2\) is immune to arbitrary sums of link- and cube-channel corrections \(D_2^TAD_2+D_3BD_3^T\).

This theorem:

- needs no translation invariance;
- needs no constant coefficients;
- includes bond disorder and inhomogeneous simulation errors;
- is stronger than polynomial functional calculus; and
- gives a clean maximal class of perturbations that the paper actually proves harmless.

The factorization should also be positioned against the signed-line-graph and lattice-supersymmetry literature. Useful primary references are T. Zaslavsky, [*Matrices in the Theory of Signed Simple Graphs*](https://arxiv.org/abs/1303.3083), and K. Roychowdhury et al., [*Supersymmetry on the Lattice: Geometry, Topology, and Flat Bands*](https://arxiv.org/abs/2207.09475). The novelty is not the abstract fact that \(R^\dagger R\) can host zero modes; it is that the SU(3) strong-coupling recoupling signs produce the cellular boundary operator and hence a homological singular glueball band.

## 6. Twisted-boundary spectral flow

The topology/boundary discussion can be strengthened without new group theory.

Impose Bloch twists
\[
k_j=\frac{2\pi n_j+\phi_j}{L}.
\]
For trivial twist \(\phi=0\), the allowed momenta contain \(\Gamma\), where the kernel has dimension three. The total flat-level multiplicity is \(L^3+2\).

If any \(\phi_j\not\equiv0\pmod{2\pi}\), no allowed momentum equals \(\Gamma\). Every momentum then has a one-dimensional flat kernel, so
\[
\boxed{\dim E_{-4}=L^3.}
\]

The two states removed from the flat level rise quadratically:
\[
\delta E(\phi)
\propto
4\sum_j\sin^2\frac{\phi_j}{2L}.
\]

This is an exact spectral-flow signature of the singular \(\Gamma\) touching. It is more discriminating than comparing periodic and open boundaries because the Hamiltonian can be varied continuously from one case to the other.

This should be presented first as a twist of the one-excitation translation problem. It should **not** be identified with an SU(3) 't Hooft twist until the full gauge-theory boundary conditions and center cocycle are derived.

## 7. Sharpen the fourth-order criterion

Let \(P_H\) project onto the three wrapping cycles \(H_2(T^3)\).

Three distinct tests should be separated:

| Test | Meaning |
|---|---|
| \(XP_H=0\) | exact invariant pinning to all orders in the added operator |
| \(P_HXP_H=0\) | no first-order shift, but higher-order mixing may still move the level |
| \(P_HXP_H=cI_3\) | cubic symmetry preserves the triplet but permits a common shift |

At \(\Gamma\), the three harmonic states transform as the irreducible \(T_1^{+-}\) representation. Therefore any correction preserving the full cubic group acts as a scalar on this three-dimensional space by Schur's lemma.

Criterion 9.1 should consequently be refined:

1. **link factorization:** the whole band remains flat;
2. **harmonic annihilation:** the band disperses but the \(H_2\) triplet remains pinned relative to scalar self-energy;
3. **nonzero harmonic scalar:** the band disperses and the triplet shifts as a whole;
4. **cubic-symmetry breaking:** only then can the \(T_1\) triplet split.

Thus the present phrase “no exact remnant survives” is too strong. Even when homological pinning fails, cubic symmetry still enforces a threefold \(T_1\) level within the one-excitation \(\Gamma\) sector.

The actual fourth-order deliverable should print:

\[
\|XP_H\|,\qquad
\|P_HXP_H\|,\qquad
\left\|P_HXP_H-\frac{\operatorname{tr}(P_HXP_H)}3I_3\right\|,
\]

with exact arithmetic where possible.

## 8. Candidate momentum-space topological charge

The small-\(k\) normalized cube generator satisfies
\[
\widehat w(k)\longrightarrow iR\widehat k.
\]
After removing the common phase, this is a hedgehog map from a small momentum sphere around \(\Gamma\) to the real normalized kernel vector. Since \(\det R=+1\), the linearized texture has degree \(+1\).

This strongly suggests that the \(\Gamma\) singularity carries a unit \(\pi_2\) charge in the appropriate real/chiral classifying space. Three-dimensional supersymmetric flat-band nexus points with precisely such hedgehog textures are discussed by Roychowdhury et al.

This is potentially the paper's strongest conceptual addition, but it should be labeled **Open until the symmetry-class convention is checked**. The required proof is short:

1. construct the Hermitian square-root Hamiltonian
   \[
   Q(k)=
   \begin{pmatrix}
   0&\widetilde N(k)\\
   \widetilde N^\dagger(k)&0
   \end{pmatrix};
   \]
2. identify its chiral, time-reversal, and particle-hole symmetries;
3. flatten \(Q\) on a small \(S^2\) around \(\Gamma\);
4. compute the homotopy invariant; and
5. show whether the charge is stable under the physical symmetry-preserving perturbation class.

Do not substitute a Chern number: the singular flat line is not an isolated complex band, and its ordinary Chern number is not the relevant invariant.

## 9. Highest-value new computations

### Priority 1: resolve the SU(3) \(O(y^4)\) signed corner operator

This is the decisive extension. It converts the paper's pre-registered criterion into a result.

Minimum output:

- exact fourth-order effective matrix elements;
- separation of scalar, shared-link, cube, and genuine corner channels;
- exact action on the three wrapping sheets;
- flat-band bandwidth at \(O(y^4)\);
- common \(T_1^{+-}\) shift at \(\Gamma\);
- certificate hashes and reproducible script.

### Priority 2: smallest multi-plaquette survival test

The current topology theorem is one-excitation only. The first honest test is not a continuum extrapolation; it is exact diagonalization of the smallest periodic and open systems after including the two-plaquette manifold.

Measure:

- whether the \(H_2\)-derived triplet remains an invariant subspace;
- which two-particle channels mix with it;
- whether the mixing is forbidden by charge conjugation, cubic symmetry, or center charge; and
- how the periodic/open/twisted spectral flow changes.

### Priority 3: strong-coupling SU(\(N\)) generalization

The supplied fixed-rank SU(\(N\)) local-gap documents do not do this. A valid extension requires deriving the **shared-link strong-coupling recoupling amplitudes** for general \(N\) and proving that the \(C\)-odd effective matrix is still
\[
\alpha_N I+\beta_N S
\]
through the claimed order.

Only after that derivation may the topology theorem be promoted from SU(3) to SU(\(N\)). If an earlier \(N\ge7\) certificate exists elsewhere in the project archive, it should be supplied rather than reconstructed.

### Priority 4: one non-product topology

The current table uses only products of circles and intervals. Add a cubulation with a different global topology, or formulate the theorem for relative homology under a clearly specified boundary convention.

For a connected closed orientable three-manifold, Poincare duality gives
\[
b_2=b_1,\qquad b_3=1,
\]
so
\[
\dim Z_2=N_3+b_1-1.
\]
One non-product example would demonstrate that the theorem is genuinely topological rather than a periodic/open counting identity.

## 10. Recommended revised paper structure

1. **Introduction and exact scope**
   - historical strong-coupling series, including Hamer 1989;
   - modern Hamiltonian-simulation motivation;
   - precise novelty statement.
2. **One-excitation SU(3) Hamiltonian**
   - distinguish vertex Gauss law from 2-chain closure.
3. **Signed cellular line graph and incidence factorization**
   - connect to signed graphs and square-root/SUSY constructions.
4. **Complete \(C\)-odd Bloch spectrum**
   - exact doublet dispersion, projector, finite-size scale.
5. **Homology, compact cube states, and boundary/twist counts**
   - periodic, mixed, open, and twisted cases.
6. **Hodge decomposition and channel-ideal protection**
   - arbitrary \(A\) and \(B\), including inhomogeneity.
7. **Singular projector and \(\Gamma\) nexus**
   - \(r^{-3}\) tail;
   - \(\pi_2\) charge if fully proved.
8. **SU(3) coefficients through \(O(y^3)\)**
   - full analytic dispersion, not only band endpoints.
9. **Symmetry-resolved fourth-order test**
   - \(XP_H\), scalar triplet shift, symmetry-breaking diagnostics.
10. **Finite-volume simulation protocol**
    - periodic/open/twisted degeneracies and controlled channel perturbations.
11. **Scope and open problems**
    - multi-plaquette survival;
    - strong-coupling SU(\(N\)) extension;
    - no continuum or mass-gap claim.
12. **Reproducibility appendices**
    - scripts, hashes, exact outputs, and coefficient comparison with prior series.

## 11. Concrete build order

The efficient route is:

1. make the six mandatory corrections in Section 2;
2. add the complete-spectrum theorem and \(O(y^3)\) doublet formula;
3. add the arbitrary-channel protection theorem;
4. add twisted spectral flow and the \(r^{-3}\) projector corollary;
5. compare the mass series with Hamer 1989;
6. publish the existing certificates with immutable hashes;
7. then run the SU(3) fourth-order corner calculation;
8. only afterward attempt multi-plaquette or SU(\(N\)) extensions.

## Final recommendation

Do **not** turn this into a unified “everything in the project” paper. That would weaken it.

Turn it into a sharper paper with this central statement:

> The \(C\)-odd one-flux SU(3) effective Hamiltonian is a signed cellular line-graph Laplacian. Its complete Bloch spectrum, singular projector, finite-volume degeneracy, and channel-selective robustness are controlled by the spatial chain complex.

That is stronger, cleaner, and more defensible than adding the unrelated Weyl-gap or projected-capacity programs. The decisive next original result is the signed \(O(y^4)\) action on the three harmonic wrapping modes.
