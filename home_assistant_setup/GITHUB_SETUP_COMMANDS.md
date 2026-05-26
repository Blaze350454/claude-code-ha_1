# GitHub Setup Commands - Ready to Execute

## Your Setup (Confirmed)
- **Username:** homeadmin
- **HA Config Location:** `/home/homeassistant/.config`
- **Git Version:** 2.43.0 ✅ (already installed)
- **Docker Compose:** `/home/homeadmin/homeassistant/docker-compose.yml`

---

## Step 1: Navigate to HA Config Directory

```bash
cd /home/homeassistant/.config
```

Check you're in the right place:
```bash
ls -la
```

You should see files like:
- `configuration.yaml`
- `automations.yaml`
- `.storage/` directory
- etc.

**Paste the output to confirm we're in the right spot.**

---

## Step 2: Initialize Git

```bash
# Initialize Git repository
git init

# Configure your Git identity
git config user.name "Your Name"
git config user.email "your-github-email@example.com"

# Check it worked
git config --list
```

**Replace "Your Name" and email with your actual info!**

---

## Step 3: Create .gitignore File (CRITICAL!)

This prevents secrets from being uploaded to GitHub.

```bash
nano .gitignore
```

**Copy and paste this entire list into nano:**

```gitignore
# Secrets and sensitive data
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
.cloud
.google.token

# Storage directory (except lovelace)
.storage/
!.storage/lovelace*

# Logs and databases
home-assistant.log
home-assistant_v2.db
ip_bans.yaml
known_devices.yaml

# Dependencies
deps/
tts/
__pycache__/
*.pyc

# Custom components
custom_components/**/

# Backup files
*.backup
*.bak
*.zip
*.tar

# Media files
*.jpg
*.jpeg
*.png
*.gif
www/

# Docker files (already in parent directory)
docker-compose.yml
Dockerfile
```

**To save in nano:**
1. Press `Ctrl + O` (WriteOut)
2. Press `Enter` (confirm filename)
3. Press `Ctrl + X` (Exit)

---

## Step 4: Create secrets.yaml.example Template

```bash
nano secrets.yaml.example
```

Paste this template:

```yaml
# secrets.yaml.example
# Copy this to secrets.yaml and fill in your actual values
# This template is safe to commit to GitHub

# Location
latitude: 00.0000
longitude: 00.0000
elevation: 0

# Example secrets (add your own)
# mqtt_password: your_password_here
# api_key: your_api_key_here
```

Save with `Ctrl + O`, `Enter`, `Ctrl + X`

---

## Step 5: Check What Will Be Committed

```bash
# Add all files
git add .

# See what Git found
git status
```

**IMPORTANT:** Look at the output! Make sure you DON'T see:
- ❌ `secrets.yaml`
- ❌ `.db` files
- ❌ `.log` files

If you see any of those, **STOP** and tell me!

---

## Step 6: Create Initial Commit

```bash
git commit -m "Initial commit - Home Assistant configuration"
```

---

## Step 7: Create GitHub Repository

**On GitHub.com:**

1. Go to https://github.com/new
2. Repository name: `homeassistant-config` (or whatever you want)
3. **IMPORTANT:** Set to **Private** ⚠️
4. **Do NOT** check "Add a README"
5. Click **Create repository**

**After creating, GitHub will show you commands. IGNORE THEM - use these instead:**

---

## Step 8: Link to GitHub and Push

```bash
# Add GitHub remote (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/homeassistant-config.git

# Check default branch name
git branch

# If it says "master", rename to "main"
git branch -M main

# Push to GitHub
git push -u origin main
```

**GitHub will ask for credentials:**
- **Username:** Your GitHub username
- **Password:** Use a **Personal Access Token** (NOT your GitHub password)

### Creating a Personal Access Token:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. Name: "Home Assistant Config"
4. Expiration: No expiration (or your choice)
5. Scopes: Check `repo` (all)
6. Generate token
7. **COPY THE TOKEN** - you won't see it again!
8. Use this as your "password" when pushing

---

## Step 9: Verify on GitHub

Go to your repository on GitHub and check:
- ✅ You see `configuration.yaml`
- ✅ You see `automations.yaml`
- ✅ You see `.gitignore`
- ✅ You see `secrets.yaml.example`
- ❌ You DON'T see `secrets.yaml`
- ❌ You DON'T see `.db` files

---

## Future Updates (Daily Workflow)

Whenever you make changes to HA:

```bash
cd /home/homeassistant/.config
git add .
git commit -m "Description of what you changed"
git push
```

---

## Optional: Also Version Control Docker Compose

```bash
cd /home/homeadmin/homeassistant
git init
nano .gitignore
```

Add to .gitignore:
```
*.env
.env
```

Then:
```bash
git add docker-compose.yml
git commit -m "Add docker compose configuration"
git remote add origin https://github.com/USERNAME/homeassistant-docker.git
git push -u origin main
```

---

## Ready to Start?

**Begin with Step 1 and work through each step.**
**Let me know when you complete each step or if you get stuck!**
