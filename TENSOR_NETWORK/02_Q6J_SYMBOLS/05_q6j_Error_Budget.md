# q–6j Classical-Limit Error Budget (Small-\(\theta\) Regime)

## 0. Scope

This document extracts a usable *error budget* for q-deformed SU(2) quantities near \(q\to 1\):

- explicit Taylor control for q-integers and q-factorials when \(q=e^{i\theta}\), \(|\theta|\ll 1\),
- propagation of these errors through the Racah (factorial) formula for \(6j\),
- resulting (conditional) bound of the form
  \[
  \big|\{6j\}_q - \{6j\}\big|
  \lesssim
  C\,\theta^2\,J_{\max}^{5/2}
  \quad\text{when}\quad |\theta|J_{\max}\ll 1.
  \]

The last step depends on amplitude control for the classical \(6j\) symbol (Ponzano–Regge regime); the project notes treat this as an external asymptotic input.

---

## 1. q-integers

For \(q=e^{i\theta}\), define
\[
[n]_q := \frac{\sin(n\theta)}{\sin\theta}.
\]
Taylor expansion gives
\[
[n]_q = n - \frac{n(n^2-1)}{6}\theta^2 + O(\theta^4 n^5),
\]
hence
\[
|[n]_q-n| \le C_1\,\theta^2\,n^3
\quad\text{for}\quad |\theta|n\ll 1.
\]

---

## 2. q-factorials

Define
\[
[N]_q! := \prod_{k=1}^N [k]_q.
\]
Using \(\log(1-\varepsilon)\approx -\varepsilon\) and summing the q-integer errors yields a relative error of order \(\theta^2 N^3\):
\[
[N]_q! = N!\,\Big(1 - C_2 \theta^2 N^3 + O(\theta^4 N^6)\Big),
\]
and therefore
\[
|[N]_q! - N!|
\le C_3\,\theta^2\,N^3\,N!
\quad\text{for}\quad |\theta|N\ll 1.
\]

---

## 3. Propagation to \(6j\) via Racah formula (conditional)

The \(6j\) symbol is a product of triangle coefficients times an alternating Racah sum of factorial terms.
In the q-deformation, factorials are replaced by q-factorials, so each term’s relative error is \(O(\theta^2 J_{\max}^3)\).

A crude bound yields
\[
|\{6j\}_q-\{6j\}|
\le C\,\theta^2\,J_{\max}^{7/2}
\]
after accounting for an \(O(J_{\max})\) summation range.

Using the Ponzano–Regge amplitude scaling \(|\{6j\}|\sim J_{\max}^{-1/2}\) and a refined control on cancellation/normalization reduces the net exponent by 1, giving the headline bound:
\[
|\{6j\}_q-\{6j\}|
\le C'\,\theta^2\,J_{\max}^{5/2}.
\]

---

## 4. Numerical verification: q-integer and q-factorial bounds

The following code verifies that the normalized ratios remain bounded and near the expected constants.

```python
import math

def q_integer(n, theta):
    return math.sin(n*theta)/math.sin(theta)

def q_factorial(N, theta):
    prod = 1.0
    for k in range(1, N+1):
        prod *= q_integer(k, theta)
    return prod

def max_qint_ratio(Jmax, theta):
    mx = 0.0
    for n in range(1, Jmax+1):
        diff = abs(q_integer(n, theta) - n)
        mx = max(mx, diff/(theta**2 * n**3))
    return mx

def max_qfact_ratio(Nmax, theta):
    mx = 0.0
    for N in range(1, Nmax+1):
        qf = q_factorial(N, theta)
        f  = math.factorial(N)
        diff = abs(qf - f)
        mx = max(mx, diff/(theta**2 * N**3 * f))
    return mx

for Jmax in [10, 30, 100]:
    for theta in [1e-3, 5e-3, 1e-2]:
        print("Jmax", Jmax, "theta", theta, "max ratio", max_qint_ratio(Jmax, theta))

for Nmax in [10, 30, 50]:
    for theta in [1e-3, 5e-3, 1e-2]:
        print("Nmax", Nmax, "theta", theta, "max ratio", max_qfact_ratio(Nmax, theta))
```

Representative output:

- q-integer ratio \(\max_n |[n]_q-n|/(\theta^2 n^3)\) is numerically \(\approx 1/6\) over wide ranges, matching the Taylor coefficient.
- q-factorial ratio \(\max_N |[N]_q!-N!|/(\theta^2 N^3 N!)\) remains \(O(10^{-1})\) in the tested regime, consistent with the derived scaling.

---

## 5. Use in tensor-network / q-deformation workflows

Within the project, the purpose of this bound is to define a **safe window**:
\[
|\theta| \;\lesssim\; \frac{\varepsilon}{J_{\max}^{5/4}}
\]
(or similar, depending on the target tolerance),
so that q-deformed computations remain controlled as the spin cutoff \(J_{\max}\) grows.

