# Extract 07 — VSU Hyperbolicity, Effective Metric, and the “Sign of $X$” Trap

\begin{center}
\textbf{Theme:} the scalar sector is (formally) strictly hyperbolic with subluminal characteristics — 
\emph{but} the cosmological background forces you to confront a domain/sign issue for the invariant $X$.
\end{center}

## 0. Context

The VSU scalar field is defined by a covariant action of the form
\[
S[g,\phi] \supset \frac{a_0^2}{8\pi G}\int d^4x\sqrt{-g}\,F(X),
\qquad
X:=\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}.
\]
The constitutive choice is encoded by
\[
K(X):=F'(X)=1-e^{-\sqrt{X}},
\qquad
K'(X)=F''(X)=\frac{e^{-\sqrt{X}}}{2\sqrt{X}}\quad (X>0).
\]

The hyperbolicity analysis derives the principal symbol of the scalar equation
\(
\nabla_\mu(K(X)\nabla^\mu\phi)=0
\)
and identifies an \textbf{effective characteristic metric}.

---

## 1. Linearization and the effective inverse metric

Let
\[
\phi=\phi_0+\varepsilon\,\varphi,\qquad 0<\varepsilon\ll 1,
\]
with background gradient
\[
u_\mu:=\nabla_\mu\phi_0,
\qquad
X_0:=\frac{g^{\mu\nu}u_\mu u_\nu}{a_0^2}.
\]
Keeping only the second-derivative terms in the linearized equation yields
\[
\mathcal P(\varphi)=
\Bigl[
K(X_0)\,g^{\mu\nu}
+\frac{2K'(X_0)}{a_0^2}u^\mu u^\nu
\Bigr]\nabla_\mu\nabla_\nu\varphi
+\text{(lower order)}.
\]
Define
\[
\boxed{
G^{\mu\nu}_{\mathrm{eff}}:=K(X_0)\,g^{\mu\nu}+\frac{2K'(X_0)}{a_0^2}u^\mu u^\nu.
}
\]
Characteristics are the null covectors of $G^{\mu\nu}_{\mathrm{eff}}$:
\[
G^{\mu\nu}_{\mathrm{eff}}\,\xi_\mu\xi_\nu=0.
\]

---

## 2. Hyperbolicity conditions

Strict hyperbolicity requires that $G^{\mu\nu}_{\mathrm{eff}}$ has Lorentzian signature.
For a $k$-essence-type scalar this reduces to the algebraic conditions
\[
\boxed{
K(X_0)>0,
\qquad
K(X_0)+2X_0K'(X_0)>0.
}
\]
For the VSU constitutive law (in its stated $X>0$ domain),
\[
K(X)=1-e^{-\sqrt{X}}>0,
\]
and
\[
K(X)+2XK'(X)
=1-e^{-\sqrt{X}}+\sqrt{X}e^{-\sqrt{X}}
=1-e^{-\sqrt{X}}(1-\sqrt{X})>0.
\]
So: \textbf{if $X_0>0$}, the equation is strictly hyperbolic.

---

## 3. Characteristic (sound) speed and its bounds

Choose a local inertial frame where the background gradient is timelike:
\[
 u^\mu=(\dot\phi_0,0,0,0).
\]
Then
\[
G^{00}_{\mathrm{eff}}=-\bigl[K(X_0)+2X_0K'(X_0)\bigr],
\qquad
G^{ij}_{\mathrm{eff}}=K(X_0)\,\delta^{ij}.
\]
The characteristic speed is
\[
\boxed{
 c_s^2=\frac{K(X_0)}{K(X_0)+2X_0K'(X_0)}.
}
\]

### 3.1 Weak-field limit
For $X\ll 1$, $K(X)\sim \sqrt{X}$ and $K'(X)\sim (2\sqrt{X})^{-1}$, hence
\[
 c_s^2\to \frac{\sqrt{X}}{\sqrt{X}+2X\cdot\frac{1}{2\sqrt{X}}}=\frac{1}{2}.
\]

### 3.2 Strong-field limit
For $X\gg 1$, $K(X)\to 1$ and $K'(X)\to 0$, hence
\[
 c_s^2\to 1.
\]

So (again, in the $X>0$ branch)
\[
\boxed{\tfrac12\le c_s^2<1.}
\]
That’s a tidy stability statement: no elliptic regions, no gradient instabilities, no superluminal propagation.

---

## 4. The “sign of $X$” problem (this is the bit you do \emph{not} want to sweep under the rug)

In cosmology, the homogeneous background is $\phi=\phi(t)$, so the gradient is timelike.
With the usual GR signature $(-,+,+,+)$,
\[
X_0=\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}
= -\frac{\dot\phi_0^2}{a_0^2}
<0.
\]
So the background relevant for the cosmology sector lives on the \textbf{$X<0$ side}.

But the VSU constitutive law is written as
\(
K(X)=1-e^{-\sqrt{X}}
\)
with $K'$ explicitly labeled $(X>0)$, and the hyperbolicity verification is done under the same assumption.

This means:

- the hyperbolicity proof is formally correct \textbf{for the spacelike-gradient sector} (quasistatic, galaxy-scale, $X>0$),
- the cosmological sector as currently written is using $K(X_0)$ and $K'(X_0)$ for $X_0<0$, which is undefined unless an analytic continuation / separate branch is specified.

This is not a nit. It determines whether the background stress–energy, equation of state, and perturbation sound speed are even well-defined.

---

## 5. Three plausible fixes (each with different “theory smell”)

### Fix A: k-essence sign convention
Define instead
\[
\tilde X:=-\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}
\quad\Rightarrow\quad \tilde X>0\ \text{for timelike backgrounds}.
\]
Then $K(\tilde X)=1-e^{-\sqrt{\tilde X}}$ is immediately cosmology-safe.

But: in the quasistatic galaxy regime $\nabla\phi$ is spacelike, giving $\tilde X<0$. So you still need a prescription for the spatial-gradient branch.

### Fix B: two-branch constitutive law (timelike vs spacelike)
Define two smooth functions $K_\mathrm{time}(X)$ for $X<0$ and $K_\mathrm{space}(X)$ for $X>0$, matched continuously at $X=0$.

This is essentially admitting that “cosmology” and “galaxy dynamics” probe different branches of the same scalar EFT.
It can be made consistent, but the matching conditions matter (continuity of $K$ and $K'$ affect the principal symbol).

### Fix C: replace $\sqrt{X}$ by $\sqrt{|X|}$ (or a smooth proxy)
The blunt instrument is
\[
K(X)=1-e^{-\sqrt{|X|}}.
\]
This makes both branches real, but introduces non-analyticity at $X=0$.
A smoother option is to use
\(
\sqrt{|X|}\approx (X^2+\epsilon^2)^{1/4}
\)
with $\epsilon$ a tiny regulator that one can attempt to send to $0$ after deriving the field equations.

The danger: you may inadvertently generate ghosts/instabilities near $X\approx 0$ unless you check $K+2XK'$ carefully on both sides.

---

## 6. Why this is potentially exciting (not just bookkeeping)

If the sign issue is fixed cleanly, VSU becomes a \textbf{single-function} $k$-essence / k-mouflage style scalar with:

- a MOND-like quasistatic branch in galaxies,
- a controlled, subluminal hyperbolic sector in time-dependent settings,
- and a built-in screening interpolation.

That’s a rare combination: many modified gravity models get two of the three and pay for the third with extra fields or tuning.

---

## 7. Immediate next research moves

1. \textbf{Specify $F(X)$ (or $K(X)$) globally on $X\in\mathbb R$.}  
   Until then, cosmological background equations are formally underdefined.

2. \textbf{Re-derive stress–energy, equation of state, and $c_s^2$ on the timelike branch.}  
   The formulas are standard, but their sign details matter.

3. \textbf{Check Cauchy stability on FRW explicitly.}  
   Hyperbolicity in a local inertial frame is necessary but not sufficient for global well-posedness in an expanding background.

4. \textbf{Map to known EFT language.}  
   Placing the model in the “$P(X)$” (k-essence) taxonomy would let you import existing constraints and consistency conditions.
