#!/usr/bin/env python3
"""Split incident sound energy into reflected, absorbed and through shares.

reflected = 1 - alpha            (alpha = book absorption coefficient, everything not reflected)
through   = 10 ** (-R / 10)      (R = sound reduction index of the whole construction, dB)
absorbed  = alpha - through

Emits the Markdown tables and four PNG graphs for docs/acoustics.md, and checks the energy balance.
Graph generation requires matplotlib and scipy, pinned in requirements.txt.

Usage: split.py [TEMPLATE [TARGET]], by default acoustics.template.md next to this file and the
repository's docs/acoustics.md. The graphs go to assets/acoustics/ next to TARGET.
"""
import math
import pathlib
import sys

# ISO 266 octave-band centres. The 31.5 Hz and 16 kHz bands span about 22 Hz to 22 kHz.
FREQS = (31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000)
LABELS = ("31.5 Hz", "63 Hz", "125 Hz", "250 Hz", "500 Hz", "1 kHz", "2 kHz", "4 kHz", "8 kHz", "16 kHz")
N = len(FREQS)
CAP_DB = 80  # preserve the existing display limit for estimates; not a laboratory performance guarantee
RHO_C = 1.21 * 343.0  # characteristic impedance of air, kg/(m^2 s)
C = 343.0


# --- single-leaf prediction (Sharp's method, as given in Bies & Hansen) -------------------------------------------

def critical_frequency(rho, e_mod, nu, h):
    """Coincidence frequency of a homogeneous plate, Hz."""
    m = rho * h
    bending = e_mod * h ** 3 / (12 * (1 - nu ** 2))
    return C ** 2 / (2 * math.pi) * math.sqrt(m / bending)


def critical_frequency_mb(m, bending):
    return C ** 2 / (2 * math.pi) * math.sqrt(m / bending)


def total_loss_factor(f, m, eta_int):
    """Laboratory total loss factor of a heavy leaf, EN ISO 12354-1 Annex C: eta_int + m' / (485 sqrt f)."""
    return eta_int + m / (485 * math.sqrt(f))


def sharp_tl(f, m, f_c, eta_int):
    """Diffuse-field TL of a single leaf, dB.

    f < 0.5 f_c : 20 lg(pi f m / rho c) - 5.5
    f >= f_c    : 20 lg(pi f m / rho c) + 10 lg(2 eta f / (pi f_c)), eta = total loss factor at f
    in between  : straight line in log frequency
    """
    def below(freq):
        return 20 * math.log10(math.pi * freq * m / RHO_C) - 5.5

    def above(freq):
        eta = total_loss_factor(freq, m, eta_int)
        return 20 * math.log10(math.pi * freq * m / RHO_C) + 10 * math.log10(2 * eta * freq / (math.pi * f_c))

    if f < 0.5 * f_c:
        return below(f)
    if f >= f_c:
        return above(f)
    lo, hi = below(0.5 * f_c), above(f_c)
    t = math.log10(f / (0.5 * f_c)) / math.log10(2)
    return lo + t * (hi - lo)


def field_mass_law(f, m):
    return 20 * math.log10(f * m) - 47


# --- interpolation ------------------------------------------------------------------------------------------------

