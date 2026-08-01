# Secrets and Credentials

> **⚠ THIS REPOSITORY IS PUBLIC.**
> `https://github.com/Blaze350454/claude-code-ha_1` — public since 2026-03-14.
> Anything committed here is world-readable the moment it is pushed. There is no
> "I'll clean it up later": assume every pushed commit was scraped.

This repo drives physical hardware (irrigation valves, pumps, climate control) on a
home LAN. Credentials here are not abstract.

---

## Where credentials actually live

**No credential value belongs in a tracked file — ever.** These are the only
sanctioned locations, all gitignored:

| Location | Holds | Consumed by |
|---|---|---|
| `.env` (repo root) | `HA_URL`, `HA_TOKEN`, `PROXMOX_*` | MCP server, `update-homelab` scripts, ad-hoc tooling |
| `.cursor/mcp.json` | `HA_URL`, `HA_TOKEN` | the `tag_migration_*.py` / `registry_export.py` family |
| `.claude/mcp.json` | MCP server env | Claude Code |
| `.mcp.json` | `${env}` placeholders only | Claude Code (expands from launch environment) |
| `/home/homeadmin/.ha_token` (VM 101) | HA token, bare, no trailing newline, `chmod 600` | `pull-ha.sh` cron |

`.cursor/mcp.json.example` is the tracked, placeholder-only template. Copy it, never
commit the filled-in version.

The Proxmox password doubles as the `sudo` password on VM 101 and the `root` SSH
password on the Proxmox host. Rotating it means updating all three uses.

---

## Rotating the HA long-lived token

The token exists in **four** places. Miss one and something breaks silently.

1. **Create** the replacement first — `http://192.168.2.151:8123/profile/security` →
   Long-lived access tokens → Create token. Name it with the date
   (e.g. `grow-home-tooling-2026-08`) so the old and new are unambiguous in the list.
   The old token stays valid until explicitly revoked, so nothing breaks mid-swap.
2. **Update all four**: `.env`, `.cursor/mcp.json`, `.claude/mcp.json`, and
   `/home/homeadmin/.ha_token` on VM 101. The VM file must be exactly the token —
   183 bytes, **no trailing newline**, mode `600`.
3. **Verify before revoking** — see the next section. This step is not optional.
4. **Then** revoke the old token in the same HA UI page.
5. Restart Claude Code so its MCP servers pick up the new value.

### ⚠ The verification that matters: `pull-ha.sh` fails OPEN

`/home/homeadmin/pull-ha.sh` runs from cron at `:05 :20 :35 :50` — four times an
hour. Before restarting Home Assistant it checks whether irrigation is mid-cycle:

```sh
status=$(curl -s -m 5 -H "Authorization: Bearer $(cat "$TOKEN_FILE")" \
    http://localhost:8123/api/states/input_text.tent_irrigation_status \
    | sed -n 's/.*"state": *"\([^"]*\)".*/\1/p' | head -1)

if [ -n "$status" ] && [ "$status" != "Idle" ] && ... ; then defer; fi
```

A revoked or stale token makes that `curl` return 401 → `status` is **empty** → the
`[ -n "$status" ]` test **fails** → the defer branch is skipped entirely and it goes
straight to `docker restart homeassistant`.

**An invalid token does not disable auto-deploy. It disables the irrigation safety
interlock, silently, with no error anywhere.** HA can then be restarted mid feed or
flush, with valves dropping closed on reboot.

So after any rotation, confirm the guard still works:

```sh
ssh homeadmin@192.168.2.151 'bash -s' <<'EOF'
status=$(curl -s -m 5 -H "Authorization: Bearer $(cat /home/homeadmin/.ha_token)" \
    http://localhost:8123/api/states/input_text.tent_irrigation_status \
    | sed -n 's/.*"state": *"\([^"]*\)".*/\1/p' | head -1)
[ -n "$status" ] && echo "guard ACTIVE (status=$status)" || echo "guard BROKEN"
EOF
```

Non-empty status = the guard is live. Empty = stop and fix the token before doing
anything else.

---

## Auditing history for leaked secrets

`.gitignore` does **not** untrack a file that is already committed, and it does
nothing about history. Adding an ignore rule closes the door going forward only.

To untrack without deleting the local file:

```sh
git rm --cached <path>     # file stays on disk
# then add it to .gitignore and commit both
```

To audit what was ever committed:

```sh
# was a specific credential file ever added?
git log --all --diff-filter=A -- .env

# scan every blob in all history for an HA token
git rev-list --all --objects | ... | git cat-file -p | grep 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
```

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9` is the base64 HS256 JWT header — a generic,
non-secret fingerprint that matches any HA token, so it is safe to grep for and safe
to send to a remote host.

**If a secret was pushed, rotate it — do not reach for a history rewrite first.** A
revoked credential in public history is an inert string. Rewriting history on a
pushed branch is disruptive and does not un-publish anything already scraped.

---

## Incident log

**2026-08-01 — HA token exposed publicly.** `.cursor/mcp.json` was the one
credentials file missing from `.gitignore`, and it held a *literal* HA long-lived
token (not a placeholder). Committed in `819a494` ("Add .gitignore and store HA token
in mcp.json") and world-readable from that moment.

Resolution: untracked + gitignored (`f8eb866`), token rotated across all four
locations, old tokens revoked. The two historical blobs are now inert, so no history
rewrite was performed.

Full-history audit at the same time confirmed:

- `.env` — **never committed** (the real Proxmox password never leaked)
- `.claude/mcp.json`, `.mcp.json` — only ever held `${env}` placeholders
- Google Drive credentials, `Irrigation/esphome/secrets.yaml`, `Pics/*token*.jpg`,
  `Pics/*Encryption Key*.jpg` — never committed
- No GitHub tokens, AWS keys, private keys, or webhook URLs in tracked files
  (`BEGIN RSA PRIVATE KEY` appears only as prose inside crawled GitHub docs under
  `storage/`)

**Known outstanding:** `.playwright-mcp/*.log` (13 files) are tracked and contain
third-party session `access_token` values captured from a browsing session on
2026-05-15. Not credentials for any system in this repo, and long expired, but they
are accidental debug output that does not belong in a public repo. Untrack + ignore
when convenient.
