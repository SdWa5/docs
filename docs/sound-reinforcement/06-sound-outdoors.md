# 6. Sound outdoors

> **Draft, pass 1.** This chapter was written from general knowledge and checked against the 1989 handbook for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers how sound behaves when there are no walls, which is the simplest case and the base for every
other. It covers the loss with distance from point and line sources, a level budget from the loudspeaker to the last
row, what air, wind and temperature do over longer distances, how far a festival carries into the neighbourhood, and
how much gain a microphone can have before the system feeds back. It replaces handbook §5 (pp. 43–52) and §18.3.3,
together with the parts of §18.2.3 to §18.3.2 that lead up to it (pp. 351–353). Rooms follow in
[chapter 7](07-sound-indoors.md).

## Loss with distance

Outdoors, far from buildings and above a ground that absorbs some sound, a loudspeaker works in what is called a free
field. Its sound spreads without returning, and the level at a listener depends on the distance alone.

### Point source

A source that is small compared with the distance to the listener radiates as a point. Its power spreads over the
surface of a sphere, which grows with the square of the radius. The intensity therefore falls with the square of the
distance, and the sound pressure with the distance itself.

$$L(r) = L(r_0) - 20 \lg \frac{r}{r_0}$$

Every doubling of the distance costs 6.02 dB, which is usually written as 6 dB. Ten times the distance costs 20 dB.
The source's sound power level does not change with distance, because it describes the whole output, while the
sound pressure level describes one place in the field. Chapter 3 explains the difference.

### Line source

A source that is long compared with the distance to the listener, such as a tall line array seen from close by,
radiates a cylinder rather than a sphere. The surface grows with the radius alone, and the level falls by 3 dB per
doubling of the distance. No real line is infinite, so this holds only in the near field of the array. Beyond a
transition distance the array behaves like a point source again and loses 6 dB per doubling.

A common estimate of the transition distance is $r_t \approx H^2 f / (2c)$ for an array of height $H$ at frequency
$f$. It grows with frequency, so an array is a line source for the treble and a point source for the bass at the same
listener.

| Array height | 100 Hz | 1 kHz | 4 kHz | 10 kHz |
|---|---|---|---|---|
| 2 m | 0.6 m | 5.8 m | 23 m | 58 m |
| 4 m | 2.3 m | 23 m | 93 m | 233 m |
| 8 m | 9.3 m | 93 m | 373 m | 933 m |

The consequence is a tonal balance that shifts with distance, with relatively more treble near a long array than near
a point source of the same output. A line array is curved and processed so that its far field is shaped as well,
which chapter 14 covers.

| Distance from 1 m | Point source | Line source (near field) |
|---|---|---|
| 2 m | −6.0 dB | −3.0 dB |
| 4 m | −12.0 dB | −6.0 dB |
| 10 m | −20.0 dB | −10.0 dB |
| 25 m | −28.0 dB | −14.0 dB |
| 50 m | −34.0 dB | −17.0 dB |
| 100 m | −40.0 dB | −20.0 dB |

### A level budget

The handbook works two examples in feet and watts. The same method in metres starts from the level wanted at the last
listener and works back to the loudspeaker.

Say the audience should hear 100 dB(A) averaged over time at 50 m, and the programme has peaks 12 dB above that
average. A point source then has to produce 134 dB at 1 m for the average and 146 dB at 1 m for the peaks. At 25 m the
same targets need 128 dB and 140 dB. A single box of the kind used at small events has a maximum level of 125 to
135 dB at 1 m, so the budget shows at once whether one box per side is enough or whether the system needs more
boxes, a line array or delay loudspeakers further back.

Several boxes add up as follows. Boxes that cover the same area and add coherently gain up to 6 dB per doubling of
their number, while boxes whose sound adds without a fixed phase relation gain 3 dB. The handbook advises planning
with 3 dB per doubling and treating any further gain as headroom, and that is still a safe start.

### Covering the audience evenly

The front rows sit much closer to a loudspeaker than the back rows. A box whose acoustic centre lies 6 m above the
ears of the audience is 7.8 m from a listener at 5 m and 40.4 m from one at 40 m, a difference of 14.3 dB.

| Horizontal distance | Distance to the box | Angle below horizontal | Level relative to the back row |
|---|---|---|---|
| 5 m | 7.8 m | 50° | +14.3 dB |
| 10 m | 11.7 m | 31° | +10.8 dB |
| 20 m | 20.9 m | 17° | +5.7 dB |
| 30 m | 30.6 m | 11° | +2.4 dB |
| 40 m | 40.4 m | 8.5° | 0 dB |

