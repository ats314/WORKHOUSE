# Fourth-Order Hodge Shape Space and Foliated Mobility

## Exact expansion and audit of the \(C\)-odd homological flat-band program

**Date:** 23 July 2026  
**Scope:** Fixed spatial lattice; strong-coupling one-plaquette \(C\)-odd sector  
**Evidence:** Exact cubical enumeration and Laurent-polynomial certificate; no fourth-order \(SU(N)\) Haar weights assumed

## Executive verdict

The proposed fourth-order shape calculation contains a real theorem, but its
strongest unconditional form is not the advertised two-parameter statement.

The exact conclusions are:

1. The aggregate tromino algebra is correct. On the flat fiber,
   \[
   f_{p^+}+f_{p^-}+f_{\mathrm{co}}=12,
   \]
   and
   \[
   f_{\mathrm{co}}(\mathbf k)
   =
   \frac{4}{q}\sum_{i<j}|u_i|^2|u_j|^2
   \ge 0.
   \]

2. Consequently, **if** every path with sign product \(+1\) has one common
   weight, every path with sign product \(-1\) has a second common weight,
   and every corner has a third common weight, then the projected correction
   does reduce algebraically to
   \[
   \mathrm{const}
   +\alpha f_{\mathrm{co}}
   +\gamma f_{\mathrm{dif}}.
   \]

3. That coarse uniformity is not implied by hopping range. The \(52\)
   \(p^+\) paths and \(40\) \(p^-\) paths are not two space-group orbits.
   Exact enumeration gives seven geometric open-path orbits, together with
   two same-link orbits, one corner orbit, and two backtrack orbits.

4. After resolving those actual space-group orbits, the full nonconstant
   flat-fiber obstruction space is **four-dimensional**, not
   two-dimensional:
   \[
   \boxed{
   \delta m_4(\mathbf k)
   =
   c_0
   +c_1q
   +c_2e_2
   +c_3\frac{e_2}{q}
   +c_4\frac{e_3}{q}.
   }
   \]
   Here
   \[
   a_i=|1-e^{ik_i}|^2,\qquad
   q=e_1=a_1+a_2+a_3,
   \]
   \[
   e_2=a_1a_2+a_1a_3+a_2a_3,\qquad
   e_3=a_1a_2a_3.
   \]
   The two rational functions are assigned their continuous value \(0\) at
   \(\Gamma\).

5. The proposed \(f_{\mathrm{dif}}\) direction is not a cubic scalar. It is
   tied to an orientation-dependent sign partition of open paths. Therefore
   an isolated term \(\gamma f_{\mathrm{dif}}\) is incompatible with cubic
   covariance. Within the coarse three-weight ansatz, cubic symmetry forces
   \(\gamma=0\).

6. The proposed “tube” interpretation is attached to the wrong zero set.
   \(f_{\mathrm{co}}\) vanishes on momentum-space axes and produces
   real-space **sheet** states. The additional orbit-resolved shape
   \(e_3/q\) vanishes on momentum-space coordinate planes and is the one
   capable of producing real-space **tube** states.

The larger result is therefore more interesting than a two-number fit:
fourth order has a finite, exact, cubic-invariant obstruction algebra with a
hierarchy of point, line, plane, and volume zero sets.

## 1. Exact second- and third-order foundation

Let
\[
u_i=1-e^{ik_i}
\]
and let the Bloch face-to-edge matrix be
\[
\widetilde N(\mathbf k)=
\begin{pmatrix}
u_2&-u_1&0\\
u_3&0&-u_1\\
0&u_3&-u_2
\end{pmatrix}.
\]

The signed plaquette adjacency satisfies
\[
S(\mathbf k)+4I
=
\widetilde N(\mathbf k)\widetilde N(\mathbf k)^\dagger.
\]
Its spectrum is
\[
\operatorname{spec}S(\mathbf k)
=
\{-4,q(\mathbf k)-4,q(\mathbf k)-4\},
\]
where
\[
q(\mathbf k)
=
\sum_i|u_i|^2
=
4\sum_i\sin^2\frac{k_i}{2}.
\]

A generic flat-fiber vector is
\[
w(\mathbf k)
=
(\overline u_3,-\overline u_2,\overline u_1)^{\mathsf T},
\qquad
w^\dagger w=q,
\]
and
\[
\widetilde N^\dagger w=0,\qquad Sw=-4w.
\]

