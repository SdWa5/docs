# SdWa5 — Sound reinforcement

A handbook on live sound for the people who set up, run and plan SdWa5's events, and for anyone else who wants
one. It covers the physics of sound, the equipment from the microphone to the loudspeaker, hearing and the limits
that protect it, and the design and tuning of a system for a real event. Its chapters follow the topics of
Davis and Jones, *The Sound Reinforcement Handbook* (2nd ed., Yamaha / Hal Leonard 1989), which taught a
generation of engineers and is still worth reading. Since 1989, consoles, processors and amplifiers have become
digital, loudspeakers are designed and aligned with measurement and prediction software, signals travel over
networks, and hearing protection has become a matter of regulation. This handbook is a complete rewrite for that
world, in its own words, its own order and its own figures. The 1989 book is cited by section and page wherever a
chapter covers the same ground, and the [concordance](#concordance) maps every one of its sections to a chapter
here.

**Status.** This is pass 1, a full draft written quickly so that the whole book can be read. Every chapter carries
a draft banner and ends with a list *To verify in pass 2*, which names each claim that has not yet been checked
against its primary source. Pass 2 works through those lists chapter by chapter, adds generated figures and removes
the banners. Until then, treat named standards, editions and limit values as pointers to check, not as quotations.

## Conventions

- **Units** are SI. Distances are in metres, pressures in pascals, and electrical supply is 230/400 V at 50 Hz.
  The speed of sound is 343 m/s (20 °C) unless a section states a temperature.
- **Levels** always carry their reference, as in dBu, dBV, dBFS or dB SPL. A level written as plain dB is a
  difference or a gain. Weighted sound levels are written as dB(A) and dB(C). Chapter 3 defines all of them.
- **Gain** means voltage gain unless a section says otherwise.
- **Standards** are cited by number. International (IEC, ISO) and AES standards come first, then European
  directives and EN standards, then Austrian (ÖVE, ÖNORM) and German (DIN) ones where they are the regional
  reference. SdWa5 is based in Austria, so national rules are Austrian unless a section says otherwise.
- **Numbers** in tables and worked examples are computed, not copied, and rounded as the text states.
- **Diagrams** are Mermaid flowcharts rendered by GitHub from the page source. Signal flows from left to right, a
  box is a device or a function, a solid arrow carries audio and a dotted arrow carries control or clock. Chapter 1
  explains the conventions.
- **Formulas** use GitHub's math rendering, so they read as formulas in the browser and as plain LaTeX in the
  source.
- **The SdWa5 rig** appears as a worked example where its own documentation exists. Those links point into the
  sibling repositories `sdwa5-3d` and `sdwa5-dsp` and resolve in a local checkout with the siblings next to this
  repository.

## Contents

| # | Chapter | Covers | Handbook § |
|---|---|---|---|
| | **Part I. Foundations** | | |
| 1 | [Signals and systems](sound-reinforcement/01-signals-and-systems.md) | Sound waves, phase and polarity, the signal chain, digital audio, block diagrams | 1, 7 |
| 2 | [Frequency, phase and time](sound-reinforcement/02-frequency-phase-time.md) | Transfer function, standard bands, filters and slopes, voices and instruments, comb filters | 2, 8.9, 8.10 |
| 3 | [Decibels, levels and loudness](sound-reinforcement/03-decibels-levels-loudness.md) | dB units, analog and digital levels, SPL, weighting, loudness, LUFS | 3, 8.7, App. A |
| 4 | [Dynamic range, headroom and gain structure](sound-reinforcement/04-dynamic-range-gain-structure.md) | Headroom, S/N, preamp gain, matching processor and amplifier, compression as range management | 4, 11.7 |
| | **Part II. Hearing and acoustics** | | |
| 5 | [Hearing](sound-reinforcement/05-hearing.md) | Thresholds, masking, precedence, exposure limits, hearing protection | 9, 3.6 |
| 6 | [Sound outdoors](sound-reinforcement/06-sound-outdoors.md) | Distance loss, air absorption, weather, barriers, neighbours, feedback | 5, 18.3.3 |
| 7 | [Sound indoors](sound-reinforcement/07-sound-indoors.md) | Reflection and absorption, room modes, reverberation, critical distance, intelligibility | 6, 18.3.4–5 |
| | **Part III. Equipment** | | |
| 8 | [Specifications](sound-reinforcement/08-specifications.md) | Reading data sheets, noise, distortion, digital specifications | 8 |
| 9 | [Microphones and DI](sound-reinforcement/09-microphones.md) | Transducer types, polar patterns, sensitivity, phantom power, DI boxes | 10.1–10.4, 11.2 |
| 10 | [Wireless](sound-reinforcement/10-wireless.md) | Frequencies in the EU, analog and digital systems, intermodulation, antennas, in-ear transmitters, intercom | 10.5, 10.6 |
| 11 | [Mixing consoles](sound-reinforcement/11-mixing-consoles.md) | Channel strip, busses, digital consoles and stageboxes, splits, front-of-house placement | 11.1–11.6, 11.8, 11.10, 11.12 |
| 12 | [Signal processing](sound-reinforcement/12-signal-processing.md) | Equalisers, delay, reverb, dynamics, loudspeaker processors, feedback suppression | 14 |
| 13 | [Power amplifiers](sound-reinforcement/13-power-amplifiers.md) | Amplifier classes, ratings, mains supply, matching to loudspeakers, 100 V systems | 12 |
| 14 | [Loudspeakers](sound-reinforcement/14-loudspeakers.md) | Drivers, enclosures, directivity, crossovers, line arrays, subwoofer arrays | 13 |
| 15 | [Cables, connectors and networks](sound-reinforcement/15-cables-connectors-networks.md) | Balanced lines, connectors, speaker cable loss, digital audio and networks | 15, 17.3, 18.4 |
| 16 | [Measurement](sound-reinforcement/16-measurement.md) | Meters and testers, SPL meters, FFT analysis, measurement practice | 16, 8.10.1 |
| | **Part IV. Systems** | | |
| 17 | [Power, grounding and safety](sound-reinforcement/17-power-grounding-safety.md) | Protective earth, RCDs, distribution, ground loops, switch-on order | 17.4–17.8 |
| 18 | [Stage monitoring](sound-reinforcement/18-stage-monitoring.md) | Wedges, fills, in-ear monitors, monitor mixing, ringing out | 11.9, 11.11 |
| 19 | [Control and sync](sound-reinforcement/19-control-and-sync.md) | MIDI, OSC, show control, timecode, clock synchronisation, playback | 19, 20 |
| 20 | [System design and tuning](sound-reinforcement/20-system-design-and-tuning.md) | Brief, prediction, coverage, subwoofer design, alignment, tuning, a worked event | 17.1, 17.2, 18 |

[Acoustics](acoustics.md) is a companion page with reflection, absorption and transmission data for common
materials. Chapter 7 uses it as its reference table.

## Concordance

Each section of the 1989 handbook and the chapter that covers its topic here. The labels are short descriptions,
not the handbook's own titles.

| Handbook § | Topic | Chapter |
|---|---|---|
| 1 | What a sound system is | 1 |
| 2 | Frequency response | 2 |
| 3.1–3.5 | Decibels, electrical and acoustic levels, RMS, gain | 3 |
| 3.6 | Loudness and weighting | 3, 5 |
| 4 | Dynamic range and headroom | 4 |
| 5 | Sound outdoors | 6 |
| 6 | Sound indoors | 7 |
| 7 | Block diagrams | 1 |
| 8.1–8.6, 8.8 | Specifications, noise, distortion, impedance, crosstalk | 8 |
| 8.7 | Operating levels | 3 |
| 8.9 | Filter slopes | 2 |
| 8.10 | Square-wave tests and oscilloscopes | 2, 16 |
| 8.11 | Dimensions and weight | 8 |
| 9 | Hearing and perception | 5 |
| 10.1–10.4 | Microphones | 9 |
| 10.5–10.6 | Radio intercom and radio microphones | 10 |
| 11.1–11.6, 11.8 | Preamps, mixers and consoles, balanced inputs, linking a second mixer | 11 |
| 11.7 | Gain structure | 4 |
| 11.9, 11.11 | Monitor desks and feedback on stage | 18 |
| 11.10, 11.12 | Sharing microphone signals, where the desks go | 11 |
| 12 | Power amplifiers | 13 |
| 13 | Loudspeakers | 14 |
| 14 | Signal processing | 12 |
| 15 | Cables and connectors | 15 |
| 16 | Test equipment | 16 |
| 17.1–17.2 | Kinds of systems and how to structure one | 20 |
| 17.3 | Interconnection | 15 |
| 17.4–17.8 | Earthing, transformers, mains, racks, fault finding | 17 |
| 18.1–18.3, 18.5–18.7 | Loudspeaker system design | 20 (18.3.3 also 6, 18.3.4–5 also 7) |
| 18.4 | Loudspeaker cabling | 15 |
| 19 | MIDI | 19 |
| 20 | Synchronisation and timecode | 19 (20.3 dropped) |
| App. A | Logarithms | 3 |

Sections the modern chapters drop entirely, such as tape transport control, are named in the *What changed since
1989* table of the chapter that covers their neighbourhood.

## Sources

- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989,
  ISBN 0-88188-900-8. Cited by section and page throughout.
- Each chapter lists the standards, papers and SdWa5 documents it relies on in its own *Sources* section.
