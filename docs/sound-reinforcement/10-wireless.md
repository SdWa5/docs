# 10. Wireless microphones, in-ear monitors and intercom

> **Draft, pass 1.** This chapter was written from general knowledge and checked against reference literature for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers where wireless audio may transmit in Europe and Austria, how analog and digital systems differ,
how several systems are made to work side by side, how antennas and cables decide the range, and how in-ear monitors
and crew intercom fit in. The frequency rules have changed more than anything else in this book. Wireless
microphones once used VHF and free TV channels, while today's European bands are the result of two rounds of
clearing TV spectrum for mobile networks. All frequency ranges and licensing rules below are marked for
verification, because they change and differ between countries.

## Where wireless audio may transmit

Wireless microphones and in-ear monitors are part of what regulators call programme making and special events
(PMSE). In most European bands they are secondary users, which means they may use a frequency only where it does not
interfere with the primary service, and they must accept interference from it.

| Band | Status in the EU | Typical use |
|---|---|---|
| 470–694 MHz (UHF TV band) | Secondary use in channels not used by TV in the area, at least until 2030 | The main band for professional microphones and in-ear monitors |
| 694–790 MHz (700 MHz band) | Cleared for mobile networks by 2020; a part of its duplex gap open for PMSE in some countries | Older equipment now unusable outside the gap |
| 790–862 MHz (800 MHz band) | Cleared for mobile networks around 2010–2015 | Old equipment unusable, except in the duplex gap |
| 823–832 MHz (duplex gap of the 800 MHz band) | Harmonised for PMSE, usually licence-exempt | A few channels, close to mobile uplink |
| 863–865 MHz | Licence-exempt short-range devices | Consumer and entry-level systems, crowded |
| 1785–1805 MHz | Harmonised for PMSE | Professional systems as an alternative to UHF |
| 1880–1900 MHz (DECT) | Licence-exempt | Intercom, some conference microphones |
| 2.4 GHz (ISM) | Licence-exempt, shared with Wi-Fi and Bluetooth | Digital consumer and some professional systems |

In the UHF TV band, which channels are free depends on the place. A TV transmitter in Salzburg occupies different
channels than one in Vienna, so a touring system needs a frequency plan for each venue. In Austria, the use of
wireless microphones in the TV band is coordinated by the telecommunications authorities, and some bands are covered
by a general authorisation while others need an individual assignment. In Germany, the Federal Network Agency issues
general authorisations for most PMSE bands, with an individual assignment for larger events.

Equipment bought before the clearing of the 800 and 700 MHz bands may still be in a rental stock or an association's
storage. It may no longer be used in the cleared ranges, and using it there interferes with mobile networks and
can be prosecuted.

## Analog and digital systems

### Analog FM

An analog wireless microphone frequency-modulates its carrier with the audio. To gain dynamic range, it compresses the
audio before transmission, typically at a ratio of 2 to 1, and expands it in the receiver. The compander is
proprietary, which makes systems of different makes incompatible. A transmitter of one make with a receiver
of another may work, but it sounds wrong because the compander and the frequency deviation do not match. Analog
systems have almost no latency and degrade gradually as the signal weakens, with noise and then crackle before a
dropout.

### Digital

A digital system converts the audio, codes it and transmits it as data. It needs no compander, so its sound does not
change with level, and it is more tolerant of intermodulation, which allows closer spacing of channels. It adds
latency, typically 2 to 4 ms for professional systems, which matters for in-ear monitors and when a wireless and a
wired microphone pick up the same source. It also fails abruptly. A digital link stays perfect until it loses too many
packets and then mutes. Some systems encrypt the audio, which matters for confidential speech at conferences.

Neither type is compatible between makers, and digital systems are often not compatible between product lines of
one maker.

## Several systems side by side

### Intermodulation

When two or more transmitters are close together, for example on performers who stand next to each other or in a rack
of in-ear transmitters, their signals mix in the output stages and in the receivers' input stages. The result is new
signals at frequencies that are combinations of the original ones. The strongest are the third-order products
$2f_1 - f_2$ and $2f_2 - f_1$ for every pair, and $f_1 + f_2 - f_3$ for every triple.

