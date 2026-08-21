# Quantitative physical curvature floor on a certified good set
\[
\textbf{(Doc 01Q: fully quantitative)}
\]

## 0. What this file is doing

We package the “Part 5 matrix hinge / Hessian perturbation” idea into a **numerically checkable** good set
\(K_\Lambda^\star\) on which the **horizontal (gauge–projected) Bakry–Émery curvature** has a uniform spectral floor.

This is the exact input you want for:
- contractive block Gibbs / Dobrushin (Doc 02Q),
- strip-kernel spectral gap (Doc 03 interface),
- and then OS gap-to-mass translation.

---

## 1. Geometry, gauge directions, and the horizontal projector

Work on the cochain model at the vacuum \(U^{(0)}\).

- Vertical (gauge) directions:
\[
V_{U^{(0)}} := \operatorname{im}(d_0)\subset \mathcal C^1(\Lambda;\mathfrak g).
\]
- Horizontal space:
\[
H^{(0)} := \ker(d_0^\*)=(\operatorname{im} d_0)^\perp.
\]
Let \(\Pi_H := P_{H^{(0)}}\) be the \(\ell^2\)-orthogonal projection onto \(H^{(0)}\).

> Note: this choice matches the project’s own convention “physical = horizontal, gauge = vertical at the vacuum.”

---

## 2. Constants (all explicit)

### 2.1 Small-field radius
Let \(r_{\mathrm{sf}}\) be the project-wide small-field cutoff.

### 2.2 Hessian perturbation size
For \(0<r\le r_{\mathrm{sf}}\), define the perturbation constant
\[
R_W(r):=\Big(\frac{\beta}{n}\Big)\,(2\nu\,M_3(r_\star))\,r.
\]
This is the “uniform Hessian perturbation size” intended to control how much \(\nabla^2 S_W\) can drift from its vacuum Hessian on \(K_\Lambda(r)\).

### 2.3 Ricci / mass and Maxwell operator
Let \(c_H\ge 0\) be the product-manifold Ricci lower bound and define
\[
m^2 := \frac{c_H}{2}.
\]
Let
\[
\alpha := \frac{\beta}{n\lambda_\rho},\qquad \mathsf M_1:=d_1^\*d_1.
\]
(So \(\alpha\mathsf M_1\) is the vacuum Wilson Hessian, modulo gauge.)

---

## 3. The certified good set \(K_\Lambda^\star\)

### 3.1 Linkwise small field
\[
K_\Lambda(r):=\{U\in M_\Lambda:\ \max_{b\in E(\Lambda)} d_G(U_b,\mathbf 1)<r\}.
\]

### 3.2 Choose a hinge radius with explicit slack
Fix a slack parameter \(\theta\in(0,1)\) (e.g. \(\theta=\tfrac12\)).
Define
\[
r_{\mathrm{hinge}}(\theta)
:=\min\!\left(r_{\mathrm{sf}},\ \frac{\theta\,n\,m^2}{2\beta\,\nu\,M_3(r_\star)}\right).
\]
Then for all \(r\le r_{\mathrm{hinge}}(\theta)\), we have
\[
R_W(r)\le \theta\,m^2.
\]

### 3.3 Good set
\[
K_\Lambda^\star := K_\Lambda\big(r_{\mathrm{hinge}}(\theta)\big).
\]

---

## 4. The quantitative hinge inequality (the only “Part 5” input)

We state this in a way that is both usable and checkable.

> **(Hinge assumption / Part 5 matrix hinge).**
> For all \(U\in K_\Lambda^\star\),
> \[
> \big\|\Pi_H\big(\nabla^2 S_W(U)-\nabla^2 S_W(U^{(0)})\big)\Pi_H\big\|_{\mathrm{op}}
> \ \le\ R_W(r_{\mathrm{hinge}}(\theta)).
> \tag{H}
> \]

At the vacuum,
\[
\nabla^2 S_W(U^{(0)})=\alpha\,d_1^\*d_1=\alpha\,\mathsf M_1.
\]

---

## 5. Physical curvature operator and spectral floor

Define the **horizontal Bakry–Émery curvature operator** (the one that matters for local log-concavity)
\[
\mathcal K_H(U)
:=\Pi_H\Big(m^2 I + \nabla^2 S_W(U)\Big)\Pi_H
\quad\text{as an operator on }H^{(0)}.
\]

### Lemma 5.1 (quantitative horizontal spectral floor on \(K_\Lambda^\star\))
Assume (H). Then for all \(U\in K_\Lambda^\star\),
\[
\lambda_{\min}\big(\mathcal K_H(U)\big)\ \ge\ (1-\theta)\,m^2.
\]

#### Proof
By (H),
\[
\Pi_H\nabla^2S_W(U)\Pi_H
\succeq
\Pi_H\nabla^2S_W(U^{(0)})\Pi_H - R_W(r_{\mathrm{hinge}}(\theta))\,I.
\]
Since \(\Pi_H\nabla^2S_W(U^{(0)})\Pi_H=\alpha\,\Pi_H\mathsf M_1\Pi_H\succeq 0\),
\[
\Pi_H\nabla^2S_W(U)\Pi_H \succeq -R_W(r_{\mathrm{hinge}}(\theta))\,I.
\]
Add \(m^2 I\) and use \(R_W(r_{\mathrm{hinge}}(\theta))\le \theta m^2\):
\[
\mathcal K_H(U)\succeq (m^2-\theta m^2)I = (1-\theta)m^2\,I.
\]
∎

---

## 6. What this buys you immediately

On \(K_\Lambda^\star\), every conditional block law (in the horizontal coordinates) is at least
\(\kappa_\star\)-strongly log-concave with
\[
\kappa_\star := (1-\theta)m^2,
\]
uniform in \(|\Lambda|\).

That is exactly the “local convexity” input for the block-Gibbs/Dobrushin theorem in Doc 02Q.

---

## 7. Next required lemma (still missing, but now sharply posed)

To make (H) a theorem rather than an assumption, you need the *Part 5* estimate that upgrades the **definition**
of \(R_W(r)\) into the **operator inequality** (H). The constant ledger already tells you what the bound
*should* look like; the remaining work is to write the combinatorial Hessian comparison cleanly.
