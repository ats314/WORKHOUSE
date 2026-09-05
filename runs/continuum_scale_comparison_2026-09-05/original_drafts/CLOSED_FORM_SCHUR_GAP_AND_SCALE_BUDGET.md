# Closed-form Schur reduction and an inverse-fast-energy scale budget

5 September 2026. Outputs-only analytic theorem. This extends the exact
matrix comparison in [the Gaussian memory predecessor](GAUSSIAN_MEMORY_AND_SPECTRAL_MATCHING.md)
to arbitrary nonnegative self-adjoint Hamiltonians. The proof uses closed
quadratic forms, min-max and finite negative index. It does not assume a
Gaussian measure, weak off-diagonal coupling, a bounded Hamiltonian, or an
identification of a configuration fiber with an OS-history complement.

The conclusion is about actual Hamiltonian energies. Square roots occur in
the Gaussian predecessor only because its matrix represents squared normal
frequencies. There is no square root in the energy comparison below.

## 1. Finite retained space: assumptions and exact construction

Let H>=0 be self-adjoint on the complex Hilbert space
`H_total=P direct_sum Q`, and let h be its densely defined closed form.
Initially P is finite dimensional, dim P=n, and every vector of P belongs
to D(h). The orthogonal projections then preserve D(h): subtracting P psi
from psi stays in the form domain. Restrict h to Q and let F be its
self-adjoint form operator. Assume the actual restricted form satisfies

```text
F>=f I_Q,                       f>0.                     (1)
```

This restricted form is closed and densely defined on Q. Its domain is
`D(F^(1/2))=D(h) intersect Q`, and
`D(h)=P direct_sum D(F^(1/2))` as vector spaces. The assumption concerns the
full restricted Hamiltonian form, including the vacuum subtraction and all
interactions present in H.

For p in P, the cross form `q -> h[p,q]` is continuous in the F form norm:
positivity gives `|h[p,q]|²<=h[p]h[q]`. By the Riesz theorem on
`D(F^(1/2))` with norm `||F^(1/2)q||`, there is a unique vector Up in that
space such that the cross term is represented by

```text
h[p,q]=<F^(1/2)Up,F^(1/2)q>,
```

with the inner-product convention used consistently in the polarization.
The map U:P->D(F^(1/2)) is bounded in the form norm, and hence bounded into
Q by (1). This is the rigorous meaning of `U=F^(-1)QHP`. That expression is
only a formal abbreviation unless the vectors p lie in the operator domain
D(H); the proof never assumes they do.

Let A be the finite matrix of h on P and define

```text
K0=A-(F^(1/2)U)*(F^(1/2)U).
```

Completing the form square gives the exact identity

```text
h[p,q]=<p,K0p>+||F^(1/2)(q+Up)||².                       (2)
```

In particular K0>=0, by choosing q=-Up. No entrywise or norm smallness of
U is needed. Formula (2) includes all off-diagonal interactions in H.

Define

```text
M=I_P+U*U,
L=M^(-1/2)K0 M^(-1/2),
Jv=(M^(-1/2)v,-U M^(-1/2)v).                            (3)
```

M is positive and boundedly invertible. J is an isometry and its exact
compressed form is

```text
h[Jv]=<v,Lv>.                                           (4)
```

Thus L is the exact static Schur operator with the induced norm retained.
Its isometric graph J(P) need not reduce H. It need not be an OS-history
range, and no intertwining identity is inferred from (4).

## 2. Exact spectral theorem

Let `0<=mu_1<=...<=mu_n` be the eigenvalues of L. Let lambda_j be the jth
min-max value of H, counting zeros and multiplicities:

```text
lambda_j=inf_(dim S=j, S subset D(h))
              sup_(psi in S, psi!=0) h[psi]/||psi||².
```

If a min-max value lies below the essential spectrum, it is an actual
discrete eigenvalue. Otherwise the terminology is variational level, not
an asserted isolated eigenvalue. For 1<=j<=n,