With carriers at 606.0, 606.4 and 606.8 MHz, equally spaced by 400 kHz, the third-order products fall at 605.2,
605.6, 606.0, 606.4, 606.8, 607.2 and 607.6 MHz. Each of the three carriers is hit by a product of the other two, so
equal spacing is the worst plan. Moving the third carrier to 607.2 MHz moves all products off the carriers.

The number of products grows quickly with the number of systems.

| Systems | Products $2f_1 - f_2$ | Products $f_1 + f_2 - f_3$ |
|---|---|---|
| 4 | 12 | 12 |
| 8 | 56 | 168 |
| 16 | 240 | 1680 |
| 32 | 992 | 14 880 |

Beyond a handful of systems, a frequency plan has to be calculated, which is what the coordination software of the
microphone makers and independent tools do. They take the free TV channels, the products up to fifth order, the
required spacing for each model and the systems already in use, and they produce compatible groups.

### Scanning and coordination

A receiver or a scanner measures the RF spectrum at the venue, and the coordination software places the channels in
the quiet parts. The scan is repeated on the day of the show with the other wireless users present, because a TV
transmitter, an OB van or the next stage at a festival changes the picture. At a larger event, one person
coordinates all wireless users, and every system that arrives is entered into one plan.

## Range, antennas and cables

### What limits the range

Radio signals weaken with distance in the same way as sound in a free field, and the free-space path loss in decibels
for a distance $d$ in kilometres and a frequency $f$ in megahertz is

$$\mathrm{FSPL} = 20\lg d + 20\lg f + 32.44$$

| Distance | 600 MHz | 1800 MHz | 2.44 GHz |
|---|---|---|---|
| 10 m | 48.0 dB | 57.5 dB | 60.2 dB |
| 30 m | 57.5 dB | 67.1 dB | 69.7 dB |
| 50 m | 62.0 dB | 71.5 dB | 74.2 dB |
| 100 m | 68.0 dB | 77.5 dB | 80.2 dB |

A transmitter of 10 to 50 mW, or 10 to 17 dBm, therefore reaches a stage-sized range comfortably in free space. The
problems come from the rest. The human body absorbs strongly at these frequencies, so a beltpack on the back of a
performer who faces away from the antenna can lose 10 to 20 dB. Higher bands lose more to distance and to bodies.

Multipath causes dropouts. The signal reaches the receiver by several paths, directly and reflected from walls,
trusses and the floor, and at some positions the paths cancel. The cancellation zones are about half a wavelength
apart, which is 25 cm at 600 MHz, so a performer who takes a step moves from a dead spot to a good one.

### Diversity

A diversity receiver has two antennas at different positions and uses whichever receives the better signal at each
moment, or combines both. It is unlikely that both are in a cancellation zone at once. The antennas are placed at least
a quarter wavelength apart, and in practice one metre or more for wide-area coverage.

### Antennas

Each receiver comes with two small whip antennas. Their length matches a quarter wavelength, about 10.8 cm at 694 MHz
and 15.9 cm at 470 MHz. For more than a few systems, or when the receivers are not at the stage, an antenna
distribution system is used. It takes two antennas, amplifies their signals and splits them to all receivers.

Directional antennas, such as log-periodic paddles and helical antennas, gain several decibels towards the stage and
reject signals from behind. High-gain beams with a very narrow pattern would need to follow the performer and are
avoided, but the moderate directivity of a paddle or a helical aimed at the performance area is now standard.
Helical antennas receive circular polarisation, which suffers less when a transmitter is held at an angle.

### Cables

Antenna cable loses signal with length and frequency, and the loss comes before the receiver's input stage, so it
adds directly to the noise. Placing the receivers near the stage and running the audio over a long line
instead avoids that loss, and a networked receiver placed at the stage is the modern form of it.

| Cable type, loss per 100 m at about 600 MHz | 10 m | 20 m | 30 m |
|---|---|---|---|
| RG58, about 35 dB | 3.5 dB | 7.0 dB | 10.5 dB |
| RG213, about 14 dB | 1.4 dB | 2.8 dB | 4.2 dB |
| Low-loss 10 mm, about 12 dB | 1.2 dB | 2.4 dB | 3.6 dB |

