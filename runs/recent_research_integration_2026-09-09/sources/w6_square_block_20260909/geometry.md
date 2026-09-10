# The original twelve-edge 2-by-2 SU(2) Wilson block

9 September 2026. All fields below are obtained by differentiating the
original edge words before fixing the tree. This is a square block with
four faces, not a chain of four faces.

## Exact tree geometry

Vertices are (x,y), x,y in {0,1,2}. Orient horizontal edges rightwards and
vertical edges upwards. Choose as tree all six vertical edges and the
two bottom horizontal edges b_0,b_1. Let

    P_(x,y)=b_0 ... b_(x-1) v_(x,0) ... v_(x,y-1).

The four based non-tree horizontal variables are

    U_(x,y)=P_(x,y) h_(x,y) P_(x+1,y)^(-1), y=1,2.

Use the order 0=(0,1), 1=(1,1), 2=(0,2), 3=(1,2). The face traces are
those of U_0, U_1, U_2 U_0^(-1), U_3 U_1^(-1); the outer boundary trace
is w=Tr(U_2 U_3)/2. Product Haar is the gauge-fixed measure.

With L_i and R_i defined as exp(tT)U_i and U_i exp(tT), T=i sigma/2,
the ORIGINAL edge fields are:

| Original edge | Induced field |
|---|---|
| h_(0,1) | L_0 |
| h_(1,1) | L_1 |
| h_(0,2) | L_2 |
| h_(1,2) | L_3 |
| v_(0,0) | L_0+L_2 |
| v_(0,1) | L_2 |
| v_(1,0) | L_1+L_3-R_0-R_2 |
| v_(1,1) | L_3-R_2 |
| v_(2,0) | -R_1-R_3 |
| v_(2,1) | -R_3 |
| b_0 | -R_0-R_2+(L_1-R_1)+(L_3-R_3) |
| b_1 | -R_1-R_3 |

The electric operator is -1/2 times the sum of squares, including the
three Lie directions. Its exact face magnetic potential is

    4u [4-Tr(U_0)/2-Tr(U_1)/2
          -Tr(U_2 U_0^(-1))/2-Tr(U_3 U_1^(-1))/2].

## Complete Gaussian and first coefficients

Use g=u^(-1/4) and the same chord charts
U_i=sqrt(1-g^2|X_i|^2/4)I+i(gX_i/2).sigma. Write D_ij=gradient_i cross
gradient_j. The normalized operator has

    H_0=-1/2 sum_ij C_ij gradient_i.gradient_j
          +1/2 sum_ij M_ij X_i.X_j,

    C=[[ 4,-1, 3,-1],
       [-1, 4,-1, 3],
       [ 3,-1, 6,-2],
       [-1, 3,-2, 6]],

    M=[[ 2, 0,-1, 0],
       [ 0, 2, 0,-1],
       [-1, 0, 1, 0],
       [ 0,-1, 0, 1]].                                  (S1)

The complete first coefficient is

    H_1=(X_0+3X_1).D_01/2
        +(-X_0+X_2).D_02/2
        +(X_0+3X_3).D_03/2
        -(3X_1+X_2).D_12/2
        +(-X_1+X_3).D_13/2
        +(X_2+2X_3).D_23.                               (S2)

The magnetic and Haar first coefficients vanish. There is no extra
first-derivative electric drift: every such contribution contracts a
cross-product tensor with equal coordinate indices and is zero.

For reproducibility, if a scaled edge field is d_i gradient_i+g e_i
(X_i cross gradient_i)+O(g^2), the two coefficient matrices are

    C=sum_edges d d^T,
    N=sum_edges d e^T
      =[[0,3/2,1/2,3/2],
        [-1/2,0,-1/2,1/2],
        [1/2,3/2,0,2],
        [-1/2,1/2,-1,0]],

and H_1=sum_(i<j)(N_ij X_j-N_ji X_i).D_ij.

The literal retained trace has

    a_g=4/g^2 (1-w)=|X_2+X_3|^2/2+O(g^2),

so its first cubic coefficient is zero in these based chord coordinates.
This does not make H_1 zero on physical functions; four loop vectors
admit independent oriented triple products.

