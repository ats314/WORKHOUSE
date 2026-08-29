"""Exact-form identification, the OEIS as an external witness, and their budgets.

Two questions with the same shape, and the same refusal at the centre of each:
what exact form could a recorded float have, and is a coefficient family known
to the OEIS? Both tools always answer, so neither answer counts until it has
been priced. ``src/workhouse/identify.py`` and ``src/workhouse/oeis.py`` carry
the machinery; ADR 0015 records why the gates are shaped the way they are.
"""

from __future__ import annotations

from .. import constants as K
from ._core import ROOT, _suite

# ==========================================================================
identification = _suite("exact-form identification and external witness (C2, G3)")


@identification.check(
    "the Stern-Brocot enumerator agrees with trial division, exactly",
    "src/workhouse/identify.py",
)
def _():
    # The descent that enumerates admissible rationals is output-sensitive and
    # subtle enough to be wrong in a way that looks right -- an off-by-one in
    # the split gap silently drops or double-counts a fraction, and every count
    # downstream inherits it. So it is checked against the algorithm with no
    # cleverness in it, over windows wide enough that both can run.
    from fractions import Fraction as F

    from .. import identify as ident

    rows = []
    for value, half, qmax in (
        (F(1234567, 10000000), F(1, 10000), 800),
        (F(-3, 7), F(1, 1000), 400),
        (F(22, 7), F(1, 100000), 1200),
    ):
        w = ident.Window(float(value), float(half), "controlled")
        clever, truncated = ident.admissible_rationals(w, qmax)
        stupid = ident.brute_force_count(w, qmax)
        rows.append((str(value), qmax, len(clever), stupid, truncated))
    ok = all(a == b and not t for _v, _q, a, b, t in rows)
    return ok, "; ".join(f"{v} q<={q}: {a} vs {b}" for v, q, a, b, _t in rows)


@identification.check(
    "above the saturation denominator every denominator admits a match",
    "C2 / src/workhouse/identify.py",
)
def _():
    # The elementary bound the C2 verdict rests on, and it needs no asymptotics:
    # the admissible numerators for denominator q are the integers in an
    # interval of length 2*h*q, so once 2*h*q >= 1 that interval contains one
    # whatever the value is. Checked in exact rationals, both directions --
    # every denominator at or above the bound has a match, and denominators
    # well below it do not.
    import math
    from fractions import Fraction as F

    from .. import identify as ident

    half = F(1, 10**9)
    w = ident.Window(0.123456789, float(half), "controlled")
    lo, hi = F(w.value) - half, F(w.value) + half
    sat = ident.saturation_denominator(w)

    def has_match(q):
        return math.ceil(lo * q) <= math.floor(hi * q)

    above = all(has_match(q) for q in (sat, sat + 1, sat + 7, 2 * sat, 10 * sat))
    below = sum(1 for q in range(1, 1000) if has_match(q))
    return above and below == 0, (
        f"halfwidth 1/{half.denominator}, saturation denominator {sat:,}: every q in "
        f"{{sat, sat+1, sat+7, 2 sat, 10 sat}} admits a numerator, and {below} of the "
        "999 denominators below 1000 do"
    )


