# A temporal Wilson–Hamiltonian matching step for WORKHOUSE

Date: 4 September 2026. Repository reference: `31255abac3829cb0cc1ce7c36c1852db8cdafbea`.

## Result and scope

This note advances the temporal-regulator part of G18/G19. It does not claim a spatial continuum limit or a volume-uniform Wilson carrier theorem.

There are three separate results:

1. An explicit positive Wilson transfer family has WORKHOUSE's canonical Hamiltonian as its **fixed finite spatial-volume, continuous-time limit**. This is a convention-explicit application of the established transfer-matrix/product-formula method, not a priority claim.
2. A direct Lie-algebra Laplace calculation gives the first temporal discretization correction at every fixed SU(N) irrep. That correction is universally proportional to the quadratic Casimir. A clock determined from the fundamental character removes it for every fixed irrep, not only the fundamental.
3. If a Wilson-band symbol is constructed and matched to the Hamiltonian symbol in the spatially weighted norm used in G18, the relative-gap lemma transfers that estimate to the entire punctured momentum zone. The required matched-band estimate remains an explicit hypothesis, not a consequence of the numerical tests below.

The older `RELATIVE_GAP_BRIDGE.md` is included unchanged as provenance. Its 12 checks were rerun. The new Weyl quadrature and truncated-plaquette calculation are in `wilson_clock.py`; they use no historical fourth-order kernel, C_shp value, or hopping target.

## 1. Freeze the normalization before comparing spectra

The basis is the manuscript's convention

\[
H(u)=H_E-uV,\qquad H_E=\frac12\sum_\ell C_2(\ell),\qquad
V=\sum_p(\chi_p+\overline\chi_p).
\]

Every spatial plaquette is counted once. Fundamental generators obey
\(\operatorname{tr}_F(T_aT_b)=\delta_{ab}/2\).

Let \(\beta_t,\beta_s\) denote the **actual coefficients multiplying**
\(W_p=1-\operatorname{ReTr}U_p/N\) on temporal and spatial plaquettes. They are not the \(\beta_N\) in the manuscript's electric-unit Hamiltonian.

Define the normalized one-link temporal Wilson density

\[
p_{\beta_t}(U)=Z(\beta_t)^{-1}
\exp\!\left[\frac{\beta_t}{N}\operatorname{ReTr}U\right].
\]

Its convolution operator is denoted \(C_{\beta_t}\). Peter–Weyl decomposition diagonalizes it: on irrep \(R\), it is the scalar

\[
\lambda_R(\beta_t)=\frac1{d_R}\int p_{\beta_t}(U)\overline{\chi_R(U)}\,dU.
\]

The conjugation convention is immaterial here because the density is invariant under inversion and \(\lambda_R=\lambda_{\bar R}\).

For an electric-unit time step \(\epsilon>0\), take

\[
\boxed{\beta_t=\frac{2N}{\epsilon},\qquad \beta_s=2Nu\epsilon.}
\tag{1}
\]

The corresponding symmetric transfer operator on a finite spatial lattice is

\[
T_\epsilon^W(u)
=e^{\epsilon uV/2}\left(\bigotimes_\ell C_{2N/\epsilon}\right)e^{\epsilon uV/2}.
\tag{2}
\]

Temporal gauge produces this kernel. Integrating the remaining temporal gauge variables inserts the gauge projector; equivalently, restrict (2) to the gauge-invariant Hilbert space. Gauge transformations, charge conjugation, and spatial electric one-form symmetries commute with the displayed factors, so this restriction and the neutral charge-odd restriction are consistent.

The expansion of
\(e^{\beta_t(\chi_F+\chi_{\bar F})/(2N)}\)
is a sum of tensor-product characters with nonnegative coefficients. Consequently \(C_{\beta_t}\) is a positive contraction. Every SU(N) irrep appears in tensor powers of the fundamental and its conjugate, so its multiplier is positive for \(\beta_t>0\). Sandwiching by the positive multiplication operator preserves positivity. The construction does not introduce negative transfer eigenvalues in order to improve the clock.

## 2. Fixed-volume continuous-time limit

**Proposition.** On any fixed finite spatial lattice and for fixed real \(u\),

