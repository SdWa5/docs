# 8. Specifications

> **Draft, pass 1.** This chapter was written from general knowledge and checked against the 1989 handbook for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers how to read a data sheet so that its numbers mean something. It explains why a figure without
its conditions is worthless, and it goes through frequency response, noise, distortion, impedance, crosstalk, the
specifications of digital equipment and the mechanical data, each with what a complete statement contains. It ends
with a checklist. It replaces handbook §8 (pp. 71–104) except §8.7, which is in
[chapter 3](03-decibels-levels-loudness.md), and §8.9 and §8.10, which are in
[chapter 2](02-frequency-phase-time.md). How a measurement and a listener can disagree is in
[chapter 5](05-hearing.md).

## A number needs its conditions

A specification is a measurement result, and a measurement result is only meaningful with the conditions under which
it was taken. The handbook states the rule plainly, and it remains the best test of any data sheet. A competent
technician with standard test equipment should be able to repeat the measurement from the data sheet alone and get
the same result. Anything that would stop them, such as an unnamed load, an unknown bandwidth or an unstated level,
makes the figure unverifiable.

The handbook illustrates this with an invented data sheet in which every line looks plausible and none can be checked.
The same exercise works today with a sheet of the kind found on many product pages.

| Line on the sheet | What is missing |
|---|---|
| Frequency response 20 Hz – 20 kHz | The tolerance in dB and the level at which it was measured |
| THD < 0.01 % | The level, the frequency, the load and the bandwidth of the measurement |
| Dynamic range 115 dB | Weighting, bandwidth, and whether it is AES17 or an output noise figure against full scale |
| Max output +24 dBu | The load and the distortion at which "maximum" was decided |
| Input impedance 10 kΩ | Whether balanced or unbalanced, and at which frequency |
| Latency < 1 ms | Which path, at which sample rate, and whether converters are included |
| Max SPL 135 dB | Peak or continuous, at what distance, with which signal and for how long |

A data sheet that gives the conditions for each figure is usually from a manufacturer who expects to be checked. One
that gives round numbers without conditions should be read as an advertisement.

Two habits help. The first is to compare devices only on figures measured the same way, ideally to the same standard.
The second is to look for the graph behind the number, because a graph shows what a single figure hides.

## Frequency response

Three different statements are often confused.

- **Frequency response** is the output level over frequency at a stated level, within a stated tolerance, such as
  20 Hz to 20 kHz, +0/−1 dB at +4 dBu. Without a tolerance it says nothing, because every device produces some
  output at 20 Hz.
- **Frequency range** is the range in which a device does something useful, without a tolerance. It is a marketing
  figure.
- **Power bandwidth** is the range in which an amplifier reaches its rated output at a stated distortion. It is
  usually narrower than the small-signal frequency response, because an amplifier can follow a quiet signal at
  50 kHz but not a loud one.

For electronic equipment, ±0.5 dB from 20 Hz to 20 kHz is easy to achieve and should be expected. Loudspeakers are a
different case. A loudspeaker's response depends on the direction, the distance, the room and the mounting, so its
data sheet needs the measuring conditions in detail. A figure such as 45 Hz to 18 kHz at −10 dB says much less than
an on-axis graph and a set of off-axis curves. AES2-2012 and IEC 60268-5 describe how loudspeaker components and
systems are to be measured, and CTA-2034 describes a set of curves for direct, early-reflected and sound-power
response that predicts in-room behaviour well.

A graph is worth more than a printed range, provided its scale is honest. A vertical axis of 50 dB over a short
height makes a response with ±3 dB of ripple look flat, and smoothing to one-third octave hides narrow peaks.

## Noise

### What noise is and how it is shaped

Noise is any unwanted signal that is not related to the wanted one. Its most basic form, thermal noise, comes from the
random motion of electrons in every resistor and sets a limit that no amplifier can beat.

- **White noise** has equal energy per hertz. Per octave its energy doubles, so it rises by 3 dB per octave on a
  fractional-octave analyser, and the octave from 10 to 20 kHz contains half its energy.
- **Pink noise** has equal energy per octave. On a third-octave analyser it reads flat, which is why it is the test
  signal for system equalization. It is white noise filtered at −3 dB per octave.

A noise figure depends on the bandwidth of the measurement and on the weighting. For white noise, a measurement
weighted with the A-curve reads about 2 dB lower than an unweighted one over 20 Hz to 20 kHz, and an unweighted
measurement with an 80 kHz bandwidth reads about 6 dB higher. A difference of 8 dB between two data sheets can come
from the measuring conditions alone.

