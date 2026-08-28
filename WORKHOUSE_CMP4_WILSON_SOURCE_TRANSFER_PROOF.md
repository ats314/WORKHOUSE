# CMP(4): transfer from canonical plaquette creation to the literal Wilson source

**External proof artifact — read-only WORKHOUSE analysis**  
**Date:** 2026-08-22  
**Scope:** infinite volume, fixed spacing, sufficiently small strong-coupling coordinate  
**Status:** closed conditional only on the completed CMP(1)–CMP(3) package; independently refereed after the two decay-quantifier repairs recorded below  
**Repository status:** no file in the read-only WORKHOUSE clone was modified

## Theorem

Assume CMP(1)--CMP(3), in particular that the canonical projected synthesis

\[
T_c e_{x,\alpha}
=P_u^-\pi_u(\widehat w_{x,\alpha})\Omega_u
\]

is an isomorphism from
\(\ell^2(\mathbb Z^3;\mathbb C^3)\) onto the isolated physical
charge-odd Riesz band and that its Gram kernel
\(G=T_c^*T_c\) satisfies \(\|G-I\|_\mu<1\) in an exponentially weighted
convolution algebra.

Let

\[
O^W_{x,\alpha}=\operatorname{ImTr}U_{p(x,\alpha)}
\]

act by multiplication. Choose the fixed phase and normalization \(c_W\) so
that \(c_WO^W_{x,\alpha}\Omega_0=w_{x,\alpha}\), and define

\[
T_W e_{x,\alpha}
=P_u^-\pi_u(c_WO^W_{x,\alpha})\Omega_u.
\]

Then, after shrinking the small-coupling interval if necessary:

1. \(T_W\) is an isomorphism onto the same isolated Riesz band;
2. its Gram kernel is exponentially summable and analytic in a complex
   momentum strip;
3. at every real momentum, the three Wilson plaquette sources have a
   uniformly positive-definite full-band residue matrix.

Thus CMP(4) does not require a new rooted BCH expansion of the Wilson
source.  It follows from local product-vacuum continuity, Yarotsky
clustering, and the already-proved single canonical Riesz mark.

## 1. Exact free-vacuum matching

In the standard Haar-character convention,

\[
w=\frac{\chi_3-\chi_{\bar3}}{\sqrt2},\qquad
\operatorname{Im}\chi_3
=\frac{\chi_3-\chi_{\bar3}}{2i}.
\]

Character orthogonality gives
\(\|\operatorname{Im}\chi_3\|_{L^2(SU(3))}^2=1/2\).  Hence one may take

\[
c_W=i\sqrt2,
\tag{1.1}
\]

up to the phase convention used for \(w\).  Put

\[
D_s:=c_WO_s^W-\widehat w_s,
\qquad s=(x,\alpha).
\tag{1.2}
\]

Both summands are bounded, gauge invariant, charge odd, and supported on
the same fixed three grouped cells \(S_s\).  Most importantly,

\[
D_s\Omega_0=0.
\tag{1.3}
\]

Since \(|\operatorname{ImTr}U|\le3\) and
\(\|\widehat w_s\|=1\), a uniform explicit operator bound is

\[
\|D_s\|\le M_D:=3\sqrt2+1.
\tag{1.4}
\]

## 2. The local difference vector is small

Let
\(Q_s=|\Omega_{S_s,0}\rangle\langle\Omega_{S_s,0}|\).  The local
product-vacuum estimate from CMP(3) gives

\[
1-\omega_u(Q_s)\le2|S_s|g=6g,
\qquad g=27|u|.
\tag{2.1}
\]

Equation (1.3) implies \(D_sQ_s=0\), and therefore

\[
D_s^*D_s
=(1-Q_s)D_s^*D_s(1-Q_s)
\le M_D^2(1-Q_s).
\]

Consequently

\[
\boxed{
\|\pi_u(D_s)\Omega_u\|^2
=\omega_u(D_s^*D_s)
\le6gM_D^2.}
\tag{2.2}
\]

This is a direct bounded-projector estimate; no density matrix or
finite-dimensional onsite space is used.

