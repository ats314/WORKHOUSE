# Canonical Folded Theory — 20 August 2026

## Nested-Quotient Temporal-Circuit–Hodge Gauge Spectral Theory with Scalar-Gauge Separation

### Canonical status

The strongest defensible project-wide theory is a theory of **physical temporal histories, quotient protection, scalar-gauge separation, and dispersive escape**. It supersedes the older interpretation in which a static cellular circuit or a single raw fourth-order scalar was treated as the decisive object.

The governing hierarchy is

\[
\boxed{
\text{physical degenerate sector}
\to
\text{ordered temporal histories}
\to
\text{Haar/Gram quotient}
\to
\text{electric resolvents}
\to
\text{folded/rooted assembly}
\to
\text{scalar/shape separation}
\to
\text{dispersive spectrum}.
}
\]

The theory is finite-order lattice spectral theory. It is not a continuum Yang–Mills mass-gap proof.

---

## 1. Physical retained space comes first

Let

\[
H=H_0+uV,
\qquad
u=\frac{\beta}{6}=\frac1{g_H^4}.
\]

For a chosen excitation, first select the **actual degenerate gauge-invariant eigenspace** of the electric Hamiltonian,

\[
P_E,
\qquad
Q_E=I-P_E.
\]

Only after this physical selection should one apply cellular or Hodge compression.

This ordering is essential. On the isotropic pentagonal prism,

\[
E_{\rm cap}=\frac{10}{3},
\qquad
E_{\rm side}=\frac83,
\]

so cap and side one-face states are not one degenerate physical band. The isotropic physical one-face problem is the cap band. A cap-plus-side Hodge model is a distinct, tuned Hamiltonian problem.

---

## 2. The fundamental dynamical object is an ordered history

An order-\(r\) history is

\[
h=(f_1,\sigma_1;\ldots;f_r,\sigma_r),
\]

with intermediate flux sequence

\[
q_0\to q_1\to\cdots\to q_r.
\]

After Gram-null quotienting, its direct Feshbach weight is schematically

\[
\mathcal A_N[h]
=
\langle q_{\rm out}|
V R_{r-1}V\cdots R_2VR_1V
|q_{\rm in}\rangle,
\]

where the reduced resolvents act on the physical representation quotient.

The full order-\(r\) operator is

\[
\boxed{
H_{\rm eff}^{(r)}
=
\sum_{[h]\in\mathscr H_r^{\rm phys}}
\mathcal A_N[h]T_h
+F_r,
}
\]

with \(F_r\) containing energy-dependent folds and the final result subjected to support-resolved linked/rooted subtraction.

If

\[
\pi(h)=\sum_j\sigma_j e_{f_j}
\]

forgets temporal ordering, then in general

\[
\boxed{
\mathcal A_N[h]\not\equiv \mathcal A_N[\pi(h)].
}
\]

Equal static support does not imply equal dynamics because the intermediate representations and denominators can differ.

---

## 3. Scalar gauge and the physical shape quotient

At any order write

\[
H_r=s_rI+K_r.
\]

The physically shape-sensitive datum is the scalar equivalence class

\[
\boxed{
[H_r]\in \operatorname{End}(P_E)/\mathbb RI.
}
\]

A simultaneous shift

\[
H_r\mapsto H_r+\delta I,
\qquad
s_r\mapsto s_r+\delta
\]

leaves

\[
K_r=H_r-s_rI
\]

unchanged.

For a Hodge/cube-boundary sector with \(\mathsf C=\partial_3\), define

\[
\boxed{
\mathcal K_r
=\mathsf C^\dagger(H_r-s_rI)\mathsf C.
}
\]

This operator is invariant under scalar re-anchoring. Therefore scalar shifts cannot change its eigenvectors, momentum dependence, bandwidth, or sum-of-squares coefficients.

This yields the key separation

\[
\boxed{
\text{scalar/rest coordinate}
\neq
\text{centered shape operator}
\neq
\text{physical dispersion}.
}
\]

