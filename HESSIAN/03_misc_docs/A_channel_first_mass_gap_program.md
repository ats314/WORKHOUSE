---
title: "A Channel-First Route to the Yang–Mills Mass Gap (Speculative Program)"
format: "markdown+latex"
status: "Research sketch: plausible ingredients, unproven core conjectures"
---

## 0. Scope and epistemic status

This document extracts the *one* idea from the chat that feels both (i) technically grounded in known mathematics and (ii) **unusually cross-disciplinary** in a way that could plausibly open a new attack surface on the Yang–Mills mass gap:

> Treat the Euclidean time step (transfer matrix / time-slab) as a **mixing operator** (and, after suitable normalization/truncation, a **quantum channel**) and attempt to bound the physical mass gap using **functional inequalities** (Poincaré / log-Sobolev / hypercontractivity) stated for that operator.  
> Then tie those inequalities to **information geometry** (Fisher curvature) of a family of YM Gibbs states.

Nothing below is a proof of the Clay problem. The novelty (if any) is in the **organizational choice** and the proposed bridge: curvature → log-Sobolev constant → spectral gap → mass gap.

---

## 1. The hard target in the cleanest algebraic form

On a lattice with time spacing \(a\), define the transfer matrix
\[
T(a)=e^{-aH(a)}.
\]
Let its eigenvalues be \(\lambda_0(a)>\lambda_1(a)\ge \cdots\). Then
\[
m(a)=E_1(a)-E_0(a)=-\frac1a\log\!\left(\frac{\lambda_1(a)}{\lambda_0(a)}\right).
\]

The continuum mass gap statement is:
\[
m_{\mathrm{phys}}=\lim_{a\to 0}m(a)>0,
\]
together with existence of the continuum theory.

Define the **normalized transfer operator**
\[
\widetilde T(a)\equiv \lambda_0(a)^{-1} T(a),
\]
so that \(\widetilde T(a)\) has top eigenvalue \(1\) and next eigenvalue \(e^{-a m(a)}\).

Then the mass gap is equivalently:
\[
m(a)=-\frac1a\log|\lambda_1(\widetilde T(a))|.
\]

---

## 2. Reframing: spectral gap as “mixing” of a positive operator

Even before invoking “quantum channels”, one can treat \(\widetilde T(a)\) as a **positivity-preserving** linear operator acting on a finite-volume Hilbert space (with an inner product induced by reflection positivity / the vacuum).

The mass gap becomes the rate at which iterates of \(\widetilde T\) contract orthogonal components:
\[
\|\widetilde T^n f\| \le |\lambda_1(\widetilde T)|^n \|f\|
\quad\Rightarrow\quad
\|\widetilde T^n f\|\lesssim e^{-a m\, n}\|f\|.
\]

So: **mass gap = exponential mixing rate in Euclidean time.**

This suggests importing the toolkit of mixing bounds:

- Poincaré (spectral gap) inequalities,
- log-Sobolev inequalities,
- hypercontractivity.

---

## 3. “Quantum channel” version (where it might become genuinely new)

### 3.1 Why a literal channel is nontrivial

\(T\) is a positive operator; it is not automatically a **trace-preserving completely positive map** on density matrices. To speak honestly:

- In a **finite-dimensional truncation** (e.g., quantum link models, tensor-network coarse-graining, or boundary-MPO representations of a time slab), the Euclidean slab naturally defines a linear map between boundary operator algebras.
- After normalization (to make the fixed point a state) and choosing an appropriate Heisenberg/Schrödinger picture, one may obtain a **primitive** (mixing) CPTP map \(\Phi\) whose second eigenvalue is controlled by the same physics as \(\lambda_1(\widetilde T)\).

This is a concrete program step: *make the “channel” representation explicit and correct in a controlled finite-dimensional setting first.*

### 3.2 What you would try to prove once you have \(\Phi\)

Let \(\Phi\) be a primitive quantum channel with invariant state \(\rho_\infty\).
A **quantum log-Sobolev inequality** (QLSI) of the rough form
\[
D\!\left(\Phi^n(\rho)\,\Vert\,\rho_\infty\right)
\le e^{-2\alpha n}\, D\!\left(\rho\,\Vert\,\rho_\infty\right)
\]
implies exponential mixing in relative entropy, which typically implies:

