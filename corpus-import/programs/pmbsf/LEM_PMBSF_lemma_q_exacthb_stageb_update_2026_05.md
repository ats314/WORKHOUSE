# Lemma Q Update — Exact Heat-Bath Stage B Geometry Robustness

**Project:** PMBSF projected-capacity / SU(2) Wilson transfer  
**Run:** `PMBSF_SU2_LemmaQ_block_conditional_stageB_heatbath_20260525_215913`  
**Date incorporated:** 2026-05-26  
**Status:** Strongest current side-10/core-margin-3 numerical diagnostic for Lemma Q. This is not a proof of Lemma Q.

---

## 1. Executive update

The Stage B geometry-robustness test has now been repeated with exact SU(2) one-link heat-bath sampling rather than Metropolis block resampling.

The update law is

\[
U_\ell
\sim
\mathrm{vMF}_4
\left(
\frac{\overline H_\ell}{\|H_\ell\|},
\beta\|H_\ell\|
\right),
\]

where \(H_\ell\) is the staple-sum quaternion and the project convention is

\[
\operatorname{Scal}(UH)=U\cdot\overline H.
\]

Thus the heat-bath mean direction is \(\overline H/\|H\|\), not \(H/\|H\|\). The update is exact and has no Metropolis rejection; the reported update statistic is identically \(1\).

This run supersedes the earlier side-10 Metropolis Stage B diagnostic as the primary geometry-robustness evidence. The earlier exact heat-bath side-8 run remains the clean primary conditional-sampling anchor; this new exact heat-bath side-10 run is now the primary larger-geometry anchor.

---

## 2. Configuration

\[
L=16,\qquad
\beta=3.5,\qquad
q_\eta=0.003,\qquad
\eta=0.005.
\]

Global ensemble:

\[
N_{\rm cfg}=32,\qquad
\text{thermal sweeps}=300,\qquad
\text{between sweeps}=30.
\]

Block conditional experiment:

\[
\text{block side}=10,
\qquad
\text{core margin}=3,
\qquad
2\ \text{blocks/config}.
\]

Thus:

\[
64\ \text{frozen-boundary blocks total}.
\]

Each block has:

\[
864\ \text{core plaquettes}.
\]

The core-depth distribution is:

\[
\{3,4\}.
\]

The block heat-bath settings were:

\[
\text{block therm}=192,\qquad
\text{block between}=8,\qquad
\text{block samples}=256.
\]

The run reports reliable distance coverage through

\[
d_{\max}=12.
\]

---

## 3. Thresholding

The corrected proof-friendly upper-envelope ramp smoother was used:

\[
X_{p,\eta}
=
\operatorname{clip}
\left(
\frac{\phi_p-t}{\eta}+1,
0,
1
\right),
\]

so that

\[
\mathbf 1_{\{\phi_p\ge t\}}
\le
X_{p,\eta}
\le
\mathbf 1_{\{\phi_p\ge t-\eta\}}.
\]

This matches the cap-threshold bridge

\[
a_{t-\eta}=1-(t-\eta).
\]

The global thresholding result was:

\[
t=1.0104245908659366,
\]

\[
q_\eta=0.003000000000000041,
\]

\[
q_{\rm hard}=0.0029478073120117188.
\]

Additional plaquette-score statistics:

\[
\mathbb E[\phi]=0.23225818574428558,
\]

\[
\operatorname{std}(\phi)=0.18309813737869263,
\]

\[
\phi_{0.99}=0.8390360474586487,
\qquad
\phi_{0.999}=1.1516469717025757.
\]

---

## 4. Main Lemma Q diagnostics

### 4.1 Single-source conditional control

The maximum depth-median source-rate ratio was

\[
\max_{\rm depth}
\operatorname{median}
\left(
q_{\rm cond}/q_\eta
\right)
=
1.3020833.
\]

The depth-level upper quantile and maximum were

\[
q95(q_{\rm cond}/q_\eta)=2.6041667,
\]

\[
\max(q_{\rm cond}/q_\eta)=9.1145833.
\]

Interpretation:

\[
\mathbb E[X_{p,\eta}\mid \mathcal F_{C^c}]
=
O(q_\eta)
\]

