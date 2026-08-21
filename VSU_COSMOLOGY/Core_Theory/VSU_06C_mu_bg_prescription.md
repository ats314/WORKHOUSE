# VSU 06C — A Cosmological Prescription for $\mu_{\rm bg}(a)$ (No Trench-Coat Free Functions)

## Purpose

In the VSU linear-growth sector, the effective coupling is written as
\[
G_{\rm eff}(k,a)=G\,[1+\alpha_{\rm eff}(k,a)] ,
\]
with $\alpha_{\rm eff}$ containing the constitutive function $\mu(\cdot)$.
The constitutive law $\mu(x)=1-e^{-x}$ is fixed, but **one must still specify what
background argument** enters it in cosmology.  

If left unspecified, $\mu_{\rm bg}(a)$ becomes an implicit *free function of time*.
This note gives a *closed* and *predictive* prescription for $\mu_{\rm bg}(a)$ in the
spirit of VSU’s parameter minimality.

---

## 1. What $\mu_{\rm bg}$ means physically: EFE as “renormalized Poisson”

The nonlinear operator implies an **External Field Effect (EFE)**: if a system’s field is
\[
\mathbf g = \mathbf g_{\rm int} + \mathbf g_{\rm ext},
\]
then to leading order the internal potential obeys a *linear* Poisson equation with a
renormalized coefficient
\[
\nabla\cdot\!\left[\mu\!\left(\frac{|\mathbf g_{\rm ext}|}{a_0}\right)\nabla\Phi_{\rm int}\right]
\;\approx\;4\pi G \rho_{\rm int}.
\]
Thus, at linear order, the relevant $\mu$ is evaluated not at zero field, but at the
**external/background field strength**.

Cosmologically, the mean field vanishes by statistical isotropy, but the **variance**
does not. The only clean choice is to define the background argument via an RMS external
field amplitude.

---

## 2. Definition: $\mu_{\rm bg}(a)$ from an RMS peculiar-acceleration field

Define a coarse–grained (“long”) peculiar gravitational acceleration field
\[
\mathbf g_L(\mathbf x,a) := -\frac{1}{a}\nabla \Phi_L(\mathbf x,a),
\]
where $\Phi_L$ is the Newtonian potential smoothed on a comoving scale $R$.

Then define
\[
g_{\rm bg}(a;R) \;:=\;\sqrt{\big\langle |\mathbf g_L|^2 \big\rangle},
\qquad
\boxed{\;
\mu_{\rm bg}(a)\;:=\;\mu\!\left(\frac{g_{\rm bg}(a;R_{\rm nl}(a))}{a_0}\right)
\;=\;
1-\exp\!\left[-\frac{g_{\rm bg}(a;R_{\rm nl}(a))}{a_0}\right].
\;}
\]

The RMS can be written in Fourier space in terms of the potential power spectrum:
\[
g_{\rm bg}^2(a;R)
=
\frac{1}{a^2}\int_0^\infty \frac{dk}{2\pi^2}\,k^4\,P_\Phi(k,a)\,W^2(kR),
\]
with $W(kR)$ the usual real–space top-hat window (or whichever window is already adopted
for $\sigma_R$; see next section).

---

## 3. The only “choice” is the smoothing scale — so define it *unambiguously*

To avoid introducing an arbitrary pivot scale, set the smoothing scale to the **nonlinear
transition scale**, defined exactly as in standard LSS practice:

\[
\sigma_R^2(a)
=
\int_0^\infty \frac{dk}{k}\,\Delta^2(k,a)\,W^2(kR),
\qquad
\Delta^2(k,a)=\frac{k^3}{2\pi^2}P_m(k,a),
\]
and define $R_{\rm nl}(a)$ by the condition
\[
\boxed{\;\sigma_{R_{\rm nl}}(a)=1.\;}
\]

This prescription is parameter–free:
- $W$ is fixed once (e.g. the top-hat used for $\sigma_8$),
- $R_{\rm nl}(a)$ is then determined by the *same* $P_m(k,a)$ you already compute for
  $\sigma_8$, lensing kernels, etc.

