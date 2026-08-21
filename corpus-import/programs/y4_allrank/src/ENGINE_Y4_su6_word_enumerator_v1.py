#!/usr/bin/env python3
"""
SU(6) exceptional-rank O(y^4) ordered-word enumerator.

One-block Colab/local stage. Upload the full symbolic source bundle when
prompted. The script reuses the verified stable-rank geometry generator but
replaces the local exact-balance condition

    sum_j row[j] * sign[j] == 0

by the exact SU(6) N-ality condition

    sum_j row[j] * sign[j] == 0 (mod 6).

It then proves that:
  * the original 4,171 stable ordered words and all 33,500 stable sign
    assignments are reproduced byte-semantically;
  * the stable sector is an unchanged subset of the SU(6) sector;
  * every newly admitted assignment contains at least one and only local
    determinant nodes with charge +6 or -6, equivalently (6,0)/(0,6);
  * no denominator/fusion data are modified at this stage.

Outputs:
  SU6_WORD_ENUMERATOR_V1/SU6_WORD_ENUMERATOR_V1.json
  SU6_WORD_ENUMERATOR_V1/SU6_WORD_ENUMERATOR_V1.md
  SU6_WORD_ENUMERATOR_V1/y4_su6_ordered_words.json.gz
  SU6_WORD_ENUMERATOR_V1/y4_su6_determinant_ordered_words.json.gz
  SU6_WORD_ENUMERATOR_V1_BUNDLE.zip

This stage enumerates and certifies the exceptional word/sign corpus. It does
not yet perform the epsilon_6 trace-network contraction.
"""
from __future__ import annotations

import gzip
import hashlib
import importlib.util
import itertools
import json
import os
import re
import sys
import time
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

VERSION = "2026-06-14-su6-word-enumerator-v1"
BASE = Path("/content") if Path("/content").exists() else Path("/mnt/data")
OUT = BASE / "SU6_WORD_ENUMERATOR_V1"
EXTRACT = OUT / "extracted"
OUT.mkdir(parents=True, exist_ok=True)
EXTRACT.mkdir(parents=True, exist_ok=True)

PREFERRED_BUNDLE_GLOB = "Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE*.zip"
REQUIRED_STAGE1 = "y4_sun_stable_rank_stage1.py"
REQUIRED_WORDS = "y4_sun_stable_ordered_words.json.gz"


def gate(name: str, cond: bool, detail: str = "") -> None:
    status = "PASS" if cond else "FAIL"
    print(f"{status:4s} {name:78s} {detail}")
    if not cond:
        raise AssertionError(f"{name}: {detail}")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def write_json(path: Path, payload: Any) -> str:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return sha256(path)


def write_json_gz(path: Path, payload: Any) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    with path.open("wb") as raw_file:
        with gzip.GzipFile(filename="", mode="wb", compresslevel=9, fileobj=raw_file, mtime=0) as f:
            f.write(raw)
    return sha256(path)


def read_json_gz(path: Path) -> Any:
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def safe_extract(zpath: Path, dest: Path) -> list[Path]:
    dest.mkdir(parents=True, exist_ok=True)
    root = dest.resolve()
    with zipfile.ZipFile(zpath) as zf:
        for info in zf.infolist():
            target = (dest / info.filename).resolve()
            if target != root and not str(target).startswith(str(root) + os.sep):
                raise ValueError(f"unsafe ZIP member: {info.filename}")
        zf.extractall(dest)
        return [dest / i.filename for i in zf.infolist() if not i.is_dir()]


def recursive_extract(archives: Iterable[Path], max_depth: int = 4) -> list[dict[str, Any]]:
    queue = [(p, 0) for p in archives]
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
        label = re.sub(r"[^A-Za-z0-9_.-]+", "_", zp.stem)[:90]
        dest = EXTRACT / f"d{depth}_{label}_{h[:10]}"
        try:
            files = safe_extract(zp, dest)
            records.append({
                "archive": str(zp), "sha256": h, "depth": depth,
                "destination": str(dest), "file_count": len(files), "status": "ok",
            })
            for p in files:
                if p.suffix.lower() == ".zip":
                    queue.append((p, depth + 1))
        except Exception as exc:
            records.append({
                "archive": str(zp), "sha256": h, "depth": depth,
                "status": "error", "error": repr(exc),
            })
    return records


