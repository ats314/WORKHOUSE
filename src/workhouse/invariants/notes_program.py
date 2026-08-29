from __future__ import annotations

from sympy import (
    Matrix,
    Rational,
    cos,
    diff,
    expand,
    eye,
    pi,
    series,
    simplify,
    sin,
    sqrt,
    symbols,
    zeros,
)

from ._core import _suite

# ==========================================================================
notes_prog = _suite("notes program: SAFE, Davies, coercivity (G20-G23)")


@notes_prog.check(
    "G21 exponent identity: arcosh(1 + 2x^2) = 2 arsinh(x)",
    "notes review 2026-08-22 / G21",
)
def _():
    from sympy import acosh, asinh, cosh, expand_trig

    x = symbols("x", positive=True)
    # acosh is monotone on [1, oo) and 2 asinh(x) >= 0, so the identity holds
    # iff cosh(2 asinh(x)) = 1 + 2x^2 — which is the double-angle formula
    # cosh(2t) = 1 + 2 sinh(t)^2 evaluated at t = asinh(x). sympy closes that
    # form directly where the acosh difference resists simplification.
    residual = simplify(expand_trig(cosh(2 * asinh(x))) - (1 + 2 * x**2))
    small = series(acosh(1 + 2 * x**2), x, 0, 2).removeO()
    return residual == 0 and simplify(small - 2 * x) == 0, (
        f"cosh(2 asinh x) - (1+2x^2) = {residual} with both sides' arguments nonnegative, "
        f"so acosh(1+2x^2) = 2 asinh(x); leading order {small} = 2x, "
        "so the Davies exponent is O(m), not O(m^2) — the identity the G21 bound rides on"
    )


@notes_prog.check(
    "V_Haar Hessian at the identity is exactly I/4 (adjoint Casimir 3)",
    "notes review 2026-08-22 / G20",
)
def _():
    from sympy import I as i_unit
    from sympy import im, trace

    # Gell-Mann matrices, exact; T_a = i lambda_a / 2 is orthonormal under
    # <A,B> = -2 Re Tr(AB) — the archive code's own normalization.
    s3 = sqrt(3)
    lam = [
        Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        Matrix([[0, -i_unit, 0], [i_unit, 0, 0], [0, 0, 0]]),
        Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        Matrix([[0, 0, -i_unit], [0, 0, 0], [i_unit, 0, 0]]),
        Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        Matrix([[0, 0, 0], [0, 0, -i_unit], [0, i_unit, 0]]),
        Matrix([[1 / s3, 0, 0], [0, 1 / s3, 0], [0, 0, -2 / s3]]),
    ]
    T = [i_unit * m / 2 for m in lam]

    def inner(a: Matrix, b: Matrix):
        return simplify(-2 * ((trace(a * b)) - i_unit * im(trace(a * b))))

    ortho = all(inner(T[a], T[b]) == (1 if a == b else 0) for a in range(8) for b in range(8))
    f = {}
    for a in range(8):
        for b in range(8):
            comm = T[a] * T[b] - T[b] * T[a]
            for c in range(8):
                v = inner(comm, T[c])
                if v != 0:
                    f[(a, b, c)] = v
    # Adjoint Casimir: sum_cd f_acd f_bcd = 3 delta_ab, so -tr(ad_X^2) = 3|x|^2,
    # log J = -sum theta_k^2 / 24 + O(4), V_Haar = |x|^2 * (3/24) = |x|^2 / 8.
    casimir_ok = True
    for a in range(8):
        for b in range(8):
            s = sum(f.get((a, c, d), 0) * f.get((b, c, d), 0) for c in range(8) for d in range(8))
            if simplify(s - (3 if a == b else 0)) != 0:
                casimir_ok = False
    coeff = Rational(3, 24)
    ok = ortho and casimir_ok and coeff == Rational(1, 8) and 2 * coeff == Rational(1, 4)
    return ok, (
        "T_a orthonormal under -2ReTr; sum_cd f_acd f_bcd = 3 delta_ab exactly, so "
        "-tr(ad_X^2) = 3|x|^2 and V_Haar = |x|^2/8 + O(|x|^4): Hessian(0) = I/4. This is "
        "the only well-defined constant in the SAFE ledger, and it equals 1/4 — not the "
        "draft's 0.291 (a reverse-fitted normalization artifact, see the notes register)"
    )


