# One-link Wilson + Haar Convexity: the critical β and the non-convex annulus

This note turns the qualitative “Haar helps convexity” slogan into a quantitative toy model:

- **one SU(2) degree of freedom**, in exponential coordinates,
- with **Haar action** + **Wilson weight** \(\propto e^{\beta \cos\theta}\),
- and an explicit Hessian analysis showing where convexity fails.

The repository’s original (JAX-based) exploration of this is in `analysis_beta_c.py`. fileciteturn2file9  
The derivations below reproduce the same structure without JAX.

---

## 1. The toy model

Let \(\theta\in[0,\pi)\) parameterize \(SU(2)\) as
\[
U(\theta,\mathbf n)=\cos\theta\,I + i\sin\theta\,(\mathbf n\cdot\sigma).
\]
In Lie algebra coordinates \(a\in\mathbb R^3\) with \(\theta=\|a\|/2\), define the total action
\[
S_\beta(a) = S_H(a) + S_W(a),
\]
where
\[
S_H(a) = -2\log\left(\frac{\sin\theta}{\theta}\right),
\qquad
S_W(a) = -\beta\cos\theta.
\]

This is exactly the scalar “one-link” effective potential behind the concentration calculations elsewhere in the repo. fileciteturn2file3

---

## 2. Hessian eigenvalues

Because \(S_\beta(a)\) is radial, its Hessian splits into radial vs tangential eigenvalues (one radial, two tangential).

Write \(\lambda^{H}_{\rm rad},\lambda^{H}_{\rm tan}\) for the Haar contributions from the previous note, and \(\lambda^{W}_{\rm rad},\lambda^{W}_{\rm tan}\) for Wilson.

### Haar part
\[
\lambda^{H}_{\mathrm{rad}}(\theta)=\frac{1}{2}\left(\csc^2\theta-\frac{1}{\theta^2}\right),
\qquad
\lambda^{H}_{\mathrm{tan}}(\theta)=\frac{1-\theta\cot\theta}{2\theta^2}.
\]

### Wilson part
Since \(S_W(a)=-\beta\cos\theta\) with \(\theta=\|a\|/2\), one finds
\[
\lambda^{W}_{\mathrm{rad}}(\theta)=\frac{\beta}{4}\cos\theta,
\qquad
\lambda^{W}_{\mathrm{tan}}(\theta)=\frac{\beta}{4}\frac{\sin\theta}{\theta}.
\]

### Total
\[
\lambda_{\mathrm{rad}}(\theta)=\lambda^{H}_{\mathrm{rad}}(\theta)+\lambda^{W}_{\mathrm{rad}}(\theta),
\qquad
\lambda_{\mathrm{tan}}(\theta)=\lambda^{H}_{\mathrm{tan}}(\theta)+\lambda^{W}_{\mathrm{tan}}(\theta).
\]

Observation: \(\lambda_{\mathrm{tan}}(\theta)\) stays **positive** for all \(\beta\ge 0\), since both terms are positive on \((0,\pi)\).  
So any convexity failure is driven by the **radial eigenvalue**.

---

## 3. The convexity threshold β\_c

Convexity fails precisely when
\[
\min_{\theta\in(0,\pi)} \lambda_{\rm rad}(\theta) < 0.
\]

The threshold \(\beta_c\) occurs when the minimum touches zero:
\[
\exists\,\theta_\star\in(\pi/2,\pi):\quad \lambda_{\rm rad}(\theta_\star)=0,
\quad
\lambda_{\rm rad}'(\theta_\star)=0.
\]

Equivalently, for each \(\theta\in(\pi/2,\pi)\) (where \(\cos\theta<0\)) the value of \(\beta\) that makes \(\lambda_{\rm rad}(\theta)=0\) is
\[
\beta(\theta)
= -2\,\frac{\csc^2\theta-\theta^{-2}}{\cos\theta}.
\]
Then
\[
\boxed{\ \beta_c = \min_{\theta\in(\pi/2,\pi)} \beta(\theta)\ }.
\]

### Numerical value (this environment)
\[
\boxed{
\beta_c \approx 4.413914663162,
\qquad
\theta_\star \approx 2.118504915119.
}
\]

So this toy model predicts:
- for \(\beta<\beta_c\): **global convexity** (Bakry–Émery curvature stays positive everywhere in the chart),
- for \(\beta>\beta_c\): convexity fails on an intermediate annulus of angles.

This matches the qualitative conclusion in `analysis_beta_c.py`. fileciteturn2file9

---

## 4. The non-convex annulus \([\theta_-(\beta),\theta_+(\beta)]\)

For \(\beta>\beta_c\), the equation \(\lambda_{\rm rad}(\theta)=0\) has **two** solutions,
\[
\theta_-(\beta) < \theta_+(\beta),
\]
and the radial Hessian is negative for \(\theta\in(\theta_-,\theta_+)\).

A few representative values:

| beta | r_start | r_end |
|---|---|---|
| 4.500000 | 2.038649 | 2.201505 |
| 5.000000 | 1.924823 | 2.332324 |
| 6.000000 | 1.831386 | 2.454436 |
| 8.000000 | 1.747900 | 2.581050 |
| 10.000000 | 1.706223 | 2.654222 |
| 20.000000 | 1.633771 | 2.812795 |
| 50.000000 | 1.595101 | 2.938592 |

*(Angles are in radians; \(\pi/2\approx 1.5708\), \(\pi\approx 3.1416\).)*

Trend:
- as \(\beta\to\infty\), \(\theta_-(\beta)\downarrow \pi/2\) and \(\theta_+(\beta)\uparrow \pi\).

So the “bad” region expands, but it also moves into zones where the Gibbs weight is exponentially suppressed (see the concentration note).

---

## 5. Why this is interesting (and not just calculus)

The project’s intended strategy is not “global convexity holds for all β” (it does not), but rather:

1. **Use global convexity** at least in some regime or at some coarse-grained scale to get uniform functional inequalities.
2. **Control the convexity failure** for large \(\beta\) by showing the non-convex set has tiny probability (defect gas / rare-event control).
3. Bootstrap to **spectral gap** and then **mass gap**.

This toy model quantifies Step (2): it tells you exactly where convexity fails and how to define a “defect” set.
