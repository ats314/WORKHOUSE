# Merged PMBSF / SU(N) / Wilson Projected-Capacity Draft

**Merge date:** 2026-05-30  
**Merge operation:** Integrated the corrected key derivations into the existing $\mathrm{SU}(3)$ one-plaquette class-spectrum manuscript.  

## Merge map

- §§1--6: local $\mathrm{SU}(3)$ class-spectrum computation and leakage matrix, preserving the existing manuscript spine.
- §7: replaces the older threshold-only text with the finite-channel threshold plus the full-channel Laguerre-tail obstruction and the Casimir-shell replacement target.
- §8: updates the $\mathrm{SU}(N)$ framework with the corrected $c_0^{(N)}$ formula, the $N=4,5,6$ ledgers, the $H_1$ notation warning, and degree-six reduced-leakage saturation.
- §9: adds the corrected projected-capacity route: no-go theorem for global fixed-window top norm, rooted polymer replacement, correct source-tilting identity, Wilson-to-Bernoulli square-free domination, and the inhomogeneous free-energy target.
- §10: consolidates scope and next analytic targets.
- Appendix A: retained from the existing derivation of $H_1$ and $H_2$.

---


# 1. Introduction and merged theorem map

## 1.1 Purpose of this merged draft

This draft merges the existing $\mathrm{SU}(3)$ one-plaquette class-spectrum manuscript with the corrected derivations from the recent project notes. The merger keeps the local spectral computation as the rigorous core and moves the polymer/firewall material into a carefully separated conditional layer.

The central local object is the class-sector one-plaquette Wilson Hamiltonian
$$
H_\beta=\frac12 C_2+\beta\left(1-\frac1N\Re\chi_{\mathrm{fund}}(g)\right),
$$
restricted to Weyl-invariant class functions near the identity. Large $\beta$ is the strong-potential regime. After the Cartan rescaling, the spectrum is oscillator-dominated, with corrections in half-integer powers of $\beta^{-1}$.

The project now has three distinct layers:

1. **Local class-spectrum layer.** Exact $\mathrm{SU}(3)$ one-plaquette gap and exact four-channel leakage matrix.
2. **Finite-channel polymer diagnostic layer.** A conditional threshold obtained by inserting the exact finite leakage matrix into a polymer-resolvent architecture.
3. **Projected-capacity / Wilson-transfer layer.** A corrected route for sparse hard defects after the no-go result for global fixed-window top-norm control.

The first layer is the theorem-level contribution of the present manuscript. The second and third layers identify where additional constructive input is required.

## 1.2 The local $\mathrm{SU}(3)$ spectral anchor

The $\mathrm{SU}(3)$ one-plaquette class gap is
$$
\boxed{
\Delta_{\mathrm{SU}(3)}(\beta)
=
\sqrt{\frac{2\beta}{3}}
-\frac5{16}
-\frac{311\sqrt6}{9216}\,\beta^{-1/2}
+O(\beta^{-1}).
}
$$

The leading term is the Cartan oscillator gap. The coefficient $-5/16$ is the first-order shift from $H_1=-p_2^2/96$. The coefficient $-311\sqrt6/9216$ is the sum of a radial resolvent contribution and a direct second-order shift from $H_2$.

The rank-two point is that $H_2$ contains the non-radial Weyl invariant $p_3^2$. A radial reduction gives
$$
c_1^{\mathrm{radial}}=-\frac{327\sqrt6}{9216},
$$
while the full Weyl-invariant computation gives
$$
c_1=-\frac{311\sqrt6}{9216}.
$$
The discrepancy
$$
\boxed{c_1-c_1^{\mathrm{radial}}=\frac{\sqrt6}{576}}
$$
comes exactly from the $p_3^2$ term in $H_2$.

## 1.3 The finite leakage matrix

The same first-order matrix elements define a four-channel nonnegative leakage matrix $T^{(3)}$ on the radial channels
$$
F_3=\{\psi_0,\psi_1,\psi_3,\psi_5\}.
$$
Its Perron root is
$$
\boxed{\rho_3=0.5501615335231425806844\ldots.}
$$
This is an exact finite-channel diagnostic: it measures low-channel source leakage through $H_1$. It is not, by itself, a full infinite-channel polymer constant.

## 1.4 Corrected status of the polymer threshold

The finite-channel polymer-resolvent threshold remains a useful number. In the isolated four-channel model, the Schur/Poincaré criterion gives
$$
\boxed{\beta>\frac32\,\mu_{\mathcal G}^4\rho_3^2.}
$$
At the representative value $\mu_{\mathcal G}=3$, this is
$$
\boxed{\beta>36.78.}
$$

The corrected status is sharper than the older draft: this is a finite-channel threshold only. The infinite radial Laguerre tower is not automatically a compact perturbation of the four-channel matrix. The obstruction is that multiplication by $H_1=-u^2/96$ has off-diagonal coefficients growing like $n^2$, while the one-step class resolvent supplies only one shell denominator. Schur symmetrisation makes the high-shell transfer bounded but not tail-compact. A full-channel theorem needs additional smoothing, a different norm, a finite analytic cutoff, or a genuine full radial/Peter--Weyl transfer constant.

## 1.5 Corrected $\mathrm{SU}(N)$ local extension

For fixed $N$, the same finite local computation is mechanical through degree six. The corrected candidate for the first-order gap coefficient is
$$
\boxed{
c_0^{(N)}=-\frac{2N^2-3}{16N}
=-\frac N8+\frac{3}{16N}.
}
$$
It matches the local ledgers
$$
c_0^{(3)}=-\frac5{16},\qquad
c_0^{(4)}=-\frac{29}{64},\qquad
c_0^{(5)}=-\frac{47}{80},\qquad
c_0^{(6)}=-\frac{23}{32}.
$$

The $\mathrm{SU}(4)$ numerical local ledger is
$$
\Delta_{\mathrm{SU}(4)}(\beta)
=
\sqrt{\frac\beta2}
-\frac{29}{64}
-0.205951755360250\,\beta^{-1/2}
+O(\beta^{-1}),
$$
with
$$
\rho_4^{\mathrm{red}}=0.959702818730095.
$$
This is numerically locked, but the exact symbolic write-up has not yet been produced.

## 1.6 Corrected projected-capacity route

The previous global fixed-window top-norm target
$$
\|P_{\Lambda,L}\mathbf 1_{D_L}P_{\Lambda,L}\|\le c<1
$$
uniformly in $L$ at fixed nonzero defect density is false. Rare fully defective islands force the norm to approach one in probability.

The replacement is rooted: control the bad plaquette animal containing a fixed root, not the largest island anywhere in the volume. The Wilson input becomes an inhomogeneous free-energy stability or Peierls estimate. In its clean source-tilted form, the target is
$$
\boxed{
\frac{Z_{\beta,\alpha,\Gamma}}{Z_\beta}\le K_\alpha^{|\Gamma|}
}
$$
for finite connected plaquette animals $\Gamma$, where $Z_{\beta,\alpha,\Gamma}$ has coupling $\alpha\beta$ on $\Gamma$ and $\beta$ off $\Gamma$. This yields
$$
z_{\beta,\delta,\alpha}=K_\alpha e^{-(1-\alpha)\beta\delta},
$$
and the rooted projected-capacity polymer condition
$$
\boxed{
\mu_{\mathcal P}K_\alpha
\exp\left[-(1-\alpha)\beta\delta+a+s\gamma\right]<1.
}
$$

The exact source-tilting identity is
$$
\boxed{
\mathbb E_\beta\exp\left(t\sum_{p\in\Gamma}V_p\right)
=
\frac{Z(\beta-t\mathbf 1_\Gamma)}{Z(\beta)}.
}
$$
The inverse ratio is wrong.

## 1.7 Manuscript boundary

The theorem-level content of this merged draft is the local $\mathrm{SU}(3)$ computation and the finite leakage matrix. The finite-channel polymer threshold is conditional. The projected-capacity route is a corrected theorem architecture with a precise missing input: inhomogeneous Wilson free-energy stability strong enough to imply rooted Peierls summability.


# 2. The one-plaquette class Hamiltonian, Weyl reduction, and the perturbation series

## 2.1 The one-plaquette class Hamiltonian

The object of study is the class sector of the $\mathrm{SU}(3)$ one-plaquette Wilson Hamiltonian,
$$
H_\beta=\tfrac12\,C_2+\beta\Bigl(1-\tfrac13\,\Re\chi_{(1,0)}(g)\Bigr),
$$
acting on class functions on $\mathrm{SU}(3)$. The electric term $\tfrac12 C_2$ is the quadratic Casimir, i.e. the Laplace–Beltrami operator on the group; the magnetic term is built from the character $\chi_{(1,0)}$ of the fundamental representation. The parameter $\beta$ is the inverse coupling. We work in the regime of large $\beta$, where the plaquette potential is strong, the class variable is confined to a neighbourhood of the identity, and the spectrum is dominated by a harmonic well with corrections organised in powers of $\beta^{-1/2}$.

The local class-function gap is
$$
\Delta_{\mathrm{SU}(3)}(\beta)=E_1(\beta)-E_0(\beta),
$$
the difference between the ground class state $E_0$ and the first excited class state $E_1$ of $H_\beta$ in the inner product fixed in §2.5.

## 2.2 Reduction to the Cartan torus and the Weyl group

A class function is constant on conjugacy classes, so it is determined by its restriction to the maximal torus. Writing an element near the identity as $g\sim\operatorname{diag}(e^{i\theta_1},e^{i\theta_2},e^{i\theta_3})$ with the $\mathfrak{su}(3)$ trace condition
$$
\theta_1+\theta_2+\theta_3=0,
$$
the angles $\vec\theta$ lie on a two-dimensional plane in $\mathbb{R}^3$. The fundamental character restricts to
$$
\chi_{(1,0)}=\sum_{j=1}^3 e^{i\theta_j},
\qquad
\Re\chi_{(1,0)}=\sum_{j=1}^3\cos\theta_j,
$$
so the plaquette potential is $V=\beta\bigl(1-\tfrac13\sum_j\cos\theta_j\bigr)$.

The residual gauge symmetry on the torus is the Weyl group $W=S_3$, which permutes the three angles. Class functions are exactly the $W$-invariant (symmetric) functions of $\vec\theta$; equivalently they are functions on the closed Weyl chamber, a $60^\circ$ wedge of the $\sum_j\theta_j=0$ plane. We coordinatise this plane orthonormally by $(x,y)$ through the orthonormal basis $u=\tfrac1{\sqrt2}(1,-1,0)$, $v=\tfrac1{\sqrt6}(1,1,-2)$, so that
$$
\theta_1=\tfrac{x}{\sqrt2}+\tfrac{y}{\sqrt6},
\qquad
\theta_2=-\tfrac{x}{\sqrt2}+\tfrac{y}{\sqrt6},
\qquad
\theta_3=-\tfrac{2y}{\sqrt6}.
$$
In these coordinates the Weyl reflection $y\mapsto-y$ is one of the generators of $W$, and it will provide the parity selection rule used throughout §§4–6.

## 2.3 The Weyl invariants as power sums

