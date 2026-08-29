#!/usr/bin/env python3
"""Minimal exact-path B=6 open-cube Schur calculation.

This instrument deliberately does *not* enumerate the full B=6 cube Hilbert
space.  Through second order, the vacuum and the six charge-odd one-face
states only require the states reached by one action of

    M = sum_faces (Box_face + Box_face^dagger).

The six local face tables are generated directly with the public pyclebsch
open-boundary master-formula implementation at the B=6 cutoff.  The resulting
reachable-state amplitudes are then contracted with exact electric-energy
denominators.  Local Wilson-loop coefficients are double precision; reported
"exact rational" comparisons are therefore numerical rational-reconstruction
checks, not symbolic execution of pyclebsch.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import platform
import sys
import time
import zipfile
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
SCRATCH = HERE / ".scratch"
WORKSPACE = HERE
REFERENCE_SCRIPT = SCRATCH / "cube_matrix_reconstruction_balaji_20260828.py"
if not REFERENCE_SCRIPT.is_file():
    raise FileNotFoundError(f"Missing prior public-code adapter: {REFERENCE_SCRIPT}")
sys.path.insert(0, str(SCRATCH))

# This adapter supplies the pinned public pyclebsch source path, dependency
# fallbacks for more-itertools/tqdm, and the already-audited cube geometry.
import cube_matrix_reconstruction_balaji_20260828 as cube  # noqa: E402


ONE = (0, 0, 0)
THREE = (1, 0, 0)
THREE_BAR = (1, 1, 0)
SIX = (2, 0, 0)
EIGHT = (2, 1, 0)
SIX_BAR = (2, 2, 0)
B6_IRREPS = (ONE, THREE, THREE_BAR, SIX, EIGHT, SIX_BAR)
CONJUGATE = {
    ONE: ONE,
    THREE: THREE_BAR,
    THREE_BAR: THREE,
    SIX: SIX_BAR,
    SIX_BAR: SIX,
    EIGHT: EIGHT,
}
C2 = {
    ONE: Fraction(0),
    THREE: Fraction(4, 3),
    THREE_BAR: Fraction(4, 3),
    SIX: Fraction(10, 3),
    SIX_BAR: Fraction(10, 3),
    EIGHT: Fraction(3),
}
E0 = Fraction(8, 3)
EXPECTED_T = Fraction(5, 612)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def state_energy(state: tuple[tuple[int, int, int], ...]) -> Fraction:
    return sum((C2[irrep] for irrep in state), Fraction(0)) / 2


def group_values(values, tolerance: float = 2e-9) -> list[dict]:
    groups: list[list[float]] = []
    for value in sorted(map(float, values)):
        if not groups or abs(value - float(np.mean(groups[-1]))) > tolerance:
            groups.append([value])
        else:
            groups[-1].append(value)
    return [
        {
            "value": float(np.mean(group)),
            "multiplicity": len(group),
            "spread": float(max(group) - min(group)),
        }
        for group in groups
    ]


def sparse_dot(left: dict, right: dict) -> float:
    if len(left) > len(right):
        left, right = right, left
    return float(sum(value * right.get(state, 0.0) for state, value in left.items()))


def add_scaled(target: dict, source: dict, scale: float) -> None:
    for state, value in source.items():
        target[state] += scale * value


def cubical_face_gram(plaquette_items, link_index) -> np.ndarray:
    boundary = np.zeros((len(link_index), len(plaquette_items)), dtype=np.int64)
    for face_index, (_, plaquette_data) in enumerate(plaquette_items):
        for address, sign in zip(plaquette_data[0], (1, 1, -1, -1), strict=True):
            boundary[link_index[address], face_index] = sign
    return boundary.T @ boundary


def global_to_local(state, plaquette_data, link_index):
    active_addresses, control_addresses_by_site = plaquette_data[:2]
    active = tuple(state[link_index[address]] for address in active_addresses)
    controls = tuple(
        tuple(state[link_index[address]] for address in addresses)
        for addresses in control_addresses_by_site
    )
    # At B=6 every allowed trivalent singlet in the local table is unique.
    return active + controls + (0, 0, 0, 0)


def updated_global(state, final_local, plaquette_data, link_index):
    result = list(state)
    for address, irrep in zip(plaquette_data[0], final_local[:4], strict=True):
        result[link_index[address]] = irrep
    return tuple(result)


def generate_face_actions(
    sites, plaquette_items, irreps, singlets, conjugates, expected_directed_entries=1000
):
    """Generate six local Hermitian M_face actions and their diagnostics."""

    actions = []
    diagnostics = []
    for face, plaquette_data in plaquette_items:
        start = time.perf_counter()
        directed = cube.pme.calc_plaquette_elements(
            3,
            face,
            sites,
            dict(plaquette_items),
            irreps,
            singlets,
            conjugates,
            cube.FORDER,
            1e-12,
            14,
            False,
        )
        elapsed = time.perf_counter() - start
        if len(directed) != expected_directed_entries:
            raise AssertionError(
                f"Expected {expected_directed_entries} directed entries for {face}, got {len(directed)}"
            )

        hermitian = defaultdict(list)
        all_reps = set()
        multiplicities = set()
        for (final_local, initial_local), amplitude in directed.items():
            amplitude = float(amplitude)
            hermitian[initial_local].append((final_local, amplitude))
            hermitian[final_local].append((initial_local, amplitude))
            for local in (initial_local, final_local):
                all_reps.update(local[:4])
                for control_group in local[4:8]:
                    all_reps.update(control_group)
                multiplicities.add(tuple(local[8:12]))
        if all_reps != set(B6_IRREPS):
            raise AssertionError(f"Unexpected B=6 irrep set on {face}: {sorted(all_reps)}")
        if multiplicities != {(0, 0, 0, 0)}:
            raise AssertionError(f"Non-unique trivalent intertwiner encountered on {face}: {multiplicities}")
        actions.append((plaquette_data, dict(hermitian), directed))
        diagnostics.append(
            {
                "face": str(face),
                "directed_entries": len(directed),
                "hermitian_initial_keys": len(hermitian),
                "elapsed_seconds": elapsed,
                "coefficient_value_count": len(set(map(float, directed.values()))),
                "coefficient_min": min(map(float, directed.values())),
                "coefficient_max": max(map(float, directed.values())),
            }
        )
    return actions, diagnostics


def apply_m(state, face_actions, link_index):
    result = defaultdict(float)
    missing = []
    for face_index, (plaquette_data, hermitian, _) in enumerate(face_actions):
        local = global_to_local(state, plaquette_data, link_index)
        transitions = hermitian.get(local)
        if transitions is None:
            missing.append((face_index, local))
            continue
        for final_local, amplitude in transitions:
            # The Wilson loop does not change controls or the unique G=0 labels.
            if final_local[4:8] != local[4:8] or final_local[8:12] != local[8:12]:
                raise AssertionError("Local face transition changed a control or multiplicity label")
            result[updated_global(state, final_local, plaquette_data, link_index)] += amplitude
    if missing:
        raise AssertionError(f"Missing local B=6 initial state on {len(missing)} faces")
    return dict(result)


def channel_label(state, shared_address, link_index):
    irrep = state[link_index[shared_address]]
    return {
        ONE: "1",
        THREE: "3",
        THREE_BAR: "3bar",
        SIX: "6",
        SIX_BAR: "6bar",
        EIGHT: "8",
    }[irrep]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cache", type=Path, default=SCRATCH / "b6_cube_reduced" / "CGC_Data"
    )
    parser.add_argument("--certificate", type=Path, default=HERE / "b6_cube_reduced_certificate.json")
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    args.certificate.parent.mkdir(parents=True, exist_ok=True)
    cube.cgc.set_cache_dir(args.cache.resolve())

    run_start = time.perf_counter()
    sites, links, plaquettes = cube.sites_links_and_plaquettes(
        (2, 2, 2), (False, False, False), cube.FORDER
    )
    plaquette_items = tuple(plaquettes.items())
    link_order = tuple(links)
    link_index = {address: index for index, address in enumerate(link_order)}
    irreps, singlets, conjugates = cube.irreps_and_singlets(3, sites, "B", 6)
    if tuple(irreps[3]) != B6_IRREPS:
        raise AssertionError(f"Unexpected B=6 irrep order: {irreps[3]}")
    singlet_count = sum(len(active_pairs) for active_pairs in singlets[3].values())
    if singlet_count != 24:
        raise AssertionError(f"Unexpected trivalent singlet census: {singlet_count}")

    face_actions, face_diagnostics = generate_face_actions(
        sites, plaquette_items, irreps, singlets, conjugates
    )

    # The public repository contains a B=6 trivalent (d=3/2 ladder-interior)
    # table.  Direction conventions change signs, but the complete absolute
    # coefficient multiset is local and must match every cube face.
    public_b6_table = (
        SCRATCH
        / "literature"
        / "ymcirc-feature-obc"
        / "ymcirc-feature-OBC-mixed-BC"
        / "ymcirc"
        / "_ymcirc_data"
        / "magnetic-hamiltonian-box-term-matrix-elements"
        / "B6_dim(3_2)_magnetic_hamiltonian.json.gz"
    )
    with gzip.open(public_b6_table, "rt", encoding="utf-8") as stream:
        public_table_raw = json.load(stream)
    interior_signature = "((1, 2, -1), (1, 2, -1), (1, -1, -2), (1, -1, -2))"
    public_abs_coefficients = sorted(
        abs(float(by_plane["(1, 2)"][interior_signature]))
        for by_plane in public_table_raw["data"].values()
        if interior_signature in by_plane.get("(1, 2)", {})
    )
    face_public_abs_errors = []
    for _, _, directed in face_actions:
        generated = sorted(abs(float(value)) for value in directed.values())
        if len(generated) != len(public_abs_coefficients):
            raise AssertionError("Generated/public B=6 local table count mismatch")
        face_public_abs_errors.append(
            float(np.max(np.abs(np.asarray(generated) - np.asarray(public_abs_coefficients))))
        )

    vacuum = (ONE,) * len(link_order)
    sqrt2 = np.sqrt(2.0)
    shell_vectors = []
    shell_records = []
    for face_index, ((face, plaquette_data), (_, _, directed)) in enumerate(
        zip(plaquette_items, face_actions, strict=True)
    ):
        oriented = list(vacuum)
        for address, irrep in zip(
            plaquette_data[0], (THREE, THREE, THREE_BAR, THREE_BAR), strict=True
        ):
            oriented[link_index[address]] = irrep
        oriented = tuple(oriented)
        conjugate = tuple(CONJUGATE[irrep] for irrep in oriented)
        vacuum_local = global_to_local(vacuum, plaquette_data, link_index)
        oriented_local = global_to_local(oriented, plaquette_data, link_index)
        box_amplitude = directed.get((oriented_local, vacuum_local))
        if box_amplitude is None or abs(float(box_amplitude) - 1.0) > 1e-12:
            raise AssertionError(f"Vacuum-to-loop Box normalization failed on {face}")
        shell_vectors.append({oriented: 1.0 / sqrt2, conjugate: -1.0 / sqrt2})
        shell_records.append(
            {
                "face_index": face_index,
                "face": str(face),
                "oriented_link_irreps": [str(irrep) for irrep in oriented],
                "conjugate_link_irreps": [str(irrep) for irrep in conjugate],
            }
        )

    # V=-M.  The sign is retained for the first-order operator and cancels in
    # all quadratic second-order contractions.
    shell_images = []
    image_state_counts = []
    for vector in shell_vectors:
        image = defaultdict(float)
        for state, coefficient in vector.items():
            add_scaled(image, apply_m(state, face_actions, link_index), -coefficient)
        shell_images.append(dict(image))
        image_state_counts.append(len(image))

    first = np.array(
        [[sparse_dot(shell_vectors[a], shell_images[b]) for b in range(6)] for a in range(6)]
    )
    all_intermediates = set().union(*(image.keys() for image in shell_images))
    shell_second = np.zeros((6, 6), dtype=np.float64)
    for intermediate in all_intermediates:
        energy = state_energy(intermediate)
        if energy == E0:
            continue
        denominator = float(E0 - energy)
        amplitudes = np.array([image.get(intermediate, 0.0) for image in shell_images])
        shell_second += np.outer(amplitudes, amplitudes) / denominator

    vacuum_image = {state: -value for state, value in apply_m(vacuum, face_actions, link_index).items()}
    vacuum_second = 0.0
    for intermediate, amplitude in vacuum_image.items():
        energy = state_energy(intermediate)
        if energy == 0:
            continue
        vacuum_second += amplitude * amplitude / float(-energy)
    gap_second = shell_second - vacuum_second * np.eye(6)

    gram = cubical_face_gram(plaquette_items, link_index)
    gram_eigenvalues = np.linalg.eigvalsh(gram)
    gap_eigenvalues = np.linalg.eigvalsh(gap_second)
    # Off-diagonal least-squares fit determines t independently of the scalar.
    mask = ~np.eye(6, dtype=bool)
    t_fit = float(np.sum(gap_second[mask] * gram[mask]) / np.sum(gram[mask] ** 2))
    scalar_fit = float(np.mean(np.diag(gap_second - t_fit * gram)))
    fitted = scalar_fit * np.eye(6) + t_fit * gram
    fit_error = float(np.max(np.abs(gap_second - fitted)))
    t_fraction = Fraction(t_fit).limit_denominator(100000)

    # Resolve the four predicted shared-link routes on one adjacent face pair.
    adjacent_pairs = [
        (i, j)
        for i in range(6)
        for j in range(i + 1, 6)
        if gram[i, j] != 0
    ]
    channel_audit = []
    for i, j in adjacent_pairs:
        shared = set(plaquette_items[i][1][0]).intersection(plaquette_items[j][1][0])
        if len(shared) != 1:
            raise AssertionError("Adjacent faces do not have exactly one shared link")
        shared_address = next(iter(shared))
        contributions = defaultdict(float)
        for intermediate in set(shell_images[i]).intersection(shell_images[j]):
            energy = state_energy(intermediate)
            if energy == E0:
                continue
            value = (
                shell_images[i][intermediate]
                * shell_images[j][intermediate]
                / float(E0 - energy)
            )
            contributions[channel_label(intermediate, shared_address, link_index)] += value
        channel_audit.append(
            {
                "face_pair": [i, j],
                "gram_entry": int(gram[i, j]),
                "shared_link": str(shared_address),
                "contributions": dict(sorted(contributions.items())),
                "four_theory_routes": {
                    "-w_1": contributions.get("1", 0.0),
                    "w_3bar": contributions.get("3", 0.0)
                    + contributions.get("3bar", 0.0),
                    "w_6": contributions.get("6", 0.0)
                    + contributions.get("6bar", 0.0),
                    "-w_8": contributions.get("8", 0.0),
                },
                "sum": float(sum(contributions.values())),
                "expected_off_diagonal": float(EXPECTED_T * int(gram[i, j])),
            }
        )

    expected_gap_relative = np.array(
        [0.0, 5.0 / 153.0, 5.0 / 153.0, 5.0 / 153.0, 5.0 / 102.0, 5.0 / 102.0]
    )
    expected_gap_absolute = np.array(
        [39.0 / 68.0, 371.0 / 612.0, 371.0 / 612.0, 371.0 / 612.0,
         127.0 / 204.0, 127.0 / 204.0]
    )
    observed_relative = gap_eigenvalues - float(np.min(gap_eigenvalues))
    # Positive t means the singleton (G=0) is the lowest coefficient.
    expected_t_float = float(EXPECTED_T)
    checks = {
        "geometry_is_open_cube": (len(sites), len(links), len(plaquettes)) == (8, 12, 6),
        "b6_irrep_set_is_1_3_3bar_6_8_6bar": tuple(irreps[3]) == B6_IRREPS,
        "trivalent_singlet_census_is_24": singlet_count == 24,
        "six_faces_each_have_1000_directed_entries": all(
            record["directed_entries"] == 1000 for record in face_diagnostics
        ),
        "public_B6_trivalent_table_has_1000_interior_entries": len(public_abs_coefficients) == 1000,
        "all_cube_face_absolute_coefficients_match_public_B6_table": max(face_public_abs_errors) < 6e-10,
        "one_face_first_order_is_identity": float(np.max(np.abs(first - np.eye(6)))) < 2e-11,
        "vacuum_second_order_is_minus_9_over_2": abs(vacuum_second + 4.5) < 2e-11,
        "face_gram_spectrum_is_1_plus_3_plus_2": np.allclose(
            gram_eigenvalues, [0, 4, 4, 4, 6, 6], atol=1e-12, rtol=0
        ),
        "gap_matrix_is_scalar_plus_tG": fit_error < 2e-10,
        "t_is_plus_5_over_612": abs(t_fit - expected_t_float) < 2e-10,
        "t_rational_reconstructs_to_5_over_612": t_fraction == EXPECTED_T,
        "b6_scalar_is_39_over_68": abs(scalar_fit - 39.0 / 68.0) < 2e-10,
        "absolute_gap_spectrum_matches_rationals": np.allclose(
            gap_eigenvalues, expected_gap_absolute, atol=3e-10, rtol=0
        ),
        "relative_shell_is_1_plus_3_plus_2_with_reversed_order": np.allclose(
            observed_relative, expected_gap_relative, atol=3e-10, rtol=0
        ),
        "all_adjacent_pairs_have_six_raw_reps_grouping_to_four_routes": all(
            set(record["contributions"]) == {"1", "3", "3bar", "6", "6bar", "8"}
            for record in channel_audit
        ),
        "four_route_weights_match_exact_prediction": all(
            np.allclose(
                list(record["four_theory_routes"].values()),
                np.sign(record["gram_entry"])
                * np.array([1.0 / 12.0, -1.0 / 6.0, -2.0 / 9.0, 16.0 / 51.0]),
                atol=2e-10,
                rtol=0.0,
            )
            for record in channel_audit
        ),
        "all_adjacent_channel_sums_match_tG": all(
            abs(record["sum"] - record["expected_off_diagonal"]) < 2e-10
            for record in channel_audit
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    pme_path = Path(cube.pme.__file__).resolve()
    lattice_path = Path(cube.sites_links_and_plaquettes.__code__.co_filename).resolve()
    source_archive = SCRATCH / "literature" / "pyclebsch-feature-obc.zip"
    archive_member_hashes = {}
    if source_archive.is_file():
        with zipfile.ZipFile(source_archive) as archive:
            for suffix, extracted_path in (
                ("/pyclebsch/matrix_elements/plaquette_matrix_elements.py", pme_path),
                ("/pyclebsch/matrix_elements/lattice_data.py", lattice_path),
            ):
                names = [name for name in archive.namelist() if name.endswith(suffix)]
                if len(names) != 1:
                    raise AssertionError(f"Could not uniquely identify {suffix} in source archive")
                archive_member_hashes[suffix] = hashlib.sha256(archive.read(names[0])).hexdigest()
                archive_member_hashes[suffix + ":extracted"] = sha256_file(extracted_path)
        checks["executed_source_files_match_downloaded_archive"] = all(
            archive_member_hashes[suffix] == archive_member_hashes[suffix + ":extracted"]
            for suffix in (
                "/pyclebsch/matrix_elements/plaquette_matrix_elements.py",
                "/pyclebsch/matrix_elements/lattice_data.py",
            )
        )
    else:
        checks["executed_source_files_match_downloaded_archive"] = False
    try:
        import scipy

        scipy_version = scipy.__version__
    except Exception as error:  # pragma: no cover
        scipy_version = f"unavailable: {error}"

    certificate = {
        "schema": "workhouse.b6-open-cube-reduced-second-order.v1",
        "scope": (
            "SU(3) open cube, local B=6 cutoff, vacuum and six charge-odd one-face "
            "states through second order; reachable-state Schur complement only"
        ),
        "method": (
            "Generate each open-cube face table directly with public pyclebsch; "
            "contract only states in M|vacuum> and M|one-face C- shell>."
        ),
        "numerical_exactness_boundary": (
            "pyclebsch coefficients are double precision rounded to 14 decimal places; "
            "rational identities are certified by residual and rational reconstruction, "
            "not symbolic CGC arithmetic"
        ),
        "geometry": {
            "vertices": len(sites),
            "links": len(links),
            "faces": len(plaquettes),
            "boundary_conditions": "open",
        },
        "truncation": {
            "mode": "B",
            "cutoff": 6,
            "irreps": [str(irrep) for irrep in irreps[3]],
            "irrep_names": ["1", "3", "3bar", "6", "8", "6bar"],
            "trivalent_ordered_singlet_tuples": singlet_count,
        },
        "local_generation": face_diagnostics,
        "public_B6_trivalent_table_crosscheck": {
            "path": str(public_b6_table.resolve()),
            "sha256": sha256_file(public_b6_table),
            "interior_entry_count": len(public_abs_coefficients),
            "per_face_max_absolute_multiset_errors": face_public_abs_errors,
            "note": (
                "Absolute multisets are compared because cube and ladder vertex direction "
                "conventions can rephase unique trivalent intertwiner states."
            ),
        },
        "reachable_space": {
            "shell_image_state_counts": image_state_counts,
            "shell_image_union_dimension": len(all_intermediates),
            "vacuum_image_dimension": len(vacuum_image),
            "full_B6_global_basis_enumerated": False,
        },
        "shell": shell_records,
        "first_order_matrix": first.tolist(),
        "vacuum_second_order": vacuum_second,
        "shell_raw_second_order_matrix": shell_second.tolist(),
        "gap_second_order_matrix": gap_second.tolist(),
        "face_gram": gram.tolist(),
        "face_gram_eigenvalues": gram_eigenvalues.tolist(),
        "gap_second_order_eigenvalues": gap_eigenvalues.tolist(),
        "gap_second_order_groups": group_values(gap_eigenvalues),
        "scalar_plus_tG_fit": {
            "scalar": scalar_fit,
            "scalar_rational_reconstruction": str(Fraction(scalar_fit).limit_denominator(100000)),
            "expected_B6_scalar": "39/68",
            "t": t_fit,
            "t_rational_reconstruction": str(t_fraction),
            "expected_t": str(EXPECTED_T),
            "t_error": t_fit - expected_t_float,
            "matrix_max_absolute_residual": fit_error,
        },
        "relative_to_G0_singleton": {
            "observed_sorted": observed_relative.tolist(),
            "expected_sorted": expected_gap_relative.tolist(),
            "groups": group_values(observed_relative),
        },
        "absolute_gap_second_order_spectrum": {
            "observed_sorted": gap_eigenvalues.tolist(),
            "expected_rationals": ["39/68", "371/612", "371/612", "371/612", "127/204", "127/204"],
            "expected_sorted": expected_gap_absolute.tolist(),
        },
        "B6_vs_B7_boundary": {
            "B6_shared_link_sextet_vertex_casimir_sum": "C2(6)+2*C2(3)=6",
            "B6_shared_link_sextet_is_included": True,
            "same_face_sextet_pair_vertex_casimir_sum": "C2(6)+C2(6bar)=20/3",
            "same_face_sextet_first_integer_cutoff": 7,
            "interpretation": (
                "B=6 is channel-complete for the adjacent-face hopping coefficient t, "
                "but its scalar 39/68 is the B=6 onsite scalar.  The same-face sextet "
                "route first admitted at B=7 can change the scalar without changing t."
            ),
        },
        "adjacent_shared_link_channel_audit": channel_audit,
        "checks": checks,
        "pass": all(checks.values()),
        "runtime": {
            "total_seconds": time.perf_counter() - run_start,
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "scipy": scipy_version,
        },
        "source_provenance": {
            "pyclebsch_root": str(cube.PYCLEBSCH_ROOT.resolve()),
            "source_archive": str(source_archive.resolve()),
            "source_archive_sha256": sha256_file(source_archive) if source_archive.is_file() else None,
            "archive_member_hashes": archive_member_hashes,
            "plaquette_matrix_elements": str(pme_path),
            "plaquette_matrix_elements_sha256": sha256_file(pme_path),
            "lattice_data": str(lattice_path),
            "lattice_data_sha256": sha256_file(lattice_path),
            "adapter": str(REFERENCE_SCRIPT.resolve()),
            "adapter_sha256": sha256_file(REFERENCE_SCRIPT),
            "cgc_cache": str(args.cache.resolve()),
        },
    }
    args.certificate.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(certificate, indent=2, sort_keys=True))
    if not certificate["pass"]:
        failed = [name for name, passed in checks.items() if not passed]
        raise SystemExit(f"B=6 reduced calculation failed checks: {failed}")


if __name__ == "__main__":
    main()
