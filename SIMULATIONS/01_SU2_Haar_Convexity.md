# SU(2) Haar Convexity in Exponential Coordinates

This note isolates (and checks) a key “engine” in this repository’s mass-gap program: **the Haar measure induces a strictly convex effective potential in exponential (Lie algebra) coordinates**. In Bakry–Émery language, this contributes a uniform positive curvature term to the Hessian of the lattice action.

The original project script that motivated this note is `analysis_haar_bound.py` (JAX-based). fileciteturn2file1  
Because `jaxlib` is not available in this execution environment, I reproduce the *analytic derivation* and verify it numerically with NumPy/SciPy.

---

## 1. Setup and conventions

Any element of \(SU(2)\) can be written as
\[
U(\theta,\mathbf{n})=\cos\theta\,\mathbf{1} + i\sin\theta\,(\mathbf{n}\cdot \boldsymbol{\sigma}),
\qquad \theta\in[0,\pi),\ \mathbf{n}\in S^2.
\]

A common exponential-coordinate map uses Lie algebra variables \(a\in\mathbb{R}^3\) with
\[
U(a) = \exp\!\left( i\,\frac{a\cdot \boldsymbol{\sigma}}{2}\right),
\qquad \theta = \frac{\|a\|}{2}.
\]

In these coordinates, Haar measure has Jacobian density
\[
J(a)\propto \left(\frac{\sin \theta}{\theta}\right)^2,
\qquad \theta=\frac{\|a\|}{2}.
\]
Thus the “Haar action” (negative log-density up to an additive constant) is
\[
S_H(a)
= -\log J(a)
= -2\log\!\left(\frac{\sin\theta}{\theta}\right).
\]

---

## 2. Radial Hessian eigenvalues

Let \(f(a)=\phi(\|a\|)\) be radial on \(\mathbb{R}^3\). Then (for \(\rho=\|a\|>0\))
\[
\nabla^2 f(a)
=
\phi''(\rho)\,\frac{a a^\top}{\rho^2}
+
\frac{\phi'(\rho)}{\rho}\left(I-\frac{a a^\top}{\rho^2}\right).
\]
So the Hessian has:
- one **radial** eigenvalue \(\lambda_{\mathrm{rad}}=\phi''(\rho)\),
- two equal **tangential** eigenvalues \(\lambda_{\mathrm{tan}}=\phi'(\rho)/\rho\).

For the Haar action \(S_H(a)=\Phi(\rho)\) with \(\theta=\rho/2\) and
\[
\Phi(\rho) = -2\log\left(\frac{\sin(\rho/2)}{\rho/2}\right),
\]
a straightforward chain-rule computation yields the eigenvalues as functions of \(\theta\):

\[
\boxed{
\lambda_{\mathrm{rad}}(\theta)
=
\frac{1}{2}\left(\csc^2\theta - \frac{1}{\theta^2}\right)
}
\]
\[
\boxed{
\lambda_{\mathrm{tan}}(\theta)
=
\frac{1 - \theta\cot\theta}{2\theta^2}
}
\qquad (\theta\in(0,\pi)).
\]

These match the formulas hard-coded in the original JAX analysis. fileciteturn2file1

---

## 3. The global lower bound (the “Haar mass”)

### Proposition (global uniform convexity for \(SU(2)\) Haar action)
For all \(\theta\in(0,\pi)\),
\[
\lambda_{\mathrm{rad}}(\theta)\ge \frac{1}{6},\qquad
\lambda_{\mathrm{tan}}(\theta)\ge \frac{1}{6}.
\]
Equivalently,
\[
\nabla^2 S_H(a)\ \succeq\ \frac{1}{6}\,I_3
\quad\text{for all } a \text{ with } \|a\|\in(0,2\pi).
\]

### Proof sketch
Both eigenvalues have convergent series at \(\theta=0\):
\[
\lambda_{\mathrm{rad}}(\theta)=\frac{1}{6}+\frac{\theta^2}{30}+\frac{\theta^4}{189}+\cdots,
\qquad
\lambda_{\mathrm{tan}}(\theta)=\frac{1}{6}+\frac{\theta^2}{90}+\frac{\theta^4}{945}+\cdots.
\]
So \(\lim_{\theta\to 0}\lambda_{\mathrm{rad}}(\theta)=\lim_{\theta\to 0}\lambda_{\mathrm{tan}}(\theta)=1/6\) and both increase to \(+\infty\) as \(\theta\to\pi^{-}\) (because \(\sin\theta\to 0\)). One can show (by differentiating) that both eigenvalue functions are monotone increasing on \((0,\pi)\), hence their global minimum is attained at \(\theta=0\) and equals \(1/6\).

A numerically stable verification is given next.

---

## 4. Numerical verification (NumPy)

The following snippet evaluates the eigenvalues on a dense grid in \((0,\pi)\), using
series expansions for \(\theta<10^{-3}\) to avoid catastrophic cancellation:

```python
import numpy as np, math

def lam_haar_rad(theta):
    theta = np.asarray(theta)
    out = np.empty_like(theta, dtype=float)
    small = theta < 1e-3
    t = theta[small]
    out[small] = (1/6 + t**2/30 + t**4/189)  # series
    u = theta[~small]
    out[~small] = 0.5*(1/np.sin(u)**2 - 1/u**2)
    return out

def lam_haar_tan(theta):
    theta = np.asarray(theta)
    out = np.empty_like(theta, dtype=float)
    small = theta < 1e-3
    t = theta[small]
    out[small] = (1/6 + t**2/90 + t**4/945)  # series
    u = theta[~small]
    out[~small] = (1 - u/np.tan(u))/(2*u**2)
    return out

thetas = np.linspace(1e-8, math.pi-1e-8, 500_000)
print(lam_haar_rad(thetas).min(), lam_haar_tan(thetas).min())
```

Result (in this environment):
\[
\min \lambda_{\mathrm{rad}} = \min \lambda_{\mathrm{tan}} = \frac{1}{6}.
\]

---

## 5. Why this matters for the mass-gap program

In Bakry–Émery form, if a Gibbs measure has potential \(V\) with
\[
\nabla^2 V \succeq \kappa I,
\]
then one gets uniform Poincaré/log-Sobolev inequalities with constants depending on \(\kappa\). The Haar lower bound above provides a **volume-independent positive curvature floor** in exponential coordinates.

The interesting fight is whether the **Wilson interaction** can be shown not to destroy this convexity *in the regime relevant to the continuum limit*, or whether one can compensate loss of convexity by concentration-of-measure and defect-gas arguments (see the other notes in this output set).

---

## 6. Open directions suggested by this lemma

1. **Extend to \(SU(N)\)**: find an explicit constant \(c_0(N)\) with \(\nabla^2 S_H \succeq c_0(N) I\) in a useful coordinate chart (and track how it scales with \(N\)).  
2. **Gauge fixing and fundamental modular region**: since the exponential chart is not global and gauge orbits can push links near the cut locus, a rigorous approach likely needs a gauge-fixed representative to keep most links in the convex chart.  
3. **Integrate with RG**: the proof plan in this repo argues that convexity may re-emerge after block-spin/RG steps even if it fails microscopically.

