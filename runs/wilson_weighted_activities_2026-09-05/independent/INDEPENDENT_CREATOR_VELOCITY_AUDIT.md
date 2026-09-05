# Independent audit of the exact creator-velocity unitary

5 September 2026. This is a different excited-sector gauge from the
previous common-filter spectral flow.

Let W=sum_Y a_Y(w_Y), where a_Y(w_Y)=|w_Y><Omega_Y| has exact excited
support Y. Let B=sum_X a_X(b_X), and write Q for removal of the product
vacuum coefficient followed by exact-support decomposition. Define

    T_w b = Q exp(-W) B^* exp(W) Omega.

It is conjugate-linear in b at fixed w. Fix nu>=0 and put

    a=||w||_nu,  M1(w;nu)=sup_i sum_{Y contains i}|Y|exp(nu|Y|)||w_Y||.

If a<=nu, then

    ||T_w b||_nu <= 2 exp(-2(nu-a)) M1(w;nu) ||b||_nu.             (1)

## Exact support accounting

Consider one lowering term a_X(b_X)^*. Creators with support disjoint
from X commute with this term and with all other creators, so their two
exponentials cancel exactly. Only creators whose supports intersect X
remain on its left and right.

A nonzero right product has pairwise disjoint creator supports. Their
union must cover X, since the bra <b_X| is fully excited on every link
of X. Lowering then makes every site of X vacuum. A nonzero left product
may reexcite parts of X or create outside the right union, but it cannot
overlap any surviving excited site outside X.

Consequently every surviving term has one, and only one, exact output
support Z, with

    |Z| = sum_right |Y| + sum_left |Y| - |X|.                    (2)

Entanglement does not change this statement: partial contraction of a
fully excited tensor vector remains in the fully excited tensor factor
on its uncontracted sites. Its norm is bounded by ||b_X|| times the norms
of all creator inputs. There is no sum over 2^|Z| projection patterns.

Write beta_X=exp(nu|X|)||b_X|| and c_Y=exp(nu|Y|)||w_Y||.
Equation (2) gives a factor exp(-2nu|X|) beta_X product_Y c_Y.
For fixed X,

    sum_{Y intersects X} c_Y <= |X| a.

Every root i in a nonempty output Z belongs to at least one of the left
or right creator supports. Marking such an input in the two exponential
series gives the positive upper bound

    2 exp(2|X|a) sum_{Y contains i, Y intersects X} c_Y.

This marking may overcount roots later removed by the lowering operation;
that only enlarges the bound. Summing X and using X nonempty and a<=nu,

    output_root_sum
      <=2 exp(-2(nu-a)) sum_{Y contains i} c_Y
                                    sum_{X intersects Y} beta_X
      <=2 exp(-2(nu-a)) sum_{Y contains i}|Y|c_Y ||b||_nu.

Taking the supremum proves (1). All series are finite creator polynomials
at finite volume; the majorants are volume and dimension independent.

## Inversion, exact vacuum transport and component factorization

If the constant in (1) is theta<1, the equation

    b-T_w b = dot w

has the unique solution sum_{n>=0} T_w^n dot w on the underlying REAL
Banach space, with ||b||_nu<=||dot w||_nu/(1-theta). Conjugate-linearity
is compatible with this real-linear Neumann series; complex linearity
must not be asserted.

Put S=B-B^*, which is anti-Hermitian. Creators commute, so

    exp(-W) S exp(W) Omega = dot W Omega + c Omega,
    c=<Omega, exp(-W) S exp(W) Omega>.

For phi=exp(W)Omega one has dot phi=dot W phi. Therefore the solution of
dot V=S V, V(0)=I obeys

    V(s)Omega = exp(integral_0^s c(t)dt) phi(s),

provided w(0)=0. Unitarity fixes the modulus of this scalar to
1/||phi(s)||. Its imaginary part is only a phase. This is exact transport
of the desired vacuum line, with no global condition-number estimate.

If the creator family splits over disjoint induced components, T_w
preserves the direct sum of their velocity families. Uniqueness of the
inverse gives b=b_A+b_B, hence S=S_A+S_B and V=V_A tensor V_B from the
common initial value. This is the factorization needed for actual
induced-subsystem transfer activities in the replacement chart.

For analytic continuation one must double the unknowns corresponding to
b and its conjugate, rather than interpret T_w as a complex-linear map.
The two coupled equations with independently continued w and conjugate-w
are holomorphic and have a block Neumann inverse whenever both bounds
(1) are below one. On the real slice they reproduce the real-linear
solution by uniqueness. This supplies the appropriate route to the
common-polydisk assertion; it does not identify V with the old filter U.

## The proposed numerical inverse constant

With ||w||_(log 2)<=1/8 and nu=(log 2)/2, one has
M1(w;nu)<=3/16, using n*2^(-n/2)<=3/2 for integers n>=1.
Also a<=1/8<=nu and

    2 exp(-2(nu-a)) <= exp(1/4) < 4/3.

Thus theta<=1/4. If ||dot w||_nu<=1/8, then ||b||_nu<=1/6.
These are conservative scalar bounds, independent of volume and mesh.

The two-chart distinction is substantive: the construction fixes the
actual vacuum and retained symmetries, but changes the excited-sector
unitary. A transfer activity estimate proved using V is not automatically
an estimate of the common-filter U activities.