```text
f mu_j/(f+mu_j) <= lambda_j <= mu_j.                      (5)
```

Moreover H has at most n eigenvalues below f, counting multiplicity, and
no essential spectrum below f. If mu_j<f, both the existence of the jth
discrete eigenvalue below f and its two bounds follow. For mu_j>=f the
lower comparison endpoint is still below f and (5) remains a valid
min-max inequality; discreteness is not thereby asserted.

The upper bound is immediate from the first j eigenvectors of L, embedded
by J. Their norm and h form are exactly those in (4).

For the lower bound fix 0<z<f. Define bounded operators

```text
U_z=U+z(F-z)^(-1)U,
R_z=U*(F-z)^(-1)U,
S(z)=K0-zM-z²R_z.                                       (6)
```

Completing the shifted form gives

```text
h[p,q]-z(||p||²+||q||²)
 = <p,S(z)p>+||(F-z)^(1/2)(q+U_z p)||².                 (7)
```

For a direct verification, set s=q+Up. Then the left side is
`<p,K0p>-z||p||²+<s,(F-z)s>+2z Re<s,Up>-z||Up||²`;
complete the square in s. This proof is valid on the form domain and
uses no product FU as an everywhere-defined operator.

The triangular change `(p,q)->(p,q+U_zp)` is bounded and invertible on the
Hilbert space and preserves the relevant form domains. The second term
in (7) is strictly positive on its fiber. Therefore the maximal dimension
of a negative form subspace is exactly

```text
dim 1_(-infinity,z)(H) = n_-(S(z)).                      (8)
```

The equality is one of inertia under an invertible congruence, not unitary
equivalence of operators. It follows directly by mapping negative
subspaces in (7): projection of a negative subspace onto P is injective,
and completing the fiber to zero realizes every negative subspace of S.

Since F>=f,

```text
0<=R_z<=U*U/(f-z)=(M-I)/(f-z),

M^(-1/2)S(z)M^(-1/2)
 >= L-zI-[z²/(f-z)](I-M^(-1))
 >= L-[zf/(f-z)]I.                                     (9)
```

If `z<f mu_j/(f+mu_j)`, the last form has at most j-1 negative directions,
so H has at most j-1 eigenvalues below z. Increase z to the endpoint to
obtain the lower bound. The zero-mu case follows from H>=0. Equation (8)
also gives at most n spectral directions below every z<f, excluding
essential spectrum below f.

The factor M is necessary, not a cosmetic normalization. For example,

```text
H=[[5,2],[2,1]],   f=1,   U=2,   K0=1,   M=5,   mu=1/5.
```

The actual lower energy `3-2sqrt(2)` lies between 1/6 and 1/5. Omitting M
would falsely give the lower bound 1/2. Large cross terms are allowed by
the theorem, but their induced metric must remain in the coarse operator.

## 3. Vacuum correspondence and the complete gap

Positivity in (2) proves the exact nullspace correspondence

```text
ker H = {(p,-Up):p in ker K0}=J ker L.                   (10)
```

For a nonnegative closed form, zero form energy is equivalent to belonging
to the operator kernel, so this is an operator statement. In particular
the retained space need not contain the actual vacuum vector in advance:
its graph dressing recovers it. Assumption (1) ensures no zero vector can
live entirely in Q, so P is injective on the full vacuum space.

Suppose L has a k-dimensional kernel and its first positive eigenvalue is
mu>0. Then H has exactly k zero eigenvalues, and its complete nonvacuum
gap Delta obeys

```text
Delta >= f mu/(f+mu) = (mu^(-1)+f^(-1))^(-1).            (11)
```

If k<n, also Delta<=mu as a min-max bound. In particular mu<f guarantees
a discrete full excitation below f. If K0=0 on all of P, there is no
positive retained level, but (8) and (10) still show Delta>=f; interpret
the lower formula with mu=infinity. The case P={0} is simply H=F.

