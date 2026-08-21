# Admissibility as a Structural Layer: From Convexity Tests to an Energy-Honest “Rectifier” Simulation

> Curated from (a) the project’s admissibility/convexity themes and
> (b) the ALPO discussion in this chat, plus an explicit simulation and energy audit.

## 1. The real abstraction: “admissibility” = structural inequalities

Across the project, the recurring pattern is:

- write the physics as a variational principle (energy/Hamiltonian),
- demand strict convexity/coercivity/positivity properties,
- use those structural inequalities to enforce stability, uniqueness, and controlled limits.

In the gravity track this is convexity of $\mathcal H(|\nabla\Phi|/a_0)$.
In the lattice gauge track it’s reflection positivity + operator inequalities that imply a spectral gap.

This is a real meta-theory seed:

> **Physical admissibility is not a specific equation; it’s a test suite of inequalities
> that a candidate model must satisfy to be deployable.**

---

## 2. The engineering temptation: “rectify stiffness, harvest work”

A minimal toy device is a base-excited oscillator with a **path-dependent stiffness**:
\[
m\ddot x + c_{\rm tot}\dot x + k(\dot x)\,x = -m\,\ddot x_{\rm ext}(t),
\qquad
x_{\rm ext}(t)=A\sin(\omega t),
\]
with $c_{\rm tot}=c_{\rm mech}+c_{\rm load}$.
We model energy extraction as “electrical damping”:
\[
P_{\rm load}(t)=c_{\rm load}\dot x^2.
\]

A direction-dependent stiffness can be modeled smoothly as
\[
k(\dot x)=k_{\rm soft}+(k_{\rm stiff}-k_{\rm soft})\frac12\Big(1-\tanh(\dot x/v_0)\Big).
\]

### The key energy-accounting fact

When $k$ varies in time (even indirectly via $\dot x$),
the stored energy
\[
E(t)=\frac12 m\dot x^2+\frac12 k(t)x^2
\]
obeys
\[
\boxed{
\frac{dE}{dt}
=
P_{\rm base}
+
P_k
-
(c_{\rm mech}+c_{\rm load})\dot x^2,
}
\]
where
\[
P_{\rm base}=-m\ddot x_{\rm ext}\dot x,
\qquad
P_k=\frac12\dot k\,x^2.
\]

So a “stiffness diode” is *not automatically passive*.
If $\langle P_k\rangle>0$ in steady state, then something is actively injecting energy through stiffness modulation (parametric drive).

---

## 3. Numerical sweep: harvested power vs tuned load

I implemented an RK4 simulation with default parameters:
- $m=1\,{\rm kg}$,
- $A=1\,{\rm cm}$,
- $f=5\,{\rm Hz}$ (so base acceleration amplitude $\sim 1g$),
- $k_{\rm soft}=1000\,{\rm N/m}$, $k_{\rm stiff}=5000\,{\rm N/m}$,
- $c_{\rm mech}=1\,{\rm N\,s/m}$,
- sweep $c_{\rm load}\in[0,20]\,{\rm N\,s/m}$.

### Summary results

The table below reports steady-state averages over the post-transient window:

| c_load | P_load_W | P_mech_W | P_base_W | P_k_W | eta_load_over_total_in | eta_load_over_base_only |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.2404 | 0.1397 | 0.1007 | 0 | 0 |
| 4 | 0.8927 | 0.2232 | 0.6524 | 0.4634 | 0.8 | 1.368 |
| 8 | 1.525 | 0.1907 | 1.017 | 0.6992 | 0.8889 | 1.5 |
| 12 | 1.851 | 0.1542 | 1.211 | 0.7937 | 0.9231 | 1.528 |
| 16 | 1.937 | 0.121 | 1.272 | 0.7851 | 0.9412 | 1.522 |
| 20 | 1.846 | 0.09232 | 1.226 | 0.7131 | 0.9524 | 1.507 |

Interpretation:

- Harvested power increases with $c_{\rm load}$ until a broad maximum.
- The ratio $\eta_{\rm load}/P_{\rm base}$ exceeds $1$ in this toy model **only because** $P_k>0$:
  stiffness modulation is injecting substantial energy.

This is not “bad news”; it’s a diagnostic:
**your rectifier claim becomes physically meaningful only once you specify the mechanism that pays for (or extracts from) $P_k$.**

---

## 4. Code and raw results (download)

- `alpo_simulation.py` — the simulator (includes the energy audit and load sweep).
- `alpo_results.csv` — the full sweep output.

---

## 5. How to upgrade the toy into a physically respectable device model

The next-step model is to *replace* the prescribed $k(\dot x)$ rule with an **internal coordinate**
$q$ (a latch angle, buckling mode amplitude, phase state) so that:

- $k = k(q)$,
- $q$ has its own dynamics and energy accounting,
- coupling to the base is explicit.

Then the “vacuum rectifier” question becomes:

> does the coupled $(x,q)$ system admit a passive mechanism where the effective stiffness is history-dependent
> while the net extracted energy is traceable to base work, not to hidden parametric injection?

That is a falsifiable engineering question, and the admissibility framework provides the right language to state it cleanly.

---

## Appendix: key lesson (one sentence)

A direction-dependent stiffness element is either  
(a) **a dissipative rectifier**, or  
(b) **a parametric amplifier** — and the difference is exactly the sign and source of $\langle P_k\rangle$.
