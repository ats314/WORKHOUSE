# Cellular-circuit protection and the first mobility of lattice flux composites

**Research note — 19 August 2026**  
**Status:** theorem formulation plus exact CPU certificate; not a universality or continuum-limit claim.

## Abstract

Consider the cellular chain complex

\[
C_3 \xrightarrow{B_3} C_2 \xrightarrow{B_2} C_1,
\qquad B_2B_3=0,
\]

with a degenerate excitation space indexed by oriented two-cells. An order-\(r\) magnetic process connecting two such excitations produces a signed dependence involving the two endpoint columns of \(B_2\) and at most \(r\) inserted columns. Consequently, a reduced connected process cannot occur before the smallest relevant signed circuit of the boundary matrix can be completed. For regular cell boundaries with \(F\) unit-incidence faces, this gives the lower bound \(r\ge F-2\). Equality produces mobility only when the local Haar–Casimir amplitude is nonzero and the induced cell operator is non-scalar after compression to the cycle sector.

For the triangular-prism complex used in the project, this mechanism is exact. The complete second-order shape operator is scalar on \(\ker B_\square\), whereas the order-three prism-completion operator is non-scalar. Its compression has the exact dual-honeycomb bands

\[
\mu_\pm(k)=-1\pm\left|1+e^{ik_x}+e^{ik_y}\right|,
\]

together with two flat harmonic modes at \(\mu=2\). Multiplication by the exact local coefficient

\[
c_3(N)=\frac{64}{N(N^2-1)^2}
\]

gives an SU(3) third-order bandwidth of \(2\) in the project normalization. The analogous periodic-cube sector gives a cosine band \(2\cos k_z\) at order four. Its SU(3) coefficient \(c_4^\square=-5/48\) yields the previously recorded \(\alpha_3=4|c_4^\square|=5/12\). A tetrahedral test gives the predicted topological order two and a non-scalar geometric compression, while its local gauge-theory coefficient remains to be calculated.

The resulting factorization is

\[
\boxed{
\text{first allowed support from cellular circuits}
\quad\times\quad
\text{local Haar–Casimir weight}
\quad\times\quad
\text{non-scalar cycle compression}
}
\]

and not any particular large Krylov or Q-space computation.

---

## 1. Operator and chain-complex setup

Let \(X\) be a finite oriented cellular complex. Write \(e_f\) for the basis vector of an oriented face \(f\in X_2\), and

\[
b_f=B_2e_f\in C_1(X)
\]

for its oriented link boundary. The degenerate shape space is a selected subspace of \(C_2(X)\), such as the vertical-square space in the triangular-prism construction or the parallel-\(xy\) plaquette space in the cubic construction.

Let

\[
Z=\ker B
\]

denote the cycle space of the boundary map restricted to that selected face space, and let \(P_Z\) be its orthogonal projector. The term *cycle sector* is used deliberately. In standard combinatorial Hodge terminology the harmonic space requires both closedness and coclosedness:

\[
\mathcal H=\ker B\cap\ker D^\dagger,
\]

where \(D\) is the next boundary map whose image lies in the selected space. Thus \(\ker B\) generally contains both boundaries and harmonic representatives.

### 1.1 A precise flatness map

Rather than treating “boundary ideal” as an undefined algebraic ideal, define the traceless cycle compression

\[
\mathfrak M_Z(A)
=P_ZAP_Z-
\frac{\operatorname{tr}(P_ZAP_Z)}{\dim Z}P_Z.
\]

Then:

* \(A\) is shape-flat on \(Z\) exactly when \(\mathfrak M_Z(A)=0\);
* every scalar is killed by \(\mathfrak M_Z\);
* every operator \(B^\dagger X B\) is killed because \(BP_Z=0\).

The first mobility order is therefore defined without ambiguity by

\[
r_{\mathrm{mob}}
=\min\left\{r:\mathfrak M_Z\!\left(H_{\mathrm{eff}}^{(r)}\right)\ne0\right\}.
\]