def pchip(xs, ys, x):
    """Shape-preserving piecewise cubic Hermite interpolation (Fritsch-Carlson) at xs[0] <= x <= xs[-1].

    Uses the same derivatives as scipy.interpolate.PchipInterpolator, so data.py needs no scipy.
    """
    n = len(xs)
    assert n >= 3 and all(a < b for a, b in zip(xs, xs[1:])) and xs[0] <= x <= xs[-1], (xs, x)
    h = [b - a for a, b in zip(xs, xs[1:])]
    m = [(ys[k + 1] - ys[k]) / h[k] for k in range(n - 1)]

    def sign(v):
        return (v > 0) - (v < 0)

    def edge(h0, h1, m0, m1):
        d = ((2 * h0 + h1) * m0 - h0 * m1) / (h0 + h1)
        if sign(d) != sign(m0):
            return 0.0
        if sign(m0) != sign(m1) and abs(d) > abs(3 * m0):
            return 3 * m0
        return d

    d = [edge(h[0], h[1], m[0], m[1])]
    for k in range(1, n - 1):
        if sign(m[k - 1]) != sign(m[k]) or m[k - 1] == 0 or m[k] == 0:
            d.append(0.0)
        else:
            w1, w2 = 2 * h[k] + h[k - 1], h[k] + 2 * h[k - 1]
            d.append((w1 + w2) / (w1 / m[k - 1] + w2 / m[k]))
    d.append(edge(h[-1], h[-2], m[-1], m[-2]))
    k = min(max(i for i in range(n - 1) if xs[i] <= x), n - 2)
    t = (x - xs[k]) / h[k]
    return ((2 * t ** 3 - 3 * t ** 2 + 1) * ys[k] + (t ** 3 - 2 * t ** 2 + t) * h[k] * d[k]
            + (-2 * t ** 3 + 3 * t ** 2) * ys[k + 1] + (t ** 3 - t ** 2) * h[k] * d[k + 1])


# --- formatting ---------------------------------------------------------------------------------------------------

DAGGER = "†"


def pct_int(x):
    return f"{round(x * 100)} %"


def through_db(r_db, estimate):
    """Shown dB value: estimates rounded to 5 dB and capped at CAP_DB, sourced values to 1 dB."""
    if r_db == 0:
        return 0
    if not estimate:
        return int(round(r_db))
    return min(int(5 * round(r_db / 5)), CAP_DB)


def capped(r_db, estimate):
    return estimate and through_db(r_db, estimate) >= CAP_DB


def pct_from_db(r_shown):
    share = 10 ** (-r_shown / 10) * 100  # percent
    exp = math.floor(math.log10(share))
    digit = round(share / 10 ** exp)
    if digit == 10:
        digit, exp = 1, exp + 1
    decimals = max(0, -exp)
    return f"{digit * 10 ** exp:.{decimals}f} %"


def mark(text, estimate):
    return f"{text}{DAGGER}" if estimate else text


def table(title, rows, cell, legend):
    out = [f"### {title}", "", "| Material | Thickness | " + " | ".join(LABELS) + " |", "|---|---:|" + "---:|" * N]
    for row in rows:
        out.append(f"| {row['material']} | {row['thickness']} | " + " | ".join(cell(row, i) for i in range(N)) + " |")
    out += ["", legend]
    return "\n".join(out)


def build(rows, constructions):
    for row in rows:
        con = constructions[row["construction"]]
        row["R"] = con["R"]
        row["R_est"] = con["R_est"]
        assert len(row["alpha"]) == len(row["alpha_est"]) == len(con["R"]) == len(con["R_est"]) == N, row["name"]
        for i in range(N):
            alpha = row["alpha"][i]
            assert math.isfinite(alpha) and 0 <= alpha <= 1, (row["name"], FREQS[i], alpha)
            assert math.isfinite(con["R"][i]) and con["R"][i] >= 0, (row["name"], FREQS[i], con["R"][i])
            tau = 10 ** (-con["R"][i] / 10)
            refl, absd = 1 - alpha, alpha - tau
            assert absd >= -1e-12, (row["name"], FREQS[i], alpha, tau)
            assert abs(refl + absd + tau - 1) < 1e-12
    return rows


