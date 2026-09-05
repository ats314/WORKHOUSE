"""Finite partition-extraction controls, separate from the analytic Wilson lemma."""

from sympy import Rational

from ..wilson_activity_extraction import exact_controls, missing_factorization_control
from ._core import _suite

activity_extraction_suite = _suite("the Wilson transfer activities: exact partition extraction")
PROOF = "paper/research_notes/G18_WILSON_ACTIVITY_EXTRACTION_20260905.md"


@activity_extraction_suite.check(
    "partition cumulants reconstruct 32 exact induced tensor transfers "
    "and give 30 vacuum-anchored activities with noncommuting overlaps",
    "G18; " + PROOF + " section 2; two positive four-link rational congruence models",
)
def _():
    models = exact_controls()["models"]
    reconstruction = sum(m["reconstruction_count"] for m in models)
    anchoring = sum(m["vacuum_anchoring_count"] for m in models)
    disconnected = sum(len(m["disconnected_cancellations"]) for m in models)
    commutator = Rational(models[0]["overlap_commutator_frobenius_squared"])
    ok = (
        reconstruction == 32
        and anchoring == 30
        and disconnected == 14
        and all(m["closed_formula_equals_root_block_recursion"] for m in models)
        and commutator == Rational(390963, 51200000000)
        and models[0]["full_activity_nonzero"]
        and not models[1]["full_activity_nonzero"]
    )
    return ok, (
        f"{reconstruction} exact reconstructions, {anchoring} local two-leg vacuum cancellations, "
        f"{disconnected} disconnected-support zeros; "
        f"overlap commutator Frobenius square={commutator}. "
        "Closed partition inversion agrees with a separate root-block recursion "
        "and tensor embedding. "
        "These two finite models do not establish a uniform Wilson activity norm."
    )


@activity_extraction_suite.check(
    "vacuum fixing without component factorization leaves a disconnected "
    "two-link activity of exactly 1/12",
    "G18; " + PROOF + " section 2; missing-factorization negative control",
)
def _():
    control = missing_factorization_control()
    return (
        control["positive_and_vacuum_fixing"]
        and control["component_factorization_fails"]
        and Rational(control["disconnected_activity_11_entry"]) == Rational(1, 12),
        "For G_X=(I+sum_i q_i)^(-1), all matrices are positive and fix the vacuum, "
        "but G_{01}-G_0 tensor G_1=diag(0,0,0,1/12) on two disconnected binary sites. "
        "Thus vacuum fixing alone does not imply disconnected cancellation.",
    )