def upload_if_needed() -> list[Path]:
    candidates = list(BASE.rglob(PREFERRED_BUNDLE_GLOB))
    candidates += list(BASE.rglob(REQUIRED_STAGE1))
    candidates += list(BASE.rglob(REQUIRED_WORDS))
    if candidates:
        return candidates
    if not Path("/content").exists():
        return []
    try:
        from google.colab import files as colab_files  # type: ignore
    except Exception:
        return []
    print("\nUPLOAD REQUIRED — select the full symbolic source bundle:")
    print("  Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE_2026-06-14_V2*.zip")
    uploaded = colab_files.upload()
    saved: list[Path] = []
    for name, data in uploaded.items():
        target = Path("/content") / Path(name).name
        # colab_files.upload normally writes the file already, but write_bytes
        # is deterministic and harmless.
        target.write_bytes(data)
        saved.append(target)
        print(f"saved {len(data):,} bytes -> {target}")
    return saved


def find_unique(name: str, roots: Iterable[Path]) -> list[Path]:
    found: dict[str, Path] = {}
    for root in roots:
        if not root.exists():
            continue
        try:
            for p in root.rglob(name):
                if p.is_file():
                    found[sha256(p)] = p
        except Exception:
            pass
    return sorted(found.values(), key=lambda p: str(p))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def bit_indices(mask: int) -> list[int]:
    return [i for i in range(64) if (mask >> i) & 1]


def key_from_record(record: dict[str, Any]):
    return (
        tuple(tuple(int(x) for x in p) for p in record["ordered_insertions"]),
        tuple(int(x) for x in record["output"]),
    )


def assignments_from_record(record: dict[str, Any]) -> set[tuple[int, ...]]:
    return {tuple(int(x) for x in s) for s in record["exact_balance_assignments"]}


