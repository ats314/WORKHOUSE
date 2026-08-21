# Reflection Positivity → OS Reconstruction → Gap Extraction (Fixed Cutoff)

## Scope

This document isolates the *RP→OS→gap* chain as a stand-alone module.

---

## 1. Reflection datum and positivity (finite volume)

Appendix K fixes a reflection \(\Theta\) across a time mid-plane (even temporal extent), defines positive-time algebra \(\mathcal A_+\), OS involution \(\theta\), and proves:

\[
\boxed{\mu_{\Lambda_L,\beta}((\theta F)F)\ge 0 \quad \forall F\in\mathcal A_+.}
\]

This is the only input needed downstream from Appendix K.

---

## 2. OS Hilbert space + transfer operator interface

Appendix L assumes OS axioms (translation invariance, reflection invariance, reflection positivity, etc.) and isolates the reconstruction as **External Input L.2.6**, yielding:

- \(\mathcal H_{\mathrm{OS}}\) from \(\mathcal A_+/\mathcal N\),
- a positive self-adjoint contraction \(T\) with \(T^n[F]=[\tau_n F]\),
- transfer identity:
\[
\langle [F],T^n[G]\rangle_{\mathrm{OS}}=\mu((\theta F)(\tau_n G)).
\]

---

## 3. Hamiltonian and spectral support lemma

Proposition L.2.7: \(T=e^{-aH}\) for a unique \(H\ge 0\).

Lemma L.3.2: if \(\langle \psi,e^{-naH}\psi\rangle \le C_\psi e^{-mna}\) for all \(n\), then \(E_H([0,m))\psi=0\).

---

## 4. Gap extraction from Euclidean decay

Appendix L culminates in a gap extraction theorem (Theorem L.4.7): if centered OS correlations decay exponentially in discrete Euclidean time,
\[
|\mu((\theta F^\circ)(\tau_n F^\circ))|\le C e^{-\eta n},
\]
then \(\mathrm{gap}(H)\ge \eta/a\) on \(\Omega^\perp\).

---

## 5. Permanence under coarse-graining/limits

Appendix M supplies two permanence results:

- RP preserved by reflection-equivariant pushforward;
- gap inequalities for quadratic forms persist under monotone supremum limits (Proposition M.2.6), with the operator representation step isolated as External Input M.2.7.

Appendix N records the external inputs used in this chain and enforces an “explicit imports only” discipline.

---

## 6. Minimal “what remains” to turn this into a mass derivation

To convert this interface package into an explicit mass scale:

1. Prove an explicit Euclidean time decay exponent \(\eta\) for a chosen family of observables (typically via clustering bounds).
2. Feed \(\eta\) into Theorem L.4.7 to obtain a spectral gap \(\eta/a\).
3. Track constants uniformly if passing to limits (Appendix M).

