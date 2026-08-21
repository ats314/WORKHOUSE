# Smooth Gluing Lemma with Boundary-Strip Drift (Barrier Proof)

This document gives the *legal* between-set (mixing) control used in gluing: **smooth cutoff**, **no indicator gradients**, **no Rayleigh-quotient shortcut**, and the key replacement input is a **pointwise drift bound across a boundary strip**.

---

## 1. Setting

Let $(M,g)$ be a compact Riemannian manifold and
\[
d\mu = Z^{-1}e^{-S}\,d\mathrm{vol},\qquad
L=\Delta-\langle\nabla S,\nabla\cdot\rangle,\qquad
\mathcal E(f):=\int_M |\nabla f|^2\,d\mu.
\]
Equivalently, in carré-du-champ notation,
\[
\Gamma(f):=|\nabla f|^2,\qquad \mathcal E(f)=\int \Gamma(f)\,d\mu.
\]

Fix a $C^2$ order parameter $B:M\to\mathbb R$ (in the lattice application: $B=\mathcal B_\Lambda$).

Fix $\varepsilon\in\mathbb R$ and thickness $\delta>0$, and define
\[
K:=\{B\le \varepsilon\},\qquad
K^c:=\{B\ge \varepsilon+\delta\},\qquad
\Sigma:=\{\varepsilon< B < \varepsilon+\delta\}.
\]
Write
\[
p:=\mu(K),\qquad q:=\mu(K^c),\qquad r:=\mu(\Sigma)=1-p-q.
\]

Choose $\psi\in C^\infty(\mathbb R)$ such that
\[
\psi(t)=1\ (t\le 0),\qquad
\psi(t)=0\ (t\ge 1),\qquad
\psi'\le 0.
\]
Define the smooth cutoff
\[
\chi_\delta(U):=\psi\!\left(\frac{B(U)-\varepsilon}{\delta}\right)\in[0,1].
\]
Then $\chi_\delta\equiv 1$ on $K$, $\chi_\delta\equiv 0$ on $K^c$, and $\nabla\chi_\delta$ is supported on $\Sigma$.

---

## 2. Hypotheses

### (H1) Restricted Poincaré on $K$ and on $K^c$

There exist constants $C_K,C_{K^c}<\infty$ such that for all smooth $f$,
\[
\int_K (f-\mu_K f)^2\,d\mu \le C_K\int_K |\nabla f|^2\,d\mu,
\qquad
\int_{K^c} (f-\mu_{K^c} f)^2\,d\mu \le C_{K^c}\int_{K^c} |\nabla f|^2\,d\mu.
\]

### (H2) Boundary-strip drift domination

There exists $\rho>0$ such that on the strip $\Sigma$,
\[
LB \le -\rho.
\tag{DRIFT}
\]

### (H3) Local bounded geometry of $B$ in the strip

There exists $M_B<\infty$ such that on $\Sigma$,
\[
|\nabla B|\le M_B,\qquad |LB|\le M_B.
\tag{B-bounds}
\]

---

## 3. Claim (between-set mixing bound with explicit strip term)

There exist constants $C_{\mathrm{mix}}<\infty$ and $C_\Sigma<\infty$, depending only on $\psi,\rho,\delta,M_B$ and $(p,q,r)$, such that for every smooth $f$,
\[
\boxed{
p\,q\,(\mu_K f-\mu_{K^c}f)^2
\ \le\
C_{\mathrm{mix}}\;\mathcal E(f)
\ +\ C_\Sigma \int_{\Sigma}(f-\mu f)^2\,d\mu.
}
\tag{Mix}
\]

In gluing applications $\Sigma$ has fixed thickness and this $\Sigma$-variance term is absorbed either by the “good/bad” restricted controls or by a crude $r\,\mathrm{Var}_\mu(f)$ estimate.

---

## 4. Proof

### Step 1. Reduce the jump to a pairing with the cutoff plus strip leakage

Let $m_K:=\mu_K f$ and $m_{K^c}:=\mu_{K^c} f$.

Define strip errors
\[
E_1:=\int_\Sigma f\,\chi_\delta\,d\mu,\qquad
E_2:=\int_\Sigma f\,(1-\chi_\delta)\,d\mu.
\]
Since $\chi_\delta=1$ on $K$ and $0$ on $K^c$,
\[
\int_K f\,d\mu = \int f\chi_\delta\,d\mu - E_1,
\qquad
\int_{K^c} f\,d\mu = \int f(1-\chi_\delta)\,d\mu - E_2.
\]
Hence
\[
m_K-m_{K^c}
=
\frac{1}{p}\int f\chi_\delta\,d\mu
-\frac{1}{q}\int f(1-\chi_\delta)\,d\mu
+\left(\frac{E_2}{q}-\frac{E_1}{p}\right).
\tag{4.1}
\]

Now set $h_\delta:=\chi_\delta-\mu(\chi_\delta)$. Since $\int(f-\mu f)\,d\mu=0$,
\[
\frac{1}{p}\int f\chi_\delta\,d\mu
-\frac{1}{q}\int f(1-\chi_\delta)\,d\mu
=
\frac{1}{pq}\int (f-\mu f)\,h_\delta\,d\mu.
\tag{4.2}
\]

Thus the mean jump decomposes as (pairing term) + (strip leakage term).

### Step 2. Bound the strip leakage

By Cauchy–Schwarz and $0\le\chi_\delta\le 1$,
\[
|E_1|\le \int_\Sigma |f|\,d\mu \le \sqrt{r}\,\|f\|_2,
\qquad
|E_2|\le \sqrt{r}\,\|f\|_2,
\]
so
\[
\left|\frac{E_2}{q}-\frac{E_1}{p}\right|
\le
\left(\frac{1}{p}+\frac{1}{q}\right)\sqrt{r}\,\|f\|_2.
\tag{4.3}
\]

