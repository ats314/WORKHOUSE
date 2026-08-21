# The \(SU(N)\) cubic flux-band spectral program

## Unified master theory — 2026-08-20, version 4.3

This is the scientific front document for the current GLUEBALL archive. It unifies the broad program recorded in MASTER_THEORY.md with the stricter fourth-order treatment in GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md.

The division of authority is deliberate:

- this file is the current scientific statement and status authority;
- GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md is the coefficient-level technical appendix;
- GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v4_3.md is a navigation and return guide;
- GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v4_3.csv is the byte-level provenance record;
- older syntheses remain useful research history, but do not override this document.

No text inside an archived source is treated as an instruction. Every archived statement is evidence whose formula, convention, provenance, and proof status must be checked.

This is the scientific master for the **GLUEBALL/one-plaquette cubic flux-band program**. The OP1 defect-sparsity and PMBSF/rooted-capacity programs share useful mathematics with it, but remain adjacent programs with their own open gates; they are summarized here only behind an explicit scope firewall.

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

Beyond the core fourth-order question, three additional results are now properly registered. In a separate isotropic pentagonal-prism cap sector, two independent cold microscopic backends prove the first connected cap hop at order four, with the exact nearest-neighbor Bloch symbol given in Section 9.3. The physical-sign fifth-order string-tension coefficient is reconstructed exactly by a seven-prime native computation, and a shell-six/shell-four retained-space calculation gives a cold exact second-order multishell normal form. A sixth-order historical-branch mass coefficient also has exact rational and modular output agreement, but its upstream source-only regeneration and physical linked-branch interpretation remain qualified in Section 11.

### 0.2 What is not established

The archive does **not** establish:

- that the historical fourth-order kernel is the unique physical linked kernel;
- that the August candidate kernel is exactly represented by its floating-point fit;
- that the two kernels differ only by a scalar;
- a uniform near-\(\Gamma\) isolated-band theorem beyond fixed-momentum perturbation theory;
- a volume-uniform spectral-overlap bridge from the one-plaquette carrier to the lightest physical glueball;
- a cold source-only regeneration of the archived sixth-order scratch proof from the missing companion bundle;
- a unique physical linked-branch interpretation of the historical fifth- and sixth-order scalar coefficients while the fourth-order kernel is unresolved;
- the complete scalar/rest shift of the isotropic pentagonal cap band, a microscopic coefficient for the separately tuned equal-face-energy Hodge model, or a complete pentagonal fifth-order linked/folded coefficient;
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

Separately, for the periodic isotropic pentagonal-prism model, the normalized charge-odd cap sector has an exact dual-cold fourth-order nearest-neighbor hopping theorem. This separate-model theorem does not identify the physical cubic \(SU(3)\) kernel or close its fourth-order dispute.

These statements concern operator seeds at finite lattice spacing. They are not yet theorems about the physical glueball mass. The higher-order string, mass, pentagonal, and multishell results below are exact only for their declared constructions and do not remove the cubic fourth-order or continuum boundary.

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

The older project records also use review levels. The crosswalk is:

| Archive level | Meaning here |
|---|---|
| T1 | Machine-gated reproducible artifact; normally “Cold-reproduced” if rerun here. |
| T2 | Internally reviewed artifact. |
| T3 | Externally validated artifact. |

No T3 validation record is presently registered. Therefore “proved” in this document means internally analytic or internally machine-gated under the stated hypotheses; it does not mean externally validated.

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

The canonical all-rank insertion variable is the coefficient of
\(-(\chi_p+\bar\chi_p)\):

\[
\boxed{
u:=u_{\mathrm{ins}}=\frac{\beta_N}{2N}.
}
\]

For \(SU(3)\),

\[
u=\frac{\beta_3}{6}=\frac1{g_H^4}.
\]

If an older source uses an \(SU(3)\)-normalized symbol
\(\beta_{\mathrm{lat}}:=3\beta_N/N\), then \(u=\beta_{\mathrm{lat}}/6\).
This equality must not be read as an \(N\)-independent definition of the
coefficient multiplying the all-rank Wilson term.

In the project normalization,