---

## 4. Correct definition of first dispersive order

For a finite retained band, traceless compression

\[
\mathfrak M_P(A)
=
PAP-
\frac{\operatorname{tr}_P(PAP)}{\dim P}P
\]

detects non-scalar action, but a momentum-independent onsite splitting can be non-scalar without producing transport.

The invariant definition is therefore

\[
\boxed{
r_{\rm disp}
=
\min\left\{
r:
\operatorname{Spec}
\bigl(P(k)H_{\rm eff}^{(r)}(k)P(k)\bigr)
\text{ depends on }k
\right\}.
}
\]

On a one-band Hodge fiber, this reduces to the older non-scalar compression criterion. In general it is stricter.

---

## 5. Exact cubic protection through third order

For the \(SU(3)\), \(C=-\), one-plaquette cubic sector,

\[
\boxed{
H_{\mathrm{eff},-}(k,u)
=
E_{\rm flat}(u)I+t(u)B(k)B(k)^\dagger+O(u^4),
}
\]

with

\[
E_{\rm flat}(u)
=
\frac83+u+\frac{11}{306}u^2
-\frac{109151}{249696}u^3,
\]

\[
t(u)
=
\frac5{612}u^2
+\frac{1975}{124848}u^3.
\]

Since

\[
B^\dagger\partial_3=0,
\]

all cube-boundary states are exactly flat through \(O(u^3)\):

\[
\boxed{
r_{\rm disp}^{\rm cubic}\ge4.}
\]

---

## 6. Cubic fourth order: what is actually closed

### 6.1 Axial mobility is closed

The elementary-cube localization theorem gives

\[
K_{\rm r2}^{(4)}
=x_NT+c_N^\square H_\square,
\]

with

\[
T=(2q-16)I+2H_\square+(8-q)\widetilde N\widetilde N^\dagger.
\]

The boundary-exact term annihilates the flat fiber, and exact cube temporal amplitudes give

\[
\boxed{
c_N^\square
=-\frac{160}{N(N^2-1)^3},
\qquad
\alpha_N
=\frac{640}{N(N^2-1)^3}
\quad(N\ge3).
}
\]

For \(SU(3)\),

\[
\boxed{\alpha_3=\frac5{12}.}
\]

The microscopic shape gate also closes

\[
\boxed{B_N^{\rm shp}=D_N^{\rm shp}=0}
\]

for the certified ranks, with independent symbolic support for the axial law.

### 6.2 Historical exact centered SOS

For the packaged historical \(SU(3)\) 189-record kernel,

\[
q_{\rm band}^{(4)}
=-\frac{20721577909065127111}
{7250590288602460800}
=-2.857915988114559\ldots
\]

and

\[
\boxed{
\mathsf C^\dagger
\left(H_4-q_{\rm band}^{(4)}I\right)
\mathsf C
=
\frac5{48}\sum_iL_i^2
+
\frac{17607806155349}{1101327605164800}
\sum_{i<j}L_iL_j.
}
\]

Both coefficients are positive, so this historical centered operator is an exact local sum of squares.

This is an exact theorem **for that packaged historical kernel**. It is not by itself proof that the same mixed-gradient coefficient belongs to the final linked physical \(U4\) kernel.

---

## 7. Fourth-order scalar reconciliation

The linked/rooted calculation gives the numerical \(\Gamma\)-point coefficient

\[
\boxed{
m_\Gamma^{(4)}=-0.7751458630189173.}
\]

Hamer's convention obeys

\[
m(u)=\frac12M_A(2u),
\qquad
m_n=2^{n-1}a_n,
\]

so the published decimal \(a_4=-0.0968932328773\) maps to

\[
8a_4=-0.7751458630184,
\]

agreeing with the linked result to about \(5\times10^{-13}\).

The historical band anchor and the linked mass coordinate differ by

