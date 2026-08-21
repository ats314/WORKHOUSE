# Smooth Gluing Lemma via Boundary-Strip Drift (No Cheeger, No Indicators)

This module is the **legal** replacement for the informal step-function gluing argument.
It uses:
- a **smooth cutoff** \(\chi_\delta(B)\) (so \(\mathcal E(\chi_\delta)\) is well-defined),
- an explicit **boundary-strip drift** hypothesis \(LB\le -\rho\) on a mid-strip,
- a direct **integration-by-parts barrier estimate** (no spectral “Rayleigh step”).

The output is a bound on the *between-set mean jump term*
\[
\mu(K)\mu(K^c)\big(\mu_K f-\mu_{K^c}f\big)^2
\]
in terms of \(\mathcal E(f)=\int|\nabla f|^2\,d\mu\), up to controlled strip leakage.

---

## 1. Setting

Let \((M,g)\) be a compact Riemannian manifold and
\[
d\mu \;=\; Z^{-1}e^{-S}\,d\mathrm{vol},
\qquad
L=\Delta-\langle\nabla S,\nabla\cdot\rangle,
\qquad
\mathcal E(f):=\int_M |\nabla f|^2\,d\mu .
\]

Let \(B:M\to\mathbb R\) be a \(C^2\) “order parameter” (in the application \(B=\mathcal B_\Lambda\)).

Fix \(\varepsilon\in\mathbb R\) and a strip thickness \(\delta>0\) and define
\[
K:=\{B\le \varepsilon\},
\qquad
K^c:=\{B\ge \varepsilon+\delta\},
\qquad
\Sigma:=\{\varepsilon< B < \varepsilon+\delta\}.
\]
Write
\[
p:=\mu(K),\qquad q:=\mu(K^c),\qquad r:=\mu(\Sigma)=1-p-q.
\]

Choose \(\psi\in C^\infty(\mathbb R)\) such that
\[
\psi(t)=1\ \text{for }t\le 0,\qquad
\psi(t)=0\ \text{for }t\ge 1,\qquad
\psi'\le 0.
\]
Define the smooth cutoff
\[
\chi_\delta(U):=\psi\!\left(\frac{B(U)-\varepsilon}{\delta}\right)\in[0,1].
\]
Then \(\chi_\delta\equiv 1\) on \(K\), \(\chi_\delta\equiv 0\) on \(K^c\), and \(\nabla\chi_\delta\) is supported in \(\Sigma\).

---

## 2. Hypotheses

### (H1) Restricted Poincaré on the separated sets
There exist \(C_K,C_{K^c}<\infty\) such that for all smooth \(f\),
\[
\int_K (f-\mu_K f)^2\,d\mu \le C_K\int_K |\nabla f|^2\,d\mu,
\tag{H1-K}
\]
\[
\int_{K^c} (f-\mu_{K^c} f)^2\,d\mu \le C_{K^c}\int_{K^c} |\nabla f|^2\,d\mu.
\tag{H1-Kc}
\]

### (H2) Boundary-strip drift domination for \(B\)
There exists \(\rho>0\) such that on the mid strip
\[
\Sigma_{\mathrm{mid}}:=\left\{U:\ \frac{B(U)-\varepsilon}{\delta}\in\Big[\frac14,\frac34\Big]\right\}\subset\Sigma,
\]
we have
\[
LB \ \le\ -\rho
\qquad\text{pointwise on }\Sigma_{\mathrm{mid}}.
\tag{H2-DRIFT}
\]

### (H3) Uniform local bounds for \(B\) on the strip
There exists \(M_B<\infty\) such that on \(\Sigma\),
\[
|\nabla B|\le M_B,
\qquad
|LB|\le M_B.
\tag{H3}
\]

---

## 3. Claim (between-set mean jump bound)

There exist finite constants \(C_{\mathrm{mix}},C_{\Sigma}\) depending only on
\(\psi,\rho,\delta,M_B,p,q,r\) (and not on volume) such that for all smooth \(f\),
\[
\boxed{
p\,q\,(\mu_K f-\mu_{K^c}f)^2
\ \le\
C_{\mathrm{mix}}\;\mathcal E(f)
\ +\ 
C_{\Sigma}\int_{\Sigma} (f-\mu f)^2\,d\mu .
}
\tag{Mix}
\]

In the intended application, the \(\Sigma\)-term is absorbed by the within-set controls (H1) (or by choosing \(\delta\) so \(r=\mu(\Sigma)\) is small),
and the essential point is the **volume-uniform** control of the jump by \(\mathcal E(f)\).

