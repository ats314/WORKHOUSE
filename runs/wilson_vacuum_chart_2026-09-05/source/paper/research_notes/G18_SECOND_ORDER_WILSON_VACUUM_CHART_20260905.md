# A second-order local vacuum chart for the actual Wilson transfer

Date: 5 September 2026.

This note advances the operator mechanism in
`G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md`. It constructs the next
vacuum rotation directly from the actual symmetric Wilson transfer and proves
a volume-, temporal-mesh-, and representation-uniform bound on its complete
second Taylor coefficient. The result is coefficientwise on the full
kinematic Hilbert space. The construction preserves gauge, charge-conjugation,
and one-form symmetries and therefore restricts to the physical neutral odd
space.

No representation cutoff, source-span compression, replacement of the Wilson
logarithm by an auxiliary Hamiltonian, or all-orders activity hypothesis is
used. The input is the calibrated free kinetic gap from the preceding Wilson
window note. Uniform bounds on a finite-coupling remainder and on the complete
nonlinear activity series are subsequent questions.

## 1. Actual transfer, local subsystems, and coefficient convention

Let the periodic cubic spatial lattice have side length `L >= 3`. A link is
contained in four plaquettes. Each plaquette has four links and meets at most
twelve other plaquettes in a link. Supports in this note are **sets of links**;
meeting at a vertex alone does not create an overlap of operator supports.

Use the calibrated temporal step `tau = tau_F(epsilon)` and write

\[
 K_{\epsilon,L}=\sum_{\ell}k_{\epsilon,\ell},\qquad
 k_{\epsilon,\ell}\Omega_\ell=0,\qquad
 k_{\epsilon,\ell}\big|_{\Omega_\ell^\perp}\ge\gamma,
 \qquad \gamma=C_F/2.
\]

The link vacuum is the constant Haar function. On every nonempty finite link
set `X`, put

\[
 \Omega_X=\bigotimes_{\ell\in X}\Omega_\ell,\qquad
 P_X=|\Omega_X\rangle\langle\Omega_X|,\qquad Q_X=1-P_X,
 \qquad D_X=e^{-sK_X},\quad K_X=\sum_{\ell\in X}k_{\epsilon,\ell}.
\]

Then

\[
 D_XP_X=P_X,\qquad 0\le D_XQ_X\le\delta Q_X,
 \qquad\delta=e^{-\gamma s}.
\]

For a plaquette `p`, let `v_p = chi_p + bar(chi_p)`, so
`||v_p|| <= J := 2N`, and give every face its own dimensionless coupling
`z_p`. The genuine transfer and its positive integer block are

\[
 T_L(z)=e^{\frac\tau2\sum_pz_pv_p}
        e^{-\tau K_{\epsilon,L}}
        e^{\frac\tau2\sum_pz_pv_p},
 \qquad B_L(z)=T_L(z)^m,\qquad s=m\tau.
 \tag{1.1}
\]

For a finite set `A` of active faces, let `X(A)` be their union of links.
Define `T_A(z)` and `B_A(z)` by (1.1) on `X(A)`, with only faces in `A`
active. All other links are free. In particular,

\[
 B_L(z_A,0)=B_A(z_A)\otimes D_{X(A)^c}.
 \tag{1.2}
\]

Write `b_A(z)` for the simple eigenvalue of `B_A(z)` continuing its free
vacuum eigenvalue 1. For sufficiently small real couplings it is the Perron
eigenvalue. Analytic bounded perturbation of the isolated free eigenvalue
defines its complex branch near zero as well. These assertions concern only
the finite spatial subsystem in question; the link representation spaces
remain untruncated. Set

\[
 \mathcal D_A(z)=B_A(z)/b_A(z).
 \tag{1.3}
\]

Equation (1.2) implies `b_L(z_A,0)=b_A(z_A)` near zero. Thus coefficients
of the normalized global operator can be computed in the corresponding
active-face subsystem. This is a property of the actual Perron normalization,
not an assumed linked expansion.