\[
\boxed{
\Delta_\Gamma
=m_\Gamma^{(4)}-q_{\rm band}^{(4)}
=2.0827701250956417\ldots .
}
\]

Thus one may define

\[
H_{4,\rm reanch}
=H_{4,\rm band}+\Delta_\Gamma I,
\]

for which

\[
\boxed{
H_{4,\rm reanch}-m_\Gamma^{(4)}I
=
H_{4,\rm band}-q_{\rm band}^{(4)}I.
}
\]

This is a valid scalar-coordinate reconciliation. It means the two numbers should not be treated as competing values of the same unqualified object.

It does **not** establish equality of the two full fourth-order kernels.

---

## 8. The remaining cubic \(U4\) dispute is off-axis shape

The historical exact shape coordinate is

\[
C_{\rm shp,old}
=-0.04808638318135875\ldots,
\]

while the newest folded numerical extraction gives

\[
C_{\rm shp,new}
=-0.020213328886166577.
\]

Hence

\[
\boxed{
\Delta_C
=0.027873054295192174\ldots>0.
}
\]

Under the common observed tier

\[
A_{\rm shp}=\frac5{48},
\qquad
B_{\rm shp}=D_{\rm shp}=0,
\]

this becomes

\[
\Delta\alpha=0,
\qquad
\Delta\beta=16\Delta_C
=0.4459688687230748\ldots,
\]

and therefore

\[
\boxed{
\mathcal K_{4,\rm new}
-
\mathcal K_{4,\rm old}
=
4\Delta_C
\sum_{i<j}L_iL_j.
}
\]

The candidate new branch is thus the historical SOS plus a positive mixed-gradient ray.

The two branches agree, after scalar alignment, at \(\Gamma\) and on axial cuts where the mixed invariant vanishes, but differ at \(M\), \(R\), and generic off-axis momentum.

Therefore the current cubic status is

\[
\boxed{
\text{scalar reconciliation: achieved;}\qquad
\alpha/B/D\text{ mobility gate: closed;}\qquad
\text{complete off-axis }C/\beta\text{ coefficient: unresolved.}
}
\]

---

## 9. Fixed scalar gauge is not a coupling redefinition

A fixed-coordinate fourth-order scalar shift

\[
H_4\mapsto H_4+\delta I
\]

does not force any change in \(H_5,H_6,H_7,\ldots\).

Only if one deliberately changes the coupling coordinate, for example

\[
\boxed{
u_{\rm band}=u_{\rm mass}+\delta u_{\rm mass}^4,}
\]

with no additional fifth-, sixth-, or seventh-order terms, do the higher coefficients transform:

\[
\widetilde H_4=H_4+\delta I,
\]

\[
\widetilde H_5=H_5+2\delta H_2,
\]

\[
\widetilde H_6=H_6+3\delta H_3,
\]

\[
\widetilde H_7=H_7+4\delta H_4.
\]

This distinction is mandatory for any \(M5\)–\(M7\) calculation. The scalar re-anchoring \(\Delta_\Gamma\) must **not** be propagated into higher orders unless a coupling-coordinate change is explicitly declared.

---

## 10. Pentagonal prism: exact counterexample to static-circuit equality

The primitive integral pentagonal cell relation has weight seven, so the square-free cell-completion subchannel occurs at five insertions and has

\[
\boxed{
c_{5,\rm prim}(N)
=\frac{1120}{N(N^2-1)^4},
\qquad
c_{5,\rm prim}^{SU(3)}=\frac{35}{384}.}
\]

But the isotropic physical cap band already hops at fourth order.

Two independent exact microscopic backends give

\[
\boxed{
h_4^{\rm side}
=-\frac{2861009}{84387303000},}
\]

and summing the five equivalent side supports gives

\[
\boxed{
\tau_4
=-\frac{2861009}{16877460600}.}
\]

No offsite cap transfer occurs at orders one through three, and at fourth order

