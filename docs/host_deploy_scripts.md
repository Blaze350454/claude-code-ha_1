# Host deploy scripts (VM `homeadmin@192.168.2.151`)

These live on the HA VM's host filesystem (`/home/homeadmin/`), **not** in this
repo's deploy path, so HA never loads them. This file is the version‑controlled
record of them. See [DEPLOY.md](../DEPLOY.md) for the deploy flow.

Last captured / revised: **2026-06-27**.

## crontab (`crontab -l`, user `homeadmin`)

```cron
0 2 * * * /home/homeadmin/backup-ha.sh
0 3 * * * /home/homeadmin/ha_backup_helpers.sh >> /home/homeadmin/ha_backup.log 2>&1
5,20,35,50 * * * * /home/homeadmin/pull-ha.sh
```

- `backup-ha.sh` (02:00) — nightly: `git pull --rebase`, commit UI-edited state, push.
- `ha_backup_helpers.sh` (03:00) — helper-value backup.
- `pull-ha.sh` (every 15 min) — auto-deploy; see below.
  - **Staggered to `:05/:20/:35/:50`** (was `*/15` = `:00/...`) so it no longer
    collides with the 02:00 / 03:00 jobs' `git pull` (the collision caused a
    daily "cannot lock ref → git pull failed" at 02:00).
- Pre-change crontab backed up on the VM at `~/.crontab.bak.20260627`.

## `/home/homeadmin/pull-ha.sh`

Revised 2026-06-27 from "restart on ANY new commit" to a **selective restart**:
skips CI/docs-only commits, and defers the restart while a tent feed/flush is
mid-cycle (needs a long-lived token at `~/.ha_token`, `chmod 600`; absent → it
restarts immediately, no defer). Original saved on the VM as `pull-ha.sh.bak`.

```bash
#!/bin/bash
# Auto-pull HA config from GitHub and restart HA — but only when it matters:
#   * Skip the restart when the new commits touch ONLY CI / docs / git metadata
#     (ci/, .github/, *.md, .gitignore, .yamllint*) — HA never loads those.
#   * Defer the restart (up to ~1h) while a tent feed/flush cycle is mid-run so a
#     deploy can't interrupt irrigation. Needs a long-lived token at
#     ~/.ha_token (chmod 600); without it, restarts immediately (no defer).
# Runs every 15 min via cron. Log: /home/homeadmin/pull.log
# Original kept as pull-ha.sh.bak.

set -euo pipefail

CONFIG_DIR=/home/homeadmin/homeassistant/.config
LOG=/home/homeadmin/pull.log
TOKEN_FILE=/home/homeadmin/.ha_token
DEFER_FILE=/home/homeadmin/.pull-ha.deferred
MAX_DEFERS=4   # ~1h (4 x 15 min) of deferral, then restart regardless

cd "$CONFIG_DIR"

before=$(git rev-parse HEAD)
if ! git pull --rebase --quiet origin main 2>>"$LOG"; then
    echo "$(date): git pull failed" >> "$LOG"
    exit 1
fi
after=$(git rev-parse HEAD)

# A restart may already be pending from an earlier deferral even with no new commit.
pending=0
[ -f "$DEFER_FILE" ] && pending=1

if [ "$before" = "$after" ] && [ "$pending" = "0" ]; then
    exit 0
fi

# New commits: restart only if any touch HA-loaded files.
if [ "$before" != "$after" ]; then
    changed=$(git diff --name-only "$before" "$after")
    runtime_changed=$(echo "$changed" | grep -vE '^(ci/|\.github/|.*\.md$|\.gitignore$|\.yamllint.*$)' || true)
    if [ -z "$runtime_changed" ] && [ "$pending" = "0" ]; then
        echo "$(date): pulled ${before:0:7}..${after:0:7} - non-runtime only (CI/docs), no restart" >> "$LOG"
        exit 0
    fi
fi

# Restart warranted. Defer if irrigation is mid-cycle (status != Idle), capped.
status=""
if [ -f "$TOKEN_FILE" ]; then
    status=$(curl -s -m 5 -H "Authorization: Bearer $(cat "$TOKEN_FILE")" \
        http://localhost:8123/api/states/input_text.tent_irrigation_status 2>/dev/null \
        | sed -n 's/.*"state": *"\([^"]*\)".*/\1/p' | head -1 || true)
fi

defers=0
[ -f "$DEFER_FILE" ] && defers=$(cat "$DEFER_FILE" 2>/dev/null || echo 0)

if [ -n "$status" ] && [ "$status" != "Idle" ] && [ "$status" != "unavailable" ] && [ "$defers" -lt "$MAX_DEFERS" ]; then
    echo $((defers + 1)) > "$DEFER_FILE"
    echo "$(date): restart pending (HEAD ${after:0:7}) but irrigation busy ($status) - deferring [$((defers + 1))/$MAX_DEFERS]" >> "$LOG"
    exit 0
fi

rm -f "$DEFER_FILE"
echo "$(date): pulled up to ${after:0:7} - restarting HA${status:+ (status=$status)}" >> "$LOG"
if docker restart homeassistant >> "$LOG" 2>&1; then
    echo "$(date): HA restart ok" >> "$LOG"
else
    echo "$(date): HA restart FAILED" >> "$LOG"
    exit 1
fi
```

## `~/.ha_token` (enables the defer-while-busy check)

A long-lived access token (HA → profile → Long-Lived Access Tokens), `chmod 600`.
Not in git. Without it, `pull-ha.sh` restarts immediately (no deferral). Recreate:

```bash
# on the VM:
read -rs t && printf '%s' "$t" > ~/.ha_token && chmod 600 ~/.ha_token && unset t
```

## Restore originals (if a change misbehaves)

```bash
# on the VM:
cp ~/pull-ha.sh.bak ~/pull-ha.sh            # revert script
crontab ~/.crontab.bak.20260627             # revert crontab
```
