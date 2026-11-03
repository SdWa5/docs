# 15. Cables, connectors and networks

> **Draft, pass 1.** This chapter was written from general knowledge and checked against the 1989 handbook for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers which cables and connectors carry analog signals, loudspeaker power and mains power on a sound
system, how thick a loudspeaker cable must be, and how digital audio travels over dedicated links and over networks.
It replaces handbook §15 (pp. 281–302), §17.3 (pp. 325–327) and §18.4 (pp. 355–358). Grounding and hum are in
chapter 17, and the levels the cables carry in [chapter 3](03-decibels-levels-loudness.md).

The handbook opens with the observation that most failures of a sound system are failures of a cable or a
connector. That has not changed, and the cheapest reliability measure on a stage is still a spare for every cable
type and a cable tester.

## Analog signal cables

### Shielding

Microphone and line signals are small and will be amplified, so any interference that enters the cable is amplified
with them. A shield around the conductors intercepts electric fields and drains them to ground. Three kinds are
common.

- **Braided shields** cover 85 % to 95 % of the conductors, are robust and are the usual choice for cables that are
  plugged and coiled every day.
- **Spiral (served) shields** are more flexible, but the spiral opens when the cable is bent, which lowers the coverage
  and can make the cable microphonic, so that handling it produces noise.
- **Foil shields** cover fully and are thin, but they break under repeated flexing, and they suit fixed installation.

A shield does little against magnetic fields from transformers, dimmers and mains cables. The defence against those
is a twisted pair, because the field induces opposite voltages in successive twists, and a star-quad cable, with two
pairs twisted together and the opposite conductors connected, rejects magnetic hum further. Keeping signal cables
away from mains and dimmer cables, and crossing them at a right angle where they must meet, still helps.

### Capacitance

Every cable has capacitance between its conductors and the shield, typically around 100 pF per metre for
microphone cable. Together with the output impedance of the source it forms a low-pass filter.

| Source | Cable | Upper limit (−3 dB) |
|---|---|---|
| Line output, 100 Ω | 100 m at 100 pF/m | 159 kHz |
| Old transformer output, 600 Ω | 100 m at 100 pF/m | 27 kHz |
| Source of 10 kΩ | 100 m at 100 pF/m | 1.6 kHz |
| Passive pickup, about 47 kΩ | 5 m at 100 pF/m | 6.8 kHz |

A modern low-impedance output drives a long cable without loss. A high-impedance source, such as a passive guitar
pickup, loses treble already on a few metres, which is why such instruments go into a DI box close to the source, as
chapter 9 explains. The pickup's own inductance makes the real behaviour a resonance rather than a plain roll-off,
but the conclusion is the same.

### Balanced and unbalanced

An **unbalanced** connection carries the signal on one conductor and returns it through the shield. Any voltage
between the grounds of the two devices, and any interference on the shield, adds to the signal. Unbalanced
connections suit short runs between devices on the same power outlet, which is the domain of consumer equipment at
−10 dBV.

A **balanced** connection carries the signal on a twisted pair, with the shield separate. The receiving input amplifies
only the difference between the two conductors, so interference that reaches both equally cancels. What matters is
that both conductors have the same impedance to ground at the source and at the input, not that both carry a mirror
image of the signal. An output that drives only one conductor and holds the other at ground through the same
impedance is balanced in this sense. Professional line and microphone connections are balanced, and they work over
hundreds of metres.

Modern equipment uses voltage bridging, with an output impedance of 50 Ω to 200 Ω and an input impedance of
10 kΩ or more. The 600 Ω matching of the telephone era, which the handbook still discusses, is needed only for
old transformer equipment and long telephone lines. Connecting a +4 dBu output to a −10 dBV input, or the reverse,
gives an 11.8 dB level mismatch, as chapter 3 computes. Interface boxes, or the trim of the receiving input, correct
it, and an unbalanced output into a balanced input needs the cold conductor tied to ground at the source end.

### Multicores and stage boxes

