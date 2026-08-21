# Drift + Riccati convexification under PBH-type RG flows

## Overview

Two "nonperturbative convexity tools" recur across the project files:

1. **Lyapunov drift:** a global mechanism to control the large-field region even when uniform convexity holds only locally.
2. **Riccati convexification:** a matrix differential inequality showing that certain coarse-graining / Polchinski–Brydges–Houghton (PBH) type flows *restore* (or at least preserve) uniform convexity of the effective action.

Both are standard ideas in isolation, but the **combination** is unusual in the Yang--Mills context: it suggests an RG-stable pipeline

\[
\text{local SAFE convexity} \quad\Rightarrow\quad
\text{global functional inequalities} \quad\Rightarrow\quad
\text{scale-stable convexity under RG}.
\]

This note extracts the cleanest, reusable statements.

---

## 1. Lyapunov drift: globalization template

Let $(M,g)$ be a complete Riemannian manifold and let
\[
d\mu = Z^{-1} e^{-S}\, d{\rm vol}_g
\]
with generator (Langevin diffusion)
\[
L f = \Delta_g f - \langle \nabla S, \nabla f\rangle.
\]

A **Lyapunov function** is a smooth $W:M\to[1,\infty)$ such that there exist constants $\alpha>0$, $\beta\ge0$ and a "small set" $\Omega\subset M$ with
\[
\boxed{
L W \;\le\; -\alpha W + \beta\,{\bf 1}_{\Omega}.
}
\]

Interpretation: outside $\Omega$, the drift $-\nabla S$ forces rapid return, preventing escape to infinity.

### Yang--Mills specialization

In the YM files, one uses a gauge-invariant Lyapunov candidate of the form
\[
W_\Lambda(U) = 1 + \sum_{p\in P(\Lambda)} \Phi(U_p)
\]
for a smooth class-function-like $\Phi$ that is convex near the identity and grows with plaquette angle / field strength.

The key mechanism is that for large fields, the drift term dominates:
\[
-\langle \nabla S_\Lambda, \nabla W_\Lambda\rangle
\le -c_0 W_\Lambda + C_1,
\]
while locality controls the Laplacian term:
\[
\Delta W_\Lambda \le C_2 + C_3 W_\Lambda,
\]
yielding the drift inequality with $\alpha=c_0-C_3>0$.

**Why this matters:** once local Poincaré/LSI holds on $\Omega$ (e.g. the SAFE region), standard theorems upgrade it to a **global** PI/LSI with constants depending only on local constants and $(\alpha,\beta)$.

---

## 2. PBH / Polchinski-type flows and a Riccati inequality for Hessians

Many RG constructions can be phrased as a semigroup on effective potentials $V_t$ obtained by integrating out Gaussian (or approximately Gaussian) fluctuations with covariance $C_t$:
\[
e^{-V_{t+\delta t}(x)}
\;\propto\;
\int e^{-V_t(x+\eta)}\, d\gamma_{C_{\delta t}}(\eta).
\]

Differentiating in $t$ yields a PBH/Polchinski-type PDE. Under broad hypotheses, one can derive a **matrix Riccati-type inequality** for the Hessian
\[
H_t(x) := \nabla^2 V_t(x).
\]

A prototypical inequality (the one extracted in the project files) is:

\[
\boxed{
\frac{d}{dt}H_t(x)
\;\succeq\;
- H_t(x)^2 + \kappa\, I
}
\]
in the Loewner order, for some $\kappa>0$ depending on the fluctuation covariance.

Intuition: convolution with a log-concave kernel is "smoothing + convexifying", and the quadratic term $-H^2$ is the nonlinear relaxation pushing eigenvalues upward toward $\sqrt{\kappa}$.

---

## 3. Scalar comparison and explicit lower bounds

Let $y(t)$ solve the scalar ODE
\[
y'(t) = -y(t)^2 + \kappa,\qquad y(0)=y_0.
\]
Then standard comparison results imply:

> If $H_0(x)\succeq y_0 I$ for all $x$ and $H_t$ satisfies $H_t'\succeq -H_t^2+\kappa I$, then
> \[
> H_t(x)\succeq y(t)\, I \quad\text{for all }x,t.
> \]

The scalar ODE can be solved explicitly:

- If $|y_0|<\sqrt{\kappa}$,
  \[
  y(t)=\sqrt{\kappa}\,\tanh\!\bigl(\sqrt{\kappa}\,t + \operatorname{artanh}(y_0/\sqrt{\kappa})\bigr).
  \]
- If $y_0>\sqrt{\kappa}$,
  \[
  y(t)=\sqrt{\kappa}\,\coth\!\bigl(\sqrt{\kappa}\,t + \operatorname{arcoth}(y_0/\sqrt{\kappa})\bigr).
  \]

In either case:
\[
y(t)\to \sqrt{\kappa}\quad\text{as }t\to\infty,
\]
and convergence is exponential on the scale $t\sim 1/\sqrt{\kappa}$.

### A practical corollary

If at some intermediate scale you can certify even a weak uniform convexity
\[
H_{t_0}(x)\succeq \varepsilon I,
\]
then after RG time $\Delta t \gtrsim \frac{1}{\sqrt{\kappa}}\log\!\frac{1}{\varepsilon}$ you can upgrade to
\[
H_{t_0+\Delta t}(x)\succeq (1-\eta)\sqrt{\kappa}\,I,
\]
for any chosen tolerance $\eta\in(0,1)$.

---

## 4. How this plugs into the SAFE-region strategy

The SAFE-region work provides a *local* convexity window at a fixed microscopic scale:
\[
\nabla^2 S_a \succeq \kappa_* I \quad\text{on }\Omega_{\rm SAFE}.
\]

Two threats remain:

1. **Global escape:** the measure may spend time outside $\Omega_{\rm SAFE}$.
2. **Scale degradation:** integrating out modes may weaken convexity.

The two tools above respond, respectively:

- Lyapunov drift gives a uniform return mechanism (globalization).
- Riccati convexification suggests convexity is **RG-stable** or even **RG-improving**, provided the coarse-graining kernel has a uniform log-concavity scale $\kappa$.

This is a plausible route to an RG-invariant (or at least nonvanishing) lower bound on the effective convexity parameter:
\[
\inf_{t\ge0}\;\inf_x \lambda_{\min}\bigl(\nabla^2 V_t(x)\bigr) \;>\;0,
\]
which is exactly what one wants to keep PI/LSI constants from collapsing.

---

## 5. Missing pieces to make this rigorous in Yang--Mills

1. **Identify the correct RG PDE.** The YM block-spin map is not exactly Gaussian; one needs either a rigorous approximate Gaussianization or a comparison theorem.
2. **Control of the nonlinearities.** The Riccati inequality typically requires bounds on third derivatives or conditional covariance operators.
3. **Gauge constraints / physical sector.** The inequality should hold in the horizontal (gauge-invariant) directions; the flow must respect the sector.

---

## Provenance in this project

This note is synthesized primarily from:

- `Riccati comparison for Hessian lower bounds under PBH-type flows.txt` (matrix Riccati inequality and comparison philosophy),
- `Comparing Diffusion and OS Gaps.txt` (Riccati restoration inequality phrased for RG steps),
- `Full Proof Attempt at 12-10-25 Many holes.txt` (Lyapunov drift inequalities and the YM specialization via plaquette Lyapunov functions).

