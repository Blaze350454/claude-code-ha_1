# Proxmox Host — storage, backups, monitoring

Covers the Proxmox VE host at **192.168.2.100** (node name `proxmox`, PVE 9.1.1): its
storage layout, the VM backup job, and how backup health surfaces in Home Assistant.

Access: the host has **no SSH key** — password auth as `root` with `PROXMOX_PASSWORD`
from `.env` (see [`secrets_and_credentials.md`](secrets_and_credentials.md)). VM 101
(`homeadmin@192.168.2.151`) uses key auth. Guests are reached with `pct exec <id>` (LXC)
or `qm` (VM).

Guests: **VM 101** = `home-assistant` (Ubuntu 24.04, 64 GB, the HA Docker host) ·
**LXC 100** = `esphome` (the ESPHome build/dashboard box).

---

## Storage layout

Rebuilt 2026-08-06 after `local` hit **100 % full (0 KiB available)**, which had been
silently breaking backups for two months.

| Storage | Type | Backing | Holds |
|---|---|---|---|
| `local` | dir on `/var/lib/vz` | `pve/root` LV, **112 GB** | ISOs, container templates, backups |
| `local-lvm` | lvmthin | `pve/data` thin pool, 794 GB | VM/CT disks (~21 % used) |
| — | ext4, mounted at `/var/lib/vz/dump` | `pve/backups` LV, **295 GB** | **vzdump archives only** |

**`/var/lib/vz/dump` is its own filesystem.** It is *not* part of the root filesystem any
more, so filling root and filling the dump volume are now two separate problems. It is
mounted by **UUID in `/etc/fstab`** (`1356440f-974e-4162-9137-fbc85dbf83d7`) so it survives
reboot; the pre-change fstab is backed up at `/root/fstab.bak-20260806`.

⚠ **Volume group `pve` has `VFree = 0`.** Extending `pve/root` from 96 GB to 112 GB
consumed the last free extents, so `local` **cannot be grown that way again**. Future
growth has to come from the thin pool (create/extend a thin LV) or a new physical disk.

```
lvextend -l +100%FREE pve/root && resize2fs /dev/pve/root   # how root was grown (no space left now)
lvcreate -V 300G --thinpool data -n backups pve             # how the backup volume was made
```

---

## Backups

Weekly `vzdump` of **VM 101**, Sundays 03:00, snapshot mode, zstd. Roughly **20 GB** per
archive against 64 GB of source (~37 % of the disk is zeroes, so it compresses well).
Retention is **`prune-backups keep-last=3`** on the `local` storage — set 2026-08-06;
before that there was no retention at all and archives accumulated unbounded.

Manual run:

```bash
vzdump 101 --storage local --mode snapshot --compress zstd
```

### The 2026-06 → 2026-08 silent failure (read this before debugging a backup)

25 weekly runs existed but only **5 had produced a `.vma.zst`**. Every run from
**2026-06-14 to 2026-08-02** — eight consecutive weeks — failed with:

```
ERROR: vma_queue_write: write error - Broken pipe
```

That message means **out of disk**, nothing more exotic. It went unnoticed for two months
because Proxmox's only notification target was the builtin `mail-to-root` — local mail on
the host that nothing reads.

**How to spot it at a glance:** in `/var/lib/vz/dump`, a failed run leaves a `.log` and
**no `.vma.zst`**. Failed logs are 2.0–2.7 KB; successful ones are 4–5 KB.

### QEMU guest agent

`agent: 1` is set in `qm config 101` and `qemu-guest-agent` is installed in the guest, so
backups are **filesystem-consistent** (vzdump can `fs-freeze` before snapshotting) rather
than crash-consistent. This matters for HA's SQLite recorder DB.

Verify from the **host**, not the guest:

```bash
qm agent 101 ping              # rc 0
qm agent 101 fsfreeze-status   # -> thawed
```

- The unit shows `is-enabled = static`. **That is correct** — it is udev-activated via
  `/lib/udev/rules.d/60-qemu-guest-agent.rules` and `WantedBy` the virtio port device, so
  it starts on boot. Don't "fix" it.
- Installing the package needed **no VM power cycle** because the virtio channel
  `/dev/virtio-ports/org.qemu.guest_agent.0` already existed. Only if that channel is
  *missing* do you need a full stop/start — a reboot does not attach it.
- **Never run `qm agent 101 fsfreeze-freeze` on the live VM.** A failed thaw hangs all
  guest I/O. `fsfreeze-status` is proof enough.

---

## Monitoring (both halves live in the `homeassistant-config` repo)

Backup health is watched from two directions so neither can fail quietly.

### Pull — `packages/system/proxmox_backups.yaml`

HA polls the storage-content API every 30 min and exposes:

