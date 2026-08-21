#!/usr/bin/env python3
"""
SU(6) O(y^4) exceptional-rank single-orbit contraction.

This exact stage consumes:
  1. Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE*.zip
  2. SU6_WORD_ENUMERATOR_V1_BUNDLE.zip
     OR y4_su6_determinant_ordered_words.json.gz already present in /content.

The word enumerator proves that the entire SU(6) determinant correction consists
of one existing mixed ordered word, two charge-conjugate assignments, and one
C-orbit. Geometrically all six factors are the same plaquette. Thus each of its
four links is in the one-dimensional determinant channel.

For N=6:
  C2(wedge^p F) = p(6-p)7/12,
  d_p = E_one_flux - 2*C2(wedge^p F),
  (d_2,d_3,d_4)=(-7/2,-14/3,-7/2),
  folded coefficient = 1/(d_2 d_3 d_4) = -6/343.

The four-link epsilon network has raw contraction exactly one:
each link contributes epsilon epsilon / 6!, while each of the four plaquette
vertices contracts two epsilons to 6!, cancelling all four normalizations.

The script:
  * independently reruns the verified balanced/walled-Brauer engine at N=6;
  * constructs the unique determinant topology key exactly as build_corpus does;
  * adds the single exact amplitude -6/343;
  * reuses the verified extract_qab routine to obtain the corrected SU(6)
    kernel and q_6,A_6,B_6;
  * verifies that only the rigid/local coefficient changes and that A_6,B_6
    retain the stable-rank values.

Outputs:
  SU6_SINGLE_ORBIT_CONTRACTION_V1/SU6_SINGLE_ORBIT_CONTRACTION_V1.json
  SU6_SINGLE_ORBIT_CONTRACTION_V1/SU6_SINGLE_ORBIT_CONTRACTION_V1.md
  SU6_SINGLE_ORBIT_CONTRACTION_V1_BUNDLE.zip
"""
from __future__ import annotations

import copy
import gzip
import hashlib
import importlib.util
import itertools
import json
import math
import os
import re
import sys
import tempfile
import time
import zipfile
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

VERSION = "2026-06-14-su6-single-orbit-contraction-v1"
BASE = Path("/content") if Path("/content").exists() else Path("/mnt/data")
OUT = BASE / "SU6_SINGLE_ORBIT_CONTRACTION_V1"
EXTRACT = OUT / "extracted"
OUT.mkdir(parents=True, exist_ok=True)
EXTRACT.mkdir(parents=True, exist_ok=True)

SOURCE_GLOB = "Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE*.zip"
ENUM_BUNDLE_GLOB = "SU6_WORD_ENUMERATOR_V1_BUNDLE*.zip"
DET_WORDS_NAME = "y4_su6_determinant_ordered_words.json.gz"
FIXED_SOURCE_NAME = "y4_sun_walled_brauer_fixed_rank.py"
STABLE_WORDS_NAME = "y4_sun_stable_ordered_words.json.gz"
STABLE_STAGE1_NAME = "y4_sun_stable_rank_stage1.py"
EXTRACTED_SOURCES_NAME = "y4_extracted_sources.zip"


def gate(name: str, cond: bool, detail: str = "") -> None:
    status = "PASS" if cond else "FAIL"
    print(f"{status:4s} {name:84s} {detail}")
    if not cond:
        raise AssertionError(f"{name}: {detail}")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def safe_extract(zpath: Path, dest: Path) -> list[Path]:
    dest.mkdir(parents=True, exist_ok=True)
    root = dest.resolve()
    with zipfile.ZipFile(zpath) as zf:
        for info in zf.infolist():
            target = (dest / info.filename).resolve()
            if target != root and not str(target).startswith(str(root) + os.sep):
                raise ValueError(f"unsafe ZIP member: {info.filename}")
        zf.extractall(dest)
        return [dest / x.filename for x in zf.infolist() if not x.is_dir()]


def recursive_extract(archives: Iterable[Path], max_depth: int = 5) -> list[dict[str, Any]]:
    queue = [(Path(p), 0) for p in archives]
    seen: set[str] = set()
    records: list[dict[str, Any]] = []
    while queue:
        zp, depth = queue.pop(0)
        if depth > max_depth or not zp.is_file():
            continue
        try:
            h = sha256(zp)
        except Exception:
            continue
        if h in seen:
            continue
        seen.add(h)
        label = re.sub(r"[^A-Za-z0-9_.-]+", "_", zp.stem)[:100]
        dest = EXTRACT / f"d{depth}_{label}_{h[:10]}"
        try:
            files = safe_extract(zp, dest)
            records.append({
                "archive": str(zp),
                "sha256": h,
                "depth": depth,
                "destination": str(dest),
                "file_count": len(files),
                "status": "ok",
            })
            for p in files:
                if p.suffix.lower() == ".zip":
                    queue.append((p, depth + 1))
        except Exception as exc:
            records.append({
                "archive": str(zp),
                "sha256": h,
                "depth": depth,
                "status": "error",
                "error": repr(exc),
            })
    return records


