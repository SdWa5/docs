"""Ten-band inputs for split.py, extended from the unchanged three-frequency seed data.

The seed data below remains at 125 Hz / 1 kHz / 4 kHz. The final section adds the other seven
ISO 266 octave bands from measurements, comparable specimens or models, and marks every estimate.
The graphs also retain additional source transmission frequencies independently of the ten table bands.
"""

# R in dB per construction; R_est marks values that are estimated or modelled rather than measured for that
# construction.
CONSTRUCTIONS = {
    # 30 cm solid brick measured twice (BMS 144 panel 307: 45/59/61, 591 kg/m2; BIA 5A TL67-32: 44/61/69,
    # 570 kg/m2); 46 cm is nominally 1.5x the mass, +5 dB (DIN 4109 masonry slope 30.9 lg 1.5 = 5.4;
    # mass law 3.5 below, ~7 above coincidence).
    "brick18": {"R": (44.5 + 5, 60 + 5, 65 + 5), "R_est": (True, True, True)},
    # BMS 144 Table 2 panel 228: nominal 50 × 100 mm studs, expanded-metal lath + 19 mm sanded gypsum plaster
    # both sides, 88 kg/m2.
    "lath_plaster": {"R": (29, 45, 54), "R_est": (False, False, False)},
    # PCI Designer's Notebook Acoustics, 150 mm solid concrete wall, 366 kg/m2, ASTM E90.
    "concrete150": {"R": (38, 59, 72), "R_est": (False, False, False)},
    # BMS 144 Table 3 panel 708: nominal 50 × 200 mm joists, 25 mm pine subfloor + 25 mm pine finish floor,
    # fibreboard + plaster ceiling, 77 kg/m2.
    "pine_floor": {"R": (31, 47, 68), "R_est": (False, False, False)},
    # Lining, curtain or seats in front of / on a 150 mm concrete wall or slab; the lining's own share ignored.
    "on_concrete150": {"R": (38, 59, 72), "R_est": (True, True, True)},
    "open": {"R": (0, 0, 0), "R_est": (False, False, False)},
    # No measurement of this construction; heavy walls of similar mass in the lab: 300 mm rammed earth 614 kg/m2
    # ~42/60/66, 300 mm cob 536 kg/m2 ~39/51/60 (Blinet et al. 2026, read from graph), 150 mm concrete 366 kg/m2
    # 38/59/72. Wall: 2 x 25 mm softwood + 250 mm dry sand (1550 kg/m3) ~ 410 kg/m2, tight joints.
    "sand_wall": {"R": (40, 55, 65), "R_est": (True, True, True)},
}

BOOK = (False, False, False)
EST = (True, True, True)

ROWS = [
    {"name": "Brick wall (46 cm thick, unpainted)", "material": "Brick wall (unpainted)", "thickness": "46 cm",
     "alpha": (.02, .04, .07), "construction": "brick18"},
    {"name": "Brick wall (46 cm thick, painted)", "material": "Brick wall (painted)", "thickness": "46 cm",
     "alpha": (.01, .02, .02), "construction": "brick18"},
    {"name": "Interior plaster (on metal lath)", "alpha": (.02, .06, .03), "construction": "lath_plaster"},
    {"name": "Poured concrete", "alpha": (.01, .02, .03), "construction": "concrete150"},
    {"name": "Pine flooring", "alpha": (.09, .08, .10), "construction": "pine_floor"},
    {"name": "Carpeting (with pad)", "alpha": (.10, .30, .70), "construction": "on_concrete150"},
    {"name": "Drapes (cotton, 2× fullness)", "alpha": (.07, .80, .50), "construction": "on_concrete150"},
    {"name": "Drapes (velour, 2× fullness)", "alpha": (.15, .75, .65), "construction": "on_concrete150"},
    {"name": "Acoustic tile (16 mm, #1 mount\\*)", "material": "Acoustic tile (#1 mount\\*)", "thickness": "16 mm",
     "alpha": (.15, .70, .65), "construction": "on_concrete150"},
    {"name": "Acoustic tile (16 mm, #2 mount\\*)", "material": "Acoustic tile (#2 mount\\*)", "thickness": "16 mm",
     "alpha": (.25, .70, .65), "construction": "on_concrete150"},
    {"name": "Acoustic tile (16 mm, #7 mount\\*)", "material": "Acoustic tile (#7 mount\\*)", "thickness": "16 mm",
     "alpha": (.50, .75, .65), "construction": "on_concrete150"},
    {"name": "Tectum panels (25 mm, #2 mount\\*)", "material": "Tectum panels (#2 mount\\*)", "thickness": "25 mm",
     "alpha": (.08, .55, .65), "construction": "on_concrete150"},
    {"name": "Tectum panels (25 mm, #7 mount\\*)", "material": "Tectum panels (#7 mount\\*)", "thickness": "25 mm",
     "alpha": (.35, .35, .65), "construction": "on_concrete150"},
    {"name": "Plywood panel (3 mm, 5 cm air space)", "material": "Plywood panel (5 cm air space)", "thickness": "3 mm",
     "alpha": (.30, .10, .07),
     "construction": "on_concrete150"},
    {"name": "Plywood cylinders (2 layers, 3 mm)", "material": "Plywood cylinders (2 layers)", "thickness": "3 mm",
     "alpha": (.35, .20, .18), "construction": "on_concrete150"},
    {"name": "Perforated transite (with pad, #7 mount\\*)", "alpha": (.90, .95, .45), "construction": "on_concrete150"},
    {"name": "Occupied audience seating area", "alpha": (.50, .95, .85), "construction": "on_concrete150"},
    {"name": "Upholstered theatre seats (hard floor)", "alpha": (.45, .90, .70), "construction": "on_concrete150"},
    {"name": "Open window", "alpha": (1.0, 1.0, 1.0), "construction": "open"},
    {"name": "Sand-filled timber wall (30 cm total)", "material": "Sand-filled timber wall", "thickness": "30 cm total",
     "alpha": (.05, .06, .07), "construction": "sand_wall",
     "alpha_est": EST},
]

