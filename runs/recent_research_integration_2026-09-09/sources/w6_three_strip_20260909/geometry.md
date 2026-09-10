# Original-edge strip geometry and cancellation of the complete first jet

9 September 2026. This calculation differentiates the original Wilson link
variables before choosing tree gauge. The all-length identity in section 5
was obtained after the three-face coefficient exposed its cancellation.

## 1. Ten original edges and their exact fields

Use generators T_a=i sigma_a/2, so [T_a,T_b]=-epsilon_abc T_c. Orient
bottom edges b_i and top edges a_i from column i to i+1, and vertical
edges r_i from bottom to top. Set B_i=b_0 ... b_{i-1}. Based face loops are

    U_i=B_i r_i a_i r_{i+1}^{-1} B_{i+1}^{-1}.

The bottom and vertical edges form the tree. At tree gauge U_i=a_i.
Let L_i generate exp(tT)U_i, R_i generate U_i exp(tT), and G_i=L_i-R_i.
Differentiating each ORIGINAL edge in the loop word gives exactly

    top a_i:       L_i,
    vertical r_0:  L_0,
    vertical r_j:  L_j-R_{j-1}  (1 <= j <= n-1),
    vertical r_n: -R_{n-1},
    bottom b_j:   -R_j + sum_{i>j}(L_i-R_i).
                                                        (E1)

The original electric Hamiltonian is minus one half the sum of squares
of these fields, summed also over the three Lie directions. For n=3 this
includes ten edges. In particular the middle bottom field is
-R_1+L_2-R_2. Dropping it gives the wrong first quantum coefficient.
Its flow and all other fields in (E1) follow directly from the original
single-edge flows, so this identification applies to squares as well.

The physical Hilbert space consists of simultaneous-conjugation invariant
functions. There sum_i G_i=0. This permits bottom b_0=-L_0 on physical
functions but does not permit deleting the other transported derivatives.

The product Haar measure of the n face variables is the gauge-fixed
measure. The exact scalar magnetic potential is 4u sum_i(1-Tr(U_i)/2).

## 2. Complete first weak-field coefficient

Use the chord chart

    U_i=sqrt(1-g^2 |X_i|^2/4) I + i (g X_i/2).sigma,
    g=u^(-1/4),  D_ij=gradient_i cross gradient_j.

Put C_i=X_i cross gradient_i. The scaled invariant fields are

    g L_i=gradient_i - (g/2) C_i + O(g^2),
    g R_i=gradient_i + (g/2) C_i + O(g^2).

Haar flattening is even in g and has no first jet; the scalar magnetic
potential has no first jet either. Applying these expansions to (E1)
gives the complete operator coefficients

    H_0=-1/2 sum_ij C_ij gradient_i.gradient_j + 1/2 sum_i |X_i|^2,
    C_ii=4, C_{i,i+1}=C_{i+1,i}=-1, all other C_ij=0,

    H_1=1/2 sum_{i=0}^{n-2}(X_i+X_{i+1}).D_{i,i+1}
        + sum_{i<j} X_j.D_ij.                            (E2)

There is no additional first-derivative drift at this order. For n=3,

    H_1=(X_0+3X_1).D_01/2
        +(X_1+3X_2).D_12/2 + X_2.D_02.                 (E3)

## 3. True first ground correction of the three-face strip

Let A=C^(-1/2), Omega_0 proportional to
exp[-sum_ij A_ij X_i.X_j/2]. Write

    A=[[a,b,c],[b,d,b],[c,b,a]],
    h=(4-sqrt(2))^(-1/2), l=(4+sqrt(2))^(-1/2),
    a=(h+l+1)/4, c=(h+l-1)/4,
    b=sqrt(2)(h-l)/4, d=(h+l)/2,
    T=X_0.(X_1 cross X_2).

Direct application of the COMPLETE H_1 gives

    H_1 Omega_0=k T Omega_0,
    k=-ab+2b^2+bc-2cd
     =(2h+2l-sqrt(2)h+sqrt(2)l-8hl)/8
     =-0.03831121825264784276825546... .                  (E4)

The Gaussian expectation of T is zero. The ground-transformed H_0-e_0
maps T to lambda T, where

    lambda=Tr(sqrt(C))=sqrt(4-sqrt(2))+2+sqrt(4+sqrt(2)).

This follows because every mixed contracted second derivative of a
determinant vanishes and the linear drift acts by its trace. Therefore

    e_1=0,
    p_1=-(k/lambda)T=(c/2)T
       =0.006455259454822463154393065... T.             (E5)

The coefficient is a true quantum ground correction, not a classical
Gibbs-density correction.

## 4. Independent three-face audit of compatible source transport