## 3. Weighted kernel algebra

For a translation-invariant \(3\times3\) kernel \(K(r)\), use the
adjoint-stable Schur norm

\[
\|K\|_{\mu,\sharp}
:=\max\left\{
\max_\alpha\sum_{r,\beta}e^{\mu|r|_1}|K_{\alpha\beta}(r)|,
\max_\beta\sum_{r,\alpha}e^{\mu|r|_1}|K_{\alpha\beta}(r)|
\right\}.
\tag{3.1}
\]

It is submultiplicative under convolution, invariant under adjoint, and
dominates both the \(\ell^2\) convolution norm and the matrix norm of every
real-momentum fiber.  For Hermitian kernels it agrees with the row norm used
in CMP(3).  Denote this unital Banach \(*\)-algebra by
\(\mathcal A_{\mu,\sharp}\).

## 4. The unprojected difference synthesis is small

Let \(J_D e_s=\pi_u(D_s)\Omega_u\), initially for finitely supported
wave packets, and let

\[
K^D_{st}=\langle J_De_s,J_De_t\rangle
=\omega_u(D_s^*D_t).
\]

Charge oddness gives \(\omega_u(D_s)=0\).  For separated supports,
Yarotsky's equation (16) therefore gives

\[
|K^D_{st}|
\le C_0^6M_D^2\tau^{\operatorname{dist}(S_s,S_t)}.
\tag{4.1}
\]

For every pair of labels, Cauchy--Schwarz and (2.2) give the global bound

\[
|K^D_{st}|\le6gM_D^2.
\tag{4.2}
\]

Choose a clustering base \(\tau\) with \(e^\mu\tau<1\), and then make
\(g\) small enough for equation (16) with that base.  Split the weighted
sum into a finite ball and its complement.  Equation (4.2) sends the finite
ball to zero as \(g\to0\), while (4.1) makes the tail uniformly summable and
arbitrarily small.  Hence

\[
\boxed{\|K^D\|_{\mu,\sharp}\longrightarrow0.}
\tag{4.3}
\]

In particular, \(J_D\) extends to \(\ell^2\) and

\[
\|J_D\|^2=\|K^D\|_{\ell^2\to\ell^2}
\le\|K^D\|_{\mu,\sharp}\longrightarrow0.
\tag{4.4}
\]

Projection contraction already proves operator-norm closeness
\(\|T_W-T_c\|\to0\).  The next step strengthens this to a weighted,
every-momentum statement.

## 5. One canonical Riesz mark gives the weighted cross kernel

Set

\[
T_D:=T_W-T_c=P_u^-J_D,
\qquad
C:=T_c^*T_D.
\tag{5.1}
\]

Orthogonality of \(P_u^-\) and coefficient/GNS intertwining give the exact
one-sided identity

\[
\begin{aligned}
C_{st}
&=\langle P_u^-\Gamma_uw_s,P_u^-\pi_u(D_t)\Omega_u\rangle\\
&=\langle\Gamma_u\mathcal P_u^-w_s,\pi_u(D_t)\Omega_u\rangle\\
&=\omega_u(\widehat w_s^{\,*}D_t)
  +\sum_J\omega_u(\widehat c_{s,J}^{\,*}D_t),
\end{aligned}
\tag{5.2}
\]

where

\[
\mathcal P_u^-w_s=w_s+c_s,
\qquad
\sum_Je^{\sigma d(J;S_s)}\|c_{s,J}\|
\le A(u),
\qquad A(u)\to0.
\tag{5.3}
\]

The raw term in (5.2) has the following global small bound by (2.2):

\[
|\omega_u(\widehat w_s^{\,*}D_t)|
\le\|\widehat w_s\Omega_u\|\,\|D_t\Omega_u\|
\le M_D\sqrt{6g}.
\tag{5.4}
\]

For separated roots it also has the equation-(16) bound
\(C_0^6M_D\tau^R\).  For the corrected term, the supportwise symmetry
invariance proved in CMP(1)–CMP(3) makes every exact-support coefficient
charge odd; hence charge oddness kills both one-point functions and forces
the empty scalar coefficient to vanish. At zero support separation use the
trivial operator bound, which is the same estimate with \(\tau^0=1\). For
positive separation use equation (16), while

