"""The single-link Dobrushin coefficient of the Wilson action, exactly.

G22's register entry records a second attack on coercivity, separate from the
drift route: "uniform block conditional LSI plus interaction-matrix contraction
q < 1 gives global LSI with (1-q) loss ... No q has ever been computed in the
archive; that computation is a well-posed future check."

This module is that computation, for the **classical single-site (= single-link)
coefficient**. Read the scope note at the bottom before quoting it: the archive's
own template is a *block* coefficient, which is a different quantity.

The setup. For the Wilson action S = beta sum_p (1 - (1/n) Re Tr U_p), the
conditional law of one link given the rest is

    mu_l(dg | rest)  ∝  exp( (beta/n) Re Tr( g St_l ) ) dHaar(g),
    St_l = sum over the plaquettes through l of that plaquette's staple product,

and the Dobrushin coefficient is q = sup_l sum_{l' != l} sup ||mu_l(.|x) -
mu_l(.|x')||_TV over configurations differing only at l'.

Three facts make this computable rather than merely bounded:

1. **The geometry is finite and L-independent.** In d = 4 every link lies in
   2(d-1) = 6 plaquettes, each contributing a 3-link staple, so a link has 18
   neighbours. For L >= 3 those 18 are DISTINCT and each lies in exactly one
   staple, so a single-link change moves exactly one summand of St and all 18
   influences are equal:  q = 18 * sup over St, St' of TV. At L = 2 the count
   collapses to 15 distinct links (wrap-around), which is why L = 2 is
   degenerate and must not be used to calibrate anything.

2. **The supremum is attained at a central flip.** Five SU(3) staples can be made
   to sum to the zero matrix, exactly: A_k = diag(z^k, z^2k, z^-3k) with
   z = exp(2 pi i / 5), k = 0..4. Then setting the sixth staple to 1 or to the
   central element omega = exp(2 pi i / 3) gives St = 1 and St' = omega, so both
   conditionals are class measures.

3. **Class measures reduce to Bessel series.** Weyl integration turns the
   8-dimensional Haar integral into a 2-torus integral, and Jacobi-Anger turns
   that into an exact sum of products of modified Bessel functions -- no
   quadrature anywhere, so arb ball arithmetic certifies it:

       D(z) = sum_{sigma,tau in S3} sgn(sigma tau) sum_{c in Z}
                  prod_j I_{c + sigma(j) - tau(j)}(z),        z = beta / 3
       m(beta) = D'(z) / D(z) = E[ Re Tr g ]  under the tilted class measure.

   D(0) = 6 = |Weyl group| and m(0) = 0 are the structural checks on it.

The bound. With f = Re Tr(g)/3, so ||f||_inf <= 1: under mu' the substitution
h = omega g gives E'[Re Tr g] = Re(omega^2) m = -m/2, hence

    TV >= (1/2) |E f - E' f| = (1/2) |m/3 + m/6| = m/4,   q >= 18 * m/4 = 4.5 m.

SCOPE -- what this does and does not say:

* It is the CLASSICAL SINGLE-SITE coefficient. `EXTRACT_04_pulse_door_block_lsi
  _template.md` defines a *block* coefficient q := max_i sum_{j != i} eps_ij with
  eps_ij a normalised mixed-Hessian operator norm. That is a different quantity,
  and coarse-graining into blocks is the standard way to rescue a Dobrushin
  condition that fails site-by-site. Nothing here touches the block route.
* Dobrushin's condition is SUFFICIENT, not necessary. q >= 1 does not disprove a
  log-Sobolev inequality; it only means this particular lever does not close.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass

from .rigor import arb, ball, bessel_i

#: Spatial dimension of the lattice the corpus works on.
DIM = 4

#: Permutations of the three SU(3) eigenvalue slots, with signs.
_PERMS = list(itertools.permutations(range(3)))


def _parity(perm: tuple[int, ...]) -> int:
    sign, seen = 1, [False] * len(perm)
    for i in range(len(perm)):
        if seen[i]:
            continue
        j, length = i, 0
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            length += 1
        if length % 2 == 0:
            sign = -sign
    return sign


_SGN = {p: _parity(p) for p in _PERMS}


@dataclass(frozen=True)
class LinkGeometry:
    """Staple and neighbour counts for one link, at side length ``L``."""

    staples: int
    distinct_neighbours: int
    neighbours_with_multiplicity: int

    @property
    def degenerate(self) -> bool:
        """True when wrap-around makes two staples share a link."""
        return self.distinct_neighbours != self.neighbours_with_multiplicity


def link_geometry(side: int, dim: int = DIM) -> LinkGeometry:
    """Count the staples through a link and the links they touch. Pure integers."""
    origin = (0,) * dim
    mu = 0

    def shift(vec, axis, step):
        return tuple((v + step) % side if i == axis else v for i, v in enumerate(vec))

    staples = []
    for nu in range(dim):
        if nu == mu:
            continue
        # forward staple around the plaquette in the (mu, nu) plane
        staples.append([(origin, nu), (shift(origin, nu, 1), mu), (shift(origin, mu, 1), nu)])
        # and the backward one
        back = shift(origin, nu, -1)
        staples.append([(back, nu), (back, mu), (shift(back, mu, 1), nu)])
    touched = [link for staple in staples for link in staple]
    return LinkGeometry(len(staples), len(set(touched)), len(touched))


def weyl_bessel_mean(beta_num: int, beta_den: int, cutoff: int = 12) -> arb:
    """``E[Re Tr g]`` under the class measure tilted by ``exp((beta/3) Re Tr g)``.

    Certified: every quantity is an arb ball, so the returned enclosure carries
    its own error bound rather than a hoped-for precision. ``cutoff`` truncates
    the Fourier index of the periodic delta; the summand falls off like
    ``(z/2)^|c| / |c|!``, so the value is stable long before c = 12 (it agrees to
    every printed digit with c = 24, and with an independent 2-D quadrature).
    """
    z = ball(beta_num) / ball(3 * beta_den)
    lo, hi = -cutoff - 4, cutoff + 4
    bessel = {n: bessel_i(n, z) for n in range(lo, hi + 1)}
    # I_n'(z) = (I_{n-1}(z) + I_{n+1}(z)) / 2
    deriv = {n: (bessel[n - 1] + bessel[n + 1]) / 2 for n in range(lo + 1, hi)}
    total = ball(0)
    total_deriv = ball(0)
    for sigma in _PERMS:
        for tau in _PERMS:
            sign = _SGN[sigma] * _SGN[tau]
            for c in range(-cutoff, cutoff + 1):
                idx = [c + sigma[j] - tau[j] for j in range(3)]
                a, b, d = (bessel[i] for i in idx)
                total += sign * a * b * d
                total_deriv += sign * (
                    deriv[idx[0]] * b * d + a * deriv[idx[1]] * d + a * b * deriv[idx[2]]
                )
    return total_deriv / total


def weyl_partition(beta_num: int, beta_den: int, cutoff: int = 12) -> arb:
    """The same series' denominator ``D(z)``. ``D(0)`` must enclose 6 = |Weyl group|."""
    z = ball(beta_num) / ball(3 * beta_den)
    lo, hi = -cutoff - 4, cutoff + 4
    bessel = {n: bessel_i(n, z) for n in range(lo, hi + 1)}
    total = ball(0)
    for sigma in _PERMS:
        for tau in _PERMS:
            sign = _SGN[sigma] * _SGN[tau]
            for c in range(-cutoff, cutoff + 1):
                idx = [c + sigma[j] - tau[j] for j in range(3)]
                total += sign * bessel[idx[0]] * bessel[idx[1]] * bessel[idx[2]]
    return total


def dobrushin_lower_bound(beta_num: int, beta_den: int, cutoff: int = 12) -> arb:
    """Certified lower bound ``q >= 4.5 m(beta)`` for the single-link coefficient."""
    return (ball(9) / 2) * weyl_bessel_mean(beta_num, beta_den, cutoff)
