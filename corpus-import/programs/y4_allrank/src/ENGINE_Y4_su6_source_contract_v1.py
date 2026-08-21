#!/usr/bin/env python3
"""
SU(6) exceptional-rank O(y^4) source-contract extractor.

One-block Colab/local diagnostic. Upload the full symbolic source bundle when
prompted. The script extracts it, fingerprints the source chain, exposes the
ordered-word schema, finds every reference to the 4,171-word archive, and
prints exact function-level source blocks that implement stable-rank,
balance, signature, trace-topology, and fusion-path logic.

This stage does not alter or execute the verified contraction. Its purpose is
to identify the minimal source hook for adding SU(6) determinant-sector words
without changing the 4,171 stable words or the verified 35,130 stable paths.
"""
from __future__ import annotations

import ast
import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

VERSION = "2026-06-14-su6-source-contract-v1"
BASE = Path("/content") if Path("/content").exists() else Path("/mnt/data")
OUT = BASE / "SU6_SOURCE_CONTRACT_V1"
EXTRACT = OUT / "extracted"
OUT.mkdir(parents=True, exist_ok=True)
EXTRACT.mkdir(parents=True, exist_ok=True)

REQUIRED_SOURCE = "y4_sun_walled_brauer_fixed_rank.py"
REQUIRED_WORDS = "y4_sun_stable_ordered_words.json.gz"
PREFERRED_BUNDLE_GLOB = "Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE*.zip"

TARGET_FILES = {
    "stage0.py", "stage1.py", "stage2.py", "stage3b.py", "stage3c.py",
    "stage3e.py", "stage3g.py", "stage3i.py", "stage3j.py",
    "y4_sun_stable_rank_stage1.py", "y4_sun_walled_brauer_fixed_rank.py",
    "ENGINE_Y4_sun_symbolic_qab_verify.py",
}

KEYWORDS = re.compile(
    r"stable|rank|balanced|balance|signature|charge|imbalance|walled|brauer|"
    r"ordered.?word|trace.?topolog|fusion.?path|admiss|haar|weingarten|"
    r"epsilon|determinant|r\s*==\s*s|p\s*==\s*q|N\s*[><=]|modulo|%\s*N",
    re.I,
)
HIGH_VALUE = re.compile(
    r"balanced|signature|charge|imbalance|admiss|ordered.?word|"
    r"trace.?topolog|fusion.?path|r\s*==\s*s|p\s*==\s*q|%\s*N|N\s*[><=]",
    re.I,
)


def gate(name: str, cond: bool, detail: str = "") -> None:
    status = "PASS" if cond else "FAIL"
    print(f"{status:4s} {name:72s} {detail}")
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
    with zipfile.ZipFile(zpath) as zf:
        root = dest.resolve()
        for info in zf.infolist():
            target = (dest / info.filename).resolve()
            if target != root and not str(target).startswith(str(root) + os.sep):
                raise ValueError(f"unsafe ZIP member: {info.filename}")
        zf.extractall(dest)
        return [dest / i.filename for i in zf.infolist() if not i.is_dir()]


def upload_if_needed() -> list[Path]:
    candidates = list(BASE.rglob(PREFERRED_BUNDLE_GLOB))
    candidates += list(BASE.rglob(REQUIRED_SOURCE))
    candidates += list(BASE.rglob(REQUIRED_WORDS))
    if candidates:
        return candidates
    if not Path("/content").exists():
        return []
    try:
        from google.colab import files as colab_files  # type: ignore
    except Exception:
        return []
    print("\nUPLOAD REQUIRED:")
    print("  Preferred: Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE_2026-06-14_V2.zip")
    print("  Fallback: upload both y4_sun_walled_brauer_fixed_rank.py and")
    print("            y4_sun_stable_ordered_words.json.gz")
    uploaded = colab_files.upload()
    saved = []
    for name, data in uploaded.items():
        target = Path("/content") / Path(name).name
        target.write_bytes(data)
        saved.append(target)
        print(f"saved {len(data):,} bytes -> {target}")
    return saved


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
        dest = EXTRACT / f"d{depth}_{re.sub(r'[^A-Za-z0-9_.-]+','_',zp.stem)[:80]}_{h[:10]}"
        try:
            files = safe_extract(zp, dest)
            records.append({"archive": str(zp), "sha256": h, "depth": depth,
                            "destination": str(dest), "files": len(files), "status": "ok"})
            for p in files:
                if p.suffix.lower() == ".zip":
                    queue.append((p, depth + 1))
        except Exception as e:
            records.append({"archive": str(zp), "sha256": h, "depth": depth,
                            "status": "error", "error": repr(e)})
    return records


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


