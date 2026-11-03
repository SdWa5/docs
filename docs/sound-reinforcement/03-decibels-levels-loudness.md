# 3. Decibels, levels and loudness

> **Draft, pass 1.** This chapter was written from general knowledge and checked against the 1989 handbook for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers what a decibel is, which reference each common dB unit uses, how analog and digital levels
relate, and how measured sound levels connect to perceived loudness. It is the vocabulary for everything that
follows. It replaces handbook §3 (pp. 19–32), the operating-level part of §8.7 (pp. 92–96) and Appendix A on
logarithms (pp. 409–412).

## Logarithms in one table

The decibel is built on the base-ten logarithm. $\lg x$ is the power to which 10 must be raised to give $x$, so
$\lg 100 = 2$ and $\lg 0.001 = -3$. Three rules cover nearly all sound system arithmetic.

- $\lg(a \cdot b) = \lg a + \lg b$. Multiplying ratios means adding decibels.
- $\lg(a / b) = \lg a - \lg b$. Dividing ratios means subtracting decibels.
- $\lg(a^n) = n \cdot \lg a$. Squaring a ratio doubles its decibel value, which is why voltage and pressure use 20 lg.

| Ratio | 1.12 | 1.26 | 1.41 | 2 | 3.16 | 4 | 10 | 100 | 1000 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| As a power ratio, $10 \lg$ | 0.5 dB | 1.0 dB | 1.5 dB | 3.0 dB | 5.0 dB | 6.0 dB | 10 dB | 20 dB | 30 dB |
| As a voltage or pressure ratio, $20 \lg$ | 1.0 dB | 2.0 dB | 3.0 dB | 6.0 dB | 10 dB | 12 dB | 20 dB | 40 dB | 60 dB |

The values worth memorising are $\lg 2 \approx 0.301$, $\lg 3 \approx 0.477$ and $\lg 5 \approx 0.699$. From them
follow "double the power is +3 dB", "double the voltage is +6 dB" and "ten times the power is +10 dB". Nine watts
against two watts is $10 \lg 4.5 = 6.5$ dB, which a quick estimate confirms (2 → 4 → 8 W is two doublings, 6 dB,
and the ninth watt adds a little).

## What a decibel is

A decibel expresses the ratio of two quantities. For powers it is

$$L = 10 \lg \frac{P_1}{P_0} \ \text{dB},$$

and for field quantities whose square is proportional to power, such as voltage, current and sound pressure, it is

$$L = 20 \lg \frac{V_1}{V_0} \ \text{dB}.$$

The factor 20 is not a second definition. Power into a fixed resistance is $P = V^2/R$, so a tenfold voltage gives a
hundredfold power, and both are 20 dB. The two formulas give the same number of decibels for the same physical
change, as long as the impedance stays the same.

A decibel figure without a reference is a **relative** level, a difference or a gain. "The fader is at −10 dB" or
"the channel has 20 dB of headroom" are relative statements and complete as they stand. A decibel figure with a
fixed reference is an **absolute** level, and the reference must be named. "The console clips at +20 dB" says
nothing. "The console clips at +20 dBu" says it delivers 7.75 V. The suffix after "dB" carries the reference, and
confusing the suffixes is the most common way to misread a data sheet.

## Electrical levels

| Unit | Reference | Measures | Typical use |
|---|---|---|---|
| dBu | 0.7746 V | voltage, any impedance | professional line and mic levels |
| dBV | 1 V | voltage, any impedance | consumer line level, microphone sensitivity |
| dBm | 1 mW | power into a stated impedance | legacy, telephone lines, RF |
| dBW | 1 W | power | amplifier output, sometimes |
| dBFS | digital full scale | digital value | converters, digital consoles and files |

