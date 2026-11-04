# Appendix. Units, abbreviations and symbols

> **Draft, pass 1.** This chapter was written from general knowledge and checked against reference literature for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This appendix collects what the chapters define once and then use everywhere. It lists the units and their
prefixes, the levels with their references, the letters used in formulas and every abbreviation in the book.
Each entry is short and points to the chapter that explains it.

## Units

SI is the International System of Units, the modern and formal version of the metric system. Every SI unit is
metric, but not every metric unit is SI. Older decimal systems such as CGS, with the dyne and the microbar, are
metric too, and some units outside SI are accepted for use with it. This book uses SI throughout, with the
decibel as the one exception that it needs on almost every page.

| Symbol | Unit | Quantity | Note |
|---|---|---|---|
| m, mm, km | metre | length, distance, wavelength | |
| mm² | square millimetre | cable cross-section | |
| s, ms, µs, ns | second | time, delay, latency | |
| Hz, kHz, MHz, GHz | hertz | frequency | One cycle per second |
| K, °C | kelvin, degree Celsius | temperature | 0 °C is 273.15 K, and a difference of 1 K equals 1 °C |
| Pa, mPa, µPa | pascal | sound pressure | 1 Pa is about 94 dB SPL |
| V, mV, µV | volt | voltage | |
| A, mA | ampere | current | |
| W, mW, kW | watt | power | |
| VA, kVA | volt-ampere | apparent power | Used for generators and supplies |
| J | joule | energy | |
| Ω, kΩ, MΩ | ohm | resistance, impedance | |
| F, µF, nF, pF | farad | capacitance | |
| H, mH | henry | inductance | |
| bit/s, Mbit/s | bit per second | data rate | Not an SI unit, but used with SI prefixes |

| Prefix | Symbol | Factor |
|---|---|---|
| giga | G | 10⁹ |
| mega | M | 10⁶ |
| kilo | k | 10³ |
| milli | m | 10⁻³ |
| micro | µ | 10⁻⁶ |
| nano | n | 10⁻⁹ |
| pico | p | 10⁻¹² |

Older microphone data sheets give pressure in microbar, where 1 µbar equals 0.1 Pa and 1 dyn/cm². A sensitivity of
1 mV/µbar is therefore 10 mV/Pa, and a sensitivity in dB re 1 V/µbar becomes dB re 1 V/Pa by adding 20 dB, so
−74 dB re 1 V/µbar is −54 dBV/Pa.

## Levels

A level is ten times the logarithm of a power ratio or twenty times the logarithm of a ratio of voltages or
pressures. Its unit is the decibel, which is accepted for use with SI but is not an SI unit. A level without a
reference is a difference or a gain, and a level with one names it in the unit.
[Chapter 3](03-decibels-levels-loudness.md) explains all of them.

| Unit | Reference or meaning | Used for |
|---|---|---|
| dB | none, a ratio | gain, attenuation, differences |
| dBu | 0.7746 V | professional analog levels |
| dBV | 1 V | consumer line level, microphone sensitivity |
| dBm | 1 mW | legacy power levels, RF |
| dBW | 1 W | amplifier power |
| dBFS | digital full scale | digital levels, always 0 or below |
| dB SPL | 20 µPa | sound pressure level |
| dB(A), dB(C) | 20 µPa, weighted | sound levels with A or C frequency weighting |
| LUFS, LU | loudness units relative to full scale | programme loudness after ITU-R BS.1770, and differences of it |
| phon | level of an equally loud 1 kHz tone | loudness level |
| sone | 1 sone at 40 phon | loudness, doubling with every 10 phon above about 40 phon |

## Symbols

The same letter can stand for different quantities in different chapters, as is usual in acoustics. The table names
every meaning the book uses.

