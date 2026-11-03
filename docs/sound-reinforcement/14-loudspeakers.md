# 14. Loudspeakers

> **Draft, pass 1.** This chapter was written from general knowledge and checked against the 1989 handbook for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers how a loudspeaker turns power into sound, why a box of a given size has the bass and the
directivity it has, how drivers are combined with crossovers, how boxes are combined into point-source systems, line
arrays and subwoofer arrays, how a loudspeaker data sheet is read, and how loudspeakers fail. It replaces handbook §13
(pp. 209–243). Amplifiers are in [chapter 13](13-power-amplifiers.md), and filters and crossover alignments in
[chapter 2](02-frequency-phase-time.md).

## Drivers

Almost every loudspeaker in sound reinforcement uses the electrodynamic principle. A voice coil in the gap of a
magnet carries the signal current and moves, and it drives a diaphragm that moves the air.

- **Cone drivers** move a paper or composite cone, from small midrange drivers to 21-inch subwoofer drivers. Their
  long-throw versions move the cone by tens of millimetres at full power.
- **Compression drivers** drive a light dome diaphragm into a small chamber, which opens through a narrow throat into
  a horn. The compression raises the efficiency strongly, to the point that a compression driver on a horn is far
  louder than a cone driver of the same power, and it is the standard for high frequencies in professional systems.
- **Ribbon and air-motion transformer (AMT) drivers** use a thin folded or flat membrane, and they appear as
  high-frequency drivers in some systems.

The handbook also covers piezoelectric tweeters, which were cheap and needed no crossover, but they are not used in
professional systems today. Neodymium magnets, much stronger per kilogram than ferrite, have cut the weight of
drivers by half or more and made flown arrays practical.

## Directivity

A driver radiates in all directions when it is small compared with the wavelength, and it concentrates its output
forward as the wavelength becomes comparable to its size. As a rule, the pattern starts to narrow where the
circumference equals the wavelength, $ka = 1$, and it is narrow where the diameter equals the wavelength.

| Driver | Effective diameter | Starts to narrow ($ka = 1$) | Narrow ($\lambda = d$) |
|---|---|---|---|
| 1-inch dome | 2.5 cm | 4.4 kHz | 13.7 kHz |
| 6.5-inch cone | 14 cm | 780 Hz | 2.5 kHz |
| 12-inch cone | 26 cm | 420 Hz | 1.3 kHz |
| 15-inch cone | 33 cm | 330 Hz | 1.0 kHz |
| 18-inch cone | 40 cm | 270 Hz | 860 Hz |

A 15-inch driver in a two-way box therefore beams above about 1 kHz, and a crossover to the horn below that point
keeps the pattern consistent. A subwoofer of any size is practically omnidirectional over its range. Directivity at
low frequencies needs size or several sources, which is the reason for the subwoofer arrays later in this chapter.

### Horns and waveguides

A horn loads a driver acoustically and shapes its coverage. It controls the pattern down to roughly the frequency at
which its mouth is one wavelength wide, so a mouth of 0.5 m controls to about 690 Hz and one of 1 m to about 340 Hz.
The handbook describes the change from exponential horns, whose pattern narrowed with rising frequency, to the
constant-directivity horns of the 1980s, which hold a stated coverage over a wide band. Today's waveguides continue
that line. They are shallow horns optimised by simulation for smooth coverage, often with asymmetric patterns that
throw further at the top of the pattern than at the bottom.

A horn whose throat is driven hard adds distortion, because air is not linear at very high pressure. This is part of
why a compression driver sounds harsh when it is pushed close to its limits.

## Enclosures and bass

A cone driver on its own cancels its bass, because the front and the back of the cone radiate in opposite polarity
and the sound from the back wraps around. An enclosure separates the two.

- **Sealed box.** The air in the box acts as a spring, and the response falls by 12 dB per octave below the resonance.
  It is compact and has a good transient response.
- **Vented box (bass reflex).** A port, tuned with the air volume to a frequency near the bottom of the range, adds
  output there and falls by 24 dB per octave below it. It is the most common design for tops and subwoofers.
- **Bandpass.** The driver sits inside one or two chambers and radiates only through a port, which gives high
  output in a narrow band.
- **Horn-loaded bass.** A horn, usually folded to fit into a box, raises the efficiency of a bass driver. A real
  low-frequency horn needs a mouth of several metres, so a folded subwoofer is a compromise, and several of them
  side by side act as a larger mouth.

The behaviour of a driver in a box can be predicted from a few measured parameters, the Thiele-Small parameters,
such as the resonance frequency, the moving mass, the compliance and the losses. Box design software uses them.

One law limits every design. For a direct radiator, the efficiency is proportional to the box volume and to the cube of
the lowest frequency, which is often called Hofmann's iron law. To halve the lowest frequency at the same efficiency,
the box needs eight times the volume. In the same box, halving the lowest frequency costs a factor of eight in
efficiency, or 9 dB. A small box with deep bass is possible, but only by giving up level, which is why loudspeakers
for events are large.

## Crossovers

