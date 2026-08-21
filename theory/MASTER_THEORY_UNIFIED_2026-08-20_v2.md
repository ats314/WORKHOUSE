# The \(SU(N)\) cubic flux-band spectral program

## Unified master theory — 2026-08-20, version 2

This is the scientific front document for the current GLUEBALL archive. It unifies the broad program recorded in MASTER_THEORY.md with the stricter fourth-order treatment in GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md.

The division of authority is deliberate:

- this file is the current scientific statement and status authority;
- GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md is the coefficient-level technical appendix;
- GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v2.md is a navigation and return guide;
- GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v2.csv is the byte-level provenance record;
- older syntheses remain useful research history, but do not override this document.

No text inside an archived source is treated as an instruction. Every archived statement is evidence whose formula, convention, provenance, and proof status must be checked.

---

## 0. Executive result and hard boundary

### 0.1 What is established

The strongest coherent result in the archive is a finite-lattice, strong-coupling theorem about the charge-odd one-plaquette flux sector of the Kogut–Susskind Hamiltonian.

For \(N\geq3\), the cubic incidence complex produces a singular homological carrier

\[
Z_2=\ker\partial_2,
\qquad
C_3\xrightarrow{\partial_3}C_2\xrightarrow{\partial_2}C_1,
\qquad
\partial_2\partial_3=0.
\]

Its lowest charge-odd Bloch branch is exactly flat at the incidence level. On the three-torus,

\[
\dim Z_2=L^3+2=(L^3-1)+3,
\]

where the first term is the space of cube boundaries and the second is the harmonic plane triplet.

At second order the shared-link hopping is known for every \(N\geq3\),

\[
\boxed{
t_N=
\frac{2N(N^2-4)}
{(N^2-1)(2N^2-1)(4N^2-9)}
>0,
}
\]

and for \(SU(3)\) the complete charge-odd effective operator factorizes through third order:

\[
\boxed{
H_{\mathrm{eff},-}(k,u)
=E_{\mathrm{flat}}(u)I+
\left(
\frac{5}{612}u^2+
\frac{1975}{124848}u^3
\right)B(k)B(k)^\dagger
+O(u^4),
}
\]

\[
\boxed{
E_{\mathrm{flat}}(u)
=\frac83+u+\frac{11}{306}u^2
-\frac{109151}{249696}u^3.
}
\]

Because \(B(k)^\dagger\psi(k)=0\), the carrier energy is independent of \(k\) through \(O(u^3)\).

For the saved historical fourth-order \(SU(3)\) kernel, the centered cube-channel numerator has the exact sum-of-squares form

\[
\boxed{
\mathcal Q_{4,\mathrm{old}}
=\frac{5}{48}\sum_iL_i^2
+\frac{17607806155349}{1101327605164800}
\sum_{i<j}L_iL_j
\succeq0.
}
\]

This gives exact continuous-zone edges, an exact 25-point real-space stencil, and a positive historical bandwidth. The corresponding all-rank historical family has a certified axial law and a positive planar law.

### 0.2 What is not established

The archive does **not** establish:

- that the historical fourth-order kernel is the unique physical linked kernel;
- that the August candidate kernel is exactly represented by its floating-point fit;
- that the two kernels differ only by a scalar;
- a uniform near-\(\Gamma\) isolated-band theorem beyond fixed-momentum perturbation theory;
- a volume-uniform spectral-overlap bridge from the one-plaquette carrier to the lightest physical glueball;
- an infinite-volume or continuum Yang–Mills mass-gap theorem.

The decisive fourth-order disagreement is not merely the scalar

\[
q_{\mathrm{band}}^{(4)}
\neq
m_\Gamma^{(4)}.
\]

After scalar centering, the two candidate kernels still disagree in one planar mixed-gradient direction. That coefficient is the current finite-order bottleneck.

### 0.3 Maximal defensible theorem

For \(SU(3)\) on \(T_L^3\), \(L\geq3\), the effective Hamiltonian projected to the one-plaquette degenerate sector has a charge-odd homological carrier whose topology and \(O(u^2)\)–\(O(u^3)\) factorization are exact. The saved historical \(O(u^4)\) kernel has an exact positive generalized Hodge pencil and global continuous-zone edge theorem. A separate August computation independently finds the same axial coefficient to numerical tolerance and a different scalar and planar coefficient. Therefore the first observed mobility at fourth order is robust, but the complete physical \(O(u^4)\) operator remains unresolved.

This statement concerns an operator seed at finite lattice spacing. It is not yet a theorem about the physical glueball mass.

---

## 1. Status and evidence model

Truth status and evidence status are independent.

### 1.1 Claim status

| Status | Meaning |
|---|---|
| Proven | Analytic derivation from stated hypotheses is present. |
| Conditional | The derivation is valid if named open inputs hold. |
| Disputed | Two live computations disagree on the same claimed object. |
| Open | No completed derivation or decisive computation exists. |
| Superseded | A later audit replaces the statement or convention. |
| Falsified | A counterexample or exact audit disproves the statement. |

