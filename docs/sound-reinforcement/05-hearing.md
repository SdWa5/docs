# 5. Hearing

> **Draft, pass 1.** This chapter was written from general knowledge and checked against reference literature for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers what the ear can hear, how it hides one sound behind another, how it decides where a sound
comes from, why a measurement and a listener can disagree about the same system, and how loud an event may be before
it harms the people in it. The answer to the last question has changed most in recent decades. Older sound
reinforcement literature advised caution above about 95 dB(C) and left the danger levels to others, while today an
EU directive protects the crew and a WHO standard and national norms address the audience. The numbers behind
decibels, weighting and loudness are in [chapter 3](03-decibels-levels-loudness.md).

## Range and sensitivity

A healthy young ear hears from about 20 Hz to about 20 kHz. The upper limit falls with age, and by fifty it often
lies between 12 and 16 kHz. Noise exposure takes away the range above 3 kHz first, with a typical notch near 4 kHz.
Below 20 Hz, sound is felt in the body rather than heard as a tone, which matters for subwoofers at high level.

The reference for sound pressure level, 20 µPa, sits close to the threshold of hearing at 1 kHz. The ear is most
sensitive between about 2 and 5 kHz, where the threshold drops a few decibels below 0 dB SPL. Two reasons are
mechanical. The ear canal is a tube of about 25 mm that is closed at the eardrum, and a quarter-wave resonance of such
a tube lies near $343 / (4 \times 0.025) \approx 3.4$ kHz. The eardrum and the middle ear are small and light, so they
couple poorly to long wavelengths at the bottom of the range and lose motion at the top.

Sensitivity also depends on level. The equal-loudness contours of ISO 226:2023 show that the ear needs much more
pressure at 50 Hz than at 1 kHz to hear the same loudness at a quiet level, and that the contours flatten as the
level rises. A mix balanced loud sounds thin when it is played quietly, and a mix balanced quietly sounds boomy when
it is played loud. Chapter 3 explains the phon, the sone and the A- and C-weightings that follow from this.

| Pressure | Level | What it means |
|---|---|---|
| 20 µPa | 0 dB SPL | Reference, close to the threshold at 1 kHz |
| 0.36 Pa | 85 dB SPL | Upper action value for an 8-hour working day (A-weighted) |
| 1 Pa | 94 dB SPL | Calibrator level |
| 2 Pa | 100 dB SPL | WHO limit for an audience over 15 minutes (A-weighted) |
| 20 Pa | 120 dB SPL | Discomfort for most listeners |
| 112 Pa | 135 dB SPL | Lower action value for peaks (C-weighted) |
| 200 Pa | 140 dB SPL | Exposure limit for peaks (C-weighted), threshold of pain |

The smallest level change a listener notices in a direct comparison is about 1 dB for broadband sound. Over minutes,
without a direct comparison, a few decibels go unnoticed, which is why levels creep upwards during a show.

## Masking and critical bands

A loud sound makes a quieter one inaudible when the two are close in frequency or in time. This is masking, and it
explains much of what a mix engineer does with an equalizer.

The inner ear analyses sound in overlapping bands, the critical bands. Two components inside one band compete, and
the louder one masks the quieter. Components in different bands are heard separately. One common model of the band
width is the equivalent rectangular bandwidth of Glasberg and Moore, $\mathrm{ERB} = 24.7\,(4.37 f / 1000 + 1)$ Hz.

| Centre | ERB | Relative width |
|---|---|---|
| 100 Hz | 35.5 Hz | 35.5 % |
| 500 Hz | 78.7 Hz | 15.7 % |
| 1 kHz | 132.6 Hz | 13.3 % |
| 4 kHz | 456.5 Hz | 11.4 % |
| 10 kHz | 1104.1 Hz | 11.0 % |

A third-octave band is 23.2 % wide, so above a few hundred hertz the ear's bands are about half as wide as the bands of
a third-octave equalizer. Below a few hundred hertz they are wider in relative terms.

Masking spreads further upwards in frequency than downwards, and the spread grows with level. A loud bass line
therefore masks the lower midrange of a vocal more than a loud vocal masks the bass. Masking also works in time. A
loud sound hides quieter sounds that follow it for some tens of milliseconds, and it hides sounds just before it for a
few milliseconds.

