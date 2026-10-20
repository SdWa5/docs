"""Matplotlib graphs for acoustics.md; called by split.py.

Requires matplotlib and scipy. All four graphs use logarithmic frequency axes.
Reflection/absorption use linear percentages. Transmission comes twice, with the same
curves on a linear and on a logarithmic percentage axis.
Each figure contains one plot. Curves use unrounded, uncapped energy inputs; rounding is confined to tables.
All curves are solid and have no point markers. Reflection/absorption use PCHIP in log-frequency;
transmission uses modified Akima interpolation in log-frequency and log-energy to avoid flat runs.
Additional source transmission frequencies feed the curves independently of the ten table bands and axis labels.
Names sit beside the curve endpoints; ties use the pink noise average, largest first from the top.
"""
from pathlib import Path
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FixedLocator, FixedFormatter, MaxNLocator, NullFormatter
import numpy as np
from scipy.interpolate import Akima1DInterpolator, PchipInterpolator

from data import EXTRA_R
from split import FREQS, LABELS


COLORS = (
    "#1f77b4", "#e67300", "#238b45", "#d62728", "#8060ac",
    "#8c564b", "#c63d98", "#687680", "#827b0c", "#129bb2",
    "#003f5c", "#7a5195", "#ef5675", "#b67b00", "#006d2c",
    "#8c510a", "#636363", "#007f87", "#111827", "#be123c",
)
PLOT_SPECS = (
    ("reflected", "reflected", "Reflected sound", "Reflected energy (%)", "linear"),
    ("absorbed", "absorbed", "Absorbed sound", "Absorbed energy (%)", "linear"),
    ("transmitted-linear", "transmitted", "Transmitted sound", "Transmitted energy (%)", "linear"),
    ("transmitted-log", "transmitted", "Transmitted sound — logarithmic energy scale", "Transmitted energy (%)", "log"),
)
OUTPUT_DPI = 160


def series(row, kind):
    """Return unrounded energy percentages, independently of table display conventions."""
    alpha = np.asarray(row["alpha"], dtype=float)
    tau = 10.0 ** (-np.asarray(row["R"], dtype=float) / 10)
    if kind == "reflected":
        y = 100 * (1 - alpha)
    elif kind == "absorbed":
        y = 100 * (alpha - tau)
    else:
        y = 100 * tau
    assert len(y) == len(FREQS) and np.all(np.isfinite(y)) and np.all((y >= 0) & (y <= 100))
    return y


def curve_samples(row, kind):
    """Return the table anchors plus any additional source frequencies relevant to this energy share.

    Extra R measurements change transmission and true absorption, but supply no new reflection evidence.
    At those frequencies alpha still follows the existing ten-band interpolation. All inputs remain
    unrounded and uncapped so table formatting cannot introduce artificial plateaus in the curves.
    """
    values = series(row, kind)
    samples = dict(zip(FREQS, values))
    if kind != "reflected" and row["construction"] in EXTRA_R:
        extra, _estimated = EXTRA_R[row["construction"]]
        alpha = PchipInterpolator(np.log10(FREQS), row["alpha"], extrapolate=False)
        for f, r_db in extra.items():
            assert f not in samples and FREQS[0] < f < FREQS[-1]
            if kind == "transmitted":
                samples[f] = 100 * 10.0 ** (-r_db / 10)
            else:
                samples[f] = 100 * (float(alpha(np.log10(f))) - 10.0 ** (-r_db / 10))
    frequencies = np.array(sorted(samples), dtype=float)
    percentages = np.array([samples[f] for f in frequencies])
    assert np.all(np.isfinite(percentages)) and np.all((percentages >= 0) & (percentages <= 100))
    return frequencies, percentages


def style_axes(ax, ylabel):
    ax.set_xscale("log")
    ax.set_xlim(27, 19000)
    ax.xaxis.set_major_locator(FixedLocator(FREQS))
    ax.xaxis.set_major_formatter(FixedFormatter(LABELS))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.tick_params(axis="both", labelsize=10, length=3, colors="#475569")
    ax.set_xlabel("Frequency (logarithmic scale)", fontsize=11, labelpad=8)
    ax.set_ylabel(ylabel, fontsize=11, labelpad=8)
    ax.grid(which="major", color="#d7dee7", linewidth=.7)
    ax.grid(which="minor", axis="x", color="#edf1f5", linewidth=.4)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_color("#b6c0cd")
    ax.set_ylim(-2, 102)
    ax.set_yticks(np.arange(0, 101, 20))


