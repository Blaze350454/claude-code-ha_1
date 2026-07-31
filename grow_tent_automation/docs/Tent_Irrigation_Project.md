# Tent Irrigation Project

## Overview

| Component | Details |
|-----------|---------|
| Grow Space | 5' x 5' x 10' tent |
| Plants | 9 cannabis plants |
| Growing Medium | Boiled pro mix + perlite in fabric pots |
| Feeding Method | Hydroponic via drip irrigation |
| Nutrient Reservoir | 25 gallon |
| Flush Reservoir | 20 gallon (clean water) |

## System Goals
- Deliver nutrients to 9 plants via drippers
- Ability to flush entire irrigation system with clean water
- Switch between nutrient feed and flush cycles
- Push remaining nutrients to plants before filling lines with clean water

---

## Parts List

| Category | Part | Details |
|----------|------|---------|
| **Hose/Fittings** | Poly hose | 3/4" diameter throughout |
| **Solenoid Valves** | U.S. Solid 3/4" 12V DC (x3) | Main valve, Flush reservoir valve, Drain valve |
| **Check Valves** | Check valve #1 | Nutrient reservoir (after Flora Flex pump) |
| | Check valve #2 | After Main Valve (protects all upstream) |
| **Manual Valves** | Ball valve #1 | Main system shutoff (after merge) |
| | Ball valve #2 | Final shutoff before orbits |
| **Filtration** | 200 micron filter | |
| **Pressure** | Adjustable pressure regulator | |
| | Pressure gauge #1 | On tee after filter (pre-regulator) |
| | Pressure gauge #2 | On/after pressure regulator (post-regulator) |
| **Sensors** | Pressure transducer | 1/8" NPT, 0-100 PSI, 5V DC, stainless steel — ⚠️ firmware uses a 0-30 psi transfer function; confirm the installed range |
| | Hall flow sensor | 3/4", 1-100 L/min, 5V DC (see note) |
| **Electronics** | ESP32 | Microcontroller for sensor data |
| | LM2596 buck converter | 12V → 5V DC for sensors |
| | 10kΩ resistors (x2) | Voltage dividers |
| | 20kΩ resistors (x2) | Voltage dividers |
| **Pumps** | BOKYWOX 115 VAC diaphragm | 3 GPM, adjustable 30–50 psi switch — **FEED** (25 gal nutrient), external mount |
| | Flora Flex FSP-10001 | 3/4 HP submersible, 17.34 psi max — **FLUSH** (20 gal), moved off feed duty |
| | DEKOPRO 1/4 HP | 1850 GPH, 27 ft head (~11.7 PSI) — **RETIRED**, displaced by the FloraFlex |
| **Reservoir equipment** | 400 GPH stir pump | **1 per reservoir** (2 total — feed and flush each have one) |
| | Air pump + air stone(s) | ~60 L/min single pump, **routed to one reservoir at a time** by the servo pinch valve — never both |
| **Air Bleed** | Flora Flex 1517 | Air bleed valve |
| **Distribution** | ORB 8-Port Manifold (61008) | Qty: 4 |
| **Emitters** | PCJ 0.5 GPH | Pressure compensating, Qty: 27 (3 per plant) |
| **Automation** | Relay module | 12V DC relay for solenoid valve control |

---

## System Flow Diagram

```
NUTRIENT: BOKYWOX Diaphragm Pump → Check Valve → Expansion Tank Tee ──┐
                                                                     │
                                                                  [MERGE]
                                                                     │
FLUSH: Flora Flex FSP-10001 → Flush Valve ───────────────────────────┘
                                                                     ↓
Ball Valve → Filter → Tee(Air Bleed↑) → Tee(Pressure Gauge #1↑) → Pressure Regulator → Tee(Pressure Gauge #2↑) → Main Valve → Check Valve → Ball Valve → ORBITS → Drain Valve
```

**Note:** All three valves (Main, Flush, Drain) are U.S. Solid 3/4" 12V DC solenoid valves.

---

## Flow Sequence (Detailed)

