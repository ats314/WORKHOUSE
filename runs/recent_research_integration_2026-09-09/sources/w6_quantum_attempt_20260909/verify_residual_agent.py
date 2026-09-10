"""Exact rational controls for the torus residual obstruction; not Wilson."""
from fractions import Fraction as Q
import json
from pathlib import Path

rows = []
for n in (1, 2, 3, 5, 10, 100, 1000):
    m = n * n
    synthesis = Q(m, 2 * (m + 1))
    gradient = Q(m**3, 2 * (m + 1)**2)
    dual = Q(m**3, 8 * (m + 1)**2 * (m + 4))
    assert synthesis <= Q(1, 2)
    # m >= 1 implies (m+1)^2 <= 4m^2, giving growth >= m/8.
    assert gradient >= Q(m, 8)
    assert gradient <= Q(m, 2)
    assert dual <= Q(1, 8)
    assert (m + 1)**2 * (m + 4) - m**3 == 6*m*m + 9*m + 4
    # Norm of g*n^4/(2(n^2+1))*cos(2k) divided by g^2*b[p].
    hilbert = Q(m**3, 8 * (m + 1)**2)
    assert gradient == 4 * hilbert
    assert dual == hilbert / (m + 4)
    rows.append({"n": n, "synthesis_over_b": str(synthesis),
                 "gradient_over_g2_b": str(gradient),
                 "full_dual_over_g2_b": str(dual)})

out = {"status": "passed", "scope": "exact rational torus-model controls; analytic all-mode proof in residual_agent.md; no Wilson conclusion", "cases": rows}
target = Path(__file__).with_name("residual_agent_checks.json")
target.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
