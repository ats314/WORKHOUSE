# Cubic Hodge flux-band mobility

## Detailed theorem, reconciliation, and evidence document — version 3.1

**Date:** 2026-08-20  
**Scope:** the cubic-lattice, charge-conjugation-odd one-plaquette sector; its homological carrier; perturbative mobility through fourth order; the archived all-rank family; the August linked-cluster scalar; and the boundary between exact algebra, numerical evidence, and open physical identification.

This version supersedes the earlier detailed formula document, its v2 revision, and the intermediate v3 draft. It is a research-status theorem, not a continuum Yang–Mills mass-gap theorem. The object should be called the **one-plaquette \(T_1^{+-}\) flux band/operator seed**, not the physical glueball without a separate overlap and continuum argument.

---

## 1. Evidence firewall

The document uses the following status vocabulary. The consolidated ledger in Section 17 controls whenever a paragraph does not carry its own label.

| Label | Meaning |
|---|---|
| **Analytic exact** | Follows from displayed finite-dimensional algebra, topology, or a directly checkable identity. |
| **Cold-certified** | Recomputed from source and inputs without inserting the target value. |
| **Output-certified** | Exact saved outputs and independent verifiers agree, but the entire upstream generator has not been cold-regenerated in one authenticated run. |
| **Conditional exact** | Exact once a named kernel, factorization, or tier-collapse hypothesis is accepted. |
| **Numerical evidence** | Floating-point or statistical output with stated limitations. |
| **Open / audit-pending** | The available files do not close the claim. |

Three distinctions control the whole document:

1. an exact theorem about a **saved kernel** is not automatically a derivation of the physical kernel;
2. a scalar identity shift cannot repair a disagreement in a centered off-axis shape coefficient;
3. a source program, a passing self-test, and a completed physics calculation are three different objects.

---

## 2. Coupling and normalization registry

### 2.1 Canonical Hamiltonian coordinate

The canonical strong-coupling coordinate is

\[
\boxed{
u=\frac{\beta_{\mathrm{lat}}}{6}=\frac{1}{g_H^4},
\qquad
\beta_{\mathrm{lat}}=\frac{6}{g_H^4}.
}
\]

We write

\[
H_{\mathrm{eff}}(u)=\sum_{r\ge0}u^rH_r.
\]

### 2.2 The archived \(Y=4u\) statement is an erratum, not a rescaling rule

An archived v0.8 source printed

\[
Y=\frac{2\beta_{\mathrm{lat}}}{3}=4u.
\]

The normalization audit found that this was a factor-four **definition/label error**: the contractions and printed coefficients were already coefficients of

\[
u=\frac{\beta_{\mathrm{lat}}}{6}=\frac1{g_H^4}.
\]

The corrected v0.8a/v1.1 sources changed the label without rescaling the coefficients. Therefore the old fourth-order numbers must not be divided by \(4^4\), and the lower-order series must not be multiplied by powers of four.

Other historical symbols remain source-specific. The safe rule is

\[
\boxed{
\text{match the Hamiltonian prefactor before converting any legacy coupling symbol.}
}
\]

### 2.3 Hamiltonian-series bridge used in the historical comparison

The local comparison uses

\[
H_{\mathrm{project}}=\frac12W,
\qquad
x=2u,
\qquad
m(u)=\frac12M_A(2u).
\]

If \(M_A(x)=\sum_ra_rx^r\), then

\[
\boxed{m_r=2^{r-1}a_r.}
\]

The convention \(x=2/g_H^4\) is independently present in the historical Hamiltonian literature stored with the project. However, the decimal \(a_4=-0.0968932328773\) used locally is a **notebook transcription**; it has not yet been checked against a hashed primary copy of the Hamer table. It is a strong local cross-check, not primary-source verification of that decimal.

### 2.4 Separate weak-well coordinate

The one-plaquette large-field asymptotics later in this document use \(\beta_{\mathrm{loc}}\). It must not be silently identified with \(\beta_{\mathrm{lat}}\), \(u\), or a Euclidean Wilson coupling.

---

## 3. Cubic chain complex and the flat carrier

Let

\[
C_3\xrightarrow{\mathsf C=\partial_3}C_2
\xrightarrow{\partial_2}C_1
\]

be the oriented cellular chain complex. Define

\[
B(k):=\partial_2(k)^\dagger.
\]

The boundary identity is

\[
\boxed{\partial_2\mathsf C=0,}
\]

so

\[
B(k)^\dagger w(k)=0
\]

for the Fourier symbol \(w(k)\) of \(\mathsf C\).

Set

\[
d_j(k)=e^{ik_j}-1,
\qquad
q(k)=\sum_j|d_j(k)|^2
=4\sum_j\sin^2\frac{k_j}{2},
\]

and, up to the fixed orientation convention,

\[
w(k)=
\begin{pmatrix}
\overline d_3\\
-\overline d_2\\
\overline d_1
\end{pmatrix},
\qquad
w^\dagger w=q(k).
\]

The signed plaquette adjacency obeys

\[
\boxed{S(k)+4I=B(k)B(k)^\dagger,}
\]

and therefore

\[
\boxed{
\operatorname{spec}S(k)
=\{-4,-4+q(k),-4+q(k)\}.
}
\]

For \(k\ne0\),