\[
|J|\le d(J;S_s)+3
\]

absorbs the support prefactor \(C_0^{|J|}\).  Exactly the rooted calculation
used in CMP(3) yields, after choosing the input exponent and clustering base
so that \(e^\mu\vartheta<1\), where
\(\vartheta=\max\{C_0e^{-\sigma},\tau\}\),

\[
\left|\sum_J\omega_u(\widehat c_{s,J}^{\,*}D_t)\right|
\le C_0^6M_DA(u)\,
\vartheta^{\operatorname{dist}(S_s,S_t)}.
\tag{5.5}
\]

The same finite-ball/tail argument, including the bounded root diameter and
the three orientation labels, proves

\[
\boxed{\|C\|_{\mu,\sharp}\longrightarrow0.}
\tag{5.6}
\]

No coefficient expansion of the Wilson vector is used; only the already
proved canonical projected mark is expanded.

## 6. Exact weighted factorization

The canonical Gram operator is

\[
G=T_c^*T_c.
\]

After shrinking \(u\) once more, CMP(3) gives
\(\|G-I\|_{\mu,\sharp}<1\), so
\(G^{-1}\in\mathcal A_{\mu,\sharp}\).  Define

\[
E:=G^{-1}C.
\tag{6.1}
\]

Then \(\|E\|_{\mu,\sharp}\to0\).  Because \(T_c\) is an isomorphism onto
the band,

\[
T_cG^{-1}T_c^*=I_{\operatorname{Ran}P_u^-}.
\]

Using \(C=T_c^*T_D\), we obtain the exact identity

\[
T_cE=T_cG^{-1}T_c^*T_D=T_D.
\tag{6.2}
\]

Therefore

\[
\boxed{T_W=T_c(I+E).}
\tag{6.3}
\]

For \(\|E\|_{\mu,\sharp}<1\), the Neumann series makes \(I+E\) invertible
inside the same weighted algebra.  Hence \(T_W\) is an isomorphism from
\(\ell^2(\mathbb Z^3;\mathbb C^3)\) onto the full isolated Riesz band.

## 7. Every-momentum Wilson residue

The literal Wilson projected Gram kernel factors as

\[
\boxed{
G_W=T_W^*T_W=(I+E)^*G(I+E)
\in\mathcal A_{\mu,\sharp}.}
\tag{7.1}
\]

Thus \(G_W(k)\) is analytic in the corresponding complex momentum strip.
On every real momentum fiber,

\[
G_W(k)\succeq
\lambda_{\min}(G(k))
\bigl(1-\|E(k)\|\bigr)^2I.
\]

In particular,

\[
\boxed{
G_W(k)\succeq
\bigl(1-\|G-I\|_{\mu,\sharp}\bigr)
\bigl(1-\|E\|_{\mu,\sharp}\bigr)^2I>0
\quad\text{for every real }k.}
\tag{7.2}
\]

Accordingly, no nonzero state in the three-dimensional band fiber is dark
to the complete three-source Wilson family.  This does not say that each
individual orientation source overlaps every eigenvector, and a degenerate
crossing has no canonical scalar-sheet labelling.

## 8. Boundary of the result

This closes the fixed-spacing literal-source gate at sufficiently small
strong-coupling coordinate.  It does not:

1. continue the band toward the asymptotically free continuum trajectory;
2. prove a physical mass or residue uniform in lattice spacing;
3. restore \(SO(3)\) or identify continuum spin;
4. replace smearing in practical continuum-regime spectroscopy.

The unnormalized literal source \(O_s^W\) differs from the normalized source
by the fixed nonzero scalar \(c_W=i\sqrt2\). Its Gram lower bound is therefore
the displayed normalized bound divided by \(|c_W|^2=2\), and remains strictly
positive.

The earlier M1--M3 rooted BCH estimates may still be useful for quantitative
operator dressing, but they are not needed for the qualitative fixed-spacing
Wilson residue theorem above.