**dBu** is the professional voltage unit. Its odd reference of 0.7746 V is the voltage that dissipates 1 mW in
600 Ω, a legacy of the telephone lines on which early studio and broadcast systems ran. The "u" stood for
"unloaded", meaning the voltage is quoted regardless of load. Modern line inputs have impedances of 10 kΩ or more
and outputs of a few tens of ohms, so a source delivers the same voltage into any reasonable input, and a dBu figure
stays valid whatever is connected.

**dBV** uses 1 V as reference. It is the consumer line-level unit and the unit for microphone sensitivity
(chapter 9). The conversion is fixed.

$$L_{\text{dBu}} = L_{\text{dBV}} + 2.22 \ \text{dB}$$

**dBm** is a power unit and only equals dBu when the load is 600 Ω. It belongs to the era of 600 Ω matched lines and
appears today in older documentation, in RF and in some broadcast contexts. A line output "rated +20 dBm into
600 Ω" delivers 7.75 V. The same output into a 10 kΩ input delivers about the same voltage but far less power, so
its dBm figure changes with the load while its dBu figure does not. That is why voltage units replaced it.

**dBW** is a power unit for amplifiers. A 100 W amplifier delivers 20 dBW, a 1 kW one 30 dBW.

| dBu | −60 | −40 | −20 | −10 | 0 | +4 | +10 | +18 | +20 | +24 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Voltage (V rms) | 0.00077 | 0.0077 | 0.077 | 0.245 | 0.775 | 1.23 | 2.45 | 6.15 | 7.75 | 12.3 |
| dBV | −62.2 | −42.2 | −22.2 | −12.2 | −2.2 | +1.8 | +7.8 | +15.8 | +17.8 | +21.8 |

### Nominal levels and the three classes

Equipment is designed around a **nominal** operating level, the average level the circuits expect, with headroom
above it for peaks (chapter 4).

- **Mic level** is anything from the noise floor to around −20 dBu. A dynamic microphone with 2 mV/Pa delivers about
  −52 dBu at 94 dB SPL and about −16 dBu at 130 dB SPL. A condenser with 20 mV/Pa reaches +4 dBu at 130 dB SPL,
  which is why condenser microphones in kick drums and guitar cabinets need pads.
- **Line level** runs from about −20 dBu to the clip point of the equipment, typically +20 to +28 dBu. Two nominal
  standards coexist. Professional equipment uses **+4 dBu** (1.23 V). Consumer and much DJ equipment uses
  **−10 dBV** (0.316 V).
- **Speaker level** is the output of power amplifiers, from a few volts to well over 100 V (chapter 13).

The difference between the two line standards is

$$20 \lg \frac{1.228\ \text{V}}{0.316\ \text{V}} = 11.78 \ \text{dB}.$$

A consumer device plugged into a +4 dBu input arrives about 12 dB low and needs more gain, which costs noise. A
+4 dBu output plugged into a −10 dBV input arrives about 12 dB hot, and since consumer inputs often clip at around
+4 to +8 dBu, a professional output driven to its normal peaks will overload them. USB interfaces, DJ mixers and
playback devices often have switchable or poorly documented levels, so check the clip point of both sides rather
than the label.

### Voltage gain and power gain

Gain without a qualifier is ambiguous. A power amplifier fed 1.23 V into its 10 kΩ input and delivering 1.23 V into
an 8 Ω loudspeaker has a voltage gain of 0 dB and a power gain of 31 dB, because the input draws 0.15 mW and the
loudspeaker 189 mW. In a modern system nearly every gain is a voltage gain, and every stage except the power
amplifier is designed to deliver voltage into a light load. This book means voltage gain whenever it says gain.

The handbook also untangled the words volume, level and gain. Its advice still holds. "Level" is a quantity relative
to a stated reference, "gain" is a change of level through a stage, and "volume" is a colloquial word best avoided in
technical writing.

## Digital levels

