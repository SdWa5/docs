# 14. Loudspeakers

> **Draft, pass 1.** This chapter was written from general knowledge and checked against reference literature for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers which kinds of box a system is built from, how a loudspeaker turns power into sound, why a box
of a given size has the bass and the directivity it has, which enclosure designs exist, how drivers are combined with
crossovers and amplifiers, how boxes are combined into point-source systems, line arrays and subwoofer arrays, when a
system plays stereo or mono, how a loudspeaker data sheet is read, and how loudspeakers fail.
Amplifiers are in [chapter 13](13-power-amplifiers.md), and filters and crossover alignments in
[chapter 2](02-frequency-phase-time.md).

## Kinds of box

A sound system splits the audio range between boxes that each reproduce one part of it well, because no single driver
reproduces 30 Hz and 15 kHz at a high level.

| Box | Band, roughly | Typical drivers | Use |
|---|---|---|---|
| Subwoofer (sub) | Below 80 to 120 Hz | One or two 15- to 21-inch cones | Deep bass, felt as much as heard |
| Kick bin (kick) | 80 to 200 Hz | 12- or 15-inch cones, often horn-loaded | The punch of the kick drum and the upper bass |
| Top (mid-high) | Above the subwoofers | A 10- to 15-inch cone and a compression driver on a horn | Voices and instruments, everything above the bass |
| Midrange and high boxes | About 200 Hz to 2 kHz, and above | Horn-loaded cones, compression drivers | One box per band in four- and five-way systems |
| Full-range | The whole range down to 50 to 70 Hz | Like a top, in a larger box | Small events without subwoofers, fills, monitors |

A top and a subwoofer form the most common system today, and a crossover at about 80 to 120 Hz divides the work
between them. Systems for dance music often add kick bins between the two, because the cone of a top runs short of
excursion in the upper bass at high levels, and a box made for that band reproduces the kick drum with less distortion.
Many crews who build their own systems take this further and give each band its own box and amplifier channel, from
the subwoofers and kicks to mid horns and high horns.