| Step | Component | Function |
|------|-----------|----------|
| 1 | BOKYWOX Diaphragm Pump | Draws from 25 gal nutrient reservoir (external mount, suction strainer) |
| 2 | Check Valve #1 | Prevents backflow to nutrient reservoir |
| 2a | Expansion Tank Tee | Eastman 60008 mini tank — pulsation damping / hammer arrest |
| 3 | **MERGE** | Flush line joins main line |
| - | ↳ Flora Flex FSP-10001 | Draws from 20 gal flush reservoir |
| - | ↳ Flush Valve | U.S. Solid 12V DC - controls flush water input |
| 4 | Ball Valve | Main system shutoff |
| 5 | Filter | 200 micron - protects downstream |
| 6 | Tee → Air Bleed | Releases trapped air |
| 7 | Tee → Pressure Gauge #1 | Shows pre-regulator pressure |
| 8 | Pressure Regulator | Sets system pressure for emitters |
| 9 | Tee → Pressure Gauge #2 | Shows post-regulator pressure |
| 10 | Main Valve | U.S. Solid 12V DC - controls flow to distribution |
| 11 | Check Valve #2 | Prevents backflow from manifolds |
| 12 | Ball Valve | Final shutoff before orbits |
| 13 | 4x ORB Manifolds | 8-port distribution |
| 14 | 27 PCJ Emitters | 0.5 GPH pressure compensating |
| 15 | Drain Valve | U.S. Solid 12V DC - end-of-line flush to waste |

---

## Flow Calculations

- 27 emitters x 0.5 GPH = **13.5 GPH total system flow = 0.225 GPM = 0.85 L/min**
- Nutrient reservoir: 25 gal / 13.5 GPH = ~1.85 hours continuous feed
- Flush reservoir: 20 gal - for line filling and flush cycles

### ⚠️ Pressure does NOT change delivered volume

The PCJ emitters are **pressure compensating** — they hold 0.5 GPH each across roughly
**7–58 psi**. Total system flow is therefore pinned at **0.85 L/min at any pressure inside
that band**, and measured flow (~1 L/min) already matches the design figure.

Raising system pressure from ~12 psi to 25 psi buys **emitter-to-emitter uniformity and
comfortable operation inside the PC band — not more water**. Feed `*_duration` helpers do
**not** need shortening after the pump swap, and the flow-meter K-factor does not need
re-deriving for a new flow rate.

Corollary for pump sizing: the BOKYWOX passes ~6 L/min at 35 psi while the emitters accept
0.85 L/min — a ~7x mismatch, so its demand switch **will** rapid-cycle. A bypass/recirc leg
back to the feed reservoir (shedding ~5 L/min, tuned with a needle valve) is required, not
optional. The mini expansion tank is far too small to absorb this on its own (~29 mL usable
drawdown ≈ 1 s of run time).

---

## Detailed Component Specifications

### Flora Flex FSP-10001 (3/4 HP Submersible Pump — FLUSH Reservoir)

> **Moved off feed duty.** It can never exceed 17.34 psi dead-head, so it could not deliver the
> 25 psi target at the emitters. It now runs the **20 gal flush reservoir**, where ~17 psi
> dead-head (roughly 10–14 psi at the emitters after losses) still clears the PCJ emitters'
> ~7 psi compensating minimum. Replaced on feed by the BOKYWOX diaphragm pump.

| Spec | Value |
|------|-------|
| Output Power | 3/4 HP |
| Max Flow Rate | 4450 GPH (74.2 GPM) |
| Max Head | 40 ft |
| Max Pressure | 17.34 PSI |
| Voltage | 115V / 60Hz |
| Amperage | 7.1A full load |
| Max Fluid Temp | 86°F |
| Pipe Diameter | NPT 1", 1-1/4", 1-1/2" |
| Protection | IPX8, thermal overload |
| Warranty | 1 Year |

**Benefits:**
- Runs on power-on (no switch needed - good for automation)
- Drains down to 0.2" water level
- Corrosion resistant plastic
- Thermal overload protection for continuous duty

**Watch out for:**
- Max fluid temp 86°F - keep nutrient reservoir cool
- Outlet is 1" minimum - need reducer to 3/4"
- 17.34 PSI max - ensure pressure regulator is set appropriately
- High flow (4450 GPH) vs 13.5 GPH system need - most water recirculates in reservoir

---

### U.S. Solid Solenoid Valves — Model USS2-01006

All solenoid valves in this system are the same model.

