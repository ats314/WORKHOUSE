# Interacting 1D Quantum Rotor with a θ-Term: Polynomial Transfer Matrix, Positivity Proof, and Cost Scaling
*(Extracted + sanity-checked from the interacting-rotor construction and complexity notes.)*

## 0. Why this is “exciting”

The interacting rotor adds a potential term (e.g. \(\lambda\cos\phi\)), which destroys the free rotor’s simple diagonal structure.  
What’s novel in the project is that the **phase-isolation trick still works**:

- all *bulk* tensor entries remain **real and non-negative**, even with interactions,
- the \(\theta\)-term remains a **boundary-only phase** \(e^{ik\theta}\),
- the resulting contraction can be organized as a **polynomial transfer matrix** \(W(X)\) whose coefficients are sector weights.

That gives a deterministic, sign-problem-free (in the strict local sense) pipeline—plus an explicit resource scaling analysis.

---

## 1. Hamiltonian and Trotterization

Consider
\[
H(\theta,\lambda)=\frac{1}{2I}\left(L_z-\frac{\theta}{2\pi}\right)^2+\lambda\cos\phi.
\]

Use a second-order Trotter–Suzuki split over \(\beta=N\Delta\tau\):
\[
e^{-\Delta\tau H}\approx
e^{-\frac{\Delta\tau}{2}V}\,e^{-\Delta\tau T(\theta)}\,e^{-\frac{\Delta\tau}{2}V},
\quad
V(\phi)=\lambda\cos\phi.
\]

The kinetic propagator admits the same covering-space Gaussian structure as the free rotor; the potential factors are pointwise positive:

\[
\exp\!\left[-\frac{\Delta\tau}{2}\lambda(\cos\phi_{j+1}+\cos\phi_j)\right] > 0
\quad \text{for real }\lambda.
\]

---

## 2. Local non-negativity with winding indices

Let \(\phi_j\in[0,2\pi)\) and lift indices \(k_j\in\mathbb Z\).  
Define the unwrapped Gaussian kernel for a winding increment \(n=k_{j+1}-k_j\):

\[
K_{0,n}(\phi_{j+1},\phi_j)
=
\exp\!\left[-\frac{I}{2\Delta\tau}\,(\phi_{j+1}-\phi_j+2\pi n)^2\right].
\]

Then a single-step transfer weight is

\[
T^{(n)}(\phi_{j+1},\phi_j)
=
\exp\!\left[-\frac{\Delta\tau\lambda}{2}\big(\cos\phi_{j+1}+\cos\phi_j\big)\right]
\;K_{0,n}(\phi_{j+1},\phi_j).
\]

Every factor is \(\ge 0\), hence:

> **Proposition (bulk positivity survives interactions).**  
> All local tensor elements can be chosen real and non-negative; the \(\theta\)-term is inserted only at the boundary by weighting total winding sectors by \(e^{ik\theta}\).

This is explicitly stated as a design requirement in the interacting-rotor construction notes.

---

## 3. Polynomial transfer matrix \(W(X)\)

Discretize \(\phi\) by an \(M\)-point quadrature grid \(\{\phi_a\}_{a=1}^M\) (with suitable weights absorbed into the tensor).

Define a discrete index \(s\equiv a\) for the angle grid point. Then each time step has a matrix of *polynomials* in a formal variable \(X\):