\[
\boxed{
H_{\rm eff,cap}^{(4),\rm conn}
=u^4\tau_4\sum_z
\left(|a_z,-\rangle\langle a_{z+1},-|+\mathrm{h.c.}\right),
}
\]

so

\[
\boxed{
\Delta E_{\rm cap}^{(4)}(k)
=-\frac{2861009}{8438730300}u^4\cos k,
\qquad
r_{\rm disp}^{\rm iso,cap}=4.
}
\]

Thus

\[
\boxed{
r_{\rm physical}\neq w_{\min}-2}
\]

in general. The older weighted-circuit rule remains a lower-bound/completion statement for the restricted reduced integral circuit class, not a universal equality for physical hopping.

The reason is temporal: repeated/conjugate insertions can cancel in the final static chain while still changing the intermediate resolvent sequence.

---

## 11. Finite-rank representation dressing remains independent

At fifth order in the pentagonal \(SU(3)\) local census,

\[
14^5=537824
\to
1030
=120_{\mathbb Z}+910_{\mathbb Z_3\setminus\mathbb Z}.
\]

The 910 modular histories collapse to 14 oriented-face lifts and then to

\[
910=338_{\rm direct}+572_{\rm return/fold}.
\]

The representation-resolved direct calculation gives a nonzero triple-side determinant correction

\[
\boxed{
\delta c_{5,\det}^{SU(3)}
=
\frac{235424477177}{407461473619200}
\approx5.777834\times10^{-4},
}
\]

so the direct fifth-order coefficient becomes

\[
\boxed{
c_{5,\rm direct}^{SU(3)}
=0.0917236167372\ldots .
}
\]

This proves that raw center/Haar cancellation cannot be applied before electric resolvents.

The complete fifth-order coefficient remains open because the 572 proper-return histories still require the full support-resolved fifth-order Feshbach fold and rooted linked-cluster assembly.

---

## 12. What survives from the primitive cell law

For the explicitly restricted square-free simple-loop completion subchannel,

\[
\boxed{
c_{r,\rm prim}(N)
=
\frac{S_r}{N^rC_F^{r-1}}
=
\frac{2^{r-1}S_r}{N(N^2-1)^{r-1}},
\qquad
C_F=\frac{N^2-1}{2N}.
}
\]

Hence

\[
\boxed{c_{r,\rm prim}(N)\sim N^{-(2r-1)}.}
\]

The certified sequence includes the tetrahedron \(r=2\), triangular prism \(r=3\), cube \(r=4\), and primitive pentagonal prism \(r=5\).

The correct interpretation is now:

\[
\boxed{
\text{primitive completion order determines a distinguished cellular channel,}
\text{ not necessarily the leading physical transfer order.}
}
\]

---

## 13. Hodge protection remains an exact special case

Whenever an effective correction has the form

\[
cI+B^\dagger X B,
\]

its restriction to \(\ker B\) is scalar. This is the exact reason lower-order cubic and prism terms can be flat.

The cube theorem further shows that nontrivial microscopic tree processes can combine into a boundary-exact operator plus a single cell-completion residue. Thus Hodge structure remains a powerful **quotient theorem**, but not a universal substitute for the energy-decorated temporal history graph.

---

## 14. Same-source bridge to the physical glueball channel

The gauge-invariant source

\[
\boxed{B_i^-(x)=\operatorname{ImTr}U_{jk}(x)}
\]

creates the one-plaquette \(C=-\) state at strong coupling and has weak-field tangent

\[
\boxed{
B_i^-
=-\frac16\operatorname{Tr}X^3
+\frac1{120}\operatorname{Tr}X^5+\cdots .
}
\]

Thus the spatial Hodge/temporal-circuit state and the odd local Weyl \(P_3\) oscillator are two asymptotic descriptions of the spectral measure of the same gauge-invariant operator.

At finite volume, the corresponding strong-coupling pole has nonzero overlap locally in coupling. Continuation to the physical/continuum glueball remains open.

---

## 15. Canonical master principle