| Spec | Value |
|------|-------|
| Brand | U.S. Solid |
| Model | USS2-01006 |
| Size | 3/4" NPT |
| Voltage | 12V DC |
| Quantity | 5 (Main Irrigation, Flush Irrigation, Flush Drain, Empty One, Empty Two) |

**Benefits:**
- 3/4" fits system directly - no adapters needed
- 12V DC - easy integration with Home Assistant via relay
- No minimum pressure requirement (unlike pilot-operated valves)
- Direct-acting solenoid works at any pressure

**Watch out for:**
- Ensure proper polarity when wiring
- Install with flow direction arrow pointing correct way
- May need inline fuse for protection

---

### BOKYWOX 115 VAC Diaphragm Demand Pump (FEED Reservoir)

| Spec | Value |
|------|-------|
| Type | Self-priming diaphragm demand pump (Shurflo 2088 clone) |
| Flow | 3 GPM (~11 L/min open flow) |
| Pressure switch | Adjustable, 30–50 psi (settable down to ~10) |
| Voltage | 115 VAC — plug control on the HS300 |
| Mount | **External** to the reservoir (mains out of the water) |
| Ports | Female-swivel-with-gasket, 1/2"-14 NPSM straight **male** thread |

**Setup notes:**
- Set cut-out **45–50 psi** (cut-in lands ~35) so the regulator keeps ≥10 psi of headroom
  above its 25 psi setpoint. A 35 psi cut-out drops cut-in to ~25 and starves the regulator
  at the bottom of every cycle.
- Needs a **suction strainer + dip tube/bulkhead** — it is not submersible like the FloraFlex.
- Needs a **bypass/recirc leg** — see the pressure-compensating note under Flow Calculations.
- Thread adaptation to the 1/2" female NPT reducing couplings is a deliberate
  **NPSM-male-into-NPT-female jimmy rig** (no sourceable NPSM adapters). Plastic male port,
  brass female coupling. One-shot fit; hand tight + 1–1.5 turns only.

---

### DEKOPRO 1/4 HP — RETIRED

Displaced by the FloraFlex on flush duty. Kept as a spare.

| Spec | Value |
|------|-------|
| Flow | 1850 GPH |
| Max Head | 27 ft (~11.7 PSI) |
| Power | 1/4 HP |

---

### Pressure Transducer (1/8" NPT Stainless Steel)

| Spec | Value |
|------|-------|
| Thread | 1/8" NPT |
| Range | 0-100 PSI |
| Voltage | 5V DC |
| Output | 0.5-4.5V (typical) |
| Material | Stainless steel |

**Benefits:**
- Real-time pressure monitoring (digital readout)
- Can replace or supplement mechanical pressure gauges
- Stainless steel suitable for nutrient solutions
- Wide range (0-100 PSI) covers all system conditions

