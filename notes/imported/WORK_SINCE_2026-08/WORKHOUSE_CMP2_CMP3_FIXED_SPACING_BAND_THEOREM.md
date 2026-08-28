# CMP(2)–CMP(3): a nonzero three-component fixed-spacing lattice band

**Read-only external proof artifact**  
**Date:** 2026-08-22  
**Model:** Hamiltonian (SU(3)) lattice gauge theory on (mathbb Z^3), at sufficiently small strong-coupling coordinate (u)  
**Status:** proved from Yarotsky's published coefficient estimate and correlation bound, the WORKHOUSE electric-shell theorem, and the completed CMP(1) close-projection theorem. The companion CMP(4) proof now transfers this result to the literal Wilson source. Every continuum claim remains open.

## 1. Result

In the infinite-volume, gauge-invariant, charge-conjugation-odd vacuum GNS
sector, let (P_u^-) be the Riesz projection onto the isolated spectral
window descended from the free one-plaquette energy. For sufficiently small
(|u|), the projected normalized plaquette seeds

\[
\psi_{x,\alpha}
=P_u^-\pi_u(\widehat w_{x,\alpha})\Omega_u,
\qquad x\in\mathbb Z^3,
\quad \alpha=1,2,3,
\]

have a translation-invariant block Gram kernel (G) satisfying, for some
(mu>0),

\[
\|G-I\|_\mu<1,
\qquad
\|K\|_\mu
:=\max_\alpha\sum_{r\in\mathbb Z^3,\,\beta}
e^{\mu|r|_1}|K_{\alpha\beta}(r)|.
\tag{1.1}
\]

Consequently the projected synthesis map is an (ell^2) frame, and CMP(1)
totality upgrades it to an exact unitary identification

\[
\operatorname{Ran}P_u^-
\simeq\ell^2(\mathbb Z^3)\otimes\mathbb C^3.
\tag{1.2}
\]

In this representation (H_u^-|_{\operatorname{Ran}P_u^-}) is convolution
by an exponentially summable Hermitian (3\times3) matrix kernel. Its Bloch
matrix is analytic in a complex strip. This is a rigorous fixed-lattice-
spacing, three-component lattice quasiparticle band with a true external
spectral gap and a uniformly positive residue for the **canonical plaquette
creation source**.

The conclusion is not a continuum particle theorem. A companion proof now
dresses the literal Wilson multiplication source, but nothing here identifies
continuum spin or continues the band from small (u) toward the continuum
direction.

## 2. Inputs and notation

Use the gap-one rescaling (widehat H=(3/2)H). The free target energy is
(widehat E_F=4), and

\[
g:=\sup_x\|\widehat\phi_x(u)\|=27|u|.
\tag{2.1}
\]

The completed CMP(1) theorem supplies:

1. the exact physical coefficient shell
   (operatorname{Ran}R^-=ell^1)-span of all
   (w_{x,\alpha});
2. the infinite-volume coefficient Riesz projection (mathcal P_u^-);
3. the GNS intertwiner
   (P_u^-\Gamma_u=\Gamma_u\mathcal P_u^-);
4. the totality identity

   \[
   \operatorname{Ran}P_u^-
   =\overline{\operatorname{span}}
   \{P_u^-\Gamma_uw_{x,\alpha}\};
   \tag{2.2}
   \]

5. nonzero individual projected seeds for small (u).

For a seed label (s=(x,\alpha)), write (S_s) for its three-cell support.
For a finite exact support (J), let (d(J,S_s)) be Yarotsky's rooted
forest pseudometric: the minimum number of lattice edges in a forest whose
components each meet (S_s) and whose vertices include every site of (J).
The root set is available at zero cost, so (d(J,S_s)=0) when
(J\subseteq S_s). The two elementary geometric facts used below are

\[
|J|\le d(J,S_s)+|S_s|=d(J,S_s)+3,
\tag{2.3}
\]

and, for two roots (S_s,S_t),

\[
\operatorname{dist}(S_s,S_t)
\le
\operatorname{dist}(S_s,J)+d(J,S_t).
\tag{2.4}
\]

The first follows because the added graph plus the three root vertices has
at most (d+3) vertices. For the second, join a closest point of (J) to
(S_s) and then use the rooted graph connecting (J) to (S_t).

## 3. CMP(2): rooted localization of a projected three-cell seed

