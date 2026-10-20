"""Tests for the acoustics generator and the committed docs/acoustics.md it produced.

The table tests need only the standard library. The graph tests need the packages in requirements.txt and
are skipped without them, unless ACOUSTICS_REQUIRE_GRAPHS=1 turns the skip into a failure, as CI does.
"""
import importlib.util
import math
import os
import random
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import split  # noqa: E402
from data import (  # noqa: E402
    ALPHA_ANCHORED, ALPHA_SOURCES, ASSUMPTIONS, BASE_FREQUENCIES, CONSTRUCTIONS, EXTRA_R, MEASURED_R,
    MID_FREQUENCIES, ROWS,
)

ASSETS = split.TARGET.parent / "assets" / "acoustics"
GRAPHS = ("reflected.png", "absorbed.png", "transmitted-linear.png", "transmitted-log.png")
HAVE_GRAPH_DEPS = all(importlib.util.find_spec(m) for m in ("matplotlib", "numpy", "scipy"))
REQUIRE_GRAPHS = os.environ.get("ACOUSTICS_REQUIRE_GRAPHS") == "1"
ROWS_BUILT = split.build(ROWS, CONSTRUCTIONS)
TEXT = split.TARGET.read_text()

# Independent fixtures for the unchanged 125 Hz / 1 kHz / 4 kHz seed. These protect the source values and
# their provenance while data.py expands its input dictionaries in place to the ten-band representation.
SEED_ALPHA = {
    "Brick wall (46 cm thick, unpainted)": (.02, .04, .07),
    "Brick wall (46 cm thick, painted)": (.01, .02, .02),
    "Interior plaster (on metal lath)": (.02, .06, .03),
    "Poured concrete": (.01, .02, .03),
    "Pine flooring": (.09, .08, .10),
    "Carpeting (with pad)": (.10, .30, .70),
    "Drapes (cotton, 2× fullness)": (.07, .80, .50),
    "Drapes (velour, 2× fullness)": (.15, .75, .65),
    "Acoustic tile (16 mm, #1 mount\\*)": (.15, .70, .65),
    "Acoustic tile (16 mm, #2 mount\\*)": (.25, .70, .65),
    "Acoustic tile (16 mm, #7 mount\\*)": (.50, .75, .65),
    "Tectum panels (25 mm, #2 mount\\*)": (.08, .55, .65),
    "Tectum panels (25 mm, #7 mount\\*)": (.35, .35, .65),
    "Plywood panel (3 mm, 5 cm air space)": (.30, .10, .07),
    "Plywood cylinders (2 layers, 3 mm)": (.35, .20, .18),
    "Perforated transite (with pad, #7 mount\\*)": (.90, .95, .45),
    "Occupied audience seating area": (.50, .95, .85),
    "Upholstered theatre seats (hard floor)": (.45, .90, .70),
    "Open window": (1.0, 1.0, 1.0),
    "Sand-filled timber wall (30 cm total)": (.05, .06, .07),
}
SEED_R = {
    "brick18": ((49.5, 65, 70), (True, True, True)),
    "lath_plaster": ((29, 45, 54), (False, False, False)),
    "concrete150": ((38, 59, 72), (False, False, False)),
    "pine_floor": ((31, 47, 68), (False, False, False)),
    "on_concrete150": ((38, 59, 72), (True, True, True)),
    "open": ((0, 0, 0), (False, False, False)),
    "sand_wall": ((40, 55, 65), (True, True, True)),
}
# Further source frequencies used in the curves, while the ten table bands remain unchanged.
SOURCE_EXTRA_R = {
    "lath_plaster": ({192: 28, 384: 38, 768: 43}, False),
    "pine_floor": ({192: 23, 384: 40, 768: 44}, False),
    "concrete150": ({160: 41, 200: 41, 315: 45, 400: 48, 630: 54, 800: 57,
                     1250: 62, 1600: 65, 2500: 69, 3150: 71}, False),
    "on_concrete150": ({160: 41, 200: 41, 315: 45, 400: 48, 630: 54, 800: 57,
                        1250: 62, 1600: 65, 2500: 69, 3150: 71}, True),
}