The inequality is a bound on every physical excitation in the chosen
Hilbert space, not just a selected source-visible band. Its assumptions
must therefore be established on that entire space. If H is already
restricted to gauge-invariant states, all forms and projections in the
argument belong to that physical space.

## 4. Infinite retained spaces and unbounded coarse forms

The finite-dimensional construction above derives U directly from h. A
useful extension starts instead from the exact factorization as data.
Let P,Q be arbitrary Hilbert spaces, let k0 be a nonnegative densely
defined closed form on P, let F>=f be self-adjoint on Q, and let U:P->Q
be bounded. Set

```text
D(h)={(p,q):p in D(k0), q+Up in D(F^(1/2))},
h[p,q]=k0[p]+||F^(1/2)(q+Up)||².                         (12)
```

This form is closed and densely defined: it is the pullback of the closed
direct-sum form under the bounded invertible triangular map
`(p,q)->(p,q+Up)`. No assumption that U sends every p into D(F^(1/2)) is
needed in this formulation. In particular D(h) need not be a product
domain before the triangular map.

Define the closed normalized coarse form

```text
l[v]=k0[M^(-1/2)v],   D(l)=M^(1/2)D(k0),  M=I+U*U.      (13)
```

Equations (3)-(4), (6)-(10) remain valid as form identities; S(z) is the
closed form k0 minus the displayed bounded terms. The shifted triangular
map respects domains because `(F-z)^(-1)Up` lies in D(F). The same
negative-index proof gives (5) whenever its coarse/full min-max levels
are interpreted variationally. To infer discreteness, a finite spectral
rank below the relevant comparison threshold must be supplied. Infinite
P alone no longer gives the automatic essential-spectrum threshold f.

In particular, if L has a finite-dimensional kernel and a genuine full
gap mu>0 above it, the complete H gap (11) still follows. For any
`0<z<fmu/(f+mu)`, the right side of (9) has exactly k negative directions;
H has at most k directions below z and already has its k-dimensional
kernel. Thus no additional discrete or essential spectral point lies in
that interval. The case L=0 on an infinite retained space is not covered
by this finite-vacuum argument and is not silently included.

This extension is the natural form for an unbounded physical coarse
Hamiltonian. Its exact factorization and bounded U are substantive
analytic assumptions to be proved for an application.

## 5. Exact resolvent memory and the Gaussian specialization

For a real parameter z<f outside the spectrum of H, eliminating the
fiber in the resolvent equation gives, on the retained variables,

```text
P(H-z)^(-1)P = S(z)^(-1),                               (14)
```

whenever the inverse is defined; the formula is understood through the
closed form solution. In particular z<0 is available except for z=0.
The static normalized operator L does not delete the energy-dependent
term `-z²U*(F-z)^(-1)U`. Equation (5) compares the low spectrum while
retaining an exact estimate of that term.

For the Gaussian predecessor use the finite matrix
`H=V=[[C,D],[D*,F]]`, so `U=F^(-1)D*`. Then

```text
K0=C-D F^(-1)D*,
M=I+D F^(-2)D*,
R_z=D F^(-2)(F-z)^(-1)D*.
```

Setting z=-x gives exactly its Euclidean-frequency kernel
`K0+xM-x²D F^(-2)(F+x)^(-1)D*`. Matrix eigenvalues of V are squared
oscillator frequencies, explaining the square roots there. For an actual
Hamiltonian H satisfying (12), (5) concerns energies directly. Neither
case identifies J(P) with an actual history pullback range.

## 6. Complete low-window transport by graph sources

There is a stronger source statement than individual eigenvector overlap.
Let `Pi=1_[0,E](H)` for `0<=E<f`, and let J be the graph isometry in (3).
The spectral theorem gives `ran Pi subset D(H)` and
`||H psi||<=E||psi||` on that entire range, even if it is infinite dimensional.

Write psi=(p,q). Testing its operator/form equation against all
`(0,q')`, `q' in D(F^(1/2))`, gives