def draw_curve(ax, row, kind, index):
    frequencies, y = curve_samples(row, kind)
    color = COLORS[index]
    x_smooth = np.unique(np.concatenate((np.geomspace(FREQS[0], FREQS[-1], 1001), frequencies)))
    if kind == "transmitted":
        # Interpolate orders of magnitude in log-percent as well as log-frequency.
        # Equal readings constrain the endpoints, not the entire interval between them. PCHIP would
        # flatten each such interval; modified Akima retains every input without those stair steps.
        interpolator = Akima1DInterpolator(np.log10(frequencies), np.log10(y), method="makima", extrapolate=False)
        y_smooth = 10.0 ** interpolator(np.log10(x_smooth))
    else:
        interpolator = PchipInterpolator(np.log10(frequencies), y, extrapolate=False)
        y_smooth = interpolator(np.log10(x_smooth))
    assert np.all(np.isfinite(y_smooth)) and np.all(y_smooth >= -1e-10) and np.all(y_smooth <= 100 + 1e-10)
    # Both interpolators must pass through the unrounded source and model samples.
    np.testing.assert_allclose(y_smooth[np.searchsorted(x_smooth, frequencies)], y, rtol=1e-12, atol=1e-12)
    line, = ax.plot(x_smooth, y_smooth, color=color, linestyle="-",
                    linewidth=2.2 if index == 19 else 1.5, alpha=.94,
                    zorder=4 if index == 19 else 3)
    line.set_gid(f"material-{index + 1:02d}")
    return frequencies, y


def energy_average(frequencies, percentages):
    """Mean plotted energy percentage for equal incident energy per octave (a pink-noise reference).

    Integrate energy, including on the logarithmic-energy plot; averaging log percentages would instead
    produce a geometric mean. The result summarizes the displayed curve over its sampled frequency range.
    """
    log_frequency = np.log(frequencies)
    return float(np.trapezoid(percentages, log_frequency) / (log_frequency[-1] - log_frequency[0]))


def label_order(endpoints, averages, tolerance):
    """Return indices from top to bottom, sorting visually equal endpoints by descending energy average.

    A group spans at most tolerance in axes height, so roundoff at a shared endpoint cannot decide its order.
    Original material order breaks ties between identical averages.
    """
    remaining = sorted(range(len(endpoints)), key=lambda i: (-endpoints[i], i))
    ordered = []
    while remaining:
        top = endpoints[remaining[0]]
        group = []
        while remaining and top - endpoints[remaining[0]] <= tolerance:
            group.append(remaining.pop(0))
        ordered.extend(sorted(group, key=lambda i: (-averages[i], i)))
    return ordered


def curve_groups(displayed, kind):
    """Merge only identical full input curves, never merely equal endpoints or averages."""
    groups, samples = [], []
    for index, row in displayed:
        x, y = curve_samples(row, kind)
        for group, (previous_x, previous_y) in zip(groups, samples):
            if np.array_equal(x, previous_x) and np.array_equal(y, previous_y):
                group.append((index, row))
                break
        else:
            groups.append([(index, row)])
            samples.append((x, y))
    return groups


def group_label(members, average):
    """Name every represented material, condensing the shared concrete backing into one labelled block."""
    numbers = [index + 1 for index, _row in members]
    ranges = []
    first = last = numbers[0]
    for number in numbers[1:]:
        if number == last + 1:
            last = number
            continue
        ranges.append((first, last))
        first = last = number
    ranges.append((first, last))
    prefix = "/".join(f"{first:02d}–{last:02d}" if last - first >= 2 else
                      "/".join(f"{number:02d}" for number in range(first, last + 1))
                      for first, last in ranges)
    average_text = f"pink noise average ≈{average:.2g}%"
    if len(members) == 1:
        name = members[0][1]["name"].replace("\\*", "").replace("*", "")
        return f"{prefix}  {name} · {average_text}"
    if all(row["construction"] in ("concrete150", "on_concrete150") for _index, row in members):
        families = list(dict.fromkeys(row["material"].split(" (")[0] for _index, row in members))
        family_text = textwrap.fill("; ".join(families), width=64, initial_indent="    ", subsequent_indent="    ")
        return f"{prefix}  Concrete + finishes ({len(members)} materials) · {average_text}\n{family_text}"
    if all(row["construction"] == "brick18" for _index, row in members):
        finishes = "/".join(row["material"].removeprefix("Brick wall (").removesuffix(")") for _index, row in members)
        return f"{prefix}  Brick wall ({members[0][1]['thickness']}, {finishes}) · {average_text}"
    names = [row["name"].replace("\\*", "").replace("*", "") for _index, row in members]
    return f"{prefix}  {average_text}\n" + "\n".join(names)