At second order, the group and spatial factors separate:
\[
H_{-,N}^{(2)}(\mathbf k)
=
a_{N,-}I+t_NS(\mathbf k),
\]
\[
t_N=
\frac{2N(N^2-4)}
{(N^2-1)(2N^2-1)(4N^2-9)}.
\]
This proves flatness for \(SU(N\ge3)\) through \(O(y^2)\).

For \(SU(3)\), the supplied third-order derivation states that all
three-distinct-plaquette tromino numerators vanish by the bare-link lemma and
the surviving hop is again proportional to \(S\). In boundary-ideal language,
\[
H_2-c_2I,\ H_3-c_3I
\in
\widetilde N\,\mathcal B\,\widetilde N^\dagger.
\]
The fourth order is the first order at which dressed trominoes can escape
that ideal.

## 2. The exact coarse-class collapse

The \(144\) ordered two-hop sequences from one source plaquette split as

| Aggregate class | Count |
|---|---:|
| Backtrack | 12 |
| Same-link triangle | 24 |
| Corner triangle | 16 |
| Open path, sign product \(+1\) | 52 |
| Open path, sign product \(-1\) | 40 |

Let their Bloch operators be
\[
B_{\mathrm{bt}},\quad
B_{\mathrm{sl}},\quad
B_{\mathrm{co}},\quad
B_{p^+},\quad
B_{p^-}.
\]
Exact Laurent-polynomial identities give
\[
B_{\mathrm{bt}}=12I,
\qquad
B_{\mathrm{sl}}=2S,
\qquad
B_{\mathrm{co}}=-2S_\perp,
\]
and
\[
B_{p^+}+B_{p^-}+B_{\mathrm{co}}
=
S^2-12I-2S.
\]

Define the flat-fiber class functions
\[
f_X(\mathbf k)
=
\frac{w^\dagger B_Xw}{w^\dagger w}.
\]
Since \(Sw=-4w\),
\[
\boxed{
f_{p^+}+f_{p^-}+f_{\mathrm{co}}=12.
}
\]

If one assigns aggregate weights
\[
W_+,\qquad W_-,\qquad W_{\mathrm{co}},
\]
then
\[
W_+f_{p^+}+W_-f_{p^-}+W_{\mathrm{co}}f_{\mathrm{co}}
\]
equals
\[
12\overline W_{\mathrm{path}}
+
\left(W_{\mathrm{co}}-\overline W_{\mathrm{path}}\right)
f_{\mathrm{co}}
+
\frac{W_+-W_-}{2}
\left(f_{p^+}-f_{p^-}\right),
\]
where
\[
\overline W_{\mathrm{path}}=\frac{W_++W_-}{2}.
\]
Thus, with
\[
\alpha=W_{\mathrm{co}}-\overline W_{\mathrm{path}},
\qquad
\gamma=\frac{W_+-W_-}{2},
\]
and
\[
f_{\mathrm{dif}}=f_{p^+}-f_{p^-},
\]
the two-shape formula is algebraically exact:
\[
\boxed{
\delta m_4
=
\mathrm{const}
+\alpha f_{\mathrm{co}}
+\gamma f_{\mathrm{dif}}.
}
\]

This is a valid **conditional collapse theorem**. It is not yet the complete
range-two theorem.

## 3. The corner function

Set
\[
a_i=|u_i|^2=4\sin^2\frac{k_i}{2}.
\]
Direct projection gives
\[
\boxed{
f_{\mathrm{co}}
=
4\frac{e_2}{q}
=
\frac{4(a_1a_2+a_1a_3+a_2a_3)}
{a_1+a_2+a_3}.
}
\]

It has the exact properties
\[
0\le f_{\mathrm{co}}\le16,
\]
\[
f_{\mathrm{co}}=0
\iff
\text{at most one }a_i\text{ is nonzero},
\]
and
\[
f_{\mathrm{co}}(X)=0,\qquad
f_{\mathrm{co}}(M)=8,\qquad
f_{\mathrm{co}}(R)=16.
\]

Therefore its zero set is the union of the three coordinate axes of the
Brillouin zone. If \(\alpha>0\) and every other shape coefficient vanishes,
those axes are the fourth-order ground set. If \(\alpha<0\), the axes are
maxima; the minimum is driven toward \(R\), where \(f_{\mathrm{co}}\) is
largest.

## 4. Why \(\gamma\) is not an independent cubic observable

The \(p^+/p^-\) split is made by the product of two signed hops along an open
path. Unlike the sign around a closed triangle, an open-path sign product
depends on the endpoint orientation convention. Accordingly,
\[
f_{\mathrm{dif}}=f_{p^+}-f_{p^-}
\]
is not invariant under the cubic point group.