@identification.check(
    "FINDING: the v10a.26 C_shp cannot be identified, and 31 digits would be needed",
    "C2 / G3 / GLUEBALL §10",
    tier=2,
)
def _():
    # The whole answer to "run PSLQ on the float side of C2", stated as an
    # exclusion rather than as a failed search. The window is the reproduction
    # gap, not the half-ulp: the transcript's printed value and the cold rerun
    # are 219 ulps apart, and using the ulp instead would overstate the run's
    # knowledge four hundredfold -- squared, in the ceiling.
    #
    # Neither record is preferred here. C2 stays open, and this check makes the
    # sharper statement that the recorded evidence CANNOT close it: the
    # historical denominator sits three orders of magnitude above the point
    # where every denominator admits a match, so the float excludes nothing.
    from .. import identify as ident

    w = ident.targets()["C_shp"]
    small, _ = ident.admissible_rationals(w, 10**6)
    mid, _ = ident.admissible_rationals(w, 10**8)
    sat = ident.saturation_denominator(w)
    hist_q = K.C_SHP_HISTORICAL.q
    need = ident.digits_required(w.value, hist_q)
    relations = {name: ident.sweep(w, b, limit=3) for name, b in sorted(ident.bases().items())}
    best = max(
        (r for rels in relations.values() for r in rels),
        key=lambda r: r.margin,
        default=None,
    )
    ok = (
        not small
        and hist_q > sat
        and need > w.digits
        and all(r.verdict != "candidate" for rels in relations.values() for r in rels)
    )
    return ok, (
        f"window +-{w.halfwidth:.1e} ({w.provenance}) = {w.digits:.1f} reliable digits; "
        f"no rational with denominator <= 1e6 lies in it, {len(mid)} lie below 1e8, and "
        f"every denominator at or above {sat:,} admits one. The historical C_shp "
        f"denominator {hist_q} is {hist_q / sat:.1f}x past that saturation point, so the "
        f"recorded float excludes no candidate there. Identifying a rational of that "
        f"denominator needs {need:.1f} significant digits against {w.digits:.1f} recorded "
        f"({need - w.digits:.1f} short). Over the {len(relations)} registered bases no "
        f"relation clears its own counting budget -- the best is H = {best.height}, "
        f"expected by counting {best.expected:.2g}, margin {best.margin:+.1f}. "
        "Neither record is preferred here; C2 stays open"
    )


@identification.check(
    "the identifier recovers A = 5/48 uniquely from the same run's float",
    "GLUEBALL §10 / src/workhouse/identify.py",
    tier=2,
)
def _():
    # The positive control, and it is the reason the negative verdict above is
    # about the data rather than about the method. A_shp comes from the SAME
    # v10a.26 run, is recorded the SAME way, and both disputed kernels agree
    # its value is 5/48 -- so the instrument has a known answer to find. It
    # finds it, and finds it alone, at every denominator bound out to 1e9.
    from fractions import Fraction

    from sympy import Rational as R

    from .. import identify as ident

    w = ident.targets()["A_shp"]
    found = {q: ident.admissible_rationals(w, q)[0] for q in (10**3, 10**6, 10**9)}
    want = Fraction(int(K.A_SHP_3.p), int(K.A_SHP_3.q))
    unique = all(v == [want] for v in found.values())
    # ... and the alpha row of the same run, windowed at the four-times bound
    # the registered alpha_new FINDING says it needs, recovers 5/12 the same way.
    a = ident.targets()["alpha_pen"]
    alpha_found, _ = ident.admissible_rationals(a, 10**6)
    alpha_ok = alpha_found == [Fraction(int(R(5, 12).p), int(R(5, 12).q))]
    return unique and alpha_ok, (
        f"A_shp window +-{w.halfwidth:.1e}: the unique admissible rational is {want} at "
        f"q <= 1e3, 1e6 and 1e9 alike, and 5/48 is what both disputed kernels return for "
        f"A. alpha_pen at 4x that bound recovers {alpha_found[0] if alpha_found else None} "
        "alone -- the registered alpha_new finding seen through a second instrument"
    )


