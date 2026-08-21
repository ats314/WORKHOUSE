# M3a Reduction and First Breach Point

**Date:** June 12, 2026  
**Scope:** SU(2) PMBSF stochastic-sparsity input  
**Status:** Exact deterministic reduction proved below; Theorems Z.A and Z.B remain the two open analytic inputs.

## 1. Source variables

Let \(\mathcal P\) be a finite plaquette set and let

\[
0\le X_{p,\eta}\le 1,
\qquad
q_\eta:=\mathbb E_\mu X_{p,\eta}>0,
\]

where in the SU(2) Wilson application

\[
X_{p,\eta}=f_\eta\!\bigl(\phi(U_p)-t\bigr),
\qquad
\phi(U_p)=1-\frac12\operatorname{ReTr}U_p.
\]

For a finite source set \(A\subset\mathcal P\) and \(s\ge0\), define

\[
Z_A(s):=\mathbb E_\mu\prod_{r\in A}(1+sX_{r,\eta})
\]

and the source-tilted measure

\[
\mathbb E_{A,s}[F]
:=
\frac{\mathbb E_\mu\left[F\prod_{r\in A}(1+sX_{r,\eta})\right]}{Z_A(s)}.
\]

All coefficients of \(Z_A\) are nonnegative.

## 2. The two open inputs in canonical form

Fix a good local-cap-intersection event \(\mathcal G_p\), constants
\(C_{\rm LCI},C_B,J_*<\infty\), and a source radius \(\rho_0>0\).
The required uniformity range is

\[
0\le s\le \frac{\rho_0}{q_\eta}.
\]

### Theorem Z.A — LCI typicality

For every finite \(A\subset\mathcal P\setminus\{p\}\),

\[
\mathbb E_{A,s}
\left[X_{p,\eta}\mathbf 1_{\mathcal G_p}\right]
\le C_{\rm LCI}q_\eta.
\tag{Z.A}
\]

### Theorem Z.B — Bałaban far-source stability

There is a nonnegative remainder \(Y_p^{\rm LCI}\) satisfying

\[
X_{p,\eta}\mathbf 1_{\mathcal G_p^c}
\le Y_p^{\rm LCI}
\]

and, uniformly in the same source family,

\[
\mathbb E_{A,s}Y_p^{\rm LCI}
\le C_Be^{J_*}q_\eta.
\tag{Z.B}
\]

Set

\[
C_{\rm TOS}:=C_{\rm LCI}+C_Be^{J_*}.
\tag{2.1}
\]

## 3. Z.A + Z.B imply tilted one-site stability

Splitting into the good and bad sectors gives

\[
\mathbb E_{A,s}X_{p,\eta}
\le C_{\rm TOS}q_\eta.
\tag{3.1}
\]

This is the tilted one-site estimate (TOS). No independence is used.

## 4. Positive source radius

Order \(A=\{p_1,\ldots,p_n\}\) and write \(A_j=\{p_1,\ldots,p_j\}\).
The exact telescoping identity is

\[
\frac{Z_{A_j}(s)}{Z_{A_{j-1}}(s)}
=
1+s\,\mathbb E_{A_{j-1},s}X_{p_j,\eta}.
\]

Take \(s=\rho/q_\eta\), where \(0<\rho\le\rho_0\). By (3.1),

\[
\frac{Z_{A_j}(\rho/q_\eta)}{Z_{A_{j-1}}(\rho/q_\eta)}
\le 1+\rho C_{\rm TOS}
\le e^{\rho C_{\rm TOS}}.
\]

Multiplication gives

\[
\boxed{
Z_A(\rho/q_\eta)
\le
\exp\!\left(\rho C_{\rm TOS}|A|\right).
}
\tag{4.1}
\]

## 5. Lemma Q

For \(B\subset\mathcal P\), \(|B|=n\), nonnegative coefficient extraction gives

\[
\left(\frac{\rho}{q_\eta}\right)^n
\mathbb E_\mu\prod_{p\in B}X_{p,\eta}
\le Z_B(\rho/q_\eta).
\]

Combining with (4.1),