def read_table(title):
    """Return stripped cells of a generated table, material and thickness first."""
    block = TEXT.split(f"### {title}\n", 1)[1]
    lines = [line for line in block.split("\n\n", 1)[0].splitlines() if line.startswith("|")]
    return [[cell.strip() for cell in line.strip("|").split("|")] for line in lines[2:]]


def one_digit(share):
    """Round a percentage to one significant digit, as the Through, in % table does."""
    exp = math.floor(math.log10(share))
    digit = round(share / 10 ** exp)
    return digit * 10 ** exp if digit < 10 else 10 ** (exp + 1)


class TableTest(unittest.TestCase):
    def test_ten_octave_bands(self):
        self.assertEqual(split.FREQS, (31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000))
        self.assertEqual(len(split.LABELS), len(split.FREQS))

    def test_document_is_current(self):
        text = split.document(split.TEMPLATE.read_text(), ROWS_BUILT, ASSUMPTIONS, CONSTRUCTIONS,
                              ALPHA_SOURCES, ALPHA_ANCHORED)
        self.assertEqual(text, TEXT, "docs/acoustics.md is stale, run split.py")

    def test_energy_balance(self):
        for row in ROWS_BUILT:
            for i, f in enumerate(split.FREQS):
                tau = 10 ** (-row["R"][i] / 10)
                shares = (1 - row["alpha"][i], row["alpha"][i] - tau, tau)
                self.assertTrue(all(-1e-12 <= s <= 1 for s in shares), (row["name"], f, shares))
                self.assertAlmostEqual(sum(shares), 1, delta=1e-12)

    def test_open_window_is_the_ideal_reference(self):
        window = [row for row in ROWS_BUILT if row["construction"] == "open"]
        self.assertEqual(len(window), 1)
        self.assertEqual(list(window[0]["alpha"]), [1] * len(split.FREQS))
        self.assertEqual(list(window[0]["R"]), [0] * len(split.FREQS))
        self.assertFalse(any(window[0]["alpha_est"]) or any(window[0]["R_est"]))
        through = [cells for cells in read_table("Through, in %") if cells[0] == window[0]["name"]]
        self.assertEqual(len(through), 1)
        self.assertEqual(through[0][2:], ["100 %"] * len(split.FREQS))

    def test_band_provenance(self):
        self.assertEqual({row["name"] for row in ROWS_BUILT}, set(SEED_ALPHA))
        self.assertEqual(set(CONSTRUCTIONS), set(SEED_R))
        for row in ROWS_BUILT:
            key = row["construction"]
            for i, f in enumerate(split.FREQS):
                with self.subTest(row=row["name"], frequency=f):
                    if f in BASE_FREQUENCIES:
                        seed_i = BASE_FREQUENCIES.index(f)
                        self.assertEqual(row["alpha"][i], SEED_ALPHA[row["name"]][seed_i])
                        self.assertEqual(row["alpha_est"][i], key == "sand_wall")
                        self.assertEqual(row["R"][i], SEED_R[key][0][seed_i])
                        self.assertEqual(row["R_est"][i], SEED_R[key][1][seed_i])
                    elif key != "open":
                        self.assertTrue(row["alpha_est"][i])
                        if f in MID_FREQUENCIES and key in MEASURED_R:
                            values, estimated = MEASURED_R[key]
                            self.assertEqual(row["R"][i], values[MID_FREQUENCIES.index(f)])
                            self.assertEqual(row["R_est"][i], estimated)
                        else:
                            self.assertTrue(row["R_est"][i])

    def test_anchored_alpha_weights_and_energy_bounds(self):
        self.assertEqual(set(ALPHA_ANCHORED), set(ALPHA_SOURCES))
        rows = {row["name"]: row for row in ROWS_BUILT}
        for name, (mismatch, weights) in ALPHA_ANCHORED.items():
            self.assertTrue(0 <= mismatch <= 1, name)
            self.assertEqual(set(weights), set(MID_FREQUENCIES), name)
            for f, weight in weights.items():
                with self.subTest(row=name, frequency=f):
                    self.assertTrue(0 < weight < 1, weight)
                    i = split.FREQS.index(f)
                    tau = 10 ** (-rows[name]["R"][i] / 10)
                    self.assertTrue(tau <= rows[name]["alpha"][i] <= 1)

    def test_extra_source_frequencies_and_provenance(self):
        self.assertEqual(set(EXTRA_R), set(SOURCE_EXTRA_R) | {"brick18"})
        for key, expected in SOURCE_EXTRA_R.items():
            self.assertEqual(EXTRA_R[key], expected, key)
        brick_values, brick_estimated = EXTRA_R["brick18"]
        self.assertTrue(brick_estimated)
        self.assertEqual(set(brick_values), set(SOURCE_EXTRA_R["concrete150"][0]) | {192, 384, 768})
        for key, (values, _estimated) in EXTRA_R.items():
            self.assertTrue(set(values).isdisjoint(split.FREQS), key)
            self.assertTrue(all(125 < f < 4000 and math.isfinite(r) and r >= 0
                                for f, r in values.items()), key)

    def test_alpha_sources_are_rendered(self):
        text = split.render_alpha_sources(ALPHA_SOURCES, ALPHA_ANCHORED)
        for name, (source, specimen, values) in ALPHA_SOURCES.items():
            self.assertIn(name, text)
            self.assertIn(source, text)
            self.assertIn(specimen, text)
            self.assertEqual(set(values), set(BASE_FREQUENCIES + MID_FREQUENCIES))
        self.assertIn(text, TEXT)
        self.assertNotIn("{{ALPHA_SOURCES}}", TEXT)

    def test_material_and_specimen_measurements_are_metric(self):
        descriptions = [row["name"] for row in ROWS_BUILT]
        descriptions += [specimen for _source, specimen, _values in ALPHA_SOURCES.values()]
        for description in descriptions:
            self.assertNotIn("″", description)
            self.assertNotIn("oz/yd", description)

    def test_table_shape_and_estimate_marks(self):
        for title in ("Reflected", "Absorbed", "Through, in dB", "Through, in %"):
            rows = read_table(title)
            self.assertEqual([len(r) for r in rows], [len(split.FREQS) + 2] * len(ROWS_BUILT), title)
            for cells, row in zip(rows, ROWS_BUILT):
                self.assertEqual(cells[:2], [row["material"], row["thickness"]])
                for i, cell in enumerate(cells[2:]):
                    if title == "Reflected":
                        estimated = row["alpha_est"][i]
                    elif title == "Absorbed":
                        tau = 10 ** (-row["R"][i] / 10)
                        estimated = row["alpha_est"][i] or (row["R_est"][i] and tau >= .005)
                    else:
                        estimated = row["R_est"][i]
                    self.assertEqual(cell.endswith("†"), estimated, (title, row["name"], split.FREQS[i], cell))

    def test_material_and_thickness_are_separate(self):
        rows = read_table("Reflected")
        self.assertEqual(rows[0][:2], ["Brick wall (unpainted)", "46 cm"])
        self.assertEqual(rows[3][:2], ["Poured concrete", "—"])
        self.assertEqual(rows[8][:2], ["Acoustic tile (#1 mount\\*)", "16 mm"])
        self.assertEqual(rows[13][:2], ["Plywood panel (5 cm air space)", "3 mm"])
        self.assertEqual(rows[-1][:2], ["Sand-filled timber wall", "30 cm total"])

    def test_db_and_percent_tables_agree(self):
        for db_row, pct_row in zip(read_table("Through, in dB"), read_table("Through, in %")):
            for db_cell, pct_cell in zip(db_row[2:], pct_row[2:]):
                db = int(db_cell.removeprefix("≤ ").removesuffix("†").removesuffix(" dB").lstrip("−"))
                self.assertEqual(pct_cell.removeprefix("≤ ").removesuffix("†"), split.pct_from_db(db))
                self.assertEqual(db_cell.startswith("≤ "), pct_cell.startswith("≤ "))

    def test_display_limit(self):
        self.assertEqual(split.through_db(83, True), 80)
        self.assertEqual(split.through_db(83, False), 83)
        self.assertTrue(split.capped(83, True) and not split.capped(83, False))
        self.assertEqual(split.pct_from_db(80), "0.000001 %")
        self.assertEqual(split.pct_from_db(0), "100 %")

    def test_document_embeds_every_graph(self):
        for name in GRAPHS:
            self.assertIn(f"](assets/acoustics/{name})", TEXT)