Throughout, `[u^2]` means the Taylor coefficient, namely one half of the
second derivative at zero. For distinct faces, `[z_p z_q]` is the mixed
derivative at zero without a factor of one half. After all face couplings
are set to `u`, unordered distinct pairs occur once.

We use the short spectral block from the preceding note:

\[
 s_{\rm sp}=\gamma^{-1}\log(5/4),\qquad
 m=\lceil s_{\rm sp}/\tau\rceil,\qquad
 0<\tau\le\tau_0\le s_{\rm sp}/4,
 \qquad s\le s_1:=s_{\rm sp}+\tau_0.
 \tag{1.4}
\]

Hence `delta <= 4/5`. The one-plaquette vacuum excitation has calibrated
energy `E_s=4 gamma` exactly, as assumed and proved upstream.

## 2. The first rotation and its local coefficient

Define

\[
 d_\tau(E_s)=\frac\tau2\coth(\tau E_s/2),\qquad
 S_p=d_\tau(E_s)(v_pP_p-P_pv_p),\qquad
 U_{1,A}(z)=\exp\!\left(\sum_{p\in A}z_pS_p\right).
 \tag{2.1}
\]

The notation `P_p` means the product vacuum projection on the four links of
`p`. Each `S_p` is anti-Hermitian and bounded. Since `v_p Omega_p` is
orthogonal to `Omega_p`, its off-diagonal rank-two form gives

\[
 \|S_p\|=d_\tau(E_s)\|v_p\Omega_p\|\le d_\tau(E_s)J.
\]

For real couplings `U_1` is unitary. For complex couplings its inverse,
rather than its adjoint, is used in the analytic expressions. Put

\[
 \mathcal E_A(z)=U_{1,A}(z)^{-1}\mathcal D_A(z)U_{1,A}(z).
 \tag{2.2}
\]

The one-face derivative is

\[
 F_p:=[z_p]\mathcal E_{\{p\}}(z_p)
      =B_p'(0)+[D_p,S_p],
 \qquad F_pP_p=P_pF_p=0.
 \tag{2.3}
\]

Indeed `b_p'(0)=0`, and direct differentiation of the integer power gives

\[
 B_p'(0)\Omega_p
 =d_\tau(E_s)(1-e^{-sE_s})v_p\Omega_p.
\]

The commutator contributes exactly its negative. Self-adjointness gives
annihilation on the other side. Every partial first derivative of (2.2)
therefore annihilates the full subsystem vacuum.

A convenient common bound is

\[
 f_*:=J(s_1+2/E_s+\tau_0),\qquad \|F_p\|\le f_*.
 \tag{2.4}
\]

To see the temporal uniformity, use
`d_tau(E_s) <= 1/E_s + tau/2`; this follows from
`x coth x <= 1+x` for `x>0`. The unrounded local estimate is
`J(s+2d_tau(E_s))`. No kinetic operator is differentiated in deriving it;
the kinetic factors enter only as contractions.

## 3. Precisely normalized one- and two-face coefficients

For a single face and for distinct overlapping faces define

\[
 A_{pp}:=[z_p^2]\mathcal E_{\{p\}}(z_p),\qquad
 A_{pq}:=[z_pz_q]\mathcal E_{\{p,q\}}(z_p,z_q)
 \quad(p\cap q\ne\varnothing).
 \tag{3.1}
\]

These are self-adjoint local operators on four or at most seven links.
Their definition includes the actual local Perron eigenvalue to the same
order. There is no manual vacuum-energy replacement.

### Lemma 3.1. Local scalar cancellation

For every coefficient in (3.1), on its own link support `X`,

\[
 \langle\Omega_X,A\Omega_X\rangle=0.
 \tag{3.2}
\]

**Proof.** Let `psi_A(z)` be the eigenvector of `E_A(z)` with eigenvalue
1, analytically normalized by
`<Omega_X,psi_A(z)>=1`. Its zeroth coefficient is `Omega_X`. Every first
coefficient vanishes: differentiating the eigenvector equation gives

\[
 (1-D_X)[z_p]\psi_A=([z_p]\mathcal E_A)\Omega_X=0,
\]