\[
\boxed{
\mathbb E_\mu\prod_{p\in B}X_{p,\eta}
\le
\left(C_Q(\rho)q_\eta\right)^{|B|},
\qquad
C_Q(\rho):=\rho^{-1}e^{\rho C_{\rm TOS}}.
}
\tag{5.1}
\]

This is Lemma Q/(M').

### Correct optimization

The logarithmic derivative is

\[
\frac{d}{d\rho}\log C_Q(\rho)
=-\frac1\rho+C_{\rm TOS}.
\]

Therefore

\[
\rho_*=
\min\!\left\{\rho_0,\frac1{C_{\rm TOS}}\right\}.
\tag{5.2}
\]

If \(\rho_0\ge C_{\rm TOS}^{-1}\), then

\[
\boxed{C_Q^{\rm opt}=e\,C_{\rm TOS}.}
\tag{5.3}
\]

The previously recorded value \(e^{C_{\rm TOS}}\) does not follow from
\(C_Q(\rho)=\rho^{-1}e^{\rho C_{\rm TOS}}\); it is an algebraic typo.

## 6. Pair-covariance consequence and the pass-10 target

For distinct plaquettes \(p,r\), Lemma Q gives

\[
\mathbb E[X_{p,\eta}X_{r,\eta}]
\le C_Q^2q_\eta^2.
\]

Under translation invariance, \(\mathbb E X_{p,\eta}=q_\eta\), hence

\[
\operatorname{Cov}(X_{p,\eta},X_{r,\eta})
\le (C_Q^2-1)q_\eta^2
\]

for the positive part, and the unconditional absolute estimate

\[
\left|\operatorname{Cov}(X_{p,\eta},X_{r,\eta})\right|
\le (C_Q^2+1)q_\eta^2.
\tag{6.1}
\]

For PTO weights

\[
w_{pr}:=\operatorname{tr}(A_pA_r),
\qquad
A_p=P_{\le\Lambda,L}\mathbf1_{\partial p}P_{\le\Lambda,L},
\]

(6.1) yields

\[
\max_p\sum_{r\ne p}w_{pr}
\left|\operatorname{Cov}(X_{p,\eta},X_{r,\eta})\right|
\le
(C_Q^2+1)q_\eta^2
\max_p\sum_{r\ne p}w_{pr}.
\tag{6.2}
\]

The pass-10 local target is the sharper conditional statement

\[
\boxed{
W_e(U):=
\max_{p\ni e}
\sum_{r\ni e,\ r\ne p}
|C_e(p,r;U)|\,w_{pr}
\le C_{\rm HB}q_\eta^2
}
\tag{6.3}
\]

on an LCI-good environment, with the old-bad contribution handled separately.
Here \(C_e\) is covariance under the exact one-link SU(2) heat-bath law.
This is the first numerically falsifiable breach point for Z.A.

Pair covariance alone does **not** imply the all-order source bound (4.1);
Z.A requires uniform control under arbitrary positive source tilts. The correct
local diagnostic is therefore the rooted ratio

\[
R_{p,A}(\rho;U)
:=
\frac{
\mathbb E_{\nu_e}
\left[X_{p,\eta}
\prod_{r\in A}(1+(\rho/q_\eta)X_{r,\eta})\right]
}{
q_\eta\,
\mathbb E_{\nu_e}
\left[\prod_{r\in A}(1+(\rho/q_\eta)X_{r,\eta})\right]
}.
\tag{6.4}
\]

A volume-stable upper tail for (6.4), together with the far-source theorem Z.B,
is the direct route to M3a.

## 7. Current boundary

The deterministic chain

\[
\text{Z.A + Z.B}
\Longrightarrow
\text{TOS}
\Longrightarrow
\text{positive source radius}
\Longrightarrow
\text{Lemma Q}
\]

is complete, with the correction (5.3). The remaining mathematics is exactly:

1. prove the LCI-good rooted bound Z.A;
2. prove the far-source remainder bound Z.B.

The companion script `m3a_stage_c_exact_hb_lci_probe.py` attacks item 1 by
sampling the exact SU(2) one-link heat-bath law and enumerating all local source
subsets around the updated link.
