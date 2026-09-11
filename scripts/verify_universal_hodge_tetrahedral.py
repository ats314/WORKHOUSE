#!/usr/bin/env python3
"""Run exact cellular algebra controls and the tetrahedral projection-boundary finding."""

from workhouse.invariants.universal_cellular_hodge import cellular_hodge


def main():
    results = cellular_hodge.run()
    for result in results:
        print(f"{'PASS' if result.passed else 'FAIL'} T{result.tier} {result.name}")
        print(f"  {result.detail}")
    return 0 if all(result.passed for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
