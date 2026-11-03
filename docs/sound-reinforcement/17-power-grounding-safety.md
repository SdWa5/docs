# 17. Power, grounding and safety

> **Draft, pass 1.** This chapter was written from general knowledge and checked against reference literature for
> coverage. Standards, editions and figures are named but have not yet been verified against their sources. The
> list *To verify in pass 2* at the end names every claim that still needs one.

This chapter answers how a sound system is connected to mains power safely, how the power is distributed over the
phases, why hum and buzz appear and how they are removed without touching the protective earth, how equipment is
built into racks, and how a fault is found. It assumes the European system with 230 V and 400 V at 50 Hz. Electrical
installation work itself belongs to a qualified electrician, and nothing in this chapter replaces the national
rules.

## Two kinds of ground

Grounding serves two purposes, and keeping them apart is the key to the whole chapter.

- **Protective earth (PE)** connects every metal housing to earth, so that a fault in a device trips the circuit
  breaker or the residual current device instead of putting the housing at mains voltage. It protects people, and
  it is never interrupted.
- **Signal reference** is the common zero against which the audio signals are measured. It connects through the
  shields of the audio cables and inside the devices to the chassis, and through the chassis to PE.

Hum and buzz are problems of the signal reference. Their solutions all act on the signal side, never on PE.

## Mains supply

### Systems and connectors

Public supplies in Austria and Germany are TN systems, in which the neutral is earthed at the transformer. Older
installations combine neutral and earth in one conductor (PEN, TN-C) up to a point where they are separated
(TN-C-S), and newer ones carry them separately from the start (TN-S). A sound system needs separate N and PE from its
distribution onwards, which every CEE and Schuko outlet provides.

| Supply | Connector | Power at 230 V per phase |
|---|---|---|
| Single phase, 16 A | Schuko or blue CEE | 3.7 kW |
| Three phase, 16 A | Red CEE, 5 pins | 11.0 kW |
| Three phase, 32 A | Red CEE, 5 pins | 22.1 kW |
| Three phase, 63 A | Red CEE, 5 pins | 43.5 kW |

A mobile distribution box splits a CEE supply into the circuits of the system, each with its own circuit breaker and
with residual current devices (RCD). An RCD with 30 mA rated residual current protects every final circuit that people
can touch, and installation rules for shows, exhibitions and temporary structures require it. Switch-mode power
supplies can produce smooth DC fault currents that blind a common type A RCD, which is why distributions for event
technology increasingly use type B or type F devices where the rules ask for them.

### Phase balance and the neutral

A three-phase supply is used best when its load is spread evenly over the three phases. With linear loads, the
currents of balanced phases cancel in the neutral. Switch-mode power supplies, in amplifiers, LED fixtures and
computers, draw their current in short pulses, and the harmonics at three times the mains frequency add in the
neutral instead of cancelling. The neutral current can then exceed the phase current, which is a reason for neutral
conductors of full cross-section and for amplifiers with power factor correction (PFC), which draw a nearly sinusoidal
current. Sound and lighting are best fed from separate circuits, or separate distributions, from a common supply
point.

### Voltage drop

Long mains cables lose voltage. For a single-phase circuit, both conductors carry the current, and the drop is
$\Delta U = 2 \rho L I / A$. For a balanced three-phase load, the neutral carries no current, and the drop per phase
is half of that.

| Current | Length | Cross-section | Drop single phase | Drop three phase, balanced |
|---|---|---|---|---|
| 16 A | 25 m | 1.5 mm² | 9.3 V (4.1 %) | 4.7 V (2.0 %) |
| 16 A | 25 m | 2.5 mm² | 5.6 V (2.4 %) | 2.8 V (1.2 %) |
| 16 A | 50 m | 2.5 mm² | 11.2 V (4.9 %) | 5.6 V (2.4 %) |
| 32 A | 50 m | 6 mm² | 9.3 V (4.1 %) | 4.7 V (2.0 %) |
| 63 A | 50 m | 16 mm² | 6.9 V (3.0 %) | 3.4 V (1.5 %) |

An amplifier at full power can draw short peaks well above its average current, and a drop of a few percent at the
average becomes a larger dip at each peak, which lowers the amplifier's rail voltage and its headroom. Extension
cables are therefore kept short and heavy, which means 2.5 mm² for 16 A runs of more than a few metres. A cable drum
is fully unwound under load, because a coiled cable heats up.

### Generators

Outdoor events often run on a generator. Its rating in kVA must cover the peak demand of the system with a reserve,
because switch-mode loads and amplifier peaks stress a generator more than a resistive load does. Inverter
generators supply a cleaner voltage than simple ones. Sound runs best on its own generator, or at least separated
from the lighting and catering loads whose switching produces dips and spikes. The generator's earthing follows its
manufacturer's instructions and the local rules, and it is set up by someone qualified to do so.

### Checks before connecting

Every outlet is checked before use, and an outlet whose wiring is in doubt is not used. A socket tester shows a
missing PE or swapped conductors, a meter confirms 230 V between phase and neutral and 400 V between phases, and a
voltage tester finds a voltage between the housings of two devices, such as a guitar amplifier and a microphone
stand, before a performer bridges them with a hand and lips. Mobile distributions and cables are inspected at
regular intervals by a qualified person, as the national rules require.

### Switching on and off

Amplifiers are switched on last and off first. A console or a processor that starts up after the amplifiers sends
switching transients into live loudspeakers, and many amplifiers starting at once draw an inrush current that can
trip a breaker. The amplifiers are therefore switched on one at a time, or by a sequencer that delays each circuit
by a second or two. The shutdown runs in reverse.

### Clean and reliable power