\[
H_\beta=
\frac12\sum_\ell C_2(\ell)
+\beta_N\sum_p
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

## 3. Exact incidence and homology

### 3.1 Retained sector

The electric energy of a fundamental plaquette is

\[
E_{F,N}=2C_F=\frac{N^2-1}{N},
\]

so \(E_{F,3}=8/3\). The construction concerns the effective Hamiltonian
projected to the degenerate one-plaquette sector. Virtual intermediate
sectors remain in the perturbative resolvents; projection of the external
sector is not deletion of virtual multi-plaquette states.

For \(SU(2)\), complex conjugation is a gauge transformation,

\[
U^*=\varepsilon U\varepsilon^{-1},
\]

so the charge-odd projector vanishes. The \(T_1^{+-}\) construction begins
at \(N=3\).

### 3.2 Signed and unsigned incidence factorizations

In the plaquette-orbital basis \((12),(13),(23)\), choose

\[
B(k)=
\begin{pmatrix}
d_2&-d_1&0\\
d_3&0&-d_1\\
0&d_3&-d_2
\end{pmatrix}.
\]

The signed shared-link adjacency satisfies

\[
\boxed{S(k)+4I=B(k)B(k)^\dagger,}
\]

and therefore

\[
\operatorname{spec}S(k)
=\{-4,-4+q_a(k),-4+q_a(k)\}.
\]

For \(k\neq\Gamma\),

\[
\psi(k)=
\begin{pmatrix}
\overline d_3\\
-\overline d_2\\
\overline d_1
\end{pmatrix},
\qquad
B(k)^\dagger\psi(k)=0,
\qquad
\|\psi(k)\|^2=q_a(k).
\]

Thus \(S(k)\psi(k)=-4\psi(k)\). This is precisely
\(\partial_2\partial_3=0\) in Bloch form.

The normalized vector has no continuous extension to \(\Gamma\), where
all three incidence branches meet. The flat band is singular: translated
cube boundaries alone do not span the torus carrier.

For the unsigned incidence matrix \(N(k)\), with
\(v_i=1+e^{ik_i}\),

\[
A(k)+4I=N(k)N(k)^\dagger,
\qquad
\det N(k)=-2v_1v_2v_3.
\]

Its determinant vanishes only on the planes \(k_i=\pi\), so the
charge-even shared-link sector has no momentum-independent band.

### 3.3 Finite-volume count

For a finite cubic complex with no four-cells,

\[
\boxed{\dim Z_2=\#C_3+b_2-b_3.}
\]

On \(T_L^3\),

\[
\operatorname{rank}\partial_3=L^3-1,
\qquad
\dim\mathcal H_2=3,
\qquad
\dim Z_2=L^3+2.
\]

The translated cube boundaries obey the single relation
\(\sum_x\partial_3c_x=0\); three wrapping sheets complete the carrier.
The first incidence level above it is

\[
4\sin^2\frac{\pi}{L}.
\]

The ordinary 12-neighbor convention assumes \(L\geq3\). At \(L=2\),
coincident periodic neighbors require an explicit multigraph convention.

The rest-frame axial \(T_1\), parity-even, charge-odd dictionary is an
analytic assignment in the one-plaquette operator space. It is not a
measured physical overlap theorem.

### 3.4 Protection and its exact boundary

If

\[
H_r(k)=a_rI+b_rS(k)+B(k)M_r(k)B(k)^\dagger,
\]

then

\[
H_r(k)\psi(k)=(a_r-4b_r)\psi(k).
\]

Hence every link-factorized correction shifts the carrier rigidly.

In real space,

\[
L_2^\downarrow=\partial_2^\dagger\partial_2,
\qquad
L_2^\uparrow=\mathsf C\mathsf C^\dagger,
\qquad
L_2^\downarrow L_2^\uparrow
=L_2^\uparrow L_2^\downarrow=0.
\]

Every polynomial in these two Laplacians acts on \(\mathcal H_2\) by its
constant term. In the model deformation \(S+\epsilon L_2^\uparrow\),
every nonzero \(\epsilon\) disperses the boundary component while retaining
the \(b_2\)-dimensional harmonic level. At \(\epsilon=0\), all of \(Z_2\)
is pinned.

This is an all-orders theorem only within the boundary-factorized corner
generated by the incidence maps. The set \(\{BMB^\dagger\}\) is not a
two-sided ideal of all endomorphisms of \(C_2\), and topology does not prove
that every physical correction belongs to it.

The possible outcomes are therefore distinct:

1. link factorization — the entire band stays flat;
2. harmonic annihilation — the band disperses but \(\mathcal H_2\) stays pinned;
3. harmonic scalar action — the triplet shifts rigidly;
4. cubic-symmetry breaking — only then can the \(T_1\) triplet split.

---

## 4. Dynamics through third order

### 4.1 Exact all-rank second-order law

The representation products are

\[
\boxed{
F\otimes\overline F=\mathbf1\oplus\mathrm{Adj},
\qquad
F\otimes F=\operatorname{Sym}^2F\oplus\Lambda^2F.
}
\]

The orientation-dependent labels “parallel” and “antiparallel” are assigned
only after fixing the shared-link convention. The two channel sums are

\[
\mathcal A_N
=-\frac{2N^3}{(N^2-1)(2N^2-1)},
\qquad
\mathcal B_N
=-\frac{4N(N^2-2)}
{(N^2-1)(4N^2-9)}.
\]

Their cancellation gives

\[
\boxed{
t_N=\mathcal B_N-\mathcal A_N
=\frac{2N(N^2-4)}
{(N^2-1)(2N^2-1)(4N^2-9)}>0.
}
\]

Moreover,

\[
\frac14-N^3t_N
=
\frac{2N^4+31N^2-9}
{4(N^2-1)(2N^2-1)(4N^2-9)}>0,
\]

and

\[
t_N=
\frac1{4N^3}
-\frac1{16N^5}
-\frac{77}{64N^7}
-\frac{1021}{256N^9}
+O(N^{-11}).
\]

The charge-odd second-order spectrum is

\[
\left\{
E_{\mathrm{flat}}^{(2)},
\;
E_{\mathrm{flat}}^{(2)}+t_Nq_a(k)u^2
\quad(\text{twice})
\right\}.
\]

Consequently,

\[
W_N^{(-)}(u)=12t_Nu^2+O(u^3),
\]

and on \(T_L^3\),

\[
\Delta_{N,L}^{(2)}
=4t_Nu^2\sin^2\frac{\pi}{L}+O(u^3).
\]

### 4.2 \(SU(3)\) second-order ledger

The exact coefficients are

\[
d_+^{(2)}=\frac{223}{1020},
\qquad
t_+^{(2)}=-\frac{11}{306},
\]

\[
d_-^{(2)}=\frac7{102},
\qquad
t_-^{(2)}=\frac5{612},
\qquad
d_-^{(2)}-4t_-^{(2)}=\frac{11}{306}.
\]

The older \(t_+^{(2)}=-481/612\) omitted a vacuum-mediated route and is
superseded.

### 4.3 Exact \(SU(3)\) third-order factorization

The effective operator is

\[
\boxed{
H_{\mathrm{eff},-}(k,u)
=E_{\mathrm{flat}}(u)I+t(u)B(k)B(k)^\dagger+O(u^4),
}
\]

with

\[
E_{\mathrm{flat}}(u)
=\frac83+u+\frac{11}{306}u^2
-\frac{109151}{249696}u^3,
\]

\[
t(u)=\frac5{612}u^2+\frac{1975}{124848}u^3.
\]

The scalar ledger is

\[
b_3=\frac{1975}{124848},
\qquad
\operatorname{leak}_3=-\frac{12331}{249696},
\]

\[
d_3=\frac7{32}
+12\operatorname{leak}_3-4b_3
=-\frac{109151}{249696}.
\]

Three-distinct-plaquette tromino numerators vanish at \(O(u^3)\), so the
incidence structure survives one order beyond the first shared-link hop.
The canonical cold checks reproduce all displayed coefficients.

This is a projected finite-order coefficient theorem. Positivity of the
truncated rest value does not prove convergence, full-sector isolation,
or identification with the lightest physical glueball.

---

## 5. The generic fourth-order obstruction space

### 5.1 Four cubic shapes

After removing the scalar anchor, the generic cubic-invariant coefficient
has four independent shapes:

\[
\boxed{
\varepsilon_4(k)
=c_0+Aq_a+Be_2+C\frac{4e_2}{q_a}
+D\frac{e_3}{q_a}.
}
\]

Equivalently,

\[
q_a\varepsilon_4
\in
\operatorname{span}
\{q_a,q_a^2,q_ae_2,e_2,e_3\}.
\]

The two-invariant tier is therefore a dynamical collapse, not a consequence
of cubic symmetry.

At

\[
X=(\pi,0,0),\quad
M=(\pi,\pi,0),\quad
P=(\pi,\pi/2,0),\quad
R=(\pi,\pi,\pi),
\]

let \(\Delta_K=\varepsilon_4(K)-\varepsilon_4(\Gamma)\). Then

\[
A=\frac{\Delta_X}{4},
\]

\[
B=\frac{\Delta_X+4\Delta_M-6\Delta_P}{16},
\]

\[
C=\frac{3(2\Delta_P-\Delta_M-\Delta_X)}8,
\]

\[
D=\frac{3(\Delta_R-6\Delta_M+6\Delta_P)}{16}.
\]

The \(q_a\) and \(4e_2/q_a\) tiers scale as \(L^{-2}\); the \(e_2\) and
\(e_3/q_a\) tiers scale as \(L^{-4}\). This regularity filtration is useful
for detecting false two-shape fits.

### 5.2 Generalized Hodge pencil

Pull \(H_4\) back to cube amplitudes:

\[
Q_4=\mathsf C^\dagger H_4\mathsf C,
\qquad
G=\mathsf C^\dagger\mathsf C.
\]

With

\[
\nabla_i=T_i-I,
\qquad
L_i=\nabla_i^\dagger\nabla_i
=2I-T_i-T_i^{-1},
\]

one has

\[
\boxed{G=\sum_iL_i.}
\]

Assume the cubic \(\Gamma\)-block is scalar,

\[
H_4(\Gamma)=s_4I_3,
\qquad
s_4=\frac13\operatorname{tr}H_4(\Gamma),
\]

and define

\[
K_4=H_4-s_4I,
\qquad
\mathcal Q_4
=\mathsf C^\dagger K_4\mathsf C
=Q_4-s_4G.
\]

The centered coefficient is a generalized eigenvalue:

\[
\boxed{\mathcal Q_4\phi=\lambda_4G\phi.}
\]

Scalar-gauge equivalence is

\[
\boxed{(Q_4,G)\sim(Q_4+\delta G,G).}
\]

This equivalence requires the simultaneous representative change
\(H_4\mapsto H_4+\delta I\), \(s_4\mapsto s_4+\delta\). Changing only the
anchor shifts the coefficient.

If the centered numerator has two invariants,

\[
\mathcal Q_4(k)=\alpha\mathsf Q+\beta\mathsf R,
\]

then, for \(k\neq\Gamma\),

\[
\boxed{
\lambda_4(k)
=\frac{\alpha\mathsf Q+\beta\mathsf R}{2\mathsf S}.
}
\]

In real space,

\[
\boxed{
\mathcal Q_4
=\frac\alpha4\sum_iL_i^2
+\frac\beta4\sum_{i<j}L_iL_j.
}
\]

When \(\alpha,\beta>0\), this is positive semidefinite on cube amplitudes.
It does not imply \(K_4\succeq0\) on the full plaquette space and does not
determine the harmonic sector.

### 5.3 Edges, holdout, stencil, and curvature

For \(\alpha,\beta>0\),

\[
0\leq\lambda_4(k)\leq\alpha+\beta.
\]

The continuous-zone minimum is unique at \(\Gamma\), and the maximum is
unique at \(R\). An odd-\(L\) grid does not contain \(R\). Thus

\[
W_4=\alpha+\beta
\]

is the continuous-zone and even-\(L\) width.

At high symmetry,

\[
\boxed{
\lambda_X=\alpha,\qquad
\lambda_M=\alpha+\frac\beta2,\qquad
\lambda_R=\alpha+\beta.
}
\]

The recommended protocol extracts \(\alpha\) and \(\beta\) from \(X,M\)
and reserves

\[
\boxed{\lambda_R=2\lambda_M-\lambda_X}
\]

as a blind holdout.

The generalized numerator has the exact 25-point stencil

\[
\begin{aligned}
(\mathcal Q_4\phi)_x={}&w_0\phi_x
+w_1\sum_i(\phi_{x+e_i}+\phi_{x-e_i})\\
&+w_2\sum_i(\phi_{x+2e_i}+\phi_{x-2e_i})\\
&+w_d\sum_{i<j}\sum_{\sigma,\tau=\pm1}
\phi_{x+\sigma e_i+\tau e_j},
\end{aligned}
\]

where

\[
w_0=\frac92\alpha+3\beta,\quad
w_1=-(\alpha+\beta),\quad
w_2=\frac\alpha4,\quad
w_d=\frac\beta4,
\]

and

\[
\boxed{w_0+6w_1+6w_2+12w_d=0.}
\]

For a unit vector \(n\),

\[
\lambda_4(tn)=a(n)t^2+O(t^4),
\]

\[
a(n)=\frac14\left[
\alpha\sum_in_i^4+
\beta\sum_{i<j}n_i^2n_j^2
\right].
\]

The radial second derivative is

\[
\boxed{
\kappa(n)=2a(n)
=\frac12\left[
\alpha\sum_in_i^4+
\beta\sum_{i<j}n_i^2n_j^2
\right].
}
\]

These are directional radial curvatures, not a Hessian at \(\Gamma\).
A cubic Hessian exists only if \(\beta=2\alpha\). At \(R\), however,

\[
\nabla^2\lambda_4(R)
=-\frac{\alpha+\beta}{6}I.
\]

Fixed-\(k\) quotient algebra does not provide uniform perturbative
isolation: \(O(u^2|k|^2)\) competes with \(O(u^4)\) for
\(|k|\lesssim u\).

---

## 6. Exact historical \(SU(3)\) fourth-order kernel

The saved 189-record kernel has

\[
\boxed{
q_{\mathrm{old}}^{(4)}
=-\frac{20721577909065127111}
{7250590288602460800}
=-2.857915988114558978\ldots
}
\]

and

\[
\boxed{
\alpha_{\mathrm{old}}=\frac5{12},
\qquad
\beta_{\mathrm{old}}
=\frac{17607806155349}{275331901291200}.
}
\]

Therefore

\[
\boxed{
\mathcal Q_{4,\mathrm{old}}
=\frac5{48}\sum_iL_i^2+
\frac{17607806155349}{1101327605164800}
\sum_{i<j}L_iL_j
\succeq0.
}
\]

The exact width is

\[
\boxed{
W_{4,\mathrm{old}}
=\frac{132329431693349}{275331901291200}
=0.48061786909826\ldots
}
\]

and the radial curvatures are

\[
\kappa_{100}=\frac5{24},
\]

\[
\kappa_{110}
=\frac{247051057231349}{2202655210329600},
\]

\[
\kappa_{111}
=\frac{132329431693349}{1651991407747200}.
\]

The exact stencil weights are

\[
w_0=\frac{189690244462349}{91777300430400},
\qquad
w_1=-\frac{132329431693349}{275331901291200},
\]

\[
w_2=\frac5{48},
\qquad
w_d=\frac{17607806155349}{1101327605164800}.
\]

In the four-shape registry,

\[
A_{\mathrm{old}}=\frac5{48},
\qquad
B_{\mathrm{old}}=D_{\mathrm{old}}=0,
\]

\[
C_{\mathrm{old}}
=-\frac{211835444920651}{4405310420659200}.
\]

The \(SU(3)\) determinant sector changes the historical diagonal shape:

\[
\Delta\beta_3=-\frac{25}{64},
\qquad
\Delta C_3=-\frac{25}{1024}.
\]

Thus the statement “determinant sectors shift only the scalar anchor” is
false at \(N=3\). For \(N\geq4\), the archived exceptional-sector analysis
does leave the centered \(\alpha,\beta\) shapes unchanged.

All identities in this section are exact for the supplied kernel and its
cold fixed-kernel checks. Their unresolved input is the upstream physical
identification of that kernel.

---

## 7. August scalar and the off-axis adjudication

### 7.1 Blind linked scalar

The linked marked-cluster computation reports

\[
\boxed{
m_\Gamma^{(4)}=-0.7751458630189173.
}
\]

The lower orders and linked scalar were computed before the historical
fourth-order targets entered the data flow. Hence this is meaningful blind
numerical evidence.

The arithmetic difference from the historical anchor is

\[
\Delta_\Gamma
=m_\Gamma^{(4)}-q_{\mathrm{old}}^{(4)}
=2.0827701250956417\ldots
\]

but this number does not prove that the two kernels differ by
\(\Delta_\Gamma I\).

### 7.2 Exact same-kernel firewall

For an unshifted new kernel \(\widehat H_4^{\mathrm{new}}\), define

\[
\widehat s_{\mathrm{new}}
=\frac13\operatorname{tr}
\widehat H_4^{\mathrm{new}}(\Gamma),
\]

\[
H_4^{\mathrm{new,mass}}
=\widehat H_4^{\mathrm{new}}
+(m_\Gamma^{(4)}-\widehat s_{\mathrm{new}})I.
\]

Then, exactly,

\[
\boxed{
H_4^{\mathrm{new,mass}}-m_\Gamma^{(4)}I
=\widehat H_4^{\mathrm{new}}
-\widehat s_{\mathrm{new}}I.
}
\]

This is scalar-gauge invariance within one chosen kernel. It says nothing
automatic about equality with the historical centered kernel.

The actual final diagonal adjustment in the 15-hour run was

\[
+11.17343231638178,
\]

chosen to map a raw folded rest value to the linked scalar. It was not
\(\Delta_\Gamma\); the equality after this step is by construction.

A near-identity coordinate change can realize a scalar reanchor formally:

\[
u_{\mathrm{old}}
=u+\delta u^4+a_5u^5+a_6u^6+a_7u^7+O(u^8),
\]

\[
H_4'=H_4+\delta I,
\]

\[
H_5'=H_5+2\delta H_2+a_5I,
\]

\[
H_6'=H_6+3\delta H_3+2a_5H_2+a_6I,
\]

\[
H_7'=H_7+4\delta H_4+3a_5H_3+2a_6H_2+a_7I.
\]

Choosing \(\delta=\Delta_\Gamma\) is a convention, not a derived physical
matching condition.

### 7.3 One surviving planar discrepancy

The August fit gives

\[
A_{\mathrm{new}}=0.104166666666728,
\]

\[
B_{\mathrm{new}}\approx3.55\times10^{-16},
\qquad
C_{\mathrm{new}}=-0.020213328886166577,
\]

\[
D_{\mathrm{new}}\approx2.23\times10^{-13},
\qquad
\alpha_{\mathrm{new}}=0.41666666666691.
\]

These are consistent with \(A=5/48\), \(B=D=0\), and \(\alpha=5/12\), but
they are not exact equalities from the new run.

Define

\[
\Delta C
=C_{\mathrm{new}}-C_{\mathrm{old}}
=0.027873054295192174\ldots
\]

If exact tier collapse and a common exact axial coefficient are assumed
for the new kernel, then

\[
\beta_{\mathrm{new}}
=8\left(\frac5{48}\right)+16C_{\mathrm{new}}
\approx0.5099200711546681,
\]

\[
W_{4,\mathrm{new}}\approx0.9265867378213348,
\]

and

\[
\boxed{
\mathsf C^\dagger
\left[
(H_4^{\mathrm{new}}-s_{\mathrm{new}}I)
-(H_4^{\mathrm{old}}-q_{\mathrm{old}}I)
\right]\mathsf C
=4\Delta C\sum_{i<j}L_iL_j.
}
\]

At the quotient level,

\[
\boxed{
\lambda_{\mathrm{new}}-\lambda_{\mathrm{old}}
=8\Delta C\frac{\mathsf R}{\mathsf S}.
}
\]

Consequently,

\[
\Delta\lambda_X=0,
\qquad
\Delta\lambda_M=8\Delta C
\approx0.2229844343615374,
\]

\[
\Delta\lambda_R=16\Delta C
\approx0.4459688687230748.
\]

The unresolved fourth-order problem is therefore compressed to one planar
mixed-gradient direction. The historical coefficients are exact; the new
ones are numerical; the displayed cross-kernel formula is conditional on
exact tier collapse for the new kernel.

The locally transcribed Hamer decimal gives

\[
8(-0.0968932328773)
=-0.7751458630184,
\]

within about \(5.2\times10^{-13}\) of the linked scalar. This remains a
normalization cross-check pending verification of the primary table.

---

## 8. All-rank historical fourth-order family

The archived family has

\[
\boxed{
\mathcal Q_{4,N}^{\mathrm{hist}}
=\frac{\alpha_N}{4}\sum_iL_i^2
+\frac{\beta_N}{4}\sum_{i<j}L_iL_j.
}
\]

The axial coefficient is

\[
\boxed{
\alpha_N=\frac{640}{N(N^2-1)^3}.
}
\]

For \(N=3\), \(\beta_3\) is the separate value in Section 6. For \(N\geq4\),
with \(z=N^2\),

\[
\boxed{
\beta_N=\frac{P_{17}(z)}{NR_{20}(z)}>0,
}
\]

where

\[
\begin{aligned}
R_{20}(z)={}&(z-1)^3(2z-3)(2z-1)^3(3z-2)(3z-1)\\
&\times(4z-9)^3(4z-5)(4z-1)(9z-25)(9z-16)\\
&\times(16z^2-44z+25)(16z^2-33z+16).
\end{aligned}
\]

The full \(P_{17}\) coefficient list remains in the technical appendix,
where it has one canonical location.

For \(N\geq7\), positivity follows from positive denominator factors and
a positive binomial-basis expansion of \(P_{17}\) about \(z=49\). The
ranks \(N=4,5,6\) are handled by exact exceptional-rank substitutions and
determinant-sector checks; \(N=3\) is separate.

Thus

\[
\mathcal Q_{4,N}^{\mathrm{hist}}\succeq0,
\qquad
W_{4,N}^{\mathrm{hist}}=\alpha_N+\beta_N.
\]

At large rank,

\[
\alpha_N\sim\frac{640}{N^7},
\qquad
\beta_N\sim\frac{6170}{9N^7},
\]

\[
\boxed{
W_{4,N}^{\mathrm{hist}}
=\frac{11930}{9N^7}
+\frac{1299983}{324N^9}
+O(N^{-11}),
}
\]

\[
\boxed{
\frac{\beta_N}{\alpha_N}\longrightarrow\frac{617}{576}.
}
\]

The scalar anchor \(q_N\) and ratios involving \(|q_N|\) are coordinate
dependent under \(H_4\mapsto H_4+\delta_NI\). The robust all-rank
statements are the centered \(\alpha_N,\beta_N,W_{4,N}\).

The all-rank claim is output-certified with cold verification of saved
symbolic outputs and exceptional-rank ledgers. The archive still lacks a
single authenticated run regenerating every upstream contraction path.

---

## 9. Temporal histories and cellular mobility

### 9.1 Energy-decorated histories

An order-\(r\) history is

\[
h=(f_1,\sigma_1;\ldots;f_r,\sigma_r).
\]

At intermediate cut \(j\),

\[
R_j
=\bar Q_j(E_0\bar G_j-\bar H_{0,j})^{-1}\bar Q_j,
\]

and schematically

\[
H_{\mathrm{eff}}^{(r)}
=\sum_{[h]\in\mathscr H_r^{\mathrm{phys}}}
\mathcal A_N[h]T_h+F_r.
\]

The static projection

\[
\pi(h)=\sum_j\sigma_je_{f_j}
\]

forgets temporal ordering. In general there exist \(h_1,h_2\) with the
same \(\pi(h)\) and different amplitudes. Static incidence alone cannot
determine the first physical mobility order.

Separate

\[
r_{\mathrm{split}}
=\min\{r:H_{\mathrm{eff}}^{(r)}(0)
\text{ has non-scalar internal splitting}\},
\]

\[
r_{\mathrm{off}}
=\min\{r:H_{\mathrm{eff}}^{(r)}(R)\neq0
\text{ for some }R\neq0\},
\]

\[
r_{\mathrm{mob}}
=\min\{r:\operatorname{spec}
H_{\mathrm{eff}}^{(\leq r)}(k)
\text{ is nonconstant in }k\}.
\]

Generally \(r_{\mathrm{off}}\leq r_{\mathrm{mob}}\), while onsite splitting
can occur without mobility.

The linked-cluster subtraction rule is essential:

\[
H_{\mathrm{eff}}\text{ is not cluster additive, whereas }
H_{\mathrm{eff}}-eI\text{ is}.
\]

Möbius subtraction must act on the vacuum-subtracted operator or gap.

### 9.2 Restricted primitive color law

For the archived restricted primitive simple-loop channel, let the listed
\(S_r>0\) be unsigned counts. The correct signed law is

\[
\boxed{
c_{r,\mathrm{prim}}(N)
=(-1)^{r+1}
\frac{2^{r-1}S_r}
{N(N^2-1)^{r-1}}.
}
\]

For

\[
(r,S_r)=(2,4),(3,16),(4,20),(5,70),
\]

this yields coefficients proportional to

\[
-8,\quad +64,\quad -160,\quad +1120.
\]

This is not a universal formula for the complete order-\(r\) amplitude.
Folded terms, determinant sectors, and temporally distinct histories can
change the result.

A static integer-circuit weight remains a useful candidate-support
diagnostic, but the archived proof that every physical reduced history
obeys \(r\geq w_{\min}-2\) is not accepted as a general amplitude theorem:
its cancellation step does not preserve temporal resolvents.

### 9.3 Pentagonal cap theorem

The pentagonal-prism calculation is a separate geometry and retained
sector. For the standard isotropic Kogut–Susskind electric Hamiltonian,

\[
H_0=\frac12\sum_eE_e^2,
\qquad
E_{\mathrm{cap}}=\frac{10}{3},
\qquad
E_{\mathrm{side}}=\frac{8}{3},
\]

the physical equal-energy one-face manifold is the normalized charge-odd
pentagonal-cap sector, not the formal cap-plus-side cycle space.

Two independent exact microscopic backends now derive, without embedding
the target numerator or denominator,

\[
\boxed{
h_4^{\mathrm{side}}
=-\frac{2861009}{84387303000},
}
\]

from the endpoint subtotals

\[
A_+=\frac{6482621}{21879000},
\qquad
A_-=\frac{9714969}{32784500},
\qquad
A_+-A_-=h_4^{\mathrm{side}}.
\]

All 48 fixed-side histories agree row by row between the two backends. The
20 cap/vacuum-\(P\)-irreducible histories give the displayed coefficient;
all 28 proper-return histories vanish individually after exact \(Q\)
projection, and the required fixed-side fourth-order fold entries vanish.
Exact \(D_5\) covariance then gives

\[
\boxed{
\tau_4
=-\frac{2861009}{16877460600},
}
\]

and, modulo a translation-invariant scalar,

\[
\boxed{
H_{\mathrm{eff,cap}}^{(4),\mathrm{conn}}
=u^4\tau_4\sum_{z\in\mathbb Z_L}
\left(
|a_z,-\rangle\langle a_{z+1},-|+
|a_{z+1},-\rangle\langle a_z,-|
\right).
}
\]

Independent open-neighborhood and periodic \(L=5\) support audits find no
connected offsite cap transfer at orders one through three. At order four,
only nearest-neighbor cap transfer survives, with \(240=5\times48\)
histories in each adjacent direction and no next-nearest transfer. Therefore

\[
\boxed{
\Delta E_{\mathrm{cap}}^{(4)}(k)
=-\frac{2861009}{8438730300}u^4\cos k,
\qquad
r_{\mathrm{hop}}^{\mathrm{iso,cap}}=4.
}
\]

The continuous fourth-order bandwidth coefficient is

\[
\boxed{
4|\tau_4|=\frac{2861009}{4219365150},
}
\]

and the band minimum is at \(k=0\). The full verification chain passes
21/21 and 24/24 internal backend gates, 17/17 strict-contract gates for
each backend, a 26/26 rowwise cross-check, 17/17 open-neighborhood gates,
27/27 periodic-operator gates, 7/7 tuned-Hodge firewall gates, and 29/29
frozen-bundle gates. A deliberate one-row mutation is rejected. The full
bundle was also cold-regenerated end to end during the current audit.

This theorem is exact for the isotropic cap band and remains outside the
cubic \(SU(3)\) kernel. The older formal cap-plus-side compression

\[
\mu(k)=\frac{4\cos k(1-\cos k)}{7-2\cos k}
\]

belongs to a different, tuned equal-face-energy Hamiltonian requiring

\[
\boxed{
w_{\mathrm{vertical}}=\frac32w_{\mathrm{horizontal}}.
}
\]

The isotropic value of \(h_4^{\mathrm{side}}\) cannot be reused there; a
fresh anisotropic microscopic backend is required. The theorem also leaves
the complete fourth-order scalar/rest shift open.

### 9.4 Pentagonal order-four frontier and zero-backend audit

A separate exact raw-frontier certificate enumerates 20 canonical
order-four histories in two temporal multisets of ten. At its three cuts,
the raw-state count, Gram rank, and nullity are

\[
\boxed{
(4,4,0),\qquad(10,6,4),\qquad(20,6,14).
}
\]

The raw Haar sectors are precisely \((1,1),(2,2),(3,3)\), whose local
Gram ranks are \(1,2,6\). Fierz/electric closure additionally generates the
\(SU(3)\)-specific \((4,1)/(1,4)\) delta–epsilon sector; its raw Gram rank is
three and its four raw tensors obey the alternating null relation

\[
-v_1+v_2-v_3+v_4=0.
\]

All 20 complete bare endpoint Haar contractions equal one. An independent
stranded-flux audit therefore falsifies the earlier zero backend: every
rejected history contains two balanced \((2,2)\) links, for which

\[
\operatorname{Wg}(e)=\frac18,
\qquad
\operatorname{Wg}((12))=-\frac1{24},
\qquad
\int_{SU(3)}|U_{11}|^4\,dU=\frac16\ne0.
\]

Both saved audits report 8/8 gates. They do not import or infer
\(h_4^{\mathrm{side}}\). Their stated next object—Fierz closure, physical
Gram quotienting, and exact reduced resolvents—was subsequently completed
for the isotropic cap sector by the dual-cold bundle in Section 9.3. The
frontier remains useful because it records exactly why the zero backend was
invalid and which determinant sector a future tuned model must retain.

### 9.5 Pentagonal direct fifth-order candidate

The newest preserved order-five transcript reports an exhaustive local
census of 537,824 signed words, 1,030 \(\mathbb Z_3\)-balanced endpoints,
120 primitive histories, and 910 \(SU(3)\)-only modular histories. The
primitive contribution is

\[
40\left(\frac1{768}\right)
+40\left(\frac1{1536}\right)
+40\left(\frac1{3072}\right)
=\frac{35}{384}.
\]

For 228 cap-dominated center-irreducible direct histories, the reported
\(+C\) and \(-C\) sums are both

\[
-\frac{725305277663}{1081888500000},
\]

so that family is charge-odd dark. For 110 triple-side-determinant direct
histories, however, the transcript reports

\[
A_+=\frac{6541241053973}{3063620102400},
\qquad
A_-=\frac{32818383}{15374800},
\]

and hence the exact-looking nonzero correction

\[
\boxed{
A_+-A_-
=\frac{235424477177}{407461473619200}.
}
\]

The resulting center-irreducible **direct-sector candidate** is

\[
\boxed{
\frac{35}{384}
+\frac{235424477177}{407461473619200}
=\frac{37373840041427}{407461473619200}
\approx0.0917236167372117.
}
\]

The transcript also reports that 90 side-determinant proper-prefix-return
five-\(V\) chains give \(-2511/1360\) at both endpoints and therefore zero
charge-odd difference. If independently regenerated, the nonzero
triple-side determinant fraction would falsify the strong conjecture that
all center-only circuits are dynamically dark before linked assembly.

This is deliberately **not promoted as a theorem**. No controlling source,
machine-readable ledger, or independently runnable certificate that derives
the final fractions has yet been located. The transcript is therefore a
prose-only candidate. Moreover, the remaining 572
proper-prefix-return histories still require the complete canonical
fifth-order folded, linked, and rooted-cluster assembly. The boxed direct
fraction is not the full \(O(u^5)\) effective-Hamiltonian coefficient.

---

## 10. Operator and numerical bridges

### 10.1 Improved charge-odd source

For traceless Hermitian \(X\), \(P_r=\operatorname{Tr}X^r\),

\[
\operatorname{ImTr}e^{iX}
=-\frac{P_3}{6}
+\frac{P_5}{120}
-\frac{P_7}{5040}
+O(|X|^9).
\]

The improved source

\[
\boxed{
\mathcal O_3^{\mathrm{imp}}(U)
=\frac{32\,\operatorname{ImTr}U-\operatorname{ImTr}U^2}{24}
}
\]

cancels the quintic term:

\[
\boxed{
\mathcal O_3^{\mathrm{imp}}(e^{iX})
=-\frac{P_3}{6}
+\frac{P_7}{1260}
+O(|X|^9).
}
\]

A second branch-free combination is

\[
\boxed{
\mathcal O_5^{\mathrm{prim}}
=\operatorname{ImTr}U^2
-8\operatorname{ImTr}U
+2(N-\operatorname{ReTr}U)\operatorname{ImTr}U
=e_5+O(|X|^7).
}
\]

For \(SU(5)\), \(e_5=\det X\). These are exact local operator identities,
not overlap theorems.

### 10.2 Current Monte Carlo record

The stored finite-volume fit at
\(\beta=5.8941\), \(L=14\), \(N_t=16\), 2000 configurations reports

\[
aM(T_1^{+-})
=1.6897344913\pm0.1206114757,
\]

\[
\text{projected variational-correlator cosh amplitude}
=0.7996986994,
\]

\[
\text{raw-correlator fitted ground-state fraction}
=0.0072359730\pm0.0164694235,
\]

\[
a\sqrt\sigma
=0.2628289891\pm0.0023244282.
\]

The variational amplitude is not automatically a normalized overlap
probability. The source/output pair lacks raw block data and source-hash
binding; one claimed hard gate is a literal truth value. These are
structured numerical outputs, not a cold ensemble certificate and not
proof that the physical state is spatially extended.

A decisive rerun should preserve block observables, bind source and input
hashes, jointly bootstrap longitudinal and transverse channels, propagate
the covariance of \(a^2\sigma\) and \(M/\sqrt\sigma\), and compare the
improved source above with the raw plaquette source.

### 10.3 Separate weak-well theorem

For the fixed-rank local \(SU(3)\) charge-even class Hamiltonian,

\[
\boxed{
\Delta_+^{SU(3)}(\beta_{\mathrm{loc}})
=
\sqrt{\frac{2\beta_{\mathrm{loc}}}{3}}
-\frac5{16}
-\frac{311\sqrt6}{9216}
\beta_{\mathrm{loc}}^{-1/2}
+O(\beta_{\mathrm{loc}}^{-1}).
}
\]

This three-term statement has the analytic remainder theorem. The next
arithmetic coefficient

\[
c_2^+(3)=-\frac{5665}{110592}
\]

is exact in the perturbative ledger, but promotion with an
\(O(\beta_{\mathrm{loc}}^{-3/2})\) remainder is open.

The fixed-rank all-\(N\) formulas have mixed status: \(c_0^\pm\) is
analytic; \(c_1^\pm\) has exact-arithmetic checks for \(N=3,\ldots,12\);
the unrestricted closed forms remain conjectural; small-rank \(c_2^\pm\)
gaps remain. None of these local class-Hamiltonian gaps is a lattice
glueball or continuum gap.

The exceptional-point atlas is likewise certified only for a finite
restricted class-pencil truncation. It does not establish the convergence
radius of the spatial strong-coupling operator.

---

## 11. Higher-order and multishell results

### 11.1 Historical fifth-order cubic band

The historical \(SU(3)\) fifth-order output has the same two-invariant
shape,

\[
c_5(k)
=q_5^{\mathrm{hist}}
+\frac{A_5\mathsf Q+B_5\mathsf R}{2\mathsf S},
\]

with

\[
q_5^{\mathrm{hist}}
=-\frac{866236750503342026253096691057}
{1169668083793811403447133488000},
\]

\[
A_5=\frac{313}{240},
\]

\[
B_5=
\frac{1881863087742908605903793}
{1652932248975967181040000},
\]

\[
\Delta c_5=A_5+B_5
=
\frac{4037562229115732471176793}
{1652932248975967181040000}.
\]

The saved-output arithmetic and anchor gates are exact. Its physical scalar
interpretation inherits the unresolved fourth-order source-chain issue.

### 11.2 Native string tension through fifth order

In the canonical physical perturbation convention,

\[
\boxed{
\begin{aligned}
\sigma(u)
={}&\frac23
-\frac{22}{153}u^2
-\frac{61}{408}u^3\\
&-\frac{737327120374220449}
{7250590288602460800}u^4\\
&-\frac{137767222189182735950309}
{2009803206414863779920000}u^5
+O(u^6).
\end{aligned}
}
\]

The native engine reconstructs the positive unit-insertion magnitude

\[
\sigma_{5}^{\mathrm{raw}}
=
\frac{137767222189182735950309}
{2009803206414863779920000}
\]

from \(22{,}820\) canonical topologies modulo seven independent primes.
Their product has 189 bits; the 77-bit numerator and 81-bit denominator
lie below the 94-bit uniqueness bound, and the rational round-trips
against all seven stored residues. The physical perturbation
\(V=-\sum_p(\chi_p+\bar\chi_p)\) supplies

\[
\sigma_n^{\mathrm{phys}}=(-1)^n\sigma_n^{\mathrm{raw}},
\]

so both odd physical coefficients are negative. The positive odd signs
in parts of the June registry and in the raw certificate are not the
canonical \(u\)-series signs.

This pass independently rechecked all seven residue round-trips and the
reconstruction bound. The per-prime intermediate pickles are not present,
so the full native calculation was not cold-regenerated here; its status
is exact output-certified native reconstruction, not a new cold run.

The scale-matched ratio has the undisputed lower-order part

\[
\frac{m_{1^{+-}}(u)}{\sqrt{\sigma(u)}}
=
\sqrt6
\left(
\frac43+\frac12u+\frac{11}{68}u^2
-\frac{7559}{499392}u^3
+O(u^4)
\right).
\]

The \(u^4\) and higher ratio coefficients still inherit the physical
fourth-order mass-kernel dispute. The fifth-order tension input itself is
no longer merely a historical target.

### 11.3 Sixth-order historical-branch computational result

The later scratch-proof output closes the *contraction* stage of the
historical one-flux branch. Define that branch by

\[
\begin{aligned}
m_{\mathrm{hist}}(u)
={}&\frac83+u+\frac{11}{306}u^2
-\frac{109151}{249696}u^3\\
&+q_{\mathrm{band}}^{(4)}u^4
+q_5^{\mathrm{hist}}u^5
+m_6^{\mathrm{hist}}u^6+O(u^7).
\end{aligned}
\]

Then the archived exact rational result is

\[
\boxed{
m_6^{\mathrm{hist}}
=
-\frac{
156998370765216917515896262601525405897211506214753116643443873
}{
4880681791275629050759264798095652027950878794719744000000
}
}
\]

or

\[
m_6^{\mathrm{hist}}
\approx-32167.303151345863.
\]

The original release authenticates 27 files and the scratch-results release
authenticates 86. The scratch rational contraction covers
\(205{,}699\) nonzero \(\Gamma\)-blocks and \(10{,}907{,}384\) path
choices. A separately implemented modular contraction recomputes all
blocks and agrees with the exact fraction:

\[
m_6^{\mathrm{hist}}\equiv461041\pmod{1000003},
\qquad
m_6^{\mathrm{hist}}\equiv822068\pmod{1000033}.
\]

The rational and modular engines share the scratch topology and local
tensor artifacts, and the named source-only companion bundle is absent.
The correct evidence label is therefore:

> exact output-certified contraction agreement for the stated historical
> construction; not cold source-regenerated from the presently accessible
> corpus.

If the same historical branch and normalization-corrected tension series
are used, the archive derives

\[
c_6^{\mathrm{hist}}
=
-\frac{
4270353824428899200786427191557487127249971701568661364147801
}{
265509089445394220361304005016403470320527806432754073600
}.
\]

Neither coefficient is automatically the physical linked-branch
coefficient. The series above contains
\(q_{\mathrm{band}}^{(4)}\), whereas the August linked scalar is
\(m_\Gamma^{(4)}\). Under the near-identity map of Section 7.2,
\(H_6\) changes by \(3\delta H_3+2a_5H_2+a_6I\); until the matching
coordinate and fourth-order kernel are fixed, there is no unique promoted
physical \(m_6\) or \(c_6\).

### 11.4 Shell-six and shell-four/shell-six companion theorem

A separate retained-space calculation, in the same canonical
\(u=\beta_{\mathrm{lat}}/6\) convention, gives the first-order-flat
charge-odd shell-six channels

\[
E_{0^{--}}
=4-\frac{6117632}{479655}u^2+O(u^3),
\qquad
E_{3^{+-}}
=4-\frac{21281}{1530}u^2+O(u^3),
\]

\[
E_{2^{--},E}
=4-\frac{6597287}{479655}u^2+O(u^3),
\qquad
E_{2^{--},T_2}
=4-\frac{6277517}{479655}u^2+O(u^3),
\]

and the two \(T_2^{+-}\) second-order coefficients

\[
-\frac{27013849}{1918620}
\pm\frac{\sqrt{59782141}}{9180}.
\]

The three shell-six \(T_1^{+-}\) branches are

\[
E_{6,-}
=4-\frac{2\sqrt2}{3}u+
\left(
-\frac{13029053}{959310}-\frac{\sqrt2}{2}
\right)u^2+O(u^3),
\]

\[
E_{6,0}
=4-\frac{52959}{3553}u^2+O(u^3),
\]

\[
E_{6,+}
=4+\frac{2\sqrt2}{3}u+
\left(
-\frac{13029053}{959310}+\frac{\sqrt2}{2}
\right)u^2+O(u^3).
\]

In particular,

\[
E_{3^{+-}}-E_{0^{--}}
=-\frac{1107923}{959310}u^2+O(u^3).
\]

The projected shell-four/shell-six couplings obey

\[
g_-^2=\frac49,\qquad
g_0^2=\frac89,\qquad
g_+^2=\frac49,\qquad
g_{\mathrm{tot}}^2=\frac{16}{9}.
\]

Thus the virtual shell-six contribution is

\[
-\frac34g_{\mathrm{tot}}^2=-\frac43,
\]

and the unfolded shell-four coefficient is

\[
\boxed{
m_{2,\mathrm{unfolded}}
=\frac{11}{306}+\frac43
=\frac{419}{306}.
}
\]

The complete atomic ZIP cold-passes every release gate. The extracted
browsing folder is incomplete—it lacks
`shell6_o2_analysis_v2.json`—so the ZIP, not that folder, is the
reproducible authority. These identities are exact inside the declared
shell-six and shell-four/shell-six retained-space construction. They do
not prove the full-Hilbert-space physical eigenvalue, continuum survival,
or the still-missing cross-shell \(O(u^2)\) matrix elements.

---

## 12. Infinite-volume, comparator, and capacity firewall

### 12.1 Core glueball firewall

A Bernoulli rare-box argument proves that every global fixed-window defect
firewall fails: at fixed positive defect density, the projected norm tends
to one in probability as volume grows.

The rooted replacement begins with the exact source-tilt identity

\[
\mathbb E_{\beta,L}
\exp\left(t\sum_{p\in\Gamma}V_p\right)
=
\frac{Z_{\beta,t,\Gamma,L}}{Z_{\beta,L}}.
\]

Its Peierls and rooted-capacity implications require the open inhomogeneous
free-energy estimate

\[
\frac{Z_{\beta,\alpha,\Gamma,L}}{Z_{\beta,L}}
\leq K_\alpha^{|\Gamma|}
\]

and a separate source-radius reduction. Even if those are proved, three
further steps remain independent:

1. a volume-uniform dressed-operator spectral-overlap theorem;
2. survival of the relevant level beyond the one-plaquette retained sector;
3. a controlled continuum limit.

The finite-volume incidence isolation scales as \(L^{-2}\) and collapses
as \(L\to\infty\). No formula in this document is a proof of the
Yang–Mills mass gap.

### 12.2 Adjacent OP1 deterministic comparator claim

The OP1 defect-sparsity program is separate from the cubic glueball
operator. Its deterministic comparator half has an exact Fourier
decomposition. On the four-torus, let

\[
\widehat w(n)=\sum_{\mu=1}^{4}
\sin^2\left(\frac{\pi n_\mu}{L}\right),
\]

\[
g_H=\frac1{m_0^2L^4},
\qquad
T_H=\frac1{m_0^4L^4},
\]

\[
g_C=
\frac3{4L^4}
\sum_{n\ne0}
\frac1{m_0^2+\alpha_W\widehat w(n)},
\qquad
T_C=
\frac3{4L^4}
\sum_{n\ne0}
\frac1{(m_0^2+\alpha_W\widehat w(n))^2},
\]

with

\[
g_{\mathrm{diag}}=g_H+g_C,
\qquad
T_{\mathrm{full}}=T_H+T_C.
\]

The proposed all-volume cover inequality is

\[
\Phi_L(t)^4-L^{-4}\leq q(t)^4
\qquad(L\geq4,\ t>0),
\]

where

\[
\Phi_L(t)=\frac1L\sum_{n=0}^{L-1}
e^{-4t\sin^2(\pi n/L)},
\qquad
q(t)=e^{-2t}I_0(2t).
\]

Lemma B gives the much stronger rationally assembled bound

\[
\boxed{
C_\infty(x)
\leq
G_{\mathrm{BOUND}}
=0.018664535031\ldots
<\frac1{28},
}
\]

subject only to the stated cited intervals for \(\pi\) and Euler’s
constant. If the cover inequality is upgraded to a rigorous numerical
enclosure, then on the AF diagonal \((m_0^2,v_0)=(1/2,1)\),

\[
T_C\leq0.124806<\frac18,
\qquad
N_C^*\geq8,
\qquad
T_{\mathrm{full}}<\frac9{64},
\qquad
N^*\geq7
\]

uniformly for every integer \(L\geq4\).

This pass cold-ran Lemma A’s WB0–WB5 gates and both parts of Lemma B;
all advertised gates reproduced. That does **not** make Lemma A
theorem-grade: its compact-window runner uses ordinary mpmath values
with padding, non-enclosed quadrature/Bessel evaluations, and sampled
validity checks. The margins are large, so this is strong
computer-assisted evidence, but the all-\(L\) cover and its floor
corollaries remain conditional pending true intervalization or analytic
error bounds. The stochastic covariance hypothesis,
comparator-to-true-Hessian calibration, and continuum closure also remain
open.

### 12.3 Adjacent cap-geometry correction

The bare single-cap geometry has the exact identities

\[
\Delta_p
=1-\cos(\alpha-\beta)
=2\sin^2\delta,
\qquad
\chi_0=2\sin\sigma\sin\delta,
\]

and therefore

\[
\boxed{
\Delta_p\geq\frac{\chi_0^2}{2}.
}
\]

For multiple caps, the correct contextual quantity is the height drop

\[
\Delta_p(A)=h(A)-h(A\cup\{p\}),
\]

For regular full-dimensional intersections---in particular, when both
\(C_A\) and \(C_A\cap C_p\) are positive-measure continuity sets for the
Laplace principle---the compact-manifold exponential-rate theorem is

\[
\boxed{
\lim_{\kappa\to\infty}
-\frac1\kappa
\log\nu_\kappa(C_p\mid C_A)
=
\Delta_p(A).
}
\]

No uniqueness of the maximizing configuration is needed at exponential
rate. Empty or lower-dimensional intersections are excluded from this
statement; there the conditional probability can be zero or undefined.

The older universal reduction from an incident \(\chi_0\) to
\(\Delta_p(A)\) is false. Uniform finite-\(\kappa\) prefactors, stochastic
typicality, and far-source decay remain open, so this rate theorem does
not close PMBSF or the glueball continuum bridge.

### 12.4 Checkerboard/local-curvature obstruction

For the local plaquette Hessian,

\[
H_{ab}
=
\frac16\operatorname{Re}
\operatorname{tr}\!\left(\{T_a,T_b\}U_p\right),
\qquad
\operatorname{tr}H
=
\frac43(1-s_p).
\]

The deposited engine only scans a \(240\times240\) angle grid, but the
local onset can be closed analytically. Diagonalize

\[
U_p=\operatorname{diag}(e^{i\theta_1},e^{i\theta_2},e^{i\theta_3}),
\qquad c_j=\cos\theta_j,
\qquad R=\sum_jc_j=3(1-s_p),
\]

and write \(t=\operatorname{tr}U_p=R+iI\). The six off-diagonal Hessian
eigenvalues are \((c_i+c_j)/12\), while the Cartan-plane determinant is
proportional to

\[
E_2=c_1c_2+c_1c_3+c_2c_3.
\]

The exact identity

\[
\boxed{
4E_2=2R+|t|^2-3=(R-1)(R+3)+I^2
}
\]

shows that \(s_p<2/3\), hence \(R>1\), makes every pair sum
\(c_i+c_j=R-c_k\) positive and gives \(E_2>0\). The Cartan trace is
positive as well, so its positive determinant makes the Cartan form
positive. At
\(U_p=\operatorname{diag}(1,i,-i)\), \(R=1\) and a zero mode appears;
along \(\operatorname{diag}(1,e^{i\theta},e^{-i\theta})\) with
\(\theta>\pi/2\), that mode is negative. Thus the exact **local** onset
is \(s_p^*=2/3\). Independently, \(s_p>1\) forces a negative direction
by the trace law.

This local theorem does not by itself prove a global comparator ceiling.
The claimed \(\delta\leq1\) faithfulness ceiling is valid only for the
project’s *per-plaquette PSD-background domination* architecture; mass,
neighboring, or global compensation remains possible without a separate
domination theorem.

---

## 13. Governing evidence ledger

| Claim | Claim status | Evidence level |
|---|---|---|
| Incidence factorization, spectrum, Betti count | Proven | Analytic; 14/14 cold topology gates |
| Independent Bloch and lower-order checks | Proven | 36/36 cold gates; Windows requires UTF-8 output mode |
| All-rank \(t_N\) | Proven | Analytic and saved-output verified |
| \(SU(3)\) \(O(u^3)\) factorization | Proven for the retained operator | 251/251 cold exact gates |
| Historical 189-record \(O(u^4)\) pencil and stencil | Exact for saved kernel | Cold fixed-kernel reproduction |
| Historical all-rank \(\alpha_N,\beta_N\) family | Exact for saved outputs | Cold verifiers; no one-shot upstream regeneration |
| August \(m_\Gamma^{(4)}\) | Live candidate | Blind numerical linked-cluster output |
| August \(A,B,C,D\) | Live candidate | Floating-point fit |
| Old and new centered kernels equal | Not established | Contradicted by current off-axis fits |
| Marked-cluster adjudicator | Open physics run | Self-test 47/47; geometry 609/609; zero physics contractions |
| Marked-engine companion tests | One stale test | 20/21; expected-status string is obsolete |
| Isotropic pentagonal cap hop | Proven for separate retained model | Two independent cold microscopic backends; full bundle cold-regenerated |
| Pentagonal \(O(4)\) raw representation frontier | Exact for its declared raw spaces | Source/certificate pair; 8/8 saved gates |
| Stranded-flux zero backend | Falsified | Exact \(SU(3)\) Haar witness and 8/8 saved audit gates |
| Pentagonal direct \(O(5)\) modular correction | Candidate only | Transcript-backed/prose-only; no located generating source or certificate |
| Monte Carlo source/output | Numerical | Structured output; no raw ensemble certificate |
| Local weak-well three-term gap | Proven locally | Analytic fixed-rank theorem |
| Native physical \(\sigma_5\) | Exact for native construction | Seven-prime CRT output certificate; sign fixed by normalization audit |
| Historical-branch \(m_6\) | Exact for saved construction | Rational plus two modular contractions; shared upstream artifacts; source-only bundle missing |
| Shell-six/shell-four normal form | Proven for retained model | Complete atomic ZIP cold-reproduced; T1 |
| OP1 all-volume comparator ceiling | Conditional | Lemma B rationally certified; Lemma A reproduces with non-interval high precision and samples |
| Bare/multicap exponential rate | Proven in stated finite-dimensional setting | Analytic; prefactor, typicality, and far-source gates remain open |
| Complete physical cubic \(O(u^4)\) kernel | Open | Decisive target-blind run not complete |
| Continuum Yang–Mills mass gap | Open | No bridge or construction |

The local Lean tree contains no encoding of the 189-record kernel,
\(\alpha,\beta\), the scalar adjudication, or the generalized Hodge pencil.
Its unfinished or axiomatized mass-gap statements are not evidence here.
The organized SU(2)/q-\(6j\)/TRG experiment archive is useful context but
has no substantive \(SU(3)\) \(O(u^4)\) overlap.

---

## 14. Governing contradiction and errata register

1. **Coupling.** The archived \(Y=4u\) line is a label erratum; no
   \(4^r\) coefficient rescaling is allowed.
2. **All-rank coordinate.** The insertion coefficient is
   \(u=\beta_N/(2N)\); \(u=\beta_3/6\) is the \(SU(3)\) specialization.
3. **Tensor products.**
   \(F\otimes\bar F=\mathbf1\oplus\mathrm{Adj}\) and
   \(F\otimes F=\operatorname{Sym}^2F\oplus\Lambda^2F\).
4. **Fourth-order scalar.**
   \(q_{\mathrm{old}}^{(4)}=-2.8579\ldots\) and
   \(m_\Gamma^{(4)}=-0.7751\ldots\) are different coordinates/results;
   their difference alone proves no kernel identity.
5. **Off-axis coefficient.**
   \(C_{\mathrm{old}}=-0.0480863\ldots\) and
   \(C_{\mathrm{new}}=-0.0202133\ldots\) cannot be reconciled by an
   identity shift.
6. **Run shift.** The final August adjustment was
   \(+11.17343231638178\), target-derived; it was not
   \(\Delta_\Gamma\).
7. **New tier collapse.** Historical \(A=5/48,B=D=0\) is exact; the new
   fit agrees only numerically.
8. **Curvature.** The \(\Gamma\) quantities are radial directional second
   derivatives, not a Hessian unless \(\beta=2\alpha\).
9. **Primitive sign.** Positive counts \(S_r\) require the factor
   \((-1)^{r+1}\).
10. **Circuit rule.** Static circuit completion is not a universal equality
    for physical mobility order.
11. **Weak-well order.** The analytic theorem stops with an
    \(O(\beta_{\mathrm{loc}}^{-1})\) remainder; the next coefficient is
    arithmetic, not yet a promoted asymptotic term.
12. **Monte Carlo language.** The stored amplitude is not automatically a
    normalized overlap probability.
13. **Exceptional scalarity.** At \(SU(4)\), the certified statement is a
    flat-branch eigenvalue identity, not scalarity of the full exceptional
    operator.
14. **String signs.** The native finite-field certificate records positive
    unit-insertion odd coefficients; the physical canonical \(u\)-series has
    \(\sigma_n^{\mathrm{phys}}=(-1)^n\sigma_n^{\mathrm{raw}}\).
15. **Sixth-order scope.** The exact saved \(m_6\) belongs to the branch whose
    fourth-order scalar is \(q_{\mathrm{band}}^{(4)}\). It is not a uniquely
    matched physical linked coefficient while the fourth-order kernel and
    coupling scheme remain unresolved.
16. **Registry lag.** `F:\THEORY\STATE.md` and `PROGRAM_INDEX.md` predate the
    later scratch-proof output and contain stale higher-order status/sign cells.
17. **Cap geometry.** The old incident-step reduction is false; the correct
    multicap rate is the contextual height drop \(h(A)-h(A\cup\{p\})\).
18. **Atomic shell-six source.** The extracted browsing directory is missing a
    required analysis JSON; the complete ZIP is the reproducible authority.
19. **OP1 enclosure.** Lemma A’s ordinary high-precision padding and samples
    are not directed interval arithmetic; its unconditional-theorem label is
    downgraded pending intervalization or analytic error bounds.
20. **Pentagonal provenance.** The older 60,144-byte
    `pentagonal_verification_bundle.zip` correctly rejected an imported-only
    \(h_4^{\mathrm{side}}\) payload. It is superseded for that coefficient by
    the 111,743-byte dual-cold bundle, whose two target-blind backends and
    operator audits pass under end-to-end cold regeneration.
21. **Pentagonal Hamiltonian firewall.** In the standard isotropic model the
    physical retained manifold is cap-only and the symbol is \(2\tau_4\cos k\).
    The formal cap-plus-side Hodge symbol belongs to the separately tuned
    ratio \(w_{\mathrm{vertical}}/w_{\mathrm{horizontal}}=3/2\); the isotropic
    coefficient cannot be transferred to it.
22. **Pentagonal fifth-order scope.** The displayed nonzero modular correction
    is a direct-sector transcript result, not a complete folded/linked
    coefficient and not yet a source-regenerated theorem.
23. **Scope.** A positive projected finite-order coefficient is not a
    full-Hamiltonian, infinite-volume, or continuum gap theorem.

---

## 15. Decisive research program

### 15.1 First priority: one target-blind fourth-order artifact

The next production run must freeze and authenticate:

1. the all-rank insertion coordinate and the \(Y\)-erratum;
2. the exact order-four occurrence schedule;
3. all \(203\times3=609\) exact marked-cluster evaluations;
4. a rooted Möbius ledger on the vacuum-subtracted object;
5. source, input, checkpoint, and output hashes;
6. no historical scalar or shape target in the data flow;
7. a cold 3,895-topology Stage-3H generation of an unshifted 189-record kernel;
8. \(X/M\) extraction, blind \(R\) holdout, and full Laurent-symbol equality;
9. an independent scalar ledger testing
   \(q_{\mathrm{band}}^{(4)}-E_0^{(4)}
   \stackrel?=m_\Gamma^{(4)}\);
10. the \(W_{22}\) order toggle across all 33 rooted classes;
11. \(m_\Gamma^{(4)}\) and \(C^{(4)}\) from the same sealed run.

The 3,895 Stage-3H topologies and the 3,850 stable-rank trace topologies
are different inventories and must never be interchanged.

### 15.2 Second priority: regenerate the all-rank chain atomically

One authenticated run should regenerate the 4,171-word inventory, 35,130
fusion paths, determinant exceptions, \(P_{17}\), \(R_{20}\), positivity,
and fixed-rank anchors. Current saved-output verification is strong; this
step closes provenance rather than repairing failed algebra.

### 15.3 Third priority: uniformity and physics bridge

Prove the two-parameter estimate for \(|k|\lesssim u\), then rerun the
finite-momentum operator analysis with the improved source and stored block
observables. Only after a dressed-operator spectral bridge is proved do
PC-2, source-radius control, multi-plaquette survival, and a continuum
construction become relevant.

### 15.4 Higher-order and geometry program

After fourth-order adjudication:

- obtain the missing source-only scratch-proof bundle and cold-regenerate the
  sixth-order geometry, tensor, and contraction chain atomically;
- compute the native sixth-order string/torelon coefficient \(\sigma_6\);
- derive linked-branch fifth- and sixth-order coefficients only after declaring
  and matching the fourth-order scalar/kernel coordinate;
- compute the still-missing cross-shell \(O(u^2)\) matrix elements;
- derive a classification of energy-decorated temporal histories;
- reconstruct the pentagonal \(O(u^5)\) direct ledger from source, then
  assemble all 572 proper-prefix-return histories with the complete canonical
  folded, linked, and rooted-cluster formula;
- build a fresh anisotropic microscopic backend before assigning any
  coefficient to the tuned equal-face-energy pentagonal Hodge model;
- determine whether the two-invariant tier collapse has a selection-rule
  explanation;
- test the hyperhoneycomb candidate only after constructing the actual
  retained-sector compression;
- replace OP1 Lemma A’s ordinary high-precision cells by rigorous intervals or
  analytic error bounds;
- for OP1/PMBSF, keep deterministic comparator and cap-rate statements separate
  while attacking stochastic covariance, typicality, and far-source decay.

---

## Appendix A. Source roles

The authoritative reading order is:

1. **Scientific authority:** this unified master.
2. **Technical appendix:** GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md.
3. **Navigation:** GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v4_3.md.
4. **Provenance:** GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v4_3.csv.

The current June manuscript and corrected all-rank V2 ZIPs remain the
canonical sources for the saved historical fourth-order family. The 15-hour
transcript and result file control the August numerical adjudication. The
seven-prime native certificate controls \(\sigma_5\); the scratch-results ZIP
controls the output-certified historical-branch \(m_6\); and the complete
shell-six ZIP controls the multishell companion theorem. The marked engine
is the designated future fourth-order decider, but its present preflight
contains zero physics contractions.

For the separate pentagonal model, the 111,743-byte
`pentagonal_o4_dual_cold_verification_bundle.zip` controls the isotropic
fourth-order cap theorem. The order-four raw-frontier and zero-backend
source/certificate pairs are independent diagnostic records. The order-five
resolvent transcript is a candidate lead only until its generating source and
machine-readable ledger are recovered.

Older MASTER_THEORY.md retains a valuable long claims ledger and research
history. It is superseded as a status authority by this file because it
used the stale \(Y=4u\) interpretation, reversed two tensor products,
overstated the new tier collapse, treated radial warping as a Hessian, and
phrased cross-kernel scalar reanchoring too strongly.

---

## Appendix B. Shortest safe statement

\[
\boxed{
\begin{aligned}
&S(k)+4I=B(k)B(k)^\dagger,\qquad
\operatorname{spec}S(k)=\{-4,-4+q_a,-4+q_a\};\\
&\dim\ker\partial_2=\#C_3+b_2-b_3,\qquad
\dim\ker\partial_2(T_L^3)=L^3+2;\\
&t_N=
\frac{2N(N^2-4)}
{(N^2-1)(2N^2-1)(4N^2-9)};\\
&H_{\mathrm{eff},-}^{SU(3)}
=E_{\mathrm{flat}}(u)I+t(u)BB^\dagger+O(u^4);\\
&\mathcal Q_4\phi=\lambda_4G\phi,\qquad
G=\sum_iL_i,\qquad
(Q_4,G)\sim(Q_4+\delta G,G);\\
&\mathcal Q_{4,N}^{\mathrm{hist}}
=\frac{\alpha_N}{4}\sum_iL_i^2+
\frac{\beta_N}{4}\sum_{i<j}L_iL_j,\qquad
\alpha_N=\frac{640}{N(N^2-1)^3}.
\end{aligned}
}
\]

This establishes exact homological structure, exact \(SU(3)\) flatness
through third order, and an exact positive fourth-order pencil for the
saved historical family. The archive also contains an exact native
physical-sign \(\sigma_5\), an output-certified historical-branch \(m_6\),
and a cold exact shell-six retained-space normal form. In a separate geometry,
the isotropic pentagonal cap band has an exact dual-cold fourth-order
nearest-neighbor hop; its fifth-order direct correction remains a prose-only
candidate. None reconciles the August off-axis candidate with the historical
fourth-order kernel. The complete physical fourth-order kernel, the spectral bridge, the
infinite-volume theory, and the continuum mass gap remain open.
