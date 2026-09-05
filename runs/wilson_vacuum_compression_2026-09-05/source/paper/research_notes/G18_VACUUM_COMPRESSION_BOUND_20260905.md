# Vacuum anchoring is exact compression

Date: 5 September 2026.

This additive note sharpens a norm estimate in
`G18_SECOND_ORDER_WILSON_VACUUM_CHART_20260905.md` and
`G18_VACUUM_CHART_RECURSION_20260905.md`. Their earlier estimates remain
valid. The local vacuum rotation does not enlarge the retained coefficient:
its commutator removes exactly the two vacuum off-diagonal blocks. This
improves the quadratic full-operator constant from `40432/5` to `6032/5`,
and replaces the arbitrary-fixed-order local activity bound `l_n=11k_n`
by `l_n=k_n`. Retaining the quadratic normalization and the fine kinetic
damping gives the further sufficient constant `118872/125` below. The
generator bounds and the convergence question are unchanged.

## 1. Exact local identity

Let `H` be a Hilbert space with a unit vector `Omega`, and set

\[
 P=|\Omega\rangle\langle\Omega|,\qquad Q=I-P.
\]

Assume:

- `D` is bounded and self-adjoint, with `D Omega=Omega`;
- `A` is bounded and self-adjoint, with `<Omega,A Omega>=0`;
- `chi` belongs to `QH` and solves `(I-D)chi=A Omega`.

For the Wilson application `D=D_X=e^{-sK_X}` and
`chi=(I-D_X)^(-1)Q_XA Omega_X`. The calibrated local gap makes this solution
unique and bounded on `Q_X`. The compression identity itself needs only the
displayed equation, not a numerical bound on its inverse.

Define

\[
 S=|\chi\rangle\langle\Omega|-|\Omega\rangle\langle\chi|,
 \qquad F=A+[D,S],\qquad [D,S]=DS-SD.
 \tag{1}
\]

### Proposition 1. Exact vacuum compression

\[
 \boxed{[D,S]=-AP-PA,\qquad F=QAQ.}
 \tag{2}
\]

Consequently

\[
 FP=PF=0,\qquad \boxed{\|F\|\le\|A\|.}
 \tag{3}
\]

**Proof.** Self-adjointness and `D Omega=Omega` give `DP=PD=P`.
Expanding the commutator in (1) therefore yields

\[
 [D,S]
 =|(D-I)\chi\rangle\langle\Omega|
   +|\Omega\rangle\langle(D-I)\chi|.
\]

The equation for `chi` makes the first term `-AP`; the second is `-PA`
because `A` is self-adjoint. Thus `[D,S]=-AP-PA`. Since `PAP=0`,

\[
 A+[D,S]=A-AP-PA=A-AP-PA+PAP=QAQ.
\]

Compression by the orthogonal projection `Q` has operator norm at most one,
which proves (3). ∎

Equivalently, in the decomposition `H=C Omega direct-sum QH`, write

\[
 A=\begin{pmatrix}0&a^\dagger\\a&A_Q\end{pmatrix},\quad
 D=\begin{pmatrix}1&0\\0&D_Q\end{pmatrix},\quad
 S=\begin{pmatrix}0&-\chi^\dagger\\\chi&0\end{pmatrix}.
\]

The equation `(I-D_Q)chi=a` gives

\[
 [D,S]=\begin{pmatrix}0&-a^\dagger\\-a&0\end{pmatrix},\qquad
 F=\begin{pmatrix}0&0\\0&A_Q\end{pmatrix}.
 \tag{4}
\]

This also makes the necessity of the scalar hypothesis explicit. A nonzero
`PAP` could not be removed by this commutator. The preceding Wilson notes
obtain `PAP=0` from the actual Perron normalization and the already anchored
lower-order eigenvector coefficients; it is not an extra fitted subtraction.

## 2. Sharpened quadratic operator bound

Keep the definitions of the second-order note. After the first local
rotation and the actual local Perron normalization,

\[
 \|A_{pp}\|\le f_*^2,\qquad
 \|A_{pq}\|\le2f_*^2,
 \qquad f_*=J(s_1+2/E_s+\tau_0),\quad J=2N.
\]

Here `p,q` are distinct overlapping plaquettes in the second inequality.
Applying Proposition 1 to their four-link and at-most-seven-link supports
gives the stronger local bounds

\[
 \boxed{\|F_{pp}\|\le f_*^2,\qquad
        \|F_{pq}\|\le2f_*^2.}
 \tag{5}
\]

The exact connected/disconnected coefficient identity from that note is
unchanged. At `delta<=4/5`, its three support majorants have maxima

\[
 \begin{array}{c|c}
 \text{term family}&\text{support majorant maximum}\\ \hline
 \text{repeated face}&16\\
 \text{overlapping unordered pair}&336\\
 \text{disjoint unordered pair}&2592/5
 \end{array}
\]

The disjoint product uses the previous `||F_p||<=f_*` bound for each
first-order activity. Therefore the same full-Hilbert-space quadratic-form
argument now gives

\[
 \boxed{
 \sup_{L,\epsilon}\|[u^2]\widetilde{\mathcal D}_L(u)\|
 \le\left(16+2\cdot336+\frac{2592}{5}\right)f_*^2
 =\frac{6032}{5}f_*^2.
 }
 \tag{6}
\]

As before, `[u^2]` is the Taylor coefficient. The corresponding second
derivative bound is twice (6). No representation truncation or restriction
to a source-generated subspace enters the estimate.

There is also a direct refinement of the first-order input. For a single
face, `A_p=B_p'(0)` is self-adjoint with zero vacuum expectation, and the
first generator obeys the same equation as (1). Hence

