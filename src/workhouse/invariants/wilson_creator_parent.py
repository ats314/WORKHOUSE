"""Finite exact controls and scalar majorants for the analytic creator parent.

None of these checks machine-certifies the uniform Hilbert-space parent
theorem, a spectral-flow automorphism, or the physical Wilson excitation gap.
"""

from sympy import Rational

from ..wilson_creator_parent import (
    control_cases,
    disjoint_condition_number_control,
    replay_model,
    verify_model,
)
from ._core import _suite

creator_parent_suite = _suite("the Wilson creator parent: exact finite tensor controls")
PROOF = "paper/research_notes/G18_WILSON_CREATOR_PARENT_AND_SPECTRAL_FLOW_20260905.md"


def finite_models():
    """Recompute the six fixed tensor models; no persisted verdict is read."""
    return [verify_model(*case) for case in control_cases()]


def scalar_majorants():
    """Exact substitution in the proof's stated scalar sufficient bounds."""
    a, t = Rational(1, 8), Rational(5, 8)
    m1, k1 = a / 2, a / 4
    value = a * t / (1 - t)
    derivative = a * t / (1 - t) ** 2
    return {
        "a": a,
        "t": t,
        "M1_upper": m1,
        "K1_upper": k1,
        "gap_lower": 1 - k1 - m1**2,
        "cover_path_upper": value,
        "cover_derivative_upper": derivative,
        "cover_total_upper": value + derivative,
    }


@creator_parent_suite.check(
    "six exact finite tensor creator parents have commuting idempotents "
    "and a one-dimensional vacuum",
    "G18; " + PROOF + " section 2; finite dimensions 8, 16, 16, 8, 27 and 12",
)
def _():
    models = finite_models()
    dimensions = [m["hamiltonian_psd"]["dimension"] for m in models]
    ok = dimensions == [8, 16, 16, 8, 27, 12] and all(
        m["commuting_idempotents"]
        and m["exact_similarity"]
        and m["hamiltonian_psd"]["rank"] == m["hamiltonian_psd"]["dimension"] - 1
        and Rational(m["state_norm_squared"]) > 0
        for m in models
    )
    return ok, (
        f"dimensions={dimensions}; direct basis action, local Kronecker products and "
        "disjoint-support creation exponentials agree; vacuum coefficient one and "
        "one-dimensional kernels are exact. These are six finite examples."
    )


@creator_parent_suite.check(
    "81 exact rational PSD congruences independently certify "
    "six finite parent gap and block controls",
    "G18; " + PROOF + " section 2; explicit rational congruences, no numerical eigenvalues",
)
def _():
    models = finite_models()
    replays = [replay_model(model) for model in models]
    count = sum(
        3 + len(m["idempotent_singular_controls"]) + len(m["overlap_commutator_controls"])
        for m in models
    )
    return count == 81 and all(r["success"] for r in replays), (
        f"{count} exact identities M=U.T diag(d) U with d>=0 independently replayed; "
        "each model checks H^2-gH and H-g(I-Psi Psi.T/||Psi||^2), with "
        f"g={[m['g_lower'] for m in models]}. No infinite-volume theorem is certified here."
    )


@creator_parent_suite.check(
    "20 finite idempotent singular bounds and 43 overlap commutator bounds "
    "retain orthogonal support blocks",
    "G18; "
    + PROOF
    + " section 2 equations (2)-(4); exact binary and vector-valued ternary examples",
)
def _():
    models = finite_models()
    singular = sum(len(m["idempotent_singular_controls"]) for m in models)
    overlap = sum(len(m["overlap_commutator_controls"]) for m in models)
    ternary = next(m for m in models if m["name"] == "ternary_vector_creators")
    return singular == 20 and overlap == 43 and ternary["binary_oracle"] is None, (
        f"{singular} identities certify (P.T P)^2-P.T P>=0; {overlap} congruences "
        "certify ||[a_X,a_Y.T]||^2<=||w_X||^2||w_Y||^2 on intersecting supports. "
        "The ternary example keeps multiple excited-vector components and uses no binary oracle."
    )


@creator_parent_suite.check(
    "the stated creator majorants evaluate exactly to gap 247/256 "
    "and cover bounds 5/24, 5/9 and 55/72",
    "G18; " + PROOF + " sections 2 and 3; scalar sufficient-bound arithmetic only",
)
def _():
    values = scalar_majorants()
    ok = (
        values["M1_upper"] == Rational(1, 16)
        and values["K1_upper"] == Rational(1, 32)
        and values["gap_lower"] == Rational(247, 256)
        and values["cover_path_upper"] == Rational(5, 24)
        and values["cover_derivative_upper"] == Rational(5, 9)
        and values["cover_total_upper"] == Rational(55, 72)
    )
    return ok, (
        "At a=1/8,t=5/8: M1<=a/2=1/16, K1<=a/4=1/32; "
        "1-K1-M1^2=247/256; a*t/(1-t)=5/24; a*t/(1-t)^2=5/9; sum=55/72. "
        "This substitutes the analytic proof's premises; it does not establish its operator norms."
    )


@creator_parent_suite.check(
    "exact negative controls reject omitted parent quadratic terms "
    "and a uniform global creator similarity bound",
    "G18; " + PROOF + " sections 1 and 2; six finite witnesses and a factorized one-link family",
)
def _():
    models = finite_models()
    global_control = disjoint_condition_number_control()
    values = [m["negative_control"]["psi_T_H_linear_psi"] for m in models]
    return (
        all(Rational(value) < 0 for value in values)
        and all(m["negative_control"]["vacuum_annihilation_fails"] for m in models)
        and global_control["bound_at_n_8192_exceeds_1000_exactly"],
        f"Omitting sum A_i.T A_i gives negative expectations {values}; "
        "the amplitude-1/32 product family has rooted weight-2 norm 1/16 and "
        "parent gap 1025/1024, but cond(exp(S))>=(1025/1024)^n, exceeding 1000 at n=8192. "
        "The tensor formula is exact; no 2^8192 matrix is constructed.",
    )