def load_json(path: Path) -> Any:
    if path.suffix == ".gz":
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return json.load(f)
    return json.loads(path.read_text(encoding="utf-8"))


def container_records(obj: Any) -> tuple[str, list[Any]]:
    if isinstance(obj, list):
        return "<top-level-list>", obj
    if isinstance(obj, dict):
        for key in ("ordered_words", "words", "records", "data", "items"):
            if isinstance(obj.get(key), list):
                return key, obj[key]
    return "<none>", []


def summarize_value(v: Any, depth: int = 0) -> Any:
    if depth >= 3:
        return f"<{type(v).__name__}>"
    if isinstance(v, dict):
        return {str(k): summarize_value(vv, depth + 1) for k, vv in list(v.items())[:20]}
    if isinstance(v, list):
        return [summarize_value(x, depth + 1) for x in v[:5]] + ([f"...({len(v)} total)"] if len(v) > 5 else [])
    if isinstance(v, tuple):
        return tuple(summarize_value(x, depth + 1) for x in v[:5])
    if isinstance(v, str) and len(v) > 300:
        return v[:300] + "..."
    return v


def schema_walk(obj: Any, path: str = "$", depth: int = 0, out: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    if out is None:
        out = []
    if depth > 4 or len(out) >= 300:
        return out
    if isinstance(obj, dict):
        out.append({"path": path, "type": "dict", "keys": [str(k) for k in list(obj.keys())[:80]], "size": len(obj)})
        for k, v in list(obj.items())[:30]:
            schema_walk(v, f"{path}.{k}", depth + 1, out)
    elif isinstance(obj, list):
        out.append({"path": path, "type": "list", "size": len(obj)})
        if obj:
            schema_walk(obj[0], f"{path}[0]", depth + 1, out)
    else:
        out.append({"path": path, "type": type(obj).__name__, "sample": summarize_value(obj)})
    return out


def node_source(lines: list[str], node: ast.AST) -> str:
    start = max(1, getattr(node, "lineno", 1))
    end = min(len(lines), getattr(node, "end_lineno", start))
    return "\n".join(f"{i:5d}: {lines[i-1]}" for i in range(start, end + 1))


def function_inventory(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    try:
        tree = ast.parse(text)
    except SyntaxError as e:
        return {"path": str(path), "sha256": sha256(path), "parse_error": repr(e)}

    parents: dict[ast.AST, ast.AST] = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            parents[child] = parent

    defs = []
    candidates = []
    calls = defaultdict(set)
    current_fn: dict[ast.AST, str] = {}

    def fn_name(n: ast.AST) -> str:
        cur = n
        while cur in parents:
            cur = parents[cur]
            if isinstance(cur, (ast.FunctionDef, ast.AsyncFunctionDef)):
                return cur.name
        return "<module>"

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = []
            for a in list(node.args.posonlyargs) + list(node.args.args):
                args.append(a.arg)
            if node.args.vararg:
                args.append("*" + node.args.vararg.arg)
            for a in node.args.kwonlyargs:
                args.append(a.arg)
            if node.args.kwarg:
                args.append("**" + node.args.kwarg.arg)
            src = node_source(lines, node)
            rec = {"name": node.name, "line_start": node.lineno,
                   "line_end": getattr(node, "end_lineno", node.lineno), "args": args}
            defs.append(rec)
            if KEYWORDS.search(node.name) or HIGH_VALUE.search(src):
                rec2 = dict(rec)
                rec2["source"] = src
                candidates.append(rec2)
        if isinstance(node, ast.Call):
            caller = fn_name(node)
            callee = None
            if isinstance(node.func, ast.Name):
                callee = node.func.id
            elif isinstance(node.func, ast.Attribute):
                callee = node.func.attr
            if callee:
                calls[caller].add(callee)

    line_hits = []
    for i, line in enumerate(lines, 1):
        if KEYWORDS.search(line):
            lo, hi = max(1, i - 3), min(len(lines), i + 3)
            line_hits.append({"line": i, "text": line,
                              "context": "\n".join(f"{j:5d}: {lines[j-1]}" for j in range(lo, hi + 1))})

    archive_refs = []
    for i, line in enumerate(lines, 1):
        if REQUIRED_WORDS in line or "ordered_words" in line or "ordered words" in line.lower():
            lo, hi = max(1, i - 8), min(len(lines), i + 12)
            archive_refs.append({"line": i,
                                 "context": "\n".join(f"{j:5d}: {lines[j-1]}" for j in range(lo, hi + 1))})

    return {
        "path": str(path), "name": path.name, "sha256": sha256(path), "bytes": path.stat().st_size,
        "definitions": defs, "candidate_functions": candidates,
        "keyword_line_hits": line_hits, "archive_references": archive_refs,
        "call_graph": {k: sorted(v) for k, v in sorted(calls.items())},
    }


def print_block(title: str, text: str, max_lines: int = 160) -> None:
    print("\n" + "-" * 100)
    print(title)
    print("-" * 100)
    ls = text.splitlines()
    print("\n".join(ls[:max_lines]))
    if len(ls) > max_lines:
        print(f"... [{len(ls)-max_lines} more lines in JSON/MD report]")


def main() -> None:
    t0 = time.time()
    print("=" * 100)
    print("SU(6) O(y^4) SOURCE-CONTRACT EXTRACTOR")
    print("=" * 100)

    upload_if_needed()
    roots = [BASE, Path("/content/drive/MyDrive"), EXTRACT]
    archives = []
    for root in roots[:2]:
        if root.exists():
            archives.extend(root.rglob(PREFERRED_BUNDLE_GLOB))
    archives = sorted({str(p.resolve()): p for p in archives if p.is_file()}.values(), key=lambda p: str(p))
    extraction = recursive_extract(archives)

    search_roots = [BASE, Path("/content/drive/MyDrive"), EXTRACT]
    sources = find_unique(REQUIRED_SOURCE, search_roots)
    words = find_unique(REQUIRED_WORDS, search_roots)
    gate("fixed-rank contraction source located", bool(sources), str(sources[:2]))
    gate("4,171-word stable archive located", bool(words), str(words[:2]))

    # Select copies nearest to the extracted full bundle, preferring EXTRACT.
    source = sorted(sources, key=lambda p: (0 if str(p).startswith(str(EXTRACT)) else 1, len(str(p))))[0]
    word_path = sorted(words, key=lambda p: (0 if str(p).startswith(str(EXTRACT)) else 1, len(str(p))))[0]

    source_root = source.parent
    py_files = []
    for name in TARGET_FILES:
        matches = list(source_root.rglob(name))
        if matches:
            py_files.append(sorted(matches, key=lambda p: len(str(p)))[0])
    # Include any sibling stage*.py missed through nesting.
    py_files.extend(source_root.glob("stage*.py"))
    unique_py = {sha256(p): p for p in py_files if p.is_file()}
    py_files = sorted(unique_py.values(), key=lambda p: p.name)

    inventories = [function_inventory(p) for p in py_files]
    gate("fixed-rank source included in audited source set",
         any(x.get("name") == REQUIRED_SOURCE for x in inventories),
         f"audited={len(inventories)}")

    obj = load_json(word_path)
    container_key, records = container_records(obj)
    gate("stable archive contains exactly 4,171 records", len(records) == 4171,
         f"container={container_key}, records={len(records)}")

    schema = schema_walk(obj)
    samples = [summarize_value(x) for x in records[:3]]
    record_key_hist = Counter()
    record_type_hist = Counter(type(x).__name__ for x in records)
    for rec in records:
        if isinstance(rec, dict):
            record_key_hist.update(rec.keys())

    archive_ref_count = sum(len(x.get("archive_references", [])) for x in inventories)
    candidate_fn_count = sum(len(x.get("candidate_functions", [])) for x in inventories)
    gate("ordered-word archive has at least one source-code consumer", archive_ref_count > 0,
         f"references={archive_ref_count}")
    gate("candidate generator/contraction functions identified", candidate_fn_count > 0,
         f"functions={candidate_fn_count}")

    # Rank likely hook files by high-value evidence.
    ranked = []
    for inv in inventories:
        score = 10 * len(inv.get("archive_references", [])) + 3 * len(inv.get("candidate_functions", [])) + len(inv.get("keyword_line_hits", []))
        ranked.append({"name": inv.get("name"), "path": inv.get("path"), "score": score,
                       "archive_refs": len(inv.get("archive_references", [])),
                       "candidate_functions": len(inv.get("candidate_functions", [])),
                       "keyword_hits": len(inv.get("keyword_line_hits", []))})
    ranked.sort(key=lambda x: (-x["score"], x["name"] or ""))

    result = {
        "meta": {"version": VERSION, "created": time.strftime("%Y-%m-%d %H:%M:%S"),
                 "runtime_seconds": time.time() - t0},
        "status": "SOURCE_CONTRACT_EXTRACTED",
        "selected_source": {"path": str(source), "sha256": sha256(source)},
        "selected_words": {"path": str(word_path), "sha256": sha256(word_path),
                           "container_key": container_key, "records": len(records)},
        "archive_extraction": extraction,
        "word_archive": {
            "top_level_type": type(obj).__name__, "container_key": container_key,
            "record_count": len(records), "record_type_histogram": dict(record_type_hist),
            "record_key_histogram": dict(record_key_hist), "schema": schema, "sample_records": samples,
        },
        "ranked_hook_files": ranked,
        "source_inventories": inventories,
        "conclusion": (
            "The 4,171-record archive is a stable-sector product, not a raw local-signature list. "
            "SU(6) exceptional words must be generated upstream at the first source function that "
            "computes local charge/signature admissibility, then passed through the existing "
            "trace-topology and global-fusion-path chain with determinant nodes tagged separately."
        ),
    }

    json_path = OUT / "SU6_SOURCE_CONTRACT_V1.json"
    json_path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")

    md = [
        "# SU(6) fourth-order source contract", "",
        f"**Status:** `SOURCE_CONTRACT_EXTRACTED`  ",
        f"**Version:** `{VERSION}`", "",
        "## Stable archive", "",
        f"- Path: `{word_path}`",
        f"- SHA-256: `{sha256(word_path)}`",
        f"- Container: `{container_key}`",
        f"- Records: **{len(records)}**", "",
        "The archive contains already-admitted stable-rank ordered words. It does not expose explicit",
        "local `(r,s)` pairs, so the SU(6) determinant sector must be generated upstream rather than",
        "recovered by filtering the 4,171 records.", "",
        "## Ranked source hooks", "",
        "| file | score | archive refs | candidate functions | keyword hits |",
        "|---|---:|---:|---:|---:|",
    ]
    for r in ranked:
        md.append(f"| `{r['name']}` | {r['score']} | {r['archive_refs']} | {r['candidate_functions']} | {r['keyword_hits']} |")
    md += ["", "## Required implementation invariant", "",
           "The patched generator must reproduce the original 4,171 stable words byte-for-byte,",
           "then append a disjoint determinant-sector collection tagged by every exceptional local",
           "node `(6,0)` or `(0,6)`. No stable trace topology, denominator, or fusion-path weight may change.", "",
           "Full function bodies, archive references, call graphs, schema, and sample records are in the JSON report."]
    md_path = OUT / "SU6_SOURCE_CONTRACT_V1.md"
    md_path.write_text("\n".join(md) + "\n", encoding="utf-8")

    # Human-visible exact excerpts.
    print("\nSelected source:", source)
    print("Selected words: ", word_path)
    print("Stable archive container:", container_key, "records:", len(records))
    print("Record type histogram:", dict(record_type_hist))
    print("Top record keys:", record_key_hist.most_common(30))
    print_block("FIRST STABLE-WORD RECORD", json.dumps(samples[0], indent=2, sort_keys=True))
    print("\nRanked source-hook files:")
    for r in ranked:
        print(f"  score={r['score']:4d} refs={r['archive_refs']:2d} funcs={r['candidate_functions']:3d} hits={r['keyword_hits']:3d}  {r['name']}")

    # Print the most relevant function bodies and archive load/write blocks.
    blocks_printed = 0
    for inv in sorted(inventories, key=lambda x: next((i for i,r in enumerate(ranked) if r['path']==x.get('path')), 999)):
        for ref in inv.get("archive_references", [])[:4]:
            print_block(f"{inv['name']} — ORDERED-WORD ARCHIVE REFERENCE @ line {ref['line']}", ref["context"], 80)
            blocks_printed += 1
        for fn in inv.get("candidate_functions", [])[:8]:
            if HIGH_VALUE.search(fn.get("source", "")):
                print_block(f"{inv['name']} — CANDIDATE FUNCTION {fn['name']} lines {fn['line_start']}-{fn['line_end']}", fn["source"], 180)
                blocks_printed += 1
        if blocks_printed >= 24:
            break

    zip_path = BASE / "SU6_SOURCE_CONTRACT_V1_BUNDLE.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        try:
            script_path = Path(__file__)  # type: ignore[name-defined]
            if script_path.is_file():
                zf.write(script_path, arcname=script_path.name)
        except NameError:
            pass
        zf.write(json_path, arcname=json_path.name)
        zf.write(md_path, arcname=md_path.name)

    print("\n" + "=" * 100)
    print("SOURCE CONTRACT STATUS: SOURCE_CONTRACT_EXTRACTED")
    print("JSON:", json_path)
    print("MD:  ", md_path)
    print("ZIP: ", zip_path)
    print("Return the printed candidate functions or upload the JSON report for the exact SU(6) patch stage.")
    print("=" * 100)


if __name__ == "__main__":
    main()
