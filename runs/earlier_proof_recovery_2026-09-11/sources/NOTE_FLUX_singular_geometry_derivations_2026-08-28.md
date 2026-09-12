# Singular geometry: four new flux-band derivations

**Date:** 2026-08-28  
**Role:** analytic derivation note, not yet promoted to `theory/theorems/`  
**Authority used:** `corpus/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md` and
`corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md`

## 0. Scope and status

This note derives consequences of two inputs already established in the authority
stack:

1. the exact incidence symbol and flat projector
   \(P_{\rm flat}(k)=w(k)w(k)^\dagger/q_a(k)\);
2. the generic fourth-order cubic shape
   \[
   \Delta(k)=Aq_a+Be_2+4C\frac{e_2}{q_a}+D\frac{e_3}{q_a}.
   \]

The derivations do **not** select either disputed physical SU(3) fourth-order
kernel. Results about the generic shape are analytic identities conditional only
on the displayed symbol. The second-order rank-volume result and the incidence
projector result are unconditional within the retained one-plaquette sector.

A repository-wide exact-text search found the ingredients, the statement that the
two-invariant band is \(C^1\) but not \(C^2\), and the qualitative \(r^{-3}\)
projector tail. It did not find the regularity trichotomy, equal-ray extraction,
uniform-frame obstruction, tensorial tail coefficient, or joint rank-volume
monotonicity below. Thus "new" here means new to the local corpus, not a claim of
priority over the mathematical literature.

---

## 1. Exact regularity trichotomy of the four-shape quotient

Write

\[
a_i=4\sin^2(k_i/2),\qquad q_a=a_1+a_2+a_3,
\qquad e_2=\sum_{i<j}a_i a_j,\qquad e_3=a_1a_2a_3.
\]

For \(k=tn\), \(|n|=1\), put

\[
s_4=\sum_i n_i^4,\qquad s_6=\sum_i n_i^6,
\qquad p=\sum_{i<j}n_i^2n_j^2,\qquad r=n_1^2n_2^2n_3^2.
\]

Taylor expansion gives

\[
\begin{aligned}
q_a&=t^2-\frac{s_4}{12}t^4+O(t^6),\\
e_2&=p\,t^4-\frac{s_4-s_6}{12}t^6+O(t^8),\\
e_3&=r\,t^6+O(t^8).
\end{aligned}
\]

Consequently the complete radial expansion through quartic order is

\[
\boxed{
\begin{aligned}
\Delta(tn)
={}&t^2\bigl(A+4Cp\bigr)\\
&+t^4\left[
-\frac{A}{12}s_4+Bp
+\frac{C}{3}\bigl(ps_4-s_4+s_6\bigr)+Dr
\right]+O(t^6).
\end{aligned}}
\tag{1.1}
\]

### Theorem 1 (regularity trichotomy)

At \(\Gamma\), the four-shape coefficient has exactly the following generic
regularity:

1. If \(C\ne0\), then \(\Delta\in C^{1,1}\) but \(\Delta\notin C^2\).
2. If \(C=0\) and \(D\ne0\), then \(\Delta\in C^{3,1}\) but
   \(\Delta\notin C^4\).
3. If \(C=D=0\), then \(\Delta\) is real analytic at \(\Gamma\).

Here \(C^{m,1}\) means that the \(m\)-th derivatives are locally Lipschitz.

**Proof.** Near zero, \(q_a\asymp |k|^2\), while \(e_2=O(|k|^4)\) and
\(e_3=O(|k|^6)\). Hence \(e_2/q_a\) is a smooth angular function times
\(|k|^2\), and \(e_3/q_a\) is a smooth angular function times \(|k|^4\).
Differentiating the homogeneous leading terms proves the stated upper
regularity.

If a Hessian existed in the first case, its radial quadratic form would be
\(A+4Cp(n)\). But \(p\) ranges from \(0\) on an axis to \(1/3\) on a body
diagonal, so this is not a quadratic form when \(C\ne0\). Thus no second
Frechet derivative exists.

In the second case a fourth derivative would make
\(n\mapsto r(n)\) the restriction to the unit sphere of a homogeneous quartic
polynomial. Such a polynomial would vanish on all three coordinate planes,
so it would be divisible by \(n_1n_2n_3\). Its remaining linear factor cannot
make it even under all three independent sign flips unless it vanishes.
This contradicts \(r(1,1,1)/\sqrt3^6=1/27\). The third case is immediate
because only trigonometric polynomials remain. \(\square\)

