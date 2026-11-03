# 7. Sound indoors

> **Draft, pass 1.** This chapter was written from general knowledge and checked against the 1989 handbook for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers what a room adds to a sound system. It covers what boundaries do with sound, the resonances of a
room at low frequencies, reverberation and how long it lasts, the distance at which the room becomes louder than the
loudspeaker, how intelligibility is measured, and how loudspeakers are placed and feedback is controlled when the
room takes part. It replaces handbook §6 (pp. 53–60) and §18.3.4 to §18.3.5 (p. 354). Free-field behaviour, the
inverse square law and gain before feedback are in [chapter 6](06-sound-outdoors.md).

## Boundaries

A sound wave that hits a wall, a floor or a ceiling is split three ways. Part of it is reflected back into the room,
part is turned into heat inside the material, and the rest passes through to the other side. The shares depend on the
frequency and the angle, but not on the level. An object that is small compared with the wavelength, such as a
lectern at 100 Hz, does not cast a shadow at all, because the sound bends around it. That bending is diffraction,
which the handbook calls refraction.

The absorption coefficient α, introduced by Wallace Sabine, gives the share of energy that does not come back, from
0 for a perfect reflector to 1 for an open window. A surface with α = 0.15 reflects 85 % of the energy, which is
$10 \lg 0.85 = -0.7$ dB. A reflection is therefore weakened much less than the absorption coefficient suggests, and a
room needs many reflections or highly absorbent surfaces before its sound decays.

