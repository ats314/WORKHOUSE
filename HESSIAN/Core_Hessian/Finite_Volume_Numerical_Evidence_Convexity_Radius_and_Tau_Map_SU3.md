# Finite-Volume Numerical Evidence: Convexity Radius \(R(\beta)\) and Restoration Time \(\tau(\beta,r)\) (SU(3), 4D lattice)

## Scope and status

This document records numerical outputs produced in the chat for SU(3) lattice Yang–Mills in 4D using exponential coordinates \(U_\ell = \exp(A_\ell)\), with \(A_\ell \in \mathfrak{su}(3)\), and an auxiliary quadratic “Haar mass” term of strength \(c_0\).

**Epistemic status:** numerical evidence only. No statement below is a proof of any analytic inequality or of any continuum-limit claim.

---

## A. Numerical definition of “convexity” used in the scans

For fixed lattice size \(L\), inverse coupling \(\beta\), and amplitude (“scale”) \(r\), the code:

1. draws i.i.d. random field samples \(A\) with entries \(A_\ell\) drawn from a centered normal distribution and scaled so that typical magnitude is \(r\);
2. forms an action
   \[
   S(A) \;=\; S_{\mathrm{W}}(A;\beta) \;+\; S_{\mathrm{Haar}}(A;c_0),
   \]
   where \(S_{\mathrm{W}}\) is the Wilson plaquette action (implemented via plaquette products of \(\exp(A_\ell)\)), and
   \[
   S_{\mathrm{Haar}}(A;c_0) \;=\; c_0 \sum_\ell \operatorname{Tr}(A_\ell^\dagger A_\ell)
   \]
   (as implemented in code);
3. estimates the minimal Hessian eigenvalue
   \[
   \lambda_{\min}(A) := \lambda_{\min}(\nabla^2 S(A))
   \]
   by a Lanczos routine using Hessian–vector products computed by JAX automatic differentiation.

A point \((\beta,r)\) is declared **convex** if the *minimum over samples* of the estimated \(\lambda_{\min}\) is strictly positive:
\[
\min_{i=1,\dots,n_{\mathrm{samples}}} \lambda_{\min}(A^{(i)}) \;>\; 0.
\]
This is a **conservative** criterion, but it is still sample-based.

---

## B. Three-volume convexity comparison at scale \(r=0.05\)

The chat included three datasets \(L\in\{4,6,8\}\) giving \(\lambda_{\min}\) vs \(\beta\) at scale \(r=0.05\) (and, for \(L=4,6\), also at \(r\in\{0.10,0.15\}\)).

### B.1. Extracted \(r=0.05\) curves

#### \(L=4\) (subset at \(r=0.05\))
\[
(\beta,\lambda_{\min}) \in \{
(0.40,0.107639),
(0.77,0.090999),
(1.14,0.074027),
(1.51,0.058620),
(1.89,0.042761),
(2.26,0.024951),
(2.63,0.006105),
(3.00,-0.008208)
\}.
\]

#### \(L=6\) (subset at \(r=0.05\))
\[
(\beta,\lambda_{\min}) \in \{
(0.40,0.108966),
(0.77,0.093839),
(1.14,0.079105),
(1.51,0.063542),
(1.89,0.048837),
(2.26,0.033850),
(2.63,0.018730),
(3.00,0.003391)
\}.
\]

#### \(L=8\) (subset at \(r=0.05\))
\[
(\beta,\lambda_{\min}) \in \{
(0.40,0.109223),
(0.77,0.094255),
(1.14,0.079963),
(1.51,0.064737),
(1.89,0.050365),
(2.26,0.035428),
(2.63,0.021559),
(3.00,0.006509)
\}.
\]

### B.2. Interpretation (numerical only)

- Across these three volumes, the reported \(r=0.05\) curves are close.
- For \(L=4\), the reported \(\lambda_{\min}\) becomes negative by \(\beta=3.00\), whereas for \(L=6,8\) it remains positive at \(\beta=3.00\) at this scale.
- This is consistent with finite-volume effects at the threshold, but no quantitative finite-size scaling analysis is included in the chat excerpt.

---

## C. Bisection-estimated convexity radius \(R(\beta)\) at \(L=8\)

A separate routine estimated a critical amplitude \(R(\beta)\) by bisection, using the conservative rule “convex if all samples have \(\lambda_{\min}>0\)”.

### C.1. Reported \(R(\beta)\) data (L=8)

| \(\beta\) | \(R(\beta)\) |
|---:|---:|
| 0.40 | 0.24488281250000005 |
| 0.80 | 0.14542968750000002 |
| 1.20 | 0.1038671875 |
| 1.60 | 0.0816015625 |
| 2.00 | 0.0682421875 |
| 2.40 | 0.05785156250000001 |
| 2.80 | 0.051171875000000006 |
| 3.20 | 0.045976562500000005 |

**Runtime note:** the run reported \(\approx 1361\) seconds.

### C.2. Minimal methodological caveats

- The output depends on: number of samples per bisection point, Lanczos truncation \(k\), and random seed policy.
- The decision rule is discontinuous in finite samples. Small changes in sample count can shift the estimated boundary.
- No systematic error bars are reported.

---

## D. Dynamic restoration under gradient flow (single run)

