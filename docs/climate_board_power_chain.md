# grow-tent-climate power chain — rebuild spec and bench procedure

The 24 V → 5 V → dual 3.3 V chain that replaces the DFR0379 which died on
**2026-08-14** when the new SCD41 was connected, plus the protection this board has
never had and the bench order that proves each stage before the next one is connected.

Written 2026-09-02, when the rebuild parts arrived and the fuse values had to be
re-derived against what actually turned up in the box.

**Scope:** electronics and power for `grow-tent-climate` only. The bus map (mux
channels, addresses, GPIOs) is not repeated here — it lives in the ESPHome config and
the device memory note. Part numbers and provenance for the whole grow build stay in
`D:\Claude\Knowledge\grow\hardware-inventory.md`, which remains the authority; this
file is the build sheet.

**Naming — the board, not the chip.** This buck is called **HW-083B** throughout, the
same way the one it replaces is called **DFR0379** and never "the LM2596 board".
`XL4015` is the regulator IC soldered to it. The board is what you buy, what you hold,
and what settles the question this procedure depends on — **not every XL4015 module is
CC/CV.** The plain ones have a single voltage pot, and shorting their output to set a
current limit destroys them. Calling it "the XL4015" hides exactly that distinction.
⚠ `HW-083B` is a generic silkscreen designation and sellers vary it. If the board in
hand prints something else, **record what it actually prints** and use that name — the
identity has to match the object on the bench.

---

## Why this rebuild exists

Every hardware failure on this board has been a **power** failure, on a system with
**no fuse anywhere**:

| Failure | Real cause |
|---|---|
| CN3903 mini modules, several | Bad joint or a short |
| Sensor-rail regulator, 2026-07-28 | SCD41 arrived DOA with an internal VDD↔GND short |
| DFR0379, 2026-08-14 | connecting the new SCD41 |

**Not one is a part being under-specified.** They are joints and shorts. Buying premium
silicon fixes none of them — a premium regulator driven into a dead short still dies.
The spend goes on **protection**, and the design input is that *a joint will
occasionally be bad*: the goal is that a bad joint costs a fuse and a lesson, not a
regulator and three weeks of downtime.

---

## The chain

```
120 VAC
  └─ switch.controller_tent            Sonoff plug, mains
      └─ Mean Well RSP-100-24          24 V 100 W — SHARED backbone,
          │                            also feeds tent-one and tent-two
          │
          ├─[PPTC 0.5 A]─ HW-083B   CV 5.00 V · CC ~3 A · both pots locked
          │                   │
          │                   ├─[PPTC 1.1 A]─ LM1117T-3.3 (I) ─── SENSOR RAIL 3.3 V
          │                   │                                    ├── 3.6 V zener 1N4729A → GND
          │                   │                                    ├── SHT41 Canopy      ch0
          │                   │                                    ├── SHT41 Flower      ch1
          │                   │                                    ├── SHT41 Stem        ch2
          │                   │                                    ├── SHT41 Controller  ch3
          │                   │                                    └──[PPTC 0.5 A]─ SCD41 ch4
          │                   │                                   (1N5819 across VDD→GND at every drop)
          │                   │
          │                   └─[PPTC 1.1 A]─ LM1117T-3.3 (II) ── ESP RAIL 3.3 V
          │                                                        ├── 3.6 V zener 1N4729A → GND
          │                                                        ├── ESP32 3V3 pin
          │                                                        └── TCA9548A VIN
          │
          └─ (tent-one and tent-two keep their own DFR0379s — untouched)
```

**Common ground is mandatory:** 24 V return, HW-083B GND, both LDO grounds, ESP GND and
every sensor ground bonded together.

**No firmware change.** `mux_co2` / channel 4 is already in the flashed config, so the
replacement SCD41 is a drop-in.

### Why the intermediate 5 V stage exists — keep it

It is **fault containment, not efficiency**. If an LDO ever fails short input→output,
this stage caps what lands on the 3.3 V sensor rail at 5 V instead of the full 24 V.
The SHT41s are 3.6 V absolute-max, so 5 V is survivable-ish and 24 V is certainly not.
It is also a hard requirement: **LM1117 maximum input is 15 V**, so it cannot be fed
from the 24 V backbone at all.

### Set the buck to 5 V, not 6 V, and never to match tent-one

tent-one and tent-two's DFR0379s feed their boards **directly**, so they are set to
board voltage. This one feeds LDOs and needs headroom above 3.3 V to regulate — setting
it to match tent-one will brown out the sensor rail.

5 V rather than the old ~6 V keeps LDO dissipation down (0.43 W on the sensor rail,
~27 °C rise on a bare TO-220) while staying well clear of the ~1.1 V dropout.

There is a second reason the 5 V stage is not negotiable: the HW-083B is
**non-synchronous**, and the classic death for that architecture is the high-side switch
shorting input to output. Set to 5 V with LDOs below it, the worst case that can reach a
3.6 V absolute-max sensor is 5 V. Set to 3.3 V feeding the board directly, it is the
full **24 V**.

### Two pots, not one — the HW-083B is CC/CV

⚠ **Confirm this before the bench work.** What follows is only valid on a CC/CV board.
**On a plain single-pot buck, shorting the output to set current destroys it.**

Both trimmers are marked **`W103`**, which is only the trimmer's own value — 10 kΩ. It
says nothing about which is which. Tell them apart by:

- **the PCB silkscreen** — look for `CV` / `CC` printed beside them;
- **the LED count** — two LEDs is a strong CC/CV tell;
- **turning each one unloaded** — only the CV pot moves the output voltage.

They are typically 3296W multiturn, roughly 25 turns end to end, and they **slip at the
ends rather than stopping hard**. So a pot that turns with no effect is not necessarily
broken or the wrong one — keep going, then check again.

**Set CV to 5.00 V** with nothing downstream.

**Set CC to ~3 A — deliberately high.** Short the output **through your ammeter** — the
meter in its 20 A range *is* the short — and adjust CC until it reads the target. The voltage
collapsing while you do this is correct; that is what constant-current means. Remove the
short and confirm CV returns to 5.00 V.

**⚠ The 20 A jack on the Mastercraft 052-0052-2 is dead (2026-09-14) — use the wire-shunt
method below instead.** Its fuse read `OL`, and a replacement 20 A fuse did not restore the
path: poking the red probe (V/Ω jack, ohms) into the **COM** socket reads 0.2 Ω, into the
**20A** socket reads `OL`. Same probe, same technique — that is a physically open shunt path,
most likely holder clips sprung open by the original failure. The µA/mA path is fine, proven
at 2.5 mA. Do not use it for this step: 3 A into a 400 mA jack kills that fuse instantly.

#### Setting CC with a wire shunt and a voltmeter (no ammeter needed)

**A length of wire IS a calculable resistor**, and `I = V / R` needs only the DC V range.
1/4 W resistors cannot do this job — 1 Ω at 3 A is 9 W — and the meter cannot measure a
sub-ohm shunt either: leads alone are ~0.2 Ω and the low range steps in 0.1 Ω, so **compute
the shunt from a wire table, never from an ohms reading.**

Copper 18 AWG is 0.00637 Ω/ft; **copper-clad aluminium (CCA) is ~1.6× that**, and speaker
wire is usually CCA — nick a strand and look for a silver-white core. Joining the two
conductors of a zip cord at the far end doubles the length and the volts you read.

**What was actually used, 2026-09-14:** 64 in of 18 AWG **CCA** speaker wire, both conductors
joined at the far end = 10.67 ft ≈ **0.109 Ω**. Landed on OUT+/OUT−, probes on the wire
itself at the terminals (not the screw heads — contact resistance is the same order as the
shunt), CC wound up until the shunt read **0.38 V ≈ 3.5 A**. Aim ~15 % high like this on
purpose: overshoot toward the module's ceiling is harmless, while an undershoot below
**2.2 A** means a faulted branch never trips its RXEF110 — the whole point of the setting.
With the shunt on, the buck's own terminals sit at 0.25–0.45 V; 5 V there means the shunt is
not really connected.

### Why CC goes high, and never to ~1.3 A

⚠ **Corrected 2026-09-06.** This sheet previously said ~1.3 A, reasoning that real draw
is ~750 mA peak so a tight limit is a tight guard. That reasoning is wrong, and wrong in
the one way that matters: **it would stop the 5 V branch fuses from ever tripping.**

**A polyfuse's hold current is not its trip current — it needs roughly 2× hold to open at
all.** So an `RXEF110` on a 5 V branch needs **≥ 2.2 A** before it does anything. Set CC
to 1.3 A and a dead short on that branch simply sits there: the buck holds in current
limit, the fuse runs warm and never opens, the rail stays down, and nothing clears. The
touch-test-for-the-hot-fuse diagnostic fails too, because no fuse tripped.

| CC setting | What happens on a shorted 5 V branch |
|---|---|
| ~1.3 A | Nothing clears. Fault persists silently, whole board down. **Avoid.** |
| **~3 A** | The branch `RXEF110` sees 3 A and opens in seconds. **The other rail keeps running** — the ESP stays online and HA tells you which branch died. |
| wide open (~5 A) | Same, faster, but maximum energy into the fault and into the sacrificial zener. |