The failure is exact, not numerical. For example,
\[
f_{\mathrm{dif}}
\left(\frac\pi3,\frac\pi2,\pi\right)
=
-8+4\sqrt3,
\]
while a cyclic coordinate permutation gives
\[
f_{\mathrm{dif}}
\left(\frac\pi2,\pi,\frac\pi3\right)
=
-8-4\sqrt3.
\]

At the familiar checkpoints,
\[
f_{\mathrm{dif}}(X)=-4,\qquad
f_{\mathrm{dif}}(R)=12,
\]
but those two values do not make the function a cubic scalar.

Consequences:

- In the isolated coarse three-weight ansatz, cubic covariance requires
  \[
  \gamma=0
  \quad\Longleftrightarrow\quad
  W_+=W_-.
  \]
- If orbit-resolved terms are present, the \(p^+/p^-\) decomposition is not a
  physical invariant parametrization. One must assemble the full cubic
  operator first and only then project it onto the flat fiber.

Thus the physically covariant coarse collapse is
\[
\delta m_4
=
\mathrm{const}+\alpha f_{\mathrm{co}},
\]
not a generic two-parameter scalar dispersion.

## 5. The true orbit refinement

Range at most two restricts the support, but it does not equate all processes
with that support. Exact classification under translations, all signed
coordinate permutations, and path reversal gives:

| Geometric type | Number of space-group orbits |
|---|---:|
| Backtrack | 2 |
| Same-link triangle | 2 |
| Corner triangle | 1 |
| Open three-plaquette path | 7 |
| **Total** | **12** |

The two backtrack orbits are separately scalar on plaquette space. The
remaining ten orbit operators project into a five-dimensional function space
including the scalar.

This is the load-bearing distinction:

> A certificate that sums all \(52\) positive-sign paths into one Bloch
> object proves a geometric identity for that aggregate. It does not prove
> that the fourth-order Haar-resolvent contraction assigns one common weight
> to every constituent path.

“Class uniformity” is therefore not a routine lemma following from the
tromino count. It is a nontrivial dynamical identity collapsing seven
geometric path weights, two same-link weights, and the corner weight into a
much smaller parameter set.

## 6. Four-dimensional cubic obstruction theorem

Let an \(O(y^4)\) momentum-dependent correction be assembled from
orbit-uniform tromino operators, with one coefficient for each actual
space-group orbit. Project it onto the generic flat fiber:
\[
\varepsilon_4(\mathbf k)
=
\frac{w^\dagger H_4(\mathbf k)w}{q}.
\]

The exact orbit enumeration gives the numerator space
\[
q\,\varepsilon_4
\in
\operatorname{span}
\{q,\ q^2,\ qe_2,\ e_2,\ e_3\}.
\]
Dividing by \(q\) gives:

> **Fourth-order cubic shape theorem.**
> Under the tromino-completeness and space-group orbit-uniformity hypotheses,
> the most general projected fourth-order correction is
> \[
> \boxed{
> \varepsilon_4(\mathbf k)
> =
> c_0
> +c_1q
> +c_2e_2
> +c_3\frac{e_2}{q}
> +c_4\frac{e_3}{q}.
> }
> \]
> The four nonconstant functions are linearly independent as Laurent-rational
> functions.

A convenient normalized basis is
\[
\phi_1=q,\qquad
\phi_2=e_2,\qquad
\phi_3=f_{\mathrm{co}}=4e_2/q,\qquad
\phi_4=e_3/q.
\]
Then
\[
\varepsilon_4=c_0+A\phi_1+B\phi_2+C\phi_3+D\phi_4.
\]

The original two-shape proposal is a special, non-generic collapse of this
space. After imposing cubic covariance on the coarse ansatz, it occupies only
the \(C\phi_3\) direction.

## 7. Exact four-number extraction

The complete orbit-resolved shape can be measured without fitting a
Brillouin-zone surface.

Let
\[
\Delta_K=\varepsilon_4(K)-\varepsilon_4(\Gamma)
\]
at
\[
X=(\pi,0,0),\quad
M=(\pi,\pi,0),\quad
R=(\pi,\pi,\pi),
\]
and introduce one additional checkpoint
\[
P=\left(\pi,\frac\pi2,0\right).
\]

The basis values are:

