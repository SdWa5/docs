#!/usr/bin/env python3
"""Reproduce the absorption-error study behind data.py's weighting constants.

Usage, from the repository root (only the Python standard library is required)::

    python3 -I scripts/acoustics/measure_weights.py /path/to/materials.json

The input is the pyroomacoustics materials database, after Vorländer,
*Auralization* (2008), Appendix A. The dataset used for the constants in data.py
has SHA256 1249f0cfdcd4598cf98ec9be05230f910e53aa1da4861d7fe3f88de23a24e0e0.
It supplies 90 specimens with at least six coefficients, or 8010 ordered pairs.
The same bytes are available at this immutable upstream URL:
https://raw.githubusercontent.com/LCAV/pyroomacoustics/021a666077f4dce8149492d8c704ffcafd0327d2/pyroomacoustics/data/materials.json

PCHIP interpolation through 125 Hz / 1 kHz / 4 kHz is compared with measurements
at 250 Hz / 500 Hz / 2 kHz. Anchoring adds another specimen's deviation from its
own interpolation; mismatch is the largest difference at the three seed bands.
The final fit uses count-weighted 0.01-wide mismatch bins below 0.15 and a cap
equal to the RMS error at mismatch >= 0.15. Earlier exploratory fits are retained
in the output so the original study can be reproduced in full.

The 8 kHz comparisons audit the database rather than set production weights:
44 of its 47 entries at 8 kHz repeat 4 kHz. data.py ignores that column. This
script prints results and does not update data.py or generated documentation.
"""

import argparse
import importlib.util
import itertools
import json
import math
from pathlib import Path


BASE_BANDS = (125, 1000, 4000)
MIDDLE_BANDS = (250, 500, 2000)
AUDIT_BANDS = (*MIDDLE_BANDS, 8000)