3 A also sits comfortably above one LM1117's own ~1.3–1.5 A limit, so a single faulted
LDO puts *itself* into limit rather than dragging the buck into CC and collapsing the
healthy rail with it. Real combined draw is ~750 mA peak with both rails at maximum, so
3 A is nowhere near nuisance territory.

**A low CC is a bench tool for first power-up only — not for landing drops.**

⚠ **Corrected 2026-09-06, the same day it was written.** This section first said to wind
CC down to ~200 mA while landing drops at step 13. That is wrong twice over.

**The sensor rail is already behind LM1117 (I), which current-limits at ~1.3–1.5 A and
thermally shuts down.** A shorted or reversed drop is caught there — locally, at a lower
threshold than the buck could impose — and the buck's CC sits upstream of *both* LDOs, so
it cannot tell which rail is faulted anyway. **And 200 mA is below the board's own running
draw:** with the ESP rail up, WiFi bursts alone hit ~500 mA, so a 200 mA ceiling parks the
buck in permanent current limit and browns out the ESP. That is the *current limit set low
looks exactly like a broken board* trap, self-inflicted.

Where a low ceiling does earn its place is **step 12, first power-up of the LDO stage with
nothing downstream**, where expected draw is a few mA of quiescent current. A 100–200 mA
limit there turns a solder bridge into a sagging rail instead of a fault current. Even
that is belt-and-braces — step 11's unpowered ohm check should have caught it already.

Wind CC back to ~3 A before step 13, and leave it there in service, or the branch fuses
are decorative.

**One fault no CC setting helps with:** a short at the buck's own output terminals,
upstream of both branch fuses. Only the 24 V input fuse is in that path, and it needs
~4.5 A at 5 V to open — essentially wide open. That stretch of wire is short and inside
the box; ohm it before powering rather than trying to fuse around it.

**Lock both pots** — nail polish or threadlocker — **and photograph them into
`D:\Claude\Pictures\`.** The DFR0379's setpoint was lost when it died and nothing on
disk recorded it. There are now two settings to lose instead of one.

---

## Fuse map

Every polyfuse sits **in the box, upstream of its GX16 connector** — never out at the
sensor. That puts the connector, the whole drop cable and any joint in it inside the
protected zone.

**Every polyfuse goes in the positive conductor only. Never fuse a ground return.** A
tripped ground fuse leaves the load powered with no way home, and the current finds its
way back through the signal lines instead.

| Position | Value | Why this value |
|---|---|---|
| 24 V → HW-083B | **0.5 A** | Draw is ~180 mA peak at 24 V. Protects the shared backbone: a shorted HW-083B input would otherwise drag tent-one and tent-two down with it. |
| 5 V → sensor LDO | **1.1 A** | Sensor rail peaks ~250 mA, so it never nuisance-trips. Sized *up* for discrimination — see below. |
| 5 V → ESP LDO | **1.1 A** | ESP32 WiFi bursts hit ~500 mA; polyfuse thermal constant is seconds, so no nuisance trip. |
| SCD41 drop | **0.5 A** | Contains a dead short in under a second. |
| SHT41 drops ×4 | **0.05 A** | *Not fitted yet — see "Deferred".* One per drop, board-side, feeding pin 1 of that drop's connector — see below. |

### One fuse per drop, all board-side — revised 2026-09-13 for GX16

**Superseded:** the 2026-09-12 arrangement in which the three remote SHT41s shared a single
3.3 V terminal position (TB1.1) with the fuse split on the far side of it. That existed to save
screw-terminal positions. With a **4-pin GX16 per drop** there are no positions to save — every
drop carries its own V / GND / SCL / SDA — so the shared feed is gone.

**What replaces it:** each drop's 0.05 A PPTC sits on the board, its input on the sensor rail
and its output on **pin 1 of that drop's connector**. All four fuse inputs common at the
sensor-rail LM1117's output; each fuse output serves exactly one connector.

```
U9.OUT ─┬─[0.05 ch3]─ SHT41 Controller (on board, no connector)
        ├─[0.05 ch0]─ J1 pin 1 → Canopy
        ├─[0.05 ch1]─ J2 pin 1 → Flower
        ├─[0.05 ch2]─ J3 pin 1 → Stem
        └─[0.5  ch4]─ J4 pin 1 → SCD41
