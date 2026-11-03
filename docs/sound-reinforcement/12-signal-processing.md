# 12. Signal processing

> **Draft, pass 1.** This chapter was written from general knowledge and checked against reference literature for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers what the processors between the console and the amplifiers do, and what they cannot do. It
covers equalizers, delay, reverb, dynamics processors, loudspeaker management, feedback suppression, automatic mixing
and the modulation effects. Filters, slopes and phase are explained in
[chapter 2](02-frequency-phase-time.md), compression as range management in
[chapter 4](04-dynamic-range-gain-structure.md#compression-and-limiting-as-range-management), and the measurement
that guides equalization in chapter 16.

Each of these functions used to be a separate box in a rack. Today
almost all of them run inside the digital console or a loudspeaker processor, often several times per channel.
What they do has changed less than where they sit.

## Equalizers

### Kinds of filter

- **Shelving filters** raise or lower everything above or below a corner frequency by a set amount, like the bass and
  treble controls of a hi-fi amplifier. They suit broad tonal changes.
- **Parametric filters** raise or lower a band around a centre frequency, with three controls for frequency, gain and
  bandwidth. The bandwidth is given as Q or in octaves, and a Q of 1.41 is one octave and 4.32 one third of an octave,
  as chapter 2 explains. Four to eight parametric bands per channel are standard on digital consoles.
- **High-pass and low-pass filters** remove everything beyond a corner frequency, with a slope of 6 dB per octave per
  order. They are covered in chapter 2.
- **Graphic equalizers** have a fixed set of bands, each with a slider, so the positions of the sliders draw a rough
  picture of the correction. A third-octave graphic has 31 bands on the ISO 266 centre frequencies from 20 Hz to
  20 kHz.

Older designs include sweep equalizers, which have an adjustable frequency but a fixed bandwidth, and the
so-called paragraphic, which is a set of parametric bands. Both are forms of the parametric filter today.

### Graphic equalizers in detail

The bands of a graphic overlap. Two behaviours are common.

- **Constant Q.** Each band keeps its bandwidth whatever its gain, so a small boost is as narrow as a large one.
  Neighbouring bands then combine with ripple between their centres.
- **Proportional Q.** The bandwidth narrows as the gain rises, so a small boost is broad and gentle and a large cut is
  narrow. Neighbouring bands combine more smoothly at small settings.

Neither shape matches the slider picture exactly. When two adjacent sliders are both raised by 6 dB, the response
between them rises by more or less than 6 dB depending on the design, and a single slider at full cut narrows or
widens differently from its neighbours. The graphic shows the intent, while the response curve on a digital console
shows the result, which is the one to trust.

### What equalization can and cannot fix

An equalizer changes the level of a band for everybody who hears the system. It fixes problems that are the same at
every seat, such as the tonal balance of a loudspeaker, the build-up of low frequencies from several boxes and the
air absorption at a distance. It cannot fix a problem that differs from seat to seat.

- **Comb filters** from two sources or a reflection put notches at frequencies that change with the position, as
  chapter 2 shows. A boost at a notch at one seat fills nothing there, because the notch is a cancellation, and adds
  a peak at the next seat.
- **Room modes** below the Schroeder frequency differ by position too, as chapter 7 shows.
- **Gaps between the ways of a loudspeaker** at the crossover come from the alignment of the drivers. An equalizer can
  lift the band, but the cancellation stays, and it moves with the listening angle.
- **Reverberation** is energy that the room returns late. An equalizer that lowers a band lowers the direct sound in
  that band too.

Why tuning with an analyser that shows only level misleads is covered in chapter 5. Modern
transfer-function measurement averages several positions and shows the phase and the coherence. Corrections where
the coherence is low address reflections and are mostly wasted. Chapter 20 describes system tuning.

### Linear phase and dynamic equalizers

A conventional equalizer filter is minimum phase, so it changes the phase together with the level, which chapter 2
explains. An FIR filter can be linear phase, changing the level without the phase, at the cost of latency. In
loudspeaker processors, FIR filters are used to correct the phase response of a loudspeaker and to build crossovers
without phase shift.

A dynamic equalizer applies a band's boost or cut only when the level in that band exceeds a threshold. It suits
problems that come and go, such as a harsh resonance on loud notes of a singer, a boomy note on a bass guitar or
sibilance.

## Delay

A delay holds the signal back for a set time. Its uses in sound reinforcement are alignment and effect.

### Alignment

Sound in air travels 0.343 m per millisecond. A delay that matches a distance brings two sources into time.

| Distance | Delay |
|---|---|
| 1 m | 2.92 ms |
| 3 m | 8.75 ms |
| 10 m | 29.15 ms |
| 20 m | 58.31 ms |
| 40 m | 116.62 ms |

- **Delay loudspeakers.** A loudspeaker 40 m from the main system receives a delay of about 117 ms so that its sound
  arrives with the main system's. A further few milliseconds, often 5 to 15 ms, make the main system arrive first,
  so that the precedence effect keeps the image on the stage, as chapter 5 explains. Chapter 20 sets the times by
  measurement.
- **Front fills and subwoofers.** The front fills along the stage edge and a subwoofer array on the ground are aligned
  to the main system at the seats where they overlap.
- **Microphones on one source.** A microphone close to a guitar cabinet and another further away are aligned in the
  console to avoid a comb filter in the mix.

### History

Tape echo and analog bucket-brigade delays have given way to digital ones. All delay is
digital today, with any length, no loss of quality and a resolution of one sample, which is 21 µs at 48 kHz.

## Reverb

Reverb adds the decay of a room to a dry signal. In a live system it gives close-miked vocals and instruments the
sense of space that they lose by being picked up from a few centimetres away.

Reverb was once made physically, in rooms, ducts, springs and steel plates. Two digital methods are in use today.

- **Algorithmic reverb** builds the decay from networks of delays and filters. It offers parameters such as the decay
  time, the pre-delay before the reverb starts, the size, the damping of high frequencies and the density of the early
  reflections. Simulations of plates and springs are among its presets.
- **Convolution reverb** applies a measured impulse response of a real room or device. It sounds like that room, but it
  offers fewer controls and needs more processing.

In a live room, the reverb of the system adds to the room's own reverberation. A reverberant hall needs less of it,
and a reverb with a long tail on a vocal in a hall with 2 s of reverberation mostly reduces intelligibility. A
pre-delay of 20 to 60 ms keeps the start of each word dry, and a high-pass filter on the reverb return keeps it out of
the low frequencies that the room already has plenty of.

## Dynamics processors

### Compressor and limiter

A compressor reduces the level of the signal above a threshold by a ratio. With a threshold of −20 dB and a ratio of
4 to 1, a signal 12 dB over the threshold comes out 3 dB over it.

| Input | Output | Gain reduction |
|---|---|---|
| −30 dB | −30 dB | 0 dB |
| −20 dB | −20 dB | 0 dB |
| −12 dB | −18 dB | 6 dB |
| −8 dB | −17 dB | 9 dB |
| 0 dB | −15 dB | 15 dB |

The controls are the same on every compressor.

- **Threshold and ratio** set where and how strongly it acts. A ratio of 10 to 1 or more acts as a limiter.
- **Attack** sets how quickly the gain falls when the signal rises above the threshold, typically from under a
  millisecond to about 100 ms. A slower attack lets the start of a note through, which keeps punch.
- **Release** sets how quickly the gain returns, typically from 50 ms to over a second. A short release pumps audibly,
  a long one holds the level down after a loud passage.
- **Knee** sets whether the ratio applies suddenly at the threshold (hard knee) or gradually around it (soft knee).
- **Make-up gain** restores the level lost to compression.

### Newer forms

- **Look-ahead limiter.** The processor delays the signal by a few milliseconds and reacts to what is coming, so it
  can catch a peak completely. It is standard in loudspeaker processors, where a missed peak can damage a driver.
- **True-peak limiter.** It limits the level between the samples, which matters before a converter or a lossy codec.
- **Multiband compressor.** Splits the signal into bands and compresses each separately, so a loud bass note does not
  pull down the voice.
- **De-esser.** Compresses only the sibilant band, typically between 4 and 10 kHz, when it exceeds a threshold.
- **Sidechain.** The detector listens to a filtered or a different signal from the one it controls, which is how a
  de-esser and a ducker work.

### Gate, expander and ducker

A gate mutes a signal below a threshold, and an expander lowers it by a ratio. On a drum kit, a gate on each tom
removes the bleed from the rest of the kit, and on a noisy instrument it removes the hum between notes. A gate needs a
range, so that it lowers rather than mutes when that sounds more natural, and a hold time and hysteresis, so that it
does not chatter at the threshold. A gate can also be keyed from another source, such as a kick drum
gating a bass tone, on any console with sidechain inputs.

A ducker lowers one signal when another is present, such as the background music when a presenter speaks.

## Loudspeaker management

A loudspeaker management processor sits between the console and the amplifiers and turns a mix into what each
amplifier channel needs. It combines several functions that were once separate boxes.

- **Crossover.** Splits the signal into the bands for subwoofers, low, mid and high drivers, with chosen filter types
  and slopes, as chapter 2 explains.
- **Delay.** Aligns the drivers within a box and the boxes within a system.
- **Equalization.** Corrects the loudspeaker's response and the system's response in the room.
- **Limiters.** Protect each driver and amplifier, with thresholds set from the amplifier's gain and the driver's power
  rating, as chapter 4 shows. A peak limiter protects against clipping and excursion, and an RMS limiter against
  heat over time.
- **Polarity and gain** for each output.

Many amplifiers now contain this processing, and loudspeaker manufacturers supply presets that set it for their boxes.
A preset from the manufacturer is usually the better start than one built by ear.

## Feedback suppression and automatic mixing

### Feedback suppressors

A feedback suppressor detects a frequency that rings, by its steady and growing sine-like character, and places a
narrow notch on it. Fixed notches are set during the ring-out before the show, and dynamic ones follow new feedback
during it and are released when it stops. A good suppressor gains a few decibels of gain before feedback with little
audible change. A suppressor that is allowed too many notches cuts into the programme and can mistake a sustained
note for feedback. Chapter 7 describes the manual ring-out.

### Automatic mixers

An automatic mixer opens the microphone of whoever is talking and lowers the others. The most common method, gain
sharing, distributes a constant total gain among the microphones in proportion to their levels. A single talker gets
full gain, and two talkers at equal level each get −3 dB, so the system behaves as if one microphone were open. The
gain before feedback that chapter 6 loses with the number of open microphones, 3 dB per doubling, is gained back.
Automatic mixers are standard for panel discussions, conferences and council meetings, and many digital consoles have
one built in.

## Effects

Flangers, phasers and exciters remain in use as effects rather than corrections.

- **Flanger and chorus.** Mix the signal with a copy that is delayed by a few milliseconds, with the delay slowly
  varied. A delay of 1 ms places the first notch of the resulting comb filter at 500 Hz and one of 5 ms at 100 Hz.
- **Phaser.** Mixes the signal with a copy passed through all-pass filters, which shift the phase and produce fewer,
  irregularly spaced notches.
- **Exciter.** Adds generated harmonics to the high frequencies to make a signal brighter and more present. Used
  sparingly on dull sources, it can help a voice through a dense mix.
- **Pitch correction and harmonisers** process vocals in real time and are common in some styles of music.

## In the SdWa5 rig

The rig's DSP 8x8 was measured on the bench after the MARK Salzburg event, and three findings illustrate this chapter.
Its limiters act on the peak, and their threshold holds a 100 Hz signal about 2.2 dB higher than a 1 kHz one. Its
compressors produce an image of the signal mirrored around 24 kHz while they reduce gain, so a bus compressor that
works all the time colours the top end, while a limiter that catches the odd peak costs nothing. The automatic
equalization of one Tecnare top left a hollow of 8.5 dB at 2.5 kHz between its two ways, which the crossover rather
than the equalizer has to close.

The findings and their consequences for the rig are in
[On the bench, 2026-09-29](../../sdwa5-3d/docs/signal-chain.md#on-the-bench-2026-09-29). The raw measurements are in
[B3, limiter and threshold](../../sdwa5-dsp/docs/measurements.md#b3-limiter-and-threshold) and
[Auto EQ and gain rider on the device](../../sdwa5-dsp/docs/measurements.md#auto-eq-and-gain-rider-on-the-device),
and the tools that took them in [Gain rider, compressor, auto EQ and measurements](../../sdwa5-dsp/docs/automation.md).

## To verify in pass 2

- The behaviour of constant-Q and proportional-Q graphic equalizers when adjacent bands are combined; check
  Rane and other manufacturer notes.
- The typical ranges of attack (under 1 ms to 100 ms) and release (50 ms to over 1 s).
- The precedence offset of 5 to 15 ms for delay loudspeakers.
- The de-esser band of 4 to 10 kHz.
- Gain-sharing automatic mixing (Dugan) and its constant total gain.
- The detection methods of feedback suppressors.

## Sources

- ISO 266, preferred frequencies.
- Dugan, D.: Automatic microphone mixing, *JAES* 23, 1975.
- SdWa5: [Signal chain](../../sdwa5-3d/docs/signal-chain.md), section *On the bench, 2026-09-29*;
  [Measurements](../../sdwa5-dsp/docs/measurements.md); [Automation](../../sdwa5-dsp/docs/automation.md).
- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §14 (pp. 244–280).
