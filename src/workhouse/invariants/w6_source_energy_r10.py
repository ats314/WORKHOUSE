"""Exact finite controls for the repaired R10 argument, not a proof of R10.

The analytic implications C1-C5 are registered separately with explicit hypotheses.
These checks detect missing conditional-measure/product-rule terms and power errors.
"""

from __future__ import annotations

import sympy as sp

from ._core import _suite

r10_suite = _suite("W6 R10 repaired identities and counterchecks")
CITE = "W6_SOURCE_ENERGY_JETS_R10"
W, Y = sp.symbols("w y", real=True)


def conditional_derivative_terms(phi, a=sp.S.Half):
    """Return actual, frozen-measure, and covariance derivatives for a finite model.

    Density is (1+a*w*y)/4 on [-1,1]^2; require |a|<1 for strict positivity.
    This model checks the general differentiation rule, not the actual square.
    """
    rho = (1 + a * W * Y) / 4
    marginal = sp.integrate(rho, (Y, -1, 1))
    mean = sp.integrate(sp.expand(phi * rho), (Y, -1, 1)) / marginal
    frozen = sp.integrate(sp.expand(sp.diff(phi, W) * rho), (Y, -1, 1)) / marginal
    # E[Phi B] with B=partial_w log rho, canceling rho before integration.
    covariance = sp.integrate(phi * sp.diff(rho, W), (Y, -1, 1)) / marginal
    covariance -= mean * sp.diff(marginal, W) / marginal
    return tuple(sp.simplify(v) for v in (sp.diff(mean, W), frozen, covariance))


def commutator(a, b):
    return a * b - b * a


def projection_jet_data():
    """Actual and recurrence jets in a normalized positive two-point ground frame."""
    t = sp.Symbol("t", positive=True)
    omega = sp.Matrix([1, t]) / sp.sqrt(1 + t**2)
    inverse_frame = sp.diag(*omega)
    frame = inverse_frame.inv()
    score = (inverse_frame.diff(t) * frame).applyfunc(sp.simplify)
    pi = sp.ones(2, 1) * sp.Matrix([[1, t**2]]) / (1 + t**2)
    p = omega * omega.T
    f = pi
    jets = []
    for n in range(4):
        represented = (inverse_frame * f * frame).applyfunc(sp.simplify)
        jets.append((p.diff(t, n).applyfunc(sp.simplify), represented))
        f = (f.diff(t) + commutator(score, f)).applyfunc(sp.simplify)
    omitted = 2 * inverse_frame * commutator(score, pi.diff(t)) * frame
    return t, jets, omitted.applyfunc(sp.simplify)


@r10_suite.check("W6 R10 repair: conditional measure derivative finite example", CITE + " C1")
def check_conditional_derivative():
    actual, frozen, covariance = conditional_derivative_terms(Y)
    return actual == sp.Rational(1, 6) and actual == frozen + covariance and frozen == 0, (
        "Density (1+w*y/2)/4: d_w E[y|w]=1/6, E[d_w y|w]=0, covariance=1/6. "
        "Exact counterexample to frozen-measure differentiation; actual-model H0 remains open."
    )


@r10_suite.check("W6 R10 repair: centered product retains covariance", CITE + " C2")
def check_centered_product():
    centered = Y - W / 6
    actual, frozen, covariance = conditional_derivative_terms(centered**2)
    return actual == -W / 18 and frozen == 0 and actual == covariance, (
        "For centered y-w/6, d_w E[(y-w/6)^2|w]=-w/18; frozen derivative is zero. "
        "The product conditional derivative retains its covariance; this does not prove H3."
    )


@r10_suite.check(
    "W6 R10 repair: projection recurrence through third derivative finite model", CITE + " C5"
)
def check_projection_recurrence():
    _, jets, _ = projection_jet_data()
    residuals = [(actual - represented).applyfunc(sp.simplify) for actual, represented in jets]
    return all(r == sp.zeros(2) for r in residuals), (
        "Normalized Omega=(1,t)/sqrt(1+t^2): F_(n+1)=F_n'+[sigma,F_n] reproduces "
        "P^(n) exactly for n=0,1,2,3. Finite matrix control only; no uniform energy bound."
    )


@r10_suite.check("W6 R10 repair: omitted projection mixed terms are nonzero", CITE + " C5a")
def check_missing_projection_terms():
    t, _, omitted = projection_jet_data()
    witness = omitted.subs(t, 1)
    return witness == sp.Matrix([[0, -1], [-1, 0]]), (
        "At t=1 in the rational two-point frame, the omitted 2 U^-1[sigma,Pi']U "
        "equals [[0,-1],[-1,0]], not zero. This falsifies the submitted product formula."
    )


@r10_suite.check("W6 R10 repair: diffusion-gap inverse has g^-3 scaling", CITE + " C6a")
def check_diffusion_gap_power():
    g, c, cv = sp.symbols("g c cv", positive=True)
    estimate = sp.simplify((4 * g**-3 * cv * g**2) / (g**2 * c / 2))
    return sp.simplify(estimate - 8 * cv / (c * g**3)) == 0, (
        "Given diffusion gap c and potential fluctuation C_V*g^2, inverse arithmetic is "
        "8*C_V/(c*g^3), not g^-1. No actual fiber gap or forcing estimate is certified."
    )


@r10_suite.check("W6 R10 repair: H2 proposed uniform Young bound fails", CITE + " C6b")
def check_covariance_power_obstruction():
    g, k, v = sp.symbols("g k v", positive=True)
    ratio = sp.simplify(4 * sp.sqrt(32 * k) * g**-4 * sp.sqrt(v) / (g**-2 * (1 + v / g**2)))
    witness = sp.simplify(ratio.subs(v, g**2))
    return witness == 8 * sp.sqrt(2 * k) / g and sp.limit(witness, g, 0, dir="+") == sp.oo, (
        "At v=g^2 the required Young constant is 8*sqrt(2*kappa_0)/g, unbounded at zero. "
        "The scalar implication fails; actual-model H2 is not disproved."
    )
