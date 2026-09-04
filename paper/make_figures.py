from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon

HERE = Path(__file__).resolve().parent


def momentum_path(points: list[tuple[float, float, float]], per_segment: int = 180):
    pieces = []
    for left, right in zip(points[:-1], points[1:], strict=False):
        t = np.linspace(0.0, 1.0, per_segment, endpoint=False)
        pieces.append(
            np.asarray(left)[None, :] * (1 - t[:, None]) + np.asarray(right)[None, :] * t[:, None]
        )
    pieces.append(np.asarray(points[-1])[None, :])
    return np.concatenate(pieces), np.arange(len(points)) * per_segment


def style_axis(ax, ticks, labels):
    ax.set_xticks(ticks, labels)
    for tick in ticks:
        ax.axvline(tick, color="#d9d9d9", lw=0.8, zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#ececec", lw=0.7)


def second_order_figure():
    points = [(0, 0, 0), (np.pi, 0, 0), (np.pi, np.pi, 0), (np.pi, np.pi, np.pi), (0, 0, 0)]
    k, ticks = momentum_path(points)
    q = 4 * np.sum(np.sin(k / 2) ** 2, axis=1)
    flat = float(Fraction(11, 306))
    t3 = float(Fraction(5, 612))
    odd_partner = flat + t3 * q

    dplus = float(Fraction(223, 1020))
    ell3 = float(Fraction(-11, 306))
    ahat = 2 + 2 * np.cos(k)
    p = np.sum(ahat, axis=1)
    product = np.prod(ahat, axis=1)
    unsigned = np.empty((len(k), 3))
    for i, (pi, prod) in enumerate(zip(p, product, strict=False)):
        roots = np.roots([1.0, -2 * pi, pi * pi, -4 * prod])
        roots = np.sort(np.real_if_close(roots, tol=1000).real)
        unsigned[i] = dplus + ell3 * (roots - 4)

    fig, ax = plt.subplots(figsize=(8.8, 4.8), constrained_layout=True)
    ax.plot(flat + np.zeros_like(q), color="#b33a2e", lw=2.7, label=r"signed carrier $11/306$")
    ax.plot(odd_partner, color="#b33a2e", lw=1.8, ls="--", label="signed dispersive doublet")
    for branch in unsigned.T:
        ax.plot(branch, color="#2569a8", lw=1.7, ls=":")
    ax.plot([], [], color="#2569a8", lw=1.7, ls=":", label="unsigned comparison")
    style_axis(ax, ticks, [r"$\Gamma$", "$X$", "$M$", "$R$", r"$\Gamma$"])
    ax.set_ylabel(r"order-$u^2$ coefficient")
    ax.set_title("Exact signed carrier and unsigned-incidence comparison")
    ax.legend(frameon=True, fontsize=9, loc="best")
    ax.annotate(
        "flat for every momentum",
        xy=(ticks[2], flat),
        xytext=(ticks[2] - 95, flat + 0.085),
        arrowprops={"arrowstyle": "->", "color": "#b33a2e"},
        color="#b33a2e",
        fontsize=9,
    )
    fig.savefig(HERE / "figure_second_order_bands.pdf", bbox_inches="tight")
    fig.savefig(HERE / "figure_second_order_bands.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def historical_fourth_order_figure():
    points = [(0, 0, 0), (np.pi, 0, 0), (np.pi, np.pi, 0), (np.pi, np.pi, np.pi), (0, 0, 0)]
    k, ticks = momentum_path(points)
    x = 1 - np.cos(k)
    s = np.sum(x, axis=1)
    q2 = np.sum(x * x, axis=1)
    r2 = x[:, 0] * x[:, 1] + x[:, 0] * x[:, 2] + x[:, 1] * x[:, 2]
    alpha = float(Fraction(5, 12))
    beta = float(Fraction(17607806155349, 275331901291200))
    qold = float(Fraction(-20721577909065127111, 7250590288602460800))
    lam = np.zeros_like(s)
    nz = s > 1e-14
    lam[nz] = (alpha * q2[nz] + beta * r2[nz]) / (2 * s[nz])
    c4 = qold + lam

    fig, ax = plt.subplots(figsize=(8.8, 4.8), constrained_layout=True)
    ax.plot(c4, color="#147a68", lw=2.6)
    ax.scatter(
        [ticks[0], ticks[3]], [qold, qold + alpha + beta], color=["#147a68", "#a84432"], zorder=4
    )
    style_axis(ax, ticks, [r"$\Gamma$", "$X$", "$M$", "$R$", r"$\Gamma$"])
    ax.set_ylabel(r"saved-kernel fourth-order coefficient")
    ax.set_title("Exact historical saved-kernel dispersion (physical identification disputed)")
    ax.annotate(
        r"$\Gamma$: scalar anchor",
        xy=(ticks[0], qold),
        xytext=(ticks[0] + 45, qold + 0.04),
        fontsize=9,
    )
    ax.annotate(
        r"$R$: $\Delta W_4=\alpha+\beta$",
        xy=(ticks[3], qold + alpha + beta),
        xytext=(ticks[3] - 145, qold + alpha + beta - 0.055),
        arrowprops={"arrowstyle": "->", "color": "#a84432"},
        color="#a84432",
        fontsize=9,
    )
    fig.savefig(HERE / "figure_historical_fourth_order.pdf", bbox_inches="tight")
    fig.savefig(HERE / "figure_historical_fourth_order.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def cellular_carrier_figure():
    fig, (ax_cube, ax_chain) = plt.subplots(
        1,
        2,
        figsize=(9.4, 4.25),
        gridspec_kw={"width_ratios": [0.9, 1.35]},
        constrained_layout=True,
    )

    # Isometric cube: three visible, outward-oriented faces of one 3-cell.
    a = np.array([0.0, 0.0])
    b = np.array([1.55, 0.18])
    c = np.array([1.55, 1.55])
    d = np.array([0.0, 1.37])
    shift = np.array([0.72, 0.55])
    a2, b2, c2, d2 = a + shift, b + shift, c + shift, d + shift
    faces = [
        ([a, b, c, d], "#dcecf7"),
        ([d, c, c2, d2], "#f7e5c8"),
        ([b, b2, c2, c], "#dcefdc"),
    ]
    for vertices, color in faces:
        ax_cube.add_patch(
            Polygon(vertices, closed=True, facecolor=color, edgecolor="#243447", lw=1.5)
        )
    for u, v in [(a, a2), (a2, b2), (a2, d2), (b2, c2), (d2, c2)]:
        ax_cube.plot(
            [u[0], v[0]],
            [u[1], v[1]],
            color="#59636e",
            lw=1.1,
            ls="--" if np.array_equal(u, a) else "-",
        )
    ax_cube.text(0.62, 0.67, r"$-[x;12]$", color="#1f4d70", ha="center", fontsize=11)
    ax_cube.text(1.11, 1.72, r"$+[x+e_3;12]$", color="#80510b", ha="center", fontsize=10)
    ax_cube.text(
        1.82, 0.98, r"$+[x+e_1;23]$", color="#216533", ha="center", rotation=81, fontsize=9.5
    )
    ax_cube.text(
        1.1, -0.28, "one oriented cube boundary", ha="center", fontsize=10.5, fontweight="bold"
    )
    ax_cube.set_xlim(-0.2, 2.55)
    ax_cube.set_ylim(-0.4, 2.35)
    ax_cube.set_aspect("equal")
    ax_cube.axis("off")

    ax_chain.axis("off")
    ax_chain.set_xlim(0, 1)
    ax_chain.set_ylim(0, 1)
    ax_chain.text(0.5, 0.9, r"$C_3$", ha="center", fontsize=14)
    ax_chain.text(0.5, 0.68, r"$C_2$", ha="center", fontsize=14)
    ax_chain.text(0.5, 0.46, r"$C_1$", ha="center", fontsize=14)
    for y0, y1, label in [(0.86, 0.73, r"$\partial_3$"), (0.64, 0.51, r"$\partial_2$")]:
        ax_chain.add_patch(
            FancyArrowPatch(
                (0.5, y0), (0.5, y1), arrowstyle="-|>", mutation_scale=13, lw=1.4, color="#243447"
            )
        )
        ax_chain.text(0.54, (y0 + y1) / 2, label, va="center", fontsize=12)
    ax_chain.text(
        0.68, 0.57, r"$\partial_2\partial_3=0$", fontsize=12, color="#9b2f26", va="center"
    )

    boxes = [
        (
            0.03,
            0.17,
            0.42,
            0.18,
            "cube boundaries",
            r"$\dim\operatorname{im}\partial_3=L^3-1$",
            "#edf4fa",
        ),
        (0.55, 0.17, 0.42, 0.18, "wrapping classes", r"$\dim H_2(T^3)=3$", "#f8f1e7"),
    ]
    for x, y, w, h, title, formula, color in boxes:
        ax_chain.add_patch(
            FancyBboxPatch(
                (x, y),
                w,
                h,
                boxstyle="round,pad=0.018",
                facecolor=color,
                edgecolor="#6a737d",
                lw=1.0,
            )
        )
        ax_chain.text(x + w / 2, y + 0.125, title, ha="center", fontsize=9.5)
        ax_chain.text(x + w / 2, y + 0.055, formula, ha="center", fontsize=10.5)
    ax_chain.text(
        0.5,
        0.055,
        r"$\ker\partial_2=\operatorname{im}\partial_3\oplus H_2,$"
        r"  $\dim\ker\partial_2=L^3+2$",
        ha="center",
        fontsize=11.5,
        fontweight="bold",
    )
    ax_chain.set_title("Cellular origin of the carrier", fontsize=11.5, fontweight="bold", pad=4)

    fig.savefig(HERE / "figure_cellular_carrier.pdf", bbox_inches="tight")
    fig.savefig(HERE / "figure_cellular_carrier.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    cellular_carrier_figure()
    second_order_figure()
    historical_fourth_order_figure()
