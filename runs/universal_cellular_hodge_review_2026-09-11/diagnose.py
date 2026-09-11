"""Independent exact diagnostics for the submitted Hodge package.

Run from the repository root with uv run --no-sync python <this path>.
These diagnostics test the manuscript's definitions, not physical Haar histories.
"""

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from workhouse import cellular as cell
from workhouse import kernel_orbits as ko
from workhouse.invariants import hodge_feshbach as hf


def evaluate(poly):
    return sum(c * Fraction(-1) ** sum(e) for e, c in poly.items())


def main():
    boundary = sp.Matrix(cell.TETRAHEDRON.boundary_matrix())
    psi = sp.Matrix(cell.integer_kernel(cell.TETRAHEDRON)[0])
    projector = psi * psi.T / 4
    complement = sp.eye(4) - projector
    face = sp.eye(4)[:, 0]
    assert complement * psi == sp.zeros(4, 1)
    assert complement * face != sp.zeros(4, 1)
    assert boundary * psi == sp.zeros(6, 1)
    columns = [tuple(boundary[:, i]) for i in range(4)]
    zero_flux = (0,) * 6
    witnesses = []
    total = flagged = all_face_flagged = 0
    for word in itertools.product(itertools.product(range(4), (-1, 1)), repeat=4):
        flux = columns[0]
        prefixes = []
        for f, sign in word:
            flux = tuple(a + sign * b for a, b in zip(flux, columns[f], strict=True))
            prefixes.append(flux)
        if flux != columns[1]:
            continue
        total += 1
        flagged_here = any(p in (columns[0], columns[1], zero_flux) for p in prefixes[:-1])
        flagged += flagged_here
        all_face_flagged += any(p in (*columns, zero_flux) for p in prefixes[:-1])
        if flagged_here and len(witnesses) < 2:
            witnesses.append({"word": word, "prefixes": prefixes})
    assert (total, flagged, total - flagged) == (96, 60, 36)

    # Derive commutant dimension from ALL 16 unknown matrix entries and all permutations.
    entries = sp.symbols("x:16")
    unknown = sp.Matrix(4, 4, entries)
    constraints = []
    for perm in itertools.permutations(range(4)):
        action = sp.zeros(4)
        for i, j in enumerate(perm):
            action[i, j] = 1
        constraints.extend(unknown * action - action * unknown)
    coefficient, _ = sp.linear_eq_to_matrix(constraints, entries)
    dimension = 16 - coefficient.rank()
    assert dimension == 2

    identity, down, up, shifted, hopping = hf._ops()
    carrier = hf._psi()
    total_laplacian = ko.combine((1, down), (1, up))
    gens = {"S": shifted, "T": total_laplacian, "U": up, "R": hopping}
    rr = evaluate(hf._sigma("RR", gens, identity, carrier))
    rur = evaluate(hf._sigma("RUR", gens, identity, carrier))
    rsr = evaluate(hf._sigma("RSR", gens, identity, carrier))
    rtr = evaluate(hf._sigma("RTR", gens, identity, carrier))
    q, e2, e3 = map(evaluate, hf._elementary())
    assert (q, e2, e3) == (12, 48, 64)
    assert rsr == (q - 4) * rr - rur
    assert rtr == q * rr
    assert rtr != rsr

    variable = sp.Symbol("q")
    pi4 = sp.expand(sum((-4) ** j * (variable - 4) ** (3 - j) for j in range(4)))
    printed_pi4 = variable**3 - 16 * variable**2 + 112 * variable - 384
    assert pi4 != printed_pi4
    rs4r = evaluate(hf._sigma("RSSSSR", gens, identity, carrier))
    correct_m4 = (q - 4) ** 4 * rr - int(pi4.subs(variable, q)) * rur
    printed_m4 = (q - 4) ** 4 * rr - int(printed_pi4.subs(variable, q)) * rur
    assert rs4r == correct_m4
    assert rs4r != printed_m4

    output = {
        "face_projection": {
            "Q_psi": list(complement * psi),
            "Q_e0": list(complement * face),
            "Q_e0_norm_squared": (face.T * complement * face)[0],
            "B_psi": list(boundary * psi),
            "B_e0": columns[0],
            "scope": "Face-space calculation; no physical history projector is constructed.",
        },
        "flux_enumeration": {
            "total": total, "submitted_return_predicate": flagged,
            "remaining": total - flagged, "any_positive_face_or_zero": all_face_flagged,
            "witnesses": witnesses,
            "scope": "Unweighted additive boundary-flux paths; not Haar/resolvent amplitudes.",
        },
        "commutant_dimension_independent": dimension,
        "master_formula_at_z_minus_one": {
            "q": q, "e2": e2, "e3": e3, "sigma_RR": rr, "sigma_RUR": rur,
            "sigma_R_Scode_R": rsr, "sigma_R_Spaper_R": rtr,
            "S_code": "L_down - 4 I", "S_paper": "L_down + L_up",
            "pi4_correct": str(pi4), "pi4_printed": str(printed_pi4),
            "sigma_RS4R_exact": rs4r, "sigma_RS4R_printed": printed_m4,
        },
    }
    rendered = json.dumps(output, indent=2, default=str) + "\n"
    Path(__file__).with_name("diagnostics.json").write_text(rendered, encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