RG58 is acceptable for a few metres only. A booster at the antenna makes up for a long cable but also amplifies
interference, so it is set to compensate the cable loss and no more. All cables, splitters and antennas are 50 Ω.

## In-ear monitors

An in-ear monitor (IEM) system is a wireless link in the other direction, from a transmitter at the monitor position
to a bodypack receiver worn by the performer. Analog systems use stereo FM with a multiplex signal like FM radio,
and digital systems are spreading.

Several IEM transmitters in one rack produce strong intermodulation with each other, because their outputs are close
together and at full power. An active combiner merges them into one antenna with isolation between the inputs. IEM
frequencies are placed in the frequency plan together with the microphones, often in a separate part of the band, so
that the strong IEM carriers do not land products on the weak microphone signals at the receiver.

The latency of a digital IEM link adds to the latency of the console. A singer hears their own voice through the
bone of the skull at once and through the in-ear mix with a delay, and more than a few milliseconds of total delay
can be noticed as a comb filter or a doubling. Chapter 18 covers monitor mixing and in-ear levels, and chapter 5 the
risk to hearing.

## Intercom

Wireless intercom began as a specialised tool for TV and theatre crews, with belt packs, base stations and the
distinction between simplex, half duplex and full duplex. Today intercom has become a system in
its own right at most events beyond the smallest.

- **Wired partyline.** A two-wire or four-wire system over microphone cable, with belt packs and speaker stations. All
  stations on a channel hear each other. Robust and simple, still common.
- **Wireless.** Belt packs that work full duplex, so that a crew member talks without pressing a button. DECT-based
  systems at 1.9 GHz are licence-exempt in Europe and handle many belt packs, and other systems use 2.4 GHz or
  5 GHz.
- **Matrix and IP.** A central matrix routes any station to any other, and IP-based systems carry intercom over the
  same network as the audio, often using AES67 for interoperability with other audio devices. Chapter 15 covers
  networks.

At an event, a minimum intercom connects the front-of-house position, the monitor position and the stage manager.
Where a crew depends on it for safety, such as for flown loads or pyrotechnics, a second, independent path is
planned.

## Batteries and practice

Batteries decide more shows than any specification. Alkaline AA cells give the longest runtime per cell in most
transmitters but are used once. NiMH cells and the makers' lithium packs are rechargeable, and the packs report their
remaining runtime to the receiver, which shows it at the console. A routine that has served many crews is to start
every show with fresh or fully charged cells, to note the time of insertion, and to watch the runtime display during
the show.

Further practice that keeps wireless reliable:

1. **Plan before the venue.** Check the free TV channels for the location, plan with coordination software and
   bring spare frequencies.
2. **Scan on site** with all systems of all users switched on.
3. **Walk the stage** with a transmitter before the show, listening and watching the receiver's RF meters for
   dropouts.
4. **Antennas in line of sight** of the performance area, above the heads of the audience, away from metal and LED
   walls, which radiate broadband interference.
5. **Spares ready.** A spare handheld with fresh batteries, set up and tested, at the side of the stage.

## To verify in pass 2

- Every band in the table, its status in the EU and in Austria, and the end date of PMSE use in 470–694 MHz; check
  Decision (EU) 2017/899, ECC Report 204 and ERC Recommendation 70-03 Annex 10, and the Austrian frequency usage
  plan (FNV) and RTR information.
- The licensing rules in Austria (general authorisation or individual assignment by band) and the German BNetzA
  general authorisations.
- The PMSE parts of the 700 MHz duplex gap (around 738–753 MHz) and their availability in Austria.
- The typical latency of digital systems (2 to 4 ms) and of digital IEM systems.
- The 10 to 20 dB loss through a performer's body at UHF.
- The cable loss figures per type at 600 MHz.
- The DECT intercom band and the use of AES67 in IP intercom systems.

## Sources

- Decision (EU) 2017/899 on the use of the 470–790 MHz band in the Union.
- CEPT ECC Report 204 and ERC Recommendation 70-03.
- Austrian Frequenznutzungsverordnung (FNV), RTR.
- AES67, high-performance streaming audio-over-IP interoperability.
- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §10.5 and §10.6
  (pp. 132–148).