\[
\operatorname*{s-lim}_{n\to\infty}
\left[T_{t/n}^{W}(u)\right]^n=e^{-tH(u)},\qquad t\ge0.
\tag{3}
\]

The same assertion holds in the reducing physical charge/flux sectors.

**Proof.** The character asymptotic proved in Section 3 begins with

\[
\lambda_R(2N/\epsilon)=1-\frac{C_R}{2}\epsilon+O_R(\epsilon^2).
\]

Hence \((C_{2N/\epsilon}-I)/\epsilon\to-C_2/2\) on each finite Peter–Weyl sum. For finitely many links, tensoring gives \(-H_E\). The finite Peter–Weyl algebra is a core for \(H_E\), and the bounded finite-volume potential preserves the required core/domain estimates. Differentiating the two multiplication factors in (2) adds \(+uV\), so the strong derivative of (2) on this core is \(-H\).

Also
\(\|T_\epsilon^W\|\le e^{\epsilon |u|\|V\|}\),
and \(H_E-uV\) is self-adjoint and bounded below on the electric domain. Multiplying by a scalar exponential reduces to the contraction version of the Chernoff product theorem, which gives (3). Commutation with the symmetry projectors gives sector descent.

The statement controls matrix elements of the semigroup between fixed Hilbert-space vectors. It does **not**, by itself, prove convergence of varying vacuum vectors or convergence of isolated excited projections. Those require additional spectral control. The extensive norm \(\|V\|\) has not been replaced by a volume-uniform local estimate.

The heat-kernel comparator is

\[
T_\epsilon^{HK}(u)=e^{\epsilon uV/2}e^{-\epsilon H_E}e^{\epsilon uV/2}.
\]

It has exactly the same limiting Hamiltonian. At nonzero \(\epsilon\), neither symmetric transfer is generally equal to \(e^{-\epsilon H}\): the magnetic and electric factors need not commute.

## 3. The first finite-time correction at all ranks

**Proposition.** For each fixed irrep \(R\) of SU(N), \(N\ge2\), as \(\epsilon\downarrow0\),

\[
\boxed{
\lambda_R(2N/\epsilon)
=1-\frac{C_R}{2}\epsilon
+\left(\frac{C_R^2}{8}-\frac{N^2-2}{16N}C_R\right)\epsilon^2
+O_R(\epsilon^3).
}
\tag{4}
\]

Equivalently,

\[
-\frac1\epsilon\log\lambda_R
=\frac{C_R}{2}+\frac{N^2-2}{16N}C_R\epsilon+O_R(\epsilon^2).
\tag{5}
\]

The remainder is at fixed irrep and fixed rank. No estimate uniform over the unbounded electric Hilbert space is asserted.

### Derivation

Use exponential coordinates \(U=e^{i\sqrt\epsilon Y}\), where \(Y=y_aT_a\), and put \(D=N^2-1\). Identity is the unique maximum of \(\operatorname{ReTr}U\). Ordinary Laplace localization on the compact group therefore reduces the expansion to a neighborhood of identity; the complementary integral is exponentially small relative to its peak.

The Wilson factor expands as

\[
\frac{2}{\epsilon}\operatorname{ReTr}e^{i\sqrt\epsilon Y}
=\frac{2N}{\epsilon}-\operatorname{Tr}Y^2
+\frac\epsilon{12}\operatorname{Tr}Y^4+O(\epsilon^2|y|^6).
\]

Since \(\operatorname{Tr}Y^2=|y|^2/2\), the leading measure is a standard \(D\)-dimensional Gaussian. The exponential-coordinate Haar Jacobian satisfies

\[
J(\sqrt\epsilon y)=1-\frac{N\epsilon}{24}|y|^2+O(\epsilon^2|y|^4).
\]

For example, on a Cartan subalgebra it is the product of
\(\left[\sin((x_i-x_j)/2)/((x_i-x_j)/2)\right]^2\), and
\(\sum_{i<j}(x_i-x_j)^2=N\operatorname{Tr}X^2\)
gives the coefficient. Thus the first normalized-density correction is the covariance with

\[
D_1(Y)=\frac1{12}\operatorname{Tr}_F Y^4-\frac N{24}|y|^2.
\]

The irrep character contributes

