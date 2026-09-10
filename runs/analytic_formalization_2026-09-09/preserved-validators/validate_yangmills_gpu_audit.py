"""Independent, read-only replay of archived models; no GPU or dense eigensolver."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "runs/gpu_yangmills_millennium_resolutions_2026-09-09"


def first_two(diagonal: list[float], off: float) -> list[float]:
    """Floating Sturm bisection, diagnostic rather than interval certification."""
    lo = min(diagonal) - 2 * abs(off) - 1
    hi = max(diagonal) + 2 * abs(off) + 1

    def count(x: float) -> int:
        pivot = diagonal[0] - x
        result = int(pivot < 0)
        for d in diagonal[1:]:
            if abs(pivot) < 1e-100:
                pivot = -1e-100
            pivot = d - x - off * off / pivot
            result += int(pivot < 0)
        return result

    values = []
    for index in (0, 1):
        left, right = lo, hi
        for _ in range(90):
            mid = (left + right) / 2
            if count(mid) <= index:
                left = mid
            else:
                right = mid
        values.append((left + right) / 2)
    return values


def rotor(c: float, v: float, size: int) -> list[float]:
    return first_two([c * n * (n + 2) + v for n in range(size)], -v / 2)


def pairing(size: int, g: float) -> float:
    cosines = [math.cos(2 * math.pi * n / size) for n in range(size)]
    terms = []
    for x in cosines:
        for y in cosines:
            lam = 4 - 2 * x - 2 * y
            d = 2 - lam / 4
            terms.append(g * d / ((2.25 + lam) * (2.25 + lam + g * d)))
    return math.fsum(terms) / size**2


def shell_counts(half: int) -> dict[int, int]:
    """Multiplicities of i^2+j^2+k^2 over the box [-half,half]^3 minus the origin."""
    counts: dict[int, int] = {}
    for i in range(-half, half + 1):
        for j in range(-half, half + 1):
            for k in range(-half, half + 1):
                n2 = i * i + j * j + k * k
                if n2 == 0:
                    continue
                counts[n2] = counts.get(n2, 0) + 1
    return counts


def block_row_sum(counts: dict[int, int], mass: float, amplitude: float) -> float:
    """Sum over v != 0 of C0 exp(-M 2|v|), from a precomputed shell table."""
    return math.fsum(
        multiplicity * amplitude * math.exp(-mass * 2.0 * math.sqrt(n2))
        for n2, multiplicity in counts.items()
    )


def single_link_row_sum(mass: float, amplitude: float, cutoff: int = 500) -> float:
    """The archived z(1)=12, z(r)=12 r^2 budget, summed as coded."""
    return math.fsum(
        (12 if r == 1 else 12 * r * r) * amplitude * math.exp(-mass * r)
        for r in range(1, cutoff)
    )


def symmetric_invariants(matrix: list[list[float]]) -> tuple[float, float, float]:
    """Trace, second symmetric function and determinant of a 3x3 symmetric matrix."""
    trace = matrix[0][0] + matrix[1][1] + matrix[2][2]
    second = math.fsum(
        (
            matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0],
            matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0],
            matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1],
        )
    )
    determinant = math.fsum(
        (
            matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]),
            -matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]),
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]),
        )
    )
    return trace, second, determinant


def phase8_replay(archived: dict) -> dict:
    """GA9. Every deterministic Phase 8 quantity, from its own inserted ansatz."""
    amplitude = 0.50
    # The archived sums accumulate up to 10^6 terms sequentially; the replay uses
    # math.fsum, so the comparison is at the summation-order level, not bitwise.
    RELATIVE = 1e-11
    checks = []

    kappa_single = single_link_row_sum(2.1939, amplitude)
    archived_single = archived["part2_single_link_defect"]["kappa_single"]
    checks.append(
        dict(
            name="phase8_kappa_single",
            replay=kappa_single,
            archived=archived_single,
            absolute_error=abs(kappa_single - archived_single),
            tolerance=1e-14,
            passed=abs(kappa_single - archived_single) < 1e-14,
        )
    )

    tables = {half: shell_counts(half) for half in (2, 4, 8, 16, 32, 50)}
    for row in archived["part3_block_tensorization"]["scans"]:
        value = block_row_sum(tables[row["Nb"] // 2], row["M"], amplitude)
        error = abs(value - row["kappa_block"])
        checks.append(
            dict(
                name="phase8_kappa_block_M{0}_L{1}".format(row["M"], row["L"]),
                replay=value,
                archived=row["kappa_block"],
                absolute_error=error,
                tolerance=RELATIVE * max(1.0, abs(row["kappa_block"])),
                passed=error < RELATIVE * max(1.0, abs(row["kappa_block"])),
            )
        )

    block = archived["part3_block_tensorization"]
    gamma_block = archived["part4_thermodynamic_gap"]["gamma_block"]
    for mass, key, gap_key in (
        (2.1939, "phys", "gap_phys_thermodynamic"),
        (1.5515, "b1", "gap_phys_b1"),
        (0.8000, "cons", "gap_phys_conservative"),
    ):
        value = block_row_sum(tables[50], mass, amplitude)
        target = block["kappa_block_inf_" + key]
        error = abs(value - target)
        checks.append(
            dict(
                name="phase8_kappa_block_infinite_" + key,
                replay=value,
                archived=target,
                absolute_error=error,
                tolerance=RELATIVE * max(1.0, abs(target)),
                passed=error < RELATIVE * max(1.0, abs(target)),
            )
        )
        gap = gamma_block * (1.0 - value)
        gap_target = archived["part4_thermodynamic_gap"][gap_key]
        gap_error = abs(gap - gap_target)
        checks.append(
            dict(
                name="phase8_gap_" + key,
                replay=gap,
                archived=gap_target,
                absolute_error=gap_error,
                tolerance=RELATIVE * max(1.0, abs(gap_target)),
                passed=gap_error < RELATIVE * max(1.0, abs(gap_target)),
            )
        )

    amplitude_threshold = amplitude / kappa_single
    lo, hi = 0.5, 6.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if single_link_row_sum(mid, amplitude) > 1.0:
            lo = mid
        else:
            hi = mid
    mass_threshold = (lo + hi) / 2

    four = {}
    for half in (10, 20):
        counts: dict[int, int] = {}
        for i in range(-half, half + 1):
            for j in range(-half, half + 1):
                for k in range(-half, half + 1):
                    for m in range(-half, half + 1):
                        n2 = i * i + j * j + k * k + m * m
                        if n2:
                            counts[n2] = counts.get(n2, 0) + 1
        four[half] = counts
    four_d = {
        "kappa_block_4d_M{0}".format(mass): block_row_sum(
            four[10 if mass > 1 else 20], mass, amplitude
        )
        for mass in (2.1939, 1.5515, 0.8000)
    }
    four_d["kappa_single_4d_z32r3"] = math.fsum(
        (24 if r == 1 else 32 * r**3) * amplitude * math.exp(-2.1939 * r)
        for r in range(1, 500)
    )

    return dict(
        scope=(
            "GA9 inserted row-sum ansatz only: C0 = 0.50, M inserted, z(1) = 12, "
            "z(r) = 12 r^2, and block separation 2|v| on a three-dimensional block "
            "lattice. The archived script constructs no conditional projection, no "
            "block Dirichlet form and no SU(2) ensemble, so none is replayed."
        ),
        comparisons=checks,
        all_passed=all(row["passed"] for row in checks),
        single_link_closed_form=dict(
            note=(
                "12 C0 q (1 + q) / (1 - q)^3 with the r = 1 shell replaced by 12 C0 q; "
                "q = exp(-M). The r = 1 term alone carries 63 percent of the total."
            ),
            r1_term=12 * amplitude * math.exp(-2.1939),
            r1_fraction=12 * amplitude * math.exp(-2.1939) / kappa_single,
        ),
        threshold=dict(
            note=(
                "The reported single-link defect is a choice of amplitude and mass, "
                "not a derived obstruction: kappa_single reaches 1 at these values."
            ),
            amplitude_at_kappa_one=amplitude_threshold,
            mass_at_kappa_one=mass_threshold,
            archived_amplitude=amplitude,
            archived_mass=2.1939,
        ),
        four_dimensional=dict(
            note=(
                "The archived block sum runs over three-dimensional integer vectors "
                "and its single-link shell count 12 r^2 is three-dimensional, which the "
                "file asserts without stating it. The same ansatz on Z^4, to show how "
                "much of the reported margin is carried by that choice."
            ),
            **four_d,
        ),
        not_replayed=(
            "Part 1 binned conditional mean is a Monte-Carlo statistic with no stored "
            "seed; its reported 0.1051181855075641 is not reproducible bitwise, and its "
            "population value is zero by the invariance identity GA14."
        ),
    )


def phase9_replay(archived: dict) -> dict:
    """GA10. The OS2 Gram matrix and the OS4 sequence, from their typed inputs."""
    elements = [
        [0.0, 0.85, 0.10, 0.05],
        [0.0, 0.05, 0.90, 0.08],
        [0.0, 0.85, 0.10, 0.05],
        [0.0, 0.05, 0.90, 0.08],
        [0.0, 0.85, 0.10, 0.05],
        [0.0, 0.85, 0.10, 0.05],
    ]
    energies = [0.0, 2.1939, 2.9250, 3.5000]
    times = [1.0, 1.0, 2.0, 2.0, 3.0, 4.0]
    vectors = [
        [elements[i][n] * math.exp(-energies[n] * times[i]) for n in range(4)]
        for i in range(6)
    ]
    gram_small = [
        [math.fsum(vectors[i][m] * vectors[i][n] for i in range(6)) for n in range(1, 4)]
        for m in range(1, 4)
    ]
    archived_eigenvalues = sorted(archived["os2_reflection_positivity"]["eigenvalues"])
    top = archived_eigenvalues[3:]
    replay_invariants = symmetric_invariants(gram_small)
    archived_invariants = (
        math.fsum(top),
        math.fsum((top[0] * top[1], top[0] * top[2], top[1] * top[2])),
        top[0] * top[1] * top[2],
    )
    checks = [
        dict(
            name="phase9_os2_gram_invariant_{0}".format(label),
            replay=replay_invariants[index],
            archived=archived_invariants[index],
            absolute_error=abs(replay_invariants[index] - archived_invariants[index]),
            tolerance=1e-11 * abs(archived_invariants[index]),
            passed=abs(replay_invariants[index] - archived_invariants[index])
            < 1e-11 * abs(archived_invariants[index]),
        )
        for index, label in enumerate(("trace", "second", "determinant"))
    ]
    checks.append(
        dict(
            name="phase9_os2_three_exact_zeros",
            replay=0.0,
            archived=max(abs(value) for value in archived_eigenvalues[:3]),
            absolute_error=max(abs(value) for value in archived_eigenvalues[:3]),
            tolerance=1e-18,
            passed=max(abs(value) for value in archived_eigenvalues[:3]) < 1e-18,
        )
    )

    sequence = [
        0.85**2 * math.exp(-2.1939 * t) + 0.10**2 * math.exp(-2.9250 * t)
        for t in range(1, 11)
    ]
    for index, target in enumerate(archived["os4_clustering"]["S2_connected"]):
        error = abs(sequence[index] - target)
        checks.append(
            dict(
                name="phase9_os4_S2_t{0}".format(index + 1),
                replay=sequence[index],
                archived=target,
                absolute_error=error,
                tolerance=1e-18,
                passed=error < 1e-18,
            )
        )

    return dict(
        scope=(
            "GA10 typed matrix elements, typed energies and the inserted two-exponential "
            "formula only. The archived script builds no gauge configuration, no transfer "
            "matrix and no reflection, so none is replayed."
        ),
        comparisons=checks,
        all_passed=all(row["passed"] for row in checks),
        os2_structure=dict(
            note=(
                "M = V V^T with V the 6x4 array A[i][n] exp(-E_n t_i) whose n = 0 column "
                "is identically zero. M is the Gram matrix of six vectors in a "
                "three-dimensional space: rank at most 3, three exact zero eigenvalues, "
                "and positive semidefiniteness by construction rather than by test."
            ),
            rank_bound=3,
            zero_eigenvalues=3,
            archived_minimum=archived["os2_reflection_positivity"]["min_eigenvalue"],
        ),
        os4_structure=dict(
            note=(
                "S_2^c(t) = 0.85^2 exp(-2.1939 t) + 0.10^2 exp(-2.9250 t) is evaluated "
                "and plateau_mass is float(Delta_phys): the inserted mass returned unchanged."
            ),
            inserted_mass=2.1939,
            reported_plateau=archived["os4_clustering"]["plateau_mass"],
        ),
        haar_kurtosis=dict(
            note=(
                "Part 3 statistic is the excess kurtosis of Tr U for a single SU(2) "
                "matrix. At beta = 0, Tr U = 2 u_0 with u_0 semicircular: E[u_0^2] = 1/4 "
                "and E[u_0^4] = 1/8 give m2 = 1, m4 = 2 and S_4^c = -1 exactly. The "
                "statistic is nonzero for the free Haar measure, so its nonvanishing at "
                "beta = 4 is not evidence of an interacting field theory."
            ),
            haar_m2=1.0,
            haar_m4=2.0,
            haar_connected_four_point=-1.0,
            archived_beta4=archived["wightman_non_triviality"]["S4_connected_zero"],
        ),
        not_replayed=(
            "Part 3 beta = 4 moments are Monte-Carlo statistics with no stored seed."
        ),
    )


def main() -> None:
    hashes = {}
    for line in (RUN / "SHA256SUMS").read_text().splitlines():
        if not line.strip():
            continue
        expected, name = line.split(maxsplit=1)
        name = name.lstrip("* ")
        actual = hashlib.sha256((RUN / name).read_bytes()).hexdigest()
        assert actual.lower() == expected.lower(), name
        hashes[name] = actual

    def load(name):
        return json.loads((RUN / name).read_text())

    p1 = load("phase1_w6_results.json")
    p2 = load("phase2_wr26_results.json")["phase2_wr26_results"]
    p3 = load("phase3_transfer_vs_langevin_results.json")["phase3_transfer_vs_langevin_results"]
    p4 = load("phase4_continuum_scaling_results.json")
    comparisons = []

    def compare(name: str, actual: float, archived: float, tolerance: float = 1e-10):
        error = abs(actual - archived)
        comparisons.append(
            dict(
                name=name,
                replay=actual,
                archived=archived,
                absolute_error=error,
                tolerance=tolerance,
                passed=error <= tolerance,
            )
        )

    scan = p1["phase1_spectator_volume_independence"]
    for size, archived in zip(scan["sizes"], scan["pairings"], strict=True):
        compare(f"phase1_volume_L{size}", pairing(size, 0.1), archived, 1e-14)
    scan = p1["phase1_coupling_linear_bound"]
    for g, archived in zip(scan["couplings"], scan["pairings"], strict=True):
        compare(f"phase1_coupling_{g}", pairing(32, g), archived, 1e-14)
    decay = p1["phase1_combes_thomas_decay"]
    kernels = []
    for distance in decay["distances"]:
        value = (
            math.fsum(
                math.cos(2 * math.pi * r * distance / 32)
                / (
                    2.25
                    + 0.4
                    + 0.95
                    * (4 - 2 * math.cos(2 * math.pi * r / 32) - 2 * math.cos(2 * math.pi * s / 32))
                )
                for r in range(32)
                for s in range(32)
            )
            / 32**2
        )
        kernels.append(value)
        compare(f"phase1_kernel_{distance}", value, decay["kernel_vals"][distance], 1e-14)
    xs = list(range(1, 8))
    logs = [math.log(kernels[d]) for d in xs]
    xmean, ymean = sum(xs) / 7, sum(logs) / 7
    eta = -sum((x - xmean) * (y - ymean) for x, y in zip(xs, logs, strict=True)) / sum(
        (x - xmean) ** 2 for x in xs
    )
    compare("phase1_decay_fit", eta, decay["eta_measured"], 1e-9)
    compare("phase1_CT_exponent", 2 * math.asinh(1.5 / 4), decay["eta_theory"])
    for row in p2["frustration_table"]:
        v = row["v"]
        e0, e1 = rotor(0.625, v, 25)
        base = rotor(0.5, v, 25)[0]
        for key, value in {
            "E0": 2 * e0,
            "2_e_star": 2 * base,
            "F_lambda": 2 * (e0 - base),
            "gap_delta": e1 - e0,
        }.items():
            compare(f"phase2_v{v}_{key}", value, row[key])
    for row in p3["beta_scan"]:
        beta = row["beta"]
        h = (math.pi - 0.0002) / 999
        theta = [0.0001 + n * h for n in range(1000)]
        ep = first_two([1 / h**2 - 1 + beta / 2 * (1 - math.cos(t)) for t in theta], -0.5 / h**2)
        el = first_two(
            [
                2 / h**2 + beta**2 * math.sin(t) ** 2 / 4 - 1.5 * beta * math.cos(t) - 1
                for t in theta
            ],
            -1 / h**2,
        )
        dp, dl = ep[1] - ep[0], el[1] - el[0]
        for key, value in {
            "delta_phys": dp,
            "lambda_diff": dl,
            "sqrt_lambda_diff": math.sqrt(dl),
            "ratio": dp / math.sqrt(dl),
        }.items():
            compare(f"phase3_beta{beta}_{key}", value, row[key], 1e-7)
    for row in p4["phase4_2x2_cluster"]["cluster_results"]:
        e0, e1 = rotor(0.75, row["v"], 7)
        for key, value in {
            "E0": 4 * e0,
            "E1": 3 * e0 + e1,
            "E2": 3 * e0 + e1,
            "gap": e1 - e0,
        }.items():
            compare(f"phase4_v{row['v']}_{key}", value, row[key])
    b0 = 22 / (48 * math.pi**2)
    ell, h = math.log(5), math.log(2)
    c = 0.053 * (2 * b0) ** -1.5
    a, b = 1.0, 0.8
    for row in p4["phase4_multiscale_schur_continuum"]["steps"]:
        j = row["step"]
        eps = c * (ell + j * h) ** -1.5
        compare(f"phase4_A_{j}", a, row["A_j"])
        compare(f"phase4_Delta_{j}", a / b, row["Delta_j"])
        compare(f"phase4_eps_{j}", eps, row["eps_j"])
        if j < 20:
            a *= 1 - eps
            b += a / (2.5 * 2**j)
    tail_integral = 2 * c / (h * math.sqrt(ell + 20 * h))
    a_lower = a * math.exp(-(tail_integral + eps) / (1 - eps))
    a_upper = a * math.exp(-tail_integral)
    b_upper = b + 0.8 * a * 2**-20
    report = dict(
        scope="T2 independent replay of the coded models only; no Wilson operator identification",
        method="Pure Python Fourier sums and tridiagonal Sturm bisection; no GPU output rewritten",
        input_sha256=hashes,
        comparisons=comparisons,
        all_passed=all(row["passed"] for row in comparisons),
        scalar_infinite_limit=dict(
            scope="GA8 analytic bounds evaluated as floats, not outward-rounded intervals",
            delta20=a / b,
            lower_formula=a_lower / b_upper,
            upper_formula=a_upper / b,
            A20=a,
            A_infinity_lower_formula=a_lower,
            A_infinity_upper_formula=a_upper,
            eps0=c * ell**-1.5,
        ),
    )
    phase7 = load("phase7_g17_results.json")
    phase7_checks = []
    for row in phase7["free_energy_volume_independence"]:
        size = row["L"]
        value = math.fsum(
            38 ** (n - 1)
            / math.factorial(n)
            * (0.038 / 4) ** n
            * (1 + (math.exp(-size) if n >= size else 0))
            for n in range(1, 9)
        )
        error = abs(value - row["free_energy_density"])
        phase7_checks.append(dict(L=size, replay=value, error=error, passed=error < 1e-15))
    assert all(row["passed"] for row in phase7_checks)
    report["phase7_supplementary_scalar_replay"] = dict(
        scope="Inserted eight-term scalar formula only; Gaussian random correlations not replayed",
        beta_threshold=2 / (38 * math.e),
        comparisons=phase7_checks,
    )
    report["phase8_supplementary_ansatz_replay"] = phase8_replay(load("phase8_va12_results.json"))
    assert report["phase8_supplementary_ansatz_replay"]["all_passed"]
    report["phase9_supplementary_typed_input_replay"] = phase9_replay(
        load("phase9_wightman_results.json")
    )
    assert report["phase9_supplementary_typed_input_replay"]["all_passed"]
    target = ROOT / "docs/validation/yangmills-gpu-audit-2026-09-09.json"
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    failures = [row for row in comparisons if not row["passed"]]
    print(
        json.dumps(
            dict(
                comparisons=len(comparisons),
                failures=failures,
                scalar_infinite_limit=report["scalar_infinite_limit"],
                report=str(target),
            ),
            indent=2,
        )
    )
    assert not failures


if __name__ == "__main__":
    main()
