# PULSE Door: Block-to-Global LSI on a Typical Set \(K^\star\)
*(A template for bypassing global “pairing coercivity” sign issues)*

## 1. Purpose

The project already has a clean “Part 6 + Part 9” conditional clustering mechanism, but it requires a **typical set** \(K\) where the HS/hinge hypothesis holds.

The PULSE door gives a plausible route to typicality:

\[
\text{(block conditional LSI on }K^\star)\ +\ \text{(cross-block influence small)}
\quad\Longrightarrow\quad
\text{global LSI on }K^\star,
\]
then
\[
\text{global LSI}\quad\Longrightarrow\quad
\mu_\Lambda((K^\star)^c)\le e^{-c|P(\Lambda)|}
\quad\text{for }\mathcal B_\Lambda^\star\text{-type constraints.}
\]

This door does **not** require a deterministic global lower bound for the pairing functional.  
It instead uses Dobrushin/block dynamics: *control conditional measures + control how much blocks talk to each other.*

---

## 2. Setup: blocks and conditional measures

Let \(\Lambda\) be a periodic lattice. Choose a block decomposition \(\Lambda=\bigsqcup_i \Lambda_i\) (typically cubes of side \(\ell\)).  
Let \(U=(U_i,U_{i^c})\) denote the block variables and their complement.

Let \(\mu_\Lambda\) be the Gibbs measure; for each block \(i\), let \(\mu_\Lambda(\cdot\mid U_{i^c})\) denote the conditional law of \(U_i\) given the outside.

We will always work **on the typical set** \(K^\star\) (e.g. \(K_\Lambda^\star(\varepsilon)\)) and consider the *restricted conditional measures* \(\mu_\Lambda(\cdot\mid U_{i^c},\,K^\star)\).

---

## 3. The two hypotheses (as written in PULSE)

### (Hloc) Uniform block LSI on \(K^\star\)

There exists \(\rho_{\mathrm{loc}}>0\) such that for all blocks \(i\) and all admissible boundary configurations,
the conditional law on block \(i\) satisfies an LSI with constant \(\rho_{\mathrm{loc}}\) **uniformly** (in \(i\), \(\Lambda\), and boundary data) when restricted to \(K^\star\).

In practice, this comes from **conditional convexity**:
a uniform lower bound on the block Hessian of the effective conditional potential.

### (Mix) Cross-block influence bound

Let \(H_{ii}\) denote the block Hessian (within block \(i\)) and \(H_{ij}\) the mixed Hessian coupling blocks \(i\neq j\).  
Assume there is a uniform bound on
\[
\varepsilon_{ij}\ :=\ \sup_{U\in K^\star}\|H_{ii}^{-1/2} H_{ij} H_{jj}^{-1/2}\|_{\mathrm{op}}
\]
(or an equivalent influence coefficient), with finite interaction range and a bounded-degree block adjacency graph.

Define the Dobrushin-type contraction coefficient
\[
q\ :=\ \max_i \sum_{j\neq i} \varepsilon_{ij}.
\]

The PULSE template is set up so that the entire game is: **show \(q<1\)**.

---

## 4. Conclusion: global LSI on \(K^\star\)

Under (Hloc) and (Mix) with \(q<1\), standard block dynamics (or Dobrushin comparison) yields:

> **Theorem (Block-to-global LSI on \(K^\star\)).**  
> The conditioned measure \(\mu_\Lambda(\cdot\mid K^\star)\) satisfies an LSI with constant
> \[
> \rho_{\mathrm{glob}}\ \gtrsim\ \rho_{\mathrm{loc}}\,(1-q),
> \]
> with all constants volume-uniform.

This is exactly what Part 8.3 needs to run Gaussian concentration for functions with Lipschitz constant \(\sim |P|^{-1/2}\) (like \(\mathcal B_\Lambda^\star\)).

---

## 5. Implementation checklist (the “end-to-end” job)

To implement PULSE in this project, the work splits cleanly:

### Step 1: Choose \(K^\star\) so that (Hloc) is true
- Define \(K^\star=K_\Lambda^\star(\varepsilon)\) using block-averaged badness.
- Prove a **uniform conditional convexity** lower bound on each block Hessian on \(K^\star\).  
  (This is where the HS/hinge and “massive Maxwell structure” are supposed to reattach.)

### Step 2: Bound the mixed derivatives and compute \(q\)
- Use finite-range structure: each block only interacts with \(O(1)\) neighbors.
- Use the constants ledger (row-sum bounds, overlap constants) to bound \(\varepsilon_{ij}\).
- Compute the resulting \(q\) explicitly and check \(q<1\).

### Step 3: Deduce global LSI and concentration
- Apply the block-to-global theorem to get LSI for \(\mu(\cdot\mid K^\star)\).
- Use the Lipschitz bound for \(\mathcal B_\Lambda^\star\) to get
  \[
  \mu_\Lambda\big((K_\Lambda^\star(\varepsilon))^c\big)\ \le\ e^{-c|P(\Lambda)|}.
  \]

### Step 4: Plug into Part 10
- Replace “event \(K\)” in Theorem 10.1 by \(K^\star\).
- Apply Corollary 10.3: conditional clustering + typicality \(\Rightarrow\) pure clustering.

---

## 6. Why this is potentially publishable even before “full LGT mass gap”

The PULSE method reframes the hardest obstruction (sign-indefinite cross terms in a global pairing functional) into:

- local convexity on a typical set, plus
- quantifiable influence bounds.

That is a standard high-dimensional probability playbook, but here it’s being applied in a geometrically nontrivial gauge setting with:
- horizontal projections,
- Lie-group manifold geometry,
- an explicit operator-theoretic decay mechanism (Part 9).

That combination is not standard in the lattice gauge literature.

---

## Source inside the project

- `12-20-25 PULSE.txt`: the quantitative template with the (Hloc)/(Mix) hypotheses and the \(q<1\) strategy.