\[
P_{\mathrm{flat}}(k)=\frac{w(k)w(k)^\dagger}{q(k)}.
\]

The \(k=0\) fiber is a homology problem, not a quotient by \(q(0)\).

**Status:** analytic exact.

### 3.1 Finite-volume multiplicity

For a finite three-dimensional cell complex,

\[
\boxed{
\dim\ker\partial_2=\#C_3+b_2-b_3.
}
\]

On the periodic cubic torus \(T_L^3\),

\[
\operatorname{rank}\partial_3=L^3-1,
\qquad
\dim\ker\partial_2=L^3+2.
\]

Define

\[
Z_2:=\ker\partial_2,
\qquad
B_2:=\operatorname{im}\partial_3,
\]

and the harmonic representative space

\[
\mathcal H_2:=Z_2\cap\ker\partial_3^\dagger
\cong H_2(C_\bullet).
\]

Then

\[
Z_2=B_2\oplus\mathcal H_2,
\qquad
\dim B_2=L^3-1,
\qquad
\dim\mathcal H_2=3.
\]

The \(L^3\) translated cube boundaries have one telescoping relation; the other three states are harmonic wrapping sheets. The first nonflat adjacency level is

\[
\boxed{4\sin^2\frac{\pi}{L},}
\]

so finite-volume isolation closes as \(L^{-2}\).

In the archived orientation/representation dictionary, a compact cube boundary is assigned \(A_1^{--}\) and telescopes at zero momentum, while the harmonic plane triplet is assigned axial \(T_1\), parity \(+\), and \(C=-\) from the imaginary-trace source. The topology of the split is exact; the representation-to-interpolating-operator bridge is a separate analytic interpretation and should not be mislabeled as a measured physical overlap.

The simple 12-neighbor adjacency convention used above assumes \(L\ge3\). At \(L=2\), coincident periodic neighbors require a separate multigraph/incidence convention.

**Status:** topology analytic exact; representation dictionary analytic/supporting. Stored finite-\(L\) computations are checks, not the proof.

---

## 4. Exact second-order all-rank law

For \(SU(N)\), \(N\ge3\),

\[
\boxed{
t_N=
\frac{2N(N^2-4)}{(N^2-1)(2N^2-1)(4N^2-9)}.
}
\]

It is positive, and its expansion is

\[
\boxed{
t_N=
\frac1{4N^3}-\frac1{16N^5}-\frac{77}{64N^7}
+O(N^{-9}).
}
\]

Equivalently,

\[
\frac14-N^3t_N
=\frac{2N^4+31N^2-9}
{4(N^2-1)(2N^2-1)(4N^2-9)}>0.
\]

The one-plaquette \(C\)-odd bandwidth begins as

\[
\boxed{
W_N^{(-)}(u)=12t_Nu^2+O(u^3)
\sim\frac{3u^2}{N^3}.
}
\]

For \(SU(3)\),

\[
t_3=\frac5{612}.
\]

The exact second-order spectrum is

\[
\operatorname{spec}H_-^{(2)}(k)
=\left\{
E_{\mathrm{flat}}^{(2)},
E_{\mathrm{flat}}^{(2)}+\frac5{612}q(k)u^2,
E_{\mathrm{flat}}^{(2)}+\frac5{612}q(k)u^2
\right\},
\]

where

\[
E_{\mathrm{flat}}^{(2)}=\frac83+u+\frac{11}{306}u^2.
\]

The exact ledger is

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

The \(C\)-even branch has no momentum-independent eigenvalue: its adjacency spectra at \(\Gamma\) and \(R\) have empty intersection.

**Status:** analytic exact and certificate-backed.

---

## 5. Exact \(SU(3)\) factorization through third order

The strongest uncontested perturbative result is

\[
\boxed{
H_{\mathrm{eff},-}(k,u)
=E_{\mathrm{flat}}(u)I+t(u)B(k)B(k)^\dagger+O(u^4),
}
\]

with

\[
\boxed{
E_{\mathrm{flat}}(u)
=\frac83+u+\frac{11}{306}u^2
-\frac{109151}{249696}u^3,
}
\]

and

\[
\boxed{
t(u)=\frac5{612}u^2+\frac{1975}{124848}u^3.
}
\]

Since \(B^\dagger w=0\),

\[
H_{\mathrm{eff},-}(k,u)w(k)
=E_{\mathrm{flat}}(u)w(k)+O(u^4).
\]

One useful third-order bookkeeping form is

\[
b_3=\frac{1975}{124848},
\qquad
\operatorname{leak}_3=-\frac{12331}{249696},
\]

\[
d_3=\frac7{32}+12\operatorname{leak}_3-4b_3
=-\frac{109151}{249696}.
\]

The name \(\operatorname{leak}_3\) is used to avoid collision with an older all-rank symbol \(\ell_N\).

**Status:** cold-certified plus analytic incidence factorization.

---

## 6. What homology protects—and what it does not

### 6.1 Link-mediated annihilating ideal

If

\[
H(k)=aI+bS(k)+B(k)M(k)B(k)^\dagger,
\]

then

\[
H(k)w(k)=(a-4b)w(k).
\]

Equivalently,

\[
P_{\mathrm{flat}}BMB^\dagger P_{\mathrm{flat}}=0.
\]