The linear subspace annihilated by this compression is the correct object behind the project’s “boundary-generated” language.

---

## 2. Circuit lower bound

An order-\(r\) magnetic history from an initial oriented face \(p\) to a final oriented face \(q\) obeys stable-rank flux balance of the form

\[
b_p+\sum_{j=1}^{r}\sigma_j b_{f_j}-\tau b_q=0,
\qquad \sigma_j,\tau\in\{\pm1\}.
\]

Equivalently,

\[
B_2x=0,
\qquad
x=e_p+\sum_{j=1}^{r}\sigma_je_{f_j}-\tau e_q.
\]

Opposite repeated actions and vacuum-disconnected pieces must first be removed. A history remaining after this reduction gives a nonzero integer dependency among columns of \(B_2\).

### Theorem 1 — weighted cellular-circuit bound

Let \(w_{\min}\) be the minimum \(\ell_1\) weight of a primitive nontrivial integer dependency of \(B_2\) that is compatible with the selected endpoint sector. Then every reduced connected order-\(r\) process satisfies

\[
r\ge w_{\min}-2.
\]

If a minimizing dependency has coefficients \(\pm1\), if two of its columns can be chosen as the endpoints, and if the corresponding local representation-theory amplitude is nonzero, then the bound is attained at the support level.

#### Proof

The reduced history supplies a nonzero \(x\in\ker_{\mathbb Z}B_2\). Each endpoint contributes one unit to \(\lVert x\rVert_1\), while the \(r\) insertions contribute at most \(r\) further units after cancellation. Hence

\[
w_{\min}\le \lVert x\rVert_1\le r+2,
\]

which gives \(r\ge w_{\min}-2\). If a primitive dependency of weight \(w_{\min}\) has unit coefficients, selecting two entries as endpoints leaves exactly \(w_{\min}-2\) unit insertions. This realizes the balanced support. Whether it contributes to \(H_{\mathrm{eff}}\), and whether its compression is non-scalar, are separate dynamical questions. ∎

### Corollary 1 — regular \(F\)-face cell

Suppose the boundary of a regular three-cell is a minimal signed circuit containing \(F\) faces, all with incidence coefficient \(\pm1\), and no smaller physically relevant circuit exists. Then

\[
r_{\mathrm{allowed}}=F-2.
\]

This is the precise domain of the project’s \(F-2\) rule. For a general cellular boundary matrix the weighted circuit length, not the bare face count, is the invariant.

### 2.1 Physical survival conditions

Circuit completion is necessary but not sufficient for mobility. Equality with \(r_{\mathrm{mob}}\) additionally requires:

1. **Haar survival:** the local group integral is nonzero;
2. **resolvent survival:** allowed intermediate representation channels have finite denominators and do not cancel;
3. **linked survival:** vacuum-disconnected and folded pieces are removed consistently;
4. **symmetry survival:** charge conjugation, parity, and other sector projections do not kill the process;
5. **compression survival:** the assembled operator has \(\mathfrak M_Z(A)\ne0\).

The circuit theorem determines when motion becomes possible. Representation theory determines whether the possible process actually occurs.

### 2.2 Finite-\(N\) modular relations

Center balance weakens integral balance to a congruence,

\[
B_2x=0\pmod N.
\]

These are weighted modular circuits and can appear earlier than stable-rank circuits. They are not automatically physical matrix elements. The prism artifacts explicitly classify the additional SU(3), SU(4), and SU(5) candidates. In the SU(3) prism case, the extra families are diagonal, reduce to the already-flat shared-edge class, or vanish by charge parity and factorization. This explains why the integral five-face circuit still controls the first non-scalar term there.

---

## 3. All-volume prism algebra

Let \(K\) be the periodic triangulation of \(T^2\) used in the attached prism notebooks, and let \(Z_L\) be a length-\(L\) periodic one-complex. Write

\[
D_1:C_1(K)\to C_0(K),
\qquad
D_2:C_2(K)\to C_1(K),
\qquad
\partial_z:C_1(Z_L)\to C_0(Z_L).
\]