---

## 4. Where $P_\Phi$ and $P_m$ come from

Using the standard relation between $\Phi$ and $\delta$ in the linear theory, one may write
\[
P_\Phi(k,a)
=
\left(\frac{3}{2}\frac{H_0^2\Omega_{m0}}{k^2}\right)^2
\mathcal G^2(k,a)\frac{D^2(k,a)}{a^2}P_{\rm ini}(k),
\qquad
\mathcal G:=1+\alpha_{\rm eff}.
\]

If you want a *non-circular* first pass, you can evaluate $g_{\rm bg}$ using GR
($\mathcal G=1$ and $D=D_{\rm GR}$) because the long modes that dominate the external field are
precisely those where the VSU Yukawa factor suppresses modifications.

For full self-consistency, treat the above as a closure problem and iterate (see below).

---

## 5. Closed predictive system (practical recipe)

Given $(H_0,\Omega_{m0},\Omega_{\Lambda0})$ and the single new parameter $a_0$:

1. **Initialize** with GR growth $D_{\rm GR}(a)$ and $P_m^{(0)}(k,a)=P_{\rm ini}(k)D_{\rm GR}^2(a)$.
2. Compute $\sigma_R^{(0)}(a)$ and solve $\sigma_{R_{\rm nl}}(a)=1$ for $R_{\rm nl}^{(0)}(a)$.
3. Compute $g_{\rm bg}^{(0)}(a)=g_{\rm bg}(a;R_{\rm nl}^{(0)}(a))$ and hence $\mu_{\rm bg}^{(0)}(a)$.
4. Insert $\mu_{\rm bg}^{(0)}(a)$ into $\alpha_{\rm eff}(k,a)$ and solve the growth equation for
   $D^{(1)}(k,a)$.
5. Recompute $P_m^{(1)}$, $R_{\rm nl}^{(1)}$, $g_{\rm bg}^{(1)}$, $\mu_{\rm bg}^{(1)}$.
6. Iterate to convergence.

Nothing is fit as a function of time: $\mu_{\rm bg}(a)$ is an *output*.

---

## 6. Why this prescription behaves correctly (sanity checks)

- **Early times:** $R_{\rm nl}(a)$ shifts to smaller physical scales, where typical accelerations are
  larger, pushing $g_{\rm bg}\gg a_0$ and hence $\mu_{\rm bg}\to 1$. The modification shuts off,
  consistent with the required $\alpha_{\rm eff}\to 0$ limit.

- **Late times ($z\lesssim 2$):** growth slows/freeze under $\Lambda$, so $P_m(k,a)$ and the nonlinear
  scale evolve slowly. Therefore $g_{\rm bg}(a)$ and $\mu_{\rm bg}(a)$ become slowly varying, making
  $\alpha_{\rm eff}$ approach a time-independent $\alpha_\infty(k)$.

- **No hidden functions:** all time dependence is inherited from $H(a)$ and the linear growth that is
  already being solved for. There is no extra phenomenological dial.

---

## 7. Minimal fix to the $\alpha_{\rm eff}$ ansatz

To ensure *strict* GR recovery when $\mu_{\rm bg}\to 1$ (screened limit), the small-scale amplitude
should scale like $(1/\mu_{\rm bg}-1)$ rather than $1/\mu_{\rm bg}$, i.e.
\[
\boxed{
\alpha_{\rm eff}(k,a)
=
\left(\frac{1}{\mu_{\rm bg}(a)}-1\right)
\frac{k^2}{k^2+a^2 m_{\rm eff}^2(a)} .
}
\]
This preserves the intended “Yukawa-on / Yukawa-off” behavior but removes an otherwise unavoidable
$\alpha_{\rm eff}\to 1$ offset in the screened regime.

---

## Status

This note provides a fully specified cosmological $\mu_{\rm bg}(a)$ prescription that:
- uses the EFE structure already present in the nonlinear operator,
- introduces no free functions or tunable scales,
- can be implemented analytically (symbolically) or numerically (iterative closure).