| Point | \(q\) | \(e_2\) | \(f_{\mathrm{co}}\) | \(e_3/q\) |
|---|---:|---:|---:|---:|
| \(\Gamma\) | 0 | 0 | 0 | 0 |
| \(X\) | 4 | 0 | 0 | 0 |
| \(M\) | 8 | 16 | 8 | 0 |
| \(P\) | 6 | 8 | \(16/3\) | 0 |
| \(R\) | 12 | 48 | 16 | \(16/3\) |

The coefficient map is exactly invertible:
\[
\boxed{
A=\frac{\Delta_X}{4},
}
\]
\[
\boxed{
B=\frac{\Delta_X+4\Delta_M-6\Delta_P}{16},
}
\]
\[
\boxed{
C=\frac{3(2\Delta_P-\Delta_M-\Delta_X)}{8},
}
\]
\[
\boxed{
D=\frac{3(\Delta_R-6\Delta_M+6\Delta_P)}{16}.
}
\]

This is the stronger pre-registration:

- **Full boundary-ideal survival:** \(A=B=C=D=0\).
- **Coarse cubic collapse:** \(A=B=D=0\), with only \(C\) allowed.
- **Generic orbit-resolved lifting:** at least one of \(A,B,D\) is nonzero.
- **Full flatness failure scale:** the exact bandwidth of the resulting
  four-shape function.

The extraction should be performed directly from exact orbit weights or the
exact \(H_4(\mathbf k)\), before numerical plotting.

## 8. Foliated zero-set hierarchy

The four invariant shapes reveal a hierarchy that was hidden in the
two-class description.

| Shape | Zero set in momentum space | Degeneracy scale | Real-space hybrid localization |
|---|---|---:|---|
| \(q\) | \(\Gamma\) only | \(O(1)\) | fully extended Bloch triplet |
| \(e_2\) or \(e_2/q\) | three coordinate axes | \(O(L)\) | sheets: localized in one coordinate, extended in two |
| \(e_3/q\) | three coordinate planes | \(O(L^2)\) | tubes: localized in two coordinates, extended in one |
| zero correction | full Brillouin zone | \(O(L^3)\) | compact cube boundaries plus harmonic surfaces |

For nonnegative isolated coefficients, the exact finite-torus counts,
including the three-dimensional \(\Gamma\) fiber, are:

\[
\text{axis-zero phase:}\qquad 3L,
\]
\[
\text{plane-zero phase:}\qquad
3L^2-3L+3,
\]
\[
\text{fully flat phase:}\qquad
L^3+2.
\]

This corrects the original real-space interpretation:

- a momentum-space **line** permits superposition over one momentum
  coordinate, so it localizes only the conjugate real-space coordinate and
  produces a sheet;
- a momentum-space **plane** permits superposition over two momenta, so it
  produces a tube extended along the remaining direction.

The tube phase is therefore not generated by \(f_{\mathrm{co}}\) alone. It is
available through the additional \(e_3/q\) obstruction uncovered by the
space-group orbit refinement.

These are hybrid Wannier states, not compact three-dimensional localized
states. On a periodic torus the sheets and tubes wrap around the system.

## 9. What the Hodge statement really says

The face/link superpartner pair is exact:
\[
\mathcal H_2=\widetilde N\widetilde N^\dagger,\qquad
\mathcal H_1=\widetilde N^\dagger\widetilde N,
\]
\[
\operatorname{spec}\mathcal H_1
=
\operatorname{spec}\mathcal H_2
=
\{0,q,q\}.
\]

On an \(L^3\) torus,
\[
\dim\ker\mathcal H_2
=
\dim\ker\mathcal H_1
=
L^3+2,
\]
so the Witten/Fredholm index is zero.

The plaquette kernel decomposes as
\[
\ker\partial_2
=
\operatorname{im}\partial_3\oplus H_2(T^3),
\]
\[
\dim\ker\partial_2
=
(L^3-1)+3.
\]

Thus:

- the \(L^3-1\) compact cube-boundary states are exact two-boundaries, not
  nontrivial homology classes;
- only the three harmonic wrapping surfaces measure \(b_2(T^3)=3\);
- the raw flat-band degeneracy is not itself a Betti number.

For a general finite cellulation,
\[
\dim\ker\partial_2
=
\operatorname{rank}\partial_3+b_2.
\]
The spectrum can therefore recover \(b_2\) only after the
cellulation-dependent boundary rank is known or independently measured.

The correct headline is:

> The \(C\)-odd one-plaquette Hamiltonian realizes a one-sided cubical Hodge
> operator whose kernel separates exact cube boundaries from harmonic
> two-cycles.