Three examples show where masking fails.

- **Distortion is not masked by other distortion of a different kind.** A loudspeaker with 1 % of mostly second and
  third harmonics does not hide an amplifier's much smaller share of high odd harmonics. Higher and odd harmonics
  are more audible than low and even ones, so a total figure such as THD says little about what is heard.
- **Structured noise is heard below random noise.** The quantization noise of an early digital delay, for example, was
  audible through the hiss of an analog equalizer. Today the remedy is dither, which turns the
  structured error into a smooth noise, and converters with enough bits that the error lies far below any analog noise.
- **Noise that rises with the signal is hidden only near the signal.** Modulation noise accompanies a note and is
  masked within about an octave of it, but a strong low note can let higher noise sidebands through.

Perceptual audio codecs such as MP3, AAC and Opus remove what masking hides, and they are the best-known application
of masking today. The same principle sets a limit for live work. An instrument that is masked by another in the same
band cannot be made audible by raising its fader alone without raising the whole band. A cut in the masking
instrument, or a different arrangement, usually works better.

## Localisation and the precedence effect

Two ears give the brain two cues for direction. The interaural time difference is the delay between the ears, which
reaches about 0.66 ms for a source at the side of a head with a radius of 87.5 mm. The interaural level difference
comes from the shadow of the head and matters above about 1.5 kHz, where the head is large compared with the
wavelength. The outer ear filters sound differently for each direction, which gives the brain cues for elevation and
for front and back.

When the same sound arrives twice from two directions, the brain does not hear two sources if the second arrival is
close enough in time. This is the precedence effect, also called the law of the first wavefront or the Haas effect.

| Delay of the second arrival | What a listener hears |
|---|---|
| Below about 1 ms | One source between the two, shifted towards the earlier one (summing localisation, as in stereo) |
| About 1 to 30 ms | One source at the first arrival. The second adds loudness and colour but no direction, even if it is somewhat louder |
| Above about 30 to 50 ms | The second arrival is heard as an echo |

The window depends on the signal. For clicks it closes after a few milliseconds, and for speech and music it stays
open for tens of milliseconds. A delayed arrival of 10 ms corresponds to 3.43 m of path difference, and 30 ms to
10.3 m.

Sound reinforcement uses the effect to keep the image on the stage. A delay loudspeaker halfway down a hall is
delayed so that its sound arrives a little after the sound from the main system, and listeners near it then localise
the source at the stage while hearing the level of the delay. Chapter 20 sets the delay times. The same effect also
explains why a reflection from a wall does not shift the image, and why one at 60 ms or more is heard as an echo.

## Measurement and listening

Every engineer meets the question why a system that measures well can sound wrong and the reverse. There are
several reasons, and the tools have answered some of them.

- **A microphone is one point, and a listener is two moving ones.** At one fixed point, reflections add and cancel
  into a comb of peaks and notches. A shift of a few centimetres changes the comb at high frequencies. Two ears and a
  head that moves let the brain form an average of the field around the head, and that average is what the listener
  calls the sound of the room.
- **An amplitude-only analyser misses time.** The real-time analysers of the 1980s showed level per third-octave
  band from pink noise and nothing else. A correction made from it could match two loudspeakers in level and leave
  them sounding different, because the equalizers changed phase as well. Today's dual-channel FFT analysers, such as
  Smaart, REW and Open Sound Meter, measure the transfer function with magnitude, phase and coherence, which answers
  much of this objection. Chapter 16 covers them.
- **One test examines one property, the ear all at once.** A sine sweep shows response, a THD test shows harmonics,
  and the ear judges both together with the time behaviour of the system.
- **Static signals hide dynamic faults.** A circuit can ring on a fast transient, and an amplifier can misbehave into
  a reactive loudspeaker load that a resistor on the bench does not present. Bursts and music-like test signals reveal
  what steady tones do not. Chapters 8 and 13 return to this.
- **Analysers once had less range than the ear.** Analysers of that time showed 30 to 60 dB on screen against about
  120 dB for the ear. A current FFT analyser behind a 24-bit interface shows over 100 dB, so this reason has mostly
  gone.