def label_curves(ax, groups):
    """Place names outside the plot with coloured leaders, keeping the data curves untouched."""
    endpoints, averages = [], []
    for line in ax.lines:
        points = ax.transAxes.inverted().transform(ax.transData.transform(line.get_xydata()))
        endpoints.append(points[-1])
        averages.append(energy_average(line.get_xdata(), line.get_ydata()))
    assert len(endpoints) == len(groups)
    labels = []
    for members, average in zip(groups, averages):
        label = ax.text(1.105, .5, group_label(members, average), transform=ax.transAxes,
                        va="center", ha="left", fontsize=9.2, color="#172033")
        suffix = "-".join(f"{index + 1:02d}" for index, _row in members)
        label.set_gid(f"material-label-{suffix}")
        labels.append(label)
    ax.figure.canvas.draw()
    renderer = ax.figure.canvas.get_renderer()
    heights = [label.get_window_extent(renderer).height / ax.bbox.height for label in labels]
    # Treat endpoints within one pixel of the exported PNG as the same visible height.
    tolerance = ax.figure.dpi / (OUTPUT_DPI * ax.bbox.height)
    ordered = label_order([point[1] for point in endpoints], averages, tolerance)
    bottom_up = list(reversed(ordered))
    gap, margin = .0465, .015
    positions = []
    separations = [max(gap, (heights[a] + heights[b]) / 2 + .015)
                   for a, b in zip(bottom_up, bottom_up[1:])]
    for position, i in enumerate(bottom_up):
        lower = margin + heights[i] / 2 if not positions else positions[-1] + separations[position - 1]
        positions.append(max(endpoints[i][1], lower))
    positions[-1] = min(positions[-1], 1 - margin - heights[bottom_up[-1]] / 2)
    for position in range(len(positions) - 2, -1, -1):
        positions[position] = min(positions[position], positions[position + 1] - separations[position])
    assert positions[0] >= margin + heights[bottom_up[0]] / 2 - 1e-12
    for i, position in zip(bottom_up, positions):
        index = groups[i][0][0]
        start_x, start_y = endpoints[i]
        leader = Line2D([start_x, 1.012, 1.09], [start_y, start_y, position],
                        transform=ax.transAxes, clip_on=False, color=COLORS[index], alpha=.7, linewidth=.9)
        leader.set_gid(labels[i].get_gid().replace("material-label-", "material-leader-"))
        ax.figure.add_artist(leader)
        labels[i].set_position((1.105, position))


