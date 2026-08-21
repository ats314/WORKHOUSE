# L=64 Projected-Capacity Critical Threshold Law

## Status

This is a finite-dimensional spectral result and numerical threshold-law diagnostic. It is not a Yang-Mills mass-gap proof. It does not prove the Wilson-measure stochastic theorem. It does establish, in a controlled synthetic setting, that projected capacity is a genuine predictive variable for low-mode instability after density and local cluster geometry are fixed.

The core conclusion is:

\[
\boxed{\text{Projected capacity predicts the critical sparse-defect strength for low-mode instability.}}
\]

More precisely, for fixed-local-geometry dimer defect sets on the periodic two-dimensional lattice at \(L=64\), the scalar

\[
R_{\mathrm{nonzero}}(D)=\|P_{\mathrm{nonzero}}1_D P_{\mathrm{nonzero}}\|
\]

orders the exact projected Birman--Schwinger critical threshold

\[
V_c^{BS}(D)=\left\|\Lambda^{-1/2}G_D\Lambda^{-1/2}\right\|^{-1},
\qquad
G_D=P_{\mathrm{nonzero}}1_D P_{\mathrm{nonzero}}.
\]

The cheaper scalar surrogate

\[
V_c^R(D)=\frac{\lambda_1}{R_{\mathrm{nonzero}}(D)}
\]

tracks \(V_c^{BS}\) strongly, with a stable calibration factor across defect-arrangement families.

---

## 1. Experimental object

Work on the periodic lattice

\[
\mathbb T_L^2,\qquad L=64,
\qquad N=L^2=4096.
\]

Use the nonzero low Fourier sector of the periodic lattice Laplacian:

\[
P=P_{\mathrm{nonzero},K},
\qquad K=128.
\]

The first nonzero eigenvalue and low-window maximum were

\[
\lambda_1=0.009630546655606143,
\qquad
\lambda_{\max,K}=0.37549021458844867.
\]

For a defect set \(D\subset\mathbb T_L^2\), define

\[
G_D=P1_D P.
\]

The projected low-sector Hamiltonian is

\[
H_K(V,D)=\Lambda - V G_D,
\]

where \(\Lambda=\operatorname{diag}(\lambda_k)\) is the diagonal low-mode Laplacian spectrum.

The exact finite-dimensional instability threshold is the value of \(V\) where

\[
\lambda_{\min}(H_K(V,D))=0.
\]

---

## 2. Exact Birman--Schwinger threshold

### Proposition: finite-dimensional projected BS threshold

Let \(\Lambda\) be positive diagonal and let \(G_D\succeq0\). Then

\[
H_K(V,D)=\Lambda - V G_D
\]

has a zero eigenvalue exactly when

\[
V\,\lambda_{\max}\!\left(\Lambda^{-1/2}G_D\Lambda^{-1/2}\right)=1.
\]

Therefore the exact critical coupling is

\[
\boxed{
V_c^{BS}(D)=
\left\|\Lambda^{-1/2}G_D\Lambda^{-1/2}\right\|^{-1}.
}
\]

### Proof

Since \(\Lambda\succ0\),

\[
\Lambda - VG_D \succeq 0
\]

is equivalent, after conjugation by \(\Lambda^{-1/2}\), to

\[
I - V\Lambda^{-1/2}G_D\Lambda^{-1/2}\succeq0.
\]

The first loss of positivity occurs when

\[
V\,\lambda_{\max}(\Lambda^{-1/2}G_D\Lambda^{-1/2})=1.
\]

This gives the stated formula.

---

## 3. Scalar projected-capacity surrogate

The exact BS score uses spectral weights \(\lambda_k^{-1}\). The cheaper scalar capacity ignores those weights and keeps only

\[
R_{\mathrm{nonzero}}(D)=\|G_D\|.
\]

The corresponding scalar threshold estimate is

\[
\boxed{
V_c^R(D)=\frac{\lambda_1}{R_{\mathrm{nonzero}}(D)}.
}
\]

This estimate is not expected to be exactly normalized because replacing \(\Lambda\) by \(\lambda_1 I\) discards the spectral distribution of the top \(G_D\)-direction. The question is whether it orders the threshold robustly.

---

## 4. Fixed-local-geometry ensemble

The run deliberately removed the obvious confounds. Every mask had exactly:

\[
m=128,
\qquad
\rho=0.03125,
\qquad
\text{cluster count}=64,
\qquad
\text{largest cluster}=2.
\]