Two practices follow. A measurement for equalization is taken at several positions across the audience and averaged
by power, never by adding microphones electrically, because an electrical sum makes its own comb. A spatial average
of five to eight positions shows the trend that the audience hears, while a single position shows that seat only.
The second practice is a listening test after every correction, with known programme material, because the analyser
answers only the question it was asked.

### Listening tests that mean something

A listener can be trained, and an experienced engineer does hear faults that others miss. Such a listener deserves
the benefit of the doubt, and what sounds good is partly a matter of taste. One more finding has to be added. A
listener who knows which device is playing is influenced by that knowledge, and a louder version of the same sound
is usually judged better.

A fair comparison therefore has three properties.

1. **Matched levels.** The two versions are matched within about 0.1 dB, measured with a meter, because a difference
   of a fraction of a decibel is heard as a difference in quality rather than in level.
2. **Blind.** The listener does not know which version plays, and in an ABX test has to identify an unknown X as A or
   B often enough that chance is unlikely.
3. **Same conditions.** The same seat, the same programme and quick switching, because auditory memory for detail
   fades within seconds.

ITU-R BS.1116 describes formal tests for small impairments, and ITU-R BS.1534 (MUSHRA) for intermediate ones. A
sound check cannot follow either, but the three properties above can be kept with a level meter and a helper.

## How hearing is damaged

Sound damages the hair cells of the inner ear. A loud exposure first causes a temporary threshold shift. Sounds are
duller and quieter after the event, often with ringing in the ears, and hearing returns over hours to days. Repeated
exposure turns the shift into a permanent one, and the hair cells do not grow back. Tinnitus, a sound heard without a
source, can stay after a single exposure or develop over years. Research since about 2009 suggests that an exposure
whose threshold shift recovers fully can still damage the nerve connections of the inner ear, which impairs hearing in
noise. The damage therefore starts before a hearing test shows it.

The risk depends on level and time together. Most limits use the equal-energy rule, under which 3 dB more level halves
the allowed time. The rule turns any exposure into a daily dose, so that 15 minutes at 100 dB(A) carry the same energy
as 8 hours at 85 dB(A).

| Level, A-weighted | Time with the same dose as 85 dB(A) for 8 h |
|---|---|
| 85 dB | 8 h |
| 88 dB | 4 h |
| 91 dB | 2 h |
| 94 dB | 1 h |
| 97 dB | 30 min |
| 100 dB | 15 min |
| 103 dB | 7.5 min |
| 106 dB | 3.8 min |

A two-hour show at 100 dB(A) gives a daily exposure level of 94 dB(A), which is eight times the dose of the upper
action value. A crew member who stands near the stage for the sound check, the support act and the headliner has a
larger dose than anyone in the audience.

## Limits for crew and audience

### Crew

The EU noise directive 2003/10/EC protects workers, and it covers everyone employed at an event, including sound
engineers, bar staff and security. It sets three values for the daily exposure level $L_{EX,8h}$ and for the
C-weighted peak.

| Value | $L_{EX,8h}$ | Peak $L_{Cpeak}$ | What it requires |
|---|---|---|---|
| Lower action value | 80 dB(A) | 135 dB(C) | Information, training, hearing protection made available |
| Upper action value | 85 dB(A) | 137 dB(C) | Hearing protection worn, a programme to reduce exposure, marked areas |
| Exposure limit | 87 dB(A) | 140 dB(C) | Must not be exceeded at the ear, hearing protection included |

The directive asked for a code of conduct for the music and entertainment sector, and the EU later published
non-binding guidance for it. Austria transposed the directive with the ordinance on noise and vibration (VOLV), and
Germany with the LärmVibrationsArbSchV. Volunteers who are not employed may fall outside the directive's letter,
but its values are a sound measure for anyone who works near a PA.

### Audience

No EU law limits the level for an audience. The references in use are these.

- **WHO Global Standard for Safe Listening Venues and Events (2022).** It sets a limit of 100 dB $L_{Aeq,15min}$,
  measured continuously, together with live monitoring, free hearing protection, quiet zones, information for the
  audience and trained staff. It is a recommendation, and its value of 100 dB for 15 minutes equals the daily dose of
  the workers' upper action value.
- **DIN 15905-5 (Germany).** The norm for event technology rates the level over 30 minutes at the loudest audience
  position. The 2007 edition sets 99 dB(A) for the rating level and 135 dB(C) for peaks, with information and hearing
  protection required from lower levels. German courts and authorities use it as the state of the art, which makes it
  the DACH reference.
