# W6 conditional score domination M10: exact reduction to three obligations

11 September 2026. Reviewed continuation of the
[conditional score tail control](w6-conditional-score-tail-control.md) (M1–M15),
the [conditional transport obstruction](w6-conditional-transport-obstruction.md) (S1–S15),
and the [antipodal magnetic geometry](w6-antipodal-magnetic-geometry.md) (A1–A15).

This note does **not** prove M10. An earlier draft of this document claimed
the full domination bound; review found that its three substantive steps
restated the open items of S6 as assertions. What survives is recorded here:
the exact algebra that turns the three S6 obligations into M10 with explicit
constants, one exact obstruction to the naive nine-dimensional tube estimate
near the antipode, and the precise statements that remain to be proved.
`DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10` stays **open**.

Every check named below is in
`src/workhouse/invariants/w6_score_tail_m10.py` and is exact (symbolic or
rational), not a float agreement.

---

## 1. Setting and notation

Fixed twelve-edge, four-face compact Wilson square $M=\mathrm{SU}(2)^4$, true
normalized positive ground $\Psi_g$, $d\mu_g=\Psi_g^2\,dU$, literal source
$w=\operatorname{Sc}(U_2U_3)=\tfrac12\operatorname{tr}(U_2U_3)$ with marginal
$\nu_g$. Conditioning on $w$ and on $Q=U_2U_3$ give the same conditional
variance of a gauge-invariant score (transport obstruction, S2). Write
$Q=\exp(i\,q\cdot\sigma/2)$ in Lie-vector convention, $|q|=2\theta$,
$\theta\in[0,\pi]$.

The transported score and the two conditional quantities of M10 are

\[
\sigma_g=\frac{\partial_g\Psi_g+D\Psi_g/g}{\Psi_g},\qquad
K_g(Q)=\operatorname{Var}_{\mu_g}(\sigma_g\mid Q),\qquad
W_g(Q)=g^{-2}\,\mathbb E_{\mu_g}(V\mid Q). \tag{R1}
\]

On the constrained minimizing curve $m(q)$ ($U_0=U_1=A$, $U_2=U_3=A^2$,
$Q=A^4$, $A=\exp(\theta n/4)$), the four-face potential of A2 at zero
transverse displacement is

\[
v_*(\theta)=16\,(1-\cos(\theta/4))=32\sin^2(\theta/8),\qquad
v_*(\pi)=16-8\sqrt2. \tag{R2}
\]

Check `W6 M10 reduction: constrained minimum potential and antipodal value`
re-derives (R2) from the A2 quaternion expansion (constant term $16-16C$
with $C=\cos(\theta/4)$) and confirms $v_*(\pi)=16-8\sqrt2$ against A12.

---

## 2. What is proved exactly

### 2.1 Synchronized tangency (S12–S13)

With the S13 profiles $z_0=z_1=r\chi(4r)$, $z_2=r\chi(2r)$, $z_Q=r\chi(r)$
and an **arbitrary** smooth cutoff $\chi$, the speeds of the four factors on
$m(q)$ are $(\theta/4)\chi(\theta)$, $(\theta/4)\chi(\theta)$,
$(\theta/2)\chi(\theta)$, and $\theta\chi(\theta)$, while
$Dm(q)\,Z_q=(\tfrac14,\tfrac14,\tfrac12)\,\theta\chi(\theta)$. Hence
$Z_y(m(q),q)-Dm(q)Z_q(q)=0$ identically in $\theta$ and $\chi$, so the linear
term S12 vanishes:

\[
\partial_y(2S-ZS)\big|_{m(q)}=0. \tag{R3}
\]

Check `W6 M10 reduction: synchronized tangency for every cutoff` verifies
(R3) with $\chi$ a symbolic function.

### 2.2 The potential floor used by S14

\[
v_*(\theta)=32\sin^2(\theta/8)\;\ge\;\frac{2\theta^2}{\pi^2}=\frac{|q|^2}{2\pi^2},
\qquad 0\le\theta\le\pi. \tag{R4}
\]

Proof. $f(x)=\sin x-2x/\pi$ has $f(0)=f(\pi/2)=0$ and $f''=-\sin x<0$ on
$(0,\pi/2)$, so $f\ge0$ there; with $x=\theta/8\in[0,\pi/8]$,
$32\sin^2(\theta/8)\ge32\cdot4\theta^2/(64\pi^2)=2\theta^2/\pi^2$.
Since $v_*(\theta)$ is the minimum of $V$ on the fiber,
$|q|^2\le2\pi^2\,\mathbb E(V\mid Q)=2\pi^2g^2W_g(Q)$.
Check `W6 M10 reduction: potential floor v_* >= |q|^2/(2 pi^2)`.