A multicore (snake) carries many balanced pairs from the stage to the console, each pair individually shielded, and
ends in a stage box with XLR connectors. On most systems today the stage box is digital, with the microphone
preamplifiers on the stage and a single network or fibre cable to the console, as chapter 11 describes. Analog
multicores remain in use on small systems and as a backup.

### Strain relief and care

The handbook's advice on strain relief still holds. The cable clamp of the connector must hold the jacket, so that a
pull never reaches the solder joints. Cables are coiled over-under so that they lie flat and do not twist, and a cable
that crackles when it is moved is replaced rather than repaired on the night.

## Connectors

| Connector | Use | Notes |
|---|---|---|
| XLR-3 | Microphone, line, AES3 | Locks; pin 1 shield, pin 2 hot, pin 3 cold |
| XLR-5 | DMX512 lighting control, stereo intercom | Not for audio between unknown devices |
| 6.35 mm TRS (jack) | Balanced line, insert points, headphones | Tip hot, ring cold, sleeve shield |
| 6.35 mm TS | Unbalanced instrument and line | Shorts briefly when plugged |
| 3.5 mm TRS | Consumer stereo, laptops, phones | Unbalanced stereo |
| RCA (phono) | Consumer line, S/PDIF | Unbalanced, no lock |
| speakON NL2, NL4, NL8 | Loudspeaker power | Locks; 2, 4 or 8 poles for one to four ways |
| powerCON, powerCON TRUE1 | Mains to devices | Locks; TRUE1 may be plugged under load |
| etherCON | Ethernet in rugged housing | Locks over a standard RJ45 plug |
| CEE (IEC 60309) | Mains distribution | Blue 230 V, red 400 V three-phase; 16 A, 32 A, 63 A |
| Optical (opticalCON, LC, ST) | Fibre links | Clean caps on every unused end |

The XLR connector has been the standard for professional audio since before 1989. It locks, and pin 1 makes contact
first, so the grounds connect before the signal does. The polarity of pin 2 and pin 3 was not uniform in 1989, and
some American equipment used pin 3 as hot. Pin 2 hot has since been standardized internationally, and equipment
built to the older convention is now rare, but a polarity tester (chapter 16) settles any doubt.

The jack plug lacks a lock, and its tip and ring touch the sleeve contact while it is inserted, which can cause loud
bangs and short an amplifier output. The handbook already warned against jack plugs on loudspeaker cables, and
speakON has since replaced them. A speakON NL4 cable carries pins 1+ and 1− for a single box, and pins 2+ and 2−
for the second way of a biamped box or for a second box. The convention for which pins carry which way varies
between manufacturers, so the pinout of an NL4 or NL8 cable is checked against the box before use.

### The pin-1 problem

A device that connects the cable shield (pin 1) to its internal signal ground, rather than directly to the chassis
where the cable enters, lets current on the shield flow through its signal circuits. This produces hum and buzz that
no balanced input can reject, because it is created inside the device. The effect was described in 1995 and is the
subject of AES48, which requires the shield to be bonded to the chassis at the connector. Chapter 17 explains how to
find it.

## Loudspeaker cables

Loudspeaker cables carry large currents into low impedances, so their resistance matters and their shielding does
not. Both conductors count, so the resistance of a cable of length $L$ and cross-section $A$ is
$R = 2 \rho L / A$, with $\rho = 0.0175\ \Omega\,\text{mm}^2/\text{m}$ for copper. The loss in level is
$20 \lg \frac{Z}{Z+R}$ for a load impedance $Z$.

| Cross-section | Length | Resistance | Loss into 8 Ω | Loss into 4 Ω |
|---|---|---|---|---|
| 1.5 mm² | 20 m | 0.47 Ω | 0.5 dB | 1.0 dB |
| 2.5 mm² | 20 m | 0.28 Ω | 0.3 dB | 0.6 dB |
| 2.5 mm² | 50 m | 0.70 Ω | 0.7 dB | 1.4 dB |
| 4 mm² | 20 m | 0.18 Ω | 0.2 dB | 0.4 dB |
| 4 mm² | 50 m | 0.44 Ω | 0.5 dB | 0.9 dB |
| 6 mm² | 50 m | 0.29 Ω | 0.3 dB | 0.6 dB |