Fix an auxiliary decay parameter (0<\eta<1). Yarotsky's construction
allows (eta) to be chosen first and then (g) to be made sufficiently
small. For a coefficient family (v=(v_J)), define

\[
\|v\|_{S,0}^{(\eta)}
=\sum_J\eta^{-d(J,S)}\|v_J\|,
\qquad
\|v\|_{S,1}^{(\eta)}
=\sum_J\eta^{-d(J,S)}\|H_{J,0}v_J\|.
\tag{3.1}
\]

The rooted-distance triangle inequality

\[
d(K,S)\le d(K,J)+d(J,S)
\tag{3.2}
\]

and Yarotsky's equation (14) give

\[
\|F_uv\|_{S,0}^{(\eta)}
\le a_\eta(g)\|v\|_{S,1}^{(\eta)},
\qquad
a_\eta(g)=\eta C_{14}(\eta)g.
\tag{3.3}
\]

Indeed, equation (14) bounds a column from (J) by

\[
\sum_K\|(F_uv_J)_K\|
\eta^{-(d(K,J)+1)}
\le C_{14}(\eta)g|J|\|v_J\|,
\]

and (H_{J,0}\ge|J|) absorbs the support factor. Summing columns with
(3.2) proves (3.3).

Let (gamma) be a contour surrounding only (4), and set

\[
K_1=\sup_{z\in\gamma}
\|D(D-z)^{-1}\|,
\qquad
q_\eta=a_\eta(g)K_1.
\tag{3.4}
\]

For (q_\eta<1), the same Neumann series as Yarotsky's equation (15)
is bounded in the rooted norm. For every normalized plaquette seed (w_s),

\[
\mathcal P_u^-w_s=w_s+c_s,
\tag{3.5}
\]

with

\[
\boxed{
\|c_s\|_{S_s,1}^{(\eta)}
\le
A_\eta(g)
:=
\frac{\operatorname{length}(\gamma)}{2\pi}
K_1\frac{q_\eta}{1-q_\eta}.}
\tag{3.6}
\]

The bound is uniform in (x), (alpha), and volume, and
(A_\eta(g)\to0) as (g\to0). This is the finite-support version of
Yarotsky's equations (19)--(20). The proof uses equation (14) for arbitrary
input support; no one-site nondegeneracy or nonoverlap assumption enters.

For the fixed circle (|z-4|=1/8), one may take (K_1=34). All resulting
smallness conditions remain existential because (C_{14}(\eta)) is not
explicit in the primary source.

## 4. Local product-vacuum continuity

The correlation estimate used below is small only at positive separation.
The finitely many overlapping seed pairs require a separate local estimate.

Let (T) be any fixed finite set of grouped cells and

\[
Q_T=|\Omega_{T,0}\rangle\langle\Omega_{T,0}|.
\]

The unit onsite gap gives

\[
1-Q_T\le\sum_{x\in T}
(1-|\Omega_x\rangle\langle\Omega_x|)
\le\sum_{x\in T}\widehat h_x.
\tag{4.1}
\]

A periodic finite-volume variational energy-density estimate gives the
bounded local-excitation estimate

\[
\omega_u(1-|\Omega_x\rangle\langle\Omega_x|)\le2g.
\tag{4.2}
\]

Indeed, (E_\Lambda\le\langle\Omega_0,H_\Lambda\Omega_0\rangle
\le|\Lambda|g), while
(E_\Lambda\ge\sum_x\langle\widehat h_x\rangle-|\Lambda|g).
Average a finite-volume ground state over translations if necessary. Then
(|\Lambda|^{-1}\sum_x\langle\widehat h_x\rangle\le2g), and translation
invariance makes this pointwise. Since
(1-|\Omega_x\rangle\langle\Omega_x|\le\widehat h_x), the resulting
bounded projector estimate passes to every thermodynamic subsequential
limit. Such a limit is an infinite-volume ground state; Yarotsky uniqueness
identifies it with (omega_u). There is one bundled interaction anchor per
grouped cell. Thus

\[
\beta_T(u):=1-\omega_u(Q_T)\le2|T|g.
\tag{4.3}
\]

For any local operator (A\in\mathcal B(\mathcal H_T)), use
(Q_TAQ_T=\omega_0(A)Q_T), insert (Q_T+(1-Q_T)) on both sides, and apply
the Cauchy--Schwarz inequality for the state. This gives

\[
|\omega_u(A)-\omega_0(A)|
\le
2\|A\|\sqrt{\beta_T(u)}+2\|A\|\beta_T(u).
\tag{4.4}
\]

