#!/usr/bin/env python3
"""Render figure_radius_two_spectrum.pdf from the sealed radius-two artifact.

Revision 5 of the publication edition includes this figure by name and the
release directory it came from never travelled with the source; the pinned
NPZ does. So the figure is regenerated here from that artifact alone, with
the same standard-library reader ``verify_radius2_report.py`` uses, so the
plot is a view of the pinned bytes and of nothing else.

Left: the retained odd-even Ritz gaps of the three nested operators K_1,
K_{2,*} and K_{2,full} against the coupling. Right: the weak-coupling
Hellmann-Feynman shifts divided by their predicted onset powers, u^4 for
K_{2,*} - K_1 and u^5 for K_{2,full} - K_{2,*}, with the direct products
of the paper's Reported result (radius-two replay) as dashed lines.

Run:  uv run --with matplotlib --with numpy python make_figure_radius2.py
"""

from __future__ import annotations

import ast
import struct
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
NPZ = HERE / "two_cube_cutoff_free_radius2_finite_u_spectrum.npz"


def load(member):
    with zipfile.ZipFile(NPZ) as z:
        raw = z.read(member + ".npy")
    assert raw[:6] == b"\x93NUMPY", "not an npy payload"
    (hlen,) = struct.unpack("<H", raw[8:10])
    header = ast.literal_eval(raw[10 : 10 + hlen].decode("latin1"))
    body = raw[10 + hlen :]
    n = 1
    for s in header["shape"]:
        n *= s
    assert header["descr"] == "<f8", header["descr"]
    return list(struct.unpack(f"<{n}d", body[: 8 * n]))


def main():
    u = load("main_u_grid")
    gaps = {
        r"$K_1$": load("main_matched_gap_k1"),
        r"$K_{2,\star}$": load("main_matched_gap_star"),
        r"$K_{2,full}$": load("main_matched_gap_full"),
    }
    wu = load("weak_u_grid")
    i4 = load("weak_gap_star_minus_k1_over_u4")
    i5 = load("weak_gap_full_minus_star_over_u5")
    d4 = load("direct_c4_ground_odd_even_gap")[0]
    d5 = load("direct_c5_ground_odd_even_gap")[0]

    fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 4.2), constrained_layout=True)
    styles = ["-", "--", ":"]
    for (label, series), style in zip(gaps.items(), styles, strict=True):
        left.plot(u, series, style, color="#2b2b2b", lw=1.8, label=label)
    left.set_xlabel(r"$u=g^{-4}$")
    left.set_ylabel("retained odd--even Ritz gap")
    left.set_title("Nested radius-two operators")
    left.legend(frameon=True, fontsize=9)
    left.spines[["top", "right"]].set_visible(False)
    left.grid(color="#ececec", lw=0.7)

    right.plot(wu, i4, "o-", color="#b33a2e", lw=1.4, ms=4, label=r"$(K_{2,\star}-K_1)/u^4$")
    right.axhline(d4, color="#b33a2e", ls="--", lw=1.0)
    right.set_ylabel(r"$I_4$ shift $/u^4$", color="#b33a2e")
    right.tick_params(axis="y", labelcolor="#b33a2e")
    twin = right.twinx()
    twin.plot(wu, i5, "s-", color="#2569a8", lw=1.4, ms=4, label=r"$(K_{2,full}-K_{2,\star})/u^5$")
    twin.axhline(d5, color="#2569a8", ls="--", lw=1.0)
    twin.set_ylabel(r"$I_5$ shift $/u^5$", color="#2569a8")
    twin.tick_params(axis="y", labelcolor="#2569a8")
    right.set_xlabel(r"$u$ (weak-coupling grid)")
    right.set_title("Onset powers against the direct products")
    lines = right.get_legend_handles_labels()
    lines2 = twin.get_legend_handles_labels()
    right.legend(
        lines[0] + lines2[0], lines[1] + lines2[1], frameon=True, fontsize=8, loc="center right"
    )
    right.spines[["top"]].set_visible(False)
    right.grid(color="#ececec", lw=0.7)

    fig.savefig(
        HERE / "figure_radius_two_spectrum.pdf",
        bbox_inches="tight",
        metadata={"CreationDate": None},
    )
    print("figure_radius_two_spectrum.pdf")


if __name__ == "__main__":
    main()