and `1-D_X` is invertible on `Q_X`. For a degree-two monomial `alpha`,
the same equation now has no first-derivative cross terms:

\[
 (1-D_X)[z^\alpha]\psi_A=([z^\alpha]\mathcal E_A)\Omega_X.
 \tag{3.3}
\]

Taking its vacuum component proves (3.2). This argument applies separately
to `z_p^2` and to `z_pz_q`. ∎

### Lemma 3.2. Uniform local norm bounds

\[
 \boxed{\ \|A_{pp}\|\le f_*^2,\qquad
          \|A_{pq}\|\le2f_*^2.\ }
 \tag{3.4}
\]

**Proof.** First omit the scalar normalization and put
`bar B_A=U_1,A^{-1} B_A U_1,A`. Expand its actual finite product of
exponentials. Taking norms term by term, the sum of absolute coefficient
bounds is majorized coefficientwise by

\[
 \exp\!\left(J(s+2d_\tau(E_s))\sum_{p\in A}|z_p|\right).
 \tag{3.5}
\]

There are `m` kinetic contractions, while the total weight of the magnetic
exponentials is `m tau=s`. The two rotations each contribute at most
`d_tau(E_s)J` per face. Noncommuting ordered products are all included in
this exponential majorant; their norms are submultiplicative. Consequently

\[
 \|[z_p^2]\bar B_A\|\le f_*^2/2,
 \qquad \|[z_pz_q]\bar B_A\|\le f_*^2.
\]

The first vacuum columns of `bar B_A` vanish, and its first eigenvalue
coefficients vanish. Ordinary degree-two eigenvector expansion therefore
gives, for either monomial,

\[
 [z^\alpha]b_A
 =\langle\Omega_X,[z^\alpha]\bar B_A\Omega_X\rangle,
 \qquad
 [z^\alpha]\mathcal E_A
 =[z^\alpha]\bar B_A-([z^\alpha]b_A)D_X.
 \tag{3.6}
\]

The triangle inequality and `||D_X||=1` multiply the two unnormalized bounds
by at most two. This proves (3.4). ∎

## 4. The second local vacuum rotation

For each `A=A_pp` or `A=A_pq`, define on its support `X`

\[
 \chi_A=(1-D_X)^{-1}Q_XA\Omega_X,\qquad
 S_A=|\chi_A\rangle\langle\Omega_X|
       -|\Omega_X\rangle\langle\chi_A|,
 \qquad F_A=A+[D_X,S_A].
 \tag{4.1}
\]

The inverse is only on `Q_X`; its norm is at most `1/(1-delta)`. All
operators in (4.1) are bounded on the entire local Hilbert space.

### Lemma 4.1. Quadratic local anchoring

\[
 F_AP_X=P_XF_A=0,\qquad
 \|S_A\|=\|\chi_A\|\le\frac{\|A\|}{1-\delta},\qquad
 \|F_A\|\le11\|A\|.
 \tag{4.2}
\]

In particular, writing `F_pp=F_(A_pp)` and `F_pq=F_(A_pq)`,

\[
 \boxed{\ \|F_{pp}\|\le11f_*^2,\qquad
          \|F_{pq}\|\le22f_*^2.\ }
 \tag{4.3}
\]

**Proof.** Equation (3.2) makes `A Omega_X` orthogonal to the vacuum.
Since `S_A Omega_X=chi_A`,

\[
 [D_X,S_A]\Omega_X=(D_X-1)\chi_A=-A\Omega_X.
\]

Both `A` and `[D_X,S_A]` are self-adjoint, so the opposite vacuum leg also
vanishes. Since `chi_A` is orthogonal to `Omega_X`, the norm of its
anti-Hermitian rank-two generator is exactly `||chi_A||`, without an extra
factor of two. Finally

\[
 \|F_A\|\le\|A\|+2\|S_A\|
 \le\left(1+\frac2{1-\delta}\right)\|A\|
 \le11\|A\|.
\]

This proves the lemma. ∎

## 5. Exact linked identity for the complete quadratic coefficient