```

⚠ **The screw terminals STAY — changed 2026-09-14 (user).** Earlier notes had the GX16
*replacing* TB1–TB6. It does not: the drop now runs **board fuse → screw terminal → GX16 →
sensor**, with the terminal as the board's own landing point and the connector as the detach
point in the enclosure wall. Only the on-board **ch3 Controller SHT41 has no connector** — it is
hardwired, as it always was.

**Both halves are in the drawing (2026-09-14):** `J1`–`J4` are the **female panel** sockets, on
the box side because that is the powered side, and `P1`–`P4` are the **male cable** plugs whose
drop is hardwired at the sensor. J1/P1 = ch0 Canopy · J2/P2 = ch1 Flower · J3/P3 = ch2 Stem ·
J4/P4 = ch4 SCD41, matching the fuse map above. Each drop's Schottky and, on the SCD41, its
local caps sit **downstream of the connector**, at the sensor, where the spec puts them.

**Discrimination is unchanged and still the reason for the layout.** A fuse only discriminates
if it sits downstream of the branch. Four PPTCs feeding one common node are four resistors in
parallel — a short pulls through all of them at once and nothing says which drop did it.
Downstream, a short on Flower trips Flower's fuse only, and Canopy and Stem keep reading.

⚠ **The SCD41 does not share the SHT41 fusing.** It draws 205 mA measurement bursts and would
trip a 0.05 A on its first reading. Its own leg, its own **0.5 A**.

**Build points:**

- **Every fuse stays inside the box, upstream of its connector.** A fuse protects only what is
  downstream of it, so a fuse out at the sensor leaves the whole 15 ft drop and the zipper pass
  unprotected — and a PPTC in a 30 °C tent holds like a 0.04 A part instead of 0.05 A. It would
  also sit at 80–100 °C while tripped, right beside the sensor measuring air temperature.
- **Keep the fuse bodies ~5 mm apart.** A PPTC latches by self-heating; against its neighbour it
  becomes that neighbour's ambient and drags it toward tripping too.
- **Stand each PPTC 2–3 mm off the board** on its own leads. ABS softens near 95–100 °C and a
  tripped body resting flat on a drilled-out breadboard will dimple it. Solder is in no danger —
  Sn63Pb37 melts at 183 °C, SAC305 at ~217 °C.
- **Use 105 °C PVC or silicone** for the fuse pigtails and each drop's V lead. Common 80 °C PVC
  softens right in the tripped-body band. Polyolefin heatshrink at 125 °C is fine.
- **No hot glue anywhere near a fuse** — it melts at 60–80 °C. Zip tie or adhesive-lined
  heatshrink for strain relief.
- **Strain-relieve each drop at the box wall**, not on the connector's own clamp alone.

**Connector map:** J1 = ch0 Canopy · J2 = ch1 Flower · J3 = ch2 Stem · J4 = ch4 SCD41.
ch3 Controller is on the board and has no connector. Two spare pairs remain from the kit of six.

### Corrected 2026-09-02 — two values changed from the 2026-08-16 spec

**1. SCD41 drop: 0.2 A → 0.5 A.** The 0.2 A device is a few ohms. The SCD41's 205 mA
measurement bursts through that is a ~0.5 V drop, and those bursts run far too long for
the 10 µF local cap to ride out — it eats half the margin down to the SCD41's 2.4 V
minimum. The 0.5 A drops ~0.1 V and still opens well under a second on the failure that
actually happened, which is a **dead** VDD↔GND short pulling the LDO to its ~1.3 A
limit. What 0.5 A will not catch is a soft partial fault of a few hundred mA — accepted;
0.2 A barely caught that either.

**2. Sensor LDO input: 0.5 A → 1.1 A.** **Two polyfuses of the same value in series
cannot discriminate.** They see identical fault current and which one opens is a coin
flip — and if the upstream one wins, the whole rail drops and the per-drop fuse bought
nothing. Roughly a 10× ratio is wanted; 2.2× is what these values allow and it is real
selectivity. The 24 V fuse has no such problem: a full 1.3 A fault on the 5 V rail
reflects to only ~0.32 A at 24 V, well under its hold current.

### Reading the RXEF body print

The number on the body is **hold current × 100** — the same scheme as the AliExpress
variant codes, which is why three near-identical options sit in one dropdown.

| Marking | Hold | Where | Qty |
|---|---|---|---|
| `RXEF050` | 0.5 A | 24 V feed · SCD41 drop | 2 |
| `RXEF110` | 1.1 A | both LDO inputs | 2 |
| `RXEF005` | 0.05 A | SHT41 drops — on order | 4 |
| `RXEF200` | 2.0 A | nothing here — set it aside | 0 |

`050` and `110` are near-identical in the bag. **Read the body print, not the size.**

**Hold current is not trip current.** An `RXEF050` passes 0.5 A indefinitely and only
opens at around double that. That is why the SCD41's 205 mA measurement bursts sail
through it, and why the 0.2 A was rejected — see the correction above.

It also sets a floor under the buck's current limit: **nothing on the 5 V side can clear
a fault unless the supply can deliver ≥ 2.2 A into it.** That is the whole reason CC is
set to ~3 A and not to something tight. See *Why CC goes high* above.

### Deferred — the four SHT41 drop fuses

The 0.05 A devices were in an order that was stopped without notice; re-ordered
2026-09-02. **Leave those four drops unfused rather than substituting 0.5 A** — under a
1.1 A input fuse the ratio is far too tight to discriminate, so a substitute buys a coin
flip plus series resistance.

Running unfused there costs **isolation, not hardware.** The LM1117 current-limits at
~1.3 A and thermally shuts down; that is precisely the protection the old CN3903-class
modules never had, and the reason the spec moved to LDOs. Worst case all five sensors go
dark instead of one. Weigh that against the record: **four SHT41s, zero failures, ever.**
Both deaths in this system were SCD41s, and that branch is fused.

Fitting them later means breaking one wire per drop.

---

## Protection parts and where they go

| Part | Where | Purpose |
|---|---|---|
| PPTC polyfuse, RXEF | per branch, in the box | one shorted drop can't take the rail down |
| 1N4729A, 3.6 V zener ×2 | **each** 3.3 V rail, at that LDO's output | crowbar if an LDO fails short input→output |
| 1N5819 Schottky | across VDD→GND at **each** sensor, **cathode — the banded end — to VDD** | reverse-polarity clamp |
| 10–22 µF electrolytic + 0.1 µF ceramic | both LDOs, input **and** output, close to the pins | LM1117 stability |
| 10 µF + 0.1 µF ceramic X7R ≥16 V | at the SCD41 pins | supplies the 205 mA pulses locally |
| **1.5KE6.8A TVS** | **across the HW-083B's own OUT+ / OUT− terminals**, cathode (band) to OUT+ | clamps a buck high-side short so 24 V never reaches the LDOs |

**No tantalum anywhere** — it fails short on overvoltage.

The LM1117 output cap needs **some ESR**; a small pure-ceramic output cap alone can make
it oscillate. Use the electrolytic-plus-ceramic pair, not ceramic alone.

**Use 3.6 V for the clamp, not 3.3 V.** A 3.3 V clamp on a 3.3 V rail sits at its knee
and leaks continuously. If 3.6 V is ever unobtainable, 3.9 V is the better fallback than
3.3 V — a weaker clamp beats one that conducts all day.

The zener is **sacrificial and only works if an upstream fuse trips**. Expect to replace
it after any event; an overloaded zener usually fails short but can fail open.

### Both rails get a clamp, not just the sensor rail — corrected 2026-09-12

The original sheet put a 3.6 V zener on the **sensor** rail only, reasoning about the four SHT41s
and their 3.6 V absolute maximum. That reasoning was never applied to the other rail, and it
applies identically: **the ESP32's VDD33 absolute maximum is also 3.6 V.** A shorted LM1117 on the
ESP rail puts 5 V on the ESP32 and kills it — the TCA9548A survives (1.65–5.5 V), so the ESP is the
part at risk, and it is the one whose loss means the board is dead until it is replaced and
reflashed.

**D9, a second 1N4729A, cathode to the ESP rail, anode to ground** (user, 2026-09-12). Same
sacrificial behaviour as D7: it conducts hard, holds the rail down, and will likely die while the
1.1 A PPTC opens. That is the intended outcome.

**Why it stays at the LDO output and never at a sensor.** A clamp works on the node; the sensor
10 ft down a drop sits on that same node and is protected, because in a fault essentially all the
current runs through the zener at the board and only the sensor's microamps run down the cable.
Move the clamp to a sensor end and both things break: fault current would have to travel the drop
to reach it, so cable resistance lets the board end rise above 3.6 V anyway, and the other drops
would have no clamp at all. This is the sheet's own rule — **fuse at the source end, protection
diode at the load end**. The zener is a rail clamp, so it is a source-end part; what each remote
sensor gets at its end is its own 1N5819.

### The 5 V clamp — added 2026-09-11

**1.5KE6.8A, across the buck's output terminals, band to OUT+.** It is there for one failure:
the XL4015 is non-synchronous, and that architecture's catastrophic death is the high-side
switch shorting VIN onto VOUT — which would put **24 V on the 5 V bus**, past the 50 V input
caps and into LM1117s rated 15–20 V absolute maximum. A shorted LDO then puts that on 3.6 V
sensors.

- **5.8 V standoff**, so it does nothing at 5.00 V; breakdown 6.45–7.14 V, clamps ~10.5 V.
- **Sits across the buck output, upstream of both 1.1 A PPTCs**, so one part covers both rails,
  and the loop is as short as it can be.
- **It is a clamp, not a fuse.** It does not interrupt the fault — it drags the bus down until
  the **0.5 A PPTC at the Mean Well** opens. Expect it to **fail short** doing that, and expect
  to replace it. That is the intended outcome: a shorted TVS is an obvious diagnosis and a 20¢
  part instead of two LDOs and five sensors.
- **A 1 W zener from the kit will not do this job** — it goes open at ~0.16 A, and open protects
  nothing. Choose the standoff, not the wattage: 6.8 V belongs on a 5 V rail and cooks on 12 V.
- Probability of the failure it guards is **low** (this board's own two regulator deaths both
  ended dead-not-pass-through, and it runs at ~6 % of the module's rating). It is fitted for the
  asymmetry, and because a bench mis-wire reaches the same rail.

### On the Schottky-needs-a-fuse rule

The original spec says a Schottky without a polyfuse in series just cooks itself. That
was written against the old topology, where the rail came off a CN3903-class module with
no real short protection and nothing upstream to stop the current. **It does not hold the
same way now:** an LM1117 current-limits and thermally shuts down, the 1.1 A input fuse
opens in about a second, and a 1N5819 is rated 1 A continuous with 25 A surge.

So fit all five, including on the four unfused SHT41 drops — worst case they convert a
destroyed sensor into a tripped rail fuse. Note also that reverse polarity is a
**crimping** error, and those four drops are not being re-crimped: they were built in
July, ohmed pin-for-pin, and have run since. The only new cable is the SCD41 drop, and
that branch is fused.

---

## Pre-power checks on a finished board

The bench sequence assumes the board grows in stages, so step 11 only asks for Vin→GND and
Vout→GND. **This board was built complete before any of it was metered** (2026-09-14), so the
short hunt has to cover every net at once. All of it is **unpowered, buck disconnected from the
board's 5 V input**, meter on OHM with the leads shorted and **Relative** pressed first.

**Every reading starts low and climbs** — you are charging the electrolytics through the meter.
Take the settled value, and reverse the probes on anything that looks wrong before believing it.

| Probe between | Expect | Near 0 Ω means |
|---|---|---|
| 5 V bus ↔ GND | kΩ+ | backwards electrolytic or solder bridge |
| Sensor 3V3 ↔ GND | kΩ+ | same, or a reversed Schottky |
| ESP 3V3 ↔ GND | few hundred Ω to kΩ | same |
| **Sensor 3V3 ↔ ESP 3V3** | **high / `OL`** | **the two rails are bridged — that undoes the rail split, which is what designs out the 2026-07-27 bus jam** |
| Each LM1117 tab ↔ its middle pin | ≈ 0 Ω | (expected — tab IS Vout) |
| Tab ↔ tab | high | the tabs are touching: the two 3.3 V rails are shorted together |
| GPIO21 ↔ mux SDA · GPIO22 ↔ mux SCL | **≈ 200 Ω** each | resistor bridged. `OL` instead = dry joint |
| SDA ↔ SCL | high | a bridge between the two I²C lines |
| Buck OUT− ↔ ESP GND, mux GND, both LM1117 pin 1, each drop ground | **< 1 Ω** | (expected — `OL` here is the fault: the ground star is not common) |

Two things that look like faults and are not: the **ESP32 devkit gives drifting, asymmetric
numbers** because the meter's test voltage leaks through its protection diodes and its own
AMS1117; and **any reading that changes when you swap the probes is a diode**, not a short.

**A missing TVS does not block bring-up.** D8 is a clamp — inert until a fault arrives — so the
board powers up and commissions without it. Fit it when it lands.

## I²C — the resistors, not the map

The channel map lives in the ESPHome config and the device memory note. What belongs on
a build sheet is the passives, because they are easy to leave off and invisible in YAML.

| Where | Part | Why |
|---|---|---|
| ESP32 GPIO21 → TCA9548A SDA | 200 Ω series | limits fault current on the main bus |
| ESP32 GPIO22 → TCA9548A SCL | 200 Ω series | same |
| TCA9548A A0/A1/A2 → GND | — | sets the mux address to `0x70` |
| each drop's SDA / SCL | 100 Ω series, optional | limits fault current into that one mux channel |

**Pull-ups:** every SHT41 breakout and the SCD41 board carries its own 10 kΩ pair, so
each mux channel is already pulled up by the sensor sitting on it. The bus runs at
**50 kHz** deliberately — long cable in a wet tent — and that is set in firmware, not
here.

---

## Bench sequence

Order carries the safety. **Nothing is connected downstream of a regulator that has not
been metered unloaded first.**

| # | Step | Expect |
|---|---|---|
| 1 | ~~Adjust-up test on the DFR0379~~ — **DONE 2026-09-06** | **Genuinely dead.** Would not come up off 1.23 V with nothing downstream. No spare buck from it. |
| 2 | Ohm the SCD41 that was connected 2026-08-14 | kΩ+ VDD↔GND ⇒ that sensor is alive and the buck died of something else |
| 3 | Identify the two pots on the HW-083B — silkscreen, LED count, or turn each unloaded | only the CV pot moves the output voltage |
| 4 | ~~Set CV, nothing downstream~~ — **DONE 2026-09-14** | **5.00 V set** (user-metered) |
| 5 | ~~Set CC by shorting the output **through the ammeter**~~ — **DONE 2026-09-14 via the wire shunt** (the 20 A jack is dead; see §"Setting CC with a wire shunt") | **~3.5 A set**, read as 0.38 V across a 0.109 Ω CCA shunt · CV returns to 5.00 V when the shunt is removed · **not 1.3 A — see above** |
| 6 | Lock **both** pots; photograph them | — |
| 7 | ~~Continuity-check both LM1117s loose~~ — **MOOT 2026-09-14, the board was already fully soldered**; superseded by §"Pre-power checks on a finished board" | tab ↔ middle pin ≈ 0 Ω — in circuit this now only confirms the Vout NET, not the part |
| 8 | Ohm the **new** SCD41 bare, all wires off, before any diode is near it | kΩ+ VDD↔GND — anything near 0 Ω does not get connected |
| 9 | Ohm every drop cable **pin-for-pin** | each conductor to its own pin at the far end, no cross-pairs |
| 10 | ~~Build the LDO stage: caps, fuses, clamp, Schottkys~~ — **DONE 2026-09-14** | Built complete **except D8, the 1.5KE6.8A TVS** (on order). Both 200 Ω I²C resistors, all caps, fuses, zener and Schottkys are in |
| 11 | **Unpowered**, ohm Vin→GND and Vout→GND at each regulator — on a finished board run the fuller table in §"Pre-power checks on a finished board" | kΩ+. Near 0 Ω is a backwards electrolytic or a solder bridge — find it now, not with 5 V on it |
| 12 | Power up with **no sensors connected** | each rail 3.25 – 3.35 V |
| 13 | Land the drops **one at a time**, re-metering after each | rail holds 3.3 V after every drop |
| 14 | Boot with logs, read the I²C scan | 0x70 + 4 serials + 0x62 on ch4 · `Tent CO2` publishing within 30 s |
| 15 | FRC outdoors, powered ≥ 3 min | — |

**Step 1 is closed (2026-09-06).** The DFR0379 was tested with nothing downstream and would
not come up off the 1.23 V reference — it is genuinely dead, not a lost setpoint, so there
is **no spare buck** from it. One unit only, the climate board's; tent-one's and tent-two's
are untouched and still good. The rebuild runs on the HW-083B, of which there are four.

**Step 2 is still free and still not run** — it could yet exonerate the 08-14 SCD41.

⚠ **Step 5 is only safe once step 3 has confirmed the board is CC/CV.**

On step 12: a fixed-output LM1117 self-biases through its internal divider, so an
unloaded reading is trustworthy. If it reads high, hang ~1 kΩ across the output to
settle it. Optionally wind CC to ~100–200 mA for this one step — with nothing downstream
the expected draw is a few mA, so a solder bridge sags the rail rather than being fed.
**Wind it back to ~3 A before step 13**; the ESP will not run at 200 mA.

Step 13 is not ceremony — **one-at-a-time reconnection is the diagnostic that actually
found the fault on 2026-07-28.** The protection during it is **the sensor LM1117's own
~1.3–1.5 A limit and thermal shutdown**, not the buck. Do not try to guard this step by
winding CC down: the ESP is running by now, and a low ceiling browns it out instead.

On step 14: a serial on the wrong channel means **fix the wiring, not the YAML**. And if
all eight SHT41 entities come up `unknown` rather than `unavailable`, the ESP is
connected fine and it is an I²C setup failure — that distinction has saved a wrong
diagnosis before.

On step 15: tent intake is **living-room air** (exhaust goes outside), so the tent never
breathes 420 ppm and the in-tent guard blocks the button anyway. FRC happens outdoors at
the start of every grow. Afterwards, cross-check `temperature_offset: 4.0` against the
adjacent Flower SHT41 — the four agreeing to 0.29 °C are the reference.

---

## Part sizing and physical placement — settled 2026-09-10

### Where the buck lives, and therefore where the 0.5 A goes

**The HW-083B goes in the tent, next to the ESP32** (user, 2026-09-10). That settles the open
"15-foot run" question the right way round: **the 15 ft carries 24 V, not 5 V** — one fifth the
current in the run, and the buck regulates at the load instead of 15 ft upstream of it, so wire drop
stops mattering. 22 AWG is fine over that distance behind a 0.5 A fuse.

**The 0.5 A PPTC goes at the Mean Well end, outside the tent** — first thing after the +24 V terminal,
before the run starts. Four reasons, and the first is the one that counts:

1. **A fuse protects only what is downstream of it.** At the buck, the whole 15 ft is unprotected — a
   chafe or a pinch at the tent zipper draws straight off a 100 W supply with nothing limiting it.
   That run is the most exposed part of the chain.
2. It is guarding the **shared backbone**, so it must sit where this branch taps it, or a fault here
   drags tent-one and tent-two down.
3. **PPTC hold current derates with ambient.** 0.5 A in a 30 °C tent behaves like ~0.4 A; outside it
   holds its nameplate. (Either survives the ~180 mA draw, but cooler is better.)
4. It is self-resetting, so put it where it can be inspected without opening the tent.

Keep the unprotected stub short: solder the PPTC lead onto the terminal tail and heatshrink over it.

### Fuse at the source, protection diode at the load

The same rule decides the drop wiring, and it lands differently for the two parts:

| Part | Goes at | Because |
|---|---|---|
| Drop PPTC | **Board end** | It protects the drop cable, so it must be upstream of it |
| 1N5819 Schottky | **At the sensor, across its own VDD/GND pins** | It only catches a reversed drop if it sits on the node whose polarity can be wrong. The board's rails are correct by definition, so a diode there would never conduct and would protect nothing |

The drawing already has each Schottky on its sensor's own pins; the physical part must match — soldered
across the breakout's VIN and GND pads, out at the sensor. Not at the board end, and not in the
GX16 shell.

### Capacitor and diode values

**Per LM1117T-3.3, four capacitors:**

| Position | Part | Rating | Reasoning |
|---|---|---|---|
| Vin ↔ GND | 10 µF electrolytic | **50 V** | The rail is 5 V, but the **HW-083B is non-synchronous** — a high-side short puts **24 V** on it. A 25 V part sitting at 24 V vents. Rate input caps for the fault voltage upstream, not the nominal rail |
| Vin ↔ GND | 0.1 µF ceramic | ≥16 V | HF bypass, at the pin |
| Vout ↔ GND | 22 µF electrolytic | **16 V** | Worst case on this node is 5 V (an LDO failing short), so 16 V is 3× the fault. Smaller can, and **more ESR**, which the LM1117 wants |
| Vout ↔ GND | 0.1 µF ceramic | ≥16 V | HF bypass, at the pin |

- **22 µF, not 10 µF, on the output.** The datasheet's 10 µF is the *tantalum* figure; aluminium ESR
  rises as it cools, so aluminium wants 22 µF. No tantalum anywhere — it fails short on overvoltage.
- **The output electrolytic is a stability part.** A pure-ceramic output can fall below the LM1117's
  minimum ESR and oscillate. Do not "tidy" it into a 10 µF MLCC.
- **The input cap does real work here** even though the buck is inches away, because a **PPTC sits in
  series** ahead of it — a fuse is resistance, so the buck's output caps are not electrically at the pin.

**Physical placement on the TO-220** (printed face toward you, legs down): **pin 1 left = GND, pin 2
middle = Vout, pin 3 right = Vin, and the tab is tied to pin 2 — live at 3.3 V.** Input pair between
pins 3 and 1, output pair between pins 2 and 1, ceramics with ~5 mm of lead right at the pins,
electrolytics within 1–2 cm, **stripe to pin 1**. **Return all four capacitor grounds to pin 1 itself**,
not to separate points on the ground bus, or input ripple current crosses that stretch of bus and shows
up on the output. Order along the path: fuse → Vin node (input pair) → regulator → Vout node (output
pair) → drop fuses. Keep the two tabs clear of each other and of the bus — they are **different nets**.

**Sensor Schottkys: 1N5819**, 40 V / 1 A / 25 A surge. Schottky rather than a 1N400x for the ~0.35 V
drop; the 1 A rating is what lets it survive until the upstream protection acts (LM1117 limits at
~1.3–1.5 A then thermally shuts down; the 1.1 A PPTC opens in about a second). The 40 V is incidental.

**SCD41 local pair: 10 µF + 0.1 µF, X7R, take the highest voltage rating the kit offers.** This is the
opposite of the electrolytic advice above and for a different reason: **MLCC capacitance collapses
under DC bias**, worse in smaller and lower-rated parts, so a bigger-bodied part keeps more of its
nameplate at 3.3 V. **Check the 10 µF is X7R and not Y5V/Z5U** — assortment kits sometimes use Y5V for
larger values, and a Y5V part would be 10 µF in name only, exactly where a 205 mA pulse needs it.

### Open drawing item found while re-verifying

**The two regulators are not wired alike.** The ESP-rail LM1117 has its input capacitors on the Vin
node, downstream of its 1.1 A fuse — correct. The **sensor-rail LM1117 has no capacitor at its Vin pin
at all**: that node contains only the fuse lead and the pin, and the three capacitors that look like its
input caps sit on the **5 V bus upstream of the fuse**. They are useful bulk there, but they are on the
far side of a PPTC's resistance, so that regulator has no local input decoupling. Add a 10 µF + 0.1 µF
pair across its Vin↔GND to match the other rail.

---

## Traps

### Current limit set low looks exactly like a broken board

CC/CV boards often ship near minimum current. You will set 5.00 V unloaded, connect the
LDOs, and watch the rail sag to 2 V or wander — which reads as a dead voltage pot or a
faulty module. It is neither. **It is in current limit. Turn CC up.**

### A polyfuse latches. It does not blow.

It goes high-resistance, runs hot while powered, and **resets itself once you remove
power and it cools.** A rail that comes back after a power cycle has therefore *not*
healed — the fault is still there and it will trip again.

The useful corollary: **the tripped fuse is the hot one.** Touch-test them to find the
faulted branch before you start unplugging things.

### The Schottky inverts the standing VDD↔GND test

Once a 1N5819 sits across the rail, the meter's own test voltage forward-biases it.

- **Red lead on VDD, black on GND** reverse-biases the diode. This is the valid test and
  it should still read **kΩ+**.
- Leads swapped reads ~0.3 V and low ohms. **Correct, not a fault.**
- Low **both** ways means the diode is in backwards.

A false "shorted sensor" call is a mistake this system has already made. Note the
standing rule still applies to the **bare** sensor, with all wires off, before any diode
is fitted.

### The LM1117 pinout is not the 7805 pinout

Printed face toward you, legs down:

| Pin | LM1117 | 7805, for contrast |
|---|---|---|
| 1 · left | **GND** | Vin |
| 2 · middle | **Vout** | GND |
| 3 · right | **Vin** | Vout |
| tab | **Vout** | GND |

Wiring it from 78xx muscle memory puts the input on the ground pin. The continuity check
in **step 7** confirms both the pinout and which way round the part is, before any power,
for free.

Order by `LD1117V33` or `LM1117T-3.3` — the **V** suffix is what means TO-220.
`AMS1117-3.3` is almost always SOT-223 SMD.

### The tab is live at 3.3 V

- Never bolt it to a grounded chassis or heatsink — that shorts Vout to GND.
- **Never put both LDOs on a shared heatsink.** That ties the sensor rail to the ESP rail
  through the tabs and destroys the entire reason they are separate.
- Neither needs a heatsink at this load. Give both tabs clearance from each other, from
  stray wire and from the enclosure.

### Never USB and external 3.3 V together

Feeding the ESP32's 3V3 pin bypasses its onboard AMS1117. Two regulators fighting one
rail — unplug the PSU before any serial reflash, or stay on OTA. ~2.6 V floating on VIN
from body-diode backfeed is normal.

### `switch.controller_tent` is a common-mode point

It feeds the one PSU, so cutting it drops all three tent boards together. **Never toggle
it during a feed/flush or a flash.**

### The capacitor kit derates voltage as capacitance rises

Only relevant at one place in this build: **bulk cap added on the 24 V input to the
HW-083B needs ≥35 V**, and the BOJACK kit's big values are commonly 16–25 V with no
rating in the listing. Read the sleeve. The HW-083B ships with its own input electrolytic,
so adding one is optional. Everywhere else in this chain is 5 V or 3.3 V and the trap
does not bite.

---

## The wiring drawing lives in Fusion 360

The board's wiring drawing is a Fusion 360 model, not a paper schematic: **"Grow Tent Climate
Schematic"** (project Aqua, folder Tent), built 2026-09 from the user's own part models, every
part labelled, the wiring split into five show/hide components — power source · ESP-32 to
TCA9548A · rectifier diodes · sensor logic · sensor power. It is the drawing the board is wired
from, so its correctness matters as much as this sheet's.

**Read it orthographic, from the front.** Wires sit on a plane 2.5 cm in front of the parts; a
perspective view parallaxes every wire end off its terminal.

**Connection = one fused body, no seam. Crossing = the crossed wire is cut and abuts the
continuous wire on both sides**, with small stub bodies filling the gaps between adjacent
crossing wires. A wire end touching another wire is therefore *never* a connection — including
black on black.

**Breadboards:** the bus strips are being drilled out, so every connection must be an explicit
wire. The model already does this; keep it that way.

### Review 2026-09-06 — what the drawing got wrong

The model was machine-traced (89 wire bodies → 42 nets, every free end matched to a pin) and
each finding confirmed on a front render. **Correct as drawn:** the 24 V chain and its fuse,
both LM1117 pinouts, ESP D21→SDA / D22→SCL, LM1117 (I) → ESP 3V3 + mux Vin, fuse→sensor→Schottky
order on all five drops, all four electrolytic polarities, ch3 = the on-board Controller SHT41.

Open as of the review. (The tickable fix list is a private page; its URL is in the memory store,
not here, because this repo is public.)

| # | Finding | Fix |
|---|---|---|
| 1 | The two old DC-DC mini step-down modules are still drawn **in series** between the HW-083B and both LM1117s, their outputs drawn as 3.3 V — an LM1117 fed 3.3 V cannot regulate | Remove them and their two input electrolytics; buck → 1.1 A PPTC → LM1117 Vin, twice. **DECIDED 2026-09-10 — not deliberate; user removed both modules and their caps.** The deletion alone is not the whole edit — see §“After deleting the two mini modules” below. |
| 2 | Schottkys on the **SCD41** and the **on-board SHT41** are reversed — anode to VCC, a short across the rail at power-up | Banded end to VCC / Vin. The three remote-SHT41 diodes are right; copy them |
| 3 | SCD41 SDA lands on `SC4`, SCL on `SD4` | `SDA → SD4`, `SCL → SC4` |
| 4 | The sensor-ground bus terminates only at screw terminal 4 pin 3, and crosses the regulator ground bus twice without joining | Join it to the star point. **Pending: is that terminal the star point?** |
| 5 | Right output ceramic has both leads on GND · zener unwired · left 1.1 A PPTC unwired, so LM1117 (I) is unfused | Ceramic: one lead to LM1117 (II) Vout. Zener: band to Vout, other lead to GND. PPTC: in series with LM1117 (I) Vin |
| 6 | All five drop fuses labelled 0.5 | SCD41 only. The SHT41 drops are 0.05 A, deferred |
| 7 | Not drawn: SCD41 local caps, the 200 Ω main-bus series pair, A0–A2 → GND | Add |

Plus legend and drawing-clarity items, on the page.

#### Re-trace of v44 — 2026-09-10

The model was re-traced at **v44** (the review above was v31): 97 wire bodies → 55 nets, each net
checked for colour consistency (no net mixes two wire colours, which is the signal that the
crossing/continuation reading is right). Status of the seven findings:

| # | Finding | v44 status |
|---|---|---|
| 1 | Two mini step-down modules in series | **Still drawn** — removal decided, see below |
| 2 | Two Schottkys reversed | **FIXED.** All five now sit GND on the low-X lead, VDD on the banded high-X lead |
| 3 | SCD41 SDA/SCL swapped | **Consistent now** — the SCL-coloured wire lands on `SC4`, the SDA-coloured on `SD4`. The SCD41 model carries no pin text, so the drawing cannot prove the board's own pin order — check the physical silkscreen |
| 4 | Sensor-ground bus floats | **STILL OPEN.** The five sensor grounds still terminate only at screw terminal 4 pin 3 and never join the regulator ground |
| 5 | Ceramic on GND–GND, zener unwired, left 1.1 A unfused | **Mostly fixed** — the zener is now across the sensor rail (3.3 V to GND) and the right ceramic has one lead on the rail. The left 1.1 A PPTC is placed and half-wired, but its run to the LM1117 does not close — see the new findings |
| 6 | Drop fuses all labelled 0.5 | **FIXED** — 0.05 on the four SHT41 drops, 0.5 on the SCD41 drop. The legend still has no 5 V entry |
| 7 | SCD41 local caps, 200 Ω pair, A0–A2 → GND not drawn | **STILL OPEN** — none of the three appear in the model |

**New, not in the v31 review:**

1. **The ESP-rail LM1117's input does not connect to its 1.1 A fuse.** That LM1117's Vin pin is on a
   net with only its own input caps; the fuse's other lead is on a net that ends in space, and five
   green wire ends float around x≈20.2, z −1.4…−3.3 (touching no other body). Traced as drawn, that
   regulator is fed by nothing.
2. **A duplicated wire** — two black bodies with identical volume and identical end points at
   (12.91, −1.06). Delete one.
3. **Three wires with both ends in free space:** a long black one spanning x≈18.7→20.8 at z≈0.5, a
   long green one at x≈30.8 near z≈−6, and green ends beside the zener at (29.5, −1.9)/(29.6, −2.0).
4. **Two blue (24 V-coloured) ends float** beside the mini modules' input electrolytics
   (7.7/7.8, −3.9) and (9.5/9.6, −3.9) — these disappear with the modules.
5. **The sensor-rail LM1117 has an electrolytic on its output but no ceramic.** The ESP-rail one has
   both on both sides. Add the 0.1 µF.
6. A black wire ends at (11.82, 0.58), within 0.06 cm of the mux's `SC7` pin. Channel 7 is unused so
   nothing is broken, but it reads as ground landing on a channel pin.

**Correction to finding 4 above:** those blue "floating" ends were a false positive. A 90° jog in a
wire exposes two 0.15×0.15 faces that look exactly like end caps to a face-area test. A pair of such
faces 0.15 apart on the diagonal is a **jog, not an end** — the same is true of several other pairs in
the list (x≈20.2 near the ESP-rail LM1117, and the pair beside the zener). Only a lone unpaired face
is a real end.

#### Modules removed and the 5 V rebuilt — 2026-09-10

Done in the live model (not saved by Claude). Both **Volt Regulator** modules and their two input
electrolytics are deleted: 53 → 49 root occurrences, 42 → 38 joints (Rigid 25/26/34/35 went with
them). The buses were then repaired and the chain is now, as traced:

`MW24 +24 V → PPTC 0.5 → HW-083B → 5 V → PPTC 1.1 ×2 → LM1117 Vin`, with the sensor-rail LM1117's
input capacitors (CER:1, ELE:3, CER:2) sitting on the 5 V rail where they belong.

What the rebuild needed beyond the deletion, in case it is ever repeated:

1. **The cap stubs had to be trimmed off the buses.** Each bus body was one solid carrying the
   horizontal run, a riser and a down-stub to a capacitor; only the stub goes.
2. **Two bus gaps had to be CLOSED.** They were crossings — of the very cap wires that were removed.
   Once the crossing wire is gone, the gap means "not connected" and has to be filled.
3. **Four bridges**, buck-side riser to onward run, at x = 6.80 / 7.70 / 8.54 / 9.44, each **joined**
   into one body so the drawing reads as connected rather than abutting.
4. **Recoloured to a new 5 V red** (255,0,0), with a **"5 Volt" legend row** added. The run had been
   drawn half in 24 V blue and half in 3.3 V green.
5. Common ground is now real: the buck's negative reaches the ESP32, mux, both LM1117 grounds and
   the output capacitors on one net.

**Traps hit doing it, worth knowing before editing this file again:**

- **Deleting a body that a split produced deleted the whole parent feature** — all ten Power Wiring
  bodies vanished at once, because they share one feature. Recovered with undo. **Cut with a
  Combine‑cut (modifies in place); never delete a body in this model.**
- A base feature's tool body **cannot be used by a Combine in the same script** —
  `ALL_TOOL_BODY_REFERENCE_LOST`. Create the tool in one call, combine in the next.
- A cut box spanning "everything below z" also removes **other wires' crossings** in that band, which
  silently opens gaps elsewhere. Re-probe every gap after cutting.
- Sketch text on an offset XZ plane comes out **vertically mirrored** (sketch +Y = world −Z);
  `isVerticalFlip` does not recompute the extrude. Fix with a 180° move-rotate about the row axis.

#### 200 Ω I²C resistors fitted — 2026-09-10

The user added two `Electric Resistor 1/4` occurrences; both are now **in series in the I²C trunk**,
one per line, mounted with joints and wired in:

- Each resistor sits **above the mux corridor** (SDA at z 6.55, SCL at z 7.05 — the only bands wide
  enough; the corridor itself is six wires on a 0.25 pitch from z 4.39 to 5.79) with its **right lead
  directly above the mux pin** it feeds, so the descent is a straight drop.
- The old trunk wires were cut in the middle; their ESP-side risers and their mux-side drops were
  kept and re-used, so only the middle span is new.
- Route: ESP pin → existing riser → up across the crossing → left along a clear band → up to the
  left lead → **resistor** → right lead → straight down through the corridor → existing mux drop.
- Mounted with **as-built rigid joints** to Breadboard 2, named `SDA resistor 200R` /
  `SCL resistor 200R`, so both are editable and deletable from the browser like any joint.

**How wire geometry is authored in this file** (matters for every future edit):

- Each wiring component has **one `Sketch1`**, whose plane sits at `y = -3.0` with **sketch +X = world
  X and sketch +Y = world Z**, and every wire is a profile extruded by the parameter **`wire_od`**
  along the sketch normal (into −Y). Add wires by drawing into that sketch — never a new one.
- **`addTwoPointRectangle` works; a chain of `addByTwoPoints` does not** — polyline endpoints do not
  merge, so no closed profile forms and the extrude silently finds nothing. Build an L or a T from
  **two overlapping rectangles** and join the resulting bodies.
- A new rectangle drawn over existing sketch curves is **split into several sub-profiles**. Extrude
  all of them — first as a new body, the rest joined into it — or the wire comes out a fragment.
- `sketch.isComputeDeferred = True` raises `InternalValidationError` on these sketches. Don't.
- Crossing convention, in parameter terms: the interrupted wire stops **`wire_od` + 0.002** short on
  each side, and where two crossing wires are adjacent the space between them is exactly
  **`wire_space`** (1 mm), filled by a stub of that width.

#### Second pass — 2026-09-10

Also done in the model, same rules (drawn into each component's existing `Sketch1`, extruded by
`wire_od`, parts mounted with joints):

- **A0–A2 → GND.** A black comb ties the mux's three address pins and runs right into the ground
  wire at the `GND` pin, interrupted at the `SCL` and `SDA` drops with a `wire_space` stub between
  them. The mux address is now explicitly 0x70 in the drawing.
- **ESP-rail LM1117 Vin → its 1.1 A fuse: connected.** The gap was one crossing wide; the run from
  the fuse and the run to Vin were both already drawn and just never met. That whole input rail
  (fuse output, Vin, and its two input capacitors) is now **5 V red**, matching the sensor side.
- **Sensor-rail LM1117 output ceramic: added.** A new `Ceramic Capacitor v3` occurrence sits between
  the existing output electrolytic and the input ceramic, jointed as `sensor rail output ceramic`,
  with its left lead on the 3.3 V output (same body as the electrolytic's output lead) and its right
  lead up to the ground bus.
- **The duplicated black wire body is gone** (two coincident bodies, identical volume and endpoints).

#### SCD41 local caps fitted — 2026-09-10

**Decision: they mount at the SCD41, not at the board end** (user, 2026-09-10). Two
`Ceramic Capacitor v3` occurrences sit immediately left of the sensor, jointed as
**`SCD41 local 10uF`** and **`SCD41 local 0.1uF`**, wired across the sensor's own VDD and GND:

- Both lead rows end at the same height, so each bus runs **above** the lead tips with a short stub
  down to each lead — a bus drawn below the tips would cross the leads themselves and read as a
  short. VDD bus sits 0.25 above the tips, GND bus 0.25 above that (`wire_od` + `wire_space`).
- The VDD bus fuses into the sensor's existing VDD wire from the 0.5 A drop fuse; the GND bus runs
  right and fuses into the existing GND wire at the sensor's GND pin, interrupted where it crosses
  the VDD feed and the Schottky wire.
- Which cap is the 10 µF and which the 0.1 µF is carried by the **joint names**, since both use the
  same ceramic body.

⚠ **Join needs overlap, not contact.** Extruding a profile with `JoinFeatureOperation` and
`participantBodies` only merges if the new material *overlaps* the target; a profile that merely
abuts it produces a **separate body with the default appearance** (renders grey-blue), which is easy
to miss. Four comb fragments came out that way and had to be merged with a Combine-join afterwards.
After any join-extrude, check for bodies whose colour is not one of the palette values.

#### Sensor ground bonded, drawing swept clean — 2026-09-10

- **The sensor-ground bus now reaches the regulator ground.** The route was already half-drawn in
  the model — a black run heading down from screw terminal 4 pin 3 toward the sensor-rail LM1117's
  ground pin, with two gaps left in it. Both gaps are filled, and the lane now walks continuously
  from the terminal down to that ground pin, interrupted only where other wires legitimately cross.
  **Assumption, easily changed:** the star point is the sensor-rail LM1117's ground pin, which is
  what the half-built run pointed at. If it belongs somewhere else — the buck's negative, say — it
  is a short re-route of two pieces.
- **Palette sweep.** Three wire bodies carried the default `Steel - Satin` appearance, which renders
  steel-blue and therefore lies about its rail: two were fragments of this session's work that failed
  to merge, and one was the pre-existing zener-bottom-to-sensor-rail wire, now green. A
  zero-volume 2 µm sliver left by a join was deleted. **Sweep for non-palette colours and
  sub-0.0006 bodies after any batch of join-extrudes** — both are silent.
- The SCL riser's 1 mm short reach is closed; it now abuts its crossing properly.

#### Three dangling leads found by a proper terminal audit — 2026-09-10

The user spotted two parts that looked unwired. He was right, and a proper audit found a third:

| Part | Was | Now |
|---|---|---|
| Output electrolytic on the sensor rail | left (−) lead in the air | tied up to the ground bus |
| Input ceramic on the sensor rail | right lead in the air | tied up to the ground bus |
| **3.6 V zener** | **top lead in the air — the clamp was inert** | top lead down into the ground bus |

⚠ **Why they were missed, and the check that catches them.** The net tracer matched a wire end to a
part when the end fell within 0.25 cm of the part's **bounding box**. A wire that merely ends *near*
a capacitor therefore reads as connected to it, which is how "the zener is now wired" and "the
ceramic's lead is on the rail" were both reported as fixed when neither was. **Probe the actual lead
point instead**: for a vertical two-lead part the leads sit at the bbox centre ± 0.255 at the bbox
top; step outward from there and see whether a wire body actually contains that point. A full sweep
over every part on the board now shows two or more wired terminals everywhere, with one exception:
**screw terminal 5 has all three pins bare** — spare block, or an unfinished drop.

**The SCD41's two capacitors are both ceramic, and that is correct** — the spec is 10 µF + 0.1 µF
X7R right at the sensor, ceramic for the low ESR that a 205 mA pulse needs. Both values are inside
the BOJACK MLCC kit's 0.1–10 µF range, so nothing needs buying.

**Star point confirmed by the user: the LM1117's ground pin.**

#### Read the part markings — they are there, under the wires (2026-09-10)

Several conclusions in this file had been *inferred* from wire colours because the part markings
looked absent. They are not absent — they are **hidden behind the wire bodies**. Switch the five
wiring components' light bulbs off, look from the front, and the silkscreen is readable; switch them
back on afterwards. Doing that settled three things:

- **SCD41 silkscreen reads `VCC · GND · SCL · SDA`**, left to right. The drawing's I²C mapping is
  therefore **confirmed correct** — SCL to `SC4`, SDA to `SD4`. No need to check the physical board.
- **The rectifier diodes DO carry a band**, a grey ring at the high-X end of the body. With GND on the
  low-X lead and VDD on the high-X lead throughout, all five really are **cathode-to-VDD** — verified
  by eye now, not deduced.
- **The zener model carries no band at all** — a plain red cylinder with a text label. Its orientation
  genuinely cannot be read from the drawing. As wired (top lead to ground, bottom lead to the 3.3 V
  rail) the physical part must go in **banded end down, toward the rail**. Worth putting a band on
  that part model so the drawing can state it.

**Every item from the 2026-09-06 review is now closed and verified in the model**, and the user has
confirmed **the parts list is complete — nothing further is needed for this board**. Screw terminal 5
is therefore a **deliberate spare**; its three bare pins are not an omission, so don't re-raise them.
**Zener orientation is now settled and stated by the drawing.** The user added a cathode band to the
part; it landed on the top end while the top lead was wired to ground, which would have put the
cathode on ground and the anode on +3.3 V — a forward-biased zener, i.e. a short across the sensor
rail rather than a clamp. The part was rotated 180° (his choice of the two fixes), so the **banded
cathode end now sits on the 3.3 V rail and the plain end on ground**, which is the correct shunt
clamp. Verified by face appearance, not by eye alone: the black band/lead faces span the lower half,
the bare aluminium lead the upper.

The zener is held at the corrected pose by an as-built joint, **`zener 3.6V clamp`**.

⚠ **Two old joints in that cluster stay suppressed** — `Rigid 54` (zener ↔ input ceramic) and
`Rigid 65` (input ceramic ↔ output electrolytic). **Do not un-suppress `Rigid 54`:** it holds the
zener's pre-flip pose and would undo the orientation fix. It is now redundant and safe to delete, but
**it cannot be deleted through the API** — see below. Delete it from the browser by hand, or leave it.

#### The wiring sketches carry orphaned projections — forced recomputes fail

Deleting `Rigid 54` from a script fails and rolls back with a wall of
`PROJECT_SOURCE_LOST — the project source is lost, Cache is used!` and `TARGET_OCCURRENCE_LOST`
errors naming `Project1`…`Project76` across **three wiring `Sketch1`s** (Power Wiring, ESP-32/TCA9548A,
Sensor Power), plus a `Combine1` whose target body reference is lost.

What that means: those sketches **project geometry from the part bodies** to place wires, and some of
those projections have lost their source — consistent with the four occurrences removed earlier (the
two mini step-downs and their two electrolytics), though which specific projections broke has not been
traced. The design **works and displays correctly on the cached geometry**; the failure only appears
when an operation forces those sketches to fully re-resolve. Deleting a joint is one such operation.

**Diagnosed 2026-09-10, and the verdict is leave it alone.** Every wiring sketch is built almost
entirely on **projected geometry from the part bodies** — that is how wires get placed on pins:

| Sketch | curves | of which projected | unreadable | flagged |
|---|---|---|---|---|
| Power Wiring | 388 | 302 | 0 | yes |
| ESP-32 / TCA9548A | 612 | 263 | 0 | yes |
| Sensor Power | 842 | 514 | 0 | yes |
| Rectifier Diode | 362 | 248 | 0 | no |
| Sensor Logic | 1499 | 1297 | 0 | no |

**Not one projected curve fails to resolve** — the cache is complete, which is why the drawing measures
and renders correctly. The three flagged sketches are exactly the three components where parts or
bodies were removed or consumed during this session (the two mini step-downs and their electrolytics,
and the bodies pulled across components by the bridge joins). Cleaning them would mean deleting
orphaned projections out of sketches holding 300–500 of them with live profiles built on top — real
risk, no functional gain, since every wire is already solid geometry that no longer depends on a live
projection. **Recommendation: leave it.**

**Practical rule:** avoid API operations that force a full recompute of the wiring sketches. Adding
geometry to them and extruding it is fine (that is all this session did). Deleting joints or features
that trigger re-resolution is not — do those in the UI, where Fusion negotiates the cache, and check
the result.

**Model state at close (2026-09-10):** 54 occurrences, 38 joints plus 5 as-built joints holding the
parts added this session (`SDA resistor 200R`, `SCL resistor 200R`, `sensor rail output ceramic`,
`SCD41 local 10uF`, `SCD41 local 0.1uF`), 122 wire bodies, 274 timeline features, **zero invalid
features**, nothing left hidden. The user saved; the document is at v51.

**Already right in v44, do not "fix":** the LM1117s each already carry their own input *and* output
electrolytic; only the two electrolytics on the mini modules go with them.

#### After deleting the two mini modules — 2026-09-10

Decided: they were not deliberate. Both modules and their input electrolytics come out. The
intended segment is exactly the chain above, twice:

```
HW-083B 5.00 V ─[PPTC 1.1 A]─ LM1117T-3.3 (I)  → sensor rail
               └[PPTC 1.1 A]─ LM1117T-3.3 (II) → ESP rail
