# Gauge-fixing, Hodge stiffness, and sharper decay constants (with simulations)

> **Thesis.** The constant that controls rigorous exponential decay bounds is not “a law of nature”;
> it is partly a bookkeeping choice.  
> For lattice Maxwell, adding a gauge-fixing / exactness penalty upgrades curl--curl to the **Hodge Laplacian**,
> collapses the stencil, and dramatically improves the decay constant entering Davies/CT bounds.

---

## 1. The analytic move: add an exactness penalty

Work on a finite complex with cochain operators
\[
d_0:C^0\to C^1,\qquad d_1:C^1\to C^2,
\]
and adjoints \(d_0^\*, d_1^\*\) w.r.t. the natural \(\ell^2\) inner products.

The gauge-invariant Maxwell kinetic energy on 1-forms is
\[
\langle A,\; d_1^\* d_1 A\rangle = \|d_1 A\|_2^2.
\]
But \(d_1^\* d_1\) has a large nullspace coming from exact forms \(A=d_0\phi\), reflecting gauge redundancy.

A standard gauge-fixing / stiffness term is
\[
\frac{1}{\xi}\,\langle A,\; d_0 d_0^\* A\rangle
=\frac{1}{\xi}\,\|d_0^\* A\|_2^2,
\qquad \xi>0.
\]
So the gauge-fixed quadratic form is
\[
\|d_1 A\|_2^2 + \frac{1}{\xi}\|d_0^\* A\|_2^2
=\langle A,\; (d_1^\*d_1+\xi^{-1}d_0 d_0^\*)A\rangle,
\]
i.e. the **Hodge Laplacian on 1-forms** up to the scalar \(\xi\).

This is the structural content of the local stiffness lemma: adding the exactness penalty gives uniform control
over the gauge directions and makes the operator genuinely elliptic.

---

## 2. What happens in Fourier space (why this helps constants)

On a periodic lattice, the Maxwell symbol decomposes into transverse and longitudinal projectors,
\[
P_T(p),\;P_L(p),
\qquad P_T+P_L=I.
\]
For the massive Maxwell operator
\[
M(p)= (m^2+\alpha\hat p^2)\,P_T(p) \;+\; m^2\,P_L(p),
\]
the longitudinal modes are *massive but not dispersive* (no \(\hat p^2\)), which is fine physically but makes
kernel bookkeeping “weird” when you take absolute values of coefficients.

After adding \(\xi\, d_0 d_0^\*\) (the grad--div part), you get
\[
M_{\mathrm{gf}}(p)= (m^2+\alpha\hat p^2)\,P_T(p)\;+\;(m^2+\xi\hat p^2)\,P_L(p).
\]
In **Feynman gauge** \(\xi=\alpha\), this becomes
\[
M_{\mathrm{gf}}(p)= (m^2+\alpha\hat p^2)\,(P_T+P_L)= (m^2+\alpha\hat p^2)\,I.
\]
Translation: the \(1\)-form operator decouples into \(d\) copies of the scalar massive Laplacian.
The off-diagonal mixed-derivative stencil disappears.

That is exactly the kind of structural simplification that improves the row-sum constant \(C_0\).

---

## 3. Simulation: \(C_0\) collapses from \(\sim 44\) to \(8\) in \(d=4\)

A GPU/FFT inversion experiment on a \(16^4\) torus computes the exact Green kernel
\(G(b,b') = (m^2 I+\alpha d_1^\*d_1)^{-1}_{bb'}\),
checks the Davies bound shell-by-shell, and measures the “connectivity constants”.

**Measured geometry/constants (Maxwell, no gauge-fixing).**
For \(d=4\), \(L=16\), \(m^2=0.3\), \(\alpha=1\), one obtains
\[
D_{\mathcal E}=18,\qquad C_0(\Delta_1)\approx 43.9077,
\]
and the numeric verification reports the bound ratio
\[
\max_{b}\Big(\frac{m^2}{2}|G(b,b_0)|e^{\eta\,\mathrm{dist}_{\mathcal E}(b,b_0)}\Big)
\approx 0.1412<1,
\]
for the tested \(\eta\)'s, confirming the decay bound is satisfied.