**Suggested Placement:**
- Pre-regulator (replaces/supplements Pressure Gauge #1)
- Post-regulator (replaces/supplements Pressure Gauge #2)

---

### Hall Effect Flow Sensor (3/4")

| Spec | Value |
|------|-------|
| Size | 3/4" |
| Flow Range | 1-100 L/min |
| Voltage | 5V DC |
| Output | Pulse signal |
| K-factor | 62.72 pulses/L (bucket test 2026-05-10) |

*(An earlier revision of this doc listed a 30-500 L/min sensor. That part was never installed —
it has always been the 1-100 L/min unit.)*

**⚠️ FLOW RANGE MISMATCH (still present, but mild):**
- Sensor minimum: **1 L/min**
- Steady emitter flow: **0.85 L/min** — just *below* cut-in
- Pressurization bursts at the start of a feed read fine (2.49 L/min confirmed good)

**Consequence:** the meter sees the leading burst of each feed but under-reports or drops out
during the steady portion. Adequate for the idle-flow watchdog and for "did a feed happen",
not for accurate per-feed volume totalling.

**Recommended replacement:** DIGITEN FL-308D (G3/8, 0.3-10 L/min, F=23.6Q, ±3%) — covers 0.85
L/min properly. **Mount it downstream of the bypass tee**, otherwise it reads recirculation
rather than delivery to the plants.

---

## ESP32 Sensor Wiring

### Power Supply Chain

```
                    ┌─────────────┐
   12V DC ─────────►│   LM2596    │
                    │  (set 5V)   │
                    └──────┬──────┘
                           │ 5V
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
         ┌────────┐   ┌────────┐   ┌────────┐
         │Pressure│   │  Flow  │   │  ESP32 │◄── 3.3V (USB or own regulator)
         │Transdu.│   │ Sensor │   │        │
         └───┬────┘   └───┬────┘   └────────┘
             │            │
         SIGNAL       SIGNAL
         (0.5-4.5V)   (5V pulses)
             │            │
             ▼            ▼
        ┌─────────┐  ┌─────────┐
        │ Voltage │  │ Voltage │
        │ Divider │  │ Divider │
        └────┬────┘  └────┬────┘
             │            │
             ▼            ▼
          ESP32        ESP32
          ADC pin      GPIO pin
          (0-3.3V)     (3.3V logic)
```

### Why Voltage Dividers?

ESP32 GPIO pins are **3.3V max** - 5V signals will damage them.

- Pressure transducer outputs 0.5-4.5V (analog)
- Flow sensor outputs 5V pulses (digital)

### Voltage Divider Circuit

```
Sensor Signal ────┬──── R1 (10kΩ) ────┐
                  │                    │
                  └── to ESP32 pin ◄───┤
                                       │
                       R2 (20kΩ) ──────┤
                                       │
                         GND ──────────┘
```

**Formula:** Vout = Vin × R2/(R1+R2)

| Input | R1 | R2 | Output | Safe for ESP32? |
|-------|----|----|--------|-----------------|
| 4.5V (pressure max) | 10kΩ | 20kΩ | 3.0V | Yes |
| 0.5V (pressure min) | 10kΩ | 20kΩ | 0.33V | Yes |
| 5.0V (flow pulse) | 10kΩ | 20kΩ | 3.3V | Yes |

### Common Ground (Critical)

All grounds must be connected together:
- 12V supply GND
- LM2596 GND
- ESP32 GND
- Pressure transducer GND
- Flow sensor GND

### ESP32-WROOM-32E Pin Assignments (Confirmed)

**New sensor GPIOs — verified against boot, strapping, and WiFi constraints:**

| Sensor | GPIO | ADC Channel | ADC1 (WiFi-safe) | Boot/Strapping Issue | Input-Only | Interrupt-Capable |
|--------|------|-------------|-------------------|----------------------|------------|-------------------|
| Pressure Pre-Regulator | GPIO34 | ADC1_CH6 | Yes | None | Yes | Yes |
| Pressure Post-Regulator | GPIO35 | ADC1_CH7 | Yes | None | Yes | Yes |
| Flow Sensor | GPIO32 | ADC1_CH4 | Yes (unused as ADC) | None | No | Yes (hardware PCNT) |

**Strapping pins — not used, but must not be pulled incorrectly at boot:**

| GPIO | Boot Requirement | Risk if Violated |
|------|-----------------|-----------------|
| GPIO0 | HIGH = normal boot, LOW = flash mode | Device stuck in flash mode |
| GPIO2 | Must be LOW during programming | Programming failure |
| GPIO12 | Must be LOW at boot (3.3V flash) | Can damage flash at 1.8V |
| GPIO15 | Must be HIGH at boot (has internal pull-up) | Suppresses boot log output |

**ADC note:** ADC2 pins (GPIO0, 2, 4, 12–15, 25–27) are disabled when WiFi is active. Always use ADC1 (GPIO32–39) for analog sensors. GPIO34, 35, 36, 39 are input-only with no internal pull-up/down — ideal for voltage-divider-driven signals.

**WiFi + ADC noise:** WiFi transmissions cause brief ADC noise spikes even on ADC1. Mitigated by `sliding_window_moving_average` in ESPHome code. If jitter persists in Home Assistant, add `samples: 5` to each ADC sensor config.

**All pins in use on this device:**

| GPIO | Used For | Direction | Safe |
|------|----------|-----------|------|
| GPIO4 | One-wire (Dallas temp sensors) | Bidirectional | Yes |
| GPIO16 | Binary sensor - Flush Quarter | Input | Yes |
| GPIO17 | Binary sensor - Flush Full | Input | Yes |
| GPIO18 | Binary sensor - Res Three Quarter Full | Input | Yes |
| GPIO19 | Binary sensor - Res Half-Three Quarter | Input | Yes |
| GPIO21 | Binary sensor - Res Quarter-Half | Input | Yes |
| GPIO22 | Output - Flush Drain Valve | Output | Yes |
| GPIO23 | Output - Flush Irrigation Valve | Output | Yes |
| GPIO25 | Output - Empty Two (spare) | Output | Yes |
| GPIO26 | Output - Empty One (spare) | Output | Yes |
| GPIO27 | Output - Main Irrigation Valve | Output | Yes |
| GPIO32 | Flow Sensor (pulse counter) | Input | Yes |
| GPIO34 | Pressure Pre-Regulator (ADC) | Input-only | Yes |
| GPIO35 | Pressure Post-Regulator (ADC) | Input-only | Yes |

### Parts List for Wiring

| Part | Quantity | Purpose |
|------|----------|---------|
| LM2596 DC-DC buck module | 1 | 12V → 5V for sensors |
| 10kΩ resistor | 2 | Voltage dividers (R1) |
| 20kΩ resistor | 2 | Voltage dividers (R2) |

**Note:** Can substitute 2x 10kΩ in series for each 20kΩ resistor.

---

## CAD Drawings

Location: `C:\Users\bbcbg\Pictures\Fusion 360\Irrigation`

| File | Description |
|------|-------------|
| Complete.jpg | Full system overview |
| Lables.jpg | Component labels |
| Main Wall.jpg | Wall-mounted control assembly |
| Orbits.jpg | 4x ORB 8-port manifolds on frame |
| Reservoirs.jpg | Two reservoir setup |
| Table.jpg | Grow table with manifold frame |

---

## Notes

- Check valve after Main Valve protects all upstream components from backflow
- Air bleed valve positioned at high point to release trapped air
- Pressure gauge before regulator shows input pressure for diagnostics
- PCJ emitters are pressure compensating - deliver consistent 0.5 GPH regardless of line length **or system pressure** (across ~7-58 psi). See the pressure/volume note under Flow Calculations — raising pressure improves uniformity, it does not increase delivered volume
- 4 manifolds x 8 ports = 32 available, 27 in use (5 capped)
- Each reservoir has the same fit-out: 1x 400 GPH stir pump, air stone(s), float switches, DS18B20 temp probe, and a fill valve
- The ~60 L/min air pump is a **single source shared between both reservoirs, but not simultaneously** — the DS3225 servo pinch valve (in build) diverts the air to feed *or* flush, one at a time. Stir pumps are genuinely one-per-reservoir and independent

---

## Key System Concerns

| Issue | Details | Status/Recommendation |
|-------|---------|----------------------|
| **Flush pump pressure** | ~~075DV needs 15 PSI min; DEKOPRO provides ~11.7 PSI~~ | **RESOLVED** - Using U.S. Solid 12V DC valves (no minimum pressure requirement) |
| **Feed pump oversized** | BOKYWOX passes ~6 L/min at 35 psi; PC emitters accept 0.85 L/min (~7x mismatch) | Demand switch will rapid-cycle. **Bypass/recirc leg back to the feed reservoir is required**, tuned with a needle valve to shed ~5 L/min. Returns below the surface so it doesn't aerate/foam. Bonus: stirs the reservoir during every feed |
| **Pipe sizing** | Flora Flex pump is 1"+ outlet | Need reducers to 3/4" |
| **Low flow operation** | At 13.5 GPH (0.225 GPM), below 3 GPM threshold | Add 200 mesh filter upstream |
| **12V controller** | U.S. Solid valves need 12V DC | Use relay module for control |
| **Flush water temp** | Flora Flex max 86°F — now applies to the flush reservoir, not the nutrient one | Keep flush reservoir cool |
| **Check valve quality** | Must seal properly to prevent cross-contamination | Use spring-loaded, quality seals (Viton/EPDM) |
| **Flow sensor range** | Sensor min 1 L/min; steady system flow 0.85 L/min | Reads the feed's leading burst but drops out on the steady portion. Replace with DIGITEN FL-308D (0.3-10 L/min) for accurate per-feed volume |

---

## Reference Links

- [FloraFlex Submersible Pump 3/4 HP - Indoor Farmer](https://indoorfarmer.ca/products/floraflex-submersible-pump-3-4-hp-4450gph-max-17-34-psi)