Embed all local generators into the full lattice and set

\[
 S_{2,L}=\sum_pS_{A_{pp}}
          +\sum_{\{p,q\}:p\cap q\ne\varnothing}S_{A_{pq}},
 \qquad
 U_{2,L}(u)=e^{u^2S_{2,L}},\qquad U_L(u)=U_{1,L}(u)U_{2,L}(u),
\]

\[
 \widetilde{\mathcal D}_L(u)
 =U_L(u)^*\frac{T_L(u)^m}{b_L(u)}U_L(u)
 \quad\text{for real }u.
 \tag{5.1}
\]

The finite-volume unitaries in (5.1) are exact operators. Only their first
two Taylor coefficients are controlled by the present theorem.

### Theorem 5.1. Complete second-order connected/disconnected decomposition

With every distinct pair below unordered,

\[
 \begin{aligned}
 [u^2]\widetilde{\mathcal D}_L={}&
 \sum_p F_{pp}\otimes D_{p^c}\\
 &+\sum_{\{p,q\}:p\cap q\ne\varnothing}
       F_{pq}\otimes D_{(p\cup q)^c}\\
 &+\sum_{\{p,q\}:p\cap q=\varnothing}
       F_p\otimes F_q\otimes D_{(p\cup q)^c}.
 \end{aligned}
 \tag{5.2}
\]

This identity retains every ordered magnetic history through degree two;
the mixed local coefficient combines the two distinct chronological face
orders rather than dropping either of them.

**Proof.** Every multivariate monomial of total degree two is either
`z_p^2` or `z_pz_q`. By (1.2), its global coefficient is its local
coefficient tensor the free outside operator. This includes local Perron
normalization, since `b_L(z_A,0)=b_A(z_A)`.

For disjoint `p,q`, the entire two-face transfer factorizes, before any
Taylor expansion:

\[
 B_{\{p,q\}}(z_p,z_q)=B_p(z_p)\otimes B_q(z_q),\qquad
 b_{\{p,q\}}(z_p,z_q)=b_p(z_p)b_q(z_q).
\]

The first rotations also factor because their supports are disjoint.
Therefore

\[
 \mathcal E_{\{p,q\}}(z_p,z_q)
 =\mathcal E_p(z_p)\otimes\mathcal E_q(z_q),\qquad
 [z_pz_q]\mathcal E_{\{p,q\}}=F_p\otimes F_q.
 \tag{5.3}
\]

For a repeated face or an overlapping pair the coefficient is precisely
the operator in (3.1). Conjugation by `U_2` changes the quadratic
coefficient only by `[D_L,S_2,L]`, which adds the commutator in (4.1) to
each of these local terms. It does not alter the first coefficient and
does not change the disjoint products. Equations (4.1) and (5.3) prove
(5.2). No all-orders polymer representation was assumed. ∎

As an immediate consequence, both the linear and quadratic coefficients
annihilate the product vacuum on both sides. The quadratic cancellation is
stronger than the first-rotation result alone: the latter can retain an
extensive quadratic vacuum-creation column.

## 6. A rational uniform full-operator bound

### Theorem 6.1. Uniform complete second Taylor coefficient

Under (1.4),

\[
 \boxed{
 \sup_L\big\|[u^2]\widetilde{\mathcal D}_L(u)\big\|
 \le\frac{40432}{5}\,f_*^2.
 }
 \tag{6.1}
\]

The same bound holds after restriction to any reducing gauge/charge/flux
sector. The bound on the actual second derivative is twice (6.1).

**Proof.** If a local self-adjoint `F` annihilates its local vacuum, then
`F=Q_XFQ_X` and

\[
 -\|F\|Q_X\le F\le\|F\|Q_X.
 \tag{6.2}
\]

Tensoring with positive outside free factors preserves this quadratic-form
bound. For a product of two disjoint first-order activities, use its norm
bound times `Q_p Q_q`. The majorants commute with all link vacuum
projections and free link kinetic operators. They can therefore be bounded
by their values on configurations with `n` excited links. This argument
controls all input vectors, not merely a set of source-generated states.

