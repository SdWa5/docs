# 9. Microphones, instruments and other sources

> **Draft, pass 1.** This chapter was written from general knowledge and checked against reference literature for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter covers everything that feeds a signal into the mixer. It starts with the kinds of source and what each
needs at its input. It then explains how a microphone turns sound into a signal, how its pattern, sensitivity and
noise are read from its data sheet and how it is powered and connected. The second half brings in the sources that
need no microphone, which are instruments with pickups, drum machines, synthesizers, turntables, DJ mixers and
laptops, through DI boxes and line inputs, and sets their gain. Wireless microphones are in
[chapter 10](10-wireless.md), gain before feedback is in
[chapter 6](06-sound-outdoors.md#feedback-and-gain-before-feedback), and MIDI clock and sync between instruments are
in [chapter 19](19-control-and-sync.md).

## Kinds of source

A source is anything that delivers a signal to the mixer. Four kinds differ in level, impedance and connector, and
each needs a different input.

| Kind | Examples | Output | Input it needs |
|---|---|---|---|
| Transducers | Microphones, guitar and bass pickups, contact pickups | Microphone level of about −60 to −40 dBu, or a high-impedance pickup signal | Microphone preamplifier, or a DI box for a pickup |
| Electronic instruments | Drum machines, grooveboxes, synthesizers, samplers, step sequencers with sound | Line level, mostly unbalanced on jack sockets, often stereo | Line input close by, or a DI box for a long run |
| Players | Turntables, media players, laptops | Phono level of a few millivolts, or line level, or USB | Phono stage for a turntable, line input or audio interface for the rest |
| Sub-mixers | DJ mixers, DJ controllers, a performer's small mixer | Line level, balanced master output or unbalanced RCA | Line input, or a DI box for a long run |

On many electronic music events the microphone is the exception and the second half of this chapter covers most of
the inputs. The microphone sections come first because the preamplifier, phantom power and balanced connection they
explain apply to every other source as well.

## How microphones work

Every microphone has a diaphragm that moves with the sound pressure, and a transducer that turns that motion into a
voltage. The transducer decides most of the microphone's character.

- **Dynamic (moving coil).** A coil attached to the diaphragm moves in a magnetic field and generates a voltage. It
  needs no power, handles very high levels and survives rough treatment, which makes it the standard for vocals on
  loud stages and for drums and guitar amplifiers. Its heavier diaphragm responds less to the highest frequencies and
  fast transients than a condenser.
- **Condenser.** The diaphragm forms one plate of a capacitor, and its motion changes the capacitance against a fixed
  back plate. The element needs a polarising voltage and an impedance converter, both powered through the cable. Its
  light diaphragm gives extended high-frequency response and a detailed transient response, and its higher output
  makes it quieter in use. Condensers are the choice for overheads, acoustic instruments, choirs and speech at a
  distance.
- **Electret.** A condenser whose polarisation is stored permanently in a charged layer, so it needs power only for
  its impedance converter. Almost all lavalier and headset microphones, and many measurement microphones, are
  electrets.
- **Ribbon.** A thin metal ribbon moves in a magnetic field. Its natural pattern is a figure-of-eight, its sound is
  smooth and its output low. Classic passive ribbons are fragile, and a wiring fault that puts phantom power across
  the ribbon can damage it. Active ribbons with built-in amplifiers need phantom power and give a normal output.
- **Piezoelectric.** A crystal or ceramic element produces a voltage when it is bent. It survives today in contact
  pickups on acoustic guitars, violins and drums, with a very high source impedance that needs a suitable input.

The carbon microphone of early telephones has no place in sound reinforcement.

## Forms and uses

| Form | Typical use | Notes |
|---|---|---|
| Handheld | Vocals, speech | Built-in pop protection and handling-noise isolation |
| Stand or clip | Instruments, choirs, lecterns | Shock mount and windscreen as needed |
| Lavalier | Speech, theatre | Omni electret, placed on the chest, with a presence lift to make up for the off-axis position |
| Headset | Speech, singing actors, presenters | Capsule at the mouth corner, the strongest feedback measure for a moving talker |
| Boundary | Lecterns, conference tables, stage floors | Capsule close to a surface, so the direct and reflected sound arrive together without a comb filter |
| Shotgun | Film, distant pickup | Directional only at high frequencies, little use on a live stage |
| Contact pickup | Acoustic instruments | Feedback-resistant, sound differs from an air microphone |
| Ceiling array | Conference rooms, hybrid events | Many capsules with beamforming that follows the active talker |

A lecturer who moves around a lectern microphone changes the level by many decibels with every step, because the
inverse square law is steep close to the microphone. A lavalier keeps the distance constant for such a speaker, and a
headset is better still where the gain before feedback is short.

## Pickup patterns

Most microphones have a first-order pattern, a mix of a pressure element, which responds equally in all directions,
and a pressure gradient element, which responds as the cosine of the angle. The sensitivity at angle θ is

$$S(\theta) = A + B \cos\theta, \quad A + B = 1$$

| Pattern | A | Null angle | At 90° | At 180° | Directivity index | Distance factor |
|---|---|---|---|---|---|---|
| Omnidirectional | 1 | none | 0 dB | 0 dB | 0 dB | 1.0 |
| Subcardioid | 0.7 | none | −3.1 dB | −8.0 dB | 2.8 dB | 1.4 |
| Cardioid | 0.5 | 180° | −6.0 dB | null | 4.8 dB | 1.7 |
| Supercardioid | 0.37 | 125° | −8.7 dB | −11.4 dB | 5.7 dB | 1.9 |
| Hypercardioid | 0.25 | 110° | −12.0 dB | −6.0 dB | 6.0 dB | 2.0 |
| Figure-of-eight | 0 | 90° | null | 0 dB | 4.8 dB | 1.7 |

The directivity index says how much less of a diffuse sound field, such as reverberation or the sound of a crowd, the
microphone picks up than an omnidirectional one. The distance factor says how much further away a directional
microphone can be placed for the same ratio of direct to diffuse sound. A hypercardioid at 0.2 m picks up as much room
sound as an omnidirectional microphone at 0.1 m.

The null angle decides where a monitor wedge belongs. A cardioid rejects most at the back, so its wedge sits
directly behind it, in front of the performer. A supercardioid or hypercardioid rejects most at 110° to 125° and has
a rear lobe, so its wedges belong at about 55° to 70° on either side of the line behind the microphone, which
usually means two wedges, one on each side. Placing a wedge for a hypercardioid where a cardioid's would go puts it
into the rear lobe.

Real microphones follow these patterns only in the midrange. At low frequencies most directional microphones become
less directional, and at high frequencies the size of the capsule narrows the pattern. A pattern graph at several
frequencies in the data sheet, or a polar plot at 125 Hz, 1 kHz and 8 kHz, shows how far the microphone keeps its
pattern. For feedback, a microphone with smooth off-axis response gains more than
one whose pattern is sharper on paper but has peaks off axis.

## Frequency response and proximity effect

A vocal microphone usually has a presence peak of a few decibels between 3 and 8 kHz and a roll-off below about
100 Hz. Both are intended. The peak helps the voice cut through, and the roll-off compensates for the proximity effect.
A measurement microphone is flat instead, and chapter 16 covers it.

A directional microphone close to a source picks up more bass. The pressure gradient at low frequencies is larger near
a point source, because the curvature of the wavefront adds to it. For an ideal cardioid, the boost relative to the
far field follows from $|1 + 1/(2jkr)|$, with $k = 2\pi f / c$.

| Distance | 50 Hz | 100 Hz | 200 Hz | 500 Hz |
|---|---|---|---|---|
| 2 cm | +28.7 dB | +22.7 dB | +16.8 dB | +9.3 dB |
| 5 cm | +20.8 dB | +14.9 dB | +9.3 dB | +3.4 dB |
| 10 cm | +14.9 dB | +9.3 dB | +4.6 dB | +1.1 dB |
| 30 cm | +6.3 dB | +2.6 dB | +0.8 dB | +0.1 dB |
| 1 m | +1.1 dB | +0.3 dB | +0.1 dB | 0 dB |

These are values for an ideal point source and an ideal capsule, and a real vocal microphone is designed with a
rising bass roll-off that takes back much of it at a typical singing distance. Figures of up to 16 dB are commonly
quoted. An omnidirectional microphone has no proximity effect, which is one reason lavaliers and headsets are
omnis. A singer who uses the proximity effect deliberately gains warmth, and a public speaker who leans in by
accident loses intelligibility. A high-pass filter in the channel, set by ear between 80 and 150 Hz, is the remedy.

Peaks in the frequency response matter for a further reason. A peak in the response of any element in
the loop is where feedback starts first, which is why a microphone with a smooth response gains more than one with a
peaky response and the same pattern.

## Sensitivity, noise and maximum level

### Sensitivity

Sensitivity is the output voltage for 1 Pa, which is 94 dB SPL, given in mV/Pa or in dBV re 1 V/Pa.

| Sensitivity | dBV re 1 V/Pa | At 94 dB SPL | At 120 dB SPL | At 135 dB SPL |
|---|---|---|---|---|
| 1.5 mV/Pa (dynamic vocal) | −56.5 | −54.3 dBu | −28.3 dBu | −13.3 dBu |
| 2 mV/Pa | −54.0 | −51.8 dBu | −25.8 dBu | −10.8 dBu |
| 5 mV/Pa | −46.0 | −43.8 dBu | −17.8 dBu | −2.8 dBu |
| 10 mV/Pa (lavalier) | −40.0 | −37.8 dBu | −11.8 dBu | +3.2 dBu |
| 20 mV/Pa (studio condenser) | −34.0 | −31.8 dBu | −5.8 dBu | +9.2 dBu |

The preamplifier must take the whole range, from a quiet voice on a dynamic microphone at around −60 dBu to a
condenser on a kick drum at over +5 dBu. A condenser at 135 dB SPL delivers a level that overloads many microphone
inputs at their lowest gain, which is why distortion with close miking usually comes from the preamplifier, not
the microphone. A pad in the microphone or at the input solves it.

### Self-noise and the noise of a dynamic microphone

A condenser's self-noise is given as an equivalent sound level, such as 13 dB(A), the level of a sound that would give
the same output as the microphone's own noise. Below about 15 dB(A) is quiet, and above 25 dB(A) is audible on quiet
sources.

A dynamic microphone has almost no self-noise beyond the thermal noise of its coil, but its low output brings the
preamplifier's noise into play. With 1.5 mV/Pa and a preamplifier with an EIN of −128 dBu, the signal at 94 dB SPL is
73.7 dB above the noise, which is equivalent to a microphone with a self-noise of about 20 dB. A condenser with
20 mV/Pa into the same preamplifier is limited by its own self-noise instead. For speech at a distance, a condenser
is quieter. For a vocal at 5 cm, both are far above any noise.

### Maximum level

Maximum SPL is the level at which a condenser's distortion reaches a stated value, usually 0.5 % or 1 % THD. It is
limited by the impedance converter, not the capsule, so a pad switch in the microphone raises it. A dynamic
microphone has no practical limit on a stage.

## Phantom power and connection

### Phantom power

Condenser microphones, active ribbons and active DI boxes are powered through the microphone cable. The same voltage
is applied to both signal wires through matched resistors, and the current returns through the shield. The audio
signal between the wires is unaffected, and a balanced dynamic microphone sees no voltage across its coil.

IEC 61938 defines three variants.

| Variant | Voltage | Feed resistors | Current at most |
|---|---|---|---|
| P48 | 48 V | 6.81 kΩ per wire | about 10 mA |
| P24 | 24 V | 1.2 kΩ per wire | about 10 mA |
| P12 | 12 V | 680 Ω per wire | about 15 mA |

P48 is standard on mixing consoles and stageboxes. With its high feed resistors, the power available is small. A
short circuit draws 14 mA, and the most a device can draw is about 169 mW, at 24 V and 7 mA. A microphone or DI box
that needs more current than its supply provides loses headroom without warning, which is a common fault on cheap
interfaces and battery recorders.

Phantom power is safe for balanced dynamic microphones and active ribbons. It is a risk for a passive ribbon if a
cable or adapter has a fault, for an unbalanced source connected through an adapter, and for any device when
connections are made with the power on, because the switching surge reaches the output of the device and the input of
the preamplifier. Phantom power is switched on after the connection and off before it is broken, with the channel
muted.

### Balanced connection

A professional microphone has a low source impedance of 150 to 300 Ω and a balanced output on an XLR connector. The
input it feeds has a load impedance of 1 to 3 kΩ, at least five to ten times the source impedance, so that the voltage
arrives almost unchanged. Balanced means that both wires have the same impedance to ground, so noise induced along the
cable is equal on both and cancelled by the differential input. The input's common-mode rejection ratio (CMRR) says
how well it does this. Chapter 15 covers cables and connectors.

### Accessories

Wind noise is turbulence at the microphone, not sound, and it overloads the low frequencies. A foam windscreen helps
indoors and in a light breeze, and a basket with a fur cover helps outdoors. A pop filter or the grille of a vocal
microphone stops the blasts of plosives such as p and b. A shock mount isolates the microphone from the vibration of
its stand, which a stage floor or a kick drum passes into it. The high-pass filter in the channel removes what is
left below the instrument's range.

### Digital microphones

AES42 defines a microphone with its own converter and a digital AES3 output, powered with 10 V over the cable, and
with remote control of gain and pattern. Such microphones avoid the analog cable and the preamplifier entirely, but
they need inputs that support the standard and remain rare on live stages. Network microphones that connect over an
audio network such as Dante are another variant, mostly in conference systems.

## DI boxes and instrument inputs

A DI (direct injection) box takes the output of an instrument, an amplifier or a playback device and turns it into a
balanced, low-impedance signal at microphone level, so that it can run on the same multicore and into the same
preamplifiers as the microphones.

### Why they are needed

An electric guitar or bass pickup has a source impedance of many kilohms, rising steeply with frequency through its
inductance. It needs a load of about 1 MΩ, and a lower load dulls its tone. An unbalanced output also picks up hum on
a long cable. A DI box provides the high input impedance, a balanced output and a ground separation.

### Passive and active

- **Passive DI** uses a transformer with a turns ratio of typically 10 to 12 to 1, which lowers the voltage by 20 to
  21.6 dB and the impedance by 100 to 144 times. It needs no power, isolates galvanically, and handles high levels well.
  Its input impedance is lower than that of an active DI, which suits line sources, keyboards and active basses better
  than passive pickups.
- **Active DI** uses an amplifier with an input impedance of 1 MΩ or more, powered by phantom power or a battery. It
  suits passive pickups, and its output level is set for a microphone input.

A ground lift switch separates the shield of the output from that of the input. It interrupts a ground loop between
the stage equipment and the console, which chapter 17 discusses. A pad of 20 to 40 dB is needed for line-level and
loudspeaker-level sources, and some DI boxes take the loudspeaker output of an instrument amplifier directly.

### Stereo and playback

Laptops, playback devices and keyboards usually feed a stereo DI with two channels. The ground loop between a laptop
on mains power and the console is the most common source of hum on a stage today, and a transformer DI or a ground
lift removes it.

### Preamplifiers in the console

The microphone preamplifier in the console or stagebox raises signals from around −60 dBu to line level or to the
converter's working level, which can need up to about 70 dB of gain. Chapter 4 covers gain structure and chapter 11
the console.

## Electronic instruments

Drum machines, grooveboxes, synthesizers and samplers produce their signal electronically, so they need no
microphone. Their outputs are line outputs, but they differ from the balanced +4 dBu outputs of professional
equipment in several ways that decide how they are connected.

- **Unbalanced jacks.** Most outputs are unbalanced 6.35 mm TS jacks, some are TRS jacks that are balanced or
  impedance-balanced. An unbalanced output picks up hum on a long cable and forms a ground loop with the console,
  so it runs a few metres at most to a line input or into a DI box next to the instrument.
- **Level.** The nominal level lies anywhere between the consumer −10 dBV and the professional +4 dBu, and few
  manuals state the clip point. The level is checked at the console, as chapter 3 describes for consumer and DJ
  equipment.
- **Volume control.** The master volume of the instrument sits in front of its output. It is set high and left
  there, so that the output stage works well above its noise, and the gain is set at the console. A volume that is
  turned up and down during a set moves the whole gain structure with it.
- **Main and individual outputs.** Many drum machines and grooveboxes have a stereo main output and some individual
  outputs, which take single parts such as the kick drum out of the main mix. Separate channels for the kick and the
  bass let the console treat them on their own, at the cost of more inputs and more cables to check.
- **Headphone output.** The headphone output is a power output for a low-impedance load, with its own volume and
  often its own noise. It is not used as a feed, except as an emergency when the main output has failed.
- **Mono and stereo.** Some synthesizers have a single output, which goes to a mono channel or to both sides of a
  stereo channel. A stereo instrument feeds a stereo channel pair. The subwoofers usually receive a mono sum, and
  stereo effects that put the bass out of phase between the two sides cancel in that sum. A check with the channel
  pair switched to mono shows it before the event.

Several instruments of one live act are often combined on a small mixer at the performer, which then sends one stereo
mix to the console. That gives the performer control over the balance but adds a gain stage and a ground point, and
[chapter 11](11-mixing-consoles.md#sub-mixers-feeds-and-cascades) covers sub-mixers. Tempo sync between the
instruments runs over MIDI clock or a sync signal and is covered in [chapter 19](19-control-and-sync.md).

## Turntables and phono

A turntable with a moving-magnet cartridge delivers a few millivolts, and the record is cut with the RIAA
equalization, which reduces the bass and raises the treble. The phono stage amplifies the signal and applies the
inverse curve. Relative to 1 kHz it raises 20 Hz by 19.3 dB and lowers 20 kHz by 19.6 dB.

| Frequency | 20 Hz | 50 Hz | 100 Hz | 1 kHz | 10 kHz | 20 kHz |
|---|---|---|---|---|---|---|
| RIAA playback curve | +19.3 dB | +16.9 dB | +13.1 dB | 0 dB | −13.7 dB | −19.6 dB |

At 5 mV, which is −43.8 dBu, the phono stage needs about 36 dB of gain at 1 kHz to reach −10 dBV and about
48 dB to reach +4 dBu. DJ mixers have phono stages built in, and a turntable is never connected to a line input,
where it would sound thin and far too quiet.

- **Ground wire.** The turntable's ground wire connects the tonearm and chassis to the ground terminal of the DJ
  mixer. Without it, a hum appears that the console cannot remove.
- **Acoustic feedback.** The stylus picks up the vibration of the table it stands on. Low frequencies from the
  subwoofers reach the platter and the tonearm through the floor and the air, are amplified and played back, and
  build up into a low-frequency howl. The turntables stand on a heavy, stable surface that is decoupled from a stage
  floor, as far from the subwoofers as the layout allows, and a cardioid subwoofer arrangement
  ([chapter 14](14-loudspeakers.md#cardioid-arrays)) reduces the level behind it. A high-pass filter in the phono
  channel removes rumble below the music.
- **Line-level players.** CD players, media players and digital vinyl systems have line outputs and need no phono
  stage. A digital vinyl system reads a timecode record through the phono stage of its interface.

## DJ mixers and controllers

A DJ mixer is a sub-mixer with phono stages, and it reaches the system through its outputs.

- **Master output.** The balanced XLR master output feeds the console or the system processor. The unbalanced RCA
  master output is used only on short cables. The master level is set so that the DJ mixer's meter stays below its
  red range, and the system's gain follows from that. A limiter on the master output, where the mixer has one,
  protects the system from a DJ who turns everything up, but the system's own limiters remain the protection
  (chapter 13).
- **Booth output.** The booth output feeds the DJ's monitor with its own level control, independent of the master.
  [Chapter 18](18-stage-monitoring.md) covers monitors.
- **Record output.** A separate record or session output takes a recording or stream feed without touching the
  master.

A DJ controller combines the control surface with an audio interface and works with software on a laptop. Its
outputs are often unbalanced RCA or TRS, and its power often comes over USB from the laptop. The ground loop through
the laptop's charger then reaches the controller's outputs as well, which the next section explains.

## Laptops and USB audio

A laptop plays back through an audio interface, which may be built into a DJ controller or be a separate box. The
laptop's own headphone socket is noisy, unbalanced and shares its ground with the charger, so it is avoided.

- **Buffer and latency.** The software hands audio to the interface in blocks. Each block adds its length in time,
  and a larger buffer is safer against dropouts but adds latency.

  | Buffer | 64 samples | 128 samples | 256 samples | 512 samples |
  |---|---|---|---|---|
  | At 48 kHz | 1.33 ms | 2.67 ms | 5.33 ms | 10.67 ms |
  | At 44.1 kHz | 1.45 ms | 2.90 ms | 5.80 ms | 11.61 ms |

  Pure playback tolerates a large buffer. A performer who plays instruments through the laptop needs a small one,
  and the round trip from key to sound is at least twice the buffer plus the converters.
- **Sample rate.** The software, the interface and any digital connection to the console run at the same sample
  rate, or the computer resamples and some combinations drop out.
- **Settings.** Power saving, sleep, notifications, automatic updates, Wi-Fi and Bluetooth are switched off for the
  show, and the laptop runs on its charger.
- **Hum.** The charger connects the laptop to the mains, and its ground meets the console's ground through the
  audio cable. The hum that results is the most common hum on a stage today. A DI box with a transformer or a ground
  lift, or a USB isolator, breaks the loop. The protective earth of the charger or the console is never disconnected
  ([chapter 17](17-power-grounding-safety.md)).

## Gain into the mixer

Every source ends at a channel whose gain is set as [chapter 4](04-dynamic-range-gain-structure.md) describes. The
connection decides how much gain that channel needs.

| Source and connection | Level at the channel input | Gain to the nominal +4 dBu |
|---|---|---|
| Professional line output, balanced | +4 dBu | 0 dB |
| Consumer line output, −10 dBV, short cable to a line input | −7.8 dBu | 11.8 dB |
| Consumer line output through a passive DI with 20 dB loss | −27.8 dBu | 31.8 dB |
| Turntable without phono stage, 5 mV | −43.8 dBu | not usable, the RIAA curve is missing |

A line source through a DI box arrives at the microphone preamplifier with a gain need similar to a loud
microphone, which suits it well. A hot line output that clips the preamplifier even at its lowest gain needs the pad
of the DI box or of the channel. The input list of an event names each source with its connection, so that the
channels can be prepared before the performers arrive.

## To verify in pass 2

- The coefficients of the supercardioid (0.37) and hypercardioid (0.25) and their null angles; check textbook
  definitions (Eargle, *The Microphone Book*).
- The proximity effect model $|1 + 1/(2jkr)|$ for an ideal cardioid, and typical real values.
- Typical self-noise categories (below 15 dB(A) quiet, above 25 dB(A) audible).
- IEC 61938 phantom power values, tolerances and maximum currents for P48, P24 and P12.
- AES42 powering (10 V) and features.
- Typical turns ratios and input impedances of passive DI boxes.
- The 1 MΩ load for passive pickups.
- The maximum preamplifier gain of about 70 dB in current stageboxes.
- Output levels of moving-magnet cartridges, including DJ cartridges, and the usual phono input load of 47 kΩ.
- The RIAA time constants (3180 µs, 318 µs, 75 µs) and the optional IEC amendment below 20 Hz.
- Typical nominal and maximum output levels of drum machines, grooveboxes and DJ mixer master outputs.
- Interface round-trip latency figures beyond the buffer, for common USB audio interfaces.

## Sources

- Eargle, J.: *The Microphone Book*, Focal Press.
- IEC 61938, guidance on interconnections and matching values, including phantom power.
- AES42, digital interface for microphones.
- IEC 60098, analogue audio disk records and reproducing equipment (RIAA curve).
- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §10.1 to §10.4
  (pp. 113–131) and §11.2 (pp. 152–154).
