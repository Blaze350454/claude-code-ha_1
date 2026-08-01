# 2026-07-31 — Weekly Recap

**32-day streak (since Jun 30) | Focus: grow-tent-climate ESP32 build-out**

## What you worked on
- **Grow Home / climate node**: schematic review off the cirkitdesigner drawing, 3V3-vs-VIN power decision, cap sizing from the BOJACK kit, CAT5 runs for 3× SHT41 + SCD41, SCD41 placement + ASC/FRC calibration, then the rail failure and recovery. Closed out with dashboard cards (Canopy/Flower/Stem/Controller), the 50 °C controller alert, and the dewpoint-based condensation alert.
- **Grow Home / irrigation**: Eastman 2-gal expansion tank sizing vs. the BOKYWOX pump's adjustable pressure switch, plus the settled NPT thread jimmy-rig.
- **3D-Printer**: Bambu P1S camera missing in HA — fixed via the access code rather than a re-add.

## Best session
Jul 27–28: the 3.3 V rail read 0.1 V after a wiring cleanup. Instead of chasing the regulator you'd just swapped, you bisected by powering sensors one at a time and caught the *brand-new* SCD41 as internally shorted VDD↔GND — it had killed the regulator and was holding SCL low. Replacement unit DOA, refund secured.

## Add to your playbook
1. **Commit as you go.** ~177 edits landed this week against 2 commits, and the working tree is carrying 7 `tag_migration_*.py` scripts, dashboard backups, migration snapshots, and two untracked skills. The drift habit you wrote up in `feedback_check_repo_drift_before_deploy` applies to this repo too, not just the HA VM.
2. **Use `flash-esp32`.** You ran the `pct exec` + `esphome run` loop by hand in 7 sessions this week; the skill that encodes exactly that loop has been sitting unused since Jul 15. Invoking it beats re-deriving the LXC path each time — and it's still untracked, so it's one `rm -rf` from gone.