\[
W(X)_{s',s} = \sum_{n=-K_{\text{step}}}^{K_{\text{step}}} T^{(n)}_{s',s}\,X^{n},
\qquad T^{(n)}_{s',s}\ge 0.
\]

After \(N\) steps,
\[
W(X)^N_{s',s}
=
\sum_{k} C^{(k)}_{s',s}\,X^{k},
\qquad C^{(k)}_{s',s}\ge 0.
\]

The winding-sector partition functions are obtained by tracing over angle indices:
\[
Z_k^{(0)}(\beta,\lambda)=\sum_s C^{(k)}_{s,s}.
\]

Finally, evaluate the generating function at \(X=e^{i\theta}\):
\[
Z(\beta,\theta,\lambda) = \sum_{k\in\mathbb Z} e^{ik\theta} Z_k^{(0)}(\beta,\lambda).
\]

This is the interacting rotor’s concrete implementation of phase isolation.

---

## 4. Error budget and scaling laws

Three main error sources appear:

1. **Trotter error** (second order): typically \(O(\beta^3/N^2)\).
2. **Angle discretization error** from quadrature over \(\phi\). For analytic kernels/potentials, the notes bound it by an exponential-in-\(M^2\) form that depends on \(N\):
   \[
   \varepsilon_M \lesssim C\,N\,\exp\!\left(-C_3\,\frac{\beta M^2}{N}\right).
   \]
3. **Winding truncation error** from restricting \(|k|\le K_{\max}\), with Gaussian tails:
   \[
   \varepsilon_K \sim \exp\!\left(-c\,\frac{K_{\max}^2}{\beta}\right).
   \]

Balancing \(\varepsilon_N\sim\varepsilon_M\sim\varepsilon_K\sim\varepsilon\) yields the scaling relations quoted in the project:

\[
N \sim \beta^{3/2}\varepsilon^{-1/2},
\qquad
M \sim \beta^{1/4}\varepsilon^{-1/4}\sqrt{\ln(1/\varepsilon)},
\qquad
K_{\max}\sim \sqrt{\beta\ln(1/\varepsilon)}.
\]

---

## 5. Bond dimension and computational cost (log-factor audit)

The natural bond dimension for the discrete TN is

\[
D \sim M\,(2K_{\max}+1).
\]

Substituting the above scalings gives

\[
D
\sim
\Big(\beta^{1/4}\varepsilon^{-1/4}\sqrt{\ln(1/\varepsilon)}\Big)
\Big(\sqrt{\beta\ln(1/\varepsilon)}\Big)
=
\beta^{3/4}\varepsilon^{-1/4}\,\ln(1/\varepsilon).
\]

A straightforward contraction / transfer-matrix multiplication cost model is

\[
\mathcal C_{\mathrm{TN}}\sim N D^3.
\]

Therefore,

\[
\mathcal C_{\mathrm{TN}}
\sim
\Big(\beta^{3/2}\varepsilon^{-1/2}\Big)\,
\Big(\beta^{3/4}\varepsilon^{-1/4}\ln(1/\varepsilon)\Big)^3
=
\beta^{15/4}\,\varepsilon^{-5/4}\,(\ln(1/\varepsilon))^{3}.
\]

### Note on the project’s reported \((\ln(1/\varepsilon))^{3/2}\)

Some project notes quote a \((\ln(1/\varepsilon))^{3/2}\) factor in the final complexity.  
The *algebraic* exponents \(\beta^{15/4}\varepsilon^{-5/4}\) are consistent across the files; the discrepancy is in log bookkeeping (effectively whether one counts a \(\sqrt{\ln}\) factor once or twice inside \(D\)).

Because log factors are subleading and implementation-dependent (different truncation allocations, adaptive cutoffs, non-uniform grids, etc.), the actionable take-away is:

- **Polynomial exponents:** \(\beta^{15/4}\varepsilon^{-5/4}\) (robust target),
- **Log factors:** should be treated as a “to-be-measured” detail and validated by numerical scaling studies.

A clean next step is to run fixed-\((\beta,\lambda)\) convergence scans in \(N,M,K_{\max}\) and empirically fit the effective log behavior.

---

## 6. Suggested “next proof” to solidify this framework

To turn these scaling arguments into something theorem-like, one would want:

1. an explicit bound on the **Trotter error constant** for the rotor’s \(\lambda\cos\phi\) potential,
2. a rigorous quadrature error bound matching the \(\exp(-C\beta M^2/N)\) form for the specific discrete kernel used,
3. a full **composition argument** that the winding distribution tails remain Gaussian (or better) in the presence of the potential.

The rotor archive already flags which earlier “dead end” truncation bounds were unphysical and which were corrected; these would be the natural lemmas to formalize.

---

## Sources in the project

- Bulk positivity and boundary-only \(\theta\): `Technical Elaboration_ Tensor Network Construction Modifications for the Interacting Quantum Rotor.md`.
- Winding truncation scaling and corrected \(N\)-independence: `TN_1D_Rotor_Detail_v2.md`.
- Complexity summaries and comparative discussion: the “Computational Complexity…” notes.