\[
\frac{\operatorname{Re}\chi_R(e^{i\sqrt\epsilon Y})}{d_R}
=1-\frac\epsilon{2d_R}\operatorname{Tr}_R Y_R^2
+\frac{\epsilon^2}{24d_R}\operatorname{Tr}_R Y_R^4+O_R(\epsilon^3|y|^6).
\]

Odd terms integrate to zero under inversion. The trace identities

\[
\sum_a T_aT_a=C_RI,\qquad
\sum_aT_aT_bT_a=(C_R-N/2)T_b
\]

and the three Gaussian pairings give

\[
\frac1{d_R}\mathbb E\operatorname{Tr}_R Y_R^4
=3C_R^2-\frac N2C_R,
\qquad
\mathbb E\operatorname{Tr}_F Y^4=\frac{D(2N^2-3)}{4N}.
\]

Gaussian integration by parts gives
\(\operatorname{Cov}(|y|^2,P_4)=4\mathbb EP_4\)
for a homogeneous quartic, and
\(\operatorname{Var}(|y|^2)=2D\).
Consequently

\[
\operatorname{Cov}(|y|^2,D_1)=\frac{D(N^2-3)}{12N}.
\]

Since \(\operatorname{Tr}_R Y_R^2/d_R=C_R|y|^2/D\), the coefficient of \(\epsilon^2\) in the normalized character integral is

\[
\frac{3C_R^2-(N/2)C_R}{24}
-\frac{C_R}{2D}\frac{D(N^2-3)}{12N}
=\frac{C_R^2}{8}-\frac{N^2-2}{16N}C_R.
\]

This proves (4). Expanding the logarithm cancels \(C_R^2/8\) and proves (5).

## 4. A fundamental-character clock, with the magnetic term retuned

Define the clock using only the microscopic fundamental multiplier:

\[
\boxed{\tau_F(\epsilon)=-\frac{2}{C_F}\log\lambda_F(2N/\epsilon).}
\tag{6}
\]

Then

\[
\tau_F(\epsilon)=\epsilon+\frac{N^2-2}{8N}\epsilon^2+O(\epsilon^3),
\qquad
-\frac{\log\lambda_R(2N/\epsilon)}{\tau_F(\epsilon)}
=\frac{C_R}{2}+O_R(\epsilon^2).
\tag{7}
\]

For SU(3), the clock coefficient is exactly \(7/24\). For SU(2), it is \(1/8\); this also follows independently from the exact Bessel-character multiplier \(I_{2j+1}(4/\epsilon)/I_1(4/\epsilon)\).

The SU(2) comparison tests kinetic normalization only, not an SU(2) charge-odd carrier.

The fundamental energy is correct by definition. Therefore it is **not a holdout test**. The adjoint, sextet, decuplet, and 27-dimensional SU(3) representations are the meaningful holdouts supplied here.

To keep the target Hamiltonian coupling \(u\) fixed, use

\[
\boxed{
\beta_t=2N/\epsilon,\qquad \beta_s=2Nu\tau_F(\epsilon),
\quad
T_{\epsilon,F}^{W}
=e^{\tau_FuV/2}\left(\bigotimes_\ell C_{2N/\epsilon}\right)e^{\tau_FuV/2}.
}
\tag{8}
\]

Changing the time coordinate while leaving the old magnetic weight unchanged would instead replace \(u\) by \(u\epsilon/\tau_F\). Retuning the magnetic factor is essential, not optional bookkeeping.

On any fixed finite representation truncation, the kinetic generator in (8) differs from \(H_E\) by \(O(\epsilon^2)\) in matrix norm. Symmetric product splitting also gives a generator correction \(O(\tau_F^2)\) for bounded matrices. Hence the complete truncated transfer generator matches \(H_E-uV\) to second order in the temporal step. This bounded-matrix conclusion is what the finite plaquette test exercises.

This calibration is not a measurement of the interacting physical speed of light. It is an exact definition of a single-link kinetic time unit, and an improvement of its fixed-irrep temporal approximation.

## 5. Relation to anisotropic couplings and the physical prefactor

In the anisotropic convention of Byrnes et al. (their equations (1)–(8)), write

\[
\beta_t=\frac{2N\xi}{g_\tau^2},\qquad
\beta_s=\frac{2N}{\xi g_\sigma^2},\qquad \xi=\frac{a_s}{a_t}.
\]

