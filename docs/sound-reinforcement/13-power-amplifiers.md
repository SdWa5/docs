# 13. Power amplifiers

> **Draft, pass 1.** This chapter was written from general knowledge and checked against reference literature for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers how much voltage, current and power an amplifier delivers into a loudspeaker, how its ratings
are to be read, how amplifiers and loudspeakers are matched, how much a mains circuit can feed, and how the cable
between them and the constant-voltage systems of installations fit in.
Setting the amplifier's gain against the processor's limiters is in
[chapter 4](04-dynamic-range-gain-structure.md#matching-the-stages-after-the-console), and the loudspeakers
themselves are in [chapter 14](14-loudspeakers.md).

## Voltage, current and power

An amplifier is a voltage source. It turns a small input voltage into a large output voltage, and the loudspeaker's
impedance decides how much current flows and therefore how much power is delivered. Ohm's law and the power law tie
the four quantities together.

$$V = I R, \qquad P = V I = \frac{V^2}{R} = I^2 R$$

For a sine wave, the RMS values give the average power. The table gives the voltage and current an amplifier must
deliver for a given power into three loads.

| Power | 8 Ω | 4 Ω | 2 Ω |
|---|---|---|---|
| 100 W | 28.3 V, 3.5 A | 20.0 V, 5.0 A | 14.1 V, 7.1 A |
| 250 W | 44.7 V, 5.6 A | 31.6 V, 7.9 A | 22.4 V, 11.2 A |
| 500 W | 63.2 V, 7.9 A | 44.7 V, 11.2 A | 31.6 V, 15.8 A |
| 1000 W | 89.4 V, 11.2 A | 63.2 V, 15.8 A | 44.7 V, 22.4 A |
| 2000 W | 126.5 V, 15.8 A | 89.4 V, 22.4 A | 63.2 V, 31.6 A |

An ideal amplifier with a fixed maximum voltage of 40 V RMS would deliver 200 W into 8 Ω, 400 W into 4 Ω and 800 W
into 2 Ω. Real amplifiers fall short of the doubling at low impedances, because their power supply and output stage
limit the current. The ratio between the 8 Ω and 4 Ω ratings shows how stiff an amplifier is.

A loudspeaker's impedance is not a resistor. It varies with frequency, falling below the nominal value at some
frequencies and rising far above it at resonance, and it has a reactive part that shifts current and voltage apart in
phase. An amplifier that drives a nominal 4 Ω load may see 2.5 Ω at one frequency, and the reactive load makes the
output stage dissipate more than a resistor of the same value would. Chapter 5 explains why static tests on a
resistor miss this.

## How amplifiers are built

### Output stages

- **Class AB.** The traditional linear output stage. Its efficiency is about 50 to 60 % at full power and much lower at
  the average levels of music, so it turns most of its input into heat.
- **Class G and H.** Linear stages with two or more supply voltages, or a supply that tracks the signal, which raise
  the efficiency at average levels. They were the standard for high-power touring amplifiers before class D.
- **Class D.** The output transistors switch on and off at several hundred kilohertz, and a filter recovers the audio
  from the pulse width. Efficiency reaches about 80 to 90 % at high power, so a 4-channel amplifier of several
  kilowatts fits into two rack units and weighs a fraction of a linear one. Class D is now the standard for
  professional amplifiers.

### Power supplies

A linear supply with a mains transformer is heavy and draws its current in short peaks. A switch-mode supply (SMPS)
is much lighter. With power factor correction (PFC), it draws a sine-shaped current from the mains, which lets more
real power through a given breaker and reduces the load on generators. Many amplifiers can also limit their own
mains current, so that they do not trip a breaker on a loud passage.

### Processing and networks

Most current touring amplifiers include a loudspeaker processor with crossover, equalization, delay and limiters for
each output, as chapter 12 describes, and a network connection for audio, control and monitoring. The monitoring
reports load impedance, temperature, mains voltage and clip and limit events for each channel, which turns the
amplifier rack into a source of live diagnostics.

## Ratings

### What a power rating means

A power rating is meaningful only with its conditions, as chapter 8 explains. The conditions are the load, the
frequency range, the distortion at which the power was measured, how many channels were driven at once and for how
long.

- **Continuous power** is what the amplifier delivers with a sine wave, all channels driven, for a stated time.
- **Burst or peak power** is what it delivers for a short time, such as with a burst signal of a few milliseconds,
  before the supply sags. It is larger and closer to what music asks for, but it is not comparable between
  manufacturers who use different bursts.
- **Power bandwidth** is the frequency range over which the rated power is reached, as chapter 8 explains.

In the United States, the FTC rule on amplifier power ratings has required a preconditioning period and continuous
ratings for consumer amplifiers since the 1970s. CTA-2006 is a later test method for car
audio amplifiers. Professional amplifiers are not covered by either, and their data sheets give whatever the
manufacturer chooses. A sheet that states the burst signal, the duration, the load and the number of channels driven
can be compared with another that does the same.

### Bridging

Two channels of an amplifier can drive one loudspeaker in bridge mode. One channel receives the signal inverted, and
the loudspeaker is connected between the two hot outputs, so it sees twice the voltage. Into the same load, the
power quadruples in theory. Each channel, however, sees half the load impedance, so a bridged amplifier into 4 Ω loads
each channel as if it were driving 2 Ω. A bridged amplifier is therefore never connected to a load below its rated
bridged minimum.

### Gain and input sensitivity

An amplifier is specified either by its voltage gain in decibels or by its input sensitivity, which is the input
level that drives it to rated power. The two describe the same thing. An amplifier rated 1000 W into 8 Ω delivers
89.4 V at full power, which needs 2.25 V or +9.2 dBu at its input with 32 dB of gain, and +15.2 dBu with 26 dB. A
fixed voltage gain across all amplifiers of a system makes the processor's limiter thresholds the same for every
channel, which chapter 4 uses.

## Clipping and protection

When the signal asks for more voltage than the supply provides, the output clips. The peaks are flattened, and the
signal gains harmonics at high frequencies. Clipping can damage a tweeter even when the
amplifier is small. The clipped signal sends energy into the high-frequency driver that the programme did not have,
and a small, heavily clipping amplifier can burn a tweeter that a large amplifier running cleanly would not.

A limiter before the amplifier, set to the amplifier's clip level and the loudspeaker's limits, prevents both. Most
amplifiers have a clip limiter of their own, and the processor adds the driver protection, as chapter 4 shows.

Amplifiers also protect themselves, with current limits, thermal sensors and fans, DC protection that disconnects the
loudspeaker if a fault puts direct current on the output, and a soft start that limits the inrush current at power-on.

## Matching amplifiers to loudspeakers

### Power

A loudspeaker's power rating says how much it survives under a stated test signal, which chapter 14 explains. An
amplifier is usually chosen with more power than that rating, because a larger amplifier that runs below clipping is
safer than a smaller one that clips. A common rule is an amplifier rated at about 1.5 to 2 times the loudspeaker's
continuous rating, with the processor's limiters set to protect the loudspeaker. The manufacturer's recommendation for
a given box overrides any rule.

Every 3 dB of level costs twice the power, and every 10 dB ten times. A loudspeaker with a sensitivity of 98 dB at
1 W and 1 m reaches $L = L_{1W} + 10\lg P - 20\lg d$, so 125 dB at 1 m with 500 W, and 99 dB at 20 m. Doubling the
amplifier power to 1000 W adds 3 dB. More level beyond that point comes from more boxes or more efficient ones, not from
more amplifier.

### Impedance

Loudspeakers connected in parallel lower the impedance, and in series they raise it.

- Two 8 Ω boxes in parallel make 4 Ω, four make 2 Ω.
- Two 8 Ω boxes in series make 16 Ω, which is rarely useful because each box's impedance curve then affects the
  other's response.

Most professional amplifiers are stable down to 2 Ω, but they deliver their best performance at 4 Ω and above, and
many manufacturers recommend no more than two boxes per channel.

### The cable and the damping factor

The damping factor is the ratio of the load impedance to the source impedance the loudspeaker sees. An amplifier's
output impedance is very small, often a few milliohms, so the cable decides it. The resistance of a copper cable is
$R = \rho \cdot 2L / A$, with $\rho = 0.0175\ \Omega\,\mathrm{mm^2/m}$, the length $L$ one way and the cross-section
$A$.

| Cable | Length | Resistance | Loss into 8 Ω | Loss into 4 Ω | Damping factor at 4 Ω |
|---|---|---|---|---|---|
| 1.5 mm² | 20 m | 0.47 Ω | −0.49 dB | −0.96 dB | 8.4 |
| 2.5 mm² | 20 m | 0.28 Ω | −0.30 dB | −0.59 dB | 13.8 |
| 2.5 mm² | 50 m | 0.70 Ω | −0.73 dB | −1.40 dB | 5.6 |
| 4 mm² | 20 m | 0.18 Ω | −0.19 dB | −0.37 dB | 21.6 |
| 4 mm² | 50 m | 0.44 Ω | −0.46 dB | −0.90 dB | 8.9 |

The loss in level is small, but the cable resistance adds to the loudspeaker's own and changes the tuning of a
subwoofer, which damps its resonance less. Keeping the amplifiers close to the loudspeakers and the cables short and
thick matters more than an amplifier's damping factor of several hundred. Chapter 15 covers loudspeaker cables.

## Mains power

A single-phase circuit at 230 V with a 16 A breaker delivers at most 3680 W, and one with 10 A delivers 2300 W. An
amplifier of 85 % efficiency could turn that into about 3100 W of continuous output, so the mains circuit, not the
amplifier, is often the limit of a rack.

Music does not draw continuous power. Its average lies 6 to 12 dB below its peaks, so a channel that reaches its
rated power on the peaks draws a quarter to a sixteenth of it on average. Manufacturers state the mains current at one
eighth of rated power as a typical programme figure. Eight channels of 1000 W at one eighth power deliver 1000 W in
total, and with 80 % efficiency draw about 1250 W, which fits easily on a 16 A circuit. Heavily compressed programme
and limiters that work all the time raise the average towards a quarter, which halves the margin.

Large systems therefore spread their amplifiers over the three phases of a CEE supply, and they switch the amplifiers
on one after another, because their combined inrush current can trip a breaker before any programme plays. Chapter 17
covers mains distribution and safety.

## Constant-voltage systems

Installations with many loudspeakers far apart, such as public address in a building, background music and voice
alarm, use a constant-voltage distribution. The amplifier delivers a fixed voltage at full power, 100 V in Europe and
70.7 V in the United States, and each loudspeaker has a transformer with taps for the power it should draw. A tap of
$P$ watts at 100 V presents $Z = 100^2 / P$, which is 1000 Ω for 10 W and 2000 Ω for 5 W.

The loudspeakers are connected in parallel, and the sum of their taps must stay below the amplifier's rating. A 500 W
amplifier at 100 V can drive a total of 500 W of taps, which is a minimum load of 20 Ω. The high voltage and low current
allow long, thin cables, and the taps make the level of each loudspeaker independent of how many are connected.

Voice alarm systems for evacuation are constant-voltage systems with requirements of their own, under EN 54 for their
components and the national installation rules, including monitored lines, battery backup and a minimum
intelligibility. Their planning and installation are a specialist field outside the scope of an event system.

## In the SdWa5 rig

The rig's mains plan, which places four amplifiers and two DSPs on the three phases of a 16 A CEE supply, is in
[Mains](../../sdwa5-3d/docs/signal-chain.md#mains). It shows that the breaker is the tightest limit of the rig, that
the phases trip at about a third of the limiters' maximum, and that the amplifiers are switched on one at a time. The
choice of 32 dB of gain on the MM14K amplifiers and 26 dB on the TIP10000q follows from the DSP's ceiling and the
limiter thresholds, as [Why 32 dB and 26 dB](../../sdwa5-3d/docs/signal-chain.md#why-32-db-and-26-db) explains. The
mains figures there rest on assumed efficiency and programme fractions, which the rig document names as such.

## To verify in pass 2

- The efficiency of class AB (50 to 60 %) and class D (80 to 90 %) amplifiers at rated power.
- The FTC rule (16 CFR Part 432), its preconditioning and its scope; CTA-2006 title and scope.
- The rule of 1.5 to 2 times the loudspeaker's continuous rating; check loudspeaker manufacturers' guidance.
- The one-eighth power convention for mains current in amplifier data sheets (IEC 62368-1 or manufacturer practice).
- The resistivity of copper (0.0175 Ω mm²/m at 20 °C).
- EN 54-16 and EN 54-24 for voice alarm components, and the Austrian TRVB and German DIN VDE 0833-4 for installation.

## Sources

- 16 CFR Part 432, power output claims for amplifiers utilized in home entertainment products.
- CTA-2006, testing and measurement methods for mobile audio amplifiers.
- EN 54, fire detection and fire alarm systems, parts 16 and 24.
- SdWa5: [Signal chain](../../sdwa5-3d/docs/signal-chain.md), sections *Mains* and *Why 32 dB and 26 dB*.
- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §12 (pp. 193–208).