| Symbol | Quantity | Unit |
|---|---|---|
| $A$ | equivalent absorption area; cable cross-section | m²; mm² |
| $a$ | radius of a driver, as in $ka$ | m |
| $B$ | bandwidth | Hz |
| $c$ | speed of sound, 343 m/s at 20 °C | m/s |
| $D_c$ | critical distance | m |
| $D_0, D_s, D_1, D_2$ | distances in the acoustic gain equations | m |
| $d$ | distance; spacing between sources | m |
| $f$ | frequency | Hz |
| $H$ | height | m |
| $I$ | current | A |
| $k$ | wave number $2\pi f/c$; Boltzmann constant | 1/m; J/K |
| $L$ | level; length | dB; m |
| $L_p, L_W$ | sound pressure level, sound power level | dB |
| $L_{\text{Aeq},T}, L_{\text{Cpeak}}, L_{EX,8h}$ | A-weighted equivalent level over time $T$, C-weighted peak level, daily exposure level | dB |
| $N$ | number of sources, microphones or averages | |
| $n$ | counting index, as in a mode or band number | |
| $P$ | electrical power | W |
| $p$ | sound pressure | Pa |
| $Q$ | directivity factor | |
| $R$ | resistance | Ω |
| $r$ | distance from a source | m |
| $S$ | surface area | m² |
| $T$ | period; temperature; reverberation time | s; °C; s |
| $t, \Delta t$ | time, time difference | s |
| $U, V$ | voltage | V |
| $V$ | room volume | m³ |
| $W$ | sound power | W |
| $Z$ | impedance | Ω |
| $\alpha, \bar\alpha$ | absorption coefficient, mean absorption coefficient | |
| $\theta$ | angle | ° |
| $\lambda$ | wavelength | m |
| $\rho$ | resistivity, 0.0175 Ω mm²/m for copper | Ω mm²/m |
| $\lg, \ln$ | logarithm to base 10, natural logarithm | |

## Abbreviations

Names of products and software are left out, and so are standard numbers such as AES17 or IEC 61672-1, which each
chapter's *Sources* lists with their titles. The exceptions are AES3, AES50 and AES67, which name interfaces. The
chapter column links to the chapter that explains the term or uses it most.