@identification.check(
    "the integer-relation false-positive law H ~ 10^(p/n), measured",
    "src/workhouse/identify.py",
    tier=2,
)
def _():
    # Why a relation is not a finding. Over n reals at p reliable digits, LLL
    # ALWAYS returns a relation with coefficients around 10^(p/n) -- the
    # pigeonhole says so and this measures it, on targets with no structure at
    # all.
    #
    # The targets come from SHA-256, not from a linear congruential generator,
    # and that is not fussiness. An LCG's outputs lie on a small number of
    # hyperplanes in n dimensions (Marsaglia), which is to say they satisfy
    # REAL integer relations of small height. Seeding this experiment from one
    # made the measured false-positive height come out an order of magnitude
    # below the law, i.e. it made the guard look far safer than it is. A
    # hash-derived stream has no such structure, and it is byte-reproducible
    # forever, which the `make catalogue` fixpoint needs.
    import hashlib

    from .. import identify as ident

    def draw(tag: str) -> float:
        return int.from_bytes(hashlib.sha256(tag.encode()).digest()[:8], "big") / 2**64 - 0.5

    rows = []
    for n in (3, 4, 5):
        heights = []
        for trial in range(12):
            xs = [draw(f"workhouse:{n}:{trial}:{i}") for i in range(n)]
            rel = ident.lll_relations(xs, 16, limit=1)
            heights.append(max(abs(c) for c in rel[0][0]))
        heights.sort()
        median = heights[len(heights) // 2]
        law = 10 ** (16 / n)
        rows.append((n, median, law, median / law))
    ok = all(0.1 <= ratio <= 10 for _n, _m, _l, ratio in rows)
    return ok, "; ".join(
        f"n={n}: median H {m:.2e} against the law 10^(16/{n}) = {law:.2e} (ratio {r:.2f})"
        for n, m, law, r in rows
    )


@identification.check(
    "flint's exact LLL and mpmath's PSLQ find the same planted relation",
    "src/workhouse/identify.py",
    tier=2,
)
def _():
    # Two engines, because a relation resting on one implementation rests on
    # that implementation's bugs. The lattice reduction is exact integer
    # arithmetic (python-flint, ADR 0010); PSLQ is floating point at raised
    # precision. They are asked for a relation that is really there, and then
    # for one that is not: PSLQ's second answer is an EXCLUSION with a number
    # on it -- a completed search proves no relation of norm below its bound
    # exists at that tolerance, which is worth more than "found nothing".
    import math

    from .. import identify as ident

    planted = [math.pi, math.sqrt(2), 3 * math.pi - 5 * math.sqrt(2)]
    lll = ident.lll_relations(planted, 14, limit=1)[0][0]
    pslq = ident.pslq_relation(planted, 12)

    def norm(v):
        lead = next(c for c in v if c)
        scale = math.gcd(*(abs(x) for x in v if x))
        return tuple(c // scale * (1 if lead > 0 else -1) for c in v)

    agree = pslq["relation"] is not None and norm(lll) == norm(pslq["relation"])
    absent = ident.pslq_relation(
        [ident.targets()["C_shp"].value, math.pi, math.e], 16, maxcoeff=10**5
    )
    excluded = (
        absent["relation"] is None
        and not absent["exhausted"]
        and absent["norm_bound"] is not None
        and absent["norm_bound"] >= 10**5
    )
    # ... and the same search on a step budget too small to finish must NOT be
    # reported as an exclusion: mpmath prints its norm-bound line on the
    # timeout exit too, so the line's presence is not the discriminator.
    starved = ident.pslq_relation(
        [ident.targets()["C_shp"].value, math.pi, math.e], 16, maxcoeff=10**5, maxsteps=2
    )
    return agree and norm(lll) == (3, -5, -1) and excluded and starved["exhausted"], (
        f"planted 3*pi - 5*sqrt(2) - x = 0: flint LLL {lll}, mpmath PSLQ "
        f"{pslq['relation']}, both normalising to {norm(lll)}. Asked the same way for "
        f"C_shp against (pi, e), PSLQ completes and returns nothing, proving no relation "
        f"of norm below {absent['norm_bound']:.6g} exists at 16 digits. The same search "
        f"on a two-step budget reports exhaustion rather than exclusion "
        f"(bound {starved['norm_bound']}), which is the distinction mpmath's own output "
        "does not draw"
    )


@identification.check(
    "FINDING: the v10a.26 side of C2 is one recorded number, not five",
    "C2 / G3 / MASTER_THEORY §5.5",
    tier=2,
)
def _():
    # What an identification attempt has to work with, and it is less than the
    # registry's five float entries suggest. beta_pen_new, the M and R band
    # splits and Delta_C are all exact float functions of C_SHP_NEW_NUM and the
    # agreed A = 5/48 -- bit-for-bit, not to a tolerance. So there is nothing to
    # average, no over-determination, and no second measurement: the float side
    # of C2 carries 13.4 reliable digits, once.
    a = float(K.A_SHP_3)
    derived = {
        "beta_pen_new = 8A + 16C": (8 * a + 16 * K.C_SHP_NEW_NUM, K.BETA_PEN_NEW_NUM),
        "M split = 8 Delta_C": (8 * K.DELTA_C_NUM, K.M_SPLIT_RECORDED_NUM),
        "R split = 16 Delta_C": (16 * K.DELTA_C_NUM, K.R_SPLIT_RECORDED_NUM),
        "Delta_C = C_new - C_old": (
            K.C_SHP_NEW_NUM - float(K.C_SHP_HISTORICAL),
            K.DELTA_C_NUM,
        ),
    }
    exact = {k: (got == want) for k, (got, want) in derived.items()}
    from .. import identify as ident

    digits = ident.targets()["C_shp"].digits
    return all(exact.values()), (
        "bit-for-bit, with no tolerance: "
        + "; ".join(f"{k} {'exact' if v else 'DIFFERS'}" for k, v in sorted(exact.items()))
        + ". Four of the five registered v10a.26 floats are functions of the fifth, so "
        f"the float side of C2 is a single {digits:.1f}-digit datum. Neither record is preferred"
    )


@identification.check(
    "the historical record quantum splits the 189 records 144/45, exactly",
    "C2 / G14 / src/workhouse/kernel_comparison.py",
)
def _():
    # Exact rational arithmetic on the pinned historical certificate alone --
    # no float, no cold run. Every record weight is measured against the
    # degree-3 record quantum X_QUANTUM, and the ones that are NOT integer
    # multiples of it are exactly the 45 records in five displacement classes.
    # The three multiples that do occur are -1, +1 and +2, which is the tier
    # collapse the off-axis ledger already records.
    import collections
    import json
    from fractions import Fraction

    from .. import kernel_comparison as KCMP

    quantum = Fraction(int(K.X_QUANTUM.p), int(K.X_QUANTUM.q))
    kernel = json.loads(KCMP.HIST_CERT.read_text())["kernel"]
    quantised, ragged = {}, collections.Counter()
    for rec in kernel:
        key = (
            tuple(rec["displacement"]),
            tuple(rec["input_plane"]),
            tuple(rec["output_plane"]),
        )
        ratio = Fraction(rec["weight"]) / quantum
        if ratio.denominator == 1:
            quantised[key] = int(ratio)
        else:
            ragged[KCMP.record_class(key)] += 1
    classes = dict(sorted(ragged.items()))
    ok = (
        len(kernel) == 189
        and len(quantised) == 144
        and sum(ragged.values()) == 45
        and set(quantised.values()) == {-1, 1, 2}
        and classes
        == {
            ("diag2", "cross"): 6,
            ("nn", "cross"): 12,
            ("nn", "same"): 18,
            ("onsite", "cross"): 6,
            ("onsite", "same"): 3,
        }
    )
    return ok, (
        f"X_QUANTUM = {quantum}: {len(quantised)} of {len(kernel)} historical record "
        f"weights are integer multiples of it, and they take only the values "
        f"{sorted(set(quantised.values()))}. The {sum(ragged.values())} that are not "
        f"fall in exactly five displacement classes {classes}"
    )


@identification.check(
    "FINDING: the two kernels diverge on exactly the non-quantised sector",
    "C2 / G3 / runs/g3_kernel_record_dump_2026-08-28",
    tier=2,
)
def _():
    # Two independent characterisations of the same 45 records, and they
    # coincide on all 189. The divergent set was found by a FLOAT test (the
    # cold/historical weight ratio departing from the shared scale); the ragged
    # set is EXACT rational arithmetic on the historical certificate, which
    # never sees the cold run at all. So "which records the two kernels
    # disagree on" is a property of the historical certificate's own arithmetic,
    # decidable without running anything -- and the three disputed amplitudes
    # G3 must settle are the ones the record quantum does not reach.
    #
    # This orders neither side. It says where the disagreement lives.
    import json
    from fractions import Fraction

    from .. import kernel_comparison as KCMP

    quantum = Fraction(int(K.X_QUANTUM.p), int(K.X_QUANTUM.q))
    ragged = {
        (
            tuple(r["displacement"]),
            tuple(r["input_plane"]),
            tuple(r["output_plane"]),
        )
        for r in json.loads(KCMP.HIST_CERT.read_text())["kernel"]
        if (Fraction(r["weight"]) / quantum).denominator != 1
    }
    comparison = KCMP.compare()
    divergent = {k for keys in comparison["divergent"].values() for k in keys}
    return ragged == divergent and len(ragged) == 45, (
        f"the {len(divergent)} records where the cold and historical weights depart from "
        f"the shared scale s = {comparison['scale']:.9f} are exactly the {len(ragged)} whose "
        "historical weight is not an integer multiple of the record quantum -- one set "
        "found by float ratio, the other by exact rational arithmetic on the certificate "
        "alone. Symmetric difference is empty on all 189. Neither kernel is preferred"
    )


@identification.check(
    "the sequence register rebuilds its own terms and resolves its own targets",
    "ledger/sequences.yaml",
)
def _():
    # Terms are computed from the registered constants, never transcribed, so a
    # sequence in the register cannot drift away from the numbers it came from.
    # This is the check that says so: every builder resolves, every recorded
    # term list is what the builder returns today, and every bears_on target is
    # a node the catalogue actually has.
    from .. import claims as claims_mod
    from .. import oeis as oeis_mod

    sequences = oeis_mod.load()
    problems = oeis_mod.validate(sequences)
    ids = {c.id for c in claims_mod.load_catalogue()}
    drift, dangling = [], []
    for s in sequences:
        recorded = s.scan.get("terms")
        if recorded is not None and list(recorded) != s.terms:
            drift.append(s.id)
        for target in s.bears_on:
            node = target if claims_mod.LEDGER_ID.fullmatch(target) else f"CONST:{target}"
            if node not in ids:
                dangling.append(f"{s.id} -> {node}")
    ok = not problems and not drift and not dangling
    return ok, (
        f"{len(sequences)} registered sequences, "
        f"{sum(len(s.terms) for s in sequences)} terms rebuilt from the constants; "
        f"validation {problems or 'clean'}, term drift {drift or 'none'}, "
        f"unresolved targets {dangling or 'none'}"
    )


@identification.check(
    "every recorded OEIS verdict is what the gate returns from the recorded evidence",
    "ledger/sequences.yaml",
    tier=2,
)
def _():
    # The register records a verdict; this re-derives it. A change to the
    # evidence gate that would flip a recorded verdict fails here rather than
    # silently rewriting what the repository claims the OEIS said. CI never
    # touches the network or the 32 MB dump: the hits and the chance count are
    # read from the register, and only the JUDGEMENT is recomputed.
    import collections

    from .. import oeis as oeis_mod

    rows, wrong = [], []
    for s in oeis_mod.load():
        scan = s.scan
        if not scan:
            wrong.append(f"{s.id}: no recorded scan")
            continue
        got, _reason = oeis_mod.verdict(s, list(scan.get("hits", ())), scan["expected_by_chance"])
        rows.append((s.id, got))
        if got != scan["verdict"]:
            wrong.append(f"{s.id}: recorded {scan['verdict']}, gate returns {got}")
    tally = collections.Counter(v for _i, v in rows)
    hits = sorted({a for s in oeis_mod.load() for a in s.scan.get("hits", ())})
    return not wrong, (
        f"{len(rows)} recorded verdicts re-derived: {dict(sorted(tally.items()))}. "
        f"{wrong or 'no disagreement'}. The only OEIS entries this corpus reaches are "
        f"{hits}, both of them the polynomial L^3 + 2 registered as the calibration case "
        "-- a hit whose verdict is not-evidence by construction. Every family that could "
        "have carried news returned nothing, which is the expected result and establishes "
        "nothing either way about the coefficients"
    )


@identification.check(
    "the OEIS chance model is corrected past the worst case it was measured against",
    "ledger/sequences.yaml",
    tier=2,
)
def _():
    # "It's in the OEIS" is worth nothing until you know how many things are.
    # The unigram null model treats term values as independent draws and they
    # are not: measured against the snapshot, real sequences beat it by up to
    # 1.2e11, because the Catalan numbers alone sit inside hundreds of entries.
    # The error is one-directional, so the gate is usable only if it carries a
    # correction at least as large as the worst case measured. This is that
    # inequality, and it is what stops the gate certifying a small-integer hit.
    import yaml as _yaml

    from .. import oeis as oeis_mod

    doc = _yaml.safe_load(oeis_mod.REGISTRY.read_text(encoding="utf-8"))
    controls = doc["null_model_controls"]
    ratios = [c["ratio"] for c in controls if c["ratio"]]
    exact = [c for c in controls if not c["ratio"]]
    worst = max(ratios)
    covered = worst <= oeis_mod.CORRELATION_FACTOR
    zero_hits = all(c["observed"] == 0 for c in exact)
    return covered and zero_hits and len(controls) == 9, (
        f"{len(controls)} controls: the model under-counts real sequences by up to "
        f"{worst:.2e} (worst is the eight-term Catalan run) and is exact on the "
        f"{len(exact)} irregular decoys, which is the regime this corpus sits in. "
        f"The gate carries {oeis_mod.CORRELATION_FACTOR:.0e}, above that worst case"
    )


@identification.check(
    "FINDING: the v10a.26 shape fit is shift-invariant only to 4.6e-15",
    "C2 / G3 / notes/imported/HODGE_RUNS_2026-08-28/15_hour_RUN.txt",
    tier=2,
)
def _():
    # Where the digit budget for C_shp comes from, measured inside the run
    # rather than assumed from the printed digits.
    #
    # The transcript prints the same kernel's shape fit twice: section [13]
    # blind, and again after adding an independently linked local scalar shift
    # of 11.17343231638178. A scalar diagonal shift moves the constant term and
    # nothing else -- that is the Phi_C(0) = 0 argument the whole C2 geography
    # rests on -- so `rest` must move by exactly the shift and A, B, C, D must
    # not move at all. `rest` does move by exactly the shift. C moves by
    # 4.6e-15, A by 6.0e-15, alpha by 2.1e-14.
    #
    # So the run knows C to about 12.6 significant digits, not the 17 its repr
    # prints. Every identification ceiling in this suite is computed from that
    # number, and using the printed precision instead would overstate the
    # ceiling by a factor of 50.
    import math
    import re

    path = ROOT / "notes" / "imported" / "HODGE_RUNS_2026-08-28" / "15_hour_RUN.txt"
    text = path.read_text(errors="ignore")

    def field(marker, name):
        block = text[text.rfind(marker) :][:700]
        m = re.search(rf"^\s*{re.escape(name)}\s*=\s*([+-][\d.e+-]+)", block, re.M)
        return float(m.group(1))

    blind, final = "[13] FOLDED AXIAL BLOCH/HODGE SHAPE", "final mass-kernel shape:"
    shift = float(re.search(r"independently linked local shift=\s*([\d.]+)", text).group(1))
    moved = {n: field(final, n) - field(blind, n) for n in ("A", "B", "C_direct", "D", "alpha")}
    rest_moved = field(final, "rest_direct") - field(blind, "rest_direct")
    ok = (
        abs(rest_moved - shift) < 1e-12
        and abs(moved["C_direct"]) > 1e-15
        and all(abs(v) < 1e-13 for v in moved.values())
    )
    known = -math.log10(abs(moved["C_direct"]) / abs(K.C_SHP_NEW_NUM))
    return ok, (
        f"a scalar shift of {shift} moves rest by {rest_moved:.14f} (exactly the shift) "
        f"and must move nothing else; it moves "
        + ", ".join(f"{k} by {v:+.2e}" for k, v in sorted(moved.items()))
        + f". So the run knows C_shp to {known:.1f} significant digits, not the 17 its "
        "repr prints. Both records stand; neither is preferred"
    )


@identification.check(
    "the shape fit's amplitude sensitivities are exact algebraic numbers",
    "C2 / G3 / src/workhouse/kernel_comparison.py",
    tier=2,
)
def _():
    # The 4-point Bloch fit is an exact linear functional of the 189 record
    # weights, so d(coefficient)/d|amplitude| is an exact number and a finite
    # difference recovers it at any step size. Against the closed forms -- the
    # sqrt(5) enters because the fit points sit at 2*pi/5:
    #
    #   ('onsite','cross')    dC = -(5 + 3 sqrt5)/20      dA = 0
    #   ('diag2','cross')     dC = -(5 + 3 sqrt5)/20      dA = 0
    #   ('nn','cross')        dC = +3 sqrt5/10            dA = 0
    #   ('nn-inplane','same') dC = +1/2                   dA = 0
    #   ('nn-normal','same')  dC = -1/2                   dA = +1
    #   ('onsite','same')     dC = 0                      dA = 0
    #
    # Two of these are the load-bearing ones. The on-site anchor moves NOTHING
    # -- not C, not A, not B, not D -- which is ADR 0002 at the level of the
    # fit and is why an exact recomputation of the anchor cannot decide C2.
    # And dA is nonzero for exactly one family, so the agreed A = 5/48 pins
    # that family and no other.
    import math

    from .. import kernel_comparison as KCMP

    root5 = math.sqrt(5)
    want = {
        ("onsite", "cross"): (-(5 + 3 * root5) / 20, 0.0),
        ("diag2", "cross"): (-(5 + 3 * root5) / 20, 0.0),
        ("nn", "cross"): (3 * root5 / 10, 0.0),
        ("nn-inplane", "same"): (0.5, 0.0),
        ("nn-normal", "same"): (-0.5, 1.0),
        ("onsite", "same"): (0.0, 0.0),
    }
    families = KCMP.divergent_families()
    got = KCMP.sensitivities(keys={k for keys in families.values() for k in keys})
    worst = 0.0
    for family, (dc, da) in want.items():
        worst = max(worst, abs(got[family]["C"] - dc), abs(got[family]["A"] - da))
    cross_sum = sum(v["C"] for f, v in got.items() if f[1] == "cross")
    a_carrying = sorted(f for f, v in got.items() if abs(v["A"]) > 1e-9)
    ok = (
        set(got) == set(want)
        and worst < 1e-11
        and abs(cross_sum + 0.5) < 1e-11
        and a_carrying == [("nn-normal", "same")]
    )
    return ok, (
        f"six amplitude families over the 45 disputed records, every sensitivity within "
        f"{worst:.1e} of its closed form; the three cross-plane classes' dC sums to "
        f"{cross_sum:+.12f} = -1/2 exactly; the on-site anchor moves A, B, C and D by zero "
        f"(ADR 0002 at the level of the fit, so recomputing it cannot decide C2); and dA is "
        f"nonzero for exactly one family, {a_carrying[0]}, where it is +1"
    )


@identification.check(
    "FINDING: with A = 5/48 agreed, the C2 dispute is one scalar, not three amplitudes",
    "C2 / G3 / runs/g3_kernel_record_dump_2026-08-28",
    tier=2,
)
def _():
    # The sharpening the sensitivities force, and it narrows what G3 has to buy.
    #
    # Swapping each amplitude family alone from the scale-matched historical
    # kernel to the cold one splits the C difference exactly (the fit is
    # linear, and the parts sum to the whole to 1e-12). Of the four disputed
    # families:
    #
    #   on-site anchor    contributes exactly ZERO to both A and C
    #   nn-normal         is the only family that moves A, with dA/dw = +1, so
    #                     requiring the agreed A = 5/48 fixes it -- and since
    #                     dC/dw = -1/2 there, its C contribution is exactly
    #                     -dA/2, carried rather than chosen
    #   cross-plane and nn-inplane   are what is left, and they enter C only
    #                     through their difference
    #
    # So an independent exact computation of the ON-SITE ANCHOR settles
    # nothing, and one of nn-normal only re-checks A. What decides C2 is the
    # cross-plane amplitude against the nn same-plane in-plane amplitude. That
    # is a correction to G3's step-2 status line, which says any of the three.
    #
    # Neither kernel is preferred: this says where the disagreement lives and
    # how much of it is already determined, not which side is right.
    from .. import kernel_comparison as KCMP

    a = KCMP.attribution()
    parts = a["parts"]
    anchor = parts[("onsite", "same")]
    normal = parts[("nn-normal", "same")]
    free = sum(
        p["dC"] for f, p in parts.items() if f not in (("onsite", "same"), ("nn-normal", "same"))
    )
    inert = abs(anchor["dA"]) < 1e-11 and abs(anchor["dC"]) < 1e-11
    forced = abs(normal["dC"] + normal["dA"] / 2) < 1e-11
    complete = abs(a["total_dC"] - (a["cold"]["C"] - a["base"]["C"])) < 1e-11
    reaches_a = abs(a["base"]["A"] + a["total_dA"] - float(K.A_SHP_3)) < 1e-11
    return inert and forced and complete and reaches_a, (
        f"C_cold - C_scaled-historical = {a['total_dC']:+.12f}, split exactly: "
        f"on-site anchor {anchor['dC']:+.12f} (and dA {anchor['dA']:+.1e}) -- inert; "
        f"nn-normal {normal['dC']:+.12f} = -dA/2 with dA {normal['dA']:+.12f}, which is "
        f"precisely what carries the scaled historical A of {a['base']['A']:.12f} to 5/48; "
        f"cross-plane and nn-inplane leave {free:+.12f} free. One scalar, not three "
        "amplitudes. Both kernels stand; C2 stays open"
    )


@identification.check(
    "FINDING: no disputed amplitude is identifiable from the recorded doubles either",
    "C2 / G3 / src/workhouse/identify.py",
    tier=2,
)
def _():
    # The last place an exact form could have been hiding. Each disputed
    # amplitude is one scalar replicated across its cubic-symmetry images, so
    # the replicate scatter measures how well the cold run knows it -- and the
    # cross-plane amplitude, with 24 replicates, is the best-determined number
    # in the whole dispute. It is still nowhere near enough: the historical
    # amplitudes are exact rationals with denominators up to 2.9e19, and
    # identifying one of those needs about 39 digits.
    #
    # So the answer to "run an integer-relation search on the float side of C2"
    # is the same at every level of the object: the recorded doubles cannot
    # carry an identification. G3's decisive route is an exact recomputation,
    # and this is the precision it has to reach.
    import json
    import math
    from fractions import Fraction

    from .. import identify as ident
    from .. import kernel_comparison as KCMP

    hist = {
        (
            tuple(r["displacement"]),
            tuple(r["input_plane"]),
            tuple(r["output_plane"]),
        ): Fraction(r["weight"])
        for r in json.loads(KCMP.HIST_CERT.read_text())["kernel"]
    }
    parts = KCMP.attribution()["parts"]
    rows = []
    for family, keys in sorted(KCMP.divergent_families().items()):
        part = parts[family]
        spread = max(part["cold_replicate_spread"], math.ulp(part["cold"]))
        w = ident.Window(part["cold"], spread, f"{len(keys)} cubic replicates")
        denominator = hist[keys[0]].denominator
        rows.append(
            (family, len(keys), w.digits, denominator, ident.digits_required(w.value, denominator))
        )
    short = all(need > have for _f, _n, have, _q, need in rows)
    return short, (
        "; ".join(
            f"{f[0]}/{f[1]} ({n} replicates) knows {have:.1f} digits, "
            f"identifying its exact denominator {q:.3g} needs {need:.1f}"
            for f, n, have, q, need in rows
        )
        + ". Every disputed amplitude is short by at least "
        f"{min(need - have for _f, _n, have, _q, need in rows):.0f} digits, so no exact form "
        "is recoverable anywhere in the C2 dispute from what was recorded"
    )