This proves local weak-* convergence to the product state with an explicit
uniform modulus. It does not assume a finite-dimensional local Hilbert
space or a density matrix.

## 5. CMP(3): exponentially summable block Gram kernel

Yarotsky's correlation estimate (16) can be written as follows. For a fixed
interaction range, there is (C_0>1), independent of (g), and a decay
base (\tau(g)\to0) such that

\[
|\omega_u(A^*B)-\omega_u(A^*)\omega_u(B)|
\le
C_0^{|I|+|J|}\tau(g)^{\operatorname{dist}(I,J)}
\|A\|\|B\|
\tag{5.1}
\]

for (A,B) supported on (I,J). All exact-support coefficients in the
physical odd sector are charge odd, so their one-point functions vanish.

Define the block Gram kernel

\[
G_{st}=\langle P_u^-\Gamma_uw_s,P_u^-\Gamma_uw_t\rangle.
\tag{5.2}
\]

Because (P_u^-) is an orthogonal projection, only **one** projected mark
needs to be expanded:

\[
\begin{aligned}
G_{st}
&=\langle\Gamma_uw_s,P_u^-\Gamma_uw_t\rangle\\
&=\omega_u(\widehat w_s^{,*}\widehat w_t)
+\sum_J\omega_u(\widehat w_s^{,*}\widehat c_{t,J}).
\end{aligned}
\tag{5.3}
\]

This identity is why a separate two-Riesz-mark expansion is unnecessary for
the canonical Gram matrix.

Let

\[
R_{st}=\operatorname{dist}(S_s,S_t).
\]

For (R_{st}\ge1), the raw term is bounded by

\[
|\omega_u(\widehat w_s^{,*}\widehat w_t)|
\le C_0^6\tau(g)^{R_{st}}.
\tag{5.4}
\]

For a correction support (J), put (d=d(J,S_t)) and
(p=\operatorname{dist}(S_s,J)). Equations (2.3)--(2.4) imply

\[
|J|\le d+3,
\qquad
R_{st}\le p+d.
\]

Write

\[
a_{t,J}=\|c_{t,J}\|\eta^{-d},
\qquad
\sum_Ja_{t,J}\le A_\eta(g),
\tag{5.5}
\]

The empty coefficient vanishes because (c_t) is charge odd whereas charge
conjugation is trivial on the scalar exact-support summand. Therefore
(H_{J,0}\ge1) on every nonzero term, and (3.6) proves the displayed sum
bound. Then (5.1) gives

\[
\begin{aligned}
|\omega_u(\widehat w_s^{,*}\widehat c_{t,J})|
&\le C_0^{3+|J|}\tau(g)^p\|c_{t,J}\|\\
&\le C_0^6 a_{t,J}(C_0\eta)^d\tau(g)^p.
\end{aligned}
\tag{5.6}
\]

Set

\[
\theta=\max\{C_0\eta,\tau(g)\}.
\tag{5.7}
\]

Since (0<\theta<1) and (p+d\ge R_{st}), summation of (5.6) yields

\[
\left|\sum_J
\omega_u(\widehat w_s^{,*}\widehat c_{t,J})\right|
\le C_0^6A_\eta(g)\theta^{R_{st}}.
\tag{5.8}
\]

For (R_{st}=0), there are only finitely many relative seed labels. Their
product-vacuum inner products are

\[
\omega_0(\widehat w_s^{,*}\widehat w_t)=\delta_{st}.
\]

Apply (4.4) on (T=S_s\cup S_t), where (|T|\le6), and use
(|\Gamma_uc_t\|\le\|c_t\|_1\le A_\eta(g)). Uniformly over all contact
pairs,

\[
|G_{st}-\delta_{st}|
\le C_{\rm loc}\sqrt g+A_\eta(g),
\qquad R_{st}=0.
\tag{5.9}
\]

The constant includes the harmless (O(g)) term from (4.4).

Choose (mu>0). First choose (eta) so small that

\[
e^\mu C_0\eta<1.
\tag{5.10}
\]

Then shrink (g) so that (e^\mu\tau(g)<1). The three-dimensional shell
count grows only quadratically, and the three-cell roots have bounded
diameter. Therefore (5.4), (5.8), and (5.9) imply