This is sufficient protection, not an if-and-only-if criterion for arbitrary corrections. The correct order-\(r\) flatness criterion is

\[
\boxed{
P_{\mathrm{flat}}H_rP_{\mathrm{flat}}=c_rP_{\mathrm{flat}},
}
\]

with the appropriate perturbative mixing assumptions.

### 6.2 Boundary-Laplacian algebra

Define

\[
L_2^\downarrow=\partial_2^\dagger\partial_2,
\qquad
L_2^\uparrow=\partial_3\partial_3^\dagger.
\]

Then

\[
\boxed{
L_2^\downarrow L_2^\uparrow
=L_2^\uparrow L_2^\downarrow=0.
}
\]

Every polynomial in these operators acts on

\[
\mathcal H_2=\ker\partial_2\cap\ker\partial_3^\dagger
\]

by its constant term. This is an all-orders theorem **inside this operator algebra**, not a theorem that every physical correction belongs to it.

### 6.3 Four possible outcomes

1. **Link factorization:** the entire band remains flat.
2. **Harmonic annihilation:** the band disperses but the \(\mathcal H_2\) triplet stays pinned.
3. **Harmonic scalar:** the triplet shifts rigidly without splitting.
4. **Cubic-symmetry breaking:** only then can the \(T_1\) triplet split.

Band dispersion and rest-multiplet splitting are therefore different questions.

---

## 7. The fourth-order generalized Hodge pencil

Let \(H_4\) act on plaquette amplitudes. Pull it back to cube amplitudes:

\[
Q_4:=\mathsf C^\dagger H_4\mathsf C,
\qquad
G:=\mathsf C^\dagger\mathsf C.
\]

With

\[
\nabla_i=T_i-I,
\qquad
L_i=\nabla_i^\dagger\nabla_i
=2I-T_i-T_i^{-1},
\]

the Gram operator is

\[
\boxed{G=\sum_iL_i.}
\]

Assume the cubic \(\Gamma\) block is scalar,

\[
H_4(\Gamma)=s_4I_3,
\qquad
s_4=\frac13\operatorname{tr}H_4(\Gamma),
\]

and define

\[
K_4:=H_4-s_4I,
\qquad
\boxed{\mathcal Q_4:=\mathsf C^\dagger K_4\mathsf C=Q_4-s_4G.}
\]

The centered band coefficient is not an ordinary eigenvalue of \(\mathcal Q_4\). It solves

\[
\boxed{
\mathcal Q_4\phi=\lambda_4G\phi.
}
\]

Equivalently, the uncentered pencil has the scalar equivalence

\[
\boxed{
(Q_4,G)\sim(Q_4+\delta G,G).
}
\]

This is the precise operator meaning of fourth-order scalar-gauge freedom.

Define

\[
X_i=1-\cos k_i,
\qquad
\mathsf S=\sum_iX_i,
\qquad
\mathsf Q=\sum_iX_i^2,
\qquad
\mathsf R=\sum_{i<j}X_iX_j.
\]

The symbols of \(G\) and \(\mathcal Q_4\) are

\[
G(k)=2\mathsf S,
\qquad
\mathcal Q_4(k)=\alpha\mathsf Q+\beta\mathsf R.
\]

Thus, for \(k\ne\Gamma\),

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

If \(\alpha,\beta>0\), then \(\mathcal Q_4\succeq0\) on cube amplitudes. This does **not** imply \(K_4\succeq0\) on the full plaquette space, and it does not by itself determine the harmonic \(H_2\) sector.

**Status:** analytic exact once the two-invariant symbol is given.

### 7.1 Exact edges

Since \(0\le X_i\le2\),

\[
\mathsf Q\le2\mathsf S,
\qquad
\mathsf R\le2\mathsf S.
\]

For \(\alpha,\beta>0\),

\[
0\le\lambda_4(k)\le\alpha+\beta.
\]

In the continuous Brillouin zone the lower edge is unique at \(\Gamma\) and the upper edge is unique at \(R=(\pi,\pi,\pi)\). The same holds on an even-\(L\) torus; an odd-\(L\) momentum grid does not contain \(R\). Hence, in the continuous problem,

\[
\boxed{W_4=\alpha+\beta.}
\]

### 7.2 High-symmetry reconstruction and blind holdout

At \(X,M,R\),

\[
\boxed{
\lambda_X=\alpha,
\qquad
\lambda_M=\alpha+\frac\beta2,
\qquad
\lambda_R=\alpha+\beta.
}
\]

Therefore

\[
\alpha=\lambda_X,
\qquad
\beta=2(\lambda_M-\lambda_X),
\]

while

\[
\boxed{\lambda_R=2\lambda_M-\lambda_X}
\]

should be reserved as a blind holdout rather than used in the fit.

For the full four-shape basis of Section 10, let \(\Delta_K=\varepsilon_4(K)-\varepsilon_4(\Gamma)\). Then the target-free checkpoint extraction is

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

### 7.3 Directional radial curvatures at \(\Gamma\)

For a unit vector \(n\),

\[
\lambda_4(tn)=a(n)t^2+O(t^4),
\]

where

\[
a(n)=\frac14\left[
\alpha\sum_in_i^4
+\beta\sum_{i<j}n_i^2n_j^2
\right].
\]