The radial second derivative is

\[
\boxed{\kappa(n)=2\bigl(A+4Cp(n)\bigr)},\qquad 0\le p(n)\le\frac13.
\tag{1.2}
\]

Therefore \(\Gamma\) is a strict quadratic local minimum exactly when

\[
\boxed{A>0\quad\hbox{and}\quad A+\frac{4C}{3}>0.}
\tag{1.3}
\]

This criterion is independent of \(B,D\), which enter only at quartic order.
For the two-invariant pencil,

\[
A=\frac\alpha4,\qquad C=\frac{\beta-2\alpha}{16},\qquad B=D=0,
\]

so Theorem 1 recovers and sharpens the known statement: the coefficient is
\(C^{1,1}\), not merely \(C^1\), and has a Hessian precisely when
\(\beta=2\alpha\).

---

## 2. Equal-ray tomography and a new blind identity

The four coefficients can be extracted without mixing unrelated momenta. Let

\[
a(t)=4\sin^2(t/2)
\]

and define the centered values on the axial, face-diagonal, and body-diagonal
rays:

\[
E_1(t)=\Delta(t,0,0),\quad
E_2(t)=\Delta(t,t,0),\quad
E_3(t)=\Delta(t,t,t).
\]

Direct substitution gives the exact all-\(t\) identities

\[
\boxed{
\begin{aligned}
E_1(t)&=Aa,\\
E_2(t)&=2(A+C)a+Ba^2,\\
E_3(t)&=(3A+4C)a+\left(3B+\frac D3\right)a^2.
\end{aligned}}
\tag{2.1}
\]

Thus the normalized ray functions

\[
R_j(a)=\frac{E_j(t(a))}{a}
\]

are affine in \(a\):

\[
R_1=A,quad
R_2=2(A+C)+Ba,quad
R_3=3A+4C+\left(3B+\frac D3\right)a.
\tag{2.2}
\]

For any two distinct nonzero values \(a_1,a_2\), let \(m_j\) and \(b_j\)
be the exact slope and intercept of \(R_j\) through those two values. Then

\[
\boxed{
A=R_1,\qquad B=m_2,\qquad C=\frac{b_2}{2}-A,
\qquad D=3m_3-9m_2.}
\tag{2.3}
\]

The body-diagonal intercept is not needed for the fit. It supplies the new
target-blind holdout

\[
\boxed{b_3=2b_2-R_1.}
\tag{2.4}
\]

This protocol separates the \(L^{-2}\) tiers \((A,C)\) from the \(L^{-4}\)
tiers \((B,D)\) exactly, at finite momentum, rather than by a small-momentum
fit. Curvature inferred from a physical kernel should not be accepted unless
the affine-ray tests and (2.4) hold in addition to the existing \(X/M/R\)
holdout.

---

## 3. Tensorial projector tail and the localization obstruction

The exact flat projector for \(k\ne0\) is

\[
P_{\rm flat}(k)=\frac{w(k)w(k)^\dagger}{q_a(k)},
\qquad
w=(\bar d_3,-\bar d_2,\bar d_1)^T.
\]

Let

\[
J=\begin{pmatrix}0&0&1\\0&-1&0\\1&0&0\end{pmatrix}.
\]

Since \(w(k)=-iJk+O(|k|^2)\),

\[
P_{\rm flat}(k)=J\frac{kk^T}{|k|^2}J^T+O(|k|).
\tag{3.1}
\]

Using \(\mathcal F^{-1}(|k|^{-2})=(4\pi|x|)^{-1}\) in three dimensions,
the long-distance projector kernel has the explicit dipolar principal term

\[
\boxed{
P_{ab}(x)=
J_{ai}J_{bj}
\frac{\delta_{ij}|x|^2-3x_ix_j}{4\pi|x|^5}
+O(|x|^{-4}),\qquad |x|\to\infty.}
\tag{3.2}
\]

This supplies the tensor and coefficient behind the previously recorded
qualitative \(r^{-3}\) tail.

### Theorem 2 (no uniformly localized translation frame)

There is no finite collection of exponentially localized seed states whose
lattice translates span the \(k\ne0\) flat fiber and retain a volume-uniform
positive lower frame bound as \(k\to\Gamma\).

