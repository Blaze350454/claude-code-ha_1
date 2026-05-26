# Home Assistant Backup - Container vs OS Explained

## Your Setup: Home Assistant Container

You're running **Home Assistant Container** (Docker on Ubuntu), which means:

❌ **What You DON'T Have:**
- No Supervisor
- No Settings → System → Backups menu
- No backup location selector
- No network storage options
- No add-ons (like automatic backup add-ons)

✅ **What You DO Have:**
- Direct access to your config files
- Full control over Ubuntu host
- Can use standard backup methods (Git, rsync, etc.)

---

## Home Assistant OS vs Container

### Home Assistant OS (HAOS)
- Full OS installation
- Has **Supervisor** built-in
- Settings → System → **Backups** menu exists
- Can configure backup locations (network storage, NAS, etc.)
- Can install backup add-ons
- Automatic scheduled backups via UI

### Home Assistant Container (Your Setup)
- Docker container on Ubuntu
- **No Supervisor** = No backup UI
- No Settings → System → Backups
- Must use manual backup methods
- More control, but more DIY

---

## Your Backup Options (Container)

Since you don't have the built-in backup system, here are your options:

### Option 1: Git + GitHub (What We Just Set Up) ✅ RECOMMENDED
**Pros:**
- Version control - see what changed and when
- Easy to restore specific files
- Free (for private repos)
- Already working!

**Cons:**
- Only backs up config files, not database/media
- Manual unless you set up cron

**What it backs up:**
- ✅ configuration.yaml
- ✅ automations.yaml
- ✅ scripts, scenes, themes
- ✅ custom_components
- ❌ Database (.db files)
- ❌ Media files
- ❌ Add-on configs (you don't have add-ons)

### Option 2: Automated Git Backups (Cron Job)
**What we were about to set up:**
- Runs every night at 2 AM
- Automatically commits and pushes to GitHub
- Logs success/failures

**Commands:**
```bash
# Create backup script
nano /home/homeadmin/backup-ha.sh

# Add to cron for automatic daily backups
crontab -e
```

### Option 3: Full System Backups (Ubuntu level)
**Backup entire Ubuntu VM from Proxmox:**

From Proxmox:
```bash
# Backup entire VM 101 (includes everything)
vzdump 101 --compress zstd --storage local
```

**Pros:**
- Complete system backup
- Includes database, media, everything

**Cons:**
- Large file size
- Slower to restore
- Takes more space

### Option 4: Docker Volume Backups
**Backup the Docker volumes:**

```bash
# Find your HA volume
sudo docker inspect homeassistant | grep -A 10 Mounts

# Backup the volume
sudo tar -czf ha-backup-$(date +%Y%m%d).tar.gz /home/homeadmin/homeassistant/config
```

### Option 5: Rsync to NAS/Network Storage
**Sync to a network location:**

```bash
# Install rsync
sudo apt install rsync

# Sync to NAS (example)
rsync -av /home/homeadmin/homeassistant/config/ user@nas:/backups/homeassistant/
```

---

## Recommended Multi-Layer Backup Strategy

### Layer 1: Git + GitHub (Daily - Config Only) ✅
- What: Config files version control
- When: Automatic daily at 2 AM
- Where: GitHub (private repo)
- **Status:** Already set up! Just need to add cron

### Layer 2: Full VM Backup (Weekly - Everything)
- What: Complete VM snapshot from Proxmox
- When: Weekly
- Where: Proxmox local storage
- **How:**
  ```bash
  # From Proxmox shell
  vzdump 101 --compress zstd --storage local
  ```

### Layer 3: Off-site Backup (Monthly - Disaster Recovery)
- What: Copy of VM backup to external location
- When: Monthly
- Where: External drive or cloud storage

---

## What Should You Do?

**My Recommendation:**

1. **✅ Keep Git + GitHub** (already done!)
   - Best for config tracking and quick restores

2. **✅ Add Cron Job** (5 minutes to set up)
   - Automatic daily config backups to GitHub

3. **✅ Set up Proxmox VM Backup** (optional but recommended)
   - Weekly full VM backup for complete disaster recovery

You **cannot** use the Settings → System → Backups feature because that requires Home Assistant OS with Supervisor, which you don't have with Container installation.

---

## Do You Want to Continue with Cron Setup?

The cron job will:
- Run every night at 2 AM
- Check for config changes
- Auto-commit and push to GitHub
- Log results

**It takes 5 minutes to set up and runs automatically forever!**

Or would you prefer to:
- Stick with manual Git backups (run commands when you make changes)
- Set up Proxmox VM backups instead
- Do both

---

**Let me know what you'd like to do!**