The directional second derivative is

\[
\boxed{
\kappa(n)=2a(n)
=\frac12\left[
\alpha\sum_in_i^4
+\beta\sum_{i<j}n_i^2n_j^2
\right].
}
\]

These are **radial directional curvatures**, not the entries of a Hessian at \(\Gamma\). A genuine quadratic Hessian compatible with cubic symmetry would require direction independence, which here is equivalent to

\[
\beta=2\alpha.
\]

The historical kernel does not satisfy that relation, so it has cubic warping and no single effective-mass tensor at \(\Gamma\).

At \(R\), by contrast,

\[
\lambda_4(R+tn)
=(\alpha+\beta)-\frac{\alpha+\beta}{12}t^2+O(t^4),
\]

and the Hessian is genuinely isotropic:

\[
\nabla^2\lambda_4(R)=-\frac{\alpha+\beta}{6}I.
\]

### 7.4 Near-\(\Gamma\) perturbative warning

The fixed-\(k\) quotient algebra above is exact. Uniform perturbative isolation is a separate problem: the second-order separation is \(O(u^2|k|^2)\), which competes with fourth-order terms for \(|k|\lesssim u\). A physical band theorem uniform in both \(u\to0\) and \(k\to0\) requires an additional two-parameter estimate.

---

## 8. Historical exact \(SU(3)\) fourth-order pencil

The packaged 189-record historical kernel has