def load_pchip():
    """Load the sibling interpolation implementation, including under python -I."""
    path = Path(__file__).resolve().with_name("split.py")
    spec = importlib.util.spec_from_file_location("acoustics_split", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.pchip


def load_specimens(path):
    """Keep the original database order and eligibility rule of six coefficients."""
    with path.open(encoding="utf-8") as source:
        data = json.load(source)
    frequencies = data["center_freqs"]
    specimens = []
    for category, materials in data["absorption"].items():
        for key, material in materials.items():
            coefficients = material["coeffs"]
            if len(coefficients) >= 6:
                specimens.append((category, key, dict(zip(frequencies, coefficients))))
    return specimens


def rms(errors):
    return math.sqrt(sum(error * error for error in errors) / len(errors))


def run_study(specimens, pchip):
    """Print the original study's diagnostics without changing its fit decisions."""
    def interpolate(points, frequency):
        xs = sorted(points)
        return pchip([math.log10(x) for x in xs], [points[x] for x in xs], math.log10(frequency))

    def prediction(alpha, frequency):
        base = {band: alpha[band] for band in BASE_BANDS}
        return alpha[4000] if frequency == 8000 else interpolate(base, frequency)

    print("specimens", len(specimens))
    interpolation_errors = {frequency: [] for frequency in MIDDLE_BANDS}
    for _, _, alpha in specimens:
        base = {frequency: alpha[frequency] for frequency in BASE_BANDS}
        for frequency in MIDDLE_BANDS:
            interpolation_errors[frequency].append(interpolate(base, frequency) - alpha[frequency])
    for frequency in MIDDLE_BANDS:
        print("interp RMS", frequency, round(rms(interpolation_errors[frequency]), 4))
    all_errors = [error for frequency in MIDDLE_BANDS for error in interpolation_errors[frequency]]
    print("interp RMS all", round(rms(all_errors), 4))

    # Exploratory anchoring errors across all ordered pairs, pooled over middle bands.
    pairs = []
    for (category_a, _, alpha), (category_b, _, anchor) in itertools.permutations(specimens, 2):
        mismatch = max(abs(alpha[frequency] - anchor[frequency]) for frequency in BASE_BANDS)
        base = {frequency: alpha[frequency] for frequency in BASE_BANDS}
        anchor_base = {frequency: anchor[frequency] for frequency in BASE_BANDS}
        for frequency in MIDDLE_BANDS:
            estimate = interpolate(base, frequency) + anchor[frequency] - interpolate(anchor_base, frequency)
            pairs.append((mismatch, estimate - alpha[frequency], category_a == category_b))
    boundaries = [0, .02, .05, .1, .15, .2, .3, .5, 1.01]
    for low, high in zip(boundaries, boundaries[1:]):
        errors = [error for mismatch, error, _ in pairs if low <= mismatch < high]
        if errors:
            print(f"anchor mismatch [{low:.2f},{high:.2f}) n={len(errors):5d} RMS={rms(errors):.4f}")

    # Exploratory least-squares fit of sigma_A^2 = s0^2 + k m^2.
    xs = [mismatch * mismatch for mismatch, _, _ in pairs]
    ys = [error * error for _, error, _ in pairs]
    count = len(xs)
    mean_x, mean_y = sum(xs) / count, sum(ys) / count
    slope = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)) / sum((x - mean_x) ** 2 for x in xs)
    intercept = mean_y - slope * mean_x
    print("fit s0^2", round(intercept, 5), "s0", round(math.sqrt(max(intercept, 0)), 4), "k", round(slope, 4))

    print("---- per band, 8k included (flat hold vs anchored), specimens with 8k for the 8k band")
    for frequency in AUDIT_BANDS:
        eligible = [specimen for specimen in specimens if frequency in specimen[2]]
        errors = [prediction(alpha, frequency) - alpha[frequency] for _, _, alpha in eligible]
        sigma_interp = rms(errors)
        points = []
        for (_, _, alpha), (_, _, anchor) in itertools.permutations(eligible, 2):
            mismatch = max(abs(alpha[band] - anchor[band]) for band in BASE_BANDS)
            estimate = prediction(alpha, frequency) + anchor[frequency] - prediction(anchor, frequency)
            points.append((mismatch, estimate - alpha[frequency]))
        # Exploratory squared-error fit in the linear regime, with saturation above.
        linear = [(mismatch, error) for mismatch, error in points if mismatch < .15]
        xs = [mismatch * mismatch for mismatch, _ in linear]
        ys = [error * error for _, error in linear]
        count = len(xs)
        mean_x, mean_y = sum(xs) / count, sum(ys) / count
        slope = (sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
                 / sum((x - mean_x) ** 2 for x in xs))
        intercept = mean_y - slope * mean_x
        saturation = rms([error for mismatch, error in points if mismatch >= .15])
        print(f"{frequency:5d} n={len(eligible)} sigma_I={sigma_interp:.4f} | "
              f"anchor fit s0={math.sqrt(max(intercept, 0)):.4f} c={math.sqrt(max(slope, 0)):.3f} "
              f"(pairs m<.15: {count}) | sat RMS m>=.15: {saturation:.4f}")

    print("---- sigma_A = a + b m on 0.01-wide bins below 0.15 (count-weighted), cap = RMS at m >= 0.15")
    for frequency in AUDIT_BANDS:
        eligible = [specimen for specimen in specimens if frequency in specimen[2]]
        points = []
        for (_, _, alpha), (_, _, anchor) in itertools.permutations(eligible, 2):
            mismatch = max(abs(alpha[band] - anchor[band]) for band in BASE_BANDS)
            points.append((mismatch, prediction(alpha, frequency) + anchor[frequency]
                           - prediction(anchor, frequency) - alpha[frequency]))
        bins = {}
        for mismatch, error in points:
            if mismatch < .15:
                bins.setdefault(int(mismatch * 100 + 1e-9), []).append(error)
        xs, ys, weights = [], [], []
        for key, errors in sorted(bins.items()):
            xs.append((key + .5) / 100)
            ys.append(rms(errors))
            weights.append(len(errors))
        total_weight = sum(weights)
        mean_x = sum(weight * x for weight, x in zip(weights, xs)) / total_weight
        mean_y = sum(weight * y for weight, y in zip(weights, ys)) / total_weight
        slope = (sum(weight * (x - mean_x) * (y - mean_y) for weight, x, y in zip(weights, xs, ys))
                 / sum(weight * (x - mean_x) ** 2 for weight, x in zip(weights, xs)))
        intercept = mean_y - slope * mean_x
        cap = math.sqrt(sum(error * error for mismatch, error in points if mismatch >= .15)
                        / sum(1 for mismatch, error in points if mismatch >= .15))
        print(f"{frequency:5d} a={intercept:.4f} b={slope:.3f} cap={cap:.4f}  bins:",
              " ".join(f"{x:.3f}:{y:.3f}" for x, y in zip(xs, ys)))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("materials", type=Path, help="path to the pyroomacoustics materials.json database")
    args = parser.parse_args(argv)
    try:
        specimens = load_specimens(args.materials)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(f"cannot read materials database: {error}")
    run_study(specimens, load_pchip())


if __name__ == "__main__":
    main()