@notes_prog.check(
    "FINDING: the alpha^n RG iteration contradicts its own one-step bound",
    "notes review 2026-08-22 / G20",
)
def _():
    kappa, delta = Rational(1, 4), Rational(6, 1000)
    alpha = 1 - delta / kappa
    subtractive_100 = kappa - 100 * delta
    multiplicative_100 = alpha**100 * kappa
    ok = (
        alpha == Rational(122, 125)
        and subtractive_100 == Rational(-7, 20)
        and subtractive_100 < 0 < multiplicative_100
    )
    return ok, (
        f"one-step bound is subtractive (kappa - delta), so 100 steps give "
        f"kappa - 100 delta = {subtractive_100} < 0 (zero crossed at step "
        f"{kappa / delta} = 41.67); the boxed multiplicative form alpha = {alpha} gives "
        f"alpha^100 kappa = {float(multiplicative_100):.4f} > 0 forever. The two are "
        "inconsistent and no archive document derives the multiplicative one"
    )


@notes_prog.check(
    "FINDING: six bounded vectors in R^3 refute the 6-vs-3 Cartan counting",
    "notes review 2026-08-22 / G22",
)
def _():
    e1, e2, e3 = Matrix([1, 0, 0]), Matrix([0, 1, 0]), Matrix([0, 0, 1])
    six = [e1, -e1, e2, -e2, e3, -e3]
    total = sum(six, zeros(3, 1))
    span = Matrix.hstack(*six).rank()
    ok = total == zeros(3, 1) and span == 3
    return ok, (
        "three orthogonal antipodal unit pairs: sum = 0 with the six directions spanning "
        "all of R^3 (rank 3) — zero force with no common Cartan direction, so 'small sum "
        "implies near-alignment' is false for six vectors, and stationarity at a link is 3 "
        "scalar equations, not 6. G22's conjecture must rest on gauge coupling, not this "
        "counting"
    )


@notes_prog.check(
    "center elements are critical points of Re Tr, with exact heights",
    "notes review 2026-08-22 / G20",
)
def _():
    from sympy import I as i_unit
    from sympy import re

    a, b, c = symbols("a b c")
    x2 = Matrix([[a, b], [c, -a]])  # generic traceless 2x2
    d_su2 = simplify(re((-eye(2) * x2).trace()))
    phi_su2 = 1 - Rational(1, 2) * re((-eye(2)).trace())
    om = cos(2 * pi / 3) + i_unit * sin(2 * pi / 3)
    x3 = Matrix(3, 3, lambda r, s: symbols(f"y{r}{s}"))
    x3[2, 2] = -x3[0, 0] - x3[1, 1]  # traceless
    d_su3 = simplify((om * x3).trace())
    phi_su3 = simplify(1 - Rational(1, 3) * re(3 * om))
    ok = (
        d_su2 == 0
        and phi_su2 == 2
        and simplify(d_su3 - om * (x3[0, 0] + x3[1, 1] + x3[2, 2])) == 0
        and phi_su3 == Rational(3, 2)
    )
    return ok, (
        f"d/dt ReTr(-I e^(tX))|_0 = -ReTr(X) = 0 for traceless X, phi(-I) = {phi_su2} "
        f"(SU(2)); Tr(omega X) = omega TrX = 0, phi(omega I) = {phi_su3} (SU(3)) — the "
        "center sectors are large-height critical points, so the action-built Lyapunov "
        "candidates genuinely fail there; the universal impossibility claim stays out"
    )