Aiming the axis at the back row places the closer listeners off axis, and the box's vertical pattern then lowers
their level. The handbook shows a case where the off-axis loss and the distance gain cancel within ±2 dB. With a
conventional box of about 40° vertical coverage, this works for the rear two thirds of such an audience but not for
the front rows, which need front fills or a line array whose curvature spreads the energy by distance. Aiming the axis
into the middle of the audience makes it worse, because the front then gets both the shorter distance and the axis.
Two systems at the sides of a stage are each aimed towards the centre of the rear edge of the audience, so that they
overlap down the middle. Prediction software from the loudspeaker manufacturers makes this calculation for real
patterns and is covered in chapter 20.

## Air, wind and weather

Over the first tens of metres, distance is all that matters. Further out, the air itself changes the sound.

### Air absorption

Air turns sound into heat, and much more so at high frequencies. The cause is a relaxation of oxygen and nitrogen
molecules, which water vapour shifts in frequency. The handbook explains the humidity effect by the lower density of
moist air, but that explanation does not hold. The loss depends on temperature and humidity together, and not
monotonically, so dry air is not always the worst case. ISO 9613-1 gives the formula. The values below are computed
from it for standard air pressure.

| Air | 125 Hz | 500 Hz | 1 kHz | 2 kHz | 4 kHz | 8 kHz | 16 kHz |
|---|---|---|---|---|---|---|---|
| 20 °C, 70 % | 0.3 | 2.8 | 5.0 | 9.0 | 23.1 | 77.6 | 281 |
| 20 °C, 50 % | 0.4 | 2.7 | 4.7 | 9.9 | 29.7 | 105 | 365 |
| 20 °C, 30 % | 0.6 | 2.5 | 5.0 | 14.1 | 48.9 | 168 | 466 |
| 10 °C, 70 % | 0.4 | 1.9 | 3.7 | 9.7 | 33.1 | 118 | 370 |
| 10 °C, 30 % | 0.5 | 2.3 | 6.8 | 23.6 | 77.2 | 188 | 314 |

The values are in dB per kilometre. At 20 °C and 50 % humidity the air takes 1.5 dB at 4 kHz and 5.3 dB at 8 kHz over
50 m, and 10.5 dB at 8 kHz over 100 m. On a dry day the 8 kHz loss over 50 m grows to about 11 dB. The far audience of a
large event therefore needs high-frequency correction that changes with the weather, and modern line-array systems
provide an air-absorption filter per box or per zone for this. Thunder heard from far away is a low rumble for the
same reason.

### Wind and temperature

Sound travels with the air it moves in, and it travels faster in warm air. The speed is about 331 m/s at 0 °C,
343 m/s at 20 °C and 349 m/s at 30 °C.

A steady wind of 5 m/s changes the speed of sound by only 1.5 %, so a crosswind displaces the sound a little but does
not blow it away. What does matter is that wind is slower near the ground than above it. Sound that travels against
the wind is bent upwards, away from the audience, and sound that travels with the wind is bent downwards. Behind the
stage on a windy day, the PA sounds louder than expected, and the audience in front of it hears it weaker and thinner,
often with a level that pumps with the gusts. A gusty crosswind also moves the stereo image.

Temperature layers bend sound in the same way. Sound bends towards the slower, colder air.

- **Warm ground, cool air above** is the usual daytime case on a sunny afternoon. Sound bends upwards, and the level
  far away is lower than the distance law predicts.
- **Cool ground, warm air above** is an inversion, common after sunset on a clear evening and in valleys. Sound bends
  back down to the ground and can carry far, sometimes several decibels above the free-field prediction at hundreds of
  metres.

The inversion explains a familiar pattern of complaints. A festival that is inaudible in the village in the afternoon
can be heard well there at ten at night with the same settings, because the weather has turned the air into a
duct. The level at the mix position has not changed, only the path.

### The ground

Above hard ground, such as asphalt or a paved square, the sound reflected from the ground adds to the direct sound and
causes a comb filter at the listener, which chapter 2 explains. Grass and soft ground absorb part of the reflection,
and an audience absorbs much more. Raising the loudspeakers above the heads keeps the path to the back rows clear of
the people in front, who would otherwise absorb and scatter the high frequencies.

## Barriers and neighbours

### Barriers

