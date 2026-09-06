"""Preflight every pinned candidate before applying the authorized new docs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    if args.report.exists():
        raise FileExistsError(args.report)
    here = Path(__file__).resolve().parent
    root = next(p for p in here.parents if (p / "pyproject.toml").is_file())
    tree = here / "tree"
    manifest = json.loads((here / "CANDIDATE_COPY_AUDIT.json").read_text(encoding="utf-8"))
    pending, links, staged = [], [], {}
    for rel, record in manifest["targets"].items():
        target = (root / rel).resolve()
        candidate = (tree / rel).resolve()
        if not target.is_relative_to(root) or not candidate.is_relative_to(tree):
            raise ValueError("Candidate target escapes the intended repository")
        data = candidate.read_bytes()
        if sha(data) != record["after_sha256"]:
            raise ValueError(f"Candidate drift: {rel}")
        actual = sha(target.read_bytes()) if target.exists() else None
        if actual != record["before_sha256"]:
            raise ValueError(
                f"Existing target changed; regenerate and review before applying: {rel}"
            )
        staged[rel] = data
        if rel.endswith(".md"):
            for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", data.decode("utf-8")):
                url = match.group(1).strip("<>")
                if "://" in url or url.startswith("#"):
                    continue
                # Mathematical spectral notation such as [0,E](h) is not a link.
                if "/" not in url and "." not in url:
                    continue
                url = unquote(url.split("#", 1)[0])
                resolved = (target.parent / url).resolve()
                if not resolved.is_relative_to(root):
                    raise ValueError(f"Local documentation link escapes repository: {rel}: {url}")
                local = resolved.relative_to(root).as_posix()
                if (tree / local).is_file() or resolved.is_file():
                    links.append([rel, url])
                elif local.startswith(f"runs/{manifest['run']}/"):
                    pending.append([rel, url, local])
                else:
                    raise FileNotFoundError(f"Unresolved local link: {rel}: {url}")
    for copy in manifest["proof_copies"]:
        source = (root / copy["source"]).read_bytes()
        if sha(source) != copy["source_sha256"]:
            raise ValueError("An immutable original proof changed")
        text = source.decode("utf-8").replace("\r\n", "\n")
        for change in copy["replacements"]:
            if text.count(change["old"]) < change["count"]:
                raise ValueError("Copy reconstruction substitution missing")
            text = text.replace(change["old"], change["new"], change["count"])
        reconstructed = (text.rstrip() + copy["appendix"]).encode("utf-8")
        if reconstructed != staged[copy["canonical"]]:
            raise ValueError("Canonical proof is not its exact intended reconstruction")
    # Preflight all paths and bytes above before performing any repository mutation.
    if args.apply:
        for rel, data in staged.items():
            destination = root / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
        for rel, data in staged.items():
            if (root / rel).read_bytes() != data:
                raise ValueError("Written canonical bytes differ")
    report = {
        "passed": True,
        "applied": args.apply,
        "targets": manifest["targets"],
        "proofs_reconstructed": len(manifest["proof_copies"]),
        "existing_local_links": len(links),
        "pending_new_run_links": pending,
        "old_fields_and_route_history_preserved": manifest[
            "old_result_alias_gap_fields_and_route_history_preserved"
        ],
        "scope": (
            "Documentation/copy audit only; root pins, run, supports and "
            "regenerated repository gates remain separate."
        ),
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("x", encoding="utf-8", newline="\n") as output:
        json.dump(report, output, indent=2)
        output.write("\n")
    print(
        json.dumps(
            {
                "passed": True,
                "applied": args.apply,
                "proofs": len(manifest["proof_copies"]),
                "local_links": len(links),
                "pending_run_links": len(pending),
            }
        )
    )


if __name__ == "__main__":
    main()