@notes_prog.check(
    "G21 Davies bound verified on the 3x3 periodic 2D lattice, arb-certified",
    "notes review 2026-08-22 / G21",
    tier=2,
)
def _():
    # M = m^2 I + d1^T d1 on 1-forms of the 3x3 periodic square lattice
    # (m^2 = alpha = 1), G = M^-1 exact; assert |G(b,b')| < (2/m^2) e^{-eta d}
    # for every pair, with eta = arcosh(1 + m^2/(2 alpha D_E)) evaluated in
    # certified ball arithmetic (ADR 0010) — the comparison is provable, not
    # approximate.
    from .. import rigor

    L = 3
    links = [(x, y, mu) for x in range(L) for y in range(L) for mu in (0, 1)]
    idx = {b: i for i, b in enumerate(links)}
    plaqs = [(x, y) for x in range(L) for y in range(L)]
    d1 = zeros(len(plaqs), len(links))
    for p, (x, y) in enumerate(plaqs):
        d1[p, idx[(x, y, 0)]] += 1
        d1[p, idx[((x + 1) % L, y, 1)]] += 1
        d1[p, idx[(x, (y + 1) % L, 0)]] -= 1
        d1[p, idx[(x, y, 1)]] -= 1
    M = eye(len(links)) + d1.T * d1
    G = M.inv()

    # link graph: adjacent iff they co-bound a plaquette
    co = {i: set() for i in range(len(links))}
    for p in range(len(plaqs)):
        members = [i for i in range(len(links)) if d1[p, i] != 0]
        for i in members:
            for j in members:
                if i != j:
                    co[i].add(j)
    d_e = max(len(v) for v in co.values())

    def bfs(src: int) -> dict[int, int]:
        dist, frontier = {src: 0}, [src]
        while frontier:
            nxt = []
            for u in frontier:
                for v in co[u]:
                    if v not in dist:
                        dist[v] = dist[u] + 1
                        nxt.append(v)
            frontier = nxt
        return dist

    eta = rigor.ball(1) + rigor.ball(Rational(1, 2 * d_e))
    eta = eta.acosh()
    worst = None
    certified = True
    for i in range(len(links)):
        dist = bfs(i)
        for j in range(len(links)):
            ratio = abs(rigor.ball(G[i, j])) / (rigor.ball(2) * (-eta * dist[j]).exp())
            if not rigor.certified_lt(ratio, rigor.ball(1)):
                certified = False
            if worst is None or float(ratio.mid()) > float(worst.mid()):
                worst = ratio
    return certified and d_e == 6, (
        f"18 links, D_E = {d_e}, eta = {rigor.describe(eta)}; every |G(b,b')| is provably "
        f"below (2/m^2) e^(-eta dist) in 128-bit ball arithmetic, worst ratio "
        f"{rigor.describe(worst)} — the review's 6x6 margin (<= 0.31) reproduced here as a "
        "standing certified check at m^2 = alpha = 1"
    )


@notes_prog.check(
    "one-step bridge spectral lemma: inf over the orthocomplement is 1 - lambda_1",
    "notes review 2026-08-22 / G23 (Exciting_03 Lemma 3.1)",
)
def _():
    # T = e^{-aH} on a finite spectrum, exactly: with T = diag(1, t1, t2),
    # 1 > t1 >= t2 > 0 and Omega the first basis vector, the constrained
    # infimum of <psi,(I-T)psi> over psi perp Omega, |psi| = 1, is 1 - t1.
    t1, t2 = Rational(3, 4), Rational(1, 5)
    a, b = symbols("a b", real=True)
    psi = Matrix([0, a, b])
    q = expand((psi.T * (eye(3) - Matrix.diag(1, t1, t2)) * psi)[0, 0])
    # q = (1-t1) a^2 + (1-t2) b^2 with a^2 + b^2 = 1: minimum at b = 0.
    at_min = q.subs({a: 1, b: 0})
    general = expand(q - ((1 - t1) * (a**2 + b**2) + ((1 - t2) - (1 - t1)) * b**2))
    ok = at_min == 1 - t1 and general == 0 and (1 - t2) - (1 - t1) > 0
    return ok, (
        f"q = (1-t1)(a^2+b^2) + (t1-t2) b^2 exactly, so inf = 1 - t1 = {1 - t1} at the "
        "second eigenvector -- the verified spectral lemma that reduces G23's bridge to "
        "the single bottleneck inequality (4.3)"
    )


@notes_prog.check(
    "FINDING: the naive diffusion-to-OS bridge fails in the Gaussian model",
    "notes review 2026-08-22 / G23 (06_toy)",
    tier=2,
)
def _():
    from .. import rigor

    # 1D Gaussian chain: lambda_diff = m^2, exact transfer gap
    # omega = arccosh(1 + m^2/2). Naive bridge claims Delta >= lambda_diff.
    # At m^2 = 4: omega = arccosh(3) < 4 -- certified strict violation.
    # At m^2 = 1/4: omega/lambda ~ 1.98 -- the ratio is not constant, and
    # omega tracks sqrt(lambda) (continuum dispersion), the toy's point.
    om4 = rigor.ball(3).acosh()
    om_quarter = (rigor.ball(1) + rigor.ball(Rational(1, 8))).acosh()
    violated = rigor.certified_lt(om4, rigor.ball(4))
    also_below_sqrt = rigor.certified_lt(om4, rigor.ball(2))
    ratio_small_m = om_quarter / rigor.ball(Rational(1, 4))
    near_two = rigor.certified_lt(abs(ratio_small_m - 2), rigor.ball(Rational(3, 100)))
    return violated and also_below_sqrt and near_two, (
        f"at m^2 = 4 the exact transfer gap arccosh(3) = {rigor.describe(om4)} is provably "
        f"below lambda_diff = 4 (and below sqrt = 2); at m^2 = 1/4 the ratio omega/lambda = "
        f"{rigor.describe(ratio_small_m)} ~ 2, not 1 -- Delta >= lambda_diff is false and "
        "the true scaling is the square root, exactly as the archive's toy note states"
    )