The ring of $W=S_3$ invariants on $\{\sum_j\theta_j=0\}$ is generated by two algebraically independent polynomials. The most convenient generators are the power sums
$$
p_2=\sum_j\theta_j^2=x^2+y^2,
\qquad
p_3=\sum_j\theta_j^3=\tfrac{\sqrt6}{6}\,y\,(3x^2-y^2),
$$
the first identity following from orthonormality of $(x,y)$ and the second by direct substitution. (Equivalently one may use the elementary symmetric polynomials $e_2=\sum_{i<j}\theta_i\theta_j=-\tfrac12 p_2$ and $e_3=\theta_1\theta_2\theta_3=\tfrac13 p_3$, obtained from Newton's identities with $e_1=0$.) Every class function near the identity is a function of $p_2$ and $p_3$.

The two generators play structurally different roles. The degree-$2$ invariant $p_2$ is the squared radius of the Cartan plane and is even under every Weyl reflection. The degree-$3$ invariant $p_3$ is genuinely angular: under $y\mapsto-y$ it changes sign, $p_3\mapsto-p_3$, while $p_2$ is fixed. We use "radial" for dependence on $p_2$ alone and "non-radial" or "angular" for any dependence on $p_3$. There is no degree-$1$ invariant — the trace condition $\sum_j\theta_j=0$ removes the linear coordinate — and this fact fixes the location of the first excited class state in §2.6.

## 2.4 The Weyl discriminant

The Jacobian of the Weyl integration formula is the squared Weyl denominator, whose leading polynomial form near the identity is the squared Vandermonde of the angles, $\prod_{i<j}(\theta_i-\theta_j)^2$. This is precisely the discriminant of the characteristic cubic, and it has a clean closed form in the invariants.

**Lemma 2.1.**
$$
\Delta_W^2:=\prod_{i<j}(\theta_i-\theta_j)^2
=\tfrac{x^2(x^2-3y^2)^2}{2}
=\tfrac{p_2^3}{2}-3\,p_3^2 .
$$

*Proof.* The angles $\theta_j$ are the roots of the monic cubic $t^3-e_1t^2+e_2t-e_3=t^3+e_2t-e_3$, since $e_1=\sum_j\theta_j=0$. The discriminant of a depressed cubic $t^3+Pt+Q$ is $-4P^3-27Q^2$, and it equals $\prod_{i<j}(\theta_i-\theta_j)^2$. With $P=e_2=-\tfrac{p_2}{2}$ and $Q=-e_3=-\tfrac{p_3}{3}$,
$$
\prod_{i<j}(\theta_i-\theta_j)^2
=-4\Bigl(-\tfrac{p_2}{2}\Bigr)^3-27\Bigl(\tfrac{p_3}{3}\Bigr)^2
=\tfrac{p_2^3}{2}-3\,p_3^2 .
$$
Substituting the coordinate expressions for $p_2,p_3$ gives the equivalent form $\tfrac12 x^2(x^2-3y^2)^2$. $\qquad\blacksquare$

Geometrically, $\Delta_W^2$ vanishes exactly when two of the angles coincide — that is, on the walls of the Weyl chamber — which is where the conjugacy classes degenerate. The crucial structural feature for the rest of the paper is the explicit $-3p_3^2$ term: the Weyl measure is *not* a function of $p_2$ alone. The angular invariant is built into the very weight against which class-function expectations are computed, and this is the ultimate reason the gap cannot be computed by a radial reduction (§2.7, §5.3).

## 2.5 The Weyl–Gaussian inner product

For class functions $f,g$ — functions of $(p_2,p_3)$ — the inner product appropriate to the rescaled near-identity problem is the Weyl–Gaussian form
$$
\langle f,g\rangle=\int_{\mathbb{R}^2}f\,g\,\Delta_W^2\,e^{-x^2-y^2}\,dx\,dy .
$$
Two factors appear. The discriminant $\Delta_W^2$ is the Weyl Jacobian of §2.4, converting the integral over the chamber into an integral over the plane. The Gaussian $e^{-x^2-y^2}$ is the leading harmonic weight of the strong-potential regime: after the rescaling of §2.6 extracts the oscillator, the natural $L^2$ measure for the perturbation theory carries this Gaussian. Multiplication by any real class function — in particular by the potential — is self-adjoint in this inner product, so Rayleigh–Schrödinger perturbation theory applies directly. The orthonormal shell basis $\psi_0,\dots,\psi_6$ of §3 is constructed against exactly this measure.

A radial reduction would replace this rank-two inner product by a one-dimensional Gaussian in the modulus of the Cartan plane, discarding the angular dependence. As Lemma 2.1 makes plain, this cannot be exact: the weight $\Delta_W^2$ itself contains $p_3^2$, so even radial states acquire nonzero, state-dependent expectations of angular invariants. The truncation is harmless at the first two orders of the gap and false at the third (§5.3–5.4).

## 2.6 The scaled perturbation series

To expose the strong-potential structure, rescale the Cartan coordinates by $\beta^{1/4}$. The Hamiltonian then organises by half-integer powers of $\beta$,
$$
H_\beta=\beta^{1/2}H_0+H_1+\beta^{-1/2}H_2+O(\beta^{-1}).
$$

**The leading operator and its spectrum.** The kinetic term reduces, after conjugation by the Weyl denominator, to a constant multiple of the flat Laplacian plus an additive constant: the denominator $\delta(\theta)=\prod_{\alpha>0}2\sin\!\bigl(\tfrac{\alpha(\theta)}{2}\bigr)$ satisfies $\Delta_T\delta=-\|\rho\|^2\delta$ exactly, so the conjugation contributes only the constant $-\|\rho\|^2$ and no $\theta$-dependent potential (Appendix A). Combining with the quadratic part of $V$, the leading operator $H_0$ is a two-dimensional harmonic oscillator. Its eigenstates are graded by total polynomial degree — the *shell* — with unperturbed energies
$$
E^{(0)}_s=\tfrac{\sqrt6}{6}\,s\,\beta^{1/2}+\text{const},
\qquad s=\text{shell},
$$
i.e. a uniform per-degree spacing of one oscillator quantum $\tfrac{\sqrt6}{6}\beta^{1/2}=\sqrt{\beta/6}$. The additive constant is common to all class states and cancels in every energy difference.

**The leading gap.** Because the lowest Weyl invariant above the constant is the degree-$2$ invariant $p_2$ — there being no degree-$1$ class invariant (§2.3) — the first excited class state sits two oscillator quanta above the ground state. The leading gap is therefore
$$
\omega(\beta):=E^{(0)}_2-E^{(0)}_0=2\cdot\tfrac{\sqrt6}{6}\beta^{1/2}=\sqrt{\tfrac{2\beta}{3}} .
$$
This is the leading term of the gap law; we write $\omega(\beta)$ for it throughout.

**The perturbations.** The order-$\beta^0$ and order-$\beta^{-1/2}$ terms of the scaled Hamiltonian are
$$
\boxed{\,H_1=-\tfrac{p_2^2}{96}\,}
\qquad\text{and}\qquad
\boxed{\,H_2=\sqrt6\Bigl(\tfrac{p_2^3}{11520}+\tfrac{p_3^2}{8640}\Bigr).\,}
$$
Both are read off from the Taylor expansion of the Wilson plaquette character after rescaling and Weyl reduction; the derivation, including the precise normalisation convention that fixes these constants, is carried out in Appendix A. The convention amounts to a single gap-invariant rescaling of the Cartan coordinates and does not affect the spectrum, hence does not affect $c_0$, $c_1$, or any coefficient of the gap law.

## 2.7 The non-radial term in $H_2$

The structural feature that drives the paper's result is the second term of $H_2$. The coefficient $\tfrac{\sqrt6}{8640}$ multiplies $p_3^2$, a genuinely non-radial invariant. Since $H_0$ and $H_1$ depend only on $p_2$, the perturbation series is radial through order $\beta^0$, and — as the parity argument of §4 will show — the second-order *resolvent* of $H_1$ is radial as well. The angular invariant therefore enters the gap for the first time, and only, through the direct first-order shift of $H_2$.

Two features of $H_2$ are worth recording now, both traced to the character expansion in Appendix A. First, the radial and non-radial terms occur in the fixed ratio
$$
[\,p_2^3\,]:[\,p_3^2\,]=3:4
$$
of their coefficients in the underlying potential, an algebraic consequence of the power-sum identity $P_6=\tfrac{P_2^3}{4}+\tfrac{P_3^2}{3}$. Second, the $p_3^2$ term is not optional: a radial truncation that drops it produces a different rational coefficient at order $\beta^{-1/2}$, the discrepancy being exactly $\tfrac{\sqrt6}{576}$ (§5.3–5.4). This single term is the entire difference between the genuine rank-two gap and its radial approximation.

With the Hamiltonian, the invariants, the discriminant, the inner product, and the scaled perturbations $H_1,H_2$ in place, §3 constructs the orthonormal shell basis in which all matrix elements are evaluated.


# 3. The Weyl-invariant shell basis

## 3.1 Shell grading and the invariant ring

Class functions near the identity are functions of the two Weyl invariants $p_2,p_3$ of §2.3. We grade the polynomial invariants by total degree in the Cartan coordinates $(x,y)$ — the *shell* — and orthonormalise shell by shell.

The graded dimensions are fixed by the structure of the $\mathrm{SU}(3)$ invariant ring. By Chevalley's theorem the ring of $W=S_3$ invariants is a free polynomial algebra on generators of degrees $2$ and $3$, so its Hilbert (Poincaré) series is
$$
\sum_{d\ge0}\dim\!\big(\text{invariants of degree }d\big)\,t^d
=\frac{1}{(1-t^2)(1-t^3)}
=1+t^2+t^3+t^4+t^5+2t^6+t^7+2t^8+\cdots .
$$
The coefficient of $t^d$ counts the monomials $p_2^a p_3^b$ with $2a+3b=d$. Through degree $6$ this gives one invariant at each of degrees $0,2,3,4,5$ and **two** at degree $6$, namely $p_2^3$ and $p_3^2$. The shell-graded monomial basis through degree $6$ is therefore
$$
\mathcal{B}=\{\,1,\ p_2,\ p_3,\ p_2^2,\ p_2 p_3,\ p_2^3,\ p_3^2\,\},
\qquad
\deg=\{0,2,3,4,5,6,6\}.
$$
The doubling at degree $6$ is the first appearance of the rank-two structure in the class basis, and it is precisely the shell the third-order computation reaches. In the rescaled oscillator (§2.6) the unperturbed energy is linear in the shell, $E^{(0)}_s=\tfrac{\sqrt6}{6}\,s\,\beta^{1/2}+\text{const}$.

## 3.2 The Gram–Schmidt construction and the orthonormal states

Orthonormalising $\mathcal{B}$ against the Weyl–Gaussian inner product
$$
\langle f,g\rangle=\int_{\mathbb{R}^2}f\,g\,\Delta_W^2\,e^{-x^2-y^2}\,dx\,dy
$$
produces seven orthonormal states $\psi_0,\dots,\psi_6$, one per monomial, each a polynomial of its shell degree. The required integrals are Gaussian moments weighted by the discriminant $\Delta_W^2=\tfrac12 x^2(x^2-3y^2)^2$; for instance $\langle 1,1\rangle=\tfrac{3\pi}{2}$ and the first invariant has mean $\langle p_2\rangle=4$, so the degree-$2$ state is $\psi_1\propto(p_2-4)$ after projecting off the constant. Carrying the construction through degree $6$ gives the following, which we have verified to be exactly orthonormal, $\langle\psi_i,\psi_j\rangle=\delta_{ij}$, against the measure.

$$
\psi_0=\tfrac{\sqrt6}{3\sqrt\pi},
\qquad
\psi_1=\tfrac{\sqrt6}{6\sqrt\pi}\,(x^2+y^2-4),
$$
$$
\psi_2=\tfrac{\sqrt5}{15\sqrt\pi}\,y\,(3x^2-y^2),
$$
$$
\psi_3=\tfrac{\sqrt{15}}{30\sqrt\pi}\,\bigl(x^4+2x^2y^2-10x^2+y^4-10y^2+20\bigr),
$$
$$
\psi_4=\tfrac{\sqrt{35}}{105\sqrt\pi}\,y\,\bigl(3x^4+2x^2y^2-21x^2-y^4+7y^2\bigr),
$$
$$
\psi_5=\tfrac{\sqrt{30}}{180\sqrt\pi}\,\bigl(x^6+3x^4y^2-18x^4+3x^2y^4-36x^2y^2+90x^2+y^6-18y^4+90y^2-120\bigr),
$$
$$
\psi_6=\tfrac{\sqrt{70}}{2520\sqrt\pi}\,\bigl(-x^6+33x^4y^2-27x^2y^4+3y^6\bigr).
$$

## 3.3 Radial and angular structure

These polynomials are not an arbitrary orthogonalisation; they organise into a transparent radial/angular pattern that the rest of the paper exploits. Pass to polar coordinates $x=r\cos\varphi$, $y=r\sin\varphi$. The two invariants become
$$
p_2=r^2,
\qquad
p_3=\tfrac{\sqrt6}{6}\,r^3\sin(3\varphi),
$$
and the Vandermonde factor is $x(x^2-3y^2)=r^3\cos(3\varphi)$, so the discriminant is the pure angular harmonic
$$
\Delta_W^2=\tfrac12\,r^6\cos^2(3\varphi)=\tfrac{r^6}{4}\bigl(1+\cos 6\varphi\bigr).
$$
The threefold angular dependence $\cos 3\varphi,\sin 3\varphi$ is the imprint of the order-$3$ Weyl group.

**The radial tower is associated Laguerre.** Restricting the inner product to radial functions $f(p_2),g(p_2)$ and integrating out $\varphi$, the effective one-dimensional weight is, with $u=p_2=r^2$,
$$
\int f g\,\Delta_W^2\,e^{-x^2-y^2}\,dx\,dy
\ \propto\
\int_0^\infty f(u)\,g(u)\,u^{3}\,e^{-u}\,du,
$$
the discriminant contributing the factor $u^3$ (three positive roots). The radial states are therefore the associated Laguerre polynomials $L_n^{(3)}(p_2)$:
$$
\psi_0\propto L_0^{(3)},\quad
\psi_1\propto L_1^{(3)}=-(p_2-4),\quad
\psi_3\propto L_2^{(3)},\quad
\psi_5\propto L_3^{(3)},
$$
explicitly $p_2-4$, $p_2^2-10p_2+20$, $p_2^3-18p_2^2+90p_2-120$ for $n=1,2,3$. These four states (shells $0,2,4,6$) are the radial channels that carry the gap.

**The angular sectors.** The remaining states involve $p_3$. The lowest, $\psi_2\propto p_3$ (shell $3$), is the pure threefold harmonic. The next, $\psi_4\propto p_3\,(p_2-7)$ (shell $5$), is $p_3$ times an associated Laguerre polynomial $L_1^{(6)}(p_2)$ — the $p_3$-sector carries the effective weight $u^{6}e^{-u}$, since the factor $|p_3|^2$ raises the radial power by three. Finally $\psi_6$ (shell $6$) is the lowest *even* non-radial state, built from $p_3^2$ orthogonalised against the radial tower; it is the degree-$6$, $\cos 6\varphi$ companion of the radial $\psi_5$.

## 3.4 Parity, sectors, and the unperturbed spectrum

The Weyl reflection $y\mapsto-y$ acts as $p_2\mapsto p_2$, $p_3\mapsto-p_3$, equivalently $\varphi\mapsto-\varphi$. It splits the basis into three sectors:

| sector | states | shells | form |
|---|---|---|---|
| even, radial | $\psi_0,\psi_1,\psi_3,\psi_5$ | $0,2,4,6$ | $L_n^{(3)}(p_2)$ |
| odd | $\psi_2,\psi_4$ | $3,5$ | $p_3\,L_n^{(6)}(p_2)$ |
| even, non-radial | $\psi_6$ | $6$ | degree-$6$, $\cos 6\varphi$ |

The two odd states $\psi_2,\psi_4$ change sign under the reflection; the five even states are invariant. This parity is the selection rule of §4: the first-order perturbation $H_1=-p_2^2/96$ is a radial (even) multiplication operator, so it cannot connect the even sector to the odd sector, and the matrix $M_1$ block-diagonalises accordingly. The non-radial even state $\psi_6$ turns out to decouple from $H_1$ entirely except for its diagonal entry, as the explicit computation of §4 confirms; consequently the gap, through order $\beta^{-1/2}$, is carried by the four radial states alone, and the angular invariant $p_3$ re-enters only through the direct $H_2$ shift of §5.3.

The ground class state is $\psi_0$ (shell $0$). The first excited class state is the radial $\psi_1$ at shell $2$ — there is no shell-$1$ invariant — so the leading gap is $E^{(0)}_2-E^{(0)}_0=\omega(\beta)=\sqrt{2\beta/3}$, consistent with §2.6.

## 3.5 Remark: relation to generalized Hermite polynomials

The Weyl–Gaussian measure $\Delta_W^2\,e^{-\|\xi\|^2}=\prod_{\alpha>0}(\alpha\!\cdot\!\xi)^2\,e^{-\|\xi\|^2}$ (near the identity) is the Dunkl weight for the $A_2$ root system at multiplicity $k=1$, with one factor of $|\alpha\!\cdot\!\xi|^{2k}$ per positive root. The $W$-invariant orthogonal polynomials for this weight are the symmetric generalized (Dunkl–)Hermite polynomials of the $A_2$ system; the shell basis $\psi_0,\dots,\psi_6$ is their lowest-degree truncation, and the reduction of the radial channels to associated Laguerre polynomials $L_n^{(3)}$ is the standard radial form of these objects. We use only the explicit low-degree polynomials above, but this identification places the construction in a known orthogonal-polynomial family and indicates how the basis extends to higher shells and, via the analogous $A_{N-1}$ weight, to $\mathrm{SU}(N)$ (§8).

With the orthonormal shell basis and its sector structure established, §4 computes the matrix of the first-order perturbation $H_1$.


# 4. The matrix $M_1$ of $H_1$ in the shell basis

## 4.1 The matrix

The first-order perturbation $H_1=-p_2^2/96$ is a real multiplication operator, self-adjoint in the Weyl–Gaussian inner product, so its matrix $M_1$ in the orthonormal shell basis $\{\psi_0,\dots,\psi_6\}$ is real symmetric. Evaluating $\langle\psi_i,H_1\psi_j\rangle$ by direct integration against $\Delta_W^2\,e^{-x^2-y^2}\,dx\,dy$ and ordering the basis as $(\psi_0,\psi_1,\psi_2,\psi_3,\psi_4,\psi_5,\psi_6)$ gives
$$
M_1=-\begin{pmatrix}
\tfrac{5}{24} & \tfrac{5}{24} & 0 & \tfrac{\sqrt{10}}{48} & 0 & 0 & 0\\[4pt]
\tfrac{5}{24} & \tfrac{25}{48} & 0 & \tfrac{7\sqrt{10}}{48} & 0 & \tfrac{\sqrt5}{16} & 0\\[4pt]
0 & 0 & \tfrac{7}{12} & 0 & \tfrac{\sqrt7}{6} & 0 & 0\\[4pt]
\tfrac{\sqrt{10}}{48} & \tfrac{7\sqrt{10}}{48} & 0 & \tfrac{23}{24} & 0 & \tfrac{9\sqrt2}{16} & 0\\[4pt]
0 & 0 & \tfrac{\sqrt7}{6} & 0 & \tfrac{13}{12} & 0 & 0\\[4pt]
0 & \tfrac{\sqrt5}{16} & 0 & \tfrac{9\sqrt2}{16} & 0 & \tfrac{73}{48} & 0\\[4pt]
0 & 0 & 0 & 0 & 0 & 0 & \tfrac{55}{48}
\end{pmatrix}.
$$
The overall minus sign is the $-1/96$ convention; it is shown once here and restored throughout. Every entry has been verified by exact symbolic integration. The remainder of the section explains the pattern of zeros and nonzeros entirely from the sector structure of §3.4, so that none of it need be read off the matrix by inspection.

## 4.2 Parity block structure

$H_1$ multiplies by $p_2^2$, which is even under the Weyl reflection $y\mapsto-y$. Multiplication by an even function preserves parity, so $M_1$ has no entries connecting the even sector $\{\psi_0,\psi_1,\psi_3,\psi_5,\psi_6\}$ to the odd sector $\{\psi_2,\psi_4\}$. The matrix is therefore block-diagonal,
$$
M_1=M_1^{\text{even}}\oplus M_1^{\text{odd}},
$$
a $5\times5$ even block on $(\psi_0,\psi_1,\psi_3,\psi_5,\psi_6)$ and a $2\times2$ odd block on $(\psi_2,\psi_4)$. The odd block,
$$
M_1^{\text{odd}}=-\begin{pmatrix}\tfrac{7}{12} & \tfrac{\sqrt7}{6}\\[3pt]\tfrac{\sqrt7}{6} & \tfrac{13}{12}\end{pmatrix},
$$
is decoupled from the ground and first-excited states, which are even; the odd states therefore play no role in the gap (§5.2).

## 4.3 The radial tower as a banded Laguerre operator

Within the even sector the four radial states $\psi_0,\psi_1,\psi_3,\psi_5$ are the associated Laguerre polynomials $L_0^{(3)},L_1^{(3)},L_2^{(3)},L_3^{(3)}$ in $p_2$ (§3.3). On this tower, $H_1$ acts as multiplication by $-\tfrac1{96}p_2^2$, i.e. by $u^2$ in the Laguerre variable $u=p_2$. Because the Laguerre polynomials obey a three-term recurrence, multiplication by $u^2$ is a **band-$2$** (pentadiagonal) operator:
$$
\langle L_m^{(3)},u^2L_n^{(3)}\rangle=0
\qquad\text{whenever}\qquad
|m-n|>2 .
$$
The radial block of $M_1$ is therefore pentadiagonal, and its single off-band zero is the $(\psi_0,\psi_5)$ entry, corresponding to $|m-n|=3$ between $L_0^{(3)}$ and $L_3^{(3)}$:
$$
M_1^{\text{radial}}
=-\begin{pmatrix}
\tfrac{5}{24} & \tfrac{5}{24} & \tfrac{\sqrt{10}}{48} & 0\\[4pt]
\tfrac{5}{24} & \tfrac{25}{48} & \tfrac{7\sqrt{10}}{48} & \tfrac{\sqrt5}{16}\\[4pt]
\tfrac{\sqrt{10}}{48} & \tfrac{7\sqrt{10}}{48} & \tfrac{23}{24} & \tfrac{9\sqrt2}{16}\\[4pt]
0 & \tfrac{\sqrt5}{16} & \tfrac{9\sqrt2}{16} & \tfrac{73}{48}
\end{pmatrix}
\qquad(\psi_0,\psi_1,\psi_3,\psi_5).
$$
The vanishing of $M_1[\psi_0,\psi_5]$ is thus not an accident of the numbers but the band-$2$ selection rule of the Laguerre family; it is what restricts the ground-state resolvent of §5.2 to the two intermediate states $\psi_1,\psi_3$.

## 4.4 Decoupling of the non-radial state $\psi_6$

The non-radial even state $\psi_6$ connects to nothing under $H_1$ except itself. The reason is structural and exact: $\psi_6$ is orthogonal to **every** radial function — one checks $\langle\psi_6,p_2^m\rangle=0$ for all $m$, since its angular content (the $\cos 6\varphi$ harmonic) integrates to zero against the radial angular content under the measure $\Delta_W^2\propto1+\cos 6\varphi$. Multiplication by the radial function $p_2^2$ maps any radial state to a radial state, so
$$
\langle\psi_6,H_1\psi_j\rangle=-\tfrac1{96}\langle\psi_6,p_2^2\psi_j\rangle=0
\quad\text{for every radial }\psi_j\ (j=0,1,3,5),
$$
because $p_2^2\psi_j$ is again radial and $\psi_6$ is orthogonal to all radials. The couplings to the odd states $\psi_2,\psi_4$ vanish by parity (§4.2). Hence the only nonzero entry in the $\psi_6$ row and column is the diagonal one,
$$
\langle\psi_6,H_1\psi_6\rangle=-\tfrac{55}{48},
$$
and $\psi_6$ contributes to the gap only through the direct $H_2$ shift of §5.3, never through the first-order matrix or the resolvent.

## 4.5 The ledgers used downstream

The structure above isolates exactly which entries the gap computation needs.

For the first-order shift $c_0$ (§5), only the two diagonal entries of the ground and first-excited radial states are required:
$$
\langle\psi_0,H_1\psi_0\rangle=-\tfrac{5}{24},
\qquad
\langle\psi_1,H_1\psi_1\rangle=-\tfrac{25}{48}.
$$

For the second-order resolvent $\Delta_{\mathrm{res}}$ (§5.2), the band-$2$ rule fixes the participating couplings. The ground state $\psi_0$ ($L_0^{(3)}$) couples only to $\psi_1$ and $\psi_3$ ($L_1^{(3)},L_2^{(3)}$); the first excited state $\psi_1$ ($L_1^{(3)}$) couples to $\psi_0,\psi_3,\psi_5$ ($L_0^{(3)},L_2^{(3)},L_3^{(3)}$):
$$
\langle\psi_0,H_1\psi_1\rangle=-\tfrac{5}{24},
\quad
\langle\psi_0,H_1\psi_3\rangle=-\tfrac{\sqrt{10}}{48},
\quad
\langle\psi_1,H_1\psi_3\rangle=-\tfrac{7\sqrt{10}}{48},
\quad
\langle\psi_1,H_1\psi_5\rangle=-\tfrac{\sqrt5}{16}.
$$
All of these lie within the radial tower; the odd states ($\psi_2,\psi_4$) are excluded by parity and the non-radial state $\psi_6$ by §4.4. This is the precise sense in which the resolvent contribution to the gap is a radial quantity, and it is why the non-radial correction must enter elsewhere — through the single direct expectation of $p_3^2$ computed in §5.3. The coupling $\langle\psi_3,H_1\psi_5\rangle=-\tfrac{9\sqrt2}{16}$, though nonzero in $M_1$, connects two intermediate states and does not enter the second-order gap; it reappears only in the leakage matrix discussion of §6.


# 5. Computation of the gap law

This section assembles the three-term gap law from the data of §4. The computation has three inputs — a first-order shift, a second-order resolvent contribution, and a direct second-order shift — combined in §5.4 into the main theorem. Each quantity is exact and has been verified by symbolic integration against the Weyl–Gaussian measure; the parity and band-$2$ selection rules of §4 fix which matrix elements participate at every step.

## 5.1 First-order shift: $c_0=-\tfrac{5}{16}$

The order-$\beta^0$ term of the gap is the first-order Rayleigh–Schrödinger shift of $H_1=-p_2^2/96$, taken as the difference between the first excited class state $\psi_1$ and the ground state $\psi_0$. By §4.5 only two diagonal entries of $M_1$ are needed:
$$
c_0
=\langle\psi_1,H_1\psi_1\rangle-\langle\psi_0,H_1\psi_0\rangle
=-\tfrac{25}{48}-\Bigl(-\tfrac{5}{24}\Bigr)
=-\tfrac{25}{48}+\tfrac{10}{48}
=\boxed{-\tfrac{5}{16}}.
$$
Both states are radial and $H_1$ is radial, so $c_0$ is exactly the value of a one-dimensional radial reduction; it agrees with the radial strong-coupling computations of [Münster 1981; Drouffe–Zuber 1983]. The non-radial invariant $p_3$ plays no role at this order.

## 5.2 Second-order resolvent contribution: $\Delta_{\mathrm{res}}=-\tfrac{205\sqrt6}{3072}$

The second-order contribution to the energy of a class state $\psi_i$ is the resolvent sum
$$
E_i^{(2)}=\sum_{m\ne i}\frac{|\langle\psi_i,H_1\psi_m\rangle|^2}{E_i^{(0)}-E_m^{(0)}},
\qquad
E^{(0)}_s=\tfrac{\sqrt6}{6}\,s\,\beta^{1/2}+\text{const},
$$
with shells $s=(0,2,3,4,5,6,6)$ for $(\psi_0,\dots,\psi_6)$ as in §3. By the band-$2$ Laguerre rule of §4.3 and parity, the ground state $\psi_0$ couples only to $\psi_1,\psi_3$, and the first excited state $\psi_1$ couples only to $\psi_0,\psi_3,\psi_5$.

**Ground state.** With $\langle\psi_0,H_1\psi_1\rangle=-\tfrac5{24}$, $\langle\psi_0,H_1\psi_3\rangle=-\tfrac{\sqrt{10}}{48}$ and denominators $-\tfrac{\sqrt6}{3},-\tfrac{2\sqrt6}{3}$ (rescaled),
$$
E_0^{(2)}
=\frac{(5/24)^2}{-\sqrt6/3}+\frac{(\sqrt{10}/48)^2}{-2\sqrt6/3}
=-\tfrac{35\sqrt6}{1536}.
$$

**First excited state.** With $\langle\psi_1,H_1\psi_0\rangle=-\tfrac5{24}$, $\langle\psi_1,H_1\psi_3\rangle=-\tfrac{7\sqrt{10}}{48}$, $\langle\psi_1,H_1\psi_5\rangle=-\tfrac{\sqrt5}{16}$ and denominators $+\tfrac{\sqrt6}{3},-\tfrac{\sqrt6}{3},-\tfrac{2\sqrt6}{3}$,
$$
E_1^{(2)}
=\frac{(5/24)^2}{\sqrt6/3}+\frac{(7\sqrt{10}/48)^2}{-\sqrt6/3}+\frac{(\sqrt5/16)^2}{-2\sqrt6/3}
=-\tfrac{275\sqrt6}{3072}.
$$

**Resolvent gap.**
$$
\Delta_{\mathrm{res}}=E_1^{(2)}-E_0^{(2)}
=-\tfrac{275\sqrt6}{3072}+\tfrac{70\sqrt6}{3072}
=\boxed{-\tfrac{205\sqrt6}{3072}}.
$$
Every coupling here lies within the radial tower (§4.5); the odd states are excluded by parity and the non-radial $\psi_6$ by §4.4. Thus $\Delta_{\mathrm{res}}$, like $c_0$, is a radial quantity. The entire radial/non-radial discrepancy of the gap is therefore confined to the single direct term computed next.

## 5.3 Direct $H_2$ shift and the non-radial $p_3^2$ term: $\Delta_{H_2}=\tfrac{19\sqrt6}{576}$

The perturbation $H_2=\sqrt6\bigl(\tfrac{p_2^3}{11520}+\tfrac{p_3^2}{8640}\bigr)$ already carries a factor $\beta^{-1/2}$, so it contributes to the gap through its first-order shift, the diagonal difference $\langle\psi_1,H_2\psi_1\rangle-\langle\psi_0,H_2\psi_0\rangle$. The two summands split it into a radial and a non-radial part.

**Radial part.** From the moments $\langle\psi_0,p_2^3\psi_0\rangle=120$, $\langle\psi_1,p_2^3\psi_1\rangle=480$,
$$
\Delta_{H_2}^{\mathrm{rad}}=\tfrac{\sqrt6}{11520}(480-120)=\tfrac{\sqrt6}{32}=\tfrac{18\sqrt6}{576}.
$$

**Non-radial part.** From the moments $\langle\psi_0,p_3^2\psi_0\rangle=5$, $\langle\psi_1,p_3^2\psi_1\rangle=20$,
$$
\Delta_{H_2}^{p_3^2}=\tfrac{\sqrt6}{8640}(20-5)=\tfrac{\sqrt6}{576}\neq0.
$$
This is the first and only place where the non-radial invariant $p_3$ reaches the gap: even though $\psi_0,\psi_1$ are radial, the angular invariant $p_3^2$ has different expectations in them because the Weyl measure $\Delta_W^2=\tfrac{p_2^3}{2}-3p_3^2$ is itself non-radial (§2.4–2.5).

**Combined.**
$$
\Delta_{H_2}=\tfrac{18\sqrt6}{576}+\tfrac{\sqrt6}{576}=\boxed{\tfrac{19\sqrt6}{576}}.
$$

## 5.4 Assembly and the three-term gap law

The order-$\beta^{-1/2}$ coefficient combines the resolvent and direct contributions. Over the common denominator $9216=2^{10}\cdot3^2$,
$$
\Delta_{\mathrm{res}}=-\tfrac{615\sqrt6}{9216},
\qquad
\Delta_{H_2}=\tfrac{304\sqrt6}{9216},
\qquad
c_1=\Delta_{\mathrm{res}}+\Delta_{H_2}=-\tfrac{311\sqrt6}{9216}\approx-0.0827.
$$

> **Theorem 5.1 (Three-term SU(3) class-function gap law).**
> For the $\mathrm{SU}(3)$ one-plaquette class-function Hamiltonian $H_\beta=\tfrac12 C_2+\beta(1-\tfrac13\Re\chi_{(1,0)})$ under the canonical Weyl–Gaussian inner product, as $\beta\to\infty$,
> $$
> \boxed{\;
> \Delta_{\mathrm{SU}(3)}(\beta)
> =\sqrt{\tfrac{2\beta}{3}}-\tfrac{5}{16}-\tfrac{311\sqrt6}{9216}\,\beta^{-1/2}+O(\beta^{-1}).
> \;}
> $$

*Proof.* The leading term is the gap of $H_0$ (§2.6); the order-$\beta^0$ term is $c_0=-\tfrac5{16}$ (§5.1); the order-$\beta^{-1/2}$ term is $c_1=\Delta_{\mathrm{res}}+\Delta_{H_2}=-\tfrac{311\sqrt6}{9216}$ by §5.2–5.3. All matrix elements, energies, and moments were evaluated exactly against the Weyl–Gaussian measure. $\qquad\blacksquare$

**The radial value and the size of the correction.** A radial-only reduction reproduces $\omega(\beta)$, $c_0$, and $\Delta_{\mathrm{res}}$ exactly (§5.1–5.2) but replaces $\Delta_{H_2}$ by its radial part $\tfrac{\sqrt6}{32}=\tfrac{288\sqrt6}{9216}$, giving
$$
c_1^{\,\mathrm{radial}}=-\tfrac{615\sqrt6}{9216}+\tfrac{288\sqrt6}{9216}=-\tfrac{327\sqrt6}{9216},
\qquad
c_1-c_1^{\,\mathrm{radial}}=\tfrac{16\sqrt6}{9216}=\tfrac{\sqrt6}{576}.
$$
Numerically $c_1\approx-0.0827$ against $c_1^{\,\mathrm{radial}}\approx-0.0869$, about a $5\%$ change in the third coefficient. The discrepancy is exactly $\tfrac{\sqrt6}{576}$ — rational times $\sqrt6$, unambiguous, and checkable — and it is the entire difference between the genuine rank-two gap and its radial approximation. This is the paper's central computational claim.

**Status.** Theorem 5.1 is unconditional within its scope: an asymptotic statement about the one-plaquette class spectrum under the canonical inner product, with error $O(\beta^{-1})$. It is not a statement about the four-dimensional theory, the infinite-volume limit, or the continuum limit. The same first-order data are repackaged in §6 as a finite leakage matrix, whose Perron root governs the conditional polymer-resolvent threshold of §7.


# 6. The finite-channel leakage matrix and its Perron root

## 6.1 Construction

The second-order gap computation of §5.2 is driven by a small, fixed set of first-order leakage amplitudes: the couplings of the two gap states $\psi_0,\psi_1$ to one another and to the resolvent channels $\psi_3,\psi_5$. We isolate exactly those amplitudes — the ones that appear in $E_0^{(2)}$ and $E_1^{(2)}$ — into a finite, nonnegative, symmetric *leakage matrix* on the four radial states $\{\psi_0,\psi_1,\psi_3,\psi_5\}=\{L_0^{(3)},L_1^{(3)},L_2^{(3)},L_3^{(3)}\}$ that they connect:
$$
T^{(3)}_{ab}=\bigl|\langle\psi_a,H_1\psi_b\rangle\bigr|\ \text{ for the gap-resolvent couplings},
\qquad
T^{(3)}_{aa}=0 .
$$
Ordering the states as $(\psi_0,\psi_1,\psi_3,\psi_5)$, the nonzero couplings are those entering §5.2 —
$$
|\langle\psi_0,H_1\psi_1\rangle|=\tfrac{5}{24},\quad
|\langle\psi_0,H_1\psi_3\rangle|=\tfrac{\sqrt{10}}{48},\quad
|\langle\psi_1,H_1\psi_3\rangle|=\tfrac{7\sqrt{10}}{48},\quad
|\langle\psi_1,H_1\psi_5\rangle|=\tfrac{\sqrt5}{16}
$$
— so that
$$
T^{(3)}
=\begin{pmatrix}
0 & \tfrac{5}{24} & \tfrac{\sqrt{10}}{48} & 0\\[4pt]
\tfrac{5}{24} & 0 & \tfrac{7\sqrt{10}}{48} & \tfrac{\sqrt5}{16}\\[4pt]
\tfrac{\sqrt{10}}{48} & \tfrac{7\sqrt{10}}{48} & 0 & 0\\[4pt]
0 & \tfrac{\sqrt5}{16} & 0 & 0
\end{pmatrix}.
$$
Two entries of the radial block of $M_1$ are deliberately excluded. The diagonal entries are dropped because the leakage matrix records inter-channel transfer, not on-channel energy. The coupling $\langle\psi_3,H_1\psi_5\rangle=-\tfrac{9\sqrt2}{16}$, although nonzero in $M_1$, connects two *intermediate* states and does not enter the second-order gap (§4.5); it would first contribute at third order. Thus $T^{(3)}$ is exactly the finite-channel object that governs the gap-resolvent leakage — neither more nor less. Its sparsity pattern is the band-$2$ Laguerre structure of §4.3 with the two gap states $\psi_0,\psi_1$ as sources: $\psi_5$ couples only to $\psi_1$, and the corner $(\psi_0,\psi_5)$ vanishes.

## 6.2 The Perron quartic and the trace identities

$T^{(3)}$ is nonnegative and irreducible on the connected channel graph $\psi_5-\psi_1-\{\psi_0,\psi_3\}$, so by the Perron–Frobenius theorem it has a simple, positive largest eigenvalue $\rho_3$. Its characteristic polynomial is the explicit quartic
$$
\boxed{\;
\lambda^4-\tfrac{215}{768}\lambda^2-\tfrac{175}{13824}\lambda+\tfrac{25}{294912}=0 .
\;}
$$
The coefficients are the elementary symmetric functions of the four eigenvalues and are fixed by the power-sum traces of $T^{(3)}$ through Newton's identities:
$$
\operatorname{tr}T^{(3)}=0,
\qquad
\operatorname{tr}\bigl(T^{(3)}\bigr)^2=\tfrac{215}{384},
\qquad
\operatorname{tr}\bigl(T^{(3)}\bigr)^3=\tfrac{175}{4608},
\qquad
\operatorname{tr}\bigl(T^{(3)}\bigr)^4=\tfrac{5125}{32768}.
$$
The vanishing trace removes the $\lambda^3$ term; the second trace gives the $\lambda^2$ coefficient $-\tfrac12\operatorname{tr}(T^{(3)})^2=-\tfrac{215}{768}$; the third trace gives the linear coefficient $-\tfrac13\operatorname{tr}(T^{(3)})^3=-\tfrac{175}{13824}$; and the quartic invariant fixes the constant $\tfrac{25}{294912}$. The presence of the linear term — equivalently the nonzero $\operatorname{tr}(T^{(3)})^3$ — is what makes the spectrum asymmetric about the origin; it arises from the single odd cycle $\psi_0-\psi_1-\psi_3-\psi_0$ in the channel graph.

## 6.3 The Perron root and the spectrum

The four eigenvalues of $T^{(3)}$ are
$$
\{\,-0.504502,\ -0.051580,\ 0.005921,\ 0.550162\,\},
$$
so the Perron root is
$$
\boxed{\;\rho_3=0.5501615335231425806844\ldots\;}
$$
It is simple and strictly dominant: the next-largest eigenvalue in magnitude is $0.5045$, so $\rho_3$ is the spectral radius with a modest spectral gap of about $0.046$. Two elementary two-sided bounds confirm the value without solving the quartic. The row sums of $T^{(3)}$ are $0.274,\,0.809,\,0.527,\,0.140$, giving the Perron–Frobenius row-sum sandwich $0.140\le\rho_3\le0.809$. The Frobenius norm gives the sharper bound
$$
\sqrt{\tfrac14\operatorname{tr}(T^{(3)})^2}\le\rho_3\le\sqrt{\operatorname{tr}(T^{(3)})^2},
\qquad\text{i.e.}\qquad
0.374\le\rho_3\le0.748,
$$
since $\rho_3^2$ is the largest of four nonnegative squares summing to $\operatorname{tr}(T^{(3)})^2=\tfrac{215}{384}$. The computed value $0.5502$ sits inside both intervals.

The (L¹-normalised, positive) Perron eigenvector is
$$
v_{\rho_3}\propto(0.184,\ 0.379,\ 0.340,\ 0.096)\quad\text{on }(\psi_0,\psi_1,\psi_3,\psi_5).
$$
The leakage is carried mainly by the first excited state $\psi_1$ and its strongest neighbour $\psi_3$ (the largest off-diagonal entry is $\langle\psi_1,H_1\psi_3\rangle=\tfrac{7\sqrt{10}}{48}$), with smaller weight on the ground state $\psi_0$ and the highest channel $\psi_5$. This is the channel structure that the multi-plaquette expansion of §7 inherits.

## 6.4 Interpretation

$\rho_3$ is the contraction constant of the finite-channel resolvent truncation: it measures how strongly the gap states leak, through $H_1$, into the active resolvent channels, normalised against the unperturbed shell spacing. In the single-plaquette problem this leakage is already accounted for exactly by the resolvent sum of §5.2; the role of $\rho_3$ is to provide the per-step amplitude for the *multi-plaquette* expansion of §7, where the same local leakage recurs at every plaquette and must be resummed. In this sense $\rho_3$ plays the part of a Cheeger-type constant for the class-channel graph — the local amplitude whose powers control the convergence of the polymer resolvent. We emphasise that everything in this section is unconditional: $T^{(3)}$ and $\rho_3$ are exact consequences of the first-order matrix $M_1$. The conditional content begins only when $\rho_3$ is fed into the multi-plaquette expansion in §7.


# 7. Finite-channel polymer-resolvent threshold and full-channel obstruction

## 7.1 Setup and status

Everything in §§2--6 is an unconditional statement about the one-plaquette class Hamiltonian and the finite leakage matrix $T^{(3)}$. This section records what that finite leakage matrix implies if the four-channel subspace
$$
F_3=\{\psi_0,\psi_1,\psi_3,\psi_5\}
$$
is treated as the active local class sector in a polymer-resolvent expansion.

The result is a finite-channel threshold. It is not a proof that the full class-channel expansion is controlled by $\rho_3$. The obstruction is structural: in the infinite radial Laguerre tower, multiplication by $H_1=-u^2/96$ has off-diagonal matrix elements growing quadratically with shell index, while the one-step class resolvent supplies only one shell denominator. Thus the high-channel tail is not a compact perturbation of the four-channel matrix unless an additional smoothing mechanism is proved.

Accordingly, the threshold below should be read as
$$
\boxed{\text{finite-channel diagnostic, not full-channel truncation theorem}.}
$$

## 7.2 Finite-channel per-step factor

Within $F_3$, the local off-diagonal class leakage is represented by $T^{(3)}$. Its Perron root is
$$
\rho_3=0.5501615335231425806844\ldots.
$$
The unperturbed shell spacing between the ground and first excited class shell is
$$
\omega(\beta)=\sqrt{\frac{2\beta}{3}}.
$$
Thus, if the expansion is restricted to $F_3$, each local class-resolvent step carries the dimensionless degradation factor
$$
\delta_3(\beta)=\frac{\rho_3}{\omega(\beta)}=\rho_3\sqrt{\frac{3}{2\beta}}.
$$

Let $\mu_{\mathcal G}$ denote the connective growth constant of the plaquette-overlap graph relevant to the polymer expansion. The elementary finite-channel summability criterion is
$$
\mu_{\mathcal G}\delta_3(\beta)<1,
$$
or equivalently
$$
\boxed{\beta>\frac32\,\mu_{\mathcal G}^2\rho_3^2.}
$$
At $\mu_{\mathcal G}=3$, this gives
$$
\beta>\frac32\cdot 9\cdot \rho_3^2\approx 4.09.
$$

## 7.3 Schur/Poincaré finite-channel threshold

For a polymer kernel with exponential decay in cluster diameter, the finite-channel criterion is strengthened by the Schur/Poincaré weighting. In this form the overlap growth enters quadratically, giving
$$
\boxed{\beta>\frac32\,\mu_{\mathcal G}^4\rho_3^2.}
$$
At $\mu_{\mathcal G}=3$,
$$
\beta>\frac32\cdot 81\cdot (0.5501615335\ldots)^2
\approx \boxed{36.78}.
$$
Thus, in the isolated four-channel model, the class polymer kernel is summable with an exponentially weighted Schur bound above this threshold, subject to the usual polymer-convergence hypotheses and the chosen overlap constant.

## 7.4 Why the finite-channel threshold does not control the full radial tail

Let $e_n$ denote the radial basis state corresponding to $L_n^{(3)}(u)$, with shell $s=2n$. The unperturbed energy above the ground grows linearly,
$$
D_n\sim \kappa n,
\qquad
\kappa=\frac{\sqrt6}{3}.
$$
On this tower, $H_1=-u^2/96$ is band-$2$, but its off-diagonal coefficients grow quadratically. The exact Laguerre recurrence gives the large-$n$ asymptotics
$$
|\langle e_{n+1},H_1e_n\rangle|\sim \frac{n^2}{24},
\qquad
|\langle e_{n+2},H_1e_n\rangle|\sim \frac{n^2}{96}.
$$
Thus
$$
|H_{1,\mathrm{off}}|_{mn}\sim Cn^2
\qquad(m=n+O(1)).
$$

Define the symmetrically weighted transfer family
$$
K_p=D^{-p}|H_{1,\mathrm{off}}|D^{-p}.
$$
Then
$$
(K_p)_{mn}\sim Cn^{2-2p}.
$$

The actual one-resolvent polymer step supplies one total denominator. In symmetric notation this corresponds to $p=1/2$, hence
$$
(K_{1/2})_{mn}\sim Cn,
$$
which is unbounded.

A Schur/Poincaré symmetrisation supplies one denominator on each side, $p=1$, hence
$$
(K_1)_{mn}\sim C.
$$
This is bounded at the coefficient level, but it does not decay in the tail. Indeed the asymptotic off-diagonal row-sum contribution is
$$
2\cdot\frac{n^2/24}{(\kappa n)^2}
+
2\cdot\frac{n^2/96}{(\kappa n)^2}
=
\frac{5}{48}\kappa^{-2}.
$$
Since $\kappa^2=2/3$, the limit is
$$
\frac{5}{48}\cdot\frac32=\frac5{32}.
$$
Therefore the $p=1$ tail is bounded but not compact.

For the high-shell tail to vanish by this mechanism, one needs
$$
2-2p<0,
\qquad\text{i.e.}\qquad
\boxed{p>1.}
$$
Such a gain is not supplied by the present finite-channel class-resolvent step.

Consequently, an estimate of the form
$$
\tilde\rho_3=\rho_3+\varepsilon_{\mathrm{tail}},
\qquad
\varepsilon_{\mathrm{tail}}\to0,
$$
does not follow from the current argument.

## 7.5 Correct full-channel alternatives

A full-channel theorem requires one of the following additional inputs.

First, prove a stronger local smoothing estimate giving more than one denominator per side, i.e. an effective $p>1$ bound for the relevant polymer step.

Second, work in a different weighted norm where the $n^2$ growth of $H_1=-u^2/96$ is absorbed by the Gaussian or factorial shell weights of the Laguerre system.

Third, prove a finite analytic cutoff theorem showing that high shells are not activated in the relevant polymer channel. This must be stronger than the band-$2$ selection rule, since repeated band-$2$ moves eventually reach arbitrarily high shells.

Fourth, abandon the perturbative-tail form $\rho_3+\varepsilon_{\mathrm{tail}}$ and define a genuine full radial transfer constant
$$
\rho_{\mathrm{full}}=r(K_{\mathrm{full}}),
$$
where $K_{\mathrm{full}}$ is the appropriate infinite Laguerre transfer operator in the norm used by the polymer expansion. The finite-channel threshold would then be replaced by a full-channel threshold of schematic form
$$
\boxed{\beta>\frac32\,\mu_{\mathcal G}^4\rho_{\mathrm{full}}^2}
$$
provided $\rho_{\mathrm{full}}$ is finite in that norm.

## 7.6 Casimir-shell replacement

The oscillator-shell obstruction suggests using the exact compact-group Peter--Weyl/Casimir shell instead. Let $G=\mathrm{SU}(N)$ and let $L^2_{\mathrm{cl}}(G)$ have class-character basis $\{\chi_\lambda\}_{\lambda\in P_+}$. The quadratic Casimir obeys
$$
C_2(\lambda)\ge c_N|\lambda|^2-C_N.
$$
For
$$
H_\beta=\frac12\mathcal C+\beta V,
\qquad
V(U)=1-\frac1N\Re\operatorname{Tr}U,
$$
with $0\le V\le2$, the high-Casimir denominator is quadratic. A manuscript-safe target estimate is
$$
\boxed{
\left\|\Pi_{>R}(H_\beta-E)^{-1}\Pi_{>R}\right\|
\le
\frac{C_{N,\beta,E}}{R^2}
}
$$
once $R^2$ dominates $\beta+|E|$ and the finite coupling buffer has been absorbed into the low block.

Multiplication by a fundamental character moves Peter--Weyl labels by a finite step set:
$$
\chi_\lambda\chi_{\mathrm{fund}}
=
\sum_{\lambda'\in\lambda+\mathcal S_N}
N^{\lambda'}_{\lambda,\mathrm{fund}}\chi_{\lambda'}.
$$
This gives a cleaner high-shell geometry than the local oscillator Laguerre tail, but the finite-buffer and Schur-complement details still have to be written.


# 8. The $\mathrm{SU}(N)$ local class extension

## 8.1 General finite-rank procedure

For $\mathrm{SU}(N)$ the Cartan plane is $(N-1)$-dimensional and the Weyl group is $S_N$. The class algebra near the identity is generated by the basic Weyl invariants
$$
p_2,p_3,\ldots,p_N,
$$
and the squared Weyl discriminant $\Delta_W^2$ gives the class inner product
$$
\langle f,g\rangle
=
\int_{\mathbb R^{N-1}} f g\,\Delta_W^2 e^{-\|\xi\|^2}\,d\xi.
$$

For each fixed $N$, the local computation through degree six is finite:

1. Expand
$$
H_\beta=\beta^{1/2}H_0+H_1+\beta^{-1/2}H_2+O(\beta^{-1}).
$$
2. Generate the shell-graded Weyl-invariant monomial basis through degree six.
3. Orthonormalise against the Weyl--Gaussian measure.
4. Compute the matrix of $H_1$ and the diagonal shifts from $H_2$.
5. Extract
$$
c_0^{(N)},\qquad \Delta_{\mathrm{res}}^{(N)},\qquad \Delta_{H_2}^{(N)},\qquad c_1^{(N)}.
$$
6. Construct the reduced source-leakage matrix and its Perron root $\rho_N^{\mathrm{red}}$.

## 8.2 Normalisation warning for $H_1$

The notation
$$
H_1=-P_4/48
$$
is safe only if $P_4$ is explicitly defined in the script convention. If instead
$$
P_4=p_4=\sum_i\phi_i^4,
$$
then the convention corresponding to the $\mathrm{SU}(4)$ script is
$$
H_1=-P_4/96.
$$
The manuscript should not write $H_1=-P_4/48$ unless the definition of $P_4$ is fixed at the same time.

## 8.3 Corrected first-order coefficient

The corrected candidate for the first-order local class gap coefficient is
$$
\boxed{
c_0^{(N)}=-\frac{2N^2-3}{16N}
=-\frac N8+\frac{3}{16N}.
}
$$
It matches the computed local rows:
$$
N=3:\quad -\frac{18-3}{48}=-\frac5{16},
$$
$$
N=4:\quad -\frac{32-3}{64}=-\frac{29}{64},
$$
$$
N=5:\quad -\frac{50-3}{80}=-\frac{47}{80},
$$
$$
N=6:\quad -\frac{72-3}{96}=-\frac{23}{32}.
$$
The earlier candidate $-(N^2+N-2)/(16N)$ is rejected because it gives $-5/24$ at $N=3$ rather than $-5/16$.

## 8.4 Numerical local ledgers through $N=6$

The current local ledgers are:

| $N$ | $\omega_N/\sqrt\beta$ | $c_0^{(N)}$ | $\Delta_{\mathrm{res}}^{(N)}$ | $\Delta_{H_2}^{(N)}$ | $c_1^{(N)}$ | reduced leakage |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | $0.816496580927726$ | $-0.312500000000000$ | $-0.163458788174008$ | $0.080799140820973$ | $-0.082659647353035$ | $0.550161533523143$ |
| 4 | $0.707106781186548$ | $-0.453125000000000$ | $-0.400221977795616$ | $0.194270222435366$ | $-0.205951755360250$ | $0.959702818730095$ |
| 5 | $0.632455532033676$ | $-0.587500000000001$ | $-0.758493708046377$ | $0.364320738765233$ | $-0.394172969281145$ | $1.466426457153154$ |
| 6 | $0.577350269189626$ | $-0.718749999999970$ | $-1.250267794851559$ | $0.596895981427813$ | $-0.653371813423746$ | $2.073397614578208$ |

For $N=4$, this gives
$$
\Delta_{\mathrm{SU}(4)}(\beta)
=
\sqrt{\frac\beta2}
-\frac{29}{64}
-0.205951755360250\,\beta^{-1/2}
+O(\beta^{-1}),
$$
with
$$
\rho_4^{\mathrm{red}}=0.959702818730095.
$$

The $N=5$ and $N=6$ rows are numerical finite-rank ledgers, not yet symbolic manuscript theorems.

## 8.5 Degree-six saturation of the reduced source leakage

The reduced leakage diagnostic is saturated at degree six. The source shells are
$$
s_0=0,\qquad s_1=2,
$$
and the perturbation $H_1$ has degree four. Therefore direct leakage from the two source states can reach only
$$
0+4=4,
\qquad
2+4=6.
$$
Extending the invariant basis above degree six cannot change the reduced source-leakage matrix constructed from direct edges incident to the source states.

The correct interpretation is
$$
\boxed{
\rho_N^{\mathrm{red}}\text{ is a sharp finite source-leakage diagnostic, not a full-channel polymer constant.}
}
$$
Further degree extension of the reduced diagnostic does not solve the full-channel tail. The correct full-channel target is a genuine full transfer norm or a Casimir-shell/Peter--Weyl replacement.

## 8.6 Radial Weyl--Vandermonde conjugation

Let
$$
H=\{\theta=(\theta_1,\ldots,\theta_N)\in\mathbb R^N:\sum_i\theta_i=0\}
$$
be the $A_{N-1}$ Cartan hyperplane. Write $r=\|\theta\|$ and
$$
\Delta_W(\theta)=\prod_{1\le i<j\le N}(\theta_i-\theta_j).
$$
The Vandermonde is homogeneous of degree
$$
M=\frac{N(N-1)}2
$$
and harmonic on $H$. Since $\dim H=N-1$, radial conjugation by $\Delta_W$ gives
$$
\Delta_W^{-1}\Delta_H\Delta_W f
=
f''(r)+\frac{2M+N-2}{r}f'(r)
=
f''(r)+\frac{N^2-2}{r}f'(r).
$$
With $u=r^2$,
$$
f_r=2rf_u,
\qquad
f_{rr}=4u f_{uu}+2f_u,
$$
so
$$
\Delta_W^{-1}\Delta_H\Delta_W f
=
4u f_{uu}+2(N^2-1)f_u.
$$
After division by $4$, the radial Laguerre parameter is
$$
\boxed{\alpha_N=\frac{N^2-3}{2}.}
$$
For $N=3$, $\alpha_3=3$, and the radial Weyl--Gaussian measure is
$$u^3e^{-u}\,du,
$$
so the radial tower is $L_n^{(3)}(u)$, exactly as used in the $\mathrm{SU}(3)$ computation.


# 9. Corrected Wilson projected-capacity route

## 9.1 Global fixed-window top-norm no-go theorem

The global fixed-window projected-capacity theorem
$$
\|P_{\Lambda,L}\mathbf 1_{D_L}P_{\Lambda,L}\|\le c<1
$$
uniformly in $L$, at fixed nonzero spectral window $\Lambda>0$ and fixed positive defect density $q>0$, is false.

Let $D_L$ be a Bernoulli defect set with density $q>0$, and let $P_{\Lambda,L}$ project onto a fixed nonzero Fourier/Hodge spectral window. Then
$$
\boxed{
\|P_{\Lambda,L}\mathbf 1_{D_L}P_{\Lambda,L}\|\longrightarrow 1
}
$$
in probability along $L\to\infty$.

Proof spine. Fix $t<1$ and choose a cube $Q_R$ with $R\gg\Lambda^{-1/2}$. A smooth bump of scale $R$, projected into the spectral window, produces a normalized vector
$$
f_R\in\operatorname{Ran}P_{\Lambda,L}
$$
with
$$
\langle f_R,\mathbf 1_{Q_R}f_R\rangle\ge t.
$$
For fixed $R$, the probability that a given $R$-cube is fully defective is
$$
p_R=q^{cR^4}>0.
$$
There are order $(L/R)^4$ disjoint $R$-cubes, so with probability tending to one at least one such cube is fully defective. On that event,
$$
\mathbf 1_{D_L}\ge\mathbf 1_{Q_R},
$$
and therefore
$$
\|P_{\Lambda,L}\mathbf 1_{D_L}P_{\Lambda,L}\|
\ge
\langle f_R,\mathbf 1_{D_L}f_R\rangle
\ge t.
$$
Since $t<1$ was arbitrary, the norm tends to one in probability.

The infinite-volume theorem cannot therefore be a global top-norm firewall theorem at fixed $\beta$, fixed threshold, and fixed $\Lambda>0$.

## 9.2 Rooted projected-capacity polymer replacement

The correct object is rooted. Large rare islands exist globally; what must be controlled is the bad island containing a fixed root.

Let
$$
X_p(U)=\mathbf 1\{V(U_p)\ge\delta\}
$$
be a hard plaquette-defect indicator. For a finite connected plaquette animal $\Gamma\subset\mathcal P_L$, define
$$
X_\Gamma=\prod_{p\in\Gamma}X_p.
$$
Let projected plaquette atoms be
$$
A_p=P_{\Lambda,L}\mathbf 1_{\partial p}P_{\Lambda,L},
$$
and define
$$
\Theta(\Gamma)
=
\gamma\left\|\sum_{p\in\Gamma}A_p\right\|_{\mathrm{op}}.
$$
Since $0\preceq A_p\preceq I$,
$$
\Theta(\Gamma)\le\gamma|\Gamma|.
$$

Assume the Wilson Peierls input
$$
\boxed{
\mathbb P_\beta(X_\Gamma=1)\le z_\beta^{|\Gamma|}
}
$$
for every finite connected plaquette animal $\Gamma$. Let $\mu_{\mathcal P}$ be the plaquette-animal counting constant:
$$
\#\{\Gamma\ni p_0:|\Gamma|=n\}\le\mu_{\mathcal P}^n.
$$
Then
$$
\sum_{\Gamma\ni p_0}
e^{a|\Gamma|}\mathbb E_\beta\left[X_\Gamma e^{s\Theta(\Gamma)}\right]
\le
\sum_{n\ge1}
\left(\mu_{\mathcal P}z_\beta e^{a+s\gamma}\right)^n.
$$
Therefore, if
$$
\boxed{
\mu_{\mathcal P}z_\beta e^{a+s\gamma}<1,
}
$$
then
$$
\boxed{
\sum_{\Gamma\ni p_0}
e^{a|\Gamma|}\mathbb E_\beta\left[X_\Gamma e^{s\Theta(\Gamma)}\right]
\le
\frac{\mu_{\mathcal P}z_\beta e^{a+s\gamma}}
{1-\mu_{\mathcal P}z_\beta e^{a+s\gamma}}.
}
$$
This is the correct rooted polymer summability theorem, conditional on the Wilson Peierls input.

## 9.3 Correct source-tilting identity

For $V_p(U)\ge0$ and $X_p=\mathbf 1\{V_p\ge\delta\}$,
$$
X_\Gamma
\le
\exp\left(-t\delta|\Gamma|+t\sum_{p\in\Gamma}V_p\right).
$$
Therefore
$$
\mathbb P_\beta(X_\Gamma=1)
\le
e^{-t\delta|\Gamma|}
\mathbb E_\beta\exp\left(t\sum_{p\in\Gamma}V_p\right).
$$

The moment-generating identity is
$$
\boxed{
\mathbb E_\beta\exp\left(t\sum_{p\in\Gamma}V_p\right)
=
\frac{Z(\beta-t\mathbf 1_\Gamma)}{Z(\beta)}.
}
$$
Indeed,
$$
\mathbb E_\beta e^{t\sum_\Gamma V_p}
=
\frac1{Z(\beta)}
\int e^{t\sum_\Gamma V_p}e^{-\beta\sum_pV_p}\,dU
=
\frac{Z(\beta-t\mathbf 1_\Gamma)}{Z(\beta)}.
$$
It is not $Z(\beta)/Z(\beta-t\mathbf 1_\Gamma)$.

## 9.4 Inhomogeneous Wilson free-energy target

The exact theorem target is
$$
\boxed{
\frac{Z(\beta-t\mathbf 1_\Gamma)}{Z(\beta)}
\le e^{C_0(t,\beta)|\Gamma|}
}
$$
with
$$
\boxed{
t\delta-C_0(t,\beta)
>
\log\mu_{\mathcal P}+a+s\gamma.
}
$$

Equivalently choose
$$
t=(1-\alpha)\beta,
\qquad 0<\alpha<1.
$$
Then
$$
Z_{\beta,\alpha,\Gamma}
=Z(\beta-(1-\alpha)\beta\mathbf 1_\Gamma),
$$
which is the partition function with coupling $\alpha\beta$ on $\Gamma$ and $\beta$ off $\Gamma$.

If
$$
\boxed{
\frac{Z_{\beta,\alpha,\Gamma}}{Z_\beta}\le K_\alpha^{|\Gamma|},
}
$$
then
$$
\mathbb P_\beta(X_\Gamma=1)
\le
\left[K_\alpha e^{-(1-\alpha)\beta\delta}\right]^{|\Gamma|}.
$$
Define
$$
\boxed{
z_{\beta,\delta,\alpha}
=
K_\alpha e^{-(1-\alpha)\beta\delta}.
}
$$
The rooted projected-capacity condition becomes
$$
\boxed{
\mu_{\mathcal P}K_\alpha
\exp\left[-(1-\alpha)\beta\delta+a+s\gamma\right]<1.
}
$$
Equivalently,
$$
\boxed{
\beta>
\frac{\log\mu_{\mathcal P}+\log K_\alpha+a+s\gamma}
{(1-\alpha)\delta}.
}
$$
For $\alpha=1/2$,
$$
\boxed{
\beta>
\frac2\delta
\left(\log\mu_{\mathcal P}+\log K_{1/2}+a+s\gamma\right).
}
$$

## 9.5 Wilson-to-Bernoulli square-free domination

If the Peierls/moment bound holds for all finite plaquette sets $Y$,
$$
\mathbb E_\beta\prod_{p\in Y}X_p\le z^{|Y|},
$$
and if $B_p$ are independent Bernoulli variables with $\mathbb P(B_p=1)=z$, then
$$
\mathbb E_R\prod_{p\in Y}B_p=z^{|Y|}.
$$
Therefore
$$
\boxed{
\mathbb E_\beta\prod_{p\in Y}X_p
\le
\mathbb E_R\prod_{p\in Y}B_p.
}
$$
Consequently, for every nonnegative square-free plaquette polynomial
$$
\mathcal F(X)=\sum_Y c_Y\prod_{p\in Y}X_p,
\qquad c_Y\ge0,
$$
one gets
$$
\boxed{
\mathbb E_\beta\mathcal F(X)
\le
\mathbb E_R\mathcal F(B).
}
$$

For positive closed-walk trace weights
$$
\mathcal W_m(X)=
\sum_{p_1,\ldots,p_m}
w(p_1,\ldots,p_m)\prod_{j=1}^m X_{p_j},
\qquad w\ge0,
$$
collapse multiplicities to $Y=\{p_1,\ldots,p_m\}$. Since $X_p^k=X_p$,
$$
\prod_{j=1}^mX_{p_j}=\prod_{p\in Y}X_p,
$$
and square-free domination gives
$$
\boxed{
\mathbb E_\beta\mathcal W_m(X)
\le
\mathbb E_{\mathrm{Bern}(z)}\mathcal W_m(B).
}
$$
This is the HPM transfer in the polymer sense.

## 9.6 Corrected route

The retired target is
$$
\boxed{
\|P_{\Lambda,L}\mathbf 1_D P_{\Lambda,L}\|<c<1
\quad\text{uniformly in }L.
}
$$
The corrected route is
$$
\text{inhomogeneous Wilson free-energy stability}
\Longrightarrow
\text{hard-defect plaquette-animal Peierls bound}
\Longrightarrow
\text{Wilson-to-Bernoulli square-free domination}
\Longrightarrow
\text{closed-walk HPM transfer}
\Longrightarrow
\text{rooted projected-capacity polymer summability}
\Longrightarrow
\text{patched coercivity / clustering expansion}.
$$
The exact remaining analytic input is
$$
\boxed{
\frac{Z_{\beta,\alpha,\Gamma}}{Z_\beta}
\le
K_\alpha^{|\Gamma|}
\quad\text{uniformly in }L,\Gamma.
}
$$


# 10. Conclusions and next analytic targets

## 10.1 Proved local content

The local $\mathrm{SU}(3)$ theorem is the strongest established result in this merged draft:
$$
\Delta_{\mathrm{SU}(3)}(\beta)
=
\sqrt{\frac{2\beta}{3}}
-\frac5{16}
-\frac{311\sqrt6}{9216}\beta^{-1/2}
+O(\beta^{-1}).
$$
The coefficient at order $\beta^{-1/2}$ is genuinely rank-two; a radial reduction misses exactly $\sqrt6/576$. The finite leakage matrix has exact Perron root
$$
\rho_3=0.5501615335231425806844\ldots.
$$

## 10.2 Conditional finite-channel content

The finite-channel polymer-resolvent threshold is
$$
\beta>\frac32\mu_{\mathcal G}^4\rho_3^2,
$$
which gives $\beta>36.78$ at $\mu_{\mathcal G}=3$. It is a diagnostic for the isolated four-channel model. It does not control the infinite radial tail without additional smoothing or a replacement full-channel transfer theorem.

## 10.3 Corrected global route

The global fixed-window top-norm projected-capacity theorem is false at fixed positive defect density. The correct replacement is a rooted projected-capacity polymer theorem controlled by a Wilson Peierls/free-energy stability input. The source-tilted identity fixes the sign and ratio:
$$
\mathbb E_\beta e^{t\sum_\Gamma V_p}
=
\frac{Z(\beta-t\mathbf 1_\Gamma)}{Z(\beta)}.
$$
The missing theorem is
$$
\frac{Z_{\beta,\alpha,\Gamma}}{Z_\beta}
\le K_\alpha^{|\Gamma|}
$$
with constants strong enough that
$$
\mu_{\mathcal P}K_\alpha
\exp[-(1-\alpha)\beta\delta+a+s\gamma]<1.
$$

## 10.4 Immediate work items

1. Replace any occurrence of the inverted source-tilt ratio by
$$
Z(\beta-t\mathbf 1_\Gamma)/Z(\beta).
$$
2. Demote any global fixed-window top-norm firewall statement; replace it with rooted projected-capacity polymer summability.
3. Write the inhomogeneous Wilson free-energy stability lemma as the next load-bearing analytic input.
4. Keep $\rho_N^{\mathrm{red}}$ labelled as a reduced finite source-leakage diagnostic, not a full-channel constant.
5. Produce exact symbolic cleanups for the $\mathrm{SU}(4)$ local row, especially $c_1^{(4)}$.
6. Decide whether the full-channel class problem will be attacked through a stronger smoothing norm, a finite analytic cutoff, or the Peter--Weyl/Casimir shell transfer.

## 10.5 One-line bottom line

The durable corrected architecture is
$$
\boxed{
\text{exact local }\mathrm{SU}(3)\text{ spectrum}
\;+
\text{finite leakage diagnostic}
\;+
\text{rooted Wilson hard-defect polymer route}.}
$$
The remaining proof obligation is not more finite-channel numerics; it is the inhomogeneous Wilson free-energy stability theorem and the associated full-channel transfer control.


# Appendix A. Derivation of $H_1$ and $H_2$ from the Wilson plaquette character

This appendix derives the perturbations $H_1=-p_2^2/96$ and $H_2=\sqrt6\bigl(p_2^3/11520+p_3^2/8640\bigr)$ used in the main text from the Taylor expansion of the $\mathrm{SU}(3)$ Wilson plaquette character. The computation follows the strong-coupling method of [Münster 1981; Drouffe–Zuber 1983]; the one point we stress, because it is the source of the paper's main result, is the emergence of the non-radial invariant $p_3^2$ and its exact relative weight. Every algebraic identity below has been verified symbolically.

## A.1 Cartan coordinates and the invariants as power sums

Conjugate a group element near the identity into the maximal torus, $g=\operatorname{diag}(e^{i\theta_1},e^{i\theta_2},e^{i\theta_3})$ with $\theta_1+\theta_2+\theta_3=0$. Introduce orthonormal coordinates $(x,y)$ on the plane $\sum_j\theta_j=0\subset\mathbb{R}^3$ via the orthonormal basis $u=\tfrac1{\sqrt2}(1,-1,0)$, $v=\tfrac1{\sqrt6}(1,1,-2)$:
$$
\theta_1=\tfrac{x}{\sqrt2}+\tfrac{y}{\sqrt6},
\qquad
\theta_2=-\tfrac{x}{\sqrt2}+\tfrac{y}{\sqrt6},
\qquad
\theta_3=-\tfrac{2y}{\sqrt6}.
$$
A direct computation then gives the two basic Weyl invariants as the power sums
$$
p_2=\sum_{j}\theta_j^2=x^2+y^2,
\qquad
p_3=\sum_{j}\theta_j^3=\tfrac{\sqrt6}{6}\,y\,(3x^2-y^2).
$$
These are exactly the generators used throughout the paper: $p_2$ is the radial (degree-$2$) invariant and $p_3$ the non-radial (degree-$3$) invariant. The reflection $y\mapsto-y$, a Weyl reflection, fixes $p_2$ and sends $p_3\mapsto-p_3$, which is the parity used in §3.3 and §4.2.

## A.2 The Wilson character expansion and the appearance of $p_3^2$

The plaquette potential is
$$
V=\beta\Bigl(1-\tfrac13\,\Re\chi_{(1,0)}\Bigr)
=\beta\Bigl(1-\tfrac13\sum_{j}\cos\theta_j\Bigr).
$$
Expanding $\cos\theta_j=1-\tfrac{\theta_j^2}{2}+\tfrac{\theta_j^4}{24}-\tfrac{\theta_j^6}{720}+\cdots$ and using $\sum_j\theta_j=0$,
$$
V=\beta\Bigl(\tfrac16 P_2-\tfrac1{72}P_4+\tfrac1{2160}P_6-\cdots\Bigr),
\qquad
P_k:=\sum_j\theta_j^k.
$$
The higher power sums reduce to $p_2,p_3$ by Newton's identities, specialised to $e_1=\sum_j\theta_j=0$ (so $e_2=-P_2/2$, $e_3=P_3/3$):
$$
P_4=\tfrac{P_2^2}{2},
\qquad
P_6=\tfrac{P_2^3}{4}+\tfrac{P_3^2}{3}.
$$
Substituting and writing $P_2=p_2$, $P_3=p_3$,
$$
\boxed{\;
\frac{V}{\beta}
=
\tfrac16\,p_2
-\tfrac1{144}\,p_2^2
+\tfrac1{8640}\,p_2^3
+\tfrac1{6480}\,p_3^2
-\cdots
\;}
$$

This is the crux of the derivation. The non-radial invariant $p_3^2$ enters the potential for the first time at order $\theta^6$, through the $P_6$ term, with coefficient $\tfrac1{6480}$, alongside the radial $p_2^3$ with coefficient $\tfrac1{8640}$. Their ratio is
$$
\frac{[\,p_2^3\,]}{[\,p_3^2\,]}=\frac{1/8640}{1/6480}=\frac34 .
$$
A radial truncation of the class problem keeps the $p_2$-tower ($p_2,p_2^2,p_2^3,\ldots$) and discards $p_3$ entirely; it therefore omits the $\tfrac1{6480}p_3^2$ term. This single omission is what produces the wrong order-$\beta^{-1/2}$ coefficient in §5.3–5.4.

## A.3 The kinetic term and the Weyl-denominator conjugation

The kinetic operator $\tfrac12 C_2$ is the Laplace–Beltrami operator on class functions. On the maximal torus it is conjugate, through the Weyl denominator
$$
\delta(\theta)=\prod_{\alpha>0}2\sin\!\bigl(\tfrac{\alpha(\theta)}{2}\bigr),
$$
to a flat operator with a constant shift: since $\delta=\sum_{w\in W}(\det w)\,e^{i\,w\rho\cdot\theta}$ is a finite combination of torus characters with $|w\rho|^2=\|\rho\|^2$, one has the exact identity $\Delta_T\,\delta=-\|\rho\|^2\,\delta$, and hence on Weyl-invariant $\psi$,
$$
C_2\,\psi=\delta^{-1}\bigl(-\Delta_T-\|\rho\|^2\bigr)(\delta\psi).
$$
The conjugation contributes only the *constant* $-\|\rho\|^2$; it produces no $\theta$-dependent potential. The squared Weyl denominator $\delta^2$ has leading polynomial form $\Delta_W^2=\tfrac{p_2^3}{2}-3p_3^2$ (Lemma 2.1), which is exactly the Jacobian weight of the class inner product (§2.3). Working in the near-identity Gaussian approximation, the kinetic operator therefore reduces to $-\Delta_{xy}$ plus a constant.

Combining with the quadratic part of the potential, the leading operator is the two-dimensional oscillator
$$
H_0^{\mathrm{full}}=-\Delta_{xy}+\tfrac\beta6\,(x^2+y^2)+\text{const},
$$
whose first excitation gap is
$$
\omega(\beta)=\sqrt{\tfrac{2\beta}{3}} .
$$
The additive constant ($-\|\rho\|^2$ together with the $\beta\cdot$const from the potential) is common to all class states and cancels identically in the gap $E_1-E_0$; it never appears in $c_0$, $c_1$, or any coefficient of the gap law.

## A.4 The scaled perturbations and the rescaling convention

Rescaling the Cartan coordinates by $\beta^{1/4}$ organises $H_\beta$ by half-integer powers of $\beta$,
$$
H_\beta=\beta^{1/2}H_0+H_1+\beta^{-1/2}H_2+O(\beta^{-1}),
$$
with the perturbations read off from the potential of §A.2. In the orthonormal coordinates above, the raw expansion gives $H_1\propto p_2^2$ and $H_2\propto\bigl(\tfrac14 p_2^3+\tfrac13 p_3^2\bigr)$ — i.e. with the $3:4$ ratio of §A.2.

The specific constants quoted in the main text,
$$
H_1=-\tfrac{p_2^2}{96},
\qquad
H_2=\sqrt6\Bigl(\tfrac{p_2^3}{11520}+\tfrac{p_3^2}{8640}\Bigr),
$$
correspond to a fixed normalisation of the rescaling (equivalently, of the quadratic Casimir). Relative to the bare orthonormal expansion $-\tfrac{p_2^2}{144}$ and $\tfrac{p_2^3}{8640}+\tfrac{p_3^2}{6480}$ of §A.2, the main-text constants are obtained by a single coordinate rescaling $p_2\mapsto\lambda^2 p_2$, $p_3\mapsto\lambda^3 p_3$ with
$$
\lambda^4=\tfrac32 .
$$
This is consistent across all three coefficients: $H_1$ (a $p_2^2\sim\lambda^4$ object) scales by $\tfrac32$, and both $H_2$ terms ($\sim\lambda^6$) scale by $(\tfrac32)^{3/2}=\tfrac{3\sqrt6}{4}$, exactly reproducing $\sqrt6/11520$ from $1/8640$ and $\sqrt6/8640$ from $1/6480$. The $p_2^3:p_3^2=3:4$ ratio is invariant under the rescaling.

## A.5 What is convention-independent

A coordinate rescaling does not change the spectrum, so the gap $\Delta_{\mathrm{SU}(3)}(\beta)$, and in particular the coefficients $c_0$ and $c_1$, are independent of the rescaling normalisation: the factor $\lambda^4=\tfrac32$ above is absorbed into intermediate quantities and cancels in the final eigenvalue differences. What this appendix establishes directly from the Wilson character — independently of any normalisation choice — is the structural content on which the paper's result rests:

1. the class invariants are the power sums $p_2=\sum\theta_j^2$, $p_3=\sum\theta_j^3$;
2. the potential contains a non-radial $p_3^2$ term, entering at order $\theta^6$;
3. the radial and non-radial second-order terms occur in the exact ratio $p_2^3:p_3^2=3:4$;
4. the kinetic conjugation contributes only a constant, so the perturbations $H_1,H_2$ are the potential terms and the additive constant cancels in the gap.

Facts (2)–(3) are precisely what make the non-radial correction $\tfrac{\sqrt6}{576}$ to $c_1$ nonzero and fix its size; they are derived here without recourse to the downstream spectral computation, which (in §§5–6 and the companion verification script) independently confirms the absolute constants and the resulting gap law.