Every console and processor is a computer, and an unstable supply can crash it. A small uninterruptible power supply
(UPS) on the console, the processors and the network switches keeps them running through a dip or a short
interruption, and gives time to shut them down cleanly in a real outage. It does not supply the amplifiers.

## Hum, buzz and ground loops

### How a ground loop forms

Two devices connected by an audio cable are also both connected to PE through their mains cables. Shield and PE
together form a loop. A magnetic field through the loop, or a small voltage between the PE contacts of two outlets,
drives a current around it, and part of that current flows through the shield of the audio cable. On an unbalanced
connection the voltage drop along the shield adds directly to the signal, and on a balanced connection it can still
enter through a device with the pin-1 problem, as chapter 15 explains. The result is hum at 50 Hz and its harmonics,
or a buzz with many harmonics.

### Grounding schemes

Studio installations often bring all signal grounds to one central point, but a portable system changes from
event to event and cannot be built that way. Portable systems combine the following measures instead.

- **Balanced connections everywhere** with the shield connected at both ends, and devices that bond the shield to the
  chassis at the connector (AES48). A ground loop then carries its current on the shield and the chassis, outside the
  signal circuit, and causes no hum.
- **Everything on one power distribution.** The devices of one system, the console, the processors, the amplifiers
  and the backline, draw power from one distribution, so that their PE contacts are at the same potential. This is
  the central-point principle in a form a portable system can keep, and it also covers the backline on stage.
- **Lifting the shield on the signal side** where a loop remains. A ground-lift switch on a DI box or a device
  input disconnects the shield at one end, and it breaks the loop
  without touching PE.
- **An isolation transformer** in the signal path, either in a DI box or as a line isolator, breaks the loop
  completely, because the transformer passes the signal magnetically and has no conductive path between its sides.

An adapter without a protective earth contact, or a cut earth conductor, would also break a loop on the mains
side. That is dangerous and against the rules. A device without PE is protected only by its insulation, and in a
fault its housing, and every shield connected to it, can carry mains voltage to the microphone in a performer's
hand. Protective earth is never lifted, neither by an adapter, nor by a broken contact, nor by cutting the conductor.

### Interference

Dimmers with SCRs, which chopped the mains waveform and produced a hard buzz in audio lines, have largely given
way to LED fixtures. Their switch-mode drivers produce interference at higher frequencies, often heard as a whine or
a buzz that changes with the brightness. The remedies have not changed. They are separate circuits for sound and
light, distance between signal and power cables, balanced connections, and crossing at right angles. Wireless
receivers and mobile phones are further sources, which chapter 10 covers.

## Racks

Equipment is mounted in 19-inch racks with a height unit of 1.75 inches (44.45 mm). A few practical points
keep a rack reliable.

- **Rear support** for heavy devices such as amplifiers, which otherwise bend their front panels in transport.
- **Ventilation** in the direction the devices blow, usually front to back, without blocking panels in the air path,
  and with space or a fan where the rack is closed.
- **Shock-mounted racks** for sensitive devices that travel.
- **Cable routing** with mains on one side and signals on the other, and with strain relief at the rear rails.
- **Labels** on every connector and every cable, matching the patch documentation (chapter 20).

## Finding faults

Faults come in two kinds, the absence of the expected signal and the presence of an unwanted one,
such as hum, noise, distortion or oscillation. The method is the same for both.

1. **Check the obvious first.** Every device is switched on, every fuse is intact, no channel is muted, no other
   channel is soloed, and the routing is what it should be. Experienced engineers are caught by this
   too.
2. **Change one thing at a time**, and undo the change if it did not help.
3. **Trace the signal.** A missing signal is followed from the source towards the output, an unwanted one from the
   output towards the source, by listening at each point with the console's solo, a headphone amplifier or a meter.
4. **Halve the chain.** In a long chain, checking the middle first tells which half holds the fault, and repeating
   the step on that half finds it in a few steps. With a digital console and a network, the meters at each stage
   make this fast.
5. **Substitute a known good part**, a cable, a microphone or a channel, and see whether the fault follows it.

Hum that disappears when one cable is unplugged at one end is a ground loop through that cable. Hum that stays when
every input is unplugged comes from the device itself or from its power.

## In the SdWa5 rig

The rig's [mains section](../../sdwa5-3d/docs/signal-chain.md#mains) applies this chapter to one event on a 16 A
three-phase CEE supply. It finds the circuit breakers to be the tightest limit of the rig, spreads the amplifiers
over the phases to balance them, puts the processors on the lightest phase, and switches on the processors first and
then the amplifiers one at a time, because four large amplifiers starting together would trip a 16 A breaker on
inrush alone.

## To verify in pass 2

- IEC 60364-7-711 (exhibitions, shows and stands) and IEC 60364-7-740 (temporary installations), and their RCD
  requirements.
- The Austrian rules for installations and event venues (ÖVE E 8101 and its part for temporary installations), and
  the inspection intervals for mobile distributions in Austria (and DGUV V3 for Germany).
- RCD types A, F and B and when event distributions need type B.
- Neutral current with switch-mode loads, the factor by which it can exceed the phase current.
- Generator sizing factors for amplifier and LED loads, and the earthing of mobile generators.
- Recommended maximum voltage drop for final circuits (3 % or 5 %).
- Voltage testers per EN 61243-3 and socket testers for Schuko outlets.

## Sources

- IEC 60364-7-711, IEC 60364-7-740, IEC 60309, ÖVE E 8101, AES48.
- Whitlock, B.: Balanced lines in audio systems, fact, fiction and transformers, *JAES* 43, 1995.
- SdWa5: [signal chain, mains](../../sdwa5-3d/docs/signal-chain.md#mains).
- Davis, G., Jones, R.: *The Sound Reinforcement Handbook*, 2nd ed., Yamaha / Hal Leonard 1989, §17.4 to §17.8
  (pp. 327–346).
