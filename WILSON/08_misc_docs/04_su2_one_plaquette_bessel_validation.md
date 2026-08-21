# A hard validation anchor: exact SU(2) one-plaquette partition function and Bessel weights

> **Why include this?**  
> It’s not “new physics,” but it is the kind of exact baseline that prevents re-debugging the same pipeline forever.  
> If your tensor / recoupling machinery can’t reproduce this, nothing downstream is trustworthy.

## 1. The SU(2) one-plaquette integral

Parameterize an SU(2) group element by a class angle \(\phi\in[0,\pi]\):

\[
\mathrm{Tr}\,U = 2\cos\phi.
\]

The Haar measure on SU(2) for class functions reduces to

\[
dU = \frac{2}{\pi}\,\sin^2\phi\; d\phi.
\]

For the standard one-plaquette Wilson weight
\[
w(U)=\exp\!\left(\beta \cos\phi\right),
\]
the exact one-plaquette partition function is

\[
Z_{1}(\beta)
=
\int_{SU(2)} dU\; e^{\beta\cos\phi}
=
\frac{2}{\pi}\int_0^\pi \sin^2\phi\; e^{\beta\cos\phi}\, d\phi.
\]

### Closed form using modified Bessel functions

A standard integral identity gives

\[
\int_0^\pi e^{\beta\cos\phi}\sin^2\phi\; d\phi
=
\pi\,\frac{I_1(\beta)}{\beta},
\]

so

\[
Z_1(\beta) = 2\,\frac{I_1(\beta)}{\beta}.
\]

This is an *exact* number for every \(\beta>0\).

## 2. Character expansion (representation expansion)

The SU(2) character in spin-\(j\) is

\[
\chi_j(\phi) = \frac{\sin((2j+1)\phi)}{\sin\phi}.
\]

Any class function can be expanded in characters:

\[
e^{\beta\cos\phi} = \sum_{j\in\{0,\frac12,1,\dots\}} c_j(\beta)\,\chi_j(\phi).
\]

Orthogonality implies the coefficients are

\[
c_j(\beta)
=
(2j+1)\int dU\; e^{\beta\cos\phi}\,\chi_j(\phi)
\quad (\text{up to convention factors}).
\]

For the Wilson weight, the known result is that these coefficients can be written using modified Bessel functions \(I_{2j+1}(\beta)\) (the exact prefactors depend on the precise normalization of \(\chi_j\) and the action).

## 3. Why this matters for the project pipeline

Your project constructs tensors with local weights that are (in some versions) built from Bessel-function-like character coefficients (or should be).

This gives you multiple non-negotiable unit tests:

1. **Direct integral check:** your code’s lowest-spin / smallest-lattice limit should reproduce \(Z_1(\beta)=2I_1(\beta)/\beta\).
2. **Coefficient consistency:** your numerical \(c_j(\beta)\) must agree with the known \(I_{2j+1}(\beta)\) scaling.
3. **Truncation behavior:** as \(j_{\max}\to\infty\), truncated sums should converge toward the exact result.

If this anchor passes, then:
- HOTRG contraction is less likely to be silently broken,
- θ-dependent generalizations have a stable reference point.

## 4. Practical recipe (minimal pain)

- Start with the one-plaquette (or a 2D analog) where exact results exist.
- Ensure your tensor contraction reproduces \(Z_1(\beta)\) within truncation error.
- Only then turn on θ/q-deformation features.

This sequencing is how you prevent “repeat work forever syndrome.”
