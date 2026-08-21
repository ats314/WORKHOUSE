# Viscous Hamilton–Jacobi flow, Hessian evolution, and a Riccati lower bound

## The conceptual move

Turn an RG-like smoothing step into a PDE for an *effective action* \(S_t\).  
Then track the smallest eigenvalue of \(\nabla^2 S_t\) through time via a Riccati inequality.

This is exciting because it tries to make “mass gap persistence under coarse-graining” into a one-dimensional dynamical inequality.

---

## 1. Deriving the viscous Hamilton–Jacobi equation

Let \(\rho_t\) be a smooth positive density solving the heat equation
\[
\partial_t \rho_t = \Delta \rho_t.
\]

Write \(\rho_t\) in Gibbs form:
\[
\rho_t(x)=Z_t^{-1}e^{-S_t(x)}.
\]

Compute derivatives:
\[
\partial_t\rho_t = \rho_t\bigl(-\partial_t S_t - \partial_t\log Z_t\bigr),
\]
and
\[
\Delta\rho_t = \Delta\!\bigl(e^{-S_t}\bigr)Z_t^{-1}
=\rho_t\bigl(-\Delta S_t + |\nabla S_t|^2\bigr).
\]

Equating \(\partial_t \rho_t=\Delta\rho_t\) yields
\[
-\partial_t S_t - \partial_t\log Z_t = -\Delta S_t + |\nabla S_t|^2.
\]

Absorb the purely time-dependent term into the normalization by defining
\(\widetilde S_t := S_t + \log Z_t\). Then
\[
\boxed{\;\partial_t \widetilde S_t = \Delta \widetilde S_t - |\nabla \widetilde S_t|^2.\;}
\]
Dropping tildes (standard abuse), this is the **viscous Hamilton–Jacobi (vHJ)** equation:
\[
\partial_t S_t = \Delta S_t - |\nabla S_t|^2.
\]

---

## 2. Evolution of gradient and Hessian

Define
\[
b_t:=\nabla S_t,\qquad h_t:=\nabla^2 S_t.
\]

Differentiate the vHJ equation:

### Gradient evolution
Using commutation of \(\nabla\) and \(\Delta\) in flat coordinates (or in a normal chart),
\[
\partial_t b_t = \Delta b_t - 2(\nabla S_t\cdot\nabla)b_t.
\]

### Hessian evolution
Differentiate again:
\[
\boxed{\;\partial_t h_t
=\Delta h_t -2(\nabla S_t\cdot\nabla)h_t -2\,h_t^2.\;}
\]

The nonlinear term \(-2h_t^2\) is the star: it forces a Riccati-type behavior for eigenvalues.

---

## 3. Eigenvalue inequality and Riccati ODE at the spatial minimum

Let \(\lambda(t,x)\) be a simple eigenvalue of \(h_t(x)\) with unit eigenvector \(v\).  
Standard perturbation theory yields an inequality of the form
\[
\partial_t \lambda \;\ge\;
\Delta\lambda -2(\nabla S_t\cdot\nabla)\lambda -2\lambda^2
\quad(+\text{geometric/curvature terms on manifolds}).
\]

Now suppose \(x_t\) is a point where \(\lambda(t,\cdot)\) attains its spatial minimum, and define
\[
\ell(t):=\min_x \lambda(t,x)=\lambda(t,x_t).
\]

At such a minimum, \(\nabla\lambda=0\) and \(\Delta\lambda\ge 0\).  
One gets a **scalar Riccati inequality**
\[
\boxed{\;\dot\ell(t)\;\ge\; -2\ell(t)^2 + \sigma(t).\;}
\]

Here \(\sigma(t)\) packages the *positive* contributions you can guarantee:
- background Ricci curvature,
- a fixed positive Haar contribution at finite cutoff,
- and whatever “anomaly source” survives the RG step.

---

## 4. What the Riccati inequality buys you

If \(\sigma(t)\ge \sigma_*>0\) uniformly and \(\ell(0)>0\), then compare \(\ell\) with the solution of
\[
\dot y = -2y^2 + \sigma_*.
\]

This ODE has a stable positive fixed point
\[
y_*=\sqrt{\sigma_*/2}.
\]

So the comparison principle gives:
- \(\ell(t)\) stays positive for all \(t\),
- and \(\ell(t)\to y_*\) as \(t\to\infty\).

Interpretation: the flow *preserves* strict convexity and pushes it toward a universal scale.

---

## 5. Where it becomes a “mass gap persistence” mechanism

At finite lattice cutoff, the Haar Jacobian gives an explicit \(\sigma_*\) contribution.  
But in an asymptotically free continuum limit, that contribution vanishes. The project’s idea (as I read it) is:

1. Use the Riccati inequality as an organizing equation.
2. Identify an “anomaly source” or effective positive term in \(\sigma(t)\) that does **not** vanish with \(a\).
3. Control error terms \(\varepsilon_j\) across RG steps (summability is the key).
4. Conclude that the fixed point of the recursion remains positive, giving a persistent physical mass scale.

That’s not a complete proof of the Clay problem (obviously), but it is a sharp *mathematical lens* for attacking the right failure mode: “convexifier disappears as \(a\to 0\).”