# 16. Measurement

> **Draft, pass 1.** This chapter was written from general knowledge and checked against reference literature for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers which instruments a sound system needs, what each of them can and cannot show, and how the
measurement of a loudspeaker or a room is set up so that its result can be trusted. Tuning a system with these
measurements is the subject of chapter 20, and the transfer function behind most of them is explained in [chapter
2](02-frequency-phase-time.md#the-transfer-function).

The classic test bench held a volt-ohm meter, a sine wave oscillator, an oscilloscope, a phase tester, a sound level
meter, a real-time analyzer and a loudness monitor. Most of them still exist, but a laptop with an audio
interface, a measurement microphone and free software now does the work of the larger part of that list, and does
some of it far better.

## Electrical test equipment

### The multimeter

A digital multimeter that reads true RMS, rather than an average scaled for sine waves, measures AC voltages
correctly on any waveform. It checks mains voltage, battery voltage, the DC on a microphone line that carries phantom
power, and the continuity of a cable.

Its resistance range also checks a loudspeaker line before the amplifier is connected. It reads the DC resistance of
the voice coils, which is lower than the nominal impedance, typically by 20 % to 30 %, so a nominal 8 Ω box reads
around 6 Ω.

| Line | Nominal | What the meter shows |
|---|---|---|
| One 8 Ω box | 8 Ω | About 6 Ω |
| Two 8 Ω boxes in parallel | 4 Ω | About 3 Ω |
| Four 8 Ω boxes in parallel | 2 Ω | About 1.5 Ω |
| Four boxes, one not connected | 2.67 Ω | About 2 Ω, a third higher than expected |
| Short circuit | — | Near 0 Ω |

A reading that differs from the sibling lines finds a missing box, a short or a burnt voice coil before power is
applied. A constant-voltage line (chapter 13) cannot be checked this way, because its transformers read almost as a
short at DC. It needs an impedance meter that measures at 1 kHz, and its reading should match $Z = U^2 / P$ for the
connected taps, so 100 Ω for ten loudspeakers at 10 W on a 100 V line.

### Cable and polarity testers

A cable tester checks every pin of XLR, jack, speakON and network cables for continuity, shorts and swapped
conductors in seconds. It is the most useful instrument on a stage per euro spent.

A polarity tester, often called a phase tester, sends a pulse of known polarity into a device or a
loudspeaker and reports whether it comes back with the same sign. It has its traps.
It is sensitive to level, and it fails on anything that changes phase with frequency. A multi-way box with a
crossover reverses the polarity of one way on purpose in some designs, and the phase shift of the crossover filters
makes the pulse arrive smeared, so the tester's answer for the whole box is close to meaningless. It is reliable for
cables, for single drivers and for checking that all boxes of one type agree with each other. The polarity of a
multi-way system is settled by a transfer-function measurement, described below.

### Generators and the oscilloscope

A signal generator is now an app or a function of the measurement software, and the console and the processor
often contain one. Sine tones find rattles and buzzes, sweeps measure responses, and pink noise is the standard
signal for listening and for real-time analysis, because it carries equal energy per octave like music does.

The oscilloscope, once the central bench instrument, has become a specialist tool. A USB oscilloscope or the scope
view of the measurement software shows clipping, oscillation and DC offset, which is mostly what a sound system
needs. Square-wave tests are covered in [chapter 2](02-frequency-phase-time.md#square-waves-and-other-legacy-tests).

## Sound level meters

A sound level meter measures the sound pressure level with a defined frequency weighting and time weighting, as
chapter 3 explains. IEC 61672-1 defines two accuracy classes. Class 1 meets tighter tolerances and is required where
the measurement has legal consequences, such as noise limits at the neighbours or audience exposure. Class 2 is
adequate for setting up a system. An acoustic calibrator per IEC 60942, which produces 94 dB or 114 dB at 1 kHz,
checks the meter before and after each measurement.

The meter must read the quantity the limit refers to. Exposure limits refer to an equivalent continuous level such as
$L_{Aeq}$ over a stated period, and peak limits to $L_{Cpeak}$, so a meter that shows only a momentary level with
fast time weighting cannot prove compliance. Event limits and their logging are in
[chapter 5](05-hearing.md#audience). Phone apps with a calibrated external microphone can come close to class 2, but
phone apps on the internal microphone vary by several dB and stop working at high levels.

## Analyzers

### The real-time analyzer

A real-time analyzer (RTA) shows the level in each band, usually in 31 third-octave bands, of whatever the microphone
picks up. Fed with pink noise, a flat system shows a flat line. It was long the tool for setting a
graphic equalizer band by band.

An RTA shows only the magnitude and only of the sum of everything at the microphone. It cannot separate the direct
sound of the loudspeaker from the reflections of the room, it shows nothing of phase or timing, and it needs pink
noise rather than music. These limits led to the dual-channel analyzer.

### The dual-channel FFT analyzer

A dual-channel analyzer compares the signal sent to the system, the reference, with the signal the microphone
picks up, the measurement, and computes the transfer function between them, magnitude and phase over frequency.
Because it compares, it works with any broadband signal, including music during a show. Smaart, Open Sound Meter and
Room EQ Wizard (REW) are common programs, the first commercial and the other two free.

The analyzer shows four things.

- **Magnitude.** The response of the system in dB, like an RTA but independent of the signal's spectrum.
- **Phase.** The phase difference over frequency, which shows the alignment of drivers and boxes and their polarity.
- **Coherence.** A value between 0 and 1 per frequency that states how much of the measured signal is explained by
  the reference. Low coherence means noise, late reflections or a distorting system, and a data point with low
  coherence is not trusted.
- **Impulse response.** The response to a single click, computed from the same data. Its first peak gives the delay
  from the reference to the microphone, which sets the delay of fills and subwoofers, and its later peaks show
  reflections.

The reference must be taken from the signal as close as possible to the system input, usually from a spare output of
the console or the processor, or by a loopback in the audio interface. The delay between reference and measurement is
found with the delay finder, and 1 ms equals 0.34 m of sound travel.

Swept sine measurements, as in REW, measure the transfer function as well. They reach a higher signal-to-noise ratio
in a given time and separate harmonic distortion from the response, but they need the system to play the sweep and
cannot run during a show.

### Resolution and windows

An FFT analyzer divides the spectrum into bins of equal width, the sample rate divided by the FFT length. A long FFT
resolves fine detail at low frequencies, but it also takes in more of the room's reflections.

| FFT length at 48 kHz | Bin width | Time window |
|---|---|---|
| 1024 | 46.9 Hz | 21 ms |
| 8192 | 5.9 Hz | 171 ms |
| 65536 | 0.73 Hz | 1.37 s |

Analyzers for sound systems therefore combine several FFT lengths, a long one for the bass and short ones for the
treble, which gives an approximately constant resolution per octave. A short time window, either by the FFT length or
by gating the impulse response, shows the loudspeaker almost without the room, while a long window shows what the
audience hears including the room. Both views are needed.

### Averaging

Measurements in a room fluctuate, and averaging several reduces the random part. Averaging $n$ uncorrelated
measurements improves the signal-to-noise ratio by $10 \lg n$, so 4 averages gain 6 dB and 16 gain 12 dB. Averaging
over several microphone positions, rather than over time at one position, is what removes the comb filtering and
room modes that differ from seat to seat, and it gives a response that represents the area, not one seat.

## Measurement microphones

A measurement microphone is a small omnidirectional condenser microphone with a flat response, usually supplied with
an individual calibration file that the software applies. An omnidirectional capsule avoids the proximity effect and
the off-axis colouration of a cardioid, so its reading does not depend on the exact angle.

- **Placement for a loudspeaker.** On axis, at a distance of several times the size of the box, so that all drivers
  have merged into one source. Close distances overstate the driver nearest to the microphone.
- **Ground plane.** A microphone lying on the floor, pointed at the box, avoids the floor reflection that would
  otherwise cause a comb filter. The pressure at the boundary is doubled, which reads 6 dB higher, and that offset is
  constant over frequency.
- **Placement in the audience.** At ear height, at several representative positions per zone, never on the centre
  line only, and away from walls and other reflecting surfaces close to the microphone.
- **Level.** High enough above the background noise for a coherent measurement, and not so high that the system
  compresses or the audience in the room is annoyed.

Two microphones of the same model can differ by a decibel or more. When several are used at once, they are compared
at the same position first, and the difference is corrected or noted.

## In the SdWa5 rig

The rig measures with an audio interface, two measurement microphones and the command `sdwa5-dsp:measure`, which
records reference and microphone channels and computes the transfer function
([automation](../../sdwa5-dsp/docs/automation.md#transfer-function)). The bench results show the methods of this
chapter on real equipment.

- [S1, noise floor and hum](../../sdwa5-dsp/docs/measurements.md#s1-noise-floor-and-hum) separates the noise of the
  amplifiers' fans from the room by switching them on one at a time.
- [C3, SPL offset](../../sdwa5-dsp/docs/measurements.md#c3-spl-offset) ties the microphone's digital level to SPL
  with a simple sound level meter, and states how far that offset can be trusted.
- [Transfer function](../../sdwa5-dsp/docs/measurements.md#transfer-function) reads the delay, polarity and coherent
  range of each cabinet from its impulse response and phase.

## To verify in pass 2

- The ratio of DC resistance to nominal impedance of typical voice coils (20 % to 30 % lower).
- IEC 61672-1 class tolerances and the IEC 60942 calibrator classes and levels.
- Whether phone apps with external microphones reach class 2 performance, and the AES or NIOSH study on apps.
- The licensing of Smaart, Open Sound Meter and REW, and REW's dual-channel mode.
- Polarity-tester behaviour on multi-way boxes with inverted ways.
- Typical sensitivity spread between measurement microphones of one model.

## Sources

- IEC 61672-1, IEC 60942.
- McCarthy, B.: *Sound Systems: Design and Optimization*, Focal Press, 3rd ed. 2016.
- SdWa5: [measurements](../../sdwa5-dsp/docs/measurements.md), [automation](../../sdwa5-dsp/docs/automation.md).
- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §16 (pp. 303–312),
  §8.10 (pp. 101–103).