### Equivalent input noise

The noise of a microphone preamplifier is specified as equivalent input noise (EIN), the noise at the output divided
by the gain, so that it can be compared with the signal at the input. A source resistance must be stated, because
the preamplifier cannot be quieter than the resistor at its input. The thermal noise voltage of a resistance $R$ over
a bandwidth $B$ at absolute temperature $T$ is given by Boltzmann's constant $k$.

$$v_n = \sqrt{4 k T R B}$$

For 150 Ω, 20 kHz and 290 K, this is 219 nV, or −131.0 dBu. For 200 Ω it is −129.7 dBu. A microphone preamplifier
with an EIN of −128 dBu at 150 Ω therefore adds 3 dB to the noise of an ideal source, which is good. A figure of
−135 dBu at 150 Ω is below the thermal limit, so it was measured with a shorted input, A-weighted or in a narrower
bandwidth, and it cannot be compared with the others.

A complete EIN statement reads like this: −128 dBu, 150 Ω source, 20 Hz to 20 kHz, unweighted, at 60 dB gain. The
gain matters, because at low gain the stages after the preamplifier add their own noise and the EIN gets worse.

### Output noise

The output noise of a console depends on how many channels are routed to the bus, where the faders and the master
sit, whether the hum was included and how the output was terminated. The handbook shows one console described in four
ways that differ by 20 dB. The method still applies. A useful statement names the routing, the positions of the
controls, the bandwidth, the weighting and the load.

### Hum, buzz and other noises

Hum is the mains frequency and its harmonics, at 50, 100, 150 Hz and up in Europe, and it gets into a system through
earth loops, magnetic fields near transformers and poorly filtered power supplies. Buzz contains much higher
harmonics, typically from phase-cut dimmers and switch-mode supplies. Radio frequency that a circuit rectifies turns
into crackle or into a radio station in the PA. None of these is usually specified, and all of them depend more on
the installation than on the device. Chapter 17 covers the causes and the remedies.

## Distortion

### Harmonic distortion

A nonlinear device adds harmonics, components at integer multiples of the input frequency. Total harmonic distortion
(THD) is their combined level relative to the fundamental, as a percentage or in decibels.

| THD | In dB |
|---|---|
| 10 % | −20 dB |
| 1 % | −40 dB |
| 0.1 % | −60 dB |
| 0.01 % | −80 dB |
| 0.001 % | −100 dB |

Most analysers measure THD+N, which removes the fundamental with a notch filter and measures everything that is left,
including noise and hum. At low levels, THD+N is dominated by noise and rises as the level falls, while at high levels
it rises sharply at clipping. A THD+N curve against level shows both, while a single figure shows only one point on
it.

A total says nothing about which harmonics are present. Low, even harmonics are much less audible than high, odd
ones, and chapter 5 gives the handbook's example where a loudspeaker's larger distortion does not hide an amplifier's
smaller one. A spectrum of the distortion products tells more than the total.

### Intermodulation distortion

Two tones through a nonlinear device produce sum and difference frequencies that are not harmonically related to
either, and these intermodulation (IM) products are more audible than harmonics. Two standard methods are in use.

- **SMPTE IM** (also in DIN and IEC variants) uses a low tone, typically 60 Hz, and a high tone, typically 7 kHz, at a
  level ratio of 4 to 1, and it measures the sidebands around the high tone.
- **CCIF or twin-tone IM** uses two high tones close together, such as 19 and 20 kHz at equal level, and it measures
  the difference frequency at 1 kHz and other products in the audible range.

Twin-tone tests reveal problems at high frequencies that a THD test at 1 kHz misses, because the harmonics of a
10 kHz tone lie above the audio band and are filtered out of a THD measurement.

### Transient intermodulation

Transient intermodulation (TIM) was proposed in the 1970s for amplifiers that distorted on fast transients because
their input stage overloaded before the feedback could correct it. It was controversial then and is rarely
specified now, because a current amplifier's slew rate lies far above what audio requires. An amplifier delivering
100 W into 8 Ω has a peak voltage of 40 V and needs a slew rate of about 5 V/µs to reproduce a full-power 20 kHz
sine.

## Impedance

### Bridging rather than matching