**Proof.** Exponential localization makes every Bloch column continuous
(indeed analytic in a strip). A positive lower frame bound would keep the
nonzero eigenvalue of the Bloch frame operator uniformly away from zero.
Its rank-one range projector would then extend continuously to \(\Gamma\).
Equation (3.1) has different limits along different rays, a contradiction.
\(\square\)

The compact cube-boundary seed saturates the obstruction. Its Bloch vector is
\(w(k)\), its frame operator is \(w(k)w(k)^\dagger\), and its only nonzero
eigenvalue is exactly \(q_a(k)\). On \(T_L^3\),

\[
\boxed{\min_{k\ne0}q_a(k)=4\sin^2(\pi/L),}
\tag{3.3}
\]

so the lower frame bound collapses as \(L^{-2}\). The three harmonic wrapping
sheets are therefore not an optional basis decoration: they are the finite-volume
completion forced by the singular projector.

---

## 4. Exact joint rank-volume scaling at second order

The established all-rank coefficient is

\[
t_N=\frac{2N(N^2-4)}{(N^2-1)(2N^2-1)(4N^2-9)},\qquad N\ge3.
\]

### Theorem 3 (rank monotonicity)

For real \(N\ge3\), \(t_N\) is strictly decreasing, while
\(g_N=N^3t_N\) is strictly increasing and satisfies

\[
\boxed{0<g_N<\frac14,\qquad \lim_{N\to\infty}g_N=\frac14.}
\tag{4.1}
\]

**Proof.** The common derivative denominator is positive, and

\[
t_N'=
\frac{-2(24N^8-190N^6+329N^4-97N^2-36)}
{(N-1)^2(N+1)^2(2N-3)^2(2N+3)^2(2N^2-1)^2}.
\]

With \(N^2=9+y\), the polynomial in parentheses is

\[
24y^4+674y^3+6863y^2+29639y+44694>0.
\]

Likewise,

\[
g_N'=
\frac{4N^3(2N^6+62N^4-151N^2+72)}
{(N-1)^2(N+1)^2(2N-3)^2(2N+3)^2(2N^2-1)^2}>0,
\]

because the final polynomial becomes
\(2y^3+116y^2+1451y+5193\). Finally,

\[
\frac14-g_N=
\frac{2N^4+31N^2-9}
{4(N^2-1)(4N^2-9)(2N^2-1)}>0,
\]

and the limit is immediate from the degrees. \(\square\)

The established finite-volume separation is

\[
\Delta^{(2)}_{N,L}=4t_Nu^2\sin^2(\pi/L).
\]

Since \(L\sin(\pi/L)\) is strictly increasing for \(L\ge3\), Theorem 3
gives a two-parameter monotonic scaling law:

\[
\boxed{
G_{N,L}:=\frac{N^3L^2}{u^2}\Delta^{(2)}_{N,L}
=4(N^3t_N)\,L^2\sin^2(\pi/L)
\nearrow\pi^2.}
\tag{4.2}
\]

It is strictly increasing in each of \(N\) and \(L\), and for all integers
\(N,L\ge3\),

\[
\boxed{\frac{405}{68}\le G_{N,L}<\pi^2,}
\tag{4.3}
\]

with equality on the left only at \((N,L)=(3,3)\). Thus the exact joint
large-rank/large-volume law is

\[
\Delta^{(2)}_{N,L}\sim\frac{\pi^2u^2}{N^3L^2}.
\tag{4.4}
\]

This sharpens the separate statements \(t_N\sim(4N^3)^{-1}\) and
finite-volume isolation \(\sim L^{-2}\) into one monotone scaling theorem.

---

## 5. What these results do and do not resolve

The strongest immediate use is diagnostic:

- (2.1)-(2.4) give a target-blind shape audit for the decisive fourth-order run;
- Theorem 1 tells exactly which nonsmoothness survives if the generic \(D\) tier
  is present, and gives the coefficient-independent local-minimum cone;
- Theorem 2 explains why compact cube boundaries coexist with an algebraic
  projector and why their finite-volume conditioning must collapse;
- Theorem 3 fixes the exact two-parameter scale of the second-order isolation.

None of these statements identifies the complete physical SU(3) fourth-order
kernel, supplies the missing \(|k|\lesssim u\) uniform perturbation estimate,
proves an overlap with the physical glueball, or makes an infinite-volume or
continuum mass-gap claim.

The companion verifier is
`numerics/engines/ENGINE_FLUX_singular_geometry_derivations.py`.