Equivalently, each defect set was composed of \(64\) separated dimers.

What varied was only the long-range arrangement of those dimers. The mask families were:

- random dimers,
- stripe dimers,
- ring dimers,
- low-mode-biased \(x\)-direction dimers,
- low-mode-biased diagonal dimers,
- blue-noise dimers.

Thus any threshold variation cannot be attributed to raw density, defect count, cluster count, or largest local cluster.

---

## 5. Main numerical threshold results

The global threshold diagnostics were:

\[
\operatorname{corr}(V_c^R,V_c^{BS})=0.9581230919858064,
\]

\[
\operatorname{corr}(\log V_c^R,\log V_c^{BS})=0.9599848701034337.
\]

The raw scalar threshold has a systematic scale offset:

\[
\frac{V_c^R}{V_c^{BS}}
\approx
0.3418555180839468
\pm
0.02865366354277507.
\]

The coefficient of variation is

\[
\frac{\sigma}{\mu}=0.08381805185820874.
\]

So \(V_c^R\) is not absolutely normalized, but the ratio is stable enough to function as a calibrated order parameter.

---

## 6. Calibrated scalar law

The fitted scalar collapse law was

\[
\boxed{
\log V_c^{BS}
=
1.66154015
+
1.21614844\log V_c^R.
}
\]

Fit quality:

\[
R^2=0.9215709508275064,
\]

\[
\mathrm{MAE}_{\log}=0.05625217922082485,
\]

\[
\mathrm{MAE}_{V_c}=0.011484055916001108.
\]

Equivalent raw-form model:

\[
V_c^{BS}
\approx
\exp(1.66154015)\,(V_c^R)^{1.21614844}.
\]

Since

\[
V_c^R=\frac{\lambda_1}{R_{\mathrm{nonzero}}},
\]

this says, empirically on the fixed-local-geometry ensemble,

\[
\boxed{
V_c^{BS}(D)
\approx
\exp(1.66154015)
\left(
\frac{\lambda_1}{\|P1_D P\|}
\right)^{1.21614844}.
}
\]

---

## 7. Heldout prediction results

### Mask-heldout CV

Target: \(\log V_c^{BS}\).

| Model | MAE | R² |
|---|---:|---:|
| scalar capacity | 0.028262 | 0.978415 |
| scalar plus alignment | 0.028642 | 0.978001 |
| geometry, no capacity | 0.030109 | 0.975492 |
| local only | 0.216970 | -0.034762 |

Scalar improvement over geometry-only:

\[
0.03010927719360353-0.02826224326563742
=0.0018470339279661081.
\]

This is a modest but positive improvement in random mask-heldout prediction.

### Family-heldout CV

Target: \(\log V_c^{BS}\).

| Model | MAE | R² |
|---|---:|---:|
| scalar capacity | 0.153438 | -72.530196 |
| scalar plus alignment | 0.153712 | -71.669784 |
| geometry, no capacity | 0.179924 | -87.192189 |
| local only | 0.245234 | -181.937549 |

Scalar improvement over geometry-only:

\[
0.17992422836140418-0.15343764944787
=0.026486578913534176.
\]

The negative family-heldout \(R^2\) values show that leaving out entire synthetic families is a hard extrapolation problem. But scalar capacity still gives the best MAE and improves materially over geometry-only.

---

## 8. Family threshold summary

| Family | R mean | R std | B0 mean | B0 std | Vc BS mean | Vc BS std | Vc R mean | Vc R std | ratio mean | ratio std |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| blue_noise_dimers | 0.106183 | 0.002768 | 3.432189 | 0.078997 | 0.291504 | 0.006530 | 0.090759 | 0.002429 | 0.311585 | 0.013312 |
| lowmode_biased_diag | 0.138087 | 0.008458 | 5.210603 | 0.332743 | 0.192680 | 0.012433 | 0.069993 | 0.004230 | 0.363966 | 0.021676 |
| lowmode_biased_x | 0.143193 | 0.009576 | 4.837252 | 0.297986 | 0.207454 | 0.012212 | 0.067549 | 0.004549 | 0.326197 | 0.022584 |
| random_dimers | 0.130328 | 0.009720 | 4.401002 | 0.267303 | 0.228038 | 0.013945 | 0.074284 | 0.005420 | 0.325946 | 0.017776 |
| ring_dimers | 0.167012 | 0.010683 | 6.068882 | 0.443105 | 0.165606 | 0.011802 | 0.057894 | 0.003736 | 0.350397 | 0.021269 |
| stripe_dimers | 0.197039 | 0.005686 | 7.628295 | 0.150743 | 0.131140 | 0.002590 | 0.048916 | 0.001418 | 0.373041 | 0.009574 |