A digital signal is a sequence of numbers with a largest possible value, **full scale**. Levels are given in **dBFS**,
decibels relative to full scale, so every real digital level is negative and 0 dBFS is the ceiling. AES17 defines
full scale by a sine wave whose peaks just reach the largest digital value. Under that definition a full-scale sine
reads 0 dBFS, and a square wave touching the same peaks would read +3 dBFS.

How a digital level corresponds to an analog voltage is a design choice of each converter, called **alignment**.
Two conventions are common.

| Alignment | 0 dBu corresponds to | +4 dBu corresponds to | 0 dBFS corresponds to |
|---|---:|---:|---:|
| EBU R68 | −18 dBFS | −14 dBFS | +18 dBu (6.15 V) |
| SMPTE RP 155 | −24 dBFS | −20 dBFS | +24 dBu (12.3 V) |

Live consoles and stageboxes do not follow either strictly. Many map 0 dBFS to somewhere between +18 and +24 dBu at
their analog outputs, and some let the user choose. The practical rule is to look up the maximum output level of
every analog output and the maximum input level of the device it feeds, and to match them (chapter 4). The SdWa5
rig's measurements showed that a processor's nominal ceiling and its real one can differ by several decibels.

**Peak versus true peak.** A digital meter that reads sample values can miss peaks that occur between samples and
appear after reconstruction in the DAC. A **true-peak** meter oversamples to estimate them. The difference is usually
below 1 dB, but heavily limited material can exceed 0 dBFS true peak while every sample stays below it.

## Acoustic levels

**Sound pressure level** uses 20 µPa as reference, roughly the threshold of hearing at 1 kHz.

$$L_p = 20 \lg \frac{p}{20\ \mu\text{Pa}} \ \text{dB SPL}$$

A pressure of 1 Pa is 94 dB SPL, which is why microphone sensitivities and acoustic calibrators use 94 dB.

| Situation | Approximate level |
|---|---:|
| Quiet bedroom at night | 25–30 dB(A) |
| Conversation at 1 m | 55–65 dB(A) |
| Busy street at the kerb | 75–85 dB(A) |
| Loud club, dance floor | 95–105 dB(A) |
| Front of a rock concert | 105–110 dB(A) |
| Kick drum, microphone inside the shell | 140 dB SPL peak and above |

**Sound power level** describes how much acoustic power a source radiates in all directions, with 1 pW as reference.

$$L_W = 10 \lg \frac{W}{1\ \text{pW}} \ \text{dB}$$

One acoustic watt is 120 dB re 1 pW. Sound power is a property of the source, while sound pressure depends on where
it is measured. Noise regulations for machines and the prediction of levels in rooms use sound power (chapters 6 and
7). The acoustic power a loudspeaker radiates is a small fraction of the electrical power it receives, typically a few
percent for direct-radiating cones and somewhat more for horn-loaded designs.

### Adding levels

Levels in decibels cannot be added directly. Incoherent sources, such as two different instruments or a band and the
crowd, add their powers.

$$L_{\text{sum}} = 10 \lg \left( 10^{L_1/10} + 10^{L_2/10} + \dots \right)$$

| Difference between two levels | 0 dB | 1 dB | 2 dB | 3 dB | 4 dB | 6 dB | 10 dB |
|---|---:|---:|---:|---:|---:|---:|---:|
| Add to the louder level | 3.0 dB | 2.5 dB | 2.1 dB | 1.8 dB | 1.5 dB | 1.0 dB | 0.4 dB |

Two sources of 90 dB give 93 dB. A source 10 dB quieter than another hardly changes the total. Four equal sources
give +6 dB. Coherent sources, such as two loudspeakers playing the same signal, can give up to +6 dB for two, or a
notch, depending on phase (chapter 1).

## RMS, peak and crest factor

The **RMS** (root mean square) value of a signal is the square root of the mean of its squared instantaneous values.
It is the value that produces the same heating in a resistor as a DC voltage of the same size, and it tracks the
energy of a signal and roughly its loudness. The **peak** value is the largest instantaneous value. Their ratio in
decibels is the **crest factor**.