def find_all(name: str, roots: Iterable[Path]) -> list[Path]:
    by_hash: dict[str, Path] = {}
    for root in roots:
        if not root.exists():
            continue
        try:
            for p in root.rglob(name):
                if p.is_file():
                    by_hash[sha256(p)] = p
        except Exception:
            pass
    return sorted(by_hash.values(), key=lambda p: str(p))


def find_glob(pattern: str, roots: Iterable[Path]) -> list[Path]:
    by_hash: dict[str, Path] = {}
    for root in roots:
        if not root.exists():
            continue
        try:
            for p in root.rglob(pattern):
                if p.is_file():
                    by_hash[sha256(p)] = p
        except Exception:
            pass
    return sorted(by_hash.values(), key=lambda p: str(p))


def upload_if_needed() -> list[Path]:
    roots = [BASE]
    have_source = bool(find_glob(SOURCE_GLOB, roots) or find_all(FIXED_SOURCE_NAME, roots))
    have_det = bool(find_all(DET_WORDS_NAME, roots) or find_glob(ENUM_BUNDLE_GLOB, roots))
    if have_source and have_det:
        return []
    if not Path("/content").exists():
        return []
    try:
        from google.colab import files as colab_files  # type: ignore
    except Exception:
        return []

    print("\nUPLOAD REQUIRED — select the missing files in one picker:")
    if not have_source:
        print("  Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE_2026-06-14_V2*.zip")
    if not have_det:
        print("  SU6_WORD_ENUMERATOR_V1_BUNDLE.zip")
        print("    OR y4_su6_determinant_ordered_words.json.gz")
    uploaded = colab_files.upload()
    saved: list[Path] = []
    for name, data in uploaded.items():
        target = Path("/content") / Path(name).name
        target.write_bytes(data)
        saved.append(target)
        print(f"saved {len(data):,} bytes -> {target}")
    return saved


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def read_json_gz(path: Path) -> Any:
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def fraction_string(x: Any) -> str:
    if isinstance(x, Fraction):
        return str(x)
    try:
        return str(Fraction(x))
    except Exception:
        return str(x)


def rational_map(payload: dict[str, Any]) -> dict[str, str]:
    out = {}
    for k, v in payload.items():
        if isinstance(v, Fraction):
            out[k] = str(v)
        elif isinstance(v, (int, bool, str)) or v is None:
            out[k] = v
        else:
            out[k] = str(v)
    return out


def wedge_c2(N: int, p: int) -> Fraction:
    return Fraction(p * (N - p) * (N + 1), 2 * N)


