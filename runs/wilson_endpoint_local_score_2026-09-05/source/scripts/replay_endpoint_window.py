"""Replay a endpoint/local-source certificate without creating or modifying evidence."""

from __future__ import annotations

import argparse
import importlib.abc
import importlib.util
import json
import sys
from pathlib import Path


class NoNumericalDependencies(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in {"numpy", "scipy"}:
            raise ImportError("Forbidden numerical dependency: " + fullname)


def main():
    if sys.flags.optimize:
        raise RuntimeError("Exact replay requires assertions enabled")
    sys.dont_write_bytecode = True
    sys.meta_path.insert(0, NoNumericalDependencies())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    runner = Path(__file__).with_name("verify_endpoint_window.py")
    spec = importlib.util.spec_from_file_location("endpoint_selected_runner", runner)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load the adjacent selected verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.replay_report(json.loads(args.certificate.read_text(encoding="utf-8")))
    print("PASS: all source pins, ten check records and all complete mathematical payloads")


if __name__ == "__main__":
    main()
