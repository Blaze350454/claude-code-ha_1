# 2026-08-10 — Weekly Recap

**7-day streak (Aug 4–10) | Focus: Servo Air Control Valve (Fusion) + homelab hardening**

## What you worked on
- **Servo Air Control Valve (CAD)** — the week's centre of gravity, across three long sessions. Cam → pivot arm → push arm chain worked out from scratch after you scrapped the earlier design, then both stations live-mirrored and closed at v49 with 0.000000 interference in all three states.
- **Power outage detection** — a real area outage on Aug 4 became the test rig. You redirected the detector from "rooms went dark" to "≥3 independent power *chains* dropped inside 180 s", which killed a whole class of false alarms, and the tent banner collapsed from a dozen bogus errors down to one honest TENT OFFLINE.
- **Proxmox** — `local` at 100% had been silently failing HA VM backups for 8 weeks. Dumps moved onto their own 295 G LV, backup-age alert wired into HA, guest agent fixed, host notifications routed through a webhook.
- **Network + docs** — ESP static IPs lifted above the DHCP pool with an HA re-point tool, HS300 socket map corrected, timelapse sync script and offline gallery.

## Best session
Aug 9–10: you refused the ±0.03 blade-band offset outright and made the fix land at the datum instead — pivot re-referenced off the servo shaft ("that will never change") and `Slider 5` re-pointed to the as-built face, putting `d165`/`d166` back to a clean 4 mm rather than carrying a compensation hack forever.

## Following up on last week
- **Use `flash-esp32`** — done. Invoked twice this week instead of hand-rolling `pct exec`, and the skills are now tracked in git rather than one `rm -rf` from gone.
- **Commit as you go** — half done, and it inverted mid-week. Aug 4–7 was your strongest committing stretch in a while (10 commits here, 15 in `homeassistant-config`). Then the three longest sessions of the week — Aug 8, 9, 10, all CAD — produced zero commits.

## Add to your playbook
1. **Commit the valve spec at the end of each CAD session.** Fusion holds the geometry; the spec file is the only place the *reasoning* lives — squeeze depth, dead travel, the 0.07/side clearance, why the pivot is datumed off the servo shaft. It is one file and it is still untracked: `git add air_squeeze_valve/servo_air_control_valve_spec.md`.
2. **Promote the two hard Fusion rules from memory into the skill.** "Never create a new component when one already exists" and "never `computeAll()` on his model" both cost real time — the first triggered a version rollback on Aug 6 and then *recurred* on Aug 8 despite being stated. They live only in memory today, which is recalled probabilistically, whereas the "Always" section of `~/.claude/skills/fusion-360/SKILL.md` loads every session. Related signal: the Aug 6 session ran 71 Fusion MCP calls without that skill loaded at all.