**Repeated face.** At most `4n` faces meet the excited set. Each leaves at
least `max(n-4,0)` excited links outside. Their total contribution is at most

\[
 11f_*^2\,4n\delta^{\max(n-4,0)}\le176f_*^2.
 \tag{6.3}
\]

The maximum of `4n(4/5)^max(n-4,0)` is 16, at `n=4,5`.

**Overlapping pair.** A pair whose union meets the excited set has at
least one member among those `4n` faces. Such a face overlaps at most
twelve other faces. Hence there are at most `48n` relevant unordered
pairs; any double count only increases this upper bound. Their union has
at most seven links. Their total contribution is at most

\[
 22f_*^2\,48n\delta^{\max(n-7,0)}\le7392f_*^2.
 \tag{6.4}
\]

Here `n(4/5)^max(n-7,0)` has maximum 7 at `n=7`. For `n>=7`, the
successive ratio is at most `(4/5)(8/7)<1`.

**Disjoint pair.** Each activity must meet the excited set independently.
There are at most `binom(4n,2)<=8n^2` unordered choices. Their union has
eight links and the product norm is at most `f_*^2`. Thus this contribution
is at most

\[
 f_*^2\,8n^2\delta^{\max(n-8,0)}\le\frac{2592}{5}f_*^2.
 \tag{6.5}
\]

For `n<=8`, the expression without the prefactor eight is at most 64.
At `n=9` it is `81(4/5)=324/5`. For every `n>=9`, the ratio of successive
terms is at most `(4/5)(10/9)^2=80/81<1`. This proves the stated exact
maximum.

Adding (6.3)--(6.5) gives
`176+7392+2592/5=40432/5`. The majorant applies to both signs of the
self-adjoint quadratic form in (5.2), proving (6.1). ∎

The constant is an explicit sufficient bound, not an optimized physical
estimate. Its role is to prove that the second coefficient cannot grow
with the spatial volume or with the dimensions of the link representation
spaces after the second local rotation.

## 7. One vacuum chart works at both temporal block scales

### Proposition 7.1. Positive-integer-block independence of the two generators

Fix the fine transfer `T_A(z)` and `tau`. Construct the local generators
above using any positive integer block `T_A(z)^m`. Both `S_p` and every
`S_A` in (4.1) are independent of `m`.

**Proof.** The first generator in (2.1) depends on `tau` and the calibrated
energy `E_s`, not on `m`. For sufficiently small real couplings all positive
integer powers of `T_A(z)` have exactly the same simple Perron vector.
After the same first rotation and the normalization
`<Omega_X,psi_A>=1`, their Perron vector `psi_A(z)` is identical.
Its analytic continuation near zero is identical as well. Equation (3.3)
identifies

\[
 \chi_A=[z^\alpha]\psi_A(z),
 \tag{7.1}
\]

for each repeated-face or overlapping-pair degree-two monomial. Although
the formula `(1-D_X)^-1 Q_X A Omega_X` contains the block duration in both
factors, their combination equals this common eigenvector coefficient.
Consequently `chi_A` and its anti-Hermitian generator are independent of
`m`. ∎

Thus the two generators can be constructed using the long block convenient
for the vacuum expansion and applied to the short block that maximizes the
guaranteed free excited-window separation. The quadratic **operator
activities** themselves still depend on the block: only the vacuum chart is
common. No identification of a finite-spacing Wilson logarithm with the
Hamiltonian GNS generator follows from (7.1).

## 8. Exact two-level control of the new cancellation

An elementary local model makes the nonlinear repair explicit. Let

\[
 T(u)=e^{uV/2}\begin{pmatrix}1&0\\0&\delta\end{pmatrix}e^{uV/2},
 \qquad V=\begin{pmatrix}0&v\\v&h\end{pmatrix},\qquad0<\delta<1.
\]

For real `v,h`, the first generator is

\[
 S_1=\begin{pmatrix}0&-s_1\\s_1&0\end{pmatrix},\qquad
 s_1=\frac{v(1+\delta)}{2(1-\delta)}.
\]

