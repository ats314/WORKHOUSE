"""Replay the saved SU(2) rotor enclosures using integer signs, with no eigensolver."""

import copy
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True
import check_su2_physical_rotor as rotor


def replay_entry(entry):
    u, cutoff = F(entry["u"]), entry["cutoff"]
    kappa = F(cutoff*(cutoff+2),4)
    barrier = F(entry["barrier"])
    assert 0 < barrier < kappa
    correction = 16*u*u/(kappa-barrier)
    assert F(entry["tail_kinetic_floor"]) == kappa
    assert F(entry["boundary_subtraction"]) == correction
    assert rotor.sturm_count(u,cutoff,barrier) >= 2
    assert rotor.sturm_count(u,cutoff,barrier,correction) >= 2
    for interval in entry["eigenvalues"]:
        index = interval["index"]
        for key, shift in (("ritz_interval",F(0)),("lower_matrix_interval",correction)):
            low, high = map(F,interval[key])
            assert low < high < barrier
            assert rotor.sturm_count(u,cutoff,low,shift) == index
            assert rotor.sturm_count(u,cutoff,high,shift) == index+1
        assert interval["lower"] == interval["lower_matrix_interval"][0]
        assert interval["upper"] == interval["ritz_interval"][1]
    lower = F(entry["eigenvalues"][1]["lower"])-F(entry["eigenvalues"][0]["upper"])
    upper = F(entry["eigenvalues"][1]["upper"])-F(entry["eigenvalues"][0]["lower"])
    assert 0 < lower <= upper
    assert list(map(F,entry["gap_interval"])) == [lower,upper]


def main():
    if not __debug__:
        raise RuntimeError("Assertions must remain enabled")
    root = Path(__file__).resolve().parent
    base = json.loads((root/"su2_physical_rotor_control.json").read_text())
    extra = json.loads((root/"su2_rotor_1000000_certificate.json").read_text())
    assert hashlib.sha256((root/"check_su2_physical_rotor.py").read_bytes()).hexdigest() == base["source_sha256"]
    for name,digest in extra["sources"].items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest() == digest
    # Disable the proposal path: saved certificates are accepted by integer signs.
    def forbidden(*args,**kwargs):
        raise AssertionError("An eigensolver cannot participate in exact certificate replay")
    rotor.jacobi_eigenvalues = forbidden
    entries = [*base["rigorous_fixed_u_enclosures"],extra]
    for entry in entries:
        replay_entry(entry)
    corrupted = copy.deepcopy(entries[1])
    corrupted["eigenvalues"][0]["ritz_interval"][1] = "0"
    try:
        replay_entry(corrupted)
    except AssertionError:
        pass
    else:
        raise AssertionError("A false eigenvalue interval was accepted")
    print("4 untruncated fixed-u enclosures replayed by exact integer signs; corrupted interval rejected")


if __name__ == "__main__":
    main()