def main() -> None:
    started = time.time()
    print("=" * 108)
    print("SU(6) O(y^4) EXCEPTIONAL-RANK ORDERED-WORD ENUMERATOR")
    print("=" * 108)
    print("version :", VERSION)
    print("output  :", OUT)
    print("hardware: CPU exact combinatorics; GPU not used")

    initial = upload_if_needed()
    archives = [p for p in initial if p.suffix.lower() == ".zip"]
    extraction = recursive_extract(archives)
    roots = [BASE, EXTRACT]

    stage1_paths = find_unique(REQUIRED_STAGE1, roots)
    words_paths = find_unique(REQUIRED_WORDS, roots)
    gate("stable-rank Stage-1 source located", bool(stage1_paths), str(stage1_paths[:3]))
    gate("4,171-word stable archive located", bool(words_paths), str(words_paths[:3]))

    st_path = stage1_paths[0]
    words_path = words_paths[0]
    st = load_module("y4_sun_stable_rank_stage1_su6_enum", st_path)

    required_names = [
        "locate_complete_source", "decode_stage1", "load_module_from_source",
        "ensure_stage0_supports", "rows_for", "SIGNS", "FULL_MASK",
    ]
    missing = [name for name in required_names if not hasattr(st, name)]
    gate("stable Stage-1 runtime contract available", not missing, str(missing))
    gate("stable sign basis contains 64 assignments", len(st.SIGNS) == 64, str(len(st.SIGNS)))

    complete_source = st.locate_complete_source(None)
    stage0_source, stage1_source = st.decode_stage1(complete_source)
    stage0 = st.load_module_from_source("y4_stage0_su6_enum", stage0_source)
    _stage1_su3 = st.load_module_from_source("y4_stage1_su6_enum", stage1_source)
    support_path = st.ensure_stage0_supports(stage0, stage0_source, None)
    support_payload = read_json_gz(Path(support_path))
    supports = [
        tuple(tuple(int(x) for x in p) for p in record)
        for record in support_payload["supports"]
    ]
    gate("Stage-0 connected support count", len(supports) == 182440, f"{len(supports):,}")

    signs_basis = tuple(tuple(int(x) for x in s) for s in st.SIGNS)
    full_mask = int(st.FULL_MASK)
    gate("FULL_MASK covers all 64 assignments", full_mask == (1 << 64) - 1, hex(full_mask))

    row_cache_stable: dict[tuple[int, ...], int] = {}
    row_cache_su6: dict[tuple[int, ...], int] = {}
    max_local_degree = 0
    observed_row_charges: Counter[int] = Counter()

    def row_mask(row: tuple[int, ...], *, su6: bool) -> int:
        nonlocal max_local_degree
        cache = row_cache_su6 if su6 else row_cache_stable
        if row in cache:
            return cache[row]
        degree = sum(abs(int(x)) for x in row)
        max_local_degree = max(max_local_degree, degree)
        mask = 0
        for index, signs in enumerate(signs_basis):
            charge = sum(int(row[j]) * int(signs[j]) for j in range(6))
            observed_row_charges[charge] += 1
            ok = (charge % 6 == 0) if su6 else (charge == 0)
            if ok:
                mask |= 1 << index
        cache[row] = mask
        return mask

    def mask_for(stage0_runtime, word, output, *, su6: bool) -> int:
        mask = full_mask
        for row0 in st.rows_for(stage0_runtime, word, output):
            row = tuple(int(x) for x in row0)
            mask &= row_mask(row, su6=su6)
            if mask == 0:
                break
        return mask

    stable_survivors: dict[Any, int] = {}
    su6_survivors: dict[Any, int] = {}
    candidate_pairs = 0

    for index, multiset in enumerate(supports, start=1):
        for output in stage0.candidate_outputs(multiset):
            candidate_pairs += 1
            stable_mask = mask_for(stage0, multiset, output, su6=False)
            su6_mask = mask_for(stage0, multiset, output, su6=True)
            if stable_mask:
                key = stage0.canonical_support_output(multiset, output)
                stable_survivors[key] = 1
            if su6_mask:
                key = stage0.canonical_support_output(multiset, output)
                su6_survivors[key] = 1
            if stable_mask & ~su6_mask:
                raise AssertionError("stable assignment absent from SU(6) N-ality sector")
        if index % 40000 == 0:
            print(
                f"[geometry] supports={index:,}/{len(supports):,} "
                f"stable_classes={len(stable_survivors):,} su6_classes={len(su6_survivors):,}",
                flush=True,
            )

    gate("candidate support/output pair count", candidate_pairs == 895524, f"{candidate_pairs:,}")
    gate("stable support/output classes reproduced", len(stable_survivors) == 439, str(len(stable_survivors)))
    gate("stable support classes are an SU(6) subset",
         set(stable_survivors).issubset(set(su6_survivors)),
         f"stable={len(stable_survivors)} su6={len(su6_survivors)}")

    def ordered_keys_from(survivors: dict[Any, int]) -> set[Any]:
        keys = set()
        for multiset, output in survivors:
            for word in set(itertools.permutations(multiset)):
                keys.add(stage0.canonical_ordered_transition(word, output))
        return keys

    stable_ordered_keys = ordered_keys_from(stable_survivors)
    su6_ordered_keys = ordered_keys_from(su6_survivors)
    gate("stable ordered-key candidates are an SU(6) subset",
         stable_ordered_keys.issubset(su6_ordered_keys),
         f"stable={len(stable_ordered_keys)} su6={len(su6_ordered_keys)}")

    stable_ordered: dict[Any, int] = {}
    su6_ordered: dict[Any, int] = {}
    determinant_ordered: dict[Any, int] = {}

    for idx, (word, output) in enumerate(sorted(su6_ordered_keys), start=1):
        stable_mask = mask_for(stage0, word, output, su6=False)
        su6_mask = mask_for(stage0, word, output, su6=True)
        det_mask = su6_mask & ~stable_mask
        if stable_mask:
            stable_ordered[(word, output)] = stable_mask
        if su6_mask:
            su6_ordered[(word, output)] = su6_mask
        if det_mask:
            determinant_ordered[(word, output)] = det_mask
        if idx % 10000 == 0:
            print(
                f"[ordered] keys={idx:,}/{len(su6_ordered_keys):,} "
                f"stable={len(stable_ordered):,} determinant={len(determinant_ordered):,}",
                flush=True,
            )

    stable_assignments = sum(mask.bit_count() for mask in stable_ordered.values())
    stable_c_orbits = stable_assignments // 2
    gate("stable ordered words reproduced", len(stable_ordered) == 4171, str(len(stable_ordered)))
    gate("stable sign assignments reproduced", stable_assignments == 33500, f"{stable_assignments:,}")
    gate("stable charge-conjugation orbits reproduced", stable_c_orbits == 16750, f"{stable_c_orbits:,}")

    archive_payload = read_json_gz(words_path)
    archive_records = archive_payload["words"]
    gate("reference archive record count", len(archive_records) == 4171, str(len(archive_records)))
    archive_map = {key_from_record(r): assignments_from_record(r) for r in archive_records}
    computed_map = {
        key: {signs_basis[i] for i in bit_indices(mask)}
        for key, mask in stable_ordered.items()
    }
    gate("stable ordered-word key set exactly matches reference archive",
         set(computed_map) == set(archive_map),
         f"computed={len(computed_map)} archive={len(archive_map)}")
    mismatch_keys = [k for k in archive_map if archive_map[k] != computed_map.get(k)]
    gate("all stable sign assignments exactly match reference archive",
         not mismatch_keys, f"mismatches={len(mismatch_keys)}")

    determinant_assignment_count = sum(mask.bit_count() for mask in determinant_ordered.values())
    new_word_keys = set(su6_ordered) - set(stable_ordered)
    mixed_word_keys = set(determinant_ordered) & set(stable_ordered)
    pure_det_word_keys = set(determinant_ordered) - set(stable_ordered)
    gate("every determinant-bearing word is in the SU(6) corpus",
         set(determinant_ordered).issubset(set(su6_ordered)))
    gate("new SU(6) words are exactly pure determinant words",
         new_word_keys == pure_det_word_keys,
         f"new={len(new_word_keys)} pure_det={len(pure_det_word_keys)}")
    gate("determinant assignment count is even under charge conjugation",
         determinant_assignment_count % 2 == 0, str(determinant_assignment_count))

    det_charge_hist: Counter[int] = Counter()
    det_link_count_hist: Counter[int] = Counter()
    det_sector_hist: Counter[str] = Counter()
    bad_det_assignments: list[dict[str, Any]] = []
    max_det_links = 0

    for (word, output), det_mask in determinant_ordered.items():
        rows = [tuple(int(x) for x in r) for r in st.rows_for(stage0, word, output)]
        for sign_index in bit_indices(det_mask):
            signs = signs_basis[sign_index]
            charges = [sum(row[j] * signs[j] for j in range(6)) for row in rows]
            exceptional = [q for q in charges if q != 0]
            det_link_count_hist[len(exceptional)] += 1
            max_det_links = max(max_det_links, len(exceptional))
            valid = bool(exceptional) and all(abs(q) == 6 for q in exceptional)
            if not valid and len(bad_det_assignments) < 20:
                bad_det_assignments.append({
                    "word": [list(p) for p in word], "output": list(output),
                    "signs": list(signs), "charges": charges,
                })
            for q in exceptional:
                det_charge_hist[q] += 1
                det_sector_hist["(6,0)" if q == 6 else "(0,6)"] += 1
                # A charge +/-6 must come from exactly six active local factors.
                row = rows[charges.index(q)]
                if sum(abs(x) for x in row) != 6 and len(bad_det_assignments) < 20:
                    bad_det_assignments.append({"reason": "degree_not_6", "row": row, "q": q})

    gate("every added assignment contains a determinant node", not bad_det_assignments,
         f"bad={len(bad_det_assignments)}")
    gate("only local charges +6 and -6 occur in the determinant sector",
         set(det_charge_hist).issubset({-6, 6}), str(dict(det_charge_hist)))
    gate("maximum local tensor degree remains six", max_local_degree <= 6, str(max_local_degree))

    # Preserve reference IDs for the unchanged stable words.
    archive_id = {key_from_record(r): r["ordered_id"] for r in archive_records}

    all_records: list[dict[str, Any]] = []
    det_records: list[dict[str, Any]] = []
    for record_index, (key, su6_mask) in enumerate(sorted(su6_ordered.items()), start=1):
        word, output = key
        stable_mask = stable_ordered.get(key, 0)
        det_mask = determinant_ordered.get(key, 0)
        stable_assign = [list(signs_basis[i]) for i in bit_indices(stable_mask)]
        det_assign = [list(signs_basis[i]) for i in bit_indices(det_mask)]
        rec = {
            "su6_ordered_id": f"S6N4-{record_index:05d}",
            "stable_ordered_id": archive_id.get(key),
            "root": list(stage0.ROOT),
            "ordered_insertions": [list(p) for p in word],
            "output": list(output),
            "su6_assignment_count": su6_mask.bit_count(),
            "stable_assignment_count": stable_mask.bit_count(),
            "determinant_assignment_count": det_mask.bit_count(),
            "stable_assignments": stable_assign,
            "determinant_assignments": det_assign,
            "word_sector": (
                "mixed_stable_and_determinant" if stable_mask and det_mask
                else "stable_only" if stable_mask
                else "determinant_only"
            ),
        }
        all_records.append(rec)
        if det_mask:
            det_records.append(rec)

    all_path = OUT / "y4_su6_ordered_words.json.gz"
    det_path = OUT / "y4_su6_determinant_ordered_words.json.gz"
    all_sha = write_json_gz(all_path, {
        "meta": {
            "version": VERSION,
            "rank": 6,
            "criterion": "local charge sum is 0 modulo 6",
            "stable_reference": str(words_path),
            "stable_reference_sha256": sha256(words_path),
            "stage1_source": str(st_path),
            "stage1_source_sha256": sha256(st_path),
        },
        "counts": {
            "ordered_words": len(all_records),
            "stable_words": len(stable_ordered),
            "determinant_bearing_words": len(det_records),
            "new_determinant_only_words": len(new_word_keys),
            "mixed_words": len(mixed_word_keys),
            "stable_assignments": stable_assignments,
            "determinant_assignments": determinant_assignment_count,
        },
        "words": all_records,
    })
    det_sha = write_json_gz(det_path, {
        "meta": {
            "version": VERSION,
            "rank": 6,
            "scope": "only assignments absent from the N>=7 stable-rank corpus",
            "criterion": "at least one local charge is +6 or -6; all others are 0 mod 6",
        },
        "counts": {
            "determinant_bearing_words": len(det_records),
            "new_determinant_only_words": len(new_word_keys),
            "mixed_words": len(mixed_word_keys),
            "determinant_assignments": determinant_assignment_count,
            "determinant_charge_conjugation_orbits": determinant_assignment_count // 2,
        },
        "words": det_records,
    })

    summary = {
        "version": VERSION,
        "status": "PASS",
        "inputs": {
            "stage1_source": str(st_path),
            "stage1_source_sha256": sha256(st_path),
            "stable_words": str(words_path),
            "stable_words_sha256": sha256(words_path),
            "complete_source": str(complete_source),
            "support_path": str(support_path),
            "support_sha256": sha256(Path(support_path)),
            "extraction": extraction,
        },
        "stable_regression": {
            "support_output_classes": len(stable_survivors),
            "ordered_words": len(stable_ordered),
            "sign_assignments": stable_assignments,
            "charge_conjugation_orbits": stable_c_orbits,
            "archive_key_set_exact": True,
            "archive_assignment_sets_exact": True,
        },
        "su6": {
            "support_output_classes": len(su6_survivors),
            "ordered_words": len(su6_ordered),
            "total_assignments": sum(mask.bit_count() for mask in su6_ordered.values()),
            "determinant_bearing_words": len(determinant_ordered),
            "new_determinant_only_words": len(new_word_keys),
            "mixed_words": len(mixed_word_keys),
            "determinant_assignments": determinant_assignment_count,
            "determinant_charge_conjugation_orbits": determinant_assignment_count // 2,
            "determinant_local_charge_histogram": {str(k): v for k, v in sorted(det_charge_hist.items())},
            "determinant_sector_histogram": dict(sorted(det_sector_hist.items())),
            "determinant_links_per_assignment_histogram": {
                str(k): v for k, v in sorted(det_link_count_hist.items())
            },
            "max_determinant_links_in_one_assignment": max_det_links,
            "max_local_degree": max_local_degree,
        },
        "outputs": {
            "all_words": str(all_path), "all_words_sha256": all_sha,
            "determinant_words": str(det_path), "determinant_words_sha256": det_sha,
        },
        "next_stage": (
            "Keep the verified 4,171-word stable contraction unchanged. Build a second corpus from "
            "y4_su6_determinant_ordered_words.json.gz and route each local +/-6 node through "
            "epsilon_6 epsilon_6 / 720; then add its exact kernel contribution to the stable N=6 evaluation."
        ),
        "elapsed_seconds": time.time() - started,
    }

    json_path = OUT / "SU6_WORD_ENUMERATOR_V1.json"
    json_sha = write_json(json_path, summary)

    md = f"""# SU(6) exceptional-rank ordered-word enumeration

**Status:** PASS  
**Version:** `{VERSION}`

## Stable-rank regression

- Stable support/output classes: **{len(stable_survivors):,}**
- Stable ordered words: **{len(stable_ordered):,}**
- Stable sign assignments: **{stable_assignments:,}**
- Stable charge-conjugation orbits: **{stable_c_orbits:,}**
- Reference archive key set: **exact match**
- Reference assignment sets: **exact match**

## SU(6) N-ality extension

The local admissibility condition was changed only from

```text
charge = 0
```

to

```text
charge = 0 mod 6.
```

Counts:

- SU(6) support/output classes: **{len(su6_survivors):,}**
- SU(6) ordered words: **{len(su6_ordered):,}**
- Determinant-bearing words: **{len(determinant_ordered):,}**
- New determinant-only words: **{len(new_word_keys):,}**
- Mixed stable/determinant words: **{len(mixed_word_keys):,}**
- Added determinant assignments: **{determinant_assignment_count:,}**
- Added charge-conjugation orbits: **{determinant_assignment_count // 2:,}**

Every added assignment contains at least one local charge `+6` or `-6`, and no
other nonzero local charge occurs. These are exactly the `(6,0)` and `(0,6)`
determinant sectors.

## Outputs

- `{all_path.name}` — complete SU(6) word/sign corpus
- `{det_path.name}` — determinant-sector delta relative to stable rank
- `{json_path.name}` — machine-readable certificate

## Next exact stage

Do not alter the verified stable contraction. Contract the determinant delta as
a separate additive corpus. At every local `+6` or `-6` node use

```text
(1/720) * sum_{{sigma in S6}} sgn(sigma) prod_a delta(i_a,j_{{sigma(a)}}).
```

All balanced local nodes retain the existing walled-Brauer library. Add the
resulting exact determinant kernel to the stable engine evaluated at `N=6`.
"""
    md_path = OUT / "SU6_WORD_ENUMERATOR_V1.md"
    md_path.write_text(md, encoding="utf-8")
    md_sha = sha256(md_path)

    bundle = BASE / "SU6_WORD_ENUMERATOR_V1_BUNDLE.zip"
    with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in (json_path, md_path, all_path, det_path):
            zf.write(p, arcname=p.name)
        source_path = Path(globals().get("__file__", ""))
        if source_path.is_file():
            zf.write(source_path, arcname=source_path.name)

    print("\n" + "=" * 108)
    print("SU(6) WORD ENUMERATOR STATUS: PASS")
    print("=" * 108)
    print(f"stable words              : {len(stable_ordered):,}")
    print(f"SU(6) words               : {len(su6_ordered):,}")
    print(f"determinant-bearing words : {len(determinant_ordered):,}")
    print(f"new determinant-only words: {len(new_word_keys):,}")
    print(f"mixed words               : {len(mixed_word_keys):,}")
    print(f"determinant assignments   : {determinant_assignment_count:,}")
    print(f"determinant C-orbits       : {determinant_assignment_count // 2:,}")
    print("JSON:", json_path, json_sha)
    print("MD:  ", md_path, md_sha)
    print("ALL: ", all_path, all_sha)
    print("DET: ", det_path, det_sha)
    print("ZIP: ", bundle, sha256(bundle))
    print("=" * 108)


if __name__ == "__main__":
    main()
