# Actual 2x2 block: complete source unitary and irreducible first interaction

9 September 2026. The block is the actual twelve-edge square with four
faces. Its tree and electric first jet are independently derived in
`geometry.md`. Coordinates X0,X1 are the two middle horizontal holonomies;
X2,X3 are the top horizontal holonomies. The outer observation is U2 U3.

## 1. Quadratic quantum operator and the literal source

The complete quadratic matrices are

    C=[[4,-1,3,-1],[-1,4,-1,3],[3,-1,6,-2],[-1,3,-2,6]],
    M=[[2,0,-1,0],[0,2,0,-1],[-1,0,1,0],[0,-1,0,1]],
    H0=-1/2 sum Cij grad_i.grad_j+1/2 sum Mij Xi.Xj.

Put qb=(X0+X1)/sqrt(2), qt=(X2+X3)/sqrt(2),
rb=(X0-X1)/sqrt(2), rt=(X2-X3)/sqrt(2). In the ordered pairs
(qb,qt) and (rb,rt), C has blocks [[3,2],[2,4]] and [[5,4],[4,8]],
and M has the same block [[2,-1],[-1,1]] twice.

The positive Gaussian ground matrix A, characterized by A C A=M, has blocks

    Aplus=[[1,-1/2],[-1/2,(1+sqrt(2))/4]],
    Aminus=[[sqrt(6)/3,-sqrt(6)/6],
            [-sqrt(6)/6,(sqrt(6)+3)/12]].                       (Q1)

Thus Omega0=constant exp(-X.A.X/2). The ground drift B=C A has blocks

    Bplus=[[2,-1/(2+sqrt(2))],[0,sqrt(2)]],
    Bminus=[[sqrt(6),-1/(sqrt(6)+2)],[0,2]].                    (Q2)

The four oscillator frequencies are sqrt(2),2,2,sqrt(6). The literal
outer trace has

    ag=4(1-Tr(U2 U3)/2)/g^2=a0+O(g^2),  a0=|qt|^2.           (Q3)

For a radial retained function phi(a0), the exact Gaussian action is

    Omega0^-1(H0-e0)[Omega0 phi]
      =-8a0 phi''+(2sqrt(2)a0-12)phi'.                        (Q4)

The retained Gaussian source therefore reduces H0, despite the coupled
four-vector metric. Its marginal has qt covariance sqrt(2) I and
E[a0]=3sqrt(2). Consequently the Gaussian graph equals the source
injection: J_z=J0 on its domain.

## 2. Complete first ground and true marginal

Write Tijk=Xi.(Xj cross Xk). The actual H1 is given in `geometry.md`.
Its action on the Gaussian has coefficients

    H1 Omega0/Omega0 = h(T012+T013)+j(T023+T123),
    h=-sqrt(3)/12+sqrt(6)/24+sqrt(2)/8,
    j=-sqrt(3)/24+sqrt(6)/48+sqrt(2)/8.

Solving the exact four-dimensional cubic oscillator equation gives

    p1=c(T012+T013)+d(T023+T123),
    c=-1/8+sqrt(6)/24,
    d=-3/56-sqrt(2)/56+sqrt(6)/48,
    Psi_g=Omega0(1+g p1+O(g^2)), e1=0.                       (Q5)

Here e1=0 and ground normalization follow from reflection parity. The
Haar half-density has zero first jet, the literal outer observation has
a1=0, and E[p1|a0]=0. Hence the full true marginal has m1=0 and

    J1 phi=Omega0 p1 phi(a0).                                (Q6)

## 3. Explicit complete source-compatible unitary

Set

    alpha=-13/56-sqrt(2)/28,  beta=-1/56+sqrt(2)/28,
    K=[X0 cross (alpha X2+beta X3)].grad_0
       -[X1 cross (beta X2+alpha X3)].grad_1.                 (Q7)

This vector field fixes X2,X3. It rotates X0 and X1 independently about
fixed top-vector axes, preserves each radius, and has zero divergence.
Its flow is complete and measure preserving for all flow times. It
therefore defines a full unitary group on flat L2(R12), preserving
simultaneous SO(3) invariance.

Exact coefficient comparison gives

    K a0=0,  K Omega0=p1 Omega0,  K J0=J1.                  (Q8)

The complete first transported physical operator is therefore the fully
specified operator W1=H1+[H0,K]. In particular W1 Omega0=0. This choice
fixes its Q-Q action, while matching the actual source jet; it does not
replace the quantum ground by a classical density.

## 4. Why the open-strip cancellation fails here

Consider the entire homogeneous quadratic SO(3)-equivariant vector-field
ansatz

    Kgen=sum_{k=0}^3 sum_{i<j} alpha_(kij)
                       (Xi cross Xj).grad_k.                (Q9)

