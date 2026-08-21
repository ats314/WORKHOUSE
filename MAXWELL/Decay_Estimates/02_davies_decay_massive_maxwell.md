# Davies-type decay for the massive Maxwell Green kernel

## 1. Abstract finite-range setting

Let $(V,\mathrm{dist})$ be a countable graph metric space and let $\mathsf H_0$ be a finite-dimensional Hilbert space.  Consider the Hilbert space $\ell^2(V;\mathsf H_0)$.

Let $L$ be a self-adjoint, positive semidefinite operator on $\ell^2(V;\mathsf H_0)$ with **finite range 1**:
\[
L_{xy}=0\quad\text{whenever }\mathrm{dist}(x,y)>1.
\]
Assume a uniform off-diagonal row-sum bound
\[
C_0:=\sup_{x\in V}\sum_{y\neq x}\|L_{xy}\|_{\mathrm{op}}<\infty.
\]
Fix $m>0$ and define the massive resolvent
\[
G:=(L+m^2)^{-1}.
\]

The goal is an **explicit exponential off-diagonal bound** on the kernel $G_{xy}$.

## 2. Davies conjugation

Fix a basepoint $y\in V$ and define the 1-Lipschitz function
\[
\phi_y(x):=\mathrm{dist}(x,y).
\]
For $\lambda\in\mathbb R$ define the multiplication operator
\[
(W_\lambda f)(x):=e^{\lambda \phi_y(x)}f(x),
\]
and the conjugated operator
\[
L_{\lambda}:=W_\lambda L W_{-\lambda}.
\]
Since $W_\lambda$ is invertible, $L_\lambda$ is similar to $L$ and therefore generates a (possibly non-self-adjoint) semigroup.

