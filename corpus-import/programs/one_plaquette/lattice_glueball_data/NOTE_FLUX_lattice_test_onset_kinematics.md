# Lattice test of the O(y⁴) prediction — the onset is kinematic (independent)

**2026-06-13.** An independent check of the band prediction. Grounds: **[V]** machine-verified here.

## Feasibility framing
A direct exact diagonalization of the SU(3) Kogut–Susskind Hamiltonian is infeasible at the size this
needs: SU(3) is required (SU(2) is real ⇒ no C-odd 1⁺⁻), the O(y⁴) hopping reaches displacement 2 ⇒ L≥4
(~192 links), and each truncated link already carries ~805 states ⇒ Hilbert space ~10⁴⁹ (L=3) to 10¹¹⁶ (L=4).
So a faithful "lattice test" must be an independent strong-coupling computation, not ED.

## What is independently proven here [V]
The prediction's headline feature — **flat through O(y³), first dispersion at O(y⁴)** — is a *kinematic*
fact provable from GF(2) lattice homology alone (no SU(3), no kernel, no pipeline):

1. A magnetic (plaquette) operation toggles a plaquette's 4 boundary links. Hopping a one-plaquette flux
   loop from `p₀` to `p_r` (`p_r≠p₀`) at order k needs k plaquettes `S` with `∂(ΣS)=∂p₀+∂p_r`, i.e.
   `{p₀,p_r}∪S` must be a **closed surface** (2-cycle).
2. **Verified computationally:** the minimal nonempty closed surface in ℤ³ is the **unit cube (6 faces)** —
   exhaustive search finds *no* closed surface with ≤5 plaquettes, and the 6-face cube closes (`∂=0`).
3. ⇒ `|{p₀,p_r}∪S| ≥ 6` ⇒ `|S| ≥ 4`. Repeated plaquettes don't shorten the GF(2) connection. So the
   **leading hopping is order 4** — no dispersion at O(y¹,y²,y³), first dispersion at **O(y⁴)**, realized by
   **cube completion** (apply the other 4 faces of a cube sharing the source face).

This is exactly the band prediction's structural core, derived independently. It also **resolves the
kinematic-vs-dynamical question**: the O(y³) flatness is *kinematic* (a minimal-surface bound), not a
delicate dynamical cancellation.

## What this does and does not test
- **Confirmed independently [V]:** the onset order (flat ≤O(y³), disperse at O(y⁴)) and its geometric
  mechanism (cube completion). The order-4 single-plaquette cube-completion hops populate shells
  `(L1,L∞) = (0,0),(1,1),(2,1)`; the kernel's *cube-state* support is the cube-to-cube generalization,
  reaching `L∞=2`, consistent with the 1⁺⁻ basis being the 6-face cube state.
- **NOT tested here:** the *dynamical* SU(3) content — the exact bandwidth `0.4806`, the `5/48` leakage, the
  band shape (min Γ, max R), and the C-odd-vs-C-even distinction (the kinematic bound is blind to C). These
  require the SU(3) Haar amplitudes + folding, supplied by the verified kernel. An independent
  amplitude-level reconstruction (own SU(3) engine + own folding) is the remaining, harder piece.

## Bottom line
The prediction's **structural claim is independently confirmed** and explained (cube/minimal-surface);
the **quantitative O(y⁴) value** remains anchored to the verified kernel. Reproducible: `kin3.py`.