It does not dynamically realize the entire de Rham Laplacian. The full Hodge
operator
\[
\Delta_2
=
\partial_2^\dagger\partial_2
+
\partial_3\partial_3^\dagger
\]
would lift the exact cube boundaries and retain only the \(b_2\) harmonic
zero modes.

## 10. Boundary ideal and the all-orders conjecture

Let
\[
K=\ker\widetilde N^\dagger,\qquad P_K\text{ its projector}.
\]
At perturbative order \(r\), exact preservation of the full flat space at
energy \(c_r\) is equivalent to
\[
\boxed{
(H_r-c_rI)P_K=0.
}
\]

A local sufficient condition is
\[
\boxed{
H_r-c_rI
=
\widetilde N B_r\widetilde N^\dagger.
}
\]

The boundary ideal
\[
\mathcal I_\partial
=
\{\widetilde N B\widetilde N^\dagger\}
\]
is the correct algebraic object. The projected shape map
\[
\Pi_K(H)
=
\frac{w^\dagger Hw}{q}
\quad \bmod\ \text{constants}
\]
annihilates this ideal. At fourth order, the orbit-resolved tromino quotient
has dimension four:
\[
\dim\Pi_K(\mathcal A_{\mathrm{tromino}})=4.
\]

Therefore the exact all-orders question is:

> Does the connected \(C\)-odd effective Hamiltonian land in the boundary
> ideal at every order, or which orbit invariant first survives in the
> quotient?

The bare-link lemma proves one low-order selection rule. It does not by
itself establish an induction, because balanced link dressings become
possible at fourth order.

Even if all four fourth-order coefficients vanish, all-orders flatness still
requires:

1. an order-by-order factorization or annihilator proof;
2. control of folded/subtraction terms in the same ideal;
3. convergence of the effective Hamiltonian series;
4. separate control of the inverse block-diagonalizing transformation that
   dresses physical states.

Exact flatness of the effective band implies zero group velocity. It does
not automatically imply that a fully dressed microscopic eigenstate has
strict six-plaquette support.

## 11. Rank-cubic matched-scaling target

The exact second-order coefficient obeys
\[
t_N\sim\frac1{4N^3}.
\]
The full \(C\)-odd one-plaquette manifold has width
\[
W_N^{(-)}
\sim
\frac{3y^2}{N^3},
\]
while the unperturbed one-plaquette energy is
\[
E_{F,N}=2C_F\sim N.
\]
Hence the formal fractional mobility is
\[
\frac{W_N^{(-)}}{E_{F,N}}
\sim
\frac{3y^2}{N^4}.
\]

Using the exact bridge
\[
\beta=\frac{Ny}{2},
\]
and setting
\[
\tau=\frac{\beta}{N^3},
\]
gives the formal relation
\[
\frac{W_N^{(-)}}{E_{F,N}}
\sim
12\tau^2.
\]

Independently, the fixed-rank local strong-potential expansion is ordered
only when
\[
\frac{N^3}{\beta}
=
\tau^{-1}
\ll1.
\]

Thus both formal asymptotic descriptions select the same dimensionless
variable \(\tau=\beta/N^3\), from opposite sides:

| Formal side | Diagnostic |
|---|---|
| Extrapolated strong-coupling mobility | \(12\tau^2\) |
| Ordering of the local strong-potential series | \(\tau^{-1}\) |

This is a sharp **matched-scaling target**, not a proved crossover. The
strong-coupling series is not controlled at \(y\sim N^2\), and the local
large-\(\beta\) remainder is not uniform at \(\beta\sim N^3\). There is no
overlap theorem.

The credible conjecture is:

> A nonperturbative double-scaled spectral problem at
> \(\beta=N^3\tau\) governs the reorganization between rank-suppressed
> homological mobility and the rank-growing local Weyl dynamics.

A theorem would require a rank-uniform Hamiltonian or resolvent limit in
\(\tau\), not substitution into either fixed-regime series.

## 12. Finite-density continuation

If the one-particle flat space survives to a controlled order, the next
physical object is the projected two-particle interaction
\[
V_{\mathrm{proj}}
=
P_{K\otimes K}
H_{\mathrm{eff}}^{(2\text{-particle})}
P_{K\otimes K}.
\]

The first exact calculation should classify two cube-boundary excitations by:

- disjoint support;
- face sharing;
- edge sharing;
- corner sharing;
- coincident or forbidden overlap;
- relative wrapping sector.