- **Austria.** No federal norm for audience levels is known to the author. Event permits under the event laws of the
  federal states can set conditions, and authorities often refer to the WHO standard or to DIN 15905-5.
- **Switzerland.** The ordinance on sound and laser (V-NISSG) sets binding limits for events, graded by level.

A practical policy for an SdWa5 event combines these. The level is logged at the mix position as $L_{Aeq,15min}$ and
$L_{Cpeak}$, the offset to the loudest audience position is measured once during the setup, the target stays below
100 dB(A) over 15 minutes at that position, and earplugs are free at the bar.

### Hearing protection

Foam earplugs attenuate a lot, but more at high than at low frequencies, so music through them sounds muffled and
many people take them out. Earplugs with a flatter attenuation, sold as musician's earplugs, keep the balance and
lower the level by about 10 to 25 dB depending on the filter. Custom-moulded plugs with interchangeable filters fit
best and are the usual choice for crew. A filter of 15 dB brings 105 dB(A) at the mix position down to 90 dB(A) at
the ear, and one of 25 dB to 80 dB(A). The rated attenuation is a laboratory value per EN 352-2 and the SNR of
ISO 4869-2, and a plug worn badly gives much less.

In-ear monitors can protect or harm. A well-sealed earpiece blocks the stage sound, so the monitor mix can be quieter
than a wedge mix for the same clarity. The risk is that a performer raises the mix until it masks the remaining
leakage and the crowd, and that a feedback squeal or a dropped wireless link reaches the ear at full level. A limiter
on every in-ear mix, a seal checked by the performer, ambient microphones instead of one earpiece taken out, and a
level that is measured rather than guessed make in-ear monitoring the quieter option.

## To verify in pass 2

- The upper frequency limit by age (12 to 16 kHz at fifty); check ISO 7029.
- The just noticeable level difference of about 1 dB; check psychoacoustics literature (Zwicker and Fastl, Moore).
- The ERB formula and constants; check Glasberg and Moore 1990.
- The temporal masking durations (tens of ms forward, a few ms backward).
- The precedence windows (1 ms, 30 to 50 ms) and the level a second arrival may have without shifting the image;
  check Blauert, *Spatial Hearing*, and Haas 1951.
- The ITD model with a head radius of 87.5 mm (Woodworth).
- The level-matching tolerance of 0.1 dB for comparisons; check ITU-R BS.1116 and AES literature.
- The editions and scope of ITU-R BS.1116 and BS.1534.
- The synaptopathy findings since 2009; check Kujawa and Liberman 2009 and later human studies.
- The values and duties of Directive 2003/10/EC (80/85/87 dB(A), 135/137/140 dB(C)), and the EU code of conduct for
  music and entertainment.
- The Austrian VOLV (title, BGBl. number) and the German LärmVibrationsArbSchV as transpositions.
- Whether unpaid volunteers of an association fall under the directive or the Austrian ASchG.
- The WHO Global Standard for Safe Listening Venues and Events (2022), its 100 dB $L_{Aeq,15min}$ and its features.
- DIN 15905-5, the current edition, its 99 dB(A) over 30 minutes and 135 dB(C), and its graded duties.
- The Austrian situation for audience levels, including the Salzburg event law and any ÖNORM.
- The Swiss V-NISSG values.
- The attenuation of musician's earplug filters and the standards EN 352-2 and ISO 4869-2.

## Sources

- ISO 226:2023, normal equal-loudness-level contours.
- ISO 7029, statistical distribution of hearing thresholds related to age.
- Glasberg, B. R., Moore, B. C. J.: Derivation of auditory filter shapes from notched-noise data, *Hearing Research*
  47, 1990.
- Blauert, J.: *Spatial Hearing*, MIT Press.
- ITU-R BS.1116 and ITU-R BS.1534.
- Directive 2003/10/EC on the minimum health and safety requirements regarding the exposure of workers to noise.
- WHO: *Global Standard for Safe Listening Venues and Events*, 2022.
- DIN 15905-5, event technology, sound exposure of the audience.
- EN 352-2 and ISO 4869-2, hearing protectors.
- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §9 (pp. 105–112) and
  §3.6 (pp. 29–32).