@notes_prog.check(
    "FINDING: the localization error is n-independent, so the boxed gap does not follow",
    "notes review 2026-08-22 / G23 (iter2 8.2 -> 9.3)",
    tier=2,
)
def _():
    from .. import rigor

    # iter2's unconditional covariance bound is e^{-eta n} + 8|F||G| mu(K^c).
    # The second term does not decay in n: with mu(K^c) = 10^-6, eta = 1/2,
    # unit norms, the bound plateaus at 8e-6 while pure decay at n = 50 is
    # e^{-25} -- certified orders below the plateau. Hence (9.3)'s
    # "for all n >= n_0" extraction fails as written.
    plateau = rigor.ball(Rational(8, 10**6))
    decay_50 = (-rigor.ball(25)).exp()
    ok = rigor.certified_lt(decay_50, plateau)
    return ok, (
        f"e^-25 = {rigor.describe(decay_50)} is provably below the n-independent plateau "
        f"8 mu(K^c) = {rigor.describe(plateau)}: from n ~ 28 the localization error "
        "dominates, so exponential decay in n -- and with it the boxed gap(H) >= eta/a -- "
        "does not follow from (8.2); only 'spectral mass below eta/a is O(mu(K^c))' does"
    )


@notes_prog.check(
    "FINDING: the curvature-mass fit is the placeholder dataset fitted to itself",
    "notes review 2026-08-22 / TENSOR_NETWORK contamination chain",
)
def _():
    # The template's "(EDIT)" placeholder arrays, transcribed exactly; the
    # "results you reported" downstream are the template run on these very
    # numbers. Exact rational least squares through the origin pins it.
    mu = [
        Rational(92, 100),
        Rational(81, 100),
        Rational(74, 100),
        Rational(68, 100),
        Rational(63, 100),
    ]
    m = [
        Rational(88, 100),
        Rational(78, 100),
        Rational(71, 100),
        Rational(66, 100),
        Rational(61, 100),
    ]
    k = sum(a * b for a, b in zip(mu, m, strict=True)) / sum(a * a for a in mu)
    mean = sum(m) / 5
    ss_res = sum((b - k * a) ** 2 for a, b in zip(mu, m, strict=True))
    ss_tot = sum((b - mean) ** 2 for b in m)
    r2 = 1 - ss_res / ss_tot
    ok = k == Rational(9333, 9698) and r2 == Rational(21627127, 21665332)
    return ok, (
        f"through-origin fit of the (EDIT) placeholders gives exactly k = {k} = "
        f"{float(k):.6f} and R^2 = {r2} = {float(r2):.6f} -- digit-for-digit the numbers "
        "the EVIDENCE document (inside best_of_bundle_v2.zip) presents as 'STRONG EVIDENCE "
        "FOR MECHANISM'. The fit measured its own example data; no independent measurement "
        "ever existed, and this check keeps that fact permanent"
    )


@notes_prog.check(
    "FINDING: Riccati blow-up adjudicates the archive's 10/10 proof against its SIM note",
    "notes review 2026-08-22 / RICCATI",
    tier=2,
)
def _():
    from sympy import tanh

    # T1 half: the explicit solution and rate for lambda' = -2 lambda^2 + sigma.
    t = symbols("t", positive=True)
    sig = symbols("sigma", positive=True)
    lam_star = sqrt(sig / 2)
    sol = lam_star * tanh(2 * lam_star * t)  # lambda(0) = 0 branch
    residual = simplify(diff(sol, t) - (-2 * sol**2 + sig))
    rate_ok = simplify(2 * sqrt(2 * sig) - 4 * lam_star) == 0  # gamma = 2 sqrt(2 sigma)

    # T2 half: RK4 at sigma = 1, reproducing the SIM note's digits and the
    # blow-up the "10/10" proof document denies.
    def rk4(lam0, t_end, n):
        h, lam = t_end / n, lam0
        for _ in range(n):
            if abs(lam) > 1e6:
                return lam

            def f(x):
                return -2 * x * x + 1.0

            k1 = f(lam)
            k2 = f(lam + h * k1 / 2)
            k3 = f(lam + h * k2 / 2)
            k4 = f(lam + h * k3)
            lam += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return lam

    converges = rk4(-0.7, 10.0, 40000)
    blows = rk4(-1.0, 0.7, 40000)
    sim_match = abs(converges - 0.707106781041) < 1e-9
    blow_confirmed = blows < -1e6
    ok = residual == 0 and rate_ok and sim_match and blow_confirmed
    return ok, (
        f"tanh solution verified symbolically (residual {residual}), rate 2 sqrt(2 sigma); "
        f"RK4 at sigma = 1: lambda_0 = -0.7 -> {converges:.12f} (SIM note prints "
        f"0.707106781041, matched to 1e-9) while lambda_0 = -1.0 blows down past -1e6 "
        "before t = 0.7 -- the archive's 'Rigor 10/10' Theorem 2.2 (global existence for "
        "all initial data) is false and its own SIM verification note is right"
    )


