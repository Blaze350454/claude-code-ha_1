# GitHub Integration Plan - Home Assistant Container

## Your Setup (Confirmed)

**VM 101 - Ubuntu + Docker**
- Ubuntu OS
- Docker Container: Home Assistant
- Docker Container: Matter Server
- IP: 192.168.2.151
- **Installation Type:** Home Assistant Container (NOT HAOS)

**Important:** Since you're running Home Assistant Container (not Home Assistant OS), you:
- ❌ **Cannot** use Supervisor add-ons (Git Pull, SSH, etc.)
- ✅ **Can** use standard Git directly on Ubuntu
- ✅ **Have** full control over the OS

## GitHub Integration Strategy

We'll set up Git directly on your Ubuntu VM to push/pull your HA configuration.

### Phase 1: Access Ubuntu VM
First, we need SSH access to your Ubuntu VM (192.168.2.151).

**Option A: SSH from Proxmox**
```bash
# From Proxmox shell
ssh user@192.168.2.151
```

**Option B: Proxmox Console**
- In Proxmox web UI → VM 101 → Console
- Login with your Ubuntu credentials

### Phase 2: Locate HA Config Directory

Your HA config is likely in one of these locations:
- `/opt/homeassistant/config` (common)
- `/home/user/homeassistant` (if using compose)
- Check your docker-compose.yml or docker run command

### Phase 3: Install Git on Ubuntu VM

```bash
# Update packages
sudo apt update

# Install Git
sudo apt install git -y

# Verify installation
git --version
```

### Phase 4: Create GitHub Repository

1. Go to GitHub.com
2. Create new repository (e.g., `homeassistant-config`)
3. **IMPORTANT:** Make it **Private** (contains sensitive data)
4. Don't initialize with README (we'll push existing files)

### Phase 5: Configure Git in HA Config Directory

```bash
# Navigate to HA config directory
cd /path/to/homeassistant/config

# Initialize Git
git init

# Configure Git user
git config user.name "Your Name"
git config user.email "your-email@example.com"

# Create .gitignore (critical!)
```

### Phase 6: Create .gitignore File

**Critical:** You MUST ignore sensitive files!

```bash
# Create .gitignore
nano .gitignore
```

Paste this (verified from HA documentation):

```gitignore
# Secrets
secrets.yaml
*.db
*.db-shm
*.db-wal
*.log
*.sqlite

# Temporary files
*.pid
*.xml
*.csr
*.crt
*.key
OZW_Log.txt
._*
.DS_Store
.uuid
.HA_VERSION
.storage/
.cloud
.google.token

# Ignore all of .storage except for things we want
!.storage/lovelace*

# Specific directories to ignore
home-assistant.log
home-assistant_v2.db
ip_bans.yaml
known_devices.yaml
deps/
tts/
__pycache__/
*.pyc

# Custom component dependencies
custom_components/**/

# Backup files
*.backup
*.bak

# Image/media files
*.jpg
*.jpeg
*.png
*.gif
www/
```

### Phase 7: Initial Commit and Push

```bash
# Add files (respecting .gitignore)
git add .

# Check what will be committed
git status

# Create initial commit
git commit -m "Initial commit - Home Assistant configuration"

# Add GitHub remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/homeassistant-config.git

# Push to GitHub
git push -u origin main
```

### Phase 8: Set Up SSH Keys (Recommended)

For easier push/pull without passwords:

```bash
# Generate SSH key (on Ubuntu VM)
ssh-keygen -t ed25519 -C "your-email@example.com"

# Display public key
cat ~/.ssh/id_ed25519.pub
```

Copy the public key and add to GitHub:
1. GitHub → Settings → SSH and GPG keys
2. New SSH key → Paste key

Then update remote:
```bash
git remote set-url origin git@github.com:yourusername/homeassistant-config.git
```

## Daily Workflow

### Push Changes to GitHub
```bash
cd /path/to/homeassistant/config
git add .
git commit -m "Description of changes"
git push
```

### Pull Changes from GitHub
```bash
cd /path/to/homeassistant/config
git pull
```

### Automated Commits (Optional)

Create a cron job to auto-commit daily:

```bash
# Edit crontab
crontab -e

# Add this line (commits at 2 AM daily)
0 2 * * * cd /path/to/homeassistant/config && git add -A && git commit -m "Auto backup $(date)" && git push
```

## Important Files to Version Control

✅ **Should commit:**
- `configuration.yaml`
- `automations.yaml`
- `scripts.yaml`
- `scenes.yaml`
- Custom component configs
- Blueprints
- Themes
- Lovelace dashboards

❌ **Should NOT commit:**
- `secrets.yaml`
- `.storage/` (except lovelace)
- Database files (*.db)
- Log files
- SSL certificates
- Tokens/API keys

## Secrets Management

For `secrets.yaml`:

1. Create `secrets.yaml.example`:
```yaml
# secrets.yaml.example - Template for secrets
# Copy to secrets.yaml and fill in real values

latitude: 00.0000
longitude: 00.0000
mqtt_password: your_password_here
api_key: your_api_key_here
```

2. Commit the example, not the real secrets:
```bash
git add secrets.yaml.example
git commit -m "Add secrets template"
```

## Docker Compose Considerations

If using docker-compose:

```bash
# Also version control your compose file
git add docker-compose.yml
git commit -m "Add docker compose configuration"
```

## Next Steps

1. **Get SSH access** to Ubuntu VM (192.168.2.151)
2. **Find your HA config directory**
3. **Install Git** on Ubuntu
4. **Create GitHub repo** (private!)
5. **Follow Phase 6-7** to initialize and push

## Questions to Answer

Before we start:
1. What's your Ubuntu username?
2. Do you have SSH access to the VM?
3. Where is your HA config located? (check docker-compose.yml or docker run command)

---

**Ready to start? Let me know and we'll go step-by-step!**