The SdWa5 acoustics page rebuilds the handbook's table of absorption coefficients with the split into reflected,
absorbed and transmitted energy, and it adds the sound reduction index that matters for the neighbours. It is the
reference for this section, in [Reflected, absorbed and through](../acoustics.md#reflected-absorbed-and-through).

Three results from it matter most for a sound system.

- **The audience is the main absorber.** An occupied audience area absorbs nearly all the energy at mid and high
  frequencies, so a hall sounds very different empty at the sound check and full at the show.
- **Curtains work only at mid and high frequencies.** A curtain hung in front of a wall absorbs most where it hangs a
  quarter wavelength in front of the wall, where the air moves fastest. A curtain 10 cm from a wall helps from about
  850 Hz upwards and does almost nothing at 100 Hz.
- **Bass needs mass or depth.** Low frequencies pass through light walls and are absorbed only by deep porous
  absorbers or tuned resonators.

## Room modes

A wave that reflects back and forth between two parallel walls reinforces itself when a whole number of half
wavelengths fits between them. The room then resonates at those frequencies, and the pressure varies through the room
with loud places, the antinodes, and quiet ones, the nodes, half a wavelength apart. These resonances are the room
modes. Between two walls at distance $L$ they lie at

$$f_n = \frac{n\,c}{2L}, \quad n = 1, 2, 3, \dots$$

Those between one pair of opposite surfaces are axial modes. Tangential modes involve four surfaces and oblique modes
all six, and they are weaker. A rectangular room has all three kinds.

| Dimension | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|
| Hall, length 20 m | 8.6 Hz | 17.1 Hz | 25.7 Hz | 34.3 Hz |
| Hall, width 12 m | 14.3 Hz | 28.6 Hz | 42.9 Hz | 57.2 Hz |
| Hall, height 6 m | 28.6 Hz | 57.2 Hz | 85.8 Hz | 114.3 Hz |
| Small room, length 8 m | 21.4 Hz | 42.9 Hz | 64.3 Hz | 85.8 Hz |
| Small room, width 5 m | 34.3 Hz | 68.6 Hz | 102.9 Hz | 137.2 Hz |
| Small room, height 3 m | 57.2 Hz | 114.3 Hz | 171.5 Hz | 228.7 Hz |

Modes are spaced widely at the bottom of the range and crowd together further up. Above a certain frequency they
overlap so densely that the room no longer has distinct resonances, and the sound field behaves statistically. That
limit is the Schroeder frequency, with $T$ the reverberation time in seconds and $V$ the volume in cubic metres.

$$f_S \approx 2000 \sqrt{\frac{T}{V}}$$

| Room | Volume | Reverberation time | Schroeder frequency |
|---|---|---|---|
| Small room 8 × 5 × 3 m | 120 m³ | 0.5 s | 129 Hz |
| Hall 20 × 12 × 6 m, empty | 1440 m³ | 1.79 s | 71 Hz |
| Hall 20 × 12 × 6 m, occupied | 1440 m³ | 0.93 s | 51 Hz |
| Large hall | 10 000 m³ | 2.5 s | 32 Hz |

Below the Schroeder frequency, the bass at a seat depends on where the seat lies in the mode pattern, and two seats a
few metres apart can differ by 10 dB or more. Above it, the reverberation dominates. The practical consequences of the
modes are these.

- **An equalizer cannot fix a mode for the whole room.** A cut at a modal peak helps where the peak is and deepens the
  dip at a node. Moving the subwoofers, the listening position or the measurement position changes more.
- **Source position matters.** A mode is excited strongly by a source at its antinode and hardly at all by one at its
  node. The handbook says that loudspeaker placement does not change the modes, which is right for their frequencies
  but not for how strongly they are excited. Subwoofers placed at the middle of a wall do not excite the first width
  mode, which has its node there.
- **Small rooms are the hard case.** A rehearsal room or a small club has few, widely spaced modes in the range of the
  kick drum and the bass guitar.

## Reverberation

When a source in a room stops, its sound does not stop with it. The reflections go on, losing energy at every
boundary and in the air, until they die away. The time it takes for the level to fall by 60 dB is the reverberation
time $T$ or RT60.

### Calculating it

Sabine found that the reverberation time grows with the volume and falls with the total absorption. In SI units, with
$V$ in cubic metres and the equivalent absorption area $A = \sum S_i \alpha_i$ in square metres, his equation reads as
follows.

$$T = 0.161 \frac{V}{A}$$

Sabine's equation overestimates the time in rooms with a lot of absorption, because even a room with α = 1 everywhere
would still give a finite time. Eyring's equation, with the total surface $S$ and the mean absorption coefficient
$\bar\alpha$, corrects this.

$$T = 0.161 \frac{V}{-S \ln(1 - \bar\alpha)}$$

For a hall of 20 × 12 × 6 m, with 1440 m³ and 864 m² of surface, the two give the following.

| Mean absorption | Sabine | Eyring |
|---|---|---|
| 0.10 | 2.68 s | 2.55 s |
| 0.15 | 1.79 s | 1.65 s |
| 0.20 | 1.34 s | 1.20 s |
| 0.30 | 0.89 s | 0.75 s |

The same hall with a mean α of 0.15 empty gets an audience on 150 m² of its floor, which raises the absorption there
from about 0.1 to about 0.9. The reverberation time at mid frequencies falls from 1.79 s to 0.93 s by Sabine. The
audience halves the reverberation time, which is why a sound check in an empty hall misleads. The Fitzroy equation
mentioned in the handbook treats rooms where the absorption is concentrated on one pair of surfaces, such as a
hall with an absorbent ceiling and hard walls, and it gives longer times than Sabine there.

### What the room should have

A target depends on use and volume. The German DIN 18041 gives target times for rooms by use, as functions of the
volume, and it is the usual DACH reference for rooms up to about 30 000 m³. For a volume of 1440 m³ its formulas give
about 1.5 s for music and about 1.0 s for speech. A room for amplified music can be drier than one for acoustic
music, because the system supplies the energy and the room only needs to stay out of the way.

### Measuring it

ISO 3382-1 describes the measurement for performance spaces and ISO 3382-2 for ordinary rooms. A loudspeaker excites
the room with a sweep or noise, an omnidirectional microphone records the decay at several positions, and the
software calculates the time. The full 60 dB of decay is rarely above the background noise, so the standard
extrapolates from the slope between −5 and −25 dB (T20) or between −5 and −35 dB (T30). The early decay time (EDT),
from the first 10 dB, matches what listeners perceive more closely. REW, which is free, and commercial tools such as
Smaart and ODEON's measurement module all report these values from an impulse response.

## Direct and reverberant sound

### Critical distance

Close to a loudspeaker, the direct sound dominates and falls by 6 dB per doubling of the distance as outdoors. The
reverberant sound, on the other hand, is about equally strong throughout the room, as long as the source keeps
running. At some distance the two are equally loud. That distance is the critical distance $D_c$, and beyond it the
level stops falling and the room is louder than the loudspeaker.

$$D_c \approx 0.057 \sqrt{\frac{Q\,V}{T}}$$

$Q$ is the directivity factor of the loudspeaker on the axis that points at the listener, 1 for an omnidirectional
source and 10 for a horn with a directivity index of 10 dB. For the example hall, the critical distance is as follows.

| Directivity $Q$ | Directivity index | Empty, 1.79 s | Occupied, 0.93 s |
|---|---|---|---|
| 1 | 0 dB | 1.6 m | 2.2 m |
| 2 | 3 dB | 2.3 m | 3.2 m |
| 5 | 7 dB | 3.6 m | 5.0 m |
| 10 | 10 dB | 5.1 m | 7.1 m |
| 20 | 13 dB | 7.2 m | 10.0 m |

The direct-to-reverberant ratio falls by 6 dB per doubling of the distance, from +6 dB at half the critical distance
to −6 dB at twice and −12 dB at four times. Even a directional loudspeaker in a hall of this size leaves most of the
audience beyond the critical distance.

### Why directivity matters indoors

A directional loudspeaker raises the critical distance along its axis, because it sends more energy towards the
listener and less into the room. When its axis points at the audience, the energy that misses the listeners' ears
lands on the most absorbent surface in the room and does not return. Both effects reduce the reverberant field. Off
the axis, the critical distance shrinks, so the coverage pattern must match the audience area. A loudspeaker that
covers the side walls as well as the audience feeds the reverberation and gains nothing.

This is the main reason why directivity, and especially directivity that holds down into the lower midrange,
is valued so highly in sound reinforcement. A line array or a large horn keeps its pattern to lower frequencies than
a small box, and the bass, which no practical box can steer, is what makes a reverberant hall sound boomy.

## Intelligibility

Reverberation blurs speech. Each syllable is followed by its own decay, which masks the next, quieter syllable, and
consonants suffer most. A loud system cannot help beyond a point, because it raises the reverberation with the direct
sound.

The handbook mentions that acousticians relate intelligibility to the direct-to-reverberant ratio and leaves the
methods to the specialist. Since then, measured indices have become routine.

- **Speech Transmission Index (STI), IEC 60268-16.** STI measures how much the modulation of speech survives the
  path through the system and the room, including noise and reverberation, on a scale from 0 to 1. The standard's
  categories run from bad below 0.30 to excellent above 0.75. Voice alarm systems usually have to reach about 0.50.
  STIPA is a simplified test signal for measurement with a hand-held meter.
- **%ALcons (Peutz).** The articulation loss of consonants is an older measure that estimates the share of consonants
  missed by a listener. Peutz's estimate is $200\,D^2 T^2 N / (V Q)$, with $N = 1$ for a single source. For the
  example hall occupied, a horn with $Q = 10$ and a listener at 15 m, it gives about 2.7 %, which counts as good. The
  same hall empty gives about 10 %, at the edge of poor. The estimate is valid up to about three times the critical
  distance.
- **Clarity C50 and C80.** These compare the energy arriving in the first 50 ms (for speech) or 80 ms (for music) with
  the energy after it, in decibels. They come from the same impulse response as the reverberation time and are
  defined in ISO 3382-1.

Background noise reduces intelligibility as well. As a rule, speech should be at least about 10 to 15 dB above the
noise, and much more makes no further difference.

## Loudspeakers and feedback in a room

### Placement

The outdoor rules from chapter 6 hold indoors, with the room as an extra participant.

- **Aim at the audience, not at the walls.** The audience absorbs, and the walls reflect. The handbook aims at about
  two thirds of the depth of the hall, so that the level falls off towards the back and less sound reaches the rear
  wall. A slightly lower level at the back is accepted by listeners and often wanted.
- **Treat the rear wall if possible.** A reflective rear wall sends an echo back to the stage and the front rows, which
  is late enough to be heard as a separate event in a large hall. Heavy curtains help at mid and high frequencies.
- **Several sources rather than one loud one.** Delay loudspeakers further back keep the listeners there inside the
  critical distance of a closer source, at a lower level overall. Chapter 20 sets them up.
- **Mind the boundaries near the subwoofers.** A subwoofer on the floor gains up to 6 dB at low frequencies over the
  same box in free space, in a floor-wall edge up to 12 dB and in a corner up to 18 dB, as long as the distances are
  small compared with the wavelength. At larger distances, the reflection from a nearby wall cancels the direct sound
  at $f = c / (4d)$, which is 86 Hz for a box 1 m from the wall and 43 Hz for 2 m. A subwoofer against the wall or
  well away from it avoids a cancellation in its own range.

### Feedback indoors

A room makes feedback worse in two ways. The reverberant field adds to the sound at the microphone, and the modes
favour some frequencies where the loop gain rises first. A feedback frequency in a room is often a modal peak at the
microphone position, and it can shift when the temperature changes the speed of sound, because the room resonates at
a fixed wavelength.

The handbook prefers acoustic measures over equalization, and that order still holds.

1. **Move the microphone.** A microphone at a node of the troublesome mode picks it up much less, and a microphone in a
   damped part of the stage picks up less reverberation.
2. **Use a directional microphone close to the source,** with smooth off-axis response, because a lobe off its axis
   cancels the advantage of its pattern.
3. **Notch narrowly.** A modal resonance is only a few hertz wide. Its bandwidth is about $2.2 / T$, which gives
   1.2 Hz for the empty example hall and 2.4 Hz when occupied. A third-octave filter at 250 Hz is 58 Hz wide, a
   tenth-octave filter 17 Hz and a sixtieth-octave filter 3 Hz. Parametric notches of a tenth octave or narrower,
   set by ear or by an automatic feedback suppressor, take far less out of the programme than the third-octave
   graphic equalizers of 1989. Chapter 12 covers them.
4. **Ring out with care.** The gain is raised slowly until a frequency rings, that frequency is notched, and the step
   is repeated a few times. After the third or fourth notch, the gain gained per notch is usually small, and the
   remaining margin is better left unused.

## Predicting and measuring a room

Room acoustics software builds a 3D model of the room with the absorption of its surfaces and calculates the
reverberation, the coverage of each loudspeaker and the STI before anything is installed. EASE, ODEON and CATT-Acoustic
are the established tools for this. The loudspeaker manufacturers' own tools, such as EASE Focus, d&b ArrayCalc,
L-Acoustics Soundvision and Meyer MAPP 3D, calculate their own systems quickly, but they mostly treat the room as free
field and leave the reverberation out. For an existing room, a measurement with REW, Smaart or a similar tool gives
the reverberation time, the modes and the clarity from a few impulse responses in an hour, and that is usually the
better start for a temporary system in a venue that has been measured once.

## What changed since 1989

| Handbook | Then | Today |
|---|---|---|
| §6.1 | Reflection, absorption, transmission; bending around small objects called refraction | Same split, link to the SdWa5 acoustics page; bending is diffraction |
| §6.1.1 | Absorption coefficient, table of materials | Table kept in the acoustics page with transmission added |
| §6.2, §6.2.1 | Standing waves between walls, three kinds of mode, drapes at a quarter wavelength | Mode tables for two rooms, Schroeder frequency, source position |
| §6.3 | RT60 with Sabine, Eyring and Fitzroy in two unit systems | SI only, computed example, ISO 3382 measurement, DIN 18041 targets |
| §6.4 | Critical distance, directivity raises it on axis | Kept, with a formula and a computed table |
| §6.4.1 | Intelligibility left to specialists and computers | STI per IEC 60268-16, %ALcons, C50 and C80, prediction software |
| §18.3.4 | Feedback locks to room modes, loudspeaker placement does not help, third- to twelfth-octave notches | Source position does change mode excitation; tenth-octave and narrower notches, automatic suppressors |
| §18.3.5 | Aim two thirds back, treat the rear wall | Kept, with delay loudspeakers and subwoofer boundary effects |

## To verify in pass 2

- The quarter-wavelength rule for curtains (850 Hz for 10 cm); check absorber literature for the frequency where a
  porous layer at that distance becomes effective.
- The Schroeder frequency constant 2000; check Schroeder and Kuttruff, *Room Acoustics*.
- The assumed absorption of an occupied audience area (0.9) against an empty floor (0.1); check published data.
- The Fitzroy equation and when it gives longer times than Sabine.
- DIN 18041:2016, the room groups, the formulas for target reverberation times and their volume limits; and the
  Austrian ÖNORM B 8115-3 as the corresponding reference.
- ISO 3382-1 and ISO 3382-2, the evaluation ranges for T20 and T30, EDT, C50 and C80.
- The critical distance constant 0.057 and the assumption of a diffuse field.
- IEC 60268-16 edition, STI categories and the 0.50 target for voice alarm systems (EN 54-32, ISO 7240-19).
- Peutz's %ALcons formula, its constant, the meaning of $N$ (some versions use $N + 1$, which doubles the result),
  the categories below 5 % and above 10 %, and its range of validity.
- The 10 to 15 dB speech-to-noise ratio for intelligibility.
- Boundary gains of 6, 12 and 18 dB and the $c / (4d)$ cancellation.
- The mode bandwidth $2.2 / T$.

## Sources

- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §6 (pp. 53–60) and
  §18.3.4 to §18.3.5 (p. 354).
- Kuttruff, H.: *Room Acoustics*, CRC Press.
- ISO 3382-1 and ISO 3382-2, measurement of room acoustic parameters.
- IEC 60268-16, objective rating of speech intelligibility by speech transmission index.
- DIN 18041, acoustic quality in rooms.
- Peutz, V. M. A.: Articulation loss of consonants as a criterion for speech transmission in a room, *JAES* 19, 1971.
- SdWa5: [Acoustics](../acoustics.md), section *Reflected, absorbed and through*.
