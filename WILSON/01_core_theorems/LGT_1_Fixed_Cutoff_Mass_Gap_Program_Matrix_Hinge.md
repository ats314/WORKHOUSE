# Fixed-Cutoff Lattice Gauge Mass-Gap Program (Sketch)
## Vacuum Hessian \(\to\) Maxwell Operator \(\to\) Matrix Hinge \(\to\) Typicality \(\to\) Exponential Clustering \(\to\) OS Gap

\begin{center}
\textit{A compact map of the project’s rigorous lattice gauge chain. This is a program skeleton: most steps are formalized, but key analytic inputs remain isolated as “external inputs.”}
\end{center}

## Abstract

The lattice gauge portion of the project is a constructive-QFT style attempt to convert geometric/analytic control of a Wilson Gibbs measure into a spectral gap for the corresponding Osterwalder–Schrader (OS) Hamiltonian at fixed cutoff. The technical spine is:

\[
\text{(vacuum linearization)}\Rightarrow\text{(deterministic massive Maxwell operator)}\Rightarrow\text{(curvature lower bound on a good set)}\Rightarrow\text{(Helffer–Sj\"ostrand covariance)}\Rightarrow\text{(Green-kernel decay)}\Rightarrow\text{(Euclidean clustering)}\Rightarrow\text{(OS gap)}.
\]

The most distinctive “local” idea is the **matrix hinge**: a pointwise operator inequality on a high-probability good set that compares the random Bakry--\'Emery curvature matrix to a deterministic massive Maxwell operator.

---

## 1. Vacuum expansion produces a Maxwell operator

Let \(U^{(0)}\) be the vacuum configuration. The vacuum linearization identifies the discrete curvature (plaquette holonomy) differential with the cochain coboundary \(d_1\), and the Wilson action Hessian with the discrete Maxwell operator.

### 1.1 Vacuum Hessian identity

At the vacuum,
\[
\boxed{\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})=\alpha_W\,d_1^*d_1}\qquad\text{on }\mathcal C^1(\Lambda_L;\mathfrak g).
\]

This is the exact, deterministic “Gaussian” approximation to the gauge measure around the vacuum: the second variation of the Wilson action is literally a Maxwell stiffness term.

### 1.2 Massive Maxwell operator

The program then works with a massive deformation
\[
M_{\Lambda_L}:=m_H^2\,\mathrm{Id}+\alpha_W\,d_1^*d_1,
\]
whose inverse has good decay properties (finite range + mass).

---

## 2. The matrix hinge: coercivity on a good set

The hard part is to control the full nonlinear measure away from strict vacuum. The project does this by conditioning on a canonical “good set” where plaquettes are small.

### 2.1 Hinge operator

A deterministic comparison operator is introduced:
\[
\boxed{M_{\Lambda_L}^{\mathrm{hinge}}:=m_H^2\,\mathrm{Id}+\tfrac12\alpha_W\,d_1^*d_1.}
\]

### 2.2 Curvature lower bound on the good set

On the good set \(\mathcal K_{\Lambda_L,\beta}\), the Bakry--\'Emery curvature matrix of the Gibbs measure is bounded below by the hinge operator:
\[
\boxed{\mathrm{Ric}_{\mu_{\Lambda_L,\beta}}(U)\succeq M_{\Lambda_L}^{\mathrm{hinge}}\qquad (U\in\mathcal K_{\Lambda_L,\beta}).}
\]

This inequality is the bridge from the nonlinear gauge measure to a deterministic linear Green operator. It is designed as the key input for Helffer–Sj\"ostrand covariance bounds.

### 2.3 The isolated bottleneck

The file explicitly isolates a model-specific “small-field stability” estimate as an external input: show that on \(\mathcal K\), the Wilson Hessian stays close to its vacuum value, uniformly in volume. In the program’s logic, this is the single non-generic bound that must be proved by hand.

---

## 3. Typicality: the good set dominates at volume scale

Conditioning is only useful if the bad set has tiny probability. The project supplies an explicit tail bound for the canonical good set defined by the average plaquette potential.

### 3.1 Canonical good set and tail bound