```

Deleting the modules is **not** the whole edit. Five things go with it:

1. **Capacitors — corrected against the v44 trace.** The two electrolytics that come out with the
   modules are the *modules'* input caps; both LM1117s already carry their own electrolytic on Vin
   and on Vout, so nothing has to be put back. The one real gap is that the **sensor-rail LM1117
   has no 0.1 µF ceramic on its output** — add it. (An output cap must not be ceramic alone
   either: the LM1117 needs some output ESR or it can oscillate.)
2. **Both branches get their 1.1 A PPTC.** The left one was never wired (finding 5), so before
   this edit LM1117 (I) Vin was unfused. After the edit, check both.
3. **Recolour the two runs.** Buck → LM1117 Vin now carries **5 V**; the module outputs were
   drawn green (3.3 V). Rendered colour is truth in this model, so a stale green here reads as a
   3.3 V feed into a regulator that cannot regulate — the exact error being fixed.
4. **Re-fuse the wire bodies where each module sat.** In this drawing a connection is one fused
   body and abutting ends are a *crossing*. Two wire stubs left touching where a module used to
   be will trace as a crossing, i.e. **not connected**.
5. **Check ground continuity through the gap.** The modules' GND pins sat in the regulator
   ground bus. Confirm buck GND → both LM1117 pin 1 → star point is still continuous after the
   deletion. This is the same net as finding 4, still open.

Still open and unaffected by this edit: findings 2, 3, 6, 7, and the star-point question in 4.
Also still undecided: whether the buck moves to the board end so the 15 ft run carries 24 V —
that changes where these two 5 V runs are drawn, so settle it before redrawing much (see
§“The 15-foot run”).

**Trap that produced two of these:** the diode models carry no visible cathode band, so a
reversed diode looks identical to a correct one from the front. Put a band on the model before
trusting any diode orientation in it. **The ESP32 model has no pin text either** — D21 / D22 /
3V3 / GND were inferred from a standard 30-pin DevKit V1 laid USB-left; label the model from the
silkscreen before wiring from it.

### The 15-foot run — SETTLED 2026-09-10, see §"Where the buck lives"

The HW-083B sits about 15 ft of wire from the boards. The review draft carried **5 V** over that
run and regulated at the wrong end — the buck holds 5.00 V at its own terminals, not at the LDO
inputs, and 22 AWG loses roughly 0.35 V round trip at full draw.

**Decided: the buck goes in the tent at the board end, so the 15 ft carries 24 V**, and the
0.5 A PPTC goes at the Mean Well, ahead of the run. The reasoning is in §"Where the buck lives,
and therefore where the 0.5 A goes" and is not repeated here. This paragraph said "not yet
decided" for a day after it was; it is kept only because the voltage-drop number is the reason.

---

## Sensor connector

**SETTLED 2026-09-13: GX16 aviation, 16 mm, panel-mount at the control box. The sensor end
is hardwired.** Ordered: FULARR 6-pair GX16 kit (metal shell, solder cups, rubber caps,
screwdriver) — six pairs covers the four drops with two spare.

⚠ **The kit that shipped is GX16-*5*, not GX16-4.** Same shell, same cups; land four
conductors and leave the fifth cup empty. If a 4-pin kit is bought later the pin map below
is unchanged — the fifth position simply stops existing.

### Why this and not the alternatives

| Rejected | Why |
|---|---|
| **JST-XH 4-pin** (the 2026-09-02 choice) | Superseded. It was chosen to give the SCD41 a tool-free detach *at the sensor*; with the drop hardwired, the detach point moved to the box and JST-XH has no panel-mount form. |
| **RJ45 / 8P8C** | A socket carrying 3.3 V that looks exactly like a network port. PoE puts 48 V on pins 1-2/3-6 or 4-5/7-8 — every one of those is a rail here, and neither the 3.6 V zener nor the TVS survives it. One wrong patch cord destroys both LDOs and the ESP32. Also unsealed, unkeyed, and needs a rectangular cutout. |
| **Qwiic / JST-SH 1.0 mm** | Unsolderable by hand, wires too fragile for a tent drop. The Eyewink board was chosen over the LaskaKit specifically to avoid it. |
| **Dupont** | No keying, no retention, useless in damp. |
| **M12 4-pin A-coded** | Correct and IP67, but ~$30 for sealing the box end does not need. Revisit only if a connector ends up somewhere that actually gets wet. |

**The GX12 rejection of 2026-09-02 does not apply here.** That entry rejected aviation
connectors because they are *metal and heavy hanging on a drop lead 4″ above canopy* — a
statement about the **sensor** end. Nothing hangs at the box end, and the sensor end is now
hardwired, so the objection has no target.

### What it buys

- **Keyed shell** — one orientation only, cannot mate backwards.
- **Screw coupling** — will not vibrate or pull out; no plastic latch to snap off.
- **Solder cups on both halves** — the joint this build prefers, and 16 mm rather than 12 mm
  so four cups are workable by hand.
- **Round hole** in the enclosure wall, drilled, not filed square.
- **Cannot be confused with a network port.** The PoE failure mode is designed out, not
  labelled around.
- Rated 5 A / 125 V AC against 3.3 V at milliamps — enormous margin.
- Rubber caps included: cap any unused socket.

### Pin map — decide once, use on every drop ever made

| GX16 pin | Function | Cat5 conductor |
|---|---|---|
| 1 | **3.3 V** | orange |
| 2 | **GND** | brown + the four whites, commoned into one tail |
| 3 | **SCL** | blue |
| 4 | **SDA** | green |
| 5 | *unused* — leave the cup empty (5-pin shells only) | — |

**Why this order:** it mirrors the sensor breakout's own silkscreen, `VCC GND SCL SDA`,
confirmed by eye on the SCD41 on 2026-09-10. Connector pin order then equals pad order at the
far end of the cable, which removes a whole class of transcription error while soldering.

⚠ **Verify the pin numbers on the actual part before soldering.** GX16 numbering is moulded
into the insulator face and is easy to read mirrored — the socket half counts the opposite way
round from the plug half. Number one cup, ohm it through to the mating half, then do the rest.

**Which half goes on the box: the female contacts.** The box side is the powered side, and
exposed pins on a live connector are a bad habit even at 3.3 V — an unmated plug left dangling
against the chassis shorts the rail through the 0.05 A fuse. Check which half of the kit carries
the panel-mount thread before committing to a hole.

**Placement:** at the **fixture end** of the drop, not down at canopy level. Mate it pointing
down so nothing pools in the shell. At 3.3 V and microamps corrosion is slow, but there is no
reason to sit it in the spray.

**All four drops are identical**, so a cross-plug puts a sensor on the wrong mux channel. That
is harmless — a *fix the wiring, not the YAML* annoyance — but label both halves of every pair
as it is made.

### Cat5 drop pinout (unchanged, 2026-07-26)

One cable per sensor drop, **never daisy-chained** — that defeats the mux isolation.

```
blue        = SCL      white/blue   = GND
green       = SDA      white/green  = GND
orange      = 3.3 V    white/orange = GND
brown       = GND      white/brown  = GND
```

Each signal is twisted with a ground return, SDA and SCL never in the same pair, white
partners **must** be landed rather than left floating.

**The colour map above is unchanged. What changed on 2026-09-13 is how each end terminates.**
No RJ45, no screw terminals, no T568A/B — the cable is now soldered directly into cups.

**Both ends common the five grounds into one tail** — the four whites plus brown, twisted and
soldered together. At the **box** end that tail goes into GX16 **pin 2**; at the **sensor** end
it goes to the breakout's single GND pad. Every drop uses the same four conductors in the same
four positions; see §"Sensor connector" for the pin map.

⚠ **Ohm every drop cable pin-for-pin before it is powered, never just for continuity.**
The old failure mode here was a T568A/B mismatch reversing power while still passing a
continuity test. That one is gone with the RJ45, but the replacement is at least as easy to
make: **orange (3.3 V) and brown (GND) are one cup apart in the shell**, and a cup soldered a
position out reverses power on a sensor that has no reverse protection beyond its 1N5819.
Confirm pin 1 → orange → VCC pad, end to end, on every cable.

---

## Parts state, 2026-09-02

**In hand:** HW-083B ×4 (XL4015-based) · LM1117T-3.3 ×10 · PPTC 0.5 / 1.1 / 2 A ·
3.6 V zener (kit) ·
1N5819 (kit) · SCD41 (Eyewink, blue) · BOJACK ceramic + electrolytic cap kits.

**On order, placed 2026-09-02:** PPTC **0.05 A** (the four SHT41 drop fuses) plus **0.2 A**
and **0.1 A** to stock the range. AliExpress item `1005005328928802`, TLZWLA — the vetted
listing. ⚠ On that listing the variant code is hold current × 100, so `005` = 0.05 A while
`050` = 0.5 A and `500` = 5 A; three near-identical options in one dropdown.

**Unused:** the 2 A PPTC. Nothing in this chain is above 1.1 A, so it would need over
4 A to trip and protects nothing here.

**Connector — ORDERED 2026-09-13.** FULARR 6-pair **GX16** aviation kit, arriving with the
brass tees. Supersedes the JST-XH assortment that was listed here and never ordered; do not
buy JST-XH for this board. ⚠ The kit that shipped is the **5-pin** variant — see
§"Sensor connector".

**Still open:** what else was in the order that got stopped.

**The drop fuses are still a finishing pass** — break one wire per drop when they land.

⚠ **The connector is now on the critical path, which it was not before.** As the JST-XH it
was the SCD41's detach point only, needed before the first outdoor FRC and not before
commissioning. As the GX16 it is the **only** way any of the four drops reaches the board, so
nothing can be commissioned until the kit arrives and the shells are soldered.

---

## Related

- `D:\Claude\Knowledge\grow\hardware-inventory.md` — authority for part numbers,
  provenance and the whole-build power tree. **Nothing from this rebuild enters its
  INSTALLED section until it is fitted, working, and the user says so.**
- `docs/network_addressing.md` — this board is `192.168.2.236`; zeroconf does not follow
  a static IP change.
- `grow_tent_automation/docs/air_diverter_valve.md` — the other live subsystem whose
  failure mode was a missing common ground.
- Fusion 360, *Grow Tent Climate Schematic* (Aqua / Tent) — the wiring drawing. Read the
  section above before trusting it.

**Working checklists.** The same content also exists as two tickable pages, tick state
saved in the browser: *Climate Board Rebuild* (phases A–D end to end) and *Climate Board
LDO Stage* (the LDO stage in detail). They are private Claude artifacts and **their URLs
are deliberately not recorded here, because this repo is public** — they live in the
`project-co2-sensor` memory note instead. Do not add them back.

**This file is the authority.** If a page and this file disagree, the page is stale.