| Signal | Crest factor |
|---|---:|
| Square wave | 0 dB |
| Sine wave | 3.01 dB |
| Pink noise, unfiltered | about 12 dB |
| Heavily limited modern master | about 6–10 dB |
| Speech, live drums, unprocessed acoustic music | 15–20 dB and more |

The crest factor of the programme decides how much of a system's peak capability is left for its average level, which
is the subject of chapter 4. It also explains why the phrase "RMS power" on amplifiers is a misnomer. What is meant is
the average power of a continuous sine, computed from the RMS voltage. Chapter 13 handles amplifier ratings.

Meters differ in what they show. A **peak** meter shows the highest instantaneous value and warns of clipping. An
**RMS** or VU-style meter averages over a few hundred milliseconds and follows loudness. A digital console meter
usually shows sample peaks in dBFS, and the gain structure of the console is set by it.

## Weighting and time constants

A sound level meter does not hear like a person, so it applies frequency weightings and time constants defined in
IEC 61672-1.

- **A-weighting** follows the ear's sensitivity at low levels, cutting about 30 dB at 50 Hz and 50 dB at 20 Hz. It is
  the weighting of most noise regulations and hearing-protection rules. It underestimates bass-heavy music at
  concert levels.
- **C-weighting** is nearly flat from about 30 Hz to 8 kHz and is used for loud music, for low-frequency complaints
  and for peak measurements.
- **Z-weighting** is flat across the measurement range and replaces the older "linear" setting.
- B and D weightings are obsolete.

The time constants are **F** (fast, 125 ms) and **S** (slow, 1 s). The quantities that matter for events are
averages over time.

- $L_{\text{Aeq},T}$ is the A-weighted energy average over a period $T$, such as 15 minutes or 60 minutes. Limits for
  audience exposure and for neighbours are usually given this way (chapters 5 and 6).
- $L_{\text{Ceq},T}$ is the same with C-weighting, increasingly used to limit bass.
- $L_{\text{Cpeak}}$ is the highest C-weighted instantaneous peak, used in hearing-protection rules.

Writing a level as "dB(A)" names the weighting. A level written as "dB" alone is unweighted or ambiguous, and an
SPL figure in a specification without weighting and time constant is incomplete.

## Loudness

Loudness is what a listener perceives, and it is not the same as sound pressure level. The ear is most sensitive
between about 2 and 5 kHz, largely because of the resonance of the ear canal, and much less sensitive at low and very
high frequencies, especially at low levels. **Equal-loudness contours** show which levels at each frequency sound
as loud as a 1 kHz tone. The original curves by Fletcher and Munson (1933) and Robinson and Dadson (1956) have been
replaced by ISO 226, last revised in 2023.

The **phon** names a contour by the level of the 1 kHz tone on it. A 60 phon sound is as loud as 60 dB SPL at 1 kHz,
whatever its frequency. Above about 40 phon, a rise of 10 phon is heard as roughly twice as loud. The **sone** scale
expresses that directly, with 1 sone at 40 phon.

| Loudness level (phon) | 40 | 50 | 60 | 70 | 80 | 90 | 100 | 110 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Loudness (sone) | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 |

This gives the rules of thumb that every engineer uses. A change of 1 dB is barely noticeable on music, 3 dB is easily
audible, and 10 dB sounds about twice as loud. Doubling the amplifier power gives 3 dB, so twice the perceived
loudness needs ten times the power.

The contours flatten at higher levels. At concert levels the ear hears bass and treble nearly as strongly as the
midrange, while at background levels the same mix sounds thin. A system set up for a quiet dinner may need more low
and high end than the same system at a party, which the handbook illustrated with the loudness button of hi-fi
amplifiers. Current DSPs can apply level-dependent loudness compensation based on ISO 226 automatically.