The handbook sets its practical limit at a loss of less than 0.5 dB, and that limit is a fair one. With 2.5 mm², it
allows about 34 m into 8 Ω and 17 m into 4 Ω, and with 4 mm² about 54 m and 27 m. A subwoofer at 2 Ω, or two boxes
in parallel on one cable, halves these lengths again. The cable resistance also lowers the damping that the amplifier
exerts on the bass driver, as [chapter 13](13-power-amplifiers.md#the-cable-and-the-damping-factor) shows, which is a
second reason for the thicker cable on long subwoofer runs, or for placing the amplifiers next to the boxes.

The handbook also warns that the capacitance and inductance of unsuitable cable, such as coaxial or thin multicore
cable, can roll off the response. Proper loudspeaker cable with two heavy conductors avoids this.

Loudspeaker polarity is kept by convention, with pin 1+ to the positive terminal of the amplifier, and every cable is
checked once with a polarity tester or by measurement before it goes into stock.

## Digital audio links

Digital audio removes the noise and loss of long analog runs and carries many channels on one cable.

| Format | Medium | Channels at 48 kHz | Notes |
|---|---|---|---|
| AES3 (AES/EBU) | 110 Ω twisted pair, XLR | 2 | Self-clocking; 75 Ω coaxial variant AES-3id |
| S/PDIF | Coaxial RCA or optical | 2 | Consumer variant of AES3 |
| ADAT | Optical | 8 | Common on interfaces; 4 channels at 96 kHz |
| MADI (AES10) | Coaxial or fibre | 64 | Point to point, also 56-channel mode |
| AES50 | Ethernet cable, point to point | 48 | Not a network; carries its own clock |
| Dante | Ethernet network | Up to hundreds | Proprietary, most widely used; AES67 mode |
| AES67 | Ethernet network | Depends on network | Interoperability standard between networks |
| AVB / Milan | Ethernet network, AVB switches | Depends on network | IEEE 802.1 standards; Milan profile for audio |
| SMPTE ST 2110-30 | Ethernet network | Depends on network | Broadcast, based on AES67 |

A MADI link with 64 channels of 24 bits at 48 kHz carries about 74 Mbit/s of audio. A gigabit network carries
hundreds of such channels, which is why one network cable now replaces a multicore.

### Clocking

Every digital device samples at a rate set by a clock, and two devices that exchange audio must share that clock, or
samples are lost or repeated at regular intervals, heard as clicks. Point-to-point links such as AES3 and MADI carry
the clock in the signal or alongside it on a word clock cable, and one device is the master. Networks distribute the
clock with the Precision Time Protocol (PTP, IEEE 1588), which elects one device as the leader and synchronises all
others to it. Dante uses PTP version 1, and AES67 and Milan use version 2, which matters when they are combined.

### Latency

Each link and each conversion adds latency. A network such as Dante adds a set latency per receiver, chosen between
about 0.25 ms and a few milliseconds depending on the number of switches in the path. One millisecond is 48 samples at
48 kHz and equals 0.34 m of sound travel, so a few milliseconds in the signal chain are small next to the distances
in a venue, but they add up across a console, a processor and the network, and they matter for in-ear monitoring,
as chapter 18 explains.

## Networks in practice

Audio networks use standard Ethernet equipment, but they need more care than an office network.

- **Dedicated switch or VLAN.** Audio runs on its own switches, or on a separate VLAN, so that other traffic cannot
  delay it. Lighting and video may share a switch through VLANs, not as a flat network.
- **Quality of service.** The switch prioritises the clock (PTP) and audio packets over other traffic, with the DSCP
  values the protocol documents.
- **Energy-efficient Ethernet off.** EEE (IEEE 802.3az) lets ports sleep and disturbs the clock, and it is disabled on
  every switch port that carries audio.
- **Multicast.** Flows to several receivers are sent as multicast, and IGMP snooping keeps them from flooding every
  port.
- **Redundancy.** Dante and similar protocols can run a primary and a secondary network in parallel, on separate
  switches and cables, so that a failed cable does not interrupt the audio.
- **Length.** Copper Ethernet runs up to 100 m per segment. Longer runs, and runs that need electrical isolation, use
  fibre, with multimode fibre for some hundreds of metres and single-mode fibre for kilometres.
- **Documentation.** A diagram of the network with IP addresses, switch ports and device names, kept with the
  system, saves an hour on every fault.

## USB, Bluetooth and computers

Computers join the system through USB audio interfaces, through the console's own USB or network card, or through a
software implementation of the network protocol. Class-compliant USB audio needs no driver on most operating systems.

Bluetooth audio adds a latency of roughly 100 ms to 300 ms, which corresponds to 34 m to 100 m of sound travel. It is
acceptable for background music from a phone, but not for any signal that must be in time with live sound or a
screen. Its codecs reduce the data, and its range and reliability on a crowded stage are poor, so a cable or a
dedicated wireless system is preferred wherever it matters.

## What changed since 1989

| Handbook | Then | Today |
|---|---|---|
| §15.1, §15.2 | Shielding, capacitance, jackets, snakes | Kept; star-quad added; digital stage boxes |
| §15.3 | Phone, phono, XLR connectors | Kept; pin 2 hot standardized; speakON, powerCON, etherCON, CEE |
| §17.3 | +4 dBu and −10 dBV, balanced and unbalanced, 600 Ω matching | Voltage bridging; pin-1 problem (AES48) |
| §18.4 | Wire gauge table, banana and phone connectors | Metric cross-sections computed; speakON |
| — | Not covered | AES3, MADI, AES50, Dante, AES67, AVB/Milan, ST 2110-30; PTP; network practice; USB and Bluetooth |

## In the SdWa5 rig

[The connections](../../sdwa5-3d/docs/signal-chain.md#the-connections) of one event, MARK Salzburg, list every
device and cable of the rig. Which output socket of an amplifier feeds which way of a two-way box over a single
speakON cable was found on the bench by measurement, as
[S3, pinout and high-pass check](../../sdwa5-dsp/docs/measurements.md#s3-pinout-and-high-pass-check) records, which
is the pin-convention problem of the connector section in practice.

## To verify in pass 2

- Typical capacitance of microphone cable (about 100 pF per metre) and of star-quad cable.
- Pin 2 hot in IEC 60268-12 and AES14, and when the American convention changed.
- AES48 and the 1995 description of the pin-1 problem (Muncy, *JAES* 43).
- powerCON TRUE1 rated for connection under load; CEE colours and ratings per IEC 60309.
- Channel counts of ADAT, MADI (56 and 64), AES50 at 48 kHz.
- Dante latency settings, its PTP version, and the AES67 and Milan PTP versions.
- The EEE effect on PTP and the switch recommendations of Dante and Milan.
- Multimode and single-mode fibre ranges for the common transceivers.
- Bluetooth latency of current codecs, including LE Audio.
- The speakON NL4 pin convention for two-way boxes across manufacturers.

## Sources

- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §15 (pp. 281–302),
  §17.3 (pp. 325–327), §18.4 (pp. 355–358).
- AES3, AES10 (MADI), AES14, AES48, AES50, AES67; IEC 60268-12; IEC 60309; IEEE 1588; IEEE 802.1 (AVB);
  SMPTE ST 2110-30.
- Muncy, N.: Noise susceptibility in analog and digital signal processing systems, *JAES* 43, 1995.
- SdWa5: [signal chain](../../sdwa5-3d/docs/signal-chain.md), [measurements](../../sdwa5-dsp/docs/measurements.md).