A crossover splits the signal so that each driver receives only the band it reproduces well.

- **Passive crossovers** sit inside the box, after the amplifier. They are simple to connect but waste power in their
  components, cannot be adjusted, and place the amplifier's output impedance behind a network that weakens its control
  of the bass driver.
- **Active crossovers** split the signal before separate amplifier channels. The handbook lists their advantages,
  which are more headroom because each amplifier handles only one band, efficiency, better damping, and lower
  intermodulation because a clipping bass channel does not distort the high frequencies. All of these still hold.

A digital processor or an amplifier with DSP now provides the crossover along with delay to align the drivers in
time, equalization for each way and limiters for each driver, as chapter 12 describes. A Linkwitz–Riley alignment,
with two filters of the same order that sum flat in level and in phase, is the usual choice, and chapter 2 explains
it. FIR filters can build crossovers with linear phase, at the cost of latency. Loudspeaker manufacturers supply
presets that contain all of this for their boxes, and a box run without its preset sounds and behaves differently from
its data sheet.

Many current boxes are self-powered, with the amplifier and the processing built in.

## Combining boxes

### Point-source systems and clusters

A single box or a small cluster of boxes, each covering its own angle, acts as a point source and loses 6 dB per
doubling of distance, as chapter 6 explains. Where the coverage of two boxes overlaps, they interfere and produce a
comb filter, so a well-built cluster splays its boxes so that their patterns meet at about their −6 dB points. The
handbook's estimate for clusters, between 3 and 6 dB more level per doubling of the number of boxes, assumes some
overlap. Coaxial boxes, with the horn in the centre of the bass driver, behave like one source and are common as
monitors and fills.

### Line arrays

A line array is a vertical column of identical boxes, close enough together that they act as one source over most of
their range. Its advantage is control of the vertical pattern, which can be shaped by the angles between the boxes
and by processing so that the level stays even from the front to the back of the audience. Chapter 6 shows that a
line source loses only 3 dB per doubling of distance in its near field.

The boxes act as one source only where their spacing is less than half a wavelength. A box of 0.3 m height couples
coherently up to about 570 Hz with conventional drivers, which is why line-array boxes use waveguides that form a flat
wavefront at high frequencies across the whole height of the box. Criteria for when a column of sources behaves as a
continuous line have been published as the wavefront sculpture technology (WST) criteria, which require that the
flat wave sources fill most of the array's height. At low frequencies, a line array is shorter than the wavelength
and becomes a point source.

Line arrays are designed in the manufacturer's prediction software, which chapter 20 discusses, because the angles,
the trim height and the processing interact.

### Steerable columns

A column of small drivers, each with its own amplifier and processing, can steer and shape its vertical beam
electronically. Such columns serve speech in reverberant spaces such as churches, stations and halls, where they
place the sound on the audience and keep it off the ceiling, which chapter 7 explains.

## Subwoofer arrays

Subwoofers are omnidirectional on their own, but several together can be arranged to shape their pattern.

### Coupling

Subwoofers placed close together, within a fraction of a wavelength, add coherently in all directions and gain 6 dB
per doubling of their number at low frequencies. A floor and a wall add further gain, as chapter 7 shows.

### Left and right or centre

Subwoofers placed left and right of the stage, as most systems were built in 1989, produce a comb filter across the
audience. On the centre line both arrive together, and the sum is loud, which is called the power alley. Off the
centre line the path difference creates cancellations.

| Listener off the centre line (subwoofers 10 m apart, listener at 30 m) | Path difference | First cancellation |
|---|---|---|
| 1 m | 0.33 m | 522 Hz |
| 2 m | 0.66 m | 261 Hz |
| 5 m | 1.62 m | 106 Hz |
| 10 m | 3.13 m | 55 Hz |

A few metres off the centre line, the first cancellation falls into the subwoofer range, and the bass changes from
seat to seat. A central array, either a line of subwoofers along the front of the stage or a flown array, gives the
same bass across the audience and is preferred wherever the stage allows it.

### Arcs and delay-shaded lines

A straight line of subwoofers along the stage narrows the pattern in the horizontal plane and sends side lobes to
the sides. Placing the boxes on an arc, or electronically delaying the outer boxes so that the line behaves like an
arc, widens the pattern to cover a wide audience.

### Cardioid arrays

A cardioid array suppresses the sound behind the subwoofers, which keeps the stage quieter and helps feedback, the
monitor mix and the neighbours behind the stage.

- **Gradient arrays** use a box facing backwards, or a box behind the front ones, delayed by the distance between them
  and polarity-inverted, so that its sound cancels the front boxes' sound behind the array and adds in front. With
  0.6 m between the fronts of the boxes, the delay is 1.75 ms.
- **End-fire arrays** place several boxes in a row from front to back, spaced a quarter wavelength apart at a design
  frequency and delayed so that they add in front and cancel behind. For 80 Hz, the spacing is 1.07 m and the delay
  per box 3.12 ms.

Both reach well over 10 dB of rear rejection over most of the subwoofer range when they are set up by measurement.
Chapter 6 gives the basic delay for a pair, and chapter 20 the measurement.