A gradient flow routine was executed at parameters intended to be “deep unstable”:
- \(L=8\),
- \(\beta=3.00\),
- scale \(r=0.15\),
- \(c_0=0.125\),
- step size \(dt=0.005\).

The run reported:
- initial \(\lambda_{\min} \approx -0.350166\),
- restored to \(\lambda_{\min} \approx +0.001775\) at flow time \(t=0.260\) (step 52),
- total wall time \(\approx 67.79\) seconds.

**Status:** this is a single-sample numerical observation, not a theorem. It does not establish a uniform restoration mechanism in any parameter limit.

---

## E. Partial \(\tau(\beta,r)\) map (fast run)

A “fast” restoration-time map output was pasted for \(\beta\in\{0.40,0.96,1.52,2.08,2.64,3.20\}\) and \(r\in[0.04,0.24]\) (10 values per \(\beta\)). Values were reported on a discrete grid of \(\tau\) values (multiples of \(dt\)).

The raw tuples were printed in the form \((\beta,r,\tau)\); they are preserved below as-is.

### E.1. Raw \((\beta,r,\tau)\) tuples (as pasted)

#### \(\beta=0.40\)
- (0.4, 0.04, 0.0)
- (0.4, 0.06222222222222222, 0.0)
- (0.4, 0.08444444444444443, 0.0)
- (0.4, 0.10666666666666666, 0.0)
- (0.4, 0.1288888888888889, 0.0)
- (0.4, 0.1511111111111111, 0.0)
- (0.4, 0.1733333333333333, 0.0)
- (0.4, 0.19555555555555554, 0.0)
- (0.4, 0.21777777777777776, 0.0)
- (0.4, 0.24, 0.0)

#### \(\beta=0.96\)
- (0.9600000000000001, 0.04, 0.0)
- (0.9600000000000001, 0.06222222222222222, 0.0)
- (0.9600000000000001, 0.08444444444444443, 0.0)
- (0.9600000000000001, 0.10666666666666666, 0.0)
- (0.9600000000000001, 0.1288888888888889, 0.0)
- (0.9600000000000001, 0.1511111111111111, 0.16)
- (0.9600000000000001, 0.1733333333333333, 0.24)
- (0.9600000000000001, 0.19555555555555554, 0.32)
- (0.9600000000000001, 0.21777777777777776, 0.4)
- (0.9600000000000001, 0.24, 0.48)

#### \(\beta=1.52\)
- (1.52, 0.04, 0.0)
- (1.52, 0.06222222222222222, 0.0)
- (1.52, 0.08444444444444443, 0.0)
- (1.52, 0.10666666666666666, 0.08)
- (1.52, 0.1288888888888889, 0.16)
- (1.52, 0.1511111111111111, 0.24)
- (1.52, 0.1733333333333333, 0.32)
- (1.52, 0.19555555555555554, 0.4)
- (1.52, 0.21777777777777776, 0.4)
- (1.52, 0.24, 0.48)

#### \(\beta=2.08\)
- (2.08, 0.04, 0.0)
- (2.08, 0.06222222222222222, 0.0)
- (2.08, 0.08444444444444443, 0.08)
- (2.08, 0.10666666666666666, 0.16)
- (2.08, 0.1288888888888889, 0.24)
- (2.08, 0.1511111111111111, 0.24)
- (2.08, 0.1733333333333333, 0.32)
- (2.08, 0.19555555555555554, 0.4)
- (2.08, 0.21777777777777776, 0.4)
- (2.08, 0.24, 0.48)

#### \(\beta=2.64\)
- (2.64, 0.04, 0.0)
- (2.64, 0.06222222222222222, 0.08)
- (2.64, 0.08444444444444443, 0.16)
- (2.64, 0.10666666666666666, 0.16)
- (2.64, 0.1288888888888889, 0.24)
- (2.64, 0.1511111111111111, 0.28)
- (2.64, 0.1733333333333333, 0.32)
- (2.64, 0.19555555555555554, 0.32)
- (2.64, 0.21777777777777776, 0.4)
- (2.64, 0.24, 0.4)

#### \(\beta=3.20\)
- (3.2, 0.04, 0.0)
- (3.2, 0.06222222222222222, 0.08)
- (3.2, 0.08444444444444443, 0.16)
- (3.2, 0.10666666666666666, 0.16)
- (3.2, 0.1288888888888889, 0.24)
- (3.2, 0.1511111111111111, 0.24)
- (3.2, 0.1733333333333333, 0.32)
- (3.2, 0.19555555555555554, 0.32)
- (3.2, 0.21777777777777776, 0.4)
- (3.2, 0.24, 0.4)

**Interpretation note:** since \(\tau\) is reported in discrete steps and some entries are exactly \(0\), this table is consistent with a threshold behavior (“already convex” vs “requires restoration time”), but it is not sufficient to infer scaling laws without additional controlled runs.

---

## F. Items explicitly not established by this numerical record

- No theorem-level bound of the form \(\lambda_{\min} \ge c_0 - C\beta r^2\) has been proved.
- No uniformity in \(L\to\infty\) or \(a\to 0\) has been established.
- No gauge-fixing, BRST, or OS reconstruction claims follow from this record alone.