continues to hold numerically at side-10/core-margin-3 exact heat-bath geometry. The maximum is larger than the median but remains a small \(O(1)\) constant rather than runaway amplification.

### 4.2 Ordinary cavity source-stability

The ordinary cavity ratio is

\[
\Lambda
=
\frac{
\mathbb E[X_rX_p\mid\mathcal F_{C^c}]
}{
q_\eta\mathbb E[X_r\mid\mathcal F_{C^c}]
}.
\]

The run reports

\[
\max\Lambda=2.5930038,
\]

\[
\operatorname{median}\Lambda=1.0158112.
\]

Interpretation:

\[
\mathbb E[X_rX_p\mid\mathcal F_{C^c}]
\approx
q_\eta\mathbb E[X_r\mid\mathcal F_{C^c}]
\]

at the median level, with the maximum remaining \(O(1)\). This supports the finite-volume version of

\[
\lambda_p(S\mid\mathcal F_{C^c})
\le
Cq_\eta
\exp\left(\sum_{r\in S}J(p,r)\right).
\]

### 4.3 Rooted bad-staple cavity stability

The rooted cavity ratio is

\[
\Lambda_{\rm root}
=
\frac{
\mathbb E[Y_rX_p\mid\mathcal F_{C^c}]
}{
q_\eta\mathbb E[Y_r\mid\mathcal F_{C^c}]
},
\qquad
Y_r=X_r\mathbf1_{\rm bad}.
\]

The run reports

\[
\max\Lambda_{\rm root}=2.3431348,
\]

\[
\operatorname{median}\Lambda_{\rm root}=1.0221089.
\]

Interpretation:

The rooted bad-staple mechanism remains stable under exact heat-bath side-10 geometry. This matters because the proof architecture does not require unrooted bad-staple rarity. It requires rooted control:

\[
\mathbb E[Y_rX_p\mid\mathcal F_{C^c}]
=
O(q_\eta\mathbb E[Y_r\mid\mathcal F_{C^c}]).
\]

---

## 5. Cap-feature regressions

The run reports directionally correct but weak cap-feature regressions.

For the \(g\)-feature:

\[
\text{slope}_g=-0.17918134,
\qquad
R_g^2=0.0075893205.
\]

For the \(\rho\)-feature:

\[
\text{slope}_\rho=-8.33064,
\qquad
R_\rho^2=0.022467109.
\]

Interpretation:

The signs agree with the heat-bath cap intuition: stronger cap obstruction / alignment features reduce source rates. But the low \(R^2\) values show that the one-link cap predictor is not the whole mechanism.

Therefore this run supports the current analytic conclusion:

\[
\boxed{
\text{Lemma Q should be attacked as block source-stability, not as a pure one-link cap regression theorem.}
}
\]

The one-link cap estimate supplies the local seed. The load-bearing theorem remains TOS+J / LCI plus Balaban far-source stability.

---

## 6. Updated numerical hierarchy

The numerical hierarchy should now be stated as follows.

1. **Primary local conditional-sampling anchor:** exact heat-bath side-8.
2. **Primary geometry-robustness anchor:** exact heat-bath side-10/core-margin-3 Stage B, run `PMBSF_SU2_LemmaQ_block_conditional_stageB_heatbath_20260525_215913`.
3. **Historical geometry supplement:** prior side-10/core-margin-3 Metropolis Stage B.
4. **Global consequence evidence:** full-volume pair/rooted covariance diagnostics through \(L=64\).
5. **Deterministic PMBSF evidence:** PTO / projected Birman-Schwinger / random plaquette-incidence stack.

The old Metropolis Stage B should be demoted to historical/supporting context. The new exact-HB Stage B supersedes it.

---

## 7. Manuscript-safe wording

Use:

