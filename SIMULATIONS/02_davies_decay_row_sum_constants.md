# Combes–Thomas/Davies decay with row-sum constants (Δ₁-controlled)

This note extracts the **finite-range inverse-decay mechanism** used in Part 9,
and the key refinement: replacing crude bounded-degree constants by a genuine **row-sum constant**
attached to \(\Delta_1\).

---

## 1. Row-sum constants for \(\Delta_1\)

Let \(\Delta_1\) be the 1-cochain Hodge Laplacian on \(\mathcal C^1(\Lambda;\mathfrak g)\).
Define the off-diagonal row-sum constant
\[
\boxed{
C_0(\Delta_1)
:=
\max_{b\in E(\Lambda)}
\ \sum_{\tilde b\in E(\Lambda),\ \tilde b\neq b}
\ \big\|(\Delta_1)_{b\tilde b}\big\|_{\mathrm{op}}.
}
\]

A boundary version \(C_{\partial}(\Delta_1)\) is defined analogously by restricting the \(\tilde b\)-sum to boundary edges.

These constants are **combinatorial but operator-theoretic**:
they depend on which link-stencil couplings exist (and their norms), not on a generic “graph degree” proxy.

---

## 2. Abstract inverse-decay lemma (Combes–Thomas conjugation)

Let \(H\) be a strictly positive self-adjoint operator on \(\ell^2(V)\) with:
- a positivity gap: \(H \succeq a_0 I\),
- finite range \(R\) in a graph metric \(\mathrm{dist}\),
- bounded off-diagonal row-sum: \(B\) (in the sense used in the project’s Definition 9.DG).

Then one obtains an exponential kernel bound for \(H^{-1}\):
\[
\big|H^{-1}(x,y)\big|
\ \le\
C\,e^{-\eta\,\mathrm{dist}(x,y)},
\]
with
\[
\boxed{
\eta
=
\frac{2}{R}\,\mathrm{arsinh}\!\left(\frac{\sqrt{a_0}}{2\sqrt{B}}\right).
}
\]

The proof uses the standard Combes–Thomas conjugation:
conjugate by \(e^{\gamma \phi}\) where \(\phi\) is a Lipschitz function increasing with distance,
and choose \(\gamma\) so the perturbation from conjugation does not close the spectral gap.

---

## 3. Applying it to the massive Maxwell operator

In the project, the operator is
\[
M_H = m^2 I + \alpha\, d_1^\*d_1\quad \text{(restricted to horizontals)}.
\]

The Combes–Thomas lemma applies because:
- \(m^2 I\) gives a uniform positivity gap \(a_0=m^2\),
- \(d_1^\*d_1\) is finite-range (plaquette-local stencil),
- the off-diagonal row-sum is controlled by \(\alpha C_0(\Delta_1)\).

Thus one can take
\[
B_0(M_H)\ \le\ \alpha\,C_0(\Delta_1)
\]
and get
\[
\boxed{
\eta_{\mathrm{DG}}
=
2\,\mathrm{arsinh}\!\left(\frac{\sqrt{m^2}}{2\sqrt{\alpha\,C_0(\Delta_1)}}\right)
}
\quad\text{(when }R=1\text{ in link-adjacency distance).}
\]

---

## 4. Why this refinement matters

A bounded-degree bound treats \(\Delta_1\) like an arbitrary graph Laplacian.
But \(\Delta_1\) is not arbitrary: it is a geometric cochain operator built out of incidence structure.

Replacing degree by \(C_0(\Delta_1)\):
- tightens constants,
- remains invariant under many harmless geometric relabelings,
- isolates exactly which local couplings drive the decay exponent.

This is a **portable analytic device**: it can be reused for any finite-range operator where one wants an inverse-decay exponent with explicit constants.

---

## 5. Simulation diagnostic: computed “C0” may not match the theoretical \(C_0(\Delta_1)\)

One simulation notebook computes a quantity labelled `C0` via an inverse FFT of the Fourier symbol
\[
Q_{\mu\nu}(p)=\hat p^2\,\delta_{\mu\nu} - \hat p_\mu \hat p_\nu
\]
and then sums absolute values of the resulting kernel coefficients.

This produced values like \(C0\approx 87\)–\(116\) depending on \(L\).
That is **not obviously the same object** as the combinatorial \(C_0(\Delta_1)\) above, which should be volume-independent for a finite-range stencil.

This mismatch is not a disaster; it is a **useful reality check**:
- either the simulation is computing a different (legitimate) \(\ell^1\)-kernel norm in a different basis,
- or there is a phase/normalization/convention bug in the Fourier ↔ cochain kernel conversion (common when link-centered vs site-centered conventions are mixed).

Fixing this and demonstrating that the numeric method recovers the theoretical row-sum constant is an excellent “sanity trophy” to aim for.

---

## 6. What this note enables next

Once you have exponential decay for \(M_H^{-1}\), your Part 10 clustering theorem turns it into an **exponential covariance bound** (up to localization error), which then feeds OS reconstruction (Part 11) to yield a Hamiltonian gap lower bound.
