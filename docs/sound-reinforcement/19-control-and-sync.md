# 19. Control and synchronization

> **Draft, pass 1.** This chapter was written from general knowledge and checked against reference literature for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers how devices on a show control each other, how MIDI, OSC and the remote interfaces of consoles
are used, how timecode keeps playback, light and video in step, and how a playback rig is built so that it does not
stop the show. It is about control data and time positions. Sample clocks, which keep digital audio itself in step,
are covered in [chapter 15](15-cables-connectors-networks.md#clocking).

## MIDI

The Musical Instrument Digital Interface (MIDI) was defined in 1983 to connect synthesizers, and it is still the
most widespread control protocol in music. On a show it switches presets of instruments and effects, recalls
console scenes, fires cues and carries timecode.

### Messages

MIDI 1.0 sends short messages of one to three bytes. A status byte names the type of message and, for channel
messages, one of 16 channels, and one or two data bytes of 7 bits each follow, so most values range from 0 to 127.

| Message | Meaning | Typical use on a show |
|---|---|---|
| Note On, Note Off | A key pressed or released, with velocity | Instruments, triggering samples or cues |
| Control Change | A controller moved, 128 controller numbers | Faders, effect parameters, footswitches |
| Program Change | Select one of 128 programmes | Recall a preset or a console scene |
| Pitch Bend, Aftertouch | Continuous expression | Instruments |
| System Exclusive | Manufacturer-specific data of any length | Device settings, backups, editors |
| Timing Clock | 24 pulses per quarter note | Tempo sync of sequencers and delays |
| MIDI Timecode | Time position in hours to frames | Following timecode, see below |

A device documents which messages it sends and understands in its MIDI implementation chart, which is the first
thing to read when two devices refuse to talk.

### Connections

The original connection is a 5-pin DIN cable carrying a current loop at 31 250 bit/s, isolated by an optocoupler at
the receiver so that MIDI cables do not create ground loops. With 10 bits on the wire per byte, a three-byte message
takes about 0.96 ms, and a chord of ten notes takes several milliseconds, which is why dense MIDI streams on one
cable can smear timing. A MIDI input, an output and a thru port pass the data on to the next device in a chain.

Today MIDI mostly travels in other ways.

- **USB-MIDI.** Class-compliant devices appear as MIDI ports on a computer without a driver, at a far higher speed
  than the DIN cable.
- **RTP-MIDI.** MIDI over Ethernet and Wi-Fi as a standardized network session, built into macOS and available on
  other systems, which replaces long DIN cables and merge boxes on a stage.
- **Bluetooth MIDI.** Convenient for a controller at a desk, but with a latency that varies too much for timing-critical
  use.

MIDI 2.0, published in 2020, adds higher resolution, two-way negotiation of capabilities and a new packet format.
It is backwards compatible, and devices that support it are still the exception in live sound.

### Common faults

- **No response.** The sender and the receiver are on different channels, the receiver ignores that message type,
  or the cable connects an input to an input.
- **Stuck notes.** A Note Off was lost, for example when a cable was unplugged during a note, and the note sounds
  until an All Notes Off message or a reset.
- **Loops.** A device that echoes its input to its output, connected back to the sender, creates a loop that floods
  both. The echo function (soft thru) is switched off on one of them.

## OSC and remote interfaces

Open Sound Control (OSC) sends named messages over a network, such as `/ch/01/mix/fader 0.75`, as UDP or TCP
packets. Its addresses are readable, its values can be floating point numbers or text, and it suits control from
software, tablets and show-control systems. Many digital consoles, playback programs and lighting desks accept OSC,
each with its own address scheme that its manufacturer documents.

Beyond OSC, most digital consoles and processors offer their own remote protocol, used by the manufacturer's app
and often documented for third parties. A tablet app connected over Wi-Fi lets an engineer set monitor mixes from the
stage, as chapter 18 describes, and a script can read meters or recall a scene. Such access goes over the control
network, which is separate from the audio network or at least on its own VLAN, and is protected like any other
network access, because a remote app can mute the whole system.

## Show control

A show with several departments, sound, light, video and stage machinery, needs them to change state together. Two
approaches are common.

- **A central cue list.** A playback or show-control program holds the cues, and each cue sends the commands for
  all departments, such as a scene recall by MIDI or OSC for the console, a cue number for the lighting desk and a
  start command for video. An operator advances the cues.
- **Timecode.** For shows that run to a fixed time line, such as a musical set to a backing track or a video
  mapping, every department follows a common timecode and fires its cues at set times.

MIDI Show Control (MSC) is a MIDI extension for cue commands between show-control devices. In practice OSC and the
programs' own network protocols have largely taken over its role.

## Timecode

### What timecode is

Timecode marks every frame of a time line with an address in hours, minutes, seconds and frames, as defined in
SMPTE ST 12-1 (and in an equivalent EBU form in Europe). It was made for film and video, and it serves on a show to
let every system know where in the time line it is.

| Frame rate | Use | Remarks |
|---|---|---|
| 24 fps | Film | |
| 25 fps | Video in Europe (PAL regions) | The usual rate for shows in Austria |
| 29.97 fps drop frame | Video in North America (NTSC regions) | Skips frame numbers to match clock time |
| 29.97 fps non-drop | Video in North America | Drifts from clock time |
| 30 fps | Audio-only work in North America | |

North American colour video runs at 29.97 frames per second rather than 30. Counting 30 frame numbers per second
at that rate drifts from the clock by 108 frames, or about 3.6 s, per hour. Drop-frame timecode skips the frame
numbers 0 and 1 at the start of every minute except every tenth minute, which removes exactly those 108 numbers
per hour. No frames are dropped, only numbers. All systems on a show must use the same rate and the same drop-frame
setting, or their cues drift apart.

### How it is carried

- **Linear timecode (LTC)** is an audio signal, a square-wave-like bit stream of 80 bits per frame, so 2000 bit/s at
  25 fps. It travels on any audio cable or audio channel, can be recorded on a track of the playback, and is the
  most robust way to distribute timecode. It is loud and harsh, and it is kept out of every audio path that reaches
  a loudspeaker.
- **MIDI Timecode (MTC)** carries the same information as MIDI messages. It sends four quarter-frame messages per
  frame, so a complete time address takes two frames to arrive, and a full-frame message locates directly.
- **Network timecode.** Several lighting and media systems distribute timecode over the network in their own
  protocols.

A device that follows timecode chases it, which means it locates to the incoming position and keeps running with
it. A short dropout in the timecode should not stop the show, so receivers have a freewheel setting that keeps
running for a set time without code.

### Timecode and clocks are different things

Timecode says where in the time line a system is. It does not say how fast the samples run. Two audio devices that
follow the same timecode but run on independent sample clocks still drift by a few samples per second relative to
each other, and they are locked by a word clock or PTP, as chapter 15 explains. A playback computer that sends
timecode and plays audio into the console's network uses the network clock for the audio and the timecode only to
tell the other departments where it is.

## Playback rigs

Backing tracks, click tracks and time-coded shows run from a computer, and a computer that stops in the middle of a
song stops the show. Productions that depend on playback build it redundant.

- **Two computers** play the same session in sync, the main and the backup, each into its own interface or network
  outputs.
- **A switchover** selects the backup when the main stops, either by an operator or automatically when the main's
  signal or timecode disappears.
- **The click and the cues** go to the in-ear mixes of the musicians and the musical director, never to the main
  system, and the sound engineer can mute the playback at once.
- **A known state.** Operating system updates, notifications, sleep modes and network services are switched off on
  show computers, and the session is tested on the same machines before the tour.

Smaller productions accept a single computer, and then at least keep the songs as separate files that can be
restarted quickly, rather than one long file.

## In the SdWa5 rig

At MARK Salzburg, the [video mapping machine](../../sdwa5-3d/docs/signal-chain.md#video-mapping-machine) received a
full-range line feed from output 7 of the DSP. The rig's documentation names no timecode or control connection
between audio and video for that event.

## To verify in pass 2

- The MIDI 1.0 data rate (31 250 bit/s), the optocoupler requirement and the timing of running status.
- RTP-MIDI as RFC 6295 and its availability on Windows and Linux.
- The date and scope of MIDI 2.0 (MIDI Association, 2020) and the Universal MIDI Packet.
- SMPTE ST 12-1 edition, the EBU equivalent, and the 80-bit LTC frame.
- The drop-frame rule (frame numbers 0 and 1 at each minute except every tenth).
- MTC quarter-frame structure and the full-frame message.
- MIDI Show Control as a MIDI recommended practice, and its current use.
- OSC 1.0 and 1.1 specifications.

## Sources

- MIDI Association: MIDI 1.0 Detailed Specification; MIDI 2.0 specifications, 2020.
- IETF RFC 6295: RTP Payload Format for MIDI.
- Wright, M.: The Open Sound Control 1.0 Specification, CNMAT, 2002.
- SMPTE ST 12-1, Time and Control Code.
- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §19 (pp. 371–393),
  §20 (pp. 395–408).
- SdWa5: [signal chain](../../sdwa5-3d/docs/signal-chain.md).
