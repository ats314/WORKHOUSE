# Exact boundary coupling, memory, and low-energy matching

Research draft, 5 September 2026. This follows the frozen physical-block
package; it does not alter that package or claim a nonlinear Wilson result.
The target is the scale comparison: retain actual boundary coupling while
quantifying the error of replacing an exact history pushforward by a local
coarse oscillator. No smallness of the boundary coupling is assumed.

## 1. An exact finite Gaussian theorem

Let the mass-normalized oscillator have positive squared-frequency matrix

    V = [ C  D ] > 0,
        [ D* F ]

on an orthogonal decomposition of a real finite-dimensional coordinate
space into retained and fiber coordinates. Assume F >= f I, f > 0. The
Euclidean action has Fourier kernel x I + V, x = omega^2 >= 0. Integrating
the fiber coordinates exactly gives the retained kernel

    K(x) = C + x I - D(F+x I)^(-1)D*.

The retained process is generally not Markov. Define

    K0 = C - DF^(-1)D* > 0,
    M  = I + DF^(-2)D* >= I,
    R(x) = DF^(-2)(F+x I)^(-1)D*.

Resolvent algebra, without a series or commutativity assumption involving
D, gives the exact identity

    K(x) = K0 + x M - x^2 R(x).                         (1)

Indeed (F+x I)^(-1) = F^(-1) - x F^(-2)
+ x^2 F^(-2)(F+x I)^(-1). Only functions of F are commuted.
For x >= 0,

    0 <= R(x) <= (M-I)/(f+x),
    K0 + x I + xf/(f+x) (M-I) <= K(x) <= K0 + x M.       (2)

Thus the exact temporal memory begins at the fourth frequency power once
the static Schur potential and the induced mass matrix have both been
retained. Dropping M-I would miss a second-frequency-order term. Neither
an assumption that D is small nor a bound on the number of blocks occurs.

## 2. Exact comparison of the low normal frequencies

Let n be the retained dimension and let mu_1 <= ... <= mu_n be the
eigenvalues of L = M^(-1/2)K0 M^(-1/2). Let lambda_j, 1 <= j <= n,
denote the first n eigenvalues of V, including multiplicities. Then

    f mu_j/(f+mu_j) <= lambda_j <= mu_j.                 (3)

For the upper bound, use the n-dimensional graph trial space
(q,-F^(-1)D*q). Its norm squared is q*Mq and its V form is q*K0q.
The Rayleigh-Ritz min-max principle gives lambda_j <= mu_j.

For the lower bound, take 0 < z < f. Block congruence gives

    n_-(V-z I) = n_-(S(z)),
    S(z) = K0 - z M - z^2 DF^(-2)(F-z I)^(-1)D*.

Since 0 <= M^(-1/2)DF^(-2)(F-z I)^(-1)D*M^(-1/2)
<= I/(f-z),

    M^(-1/2)S(z)M^(-1/2) >= L - zf/(f-z) I.            (4)

If z < f mu_j/(f+mu_j), the right side has at most j-1 strictly
negative eigenvalues. Therefore V has at most j-1 eigenvalues below z.
Let z increase to the endpoint. This proves the lower bound in (3).
It remains valid when mu_j >= f: the comparison endpoint is always < f.
No expansion in z and no isolated-eigenvalue assumption was used.

In particular, for a low effective squared frequency mu_j <= eta f,

    sqrt(mu_j)/sqrt(1+eta) <= sqrt(lambda_j) <= sqrt(mu_j).

The relative frequency error is bounded by
1 - 1/sqrt(1+eta) <= eta/2. The inequality controls the sorted finite
spectrum; identifying a particular degenerate source or channel requires
the corresponding spectral/source argument as well.

## 3. What this repairs in actual history blocking

The exact marginal and the local coarse approximation are different
objects. The exact marginal retains the rational memory (1) and may
contain all full oscillator frequencies, as witnessed by observability
of the retained coordinates. Its OS range need not have the dimension
suggested by a configuration fiber. Equations (1)-(4) give a useful
comparison even when that exact OS complement is zero.

The repaired Gaussian scale task is therefore: prove F >= f for the
chosen geometric split, retain K0 and M, and bound the frequency range
of interest relative to f. These statements compare a true pushforward
to an explicit coarse dynamical model rather than identifying two
different projections.

## 4. Coupled Wilson rectangles and the coordinate boundary

For a planar rectangular Wilson block, the harmonic face co-metric is
K = CC*, where C is the original oriented edge-to-face curl. With the
fundamental SU(N) metric of the frozen package, the harmonic oscillator
has frequency matrix sqrt(u K). In harmonic units, its face Hamiltonian
is (p*Kp + x*x)/2. Fourier exchange of position and momentum puts it in
the mass-normalized form (p*p + q*Kq)/2 used above. This exchange preserves
the common adjoint gauge action but q is the electric dual coordinate;
its literal box average is not automatically a magnetic Wilson history
block. That source and reflection identification must be supplied before
calling it such a block.

The independent boundary-incidence derivation is checking a decomposition
of K into box Neumann forms plus positive boundary/interface forms. If it
establishes QKQ >= kappa_L Q for the mean-zero subspace in boxes of side L,
then f=kappa_L can be used in (1)-(4), uniformly in the number of boxes.
All interfaces remain in C,D,F. This is not a perturbation expansion in
interface couplings.

In physical units, a lower fast frequency of order 1/(La) would make the
relative error at a fixed finite physical target frequency O((La)^2).
That is the desired direction of ultraviolet decoupling. A Wilson theorem
still requires control of the nonlinear terms, the actual generated
measure, the physical clock and sources, and constants along the chosen
scaling trajectory. This Gaussian identity does not supply them.
