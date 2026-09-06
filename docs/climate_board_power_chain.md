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
meter in 10 A mode *is* the short — and adjust CC until it reads the target. The voltage
collapsing while you do this is correct; that is what constant-current means. Remove the
short and confirm CV returns to 5.00 V.

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

**Use a low CC as a bench tool, not as the final setting.** While landing drops one at a
time (step 13), winding CC down to ~200 mA makes a miswired drop a non-event — the rail
sags instead of delivering fault current. Wind it back to ~3 A before the board goes into
service, or the branch fuses are decorative.

**One fault no CC setting helps with:** a short at the buck's own output terminals,
upstream of both branch fuses. Only the 24 V input fuse is in that path, and it needs
~4.5 A at 5 V to open — essentially wide open. That stretch of wire is short and inside
the box; ohm it before powering rather than trying to fuse around it.

**Lock both pots** — nail polish or threadlocker — **and photograph them into
`D:\Claude\Pictures\`.** The DFR0379's setpoint was lost when it died and nothing on
disk recorded it. There are now two settings to lose instead of one.

---

## Fuse map

Every polyfuse sits **in the box, on the terminal side** — never out at the sensor.
That puts a bridged Cat5 crimp inside the protected zone too.

**Every polyfuse goes in the positive conductor only. Never fuse a ground return.** A
tripped ground fuse leaves the load powered with no way home, and the current finds its
way back through the signal lines instead.

| Position | Value | Why this value |
|---|---|---|
| 24 V → HW-083B | **0.5 A** | Draw is ~180 mA peak at 24 V. Protects the shared backbone: a shorted HW-083B input would otherwise drag tent-one and tent-two down with it. |
| 5 V → sensor LDO | **1.1 A** | Sensor rail peaks ~250 mA, so it never nuisance-trips. Sized *up* for discrimination — see below. |
| 5 V → ESP LDO | **1.1 A** | ESP32 WiFi bursts hit ~500 mA; polyfuse thermal constant is seconds, so no nuisance trip. |
| SCD41 drop | **0.5 A** | Contains a dead short in under a second. |
| SHT41 drops ×4 | **0.05 A** | *Not fitted yet — see "Deferred".* |

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
| 1N4729A, 3.6 V zener | sensor rail, at the LDO output | crowbar if an LDO fails short input→output |
| 1N5819 Schottky | across VDD→GND at **each** sensor, **cathode — the banded end — to VDD** | reverse-polarity clamp |
| 10–22 µF electrolytic + 0.1 µF ceramic | both LDOs, input **and** output, close to the pins | LM1117 stability |
| 10 µF + 0.1 µF ceramic X7R ≥16 V | at the SCD41 pins | supplies the 205 mA pulses locally |

**No tantalum anywhere** — it fails short on overvoltage.

The LM1117 output cap needs **some ESR**; a small pure-ceramic output cap alone can make
it oscillate. Use the electrolytic-plus-ceramic pair, not ceramic alone.

**Use 3.6 V for the clamp, not 3.3 V.** A 3.3 V clamp on a 3.3 V rail sits at its knee
and leaks continuously. If 3.6 V is ever unobtainable, 3.9 V is the better fallback than
3.3 V — a weaker clamp beats one that conducts all day.

The zener is **sacrificial and only works if an upstream fuse trips**. Expect to replace
it after any event; an overloaded zener usually fails short but can fail open.

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
| 1 | Adjust-up test on the dead DFR0379, **nothing downstream** | holds ~6 V unloaded ⇒ alive, only the setpoint was lost ⇒ you have a spare |
| 2 | Ohm the SCD41 that was connected 2026-08-14 | kΩ+ VDD↔GND ⇒ that sensor is alive and the buck died of something else |
| 3 | Identify the two pots on the HW-083B — silkscreen, LED count, or turn each unloaded | only the CV pot moves the output voltage |
| 4 | Set CV, nothing downstream | 5.00 V |
| 5 | Set CC by shorting the output **through the ammeter** | ~3 A in limit · CV returns to 5.00 V when the short is removed · **not 1.3 A — see above** |
| 6 | Lock **both** pots; photograph them | — |
| 7 | Continuity-check both LM1117s | tab ↔ middle pin ≈ 0 Ω |
| 8 | Ohm the **new** SCD41 bare, all wires off, before any diode is near it | kΩ+ VDD↔GND — anything near 0 Ω does not get connected |
| 9 | Ohm every drop cable **pin-for-pin** | each conductor to its own pin at the far end, no cross-pairs |
| 10 | Build the LDO stage: caps, fuses, clamp, Schottkys | — |
| 11 | **Unpowered**, ohm Vin→GND and Vout→GND at each regulator | kΩ+. Near 0 Ω is a backwards electrolytic or a solder bridge — find it now, not with 5 V on it |
| 12 | Power up with **no sensors connected** | each rail 3.25 – 3.35 V |
| 13 | Land the drops **one at a time**, re-metering after each | rail holds 3.3 V after every drop |
| 14 | Boot with logs, read the I²C scan | 0x70 + 4 serials + 0x62 on ch4 · `Tent CO2` publishing within 30 s |
| 15 | FRC outdoors, powered ≥ 3 min | — |

Steps 1 and 2 are free and were never run. Either could still exonerate a part.

⚠ **Step 5 is only safe once step 3 has confirmed the board is CC/CV.**

On step 12: a fixed-output LM1117 self-biases through its internal divider, so an
unloaded reading is trustworthy. If it reads high, hang ~1 kΩ across the output to
settle it.

Step 13 is not ceremony — **one-at-a-time reconnection is the diagnostic that actually
found the fault on 2026-07-28.**

On step 14: a serial on the wrong channel means **fix the wiring, not the YAML**. And if
all eight SHT41 entities come up `unknown` rather than `unavailable`, the ESP is
connected fine and it is an I²C setup failure — that distinction has saved a wrong
diagnosis before.

On step 15: tent intake is **living-room air** (exhaust goes outside), so the tent never
breathes 420 ppm and the in-tent guard blocks the button anyway. FRC happens outdoors at
the start of every grow. Afterwards, cross-check `temperature_offset: 4.0` against the
adjacent Flower SHT41 — the four agreeing to 0.29 °C are the reference.

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
in step 4 confirms both the pinout and which way round the part is, before any power,
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

## Sensor connector

The SCD41 is unclipped and carried outdoors for FRC **at the start of every grow**, so
its drop must detach without tools. Chosen 2026-09-02: **JST-XH, 2.54 mm pitch, 4-pin.**

- **Keyed and shrouded** — cannot mate backwards. This matters more than the original
  analysis assumed, which was written for a connector mated once; repeated mating is
  exactly when that error becomes likely. With the 1N5819 and the 0.5 A fuse already on
  that branch, this becomes the best-protected drop on the board.
- **2.54 mm pitch matches the breakout's own header row**, so the through-hole header
  solders straight into the holes already on the SCD41 board — no adapter.
- Positive detent latch; ~30 mating cycles rated; once per grow is decades.

Rejected: **Qwiic / JST-SH 1.0 mm** — unsolderable by hand, wires too fragile for a tent
drop; the Eyewink board was chosen over the LaskaKit specifically to avoid it.
**Dupont** — no keying, no retention, useless in damp. **GX12 aviation** — solder cups
and a screw lock are appealing, but it is metal and heavy hanging on a drop lead 4" above
canopy.

**Before ordering:** count the pads on the breakout and note their order. Most are a
4-pin 0.1" row (VIN / GND / SCL / SDA) but some break out 5 or 6.

**Placement:** put the connector at the **fixture end** of the drop, not down at canopy
level — it is not sealed and the tent is wet. Mate it pointing down so nothing pools in
the housing. At 3.3 V and microamps corrosion is slow, but there is no reason to sit it
in the spray.

**Pin order:** pick one and use it on every drop ever made. Low stakes here — all five
drops carry the same four signals, so a cross-plug puts a sensor on the wrong mux channel
rather than damaging anything, and that is a *fix the wiring, not the YAML* annoyance.
Decide once and record it beside the Cat5 pinout.

### Cat5 drop pinout (unchanged, 2026-07-26)

One cable per sensor drop, **never daisy-chained** — that defeats the mux isolation.

```
blue        = SCL      white/blue   = GND
green       = SDA      white/green  = GND
orange      = 3.3 V    white/orange = GND
brown       = GND      white/brown  = GND
```

Each signal is twisted with a ground return, SDA and SCL never in the same pair, white
partners **must** be landed rather than left floating. T568B straight-through both ends.

⚠ **orange (3.3 V) and white/orange (GND) are the same pair**, so a T568A/B mismatch at
one end reverses power **and still passes a continuity test**. Ohm every drop cable
**pin-for-pin**, never just for continuity.

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

**Still to buy:** a JST-XH assortment — not on the 09-02 order. Needed before the first
outdoor FRC, not before commissioning.

**Still open:** what else was in the order that got stopped.

**Nothing blocks the build.** The drop fuses are a finishing pass — break one wire per
drop when they land. The connector is needed before the first FRC, which happens at the
start of a grow, not at commissioning.

---

## Related

- `D:\Claude\Knowledge\grow\hardware-inventory.md` — authority for part numbers,
  provenance and the whole-build power tree. **Nothing from this rebuild enters its
  INSTALLED section until it is fitted, working, and the user says so.**
- `docs/network_addressing.md` — this board is `192.168.2.236`; zeroconf does not follow
  a static IP change.
- `grow_tent_automation/docs/air_diverter_valve.md` — the other live subsystem whose
  failure mode was a missing common ground.

**Working checklists.** The same content also exists as two tickable pages, tick state
saved in the browser: *Climate Board Rebuild* (phases A–D end to end) and *Climate Board
LDO Stage* (the LDO stage in detail). They are private Claude artifacts and **their URLs
are deliberately not recorded here, because this repo is public** — they live in the
`project-co2-sensor` memory note instead. Do not add them back.

**This file is the authority.** If a page and this file disagree, the page is stale.