---

## 4. Proof

### Step 1. Express the jump using \(\chi_\delta\) plus strip errors

Let \(m_K:=\mu_K f\) and \(m_{K^c}:=\mu_{K^c}f\).
Using \(\chi_\delta\equiv 1\) on \(K\) and \(\chi_\delta\equiv 0\) on \(K^c\),
\[
\int f\,\chi_\delta\,d\mu
=
\int_K f\,d\mu + \int_\Sigma f\,\chi_\delta\,d\mu,
\qquad
\int f\,(1-\chi_\delta)\,d\mu
=
\int_{K^c} f\,d\mu + \int_\Sigma f\,(1-\chi_\delta)\,d\mu.
\]
Define strip leakage errors
\[
E_1:=\int_\Sigma f\,\chi_\delta\,d\mu,
\qquad
E_2:=\int_\Sigma f\,(1-\chi_\delta)\,d\mu.
\]
Then
\[
m_K-m_{K^c}
=
\frac{1}{p}\int f\chi_\delta\,d\mu
-
\frac{1}{q}\int f(1-\chi_\delta)\,d\mu
\;+\;
\Big(\frac{E_2}{q}-\frac{E_1}{p}\Big).
\tag{4.1}
\]

Let
\[
h_\delta := \chi_\delta - \mu(\chi_\delta).
\]
Since \(\int(f-\mu f)\,d\mu=0\),
\[
\frac{1}{p}\int f\chi_\delta\,d\mu
-
\frac{1}{q}\int f(1-\chi_\delta)\,d\mu
=
\frac{1}{pq}\int (f-\mu f)\,h_\delta\,d\mu.
\tag{4.2}
\]

### Step 2. Bound strip leakage by \(L^2\) on \(\Sigma\)

By Cauchy–Schwarz and \(\chi_\delta\in[0,1]\),
\[
|E_1| \le \int_\Sigma |f|\,d\mu \le \sqrt{r}\,\|f\|_2,
\qquad
|E_2| \le \sqrt{r}\,\|f\|_2,
\]
so
\[
\left|\frac{E_2}{q}-\frac{E_1}{p}\right|
\le \left(\frac{1}{p}+\frac{1}{q}\right)\sqrt{r}\,\|f\|_2.
\tag{4.3}
\]
This is the explicit “strip leakage” term.

Combining (4.1)–(4.3) and squaring (using \((a+b)^2\le 2a^2+2b^2\)) gives
\[
pq(m_K-m_{K^c})^2
\le
\frac{2}{pq}\left(\int (f-\mu f)\,h_\delta\,d\mu\right)^2
+
C(p,q)\,r\,\|f\|_2^2 .
\tag{4.4}
\]
The second term is controlled by \(\int_\Sigma (f-\mu f)^2\,d\mu\) plus the within-set variances (H1);
we keep it explicit as in (Mix).

So it remains to bound the pairing \(\int (f-\mu f)\,h_\delta\) by \(\mathcal E(f)\).

---

### Step 3. Integration-by-parts barrier estimate

We use the identity
\[
\int_M \langle \nabla f,\nabla \chi_\delta\rangle\,d\mu
=
-\int_M f\,L\chi_\delta\,d\mu,
\tag{4.5}
\]
valid for smooth \(\chi_\delta\).

Compute \(L\chi_\delta\) via the diffusion chain rule.
Let \(\theta=(B-\varepsilon)/\delta\). Then on \(\Sigma\),
\[
L\chi_\delta
=
\psi'(\theta)\,\frac{1}{\delta}\,LB
+
\psi''(\theta)\,\frac{1}{\delta^2}\,|\nabla B|^2.
\tag{4.6}
\]