for _row in ROWS:
    _row.setdefault("alpha_est", BOOK)
    _row.setdefault("material", _row["name"])
    _row.setdefault("thickness", "—")

# Assumptions table: rows covered, construction assumed with what lies behind it, construction key, basis.
ASSUMPTIONS = [
    ("Brick wall, both rows",
     "Solid brick wall 46 cm, about 870 kg/m², neighbouring room behind",
     "brick18",
     "Two lab tests of 30 cm solid brick at 125 Hz / 1 kHz / 4 kHz, 45 / 59 / 61 dB (BMS 144, Table 2, "
     "panel 307) and 44 / 61 / 69 dB (BIA 5A, Table 1, TL67-32), and at 250 / 500 / 2000 Hz 44 / 53 / 60 dB and "
     "47 / 55 / 66 dB, plus 5 dB for 1.5 times the mass"),
    ("Interior plaster",
     "Wood-stud partition with expanded-metal lath and 19 mm sanded gypsum plaster on both sides, 88 kg/m², "
     "neighbouring room behind",
     "lath_plaster",
     "Lab test, BMS 144, Table 2, panel 228, with 256 / 512 / 2048 Hz taken as 250 / 500 / 2000 Hz"),
    ("Poured concrete",
     "Solid concrete wall 150 mm, 366 kg/m², neighbouring room behind",
     "concrete150",
     "Lab test to ASTM E90, PCI Designer's Notebook *Acoustics*, Fig. 2 and its worked example; 250 / 500 / "
     "2000 Hz read from the graph to about ±1 dB"),
    ("Pine flooring",
     "Timber joist floor with 25 mm pine subfloor and 25 mm pine finish floor, fibreboard and plaster ceiling, "
     "77 kg/m², room below",
     "pine_floor",
     "Lab test, BMS 144, Table 3, panel 708, with 256 / 512 / 2048 Hz taken as 250 / 500 / 2000 Hz"),
    ("Carpeting, drapes, acoustic tile, Tectum panels, plywood panel and cylinders, perforated transite, "
     "audience seating, theatre seats",
     "The finish or object in front of or on a 150 mm concrete wall or slab, room on the other side of the "
     "concrete. For the #7 mount that is the floor above; sound running through the ceiling void into the next "
     "room is not included",
     "on_concrete150",
     "The bare concrete wall above, rounded; the finish itself adds a little, which is ignored"),
    ("Open window",
     "An opening, outside behind it",
     "open",
     "By definition, the reference Sabine used for α = 1 (handbook p. 54)"),
    ("Sand-filled timber wall",
     "Two faces of 25 mm softwood boards with 25 cm of dry sand between them, about 410 kg/m², tight joints, "
     "other side of the wall behind it",
     "sand_wall",
     "No measurement of this construction was found. Heavy walls of similar mass measured in the lab: 300 mm "
     "rammed earth, 614 kg/m², about 42 / 60 / 66 dB, and 300 mm cob, 536 kg/m², about 39 / 51 / 60 dB "
     "(Blinet et al. 2026, Fig. 4a and Fig. 5, read from the graphs), and the 150 mm concrete wall above. "
     "Absorbed share from timber fixed directly to a solid backing, such as parquet on concrete at 0.04 / 0.06 / "
     "0.07 and plywood mounted solidly at 0.05 (akustik.ua compilation)"),
]