The vertical-square space is \(C_1(K)\otimes C_1(Z_L)\). Up to the project’s orientation convention, its restricted boundary is

\[
B_\square=
\begin{pmatrix}
-I\otimes\partial_z\\
D_1\otimes I
\end{pmatrix}.
\]

Because \(\ker\partial_z=\operatorname{span}\{\mathbf1_z\}\), one obtains for every stable periodic size

\[
\boxed{
\ker B_\square
\cong
\ker D_1\otimes\operatorname{span}\{\mathbf1_z\}
}.
\]

For the regular \(L\times L\) triangulation,

\[
\dim\ker B_\square=2L^2+1,
\]

matching the \(L=3,4,5\) notebook checks.

### Proposition 2 — exact second-order cycle flatness

Let \(S_\square\) be the signed shared-edge square adjacency. Each square has four boundary edges, so

\[
S_\square+4I=B_\square^\dagger B_\square.
\]

The nontrivial physical assertion in the attached second-order certificate is that the complete support-changing kernel assembles as

\[
H_{\mathrm{shape}}^{(2)}=a_2I+t_NS_\square,
\]

where the same local fusion coefficient multiplies every surviving shared-edge pair. Therefore

\[
P_ZH_{\mathrm{shape}}^{(2)}P_Z=(a_2-4t_N)P_Z,
\]

and

\[
\mathfrak M_Z\!\left(H_{\mathrm{shape}}^{(2)}\right)=0.
\]

The identity by itself is incidence algebra; the physics is the exhaustive reduction of the physical second-order processes to this single adjacency class.

### Proposition 3 — third-order prism escape

Each triangular prism has three vertical-square faces. If their oriented cell-boundary signs are \(s_i\), the square-to-square cell operator assigns

\[
(H_{\mathrm{cell}})_{ij}=-s_is_j,
\qquad i\ne j.
\]

Each base edge belongs to two base triangles. Direct assembly gives the all-volume product identity

\[
\boxed{
H_{\mathrm{cell}}
=\left(2I-D_2D_2^\dagger\right)\otimes I_z
}.
\]

The Hodge decomposition of the base cycle space is

\[
\ker D_1=\operatorname{im}D_2\oplus\mathcal H_1(T^2).
\]

Consequently:

* on \(\mathcal H_1(T^2)\), \(D_2^\dagger h=0\) and \(H_{\mathrm{cell}}h=2h\);
* on \(\operatorname{im}D_2\), the operator has the nonzero upper-Laplacian spectrum and is non-scalar.

Thus the order-three cell term mobilizes boundary cycles while the two harmonic representatives remain flat under this term. This is more precise than saying that the entire “Hodge sector” disperses.

### 3.1 Exact dual-honeycomb bands

The dual graph of the regular triangular tiling is honeycomb. On triangle chains,

\[
D_2^\dagger D_2=3I-A_{\mathrm{hex}}.
\]

With

\[
f(k)=1+e^{ik_x}+e^{ik_y},
\]

the two dual-Laplacian bands are

\[
\lambda_\pm(k)=3\pm|f(k)|.
\]

The nonzero spectra of \(D_2D_2^\dagger\) and \(D_2^\dagger D_2\) agree, giving the boundary-cycle cell bands

\[
\boxed{
\mu_\pm(k)=-1\mp|f(k)|
}.
\]

The sign label can be exchanged, so equivalently \(\mu_\pm=-1\pm|f|\). The single \(k=0\) zero-boundary triangle mode is omitted; the two harmonic edge modes occur separately at \(\mu=2\). At honeycomb \(K\) points, \(f(k)=0\), so the dispersive bands meet at \(\mu=-1\).

The geometric spectrum ranges from \(-4\) to \(2\), explaining the notebook’s exact spread \(6\).

### 3.2 SU(\(N\)) amplitude and bandwidth

The attached temporal-history/Haar calculation gives

\[
c_3(N)=\frac{64}{N(N^2-1)^2}.
\]

For SU(3),