## Exact cancellation of retained second derivatives

For any g before expanding, let Omega be the true positive quantum
ground and let L=Omega^(-1)(H-E)Omega. Let P be conditional expectation
onto w in Omega^2 times product Haar and Q=I-P.

Only the eight original boundary edges differentiate w. The two middle
horizontal edges and the two central vertical edges annihilate it. Each
boundary contribution is an invariant derivative of the same product
trace. Therefore, with Gamma(f,h)=sum_edges,axes (Y f)(Y h),

    Gamma(w,w)=2(1-w^2),
    sum_edges,axes Y^2 w=-6w.                           (S3)

The chain rule gives the exact complete ground-transformed source

    Q L P p(w)=-Q[Gamma(log Omega,w)] p'(w).             (S4)

Both the p'' term and the Casimir p' term depend only on w and disappear
under Q. Formula (S4) retains the full true vacuum and all shared-edge
electric derivatives. It is an exact identity, prior to coefficient or
inverse-energy estimates.

## Independently reconstructed complete first force

For the true Gaussian ground, let A solve A C A=M with A positive, so
Omega_0 is proportional to exp[-sum A_ij X_i.X_j/2]. The source calculation
provides the complete compatible generator

    K=[X_0 cross (alpha X_2+beta X_3)].gradient_0
       -[X_1 cross (beta X_2+alpha X_3)].gradient_1,
    alpha=-13/56-sqrt(2)/28,
    beta=-1/56+sqrt(2)/28.

It has zero divergence, preserves a_0=|X_2+X_3|^2/2, and satisfies

    K Omega_0=p_1 Omega_0,
    p_1=c(T_012+T_013)+d(T_023+T_123),
    c=-1/8+sqrt(6)/24,
    d=-3/56-sqrt(2)/56+sqrt(6)/48,
    T_ijk=X_i.(X_j cross X_k).

We independently applied the original H_1 and H_0 to verify the complete
first true-ground equation (H_0-e_0)(p_1 Omega_0)+H_1 Omega_0=0. We then
computed the full commutator, including its scalar potential part, and
verified W_1 Omega_0=0 for W_1=H_1+[H_0,K].

Acting on every smooth radial retained source gives the explicit result

    W_1[Omega_0 phi(a_0)]
      =Omega_0 [(sqrt(2)-4)/7]
          (T_023+T_123) phi'(a_0).                    (S5)

The coefficient of phi'' is identically zero. The right side has zero
conditional Gaussian mean, because the triple product changes sign
under a simultaneous spatial reflection fixing X_2+X_3. It is therefore
already Q_0 projected.

In this square geometry the Gaussian graph lift needs no correction.
Indeed set face variables Y=B X where

    B=[[1,0,0,0],[0,1,0,0],[-1,0,1,0],[0,-1,0,1]].

Then the face electric matrix is

    B C B^T=[[4,-1,-1,0],[-1,4,0,-1],
             [-1,0,4,-1],[0,-1,-1,4]].

The uniform face mode has eigenvalue 2, and
X_2+X_3=Y_0+Y_1+Y_2+Y_3. The radial retained space hence reduces H_0,
so J_z=J_0 and (S5) is precisely the nonzero first physical force t_1.
For example phi(a)=a produces a nonzero physical triple-product source.

## Verification

`verify_square_geometry.py` checks 71 exact identities, including every
one of the twelve original edge words in all three Lie directions,
the complete electric cometric and first coefficient, all four magnetic
cubic coefficients, and the literal outer trace first coefficient.
It also verifies all eight boundary Casimirs, the four internal-edge
annihilations, and the exact carré du champ and Laplacian in (S3).
The magnetic matrix is built directly as B^T B from the four face
linearizations. `square_geometry_checks.json` records the results.

`verify_complete_force_geometry.py` independently checks nine exact
identities for the full Gaussian Riccati equation, retained reducing
mode, complete source generator, true first-ground equation, ground
annihilation, second-derivative cancellation and the force decomposition
(S5). Its results are in `complete_force_geometry_checks.json`.