# --- Additional frequencies ----------------------------------------------------
# The seed data above stays at 125 Hz / 1 kHz / 4 kHz. Every other band comes from, in this order, a measurement
# of the construction, a measured comparable specimen anchored to the seed, or a model or interpolation.
# Everything that is not a measurement of the construction itself is marked as an estimate.
from split import FREQS, pchip, sharp_tl  # noqa: E402
import math  # noqa: E402

BASE_FREQUENCIES = (125, 1000, 4000)
MID_FREQUENCIES = (250, 500, 2000)
OUTER_FREQUENCIES = (31.5, 63, 8000, 16000)
assert sorted(BASE_FREQUENCIES + MID_FREQUENCIES + OUTER_FREQUENCIES) == sorted(FREQS)


def log_pchip(points, f):
    """PCHIP in log frequency through {frequency: value}."""
    xs = sorted(points)
    return pchip([math.log10(x) for x in xs], [points[x] for x in xs], math.log10(f))


# R at 250 / 500 / 2000 Hz, and whether it is an estimate for the construction.
MEASURED_R = {
    # Mean of BMS 144 panel 307 at 256/512/2048 Hz (44/53/60) and BIA 5A TL67-32 at 250/500/2000 Hz (47/55/66),
    # +5 dB for 1.5x the mass, as at the seed bands.
    "brick18": ((45.5 + 5, 54 + 5, 63 + 5), True),
    # BMS 144 Table 2 panel 228 at 256/512/2048 Hz.
    "lath_plaster": ((28, 38, 46), False),
    # PCI Designer's Notebook Acoustics, Fig. 2, 150 mm solid concrete, read from the third-octave graph to +-1 dB.
    "concrete150": ((43, 52, 67), False),
    # BMS 144 Table 3 panel 708 at 256/512/2048 Hz.
    "pine_floor": ((30, 40, 56), False),
    "on_concrete150": ((43, 52, 67), True),
}

# Additional source frequencies for the graphs, independent of the ten table bands.
# BMS 144 Table 2 panel 228 (printed p. 33) and Table 3 panel 708 (printed p. 53):
# 192 / 384 / 768 Hz are retained at their actual test frequencies.
EXTRA_R = {
    "lath_plaster": ({192: 28, 384: 38, 768: 43}, False),
    "pine_floor": ({192: 23, 384: 40, 768: 44}, False),
    # PCI Fig. 2, printed p. 40: the other ten measured markers of the 150 mm concrete curve, read to +/-1 dB.
    "concrete150": ({160: 41, 200: 41, 315: 45, 400: 48, 630: 54, 800: 57,
                     1250: 62, 1600: 65, 2500: 69, 3150: 71}, False),
}
EXTRA_R["on_concrete150"] = (dict(EXTRA_R["concrete150"][0]), True)

# The two measured 30 cm brick walls have different frequency grids. Preserve the existing 46 cm estimate:
# mean of the two tests +5 dB, interpolating each test in log frequency only within their common range.
# BMS 144 Table 2 panel 307, printed p. 21. The six octave tests use the same nominal-band mapping as above.
BMS_BRICK_R = dict(zip((125, 192, 250, 384, 500, 768, 1000, 2000, 4000),
                      (45, 49, 44, 52, 53, 54, 59, 60, 61)))
# BIA 5A Table 1, TL67-32, PDF p. 8. The 100 and 5000 Hz points inform interpolation but do not extend
# the mean-of-two-tests estimate outside the shared 125 Hz to 4 kHz range.
BIA_BRICK_R = dict(zip((100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000,
                       2500, 3150, 4000, 5000),
                      (44, 44, 44, 46, 47, 52, 52, 55, 57, 59, 61, 63, 65, 66, 66, 67, 69, 71)))
EXTRA_R["brick18"] = ({f: (log_pchip(BMS_BRICK_R, f) + log_pchip(BIA_BRICK_R, f)) / 2 + 5
                       for f in sorted(set(BMS_BRICK_R) | set(BIA_BRICK_R))
                       if 125 < f < 4000 and f not in FREQS}, True)