\[
c_3(3)=\frac13.
\]

Ignoring the independent scalar rest shift, the order-three shape bands are

\[
\delta E_\pm^{(3)}(k)
=u^3c_3(N)\left[-1\pm|f(k)|\right],
\]

in the project convention. Their bandwidth is

\[
\Delta_3(N)=6c_3(N)
=\frac{384}{N(N^2-1)^2},
\qquad
\Delta_3(3)=2.
\]

This is an immediate quantitative prediction extracted from the previously reported non-scalar spread.

---

## 4. Cubic cell: order four becomes a cosine band

A cube boundary is a primitive six-face circuit. Selecting its two opposite \(xy\) faces as endpoints requires the other four faces as insertions, so the circuit theorem gives

\[
r_{\mathrm{allowed}}=6-2=4.
\]

On a periodic cubic \(T^3_L\), restrict to the parallel-\(xy\) face sector. Its cycle space has one uniform closed \(xy\) sheet for every \(z\) layer:

\[
\dim\ker B_{xy}=L.
\]

The cube-completion operator connects the bottom and top \(xy\) face of each cube. Exact compression to the layer-cycle basis gives

\[
\boxed{
P_ZH_{\mathrm{cube}}P_Z=A(C_L)
}

\]

under the normalized identification, where \(A(C_L)\) is the adjacency matrix of the periodic one-dimensional cycle. Hence

\[
\mu(k_z)=2\cos k_z,
\qquad
\operatorname{width}(H_{\mathrm{cube}})=4.
\]

The attached exact local coefficient is

\[
c_4^\square(N)
=-\frac{160}{N(N^2-1)^3},
\qquad
c_4^\square(3)=-\frac5{48}.
\]

Therefore the SU(3) cubic band width is

\[
4\left|c_4^\square(3)\right|
=\frac5{12}.
\]

This reproduces and explains the previously recorded relation

\[
\boxed{\alpha_3=-4c_4^\square(3)=\frac5{12}}.
\]

The factor four is the exact width of the compressed nearest-neighbor cosine band, not an arbitrary numerical multiplier.

---

## 5. Tetrahedral prediction and open local coefficient

A tetrahedron boundary is a primitive four-face circuit, so

\[
r_{\mathrm{allowed}}=4-2=2.
\]

The accompanying CPU certificate constructs two oppositely glued tetrahedra. Its two-dimensional cycle space equals the range of the two cell boundaries. The oriented pair-completion operator has generalized compressed eigenvalues

\[
-\frac{18}{5},\qquad -2,
\]

and exact spread

\[
\frac85.
\]

Thus the geometric order-two cell operator is non-scalar. The project artifacts do not yet contain the corresponding local SU(\(N\)) Haar–resolvent coefficient. The theorem therefore predicts the first *allowed* tetrahedral mobility order but does not yet assert a nonzero gauge-theory hopping amplitude.

A tetrahedral local calculation is the cheapest high-value falsification test of the mechanism: if symmetry or representation theory kills this coefficient, the result will cleanly demonstrate the distinction between circuit allowance and physical survival.

---

## 6. Exact CPU certificate

The companion program `hodge_circuit_mobility_certificate.py` uses no GPU, network, Wilson-network census, or Q-space construction. It performs:

* exact rational ranks and nullspaces with an internal fraction-based RREF;
* exact checks of \(B_2B_3=0\);
* exact enumeration of minimal local column circuits;
* exact cycle-basis membership;
* exact scalar versus non-scalar compression tests;
* numerical diagonalization only after the exact tests;
* Fourier-spectrum regressions for the prism and cube.

Its reference run passes **26/26 gates** and yields:

| Cell | Faces \(F\) | Circuit order \(F-2\) | Exact geometric compression |
|---|---:|---:|---|
| Tetrahedron | 4 | 2 | eigenvalues \(-18/5,-2\); spread \(8/5\) |
| Triangular prism | 5 | 3 | honeycomb bands plus two harmonic modes; spread \(6\) |
| Cube | 6 | 4 | \(2\cos k_z\); spread \(4\) |

