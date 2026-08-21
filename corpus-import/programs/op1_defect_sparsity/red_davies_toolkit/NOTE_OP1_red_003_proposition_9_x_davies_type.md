# Proposition 9.X (Davies‑type decay for the massive Maxwell Green kernel).

Proposition 9.X (Davies‑type decay for the massive Maxwell Green kernel).
Let \Lambda be any finite periodic lattice, let D_E be the link‑graph degree constant from Lemma 9.3, and let
M_\Lambda \;=\; m^2 I + \alpha d_1^*d_1
\qquad\text{on}\qquad
\mathsf H_E=\ell^2(E(\Lambda);\mathfrak g),
with m^2>0, \alpha>0. Then for all links b,b'\in E(\Lambda),
\big|\big(M_\Lambda^{-1}\big)_{bb'}\big|_{\mathrm{op}}
\ \le\
\frac{2}{m^2}\,
\exp\!\Big(-\eta_{\mathrm{DG}}\,\mathrm{dist}_E(b,b')\Big),
\tag{9.DG.1}
where one may take the decay rate
\eta_{\mathrm{DG}}
\ :=\
2\,\operatorname{arsinh}\!\Big(\frac{m}{2\sqrt{\alpha D_E}}\Big)
\ =\
\operatorname{arcosh}\!\Big(1+\frac{m^2}{2\alpha D_E}\Big).
\tag{9.DG.2}

In particular, in the “small mass” regime m^2\ll \alpha,
\eta_{\mathrm{DG}}
\sim
\frac{m}{\sqrt{\alpha D_E}},
\qquad\text{whereas}\qquad
\eta_{\mathrm{CT}}
\sim
\frac{m^2}{\alpha D_E}.
\tag{9.DG.3}
Thus the Davies/Dirichlet‑form method improves the small‑mass scaling of the decay exponent from quadratic in m to linear in m (up to the same local constant D_E).

⸻

Proof.

Step 1: a Davies perturbation bound for the Maxwell semigroup.
Let L_\Lambda:=\alpha d_1^*d_1, so M_\Lambda=m^2I+L_\Lambda. Fix a “target link” b'\in E(\Lambda) and define the 1‑Lipschitz weight
\phi_{b'}(b):=\mathrm{dist}_E(b,b'),\qquad b\in E(\Lambda).
For \lambda\ge 0, let W_\lambda be multiplication by e^{\lambda\phi_{b'}} on \mathsf H_E, i.e.
(W_\lambda f)(b)=e^{\lambda\phi_{b'}(b)}\,f(b).
Define the conjugated operator L_{\Lambda,\lambda}:=W_\lambda L_\Lambda W_\lambda^{-1}. Since L_\Lambda is self‑adjoint and W_\lambda is self‑adjoint and invertible, one has
L_{\Lambda,\lambda}^* \;=\; L_{\Lambda,-\lambda}.
Hence for any u\in\mathsf H_E,
\Re\langle u,L_{\Lambda,\lambda}u\rangle
=\frac12\,\langle u,(L_{\Lambda,\lambda}+L_{\Lambda,-\lambda})u\rangle.
\tag{9.DG.4}
In the link‑coordinate block representation, for b\neq \tilde b,
(L_{\Lambda,\lambda})_{b\tilde b}
=
e^{\lambda(\phi_{b'}(b)-\phi_{b'}(\tilde b))}\,(L_\Lambda)_{b\tilde b},
\qquad
(L_{\Lambda,-\lambda})_{b\tilde b}
=
e^{-\lambda(\phi_{b'}(b)-\phi_{b'}(\tilde b))}\,(L_\Lambda)_{b\tilde b},
so the symmetric part satisfies
\Big(\frac{L_{\Lambda,\lambda}+L_{\Lambda,-\lambda}}{2}\Big)_{b\tilde b}
=
\cosh\!\big(\lambda(\phi_{b'}(b)-\phi_{b'}(\tilde b))\big)\,(L_\Lambda)_{b\tilde b}
\qquad (b\neq \tilde b).
\tag{9.DG.5}
By Lemma 9.4, (L_\Lambda)_{b\tilde b}\neq 0 implies \mathrm{dist}_E(b,\tilde b)\le 1, hence by 1‑Lipschitzness |\phi_{b'}(b)-\phi_{b'}(\tilde b)|\le 1. Therefore
\cosh\!\big(\lambda(\phi_{b'}(b)-\phi_{b'}(\tilde b))\big)-1
\ \le\
\cosh(\lambda)-1.
Define the symmetric perturbation
Q_{\Lambda,\lambda}
:=\frac{L_{\Lambda,\lambda}+L_{\Lambda,-\lambda}}{2}-L_\Lambda.
Then Q_{\Lambda,\lambda} has zero diagonal and for each b,
\sum_{\tilde b\neq b}\big| (Q_{\Lambda,\lambda})_{b\tilde b}\big|_{\mathrm{op}}
\le
(\cosh\lambda-1)\sum_{\tilde b\neq b}\big|(L_\Lambda)_{b\tilde b}\big|_{\mathrm{op}}.
Using Lemma 9.4’s crude bound \sum_{\tilde b\neq b}|(L_\Lambda)_{b\tilde b}|_{\mathrm{op}}\le \alpha D_E, we obtain
\|Q_{\Lambda,\lambda}\|
\le
\alpha D_E\,(\cosh\lambda-1).
\tag{9.DG.6}
Since L_\Lambda\succeq 0, we deduce the lower bound on the symmetric part
\Re\langle u,L_{\Lambda,\lambda}u\rangle
=
\Big\langle u,\Big(L_\Lambda+Q_{\Lambda,\lambda}\Big)u\Big\rangle
\ge
-\alpha D_E(\cosh\lambda-1)\,\|u\|^2.
\tag{9.DG.7}

Now consider S_t:=e^{-tL_\Lambda}, a contraction semigroup on \mathsf H_E. By similarity,
W_\lambda S_t W_\lambda^{-1}
=
e^{-tL_{\Lambda,\lambda}}.
Let u(t):=e^{-tL_{\Lambda,\lambda}}u_0. Then
\frac{d}{dt}\|u(t)\|^2
=
-2\,\Re\langle u(t),L_{\Lambda,\lambda}u(t)\rangle
\le
2\alpha D_E(\cosh\lambda-1)\,\|u(t)\|^2,
so Grönwall yields
\|e^{-tL_{\Lambda,\lambda}}\|
\le
\exp\!\big(\alpha D_E(\cosh\lambda-1)t\big).
\tag{9.DG.8}

Step 2: weighted resolvent bound.
Using the Laplace transform representation
M_\Lambda^{-1}
=
\int_0^\infty e^{-m^2 t}\,e^{-tL_\Lambda}\,dt
\qquad\text{(Bochner integral in operator norm)},
multiply by W_\lambda and use (9.DG.8):
\|W_\lambda M_\Lambda^{-1} W_\lambda^{-1}\|
\le
\int_0^\infty e^{-m^2 t}\,\|W_\lambda e^{-tL_\Lambda} W_\lambda^{-1}\|\,dt
\le
\int_0^\infty
\exp\!\big(-(m^2-\alpha D_E(\cosh\lambda-1))t\big)\,dt.
Hence, whenever
m^2>\alpha D_E(\cosh\lambda-1),
\tag{9.DG.9}
we obtain
\|W_\lambda M_\Lambda^{-1} W_\lambda^{-1}\|
\le
\frac{1}{m^2-\alpha D_E(\cosh\lambda-1)}.
\tag{9.DG.10}

Step 3: pointwise kernel bound.
By definition of W_\lambda, for b' fixed we have
(W_\lambda M_\Lambda^{-1} W_\lambda^{-1})_{bb'}
=
e^{\lambda\phi_{b'}(b)}(M_\Lambda^{-1})_{bb'}e^{-\lambda\phi_{b'}(b')}
=
e^{\lambda\mathrm{dist}_E(b,b')}(M_\Lambda^{-1})_{bb'}.
Therefore
\big|(M_\Lambda^{-1})_{bb'}\big|_{\mathrm{op}}
\le
e^{-\lambda\mathrm{dist}_E(b,b')}\,\|W_\lambda M_\Lambda^{-1} W_\lambda^{-1}\|.
\tag{9.DG.11}
Insert (9.DG.10), and choose \lambda so that the denominator is exactly m^2/2, i.e.
\alpha D_E(\cosh\lambda-1)=\frac{m^2}{2}.
This is equivalent to \sinh(\lambda/2)=\frac{m}{2\sqrt{\alpha D_E}}, hence \lambda=2\operatorname{arsinh}\!\big(\frac{m}{2\sqrt{\alpha D_E}}\big). With this choice, (9.DG.11) becomes (9.DG.1)–(9.DG.2). The asymptotics (9.DG.3) follow from \operatorname{arsinh}(x)\sim x and \log(1+x)\sim x as x\downarrow 0. \square

⸻
