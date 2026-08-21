# One-Step Bridge: Configuration Diffusion Gap \(\Rightarrow\) OS Mass Gap
*(a single inequality \((18.\star)\) that collapses the diffusion-to-Hamiltonian interface)*

## 1. Two “gaps” that live on different objects

### 1.1 Configuration diffusion (geometric/analytic side)
Let \((M_\Lambda,\mu_\Lambda)\) be the finite-volume configuration manifold with Gibbs measure \(\mu_\Lambda\). Let
\[
L_\Lambda = \Delta_{g_\Lambda} - \langle \nabla S_\Lambda,\nabla \cdot\rangle
\]
be the reversible Langevin generator on \(L^2(\mu_\Lambda)\), with Dirichlet form
\[
\mathcal E_\Lambda^{\mathrm{conf}}(f,f)=\int_{M_\Lambda} |\nabla f|^2\,d\mu_\Lambda.
\]
A Poincaré inequality is a lower bound
\[
\mathcal E_\Lambda^{\mathrm{conf}}(f,f)\ \ge\ \lambda_*\,\|f\|_{L^2(\mu_\Lambda)}^2
\quad\text{for all } f\perp 1.
\tag{Poinc}
\]

### 1.2 OS reconstruction (QFT side)
Assume the lattice OS axioms (reflection positivity etc.) so OS reconstruction yields a Hilbert space \(\mathcal H_\Lambda\), vacuum \(\Omega_\Lambda\), transfer operator \(T_\Lambda\) and Hamiltonian \(H_\Lambda\ge 0\) such that
\[
T_\Lambda = e^{-aH_\Lambda},
\]
with lattice spacing \(a>0\).

Define the (finite-volume) mass gap
\[
\Delta_\Lambda := \inf\big(\sigma(H_\Lambda)\setminus\{0\}\big).
\]

---

## 2. Transfer gap = Hamiltonian gap

### Lemma 2.1 (Spectral mapping for the one-step transfer gap)
\[
\boxed{
1-e^{-a\Delta_\Lambda}
=
\inf_{\substack{\Psi\perp\Omega_\Lambda\\ \|\Psi\|=1}}
\langle \Psi,(I-T_\Lambda)\Psi\rangle_{\mathcal H_\Lambda}.
}
\]

**Proof.**
Since \(T_\Lambda=e^{-aH_\Lambda}\) is a bounded self-adjoint contraction with spectrum in \([0,1]\), functional calculus implies
\[
\sigma(T_\Lambda)\setminus\{1\}=e^{-a(\sigma(H_\Lambda)\setminus\{0\})}.
\]
The spectral gap above the eigenvalue \(1\) of \(T_\Lambda\) equals \(1-\sup(\sigma(T_\Lambda)\setminus\{1\})\), which is \(1-e^{-a\Delta_\Lambda}\).
The variational characterization of the top of the spectrum on \(\Omega_\Lambda^\perp\) yields the Rayleigh–Ritz formula stated. \(\square\)

---

## 3. The single missing inequality

To bridge the diffusion Dirichlet form to the OS one-step dissipation, isolate the following target.

### Hypothesis \((18.\star)\) (One-step OS/Dirichlet comparison)
There exists a constant \(c>0\) (uniform in \(\Lambda\)) such that for all \(F\) in a dense positive-time core \(\mathfrak D\),
\[
\boxed{
\langle [F],(I-T_\Lambda)[F]\rangle_{\mathcal H_\Lambda}
\ \ge\ 
c\,\mathcal E_\Lambda^{\mathrm{conf}}(F,F),
}
\tag{18.*}
\]
where \(F\) is viewed as a time-slice observable so that the OS norm matches the \(L^2(\mu_\Lambda)\) norm on \(\mathfrak D\).

This is the “bridge seam.” Everything else is standard spectral theory.

---

## 4. Theorem: \((18.\star)\) + Poincaré \(\Rightarrow\) mass gap

### Theorem 4.1 (Finite-volume OS gap from configuration Poincaré)
Assume:

1. the Poincaré inequality (Poinc) holds with constant \(\lambda_*>0\),
2. the comparison hypothesis \((18.\star)\) holds with constant \(c>0\).

Then
\[
\boxed{
\Delta_\Lambda \ \ge\ \frac{1}{a}\bigl[-\log(1-c\lambda_*)\bigr]\ \ge\ \frac{c}{a}\lambda_*.
}
\]

**Proof.**
Let \(\Psi\in\Omega_\Lambda^\perp\) with \(\|\Psi\|=1\). Approximate \(\Psi\) in \(\mathcal H_\Lambda\) by time-slice vectors \([F_n]\) with \(F_n\in\mathfrak D\), normalized so that \(\|F_n\|_{L^2(\mu_\Lambda)}=1\) and \(\mu_\Lambda(F_n)=0\).

Then by \((18.\star)\) and (Poinc),
\[
\langle [F_n],(I-T_\Lambda)[F_n]\rangle
\ge c\,\mathcal E_\Lambda^{\mathrm{conf}}(F_n,F_n)
\ge c\,\lambda_*.
\]
Pass to the limit \(n\to\infty\) using boundedness of \(I-T_\Lambda\) to get
\[
\langle \Psi,(I-T_\Lambda)\Psi\rangle \ge c\lambda_*.
\]
Taking the infimum over unit \(\Psi\perp\Omega_\Lambda\) and applying Lemma 2.1 yields
\[
1-e^{-a\Delta_\Lambda}\ge c\lambda_*,
\]
hence
\[
\Delta_\Lambda \ge \frac{1}{a}\bigl[-\log(1-c\lambda_*)\bigr].
\]
Finally \(-\log(1-x)\ge x\) for \(x\in(0,1)\) gives \(\Delta_\Lambda \ge (c/a)\lambda_*\). \(\square\)

---

## 5. What this buys you conceptually

The mass-gap program becomes an explicit two-module system:

- **Module A (configuration engine):** prove a uniform \(\lambda_*>0\) via curvature/LSI/Poincaré, local-to-global, drift, etc.
- **Module B (OS bridge):** prove \((18.\star)\) uniformly.

Everything after that is a two-page spectral argument.

---

## 6. Where conditional monotonicity may help next

A forward-leaning idea is to interpret \((I-T_\Lambda)\) itself as a conditional expectation “energy drop” across one time step—i.e. as an operator built from conditioning on a time-slice \(\sigma\)-algebra.

If that representation can be made precise, then the inequality \((18.\star)\) becomes a comparison between:

- a **conditional spectral floor** (one-step OS dissipation),
- and a **Dirichlet form** (configuration gradients),

opening the door to using the conditioning monotonicity lemma as a structural constraint on how \((18.\star)\) can fail.

This does not prove \((18.\star)\), but it isolates a narrow target: the only thing left to control is a single one-step coercivity inequality, not an entire multiscale cascade.