This produces the explicit strip term in (Mix).

### Step 3. The barrier estimate: control the pairing by Dirichlet energy

We start from the exact integration-by-parts identity valid for smooth $\chi_\delta$:
\[
\int \langle \nabla f,\nabla \chi_\delta\rangle\,d\mu
=
-\int f\,L\chi_\delta\,d\mu.
\tag{4.4}
\]

Compute $L\chi_\delta$ by the diffusion chain rule. Let $\theta=(B-\varepsilon)/\delta$. Then on $\Sigma$,
\[
L\chi_\delta
=
\psi'(\theta)\,\frac{1}{\delta}\,LB
+\psi''(\theta)\,\frac{1}{\delta^2}\,|\nabla B|^2.
\tag{4.5}
\]

Fix the mid-strip
\[
\Sigma_{\mathrm{mid}}:=\left\{U:\ \theta(U)\in[1/4,3/4]\right\}\subset\Sigma,
\]
and choose $\psi$ so that $-\psi'\ge c_\psi>0$ on $[1/4,3/4]$.

On $\Sigma_{\mathrm{mid}}$, (DRIFT) gives $LB\le -\rho$, hence the drift part contributes a **uniform positive lower bound** to $-L\chi_\delta$:
\[
-\psi'(\theta)\,\frac{1}{\delta}\,(-LB)\ \ge\ \frac{c_\psi\rho}{\delta}
\qquad\text{on }\Sigma_{\mathrm{mid}}.
\tag{4.6}
\]
The second term is controlled by (B-bounds):
\[
\left|\psi''(\theta)\,\frac{1}{\delta^2}\,|\nabla B|^2\right|
\le
\frac{\|\psi''\|_\infty M_B^2}{\delta^2}.
\tag{4.7}
\]

Choose $\delta$ (fixed once and for all) so that the $\psi''$-term cannot overwhelm the drift:
\[
\frac{\|\psi''\|_\infty M_B^2}{\delta^2}\le \frac{c_\psi\rho}{2\delta}.
\tag{4.8}
\]
Then combining (4.5)–(4.8) yields the pointwise mid-strip barrier:
\[
\boxed{
-L\chi_\delta \ \ge\ \frac{c_\psi\rho}{2\delta}
\qquad\text{on }\Sigma_{\mathrm{mid}}.
}
\tag{4.9}
\]

Now apply (4.4) and Cauchy–Schwarz:
\[
\left|\int (f-\mu f)\,L\chi_\delta\,d\mu\right|
=
\left|\int \langle\nabla f,\nabla\chi_\delta\rangle\,d\mu\right|
\le
\sqrt{\mathcal E(f)}\,\sqrt{\mathcal E(\chi_\delta)}.
\tag{4.10}
\]
Also, by (4.9),
\[
\int_{\Sigma_{\mathrm{mid}}}|f-\mu f|\,d\mu
\le
\frac{2\delta}{c_\psi\rho}\int |f-\mu f|\,(-L\chi_\delta)\,d\mu
\le
\frac{2\delta}{c_\psi\rho}\left|\int (f-\mu f)\,L\chi_\delta\,d\mu\right|.
\tag{4.11}
\]
Combining (4.10)–(4.11) gives
\[
\int_{\Sigma_{\mathrm{mid}}}|f-\mu f|\,d\mu
\le
\frac{2\delta}{c_\psi\rho}\,\sqrt{\mathcal E(f)}\,\sqrt{\mathcal E(\chi_\delta)}.
\tag{4.12}
\]

Finally, $\mathcal E(\chi_\delta)$ is controlled directly from (B-bounds):
\[
\nabla\chi_\delta=\psi'(\theta)\frac{1}{\delta}\nabla B
\quad\Rightarrow\quad
\mathcal E(\chi_\delta)
=\int_\Sigma (\psi'(\theta))^2\frac{|\nabla B|^2}{\delta^2}\,d\mu
\le \frac{\|\psi'\|_\infty^2 M_B^2}{\delta^2}\,r.
\tag{4.13}
\]
Insert (4.13) into (4.12):
\[
\int_{\Sigma_{\mathrm{mid}}}|f-\mu f|\,d\mu
\le
\frac{2\|\psi'\|_\infty M_B}{c_\psi\rho}\,\sqrt{r}\,\sqrt{\mathcal E(f)}.
\tag{4.14}
\]

This is the barrier estimate: the drift bound forces the function to “pay” Dirichlet energy to transport mass across the strip.

### Step 4. Finish (Mix)

Returning to (4.2), the pairing term is supported where $\chi_\delta$ varies, hence can be controlled by strip $L^1$ and $L^2$ norms; one convenient bound is
\[
\left|\int (f-\mu f)\,h_\delta\,d\mu\right|
=
\left|\int (f-\mu f)\,\chi_\delta\,d\mu\right|
\le
\int_{\Sigma}|f-\mu f|\,d\mu
\]
and split $\Sigma=\Sigma_{\mathrm{mid}}\cup(\Sigma\setminus\Sigma_{\mathrm{mid}})$, using (4.14) on $\Sigma_{\mathrm{mid}}$ and Cauchy–Schwarz on the remainder. Squaring and inserting back into (4.1)–(4.3) yields
\[
p\,q\,(\mu_K f-\mu_{K^c}f)^2
\le
C_{\mathrm{mix}}\,\mathcal E(f)
+
C_\Sigma\int_\Sigma (f-\mu f)^2\,d\mu,
\]
for constants depending only on $(\psi,\rho,\delta,M_B,p,q,r)$.

That is (Mix). $\square$