\[
\boxed{
\|G-I\|_\mu
\le
C_{\rm contact}\bigl(\sqrt g+A_\eta(g)\bigr)
+C_{\rm geom}\sum_{n\ge1}(n+1)^2e^{\mu n}
\left[
C_0^6\tau(g)^n+C_0^6A_\eta(g)\theta^n
\right].}
\tag{5.11}
\]

The right-hand side tends to zero as (g\to0) with the chosen (eta).
Hence it is below one for an existential nonempty small-(u) interval.
This proves CMP(3).

## 6. Frame, totality, and the exact three-component fiber

Let (J_P) initially act on finitely supported
(f\in\ell^2(\mathbb Z^3;\mathbb C^3)) by

\[
J_Pf=\sum_{x,\alpha}f_{x,\alpha}\psi_{x,\alpha}.
\tag{6.1}
\]

Its Gram operator is the convolution operator (G). Put
(g_0=\|G-I\|_\mu<1). Since the weighted row norm dominates the
(ell^2) convolution norm,

\[
(1-g_0)\|f\|_2^2
\le\|J_Pf\|^2
\le(1+g_0)\|f\|_2^2.
\tag{6.2}
\]

Hermiticity and translation invariance give the matching weighted column
bound, so the Schur estimate is two-sided. Thus (J_P) extends to a bounded,
bounded-below map. CMP(1) says its range
is dense in (operatorname{Ran}P_u^-); bounded-below maps have closed
range, so it is onto that Riesz space.

Matrix-valued weighted convolution kernels form a unital Banach algebra.
The convergent binomial series gives (G^{-1/2}) in the same algebra. Hence

\[
W:=J_PG^{-1/2}:
\ell^2(\mathbb Z^3)\otimes\mathbb C^3
\longrightarrow\operatorname{Ran}P_u^-
\tag{6.3}
\]

is unitary and intertwines translations. This proves the exact
three-component translation multiplicity, not merely nonzero individual
seeds.

## 7. Exponentially local Hamiltonian kernel

Let (mathbb H_u=D+F_u) be the coefficient Hamiltonian. Since
(mathcal P_u^-) is its Riesz projection,

\[
\mathbb H_u\mathcal P_u^-w_t=4w_t+k_t,
\tag{7.1}
\]

where, using (3.5),

\[
k_t=Dc_t+F_uw_t+F_uc_t.
\tag{7.2}
\]

Again the empty coefficient is absent by charge oddness.

Equations (3.3) and (3.6) imply a rooted bound

\[
\|k_t\|_{S_t,0}^{(\eta)}
\le
B_\eta(g)
:=A_\eta(g)+4a_\eta(g)+a_\eta(g)A_\eta(g)
\xrightarrow[g\to0]{}0.
\tag{7.3}
\]

All Hamiltonians in this section remain in the gap-one rescaled units, so the
free target is (4). Define the energy kernel in the projected seed frame,

\[
B_{st}
=\langle P_u^-\Gamma_uw_s,
H_u^-P_u^-\Gamma_uw_t\rangle.
\tag{7.4}
\]

Self-adjointness, (P_u^-H_u^-=H_u^-P_u^-), and the coefficient
intertwining give the one-sided identity

\[
B_{st}
=\langle\Gamma_uw_s,
\Gamma_u(4w_t+k_t)\rangle.
\tag{7.5}
\]

To apply the intertwining to the infinite coefficient family
(mathcal P_u^-w_t\in\operatorname{Dom}D), truncate it by exact support in
the (D)-graph norm. The relative (D)-bound on (F_u), boundedness of
(Gamma_u), and closedness of (H_u^-) pass equation (18) to the limit.

Repeating the proof of Section 5 with (A_\eta(g)) replaced by
(B_\eta(g)) gives, explicitly, a raw contribution
(4(G^{\rm raw}-I)) plus the rooted corrected-mark contribution. Hence

\[
\|B-4I\|_\mu\longrightarrow0.
\tag{7.6}
\]

In the orthonormal representation (6.3),

\[
W^*H_u^-W=G^{-1/2}BG^{-1/2}=:\mathcal A_u.
\tag{7.7}
\]

The kernel of (mathcal A_u) belongs to the same weighted convolution
algebra. Its Fourier transform

\[
\mathcal A_u(k)=\sum_{r\in\mathbb Z^3}
\mathcal A_u(r)e^{-ik\cdot r}
\tag{7.8}
\]

is a Hermitian (3\times3) matrix for real (k) and is analytic for
(|\operatorname{Im}k_j|<\mu). Its three eigenvalues are continuous
dispersion sheets and are analytic wherever the corresponding eigenvalue is
simple. Crossings are allowed; global analyticity belongs to the matrix, not
necessarily to three separately labelled scalar branches.