Let \(K_{\Lambda_L}(\varepsilon)\) be the event that the average plaquette potential is \(\le\varepsilon\). In \(d=4\), one obtains a **volume-scale** estimate:
\[
\boxed{\mu_{\Lambda_L,\beta}\big(K_{\Lambda_L}(\varepsilon)^c\big)\le \exp\big(-c_{\mathrm{typ}}(\beta;\varepsilon,r)\,|P(\Lambda_L)|\big)}
\]
for an explicit exponent \(c_{\mathrm{typ}}\) provided it is positive.

This is the measure-theoretic lever: it guarantees that any covariance decomposition “error term on the bad set” is exponentially small in the volume.

---

## 4. From curvature to covariances (Helffer–Sj\"ostrand + localization)

The intended covariance mechanism is:

1. represent \(\mathrm{Cov}_{\mu}(F,G)\) as an inner product of gradients against the inverse Witten Laplacian (Helffer–Sj\"ostrand representation),
2. use the matrix hinge to compare that inverse to \((M_{\Lambda_L}^{\mathrm{hinge}})^{-1}\) on the good set,
3. control the complement by typicality.

Symbolically, for local observables \(F,G\),
\[
\mathrm{Cov}(F,G)\ \approx\ \langle\nabla F,(M_{\Lambda_L}^{\mathrm{hinge}})^{-1}\nabla G\rangle\ +\ \text{(typicality-suppressed error)}.
\]

The important structural point is that *locality lives in the gradient*: gradients of cylinder observables have support only on the links the observable depends on, which allows one to convert kernel decay into clustering.

---

## 5. Kernel decay for \((M_{\Lambda_L}^{\mathrm{hinge}})^{-1}\)

The operator \(M_{\Lambda_L}^{\mathrm{hinge}}\) is finite-range (graph-local) and uniformly positive. Deterministic Combes–Thomas/Davies-type arguments yield exponential off-diagonal decay of its inverse blocks:
\[
\|(M_{\Lambda_L}^{\mathrm{hinge}})^{-1}(x,y)\|\ \lesssim\ \exp\big(-\eta\,\mathrm{dist}(x,y)\big).
\]

Once you have that, the covariance bound becomes exponential clustering: distant observables have exponentially small covariance at fixed cutoff.

---

## 6. Euclidean time decay \(\Rightarrow\) OS Hamiltonian gap

Reflection positivity plus translation covariance is the OS doorway: Euclidean correlation decay in the time direction becomes a statement about the transfer matrix \(T\) and hence the OS Hamiltonian \(H\) defined via \(T=e^{-aH}\).

In the program’s organization, the only substantive OS fact needed is isolated as an external input (in the OS appendix chain): **Euclidean time decay implies a spectral gap** above the vacuum sector.

---

## 7. What’s novel here (as a program)

The techniques used in the chain are classical, but the project’s potential novelty is the *packaging*:

- it identifies the **single model-specific analytic bottleneck** (small-field stability of the Wilson Hessian),
- it builds everything else as a deterministic/functorial pipeline: hinge \(\Rightarrow\) covariance \(\Rightarrow\) clustering \(\Rightarrow\) gap.

That is the right shape for a serious attempt at fixed-cutoff gap statements.

---

## 8. What to do next (highest-leverage work)

1. **Prove the “small-field stability” external input.** This is the keystone: a volume-uniform operator-norm control of Hessian deviations on \(\mathcal K\).

2. **Make the good set canonical across appendices.** The typicality appendix uses \(K_{\Lambda_L}(\varepsilon)\); the hinge appendix uses \(\mathcal K_{\Lambda_L,\beta}\). Showing these are compatible (or replacing one with the other) will simplify the global logic.

3. **Quantify the mass parameter \(m_H\).** In practice, the decay rate \(\eta\) and the OS gap lower bound will depend on the mass term. A clean derivation of \(m_H\) from gauge fixing/horizontal restriction would sharpen the physical statement.

4. **Thermodynamic limit interfaces.** The appendices anticipate a “gap permanence” story under limits; formalizing that operator-limit step is crucial if the end goal is continuum physics.