Applying the leading matching (1) gives

\[
\epsilon=\frac{g_\tau^2a_t}{a_s},\qquad
u:=\frac{\beta_s}{2N\epsilon}=\frac1{g_\sigma^2g_\tau^2}.
\]

Thus if the Hamiltonian coupling is defined in that balanced convention by
\(g_H^2=g_\sigma g_\tau\), then \(u=g_H^{-4}\) and

\[
H_{\rm physical}=\frac{g_\tau^2}{a_s}H(u)
=\eta\frac{g_H^2}{a_s}H(u),\qquad
\eta:=\frac{g_\tau}{g_\sigma}.
\tag{9}
\]

This identifies the electric/magnetic coupling ratio that can appear in the finite-coupling energy prefactor. It does not compute \(\eta\), nor does it equate bare and renormalized anisotropies. In the matched weak-coupling expansion where \(\eta=1+O(g_H^2)\), the leading asymptotic normalization has \(c_H=1\) with the correction inside \([1+o(1)]\). At finite coupling the ratio must not be silently discarded. A convention defining \(g_H\) differently requires a new dictionary; no historical factor of four is applied to the strong-coupling coefficients.

The temporal refinement in (8) is a specific trajectory through bare action parameters approaching a fixed Hamiltonian. It is not automatically a line of constant continuum physics.

## 6. How a weighted matching estimate would reach the carrier

This is a separate conditional implication, not a claim that a one-link test establishes a lattice band.

Suppose the complete Wilson and Hamiltonian target bands have been identified in a common symmetry-covariant three-component frame, with symbols \(h^W_{\epsilon,u}\), \(h^H_u\) in \(\mathcal A_\mu\). Assume

\[
\|h^W_{\epsilon,u}-h^H_u\|_{\mu,\sharp}\le D(u)\epsilon^p.
\tag{10}
\]

Both Gamma fibers are scalar and both first momentum derivatives vanish. The weighted-centering lemma gives

\[
\|[h^W(k)-h^W(0)]-[h^H(k)-h^H(0)]\|
\le d(\epsilon,u)q(k),
\quad d(\epsilon,u)=\frac{\pi^2}{2e^2\mu^2}D(u)\epsilon^p.
\tag{11}
\]

Suppose the exact Hamiltonian carrier gap satisfies
\(g_H(k,u)\ge a(u)q(k)\), \(a(u)>0\), as proved conditionally on the G18 inputs by the relative-gap theorem. Then

\[
\boxed{g_W(k,\epsilon,u)\ge [a(u)-2d(\epsilon,u)]q(k).}
\tag{12}
\]

For \(d\le a/4\), the Wilson carrier is simple at every \(k\ne0\), with gap at least \(a q/2\). The rank-one projection obeys

\[
\|P_W(k)-P_H(k)\|\le\frac{d}{a-2d}.
\tag{13}
\]

**Proof.** Centering changes no within-fiber gap or eigenvector. Equation (11) and Weyl's eigenvalue inequality prove (12). For (13), subtract the lowest Hamiltonian eigenvalue, project the Wilson eigenvector equation onto its Hamiltonian complement, and use the lower bound \(a q\) there; the perturbation and eigenvalue displacement are each at most \(d q\). Solving the complementary equation gives the stated bound. The common \(q\) cancels before taking \(k\to0\).

A matching estimate on the source synthesis maps, in the same frame, would then transport the source residue bounds by the triangle inequality. No energy-only contour separating the entire carrier's energy range from the other bands is required or claimed.

What remains to prove for the physical application is the **uniform matched-band construction and estimate (10)**, including high-irrep control and the source frame. Fixed-irrep \(O_R(\epsilon^2)\) does not establish it. Neither the extensive finite-volume product estimate nor the 21-character model can be substituted for it.

A useful next decomposition is to establish a uniform low-energy window for the Wilson kinetic spectrum \(-\log\lambda_R/\tau_F\), then construct the magnetic-dressed shell with spatially weighted estimates. Treating its kinetic generator as a small bounded perturbation of the Casimir on every irrep is not justified by (4).

## 7. Executed numerical checks