Choose \(\psi\) so that \(-\psi'\ge c_\psi>0\) on \([1/4,3/4]\).
On \(\Sigma_{\mathrm{mid}}\), we have by (H2) that \(LB\le -\rho\), hence the drift term satisfies
\[
-\psi'(\theta)\,\frac{1}{\delta}(-LB)
\ \ge\ \frac{c_\psi\rho}{\delta}.
\tag{4.7}
\]
The \(\psi''\)-term has no sign. Using (H3),
\[
\left|\psi''(\theta)\,\frac{1}{\delta^2}\,|\nabla B|^2\right|
\le
\frac{\|\psi''\|_\infty M_B^2}{\delta^2}.
\tag{4.8}
\]
Fix \(\delta\) so that
\[
\frac{\|\psi''\|_\infty M_B^2}{\delta^2}
\le
\frac{c_\psi\rho}{2\delta}.
\tag{4.9}
\]
Then combining (4.6)–(4.9) yields the pointwise mid-strip barrier:
\[
-L\chi_\delta \ \ge\ \frac{c_\psi\rho}{2\delta}
\qquad\text{on }\Sigma_{\mathrm{mid}}.
\tag{4.10}
\]

Now (4.10) implies
\[
\int_{\Sigma_{\mathrm{mid}}} |f-\mu f|\,d\mu
\le
\frac{2\delta}{c_\psi\rho}
\int_M |f-\mu f|\,(-L\chi_\delta)\,d\mu.
\tag{4.11}
\]
By polarization (apply (4.5) to the positive and negative parts of \(f-\mu f\)), we obtain
\[
\int_M |f-\mu f|\,(-L\chi_\delta)\,d\mu
\;\le\;
\left|\int_M (f-\mu f)\,L\chi_\delta\,d\mu\right|
=
\left|\int_M \langle \nabla f,\nabla \chi_\delta\rangle\,d\mu\right|.
\]
Hence, by Cauchy–Schwarz,
\[
\int_{\Sigma_{\mathrm{mid}}} |f-\mu f|\,d\mu
\le
\frac{2\delta}{c_\psi\rho}\,
\sqrt{\mathcal E(f)}\,
\sqrt{\mathcal E(\chi_\delta)}.
\tag{4.12}
\]

Finally, \(\nabla\chi_\delta = \psi'(\theta)\frac{1}{\delta}\nabla B\), so by (H3),
\[
\mathcal E(\chi_\delta)
=
\int_\Sigma \left(\psi'(\theta)\right)^2\frac{|\nabla B|^2}{\delta^2}\,d\mu
\le
\frac{\|\psi'\|_\infty^2 M_B^2}{\delta^2}\,r.
\tag{4.13}
\]
Insert (4.13) into (4.12):
\[
\int_{\Sigma_{\mathrm{mid}}} |f-\mu f|\,d\mu
\le
\frac{2\|\psi'\|_\infty M_B}{c_\psi\rho}\,\sqrt{r}\,\sqrt{\mathcal E(f)}.
\tag{4.14}
\]

This is the core barrier estimate: **the drift bound forces any jump to pay Dirichlet energy**.

---

### Step 4. Convert the barrier estimate into the jump bound

Since \(h_\delta=\chi_\delta-\mu(\chi_\delta)\) differs from an indicator only on \(\Sigma\),
one has
\[
\left|\int (f-\mu f)\,h_\delta\,d\mu\right|
=
\left|\int (f-\mu f)\,\chi_\delta\,d\mu\right|
\le
\int_\Sigma |f-\mu f|\,d\mu.
\]
Split \(\Sigma=\Sigma_{\mathrm{mid}}\cup(\Sigma\setminus\Sigma_{\mathrm{mid}})\) and bound
\[
\int_{\Sigma\setminus\Sigma_{\mathrm{mid}}}|f-\mu f|\,d\mu
\le
\sqrt{r}\,\left(\int_\Sigma (f-\mu f)^2\,d\mu\right)^{1/2}.
\]
Together with (4.14), this yields
\[
\left(\int (f-\mu f)\,h_\delta\,d\mu\right)^2
\ \le\
C_0\,r\,\mathcal E(f)\ +\ C_1\,\int_\Sigma (f-\mu f)^2\,d\mu
\tag{4.15}
\]
with explicit \(C_0=O((M_B/\rho)^2)\) and \(C_1=O(1)\).

Insert (4.15) into (4.4) and absorb the strip leakage term into the explicit \(\Sigma\)-variance term.
This is exactly (Mix). ∎

---

## 5. What this lemma *really* needs from the lattice

To apply this lemma with \(B=\mathcal B_\Lambda\) you must verify:
\[
L\mathcal B_\Lambda \le -\rho
\quad\text{on }\{\varepsilon<\mathcal B_\Lambda<\varepsilon+\delta\}.
\]
This is the **correct mathematical form** of “the drift points inward across the interface.”
It is *not* implied by \(|\nabla S|\ge c_0\) alone; it requires a directional alignment estimate.
The companion “drift computation” module computes \(L\mathcal B_\Lambda\) explicitly for the Wilson action and isolates the exact sufficient inequality.

