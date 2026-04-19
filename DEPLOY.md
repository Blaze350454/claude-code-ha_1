# Deploying HA Config Changes

This repo is the dev/backup layer for the live Home Assistant instance on the
Ubuntu VM at `192.168.2.151`. Flow:

```
Windows edit  →  git push  →  GitHub Actions validates  →  VM git pull  →  HA reload
```

## 1. Edit on Windows

Work in `D:\Claude\Projects\homeassistant-config\`. Standard git workflow.

```bash
git pull --rebase        # sync first — VM's 2 AM cron may have pushed
# ...edit files...
git add <files>
git commit -m "what changed"
git push
```

## 2. Watch CI

After push, check GitHub Actions: https://github.com/Blaze350454/claude-code-ha_1/actions

- **YAML Lint** must be green.
- **Home Assistant Config Check** is currently non-blocking (HA 2026.4.x
  `check_config` bug — see comment in `.github/workflows/validate.yml`). Read
  the log anyway; if it fails for a reason unrelated to the known
  `helpers/trigger.py:205` KeyError, investigate before deploying.

Do not deploy to the VM if YAML Lint failed.

## 3. Deploy to VM

SSH in and pull:

```bash
ssh homeadmin@192.168.2.151
cd ~/homeassistant/.config
git pull --rebase
```

## 4. Reload HA

Pick the lightest option that covers what you changed.

| Changed | Reload command |
|---|---|
| Automations only | Developer Tools → YAML → Reload Automations (UI) |
| Scripts only | Developer Tools → YAML → Reload Scripts |
| Template sensors | Developer Tools → YAML → Reload Template Entities |
| Packages / `configuration.yaml` / integrations | Full restart (below) |

Full restart from the VM:

```bash
docker restart homeassistant
```

Watch the logs for startup errors:

```bash
docker logs -f homeassistant
```

`Ctrl-C` to detach once you see `Home Assistant initialized` (or the error
you're hunting).

## 5. Rollback

If the deploy broke something, on the VM:

```bash
cd ~/homeassistant/.config
git log --oneline -5                  # find the last good commit
git reset --hard <good-commit-sha>
docker restart homeassistant
```

Then on Windows, revert the bad commit so GitHub and VM stay in sync:

```bash
git revert <bad-commit-sha>
git push
```

(Or `git reset --hard` locally and force-push — only if no one else has
pulled the bad commit yet.)

## Nightly auto-backup

`/home/homeadmin/backup-ha.sh` runs at 2 AM via cron. It:

1. `git pull --rebase` — picks up anything pushed from Windows during the day.
2. `git add -A && git commit` — captures UI-edited state (dashboards, etc.).
3. `git push` — sends VM-side changes back to GitHub.

Log: `/home/homeadmin/backup.log`.

If Windows and VM both edit the same file the same day, the 2 AM rebase
handles clean cases automatically. A true conflict will abort the backup
and leave a message in the log — resolve manually on the VM.

## Things that are NOT in git

Per `.gitignore` on the VM:

- `secrets.yaml` — real secrets, never committed
- `home-assistant.log*`, `*.db`, `*.db-*` — runtime state
- `.storage/` except lovelace dashboards — HA-managed UI state
- `*.bak*`, `ogb_data/` — local scratch

Disaster recovery for those relies on the weekly Proxmox VM snapshot (3 AM
Sunday), not this repo.