### 2.3 Polynomial-times-exponential suprema (used by S15)

For $p>0$, $c>0$:

\[
\sup_{g>0}\,g^{-p}\exp(-c/g^2)=\Big(\frac{p}{2ec}\Big)^{p/2},
\qquad\text{in particular}\quad
\sup_{g>0}g^{-6}e^{-c/g^2}=\Big(\frac{3}{ec}\Big)^{3}. \tag{R5}
\]

Proof. With $t=g^{-2}$ the function is $t^{p/2}e^{-ct}$, stationary at
$t=p/(2c)$. Consequently an outside term of the form
$C\,g^{-p}\exp(-c_{\rm tube}/g^2)$ is bounded uniformly on $(0,g_*]$ for
**any** polynomial order $p$: the rare-fiber obligation in §4.2 therefore
needs only a polynomial conditional moment bound, not a sharp one.
Check `W6 M10 reduction: exact supremum of g^-p exp(-c/g^2)`.

### 2.4 Conditional synthesis theorem

**Hypotheses** (all on $0<g<g_*$, with constants independent of $g$ and $Q$).

- **(H1) Tube moments.** On a uniform tube $|\eta|\le\delta_{\rm tube}$ about
  $m(q)$, $\mathbb E_{\rm tube}[|\eta|^{2j}\mid Q]\le c_{2j}g^{2j}$, $j=1,2,3$.
- **(H2) Differentiated amplitude.** With $\Psi_g=g^{-6}A_g e^{-S/g^2}$ and
  $a_g=\partial_g\log A_g+g^{-1}[Z\log A_g+\tfrac12\operatorname{div}Z-6]$,
  $|D_\eta a_g|\le c_a/g$ on the tube.
- **(H3) Jet bound.** $|F(q,\eta)-F(q,0)|\le c_F(|q||\eta|^2+|\eta|^3)$ on the
  tube, $F=2S-ZS$.
- **(H4) Outside deviation.** $\mathbb E[\mathbf 1_{\rm outside}|\sigma_g-\beta_g|^2\mid Q]\le C_0^{\rm out}$
  for $\theta<\theta_b$, with $\beta_g(q)=F(q,0)/g^3+a_g(q,0)$.
- **(H5) Antipodal region.** $K_g(Q)\le C_{\rm ant}\,g^{-2}$ for
  $\theta\ge\theta_b$, for some fixed $\theta_b\in(0,\pi)$.

**Conclusion.** M10 holds with

\[
C_0=4c_F^2c_6+2c_a^2c_2+C_0^{\rm out},\qquad
C_1=\max\Big(8\pi^2c_F^2c_4,\ \frac{C_{\rm ant}}{v_*(\theta_b)}\Big). \tag{R6}
\]

Proof. For $\theta<\theta_b$: (H3) and (H2) give, pointwise on the tube,
$|\sigma_g-\beta_g|^2\le2g^{-6}c_F^2(2|q|^2|\eta|^4+2|\eta|^6)+2c_a^2g^{-2}|\eta|^2$;
(H1) gives $\mathbb E_{\rm tube}|\sigma_g-\beta_g|^2\le4c_F^2(c_4|q|^2/g^2+c_6)+2c_a^2c_2$,
which is S14. By (R4), $c_4|q|^2/g^2\le2\pi^2c_4W_g$. S15 with tube
probability $p\le1$ and (H4) gives $K_g\le C_0+8\pi^2c_F^2c_4W_g$.
For $\theta\ge\theta_b$: $W_g\ge g^{-2}v_*(\theta_b)$ by (R2) and monotonicity
of $v_*$, so (H5) gives $K_g\le C_{\rm ant}g^{-2}\le(C_{\rm ant}/v_*(\theta_b))W_g$.
Check `W6 M10 reduction: synthesis constants from the five hypotheses` verifies the
two inequalities symbolically, with $|q|^2=2\pi^2g^2W_gs$, $0\le s\le1$, and
$p\in[0,1]$ kept as symbols.

### 2.5 Downstream constants (M11–M15, unchanged)

Given M10 with $(C_0,C_1)$, the source-moment bound $e_g\le E$ and the gap
$\gamma$: M11 reads $\int K_g|f|^2d\nu_g\le C_1b_g[f]+(C_0+C_1E)\|f\|^2$;
$\|f\|^2\le b_g[f]/\gamma$ for centered $f$ gives the M12 coefficient
$C_1+(C_0+C_1E)/\gamma$; the half-support median argument
$\|h\|^2\le2b_g[h]/\gamma$ gives $\mathfrak B_g\le C_1+2(C_0+C_1E)/\gamma$.
Check `W6 M10 reduction: M12 and M15 coefficients from M11` verifies the
algebra. These statements were already established as conditional on M10 in
M.4–M.5 and remain conditional.