@notes_prog.check(
    "fundamental Casimir: c_0 = (N^2-1)/(2N) exactly, with the convention trap pinned",
    "notes review 2026-08-22 / G20, G22 (DOC4)",
)
def _():
    from sympy import I as i_unit

    s3 = sqrt(3)
    pauli = [
        Matrix([[0, 1], [1, 0]]),
        Matrix([[0, -i_unit], [i_unit, 0]]),
        Matrix([[1, 0], [0, -1]]),
    ]
    gell = [
        Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        Matrix([[0, -i_unit, 0], [i_unit, 0, 0], [0, 0, 0]]),
        Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        Matrix([[0, 0, -i_unit], [0, 0, 0], [i_unit, 0, 0]]),
        Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        Matrix([[0, 0, 0], [0, 0, -i_unit], [0, i_unit, 0]]),
        Matrix([[1 / s3, 0, 0], [0, 1 / s3, 0], [0, 0, -2 / s3]]),
    ]
    c2_su2 = simplify(
        sum(((m / 2) * (m / 2) for m in pauli), zeros(2, 2)) - Rational(3, 4) * eye(2)
    )
    c2_su3 = simplify(sum(((m / 2) * (m / 2) for m in gell), zeros(3, 3)) - Rational(4, 3) * eye(3))
    formula = all(
        Rational(n**2 - 1, 2 * n) == v for n, v in ((2, Rational(3, 4)), (3, Rational(4, 3)))
    )
    ok = c2_su2 == zeros(2, 2) and c2_su3 == zeros(3, 3) and formula
    return ok, (
        "sum (sigma_a/2)^2 = (3/4) I and sum (lambda_a/2)^2 = (4/3) I exactly -- DOC4's "
        "c_0 = (N^2-1)/(2N) is the fundamental Casimir, the correct Haar gap scale in the "
        "orthonormal normalization. Convention trap pinned: the archive's SU(2) simulations "
        "use T_a = -i sigma_a, where the same eigenvalue reads 4 x 3/4 = 3 (their "
        "Delta B_p = 12 - 12 B_p is 4 links x 3) -- a factor-4 join hazard, not a conflict"
    )


@notes_prog.check(
    "drift-constant closure: two independent derivations agree exactly",
    "notes review 2026-08-22 / G22 (Section 7 vs G_drift_full_algebra)",
)
def _():
    s = symbols("s", positive=True)
    c_delta, c_grad, nu, kappa, c_pair, cap_pair, d = symbols(
        "C_Delta C_grad nu kappa c_pair Cpair D", positive=True
    )
    # K_Phi for Phi = s^2 on (0, 2]: s * (2s)^2 / s^2 = 4s, sup = 8 at s = 2.
    k_phi = (s * (2 * s) ** 2 / s**2).subs(s, 2)
    v_le_2d = simplify(2 * s - s**2)  # s(2 - s) >= 0 on [0, 2]
    # G_drift C_1 with B_Phi = A_Phi = 2 equals Section 7's C_V; C_2 = C_Gamma.
    c1 = 4 * (2 * c_delta + 2 * c_grad)
    c_v = 8 * c_delta + 8 * c_grad
    c2_const = 64 * nu * c_grad
    # Prop 7.39 closure: the drift bound rearranges exactly.
    lhs = (kappa * c_v + kappa**2 * c2_const) * d - 2 * kappa * (c_pair * d - cap_pair)
    rhs = -kappa * (2 * c_pair - c_v - kappa * c2_const) * d + 2 * kappa * cap_pair
    ok = (
        k_phi == 8
        and simplify(v_le_2d.subs(s, 1)) == 1  # positive at interior point
        and expand(c1 - c_v) == 0
        and expand(lhs - rhs) == 0
    )
    return ok, (
        "K_Phi = 8 at the endpoint s = 2; C_1(Phi = s^2) = 4(2C_Delta + 2C_grad) equals "
        "Section 7's C_V = 8C_Delta + 8C_grad identically, C_2 = C_Gamma = 64 nu C_grad; "
        "and Prop 7.39's rearrangement is an exact identity -- the manuscript spine and "
        "G_drift_full_algebra derive the same G22 reduction independently and agree"
    )