@unittest.skipUnless(HAVE_GRAPH_DEPS or REQUIRE_GRAPHS, "matplotlib, numpy and scipy are not installed")
class InterpolationTest(unittest.TestCase):
    def test_pink_noise_average_weights_octaves_and_energy(self):
        import numpy as np
        import plots

        frequencies = np.array([31.5, 40, 125, 500, 16000])
        self.assertAlmostEqual(plots.energy_average(frequencies, np.full(5, 7.0)), 7)
        # A straight ramp in log frequency has its endpoint mean, even with an uneven sample grid.
        ramp = 20 * np.log(frequencies / frequencies[0]) / np.log(frequencies[-1] / frequencies[0])
        self.assertAlmostEqual(plots.energy_average(frequencies, ramp), 10)
        self.assertAlmostEqual(plots.energy_average([1, 10, 100], [1, 1, 100]), 25.75)

    def test_label_order_uses_average_only_for_equal_endpoint_height(self):
        import plots

        self.assertEqual(plots.label_order([.6, .6 + 1e-12, .8, .2], [10, 20, 1, 100], 1e-6),
                         [2, 1, 0, 3])
        self.assertEqual(plots.label_order([.5, .5, .5], [7, 7, 7], 1e-6), [0, 1, 2])

    def test_pchip_matches_scipy(self):
        from scipy.interpolate import PchipInterpolator

        cases = [
            ([0, 1, 2], [0, 0, 0]),
            ([0, 1, 2], [0, 1, 1]),
            ([0, 1, 2], [1, 1, 0]),
            ([0, 1, 2], [0, 1, 0]),
            ([0, 1, 3], [1, 0, 1]),
            ([0, 1, 2], [0, 1, 10]),
        ]
        rng = random.Random(314159)
        for _ in range(2000):
            xs = [0.0]
            for _ in range(rng.randrange(2, 8)):
                xs.append(xs[-1] + rng.uniform(.01, 2))
            cases.append((xs, [rng.uniform(-1, 1) for _ in xs]))
        for xs, ys in cases:
            expected = PchipInterpolator(xs, ys, extrapolate=False)
            points = [*xs, *(rng.uniform(xs[0], xs[-1]) for _ in range(3))]
            for x in points:
                with self.subTest(xs=xs, ys=ys, x=x):
                    self.assertAlmostEqual(split.pchip(xs, ys, x), float(expected(x)), delta=1e-12)