These are all quadratic equivariant vector fields, and all are divergence
free. For one basis term, its kinetic commutator is

    [Hkin,(Xi cross Xj).grad_k]
       =sum_s (Cjs Xi-Cis Xj).(grad_k cross grad_s).          (Q10)

The physical second-order relations are multiples of
sum_j Xj.(grad_i cross grad_j), which vanish by differentiating the
Gauss rotation constraint. Solving all twenty-four operator-symbol
coefficients exactly, with four Gauss multipliers, gives rank 24 and a
four-parameter affine family of kinetic normal forms.

For EVERY member of this family the following cubic defects are fixed:

    Kgen V0=(T023+T123)/32,
    Kgen a0=(T023+T123)/8.                                   (Q11)

Thus no such kinetic normal form preserves either the quadratic magnetic
potential or the first literal outer source coefficient. Adding either
constraint gives coefficient rank 24 and augmented rank 25. This is a
specific obstruction to the open-strip first-order cancellation, not an
obstruction to applying the source-compatible K in (Q7).

The first transported force must therefore be computed with (Q7), keeping
the residual first physical interaction. The companion force calculation
does exactly that.

## 5. Verification and scope

`source_solver.py` solves the full rational coefficient system in (Q9)-
(Q11). `source_ground.py` solves the true cubic ground equation and the
four fixed-top rotation coefficients exactly over the radical field.
`verify_source.py` controls the displayed closed forms and identities.

All statements about the compact model here concern its fixed-cell
weak-field coefficients on the admissible smooth core. The full R_g flow
in (Q7) exists on the Gaussian space, but identifying it with finite-g
literal compact source transport beyond its stated jet would require
the higher source coefficients as well.

## 6. Complete Gaussian differential normal form

Use independent Gaussian modes

    q=qt, u=qb-qt/2, s=rt, v=rb-rt/2.

Their ground matrix is diagonal with entries

    aq=sqrt(2)/4, au=1, as=1/4, av=sqrt(6)/3.

For a term Yl.Dij define its Gaussian conjugated differential part by

    B(Yl.Dij)=Yl.[Dij-ai Yi cross grad_j+aj Yj cross grad_i].

The full physical first operator, including its ground/source transport,
is exactly

    W1tilde=B(S),
    S=Acoef s.Dqu+Bcoef q.Dus+Ccoef q.Dqs
                         +Dcoef(q.Dqv-u.Duv),
    Acoef=(2sqrt(2)-1)/7, Bcoef=(sqrt(2)-4)/14,
    Ccoef=(4-sqrt(2))/7, Dcoef=sqrt(2)/4.                     (Q12)

This is an equality on physical functions; four Gauss divergences were
subtracted from the full twenty-four second-order coefficients. The
zeroth-order term is zero because W1 Omega0=0.

Put T=q.(u cross s), a=|q|^2 and define

    P=W1tilde T
      =Acoef[2|s|^2-aq(a|s|^2-(q.s)^2)
                        -(|u|^2|s|^2-(u.s)^2)]
       +Bcoef[2a-(a|u|^2-(q.u)^2)
                        -as(a|s|^2-(q.s)^2)]
       +Ccoef[-2q.u+as((q.u)|s|^2-(q.s)(u.s))]
       +Dcoef av[2(q.u)(v.s)-(q.s)(v.u)-(u.s)(v.q)].          (Q13)

For every smooth scalar function psi,

    W1tilde[T psi(a)]
      =P psi(a)+2Acoef[a|s|^2-(q.s)^2-T^2]psi'(a).          (Q14)

There is no psi'' term. The retained radial derivative appears only once
in each second-order coefficient in (Q12).

The source force and its full inverse take the form

    t1 phi/Omega0=delta T phi'(a),
    delta=sqrt(2)(sqrt(2)-4)/7,
    R0 t1 phi/Omega0=delta T psi(a),
    psi=[-8a partial_a^2+(2sqrt(2)a-20)partial_a
                                  +(sqrt(2)+4)]^-1 phi'.   (Q15)

This inverse includes the retained angular-one radial energy and the
two fast frequencies 2+2. The independent fast variances are
E[u_i^2]=1/2, E[s_i^2]=2, E[v_i^2]=sqrt(6)/4. Hence

    E[P|q]=Acoef(6-sqrt(2)a),
    E[a|s|^2-(q.s)^2-T^2|q]=2a.

The complete first residual coefficient is therefore explicit for every
radial source in the corresponding core:

    rho1/Omega0
      =delta { [P-Acoef(6-sqrt(2)a)]psi(a)
          +2Acoef[a|s|^2-(q.s)^2-T^2-2a]psi'(a) }.          (Q16)

The bounded inverse in (Q15) is applied before either residual profile
is estimated. This formula uses the full first transported operator,
not only its action on a retained source.