The file `wilson_clock_certificate.json` records an independent two-dimensional SU(3) Weyl quadrature on \(512^2\) and \(1024^2\) grids, five temporal steps, and all 21 irreps with \(p+q\le5\). The largest difference between grids, divided by the time step to put it in electric-energy units, was approximately \(2.83\times10^{-14}\). Grid agreement is a numerical consistency check, not an interval enclosure.

At \(\epsilon=0.0125\), held-out one-link absolute energy errors were:

| Irrep | Raw Wilson clock | Fundamental-matched clock |
|---|---:|---:|
| adjoint 8 | 0.005481660994 | 0.000008260005 |
| sextet 6 | 0.006088892184 | 0.000011013320 |
| decuplet 10 | 0.010933478666 | 0.000046254506 |
| 27 | 0.014551446004 | 0.000088101496 |

The last two step sizes give raw error orders approximately 1 and matched error orders approximately 2.02 for these holdouts.

The coupled test is one closed four-link plaquette restricted to the 21-dimensional class-function space \(p+q\le5\). Its electric matrix is \(2C_R\); multiplication by \(\chi_F+\chi_{\bar F}\) is built from SU(3) tensor-product neighbors. Charge parity is diagonalized explicitly. Both the transfer matrix and the reference Hamiltonian use **the same declared truncation**. No full-Hilbert-space error is inferred.

At \(u=0.2\), the reference odd–even gap is 2.8884161619731024 in electric units:

| epsilon | raw transfer gap error | matched transfer gap error |
|---:|---:|---:|
| 0.05 | 0.03916415601 | 0.00001115526825 |
| 0.025 | 0.01942712256 | 0.00000275283782 |
| 0.0125 | 0.00967503504 | 0.00000068393757 |

The observed last-step orders are 1.0057 (raw), 2.0090 (matched), and 2.0002 (heat-kernel comparator). The near-fundamental lowest state partly benefits from the calibration by construction; this is why the independent irrep holdouts are reported separately. These data validate temporal matching in the test model, not a 3+1-dimensional glueball mass.

## 8. Provenance and literature boundary

Repository-derived input: canonical Hamiltonian and coupling convention in Revision 6, equations (1)–(4); G18's weighted Banach algebra and symbol statement in `paper/research_notes/G18_INTERNAL_BBDAGGER_SHEET_CLOSURE_20260830.tex`; symmetry discussion in ADR 0028; normalization and matching boundary in `paper/research_notes/G19_CONTINUUM_BRIDGE_INSERT.tex`.

Derived in this session: the complete calculation (4)–(7) in the stated normalization, the explicitly retuned transfer prescription, and the matched-band implication (10)–(13). These are derivations made here, not claims of previously unknown results.

Primary sources consulted for the methodological/normalization context:

- J. Kogut and L. Susskind, *Hamiltonian formulation of Wilson's lattice gauge theories*, Phys. Rev. D 11, 395 (1975), DOI `10.1103/PhysRevD.11.395`. The publisher abstract was consulted; its full derivation was not reproduced from the paper.
- M. Creutz, *Gauge fixing, the transfer matrix, and confinement on a lattice*, Phys. Rev. D 15, 1128 (1977), DOI `10.1103/PhysRevD.15.1128`. The primary publisher abstract explicitly describes the temporal-limit relation; its paywalled full text was not read here.
- P. R. Chernoff, *Note on product formulas for operator semigroups*, J. Funct. Anal. 2, 238–242 (1968), DOI `10.1016/0022-1236(68)90020-7`. The standard product theorem is an external mathematical input; this note verifies its model-specific core and stability hypotheses.
- T. M. R. Byrnes et al., *Hamiltonian limit of (3+1)-dimensional SU(3) lattice gauge theory on anisotropic lattices*, Phys. Rev. D 69, 074509 (2004), arXiv `hep-lat/0311014`, especially Section II, equations (1)–(10), on physical/bare anisotropy and the two couplings. These equations were read directly from the preprint.
- P. Menotti and E. Onofri, *The action of SU(N) lattice gauge theory in terms of the heat kernel on the group manifold*, Nucl. Phys. B 190, 288–300 (1981), DOI `10.1016/0550-3213(81)90560-5`. The publisher abstract supplies historical context for heat-kernel alternatives, not the coefficient in (4).

No source above is invoked as proving the new volume-uniform Wilson carrier estimate. G19 remains open.
