# M3a Stage-C Preliminary Exact-HB Result

**Date:** June 12, 2026  
**Engine:** `m3a_stage_c_exact_hb_lci_probe.py`  
**Run used for this note:** deliberately small diagnostic, \(L=4\), \(\beta=3.5\), \(q_\eta=0.003\), \(\eta=0.005\), eight link environments, 4096 deterministic-mixture importance samples per environment.

## Verdict

The calculation identifies the first breach point more sharply:

1. **Un-tilted local rarity passes.** The largest cavity ratio was
   \[
   \max_{e,p}\frac{\mathbb E_{\nu_e}X_{p,\eta}}{q_\eta}
   =1.8495.
   \]

2. **Pair covariance passes the \(q_\eta^2\) scale strongly.** The largest unweighted six-plaquette row sum was
   \[
   \max_e\max_p\sum_{r\ne p}
   \frac{|\operatorname{Cov}_{\nu_e}(X_p,X_r)|}{q_\eta^2}
   =0.5543.
   \]

3. **Arbitrary positive local source tilts fail without an LCI-good restriction.** Enumerating every subset of the other five plaquettes and \(\rho\in\{0.25,0.5,1\}\) produced
   \[
   \max R_{p,A}(\rho;U)=326.24\approx q_\eta^{-1}=333.33.
   \]
   Thus a compatible multi-cap intersection can make the root event nearly certain after source tilting, even though every un-tilted pair covariance is small.

This does not disprove Theorem Z.A as stated with its good-sector restriction. It proves that the restriction is essential and that the pass-10 pair-covariance estimate by itself cannot yield the required all-order source-radius bound.

## Consequence for the proof strategy

The next analytic object is not another covariance estimate. It is a quantitative cap-intersection exclusion/penalty:

\[
\mathbb P_\mu\!\left(
\exists A:\ R_{p,A}(\rho;U)>C_{\rm LCI}
\right)
\]

must be absorbed into \(Y_p^{\rm LCI}\) and controlled by Theorem Z.B, or the good event must impose a deterministic cap-support condition that prevents the compatible intersection.

The exact geometric coordinates already produced by the engine are:

- heat-bath concentration \(\kappa_e\);
- six cap normals \(n_p\);
- tangent correlations at the heat-bath mode;
- the maximizing root/source subset and \(\rho\).

The next code revision should compute the support loss

\[
\Delta_p(A)=h(A)-h(A\cup\{p\}),
\qquad
h(A)=\sup_{u\in\cap_{r\in A}C_r} h_e\cdot u,
\]

for the maximizing subset. That directly tests the cap-Laplace mechanism required by Z.A.

## Qualification

The run is too small for volume-uniform inference. Its role is structural: it separates the successful \(q_\eta^2\) pair scale from the failed unrestricted all-order local source tilt. All implementation gates passed, including exact vMF mean validation, staple identity, calibrated \(q_\eta\), covariance positive-semidefiniteness, and output round-trip.