> **Nested-Quotient Temporal-Circuit–Hodge Spectral Principle.** For a Kogut–Susskind lattice gauge Hamiltonian, first select the actual degenerate gauge-invariant eigenspace of the electric Hamiltonian. Perturbative transfer inside that sector is generated by ordered magnetic histories in the Gram-quotiented Feshbach state graph. Their amplitudes depend on exact Haar/Peter–Weyl contraction data and representation-dependent electric resolvents, while proper retained-space returns enter through support-resolved folded terms and rooted linked subtraction. Scalar coordinates are defined only modulo the identity, and physical shape belongs to the quotient \(\operatorname{End}(P_E)/\mathbb RI\). Hodge/boundary ideals can protect a sector by annihilating the centered operator, but physical dispersion begins only when the fully assembled retained-space spectrum becomes momentum dependent. Primitive cell completions give distinguished cellular channels with \(N^{-(2r-1)}\) scaling, yet temporally nontrivial histories with statically cancelling support can produce earlier transfer. Finite-rank determinant sectors provide an additional representation-theoretic dressing and cannot be eliminated before resolvent evaluation.

---

## 16. Current claim ledger

| Claim | Status |
|---|---|
| Cubic flatness through \(O(u^3)\) | Exact theorem |
| Cubic \(\alpha_N=640/[N(N^2-1)^3]\) | Exact symbolic/certified mobility law |
| Cubic \(B_N^{\rm shp}=D_N^{\rm shp}=0\) | Closed shape gate in certified scope |
| Historical \(SU(3)\) fourth-order SOS | Exact for historical 189-record kernel |
| Historical \(q_{\rm band}^{(4)}\) | Exact band-kernel anchor |
| \(m_\Gamma^{(4)}=-0.7751458630189173\) | Strong numerical linked result, independently normalized to Hamer |
| Scalar re-anchoring \(q_{\rm band}\leftrightarrow m_\Gamma\) | Exact algebraic crosswalk |
| Complete physical cubic off-axis \(C/\beta\) | Open |
| Pentagonal isotropic cap hop at \(O(u^4)\) | Exact dual-cold theorem |
| Primitive pentagonal \(O(u^5)\) completion | Exact restricted-channel result |
| Pentagonal fifth-order direct determinant correction | Exact direct-sector result |
| Full pentagonal fifth-order folded/rooted coefficient | Open |
| General shortest-temporal-history classification | Open theorem problem |
| Continuum \(T_1^{+-}\) mass prediction | Open |
| Yang–Mills mass-gap proof | Not claimed |

---

## 17. Decisive next calculations

1. **Direct linked off-axis cubic \(U4\) calculation.** Compute \(X,M,R\) without fitting either branch. This decides the physical mixed-gradient coefficient immediately.
2. **Exact marked-cluster \(m_4\) sweep.** This would promote the strongly corroborated \(\Gamma\)-coefficient from numerical reconstruction to a fully exact internal certificate.
3. **Complete pentagonal fifth-order fold/rooted assembly.** The remaining 572 return histories are the exact finite task.
4. **Shortest physical temporal-history classifier.** Replace raw word enumeration by an energy-decorated incidence/Feshbach graph theorem.
5. **Keep M5–M7 coordinate-clean.** Do not propagate \(\Delta_\Gamma\) into higher orders unless a nonlinear coupling-coordinate transformation is explicitly chosen.

---

## Final status sentence

\[
\boxed{
\textbf{The project has an exact theory of lower-order Hodge protection and axial fourth-order mobility,}
\atop
\textbf{a strong scalar reconciliation of the cubic }m_4\textbf{ coefficient, and an exact temporal-history counterexample to static-circuit equality.}
}
\]

The remaining cubic fourth-order problem is sharply localized: **determine the physical off-axis mixed-gradient coefficient**. The remaining pentagonal fifth-order problem is also sharply localized: **assemble the 572 return histories with the full support-resolved fold/rooted formula**.