## Reading a loudspeaker data sheet

Chapter 8 explains why data sheets need conditions. For loudspeakers they need more than for any other device.

- **Frequency response.** A curve with a tolerance and the measurement conditions, preferably on axis and at several
  off-axis angles, and with the processing preset named.
- **Sensitivity.** The level at 1 m with 1 W or with 2.83 V. Into 8 Ω both are 1 W, but into 4 Ω 2.83 V is 2 W, which
  makes the 4 Ω box look 3 dB more sensitive than it is per watt.
- **Power handling.** Per AES2-2012, with band-limited noise of 6 dB crest factor for two hours, or per IEC 60268-5
  with programme simulation noise. It is a survival rating, not a recommendation for amplifier power.
- **Maximum SPL.** Peak, continuous or measured with M-Noise (AES75), which chapter 8 explains.
- **Impedance.** A curve with its minimum, which is what the amplifier sees.
- **Coverage.** Horizontal and vertical angles between the −6 dB points, and a plot of how they change with frequency.
  A full balloon of the directivity in a format such as GLL or CLF lets prediction software model the box.

## How loudspeakers fail

The handbook lists the failures, and they are the same today.

- **Over-excursion.** At a constant level, the cone excursion needed rises by a factor of four for every octave down,
  so 50 Hz needs four times and 25 Hz sixteen times the excursion of 100 Hz. Below the tuning frequency of a vented
  box, the port no longer loads the driver, and the cone moves freely until it hits its limits. A high-pass filter at
  or just below the tuning frequency prevents this, and it belongs in every processor preset.
- **Heat.** The voice coil turns most of the power into heat, and its resistance rises with temperature, which lowers
  the output as the coil heats up, called power compression. Sustained power beyond the rating burns the coil.
- **Clipping.** A clipping amplifier sends high-frequency energy to the tweeter that the programme did not contain, as
  chapter 13 explains.
- **Feedback, DC and drops.** A sustained feedback tone concentrates power in one band. A fault that puts DC on the
  output pushes the cone to one side and heats the coil. A box that is dropped can shift its voice coil.
- **Intermodulation.** A cone that moves a long way for the bass modulates the midrange it also reproduces, a form of
  Doppler distortion, which is another reason to keep large excursions in separate subwoofers.

Limiters in the processor, set from the driver's ratings, prevent most of these. A defective box usually shows itself
by an impedance curve that differs from its siblings, which chapter 16 covers.

## What changed since 1989

| Handbook | Then | Today |
|---|---|---|
| §13.2 | Electromagnetic and piezoelectric drivers | Piezo dropped; neodymium and AMT drivers added |
| §13.3 | Cone directivity narrows with frequency | Kept, computed table |
| §13.4 | Vented boxes and LF horns | Kept, Thiele-Small and Hofmann's law |
| §13.5, §13.6 | Exponential and constant-directivity horns, compression drivers | Waveguides, asymmetric patterns |
| §13.7 | Passive versus active crossovers, biamping | Active with DSP presets, LR alignment, FIR, self-powered boxes |
| §13.8 | Stacks and clusters, boundary effects | Line arrays, steerable columns, subwoofer arrays; boundaries in chapter 7 |
| §13.9 | Response, power, sensitivity, impedance, directivity | 2.83 V convention, AES2, AES75, directivity data for software |
| §13.10, §13.11 | Over-excursion, IMD, failure causes | Kept, with power compression and processor protection |

## In the SdWa5 rig

Most SdWa5 cabinets are DIY builds of commercial designs, so their weight, dimensions and rigging points can differ
from the original's data sheet. [What drifts between a clone and its original](../../sdwa5-3d/docs/measuring.md#what-drifts-between-a-clone-and-its-original)
lists what to measure first, and the rest of that page describes how a cabinet is measured for the rig's model.

## To verify in pass 2

- The $ka = 1$ and $\lambda = d$ rules for the onset of beaming and the effective diameters used.
- The rule that a horn controls its pattern down to where its mouth is one wavelength.
- Hofmann's iron law and its statement in terms of volume and cut-off cubed.
- The WST criteria (Heil and Urban, *JAES* 2003) and the fill-ratio condition.
- The rear rejection of gradient and end-fire arrays (over 10 dB).
- AES2-2012 test signal and duration; IEC 60268-5 programme simulation noise; AES75.
- GLL (EASE) and CLF (Common Loudspeaker Format) as directivity formats.

## Sources

- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §13 (pp. 209–243).
- Thiele, A. N.: Loudspeakers in vented boxes, *JAES* 19, 1971; Small, R. H.: Vented-box loudspeaker systems,
  *JAES* 21, 1973.
- Heil, C., Urban, M.: Sound fields radiated by multiple sound source arrays, AES convention paper, 1992; Urban, M.,
  Heil, C., Bauman, P.: Wavefront sculpture technology, *JAES* 51, 2003.
- AES2-2012, AES75, IEC 60268-5.
- SdWa5: [Measuring a cabinet](../../sdwa5-3d/docs/measuring.md).
