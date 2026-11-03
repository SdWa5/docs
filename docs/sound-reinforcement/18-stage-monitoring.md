# 18. Stage monitoring

> **Draft, pass 1.** This chapter was written from general knowledge and checked against reference literature for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers how performers hear themselves and each other on stage, who mixes what they hear, how a monitor
system is set up for the most gain before feedback, and how in-ear monitoring changes the job. The console's side of
monitoring, its sends and the placement of a monitor console, is in [chapter 11](11-mixing-consoles.md#monitors),
the physics of feedback in [chapter 6](06-sound-outdoors.md#feedback-and-gain-before-feedback), and the wireless
side of in-ear monitors in [chapter 10](10-wireless.md#in-ear-monitors).

## Why monitors

The main system points at the audience, and the stage is behind it. Without monitors, performers hear mostly the
reflections of the room and the backline next to them, which makes it hard to sing in tune and to play in time. A
monitor system gives each performer a mix of what they need to hear, at a level they can work with, and it is part
of the performance as much as the main system.

A good monitor mix is not only for comfort. Performers who
hear themselves play and sing better, and they do not raise their own level to compensate, which keeps the stage
quieter and the house mix cleaner.

## Ways to monitor

- **Wedges** are floor monitors angled up at the performer, usually a two-way box with a 12-inch or 15-inch driver
  and a horn, on a separate mix per position or per performer.
- **Side fills** are larger boxes at the sides of the stage that cover the whole stage area with a common mix,
  for performers who move around.
- **Drum fills** give the drummer a loud mix with low-frequency extension, often with a subwoofer, because the
  drum kit itself is loud.
- **In-ear monitors (IEM)** place the mix directly in the performer's ears, through wireless or wired bodypacks and
  earphones, and remove most of the monitor sound from the stage.

Most productions mix these. A band may use in-ear monitors for the singers and the keyboard, a wedge for a guest,
and a drum fill for the drummer who wants to feel the kick drum.

## Who mixes the monitors

On larger stages, a separate monitor console is the rule. The engineer at the front of
house cannot hear the stage, has to communicate by hand signals, and has a house mix to run. A monitor engineer at
the side of the stage, with a direct view of the performers, can listen to each mix, react at once and keep the
performers' trust.

Digital consoles have added two more options.

- **Front of house runs the monitors** on its own console, from sends that are independent of the house faders. On a
  small production, with a few mixes that change little during the show, this works well, and a tablet with the
  console's remote app lets the engineer adjust the mixes from the stage during the soundcheck.
- **Personal mixing.** Each performer adjusts their own mix, on a small mixer at their position or on a phone with the
  console's app, from a set of stems that the engineer prepares. This relieves the engineer, but it needs performers
  who know what they want and an engineer who keeps control of the overall level and the limiters.

On a shared stage with several acts, the monitor mixes for each act are stored as scenes and recalled at the
changeover, as chapter 11 describes.

## Gain before feedback on stage

A wedge points at the microphone it serves, at a short distance, which makes stage monitoring the hardest case of
feedback. Chapter 6 explains the loop. The measures that help are, in order of their effect, the following.

### Microphone and wedge placement

A directional microphone rejects sound from its null, and a wedge placed in that null contributes least to the
loop. The null lies at a different angle for each pattern.

| Pattern | Null from the front axis | Wedge position |
|---|---|---|
| Cardioid | 180° | Directly behind the microphone, one wedge |
| Supercardioid | about 125° | About 55° to either side of the line behind the microphone, two wedges |
| Hypercardioid | about 110° | About 70° to either side of the line behind the microphone, two wedges |

A performer who sings into the microphone with the wedge in front of them places the wedge behind the microphone,
which suits a cardioid. Supercardioid and hypercardioid microphones are more directional overall, but their wedges
belong to the sides, as chapter 9 shows. Real patterns differ from the ideal ones, especially at high frequencies,
and the manufacturer's polar plots show where the null lies for a given model.

The other placement rules follow from the loop. The microphone is close to the source, a performer's hand does not
cover the grille, which makes a cardioid behave more like an omnidirectional microphone, and the number of open
microphones is kept as low as the music allows.

### Polarity

A polarity reversal on a monitor output is worth a try, because each monitor mix is heard on its own and its
polarity does not interact with the other mixes. A reversal changes where the loop's phase adds, and it can
move the first feedback frequency to a place where the loop gain is lower. The gain it wins is usually small and
depends on the position, so it is a quick test during the soundcheck rather than a rule. Reversing the polarity at
the microphone would affect the house mix and any recording, so it is done on the monitor output.

### Ringing out

Ringing out finds the frequencies where the loop gain is highest and lowers them with an equalizer before the show,
so that the first feedback comes later. It used to be done by ear with a graphic equalizer per monitor mix, and a
current workflow combines measurement with listening.

1. **Equalize the wedge first.** A measurement of each wedge model, with the dual-channel analyzer of chapter 16,
   gives a corrective equalization that the processor stores per wedge. A wedge with a smooth response rings later
   than one with peaks.
2. **Raise the gain slowly** with the microphone at the performer's position, until the first ringing appears.
3. **Find its frequency** with the analyzer, or with the console's feedback display, and set a narrow parametric
   notch of a few dB at that frequency.
4. **Repeat a few times.** Three to five notches per mix are usually enough. Many more notches remove more of the
   voice than they win in gain, and the mix starts to sound thin.
5. **Leave headroom.** A performer moves, and the stage changes when the audience arrives, so the working level stays
   a few dB below the point where the last ringing appeared.

Automatic feedback suppressors, described in
[chapter 12](12-signal-processing.md#feedback-suppressors), can set the notches during ringing out, and some engineers
use them during the show as a safety net. They do not replace a well-placed wedge and microphone.

## In-ear monitoring

In-ear monitors seal the ear, which blocks most of the stage noise and lets the performer listen at a lower level
than on a wedge. They remove the wedges' contribution to feedback and to the noise on stage, which helps the house
mix too. They also bring their own practice.

- **Fit.** Earphones only work when they seal. Universal tips work for a short time, and custom-moulded earphones
  are more comfortable and seal better.
- **Ambience.** A sealed ear hears no audience and no room, which isolates the performer. One or two ambient
  microphones aimed at the audience, mixed in at a low level, bring the room back.
- **Level and limiters.** The earphones deliver high levels directly into the ear canal. A limiter in each mix, set
  with the performer, and a clear agreement on the level protect the hearing, as
  [chapter 5](05-hearing.md#hearing-protection) explains. The bodypack's volume is not a limiter.
- **Mono, stereo and mix.** A stereo mix with the instruments panned to their positions on stage is easier to listen
  to at a lower level than a mono mix, because the ear separates the sources by direction.
- **Failure.** A bodypack that loses its signal leaves the performer in silence. Spare packs, a check of the
  frequencies before the show and a wedge or side fill as backup on the stage are common practice.

### Latency

A performer hears their own voice through bone conduction at once, and the in-ear signal adds the latency of the
whole chain. Each digital stage adds some.

| Stage | Typical latency |
|---|---|
| Stage box with network to the console | about 0.5 ms to 1 ms |
| Digital console | about 1 ms to 2 ms |
| Network back to the stage | about 0.5 ms to 1 ms |
| Digital in-ear transmitter | up to a few milliseconds |

A total of a few milliseconds equals the travel time from a wedge at 1 m to 2 m, which takes 2.9 ms to 5.8 ms.
Musicians accept this, but a chain with plug-in processing or a slow wireless system can exceed it, and the
performer then hears a comb filter or a slight echo on their own voice. Chapter 1 explains where latency arises in
a digital system.

## Talking to the stage

The monitor engineer needs to hear what the performers hear, and to talk with them.

- **Listening.** A cue wedge next to the monitor console, and a set of the same in-ear monitors the performers use,
  reproduce each mix through the console's PFL or AFL bus, so that the engineer hears exactly what was sent.
- **Talkback.** A talkback microphone on the console routes to any mix, so that the engineer can speak to one
  performer without the audience hearing it.
- **Shout microphones.** The performers in turn have a microphone, often a switched one, that goes only to the
  monitor engineer's cue, so they can ask for changes without hand signals.

The monitor console needs a position with a clear view of the stage, and with in-ear monitors the view matters
even more, because the engineer sees a performer's request before hearing it.

## To verify in pass 2

- The null angles of real supercardioid and hypercardioid microphones compared with the ideal patterns.
- The typical latency of stage boxes, digital consoles and digital in-ear systems.
- What latency performers accept on in-ear monitors (figures of about 5 ms to 10 ms are often quoted).
- Typical wedge driver sizes and the use of coaxial wedges.
- Advice on in-ear levels and limiters from hearing conservation guidance.

## Sources

- Manufacturer documentation of digital consoles and in-ear systems, to be selected in pass 2.
- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §11.9 (pp. 178–181),
  §11.11 (pp. 186–189).
