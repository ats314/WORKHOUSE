# Numerics: What to Measure, How to Measure It, and What You Currently See

*This note extracts the numerical pieces that directly test the project’s distinctive geometric mechanism: “near-Cartan rarity” and “order-one curvature defect \(\Phi(a)\)” for \(\mathrm{SU}(3)\).*

---

## 1. Core observables

### 1.1 Star curvature defect \(\Delta_\ell\) and its mean \(\Phi(a)\)

At a link \(\ell\), define the star Hessian \(\mathsf H_W^{(\ell)}(U)\) (gauge-fixed at \(\ell\)) and its smallest eigenvalue \(\lambda_{\min}\).

Fix a vacuum reference constant \(\kappa_\*=\lambda_{\min}(\mathsf H_W^{(\ell)}(U^{(0)}))\).

Define the defect observable
\[
\Delta_\ell(U):=(\kappa_\*-\lambda_{\min})_+,
\]
and define the average
\[
\Phi(a):=\mathbb E_{\mu_a}[\Delta_\ell(U)].
\]

The project’s mechanism predicts \(\Phi(a)\) is order-one in lattice units (and scale-stable under coarse graining).

### 1.2 Cartan misalignment statistic \(r_\ell\)

Given the six plaquettes incident to \(\ell\), compute six associated Lie algebra vectors \(X_p(U)\) (transported force directions, or normalized plaquette logs). Define a misalignment score \(r_\ell\in[0,1]\) such that:
- \(r_\ell\approx 0\) means “near a common Cartan direction” (almost abelian / aligned),
- \(r_\ell\approx 1\) means “strongly noncommuting / generic.”

The framework predicts:
- \(r_\ell\) is typically order-one,
- and the event \(r_\ell\le \epsilon\) is extremely rare for small \(\epsilon\).

---

## 2. One-page protocol: measuring \(\Phi(a)\) in lattice simulations

This is deliberately **measurement-only**. You can generate gauge configurations with any standard codebase; this protocol does not require you to tune an in-chat Metropolis kernel.

### Inputs
- Gauge group: \(\mathrm{SU}(3)\).
- An ensemble of Wilson gauge configurations \(U\) at a fixed \(\beta\) and lattice spacing \(a\), with periodic boundaries.
- For each configuration: link variables \(U_\mu(x)\in \mathrm{SU}(3)\).

### Measurement steps (per configuration)
1. **Choose a batch of links** \(\{\ell_i\}_{i=1}^B\) uniformly at random from all oriented links.
2. **For each link \(\ell\):**
   1. Enumerate the six plaquettes in \(\mathrm{Star}(\ell)\).
   2. Compute each oriented plaquette holonomy \(U_p\) as an ordered product of four links (with inverses for backward edges).
   3. Gauge-fix at \(\ell\): multiply the star neighborhood by a local gauge transformation so that \(U_\ell=\mathbf 1\).
   4. Assemble the **exact** physical star Hessian \(\mathsf H_W^{(\ell)}(U)\) (finite-dimensional).
   5. Compute \(\lambda_{\min}(\mathsf H_W^{(\ell)}(U))\).
   6. Record \(\Delta_\ell=(\kappa_\*-\lambda_{\min})_+\).
   7. Compute misalignment \(r_\ell\) from the same six plaquettes (using your chosen force/log direction definition).
3. **Average:**
   \[
   \widehat\Phi(a)=\frac1B\sum_{i=1}^B \Delta_{\ell_i},\qquad
   \widehat r=\frac1B\sum_{i=1}^B r_{\ell_i}.
   \]
4. Repeat over configurations and report mean ± standard error.

### Outputs to record
- \(\widehat\Phi(a)\) and its standard error.
- Histogram / quantiles of \(r_\ell\); especially \(\mathbb P(r_\ell<0.1)\), \(\mathbb P(r_\ell<0.2)\).
- Joint correlation \(\mathrm{corr}(\lambda_{\min}, r)\).

---

## 3. Expected numerical outcomes if the framework is correct

If the “Cartan exceptional set is rare” picture is correct, you should see:

1. **Misalignment rarity:**  
   \(\mathbb P(r_\ell<0.1)\) and \(\mathbb P(r_\ell<0.2)\) are tiny (often consistent with 0 at moderate sample sizes).

2. **Order-one curvature defect:**  
   \(\widehat\Phi(a)\) is not small; it is comparable to \(\kappa_\*\) in lattice units (not exponentially small in \(\beta\)).

3. **Stiffness collapse correlates with alignment:**  
   \(\lambda_{\min}\) should increase as \(r\) decreases (Cartan-aligned stars are the only ones that *avoid* stiffness loss); equivalently, you should see a positive correlation between “alignment” and “larger \(\lambda_{\min}\).”

4. **Scale stability (harder test):**  
   as you block-spin / coarse-grain, the distribution of \(\Delta_\ell\) should remain order-one (up to predictable renormalizations of \(\kappa_\*\)).

---

## 4. The useful numerical results already present in this project + chat

### 4.1 Exact-force adversarial search (SU(2), 2D) — supports A′

The project ran exact-force gradient-descent experiments on a 2D torus for SU(2) (varying lattice size, random and checkerboard Cartan initializations) and observed:

> driving \(\|\nabla S\|\) down forces plaquette disorder to collapse toward the vacuum; no rough configurations with near-zero force were found.

This supports (A′) as an energy-landscape fact (though it does not prove it).

### 4.2 Your GPU measurements in this chat (SU(3), 4D Wilson)

From the runs recorded in this chat (A100 / CUDA), you observed:

- Cartan misalignment \(r\): mean \(\approx 0.75\), and empirically
  \(\mathbb P(r<0.2)=0\) over \(\sim 30{,}000\) sampled links.
- Star Hessian minimum eigenvalue: mean \(\lambda_{\min}\approx -2.09\) on a batch of \(512\) links.
- With \(\kappa_\*\approx 12\), the measured mean defect was
  \[
  \widehat\Phi_{\delta K}=\mathbb E[(\kappa_\*-\lambda_{\min})_+]\approx 14.09.
  \]

These three numbers are already a strong qualitative match to the theory’s “near-Cartan rarity + order-one defect” expectations.

---

## 5. Code artifacts available inside this project

- `exact_force_su2_2d.py` implements the SU(2) exact-force search / projected gradient descent infrastructure used in the counterexample search.

For SU(3) \(\Phi(a)\) measurement, the measurement logic is contained in your Colab notebook(s) used in this chat. A next clean engineering step is to factor that measurement code into a standalone script that:
- loads configurations from disk (MILC/openQCD formats or a simple torch tensor format),
- computes \((r_\ell,\lambda_{\min},\Delta_\ell)\) in large GPU batches,
- emits summary statistics and a compact JSON.

---

## Sources inside this project

- Assumption A′ statement + numerical counterexample search summary: `02_Assumption_A_and_LocalCancellation_SU2.docx`
- Exact-force counterexample search design + code: `03_Numerical_Counterexample_Search_SU2_ExactForce.docx`, `exact_force_su2_2d.py`
- Broader numerical observations: `NUMERICAL_NOTES.md`
