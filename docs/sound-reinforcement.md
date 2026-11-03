# SdWa5 — Sound reinforcement

A handbook on live sound for the people who set up, run and plan SdWa5's events, and for anyone else who wants
one. It covers the physics of sound, the equipment from the microphone to the loudspeaker, hearing and the limits
that protect it, and the design and tuning of a system for a real event. It is written for today's practice, in
which consoles, processors and amplifiers are digital, loudspeakers are designed and aligned with measurement and
prediction software, signals travel over networks, and hearing protection is a matter of regulation. Its chapters,
their order and their figures are its own, and each chapter names the literature it draws on in its *Sources*.

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

| # | Chapter | Covers |
|---|---|---|
| | **Part I. Foundations** | |
| 1 | [Signals and systems](sound-reinforcement/01-signals-and-systems.md) | Sound waves, phase and polarity, the signal chain, digital audio, block diagrams |
| 2 | [Frequency, phase and time](sound-reinforcement/02-frequency-phase-time.md) | Transfer function, standard bands, filters and slopes, voices and instruments, comb filters |
| 3 | [Decibels, levels and loudness](sound-reinforcement/03-decibels-levels-loudness.md) | dB units, analog and digital levels, SPL, weighting, loudness, LUFS |
| 4 | [Dynamic range, headroom and gain structure](sound-reinforcement/04-dynamic-range-gain-structure.md) | Headroom, S/N, preamp gain, matching processor and amplifier, compression as range management |
| | **Part II. Hearing and acoustics** | |
| 5 | [Hearing](sound-reinforcement/05-hearing.md) | Thresholds, masking, precedence, exposure limits, hearing protection |
| 6 | [Sound outdoors](sound-reinforcement/06-sound-outdoors.md) | Distance loss, air absorption, weather, barriers, neighbours, feedback |
| 7 | [Sound indoors](sound-reinforcement/07-sound-indoors.md) | Reflection and absorption, room modes, reverberation, critical distance, intelligibility |
| | **Part III. Equipment** | |
| 8 | [Specifications](sound-reinforcement/08-specifications.md) | Reading data sheets, noise, distortion, digital specifications |
| 9 | [Microphones and DI](sound-reinforcement/09-microphones.md) | Transducer types, polar patterns, sensitivity, phantom power, DI boxes |
| 10 | [Wireless](sound-reinforcement/10-wireless.md) | Frequencies in the EU, analog and digital systems, intermodulation, antennas, in-ear transmitters, intercom |
| 11 | [Mixing consoles](sound-reinforcement/11-mixing-consoles.md) | Channel strip, busses, digital consoles and stageboxes, splits, front-of-house placement |
| 12 | [Signal processing](sound-reinforcement/12-signal-processing.md) | Equalisers, delay, reverb, dynamics, loudspeaker processors, feedback suppression |
| 13 | [Power amplifiers](sound-reinforcement/13-power-amplifiers.md) | Amplifier classes, ratings, mains supply, matching to loudspeakers, 100 V systems |
| 14 | [Loudspeakers](sound-reinforcement/14-loudspeakers.md) | Drivers, enclosures, directivity, crossovers, line arrays, subwoofer arrays |
| 15 | [Cables, connectors and networks](sound-reinforcement/15-cables-connectors-networks.md) | Balanced lines, connectors, speaker cable loss, digital audio and networks |
| 16 | [Measurement](sound-reinforcement/16-measurement.md) | Meters and testers, SPL meters, FFT analysis, measurement practice |
| | **Part IV. Systems** | |
| 17 | [Power, grounding and safety](sound-reinforcement/17-power-grounding-safety.md) | Protective earth, RCDs, distribution, ground loops, switch-on order |
| 18 | [Stage monitoring](sound-reinforcement/18-stage-monitoring.md) | Wedges, fills, in-ear monitors, monitor mixing, ringing out |
| 19 | [Control and sync](sound-reinforcement/19-control-and-sync.md) | MIDI, OSC, show control, timecode, clock synchronisation, playback |
| 20 | [System design and tuning](sound-reinforcement/20-system-design-and-tuning.md) | Brief, prediction, coverage, subwoofer design, alignment, tuning, a worked event |

[Acoustics](acoustics.md) is a companion page with reflection, absorption and transmission data for common
materials. Chapter 7 uses it as its reference table.

## Sources

- Each chapter lists the standards, papers, books and SdWa5 documents it relies on in its own *Sources* section.
- General references are McCarthy, B.: *Sound Systems: Design and Optimization*,
  Focal Press, 3rd ed. 2016, and Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal
  Leonard 1989, ISBN 0-88188-900-8.
