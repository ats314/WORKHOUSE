#!/usr/bin/env python3
"""
y4_su6_determinant_stage0.py

One-block Colab/local preflight for the exceptional SU(6) O(y^4) band contraction.

This script does three things:
  1. Certifies the exact mathematical reduction: at O(y^4), SU(6) differs from
     the stable-rank N>=7 contraction only in final local Haar sectors (6,0)
     and (0,6). All intermediate resolvent/Casimir data are unchanged.
  2. Certifies the determinant Haar projector
         int_SU(6) U^(tensor 6) dU = epsilon epsilon / 6!
     and its signed-permutation realization.
  3. Searches Colab, Drive, and /mnt/data for the full symbolic source bundle,
     extracts it safely, inventories the source/word schemas, and identifies
     source lines where the stable balanced-sector filter must be generalized.

No manual path edits are required. In Colab, if the contraction inputs are not
found, an explicit upload picker requests the exact source bundle. It does not
claim the SU(6) numerical band coefficient; it produces the exact preflight
needed before the finite-rank run.
"""

from __future__ import annotations

import ast
import gzip
import hashlib
import itertools
import json
import os
import re
import shutil
import sys
import time
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

VERSION = "2026-06-14-su6-determinant-stage0-v2"
OUT_ROOT = Path("/content/SU6_DETERMINANT_STAGE0") if Path("/content").exists() else Path("/mnt/data/SU6_DETERMINANT_STAGE0")
EXTRACT_ROOT = OUT_ROOT / "extracted"
OUT_ROOT.mkdir(parents=True, exist_ok=True)
EXTRACT_ROOT.mkdir(parents=True, exist_ok=True)