**Measured collapse in Feynman gauge.**
When the kinetic operator is replaced by
\[
\alpha\,d_1^\*d_1 + \xi\, d_0 d_0^\*,\qquad \xi=\alpha,
\]
the script prints
\[
\text{New }C_0 \approx 8.0000,
\qquad
\eta_{\text{new}} \approx 0.1933,
\]
exactly matching the scalar Laplacian count \(C_0=2d=8\) in \(d=4\).

---

## 4. Minimal reproducible code core (FFT exact inversion + bound check)

Below is a condensed core of what the simulation does (omitting plotting and some helper boilerplate):

```python
import math, torch
import torch.fft as fft

# Parameters
L, d = 16, 4
m2, alpha = 0.3, 1.0
m = math.sqrt(m2)
device = "cuda" if torch.cuda.is_available() else "cpu"
real = torch.float64
cplx = torch.complex128

# Momentum grid
p = []
for mu in range(d):
    n = torch.arange(L, device=device, dtype=real)
    p_mu = 2.0*math.sin(math.pi*n/L)
    shape = [1]*d; shape[mu]=L
    p.append(p_mu.reshape(shape).expand([L]*d))
hatp = torch.stack(p, dim=0)              # (d,L,L,L,L)
p2   = torch.sum(hatp**2, dim=0)          # (L,L,L,L)
p2_safe = torch.where(p2>0, p2, torch.ones_like(p2))

# Longitudinal projector P_L
P_L = torch.zeros((d,d,*([L]*d)), device=device, dtype=real)
for mu in range(d):
    for nu in range(d):
        P_L[mu,nu] = (hatp[mu]*hatp[nu]) / p2_safe
P_L = torch.where(p2.unsqueeze(0).unsqueeze(0)>0, P_L, torch.zeros_like(P_L))

# Inverse symbol for Maxwell (no gauge fixing)
inv_trans = 1.0/(m2 + alpha*p2)
inv_long  = 1.0/(m2 + 0.0*p2)  # longitudinal has only m^2 in Maxwell
M_inv = torch.zeros_like(P_L)
for mu in range(d):
    M_inv[mu,mu] = inv_trans
M_inv = M_inv + (inv_long - inv_trans).unsqueeze(0).unsqueeze(0) * P_L

# Real-space Green kernel via IFFT
G = torch.zeros_like(M_inv, dtype=cplx)
for mu in range(d):
    for nu in range(d):
        G[mu,nu] = fft.ifftn(M_inv[mu,nu].to(dtype=cplx), dim=tuple(range(d)))
G = G.real.to(dtype=real)  # (d,d,L,...,L)

# --- Gauge fixed experiment (Feynman gauge xi=alpha) ---
xi = alpha
inv_long_gf = 1.0/(m2 + xi*p2)
M_inv_gf = torch.zeros_like(P_L)
for mu in range(d):
    M_inv_gf[mu,mu] = inv_trans
# if xi==alpha, inv_long_gf == inv_trans and M_inv_gf is diagonal scalar
M_inv_gf = M_inv_gf + (inv_long_gf - inv_trans).unsqueeze(0).unsqueeze(0) * P_L
```

To check Davies-style bounds, you (i) BFS the edge-graph to compute \(\mathrm{dist}_{\mathcal E}(b,b_0)\),
(ii) evaluate \(|G_{b,b_0}|\) on all links, and (iii) maximize the ratio
\[
R_\eta(b)=\frac{m^2}{2}|G_{b,b_0}|e^{\eta\,\mathrm{dist}_{\mathcal E}(b,b_0)}.
\]

---

## 5. Why this is *theoretically* interesting (beyond the numerics)

1. **It isolates the enemy.** The “bad constant” \(C_0\) is bad because absolute values erase cancellations
   from mixed derivatives (curl--curl structure). In a gauge where the operator diagonalizes, those cancellations
   are exact and the constant collapses.

2. **It suggests a path to sharper rigorous bounds.** If one can:
   - prove the functional inequalities (Poincaré/LSI) in a gauge-fixed formulation, and
   - control the passage back to gauge-invariant observables,
   then the analytic bounds may track the *physical* mass scale much more closely.

3. **It interfaces nicely with multiscale.** Coarse-graining steps tend to produce grad--div terms anyway.
   Treating “Hodge stiffness” as a feature, not a hack, may make RG-style arguments cleaner.

---