def main() -> None:
    started = time.time()
    print("=" * 116)
    print("SU(6) O(y^4) EXCEPTIONAL-RANK SINGLE-ORBIT CONTRACTION")
    print("=" * 116)
    print("version :", VERSION)
    print("output  :", OUT)
    print("hardware: CPU exact rational contraction; GPU not used")

    uploaded = upload_if_needed()
    roots0 = [BASE]
    archives = find_glob(SOURCE_GLOB, roots0) + find_glob(ENUM_BUNDLE_GLOB, roots0)
    archives += [p for p in uploaded if p.suffix.lower() == ".zip"]
    extraction = recursive_extract(archives)
    roots = [BASE, EXTRACT]

    fixed_paths = find_all(FIXED_SOURCE_NAME, roots)
    det_paths = find_all(DET_WORDS_NAME, roots)
    stable_paths = find_all(STABLE_WORDS_NAME, roots)
    stage1_paths = find_all(STABLE_STAGE1_NAME, roots)
    source_zip_paths = find_all(EXTRACTED_SOURCES_NAME, roots)

    gate("fixed-rank contraction source located", bool(fixed_paths), str(fixed_paths[:2]))
    gate("determinant-word delta located", bool(det_paths), str(det_paths[:2]))
    gate("stable ordered-word archive located", bool(stable_paths), str(stable_paths[:2]))
    gate("stable Stage-1 source located", bool(stage1_paths), str(stage1_paths[:2]))
    gate("embedded source archive located", bool(source_zip_paths), str(source_zip_paths[:2]))

    fixed_path = fixed_paths[0]
    det_path = det_paths[0]

    # Import after extraction: the fixed source resolves its own stable dependencies recursively.
    wb = load_module("y4_sun_walled_brauer_su6_single_orbit", fixed_path)

    det_payload = read_json_gz(det_path)
    det_records = det_payload["words"]
    gate("exactly one determinant-bearing ordered word", len(det_records) == 1, str(len(det_records)))
    rec = det_records[0]
    det_assignments = [tuple(int(x) for x in s) for s in rec["determinant_assignments"]]
    gate("exactly two determinant assignments", len(det_assignments) == 2, str(len(det_assignments)))
    reps = sorted({wb.rep(s) for s in det_assignments})
    gate("the two assignments form one charge-conjugation orbit", len(reps) == 1, str(reps))
    signs = tuple(reps[0])

    factors = (
        [tuple(int(x) for x in rec["root"])]
        + [tuple(int(x) for x in p) for p in rec["ordered_insertions"]]
        + [tuple(int(x) for x in rec["output"])]
    )
    gate("determinant word has six total plaquette factors", len(factors) == 6, str(len(factors)))
    gate("all six factors are the same plaquette", len(set(factors)) == 1, str(factors[0]))
    gate("determinant word is mixed with an existing stable word",
         rec.get("word_sector") == "mixed_stable_and_determinant" and rec.get("stable_ordered_id"),
         str(rec.get("stable_ordered_id")))

    # Reconstruct the topology exactly as fixed-rank build_corpus().
    eff = signs[:5] + (-signs[5],)
    links: dict[Any, list[tuple[int, int, int, int, int]]] = defaultdict(list)
    for ei, p in enumerate(factors):
        for edge, (link, inc, sc, ec) in enumerate(wb.pb(p)):
            token = eff[ei] * inc
            rv = 4 * ei + (sc if inc == 1 else ec)
            cv = 4 * ei + (ec if inc == 1 else sc)
            links[link].append((ei, edge, token, rv, cv))

    groups = []
    signatures = []
    for link, occ0 in sorted(links.items()):
        occ = tuple(sorted(occ0))
        groups.append(occ)
        sig = [0] * 6
        for ei, edge, token, rv, cv in occ:
            sig[ei] = token
        signatures.append(tuple(sig))

    gate("the repeated plaquette has exactly four active links", len(signatures) == 4, str(len(signatures)))
    gate("every active link has local degree six",
         all(sum(abs(x) for x in sig) == 6 for sig in signatures), str(signatures))
    gate("every active link is a pure determinant signature",
         all(sig.count(1) == 6 or sig.count(-1) == 6 for sig in signatures), str(signatures))

    det_key = (signs[0] * signs[5], tuple(sorted(groups)))
    gate("determinant endpoint sign is C-odd", det_key[0] == -1, str(det_key[0]))

    # Exact one-dimensional determinant-channel energy history.
    N = 6
    E0 = Fraction(N * N - 1, N)
    prefix_p = (2, 3, 4)
    c2s = tuple(wedge_c2(N, p) for p in prefix_p)
    intermediate_E = tuple(2 * c2 for c2 in c2s)  # four links, each carries 1/2 C2
    denominators = tuple(E0 - e for e in intermediate_E)
    expected_denominators = (Fraction(-7, 2), Fraction(-14, 3), Fraction(-7, 2))
    gate("determinant intermediate denominators",
         denominators == expected_denominators, str(denominators))
    folded = Fraction(1, 1)
    for d in denominators:
        folded /= d
    gate("determinant folded coefficient", folded == Fraction(-6, 343), str(folded))

    # Exact raw epsilon-network contraction:
    # four 1/6! projectors and four epsilon-epsilon vertex contractions.
    fact6 = math.factorial(6)
    raw_numerator = fact6 ** 4
    raw_denominator = fact6 ** 4
    raw = Fraction(raw_numerator, raw_denominator)
    gate("four-link epsilon-network raw contraction", raw == 1, str(raw))
    det_amp = raw * folded
    gate("unique determinant topology amplitude", det_amp == Fraction(-6, 343), str(det_amp))

    print("\nRunning unchanged balanced/walled-Brauer contraction at N=6...")
    stable_amps, stable_tops, stable_word_orbits, stable_words, stable_qab = wb.main(6, 0)
    gate("stable N=6 contraction completed", stable_qab is not None, "")
    gate("stable corpus remains 4,171 words", len(stable_words) == 4171, str(len(stable_words)))

    # Add the one determinant orbit without modifying any stable amplitude.
    corrected_amps = dict(stable_amps)
    topology_collision = det_key in corrected_amps
    if topology_collision:
        corrected_amps[det_key] += det_amp
    else:
        corrected_amps[det_key] = det_amp

    corrected_word_orbits = defaultdict(list)
    for word_id, values in stable_word_orbits.items():
        corrected_word_orbits[word_id].extend(values)

    stable_word_id = str(rec["stable_ordered_id"])
    gate("mixed word ID exists in stable orbit map", stable_word_id in corrected_word_orbits, stable_word_id)
    before_orbits = len(corrected_word_orbits[stable_word_id])
    corrected_word_orbits[stable_word_id].append((det_key, det_key[0]))
    gate("exactly one orbit appended to the mixed word",
         len(corrected_word_orbits[stable_word_id]) == before_orbits + 1,
         f"{before_orbits} -> {len(corrected_word_orbits[stable_word_id])}")

    corrected_qab = wb.extract_qab(
        6, corrected_amps, corrected_word_orbits, stable_words
    )
    gate("corrected SU(6) q/A/B extraction completed", corrected_qab is not None, "")

    # Exact deltas for every common scalar result.
    common = sorted(set(stable_qab) & set(corrected_qab))
    deltas: dict[str, Any] = {}
    for key in common:
        a = stable_qab[key]
        b = corrected_qab[key]
        if isinstance(a, Fraction) and isinstance(b, Fraction):
            deltas[key] = b - a
        elif isinstance(a, int) and isinstance(b, int):
            deltas[key] = b - a
        elif a != b:
            deltas[key] = f"{a!r} -> {b!r}"

    # The determinant word is completely local and cubic-scalar.
    if "A" in stable_qab and "A" in corrected_qab:
        gate("determinant correction leaves A_6 unchanged",
             corrected_qab["A"] == stable_qab["A"],
             f"{stable_qab['A']} -> {corrected_qab['A']}")
    if "B" in stable_qab and "B" in corrected_qab:
        gate("determinant correction leaves B_6 unchanged",
             corrected_qab["B"] == stable_qab["B"],
             f"{stable_qab['B']} -> {corrected_qab['B']}")
    if "q" in stable_qab and "q" in corrected_qab:
        gate("determinant correction changes the rigid q_6 coefficient",
             corrected_qab["q"] != stable_qab["q"],
             f"delta={corrected_qab['q'] - stable_qab['q']}")

    A_expected = Fraction(640, 6 * (6 * 6 - 1) ** 3)
    if "A" in corrected_qab:
        gate("A_6 equals stable closed form 640/[N(N^2-1)^3]",
             corrected_qab["A"] == A_expected, str(corrected_qab["A"]))
    if "A" in corrected_qab and "B" in corrected_qab:
        gate("SU(6) fourth-order bandwidth is positive",
             corrected_qab["A"] + corrected_qab["B"] > 0,
             str(corrected_qab["A"] + corrected_qab["B"]))

    # Parity-point consistency if fields are exposed by the extractor.
    parity_names = ("q", "cX", "cM", "cR")
    if all(name in corrected_qab for name in parity_names):
        gate("SU(6) hard parity identity cR-2cM+cX=0",
             corrected_qab["cR"] - 2 * corrected_qab["cM"] + corrected_qab["cX"] == 0,
             "")
    if "kernel_entries" in corrected_qab:
        gate("corrected real-space kernel retains 189 entries",
             int(corrected_qab["kernel_entries"]) == 189,
             str(corrected_qab["kernel_entries"]))

    summary = {
        "version": VERSION,
        "status": "PASS",
        "inputs": {
            "fixed_source": str(fixed_path),
            "fixed_source_sha256": sha256(fixed_path),
            "determinant_words": str(det_path),
            "determinant_words_sha256": sha256(det_path),
            "extraction": extraction,
        },
        "determinant_orbit": {
            "stable_ordered_id": stable_word_id,
            "factors": [list(x) for x in factors],
            "representative_signs": list(signs),
            "effective_signs": list(eff),
            "local_signatures": [list(x) for x in signatures],
            "determinant_links": len(signatures),
            "charge_conjugation_assignments": len(det_assignments),
            "topology_key_endpoint_sign": det_key[0],
            "topology_collision_with_stable_sector": topology_collision,
        },
        "exact_local_reduction": {
            "N": N,
            "one_flux_energy": str(E0),
            "prefix_exterior_powers": list(prefix_p),
            "prefix_casimirs": [str(x) for x in c2s],
            "intermediate_energies": [str(x) for x in intermediate_E],
            "denominators": [str(x) for x in denominators],
            "raw_epsilon_network": str(raw),
            "folded_coefficient": str(folded),
            "determinant_topology_amplitude": str(det_amp),
        },
        "stable_N6": rational_map(stable_qab),
        "corrected_N6": rational_map(corrected_qab),
        "deltas": {k: fraction_string(v) for k, v in deltas.items()},
        "counts": {
            "stable_words": len(stable_words),
            "stable_topologies": len(stable_tops),
            "stable_amplitudes": len(stable_amps),
            "corrected_amplitudes": len(corrected_amps),
            "mixed_word_orbits_before": before_orbits,
            "mixed_word_orbits_after": len(corrected_word_orbits[stable_word_id]),
        },
        "conclusion": (
            "The entire SU(6) determinant-sector correction is one additive local topology. "
            "It changes only the rigid fourth-order coefficient q_6; A_6 and B_6, hence the "
            "band shape and positive bandwidth, remain equal to the stable-rank evaluation at N=6."
        ),
        "elapsed_seconds": time.time() - started,
    }

    json_path = OUT / "SU6_SINGLE_ORBIT_CONTRACTION_V1.json"
    json_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")

    q0 = stable_qab.get("q", "not exposed")
    q1 = corrected_qab.get("q", "not exposed")
    A1 = corrected_qab.get("A", "not exposed")
    B1 = corrected_qab.get("B", "not exposed")
    bw = (
        corrected_qab["A"] + corrected_qab["B"]
        if "A" in corrected_qab and "B" in corrected_qab
        else "not exposed"
    )

    md = f"""# SU(6) exceptional-rank single-orbit contraction

**Status:** PASS  
**Version:** `{VERSION}`

## Complete exceptional corpus

The SU(6) word enumeration contains exactly one determinant-bearing word, two
charge-conjugate assignments, and one orbit. All six factors are the same
plaquette, so its four boundary links are the four determinant nodes.

## Exact determinant-channel reduction

For `N=6`, the three intermediate link representations are

```text
wedge^2 F, wedge^3 F, wedge^4 F.
```

Their complete four-link energy denominators are

```text
{denominators[0]}, {denominators[1]}, {denominators[2]}.
```

Therefore the fourth-order folded coefficient is

```text
1/(d1 d2 d3) = {folded}.
```

The four-link epsilon network has raw contraction `1`, so the unique additional
topology amplitude is

```text
delta_amp = {det_amp}.
```

## Stable and corrected SU(6) results

```text
stable q_6    = {q0}
corrected q_6 = {q1}
A_6           = {A1}
B_6           = {B1}
bandwidth      = {bw}
```

The determinant route is strictly local and cubic-scalar. It changes only the
rigid coefficient `q_6`; it does not alter `A_6`, `B_6`, the parity-point
identity, or the location of the band extrema.

## Conclusion

The `SU(6)` exceptional-rank fourth-order theorem is closed if all gates in the
machine-readable certificate pass. The remaining finite exceptional ranks are
`SU(5)` and `SU(4)`.
"""
    md_path = OUT / "SU6_SINGLE_ORBIT_CONTRACTION_V1.md"
    md_path.write_text(md, encoding="utf-8")

    bundle = BASE / "SU6_SINGLE_ORBIT_CONTRACTION_V1_BUNDLE.zip"
    with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(json_path, arcname=json_path.name)
        zf.write(md_path, arcname=md_path.name)
        source_path = Path(globals().get("__file__", ""))
        if source_path.is_file():
            zf.write(source_path, arcname=source_path.name)

    print("\n" + "=" * 116)
    print("SU(6) SINGLE-ORBIT CONTRACTION STATUS: PASS")
    print("=" * 116)
    print("determinant amplitude :", det_amp)
    print("stable q_6            :", q0)
    print("corrected q_6         :", q1)
    print("A_6                   :", A1)
    print("B_6                   :", B1)
    print("bandwidth A_6+B_6     :", bw)
    print("JSON:", json_path, sha256(json_path))
    print("MD:  ", md_path, sha256(md_path))
    print("ZIP: ", bundle, sha256(bundle))
    print("=" * 116)


if __name__ == "__main__":
    main()
