# Discrete de Rham / Topology Checks + Projection Harness

## 1. Discrete cochain complex sanity: “topology doesn’t lie”

A discrete differential-geometric pipeline can be tested with identity-level checks:

- If \(d_1\) is the discrete exterior derivative from 1-cochains to 2-cochains, and \(d_2\) from 2-cochains to 3-cochains, then the Bianchi identity is:
\[
d_2\circ d_1 = 0.
\]

The simulation outputs report:

- \( \|d_2 d_1\| \) consistent with machine precision (reported max error \(0\) at the displayed precision),
- and a computed first Betti number \(b_1 = 3\), matching \(T^3\) having 3 harmonic one-forms.

In the same block, the smallest positive eigenvalue of the relevant operator matches analytic expectation with ratio \(1.0000\).

**Interpretation:** this is a “computational proof” that the cochain complex and the spectral operator assembly agree with topology and analysis.

---

## 2. Projection as a first-class test: gauge/harmonic modes

A recurring failure mode across the project is interpreting raw spectra without respecting the invariant subspaces:

- gauge modes,
- harmonic modes,
- constraint nullspaces.

The clean unit test is the “slab-cell Hessian” check:

- the raw Hessian has a minimum eigenvalue \(\lambda_{\min}=0\), consistent with gauge zero modes,
- but after projecting to the **physical Maxwell sector**, the minimum eigenvalue becomes:
\[
\lambda_{\min}^{\text{proj}} = 3.5000,
\]
matching the expected value
\[
3\beta + c_H = 3.5000,
\]
with relative error \(\sim 10^{-16}\).

That is about as crisp as numerics get: it tests both the **projector** and the **operator assembly** in one go.

---

## 3. A reusable harness pattern (projection harness)

A general “projection harness” looks like:

1. Build operator \(H\) (Hessian / Laplacian / linearized constraint operator).
2. Identify nullspace \(N\) (gauge, harmonic, constraints).
3. Construct projector \(P\) onto the orthogonal complement (physical subspace).
4. Test:
\[
\lambda_{\min}(PHP) \stackrel{?}{=} \lambda_{\min}^{\text{theory}}.
\]

This pattern is reusable for:

- Maxwell sector checks,
- gauge-fixed YM Hessians,
- coarse-grained operators where nullspaces should be preserved.

---

## 4. What could become a “new theory” direction

The computational message is:

> Many “mysterious” negative or tiny eigenvalues are not physics; they are unprojected structure.

A potentially general research direction is to treat **projection operators** and **cochain/topology structure** as *primary data* in any coarse-graining or RG map.

Conjectural framing:

- Any “RG-like” map \(T\) should satisfy approximate commutation:
\[
T \circ P \approx P' \circ T,
\]
where \(P\) projects onto the physical subspace at the fine scale and \(P'\) at the coarse scale.

Testing this is algorithmic and scalable.