# Assumed effective plate parameters for the existing Sharp single-leaf model.
# m: kg/m2; fc: Hz; eta_int: dimensionless. They are scenario parameters, not fits
# claiming a unique material characterization. At each outer band the model is
# shifted to the nearest seed-band R value (125 Hz below, 4 kHz above).
SHARP_PARAMETERS = {
    "brick18": {"m": 870.0, "fc": 115.0, "eta_int": 0.015},
    "concrete150": {"m": 366.0, "fc": 130.0, "eta_int": 0.006},
}
BASE_R = {key: dict(zip(BASE_FREQUENCIES, con["R"])) for key, con in CONSTRUCTIONS.items()}

for _key, _con in CONSTRUCTIONS.items():
    _base = BASE_R[_key]
    if _key == "open":
        _con["R"] = (0.0,) * len(FREQS)
        _con["R_est"] = (False,) * len(FREQS)
        continue
    _values = dict(_base)
    _flags = dict(zip(BASE_FREQUENCIES, _con["R_est"]))
    if _key in MEASURED_R:
        _mid, _est = MEASURED_R[_key]
        _values.update(zip(MID_FREQUENCIES, _mid))
        _flags.update((_f, _est) for _f in MID_FREQUENCIES)
    else:
        # The sand wall has no measurement of its own; its seed estimate is interpolated.
        _values.update((_f, log_pchip(_base, _f)) for _f in MID_FREQUENCIES)
        _flags.update((_f, True) for _f in MID_FREQUENCIES)
    _model_key = "concrete150" if _key == "on_concrete150" else _key
    for _f in OUTER_FREQUENCIES:
        _anchor = 125 if _f < 125 else 4000
        if _model_key in SHARP_PARAMETERS:
            _p = SHARP_PARAMETERS[_model_key]
            _delta = sharp_tl(_f, _p["m"], _p["fc"], _p["eta_int"]) - sharp_tl(
                _anchor, _p["m"], _p["fc"], _p["eta_int"])
        else:
            # Stud/plaster and joist-floor systems are not single leaves. For
            # them and the granular sand core, only continue the nearest anchor
            # with the mass-law slope; do not claim to predict their resonances.
            _delta = 20 * math.log10(_f / _anchor)
        _values[_f] = _base[_anchor] + _delta
        _flags[_f] = True
    _con["R"] = tuple(_values[_f] for _f in FREQS)
    _con["R_est"] = tuple(_flags[_f] for _f in FREQS)

# Measured α of a comparable specimen per row at 125 Hz to 4 kHz: (source, specimen, {frequency: α}). The
# database's 8 kHz column is left out, because 44 of its 47 entries with 8 kHz repeat the 4 kHz value.
_PRA = "pyroomacoustics materials database (after Vorländer, *Auralization*, 2008, App. A)"
_EVEREST = "Everest, *The Master Handbook of Acoustics*, 4th ed., App. A"
_OCTAVES = (125, 250, 500, 1000, 2000, 4000)
ALPHA_SOURCES = {
    "Brick wall (46 cm thick, unpainted)":
        (_PRA, "Brick wall, stuccoed with a rough finish", (.03, .03, .03, .04, .05, .07)),
    "Brick wall (46 cm thick, painted)":
        (_PRA, "Smooth brickwork with flush pointing, painted", (.01, .01, .02, .02, .02, .02)),
    "Interior plaster (on metal lath)": (_PRA, "Rough lime wash", (.02, .03, .04, .05, .04, .03)),
    "Poured concrete": (_PRA, "Smooth unpainted concrete", (.01, .01, .02, .02, .02, .05)),
    "Pine flooring": (_PRA, "16 mm wood on 40 mm studs", (.18, .12, .10, .09, .08, .07)),
    "Carpeting (with pad)": (_PRA, "9 mm tufted pile carpet on felt underlay", (.08, .08, .30, .60, .75, .80)),
    "Drapes (cotton, 2× fullness)":
        (_EVEREST, "Cotton, about 475 g/m², draped to 1/2 area", (.07, .37, .49, .81, .65, .54)),
    "Drapes (velour, 2× fullness)":
        (_EVEREST, "Heavy velour, about 610 g/m², draped to 1/2 area", (.14, .35, .55, .72, .70, .65)),
    "Occupied audience seating area":
        (_PRA, "Areas with audience, orchestra or choir including narrow aisles", (.60, .74, .88, .96, .93, .85)),
    "Upholstered theatre seats (hard floor)":
        (_PRA, "Empty chairs, upholstered with cloth cover", (.44, .60, .77, .89, .82, .70)),
}
ALPHA_SOURCES = {name: (source, specimen, dict(zip(_OCTAVES, values)))
                 for name, (source, specimen, values) in ALPHA_SOURCES.items()}

