# Structure Formation: Weak–Strong Field Decoupling as a Theorem of the Framework

> Curated extraction from:
> `appendix_r_weak_strong_field_decoupling_in_structure_formation.md`,
> `02.1_Force_Law_and_Asymptotics.md`,
> plus the general screening logic in the convex-Hamiltonian notes.

## 1. The central structural statement

The appendix formalizes a very “engineer-friendly” claim:

> **Nonlinear collapse inside the screening radius is Newtonian.**
>
> Modified dynamics only enters through boundary data / matching to the exterior weak-field region.

This is the kind of separation principle you normally only get in linear systems.

---

## 2. Screening radius and decoupling scale

For a spherical overdensity of mass $M$,
define the screening radius by $g_N(r_s)=a_0$:
\[
\boxed{
r_s(M)=\sqrt{\frac{GM}{a_0}}.
}
\]

The spherical-collapse calculation introduces the key parameter
\[
\boxed{
\epsilon := \frac{a_0}{g_N},
}
\]
with the *strong-field regime* given by $\epsilon\ll 1$ (typical of high redshift and/or large masses).

---

## 3. Collapse time and critical density threshold (analytic scaling laws)

The appendix gives explicit scalings relating VSU collapse observables to GR ones:

\[
\boxed{
t_{\rm coll}^{\rm VSU}
=
t_{\rm coll}^{\rm GR}\,
\epsilon^{1/8},
\qquad
\delta_c^{\rm VSU}
=
\delta_c^{\rm GR}\,
\epsilon^{-1/4}.
}
\]

Equivalently:
\[
\boxed{
\delta_c^{\rm VSU}
=
\delta_c^{\rm GR}\left(\frac{g_N}{a_0}\right)^{1/4}.
}
\]

The interpretation is subtle but important:

- The *nonlinear interior dynamics* stays Newtonian;
- The mapping from linear growth to nonlinear collapse gets rescaled because the exterior field law changes the way boundary conditions feed inward.

---

## 4. Why this is exciting (and nontrivial)

Many modified-gravity models suffer from “double counting”:
they modify linear growth and then modify nonlinear collapse in a way that is inconsistent.

This appendix’s decoupling result says you can run a clean pipeline:

1. Evolve linear growth with $\alpha_{\rm eff}(k,a)$.
2. Use *nearly* standard collapse physics inside $r_s(M)$.
3. Correct only the boundary-to-interior mapping via the derived scalings.

This is computationally and conceptually powerful:
it suggests you can graft VSU onto existing N-body / semi-analytic structure formation codes with minimal surgery.

---

## Further work to expand this

1. **Explicit halo-model prediction for scale-dependent bias** derived from the modified $\delta_c$ scaling.
2. **Environmental screening in cosmological backgrounds**: quantify how $r_s(M)$ shifts with evolving external field strength.
3. **Beyond spherical collapse**: extend the decoupling logic to ellipsoidal collapse (Sheth–Tormen type corrections).
4. **Couple to lensing consistently**: ensure the lensing potential obeys the same screening/decoupling hierarchy (no hidden slip).