Boxes are also built for the way they combine. A point-source box is made to cover its angle on its own or in a small
cluster, while a line-array box is made for a column of identical boxes and covers a useful area only as part of one.
[Combining boxes](#combining-boxes) explains both.

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

Piezoelectric tweeters, which were cheap and needed no crossover, are not used in professional systems today.
Neodymium magnets, much stronger per kilogram than ferrite, have cut the weight of drivers by half or more and made
flown arrays practical.

### Phase plugs and compression ratio

The diaphragm of a compression driver is larger than the throat it feeds. Sound from its edge would travel further to
the throat than sound from its centre, and at high frequencies the two would arrive out of phase. If the edge of a
76 mm dome had a path 38 mm longer than its centre, the two would cancel at 4.5 kHz. A phase plug, a solid piece
between the diaphragm and the throat, prevents this. It leaves only narrow slots or rings, which lead from different
zones of the diaphragm to the throat over paths of equal length, so that all parts of the diaphragm arrive together.

The ratio of the diaphragm's area to the area of the openings in the phase plug is the compression ratio, and it gives
the compression driver its name. A higher ratio couples the light diaphragm better to the air and raises the
efficiency. It also raises the pressure in the narrow openings, where air is no longer linear, so a high ratio adds
distortion at high levels. High-frequency drivers commonly use ratios of about 10:1, and horn-loaded cones much lower
ones. This compression has nothing to do with the compressor of chapter 12 or with the power compression described
under [How loudspeakers fail](#how-loudspeakers-fail).

Cone drivers sometimes carry a phase plug too, a fixed bullet in the place of the dust cap. It replaces the dust cap
and its resonances and smooths the upper range of a midrange driver.

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
Exponential horns, whose pattern narrowed with rising frequency, gave way in the 1980s to
constant-directivity horns, which hold a stated coverage over a wide band. Today's waveguides continue
that line. They are shallow horns optimised by simulation for smooth coverage, often with asymmetric patterns that
throw further at the top of the pattern than at the bottom. The two words overlap. A horn in the older sense was built
mainly to load the driver and raise its efficiency, and a waveguide is built mainly to control the coverage, with less
loading. Most high-frequency horns today do both.

A horn whose throat is driven hard adds distortion, because air is not linear at very high pressure. This is part of
why a compression driver sounds harsh when it is pushed close to its limits.

## Enclosures and bass

A cone driver on its own cancels its bass, because the front and the back of the cone radiate in opposite polarity
and the sound from the back wraps around. An enclosure separates the two. Enclosures fall into three families. A
direct radiator lets the cone radiate straight into the air from the front of a box. A bandpass box hides the cone in
chambers and radiates through ports only. A horn-loaded box couples the cone to the air through a horn.

### Direct radiators

- **Sealed box (closed box).** The air in the box acts as a spring, and the response falls by 12 dB per octave below
  the resonance. It is compact and has a good transient response.
- **Vented box (bass reflex).** A port, tuned with the air volume to a frequency near the bottom of the range, adds
  output there and falls by 24 dB per octave below it. It is the most common design for tops and subwoofers. A
  passive radiator, a cone without a motor in the place of the port, works the same way without port noise.

The behaviour of a driver in a box can be predicted from a few measured parameters, the Thiele-Small parameters,
such as the resonance frequency, the moving mass, the compliance and the losses. Box design software uses them.

One law limits every design. For a direct radiator, the efficiency is proportional to the box volume and to the cube of
the lowest frequency, which is often called Hofmann's iron law. To halve the lowest frequency at the same efficiency,
the box needs eight times the volume. In the same box, halving the lowest frequency costs a factor of eight in
efficiency, or 9 dB. A small box with deep bass is possible, but only by giving up level, which is why loudspeakers
for events are large.

### Bandpass

A bandpass box mounts the driver on a wall between two chambers. In the fourth-order design the rear chamber is
sealed and the front chamber radiates through a port, and in the sixth-order design both chambers have ports. The
chambers act as acoustic filters, so the box gives a high output in a band of one to two octaves and falls off on
both sides. Its driver is hidden and protected, which suits boxes that stand on the ground among the audience. Its
ports carry all of the output and need a large area to stay quiet at high levels, and its steep acoustic slopes delay
the bass more than a vented box does.

### Horns

A horn is a duct that widens from a small throat at the driver to a large mouth. It matches the small, heavy
diaphragm to the light air of the open space and raises the efficiency several times compared with a direct
radiator. A horn loads its driver down to about the frequency at which the circumference of its mouth equals one
wavelength, so its lowest frequency sets its size.

| Lowest frequency | Wavelength | Mouth diameter | Mouth area |
|---|---|---|---|
| 125 Hz | 2.74 m | 0.87 m | 0.60 m² |
| 100 Hz | 3.43 m | 1.09 m | 0.94 m² |
| 80 Hz | 4.29 m | 1.36 m | 1.46 m² |
| 63 Hz | 5.44 m | 1.73 m | 2.36 m² |
| 40 Hz | 8.57 m | 2.73 m | 5.85 m² |

The table holds for a horn in free space. On the floor, the mirror source of
[chapter 6](06-sound-outdoors.md#half-quarter-and-eighth-space) halves the area a mouth needs, and in a corner it
quarters it. A horn for the kick range fits into a box, while a full horn for 40 Hz does not. Several horn-loaded
subwoofers side by side form one larger mouth, so on the floor about six boxes with a mouth of 0.5 m² each reach the
area for 40 Hz.

- **Front-loaded horn.** The front of the cone drives the throat, and the back works into a sealed chamber. Kick bins
  and mid-bass boxes are often short front-loaded horns, which give a high efficiency and some directivity in the
  upper bass.
- **Folded horn.** A bass horn is too long to build straight, so its path is folded inside the box. Most horn-loaded
  subwoofers are folded front-loaded horns whose box is only a part of the mouth they need.
- **Tapped horn.** Both sides of the cone feed the same horn, one side at the throat and the other at a point further
  along the path. The back of the cone, whose output a front-loaded horn loses in its chamber, then adds to the
  output over a band of one to two octaves, and the box reaches a high output for its size. Above that band, the two
  paths reach the mouth out of phase at some frequencies, and the response shows deep notches, so a tapped horn needs
  a steep low-pass filter and is used as a subwoofer only. The design was introduced by Tom Danley of Danley Sound
  Labs.

### Designs from the sound-system scene

Crews who build their own systems have used named designs for decades, and the plans circulate between builders. The
W-bin is a folded bass horn, named after the W shape of its path. The scoop is a short horn-loaded bass box, and the
Super Scooper is a larger one. The Paraflex is another named bass box that many crews build, and its principle is on
the verify list. Each of these designs exists in many variants, so this draft leaves their exact geometry, their
origin and their measured behaviour to pass 2 rather than describe them from hearsay. A box built from such a plan is
measured like any other DIY box, as [In the SdWa5 rig](#in-the-sdwa5-rig) describes.

## Crossovers

A crossover splits the signal so that each driver receives only the band it reproduces well.

- **Passive crossovers** sit inside the box, after the amplifier. They are simple to connect but waste power in their
  components, cannot be adjusted, and place the amplifier's output impedance behind a network that weakens its control
  of the bass driver.
- **Active crossovers** split the signal before separate amplifier channels. Their advantages
  are more headroom because each amplifier handles only one band, efficiency, better damping, and lower
  intermodulation because a clipping bass channel does not distort the high frequencies.

A digital processor or an amplifier with DSP now provides the crossover along with delay to align the drivers in
time, equalization for each way and limiters for each driver, as chapter 12 describes. A Linkwitz–Riley alignment,
with two filters of the same order that sum flat in level and in phase, is the usual choice, and chapter 2 explains
it. FIR filters can build crossovers with linear phase, at the cost of latency. Loudspeaker manufacturers supply
presets that contain all of this for their boxes, and a box run without its preset sounds and behaves differently from
its data sheet.

## Active and passive, ways and channels

Active and passive describe two different things, which causes confusion. A box is called active when it contains its
own amplifier, and a system is called active when its crossover sits before the amplifiers, so that each way has its
own amplifier channel. All four combinations exist.

| Amplifier | Crossover | Usual name | Connection |
|---|---|---|---|
| Outside the box | Passive, in the box | Passive box | One amplifier channel per box, over a loudspeaker cable |
| Outside the box | Active, in a processor | Passive box run bi-amped or tri-amped | One amplifier channel per way, over a multi-pole cable such as speakON NL4 or NL8 |
| Inside the box | Active, in its DSP | Active or self-powered box | A line-level signal and mains power to every box |
| Inside the box | Passive, in the box | Powered box | As above, but one amplifier drives a passive crossover, common in low-cost boxes |

A passive box keeps the amplifiers together in one place, out of the weather, and needs only loudspeaker cables to the
boxes. A self-powered box needs mains power at every box, but its amplifier and its processing are matched to its
drivers by the manufacturer. [Chapter 15](15-cables-connectors-networks.md) gives the speakON pin convention for
bi-amped boxes and its exceptions.

A way is a frequency band with its own drivers. A box with a 15-inch cone and a compression driver is a two-way box,
and a system of such tops with subwoofers is a three-way system. A channel is a separate signal path, either an output
of the mixer such as left and right, or an input of an amplifier. In an active system the ways and the channels
multiply. A stereo three-way system with bi-amped tops needs at least six processor outputs and amplifier channels,
and the same system with passive tops needs four, one for each top and one for each side's subwoofers. With the
subwoofers on one mono signal, as [Stereo and mono](#stereo-and-mono) recommends, the passive version needs three.

## Combining boxes

### Point-source systems and clusters

A single box or a small cluster of boxes, each covering its own angle, acts as a point source and loses 6 dB per
doubling of distance, as chapter 6 explains. Where the coverage of two boxes overlaps, they interfere and produce a
comb filter, so a well-built cluster splays its boxes so that their patterns meet at about their −6 dB points. A
common estimate for clusters, between 3 and 6 dB more level per doubling of the number of boxes, assumes some
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

Subwoofers placed left and right of the stage, as most systems were built for decades, produce a comb filter across the
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

## Stereo and mono

A stereo system plays a left and a right channel from two loudspeaker positions. A listener hears a stereo image
between them only while the two arrive within about 1 ms of each other, as
[chapter 5](05-hearing.md#localisation-and-the-precedence-effect) explains. Further off the centre line, the nearer
side arrives first, and the sound comes from there.

| Listener off the centre line (mains 10 m apart, listener at 30 m) | Path difference | Time difference |
|---|---|---|
| 0.5 m | 0.16 m | 0.48 ms |
| 1 m | 0.33 m | 0.96 ms |
| 2 m | 0.66 m | 1.91 ms |
| 5 m | 1.62 m | 4.73 ms |
| 10 m | 3.13 m | 9.12 ms |

At 30 m, only a strip about 2 m wide around the centre line hears the image, and everyone else hears mostly one side.
A source panned hard to one side is quiet or missing for the listeners on the other side. Live mixes therefore keep
the vocals and the bass in the centre, as [chapter 11](11-mixing-consoles.md) notes, and use the sides for effects
and width.

Many event systems play mono, the same signal from every loudspeaker. Everyone then hears the whole mix, and the
stacks can stand wherever the coverage needs them. Music mixed in stereo, such as most recorded music a DJ plays, is
summed to mono for such a system. Anything that is out of phase between the two channels, such as some stereo
widening effects, cancels in the sum, so a mono system is checked with the music it will play. The subwoofers run
mono in almost every system, stereo or not, because the ear hardly localises deep bass, and
[Left and right or centre](#left-and-right-or-centre) shows what their placement does.

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

The ways loudspeakers fail have not changed in decades.

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

## In the SdWa5 rig

Most SdWa5 cabinets are DIY builds of commercial designs, so their weight, dimensions and rigging points can differ
from the original's data sheet. [What drifts between a clone and its
original](../../sdwa5-3d/docs/measuring.md#what-drifts-between-a-clone-and-its-original) lists what to measure
first, and the rest of that page describes how a cabinet is measured for the rig's model.

## To verify in pass 2

- The $ka = 1$ and $\lambda = d$ rules for the onset of beaming and the effective diameters used.
- The rule that a horn controls its pattern down to where its mouth is one wavelength.
- Hofmann's iron law and its statement in terms of volume and cut-off cubed.
- The WST criteria (Heil and Urban, *JAES* 2003) and the fill-ratio condition.
- The rear rejection of gradient and end-fire arrays (over 10 dB).
- AES2-2012 test signal and duration; IEC 60268-5 programme simulation noise; AES75.
- GLL (EASE) and CLF (Common Loudspeaker Format) as directivity formats.
- The bands of subwoofers, kick bins and tops, and the usual crossover of 80 to 120 Hz between subwoofers and tops.
- Compression ratios of about 10:1 for high-frequency drivers and lower ones for horn-loaded cones; the purpose of
  phase plugs in cone drivers.
- The horn loading rule (mouth circumference of one wavelength) and the efficiency gain of horns over direct
  radiators.
- The bandwidth of bandpass boxes (one to two octaves) and their delay compared with a vented box.
- The principle, bandwidth and output per volume of the tapped horn; Tom Danley and Danley Sound Labs as its origin,
  with the patent.
- The geometry, principle, origin, variants and measured behaviour of the W-bin, the scoop, the Super Scooper and
  the Paraflex, from the plans that crews build.
- The four combinations of amplifier and crossover placement, and the name powered box for the fourth.
- The 1 ms window for a stereo image, from the sources of chapter 5.
- Keele 1977 (preprint number) and Kolbrek and Dunker 2019 (publisher, edition).

## Sources

- Thiele, A. N.: Loudspeakers in vented boxes, *JAES* 19, 1971; Small, R. H.: Vented-box loudspeaker systems,
  *JAES* 21, 1973.
- Heil, C., Urban, M.: Sound fields radiated by multiple sound source arrays, AES convention paper, 1992; Urban, M.,
  Heil, C., Bauman, P.: Wavefront sculpture technology, *JAES* 51, 2003.
- Keele, D. B.: Low-frequency horn design using Thiele/Small driver parameters, AES preprint 1250, 1977.
- Kolbrek, B., Dunker, T.: *High-Quality Horn Loudspeaker Systems*, Kolbrek Elektroakustikk, 2019.
- AES2-2012, AES75, IEC 60268-5.
- SdWa5: [Measuring a cabinet](../../sdwa5-3d/docs/measuring.md).
- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §13 (pp. 209–243).