The band retains the true external spectral gap supplied by the Riesz
window. Internal sheet crossings or the (L^{-2}) momentum spacing do not
affect this complete-cluster result.

The cubic group acts exactly on the anchored seed labels, but not always by
a constant internal matrix away from zero momentum. If
(g e_j=s_j e_{\pi(j)}), the positive plaquette anchoring shifts by

\[
a_g(\alpha)=
\mathbf1_{s_j=-1}(-e_{\pi(j)})
+\mathbf1_{s_k=-1}(-e_{\pi(k)}),
\]

and its charge-odd orientation acquires the corresponding sign. In Bloch
space this is a possibly (k)-dependent monomial matrix. At (k=0) the
phases disappear and the three-dimensional fiber is the ordinary cubic
(T_1) triplet. This fixed-spacing statement still does not assign an
(SO(3)) spin.

## 8. Canonical source residue

Equation (6.2) is exactly the canonical **spectral-projection weight** bound:

\[
J_P^*J_P=G\succeq(1-g_0)I.
\tag{8.1}
\]

After Fourier transform, the full-island three-source map is invertible in
every momentum fiber; no fiber is dark to the complete three-source family.
Indeed the operator lower bound first holds almost everywhere, while the
exponentially summable kernel makes (G(k)) continuous, upgrading it to every
real (k).
This does not assign nonzero weight to each separately labelled scalar sheet
at a crossing. It is not yet a continuum pole residue. The conclusion
is proved first for the bounded canonical rank-one plaquette-creation source
(widehat w_{x,\alpha}). The companion CMP(4) theorem transfers the complete
three-source frame and every-momentum lower bound to multiplication by
(operatorname{ImTr}U_p).

## 9. Exact status and next obstruction

### Closed at sufficiently small (u), fixed lattice spacing

1. CMP(1): irrelevant contraction, totality, and nonzero individual seeds.
2. CMP(2): exponentially rooted localization of each projected three-cell
   plaquette seed.
3. CMP(3): exponentially summable block Gram kernel and a uniform
   (ell^2) frame.
4. Exact unitary equivalence of the physical Riesz island with
   (ell^2(\mathbb Z^3)\otimes\mathbb C^3).
5. An exponentially local analytic (3\times3) Bloch Hamiltonian and a
   true external gap.
6. Uniform positive residue for the canonical creation source.

### CMP(4) — closed in the companion proof

Let (D_s) be the difference between the normalized Wilson multiplication
source and the canonical rank-one creator. It annihilates the product vacuum
exactly. Local product-vacuum continuity controls the finitely many contact
terms, while Yarotsky's correlation bound controls the spatial tail. The
resulting weighted cross kernel (C=T_c^*T_D) tends to zero. With canonical
Gram operator (G=T_c^*T_c), the exact factorization

\[
T_W=T_c\bigl(I+G^{-1}C\bigr)
\tag{9.1}
\]

transfers the exponentially local frame to the literal Wilson source. The
factor in parentheses is invertible in the weighted convolution algebra for
sufficiently small (u). No new rooted BCH/tree expansion is required.

### First remaining obstruction: the continuum gate

Even with CMP(4), small (u) is the strong-coupling, fixed-spacing regime.
Nothing here continues the band to the asymptotically free continuum
trajectory. The uniform physical mass/gap/residue and OS scaling theorem
remains a separate open problem.

## 10. Primary source and companion proofs

- D. A. Yarotsky, [*Quasi-particles in weak perturbations of
  non-interacting quantum lattice systems*](https://arxiv.org/pdf/math-ph/0411042),
  especially equations (14)--(16) and (18)--(24).
- [CMP(1) close-projection proof](./WORKHOUSE_CMP1_CLOSE_PROJECTION_PROOF.md)
- [CMP(4) Wilson-source transfer proof](./WORKHOUSE_CMP4_WILSON_SOURCE_TRANSFER_PROOF.md)
- [Electric-shell theorem proof](./WORKHOUSE_ELECTRIC_SHELL_THEOREM_PROOF.md)
- [Yarotsky spectral-localization import note](./WORKHOUSE_YAROTSKY_SPECTRAL_LOCALIZATION_IMPORT_NOTE.md)

## 11. Repository integrity

This document was created outside the WORKHOUSE repository. No repository
file was edited.