def render(rows):
    def refl(row, i):
        return mark(pct_int(1 - row["alpha"][i]), row["alpha_est"][i])

    def absd(row, i):
        # An estimated R only marks the absorbed share when the through share is big enough to move the
        # whole percent shown.
        tau = 10 ** (-row["R"][i] / 10)
        return mark(pct_int(row["alpha"][i] - tau), row["alpha_est"][i] or (row["R_est"][i] and tau >= .005))

    def thr_db(row, i):
        shown = through_db(row["R"][i], row["R_est"][i])
        text = "0 dB" if shown == 0 else f"−{shown} dB"
        if capped(row["R"][i], row["R_est"][i]):
            text = f"≤ {text}"
        return mark(text, row["R_est"][i])

    def thr_pct(row, i):
        shown = through_db(row["R"][i], row["R_est"][i])
        text = pct_from_db(shown)
        if capped(row["R"][i], row["R_est"][i]):
            text = f"≤ {text}"
        return mark(text, row["R_est"][i])

    return "\n\n".join([
        table("Reflected", rows, refl,
              "Reflected = 100 % − α. † estimated, see [Assumptions](#assumptions)."),
        table("Absorbed", rows, absd,
              "Absorbed = α − through. † estimated, see [Assumptions](#assumptions)."),
        table("Through, in dB", rows, thr_db,
              "Level of the sound that gets through, relative to the sound that hits the construction. Measured "
              "values are given to 1 dB and estimates (†) to 5 dB. Estimates rounding to 80 dB or more use "
              "≤ −80 dB†, see [Assumptions](#assumptions)."),
        table("Through, in %", rows, thr_pct,
              "The dB values above as a share of the energy, to one significant digit. Every 10 dB less is a "
              "tenth of the energy. The display limit ≤ −80 dB† corresponds to ≤ 0.000001 %†. "
              "† estimated, see [Assumptions](#assumptions)."),
    ])


def render_assumptions(assumptions, constructions):
    out = ["| Rows | Construction assumed | Basis |", "|---|---|---|"]
    for rows, construction, _key, basis in assumptions:
        out.append(f"| {rows} | {construction} | {basis} |")
    out += ["", "Sound reduction index R of each construction, the basis of the Through tables.", "",
            "| Construction | " + " | ".join(LABELS) + " |", "|---|" + "---:|" * N]
    for rows, _construction, key, _basis in assumptions:
        con = constructions[key]
        cells = []
        for i in range(N):
            text = f"{through_db(con['R'][i], con['R_est'][i])} dB"
            if capped(con["R"][i], con["R_est"][i]):
                text = f"≥ {text}"
            cells.append(mark(text, con["R_est"][i]))
        out.append(f"| {rows} | " + " | ".join(cells) + " |")
    return "\n".join(out)


def render_alpha_sources(alpha_sources, anchored):
    """Show the comparable specimens and their weights in the added mid-band α estimates."""
    out = ["| Row | Comparable specimen | Source | Mismatch m | Weight at 250 Hz | Weight at 500 Hz | Weight at 2 kHz |",
           "|---|---|---|---:|---:|---:|---:|"]
    for name, (source, specimen, _values) in alpha_sources.items():
        mismatch, weights = anchored[name]
        cells = [name, specimen, source, f"{mismatch:.2f}"]
        cells.extend(f"{weights[f]:.1%}" for f in (250, 500, 2000))
        out.append("| " + " | ".join(cells) + " |")
    out += ["", "The weights are the shares of the anchored estimate in the weighted average; the remaining share "
            "comes from interpolation. The three acoustic tile rows, both Tectum rows, the plywood panel and "
            "cylinders, perforated transite and the sand-filled timber wall use interpolation at 250 Hz, "
            "500 Hz and 2 kHz."]
    return "\n".join(out)


HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE / "acoustics.template.md"
TARGET = HERE.parents[1] / "docs" / "acoustics.md"


def document(template_text, rows, assumptions, constructions, alpha_sources, anchored):
    """Fill the template's tables, construction assumptions and comparable absorption sources."""
    text = template_text.replace("{{TABLES}}", render(rows))
    text = text.replace("{{ASSUMPTIONS}}", render_assumptions(assumptions, constructions))
    text = text.replace("{{ALPHA_SOURCES}}", render_alpha_sources(alpha_sources, anchored))
    assert "{{" not in text
    return text


if __name__ == "__main__":
    sys.path.insert(0, str(HERE))
    from data import ALPHA_ANCHORED, ALPHA_SOURCES, ASSUMPTIONS, CONSTRUCTIONS, ROWS  # noqa: E402
    from plots import write_plots  # noqa: E402

    template = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else TEMPLATE
    target = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else TARGET
    rows = build(ROWS, CONSTRUCTIONS)
    text = document(template.read_text(), rows, ASSUMPTIONS, CONSTRUCTIONS, ALPHA_SOURCES, ALPHA_ANCHORED)
    write_plots(rows, target.parent / "assets" / "acoustics")
    target.write_text(text)