| Entity | Meaning |
|---|---|
| `sensor.proxmox_backup_last` | timestamp of the newest archive |
| `sensor.proxmox_backup_age` | its age in days — this is what the watchdog triggers on |
| `sensor.proxmox_backup_count` | archives retained (3 at steady state) |
| `sensor.proxmox_backup_total_size` | GB total |

`automation.watchdog_proxmox_vm_backup_stale` pages at **>8 d** (one weekly run missed) and
**>15 d** (broken), plus a third trigger for "the monitor itself cannot reach the API" so
it cannot go blind the way mail-to-root did.

Distinct from `watchdog_ha_backup_and_database` in `host_health.yaml`, which watches HA's
*own* internal backups rather than these whole-VM images.

#### ⚠ The API permission trap

Listing **backup** volumes is not covered by any audit role. From
`PVE::Storage::check_volume_access` (`/usr/share/perl5/PVE/Storage.pm`):

```perl
} elsif ($vtype eq 'backup' && $ownervm) {
    $rpcenv->check($user, "/storage/$sid", ['Datastore.AllocateSpace']);
    $rpcenv->check($user, "/vms/$ownervm", ['VM.Backup']);
```

It needs **`Datastore.AllocateSpace`** (not `Datastore.Audit`) plus **`VM.Backup`**.
`PVEAuditor` has neither — and the API then returns **HTTP 200 with an empty list, never a
403**. A permissions fault is therefore indistinguishable from "no backups exist", while
ISOs and templates keep listing fine.

In place: user **`ha-monitor@pve`**, token `!ha` with `privsep 0`, custom role
**`HABackupMonitor`** = `Datastore.Audit,Datastore.AllocateSpace,VM.Audit,VM.Backup,Sys.Audit`
on `/`. This token is consequently **not strictly read-only** — it can create backups and
allocate space, though it cannot delete backups (that needs `Datastore.Allocate`) or touch
VM config. That is a Proxmox constraint of the content API, not a choice.

**`root@pam` bypasses all these checks**, so `pvesh get /nodes/proxmox/storage/local/content
--content backup` succeeding as root proves nothing about a token. Test with the token.

### Push — `packages/system/proxmox_notifications.yaml`

`/etc/pve/notifications.cfg` (which did not exist before 2026-08-06):

- endpoint **`ha-webhook`** — POST to `http://192.168.2.151:8123/api/webhook/{{ secrets.token }}`,
  `Content-Type: application/json`, webhook id held as a PVE **secret** so it lives in the
  root-only `/etc/pve/priv/notifications.cfg`
- matcher **`ha-alerts`** — `match-severity warning,error,unknown` → `ha-webhook`
- the builtin `default-matcher` → `mail-to-root` is left **intact**; both fire

Mechanics: `--body`, `--header` and `--secret` values are **base64 encoded**; header/secret
use `name=<name>,value=<base64>`. The body is **Handlebars, not Jinja** — use
`{{ json x }}` so multi-line backup reports produce valid JSON. Available fields:
`title`, `message`, `severity`, `timestamp`, `fields.<name>`, `secrets.<name>`; helpers
`json`, `escape`, `url-encode`. `fields.type` ∈ `package-updates`, `fencing`, `replication`,
`vzdump`, `system-mail`; note **`job-id` has a hyphen** so Jinja needs
`trigger.json.fields['job-id']`.

**Testing the routing:** `pvesh create /cluster/notifications/targets/ha-webhook/test`
exercises the endpoint but **bypasses matchers**, so it does not prove routing works. For a
real end-to-end test run `vzdump 999 --storage local` — a nonexistent VM, so it fails
harmlessly and emits a genuine `severity=error, type=vzdump` notification; the output then
confirms `notified via target 'ha-webhook'`.

---

## Rebooting VM 101

Cheap and safe — **~30 s** end to end (SSH back at 15 s, HA `RUNNING` at 30 s), measured
2026-08-06 for the 6.8.0-134 → 6.8.0-137 kernel bump.

- Both `homeassistant` and `matter-server` are `restart: unless-stopped`, so they return
  unattended. The VM is `onboot: 1` for host reboots.
- **The ESPs are unaffected** — their uptime keeps counting; valve/GPIO state is not
  disturbed by a *VM* reboot (unlike an ESP reflash, which drives all outputs OFF on boot).
- Pre-flight: feed/flush scripts idle, valves closed, and confirm the container restart
  policy.
- ⚠ **The e1000e NIC-hang history does not apply to guest reboots.** That fault is the
  host's physical I219-LM (`eno1`); VM 101 is `virtio_net`. Only rebooting the **host**
  carries it. The `tso/gso off` workaround is persisted in the host's
  `/etc/network/interfaces` regardless.
- After a restart every entity's `last_changed` becomes the restart time, so "offline
  since HH:MM" lies — get true onset from the recorder history API.
