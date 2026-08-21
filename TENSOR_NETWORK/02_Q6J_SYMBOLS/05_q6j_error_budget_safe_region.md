# \(q\)-\(6j\) Classical-Limit Error Budget: A Practical “Safe Region” \((\theta, J_{\max})\)

## Purpose

A recurring technical need in the project is to use \(q\)-deformed SU(2) data (especially \(6j_q\) symbols) while controlling how far one is from the classical (\(q\to 1\)) regime.

This note records a computationally grounded bound of the form:

\[
\big| \{6j\}_q - \{6j\} \big|
\;\le\;
C_{\rm global}\,\theta^2\,J_{\max}^{5/2},
\qquad
q=e^{i\theta}.
\]

It then scans a grid to estimate \(C_{\rm global}\) and to give a **“safe region”** where the absolute error stays below a chosen tolerance \(\varepsilon\).

---

## 1. Where the scaling comes from (derivation sketch)

Work in the small-\(\theta\) regime with \(q=e^{i\theta}\).

### 1.1 \(q\)-numbers

The standard \(q\)-number is
\[
[n]_q = \frac{\sin(n\theta)}{\sin\theta}.
\]
Expand \(\sin(n\theta)=n\theta - \frac{n^3\theta^3}{6}+O(\theta^5 n^5)\) and \(\sin\theta=\theta - \frac{\theta^3}{6}+O(\theta^5)\), giving:
\[
[n]_q = n\left(1 - \frac{(n^2-1)\theta^2}{6} + O(\theta^4 n^4)\right).
\]
So \([n]_q - n = O(\theta^2 n^3)\).

### 1.2 \(q\)-factorials and Racah sums

The \(6j\) symbol can be written in terms of triangle factors \(\Delta\) (products/ratios of factorials) times a Racah sum of alternating terms.

Heuristically:

- each \(\log([k]_q)\) differs from \(\log(k)\) by \(O(\theta^2 k^2)\),
- summing \(\log([k]_q)\) up to \(k\sim J_{\max}\) gives \(O(\theta^2 J_{\max}^3)\),
- the Racah sum length scales like \(O(J_{\max})\),
- typical magnitudes for tetrahedrally symmetric families contribute additional algebraic factors.

This motivates a conservative absolute scaling \(\theta^2 J_{\max}^{5/2}\) (empirical in this project; the exact power is a “budget” rather than a theorem).

The key practical point: **error grows quadratically in \(\theta\)** and superlinearly in \(J_{\max}\).

---

## 2. Scanner code (JAX) and output

The experiment focuses on a “family” where all six spins are equal:
\[
a=b=c=d=e=f=j,
\qquad j\in\{1/2, 1, 3/2, \dots, J_{\max}\}.
\]
It computes
\[
\max_{j\le J_{\max}} |\{6j\}_q-\{6j\}|,
\]
then forms
\[
C(J_{\max},\theta)=\frac{\max|\delta|}{\theta^2 J_{\max}^{5/2}},
\qquad
C_{\rm global}=\max_{\text{grid}} C(J_{\max},\theta).
\]

Reference excerpt:

```python
def test_family(J_max_float, theta):
    J_max = int(2*J_max_float)      # doubled spins
    js_doubled = list(range(1, J_max+1))
    errors = []
    for a in js_doubled:
        s  = sixj(a,a,a,a,a,a)              # classical
        sq = sixj_q(a,a,a,a,a,a, theta)     # q-deformed
        errors.append(abs(sq - s))
    max_err = max(errors)
    scale = theta**2 * (J_max_float ** 2.5)
    ratio = max_err / scale
    return float(max_err), float(ratio)

def scan_C_and_safe_region(J_max_list, theta_list, eps=1e-3):
    records = []
    C_global = 0.0
    for J_max in J_max_list:
        for th in theta_list:
            max_err, C = test_family(J_max, th)
            C_global = max(C_global, C)
            safe = (max_err <= eps)
            records.append((J_max, th, max_err, C, safe))
    return C_global, records
```

### 2.1 Numerical output (grid scan)

Using:
- \(J_{\max}\in\{2,3,4,5\}\),
- \(\theta\in\{0.01,0.02,0.05,0.08\}\),
- tolerance \(\varepsilon=10^{-3}\),

the scan reported:

\[
C_{\rm global} \approx 1.8301\times 10^{-1}.
\]

Selected safe/unsafe outcomes:

| \(J_{\max}\) | \(\theta\) | \(\max|\delta|\) | safe under \(\varepsilon=10^{-3}\)? |
|---:|---:|---:|:---:|
| 2 | 0.01 | \(1.001\times 10^{-4}\) | ✅ |
| 2 | 0.02 | \(4.009\times 10^{-4}\) | ✅ |
| 2 | 0.05 | \(2.534\times 10^{-3}\) | ❌ |
| 2 | 0.08 | \(6.626\times 10^{-3}\) | ❌ |
| 3 | 0.01 | \(1.001\times 10^{-4}\) | ✅ |
| 3 | 0.02 | \(4.009\times 10^{-4}\) | ✅ |
| 3 | 0.05 | \(2.534\times 10^{-3}\) | ❌ |
| 4 | 0.02 | \(6.123\times 10^{-4}\) | ✅ |
| 5 | 0.02 | \(1.136\times 10^{-3}\) | ❌ (just above) |

So, for this family and tolerance, **\(\theta\le 0.02\)** is typically safe up to \(J_{\max}\approx 4\), and **\(J_{\max}=5\)** wants \(\theta\approx 0.01\).

---

## 3. How to actually use this (engineering rule)

Given \(C_{\rm global}\), a simple parameter budget is:

\[
\theta \;\le\; \sqrt{\frac{\varepsilon}{C_{\rm global} J_{\max}^{5/2}}}.
\]

This gives a fast “clamp” condition for tensor-network or RG runs that must remain close to classical SU(2).

---

## 4. What would make this more robust (future work)

1. Expand the scan beyond the symmetric family \(j,j,j,j,j,j\); sample random admissible sextuples.
2. Increase arithmetic precision (mpmath / quad precision) to ensure the observed errors are not numerical.
3. Derive a sharper analytic bound on \(\{6j\}_q-\{6j\}\) using stationary-phase / Ponzano–Regge asymptotics with explicit remainder.
4. Track not just absolute error but *relative error* where \(\{6j\}\) is small.

---

## Sources used

- `12-2-25 code runs 3.pdf` (full q-number, log-factorial, Racah sum implementations; scan output; estimated \(C_{\rm global}\) and safe region).
- `CHAT YANG SIMULATION 4x4.txt` (program context: using this as an RG “safe region”).