**Programme loudness** is measured in LUFS (loudness units relative to full scale) according to ITU-R BS.1770, with
EBU R 128 setting −23 LUFS as the broadcast target in Europe and streaming services normalising to targets around −14
to −16 LUFS. LUFS matter in live sound wherever programme is exchanged with broadcast or streaming. A livestream
feed, a playback file for an event or a pre-show playlist should be loudness-normalised so that the first track does
not arrive 8 dB louder than the walk-in music. LUFS do not replace dB SPL in the room, because they measure the
signal, not the sound.

## What changed since 1989

| Handbook | Then | Today |
|---|---|---|
| §3.1 | Decibel derivation with power and voltage examples, power-ratio tables | Kept, condensed into one table and three rules |
| §3.2.1 | dBm explained at length, 600 Ω lines still common | Legacy. Voltage units fit bridging interfaces |
| §3.2.3 | Confusion between dBv and dBV, NAB and IEC history | dBV is settled. dBv is no longer used |
| §3.2.5 | +4 dBm and +8 dBm for professional, −10 dBV for consumer | +4 dBu and −10 dBV. The +8 dBm broadcast level is rarely seen |
| §3.3 | Pressure in dyn/cm² and N/m² | Pascal only. 1 Pa is 94 dB SPL |
| §3.4 | RMS, the "RMS power" misnomer | Kept, plus crest factor and meter types. Amplifier ratings in chapter 13 |
| §3.6.1 | Fletcher-Munson and Robinson-Dadson contours | ISO 226:2023 |
| §3.6.2 | A, B and C weighting. Criticism of A-weighted limits | A, C and Z per IEC 61672-1, B obsolete, $L_\text{Aeq}$ and $L_\text{Cpeak}$ |
| §3.6.3 | Caution above 95 dB(C) for long periods | Exposure limits moved to chapter 5 |
| §8.7.1–8.7.2 | Level classes and dBm/dBW tables | Kept, with mic levels computed from sensitivity |
| §8.7.3 | Impedance and level, amplifier ratings into 4 and 8 Ω | Voltage-source principle kept here, amplifier part in chapter 13 |
| §8.7.4 | Hi-fi and pro equipment mismatches | Kept, extended to DJ gear and USB interfaces |
| App. A | Logarithms from first principles | One table and three rules |
| — | Not covered | dBFS, alignment, true peak, LUFS |

## To verify in pass 2

- AES17 definition of full scale and the resulting +3 dBFS for a full-scale square wave.
- EBU R68 alignment of −18 dBFS for 0 dBu, and SMPTE RP 155 alignment of −20 dBFS for +4 dBu, against the current
  editions.
- Typical clip levels of consumer line inputs (+4 to +8 dBu).
- The SPL examples in the table of situations; check against a noise reference and the WHO and DIN 15905-5 material
  used in chapter 5.
- Loudspeaker efficiency of a few percent for direct radiators; check against a loudspeaker reference (chapter 14).
- Crest factors of pink noise, limited masters and live programme; check against AES2-2012 and published programme
  analyses.
- IEC 61672-1 weightings (A-weighting −30.2 dB at 50 Hz and −50.5 dB at 20 Hz), time constants and the status of B
  and D weightings.
- ISO 226:2023 as the current edition of the equal-loudness contours.
- ITU-R BS.1770 and EBU R 128 targets, and the streaming normalisation range of −14 to −16 LUFS.

## Sources

- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §3 (pp. 19–32),
  §8.7 (pp. 92–96), Appendix A (pp. 409–412).
- AES17, measurement of digital audio equipment.
- EBU R68, alignment level in digital audio production equipment.
- SMPTE RP 155, reference levels for analog and digital audio systems.
- IEC 61672-1, sound level meters.
- ISO 226, normal equal-loudness-level contours.
- ITU-R BS.1770, algorithms to measure audio programme loudness and true-peak audio level.
- EBU R 128, loudness normalisation and permitted maximum level of audio signals.