\[
 F_p=Q_pB_p'(0)Q_p,\qquad
 \|F_p\|\le\|B_p'(0)\|\le sJ\le s_1J.
 \tag{7}
\]

The last inequality follows by differentiating the actual magnetic
exponentials and leaving the free factors as contractions; their total
time weight is `s`. Consequently one may sharpen (6) further to

\[
 \sup_{L,\epsilon}\|[u^2]\widetilde{\mathcal D}_L\|
 \le688f_*^2+\frac{2592}{5}(Js_1)^2
 \le\frac{6032}{5}f_*^2.
 \tag{8}
\]

Likewise the first complete derivative has the improved uniform bound
`16Js_1`. Equations (7)--(8) do not change the definitions of the earlier
chart or of `f_*`; they use its exact compression more efficiently.

### Corollary 2.1. Retaining normalization and kinetic damping

The direct compression constant (6) can be sharpened further to

\[
 \boxed{
 \sup_{L,\epsilon}\|[u^2]\widetilde{\mathcal D}_L\|
 \le\frac{3096}{5}f_*^2+\frac{41472}{125}(Js_1)^2
 \le\frac{118872}{125}f_*^2.
 }
 \tag{8a}
\]

**Proof.** For a degree-two monomial, let

\[
 C_\alpha=[z^\alpha](U_1^{-1}BU_1),\qquad
 b_\alpha=[z^\alpha]b.
\]

The first rotated vacuum column and the linear eigenvalue coefficients
vanish. Thus the exact local normalization gives

\[
 b_\alpha=\langle\Omega,C_\alpha\Omega\rangle,\qquad
 A_\alpha=C_\alpha-b_\alpha D.
\]

Since `||DQ||<=delta`, Proposition 1 implies

\[
 F_\alpha=QC_\alpha Q-b_\alpha DQ,\qquad
 \|F_\alpha\|\le(1+\delta)\|C_\alpha\|.
 \tag{8b}
\]

The original coefficientwise exponential majorant already bounds
`||C_pp||<=f_*^2/2` and `||C_pq||<=f_*^2`. At `delta<=4/5`, these become

\[
 \|F_{pp}\|\le\frac9{10}f_*^2,\qquad
 \|F_{pq}\|\le\frac95f_*^2.
\]

For the first coefficient retain every fine kinetic factor. Writing
`C_tau=e^{-tau K_p}` on one plaquette, direct differentiation of the
actual symmetric power gives

\[
 B_p'(0)=\frac\tau2(v_pC_\tau^m+C_\tau^mv_p)
           +\tau\sum_{j=1}^{m-1}C_\tau^jv_pC_\tau^{m-j}.
\]

Compress each term by `Q_p`. This projection commutes with `C_tau`, and

\[
 \|C_\tau^jQ_p\|\le e^{-\tau\gamma j}.
\]

Each compressed term therefore carries the full damping
`exp(-tau gamma m)=delta`, including the endpoints where one kinetic
power is zero. The total differentiated weight is `m tau=s`, proving

\[
 \|F_p\|=\|Q_pB_p'(0)Q_p\|\le\delta sJ.
 \tag{8c}
\]

Using the same support maxima as before, the two connected families are
bounded by

\[
 \left(16\frac9{10}+336\frac95\right)f_*^2
 =\frac{3096}{5}f_*^2.
\]

The disjoint product is at most

\[
 \frac{2592}{5}(\delta sJ)^2
 \le\frac{41472}{125}(s_1J)^2.
\]

Adding proves the first inequality in (8a). Since `Js_1<=f_*`, its single-
constant form follows from
`3096/5+41472/125=118872/125`. ∎

This additional normalization estimate is specific to degree two. At
higher degrees the identity `C=bE` also contains products of nonconstant
lower eigenvalue and operator coefficients. Those terms cannot be dropped.
The exact compression identity `F=QAQ`, in contrast, applies at every
degree and is the only improvement used in the next section's recurrence.

## 3. Every fixed order

For a connected degree-`n` monomial, the recursion note defines

\[
 A_\alpha=[z^\alpha]E_{A(\alpha)}^{<n},\qquad
 \chi_\alpha=(I-D_{X_\alpha})^{-1}Q_{X_\alpha}
                      A_\alpha\Omega_{X_\alpha}.
\]

Its normalized eigenvector induction proves
`<Omega,A_alpha Omega>=0`. Proposition 1 therefore applies at every degree:

\[
 \boxed{F_\alpha=Q_{X_\alpha}A_\alpha Q_{X_\alpha}.}
 \tag{9}
\]

In the notation of that note, `k_n` is the uniform bound on `||A_alpha||`.
Its local bounds may consequently be replaced by

\[
 \boxed{a_n=5k_n,\qquad l_n=k_n\quad(n\ge2),}
 \tag{10}
\]

with the optional sharper first-order choice `l_1=Js_1`. The generator
bound `a_n` still uses the inverse estimate and is not reduced by
compression. The explicit Cauchy recurrence for `k_n`, which depends on
the preceding generator bounds, is therefore unchanged. The component
counting and full-operator coefficient formulas remain valid after
substituting the smaller `l_n`.

This is a strict improvement of the local activity constants. It does not
give a convergence radius: the same crude Cauchy bounding sequence still
grows too quickly. A convergent rooted estimate and an exact nonlinear
operator realization remain separate tasks.

## 4. Provenance and verification scope

The hypothesis checks, compression proof, quadratic constant and fixed-order
substitution in this note were independently derived from the existing
rank-two vacuum-chart definitions. The older `11||A||` and `40432/5`
estimates remain valid weaker bounds; their original notes and sealed run
records are preserved.

Finite exact matrix checks of (2) can separately verify the algebra and
detect a lost vacuum block or commutator sign. Those checks do not replace
the Hilbert-space argument above or establish nonlinear convergence.
