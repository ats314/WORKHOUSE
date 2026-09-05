"""Extend the exact untruncated SU(2) class-rotor certificate to u=10^6."""

import hashlib
import json
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
from check_su2_physical_rotor import rigorous_rotor_enclosure


def main():
    if not __debug__:
        raise RuntimeError("Assertions must remain enabled")
    start = time.monotonic()
    result = rigorous_rotor_enclosure(1000000)
    result["elapsed_seconds"] = time.monotonic()-start
    result["sources"] = {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in (Path(__file__), Path(__file__).with_name("check_su2_physical_rotor.py"))
    }
    destination = Path(__file__).with_name("su2_rotor_1000000_certificate.json")
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
