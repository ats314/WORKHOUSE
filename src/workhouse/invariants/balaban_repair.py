"""Exact controls for the two proposed repairs to the Balaban multiscale submission.

These check finite algebra and exponent bookkeeping only. The submission's
analytic steps -- the cluster contraction, the inductive limit, OS0-OS4 and the
reconstruction -- are not audited by anything here.
"""

from sympy import Rational, eye, simplify, symbols, zeros

from ._core import _suite

repair = _suite("Balaban submission: the two proposed repairs and what they expose")
CITE = "YM_BALABAN_MULTISCALE; G19"


@repair.check(
    "Scalar interpolation of adjoint values in different fibers is not equivariant",
    CITE + " (3.3) (3.7) R1",
)
def _adjoint_interpolation():
    """The two-cell control that defeats R1 as stated: the penalty density vanishes."""
    # Work in the adjoint (SO(3)) picture, where Ad(g) is an orthogonal matrix and the
    # counterexample is exact in rationals: a rotation by pi about axis 1 sends T3 to -T3.
    ad_g1 = eye(3)
    ad_g2 = zeros(3, 3)
    ad_g2[0, 0] = 1
    ad_g2[1, 1] = -1
    ad_g2[2, 2] = -1
    value = zeros(3, 1)
    value[2] = 1  # the same adjoint value T3 sits at both barycenters
    weight = Rational(1, 2)  # partition-of-unity weights at the midpoint

    plain = weight * value + weight * value
    transformed = weight * (ad_g1 * value) + weight * (ad_g2 * value)
    # Transported interpolation: conjugate both cell values into the frame at x first.
    # Modelled here by applying the SAME group element to both, which is what a common
    # frame achieves; a single factor then comes out of the sum.
    transported = weight * (ad_g2 * value) + weight * (ad_g2 * value)

    density = lambda column: simplify((column.T * column)[0, 0])  # noqa: E731
    return (
        ad_g2.T * ad_g2 == eye(3)
        and (ad_g2 * value) == -value
        and density(plain) == 1
        and density(transformed) == 0
        and density(transported) == 1,
        "Both barycenters carry the adjoint value T3; Ad(g_2) is the rotation by pi about "
        "axis 1, so Ad(g_2)T3=-T3. The scalar interpolation (3.3) with weights 1/2 sends "
        "the Tr|.|^2 penalty density from 1 to 0, a relative residual of 1, so no single "
        "g(x) can relate the interpolated fields and the penalty (3.7) is not gauge "
        "invariant even after R1's background-relative averaging fixes the barycenter "
        "values. Transporting both values into a common frame before averaging restores "
        "the density, which is the surviving variant.",
    )


@repair.check(
    "The small-field curvature threshold sign flip preserves the suppression exponent",
    CITE + " (4.1) (4.6) (5.13) R2",
)
def _threshold_sign():
    """R2: theta^2 rho^4 = g^(2 kappa) under either convention, and (5.13) then closes."""
    g, kappa, c1 = symbols("g kappa c1", positive=True)

    def budget(theta, rho):
        return simplify(theta**2 * rho**4)

    divergent = budget(g ** (-kappa), c1 * g**kappa)  # the document's convention
    small = budget(g**kappa, 1)  # R2, with the radius capped by the cell
    return (
        simplify(divergent / c1**4 - small) == 0
        and simplify(small - g ** (2 * kappa)) == 0
        and simplify(small / g**2 - g ** (2 * kappa - 2)) == 0,
        "With threshold theta a^-2 and half-peak radius rho a, the action budget on the "
        "ball is theta^2 rho^4/(16 g^2). The document takes theta=g^-kappa with "
        "rho=c_1 g^kappa; R2 takes theta=g^+kappa with rho capped at the cell. Both give "
        "theta^2 rho^4 proportional to g^(2 kappa) and hence S >= c g^(-(2-2 kappa)), so "
        "epsilon_0=min(2-2kappa, 2kappa') is untouched. Under R2 equation (3.10) gives "
        "delta <= C_B g^(+kappa)/L^2, which is monotone decreasing in the scale index, so "
        "one condition on g_0 discharges (5.13) at every step instead of failing in the "
        "ultraviolet as it does under the document's sign.",
    )


@repair.check(
    "Restoring the action prefactor makes the coarse subtraction a constant competition",
    CITE + " (4.6) line 176 R2",
)
def _coarse_subtraction():
    """What R2 exposes: both sides of the deficit carry the same power of g."""
    g_k, g_next, kappa, c2 = symbols("g_k g_next kappa c2", positive=True)
    gain = c2 * g_k ** (2 * kappa - 2)  # (4.6), with the 1/(4 g_k^2) prefactor
    cost = Rational(1, 4) * g_next ** (2 * kappa - 2)  # S_(k+1), prefactor restored
    ratio = simplify(gain / cost)
    return (
        simplify(gain / c2 - g_k ** (2 * kappa - 2)) == 0
        and simplify(4 * cost - g_next ** (2 * kappa - 2)) == 0
        and simplify(ratio - 4 * c2 * (g_k / g_next) ** (2 * kappa - 2)) == 0,
        "The document's line after (4.7) compares its gain against "
        "S_(k+1) <= C g_(k+1)^(-2 kappa), which omits the 1/(4 g^2) prefactor its own "
        "action (6.2) carries. Restored, both sides scale as g^(-(2-2 kappa)) and the "
        "net deficit is a competition of constants, not of powers: the ratio is "
        "4 c_2 (g_k/g_(k+1))^(2-2 kappa), whose second factor tends to one under "
        "asymptotic freedom. So epsilon_0=min(2-2kappa, 2kappa') is not established by "
        "that line under either sign convention. This is exposed by R2, not caused by it.",
    )