The outputs should be:

1. diagonal interaction energies;
2. exchange amplitudes;
3. correlated pair hopping;
4. whether interactions preserve any foliation or boundary ideal;
5. the lowest two-particle eigenstate on the smallest complete clusters.

Only after this calculation should the program use phrases such as
“glueball crystal.” A flat one-particle kinetic term does not by itself prove
crystallization: projected interactions can favor phase separation, resonant
pair motion, bound states, or ordered density patterns.

The defensible larger program is **interaction-only homological matter in a
non-Abelian gauge theory**.

## 13. Revised publication architecture

The strongest paper spine is:

1. exact \(SU(N)\) fusion coefficient \(t_N\);
2. balanced face/link Hodge pair and zero index;
3. torus kernel decomposition into exact and harmonic sectors;
4. third-order bare-link survival for \(SU(3)\), after certificate recovery;
5. exact fourth-order orbit and shape-space classification;
6. four-number pre-registered \(H_4\) test;
7. boundary-ideal conjecture;
8. rank-cubic matched-scaling target, explicitly conjectural.

A suitable title is:

> **Homological Flat Bands, Hodge Obstruction Spaces, and Rank-Cubic Mobility
> in Strong-Coupling \(SU(N)\) Lattice Gauge Theory**

The fourth-order physical contraction then becomes a decisive paper result:

- if \(A=B=C=D=0\), it is a new nontrivial boundary-ideal survival theorem;
- if only \(C\neq0\), it realizes the flat-line sheet phase;
- if only \(D\neq0\), it realizes the flat-plane tube phase;
- if several coefficients survive, it gives the first complete
  orbit-resolved breakdown of homological mobility.

## 14. Status ledger

| Statement | Status |
|---|---|
| \(144=12+24+16+52+40\) coarse path split | **Exactly certified** |
| Aggregate tromino Bloch identities | **Exactly certified** |
| \(f_{\mathrm{co}}=4e_2/q\) | **Exactly certified** |
| \(f_{\mathrm{co}}\) vanishes on the three momentum axes | **Proved** |
| Algebraic two-shape formula under three aggregate weights | **Proved, conditional on coarse uniformity** |
| \(f_{\mathrm{dif}}(X)=-4,\ f_{\mathrm{dif}}(R)=12\) | **Exactly certified** |
| \(f_{\mathrm{dif}}\) is a cubic scalar | **False** |
| Range \(\le2\) alone implies a two-dimensional shape space | **False** |
| True tromino orbit count \(2+2+1+7=12\) | **Exactly certified** |
| Orbit-resolved nonconstant obstruction dimension is four | **Exactly certified** |
| General shape basis \(\{q,e_2,e_2/q,e_3/q\}\) | **Exactly certified** |
| \(f_{\mathrm{co}}\) produces compact tube states | **False; it produces sheet-type hybrid states** |
| \(e_3/q\) permits a flat-plane tube phase | **Proved as a shape-space possibility; physical coefficient open** |
| Physical \(SU(N)\) fourth-order coefficient vector \((A,B,C,D)\) | **Open computation** |
| Fourth-order boundary-ideal survival | **Open** |
| All-orders boundary-ideal covariance | **Conjectural** |
| Nonzero Witten-index protection | **False; index is zero** |
| Raw \(L^3+2\) degeneracy equals \(b_2\) | **False; it equals \(\operatorname{rank}\partial_3+b_2\)** |
| \(\beta\sim N^3\) is a proved mobility crossover | **Conjectural matched-scaling target only** |
| Finite-density glueball crystal | **Open two-particle program** |

## Certificate

The accompanying file
`fourth_order_hodge_shape_space_certificate.py` is a standard-library,
fail-closed exact-arithmetic program. It verifies:

- the \(52/40\) sign-product count;
- every aggregate Bloch identity;
- the exact corner formula;
- the \(X/R\) values of \(f_{\mathrm{dif}}\);
- failure of cubic covariance for \(f_{\mathrm{dif}}\);
- all twelve actual space-group orbits;
- exact rank five of the projected numerator space;
- the invariant basis
  \[
  \{q,q^2,qe_2,e_2,e_3\};
  \]
- and therefore the four-dimensional nonconstant energy shape space.

## Scope firewall

Nothing here establishes a continuum Yang-Mills mass gap, a continuum
glueball mass, an all-orders localized physical particle, or a Wilson area
law. The results classify a fixed-lattice, finite-order effective band and
its exact cubical geometry.