---

## 3. An exact obstruction: the naive tube estimate fails near the antipode

By A6 the soft eigenvalue of the fixed-$Q$ Hessian is
$\lambda_{\rm soft}(\delta)=\sqrt2\,\delta-\tfrac{\sqrt2}{8}\delta^2+O(\delta^3)$,
$\delta=\pi-\theta$. If (H1) were obtained from a nine-dimensional Gaussian
comparison with weight $\exp(-\lambda|\eta|^2/g^2)$ direction by direction,
the soft direction would contribute

\[
\mathbb E[\eta_{\rm soft}^2]=\frac{g^2}{2\lambda_{\rm soft}(\delta)}
=\frac{g^2}{2\sqrt2\,\delta}+\frac{g^2}{16\sqrt2}+O(\delta), \tag{R7}
\]

so $c_2(\delta)\ge(2\sqrt2\delta)^{-1}\to\infty$ as $\theta\to\pi$. Hence (H1)
cannot hold with a $\theta$-uniform constant on the full transverse tube up
to the antipode, exactly as S6 warned ("a uniform positive nine-dimensional
conditional Hessian must not be assumed"). The region $\theta\ge\theta_b$
must be handled by (H5), and the two soft directions must be treated by
gauge reduction (A15 at $\theta=\pi$) plus a $\delta$-uniform argument, not by
Gaussian moments. Check `W6 M10 reduction: soft-mode moment diverges like
1/(2 sqrt2 delta)` computes the series (R7) from the A6 branch.

---

## 4. What remains open, stated precisely

### 4.1 Tube obligations (H1)–(H3) for $\theta<\theta_b$

- (H1) with constants uniform in $g$ and $\theta\in[0,\theta_b]$. A Gaussian
  comparison is plausible here because all nine eigenvalues are bounded below
  on $[0,\theta_b]$ (A5, A6), but the comparison must be for the **actual**
  conditional law $A_g^2e^{-2S/g^2}d\eta/Z_g(Q)$, which requires a two-sided
  control of $A_g$ on the tube. S3 gives only the undifferentiated comparison.
- (H2) is a semiclassical derivative bound at scale $1/g$; "interior elliptic
  regularity" gives bounds at a fixed scale and does not by itself give the
  $g$-dependence. This is the differentiated relative-amplitude control S6
  names as the missing premise.
- (H3): the linear term vanishes by (R3). The vanishing of the fast Hessian
  of $F$ at $q=0$ (Euler cancellation) and the third-derivative bound are
  stated in S6 without a written computation for the actual $S$; that
  computation is outstanding.

### 4.2 Rare-fiber obligation (H4)

Two conditional inputs are needed, both uniform in $Q$:

- Conditional mass $\mu_g(|\eta|>\delta_{\rm tube}\mid Q)\le C e^{-2c_{\rm tube}/g^2}$.
  An Agmon estimate relative to the fiber minimum $m(q)$ supplies this only
  together with a lower bound on $\Psi_g$ at $m(q)$ of the same order; that
  lower bound is not in the corpus.
- A conditional fourth moment $\mathbb E[|\sigma_g|^4\mid Q]\le Cg^{-p}$ for
  some $p$. A **global** $L^4(\mu_g)$ bound on $\sigma_g$ does not give this
  on a rare fiber. By (R5) any polynomial $p$ suffices.

### 4.3 Antipodal obligation (H5) for $\theta\ge\theta_b$

A15 gives $d\sigma_g|_{T\mathcal M}=0$ at $\theta=\pi$ exactly. For
$\pi-\delta_0<\theta<\pi$ the near-orbit directions are not gauge, the soft
eigenvalue is $\sqrt2\delta$, and (R7) shows Gaussian moments are not uniform.
Required: $\operatorname{Var}(\sigma_g\mid Q)\le C_{\rm ant}g^{-2}$ uniformly
for $\theta\in[\theta_b,\pi]$, with the angular potential A13 and the
displaced orbit; and a matching of $\theta_b$ with the neighbourhood
$\delta_0$ in which A13 is valid (the region $\theta_b\le\theta\le\pi-\delta_0$
must be covered by one of the two arguments).

---

## 5. Status

- Established here: (R2)–(R7), the conditional synthesis theorem, and the
  soft-mode obstruction. All are exact checks.
- Open: (H1)–(H5), hence M10 and the actual application of M11–M15.
  G19 Priority 1 remains live with these five items as its content.
- The earlier draft's claims that S14, S15 and the antipodal bound were
  "established analytically" are withdrawn.