The source calculation supplies the skew generator

    K=-1/2 (X_0 cross X_1).gradient_0.                  (E6)

It preserves all |X_i|, has divergence zero, and has a complete rotational
flow. For a_0=|X_0+X_1+X_2|^2/2,

    K a_0=-T/2=a_1,
    K Omega_0=(c/2) T Omega_0=p_1 Omega_0.

Thus it reproduces both the actual first observation jet and the true
first ground jet. The first marginal coefficient is zero by conditional
Gaussian reflection symmetry. The source agent's derivation verifies
that KJ_0 is consequently the complete literal first source jet.

Our independent commutator computation gives

    [H_0,K]=-(2X_0+X_1/2).D_01 + (X_0/2).D_02.

No scalar or first-derivative term is omitted. Put

    r_0=X_1.D_01+X_2.D_02,
    r_1=-X_0.D_01+X_2.D_12,
    r_2=-X_0.D_02-X_1.D_12.

Then the COMPLETE transported first coefficient is

    W_1=H_1-e_1+[H_0,K]=r_0+(3/2)r_1-(1/2)r_2.       (E7)

Each r_i is minus gradient_i.G, with G=sum_j X_j cross gradient_j.
Physical functions satisfy Gf=0. Hence W_1=0 on the entire smooth
physical coefficient core, including physical functions of the odd
triple product. This cancellation does not assume that all physical
invariants are even.

## 5. All-length strip identity

For every n>=2 use the complete generator

    K_n=-1/2 sum_{i<j}(X_i cross X_j).gradient_i.        (E8)

For n=3 this differs from (E6) by X_2.G/2 and so agrees on physical
functions. Each vector field is perpendicular to its own X_i, has zero
divergence, and is equivariant under simultaneous rotations. All norms
|X_i| are conserved, so its polynomial flow is complete. It generates a
unitary coordinate flow for Lebesgue measure and also for the radial
product chord Haar density at each fixed g.

The commutator with H_0 has the following closed symbol (write p_i for
gradient_i):

    [H_0,K_n]
      =1/2 sum_{i<j} sum_k
          (C_ik X_j-C_jk X_i).(p_i cross p_k).          (E9)

The potential commutator vanishes because K_n preserves all norms.
The lower derivative commutator vanishes because contraction of the
cross-product tensor against equal coordinate indices is zero.

Here is a direct coefficient proof for every n. For fixed i<j the
coefficient of D_ij in (E9) is

    (C_ij/2) sum_{b=i+1}^j X_b
    -(X_i/2) sum_{b>i} C_bj
    +(X_j/2) sum_{b>j} C_bi.

The last sum vanishes. If j=i+1, this equals
-(3+1_{j=n-1})X_i/2-X_j/2. If j>=i+2, it equals
-(1+1_{j=n-1}/2)X_i. Adding (E2) yields the exact differential identity

    H_1+[H_0,K_n]
      =-(sum_{i=0}^{n-1} gradient_i
          +(1/2)gradient_{n-1}).G.                    (E10)

Consequently the COMPLETE first transported physical coefficient
vanishes for every finite open strip length:

    W_1|physical=0,
    t_1=Q_0 W_1 J_z=0.                               (E11)

No simplification of the Gaussian graph lift J_z is needed for (E11),
because W_1 vanishes on every physical input, not only retained sources.

For compatibility with the literal outer-loop source, direct SU(2)
product expansion gives

    a_g=4/g^2(1-Tr(U_0 ... U_{n-1})/2)
       =a_0-(g/2) sum_{i<j<k} X_i.(X_j cross X_k)+O(g^2),
    a_0=|sum_i X_i|^2/2.

Applying (E8) to a_0 gives exactly its first coefficient. Since (E10)
annihilates the invariant Gaussian ground, its first perturbation
equation is solved by K_n Omega_0, with zero normalization correction
by skewness. Thus the same transport matches the complete first true
ground and observation jets for every finite strip. The source marginal
first jet vanishes because the full first density-and-observation
change is generated by this measure-preserving flow. These facts supply
the compatible first source jet, not just an electric coordinate change.

## Verification

`verify_geometry.py` checks 45 exact identities: the 30 original-edge
word derivatives (ten edges times three axes), the complete first
electric symbol and drift, the true three-face ground coefficient,
the source-rotation commutator and the differentiated-Gauss cancellation.
`check_general_strip.py` independently builds the all-pair generator and
the electric coefficient and solves the resulting polynomial identity
for n=2,3,4,5,6. All five return precisely (E10). The arbitrary-n proof
is the coefficient calculation above, not extrapolation from those five
checks.

These are exact first-coefficient identities for open strips and their
literal outer-loop source. They do not evaluate the order-g^2 force.