# A is truly dissipated energy, unlike the apparent absorption alpha = A + tau.
# Hard faces retain their 125-Hz A below 125 Hz as a simple scenario assumption.
# Porous/resonant finishes and seating use A(f) = A(125) * (f/125)^2 below it.
# Masovic eq. 8.40 motivates f^2 for thin wall-backed porous layers; applying
# that slope to unspecified resonant objects is an illustrative continuation.
# Above 4 kHz all rows retain A(4 kHz), rather than invent a high-frequency trend.
# Add the newly estimated tau to form alpha; do not extrapolate alpha in a way
# that silently makes true absorption negative when transmission increases.
# Between the seed bands alpha follows a log-frequency PCHIP through the seed. Where a comparable specimen is
# measured, a second estimate adds the specimen's deviation from its own PCHIP to the seed's PCHIP. The two are
# combined by inverse-variance weights, and the result is clipped to [tau, 1].
#
# The variances were measured on the 90 specimens of the pyroomacoustics database. SIGMA_INTERP is the RMS error
# of the PCHIP through a specimen's own 125 Hz / 1 kHz / 4 kHz at the band. SIGMA_ANCHOR is the RMS error of the
# anchored estimate over all 8010 ordered specimen pairs, as a function of the pair's mismatch m, the largest
# difference at 125 Hz / 1 kHz / 4 kHz: a + b m, fitted on 0.01-wide bins below m = 0.15, and the RMS above.
SIGMA_INTERP = {250: 0.113, 500: 0.107, 2000: 0.060}
SIGMA_ANCHOR = {250: (0.014, 0.838, 0.161), 500: (0.013, 0.778, 0.159), 2000: (0.003, 0.379, 0.090)}


def anchor_weight(f, mismatch):
    """Inverse-variance weight of the anchored estimate at band f."""
    a, b, cap = SIGMA_ANCHOR[f]
    sigma = min(a + b * mismatch, cap)
    return sigma ** -2 / (sigma ** -2 + SIGMA_INTERP[f] ** -2)


HARD_FACE_CONSTRUCTIONS = {"brick18", "lath_plaster", "concrete150", "pine_floor", "sand_wall"}
ALPHA_CONTINUATION = []
ALPHA_ANCHORED = {}
for _row in ROWS:
    _key = _row["construction"]
    _alpha = dict(zip(BASE_FREQUENCIES, _row["alpha"]))
    _flags = dict(zip(BASE_FREQUENCIES, _row["alpha_est"]))
    if _key == "open":
        _row["alpha"] = (1.0,) * len(FREQS)
        _row["alpha_est"] = (False,) * len(FREQS)
        continue
    _r = dict(zip(FREQS, CONSTRUCTIONS[_key]["R"]))
    _tau = {_f: 10 ** (-_r[_f] / 10) for _f in FREQS}
    _power = 0 if _key in HARD_FACE_CONSTRUCTIONS else 2
    _a125 = _alpha[125] - _tau[125]
    _a4k = _alpha[4000] - _tau[4000]
    _values = dict(_alpha)
    for _f in MID_FREQUENCIES:
        _values[_f] = log_pchip(_alpha, _f)
    for _f in OUTER_FREQUENCIES:
        _values[_f] = (_a125 * (_f / 125) ** _power if _f < 125 else _a4k) + _tau[_f]
    if _row["name"] in ALPHA_SOURCES:
        _src = ALPHA_SOURCES[_row["name"]][2]
        _src_base = {_f: _src[_f] for _f in BASE_FREQUENCIES}
        _mismatch = max(abs(_alpha[_f] - _src[_f]) for _f in BASE_FREQUENCIES)
        _weights = {}
        for _f in MID_FREQUENCIES:
            _anchored = min(1.0, max(0.0, _values[_f] + _src[_f] - log_pchip(_src_base, _f)))
            _weights[_f] = anchor_weight(_f, _mismatch)
            _values[_f] = _weights[_f] * _anchored + (1 - _weights[_f]) * _values[_f]
        ALPHA_ANCHORED[_row["name"]] = (_mismatch, _weights)
    for _f in FREQS:
        if _f not in _alpha:
            _values[_f] = min(1.0, max(_tau[_f], _values[_f]))
            _flags[_f] = True
    _row["alpha"] = tuple(_values[_f] for _f in FREQS)
    _row["alpha_est"] = tuple(_flags[_f] for _f in FREQS)
    ALPHA_CONTINUATION.append((_row["name"], _power))