Every output has a source impedance, and every input has a load impedance. Early telephone and broadcast practice
matched them, typically at 600 Ω, which transfers maximum power but halves the voltage, a loss of 6 dB. Modern audio
equipment instead uses bridging, where the input impedance is at least about ten times the source impedance, so the
voltage arrives almost unchanged.

| Source | Load | Loss |
|---|---|---|
| 600 Ω | 600 Ω | −6.02 dB |
| 100 Ω | 600 Ω | −1.34 dB |
| 600 Ω | 10 kΩ | −0.51 dB |
| 150 Ω | 10 kΩ | −0.13 dB |
| 50 Ω | 10 kΩ | −0.04 dB |

Line outputs today are typically 50 to 150 Ω and line inputs 10 to 20 kΩ, and a microphone input is 1 to 3 kΩ for a
microphone of 150 to 200 Ω. Only some old equipment, such as transformer-coupled outputs that expect a 600 Ω
termination and certain vintage effects, still needs a matched load to stay flat. Chapter 9 covers microphone and
instrument inputs.

### Impedance changes with frequency

An impedance is not a fixed number. A loudspeaker rated 8 Ω may fall to 5 Ω at one frequency and rise to 40 Ω at its
resonance, and an amplifier sees all of that. Input and output impedances of electronics also vary, usually rising
or falling at the ends of the band through coupling capacitors and cable capacitance. A specification should state the
frequency, and a loudspeaker's impedance curve with its minimum is more useful than its nominal rating.

### Mismatches

A low impedance load pulls down a source's voltage and can push its output stage into current limiting, as when an
amplifier drives 2 Ω or when a headphone amplifier drives a low-impedance headphone. A high source impedance into a
long cable loses the high frequencies, because the cable's capacitance forms a low-pass filter with it. Both are
reasons why outputs are specified with a minimum load and why a data sheet should give the source impedance of each
output.

## Crosstalk

Crosstalk is a signal from one channel appearing in another. It arises from capacitive coupling between conductors,
from inductive coupling between wires carrying current, from shared ground return paths and from shared power supplies.
Capacitive coupling rises with frequency at 6 dB per octave, so a figure of −80 dB at 1 kHz becomes −60 dB at 10 kHz.
A useful crosstalk specification therefore gives the figure at several frequencies, or as a curve, and names the
channels and the loads.

In cables, crosstalk between pairs in a multicore is small at audio frequencies when the pairs are individually
shielded or twisted, and the main risk is a loudspeaker cable or a digital signal run alongside microphone lines.
Inside digital equipment, crosstalk is almost absent in the processing and occurs mainly in the analog stages and
converters.

## Digital equipment

Digital equipment has its own specifications, most of them defined in AES17 for measurement and in AES11 for
synchronisation.

- **Dynamic range** per AES17 is measured with a signal at −60 dBFS, so that the noise and distortion are measured
  together at a low level, and it is usually A-weighted. A 24-bit word allows 146 dB in theory, and real converters
  reach 110 to 125 dB, limited by their analog circuits.
- **THD+N** is given in dB relative to full scale, typically at −1 dBFS, and is often better than −100 dB.
- **Maximum level** is the analog level that produces 0 dBFS, such as +18 dBu or +24 dBu. It sets the alignment that
  chapter 3 explains.
- **Latency** is the delay from analog input to analog output. A buffer of 64 samples takes 1.33 ms at 48 kHz and
  0.67 ms at 96 kHz, and the converters add their own filter delay. A complete statement names the path and the sample
  rate.
- **Jitter** is timing uncertainty in the sample clock. It limits the achievable signal-to-noise ratio at high
  frequencies. With 1 ns of jitter, a full-scale 20 kHz sine cannot exceed about 78 dB, with 100 ps about 98 dB, and
  with 10 ps about 118 dB. Modern converters with good clock recovery reach the low picosecond range.
- **Sample rate conversion** introduces its own noise and filter ripple and should be specified by the same AES17
  measurements.

A digital processor's frequency response, noise and distortion are often better than any analog circuit around it,
so the converters and the analog stages decide the result. A network audio device is specified by the same measures
plus the network latency setting, which chapter 15 covers.

## Loudspeaker and system specifications

Loudspeaker specifications are where data sheets diverge most. A maximum SPL can be a peak level with a short burst
measured at 1 m, a continuous level with pink noise calculated from sensitivity and power, or a measured value with a
music-like test signal. The difference can be 10 dB.

- **Sensitivity** is the level at 1 m with 1 W or 2.83 V input. For an 8 Ω loudspeaker, 2.83 V is 1 W, and for a
  4 Ω loudspeaker it is 2 W, which makes the 4 Ω sensitivity look 3 dB better.
