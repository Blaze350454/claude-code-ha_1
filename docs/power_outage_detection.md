# House power / network outage detection

Implemented in [`packages/system/power_outage.yaml`](../packages/system/power_outage.yaml).
Built 2026-08-04 after an area power cut, and validated end-to-end against that
same outage plus the recovery and restart that followed.

## The problem it solves

HA runs on a UPS, so when the house loses power HA stays up and watches every
mains device drop. But it had no concept of *"the house lost power"* — it
surfaced a pile of unrelated-looking per-device faults, and the tent banner could
only say `TENT OFFLINE`, which blames the tent when the tent is a victim.

## Entities

| Entity | What it is |
|---|---|
| `sensor.house_offline_witnesses` | Count of power **chains** unreachable. `witnesses` attribute lists `{key,label,members,ts,since}`. |
| `binary_sensor.house_power_outage` | On when **≥3 chains dropped within 180 s of each other**. Attributes: `kind`, `chains`, `since`, `detail`. |
| `input_datetime.ha_last_start` | Stamped on every `homeassistant.start`. Drives the restart guards. |

Automations: stamp-HA-start, outage-detected (phone + persistent notification),
outage-cleared.

## The model: chains + simultaneity

A **chain** is a set of devices that cannot fail independently — because they
share a supply, *or* because they share the integration/cloud path that reports
them. Each chain is worth exactly **one vote**, however many entities it owns.

| Chain | Members |
|---|---|
| Tent ESP trio | grow-tent-one + two + climate (share a supply) |
| HS300 strip + irrigation ESP32 | strip voltage + `feed_empty` — the ESP32 is powered from an HS300 outlet |
| Sonoff plug set (8) | HLG, Chilled, AC Circulation Fan, Circulation Fans, Duct Fan, Tent Controller, PC, Prusa |
| Mom-grow Kasa pair | `mom_grow_1` + `mom_grow_lights` |
| Irrigation multi-plug | `kasa_smart_outdoor_plug_switch_1` + `_2` |

So one ESP32 dying and taking 26 entities with it can never trip this alone.

### Why rooms were rejected

The first cut counted *areas*. That was wrong: chunks of the smart house get
unplugged when not in use, so "devices in N rooms are offline" is a normal
resting state here rather than an event.

**Simultaneity** is what separates the two — something unplugged last week
carries a week-old timestamp and can never cluster with a live event. The
detector finds the **largest cluster of chains sharing a drop-time**, not merely
what is down.

### Why the Sonoff plugs are one vote

They are 8 physically separate devices, but they report through one integration
and one cloud/LAN path, so a Sonoff outage drops them together for reasons that
have nothing to do with power. Before grouping, HLG, Chilled, the AC circulation
fan and the duct fan were **four independent votes** against a 3-chain
threshold — a single Sonoff hiccup would have cleared it alone.

### Chain `ts` is the *most recent* drop among dead members

Not the earliest. Otherwise one long-unplugged member anchors the chain in the
past and masks a live event.

## POWER vs POWER OR NETWORK

`switch.pc` and `switch.prusa` are Sonoff plugs fed **from the UPS**. They share
vendor, integration, cloud path and WiFi with the six mains Sonoff plugs and
differ **only in power source**. Six dead while those two still report cannot be
a Sonoff failure and cannot be the network — it is power.

The Blink tent cameras (battery + cloud) are the second reference, proving
internet is up. Either alive ⇒ `POWER`. Both dark ⇒ `POWER OR NETWORK`:
something bigger (modem/ISP down, or the UPS flat), and the two are not
distinguishable from inside HA.

The Brentons router is itself on the UPS, so WiFi surviving a cut is the
*expected* case — which is what makes a `POWER` verdict trustworthy.

## The HA-restart trap

**After a restart, every entity carries `last_changed` = restart time.** The
whole house looks like it dropped in one instant — which under a simultaneity
model would fire *forever*, not briefly. Three guards:

1. **Grace (180 s)** — a chain must be dead continuously before it counts, so
   reboots and OTA flashes never qualify.
2. **Restart blind spot (90 s)** — a chain whose drop-time sits within 90 s of
   `ha_last_start` is **ignored for clustering**; its true onset is unknowable, so
   it is not evidence of simultaneity.
3. **Start guard (300 s)** — suppressed entirely just after boot.

`ha_last_start` fails **open** at its 2000-01-01 initial (detector active), the
deliberate safe direction.

> The same trap corrupts *reporting*: the banner's "offline since HH:MM" is the
> restart, not the outage. On 2026-08-04 it read 15:50 (restart) when the true
> onset was 15:15. **Get true onset from the recorder history API**, never from
> `last_changed`.

## Gotchas worth keeping

- **`bad` states are per chain**, so every member must agree on what "dead" looks
  like. The HS300 is represented by its **voltage** sensor rather than
  `binary_sensor.*_cloud_connection`, because the cloud sensor needs `'off'` in
  its bad list while `'off'` on its chain-mate `feed_empty` is a perfectly normal
  reading (device_class moisture — `'on'` = liquid present). A shared `'off'`
  would silently mark a healthy ESP32 dead.
- **Witnesses must be on unprotected mains.** UPS-backed gear stays up by design
  so it can never report the event, and if it is ever simply powered off it casts
  a bogus vote. `switch.bambu` shipped as a witness and was removed for this.
- **Check 7-day recorder availability before adding a witness.** All current
  members are ≥94 %; `media_player.loft_tv` was rejected at 61.6 % (the TV sleeps).
- **Test alert logic with `POST /api/template`**, not by poking real entities —
  read-only, and it will not fire a spurious "power restored" notification.

## Planned change

The irrigation ESP32 is currently powered from an HS300 outlet, so the strip and
the ESP32 share one vote. When it moves to its own smart plug, split
`tent_hs300` back into two chains — the exact replacement block is written into
the package header. That restores a 6th independent vote.