The ordering is physically sensible: stripe and ring families have larger projected capacity and lower critical thresholds; blue-noise masks have lower projected capacity and higher critical thresholds.

---

## 9. Ridge diagnostic

For \(\log V_c^{BS}\), the ridge model gave:

\[
R^2=0.9809765194084719,
\qquad
\mathrm{MAE}=0.026854092700190322.
\]

The largest scaled coefficients were dominated by low Fourier amplitudes and \(\log V_c^R\):

| Feature | scaled coefficient |
|---|---:|
| fourier_02 | -0.089439 |
| fourier_11 | -0.075698 |
| fourier_01 | -0.066495 |
| topG_energy_harmonic | 0.040628 |
| fourier_10 | -0.039994 |
| log_Vc_R | 0.034438 |
| mean_pair_distance | 0.031204 |
| R_nonzero | -0.022983 |

This says the scalar capacity is not the only correlating descriptor, but it is the compact operator-level object that improves heldout prediction without needing a manually chosen Fourier feature set.

---

## 10. Interpretation

The result upgrades the previous regression finding into a threshold statement.

Previous result:

\[
V_0R_{\mathrm{nonzero}}
\quad\text{predicts projected binding and low-mode defect mass.}
\]

New result:

\[
\boxed{
R_{\mathrm{nonzero}}
\quad\text{predicts the critical defect strength }V_c.
}
\]

This is stronger because the critical threshold is a structural object, not merely a fitted response variable.

The finite-dimensional exact threshold is given by Birman--Schwinger. The nontrivial empirical point is that the cheaper capacity scalar

\[
\|P1_D P\|
\]

tracks the exact BS threshold across long-range arrangements while density and local cluster geometry are fixed.

In plain language:

> Two defect sets can have identical defect count, identical density, identical cluster count, and identical largest local cluster, but differ in how dangerous they are to low modes. Projected capacity detects that difference.

---

## 11. Relation to PMBSF

This synthetic result is aligned with the PMBSF architecture:

\[
\Pi M^{-1}\Pi
\quad\text{and}\quad
\Pi 1_D \Pi
\]

are not decorative. They measure how defect geometry couples into the physical/low spectral sector.

The threshold-law experiment supports the conceptual claim:

\[
\boxed{
\text{sparse defects matter through projected spectral capacity, not only through density or local clustering.}
}
\]

It does not prove the Wilson stochastic theorem. It does not prove Yang--Mills mass gap. It gives a clean controlled model where the operator quantity central to the PMBSF program has demonstrable predictive content.

---

## 12. Separate branch: v17b smooth-source cumulants

The uploaded `PMBSF_v17b_BS_smooth_source_connected_cumulants_GOOD` run is a separate diagnostic for Balaban smooth-source connected cumulants.

Its own status statement says it does not prove BS; it tests whether the expected connected coefficient hierarchy is numerically plausible.

The useful reading is:

- rooted burdens remain small even where \(q^{-k}\)-normalized cumulants look large;
- pair decay has positive signs in many rows but remains noisy;
- jackknife uncertainty remains large in worst rows;
- the run is useful as a diagnostic but not theorem-grade evidence.

This branch should not be confused with the L=64 projected-capacity critical-threshold result.

---

## 13. Final preserved claim

The clean result to preserve is:

\[
\boxed{
\begin{aligned}
&\text{For fixed-local-geometry sparse dimer masks on }\mathbb T_{64}^2,\\[2mm]
&V_c^{BS}(D)
=\left\|\Lambda^{-1/2}P1_D P\Lambda^{-1/2}\right\|^{-1}\\[2mm]
&\text{is strongly predicted by}\quad
V_c^R(D)=\frac{\lambda_1}{\|P1_D P\|}.
\end{aligned}
}
\]

Empirical calibration:

\[
\boxed{
\log V_c^{BS}
=
1.66154015
+
1.21614844\log\left(\frac{\lambda_1}{\|P1_D P\|}\right),
\qquad
R^2=0.92157.
}
\]

Interpretive statement:

\[
\boxed{
\text{Projected capacity is a threshold-order parameter for sparse-defect low-mode instability in this controlled finite-dimensional system.}
}
\]