```text
q+Up in D(F),       F(q+Up)=Q H psi,
q+Up=F^(-1)Q H psi.                                     (15)
```

This follows from the defining criterion for the form operator F. It is
valid even in (12), where U need not send every p separately into D(F^(1/2)).
Only q+Up is differentiated by F. Therefore

```text
dist(psi,ran J) <= ||psi-(p,-Up)||
               = ||q+Up|| <= (E/f)||psi||.              (16)
```

Since JJ* is the orthogonal graph projection,

```text
[1-(E/f)²] Pi <= Pi J J* Pi <= Pi.                      (17)
```

Let B=Pi J:P->ran Pi. Its frame operator BB* is boundedly invertible on
ran Pi. Thus B is onto the entire low spectral window, without an
infinite-rank dimension argument. The canonical right inverse is

```text
B^*(B B*)^(-1),     norm <= [1-(E/f)²]^(-1/2).           (18)
```

The projected vectors of any orthonormal basis of P form a frame with
lower bound `1-(E/f)²` and upper bound one. This is whole-window source
transport, not only nonzero overlap of selected vectors. The graph sources
are determined by the full Hamiltonian through U. They have not been
identified with literal Wilson observables, renormalized coarse sources,
or the image of an OS-history map. Establishing such an identification or
a controlled perturbation of these source vectors is a separate task.

For an eigenvector of energy lambda, (15) reduces to the exact identity
`q+Up=lambda F^(-1)q`. At zero energy it recovers (10).

## 7. A concrete conditional scale implication

Suppose a sequence of vacuum-subtracted physical Hamiltonians is compared
in common physical energy units. At step j, suppose the fine Hamiltonian
has the exact form (12), with a full fast bound `F_j>=f_j>0`, a bounded
map U_j, a finite-dimensional vacuum, and normalized Schur operator L_j.
Suppose the actual coarse comparison proves

```text
gap(L_j)>=Delta_j,
```

where Delta_j is an established full coarse physical gap. Exact unitary
identification of L_j with that coarse Hamiltonian is one sufficient way
to obtain this premise, but is not assumed without proof. Then (11) gives

```text
Delta_(j+1)^(-1) <= Delta_j^(-1)+f_j^(-1),
Delta_J >= [Delta_0^(-1)+sum_(j<J) f_j^(-1)]^(-1).       (19)
```

Thus a positive initial gap and a summable inverse-fast-energy budget
suffice for a uniform positive fine gap. For example, if in the same
physical clock `f_j>=c/a_j` and `a_j=a_0 b^(-j)` with b>1, then

```text
sum_j f_j^(-1) <= (a_0/c)/(1-b^(-1)) < infinity.          (20)
```

This does not ask boundary off-diagonal terms to be small. Their complete
effect enters K0 and M. It does require the exact or controlled coarse
spectral comparison; calling K0 alone the effective Hamiltonian would
miss M and invalidate the recursion. If that comparison has errors or
running energy prefactors, they must be included before iterating (19).

For Wilson theory, the new finite-cell and boundary calculations provide
concrete candidates for the fast scale and quadratic Schur geometry.
They do not yet prove a uniform nonlinear F_j bound, bounded dressing U_j,
the exact coarse comparison, or its compatibility with the physical
history measure and sources. These are now precise sufficient spectral
obligations. A uniform gap from (19) would still need a nontrivial
continuum correlation limit and the field-theory axioms to settle Clay.

## 8. Evidence boundary

The theorem is the closed-form calculation and spectral argument above.
The fresh [exact control](check_closed_form_schur.py), with saved
[JSON](check_closed_form_schur.json), checks the necessity of M, the complete
shifted-square identity, nullspace dressing, inertia and the energy bounds
in concrete noncommuting matrices. It also checks the entire rank-two
graph-source window by exact principal minors and rank, plus the scalar
inverse-gap recursion. The replay uses only SymPy and standard libraries.
Such controls do not prove an actual Wilson scale factorization or the
infinite-dimensional analytic theorem.
