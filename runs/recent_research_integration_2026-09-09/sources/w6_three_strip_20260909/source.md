# Three-plaquette strip: complete source transport and first-order cancellation

9 September 2026. This note fixes an explicit full unitary first jet for
the actual based ten-edge strip, including the true quantum ground and
the literal outer observation. Indices are 0, 1, 2.

## 1. Literal first source coefficient

Use the chord chart

    Ui = sqrt(1-g^2|Xi|^2/4) I + i(g Xi/2).sigma,
    S = X0+X1+X2,  a0=|S|^2/2,  T=X0.(X1 cross X2).

For the convention Ta=i sigma_a/2, quaternion multiplication has vector
part xw+yv-v cross w. Consequently

    Tr(U0 U1 U2)/2 = 1-g^2|S|^2/8+g^3 T/8+O(g^4),
    ag = 4(1-Tr(U0 U1 U2)/2)/g^2 = a0-g T/2+O(g^2).       (S1)

The nonzero odd observation jet is therefore a1=-T/2.

Let C have diagonal 4 and adjacent off-diagonal -1, A=C^(-1/2), and

    H0=-1/2 sum Cij grad_i.grad_j + 1/2 sum |Xi|^2,
    Omega0=constant exp[-1/2 sum Aij Xi.Xj],
    lambda=tr(sqrt(C)).

The independently derived full electric first jet is

    H1=1/2 (X0+3X1).D01 + 1/2 (X1+3X2).D12 + X2.D02,
    Dij=grad_i cross grad_j.                                  (S2)

The full Haar half-density has zero first jet, and the magnetic potential
is even in this chart. Write A=[[a,b,c],[b,d,b],[c,b,a]]. Then

    H1 Omega0=k T Omega0,
    k=-ab+2b^2+bc-2cd=-lambda c/2.

Since (H0-e0)(T Omega0)=lambda T Omega0, the normalized true-ground jet is

    Psi_g=Omega0(1+g p1+O(g^2)),  p1=c T/2,  e1=0.             (S3)

The ground probability Omega0^2 and a0 are invariant under simultaneous
orthogonal reflection of all Xi. T changes sign. Thus

    E[p1 | a0]=0,  E[a1 | a0]=0.

The first true marginal correction is zero, including observation drift:
mu1=2 mu0 E[p1|a0]-partial_a(mu0 E[a1|a0])=0. The complete literal source
jet on the smooth coefficient core is therefore

    J1 phi = Omega0 T[(c/2)phi(a0)-(1/2)phi'(a0)].             (S4)

## 2. An explicit full unitary extension

Define the real vector field and its differential generator

    V0=-(X0 cross X1)/2,  V1=V2=0,
    K=-(1/2)(X0 cross X1).grad_0.                              (S5)

The vector field is divergence free. Its flow rotates X0 about the fixed
axis X1 at angular speed |X1|/2, keeping X1 and X2 fixed. It is complete
and preserves Lebesgue measure and simultaneous SO(3) invariance.
Pullback along this flow supplies an actual strongly continuous unitary
group R_g=exp(gK) on flat L2(R9), preserving the physical subspace.
In particular this specifies K on Q as well as P; no unspecified Q-Q
extension enters the nonreducing Gaussian graph calculation.

Direct differentiation gives

    K a0=-T/2,  K Omega0=(c T/2)Omega0,
    K[Omega0 phi(a0)]=J1 phi.                                 (S6)

Thus R_g agrees with the complete literal source through first order.
As with the finite-cell weak-field expansion, this is a statement about
the actual source coefficient on its core. It does not identify the
finite-g compact and noncompact source ranges globally.

## 3. Complete first physical operator cancellation

The source-straightened operator has complete first coefficient

    W1=H1+[H0,K].                                             (S7)

The potential commutes with K because K preserves |X0|. Direct
differentiation of the full coupled kinetic energy gives

    [H0,K]=-(2X0+X1/2).D01+(X0/2).D02.                        (S8)

For any smooth physical invariant f, its total rotation generator

    Lf=(sum Xi cross grad_i)f=0.

Taking divergences grad_i.Lf yields the three exact identities

    (X1.D01+X2.D02)f=0,
    (-X0.D01+X2.D12)f=0,
    (-X0.D02-X1.D12)f=0.                                     (S9)

Combining (S2) and (S8) gives precisely

    W1=(X1.D01+X2.D02)
       +(3/2)(-X0.D01+X2.D12)
       -(1/2)(-X0.D02-X1.D12).                               (S10)

Therefore

    W1 f=0 for every smooth physical invariant f.             (S11)

This includes the odd invariant T. It is not the two-vector parity
argument: H1, p1, and J1 are individually nonzero here. They cancel in
the complete source-compatible physical operator.

Consequently, whenever the reference Gaussian graph J_z is defined on
the physical source core,

    t1=Q W1 J_z=0.                                           (S12)

No reducing-source assumption is used in this implication. The first
force in W6 vanishes for this strip and specified compatible first jet.
The next possible transported coefficient is second order; the result
does not discard it or supply its interacting remainder estimate.

## Verification

`verify_source.py` independently checks the source scalar expansion,
the vector-field action, the complete commutator identity, and the
physical cancellation on Gram invariants and triple-product polynomial
tests. The proof (S9)-(S11) applies to the entire physical smooth core;
the finite polynomial tests are independent controls, not its scope.

## 4. Closed source and ground formula for every open strip length

For n faces indexed 0,...,n-1, put A=C_n^(-1/2), where C_n has diagonal
4 and adjacent off-diagonal -1, and write Tijk=Xi.(Xj cross Xk). Expansion
of the ordered quaternion product gives

    ag=a0+g a1+O(g^2),
    a0=|sum Xi|^2/2,
    a1=-(1/2) sum_{i<j<k} Tijk.                               (S13)

A compatible full generator is

    K_n=-(1/2) sum_{i<j}(Xi cross Xj).grad_i.                  (S14)

It is divergence free and its triangular flow preserves each |Xi|:
the last vector is fixed, the preceding vector rotates under its bounded
field, and induction gives existence for all flow times. Thus it defines
a genuine unitary group for every finite n, preserving the physical
subspace. No norm uniformity in n is inferred for this generator.

In the action of K_n on a0, the three ordered pairs belonging to each
triple have signs +,-,+. Hence K_n a0=a1. Similarly

    K_n Omega0/Omega0
      =(1/2) sum_{i<j,k} Aik (Xi cross Xj).Xk
      =(1/2) sum_{i<j<k} Aik Tijk.                            (S15)

The reduction uses Aij=Aji: the other two contributions for a fixed
triple are -Aij and Aji and cancel.

The geometry calculation proves that H1+[H0,K_n] is a sum of derivatives
of the total Gauss generator on every such open strip. Consequently the
complete normalized ground coefficient is explicitly

    p1=(1/2) sum_{i<j<k} Aik Tijk,  e1=0.                    (S16)

Indeed H1 Omega0=-(H0-e0)K_n Omega0; moreover K_n Omega0 is orthogonal to
Omega0 by either unitarity or reflection parity. Uniqueness of the
orthogonal oscillator ground correction supplies (S16).

The same reflection argument gives E[p1|a0]=E[a1|a0]=0 and m1=0. Therefore

    J1 phi=Omega0[p1 phi(a0)+a1 phi'(a0)]=K_n J0 phi.         (S17)

Thus the all-length cancellation is source compatible, with the true
ground and true marginal included. It is not obtained by choosing a
unitary that changes the stated first source jet. For n=3, K_n differs
from (S5) by a multiple of the physical rotation generator and therefore
has the same action on every invariant function.
