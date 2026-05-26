# Complete Backup Setup - Git + Proxmox

## Two-Layer Backup Strategy

### Layer 1: Daily Git Backups (Config Files)
- **What:** Configuration files only
- **When:** Every day at 2 AM
- **Where:** GitHub (https://github.com/Blaze350454/homeassistant-config)
- **Good for:** Quick config restores, version history

### Layer 2: Weekly Proxmox VM Backups (Complete System)
- **What:** Entire VM (OS, database, media, everything)
- **When:** Every Sunday at 3 AM
- **Where:** Proxmox local storage
- **Good for:** Disaster recovery, complete restoration

---

## Part A: Set Up Daily Git Backups

**In your Ubuntu VM console (where you are now):**

### Step A1: Create Backup Script

```bash
nano /home/homeadmin/backup-ha.sh
```

**Paste this script:**

```bash
#!/bin/bash

# Navigate to HA config directory
cd /home/homeadmin/homeassistant/config

# Add all changes
git add .

# Check if there are changes to commit
if git diff-index --quiet HEAD --; then
    # No changes
    echo "$(date): No changes to backup" >> /home/homeadmin/backup.log
else
    # Changes found, commit and push
    git commit -m "Auto backup $(date '+%Y-%m-%d %H:%M')"
    git push
    echo "$(date): Backup completed successfully" >> /home/homeadmin/backup.log
fi
```

**Save:** `Ctrl + O`, `Enter`, `Ctrl + X`

### Step A2: Make Script Executable

```bash
chmod +x /home/homeadmin/backup-ha.sh
```

### Step A3: Test the Script

```bash
/home/homeadmin/backup-ha.sh
```

**Should say:** "No changes to backup" (since we just pushed everything)

### Step A4: Set Up Cron Job

```bash
crontab -e
```

**If it asks which editor:** Type `1` and press Enter (for nano)

**Add this line at the very bottom:**

```
0 2 * * * /home/homeadmin/backup-ha.sh
```

**Save:** `Ctrl + O`, `Enter`, `Ctrl + X`

### Step A5: Verify Cron Job

```bash
crontab -l
```

**Should show:** `0 2 * * * /home/homeadmin/backup-ha.sh`

✅ **Done!** Git backups will now run every night at 2 AM.

---

## Part B: Set Up Weekly Proxmox VM Backups

**Switch to Proxmox shell (web UI or SSH to 192.168.2.100):**

### Step B1: Test Manual Backup First

```bash
vzdump 101 --compress zstd --storage local --mode snapshot
```

**This will:**
- Create a snapshot of VM 101 (Home Assistant)
- Compress with zstd
- Save to local storage
- Take about 5-10 minutes

**Wait for it to complete.** You'll see progress messages.

### Step B2: Verify Backup Was Created

```bash
ls -lh /var/lib/vz/dump/ | grep 101
```

**Should show a .vma.zst file** (your backup!)

### Step B3: Create Automated Weekly Backup Script

```bash
nano /root/backup-ha-vm.sh
```

**Paste this:**

```bash
#!/bin/bash

# Backup VM 101 (Home Assistant)
vzdump 101 --compress zstd --storage local --mode snapshot

# Keep only last 4 backups (1 month of weekly backups)
# List backups, keep newest 4, delete others
cd /var/lib/vz/dump/
ls -t vzdump-qemu-101-*.vma.zst | tail -n +5 | xargs -r rm

# Log the backup
echo "$(date): VM 101 backup completed" >> /root/backup.log
```

**Save:** `Ctrl + O`, `Enter`, `Ctrl + X`

### Step B4: Make Script Executable

```bash
chmod +x /root/backup-ha-vm.sh
```

### Step B5: Set Up Cron Job (Weekly on Sundays at 3 AM)

```bash
crontab -e
```

**Add this line:**

```
0 3 * * 0 /root/backup-ha-vm.sh
```

**Save:** `Ctrl + O`, `Enter`, `Ctrl + X`

### Step B6: Verify Cron Job

```bash
crontab -l
```

**Should show:** `0 3 * * 0 /root/backup-ha-vm.sh`

✅ **Done!** VM backups will run every Sunday at 3 AM.

---

## Backup Schedule Summary

| Time | Day | Type | What | Where |
|------|-----|------|------|-------|
| 2:00 AM | Daily | Git | Config files | GitHub |
| 3:00 AM | Sunday | VM Snapshot | Full system | Proxmox local |

---

## Testing Your Backups

### Test Git Backup (Now)

**In Ubuntu VM console:**

```bash
# Make a small change
cd /home/homeadmin/homeassistant/config
echo "# Test backup" >> configuration.yaml

# Run backup script
/home/homeadmin/backup-ha.sh

# Check log
cat /home/homeadmin/backup.log

# Verify on GitHub
# Go to: https://github.com/Blaze350454/homeassistant-config
# You should see a new commit!
```

### Test VM Backup (Optional - takes 5-10 min)

**In Proxmox shell:**

```bash
/root/backup-ha-vm.sh
```

---

## Restoring from Backups

### Restore Config from Git

**In Ubuntu VM:**

```bash
cd /home/homeadmin/homeassistant/config
git pull
```

Or restore to specific date:
```bash
# See commit history
git log --oneline

# Restore to specific commit
git checkout <commit-id> configuration.yaml
```

### Restore Full VM from Proxmox

**In Proxmox web UI:**

1. Select VM 101 → Backups
2. Select a backup file
3. Click **Restore**
4. Confirm

Or from shell:
```bash
# List backups
ls -lh /var/lib/vz/dump/ | grep 101

# Restore (replace with actual backup filename)
qmrestore /var/lib/vz/dump/vzdump-qemu-101-YYYYMMDD-HHMMSS.vma.zst 101
```

---

## Monitoring Your Backups

### Check Git Backup Logs

**In Ubuntu VM:**

```bash
cat /home/homeadmin/backup.log
```

### Check Proxmox Backup Logs

**In Proxmox:**

```bash
cat /root/backup.log
```

### Check Available Backups

**In Proxmox:**

```bash
ls -lh /var/lib/vz/dump/ | grep 101
```

---

## Storage Considerations

### Git Backups (GitHub)
- **Size:** Small (< 10 MB typically)
- **Limit:** Free GitHub = unlimited private repos
- **Retention:** Forever (or until you delete)

### Proxmox Backups
- **Size:** ~5-10 GB per backup (compressed)
- **Limit:** Your Proxmox storage (you have 76 GB free on local)
- **Retention:** Keep 4 backups (auto-delete older ones)
- **Math:** 4 backups × 8 GB = ~32 GB used

You have plenty of space! ✅

---

## What You've Accomplished

✅ **Layer 1:** Daily Git backups to GitHub (automatic at 2 AM)
✅ **Layer 2:** Weekly full VM backups to Proxmox (automatic Sunday 3 AM)
✅ **Version control:** Track every config change
✅ **Disaster recovery:** Full system restoration capability
✅ **Peace of mind:** Your HA is now bulletproof! 🛡️

---

## Next Steps

1. **Complete Part A** (Git automation on Ubuntu VM)
2. **Complete Part B** (Proxmox VM backups)
3. **Test both systems**
4. **Relax** - your backups are automatic! ☕

**Ready to start? Begin with Part A, Step A1 in your Ubuntu VM console!**