- exponential decay of correlations for local observables,
- a spectral gap for the generator (if \(\Phi=e^{\mathcal L}\)),
- and hence a bound on \(|\lambda_1(\Phi)|\), the subleading eigenvalue magnitude.

The intended bridge is:
\[
\alpha >0\quad\Rightarrow\quad
|\lambda_1(\Phi)| \le e^{-c\alpha}
\quad\Rightarrow\quad
m \gtrsim \alpha/a.
\]

The constants and exact implications depend on the precise QLSI notion used. The point is: **prove a QLSI for the transfer step** (or its generator), and you get the mass gap “for free” as a corollary.

---

## 4. Where “information geometry” enters (the speculative bridge)

Consider a finite set of gauge-invariant sources \(\theta\) coupled to local operators \(O_i\), defining a family of Gibbs states (or Euclidean boundary states)
\[
\rho_\theta \propto e^{-H_\theta},
\qquad
H_\theta = H + \sum_i \theta_i O_i.
\]

Equip the parameter manifold \(\{\rho_\theta\}\) with a quantum Fisher metric, e.g. the Bogoliubov–Kubo–Mori (BKM) metric:
\[
g_{ij}(\theta)=\frac{\partial^2}{\partial\theta_i\partial\theta_j}\log Z(\theta)
\quad\text{(classical analogue)},
\]
with an operator-valued generalization in the quantum case.

**Speculative conjectural bridge:**
A lower bound on a suitable curvature of this state manifold (a quantum analogue of Bakry–Émery/Ricci lower bounds) implies a **uniform** quantum log-Sobolev constant for the associated transfer channel \(\Phi\).

Symbolically:
\[
\mathrm{Ric}(\{\rho_\theta\})\ge \kappa >0
\quad\Longrightarrow\quad
\alpha_{\mathrm{QLSI}}(\Phi)\gtrsim \kappa
\quad\Longrightarrow\quad
m>0.
\]

This is the “new path” ingredient: it replaces a direct Rayleigh-quotient bound on \(H\) with a curvature → hypercontractivity route.

---

## 5. Concrete, testable subproblems (so this is not just vibes)

### 5.1 Finite-volume SU(2) pilot model

Pick a tiny lattice (e.g. \(2^3\) or \(3^3\)) and a truncated Hilbert space (quantum link / small-rep truncation).

1. Build (or tensor-network represent) a single time step as a linear map on the boundary space.
2. Normalize to obtain a primitive channel \(\Phi\).
3. Numerically estimate:
   - \(|\lambda_1(\Phi)|\),
   - a mixing rate under \(\Phi^n\) for simple observables,
   - a candidate QLSI constant lower bound (even crude).
4. In parallel, compute a Fisher/BKM-like metric on a small source manifold \(\rho_\theta\) and estimate curvature proxies.
5. Check whether “larger curvature proxy ⇒ larger mixing constant ⇒ larger gap” correlates robustly under:
   - lattice refinement (within truncation),
   - coupling changes.

### 5.2 Proof-oriented toy theorem

Prove the full bridge in a model where it is known to be true:

- certain quantum spin systems with known QLSI bounds,
- then ask what structural properties are required (locality + positivity + frustration-free?).

Use that to define “what YM would need to satisfy” in the channel picture.

---

## 6. How this connects to larger theories

This program sits at the intersection of:

- **Constructive QFT / lattice gauge theory**: transfer matrix, reflection positivity.
- **Functional inequalities**: Poincaré/log-Sobolev/hypercontractivity as a route to spectral gaps.
- **Quantum information**: primitive channels, entropy contraction, quantum Markov semigroups.
- **Renormalization**: coarse-graining to a boundary channel where mixing is more tractable.
- **Tensor networks**: explicit boundary maps from Euclidean slabs.

If it works, it would recast “mass gap” as a *hypercontractivity constant* of a physically defined evolution map.

---

## 7. What would count as genuine progress

Not “we believe the vacuum is rigid”.

Progress would look like:

1. A **precise** construction of \(\Phi\) for a controlled truncated gauge model.
2. A **provable** QLSI/Poincaré inequality for \(\Phi\) with a bound uniform in volume (in that truncated setting).
3. A **controlled limit** where the truncation is relaxed and the bound remains nontrivial.

Even partial results here could be interesting, because they create a new, rigorous inequality-driven handle on the gap.