- **Power handling** per AES2-2012 is measured with a band-limited noise of 6 dB crest factor for two hours, and per
  IEC 60268-5 with a programme simulation noise. Neither is a recommendation for amplifier power.
- **Maximum SPL** with M-Noise (AES75) uses a test signal designed to resemble music in its crest factor across
  frequency, so the figure is comparable between manufacturers who use it.
- **Coverage** should be given as the angle between the −6 dB points, horizontal and vertical, and how it changes
  with frequency. A single figure such as 90° × 40° says nothing about the midrange and bass.
- **Subwoofer output** is described by CTA-2010 as the maximum level at each frequency below a distortion limit.

Chapter 14 returns to loudspeaker data, and chapter 13 to amplifier ratings.

## Mechanical data

The 19-inch rack is 482.6 mm wide at the front panel, and one rack unit (U) is 44.45 mm high. A data sheet should
give the depth behind the front panel separately from the total depth with knobs and handles, because the depth of a
rack case is usually the limit. Weight should be net, with the packed weight given as well for transport planning.
For a road case, add the case and the cables, and for flying loudspeakers, the rigging and its working load limit,
which chapter 20 covers.

## Checklist for a data sheet

1. **Conditions with every figure.** Level, frequency, bandwidth, weighting, load and gain.
2. **Graphs behind numbers.** Frequency response with tolerance, THD+N against level and frequency, impedance curve,
   polar data.
3. **Standards named.** AES17 for digital, AES2 or IEC 60268-5 for loudspeakers, AES75 for maximum SPL, CTA-2034 or
   CTA-2010 where they apply.
4. **Physical limits respected.** An EIN below the thermal limit or a dynamic range beyond the converter's bits is a
   sign of a different method, not of a better device.
5. **Like with like.** Two devices are compared only on figures measured the same way.
6. **Mechanics.** Depth behind the panel, net weight, power consumption and inrush current.

## What changed since 1989

| Handbook | Then | Today |
|---|---|---|
| §8.1–8.1.3 | An invented sheet of doubtful specs, reproducibility as the test | Same test, own example sheet with digital and loudspeaker figures |
| §8.2 | Response, range, power bandwidth, graph versus number | Kept, with CTA-2034 and AES2 for loudspeakers |
| §8.3 | Noise types, EIN, output noise in four versions | Kept, with the thermal limit computed and bandwidth effects quantified |
| §8.4, §8.5 | THD by notch, SMPTE and CCIF IM | Kept, THD+N curves against level |
| §8.5.4 | TIM, controversial | Rarely specified, slew rate explained |
| §8.6 | Matching at 600 Ω versus bridging | Bridging is standard, matching kept for old gear |
| §8.8 | Crosstalk causes and specification | Kept, with digital equipment |
| §8.11 | Rack dimensions and weight in inches and pounds | Metric, with depth behind the panel and rigging |
| — | Not covered | AES17 digital specifications, latency, jitter, M-Noise, CTA-2010 |

## To verify in pass 2

- The A-weighting and bandwidth effects on white noise (−2 dB, +6 dB at 80 kHz); recompute with the IEC 61672-1
  weighting formula and check against AES17.
- The typical EIN figures of current preamplifiers (around −128 dBu at 150 Ω).
- AES2-2012 test signal and duration, and IEC 60268-5 programme simulation noise.
- AES75 (M-Noise) title, year and scope.
- CTA-2034 and CTA-2010 titles, current editions and scope.
- AES17 measurement of dynamic range at −60 dBFS and the weighting it allows.
- The SMPTE and CCIF IM frequencies and ratios; check IEC 60268-3.
- Typical converter dynamic range of 110 to 125 dB in current stageboxes.
- The jitter limit formula and typical jitter values of current converters.
- The 19-inch rack dimensions per IEC 60297 and EIA-310.

## Sources

- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §8 (pp. 71–104).
- AES17, measurement of digital audio equipment.
- AES2-2012, specification of loudspeaker components used in professional audio and sound reinforcement.
- AES75, measuring loudspeaker maximum linear sound levels using noise (M-Noise).
- IEC 60268-3, amplifiers, and IEC 60268-5, loudspeakers.
- CTA-2034, standard method of measurement for in-home loudspeakers; CTA-2010, subwoofer output measurements.
- IEC 60297 and EIA-310, rack dimensions.