The first-rotated normalized operator has quadratic vacuum column
`(1-delta) chi_2` in its excited component, where

\[
 \boxed{\chi_2=
 \frac{hv(1+6\delta+\delta^2)}{8(1-\delta)^2}.}
 \tag{8.1}
\]

To check (8.1), the unrotated quadratic off-diagonal coefficient is
`hv(1+3 delta)/8`; the first commutator adds `s_1 delta h`, while the
double commutator is diagonal. Scalar Perron normalization does not alter
this off-diagonal coefficient. Division by `1-delta` gives (8.1).
The second generator

\[
 S_2=\begin{pmatrix}0&-\chi_2\\\chi_2&0\end{pmatrix}
\]

cancels the quadratic column exactly. If the fine magnetic factor is
`exp(tau u V/2)`, replace `v,h` by `tau v,tau h` in these formulas.
By Proposition 7.1 the same generators work for every positive integer
power of that fine transfer.

This control detects the specific failure of retaining only the first
rotation. It does not test an all-orders claim by extrapolation from two
coefficients.

## 9. Relationship to the existing G18 route and the next theorem

The Hamiltonian G18 construction obtains an exact fixed-spacing physical
GNS band by coefficient close projection, coefficient-to-GNS transport,
source totality, and exponentially weighted Gram orthonormalization. Its
analytic symbol then isolates the carrier on patches away from Gamma.
The actual Wilson transfer requires its own operator and source estimates;
the present construction addresses the background-vacuum part directly
without assuming locality of `-log T`.

The new completed step is the exact second-order local chart (4.1), the
complete linked identity (5.2), the uniform full-operator coefficient bound
(6.1), and compatibility of the vacuum chart across both block scales.
All are independent of any fourth-order rest or shape coefficient.

There is now a precise route to higher orders. Introduce independent face
couplings; after lower orders have been vacuum-anchored, restrict each
degree-`r` monomial to its active-face subsystem. Disconnected active-face
components factor exactly because both the actual transfer and all already
constructed local generators factor across disjoint link components.
For a connected residual, the normalized local vacuum equation determines
its vacuum column, and the bounded inverse of `1-D_X` gives the next
anti-Hermitian vacuum-rotation coefficient in the same way as (4.1).

The companion `G18_VACUUM_CHART_RECURSION_20260905.md` now proves the
arbitrary-fixed-order induction, retaining the multivariate lower-order
commutators, factorization and local scalar cancellation explicitly. To
obtain an exact finite-coupling vacuum chart, one must additionally bound the growth
of connected coefficients and the spatial extent of their supports by a
convergent majorant. The spectral transfer theorem from the preceding note
can then use its all-orders anchored-activity norm. A list of finite-order
bounds alone does not supply that convergence.

## 10. Verification and provenance

This note is an additive mathematical derivation using the exact transfer
and calibrated free-window premises in the imported 4 September operator
bridge. Its formulas do not read a numerical target or a retained Wilson
representation matrix. The finite product-transfer coefficient oracle in
this work session is a separate check of the local algebra and support
assembly; its result must be recorded with its own artifact and execution
evidence rather than being inferred from the arguments above.

Primary local dependencies:

- `G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md`: actual symmetric transfer,
  optimal temporal block, first vacuum rotation, full-operator support
  counting, and the all-orders sufficient activity criterion.
- `G19_UNIFORM_WILSON_WINDOW_20260904.md`: calibrated kinetic shell and
  uniform one-link gap, as the upstream physical input.
- `G18_FIXED_SPACING_CARRIER_BRIDGE_INSERT.tex` and its coefficient/GNS and
  internal-sheet inserts: the separate Hamiltonian fixed-spacing band to
  which an eventual Wilson operator-matching theorem must connect.

The sealed run `runs/wilson_vacuum_chart_2026-09-05` supplies executable
evidence. The Lean matrix kernel proves the rank-two cancellation under its
explicit premises; the full operator estimates here remain analytic proofs.
Native records distinguish this completed fixed-order result from the
remaining convergence and physical-source tasks.
