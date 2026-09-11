"""The planar limit of the fourth-order band: every cumulant, every channel, exactly.

Reads the Q(N) closed forms of runs/beta_n_symbolic_rank_2026-09-04 and the
channel decomposition of runs/channels_symbolic_rank_2026-09-04 and derives
their large-N laws by exact rational arithmetic (sympy). Writes
certificate.json next to itself.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from sympy import (Poly, Rational, Symbol, cancel, degree, diff, fraction, nroots,
                   real_roots, series, sympify, together, factor)

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
N = Symbol("N")
inv = Symbol("inv", positive=True)
ORDER = 14  # expand through N**-13


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def rf(text):
    return sympify(text, locals={"N": N})


def leading(expr):
    """(power, coefficient) of the leading large-N term, exactly."""
    num, den = fraction(cancel(together(expr)))
    pn, pd = Poly(num, N), Poly(den, N)
    return pn.degree() - pd.degree(), Rational(pn.LC(), pd.LC())


def expansion(expr, order=ORDER):
    s = series(cancel(expr).subs(N, 1 / inv), inv, 0, order).removeO()
    return {k: s.coeff(inv, k) for k in range(order) if s.coeff(inv, k) != 0}


def real_roots_at_least(poly_expr, lo):
    p = Poly(poly_expr, N)
    if p.degree() <= 0:
        return []
    return [r for r in real_roots(p) if r >= lo]


out = {"schema": "planar_band/v1", "field": "Q(N)", "basis": "the kernel's (0,2), C-odd unless named even"}

# ---------------------------------------------------------------- closed forms
forms = load("runs/beta_n_symbolic_rank_2026-09-04/closed_forms.json")["forms"]
F = {k: rf(v["factored"]) for k, v in forms.items()}
F["alpha"] = rf("640/(N*(N-1)**3*(N+1)**3)")
F["W4"] = F["alpha"] + F["beta_assembled"]
F["hop_A"] = rf("-2*N**3/((N - 1)*(N + 1)*(2*N**2 - 1))")
F["hop_B"] = rf("-4*N*(N**2 - 2)/((N - 1)*(N + 1)*(2*N - 3)*(2*N + 3))")
out["forms"] = {}
for k, e in F.items():
    p, c = leading(e)
    ex = expansion(e)
    out["forms"][k] = {"leading_power": p, "leading_coefficient": str(c),
                       "expansion_in_1_over_N": {str(kk): str(v) for kk, v in ex.items()}}
    print(f"{k:22s} ~ {c} * N^{p}   next: {[str(ex[kk]) for kk in sorted(ex)[1:3]]}")

# the planar decomposition of beta: beta = -16 u + 32 d - 16 corner + 848/(N(N^2-1)^3)
u_inf = leading(F["u_odd"])[1]
d_inf = leading(F["single_perp_odd"])[1]
c_inf = leading(F["corner_odd"])[1]
assembled = -16 * u_inf + 32 * d_inf - 16 * c_inf + 848
beta_inf = leading(F["beta_assembled"])[1]
out["planar_decomposition"] = {
    "u_odd": str(u_inf), "single_perp_odd": str(d_inf), "corner_odd": str(c_inf), "cube_848": "848",
    "-16u+32d-16corner+848": str(assembled), "beta_leading": str(beta_inf), "equal": assembled == beta_inf,
    "share_of_beta": {"-16u": str(-16 * u_inf / beta_inf), "32d": str(32 * d_inf / beta_inf),
                      "-16corner": str(-16 * c_inf / beta_inf), "848": str(848 / beta_inf)},
}
print("planar decomposition", out["planar_decomposition"])
# corpus comparison
out["corpus"] = {"beta_N7": str(beta_inf), "corpus_6170_9": beta_inf == Rational(6170, 9),
                 "beta_N9": str(expansion(F["beta_assembled"]).get(9)),
                 "corpus_677903_324": expansion(F["beta_assembled"]).get(9) == Rational(677903, 324),
                 "W4_N7": str(leading(F["W4"])[1]), "corpus_11930_9": leading(F["W4"])[1] == Rational(11930, 9)}
print("corpus", out["corpus"])

# ---------------------------------------------------------------- sign and monotonicity
mono = {}
for k in ("beta_assembled", "u_odd", "single_perp_odd", "corner_odd", "W4", "C_shp"):
    e = F[k]
    p = leading(e)[0]
    num, den = fraction(cancel(together(e)))
    scaled = cancel(N ** (-p) * e)  # tends to a nonzero constant
    dnum, _ = fraction(cancel(together(diff(scaled, N))))
    mono[k] = {
        "numerator_real_roots_ge_3": [str(r) for r in real_roots_at_least(num, 3)],
        "denominator_real_roots_ge_3": [str(r) for r in real_roots_at_least(den, 3)],
        "derivative_of_N^-p_form_real_roots_ge_3": [str(r) for r in real_roots_at_least(dnum, 3)],
        "N^-p form at N=3,5,20,1000": [str(scaled.subs(N, n)) for n in (3, 5, 20, 1000)],
        "limit": str(leading(e)[1]),
    }
    print(k, mono[k])
out["sign_and_monotonicity"] = mono

# ---------------------------------------------------------------- tau form
# u = beta/(2N) (constants: u = beta/6 at SU(3)); W_2 = 12 t_N u^2; W_4 = (alpha+beta) u^4.
t_inf = leading(F["hop_odd"])[1]  # kernel-basis hop is -t_N; use |.|
W4_inf = leading(F["W4"])[1]
ratio_coeff = W4_inf / (12 * abs(t_inf)) / 4  # W4 u^4 / (W2 u^2) = W4/(12 t) * beta^2/(4 N^2), times N^-7+3
out["tau_form"] = {
    "u_bridge": "u = beta/(2N)", "W2": "12 t_N u^2", "W4": "(alpha_N + beta_N) u^4",
    "W4/W2 = c tau^2 (1+O(N^-2)), tau = beta/N^3, c": str(ratio_coeff),
    "exact_ratio_function_of_N": str(factor(cancel(F["W4"] / (12 * (-F["hop_odd"])) * N**4 / 4))),
}
print("tau", out["tau_form"])

# ---------------------------------------------------------------- channels
# Fast exact 1/N expansion of a rational function: reversed polynomials and
# truncated power-series division over Q (sympy's series is too slow for the
# 1,400 channel forms).
from fractions import Fraction


def coeff_list(poly_expr):
    p = Poly(poly_expr, N)
    return [Fraction(int(c.p), int(c.q)) for c in p.all_coeffs()]  # highest degree first


def inv_expansion(expr, terms=6):
    """Return (leading_power, [c0, c1, ...]) with expr = N**power * sum c_j N**(-j)."""
    num, den = fraction(cancel(together(expr)))
    a, b = coeff_list(num), coeff_list(den)
    power = (len(a) - 1) - (len(b) - 1)
    a = a + [Fraction(0)] * terms
    b = b + [Fraction(0)] * terms
    q = []
    for j in range(terms):
        cj = a[j] - sum(q[i] * b[j - i] for i in range(j))
        q.append(cj / b[0])
    return power, q


def label_shape(label):
    """(kind, number of intermediate states, number of states carrying a nontrivial irrep)."""
    kind = label.split()[0]
    states = label[len(kind):].strip()
    parts = [p.strip() for p in states.split(")") if p.strip()]
    nontrivial = sum(0 if p.endswith(", -") else 1 for p in parts)
    return kind, len(parts), nontrivial


cert = load("runs/channels_symbolic_rank_2026-09-04/certificate.json")
chan_out = {}
rule_ok = True
for cl, rec in cert["clusters"].items():
    row = {}
    for sector in ("odd", "even"):
        total = rf(rec[f"sum_{sector}"])
        tp, tq = inv_expansion(total, 4)
        chan_sum = 0
        entries = []
        for label, ch in rec["channels"].items():
            d = ch[sector] if isinstance(ch[sector], dict) else eval(ch[sector], {}, {})
            e = rf(d["factored"])
            chan_sum += e
            if e == 0:
                continue
            p, q = inv_expansion(e, 6)
            entries.append((label, p, q))
        assert cancel(chan_sum - total) == 0  # the channels sum to the cumulant: an identity in Q(N)
        pmax = max(p for _, p, _ in entries)
        # total coefficient of N**-3, N**-5, N**-7 grouped by the channels' own leading power
        grouped = {}
        for label, p, q in entries:
            for j, c in enumerate(q):
                power = p - j
                if power < -7 or c == 0:
                    continue
                grouped.setdefault(str(power), {}).setdefault(str(p), Fraction(0))
                grouped[str(power)][str(p)] += c
        totals = {pw: str(sum(v.values())) for pw, v in grouped.items()}
        # label rule: leading power = -3 - 2*(number of intermediate states carrying no irrep), capped at -7
        rule_fail = [(label, p, label_shape(label)) for label, p, _ in entries
                     if p != max(-7, -3 - 2 * (label_shape(label)[1] - label_shape(label)[2]))]
        rule = not rule_fail
        rule_ok = rule_ok and rule
        by_power = {}
        for label, p, q in entries:
            by_power.setdefault(p, []).append(label)
        row[sector] = {
            "channels_nonzero": len(entries),
            "cumulant_leading_power": tp, "cumulant_leading_coefficient": str(tq[0]),
            "cumulant_next_coefficients": [str(c) for c in tq[1:3]],
            "max_channel_power": pmax,
            "cancelled_orders": (pmax - tp) // 2,
            "channels_by_leading_power": {str(p): len(v) for p, v in sorted(by_power.items(), reverse=True)},
            "coefficient_totals_by_power": totals,
            "coefficient_totals_grouped_by_channel_leading_power": {pw: {k: str(v) for k, v in g.items()} for pw, g in grouped.items()},
            "label_rule_leading_power_is_-3-2*(states without irrep)_capped_-7": rule,
            "label_rule_failures": rule_fail[:12],
            "channels_leading_at_-7": [l for l, p, _ in entries if p == -7],
        }
        print(cl, sector, {k: v for k, v in row[sector].items() if k not in ("channels_leading_at_-7",)})
    chan_out[cl] = row
out["channels"] = chan_out
out["channel_label_rule_holds_everywhere"] = rule_ok
out["second_order"] = {"A_N": out["forms"]["hop_A"], "B_N": out["forms"]["hop_B"], "t_N": out["forms"]["hop_perp_odd"],
                       "cancelled_orders": 1}
out["pattern"] = {"order_2": {"channel_content": -1, "coefficient": -3},
                  "order_4": {"channel_content": -3, "coefficient": -7},
                  "law": "order 2k: channel content N^-(2k-1), k cancelled orders, coefficient N^-(4k-1); verified k=1,2"}
(HERE / "certificate.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print("written")