| Abbreviation | Stands for | Meaning | Chapter |
|---|---|---|---|
| AA |  | Battery size of the cells in most wireless packs | [10](10-wireless.md) |
| AAC | Advanced Audio Coding | Lossy audio codec | [5](05-hearing.md) |
| ABX |  | Blind listening test in which an unknown X is identified as A or B | [5](05-hearing.md) |
| AC, DC | Alternating current, direct current |  | [16](16-measurement.md) |
| ADAT | Alesis Digital Audio Tape | Optical link for eight channels, named after the recorder that introduced it | [15](15-cables-connectors-networks.md) |
| ADC, DAC | Analog-to-digital converter, digital-to-analog converter |  | [1](01-signals-and-systems.md) |
| AES | Audio Engineering Society | Publishes the AES standards, numbered as in AES17 | [1](01-signals-and-systems.md) |
| AES3 |  | Two-channel digital audio interface | [15](15-cables-connectors-networks.md) |
| AES50 |  | Multichannel point-to-point link over network cable | [15](15-cables-connectors-networks.md) |
| AES67 |  | Interoperability standard for audio over IP networks | [15](15-cables-connectors-networks.md) |
| AFL, PFL | After-fader listen, pre-fader listen | Solo modes of a console | [18](18-stage-monitoring.md) |
| %ALcons | Articulation loss of consonants | Speech intelligibility after Peutz, in percent | [7](07-sound-indoors.md) |
| AMT | Air motion transformer | Tweeter with a folded diaphragm | [14](14-loudspeakers.md) |
| ASchG | ArbeitnehmerInnenschutzgesetz | Austrian worker protection act | [5](05-hearing.md) |
| AVB | Audio Video Bridging | IEEE 802.1 extensions for timed audio on Ethernet | [15](15-cables-connectors-networks.md) |
| BGBl | Bundesgesetzblatt | Federal law gazette in Austria and Germany | [5](05-hearing.md) |
| BNetzA | Bundesnetzagentur | German frequency regulator | [10](10-wireless.md) |
| BS | Broadcasting service (sound) | Series of ITU-R recommendations, as in ITU-R BS.1770 | [3](03-decibels-levels-loudness.md) |
| CCIF |  | Twin-tone intermodulation test, named after an international telephone committee | [8](08-specifications.md) |
| CEE |  | Common name of the IEC 60309 industrial power connectors | [17](17-power-grounding-safety.md) |
| CEPT | European Conference of Postal and Telecommunications Administrations | Coordinates radio spectrum in Europe | [10](10-wireless.md) |
| CFR | Code of Federal Regulations | United States federal rules, as in 16 CFR Part 432 | [13](13-power-amplifiers.md) |
| Class AB |  | Linear amplifier output stage | [13](13-power-amplifiers.md) |
| CLF, GLL | Common Loudspeaker Format, Generic Loudspeaker Library | Directivity data formats for prediction software | [14](14-loudspeakers.md) |
| CMRR | Common-mode rejection ratio | How well a balanced input rejects interference on both legs | [9](09-sources.md) |
| CNMAT | Center for New Music and Audio Technologies | Berkeley research centre where OSC was developed | [19](19-control-and-sync.md) |
| CONCAWE |  | Outdoor sound propagation method, named after an oil-industry environmental body | [6](06-sound-outdoors.md) |
| CTA | Consumer Technology Association | United States standards body, as in CTA-2034 | [8](08-specifications.md) |
| DACH | Germany, Austria, Switzerland | From the country codes D, A and CH | [5](05-hearing.md) |
| DCA | Digitally controlled amplifier | Control group that sets channel levels without carrying audio | [11](11-mixing-consoles.md) |
| DECT | Digital Enhanced Cordless Telecommunications | Band used by wireless intercom | [10](10-wireless.md) |
| DGUV | Deutsche Gesetzliche Unfallversicherung | German statutory accident insurance, issues safety rules | [17](17-power-grounding-safety.md) |
| DI | Direct injection | Box that turns an instrument or line output into a balanced microphone-level signal | [9](09-sources.md) |
| DIN | Deutsches Institut für Normung | German standards body | [3](03-decibels-levels-loudness.md) |
| DJ | Disc jockey |  | [1](01-signals-and-systems.md) |
| DMX512 |  | Lighting control protocol | [15](15-cables-connectors-networks.md) |
| DSCP | Differentiated Services Code Point | Priority field in the IP header | [15](15-cables-connectors-networks.md) |
| DSP | Digital signal processing, digital signal processor |  | [12](12-signal-processing.md) |
| EAD | Equivalent acoustic distance | Distance at which a listener hears a talker well enough without a system | [6](06-sound-outdoors.md) |
| EBU | European Broadcasting Union |  | [3](03-decibels-levels-loudness.md) |
| ECC, ERC | Electronic Communications Committee, European Radiocommunications Committee | CEPT committees, ERC is the predecessor | [10](10-wireless.md) |
| EDT | Early decay time | Decay time from the first 10 dB of a decay | [7](07-sound-indoors.md) |
| EEE | Energy-Efficient Ethernet | IEEE 802.3az, switched off for audio networks | [15](15-cables-connectors-networks.md) |
| EIA | Electronic Industries Alliance | United States standards body, as in EIA-310 for racks | [8](08-specifications.md) |
| EIN | Equivalent input noise | Noise of a preamplifier, referred to its input | [9](09-sources.md) |
| EN | Europäische Norm | European standard | [5](05-hearing.md) |
| EQ | Equaliser |  | [12](12-signal-processing.md) |
| ERB | Equivalent rectangular bandwidth | Width of an auditory filter | [5](05-hearing.md) |
| EU | European Union |  | [10](10-wireless.md) |
| FFT | Fast Fourier transform | Computes a spectrum from a block of samples | [16](16-measurement.md) |
| FIR, IIR | Finite impulse response, infinite impulse response | The two kinds of digital filter | [2](02-frequency-phase-time.md) |
| FM | Frequency modulation |  | [10](10-wireless.md) |
| FNV | Frequenznutzungsverordnung | Austrian frequency usage ordinance | [10](10-wireless.md) |
| FSPL | Free-space path loss | Loss of a radio signal over distance | [10](10-wireless.md) |
| FTC | Federal Trade Commission | United States authority behind the amplifier power rule | [13](13-power-amplifiers.md) |
| IEC | International Electrotechnical Commission |  | [3](03-decibels-levels-loudness.md) |
| IEEE | Institute of Electrical and Electronics Engineers |  | [15](15-cables-connectors-networks.md) |
| IEM | In-ear monitor |  | [18](18-stage-monitoring.md) |
| IETF | Internet Engineering Task Force | Publishes the RFCs | [19](19-control-and-sync.md) |
| IGMP | Internet Group Management Protocol | Manages multicast groups, used by IGMP snooping on switches | [15](15-cables-connectors-networks.md) |
| IM | Intermodulation | Distortion that creates sum and difference frequencies | [8](08-specifications.md) |
| IP | Internet Protocol |  | [15](15-cables-connectors-networks.md) |
| ISM | Industrial, scientific and medical | Licence-exempt radio band at 2.4 GHz | [10](10-wireless.md) |
| ISO | International Organization for Standardization |  | [3](03-decibels-levels-loudness.md) |
| ITD | Interaural time difference |  | [5](05-hearing.md) |
| ITU-R, ITU-T | International Telecommunication Union, radiocommunication and telecommunication sectors |  | [3](03-decibels-levels-loudness.md) |
| JAES | Journal of the Audio Engineering Society |  | [7](07-sound-indoors.md) |
| LAI | Bund/Länder-Arbeitsgemeinschaft für Immissionsschutz | German working group, issues the Freizeitlärm-Richtlinie | [6](06-sound-outdoors.md) |
| LC, ST | Lucent connector, straight tip | Optical fibre connectors | [15](15-cables-connectors-networks.md) |
| LE | Low Energy | Bluetooth variant, as in LE Audio | [15](15-cables-connectors-networks.md) |
| LED | Light-emitting diode |  | [17](17-power-grounding-safety.md) |
| LR24 | Linkwitz-Riley, 24 dB per octave | Fourth-order crossover | [2](02-frequency-phase-time.md) |
| LTC | Linear timecode | Timecode recorded as an audio signal | [19](19-control-and-sync.md) |
| LärmVibrationsArbSchV | Lärm- und Vibrations-Arbeitsschutzverordnung | German ordinance on noise and vibration at work | [5](05-hearing.md) |
| MADI | Multichannel Audio Digital Interface | Up to 64 channels on coax or fibre, AES10 | [15](15-cables-connectors-networks.md) |
| MIDI | Musical Instrument Digital Interface |  | [19](19-control-and-sync.md) |
| MP3 | MPEG-1 Audio Layer III | Lossy audio codec | [5](05-hearing.md) |
| MSC | MIDI Show Control |  | [19](19-control-and-sync.md) |
| MTC | MIDI timecode |  | [19](19-control-and-sync.md) |
| MUSHRA | Multiple stimuli with hidden reference and anchor | Listening test of ITU-R BS.1534 | [5](05-hearing.md) |
| NAG, PAG | Needed acoustic gain, potential acoustic gain | Gain a talker needs, and gain a system can give before feedback | [6](06-sound-outdoors.md) |
| NiMH | Nickel-metal hydride | Rechargeable cell | [10](10-wireless.md) |
| NIOSH | National Institute for Occupational Safety and Health | United States, publishes an exposure limit | [16](16-measurement.md) |
| NOM | Number of open microphones |  | [6](06-sound-outdoors.md) |
| NTSC, PAL | National Television System Committee, Phase Alternating Line | Analog TV systems that set the video frame rates | [19](19-control-and-sync.md) |
| ÖAL | Österreichischer Arbeitsring für Lärmbekämpfung | Austrian noise abatement body, issues ÖAL guideline No. 3 | [6](06-sound-outdoors.md) |
| OB | Outside broadcast | As in an OB van | [10](10-wireless.md) |
| ÖNORM |  | Austrian national standard | [7](07-sound-indoors.md) |
| OSC | Open Sound Control |  | [19](19-control-and-sync.md) |
| ÖVE | Österreichischer Verband für Elektrotechnik | Austrian electrotechnical association, issues ÖVE E 8101 | [17](17-power-grounding-safety.md) |
| PA | Public address | The main sound system for the audience | [6](06-sound-outdoors.md) |
| PE, PEN | Protective earth, protective earth and neutral | PEN is one conductor for both | [17](17-power-grounding-safety.md) |
| PFC | Power factor correction |  | [13](13-power-amplifiers.md) |
| PMSE | Programme making and special events | Regulatory term for wireless microphones and similar links | [10](10-wireless.md) |
| PTP | Precision Time Protocol | Clock synchronisation of audio networks, IEEE 1588 | [15](15-cables-connectors-networks.md) |
| RCA | Radio Corporation of America | Phono (cinch) connector | [15](15-cables-connectors-networks.md) |
| RCD | Residual current device |  | [17](17-power-grounding-safety.md) |
| RF | Radio frequency |  | [10](10-wireless.md) |
| RFC | Request for Comments | IETF standard document | [19](19-control-and-sync.md) |
| RG58, RG213 | Radio guide | Coaxial cable types | [10](10-wireless.md) |
| RIAA | Recording Industry Association of America | Phono equalisation curve | [9](09-sources.md) |
| RJ45 | Registered jack 45 | Eight-pin modular network connector | [15](15-cables-connectors-networks.md) |
| RMS | Root mean square |  | [3](03-decibels-levels-loudness.md) |
| RP, ST (SMPTE) | Recommended practice, standard | SMPTE document types, as in SMPTE ST 12-1 | [19](19-control-and-sync.md) |
| RT60 | Reverberation time | Time for a level decay of 60 dB | [7](07-sound-indoors.md) |
| RTA | Real-time analyser |  | [16](16-measurement.md) |
| RTP, RTP-MIDI | Real-time Transport Protocol | RTP-MIDI carries MIDI over it | [19](19-control-and-sync.md) |
| RTR | Rundfunk und Telekom Regulierungs-GmbH | Austrian frequency regulator | [10](10-wireless.md) |
| S/PDIF | Sony/Philips Digital Interface | Consumer digital audio | [15](15-cables-connectors-networks.md) |
| SCR | Silicon-controlled rectifier | Thyristor, as in old dimmers | [17](17-power-grounding-safety.md) |
| SI | Système international d'unités | See [Units](#units) | [A](#units) |
| SMPS | Switch-mode power supply |  | [13](13-power-amplifiers.md) |
| SMPTE | Society of Motion Picture and Television Engineers |  | [19](19-control-and-sync.md) |
| SNR | Signal-to-noise ratio | Also written S/N | [5](05-hearing.md) |
| SPL | Sound pressure level |  | [3](03-decibels-levels-loudness.md) |
| STI, STIPA | Speech Transmission Index, STI for public address | Speech intelligibility measures | [7](07-sound-indoors.md) |
| TA | Technische Anleitung | As in TA Lärm, German technical instruction on noise | [6](06-sound-outdoors.md) |
| TCP, UDP | Transmission Control Protocol, User Datagram Protocol |  | [19](19-control-and-sync.md) |
| THD | Total harmonic distortion |  | [8](08-specifications.md) |
| TIM | Transient intermodulation |  | [8](08-specifications.md) |
| TN, TN-S, TN-C, TN-C-S | Terre neutre | Earthing systems; S separate, C combined neutral and earth | [17](17-power-grounding-safety.md) |
| TRS, TS | Tip-ring-sleeve, tip-sleeve | Jack plugs | [15](15-cables-connectors-networks.md) |
| TRVB | Technische Richtlinien vorbeugender Brandschutz | Austrian fire protection guidelines | [13](13-power-amplifiers.md) |
| UHF, VHF | Ultra high frequency, very high frequency |  | [10](10-wireless.md) |
| UPS | Uninterruptible power supply |  | [17](17-power-grounding-safety.md) |
| USB, USB-MIDI | Universal Serial Bus |  | [15](15-cables-connectors-networks.md) |
| VCA | Voltage-controlled amplifier |  | [11](11-mixing-consoles.md) |
| VDE | Verband der Elektrotechnik Elektronik Informationstechnik | German electrical association and standards | [13](13-power-amplifiers.md) |
| VLAN | Virtual local area network |  | [15](15-cables-connectors-networks.md) |
| VOLV | Verordnung Lärm und Vibrationen | Austrian ordinance on noise and vibration at work | [5](05-hearing.md) |
| VU | Volume unit | Averaging level meter | [11](11-mixing-consoles.md) |
| WHO | World Health Organization |  | [5](05-hearing.md) |
| WST | Wavefront sculpture technology | Criteria for line arrays | [14](14-loudspeakers.md) |
| XLR |  | Locking round connector; XLR-3 for audio, XLR-5 for DMX | [15](15-cables-connectors-networks.md) |

## To verify in pass 2

- That the SI Brochure lists the decibel, bel and neper among the units accepted for use with SI, and in which
  edition.
- The expansions of ADAT, CCIF, CEE, RG and XLR, and of the Austrian and German bodies and ordinances (ASchG,
  FNV, LAI, ÖAL, ÖVE, RTR, TRVB, VDE, VOLV). ÖVE may now be named OVE.
- The symbols in ISO 80000-2 and IEC 60027-3 for logarithms and levels, against the usage in this book.

## Sources

- BIPM: *The International System of Units (SI)*, 9th ed. 2019.
- ISO 80000-1, ISO 80000-2, ISO 80000-8 (acoustics).
- IEC 60027-3, logarithmic and related quantities and their units.
- The chapters of this book, each with its own *Sources*.