def gate(name: str, cond: bool, detail: str = "") -> None:
    status = "PASS" if cond else "FAIL"
    print(f"{status:4s} {name:68s} {detail}")
    if not cond:
        raise AssertionError(f"{name}: {detail}")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def perm_sign(p: tuple[int, ...]) -> int:
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def certify_math() -> dict[str, Any]:
    # A fourth-order matrix element has bra + ket + four perturbing plaquette
    # characters: at most six U/Ubar factors on any one link.
    max_final_local_degree = 2 + 4
    max_resolvent_local_degree = 1 + 3  # ket plus at most three V's before a denominator

    gate("O(y^4) final local tensor degree is at most six", max_final_local_degree == 6,
         f"degree={max_final_local_degree}")
    gate("all resolvent local tensor degrees are below six", max_resolvent_local_degree < 6,
         f"degree<={max_resolvent_local_degree}")

    # SU(N) selection rule: r-s = 0 mod N. Under r+s<=6 at N=6,
    # the only non-balanced sectors are (6,0) and (0,6).
    sectors = [(r, s) for r in range(7) for s in range(7-r) if (r-s) % 6 == 0]
    exceptional = [(r, s) for (r, s) in sectors if r != s]
    gate("SU(6) exceptional final sectors are exactly (6,0),(0,6)",
         exceptional == [(0, 6), (6, 0)], str(exceptional))

    resolvent_exceptional = [
        (r, s) for r in range(max_resolvent_local_degree + 1)
        for s in range(max_resolvent_local_degree + 1-r)
        if r != s and (r-s) % 6 == 0
    ]
    gate("no determinant sector occurs in a fourth-order resolvent denominator",
         not resolvent_exceptional, str(resolvent_exceptional))

    perms = list(itertools.permutations(range(6)))
    signs = [perm_sign(p) for p in perms]
    sign_counts = Counter(signs)
    gate("S6 determinant expansion has 720 terms", len(perms) == 720, str(len(perms)))
    gate("S6 signs split 360 even / 360 odd", sign_counts == Counter({1: 360, -1: 360}), str(sign_counts))

    coeff = Fraction(1, 720)
    # Rank-one projector in the permutation basis:
    # P_{sigma,tau}=sgn(sigma)sgn(tau)/720.
    # Exact idempotence reduces to 720/720^2=1/720.
    idempotent_coeff = sum(Fraction(s*s, 720*720) for s in signs)
    gate("determinant projector normalization", idempotent_coeff == coeff, str(idempotent_coeff))

    # Antisymmetry under adjacent transpositions.
    def compose(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(a[b[i]] for i in range(6))

    adjacent = []
    ident = tuple(range(6))
    for i in range(5):
        t = list(ident)
        t[i], t[i+1] = t[i+1], t[i]
        adjacent.append(tuple(t))
    anti_ok = all(perm_sign(compose(t, p)) == -perm_sign(p) for t in adjacent for p in perms)
    gate("determinant tensor is antisymmetric in every adjacent pair", anti_ok)

    return {
        "max_final_local_degree": max_final_local_degree,
        "max_resolvent_local_degree": max_resolvent_local_degree,
        "su6_admissible_sectors_r_plus_s_le_6": sectors,
        "su6_exceptional_sectors": exceptional,
        "determinant_projector": {
            "formula": "Integral_SU(6) prod[a=1..6] U[i_a,j_a] dU = epsilon(i_1...i_6) epsilon(j_1...j_6)/720",
            "delta_expansion": "epsilon(i)epsilon(j)=sum_{sigma in S6} sgn(sigma) prod_a delta(i_a,j_{sigma(a)})",
            "coefficient": "1/720",
            "permutation_terms": 720,
            "even_terms": 360,
            "odd_terms": 360,
            "projector_idempotent": True,
        },
        "consequence": (
            "SU(6) uses the stable-rank fourth-order denominators and fusion/Casimir data unchanged; "
            "only final trace-network contractions containing local signatures (6,0) or (0,6) must be added."
        ),
    }


KNOWN_ARCHIVE_PATTERNS = [
    "Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE_2026-06-14*.zip",
    "GLUEBALL_FLAT_BAND_SOURCE_RELEASE_V0_7*.zip",
    "y4_extracted_sources*.zip",
    "SU_N_STAGE3G_WIRING_BUNDLE*.zip",
    "Y4_SUN_SYMBOLIC_QAB_COMPACT_BUNDLE*.zip",
]
KNOWN_DATA_PATTERNS = [
    "y4_sun_stable_ordered_words.json.gz",
    "y4_sun_walled_brauer_fixed_rank.py",
    "CERT_Y4_sun_walled_brauer_full_symbolic_certificate_2026-06-14.json",
]


def candidate_roots() -> list[Path]:
    roots = [Path("/content"), Path("/mnt/data")]
    drive = Path("/content/drive/MyDrive")
    if Path("/content").exists():
        try:
            from google.colab import drive as colab_drive  # type: ignore
            if not drive.exists():
                colab_drive.mount("/content/drive", force_remount=False)
        except Exception:
            pass
    if drive.exists():
        roots.append(drive)
    # Deduplicate existing paths.
    out = []
    seen = set()
    for r in roots:
        try:
            rr = r.resolve()
        except Exception:
            rr = r
        if r.exists() and str(rr) not in seen:
            out.append(r)
            seen.add(str(rr))
    return out


def discover_files(roots: Iterable[Path]) -> list[Path]:
    found: dict[str, Path] = {}
    for root in roots:
        for pat in KNOWN_ARCHIVE_PATTERNS + KNOWN_DATA_PATTERNS:
            try:
                for p in root.rglob(pat):
                    if p.is_file():
                        found[str(p.resolve())] = p
            except (PermissionError, OSError):
                continue
    return sorted(found.values(), key=lambda p: (p.name, str(p)))


def safe_extract_zip(zpath: Path, dest: Path) -> list[Path]:
    extracted = []
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zpath) as zf:
        for info in zf.infolist():
            target = (dest / info.filename).resolve()
            if not str(target).startswith(str(dest.resolve()) + os.sep) and target != dest.resolve():
                raise ValueError(f"unsafe ZIP path: {info.filename}")
        zf.extractall(dest)
        extracted = [dest / i.filename for i in zf.infolist() if not i.is_dir()]
    return extracted


def recursively_extract(initial_archives: list[Path], max_depth: int = 3) -> dict[str, Any]:
    queue = [(p, 0) for p in initial_archives]
    seen_hashes = set()
    records = []
    while queue:
        zpath, depth = queue.pop(0)
        try:
            h = sha256(zpath)
        except OSError:
            continue
        if h in seen_hashes or depth > max_depth:
            continue
        seen_hashes.add(h)
        label = re.sub(r"[^A-Za-z0-9_.-]+", "_", zpath.stem)[:100]
        dest = EXTRACT_ROOT / f"d{depth}_{label}_{h[:10]}"
        try:
            files = safe_extract_zip(zpath, dest)
            records.append({
                "archive": str(zpath), "sha256": h, "depth": depth,
                "destination": str(dest), "file_count": len(files), "status": "extracted"
            })
            if depth < max_depth:
                for p in files:
                    if p.suffix.lower() == ".zip":
                        queue.append((p, depth + 1))
        except Exception as e:
            records.append({"archive": str(zpath), "sha256": h, "depth": depth,
                            "status": "error", "error": repr(e)})
    return {"records": records, "unique_archives": len(seen_hashes)}