\[
\boxed{
q_{\mathrm{old}}^{(4)}
=-\frac{20721577909065127111}{7250590288602460800}
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
=\frac5{48}\sum_iL_i^2
+\frac{17607806155349}{1101327605164800}
\sum_{i<j}L_iL_j\succeq0.
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

The directional second derivatives are

\[
\boxed{\kappa_{100}=\frac5{24},}
\]

\[
\boxed{
\kappa_{110}
=\frac{247051057231349}{2202655210329600},
}
\]

\[
\boxed{
\kappa_{111}
=\frac{132329431693349}{1651991407747200}.
}
\]

### 8.1 Exact 25-point numerator stencil

On cube amplitudes,

\[
\begin{aligned}
(\mathcal Q_4\phi)_x={}&w_0\phi_x
+w_1\sum_i(\phi_{x+e_i}+\phi_{x-e_i})\\
&+w_2\sum_i(\phi_{x+2e_i}+\phi_{x-2e_i})\\
&+w_d\sum_{i<j}\sum_{\sigma,\tau=\pm1}
\phi_{x+\sigma e_i+\tau e_j}.
\end{aligned}
\]

For any two-invariant pencil,

\[
w_0=\frac92\alpha+3\beta,
\qquad
w_1=-(\alpha+\beta),
\qquad
w_2=\frac\alpha4,
\qquad
w_d=\frac\beta4.
\]

For the historical kernel,

\[
\boxed{
w_0=\frac{189690244462349}{91777300430400},
\qquad
w_1=-\frac{132329431693349}{275331901291200},
}
\]

\[
\boxed{
w_2=\frac5{48},
\qquad
w_d=\frac{17607806155349}{1101327605164800}.
}
\]

The zero-mode gate is

\[
\boxed{w_0+6w_1+6w_2+12w_d=0.}
\]

This stencil is the generalized-eigenvalue **numerator**. Dividing its Fourier symbol by \(G(k)=2\mathsf S\) produces the physical centered coefficient.

**Status:** exact for the supplied historical kernel; its saved-kernel checks are cold reproducible. The unresolved gate is upstream physical identification.

---

## 9. The August \(\Gamma\) scalar and the scalar-reanchor firewall

The August linked marked-cluster run reports

\[
\boxed{m_\Gamma^{(4)}=-0.7751458630189173.}
\]

Its data flow computes the linked scalar before the historical \(q_{\mathrm{old}}\), the historical shape coefficient, or the final diagonal adjustment enters. The lower orders were recovered first. Thus this number is meaningful numerical evidence for the linked \(\Gamma\) coefficient.

The numerical difference is

\[
\boxed{
\Delta_\Gamma=m_\Gamma^{(4)}-q_{\mathrm{old}}^{(4)}
=2.0827701250956417\ldots
}
\]

But this arithmetic difference does **not** prove that the new physical kernel is the old kernel plus \(\Delta_\Gamma I\).

### 9.1 What is always valid inside one chosen kernel

Let \(\widehat H_4^{\mathrm{new}}\) be an unshifted new kernel and

\[
\widehat s_{\mathrm{new}}
=\frac13\operatorname{tr}\widehat H_4^{\mathrm{new}}(\Gamma).
\]

Define

\[
H_4^{\mathrm{new,mass}}
=\widehat H_4^{\mathrm{new}}
+(m_\Gamma^{(4)}-\widehat s_{\mathrm{new}})I.
\]

Then the exact same-kernel identity is

\[
\boxed{
H_4^{\mathrm{new,mass}}-m_\Gamma^{(4)}I
=\widehat H_4^{\mathrm{new}}-\widehat s_{\mathrm{new}}I.
}
\]

Equivalently,

\[
\mathsf C^\dagger[(H_4+\delta I)-(s_4+\delta)I]\mathsf C
=\mathsf C^\dagger(H_4-s_4I)\mathsf C.
\]

### 9.2 What is not established

The actual final diagonal shift used in the 15-hour run was

\[
+11.17343231638178,
\]

chosen to move a raw folded rest value to the linked scalar. It was not \(\Delta_\Gamma\), and final equality after that step is by construction.

No present calculation derives \(\Delta_\Gamma\) as a physical counterterm or proves

\[
H_4^{\mathrm{new,centered}}=H_4^{\mathrm{old,centered}}.
\]

The safe statement is:

\[
\boxed{
\text{the two quoted \(\Gamma\) anchors differ by a scalar number, while the candidate centered kernels also disagree off axis.}
}
\]

### 9.3 Coupling-coordinate bookkeeping

A general near-identity coordinate change is

\[
u_{\mathrm{old}}
=u+\delta u^4+a_5u^5+a_6u^6+a_7u^7+O(u^8).
\]

Because \(H_1=I\), its coefficients transform as

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

The shorter formulas with only \(\delta\) correspond to the explicitly chosen minimal gauge

\[
a_5=a_6=a_7=0.
\]

Choosing \(\delta=\Delta_\Gamma\) is a mathematically valid coordinate convention; no current file establishes it as the physically selected convention.

The locally transcribed Hamer value maps as

\[
8(-0.0968932328773)=-0.7751458630184,
\]

within roughly \(5.2\times10^{-13}\) of the linked scalar. This is a strong local normalization check, subject to the primary-table caveat in Section 2.3.

---

## 10. The decisive off-axis discrepancy

Set

\[
a_i=4\sin^2\frac{k_i}{2}=2X_i,
\qquad
\Sigma_a=\sum_ia_i,
\]

\[
e_2=\sum_{i<j}a_ia_j,
\qquad
e_3=a_1a_2a_3.
\]

The general cubic fourth-order shape is

\[
\varepsilon_4(k)=c_0+A\Sigma_a+Be_2
+C\frac{4e_2}{\Sigma_a}
+D\frac{e_3}{\Sigma_a}.
\]

On an exact two-invariant tier \(B=D=0\),

\[
\boxed{
\alpha=4A,
\qquad
\beta=8A+16C.
}
\]

For the historical saved kernel,

\[
A_{\mathrm{old}}=\frac5{48},
\qquad
B_{\mathrm{old}}=D_{\mathrm{old}}=0,
\]

\[
C_{\mathrm{old}}
=-\frac{211835444920651}{4405310420659200}
=-0.04808638318135875\ldots
\]

exactly.

The newer numerical fit gives

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

These are consistent with \(A=5/48\), \(B=D=0\), and \(\alpha=5/12\), but they are not exact rational equalities from the new run.

Define

\[
\Delta C=C_{\mathrm{new}}-C_{\mathrm{old}}
=0.027873054295192174\ldots
\]

If the numerical tier collapse and common axial value are accepted exactly, then

\[
\beta_{\mathrm{new}}
=8\left(\frac5{48}\right)+16C_{\mathrm{new}}
\approx0.5099200711546681,
\]

\[
W_{4,\mathrm{new}}\approx0.9265867378213348,
\]

and the pulled-back centered difference is

\[
\boxed{
\mathsf C^\dagger
\left[
(H_4^{\mathrm{new}}-s_{\mathrm{new}}I)
-(H_4^{\mathrm{old}}-q_{\mathrm{old}}I)
\right]
\mathsf C
=4\Delta C\sum_{i<j}L_iL_j\succeq0.
}
\]

At the generalized-eigenvalue level,

\[
\boxed{
\lambda_{\mathrm{new}}(k)-\lambda_{\mathrm{old}}(k)
=8\Delta C\frac{\mathsf R}{\mathsf S}\ge0.
}
\]

It vanishes on momentum axes and is strictly positive when at least two components are nonzero. In particular,

\[
\Delta\lambda_X=0,
\]

\[
\Delta\lambda_M=8\Delta C
\approx0.2229844343615374,
\]

\[
\Delta\lambda_R=16\Delta C
\approx0.4459688687230748.
\]

Thus the unresolved fourth-order problem has been compressed to one planar mixed-gradient direction. The axial coefficient is common within numerical tolerance; the planar coefficient is not.

**Status:** historical coefficients exact for the saved kernel; new coefficients numerical; exact new tier collapse, new rational \(C\), and the complete physical off-axis kernel remain audit-pending.

---

## 11. All-rank historical fourth-order family

The archived symbolic outputs give, for every \(N\ge3\),

\[
\boxed{
\mathcal Q_{4,N}
=\mathsf C^\dagger(H_{4,N}-q_NI)\mathsf C
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

For \(N=3\), use the separate exact \(\beta_3\) in Section 8. For \(N\ge4\), with \(z=N^2\),

\[
\boxed{
\beta_N=\frac{P_{17}(z)}{N R_{20}(z)}>0.
}
\]

The denominator is

\[
\begin{aligned}
R_{20}(z)={}&(z-1)^3(2z-3)(2z-1)^3(3z-2)(3z-1)\\
&\times(4z-9)^3(4z-5)(4z-1)(9z-25)(9z-16)\\
&\times(16z^2-44z+25)(16z^2-33z+16).
\end{aligned}
\]

Consequently,

\[
\mathcal Q_{4,N}\succeq0,
\qquad
W_{4,N}=\alpha_N+\beta_N.
\]

At large rank,

\[
\alpha_N\sim\frac{640}{N^7},
\qquad
\beta_N\sim\frac{6170}{9N^7},
\]

\[
\boxed{
W_{4,N}\sim\frac{11930}{9N^7}.
}
\]

In particular,

\[
\boxed{
\frac{\beta_N}{\alpha_N}\longrightarrow\frac{617}{576}.
}
\]

For \(N\ge7\), the archived positivity proof uses positive denominator factors and a certified positive binomial-basis expansion of \(P_{17}\) about \(z=49\). The ranks \(N=4,5,6\) are handled by exact exceptional-rank substitutions/determinant-sector checks, and \(N=3\) uses its separate exact \(\beta_3\).

The all-rank real-space formula follows from equality of finite-range Fourier symbols, but it was not separately packaged and gated as an all-rank real-space theorem.

**Status:** output-certified with cold fixed-rank and exceptional-rank checks; not yet a one-shot cold regeneration of every upstream path.

---

## 12. Temporal histories and linked-cluster discipline

An ordered perturbative history is

\[
h=(f_1,\sigma_1;\ldots;f_r,\sigma_r).
\]

At intermediate cut \(j\), the physical reduced resolvent has the form

\[
R_j=\bar Q_j(E_0\bar G_j-\bar H_{0,j})^{-1}\bar Q_j.
\]

The order-\(r\) effective operator is schematically

\[
\boxed{
H_{\mathrm{eff}}^{(r)}
=\sum_{[h]\in\mathscr H_r^{\mathrm{phys}}}
\mathcal A_N[h]T_h+F_r.
}
\]

The static displacement map

\[
\pi(h)=\sum_j\sigma_je_{f_j}
\]

does not retain temporal ordering. In general,

\[
\boxed{
\exists h_1,h_2:
\pi(h_1)=\pi(h_2),
\quad
\mathcal A_N[h_1]\ne\mathcal A_N[h_2].
}
\]

This is why a static chain-complex argument alone cannot determine the first physical mobility order.

For a restricted primitive simple-loop channel, the archived color-counting law is

\[
c_{r,\mathrm{prim}}(N)
=\frac{S_r}{N^rC_F^{r-1}}
=\frac{2^{r-1}S_r}{N(N^2-1)^{r-1}}
\sim N^{-(2r-1)}.
\]

This is not a universal formula for complete order-\(r\) amplitudes: folded terms, determinant sectors, and temporally distinct histories can alter the full coefficient.

It is useful to separate

\[
r_{\mathrm{split}}
=\min\{r:H_{\mathrm{eff}}^{(r)}(0)
\text{ has non-scalar internal splitting}\},
\]

\[
r_{\mathrm{off}}
=\min\{r:H_{\mathrm{eff}}^{(r)}(R)\ne0
\text{ for some }R\ne0\},
\]

\[
r_{\mathrm{mob}}
=\min\{r:\operatorname{spec}H_{\mathrm{eff}}^{(\le r)}(k)
\text{ is nonconstant in }k\}.
\]

Generally \(r_{\mathrm{off}}\le r_{\mathrm{mob}}\), while onsite splitting can occur without mobility.

The linked excited-state method also imposes a crucial subtraction rule:

\[
H_{\mathrm{eff}}\ \text{is not cluster additive, whereas}
\quad H_{\mathrm{eff}}-eI\ \text{is cluster additive}.
\]

Subcluster subtraction must therefore be applied to the vacuum-subtracted operator or gap, not blindly to raw \(H_{\mathrm{eff}}\).

---

## 13. An improved charge-odd plaquette source

For traceless Hermitian \(X\), write \(P_r=\operatorname{Tr}X^r\). Then

\[
\boxed{
\operatorname{ImTr}e^{iX}
=-\frac{P_3}{6}+\frac{P_5}{120}
-\frac{P_7}{5040}+O(|X|^9).
}
\]

The linear combination

\[
\boxed{
\mathcal O_3^{\mathrm{imp}}(U)
=\frac{32\,\operatorname{ImTr}U-\operatorname{ImTr}U^2}{24}
}
\]

cancels the entire quintic term for every \(SU(N)\):

\[
\boxed{
\mathcal O_3^{\mathrm{imp}}(e^{iX})
=-\frac{P_3}{6}+\frac{P_7}{1260}+O(|X|^9).
}
\]

This is an analytic power-series identity and supplies a cleaner Monte Carlo source for the leading cubic \(C\)-odd tensor. Its practical overlap and variance must be measured; no novelty claim is made here.

For \(SU(3)\), with eigenangles summing to zero,

\[
\operatorname{ImTr}U
=-\frac{P_3}{6}
\prod_{j=1}^3\operatorname{sinc}\frac{\theta_j}{2}.
\]

For \(SU(4)\), choosing \(\theta_4=-(\theta_1+\theta_2+\theta_3)\),

\[
\operatorname{ImTr}U
=-\frac{P_3}{6}
\prod_{ij\in\{12,13,23\}}
\operatorname{sinc}\frac{\theta_i+\theta_j}{2}.
\]

For \(SU(5)\) and above, Newton's identities give

\[
P_5=\frac56P_2P_3+5e_5,
\]

so

\[
\operatorname{ImTr}e^{iX}
=-\frac{P_3}{6}\left(1-\frac{P_2}{24}\right)
+\frac{e_5}{24}+O(|X|^7).
\]

This shows where an independent primitive quintic charge-odd direction first becomes available. It is an operator-structure statement, not a proof of a new lattice band.

---

## 14. Monte Carlo interface and current numerical record

For the spatial plaquette source,

\[
\mathcal O_i(t)=\sum_x\operatorname{ImTr}U_{jk}(x,t),
\qquad(i,j,k)\ \text{cyclic}.
\]

At nonzero momentum,

\[
d_i=e^{ik_i}-1,
\qquad
q=d^\dagger d,
\qquad
e_L=\frac d{\sqrt q},
\]

with an orthonormal transverse complement. Three useful isotropy diagnostics are

\[
R_{\mathrm{shift}}
=\frac{3(E_{100}-E_0)}{E_{111}-E_0},
\]

\[
R_{E^2}
=\frac{3(E_{100}^2-E_0^2)}{E_{111}^2-E_0^2},
\]

\[
R_{\cosh}
=\frac{3(\cosh E_{100}-\cosh E_0)}
{\cosh E_{111}-\cosh E_0}.
\]

Each tends to one under its corresponding isotropic-dispersion hypothesis.

The stored `CERT_O4_next14.json` record reports, for \(\beta=5.8941\), \(L=14\), \(N_t=16\), and 2000 configurations,

\[
aM(T_1^{+-})=1.6897344913\pm0.1206114757,
\]

\[
\text{smeared amplitude}=0.7996986994,
\]

\[
\text{raw one-plaquette fitted fraction}
=0.0072359730\pm0.0164694235,
\]

\[
a\sqrt\sigma=0.2628289891\pm0.0023244282.
\]

The JSON records 23/23 gates as passing, but one “physical zero-momentum carrier” gate is a literal truth value in the source rather than a computed test. The JSON is not source-hash bound, contains non-RFC `NaN` tokens, and no raw August ensemble/checkpoint was found. Consequently it is structured finite-volume numerical evidence, not a cold-reproducible ensemble certificate.

A publishable reanalysis should store raw or block-level observables, bind every output to source and inputs, jointly bootstrap longitudinal and transverse channels, and propagate covariance between \(a^2\sigma\) and \(M/\sqrt\sigma\).

---

## 15. Separate companion results

### 15.1 Pentagonal cap mobility

The pentagonal-prism calculation is a different retained sector and geometry. Its dual-cold result is

\[
\boxed{
h_4^{\mathrm{side}}
=-\frac{2861009}{84387303000},
}
\]

\[
\boxed{
\tau_4=-\frac{2861009}{16877460600},
}
\]

\[
\boxed{
\Delta E_{\mathrm{cap}}^{(4)}(k)
=-\frac{2861009}{8438730300}u^4\cos k,
\qquad r_{\mathrm{hop}}=4.
}
\]

**Status:** cold-certified connected offsite cap operator modulo a scalar; not evidence for the cubic \(SU(3)\) off-axis coefficient.

### 15.2 Local \(SU(3)\) weak-well gap

For the fixed-rank one-plaquette \(C\)-even class Hamiltonian,

\[
\boxed{
\Delta_+^{SU(3)}(\beta_{\mathrm{loc}})
=\sqrt{\frac{2\beta_{\mathrm{loc}}}{3}}
-\frac5{16}
-\frac{311\sqrt6}{9216}\beta_{\mathrm{loc}}^{-1/2}
+O(\beta_{\mathrm{loc}}^{-1}).
}
\]

**Status:** local semiclassical theorem. It is not a lattice glueball gap and not a continuum mass-gap theorem.

---

## 16. Maximal defensible theorem

Combining only the safe layers:

\[
\boxed{
\begin{aligned}
&S(k)+4I=B(k)B(k)^\dagger,
\qquad
\operatorname{spec}S(k)=\{-4,-4+q,-4+q\};\\[1mm]
&\dim\ker\partial_2=\#C_3+b_2-b_3,
\qquad
\dim\ker\partial_2(T_L^3)=L^3+2;\\[1mm]
&H_{\mathrm{eff},-}^{SU(3)}
=E_{\mathrm{flat}}(u)I+t(u)BB^\dagger+O(u^4);\\[1mm]
&\mathcal Q_{4,N}
=\frac{\alpha_N}{4}\sum_iL_i^2
+\frac{\beta_N}{4}\sum_{i<j}L_iL_j\succeq0
\quad\text{for the archived historical family};\\[1mm]
&(Q_4,G)\sim(Q_4+\delta G,G),
\quad
\mathcal Q_4\phi=\lambda_4G\phi.
\end{aligned}
}
\]

This establishes a homological carrier, exact \(SU(3)\) flatness through third order, the exact historical fourth-order generalized Hodge pencil, its local sum of squares, unique \(\Gamma/R\) edges, rank-cubic second-order hopping, rank-seventh historical fourth-order mobility, and exact scalar-gauge invariance **within a chosen kernel**.

It does not establish that the historical centered fourth-order kernel is the final physical linked kernel.

---

## 17. Current status ledger

| Claim | Status |
|---|---|
| Incidence factorization and Bloch spectrum | Analytic exact |
| Torus split \(L^3+2=(L^3-1)+3\) | Analytic exact |
| All-rank second-order \(t_N\) | Analytic exact / certificate-backed |
| \(SU(3)\) flat carrier through \(O(u^3)\) | Cold-certified |
| Historical 189-record centered \(O(u^4)\) pencil/SOS | Exact for saved kernel; cold fixed-kernel reproduction |
| Historical 25-point numerator stencil and edges | Analytic exact for saved kernel |
| Linked scalar \(m_\Gamma^{(4)}=-0.7751458630\ldots\) | Blind numerical evidence from the completed run |
| Locally transcribed Hamer decimal | Convention cross-check; primary table not yet verified |
| Same-kernel scalar-gauge identity | Analytic exact |
| Old kernel equals new kernel plus a scalar | Not established |
| New \(A,B,C,D\) shape fit | Numerical; exact tier collapse open |
| Complete physical momentum-resolved \(SU(3)\) \(O(u^4)\) kernel | Open |
| All-rank historical centered family | Output-certified; not full cold regeneration |
| Improved \(\mathcal O_3^{\mathrm{imp}}\) source | Analytic exact series cancellation |
| `CERT_O4_next14.json` ensemble result | Structured numerical evidence; not cold reproducible |
| Pentagonal cap hop | Cold-certified, separate model |
| Current Lean tree verifies these formulas | False; it contains no encoding of this \(O(u^4)\) theorem |
| Continuum Yang–Mills mass gap | Not established |

---

## 18. Decisive verification program

### 18.1 Physical fourth-order adjudication

The next physical run must freeze and authenticate:

1. the canonical \(u\) normalization and its erratum;
2. the exact order-four occurrence schedule;
3. all \(203\times3=609\) exact rational marked-cluster evaluations and a rooted Möbius ledger;
4. linked subtraction applied to the vacuum-subtracted object;
5. checkpoint hashes and input identities, with comparison targets loaded only after sealing;
6. no historical target in scalar or shape data flow;
7. a cold 3,895-topology Stage-3H run producing an unshifted 189-record kernel;
8. direct \(X/M\) extraction, a blind \(R\) holdout, and then full Laurent-symbol equality;
9. an independent scalar ledger testing \(q_{\mathrm{band}}^{(4)}-E_0^{(4)}\stackrel?=m_\Gamma^{(4)}\);
10. the \(W_{22}\) order-schedule toggle across all 33 rooted classes;
11. both \(m_\Gamma^{(4)}\) and \(C^{(4)}\) from the same run.

The exact marked-cluster engine currently passes its cheap algebra and geometry preflights, but it has not produced a full physics certificate.

### 18.2 All-rank regeneration

One authenticated run should regenerate the 4,171-word inventory, 35,130 fusion paths, exceptional determinant sectors, \(P_{17}\), \(R_{20}\), positivity, and fixed-rank anchors. The 3,895 Stage-3H topologies and 3,850 stable-rank trace topologies are different inventories and must never be interchanged. The stored symbolic verifiers are strong, but the entire chain is not yet one cold artifact.

### 18.3 Uniform band control

Prove a two-parameter estimate in the regime \(|k|\lesssim u\). Without it, a fixed-momentum coefficient theorem must not be promoted to a uniformly isolated near-\(\Gamma\) physical band theorem.

### 18.4 Monte Carlo bridge

Rerun the operator analysis with stored block observables, the improved cubic source, authenticated code/output hashes, joint polarization bootstrap, and full covariance propagation.

---

## Appendix A. All-rank numerator polynomial

With \(z=N^2\),

\[
\begin{aligned}
P_{17}(z)={}&2096187310080z^{17}
-45206560309248z^{16}
+448972002607104z^{15}\\
&-2723575470882816z^{14}
+11288692151812096z^{13}
-33888218411529728z^{12}\\
&+76218901019673664z^{11}
-131068691814847264z^{10}
+174326341061538992z^9\\
&-180230597250871976z^8
+144751635142984472z^7
-89742150515602808z^6\\
&+42388925672412712z^5
-14916377727371552z^4
+3768794520714128z^3\\
&-641987460459360z^2
+65414604672000z
-2967321600000.
\end{aligned}
\]

The compact \(\beta_N\) formula is not to be substituted at \(N=3\); use the separate exact \(SU(3)\) value.

---

## Appendix B. The shortest safe interpretation

The scalar-invariant theorem is

\[
\boxed{
\mathsf C^\dagger[(H_4+\delta I)-(s_4+\delta)I]\mathsf C
=\mathsf C^\dagger(H_4-s_4I)\mathsf C.
}
\]

It says exactly what scalar re-anchoring can and cannot do:

- it can change the quoted rest coordinate within a chosen kernel;
- it cannot change a centered planar coefficient, bandwidth, off-axis dispersion, or radial curvature;
- it does not prove that two independently constructed kernels have the same centered part;
- a full reconciliation must derive the missing non-scalar operator, not merely add a diagonal constant.

The strongest unresolved number is therefore not the scalar gap between \(-2.8579\) and \(-0.7751\). It is the planar mixed-gradient coefficient \(C^{(4)}\).