@unittest.skipUnless(HAVE_GRAPH_DEPS or REQUIRE_GRAPHS, "matplotlib, numpy and scipy are not installed")
class GraphTest(unittest.TestCase):
    """Regenerate the graphs into a temporary directory and inspect the figures before they are saved."""

    @classmethod
    def setUpClass(cls):
        import matplotlib.figure
        import plots

        cls.figures = []
        save = matplotlib.figure.Figure.savefig

        def capture(fig, path, *args, **kwargs):
            ax = fig.axes[0]
            renderer = fig.canvas.get_renderer()
            cls.figures.append({
                "name": Path(path).name,
                "xscale": ax.get_xscale(),
                "yscale": ax.get_yscale(),
                "ylim": ax.get_ylim(),
                "ylabel": ax.get_ylabel(),
                "xticks": list(ax.get_xticks()),
                "xticklabels": [t.get_text() for t in ax.get_xticklabels()],
                "lines": [(line.get_xdata().copy(), line.get_ydata().copy()) for line in ax.lines],
                "gids": [line.get_gid() for line in ax.lines],
                "line_styles": [(line.get_linestyle(), line.get_marker()) for line in ax.lines],
                "collections": len(ax.collections),
                "labels": [{"gid": t.get_gid(), "text": t.get_text(), "position": t.get_position(),
                            "box": tuple(t.get_window_extent(renderer).bounds)} for t in ax.texts],
                "leaders": [artist.get_gid() for artist in fig.artists
                            if (artist.get_gid() or "").startswith("material-leader-")],
                "label_tolerance": fig.dpi / (160 * ax.bbox.height),
                "figure_size": (fig.bbox.width, fig.bbox.height),
                "ycolor": ax.yaxis.label.get_color(),
                "texts": [t.get_text() for t in fig.texts],
            })
            return save(fig, path, *args, **kwargs)

        cls.tmp = tempfile.TemporaryDirectory()
        matplotlib.figure.Figure.savefig = capture
        try:
            plots.write_plots(ROWS_BUILT, cls.tmp.name)
        finally:
            matplotlib.figure.Figure.savefig = save

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    @staticmethod
    def members(fig):
        if fig["name"].startswith("transmitted"):
            return [[0, 1], [2], [3, *range(5, 18)], [4], [19]]
        return [[i] for i in range(20)]

    def curves_by_material(self, fig):
        return {i: curve for members, curve in zip(self.members(fig), fig["lines"]) for i in members}

    def test_figures_and_axes(self):
        self.assertEqual([f["name"] for f in self.figures], list(GRAPHS))
        for fig in self.figures:
            transmitted = fig["name"].startswith("transmitted")
            log = fig["name"] == "transmitted-log.png"
            self.assertEqual(fig["xscale"], "log")
            self.assertEqual(fig["yscale"], "log" if log else "linear")
            expected_ylim = (1e-7, 2.5) if log else (0, 2.5) if transmitted else (-2, 102)
            self.assertEqual(fig["ylim"], expected_ylim)
            self.assertEqual(fig["xticks"], list(split.FREQS))
            self.assertEqual(fig["xticklabels"], list(split.LABELS))
            members = self.members(fig)
            self.assertEqual(len(fig["lines"]), 5 if transmitted else 20)
            self.assertEqual(fig["gids"], [f"material-{group[0] + 1:02d}" for group in members])
            suffixes = ["-".join(f"{i + 1:02d}" for i in group) for group in members]
            self.assertEqual({label["gid"] for label in fig["labels"]},
                             {f"material-label-{suffix}" for suffix in suffixes})
            self.assertEqual(set(fig["leaders"]), {f"material-leader-{suffix}" for suffix in suffixes})
            self.assertEqual(fig["collections"], 0, "Curves must have no sample dots")
            for style, marker in fig["line_styles"]:
                self.assertEqual(style, "-")
                self.assertIn(marker, (None, "None", "", " "))
            axis = "Logarithmic percentage axis" if log else "Linear percentage axis"
            self.assertTrue(any(axis in t for t in fig["texts"]), fig["name"])
            if log:
                self.assertIn("Transmitted sound — logarithmic energy scale", fig["texts"])
                self.assertIn("Logarithmic scale", fig["ylabel"])
            if transmitted:
                self.assertTrue(any("2.5%" in t for t in [fig["ylabel"], *fig["texts"]]), fig["name"])
                self.assertTrue(any("Open window omitted" in t for t in fig["texts"]), fig["name"])
                self.assertFalse(any("Open window" in label["text"] for label in fig["labels"]))
                self.assertNotEqual(fig["ycolor"], "black")
                self.assertTrue(any("ENERGY AXIS:" in text and "2.5%" in text for text in fig["texts"]))
            for _x, y in fig["lines"]:
                self.assertGreaterEqual(min(y), fig["ylim"][0] - 1e-10)
                self.assertLessEqual(max(y), fig["ylim"][1] + 1e-10)

    def test_curves_match_all_780_unrounded_table_inputs(self):
        import numpy as np

        tables = {"reflected": read_table("Reflected"), "absorbed": read_table("Absorbed"),
                  "transmitted": read_table("Through, in %")}
        samples = 0
        for fig in self.figures:
            kind = fig["name"].removesuffix(".png").split("-")[0]
            curves = self.curves_by_material(fig)
            for i, (row, cells) in enumerate(zip(ROWS_BUILT, tables[kind])):
                if i not in curves:
                    continue
                x, y = curves[i]
                self.assertGreaterEqual(len(x), 1001, (fig["name"], row["name"]))
                self.assertTrue(np.all(np.diff(x) > 0) and x[0] == split.FREQS[0] and x[-1] == split.FREQS[-1])
                self.assertTrue(np.all((y >= -1e-10) & (y <= 100 + 1e-10)))
                positions = np.searchsorted(x, split.FREQS)
                np.testing.assert_array_equal(x[positions], split.FREQS)
                curve = y[positions]
                for i, f in enumerate(split.FREQS):
                    samples += 1
                    cell, py = cells[i + 2], curve[i]
                    where = (fig["name"], cells[0], f, cell)
                    if kind == "reflected":
                        expected = 100 * (1 - row["alpha"][i])
                    elif kind == "absorbed":
                        expected = 100 * (row["alpha"][i] - 10 ** (-row["R"][i] / 10))
                    else:
                        expected = 100 * 10 ** (-row["R"][i] / 10)
                    self.assertAlmostEqual(py, expected, delta=1e-10 * max(1, expected), msg=where)
                    shown = float(cell.removeprefix("≤ ").removesuffix("†").removesuffix(" %"))
                    if kind == "transmitted":
                        table_energy = 100 * 10 ** (-split.through_db(row["R"][i], row["R_est"][i]) / 10)
                        self.assertTrue(math.isclose(shown, one_digit(table_energy), rel_tol=1e-9), where)
                    else:
                        self.assertEqual(shown, round(expected), where)
        self.assertEqual(samples, 780)

    def test_direct_labels_show_averages_and_order_without_overlap(self):
        transmitted_labels = []
        for fig in self.figures:
            metrics = {}
            for members, (x, y) in zip(self.members(fig), fig["lines"]):
                widths = [math.log(b / a) for a, b in zip(x, x[1:])]
                average = sum((a + b) / 2 * width for a, b, width in zip(y, y[1:], widths)) / sum(widths)
                low, high = fig["ylim"]
                endpoint = ((math.log(y[-1] / low) / math.log(high / low)) if fig["yscale"] == "log"
                            else (y[-1] - low) / (high - low))
                gid = "material-label-" + "-".join(f"{i + 1:02d}" for i in members)
                metrics[gid] = endpoint, average
            for label in fig["labels"]:
                endpoint, average = metrics[label["gid"]]
                self.assertIn(f"pink noise average ≈{average:.2g}%", label["text"])
                x, y, width, height = label["box"]
                self.assertGreaterEqual(min(x, y), 0)
                self.assertLessEqual(x + width, fig["figure_size"][0])
                self.assertLessEqual(y + height, fig["figure_size"][1])
            top_down = sorted(fig["labels"], key=lambda label: -label["position"][1])
            for high_label, low_label in zip(top_down, top_down[1:]):
                high_end, high_average = metrics[high_label["gid"]]
                low_end, low_average = metrics[low_label["gid"]]
                if abs(high_end - low_end) <= fig["label_tolerance"]:
                    self.assertGreaterEqual(high_average + 1e-12, low_average)
                else:
                    self.assertGreater(high_end, low_end)
                self.assertGreaterEqual(high_label["box"][1], low_label["box"][1] + low_label["box"][3] + 2)
            if fig["name"].startswith("transmitted"):
                transmitted_labels.append({label["gid"]: label["text"] for label in fig["labels"]})
        self.assertEqual(transmitted_labels[0], transmitted_labels[1],
                         "Energy averages must not depend on whether the vertical axis is linear or logarithmic")

    def test_curves_pass_through_extra_source_frequencies(self):
        import numpy as np
        from scipy.interpolate import PchipInterpolator
        import plots

        for fig in self.figures:
            kind = fig["name"].removesuffix(".png").split("-")[0]
            curves = self.curves_by_material(fig)
            for row_i, row in enumerate(ROWS_BUILT):
                if row_i not in curves:
                    continue
                x, y = curves[row_i]
                key = row["construction"]
                values, estimated = SOURCE_EXTRA_R.get(key, EXTRA_R.get(key, ({}, False)))
                sample_x, sample_y = plots.curve_samples(row, kind)
                expected_frequencies = set(split.FREQS) | (set(values) if kind != "reflected" else set())
                np.testing.assert_array_equal(sample_x, sorted(expected_frequencies))
                if kind == "reflected":
                    continue
                alpha = PchipInterpolator(np.log10(split.FREQS), row["alpha"], extrapolate=False)
                for f, r in values.items():
                    # The measurements constrain R. Added alpha values still come from the ten-band curve.
                    if kind == "transmitted":
                        expected = 100 * 10 ** (-r / 10)
                    else:
                        expected = 100 * (float(alpha(math.log10(f))) - 10 ** (-r / 10))
                    where = (fig["name"], row["name"], f, r)
                    i = np.searchsorted(x, f)
                    self.assertEqual(x[i], f, where)
                    self.assertAlmostEqual(y[i], expected, delta=1e-10 * max(1, expected), msg=where)
                    self.assertAlmostEqual(sample_y[np.searchsorted(sample_x, f)], expected,
                                           delta=1e-10 * max(1, expected), msg=where)

        # BMS panel 708 has a real dip at 192 Hz: 23 dB, below both neighbouring octave anchors.
        pine_i = next(i for i, row in enumerate(ROWS_BUILT) if row["construction"] == "pine_floor")
        for fig in self.figures:
            if not fig["name"].startswith("transmitted"):
                continue
            x, y = self.curves_by_material(fig)[pine_i]
            dip = y[np.searchsorted(x, 192)]
            self.assertAlmostEqual(dip, 100 * 10 ** (-23 / 10), delta=1e-12)
            self.assertGreater(dip, max(y[np.searchsorted(x, 125)], y[np.searchsorted(x, 250)]))

    def test_transmission_has_no_rounding_or_interpolation_stairs(self):
        import numpy as np

        for fig in self.figures:
            if not fig["name"].startswith("transmitted"):
                continue
            curves = self.curves_by_material(fig)
            x, y = curves[0]
            # Brick R at 63/125 Hz rounds to 50/50 dB; at 8/16 kHz it displays as 80/80 dB.
            # The underlying inputs differ, so neither pair may become a flat plotted segment.
            for low, high in ((63, 125), (8000, 16000)):
                section = y[(x >= low) & (x <= high)]
                self.assertGreater(len(section), 50)
                self.assertTrue(np.all(np.diff(section) < 0), (fig["name"], low, high))
            self.assertLess(y[-1], 1e-6, "The table's 80 dB display cap must not flatten the curve")
            # Identical R inputs must draw identically despite their different estimate flags.
            np.testing.assert_array_equal(curves[3][1], curves[5][1])
            # Equal reported endpoints do not establish a flat response throughout the interval.
            # Preserve each reading, but prevent the interpolator from turning them into stair treads.
            for material, intervals in ((2, ((192, 250), (384, 500))), (3, ((160, 200),)),
                                        (4, ((384, 500),))):
                x, y = curves[material]
                for low, high in intervals:
                    section = y[(x >= low) & (x <= high)]
                    self.assertGreater(len(section), 20)
                    self.assertAlmostEqual(section[0], section[-1], delta=1e-12)
                    self.assertGreater(float(np.ptp(section)), float(section[0]) * .001,
                                       (fig["name"], material, low, high))

    def test_committed_graphs_are_current(self):
        self.assertEqual(sorted(p.name for p in ASSETS.iterdir()), sorted(GRAPHS))
        for name in GRAPHS:
            fresh = (Path(self.tmp.name) / name).read_bytes()
            self.assertTrue(fresh == (ASSETS / name).read_bytes(), f"{name} is stale, run split.py")


if __name__ == "__main__":
    unittest.main()