> We also performed an exact SU(2) heat-bath side-10/core-margin-3 frozen-block diagnostic at \(L=16,\beta=3.5,q_\eta=0.003,\eta=0.005\). The update law was the exact one-link conditional \(U_\ell\sim \mathrm{vMF}_4(\overline H_\ell/\|H_\ell\|,\beta\|H_\ell\|)\), with acceptance one by construction. Across \(64\) frozen-boundary blocks and \(864\) core plaquettes per block, the median cavity and rooted-cavity ratios were \(1.0158\) and \(1.0221\), respectively, with maxima \(2.5930\) and \(2.3431\). The single-source conditional depth-median maximum was \(1.3021\), with depth-level \(q95=2.6042\). This supports the tempered block source-stability mechanism at larger side-10 geometry, but does not prove Lemma Q.

Do not write:

> Lemma Q is proved numerically.

Do not write:

> The cap predictor explains Lemma Q.

The correct statement is:

\[
\boxed{
\text{Exact heat-bath side-10 data supports block source-stability; the analytic theorem remains open.}
}
\]

---

## 8. Updated proof-stack interpretation

The present run strengthens the numerical support for

\[
\boxed{
\text{TOS+J / positive tilted one-source stability}
}
\]

and for the rooted complement

\[
\boxed{
Y_p=X_p\mathbf1_{\rm bad}
\quad\text{or}\quad
Y_p=X_p\mathbf1_{\rm LCI\ failure}.
}
\]

The analytic stack remains:

\[
\text{local cap-intersection stability}
+
\text{Balaban far-source stability}
\Rightarrow
\text{TOS+J}
\]

\[
\Rightarrow
\text{positive source-radius bound}
\Rightarrow
\text{Lemma Q}
\]

\[
\Rightarrow
\text{rooted cumulants}
\Rightarrow
\text{PMBSF closure}.
\]

This run does not change the proof gap. It makes the numerical evidence for the gap target substantially cleaner.

---

## 9. Ledger entry

**PMBSF_SU2_LEMMAQ_STAGEB_EXACT_HEATBATH_20260525_215913.**  
Exact SU(2) heat-bath side-10/core-margin-3 frozen-block diagnostic completed on NVIDIA L4. Configuration: \(L=16\), \(\beta=3.5\), hot start, exact full-link heat-bath generation, exact frozen-block heat-bath resampling, \(N_{\rm cfg}=32\), thermal_sweeps \(=300\), between_sweeps \(=30\), block side \(10\), core margin \(3\), \(2\) blocks/config, \(64\) frozen-boundary blocks, \(864\) core plaquettes/block, block_therm \(=192\), block_between \(=8\), block_samples \(=256\), \(q_\eta=0.003\), \(\eta=0.005\). The update law was \(U_\ell\sim\mathrm{vMF}_4(\overline H_\ell/\|H_\ell\|,\beta\|H_\ell\|)\), with acceptance one by construction. Thresholding with the proof-friendly upper-envelope ramp gave \(t=1.0104245908659366\), \(q_\eta=0.003000000000000041\), \(q_{\rm hard}=0.0029478073120117188\). Single-source conditional control passed with max depth-median \(q_{\rm cond}/q=1.3020833\), depth-level q95 \(=2.6041667\), and max \(=9.1145833\), with depth bins \([3,4]\). Ordinary cavity source-stability passed with max \(\Lambda=2.5930038\), median \(\Lambda=1.0158112\), and distance bins through \(d=12\). Rooted bad-staple cavity passed with max \(\Lambda_{\rm root}=2.3431348\), median \(\Lambda_{\rm root}=1.0221089\). Cap predictors had directionally correct but weak explanatory power: \(g\)-slope \(-0.17918134\), \(R_g^2=0.0075893205\), \(\rho\)-slope \(-8.33064\), \(R_\rho^2=0.022467109\). Conclusion: exact heat-bath side-10 geometry supports the block source-stability mechanism and supersedes the earlier Metropolis Stage B geometry supplement. Lemma Q remains open analytically.

---

## 10. Final status

This is now the strongest current numerical version of the Lemma Q geometry test.

It supports the claim:

\[
\boxed{
\text{finite-volume exact heat-bath diagnostics support tempered block source-stability.}
}
\]

It does not support the stronger claim:

\[
\boxed{
\text{Lemma Q has been proved.}
}
\]

The next analytic proof target remains:

\[
\boxed{
\text{local cap-intersection stability + Balaban far-source stability}
\Rightarrow
\text{TOS+J}.
}
\]
