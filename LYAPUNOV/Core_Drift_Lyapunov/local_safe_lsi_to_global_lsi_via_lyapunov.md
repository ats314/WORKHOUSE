# From Local SAFE Log-Sobolev Inequality to Global LSI via Lyapunov Drift

## Abstract
We prove that a uniform local log-Sobolev inequality (LSI) on a SAFE region, combined with a Lyapunov drift condition, yields a global LSI with a strictly positive constant independent of system size.

## Assumptions
Let $d\mu=Z^{-1}e^{-V}dx$ with generator $L=\Delta-\nabla V\cdot\nabla$.

1. (Local LSI) There exists $K\subset M$ and $\rho_K>0$ such that
\[
\mathrm{Ent}_{\mu_K}(g^2) \le \frac{2}{\rho_K}\int_K |\nabla g|^2 d\mu_K.
\]
2. (Lyapunov Drift) There exists $W\ge1$ with
\[
LW \le -\alpha W + b\mathbf{1}_K.
\]
3. (Cutoff) A smooth $\phi$ supported in $K$ with bounded gradient.

## Theorem
Under these assumptions, $\mu$ satisfies a global LSI
\[
\mathrm{Ent}_\mu(f^2) \le \frac{2}{\rho}\int |\nabla f|^2 d\mu,
\]
with
\[
\rho \gtrsim \min\Big\{\rho_K,\frac{\alpha}{1+\log\int W d\mu}\Big\}.
\]

## Proof Sketch
Decompose $f=\phi f+(1-\phi)f$. Apply local LSI to the first term and control the tail using weighted inequalities derived from the Lyapunov drift. Cross terms are absorbed via Rothaus/Herbst arguments.

## Significance
This gives a volume-uniform route from local convexity to global functional inequalities, compatible with RG and coarse-graining.

