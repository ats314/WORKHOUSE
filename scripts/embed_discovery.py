"""Create an optional revision-pinned local model index; never upload corpus text."""

import argparse
import json
from pathlib import Path

from workhouse.discovery import DiscoveryEngine
from workhouse.discovery_semantic import generate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument("--revision", required=True, help="full immutable model commit SHA")
    parser.add_argument(
        "--allow-download", action="store_true", help="explicitly download model weights"
    )
    parser.add_argument("--query-prefix", default="")
    parser.add_argument(
        "--out", type=Path, required=True, help="new output JSON; refuses overwrite"
    )
    args = parser.parse_args()
    if args.out.exists():
        parser.error("output exists; choose a new path")
    with DiscoveryEngine() as engine:
        payload = generate(
            engine.index.records,
            args.model,
            args.revision,
            allow_download=args.allow_download,
            query_prefix=args.query_prefix,
        )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=True, separators=(",", ":"))
    print(f"Wrote {len(payload['vectors'])} record vectors to {args.out}")


if __name__ == "__main__":
    main()