The program intentionally prints the following evidence boundary:

1. circuit girth proves the first order at which connected cell completion is topologically allowed;
2. non-scalar compression proves the geometric operator can generate mobility;
3. actual gauge-theory mobility additionally requires a nonzero local representation-theory coefficient;
4. that coefficient is closed in the attached work for the prism and cube, but not yet for the tetrahedron.

---

## 7. What is established and what remains conditional

### Established within the attached artifacts and this certificate

* exact chain-complex identities for the tested geometries;
* the second-order prism incidence form and flat cycle compression;
* exhaustive stable-rank order-two prism support at the tested stable volume;
* exhaustive order-three prism endpoint completion at the tested stable volume;
* the exact all-volume prism product operator;
* the exact prism honeycomb spectrum and harmonic/boundary decomposition;
* the exact prism coefficient \(64/[N(N^2-1)^2]\);
* the exact cubic opposite-face coefficient \(-160/[N(N^2-1)^3]\);
* the cubic cosine compression and \(\alpha_3=4|c_4^\square|\) relation;
* the general weighted-circuit lower bound.

### Not yet established

* a theorem that every lattice/cell family has \(r_{\mathrm{mob}}=F-2\);
* survival of the tetrahedral order-two local Haar–resolvent amplitude;
* a complete classification of weighted modular circuits for arbitrary \(N\);
* a symbolic-rational replacement for every floating physical-Q contraction;
* the missing fourth-order scalar mass and full shape coefficients;
* a controlled continuum glueball prediction.

The finite-volume prism enumerations should be replaced in a paper by a local-star classification lemma. The all-volume operator and spectral identities are already algebraic; only the completeness of the physical process classes needs this final formal step.

---

## 8. Recommended research sequence

1. **Compute the tetrahedral local coefficient.** This is CPU-small and directly tests whether circuit allowance implies physical survival in a new geometry.
2. **Promote the prism support census to a local proof.** Classify reduced two- and three-insertion dependencies within the radius-one face star, including modular SU(3) exceptions.
3. **Build a weighted modular-circuit classifier.** Its objective should be minimum insertion weight, not merely minimum distinct support.
4. **Write the paper around the circuit/compression theorem.** Put Haar–Fierz coefficients in the second layer and physical-Q quotient machinery in an implementation section or appendix.
5. **Defer further A100 Q2 production.** It does not strengthen the central mechanism until the theorem and the new-geometry falsification test are complete.

### Proposed lead claim

> In Hamiltonian lattice gauge theory, the first perturbative order at which a composite flux excitation can acquire shape dispersion is bounded by the minimum weighted cellular circuit connecting its endpoint faces. Incidence-generated operators are flat after cycle compression; mobility appears only when a circuit-completion operator has both a nonzero local Haar–Casimir weight and a non-scalar compressed action.

### Proposed short title

**Cellular-Circuit Protection of Glueball Mobility**

---

## 9. Audited source provenance

The claims above were checked against the following attached artifacts:

| Artifact | SHA-256 |
|---|---|
| `10-NB_HAAR_hodge_mixed_determinant_v05c.ipynb` | `2f12ef86ab494f675f144c56d5d7e4174af003e2fe0084dcd4e39f9f364eda48` |
| `11-NB_O2_prism_square_second_order_falsification.ipynb` | `0737d7922d4827ba7c31d781348d100d7507e62f86dabb1982e66f30696c60bb` |
| `15-NB_O3_prism_third_order_shape_closure_v2.ipynb` | `0a3649587c10af3fa051b2dba678fc0fdbce24b61bdbfc10508332d04dca1cd5` |
| `05-Hodge_Mass_String_NestedQ_Moment_v7_A100-1-.ipynb` | `03eb06cdde646ecb703d56c6059d0a651d0ee8cfa524173655b9ef1a5f169c33` |

The large physical-Q notebook supports the computational-engine claims and cubic string decomposition. It is not needed for the cellular-circuit proof.