Define the symmetric perturbation
\[
Q_\lambda:=\frac{L_{\lambda}+L_{-\lambda}}{2}-L.
\]
A direct kernel computation gives, for $x\neq x'$,
\[
(Q_\lambda)_{xx'}=\big(\cosh(\lambda(\phi_y(x)-\phi_y(x')))-1\big)\,L_{xx'}.
\]
Because $\phi_y$ is 1-Lipschitz and $L$ has range 1, whenever $L_{xx'}\neq 0$ one has $|\phi_y(x)-\phi_y(x')|\le 1$, hence
\[
\cosh(\lambda(\phi_y(x)-\phi_y(x')))-1\le \cosh(\lambda)-1.
\]
Therefore, for each $x$,
\[
\sum_{x'\neq x}\|(Q_\lambda)_{xx'}\|_{\mathrm{op}}
\le (\cosh\lambda-1)\sum_{x'\neq x}\|L_{xx'}\|_{\mathrm{op}}
\le C_0(\cosh\lambda-1),
\]
which implies the operator norm bound
\[
\|Q_\lambda\|\le C_0(\cosh\lambda-1).
\tag{2.1}
\]

Since $L\succeq 0$ and $Q_\lambda$ is self-adjoint, the real part of the quadratic form obeys
\[
\Re\langle u, L_{\lambda}u\rangle
=\langle u,(L+Q_\lambda)u\rangle
\ge -\|Q_\lambda\|\,\|u\|^2
\ge -C_0(\cosh\lambda-1)\,\|u\|^2.
\tag{2.2}
\]

## 3. Semigroup growth bound

Let $S_t:=e^{-tL}$, a contraction semigroup. By similarity,
\[
W_\lambda S_t W_{-\lambda}=e^{-tL_{\lambda}}.
\]
Let $u(t):=e^{-tL_{\lambda}}u_0$. Differentiating and using (2.2),
\[
\frac{d}{dt}\|u(t)\|^2
=-2\Re\langle u(t),L_{\lambda}u(t)\rangle
\le 2C_0(\cosh\lambda-1)\|u(t)\|^2.
\]
By Grönwall,
\[
\|e^{-tL_{\lambda}}\|
\le \exp\big(C_0(\cosh\lambda-1)t\big).
\tag{3.1}
\]

## 4. Resolvent kernel bound

Use the Laplace representation
\[
(L+m^2)^{-1}=\int_0^{\infty} e^{-m^2 t} e^{-tL}\,dt.
\]
Conjugating and taking norms yields
\[
\|W_\lambda (L+m^2)^{-1} W_{-\lambda}\|
\le \int_0^{\infty} e^{-m^2 t}\,\|e^{-tL_{\lambda}}\|\,dt
\le \int_0^{\infty}\exp\big(-(m^2-C_0(\cosh\lambda-1))t\big)\,dt.
\]
If $m^2>C_0(\cosh\lambda-1)$, then
\[
\|W_\lambda (L+m^2)^{-1} W_{-\lambda}\|
\le \frac{1}{m^2-C_0(\cosh\lambda-1)}.
\tag{4.1}
\]

Now relate operator norm bounds to kernel bounds.  For $x,y\in V$ and $v\in\mathsf H_0$ with $|v|=1$,
\[
\|(L+m^2)^{-1}_{xy}v\|
= e^{-\lambda(\phi_y(x)-\phi_y(y))}\,\big\|\big(W_\lambda (L+m^2)^{-1} W_{-\lambda}\big)_{xy}v\big\|
\le e^{-\lambda\,\mathrm{dist}(x,y)}\,\|W_\lambda (L+m^2)^{-1} W_{-\lambda}\|.
\]
Using (4.1) gives
\[
\|(L+m^2)^{-1}_{xy}\|_{\mathrm{op}}
\le \frac{e^{-\lambda\mathrm{dist}(x,y)}}{m^2-C_0(\cosh\lambda-1)}
\qquad\text{for any }\lambda\text{ with }m^2>C_0(\cosh\lambda-1).
\tag{4.2}
\]

## 5. Optimizing the exponent (small-$m$ behavior)

Choose $\lambda$ by saturating the admissibility constraint
\[
C_0(\cosh\lambda-1)=\frac{m^2}{2}.
\]
Then
\[
\cosh\lambda = 1+\frac{m^2}{2C_0},
\qquad
\lambda = \operatorname{arcosh}\Big(1+\frac{m^2}{2C_0}\Big)
=2\operatorname{arsinh}\Big(\frac{m}{2\sqrt{C_0}}\Big).
\tag{5.1}
\]
With this choice, (4.2) becomes
\[
\|(L+m^2)^{-1}_{xy}\|_{\mathrm{op}}
\le \frac{2}{m^2}\,\exp\Big(-\eta\,\mathrm{dist}(x,y)\Big),
\qquad
\eta := 2\operatorname{arsinh}\Big(\frac{m}{2\sqrt{C_0}}\Big).
\tag{5.2}
\]
Notably, for small $m$,
\[
\eta \sim \frac{m}{\sqrt{C_0}},
\]
so the decay exponent scales linearly in $m$ (in contrast to Combes–Thomas bounds of the form $\log(1+m^2/(2C_0))\sim m^2$).

## 6. Boundary row-sum refinement

Sometimes $C_0$ is a pessimistic constant because it counts all couplings out of $x$, even those that do not change the distance to $y$.

Define the **boundary row-sum constant**
\[
C_{\partial}(L)
:= \sup_{y\in V}\ \max_{x\in V}\ \sum_{\substack{x'\neq x\\|\phi_y(x)-\phi_y(x')|=1}}\|L_{xx'}\|_{\mathrm{op}}.
\tag{6.1}
\]
Repeating the proof with the improved estimate
\(
\sum_{x'\neq x}\|(Q_\lambda)_{xx'}\|\le (\cosh\lambda-1) C_{\partial}(L)
\)
shows that (5.2) holds with $C_{\partial}(L)$ in place of $C_0$.

## 7. Specialization to the massive Maxwell operator

On a lattice link graph, take
\[
L=\alpha\,d_1^*d_1\quad\text{(restricted to horizontals)},
\qquad
m^2>0,
\]
so that $M:=m^2 I+L$ is the massive Maxwell operator.  The above gives an explicit off-diagonal decay bound for $M^{-1}$ with exponent
\[
\eta = 2\operatorname{arsinh}\Big(\frac{m}{2\sqrt{\alpha\,C_0(d_1^*d_1)}}\Big)
\quad\text{or}\quad
\eta = 2\operatorname{arsinh}\Big(\frac{m}{2\sqrt{\alpha\,C_{\partial}(d_1^*d_1)}}\Big)
\]
(depending on which constant is available).