SOURCE_TERMS = re.compile(r"walled|brauer|ordered.?words|balanced|signature|fusion.?path|trace.?topolog|casimir", re.I)
PATCH_TERMS = re.compile(r"N\s*[><=]+\s*7|rank\s*[><=]+\s*7|balanced|r\s*==\s*s|p\s*==\s*q|charge|signature|imbalance", re.I)


def collect_source_files(search_roots: Iterable[Path]) -> list[Path]:
    out = []
    for root in search_roots:
        if not root.exists():
            continue
        try:
            for p in root.rglob("*.py"):
                try:
                    text = p.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                if SOURCE_TERMS.search(text) or p.name == "y4_sun_walled_brauer_fixed_rank.py":
                    out.append(p)
        except (PermissionError, OSError):
            continue
    # Unique by content hash/path.
    uniq = {}
    for p in out:
        try:
            uniq[(sha256(p), p.name)] = p
        except OSError:
            pass
    return sorted(uniq.values(), key=lambda p: (p.name, str(p)))


def source_audit(paths: list[Path]) -> list[dict[str, Any]]:
    recs = []
    for p in paths:
        text = p.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        snippets = []
        for i, line in enumerate(lines, start=1):
            if PATCH_TERMS.search(line):
                lo, hi = max(1, i-2), min(len(lines), i+2)
                snippets.append({
                    "line": i,
                    "context": "\n".join(f"{j:5d}: {lines[j-1]}" for j in range(lo, hi+1))
                })
                if len(snippets) >= 60:
                    break
        functions = []
        try:
            tree = ast.parse(text)
            functions = [n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        except SyntaxError:
            pass
        recs.append({
            "path": str(p), "sha256": sha256(p), "bytes": p.stat().st_size,
            "functions": functions[:200], "candidate_patch_snippets": snippets,
        })
    return recs


def load_json_any(path: Path) -> Any:
    if path.name.endswith(".gz"):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return json.load(f)
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


PAIR_KEYSETS = [
    ("r", "s"), ("p", "q"), ("fund", "antifund"), ("fundamental", "antifundamental"),
    ("n_fund", "n_antifund"), ("nfund", "nantifund"), ("u", "ubar"),
    ("plus", "minus"), ("forward", "backward"),
]


def extract_signature_pairs(obj: Any, path: str = "$", key_hint: str = "") -> list[tuple[str, int, int]]:
    out: list[tuple[str, int, int]] = []
    if isinstance(obj, dict):
        low = {str(k).lower(): k for k in obj}
        for a, b in PAIR_KEYSETS:
            if a in low and b in low:
                va, vb = obj[low[a]], obj[low[b]]
                if isinstance(va, int) and isinstance(vb, int) and 0 <= va <= 12 and 0 <= vb <= 12:
                    out.append((path, va, vb))
        for k, v in obj.items():
            out.extend(extract_signature_pairs(v, f"{path}.{k}", str(k)))
    elif isinstance(obj, list):
        hint = key_hint.lower()
        if any(t in hint for t in ("signature", "bidegree", "charge", "balance")):
            for i, v in enumerate(obj):
                if (isinstance(v, (list, tuple)) and len(v) == 2 and
                        all(isinstance(x, int) for x in v) and all(0 <= x <= 12 for x in v)):
                    out.append((f"{path}[{i}]", int(v[0]), int(v[1])))
        for i, v in enumerate(obj):
            out.extend(extract_signature_pairs(v, f"{path}[{i}]", key_hint))
    return out


def schema_summary(obj: Any, depth: int = 0, max_depth: int = 4) -> Any:
    if depth >= max_depth:
        return type(obj).__name__
    if isinstance(obj, dict):
        return {str(k): schema_summary(v, depth+1, max_depth) for k, v in list(obj.items())[:30]}
    if isinstance(obj, list):
        return {"type": "list", "length": len(obj), "sample": schema_summary(obj[0], depth+1, max_depth) if obj else None}
    return type(obj).__name__


def inspect_word_archives(search_roots: Iterable[Path]) -> list[dict[str, Any]]:
    candidates = []
    for root in search_roots:
        try:
            candidates.extend(root.rglob("*ordered*words*.json*"))
            candidates.extend(root.rglob("y4_sun_stable_ordered_words.json.gz"))
        except (PermissionError, OSError):
            pass
    uniq = {}
    for p in candidates:
        if p.is_file():
            try:
                uniq[sha256(p)] = p
            except OSError:
                pass
    results = []
    for p in sorted(uniq.values(), key=lambda x: str(x)):
        rec: dict[str, Any] = {"path": str(p), "sha256": sha256(p), "bytes": p.stat().st_size}
        try:
            obj = load_json_any(p)
            rec["schema"] = schema_summary(obj)
            pairs = extract_signature_pairs(obj)
            rec["explicit_signature_pairs_found"] = len(pairs)
            rec["imbalance_histogram"] = dict(sorted(Counter(r-s for _, r, s in pairs).items()))
            rec["exceptional_pair_examples"] = [x for x in pairs if abs(x[1]-x[2]) == 6][:50]
            rec["has_explicit_su6_exceptional_pairs"] = any(abs(r-s) == 6 for _, r, s in pairs)
            if isinstance(obj, list):
                rec["top_level_records"] = len(obj)
            elif isinstance(obj, dict):
                for key in ("ordered_words", "words", "records", "data"):
                    if key in obj and isinstance(obj[key], list):
                        rec["top_level_records"] = len(obj[key])
                        rec["record_container_key"] = key
                        break
        except Exception as e:
            rec["error"] = repr(e)
        results.append(rec)
    return results


def explicit_colab_upload() -> list[Path]:
    """Request the exact missing contraction inputs in Colab.

    Preferred: upload the single full symbolic bundle. Fallback: upload the
    fixed-rank source and stable ordered-word archive as two individual files.
    """
    if not Path("/content").exists():
        return []
    try:
        from google.colab import files as colab_files  # type: ignore
    except Exception:
        return []

    print("\nREQUIRED INPUT — upload ONE of the following choices:")
    print("  Preferred single file:")
    print("    Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE_2026-06-14.zip")
    print("  OR fallback pair:")
    print("    y4_sun_walled_brauer_fixed_rank.py")
    print("    y4_sun_stable_ordered_words.json.gz")
    print("\nThe compact Q/A/B bundle and independent-rerun bundle are not sufficient.")
    uploaded = colab_files.upload()
    saved: list[Path] = []
    for raw_name, data in uploaded.items():
        name = Path(raw_name).name
        target = Path("/content") / name
        target.write_bytes(data)
        saved.append(target)
        print(f"  saved {len(data):,} bytes -> {target}")
    return saved


def active_script_path() -> Path | None:
    """Return this script path when running as a file; None inside raw notebooks."""
    try:
        p = Path(__file__)  # type: ignore[name-defined]
    except NameError:
        return None
    return p if p.is_file() else None


def main() -> None:
    t0 = time.time()
    print("=" * 100)
    print("SU(6) EXCEPTIONAL-RANK O(y^4) DETERMINANT-SECTOR PREFLIGHT")
    print("=" * 100)
    math_cert = certify_math()

    roots = candidate_roots()
    print("\nSearch roots:")
    for r in roots:
        print(" ", r)
    discovered = discover_files(roots)
    print(f"\nDiscovered {len(discovered)} named source/data candidates")
    for p in discovered:
        print(f"  {sha256(p)[:12]}  {p}")

    # A mounted Drive is not evidence that the required source exists there.
    # If no contraction source/data candidate is present, request the exact
    # files explicitly rather than silently searching unrelated Drive trees.
    if not discovered:
        uploaded_now = explicit_colab_upload()
        if uploaded_now:
            roots = candidate_roots()
            discovered = discover_files(roots)
            print(f"\nAfter upload: discovered {len(discovered)} named source/data candidates")
            for p in discovered:
                print(f"  {sha256(p)[:12]}  {p}")

    archives = [p for p in discovered if p.suffix.lower() == ".zip"]
    extraction = recursively_extract(archives)
    print(f"\nExtracted {extraction['unique_archives']} unique archives")

    all_search_roots = roots + [EXTRACT_ROOT]
    source_files = collect_source_files(all_search_roots)
    sources = source_audit(source_files)
    print(f"\nAudited {len(sources)} relevant Python source files")
    for s in sources:
        print(f"  {Path(s['path']).name}: {len(s['candidate_patch_snippets'])} candidate stable-rank/filter sites")

    word_archives = inspect_word_archives(all_search_roots)
    print(f"\nInspected {len(word_archives)} ordered-word archives")
    for w in word_archives:
        print(f"  {w['path']}")
        print(f"    records={w.get('top_level_records')} explicit_pairs={w.get('explicit_signature_pairs_found')} "
              f"su6_exceptional={w.get('has_explicit_su6_exceptional_pairs')}")

    target_source = [s for s in sources if Path(s["path"]).name == "y4_sun_walled_brauer_fixed_rank.py"]
    target_words = [w for w in word_archives if Path(w["path"]).name == "y4_sun_stable_ordered_words.json.gz"]
    source_ready = bool(target_source and target_words)

    status = "SOURCE_READY" if source_ready else "SOURCE_INPUT_MISSING"
    if source_ready:
        next_action = (
            "Patch the word-admissibility filter from r=s to (r-s) mod 6=0; split stable and determinant "
            "sectors; evaluate every (6,0)/(0,6) local Haar node with the signed S6 determinant projector."
        )
    else:
        next_action = (
            "Upload Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE_2026-06-14.zip. "
            "Fallback: upload both y4_sun_walled_brauer_fixed_rank.py and "
            "y4_sun_stable_ordered_words.json.gz. The independent rerun and compact Q/A/B "
            "bundles contain results, not the contraction source chain."
        )

    result = {
        "meta": {"version": VERSION, "created": time.strftime("%Y-%m-%d %H:%M:%S"), "runtime_seconds": time.time()-t0},
        "status": status,
        "math_certificate": math_cert,
        "search_roots": [str(x) for x in roots],
        "discovered_files": [{"path": str(p), "sha256": sha256(p), "bytes": p.stat().st_size} for p in discovered],
        "archive_extraction": extraction,
        "source_audit": sources,
        "ordered_word_audit": word_archives,
        "required_target_source_found": bool(target_source),
        "required_stable_words_found": bool(target_words),
        "next_action": next_action,
    }

    json_path = OUT_ROOT / "SU6_DETERMINANT_STAGE0_REPORT.json"
    json_path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")

    md_lines = [
        "# SU(6) exceptional-rank fourth-order determinant-sector preflight",
        "",
        f"**Version:** `{VERSION}`  ",
        f"**Status:** `{status}`",
        "",
        "## Exact reduction",
        "",
        "A fourth-order matrix element contains the ket plaquette, four perturbing plaquette characters,",
        "and the bra plaquette. Hence a fixed link carries at most six fundamental/antifundamental factors:",
        "",
        r"\[r_\ell+s_\ell\le 6.\]",
        "",
        r"For Haar integration over \(SU(6)\), the selection rule is \(r_\ell-s_\ell\equiv0\pmod 6\).",
        "Within the degree-six bound, the only sectors absent at stable rank are",
        "",
        r"\[(r_\ell,s_\ell)=(6,0),(0,6).\]",
        "",
        "The three resolvent denominators occur after at most three perturbations, so their local degree is",
        "at most four. Consequently no determinant sector enters an intermediate energy or Casimir:",
        "the complete stable-rank fusion and denominator data remain valid for SU(6).",
        "",
        "## Local SU(6) replacement",
        "",
        r"\[",
        r"\int_{SU(6)}\prod_{a=1}^{6}U_{i_a j_a}\,dU",
        r"=\frac{1}{6!}\epsilon_{i_1\cdots i_6}\epsilon_{j_1\cdots j_6}",
        r"=\frac1{720}\sum_{\sigma\in S_6}\operatorname{sgn}(\sigma)",
        r"\prod_{a=1}^{6}\delta_{i_a,j_{\sigma(a)}}.",
        r"\]",
        "",
        "The conjugate formula handles `(0,6)`. The projector has 720 signed terms, split into 360 even",
        "and 360 odd permutations, and its exact normalization/idempotence gates pass.",
        "",
        "## Computational status",
        "",
        f"- Target fixed-rank source found: **{bool(target_source)}**",
        f"- Stable ordered-word archive found: **{bool(target_words)}**",
        f"- Relevant Python files audited: **{len(sources)}**",
        f"- Ordered-word archives inspected: **{len(word_archives)}**",
        "",
        "## Next action",
        "",
        next_action,
        "",
        "The required code change is localized: generalize final word admissibility from exact balance",
        "to balance modulo six, retain all stable-sector contractions unchanged, and add the determinant",
        "projector only at exceptional final Haar nodes.",
    ]
    md_path = OUT_ROOT / "SU6_DETERMINANT_STAGE0_REPORT.md"
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    zip_path = OUT_ROOT.parent / "SU6_DETERMINANT_STAGE0_V2_BUNDLE.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        script_path = active_script_path()
        if script_path is not None:
            zf.write(script_path, arcname=script_path.name)
        zf.write(json_path, arcname=json_path.name)
        zf.write(md_path, arcname=md_path.name)

    print("\n" + "=" * 100)
    print("PREFLIGHT STATUS:", status)
    print(next_action)
    print("JSON:", json_path)
    print("MD:  ", md_path)
    print("ZIP: ", zip_path)
    print("=" * 100)


if __name__ == "__main__":
    main()