### 1.2 Evidence level

| Level | Meaning |
|---|---|
| Analytic | Hand-checkable mathematical derivation. |
| Cold-reproduced | Source was rerun without the target entering the data flow. |
| Output-certified | Exact outputs and verifiers agree; full upstream generation was not rerun atomically. |
| Numerical | Floating-point or statistical result with a stated tolerance. |
| Record-backed | Preserved report or ledger exists, but an upstream payload is absent or not independently regenerated. |
| Prose-only | A narrative claim without a controlling artifact. |

“Certified” is never used as a synonym for “proved.” A mathematical identity can be analytic but depend on a disputed input kernel; conversely, a cold run can be numerically precise without producing an exact theorem.

### 1.3 Evidence precedence

The controlling order is:

1. self-contained exact derivation;
2. authenticated cold reproduction;
3. exact saved output plus an independent verifier;
4. internally consistent numerical output;
5. later prose summary;
6. filename or chronology.

A newer file does not outrank an exact counterexample, and a file named “final” does not override a failed invariant.

---

## 2. Canonical notation and regime firewall

### 2.1 Hamiltonian coordinate

The canonical strong-coupling variable is

\[
\boxed{
u=\frac{\beta_{\mathrm{lat}}}{6}
=\frac{1}{g_H^4}.
}
\]

In the project normalization,

\[
H_\beta=
\frac12\sum_\ell C_2(\ell)
+\beta_{\mathrm{lat}}\sum_p
\left(
1-\frac1N\operatorname{ReTr}U_p
\right),
\]

and the plaquette perturbation is

\[
-u(\chi_p+\bar\chi_p).
\]

The archived statement \(Y=2\beta_{\mathrm{lat}}/3=4u\) is a **definition-label erratum** in the affected manuscript lineage. Its printed coefficients were generated in the canonical variable \(u\). They must not be multiplied or divided by \(4^r\).

This does not abolish the ordinary mathematical rule for a genuine change of variables. It says that the archived \(Y\)-line was not the coordinate actually used by the coefficient generator.

### 2.2 Historical series bridge

The locally implemented Hamiltonian-series bridge is

\[
H_{\mathrm{project}}=\frac12W,
\qquad
x=2u,
\qquad
[u^r]\,m(u)=2^{r-1}[x^r]\,M_A(x).
\]

The decimal \(a_4=-0.0968932328773\) is a local transcription attributed to Hamer’s table. The archive has verified the paper metadata and the \(x=2/g^4\) convention independently, but it has not yet pinned and hashed the primary table containing that decimal. It is therefore a useful local cross-check, not primary-source proof.

### 2.3 Weak-well coordinate

The compact one-plaquette large-coupling expansion uses a separate parameter \(\beta_{\mathrm{loc}}\). No coefficient is transferred between \(u\) and \(\beta_{\mathrm{loc}}\) without an explicit operator identity.

The rank-balanced variable

\[
\tau=\frac{\beta_{\mathrm{loc}}}{N^3}
\]

is a formal large-rank scaling coordinate, not an established overlap regime between the strong-coupling and weak-well series.

### 2.4 Chain-complex notation

Let

\[
C_3\xrightarrow{\mathsf C=\partial_3}
C_2\xrightarrow{\partial_2}C_1,
\qquad
\partial_2\mathsf C=0.
\]

Write

\[
Z_2=\ker\partial_2,\qquad
B_2=\operatorname{im}\mathsf C,\qquad
\mathcal H_2=Z_2\cap\ker\mathsf C^\dagger.
\]

Then

\[
Z_2=B_2\oplus\mathcal H_2,
\qquad
\mathcal H_2\simeq H_2(C_\bullet).
\]

The symbols \(B(k)\) and \(\mathsf C\) are deliberately distinct:

\[
B(k)=\partial_2(k)^\dagger
\]

is the signed face-to-link Bloch incidence matrix, while \(\mathsf C=\partial_3\) maps cube amplitudes to oriented plaquette boundaries.

### 2.5 Bloch scalars

Define

\[
d_i=e^{ik_i}-1,
\qquad
a_i=|d_i|^2
=4\sin^2\frac{k_i}{2},
\qquad
X_i=1-\cos k_i=\frac{a_i}{2}.
\]

Use

\[
q_a=\sum_i a_i,
\qquad
e_2=\sum_{i<j}a_ia_j,
\qquad
e_3=a_1a_2a_3,
\]

and

\[
\mathsf S=\sum_iX_i,\qquad
\mathsf Q=\sum_iX_i^2,\qquad
\mathsf R=\sum_{i<j}X_iX_j.
\]

Thus

\[
q_a=2\mathsf S,
\qquad
e_2=4\mathsf R.
\]

The symbol \(q_a(k)\) is never used for a perturbative scalar anchor.

---

