# OS bridge: Euclidean decay ⇒ Hamiltonian spectral gap (fixed cutoff)

This note extracts the “bridge theorem” that turns your **Euclidean-time exponential decay**
into a **spectral gap** for the Osterwalder–Schrader (OS) Hamiltonian at fixed lattice spacing \(a>0\).

The point is: once exponential time-decay is established with constants uniform in volume,
**the spectral theorem does the rest**.

---

## 1. Minimal OS structure used

Fix a Euclidean lattice measure \(\mu\) satisfying:
- time-translation invariance,
- reflection invariance about a time-slice hyperplane,
- reflection positivity on the positive-time algebra \(\mathcal A_+\).

OS reconstruction yields a Hilbert space \(\mathcal H_{\mathrm{OS}}\),
a vacuum vector \(\Omega=[1]\),
a positive contraction \(T\) implementing one time-step,
and a self-adjoint Hamiltonian \(H\ge 0\) such that
\[
T=e^{-aH}.
\]

The only OS identity you need for the gap step is the transfer identity:
\[
\boxed{
\langle [F], e^{-naH} [G]\rangle_{\mathrm{OS}}
=
\mu\big((\theta F)\,(\tau_n G)\big).
}
\]

---

## 2. Spectral theorem lemma: exponential decay implies a gap

Let \(F\in\mathcal A_+\) be a positive-time local observable with \(\mu(F)=0\).
Suppose there exists \(m>0\) such that
\[
\boxed{
\big|\mu\big((\theta F)\,(\tau_t F)\big)\big|
\ \le\
C(F)\,e^{-mt}
\qquad \forall t\ge 0,
}
\]
where \(t\) is Euclidean time separation.

Then, writing \(\psi_F:=[F]\), the OS identity gives
\[
\langle \psi_F, e^{-tH}\psi_F\rangle
=
\mu\big((\theta F)\,(\tau_t F)\big).
\]

By the spectral theorem, this is the Laplace transform of the spectral measure \(\nu_F\) of \(H\) w.r.t. \(\psi_F\):
\[
\langle \psi_F, e^{-tH}\psi_F\rangle
=
\int_{[0,\infty)} e^{-t\lambda}\,d\nu_F(\lambda).
\]

If \(\nu_F\) had any mass on \([0,m)\), the Laplace transform would decay strictly slower than \(e^{-mt}\),
contradicting the assumed bound for large \(t\).
Thus \(\mathrm{supp}(\nu_F)\subset[m,\infty)\) for all such \(\psi_F\).

Since OS-cylindrical vectors span a dense subspace of \(\Omega^\perp\), one concludes:
\[
\boxed{
\mathrm{gap}(H)\ \ge\ m.
}
\]

This is the clean “Euclidean decay ⇒ gap” interface.

---

## 3. Packaging for your mass-gap chain

Your Part 10 provides a Euclidean clustering exponent \(\eta(a)\) in lattice steps.
Conversion to a physical mass parameter is (up to the slab-distance constant \(c_1\)):
\[
m_{\mathrm{Euc}}(a)=\frac{c_1\,\eta(a)}{a}.
\]

So, at fixed cutoff \(a>0\),
\[
\boxed{
\mathrm{gap}(H_a)\ \ge\ \frac{c_1\,\eta(a)}{a}.
}
\]

The project explicitly tracks that \(\eta(a)\) comes from Part 9’s Combes–Thomas exponent
for the massive Maxwell inverse.

---

## 4. Where the real remaining work lives

This bridge is clean; it is not where the hard physics hides.
The heavy lift is in establishing Euclidean decay with constants:
- uniform in the volume,
- valid for gauge-invariant observables,
- with localization errors controlled (the “typicality” input in your dependency ledger).

Once that is in hand, the OS bridge is essentially automatic.

---

## 5. Continuum limit note (conditional)

Your Part 12 notes that to pass \(a\downarrow 0\), one needs:
- reflection positivity persistence under the chosen limiting architecture,
- and a scaling trajectory where the physical gap does not collapse,
  i.e. \(\eta(a)\gtrsim m_0\,a\).

This is a separate (and honestly harder) problem; this note is only the fixed-cutoff gap conversion.