A wall, a building or a ridge between the stage and a listener shields them as long as it blocks the line of sight.
Sound bends over the top edge, so the screening depends on how much longer the path over the top is than the direct
path, measured in wavelengths. A barrier helps at high frequencies and little at low ones. ISO 9613-2 limits the
screening of a single barrier to 20 dB and of a double edge to 25 dB, and once the barrier's own sound reduction lies
about 10 dB above that, the sound through it no longer matters. The SdWa5 acoustics page explains this in
[What it means for the sound system](../acoustics.md#what-it-means-for-the-sound-system). Wind and temperature layers
can bend sound over a barrier, so its effect at a distance is less than the calculation on a still day.

### What reaches the neighbours

A system that produces 100 dB(A) at 30 m still gives about 75.6 dB at 500 m and about 69.5 dB at 1 km by distance
alone. Air absorption takes the treble away on the way, so the neighbours hear mostly kick drum and bass. A level
logged in dB(C) or in octave bands describes this better than one in dB(A). Cardioid subwoofer arrays, a stage
orientation that points the system away from the nearest houses, and a curfew for the loudest part of the programme
do more for the neighbours than a lower overall level.

Limits for neighbours are set nationally or regionally and, in Austria and Germany, mostly in the event permit.

- **Austria.** The noise from events falls under the event laws and the nuisance rules of the federal states, and the
  authority that issues the permit sets the conditions, often with a time limit in the evening. Assessment usually
  refers to the ÖAL guideline No. 3 for the judgement of noise immissions.
- **Germany.** Events are assessed under the leisure noise guideline of the federal states' working group on
  immission control (Freizeitlärm-Richtlinie), which follows the method of TA Lärm. In a general residential area it
  allows 55 dB(A) during the day and 40 dB(A) at night outside the most affected window, and it allows higher values,
  in the order of 70 dB(A) by day and 55 dB(A) at night, on a limited number of rare events per year.

Both countries treat ten o'clock in the evening as the start of the night period in most rules. A permit that names a
limit at the nearest house can be met only if that limit is translated into a limit at the mix position during the
setup, by measuring both at the same time with the system running.

## Feedback and gain before feedback

### The loop

A microphone in front of a loudspeaker forms a loop. The loudspeaker's sound reaches the microphone, is amplified and
comes out of the loudspeaker again. When the loop gain reaches 0 dB at a frequency where the delay around the loop
brings the sound back in phase, the system rings continuously. Just below that point, the system still rings briefly
after each sound, and it colours everything that passes through it. The rule from the handbook still stands. A system
runs at least 6 dB below the onset of feedback.

### Potential acoustic gain

The potential acoustic gain (PAG) is how much louder the system can make a talker at the listener than the talker
would be without it, at the point of feedback minus a safety margin. With four distances it follows from the inverse
square law alone, for an omnidirectional microphone and loudspeaker outdoors.

$$\mathrm{PAG} = 20\lg D_0 - 20\lg D_s + 20\lg D_1 - 20\lg D_2 - 10\lg \mathrm{NOM} - 6\ \mathrm{dB}$$

```mermaid
flowchart LR
    talker["Talker"] ---|"Ds"| mic["Microphone"]
    mic ---|"D1"| spk["Loudspeaker"]
    spk ---|"D2"| listener["Listener"]
    talker ---|"D0"| listener
```

$D_s$ is the distance from the talker to the microphone, $D_0$ from the talker to the listener, $D_1$ from the
microphone to the loudspeaker and $D_2$ from the loudspeaker to the listener. NOM is the number of open microphones,
and each doubling of it costs 3 dB. The level of the talker cancels out, so a louder voice does not help.

As an example, a speaker at a lectern talks into a microphone at 0.3 m, the loudspeaker is 5 m from the microphone,
and the listener sits 15 m from the talker and 14 m from the loudspeaker. The PAG is 25.0 dB at the point of feedback
and 19.0 dB with the margin. With a second open microphone it drops to 16.0 dB.

The needed acoustic gain (NAG) is what the listener needs, and it is set by the equivalent acoustic distance (EAD).
That is the distance at which the listener would understand the talker without a system, typically 1 to 4 m depending
on the background noise.

$$\mathrm{NAG} = 20 \lg \frac{D_0}{\mathrm{EAD}}$$

For the listener at 15 m and an EAD of 2 m, the NAG is 17.5 dB. The system with one microphone barely makes it, and
with two open microphones it does not. Moving the microphone closer makes up the difference.

| Talker to microphone | PAG with 6 dB margin |
|---|---|
| 0.3 m (lectern) | 19.0 dB |
| 0.1 m (handheld) | 28.6 dB |
| 0.05 m (handheld, close) | 34.6 dB |
| 0.02 m (headset) | 42.6 dB |

### What raises it

The handbook's three rules remain the core, and a modern system adds a few tools.

1. **Microphone close to the source.** Every halving of $D_s$ gives 6 dB, which is why a headset is the strongest
   single measure for a speaker or a singer who moves.
2. **Loudspeaker far from the microphone.** Every doubling of $D_1$ gives 6 dB. A flown system and loudspeakers in
   front of the stage line help, while a loudspeaker behind the microphone is the worst case.
3. **Directional microphones and loudspeakers, aimed.** A microphone that has the loudspeaker in its rejection zone
   and a loudspeaker that has the microphone off its axis each gain several decibels. The handbook expects about 6 dB
   together in practice, because a loudspeaker becomes omnidirectional at low frequencies and a microphone's pattern
   changes with frequency. A microphone with smooth off-axis response gains more than one with a sharper pattern and
   peaks off axis.
4. **Fewer open microphones.** Each doubling of NOM costs 3 dB. Muting unused channels or an automatic mixer that
   opens only the active microphone, covered in chapter 11, gains this back.
5. **Smooth response.** A peak in the response of the microphone, the loudspeaker or the room is where feedback
   starts first. A narrow notch at a ringing frequency raises the gain at that frequency, and chapter 12 covers
   automatic feedback suppressors.
6. **No loudspeaker where it is not needed.** Cardioid subwoofer arrays send less low frequency onto the stage, and
   in-ear monitors remove the wedge as a feedback path entirely.

A cardioid subwoofer array uses at least two sources, with one delayed and often polarity-inverted so that the two
cancel behind the array and add in front. For a gradient pair with the sources a quarter wavelength apart at 100 Hz,
the spacing is 0.86 m and the delay 2.5 ms. Such arrays reach well over 10 dB of rear rejection over the subwoofer
range, which helps the stage and the neighbours behind it. Chapter 14 covers the variants.

## What changed since 1989

| Handbook | Then | Today |
|---|---|---|
| §5.1 | Point source, 6 dB per doubling, two examples in feet | Point and line source, transition distance, metric level budget |
| §5.2.1 | Wind vector and gradient refraction, small effect | Kept, with the effect on the audience and behind the stage |
| §5.2.2 | Morning and evening temperature gradients | Kept, with night inversions and neighbour complaints |
| §5.2.3 | Air absorption above 2 kHz, explained by the density of moist air | Molecular relaxation per ISO 9613-1, computed table, air-absorption filters |
| §5.3, §5.3.1 | Feedback loop, 6 dB margin, maximum gain with four distances | PAG with NOM, NAG with EAD |
| §5.3.2 | Directional elements give about 6 dB together | Kept, with headsets, cardioid subwoofers and in-ear monitors |
| §18.2.3 | Clusters gain 3 to 6 dB per doubling | Kept, line arrays in chapter 14 |
| §18.3.1, §18.3.3 | Aiming at the rear, two clusters aimed at the centre rear | Kept, with front fills and prediction software |
| — | Not covered | Barriers per ISO 9613-2, neighbour limits in Austria and Germany |

## To verify in pass 2

- The transition distance formula $H^2 f / (2c)$ and its variants (Fresnel, Heil and Urban); check the line-array
  literature.
- Typical maximum levels of 125 to 135 dB at 1 m for small-event boxes; check data sheets.
- The ISO 9613-1 implementation in the scratchpad against the tables of the standard; the 20 °C and 10 °C rows at 70 %
  match ISO 9613-2 Table 2 as remembered.
- The size of the excess level under inversions at hundreds of metres; check ISO 9613-2 meteorological correction and
  CONCAWE.
- The barrier limits of 20 and 25 dB in ISO 9613-2.
- Austrian practice for event noise, including the ÖAL guideline No. 3 and the Salzburg event law.
- The German Freizeitlärm-Richtlinie values (55/40 dB(A) in general residential areas, rare events about 70/55 dB(A)),
  the number of rare events per year and the measuring point.
- The start of the night period at 22:00 in Austria and Germany.
- The rear rejection of cardioid subwoofer arrays (over 10 dB); check manufacturer application notes.
- The EAD range of 1 to 4 m; check Davis and Davis, *Sound System Engineering*.

## Sources

- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §5 (pp. 43–52) and
  §18.2.3 to §18.3.3 (pp. 351–353).
- ISO 9613-1, attenuation of sound during propagation outdoors, calculation of the absorption of sound by the
  atmosphere.
- ISO 9613-2, attenuation of sound during propagation outdoors, general method of calculation.
- ÖAL-Richtlinie Nr. 3, Beurteilung von Schallimmissionen.
- LAI Freizeitlärm-Richtlinie and TA Lärm.
- Davis, D., Davis, C.: *Sound System Engineering*, Focal Press.
- SdWa5: [Acoustics](../acoustics.md), section *What it means for the sound system*.