def write_plots(rows, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    assert len(rows) == len(COLORS) == 20
    plt.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none"})
    outputs = []
    for name, kind, title, ylabel, yscale in PLOT_SPECS:
        displayed = [(i, row) for i, row in enumerate(rows)
                     if kind != "transmitted" or row["construction"] != "open"]
        groups = curve_groups(displayed, kind)
        minimum, maximum = None, None
        if kind == "transmitted":
            peak = max(float(np.max(curve_samples(row, kind)[1])) for _, row in displayed)
            smallest = min(float(np.min(curve_samples(row, kind)[1])) for _, row in displayed)
            minimum = float(10 ** np.floor(np.log10(smallest)))
            # Leave a small margin and use readable tick spacing; graph tests check the full curves fit.
            transmission_ticks = MaxNLocator(nbins=6, steps=[1, 2, 2.5, 5, 10]).tick_values(0, peak * 1.05)
            maximum = float(transmission_ticks[-1])
        fig = plt.figure(figsize=(17.4, 10.2), facecolor="white")
        fig.text(.08, .94, title, fontsize=22, fontweight="bold", color="#172033")
        axis = "Logarithmic" if yscale == "log" else "Linear"
        subtitle = f"{len(displayed)} materials  |  Ten labelled frequency bands  |  {axis} percentage axis"
        if len(groups) < len(displayed):
            subtitle = subtitle.replace(f"{len(displayed)} materials", f"{len(displayed)} materials in {len(groups)} shared curves")
        if maximum is not None:
            subtitle += f"; maximum {maximum:g}%"
        fig.text(.08, .902, subtitle, fontsize=10.5, color="#596579")
        ax = fig.add_axes((.08, .16, .50, .67))
        style_axes(ax, ylabel)
        ax.tick_params(axis="both", labelsize=9)
        if maximum is not None:
            ax.set_ylabel(f"{ylabel}\n{axis} scale; maximum {maximum:g}%", fontsize=11, labelpad=8)
            if yscale == "linear":
                ax.set_ylim(0, maximum)
                ax.set_yticks(transmission_ticks)
        if yscale == "log":
            ax.set_yscale("log")
            ax.set_ylim(minimum, maximum)
            ticks = [float(tick) for tick in 10.0 ** np.arange(np.log10(minimum), 3) if tick < maximum]
            ax.set_yticks([*ticks, maximum])
            ax.set_yticklabels([*(f"{tick:.10f}".rstrip("0").rstrip(".") for tick in ticks), f"{maximum:g}"])
            ax.yaxis.set_minor_formatter(NullFormatter())
        if kind == "transmitted":
            highlight = "#9a3412"
            ax.yaxis.label.set_color(highlight)
            ax.tick_params(axis="y", colors=highlight)
            ax.spines["left"].set_color(highlight)
            ax.spines["left"].set_linewidth(1.4)
            energy_range = f"{minimum:.10f}".rstrip("0").rstrip(".") + f"–{maximum:g}%" if yscale == "log" else f"0–{maximum:g}%"
            fig.text(.08, .86, f"ENERGY AXIS: {axis.upper()}, {energy_range} · OPEN WINDOW (100%) OMITTED",
                     fontsize=9, fontweight="bold", color=highlight,
                     bbox={"facecolor": "#fff7ed", "edgecolor": "#fed7aa", "boxstyle": "round,pad=.35"})
        for members in groups:
            i, row = members[0]
            frequencies, y = draw_curve(ax, row, kind, i)
            plotted_x = ax.lines[-1].get_xdata()
            np.testing.assert_allclose(ax.lines[-1].get_ydata()[np.searchsorted(plotted_x, frequencies)], y,
                                       rtol=1e-12, atol=1e-12)
            assert ax.lines[-1].get_linestyle() == "-"
        assert len(fig.axes) == 1 and len(ax.lines) == len(groups) and ax.get_xscale() == "log"
        assert ax.get_yscale() == yscale

        label_curves(ax, groups)
        provenance = "Curves combine sourced values and estimates; see the tables for provenance. Some curves overlap."
        if kind == "transmitted":
            provenance = "Open window omitted (100%). See the tables for measurements and estimates; some curves overlap."
        fig.text(.08, .085, provenance, fontsize=9, color="#475569")
        fig.text(.08, .055, "Pink noise average: equal incident energy per octave, 31.5 Hz–16 kHz. Endpoint ties put the largest average first from the top.",
                 fontsize=9, color="#475569")
        if kind == "transmitted":
            footer = "Unrounded, uncapped inputs; modified Akima in log-frequency and log-energy. Intermediate curves and outer bands are estimates."
        elif kind == "absorbed":
            footer = "Additional transmission measurements included; alpha between table bands is interpolated in log-frequency."
        else:
            footer = "Log-frequency interpolation between available absorption inputs; intermediate values are estimates."
        fig.text(.08, .025, footer, fontsize=9, color="#475569")
        fig.canvas.draw()
        # Validate that every material name fits, with no overlapping labels or clipped axis text.
        renderer = fig.canvas.get_renderer()
        for text in [*ax.texts, *ax.get_xticklabels(), *ax.get_yticklabels(),
                     ax.xaxis.label, ax.yaxis.label, *fig.texts]:
            box = text.get_window_extent(renderer)
            assert box.x0 >= 0 and box.y0 >= 0 and box.x1 <= fig.bbox.width and box.y1 <= fig.bbox.height, text.get_text()
        boxes = sorted((text.get_window_extent(renderer) for text in ax.texts), key=lambda box: box.y0)
        assert all(a.y1 + 2 <= b.y0 for a, b in zip(boxes, boxes[1:]))
        path = output_dir / f"{name}.png"
        fig.savefig(path, dpi=OUTPUT_DPI, metadata={
            "Title": title,
            "Description": f"{len(displayed)} materials in {len(groups)} distinct curves; labelled frequencies: " + ", ".join(LABELS)
                           + "; direct labels with pink noise averages; endpoint ties ordered by energy average; no point markers; source: acoustics.md.",
        })
        outputs.append(path)
        plt.close(fig)
    return outputs
